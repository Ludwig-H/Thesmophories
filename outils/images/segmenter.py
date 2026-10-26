#!/usr/bin/env python3
"""Segmentation des pages du Ravennas (ff. 162v–177r) : colonne du texte, lignes,
blocs de scholies marginales, boîte englobante de l'écriture.

Sortie : ravennas/segmentation/fXXX.json (une page par fichier) ;
avec --debug, une vue annotée réduite dans .travail/segmentation_debug/fXXX.jpg.
Usage : python3 outils/images/segmenter.py [--pages f162v f163r ...] [--debug] [-j 8]

Méthode (détails, paramètres et limites : ravennas/segmentation/README.md) :
 1. masque d'encre (masque_encre de recadrer_facsimile.py) ; composantes connexes ;
    filtre « écriture » : taille, contraste du trait avec le fond local, élongation
    (stries des tranches et des bords de reliure), pas de contact avec le bord ;
 2. inclinaison globale (netteté du profil de projection horizontal sur une plage
    d'angles) et pas de ligne (autocorrélation du profil) ;
 3. colonne principale : bandes verticales dont le profil est périodique au pas du
    texte (les scholies, plus serrées, ont un autre pas) ;
 4. lignes : pics du profil de projection redressé dans la partie gauche de la
    colonne (où commencent toutes les lignes, même lyriques), puis pour chaque ligne
    chaînage des composantes de sa bande vers la droite et vers la gauche (écart
    maximal entre mots), droite d'ajustement robuste (pente locale) ; les lignes
    serrées sont séparées par attribution de chaque composante au centre de ligne le
    plus proche ; les marges verticales sont réduites quand les lignes se serrent ;
 5. lignes « de colonne » : suite la plus longue de lignes à l'écriture de module
    normal ; les lignes de petit module au-dessus ou au-dessous (hypothèse, scholies)
    sont rendues aux blocs marginaux ;
 6. blocs marginaux : composantes restantes regroupées par dilatation, filtrées
    (contraste, structure en lignes) ; petits blocs contigus à une ligne = sigle
    (à gauche) ou glose (à droite) ; lignes de chaque bloc par profil de projection ;
 7. boîte englobante de l'écriture : colonne + blocs retenus (croissance de région
    à partir de la colonne) + numéro de folio (coin supérieur externe des rectos).
Des corrections manuelles se mettent dans ravennas/segmentation/corrections.json.
"""
import argparse, glob, json, os, re, sys
from multiprocessing import Pool

import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from scipy import ndimage as ndi
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks
from skimage.morphology import skeletonize

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from recadrer_facsimile import masque_encre  # noqa: E402

RACINE = os.path.dirname(os.path.dirname(ICI))
SRC = os.path.join(RACINE, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
DST = os.path.join(RACINE, 'ravennas', 'segmentation')
CORR = os.path.join(DST, 'corrections.json')
DEBUG = os.path.join(RACINE, '.travail', 'segmentation_debug')

P = dict(
    aire_min=10,              # aire minimale d'une composante « écriture » (px)
    h_max=85, w_max=260,      # dimensions maximales d'une composante
    aire_max=4000,
    contraste_max_min=52,     # contraste maximal minimal (fond local − luminance)
    contraste_moy_min=34,     # contraste moyen minimal
    strie_moy_max=50,         # stries (h ≥ 2,5 w ou w ≥ 4 h) : contraste moyen < 50 → rejet
    angles=(-3.0, 3.0, 0.05), # plage d'inclinaisons testées (degrés)
    pas_min=30, pas_max=70,   # plage du pas de ligne (px)
    bande=80, pas_bande=40,   # bandes verticales (détection de la colonne)
    ac_colonne=0.30,          # autocorrélation minimale au pas du texte
    graine=450,               # largeur de la zone gauche de la colonne où l'on cherche les lignes
    ecart_droite=1.4,         # écart maximal entre mots (en pas) pour le chaînage à droite
    ecart_gauche=0.9,         # idem à gauche
    demi_bande=0.45,          # demi-hauteur de la bande d'une ligne (en pas)
    llr_seuil_d=6.0, llr_seuil_g=3.0,  # coupure gloses/scholies (à droite, à gauche) : LLR minimal
    llr_moy_d=0.6,            # à droite : LLR moyen minimal de la partie coupée
    echelle_scholies=0.65,    # module de la petite écriture par défaut (rel. au texte)
    score_min=-0.30,          # retranchement des lignes marginales (voir selection_colonne)
    score_bas=-0.15,
    saut_max=2.6,             # interligne maximal à l'intérieur de la colonne (en pas)
    sigle=100,                # largeur de la zone des sigles à gauche de la colonne (px)
    marge_haut=0.75, marge_bas=0.55,  # marges verticales des boîtes de ligne (en pas)
    bloc_noyau=(41, 25),      # dilatation pour regrouper les blocs marginaux
    bloc_cmax_med=68, bloc_cmoy_med=45,  # contraste médian minimal d'un bloc
    croissance=170,           # distance maximale d'un bloc à la zone écrite (px)
    croissance_petit=60,      # idem pour un petit bloc (< 5 lettres)
    bloc_cmoy_lettre=42,      # contraste moyen minimal d'une « lettre » pour former un bloc
    bord_seuil=1.2,           # intérieur de la page : rapport maximal des gradients vertical/horizontal
)


# ----------------------------------------------------------------------------
# utilitaires

def folio_de(nom):
    return re.search(r'_(f\d+[rv])_', nom).group(1)


def vers_de(nom):
    m = re.search(r'_vv(\d+)-(\d+)', nom)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def profil(ys, poids, n, sigma):
    """Profil 1D lissé (histogramme pondéré de positions)."""
    ys = np.round(np.asarray(ys)).astype(int)
    ok = (ys >= 0) & (ys < n)
    p = np.bincount(ys[ok], weights=None if poids is None else np.asarray(poids, float)[ok], minlength=n).astype(float)
    return gaussian_filter1d(p, sigma) if sigma > 0 else p


def boite_de(C, ids):
    ids = np.asarray(ids, int)
    return [int(C['x'][ids].min()), int(C['y'][ids].min()),
            int((C['x'][ids] + C['w'][ids]).max()), int((C['y'][ids] + C['h'][ids]).max())]


def union(b1, b2):
    if b1 is None:
        return list(b2)
    if b2 is None:
        return list(b1)
    return [min(b1[0], b2[0]), min(b1[1], b2[1]), max(b1[2], b2[2]), max(b1[3], b2[3])]


def distance_boites(b1, b2):
    dx = max(0, b1[0] - b2[2], b2[0] - b1[2])
    dy = max(0, b1[1] - b2[3], b2[1] - b1[3])
    return max(dx, dy)


# ----------------------------------------------------------------------------
# 1. composantes

def composantes(im):
    ink, lum = masque_encre(im)
    fond = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(np.float32)
    contr = fond - lum
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink.astype(np.uint8), connectivity=8)
    H, W = ink.shape
    x, y, w, h, a = (st[:, k].astype(int) for k in range(5))
    cmax = np.zeros(n); cmoy = np.zeros(n)
    sel = np.where(a >= P['aire_min'])[0]
    sel = sel[sel > 0]
    if len(sel):
        cmax[sel] = ndi.maximum(contr, lab, sel)
        cmoy[sel] = ndi.mean(contr, lab, sel)
    bord = (x <= 1) | (y <= 1) | (x + w >= W - 1) | (y + h >= H - 1)
    strie = (((h >= 2.5 * w) & (h >= 15)) | ((w >= 4 * h) & (w >= 15))) & (cmoy < P['strie_moy_max'])
    texte = ((a >= P['aire_min']) & (h <= P['h_max']) & (w <= P['w_max']) & (a <= P['aire_max'])
             & ~bord & ~strie & (cmax >= P['contraste_max_min']) & (cmoy >= P['contraste_moy_min']))
    texte[0] = False
    # caractéristiques de l'écriture : log aire, log hauteur, épaisseur du trait
    # (aire / longueur du squelette), pour les composantes d'aire ≥ 25
    f = np.full((n, 3), np.nan)
    sel = np.where(texte & (a >= 25))[0]
    if len(sel):
        sk = skeletonize(ink)
        lsq = ndi.sum(sk, lab, sel)
        f[sel, 0] = np.log(a[sel]); f[sel, 1] = np.log(h[sel])
        f[sel, 2] = a[sel] / np.maximum(lsq, 1)
    C = dict(n=n, lab=lab, x=x, y=y, w=w, h=h, a=a, cx=cen[:, 0], cy=cen[:, 1],
             cmax=cmax, cmoy=cmoy, texte=texte, f=f)
    return ink, lum, C


