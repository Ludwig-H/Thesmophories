#!/usr/bin/env python3
"""Contrôle de la répartition du commentaire (commentaire critique / commentaire de la pièce).

Pour chaque folio, compare les mots de l'ancien commentaire.tex (révision git de référence)
à ceux de commentaire.tex + critique.tex actuels : signale les mots disparus (perte de texte)
et les mots ajoutés (renvois, « je », coquilles corrigées), au-delà des changements attendus.
Usage : python3 outils/controle/repartition_commentaire.py [REVISION] [fXXX ...]
"""
import collections, os, re, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ATTENDUS = {'je', 'nous', 'pour', 'le', 'texte', 'voir', 'commentaire', 'critique', 'de', 'la', 'pièce',
            'me', 'moi', 'mon', 'ma', 'mes', 'notre', 'nos', 'ai', 'avons', 'suis', 'sommes', 'pensons', 'pense',
            'croyons', 'crois', 'proposons', 'propose', 'lisons', 'lis', 'préférons', 'préfère', 'retenons', 'retiens'}


def mots(t):
    t = re.sub(r'(?<!\\)%.*', '', t)                      # commentaires LaTeX
    t = re.sub(r'\\(comm|cc)\{[^}]*\}', ' ', t)           # plage
    t = re.sub(r'\\[a-zA-Z@]+\*?', ' ', t)                # macros
    t = re.sub(r'[{}\[\]~$&^_\\]', ' ', t)
    return collections.Counter(w.lower() for w in re.findall(r'\w+', t))


def git_show(rev, chemin):
    try:
        return subprocess.run(['git', '-C', RACINE, 'show', f'{rev}:{chemin}'], capture_output=True,
                              text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return ''


def main():
    args = sys.argv[1:]
    rev = args.pop(0) if args and not args[0].startswith('f') else 'db90b04'
    dos = os.path.join(RACINE, 'edition', 'folios')
    folios = args or sorted(d for d in os.listdir(dos) if os.path.exists(os.path.join(dos, d, 'critique.tex')))
    for f in folios:
        ancien = git_show(rev, f'edition/folios/{f}/commentaire.tex')
        nouveau = ''.join(open(os.path.join(dos, f, n), encoding='utf-8').read()
                          for n in ('commentaire.tex', 'critique.tex') if os.path.exists(os.path.join(dos, f, n)))
        a, b = mots(ancien), mots(nouveau)
        perdus = {w: a[w] - b[w] for w in a if a[w] > b[w] and w not in ATTENDUS}
        ajoutes = {w: b[w] - a[w] for w in b if b[w] > a[w] and w not in ATTENDUS}
        np, na = sum(perdus.values()), sum(ajoutes.values())
        etat = 'OK' if np <= 3 else 'À VOIR'
        print(f'{f}: {sum(a.values())} mots → {sum(b.values())} ; perdus {np}, ajoutés {na} — {etat}')
        if np > 3:
            print('   perdus :', ', '.join(f'{w}×{n}' for w, n in sorted(perdus.items(), key=lambda x: -x[1])[:25]))
        if na > 12:
            print('   ajoutés :', ', '.join(f'{w}×{n}' for w, n in sorted(ajoutes.items(), key=lambda x: -x[1])[:25]))


if __name__ == '__main__':
    main()
