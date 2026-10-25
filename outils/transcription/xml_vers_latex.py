#!/usr/bin/env python3
"""Convertit ravennas/transcription/fXXX.xml en edition/folios/fXXX/diplo.tex.
Usage : python3 outils/transcription/xml_vers_latex.py [fXXX ...]  (tous si aucun)"""
import glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diploxml import lire, valider, page_vers_latex

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    noms = sys.argv[1:] or [os.path.basename(p)[:-4] for p in sorted(glob.glob(os.path.join(RACINE, 'ravennas', 'transcription', 'f*.xml')))]
    code = 0
    for nom in noms:
        src = os.path.join(RACINE, 'ravennas', 'transcription', nom + '.xml')
        r = lire(src)
        pb = valider(r)
        if pb:
            code = 1
            print(f'{nom} : {len(pb)} problème(s)'); [print('  -', p) for p in pb[:30]]
        dst = os.path.join(RACINE, 'edition', 'folios', nom, 'diplo.tex')
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'w', encoding='utf-8').write(page_vers_latex(r))
        print(f'{nom} → {os.path.relpath(dst, RACINE)}')
    sys.exit(code)


if __name__ == '__main__':
    main()
