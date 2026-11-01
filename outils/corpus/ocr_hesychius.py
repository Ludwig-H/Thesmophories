#!/usr/bin/env python3
"""Hésychius de Latte–Hansen–Cunningham : texte des gloses (décodage des polices et OCR).

Les quatre fichiers présents sur le Drive de l'auteur couvrent tout le lexique : t. I (Α–Δ),
t. II (Ε–Ο : le fichier n'a que la page de titre du t. IIa, Ε–Ι, mais contient aussi Κ–Ο),
t. III (Π–Σ), t. IV (Τ–Ω). Ce sont des PDF d'éditeur entièrement vectoriels, sans image. Le grec y
est composé dans les polices Kleinlogel, dont les noms de glyphes sont brouillés : la
couche texte native est du charabia (« <$\\r2\\n… » pour ᾿Αβυδόθεν). Deux voies, menées de
front :

  1. OCR : rendu des pages à 400 dpi et Tesseract 5 (grc+lat), sur
     plusieurs processus, reprenable page par page (sous-commande « ocr ») ;
  2. décodage : table glyphe → caractère des polices Kleinlogel (outils/corpus/kleinlogel.tsv,
     établie sur les glyphes eux-mêmes et contrôlée par l'OCR), qui rend le texte exact
     de l'éditeur, accents et esprits compris (sous-commande « decoder »).

Les gloses sont ensuite découpées d'après la mise en page (numéro en gras en tête de
glose, signes de source dans la marge, deux apparats sous deux filets) et référencées
« Hsch. α 223 (Latte I, p. 13) » dans la numérotation de l'édition : celle de Latte pour
α–ο (inchangée dans la 2e éd. de Cunningham, t. I, Prolegomena § VII), celle de Schmidt pour
π–ω (conservée par Hansen et Cunningham, t. III, p. XXXI, n. 5 ; t. IV, p. XVI).

Sorties (non versionnées, l'édition étant sous droits) : .sources/corpus/hesychius/
  ocr/<tome>/p0001.tsv.gz      OCR Tesseract (mots, boîtes, confiance), une page par fichier
  texte/<tome>.jsonl.gz        texte décodé page par page : zones (corps, marges, apparats), texte brut
  gloses.jsonl.gz              une glose par ligne (lettre, numéro, tome, page, texte, apparats)
  anomalies.tsv                ruptures de la suite des numéros, notes sans glose
  qualite.json                 mesures de qualité (voir recherche/corpus_numeriques.md)
  controle_testimonia.tsv      références de recherche/testimonia.md confrontées à l'édition
  thesmophories_hors_testimonia.tsv  gloses que l'édition rapporte aux Thesm., absentes de testimonia.md

  python3 outils/corpus/ocr_hesychius.py ocr --processus 8      # reprenable
  python3 outils/corpus/ocr_hesychius.py decoder
  python3 outils/corpus/ocr_hesychius.py gloses
  python3 outils/corpus/ocr_hesychius.py qualite
  python3 outils/corpus/ocr_hesychius.py tester
  python3 outils/corpus/ocr_hesychius.py echantillon            # planches de contrôle visuel
  python3 outils/corpus/ocr_hesychius.py voir χ 576             # une glose et son image
puis outils/corpus/indexer.py (les gloses entrent dans la collection « drive »).
"""

import argparse
import concurrent.futures as cf
import gzip
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
DRIVE = RACINE / ".sources" / "drive" / "fichiers"
HSCH = DRIVE / "Grec" / "Lexiques" / "Hesychius"
SORTIE = RACINE / ".sources" / "corpus" / "hesychius"
sys.path.insert(0, str(ICI))
import kleinlogel  # noqa: E402

# Modèles « fast » du système : sur un échantillon de six pages, même taux de mots grecs
# reconnus que les modèles « best » (.travail/tessdata), pour un temps inférieur de 40 %.
TESSDATA = os.environ.get("TESSDATA_PREFIX") or "/usr/share/tesseract-ocr/5/tessdata"

# tome → (fichier, lettres, libellé de référence, édition)
VOLUMES = {
    "I": ("Latte_I_alpha-delta.pdf", "αβγδ", "Latte I",
          "Hesychii Alexandrini Lexicon, vol. I : Α–Δ, rec. K. Latte, 2e éd. I. C. Cunningham, "
          "Berlin-Boston, De Gruyter, 2018"),
    # Le fichier ne porte que la page de titre du t. IIa (Ε–Ι), mais contient aussi Κ–Ο
    # (pagination continue, κ commence p. 491) : tout le t. II de Cunningham (2020).
    "II": ("Hesychii Alexandrini Lexicon, Volumen II Iota-Omicron by Peter Allan Hansen, "
           "Ian C. Cunningham (z-lib.org) (1).pdf", "εζηθικλμνξο", "Latte II",
           "Hesychii Alexandrini Lexicon, vol. II : Ε–Ο, rec. K. Latte, 2e éd. I. C. Cunningham, "
           "Berlin-Boston, De Gruyter, 2020"),
    "III": ("Hansen_III_pi-sigma.pdf", "πρσ", "Hansen III",
            "Hesychii Alexandrini Lexicon, vol. III : Π–Σ, rec. P. A. Hansen, Berlin-New York, "
            "De Gruyter, 2005"),
    "IV": ("04 Latte Tau - Aumega .pdf", "τυφχψω", "Hansen–Cunningham IV",
           "Hesychii Alexandrini Lexicon, vol. IV : Τ–Ω, rec. P. A. Hansen et I. C. Cunningham, "
           "Berlin-New York, De Gruyter, 2009"),
}


# page imprimée = page du PDF − décalage (contrôlé sur les titres courants de toutes les pages)
DECALAGE = {"I": 38, "II": 12, "III": 34, "IV": 32}
# page du PDF où commencent les gloses (avant : pages liminaires)
PREMIERE_GLOSE = {"I": 41, "II": 13, "III": 37, "IV": 35}


def pdf_de(tome):
    return HSCH / VOLUMES[tome][0]


def ouvrir(tome):
    import pymupdf
    return pymupdf.open(str(pdf_de(tome)))


# ---------------------------------------------------------------------------
# 1. OCR (Tesseract, 400 dpi), reprenable page par page
# ---------------------------------------------------------------------------

def fichier_ocr(tome, i):
    return SORTIE / "ocr" / tome / f"p{i + 1:04d}.tsv.gz"


def ocr_page(args):
    """Rend la page i du tome à `dpi` (niveaux de gris) et l'océrise ; écrit le TSV de Tesseract."""
    tome, i, dpi, langues, psm = args
    sortie = fichier_ocr(tome, i)
    if sortie.exists():
        return tome, i, "déjà fait", 0.0
    t0 = time.time()
    import pymupdf
    doc = pymupdf.open(str(pdf_de(tome)))
    png = doc[i].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY).tobytes("png")
    doc.close()
    env = dict(os.environ, OMP_THREAD_LIMIT="1", TESSDATA_PREFIX=TESSDATA)
    r = subprocess.run(["tesseract", "stdin", "stdout", "-l", langues, "--psm", str(psm), "--dpi", str(dpi),
                        "-c", "tessedit_create_tsv=1", "-c", "tessedit_create_txt=0"],
                       input=png, capture_output=True, env=env, timeout=1800)
    if r.returncode != 0 or not r.stdout.startswith(b"level"):
        return tome, i, "erreur : " + r.stderr.decode("utf-8", "replace")[-300:], time.time() - t0
    sortie.parent.mkdir(parents=True, exist_ok=True)
    part = sortie.with_suffix(".part")
    with gzip.open(part, "wb") as f:
        f.write(r.stdout)
    part.rename(sortie)
    return tome, i, "ok", time.time() - t0


