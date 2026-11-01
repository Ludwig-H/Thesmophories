#!/usr/bin/env python3
"""Spécimens et planches du guide de transcription (ravennas/GUIDE_TRANSCRIPTION.md).

Entrée : ravennas/graphologie/planches/specimens_guide.tsv
  (id, folio, x0, y0, x1, y1 en px de l'image pleine résolution, ligne, vers, planche, légende).
Sorties :
  - ravennas/graphologie/specimens/guide/<id>.png : découpe agrandie (LANCZOS), 600 px de large au plus
    (dossier ignoré par git, régénérable) ;
  - ravennas/graphologie/planches/guide_pl<n>.jpg : planches légendées (versionnées).
Usage : python3 outils/graphologie/specimens_guide.py
"""
import csv, glob, os
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
TSV = os.path.join(R, 'ravennas', 'graphologie', 'planches', 'specimens_guide.tsv')
SPEC = os.path.join(R, 'ravennas', 'graphologie', 'specimens', 'guide')
PLA = os.path.join(R, 'ravennas', 'graphologie', 'planches')
FD = '/home/codespace/.local/share/fonts/'
F_LEG = ImageFont.truetype(FD + 'LibertinusSerif-Regular.otf', 19)
F_REF = ImageFont.truetype(FD + 'LibertinusSerif-Italic.otf', 16)
F_TIT = ImageFont.truetype(FD + 'LibertinusSerif-Semibold.otf', 28)
TITRES = {'1': 'Guide de transcription. Planche 1 : confusions de lettres',
          '2': 'Guide de transcription. Planche 2 : ligatures et groupes',
          '3': 'Guide de transcription. Planche 3 : faux signes et abréviations de T',
          '4': 'Guide de transcription. Planche 4 : les lignes des exemples (§ 6)'}
LARG = 1800
_p = {}


def page(f):
    if f not in _p:
        _p[f] = Image.open(glob.glob(os.path.join(SRC, f'*_{f}_*.jpg'))[0]).convert('RGB')
    return _p[f]


def decoupe(r, emax, lmax):
    b = tuple(int(r[k]) for k in ('x0', 'y0', 'x1', 'y1'))
    c = page(r['folio']).crop(b)
    e = min(emax, lmax / c.width)
    return c.resize((max(1, round(c.width * e)), max(1, round(c.height * e))), Image.LANCZOS), e


def legende(d, x, y, r, e):
    d.text((x, y), r['legende'], fill=(20, 20, 20), font=F_LEG)
    d.text((x, y + 22), f"[{r['id']}] {r['folio']} l. {r['ligne']}, v. {r['vers']} ×{e:.1f}", fill=(90, 90, 90), font=F_REF)


def planche(n, rows):
    ex = n == '4'
    # disposition en rangées
    cells = [(r, *decoupe(r, 2.2 if ex else 3, 1760 if ex else 560)) for r in rows]
    lignes, cour, x = [], [], 20
    for c in cells:
        lw = max(c[1].width, F_LEG.getbbox(c[0]['legende'])[2], 250)
        if x + lw > LARG - 20 and cour:
            lignes.append(cour); cour, x = [], 20
        cour.append((c, x, lw)); x += lw + 24
    if cour:
        lignes.append(cour)
    H = 60 + sum(max(c[0][1].height for c in l) + 62 for l in lignes)
    im = Image.new('RGB', (LARG, H), 'white')
    d = ImageDraw.Draw(im)
    d.text((20, 14), TITRES.get(n, ''), fill=(0, 0, 0), font=F_TIT)
    y = 60
    for l in lignes:
        h = max(c[0][1].height for c in l)
        for (r, cim, e), x, lw in l:
            im.paste(cim, (x, y + h - cim.height))
            legende(d, x, y + h + 4, r, e)
        y += h + 62
    s = os.path.join(PLA, f'guide_pl{n}.jpg')
    im.save(s, quality=86)
    print(s, im.size)


def main():
    rows = list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))
    os.makedirs(SPEC, exist_ok=True)
    for r in rows:
        c, _ = decoupe(r, 4, 600)
        c.save(os.path.join(SPEC, r['id'] + '.png'))
    for n in sorted({r['planche'] for r in rows}):
        planche(n, [r for r in rows if r['planche'] == n])
    print(len(rows), 'spécimens')


if __name__ == '__main__':
    main()
