#!/usr/bin/env python3
"""Souda d'Adler (Teubner, 1928–1938, 5 t.) : pages de l'OCR d'archive.org, prêtes pour l'index.

Les volumes (item archive.org « adler-a.-suidae-lexicon-3-. », cinq PDF avec leur hOCR) sont dans
.sources/web/testimonia/adler/ (domaine public ; MD5 contrôlés : md5_attendus.txt). L'OCR
d'archive.org (Tesseract, grec polytonique) confond surtout le sigma lunaire (c, ε) et lit en
lettres latines quelques mots grecs : l'index « souple » y remédie en partie.

Pagination : un feuillet par page aux t. I, II, IV et V (page = feuillet − décalage, décalage
contrôlé sur les pages numérotées d'archive.org) ; deux pages par feuillet au t. III (doubles pages,
séparées d'après la position des mots : hocr_colonnes.gouttiere, à défaut le milieu de l'image).

Sortie : .sources/corpus/adler/pages.jsonl.gz, une ligne par page imprimée :
  {"tome": 1, "feuillet": 200, "page": 171, "texte": "…"}
Les articles ne sont pas découpés : l'OCR lit mal les numéros (collés aux numéros de ligne), et le
numéro d'un article se lit sur la page.

  python3 outils/corpus/adler.py        # puis outils/corpus/indexer.py
"""

import glob
import gzip
import json
import sys
from pathlib import Path

from lxml import etree

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
sys.path.insert(0, str(ICI))
from hocr_colonnes import BBOX, gouttiere, lignes_colonne, mots_de_page  # noqa: E402

SOURCE = RACINE / ".sources" / "web" / "testimonia" / "adler"
SORTIE = RACINE / ".sources" / "corpus" / "adler" / "pages.jsonl.gz"
ITEM = "adler-a.-suidae-lexicon-3-."
DECALAGE = {1: 29, 2: 13, 4: 15, 5: 5}   # page = feuillet − décalage (t. III : deux pages par feuillet)


def fichier(vol, suffixe):
    f = glob.glob(glob.escape(str(SOURCE)) + f"/Adler A., Suidae Lexicon {vol} *{suffixe}")
    return Path(f[0]) if f else None


def sous_prefixe(vol):
    """Nom du livre dans l'item archive.org (lecteur : /details/<item>/<livre>/page/n12)."""
    return fichier(vol, "_page_numbers.json").name[:-len("_page_numbers.json")]


def texte_lignes(lignes):
    return "\n".join(l[4] for l in lignes)


def pages_hocr(vol):
    """Itère sur (feuillet, numéro de page, lignes) d'après le hOCR du volume."""
    leaf = 0
    for _, el in etree.iterparse(str(fichier(vol, "_hocr.html")), events=("end",), tag="{*}div",
                                 huge_tree=True, recover=True):
        if el.get("class") != "ocr_page":
            continue
        m = BBOX.search(el.get("title", ""))
        largeur, hauteur = (int(m.group(3)), int(m.group(4))) if m else (0, 0)
        mots = mots_de_page(el)
        if vol == 3:
            g = gouttiere(mots, largeur, hauteur) if mots else None
            milieu = (g[0] + g[1]) / 2 if g else largeur / 2
            gauche = [w for w in mots if (w[0] + w[2]) / 2 < milieu]
            droite = [w for w in mots if (w[0] + w[2]) / 2 >= milieu]
            yield leaf, 2 * leaf - 14, lignes_colonne(gauche) if gauche else []
            yield leaf, 2 * leaf - 13, lignes_colonne(droite) if droite else []
        else:
            yield leaf, leaf - DECALAGE[vol], lignes_colonne(mots) if mots else []
        leaf += 1
        el.clear()
        while el.getprevious() is not None:
            del el.getparent()[0]


def pages_cherchetexte(vol):
    """Volume sans hOCR (t. V, index) : texte à plat d'archive.org."""
    t = gzip.open(fichier(vol, "_hocr_searchtext.txt.gz")).read().decode("utf-8", "replace")
    pi = json.load(gzip.open(fichier(vol, "_hocr_pageindex.json.gz")))
    for leaf, ent in enumerate(pi):
        yield leaf, leaf - DECALAGE[vol], t[ent[0]:ent[1]]


def main():
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    part = SORTIE.with_suffix(".part")
    n = 0
    with gzip.open(part, "wt", encoding="utf-8") as f:
        for vol in range(1, 6):
            k = 0
            if fichier(vol, "_hocr.html"):
                pages = ((leaf, page, texte_lignes(lignes)) for leaf, page, lignes in pages_hocr(vol))
            else:
                pages = pages_cherchetexte(vol)
            for leaf, page, texte in pages:
                if texte.strip() and page >= 1:
                    f.write(json.dumps({"tome": vol, "feuillet": leaf, "page": page, "texte": texte},
                                       ensure_ascii=False) + "\n")
                    k += 1
            print(f"t. {vol} : {k} pages", flush=True)
            n += k
    part.rename(SORTIE)
    print(f"{n} pages → {SORTIE}")


if __name__ == "__main__":
    main()
