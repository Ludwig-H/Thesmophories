#!/usr/bin/env python3
"""Polices Kleinlogel des éditions De Gruyter : rétablir le texte grec de la couche texte.

Les PDF d'Hésychius (Latte–Hansen–Cunningham) et de la Synagoge (Cunningham) sont composés
dans les polices Kleinlogel (Type 1/CFF incorporées). Les noms de glyphes de ces polices
sont brouillés : ils viennent d'un autre vecteur d'encodage que celui des dessins (le glyphe
nommé « epsilongrave » est un β, « alpha » est le point en haut ·, « five » l'esprit doux
avec aigu ῎…), si bien que la couche texte extraite est du charabia. En revanche, le lien
nom → dessin est constant : sur les cinq PDF, chaque couple (famille, nom de glyphe) a
toujours le même contour (contrôle par empreinte des contours, sous-programmes résolus).

D'où une table (famille, nom de glyphe) → caractère(s) Unicode, `kleinlogel.tsv`, établie
une fois pour toutes sur les glyphes eux-mêmes (vote de l'OCR aligné sur les glyphes, puis
contrôle visuel de chaque glyphe dans son contexte), et ce module, qui :
  - lit les polices d'un PDF (famille, charset CFF, encodage code → nom) ;
  - réécrit en mémoire le /ToUnicode de chaque police concernée d'après la table, de sorte
    que l'extraction ordinaire de PyMuPDF (get_text) donne le grec exact, accents compris ;
  - liste les glyphes d'une page (famille, nom, boîte) pour le contrôle.

La table ne contient aucun texte des éditions : elle est versionnée.

  python3 outils/corpus/kleinlogel.py FICHIER.pdf [PAGE]   # texte rétabli d'une page
"""

import csv
import io
import re
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
TABLE = ICI / "kleinlogel.tsv"

# Noms tronqués dans certains PDF (« KleinlogelPiHaken-Regula ») → nom complet.
FAMILLES_CONNUES = [
    "Kleinlogel-Upright", "Kleinlogel-Bold", "Kleinlogel-Italic",
    "KleinlogelNeu-Upright", "KleinlogelNeu-Bold", "KleinlogelNeu-Italic",
    "KleinlogelNeuPunkt-Upright", "KleinlogelPunkt-Upright", "KleinlogelStrich-Upright",
    "KleinlogelPiHaken-Regular", "KleinlogelNeuPiHaken-Regular",
    "MathematicalPiOneBQ-Regular", "SciencePiBQ", "SymbolNeu", "AGFiguresPiBQneu-Regular",
]


def famille(base):
    """Nom de famille d'une police PDF : sans préfixe de sous-ensemble, complété s'il est tronqué."""
    f = base.split("+")[-1]
    if f in FAMILLES_CONNUES:
        return f
    for g in FAMILLES_CONNUES:
        if len(f) >= 12 and g.startswith(f):
            return g
    return f


NORMALES = {"Kleinlogel-Upright", "KleinlogelNeu-Upright", "Kleinlogel-Bold", "KleinlogelNeu-Bold",
            "Kleinlogel-Italic", "KleinlogelNeu-Italic"}
POINTEES = {"KleinlogelNeuPunkt-Upright", "KleinlogelPunkt-Upright"}   # lettre + point souscrit
SURLIGNEES = {"KleinlogelStrich-Upright"}                              # lettre + trait suscrit
PIHAKEN = {"KleinlogelPiHaken-Regular", "KleinlogelNeuPiHaken-Regular"}


def concernee(fam, table=None):
    """La police doit-elle être décodée par la table ?"""
    if fam.startswith("Kleinlogel"):
        return True
    return bool(table) and any(k[0] == fam for k in table)


