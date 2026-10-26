#!/usr/bin/env python3
"""Comparaison des versions successives des travaux de l'auteur.

Versions : « nov 2022 » (pièce entière), « Harmattan mars 2023 » (vv. 1-946),
« Harmattan 2023 » (deux fichiers, version de référence). Chaque version est extraite
avec le même analyseur que `extraire_travaux.py`, puis on recense, pour chaque version
ancienne, les commentaires, notes, entrées d'apparat et testimonia qui ne se retrouvent
pas dans la version la plus récente (ni actifs, ni désactivés, ni déplacés), ainsi que les
différences de texte grec vers par vers.

Méthode d'appariement (chaque élément ancien reçoit un statut) :
- commentaires et notes : inclusion des trigrammes de mots de l'ancien texte dans le texte
  récent le plus proche, cherché parmi les éléments du même type, puis de l'autre type (une
  note peut avoir été intégrée au corps du commentaire, ou l'inverse), puis parmi les
  éléments désactivés (lignes commentées « % ») ; les textes courts (moins de 12 mots) sont
  cherchés tels quels (après normalisation) dans tout le texte récent ;
- testimonia : signature (mots grecs et nombres, sans les abréviations latines, qui varient
  d'une version à l'autre : « Gregorius Corinthius » / « Gregor. Corinth. ») comparée aux
  testimonia du même passage (± 2 vers) ;
- apparat : lemme de R (mots grecs de la première leçon) et autorités (noms propres, sigles)
  comparés aux entrées des vers voisins (± 2) ; l'auteur abrège souvent en 2023 la leçon
  corrigée (« δεχόμεσθα R : -μεθα Dindorf »), ce que la comparaison de mots ne voit pas ;
- texte grec : comparaison vers par vers ; un vers présent sous un autre numéro (± 3) est
  classé « numérotation différente » ; les différences sont qualifiées (ponctuation seule,
  accentuation ou esprit seuls, découpage, mots).

Statuts : conservé ; conservé (rédaction abrégée ou modifiée) ; remanié ; intégré au
commentaire / mis en note ; désactivé (commenté) dans la version récente ; réécrit (même
plage, texte largement nouveau) ; absent ; hors du champ de la version récente.

Sorties (edition/donnees/travaux_anterieurs/) :
  comparaison_versions.json   détail complet
  comparaison_versions.tsv    une ligne par élément non conservé à l'identique

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
CONSERVE_ABREGE = "conservé (rédaction abrégée ou modifiée)"


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------

def sans_diacritiques(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def normaliser(s: str) -> str:
    s = sans_diacritiques(s).lower().replace("ς", "σ")
    s = re.sub(r"[’'ʼ᾽᾿`]", "'", s)
    return re.sub(r"\s+", " ", s).strip()


def mots(s: str) -> list:
    return re.findall(r"\w+", normaliser(s))


def mots_grecs(s: str, mini: int = 2) -> list:
    return [m for m in re.findall(r"[Ͱ-Ͽἀ-῿]+", normaliser(s)) if len(m) >= mini]


def nombres(s: str) -> list:
    return re.findall(r"\d+[a-z]?", s or "")


def noms_propres(s: str) -> set:
    """Autorités et sigles : mots latins à majuscule initiale (Brunck, Suid, PSI…) ; R et M
    avec leurs exposants sont ramenés à R et M."""
    s = re.sub(r"\bR[ᵃᵖᶜ²\^()\w]*", "R ", s or "")
    s = re.sub(r"\bSchol\b\.?", "Σ", s)      # « Schol. » (2022) = « Σ » (2023)
    noms = set(re.findall(r"\b[A-Z][A-Za-zäöüéèëï\-]+|\bR\b|\bM\b|Σ", s))
    return noms - {"Bibi"} | ({"Bibi"} if "Bibi" in s else set())


def reperes(s: str) -> set:
    """Repères stables d'une référence : nombres, chiffres romains, noms propres latins."""
    s = s or ""
    r = set(re.findall(r"\d+", s))
    r |= {x for x in re.findall(r"\b[IVXLC]{2,}\b", s)}
    r |= {sans_diacritiques(x).lower() for x in re.findall(r"\b[A-ZÀ-Ý][a-zà-ÿ]{2,}", s)}
    return r - {"dans", "voir", "confer", "cf", "le", "la", "les", "tome", "fragment", "fr", "chez",
                "edition", "livre", "chapitre", "vers", "ses", "son", "sa"}


