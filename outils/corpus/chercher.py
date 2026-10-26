#!/usr/bin/env python3
"""Recherche dans le corpus grec local (index SQLite FTS5 construit par indexer.py).

Syntaxe de la requête (les mots sont normalisés comme l'index : accents, esprits, iota
souscrit, apostrophes et coronis ignorés, σ = ς, majuscules = minuscules) :
  πυθοῦ χελιδών                   tous les mots dans le même passage (vers, section, article…)
  "σοφοὶ τύραννοι"                 expression exacte (mots consécutifs)
  ὀρθρογ*                         préfixe
  χελιδών OR ἀηδών                 ou ; NOT pour exclure ; parenthèses permises
  NEAR(πυθοῦ χελιδών, 3)           mots à 3 mots au plus l'un de l'autre
Options utiles :
  --exact      respecter accents, esprits et iota souscrit (grave = aigu) : filtre après coup
  --strict     ne pas utiliser l'index « souple » de l'OCR (χ = κ, lettres latines…)
  --sans-variantes  ne pas admettre ξυν-/συν-, ττ/σσ, ρρ/ρσ, γιγν-/γιν- (admis par défaut)
  --lemme      étendre chaque mot à toutes ses formes (table Diorisis), p. ex. --lemme χελιδών
  -a/--auteur, -o/--oeuvre, --collection, --sans-ocr, -c N (contexte), -n N, --json

Exemples :
  python3 outils/corpus/chercher.py '"Νείλου μὲν αἵδε καλλιπάρθενοι ῥοαί"'
  python3 outils/corpus/chercher.py 'πυθοῦ χελιδών' -c 1
  python3 outils/corpus/chercher.py 'ἀπόκυνον' -a Hsch
  python3 outils/corpus/chercher.py 'σοφοὶ τύραννοι' -a Eur --exact
  python3 outils/corpus/chercher.py --oeuvres Hsch          # œuvres indexées correspondantes
  python3 outils/corpus/chercher.py --stats
"""

import argparse
import json
import os
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from grec import forme_exacte, normaliser, plier_ocr  # noqa: E402

BASE = ICI.parent.parent / ".sources" / "corpus" / "index.sqlite"
RANG_COLL = {"perseus": 0, "first1k": 1, "lsj": 2, "dclp": 3, "ocr": 4, "drive": 5}
LETTRES_SOUDA = {"A": "α", "B": "β", "Γ": "γ", "Δ": "δ", "Aι": "αι", "E": "ε", "Ζ": "ζ", "Η": "η",
                 "Θ": "θ", "Ι": "ι", "Κ": "κ", "Λ": "λ", "Μ": "μ", "Ν": "ν", "Ξ": "ξ", "Ο": "ο",
                 "Ο255": "ο", "Π": "π", "Ρ": "ρ", "Σ": "σ", "Τ": "τ", "Υ": "υ", "Φ": "φ", "Χ": "χ",
                 "Ψ": "ψ", "Ω": "ω"}


# ---------------------------------------------------------------------------
# Analyse de la requête
# ---------------------------------------------------------------------------

JETONS = re.compile(r'"[^"]*"|\(|\)|,|\bAND\b|\bOR\b|\bNOT\b|\bNEAR\b|[^\s(),"]+')

# Variantes orthographiques usuelles (attique ancien / koinè, éditions) : ξυν- = συν-,
# -ττ- = -σσ-, -ρρ- = -ρσ-, γιγν- = γιν-. Appliquées par défaut (--sans-variantes pour
# les désactiver ; jamais avec --exact).
REGLES_VARIANTES = [("ξυν", "συν"), ("ξυμ", "συμ"), ("ξυγ", "συγ"), ("ξυλλ", "συλλ"),
                    ("ττ", "σσ"), ("ρρ", "ρσ"), ("γιγν", "γιν")]


def variantes(mot, actif=True):
    formes = {mot}
    if not actif:
        return formes
    for _ in range(2):
        for f in list(formes):
            for a, b in REGLES_VARIANTES:
                if a in f:
                    formes.add(f.replace(a, b))
                if b in f:
                    formes.add(f.replace(b, a))
        if len(formes) > 8:
            break
    return formes


