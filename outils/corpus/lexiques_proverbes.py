#!/usr/bin/env python3
"""Lexiques et proverbes d'abord : pour un passage litigieux, interroge les lexicographes et les
parémiographes du corpus local sur chaque mot du vers, de la leçon de R et des variantes.

Consigne de l'auteur (20 nov. 2026) : « sur tous les passages litigieux, chercher d'abord chez
Hésychius (et autres lexiques) et chez les proverbes ». Exemple : v. 489, κυνδ᾽ R^a.c., où la
glose d'Hésychius (κυνδός, voisine de κυνδάλη) et le proverbe du jeu des chevilles (ἥλῳ τὸν ἧλον,
chez Cicéron clavo clavum) ont orienté l'instruction (ravennas/cas/f168r.md).

Sources interrogées (index .sources/corpus/index.sqlite) :
  lexiques    : Hésychius (Latte–Hansen–Cunningham, gloses et apparats ; Schmidt), Souda (Adler,
                Bekker, First1K), Photius (Naber, Porson, Theodoridis), Synagoge, Etymologicum
                Magnum, Zonaras, Pollux (Bethe, Dindorf), Harpocration, Ammonius, Hérodien ;
  proverbes   : Zénobius, Diogénien, Grégoire de Chypre, Appendix proverbiorum, CPG I–II,
                Gaisford, Miller (Zénobius de l'Athos), Tosi (formes grecques et latines),
                Bauck (proverbes chez Aristophane).
Mots cherchés : ceux du texte imprimé (edition/folios/fXXX/texte.tex), de la transcription de R
et des leçons du répertoire critique pour ce vers, de 4 lettres ou plus, hors mots-outils ; chaque
mot sous sa forme et, s'il est long, par son début (κυνδ* trouve κυνδάλη, κυνδός).

L'index sert à TROUVER : toute référence se vérifie sur l'édition (lien d'image fourni par
chercher.py). Les sorties contiennent des extraits d'éditions sous droits : elles vont dans
.travail/lexiques_proverbes/ (non versionné).

Usage : python3 outils/corpus/lexiques_proverbes.py 489 [490 …]      (un ou plusieurs vers)
        python3 outils/corpus/lexiques_proverbes.py --folio f168r      (tous les vers d'une page)
        python3 outils/corpus/lexiques_proverbes.py --folio f168r --litigieux   (vers discutés seulement)
        toute la pièce, en parallèle :
        python3 -c "import json;[print(f['folio']) for f in json.load(open('edition/folios/folios.json'))]" \
          | xargs -P 8 -I{} python3 outils/corpus/lexiques_proverbes.py --folio {} --litigieux
        python3 outils/corpus/lexiques_proverbes.py 489 --mots κυνδ κύνδαλος   (mots ajoutés)
"""
import argparse, json, os, re, sqlite3, sys, unicodedata
from collections import defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'corpus'))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'transcription'))
import chercher  # noqa: E402

SORTIE = os.path.join(RACINE, '.travail', 'lexiques_proverbes')

GROUPES = [  # (groupe, motif sur l'abréviation de l'auteur)
    ('Hésychius', r'^Hsch'),
    ('Souda', r'^(Sud|Suda)'),
    ('Photius', r'^Phot'),
    ('Synagoge', r'^Synag'),
    ('Etymologica', r'^(EM|Et\.)'),
    ('Pollux', r'^Poll'),
    ('Zonaras', r'^Zonar'),
    ('Harpocration, Ammonius, Hérodien', r'^(Harp|Ammon|Hdn)'),
    ('Proverbes', r'^(Zen\.|Diogenian|Greg\. Cypr|App\. Prov|CPG|Gaisford|Miller|Tosi|Bauck)'),
]
MOTS_OUTILS = set('''και δε γαρ αλλα αλλ ουκ ουχ ουδε ουτε μητε μηδε τον την του της των τοις ταις τους τας
οτι ωσπερ ωστε επει επειδη οταν οπως ινα εγω εμοι εμε μου συ σοι σε σου ημεις ημιν υμεις υμιν αυτος αυτον
αυτην αυτου αυτης αυτω αυτη αυτων ουτος αυτη τουτο ταυτα τουτον ταυτην τουτου ταυτης εκεινος οστις
νυν δη μεν ουν γε περ τοι αρα ειναι εστι εστιν εισι εισιν ειμι ησαν ποτε πως που τις τινα τινος
ταυτ τουτ ουδεν μηδεν παντα παντες πασα παντων απαντα απασα εαν ουδ μηδ
παρα προς απο εκ εξ εις εσ εν κατα μετα περι υπο υπερ δια επι αντι ανα συν ξυν αμφι προ ωσ ειτα επειτα
αλλ ουτω ουτωσ ουτοσι αυτη αυτο αυτα εμου εμοι σοι ημων υμων ειπε ειπειν λεγει λεγω οιδα οπωσ
τουτω ταυτησ εκεινο εκεινη μαλλον μαλιστα πολυ πολλα σφοδρα ετι ηδη αει'''.split())