def ordre_echantillon_d_abord(n, pas=20):
    """Pages d'un tome : un échantillon régulier d'abord (contrôle précoce), puis le reste."""
    premiers = list(range(0, n, pas))
    vus = set(premiers)
    return premiers + [i for i in range(n) if i not in vus]


def cmd_ocr(a):
    import pymupdf
    taches = []
    for tome in a.tomes:
        n = len(pymupdf.open(str(pdf_de(tome))))
        pages = range(n) if not a.pages else [int(x) - 1 for x in a.pages.split(",")]
        ordre = ordre_echantillon_d_abord(n) if not a.pages else list(pages)
        taches += [(tome, i, a.dpi, a.langues, a.psm) for i in ordre if not fichier_ocr(tome, i).exists()]
    # alterner les tomes pour que l'échantillon de chacun soit fait tôt
    taches.sort(key=lambda t: (0 if t[1] % 20 == 0 else 1))
    print(f"{len(taches)} pages à océriser ({a.processus} processus, {a.dpi} dpi, {a.langues})", flush=True)
    t0, fait = time.time(), 0
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for tome, i, etat, duree in ex.map(ocr_page, taches, chunksize=1):
            fait += 1
            if etat != "ok":
                print(f"  {tome} p. {i + 1} : {etat}", flush=True)
            if fait % 25 == 0 or fait == len(taches):
                print(f"  {fait}/{len(taches)} pages ({time.time() - t0:.0f} s ; dernière {duree:.1f} s)", flush=True)
    print("OCR terminé", flush=True)


# ---------------------------------------------------------------------------
# 2. Décodage de la couche texte (polices Kleinlogel) et mise en page
# ---------------------------------------------------------------------------

# numéro de glose : « 223 », « 1943a », et numéros groupés « 710/11 », « 2481–2 », « 495–9 »
RE_NUM = re.compile(r"^(\d{1,5})([a-z]?)(?:([/–-])(\d{1,5})([a-z]?))?(?=[\s.,;:)\]]|$)")
RE_ENTETE = re.compile(r"([α-ω])\s*(\d+[a-z]?|[–-])?\s*[–-]?\s*(\d+[a-z]?)?")
RE_TITRE = re.compile(r"^\s*[Α-ΩϜ]\s*$")
RE_NUMS_SEULS = re.compile(r"^\d{1,5}[a-z]?(?:[\s.,;–-]+\d{1,5}[a-z]?)*[\s.,;–-]*$")


def fichier_texte(tome):
    return SORTIE / "texte" / f"{tome}.jsonl.gz"


def filets(page):
    """Ordonnées des filets (traits horizontaux courts) qui séparent le texte des apparats."""
    ys = []
    for g in page.get_drawings():
        for it in g["items"]:
            if it[0] == "l":
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.6 and 20 < abs(b.x - a.x) < 140:
                    ys.append(round((a.y + b.y) / 2, 1))
            elif it[0] == "re":
                r = it[1]
                if r.height < 1.2 and 20 < r.width < 140:
                    ys.append(round((r.y0 + r.y1) / 2, 1))
    out = []
    for y in sorted(ys):
        if not out or y - out[-1] > 2:
            out.append(y)
    return out


def ordonner(lignes):
    """Ordre de lecture : PyMuPDF morcelle souvent une ligne imprimée (numéro, corps du texte,
    demi-crochets, exposants, chacun avec son propre cadre) ; on regroupe les fragments en
    lignes visuelles d'après le centre vertical, puis on lit de gauche à droite. Les
    demi-crochets ⌊ ⌈ sont frappés deux fois : le doublon isolé est écarté."""
    ls = sorted(lignes, key=lambda l: (l["bbox"][1] + l["bbox"][3]) / 2)
    paquets = []
    for l in ls:
        c = (l["bbox"][1] + l["bbox"][3]) / 2
        taille = max((sp[2] for sp in l["spans"] if sp[0].strip()), default=10)
        if paquets and c - paquets[-1][0] < 0.42 * max(paquets[-1][1], taille):
            paquets[-1][2].append(l)
            if taille > paquets[-1][1]:  # centre de référence : le fragment du corps le plus grand
                paquets[-1][0], paquets[-1][1] = c, taille
        else:
            paquets.append([c, taille, [l]])
    out = []
    for _, _, groupe in paquets:
        groupe.sort(key=lambda l: l["bbox"][0])
        for l in groupe:
            t = l["texte"].strip()
            if len(t) == 1 and t in "⌊⌋⌈⌉" and any(
                    m is not l and m["bbox"][0] < l["bbox"][0] and m["bbox"][2] > l["bbox"][2] and t in m["texte"]
                    for m in groupe):
                continue
            out.append(l)
    for k, a in enumerate(out):      # signes de marge entre deux : on regarde un peu plus loin
        for b in out[k + 1:k + 4]:
            if kleinlogel.reporter_souscrit(a, b):
                break
    return out


# Coquilles du numéro imprimé qui l'empêchent d'être lu comme un nombre
NUMEROS_FAUTIFS = {"40b2": "4072"}
# Gloses dont le numéro manque à l'impression (la suite des numéros et l'apparat le donnent) :
# (tome, page du PDF, début du texte) → numéro
NUMEROS_OMIS = {("II", 353, "ἡγηλάζειν·"): "66"}
RE_NUM_CROCHETS = re.compile(r"^\[(\d{1,5}[a-z]?)\]$")


def _num_initial(spans):
    """Numéro de glose en gras en tête de ligne : (numéro, indice du premier span du texte)."""
    for k, sp in enumerate(spans):
        t = sp[0].strip()
        if not t:
            continue
        if sp[3] and t.split()[0] in NUMEROS_FAUTIFS:
            return NUMEROS_FAUTIFS[t.split()[0]], k, t[len(t.split()[0]):].strip()
        if RE_NUM_CROCHETS.match(t):  # « [1941] » : numéro réservé, glose omise par H
            return RE_NUM_CROCHETS.match(t).group(1), k, ""
        if sp[3] and RE_NUM.match(t):
            m = RE_NUM.match(t)
            reste = t[m.end():].strip()
            return m.group(0), k, reste
        return None, None, None
    return None, None, None


# Coquilles des numéros dans l'apparat (la page et le contenu de la note donnent le bon numéro)
COQUILLES_APPARAT = {"7272/3": "7472/3", "529/521": "520/521"}


