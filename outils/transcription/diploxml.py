#!/usr/bin/env python3
"""Bibliothèque DiploXML : lecture, validation et conversion en LaTeX de la
transcription diplomatique du Ravennas (voir ravennas/FORMAT_TRANSCRIPTION.md)."""
import re, unicodedata
from lxml import etree

MAINS = {'R1', 'R1c', 'R2', 'R3', 'Rsch', 'Rrec', 'Rmod', 'R?'}
ELEMENTS_EN_LIGNE = {'nota', 'parag', 'add', 'del', 'subst', 'ras', 'unclear', 'gap',
                     'abbr', 'gl', 'hi', 'sp', 'signe', 'w', 'lb', 'corr'}
# corr : couche de correction de l'édition, posée après la vérification. Le contenu reste la
# leçon de R (collation, apparat) ; le livre imprime l'attribut lire. Voir FORMAT_TRANSCRIPTION.md.
TYPES_CORR = {'accent', 'coupe', 'faute'}
# repasse = main de la campagne qui a repassé le tracé (R2 repassé en 1516 : repasse="Rrec") ;
# instrument = matière autre que l'encre (mine des repères de 1516, crayon moderne).
MAINIFS = {'main', 'repasse', 'instrument'}
INSTRUMENTS = {'mine', 'crayon'}
ATTRS = {
    'page': {'folio', 'image', 'vers'},
    'l': {'n', 'v', 'zone', 'retrait'} | MAINIFS,
    'sch': {'n', 'ancre', 'place', 'lemme'} | MAINIFS,
    'note': {'ligne', 'sch'},
    'nota': set(MAINIFS), 'parag': set(MAINIFS),
    'add': {'place'} | MAINIFS, 'del': {'type'} | MAINIFS, 'subst': set(MAINIFS),
    'ras': set(MAINIFS), 'unclear': {'cert'}, 'gap': {'n', 'unite', 'raison'},
    'abbr': {'dev', 'signe'}, 'gl': {'sur'} | MAINIFS, 'hi': {'rend'}, 'sp': {'n'},
    'signe': {'type'} | MAINIFS, 'w': set(), 'lb': {'coupe'}, 'corr': {'lire', 'type'},
}
PLACES_SCH = {'mg-g': 'mg. g.', 'mg-d': 'mg. d.', 'mg-sup': 'mg. sup.', 'mg-inf': 'mg. inf.', 'interl': 'interl.',
              'col': 'dans la col.'}


def lire(chemin):
    return etree.parse(chemin, etree.XMLParser(remove_blank_text=False)).getroot()


def valider(racine):
    """Renvoie la liste des problèmes (chaînes) ; vide si le fichier est conforme."""
    pb = []
    if racine.tag != 'page':
        pb.append('racine <page> attendue')
    for el in racine.iter():
        if not isinstance(el.tag, str):
            continue
        if el.tag in ATTRS:
            for a in el.attrib:
                if a not in ATTRS[el.tag]:
                    pb.append(f'ligne {el.sourceline} : attribut inconnu {a}= sur <{el.tag}>')
        elif el.tag not in {'lignes', 'scholies', 'notes'}:
            pb.append(f'ligne {el.sourceline} : élément inconnu <{el.tag}>')
        m = el.get('main')
        if m and m not in MAINS:
            pb.append(f'ligne {el.sourceline} : main inconnue {m}')
        m = el.get('repasse')
        if m and m not in MAINS:
            pb.append(f'ligne {el.sourceline} : main inconnue {m} (repasse=)')
        m = el.get('instrument')
        if m and m not in INSTRUMENTS:
            pb.append(f'ligne {el.sourceline} : instrument inconnu {m}')
        if el.tag == 'corr':
            if not el.get('lire'):
                pb.append(f'ligne {el.sourceline} : <corr> sans lire=')
            if el.get('type') not in TYPES_CORR:
                pb.append(f'ligne {el.sourceline} : <corr> de type inconnu {el.get("type")}')
            if len(el):
                pb.append(f'ligne {el.sourceline} : <corr> ne s\'applique qu\'à du texte nu (une intervention reste visible)')
    ns = []
    for l in racine.iter('l'):
        try:
            ns.append(int(l.get('n')))
        except (TypeError, ValueError):
            pb.append(f'ligne {l.sourceline} : <l> sans n numérique')
    if ns and ns != list(range(1, len(ns) + 1)):
        pb.append('numérotation des <l> non continue à partir de 1')
    for s in racine.iter('sch'):
        a = s.get('ancre')
        if not a or not a.isdigit() or int(a) not in ns:
            pb.append(f'ligne {s.sourceline} : <sch> avec ancre invalide ({a})')
        if s.get('place') and s.get('place') not in PLACES_SCH:
            pb.append(f'ligne {s.sourceline} : place inconnue {s.get("place")}')
    return pb


