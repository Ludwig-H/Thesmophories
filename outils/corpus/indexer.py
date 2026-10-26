#!/usr/bin/env python3
"""Construit l'index plein texte (SQLite FTS5) du corpus grec local.

Entrées (dans .sources/corpus/, voir telecharger.py et README.md) :
  canonical-greekLit/data   Perseus (TEI CTS)                  → collection « perseus »
  First1KGreek/data         Open Greek and Latin (TEI CTS)     → collection « first1k »
  ocr_archive/<id>/         OCR archive.org (sources_ocr.tsv)  → collection « ocr »
  lexica/…/lsj              LSJ (TEI P4, Beta Code)            → collection « lsj »
  idp.data/DCLP             papyrus littéraires (EpiDoc)       → collection « dclp »
  ../drive/fichiers/…       PDF du Drive de l'auteur (sources_drive.tsv, couche texte,
                            sous droits : usage local)          → collection « drive »
  diorisis/x                Diorisis (formes lemmatisées)      → table « formes »

Sortie : .sources/corpus/index.sqlite (construit dans un fichier temporaire puis renommé :
une recherche en cours n'est jamais perturbée).

Chaque « passage » est la plus petite unité citable : vers, section ou entrée (TEI),
article de lexique ou page/colonne (OCR), page (PDF). Le texte original (NFC) et sa forme
normalisée (grec.normaliser : sans diacritiques, minuscules, σ = ς, sans apostrophes ni
coronis) sont stockés ; l'index FTS5 « passages_fts » porte sur la forme normalisée.
  - « fenetres_fts » indexe la jointure de deux passages consécutifs (20 + 20 mots) pour
    trouver une expression à cheval sur deux vers, deux sections ou deux pages ;
  - « souple_fts » indexe, pour l'OCR et les PDF seulement, la forme « pliée »
    (grec.plier_ocr : χ = κ, lettres latines des mots grecs translittérées, ζ final = σ).
Chaque œuvre porte une étiquette de fiabilité (oeuvres.fiabilite) et, pour l'OCR et les
PDF, un taux de mots grecs reconnus (oeuvres.score_ocr : part des mots grecs de 4 lettres
et plus attestés dans les textes TEI).

  python3 outils/corpus/indexer.py                    # tout, 8 processus
  python3 outils/corpus/indexer.py --sources perseus first1k --processus 4
"""

import argparse
import csv
import glob
import gzip
import json
import multiprocessing as mp
import os
import re
import sqlite3
import subprocess
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from grec import beta_vers_unicode, normaliser, plier_ocr  # noqa: E402

from lxml import etree  # noqa: E402

RACINE = ICI.parent.parent
CORPUS = RACINE / ".sources" / "corpus"
DRIVE = RACINE / ".sources" / "drive" / "fichiers"
BASE = CORPUS / "index.sqlite"

TEI = "http://www.tei-c.org/ns/1.0"
NS = {"tei": TEI}
CTS = {"ti": "http://chs.harvard.edu/xmlns/cts"}
FENETRE = 20  # mots de part et d'autre de la jointure entre deux passages

PARSEUR = etree.XMLParser(huge_tree=True, remove_comments=True, remove_pis=True,
                          resolve_entities=False, load_dtd=False, no_network=True)
PARSEUR_SOUPLE = etree.XMLParser(huge_tree=True, remove_comments=True, remove_pis=True,
                                 resolve_entities=False, load_dtd=False, no_network=True,
                                 recover=True)

# nom → (description, licence, url, étiquette de fiabilité)
COLLECTIONS = {
    "perseus": ("Perseus Digital Library, canonical-greekLit", "CC BY-SA 4.0",
                "https://github.com/PerseusDL/canonical-greekLit",
                "TEI : texte numérisé et corrigé (Perseus)"),
    "first1k": ("Open Greek and Latin, First1KGreek", "CC BY-SA 4.0",
                "https://github.com/OpenGreekAndLatin/First1KGreek",
                "TEI : texte numérisé et corrigé (OGL, First1KGreek)"),
    "ocr": ("Ouvrages du domaine public, OCR Tesseract d'archive.org (non corrigé)",
            "domaine public (OCR : archive.org)", "https://archive.org",
            "OCR non corrigé : vérifier sur l'image"),
    "lsj": ("Liddell–Scott–Jones, Greek-English Lexicon (Perseus)", "CC BY-SA 4.0",
            "https://github.com/PerseusDL/lexica", "TEI : LSJ (Perseus)"),
    "dclp": ("Digital Corpus of Literary Papyri (papyri.info)", "CC BY 3.0",
             "https://github.com/papyri/idp.data", "EpiDoc : papyrus littéraires (DCLP)"),
    "drive": ("PDF du Drive de l'auteur (couche texte)", "sous droits : usage local, jamais versionné",
              ".sources/drive/fichiers", "couche texte de PDF (native ou OCR) : vérifier sur la page"),
}


def nfc(s):
    return unicodedata.normalize("NFC", s)


def espaces(s):
    return " ".join(s.split())


def local(tag):
    if not isinstance(tag, str):
        return None
    return tag.rsplit("}", 1)[-1]


# ---------------------------------------------------------------------------
# Extraction du texte d'un élément TEI
# ---------------------------------------------------------------------------

IGNORES = {
    "note", "bibl", "speaker", "stage", "figDesc", "figure", "fw", "label",
    "teiHeader", "rdg", "rdgGrp", "wit", "witDetail", "castList", "certainty",
    "precision", "handShift", "am", "listBibl", "interp", "interpGrp", "index",
}
BLOCS = {"p", "div", "ab", "lg", "sp", "head", "list", "item", "table", "row",
         "cell", "quote", "cit", "opener", "closer", "dateline", "salute",
         "signed", "trailer", "argument", "epigraph", "byline", "docTitle"}
CROCHETS_TEI = {"del": ("[", "]"), "add": ("⟨", "⟩"), "supplied": ("⟨", "⟩"),
                "surplus": ("{", "}"), "secl": ("[", "]")}
CROCHETS_PAP = {"del": ("⟦", "⟧"), "add": ("\\", "/"), "surplus": ("{", "}")}
PREF_CHOIX = ("corr", "reg", "expan", "lem", "sic", "orig", "abbr", "seg")


def choisir(choice):
    enfants = [c for c in choice if isinstance(c.tag, str)]
    for nom in PREF_CHOIX:
        for c in enfants:
            if local(c.tag) == nom:
                return c
    return enfants[0] if enfants else None


