#!/usr/bin/env python3
"""Télécharge des pages choisies d'un livre d'archive.org (images servies par le BookReader,
URL https://archive.org/download/<id>/page/n<k>.jpg, k = numéro de feuillet « leafNum ») et les
assemble en un PDF (JPEG insérés tels quels). Utile quand l'item n'a pas de PDF (ex. Küster 1710).

Usage : python3 -I ia_pages_vers_pdf.py IDENTIFIANT SORTIE.pdf --pages 1-30,523-573 [--threads 4]
        [--largeur 0]  (0 = pleine résolution ; sinon page/n<k>_w<largeur>.jpg)
Les images sont mises en cache dans SORTIE.pdf.cache/ (reprise possible après interruption).
"""
import argparse, concurrent.futures as cf, os, time, urllib.request
import pymupdf
from PIL import Image


def get(url, tries=6, timeout=180):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (philologie; recherche)'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(3 + 5 * i)


def parse_pages(s):
    out = []
    for part in s.split(','):
        lo, _, hi = part.strip().partition('-')
        out += range(int(lo), int(hi or lo) + 1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ident'); ap.add_argument('out')
    ap.add_argument('--pages', required=True)
    ap.add_argument('--threads', type=int, default=4)
    ap.add_argument('--largeur', type=int, default=0)
    a = ap.parse_args()
    leaves = parse_pages(a.pages)
    cache = a.out + '.cache'
    os.makedirs(cache, exist_ok=True)

    def fetch(k):
        fn = os.path.join(cache, f'n{k:05d}.jpg')
        if os.path.exists(fn) and os.path.getsize(fn) > 5000:
            return fn
        suf = f'_w{a.largeur}' if a.largeur else ''
        data = get(f'https://archive.org/download/{a.ident}/page/n{k}{suf}.jpg')
        with open(fn + '.part', 'wb') as f:
            f.write(data)
        os.replace(fn + '.part', fn)
        return fn

    with cf.ThreadPoolExecutor(a.threads) as ex:
        files = list(ex.map(fetch, leaves))
    doc = pymupdf.open()
    for fn in files:
        with Image.open(fn) as im:
            w, h = im.size
        pw, ph = w * 72 / 300, h * 72 / 300  # 300 dpi nominaux
        page = doc.new_page(width=pw, height=ph)
        page.insert_image(page.rect, filename=fn)
    tmp = a.out + '.part.pdf'
    doc.save(tmp, garbage=3, deflate=True)
    os.replace(tmp, a.out)
    print(f'{a.out} : {len(files)} pages')


if __name__ == '__main__':
    main()