def numeros_note(tt):
    """Numéros en tête d'une note : « 256. 262. 272. » → trois numéros ; « 519–19x » et « 4062. 63 »
    (second numéro abrégé) → numéros complets."""
    out = []
    for tok in re.findall(r"\d{1,5}[a-z]?(?:[/–-]\d{1,5}[a-z]?)?", tt):
        chiffres = re.match(r"\d+", tok).group(0)
        if out:
            base = re.match(r"\d+", out[-1]).group(0)
            if len(chiffres) < len(base):  # second numéro abrégé
                tok = base[:len(base) - len(chiffres)] + tok
        out.append(tok)
    return out


def cesures(t):
    """Apparats : « bre-\\x01vius » → « brevius », « θεσμοθε-\\x01τεῖον » → « θεσμοθετεῖον » ; \\x01 = fin de fragment."""
    t = re.sub(r"(?<=[^\W\d_])-\s*\x01(?=[a-zα-ωἀ-ῷ])", "", t)
    return t.replace("\x01", " ")


def analyser_page(page, tome=None):
    """Zones d'une page de l'édition : en-tête, lignes du texte (numéro, texte), signes de la
    marge, entrées des deux apparats (testimonia, apparat critique)."""
    lignes = kleinlogel.lignes_page(page)
    res = {"entete": "", "lettre": None, "de": None, "a": None, "page": None,
           "corps": [], "marges": [], "app1": [], "app2": [], "app": [], "notes": []}
    if not lignes:
        return res
    H = page.rect.height
    ymin = min(l["bbox"][1] for l in lignes)
    entete = [l for l in lignes if l["bbox"][1] < ymin + 4 and l["bbox"][1] < H * 0.3]
    reste = [l for l in lignes if not any(l is e for e in entete)]
    txt_ent = " ".join(l["texte"] for l in sorted(entete, key=lambda l: l["bbox"][0]))
    res["entete"] = txt_ent
    m = RE_ENTETE.search(txt_ent)
    if m:
        res["lettre"], res["de"], res["a"] = m.group(1), m.group(2), m.group(3)
    nums = [w for w in re.findall(r"(?<![\d–-])\d{1,4}(?![\d–-])", txt_ent)]
    if nums:
        res["page"] = nums[-1] if m and txt_ent.index(m.group(0)) < txt_ent.rindex(nums[-1]) else nums[0]
    # numéro de page en pied (premières pages des lettres)
    if reste:
        bas = max(reste, key=lambda l: l["bbox"][1])
        if re.fullmatch(r"\s*\d{1,4}\s*", bas["texte"]) and bas["bbox"][1] > H * 0.75:
            res["page"] = res["page"] or bas["texte"].strip()
            reste = [l for l in reste if l is not bas]
    # Texte et apparats se distinguent par le corps (10,1 pt contre 8,5 pt) ; les filets ne
    # servent qu'à séparer les deux apparats (certaines pages n'en ont qu'un, ou aucun).
    def taille_max(l):
        return max((sp[2] for sp in l["spans"] if sp[0].strip()), default=0)
    tailles = [round(taille_max(l), 1) for l in reste if _num_initial(l["spans"])[0]]
    corps_txt = max(tailles) if tailles else 10.1  # les numéros du texte sont les plus grands
    # colonne du texte : bord gauche des numéros de glose, bord droit des lignes pleines
    xs_g = [l["bbox"][0] for l in reste if _num_initial(l["spans"])[0] and taille_max(l) > 0.92 * corps_txt]
    col_g = min(xs_g) if xs_g else min((l["bbox"][0] for l in reste), default=0)
    pleines = sorted(l["bbox"][2] for l in reste if len(l["texte"]) > 35 and taille_max(l) > 0.92 * corps_txt)
    col_d = pleines[int(len(pleines) * 0.9)] if pleines else page.rect.width
    def en_marge(l):
        return l["bbox"][0] > col_d - 3 or l["bbox"][2] < col_g + 1
    fil = filets(page)
    notes_y = fil[2] if len(fil) >= 3 else None  # troisième filet : notes de l'éditeur en bas de page
    if len(fil) >= 3:
        # variante (t. I, p. 544) : note de l'éditeur entre le texte et les testimonia, sous un filet de plus
        entre = [l for l in reste if fil[0] < (l["bbox"][1] + l["bbox"][3]) / 2 < fil[1]]
        if entre and not any(sp[3] and RE_NUM.match(sp[0].strip()) for l in entre for sp in l["spans"]):
            res["notes"] += [l["texte"] for l in ordonner(entre)]
            reste = [l for l in reste if not any(l is e for e in entre)]
            fil, notes_y = fil[1:], None
    if len(fil) >= 2:   # cas ordinaire : filet texte/testimonia, filet testimonia/apparat
        fil = fil[:2]
        y_app = fil[0]
    else:               # filet(s) manquant(s) : l'apparat commence à la dernière suite de petites lignes
        ordre = sorted((l for l in reste if not en_marge(l)), key=lambda l: l["bbox"][1])
        y_app = page.rect.height + 1
        for l in reversed(ordre):
            if taille_max(l) <= 0.92 * corps_txt:
                y_app = l["bbox"][1]
            else:
                break
        y_app -= 0.5
    corps, app1, app2, app = [], [], [], []
    for l in reste:
        yc = (l["bbox"][1] + l["bbox"][3]) / 2
        if yc < y_app:
            corps.append(l)
        elif notes_y is not None and yc > notes_y:
            res["notes"].append(l["texte"])
        elif len(fil) >= 2:
            (app2 if yc > fil[1] else app1).append(l)
        elif len(fil) == 1 and fil[0] > y_app + 3:
            (app2 if yc > fil[0] else app1).append(l)
        else:
            app.append(l)
    # colonne usuelle des lignes de suite : sert à reconnaître les numéros de ligne des longues gloses
    xs_suite = Counter(round(l["bbox"][0]) for l in corps if not _num_initial(l["spans"])[0]
                       and len(l["texte"]) > 20)
    col_suite = xs_suite.most_common(1)[0][0] if xs_suite else None
    for l in ordonner(corps):
        x0, y0, x1, y1 = l["bbox"]
        if RE_TITRE.match(l["texte"]):
            continue  # grande capitale en tête de lettre
        if x0 > col_d - 3 or x1 < col_g + 1:
            res["marges"].append({"y0": y0, "y1": y1, "texte": l["texte"].strip()})
            continue
        spans = list(l["spans"])
        # signe de source dans la marge, sur la même ligne (à gauche ou à droite)
        while spans and len(spans) > 1:
            sp = spans[-1]
            ecart = sp[4][0] - spans[-2][4][2]
            if sp[4][0] > col_d - 3 and ecart > 6 and len(sp[0].strip()) <= 15:
                res["marges"].append({"y0": y0, "y1": y1, "texte": sp[0].strip()})
                spans = spans[:-1]
            else:
                break
        while (spans and len(spans) > 1 and spans[0][4][2] < col_g + 1 and not spans[0][3]
               and spans[1][4][0] - spans[0][4][2] > 6):
            res["marges"].append({"y0": y0, "y1": y1, "texte": spans[0][0].strip()})
            spans = spans[1:]
        num, k, reste_sp = _num_initial(spans)
        for (t_o, p_o, debut_o), n_o in NUMEROS_OMIS.items():
            if not num and t_o == tome and p_o == page.number + 1 and l["texte"].startswith(debut_o):
                num, k, reste_sp = n_o, -1, ""
        if not num and col_suite is not None and x0 < col_suite - 6:
            # numéro de ligne (tous les cinq vers) dans la marge d'une longue glose : « 10 (ε 26. 144) »
            m = re.match(r"\s*(\d{1,3})\s+(.*)$", spans[0][0], re.S)
            if m and int(m.group(1)) % 5 == 0:
                spans[0] = (m.group(2),) + tuple(spans[0][1:])
        if num:
            texte = (reste_sp + " " if reste_sp else "") + "".join(sp[0] for sp in spans[k + 1:])
            mx = re.match(r"\s*x(?=\s)", texte)
            if mx and not re.search(r"[a-z]$", num):  # « 2469 x » : glose ajoutée, suffixe composé à part
                num, texte = num + "x", texte[mx.end():]
        else:
            texte = "".join(sp[0] for sp in spans)
        res["corps"].append({"y0": round(y0, 1), "y1": round(y1, 1), "x0": round(x0, 1), "num": num,
                             "texte": re.sub(r"\s+", " ", texte).strip()})
    for nom, zone in (("app1", app1), ("app2", app2), ("app", app)):
        entrees = []   # [numéros, texte]
        for l in ordonner(zone):
            for sp in l["spans"]:
                t = sp[0]
                tt = t.strip()
                mm = RE_NUM.match(tt) if sp[3] else None
                if mm:
                    if RE_NUMS_SEULS.match(tt):   # « 256. 262. 272. » : plusieurs gloses
                        nums, reste = numeros_note(tt), ""
                    else:
                        nums, reste = [mm.group(0)], tt[mm.end():]
                    nums = [COQUILLES_APPARAT.get(x, x) for x in nums]
                    if entrees and entrees[-1][0] and not re.sub(r"[\s.,;–-]", "", entrees[-1][1]):
                        entrees[-1][0] += nums      # numéros successifs : une seule note
                        entrees[-1][1] = reste
                    else:
                        entrees.append([nums, reste])
                elif entrees:
                    entrees[-1][1] += t
                else:
                    entrees.append([[], t])
            if entrees:
                entrees[-1][1] += "\x01"   # fin de fragment
        res[nom] = [{"nums": n, "texte": re.sub(r"\s+", " ", cesures(t)).strip()} for n, t in entrees if t.strip() or n]
    return res