def plier(t):
    t = unicodedata.normalize('NFD', (t or '').lower())
    return ''.join(c for c in t if 'α' <= c <= 'ω').replace('ς', 'σ')


def mots_grecs(texte):
    texte = re.sub(r'\\[a-zA-Z@]+\*?(\[[^\]]*\])?', ' ', texte or '')
    return [m for m in re.findall(r'[\u0370-\u03ff\u1f00-\u1fff\u0300-\u036f᾽᾿\']+', texte)]


def texte_du_vers(v):
    """Grec imprimé du vers (rangées n=v et leurs suites) d'après edition/folios/*/texte.tex."""
    folios = json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json')))
    n = int(re.match(r'\d+', str(v)).group())
    for f in folios:
        if f['v0'] <= n <= f['v1']:
            out, dedans = [], False
            for l in open(os.path.join(RACINE, 'edition', 'folios', f['folio'], 'texte.tex'), encoding='utf-8'):
                m = re.match(r'\\vers\[([^\]]*)\]', l)
                if not m:
                    continue
                num = re.search(r'(?:^|,)\s*n=([^,\]]+)', m.group(1))
                if num:
                    dedans = num.group(1).strip() == str(n)
                if dedans:
                    args = chercher_args(l, m.end())
                    if len(args) >= 3:
                        out.append(args[2])
            return f['folio'], ' '.join(out)
    return '', ''


def chercher_args(l, i):
    a = []
    while i < len(l) and l[i] == '{':
        d, j = 0, i
        while j < len(l):
            if l[j] == '{':
                d += 1
            elif l[j] == '}':
                d -= 1
                if d == 0:
                    break
            j += 1
        a.append(l[i + 1:j])
        i = j + 1
    return a


def lecons_du_vers(v):
    p = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique.json')
    if not os.path.exists(p):
        return []
    rep = json.load(open(p, encoding='utf-8'))
    out = []
    for cle, items in rep.items():
        if re.match(r'\d+', cle) and int(re.match(r'\d+', cle).group()) == int(v):
            for it in items:
                out.append(it.get('lecon') or '')
                out += it.get('lemmes') or []
    return out


def lecture_de_R(folio, v):
    try:
        from diploxml import lire
    except Exception:
        return ''
    for p in (f'ravennas/transcription/{folio}.xml', f'ravennas/transcription/brouillons/{folio}_A.xml'):
        p = os.path.join(RACINE, p)
        if os.path.exists(p):
            try:
                r = lire(p)
            except Exception:
                continue
            txt = []
            for l in r.iter('l'):
                if str(v) in [x.strip() for x in (l.get('v') or '').split(',')]:
                    # R écrit les mots soudés : on ne garde que les leçons sous correction (R^a.c.)
                    for d in list(l.iter('del')) + list(l.iter('ras')):
                        txt.append(''.join(d.itertext()))
            if txt:
                return ' '.join(txt)
    return ''


