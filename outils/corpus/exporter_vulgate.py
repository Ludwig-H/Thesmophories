#!/usr/bin/env python3
"""Exporte vers par vers le texte des Thesmophories de Perseus (Hall–Geldart, Oxford, 1907).

Ce texte sert de « vulgate » de référence pour la collation avec R (Ravennas) : ce n'est
pas un texte établi par nous et il ne doit jamais être cité comme autorité.

Sortie : .sources/corpus/thesmo_hall_geldart.tsv (non versionné : dérivé de Perseus,
CC BY-SA 4.0), deux colonnes avec en-tête : vers, texte.
Conventions :
  - un vers par ligne, numérotation de Hall–Geldart (celle de Perseus) ;
  - les vers partagés entre personnages (antilabè, part="I/M/F" dans le TEI, numérotés
    6, 6b…) sont réunis sous le numéro du vers, les répliques séparées par « | » ;
  - le texte est celui du TEI (NFC), apostrophes d'élision comprises ; les noms des
    personnages et les didascalies sont omis.

  python3 outils/corpus/exporter_vulgate.py [--avec-locuteurs]
"""

import argparse
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import indexer  # noqa: E402

from lxml import etree  # noqa: E402

SOURCE = indexer.CORPUS / "canonical-greekLit" / "data" / "tlg0019" / "tlg008" / "tlg0019.tlg008.perseus-grc2.xml"
SORTIE = indexer.CORPUS / "thesmo_hall_geldart.tsv"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--avec-locuteurs", action="store_true", help="ajouter une 3e colonne : locuteur(s)")
    ap.add_argument("--sortie", default=str(SORTIE))
    a = ap.parse_args()
    doc = etree.parse(str(SOURCE), indexer.PARSEUR)
    passages, _ = indexer.passages_tei(doc)
    n = 0
    with open(a.sortie, "w", encoding="utf-8") as f:
        f.write("vers\ttexte" + ("\tlocuteur" if a.avec_locuteurs else "") + "\n")
        for ref, loc, texte, _ in passages:
            vers = ref[-1]
            ligne = f"{vers}\t{texte}"
            if a.avec_locuteurs:
                ligne += f"\t{loc or ''}"
            f.write(ligne + "\n")
            n += 1
    print(f"{n} vers → {a.sortie}")


if __name__ == "__main__":
    main()
