#!/usr/bin/env python3
"""Fusionne les relevés du répertoire critique (edition/donnees/repertoire_critique/*.jsonl,
un fichier par édition et par tranche de vers) en un répertoire par vers :
edition/donnees/repertoire_critique.json, et un rapport des conflits d'attribution
edition/donnees/repertoire_conflits.md.

Numérotation : chaque relevé suit les numéros de son édition ; la fusion les ramène à la
numérotation usuelle (celle du texte de l'édition) par la concordance
edition/donnees/concordance_vers.tsv, puis contrôle sur le texte : si le lemme ne se lit pas
dans le vers obtenu mais dans un voisin (± 3), l'entrée va à ce voisin. Le numéro de
l'édition est gardé dans chaque source (« v_edition ») quand il diffère.

Pour chaque vers, les entrées qui donnent la même leçon (même texte, à la ponctuation et
aux espaces près) sont regroupées : témoins (R, R², M, Iunt.…), auteurs de la
conjecture (formes latinisées ramenées à la forme usuelle), éditions qui la rapportent,
éditions qui l'adoptent, citations exactes des apparats avec leurs pages.

Usage : python3 outils/repertoire/fusionner.py
"""
import csv, glob, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique')
DST = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique.json')
CONFLITS = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_conflits.md')
sys.path.insert(0, os.path.join(RACINE, 'outils', 'controle'))
import concordance

# colonne de la concordance pour chaque édition relevée (clé = début du nom de fichier)
COLONNES = {'velsen1883': 'velsen1883', 'wilson2007': 'wilson2007', 'prato2001': 'prato2001',
            'enger1844': 'enger1844', 'blaydes1880': 'blaydes1880', 'vanleeuwen1904': 'vanleeuwen1904',
            'hallgeldart1907': 'hg1907', 'fritzsche1838': 'fritzsche1838', 'invernizi': 'invernizi1794',
            'rogers1904': 'usuel', 'iunta1515': 'hg_perseus'}

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
    'von Velsen': 'Velsen', 'Herwerden': 'van Herwerden', 'Tanneguy Le Fèvre': 'Faber',
    'Nicaise van Ellebode': 'Ellebodius', 'J. H. Voss': 'Voss', 'G. H. Schaefer': 'Schaefer',
    'J. Kaye': 'Kaye', 'L. Bachmann': 'Bachmann',
    'Anon. Par. ap. Rapheleng': 'anon. Parisinus', 'Anon. Par. ap. Rapheleng.': 'anon. Parisinus',
    'anonymus Parisinus': 'anon. Parisinus', 'Anon. apud Canini': 'anon. apud Canini',
}


IGNORER = {'alii', 'libri', 'vulgo', 'codd', 'edd', 'vulg', 'plerique', 'nonnulli', 'quidam', 'omnes'}


def sigle_temoin(t, edition):
    """Le Monacensis gr. 492 porte le sigle M dans toute l'édition : G (Velsen, Prato), Aug. (Enger), Mu2 (Wilson)."""
    if edition.startswith(('Velsen', 'Prato')):
        t = re.sub(r'^G(?=$|[\^ (])', 'M', t)
    elif edition.startswith('Enger'):
        t = re.sub(r'^Aug\.', 'M', t)
    return re.sub(r'^Mu2(?=$|[\^ (])', 'M', t)


def plier(a):
    d = unicodedata.normalize('NFD', a)
    return ''.join(c for c in d if not unicodedata.combining(c)).lower()


def norm_auteur(a):
    a = (a or '').strip()
    # Supprimer d'abord les dates de publication entre parenthèses, ex. « Austin (1987) »
    a = re.sub(r'\s*\(\s*\d{4}[a-z]?\s*\)', '', a)
    # Supprimer les précisions latines de lieu (ex. « , in adnotatione »)
    a = re.sub(r',\s*in\s+adnotatione\b.*$', '', a, flags=re.I)
    m = re.search(r'\(([^)]+)\)\s*$', a)
    if m and not re.fullmatch(r'[\d\s,.\-–p]+', m.group(1)):
        a = m.group(1).strip()
    a = re.sub(r'^(editio|ed\.|edd\.|editor|edition)\s+', '', a, flags=re.I)
    a = re.sub(r'\s+', ' ', a).strip()
    a = LATIN.get(a, a)
    if a.endswith('ii') and a[:-1] in ('Canini',):
        a = a[:-1]
    if not a or re.fullmatch(r'\d{4}[a-z]?', a) or plier(a).strip('. ') in IGNORER:
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


def grec(t):
    """Lettres grecques de base, sans diacritiques (comparaison de contenu)."""
    t = unicodedata.normalize('NFD', (t or '').lower())
    return ''.join(c for c in t if 'α' <= c <= 'ω').replace('ς', 'σ')


