#!/usr/bin/env python3
"""Conversion d'un numéro de vers des *Thesmophories* d'une édition (ou d'un fichier du dépôt) à une autre,
d'après edition/donnees/concordance_vers.tsv (une ligne par vers de la numérotation usuelle).
Méthode, sources et limites : recherche/numerotation_vers.md.

Notation des cellules du TSV :
  N        la ligne N de l'édition commence par ce vers usuel (ou, hors parties lyriques : le compte de l'édition donne N) ;
  N–M      le vers usuel couvre les lignes N à M, ou la ligne vaut les deux numéros ;
  (N)      le vers usuel commence à l'intérieur de la ligne N, qui commence par un vers usuel antérieur ;
  ~N       valeur conventionnelle ou approchée (partie lyrique ou prose : l'édition ne numérote pas ligne à ligne,
           ou le compte des lignes n'a pas pu être établi avec certitude) ;
  N*       l'édition imprime en regard de ce vers un autre numéro que son compte : voir la colonne notes ;
  —        pas de ligne propre pour ce numéro dans la numérotation usuelle ;
  vide     non établi.
Les numéros peuvent porter une lettre (330a, 994a, 1187b).

Usage :
  concordance.py SOURCE NUMERO [CIBLE ...]    convertit NUMERO de SOURCE vers les CIBLE (par défaut : toutes)
  concordance.py --colonnes                   liste des colonnes et des alias
  concordance.py --zones SOURCE CIBLE         plages où les deux numérotations diffèrent
  concordance.py --verifier                   contrôles de non-régression
Exemples :
  concordance.py texte_tex 373 usuel          → 372
  concordance.py dobree 804 usuel             → 797
  concordance.py usuel 1015 hg1907 wilson2007 velsen1883
"""
import csv, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TSV = os.path.join(RACINE, 'edition', 'donnees', 'concordance_vers.tsv')
ALIAS = {
    'ancienne': 'dindorf1835_anc', 'dobree': 'dindorf1835_anc', 'kuster1710': 'dindorf1835_anc', 'bergler1760': 'dindorf1835_anc',
    'kuster': 'dindorf1835_anc', 'bergler': 'dindorf1835_anc', 'texte': 'texte_tex', 'perseus': 'hg_perseus', 'hg': 'hg1907',
    'coulon': 'coulon1928', 'wilson': 'wilson2007', 'prato': 'prato2001', 'velsen': 'velsen1883', 'enger': 'enger1844',
    'blaydes': 'blaydes1880', 'fritzsche': 'fritzsche1838', 'meineke': 'meineke1860', 'bergk': 'bergk1872', 'bekker': 'bekker1829',
    'invernizi': 'invernizi1794', 'brunck': 'brunck1783', 'bothe': 'bothe1830', 'vanleeuwen': 'vanleeuwen1904', 'dindorf': 'dindorf1835',
}


def charger():
    with open(TSV, encoding='utf-8') as f:
        r = csv.reader(f, delimiter='\t')
        tete = next(r)
        lignes = [l for l in r if l]
    return tete, lignes


def analyser(cell):
    """(liste des numéros, approché, à l'intérieur d'une ligne)."""
    c = cell.strip().replace('*', '')
    if not c or c == '—':
        return [], False, False
    approx = c.startswith('~')
    c = c.lstrip('~')
    dedans = c.startswith('(')
    c = c.strip('()')
    m = re.fullmatch(r'(\d+)([a-z]?)–(\d+)([a-z]?)', c)
    if m:
        a, sa, b, sb = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)
        out = [str(n) for n in range(a, b + 1)]
        if sa:
            out.insert(1, f'{a}{sa}')
        if sb:
            out.append(f'{b}{sb}')
        return out, approx, dedans
    return ([c] + ([re.match(r'\d+', c).group()] if re.search(r'[a-z]$', c) else [])), approx, dedans


def colonne(nom, tete):
    nom = ALIAS.get(nom, nom)
    if nom not in tete:
        raise SystemExit(f'colonne inconnue : {nom} (voir --colonnes)')
    return nom


