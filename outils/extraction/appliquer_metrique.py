#!/usr/bin/env python3
"""Applique aux fichiers edition/folios/fXXX/texte.tex :
- la scansion et les étiquettes métriques de edition/donnees/metrique/*.json
  (liste d'objets {"v": "101", "partie": "" | "a" | "b"…, "schema": "⏑⏑–⏑⏑–|…",
   "colon": "2an", "etiquette": "lyr." (facultatif : mètre affiché en marge au début d'une
   section), "renfoncement": 0–6 (facultatif, en em)}),
- les rubriques de structure de edition/donnees/structure.json
  (liste d'objets {"v": 1, "type": "rubrique" | "scene", "gr": "ΠΡΟΛΟΓΟΣ", "fr": "Prologue"}),
  insérées avant la rangée du vers indiqué (les anciennes \\rubrique et \\scene sont retirées).

Les options n=, suite et findent de \\vers sont conservées ; met= (schéma), colon= (nom du
colon, affiché dans une colonne alignée à droite du schéma), metre= et indent= sont
remplacées quand la donnée existe.
Usage : python3 outils/extraction/appliquer_metrique.py [--essai]
"""
import glob, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOS = os.path.join(RACINE, 'edition', 'folios')
MET = os.path.join(RACINE, 'edition', 'donnees', 'metrique')
STRUCT = os.path.join(RACINE, 'edition', 'donnees', 'structure.json')


def lire_metrique():
    m = {}
    for f in sorted(glob.glob(os.path.join(MET, '*.json'))):
        for e in json.load(open(f, encoding='utf-8')):
            m[(str(e['v']), e.get('partie', '') or '')] = e
    return m


def options(s):
    """Découpe la liste d'options d'un \\vers (accolades équilibrées)."""
    out, cur, d = [], '', 0
    for c in s:
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
        if c == ',' and d == 0:
            out.append(cur.strip()); cur = ''
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out


def main():
    essai = '--essai' in sys.argv
    M = lire_metrique()
    S = json.load(open(STRUCT, encoding='utf-8')) if os.path.exists(STRUCT) else []
    S_par_vers = {}
    for e in S:
        S_par_vers.setdefault(int(e['v']), []).append(e)
    n_met = n_struct = 0
    for p in sorted(glob.glob(os.path.join(DOS, 'f*', 'texte.tex'))):
        lignes = open(p, encoding='utf-8').read().split('\n')
        out, dernier_v, vus = [], None, set()
        for l in lignes:
            if S and (l.startswith('\\rubrique') or l.startswith('\\scene')):
                continue
            m = re.match(r'\\vers\[([^\]]*)\](.*)$', l)
            if m:
                opts = options(m.group(1))
                nv = next((o[2:] for o in opts if o.startswith('n=')), None)
                suite = 'suite' in opts
                if nv:
                    dernier_v = nv
                partie = 'b' if suite else ''
                v = int(re.match(r'\d+', dernier_v).group()) if dernier_v else None
                if v and nv and v in S_par_vers and v not in vus:
                    vus.add(v)
                    for e in S_par_vers[v]:
                        if e['type'] == 'rubrique':
                            out.append('\\rubrique{%s}{%s}' % (e.get('gr', ''), e.get('fr', '')))
                        else:
                            out.append('\\scene{%s}{%s}' % (e.get('gr', ''), e.get('fr', '')))
                        n_struct += 1
                e = M.get((dernier_v, partie)) or (M.get((dernier_v, '')) if not suite else None)
                if e:
                    opts = [o for o in opts if not o.startswith(('met=', 'metre=', 'colon=')) and not (o.startswith('indent=') and e.get('renfoncement') is not None)]
                    if e.get('schema'):
                        opts.append('met={%s}' % e['schema'])
                    if e.get('colon'):
                        opts.append('colon={%s}' % e['colon'])
                    if e.get('etiquette'):
                        opts.append('metre={%s}' % e['etiquette'])
                    if e.get('renfoncement') is not None and not suite:
                        opts.append('indent=%sem' % e['renfoncement'])
                    n_met += 1
                    l = '\\vers[%s]%s' % (', '.join(opts), m.group(2))
            out.append(l)
        if not essai:
            open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print(f'{n_met} rangées scandées, {n_struct} rubriques insérées' + (' (essai)' if essai else ''))


if __name__ == '__main__':
    main()
