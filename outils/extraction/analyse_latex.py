#!/usr/bin/env python3
"""Analyse des sources LaTeX de l'auteur (macros reledmac/reledpar).

Module commun à `extraire_travaux.py` et `comparer_versions.py` :
- suppression des commentaires LaTeX en conservant la correspondance des positions ;
- arbre syntaxique minimal (commandes, groupes, texte) avec accolades équilibrées ;
- conversion en texte brut des fragments (commentaires, apparat, vers) ;
- arités des macros lues dans le préambule.

Aucune dépendance hors bibliothèque standard.
"""
from __future__ import annotations

import bisect
import re
import unicodedata
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# 1. Source : texte d'origine, texte actif (sans commentaires), correspondances
# ---------------------------------------------------------------------------


@dataclass
class Commentaire:
    debut: int          # position (texte d'origine) du '%'
    fin: int            # position de la fin de ligne
    texte: str          # texte après le '%'


class Source:
    """Fichier LaTeX : texte d'origine + texte « actif » (commentaires ôtés)."""

    def __init__(self, chemin: str, texte: str | None = None):
        self.chemin = chemin
        if texte is None:
            with open(chemin, encoding="utf-8") as f:
                texte = f.read()
        self.orig = texte
        self.debuts_lignes = [0] + [m.end() for m in re.finditer("\n", texte)]
        self.actif, self.amap, self.commentaires = self._oter_commentaires(texte)
        self._comm_debuts = [c.debut for c in self.commentaires]

    @staticmethod
    def _oter_commentaires(t: str):
        out: list[str] = []
        amap: list[int] = []
        comms: list[Commentaire] = []
        i, n = 0, len(t)
        while i < n:
            c = t[i]
            if c == "\\" and i + 1 < n:
                out.append(t[i:i + 2])
                amap.extend((i, i + 1))
                i += 2
                continue
            if c == "%":
                j = t.find("\n", i)
                if j == -1:
                    j = n
                comms.append(Commentaire(i, j, t[i + 1:j]))
                i = j + 1
                # TeX ignore les blancs en début de ligne suivante
                while i < n and t[i] in " \t":
                    i += 1
                continue
            out.append(c)
            amap.append(i)
            i += 1
        amap.append(n)
        return "".join(out), amap, comms

    def ligne_orig(self, pos_orig: int) -> int:
        """Numéro de ligne (1-based) d'une position du texte d'origine."""
        return bisect.bisect_right(self.debuts_lignes, pos_orig)

    def ligne_actif(self, pos_actif: int) -> int:
        pos_actif = max(0, min(pos_actif, len(self.amap) - 1))
        return self.ligne_orig(self.amap[pos_actif])

    def orig_de_actif(self, pos_actif: int) -> int:
        pos_actif = max(0, min(pos_actif, len(self.amap) - 1))
        return self.amap[pos_actif]

    def commentaires_entre(self, debut_orig: int, fin_orig: int) -> list[Commentaire]:
        i = bisect.bisect_left(self._comm_debuts, debut_orig)
        res = []
        while i < len(self.commentaires) and self.commentaires[i].debut < fin_orig:
            res.append(self.commentaires[i])
            i += 1
        return res


# ---------------------------------------------------------------------------
# 2. Arbre syntaxique
# ---------------------------------------------------------------------------


@dataclass
class Noeud:
    type: str                 # 'texte', 'cmd', 'groupe', 'nl', 'par', 'saut' (\\), 'math'
    debut: int                # positions dans le texte analysé
    fin: int
    nom: str = ""             # nom de commande (sans '\')
    texte: str = ""           # pour 'texte'
    args: list = field(default_factory=list)      # liste de listes de Noeud
    opt: list = field(default_factory=list)       # arguments optionnels (listes de Noeud)
    enfants: list = field(default_factory=list)   # pour 'groupe' / 'math'