def bardeaux(s: str, k: int = 3) -> set:
    m = mots(s)
    if len(m) < k:
        return set(m)
    return {" ".join(m[i:i + k]) for i in range(len(m) - k + 1)}


def inclusion(a: set, b: set) -> float:
    return len(a & b) / len(a) if a else 0.0


def premier_vers(plage):
    m = re.search(r"\d+", plage or "")
    return int(m.group()) if m else None


class Index:
    """Index inversé de trigrammes : meilleur candidat par inclusion de l'ancien texte."""

    def __init__(self, elements: list, cle_texte="texte"):
        self.el = elements
        self.inv = defaultdict(set)
        for i, e in enumerate(elements):
            for x in bardeaux(e.get(cle_texte, "")):
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
        # départage stable des ex-aequo (le premier élément dans l'ordre du texte) : sans lui,
        # le résultat dépendrait de l'ordre d'itération des ensembles (hachage aléatoire)
        i, n = min(c.items(), key=lambda kv: (-kv[1], kv[0]))
        return self.el[i], n / len(s)


# ---------------------------------------------------------------------------
# Collecte des éléments comparables d'une extraction
# ---------------------------------------------------------------------------

def collecter(res: dict) -> dict:
    out = {"commentaire": [], "note": [], "apparat": [], "testimonia": [],
           "commentaire_desactive": [], "note_desactivee": [], "apparat_desactive": [],
           "testimonia_desactive": [], "grec": {}, "francais": {}}
    for g in res["groupes"]:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                out["commentaire"].append({"id": c["id"], "plage": c["plage"], "lemme": c["lemme"],
                                           "texte": c["texte"], "groupe": g["id"],
                                           "complet": " ".join([c["texte"]] + [x["texte"] for x in
                                                                               c.get("desactive_interne") or []])})
                for n in c["notes"]:
                    out["note"].append({"id": n["id"], "plage": c["plage"], "numero": n["numero"],
                                        "texte": n["texte"], "commentaire": c["id"], "groupe": g["id"],
                                        "complet": " ".join([n["texte"]] + [x["texte"] for x in
                                                                            n.get("desactive_interne") or []])})
                if c.get("desactive_interne"):
                    out["commentaire_desactive"].append({
                        "plage": c["plage"], "groupe": g["id"],
                        "texte": " ".join(x["texte"] for x in c["desactive_interne"])})
                for n in c["notes"]:
                    if n.get("desactive_interne"):
                        out["note_desactivee"].append({
                            "plage": c["plage"], "groupe": g["id"],
                            "texte": " ".join(x["texte"] for x in n["desactive_interne"])})
            for t in g[cote]["testimonia"]:
                out["testimonia"].append({"id": t["id"], "plage": t["plage"], "texte": t["texte"],
                                          "cote": cote, "groupe": g["id"]})
                # parties commentées à l'intérieur d'une macro active (fragments réunis : une
                # entrée peut être commentée sur plusieurs lignes)
                if t.get("desactive_interne"):
                    out["testimonia_desactive"].append({
                        "plage": t["plage"], "groupe": g["id"],
                        "texte": " ".join(x["texte"] for x in t["desactive_interne"])})
            for d in g[cote]["desactives"]:
                t = {"commentaire": "commentaire_desactive", "note": "note_desactivee",
                     "apparat": "apparat_desactive", "testimonia": "testimonia_desactive"}.get(d["type"])
                if t:
                    txt = d.get("texte", "")
                    if d["type"] == "commentaire" and d.get("args"):
                        txt = " ".join(d["args"][1:])
                    plage = d["args"][0] if d.get("args") else ""
                    if d["type"] == "note" and g.get("vers"):
                        # l'argument d'une \note est son numéro : on prend les vers du groupe
                        plage = "%s-%s" % (g["vers"][0], g["vers"][1])
                    out[t].append({"plage": plage, "texte": txt, "groupe": g["id"]})
        for a in g["grec"]["apparat"]:
            for sgm in a["segments"]:
                for e in sgm["entrees"]:
                    lem = e["lecons"][0]["lecon"] if e["lecons"] else ""
                    autres = " ".join(l["texte"] for l in e["lecons"][1:])
                    retenues = " ; ".join(l["lecon"] for l in e["lecons"] if l["retenue"])
                    if not retenues and len(e["lecons"]) > 1 and not (e["lecons"][-1]["attribution"] or "").strip():
                        # dernière leçon sans autorité ni \lecon : proposition de l'auteur non signée
                        # (« … Ellebodius : (Κλεισθ.) (642-3) », nov. 2022)
                        retenues = e["lecons"][-1]["lecon"]
                    out["apparat"].append({"id": a["id"], "vers": sgm["vers"], "debut": sgm["debut"],
                                           "texte": e["texte"], "lemme": lem, "autres": autres,
                                           "retenues": retenues, "groupe": g["id"]})
            # entrées commentées à l'intérieur d'une macro active (« \apparat{417}{%μορμολύκεια R :
            # \lecon{μορμολυκεῖα} Dindorf (1830) \espApp … ») : désactivées, non absentes
            if a.get("desactive_interne"):
                out["apparat_desactive"].append({
                    "plage": a["plage"], "groupe": g["id"], "id": a["id"],
                    "texte": " ".join(x["texte"] for x in a["desactive_interne"])})
        for l in g["grec"]["lignes"]:
            if l["vers"] is not None:
                out["grec"].setdefault(l["vers"], []).append(l["texte"])
                out.setdefault("personnages", {}).setdefault(l["vers"], []).append(l["personnage"] or "∅")
        for l in g["francais"]["lignes"]:
            if l["vers"] is not None:
                out["francais"].setdefault(l["vers"], []).append(l["texte"])
    return out


