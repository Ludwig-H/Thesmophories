#!/usr/bin/env python3
"""Rétablit l'ordre de lecture des pages à plusieurs colonnes dans l'OCR d'archive.org.

Sur les pages à deux colonnes serrées (Hésychius de Schmidt, Souda de Bekker, Zonaras…),
l'analyse de mise en page de Tesseract fusionne souvent les lignes des deux colonnes :
le texte « à plat » (_hocr_searchtext) entrelace alors les gloses. Ce script relit le
fichier hOCR (_hocr.html : un cadre par mot), détecte la gouttière de chaque page
d'après la position des mots, répartit les mots entre colonnes et reconstitue les lignes
de chaque colonne. Aucun mot n'est réocérisé : seul l'ordre est corrigé.

Sortie : .sources/corpus/ocr_archive/<id>/<id>_colonnes.json.gz
  {"identifiant", "ocr_system", "pages": [{"n": rang, "largeur", "hauteur",
    "gouttiere": [x0, x1] | null,
    "colonnes": [[[x0, y0, x1, y1, "texte de la ligne"], ...], ...]}]}

  python3 outils/corpus/hocr_colonnes.py bub_gb_R-zVabafOucC suidaelexiconexr00suid
  python3 outils/corpus/hocr_colonnes.py --tous      # toutes les sources marquées colonnes=2
"""

import argparse
import csv
import gzip
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from lxml import etree

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
OCR = RACINE / ".sources" / "corpus" / "ocr_archive"

BBOX = re.compile(r"bbox (\d+) (\d+) (\d+) (\d+)")
CONF = re.compile(r"x_wconf (\d+)")