# Arités des commandes LaTeX courantes (les macros de l'auteur sont lues dans le préambule)
ARITES_BASE = {
    "textbf": 1, "textit": 1, "emph": 1, "textsc": 1, "textsuperscript": 1,
    "textsubscript": 1, "hspace": 1, "vspace": 1, "href": 2, "url": 1, "text": 1,
    "mbox": 1, "overset": 2, "underset": 2, "frac": 2, "sout": 1, "dotuline": 1,
    "uline": 1, "uuline": 1, "sqrt": 1, "xrightarrow": 1, "rotatebox": 2, "setline": 1,
    "advanceline": 1, "color": 1, "textcolor": 2, "begin": 1, "end": 1, "label": 1,
    "ref": 1, "cite": 1, "footnote": 1, "oldstylenums": 1, "texorpdfstring": 2,
    "widearc": 1, "breve": 1, "hat": 1, "cancel": 1, "mathrm": 1, "mathit": 1,
    "ledleftnote": 1, "ledrightnote": 1, "linenumannotation": 1, "fancyhead": 1,
    "title": 1, "author": 1, "date": 1, "setcounter": 2, "addtocounter": 2,
    "includegraphics": 1, "caption": 1, "section": 1, "chapter": 1, "subsection": 1,
    "fbox": 1, "underline": 1, "textup": 1, "textrm": 1, "textsf": 1, "texttt": 1,
    "textnormal": 1, "makebox": 1, "raisebox": 2, "scalebox": 2, "resizebox": 3,
    "parbox": 2, "Afootnote": 1, "Bfootnote": 1, "Cfootnote": 1, "edtext": 2,
}
# Commandes acceptant un argument optionnel [..] avant les obligatoires
AVEC_OPTION = {"xrightarrow", "rotatebox", "linebreak", "pagebreak", "includegraphics",
               "makebox", "parbox", "raisebox", "fancyhead", "Afootnote", "Bfootnote",
               "Cfootnote", "sqrt", "section", "chapter", "subsection", "cite",
               "nolinebreak", "newline", "\\"}
ACCENTS = {"'", "`", "^", '"', "~", "=", ".", "u", "v", "H", "c", "d", "b", "r", "k"}


def lire_macros_preambule(preambule: str) -> dict:
    """Retourne {nom: (arite, corps)} pour les \\newcommand du préambule (non commentés)."""
    src = Source("<preambule>", preambule)
    t = src.actif
    macros = {}
    for m in re.finditer(r"\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z@]+)\}?\s*(?:\[(\d)\])?", t):
        nom, ar = m.group(1), int(m.group(2) or 0)
        # corps : groupe équilibré suivant
        i = m.end()
        while i < len(t) and t[i] in " \t\n":
            i += 1
        if i < len(t) and t[i] == "[":   # valeur par défaut d'un argument optionnel
            j = t.find("]", i)
            i = j + 1
        if i < len(t) and t[i] == "{":
            fin = fin_groupe(t, i)
            corps = t[i + 1:fin]
        else:
            corps = ""
        macros[nom] = (ar, corps)
    return macros