def extraire(el, out, haut=True, papyrus=False):
    """Ajoute à `out` le texte de `el` (sans sa queue)."""
    tag = local(el.tag)
    if tag is None or tag in IGNORES:
        return
    if tag == "choice":
        c = choisir(el)
        if c is not None:
            extraire(c, out, False, papyrus)
        return
    if tag == "app":
        lem = [c for c in el if local(c.tag) == "lem"]
        if lem:
            extraire(lem[0], out, False, papyrus)
        return
    if tag == "gap":
        out.append(" … ")
        return
    if tag in ("lb", "cb"):
        out.append("" if el.get("break") == "no" else (" | " if papyrus else " "))
        return
    if tag in ("pb", "milestone", "space"):
        out.append(" " if tag == "space" else "")
        return
    if tag == "g" and papyrus and not (el.text or "").strip():
        return
    if papyrus:
        if tag == "supplied":
            o, f = ("[", "]") if el.get("reason") == "lost" else ("⟨", "⟩")
        else:
            o, f = CROCHETS_PAP.get(tag, ("", ""))
    else:
        o, f = CROCHETS_TEI.get(tag, ("", ""))
    if tag == "l" and not haut:
        prec = el.getprevious()
        while prec is not None and not isinstance(prec.tag, str):
            prec = prec.getprevious()
        if prec is not None and local(prec.tag) == "l":
            out.append(" / ")
        else:
            out.append(" ")
    elif tag in BLOCS:
        out.append(" ")
    out.append(o)
    if el.text:
        out.append(el.text)
    for c in el:
        extraire(c, out, False, papyrus)
        if c.tail:
            out.append(c.tail)
    out.append(f)
    if tag in BLOCS:
        out.append(" ")


def texte_de(el, papyrus=False):
    out = []
    extraire(el, out, True, papyrus)
    s = espaces(nfc("".join(out)))
    # espaces superflues à l'intérieur des crochets éditoriaux
    s = re.sub(r"([\[⟨{⟦]) ", r"\1", s)
    s = re.sub(r" ([\]⟩}⟧])", r"\1", s)
    s = s.replace("[]", "").replace("⟨⟩", "")
    return s.strip()


def locuteur_de(el):
    p = el.getparent()
    while p is not None:
        if local(p.tag) == "sp":
            for c in p:
                if local(c.tag) == "speaker":
                    return espaces(nfc("".join(c.itertext()))) or None
            return None
        if local(p.tag) in ("div", "body"):
            return None
        p = p.getparent()
    return None


# ---------------------------------------------------------------------------
# Collections TEI CTS (Perseus, First1KGreek)
# ---------------------------------------------------------------------------

def xpath_niveau(rp):
    m = re.match(r"\s*#xpath\((.*)\)\s*$", rp, re.S)
    xp = (m.group(1) if m else rp).replace("\\'", "'").replace('\\"', '"')
    return re.sub(r"@n\s*=\s*['\"]\$\d+['\"]", "@n", xp)


def lire_cts(chemin):
    try:
        return etree.parse(str(chemin), PARSEUR)
    except Exception:
        return None


def meta_oeuvre(fichier):
    """Métadonnées CTS : auteur (textgroup), titre, description de l'édition."""
    d_oeuvre = Path(fichier).parent
    d_auteur = d_oeuvre.parent
    stem = Path(fichier).name[:-4]
    meta = {"auteur": d_auteur.name, "titre": d_oeuvre.name, "edition": "", "langue": ""}
    g = lire_cts(d_auteur / "__cts__.xml")
    if g is not None:
        gn = g.xpath("string(//ti:groupname)", namespaces=CTS).strip()
        if gn:
            meta["auteur"] = espaces(gn)
    w = lire_cts(d_oeuvre / "__cts__.xml")
    if w is not None:
        titres = w.xpath("/ti:work/ti:title", namespaces=CTS)
        lat = [t for t in titres if t.get("{http://www.w3.org/XML/1998/namespace}lang") == "lat"]
        t = (lat or titres)
        if t:
            meta["titre"] = espaces("".join(t[0].itertext()))
        for ed in w.xpath("//ti:edition|//ti:translation|//ti:commentary", namespaces=CTS):
            if ed.get("urn", "").endswith(stem):
                meta["edition"] = espaces(ed.xpath("string(ti:description)", namespaces=CTS))
                meta["libelle"] = espaces(ed.xpath("string(ti:label)", namespaces=CTS))
                meta["langue"] = ed.get("{http://www.w3.org/XML/1998/namespace}lang", "")
    return meta


MILESTONE = "{%s}milestone" % TEI


def est_repere(m):
    """Repères de pagination usuels : Casaubon (Athénée, Strabon), Stephanus (Platon, Plutarque)."""
    n = m.get("n")
    if not n:
        return False
    u = m.get("unit")
    if u in ("casaubonpage", "stephpage"):
        return True
    return u == "section" and re.match(r"^\d+[a-e]$", n) is not None


def texte_avant_repere(e):
    if (e.text or "").strip():
        return True
    for d in e.iterdescendants():
        if d.tag == MILESTONE and est_repere(d):
            return False
        if local(d.tag) not in IGNORES and (d.text or "").strip():
            return True
        if (d.tail or "").strip():
            return True
    return True


def calculer_reperes(doc, unites):
    """Pour chaque unité citable : repère(s) de page en vigueur (« 165b », « 165b–d »)."""
    pos = {e: i for i, e in enumerate(unites)}
    debut = [None] * len(unites)
    courant, vu = None, False
    for el in doc.iter():
        i = pos.get(el)
        if i is not None:
            debut[i] = courant
        if el.tag == MILESTONE and est_repere(el):
            courant, vu = el.get("n"), True
    if not vu:
        return [None] * len(unites)
    out = []
    for i, e in enumerate(unites):
        internes = [m.get("n") for m in e.iter(MILESTONE) if est_repere(m)]
        d = debut[i]
        if internes and (d is None or not texte_avant_repere(e)):
            d = internes[0]
        f = internes[-1] if internes else None
        if d and f and f != d:
            md, mf = re.match(r"^(\d+)([a-z]?)$", d), re.match(r"^(\d+)([a-z]?)$", f)
            if md and mf and md.group(1) == mf.group(1) and mf.group(2):
                out.append(f"{d}–{mf.group(2)}")
            else:
                out.append(f"{d}–{f}")
        else:
            out.append(d)
    return out


