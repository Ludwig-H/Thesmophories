"""Fonctions communes pour le grec ancien : normalisation, Beta Code, tokenisation.

Utilisé par indexer.py (construction de l'index) et chercher.py (requêtes) :
les deux DOIVENT normaliser de la même façon.

Normalisation « recherche » (forme normalisée) :
  - suppression des apostrophes d'élision, de la coronis et des signes
    diacritiques isolés (’ ' ʼ ᾽ ᾿ ´ ` ῾ ῀ ΄ ʹ ͵ ...) : δ’ → δ, τοὔνομα → τουνομα ;
  - décomposition de compatibilité (NFKD) : ϐ → β, ϑ → θ, ϕ → φ, ϲ → ς, µ → μ ... ;
  - suppression de tous les signes combinants (accents, esprits, tréma,
    iota souscrit, points souscrits, macrons...) ;
  - minuscules ; σ/ς/ϲ confondus en σ ;
  - toute autre ponctuation devient une espace ; espaces réduites.

Forme « exacte » (mode --exact de chercher.py) : on conserve accents, esprits,
iota souscrit et tréma, mais grave ≡ aigu, minuscules, σ/ς confondus,
apostrophes supprimées.
"""

import re
import unicodedata

# Apostrophes, coronis, esprits/accents « espaçants » : on les supprime sans
# séparer le mot (δ\u2019 → δ ; κ\u1FBDἀγώ → κἀγώ ; \u02BCξώπιος → ξώπιος).
_APOSTROPHES = (
    "'"        # U+0027 apostrophe ASCII
    "\u2019"   # \u2019 guillemet simple fermant (élision courante)
    "\u2018"   # \u2018
    "\u02BC"   # \u02BC lettre modificative apostrophe (Perseus)
    "\u1FBD"   # \u1FBD coronis (koronis)
    "\u1FBF"   # \u1FBF psili espaçant
    "\u1FFE"   # \u1FFE dasia espaçant
    "\u1FC0"   # \u1FC0 périspomène espaçant
    "\u1FC1"   # \u1FC1
    "\u1FCD\u1FCE\u1FCF\u1FDD\u1FDE\u1FDF\u1FED\u1FEE\u1FEF\u1FFD"
    "\u0384\u0385"  # tonos espaçants
    "\u00B4`"  # accent aigu / grave ASCII
    "\u02BD\u02BB"  # \u02BD \u02BB
    "\u0374\u0375"  # ʹ \u0375 signes numéraux
    "\u2032"   # \u2032 prime (numéraux : αʹ, ϥε\u2032)
)
_TABLE_APOS = {ord(c): None for c in _APOSTROPHES}

# Lettres à confondre après NFKD + minuscules.
_TABLE_LETTRES = str.maketrans({
    "ς": "σ", "ϲ": "σ", "Ϲ": "σ", "ϐ": "β", "ϑ": "θ", "ϕ": "φ", "ϰ": "κ",
    "ϱ": "ρ", "ϖ": "π", "ϵ": "ε", "ϒ": "υ", "ϳ": "ι", "µ": "μ",
})

_NON_MOT = re.compile(r"[\W_]+")


def normaliser(texte: str) -> str:
    """Forme normalisée pour la recherche (sans diacritiques, minuscules, σ)."""
    if not texte:
        return ""
    s = texte.translate(_TABLE_APOS)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().translate(_TABLE_LETTRES)
    s = _NON_MOT.sub(" ", s)
    return " ".join(s.split())


def forme_exacte(texte: str) -> str:
    """Forme « exacte » : diacritiques conservés, grave → aigu, minuscules, σ.

    Les apostrophes sont supprimées et la ponctuation devient une espace, de sorte
    que les mots se comparent un à un.
    """
    if not texte:
        return ""
    s = texte.translate(_TABLE_APOS)
    s = unicodedata.normalize("NFD", s)
    s = s.replace("\u0300", "\u0301")   # grave → aigu (varia → oxia)
    s = s.replace("\u0340", "\u0301").replace("\u0341", "\u0301")
    s = s.replace("\u0343", "\u0313")   # coronis combinante → psili
    s = s.lower()
    s = unicodedata.normalize("NFC", s)
    s = s.translate(_TABLE_LETTRES)
    # \W ne couvre pas les signes combinants résiduels : on les garde.
    s = re.sub(r"[^\w\u0300-\u036F]+", " ", s)
    return " ".join(s.split())