def fin_groupe(t: str, i: int) -> int:
    """Position de l'accolade fermante correspondant à t[i] == '{' (texte sans commentaires)."""
    assert t[i] == "{"
    prof = 0
    n = len(t)
    while i < n:
        c = t[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            prof += 1
        elif c == "}":
            prof -= 1
            if prof == 0:
                return i
        i += 1
    return n - 1


class Analyseur:
    """Construit l'arbre d'un fragment de texte actif."""

    def __init__(self, arites: dict):
        self.arites = dict(ARITES_BASE)
        self.arites.update(arites)

    def analyser(self, t: str, debut: int = 0, fin: int | None = None) -> list:
        if fin is None:
            fin = len(t)
        noeuds, _ = self._liste(t, debut, fin, fermant=None)
        return noeuds

    # -- interne -----------------------------------------------------------
    def _liste(self, t, i, fin, fermant):
        noeuds = []
        tampon_debut = None

        def vider(j):
            nonlocal tampon_debut
            if tampon_debut is not None and j > tampon_debut:
                noeuds.append(Noeud("texte", tampon_debut, j, texte=t[tampon_debut:j]))
            tampon_debut = None

        while i < fin:
            c = t[i]
            if fermant is not None and c == fermant:
                vider(i)
                return noeuds, i
            if c == "\\":
                vider(i)
                nd, i = self._commande(t, i, fin)
                noeuds.append(nd)
                continue
            if c == "{":
                vider(i)
                f = self._fin_groupe(t, i, fin)
                enfants, _ = self._liste(t, i + 1, f, fermant=None)
                noeuds.append(Noeud("groupe", i, f + 1, enfants=enfants))
                i = f + 1
                continue
            if c == "}":
                # accolade fermante orpheline : on l'ignore
                vider(i)
                i += 1
                continue
            if c == "$":
                vider(i)
                j = t.find("$", i + 1)
                if j == -1 or j >= fin:
                    j = fin - 1
                enfants, _ = self._liste(t, i + 1, j, fermant=None)
                noeuds.append(Noeud("math", i, j + 1, enfants=enfants))
                i = j + 1
                continue
            if c == "\n":
                vider(i)
                # ligne vide = \par
                j = i + 1
                while j < fin and t[j] in " \t":
                    j += 1
                if j < fin and t[j] == "\n":
                    while j < fin and t[j] in " \t\n":
                        j += 1
                    noeuds.append(Noeud("par", i, j))
                    i = j
                else:
                    noeuds.append(Noeud("nl", i, i + 1))
                    i += 1
                continue
            if tampon_debut is None:
                tampon_debut = i
            i += 1
        vider(i)
        return noeuds, i

    def _fin_groupe(self, t, i, fin):
        prof = 0
        while i < fin:
            c = t[i]
            if c == "\\":
                i += 2
                continue
            if c == "{":
                prof += 1
            elif c == "}":
                prof -= 1
                if prof == 0:
                    return i
            i += 1
        return fin - 1 if fin > 0 else 0

    def _sauter_blancs(self, t, i, fin, nl=True):
        while i < fin and (t[i] in " \t" or (nl and t[i] == "\n")):
            i += 1
        return i

    def _argument(self, t, i, fin):
        """Argument obligatoire : groupe {..} ou jeton isolé."""
        i = self._sauter_blancs(t, i, fin)
        if i >= fin:
            return [], i
        if t[i] == "{":
            f = self._fin_groupe(t, i, fin)
            enfants, _ = self._liste(t, i + 1, f, fermant=None)
            return enfants, f + 1
        if t[i] == "\\":
            nd, j = self._commande(t, i, fin, sans_args=True)
            return [nd], j
        return [Noeud("texte", i, i + 1, texte=t[i])], i + 1

    def _option(self, t, i, fin):
        j = self._sauter_blancs(t, i, fin, nl=False)
        if j < fin and t[j] == "[":
            prof = 0
            k = j
            while k < fin:
                if t[k] == "[":
                    prof += 1
                elif t[k] == "]":
                    prof -= 1
                    if prof == 0:
                        break
                k += 1
            enfants, _ = self._liste(t, j + 1, k, fermant=None)
            return enfants, k + 1
        return None, i

    def _commande(self, t, i, fin, sans_args=False):
        debut = i
        if i + 1 >= fin:
            return Noeud("texte", i, i + 1, texte="\\"), i + 1
        c = t[i + 1]
        if c.isascii() and (c.isalpha() or c == "@"):
            j = i + 1
            while j < fin and t[j].isascii() and (t[j].isalpha() or t[j] == "@"):
                j += 1
            nom = t[i + 1:j]
            k = j
            # TeX ignore les blancs après un mot de contrôle
            while k < fin and t[k] in " \t":
                k += 1
            nd = Noeud("cmd", debut, k, nom=nom)
            if sans_args:
                nd.fin = j
                return nd, j
            ar = self.arites.get(nom, 0)
            if nom in AVEC_OPTION:
                o, k2 = self._option(t, k, fin)
                if o is not None:
                    nd.opt.append(o)
                    k = k2
            if nom == "begin":
                # \begin{env} : on ne consomme que le nom (les arguments éventuels restent du contenu)
                a, k = self._argument(t, k, fin)
                nd.args.append(a)
                nd.fin = k
                return nd, k
            if nom in ACCENTS and len(nom) == 1:
                ar = max(ar, 1)
            for _ in range(ar):
                a, k = self._argument(t, k, fin)
                nd.args.append(a)
            nd.fin = k
            return nd, k
        # symbole de contrôle
        nom = c
        k = i + 2
        if nom == "\\":
            nd = Noeud("saut", debut, k, nom="\\\\")
            if k < fin and t[k] == "*":
                k += 1
            o, k2 = self._option(t, k, fin)
            if o is not None:
                k = k2
            nd.fin = k
            return nd, k
        nd = Noeud("cmd", debut, k, nom=nom)
        if nom in ACCENTS and not sans_args:
            a, k = self._argument(t, k, fin)
            nd.args.append(a)
            nd.fin = k
        return nd, k


# ---------------------------------------------------------------------------
# 3. Conversion en texte brut
# ---------------------------------------------------------------------------

EXPOSANTS = dict(zip(
    "0123456789+-()abcdefghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUW",
    "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁᵂ"))
INDICES = dict(zip("0123456789+-()aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉₊₋₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ"))


def exposant(s: str) -> str:
    s = s.strip()
    if s and all(ch in EXPOSANTS for ch in s):
        return "".join(EXPOSANTS[ch] for ch in s)
    return f"^({s})" if s else ""


def indice(s: str) -> str:
    s = s.strip()
    if s and all(ch in INDICES for ch in s):
        return "".join(INDICES[ch] for ch in s)
    return f"_({s})" if s else ""


SYMBOLES_MATH = {
    "cup": "∪", "simeq": "≃", "sim": "~", "times": "×", "to": "→", "emptyset": "∅",
    "subset": "⊂", "cdot": "·", "ldots": "…", "dots": "…", "cdots": "⋯", "smile": "⌣",
    "approx": "≈", "neq": "≠", "leq": "≤", "geq": "≥", "pm": "±", "infty": "∞",
    "rightarrow": "→", "leftarrow": "←", "Rightarrow": "⇒", "equiv": "≡", "circ": "∘",
    "quad": " ", "qquad": "  ", "prime": "′", "vert": "|", "mid": "|", "lbrace": "{",
    "rbrace": "}", "langle": "⟨", "rangle": "⟩", "times ": "×", "colon": ":",
    "bullet": "•", "star": "*", "ast": "*", "dagger": "†", "S": "§", "P": "¶",
}
SYMBOLES_TEXTE = {
    "oe": "œ", "OE": "Œ", "ae": "æ", "AE": "Æ", "ss": "ß", "ldots": "…", "dots": "…",
    "textasciicircum": "^", "S": "§", "dag": "†", "ddag": "‡", "textperiodcentered": "·",
    "guillemotleft": "«", "guillemotright": "»", "og": "« ", "fg": " »", "LaTeX": "LaTeX",
    "TeX": "TeX", "textbackslash": "\\", "copyright": "©", "pounds": "£", "i": "ı",
    "textendash": "–", "textemdash": "—", "textquoteright": "’", "textquoteleft": "‘",
    "slash": "/", "textbar": "|", "textless": "<", "textgreater": ">",
}
ACCENTS_COMB = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303",
                "=": "\u0304", ".": "\u0307", "u": "\u0306", "v": "\u030C", "H": "\u030B",
                "c": "\u0327", "d": "\u0323", "b": "\u0331", "r": "\u030A", "k": "\u0328"}