# ----------------------------------------------------------------------------
# 2. inclinaison et pas

def inclinaison_pas(C, W, H, zone=None):
    """Inclinaison globale (degrés ; y' = y − tan(a)·(x − W/2)) et pas de ligne."""
    t = C['texte']
    if zone is not None:
        x0, x1, y0, y1 = zone
        t = t & (C['cx'] >= x0) & (C['cx'] <= x1) & (C['cy'] >= y0) & (C['cy'] <= y1)
    else:
        t = t & (C['cx'] > 0.2 * W) & (C['cx'] < 0.8 * W) & (C['cy'] > 0.08 * H) & (C['cy'] < 0.92 * H)
    ids = np.where(t)[0]
    if len(ids) < 50:
        return 0.0, 45.0, 0.0
    m = np.zeros(C['n'], bool); m[ids] = True
    ys, xs = np.nonzero(m[C['lab']])
    best = (-1, 0.0)
    a0, a1, da = P['angles']
    for ang in np.arange(a0, a1 + 1e-9, da):
        tt = np.tan(np.radians(ang))
        pr = profil(ys - tt * (xs - W / 2) + 200, None, H + 400, 2)
        s = (np.diff(pr) ** 2).sum()
        if s > best[0]:
            best = (s, ang)
    ang = best[1]
    tt = np.tan(np.radians(ang))
    pr = profil(ys - tt * (xs - W / 2) + 200, None, H + 400, 2)
    p = pr - pr.mean()
    ac = np.correlate(p, p, 'full')[len(p) - 1:]
    ac /= ac[0]
    lo, hi = P['pas_min'], P['pas_max']
    k = int(np.argmax(ac[lo:hi])) + lo
    d = ac[k - 1] - 2 * ac[k] + ac[k + 1]
    kf = k + (0.5 * (ac[k - 1] - ac[k + 1]) / d if d != 0 else 0)
    return float(ang), float(kf), float(ac[k])


def redresser(x, y, ang, W):
    return y - np.tan(np.radians(ang)) * (x - W / 2)


# ----------------------------------------------------------------------------
# 3. colonne (approximation)

def colonne_grossiere(C, W, H, ang, pas):
    """Bandes verticales dont le profil est périodique au pas du texte."""
    t = np.where(C['texte'])[0]
    cx, cy, a = C['cx'][t], C['cy'][t], C['a'][t]
    yr = redresser(cx, cy, ang, W) + 200
    res = []
    b, sb = P['bande'], P['pas_bande']
    lag = int(round(pas))
    for x0 in range(0, W - b + 1, sb):
        s = (cx >= x0) & (cx < x0 + b)
        if a[s].sum() < 1500:
            res.append((x0, 0.0))
            continue
        pr = profil(yr[s], a[s], H + 400, 3)
        p = pr - pr.mean()
        ac = np.correlate(p, p, 'full')[len(p) - 1:]
        ac /= ac[0]
        res.append((x0, float(ac[max(lag - 3, 1):lag + 4].max())))
    ok = [r[1] >= P['ac_colonne'] for r in res]
    best, cur = None, None
    for i, o in enumerate(ok):
        if o:
            if cur is None or i - cur[1] > 2:
                cur = [i, i]
            else:
                cur[1] = i
            if best is None or (cur[1] - cur[0]) > (best[1] - best[0]):
                best = list(cur)
    if best is None:
        return int(0.25 * W), int(0.75 * W)
    return int(res[best[0]][0]), int(res[best[1]][0] + b)


# ----------------------------------------------------------------------------
# 4. lignes

def pics_lignes(C, W, H, ang, pas, x0, x1, ids=None):
    """Centres de lignes (y redressé) : pics du profil de projection pondéré par l'aire."""
    if ids is None:
        ids = np.where(C['texte'])[0]
    t = ids[(C['cx'][ids] >= x0) & (C['cx'][ids] <= x1)]
    if len(t) == 0:
        return []
    yr = redresser(C['cx'][t], C['cy'][t], ang, W)
    off = 200
    pr = profil(yr + off, C['a'][t], H + 2 * off, max(pas / 7, 2))
    if not (pr > 0).any():
        return []
    pics, _ = find_peaks(pr, distance=max(int(0.55 * pas), 5), prominence=0.10 * np.percentile(pr[pr > 0], 99))
    return [float(p - off) for p in pics]


