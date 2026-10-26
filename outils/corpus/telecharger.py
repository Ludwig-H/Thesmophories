#!/usr/bin/env python3
"""Télécharge ou met à jour les corpus numériques ouverts dans .sources/corpus/.

Rien de ce qui est téléchargé n'est versionné (.sources/ est ignoré par git).

  python3 outils/corpus/telecharger.py            # tout
  python3 outils/corpus/telecharger.py perseus first1k ocr
  python3 outils/corpus/telecharger.py --maj      # met aussi à jour les dépôts git déjà clonés

Sources :
  perseus   PerseusDL/canonical-greekLit (TEI CTS, CC BY-SA 4.0)
  first1k   OpenGreekAndLatin/First1KGreek (TEI CTS, CC BY-SA 4.0)
  lsj       PerseusDL/lexica, LSJ seulement (TEI, Beta Code, CC BY-SA 4.0)
  dclp      papyri/idp.data, dossier DCLP seulement (EpiDoc, CC BY 3.0)
  diorisis  Diorisis Ancient Greek Corpus (figshare 10.6084/m9.figshare.6187256, CC BY 4.0)
  ocr       ouvrages du domaine public d'archive.org listés dans sources_ocr.tsv
            (texte OCR Tesseract + index des pages + numéros de page imprimés)
"""

import argparse
import concurrent.futures as cf
import csv
import os
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
CORPUS = RACINE / ".sources" / "corpus"

DEPOTS = {
    "perseus": ("https://github.com/PerseusDL/canonical-greekLit.git", "canonical-greekLit", None),
    "first1k": ("https://github.com/OpenGreekAndLatin/First1KGreek.git", "First1KGreek", None),
    "lsj": ("https://github.com/PerseusDL/lexica.git", "lexica", "CTS_XML_TEI/perseus/pdllex/grc/lsj"),
    "dclp": ("https://github.com/papyri/idp.data.git", "idp.data", "DCLP"),
}
DIORISIS_URL = "https://ndownloader.figshare.com/files/11296247"
SUFFIXES_OCR = ["_hocr_searchtext.txt.gz", "_hocr_pageindex.json.gz", "_page_numbers.json", "_meta.xml"]


def git(*args, cwd=None):
    print("+ git", " ".join(args), flush=True)
    subprocess.run(["git", *args], cwd=cwd, check=True)


def depot(nom, maj):
    url, dossier, sparse = DEPOTS[nom]
    cible = CORPUS / dossier
    if not cible.exists():
        if sparse:
            git("clone", "--depth", "1", "--filter=blob:none", "--sparse", url, str(cible))
            git("sparse-checkout", "set", sparse, cwd=cible)
        else:
            git("clone", "--depth", "1", url, str(cible))
    elif maj:
        git("fetch", "--depth", "1", "origin", cwd=cible)
        git("reset", "--hard", "FETCH_HEAD", cwd=cible)
    else:
        print(f"{dossier} : déjà présent (--maj pour mettre à jour)")


def telecharger_fichier(url, dest):
    dest = Path(dest)
    if dest.exists() and dest.stat().st_size > 0:
        return "déjà là"
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "thesmophories-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as f:
        while True:
            bloc = r.read(1 << 20)
            if not bloc:
                break
            f.write(bloc)
    tmp.rename(dest)
    return "ok"


def diorisis():
    d = CORPUS / "diorisis"
    d.mkdir(parents=True, exist_ok=True)
    z = d / "Diorisis.zip"
    print("Diorisis :", telecharger_fichier(DIORISIS_URL, z))
    x = d / "x"
    if not x.exists() or not any(x.iterdir()):
        print("Décompression de Diorisis…")
        with zipfile.ZipFile(z) as zf:
            zf.extractall(x)


def lire_sources_ocr():
    with open(ICI / "sources_ocr.tsv", encoding="utf-8") as f:
        lignes = [l for l in f if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(lignes, delimiter="\t"))


def fichiers_item(ident):
    """Noms réels des fichiers d'un item (ils ne reprennent pas toujours l'identifiant)."""
    import json
    import urllib.parse
    req = urllib.request.Request(f"https://archive.org/metadata/{ident}",
                                 headers={"User-Agent": "thesmophories-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        meta = json.load(r)
    noms = [f["name"] for f in meta.get("files", [])]
    res = {}
    for suf in SUFFIXES_OCR:
        cands = [n for n in noms if n.endswith(suf)]
        if cands:
            # préférer le fichier qui porte l'identifiant
            cands.sort(key=lambda n: (not n.startswith(ident), len(n)))
            res[suf] = f"https://archive.org/download/{ident}/{urllib.parse.quote(cands[0])}"
    return res


def ocr():
    taches = []
    for s in lire_sources_ocr():
        ident = s["identifiant"]
        d = CORPUS / "ocr_archive" / ident
        d.mkdir(parents=True, exist_ok=True)
        manquants = [suf for suf in SUFFIXES_OCR if not (d / f"{ident}{suf}").exists()]
        if not manquants:
            continue
        try:
            urls = fichiers_item(ident)
        except Exception as e:
            print(f"{ident} : métadonnées inaccessibles ({e})", file=sys.stderr)
            continue
        for suf in manquants:
            if suf in urls:
                taches.append((urls[suf], d / f"{ident}{suf}"))
            else:
                print(f"{ident} : pas de fichier {suf}", file=sys.stderr)
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(telecharger_fichier, u, p): (u, p) for u, p in taches}
        for fu in cf.as_completed(futs):
            u, p = futs[fu]
            try:
                print(f"{p.name} : {fu.result()}")
            except Exception as e:  # fichier absent pour certains items (p. ex. page_numbers)
                print(f"{p.name} : ÉCHEC ({e})", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="*", default=["perseus", "first1k", "lsj", "dclp", "diorisis", "ocr"])
    ap.add_argument("--maj", action="store_true", help="mettre à jour les dépôts git existants")
    a = ap.parse_args()
    CORPUS.mkdir(parents=True, exist_ok=True)
    for s in a.sources:
        if s in DEPOTS:
            depot(s, a.maj)
        elif s == "diorisis":
            diorisis()
        elif s == "ocr":
            ocr()
        else:
            sys.exit(f"source inconnue : {s}")


if __name__ == "__main__":
    main()
