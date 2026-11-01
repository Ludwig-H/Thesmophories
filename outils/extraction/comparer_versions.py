#!/usr/bin/env python3
"""Comparaison de tous les états des travaux de l'auteur ; contenus récupérables.

États comparés : toutes les versions de travail du corps de l'édition (texte grec, apparat,
testimonia, traduction, commentaire et notes) conservées sur le Drive de l'auteur — dossier de
travail GCA/ (juillet 2020 - avril 2024), TH/Versions/ et racine de TH/ (série « texte -
traduction - commentaire » de mars-juin 2020), archive de juillet 2020 — et les copies du dépôt
(latex/). Les fichiers identiques octet pour octet (empreinte SHA-256) ne sont analysés qu'une
fois. Version de référence : « Harmattan 2023 » (latex/… vv 1-641 + … vv 642-fin-bis, identiques
à leurs homonymes de GCA/). Introduction, Annexes et Index : versions du Drive (GCA/, plus
récentes et plus complètes) comparées aux copies de latex/.

Abréviations de chemins (comme dans recherche/drive_ressources.md) :
  TH/  = .sources/drive/fichiers/Grec/Aristophane/Thesmophories/
  GCA/ = TH/Grec - commentaire - traduction - apparat/

Pour chaque état distinct : extraction avec l'analyseur de `extraire_travaux.py`, puis
1. comparaison élément par élément avec la référence (méthode ci-dessous, inchangée) ;
2. passages perdus du commentaire et des notes, au mot près : chaque mot d'un commentaire ou
   d'une note de l'état ancien est « couvert » s'il appartient à une suite de mots (4-grammes,
   îlots d'au moins 6 mots) présente dans le commentaire actif de 2023 ; les suites non couvertes
   d'au moins 8 mots (ou l'élément entier, s'il est plus court) sont cherchées dans les parties
   commentées (%) des fichiers de 2023 (→ désactivé), dans les autres parties de l'édition
   (apparat, testimonia, traduction, Introduction, Annexes, Index du Drive → déplacé), parmi les
   commentaires de 2023 par trigrammes ou par mots rares des mêmes vers (→ remanié) ; sinon :
   disparu ;
3. traduction (vers par vers : seules les traductions nettement différentes et les remarques entre
   parenthèses sont retenues), conjectures « Bibi » (conservée, remplacée, désactivée, abandonnée),
   analyses métriques (notation mise à part).
Les contenus perdus sont ensuite regroupés d'un état à l'autre (lignées) : chacun n'est recensé
qu'une fois, sous sa forme la plus récente, avec le premier état qui le contient, le nombre
d'états où il figure et l'état de la filiation principale dont il est absent ; ce qu'une forme
ancienne a en propre est recensé à part (rien ne se perd au dédoublonnage). S'y ajoutent les
parties commentées de 2023 qu'aucun état n'imprime (brouillons, dossiers de travail) et deux
fichiers hors série (note.txt, texte de présentation).

Méthode d'appariement élément par élément (comparaison avec la référence) :
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

Sorties (edition/donnees/travaux_anterieurs/) :
  comparaison_versions.json   inventaire des fichiers, états, comparaisons détaillées
  comparaison_versions.tsv    une ligne par élément non conservé à l'identique, par état
  contenus_recuperables.tsv   contenus absents de la référence, une ligne par lignée

Contrôle de ce tableau sur les fichiers sources : outils/extraction/verifier_recuperables.py.

Usage : python3 outils/extraction/comparer_versions.py [--depot CHEMIN] [--processus N]
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import multiprocessing as mp
import os
import re
import sys
import unicodedata
import zipfile
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extraire_travaux import FICHIERS_2023, extraire  # noqa: E402
from analyse_latex import Source, plage_vers  # noqa: E402

CONSERVE_ABREGE = "conservé (rédaction abrégée ou modifiée)"

# ---------------------------------------------------------------------------
# Catalogue des états
# ---------------------------------------------------------------------------

TH = ".sources/drive/fichiers/Grec/Aristophane/Thesmophories/"
GCA = TH + "Grec - commentaire - traduction - apparat/"
ARCHIVE = TH + "Thesmophories Grec – Traduction – Commentaire  – Apparat.zip"
ARCHIVE_SHA = "b82d2ee689b8"                      # main.tex de l'archive (préfixe SHA-256)
ARCHIVE_LOCAL = ".travail/versions_drive/archive_juillet2020/main.tex"
TTC = TH + "texte - traduction - commentaire"
VTTC = TH + "Versions/texte - traduction - commentaire"
REFERENCE = "2023"


def E(cle, libelle, date, fichiers, nature="complet", filiation="principale", remarque="",
      plage=None):
    return {"cle": cle, "libelle": libelle, "date": date, "fichiers": fichiers, "nature": nature,
            "filiation": filiation, "remarque": remarque, "plage": plage}


# Ordre chronologique. Dates : nom du fichier, date interne (\date, archive), date
# d'enregistrement fiable (2022-2023) ; à défaut, place dans la série d'après les lignes communes
# (voir recherche/travaux_anterieurs.md § 10.1).
ETATS = [
    E("2020-03a", "mars 2020 (avant le 11)", "2020-03", [VTTC + " - Copie.tex"],
      remarque="plus ancien état commenté : ni apparat ni notes ; placé par sa ressemblance avec "
               "la copie du 11 mars"),
    E("2020-03-11", "11 mars 2020", "2020-03-11", [VTTC + " - Copie 11 mars.tex"]),
    E("2020-03-21", "21 mars 2020", "2020-03-21", [VTTC + " 21 mars 2020.tex"]),
    E("2020-03-21b", "21-25 mars 2020", "2020-03-23", [TTC + " 21 mars 2020 - Copie.tex"],
      remarque="identique à TH/Versions/… 25 mars 2020 - Copie.tex ; se place entre le 21 et le "
               "25 mars"),
    E("2020-03-25", "25 mars 2020", "2020-03-25", [VTTC + " 25 mars 2020.tex"]),
    E("2020-03-26", "26 mars 2020", "2020-03-26", [VTTC + " 26 mars 2020.tex"]),
    E("2020-03-27", "27 mars 2020", "2020-03-27", [VTTC + " 27 mars 2020.tex"]),
    E("2020-03-27b", "27 mars 2020 (2)", "2020-03-27", [VTTC + " 27 mars 2020 2.tex"]),
    E("2020-03-28", "28 mars 2020", "2020-03-28", [TTC + " 28 mars 2020.tex"]),
    E("2020-03-29", "29 mars 2020", "2020-03-29", [TTC + " 29 mars 2020.tex"]),
    E("2020-04-11", "11 avril 2020", "2020-04-11", [TTC + " 11 avril 2020.tex"]),
    E("2020-04-12", "12 avril 2020", "2020-04-12", [TTC + " 12 avril 2020.tex"]),
    E("2020-04-19", "19 avril 2020", "2020-04-19", [TTC + " 19 avril 2020.tex"]),
    E("2020-04-25", "25 avril 2020", "2020-04-25", [TTC + " 25 avril 2020.tex"]),
    E("2020-04-30", "30 avril 2020", "2020-04-30", [TTC + " 30 avril 2020.tex"]),
    E("2020-05-02", "2 mai 2020", "2020-05-02", [TH + "Versions/version 2 2 mai.tex"],
      remarque="« version 2 mai.tex » en est une copie réenregistrée en codage 8 bits (grec "
               "remplacé par « ? »), identique par ailleurs"),
    E("2020-05a", "mai 2020 (copie 2)", "2020-05", [TTC + " - Copie (2).tex"]),
    E("2020-05b", "mai 2020 (copie 3)", "2020-05", [TTC + " - Copie (3).tex"]),
    E("2020-06", "mai-juin 2020", "2020-06", [TTC + ".tex"],
      remarque="dernier état de la série « texte - traduction - commentaire »"),
    E("2020-07-03", "3 juillet 2020 (archive)", "2020-07-03", [ARCHIVE_LOCAL],
      remarque="unique fichier de l'archive zip (date interne) ; aucune copie hors de l'archive"),
    E("2020-07-11", "11 juillet 2020", "2020-07-11", [GCA + "copie 11 juillet 2020.tex"]),
    E("2020-07m2", "été 2020 (main2)", "2020-07", [GCA + "main2.tex"], filiation="branche A",
      remarque="branche A (main2 → 1er août → main), issue de l'état du 11 juillet, sans suite"),
    E("2020-07-12", "12 juillet 2020", "2020-07-12", [GCA + "copie 12 juillet 2020.tex"],
      remarque="branche B, celle qui se poursuit ; ne diffère de la copie du 3 août que par une "
               "ligne"),
    E("2020-08-01", "1er août 2020", "2020-08-01", [GCA + "copie 1er aout 2020.tex"],
      filiation="branche A"),
    E("2020-08m", "août 2020 (main)", "2020-08", [GCA + "main.tex"], filiation="branche A"),
    E("2020-08-02", "2 août 2020", "2020-08-02", [GCA + "copie 2 aout 2020.tex"]),
    E("2020-08-03", "3 août 2020", "2020-08-03", [GCA + "copie 3 aout 2020.tex"]),
    E("2020-08a", "août 2020", "2020-08", [GCA + "Aristophane-Thesmophories.tex"]),
    E("2020-08-18", "18 août 2020", "2020-08-18", [GCA + "AT 18 aout 2020.tex"],
      remarque="= GCA/Aristophane-Thesmophories (copie).tex"),
    E("2021-04", "avril 2021", "2021-04", [GCA + "Aristophane-Thesmo avril 2021.tex"],
      remarque="identique à GCA/Aristophane-Thesmo 18 aout 2020.tex ; placé en avril 2021 par "
               "son contenu, plus proche de mai 2021 que de l'état du 18 août 2020"),
    E("2021-05a", "mai 2021 (TH/Versions)", "2021-05", [TH + "Versions/Aristophane-Thesmo mai 2021.tex"]),
    E("2021-05", "mai 2021", "2021-05", [GCA + "Aristophane-Thesmo mai 2021.tex"]),
    E("2021-08", "août 2021", "2021-08", [GCA + "Aristophane-Thesmo aout 2021.tex"]),
    E("2021-08e1", "août 2021, essai 1", "2021-08", [GCA + "Aristophane-Thesmo aout 2021 test.tex"],
      nature="essai de mise en page", filiation="essai"),
    E("2021-08e2", "août 2021, essai 2", "2021-08", [GCA + "Aristophane-Thesmo aout 2021 test 2.tex"],
      nature="essai de mise en page", filiation="essai"),
    E("2021-08e3", "août 2021, essai 3", "2021-08", [GCA + "Aristophane-Thesmo aout 2021 test 3.tex"],
      nature="essai de mise en page", filiation="essai"),
    E("2021-08e4", "août 2021, essai 4", "2021-08", [GCA + "Aristophane-Thesmo aout 2021 test 4.tex"],
      nature="essai de mise en page", filiation="essai"),
    E("2021-08e5", "août 2021, essai 5", "2021-08", [GCA + "Aristophane-Thesmo aout 2021 test 5.tex"],
      nature="essai de mise en page", filiation="essai"),
    E("2021-12s", "août-décembre 2021 (sauvegarde)", "2021-10", [GCA + "Aristophane-Thesmo decembre 2021.tex~"],
      nature="sauvegarde d'éditeur", filiation="sauvegarde",
      remarque="sauvegarde automatique (« ~ ») de l'état de décembre 2021, très voisine d'août 2021"),
    E("2021-12", "décembre 2021", "2021-12", [GCA + "Aristophane-Thesmo decembre 2021.tex"],
      remarque="identique à GCA/Aristophane-Thesmo mai 2022.tex"),
    E("2022-06", "juin 2022", "2022-06", [GCA + "Aristophane-Thesmo juin 2022.tex"],
      remarque="date interne IX 2022 : fichier mis à jour en septembre 2022"),
    E("2022-09", "septembre 2022", "2022-09", [GCA + "Aristophane-Thesmo sept 2022.tex"]),
    E("2022-09v", "septembre 2022 (deux volumes)", "2022-09",
      [GCA + "Aristophane-Thesmo sept 2022 1 vv 1-633.tex", GCA + "Aristophane-Thesmo sept 2022 2 vv 634-1231.tex"],
      nature="variante", filiation="variante", remarque="découpage du précédent en deux fichiers"),
    E("2022-09e", "septembre 2022, essai (vv. 372-698)", "2022-09", [GCA + "Test.tex"],
      nature="essai de mise en page", filiation="essai", plage=(372, 698)),
    E("2022-10", "octobre 2022", "2022-10", [GCA + "Aristophane-Thesmo oct 2022.tex"]),
    E("2022-10p", "octobre 2022 (sauts de page)", "2022-10",
      [GCA + "Aristophane-Thesmo oct 2022  avec page break.tex"], nature="variante", filiation="variante",
      remarque="= … avec page break manuel.tex ; mêmes lignes qu'oct 2022 (sauts de page)"),
    E("2022-11L", "novembre 2022 (latex/)", "2022-11", ["latex/Aristophane-Thesmo nov 2022.tex"],
      remarque="copie du dépôt, antérieure à celle du Drive"),
    E("2022-11", "novembre 2022 (Drive)", "2022-11", [GCA + "Aristophane-Thesmo nov 2022.tex"],
      remarque="postérieure à la copie de latex/ (Σ au lieu de « Schol. », comme en 2023) ; "
               "enregistrée le 22 août 2023"),
    E("2023-03", "mars 2023 (Drive)", "2023-03", [GCA + "Aristophane-Thesmo Harmattan mars 2023.tex"],
      remarque="pièce entière ; enregistré le 22 août 2023"),
    E("2023-03L", "mars 2023 (latex/, tronqué)", "2023-03", ["latex/Aristophane-Thesmo Harmattan mars 2023.tex"],
      nature="partiel", filiation="variante",
      remarque="copie tronquée du précédent (texte grec jusque vers le v. 946)"),
    E("2023-03s", "mars 2023 (sauvegarde)", "2023-03", [GCA + "Aristophane-Thesmo Harmattan mars 2023.tex~"],
      nature="sauvegarde d'éditeur", filiation="sauvegarde"),
    E("2023p", "Harmattan 2023, vol. 2 (état partiel)", "2023", [GCA + "Aristophane-Thesmo Harmattan 2023 vv 642-fin.tex"],
      nature="partiel", filiation="variante", plage=(639, 1231),
      remarque="début du second volume (vv. 639-721 env.), presque identique à l'état final"),
    E(REFERENCE, "Harmattan 2023 (référence)", "2023", list(FICHIERS_2023),
      remarque="= GCA/… vv 1-641.tex et GCA/… vv 642-fin-bis.tex"),
    E("2024-04-13", "copie du 13 avril 2024", "2024-04-13",
      [FICHIERS_2023[0], GCA + "Aristophane-Thesmo Harmattan 2023 vv 642-fin-copie13-4-2024.tex"],
      nature="variante", filiation="variante",
      remarque="second volume seulement (le premier est celui de 2023) ; bascules de macros"),
]
PAR_CLE = {e["cle"]: e for e in ETATS}
RANG = {e["cle"]: i for i, e in enumerate(ETATS)}

INTRO_ANNEXES = [
    ("introduction", "Introduction", GCA + "Aristophane-Thesmo Introduction.tex", "latex/Aristophane-Thesmo Introduction.tex"),
    ("annexes", "Annexes", GCA + "Aristophane-Thesmo Annexes.tex", "latex/Aristophane-Thesmo Annexes.tex"),
    ("index", "Index", GCA + "Aristophane-Thesmo Index.tex", "latex/Aristophane-Thesmo Index.tex"),
]

# fichiers sans état propre (rôle dans l'inventaire)
ROLES = [
    (r"/Articles/|Article août 2020\.tex$", "article de l'auteur (hors champ : drive_ressources § 8.2)"),
    (r"Introduction\.tex$|Annexes\.tex$|Index\.tex$", "introduction, annexes ou index (comparés à part)"),
    (r"thesm\.tex$", "texte grec seul, page de droite en grec (gabarit antérieur à la traduction)"),
    (r"1er mars 2020\)/main\.tex$", "texte grec seul, sans apparat ni commentaire (1er mars 2020)"),
    (r"myEdition\.tex$", "essai de mise en page (février 2020)"),
    (r"Edition 4 pages Ravennas", "travail de Gemini (exclu)"),
    (r"version 2 mai\.tex$", "copie dégradée de « version 2 2 mai.tex » (codage 8 bits, grec perdu)"),
]


def abreger(rel: str) -> str:
    if rel == ARCHIVE_LOCAL:
        return "TH/" + os.path.basename(ARCHIVE) + ":main.tex"
    if rel.startswith(GCA):
        return "GCA/" + rel[len(GCA):]
    if rel.startswith(TH):
        return "TH/" + rel[len(TH):]
    return rel


def sha(chemin: str) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 16), b""):
            h.update(bloc)
    return h.hexdigest()


def preparer_archive(depot: str):
    """main.tex de l'archive de juillet 2020, copié dans .travail/ (non versionné)."""
    cible = os.path.join(depot, ARCHIVE_LOCAL)
    if os.path.exists(cible) and sha(cible).startswith(ARCHIVE_SHA):
        return True
    src = os.path.join(depot, ARCHIVE)
    if not os.path.exists(src):
        return False
    with zipfile.ZipFile(src) as z:
        donnees = z.read("main.tex")
    if not hashlib.sha256(donnees).hexdigest().startswith(ARCHIVE_SHA):
        return False
    os.makedirs(os.path.dirname(cible), exist_ok=True)
    with open(cible, "wb") as f:
        f.write(donnees)
    return True