# ---------------------------------------------------------------------------
# Comparaisons par type
# ---------------------------------------------------------------------------

def comparer_textes(A, R, typ, autre, dans_plage, res):
    """Commentaires et notes."""
    idx_meme = Index(R[typ])
    idx_autre = Index(R[autre])
    des = "commentaire_desactive" if typ == "commentaire" else "note_desactivee"
    idx_des = Index(R[des] + R["note_desactivee" if typ == "commentaire" else "commentaire_desactive"])
    idx_complet = Index(R[typ] + R[autre], cle_texte="complet")
    # « articles » récents : commentaire + ses notes (une note ancienne peut avoir été répartie
    # entre le corps du commentaire et une note)
    notes_de = defaultdict(list)
    for n in R["note"]:
        notes_de[n["commentaire"]].append(n["texte"])
    articles = [{"id": c["id"], "plage": c["plage"], "texte": " ".join([c["texte"]] + notes_de[c["id"]])}
                for c in R["commentaire"]]
    tout_recent = " | ".join(normaliser(x["texte"]) for k in (typ, autre, "commentaire_desactive",
                                                              "note_desactivee") for x in R[k])
    plages_recentes = defaultdict(list)
    for x in R[typ]:
        plages_recentes[re.sub(r"\W", "", x.get("plage", ""))].append(x)
    st = Counter()
    for e in A[typ]:
        if not e["texte"].strip():
            continue
        m, sc = idx_meme.meilleur(e["texte"])
        if sc >= 0.9:
            st["conservé"] += 1
            continue
        if len(mots(e["texte"])) < 12 and normaliser(e["texte"]).strip(" .") in tout_recent:
            st["conservé"] += 1
            continue
        m2, sc2 = idx_autre.meilleur(e["texte"])
        if sc2 >= 0.6 and sc2 > sc:
            statut = "intégré au commentaire" if typ == "note" else "mis en note"
            st[statut] += 1
            res["elements"].append({"type": typ, "statut": statut, "plage": e["plage"],
                                    "id_ancien": e["id"], "id_recent": m2["id"], "score": round(sc2, 2),
                                    "extrait": e["texte"][:300]})
            continue
        if sc >= 0.6:
            st["remanié"] += 1
            if sc < 0.75:
                res["elements"].append({"type": typ, "statut": "remanié", "plage": e["plage"],
                                        "id_ancien": e["id"], "id_recent": m["id"], "score": round(sc, 2),
                                        "extrait": e["texte"][:300]})
            continue
        mc, scc = idx_complet.meilleur(e["texte"])
        if scc >= 0.75 and mc is not None:
            # texte retrouvé dans un élément récent, parties désactivées (%) comprises : abrégé si
            # son début est resté actif, sinon entièrement désactivé
            debut_txt = " ".join(e["texte"].split()[:10])
            if inclusion(bardeaux(debut_txt), bardeaux(mc["texte"])) >= 0.8:
                statut = "abrégé (partie désactivée dans la version récente)"
                st["abrégé (partie désactivée)"] += 1
            else:
                statut = "désactivé (commenté) dans la version récente"
                st["désactivé"] += 1
            res["elements"].append({"type": typ, "statut": statut,
                                    "plage": e["plage"], "id_ancien": e["id"], "id_recent": mc["id"],
                                    "score": round(scc, 2), "extrait": e["texte"][:300]})
            continue
        md, scd = idx_des.meilleur(e["texte"])
        if scd >= 0.6:
            st["désactivé"] += 1
            res["elements"].append({"type": typ, "statut": "désactivé (commenté) dans la version récente",
                                    "plage": e["plage"], "id_ancien": e["id"], "id_recent": None,
                                    "score": round(scd, 2), "extrait": e["texte"][:300]})
            continue
        # note ou commentaire bref reformulé : tous ses repères (nombres, chiffres romains, noms
        # propres) se retrouvent dans un élément récent de même plage (± 2 vers)
        rep = reperes(e["texte"])
        if len(mots(e["texte"])) <= 80 and len(rep) >= 2:
            v0 = premier_vers(e["plage"])
            for k_, lst in (("actif", articles),
                            ("désactivé", R["commentaire_desactive"] + R["note_desactivee"])):
                cand = [x for x in lst if v0 is not None and premier_vers(x.get("plage")) is not None
                        and abs(premier_vers(x.get("plage")) - v0) <= 2 and rep <= reperes(x["texte"])]
                if cand:
                    statut = ("reformulé (repris dans un commentaire ou une note de même plage)"
                              if k_ == "actif" else "désactivé (reformulé) dans la version récente")
                    st[statut] += 1
                    res["elements"].append({"type": typ, "statut": statut, "plage": e["plage"],
                                            "id_ancien": e["id"], "id_recent": cand[0].get("id"),
                                            "score": None, "extrait": e["texte"][:300]})
                    break
            else:
                cand = None
            if cand:
                continue
        statut = "absent" if dans_plage(e["plage"]) else "hors du champ de la version récente"
        meme = plages_recentes.get(re.sub(r"\W", "", e["plage"]))
        if statut == "absent" and meme and typ == "commentaire":
            statut, m = "réécrit (même plage, texte largement nouveau)", meme[0]
        elif statut == "absent" and m is not None and sc >= 0.3 and \
                re.sub(r"\W", "", m.get("plage", "")) == re.sub(r"\W", "", e["plage"]):
            statut = "réécrit (même plage, texte largement nouveau)"
        st[statut] += 1
        res["elements"].append({"type": typ, "statut": statut, "plage": e["plage"],
                                "id_ancien": e["id"], "id_recent": m["id"] if m else None,
                                "score": round(max(sc, sc2), 2), "longueur": len(e["texte"]),
                                "extrait": e["texte"][:600]})
    res["stats"][typ] = dict(st)