def expr_fts(alts, prefixe):
    """Expression FTS5 pour une suite de positions (ensembles de formes équivalentes)."""
    combis = [[]]
    for s in alts:
        combis = [c + [f] for c in combis for f in sorted(s)][:16]
    etoile = "*" if prefixe else ""
    phrases = ['"' + " ".join(c) + '"' + etoile for c in combis]
    return phrases[0] if len(phrases) == 1 else "(" + " OR ".join(phrases) + ")"


def analyser(requete, plier=False, lemmes=None, var=True):
    """Traduit la requête de l'utilisateur en requête FTS5 sur la forme normalisée.

    Renvoie (requête_fts, termes_positifs) ; chaque terme positif est (texte brut,
    [ensemble des formes admises pour chaque mot], préfixe | « lemme ») et sert au filtre
    --exact et au surlignage."""
    jetons = JETONS.findall(requete)
    out, termes = [], []
    nier = False
    dans_near = 0

    def formes_de(mot):
        fs = variantes(mot, var and not dans_near)
        return {plier_ocr(f) for f in fs} if plier else fs

    for j in jetons:
        if j in ("AND", "OR", "NOT", "(", ")", ","):
            out.append(j)
            if j == "NOT":
                nier = True
            if j == "(" and dans_near:
                dans_near += 1
            if j == ")" and dans_near:
                dans_near -= 1
            continue
        if j == "NEAR":
            out.append("NEAR")
            dans_near = 1
            continue
        if dans_near and re.fullmatch(r"\d+", j) and out and out[-1] == ",":
            out.append(j)
            continue
        guillemets = j.startswith('"')
        prefixe = (not guillemets) and j.endswith("*")
        brut = j.strip('"').rstrip("*")
        mots = normaliser(brut).split()
        if not mots:
            continue
        if lemmes is not None and not guillemets and not prefixe and len(mots) == 1 and not dans_near:
            formes = set(lemmes(mots[0]))
            if formes:
                if plier:
                    formes = {plier_ocr(f) for f in formes}
                out.append("(" + " OR ".join(f'"{f}"' for f in sorted(formes)) + ")")
                if not nier:
                    termes.append((brut, [formes], "lemme"))
                nier = False
                continue
        if dans_near:
            # dans NEAR(…), FTS5 n'admet que des phrases simples : pas de variantes
            ms = plier_ocr(" ".join(mots)).split() if plier else mots
            out.append('"' + " ".join(ms) + '"' + ("*" if prefixe else ""))
            alts = [{m} for m in ms]
        else:
            alts = [formes_de(m) for m in mots]
            out.append(expr_fts(alts, prefixe))
        if not nier:
            termes.append((brut, alts, prefixe))
        nier = False
    # FTS5 : opérateur implicite AND entre termes juxtaposés (comportement par défaut)
    return " ".join(out).replace("( ", "(").replace(" )", ")").replace(" ,", ","), termes


# ---------------------------------------------------------------------------
# Références lisibles
# ---------------------------------------------------------------------------

def reference(o, p):
    """Référence lisible d'un passage : « Eur. Hel. 255 », « Sud. α 1002 », « Hsch. (Schmidt min.) col. 199, s.v. … »."""
    coll = o["collection"]
    ref = p["ref"] or ""
    if coll in ("perseus", "first1k"):
        if o["urn_oeuvre"] == "urn:cts:greekLit:tlg9010.tlg001":  # Souda (Adler)
            lettre, _, num = ref.partition(".")
            return f"Sud. {LETTRES_SOUDA.get(lettre, lettre)} {num}".strip()
        base = " ".join(x for x in (o["abr_auteur"], o["abr_titre"]) if x)
        s = f"{base} {ref}".strip()
        if p["repere"]:
            s += f" ({p['repere']})"
        return s
    if coll == "lsj":
        return f"LSJ s.v. {ref}"
    if coll == "dclp":
        return f"{o['abr_auteur']} ({ref})"
    return f"{o['abr_auteur']} {ref}".strip()