def caractere(fam, nom, table=None):
    """Texte Unicode d'un glyphe (famille, nom), ou None s'il est inconnu de la table."""
    table = lire_table() if table is None else table
    if (fam, nom) in table:
        return table[(fam, nom)]
    if fam in PIHAKEN:
        return table.get(("KleinlogelPiHaken", nom))
    base = table.get(("Kleinlogel", nom))
    if base is None or fam in NORMALES or not fam.startswith("Kleinlogel"):
        return base if fam.startswith("Kleinlogel") else None
    if not base[:1].isalpha():   # ponctuation et signes : ni point souscrit ni trait suscrit
        return base
    if fam in POINTEES:
        return base + "\u0323"
    if fam in SURLIGNEES:
        return base + "\u0305"
    return base


_CACHE_TABLE = {}

# Encodage standard d'Adobe pour l'ASCII imprimable (polices CFF que fontTools ne lit pas).
STANDARD = dict(zip(range(0x21, 0x7F), """exclam quotedbl numbersign dollar percent ampersand quoteright
parenleft parenright asterisk plus comma hyphen period slash zero one two three four five six seven
eight nine colon semicolon less equal greater question at A B C D E F G H I J K L M N O P Q R S T U V
W X Y Z bracketleft backslash bracketright asciicircum underscore quoteleft a b c d e f g h i j k l m n
o p q r s t u v w x y z braceleft bar braceright asciitilde""".split()))


def lire_table(chemin=TABLE):
    """(famille, nom de glyphe) → texte Unicode (chaîne vide : glyphe à ignorer)."""
    chemin = Path(chemin)
    if chemin in _CACHE_TABLE:
        return _CACHE_TABLE[chemin]
    t = {}
    if chemin.exists():
        with open(chemin, encoding="utf-8") as f:
            lignes = [l for l in f if l.strip() and not l.startswith("#")]
        for r in csv.DictReader(lignes, delimiter="\t", quoting=csv.QUOTE_NONE):
            car = r["caractere"]
            if car.startswith("U+"):  # notation explicite (espaces, signes combinants)
                car = "".join(chr(int(x[2:], 16)) for x in car.split())
            t[(r["famille"], r["glyphe"])] = car
    _CACHE_TABLE[chemin] = t
    return t


def _cff(doc, xref):
    from fontTools.cffLib import CFFFontSet
    nm, ext, typ, buf = doc.extract_font(xref)
    if ext != "cff" or not buf:
        return None
    cff = CFFFontSet()
    cff.decompile(io.BytesIO(buf), None)
    return cff[cff.fontNames[0]]


def encodage(doc, xref, top=None):
    """code → nom de glyphe : encodage interne de la police CFF, puis /Differences du PDF."""
    noms = {}
    try:
        top = top or _cff(doc, xref)
        enc = getattr(top, "Encoding", None) if top is not None else None
        if isinstance(enc, list):
            noms.update({c: n for c, n in enumerate(enc) if n != ".notdef"})
    except Exception:
        pass
    t, v = doc.xref_get_key(xref, "Encoding")
    diff = ""
    if t == "xref":
        t2, diff = doc.xref_get_key(int(v.split()[0]), "Differences")
    elif t == "dict":
        m = re.search(r"/Differences\s*\[(.*?)\]", v, re.S)
        diff = m.group(1) if m else ""
    code = None
    for tok in re.findall(r"/[^\s/\[\]()<>]+|\d+", diff or ""):
        if tok.startswith("/"):
            if code is not None:
                noms[code] = tok[1:]
                code += 1
        else:
            code = int(tok)
    return noms


def polices(doc):
    """xref → {famille, charset, codes} pour les polices Type 1/CFF du document."""
    out = {}
    for i in range(len(doc)):
        for fo in doc[i].get_fonts():
            xref = fo[0]
            if xref in out or fo[2] != "Type1":
                continue
            fam = famille(fo[3])
            info = {"famille": fam, "base": fo[3], "charset": None, "codes": {}}
            try:
                top = _cff(doc, xref)
                if top is not None:
                    info["charset"] = list(top.charset)
                info["codes"] = encodage(doc, xref, top)
            except Exception:
                info["codes"] = encodage(doc, xref)
            out[xref] = info
    return out


