#!/usr/bin/env python3
"""OCR Tesseract (par défaut grc+lat) des pages d'un PDF sans couche texte (numérisations BSB, etc.).

Écrit un fichier de textes par page au format de .travail/editions_reprise/pages/ :
  {"source": "tesseract:<langues>", "pages": [...], "printed": [null...], "n": N}
Les pages déjà océrisées sont gardées dans <sortie>.d/ (reprise possible après interruption).

Usage : python3 -I outils/ocr_pdf.py FICHIER.pdf SORTIE.json.gz [--langues grc+lat] [--pages 1-50]
        [--processus 8] [--dpi 300]
Prérequis : tesseract ≥ 5 ; modèles dans TESSDATA_PREFIX ou .travail/tessdata/.
"""
import argparse, concurrent.futures as cf, gzip, json, os, subprocess, unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TESSDATA = os.environ.get('TESSDATA_PREFIX') or str(RACINE / '.travail' / 'tessdata')


def ocr_page(args):
    pdf, i, dpi, langues, dossier = args
    txt = Path(dossier) / f'p{i + 1:05d}.txt'
    if txt.exists():
        return i, txt.read_text(encoding='utf-8')
    import pymupdf
    doc = pymupdf.open(pdf)
    png = Path(dossier) / f'p{i + 1:05d}.png'
    doc[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY).save(str(png))
    r = subprocess.run(['tesseract', str(png), 'stdout', '-l', langues, '--tessdata-dir', TESSDATA],
                       capture_output=True, text=True)
    png.unlink(missing_ok=True)
    t = unicodedata.normalize('NFC', r.stdout)
    tmp = txt.with_suffix('.part')
    tmp.write_text(t, encoding='utf-8')
    os.replace(tmp, txt)
    return i, t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf'); ap.add_argument('sortie')
    ap.add_argument('--langues', default='grc+lat')
    ap.add_argument('--pages', default='')
    ap.add_argument('--processus', type=int, default=8)
    ap.add_argument('--dpi', type=int, default=300)
    a = ap.parse_args()
    import pymupdf
    n = pymupdf.open(a.pdf).page_count
    sel = range(n)
    if a.pages:
        sel = []
        for part in a.pages.split(','):
            lo, _, hi = part.partition('-')
            sel += range(int(lo) - 1, min(n, int(hi or lo)))
    dossier = a.sortie + '.d'
    os.makedirs(dossier, exist_ok=True)
    os.environ['OMP_THREAD_LIMIT'] = '1'
    pages = [''] * n
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for i, t in ex.map(ocr_page, [(a.pdf, i, a.dpi, a.langues, dossier) for i in sel]):
            pages[i] = t
    for f in Path(dossier).glob('p*.txt'):  # pages faites lors d'exécutions antérieures
        k = int(f.stem[1:]) - 1
        if 0 <= k < n and not pages[k]:
            pages[k] = f.read_text(encoding='utf-8')
    with gzip.open(a.sortie, 'wt', encoding='utf-8') as g:
        json.dump({'source': 'tesseract:' + a.langues, 'pages': pages, 'printed': [None] * n, 'n': n}, g,
                  ensure_ascii=False)
    print(a.sortie, n, sum(1 for p in pages if p.strip()), 'pages avec texte')


if __name__ == '__main__':
    main()
