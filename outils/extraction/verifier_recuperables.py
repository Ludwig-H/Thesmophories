#!/usr/bin/env python3
"""Contrôle de contenus_recuperables.tsv sur les fichiers sources.

Pour chaque ligne du tableau : le fichier indiqué existe-t-il, la ligne indiquée aussi, et le
contenu (premiers mots de l'extrait, après conversion du LaTeX) se lit-il à cette ligne ou juste
après ? Pour les contenus dits « désactivés » : la ligne de 2023 indiquée dans `proche_2023`
contient-elle bien un % et le texte annoncé ? Pour les contenus dits « disparus » : aucune suite
d'au moins 8 mots du passage ne doit se lire dans le corps actif de 2023.

Usage : python3 outils/extraction/verifier_recuperables.py [--depot CHEMIN]
Sortie : décompte par type, puis la liste des lignes en échec (au plus 40 par type).
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyse_latex import Source  # noqa: E402
import comparer_versions as cv  # noqa: E402
from extraire_travaux import FICHIERS_2023  # noqa: E402

FENETRE = 400       # lignes lues après la ligne indiquée (un commentaire s'étend sur plusieurs lignes)
csv.field_size_limit(10 ** 8)


def chemin_reel(depot: str, fichier: str) -> str | None:
    if ":main.tex" in fichier:
        return os.path.join(depot, cv.ARCHIVE_LOCAL)
    for pref, rempl in (("GCA/", cv.GCA), ("TH/", cv.TH)):
        if fichier.startswith(pref):
            return os.path.join(depot, rempl + fichier[len(pref):])
    return os.path.join(depot, fichier)


class Fichier:
    def __init__(self, p: str):
        with open(p, encoding="utf-8", errors="replace") as f:
            self.lignes = f.read().split("\n")


MACROS = {"Rpc": "Rᵖᶜ", "Rac": "Rᵃᶜ", "Rdeux": "R²", "Mon": "M", "PsiUn": "PSI-1194", "PsiDeux": "POxy-3839",
          "PsiTrois": "POxy-3840", "PsiQuatre": "POxy-4935", "PsiCinq": "POxy-1176"}


def normal(t: str) -> list:
    """Mots normalisés, marques d'appel et chiffres exposants ôtés."""
    t = re.sub(r"\\(Rpc|Rac|Rdeux|Mon|PsiUn|PsiDeux|PsiTrois|PsiQuatre|PsiCinq)\b(?:\{\})?",
               lambda m: " %s " % MACROS[m.group(1)], t)
    t = re.sub(r"\\(?:expo|auDessus|inRas|douteux)\b", " ", t)
    t = cv.detex(t)
    return [m for m in cv.mots(t) if not m.isdigit() and not re.fullmatch(r"[ᵃ-ᶿ²³¹⁰-⁹]+", m)]


def debut_extrait(ex: str) -> list:
    ex = re.sub(r"^« .*? » — ", "", ex)
    ex = re.sub(r"^\[…\]\s*", "", ex)
    ex = ex.split("[…]")[0]
    ex = re.sub(r"⟨?à revoir :?", " ", ex).replace("⟩", " ")
    ex = re.sub(r"^eff\{", " ", ex)
    ex = ex.split(" | ")[0]
    ex = re.sub(r"[ᵃ-ᶿ²³¹⁰-⁹]+(?=\W|$)", " ", ex)       # appels de note, exposants des sigles
    ex = re.sub(r"\^\(.*?\)", " ", ex)                  # lettres ajoutées, notées ^(…)
    ex = re.sub(r"[⟦⟧]", " ", ex)
    return [m for m in cv.mots(ex) if not m.isdigit()]


