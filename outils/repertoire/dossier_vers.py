#!/usr/bin/env python3
"""Dossier critique vers par vers, par folio : edition/donnees/dossiers/fXXX.md.

Pour chaque vers du folio : texte de l'auteur (travaux antérieurs), vulgate Hall–Geldart,
lecture de R selon notre transcription (si ravennas/transcription/fXXX.xml existe, états
avant/après correction), apparat de l'auteur, et, d'après le répertoire critique fusionné
(edition/donnees/repertoire_critique.json), leçons de R et des témoins rapportées par les
éditeurs, conjectures avec leurs auteurs et les éditions qui les adoptent.

Usage : python3 outils/repertoire/dossier_vers.py [fXXX ...]
"""
import csv, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'transcription'))
DON = os.path.join(RACINE, 'edition', 'donnees')


def tsv(p, cle='vers'):
    d = {}
    if not os.path.exists(p):
        return d
    with open(p, encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            d.setdefault(str(row.get(cle, '')).strip(), []).append(row)
    return d


def vulgate():
    d = {}
    p = os.path.join(RACINE, '.sources', 'corpus', 'thesmo_hall_geldart.tsv')
    if os.path.exists(p):
        for row in csv.reader(open(p, encoding='utf-8'), delimiter='\t'):
            if len(row) >= 2:
                d[row[0].strip()] = row[1].strip()
    return d


def transcription(folio):
    p = os.path.join(RACINE, 'ravennas', 'transcription', folio + '.xml')
    if not os.path.exists(p):
        return {}
    from diploxml import lire, texte_brut
    r = lire(p)
    par_vers, cur = {}, None
    for l in r.iter('l'):
        v = (l.get('v') or '').split(',')[0].strip()
        if v:
            cur = v
        if cur:
            pc, ac = texte_brut(l, 'pc'), texte_brut(l, 'ac')
            e = par_vers.setdefault(cur, {'pc': '', 'ac': ''})
            e['pc'] = (e['pc'] + ' ' + pc).strip()
            e['ac'] = (e['ac'] + ' ' + ac).strip()
    return par_vers


def main():
    folios = json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))
    if sys.argv[1:]:
        folios = [f for f in folios if f['folio'] in sys.argv[1:]]
    rep = json.load(open(os.path.join(DON, 'repertoire_critique.json'), encoding='utf-8')) if os.path.exists(os.path.join(DON, 'repertoire_critique.json')) else {}
    # vers intervertis par l'auteur (anomalies « transposition ») : on suit la numérotation usuelle
    transposes = set()
    anom = os.path.join(DON, 'travaux_anterieurs', 'anomalies.tsv')
    if os.path.exists(anom):
        for row in csv.DictReader(open(anom, encoding='utf-8'), delimiter='\t'):
            if row.get('code') == 'transposition':
                for a, b in re.findall(r'vv\. (\d+)-(\d+)', row.get('message', '')):
                    transposes.update(str(x) for x in range(int(a), int(b) + 1))
    auteur = {}
    for k, rows in tsv(os.path.join(DON, 'travaux_anterieurs', 'texte_grec.tsv')).items():
        for row in rows:
            kk = row.get('vers_HG', '') if k in transposes and (row.get('vers_HG') or '').isdigit() else k
            auteur.setdefault(kk, []).append(row)
    app = tsv(os.path.join(DON, 'travaux_anterieurs', 'apparat.tsv'))
    vul = vulgate()
    os.makedirs(os.path.join(DON, 'dossiers'), exist_ok=True)
    for f in folios:
        tr = transcription(f['folio'])
        out = [f"# Dossier critique — folio {f['folio']} (vv. {f['v0']}–{f['v1']})\n",
               "Généré par `outils/repertoire/dossier_vers.py` ; ne pas modifier à la main.\n"]
        for v in range(f['v0'], f['v1'] + 1):
            k = str(v)
            out.append(f'\n## v. {v}\n')
            for row in auteur.get(k, []):
                out.append(f"- **auteur** : {row.get('texte', '')}" + (f" *(partie {row['partie']})*" if row.get('partie') else ''))
            if k in vul:
                out.append(f'- **vulgate (HG)** : {vul[k]}')
            if k in tr:
                t = tr[k]
                out.append(f"- **R (notre transcription)** : {t['pc']}" + (f" — *avant correction* : {t['ac']}" if t['ac'] != t['pc'] else ''))
            for row in app.get(k, []):
                out.append(f"- **apparat de l'auteur** : {row.get('texte', '') or row.get('latex', '')}")
            items = rep.get(k, [])
            if items:
                out.append('- **répertoire critique** :')
                for it in items:
                    aut = '; '.join(f"{a} ({', '.join(e)})" for a, e in it.get('auteurs', {}).items())
                    tem = ', '.join(it.get('temoins', []))
                    ado = ', '.join(it.get('adoptee_par', []))
                    lec = it.get('lecon') or '—'
                    lem = ' / '.join(it.get('lemmes', []))
                    out.append(f"  - [{', '.join(it.get('types', []))}] « {lec} »" + (f" (lemme {lem})" if lem else '')
                               + (f" — témoins : {tem}" if tem else '') + (f" — auteurs : {aut}" if aut else '')
                               + (f" — adoptée par : {ado}" if ado else '') + f" — {', '.join(it.get('editions', []))}")
        open(os.path.join(DON, 'dossiers', f['folio'] + '.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f'{len(folios)} dossier(s) écrit(s) dans edition/donnees/dossiers/')


if __name__ == '__main__':
    main()