def _cmap(codes_texte):
    """CMap ToUnicode (bfchar) pour un dictionnaire code → texte."""
    lignes = ["/CIDInit /ProcSet findresource begin", "12 dict begin", "begincmap",
              "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def",
              "/CMapName /Kleinlogel-UCS def", "/CMapType 2 def",
              "1 begincodespacerange", "<00> <FF>", "endcodespacerange"]
    items = sorted(codes_texte.items())
    for k in range(0, len(items), 100):
        bloc = items[k:k + 100]
        lignes.append(f"{len(bloc)} beginbfchar")
        for code, texte in bloc:
            hexa = "".join(f"{ord(c):04X}" if ord(c) < 0x10000 else
                           "".join(f"{u:04X}" for u in _utf16(c)) for c in texte) or "FFFD"
            lignes.append(f"<{code:02X}> <{hexa}>")
        lignes.append("endbfchar")
    lignes += ["endcmap", "CMapName currentdict /CMap defineresource pop", "end", "end"]
    return "\n".join(lignes).encode("ascii")


def _utf16(c):
    v = ord(c) - 0x10000
    return (0xD800 + (v >> 10), 0xDC00 + (v & 0x3FF))


def corriger(doc, table=None):
    """Réécrit en mémoire le /ToUnicode des polices décodables par la table.

    Renvoie {(famille, nom): nombre de codes} des glyphes absents de la table (inconnus)."""
    table = lire_table() if table is None else table
    inconnus = {}
    for xref, info in polices(doc).items():
        fam = info["famille"]
        if not concernee(fam, table):
            continue
        m = {}
        codes = dict(info["codes"])
        if info["charset"] is None:  # police CFF illisible : encodage standard pour l'ASCII
            for c in range(0x21, 0x7F):
                codes.setdefault(c, STANDARD.get(c))
        for code, nom in codes.items():
            if not nom or nom in (".notdef",):
                continue
            t = caractere(fam, nom, table)
            if t is not None:
                m[code] = t
            elif nom in ("space", "nbspace", "nonbreakingspace"):
                m[code] = " "
            elif not fam.startswith("Kleinlogel"):
                continue  # police de signes : extraction ordinaire pour les glyphes non listés
            else:
                inconnus[(fam, nom)] = inconnus.get((fam, nom), 0) + 1
                m[code] = "�"
        if not m:
            continue
        nx = doc.get_new_xref()
        doc.update_object(nx, "<<>>")
        doc.update_stream(nx, _cmap(m))
        doc.xref_set_key(xref, "ToUnicode", f"{nx} 0 R")
    return inconnus


def glyphes_page(doc, i, pol=None):
    """Glyphes d'une page : [{famille, nom, bbox, taille, police}] (gid → nom par le charset CFF)."""
    pol = pol or polices(doc)
    par_nom = {}
    for fo in doc[i].get_fonts():
        if fo[0] in pol:
            base = pol[fo[0]]["base"]
            # MuPDF tronque les noms de police à 31 caractères (préfixe de sous-ensemble compris)
            for nom in {base.split("+")[-1], base[:31].split("+")[-1]}:
                par_nom.setdefault(nom, []).append(fo[0])
    out = []
    for s in doc[i].get_texttrace():
        xs = par_nom.get(s["font"], [])
        info = pol[xs[0]] if len(xs) == 1 else None
        for c in s["chars"]:
            gid = c[1]
            nom = None
            if info and info["charset"] and 0 <= gid < len(info["charset"]):
                nom = info["charset"][gid]
            out.append({"famille": info["famille"] if info else famille(s["font"]), "nom": nom,
                        "ucs": c[0], "bbox": tuple(c[3]), "taille": s["size"], "police": s["font"]})
    return out


# ---------------------------------------------------------------------------
# Lignes de texte rétablies (après corriger(doc))
# ---------------------------------------------------------------------------

