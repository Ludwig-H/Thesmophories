#!/usr/bin/env python3
"""Repérage automatique des citations des *Thesmophories* dans le corpus local.

Parcourt tous les passages de l'index (`.sources/corpus/index.sqlite`, voir indexer.py)
et relève les suites de mots communes avec le texte de la pièce (vulgate Hall–Geldart
renumérotée selon l'usage, et texte de l'auteur, `edition/donnees/travaux_anterieurs/
texte_grec.tsv`). Les mots sont comparés sous leur forme normalisée (grec.normaliser) ;
pour l'OCR et les PDF, sous leur forme « pliée » (grec.plier_ocr : κ = χ, lettres latines…).

Méthode :
  1. trigrammes du texte de la pièce → positions (vers) ;
  2. 1er passage : fréquence de chaque trigramme dans le corpus (nombre de passages) ;
  3. 2e passage : suites maximales (≥ 3 mots) ; regroupement des suites voisines
     (variantes, omissions, interpolations : écart ≤ 3 mots) ; on garde un groupe si
     ≥ 4 mots communs, ou 3 mots dont un trigramme rare (≤ --rare passages), ou si le
     passage nomme Aristophane ou les Thesmophories.
Le résultat (JSONL, un groupe par ligne) est un relevé de CANDIDATS : chaque citation se
vérifie sur le texte (et, pour l'OCR, sur l'image de la page).

Usage :
  python3 outils/corpus/citations_thesmo.py SORTIE.jsonl [--rare 25] [--processus 8]
"""

import argparse
import csv
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from multiprocessing import Pool
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
sys.path.insert(0, str(ICI))
from grec import normaliser, plier_ocr  # noqa: E402

BASE = RACINE / ".sources" / "corpus" / "index.sqlite"
HG = RACINE / ".sources" / "corpus" / "thesmo_hall_geldart.tsv"
AUTEUR = RACINE / "edition" / "donnees" / "travaux_anterieurs" / "texte_grec.tsv"

# Œuvres exclues : la pièce elle-même et ses éditions, Aristophane (autres pièces :
# répétitions de l'auteur, pas des témoignages), Euripide (vers parodiés), ouvrages modernes.
EXCLU_URN = re.compile(r"tlg0019\.|tlg0006\.")
EXCLU_ABR = {"Hall–Geldart II", "Velsen 1883", "Fritzsche 1838", "Kock I", "Kock II", "Kock III",
             "Meineke I", "Meineke II.1", "Meineke II.2", "Meineke III", "Meineke IV",
             "Kaibel CGF", "TGF² (Nauck)", "Bergk PLG⁴ II", "Bergk PLG⁴ III",
             "Tosi, Dict. des sentences", "Bauck, De proverbiis Ar."}
EXCLU_COLL = {"lsj"}


def num_usuel(v):
    """Numéro Hall–Geldart → numérotation usuelle (HG 373-378 = 372-377 ; HG 379 = 378-379)."""
    m = re.match(r"(\d+)([a-z]?)", v or "")
    if not m:
        return None
    n, suf = int(m.group(1)), m.group(2)
    if 373 <= n <= 378:
        n -= 1
    return f"{n}{suf}"


def textes_piece():
    """Liste de flux [(mot normalisé, vers usuel)] : vulgate HG, texte de l'auteur."""
    flux = []
    f = []
    for r in csv.DictReader(open(HG, encoding="utf-8"), delimiter="\t"):
        v = r["vers"]
        t = r["texte"]
        if v == "379" and "|" in t:   # HG 379 réunit les vers usuels 378 et 379
            a, b = t.split("|", 1)
            f += [(w, "378") for w in normaliser(a).split()]
            f += [(w, "379") for w in normaliser(b).split()]
            continue
        f += [(w, num_usuel(v)) for w in normaliser(t.replace("|", " ")).split()]
    flux.append(f)
    f = []
    if AUTEUR.exists():
        for r in csv.DictReader(open(AUTEUR, encoding="utf-8"), delimiter="\t"):
            vhg = (r.get("vers_HG") or "").split("-")[0]
            v = num_usuel(vhg) or r["vers"]
            f += [(w, v) for w in normaliser(r["texte"]).split()]
        flux.append(f)
    return flux


FLUX = None
IDX = None     # mode → {trigramme: [(flux, pos)]}
MOTS = None    # mode → [liste de mots par flux]
VERS = None
EXCLUS = None
OCR = None
FREQ = None
ARGS = None


def preparer(rare):
    global FLUX, IDX, MOTS, VERS
    FLUX = textes_piece()
    IDX, MOTS = {}, {}
    VERS = [[v for _, v in f] for f in FLUX]
    for mode in ("exact", "plie"):
        idx = defaultdict(list)
        mots = []
        for k, f in enumerate(FLUX):
            ws = [w for w, _ in f]
            if mode == "plie":
                ws = [plier_ocr(w) or w for w in ws]
            mots.append(ws)
            for i in range(len(ws) - 2):
                idx[(ws[i], ws[i + 1], ws[i + 2])].append((k, i))
        IDX[mode] = dict(idx)
        MOTS[mode] = mots


def init(exclus, ocr, freq, args):
    global EXCLUS, OCR, FREQ, ARGS
    EXCLUS, OCR, FREQ, ARGS = exclus, ocr, freq, args
    preparer(args["rare"])