def avertir(racine):
    """Écarts au guide (ravennas/GUIDE_TRANSCRIPTION.md, § 2) qui n'empêchent pas la compilation :
    à examiner, jamais à corriger sans retour à l'image."""
    av = []
    for el in racine.iter('l'):
        t = ''.join(el.itertext())
        for c in sorted(set(c for c in t if c in 'ᾳῃῳᾴῄῴᾲῂῲᾷῇῷᾀᾐᾠ')):
            av.append(f'l. {el.get("n")} : iota souscrit « {c} » : R ne souscrit jamais (écrire l\'ι sur la ligne, ou rien)')
        if 'ς' in t:
            av.append(f'l. {el.get("n")} : ς : T n\'a qu\'un σ (écrire σ, même en finale)')
        for c in sorted(set(c for c in t if c in '\'’ʼ')):
            av.append(f'l. {el.get("n")} : apostrophe « {c} » : employer ᾽ (U+1FBD)')
    return av


def sigma_final(t):
    """Le copiste n'a qu'une forme de sigma ; le livre imprime ς en fin de mot (allographe, non leçon)."""
    return re.sub(r'(?<=\w)σ(?=[\s·,.;:!?—–\-)\]⟧]|$)', 'ς', t)


def esc(t):
    t = re.sub(r'(?<=\w)σ(?=[\s·,.;:!?—–\-)\]⟧])', 'ς', t)
    t = t.replace('\\', r'\textbackslash{}')
    for c in '&%$#_{}':
        t = t.replace(c, '\\' + c)
    return t.replace('~', r'\textasciitilde{}').replace('^', r'\textasciicircum{}')


def souscrire(t):
    """Point souscrit sous chaque lettre (lectures douteuses)."""
    out = []
    for ch in unicodedata.normalize('NFC', t):
        out.append(ch)
        if unicodedata.category(ch).startswith('L'):
            out.append('̣')
    return unicodedata.normalize('NFC', ''.join(out))


def interieur(el):
    """Contenu d'un élément (texte + enfants), converti en LaTeX."""
    s = esc(el.text or '')
    for c in el:
        s += convertir(c) + esc(c.tail or '')
    return s


def convertir(el):
    """Élément → LaTeX ; repasse et instrument ajoutent le pointillé orange de la légende."""
    s = convertir_nu(el)
    if el.get('instrument') == 'mine':
        return r'\Dmine{%s}' % s
    if el.get('repasse'):
        return r'\Drepasse{%s}' % s
    return s


def convertir_nu(el):
    tag, m = el.tag, el.get('main', '')
    if tag == 'nota':
        return r'\Dnota[%s]{%s}' % (m or 'R1', interieur(el))
    if tag == 'parag':
        return r'\Dparag'
    if tag == 'add':
        return r'\Dadd[%s]{%s}{%s}' % (m or 'R1', el.get('place', 'dessus'), interieur(el))
    if tag == 'del':
        return r'\Ddel[%s]{%s}{%s}' % (m or 'R1', el.get('type', 'grattage'), interieur(el))
    if tag == 'subst':
        d = el.find('del'); a = el.find('add')
        return r'\Dsubst[%s]{%s}{%s}' % (m or (a.get('main') if a is not None else '') or 'R1',
                                         interieur(d) if d is not None else '',
                                         interieur(a) if a is not None else '')
    if tag == 'ras':
        return r'\Dras[%s]{%s}' % (m or 'R1', interieur(el))
    if tag == 'unclear':   # le point souscrit ne touche que le texte, jamais les macros des enfants
        s = esc(souscrire(el.text or ''))
        for c in el:
            s += convertir(c) + esc(souscrire(c.tail or ''))
        return s
    if tag == 'gap':
        return r'\Dgap{%s}' % el.get('n', '1')
    if tag == 'abbr':   # le signe du manuscrit est imprimé ; le développement, en gris, l'explique
        return r'\Dabbr[%s]{%s}{%s}' % (esc(el.get('signe', '')), interieur(el), esc(el.get('dev', '')))
    if tag == 'corr':
        return esc(sigma_final(el.get('lire', '')))
    if tag == 'gl':
        return r'\Dgl[%s]{%s}{%s}' % (m or 'R1', esc(el.get('sur', '')), interieur(el))
    if tag == 'hi':
        if el.get('rend') == 'sus':   # lettre écrite au-dessus de la ligne par le scripteur (pas une correction)
            return r'\textsuperscript{%s}' % interieur(el)
        return r'\Dhi{%s}{%s}' % (el.get('rend', 'rouge'), interieur(el))
    if tag == 'lb':
        return '' if el.get('coupe') else ' '
    if tag == 'sp':
        return r'\Dsp{%s}' % el.get('n', '1')
    if tag == 'signe':
        if el.get('type') == 'repere':   # repères de la Juntine : données, non imprimées dans la ligne
            return ''
        return r'\Dsigne{%s}{%s}' % (el.get('type', 'autre'), interieur(el))
    if tag == 'w':
        return interieur(el)
    return interieur(el)


