#!/usr/bin/env python3
"""Découpe l'apparat critique (bas de page) des pages grecques de Prato 2001 et l'océrise à part.

Entrée : <sortie>/pages/idxNNN.png (produites par outils/prato2001_ocr.py, 400 dpi).
Sorties : <sortie>/apparat/idxNNN.png (découpe), <sortie>/apparat/idxNNN.txt (OCR grc+lat),
          <sortie>/apparat/zones.tsv (index, haut, bas, nombre de lignes).
L'apparat est le dernier groupe de lignes de la page, séparé du texte par un blanc
nettement plus grand que l'interligne, et d'interligne serré (corps plus petit).

Usage : python3 -I outils/prato2001_apparat.py SORTIE [--index 94-218] [--pas 2] [--processus 8]
"""
import argparse, concurrent.futures as cf, os, subprocess, unicodedata
from pathlib import Path

import numpy as np
from PIL import Image


def lignes(img):
    a = np.asarray(img.convert('L')) < 140
    prof = a[:, int(a.shape[1] * 0.08):int(a.shape[1] * 0.92)].sum(1)
    encre = prof > 2
    out, deb = [], None
    for y, e in enumerate(encre):
        if e and deb is None:
            deb = y
        elif not e and deb is not None:
            if y - deb > 6:
                out.append((deb, y))
            deb = None
    if deb is not None:
        out.append((deb, len(encre)))
    # fusion des fragments (accents, esprits au-dessus de la ligne)
    fus = []
    for l in out:
        if fus and l[0] - fus[-1][1] < 12:
            fus[-1] = (fus[-1][0], l[1])
        else:
            fus.append(l)
    return fus


def zone_apparat(ls):
    """Dernier groupe de lignes après le plus grand blanc de la moitié inférieure."""
    if len(ls) < 3:
        return None
    gaps = [(ls[k + 1][0] - ls[k][1], k + 1) for k in range(len(ls) - 1)]
    cand = [(g, k) for g, k in gaps if ls[k][0] > ls[0][0] + 300 and g > 110]
    if not cand:
        return None
    # le blanc retenu est le dernier blanc > 110 px suivi uniquement de lignes serrées
    for g, k in sorted(cand, key=lambda x: x[1]):
        suite = ls[k:]
        pas = [suite[j + 1][0] - suite[j][0] for j in range(len(suite) - 1)]
        if all(p < 66 for p in pas) or len(suite) == 1:
            return ls[k][0], ls[-1][1], len(suite)
    return None


def traiter(args):
    sortie, i, langues = args
    png = Path(sortie) / 'pages' / f'idx{i:03d}.png'
    dest = Path(sortie) / 'apparat'
    img = Image.open(png)
    z = zone_apparat(lignes(img))
    if not z:
        return i, None
    haut, bas, n = z
    crop = img.crop((0, max(0, haut - 15), img.width, min(img.height, bas + 15)))
    cp = dest / f'idx{i:03d}.png'
    crop.save(cp)
    txt = dest / f'idx{i:03d}.txt'
    if not txt.exists():
        r = subprocess.run(['tesseract', str(cp), 'stdout', '-l', langues, '--psm', '6'],
                           capture_output=True, text=True, env=dict(os.environ, OMP_THREAD_LIMIT='1'))
        tmp = txt.with_suffix('.part')
        tmp.write_text(unicodedata.normalize('NFC', r.stdout), encoding='utf-8')
        os.replace(tmp, txt)
    return i, z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sortie')
    ap.add_argument('--index', default='94-218')
    ap.add_argument('--pas', type=int, default=2)
    ap.add_argument('--langues', default='grc+lat')
    ap.add_argument('--processus', type=int, default=8)
    a = ap.parse_args()
    lo, hi = map(int, a.index.split('-'))
    os.makedirs(Path(a.sortie) / 'apparat', exist_ok=True)
    res = []
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for i, z in ex.map(traiter, [(a.sortie, i, a.langues) for i in range(lo, hi + 1, a.pas)]):
            res.append((i, z))
            print(i, z, flush=True)
    with open(Path(a.sortie) / 'apparat' / 'zones.tsv', 'w') as f:
        f.write('index\thaut\tbas\tlignes\n')
        for i, z in res:
            f.write(f'{i}\t' + ('\t'.join(map(str, z)) if z else '\t\t') + '\n')


if __name__ == '__main__':
    main()