def ajuster(C, ids, ang, W, lim_deg=0.8):
    """Droite y = a + b·x (moindres carrés pondérés par l'aire, pente bornée)."""
    ids = np.asarray(ids, int)
    x = C['cx'][ids]; y = C['cy'][ids]; w = C['a'][ids].astype(float)
    tt = np.tan(np.radians(ang))
    b = tt
    if len(ids) >= 5 and (x.max() - x.min()) >= 150:
        A = np.vstack([np.ones_like(x), x]).T * np.sqrt(w)[:, None]
        sol, *_ = np.linalg.lstsq(A, y * np.sqrt(w), rcond=None)
        lim = np.tan(np.radians(lim_deg))
        b = float(np.clip(sol[1], tt - lim, tt + lim))
    a0 = float(np.average(y - b * x, weights=w))
    return a0, float(b)


def mots(C, idx, xs, xe, ecart):
    """Regroupe des composantes (triées par x) en mots : écart > ecart entre mots."""
    out, cur, fin = [], [], None
    for j in idx:
        if cur and xs[j] - fin > ecart:
            out.append(cur); cur = []
        cur.append(j)
        fin = xe[j] if fin is None or len(cur) == 1 else max(fin, xe[j])
    if cur:
        out.append(cur)
    return out


BINS_A = np.linspace(np.log(25), np.log(1500), 17)   # log aire
BINS_H = np.linspace(np.log(5), np.log(60), 13)      # log hauteur


def densite(f):
    """Densité lissée (histogramme 2D log aire × log hauteur)."""
    hst, _, _ = np.histogram2d(f[:, 0], f[:, 1], bins=[BINS_A, BINS_H])
    hst = ndi.gaussian_filter(hst, 0.8) + 0.02
    return np.log(hst / hst.sum())


def llr(C, ids, modele):
    """Log-rapport de vraisemblance « petite écriture (scholies, gloses) / écriture du
    texte » de chaque composante (densités 2D lissées en log aire × log hauteur) ;
    0 pour les composantes d'aire < 25 (points, accents)."""
    ids = np.asarray(ids, int)
    f = C['f'][ids]
    ok = np.isfinite(f).all(1)
    out = np.zeros(len(ids))
    if modele is None or not ok.any():
        return out
    ia = np.clip(np.digitize(f[ok, 0], BINS_A) - 1, 0, len(BINS_A) - 2)
    ih = np.clip(np.digitize(f[ok, 1], BINS_H) - 1, 0, len(BINS_H) - 2)
    out[ok] = modele['ls'][ia, ih] - modele['lm'][ia, ih]
    return out


def occupation(C, ids, a0, b, pas, W):
    """Occupation horizontale (booléens de longueur W) de la bande centrale d'une ligne
    (± 0,25 pas autour de la droite y = a0 + b·x) par les composantes données, qu'elles
    soient ou non attribuées à la ligne : une grande lettre de la ligne voisine qui
    traverse la bande fait pont et n'interrompt pas le chaînage."""
    ids = np.asarray(ids, int)
    yl = a0 + b * C['cx'][ids]
    s = ids[(C['y'][ids] <= yl + 0.25 * pas) & (C['y'][ids] + C['h'][ids] >= yl - 0.25 * pas)]
    occ = np.zeros(W + 1, np.int32)
    np.add.at(occ, np.clip(C['x'][s], 0, W), 1)
    np.add.at(occ, np.clip(C['x'][s] + C['w'][s], 0, W), -1)
    return np.cumsum(occ)[:W] > 0


def chainer(C, cand, graine, pas, modele, gauche=True, occ=None):
    """Chaîne des composantes d'une ligne à partir de la zone graine.

    1. À droite : on étend la ligne tant que l'écart entre deux parties écrites de la
       bande est ≤ ecart_droite·pas (l'occupation `occ` compte aussi les composantes
       des lignes voisines qui traversent la bande) ; à gauche (si demandé) : idem avec
       ecart_gauche·pas.
    2. Coupure : les gloses et scholies voisines (souvent à quelques pixels de la fin
       ou du début du vers) sont écartées par détection de rupture : on cherche, parmi
       les espaces entre composantes, le point de coupure qui maximise la somme des
       log-rapports « petite écriture / texte » (fonction llr) de la partie extérieure ;
       on coupe si ce maximum dépasse le seuil (llr_seuil_d, llr_seuil_g)."""
    if len(cand) == 0:
        return []
    o = np.argsort(C['x'][cand])
    cand = cand[o]
    xs = C['x'][cand]; xe = xs + C['w'][cand]; cx = C['cx'][cand]
    dans = np.where((cx >= graine[0]) & (cx <= graine[1]))[0]
    if len(dans) == 0:
        return []
    Wd = len(occ) if occ is not None else int(xe.max()) + 1
    if occ is None:
        occ = np.zeros(Wd, bool)
    occ = occ.copy()
    for j in range(len(cand)):
        occ[max(0, xs[j]):min(Wd, xe[j])] = True
    pris = set(dans.tolist())
    g_d, g_g = int(P['ecart_droite'] * pas), int(P['ecart_gauche'] * pas)

    # à droite : fin de la partie écrite continue (écarts ≤ g_d)
    fin = int(xe[dans].max())
    while True:
        nz = np.flatnonzero(occ[fin:min(Wd, fin + g_d + 1)])
        if len(nz) == 0:
            break
        k = fin + nz[0]
        z = np.flatnonzero(~occ[k:])
        nf = k + (z[0] if len(z) else Wd - k)
        if nf <= fin:
            break
        fin = nf
    droite = [j for j in range(dans.max() + 1, len(cand)) if j not in pris and xs[j] <= fin]
    if modele is not None and droite:
        v = llr(C, cand[droite], modele)
        queue = np.cumsum(v[::-1])[::-1]
        nq = np.cumsum((v != 0)[::-1])[::-1]
        best_q, best = None, P['llr_seuil_d']
        for q in range(len(droite)):
            xq = xs[droite[q]]
            ecart = xq - max([xe[j] for j in list(dans) + droite[:q]])
            if ecart >= 0.1 * pas and queue[q] > best and nq[q] >= 4 and queue[q] / nq[q] >= P['llr_moy_d']:
                best, best_q = queue[q], q
        if best_q is not None:
            droite = droite[:best_q]
    pris.update(droite)
    if not gauche:
        return cand[sorted(pris)].tolist()

    # à gauche
    deb = int(min(xs[j] for j in pris))
    while True:
        nz = np.flatnonzero(occ[max(0, deb - g_g - 1):deb])
        if len(nz) == 0:
            break
        k = max(0, deb - g_g - 1) + nz[-1]
        z = np.flatnonzero(~occ[:k + 1])
        nd = (z[-1] + 1) if len(z) else 0
        if nd >= deb:
            break
        deb = nd
    cg = [j for j in range(len(cand)) if j not in pris and xe[j] <= min(xs[i] for i in pris) + 0.3 * pas and xs[j] >= deb]
    cg.sort(key=lambda j: -xe[j])
    if modele is not None and cg:
        v = llr(C, cand[cg], modele)
        tete = np.cumsum(v[::-1])[::-1]
        best_q, best = None, P['llr_seuil_g']
        d0 = min(xs[i] for i in pris)
        for q in range(len(cg)):
            ecart = min([d0] + [xs[j] for j in cg[:q]]) - xe[cg[q]]
            if ecart >= 0 and tete[q] > best:
                best, best_q = tete[q], q
        if best_q is not None:
            cg = cg[:best_q]
    pris.update(cg)
    return cand[sorted(pris)].tolist()