def inventaire(depot: str) -> list:
    """Tous les .tex de TH/ et de latex/ (+ archive) : empreinte, état, doublons, rôle."""
    chemins = []
    for racine, _, noms in os.walk(os.path.join(depot, TH)):
        for n in noms:
            if re.search(r"\.tex~?$", n):
                chemins.append(os.path.relpath(os.path.join(racine, n), depot))
    chemins += ["latex/" + n for n in os.listdir(os.path.join(depot, "latex")) if n.endswith(".tex")]
    if os.path.exists(os.path.join(depot, ARCHIVE_LOCAL)):
        chemins.append(ARCHIVE_LOCAL)
    chemins.sort()
    etat_de = {}
    for e in ETATS:
        for f in e["fichiers"]:
            etat_de.setdefault(f, e["cle"])
    infos = []
    par_sha = defaultdict(list)
    for rel in chemins:
        b = open(os.path.join(depot, rel), "rb").read()
        h = hashlib.sha256(b).hexdigest()
        par_sha[h].append(rel)
        infos.append({"fichier": abreger(rel), "chemin": rel, "octets": len(b), "lignes": b.count(b"\n"),
                      "sha256": h[:16], "_h": h, "nul": not b.strip(b"\x00")})
    for x in infos:
        rel = x["chemin"]
        if rel in etat_de:
            x["etat"] = etat_de[rel]
            x["role"] = "état analysé"
        else:
            jumeaux = [r for r in par_sha[x["_h"]] if r != rel and r in etat_de]
            if x["nul"]:
                x["etat"], x["role"] = None, "fichier corrompu (octets nuls) : à récupérer de nouveau sur le Drive"
            elif jumeaux:
                x["etat"] = etat_de[jumeaux[0]]
                x["role"] = "doublon (identique octet pour octet) de " + abreger(jumeaux[0])
            else:
                x["etat"] = None
                x["role"] = next((r for m, r in ROLES if re.search(m, rel)), "non classé")
                autres = [abreger(r) for r in par_sha[x["_h"]] if r != rel]
                if autres:
                    x["role"] += " ; identique à " + ", ".join(autres)
        del x["_h"], x["nul"]
    return infos


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


# Sigles des états anciens rapportés à ceux de 2023 pour la comparaison (macro \\PsiCinq :
# « POxy-1176 %P50 » ; les autres d'après les vers couverts : P13 v. 287, P14 v. 743, P68 v. 1187)
SIGLES_ANCIENS = [(r"\bMu2(?=[ᵃᵖᶜ\b\W]|$)", "M"), (r"\bP13\b", "PSI-1194"), (r"\bP14\b", "POxy-3839"),
                  (r"\bP68\b", "POxy-3840"), (r"\bP4935\b", "POxy-4935"), (r"\bP50\b", "POxy-1176"),
                  (r"\bSchol\b\.?", "Σ"), (r"\b[Ss]ch\.(?=[\s,;:)]|$)", "Σ")]


def sigles_modernes(s: str) -> str:
    for motif, rempl in SIGLES_ANCIENS:
        s = re.sub(motif, rempl, s or "")
    return s or ""


def noms_propres(s: str) -> set:
    """Autorités et sigles : mots latins à majuscule initiale (Brunck, Suid, PSI…) ; R et M
    avec leurs exposants sont ramenés à R et M."""
    s = re.sub(r"\bR[ᵃᵖᶜ²\^()\w]*", "R ", sigles_modernes(s))
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
    m = re.search(r"\d+", str(plage or ""))
    return int(m.group()) if m else None


def court(s: str, n: int) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


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

def plage_groupe(plage: str, g: dict) -> str:
    """Plage d'un élément, ou à défaut (argument vide ou fautif : « \\ligneApp κάρισος ») vers du
    groupe, entre crochets."""
    if re.search(r"\d", plage or "") or not g.get("vers"):
        return plage
    a, b = g["vers"]
    return "[%s]" % a if a == b else "[%s-%s]" % (a, b)


def collecter(res: dict, noms_fichiers: dict | None = None) -> dict:
    """Éléments comparables d'une extraction ; chaque élément porte son lieu (fichier abrégé,
    ligne de la source)."""
    noms_fichiers = noms_fichiers or {}
    out = {"commentaire": [], "note": [], "apparat": [], "testimonia": [],
           "commentaire_desactive": [], "note_desactivee": [], "apparat_desactive": [],
           "testimonia_desactive": [], "grec": {}, "francais": {}, "lieu_grec": {}, "lieu_francais": {}}

    def lieu(g, x):
        return noms_fichiers.get(g.get("fichier"), g.get("fichier")), (x or {}).get("ligne_source")

    for g in res["groupes"]:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                f, l = lieu(g, c)
                c_plage = plage_groupe(c["plage"], g)
                out["commentaire"].append({"id": c["id"], "plage": c_plage, "lemme": c["lemme"],
                                           "texte": c["texte"], "groupe": g["id"], "cote": cote,
                                           "fichier": f, "ligne": l,
                                           "complet": " ".join([c["texte"]] + [x["texte"] for x in
                                                                               c.get("desactive_interne") or []])})
                for n in c["notes"]:
                    fn, ln = lieu(g, n)
                    out["note"].append({"id": n["id"], "plage": c_plage, "numero": n["numero"],
                                        "texte": n["texte"], "commentaire": c["id"], "groupe": g["id"],
                                        "cote": cote, "fichier": fn, "ligne": ln,
                                        "complet": " ".join([n["texte"]] + [x["texte"] for x in
                                                                            n.get("desactive_interne") or []])})
                if c.get("desactive_interne"):
                    out["commentaire_desactive"].append({
                        "plage": c["plage"], "groupe": g["id"], "fichier": f,
                        "ligne": c["desactive_interne"][0].get("ligne") or l,
                        "texte": " ".join(x["texte"] for x in c["desactive_interne"])})
                for n in c["notes"]:
                    if n.get("desactive_interne"):
                        fn, ln = lieu(g, n)
                        out["note_desactivee"].append({
                            "plage": c["plage"], "groupe": g["id"], "numero": n["numero"], "fichier": fn,
                            "ligne": n["desactive_interne"][0].get("ligne") or ln,
                            "texte": " ".join(x["texte"] for x in n["desactive_interne"])})
            for t in g[cote]["testimonia"]:
                f, l = lieu(g, t)
                out["testimonia"].append({"id": t["id"], "plage": t["plage"], "texte": t["texte"],
                                          "cote": cote, "groupe": g["id"], "fichier": f, "ligne": l})
                # parties commentées à l'intérieur d'une macro active (fragments réunis : une
                # entrée peut être commentée sur plusieurs lignes)
                if t.get("desactive_interne"):
                    out["testimonia_desactive"].append({
                        "plage": t["plage"], "groupe": g["id"], "fichier": f, "ligne": l,
                        "texte": " ".join(x["texte"] for x in t["desactive_interne"])})
            for d in g[cote]["desactives"]:
                t = {"commentaire": "commentaire_desactive", "note": "note_desactivee",
                     "apparat": "apparat_desactive", "testimonia": "testimonia_desactive"}.get(d["type"])
                if t:
                    txt = d.get("texte", "")
                    if d["type"] == "commentaire" and d.get("args"):
                        txt = detex(" ".join(d["args"][1:]))
                    plage = d["args"][0] if d.get("args") else ""
                    if d["type"] == "note" and g.get("vers"):
                        # l'argument d'une \note est son numéro : on prend les vers du groupe
                        plage = "%s-%s" % (g["vers"][0], g["vers"][1])
                    f, l = lieu(g, d)
                    out[t].append({"plage": plage, "texte": txt, "groupe": g["id"], "fichier": f, "ligne": l})
        for a in g["grec"]["apparat"]:
            f, l = lieu(g, a)
            for sgm in a["segments"]:
                for e in sgm["entrees"]:
                    lem = e["lecons"][0]["lecon"] if e["lecons"] else ""
                    autres = " ".join(l_["texte"] for l_ in e["lecons"][1:])
                    retenues = " ; ".join(l_["lecon"] for l_ in e["lecons"] if l_["retenue"])
                    if not retenues and len(e["lecons"]) > 1 and not (e["lecons"][-1]["attribution"] or "").strip():
                        # dernière leçon sans autorité ni \lecon : proposition de l'auteur non signée
                        # (« … Ellebodius : (Κλεισθ.) (642-3) », nov. 2022)
                        retenues = e["lecons"][-1]["lecon"]
                    out["apparat"].append({"id": a["id"], "vers": plage_groupe(sgm["vers"], g),
                                           "debut": sgm["debut"] if sgm["debut"] is not None
                                           else premier_vers(plage_groupe(sgm["vers"], g)),
                                           "texte": e["texte"], "lemme": lem, "autres": autres,
                                           "retenues": retenues, "groupe": g["id"], "fichier": f, "ligne": l,
                                           "lecons": [(l_["lecon"], l_["attribution"] or "") for l_ in e["lecons"]]})
            # entrées commentées à l'intérieur d'une macro active (« \apparat{417}{%μορμολύκεια R :
            # \lecon{μορμολυκεῖα} Dindorf (1830) \espApp … ») : désactivées, non absentes
            if a.get("desactive_interne"):
                out["apparat_desactive"].append({
                    "plage": a["plage"], "groupe": g["id"], "id": a["id"], "fichier": f, "ligne": l,
                    "texte": " ".join(x["texte"] for x in a["desactive_interne"])})
        for l_ in g["grec"]["lignes"]:
            if l_["vers"] is not None:
                out["grec"].setdefault(l_["vers"], []).append(l_["texte"])
                out["lieu_grec"].setdefault(l_["vers"], lieu(g, l_))
                if l_.get("metre"):
                    out.setdefault("metres", {}).setdefault(l_["vers"], []).append(l_["metre"])
                out.setdefault("personnages", {}).setdefault(l_["vers"], []).append(l_["personnage"] or "∅")
        for l_ in g["francais"]["lignes"]:
            if l_["vers"] is not None:
                out["francais"].setdefault(l_["vers"], []).append(l_["texte"])
                out["lieu_francais"].setdefault(l_["vers"], lieu(g, l_))
    out["lieux"] = {x["id"]: (x["fichier"], x["ligne"])
                    for k in ("commentaire", "note", "apparat", "testimonia") for x in out[k]}
    return out