def unites_tei(doc):
    """Unités citables d'un document TEI CTS : [(ref tuple, élément)], niveaux."""
    crp = doc.xpath("//tei:refsDecl[@n='CTS']/tei:cRefPattern", namespaces=NS) or \
        doc.xpath("//tei:refsDecl/tei:cRefPattern", namespaces=NS)
    niveaux = []
    for c in crp:
        rp = c.get("replacementPattern") or ""
        k = len(re.findall(r"\$\d+", rp))
        if k:
            niveaux.append((k, c.get("n") or "", xpath_niveau(rp)))
    niveaux.sort()
    if not niveaux:
        # repli : divisions numérotées ou vers numérotés
        niveaux = [(1, "line", "/tei:TEI/tei:text/tei:body//tei:l[@n]")]
        if not doc.xpath(niveaux[0][2], namespaces=NS):
            niveaux = [(1, "section", "/tei:TEI/tei:text/tei:body/tei:div//tei:div[@n][not(.//tei:div[@n])]")]
    refs_prec = None
    elements = []
    for k, nom, xp in niveaux:
        els = doc.xpath(xp, namespaces=NS)
        refs = {}
        for e in els:
            n = espaces(e.get("n", ""))
            if refs_prec is None:
                refs[e] = (n,)
            else:
                p = e.getparent()
                while p is not None and p not in refs_prec:
                    p = p.getparent()
                refs[e] = (refs_prec[p] if p is not None else ("?",)) + (n,)
        refs_prec = refs
        elements = els
    # ne garder que les unités les plus internes (une unité qui en contient d'autres,
    # possible avec les motifs « // », n'est pas indexée deux fois)
    ens = set(elements)
    ancetres = set()
    for e in elements:
        p = e.getparent()
        while p is not None:
            if p in ens:
                ancetres.add(p)
            p = p.getparent()
    unites = [e for e in elements if e not in ancetres]
    return [(refs_prec[e], e) for e in unites], ".".join(n for _, n, _ in niveaux)


def passages_tei(doc):
    """[(ref, locuteur, texte, repère)] ; les vers partagés (part=I/M/F) sont réunis."""
    unites, niveaux = unites_tei(doc)
    reperes = calculer_reperes(doc, [e for _, e in unites])
    passages = []
    for (ref, e), rep in zip(unites, reperes):
        texte = texte_de(e)
        if not texte:
            continue
        loc = locuteur_de(e) if local(e.tag) == "l" else None
        dernier = ref[-1]
        if passages and local(e.tag) == "l" and e.get("part") in ("M", "F"):
            m = re.match(r"^(\d+)[a-z]$", dernier)
            pref, pdern = passages[-1][0][:-1], passages[-1][0][-1]
            if (m and pref == ref[:-1] and re.match(r"^%s[a-z]?$" % m.group(1), pdern)) or \
                    (pref == ref[:-1] and pdern == dernier):
                r0, l0, t0, rep0 = passages[-1]
                locs = l0 if loc in (None, l0) else f"{l0 or '?'} | {loc}"
                passages[-1] = (r0, locs, t0 + " | " + texte, rep0)
                continue
        passages.append((ref, loc, texte, rep))
    return passages, niveaux


def traiter_tei(args):
    fichier, collection = args
    stem = Path(fichier).name[:-4]
    parties = stem.split(".")
    res = {
        "collection": collection, "fichier": fichier,
        "urn": "urn:cts:greekLit:" + stem,
        "urn_oeuvre": "urn:cts:greekLit:" + ".".join(parties[:2]),
        "tlg_auteur": parties[0], "tlg_oeuvre": parties[1] if len(parties) > 1 else "",
        "passages": [], "erreur": None, "niveaux": "",
    }
    try:
        res.update(meta_oeuvre(fichier))
        doc = etree.parse(fichier, PARSEUR)
        passages, niveaux = passages_tei(doc)
        res["niveaux"] = niveaux
        res["passages"] = [(".".join(r), l, t, normaliser(t), None, rep) for r, l, t, rep in passages]
    except Exception as ex:  # un fichier défectueux ne doit pas arrêter l'indexation
        res["erreur"] = f"{type(ex).__name__}: {ex}"
    return res


def fichiers_tei(racine):
    out = []
    for f in sorted(glob.glob(str(racine) + "/*/*/*.xml")):
        nom = os.path.basename(f)
        if nom == "__cts__.xml":
            continue
        edition = nom[:-4].split(".")[-1]
        if "grc" not in edition:
            continue
        out.append(f)
    return out


# ---------------------------------------------------------------------------
# OCR archive.org
# ---------------------------------------------------------------------------

def lire_tsv(chemin):
    with open(chemin, encoding="utf-8") as f:
        lignes = [l for l in f if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(lignes, delimiter="\t"))


def lire_sources_ocr():
    return lire_tsv(ICI / "sources_ocr.tsv")


def options_de(src):
    o = {}
    for kv in (src.get("options") or "").split(";"):
        kv = kv.strip()
        if kv:
            k, _, v = kv.partition("=")
            o[k.strip()] = v.strip() or "1"
    return o


def nettoyer_ocr(t):
    t = nfc(t)
    t = re.sub(r"(\w)[-‐¬]\s*\n\s*(\w)", r"\1\2", t)  # césures de fin de ligne
    return espaces(t)


def numeros_pages(textes, fenetre=12, seuil=3):
    """Déduit la pagination imprimée à partir des titres courants de l'OCR.

    Pour chaque page du scan (rang i), on relève les nombres de la première et de la
    dernière ligne, puis on cherche, dans un voisinage de ± `fenetre` pages, la
    relation numéro = a·i + b (a = 1 : une page ; a = 2 : deux colonnes numérotées
    par page) la mieux attestée (au moins `seuil` fois). Renvoie pour chaque page
    (libellé, confirmé) : confirmé si le numéro calculé figure bien sur la page.
    Les planches hors texte et les changements de pagination sont ainsi absorbés.
    """
    nums = []
    for t in textes:
        lignes = [l for l in t.split("\n") if l.strip()]
        zone = " ".join(lignes[:1] + lignes[-1:]) if lignes else ""
        nums.append({int(x) for x in re.findall(r"(?<![\d,.])(\d{1,4})(?![\d,.])", zone) if 0 < int(x) < 3000})
    res = []
    for i in range(len(textes)):
        c = Counter()
        for j in range(max(0, i - fenetre), min(len(textes), i + fenetre + 1)):
            for n in nums[j]:
                c[(1, n - j)] += 1
                c[(2, n - 2 * j)] += 1
        lib, ok = "", False
        if c:
            (a, b), k = max(c.items(), key=lambda kv: (kv[1], -kv[0][0], -kv[0][1]))
            x = a * i + b
            if k >= seuil and x > 0:
                if a == 1:
                    lib, ok = f"p. {x}", x in nums[i]
                else:
                    lib, ok = f"col. {x}–{x + 1}", (x in nums[i] or x + 1 in nums[i])
        res.append((lib, ok))
    return res