def modele_ecritures(C, lignes, graine, L0, R0, page):
    """Densités de l'écriture du texte (composantes des lignes dans la zone graine) et
    de la petite écriture : composantes hors de la colonne approchée si elles sont
    assez nombreuses, sinon écriture du texte réduite d'un facteur echelle_scholies."""
    ids = np.array([k for li in lignes for k in li['ids']], int)
    ids = ids[(C['a'][ids] >= 25) & (C['cx'][ids] >= graine[0] + 30) & (C['cx'][ids] <= graine[1])]
    fm = C['f'][ids]; fm = fm[np.isfinite(fm).all(1)]
    if len(fm) < 30:
        return None
    t = np.where(C['texte'] & (C['a'] >= 25) & ((C['cx'] < L0 - 60) | (C['cx'] > R0 + 60)))[0]
    fs = C['f'][t]; fs = fs[np.isfinite(fs).all(1)]
    source = 'marges'
    if len(fs) < 150:
        k = P['echelle_scholies']
        fs = fm.copy(); fs[:, 0] += 2 * np.log(k); fs[:, 1] += np.log(k)
        source = 'texte réduit'
    return dict(lm=densite(fm), ls=densite(fs), n_m=len(fm), n_s=len(fs), source=source)


def module_texte(C, lignes, x0, x1):
    """Module de l'écriture du texte : 80e centile des hauteurs et aire médiane des
    composantes (aire ≥ 25) des lignes de la colonne, dans [x0, x1]."""
    ids = np.array([k for li in lignes for k in li['ids']], int)
    if len(ids) == 0:
        return 28.0, 150.0
    s = ids[(C['a'][ids] >= 25) & (C['cx'][ids] >= x0) & (C['cx'][ids] <= x1)]
    if len(s) < 20:
        s = ids[C['a'][ids] >= 25]
    return float(np.percentile(C['h'][s], 80)), float(np.median(C['a'][s]))


def lignes_colonne(C, W, H, ang, pas, L0, R0, ref=None):
    """Lignes de la colonne : pics du profil dans la zone graine, puis pour chaque
    ligne : chaînage vers la droite, droite ajustée, second chaînage dans la bande de
    la droite ajustée, enfin extension vers la gauche (sigles, débuts de vers en
    saillie) sans réajustement (pour que des scholies voisines ne faussent pas la pente)."""
    graine = (L0 + 20, min(L0 + P['graine'], R0))
    centres = pics_lignes(C, W, H, ang, pas, *graine)
    t = np.where(C['texte'])[0]
    yr = redresser(C['cx'][t], C['cy'][t], ang, W)
    centres = np.array(sorted(centres))
    if len(centres) == 0:
        return []
    tt = np.tan(np.radians(ang))
    # attribution au centre le plus proche (séparation des lignes serrées)
    k = np.abs(yr[:, None] - centres[None, :]).argmin(1)
    dy = yr - centres[k]
    lignes = []
    for i, c in enumerate(centres):
        cand = t[(k == i) & (np.abs(dy) <= P['demi_bande'] * pas)]
        a0, b = c - tt * (-W / 2), tt          # droite initiale : y = c + tt·(x − W/2)
        occ = occupation(C, t, a0, b, pas, W)
        ch = chainer(C, cand, graine, pas, ref, gauche=False, occ=occ)
        if len(ch) < 2:
            continue
        a0, b = ajuster(C, ch, ang, W)
        # second passage dans la bande de la droite ajustée (pente locale)
        d2 = C['cy'][t] - (a0 + b * C['cx'][t])
        cand2 = t[(np.abs(d2) <= P['demi_bande'] * pas) & ((k == i) | (np.abs(d2) < np.abs(dy)))]
        occ = occupation(C, t, a0, b, pas, W)
        ch2 = chainer(C, cand2, graine, pas, ref, gauche=False, occ=occ)
        if len(ch2) >= 2:
            a0, b = ajuster(C, ch2, ang, W)
            cand = cand2
            occ = occupation(C, t, a0, b, pas, W)
        ch = chainer(C, cand, graine, pas, ref, gauche=True, occ=occ)
        lignes.append(dict(c=float(c), ids=list(ch), a=a0, b=b))
    return lignes


def module(C, ids, x0, x1):
    """Module d'une ligne : (80e centile des hauteurs, aire médiane) des composantes
    d'aire ≥ 25 situées dans [x0, x1] (à défaut, de toute la ligne)."""
    ids = np.asarray(ids, int)
    s = ids[(C['a'][ids] >= 25) & (C['cx'][ids] >= x0) & (C['cx'][ids] <= x1)]
    if len(s) < 3:
        s = ids[C['a'][ids] >= 25]
    if len(s) == 0:
        return 1.0, 1.0
    return float(np.percentile(C['h'][s], 80)), float(np.median(C['a'][s]))


