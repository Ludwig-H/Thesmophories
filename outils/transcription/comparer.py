#!/usr/bin/env python3
"""Compare deux transcriptions DiploXML d'une même page (lectures indépendantes A et B),
et chacune avec un texte de référence (vulgate), pour préparer l'arbitrage.

Les différences sont classées : lettres, diacritiques (accents, esprits, iota),
ponctuation, et balises d'intervention (ajouts, grattages, substitutions, doutes, sigles…).

Usage :
  python3 outils/transcription/comparer.py A.xml B.xml [--ref .sources/corpus/thesmo_hall_geldart.tsv] [--json sortie.json]
Sortie : rapport Markdown sur la sortie standard (et JSON si demandé).
"""
import argparse, csv, difflib, json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diploxml import lire, texte_brut

PONCT = set('·.,;:;·\'’᾽‘"«»()[]—–-')


def sans_diacritiques(s):
    d = unicodedata.normalize('NFD', s)
    d = ''.join(c for c in d if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', d).replace('ς', 'σ').lower()


def sans_ponct(s):
    return re.sub(r'\s+', ' ', ''.join(c for c in s if c not in PONCT)).strip()


def balises(l):
    out = []
    for e in l.iter():
        if e is l or not isinstance(e.tag, str):
            continue
        if e.tag in ('add', 'del', 'subst', 'ras', 'unclear', 'gap', 'nota', 'parag', 'gl', 'abbr', 'hi', 'signe', 'sp'):
            attrs = ','.join(f'{k}={v}' for k, v in sorted(e.attrib.items()))
            txt = ''.join(e.itertext()).strip()
            out.append(f'{e.tag}[{attrs}]«{txt}»')
    return out


def diff_mots(a, b):
    sa, sb = a.split(), b.split()
    res = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
        if op != 'equal':
            res.append((op, ' '.join(sa[i1:i2]), ' '.join(sb[j1:j2])))
    return res


def classer(a, b):
    if a == b:
        return []
    cats = []
    if sans_ponct(sans_diacritiques(a)) != sans_ponct(sans_diacritiques(b)):
        cats.append('lettres')
    elif sans_ponct(a) != sans_ponct(b):
        cats.append('diacritiques')
    if [c for c in a if c in PONCT] != [c for c in b if c in PONCT]:
        cats.append('ponctuation')
    if not cats:
        cats.append('espaces')
    return cats


def lignes(xml):
    r = lire(xml)
    return {int(l.get('n')): l for l in r.iter('l')}, r


def vers_texte(r):
    """Texte par vers (état final), en concaténant les lignes d'un même vers."""
    par_vers, cur = {}, None
    for l in r.iter('l'):
        v = (l.get('v') or '').split(',')[0].strip()
        if v:
            cur = v
        if cur and l.get('zone', 'texte') == 'texte':
            par_vers[cur] = (par_vers.get(cur, '') + ' ' + texte_brut(l, 'pc')).strip()
    return par_vers


def lire_ref(tsv):
    ref = {}
    with open(tsv, encoding='utf-8') as f:
        for row in csv.reader(f, delimiter='\t'):
            if len(row) >= 2 and re.match(r'^\d+', row[0]):
                ref[row[0].strip()] = row[1].strip()
    return ref


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('a'); ap.add_argument('b')
    ap.add_argument('--ref')
    ap.add_argument('--json')
    a = ap.parse_args()
    LA, RA = lignes(a.a)
    LB, RB = lignes(a.b)
    rapport = {'lignes': [], 'vers_ref': []}
    print(f'# Comparaison {os.path.basename(a.a)} / {os.path.basename(a.b)}\n')
    print(f'Lignes : A = {len(LA)}, B = {len(LB)}\n')
    for n in sorted(set(LA) | set(LB)):
        la, lb = LA.get(n), LB.get(n)
        if la is None or lb is None:
            print(f'- l. {n} : présente dans {"A" if la is not None else "B"} seulement')
            rapport['lignes'].append({'n': n, 'absente': 'B' if la is not None else 'A'})
            continue
        ent = {'n': n, 'vA': la.get('v'), 'vB': lb.get('v')}
        diffs = []
        for etat in ('pc', 'ac'):
            ta, tb = texte_brut(la, etat), texte_brut(lb, etat)
            c = classer(ta, tb)
            if c:
                diffs.append({'etat': etat, 'categories': c, 'A': ta, 'B': tb, 'mots': diff_mots(ta, tb)})
        ba, bb = balises(la), balises(lb)
        if ba != bb:
            diffs.append({'etat': 'balises', 'A': ba, 'B': bb})
        if la.get('v') != lb.get('v'):
            diffs.append({'etat': 'numérotation', 'A': la.get('v'), 'B': lb.get('v')})
        if diffs:
            ent['differences'] = diffs
            rapport['lignes'].append(ent)
            print(f'## l. {n} (v. {la.get("v") or lb.get("v") or "—"})')
            for d in diffs:
                if d['etat'] in ('pc', 'ac'):
                    print(f"- {d['etat']} [{', '.join(d['categories'])}] : " + ' ; '.join(f'A « {x} » / B « {y} »' for _, x, y in d['mots']))
                else:
                    print(f"- {d['etat']} : A {d['A']} / B {d['B']}")
    if a.ref:
        ref = lire_ref(a.ref)
        print('\n# Écarts avec le texte de référence (état final, lettres seulement)\n')
        for nom, R in (('A', RA), ('B', RB)):
            vt = vers_texte(R)
            for v, t in vt.items():
                r = ref.get(v)
                if r is None:
                    continue
                if sans_ponct(sans_diacritiques(t)) != sans_ponct(sans_diacritiques(r)):
                    dm = diff_mots(sans_ponct(sans_diacritiques(r)), sans_ponct(sans_diacritiques(t)))
                    rapport['vers_ref'].append({'lecture': nom, 'v': v, 'ref': r, 'trans': t, 'mots': dm})
                    print(f'- {nom} v. {v} : ' + ' ; '.join(f'réf. « {x} » → « {y} »' for _, x, y in dm))
    if a.json:
        json.dump(rapport, open(a.json, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
