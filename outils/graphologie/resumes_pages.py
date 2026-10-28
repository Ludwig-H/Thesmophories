#!/usr/bin/env python3
"""Rassemble les rendus structurés des inventaires graphologiques (journaux des workflows)
dans ravennas/graphologie/resume_pages.json : par page, mains, faits saillants, doutes.
Usage : python3 outils/graphologie/resumes_pages.py JOURNAL.jsonl [JOURNAL.jsonl ...]
"""
import json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SORTIE = os.path.join(RACINE, 'ravennas', 'graphologie', 'resume_pages.json')

pages = json.load(open(SORTIE, encoding='utf-8')) if os.path.exists(SORTIE) else {}
for j in sys.argv[1:]:
    for l in open(j, encoding='utf-8'):
        d = json.loads(l)
        if d.get('type') != 'result':
            continue
        r = d.get('result') or d.get('value')
        if isinstance(r, str):
            try:
                r = json.loads(r)
            except ValueError:
                continue
        if isinstance(r, dict) and r.get('folio'):
            m = re.match(r'f\d+[rv]', r['folio'])
            pages[m.group() if m else r['folio']] = {k: r.get(k) for k in ('mains', 'nb_interventions', 'nb_pieges', 'faits_saillants', 'doutes')}
json.dump(dict(sorted(pages.items())), open(SORTIE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(pages)} page(s) dans {os.path.relpath(SORTIE, RACINE)}')
