#!/usr/bin/env python3
"""Planches de lecture par ligne pour les transcripteurs : pour chaque ligne de texte
segmentée (ravennas/segmentation/fXXX.json), deux demi-lignes chevauchantes, chacune
montrée en trois versions empilées et agrandies ×2 — original, CLAHE, étirement de
décorrélation Lab (cf. outils/images/ameliorer.py).

Sortie : .travail/lignes/fXXX/l<NN>_<a|b>.jpg (+ l<NN>_ctx.jpg : la ligne et ses voisines,
×1,4, pour le contexte et les ajouts interlinéaires).
Usage : OMP_NUM_THREADS=1 python3 outils/images/triptyques.py [--proc 6] [fXXX ...]
"""
import argparse, glob, json, os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageDraw, ImageFont

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(RACINE, 'ravennas', 'segmentation')
SRC = os.path.join(RACINE, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
AMEL = os.path.join(RACINE, '.travail', 'ameliorations')
DST = os.path.join(RACINE, '.travail', 'lignes')
VERSIONS = [('original', None), ('CLAHE', 'clahe.jpg'), ('décorrélation Lab', 'ds_lab.jpg')]


def police(t=18):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        if os.path.exists(p):
            return ImageFont.truetype(p, t)
    return ImageFont.load_default()


def empiler(ims, etiquettes, titre):
    f = police(18)
    w = max(i.size[0] for i in ims)
    h = sum(i.size[1] for i in ims) + 26 * len(ims) + 28
    out = Image.new('RGB', (w, h), 'white')
    d = ImageDraw.Draw(out)
    d.text((6, 4), titre, fill=(160, 0, 0), font=f)
    y = 28
    for im, et in zip(ims, etiquettes):
        d.text((6, y), et, fill=(90, 90, 90), font=f)
        y += 24
        out.paste(im, (0, y))
        y += im.size[1] + 2
    return out


def traiter(folio):
    seg = json.load(open(os.path.join(SEG, folio + '.json')))
    src = os.path.join(SRC, seg['source'])
    images = [Image.open(src).convert('RGB')]
    for _, nom in VERSIONS[1:]:
        p = os.path.join(AMEL, folio, nom)
        images.append(Image.open(p).convert('RGB') if os.path.exists(p) else images[0])
    out = os.path.join(DST, folio)
    os.makedirs(out, exist_ok=True)
    lignes = [l for l in seg['lignes']]
    for k, l in enumerate(lignes):
        x0, y0, x1, y1 = l.get('decoupe') or l['boite']
        mid = (x0 + x1) // 2
        recouv = (x1 - x0) // 8
        for suffixe, (a, b) in (('a', (x0, mid + recouv)), ('b', (mid - recouv, x1))):
            crops = [im.crop((a, y0, b, y1)) for im in images]
            crops = [c.resize((c.size[0] * 2, c.size[1] * 2), Image.LANCZOS) for c in crops]
            titre = f"{folio} · ligne {l['index']} · {'moitié gauche' if suffixe == 'a' else 'moitié droite'}"
            empiler(crops, [v[0] for v in VERSIONS], titre).save(os.path.join(out, f"l{l['index']:02d}_{suffixe}.jpg"), quality=88)
        # contexte : ligne précédente et suivante
        prev = lignes[k - 1] if k > 0 else l
        nxt = lignes[k + 1] if k + 1 < len(lignes) else l
        cy0 = (prev.get('decoupe') or prev['boite'])[1]
        cy1 = (nxt.get('decoupe') or nxt['boite'])[3]
        c = images[0].crop((x0, cy0, x1, cy1))
        c = c.resize((int(c.size[0] * 1.4), int(c.size[1] * 1.4)), Image.LANCZOS)
        c.save(os.path.join(out, f"l{l['index']:02d}_ctx.jpg"), quality=85)
    return folio, len(lignes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--proc', type=int, default=6)
    ap.add_argument('folios', nargs='*')
    a = ap.parse_args()
    fs = a.folios or sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(SEG, 'f*.json')))
    with ProcessPoolExecutor(a.proc) as ex:
        for f, n in ex.map(traiter, fs):
            print(f, n, flush=True)


if __name__ == '__main__':
    main()