def lire(bornes):
    con = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    cur = con.execute("SELECT id, oeuvre_id, norm FROM passages WHERE id >= ? AND id < ?", bornes)
    for pid, oid, norm in cur:
        if oid in EXCLUS or not norm:
            continue
        yield pid, oid, norm
    con.close()


def jetons(oid, norm):
    if oid in OCR:
        return "plie", plier_ocr(norm).split()
    return "exact", norm.split()


def compter(bornes):
    c = Counter()
    for pid, oid, norm in lire(bornes):
        mode, T = jetons(oid, norm)
        idx = IDX[mode]
        vus = set()
        for i in range(len(T) - 2):
            k = (T[i], T[i + 1], T[i + 2])
            if k in idx and k not in vus:
                vus.add(k)
        for k in vus:
            c[(mode, k)] += 1
    return c


def suites(T, mode):
    idx, mots = IDX[mode], MOTS[mode]
    res = []
    for i in range(len(T) - 2):
        k = (T[i], T[i + 1], T[i + 2])
        if k not in idx:
            continue
        for (f, p) in idx[k]:
            S = mots[f]
            if i > 0 and p > 0 and T[i - 1] == S[p - 1]:
                continue  # pas le début d'une suite
            L = 3
            while i + L < len(T) and p + L < len(S) and T[i + L] == S[p + L]:
                L += 1
            res.append((i, f, p, L))
    # une seule suite par position du texte (la plus longue, flux 0 de préférence)
    meilleur = {}
    for (i, f, p, L) in res:
        if i not in meilleur or L > meilleur[i][3] or (L == meilleur[i][3] and f < meilleur[i][1]):
            meilleur[i] = (i, f, p, L)
    out = sorted(meilleur.values())
    # supprimer les suites incluses dans une autre
    final = []
    for s in out:
        if final and s[0] + s[3] <= final[-1][0] + final[-1][3]:
            continue
        final.append(s)
    return final


def grouper(ss):
    groupes = []
    for s in ss:
        if groupes:
            g = groupes[-1]
            i0, f0, p0, L0 = g[-1]
            if s[0] - (i0 + L0) <= 3 and s[1] == f0 and 0 <= s[2] - (p0 + L0) <= 4 + max(0, s[0] - (i0 + L0)):
                g.append(s)
                continue
        groupes.append([s])
    return groupes


def analyser(bornes):
    out = []
    for pid, oid, norm in lire(bornes):
        mode, T = jetons(oid, norm)
        ss = suites(T, mode)
        if not ss:
            continue
        nomme_ar = "αριστοφαν" in norm
        nomme_th = "θεσμοφορ" in norm
        for g in grouper(ss):
            nb = sum(L for (_, _, _, L) in g)
            mots = MOTS[mode][g[0][1]]
            vers = VERS[g[0][1]]
            tris = []
            for (i, f, p, L) in g:
                for j in range(L - 2):
                    tris.append(FREQ.get((mode, tuple(mots[p + j:p + j + 3])), 0))
            fmin = min(tris) if tris else 0
            garder = nb >= 4 or (nb >= 3 and fmin <= ARGS["rare"]) or nomme_th or (nomme_ar and nb >= 3)
            if not garder:
                continue
            i0 = g[0][0]
            i1 = g[-1][0] + g[-1][3]
            p0, p1 = g[0][2], g[-1][2] + g[-1][3] - 1
            out.append({
                "passage": pid, "oeuvre": oid, "mode": mode,
                "v0": vers[p0], "v1": vers[p1], "mots_communs": nb, "freq_min": fmin,
                "suites": [[i, p, L] for (i, _, p, L) in g],
                "cite": " ".join(T[i0:i1]),
                "piece": " ".join(mots[p0:p1 + 1]),
                "nomme_ar": nomme_ar, "nomme_th": nomme_th,
            })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sortie")
    ap.add_argument("--rare", type=int, default=25)
    ap.add_argument("--processus", type=int, default=8)
    a = ap.parse_args()
    con = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    exclus, ocr = set(), set()
    for oid, coll, urn, abr in con.execute("SELECT id, collection, urn, abr_auteur FROM oeuvres"):
        if coll in EXCLU_COLL or EXCLU_URN.search(urn or "") or abr in EXCLU_ABR:
            exclus.add(oid)
        if coll in ("ocr", "drive"):
            ocr.add(oid)
    mn, mx = con.execute("SELECT min(id), max(id) FROM passages").fetchone()
    con.close()
    pas = (mx - mn) // 256 + 1
    tranches = [(mn + k * pas, mn + (k + 1) * pas) for k in range(256)]
    args = {"rare": a.rare}
    with Pool(a.processus, initializer=init, initargs=(exclus, ocr, {}, args)) as pool:
        freq = Counter()
        for c in pool.imap_unordered(compter, tranches):
            freq.update(c)
    print(f"trigrammes de la pièce rencontrés : {len(freq)}", file=sys.stderr)
    freq = dict(freq)
    n = 0
    with Pool(a.processus, initializer=init, initargs=(exclus, ocr, freq, args)) as pool, \
            open(a.sortie, "w", encoding="utf-8") as out:
        for res in pool.imap_unordered(analyser, tranches):
            for r in res:
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
                n += 1
    print(f"{n} groupes candidats écrits dans {a.sortie}", file=sys.stderr)


if __name__ == "__main__":
    main()