def urn_et_lien(o, p):
    coll = o["collection"]
    if coll in ("perseus", "first1k"):
        urn = f"{o['urn']}:{p['ref']}"
        return urn, f"https://scaife.perseus.org/reader/{urn}/"
    if coll == "ocr":
        ident = o["urn"].split(":", 1)[1]
        cible = p["cible"] or ""
        return f"ia:{ident}#{cible}", f"https://archive.org/details/{ident}/page/{cible}/mode/1up"
    if coll == "dclp":
        return o["urn"], o["source_url"] or ""
    if coll == "lsj":
        return f"lsj:{p['cible'] or p['ref']}", ""
    if coll == "drive":
        return f"{o['urn']}#{p['cible'] or ''}", ""
    return o["urn"], ""


def etiquette(o):
    s = o["fiabilite"] or ""
    if o["score_ocr"] is not None:
        s += f" ; {round(100 * o['score_ocr'])} % de mots grecs reconnus"
    return s


# ---------------------------------------------------------------------------
# Surlignage et extraits
# ---------------------------------------------------------------------------

def positions(texte, termes, exact=False, plier=False):
    """Intervalles (début, fin) des mots du texte original qui correspondent aux termes."""
    mots = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"[\ẁ-ͯ᾽᾿ʼ’']+", texte)]
    if exact:
        formes = [forme_exacte(w) for _, _, w in mots]
    else:
        formes = [normaliser(w) for _, _, w in mots]
        if plier:
            formes = [plier_ocr(f) for f in formes]
    res = []
    for brut, alts, prefixe in termes:
        if prefixe == "lemme":
            if exact:
                continue
            cibles = alts[0]
            for i, f in enumerate(formes):
                if f in cibles:
                    res.append((mots[i][0], mots[i][1]))
            continue
        cible = [{x} for x in forme_exacte(brut).split()] if exact else alts
        n = len(cible)
        if not n:
            continue
        for i in range(len(formes) - n + 1):
            ok = True
            for k in range(n):
                f, cs = formes[i + k], cible[k]
                if prefixe and k == n - 1:
                    if not any(f.startswith(c) for c in cs):
                        ok = False
                        break
                elif f not in cs:
                    ok = False
                    break
            if ok:
                res.append((mots[i][0], mots[i + n - 1][1]))
    return sorted(res)


def tous_presents(texte, termes, plier=False):
    """Filtre --exact : chaque terme positif doit figurer avec ses diacritiques."""
    for t in termes:
        if t[2] == "lemme":
            continue
        if not positions(texte, [t], exact=True):
            return False
    return True


def marquer(texte, pos, couleur):
    if not pos:
        return texte
    out, k = [], 0
    for a, b in pos:
        if a < k:
            continue
        out.append(texte[k:a])
        out.append(f"\033[1;31m{texte[a:b]}\033[0m" if couleur else f"«{texte[a:b]}»")
        k = b
    out.append(texte[k:])
    return "".join(out)


def extrait(texte, pos, largeur=220):
    if len(texte) <= 2 * largeur + 40 or not pos:
        return texte if len(texte) <= 2 * largeur + 40 else texte[:2 * largeur] + " …", pos
    a = max(0, pos[0][0] - largeur)
    b = min(len(texte), pos[0][1] + largeur)
    while a > 0 and not texte[a - 1].isspace():
        a -= 1
    while b < len(texte) and not texte[b].isspace():
        b += 1
    morceau = ("… " if a > 0 else "") + texte[a:b] + (" …" if b < len(texte) else "")
    dec = a - (2 if a > 0 else 0)
    pos2 = [(x - dec, y - dec) for x, y in pos if x >= a and y <= b]
    return morceau, pos2


# ---------------------------------------------------------------------------
# Recherche
# ---------------------------------------------------------------------------

def sans_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "") if not unicodedata.combining(c)).lower()


