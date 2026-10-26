#!/usr/bin/env python3
"""Affiche le contexte des occurrences d'un motif dans un texte OCR (djvu.txt)
et devine le numéro de page imprimé à partir des titres courants voisins.
Usage : contexte.py FICHIER MOTIF [avant] [après]"""
import re, sys
f, pat = sys.argv[1], sys.argv[2]
av = int(sys.argv[3]) if len(sys.argv) > 3 else 6
ap = int(sys.argv[4]) if len(sys.argv) > 4 else 12
L = open(f, encoding='utf-8', errors='replace').read().split('\n')
hdr = re.compile(r'^\s*(\d{1,4})\s{1,}[A-ZÄÖÜa-zäöü§IVX\.]|[A-Za-zäöü\.]\s+(\d{1,4})\s*$')
def page(i):
    for j in range(i, max(0, i - 120), -1):
        m = hdr.search(L[j])
        if m and len(L[j]) < 70:
            return (m.group(1) or m.group(2)), j
    return '?', None
rx = re.compile(pat)
for i, l in enumerate(L):
    if rx.search(l):
        p, j = page(i)
        print(f'--- ligne {i+1} (page ~{p}, titre ligne {j+1 if j else "?"})')
        print('\n'.join(L[max(0, i - av):i + ap]))
