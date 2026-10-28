#!/usr/bin/env python3
"""Contrôle des numéros de vers du répertoire critique : le lemme de chaque entrée se trouve-t-il
dans le vers indiqué (texte de Hall–Geldart, .sources/corpus/thesmo_hall_geldart.tsv, et texte de
l'auteur, edition/folios/*/texte.tex) ? Sinon, dans quel vers voisin (±1 à ±4) ?

Révèle les décalages de numérotation propres à chaque édition (une édition qui numérote
autrement que Hall–Geldart donne des décalages constants sur une plage de vers).
Usage : python3 outils/repertoire/controle_numerotation.py [--detail EDITION]
Écrit edition/donnees/repertoire_decalages.tsv (une ligne par entrée décalée).
"""
import csv, glob, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def norm(t):
    t = re.sub(r'\\[a-zA-Z@]+\*?', ' ', t or '')
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if 'α' <= c <= 'ω' or c == 'ς')
    return t.replace('ς', 'σ')


def textes():
    """Texte de chaque vers (numéro entier) : Hall–Geldart + auteur, normalisés."""
    v = defaultdict(str)
    p = os.path.join(RACINE, '.sources', 'corpus', 'thesmo_hall_geldart.tsv')
    for r in csv.reader(open(p, encoding='utf-8'), delimiter='\t'):
        m = re.match(r'(\d+)', r[0]) if r else None
        if m and len(r) >= 2:
            v[int(m.group(1))] += ' ' + norm(r[1])
    for p in glob.glob(os.path.join(RACINE, 'edition', 'folios', 'f*', 'texte.tex')):
        cur = None
        for l in open(p, encoding='utf-8'):
            m = re.match(r'\\vers\[([^\]]*)\]\{[^}]*\}\{[^}]*\}\{(.*?)\}\{', l)
            if not m:
                continue
            n = re.search(r'(?:^|,)\s*n=(\d+)', m.group(1))
            if n:
                cur = int(n.group(1))
            if cur:
                v[cur] += ' ' + norm(m.group(2))
    return v


def mots_lemme(e):
    """Mots grecs significatifs du lemme (ou, à défaut, de la leçon)."""
    src = e.get('lemme') or ''
    if not norm(src):
        src = e.get('lecon') or ''
    mots = [norm(w) for w in re.split(r'[\s,.;·:]+', src)]
    return [w for w in mots if len(w) >= 3]


def main():
    detail = sys.argv[sys.argv.index('--detail') + 1] if '--detail' in sys.argv else None
    V = textes()
    stats = defaultdict(Counter)
    lignes = []
    for p in sorted(glob.glob(os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique', '*.jsonl'))):
        for l in open(p, encoding='utf-8'):
            try:
                e = json.loads(l)
            except ValueError:
                continue
            m = re.match(r'(\d+)', str(e.get('v', '')))
            mots = mots_lemme(e)
            if not m or not mots:
                continue
            v = int(m.group(1))
            ed = e.get('edition') or os.path.basename(p).split('_')[0]
            trouve = None
            for d in (0, -1, 1, -2, 2, -3, 3, -4, 4):
                if all(w in V.get(v + d, '') for w in mots):
                    trouve = d
                    break
            stats[ed][trouve if trouve is not None else 'absent'] += 1
            if trouve not in (0,):
                lignes.append([ed, str(v), str(trouve if trouve is not None else ''), e.get('lemme', ''), e.get('lecon', ''), e.get('page', '')])
                if detail and detail.lower() in ed.lower():
                    print(f"{ed} v.{v} décalage {trouve} : lemme « {e.get('lemme', '')} »")
    for ed, c in sorted(stats.items()):
        tot = sum(c.values())
        print(f"{ed:28} {tot:5} entrées — au vers indiqué {100 * c[0] / tot:5.1f} % ; "
              + ' ; '.join(f"{k:+d} : {c[k]}" for k in (-4, -3, -2, -1, 1, 2, 3, 4) if c[k])
              + f" ; introuvable : {c['absent']}")
    out = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_decalages.tsv')
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['edition', 'vers', 'decalage', 'lemme', 'lecon', 'page'])
        w.writerows(lignes)
    print(f'{len(lignes)} entrées hors du vers indiqué → {os.path.relpath(out, RACINE)}')


if __name__ == '__main__':
    main()
