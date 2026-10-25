#!/usr/bin/env python3
"""Première conversion des travaux antérieurs de l'auteur (extraction
edition/donnees/travaux_anterieurs/thesmo.json) vers les fichiers de la nouvelle édition :
edition/folios/fXXX/texte.tex (rangées grec/français) et commentaire.tex.

Ce n'est qu'un point de départ : le texte grec sera revu sur la transcription de R et
l'apparat ; le commentaire sera réparti entre commentaire critique et commentaire de la
pièce. Ne pas relancer ce script après révision manuelle des fichiers (il les écrase,
sauf --seulement-absents).

Usage : python3 outils/extraction/vers_edition.py [--seulement-absents]
"""
import json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(RACINE, 'edition', 'donnees', 'travaux_anterieurs', 'thesmo.json')
FOLIOS = os.path.join(RACINE, 'edition', 'folios', 'folios.json')

ABR = {
    'Μνησίλοχος': 'ΜΝ.', 'Εὐριπίδης': 'ΕΥ.', 'Χορός': 'ΧΟ.', 'Μίκα': 'ΜΙ.', 'Κορυφαῖος': 'ΚΟ.',
    'Ἀγάθων': 'ΑΓ.', 'Τοξότης': 'ΤΟ.', 'Κλεισθένης': 'ΚΛ.', 'Κρίτυλλα': 'ΚΡ.', 'Θεράπων': 'ΘΕ.',
    'Στεφανόπωλις': 'ΣΤ.', 'Κορ.-Ἱέρεια': 'ΚΟ.', 'Πρύτανις': 'ΠΡ.', 'Κορυφ. β': 'ΚΟ. β´',
    'Ἠχώ': 'ΗΧ.', 'Κῆρυξ': 'ΚΗ.', 'Χορόςστροφή': 'ΧΟ.', 'Χορόςἀντιστρ': 'ΧΟ.', 'πνῖγος': 'ΧΟ.',
}
FR = {'Serviteur d\'Agathon': 'Serviteur', 'Archer Scythe': 'Archer'}
# renfoncement (em) et étiquette de mètre selon la macro de l'auteur
TYPES = {
    'trimIamb': (0, 'ia³'), 'trimIambCat': (0, 'ia³'), 'tetramIamb': (0, 'ia⁴'),
    'tetramIambCat': (0, 'ia⁴ cat.'), 'tetramTroch': (0, 'tr⁴'), 'tetramAnap': (0, 'an⁴'),
    'anap': (3, 'an.'), 'dimAnap': (3, 'an.'), 'chantChoeur': (2, 'lyr.'),
    'chantAgath': (4, 'lyr.'), 'diDoch': (2.5, 'do.'), 'paratragiques': (2, 'lyr.'),
    'prose': (0.5, 'prose'), 'chantChoeurFr': (2, 'lyr.'),
}


def nettoie_fr(t):
    t = re.sub(r'\\fin\b\s*', ' ', t)
    t = re.sub(r'\\espace\{[^}]*\}', '', t)
    t = re.sub(r'\\ligne\{\d+\}', '', t)
    t = re.sub(r'\\decalage\{[^}]*\}', '', t)
    t = t.replace('\\passeLigne', '')
    return re.sub(r'\s+', ' ', t).strip()


def nettoie_gr(t):
    t = re.sub(r'\\ligne\{\d+\}', '', t)
    t = re.sub(r'\\decalage\{(?:[^{}]|\{[^{}]*\})*\}', '', t)
    t = re.sub(r'\\espace\{[^}]*\}', '', t)
    t = re.sub(r'\\typeVers\{[^}]*\}', '', t)
    t = re.sub(r'\\(trimIamb|tetram\w+|anap|dimAnap|chant\w+|diDoch|paratragiques|prose)\b', '', t)
    t = t.replace('\\passeLigne', '').replace('\\lednopb', '')
    t = deballer(t, '\\Automatique')
    return re.sub(r'\s+', ' ', t).strip()


def deballer(t, macro):
    """Remplace macro{X} par X (accolades équilibrées)."""
    while True:
        i = t.find(macro + '{')
        if i < 0:
            return t
        j = i + len(macro)
        d = 0
        for k in range(j, len(t)):
            if t[k] == '{' and t[k - 1] != '\\':
                d += 1
            elif t[k] == '}' and t[k - 1] != '\\':
                d -= 1
                if d == 0:
                    t = t[:i] + t[j + 1:k] + t[k + 1:]
                    break
        else:
            return t


def premier(plage):
    m = re.search(r'\d+', plage or '')
    return int(m.group()) if m else None


def note_latex(n):
    return n.get('latex', '').strip()


def commentaire_latex(c):
    texte = c.get('latex', '')
    notes = {str(n.get('numero')): note_latex(n) for n in c.get('notes', [])}
    utilisees = set()

    def rempl(m):
        k = m.group(1)
        if k in notes and k not in utilisees:
            utilisees.add(k)
            return r'\nc{%s}' % notes[k]
        return ''
    texte = re.sub(r'\\marqueur\{(\d+)\}', rempl, texte)
    reste = [notes[k] for k in notes if k not in utilisees and notes[k]]
    for r in reste:
        texte += r' \nc{%s}' % r
    texte = re.sub(r'\\begin\{alignat\*\}(?!\{)', r'\\begin{alignat*}{4}', texte)  # argument manquant dans la source
    lemme = (c.get('lemme_latex') or '').strip()
    plage = (c.get('plage') or '').replace('-', '–')
    return r'\comm{%s}{%s}{%s}' % (plage, lemme, texte.strip())