def cmd_decoder(a):
    import pymupdf
    for tome in a.tomes:
        t0 = time.time()
        doc = pymupdf.open(str(pdf_de(tome)))
        inconnus = kleinlogel.corriger(doc)
        sortie = fichier_texte(tome)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        part = sortie.with_suffix(".part")
        n_lignes = 0
        with gzip.open(part, "wt", encoding="utf-8") as f:
            for i in range(len(doc)):
                r = analyser_page(doc[i], tome)
                r["page_pdf"] = i + 1
                r["brut"] = kleinlogel.texte_page(doc[i])
                n_lignes += len(r["corps"])
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        part.rename(sortie)
        print(f"{tome} : {len(doc)} pages, {n_lignes} lignes de texte ({time.time() - t0:.0f} s) → {sortie}",
              flush=True)
        if inconnus:
            print(f"  glyphes absents de la table (non utilisés pour la plupart) : {len(inconnus)}", flush=True)


# ---------------------------------------------------------------------------
# 3. Découpage en gloses
# ---------------------------------------------------------------------------

FICHIER_GLOSES = SORTIE / "gloses.jsonl.gz"

# Coquilles de l'édition dans les numéros de glose (contrôlées sur la page : la suite des numéros
# et l'apparat, qui porte le bon numéro) : (tome, page du PDF, numéro imprimé) → numéro corrigé.
COQUILLES = {
    ("I", 183, "3978"): "3078",
    ("I", 207, "3500"): "3600",
    ("II", 184, "4471"): "4171",
}
RE_RENVOI = re.compile(r"^v\. (?:post|ante) gl\. \d+")


_G = "\u0370-\u03FF\u1F00-\u1FFF"
_RE_O_LATIN = re.compile(rf"(?<=[{_G}])o|o(?=[{_G}])")
# Livres d'Homère composés en capitales latines : « (H 316) » → « (Η 316) »
_RE_HOMERE = re.compile(r"(?<=\()([ABEZHIKMNOPTYX])(?= \d)")
_LATIN_VERS_GREC = str.maketrans("ABEZHIKMNOPTYXpiv", "ΑΒΕΖΗΙΚΜΝΟΡΤΥΧριν")
_GREC_VERS_LATIN = str.maketrans("ΑΒΕΖΗΙΚΜΝΟΡΤΥΧαινορτυ", "ABEZHIKMNOPTYXaivoptu")
# Mot grec accentué contenant une lettre latine : « Bερενικίδες », « Πλυντηpίων », « τiνα »
_RE_MOT_GREC_MIXTE = re.compile(rf"(?<![\w{_G}])[A-Za-z{_G}]*[{_G}][A-Za-z{_G}]*")
_ACCENTUEES = re.compile("[\u1F00-\u1FFF\u0386-\u03CE]")
# Abréviation latine contenant une lettre grecque : « Ηerod. », « (Ιοs. », « (Ρs. », « ΟC »
_RE_ABREV = re.compile(rf"(?<![\w{_G}])[A-Za-zΑΒΕΖΗΙΚΜΝΟΡΤΥΧαινορτυ]*[A-Za-z][A-Za-zΑΒΕΖΗΙΚΜΝΟΡΤΥΧαινορτυ]*(?=[.\s,;)]|$)")


def _corriger_mixte(m):
    w = m.group(0)
    if re.search("[A-Za-z]", w) and _ACCENTUEES.search(w) and re.fullmatch(rf"[ABEZHIKMNOPTYXpiv{_G}]+", w):
        return w.translate(_LATIN_VERS_GREC)
    return w


def _corriger_abrev(m):
    w = m.group(0)
    if re.search(f"[{_G}]", w) and not re.match(r"[gvASBr]+[α-ω]", w):  # « vgαλη » : sigles, conservés
        return w.translate(_GREC_VERS_LATIN)
    return w


def latin_grec(t):
    """Lettres d'un alphabet égarées dans l'autre, à cause des dessins communs des polices : « oἱ »,
    « κoῖλον » (o latin → ο) ; « Bερενικίδες », « (H 316) » ; « Ηerod. », « (Ρs. », « Soph. ΟC »."""
    t = _RE_O_LATIN.sub("ο", t)
    t = _RE_HOMERE.sub(lambda m: m.group(1).translate(_LATIN_VERS_GREC), t)
    t = _RE_MOT_GREC_MIXTE.sub(_corriger_mixte, t)
    return _RE_ABREV.sub(_corriger_abrev, t)


def pour_recherche(t):
    """Forme de recherche : signes éditoriaux retirés à l'intérieur des mots (« ὄρ⟨ρ⟩ος » → « ὄρρος »,
    « τὸ[ν] » → « τὸν »), pour que la normalisation ne coupe pas le mot en deux."""
    t = re.sub(r"(?<=[^\W\d_])[\[\]⟨⟩⌊⌋⌈⌉{}]+(?=[^\W\d_])", "", t)
    return t.replace("*", " ").replace("†", " ")


