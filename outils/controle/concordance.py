#!/usr/bin/env python3
"""Conversion d'un numéro de vers des *Thesmophories* d'une édition (ou d'un fichier du dépôt) à une autre,
d'après edition/donnees/concordance_vers.tsv (une ligne par vers de la numérotation usuelle).

Notation des cellules du TSV :
  N        la ligne N de l'édition commence par ce vers usuel ;
  N–M      le vers usuel occupe les lignes N à M de l'édition ;
  (N)      le vers usuel commence à l'intérieur de la ligne N, qui commence par un vers usuel antérieur ;
  ~N       valeur approchée (partie lyrique dont la colométrie n'a pas été relue ligne à ligne) ;
  —        l'édition n'a pas de ligne pour ce vers (vers omis, supprimé, ou numéro sans texte) ;
  vide     non relevé.
Les numéros peuvent porter une lettre (330a, 994a, 1187b).

Usage :
  python3 outils/controle/concordance.py SOURCE NUMERO [CIBLE ...]
      SOURCE, CIBLE : nom de colonne (usuel, auteur, texte_tex, hg_perseus, hg1907, coulon1928, wilson2007,
      prato2001, velsen1883, enger1844, …) ; sans CIBLE : toutes les colonnes.
  python3 outils/controle/concordance.py --colonnes
  python3 outils/controle/concordance.py --zones SOURCE CIBLE   (plages où les deux numérotations diffèrent)
Exemples :
  python3 outils/controle/concordance.py texte_tex 373 usuel        → 372
  python3 outils/controle/concordance.py dindorf1835_anc 804 usuel
"""
import csv, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TSV = os.path.join(RACINE, 'edition', 'donnees', 'concordance_vers.tsv')


def charger():
    with open(TSV, encoding='utf-8') as f:
        r = csv.reader(f, delimiter='\t')
        tete = next(r)
        lignes = [l for l in r if l]
    return tete, lignes


def numeros(cell):
    """Ensemble des numéros (chaînes normalisées) désignés par une cellule ; et indicateurs."""
    c = cell.strip()
    if not c or c == '—':
        return [], False, False
    approx = c.startswith('~')
    c = c.lstrip('~')
    dedans = c.startswith('(')
    c = c.strip('()')
    m = re.fullmatch(r'(\d+)([a-z]?)[–-](\d+)([a-z]?)', c)
    if m:
        a, sa, b, sb = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)
        out = []
        for n in range(a, b + 1):
            out.append(str(n))
        if sa: out[0] = f'{a}{sa}'
        if sb: out.append(f'{b}{sb}')
        return out, approx, dedans
    return [c], approx, dedans


def cle(n):
    m = re.fullmatch(r'(\d+)([a-z]*)', n.strip())
    return (int(m.group(1)), m.group(2)) if m else (None, n)


def convertir(src, numero, cibles=None):
    tete, lignes = charger()
    if src not in tete:
        raise SystemExit(f'colonne inconnue : {src} (voir --colonnes)')
    js = tete.index(src)
    numero = numero.strip()
    trouve = []
    for l in lignes:
        if src == 'usuel':
            if l[0] == numero:
                trouve.append(l)
            continue
        ns, ap, de = numeros(l[js])
        if numero in ns and not (de and len(ns) == 1 and any(numero in numeros(x[js])[0] and not numeros(x[js])[2] for x in lignes if x is not l and x[0] < l[0])):
            trouve.append(l)
    if not trouve:
        # numéro avec lettre absent : essayer le numéro sans lettre
        n, s = cle(numero)
        if s and n is not None:
            return convertir(src, str(n), cibles)
        return None
    cibles = cibles or tete[2:]
    res = {'usuel': [l[0] for l in trouve], 'incipit': trouve[0][1]}
    for c in cibles:
        if c not in tete:
            raise SystemExit(f'colonne inconnue : {c}')
        j = tete.index(c)
        vals = []
        for l in trouve:
            v = l[j] if c != 'usuel' else l[0]
            if v and v not in vals:
                vals.append(v)
        res[c] = vals
    return res


def zones(a, b):
    tete, lignes = charger()
    ia, ib = tete.index(a), tete.index(b)
    out, cur = [], None
    for l in lignes:
        va, vb = (l[ia] if a != 'usuel' else l[0]), (l[ib] if b != 'usuel' else l[0])
        diff = va.strip('~') != vb.strip('~')
        if diff:
            if cur is None:
                cur = [l[0], l[0], []]
            cur[1] = l[0]; cur[2].append((l[0], va, vb))
        elif cur is not None:
            out.append(cur); cur = None
    if cur is not None:
        out.append(cur)
    return out


def main():
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'):
        print(__doc__); return
    if a[0] == '--colonnes':
        print(' '.join(charger()[0])); return
    if a[0] == '--zones':
        for d, f, det in zones(a[1], a[2]):
            print(f"usuel {d}–{f} : " + ' ; '.join(f'{u}: {a[1]} {x or "?"} / {a[2]} {y or "?"}' for u, x, y in det))
        return
    src, num = a[0], a[1]
    r = convertir(src, num, a[2:] or None)
    if r is None:
        print(f'{src} {num} : introuvable'); sys.exit(1)
    print(f"{src} {num} = usuel {', '.join(r['usuel'])} ({r['incipit']})")
    for c, v in r.items():
        if c in ('usuel', 'incipit'): continue
        print(f'  {c:18} {", ".join(v) if v else "—"}')


if __name__ == '__main__':
    main()