def main():
    seulement_absents = '--seulement-absents' in sys.argv
    d = json.load(open(DATA, encoding='utf-8'))
    folios = json.load(open(FOLIOS))

    def folio_de(v):
        for f in folios:
            if f['v0'] <= v <= f['v1']:
                return f['folio']
        return folios[-1]['folio'] if v > folios[-1]['v1'] else folios[0]['folio']

    rangs = {f['folio']: [] for f in folios}
    comms = {f['folio']: [] for f in folios}
    dernier_spk = {'gr': None}
    dernier_type = None
    for g in d['groupes']:
        fr_par = {}
        for l in g['francais']['lignes']:
            fr_par.setdefault((l['vers'], l.get('partie', '')), []).append(l)
        en_tete = [h['texte'] for h in g.get('en_tetes', []) if h.get('cote') == 'G']
        for h in en_tete:
            m = re.match(r'(\S+)\s+[—-]+\s+(.*?)\s+vv?\.', h)
            gr, frt = (m.group(1), m.group(2)) if m else (h, h)
            v0 = g['vers'][0] if g.get('vers') else 1
            rangs[folio_de(v0)].append(r'\rubrique{%s}{%s}' % (gr, frt))
        lignes = list(g['grec']['lignes'])
        # interversion de vers dans les travaux antérieurs (vv. 3–4) : on rétablit l'ordre
        # de R (numérotation usuelle), qui est aussi celui de la traduction de l'auteur
        def cle_hg(l):
            m = re.match(r'\d+', str(l.get('vers_HG') or l.get('vers') or 0))
            return int(m.group()) if m else 0
        reordonne = False
        if all(not l.get('partie') for l in lignes) and [cle_hg(l) for l in lignes] != sorted(cle_hg(l) for l in lignes):
            lignes.sort(key=cle_hg)
            reordonne = True
            # la traduction suit déjà l'ordre de R : appariement par position
            fr_seq = list(g['francais']['lignes'])
        for idx, l in enumerate(lignes):
            v = l.get('vers')
            if v is None:
                continue
            vh = l.get('vers_HG') or str(v)
            try:
                vnum = int(re.match(r'\d+', str(vh)).group())
            except Exception:
                vnum = v
            fol = folio_de(vnum)
            partie = l.get('partie', '') or ''
            fl = ([fr_seq[idx]] if reordonne and idx < len(fr_seq) else None) or fr_par.get((v, partie)) or fr_par.get((v, '')) or []
            frt = ' '.join(nettoie_fr(x.get('latex', x.get('texte', ''))) for x in fl)
            frspk = fl[0]['personnage'] if fl else ''
            frspk = FR.get(frspk, frspk)
            spk = l.get('personnage') or ''
            montrer = spk != dernier_spk['gr'] or partie in ('b', 'c', 'd')
            dernier_spk['gr'] = spk
            typ = l.get('type') or 'trimIamb'
            ind, lab = TYPES.get(typ, (0, ''))
            opts = []
            if partie in ('', 'a'):
                opts.append('n=%d' % vnum)
            if partie in ('b', 'c', 'd'):
                opts.append('suite')
            elif ind:
                opts.append('indent=%sem' % ind)
                opts.append('findent=%sem' % (ind * 0.6))
            if typ != dernier_type and lab and lab != 'ia³':
                opts.append('metre={%s}' % lab)
            dernier_type = typ
            rangs[fol].append(r'\vers[%s]{%s}{%s}{%s}{%s}' % (
                ', '.join(opts), ABR.get(spk, spk[:2].upper() + '.') if montrer and spk else '',
                frspk if montrer else '', nettoie_gr(l.get('latex', l.get('texte', ''))), frt))
        for c in g['grec'].get('commentaires', []):
            v = premier(c.get('plage')) or (g['vers'][0] if g.get('vers') else 1)
            comms[folio_de(v)].append(commentaire_latex(c))
    n_t = n_c = 0
    for f in folios:
        rep = os.path.join(RACINE, 'edition', 'folios', f['folio'])
        os.makedirs(rep, exist_ok=True)
        for nom, contenu in (('texte.tex', rangs[f['folio']]), ('commentaire.tex', comms[f['folio']])):
            p = os.path.join(rep, nom)
            if seulement_absents and os.path.exists(p):
                continue
            with open(p, 'w', encoding='utf-8') as out:
                out.write('%% %s — %s, vv. %d–%d (conversion initiale des travaux antérieurs)\n' % (nom, f['folio'], f['v0'], f['v1']))
                out.write('\n'.join(contenu) + '\n')
        n_t += len(rangs[f['folio']]); n_c += len(comms[f['folio']])
    print(f'{n_t} rangées, {n_c} commentaires répartis sur {len(folios)} folios')


if __name__ == '__main__':
    main()
