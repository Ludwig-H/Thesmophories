#!/usr/bin/env python3
"""Cherche une chaîne (insensible à la casse et aux espaces) dans la couche texte d'un PDF
et affiche l'indice de page PDF, les deux premières lignes (titre courant) et le contexte.
Usage : chercher_pdf.py FICHIER.pdf MOTIF_REGEX [largeur_contexte]"""
import re, sys, pymupdf
f, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 200
d = pymupdf.open(f)
rx = re.compile(pat, re.I)
for i in range(d.page_count):
    t = d[i].get_text()
    flat = re.sub(r'\s+', ' ', t)
    for m in rx.finditer(flat):
        head = ' | '.join([l.strip() for l in t.strip().split('\n')[:3]])[:90]
        a, b = max(0, m.start() - w), min(len(flat), m.end() + w)
        print(f'[idx {i}] titre: {head}\n   … {flat[a:b]} …\n')
