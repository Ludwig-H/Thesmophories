#!/usr/bin/env python3
"""Index des cas philologiques : lit les notices de ravennas/cas/fXXX.md (titres « ## v. N — … »)
et réécrit le tableau de ravennas/CAS_PHILOLOGIQUES.md entre les marques « index : début / fin ».
Usage : python3 outils/transcription/index_cas.py"""
import glob, os, re

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOSSIER = os.path.join(RACINE, 'ravennas', 'CAS_PHILOLOGIQUES.md')


def main():
    cas = []
    for p in sorted(glob.glob(os.path.join(RACINE, 'ravennas', 'cas', 'f*.md'))):
        f = os.path.basename(p)[:-3]
        for l in open(p, encoding='utf-8'):
            m = re.match(r'##\s+(vv?\.\s*([\d]+)[^—]*)—\s*(.+)$', l.strip())
            if m:
                cas.append((int(m.group(2)), m.group(1).strip(), f, m.group(3).strip()))
    cas.sort()
    lignes = ['| Vers | Page | Cas | Notice |', '|---|---|---|---|']
    for n, v, f, titre in cas:
        lignes.append(f'| {v} | {f} | {titre} | [`cas/{f}.md`](cas/{f}.md) |')
    s = open(DOSSIER, encoding='utf-8').read()
    a = s.index('<!-- index : début -->') + len('<!-- index : début -->')
    b = s.index('<!-- index : fin -->')
    s = s[:a] + '\n' + '\n'.join(lignes) + '\n' + s[b:]
    open(DOSSIER, 'w', encoding='utf-8').write(s)
    print(f'{len(cas)} cas indexés')


if __name__ == '__main__':
    main()