def ligne_vers_latex(l):
    """Une ligne <l> → \\ligne[...]{sigles}{texte}. Les <nota>/<parag> initiaux vont
    dans la colonne des sigles."""
    sig = []
    texte = esc((l.text or '').lstrip()) if (l.text or '').strip() else ''
    enfants = list(l)
    debut = not (l.text or '').strip()
    corps = texte
    for c in enfants:
        marque = c.tag in ('nota', 'parag') or (c.tag in ('del', 'unclear') and len(c) == 1
                                                and c[0].tag == 'parag' and not (c.text or '').strip())
        if debut and marque and not corps.strip():
            sig.append(convertir(c))
            corps += esc((c.tail or '').lstrip()) if not corps else esc(c.tail or '')
            continue
        debut = False
        corps += convertir(c) + esc(c.tail or '')
    opts = []
    if l.get('v'):
        opts.append('v={%s}' % l.get('v'))   # accolades : « 6,7 » contient une virgule
    opts.append('n=' + l.get('n'))
    if l.get('retrait'):
        opts.append('retrait=%sem' % (float(l.get('retrait')) * 0.5))
    z = l.get('zone', 'texte')
    if z not in ('texte',):
        corps = r'\Dzone{%s}{%s}' % (z, corps)
    if l.get('main') and l.get('main') != 'R1':
        corps = r'\Dmain{%s}{%s}' % (l.get('main'), corps)
    return r'\ligne[%s]{%s}{%s}' % (', '.join(opts), ''.join(sig), sigma_final(corps.strip()))


def sch_vers_latex(s, folio=''):
    corps = sigma_final(interieur(s).strip())   # l'attribut lemme est une métadonnée (index), non imprimée
    if s.get('main') and s.get('main') not in ('R1',):
        corps = r'\Dmain{%s}{%s}' % (s.get('main'), corps)
    # sans indication, la scholie est dans la marge extérieure (gauche au verso, droite au recto)
    place = s.get('place', 'mg-g')
    if place == ('mg-g' if str(folio).endswith('v') else 'mg-d'):
        place = ''
    return r'\sch[%s]{%s}{%s}' % (PLACES_SCH.get(place, ''), s.get('ancre'), corps)


def page_vers_latex(racine):
    out = ['%% Généré automatiquement depuis ravennas/transcription/f' + str(racine.get('folio')) + '.xml — ne pas modifier à la main.']
    for l in racine.iter('l'):
        out.append(ligne_vers_latex(l))
    for s in racine.iter('sch'):
        out.append(sch_vers_latex(s, racine.get('folio')))
    return '\n'.join(out) + '\n'


def texte_brut(el, garder_corrections='pc'):
    """Texte d'une ligne pour la collation : 'pc' = état final (après corrections),
    'ac' = état premier (avant corrections)."""
    def rec(e):
        tag = e.tag
        if tag in ('nota', 'parag', 'gl', 'signe'):
            return e.tail or ''
        if tag == 'add':
            s = '' if garder_corrections == 'ac' else (e.text or '') + ''.join(rec(c) for c in e)
            return s + (e.tail or '')
        if tag == 'del':
            s = ((e.text or '') + ''.join(rec(c) for c in e)) if garder_corrections == 'ac' else ''
            return s + (e.tail or '')
        if tag == 'gap':
            return '…' + (e.tail or '')
        if tag == 'abbr':
            return (e.text or '') + ''.join(rec(c) for c in e) + e.get('dev', '') + (e.tail or '')
        if tag == 'lb':
            return ('' if e.get('coupe') else ' ') + (e.tail or '')
        if tag == 'sp':
            return ' ' + (e.tail or '')
        return (e.text or '') + ''.join(rec(c) for c in e) + (e.tail or '')
    s = (el.text or '') + ''.join(rec(c) for c in el)
    return re.sub(r'\s+', ' ', s).strip()
