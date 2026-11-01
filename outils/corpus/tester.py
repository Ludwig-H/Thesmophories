#!/usr/bin/env python3
"""Tests de contrôle de l'index et du moteur de recherche (à relancer après chaque
reconstruction de l'index).

Chaque test exécute une requête de chercher.py et vérifie que les références attendues
figurent parmi les résultats (attentes vérifiées une fois sur les textes). Il contrôle
aussi l'export de la vulgate Hall–Geldart.

  python3 outils/corpus/tester.py          # résumé ; code de sortie 1 en cas d'échec
  python3 outils/corpus/tester.py -v       # affiche les références trouvées
"""

import argparse
import sqlite3
import sys
from pathlib import Path
from types import SimpleNamespace

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import chercher  # noqa: E402

# (requête, options, références attendues (début de la référence lisible), commentaire)
TESTS = [
    ('"Νείλου μὲν αἵδε καλλιπάρθενοι ῥοαί"', {}, ["Eur. Hel. 1", "Ar. Thesm. 855"],
     "Eur. Hel. 1, cité par Mnésiloque-Hélène en Thesm. 855"),
    ('"σοφοὶ τύραννοι τῶν σοφῶν ξυνουσίᾳ"', {}, ["Pl. Thg.", "Aristid."],
     "vers cité par Platon (graphie συν-) : variantes ξυν-/συν- admises par défaut (Rép. 568b intercale εἰσι)"),
    ("ὀρθρογόη", {}, ["LSJ s.v. ὀρθρογόη", "Phot. (Naber)", "Sud. (Adler) III p. 559"],
     "épithète de l'hirondelle (Hés. Op. 568 a ὀρθογόη dans Perseus) ; absente d'Hésychius"),
    ("πυθοῦ χελιδὼν", {}, [], "expression testée telle quelle (voir le compte rendu)"),
    ("ἀπόκυνον", {"auteur": "Hsch"}, ["Hsch. (Schmidt min.)"], "glose d'Hésychius (OCR de Schmidt)"),
    ("χοάνη", {"auteur": "Hsch.", "oeuvre": "gloses"}, ["Hsch. χ 576 (Hansen–Cunningham IV, p. 223)"],
     "Hésychius de Latte–Hansen–Cunningham : glose numérotée, Thesm. 18"),
    ("ἀϋτή", {"auteur": "Hsch.", "oeuvre": "gloses"}, ["Hsch. α 8382 (Latte I, p. 382)"],
     "tréma rattaché à sa lettre (glyphe isolé des polices Kleinlogel)"),
    ("Thesm", {"auteur": "Hsch.", "oeuvre": "gloses"}, ["Hsch. χ 575", "Hsch. π 3096", "Hsch. σ 2044"],
     "gloses rapportées aux Thesmophories par l'éditeur"),
    ("κατοπτρον", {"auteur": "Hsch. app."}, ["Hsch. app."], "apparats, indexés à part"),
    ("κάμπτειν", {"auteur": "Hsch.", "oeuvre": "gloses"}, ["Hsch. κ 617 (Latte II, p. 516)"],
     "Κ–Ο : le fichier du t. II contient aussi le t. IIb"),
    ("ἀμείβεσθαι ἀποκρίνεσθαι", {"auteur": "Synag"}, ["Synag. (Cunningham) p. 95"], "Synagoge : polices Kleinlogel rétablies"),
    ("ἀνακλώμενον", {"auteur": "Adler"}, ["Sud. (Adler) I p. 171"], "Souda d'Adler (OCR d'archive.org, feuillet 200)"),
]


def options(**kw):
    d = dict(requete="", exact=False, strict=False, lemme=False, sans_variantes=False, auteur=None,
             oeuvre=None, collection=None, sans_ocr=False, toutes_editions=False, sans_chevauchement=False,
             contexte=0, max=50, complet=False, json=False)
    d.update(kw)
    return SimpleNamespace(**d)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-v", "--verbeux", action="store_true")
    a = ap.parse_args()
    con = sqlite3.connect(f"file:{chercher.BASE}?mode=ro", uri=True)
    echecs = 0
    for requete, opts, attendus, commentaire in TESTS:
        o = options(requete=requete, **opts)
        res, termes, _, fts = chercher.chercher(con, o)
        refs = []
        for r in res:
            ref = chercher.reference(r["o"], r["p"])
            if r["p"].get("ref_fin"):
                ref += f" → {r['p']['ref_fin']}"
            refs.append((ref, r["mode"]))
        manquants = [x for x in attendus if not any(ref.startswith(x) for ref, _ in refs)]
        etat = "OK " if not manquants else "ÉCHEC"
        if manquants:
            echecs += 1
        print(f"[{etat}] {requete}  ({len(refs)} résultat(s)) — {commentaire}")
        if manquants:
            print(f"        attendus non trouvés : {', '.join(manquants)}")
        if a.verbeux:
            for ref, mode in refs[:40]:
                print(f"        {ref}" + (f"  [{mode}]" if mode != "normal" else ""))
    # vulgate
    tsv = chercher.BASE.parent / "thesmo_hall_geldart.tsv"
    if tsv.exists():
        lignes = tsv.read_text(encoding="utf-8").splitlines()
        ok = lignes[0] == "vers\ttexte" and lignes[1].startswith("1\t") and lignes[-1].startswith("1231\t")
        print(f"[{'OK ' if ok else 'ÉCHEC'}] vulgate Hall–Geldart : {len(lignes) - 1} vers")
        echecs += 0 if ok else 1
    else:
        print("[ÉCHEC] vulgate absente (lancer exporter_vulgate.py)")
        echecs += 1
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
