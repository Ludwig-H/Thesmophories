#!/usr/bin/env python3
"""Fusionne les relevés du répertoire critique (edition/donnees/repertoire_critique/*.jsonl,
un fichier par édition et par tranche de vers) en un répertoire par vers :
edition/donnees/repertoire_critique.json, et un rapport des conflits d'attribution
edition/donnees/repertoire_conflits.md.

Pour chaque vers, les entrées qui donnent la même leçon (même texte, à la ponctuation et
aux espaces près) sont regroupées : témoins (R, R², G/M, Iunt.…), auteurs de la
conjecture (formes latinisées ramenées à la forme usuelle), éditions qui la rapportent,
éditions qui l'adoptent, citations exactes des apparats avec leurs pages.

Usage : python3 outils/repertoire/fusionner.py
"""
import glob, json, os, re, unicodedata
from collections import defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique')
DST = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique.json')
CONFLITS = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_conflits.md')

# formes latines → formes usuelles (complété par la forme entre parenthèses fournie par les relevés)
LATIN = {
    'Bisetus': 'Biset', 'Bisetum': 'Biset', 'Kusterus': 'Kuster', 'Kusterum': 'Kuster', 'Kuesterus': 'Kuster',
    'Fritzschius': 'Fritzsche', 'Fritzschium': 'Fritzsche', 'Dobraeus': 'Dobree', 'Dobraeum': 'Dobree',
    'Porsonus': 'Porson', 'Porsonum': 'Porson', 'Hermannus': 'Hermann', 'Hermannum': 'Hermann',
    'Brunckius': 'Brunck', 'Brunckium': 'Brunck', 'Bentleius': 'Bentley', 'Bentleium': 'Bentley',
    'Elmsleius': 'Elmsley', 'Reiskius': 'Reiske', 'Casaubonus': 'Casaubon', 'Meinekius': 'Meineke',
    'Meinekium': 'Meineke', 'Dindorfius': 'Dindorf', 'Dindorfium': 'Dindorf', 'Bothius': 'Bothe',
    'Bothium': 'Bothe', 'Hirschigius': 'Hirschig', 'Cobetus': 'Cobet', 'Cobetum': 'Cobet',
    'Herwerdenus': 'van Herwerden', 'Blaydesius': 'Blaydes', 'Engerus': 'Enger', 'Engerum': 'Enger',
    'Velsenius': 'Velsen', 'Bekkerus': 'Bekker', 'Bekkerum': 'Bekker', 'Invernizius': 'Invernizi',
    'Scaliger': 'Scaliger', 'Scaligerus': 'Scaliger', 'Grynaeus': 'Grynaeus', 'Gelenius': 'Gelenius',
    'Bergkius': 'Bergk', 'Bergkium': 'Bergk', 'Hillerus': 'Hiller', 'Hillerum': 'Hiller',
    'Reisigius': 'Reisig', 'Tyrwhittus': 'Tyrwhitt', 'Toupius': 'Toup', 'Valckenarius': 'Valckenaer',
    'Elmsleium': 'Elmsley', 'Seidlerus': 'Seidler', 'Lentingius': 'Lenting', 'Schaeferus': 'Schaefer',
    'Thierschius': 'Thiersch', 'Wellauerus': 'Wellauer', 'Boissonadius': 'Boissonade', 'Caninius': 'Canini',
    'Zanettus': 'Zanetti', 'Burgesius': 'Burges', 'Daubuzius': 'Daubuz', 'Faberus': 'Faber',
    'Hamakerus': 'Hamaker', 'Nauckius': 'Nauck', 'Kockius': 'Kock', 'Leeuwenius': 'van Leeuwen',
}


IGNORER = {'alii', 'libri', 'vulgo', 'codd', 'edd', 'vulg', 'plerique', 'nonnulli', 'quidam', 'omnes'}


def plier(a):
    d = unicodedata.normalize('NFD', a)
    return ''.join(c for c in d if not unicodedata.combining(c)).lower()