# ---------------------------------------------------------------------------
# Comparaisons par type (élément par élément)
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
        sa = bardeaux(sigles_modernes(e["texte"]), 2)
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
            m, v = idx_tout.meilleur(sigles_modernes(e["texte"]))
            if m is not None and v > sc and v >= 0.8:
                best, sc, detail = m, v, "texte (autre vers)"
        if sc < 0.5 and aut and (not lem or re.match(r"\s*suppl\b", e["texte"])):
            # entrée sans leçon grecque (« suppl. Bentley ») : le même critique dans une entrée du
            # vers (± 1) ; 2023 rédige en toutes lettres (« καὶ δεῦρο πάλιν R : καὶ δεῦρο καὶ
            # πάλιν Bentley »)
            for c in cands:
                if abs((c["debut"] or -99) - (e["debut"] or 0)) <= 1 and aut <= (noms_propres(c["texte"]) - {"R"}):
                    best, sc, detail = c, 0.5, "autorités (rédaction développée)"
                    break
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
                                    "extrait": e["texte"][:300], "recent": best["texte"][:300],
                                    "ligne": e.get("ligne"), "fichier": e.get("fichier")})
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
                                    "score": round(scd, 2), "extrait": e["texte"][:300],
                                    "ligne": e.get("ligne"), "fichier": e.get("fichier")})
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
                                        "recent": mt["texte"][:300],
                                        "ligne": e.get("ligne"), "fichier": e.get("fichier")})
                continue
        statut = "absent" if dans_plage(e["vers"]) else "hors du champ de la version récente"
        st[statut] += 1
        res["elements"].append({"type": "apparat", "statut": statut, "plage": e["vers"],
                                "id_ancien": e["id"], "id_recent": best["id"] if best else None,
                                "score": round(sc, 2), "extrait": e["texte"][:300],
                                "recent": best["texte"][:300] if best else "",
                                "ligne": e.get("ligne"), "fichier": e.get("fichier")})
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
    # chiffres (numéro de vers resté dans la ligne : « 415σφραγῖδας ») : ponctuation
    lettres = lambda s: re.sub(r"[^\w]|\d", "", s)
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
    lettres = lambda s: re.sub(r"[^\w]|\d", "", norm_grec(s))
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
        # plus largement (colométrie différente, surtout dans les parties lyriques) : le texte de
        # chaque version se lit à la suite dans les vers voisins (± 3) de l'autre, sans mot changé
        la, lb = lettres(" ".join(A["grec"][v])), lettres(" ".join(R["grec"][v]))
        fa = "".join(lettres(" ".join(A["grec"].get(w, []))) for w in range(v - 3, v + 4))
        fb = "".join(lettres(" ".join(R["grec"].get(w, []))) for w in range(v - 3, v + 4))
        if nature_difference(a, b) == "mots" and (ua == ub or (la != lb and la in fb and lb in fa)):
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


def metre_canonique(m: str) -> str:
    """Notation des mètres ramenée à une forme commune (« trim. iamb. » = « 3 ia. », « ion. min.
    cat. » = « io. min^ », « anaclast. » = « anacl. ») : seules comptent les différences d'analyse."""
    m = re.sub(r"\s+", " ", m or "").strip().lower()
    for a, b in ((r"\bion?\.? ?min\.?|\bio\.? ?mi\.?|\bio\.? ?m\b\.?", "io"), (r"\biamb\.?|\bia\.?", "ia"),
                 (r"\btroch\.?|\btr\.", "tr"), (r"anaclast\.?|anacl\.?", "anacl"), (r"\bcat\.?", "^"),
                 (r"\bparoem\.?|\bpar\.", "par"), (r"\blecyth\.?|\blec\.?", "lec"),
                 (r"\bchoriamb\.?|\bchoria\.?|\bchor\.?", "cho"), (r"\btetram\.?|\btetr\.?", "4"), (r"\btrim\.?", "3"),
                 (r"\bdim\.?", "2"), (r"\bdact\.?", "da"), (r"\bcret\.?", "cr"), (r"\bbacch\.?", "ba"),
                 (r"\banap\.?", "an"), (r"[\s.]+", "")):
        m = re.sub(a, b, m)
    return m


def comparer_metres(A, R, res):
    """Analyses métriques (\\typeVers) différentes de 2023, notation mise à part."""
    MA, MR = A.get("metres", {}), R.get("metres", {})
    diffs = []
    for v in sorted(MA):
        a = [metre_canonique(x) for x in MA[v]]
        b = [metre_canonique(x) for x in MR.get(v, [])]
        if a != b and not (set(a) <= {metre_canonique(x) for w in (v - 1, v, v + 1) for x in MR.get(w, [])}):
            diffs.append({"vers": v, "ancien": " / ".join(MA[v]), "recent": " / ".join(MR.get(v, [])) or "∅"})
    res["metres"] = diffs
    res["stats"]["metres_differents"] = len(diffs)


SEUIL_TRAD = 0.75        # traduction « nettement différente » : ressemblance des mots < 0.75


def mots_fr(s: str) -> list:
    """Mots d'une ligne de traduction, sans les mots grecs (citations, restes de balisage)."""
    return [m for m in mots((s or "").replace("œ", "oe").replace("Œ", "Oe")) if not re.match(r"[α-ωϊϋ]", m)]


def lue_a_cote(wa: list, RF: dict, v: int, fenetre: int = 8) -> bool:
    """La ligne ancienne se lit-elle, à la suite, dans la traduction de 2023 à quelques vers de
    distance (colométrie ou numérotation différente des parties lyriques) ? Blocs d'au moins deux
    mots, ou bloc entier pour les lignes très courtes."""
    large = mots_fr(" ".join(" ".join(RF.get(w, [])) for w in range(v - fenetre, v + fenetre + 1)))
    if not large:
        return False
    sm = difflib.SequenceMatcher(None, wa, large, autojunk=False)
    blocs = sm.get_matching_blocks()
    if len(wa) <= 3:
        return any(t.size == len(wa) for t in blocs)
    return sum(t.size for t in blocs if t.size >= 2) / len(wa) >= SEUIL_TRAD


def comparer_traduction(A, R, res, plage=None):
    """Traduction vers par vers. Une traduction ancienne est « différente » si la suite de ses
    mots ressemble à moins de 75 % (difflib) à celle de 2023, y compris en l'élargissant aux vers
    voisins (répartition différente des lignes françaises) ; sinon « retouchée » ou identique."""
    RF = R["francais"]
    st = Counter()
    out = []
    for v in sorted(A["francais"]):
        if plage and not plage[0] <= v <= plage[1]:
            continue
        a = re.sub(r"\s+", " ", " ".join(A["francais"][v])).strip()
        wa = mots_fr(a)
        if not wa:
            continue
        # didascalies et remarques de travail entre parenthèses (« Chez W., à Mn. : … »)
        for m in re.finditer(r"\(([^()]{8,})\)", a):
            wi = mots_fr(m.group(1))
            voisins = mots_fr(" ".join(" ".join(RF.get(w, [])) for w in range(v - 3, v + 4)))
            lue = sum(t.size for t in difflib.SequenceMatcher(None, wi, voisins, autojunk=False).get_matching_blocks())
            if len(wi) >= 3 and lue / len(wi) < 0.6:
                f, l = A["lieu_francais"].get(v, (None, None))
                out.append({"vers": v, "ancien": m.group(1), "recent": " ".join(RF.get(v, [])),
                            "ratio": None, "statut": "remarque ou didascalie absente en 2023", "fichier": f, "ligne": l})
        if v not in RF:
            fen = " ".join(" ".join(RF.get(w, [])) for w in (v - 1, v + 1))
            if inclusion(set(wa), set(mots_fr(fen))) >= 0.8 or lue_a_cote(wa, RF, v):
                st["répartie autrement"] += 1
                continue
            st["absente de 2023"] += 1
            f, l = A["lieu_francais"].get(v, (None, None))
            out.append({"vers": v, "ancien": a, "recent": "", "ratio": 0.0, "statut": "absente en 2023",
                        "fichier": f, "ligne": l})
            continue
        b = re.sub(r"\s+", " ", " ".join(RF[v])).strip()
        wb = mots_fr(b)
        if wa == wb:
            st["identique"] += 1
            continue
        r = difflib.SequenceMatcher(None, wa, wb, autojunk=False).ratio()
        if r >= SEUIL_TRAD:
            st["retouchée"] += 1
            continue
        large = mots_fr(" ".join(" ".join(RF.get(w, [])) for w in (v - 1, v, v + 1)))
        sm = difflib.SequenceMatcher(None, wa, large, autojunk=False)
        couverts = sum(t.size for t in sm.get_matching_blocks())
        if couverts / len(wa) >= SEUIL_TRAD or lue_a_cote(wa, RF, v):
            st["répartie autrement"] += 1
            continue
        st["différente"] += 1
        f, l = A["lieu_francais"].get(v, (None, None))
        out.append({"vers": v, "ancien": a, "recent": b, "ratio": round(r, 2),
                    "statut": "traduction différente en 2023", "fichier": f, "ligne": l})
    res["traduction"] = {"stats": dict(st), "elements": out}
    res["stats"]["traduction"] = dict(st)


def lecon_bibi(e: dict) -> str:
    for lec, att in e.get("lecons", []):
        if "Bibi" in att:
            return lec
    m = re.search(r"(?:^|:)\s*([^:]*?)\s*Bibi", e.get("texte", ""))
    return m.group(1) if m else ""


def formes_bibi(s: str) -> list:
    """Mots grecs sans diacritiques, casse conservée (Χελιδών ≠ χελιδών), marque d'abréviation
    finale gardée (« Μύρμ- », « ἀθ. »)."""
    s = sans_diacritiques(s).replace("ς", "σ")
    s = re.sub(r"[᾽᾿ʼ’'ʹʹ΄`´]", " ", s)          # élisions et apostrophes de toute forme
    return re.findall(r"[Ͱ-Ͽἀ-῿]+[-.]?", s)


def meme_lecon(a: str, b: str) -> bool:
    A_, B_ = formes_bibi(a), formes_bibi(b)
    if not A_ or not B_:
        return normaliser(a) == normaliser(b)

    def couvert(x, ys):
        xs = x.rstrip("-.")
        for y in ys:
            ys_ = y.rstrip("-.")
            if xs == ys_ or (x[-1] in "-." and ys_.startswith(xs)) or (y[-1] in "-." and xs.startswith(ys_)):
                return True
        return False
    return sum(1 for x in A_ if couvert(x, B_)) / len(A_) >= 0.8


def graphie_retouchee(a: str, b: str) -> bool:
    """Même conjecture, majuscule ou faute de frappe mise à part (« Μόρος ἐξελ᾽ ἄχος » / « μόρος
    ἔξελ᾽ ἄχος », « πλήξασασ᾿ αὕτη » / « πλήξασ᾿ αὕτη »)."""
    x, y = " ".join(formes_bibi(a.lower())), " ".join(formes_bibi(b.lower()))
    return bool(x and y) and difflib.SequenceMatcher(None, x, y, autojunk=False).ratio() >= 0.88


def lemmes_proches(a: dict, b: dict) -> bool:
    la, lb = set(mots_grecs(a.get("lemme", ""), 1)), set(mots_grecs(b.get("lemme", ""), 1))
    if la & lb:
        return True
    return lemme_abrege(a.get("lemme", ""), b.get("lemme", "")) >= 0.5 or \
        lemme_abrege(b.get("lemme", ""), a.get("lemme", "")) >= 0.5