def requetes_pour(mot):
    p = plier(mot)
    if len(p) < 4 or p in MOTS_OUTILS:
        return []
    q = [p]
    if len(p) >= 6:
        q.append(p[:len(p) - 2] + '*')
    elif re.search(r"[᾽'’ʼ]$", mot):          # forme élidée (κυνδ᾽) : par son début
        q.append(p + '*')
    return q


def interroger(con, requete, n=400):
    a = argparse.Namespace(requete=requete, exact=False, strict=True, lemme=False, sans_variantes=False,
                           auteur=None, oeuvre=None, collection=None, sans_ocr=False, toutes_editions=True,
                           sans_chevauchement=True, contexte=0, max=n, complet=False, json=True)
    try:
        res, termes, _, _ = chercher.chercher(con, a)
    except SystemExit:
        return [], []
    return res, termes


def groupe_de(o):
    ab = o.get('abr_auteur') or ''
    for g, motif in GROUPES:
        if re.search(motif, ab):
            return g
    return None


_DICO = None


def images_poetiques(mot):
    """Pages du Dictionnaire des images du poétique dans l'Antiquité (ThesmoBiblio) où se lit le mot."""
    global _DICO
    if _DICO is None:
        p = os.path.join(RACINE, '.sources', 'drive', 'ThesmoBiblio', 'texte',
                         '0Complet_Dictionnaire_images_poetique_dans_l_Antiquite_complet.txt')
        _DICO = []
        if os.path.exists(p):
            for i, page in enumerate(open(p, encoding='utf-8', errors='replace').read().split('\f')):
                _DICO.append((i + 1, page, plier(page)))
    cle = plier(mot.rstrip('*'))
    if len(cle) < 4 or cle in MOTS_OUTILS:
        return []
    cle = cle[:max(4, len(cle) - 2)] if len(cle) >= 6 else cle
    out = []
    for n, page, pl in _DICO:
        if cle in pl:
            # extrait : premier mot grec de la page dont le pliage commence par la clé
            ext = ''
            for m in re.finditer(r'[\u0370-\u03ff\u1f00-\u1fff\u0300-\u036f]+', page):
                if plier(m.group()).startswith(cle):
                    ext = re.sub(r'\s+', ' ', page[max(0, m.start() - 120):m.end() + 160])
                    break
            out.append((f'p. PDF {n}', ext or re.sub(r'\s+', ' ', page[:200])))
    return out


def dossier(con, v, mots_en_plus=(), par_groupe=6):
    folio, gr = texte_du_vers(v)
    lecR = lecture_de_R(folio, v)
    lecons = lecons_du_vers(v)
    mots = []
    for source in [gr, lecR] + lecons + list(mots_en_plus):
        for m in mots_grecs(source) if not re.fullmatch(r'[\u0370-\u03ff\u1f00-\u1fff*]+', source or '') else [source]:
            if plier(m) and plier(m) not in [plier(x) for x in mots]:
                mots.append(m)
    lignes = [f'## v. {v} ({folio})', '', f'Texte imprimé : {gr}', f'R (transcription) : {lecR or "—"}', '']
    vus = set()
    for mot in mots:
        trouvailles = defaultdict(list)
        for q in requetes_pour(mot.rstrip('*')) + ([plier(mot.rstrip('*')) + '*'] if mot.endswith('*') else []):
            res, termes = interroger(con, q)
            for r in res:
                g = groupe_de(r['o'])
                if not g:
                    continue
                cle = (r['o']['id'], r['p']['ordre'])
                if cle in vus:
                    continue
                vus.add(cle)
                ref = chercher.reference(r['o'], r['p'])
                txt = re.sub(r'\s+', ' ', r['p']['texte'])
                tete = plier(re.split(r'[·:]', re.sub(r'^\s*\d+\s*', '', txt), maxsplit=1)[0])[:40]
                lemme = bool(tete) and tete.startswith(plier(mot.rstrip('*'))[:max(4, len(plier(mot.rstrip('*'))) - 2)])
                pos = chercher.positions(txt, termes)
                ext = chercher.extrait(txt, pos, 160) if pos else txt[:200]
                ext = ext[0] if isinstance(ext, tuple) else ext
                trouvailles[g].append((not lemme, ref.strip(), ext))
        dico = images_poetiques(mot)
        if not trouvailles and not dico:
            continue
        total = sum(len(x) for x in trouvailles.values())
        commun = total > 150          # mot trop fréquent : ne garder que les gloses dont il est le lemme
        lignes.append(f'### {mot}' + (f' (mot fréquent : {total} passages ; lemmes seulement)' if commun else ''))
        for g, _ in GROUPES:
            lst = sorted(trouvailles.get(g, []))
            if commun:
                lst = [x for x in lst if not x[0]]
            if lst:
                nl = sum(1 for x in lst if not x[0])
                lignes.append(f'- **{g}** ({len(lst)}{f", dont {nl} comme lemme" if nl else ""}) :')
                for _, ref, ext in lst[:par_groupe]:
                    lignes.append(f'  - {ref} — {ext}')
                if len(lst) > par_groupe:
                    lignes.append(f'  - … {len(lst) - par_groupe} autres')
        if dico:
            lignes.append(f'- **Dictionnaire des images du poétique** ({len(dico)}) :')
            for ref, ext in dico[:par_groupe]:
                lignes.append(f'  - {ref} — {ext}')
        lignes.append('')
    return folio, '\n'.join(lignes) + '\n'