# commandes dont le contenu est transparent (mise en forme, langue, taille)
TRANSPARENTES_1 = {
    "italique", "textbf", "textit", "emph", "textsc", "grec", "latin", "francais",
    "anglais", "allemand", "italien", "espagnol", "difference", "lecon", "text", "mbox",
    "mathrm", "mathit", "Automatique", "renverse", "underline", "uline", "uuline",
    "dotuline", "textup", "textrm", "textsf", "texttt", "textnormal", "fbox", "auteur",
    "trimIamb", "trimIambFr", "trimIambCat", "trimIambCatFr", "tetramIamb", "tetramIambFr",
    "tetramTroch", "tetramTrochFr", "tetramIambCat", "tetramIambCatFr", "dimAnap",
    "dimAnapFr", "anap", "anapFr", "diDoch", "diDochFr", "tetramAnap", "tetramAnapFr",
    "chantAgath", "chantAgathFr", "prose", "proseFr", "chantChoeur", "chantChoeurFr",
    "paratragiques", "paratragiquesFr", "strophe", "Strophe", "oldstylenums", "makebox",
    "widearc", "cancel", "chap",
}
# commandes ignorées (avec leurs arguments)
IGNOREES = {
    "espace", "hspace", "vspace", "decalage", "decalageN", "Taille", "TaillePt",
    "label", "setline", "advanceline", "ligne", "linenumannotation", "decoupeVers",
    "setcounter", "addtocounter", "color", "includegraphics", "fancyhead", "enTeteG",
    "enTeteD", "passeLigne", "skipnumbering", "lednopb", "ledpb", "cleardoublepage",
    "newpage", "pagebreak", "nopagebreak", "noindent", "indent", "centering", "small",
    "footnotesize", "scriptsize", "tiny", "large", "Large", "LARGE", "huge", "normalsize",
    "it", "bf", "rm", "sc", "sl", "em", "selectfont", "relax", "xspace", "protect",
    "hfill", "vfill", "hfil", "smallskip", "medskip", "bigskip", "par", "Petit",
    "nobreak", "allowbreak", "unskip", "ignorespaces", "leavevmode", "strut",
    "hidenumbering", "maketitle", "policeFr", "policeGr", "policeLat", "policeAn",
    "policeAll", "policeIt", "policeEsp", "begin", "end", "phantom", "hphantom", "vphantom",
}