def comparer_bibi(A, R, res):
    """Conjectures signées « Bibi » (entrées actives de l'apparat) comparées à celles de 2023 :
    même vers ou même lemme (± 2 vers) ; leçon identique (abréviations admises) → conservée ;
    autre leçon « Bibi » sur le même lemme → remplacée ; entrée commentée → désactivée ; sinon
    abandonnée (on signale si la leçon figure néanmoins dans le texte grec de 2023)."""
    def bibis(C):
        return [e for e in C["apparat"] if "Bibi" in e["texte"]]
    rb = defaultdict(list)
    for e in bibis(R):
        rb[e["debut"]].append(e)
    ra = defaultdict(list)
    for e in R["apparat"]:
        ra[e["debut"]].append(e)
    rdes = defaultdict(list)
    for x in R["apparat_desactive"]:
        if "Bibi" in x["texte"]:
            rdes[premier_vers(x["plage"])].append(x)
    st = Counter()
    out = []
    for e in bibis(A):
        v = e["debut"]
        if v is None:
            continue
        lec = lecon_bibi(e)
        cands = [x for d in (0, -1, 1, -2, 2) for x in rb.get(v + d, [])
                 if (d == 0 and not x.get("lemme")) or lemmes_proches(e, x)]
        if not cands:
            cands = [x for x in rb.get(v, []) if not mots_grecs(x.get("lemme", ""), 1)]
        if any(meme_lecon(lec, lecon_bibi(x)) for x in cands):
            st["conservée"] += 1
            continue
        if any(graphie_retouchee(lec, lecon_bibi(x)) for x in cands):
            st["conservée (graphie retouchée)"] += 1
            continue
        grec23 = formes_bibi(" ".join(R["grec"].get(v, [])))
        fl = [x.rstrip("-") for x in formes_bibi(lec)]
        imprime = bool(fl) and all(x in grec23 for x in fl)
        autre_critique = [x for d in (0, -1, 1) for x in ra.get(v + d, []) if "Bibi" not in x["texte"]
                          and any(meme_lecon(lec, l_) for l_, _ in x.get("lecons", [])[1:])]
        if cands:
            statut, proche = "remplacée par une autre conjecture « Bibi »", cands[0]["texte"]
        elif autre_critique:
            statut, proche = "même leçon attribuée à un autre critique en 2023", autre_critique[0]["texte"]
        else:
            des = [x for d in (0, -1, 1) for x in rdes.get(v + d, [])
                   if set(mots_grecs(e.get("lemme", ""), 1)) & set(mots_grecs(x["texte"], 1))]
            if des:
                statut, proche = "désactivée (commentée) en 2023", des[0]["texte"]
            else:
                autres = [x for x in ra.get(v, []) if lemmes_proches(e, x)] or ra.get(v, [])
                statut = "abandonnée"
                proche = autres[0]["texte"] if autres else "aucune entrée d'apparat à ce vers"
        if imprime and not statut.startswith(("désactivée", "même leçon")):
            statut += " (leçon néanmoins imprimée dans le texte de 2023)"
        st[statut] += 1
        out.append({"vers": e["vers"], "debut": v, "lecon": lec, "texte": e["texte"], "statut": statut,
                    "recent": proche, "fichier": e.get("fichier"), "ligne": e.get("ligne")})
    res["bibi"] = {"stats": dict(st), "elements": out}
    res["stats"]["bibi"] = dict(st)


def aligner_vers(A: dict, R: dict, fenetre: int = 5) -> dict:
    """Numérotation décalée dans un état ancien (fréquente en 2020 : vers sans \\ligne,
    répartition différente des lignes) : un vers dont le texte diffère nettement de celui du même
    numéro en 2023 (ressemblance < 0,85) est rapporté au vers voisin (± 5) dont le texte lui
    ressemble nettement mieux (≥ 0,6 et au moins 0,15 de plus) ; un numéro de 2023 déjà occupé
    par le vers ancien de même numéro, ou attribué à un vers plus ressemblant, n'est pas repris.
    Retourne {numéro dans l'état ancien: numéro de 2023}."""
    ta = {v: normaliser(" ".join(t)) for v, t in A["grec"].items()}
    tr = {v: normaliser(" ".join(t)) for v, t in R["grec"].items()}
    occupe, cand = set(), {}
    for v, a in ta.items():
        r0 = difflib.SequenceMatcher(None, a, tr[v], autojunk=False).ratio() if v in tr else 0.0
        if r0 >= 0.85:
            occupe.add(v)
            continue
        best, bw = r0, None
        for d in range(-fenetre, fenetre + 1):
            w = v + d
            if d and w in tr:
                r = difflib.SequenceMatcher(None, a, tr[w], autojunk=False).ratio()
                if r > best:
                    best, bw = r, w
        if bw is not None and best >= 0.6 and best >= r0 + 0.15:
            cand[v] = (bw, best)
    carte = {}
    for v, (w, r) in sorted(cand.items(), key=lambda kv: (-kv[1][1], kv[0])):
        if w not in occupe:
            occupe.add(w)
            carte[v] = w
    return carte


def renumeroter(A: dict, carte: dict) -> dict:
    """Copie de A dont les dictionnaires par vers suivent la numérotation de 2023."""
    if not carte:
        return A
    B = dict(A)
    for k in ("grec", "francais", "personnages", "metres"):
        d = {}
        for v in sorted(A.get(k, {})):
            d.setdefault(carte.get(v, v), []).extend(A[k][v])
        B[k] = d
    for k in ("lieu_grec", "lieu_francais"):
        d = {}
        for v in sorted(A.get(k, {})):
            d.setdefault(carte.get(v, v), A[k][v])
        B[k] = d
    return B


def plages(nums: list) -> list:
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return ["%d" % a if a == b else "%d-%d" % (a, b) for a, b in out]


def comparer(A: dict, R: dict, nom: str, plage_ancien=None, plage_recent=None) -> dict:
    """A, R : éléments collectés (collecter) de l'état ancien et de la référence."""
    res = {"version": nom, "elements": [], "stats": {}}
    carte = aligner_vers(A, R)
    res["carte_vers"] = {w: v for v, w in carte.items()}
    res["stats"]["vers_renumerotes"] = len(carte)
    res["vers_renumerotes"] = plages(list(carte))

    def dans_plage(plage: str) -> bool:
        if plage_recent is None:
            return True
        v = premier_vers(plage)
        return v is None or plage_recent[0] <= v <= plage_recent[1]

    comparer_textes(A, R, "commentaire", "note", dans_plage, res)
    comparer_textes(A, R, "note", "commentaire", dans_plage, res)
    comparer_testimonia(A, R, dans_plage, res)
    comparer_apparat(A, R, dans_plage, res)
    A2 = renumeroter(A, carte)
    comparer_grec(A2, R, plage_ancien, res)
    comparer_personnages(A2, R, res)
    comparer_metres(A2, R, res)
    res["_A2"] = A2
    # lieux (fichier, ligne) des éléments anciens
    for e in res["elements"]:
        if e.get("ligne") is None:
            f, l = A["lieux"].get(e.get("id_ancien"), (None, None))
            if l is None and e["type"] in ("texte_grec", "personnage"):
                v = premier_vers(e["plage"])
                f, l = A2["lieu_grec"].get(v, (None, None))
            e["fichier"], e["ligne"] = f, l
    return res


# ---------------------------------------------------------------------------
# Passages perdus du commentaire et des notes (au mot près)
# ---------------------------------------------------------------------------

N_GRAM = 4          # suites de mots comparées
ILOT_MIN = 6        # îlot couvert minimal (plus court : coïncidence de locutions banales)
PASSAGE_MIN = 8     # passage perdu minimal (sauf élément entier plus court)
RE_JETON = re.compile(r"\w+")


def jetons(texte: str):
    """Texte NFC et mots [(forme normalisée, début, fin)], normalisés un à un."""
    t = unicodedata.normalize("NFC", texte or "")
    out = []
    for m in RE_JETON.finditer(t):
        n = normaliser(m.group())
        if n:
            out.append((n, m.start(), m.end()))
    return t, out


class Couverture:
    """Ensemble des n-grammes (n = 1 à N_GRAM) de mots d'un corpus de référence."""

    def __init__(self, textes=()):
        self.ng = [set() for _ in range(N_GRAM + 1)]
        for t in textes:
            self.ajouter(t)

    def ajouter(self, texte: str):
        w = [j[0] for j in jetons(texte)[1]]
        for n in range(1, N_GRAM + 1):
            self.ng[n].update(zip(*[w[k:] for k in range(n)]))

    def masque(self, w: list) -> list:
        n = len(w)
        if n < N_GRAM:
            ok = n > 0 and tuple(w) in self.ng[n]
            return [ok] * n
        cov = [False] * n
        s = self.ng[N_GRAM]
        for i in range(n - N_GRAM + 1):
            if tuple(w[i:i + N_GRAM]) in s:
                for k in range(i, i + N_GRAM):
                    cov[k] = True
        # îlots trop courts : coïncidences, sauf s'ils couvrent tout l'élément
        i = 0
        while i < n:
            if cov[i]:
                j = i
                while j < n and cov[j]:
                    j += 1
                if j - i < ILOT_MIN and not (i == 0 and j == n):
                    for k in range(i, j):
                        cov[k] = False
                i = j
            else:
                i += 1
        return cov


def part_couverte(cov: list, i: int, j: int) -> float:
    return sum(cov[i:j]) / (j - i) if j > i else 0.0


def lacunes(cov: list, mini: int) -> list:
    out, i, n = [], 0, len(cov)
    while i < n:
        if not cov[i]:
            j = i
            while j < n and not cov[j]:
                j += 1
            if j - i >= mini:
                out.append((i, j))
            i = j
        else:
            i += 1
    return out