def joindre(lignes):
    """Lignes d'une glose → texte continu ; les césures de fin de ligne sont résolues
    (« ⟨λε- / λυμένους⟩ » → « ⟨λελυμένους⟩ »), le tiret n'étant jamais significatif ici."""
    out = ""
    for l in lignes:
        l = l.strip()
        if not l:
            continue
        if re.search(r"[^\W\d_\u0300-\u036F\]⟩⌋⌉]-$", " " + out[-2:]) or re.search(r"[^\W\d_][\]⟩⌋⌉]?-$", out):
            if re.match(r"[\[⟨⌊⌈]?[^\W\d_]", l):
                out = out[:-1] + l
                continue
        out = f"{out} {l}" if out else l
    return out


def entier(num):
    m = re.match(r"\d+", num or "")
    return int(m.group(0)) if m else None


def bornes(num):
    """« 710/11 » → (710, 711) ; « 495–9 » → (495, 499) ; « 223 » → (223, 223)."""
    m = RE_NUM.match(num or "")
    if not m:
        return None, None
    a = int(m.group(1))
    if not m.group(4):
        return a, a
    fin = m.group(4)
    b = int(m.group(1)[:len(m.group(1)) - len(fin)] + fin) if len(fin) < len(m.group(1)) else int(fin)
    return a, (b if b >= a else a)


def cmd_gloses(a):
    toutes, anomalies = [], []
    for tome in VOLUMES:
        if not fichier_texte(tome).exists():
            print(f"{tome} : texte non décodé (lancer « decoder »)")
            continue
        seq, lib = VOLUMES[tome][1], VOLUMES[tome][2]
        idx, prec, prec_num = 0, None, None
        gloses, cour, par_cle, entrees = [], None, {}, []
        commence = False
        for ligne in gzip.open(fichier_texte(tome), "rt", encoding="utf-8"):
            pg = json.loads(ligne)
            avec_num = [c for c in pg["corps"] if c["num"]]
            if not commence:  # pages liminaires : jusqu'à la première glose
                if not (pg["lettre"] and pg["lettre"] in seq and pg["de"]) and not any(entier(c["num"]) == 1 for c in avec_num):
                    continue
                commence = True
            if not pg["corps"]:
                continue
            if pg["lettre"] and pg["lettre"] in seq and seq.index(pg["lettre"]) > idx and avec_num:
                idx, prec = seq.index(pg["lettre"]), None
            sur_page = []
            for c in pg["corps"]:
                if c["num"]:
                    imprime = c["num"]
                    c["num"] = COQUILLES.get((tome, pg["page_pdf"], imprime), imprime)
                    n, fin = bornes(c["num"])
                    if prec is not None and n is not None and n <= 40 and prec - n > 50 and idx + 1 < len(seq):
                        idx, prec = idx + 1, None  # nouvelle lettre au milieu d'une page
                    lettre = seq[idx]
                    if prec is not None and n is not None and n != prec + 1 and not (n == prec and c["num"] != prec_num):
                        anomalies.append(f"{tome}\tPDF p. {pg['page_pdf']}\t{lettre} {prec_num} → {c['num']}")
                    if n is not None:
                        prec, prec_num = fin, c["num"]
                    cour = {"tome": tome, "lettre": lettre, "numero": c["num"], "debut": n, "fin": fin,
                            "ref": f"{lettre} {c['num']}", "edition": lib,
                            "page": pg["page_pdf"] - DECALAGE[tome],
                            "page_pdf": pg["page_pdf"], "pages_pdf": [pg["page_pdf"]], "lignes": [c["texte"]],
                            "y": [(c["y0"], c["y1"])], "marge": [], "testimonia": [], "apparat": []}
                    if imprime != c["num"]:
                        cour["numero_imprime"] = imprime
                    if RE_RENVOI.match(c["texte"]):  # « v. post gl. 2046 » : la glose est imprimée plus loin
                        cour["renvoi"] = True
                        gloses.append(cour)
                        continue
                    gloses.append(cour)
                    cles = {(lettre, c["num"])}
                    if n is not None and fin - n < 20 and not re.search(r"[a-z]$", c["num"]):
                        cles |= {(lettre, str(k)) for k in range(n, fin + 1)}
                    if (lettre, c["num"]) in par_cle:
                        anomalies.append(f"{tome}\tPDF p. {pg['page_pdf']}\tnuméro répété {lettre} {c['num']}")
                    for cle in cles:
                        par_cle.setdefault(cle, cour)
                    sur_page.append(cour)
                elif cour is not None:
                    cour["lignes"].append(c["texte"])
                    if pg["page_pdf"] not in cour["pages_pdf"]:
                        cour["pages_pdf"].append(pg["page_pdf"])
                        sur_page.append(cour)
                    cour["y"].append((c["y0"], c["y1"]) if cour["page_pdf"] == pg["page_pdf"] else None)
            for m in pg["marges"]:  # signe de source : glose qui a une ligne à la même hauteur
                for g in sur_page:
                    if g["page_pdf"] == pg["page_pdf"] and any(
                            yy and yy[0] - 2 <= (m["y0"] + m["y1"]) / 2 <= yy[1] + 2 for yy in g["y"]):
                        g["marge"].append(m["texte"])
                        break
            for zone, champ in (("app1", "testimonia"), ("app2", "apparat"), ("app", "apparat")):
                for e in pg[zone]:
                    entrees.append((pg["page_pdf"], idx, champ, e["nums"], e["texte"], sur_page))
            if pg["notes"]:   # note de l'éditeur en bas de page : à la suite de l'apparat
                entrees.append((pg["page_pdf"], idx, "apparat", [], "[note de l'éditeur] " + " ".join(pg["notes"]), sur_page))
        # apparats : chaque note va aux gloses dont elle porte le numéro (même page de préférence)
        derniere = {}
        for page_pdf, i_l, champ, nums, texte, sur_page in entrees:
            if not nums:  # suite d'une note de la page précédente
                g = derniere.get(champ) or (sur_page[0] if sur_page else None)
                if g is not None:
                    g[champ].append(texte)
                continue
            tete = ". ".join(nums) if len(nums) > 1 else nums[0]
            vues = set()
            for num in nums:
                a_n, b_n = bornes(num)
                cibles = [x for x in sur_page if x["numero"] == num]
                if not cibles and a_n is not None:   # note commune à plusieurs gloses, numéro groupé
                    cibles = [x for x in sur_page if x["debut"] is not None
                              and (a_n <= x["debut"] <= b_n or x["debut"] <= a_n <= x["fin"])]
                if not cibles:
                    for j in (i_l, i_l - 1, i_l + 1):
                        if 0 <= j < len(seq) and (seq[j], num) in par_cle:
                            cibles = [par_cle[(seq[j], num)]]
                            break
                if not cibles:
                    anomalies.append(f"{tome}\tPDF p. {page_pdf}\tnote d'apparat sans glose : {num}")
                    continue
                for g in cibles:
                    if id(g) not in vues:
                        vues.add(id(g))
                        g[champ].append(f"{tete} {texte}".strip())
                        derniere[champ] = g
        for g in gloses:
            texte = latin_grec(joindre(g.pop("lignes")))
            ys = [y for y in g.pop("y") if y]
            g["y"] = [min(y[0] for y in ys), max(y[1] for y in ys)]
            g["texte"] = texte.strip()
            m = re.match(r"^[*†⌈⌊\[⟨(]*([^·:]+?)·", g["texte"])
            g["lemme"] = m.group(1).strip() if m else ""
            g["marge"] = " ".join(g["marge"])
            g["testimonia"] = latin_grec(" ".join(g["testimonia"]))
            g["apparat"] = latin_grec(" ".join(g["apparat"]))
        compte = {}
        for g in gloses:
            compte[g["lettre"]] = compte.get(g["lettre"], 0) + 1
        print(f"{tome} : {len(gloses)} gloses — " + ", ".join(f"{k} {v}" for k, v in compte.items()), flush=True)
        toutes += gloses
    part = FICHIER_GLOSES.with_suffix(".part")
    with gzip.open(part, "wt", encoding="utf-8") as f:
        for g in toutes:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")
    part.rename(FICHIER_GLOSES)
    (SORTIE / "anomalies.tsv").write_text("tome\tpage\tanomalie\n" + "\n".join(anomalies) + "\n", encoding="utf-8")
    print(f"{len(toutes)} gloses → {FICHIER_GLOSES} ; {len(anomalies)} anomalies → {SORTIE / 'anomalies.tsv'}")