def libelles_pages(d, ident, textes):
    """Pagination imprimée : celle d'archive.org si elle est sûre, sinon nos titres courants."""
    try:
        pn = json.load(open(d / f"{ident}_page_numbers.json", encoding="utf-8"))
        if pn.get("confidence", 0) >= 80:
            par = {p["leafNum"]: p.get("pageNumber") for p in pn.get("pages", []) if p.get("pageNumber")}
            if len(par) > 0.5 * len(textes):
                return [(f"p. {par[i]}", True) if par.get(i) else ("", False) for i in range(len(textes))]
    except Exception:
        pass
    return numeros_pages(textes)


def libelle_ref(lib, ok, i):
    return lib if (lib and ok) else (f"≈{lib}" if lib else f"[n{i}]")


def libelles_colonnes(lib, ok, i, nb):
    """Pour une page à deux colonnes numérotées « col. 805–806 » : (« col. 805 », « col. 806 »)."""
    m = re.match(r"col\. (\d+)–(\d+)$", lib or "")
    if m and nb == 2:
        pre = "" if ok else "≈"
        return [f"{pre}col. {m.group(1)}", f"{pre}col. {m.group(2)}"]
    r = libelle_ref(lib, ok, i)
    return [r] * nb


ENTETE = re.compile(r"\d{2,4}|—|---")
LEMME = re.compile(r"^[\W\d_]*?([^\W\d_][^\s\"'’:·;,.()\[\]]*)")


def articles_colonne(lignes, largeur, mode):
    """Découpe une colonne de lexique en articles d'après les retraits.

    mode « suspendu » : l'article commence à la marge, ses lignes de suite sont en retrait
    (Hésychius de Schmidt, Zonaras) ; « alinea » : la première ligne est en retrait
    (Souda de Bekker). Renvoie [(début_d_article, texte)]."""
    corps = list(lignes)
    if corps and ENTETE.search(corps[0][4]) and len(corps[0][4]) < 70:
        corps = corps[1:]  # titre courant
    if not corps:
        return []
    xs = sorted(l[0] for l in corps)
    marge = xs[max(0, int(len(xs) * 0.1) - 1)]
    tol = max(12, int(largeur * 0.008))
    arts = []
    for l in corps:
        a_marge = l[0] <= marge + tol
        debut = a_marge if mode == "suspendu" else (not a_marge and l[0] <= marge + 12 * tol)
        if debut or not arts:
            arts.append([debut, [l[4]]])
        else:
            arts[-1][1].append(l[4])
    return [(d, nettoyer_ocr("\n".join(ls))) for d, ls in arts]


def traiter_ocr(args):
    src, = args
    ident = src["identifiant"]
    opts = options_de(src)
    d = CORPUS / "ocr_archive" / ident
    res = {"collection": "ocr", "fichier": str(d), "urn": f"ia:{ident}",
           "urn_oeuvre": f"ia:{ident}", "tlg_auteur": "ocr", "tlg_oeuvre": ident,
           "auteur": src["sigle"], "titre": src["description"], "edition": src["description"],
           "abr_auteur": src["sigle"], "abr_titre": "",
           "categorie": src.get("categorie", ""), "niveaux": "page", "passages": [], "erreur": None,
           "source_url": f"https://archive.org/details/{ident}", "options": src.get("options") or ""}
    try:
        fcol = d / f"{ident}_colonnes.json.gz"
        pages_cols = None
        flocal = d / f"{ident}_ocr_local.json"
        if flocal.exists():
            info = json.load(open(flocal, encoding="utf-8"))
            res["fiabilite_detail"] = f"OCR local {info.get('moteur', 'Tesseract')} ({info.get('langues', '')})"
        else:
            res["fiabilite_detail"] = "OCR d'archive.org (Tesseract)"
        if opts.get("colonnes") == "2" and fcol.exists():
            data = json.load(gzip.open(fcol, "rt", encoding="utf-8"))
            pages_cols = data["pages"]
            bruts = ["\n".join("\n".join(l[4] for l in c) for c in p["colonnes"]) for p in pages_cols]
            res["fiabilite_detail"] = "; ".join(x for x in (res.get("fiabilite_detail"),
                                                             "colonnes rétablies d'après le hOCR") if x)
        else:
            t = gzip.open(d / f"{ident}_hocr_searchtext.txt.gz").read().decode("utf-8", "replace")
            pi = json.load(gzip.open(d / f"{ident}_hocr_pageindex.json.gz"))
            bruts = [t[ent[0]:ent[1]] for ent in pi]
        num = libelles_pages(d, ident, bruts)
        mode = opts.get("entrees")
        for i, brut in enumerate(bruts):
            lib, ok = num[i]
            if pages_cols is not None and pages_cols[i]["colonnes"]:
                cols = pages_cols[i]["colonnes"]
                libs = libelles_colonnes(lib, ok, i, len(cols))
                if mode in ("suspendu", "alinea"):
                    res["niveaux"] = "article"
                    for k, c in enumerate(cols):
                        for debut, texte in articles_colonne(c, pages_cols[i]["largeur"], mode):
                            if not texte:
                                continue
                            m = LEMME.match(texte)
                            lem = m.group(1) if (m and debut) else ""
                            ref = f"{libs[k]}, s.v. {lem}" if lem else f"{libs[k]} (suite)"
                            res["passages"].append((ref, None, texte, normaliser(texte), f"n{i}", None))
                    continue
                if len(set(libs)) > 1:
                    for k, c in enumerate(cols):
                        texte = nettoyer_ocr("\n".join(l[4] for l in c))
                        if texte:
                            res["passages"].append((libs[k], None, texte, normaliser(texte), f"n{i}", None))
                    continue
            texte = nettoyer_ocr(brut)
            if texte:
                res["passages"].append((libelle_ref(lib, ok, i), None, texte, normaliser(texte), f"n{i}", None))
    except Exception as ex:
        res["erreur"] = f"{type(ex).__name__}: {ex}"
    return res


# ---------------------------------------------------------------------------
# PDF du Drive (couche texte)
# ---------------------------------------------------------------------------

MAJ_LATIN_GREC = str.maketrans("ABEZHIKMNOPTYX", "ΑΒΕΖΗΙΚΜΝΟΡΤΥΧ")
MOT_MIXTE = re.compile(r"\w*[A-Z]\w*")