def detex(t: str) -> str:
    """Conversion grossière d'un fragment LaTeX en texte (pour la recherche de mots)."""
    t = re.sub(r"\\(?:begin|end)\{[^}]*\}", " ", t)
    t = re.sub(r"\\[A-Za-z@]+\*?", " ", t)
    t = re.sub(r"[{}\[\]~$&#^_\\]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def texte_actif_fichier(chemin: str) -> tuple:
    """(texte actif converti, texte des commentaires %) d'un fichier LaTeX (corps du document)."""
    src = Source(chemin)
    i = src.actif.find("\\begin{document}")
    actif = detex(src.actif[i if i >= 0 else 0:])
    comms = detex(" \n".join(c.texte for c in src.commentaires))
    return actif, comms


MOTS_VIDES = set("""dans pour avec cette comme mais plus sans sont être fait faire aussi encore très
bien tout tous toute toutes autre autres même mêmes leur leurs nous vous elle elles avoir était
étaient quand alors ainsi donc entre après avant depuis sous vers chez dont ceux celle celui ceci
cela peut peuvent semble doit tant quelque aucun aucune notre votre parce lorsque contre selon sens
texte passage note voir""".split())
SEUIL_REMANIE = 0.75     # part des mots rares d'un passage retrouvés dans le commentaire de 2023
RARES_MIN = 5            # des mêmes vers (± 3) : au-dessus, le passage est « remanié », non « disparu »


def mots_rares(t: str) -> set:
    """Mots porteurs de sens d'un passage : mots français d'au moins 5 lettres, mots grecs d'au
    moins 4 lettres, nombres d'au moins 2 chiffres (renvois)."""
    return {x for x in mots(t) if (len(x) >= 5 and x not in MOTS_VIDES)
            or (len(x) >= 4 and re.match(r"[α-ω]", x)) or (x.isdigit() and len(x) >= 2)}


def bornes(plage) -> tuple:
    a, b = plage_vers(re.sub(r"[\[\]]", "", str(plage or "")))
    return a, b if b is not None else a


class Reference:
    """Corpus de référence (2023) pour la recherche des passages perdus."""

    def __init__(self, depot: str, R: dict):
        self.actifs = R["commentaire"] + R["note"]
        self.act = Couverture(x["texte"] for x in self.actifs)
        self.idx = Index(self.actifs)
        # « articles » : commentaire et ses notes, avec leurs bornes
        notes_de = defaultdict(list)
        for n in R["note"]:
            notes_de[n["commentaire"]].append(n["texte"])
        self.articles = []
        for c in R["commentaire"]:
            a, b = bornes(c["plage"])
            if a is not None:
                self.articles.append({"id": c["id"], "plage": c["plage"], "a": a, "b": b,
                                      "rares": mots_rares(" ".join([c["texte"]] + notes_de[c["id"]]))})
        des = [x["texte"] for k in ("commentaire_desactive", "note_desactivee", "apparat_desactive",
                                    "testimonia_desactive") for x in R[k]]
        for rel in FICHIERS_2023:
            des.append(texte_actif_fichier(os.path.join(depot, rel))[1])
        self.des = Couverture(des)
        self.autres = {
            "apparat": Couverture(x["texte"] for x in R["apparat"]),
            "testimonia": Couverture(x["texte"] for x in R["testimonia"]),
            "traduction": Couverture(" ".join(t) for t in R["francais"].values()),
        }
        self.autres["autre partie du corps"] = Couverture(
            texte_actif_fichier(os.path.join(depot, rel))[0] for rel in FICHIERS_2023)
        for cle, nom, drive, _ in INTRO_ANNEXES:
            p = os.path.join(depot, drive)
            if os.path.exists(p):
                a, c = texte_actif_fichier(p)
                self.autres[nom] = Couverture([a])
                self.des.ajouter(c)


    def article_proche(self, texte: str, plage) -> tuple:
        """Article de 2023 sur les mêmes vers (± 3) qui reprend le plus de mots rares du passage :
        (article, part des mots rares, nombre de mots rares)."""
        a, b = bornes(plage)
        rares = mots_rares(texte)
        best, sc = None, 0.0
        if a is not None and rares:
            for art in self.articles:
                if art["a"] - 3 <= b and a <= art["b"] + 3:
                    x = len(rares & art["rares"]) / len(rares)
                    if x > sc:
                        best, sc = art, x
        return best, sc, len(rares)


class Pointeur:
    """Lieu (fichier, ligne) des parties commentées (%) des fichiers de 2023 : pour réactiver un
    contenu désactivé, il suffit de lever le % à cette ligne."""

    def __init__(self, depot: str):
        self.inv = defaultdict(list)
        for rel in FICHIERS_2023:
            src = Source(os.path.join(depot, rel))
            nom = re.sub(r"^.*Harmattan 2023 ", "", os.path.basename(rel)).replace(".tex", "")
            for c in src.commentaires:
                w = [j[0] for j in jetons(detex(c.texte))[1]]
                ln = src.ligne_orig(c.debut)
                for i in range(len(w) - 2):
                    self.inv[tuple(w[i:i + 3])].append((nom, ln))

    def lieu(self, texte: str):
        w = [j[0] for j in jetons(texte)[1]]
        c = Counter()
        for i in range(len(w) - 2):
            for x in set(self.inv.get(tuple(w[i:i + 3]), ())):
                c[x] += 1
        if not c:
            return None
        (nom, ln), _ = min(c.items(), key=lambda kv: (-kv[1], kv[0]))
        return "commenté en 2023 : %s, l. %d" % (nom, ln)


def passages_perdus(A: dict, REF: Reference, etat: str) -> list:
    """Passages de commentaire et de notes de l'état A absents du commentaire actif de 2023."""
    out = []

    def analyser(e: dict, typ: str, deja_desactive: bool):
        t, js = jetons(e["texte"])
        if not js:
            return
        w = [j[0] for j in js]
        cov = REF.act.masque(w)
        if deja_desactive:
            # contenu déjà commenté dans l'état ancien : ne compte que s'il a disparu des
            # fichiers de 2023 (ni actif, ni commenté)
            cd = REF.des.masque(w)
            cov = [a or b for a, b in zip(cov, cd)]
        n = len(w)
        runs = lacunes(cov, PASSAGE_MIN if n >= PASSAGE_MIN else 1)
        if n < PASSAGE_MIN and runs and runs[0] != (0, n):
            return
        if not runs:
            return
        groupes = defaultdict(list)
        for i, j in runs:
            sous = w[i:j]
            st_, proche = None, ""
            if not deja_desactive and part_couverte(REF.des.masque(sous), 0, j - i) >= 0.6:
                st_ = "désactivé (commenté) en 2023"
            if st_ is None:
                best, part = None, 0.0
                for nom, cv in REF.autres.items():
                    p = part_couverte(cv.masque(sous), 0, j - i)
                    if p > part:
                        best, part = nom, p
                if part >= 0.6:
                    st_ = "déplacé en 2023 (%s)" % best
            frag = t[js[i][1]:js[j - 1][2]]
            if st_ is None:
                m, sc = REF.idx.meilleur(frag)
                if m is not None and sc >= 0.5 and j - i >= 4:
                    st_ = "remanié en 2023"
                    proche = "%s (%s) : %d %% des suites de mots" % (m["id"], m["plage"], round(100 * sc))
            if st_ is not None and deja_desactive:
                continue          # contenu commenté dans l'état ancien, repris ailleurs en 2023
            if st_ is None:
                # mêmes mots rares dans le commentaire de 2023 sur ces vers, rédaction différente
                art, part, nb = REF.article_proche(frag, e.get("plage"))
                if art is not None and part >= SEUIL_REMANIE and nb >= RARES_MIN:
                    st_ = "remanié en 2023"
                    proche = "%s (%s) : %d %% des mots rares" % (art["id"], art["plage"], round(100 * part))
                else:
                    st_ = "disparu"
                    if art is not None and part >= 0.3:
                        proche = "commentaire de 2023 sur ces vers : %s (%s), %d %% des mots rares" % (
                            art["id"], art["plage"], round(100 * part))
            groupes[st_].append((i, j, proche))
        couverts_tot = sum(cov) / n
        for st_, lst in groupes.items():
            nb = sum(j - i for i, j, _ in lst)
            entier = nb >= 0.9 * n
            frags = [t[js[i][1]:js[j - 1][2]] for i, j, _ in lst]
            extrait = " […] ".join(frags)
            if typ == "commentaire" and e.get("lemme") and (entier or lst[0][0] == 0):
                extrait = "« %s » — %s" % (court(e["lemme"], 120), extrait)
            if lst[0][0] > 0:
                extrait = "[…] " + extrait
            if lst[-1][1] < n:
                extrait = extrait + " […]"
            statut = st_ + (" — élément entier" if entier else " — passage(s) d'un élément conservé en partie")
            if deja_desactive:
                statut = "disparu (déjà désactivé dans cet état) — " + ("élément entier" if entier else "passage(s)")
            vers = e.get("plage") or ""
            if e.get("numero"):
                vers = "%s n. %s" % (vers, e["numero"])
            out.append({"type": typ + (" (désactivé dans l'état)" if deja_desactive else ""),
                        "vers": vers, "v0": premier_vers(e.get("plage")), "extrait": extrait,
                        "texte_cle": " ".join(frags), "statut": statut, "mots": nb,
                        "part_conservee": round(couverts_tot, 2), "id": e.get("id"),
                        "proche": "; ".join(sorted({p for _, _, p in lst if p})),
                        "fichier": e.get("fichier"), "ligne": e.get("ligne"), "etat": etat})

    for e in A["commentaire"]:
        analyser(e, "commentaire", False)
    for e in A["note"]:
        analyser(e, "note", False)
    for e in A["commentaire_desactive"]:
        analyser(e, "commentaire", True)
    for e in A["note_desactivee"]:
        analyser(e, "note", True)
    return out


# ---------------------------------------------------------------------------
# Analyse d'un état (exécutée en parallèle)
# ---------------------------------------------------------------------------

_W = {}


def _init_worker(depot: str):
    ref = extraire(depot, None, fichiers=list(FICHIERS_2023), ecrire=False)
    noms = {os.path.basename(f): abreger(f) for f in FICHIERS_2023}
    R = collecter(ref, noms)
    _W.update({"depot": depot, "ext_ref": ref, "R": R, "REF": Reference(depot, R)})


def analyser_etat(cle: str) -> dict:
    depot = _W["depot"]
    e = PAR_CLE[cle]
    if cle == REFERENCE:
        ext = _W["ext_ref"]
    else:
        ext = extraire(depot, None, fichiers=e["fichiers"], ecrire=False)
    noms = {os.path.basename(f): abreger(f) for f in e["fichiers"]}
    A = collecter(ext, noms)
    s = ext["statistiques"]
    res = {"cle": cle, "statistiques": s}
    if cle == REFERENCE:
        return res
    R = _W["R"]
    plage = e["plage"]
    pa = plage or (s["premier_vers"], s["dernier_vers"])
    c = comparer(A, R, e["libelle"], plage_ancien=pa, plage_recent=(1, 1231))
    if plage:
        # fichier commençant au milieu de la pièce : les lignes précédant le premier \ligne{n}
        # sont numérotées à partir de 1 ; on écarte ce qui tombe hors de la plage du fichier
        c["elements"] = [x for x in c["elements"]
                         if x["type"] not in ("texte_grec", "personnage")
                         or (premier_vers(x["plage"]) or 0) >= plage[0]]
        c["texte_grec"]["differences"] = [d for d in c["texte_grec"]["differences"] if d["vers"] >= plage[0]]
        c["metres"] = [d for d in c["metres"] if d["vers"] >= plage[0]]
    A2 = c.pop("_A2")
    res["lieux_grec"] = A2.get("lieu_grec", {})
    comparer_traduction(A2, R, c, plage)
    comparer_bibi(A, R, c)
    res["comparaison"] = c
    res["passages"] = passages_perdus(A, _W["REF"], cle)
    return res


# ---------------------------------------------------------------------------
# Lignées : un contenu perdu n'est recensé qu'une fois
# ---------------------------------------------------------------------------

def items_de(res: dict) -> list:
    """Contenus absents de 2023 dans un état : liste homogène pour le regroupement."""
    cle = res["cle"]
    c = res["comparaison"]
    carte = c.get("carte_vers", {})

    def note_num(v):
        return "numéroté %s dans cet état" % carte[v] if v in carte else ""
    out = []
    for p in res["passages"]:
        out.append(dict(p, famille="comm", sig=bardeaux(p["texte_cle"])))
    for x in c["elements"]:
        if x["type"] in ("apparat", "testimonia"):
            if x["statut"] in ("transféré dans les testimonia", CONSERVE_ABREGE, "conservé"):
                continue
            statut = {"absent": "disparu", "remanié": "remanié en 2023",
                      "désactivé (commenté) dans la version récente": "désactivé (commenté) en 2023"
                      }.get(x["statut"], x["statut"])
            proche = court(x.get("recent") or "", 200) if x["statut"] == "remanié" else ""
            out.append({"famille": x["type"], "type": "apparat" if x["type"] == "apparat" else "testimonium",
                        "vers": x["plage"], "v0": premier_vers(x["plage"]), "extrait": x["extrait"],
                        "statut": statut, "proche": proche, "fichier": x.get("fichier"),
                        "ligne": x.get("ligne"), "etat": cle,
                        "sig": bardeaux(x["extrait"], 2) if x["type"] == "apparat" else signature_test(x["extrait"])})
    for d in c["texte_grec"]["differences"]:
        if d["nature"] not in ("mots", "accentuation, esprit ou majuscule"):
            continue
        v = d["vers"]
        f, l = PREMIER_LIEU.get((cle, v), (None, None))
        out.append({"famille": "grec", "type": "texte grec", "vers": str(v), "v0": v,
                    "extrait": d["ancien"],
                    "statut": "leçon abandonnée (%s)" % ("mots" if d["nature"] == "mots" else "accent, esprit ou majuscule"),
                    "proche": "2023 : " + d["recent"] + (" ; " + d["differences"] if d["differences"] else ""),
                    "fichier": f, "ligne": l, "etat": cle, "cle_exacte": (v, norm_grec(d["ancien"])),
                    "note": note_num(v)})
    for x in c["elements"]:
        if x["type"] == "personnage":
            out.append({"famille": "attribution", "type": "attribution", "vers": x["plage"],
                        "v0": premier_vers(x["plage"]), "extrait": x["extrait"].split(" → ")[0],
                        "statut": "attribution abandonnée", "proche": "2023 : " + x["extrait"].split(" → ")[-1],
                        "fichier": x.get("fichier"), "ligne": x.get("ligne"), "etat": cle,
                        "cle_exacte": (x["plage"], x["extrait"]), "note": note_num(premier_vers(x["plage"]))})
    for d in c["metres"]:
        f, l = PREMIER_LIEU.get((cle, d["vers"]), (None, None))
        out.append({"famille": "metre", "type": "analyse métrique", "vers": str(d["vers"]), "v0": d["vers"],
                    "extrait": d["ancien"], "statut": "analyse métrique abandonnée", "proche": "2023 : " + d["recent"],
                    "fichier": f, "ligne": l, "etat": cle,
                    "cle_exacte": (d["vers"], metre_canonique(d["ancien"]))})
    for t in c["traduction"]["elements"]:
        f, l = PREMIER_LIEU_FR.get((cle, t["vers"]), (None, None))
        out.append({"famille": "trad", "type": "traduction", "vers": str(t["vers"]), "v0": t["vers"],
                    "extrait": t["ancien"], "statut": t["statut"],
                    "proche": ("2023 : " + t["recent"]) if t["recent"] else "",
                    "fichier": f, "ligne": l, "etat": cle, "sig": bardeaux(t["ancien"], 2),
                    "note": note_num(t["vers"])})
    for b in c["bibi"]["elements"]:
        out.append({"famille": "bibi", "type": "conjecture « Bibi »", "vers": b["vers"], "v0": b["debut"],
                    "extrait": b["texte"], "statut": b["statut"], "proche": "2023 : " + court(b["recent"], 200),
                    "fichier": b.get("fichier"), "ligne": b.get("ligne"), "etat": cle,
                    "cle_exacte": (b["debut"], " ".join(formes_bibi(b["lecon"].lower())[:6])
                                   or " ".join(formes_bibi(b["texte"].lower())[:4]) or normaliser(b["lecon"]))})
    for it in out:
        corriger_plage(it)
    return out


PREMIER_LIEU = {}       # (état, vers) -> lieu de la ligne grecque
PREMIER_LIEU_FR = {}    # (état, vers) -> lieu de la ligne française

SEUIL_LIGNEE = {"comm": 0.75, "apparat": 0.8, "testimonia": 0.8, "trad": 0.85}
STATUTS_COMPTES = {"différent (ponctuation)", "différent (découpage (antilabè/répartition))",
                   "différent (répartition des lignes entre vers voisins)", "numérotation différente"}
FENETRE = {"comm": 3, "apparat": 2, "testimonia": 2, "trad": 0}


def corriger_plage(it: dict):
    """Plages fautives des états de mars 2020 : le dossier στωμύλα μένη (vv. 1073-1075) y est
    numéroté 173-5, 173 et 174. Le contenu est rapporté aux vers véritables."""
    if it["v0"] in (173, 174) and "στωμ" in normaliser(it.get("extrait", "")):
        ancien = it["vers"]
        it["vers"] = str(it["vers"]).replace("173", "1073").replace("174", "1074")
        it["v0"] += 900
        it["note"] = "plage saisie « %s » dans cet état (lapsus pour %s)" % (ancien, it["vers"])
        if "cle_exacte" in it:
            it["cle_exacte"] = (it["v0"],) + tuple(it["cle_exacte"][1:])


def residus(it: dict, couverture: Couverture) -> list:
    """Parts d'un contenu rattaché à une lignée qui ne se lisent dans aucun contenu déjà recensé
    (au plus 25 % du texte, le seuil d'inclusion le permettant) : elles sont recensées à part, pour
    que rien ne soit perdu en dédoublonnant."""
    t, js = jetons(it["texte_cle"])
    w = [j[0] for j in js]
    out = []
    for i, j in lacunes(couverture.masque(w), PASSAGE_MIN):
        frag = t[js[i][1]:js[j - 1][2]]
        stat = it["statut"].split(" — ")[0]
        stat += " — passage(s)" if stat.startswith("disparu (déjà") else " — passage(s) d'un élément conservé en partie"
        out.append(dict(it, extrait="[…] %s […]" % frag, texte_cle=frag, sig=bardeaux(frag), mots=j - i,
                        statut=stat, note="partie propre à la forme ancienne d'un passage recensé par ailleurs"))
    return out


def regrouper(items: list) -> list:
    """Lignées : du plus récent au plus ancien état, chaque contenu est rattaché à une lignée
    existante (même famille, vers voisins, texte inclus à 75-85 % dans celui de la lignée, ou clé
    identique) ; sinon il en ouvre une nouvelle, dont il est le représentant. Ce qu'un contenu
    rattaché a en propre (commentaire et notes) forme une lignée à part (résidu)."""
    # représentant : forme la plus récente dans la filiation principale ; à défaut, dans un
    # essai, une variante, une sauvegarde ou la branche A
    items = sorted(items, key=lambda x: (not est_principal(x["etat"]), -RANG[x["etat"]]))
    lignees = []
    seaux = defaultdict(list)
    exactes = {}
    deja = Couverture()      # texte du commentaire et des notes déjà recensé

    def ouvrir(it: dict) -> dict:
        lg = {"rep": it, "etats": {it["etat"]}, "residus": []}
        lignees.append(lg)
        seaux[(it["famille"], it["v0"] if it["v0"] is not None else -1)].append(lg)
        if it["famille"] == "comm":
            deja.ajouter(it["texte_cle"])
        return lg

    for it in items:
        fam = it["famille"]
        if "cle_exacte" in it:
            k = (fam, it["cle_exacte"])
            if k in exactes:
                exactes[k]["etats"].add(it["etat"])
            else:
                exactes[k] = {"rep": it, "etats": {it["etat"]}}
                lignees.append(exactes[k])
            continue
        v0 = it["v0"] if it["v0"] is not None else -1
        best, sc = None, 0.0
        fen = FENETRE[fam]
        for d in range(-fen, fen + 1):
            for lg in seaux[(fam, v0 + d)]:
                x = inclusion(it["sig"], lg["rep"]["sig"])
                if x > sc:
                    best, sc = lg, x
        if best is not None and sc >= SEUIL_LIGNEE[fam]:
            best["etats"].add(it["etat"])
            if fam == "comm":
                for r in best["residus"]:
                    if inclusion(r["rep"]["sig"], it["sig"]) >= SEUIL_LIGNEE[fam]:
                        r["etats"].add(it["etat"])
                for rs in residus(it, deja):
                    best["residus"].append(ouvrir(rs))
            continue
        ouvrir(it)
    return lignees


PRINCIPAUX = [e["cle"] for e in ETATS if e["filiation"] == "principale" and e["nature"] == "complet"]


def est_principal(cle: str) -> bool:
    return PAR_CLE[cle]["filiation"] == "principale" and PAR_CLE[cle]["nature"] == "complet"


def suivant_principal(cle: str):
    r = RANG[cle]
    for k in PRINCIPAUX:
        if RANG[k] > r:
            return k
    return None


ORDRE_TYPES = ["commentaire", "note", "commentaire (désactivé dans l'état)", "note (désactivé dans l'état)",
               "brouillon commenté (2023)", "conjecture « Bibi »", "apparat", "testimonium", "texte grec", "attribution", "analyse métrique",
               "traduction", "introduction", "annexes", "index"]
POINTEUR = []           # Pointeur (construit dans main)


RE_WILLEMS = re.compile(r"Bull\. (?:cité|Acad)|Note (?:de|d['’]Alphonse) Willems|, ci-après\b|, ci-devant\b|"
                        r"\bci-après\.?$|note sur (?:Oiseaux|Lysistrata|Guêpes|Nuées|Paix)\b|\bt\. I+, p\.")
RE_TRAVAIL = re.compile(r"⟨à revoir|à retrouver|à vérifier|\bvérif\.|\?\?|\.\.\. \.\.\.|^voir\b|^cf\.|ytrtyrjt", re.I)


def nature_contenu(rep: dict) -> str:
    """Nature d'un passage de commentaire ou de note (indication de tri, automatique) : note de
    travail, note ou renvoi de Willems, simple renvoi, texte rédigé."""
    if not rep["type"].startswith(("commentaire", "note")):
        return ""
    corps = re.sub(r"^« .*? » — ", "", rep["extrait"]).strip(" […]")
    n = rep.get("mots") or len(mots(corps))
    if RE_WILLEMS.search(corps):
        return "note ou renvoi de Willems"
    if RE_TRAVAIL.search(corps) and n <= 40:
        return "note de travail"
    if n <= 15 and re.match(r"(Cf\.?|Voir|cf\.|voir)\b", corps):
        return "renvoi"
    return "texte rédigé"


def ligne_recuperable(lg: dict) -> dict:
    rep = lg["rep"]
    etats = sorted(lg["etats"], key=lambda k: RANG[k])
    dernier = rep["etat"]
    premier = etats[0]
    rq = []
    principaux = [k for k in etats if est_principal(k)]
    branche = {PAR_CLE[k]["filiation"] for k in etats}
    if not principaux:
        noms = [PAR_CLE[k]["libelle"] for k in etats]
        if branche <= {"branche A"}:
            rq.append("propre à la branche A de l'été 2020, sans suite (%s)" % ", ".join(noms))
        else:
            rq.append("seulement dans : " + (", ".join(noms) if len(noms) <= 4 else "%d états" % len(noms)))
    else:
        sv = suivant_principal(principaux[-1])
        if sv and not rep["statut"].startswith("disparu (déjà"):
            actif = rep["statut"].startswith("désactiv")
            rq.append("%s à partir de : %s" % ("plus actif" if actif else "absent", PAR_CLE[sv]["libelle"]))
    if rep.get("note"):
        rq.append(rep["note"])
    if rep.get("part_conservee") is not None and rep["famille"] == "comm" and "passage" in rep["statut"]:
        rq.append("élément conservé à %d %% en 2023" % round(100 * rep["part_conservee"]))
    if rep.get("mots"):
        rq.append("%d mots" % rep["mots"])
    if "⟨à revoir" in rep["extrait"]:
        rq.append("contient une note de travail de l'auteur (macro \\eff)")
    proche = rep.get("proche") or ""
    if not proche and rep["statut"].startswith("désactiv") and POINTEUR:
        proche = POINTEUR[0].lieu(rep.get("texte_cle") or rep["extrait"]) or ""
    return {"version": PAR_CLE[dernier]["libelle"], "fichier": rep.get("fichier") or "",
            "ligne": rep.get("ligne") or "", "type": rep["type"], "vers": rep.get("vers") or "",
            "extrait": rep["extrait"], "statut_2023": rep["statut"],
            "premiere_version": PAR_CLE[premier]["libelle"], "nb_versions": len(etats),
            "proche_2023": proche, "remarque": " ; ".join(rq), "nature": nature_contenu(rep),
            "mots": rep.get("mots") or "",
            "_tri": (ORDRE_TYPES.index(rep["type"]) if rep["type"] in ORDRE_TYPES else 99,
                     rep.get("v0") if rep.get("v0") is not None else 99999, RANG[dernier],
                     str(rep.get("ligne") or ""))}


# ---------------------------------------------------------------------------
# Introduction, Annexes, Index : version du Drive / copie de latex/
# ---------------------------------------------------------------------------

RE_IMAGE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")


def paragraphes(chemin: str) -> tuple:
    """Unités comparables : lignes non vides du corps (\\begin{document} … \\end{document}),
    avec leur état (actif / entièrement commenté) et leur texte converti ; figures à part."""
    lignes = open(chemin, encoding="utf-8").read().split("\n")
    debut = next((i for i, l in enumerate(lignes) if "\\begin{document}" in l and not l.lstrip().startswith("%")), 0)
    out, images = [], {}
    for i in range(debut + 1, len(lignes)):
        s = lignes[i].strip()
        if not s:
            continue
        commente = s.startswith("%")
        if "\\end{document}" in s and not commente:
            break
        src = Source("<l>", s.lstrip("%") if commente else s)
        m = RE_IMAGE.search(src.actif)
        if m:
            if not commente:
                images.setdefault(m.group(1).strip(), i + 1)
            continue
        txt = detex(src.actif)
        if len(mots(txt)) < 3:
            continue
        out.append({"ligne": i + 1, "commente": commente, "texte": txt, "mots": mots(txt)})
    return out, images


def plus_proche(u: dict, unites: list, inv: dict):
    """Unité la plus semblable (difflib sur les mots) parmi celles qui partagent un mot rare."""
    c = Counter()
    for m in set(u["mots"]):
        for k in inv.get(m, ()):
            c[k] += 1
    best, sc = None, 0.0
    for k, _ in c.most_common(15):
        r = difflib.SequenceMatcher(None, u["mots"], unites[k]["mots"], autojunk=False).ratio()
        if r > sc:
            best, sc = unites[k], r
    return best, sc


def index_mots(unites: list) -> dict:
    freq = Counter(m for u in unites for m in set(u["mots"]))
    inv = defaultdict(list)
    for k, u in enumerate(unites):
        for m in set(u["mots"]):
            if freq[m] <= 20:
                inv[m].append(k)
    return inv


def fondre_blocs(lignes: list, mini: int = 4) -> list:
    """Paragraphes consécutifs d'un même ensemble ajouté (au moins `mini`) : une seule ligne, début
    et fin de l'ensemble, lignes et nombre de mots (le texte complet est dans le fichier source)."""
    out, bloc = [], []

    def vider():
        if len(bloc) >= mini:
            x = dict(bloc[0])
            x["extrait"] = court(bloc[0]["extrait"], 500) + " […] " + bloc[-1]["extrait"][-200:]
            n = sum(b["mots"] for b in bloc)
            x["mots"] = n
            x["remarque"] = "%d paragraphes, lignes %s-%s ; %d mots ; texte complet dans le fichier" % (
                len(bloc), bloc[0]["ligne"], bloc[-1]["ligne"], n)
            out.append(x)
        else:
            out.extend(bloc)
        bloc.clear()

    for l in lignes:
        if bloc and l["statut_2023"] == bloc[-1]["statut_2023"] and l["fichier"] == bloc[-1]["fichier"] \
                and 0 <= l["ligne"] - bloc[-1]["ligne"] <= 3:
            bloc.append(l)
        else:
            vider()
            bloc.append(l)
    vider()
    return out


def comparer_intro_annexes(depot: str) -> tuple:
    """Pour chaque fichier : passages propres à la version du Drive (absents de latex/), passages
    de latex/ supprimés ou désactivés dans la version du Drive, figures ajoutées ou retirées.
    Une unité brève (moins de 8 mots) retouchée (ressemblance ≥ 0,5 avec une unité de l'autre
    version) est signalée une seule fois, du côté du Drive (« complétée ou corrigée »)."""
    lignes_tsv, bilan = [], {}

    def ligne(version, fichier, num, typ, extrait, statut, remarque, proche="", ordre=0):
        return {"version": version, "fichier": fichier, "ligne": num, "type": typ, "vers": "",
                "extrait": court(extrait, 1500), "statut_2023": statut, "premiere_version": version,
                "nb_versions": 1, "proche_2023": court(proche, 300), "remarque": remarque, "nature": "",
                "mots": len(mots(extrait)), "_tri": (ORDRE_TYPES.index(typ), num, ordre, "")}

    for cle, nom, drive, local in INTRO_ANNEXES:
        pd, pl = os.path.join(depot, drive), os.path.join(depot, local)
        if not (os.path.exists(pd) and os.path.exists(pl)):
            continue
        (D, imgD), (L, imgL) = paragraphes(pd), paragraphes(pl)
        vD, vL = "%s (Drive)" % nom, "%s (latex/)" % nom
        b = {"drive": {"fichier": abreger(drive), "octets": os.path.getsize(pd), "unites": len(D)},
             "latex": {"fichier": local, "octets": os.path.getsize(pl), "unites": len(L)}, "statuts": Counter()}
        cD_act = Couverture(" ".join(u["mots"]) for u in D if not u["commente"])
        cD_com = Couverture(" ".join(u["mots"]) for u in D if u["commente"])
        cL_all = Couverture(" ".join(u["mots"]) for u in L)
        invD, invL = index_mots(D), index_mots(L)
        # (1) contenu actif de latex/ absent de la version du Drive
        for u in L:
            if u["commente"]:
                continue
            w = u["mots"]
            cov = cD_act.masque(w)
            runs = lacunes(cov, PASSAGE_MIN if len(w) >= PASSAGE_MIN else 1)
            if len(w) < PASSAGE_MIN and runs and runs[0] != (0, len(w)):
                runs = []
            if not runs:
                b["statuts"]["latex/ : conservé"] += 1
                continue
            if len(w) < PASSAGE_MIN and plus_proche(u, D, invD)[1] >= 0.5:
                b["statuts"]["latex/ : retouché (voir la version du Drive)"] += 1
                continue
            t, js = jetons(u["texte"])
            for i, j in runs:
                part_com = part_couverte(cD_com.masque(w[i:j]), 0, j - i)
                st_ = ("désactivé (commenté) dans la version du Drive" if part_com >= 0.6
                       else "supprimé dans la version du Drive")
                b["statuts"]["latex/ : " + st_] += 1
                lignes_tsv.append(ligne(vL, local, u["ligne"], cle, t[js[i][1]:js[j - 1][2]], st_,
                                        "%d mots ; la version du Drive est la plus récente" % (j - i)))
        # (2) contenu de la version du Drive absent de latex/ (actif ou commenté)
        for u in D:
            w = u["mots"]
            cov = cL_all.masque(w)
            runs = lacunes(cov, PASSAGE_MIN if len(w) >= PASSAGE_MIN else 1)
            if len(w) < PASSAGE_MIN and runs and runs[0] != (0, len(w)):
                runs = []
            if not runs:
                continue
            t, js = jetons(u["texte"])
            suffixe = " (ligne commentée)" if u["commente"] else ""
            if len(w) < PASSAGE_MIN:
                prec, sc = plus_proche(u, L, invL)
                if sc >= 0.5:
                    st_ = "complété ou corrigé dans la version du Drive" + suffixe
                    b["statuts"]["Drive : " + st_] += 1
                    lignes_tsv.append(ligne(vD, abreger(drive), u["ligne"], cle, u["texte"], st_,
                                            "forme de latex/ en regard", proche="latex/ : " + prec["texte"], ordre=1))
                    continue
            for i, j in runs:
                st_ = "présent seulement dans la version du Drive" + suffixe
                b["statuts"]["Drive : " + st_] += 1
                lignes_tsv.append(ligne(vD, abreger(drive), u["ligne"], cle, t[js[i][1]:js[j - 1][2]],
                                        st_ + " : manque dans la copie de latex/", "%d mots" % (j - i), ordre=1))
        # (3) figures
        for f in sorted(set(imgD) - set(imgL)):
            b["statuts"]["Drive : figure ajoutée"] += 1
            lignes_tsv.append(ligne(vD, abreger(drive), imgD[f], cle, "\\includegraphics{%s}" % f,
                                    "figure présente seulement dans la version du Drive", "", ordre=1))
        for f in sorted(set(imgL) - set(imgD)):
            b["statuts"]["latex/ : figure retirée"] += 1
            lignes_tsv.append(ligne(vL, local, imgL[f], cle, "\\includegraphics{%s}" % f,
                                    "figure retirée dans la version du Drive", ""))
        b["figures"] = {"drive": len(imgD), "latex": len(imgL)}
        b["statuts"] = dict(sorted(b["statuts"].items()))
        bilan[cle] = b
    return lignes_tsv, bilan


# ---------------------------------------------------------------------------
# Parties commentées de 2023 : contenus qu'aucun état n'imprime
# ---------------------------------------------------------------------------

RE_ETIQ_VERS = re.compile(r"^\s*%{2,}\s*v\.?\s*(\d+[a-z]?(?:\s*[-–]\s*\d+[a-z]?)?)")


def empreintes(texte: str) -> set:
    w = [j[0] for j in jetons(texte)[1]]
    return {hash(x) for x in zip(w, w[1:], w[2:], w[3:])}


def nature_brouillon(mots_: list, frag: str) -> str:
    grecs = sum(1 for m in mots_ if re.match(r"[α-ω]", m))
    if grecs >= 0.5 * len(mots_):
        return "matériaux (textes grecs copiés)"
    if RE_TRAVAIL.search(frag) and len(mots_) <= 40:
        return "note de travail"
    return "texte rédigé"


def brouillons_2023(depot: str, deja: Couverture, etats: list) -> tuple:
    """Texte des lignes commentées des fichiers de 2023 qui ne se lit ni dans leur texte actif, ni
    parmi les contenus déjà recensés : brouillons, dossiers de travail, citations copiées. Une
    ligne par suite d'au moins 8 mots ; le premier état (filiation principale) où le texte se lit,
    et s'il a jamais été actif, sont cherchés par 4-grammes de mots (≥ 60 %)."""
    act = Couverture(texte_actif_fichier(os.path.join(depot, rel))[0] for rel in FICHIERS_2023)
    series = []
    for e in etats:
        if not est_principal(e["cle"]) or e["cle"] == REFERENCE:
            continue
        a_, c_ = set(), set()
        for rel in e["fichiers"]:
            a, c = texte_actif_fichier(os.path.join(depot, rel))
            a_ |= empreintes(a)
            c_ |= empreintes(c)
        series.append((e, a_, c_))
    lignes = []
    st = Counter()
    for rel in FICHIERS_2023:
        src = Source(os.path.join(depot, rel))
        lignes_src = src.orig.split("\n")
        debut = src.orig.find("\\begin{document}")
        blocs = []
        for c in src.commentaires:
            if c.debut < debut:
                continue
            ln = src.ligne_orig(c.debut)
            if blocs and ln - blocs[-1]["fin"] <= 1:
                blocs[-1]["t"].append(c.texte)
                blocs[-1]["fin"] = ln
            else:
                blocs.append({"debut": ln, "fin": ln, "t": [c.texte]})
        for b in blocs:
            t, js = jetons(detex("\n".join(b["t"])))
            w = [j[0] for j in js]
            if len(w) < 4:
                continue
            ca = act.masque(w)
            cov = [x or y for x, y in zip(ca, deja.masque(w))]
            st["mots commentés"] += len(w)
            st["mots actifs ailleurs dans 2023"] += sum(ca)
            st["mots déjà recensés"] += sum(cov) - sum(ca)
            for i, j in lacunes(cov, PASSAGE_MIN):
                sous = w[i:j]
                # étiquettes de groupes (« v. 663-666 ») et essais de polices : rien à recenser
                if sum(1 for m in sous if m == "v" or m.isdigit() or re.fullmatch(r"\d+[a-z]", m)) >= 0.5 * len(sous):
                    continue
                frag = t[js[i][1]:js[j - 1][2]]
                if frag.startswith("Une phrase en"):
                    continue
                vers = ""
                for k in range(b["debut"] - 1, -1, -1):
                    m = RE_ETIQ_VERS.match(lignes_src[k])
                    if m:
                        vers = "[%s]" % re.sub(r"\s+", "", m.group(1))
                        break
                emp = empreintes(frag)
                pres = [(e, len(emp & a_) / len(emp), len(emp & c_) / len(emp)) for e, a_, c_ in series] if emp else []
                vus = [e for e, x, y in pres if max(x, y) >= 0.6]
                actifs = [e for e, x, y in pres if x >= 0.6]
                premier = (vus or [PAR_CLE[REFERENCE]])[0]
                statut = "désactivé (commenté) en 2023 — " + (
                    "actif dans un état antérieur" if actifs else "brouillon jamais actif")
                st["mots de brouillons recensés"] += j - i
                st["lignes"] += 1
                rq = "%d mots ; texte complet à la ligne indiquée" % (j - i)
                if actifs:
                    rq += " ; actif en dernier dans : " + actifs[-1]["libelle"]
                nom = re.sub(r"^.*Harmattan 2023 ", "", os.path.basename(rel)).replace(".tex", "")
                lignes.append({"version": "Harmattan 2023 (parties commentées)", "fichier": abreger(rel),
                               "ligne": b["debut"], "type": "brouillon commenté (2023)", "vers": vers,
                               "extrait": court(frag, 800), "statut_2023": statut,
                               "premiere_version": premier["libelle"], "nb_versions": len(vus) + 1,
                               "proche_2023": "commenté en 2023 : %s, l. %d" % (nom, b["debut"]), "remarque": rq,
                               "nature": nature_brouillon(sous, frag), "mots": j - i,
                               "_tri": (ORDRE_TYPES.index("brouillon commenté (2023)"), premier_vers(vers) or 99999,
                                        RANG[REFERENCE], "%06d" % b["debut"])})
    return lignes, dict(st)


def bibi_commentees(depot: str, R: dict, deja: Couverture) -> list:
    """Entrées d'apparat commentées de 2023 (conjectures « Bibi » comprises : v. 1082 ὀλόφυγ᾽) qui ne
    se lisent ni dans le texte actif de 2023, ni dans une ligne du tableau. Les restes de macros
    (« , Reiske », sans leçon ni deux-points) ne sont pas des entrées et sont écartés."""
    act = Couverture(texte_actif_fichier(os.path.join(depot, rel))[0] for rel in FICHIERS_2023)
    lignes = []
    for x in R["apparat_desactive"]:
        w = [j[0] for j in jetons(x["texte"])[1]]
        if len(w) < 3 or not (" : " in x["texte"] or "Bibi" in x["texte"]):
            continue
        cov = [a or b for a, b in zip(deja.masque(w), act.masque(w))]
        if sum(cov) >= 0.6 * len(w):
            continue
        typ = "conjecture « Bibi »" if "Bibi" in x["texte"] else "apparat"
        lignes.append({"version": "Harmattan 2023 (parties commentées)", "fichier": x.get("fichier") or "",
                       "ligne": x.get("ligne") or "", "type": typ, "vers": x.get("plage") or "",
                       "extrait": x["texte"], "statut_2023": ("désactivée (commentée) en 2023" if "Bibi" in x["texte"]
                                                              else "désactivé (commenté) en 2023"),
                       "premiere_version": "Harmattan 2023 (parties commentées)", "nb_versions": 1,
                       "proche_2023": "commenté en 2023 : %s, l. %s" % (
                           re.sub(r"^.*Harmattan 2023 ", "", x.get("fichier") or "").replace(".tex", ""), x.get("ligne")),
                       "remarque": "entrée commentée, sans forme active antérieure recensée", "nature": "", "mots": "",
                       "_tri": (ORDRE_TYPES.index(typ), premier_vers(x.get("plage")) or 99999, RANG[REFERENCE], "")})
    return lignes


# ---------------------------------------------------------------------------
# Fichiers de travail hors série : brouillon note.txt, texte de présentation
# ---------------------------------------------------------------------------

COMPLEMENTS = [
    ("note.txt (brouillon du dossier 455-6)", GCA + "note.txt", "commentaire", "455-6",
     "brouillon non daté du commentaire de 455-6"),
    ("Présentation de la pièce", GCA + "Présentation Thesmophories.txt", "introduction", "",
     "texte de présentation de la pièce (.odt, .pdf, .txt)"),
]


def comparer_complements(depot: str, REF: Reference, recense: Couverture) -> tuple:
    """Paragraphes de ces fichiers : ce qui ne se lit ni dans le corps de 2023 (actif ou commenté),
    ni dans l'Introduction, les Annexes et l'Index du Drive, ni dans les contenus déjà recensés."""
    lignes, bilan = [], {}
    for version, rel, typ, vers, rq in COMPLEMENTS:
        p = os.path.join(depot, rel)
        if not os.path.exists(p):
            continue
        texte = open(p, encoding="utf-8").read()
        texte = re.sub(r"^===== p\. \d+ =====$", "", texte, flags=re.M)
        texte = re.sub(r"(\w)-\n(\w)", r"\1\2", texte)      # coupures de fin de ligne du .txt tiré du PDF
        st = Counter()
        n = 0
        debut, bloc = 1, []
        paras = []
        for i, l in enumerate(texte.split("\n") + [""], start=1):
            if l.strip():
                if not bloc:
                    debut = i
                bloc.append(l)
            elif bloc:
                paras.append((debut, " ".join(bloc)))
                bloc = []
        for num, par in paras:
            t, js = jetons(detex(par))
            w = [j[0] for j in js]
            if len(w) < PASSAGE_MIN:
                continue
            masques = [REF.act.masque(w), REF.des.masque(w)] + [c.masque(w) for c in REF.autres.values()]
            cov23 = [any(x) for x in zip(*masques)]
            st["mots"] += len(w)
            st["mots présents en 2023"] += sum(cov23)
            cov = [a or b for a, b in zip(cov23, recense.masque(w))]
            st["mots déjà recensés par un autre état"] += sum(cov) - sum(cov23)
            for i, j in lacunes(cov, PASSAGE_MIN):
                st["mots propres à ce fichier"] += j - i
                frag = t[js[i][1]:js[j - 1][2]]
                lignes.append({"version": version, "fichier": abreger(rel), "ligne": num, "type": typ, "vers": vers,
                               "extrait": frag, "statut_2023": "disparu — passage propre à ce fichier",
                               "premiere_version": version, "nb_versions": 1, "proche_2023": "", "remarque": rq,
                               "nature": "texte rédigé", "mots": j - i,
                               "_tri": (ORDRE_TYPES.index(typ), premier_vers(vers) or 99998, RANG[REFERENCE], "%06d" % num)})
                n += 1
        bilan[version] = {"fichier": abreger(rel), "passages": n, **st}
    return lignes, bilan


# ---------------------------------------------------------------------------
# Masquage du nom de l'auteur (dépôt public)
# ---------------------------------------------------------------------------

def motif_masquage(depot: str):
    motifs = set()
    for rel in [FICHIERS_2023[0]] + [x[2] for x in INTRO_ANNEXES] + [x[3] for x in INTRO_ANNEXES]:
        p = os.path.join(depot, rel)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        m = re.search(r"\\author\{(.*?)(?:\\\\|\})", t, re.S)
        if m:
            nom = re.sub(r"\s+", " ", re.sub(r"\\[A-Za-z]+|[{}]", " ", m.group(1))).strip()
            if len(nom) >= 4:
                motifs.add(re.escape(nom))
                parties = nom.split()
                if len(parties) >= 2 and len(parties[-1]) >= 4:
                    motifs.add(re.escape(parties[-1]))
                    # initiales, relevées dans une note de travail (« Note XX : … »)
                    motifs.add(r"(?<=Note )" + "".join(x[0] for x in parties))
    motifs.add(r"[\w.+-]+@[\w-]+\.[\w.]+")
    return re.compile("|".join(sorted(motifs)), re.I)


def masquer(obj, rx):
    if isinstance(obj, str):
        return rx.sub("[auteur]", obj)
    if isinstance(obj, list):
        return [masquer(x, rx) for x in obj]
    if isinstance(obj, tuple):
        return tuple(masquer(x, rx) for x in obj)
    if isinstance(obj, dict):
        return {k: masquer(v, rx) for k, v in obj.items()}
    return obj


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------

def suites_etats(cles: list) -> str:
    """« 2020-03a…2020-06, 2020-07-11 » : suites d'états consécutifs dans l'ordre du catalogue."""
    rangs = sorted(RANG[k] for k in cles)
    out = []
    for r in rangs:
        if out and r == out[-1][1] + 1:
            out[-1][1] = r
        else:
            out.append([r, r])
    return ", ".join(ETATS[a]["cle"] if a == b else "%s…%s" % (ETATS[a]["cle"], ETATS[b]["cle"]) for a, b in out)


def nettoyer(s) -> str:
    return re.sub(r"\s+", " ", str(s if s is not None else "")).strip()


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=os.path.abspath(os.path.join(ici, "..", "..")))
    ap.add_argument("--processus", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    a = ap.parse_args()
    depot = a.depot
    sortie = os.path.join(depot, "edition", "donnees", "travaux_anterieurs")
    rx = motif_masquage(depot)

    preparer_archive(depot)
    inv = inventaire(depot)
    presents = {x["chemin"] for x in inv}
    etats = [e for e in ETATS if all(f in presents for f in e["fichiers"])]
    manquants = [e["cle"] for e in ETATS if e not in etats]
    if manquants:
        print("États sans fichier local (ignorés) :", ", ".join(manquants))

    with mp.Pool(a.processus, initializer=_init_worker, initargs=(depot,)) as pool:
        resultats = pool.map(analyser_etat, [e["cle"] for e in etats], chunksize=1)
    par_cle = {r["cle"]: r for r in resultats}

    # lieux des lignes grecques et françaises (pour les lignées de texte et de traduction)
    for r in resultats:
        c = r.get("comparaison")
        if not c:
            continue
        for v, lieu_ in r.get("lieux_grec", {}).items():
            PREMIER_LIEU[(r["cle"], v)] = lieu_
        for t in c["traduction"]["elements"]:
            PREMIER_LIEU_FR[(r["cle"], t["vers"])] = (t.get("fichier"), t.get("ligne"))

    items = []
    for r in resultats:
        if r["cle"] != REFERENCE:
            items.extend(items_de(r))
    lignees = regrouper(items)
    POINTEUR.append(Pointeur(depot))
    lignes = [ligne_recuperable(lg) for lg in lignees]
    lignes_ia, bilan_ia = comparer_intro_annexes(depot)
    lignes_ia = fondre_blocs(sorted(lignes_ia, key=lambda x: x["_tri"]))
    ext_ref = extraire(depot, None, fichiers=list(FICHIERS_2023), ecrire=False)
    noms_ref = {os.path.basename(f): abreger(f) for f in FICHIERS_2023}
    R_ref = collecter(ext_ref, noms_ref)
    REF = Reference(depot, R_ref)
    recense = Couverture(lg["rep"]["texte_cle"] for lg in lignees if lg["rep"]["famille"] == "comm")
    lignes_cp, bilan_cp = comparer_complements(depot, REF, recense)
    tout = Couverture(x["extrait"] for x in lignes)
    lignes_bb = bibi_commentees(depot, R_ref, tout)
    lignes_br, bilan_br = brouillons_2023(depot, tout, etats)
    lignes += lignes_ia + lignes_cp + lignes_bb + lignes_br
    lignes.sort(key=lambda x: x["_tri"])

    # disparitions par état : lignées dont c'est le dernier état
    disparitions = defaultdict(Counter)
    for lg in lignees:
        disparitions[lg["rep"]["etat"]][lg["rep"]["type"]] += 1

    stats_cles = ["groupes", "lignes_grecques", "lignes_francaises", "premier_vers", "dernier_vers",
                  "commentaires", "caracteres_commentaires", "notes", "apparats", "apparat_entrees",
                  "lecons_Bibi", "testimonia_grec", "testimonia_francais", "macros_desactivees"]
    resultat = {
        "meta": {
            "genere_par": "outils/extraction/comparer_versions.py",
            "abreviations": {"TH/": TH, "GCA/": GCA},
            "reference": PAR_CLE[REFERENCE]["fichiers"],
            "methode": "voir l'en-tête du script et recherche/travaux_anterieurs.md § 10",
        },
        "inventaire": [{k: v for k, v in x.items() if k != "chemin"} for x in inv],
        "etats": [{"cle": e["cle"], "libelle": e["libelle"], "date": e["date"],
                   "fichiers": [abreger(f) for f in e["fichiers"]], "nature": e["nature"],
                   "filiation": e["filiation"], "remarque": e["remarque"],
                   "doublons": [x["fichier"] for x in inv if x["etat"] == e["cle"] and x["role"].startswith("doublon")],
                   "statistiques": {k: par_cle[e["cle"]]["statistiques"].get(k) for k in stats_cles},
                   "contenus_perdus_dont_dernier_etat": dict(sorted(disparitions.get(e["cle"], {}).items()))}
                  for e in etats],
        "comparaisons": [],
        "introduction_annexes_index": bilan_ia,
        "complements": bilan_cp,
        "parties_commentees_2023": bilan_br,
        "lignees": {"total": len(lignees), "par_type": dict(sorted(Counter(lg["rep"]["type"] for lg in lignees).items())),
                    "par_statut": dict(sorted(Counter(lg["rep"]["statut"].split(" — ")[0] for lg in lignees).items()))},
    }
    # éléments non conservés à l'identique : chacun n'est listé qu'une fois, avec les états où il
    # figure (les états successifs partagent l'essentiel de leurs différences avec 2023) ; les
    # différences de ponctuation, de découpage ou de numérotation du texte grec sont seulement
    # comptées (stats) ; extraits abrégés (texte complet des contenus perdus :
    # contenus_recuperables.tsv)
    distincts = {}
    for e in etats:
        r = par_cle[e["cle"]]
        c = r.get("comparaison")
        if not c:
            continue
        resultat["comparaisons"].append({
            "etat": e["cle"], "version": e["libelle"], "stats": c["stats"],
            "plage_version": [r["statistiques"]["premier_vers"], r["statistiques"]["dernier_vers"]],
            "vers_renumerotes": c.get("vers_renumerotes", []),
            "texte_grec": {k: c["texte_grec"][k] for k in ("vers_communs", "vers_differents", "natures",
                                                           "seulement_ancien", "seulement_recent")},
            "personnages": {k: c["personnages"][k] for k in ("vers_differents", "blocs")},
            "passages_perdus": dict(sorted(Counter(p["statut"].split(" — ")[0] for p in r["passages"]).items())),
        })
        els = [x for x in c["elements"] if x["statut"] not in STATUTS_COMPTES]
        els += [{"type": "conjecture « Bibi »", "statut": b["statut"], "plage": b["vers"], "extrait": b["texte"],
                 "recent": b["recent"], "fichier": b.get("fichier"), "ligne": b.get("ligne")}
                for b in c["bibi"]["elements"]]
        for x in els:
            k = (x["type"], x["statut"], str(x["plage"]), court(x.get("extrait"), 200))
            d = distincts.setdefault(k, {"type": x["type"], "statut": x["statut"], "plage": str(x["plage"]),
                                         "extrait": court(x.get("extrait"), 200), "etats": []})
            if e["cle"] not in d["etats"]:
                d["etats"].append(e["cle"])
            # lieu et rapprochement : ceux de l'état le plus récent
            d.update({"recent": court(x.get("recent"), 200), "id_recent": x.get("id_recent"),
                      "score": x.get("score"), "fichier": x.get("fichier"), "ligne": x.get("ligne"),
                      "id_ancien": x.get("id_ancien"), "dernier_etat": e["cle"]})
    ordre_type = {"commentaire": 0, "note": 1, "conjecture « Bibi »": 2, "apparat": 3, "testimonia": 4,
                  "texte_grec": 5, "personnage": 6}
    resultat["elements"] = sorted(distincts.values(), key=lambda d: (
        ordre_type.get(d["type"], 9), premier_vers(d["plage"]) or 0, RANG[d["etats"][0]], d["statut"], d["extrait"]))
    resultat = masquer(resultat, rx)
    lignes = masquer(lignes, rx)

    with open(os.path.join(sortie, "comparaison_versions.json"), "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
    with open(os.path.join(sortie, "comparaison_versions.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["type", "statut", "plage", "extrait", "recent_proche", "id_recent_proche", "score",
                    "nb_etats", "premier_etat", "dernier_etat", "etats", "fichier", "ligne", "id_ancien"])
        for e in resultat["elements"]:
            w.writerow([e["type"], e["statut"], e["plage"], nettoyer(e["extrait"]), nettoyer(e.get("recent")),
                        e.get("id_recent") or "", "" if e.get("score") is None else e["score"],
                        len(e["etats"]), e["etats"][0], e["dernier_etat"], suites_etats(e["etats"]),
                        e.get("fichier") or "", e.get("ligne") or "", e.get("id_ancien") or ""])
    with open(os.path.join(sortie, "contenus_recuperables.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        cols = ["version", "fichier", "ligne", "type", "vers", "extrait", "statut_2023", "premiere_version",
                "nb_versions", "proche_2023", "remarque", "nature", "mots"]
        w.writerow(cols)
        for x in lignes:
            w.writerow([nettoyer(x[k]) for k in cols])
    # contrôle bloquant : aucune donnée personnelle dans les sorties
    for nom in ("comparaison_versions.json", "comparaison_versions.tsv", "contenus_recuperables.tsv"):
        with open(os.path.join(sortie, nom), encoding="utf-8") as f:
            if rx.search(f.read()):
                raise SystemExit("ERREUR : donnée personnelle non masquée dans " + nom)
    print("États analysés : %d ; lignées de contenus absents de 2023 : %d (+ %d Introduction/Annexes/Index, "
          "+ %d fichiers hors série, + %d entrées d'apparat et %d passages commentés de 2023)"
          % (len(etats), len(lignees), len(lignes_ia), len(lignes_cp), len(lignes_bb), len(lignes_br)))
    print(json.dumps(resultat["lignees"], ensure_ascii=False))


if __name__ == "__main__":
    main()
