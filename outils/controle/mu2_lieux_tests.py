#!/usr/bin/env python3
"""Construit edition/donnees/mu2_lieux_tests.tsv : collation du Monac. gr. 492 (Mu2) aux lieux-tests.

Entrées (non versionnées, relues sur l'image) : .travail/mu2/lectures_G.tsv, .travail/mu2/lieux.json.
Données saisies à la main : outils/controle/mu2_lieux_tests_donnees.py (une entrée par lieu).

Sigles des colonnes :
  R ante, R post : marque de T : « — » paragraphos, « : » dicolon, « blanc », « om. » (rien).
  main : T, S2, Rⁿ, 1516 (« 2 m. » de Velsen 1871), post-1516 ?, indét.
  conclusion : commence par l'une des catégories CAT ci-dessous.
"""
import csv, json, re, sys, collections
from pathlib import Path

B = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(B / 'outils' / 'controle'))
from mu2_lieux_tests_donnees import LIGNES  # noqa: E402

CAT = {
    'A': 'antérieur à Mu2',
    'P': 'postérieur à Mu2 (ou négligé)',
    'V': 'absent de Mu2',
    'N': 'non probant',
    'I': 'initiative de Mu2',
}


def folio(vue):
    n = (vue - 3) // 2
    return f"{n}{'r' if vue % 2 else 'v'}"


def main():
    lieux = {x['v']: x for x in json.load(open(B / '.travail/mu2/lieux.json', encoding='utf8'))}
    lect = {}
    for r in csv.DictReader(open(B / '.travail/mu2/lectures_G.tsv', encoding='utf8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        lect.setdefault(r['vers'], []).append(r)
    v83 = collections.defaultdict(list)
    for r in csv.DictReader(open(B / '.travail/mu2/velsen1883_R2.tsv', encoding='utf8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        n = re.match(r'\d+', r['v'])
        if n:
            v83[int(n.group())].append(re.sub(r'\s*\(PDF.*', '', r['page']).split(',')[0])
    sortie = []
    for e in LIGNES:
        v, lieu, ante, post, mn, mu2, cat, txt = e[:8]
        vn = int(re.match(r'\d+', str(v)).group())
        cle = str(v)
        if len(e) > 8:
            vue, lig = e[8]
        else:
            l0 = (lect.get(cle) or lect.get(str(vn)) or [None])[0]
            if l0:
                vue, lig = int(l0['vue']), l0['ligne']
            else:
                vue, lig = None, ''
        vtxt = f"{vue:04d}, l. {lig} (f. {folio(vue)})" if vue else '—'
        x = lieux.get(vn, {})
        gr = sorted(set(x.get('groupes', [])))
        gmap = {'a': 'a', 'b': 'b', 'b83': 'b (R² Velsen 1883)', 'c': 'c', 'c71': 'c (Velsen 1871)', 'c-probant': 'c (cas probant)'}
        groupe = ' ; '.join(gmap[g] for g in gr) or 'complément'
        src = []
        if vn in v83:
            src.append('Velsen 1883, ' + v83[vn][0])
        for z in x.get('velsen71', []):
            src.append(f'Velsen 1871, {z[2]}')
        for z in x.get('rep', [])[:1]:
            src.append(f"chap. 4, {z['page']} l. {z['ligne']}")
        src = ' ; '.join(dict.fromkeys(src))
        sortie.append([str(v), lieu, ante, post, mn, mu2, vtxt, f'{CAT[cat]} : {txt}' if txt else CAT[cat], groupe, src])
    ent = ['vers', 'lieu', 'R ante', 'R post', 'main', 'Mu2', 'vue BSB', 'conclusion', 'groupe', 'sources']
    with open(B / 'edition/donnees/mu2_lieux_tests.tsv', 'w', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\', lineterminator='\n')
        w.writerow(ent)
        w.writerows(sortie)
    # bilan
    bil = collections.Counter()
    for e in LIGNES:
        bil[(couche(e[4]), e[6])] += 1
    print(len(sortie), 'lignes')
    ks = sorted({k[0] for k in bil})
    print('couche\tA\tP\tV\tN\tI')
    for c in ks:
        print(c, *[bil[(c, k)] for k in 'APVNI'], sep='\t')


def couche(m):
    if m.startswith('post'):
        return 'post-1516'
    if m.startswith('1516'):
        return '1516'
    if 'Rⁿ' in m:
        return 'Rⁿ'
    if m.startswith('S2') or m.startswith('T + S2') or m.startswith('T/S2'):
        return 'S2'
    if m.startswith('T'):
        return 'T'
    return 'indét.'


if __name__ == '__main__':
    main()