def grec_mixte(m):
    """Mot grec contenant des capitales latines (glyphes partagés des PDF d'éditeur :
    « Mεγαϱέων ») : les capitales latines deviennent grecques."""
    w = m.group(0)
    if re.search(r"[Ͱ-Ͽἀ-῿]", w):
        return w.translate(MAJ_LATIN_GREC)
    return w


def texte_pdf_page(page):
    """Texte d'une page PDF. Les espaces sont rétablis d'après l'écart entre caractères :
    dans les PDF d'éditeur, les mots grecs sont souvent collés (« τὸπϱὸτοῦἔϱγου »)."""
    try:
        lignes = []
        for b in page.get_text("rawdict").get("blocks", []):
            for l in b.get("lines", []):
                out, prec = [], None
                for s in l.get("spans", []):
                    taille = s.get("size", 10) or 10
                    for ch in s.get("chars", []):
                        c = ch.get("c", "")
                        x0, x1 = ch["bbox"][0], ch["bbox"][2]
                        if prec is not None and x0 - prec > 0.12 * taille and not c.isspace():
                            out.append(" ")
                        out.append(c)
                        prec = x1
                lignes.append("".join(out))
        t = "\n".join(lignes)
    except Exception:
        t = page.get_text("text")
    return MOT_MIXTE.sub(grec_mixte, t)


def part_grec(textes):
    mots = [w for t in textes for w in re.findall(r"[^\W\d_]{3,}", t)]
    if not mots:
        return 0.0
    return sum(1 for w in mots if re.search(r"[Ͱ-Ͽἀ-῿]", w)) / len(mots)


def traiter_drive(args):
    src, = args
    chemin = DRIVE / src["chemin"]
    res = {"collection": "drive", "fichier": str(chemin), "urn": "drive:" + src["chemin"],
           "urn_oeuvre": "drive:" + src["chemin"], "tlg_auteur": "drive", "tlg_oeuvre": src["sigle"],
           "auteur": src["sigle"], "titre": src["description"], "edition": src["chemin"],
           "abr_auteur": src["sigle"], "abr_titre": "", "categorie": src.get("categorie", ""),
           "niveaux": "page", "passages": [], "erreur": None, "source_url": "", "options": ""}
    try:
        if chemin.suffix.lower() == ".txt":
            t = open(chemin, encoding="utf-8", errors="replace").read()
            blocs, cour = [], []
            for par in re.split(r"\n\s*\n", t):
                cour.append(par)
                if sum(len(x) for x in cour) > 2500:
                    blocs.append("\n".join(cour))
                    cour = []
            if cour:
                blocs.append("\n".join(cour))
            res["niveaux"] = "bloc"
            for i, b in enumerate(blocs):
                tt = nettoyer_ocr(b)
                if tt:
                    res["passages"].append((f"§ {i + 1}", None, tt, normaliser(tt), f"b{i + 1}", None))
            return res
        import pymupdf
        doc = pymupdf.open(str(chemin))
        textes = [texte_pdf_page(p) for p in doc]
        if sum(len(x.strip()) for x in textes) < 100 * max(1, len(textes)) * 0.2:
            res["erreur"] = "pas de couche texte exploitable"
            return res
        if src.get("categorie") in ("lexiques", "fragments", "scholies") and part_grec(textes) < 0.05:
            res["erreur"] = "couche texte inutilisable (grec illisible : police non Unicode ou OCR latin)"
            return res
        num = numeros_pages(textes)
        for i, t in enumerate(textes):
            tt = nettoyer_ocr(t)
            if not tt:
                continue
            lib, ok = num[i]
            ref = f"{lib} [PDF p. {i + 1}]" if (lib and ok) else f"PDF p. {i + 1}"
            res["passages"].append((ref, None, tt, normaliser(tt), f"pdf{i + 1}", None))
    except Exception as ex:
        res["erreur"] = f"{type(ex).__name__}: {ex}"
    return res


# ---------------------------------------------------------------------------
# LSJ (TEI P4 Perseus, grec en Beta Code)
# ---------------------------------------------------------------------------

def extraire_lsj(el, out, grec=False):
    tag = el.tag if isinstance(el.tag, str) else None
    if tag is None:
        return
    lang = el.get("lang")
    if lang is not None:
        grec = lang == "greek"
    if el.text:
        out.append(beta_vers_unicode(el.text) if grec else el.text)
    for c in el:
        extraire_lsj(c, out, grec)
        if c.tail:
            out.append(beta_vers_unicode(c.tail) if grec else c.tail)


def traiter_lsj(args):
    fichier, = args
    res = {"passages": [], "erreur": None}
    try:
        doc = etree.parse(fichier, PARSEUR_SOUPLE)
        for e in doc.iter("entryFree"):
            cle = beta_vers_unicode(e.get("key", ""))
            out = []
            extraire_lsj(e, out)
            texte = espaces(nfc("".join(out)))
            res["passages"].append((cle, None, texte, normaliser(texte), e.get("id"), None))
    except Exception as ex:
        res["erreur"] = f"{type(ex).__name__}: {ex}"
    return res


# ---------------------------------------------------------------------------
# DCLP (papyrus littéraires, EpiDoc)
# ---------------------------------------------------------------------------

def traiter_dclp(args):
    fichier, = args
    res = {"meta": None, "oeuvre": None, "erreur": None}
    try:
        doc = etree.parse(fichier, PARSEUR_SOUPLE)
        tm = doc.xpath("string(//tei:publicationStmt/tei:idno[@type='TM'])", namespaces=NS).strip() \
            or Path(fichier).stem
        titre = espaces(doc.xpath("string(//tei:titleStmt/tei:title)", namespaces=NS))
        pubs = [espaces("".join(t.itertext())) for t in doc.xpath("//tei:body/tei:head//tei:title", namespaces=NS)]
        anc = doc.xpath("//tei:div[@subtype='ancientEdition']//tei:bibl", namespaces=NS)
        auteurs, oeuvres, passages_anc = [], [], []
        for b in anc:
            for a in b.xpath(".//tei:author", namespaces=NS):
                auteurs.append(espaces("".join(a.itertext())))
            for t in b.xpath(".//tei:title", namespaces=NS):
                oeuvres.append(espaces("".join(t.itertext())))
            for s in b.xpath(".//tei:biblScope", namespaces=NS):
                v = espaces("".join(s.itertext()))
                if v:
                    passages_anc.append(v)
        date = espaces(doc.xpath("string(//tei:origDate)", namespaces=NS))
        lieu = espaces(doc.xpath("string(//tei:origPlace)", namespaces=NS))
        res["meta"] = (tm, titre, " ; ".join(pubs), " ; ".join(dict.fromkeys(auteurs)),
                       " ; ".join(dict.fromkeys(oeuvres)), " ; ".join(passages_anc), date, lieu)
        eds = doc.xpath("//tei:div[@type='edition']", namespaces=NS)
        passages = []
        for ed in eds:
            parts = ed.xpath(".//tei:div[@type='textpart'][not(.//tei:div[@type='textpart'])]", namespaces=NS) or [ed]
            for p in parts:
                if not p.xpath(".//tei:lb", namespaces=NS):
                    continue
                chemin = []
                q = p
                while q is not None and local(q.tag) == "div" and q.get("type") == "textpart":
                    chemin.append(((q.get("subtype") or "") + " " + (q.get("n") or "")).strip())
                    q = q.getparent()
                ref = ", ".join(reversed(chemin)) or "texte"
                texte = texte_de(p, papyrus=True).strip(" |")
                if texte and re.search(r"[Ͱ-Ͽἀ-῿]", texte):
                    passages.append((ref, None, texte, normaliser(texte), None, None))
        if passages:
            res["oeuvre"] = passages
    except Exception as ex:
        res["erreur"] = f"{type(ex).__name__}: {ex}"
    return res


