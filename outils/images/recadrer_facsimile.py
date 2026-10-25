#!/usr/bin/env python3
"""Recadre chaque page du Ravennas sur la zone écrite (texte, sigles, scholies),
pour un fac-similé aussi grand que possible dans la page de l'édition.

Méthode : (1) masque du parchemin (clair, peu saturé, région connexe principale) ;
(2) traits d'encre = passe-haut sur la luminance (différence avec un flou de rayon 6),
ce qui ignore taches, ombres de reliure et dégradés ; on exclut les pixels saturés
(mire de couleurs) et tout ce qui est hors du parchemin ; (3) profils lissés et seuils
robustes pour la boîte englobante, plus une marge.
Des corrections manuelles éventuelles se mettent dans corrections_recadrage.json.
Sortie : edition/images/fXXX.jpg + edition/images/recadrages.json + planche de contrôle.
"""
import argparse, glob, json, os, re
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(RACINE, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
DST = os.path.join(RACINE, 'edition', 'images')
CORR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'corrections_recadrage.json')


def masque_encre(im):
    """Encre brune du Ravennas : nettement plus sombre que le fond local, teinte
    rouge-brun (H < 48° ou > 340°), saturation > 0,22."""
    hsv = np.asarray(im.convert('HSV')).astype(np.float32)
    H = hsv[..., 0] * 360 / 255; S = hsv[..., 1] / 255
    lum = np.asarray(im.convert('L')).astype(np.float32)
    fond = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))).astype(np.float32)
    return ((fond - lum) > 28) & (S > 0.22) & ((H < 48) | (H > 340)), lum


def analyser(path):
    """Boîte englobante de l'écriture : petites composantes d'encre regroupées en
    « blocs de lignes » par dilatation ; on ne garde que les blocs qui contiennent
    beaucoup de composantes (écriture), ce qui élimine bords, tranches et taches."""
    import cv2
    im = Image.open(path).convert('RGB')
    w, h = im.size
    ink, lum = masque_encre(im)
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink.astype(np.uint8), connectivity=8)
    ok = (st[:, cv2.CC_STAT_AREA] >= 6) & (st[:, cv2.CC_STAT_HEIGHT] < 80) & (st[:, cv2.CC_STAT_WIDTH] < 200)
    ok[0] = False
    k = ok[lab].astype(np.uint8)
    blobs = cv2.dilate(k, cv2.getStructuringElement(cv2.MORPH_RECT, (35, 9)))
    nb, labb, stb, _ = cv2.connectedComponentsWithStats(blobs, connectivity=8)
    # nombre de composantes d'encre par bloc (via leurs centres)
    cent = np.array([[st[i, 0] + st[i, 2] // 2, st[i, 1] + st[i, 3] // 2] for i in range(n)])
    cnt = np.zeros(nb, int)
    for i in np.where(ok)[0]:
        cnt[labb[cent[i, 1], cent[i, 0]]] += 1
    xs0, ys0, xs1, ys1 = [], [], [], []
    for j in range(1, nb):
        x, y, ww, hh, area = stb[j]
        if cnt[j] >= 12 and hh < 0.5 * h:
            xs0.append(x); ys0.append(y); xs1.append(x + ww); ys1.append(y + hh)
    return im, (int(min(xs0)), int(min(ys0)), int(max(xs1)), int(max(ys1))), (0, 0, w - 1, h - 1)


def traiter(args):
    path, marge, qualite, corr = args
    nom = os.path.basename(path)
    folio = re.search(r'_(f\d+[rv])_', nom).group(1)
    im, (x0, y0, x1, y1), p = analyser(path)
    h = im.size[1]
    mg = int(marge * h)
    b = [int(max(p[0], x0 - mg)), int(max(p[1], y0 - mg)), int(min(p[2], x1 + mg)), int(min(p[3], y1 + mg))]
    if folio in corr:
        b = corr[folio]
    im.crop(tuple(b)).save(os.path.join(DST, folio + '.jpg'), quality=qualite, subsampling=0, optimize=True)
    # vignette de contrôle
    v = im.copy(); d = ImageDraw.Draw(v)
    d.rectangle(p, outline=(0, 0, 255), width=6); d.rectangle(b, outline=(255, 0, 0), width=8)
    v = v.resize((v.size[0] * 400 // v.size[1], 400))
    return {'folio': folio, 'source': nom, 'boite': b, 'parchemin': p}, v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--marge', type=float, default=0.012)
    ap.add_argument('--qualite', type=int, default=90)
    ap.add_argument('--controle', default=os.path.join(RACINE, '.travail', 'controle_recadrage.jpg'))
    a = ap.parse_args()
    os.makedirs(DST, exist_ok=True)
    corr = json.load(open(CORR)) if os.path.exists(CORR) else {}
    fichiers = sorted(glob.glob(os.path.join(SRC, '*.jpg')))
    with ProcessPoolExecutor(8) as ex:
        res = list(ex.map(traiter, [(f, a.marge, a.qualite, corr) for f in fichiers]))
    json.dump([r for r, _ in res], open(os.path.join(DST, 'recadrages.json'), 'w'), indent=1)
    vs = [v for _, v in res]
    W = sum(v.size[0] for v in vs[:10]) + 100
    planche = Image.new('RGB', (W, 1230), 'white')
    for k, v in enumerate(vs):
        x = sum(u.size[0] + 10 for u in vs[(k // 10) * 10:k])
        planche.paste(v, (x, (k // 10) * 410))
    os.makedirs(os.path.dirname(a.controle), exist_ok=True)
    planche.save(a.controle, quality=80)
    for r, _ in res:
        print(r['folio'], r['boite'])


if __name__ == '__main__':
    main()
