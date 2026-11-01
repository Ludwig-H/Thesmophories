#!/usr/bin/env python3
"""Rendu (≥ 400 dpi) et OCR Tesseract de pages choisies d'un PDF sans couche texte exploitable.

Écrit pour l'édition Prato 2001 (texte et apparat : index 90-221 ; divergences d'avec Coulon :
index 36-39 ; Appendice metrica : index 429-442), mais générique.

Les index sont ceux de pymupdf (base 0). Pour Prato 2001 : page imprimée = index - 86.
Sorties (reprise possible : ce qui existe déjà n'est pas refait) :
  <sortie>/pages/idxNNN.png   rendu en niveaux de gris
  <sortie>/ocr/idxNNN.txt     texte Tesseract (NFC)
  <sortie>/ocr/idxNNN.tsv     mots et boîtes (pour découper l'apparat)

Usage : python3 -I outils/prato2001_ocr.py PDF SORTIE --index 90-221,36-39 [--dpi 400]
        [--langues grc+ita] [--processus 8] [--suffixe ""]
"""
import argparse, concurrent.futures as cf, os, subprocess, unicodedata
from pathlib import Path


def rendre(pdf, i, dpi, png):
    if png.exists():
        return
    import pymupdf
    doc = pymupdf.open(pdf)
    tmp = png.with_suffix('.part.png')
    doc[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY).save(str(tmp))
    os.replace(tmp, png)


def traiter(args):
    pdf, i, dpi, langues, sortie, suffixe = args
    png = Path(sortie) / 'pages' / f'idx{i:03d}.png'
    base = Path(sortie) / 'ocr' / f'idx{i:03d}{suffixe}'
    txt = Path(str(base) + '.txt')
    if txt.exists():
        return i, 'déjà'
    rendre(pdf, i, dpi, png)
    tmpbase = str(base) + '.part'
    r = subprocess.run(['tesseract', str(png), tmpbase, '-l', langues, 'txt', 'tsv'],
                       capture_output=True, text=True, env=dict(os.environ, OMP_THREAD_LIMIT='1'))
    if r.returncode != 0:
        return i, 'erreur : ' + r.stderr[-300:]
    t = unicodedata.normalize('NFC', Path(tmpbase + '.txt').read_text(encoding='utf-8'))
    Path(tmpbase + '.txt').unlink()
    tsvdest = Path(str(base) + '.tsv')
    os.replace(tmpbase + '.tsv', tsvdest)
    tmp = Path(str(base) + '.txt.part')
    tmp.write_text(t, encoding='utf-8')
    os.replace(tmp, txt)
    return i, 'ok'


def plages(s):
    out = []
    for part in s.split(','):
        lo, _, hi = part.partition('-')
        out += range(int(lo), int(hi or lo) + 1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf'); ap.add_argument('sortie')
    ap.add_argument('--index', required=True, help='index pymupdf (base 0), ex. 90-221,36-39')
    ap.add_argument('--dpi', type=int, default=400)
    ap.add_argument('--langues', default='grc+ita')
    ap.add_argument('--processus', type=int, default=8)
    ap.add_argument('--suffixe', default='', help='suffixe des fichiers OCR (passe supplémentaire)')
    a = ap.parse_args()
    for d in ('pages', 'ocr'):
        os.makedirs(Path(a.sortie) / d, exist_ok=True)
    idx = plages(a.index)
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for i, etat in ex.map(traiter, [(a.pdf, i, a.dpi, a.langues, a.sortie, a.suffixe) for i in idx]):
            print(f'idx {i} : {etat}', flush=True)


if __name__ == '__main__':
    main()