def selection_colonne(C, lignes, pas, graine):
    """Lignes de la colonne : groupe principal de lignes (interligne ≤ saut_max·pas),
    dont on retranche aux extrémités les lignes de petit module (hypothèse, scholies
    des marges supérieure et inférieure).

    Module d'une ligne : 80e centile des hauteurs de ses composantes (aire ≥ 25) dans
    la zone graine ; score = log(module / médiane des modules). On retranche à chaque
    extrémité les k lignes consécutives de score < score_bas si leur score moyen est
    < score_min et si k ≥ 2, ou si la ligne est isolée (interligne ≥ 1,4 pas), ou si
    son score est très bas (< 2·score_min)."""
    if not lignes:
        return lignes, []
    zone = (graine[0] + 30, graine[1])
    mods = [module(C, li['ids'], *zone)[0] for li in lignes]
    med = np.median(mods)
    score = []
    for li, h80 in zip(lignes, mods):
        li['module'] = round(h80, 1)
        li['score'] = round(float(np.log(max(h80, 1) / med)), 2)
        score.append(li['score'])
    score = np.array(score)
    cs = np.array([li['c'] for li in lignes])
    groupes, cur = [], [0]
    for i in range(1, len(lignes)):
        if cs[i] - cs[i - 1] > P['saut_max'] * pas:
            groupes.append(cur); cur = []
        cur.append(i)
    groupes.append(cur)
    g = max(groupes, key=lambda gr: ((score[gr] >= P['score_bas']).sum(), len(gr)))

    def a_retrancher(idx):
        sc = score[idx]
        k = 0
        while k < len(sc) - 1 and sc[k] < P['score_bas']:
            k += 1
        while k > 0:
            ecart = abs(cs[idx[1]] - cs[idx[0]]) / pas if len(idx) > 1 else 9
            if sc[:k].mean() < P['score_min'] and (k >= 2 or ecart >= 1.4 or sc[0] < 2 * P['score_min']):
                break
            k -= 1
        return k

    k = a_retrancher(g)
    g = g[k:]
    k = a_retrancher(g[::-1])
    g = g[:len(g) - k]
    gs = set(g)
    return [li for i, li in enumerate(lignes) if i in gs], [li for i, li in enumerate(lignes) if i not in gs]


def gauche_colonne(C, lignes):
    """Bord gauche du texte : histogramme des débuts de ligne (pas de 8 px, lissé) ;
    on retient le pic le plus à gauche dont la hauteur atteint 35 % du pic principal
    (les vers lyriques en retrait forment un pic à droite, les sigles chaînés sont
    dispersés à gauche)."""
    deb = np.array([C['x'][np.asarray(li['ids'])].min() for li in lignes])
    if len(deb) == 0:
        return None
    if len(deb) < 5:
        return int(np.median(deb))
    x0 = deb.min() - 40
    h = np.bincount(((deb - x0) // 8).astype(int), minlength=int((deb.max() - x0) // 8) + 6).astype(float)
    h = gaussian_filter1d(h, 1.5)
    pics, _ = find_peaks(np.concatenate([[0], h, [0]]))
    pics = pics - 1
    if len(pics) == 0:
        return int(np.median(deb))
    hmax = h[pics].max()
    ok = [q for q in pics if h[q] >= 0.35 * hmax]
    q = min(ok)
    centre = x0 + 8 * q + 4
    proches = deb[np.abs(deb - centre) <= 20]
    return int(np.percentile(proches, 20)) if len(proches) else int(centre)


# ----------------------------------------------------------------------------
# 5. intérieur de la page (exclut tranches, reliure, mire, page voisine)

def interieur_page(im):
    """Boîte de la page : on écarte, sur les bords, les zones où dominent les contours
    verticaux (tranches des feuillets, bord de la reliure) ou horizontaux (haut et bas
    de la reliure). Rapport des gradients |dI/dx| / |dI/dy| moyennés sur la bande
    centrale, lissé ; la page commence là où ce rapport reste < seuil sur 120 px."""
    g = np.asarray(im.convert('L')).astype(np.float32)
    H, W = g.shape
    gx = np.abs(cv2.Sobel(g, cv2.CV_32F, 1, 0, ksize=3))
    gy = np.abs(cv2.Sobel(g, cv2.CV_32F, 0, 1, ksize=3))
    def bornes(r, n, lim_bas, lim_haut, seuil):
        r = np.convolve(r, np.ones(41) / 41, 'same')
        ok = r < seuil
        a = 0
        while a < lim_bas and not ok[a:a + 120].all():
            a += 4
        b = n - 1
        while b > lim_haut and not ok[max(0, b - 120):b + 1].all():
            b -= 4
        return a, b
    bx = slice(int(0.25 * H), int(0.75 * H))
    x0, x1 = bornes((gx[bx].mean(0) + 1) / (gy[bx].mean(0) + 1), W, int(0.3 * W), int(0.7 * W), P['bord_seuil'])
    by = slice(max(x0, int(0.2 * W)), min(x1, int(0.8 * W)))
    y0, y1 = bornes((gy[:, by].mean(1) + 1) / (gx[:, by].mean(1) + 1), H, int(0.12 * H), int(0.88 * H), P['bord_seuil'])
    return [int(x0), int(y0), int(x1), int(y1)]


# ----------------------------------------------------------------------------
# 6. blocs marginaux

def grouper(C, ids, W, H, noyau):
    """Regroupement par dilatation (noyau rectangulaire) ; renvoie des listes d'indices."""
    if len(ids) == 0:
        return []
    ids = np.asarray(ids, int)
    m = np.zeros(C['n'], bool); m[ids] = True
    mm = m[C['lab']].astype(np.uint8)
    d = cv2.dilate(mm, cv2.getStructuringElement(cv2.MORPH_RECT, noyau))
    nb, labb = cv2.connectedComponents(d, connectivity=8)
    memb = labb[np.clip(C['cy'][ids].astype(int), 0, H - 1), np.clip(C['cx'][ids].astype(int), 0, W - 1)]
    out = []
    for j in np.unique(memb):
        if j == 0:
            continue
        out.append(ids[memb == j])
    return out


def decrire_bloc(C, ids):
    return dict(ids=np.asarray(ids, int).tolist(), boite=boite_de(C, ids),
                cmax=float(np.median(C['cmax'][ids])), cmoy=float(np.median(C['cmoy'][ids])),
                aire=int(C['a'][ids].sum()), n=len(ids))


def est_ecriture(bl):
    """Bloc vraisemblablement écrit (et non tache, tranche, bord de reliure)."""
    w = bl['boite'][2] - bl['boite'][0]; h = bl['boite'][3] - bl['boite'][1]
    if bl.get('n_lettres', bl['n']) < 2 or bl['aire'] < 120:
        return False
    if bl['cmax'] < P['bloc_cmax_med'] or bl['cmoy'] < P['bloc_cmoy_med']:
        return False
    if w < 12 or h < 6:
        return False
    if h > 4 * w and w < 60:   # strie verticale
        return False
    return True


def lignes_bloc(C, ids, ang, W):
    """Lignes d'un bloc marginal (profil redressé, pas estimé par autocorrélation)."""
    ids = np.asarray(ids, int)
    yr = redresser(C['cx'][ids], C['cy'][ids], ang, W)
    off = 50
    y0 = yr.min() - off
    n = int(yr.max() - y0 + off)
    pr = profil(yr - y0, C['a'][ids], n, 1.5)
    p = pr - pr.mean()
    pas = None
    if len(p) > 80 and (p ** 2).sum() > 0:
        ac = np.correlate(p, p, 'full')[len(p) - 1:]
        ac /= ac[0]
        k = int(np.argmax(ac[14:50])) + 14
        if ac[k] > 0.2:
            pas = k
    if pas is None:
        pas = max(16, int(np.median(C['h'][ids]) * 2.2))
    pr2 = gaussian_filter1d(profil(yr - y0, C['a'][ids], n, 0), max(pas / 6, 1.5))
    pics, _ = find_peaks(pr2, distance=max(int(0.6 * pas), 6), prominence=0.12 * pr2.max())
    centres = np.array([q + y0 for q in pics])
    if len(centres) == 0:
        return [boite_de(C, ids)], int(pas)
    k = np.abs(yr[:, None] - centres[None, :]).argmin(1)
    res = [boite_de(C, ids[k == i]) for i in range(len(centres)) if (k == i).any()]
    res.sort(key=lambda b: b[1])
    return res, int(pas)


# ----------------------------------------------------------------------------
# 7. numéro de folio (rectos : coin supérieur droit)

def numero_folio(im, ink, page, haut):
    """Numéro de folio moderne (rectos, coin supérieur externe), écrit au crayon gris :
    masque propre (plus sombre que le fond local), composantes de la taille d'un
    chiffre qui ne relèvent pas de l'encre brune du manuscrit (masque_encre), regroupées ;
    on retient le groupe de 2 à 6 composantes alignées, de la taille d'un nombre de
    3 chiffres."""
    W, H = im.size
    x0z, x1z = int(0.70 * W), min(W - 1, int(page[2]) + 60)
    y0z, y1z = 30, int(max(min(haut, 0.12 * H), 200))
    c = im.crop((x0z, y0z, x1z, y1z))
    lum = np.asarray(c.convert('L')).astype(np.float32)
    fond = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(12))).astype(np.float32)
    m = ((fond - lum) > 22) & (lum < 175)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m.astype(np.uint8), connectivity=8)
    brun = ndi.mean(ink[y0z:y1z, x0z:x1z].astype(np.float32), lab, np.arange(n))
    ok = np.zeros(n, bool)
    for k in range(1, n):
        x, y, w, h, a = st[k]
        if (a >= 15 and 12 <= h <= 45 and 3 <= w <= 40 and x > 2 and y > 2
                and x + w < m.shape[1] - 2 and y + h < m.shape[0] - 2 and brun[k] < 0.5):
            ok[k] = True
    if ok.sum() < 2:
        return None
    mm = ok[lab].astype(np.uint8)
    d = cv2.dilate(mm, cv2.getStructuringElement(cv2.MORPH_RECT, (21, 11)))
    ng, labg = cv2.connectedComponents(d, connectivity=8)
    best = None
    for g in range(1, ng):
        ks = [k for k in np.where(ok)[0] if labg[int(cen[k, 1]), int(cen[k, 0])] == g]
        if not (2 <= len(ks) <= 6):
            continue
        xs = [st[k, 0] for k in ks]; ys = [st[k, 1] for k in ks]
        xe = [st[k, 0] + st[k, 2] for k in ks]; ye = [st[k, 1] + st[k, 3] for k in ks]
        bw, bh = max(xe) - min(xs), max(ye) - min(ys)
        if not (25 <= bw <= 110 and 14 <= bh <= 55):
            continue
        b = [int(min(xs)), int(min(ys)), int(max(xe)), int(max(ye))]
        sc = len(ks) - np.std([cen[k, 1] for k in ks]) / 5
        if best is None or sc > best[0]:
            best = (sc, b)
    if best is None:
        return None
    # extension aux traits voisins (chiffres fragmentés ou pâles), puis petite marge
    b = best[1]
    lache = [k for k in range(1, n) if st[k, 4] >= 8 and st[k, 3] >= 5 and st[k, 2] <= 45
             and st[k, 3] <= 50 and brun[k] < 0.5]
    for _ in range(3):
        for k in lache:
            x, y, w, h = st[k, :4]
            if x <= b[2] + 25 and x + w >= b[0] - 25 and y <= b[3] + 8 and y + h >= b[1] - 8:
                b = [min(b[0], x), min(b[1], y), max(b[2], x + w), max(b[3], y + h)]
    return [int(b[0] + x0z - 6), int(b[1] + y0z - 6), int(b[2] + x0z + 6), int(b[3] + y0z + 6)]