def signature_test(t: str) -> set:
    return set(mots_grecs(t, 3)) | set(nombres(t))


def comparer_testimonia(A, R, dans_plage, res):
    par_vers = defaultdict(list)
    for x in R["testimonia"]:
        v = premier_vers(x["plage"])
        if v is not None:
            par_vers[v].append(x)
    des_par_vers = defaultdict(list)
    for x in R["testimonia_desactive"]:
        v = premier_vers(x["plage"])
        if v is not None:
            des_par_vers[v].append(x)
    st = Counter()
    for e in A["testimonia"]:
        if not e["texte"].strip():
            continue
        v = premier_vers(e["plage"])
        sig = signature_test(e["texte"])
        best, sc = None, 0.0
        for d in range(-2, 3):
            for c in par_vers.get((v or -99) + d, []):
                x = inclusion(sig, signature_test(c["texte"]))
                if x > sc:
                    best, sc = c, x
        if sc >= 0.7:
            exact = inclusion(bardeaux(e["texte"]), bardeaux(best["texte"])) >= 0.9
            st["conservé" if exact else CONSERVE_ABREGE] += 1
            continue
        bestd, scd = None, 0.0
        for d in range(-2, 3):
            for c in des_par_vers.get((v or -99) + d, []):
                x = inclusion(sig, signature_test(c["texte"]))
                if x > scd:
                    bestd, scd = c, x
        if sc >= 0.4 and sc >= scd:
            st["remanié"] += 1
            res["elements"].append({"type": "testimonia", "statut": "remanié", "plage": e["plage"],
                                    "id_ancien": e["id"], "id_recent": best["id"], "score": round(sc, 2),
                                    "extrait": e["texte"][:300], "recent": best["texte"][:300]})
            continue
        if scd >= 0.6:
            st["désactivé"] += 1
            res["elements"].append({"type": "testimonia", "statut": "désactivé (commenté) dans la version récente",
                                    "plage": e["plage"], "id_ancien": e["id"], "id_recent": None,
                                    "score": round(scd, 2), "extrait": e["texte"][:300]})
            continue
        statut = "absent" if dans_plage(e["plage"]) else "hors du champ de la version récente"
        st[statut] += 1
        res["elements"].append({"type": "testimonia", "statut": statut, "plage": e["plage"],
                                "id_ancien": e["id"], "id_recent": best["id"] if best else None,
                                "score": round(sc, 2), "extrait": e["texte"][:300]})
    res["stats"]["testimonia"] = dict(st)


