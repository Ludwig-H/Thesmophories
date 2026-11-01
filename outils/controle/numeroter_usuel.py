#!/usr/bin/env python3
"""Rétablit dans edition/folios/fXXX/texte.tex la numérotation usuelle (celle de Brunck, que suit
l'auteur : colonne « vers » de edition/donnees/travaux_anterieurs/texte_grec.tsv), à la place de la
numérotation de la numérisation Perseus (colonne « vers_HG ») reprise par erreur à la conversion.
Étude : recherche/numerotation_vers.md (§ 4–6).

Chaque rangée \\vers est retrouvée dans le TSV par son grec, dans l'ordre. Règles d'étiquette :
- rangée « suite » : pas de numéro (inchangée) ;
- partie b, c… qui n'est pas une « suite » : pas de numéro (le vers a déjà le sien) ;
- rangée à deux numéros (vers_fin) : le premier, ou le second s'il est multiple de 5, seul numéro
  imprimé en marge (434–435 → 435).
Écrit la table ancien → nouveau dans edition/donnees/numerotation_texte.tsv.

Usage : python3 outils/controle/numeroter_usuel.py [--appliquer]
Sans --appliquer : rapport seul (rien n'est écrit dans les folios).
"""
import csv, difflib, json, os, re, sys, unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TSV = os.path.join(RACINE, 'edition', 'donnees', 'travaux_anterieurs', 'texte_grec.tsv')
TABLE = os.path.join(RACINE, 'edition', 'donnees', 'numerotation_texte.tsv')


def norm(t):
    """Lettres grecques de base, sans diacritiques ni ponctuation ni commandes LaTeX."""
    t = re.sub(r'\\[a-zA-Z@]+\*?(\[[^\]]*\])?', ' ', t)
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if 'α' <= c <= 'ω' or c == 'ς')
    return t.replace('ς', 'σ')


def arguments(l, debut):
    """Les arguments {…} successifs à partir de la position debut."""
    args, i = [], debut
    while i < len(l) and l[i] == '{':
        d, j = 0, i
        while j < len(l):
            if l[j] == '{':
                d += 1
            elif l[j] == '}':
                d -= 1
                if d == 0:
                    break
            j += 1
        args.append(l[i + 1:j])
        i = j + 1
    return args


def etiquette(r):
    """Numéro imprimé de la rangée d'après le TSV ('' si le vers a déjà son numéro)."""
    if r['partie'] not in ('', 'a'):
        return ''
    v = r['vers']
    m = re.fullmatch(r'(\d+)-(\d+)', r['vers_fin'] or '')
    if m and int(m.group(2)) != int(v) and int(m.group(2)) % 5 == 0:
        return m.group(2)
    return v


def main():
    appliquer = '--appliquer' in sys.argv
    lignes_tsv = list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))
    for r in lignes_tsv:
        r['_n'] = norm(r['texte'])
    folios = json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))
    pris = [False] * len(lignes_tsv)
    table, changes, perdus = [], 0, 0
    pos = 0
    for f in folios:
        p = os.path.join(RACINE, 'edition', 'folios', f['folio'], 'texte.tex')
        lignes = open(p, encoding='utf-8').read().split('\n')
        for i, l in enumerate(lignes):
            m = re.match(r'\\vers\[([^\]]*)\]', l)
            if not m:
                continue
            a = arguments(l, m.end())
            if len(a) < 4:
                continue
            g = norm(a[2])
            # recherche dans le TSV : d'abord près de la position courante, à l'identique
            j = None
            for k in sorted(range(max(0, pos - 40), min(len(lignes_tsv), pos + 40)), key=lambda x: abs(x - pos)):
                if not pris[k] and lignes_tsv[k]['_n'] == g:
                    j = k
                    break
            if j is None:  # texte retouché depuis : meilleure ressemblance
                cand = [(difflib.SequenceMatcher(None, lignes_tsv[k]['_n'], g).ratio(), k)
                        for k in range(max(0, pos - 12), min(len(lignes_tsv), pos + 12)) if not pris[k]]
                if cand and max(cand)[0] >= 0.7:
                    j = max(cand)[1]
            if j is None:
                perdus += 1
                print(f"{f['folio']} l.{i + 1} : rangée non retrouvée : {a[2][:50]}")
                continue
            pris[j] = True
            pos = j + 1
            r = lignes_tsv[j]
            suite = bool(re.search(r'(^|,)\s*suite\b', m.group(1)))
            ancien = re.search(r'(?:^|,)\s*n=([^,\]]+)', m.group(1))
            ancien = ancien.group(1).strip() if ancien else ''
            nouveau = '' if suite else etiquette(r)
            table.append([f['folio'], i + 1, ancien, nouveau, r['vers'], r['partie'], r['vers_fin'], a[2][:40]])
            if nouveau != ancien:
                changes += 1
                if not appliquer:
                    print(f"{f['folio']} l.{i + 1} : {ancien or '∅'} → {nouveau or '∅'}   {a[2][:44]}")
                o = re.sub(r'(^|,)\s*n=[^,\]]+', '', m.group(1)).strip(', ')
                o = (f'n={nouveau}' + (', ' + o if o else '')) if nouveau else o
                lignes[i] = l.replace('\\vers[' + m.group(1) + ']', '\\vers[' + o + ']', 1)
        if appliquer:
            open(p, 'w', encoding='utf-8').write('\n'.join(lignes))
    with open(TABLE, 'w', encoding='utf-8', newline='') as fo:
        w = csv.writer(fo, delimiter='\t')
        w.writerow(['folio', 'ligne', 'ancien', 'nouveau', 'vers_auteur', 'partie', 'vers_fin', 'incipit'])
        w.writerows(table)
    print(f'{len(table)} rangées ; {changes} numéros changés ; {perdus} non retrouvées'
          + (' — appliqué' if appliquer else ' — essai'))


if __name__ == '__main__':
    main()