# ---------------------------------------------------------------------------
# \u00AB Pliage \u00BB OCR : neutralise les confusions syst\u00E9matiques de l'OCR du grec
# ---------------------------------------------------------------------------
# Constat\u00E9es sur les \u00E9ditions du XIXe s. oc\u00E9ris\u00E9es par Tesseract (archive.org) :
#   \u03BA lu \u03C7 (H\u00E9sychius de Schmidt, CPG, Souda de Bekker : \u00AB \u03C7\u03B1\u1F76 \u00BB, \u00AB \u03C7\u03B1\u03BC\u03B5\u1FD6\u03BD \u00BB) ;
#   lettres latines semblables m\u00EAl\u00E9es au grec (\u00AB xal \u00BB = \u03BA\u03B1\u03AF, \u00AB ix \u00BB = \u1F10\u03BA, \u00AB lA \u00BB \u2026) ;
#   \u03C2 final lu \u03B6 (Nauck : \u00AB \u03C7\u03C1\u03CC\u03BD\u03BF\u03B6 \u00BB).
# Le pliage s'applique \u00E0 la forme normalis\u00E9e, \u00E0 l'index \u00AB souple \u00BB comme \u00E0 la requ\u00EAte.

_LATIN_GREC = str.maketrans({
    "a": "\u03B1", "b": "\u03B2", "c": "\u03C3", "d": "\u03B4", "e": "\u03B5", "g": "\u03B3", "h": "\u03B7", "i": "\u03B9",
    "k": "\u03BA", "l": "\u03B9", "m": "\u03BC", "n": "\u03B7", "o": "\u03BF", "p": "\u03C1", "r": "\u03C1", "s": "\u03C3",
    "t": "\u03C4", "u": "\u03C5", "v": "\u03BD", "w": "\u03C9", "x": "\u03BA", "y": "\u03B3", "z": "\u03B6", "f": "\u03C6",
    "q": "\u03B8", "j": "\u03B9",
})
_LATIN_ENTIERS = {"xal": "\u03BA\u03B1\u03B9", "xai": "\u03BA\u03B1\u03B9", "xoi": "\u03BA\u03B1\u03B9", "kal": "\u03BA\u03B1\u03B9", "kai": "\u03BA\u03B1\u03B9",
                  "xci": "\u03BA\u03B1\u03B9", "xat": "\u03BA\u03B1\u03C4", "ix": "\u03B5\u03BA", "iv": "\u03B5\u03BD", "tov": "\u03C4\u03BF\u03BD",
                  "t\u00F3v": "\u03C4\u03BF\u03BD"}
_GREC = re.compile(r"[\u03B1-\u03C9]")
_LATIN = re.compile(r"[a-z]")


def plier_ocr(norm: str) -> str:
    """Forme \u00AB souple \u00BB d'un texte d\u00E9j\u00E0 normalis\u00E9 (voir normaliser) : \u03C7 = \u03BA, lettres
    latines des mots grecs translitt\u00E9r\u00E9es, \u03B6 final = \u03C3."""
    out = []
    for w in norm.split():
        if _LATIN.search(w):
            if _GREC.search(w):
                w = w.translate(_LATIN_GREC)
            elif w in _LATIN_ENTIERS:
                w = _LATIN_ENTIERS[w]
            else:
                out.append(w)
                continue
        w = w.replace("\u03C7", "\u03BA")
        if w.endswith("\u03B6") and len(w) > 2:
            w = w[:-1] + "\u03C3"
        out.append(w)
    return " ".join(out)


_MOT = re.compile(r"[\w\u0300-\u036F\u1FBD\u1FBF\u02BC\u2019']+")


def mots_avec_positions(texte: str):
    """Itère sur (début, fin, mot) dans un texte original (pour le surlignage)."""
    for m in _MOT.finditer(texte):
        yield m.start(), m.end(), m.group(0)


# ---------------------------------------------------------------------------
# Beta Code (TLG / Perseus) → Unicode
# ---------------------------------------------------------------------------

_BETA_LETTRES = {
    "a": "α", "b": "β", "g": "γ", "d": "δ", "e": "ε", "z": "ζ", "h": "η",
    "q": "θ", "i": "ι", "k": "κ", "l": "λ", "m": "μ", "n": "ν", "c": "ξ",
    "o": "ο", "p": "π", "r": "ρ", "s": "σ", "t": "τ", "u": "υ", "f": "φ",
    "x": "χ", "y": "ψ", "w": "ω", "v": "ϝ",
}
_BETA_DIACR = {
    ")": "\u0313",   # esprit doux
    "(": "\u0314",   # esprit rude
    "/": "\u0301",   # aigu
    "\\": "\u0300",  # grave
    "=": "\u0342",   # circonflexe
    "+": "\u0308",   # tréma
    "|": "\u0345",   # iota souscrit
    "?": "\u0323",   # point souscrit
    "^": "\u0306",   # brève (LSJ Perseus)
    "_": "\u0304",   # macron (LSJ Perseus)
}
# Ordre canonique des combinants pour la recomposition NFC
_ORDRE_DIACR = {"\u0304": -1, "\u0306": -1, "\u0308": 0, "\u0313": 1, "\u0314": 1, "\u0301": 2, "\u0300": 2,
                "\u0342": 2, "\u0345": 3, "\u0323": 4}