def comparer_apparat(A, R, dans_plage, res):
    par_vers = defaultdict(list)
    for e in R["apparat"]:
        if e["debut"] is not None:
            par_vers[e["debut"]].append(e)
    idx_des = Index(R["apparat_desactive"])
    des_par_vers = defaultdict(list)
    for x in R["apparat_desactive"]:
        v = premier_vers(x.get("plage"))
        if v is not None:
            des_par_vers[v].append(x)
    idx_tout = Index(R["apparat"])
    st = Counter()
    for e in A["apparat"]:
        lem = set(mots_grecs(e["lemme"]))
        lem_brut = e["lemme"]
        aut = noms_propres(e["texte"]) - {"R"}
        cands = [x for d in range(-2, 3) for x in par_vers.get((e["debut"] or -99) + d, [])]
        best, sc, detail = None, 0.0, ""
        sa = bardeaux(e["texte"], 2)
        for c in cands:
            v_txt = inclusion(sa, bardeaux(c["texte"], 2))
            l2 = set(mots_grecs(c["lemme"]))
            v_lem = inclusion(lem, l2) if lem else (1.0 if not l2 else 0.0)
            if lem and l2 and v_lem < 1.0:
                # lemme récent abrégé (« μυ- », « ἑπτ. οὖσ. ») ou raccourci (« δὴ » pour
                # « νῦν τότε δὴ ») : préfixes et inclusion inverse
                v_lem = max(v_lem, lemme_abrege(lem_brut, c["lemme"]), inclusion(l2, lem))
            a2 = noms_propres(c["texte"]) - {"R"}
            v_aut = inclusion(aut, a2) if aut else 1.0
            v = max(v_txt, 0.5 * v_lem + 0.5 * v_aut if v_lem >= 0.5 else 0.0)
            if v > sc:
                best, sc = c, v
                detail = "texte" if v == v_txt else "lemme+autorités"
        if sc < 0.8:
            m, v = idx_tout.meilleur(e["texte"])
            if m is not None and v > sc and v >= 0.8:
                best, sc, detail = m, v, "texte (autre vers)"
        if sc < 0.5 and aut:
            # notation récrite (« εἰσέφερε Rᵃᶜ : ἥ ἔφερε Rᵖᶜ (cum η supra ει scripto…) » devenu
            # « εἰ^(η)⟦σ⟧έφερε Rᵖᶜ ») : mêmes autorités et une même leçon variante
            var = set(mots_grecs(e.get("autres", ""), 3))
            for c in cands:
                if aut <= (noms_propres(c["texte"]) - {"R"}) and var & set(mots_grecs(c["texte"], 3)):
                    best, sc, detail = c, 0.5, "autorités+variante"
                    break
        if sc < 0.5 and e.get("retenues"):
            # même leçon retenue, autorités ou rédaction changées (« (Κλεισθ.) (642-3) » sans
            # nom en 2022, signé Bibi en 2023, les autres attributions étant commentées)
            for c in cands:
                if c.get("retenues") and normaliser(c["retenues"]) == normaliser(e["retenues"]):
                    best, sc, detail = c, 0.5, "leçon retenue"
                    break
        if sc >= 0.8:
            st["conservé" if detail.startswith("texte") else CONSERVE_ABREGE] += 1
            continue
        if sc >= 0.5:
            st["remanié"] += 1
            res["elements"].append({"type": "apparat", "statut": "remanié", "plage": e["vers"],
                                    "id_ancien": e["id"], "id_recent": best["id"], "score": round(sc, 2),
                                    "extrait": e["texte"][:300], "recent": best["texte"][:300]})
            continue
        md, scd = idx_des.meilleur(e["texte"])
        if scd < 0.6:
            # entrée désactivée et récrite (« πῶς Schol. Plat. Theag. » → « πῶς Σ Theag. ») :
            # lemme et autorités, parmi les parties commentées des vers voisins
            for c in (x for d in range(-2, 3) for x in des_par_vers.get((e["debut"] or -99) + d, [])):
                v_lem = inclusion(lem, set(mots_grecs(c["texte"]))) if lem else 0.0
                v_aut = inclusion(aut, noms_propres(c["texte"]) - {"R"}) if aut else 1.0
                v = 0.5 * v_lem + 0.5 * v_aut if v_lem >= 0.5 else 0.0
                if v > scd:
                    md, scd = c, v
        if scd >= 0.6:
            st["désactivé"] += 1
            res["elements"].append({"type": "apparat", "statut": "désactivé (commenté) dans la version récente",
                                    "plage": e["vers"], "id_ancien": e["id"],
                                    "id_recent": (md or {}).get("id"),
                                    "score": round(scd, 2), "extrait": e["texte"][:300]})
            continue
        # information passée de l'apparat aux testimonia (« τὸ πέος Suid. λ 63, π 987 », v. 142)
        sig = signature_test(e["texte"])
        if len(sig) >= 3:
            vt, mt = 0.0, None
            for t in R["testimonia"]:
                v0 = premier_vers(t["plage"])
                if v0 is not None and e["debut"] is not None and abs(v0 - e["debut"]) <= 2:
                    x = inclusion(sig, signature_test(t["texte"]))
                    if x > vt:
                        vt, mt = x, t
            if vt >= 0.7:
                st["transféré dans les testimonia"] += 1
                res["elements"].append({"type": "apparat", "statut": "transféré dans les testimonia",
                                        "plage": e["vers"], "id_ancien": e["id"], "id_recent": mt["id"],
                                        "score": round(vt, 2), "extrait": e["texte"][:300],
                                        "recent": mt["texte"][:300]})
                continue
        statut = "absent" if dans_plage(e["vers"]) else "hors du champ de la version récente"
        st[statut] += 1
        res["elements"].append({"type": "apparat", "statut": statut, "plage": e["vers"],
                                "id_ancien": e["id"], "id_recent": best["id"] if best else None,
                                "score": round(sc, 2), "extrait": e["texte"][:300],
                                "recent": best["texte"][:300] if best else ""})
    res["stats"]["apparat"] = dict(st)


