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
« Hsch. α 223 (Latte I, p. 13) » dans la numérotation de l'édition, qui est celle de
Latte (inchangée dans la 2e éd. de Cunningham, t. I, Prolegomena § VII).

Sorties (non versionnées, l'édition étant sous droits) : .sources/corpus/hesychius/
  ocr/<tome>/p0001.tsv.gz      OCR Tesseract (mots, boîtes, confiance), une page par fichier
  texte/<tome>.jsonl.gz        texte décodé, ligne par ligne, avec zone et police
  gloses.jsonl.gz              une glose par ligne (lettre, numéro, tome, page, texte, apparats)
  qualite.json                 mesures de qualité (voir recherche/corpus_numeriques.md)

  python3 outils/corpus/ocr_hesychius.py ocr --processus 8      # reprenable
  python3 outils/corpus/ocr_hesychius.py decoder
  python3 outils/corpus/ocr_hesychius.py gloses
  python3 outils/corpus/ocr_hesychius.py qualite
  python3 outils/corpus/ocr_hesychius.py tester
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
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
DRIVE = RACINE / ".sources" / "drive" / "fichiers"
HSCH = DRIVE / "Grec" / "Lexiques" / "Hesychius"
SORTIE = RACINE / ".sources" / "corpus" / "hesychius"
sys.path.insert(0, str(ICI))
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


def pdf_de(tome):
    return HSCH / VOLUMES[tome][0]


def ouvrir(tome):
    import pymupdf
    return pymupdf.open(str(pdf_de(tome)))


# ---------------------------------------------------------------------------
# 1. OCR (Tesseract, 400 dpi), reprenable page par page
# ---------------------------------------------------------------------------

def fichier_ocr(tome, i):
    f = SORTIE / "ocr" / tome / f"p{i + 1:04d}.tsv.gz"
    if tome == "II" and not f.exists():  # premier lancement : dossier nommé « IIa »
        ancien = SORTIE / "ocr" / "IIa" / f.name
        if ancien.exists():
            return ancien
    return f


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


def _num_initial(spans):
    """Numéro de glose en gras en tête de ligne : (numéro, indice du premier span du texte)."""
    for k, sp in enumerate(spans):
        t = sp[0].strip()
        if not t:
            continue
        if sp[3] and RE_NUM.match(t):
            m = RE_NUM.match(t)
            reste = t[m.end():].strip()
            return m.group(0), k, reste
        return None, None, None
    return None, None, None


def analyser_page(page):
    """Zones d'une page de l'édition : en-tête, lignes du texte (numéro, texte), signes de la
    marge, entrées des deux apparats (testimonia, apparat critique)."""
    import kleinlogel
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
    for l in sorted(corps, key=lambda l: (round(l["bbox"][1]), l["bbox"][0])):
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
        for l in sorted(zone, key=lambda l: (round(l["bbox"][1]), l["bbox"][0])):
            for sp in l["spans"]:
                t = sp[0]
                tt = t.strip()
                mm = RE_NUM.match(tt) if sp[3] else None
                if mm:
                    if RE_NUMS_SEULS.match(tt):   # « 256. 262. 272. » : plusieurs gloses
                        nums, reste = re.findall(r"\d{1,5}[a-z]?", tt), ""
                    else:
                        nums, reste = [mm.group(0)], tt[mm.end():]
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
                entrees[-1][1] += " "
        res[nom] = [{"nums": n, "texte": re.sub(r"\s+", " ", t).strip()} for n, t in entrees if t.strip() or n]
    return res


def cmd_decoder(a):
    import pymupdf
    import kleinlogel
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
                r = analyser_page(doc[i])
                r["page_pdf"] = i + 1
                n_lignes += len(r["corps"])
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        part.rename(sortie)
        usage = {}
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
    ("II", 680, "40b2"): "4072",
}
RE_RENVOI = re.compile(r"^v\. (?:post|ante) gl\. \d+")


_RE_O_LATIN = re.compile(r"(?<=[\u0370-\u03FF\u1F00-\u1FFF])o|o(?=[\u0370-\u03FF\u1F00-\u1FFF])")


def latin_grec(t):
    """« oἱ », « κoῖλον » : o latin composé par erreur au contact de lettres grecques → ο."""
    return _RE_O_LATIN.sub("ο", t)


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
                            "ref": f"{lettre} {c['num']}", "edition": lib, "page": pg["page"],
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
                    if n is not None and fin - n < 20:
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
        # apparats : chaque note va aux gloses dont elle porte le numéro (même page de préférence)
        derniere = {}
        for page_pdf, i_l, champ, nums, texte, sur_page in entrees:
            if not nums:  # suite d'une note de la page précédente
                g = derniere.get(champ) or (sur_page[0] if sur_page else None)
                if g is not None:
                    g[champ].append(texte)
                continue
            tete = ". ".join(nums) if len(nums) > 1 else nums[0]
            for num in nums:
                g = next((x for x in sur_page if x["numero"] == num or (x["debut"] is not None and entier(num) is not None and x["debut"] <= entier(num) <= x["fin"] and x["fin"] - x["debut"] < 20)), None)
                for j in (i_l, i_l - 1, i_l + 1):
                    if g is None and 0 <= j < len(seq):
                        g = par_cle.get((seq[j], num))
                if g is None:
                    anomalies.append(f"{tome}\tPDF p. {page_pdf}\tnote d'apparat sans glose : {num}")
                    continue
                g[champ].append(f"{tete} {texte}".strip())
                derniere[champ] = g
        for g in gloses:
            texte = latin_grec(" ".join(g.pop("lignes")))
            texte = re.sub(r"(\w)- (\w)", r"\1\2", texte)  # césures de fin de ligne
            g.pop("y")
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

def cmd_qualite(a):
    raise SystemExit("à venir")


def cmd_tester(a):
    raise SystemExit("à venir")


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
        p.set_defaults(f=f)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