# ---------------------------------------------------------------------------
# 4. Qualité et tests
# ---------------------------------------------------------------------------

FICHIER_QUALITE = SORTIE / "qualite.json"
FICHIER_LEXIQUE = SORTIE / "lexique_tei.txt.gz"
RE_GREC = re.compile(r"[α-ω]")


def lexique_tei():
    """Formes normalisées attestées dans les textes TEI (Perseus, First1KGreek) : la mesure du taux
    de mots reconnus est celle d'indexer.py (mots grecs de 4 lettres et plus). Cache : lexique_tei.txt.gz."""
    if FICHIER_LEXIQUE.exists():
        return set(gzip.open(FICHIER_LEXIQUE, "rt", encoding="utf-8").read().split())
    import sqlite3
    con = sqlite3.connect(f"file:{RACINE / '.sources' / 'corpus' / 'index.sqlite'}?mode=ro", uri=True)
    lex = set()
    for (norm,) in con.execute("SELECT p.norm FROM passages p JOIN oeuvres o ON o.id = p.oeuvre_id "
                               "WHERE o.collection IN ('perseus', 'first1k')"):
        lex.update(norm.split())
    with gzip.open(FICHIER_LEXIQUE, "wt", encoding="utf-8") as f:
        f.write("\n".join(sorted(lex)))
    return lex


def mots_grecs(texte):
    from grec import normaliser
    return [w for w in normaliser(texte).split() if len(w) >= 4 and RE_GREC.match(w)]


def texte_ocr_page(tome, i):
    """Mots de l'OCR d'une page (texte, confiance), dans l'ordre de lecture de Tesseract."""
    f = fichier_ocr(tome, i)
    out = []
    if not f.exists():
        return out
    with gzip.open(f, "rt", encoding="utf-8") as g:
        next(g)
        for l in g:
            c = l.rstrip("\n").split("\t")
            if len(c) >= 12 and c[0] == "5" and c[11].strip():
                out.append((c[11], float(c[10])))
    return out


def _qualite_page(args):
    """Compare, sur une page de gloses, l'OCR et le texte décodé (mots de 4 lettres et plus)."""
    tome, page_pdf, brut, lex = args
    from grec import forme_exacte, normaliser
    ocr = [w for w, _ in texte_ocr_page(tome, page_pdf - 1)]
    m_ocr = mots_grecs(" ".join(ocr))
    m_dec = mots_grecs(brut)
    c_ocr, c_dec = Counter(m_ocr), Counter(m_dec)
    commun = sum((c_ocr & c_dec).values())
    e_ocr = Counter(w for w in forme_exacte(" ".join(ocr)).split() if len(w) >= 4 and normaliser(w) in c_dec)
    e_dec = Counter(w for w in forme_exacte(brut).split() if len(w) >= 4 and normaliser(w) in c_ocr)
    return {"tome": tome, "page_pdf": page_pdf, "n_ocr": len(m_ocr), "n_dec": len(m_dec),
            "connus_ocr": sum(1 for w in m_ocr if w in lex), "connus_dec": sum(1 for w in m_dec if w in lex),
            "commun": commun, "commun_exact": sum((e_ocr & e_dec).values()),
            "inconnus_dec": [w for w in m_dec if w not in lex and w not in c_ocr][:200]}


_LEX = None


def _init_lex(lex):
    global _LEX
    _LEX = lex


def _qualite_page_w(args):
    return _qualite_page(args + (_LEX,))


def controle_numerotation():
    """Suite des numéros : titres courants (premier et dernier numéro de chaque page), lacunes."""
    res = {}
    for tome in VOLUMES:
        ok, ko, details, pages_ok, pages_ko = 0, 0, [], 0, 0
        for ligne in gzip.open(fichier_texte(tome), "rt", encoding="utf-8"):
            pg = json.loads(ligne)
            imprime = re.fullmatch(r"\d+", pg["page"] or "")
            if imprime and pg["de"]:
                if int(pg["page"]) == pg["page_pdf"] - DECALAGE[tome]:
                    pages_ok += 1
                else:
                    pages_ko += 1
            nums = [c["num"] for c in pg["corps"] if c["num"]]
            if not (pg["de"] and pg["a"] and nums):
                continue
            d = re.sub(r"[/–-].*$", "", nums[0])
            f = re.sub(r"^.*[/–-]", "", nums[-1])
            prem, dern = pg["de"], pg["a"]
            if len(f) < len(dern):  # dernier numéro abrégé (« 374-4b »)
                f = dern[:len(dern) - len(f)] + f
            if d == prem and (f == dern or len(dern) < len(d) and f.endswith(dern)):
                ok += 1
            else:
                ko += 1
                details.append(f"PDF p. {pg['page_pdf']} : titre {prem}–{dern}, gloses {nums[0]}–{nums[-1]}")
        res[tome] = {"pages_titre_ok": ok, "pages_titre_ecart": ko, "ecarts": details,
                     "folio_ok": pages_ok, "folio_ecart": pages_ko}
    return res


