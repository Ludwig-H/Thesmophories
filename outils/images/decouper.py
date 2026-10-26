#!/usr/bin/env python3
"""Découpes agrandies des pages du Ravennas à partir de la segmentation
(ravennas/segmentation/fXXX.json, produite par outils/images/segmenter.py).

Sortie (non versionnée) : .travail/decoupes/fXXX/
  lignes/fXXX_lNN.jpg      ligne NN, couleur, agrandie ×2 (Lanczos), redressée
  lignes/fXXX_lNN_c.jpg    même ligne, contraste renforcé (fond aplani, CLAHE), gris
  marges/fXXX_<région>_NN.jpg   tuiles chevauchantes des marges écrites (×2)
  planche_fXXX.jpg         planche contact : boîtes numérotées sur l'image réduite
  index.tsv                inventaire des découpes et de leurs coordonnées (pixels
                           de l'image source)
Usage : python3 outils/images/decouper.py [--pages f162v ...] [-j 8]

Chaque découpe de ligne couvre la zone des sigles à gauche de la colonne et, à
droite, la glose éventuelle ; verticalement, la bande de la ligne avec ses marges
(accents, ajouts interlinéaires). La découpe suit l'inclinaison propre de la ligne
(droite y = a + b·x de la segmentation) : le rectangle est redressé, puis agrandi.
"""
import argparse, glob, json, math, os, sys
from multiprocessing import Pool

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SRC = os.path.join(RACINE, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
SEG = os.path.join(RACINE, 'ravennas', 'segmentation')
DST = os.path.join(RACINE, '.travail', 'decoupes')

ECHELLE = 2            # agrandissement
QUALITE = 92           # JPEG
TUILE = (600, 450)     # taille maximale d'une tuile de marge (pixels source)
RECOUVREMENT = 0.25    # recouvrement des tuiles
H_PLANCHE = 1800       # hauteur de la planche contact


def police(t):
    for f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
        if os.path.exists(f):
            return ImageFont.truetype(f, t)
    return ImageFont.load_default()


def contraste(rgb):
    """Version au contraste renforcé (niveaux de gris) : canal bleu (où l'encre brune
    est la plus sombre), légèrement lissé, divisé par le fond local (flou gaussien de
    rayon 30) pour aplanir taches et dégradés, puis étiré entre le 1er centile (encre)
    et le 70e (fond) avec un gamma de 1,6 : fond blanc, encre noire, traits pâles
    renforcés."""
    b = cv2.GaussianBlur(rgb[..., 2].astype(np.float32), (0, 0), 0.7)
    fond = cv2.GaussianBlur(b, (0, 0), 30)
    r = b / np.maximum(fond, 1)
    lo, bg = np.percentile(r, 1), np.percentile(r, 70)
    v = np.clip((r - lo) / max(bg - lo, 1e-3), 0, 1)
    return (255 * v ** 1.6).astype(np.uint8)


def extraire_ligne(img, li, H):
    """Rectangle redressé autour de la droite de la ligne, agrandi ×ECHELLE.

    Abscisses : [decoupe[0], decoupe[2]] ; ordonnées : de la droite − marge haute (ou
    du haut de la découpe, s'il est plus haut) à la droite + marge basse."""
    x0, y0, x1, y1 = li['decoupe']
    a, b = li['a'], li['b']
    theta = math.atan(b)
    xm = 0.5 * (x0 + x1)
    ym = a + b * xm
    # distances verticales à la droite (au milieu) : haut et bas de la découpe
    up = max(ym - y0 - abs(b) * (x1 - x0) / 2, li['marges'][0])
    dn = max(y1 - ym - abs(b) * (x1 - x0) / 2, li['marges'][1])
    w = (x1 - x0) / math.cos(theta)
    h = up + dn
    ow, oh = int(round(w * ECHELLE)), int(round(h * ECHELLE))
    # application : point de sortie (u, v) -> point source
    c, s = math.cos(theta), math.sin(theta)
    # origine du rectangle (coin haut-gauche) dans la source
    ox = xm - c * w / 2 + s * up
    oy = ym - s * w / 2 - c * up
    M = np.array([[c / ECHELLE, -s / ECHELLE, ox],
                  [s / ECHELLE, c / ECHELLE, oy]], np.float64)
    out = cv2.warpAffine(img, M, (ow, oh), flags=cv2.INTER_LANCZOS4 | cv2.WARP_INVERSE_MAP,
                         borderMode=cv2.BORDER_REPLICATE)
    coins = [(ox, oy), (ox + c * w, oy + s * w), (ox + c * w - s * h, oy + s * w + c * h), (ox - s * h, oy + c * h)]
    return out, [[round(px, 1), round(py, 1)] for px, py in coins]


def tuiles(boite, taille, recouvrement):
    """Tuiles chevauchantes couvrant une boîte [x0, y0, x1, y1]."""
    x0, y0, x1, y1 = boite
    tw, th = taille
    def pas(l0, l1, t):
        L = l1 - l0
        if L <= t:
            return [(l0, l1)]
        n = math.ceil((L - t) / (t * (1 - recouvrement))) + 1
        st = (L - t) / (n - 1)
        return [(int(round(l0 + k * st)), int(round(l0 + k * st)) + t) for k in range(n)]
    return [(a, c, b, d) for (c, d) in pas(y0, y1, th) for (a, b) in pas(x0, x1, tw)]


def traiter(folio):
    with open(os.path.join(SEG, folio + '.json')) as f:
        seg = json.load(f)
    path = os.path.join(SRC, seg['source'])
    pil = Image.open(path).convert('RGB')
    img = np.asarray(pil)
    H, W = img.shape[:2]
    rep = os.path.join(DST, folio)
    os.makedirs(os.path.join(rep, 'lignes'), exist_ok=True)
    os.makedirs(os.path.join(rep, 'marges'), exist_ok=True)
    index = ['type\tfichier\tx0\ty0\tx1\ty1\tremarque']

    # (a) lignes
    polys = []
    for li in seg['lignes']:
        out, coins = extraire_ligne(img, li, H)
        nom = '%s_l%02d' % (folio, li['index'])
        Image.fromarray(out).save(os.path.join(rep, 'lignes', nom + '.jpg'), quality=QUALITE, subsampling=0)
        Image.fromarray(contraste(out)).save(os.path.join(rep, 'lignes', nom + '_c.jpg'), quality=QUALITE)
        polys.append((li['index'], coins))
        rq = []
        if li.get('sigle'):
            rq.append('sigle')
        if li.get('glose'):
            rq.append('glose')
        if li.get('interligne'):
            rq.append('interligne')
        if li.get('type', 'texte') != 'texte':
            rq.append(li['type'])
        index.append('ligne\tlignes/%s.jpg\t%d\t%d\t%d\t%d\t%s' % ((nom,) + tuple(li['decoupe']) + (' '.join(rq),)))

    # (b) tuiles des marges : union des blocs de chaque région, découpée en tuiles
    regions = {}
    for bl in seg['blocs']:
        regions.setdefault(bl['region'], []).append(bl['boite'])
    for li in seg['lignes']:          # gloses rattachées aux lignes : marge droite
        if li.get('glose'):
            regions.setdefault('droite', []).append(li['glose'])
    for reg, bts in sorted(regions.items()):
        u = [min(b[0] for b in bts) - 20, min(b[1] for b in bts) - 20,
             max(b[2] for b in bts) + 20, max(b[3] for b in bts) + 20]
        u = [max(0, u[0]), max(0, u[1]), min(W, u[2]), min(H, u[3])]
        k = 0
        for (tx0, ty0, tx1, ty1) in tuiles(u, TUILE, RECOUVREMENT):
            tx1, ty1 = min(tx1, W), min(ty1, H)
            if not any(b[0] < tx1 and b[2] > tx0 and b[1] < ty1 and b[3] > ty0 for b in bts):
                continue
            k += 1
            nom = '%s_%s_%02d.jpg' % (folio, reg, k)
            c = pil.crop((tx0, ty0, tx1, ty1))
            c = c.resize((c.size[0] * ECHELLE, c.size[1] * ECHELLE), Image.LANCZOS)
            c.save(os.path.join(rep, 'marges', nom), quality=QUALITE, subsampling=0)
            index.append('marge\tmarges/%s\t%d\t%d\t%d\t%d\t%s' % (nom, tx0, ty0, tx1, ty1, reg))

    # (c) planche contact
    r = H_PLANCHE / H
    v = pil.resize((int(W * r), H_PLANCHE), Image.LANCZOS)
    d = ImageDraw.Draw(v)
    f1, f2 = police(15), police(17)
    e = seg['ecriture']
    d.rectangle([e[0] * r, e[1] * r, e[2] * r, e[3] * r], outline=(255, 0, 0), width=2)
    for bl in seg['blocs']:
        b = bl['boite']
        d.rectangle([b[0] * r, b[1] * r, b[2] * r, b[3] * r], outline=(255, 140, 0), width=2)
        d.text((b[0] * r + 2, b[1] * r - 18), '%s%d' % (bl['region'][0].upper(), bl['index']), fill=(230, 100, 0), font=f2)
    for k, (idx, coins) in enumerate(polys):
        col = (210, 0, 0) if k % 2 == 0 else (0, 0, 210)
        pts = [(px * r, py * r) for px, py in coins]
        d.polygon(pts, outline=col)
        d.text((pts[0][0] - 24, (pts[0][1] + pts[3][1]) / 2 - 9), str(idx), fill=col, font=f1)
    if seg.get('numero_folio'):
        b = seg['numero_folio']
        d.rectangle([b[0] * r, b[1] * r, b[2] * r, b[3] * r], outline=(255, 0, 255), width=2)
    d.text((8, 6), '%s — %d lignes, %d blocs' % (folio, len(seg['lignes']), len(seg['blocs'])), fill=(0, 0, 0), font=f2)
    v.save(os.path.join(rep, 'planche_%s.jpg' % folio), quality=85)
    with open(os.path.join(rep, 'index.tsv'), 'w') as f:
        f.write('\n'.join(index) + '\n')
    return folio, len(seg['lignes']), len(index) - 1 - len(seg['lignes'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pages', nargs='*')
    ap.add_argument('-j', type=int, default=8)
    a = ap.parse_args()
    folios = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(SEG, 'f*.json')))
    if a.pages:
        folios = [f for f in folios if f in a.pages]
    with Pool(min(a.j, len(folios))) as pool:
        for folio, nl, nt in pool.imap(traiter, folios):
            print(folio, 'lignes:', nl, 'tuiles:', nt)


if __name__ == '__main__':
    main()