def chercher(mots_: list, cibles: str) -> bool:
    """Une suite de 3 mots (ou moins, si l'extrait est très court) prise dans les premiers mots de
    l'extrait se lit-elle dans la fenêtre ?"""
    if not mots_:
        return True
    n = min(3, len(mots_))
    for k in range(0, min(24, max(1, len(mots_) - n + 1))):
        if " ".join(mots_[k:k + n]) in cibles:
            return True
    return False


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=os.path.abspath(os.path.join(ici, "..", "..")))
    a = ap.parse_args()
    depot = a.depot
    tsv = os.path.join(depot, "edition", "donnees", "travaux_anterieurs", "contenus_recuperables.tsv")
    with open(tsv, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    cache = {}
    bilan = defaultdict(Counter)
    echecs = defaultdict(list)
    for num, r in enumerate(rows, start=2):
        typ = r["type"]
        fic = r["fichier"]
        if not fic or not r["ligne"]:
            bilan[typ]["sans lieu"] += 1
            echecs[typ].append((num, "sans lieu", r["vers"], r["extrait"][:90]))
            continue
        p = chemin_reel(depot, fic)
        if not os.path.exists(p):
            bilan[typ]["fichier introuvable"] += 1
            echecs[typ].append((num, "fichier introuvable", fic, ""))
            continue
        F = cache.setdefault(p, Fichier(p))
        n = int(r["ligne"])
        if not 1 <= n <= len(F.lignes):
            bilan[typ]["ligne hors du fichier"] += 1
            echecs[typ].append((num, "ligne hors du fichier", fic, n))
            continue
        if typ in ("attribution",) or r["statut_2023"].startswith("figure"):
            bilan[typ]["non testé"] += 1
            continue
        fen = " ".join(F.lignes[max(0, n - 3):n + FENETRE])
        cibles = " ".join(normal(fen))
        m = debut_extrait(r["extrait"])
        if typ == "traduction" or typ == "texte grec":
            m = [x for x in m if not x.isdigit()]
        if chercher(m, cibles):
            bilan[typ]["ok"] += 1
        else:
            bilan[typ]["contenu non retrouvé à ce lieu"] += 1
            echecs[typ].append((num, "non retrouvé", "%s l. %s" % (fic[-34:], n), r["extrait"][:110]))

    # désactivés : la ligne de 2023 indiquée
    fic23 = {re.sub(r"^.*Harmattan 2023 ", "", os.path.basename(x)).replace(".tex", ""): x for x in FICHIERS_2023}
    for num, r in enumerate(rows, start=2):
        m = re.match(r"commenté en 2023 : (.*), l\. (\d+)$", r["proche_2023"])
        if not m:
            if r["statut_2023"].startswith("désactiv") and r["type"] != "conjecture « Bibi »":
                bilan["pointeurs 2023"]["sans pointeur"] += 1
            continue
        p = os.path.join(depot, fic23[m.group(1)])
        F = cache.setdefault(p, Fichier(p))
        n = int(m.group(2))
        l = F.lignes[n - 1]
        # le texte doit se lire autour de cette ligne : un passage commenté occupe souvent des
        # dizaines de lignes, et le renvoi vise la ligne qui en contient le plus de mots
        proche = " ".join(normal(" ".join(F.lignes[max(0, n - 120):n + FENETRE])))
        cle = re.sub(r"^.*?\s[—:]\s", "", r["extrait"]) if r["extrait"].startswith("«") else r["extrait"]
        mots_ = [x for frag in cle.split("[…]") for x in debut_extrait(frag)]
        if "%" not in l:
            bilan["pointeurs 2023"]["ligne sans %"] += 1
            echecs["pointeurs 2023"].append((num, "ligne sans %", r["proche_2023"], l[:80]))
        elif chercher(mots_, proche):
            bilan["pointeurs 2023"]["ok (ligne commentée, texte retrouvé)"] += 1
        else:
            bilan["pointeurs 2023"]["ligne commentée, texte non retrouvé"] += 1
            echecs["pointeurs 2023"].append((num, "texte non retrouvé", r["proche_2023"], r["extrait"][:90]))

    # disparus : aucune suite de 8 mots dans le corps actif de 2023
    act = cv.Couverture()
    for rel in FICHIERS_2023:
        act.ajouter(cv.texte_actif_fichier(os.path.join(depot, rel))[0])
    for num, r in enumerate(rows, start=2):
        if not r["statut_2023"].startswith("disparu") or r["type"] not in ("commentaire", "note"):
            continue
        for frag in re.sub(r"^« .*? » — ", "", r["extrait"]).split("[…]"):
            w = [j[0] for j in cv.jetons(frag)[1]]
            if len(w) < 8:
                continue
            cov = act.masque(w)
            part = sum(cov) / len(w)
            if part >= 0.5:
                bilan["contrôle des disparus"]["encore lisible en 2023"] += 1
                echecs["contrôle des disparus"].append((num, "%.0f %%" % (100 * part), r["vers"], frag[:110]))
            else:
                bilan["contrôle des disparus"]["ok"] += 1

    for typ in sorted(bilan):
        print(typ, dict(bilan[typ]))
    for typ in sorted(echecs):
        print("---", typ, len(echecs[typ]))
        for e in echecs[typ][:40]:
            print("  ", e)


if __name__ == "__main__":
    main()
