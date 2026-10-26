#!/usr/bin/env python3
"""Contrôle de la numérotation des vers dans edition/folios/fXXX/texte.tex :
doublons, trous et retours en arrière (les vers transposés de l'auteur sont signalés à part)."""
import glob, json, os, re

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
folios = json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))
vus, prec = {}, None
for f in folios:
    p = os.path.join(RACINE, 'edition', 'folios', f['folio'], 'texte.tex')
    for i, l in enumerate(open(p, encoding='utf-8'), 1):
        m = re.match(r'\\vers\[([^\]]*)\]', l)
        if not m:
            continue
        n = re.search(r'(?:^|,)\s*n=([^,\]]+)', m.group(1))
        if not n:
            continue
        lab = n.group(1).strip()
        v = re.match(r'\d+', lab)
        if not v:
            continue
        v = int(v.group())
        if lab in vus:
            print(f"doublon   {lab:>6} : {f['folio']} l.{i} (déjà {vus[lab]})")
        vus[lab] = f"{f['folio']} l.{i}"
        if prec is not None:
            if v < prec:
                print(f"recul     {prec} → {lab} : {f['folio']} l.{i}")
            elif v > prec + 1:
                print(f"trou      {prec} → {lab} : {f['folio']} l.{i} (manque {', '.join(str(x) for x in range(prec + 1, v))})")
        if v < f['v0'] or v > f['v1']:
            print(f"hors folio {lab} : {f['folio']} (bornes {f['v0']}–{f['v1']})")
        prec = max(prec or 0, v)