# ----------------------------------------------------------------------------
# traitement d'une page

def charger_corrections():
    if os.path.exists(CORR):
        with open(CORR) as f:
            return json.load(f)
    return {}


def traiter(path, debug=False, corr=None):
    nom = os.path.basename(path)
    folio = folio_de(nom)
    cp = (corr or {}).get(folio, {})
    im = Image.open(path).convert('RGB')
    W, H = im.size
    ink, lum, C = composantes(im)
    page = cp.get('page') or interieur_page(im)
    # composantes hors de la page : écartées
    dedans = (C['cx'] >= page[0]) & (C['cx'] <= page[2]) & (C['cy'] >= page[1]) & (C['cy'] <= page[3])
    C['texte'] = C['texte'] & dedans
    ang, pas, _ = inclinaison_pas(C, W, H)
    L0, R0 = colonne_grossiere(C, W, H, ang, pas)
    if 'colonne' in cp:
        L0, R0 = cp['colonne']
    ang, pas, _ = inclinaison_pas(C, W, H, zone=(L0, R0, 0, H))
    graine = (L0 + 20, min(L0 + P['graine'], R0))
    # premier passage (chaînage libre), module du texte, second passage
    lignes = lignes_colonne(C, W, H, ang, pas, L0, R0, None)
    lignes, _ = selection_colonne(C, lignes, pas, graine)
    modele = modele_ecritures(C, lignes, graine, L0, R0, page)
    lignes = lignes_colonne(C, W, H, ang, pas, L0, R0, modele)
    lignes, rendues = selection_colonne(C, lignes, pas, graine)
    # corrections manuelles : bornes verticales de la colonne (y du centre de ligne au milieu de la page)
    if 'haut' in cp or 'bas' in cp:
        yh, yb = cp.get('haut', -1), cp.get('bas', H + 1)
        yy = lambda li: li['a'] + li['b'] * W / 2
        lignes = [li for li in lignes if yh <= yy(li) <= yb]

    # bord gauche du texte ; coupe des chaînes au-delà de la zone des sigles
    S_sig = cp.get('sigle', P['sigle'])
    L = gauche_colonne(C, lignes) if lignes else L0
    if 'gauche' in cp:
        L = int(cp['gauche'])
    for li in lignes:
        ids = np.asarray(li['ids'])
        ids = ids[C['x'][ids] + C['w'][ids] > L - S_sig]
        li['ids'] = ids.tolist()
        dr = ids[C['x'][ids] >= L - 5]
        if len(dr) >= 2:
            li['a'], li['b'] = ajuster(C, dr, ang, W)
    lignes = [li for li in lignes if len(li['ids']) >= 2]
    lignes.sort(key=lambda li: li['a'] + li['b'] * W / 2)

    yc = lambda li, x: li['a'] + li['b'] * x
    out_lignes = []
    pris = np.zeros(C['n'], bool)
    for i, li in enumerate(lignes):
        ids = np.asarray(li['ids'])
        pris[ids] = True
        sg = ids[C['x'][ids] + C['w'][ids] <= L + 3]
        tx = ids[C['x'][ids] + C['w'][ids] > L + 3]
        b = boite_de(C, ids)
        out_lignes.append(dict(index=i + 1, type='texte', a=round(li['a'], 3), b=round(li['b'], 6),
                               coeur=b, texte=boite_de(C, tx) if len(tx) else b,
                               sigle=boite_de(C, sg) if len(sg) else None, glose=None, interligne=None,
                               module=li.get('module'), score=li.get('score')))

    # composantes restantes : région de chacune
    libres = np.where(C['texte'] & ~pris)[0]
    reg = {}
    if out_lignes:
        A = np.array([li['a'] for li in out_lignes]); B = np.array([li['b'] for li in out_lignes])
        fins = np.array([li['texte'][2] for li in out_lignes])
        for k in libres:
            x, y = C['cx'][k], C['cy'][k]
            yl = A + B * x
            d = y - yl
            if d[0] < -P['marge_haut'] * pas:
                r = 'haut'
            elif d[-1] > P['marge_haut'] * pas:
                r = 'bas'
            elif C['x'][k] + C['w'][k] <= L - 3:
                r = 'gauche'
            else:
                j = int(np.searchsorted(yl, y))     # lignes encadrantes j-1, j
                encadr = [q for q in (j - 1, j) if 0 <= q < len(out_lignes)]
                fin = max(fins[q] for q in encadr)
                proche = min(encadr, key=lambda q: abs(d[q]))
                if C['x'][k] >= fin + 0.3 * pas or (C['x'][k] >= fins[proche] + 0.3 * pas and abs(d[proche]) <= 0.35 * pas):
                    r = 'droite'
                else:
                    r = 'interligne'
            reg.setdefault(r, []).append(k)
    else:
        reg['haut'] = list(libres)

    # interligne : groupes de type « mot » (≥ 3 composantes d'aire ≥ 25), rattachés à la
    # ligne au-dessous (ajout au-dessus de la ligne) ; accents et points isolés ignorés
    for g in grouper(C, reg.get('interligne', []), W, H, (25, 7)):
        if (C['a'][g] >= 25).sum() < 3:
            continue
        bk = boite_de(C, g)
        xm, ym = 0.5 * (bk[0] + bk[2]), 0.5 * (bk[1] + bk[3])
        d = np.array([ym - yc(li, xm) for li in out_lignes])
        dessous = np.where(d < 0)[0]
        j = int(dessous[0]) if len(dessous) else len(out_lignes) - 1
        out_lignes[j]['interligne'] = (out_lignes[j]['interligne'] or []) + [bk]

    # blocs par région
    blocs = []
    # blocs : regroupement des seules composantes « lettres » (aire ≥ 25, contraste
    # moyen ≥ bloc_cmoy_lettre), pour que la poussière et les taches ne fassent pas
    # pont ; les petites composantes (accents, points) situées dans la boîte d'un bloc
    # lui sont ensuite rattachées
    for r in ('haut', 'bas', 'gauche', 'droite'):
        ids_r = np.asarray(reg.get(r, []), int)
        if len(ids_r) == 0:
            continue
        lettres = ids_r[(C['a'][ids_r] >= 25) & (C['cmoy'][ids_r] >= P['bloc_cmoy_lettre'])]
        petits = ids_r[~np.isin(ids_r, lettres)]
        for g in grouper(C, lettres, W, H, P['bloc_noyau']):
            b = boite_de(C, g)
            ajout = petits[(C['x'][petits] >= b[0] - 4) & (C['x'][petits] + C['w'][petits] <= b[2] + 4)
                           & (C['y'][petits] >= b[1] - 4) & (C['y'][petits] + C['h'][petits] <= b[3] + 4)]
            bl = decrire_bloc(C, np.concatenate([g, ajout]))
            bl['region'] = r
            bl['n_lettres'] = len(g)
            if est_ecriture(bl):
                blocs.append(bl)

    # petits blocs contigus à une ligne : sigles (à gauche) et gloses (à droite)
    garde = []
    for bl in blocs:
        bx0, by0, bx1, by1 = bl['boite']
        att = False
        if bl['region'] in ('gauche', 'droite') and by1 - by0 <= 1.3 * pas and out_lignes:
            xm, ym = 0.5 * (bx0 + bx1), 0.5 * (by0 + by1)
            dists = [abs(yc(li, xm) - ym) for li in out_lignes]
            j = int(np.argmin(dists)); li = out_lignes[j]
            if dists[j] <= 0.5 * pas:
                if bl['region'] == 'gauche' and bx0 >= L - S_sig - 20 and bx1 <= L + 10:
                    li['sigle'] = union(li['sigle'], bl['boite']); att = True
                elif bl['region'] == 'droite' and bx0 - li['texte'][2] <= 8 * pas:
                    li['glose'] = union(li['glose'], bl['boite']); att = True
        if not att:
            garde.append(bl)
    blocs = garde

    # colonne
    if out_lignes:
        col = None
        for li in out_lignes:
            col = union(col, li['coeur'])
        R = int(np.percentile([li['texte'][2] for li in out_lignes], 95))
    else:
        col = [L0, 0, R0, H - 1]; R = R0

    # croissance de région : blocs proches de la zone écrite
    zone = list(col)
    for li in out_lignes:
        for k in ('sigle', 'glose'):
            if li[k]:
                zone = union(zone, li[k])
        for bk in li['interligne'] or []:
            zone = union(zone, bk)
    retenus, restants = [], list(blocs)
    change = True
    while change:
        change = False
        for bl in list(restants):
            lim = P['croissance'] if bl.get('n_lettres', 0) >= 5 else P['croissance_petit']
            if distance_boites(bl['boite'], zone) <= lim:
                zone = union(zone, bl['boite']); retenus.append(bl); restants.remove(bl); change = True

    # boîtes des lignes avec marges (réduites si les lignes se serrent) et découpes
    droite_ids = [k for bl in retenus if bl['region'] == 'droite' for k in bl['ids']]
    for i, li in enumerate(out_lignes):
        x0, x1 = li['coeur'][0], li['coeur'][2]
        xm = 0.5 * (x0 + x1)
        up = P['marge_haut'] * pas; dn = P['marge_bas'] * pas
        if i > 0:
            up = min(up, P['marge_haut'] * (yc(li, xm) - yc(out_lignes[i - 1], xm)))
        if i < len(out_lignes) - 1:
            dn = min(dn, P['marge_bas'] * (yc(out_lignes[i + 1], xm) - yc(li, xm)))
        ys = [yc(li, x0), yc(li, x1)]
        y0 = int(np.floor(min(ys) - up)); y1 = int(np.ceil(max(ys) + dn))
        y0 = min(y0, li['coeur'][1] - 2); y1 = max(y1, li['coeur'][3] + 2)
        for bk in li['interligne'] or []:
            y0 = min(y0, bk[1] - 2)
        li['boite'] = [x0, max(0, y0), x1, min(H - 1, y1)]
        li['marges'] = [round(up, 1), round(dn, 1)]
        # découpe : zone des sigles à gauche ; à droite, glose éventuelle (composantes de
        # la marge droite dont le centre est dans la bande de la ligne)
        dx1 = max(x1, (li['glose'] or [0, 0, x1])[2])
        for k in droite_ids:
            if abs(C['cy'][k] - yc(li, C['cx'][k])) <= 0.5 * pas and C['x'][k] - li['texte'][2] <= 8 * pas:
                dx1 = max(dx1, C['x'][k] + C['w'][k])
        dx0 = max(0, min(L - S_sig, x0 - 10, (li['sigle'] or [x0])[0] - 10))
        li['decoupe'] = [int(dx0), li['boite'][1], int(min(W - 1, dx1 + 20)), li['boite'][3]]

    out_blocs = []
    for k, bl in enumerate(sorted(retenus, key=lambda b: (['haut', 'gauche', 'droite', 'bas'].index(b['region']), b['boite'][1], b['boite'][0]))):
        lb, pas_b = lignes_bloc(C, bl['ids'], ang, W)
        out_blocs.append(dict(index=k + 1, region=bl['region'], boite=bl['boite'], pas=pas_b,
                              lignes=[dict(index=j + 1, boite=b) for j, b in enumerate(lb)]))

    # numéro de folio (rectos) : coin supérieur droit de la page
    num = None
    if folio.endswith('r'):
        num = cp['numero_folio'] if 'numero_folio' in cp else numero_folio(im, ink, page, zone[1] + pas)
    ecriture = union(zone, num) if num else zone
    if 'ecriture' in cp:
        ecriture = cp['ecriture']

    res = dict(folio=folio, source=nom, taille=[W, H], vers_nom_fichier=list(vers_de(nom)),
               page=page, inclinaison=round(ang, 3), pas=round(pas, 2),
               colonne=dict(boite=col, gauche=L, droite=R, zone_sigles=[max(0, L - S_sig), L]),
               lignes=out_lignes, blocs=out_blocs, numero_folio=num, ecriture=ecriture,
               corrections=cp, parametres={k: v for k, v in P.items()})
    with open(os.path.join(DST, folio + '.json'), 'w') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    if debug:
        dessiner_debug(im, res, restants)
    return res