# Esprits et accents espaçants placés devant une capitale (« ῎Αβυδος ») → signes combinants.
ESPACANTS = {"\u1FBF": "\u0313", "\u1FFE": "\u0314", "\u1FCE": "\u0313\u0301", "\u1FCD": "\u0313\u0300",
             "\u1FCF": "\u0313\u0342", "\u1FDE": "\u0314\u0301", "\u1FDD": "\u0314\u0300",
             "\u1FDF": "\u0314\u0342"}
_RE_ESPACANT = re.compile("([" + "".join(ESPACANTS) + "])([ΑΕΗΙΟΥΩΡ])")


def composer(t):
    """« ῎Αβυδος » → « Ἄβυδος » ; puis NFC."""
    t = _RE_ESPACANT.sub(lambda m: unicodedata.normalize("NFC", m.group(2) + ESPACANTS[m.group(1)]), t)
    return unicodedata.normalize("NFC", t)


def _combinant(c):
    return bool(c) and all(unicodedata.combining(x) for x in c)


# Centre de l'encre des signes de chasse nulle, en millièmes de corps à droite de l'origine
# (contours des glyphes : iota souscrit 130–389, brève −3–281, point souscrit 60–160).
_ENCRE = {"\u0345": 260, "\u0306": 140, "\u0323": 110}
# Lettres qui peuvent porter le signe (sinon : toute lettre)
_PORTEURS = {"\u0345": "αηωΑΗΩ", "\u0306": "αιυΑΙΥ", "\u0308": "ιυΙΥ"}


def _porteur(mark, base):
    lettres = _PORTEURS.get(mark[:1])
    b = unicodedata.normalize("NFD", base)[:1]
    return b in lettres if lettres else b.isalpha()


def _rattacher(chars):
    """Rattache chaque signe combinant isolé (iota souscrit, brève, point souscrit : glyphes
    superposés à la lettre, avant ou après elle dans le flux) à la lettre qu'il recouvre."""
    bases = [k for k, ch in enumerate(chars) if not _combinant(ch["c"]) and ch["c"].strip()]
    attaches = {}
    for k, ch in enumerate(chars):
        if not _combinant(ch["c"]):
            continue
        # familles Punkt et Strich : un glyphe rend lettre + signe, le signe suit donc sa lettre
        if k and ("Punkt" in ch["police"] or "Strich" in ch["police"]) and chars[k - 1]["c"].strip() \
                and not _combinant(chars[k - 1]["c"]):
            attaches.setdefault(k - 1, []).append(k)
            continue
        x0, _, x1, _ = ch["bbox"]
        if x1 - x0 < 0.3:  # chasse nulle : l'encre est à droite de l'origine
            cx = x0 + _ENCRE.get(ch["c"][:1], 150) * ch.get("taille", 10) / 1000
        else:
            cx = (x0 + x1) / 2
        def dist(j):
            a, b = chars[j]["bbox"][0], chars[j]["bbox"][2]
            return 0 if a - 0.3 <= cx <= b + 0.3 else min(abs(cx - a), abs(cx - b))
        cands = [j for j in bases if _porteur(ch["c"], chars[j]["c"]) and dist(j) < 1.2 * ch.get("taille", 10)]
        if not cands:
            continue
        j = min(cands, key=lambda j: (dist(j), abs(j - k)))
        attaches.setdefault(j, []).append(k)
    places = {k for v in attaches.values() for k in v}
    out = []
    for k, ch in enumerate(chars):
        if k in places:
            continue
        out.append(ch)
        for m in attaches.get(k, []):
            out.append(dict(chars[m], bbox=ch["bbox"]))
    return out