def filtre_oeuvres(con, a):
    """Ensemble des id d'œuvres admises (None = toutes)."""
    conds, params = [], []
    if a.collection:
        conds.append("collection IN (%s)" % ",".join("?" * len(a.collection)))
        params += a.collection
    if a.sans_ocr:
        conds.append("collection NOT IN ('ocr', 'drive')")
    if not a.toutes_editions:
        conds.append("(prioritaire = 1 OR collection IN ('ocr', 'drive', 'dclp'))")
    rows = con.execute("SELECT id, auteur, abr_auteur, tlg_auteur, titre, abr_titre, tlg_oeuvre, urn FROM oeuvres"
                       + (" WHERE " + " AND ".join(conds) if conds else ""), params).fetchall()
    ids = set()
    au = sans_accents(a.auteur) if a.auteur else None
    oe = sans_accents(a.oeuvre) if a.oeuvre else None
    for r in rows:
        if au and not any(au in sans_accents(x) for x in (r[1], r[2], r[3])):
            continue
        if oe and not any(oe in sans_accents(x) for x in (r[4], r[5], r[6], r[7])):
            continue
        ids.add(r[0])
    if not conds and not au and not oe:
        return None
    return ids


def charger_oeuvres(con, ids):
    if not ids:
        return {}
    out = {}
    cols = ["id", "collection", "urn", "urn_oeuvre", "tlg_auteur", "tlg_oeuvre", "auteur", "titre",
            "abr_auteur", "abr_titre", "edition", "fiabilite", "score_ocr", "source_url"]
    ids = list(ids)
    for k in range(0, len(ids), 900):
        lot = ids[k:k + 900]
        for r in con.execute(f"SELECT {', '.join(cols)} FROM oeuvres WHERE id IN ({','.join('?' * len(lot))})", lot):
            out[r[0]] = dict(zip(cols, r))
    return out


def chercher(con, a):
    lemmes = None
    if a.lemme:
        def lemmes(mot):
            rows = con.execute("SELECT DISTINCT forme FROM formes WHERE lemme_norm = ?", (mot,)).fetchall()
            return sorted({r[0] for r in rows if r[0]} | {mot})
    var = not (a.exact or a.sans_variantes)
    fts, termes = analyser(a.requete, lemmes=lemmes, var=var)
    fts_souple, termes_souples = analyser(a.requete, plier=True, lemmes=lemmes, var=var)
    if not termes:
        sys.exit("requête vide")
    admis = filtre_oeuvres(con, a)
    trouves = {}  # id passage → mode
    try:
        for (pid,) in con.execute("SELECT rowid FROM passages_fts WHERE passages_fts MATCH ?", (fts,)):
            trouves[pid] = "normal"
        if not a.strict:
            for (pid,) in con.execute("SELECT rowid FROM souple_fts WHERE souple_fts MATCH ?", (fts_souple,)):
                trouves.setdefault(pid, "souple")
    except sqlite3.OperationalError as e:
        sys.exit(f"requête invalide pour FTS5 : {fts}\n({e})")
    # expressions à cheval sur deux passages
    chevauchements = []
    if not a.sans_chevauchement:
        for (pid,) in con.execute("SELECT rowid FROM fenetres_fts WHERE fenetres_fts MATCH ?", (fts,)):
            if pid not in trouves and pid + 1 not in trouves:
                chevauchements.append(pid)
    ids = list(trouves) + chevauchements + [p + 1 for p in chevauchements]
    passages = {}
    cols = ["id", "oeuvre_id", "ordre", "ref", "locuteur", "texte", "norm", "cible", "repere"]
    for k in range(0, len(ids), 900):
        lot = ids[k:k + 900]
        for r in con.execute(f"SELECT {', '.join(cols)} FROM passages WHERE id IN ({','.join('?' * len(lot))})", lot):
            passages[r[0]] = dict(zip(cols, r))
    oeuvres = charger_oeuvres(con, {p["oeuvre_id"] for p in passages.values()})
    resultats = []
    for pid, mode in trouves.items():
        p = passages.get(pid)
        if not p or (admis is not None and p["oeuvre_id"] not in admis):
            continue
        o = oeuvres[p["oeuvre_id"]]
        if a.exact and not tous_presents(p["texte"], termes):
            continue
        resultats.append({"p": p, "o": o, "mode": mode})
    for pid in chevauchements:
        p, q = passages.get(pid), passages.get(pid + 1)
        if not p or not q or p["oeuvre_id"] != q["oeuvre_id"]:
            continue
        if admis is not None and p["oeuvre_id"] not in admis:
            continue
        o = oeuvres[p["oeuvre_id"]]
        texte = p["texte"] + " ‖ " + q["texte"]
        if a.exact and not tous_presents(texte, termes):
            continue
        fusion = dict(p)
        fusion["texte"] = texte
        fusion["ref_fin"] = q["ref"]
        resultats.append({"p": fusion, "o": o, "mode": "chevauchement"})
    resultats.sort(key=lambda r: (RANG_COLL.get(r["o"]["collection"], 9), sans_accents(r["o"]["abr_auteur"]),
                                  sans_accents(r["o"]["abr_titre"]), r["o"]["id"], r["p"]["ordre"]))
    return resultats, termes, termes_souples, fts


