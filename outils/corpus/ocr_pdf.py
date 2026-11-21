#!/usr/bin/env python3
"""OCR local (Tesseract) d'un PDF image sans couche texte, ou d'une partie de ses pages.

Produit un PDF « cherchable » : les pages d'origine (image inchangée) recouvertes d'une couche
texte invisible (sortie « textonly_pdf » de Tesseract), plus le texte brut de chaque page.
Le PDF produit se range dans .sources/ (jamais dans le dépôt : les livres océrisés sont en
général sous droits) ; placé sous .sources/drive/fichiers/, il est repris par sources_drive.py
puis indexer.py comme les autres fichiers du Drive.

  python3 outils/corpus/ocr_pdf.py SOURCE.pdf SORTIE.pdf --pages 437-560 --langues grc+ita --processus 12

--pages : pages du PDF, numérotées à partir de 1, bornes comprises (défaut : toutes).
Les pages faites sont gardées dans .travail/ocr_pdf/<nom de la sortie>/ : reprise possible
après interruption. Le texte brut est écrit à côté de la sortie (SORTIE.txt, pages séparées
par un saut de page \\f, chacune précédée de « [page PDF n] »).
OCR NON CORRIGÉ : toute citation tirée de ce texte se vérifie sur l'image de la page.
"""
import argparse
import concurrent.futures as cf
import os
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent


def ocr_page(args):
    source, n, dpi, langues, dossier = args
    base = dossier / f"{n:04d}"
    if (dossier / f"{n:04d}.pdf").exists() and (dossier / f"{n:04d}.txt").exists():
        return n, "déjà fait"
    import pymupdf
    doc = pymupdf.open(source)
    png = dossier / f"{n:04d}.png"
    doc[n - 1].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY).save(png)
    env = dict(os.environ, OMP_THREAD_LIMIT="1")
    subprocess.run(["tesseract", str(png), str(base), "-l", langues, "--psm", "3", "--dpi", str(dpi),
                    "-c", "textonly_pdf=1", "txt", "pdf"],
                   check=True, capture_output=True, env=env, timeout=1800)
    png.unlink()
    return n, "ok"


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    ap.add_argument("source")
    ap.add_argument("sortie")
    ap.add_argument("--pages", help="a-b (pages du PDF, à partir de 1)")
    ap.add_argument("--langues", default="grc+lat")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--processus", type=int, default=8)
    a = ap.parse_args()
    import pymupdf
    source = Path(a.source).resolve()
    sortie = Path(a.sortie).resolve()
    doc = pymupdf.open(source)
    if a.pages:
        d, f = (int(x) for x in a.pages.split("-"))
    else:
        d, f = 1, doc.page_count
    if not (1 <= d <= f <= doc.page_count):
        sys.exit(f"pages hors limites (1-{doc.page_count})")
    dossier = RACINE / ".travail" / "ocr_pdf" / sortie.stem
    dossier.mkdir(parents=True, exist_ok=True)
    taches = [(str(source), n, a.dpi, a.langues, dossier) for n in range(d, f + 1)]
    with cf.ProcessPoolExecutor(a.processus) as ex:
        for k, (n, etat) in enumerate(ex.map(ocr_page, taches), 1):
            if k % 10 == 0 or k == len(taches):
                print(f"{k}/{len(taches)} pages (dernière : {n}, {etat})", flush=True)
    # assemblage : page d'origine + couche texte invisible
    out = pymupdf.open()
    textes = []
    for n in range(d, f + 1):
        out.insert_pdf(doc, from_page=n - 1, to_page=n - 1)
        page = out[-1]
        couche = pymupdf.open(dossier / f"{n:04d}.pdf")
        page.show_pdf_page(page.rect, couche, 0, overlay=True)
        textes.append(f"[page PDF {n}]\n" + (dossier / f"{n:04d}.txt").read_text(encoding="utf-8"))
    sortie.parent.mkdir(parents=True, exist_ok=True)
    out.save(sortie, garbage=3, deflate=True)
    sortie.with_suffix(".txt").write_text("\f".join(textes), encoding="utf-8")
    print(f"{f - d + 1} pages → {sortie} (+ {sortie.with_suffix('.txt').name})")


if __name__ == "__main__":
    main()