def reporter_souscrit(a, b):
    """Iota souscrit égaré : PyMuPDF coupe une ligne justifiée en fragments, et le signe, qui
    précède sa lettre dans le flux, reste à la fin du fragment précédent (« ἐνͅ » + « ὧ »…).
    Le reporte sur la première lettre du fragment b (lignes de lignes_page) si elle peut le porter."""
    t = a["texte"].rstrip()
    if not t.endswith("\u0345"):
        return False
    tb = b["texte"].lstrip()
    if not tb or not _porteur("\u0345", tb[0]):
        return False
    nouveau = unicodedata.normalize("NFC", tb[0] + "\u0345")
    a["texte"] = t[:-1]
    b["texte"] = nouveau + tb[1:]
    for k in range(len(a["spans"]) - 1, -1, -1):
        sp = a["spans"][k]
        if sp[0].strip():
            if sp[0].rstrip().endswith("\u0345"):
                a["spans"][k] = (sp[0].rstrip()[:-1],) + tuple(sp[1:])
            break
    for k, sp in enumerate(b["spans"]):
        s = sp[0]
        s2 = s.lstrip()
        if s2:
            b["spans"][k] = (s[:len(s) - len(s2)] + nouveau + s2[1:],) + tuple(sp[1:])
            break
    return True


def lignes_page(page, flags=None):
    """Lignes d'une page (document passé par corriger()) :
    [{texte, bbox, spans: [(texte, police, taille, gras, bbox)]}], texte en NFC, espaces rétablies
    d'après l'écart entre caractères, signes combinants rattachés à leur lettre."""
    import pymupdf
    if flags is None:
        flags = pymupdf.TEXT_PRESERVE_WHITESPACE | pymupdf.TEXT_MEDIABOX_CLIP
    out = []
    for b in page.get_text("rawdict", flags=flags).get("blocks", []):
        for l in b.get("lines", []):
            chars = []
            for s in l.get("spans", []):
                coul = s.get("color", 0) or 0
                if s.get("alpha", 255) == 0 or all((coul >> d) & 255 >= 0xF0 for d in (0, 8, 16)):
                    continue  # texte invisible (blanc) : repentirs du compositeur
                gras = bool(s.get("flags", 0) & 16) or "Bold" in s.get("font", "")
                for ch in s.get("chars", []):
                    chars.append({"c": ch.get("c", ""), "bbox": ch["bbox"], "police": s.get("font", ""),
                                  "taille": s.get("size", 10) or 10, "gras": gras})
            if not chars:
                continue
            chars = _rattacher(chars)
            texte, spans, prec, cour = [], [], None, None
            for ch in chars:
                c = ch["c"]
                if c == "\uFFFD" or (len(c) == 1 and unicodedata.category(c) == "Cc"):
                    c = ""
                if not _combinant(c) and c and not c.isspace():
                    x0 = ch["bbox"][0]
                    if prec is not None and x0 - prec > 0.12 * ch["taille"] and texte and not texte[-1].isspace():
                        texte.append(" ")
                        if cour:
                            cour[0] += " "
                    prec = ch["bbox"][2]
                elif c.isspace():
                    prec = ch["bbox"][2]
                texte.append(c)
                cle = (ch["police"], round(ch["taille"], 1), ch["gras"])
                if cour is None or cour[1] != cle:
                    cour = [c, cle, list(ch["bbox"])]
                    spans.append(cour)
                else:
                    cour[0] += c
                    cour[2][2] = max(cour[2][2], ch["bbox"][2])
            t = composer("".join(texte))
            if not t.strip():
                continue
            out.append({"texte": t, "bbox": tuple(l["bbox"]),
                        "spans": [(composer(x[0]), x[1][0], x[1][1], x[1][2], tuple(x[2])) for x in spans]})
    return out


def texte_page(page):
    """Texte d'une page (document passé par corriger()), ligne par ligne."""
    return "\n".join(l["texte"] for l in lignes_page(page))


def main():
    import pymupdf
    doc = pymupdf.open(sys.argv[1])
    inconnus = corriger(doc)
    pages = [int(sys.argv[2]) - 1] if len(sys.argv) > 2 else range(len(doc))
    for i in pages:
        print(texte_page(doc[i]))
    if inconnus:
        print("glyphes absents de la table :", sorted(inconnus), file=sys.stderr)


if __name__ == "__main__":
    main()