def vers_litigieux():
    """Vers où le texte est discuté : conjecture, suppression, transposition, lacune ou ponctuation au
    répertoire ; correction de R (R^a.c., R^p.c., R², « a pr. m. ») ; crux († dans texte.tex)."""
    out = set()
    p = os.path.join(RACINE, 'edition', 'donnees', 'repertoire_critique.json')
    for cle, items in json.load(open(p, encoding='utf-8')).items():
        m = re.match(r'\d+', cle)
        if not m:
            continue
        for it in items:
            if set(it.get('types') or []) & {'conjecture', 'deletion', 'transposition', 'lacune'} \
               or any(re.match(r'R\s*(\^|²|\()', t) for t in it.get('temoins') or []):
                out.add(int(m.group()))
    for f in json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json'))):
        for l in open(os.path.join(RACINE, 'edition', 'folios', f['folio'], 'texte.tex'), encoding='utf-8'):
            m = re.match(r'\\vers\[[^\]]*n=(\d+)', l)
            if m and '†' in l:
                out.add(int(m.group(1)))
    return sorted(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('vers', nargs='*')
    ap.add_argument('--folio')
    ap.add_argument('--mots', nargs='*', default=[], help='mots ou débuts de mots ajoutés (κυνδ*)')
    ap.add_argument('--par-groupe', type=int, default=6)
    ap.add_argument('--litigieux', action='store_true', help='avec --folio : seulement les vers litigieux')
    a = ap.parse_args()
    vers = list(a.vers)
    if a.folio:
        f = next(x for x in json.load(open(os.path.join(RACINE, 'edition', 'folios', 'folios.json'))) if x['folio'] == a.folio)
        lit = set(vers_litigieux()) if a.litigieux else None
        vers += [str(n) for n in range(f['v0'], f['v1'] + 1) if lit is None or n in lit]
    if not vers:
        ap.error('donner des vers ou --folio')
    con = sqlite3.connect(str(chercher.BASE))
    os.makedirs(SORTIE, exist_ok=True)
    par_folio = defaultdict(list)
    for v in vers:
        folio, md = dossier(con, v, a.mots, a.par_groupe)
        par_folio[folio].append(md)
        if len(vers) == 1:
            print(md)
    for folio, mds in par_folio.items():
        nom = f'{folio}.md' if a.folio else f"v{'_'.join(vers[:3])}{'…' if len(vers) > 3 else ''}.md"
        p = os.path.join(SORTIE, nom)
        open(p, 'w', encoding='utf-8').write(f'# Lexiques et proverbes — {folio}\n\n*Produit par outils/corpus/lexiques_proverbes.py ; index pour trouver, références à vérifier sur les éditions.*\n\n' + '\n'.join(mds))
        print('→', os.path.relpath(p, RACINE))


if __name__ == '__main__':
    main()