def convertir(src, numero, cibles=None):
    """Lignes (vers usuels) où NUMERO de SRC est le début d'une ligne, sinon l'intérieur d'une ligne."""
    tete, lignes = charger()
    src = colonne(src, tete)
    numero = numero.strip()
    if src == 'usuel':
        trouve = [l for l in lignes if l[0] == numero]
    else:
        j = tete.index(src)
        francs, approches, dedans = [], [], []
        for l in lignes:
            ns, ap, de = analyser(l[j])
            if numero in ns:
                (dedans if de else approches if ap else francs).append(l)
        trouve = francs or approches or dedans
        if not trouve:
            m = re.fullmatch(r'(\d+)[a-z]+', numero)
            if m:
                return convertir(src, m.group(1), cibles)
    if not trouve:
        return None
    cibles = [colonne(c, tete) for c in cibles] if cibles else tete[2:-1]
    res = {'usuel': [l[0] for l in trouve], 'incipit': trouve[0][1], 'notes': [l[-1] for l in trouve if l[-1]]}
    for c in cibles:
        if c == 'usuel':
            continue
        j = tete.index(c)
        vals = []
        for l in trouve:
            if l[j] and l[j] not in vals:
                vals.append(l[j])
        res[c] = vals
    return res


def zones(a, b):
    tete, lignes = charger()
    a, b = colonne(a, tete), colonne(b, tete)
    ia, ib = tete.index(a) if a != 'usuel' else 0, tete.index(b) if b != 'usuel' else 0
    out, cur = [], None
    for l in lignes:
        va, vb = l[ia], l[ib]
        na, nb = analyser(va)[0], analyser(vb)[0]
        diff = bool(na and nb and not set(na) & set(nb))
        if diff:
            if cur is None:
                cur = [l[0], l[0], []]
            cur[1] = l[0]
            cur[2].append((l[0], va, vb))
        elif cur is not None:
            out.append(cur)
            cur = None
    if cur is not None:
        out.append(cur)
    return out


def verifier():
    attendu = [('texte_tex', '373', '372'), ('texte_tex', '434', '433'), ('texte_tex', '687', '688'), ('texte_tex', '1016', '1015'),
               ('dobree', '804', '797'), ('hg1907', '1016', '1015'), ('auteur', '1015', '1015'), ('invernizi1794', '380', '374'),
               ('fritzsche1838', '370', '372'), ('dindorf1835_anc', '860', '853'), ('coulon1928', '115', '115'), ('wilson2007', '1187b', '1187')]
    ko = 0
    for src, n, u in attendu:
        r = convertir(src, n, ['usuel'])
        ok = r is not None and u in r['usuel']
        ko += not ok
        print(('ok ' if ok else 'ÉCHEC'), f'{src} {n} → usuel {r["usuel"] if r else None} (attendu {u})')
    return ko


def main():
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'):
        print(__doc__)
        return
    if a[0] == '--colonnes':
        t = charger()[0]
        print(' '.join(t[:1] + t[2:-1]))
        print('alias :', ', '.join(f'{k}={v}' for k, v in ALIAS.items()))
        return
    if a[0] == '--verifier':
        sys.exit(1 if verifier() else 0)
    if a[0] == '--zones':
        for d, f, det in zones(a[1], a[2]):
            print(f'usuel {d}–{f} : ' + ' ; '.join(f'{u}: {x} / {y}' for u, x, y in det))
        return
    src, num = a[0], a[1]
    r = convertir(src, num, a[2:] or None)
    if r is None:
        print(f'{src} {num} : introuvable')
        sys.exit(1)
    print(f"{src} {num} = usuel {', '.join(r['usuel'])} ({r['incipit']})")
    for c, v in r.items():
        if c in ('usuel', 'incipit', 'notes'):
            continue
        print(f'  {c:18} {", ".join(v) if v else "—"}')
    for n in r['notes']:
        print('  note :', n)


if __name__ == '__main__':
    main()