def telecharger_hocr(ident):
    d = OCR / ident
    d.mkdir(parents=True, exist_ok=True)
    cible = d / f"{ident}_hocr.html"
    if cible.exists() and cible.stat().st_size > 0:
        return cible
    # le nom réel du fichier ne reprend pas toujours l'identifiant (…_201708)
    req = urllib.request.Request(f"https://archive.org/metadata/{ident}",
                                 headers={"User-Agent": "thesmophories-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        noms = [f["name"] for f in json.load(r).get("files", []) if f["name"].endswith("_hocr.html")]
    if not noms:
        raise FileNotFoundError(f"{ident} : pas de fichier _hocr.html")
    noms.sort(key=lambda n: (not n.startswith(ident), len(n)))
    url = f"https://archive.org/download/{ident}/{urllib.parse.quote(noms[0])}"
    tmp = cible.with_suffix(".html.part")
    req = urllib.request.Request(url, headers={"User-Agent": "thesmophories-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=600) as r, open(tmp, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    tmp.rename(cible)
    return cible


def mots_de_page(page):
    """[(x0, y0, x1, y1, texte, conf, id_ligne)] pour une page hOCR."""
    out = []
    for ligne in page.iter("{*}span"):
        if ligne.get("class") != "ocr_line":
            continue
        lid = ligne.get("id")
        for w in ligne:
            if w.get("class") != "ocrx_word":
                continue
            t = "".join(w.itertext()).strip()
            if not t:
                continue
            m = BBOX.search(w.get("title", ""))
            if not m:
                continue
            c = CONF.search(w.get("title", ""))
            x0, y0, x1, y1 = map(int, m.groups())
            out.append((x0, y0, x1, y1, t, int(c.group(1)) if c else 0, lid))
    return out


def gouttiere(mots, largeur, hauteur):
    """Cherche une gouttière verticale au milieu du bloc de texte. Renvoie (g0, g1) ou None."""
    corps = [m for m in mots if (m[3] - m[1]) < hauteur * 0.05 and len(m[4]) > 0]
    if len(corps) < 40:
        return None
    xmin = min(m[0] for m in corps)
    xmax = max(m[2] for m in corps)
    if xmax - xmin < largeur * 0.4:
        return None
    pas = 10
    nb = (xmax - xmin) // pas + 1
    couv = [0] * nb
    for m in corps:
        for b in range((m[0] - xmin) // pas, (m[2] - xmin) // pas + 1):
            couv[b] += 1
    # lissage (moyenne glissante sur 3 cases)
    lisse = [sum(couv[max(0, b - 1):b + 2]) / len(couv[max(0, b - 1):b + 2]) for b in range(nb)]
    # zone de recherche : partie centrale du bloc. Des mots fusionnés par l'OCR peuvent
    # enjamber la gouttière : on cherche donc un creux marqué, pas une colonne vide.
    a, z = int(nb * 0.30), int(nb * 0.70)
    zone = sorted(lisse[a:z + 1])
    if not zone:
        return None
    cmed = zone[len(zone) // 2]
    bmin = min(range(a, z + 1), key=lambda b: lisse[b])
    cmin = lisse[bmin]
    if cmed <= 0 or cmin > 0.65 * cmed:
        return None
    seuil = cmin + 0.25 * (cmed - cmin)
    d0 = bmin
    while d0 - 1 >= a and lisse[d0 - 1] <= seuil:
        d0 -= 1
    d1 = bmin
    while d1 + 1 <= z and lisse[d1 + 1] <= seuil:
        d1 += 1
    if (d1 - d0 + 1) * pas < 20:
        return None
    g0, g1 = xmin + d0 * pas, xmin + (d1 + 1) * pas
    gauche = sum(1 for m in corps if (m[0] + m[2]) / 2 < g0)
    droite = sum(1 for m in corps if (m[0] + m[2]) / 2 > g1)
    if min(gauche, droite) < 0.2 * len(corps):
        return None
    return (g0, g1)


def lignes_colonne(mots):
    """Regroupe les mots d'une colonne en lignes (par ligne hOCR, puis par position)."""
    groupes = {}
    for m in mots:
        groupes.setdefault(m[6], []).append(m)
    lignes = []
    for ms in groupes.values():
        ms.sort(key=lambda m: m[0])
        x0 = min(m[0] for m in ms)
        y0 = min(m[1] for m in ms)
        x1 = max(m[2] for m in ms)
        y1 = max(m[3] for m in ms)
        lignes.append([x0, y0, x1, y1, " ".join(m[4] for m in ms)])
    # ordre de lecture : par le milieu vertical de la ligne
    lignes.sort(key=lambda l: ((l[1] + l[3]) / 2, l[0]))
    return lignes


def traiter(ident, forcer=False):
    d = OCR / ident
    sortie = d / f"{ident}_colonnes.json.gz"
    if sortie.exists() and not forcer:
        print(f"{ident} : déjà traité")
        return sortie
    chemin = telecharger_hocr(ident)
    systeme = ""
    pages = []
    n = 0
    for _, el in etree.iterparse(str(chemin), events=("end",), tag="{*}div", huge_tree=True, recover=True):
        if el.get("class") == "ocr_meta":
            continue
        if el.get("class") != "ocr_page":
            continue
        m = BBOX.search(el.get("title", ""))
        largeur, hauteur = (int(m.group(3)), int(m.group(4))) if m else (0, 0)
        mots = mots_de_page(el)
        g = gouttiere(mots, largeur, hauteur) if mots else None
        if g:
            gauche = [w for w in mots if (w[0] + w[2]) / 2 < (g[0] + g[1]) / 2]
            droite = [w for w in mots if (w[0] + w[2]) / 2 >= (g[0] + g[1]) / 2]
            # les lignes qui chevauchent la gouttière (titre courant) restent entières en tête
            cols = [lignes_colonne(gauche), lignes_colonne(droite)]
        else:
            cols = [lignes_colonne(mots)] if mots else []
        pages.append({"n": n, "largeur": largeur, "hauteur": hauteur,
                      "gouttiere": list(g) if g else None, "colonnes": cols})
        n += 1
        el.clear()
        while el.getprevious() is not None:
            del el.getparent()[0]
    with open(chemin, "rb") as f:
        tete = f.read(4000).decode("utf-8", "replace")
    m = re.search(r'name="ocr-system" content="([^"]+)"', tete)
    systeme = m.group(1) if m else ""
    with gzip.open(sortie, "wt", encoding="utf-8") as f:
        json.dump({"identifiant": ident, "ocr_system": systeme, "pages": pages}, f, ensure_ascii=False)
    deux = sum(1 for p in pages if p["gouttiere"])
    print(f"{ident} : {len(pages)} pages, {deux} à deux colonnes → {sortie.name}")
    return sortie


def sources_colonnes():
    with open(ICI / "sources_ocr.tsv", encoding="utf-8") as f:
        lignes = [l for l in f if l.strip() and not l.startswith("#")]
    out = []
    for s in csv.DictReader(lignes, delimiter="\t"):
        if "colonnes=2" in (s.get("options") or ""):
            out.append(s["identifiant"])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("identifiants", nargs="*")
    ap.add_argument("--tous", action="store_true", help="toutes les sources marquées colonnes=2")
    ap.add_argument("--forcer", action="store_true")
    a = ap.parse_args()
    ids = a.identifiants + (sources_colonnes() if a.tous else [])
    if not ids:
        sys.exit("aucun identifiant")
    for i in dict.fromkeys(ids):
        try:
            traiter(i, a.forcer)
        except Exception as e:
            print(f"{i} : ÉCHEC ({type(e).__name__}: {e})", file=sys.stderr)


if __name__ == "__main__":
    main()
