#!/usr/bin/env python3
"""Sources citées dans les travaux antérieurs de l'auteur (édition « Harmattan 2023 »).

Lit edition/donnees/travaux_anterieurs/thesmo.json (produit par extraire_travaux.py) et
compte, pour une liste de sources (lexicographes, parémiographes, scholies, auteurs anciens,
critiques et ouvrages modernes), les occurrences dans :
  - le commentaire (texte des \\commentaire) ;
  - les notes du commentaire (\\note) ;
  - les testimonia actifs (côtés grec et français) ;
  - l'apparat critique.
Le texte compté est la conversion en texte brut de l'extraction (les macros d'abréviation de
l'auteur, \\Apostol, \\Syn, \\EtymMagnum…, y sont déjà développées).

Sortie : edition/donnees/travaux_anterieurs/sources_citees.tsv
  categorie, source, commentaires (nombre d'articles où la source apparaît, notes comprises),
  occ_commentaire, occ_notes, occ_testimonia, occ_apparat, total, motif

Les motifs sont des expressions régulières volontairement simples : les comptes sont des
ordres de grandeur (un même passage peut citer deux fois la même source ; « Euripide » compte
aussi le personnage). Ils servent à caractériser le commentaire, non à le dépouiller.

Usage : python3 outils/extraction/sources_citees.py [--depot CHEMIN]
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re

# (catégorie, source, motif)
SOURCES = [
    # lexicographes, grammairiens, compilateurs
    ("lexicographie", "Hésychius", r"Hésychius|Hesychius|Hesych\b|Hesych\.|\bHsch\b"),
    ("lexicographie", "Souda (Suidas)", r"\bSouda\b|Suidas|\bSuid\b|Suid\.|Suidae"),
    ("lexicographie", "Photius", r"Photius|\bPhot\."),
    ("lexicographie", "Pollux", r"Pollux|\bPoll\.|Onomasticon"),
    ("lexicographie", "Athénée", r"Athénée|Athenaeus|\bAth\."),
    ("lexicographie", "Synagoge", r"Συναγωγ|Synagog"),
    ("lexicographie", "Etymologica", r"Etymologicum|\bEtym\.|\bEM\b"),
    ("lexicographie", "Eustathe", r"Eustathe|Eustathius|\bEust\."),
    ("lexicographie", "Zonaras", r"Zonaras|Zonar\."),
    ("lexicographie", "Harpocration", r"Harpocration|\bHarp\."),
    ("lexicographie", "Phrynichus", r"Phrynichus|Phrynicus|\bPhryn\."),
    ("lexicographie", "Moeris", r"Moeris|Mœris"),
    ("lexicographie", "Antiatticiste", r"Antiattici"),
    ("lexicographie", "Aelius Dionysius", r"Aelius Dionysius|Ælius Dionysius"),
    ("lexicographie", "Stobée", r"Stobée|Stobaeus|Stobæus"),
    ("scholies", "scholies, scholiaste", r"[Ss]choli|\bΣ\b|\bΣ\s|Schol\."),
    # parémiographie
    ("parémiographie", "proverbe (mot)", r"[Pp]roverb|παροιμ|parœm|paroem"),
    ("parémiographie", "Érasme, Adages", r"Érasme|Erasme|Erasmus|\bAdages?\b"),
    ("parémiographie", "Zénobius", r"Zénobius|Zenobius|\bZen\."),
    ("parémiographie", "Diogénien", r"Diogénien|Diogenian|Diogén\."),
    ("parémiographie", "Apostolius", r"Apostolius|\bApost\."),
    ("parémiographie", "Macarius", r"Macarius|Macaire"),
    ("parémiographie", "Grégoire de Chypre", r"Grégoire de Chypre|Gregorius Cyprius"),
    ("parémiographie", "Corpus Paroemiographorum (Leutsch-Schneidewin)", r"Leutsch|Corpus Par[oœ]|\bCPG\b"),
    ("parémiographie", "Tosi", r"\bTosi\b"),
    ("parémiographie", "Gaisford", r"Gaisford"),
    # ouvrages et critiques modernes
    ("moderne", "Willems", r"Willems"),
    ("moderne", "Taillardat", r"Taillardat"),
    ("moderne", "Austin & Olson", r"Austin\s*(?:&|et|\\&)\s*Olson|Austin-Olson|\bA\.?\s*&\s*O\.|\bA&O\b"),
    ("moderne", "Austin (seul)", r"(?<!Kassel-)(?<!Kassel & )(?<!Kassel et )(?<!Kassel-\s)\bAustin\b(?!\s*(?:&|et|\\&)\s*Olson)(?!-Olson)"),
    ("moderne", "Kassel-Austin (PCG)", r"Kassel"),
    ("moderne", "Kannicht (TrGF V)", r"Kannicht"),
    ("moderne", "Nauck", r"Nauck|\bN²"),
    ("moderne", "Radt", r"\bRadt\b"),
    ("moderne", "Sommerstein", r"Sommerstein"),
    ("moderne", "Prato", r"\bPrato\b"),
    ("moderne", "Coulon", r"\bCoulon\b"),
    ("moderne", "Rogers", r"\bRogers\b"),
    ("moderne", "Fritzsche", r"Fritzsche"),
    ("moderne", "van Leeuwen", r"Leeuwen"),
    ("moderne", "Enger", r"\bEnger\b"),
    ("moderne", "von Velsen", r"Velsen"),
    ("moderne", "Parker (« Lætitia »)", r"Lætitia|Laetitia|\bParker\b"),
    ("moderne", "Henderson", r"Henderson"),
    ("moderne", "LSJ", r"\bLSJ\b|L\.S\.J\.|Liddell"),
    ("moderne", "Chantraine", r"Chantraine"),
    ("moderne", "Bailly", r"\bBailly\b"),
    ("moderne", "Daremberg-Saglio", r"Daremberg"),
    ("moderne", "Pauly-Wissowa (RE)", r"Pauly|Realencyclop"),
    ("moderne", "Jouan & van Looy", r"Jouan"),
    ("moderne", "Kühner-Gerth", r"Kühner"),
    ("moderne", "Boudreaux", r"Boudreaux"),
    ("moderne", "Vernhes", r"Vernhes|Verhnes"),
    ("moderne", "Brunck", r"\bBrunck\b"),
    ("moderne", "Bentley", r"\bBentley\b"),
    ("moderne", "Hermann", r"\bHermann\b"),
    ("moderne", "Dindorf", r"\bDindorf\b"),
    ("moderne", "Meineke", r"Meineke"),
    ("moderne", "Blaydes", r"Blaydes"),
    # Aristophane (autres pièces et fragments)
    ("Aristophane", "Acharniens", r"Acharniens"),
    ("Aristophane", "Cavaliers", r"Cavaliers"),
    ("Aristophane", "Nuées", r"\bNuées\b|\bNubes\b"),
    ("Aristophane", "Guêpes", r"Guêpes|\bVesp\."),
    ("Aristophane", "Paix", r"\bPaix\b"),
    ("Aristophane", "Oiseaux", r"Oiseaux"),
    ("Aristophane", "Lysistrata", r"Lysistrata|\bLys\."),
    ("Aristophane", "Grenouilles", r"Grenouilles|\bRan\."),
    ("Aristophane", "Assemblée des femmes", r"Assemblée des [Ff]emmes|\bEccl\."),
    ("Aristophane", "Ploutos", r"Ploutos|Plutus|\bPlut\."),
    ("Aristophane", "fragments d'Aristophane", r"[Ff]ragments? d'Aristophane|Ar\. fragm\.|fr\.\s*\d+[^.;]{0,20}Kassel"),
    # autres auteurs anciens
    ("auteurs", "Homère", r"Homère|homérique|Iliade|Odyssée"),
    ("auteurs", "Hésiode", r"Hésiode"),
    ("auteurs", "Pindare", r"Pindare"),
    ("auteurs", "Eschyle", r"Eschyle"),
    ("auteurs", "Sophocle", r"Sophocle"),
    ("auteurs", "Euripide (auteur et personnage)", r"Euripide"),
    ("auteurs", "Eupolis", r"Eupolis"),
    ("auteurs", "Cratinos", r"Cratin"),
    ("auteurs", "Ménandre", r"Ménandre"),
    ("auteurs", "Hérodote", r"Hérodote"),
    ("auteurs", "Thucydide", r"Thucydide"),
    ("auteurs", "Xénophon", r"Xénophon"),
    ("auteurs", "Platon", r"Platon(?! le Comique)"),
    ("auteurs", "Aristote", r"Aristote"),
    ("auteurs", "Démosthène", r"Démosthène"),
    ("auteurs", "Plutarque", r"Plutarque"),
    ("auteurs", "Lucien", r"Lucien"),
    ("auteurs", "Théocrite", r"Théocrite"),
    ("auteurs", "Plaute", r"Plaute"),
    ("auteurs", "Cicéron", r"Cicéron"),
    ("auteurs", "Pline", r"Pline"),
    # littérature française (comparaisons)
    ("français", "Brassens", r"Brassens"),
    ("français", "La Fontaine", r"La Fontaine"),
    ("français", "Molière", r"Molière"),
    ("français", "Rabelais", r"Rabelais"),
    ("français", "Villon", r"Villon"),
]


def compter(depot: str):
    chemin = os.path.join(depot, "edition", "donnees", "travaux_anterieurs", "thesmo.json")
    with open(chemin, encoding="utf-8") as f:
        d = json.load(f)
    comms, notes, tests, apps = [], [], [], []
    for g in d["groupes"]:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                comms.append(c)
            for t in g[cote]["testimonia"]:
                tests.append(t["texte"])
        for a in g["grec"]["apparat"]:
            apps.append(a["texte"])
    lignes = []
    for cat, nom, motif in SOURCES:
        rx = re.compile(motif)
        occ_c = sum(len(rx.findall(c["texte"])) for c in comms)
        occ_n = sum(len(rx.findall(n["texte"])) for c in comms for n in c["notes"])
        nb_c = sum(1 for c in comms
                   if rx.search(c["texte"]) or any(rx.search(n["texte"]) for n in c["notes"]))
        occ_t = sum(len(rx.findall(t)) for t in tests)
        occ_a = sum(len(rx.findall(t)) for t in apps)
        lignes.append([cat, nom, nb_c, occ_c, occ_n, occ_t, occ_a, occ_c + occ_n + occ_t + occ_a, motif])
    return lignes, len(comms)


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=os.path.abspath(os.path.join(ici, "..", "..")))
    a = ap.parse_args()
    lignes, n = compter(a.depot)
    sortie = os.path.join(a.depot, "edition", "donnees", "travaux_anterieurs", "sources_citees.tsv")
    with open(sortie, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["categorie", "source", "commentaires", "occ_commentaire", "occ_notes",
                    "occ_testimonia", "occ_apparat", "total", "motif"])
        w.writerows(lignes)
    print("%d articles de commentaire ; %d sources comptées -> %s" % (n, len(lignes), sortie))
    for l in sorted(lignes, key=lambda x: -x[2])[:30]:
        print("%-16s %-45s %4d articles  %5d occ." % (l[0], l[1], l[2], l[7]))


if __name__ == "__main__":
    main()
