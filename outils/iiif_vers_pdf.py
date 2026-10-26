#!/usr/bin/env python3
"""Télécharge toutes les images d'un manifeste IIIF (v2 ou v3) et les assemble en un PDF
(JPEG insérés tels quels, sans recompression).
Usage : python3 -I iiif_vers_pdf.py MANIFESTE_URL SORTIE.pdf [--max-largeur 2000] [--threads 8] [--pages 1-50 | 1-30,519-577]
Les images intermédiaires sont mises en cache dans SORTIE.pdf.cache/ (supprimé à la fin si --nettoyer).
"""
import argparse, concurrent.futures as cf, io, json, os, sys, time, urllib.request
import pymupdf
from PIL import Image

def get(url, tries=5, timeout=120):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (philologie; recherche)'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 + 3 * i)

def canvases(man):
    if 'sequences' in man:  # v2
        out = []
        for c in man['sequences'][0]['canvases']:
            res = c['images'][0]['resource']
            svc = res.get('service', {})
            if isinstance(svc, list): svc = svc[0]
            out.append((c.get('label', ''), svc.get('@id') or svc.get('id'), res.get('@id')))
        return out
    out = []  # v3
    for c in man['items']:
        body = c['items'][0]['items'][0]['body']
        svc = body.get('service', [{}])
        svc = svc[0] if isinstance(svc, list) else svc
        out.append((c.get('label', ''), svc.get('@id') or svc.get('id'), body.get('id')))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('manifest'); ap.add_argument('out')
    ap.add_argument('--max-largeur', type=int, default=0, help='0 = pleine résolution')
    ap.add_argument('--threads', type=int, default=8)
    ap.add_argument('--pages', default='')
    ap.add_argument('--nettoyer', action='store_true')
    a = ap.parse_args()
    man = json.loads(get(a.manifest))
    cv = canvases(man)
    if a.pages:  # « 1-50 » ou liste « 1-30,519-577,845 » (rangs 1..n des canvases)
        sel = []
        for part in a.pages.split(','):
            lo, _, hi = part.strip().partition('-')
            sel += range(int(lo), int(hi or lo) + 1)
        cv = [cv[i - 1] for i in sel if 1 <= i <= len(cv)]
    cache = a.out + '.cache'; os.makedirs(cache, exist_ok=True)
    def fetch(i_c):
        i, (lab, svc, direct) = i_c
        fn = os.path.join(cache, f'{i:05d}.jpg')
        if os.path.exists(fn) and os.path.getsize(fn) > 1000:
            return fn
        size = f'{a.max_largeur},' if a.max_largeur else 'full'
        url = f'{svc}/full/{size}/0/default.jpg' if svc else direct
        try:
            data = get(url)
        except Exception:
            if svc and size == 'full':
                data = get(f'{svc}/full/max/0/default.jpg')
            else:
                raise
        with open(fn + '.part', 'wb') as f: f.write(data)
        os.replace(fn + '.part', fn)
        return fn
    with cf.ThreadPoolExecutor(a.threads) as ex:
        files = list(ex.map(fetch, enumerate(cv, 1)))
    doc = pymupdf.open()
    for fn in files:
        with Image.open(fn) as im:
            w, h = im.size
        # 1 px = 72/300 pt (≈ 300 dpi)
        pw, ph = w * 72 / 300, h * 72 / 300
        page = doc.new_page(width=pw, height=ph)
        page.insert_image(page.rect, filename=fn)
    lab = man.get('label', '')
    if isinstance(lab, dict): lab = ' '.join(sum(lab.values(), []))
    doc.set_metadata({'title': str(lab)[:250], 'subject': a.manifest})
    doc.save(a.out, garbage=3, deflate=True)
    print(f'{a.out}: {len(files)} pages')
    if a.nettoyer:
        for fn in files: os.remove(fn)
        os.rmdir(cache)

if __name__ == '__main__':
    main()