def cmd_qualite(a):
    lex = lexique_tei()
    print(f"lexique TEI : {len(lex)} formes", flush=True)
    gloses = [json.loads(l) for l in gzip.open(FICHIER_GLOSES, "rt", encoding="utf-8")]
    premieres = {}
    for g in gloses:
        premieres.setdefault(g["tome"], g["page_pdf"])
    taches = []
    for tome in VOLUMES:
        for ligne in gzip.open(fichier_texte(tome), "rt", encoding="utf-8"):
            pg = json.loads(ligne)
            if pg["page_pdf"] >= premieres[tome] and pg["corps"]:
                taches.append((tome, pg["page_pdf"], pg["brut"]))
    with cf.ProcessPoolExecutor(a.processus, initializer=_init_lex, initargs=(lex,)) as ex:
        pages = list(ex.map(_qualite_page_w, taches, chunksize=20))
    res = {"date": time.strftime("%Y-%m-%d %H:%M"), "tomes": {}, "formes_lexique": len(lex)}
    inconnus = Counter()
    for tome in VOLUMES:
        ps = [p for p in pages if p["tome"] == tome]
        n_o, n_d = sum(p["n_ocr"] for p in ps), sum(p["n_dec"] for p in ps)
        c_o, c_d = sum(p["connus_ocr"] for p in ps), sum(p["connus_dec"] for p in ps)
        cm, ce = sum(p["commun"] for p in ps), sum(p["commun_exact"] for p in ps)
        for p in ps:
            inconnus.update(p["inconnus_dec"])
        gl = [g for g in gloses if g["tome"] == tome]
        res["tomes"][tome] = {
            "pages_gloses": len(ps), "gloses": len(gl),
            "mots_ocr": n_o, "taux_ocr": round(c_o / n_o, 4), "mots_decodes": n_d, "taux_decodage": round(c_d / n_d, 4),
            "accord_ocr_decodage": round(cm / n_d, 4), "accord_avec_diacritiques": round(ce / cm, 4) if cm else None,
            "gloses_sans_lemme": sum(1 for g in gl if not g["lemme"] and not g.get("renvoi")),
            "gloses_vides": sum(1 for g in gl if not g["texte"] and not g.get("renvoi")),
            "lettre_divergente": sum(1 for g in gl if g["lemme"] and not premiere_lettre_ok(g)),
        }
    res["numerotation"] = controle_numerotation()
    res["lacunes"] = lacunes_numerotation(gloses)
    res["inconnus_decodes_frequents"] = inconnus.most_common(60)
    FICHIER_QUALITE.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for t, r in res["tomes"].items():
        print(t, json.dumps(r, ensure_ascii=False))
    for t, r in res["numerotation"].items():
        print(t, {k: v for k, v in r.items() if k != "ecarts"}, r["ecarts"][:12])
    print("lacunes :", res["lacunes"])
    print(f"→ {FICHIER_QUALITE}")


def premiere_lettre_ok(g):
    from grec import normaliser
    lem = normaliser(g["lemme"])
    return lem.startswith(g["lettre"].replace("ς", "σ"))


def lacunes_numerotation(gloses):
    """Numéros manquants dans chaque lettre (hors suffixes et numéros groupés)."""
    par = {}
    for g in gloses:
        if g["debut"] is not None:
            par.setdefault(g["lettre"], set()).update(range(g["debut"], g["fin"] + 1))
    res = {}
    for l, ns in par.items():
        manque = [n for n in range(1, max(ns) + 1) if n not in ns]
        res[l] = {"dernier": max(ns), "manquants": manque}
    return res


# Gloses de contrôle : (référence, début attendu du texte), lues sur l'image de la page.
ATTENDUES = [
    ("χ 576", "χοάνη· χώνη"),
    ("χ 575", "*χοανεῦσαι· χωνεῦσαι"),
    ("φ 528", "*φιλότης· φιλία"),
    ("π 205", "παλινδία· ἡ ἐξ ὑποστροφῆς"),
    ("π 208", "παλιμπλάκτοισιν· ὀπισθορμήτοις"),
    ("κ 1", "†κααρτίας· βάτραχος"),
    ("λ 403", "λατρεύει· ἐλεύθερος ὢν"),
    ("λ 415", "*⟩λαυκή· φοβερά"),
    ("η 66", "ἡγηλάζειν· ἄγειν"),
    ("α 8382", "ἀϋτή· ἐπὶ μὲν τῆς φωνῆς"),
    ("α 2626", "ἀκροατήριον· τόπος ἐν ᾧ συνάγονται"),
]
FICHIER_TESTIMONIA = RACINE / "recherche" / "testimonia.md"
FICHIER_CONTROLE = SORTIE / "controle_testimonia.tsv"
FICHIER_ABSENTES = SORTIE / "thesmophories_hors_testimonia.tsv"


def charger_gloses():
    return {g["ref"]: g for g in (json.loads(l) for l in gzip.open(FICHIER_GLOSES, "rt", encoding="utf-8"))}


def reference_complete(g):
    """« Hsch. α 1234 (Latte I, p. 58) » ; numéro de page imprimé dans le volume cité."""
    return f"Hsch. {g['ref']} ({g['edition']}, p. {g['page']})"


def citations_testimonia():
    """Lignes de recherche/testimonia.md dont la source est Hésychius : (ligne, vers, référence, citation)."""
    if not FICHIER_TESTIMONIA.exists():
        return
    for n, l in enumerate(FICHIER_TESTIMONIA.read_text(encoding="utf-8").splitlines(), 1):
        c = [x.strip() for x in l.split("|")]
        if len(c) < 7 or c[2] != "Hésychius":
            continue
        for m in re.finditer(r"(?:Hesychius |Hsch\. )?\b([α-ω]) (\d{1,4})(?:[-–](\d{1,4}))?", c[3]):
            # (« Moeris χ 1 Hesychius χ 576 χοάνη » : seule la référence d'Hésychius compte)
            avant = c[3][:m.start()]
            if re.search(r"(Moeris|Photius|Souda|Pollux)\s*$", avant):
                continue
            yield n, c[1], m.group(1), m.group(2), m.group(3), c[5] if c[5] != "—" else c[3]


def cmd_tester(a):
    from grec import normaliser
    gl = charger_gloses()
    echecs = 0
    for ref, debut in ATTENDUES:
        g = gl.get(ref)
        ok = bool(g) and g["texte"].startswith(debut)
        echecs += not ok
        print(f"[{'OK ' if ok else 'ÉCHEC'}] {ref} : {g['texte'][:60] if g else 'absente'}")
    lignes, compte = [], Counter()
    for n, vers, lettre, num, fin, cite in citations_testimonia():
        ref = f"{lettre} {num}"
        mots = normaliser(pour_recherche(re.split(r"[·:]", cite)[0])).split()
        # « ο 265-266 » : toutes les gloses de l'intervalle sont candidates
        candidates = [gl.get(f"{lettre} {k}") for k in range(int(num), int(fin or num) + 1)]
        candidates = [c for c in candidates if c] or [
            x for x in gl.values() if x["lettre"] == lettre and x["debut"] is not None
            and x["debut"] <= int(num) <= x["fin"]][:1]   # numéro groupé (« 710/11 »)
        etat, g = "absente", None
        for c in candidates:
            cible = normaliser(pour_recherche(c["texte"])).split()
            prefixes = [w[:max(4, len(w) - 2)] for w in mots]
            if mots and all(w in cible for w in mots):
                etat, g = "lemme confirmé", c
                break
            if mots and all(any(x.startswith(p) for x in cible) for p in prefixes):
                etat, g = "autre forme du lemme", c
            elif g is None:
                etat, g = "lemme différent", c
        compte[etat] += 1
        lignes.append("\t".join([str(n), vers, ref, reference_complete(g) if g else "", etat, cite[:80],
                                 (g["texte"][:100] if g else "")]))
    FICHIER_CONTROLE.write_text("ligne\tvers\tref\treference_complete\tetat\tcitation\ttexte_edition\n"
                                + "\n".join(lignes) + "\n", encoding="utf-8")
    print(f"testimonia.md : {len(lignes)} références d'Hésychius — {dict(compte)} → {FICHIER_CONTROLE}")
    cites = set()
    for _, _, lettre, num, fin, _ in citations_testimonia():
        cites.update(f"{lettre} {k}" for k in range(int(num), int(fin or num) + 1))
    # renvois à Hésychius dans les lignes des autres sources (« Photius β 62, Hesychius β 211 »)
    if FICHIER_TESTIMONIA.exists():
        cites.update(f"{x} {n}" for x, n in re.findall(r"H[eé]s[yéi]chius ([α-ω]) (\d+)",
                                                       FICHIER_TESTIMONIA.read_text(encoding="utf-8")))
    manquantes = []
    for ref, g in gl.items():
        for zone, t in (("texte", g["texte"]), ("apparats", g["testimonia"] + " " + g["apparat"])):
            vers = re.findall(r"Thesm\.\s*(\d+[a-z]?)", t)
            if vers:
                if ref not in cites:
                    manquantes.append("\t".join([reference_complete(g), zone, ", ".join(vers), g["lemme"]]))
                break
    FICHIER_ABSENTES.write_text("reference\tzone\tvers\tlemme\n" + "\n".join(manquantes) + "\n", encoding="utf-8")
    print(f"gloses rapportées aux Thesmophories par l'édition, absentes de testimonia.md : {len(manquantes)}"
          f" → {FICHIER_ABSENTES}")
    for l in lignes:
        c = l.split("\t")
        if c[4] != "lemme confirmé":
            print("   ", c[1], c[2], "—", c[4], "—", c[5][:40], "—", c[6][:60])
    sys.exit(1 if echecs else 0)


