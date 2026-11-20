#!/usr/bin/env python3
"""Lieux de R à examiner pour le dossier des cas philologiques (ravennas/CAS_PHILOLOGIQUES.md).

Un « cas philologique » est un lieu où l'état du manuscrit ou de sa tradition dit quelque chose
du texte : correction dans R (leçon première R^a.c. différente de la leçon corrigée, surtout si
elle forme un mot ou une forme réelle), main de la correction et date relative (M, copié vers 1505,
et la Juntine, 1516, en sont des témoins), variante ancienne (lemme ou u.l. des scholies, papyrus,
lexicographes, Souda), désaccord des éditeurs sur ce que porte R.

Le script rassemble, vers par vers, ce que signalent les sources déjà dépouillées et le confronte
à la transcription :
  - répertoire critique (edition/donnees/repertoire_critique.json) : leçons de R^a.c., R^p.c., R²,
    « a pr. m. », R douteux ; Juntine ; M (et M^a.c./M^p.c.) ; scholies (lemmes, u.l.) ; papyrus ;
    Souda, Hésychius, Pollux ;
  - inventaires graphologiques (ravennas/graphologie/folios/fXXX.jsonl) : corrections, grattages,
    surcharges relevés sur l'image ;
  - transcription (ravennas/transcription/fXXX.xml, à défaut les brouillons A et B) : interventions
    balisées (<subst>, <del>, <ras>, <add>, <corr>).
Il signale en tête les lieux où une source rapporte une correction dans R alors que la
transcription n'en porte aucune (cas de κυνδ' > κύβδ', v. 489, que les deux lecteurs ont manqué).

Sortie : ravennas/cas/lieux_a_examiner.tsv (une ligne par lieu et par source) et un bilan à l'écran.
Usage : python3 outils/transcription/lieux_a_examiner.py
"""
import csv, glob, json, os, re, sys, unicodedata
from collections import defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'transcription'))
from diploxml import lire  # noqa: E402

SORTIE = os.path.join(RACINE, 'ravennas', 'cas', 'lieux_a_examiner.tsv')

R_CORR = re.compile(r'^R\s*(\^\s*(ac|pc|a\.?\s*c\.?|p\.?\s*c\.?|1|2|s|mg|sl|γρ)|²|¹|\s*\((a pr\. m\.|pr\. m\.|corr|ex corr|in ras|fortasse|ut videtur|s\. ?l\.|in marg)[^)]*\))', re.I)
JUNT = re.compile(r'Iunt|Junt|Iuntina|Juntine', re.I)
M_ = re.compile(r'^M(\^|\s*\(|$)')
SCHOL = re.compile(r'(^Σ|schol|scholiast|sch\.|v\.l\. ap\. sch)', re.I)
PAP = re.compile(r'^(Π|P\d|P\.Oxy|PSI)', re.I)
TESTIM = re.compile(r'(Su\.|Suid|Souda|Hesych|Pollux|Poll\.|Phot|EM\b|Et\. ?M)', re.I)


def plier(t):
    t = unicodedata.normalize('NFD', (t or '').lower())
    return ''.join(c for c in t if 'α' <= c <= 'ω').replace('ς', 'σ')


def categorie(t):
    if R_CORR.search(t):
        return 'R_corr'
    if JUNT.search(t):
        return 'Junt'
    if M_.match(t):
        return 'M_corr' if '^' in t else 'M'
    if PAP.match(t):
        return 'papyrus'
    if SCHOL.search(t):
        return 'scholies'
    if TESTIM.search(t):
        return 'testim'
    return None


def lecon_de_texte(lec):
    """Vrai pour une leçon du texte (au moins un mot grec de 5 lettres ou plus), faux pour un sigle de
    personnage (« ευ^ρ », « μν̃η^σι »), une note d'ordre ou de ponctuation."""
    lec = lec or ''
    if '^' in lec or re.match(r'\s*(ordre|om\.|:|·)', lec):
        return False
    return any(len(plier(w)) >= 5 for w in lec.split())


def folio_de(v, bornes):
    m = re.match(r'\d+', str(v))
    if not m:
        return ''
    n = int(m.group())
    for f, a, b in bornes:
        if a <= n <= b:
            return f
    return ''


def transcription(folio):
    """{vers: (texte de la ligne, interventions)} d'après le fichier final, sinon les brouillons A puis B."""
    res = {}
    for p in (f'ravennas/transcription/{folio}.xml', f'ravennas/transcription/brouillons/{folio}_A.xml',
              f'ravennas/transcription/brouillons/{folio}_B.xml'):
        p = os.path.join(RACINE, p)
        if not os.path.exists(p):
            continue
        try:
            r = lire(p)
        except Exception:
            continue
        for l in r.iter('l'):
            for v in (l.get('v') or '').split(','):
                v = v.strip()
                if not v or v in res:
                    continue
                inter = []
                for el in l.iter():
                    if el.tag in ('subst', 'del', 'ras', 'add', 'corr'):
                        txt = ''.join(el.itertext()).strip()
                        inter.append(f"{el.tag}[{el.get('main') or ''}{(' ' + el.get('type')) if el.get('type') else ''}]:{txt}")
                res[v] = (f"l. {l.get('n')} ({os.path.basename(p)}) " + ' '.join(''.join(l.itertext()).split()), inter)
    return res