def norm_auteur(a):
    a = (a or '').strip()
    m = re.search(r'\(([^)]+)\)\s*$', a)
    if m:
        a = m.group(1).strip()
    a = re.sub(r'^(editio|ed\.|edd\.|editor|edition)\s+', '', a, flags=re.I)
    a = re.sub(r'\s+', ' ', a)
    a = LATIN.get(a, a)
    if a.endswith('ii') and a[:-1] in ('Canini',):
        a = a[:-1]
    if plier(a).strip('. ') in IGNORER:
        return ''
    return {'Kuster': 'Küster', 'Kusterus': 'Küster', 'Invernizzi': 'Invernizi', 'Caninii': 'Canini'}.get(a, a)


def norm_lecon(s):
    s = unicodedata.normalize('NFC', s or '')
    s = s.replace('’', "'").replace('᾽', "'").replace('ʼ', "'")
    s = re.sub(r'[·.,;:!?«»"()\[\]]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def cle_vers(v):
    m = re.match(r'(\d+)', str(v))
    return (int(m.group(1)), str(v)) if m else (0, str(v))


def main():
    par_vers = defaultdict(lambda: defaultdict(lambda: {
        'lecon': None, 'lemmes': set(), 'types': set(), 'temoins': set(), 'auteurs': defaultdict(set),
        'editions': set(), 'adoptee_par': set(), 'sources': []}))
    n = 0
    for f in sorted(glob.glob(os.path.join(SRC, '*.jsonl'))):
        for ligne in open(f, encoding='utf-8'):
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                e = json.loads(ligne)
            except json.JSONDecodeError:
                continue
            n += 1
            v = str(e.get('v', '')).strip() or '?'
            lec = e.get('lecon') or ''
            k = norm_lecon(lec) if lec else ('§' + norm_lecon(e.get('lemme', '')) + '§' + e.get('type', ''))
            g = par_vers[v][k]
            g['lecon'] = g['lecon'] or lec
            if e.get('lemme'):
                g['lemmes'].add(e['lemme'])
            if e.get('type'):
                g['types'].add(e['type'])
            for t in e.get('temoins') or []:
                g['temoins'].add(t)
            ed = e.get('edition', os.path.basename(f).split('_')[0])
            g['editions'].add(ed)
            for a in e.get('auteurs') or []:
                g['auteurs'][norm_auteur(a)].add(ed)
            if e.get('adoptee_par_edition'):
                g['adoptee_par'].add(ed)
            g['sources'].append({'edition': ed, 'page': e.get('page'), 'citation': e.get('citation'), 'remarque': e.get('remarque') or ''})
    sortie, conflits = {}, []
    for v in sorted(par_vers, key=cle_vers):
        items = []
        for k, g in par_vers[v].items():
            auteurs = {a: sorted(eds) for a, eds in g['auteurs'].items() if a}
            it = {'lecon': g['lecon'], 'lemmes': sorted(g['lemmes']), 'types': sorted(g['types']),
                  'temoins': sorted(g['temoins']), 'auteurs': auteurs, 'editions': sorted(g['editions']),
                  'adoptee_par': sorted(g['adoptee_par']), 'sources': g['sources']}
            # conflit : deux éditions attribuent la même leçon à des critiques disjoints
            par_ed = defaultdict(set)
            for a, eds in auteurs.items():
                for ed in eds:
                    par_ed[ed].add(plier(a))
            eds = [x for x in par_ed.values() if x]
            if 'conjecture' in g['types'] and any(not (x & y) for i, x in enumerate(eds) for y in eds[i + 1:]):
                it['conflit_attribution'] = True
                conflits.append((v, g['lecon'], auteurs))
            items.append(it)
        sortie[v] = items
    json.dump(sortie, open(DST, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(CONFLITS, 'w', encoding='utf-8') as out:
        out.write('# Conflits d\'attribution dans le répertoire critique\n\n')
        out.write('Même leçon attribuée à des critiques différents selon les éditions (à trancher en remontant à la publication originale).\n\n')
        out.write('| vers | leçon | attributions (édition qui l\'affirme) |\n|---|---|---|\n')
        for v, lec, aut in conflits:
            out.write('| %s | %s | %s |\n' % (v, lec, ' ; '.join('%s (%s)' % (a, ', '.join(e)) for a, e in aut.items())))
    print(f'{n} entrées → {len(sortie)} vers ; {sum(len(x) for x in sortie.values())} leçons distinctes ; {len(conflits)} conflits d\'attribution')


if __name__ == '__main__':
    main()