class Convertisseur:
    """Convertit des listes de nœuds en texte brut lisible."""

    def __init__(self, macros: dict, analyseur: Analyseur):
        self.macros = macros          # {nom: (arite, corps)}
        self.an = analyseur
        self._cache = {}

    def texte(self, noeuds, mode="texte") -> str:
        res = self._liste(noeuds, mode)
        return normaliser_blancs(res)

    def _liste(self, noeuds, mode):
        return "".join(self._noeud(n, mode) for n in noeuds)

    def _arg(self, nd, k, mode="texte"):
        if k < len(nd.args):
            return self._liste(nd.args[k], mode)
        return ""

    def _noeud(self, nd: Noeud, mode: str) -> str:
        if nd.type == "texte":
            return convertir_ligatures(nd.texte)
        if nd.type == "nl":
            return " "
        if nd.type == "par":
            return "\n\n"
        if nd.type == "saut":
            return "\n"
        if nd.type == "groupe":
            return self._liste(nd.enfants, mode)
        if nd.type == "math":
            return self._math(nd.enfants)
        if nd.type == "cmd":
            return self._cmd(nd, mode)
        return ""

    def _math(self, noeuds):
        res = []
        i = 0
        while i < len(noeuds):
            n = noeuds[i]
            if n.type == "texte":
                s = n.texte
                j = 0
                while j < len(s):
                    ch = s[j]
                    if ch in "^_":
                        # argument : caractère suivant ou nœud suivant
                        if j + 1 < len(s):
                            arg = s[j + 1]
                            j += 2
                        else:
                            arg = ""
                            if i + 1 < len(noeuds):
                                i += 1
                                arg = self._math([noeuds[i]])
                            j += 1
                        res.append(exposant(arg) if ch == "^" else indice(arg))
                        continue
                    res.append(ch)
                    j += 1
            elif n.type == "cmd":
                if n.nom in SYMBOLES_MATH:
                    res.append(SYMBOLES_MATH[n.nom])
                elif n.nom == "xrightarrow":
                    res.append("→")
                elif n.nom == "overset":
                    res.append(self._math(n.args[1]) + exposant(self._math(n.args[0])))
                elif n.nom == "underset":
                    haut = self._math(n.args[1])
                    bas = self._math(n.args[0])
                    if bas.strip() in ("·", "."):
                        res.append("".join(ch + "\u0323" for ch in haut))
                    else:
                        res.append(haut + indice(bas))
                elif n.nom == "breve":
                    res.append(self._math(n.args[0]) + "\u0306")
                elif n.nom in ("widearc", "text", "mbox", "mathrm", "mathit", "sout"):
                    res.append(self._math(n.args[0]) if n.args else "")
                else:
                    res.append(self._cmd(n, "texte"))
            elif n.type == "groupe":
                res.append(self._math(n.enfants))
            else:
                res.append(self._noeud(n, "texte"))
            i += 1
        return "".join(res)

    def _cmd(self, nd: Noeud, mode: str) -> str:
        nom = nd.nom
        # symboles de contrôle
        if len(nom) == 1 and not nom.isalpha():
            if nom in ACCENTS_COMB and nd.args:
                base = self._arg(nd, 0)
                return (base[:1] + ACCENTS_COMB[nom] + base[1:]) if base else ""
            return {"&": "&", "%": "%", "_": "_", "{": "{", "}": "}", " ": " ", ",": " ",
                    "-": "", "/": "", "$": "$", "#": "#", ";": " ", ":": " ", "!": "",
                    "\n": " "}.get(nom, "")
        if nom in ACCENTS_COMB and len(nom) == 1 and nd.args:
            base = self._arg(nd, 0)
            return (base[:1] + ACCENTS_COMB[nom] + base[1:]) if base else ""
        # macros de l'auteur à traitement particulier
        if nom == "marqueur":
            return exposant(self._arg(nd, 0))
        if nom in ("expo", "textsuperscript"):
            return exposant(self._arg(nd, 0))
        if nom == "textsubscript":
            return indice(self._arg(nd, 0))
        if nom == "nieme":
            return self._arg(nd, 0) + "ᵉ"
        if nom == "douteux":
            return "".join(ch + "\u0323" if not ch.isspace() else ch for ch in self._arg(nd, 0))
        if nom == "lettreBreve":
            return self._arg(nd, 0) + "\u0306"
        if nom == "synizese":
            return self._arg(nd, 0)
        if nom == "inRas":
            a, b = self._arg(nd, 0).strip(), self._arg(nd, 1).strip()
            return f"⟦{a}⟧" + (exposant(b) if b else "")
        if nom == "auDessus":
            a, b = self._arg(nd, 0), self._arg(nd, 1).strip()
            return a + (exposant(b) if b else "")
        if nom == "overset":
            return self._arg(nd, 1) + exposant(self._arg(nd, 0))
        if nom == "citComm":
            corps = normaliser_blancs(self._arg(nd, 0))
            lignes = [l.strip() for l in corps.split("\n")]
            return "\n" + "\n".join("> " + l for l in lignes if l) + "\n"
        if nom == "eff":
            return "⟨à revoir : " + self._arg(nd, 0) + "⟩"
        if nom == "ligneApp":
            return " ‖ " + self._arg(nd, 0).strip() + " "
        if nom in ("espApp", "espTest"):
            return " | "
        if nom == "cat":
            return "^"
        if nom == "fin":
            return " "
        if nom == "alinea":
            return " "
        if nom == "cesure":
            return " […] "
        if nom == "href":
            return self._arg(nd, 1)
        if nom == "url":
            return self._arg(nd, 0)
        if nom == "texorpdfstring":
            return self._arg(nd, 0)
        if nom == "xrightarrow":
            return "→"
        if nom in ("textcolor",):
            return self._arg(nd, 1)
        if nom in ("rotatebox", "scalebox", "raisebox"):
            return self._arg(nd, 1)
        if nom == "resizebox":
            return self._arg(nd, 2)
        if nom == "parbox":
            return self._arg(nd, 1)
        if nom == "sout":
            return "⟦" + self._arg(nd, 0) + "⟧"
        if nom in ("linebreak", "newline"):
            return "\n"
        if nom in ("Afootnote", "Bfootnote", "Cfootnote", "footnote", "ledleftnote", "ledrightnote"):
            return ""
        if nom == "edtext":
            return self._arg(nd, 0)
        if nom in SYMBOLES_TEXTE:
            return SYMBOLES_TEXTE[nom]
        if nom in SYMBOLES_MATH:
            return SYMBOLES_MATH[nom]
        if nom in TRANSPARENTES_1:
            return "".join(self._liste(a, mode) for a in nd.args)
        if nom in IGNOREES:
            return ""
        # macros du préambule : expansion générique
        if nom in self.macros:
            ar, corps = self.macros[nom]
            if ar == 0:
                return self._expansion0(nom, corps)
            # macro à arguments : transparente si le corps reprend #1 sans mise en page lourde
            return " ".join(self._liste(a, mode) for a in nd.args)
        # inconnue : on conserve le contenu des arguments
        return "".join(self._liste(a, mode) for a in nd.args)

    def _expansion0(self, nom, corps):
        if nom in self._cache:
            return self._cache[nom]
        self._cache[nom] = ""  # garde contre la récursion
        noeuds = self.an.analyser(corps)
        res = self._liste(noeuds, "texte")
        self._cache[nom] = res
        return res