DOSSIER_ECHANTILLON = RACINE / ".travail" / "hesychius" / "echantillon"


def cmd_echantillon(a):
    """Tire un échantillon de gloses (graine fixe, proportionnel aux tomes), découpe leurs images en
    planches et écrit le texte décodé en regard : contrôle visuel, glose par glose."""
    import random
    import pymupdf
    from PIL import Image, ImageDraw, ImageFont
    gl = [g for g in charger_gloses().values() if g["texte"] and not g.get("renvoi") and len(g["pages_pdf"]) == 1]
    random.seed(a.graine)
    choix = sorted(random.sample(gl, a.nombre), key=lambda g: (list(VOLUMES).index(g["tome"]), g["page_pdf"]))
    DOSSIER_ECHANTILLON.mkdir(parents=True, exist_ok=True)
    docs = {t: pymupdf.open(str(pdf_de(t))) for t in VOLUMES}
    planches, cour, h = [], [], 0
    for g in choix:
        page = docs[g["tome"]][g["page_pdf"] - 1]
        clip = pymupdf.Rect(page.rect.x0, g["y"][0] - 1.5, page.rect.x1, g["y"][1] + 1.5)
        pm = page.get_pixmap(dpi=a.dpi, clip=clip, colorspace=pymupdf.csGRAY)
        im = Image.frombytes("L", (pm.width, pm.height), pm.samples)
        if h + im.height + 26 > 1500:
            planches.append(cour)
            cour, h = [], 0
        cour.append((g, im))
        h += im.height + 26
    planches.append(cour)
    police = ImageFont.load_default()
    lignes = ["planche\tref\treference\ttexte"]
    for k, pl in enumerate(planches, 1):
        W = max(im.width for _, im in pl)
        H = sum(im.height + 26 for _, im in pl)
        c = Image.new("L", (W, H), 255)
        d = ImageDraw.Draw(c)
        y = 0
        for g, im in pl:
            d.text((4, y + 4), f"{g['tome']} {g['ref']}  PDF p. {g['page_pdf']}", fill=0, font=police)
            d.line((0, y + 2, W, y + 2), fill=128)
            c.paste(im, (0, y + 22))
            y += im.height + 26
            lignes.append(f"{k}\t{g['ref']}\t{reference_complete(g)}\t{g['texte']}")
        c.save(DOSSIER_ECHANTILLON / f"planche_{k:02d}.png")
    (DOSSIER_ECHANTILLON / "echantillon.tsv").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(choix)} gloses, {len(planches)} planches → {DOSSIER_ECHANTILLON}")


def cmd_voir(a):
    """Affiche une glose (texte, apparats, OCR de ses lignes) et découpe son image pour contrôle."""
    import pymupdf
    gl = charger_gloses()
    ref = " ".join(a.ref)
    g = gl.get(ref)
    if g is None:
        sys.exit(f"glose absente : {ref}")
    print(reference_complete(g), f"— PDF p. {g['page_pdf']}, {VOLUMES[g['tome']][0]}")
    print("marge :", g["marge"] or "—")
    print("texte :", g["texte"])
    print("test. :", g["testimonia"] or "—")
    print("app.  :", g["apparat"] or "—")
    doc = pymupdf.open(str(pdf_de(g["tome"])))
    page = doc[g["page_pdf"] - 1]
    y0, y1 = g["y"]
    clip = pymupdf.Rect(0, max(0, y0 - 14), page.rect.width, min(page.rect.height, y1 + 14))
    d = RACINE / ".travail" / "hesychius" / "voir"
    d.mkdir(parents=True, exist_ok=True)
    f = d / f"{g['lettre']}_{g['numero'].replace('/', '-')}.png"
    page.get_pixmap(dpi=a.dpi, clip=clip, colorspace=pymupdf.csGRAY).save(str(f))
    print("image :", f)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("ocr", help="OCR Tesseract des pages (reprenable)")
    p.add_argument("--tomes", nargs="*", default=list(VOLUMES))
    p.add_argument("--pages", help="pages du PDF (1 = première), séparées par des virgules")
    p.add_argument("--processus", type=int, default=8)
    p.add_argument("--dpi", type=int, default=400)
    p.add_argument("--langues", default="grc+lat")
    p.add_argument("--psm", type=int, default=4)
    p.set_defaults(f=cmd_ocr)
    for nom, f, aide in (("decoder", cmd_decoder, "décodage de la couche texte (polices Kleinlogel)"),
                         ("gloses", cmd_gloses, "découpage en gloses référencées"),
                         ("qualite", cmd_qualite, "mesures de qualité (OCR et décodage)"),
                         ("tester", cmd_tester, "tests de contrôle (gloses attendues)")):
        p = sp.add_parser(nom, help=aide)
        p.add_argument("--tomes", nargs="*", default=list(VOLUMES))
        p.add_argument("--processus", type=int, default=8)
        p.set_defaults(f=f)
    p = sp.add_parser("echantillon", help="planches de contrôle visuel d'un échantillon de gloses")
    p.add_argument("--nombre", type=int, default=60)
    p.add_argument("--graine", type=int, default=20261101)
    p.add_argument("--dpi", type=int, default=230)
    p.set_defaults(f=cmd_echantillon)
    p = sp.add_parser("voir", help="une glose : texte, apparats et image de contrôle (« voir χ 576 »)")
    p.add_argument("ref", nargs=2, metavar="REF", help="lettre et numéro")
    p.add_argument("--dpi", type=int, default=250)
    p.set_defaults(f=cmd_voir)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