def main():
    bornes = [(f['folio'], f['v0'], f['v1']) for f in json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))]
    rep = json.load(open(os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique.json'), encoding='utf-8'))
    lignes = []
    cache = {}
    for v, items in rep.items():
        f = folio_de(v, bornes)
        if not f:
            continue
        cats = defaultdict(list)
        lecons_R = set()
        for it in items:
            for t in it['temoins']:
                if t.strip() == 'R':
                    lecons_R.add(plier(it['lecon']))
                c = categorie(t)
                if c:
                    cats[c].append((t, it))
        for c, lst in cats.items():
            for t, it in lst:
                # pour M, la Juntine, les scholies, les papyrus et les testimonia : seulement s'ils s'écartent de R
                if c in ('M', 'Junt', 'scholies', 'papyrus', 'testim') and plier(it['lecon']) in lecons_R:
                    continue
                if f not in cache:
                    cache[f] = transcription(f)
                tr = cache[f].get(re.match(r'\d+', v).group() if re.match(r'\d+', v) else v, ('', []))
                cit = ' | '.join((s.get('edition', '') + ' p. ' + str(s.get('page', '')) + ' : ' + (s.get('citation') or '')[:160]) for s in it['sources'][:2])
                lignes.append({'folio': f, 'vers': v, 'categorie': c, 'temoin': t, 'lecon': it['lecon'],
                               'editions': ', '.join(it['editions']), 'citation': cit.replace('\t', ' ').replace('\n', ' '),
                               'transcription': tr[0], 'interventions': ' ; '.join(tr[1]),
                               'alerte': 'correction rapportée, absente de la transcription' if c == 'R_corr' and tr[0] and not tr[1] and lecon_de_texte(it['lecon']) else ''})
    # inventaires graphologiques : corrections relevées sur l'image
    for p in sorted(glob.glob(os.path.join(RACINE, 'ravennas', 'graphologie', 'folios', 'f*.jsonl'))):
        f = os.path.basename(p)[:-6]
        for l in open(p, encoding='utf-8'):
            try:
                e = json.loads(l)
            except ValueError:
                continue
            proc = (e.get('proc') or '') + ' ' + (e.get('obj') or '')
            if not re.search(r'corr|grat|ras|surch|subst|biff|exponct|ajout|add', proc, re.I):
                continue
            lignes.append({'folio': f, 'vers': str(e.get('vers') or ''), 'categorie': 'inventaire', 'temoin': e.get('main') or '',
                           'lecon': (e.get('texte') or '')[:200], 'editions': '', 'citation': f"inventaire {e.get('obs', '')} ({e.get('certitude', '')})",
                           'transcription': '', 'interventions': '', 'alerte': ''})
    ordre = {'R_corr': 0, 'inventaire': 1, 'Junt': 2, 'M_corr': 3, 'scholies': 4, 'papyrus': 5, 'testim': 6, 'M': 7}
    cle = lambda x: (x['folio'], int(re.match(r'\d+', x['vers']).group()) if re.match(r'\d+', x['vers']) else 0, ordre.get(x['categorie'], 9))
    lignes.sort(key=cle)
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    champs = ['folio', 'vers', 'categorie', 'temoin', 'lecon', 'editions', 'citation', 'transcription', 'interventions', 'alerte']
    with open(SORTIE, 'w', encoding='utf-8', newline='') as fo:
        fo.write('# Lieux à examiner pour le dossier des cas philologiques (produit par outils/transcription/lieux_a_examiner.py ; ne pas modifier à la main)\n')
        w = csv.DictWriter(fo, fieldnames=champs, delimiter='\t')
        w.writeheader()
        w.writerows(lignes)
    from collections import Counter
    c = Counter(x['categorie'] for x in lignes)
    a = [x for x in lignes if x['alerte']]
    print(f'{len(lignes)} lignes → {os.path.relpath(SORTIE, RACINE)} ; par catégorie : ' + ', '.join(f'{k} {n}' for k, n in c.most_common()))
    print(f'{len(a)} corrections rapportées par les éditeurs sans intervention dans la transcription actuelle')
    for x in a[:12]:
        print(f"  {x['folio']} v. {x['vers']} : {x['temoin']} {x['lecon']} ({x['editions']})")


if __name__ == '__main__':
    main()
