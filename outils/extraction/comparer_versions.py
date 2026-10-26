#!/usr/bin/env python3
"""Comparaison des versions successives des travaux de l'auteur.

Versions : « nov 2022 » (pièce entière), « Harmattan mars 2023 » (vv. 1-952),
« Harmattan 2023 » (deux fichiers, version de référence). Chaque version est extraite
avec le même analyseur que `extraire_travaux.py`, puis on recense, pour chaque version
ancienne, les commentaires, notes, entrées d'apparat et testimonia qui ne se retrouvent
pas dans la version la plus récente (ni actifs, ni désactivés), ainsi que les
différences de texte grec vers par vers.

Sorties (edition/donnees/travaux_anterieurs/) :
  comparaison_versions.json   détail complet
  comparaison_versions.tsv    une ligne par élément absent/modifié

Usage : python3 outils/extraction/comparer_versions.py [--depot CHEMIN]
"""
from __future__ import annotations

import argparse
import csv
import difflib
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extraire_travaux import FICHIERS_2023, extraire  # noqa: E402

VERSIONS = [
    ("nov2022", "nov 2022", ["latex/Aristophane-Thesmo nov 2022.tex"]),
    ("mars2023", "Harmattan mars 2023", ["latex/Aristophane-Thesmo Harmattan mars 2023.tex"]),
    ("harmattan2023", "Harmattan 2023", FICHIERS_2023),
]


def mots(s: str) -> list:
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower()
    return re.findall(r"\w+", s)


def bardeaux(s: str, k: int = 3) -> set:
    m = mots(s)
    if len(m) < k:
        return set(m)
    return {" ".join(m[i:i + k]) for i in range(len(m) - k + 1)}


def inclusion(a: set, b: set) -> float:
    return len(a & b) / len(a) if a else 0.0


class Index:
    """Index inversé de bardeaux pour retrouver rapidement le meilleur candidat."""

    def __init__(self, elements: list, cle_texte="texte"):
        self.el = elements
        self.sh = [bardeaux(e.get(cle_texte, "")) for e in elements]
        self.inv = defaultdict(set)
        for i, s in enumerate(self.sh):
            for x in s:
                self.inv[x].add(i)

    def meilleur(self, texte: str):
        s = bardeaux(texte)
        if not s:
            return None, 0.0
        c = Counter()
        for x in s:
            for i in self.inv.get(x, ()):
                c[i] += 1
        if not c:
            return None, 0.0
        i, n = c.most_common(1)[0]
        return self.el[i], n / len(s)


def collecter(res: dict) -> dict:
    """Éléments comparables d'une extraction."""
    out = {"commentaire": [], "note": [], "apparat": [], "testimonia": [],
           "commentaire_desactive": [], "note_desactivee": [], "apparat_desactive": [],
           "testimonia_desactive": [], "grec": {}, "francais": {}}
    for g in res["groupes"]:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                out["commentaire"].append({"id": c["id"], "plage": c["plage"], "lemme": c["lemme"],
                                           "texte": c["texte"], "groupe": g["id"]})
                for n in c["notes"]:
                    out["note"].append({"id": n["id"], "plage": c["plage"], "numero": n["numero"],
                                        "texte": n["texte"], "commentaire": c["id"], "groupe": g["id"]})
            for t in g[cote]["testimonia"]:
                out["testimonia"].append({"id": t["id"], "plage": t["plage"], "texte": t["texte"],
                                          "cote": cote, "groupe": g["id"]})
            for d in g[cote]["desactives"]:
                t = {"commentaire": "commentaire_desactive", "note": "note_desactivee",
                     "apparat": "apparat_desactive", "testimonia": "testimonia_desactive"}.get(d["type"])
                if t:
                    txt = d.get("texte", "")
                    if d["type"] == "commentaire" and d.get("args"):
                        txt = " ".join(d["args"][1:])
                    out[t].append({"plage": d["args"][0] if d.get("args") else "", "texte": txt,
                                   "groupe": g["id"], "ligne_source": d["ligne_source"]})
        for a in g["grec"]["apparat"]:
            for sgm in a["segments"]:
                for e in sgm["entrees"]:
                    out["apparat"].append({"id": a["id"], "vers": sgm["vers"], "debut": sgm["debut"],
                                           "texte": e["texte"], "groupe": g["id"]})
        for l in g["grec"]["lignes"]:
            if l["vers"] is not None:
                out["grec"].setdefault(l["vers"], []).append(l["texte"])
        for l in g["francais"]["lignes"]:
            if l["vers"] is not None:
                out["francais"].setdefault(l["vers"], []).append(l["texte"])
    # les commentaires désactivés contiennent souvent des commentaires internes commentés
    for g in res["groupes"]:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                if c.get("desactive_interne"):
                    out["commentaire_desactive"].append({
                        "plage": c["plage"], "groupe": g["id"],
                        "texte": " ".join(x["texte"] for x in c["desactive_interne"]),
                        "ligne_source": c["desactive_interne"][0]["ligne"]})
                for n in c["notes"]:
                    if n.get("desactive_interne"):
                        out["note_desactivee"].append({
                            "plage": c["plage"], "groupe": g["id"],
                            "texte": " ".join(x["texte"] for x in n["desactive_interne"]),
                            "ligne_source": n["desactive_interne"][0]["ligne"]})
    return out