def lemme_abrege(ancien: str, recent: str) -> float:
    """Part des mots grecs du lemme ancien que couvre un lemme récent abrégé : un mot récent
    terminé par « - » ou « . » vaut pour tout mot ancien qui commence comme lui."""
    a = mots_grecs(ancien, 1)
    abr = [normaliser(m).rstrip("-.") for m in (recent or "").split() if re.search(r"[Ͱ-Ͽἀ-῿][-.]$", m)]
    entiers = set(mots_grecs(re.sub(r"\S+[-.](?=\s|$)", " ", recent or ""), 1))
    if not a or not abr:
        return 0.0
    ok = sum(1 for m in a if m in entiers or any(m.startswith(x) for x in abr if x))
    return ok / len(a)


def norm_grec(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[’'ʼ᾿]", "᾽", s)
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


def nature_difference(a: str, b: str) -> str:
    sa, sb = a.replace(" | ", " "), b.replace(" | ", " ")
    if sa == sb:
        return "découpage (antilabè/répartition)"
    lettres = lambda s: re.sub(r"[^\w]", "", s)
    if lettres(sa) == lettres(sb):
        return "ponctuation"
    if lettres(normaliser(sa)) == lettres(normaliser(sb)):
        return "accentuation, esprit ou majuscule"
    return "mots"


def comparer_grec(A, R, plage_ancien, res):
    diffs, renum = [], []
    communs = sorted(set(A["grec"]) & set(R["grec"]))
    seulement_ancien = sorted(set(A["grec"]) - set(R["grec"]))
    seulement_recent = sorted(set(R["grec"]) - set(A["grec"]))
    if plage_ancien:
        seulement_recent = [v for v in seulement_recent if plage_ancien[0] <= v <= plage_ancien[1]]
    # vers numérotés différemment : même texte sous un numéro voisin
    textes_r = {v: normaliser(" ".join(t)) for v, t in R["grec"].items()}
    textes_a = {v: normaliser(" ".join(t)) for v, t in A["grec"].items()}
    renum_a, renum_r = set(), set()
    for v in seulement_ancien:
        for d in (-1, 1, -2, 2, -3, 3):
            w = v + d
            if w in seulement_recent and w not in renum_r and \
                    difflib.SequenceMatcher(None, textes_a[v], textes_r[w]).ratio() >= 0.9:
                renum.append({"ancien": v, "recent": w, "texte": " | ".join(A["grec"][v])})
                renum_a.add(v)
                renum_r.add(w)
                break
    lettres = lambda s: re.sub(r"[^\w]", "", norm_grec(s))
    absorbes = set()
    for v in communs:
        a = norm_grec(" | ".join(A["grec"][v]))
        b = norm_grec(" | ".join(R["grec"][v]))
        if a == b:
            continue
        # lignes réparties autrement entre vers voisins (vers sur deux lignes, partie a/b
        # rattachée au vers précédent ou suivant) : le texte des vv. v-1 à v+1 est identique
        fen = [w for w in (v - 1, v, v + 1)]
        ua = "".join(lettres(" ".join(A["grec"].get(w, []))) for w in fen)
        ub = "".join(lettres(" ".join(R["grec"].get(w, []))) for w in fen)
        if nature_difference(a, b) == "mots" and ua == ub:
            nat = "répartition des lignes entre vers voisins"
            absorbes.update(w for w in fen if w not in R["grec"] or w not in A["grec"])
            diffs.append({"vers": v, "ancien": a, "recent": b, "nature": nat, "differences": ""})
            res["elements"].append({"type": "texte_grec", "statut": "différent (%s)" % nat, "plage": str(v),
                                    "id_ancien": None, "id_recent": None, "score": None,
                                    "extrait": "%s ‖ %s" % (a[:140], b[:140])})
            continue
        nat = nature_difference(a, b)
        detail = diff_mots(a.replace(" | ", " "), b.replace(" | ", " ")) if nat != "découpage (antilabè/répartition)" else ""
        diffs.append({"vers": v, "ancien": a, "recent": b, "nature": nat, "differences": detail})
        res["elements"].append({"type": "texte_grec", "statut": "différent (%s)" % nat, "plage": str(v),
                                "id_ancien": None, "id_recent": None, "score": None,
                                "extrait": (detail or nat)[:300]})
    for r_ in renum:
        res["elements"].append({"type": "texte_grec", "statut": "numérotation différente",
                                "plage": "%d → %d" % (r_["ancien"], r_["recent"]), "id_ancien": None,
                                "id_recent": None, "score": None, "extrait": r_["texte"][:300]})
    res["texte_grec"] = {
        "vers_communs": len(communs), "vers_differents": len(diffs),
        "natures": dict(Counter(d["nature"] for d in diffs)),
        "renumerotations": renum,
        "seulement_ancien": [v for v in seulement_ancien if v not in renum_a and v not in absorbes],
        "seulement_recent": [v for v in seulement_recent if v not in renum_r and v not in absorbes],
        "differences": diffs}
    trad = sum(1 for v in set(A["francais"]) & set(R["francais"])
               if re.sub(r"\s+", " ", " ".join(A["francais"][v])) != re.sub(r"\s+", " ", " ".join(R["francais"][v])))
    res["stats"]["traduction_vers_modifies"] = trad
    res["stats"]["texte_grec_vers_differents"] = len(diffs)
    res["stats"]["texte_grec_natures"] = dict(Counter(d["nature"] for d in diffs))
    res["stats"]["texte_grec_renumerotations"] = len(renum)


def comparer_personnages(A, R, res):
    """Attributions des répliques : suite des locuteurs de chaque vers commun aux deux versions
    (une ligne par partie de vers ; les répétitions consécutives du même locuteur sont fondues,
    pour ne pas compter les vers simplement redécoupés)."""
    def suite(ps):
        out = []
        for p in ps:
            if not out or out[-1] != p:
                out.append(p)
        return out
    PA, PR = A.get("personnages", {}), R.get("personnages", {})
    diffs = []
    for v in sorted(set(PA) & set(PR)):
        a, b = suite(PA[v]), suite(PR[v])
        if a != b:
            diffs.append({"vers": v, "ancien": a, "recent": b})
    # regroupement des vers consécutifs portant le même changement
    blocs = []
    for d in diffs:
        cle = (tuple(d["ancien"]), tuple(d["recent"]))
        if blocs and blocs[-1]["cle"] == cle and d["vers"] == blocs[-1]["fin"] + 1:
            blocs[-1]["fin"] = d["vers"]
        else:
            blocs.append({"cle": cle, "debut": d["vers"], "fin": d["vers"]})
    for b in blocs:
        plage = str(b["debut"]) if b["debut"] == b["fin"] else "%d-%d" % (b["debut"], b["fin"])
        res["elements"].append({"type": "personnage", "statut": "attribution différente", "plage": plage,
                                "id_ancien": None, "id_recent": None, "score": None,
                                "extrait": "%s → %s" % (" / ".join(b["cle"][0]), " / ".join(b["cle"][1]))})
    res["personnages"] = {"vers_differents": len(diffs), "blocs": len(blocs), "differences": diffs}
    res["stats"]["personnages_vers_differents"] = len(diffs)
    res["stats"]["personnages_blocs"] = len(blocs)


def comparer(ancien: dict, recent: dict, nom: str, plage_ancien=None, plage_recent=None) -> dict:
    A, R = collecter(ancien), collecter(recent)
    res = {"version": nom, "elements": [], "stats": {}}

    def dans_plage(plage: str) -> bool:
        if plage_recent is None:
            return True
        v = premier_vers(plage)
        return v is None or plage_recent[0] <= v <= plage_recent[1]

    comparer_textes(A, R, "commentaire", "note", dans_plage, res)
    comparer_textes(A, R, "note", "commentaire", dans_plage, res)
    comparer_testimonia(A, R, dans_plage, res)
    comparer_apparat(A, R, dans_plage, res)
    comparer_grec(A, R, plage_ancien, res)
    comparer_personnages(A, R, res)
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
        print("%-20s groupes %4d  lignes gr. %4d  vers %s-%s  commentaires %3d  notes %3d  apparats %3d"
              % (nom, s["groupes"], s["lignes_grecques"], s["premier_vers"], s["dernier_vers"],
                 s["commentaires"], s["notes"], s["apparats"]))
    recent = extractions["harmattan2023"]
    resultat = {"versions": {cle: {"nom": nom, "fichiers": f, "statistiques": extractions[cle]["statistiques"]}
                             for cle, nom, f in VERSIONS},
                "comparaisons": []}
    for cle, nom, fichiers in VERSIONS[:-1]:
        s = extractions[cle]["statistiques"]
        plage = (s["premier_vers"], s["dernier_vers"])
        r_plage = (recent["statistiques"]["premier_vers"], recent["statistiques"]["dernier_vers"])
        c = comparer(extractions[cle], recent, nom, plage_ancien=plage, plage_recent=r_plage)
        c["plage_version"] = plage
        resultat["comparaisons"].append(c)
        print(nom, json.dumps(c["stats"], ensure_ascii=False))
    with open(os.path.join(sortie, "comparaison_versions.json"), "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
    with open(os.path.join(sortie, "comparaison_versions.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["version", "type", "statut", "plage", "id_ancien", "id_recent_proche", "score",
                    "extrait", "recent"])
        for c in resultat["comparaisons"]:
            for e in c["elements"]:
                w.writerow([c["version"], e["type"], e["statut"], e["plage"], e.get("id_ancien") or "",
                            e.get("id_recent") or "", "" if e.get("score") is None else e["score"],
                            (e.get("extrait") or "").replace("\t", " ").replace("\n", " ¶ "),
                            (e.get("recent") or "").replace("\t", " ").replace("\n", " ¶ ")])


if __name__ == "__main__":
    main()