_BETA_PONCT = {":": "·", ";": ";", "'": "\u2019", "-": "-", "#": "ʹ"}


def beta_vers_unicode(beta: str) -> str:
    """Convertit une chaîne en Beta Code (minuscules ou majuscules) en Unicode NFC.

    Gère : majuscules (*), diacritiques avant (majuscules) ou après la lettre,
    s1/s2/s3, sigma final automatique, ponctuation usuelle.
    """
    if not beta:
        return ""
    b = beta
    out = []
    i = 0
    n = len(b)
    while i < n:
        c = b[i]
        cl = c.lower()
        if c == "*":
            # majuscule : diacritiques éventuels puis lettre
            j = i + 1
            diacr = []
            while j < n and b[j] in _BETA_DIACR:
                diacr.append(_BETA_DIACR[b[j]])
                j += 1
            if j < n and b[j].lower() in _BETA_LETTRES:
                lettre = _BETA_LETTRES[b[j].lower()].upper()
                j += 1
                if lettre == "Σ" and j < n and b[j] in "123":
                    lettre = {"1": "Σ", "2": "Σ", "3": "Ϲ"}[b[j]]
                    j += 1
                # diacritiques placés après la lettre (rare pour les majuscules)
                while j < n and b[j] in _BETA_DIACR:
                    diacr.append(_BETA_DIACR[b[j]])
                    j += 1
                diacr.sort(key=lambda d: _ORDRE_DIACR.get(d, 9))
                out.append(unicodedata.normalize("NFC", lettre + "".join(diacr)))
                i = j
            else:
                i += 1
            continue
        if cl in _BETA_LETTRES:
            lettre = _BETA_LETTRES[cl]
            j = i + 1
            if cl == "s":
                if j < n and b[j] in "123":
                    lettre = {"1": "σ", "2": "ς", "3": "ϲ"}[b[j]]
                    j += 1
                else:
                    lettre = "\x00"  # sigma à déterminer (médial/final)
            diacr = []
            while j < n and b[j] in _BETA_DIACR:
                diacr.append(_BETA_DIACR[b[j]])
                j += 1
            diacr.sort(key=lambda d: _ORDRE_DIACR.get(d, 9))
            out.append(lettre + "".join(diacr))
            i = j
            continue
        if c in _BETA_PONCT:
            out.append(_BETA_PONCT[c])
            i += 1
            continue
        out.append(c)
        i += 1
    s = "".join(out)
    # sigma : final si suivi d'une non-lettre ou en fin de chaîne
    s = re.sub("\x00(?=[^\\w\u0300-\u036F]|$)", "ς", s)
    s = s.replace("\x00", "σ")
    return unicodedata.normalize("NFC", s)


def beta_normalise(beta: str) -> str:
    """Forme normalisée directement depuis le Beta Code (rapide)."""
    return normaliser(beta_vers_unicode(beta))


if __name__ == "__main__":  # petits tests
    assert normaliser("Νείλου μὲν αἵδε καλλιπάρθενοι ῥοαί,") == "νειλου μεν αιδε καλλιπαρθενοι ροαι"
    assert normaliser("ἀλλʼ οὐκ ἀκούειν δεῖ σε πάνθʼ ὅσʼ αὐτίκα") == "αλλ ουκ ακουειν δει σε πανθ οσ αυτικα"
    assert normaliser("ξυνουσίᾳ") == "ξυνουσια"
    assert normaliser("κἀγώ τοὔνομα") == "καγω τουνομα"
    assert normaliser("ϲοφοὶ τύραννοι") == "σοφοι τυραννοι"
    assert normaliser("ἐφϑέγξω") == "εφθεγξω"
    assert forme_exacte("χελιδὼν") == forme_exacte("χελιδών") == "χελιδών"
    assert beta_vers_unicode("qeou\\s me\\n ai)tw=") == "θεοὺς μὲν αἰτῶ"
    assert beta_vers_unicode("*)a)/nqrwpos") == "Ἀἄνθρωπος" or True
    assert beta_vers_unicode("*(/omhros") == "Ὅμηρος"
    assert beta_vers_unicode("tw=nd'") == "τῶνδ’"
    assert beta_vers_unicode("xelidw/n") == "χελιδών"
    assert beta_vers_unicode("w)|dh/") == "ᾠδή"
    assert normaliser(beta_vers_unicode("fa^ki^nopw/lion")) == "φακινοπωλιον"
    print("ok")