def norm_grec(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "")
    s = s.replace("'", "᾽").replace("’", "᾽").replace("ʼ", "᾽").replace("᾿", "᾽")
    return re.sub(r"\s+", " ", s).strip()


def diff_mots(a: str, b: str) -> str:
    wa, wb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    parts = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        parts.append("%s → %s" % (" ".join(wa[i1:i2]) or "∅", " ".join(wb[j1:j2]) or "∅"))
    return " ; ".join(parts)


def comparer(ancien: dict, recent: dict, nom: str, plage_vers=None) -> dict:
    A, R = collecter(ancien), collecter(recent)
    res = {"version": nom, "elements": [], "stats": {}}
    seuil = 0.6

    def dans_plage(plage: str) -> bool:
        if plage_vers is None:
            return True
        m = re.match(r"\D*(\d+)", plage or "")
        return bool(m) and plage_vers[0] <= int(m.group(1)) <= plage_vers[1]

    for typ, typ_des in (("commentaire", "commentaire_desactive"), ("note", "note_desactivee"),
                         ("testimonia", "testimonia_desactive")):
        idx_actif = Index(R[typ])
        idx_des = Index(R[typ_des])
        plages_recentes = defaultdict(list)
        for x in R[typ]:
            plages_recentes[re.sub(r"\W", "", x.get("plage", ""))].append(x)
        st = Counter()
        for e in A[typ]:
            if not e["texte"].strip():
                continue
            m, sc = idx_actif.meilleur(e["texte"])
            if sc >= 0.9:
                st["conservé"] += 1
                continue
            if sc >= seuil:
                st["remanié"] += 1
                if typ != "testimonia" and sc < 0.75:
                    res["elements"].append({"type": typ, "statut": "remanié", "plage": e["plage"],
                                            "id_ancien": e["id"], "id_recent": m["id"], "score": round(sc, 2),
                                            "extrait": e["texte"][:300]})
                continue
            md, scd = idx_des.meilleur(e["texte"])
            if scd >= seuil:
                st["désactivé"] += 1
                res["elements"].append({"type": typ, "statut": "désactivé (commenté) dans la version récente",
                                        "plage": e["plage"], "id_ancien": e["id"], "id_recent": None,
                                        "score": round(scd, 2), "extrait": e["texte"][:300]})
                continue
            statut = "absent" if dans_plage(e["plage"]) else "hors du champ de la version récente"
            meme = plages_recentes.get(re.sub(r"\W", "", e["plage"]))
            if meme and typ == "commentaire":
                statut = "réécrit (même plage, texte largement nouveau)"
                m = meme[0]
            elif m is not None and sc >= 0.3 and re.sub(r"\W", "", m.get("plage", "")) == re.sub(r"\W", "", e["plage"]):
                statut = "réécrit (même plage, texte largement nouveau)"
            st[statut] += 1
            res["elements"].append({"type": typ, "statut": statut, "plage": e["plage"],
                                    "id_ancien": e["id"], "id_recent": m["id"] if m else None,
                                    "score": round(sc, 2), "longueur": len(e["texte"]),
                                    "extrait": e["texte"][:600]})
        res["stats"][typ] = dict(st)
    # apparat : par vers (± 2) puis global
    par_vers = defaultdict(list)
    for e in R["apparat"]:
        if e["debut"] is not None:
            par_vers[e["debut"]].append(e)
    idx_des = Index(R["apparat_desactive"])
    idx_tout = Index(R["apparat"])
    st = Counter()
    for e in A["apparat"]:
        cands = [x for d in range(-2, 3) for x in par_vers.get((e["debut"] or -99) + d, [])]
        sa = bardeaux(e["texte"], 2)
        best, sc = None, 0.0
        for c in cands:
            v = inclusion(sa, bardeaux(c["texte"], 2))
            if v > sc:
                best, sc = c, v
        if sc < 0.8:
            m, v = idx_tout.meilleur(e["texte"])
            if m is not None and v > sc and v >= 0.8:
                best, sc = m, v
        if sc >= 0.8:
            st["conservé"] += 1
            continue
        if sc >= 0.4:
            st["remanié"] += 1
            res["elements"].append({"type": "apparat", "statut": "remanié", "plage": e["vers"],
                                    "id_ancien": e["id"], "id_recent": best["id"], "score": round(sc, 2),
                                    "extrait": e["texte"][:300], "recent": best["texte"][:300]})
            continue
        md, scd = idx_des.meilleur(e["texte"])
        if scd >= 0.6:
            st["désactivé"] += 1
            res["elements"].append({"type": "apparat", "statut": "désactivé (commenté) dans la version récente",
                                    "plage": e["vers"], "id_ancien": e["id"], "id_recent": None,
                                    "score": round(scd, 2), "extrait": e["texte"][:300]})
            continue
        statut = "absent" if dans_plage(e["vers"]) else "hors du champ de la version récente"
        st[statut] += 1
        res["elements"].append({"type": "apparat", "statut": statut, "plage": e["vers"],
                                "id_ancien": e["id"], "id_recent": best["id"] if best else None,
                                "score": round(sc, 2), "extrait": e["texte"][:300]})
    res["stats"]["apparat"] = dict(st)
    # texte grec
    diffs = []
    communs = sorted(set(A["grec"]) & set(R["grec"]))
    for v in communs:
        a = norm_grec(" | ".join(A["grec"][v]))
        b = norm_grec(" | ".join(R["grec"][v]))
        if a != b:
            sa, sb = a.replace(" | ", " "), b.replace(" | ", " ")
            if sa == sb:
                nature = "découpage (antilabè/répartition) seulement"
            else:
                nature = diff_mots(sa, sb)
            diffs.append({"vers": v, "ancien": a, "recent": b, "differences": nature})
            res["elements"].append({"type": "texte_grec", "statut": "différent", "plage": str(v),
                                    "id_ancien": None, "id_recent": None, "score": None,
                                    "extrait": nature[:300]})
    seulement_ancien = sorted(set(A["grec"]) - set(R["grec"]))
    seulement_recent = sorted(set(R["grec"]) - set(A["grec"]))
    if plage_vers:
        seulement_recent = [v for v in seulement_recent if plage_vers[0] <= v <= plage_vers[1]]
    res["texte_grec"] = {"vers_communs": len(communs), "vers_differents": len(diffs),
                         "seulement_ancien": seulement_ancien, "seulement_recent": seulement_recent,
                         "differences": diffs}
    trad = sum(1 for v in set(A["francais"]) & set(R["francais"])
               if re.sub(r"\s+", " ", " ".join(A["francais"][v])) != re.sub(r"\s+", " ", " ".join(R["francais"][v])))
    res["stats"]["traduction_vers_modifies"] = trad
    res["stats"]["texte_grec_vers_differents"] = len(diffs)
    return res


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=os.path.abspath(os.path.join(ici, "..", "..")))
    a = ap.parse_args()
    sortie = os.path.join(a.depot, "edition", "donnees", "travaux_anterieurs")
    extractions = {}
    for cle, nom, fichiers in VERSIONS:
        extractions[cle] = extraire(a.depot, None, fichiers=fichiers, ecrire=False)
        s = extractions[cle]["statistiques"]
        print("%-14s groupes %4d  lignes gr. %4d  vers %s-%s  commentaires %3d  notes %3d  apparats %3d"
              % (nom, s["groupes"], s["lignes_grecques"], s["premier_vers"], s["dernier_vers"],
                 s["commentaires"], s["notes"], s["apparats"]))
    recent = extractions["harmattan2023"]
    resultat = {"versions": {cle: {"nom": nom, "fichiers": f, "statistiques": extractions[cle]["statistiques"]}
                             for cle, nom, f in VERSIONS},
                "comparaisons": []}
    for cle, nom, fichiers in VERSIONS[:-1]:
        s = extractions[cle]["statistiques"]
        plage = (s["premier_vers"], s["dernier_vers"])
        c = comparer(extractions[cle], recent, nom, plage_vers=None)
        c["plage_version"] = plage
        resultat["comparaisons"].append(c)
        print(nom, json.dumps(c["stats"], ensure_ascii=False))
    # mars 2023 -> nov 2022 : ce qui a changé entre les deux premières versions (texte grec seulement)
    with open(os.path.join(sortie, "comparaison_versions.json"), "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
    with open(os.path.join(sortie, "comparaison_versions.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["version", "type", "statut", "plage", "id_ancien", "id_recent_proche", "score", "extrait"])
        for c in resultat["comparaisons"]:
            for e in c["elements"]:
                w.writerow([c["version"], e["type"], e["statut"], e["plage"], e.get("id_ancien") or "",
                            e.get("id_recent") or "", "" if e.get("score") is None else e["score"],
                            (e.get("extrait") or "").replace("\t", " ").replace("\n", " ¶ ")])


if __name__ == "__main__":
    main()
