#!/usr/bin/env python3
"""Versions « améliorées » des pages du Ravennas pour la lecture des passages
difficiles (encre pâlie, grattages, scholies effacées), à la manière de DStretch et de
l'imagerie par composantes principales, à partir des seules images couleur RVB.

Pour chaque page fXXX, dans .travail/ameliorations/fXXX/ :
  ds_rvb.jpg   étirement de décorrélation dans l'espace RVB (ACP, variances égalisées)
  ds_lab.jpg   étirement de décorrélation dans l'espace CIE Lab
  clahe.jpg    égalisation adaptative du contraste (CLAHE) sur la luminance
  bleu.jpg     canal bleu inversé et étiré (l'encre brune absorbe le bleu)
  cp2.jpg, cp3.jpg   2e et 3e composantes principales étirées (différences d'encre, grattages)
  encre.png    masque binaire de l'encre brune (cf. recadrer_facsimile.masque_encre)

Usage : python3 outils/images/ameliorer.py [--proc 6] [fXXX ...]
"""
import argparse, glob, os, re, sys
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import cv2
from PIL import Image

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(RACINE, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
DST = os.path.join(RACINE, '.travail', 'ameliorations')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def etirer(x, bas=0.5, haut=99.5):
    a, b = np.percentile(x, [bas, haut])
    return np.clip((x - a) / max(b - a, 1e-6) * 255, 0, 255).astype(np.uint8)


def decorrelation(img, cible=50.0):
    """Étirement de décorrélation : ACP des canaux, égalisation des écarts-types,
    retour dans l'espace d'origine."""
    h, w, c = img.shape
    X = img.reshape(-1, c).astype(np.float64)
    mu = X.mean(axis=0)
    Xc = X - mu
    cov = np.cov(Xc[::17].T)
    val, vec = np.linalg.eigh(cov)
    val = np.maximum(val, 1e-6)
    T = vec @ np.diag(cible / np.sqrt(val)) @ vec.T
    Y = Xc @ T.T + mu
    return np.clip(Y, 0, 255).reshape(h, w, c).astype(np.uint8)


def composantes(img):
    h, w, c = img.shape
    X = img.reshape(-1, c).astype(np.float64)
    Xc = X - X.mean(axis=0)
    val, vec = np.linalg.eigh(np.cov(Xc[::17].T))
    ordre = np.argsort(val)[::-1]
    P = Xc @ vec[:, ordre]
    return [P[:, k].reshape(h, w) for k in range(c)]


def traiter(path):
    from recadrer_facsimile import masque_encre
    folio = re.search(r'_(f\d+[rv])_', os.path.basename(path)).group(1)
    out = os.path.join(DST, folio)
    os.makedirs(out, exist_ok=True)
    pil = Image.open(path).convert('RGB')
    rgb = np.asarray(pil)
    Image.fromarray(decorrelation(rgb)).save(os.path.join(out, 'ds_rvb.jpg'), quality=90)
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    ds = decorrelation(lab)
    Image.fromarray(cv2.cvtColor(ds, cv2.COLOR_LAB2RGB)).save(os.path.join(out, 'ds_lab.jpg'), quality=90)
    L = lab[..., 0]
    cl = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(16, 16)).apply(L)
    lab2 = lab.copy(); lab2[..., 0] = cl
    Image.fromarray(cv2.cvtColor(lab2, cv2.COLOR_LAB2RGB)).save(os.path.join(out, 'clahe.jpg'), quality=90)
    Image.fromarray(etirer(255.0 - rgb[..., 2])).save(os.path.join(out, 'bleu.jpg'), quality=90)
    cps = composantes(rgb.astype(np.float64))
    Image.fromarray(etirer(cps[1])).save(os.path.join(out, 'cp2.jpg'), quality=90)
    Image.fromarray(etirer(cps[2])).save(os.path.join(out, 'cp3.jpg'), quality=90)
    m, _ = masque_encre(pil)
    Image.fromarray(((~m) * 255).astype(np.uint8)).save(os.path.join(out, 'encre.png'), optimize=True)
    return folio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--proc', type=int, default=6)
    ap.add_argument('folios', nargs='*')
    a = ap.parse_args()
    fichiers = sorted(glob.glob(os.path.join(SRC, '*.jpg')))
    if a.folios:
        fichiers = [f for f in fichiers if any(('_' + x + '_') in f for x in a.folios)]
    with ProcessPoolExecutor(a.proc) as ex:
        for f in ex.map(traiter, fichiers):
            print(f, flush=True)


if __name__ == '__main__':
    main()