def contexte(con, p, n):
    rows = con.execute("SELECT ordre, ref, texte FROM passages WHERE oeuvre_id = ? AND ordre BETWEEN ? AND ? "
                       "ORDER BY ordre", (p["oeuvre_id"], p["ordre"] - n, p["ordre"] + n)).fetchall()
    return rows


def afficher(con, resultats, termes, termes_souples, a):
    couleur = sys.stdout.isatty() and not a.json
    if a.json:
        out = []
        for r in resultats[:a.max]:
            p, o = r["p"], r["o"]
            urn, lien = urn_et_lien(o, p)
            ref = reference(o, p)
            if p.get("ref_fin"):
                ref += f" → {p['ref_fin']}"
            d = {"reference": ref, "urn": urn, "lien": lien, "collection": o["collection"],
                 "fiabilite": etiquette(o), "mode": r["mode"], "texte": p["texte"]}
            if a.contexte:
                d["contexte"] = [{"ref": x[1], "texte": x[2]} for x in contexte(con, p, a.contexte)]
            out.append(d)
        print(json.dumps({"total": len(resultats), "resultats": out}, ensure_ascii=False, indent=1))
        return
    print(f"{len(resultats)} résultat(s)" + (f" — {a.max} premiers affichés" if len(resultats) > a.max else ""))
    for r in resultats[:a.max]:
        p, o = r["p"], r["o"]
        urn, lien = urn_et_lien(o, p)
        ref = reference(o, p)
        if p.get("ref_fin"):
            ref += f" → {p['ref_fin']} (à cheval)"
        souple = r["mode"] == "souple"
        tt = termes_souples if souple else termes
        print()
        tete = f"{ref}"
        if p.get("locuteur"):
            tete += f"  [{p['locuteur']}]"
        print(("\033[1m" + tete + "\033[0m") if couleur else tete)
        info = f"    {urn}"
        if lien:
            info += f"  {lien}"
        if o["collection"] in ("ocr", "drive") or souple:
            info += f"\n    ({etiquette(o)}{' ; trouvé par l’index souple' if souple else ''})"
        print(info)
        if a.contexte:
            for ordre, rf, tx in contexte(con, p, a.contexte):
                pos = positions(tx, tt, a.exact, souple)
                ligne, pos2 = (tx, pos) if a.complet else extrait(tx, pos)
                marque = "▸" if ordre == p["ordre"] else " "
                print(f"  {marque} {rf}: {marquer(ligne, pos2, couleur)}")
        else:
            pos = positions(p["texte"], tt, a.exact, souple)
            ligne, pos2 = (p["texte"], pos) if a.complet else extrait(p["texte"], pos)
            print("    " + marquer(ligne, pos2, couleur))


