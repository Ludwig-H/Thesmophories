#!/usr/bin/env python3
"""Renumérotation des rangées de edition/folios/fXXX/texte.tex d'après la numérotation usuelle
(Hall–Geldart, .sources/corpus/thesmo_hall_geldart.tsv), par alignement du grec.

Règle : une rangée porte le plus petit numéro de vers usuel qu'elle chevauche (au moins trois
lettres alignées, ou la moitié d'un vers très court) et qu'aucune rangée précédente du folio ne
porte encore ; si tous les vers qu'elle chevauche sont déjà numérotés (le vers est coupé sur
plusieurs rangées), elle ne porte pas de numéro. Le fichier de référence (Perseus) fusionne
quelques répliques et saute quelques numéros : relire les propositions avant d'appliquer
(option --seulement fXXX:ligne,… pour n'appliquer qu'une sélection). Les rangées « suite » (antilabè) ne sont pas
touchées ; les vers supprimés par l'auteur (absents de texte.tex) laissent un trou.

Usage : python3 outils/controle/renumeroter.py [--appliquer] [fXXX ...]
Sans --appliquer : rapport des changements proposés (rien n'est écrit).
"""
import bisect, csv, difflib, json, os, re, sys, unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TSV = os.path.join(RACINE, '.sources', 'corpus', 'thesmo_hall_geldart.tsv')


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


def main():
    appliquer = '--appliquer' in sys.argv
    seulement = None
    if '--seulement' in sys.argv:
        seulement = set(sys.argv[sys.argv.index('--seulement') + 1].split(','))
    choix = [a for a in sys.argv[1:] if re.fullmatch(r'f\d+[rv]', a)]
    hg = [(int(r[0]), r[1]) for r in csv.reader(open(TSV, encoding='utf-8'), delimiter='\t')
          if len(r) >= 2 and r[0].strip().isdigit()]
    folios = json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))
    total = 0
    for f in folios:
        if choix and f['folio'] not in choix:
            continue
        p = os.path.join(RACINE, 'edition', 'folios', f['folio'], 'texte.tex')
        lignes = open(p, encoding='utf-8').read().split('\n')
        # texte usuel du folio (marge de 6 vers de part et d'autre)
        H, hstarts, hnums = '', [], []
        for n, t in hg:
            if f['v0'] - 6 <= n <= f['v1'] + 6:
                hstarts.append(len(H)); hnums.append(n); H += norm(t)
        # rangées
        rows, T = [], ''
        for i, l in enumerate(lignes):
            m = re.match(r'\\vers\[([^\]]*)\]', l)
            if not m:
                continue
            a = arguments(l, m.end())
            if len(a) < 4:
                continue
            g = norm(a[2])
            rows.append({'i': i, 'opts': m.group(1), 'start': len(T), 'end': len(T) + len(g), 'g': a[2]})
            T += g
        sm = difflib.SequenceMatcher(None, T, H, autojunk=False)
        blocs = [b for b in sm.get_matching_blocks() if b.size > 0]
        bstarts = [b.a for b in blocs]

        def vers_h(pos):
            """Position dans H correspondant à la position pos de T (ou None)."""
            k = bisect.bisect_right(bstarts, pos) - 1
            if k >= 0 and pos < blocs[k].a + blocs[k].size:
                return blocs[k].b + (pos - blocs[k].a)
            return None

        hends = hstarts[1:] + [len(H)]
        attribues = set()
        for r in rows:
            if re.search(r'(^|,)\s*suite\b', r['opts']):
                continue
            ancien = re.search(r'(?:^|,)\s*n=([^,\]]+)', r['opts'])
            ancien = ancien.group(1).strip() if ancien else ''
            hs = [vers_h(x) for x in range(r['start'], r['end'])]
            hs = [x for x in hs if x is not None]
            if not hs:
                if ancien.isdigit():
                    attribues.add(int(ancien))
                continue  # rangée non alignée (texte propre à l'auteur) : on ne touche à rien
            compte = {}
            for x in hs:
                k = bisect.bisect_right(hstarts, x) - 1
                compte[k] = compte.get(k, 0) + 1
            chev = sorted(hnums[k] for k, c in compte.items() if c >= min(3, max(1, (hends[k] - hstarts[k]) // 2)))
            libres = [v for v in chev if v not in attribues]
            nouveau = str(libres[0]) if libres else ''
            if nouveau:
                attribues.add(int(nouveau))
            if nouveau != ancien and not (not nouveau and not ancien):
                total += 1
                print(f"{f['folio']} l.{r['i'] + 1}: n={ancien or '∅'} → {nouveau or '∅'}   {r['g'][:50]}")
                if appliquer and (seulement is None or f"{f['folio']}:{r['i'] + 1}" in seulement):
                    o = re.sub(r'(^|,)\s*n=[^,\]]+', '', r['opts']).strip(', ')
                    o = (f'n={nouveau}' + (', ' + o if o else '')) if nouveau else o
                    lignes[r['i']] = lignes[r['i']].replace('\\vers[' + r['opts'] + ']', '\\vers[' + o + ']', 1)
        if appliquer:
            open(p, 'w', encoding='utf-8').write('\n'.join(lignes))
    print(f'{total} changement(s)' + (' appliqué(s)' if appliquer else ' proposé(s)'))


if __name__ == '__main__':
    main()