class Numerotation:
    """Conversion des numéros d'une édition vers la numérotation usuelle, avec contrôle sur le texte."""

    def __init__(self):
        self.tete, lignes = concordance.charger()
        self.index = {}          # colonne → numéro de l'édition → [vers usuels], par qualité
        for j, col in enumerate(self.tete):
            if col in ('usuel', 'incipit', 'notes'):
                continue
            d = defaultdict(lambda: ([], [], []))
            for l in lignes:
                if j >= len(l):
                    continue
                ns, approche, dedans = concordance.analyser(l[j])
                for n in ns:
                    d[n][2 if dedans else 1 if approche else 0].append(l[0])
            self.index[col] = d
        # texte de chaque vers usuel : auteur + vulgate (Perseus ramenée à l'usuel)
        self.texte = defaultdict(str)
        p = os.path.join(RACINE, 'edition', 'donnees', 'travaux_anterieurs', 'texte_grec.tsv')
        for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
            self.texte[r['vers']] += ' ' + grec(r['texte'])
            m = re.fullmatch(r'(\d+)-(\d+)', r.get('vers_fin') or '')
            if m:                                   # ligne de l'auteur à deux numéros
                for n in range(int(m.group(1)), int(m.group(2)) + 1):
                    self.texte[str(n)] += ' ' + grec(r['texte'])
        p = os.path.join(RACINE, '.sources', 'corpus', 'thesmo_hall_geldart.tsv')
        if os.path.exists(p):
            for r in csv.reader(open(p, encoding='utf-8'), delimiter='\t'):
                if len(r) >= 2:
                    for u in self.candidats('hg_perseus', r[0].strip()):
                        self.texte[u] += ' ' + grec(r[1])

    def candidats(self, col, numero):
        d = self.index.get(col)
        if d is None or col == 'usuel':
            return [numero] if re.fullmatch(r'\d+', numero) else [re.match(r'\d+', numero).group()] if re.match(r'\d+', numero) else []
        for cle in (numero, re.sub(r'[a-z]+$', '', numero)):
            if cle in d:
                francs, approches, dedans = d[cle]
                return francs or approches or dedans
        return [re.match(r'\d+', numero).group()] if re.match(r'\d+', numero) else []

    def lit(self, mots, u):
        t = self.texte.get(str(u), '')
        return bool(mots) and all(w in t for w in mots)

    def usuel(self, col, v, entree):
        """(clé de vers usuelle, déplacé par le contrôle du texte ?)."""
        v = str(v).strip()
        m = re.fullmatch(r'(\d+[a-z]?)\s*[-–]\s*(\d+[a-z]?)', v)
        if m:                                       # plage : bornes converties une à une
            a = (self.candidats(col, m.group(1)) or [m.group(1)])[0]
            b = (self.candidats(col, m.group(2)) or [m.group(2)])[-1]
            return (f'{a}–{b}' if a != b else a), False
        if not re.match(r'\d', v):
            return v, False                         # personae, titre, hypothesis
        cands = self.candidats(col, v)
        if not cands:
            return v, False
        essais = [[w for w in map(grec, re.split(r'[\s,.;·:]+', entree.get(c) or '')) if len(w) >= 3]
                  for c in ('lemme', 'lecon')]
        essais = [e for e in essais if e]
        for mots in essais:
            for u in cands:
                if self.lit(mots, u):
                    return u, False
        # déplacement d'après le texte : seulement pour une leçon (pas un sigle de personnage ni une
        # note) et sur des mots distinctifs (καὶ, ἂν, δαὶ… se lisent dans trop de vers voisins)
        if entree.get('type') in ('attribution', 'note', 'ponctuation', 'scholie'):
            return cands[0], False
        base = int(cands[0])
        for mots in essais:
            if not (any(len(w) >= 6 for w in mots) or sum(map(len, mots)) >= 9):
                continue
            for d in (-1, 1, -2, 2, -3, 3):
                if self.lit(mots, base + d):
                    return str(base + d), True
        return cands[0], False


def main():
    par_vers = defaultdict(lambda: defaultdict(lambda: {
        'lecon': None, 'lemmes': set(), 'types': set(), 'temoins': set(), 'auteurs': defaultdict(set),
        'editions': set(), 'adoptee_par': set(), 'sources': []}))
    n = 0
    num = Numerotation()
    bilan = defaultdict(Counter)
    for f in sorted(glob.glob(os.path.join(SRC, '*.jsonl'))):
        col = COLONNES.get(os.path.basename(f).split('_')[0], 'usuel')
        for ligne in open(f, encoding='utf-8'):
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                e = json.loads(ligne)
            except json.JSONDecodeError:
                continue
            n += 1
            v_ed = str(e.get('v', '')).strip() or '?'
            v, deplace = num.usuel(col, v_ed, e)
            bilan[col]['inchangé' if v == v_ed else 'déplacé (texte)' if deplace else 'converti (concordance)'] += 1
            lec = e.get('lecon') or ''
            k = norm_lecon(lec) if lec else ('§' + norm_lecon(e.get('lemme', '')) + '§' + e.get('type', ''))
            g = par_vers[v][k]
            g['lecon'] = g['lecon'] or lec
            if e.get('lemme'):
                g['lemmes'].add(e['lemme'])
            if e.get('type'):
                g['types'].add(e['type'])
            ed = e.get('edition', os.path.basename(f).split('_')[0])
            for t in e.get('temoins') or []:
                g['temoins'].add(sigle_temoin(t, ed))
            g['editions'].add(ed)
            for a in e.get('auteurs') or []:
                g['auteurs'][norm_auteur(a)].add(ed)
            if e.get('adoptee_par_edition'):
                g['adoptee_par'].add(ed)
            src = {'edition': ed, 'page': e.get('page'), 'citation': e.get('citation'), 'remarque': e.get('remarque') or ''}
            if v != v_ed:
                src['v_edition'] = v_ed
            g['sources'].append(src)
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
    for col, c in sorted(bilan.items()):
        print(f'  {col:16} ' + ' ; '.join(f'{k} : {x}' for k, x in sorted(c.items())))
    print(f'{n} entrées → {len(sortie)} vers ; {sum(len(x) for x in sortie.values())} leçons distinctes ; {len(conflits)} conflits d\'attribution')


if __name__ == '__main__':
    main()