def convertir_ligatures(s: str) -> str:
    """Ligatures typographiques TeX (---, --, ``, '') et espace insécable."""
    s = s.replace("---", "—").replace("--", "–")
    s = s.replace("``", "“").replace("''", "”")
    s = s.replace("`", "‘")
    s = s.replace("~", " ")
    return s


def normaliser_blancs(s: str) -> str:
    s = s.replace("\u00a0", " ")
    lignes = []
    for l in s.split("\n"):
        l = re.sub(r"[ \t]+", " ", l).strip()
        lignes.append(l)
    s = "\n".join(lignes)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


# ---------------------------------------------------------------------------
# 4. Normalisation du grec (comparaisons)
# ---------------------------------------------------------------------------

def grec_squelette(s: str) -> str:
    """Lettres grecques minuscules sans diacritiques, sigma unifié, sans espaces."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("ς", "σ").replace("ϲ", "σ")
    return "".join(ch for ch in s if "\u03b1" <= ch <= "\u03c9")


def grec_mots(s: str) -> list:
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("ς", "σ")
    return [m for m in re.findall(r"[\u03b1-\u03c9]+", s)]


def est_grec(s: str) -> bool:
    lettres = [ch for ch in s if ch.isalpha()]
    if not lettres:
        return False
    g = sum(1 for ch in lettres if "\u0370" <= ch <= "\u03ff" or "\u1f00" <= ch <= "\u1fff")
    return g / len(lettres) > 0.5


def plage_vers(s: str):
    """'13-8' -> (13, 18) ; '637-40' -> (637, 640) ; '1210-1216' -> (1210, 1216) ;
    '101-29' -> (101, 129) ; '18-9' -> (18, 19). Retourne (None, None) si illisible."""
    if s is None:
        return None, None
    t = s.strip()
    t = re.sub(r"^(?:post|ante|ad)?\s*(?:vv?\.)?\s*", "", t)
    m = re.match(r"^(\d+)\s*[a-z]?\s*(?:[-–]\s*(\d+)\s*[a-z]?)?", t)
    if not m:
        return None, None
    a = int(m.group(1))
    if not m.group(2):
        return a, a
    b_txt = m.group(2)
    b = int(b_txt)
    if b < a:
        # notation abrégée : on complète avec les chiffres de tête de a
        sa = str(a)
        b = int(sa[: len(sa) - len(b_txt)] + b_txt)
        if b < a:
            b = int(str(int(sa[: len(sa) - len(b_txt)] or "0") + 1) + b_txt)
    return a, b