# ---------------------------------------------------------------------------
# Diorisis : table des formes (forme normalisée → lemme)
# ---------------------------------------------------------------------------

def traiter_diorisis(args):
    fichier, = args
    c = Counter()
    try:
        for _, w in etree.iterparse(fichier, tag="word", huge_tree=True, recover=True):
            forme = w.get("form")
            lem = w.find("lemma")
            if forme and lem is not None and lem.get("entry"):
                c[(normaliser(beta_vers_unicode(forme)), nfc(lem.get("entry")))] += 1
            w.clear()
            par = w.getparent()
            if par is not None:
                while w.getprevious() is not None:
                    del par[0]
    except Exception as ex:
        return {"compte": c, "erreur": f"{type(ex).__name__}: {ex}"}
    return {"compte": c, "erreur": None}


# ---------------------------------------------------------------------------
# Abréviations (« Eur. Hel. 255 »)
# ---------------------------------------------------------------------------

def lire_abreviations():
    auteurs, oeuvres = {}, {}
    with open(ICI / "abreviations.tsv", encoding="utf-8") as f:
        for l in f:
            if not l.strip() or l.startswith("#"):
                continue
            cols = l.rstrip("\n").split("\t")
            if len(cols) < 2:
                continue
            cle, abr = cols[0].strip(), cols[1].strip()
            (oeuvres if "." in cle else auteurs)[cle] = abr
    return auteurs, oeuvres


# ---------------------------------------------------------------------------
# Base SQLite
# ---------------------------------------------------------------------------

SCHEMA = """
PRAGMA page_size = 8192;
CREATE TABLE meta(cle TEXT PRIMARY KEY, valeur TEXT);
CREATE TABLE collections(nom TEXT PRIMARY KEY, description TEXT, licence TEXT, url TEXT, fiabilite TEXT);
CREATE TABLE oeuvres(
  id INTEGER PRIMARY KEY,
  collection TEXT, urn TEXT UNIQUE, urn_oeuvre TEXT,
  tlg_auteur TEXT, tlg_oeuvre TEXT,
  auteur TEXT, titre TEXT, abr_auteur TEXT, abr_titre TEXT,
  edition TEXT, categorie TEXT, fichier TEXT, niveaux TEXT,
  nb_passages INTEGER, nb_mots INTEGER, prioritaire INTEGER DEFAULT 1,
  fiabilite TEXT, score_ocr REAL, source_url TEXT, options TEXT
);
CREATE TABLE passages(
  id INTEGER PRIMARY KEY,
  oeuvre_id INTEGER, ordre INTEGER, ref TEXT, locuteur TEXT,
  texte TEXT, norm TEXT, cible TEXT, repere TEXT
);
CREATE TABLE formes(forme TEXT, lemme TEXT, lemme_norm TEXT, n INTEGER);
CREATE TABLE papyrus(tm TEXT PRIMARY KEY, titre TEXT, publications TEXT, auteurs TEXT,
                     oeuvres TEXT, passages TEXT, date TEXT, lieu TEXT, a_texte INTEGER);
CREATE VIRTUAL TABLE passages_fts USING fts5(
  norm, content='passages', content_rowid='id',
  tokenize="unicode61 remove_diacritics 0", prefix='2 3');
CREATE VIRTUAL TABLE fenetres_fts USING fts5(
  norm, content='', tokenize="unicode61 remove_diacritics 0", prefix='2 3');
CREATE VIRTUAL TABLE souple_fts USING fts5(
  norm, content='', tokenize="unicode61 remove_diacritics 0", prefix='2 3');
"""

INDEX_FINAUX = """
CREATE INDEX passages_oeuvre ON passages(oeuvre_id, ordre);
CREATE INDEX oeuvres_urn_oeuvre ON oeuvres(urn_oeuvre);
CREATE INDEX formes_forme ON formes(forme);
CREATE INDEX formes_lemme ON formes(lemme_norm);
"""

ORATEURS = {"tlg0014", "tlg0540", "tlg0026", "tlg0027", "tlg0028", "tlg0017", "tlg0030"}
GREC = re.compile(r"[α-ω]")


