#!/usr/bin/env python3
"""Redistribue rangées et articles entre les fichiers des folios selon les bornes de
vers de edition/folios/folios.json (après correction des bornes, par ex.).

- texte.tex : chaque \\vers (et les lignes \\rubrique, \\scene, \\didascalie, \\blanc qui le
  précèdent) va au folio qui contient son numéro de vers ; une ligne \\vers[suite] suit le
  vers précédent.
- commentaire.tex (\\comm), critique.tex (\\cc), paralleles.tex (\\lp), apparat.tex (\\app) :
  chaque article va au folio de son premier vers.
L'ordre est conservé ; les lignes d'en-tête (commentaires %) restent en place.

Usage : python3 outils/extraction/redistribuer.py [--essai]   (--essai : n'écrit rien)
"""
import json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOS = os.path.join(RACINE, 'edition', 'folios')


def folio_de(v, F):
    for f in F:
        if f['v0'] <= v <= f['v1']:
            return f['folio']
    return F[0]['folio'] if v < F[0]['v0'] else F[-1]['folio']


def blocs_texte(lignes):
    """Découpe texte.tex en blocs (en-tête, [lignes]) ; renvoie [(vers|None, [lignes])]."""
    blocs, attente, dernier_v = [], [], None
    for l in lignes:
        if l.startswith('%') and not blocs and not attente:
            blocs.append((None, [l]))
            continue
        if l.startswith('\\vers'):
            m = re.match(r'\\vers\[([^\]]*)\]', l)
            opts = m.group(1) if m else ''
            n = re.search(r'\bn=(\d+)', opts)
            if n:
                dernier_v = int(n.group(1))
            blocs.append((dernier_v, attente + [l]))
            attente = []
        else:
            attente.append(l)
    if attente:
        blocs.append((dernier_v, attente))
    return blocs


def articles(texte, macro):
    """Articles commençant par \\macro{ en début de ligne."""
    parties = re.split(r'(?m)^(?=\\%s\{)' % macro, texte)
    entete = parties[0] if not parties[0].startswith('\\' + macro + '{') else ''
    arts = [p for p in parties if p.startswith('\\' + macro + '{')]
    return entete, arts


def premier_vers(art, macro):
    m = re.match(r'\\%s\{([^}]*)\}' % macro, art)
    k = re.search(r'\d+', m.group(1)) if m else None
    return int(k.group()) if k else None


def main():
    essai = '--essai' in sys.argv
    F = json.load(open(os.path.join(DOS, 'folios.json')))
    noms = [f['folio'] for f in F]
    deplacements = []
    # texte.tex
    nouveaux = {n: [] for n in noms}
    entetes = {}
    for n in noms:
        p = os.path.join(DOS, n, 'texte.tex')
        if not os.path.exists(p):
            continue
        for v, bl in blocs_texte(open(p, encoding='utf-8').read().split('\n')):
            if v is None:
                entetes.setdefault(n, []).extend(bl)
                continue
            cible = folio_de(v, F)
            if cible != n:
                deplacements.append(('texte', v, n, cible))
            nouveaux[cible].extend(bl)
    if not essai:
        for n in noms:
            p = os.path.join(DOS, n, 'texte.tex')
            if os.path.exists(p) or nouveaux[n]:
                contenu = entetes.get(n, []) + [l for l in nouveaux[n]]
                open(p, 'w', encoding='utf-8').write('\n'.join(x for x in contenu).rstrip('\n') + '\n')
    # articles
    for fichier, macro in (('commentaire.tex', 'comm'), ('critique.tex', 'cc'), ('paralleles.tex', 'lp'), ('apparat.tex', 'app')):
        nouv = {n: [] for n in noms}
        ent = {}
        for n in noms:
            p = os.path.join(DOS, n, fichier)
            if not os.path.exists(p):
                continue
            e, arts = articles(open(p, encoding='utf-8').read(), macro)
            ent[n] = e
            for a in arts:
                v = premier_vers(a, macro)
                cible = folio_de(v, F) if v else n
                if cible != n:
                    deplacements.append((fichier, v, n, cible))
                nouv[cible].append(a)
        if not essai:
            for n in noms:
                p = os.path.join(DOS, n, fichier)
                if os.path.exists(p) or nouv[n]:
                    corps = ''.join(a if a.endswith('\n') else a + '\n' for a in nouv[n])
                    open(p, 'w', encoding='utf-8').write((ent.get(n) or '') + corps)
    for d in deplacements:
        print('%-16s v. %-5s %s → %s' % d)
    print(len(deplacements), 'déplacement(s)' + (' (essai, rien écrit)' if essai else ''))


if __name__ == '__main__':
    main()