def lister_oeuvres(con, a):
    a.auteur = a.auteur or a.oeuvres
    ids = filtre_oeuvres(con, a)
    q = ("SELECT id, collection, abr_auteur, abr_titre, titre, urn, nb_passages, nb_mots, fiabilite, score_ocr, "
         "prioritaire FROM oeuvres")
    rows = con.execute(q).fetchall()
    motif = sans_accents(a.oeuvres)
    n = 0
    for r in rows:
        if ids is not None and r[0] not in ids and not any(motif in sans_accents(x) for x in (r[3], r[4], r[5])):
            continue
        if ids is None and not any(motif in sans_accents(x) for x in (r[2], r[3], r[4], r[5])):
            continue
        n += 1
        score = f" ; {round(100 * r[9])} % reconnus" if r[9] is not None else ""
        prio = "" if r[10] else " [édition secondaire]"
        print(f"{r[2]} {r[3]}".strip() + f" — {r[4][:80]} — {r[5]} — {r[6]} passages, {r[7]} mots — {r[8]}{score}{prio}")
    print(f"{n} œuvre(s)")


def statistiques(con):
    stats = json.loads(con.execute("SELECT valeur FROM meta WHERE cle = 'stats'").fetchone()[0])
    print(json.dumps(stats, ensure_ascii=False, indent=1))
    print()
    for r in con.execute("SELECT collection, count(*), sum(nb_passages), sum(nb_mots) FROM oeuvres GROUP BY collection "
                         "ORDER BY sum(nb_mots) DESC"):
        print(f"{r[0]:8s} {r[1]:6d} œuvres {r[2]:9d} passages {r[3]:11d} mots")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("requete", nargs="?", help="mots, \"expression\", préfixe*, OR, NOT, NEAR(… , n)")
    ap.add_argument("--exact", action="store_true", help="respecter accents, esprits, iota souscrit (grave = aigu)")
    ap.add_argument("--strict", action="store_true", help="sans l'index souple de l'OCR (χ = κ…)")
    ap.add_argument("--lemme", action="store_true", help="étendre chaque mot à ses formes (Diorisis)")
    ap.add_argument("--sans-variantes", action="store_true",
                    help="ne pas admettre les variantes orthographiques (ξυν-/συν-, ττ/σσ, ρρ/ρσ, γιγν-/γιν-)")
    ap.add_argument("-a", "--auteur", help="filtre sur l'auteur (abréviation, nom, tlgNNNN) : « Eur », « Hsch »")
    ap.add_argument("-o", "--oeuvre", help="filtre sur l'œuvre (abréviation, titre, URN) : « Hel », « tlg014 »")
    ap.add_argument("--collection", nargs="*", choices=list(RANG_COLL), help="restreindre aux collections")
    ap.add_argument("--sans-ocr", action="store_true", help="exclure l'OCR et les PDF")
    ap.add_argument("--toutes-editions", action="store_true", help="inclure les éditions secondaires d'une même œuvre")
    ap.add_argument("--sans-chevauchement", action="store_true", help="ne pas chercher à cheval sur deux passages")
    ap.add_argument("-c", "--contexte", type=int, default=0, help="nombre de passages de contexte avant/après")
    ap.add_argument("-n", "--max", type=int, default=50, help="nombre maximal de résultats affichés (50)")
    ap.add_argument("--complet", action="store_true", help="afficher les passages en entier")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--oeuvres", metavar="MOTIF", help="lister les œuvres indexées correspondant au motif")
    ap.add_argument("--stats", action="store_true", help="statistiques de l'index")
    ap.add_argument("--base", default=os.environ.get("CORPUS_INDEX", str(BASE)))
    a = ap.parse_args()
    if not Path(a.base).exists():
        sys.exit(f"index absent : {a.base} (lancer outils/corpus/indexer.py)")
    con = sqlite3.connect(f"file:{a.base}?mode=ro", uri=True)
    if a.stats:
        statistiques(con)
        return
    if a.oeuvres:
        lister_oeuvres(con, a)
        return
    if not a.requete:
        ap.error("requête manquante")
    resultats, termes, termes_souples, fts = chercher(con, a)
    afficher(con, resultats, termes, termes_souples, a)


if __name__ == "__main__":
    main()