class Ecrivain:
    def __init__(self, con):
        self.con = con
        self.id_passage = 0
        self.nb = Counter()
        self.mots = Counter()
        self.urns = Counter()

    def oeuvre(self, r, passages, abrs):
        """Insère une œuvre (dict r) et ses passages [(ref, loc, texte, norm, cible?, repère?)]."""
        if not passages:
            return
        ab_aut, ab_oeu = abrs
        cle_oeuvre = f"{r['tlg_auteur']}.{r['tlg_oeuvre']}"
        abr_auteur = r.get("abr_auteur") or ab_aut.get(r["tlg_auteur"], r["auteur"])
        abr_titre = r.get("abr_titre")
        if abr_titre is None:
            abr_titre = ab_oeu.get(cle_oeuvre)
        if abr_titre is None and r["tlg_auteur"] in ORATEURS and re.match(r"tlg\d+$", r["tlg_oeuvre"]):
            abr_titre = str(int(r["tlg_oeuvre"][3:]))
        if abr_titre is None:
            abr_titre = r.get("titre", "")
        nb_mots = sum(len(p[3].split()) for p in passages)
        self.urns[r["urn"]] += 1
        if self.urns[r["urn"]] > 1:  # p. ex. deux fichiers DCLP pour un même numéro TM
            r = dict(r, urn=f"{r['urn']}~{self.urns[r['urn']]}")
        fiab = COLLECTIONS[r["collection"]][3]
        if r.get("fiabilite_detail"):
            fiab += f" ; {r['fiabilite_detail']}"
        cur = self.con.execute(
            "INSERT INTO oeuvres(collection, urn, urn_oeuvre, tlg_auteur, tlg_oeuvre, auteur, titre,"
            " abr_auteur, abr_titre, edition, categorie, fichier, niveaux, nb_passages, nb_mots,"
            " fiabilite, source_url, options)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (r["collection"], r["urn"], r["urn_oeuvre"], r["tlg_auteur"], r["tlg_oeuvre"],
             r["auteur"], r.get("titre", ""), abr_auteur, abr_titre, r.get("edition", ""),
             r.get("categorie", ""), os.path.relpath(r["fichier"], RACINE) if r.get("fichier") else "",
             r.get("niveaux", ""), len(passages), nb_mots, fiab, r.get("source_url", ""),
             r.get("options", "")))
        oid = cur.lastrowid
        lignes, fen, souple = [], [], []
        premier = self.id_passage + 1
        plier = r["collection"] in ("ocr", "drive")
        for i, p in enumerate(passages):
            self.id_passage += 1
            ref, loc, texte, norm = p[0], p[1], p[2], p[3]
            cible = p[4] if len(p) > 4 else None
            repere = p[5] if len(p) > 5 else None
            lignes.append((self.id_passage, oid, i, ref, loc, texte, norm, cible, repere))
            if plier:
                souple.append((self.id_passage, plier_ocr(norm)))
        for i in range(len(passages) - 1):
            a = passages[i][3].split()[-FENETRE:]
            b = passages[i + 1][3].split()[:FENETRE]
            if a and b:
                fen.append((premier + i, " ".join(a + b)))
        self.con.executemany("INSERT INTO passages VALUES (?,?,?,?,?,?,?,?,?)", lignes)
        self.con.executemany("INSERT INTO fenetres_fts(rowid, norm) VALUES (?,?)", fen)
        if souple:
            self.con.executemany("INSERT INTO souple_fts(rowid, norm) VALUES (?,?)", souple)
        self.nb[r["collection"]] += len(passages)
        self.mots[r["collection"]] += nb_mots


def priorites(con):
    """Une seule édition « prioritaire » par œuvre (les autres restent interrogeables)."""
    rang_coll = {"perseus": 0, "first1k": 1}
    groupes = defaultdict(list)
    for oid, urn, uo, coll in con.execute("SELECT id, urn, urn_oeuvre, collection FROM oeuvres"):
        groupes[uo].append((oid, urn, coll))
    for uo, eds in groupes.items():
        if len(eds) < 2:
            continue

        def cle(e):
            ed = e[1].rsplit(".", 1)[-1]
            m = re.search(r"(\d+)$", ed)
            return (rang_coll.get(e[2], 9), -(int(m.group(1)) if m else 0))
        eds.sort(key=cle)
        for oid, _, _ in eds[1:]:
            con.execute("UPDATE oeuvres SET prioritaire = 0 WHERE id = ?", (oid,))


def scores_ocr(con):
    """Taux de mots grecs (4 lettres et plus) attestés dans les textes TEI, par œuvre OCR/PDF."""
    lex = set()
    for (norm,) in con.execute("SELECT p.norm FROM passages p JOIN oeuvres o ON o.id = p.oeuvre_id "
                               "WHERE o.collection IN ('perseus', 'first1k')"):
        lex.update(norm.split())
    oids = [r[0] for r in con.execute("SELECT id FROM oeuvres WHERE collection IN ('ocr', 'drive')")]
    for oid in oids:
        n = k = 0
        for (norm,) in con.execute("SELECT norm FROM passages WHERE oeuvre_id = ?", (oid,)):
            for w in norm.split():
                if len(w) >= 4 and GREC.match(w):
                    n += 1
                    k += w in lex
        con.execute("UPDATE oeuvres SET score_ocr = ? WHERE id = ?", (round(k / n, 3) if n else None, oid))
    return len(lex)