def dessiner_debug(im, res, rejetes=()):
    os.makedirs(DEBUG, exist_ok=True)
    W, H = im.size
    v = im.copy()
    d = ImageDraw.Draw(v)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
    except OSError:
        font = None
    col = res['colonne']
    d.rectangle(res['page'], outline=(120, 120, 120), width=3)
    d.line([(col['gauche'], 0), (col['gauche'], H)], fill=(0, 160, 0), width=2)
    d.line([(col['zone_sigles'][0], 0), (col['zone_sigles'][0], H)], fill=(0, 160, 0), width=1)
    for k, li in enumerate(res['lignes']):
        c = (220, 0, 0) if k % 2 == 0 else (0, 0, 220)
        x0, x1 = li['coeur'][0], li['coeur'][2]
        d.line([(x0, li['a'] + li['b'] * x0), (x1, li['a'] + li['b'] * x1)], fill=c, width=3)
        d.rectangle(li['texte'], outline=c, width=2)
        d.text((li['decoupe'][0] - 45, li['a'] + li['b'] * x0 - 14), str(li['index']), fill=c, font=font)
        if li['sigle']:
            d.rectangle(li['sigle'], outline=(160, 0, 160), width=3)
        if li['glose']:
            d.rectangle(li['glose'], outline=(0, 150, 150), width=3)
        for bk in li['interligne'] or []:
            d.rectangle(bk, outline=(0, 200, 0), width=2)
    for bl in res['blocs']:
        d.rectangle(bl['boite'], outline=(255, 140, 0), width=4)
        d.text((bl['boite'][0], bl['boite'][1] - 28), '%s%d' % (bl['region'][0].upper(), bl['index']), fill=(255, 100, 0), font=font)
        for b in bl['lignes']:
            d.rectangle(b['boite'], outline=(230, 180, 0), width=1)
    for bl in rejetes:
        d.rectangle(bl['boite'], outline=(150, 150, 150), width=1)
    if res['numero_folio']:
        d.rectangle(res['numero_folio'], outline=(255, 0, 255), width=4)
    d.rectangle(res['ecriture'], outline=(255, 0, 0), width=5)
    v = v.resize((W // 2, H // 2), Image.LANCZOS)
    v.save(os.path.join(DEBUG, res['folio'] + '.jpg'), quality=85)


def _job(args):
    path, debug, corr = args
    return traiter(path, debug, corr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pages', nargs='*')
    ap.add_argument('--debug', action='store_true')
    ap.add_argument('-j', type=int, default=8)
    a = ap.parse_args()
    fichiers = sorted(glob.glob(os.path.join(SRC, '*.jpg')))
    if a.pages:
        fichiers = [f for f in fichiers if folio_de(os.path.basename(f)) in a.pages]
    os.makedirs(DST, exist_ok=True)
    corr = charger_corrections()
    with Pool(min(a.j, len(fichiers))) as pool:
        res = pool.map(_job, [(f, a.debug, corr) for f in fichiers])
    for r in res:
        print(r['folio'], 'incl=%.2f' % r['inclinaison'], 'pas=%.1f' % r['pas'],
              'col=', r['colonne']['gauche'], r['colonne']['droite'],
              'lignes=', len(r['lignes']), 'blocs=', len(r['blocs']), 'page=', r['page'], 'ecr=', r['ecriture'],
              'num=', r['numero_folio'])


if __name__ == '__main__':
    main()
