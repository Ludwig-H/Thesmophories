#!/usr/bin/env python3
"""Mesures globales de l'écriture du copiste (T) sur les 30 pages des Thesmophories
(chapitre 2 de l'étude graphologique).

Pour chaque ligne de la colonne de texte (segmentation ravennas/segmentation/fXXX.json) :
  - hauteur du corps des lettres (« hauteur d'x ») : largeur, sur le profil horizontal
    du masque d'encre, de la bande où la densité dépasse 50 % du maximum ;
  - position de la ligne de base et de la ligne de tête de cette bande.
Pour chaque page :
  - (essai abandonné) inclinaison des hampes : les fonctions pente() et pente_hampes()
    sont conservées pour mémoire, mais leurs résultats sont dominés par les accents
    aigus et les obliques de construction (λ, ν) et ne mesurent pas la pente de
    l'écriture : ils ne sont plus écrits dans la sortie (chapitre 2, § 2.5) ;
  - interligne (pas de la segmentation) ;
Sortie : ravennas/graphologie/chapitres/mesures_ecriture.json (+ tableau texte).
Le masque d'encre est celui de outils/images/recadrer_facsimile.py.
"""
import glob, json, os, sys, unicodedata
import numpy as np
from PIL import Image

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'outils', 'images'))
from recadrer_facsimile import masque_encre  # noqa: E402

SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
MM = 0.116  # mm par pixel


def page(folio):
    f = [p for p in glob.glob(os.path.join(SRC, '*.jpg')) if f'_{folio}_' in os.path.basename(p)][0]
    return Image.open(f).convert('RGB')


def hauteur_x(m, seuil=0.5):
    """m : masque d'une ligne (bool, h × w). Renvoie (h_x, y_tete, y_base) en px :
    bande où le profil horizontal de l'encre dépasse `seuil` × maximum."""
    prof = m.sum(axis=1).astype(float)
    if prof.max() < 5:
        return None
    k = np.ones(3) / 3
    prof = np.convolve(prof, k, mode='same')
    i = int(prof.argmax())
    s = seuil * prof[i]
    a = i
    while a > 0 and prof[a - 1] >= s:
        a -= 1
    b = i
    while b < len(prof) - 1 and prof[b + 1] >= s:
        b += 1
    return b - a + 1, a, b


def pente_hampes(m):
    """Inclinaison des hampes et des queues : composantes connexes du masque situées
    au-dessus de la tête ou au-dessous de la base du corps des lettres, allongées
    (hauteur ≥ 9 px, élongation ≥ 2,5) ; angle par les moments d'ordre 2, en degrés
    par rapport à la verticale (> 0 : penché vers la droite). Renvoie la liste des angles."""
    import cv2
    r = hauteur_x(m, 0.5)
    if not r:
        return []
    _, a, b = r
    out = []
    for zone in (m[:max(0, a - 2)], m[b + 3:]):
        if zone.shape[0] < 9:
            continue
        n, lab, st, _ = cv2.connectedComponentsWithStats(zone.astype(np.uint8), 8)
        for k in range(1, n):
            x, y, w, h, area = st[k]
            if h < 9 or area < 12:
                continue
            ys, xs = np.nonzero(lab[y:y + h, x:x + w] == k)
            xs = xs - xs.mean(); ys = ys - ys.mean()
            mu20, mu02, mu11 = (xs * xs).mean(), (ys * ys).mean(), (xs * ys).mean()
            l1 = 0.5 * (mu20 + mu02) + np.sqrt(0.25 * (mu20 - mu02) ** 2 + mu11 ** 2)
            l2 = 0.5 * (mu20 + mu02) - np.sqrt(0.25 * (mu20 - mu02) ** 2 + mu11 ** 2)
            if l2 <= 0 or l1 / l2 < 6.25:  # élongation (rapport des axes) ≥ 2,5
                continue
            th = 0.5 * np.degrees(np.arctan2(2 * mu11, mu20 - mu02))  # axe principal / horizontale (y vers le bas)
            ang = 90 - abs(th)  # écart à la verticale
            # sens : axe principal montant vers la droite (y diminue quand x augmente) = penché à droite
            sgn = -1 if th > 0 else 1
            if abs(th) < 30:  # trait plus horizontal que vertical : ignorer
                continue
            out.append(sgn * ang)
    return out


def pente(m):
    """Angle (degrés) de cisaillement qui maximise la somme des carrés du profil vertical."""
    ys, xs = np.nonzero(m)
    if len(xs) < 500:
        return None
    yc = ys.mean()
    best = None
    for ang in np.arange(-30, 30.01, 0.5):
        t = np.tan(np.radians(ang))
        # écriture penchée à droite : le haut du trait est plus à droite ; on redresse
        xx = np.round(xs + (ys - yc) * t).astype(int)
        xx -= xx.min()
        h = np.bincount(xx)
        sc = float((h.astype(float) ** 2).sum())
        if best is None or sc > best[1]:
            best = (ang, sc)
    return best[0]


def lettres(txt):
    n = 0
    for ch in unicodedata.normalize('NFD', txt):
        if unicodedata.category(ch).startswith('L'):
            n += 1
    return n


def main():
    texte = {}
    tsv = os.path.join(R, 'edition', 'donnees', 'travaux_anterieurs', 'texte_grec.tsv')
    if os.path.exists(tsv):
        for ln in open(tsv, encoding='utf-8'):
            p = ln.rstrip('\n').split('\t')
            if len(p) >= 2:
                texte[p[0]] = p[-1]
    res = {}
    for sj in sorted(glob.glob(os.path.join(R, 'ravennas', 'segmentation', 'f*.json'))):
        s = json.load(open(sj))
        folio = s['folio']
        im = page(folio)
        m, _ = masque_encre(im)
        hx, hx25, pentes, hampes = [], [], [], []
        for L in s['lignes']:
            if L.get('type') != 'texte':
                continue
            x0, y0, x1, y1 = L['texte'] if L.get('texte') else L['boite']
            sub = m[y0:y1, x0:x1]
            r = hauteur_x(sub)
            if r:
                hx.append(r[0])
            r = hauteur_x(sub, 0.25)
            if r:
                hx25.append(r[0])
        res[folio] = {
            'corps_50_px_mediane': float(np.median(hx)) if hx else None,
            'corps_25_px_mediane': float(np.median(hx25)) if hx25 else None,
            'interligne_px': s.get('pas'),
            'nb_lignes': len([L for L in s['lignes'] if L.get('type') == 'texte']),
        }
        print(folio, json.dumps(res[folio], ensure_ascii=False))
    out = os.path.join(R, 'ravennas', 'graphologie', 'chapitres', 'mesures_ecriture.json')
    json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
    print('->', out)


if __name__ == '__main__':
    main()