def versions_depots():
    out = {}
    for d in ("canonical-greekLit", "First1KGreek", "lexica", "idp.data"):
        try:
            out[d] = subprocess.run(["git", "-C", str(CORPUS / d), "log", "-1", "--format=%H %cs"],
                                    capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception:
            pass
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", nargs="*",
                    default=["perseus", "first1k", "ocr", "lsj", "dclp", "drive", "diorisis"])
    ap.add_argument("--processus", type=int, default=os.cpu_count() or 8)
    ap.add_argument("--base", default=str(BASE))
    a = ap.parse_args()

    t0 = time.time()
    base = Path(a.base)
    tmp = base.with_suffix(".sqlite.tmp")
    if tmp.exists():
        tmp.unlink()
    con = sqlite3.connect(tmp)
    con.executescript(SCHEMA)
    con.executescript("PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; "
                      "PRAGMA cache_size=-1000000; PRAGMA temp_store=MEMORY;")
    for nom, (desc, lic, url, fiab) in COLLECTIONS.items():
        con.execute("INSERT INTO collections VALUES (?,?,?,?,?)", (nom, desc, lic, url, fiab))
    abrs = lire_abreviations()
    ecr = Ecrivain(con)
    erreurs = []
    absents = []
    pool = mp.Pool(a.processus)

    racines = {"perseus": CORPUS / "canonical-greekLit" / "data",
               "first1k": CORPUS / "First1KGreek" / "data"}
    for coll in ("perseus", "first1k"):
        if coll not in a.sources or not racines[coll].exists():
            continue
        fichiers = fichiers_tei(racines[coll])
        print(f"[{coll}] {len(fichiers)} fichiers TEI grecs…", flush=True)
        # les plus gros fichiers d'abord : meilleure répartition entre processus
        fichiers.sort(key=lambda f: -os.path.getsize(f))
        for k, r in enumerate(pool.imap_unordered(traiter_tei, [(f, coll) for f in fichiers], chunksize=1), 1):
            if r["erreur"]:
                erreurs.append((r["fichier"], r["erreur"]))
            ecr.oeuvre(r, r["passages"], abrs)
            if k % 200 == 0:
                print(f"  {k}/{len(fichiers)}  {ecr.nb[coll]} passages  ({time.time() - t0:.0f} s)", flush=True)
        con.commit()

    if "ocr" in a.sources and (CORPUS / "ocr_archive").exists():
        srcs = [s for s in lire_sources_ocr() if (CORPUS / "ocr_archive" / s["identifiant"]).exists()]
        print(f"[ocr] {len(srcs)} ouvrages…", flush=True)
        for r in pool.imap_unordered(traiter_ocr, [(s,) for s in srcs]):
            if r["erreur"]:
                erreurs.append((r["fichier"], r["erreur"]))
            ecr.oeuvre(r, r["passages"], abrs)
        con.commit()

    fdrive = CORPUS / "sources_drive.tsv"
    if "drive" in a.sources and fdrive.exists():
        srcs = lire_tsv(fdrive)
        presents = [s for s in srcs if (DRIVE / s["chemin"]).exists()]
        absents = [s["sigle"] for s in srcs if not (DRIVE / s["chemin"]).exists()]
        print(f"[drive] {len(presents)} fichiers présents sur {len(srcs)} retenus…", flush=True)
        for r in pool.imap_unordered(traiter_drive, [(s,) for s in presents]):
            if r["erreur"]:
                erreurs.append((r["fichier"], r["erreur"]))
            ecr.oeuvre(r, r["passages"], abrs)
        con.commit()

    lsj = sorted(glob.glob(str(CORPUS / "lexica/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng*.xml")),
                 key=lambda f: int(re.search(r"eng(\d+)\.xml$", f).group(1)))
    if "lsj" in a.sources and lsj:
        print(f"[lsj] {len(lsj)} fichiers…", flush=True)
        entrees = []
        for r in pool.imap(traiter_lsj, [(f,) for f in lsj]):
            if r["erreur"]:
                erreurs.append(("lsj", r["erreur"]))
            entrees.extend(r["passages"])
        ecr.oeuvre({"collection": "lsj", "urn": "lsj", "urn_oeuvre": "lsj", "tlg_auteur": "lsj",
                    "tlg_oeuvre": "lsj", "auteur": "LSJ", "titre": "Greek-English Lexicon",
                    "abr_auteur": "LSJ", "abr_titre": "",
                    "edition": "Liddell–Scott–Jones, A Greek-English Lexicon, 9e éd. (1940), numérisation Perseus",
                    "fichier": str(CORPUS / "lexica"), "niveaux": "entrée"}, entrees, abrs)
        con.commit()

    dclp = sorted(glob.glob(str(CORPUS / "idp.data/DCLP/*/*.xml")))
    if "dclp" in a.sources and dclp:
        print(f"[dclp] {len(dclp)} fichiers…", flush=True)
        for r in pool.imap_unordered(traiter_dclp, [(f,) for f in dclp], chunksize=20):
            if r["erreur"]:
                erreurs.append(("dclp", r["erreur"]))
                continue
            if r["meta"]:
                con.execute("INSERT OR REPLACE INTO papyrus VALUES (?,?,?,?,?,?,?,?,?)",
                            r["meta"] + (1 if r["oeuvre"] else 0,))
            if r["oeuvre"]:
                tm, titre, pubs, auteurs, oeuvres = r["meta"][:5]
                lib = pubs.split(" ; ")[0] if pubs else f"TM {tm}"
                ecr.oeuvre({"collection": "dclp", "urn": f"dclp:{tm}", "urn_oeuvre": f"dclp:{tm}",
                            "tlg_auteur": "dclp", "tlg_oeuvre": tm, "auteur": "Pap.",
                            "titre": titre, "abr_auteur": lib, "abr_titre": "",
                            "edition": f"TM {tm} — {titre} — {pubs}",
                            "categorie": auteurs, "fichier": None, "niveaux": "partie",
                            "source_url": f"https://papyri.info/dclp/{tm}"},
                           r["oeuvre"], abrs)
        con.commit()

    dio = sorted(glob.glob(str(CORPUS / "diorisis/x/*.xml")))
    if "diorisis" in a.sources and dio:
        print(f"[diorisis] {len(dio)} fichiers (table des formes)…", flush=True)
        total = Counter()
        for r in pool.imap_unordered(traiter_diorisis, [(f,) for f in dio], chunksize=1):
            if r["erreur"]:
                erreurs.append(("diorisis", r["erreur"]))
            total.update(r["compte"])
        con.executemany("INSERT INTO formes VALUES (?,?,?,?)",
                        ((f, l, normaliser(l), n) for (f, l), n in total.items() if f))
        con.commit()
    pool.close()

    print(f"Taux de reconnaissance de l'OCR… ({time.time() - t0:.0f} s)", flush=True)
    nb_lex = scores_ocr(con)
    print(f"Index FTS5… ({time.time() - t0:.0f} s)", flush=True)
    con.execute("INSERT INTO passages_fts(passages_fts) VALUES('rebuild')")
    con.execute("INSERT INTO passages_fts(passages_fts) VALUES('optimize')")
    con.execute("INSERT INTO fenetres_fts(fenetres_fts) VALUES('optimize')")
    con.execute("INSERT INTO souple_fts(souple_fts) VALUES('optimize')")
    con.executescript(INDEX_FINAUX)
    priorites(con)
    stats = {
        "date": time.strftime("%Y-%m-%d %H:%M"),
        "oeuvres": con.execute("SELECT count(*) FROM oeuvres").fetchone()[0],
        "passages": con.execute("SELECT count(*) FROM passages").fetchone()[0],
        "mots": con.execute("SELECT sum(nb_mots) FROM oeuvres").fetchone()[0],
        "par_collection": {c: {"oeuvres": con.execute("SELECT count(*) FROM oeuvres WHERE collection=?",
                                                      (c,)).fetchone()[0],
                               "passages": ecr.nb[c], "mots": ecr.mots[c]} for c in ecr.nb},
        "formes_tei": nb_lex,
        "erreurs": len(erreurs),
        "drive_absents": absents,
        "depots": versions_depots(),
    }
    con.execute("INSERT INTO meta VALUES ('stats', ?)", (json.dumps(stats, ensure_ascii=False),))
    con.execute("INSERT INTO meta VALUES ('erreurs', ?)", (json.dumps(erreurs, ensure_ascii=False),))
    con.commit()
    con.execute("ANALYZE")
    con.close()
    os.replace(tmp, base)
    print(json.dumps(stats, ensure_ascii=False, indent=1))
    for f, e in erreurs[:40]:
        print("ERREUR", f, e, file=sys.stderr)
    print(f"Terminé en {time.time() - t0:.0f} s → {base} ({base.stat().st_size / 1e6:.0f} Mo)")


if __name__ == "__main__":
    main()
