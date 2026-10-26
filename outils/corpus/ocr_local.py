#!/usr/bin/env python3
"""OCR local (Tesseract, grec ancien + latin) d'un livre numérisé sur archive.org.

Pour les ouvrages dont l'OCR d'archive.org est inutilisable (une seule langue reconnue :
le grec d'un volume « latin » devient du charabia, et inversement), on réocérise les
images JP2 avec Tesseract en grc+lat. Les résultats sont écrits au format des fichiers
d'archive.org, dans .sources/corpus/ocr_archive/<id>/, pour que indexer.py les traite
comme les autres sources OCR (et que hocr_colonnes.py puisse s'y appliquer) :
  <id>_hocr_searchtext.txt.gz, <id>_hocr_pageindex.json.gz, <id>_hocr.html,
  <id>_ocr_local.json (moteur, langues, date) ; les pages faites sont gardées dans
  .travail/ocr_local/<id>/ (reprise possible après interruption).

  python3 outils/corpus/ocr_local.py bub_gb_y5sQAAAAIAAJ --processus 6
  python3 outils/corpus/ocr_local.py bub_gb_y5sQAAAAIAAJ --feuillets 70-480

Prérequis : tesseract ≥ 5 et les modèles grc et lat (tessdata, dans TESSDATA_PREFIX ou
.travail/tessdata/).
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
import urllib.parse
import urllib.request
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
OCR = RACINE / ".sources" / "corpus" / "ocr_archive"
TRAVAIL = RACINE / ".travail" / "ocr_local"
TESSDATA = os.environ.get("TESSDATA_PREFIX") or str(RACINE / ".travail" / "tessdata")
UA = {"User-Agent": "thesmophories-corpus/1.0"}


def metadonnees(ident):
    with urllib.request.urlopen(urllib.request.Request(f"https://archive.org/metadata/{ident}", headers=UA),
                                timeout=120) as r:
        return json.load(r)


def telecharger(url, dest, essais=4):
    for k in range(essais):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300) as r:
                data = r.read()
            dest.write_bytes(data)
            return
        except Exception:
            if k == essais - 1:
                raise
            time.sleep(5 * (k + 1))


def ocr_feuillet(args):
    ident, zipname, prefixe, n, langues, dossier = args
    sortie = dossier / f"{n:04d}.hocr"
    if sortie.exists():
        return n, "déjà fait"
    from PIL import Image
    jp2 = dossier / f"{n:04d}.jp2"
    png = dossier / f"{n:04d}.png"
    url = (f"https://archive.org/download/{ident}/{urllib.parse.quote(zipname)}/"
           f"{urllib.parse.quote(prefixe)}%2F{urllib.parse.quote(prefixe.replace('_jp2', ''))}_{n:04d}.jp2")
    telecharger(url, jp2)
    Image.open(jp2).convert("L").save(png)
    jp2.unlink()
    env = dict(os.environ, OMP_THREAD_LIMIT="1", TESSDATA_PREFIX=TESSDATA)
    base = dossier / f"{n:04d}.tmp"
    subprocess.run(["tesseract", str(png), str(base), "-l", langues, "--psm", "3",
                    "-c", "tessedit_create_hocr=1", "-c", "tessedit_create_txt=0"],
                   check=True, capture_output=True, env=env, timeout=1800)
    png.unlink()
    (dossier / f"{n:04d}.tmp.hocr").rename(sortie)
    return n, "ok"


def texte_hocr(chemin):
    """Texte d'une page hOCR (lignes dans l'ordre du fichier)."""
    from lxml import etree
    doc = etree.parse(str(chemin), etree.HTMLParser())
    lignes = []
    for l in doc.iter("span"):
        if l.get("class") == "ocr_line":
            mots = ["".join(w.itertext()).strip() for w in l if w.get("class") == "ocrx_word"]
            mots = [m for m in mots if m]
            if mots:
                lignes.append(" ".join(mots))
    return "\n".join(lignes)


def assembler(ident, nb, dossier, langues, version):
    d = OCR / ident
    d.mkdir(parents=True, exist_ok=True)
    textes, index, pos = [], [], 0
    corps_hocr = []
    for n in range(nb):
        f = dossier / f"{n:04d}.hocr"
        t = texte_hocr(f) if f.exists() else ""
        index.append([pos, pos + len(t)])
        textes.append(t)
        pos += len(t) + 1
        if f.exists():
            h = f.read_text(encoding="utf-8")
            m = re.search(r"<body>(.*)</body>", h, re.S)
            page = m.group(1) if m else ""
            corps_hocr.append(page.replace("class='ocr_page'", "class=\"ocr_page\""))
        else:
            corps_hocr.append(f'<div class="ocr_page" id="page_{n:06d}" title="bbox 0 0 0 0"></div>')
    with gzip.open(d / f"{ident}_hocr_searchtext.txt.gz", "wt", encoding="utf-8") as f:
        f.write("\n".join(textes))
    with gzip.open(d / f"{ident}_hocr_pageindex.json.gz", "wt", encoding="utf-8") as f:
        json.dump(index, f)
    with open(d / f"{ident}_hocr.html", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml"><head>'
                f'<meta name="ocr-system" content="{version} (local, {langues})" /></head><body>\n')
        f.write("\n".join(corps_hocr))
        f.write("\n</body></html>\n")
    json.dump({"identifiant": ident, "moteur": version, "langues": langues, "feuillets": nb,
               "date": time.strftime("%Y-%m-%d %H:%M")},
              open(d / f"{ident}_ocr_local.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # l'ancienne sortie de hocr_colonnes, faite sur l'OCR d'archive.org, n'est plus valable
    ancien = d / f"{ident}_colonnes.json.gz"
    if ancien.exists():
        ancien.unlink()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("identifiant")
    ap.add_argument("--feuillets", help="intervalle de feuillets à océriser, p. ex. 70-480 (défaut : tous)")
    ap.add_argument("--langues", default="grc+lat")
    ap.add_argument("--processus", type=int, default=6)
    a = ap.parse_args()
    ident = a.identifiant
    meta = metadonnees(ident)
    zips = [f["name"] for f in meta.get("files", []) if f["name"].endswith("_jp2.zip")]
    if not zips:
        sys.exit(f"{ident} : pas d'images JP2")
    zipname = zips[0]
    prefixe = zipname[:-4]  # dossier interne : <nom>_jp2
    nb = int(meta.get("metadata", {}).get("imagecount") or 0)
    if not nb:
        sys.exit(f"{ident} : nombre d'images inconnu")
    debut, fin = 0, nb - 1
    if a.feuillets:
        x, _, y = a.feuillets.partition("-")
        debut, fin = int(x), int(y or x)
    dossier = TRAVAIL / ident
    dossier.mkdir(parents=True, exist_ok=True)
    version = subprocess.run(["tesseract", "--version"], capture_output=True, text=True).stdout.split("\n")[0]
    taches = [(ident, zipname, prefixe, n, a.langues, dossier) for n in range(debut, fin + 1)]
    t0 = time.time()
    faits = 0
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for fu in cf.as_completed([ex.submit(ocr_feuillet, t) for t in taches]):
            try:
                n, etat = fu.result()
                faits += 1
                if faits % 20 == 0:
                    print(f"{faits}/{len(taches)} feuillets ({time.time() - t0:.0f} s)", flush=True)
            except Exception as e:
                print(f"ÉCHEC : {type(e).__name__}: {e}", file=sys.stderr, flush=True)
    assembler(ident, nb, dossier, a.langues, version)
    print(f"{ident} : {faits} feuillets océrisés en {time.time() - t0:.0f} s → {OCR / ident}")


if __name__ == "__main__":
    main()
