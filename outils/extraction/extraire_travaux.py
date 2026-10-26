#!/usr/bin/env python3
"""Extraction structurée des travaux antérieurs de l'auteur (édition « Harmattan 2023 »).

Parse les deux fichiers LaTeX les plus récents du corps de l'édition :
  latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex
  latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex
(texte grec en `Leftside`, traduction en `Rightside`, environnements `groupe`)
et produit dans edition/donnees/travaux_anterieurs/ :
  thesmo.json        extraction complète, groupe par groupe (grec + français)
  texte_grec.tsv     vers -> texte grec de l'auteur
  traduction.tsv     vers -> traduction française
  apparat.tsv        apparat critique découpé par vers
  commentaires.tsv   commentaires (id, plage, lemme, longueur, premier vers…)
  testimonia.tsv     testimonia (côtés gauche et droit, actifs et désactivés)
  anomalies.tsv      rapport de vérification (numérotation, alignement, notes…)

Usage :
  python3 outils/extraction/extraire_travaux.py [--depot CHEMIN] [--sortie DOSSIER]

La vérification de la numérotation utilise, si présent, le texte de Hall & Geldart
(Perseus, .sources/corpus/canonical-greekLit/…/tlg0019.tlg008.perseus-grc2.xml) :
seuls les numéros de vers correspondants sont reportés, jamais le texte.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import difflib
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyse_latex import (Analyseur, Convertisseur, Noeud, Source,  # noqa: E402
                           est_grec, grec_mots, grec_squelette, lire_macros_preambule,
                           normaliser_blancs, plage_vers)

FICHIERS_2023 = [
    "latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex",
    "latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex",
]
PERSEUS = (".sources/corpus/canonical-greekLit/data/tlg0019/tlg008/"
           "tlg0019.tlg008.perseus-grc2.xml")

# macros de « type de vers » (grec) et leurs équivalents français
MACROS_VERS = [
    "trimIamb", "trimIambCat", "tetramIamb", "tetramIambCat", "tetramTroch", "tetramAnap",
    "dimAnap", "anap", "diDoch", "chantAgath", "prose", "chantChoeur", "paratragiques",
]
MACROS_VERS_FR = [m + "Fr" for m in MACROS_VERS]
TOUTES_MACROS_VERS = set(MACROS_VERS) | set(MACROS_VERS_FR)
LYRIQUES = {"chantAgath", "chantChoeur", "paratragiques", "dimAnap", "anap", "diDoch", "prose"}

# commandes d'annotation (capturées, hors texte de la ligne)
ANNOTATIONS = {"apparat": 2, "testimonia": 2, "commentaire": 3, "debutNote": 1, "note": 2}
# commandes de mise en forme pouvant contenir de la structure (on les parcourt)
CONTENEURS = {"Automatique", "francais", "italique", "textbf", "small", "grec", "latin",
              "renverse", "textit", "emph"}


# ---------------------------------------------------------------------------
# Structures intermédiaires
# ---------------------------------------------------------------------------

@dataclass
class LigneBrute:
    noeuds: list = field(default_factory=list)       # nœuds contribuant au texte
    annotations: list = field(default_factory=list)  # (type, Noeud)
    lignes_expl: list = field(default_factory=list)  # valeurs de \ligne{n}
    passe: bool = False                              # \passeLigne
    decalage: str | None = None                      # \decalage{…} (antilabè)
    retrait: bool = False                            # \espace{…} en tête (français)
    type_vers: str | None = None
    metre: str | None = None
    decoupe: str | None = None
    strophe: str | None = None
    personnage: str | None = None
    rejet: bool = False                              # \fin (rejet typographique)
    fin_par: str = "groupe"                          # 'saut' (\\), 'nl' (fin de ligne source), 'groupe'
    debut: int | None = None                         # position (texte actif) du premier nœud de texte
    fin: int | None = None

    def a_du_texte(self) -> bool:
        return bool(self.noeuds)


class Parcours:
    """Découpe le contenu d'un groupe en lignes et rattache les annotations."""

    def __init__(self, conv: Convertisseur, src: Source, groupe_personnage: str | None):
        self.conv = conv
        self.src = src
        self.lignes: list[LigneBrute] = []      # lignes terminées (avec ou sans texte)
        self.courante = LigneBrute()
        self.personnage = groupe_personnage
        self.personnages = []
        self.en_tetes = []
        self.metre_en_attente = None
        self.inconnues = Counter()
        self.lignes_milieu = []

    # -- gestion des lignes ---------------------------------------------------
    def terminer(self, motif: str):
        self.courante.fin_par = motif
        self.lignes.append(self.courante)
        self.courante = LigneBrute()

    def derniere_avec_texte(self):
        for l in reversed(self.lignes):
            if l.a_du_texte():
                return l
        return None

    def annoter(self, typ, nd):
        cible = self.courante
        if not self.courante.a_du_texte():
            prec = self.derniere_avec_texte()
            if prec is not None:
                cible = prec
        cible.annotations.append((typ, nd))

    def ajouter_texte(self, nd, type_vers):
        l = self.courante
        if not l.noeuds:
            l.type_vers = type_vers
            l.personnage = self.personnage
            l.debut = nd.debut
            if self.metre_en_attente is not None and l.metre is None:
                l.metre = self.metre_en_attente
            self.metre_en_attente = None
        l.noeuds.append(nd)
        l.fin = nd.fin

    # -- parcours ---------------------------------------------------------------
    def parcourir(self, noeuds, type_vers=None):
        for nd in noeuds:
            t = nd.type
            if t == "saut":
                self.terminer("saut")
            elif t in ("nl", "par"):
                if self.courante.a_du_texte():
                    self.terminer("nl")
            elif t == "texte":
                if nd.texte.strip():
                    self.ajouter_texte(nd, type_vers)
                elif self.courante.a_du_texte():
                    self.courante.noeuds.append(nd)
            elif t == "math":
                self.ajouter_texte(nd, type_vers)
            elif t == "groupe":
                self.parcourir(nd.enfants, type_vers)
            elif t == "cmd":
                self.commande(nd, type_vers)

    def _arg_texte(self, nd, k=0):
        return self.conv.texte(nd.args[k]) if k < len(nd.args) else ""

    def commande(self, nd: Noeud, type_vers):
        nom = nd.nom
        if nom in TOUTES_MACROS_VERS:
            if nd.args:
                self.parcourir(nd.args[0], nom)
            return
        if nom in ANNOTATIONS:
            self.annoter(nom, nd)
            return
        if nom in ("personnageGrec", "personnageFr"):
            reste = []
            for x in (nd.args[0] if nd.args else []):
                if x.type == "cmd" and x.nom in ("strophe", "Strophe"):
                    self.courante.strophe = self.conv.texte(x.args[0]) if x.args else ""
                else:
                    reste.append(x)
            p = self.conv.texte(reste)
            if not p:
                return
            self.personnage = p
            self.personnages.append(p)
            if not self.courante.a_du_texte():
                self.courante.personnage = p
            return
        if nom in ("enTeteG", "enTeteD"):
            self.en_tetes.append({"cote": "G" if nom == "enTeteG" else "D",
                                  "texte": self._arg_texte(nd),
                                  "latex": self.src.actif[nd.debut:nd.fin]})
            return
        if nom == "typeVers":
            m = self._arg_texte(nd)
            if self.courante.a_du_texte():
                self.metre_en_attente = m
            else:
                self.courante.metre = m
            return
        if nom == "ligne":
            try:
                n = int(self._arg_texte(nd))
            except ValueError:
                return
            if self.courante.a_du_texte():
                # \ligne{n} après du texte : l'auteur commence un nouveau vers (\\ oublié)
                self.lignes_milieu.append((nd.debut, n))
                self.terminer("ligne_milieu")
            self.courante.lignes_expl.append(n)
            return
        if nom in ("passeLigne", "skipnumbering"):
            self.courante.passe = True
            return
        if nom in ("decalage", "decalageN"):
            self.courante.decalage = self._arg_texte(nd)
            return
        if nom in ("espace", "hspace"):
            if not self.courante.a_du_texte():
                self.courante.retrait = True
            elif self.courante.noeuds:
                self.courante.noeuds.append(Noeud("texte", nd.debut, nd.fin, texte=" "))
            return
        if nom == "decoupeVers":
            self.courante.decoupe = self._arg_texte(nd)
            return
        if nom in ("strophe", "Strophe"):
            self.courante.strophe = self._arg_texte(nd)
            return
        if nom == "fin":
            self.courante.rejet = True
            if self.courante.noeuds:
                self.courante.noeuds.append(Noeud("texte", nd.debut, nd.fin, texte=" "))
            return
        if nom in ("lednopb", "ledpb", "cleardoublepage", "newpage", "pagebreak", "label",
                   "vspace", "noindent", "relax", "Taille", "TaillePt", "par", "centering"):
            return
        if nom in ("small", "footnotesize", "large", "normalsize", "Large", "scriptsize"):
            return
        if nom in CONTENEURS and nd.args and self._contient_structure(nd):
            for a in nd.args:
                self.parcourir(a, type_vers)
            return
        if nom in ("setline",):
            try:
                self.courante.lignes_expl.append(int(self._arg_texte(nd)))
            except ValueError:
                pass
            return
        # tout le reste contribue au texte (mise en forme, macros textuelles)
        self.ajouter_texte(nd, type_vers)

    def _contient_structure(self, nd) -> bool:
        pile = [x for a in nd.args for x in a]
        while pile:
            x = pile.pop()
            if x.type == "saut":
                return True
            if x.type == "cmd" and (x.nom in ANNOTATIONS or x.nom in TOUTES_MACROS_VERS
                                    or x.nom in ("ligne", "passeLigne", "personnageGrec",
                                                 "personnageFr", "typeVers", "decalage")):
                return True
            if x.type == "cmd":
                pile.extend(y for a in x.args for y in a)
            if x.type in ("groupe", "math"):
                pile.extend(x.enfants)
        return False

    def finir(self):
        # contenu restant après le dernier \\ : ligne finale (avec texte) ou ligne vide
        self.terminer("groupe")


# ---------------------------------------------------------------------------
# Extraction d'un fichier
# ---------------------------------------------------------------------------

RE_GROUPE_DEBUT = re.compile(r"\\begin\{groupe\}")
RE_NUM_VERS = re.compile(r"\s*\d{1,4}[a-z]?(?:\s*[-–]\s*\d{1,4}[a-z]?)?\s*")
RE_GROUPE_FIN = re.compile(r"\\end\{groupe\}")
RE_ETIQ = re.compile(r"^\s*%{2,}\s*(v\.?\s*.*?)\s*$")


class Extracteur:
    def __init__(self, chemin_abs: str, nom: str):
        self.nom = nom
        self.src = Source(chemin_abs)
        t = self.src.actif
        i = t.find("\\begin{document}")
        self.preambule = self.src.orig[: self.src.orig_de_actif(i)] if i >= 0 else ""
        self.macros = lire_macros_preambule(self.preambule)
        arites = {k: v[0] for k, v in self.macros.items()}
        self.an = Analyseur(arites)
        self.conv = Convertisseur(self.macros, self.an)

    # -- utilitaires --------------------------------------------------------
    def latex(self, nd_ou_liste) -> str:
        if isinstance(nd_ou_liste, list):
            if not nd_ou_liste:
                return ""
            return self.src.actif[nd_ou_liste[0].debut: nd_ou_liste[-1].fin]
        return self.src.actif[nd_ou_liste.debut: nd_ou_liste.fin]

    def texte(self, noeuds) -> str:
        return self.conv.texte(noeuds)

    def ligne_src(self, pos_actif) -> int:
        return self.src.ligne_actif(pos_actif)

    def cotes(self):
        t = self.src.actif
        res = {}
        for cote, env in (("gauche", "Leftside"), ("droite", "Rightside")):
            a = t.find("\\begin{%s}" % env)
            b = t.find("\\end{%s}" % env)
            if a >= 0 and b > a:
                res[cote] = (a, b)
        return res

    def etiquette(self, pos_actif_groupe: int) -> str | None:
        """Commentaire « %% v. … » qui précède le groupe dans le texte d'origine."""
        po = self.src.orig_de_actif(pos_actif_groupe)
        n = self.src.ligne_orig(po)          # ligne du \begin{groupe}
        lignes = self.src.orig.split("\n") if not hasattr(self, "_lignes") else self._lignes
        self._lignes = lignes
        k = n - 2
        while k >= 0 and k >= n - 6:
            l = lignes[k]
            if not l.strip().startswith("%"):
                break
            m = RE_ETIQ.match(l)
            if m:
                return m.group(1).strip()
            k -= 1
        return None

    def groupes(self, cote: str):
        a, b = self.cotes()[cote]
        t = self.src.actif
        pos = a
        res = []
        while True:
            m = RE_GROUPE_DEBUT.search(t, pos, b)
            if not m:
                break
            f = RE_GROUPE_FIN.search(t, m.end(), b)
            if not f:
                break
            res.append((m.start(), m.end(), f.start(), f.end()))
            pos = f.end()
        return res

    # -- annotations ----------------------------------------------------------
    def comm_desactives(self, debut_actif: int, fin_actif: int, convertir: bool = False) -> list:
        """Parties commentées (%) comprises dans un intervalle du texte actif (une macro).

        L'intervalle s'arrête juste après le dernier caractère actif de la macro (son accolade
        fermante) : un commentaire placé après elle sur la même ligne (`}%\\testimonia{…}`)
        n'en fait pas partie. Avec `convertir`, le LaTeX commenté est aussi converti en texte
        (`texte`), le source étant gardé dans `latex` (apparat, testimonia)."""
        a = self.src.orig_de_actif(debut_actif)
        b = self.src.orig_de_actif(max(debut_actif, fin_actif - 1)) + 1
        res = []
        for c in self.src.commentaires_entre(a, b):
            txt = c.texte.strip()
            if txt and not re.fullmatch(r"[%\s]*", txt):
                d = {"ligne": self.src.ligne_orig(c.debut), "texte": c.texte}
                if convertir:
                    d["latex"] = c.texte
                    try:
                        d["texte"] = normaliser_blancs(self.conv.texte(self.an.analyser(c.texte)))
                    except Exception:  # accolades déséquilibrées dans un fragment commenté
                        d["texte"] = normaliser_blancs(re.sub(r"\\[A-Za-z]+|[{}]", " ", c.texte))
                res.append(d)
        return res

    def annotation(self, typ, nd, ancre):
        args = nd.args
        d = {"type": typ, "ligne_source": self.ligne_src(nd.debut), "ancre": ancre}
        if typ == "apparat":
            d["plage"] = self.texte(args[0]) if args else ""
            d["latex"] = self.latex(args[1]) if len(args) > 1 else ""
            d["texte"] = self.texte(args[1]) if len(args) > 1 else ""
            d["segments"] = self.segments_apparat(d["plage"], args[1] if len(args) > 1 else [])
            # entrées commentées à l'intérieur d'une macro active (« \apparat{417}{%μορμολύκεια
            # R : … \espApp » : l'entrée est désactivée, la macro reste)
            d["desactive_interne"] = self.comm_desactives(nd.debut, nd.fin, convertir=True)
        elif typ == "testimonia":
            d["plage"] = self.texte(args[0]) if args else ""
            d["latex"] = self.latex(args[1]) if len(args) > 1 else ""
            d["texte"] = self.texte(args[1]) if len(args) > 1 else ""
            d["desactive_interne"] = self.comm_desactives(nd.debut, nd.fin, convertir=True)
        elif typ == "commentaire":
            d["plage"] = self.texte(args[0]) if args else ""
            d["lemme_latex"] = self.latex(args[1]) if len(args) > 1 else ""
            d["lemme"] = self.texte(args[1]) if len(args) > 1 else ""
            d["latex"] = self.latex(args[2]) if len(args) > 2 else ""
            d["texte"] = self.texte(args[2]) if len(args) > 2 else ""
            d["appels"] = self.appels(args[2]) if len(args) > 2 else []
            d["desactive_interne"] = self.comm_desactives(nd.debut, nd.fin)
        elif typ == "debutNote":
            d["plage"] = self.texte(args[0]) if args else ""
        elif typ == "note":
            d["numero"] = self.texte(args[0]) if args else ""
            d["latex"] = self.latex(args[1]) if len(args) > 1 else ""
            d["texte"] = self.texte(args[1]) if len(args) > 1 else ""
            d["appels"] = self.appels(args[1]) if len(args) > 1 else []
            d["desactive_interne"] = self.comm_desactives(nd.debut, nd.fin)
        return d

    def appels(self, noeuds) -> list:
        res = []
        pile = list(noeuds)
        while pile:
            x = pile.pop(0)
            if x.type == "cmd" and x.nom == "marqueur":
                res.append(self.texte(x.args[0]) if x.args else "")
                continue
            if x.type == "cmd":
                pile[0:0] = [y for a in x.args for y in a]
            elif x.type in ("groupe", "math"):
                pile[0:0] = x.enfants
        return res

    # -- apparat ----------------------------------------------------------------
    def segments_apparat(self, plage: str, noeuds: list) -> list:
        """Découpe un \\apparat en segments par vers (\\ligneApp) puis en entrées (\\espApp)."""
        segs = []
        courant = {"vers": plage, "noeuds": []}
        for nd in noeuds:
            if nd.type == "cmd" and nd.nom == "ligneApp":
                segs.append(courant)
                courant = {"vers": self.texte(nd.args[0]) if nd.args else "?", "noeuds": []}
            elif nd.type == "cmd" and nd.nom == "textbf" and nd.args and \
                    RE_NUM_VERS.fullmatch(self.texte(nd.args[0])):
                # numéro de vers saisi à la main en gras au lieu de \ligneApp (vv. 135, 169,
                # 179, 581, 658) : même valeur de séparateur
                segs.append(courant)
                courant = {"vers": self.texte(nd.args[0]).strip(), "noeuds": [], "manuel": True}
            else:
                courant["noeuds"].append(nd)
        segs.append(courant)
        res = []
        for s in segs:
            if not s["noeuds"] or not self.texte(s["noeuds"]).strip():
                continue
            entrees = []
            cour = []
            for nd in s["noeuds"]:
                if nd.type == "cmd" and nd.nom == "espApp":
                    entrees.append(cour)
                    cour = []
                else:
                    cour.append(nd)
            entrees.append(cour)
            ents = []
            for e in entrees:
                if not e or not self.texte(e).strip():
                    continue
                ents.append(self.entree_apparat(e))
            d1, d2 = plage_vers(s["vers"])
            seg = {"vers": s["vers"], "debut": d1, "fin": d2,
                   "latex": self.latex(s["noeuds"]).strip(),
                   "texte": self.texte(s["noeuds"]), "entrees": ents}
            if s.get("manuel"):
                seg["separateur_manuel"] = True
            res.append(seg)
        return res

    def entree_apparat(self, noeuds: list) -> dict:
        """Une entrée : leçons séparées par ' : ' ; la leçon retenue est en \\lecon{}."""
        lecons = []
        cour = []

        def pousser():
            if cour and self.texte(cour).strip():
                lecons.append(self.lecon(cour))

        # séparateur « : » ; aussi collé au sigle ou au numéro qui précède (« R~: », « R: »,
        # « ε 1271: »), pourvu qu'une espace le suive
        SEP = r"[\s~ ]+:\s|[\s~ ]+:$|^:\s|(?<=[^\s:])~?:\s"
        for nd in noeuds:
            if nd.type == "texte" and ":" in nd.texte:
                morceaux = re.split("(%s)" % SEP, nd.texte)
                debut = nd.debut
                for k, m in enumerate(morceaux):
                    if k % 2 == 1:          # séparateur (groupe capturant de re.split)
                        pousser()
                        cour = []
                    elif m:
                        cour.append(Noeud("texte", debut, debut + len(m), texte=m))
                    debut += len(m)
            else:
                cour.append(nd)
        pousser()
        return {"latex": self.latex(noeuds).strip(), "texte": self.texte(noeuds), "lecons": lecons}

    def lecon(self, noeuds: list) -> dict:
        retenue = None
        apres = []
        avant = []
        vu = False
        for nd in noeuds:
            if nd.type == "cmd" and nd.nom == "lecon":
                t = self.texte(nd.args[0]) if nd.args else ""
                retenue = t if retenue is None else (retenue + " " + t)
                vu = True
                continue
            if vu and nd.type == "texte" and not nd.texte.strip(" ,;") and retenue is not None:
                continue
            (apres if vu else avant).append(nd)
        txt = self.texte(noeuds)
        if retenue is not None:
            lec = retenue
            attrib = self.texte(apres)
            prefixe = self.texte(avant)
            if prefixe:
                lec = (prefixe + " " + lec).strip()
        else:
            lec, attrib = separer_attribution(txt)
        return {"texte": txt, "lecon": lec, "attribution": attrib,
                "retenue": retenue is not None}


RE_SIGLE_R = re.compile(r"R(?![A-Za-zΑ-Ωα-ωἀ-ῼ])")          # R, R², Rᵖᶜ, Rᵃᶜ(… — pas Rau, Rogers
RE_SIGLE_SIGMA = re.compile(r"\(?Σ(?![α-ωάέήίόύώϊϋΐΰἀ-ῷ])")  # Σ, Σ¹, Σᵀ — pas Σκύθης
RE_SIGLE_LEX = re.compile(r"\(?[α-ωϊϋ]{1,2}")                  # Suid. ε 989, Hesych. (ο 649)
RE_NUM_PAR = re.compile(r"\(\d+(?:-\d+)?\)|\(bis\)")


def separer_attribution(txt: str):
    """Sépare « leçon témoins » : la leçon s'arrête au dernier mot grec avant les sigles et
    noms latins (heuristique). Ne comptent pas comme mots de la leçon : le sigle Σ (scholie),
    les lettres d'article de lexique suivies d'un numéro (Suid. ε 989), et tout ce qui suit le
    premier sigle de R (« στυγνὰς ὡσσε Rᵃᶜ(cf. στυγοῦσ᾽ ὥσπερ v. sq. ?) ») ; une mention de
    vers entre parenthèses qui suit le dernier mot grec reste dans la leçon (« (Μνη.) (71) et
    (Εὐρ.) (72-4) R »). Les mots descriptifs placés avant le sigle (om., bis, in mg., suppl.)
    vont avec l'attribution."""
    mots = txt.split()

    def mot_de_lecon(i):
        m = mots[i]
        if not est_grec(m) or RE_SIGLE_SIGMA.match(m):
            return False
        if RE_SIGLE_LEX.fullmatch(m) and i + 1 < len(mots) and re.match(r"\d", mots[i + 1]):
            return False
        return True

    borne = len(mots)
    for i, m in enumerate(mots):
        if RE_SIGLE_R.match(m) and any(mot_de_lecon(k) for k in range(i)):
            borne = i
            break
    dernier = -1
    for i in range(borne):
        if mot_de_lecon(i):
            dernier = i
    if dernier == -1:
        return "", txt
    while dernier + 1 < borne and RE_NUM_PAR.fullmatch(mots[dernier + 1]):
        dernier += 1
    return " ".join(mots[: dernier + 1]), " ".join(mots[dernier + 1:])


# ---------------------------------------------------------------------------
# Construction des groupes
# ---------------------------------------------------------------------------

def construire_cote(ex: Extracteur, cote: str, personnage_herite: str | None):
    groupes = []
    for (a, a2, b, b2) in ex.groupes(cote):
        etiq = ex.etiquette(a)
        noeuds = ex.an.analyser(ex.src.actif, a2, b)
        p = Parcours(ex.conv, ex.src, personnage_herite)
        p.parcourir(noeuds)
        p.finir()
        if p.personnages:
            personnage_herite = p.personnages[-1]
        # lignes : texte, annotations
        lignes = []
        vides = []          # lignes vides (pour l'émulation de la numérotation)
        sequence = []       # ordre des lignes de sortie (texte et vides)
        for lb in p.lignes:
            if lb.a_du_texte():
                lignes.append(lb)
                sequence.append(("texte", lb))
            else:
                # ligne vide : seule celle qui suit un \\ produit une ligne de sortie
                sequence.append(("vide", lb))
        # une ligne vide n'existe en sortie que si elle suit un \\ (ou en tête de groupe après \\)
        seq2 = []
        prec_motif = None
        for i, (k, lb) in enumerate(sequence):
            if k == "vide":
                # ligne vide de sortie : précédée d'un \\ (fin_par de la précédente == 'saut')
                if prec_motif == "saut" and (lb.fin_par in ("saut", "groupe")):
                    seq2.append(("vide", lb))
                prec_motif = lb.fin_par
                continue
            seq2.append((k, lb))
            prec_motif = lb.fin_par
        groupes.append({
            "debut_actif": a, "fin_actif": b2, "etiquette": etiq,
            "parcours": p, "lignes": lignes, "sequence": seq2,
            "personnage_herite": personnage_herite,
        })
    return groupes, personnage_herite


def emuler_numerotation(groupes_cote: list, depart: int = 0):
    """Émule le compteur de reledmac : chaque ligne de sortie incrémente le compteur,
    \\ligne{n} (= \\setline) le fixe, \\passeLigne (= \\skipnumbering) l'annule."""
    prec = depart
    for g in groupes_cote:
        for k, lb in g["sequence"]:
            if lb.lignes_expl:
                num = lb.lignes_expl[-1]
                if lb.passe and k == "texte":
                    num = num  # cas non rencontré : \ligne et \passeLigne sur la même ligne
            else:
                num = prec + 1
            compte = True
            if lb.passe:
                num = prec if not lb.lignes_expl else num
                compte = False
            lb.n_reledmac = num if compte else None
            lb.compte = compte
            lb.vide_comptee = (k == "vide" and compte)
            prec = num
    return prec


# ---------------------------------------------------------------------------
# Référence Hall & Geldart (Perseus) pour la vérification
# ---------------------------------------------------------------------------

def charger_hg(depot: str):
    chemin = os.path.join(depot, PERSEUS)
    if not os.path.exists(chemin):
        return None
    from lxml import etree
    NS = "{http://www.tei-c.org/ns/1.0}"
    arbre = etree.parse(chemin)
    res = []
    for l in arbre.iter(NS + "l"):
        n = l.get("n")
        if n is None:
            continue
        cp = etree.fromstring(etree.tostring(l))
        for nn in cp.iter(NS + "note"):
            nn.getparent().remove(nn)
        txt = re.sub(r"\s+", " ", " ".join(cp.itertext())).strip()
        m = re.match(r"^(\d+)([a-z]?)$", n)
        if not m or not txt:
            continue
        res.append({"n": n, "base": int(m.group(1)), "suffixe": m.group(2),
                    "sq": grec_squelette(txt)})
    return res


class ReferenceHG:
    def __init__(self, lignes):
        self.lignes = lignes
        self.par_base = defaultdict(list)
        for i, l in enumerate(lignes):
            self.par_base[l["base"]].append(i)

    def candidats(self, centre: int, rayon: int = 4):
        idx = []
        for b in range(centre - rayon, centre + rayon + 1):
            idx.extend(self.par_base.get(b, []))
        return sorted(set(idx))

    def meilleur(self, sq: str, centre: int, rayon: int = 4):
        """Meilleur appariement (ligne seule ou deux lignes consécutives)."""
        if not sq or centre is None or len(sq) < 4:
            return None
        best = None
        cands = self.candidats(centre, rayon)
        for i in cands:
            for k in (1, 2):
                if i + k - 1 >= len(self.lignes):
                    continue
                if k == 2 and self.lignes[i + 1]["base"] - self.lignes[i]["base"] > 1:
                    continue
                ref = "".join(self.lignes[j]["sq"] for j in range(i, i + k))
                sm = difflib.SequenceMatcher(None, sq, ref, autojunk=False)
                M = sum(b.size for b in sm.get_matching_blocks())
                cov_a = M / len(sq)
                cov_b = M / len(ref) if ref else 0
                score = cov_a + 0.6 * cov_b - (0.05 if k == 2 else 0) \
                    - 0.002 * abs(self.lignes[i]["base"] - centre)
                cand = {"n": self.lignes[i]["n"], "base": self.lignes[i]["base"], "k": k,
                        "n_fin": self.lignes[i + k - 1]["n"],
                        "cov_a": round(cov_a, 3), "cov_b": round(cov_b, 3),
                        "score": round(score, 3)}
                if best is None or cand["score"] > best["score"]:
                    best = cand
        return best


# ---------------------------------------------------------------------------
# Attribution des numéros de vers (grec)
# ---------------------------------------------------------------------------

def texte_ligne(ex: Extracteur, lb: LigneBrute) -> str:
    return ex.texte(lb.noeuds)


def latex_ligne(ex: Extracteur, lb: LigneBrute) -> str:
    return "".join(ex.src.actif[n.debut:n.fin] for n in lb.noeuds).strip()


RE_ETIQ_VERS = re.compile(r"v\.?\s*(\d+)([a-z])?(?![a-z])\s*(?:[-–]\s*(\d+)([a-z])?(?![a-z]))?")


def analyser_etiquette(etq):
    """« v. 22b-24 » -> (22, 'b', 24, '') ; « v. 434-5 » -> (434, '', 435, '')."""
    if not etq:
        return None
    m = RE_ETIQ_VERS.match(etq.strip())
    if not m:
        return None
    n1, p1 = int(m.group(1)), m.group(2) or ""
    if m.group(3):
        t2 = m.group(3)
        n2 = int(t2)
        if n2 < n1:
            sa = str(n1)
            n2 = int(sa[: len(sa) - len(t2)] + t2)
            if n2 < n1:
                n2 += 10 ** len(t2)
        p2 = m.group(4) or ""
    else:
        n2, p2 = n1, p1
    return (n1, p1, n2, p2)


def preuves_etiquettes(lignes):
    """Les commentaires « %% v. … » précédant les groupes : début (première ligne du premier
    groupe d'une série de groupes de même étiquette) et fin (dernière ligne du dernier)."""
    par_groupe = defaultdict(list)
    ordre = []
    for L in lignes:
        if L["ordre_groupe"] not in par_groupe:
            ordre.append(L["ordre_groupe"])
        par_groupe[L["ordre_groupe"]].append(L)
    series = []
    for g in ordre:
        etq = par_groupe[g][0]["etiquette"]
        if series and series[-1][0] == etq:
            series[-1][1].append(g)
        else:
            series.append((etq, [g]))
    for etq, gs in series:
        e = analyser_etiquette(etq)
        if not e:
            continue
        premiere = par_groupe[gs[0]][0]
        derniere = par_groupe[gs[-1]][-1]
        premiere["etq_debut"] = (e[0], e[1])
        if re.search(r"\d\s*[a-z]?\s*[-–]\s*\d", etq):      # étiquette à deux bornes
            derniere["etq_fin"] = (e[2], e[3])


def nombre_suffixe(base: int, chiffres: str) -> int:
    """Plus petit nombre >= base dont l'écriture se termine par `chiffres`."""
    k = len(chiffres)
    m = 10 ** k
    c = int(chiffres)
    n = base - (base % m) + c
    if n < base:
        n += m
    return n


def attribuer_vers_grec(lignes: list, anomalies: list, hg: ReferenceHG | None, supprimes: set):
    r"""Attribue à chaque ligne grecque son numéro de vers (« vers ») selon l'intention de
    l'auteur. Signaux, par ordre de priorité :
      1. étiquettes « %% v. … » des groupes et \decoupeVers (a, b… ; chiffres = fin du vers) ;
      2. \ligne{n} (numéro explicite) — sauf artefacts : répétition d'un numéro déjà
         attribué, saut alors que le texte est celui du vers attendu (numéro « consommé »
         par un vers supprimé qui suit, cf. vv. 23, 500), \ligne erroné sur une antilabè ;
      3. antilabè : \decalage + \ligne{n} identique, ou fragment du même vers selon HG ;
      4. incrément (les lignes vides que reledmac compte après un \\ final sont ignorées).
    Hall-Geldart (HG, Perseus) ne sert qu'à départager ces cas ; les écarts de numérotation
    entre l'auteur et HG sont signalés, non corrigés."""
    preuves_etiquettes(lignes)
    refrains = Counter(L["sq"] for L in lignes if 0 < len(L["sq"]) <= 20)
    for L in lignes:
        L["vers_HG"] = None
        L["HG"] = None
        L["numeros_consommes"] = []
        L["vers_fin"] = None
        L["continuation"] = False
        if hg is not None:
            centre = L["n_reledmac"] if L["n_reledmac"] is not None else None
            if centre is not None:
                b = hg.meilleur(L["sq"], centre)
                if b and b["cov_a"] >= 0.6:
                    L["HG"] = b
                    L["vers_HG"] = b["n"] if b["k"] == 1 else f'{b["n"]}-{b["n_fin"]}'

    def hg_base(L, strict=False):
        h = L["HG"]
        if not h or h["k"] != 1 or h["cov_a"] < 0.85:
            return None
        if strict and h["cov_b"] < 0.75:
            return None
        return h["base"]

    def hg_suffixe(L):
        h = L["HG"]
        if not h or h["k"] != 1 or h["cov_a"] < 0.85:
            return ""
        return re.sub(r"^\d+", "", h["n"])

    def decoupe(L):
        m = re.fullmatch(r"(\d*)([a-z]?)", (L["decoupe"] or "").strip())
        return (m.group(1), m.group(2)) if m else ("", "")

    compteur = 0
    prec_vers = 0
    ancre = -1           # indice de la dernière ligne au numéro sûr
    ancre_val = 0
    for i, L in enumerate(lignes):
        if not L["compte"]:
            L["vers"] = None
            L["methode"] = "hors numérotation (\\passeLigne)"
            continue
        expl = L["lignes_expl"][-1] if L["lignes_expl"] else None
        e_app = preuve_apparat(L)
        etq = L.get("etq_debut")
        chiffres, lettre = decoupe(L)
        attendu = compteur + 1
        # les vers supprimés par l'auteur n'ont pas de ligne : on saute leur numéro
        while attendu in supprimes and e_app != attendu and hg_base(L) != attendu:
            attendu += 1
        apres = None
        cont = False
        methode = ""
        hgs = hg_base(L, strict=True)
        ef = L.get("etq_fin")
        if hgs is None and L["HG"] and L["HG"]["cov_a"] >= 0.85 and len(L["sq"]) >= 20:
            hgs = L["HG"]["base"]      # ligne longue appariée à deux lignes HG
        if len(L["sq"]) < 20 and hgs == prec_vers + 1:
            hgs = None                 # ligne brève (exclamation, refrain) : l'étiquette prime
        # ---- 1. suite du vers précédent ?
        if etq and etq[1] and etq[1] != "a" and etq[0] == prec_vers and hgs != prec_vers + 1:
            cont, methode = True, "suite du vers précédent (étiquette « %s »)" % L["etiquette"]
        elif ef and not etq and ef[1] and ef[1] != "a" and ef[0] == prec_vers and hgs != prec_vers + 1:
            cont, methode = True, "suite du vers précédent (étiquette « %s »)" % L["etiquette"]
        elif lettre and lettre != "a" and not chiffres:
            cont, methode = True, "suite du vers précédent (\\decoupeVers{%s})" % lettre
        elif L["decalage"]:
            hb = hg_base(L)
            if expl is not None and expl == prec_vers:
                cont, methode = True, "antilabè"
            elif hb is not None and hb == prec_vers:
                cont, methode = True, "antilabè (fragment du même vers selon HG)"
            elif hb is not None and hb == prec_vers + 1:
                cont, methode = False, ""
            elif expl is not None and expl == prec_vers + 1 and expl in supprimes:
                cont, methode = True, "antilabè"
            elif expl is not None and expl != prec_vers + 1:
                cont, methode = True, "antilabè (présumée)"
        if cont:
            v = prec_vers
            if expl is not None and expl > prec_vers:
                nums = list(range(prec_vers + 1, expl + 1))
                if all(n in supprimes for n in nums):
                    apres = expl
                    L["numeros_consommes"] = nums
                    methode += " ; \\ligne{%d} réserve le n° du vers supprimé suivant" % expl
                else:
                    methode += " ; \\ligne{%d} erroné (ignoré)" % expl
        # ---- 2. vers découpé numéroté par ses derniers chiffres (« 4a »)
        elif chiffres and lettre:
            v = nombre_suffixe(max(prec_vers, 1), chiffres)
            if v > prec_vers + 2:
                v = attendu
            methode = "\\decoupeVers{%s%s}" % (chiffres, lettre)
        # ---- 3. numéro explicite
        elif expl is not None:
            if expl > compteur:
                if expl == attendu:
                    v = expl
                    methode = "\\ligne explicite"
                    if e_app is None:
                        # leçons de plusieurs vers dans la même ligne (ex. 1026 « ὁ Σκύθης » et
                        # 1027 « ἐφέστηκ᾽ ὀλοὸν ») : le numéro le plus élevé indique la couverture
                        pa_ = set(L.get("preuves_apparat") or [])
                        if expl in pa_ and any(x > expl for x in pa_):
                            e_app = max(pa_)
                    h = L["HG"]
                    couvre = bool(h and h["k"] == 2 and h["cov_a"] >= 0.75
                                  and h["base"] <= min(expl, e_app or expl)
                                  and int(re.match(r"\d+", h["n_fin"]).group()) >= max(expl, e_app or expl))
                    if e_app is not None and e_app != expl and couvre and e_app > expl:
                        L["vers_fin"] = e_app
                        methode = "\\ligne explicite (la ligne couvre aussi le v. %d selon l'apparat)" % e_app
                    elif e_app is not None and e_app != expl and abs(e_app - expl) <= 2 \
                            and e_app > prec_vers and hg_base(L) in (None, e_app) and not couvre:
                        v = e_app
                        methode = "corrigé : \\ligne{%d} contredit par l'apparat de l'auteur%s" % (
                            expl, " et HG" if hg_base(L) == e_app else "")
                else:  # saut
                    hb = hg_base(L, strict=True)
                    e_etq = etq[0] if etq else None
                    if e_etq == expl:
                        v = expl
                        methode = "\\ligne explicite (saut confirmé par l'étiquette)"
                    elif e_app == attendu or e_etq == attendu or \
                            (e_app is None and hb == attendu and L["type"] not in LYRIQUES):
                        v = attendu
                        nums = list(range(attendu + 1, expl + 1))
                        if all(n in supprimes for n in nums):
                            apres = expl
                            L["numeros_consommes"] = nums
                            methode = "\\ligne{%d} porté par le v. %d : n° %s réservé(s) au vers supprimé" % (
                                expl, attendu, ",".join(map(str, nums)))
                        else:
                            L["vers_fin"] = expl
                            methode = "\\ligne{%d} porté par une ligne commençant au v. %d (vv. %d-%d)" % (
                                expl, attendu, attendu, expl)
                    else:
                        v = expl
                        methode = "\\ligne explicite (saut de numérotation)"
            else:  # répétition d'un numéro déjà attribué
                hb = hg_base(L)
                hs = hg_suffixe(L)
                e_etq = etq[0] if etq else None
                prec_L = next((M for M in reversed(lignes[:i]) if M.get("vers") is not None), None)
                hp = hg_base(prec_L) if prec_L is not None else None
                if hs and hb == prec_vers:
                    v, cont = prec_vers, True
                    methode = "suite du vers précédent (\\ligne répété ; HG %s)" % L["HG"]["n"]
                elif prec_L is not None and preuve_apparat(prec_L) == prec_vers and e_app in (None, prec_vers):
                    v, cont = prec_vers, True
                    methode = "suite du vers précédent (\\ligne répété ; l'apparat confirme le vers précédent)"
                elif expl == prec_vers and prec_L is not None and hp in (None, expl) \
                        and not hg_suffixe(prec_L) and hb != prec_vers + 1 and e_app != prec_vers + 1 \
                        and prec_L["methode"].startswith("incrément"):
                    # \ligne{n} répète le numéro que la ligne précédente porte déjà (reledmac et
                    # intention de l'auteur) : seconde partie du même vers (ex. v. 994)
                    v, cont = prec_vers, True
                    methode = "suite du vers précédent (\\ligne{%d} répète le numéro de la ligne précédente)" % expl
                elif (hg_base(L, strict=True) == expl and not hs) or (e_etq == expl):
                    # le numéro explicite est juste : une ligne précédente partage un vers
                    k = prec_vers - expl + 1
                    cands = [j for j in range(ancre + 1, i)
                             if lignes[j]["vers"] is not None and not lignes[j]["continuation"]
                             and lignes[j]["methode"].startswith("incrément")]

                    def rang(j):
                        Lj, Lp = lignes[j], lignes[j - 1]
                        hbj, hpj = hg_base(Lj), hg_base(Lp)
                        if hg_suffixe(Lj) and hbj is not None and hpj is not None and hbj == hpj:
                            return 0
                        if hbj is not None and hpj is not None and hbj == hpj:
                            return 1
                        if refrains.get(Lj["sq"], 0) >= 2:
                            return 2
                        if hbj is not None and hpj is not None and hbj >= hpj + 1:
                            return 9
                        return 5 + 0.001 * (i - j)
                    choix = sorted(cands, key=rang)[:k] if len(cands) >= k else []
                    if choix and all(rang(j) < 9 for j in choix):
                        cur_v = lignes[ancre]["vers"] if ancre >= 0 else 0
                        cur_c = ancre_val
                        for j in range(ancre + 1, i):
                            Lj = lignes[j]
                            if Lj["vers"] is None:
                                continue
                            if j in choix:
                                Lj["vers"] = cur_v
                                Lj["continuation"] = True
                                Lj["methode"] = ("suite du vers précédent (déduit : \\ligne{%d} "
                                                 "plus loin)" % expl)
                            elif Lj["continuation"]:
                                Lj["vers"] = cur_v
                            else:
                                Lj["vers"] = cur_c + 1
                                if Lj["methode"].startswith("incrément"):
                                    Lj["methode"] = "incrément (recalé sur \\ligne{%d})" % expl
                            cur_v = Lj["vers"]
                            cur_c = max(cur_v, Lj["vers_fin"] or 0, max(Lj["numeros_consommes"] or [0]))
                        prec_vers = cur_v
                        compteur = cur_c
                        v = expl
                        methode = "\\ligne explicite (répétition résolue en amont)"
                        if compteur + 1 != expl:
                            methode += " [incohérence résiduelle]"
                    else:
                        v, cont = prec_vers, True
                        methode = "suite du vers précédent (\\ligne répété, non résolu)"
                elif hb == prec_vers + 1 or e_app == prec_vers + 1:
                    v = prec_vers + 1
                    methode = "corrigé : \\ligne{%d} répète un numéro ; %s indique %d" % (
                        expl, "apparat de l'auteur" if e_app == prec_vers + 1 else "HG", v)
                else:
                    v, cont = prec_vers, True
                    methode = "suite du vers précédent (\\ligne répété)"
        # ---- 4. incrément
        else:
            v = attendu
            methode = "incrément"
            # la ligne couvre-t-elle aussi le vers suivant (apparat, numéro explicite suivant) ?
            prochain = next((M["lignes_expl"][-1] for M in lignes[i + 1:i + 3]
                             if M["lignes_expl"] and M["compte"]), None)
            pp = [b for (a_, b) in (L.get("preuves_plage") or []) if a_ == v and b > v]
            if pp and prochain is not None and prochain >= max(pp) + 2:
                L["vers_fin"] = max(pp)
                methode = "incrément (la ligne couvre les vv. %d-%d selon l'apparat)" % (v, max(pp))
            elif e_app is not None and v < e_app <= v + 2 and prochain == e_app + 1:
                L["vers_fin"] = e_app
                methode = "incrément (la ligne couvre aussi le v. %d selon l'apparat)" % e_app
            if L["apres_vide"] and L["n_reledmac"] is not None and L["n_reledmac"] != v:
                methode = "incrément (ligne vide comptée par reledmac ignorée)"
            if etq and not etq[1] and etq[0] != v and prec_vers < etq[0] <= prec_vers + 2 \
                    and hg_base(L) in (None, etq[0]):
                v = etq[0]
                methode = "corrigé par l'étiquette « %s »" % L["etiquette"]
        # vers couvrant plusieurs numéros : \decoupeVers{chiffres}
        if chiffres and not lettre and not cont:
            vf = nombre_suffixe(v + 1, chiffres)
            if vf <= v + 3:
                L["vers_fin"] = vf
        # étiquette de fin de série : « v. 434-5 »
        if ef and not ef[1] and ef[0] in (v + 1, v + 2) and L["vers_fin"] is None \
                and (len(lignes) == i + 1 or lignes[i + 1].get("etq_debut", (0,))[0] > ef[0]):
            L["vers_fin"] = ef[0]
        L["vers"] = v
        L["methode"] = methode
        L["continuation"] = bool(cont)
        prec_vers = v
        compteur = max(v, L["vers_fin"] or 0, apres or 0)
        if (expl is not None and not cont) or (hg_base(L, strict=True) == v and not hg_suffixe(L)):
            ancre, ancre_val = i, compteur
    # vers couvrant plusieurs numéros (ligne suivie d'un saut et appariée à 2 lignes HG)
    numerotees = [L for L in lignes if L["vers"] is not None]
    for L, M in zip(numerotees, numerotees[1:]):
        if L["vers_fin"] is None and M["vers"] > L["vers"] + 1 and L["HG"] and L["HG"]["k"] == 2 \
                and L["HG"]["cov_a"] >= 0.85:
            fin = int(re.match(r"\d+", L["HG"]["n_fin"]).group())
            if L["vers"] < fin < M["vers"]:
                L["vers_fin"] = fin
    # parties (a, b, c…) pour les vers partagés entre plusieurs lignes
    par_vers = defaultdict(list)
    for L in lignes:
        if L["vers"] is not None:
            par_vers[L["vers"]].append(L)
    for v, Ls in par_vers.items():
        if len(Ls) == 1:
            Ls[0]["partie"] = ""
        else:
            for k, L in enumerate(Ls):
                L["partie"] = "abcdefghij"[k] if k < 10 else str(k)
    for L in lignes:
        L.setdefault("partie", "")
    # transpositions : deux lignes consécutives dont les appariements HG sont croisés.
    # L'ordre d'impression est inversé sans note d'apparat ; chaque ligne reçoit son numéro
    # usuel (seul cas : vv. 3-4, où l'apparat de l'auteur — « 3 τι R : τε » — et sa traduction
    # suivent l'ordre usuel) ; n_reledmac garde la position imprimée.
    for L, M in zip(numerotees, numerotees[1:]):
        a, b = L.get("HG"), M.get("HG")
        if a and b and a["k"] == 1 and b["k"] == 1 and min(a["cov_a"], b["cov_a"]) >= 0.85 \
                and min(a["cov_b"], b["cov_b"]) >= 0.8 and M["vers"] == L["vers"] + 1 \
                and a["base"] == M["vers"] and b["base"] == L["vers"] \
                and not L.get("transposee") and not M.get("transposee"):
            v1, v2 = L["vers"], M["vers"]
            L["vers"], M["vers"] = v2, v1
            L["transposee"] = M["transposee"] = True
            L["methode"] = ("transposition : ligne imprimée avant le v. %d ; numéro usuel (Hall-Geldart %s)"
                            % (v1, a["n"]))
            M["methode"] = ("transposition : ligne imprimée après le v. %d ; numéro usuel (Hall-Geldart %s)"
                            % (v2, b["n"]))
            anomalies.append({"code": "transposition", "gravite": "grave", "groupe": L["groupe"],
                              "vers": v1, "fichier": None, "ligne_source": L["ligne_source"],
                              "message": "vv. %d-%d : lignes imprimées dans l'ordre inverse de la "
                                         "tradition (Hall-Geldart %s puis %s), sans note d'apparat ; "
                                         "l'extraction leur rend leur numéro usuel — « %s » / « %s »" % (
                                             v1, v2, a["n"], b["n"],
                                             L["texte"][:40], M["texte"][:40])})


def aligner_traduction(fr: list, gr: list, ratio: float = 1.45):
    """Aligne des lignes françaises sur des lignes grecques (même groupe) par programmation
    dynamique sur les longueurs (fusions 2:1, 1:2, 3:1 ; ligne de didascalie rattachée au vers
    précédent). Retourne [(indices_fr, indices_gr), …]."""
    import math
    nF, nG = len(fr), len(gr)
    lf = [max(1, len(F["texte"])) for F in fr]
    lg = [max(1, len(L["texte"])) for L in gr]
    didasc = [bool(re.fullmatch(r"\s*\(.*\)\s*", F["texte"])) for F in fr]
    src = [F["ligne_source"] for F in fr]
    INF = float("inf")
    cout = [[INF] * (nG + 1) for _ in range(nF + 1)]
    arr = [[None] * (nG + 1) for _ in range(nF + 1)]
    cout[0][0] = 0.0
    pas = [(1, 1), (2, 1), (1, 2), (3, 1), (1, 3), (2, 2)]
    for i in range(nF + 1):
        for j in range(nG + 1):
            c0 = cout[i][j]
            if c0 == INF:
                continue
            for a, b in pas:
                if i + a > nF or j + b > nG:
                    continue
                f = sum(lf[i:i + a])
                g = sum(lg[j:j + b])
                c = abs(math.log((f + 8) / (g * ratio + 8))) + 0.45 * (a - 1) + 0.45 * (b - 1)
                if a >= 2:
                    c -= 0.25 * sum(1 for k in range(i, i + a - 1) if src[k] == src[k + 1])
                    c -= 0.4 * sum(1 for k in range(i + 1, i + a) if didasc[k])
                if c0 + c < cout[i + a][j + b]:
                    cout[i + a][j + b] = c0 + c
                    arr[i + a][j + b] = (a, b)
    if cout[nF][nG] == INF:
        return [(list(range(nF)), list(range(nG)))]
    res = []
    i, j = nF, nG
    while i > 0 or j > 0:
        a, b = arr[i][j]
        res.append((list(range(i - a, i)), list(range(j - b, j))))
        i, j = i - a, j - b
    return list(reversed(res))


def preuve_apparat(L):
    """Numéro de vers que l'apparat de l'auteur attribue à cette ligne (leçon retrouvée)."""
    pa = L.get("preuves_apparat") or []
    if not pa:
        return None
    c = Counter(pa).most_common()
    if len(c) > 1 and c[0][1] == c[1][1]:
        return None
    return c[0][0]


def vers_supprimes(apparats: list) -> set:
    """Vers dont l'apparat retient la suppression (« del. » en leçon retenue)."""
    res = set()
    for app in apparats:
        for seg in app["segments"]:
            if seg["debut"] is None or re.match(r"\s*(post|ante)", seg["vers"]):
                continue
            for e in seg["entrees"]:
                for lec in e["lecons"]:
                    if lec["retenue"] and re.fullmatch(r"\s*del\.?\s*", lec["lecon"] or ""):
                        res.update(range(seg["debut"], (seg["fin"] or seg["debut"]) + 1))
    return res


def mots_lemme(seg) -> list:
    """Mots grecs (>= 4 lettres) de la leçon retenue d'un segment d'apparat (ou de la
    première leçon à défaut) : sert à retrouver la ligne concernée."""
    mots = []
    for e in seg["entrees"]:
        for lec in e["lecons"]:
            if lec["retenue"] and lec["lecon"]:
                mots.extend(grec_mots(lec["lecon"]))
        if not mots and e["lecons"]:
            mots.extend(grec_mots(e["lecons"][0]["lecon"]))
    return [w for w in mots if len(w) >= 4]


def preuves_apparat(lignes_g: list, apparats: list):
    """Pour chaque segment d'apparat (vers m ou plage a-b), cherche la ligne contenant la leçon
    retenue parmi les lignes proches ; ajoute m comme preuve de numéro (ou la plage comme
    preuve de couverture)."""
    for app in apparats:
        for seg in app["segments"]:
            m, f = seg["debut"], seg["fin"]
            if m is None or f is None or f - m > 3:
                continue
            mots = mots_lemme(seg)
            if not mots:
                continue
            cands = [L for L in lignes_g if L["n_reledmac"] is not None
                     and abs(L["n_reledmac"] - m) <= 3]
            trouves = []
            for L in cands:
                lm = set(grec_mots(L["texte"]))
                if all(w in lm for w in mots[:3]):
                    trouves.append(L)
            if len(trouves) == 1:
                if f == m:
                    trouves[0].setdefault("preuves_apparat", []).append(m)
                else:
                    trouves[0].setdefault("preuves_plage", []).append((m, f))


def controle_apparat(lignes_g: list, apparats: list, anomalie):
    """Vérifie que la leçon de chaque segment d'apparat (vers m) se trouve bien dans une ligne
    numérotée m (ou couvrant m) ; sinon signale l'écart entre la numérotation de l'apparat et
    celle du texte."""
    par_vers = defaultdict(list)
    for L in lignes_g:
        if L["vers"] is None:
            continue
        for n in range(L["vers"], (L.get("vers_fin") or L["vers"]) + 1):
            par_vers[n].append(L)
    ok = ko = 0
    for app in apparats:
        for seg in app["segments"]:
            m, f = seg["debut"], seg["fin"]
            if m is None or f is None or f - m > 3:
                continue
            mots = mots_lemme(seg)
            if not mots:
                continue
            dans = [L for n in range(m, f + 1) for L in par_vers.get(n, [])
                    if all(w in set(grec_mots(L["texte"])) for w in mots[:3])]
            if dans:
                ok += 1
                continue
            voisins = [L for n in range(m - 3, f + 4) for L in par_vers.get(n, [])
                       if all(w in set(grec_mots(L["texte"])) for w in mots[:3])]
            if voisins:
                ko += 1
                L = voisins[0]
                anomalie("apparat_decale", "mineure",
                         "Apparat %s, segment « %s » (%s) : la leçon se trouve dans la ligne numérotée %s%s — « %s »"
                         % (app["id"], seg["vers"], " ".join(mots[:3]), L["vers"], L["partie"], L["texte"][:50]),
                         groupe=L["groupe"], vers=m, ligne=app["ligne_source"])
    return ok, ko


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------

def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 16), b""):
            h.update(bloc)
    return h.hexdigest()


def nom_a_masquer(ex: Extracteur):
    """Nom de l'auteur (lu dans \\author{} du préambule) et adresses électroniques, à ne
    jamais reproduire dans les sorties (dépôt public)."""
    motifs = []
    m = re.search(r"\\author\{(.*?)\\\\", ex.preambule, re.S)
    if m:
        nom = re.sub(r"\s+", " ", m.group(1)).strip()
        if nom:
            motifs.append(re.escape(nom))
            parties = nom.split()
            if len(parties) >= 2:
                motifs.append(re.escape(parties[-1]))   # patronyme seul
    motifs.append(r"[\w.+-]+@[\w-]+\.[\w.]+")
    return re.compile("|".join(motifs), re.I) if motifs else None


def masquer(obj, rx):
    if rx is None:
        return obj
    if isinstance(obj, str):
        return rx.sub("[auteur]", obj)
    if isinstance(obj, list):
        return [masquer(x, rx) for x in obj]
    if isinstance(obj, dict):
        return {k: masquer(v, rx) for k, v in obj.items()}
    return obj


def didascalies(txt: str) -> list:
    """Indications scéniques entre parenthèses dans la traduction (heuristique)."""
    res = []
    for m in re.finditer(r"\(([^()]{3,})\)", txt):
        s = m.group(1).strip()
        # majuscule initiale ; « ll » = coquille de l'auteur pour « Il » (v. 1222b) ; un seul
        # mot s'il est ponctué comme une phrase (« (Danse.) », « (Appelant.) »)
        if (s[:1].isupper() or s.startswith("ll ")) and not re.match(r"^(?:v\.|vv\.|cf\.|sic)", s) \
                and not s.isdigit() and (len(s.split()) >= 2 or s[-1:] in ".:!"):
            res.append(s)
    return res


def normaliser_personnage(p):
    if not p:
        return p
    # césure manuelle dans la marge (« Στεφανό-\\πωλις », nov 2022) : mot recollé
    p = re.sub(r"-\s*\n\s*", "", p)
    return normaliser_blancs(p).strip(" .:")


_HG_CACHE = {}


def extraire(depot: str, sortie: str | None, fichiers=None, ecrire=True):
    """Extraction complète ; `fichiers` : chemins relatifs au dépôt (par défaut les deux
    fichiers Harmattan 2023, traités à la suite). Retourne le dictionnaire résultat."""
    fichiers = fichiers or FICHIERS_2023
    anomalies = []

    def anomalie(code, gravite, message, groupe=None, vers=None, fichier=None, ligne=None):
        anomalies.append({"code": code, "gravite": gravite, "groupe": groupe,
                          "vers": vers, "fichier": fichier, "ligne_source": ligne,
                          "message": message})

    extracteurs = []
    for rel in fichiers:
        ex = Extracteur(os.path.join(depot, rel), os.path.basename(rel))
        extracteurs.append(ex)
    rx_nom = nom_a_masquer(extracteurs[0])

    if depot not in _HG_CACHE:
        hg_l = charger_hg(depot)
        _HG_CACHE[depot] = ReferenceHG(hg_l) if hg_l else None
    hg = _HG_CACHE[depot]

    # -- 1. groupes par côté, numérotation émulée (les deux fichiers à la suite) --------
    tous_g, tous_d = [], []
    prec_g = prec_d = 0
    pers_g = pers_d = None
    for ex in extracteurs:
        gg, pers_g = construire_cote(ex, "gauche", pers_g)
        dd, pers_d = construire_cote(ex, "droite", pers_d)
        # vérification : le second fichier commence-t-il par un \ligne ?
        if tous_g:
            prem = next((lb for g in gg for k, lb in g["sequence"] if k == "texte"), None)
            if prem is not None and not prem.lignes_expl:
                anomalie("numerotation_debut_fichier", "info",
                         "Le fichier commence sans \\ligne{n} : compilé seul, reledmac "
                         "numéroterait à partir de 1 ; la numérotation est ici enchaînée "
                         "sur celle du fichier précédent (dernier n° %d)." % prec_g,
                         fichier=ex.nom, ligne=ex.ligne_src(gg[0]["debut_actif"]))
        prec_g = emuler_numerotation(gg, prec_g)
        prec_d = emuler_numerotation(dd, prec_d)
        for g in gg:
            g["ex"] = ex
        for g in dd:
            g["ex"] = ex
        if len(gg) != len(dd):
            anomalie("nombre_groupes", "grave",
                     "Nombre de groupes différent : %d (grec) / %d (français)" % (len(gg), len(dd)),
                     fichier=ex.nom)
        tous_g.extend(gg)
        tous_d.extend(dd)

    # -- 2. lignes grecques, annotations ------------------------------------------------
    groupes_json = []
    lignes_g_all = []
    apparats_all = []
    compteur = Counter()

    def nouvel_id(prefixe):
        compteur[prefixe] += 1
        return "%s%04d" % (prefixe, compteur[prefixe])

    def annotations_de(ex, lb, ancre, cote, gid):
        res = defaultdict(list)
        for typ, nd in lb.annotations:
            d = ex.annotation(typ, nd, ancre)
            d["cote"] = cote
            d["groupe"] = gid
            res[typ].append(d)
        return res

    for gi, (G, D) in enumerate(zip(tous_g, tous_d), start=1):
        ex = G["ex"]
        gid = "G%04d" % gi
        gj = {"id": gid, "ordre": gi, "fichier": ex.nom,
              "etiquette": G["etiquette"], "etiquette_fr": D["etiquette"]}
        # --- grec
        lignes = []
        comms, notes_seq, apps, tests = [], [], [], []
        seq_annot = []     # ordre : (type, dict)
        for k, lb in G["sequence"]:
            if k != "texte":
                continue
            L = {
                "texte": texte_ligne(ex, lb), "latex": latex_ligne(ex, lb),
                "n_reledmac": lb.n_reledmac, "compte": lb.compte,
                "lignes_expl": lb.lignes_expl, "decalage": lb.decalage,
                "decoupe": lb.decoupe, "strophe": lb.strophe,
                "type": lb.type_vers, "metre": lb.metre,
                "personnage": normaliser_personnage(lb.personnage),
                "ligne_source": ex.ligne_src(lb.debut), "fin_par": lb.fin_par,
                "rejet": lb.rejet, "groupe": gid,
            }
            L["sq"] = grec_squelette(L["texte"])
            L["etiquette"] = G["etiquette"]
            L["ordre_groupe"] = gi
            if (lb.type_vers or "").endswith("Fr"):
                anomalie("macro_francaise_cote_grec", "mineure",
                         "Ligne grecque saisie avec la macro française \\%s (indentation du "
                         "français) — « %s »" % (lb.type_vers, L["texte"][:60]), groupe=gid,
                         fichier=ex.nom, ligne=L["ligne_source"])
            lignes.append(L)
            lb._L = L
        # annotations (après avoir les lignes, pour les ancres)
        for lb in G["lignes"]:
            ancre = lb.n_reledmac
            for typ, nd in lb.annotations:
                d = ex.annotation(typ, nd, ancre)
                d["cote"] = "grec"
                d["groupe"] = gid
                d["_ligne"] = lb._L
                seq_annot.append(d)
        # rattachement des notes aux commentaires
        dernier_comm = None
        bloc = None
        for d in seq_annot:
            t = d["type"]
            if t == "commentaire":
                d["id"] = nouvel_id("C")
                d["notes"] = []
                d["debut_note"] = None
                comms.append(d)
                dernier_comm = d
                bloc = None
            elif t == "debutNote":
                bloc = d
                if dernier_comm is not None and dernier_comm["debut_note"] is None:
                    dernier_comm["debut_note"] = d["plage"]
                    if d["plage"].replace(" ", "") != dernier_comm["plage"].replace(" ", ""):
                        anomalie("note_plage", "mineure",
                                 "\\debutNote{%s} après \\commentaire{%s}" % (d["plage"], dernier_comm["plage"]),
                                 groupe=gid, fichier=ex.nom, ligne=d["ligne_source"])
                else:
                    anomalie("note_sans_commentaire", "moyenne",
                             "\\debutNote{%s} sans commentaire précédent dans le groupe" % d["plage"],
                             groupe=gid, fichier=ex.nom, ligne=d["ligne_source"])
            elif t == "note":
                d["id"] = nouvel_id("N")
                if dernier_comm is not None:
                    d["commentaire"] = dernier_comm["id"]
                    dernier_comm["notes"].append(d)
                    if bloc is None:
                        anomalie("note_sans_debutNote", "mineure",
                                 "\\note{%s} sans \\debutNote préalable" % d["numero"],
                                 groupe=gid, fichier=ex.nom, ligne=d["ligne_source"])
                else:
                    d["commentaire"] = None
                    anomalie("note_orpheline", "moyenne",
                             "\\note{%s} sans commentaire dans le groupe" % d["numero"],
                             groupe=gid, fichier=ex.nom, ligne=d["ligne_source"])
                notes_seq.append(d)
            elif t == "apparat":
                d["id"] = nouvel_id("A")
                apps.append(d)
            elif t == "testimonia":
                d["id"] = nouvel_id("T")
                tests.append(d)
        # contrôle appels / notes
        for c in comms:
            nums = [n["numero"].strip() for n in c["notes"]]
            appels = [a.strip() for a in c["appels"]]
            # rattachement explicite de chaque note à son (ses) appel(s) \marqueur{n} dans le
            # commentaire : nombre d'appels et contexte LaTeX qui précède chacun
            for nd_ in c["notes"]:
                num = nd_["numero"].strip()
                ctx = [re.sub(r"\s+", " ", c["latex"][max(0, m.start() - 70):m.start()]).strip()
                       for m in re.finditer(r"\\marqueur\{\s*%s\s*\}" % re.escape(num), c["latex"])]
                nd_["appel"] = {"marqueur": num, "occurrences": appels.count(num), "contexte": ctx}
            for a in appels:
                if a not in nums:
                    anomalie("appel_sans_note", "moyenne",
                             "Commentaire %s (%s) : appel \\marqueur{%s} sans \\note active" % (c["id"], c["plage"], a),
                             groupe=gid, fichier=ex.nom, ligne=c["ligne_source"])
            for n in nums:
                if n not in appels:
                    anomalie("note_sans_appel", "mineure",
                             "Commentaire %s (%s) : \\note{%s} sans appel \\marqueur correspondant" % (c["id"], c["plage"], n),
                             groupe=gid, fichier=ex.nom, ligne=c["ligne_source"])
            for k, n in enumerate(nums, start=1):
                if n != str(k):
                    anomalie("notes_ordre", "mineure",
                             "Commentaire %s (%s) : notes numérotées %s" % (c["id"], c["plage"], ",".join(nums)),
                             groupe=gid, fichier=ex.nom, ligne=c["ligne_source"])
                    break
            if len(appels) != len(set(appels)):
                anomalie("appel_double", "mineure",
                         "Commentaire %s (%s) : appels répétés %s" % (c["id"], c["plage"], ",".join(appels)),
                         groupe=gid, fichier=ex.nom, ligne=c["ligne_source"])
        gj["_lignes"] = lignes
        gj["_comms"], gj["_apps"], gj["_tests"], gj["_notes"] = comms, apps, tests, notes_seq
        gj["_G"], gj["_D"] = G, D
        lignes_g_all.extend(lignes)
        apparats_all.extend(apps)
        groupes_json.append(gj)

    # -- 3. numéros de vers (grec) -------------------------------------------------------
    apres_vide = False
    for G in tous_g:
        for k, lb in G["sequence"]:
            if k == "vide":
                apres_vide = apres_vide or lb.vide_comptee
                continue
            lb._L["apres_vide"] = apres_vide
            apres_vide = False
    for app in apparats_all:
        for seg in app["segments"]:
            if seg.get("separateur_manuel"):
                anomalie("apparat_numero_manuel", "mineure",
                         "Apparat %s (%s) : numéro de vers « %s » saisi en gras (\\textbf) au lieu de "
                         "\\ligneApp ; segment découpé comme un \\ligneApp" % (app["id"], app["plage"], seg["vers"]),
                         groupe=app["groupe"], vers=seg["debut"], ligne=app["ligne_source"])
    preuves_apparat(lignes_g_all, apparats_all)
    supprimes = vers_supprimes(apparats_all)
    attribuer_vers_grec(lignes_g_all, anomalies, hg, supprimes)

    for gj in groupes_json:
        for d in gj["_comms"] + gj["_apps"] + gj["_tests"] + gj["_notes"]:
            L = d.get("_ligne")
            if L is not None:
                d["ancre"] = L["vers"]
        for c in gj["_comms"]:
            for n in c["notes"]:
                L = n.get("_ligne")
                if L is not None:
                    n["ancre"] = L["vers"]
            if not c["plage"].strip():
                prec = [x for x in gj["_comms"] if x is not c and x["ligne_source"] < c["ligne_source"]]
                if not prec:
                    prec = [x for g2 in groupes_json[:groupes_json.index(gj)] for x in g2["_comms"]][-1:]
                if prec:
                    c["suite_de"] = prec[-1]["id"]
                    c["plage_effective"] = prec[-1]["plage"]
                anomalie("commentaire_sans_plage", "info",
                         "Commentaire %s sans plage ni lemme (suite du commentaire précédent ?) — « %s »"
                         % (c["id"], c["texte"][:60]), groupe=gj["id"], fichier=gj["fichier"],
                         ligne=c["ligne_source"])

    # -- 4. côté français, appariement par groupe ----------------------------------------
    for gj in groupes_json:
        G, D = gj["_G"], gj["_D"]
        ex = D["ex"]
        gid = gj["id"]
        lignes_fr = []
        tests_fr, comms_fr, autres_fr = [], [], []
        for k, lb in D["sequence"]:
            if k != "texte":
                continue
            txt = texte_ligne(ex, lb)
            F = {"texte": txt, "latex": latex_ligne(ex, lb), "n_reledmac": lb.n_reledmac,
                 "compte": lb.compte, "lignes_expl": lb.lignes_expl, "retrait": lb.retrait,
                 "type": lb.type_vers, "personnage": normaliser_personnage(lb.personnage),
                 "ligne_source": ex.ligne_src(lb.debut), "fin_par": lb.fin_par,
                 "rejet": lb.rejet, "didascalies": didascalies(txt), "groupe": gid}
            for s in F["didascalies"]:
                if s.startswith("ll "):
                    anomalie("coquille_traduction", "mineure",
                             "Didascalie « (%s) » : « ll » pour « Il »" % s, groupe=gid,
                             fichier=gj["fichier"], ligne=F["ligne_source"])
            lignes_fr.append(F)
            for typ, nd in lb.annotations:
                d = ex.annotation(typ, nd, lb.n_reledmac)
                d["cote"] = "francais"
                d["groupe"] = gid
                d["_F"] = F
                if typ == "testimonia":
                    d["id"] = nouvel_id("T")
                    tests_fr.append(d)
                elif typ == "commentaire":
                    d["id"] = nouvel_id("C")
                    d["notes"] = []
                    comms_fr.append(d)
                else:
                    autres_fr.append(d)
        # appariement des lignes grec/français à l'intérieur du groupe
        Lg = [L for L in gj["_lignes"] if L["vers"] is not None]
        nb_g = len(Lg)
        nb_f = len(lignes_fr)
        for F in lignes_fr:
            F["vers"], F["vers_fin"], F["partie"] = None, None, ""
        if nb_f == nb_g:
            # grec transposé (lignes imprimées hors de l'ordre usuel) : la traduction, elle,
            # suit l'ordre usuel ; on l'apparie aux lignes grecques rangées par numéro de vers
            if any(L.get("transposee") for L in Lg):
                Lg_ordre = [Lg[k] for k in sorted(range(nb_g), key=lambda k: (Lg[k]["vers"], k))]
            else:
                Lg_ordre = Lg
            for F, L in zip(lignes_fr, Lg_ordre):
                F["vers"] = L["vers"]
                F["vers_fin"] = L.get("vers_fin")
                F["partie"] = L["partie"]
                F["methode_vers"] = ("appariement ligne à ligne dans l'ordre usuel des vers "
                                     "(grec imprimé transposé)" if L.get("transposee")
                                     else "appariement ligne à ligne dans le groupe")
        elif nb_g and nb_f:
            paires = aligner_traduction(lignes_fr, Lg)
            for fi, gi_ in paires:
                vs = [Lg[k]["vers"] for k in gi_]
                for k in fi:
                    F = lignes_fr[k]
                    F["vers"] = vs[0]
                    fin = max(vs[-1], Lg[gi_[-1]].get("vers_fin") or 0)
                    F["vers_fin"] = fin if fin > vs[0] else None
                    F["partie"] = Lg[gi_[0]]["partie"] if len(gi_) == 1 and len(fi) == 1 else ""
                    F["methode_vers"] = ("alignement par longueurs (%d ligne(s) fr. / %d ligne(s) gr.)"
                                         % (len(fi), len(gi_)))
            anomalie("alignement_lignes", "info" if abs(nb_f - nb_g) <= 1 else "mineure",
                     "Groupe %s (%s) : %d ligne(s) grecque(s) numérotée(s) / %d ligne(s) française(s) "
                     "— alignement par longueurs" % (gid, gj["etiquette"], nb_g, nb_f), groupe=gid,
                     fichier=ex.nom, ligne=lignes_fr[0]["ligne_source"] if lignes_fr else None)
        else:
            if nb_f and not nb_g:
                anomalie("alignement_lignes", "moyenne",
                         "Groupe %s (%s) : traduction sans ligne grecque numérotée" % (gid, gj["etiquette"]),
                         groupe=gid, fichier=ex.nom, ligne=lignes_fr[0]["ligne_source"])
            elif nb_g and not nb_f:
                anomalie("alignement_lignes", "moyenne",
                         "Groupe %s (%s) : vers grecs sans traduction" % (gid, gj["etiquette"]),
                         groupe=gid, fichier=ex.nom)
        for d in tests_fr + comms_fr + autres_fr:
            d["ancre"] = d["_F"].get("vers")
        # étiquettes %% v. …
        if (gj["etiquette"] or "") != (gj["etiquette_fr"] or ""):
            anomalie("etiquette_differente", "info",
                     "Groupe %s : étiquette grecque « %s » / française « %s »"
                     % (gid, gj["etiquette"], gj["etiquette_fr"]), groupe=gid, fichier=ex.nom)
        # personnages
        pg = [normaliser_personnage(p) for p in G["parcours"].personnages]
        pf = [normaliser_personnage(p) for p in D["parcours"].personnages]
        if len(pg) != len(pf):
            anomalie("personnage_absent", "moyenne",
                     "Groupe %s (%s) : personnages grec %s / français %s" % (gid, gj["etiquette"], pg, pf),
                     groupe=gid, fichier=ex.nom)
        gj["_fr"] = lignes_fr
        gj["_tests_fr"], gj["_comms_fr"], gj["_autres_fr"] = tests_fr, comms_fr, autres_fr

    # -- 5. vérifications de numérotation -----------------------------------------------
    for L in lignes_g_all:
        v = L["vers"]
        if v is None:
            continue
        if L["methode"].startswith("corrigé") or "consommé" in L["methode"]:
            anomalie("numero_corrige", "info",
                     "v. %s : %s (n° reledmac %s) — « %s »" % (v, L["methode"], L["n_reledmac"], L["texte"][:60]),
                     groupe=L["groupe"], vers=v, ligne=L["ligne_source"])
    ok_app, ko_app = controle_apparat(lignes_g_all, apparats_all, anomalie)
    controle_app = {"segments_verifies": ok_app + ko_app, "concordants": ok_app, "decales": ko_app}
    # écarts avec Hall-Geldart regroupés en séries de décalage constant ; les lignes brèves
    # que HG contient dans plusieurs vers (refrain « Ἀρταμουξία. », vv. 1201-1225) ne sont pas
    # comparées : leur appariement désigne n'importe laquelle des occurrences
    def ambigu_hg(sq):
        return hg is not None and 0 < len(sq) < 20 and \
            len({l["base"] for l in hg.lignes if sq in l["sq"]}) >= 2
    ambigus_hg = {L["sq"] for L in lignes_g_all if ambigu_hg(L["sq"])}
    serie = None
    series_hg = []
    for L in lignes_g_all:
        v = L["vers"]
        hgb = L.get("HG")
        if v is None or not hgb or hgb["cov_a"] < 0.85:
            continue
        if L["sq"] in ambigus_hg:
            continue
        lo = hgb["base"]
        hi = int(re.match(r"\d+", hgb["n_fin"]).group())
        vf = L.get("vers_fin") or v
        if lo <= v <= hi or lo <= vf <= hi:
            d = 0
        else:
            d = v - lo
        if serie and serie["d"] == d:
            serie["lignes"].append(L)
        else:
            serie = {"d": d, "lignes": [L]}
            series_hg.append(serie)
    for se in series_hg:
        if se["d"] == 0:
            continue
        Ls = se["lignes"]
        a, b = Ls[0], Ls[-1]
        lyr = all(L["type"] in LYRIQUES for L in Ls)
        anomalie("numero_diff_HG", "info" if (lyr or len(Ls) > 2) else "moyenne",
                 "vv. %s-%s (%d ligne(s), %s) : numérotation de l'auteur = Hall-Geldart %+d "
                 "(ex. « %s » = HG %s)" % (a["vers"], b["vers"], len(Ls),
                                          "lyrique" if lyr else ", ".join(sorted({str(L["type"]) for L in Ls})),
                                          se["d"], a["texte"][:40], a["vers_HG"]),
                 groupe=a["groupe"], vers=a["vers"], ligne=a["ligne_source"])
    # contrôle par les étiquettes « %% v. … » des groupes
    for L in lignes_g_all:
        e = L.get("etq_debut")
        if not e or L["vers"] is None:
            continue
        n, p = e
        if n != L["vers"] or (p and p not in ("a",) and not L["partie"]) or \
                (p and L["partie"] and p != L["partie"] and not (p == "a" and L["partie"] == "")):
            anomalie("etiquette_vers", "mineure",
                     "Groupe %s : étiquette « %s » mais première ligne numérotée %s%s — « %s »"
                     % (L["groupe"], L["etiquette"], L["vers"], L["partie"], L["texte"][:50]),
                     groupe=L["groupe"], vers=L["vers"], ligne=L["ligne_source"])
    # séquence : numéros manquants, régressions
    numerotees = [L for L in lignes_g_all if L["vers"] is not None]
    couverts = set()
    consommes = {}
    for L in numerotees:
        couverts.update(range(L["vers"], (L.get("vers_fin") or L["vers"]) + 1))
        for n in L.get("numeros_consommes") or []:
            consommes[n] = L
    hg_bases = {l["base"] for l in hg.lignes} if hg else set()
    for a, b in zip(numerotees, numerotees[1:]):
        if b["vers"] < a["vers"] and not (a.get("transposee") and b.get("transposee")):
            # (une transposition est déjà signalée comme telle)
            anomalie("numero_regression", "moyenne", "Régression de numérotation : %d puis %d (« %s »)"
                     % (a["vers"], b["vers"], b["texte"][:50]), groupe=b["groupe"], vers=b["vers"],
                     ligne=b["ligne_source"])
    if numerotees:
        manquants = [n for n in range(1, max(couverts) + 1) if n not in couverts]
        for n in manquants:
            L = consommes.get(n)
            hg_absent = bool(hg) and n not in hg_bases
            if n in supprimes:
                anomalie("vers_supprime", "info",
                         "v. %d supprimé par l'auteur (apparat : leçon retenue « del. »)" % n, vers=n,
                         groupe=L["groupe"] if L else None, ligne=L["ligne_source"] if L else None)
            elif L is not None:
                anomalie("vers_absent", "info",
                         "v. %d absent du texte de l'auteur (n° consommé par \\ligne sur la ligne du v. %d%s)"
                         % (n, L["vers"], " ; absent aussi de Hall-Geldart" if hg_absent else ""),
                         groupe=L["groupe"], vers=n, ligne=L["ligne_source"])
            else:
                suiv = next((x for x in numerotees if x["vers"] > n), None)
                prec = next((x for x in reversed(numerotees) if x["vers"] < n), None)
                if hg_absent:
                    detail = " (absent aussi de Hall-Geldart)"
                elif suiv is not None and suiv["vers"] in (suiv.get("lignes_expl") or []):
                    # saut voulu : \ligne{n+1} explicite ; dans les parties lyriques, l'auteur recale
                    # sa colométrie sur la numérotation usuelle (une ligne voisine vaut deux numéros)
                    detail = (" : saut explicite (\\ligne{%d} sur « %s ») après le v. %d (« %s ») ; "
                              "numérotation recalée par l'auteur (colométrie différente de celle de "
                              "Hall-Geldart)"
                              % (suiv["vers"], suiv["texte"][:30], prec["vers"] if prec else 0,
                                 prec["texte"][:30] if prec else ""))
                else:
                    detail = ""
                anomalie("numero_saut", "info" if (hg_absent or detail) else "moyenne",
                         "v. %d absent de la numérotation de l'auteur%s" % (n, detail), vers=n,
                         groupe=suiv["groupe"] if suiv else None,
                         ligne=suiv["ligne_source"] if suiv else None)

    # -- 6. sérialisation ----------------------------------------------------------------
    sortie_groupes = []
    for gj in groupes_json:
        G, D = gj["_G"], gj["_D"]
        lignes = gj["_lignes"]
        vs = [L["vers"] for L in lignes if L["vers"] is not None]
        ex = G["ex"]
        a_or = ex.src.orig_de_actif(G["debut_actif"])
        b_or = ex.src.orig_de_actif(G["fin_actif"] - 1)
        # matériaux désactivés (commentés) dans le groupe, hors annotations actives
        desact_g = macros_commentees(ex, G["debut_actif"], G["fin_actif"])
        desact_d = macros_commentees(D["ex"], D["debut_actif"], D["fin_actif"])
        types = [L["type"] for L in lignes]
        g_out = {
            "id": gj["id"], "ordre": gj["ordre"], "fichier": gj["fichier"],
            "etiquette": gj["etiquette"],
            "vers": [min(vs), max(vs)] if vs else None,
            "personnages": [normaliser_personnage(p) for p in G["parcours"].personnages],
            "personnage_courant": normaliser_personnage(lignes[0]["personnage"]) if lignes else None,
            "types_vers": sorted(set(t for t in types if t), key=types.index),
            "metres": [L["metre"] for L in lignes if L["metre"]],
            "en_tetes": G["parcours"].en_tetes + D["parcours"].en_tetes,
            "strophes": [{"vers": L["vers"], "label": L["strophe"]} for L in lignes if L["strophe"]],
            "lignes_source": [ex.src.ligne_orig(a_or), ex.src.ligne_orig(b_or)],
            "grec": {
                "lignes": [{
                    "vers": L["vers"], "partie": L["partie"], "texte": L["texte"],
                    "latex": L["latex"], "personnage": L["personnage"], "type": L["type"],
                    "metre": L["metre"], "n_reledmac": L["n_reledmac"],
                    "ligne_explicite": L["lignes_expl"][-1] if L["lignes_expl"] else None,
                    "antilabe": bool(L["decalage"]), "decoupe": L["decoupe"],
                    "strophe": L["strophe"], "methode_vers": L["methode"],
                    "vers_fin": L.get("vers_fin"),
                    "numeros_consommes": L.get("numeros_consommes") or [],
                    "vers_HG": L["vers_HG"],
                    "HG_couverture": L["HG"]["cov_a"] if L.get("HG") else None,
                    "ligne_source": L["ligne_source"], "fin_par": L["fin_par"],
                } for L in lignes],
                "apparat": [nettoyer(d) for d in gj["_apps"]],
                "testimonia": [nettoyer(d) for d in gj["_tests"]],
                "commentaires": [nettoyer_comm(d) for d in gj["_comms"]],
                "notes_orphelines": [nettoyer(d) for d in gj["_notes"] if not d.get("commentaire")],
                "desactives": desact_g,
            },
            "francais": {
                "personnages": [normaliser_personnage(p) for p in D["parcours"].personnages],
                "lignes": [{
                    "vers": F["vers"], "partie": F.get("partie", ""), "vers_fin": F.get("vers_fin"),
                    "texte": F["texte"],
                    "latex": F["latex"], "personnage": F["personnage"], "type": F["type"],
                    "didascalies": F["didascalies"], "retrait": F["retrait"],
                    "n_reledmac": F["n_reledmac"],
                    "ligne_explicite": F["lignes_expl"][-1] if F["lignes_expl"] else None,
                    "methode_vers": F.get("methode_vers"), "ligne_source": F["ligne_source"],
                    "fin_par": F["fin_par"], "rejet": F["rejet"],
                } for F in gj["_fr"]],
                "testimonia": [nettoyer(d) for d in gj["_tests_fr"]],
                "commentaires": [nettoyer_comm(d) for d in gj["_comms_fr"]],
                "autres_annotations": [nettoyer(d) for d in gj["_autres_fr"]],
                "desactives": desact_d,
            },
        }
        sortie_groupes.append(g_out)

    stats = statistiques(sortie_groupes, anomalies)
    stats["controle_apparat_numerotation"] = controle_app
    meta = {
        "titre": "Thesmophories — extraction des travaux antérieurs de l'auteur (Harmattan 2023)",
        "genere_par": "outils/extraction/extraire_travaux.py",
        "date": datetime.date.today().isoformat(),
        "sources": [{"fichier": rel, "sha256": sha256(os.path.join(depot, rel)),
                     "lignes": extracteurs[i].src.orig.count("\n") + 1}
                    for i, rel in enumerate(fichiers)],
        "reference_numerotation": ("Hall & Geldart (OCT 1907), via Perseus canonical-greekLit "
                                   "tlg0019.tlg008.perseus-grc2 (numéros seulement)") if hg else None,
        "conventions": {
            "vers": "numéro de vers attribué (voir methode_vers) ; None = ligne hors numérotation",
            "partie": "a, b, c… quand un vers est réparti sur plusieurs lignes (antilabè, vers découpé)",
            "n_reledmac": "numéro que reledmac attribuerait (émulation : \\ligne = \\setline, "
                          "\\passeLigne = \\skipnumbering, ligne vide après \\\\ comptée)",
            "vers_HG": "vers de Hall-Geldart dont le texte correspond le mieux (vérification)",
            "texte": "conversion en texte brut (exposants Unicode, ⟦ ⟧ = rature, x̣ = lettre douteuse)",
            "latex": "source LaTeX active (lignes commentées ôtées)",
            "desactives": "macros présentes dans des lignes commentées (%) du groupe",
        },
    }
    resultat = {"meta": meta, "statistiques": stats, "groupes": sortie_groupes,
                "anomalies": anomalies}
    resultat = masquer(resultat, rx_nom)
    if ecrire and sortie:
        os.makedirs(sortie, exist_ok=True)
        with open(os.path.join(sortie, "thesmo.json"), "w", encoding="utf-8") as f:
            json.dump(resultat, f, ensure_ascii=False, indent=1)
        ecrire_tsv(resultat, sortie)
        verifier_masquage(sortie, rx_nom)
    return resultat


def macros_commentees(ex: Extracteur, debut_actif: int, fin_actif: int) -> list:
    """Macros d'apparat/commentaire/testimonia/notes figurant dans des lignes commentées."""
    a = ex.src.orig_de_actif(debut_actif)
    b = ex.src.orig_de_actif(fin_actif - 1)
    comms = ex.src.commentaires_entre(a, b)
    if not comms:
        return []
    # regroupe les commentaires consécutifs (lignes successives) en blocs
    blocs = []
    for c in comms:
        ln = ex.src.ligne_orig(c.debut)
        if blocs and ln - blocs[-1]["fin"] <= 1:
            blocs[-1]["textes"].append(c.texte)
            blocs[-1]["fin"] = ln
        else:
            blocs.append({"debut": ln, "fin": ln, "textes": [c.texte]})
    res = []
    rx = re.compile(r"\\(apparat|testimonia|commentaire|note|debutNote|personnageGrec|personnageFr)\s*\{")
    for bl in blocs:
        t = "\n".join(bl["textes"])
        for m in rx.finditer(t):
            nom = m.group(1)
            nargs = {"apparat": 2, "testimonia": 2, "commentaire": 3, "note": 2,
                     "debutNote": 1, "personnageGrec": 1, "personnageFr": 1}[nom]
            i = m.end() - 1
            args = []
            for _ in range(nargs):
                while i < len(t) and t[i] in " \t\n":
                    i += 1
                if i >= len(t) or t[i] != "{":
                    break
                j, prof = i, 0
                while j < len(t):
                    if t[j] == "\\":
                        j += 2
                        continue
                    if t[j] == "{":
                        prof += 1
                    elif t[j] == "}":
                        prof -= 1
                        if prof == 0:
                            break
                    j += 1
                args.append(t[i + 1:j])
                i = j + 1
            d = {"type": nom, "ligne_source": bl["debut"] + t[:m.start()].count("\n"),
                 "args": args, "complet": len(args) == nargs}
            if args:
                try:
                    an = ex.an.analyser(args[-1])
                    d["texte"] = ex.conv.texte(an)
                except Exception:  # pragma: no cover
                    d["texte"] = args[-1]
            res.append(d)
    return res


def nettoyer(d: dict) -> dict:
    return {k: v for k, v in d.items() if not k.startswith("_")}


def nettoyer_comm(d: dict) -> dict:
    r = nettoyer(d)
    r["notes"] = [nettoyer(n) for n in d.get("notes", [])]
    a, b = plage_vers(d.get("plage"))
    r["debut"], r["fin"] = a, b
    r["longueur"] = len(d.get("texte", ""))
    return r


def statistiques(groupes, anomalies):
    nl_g = sum(len(g["grec"]["lignes"]) for g in groupes)
    nl_f = sum(len(g["francais"]["lignes"]) for g in groupes)
    vers = sorted({l["vers"] for g in groupes for l in g["grec"]["lignes"] if l["vers"] is not None})
    comms = [c for g in groupes for c in g["grec"]["commentaires"]] + \
            [c for g in groupes for c in g["francais"]["commentaires"]]
    notes = sum(len(c["notes"]) for c in comms)
    apps = [a for g in groupes for a in g["grec"]["apparat"]]
    segs = sum(len(a["segments"]) for a in apps)
    tg = sum(len(g["grec"]["testimonia"]) for g in groupes)
    td = sum(len(g["francais"]["testimonia"]) for g in groupes)
    desact = Counter(d["type"] for g in groupes for d in g["grec"]["desactives"] + g["francais"]["desactives"])
    bibi = sum(1 for a in apps for s in a["segments"] for e in s["entrees"]
               for l in e["lecons"] if "Bibi" in l["attribution"] or "Bibi" in l["texte"])
    couverts = set()
    for g in groupes:
        for l in g["grec"]["lignes"]:
            if l["vers"] is not None:
                couverts.update(range(l["vers"], (l.get("vers_fin") or l["vers"]) + 1))
    entrees = [e for a in apps for sg in a["segments"] for e in sg["entrees"]]
    vers_app, vers_comm = set(), set()
    for a in apps:
        for sg in a["segments"]:
            if sg["debut"] is not None:
                vers_app.update(range(sg["debut"], (sg["fin"] or sg["debut"]) + 1))
    for c in comms:
        if c.get("debut") is not None:
            vers_comm.update(range(c["debut"], (c.get("fin") or c["debut"]) + 1))
    longueurs = sorted(c["longueur"] for c in comms)
    supplements = {
        "vers_avec_apparat": len(vers_app),
        "vers_commentes": len(vers_comm),
        "commentaires_avec_notes": sum(1 for c in comms if c["notes"]),
        "caracteres_notes": sum(len(n.get("texte", "")) for c in comms for n in c["notes"]),
        "longueur_mediane_commentaire": longueurs[len(longueurs) // 2] if longueurs else 0,
        "didascalies": sum(len(l.get("didascalies") or []) for g in groupes for l in g["francais"]["lignes"]),
        "lignes_grecques_par_type": dict(Counter(l["type"] for g in groupes for l in g["grec"]["lignes"]).most_common()),
        "lignes_grecques_par_personnage": dict(Counter(l["personnage"] for g in groupes
                                                       for l in g["grec"]["lignes"]).most_common()),
    }
    return {
        "groupes": len(groupes), "lignes_grecques": nl_g, "lignes_francaises": nl_f,
        "vers_distincts": len(vers), "numeros_couverts": len(couverts),
        "premier_vers": vers[0] if vers else None,
        "dernier_vers": vers[-1] if vers else None,
        "commentaires": len(comms), "caracteres_commentaires": sum(c["longueur"] for c in comms),
        "notes": notes, "apparats": len(apps), "segments_apparat": segs,
        "lecons_Bibi": bibi, "testimonia_grec": tg, "testimonia_francais": td,
        "macros_desactivees": dict(desact),
        "apparat_entrees": len(entrees),
        "apparat_lecons": sum(len(e["lecons"]) for e in entrees),
        "apparat_classement": classer_apparat(entrees),
        **supplements,
        "anomalies": dict(Counter(a["code"] for a in anomalies)),
    }


RE_APP_INDIRECTE = re.compile(r"Suid|Σ|Schol|Hesych|Phot|Pollux|PSI|POxy|Eust|Greg|Stob|Moeris|Zonar|Etym|"
                              r"Harp|Antiatt|cod\. Laur|Ael|Gellius|Plut\.|(?<!ad )Eur\. |(?<!ad )Hel\.\d")
RE_APP_R = re.compile(r"(?:^|[\s,⟧)])R(?![A-Za-z])")
RE_APP_M = re.compile(r"(?:^|[\s,)])M(?![A-Za-z])|Μυ2")
RE_APP_NOM = re.compile(r"(?:van |von )?[A-ZÀ-Ý][a-zà-ÿ]+(?:(?: & |-)[A-Z][a-z]+)?|edd?\.(?: pr\.| omn(?:es)?\.?| pler(?:ique)?\.?)?")
NON_CRITIQUES = {"Suid", "Schol", "Hesych", "Hesychius", "Phot", "Photius", "Pollux", "Divus", "Bibi", "Eur", "Hel",
                 "Il", "Pl", "Nub", "Nubes", "Vesp", "Pax", "Ach", "Lys", "Lysistr", "Ran", "Av", "Eq", "Med", "Or",
                 "Theag", "Gorg", "Hipp", "Greg", "Cor", "Stob", "Eust", "Eustathe", "Moeris", "Gram", "Etym",
                 "Magn", "Gen", "Ael", "Dion", "Harp", "Antiatt", "Zonaras", "Plat", "Mosch", "Hom", "Gr", "Versk",
                 "Paratragödia", "Mnemosyne", "Iuntina", "Laur", "Laurent", "Parisinus", "Hec", "Bacch",
                 "Aristophanica", "Gellius", "Plut", "Stob", "Oxy", "Mél", "Suppl", "Obs", "Mor", "Ar", "Gregor",
                 "Coppello", "Sigma"}


def classer_apparat(entrees: list) -> dict:
    r"""Classement heuristique des entrées d'apparat selon l'autorité de la leçon retenue
    (\lecon) : Bibi ; R conservé (R, R², Rᵖᶜ) ; tradition indirecte ou papyrus ; M ; critique
    nommé (ou « edd. ») ; entrées sans leçon retenue (descriptives : corrections de R, sigles de
    personnages…). Compte aussi les critiques nommés dans tout l'apparat."""
    cl, retenus, cites = Counter(), Counter(), Counter()
    for e in entrees:
        for n in RE_APP_NOM.findall(e["texte"]):
            if n.split()[-1] not in NON_CRITIQUES and not n.startswith("ed"):
                cites[n] += 1
        r = [l for l in e["lecons"] if l["retenue"]]
        if not r:
            cl["descriptive (sans leçon retenue)"] += 1
            continue
        a = " ".join(l["attribution"] or "" for l in r)
        if "Bibi" in a:
            cl["Bibi"] += 1
        elif RE_APP_R.search(a):
            cl["R conservé"] += 1
        elif RE_APP_INDIRECTE.search(a):
            cl["tradition indirecte ou papyrus"] += 1
        elif RE_APP_M.search(a):
            cl["M"] += 1
        else:
            m = RE_APP_NOM.search(a)
            cl["critique nommé"] += 1
            retenus[m.group() if m else "?"] += 1
    return {"par_autorite_de_la_lecon_retenue": dict(cl.most_common()),
            "critiques_retenus": dict(retenus.most_common()),
            "critiques_cites": dict(cites.most_common())}


def ecrire_tsv(res, sortie):
    def w(nom, entetes, lignes):
        with open(os.path.join(sortie, nom), "w", encoding="utf-8", newline="") as f:
            wr = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
            wr.writerow(entetes)
            for l in lignes:
                wr.writerow(["" if x is None else str(x).replace("\t", " ").replace("\n", " ¶ ")
                             for x in l])

    G = res["groupes"]
    w("texte_grec.tsv",
      ["vers", "partie", "vers_fin", "personnage", "texte", "groupe", "type", "metre",
       "n_reledmac", "vers_HG", "methode_vers", "fichier", "ligne_source"],
      [[l["vers"], l["partie"], l["vers_fin"], l["personnage"], l["texte"], g["id"], l["type"],
        l["metre"], l["n_reledmac"], l["vers_HG"], l["methode_vers"], g["fichier"], l["ligne_source"]]
       for g in G for l in g["grec"]["lignes"]])
    w("traduction.tsv",
      ["vers", "partie", "vers_fin", "personnage", "texte", "didascalies", "groupe", "methode_vers",
       "fichier", "ligne_source"],
      [[l["vers"], l["partie"], l["vers_fin"], l["personnage"], l["texte"], " | ".join(l["didascalies"]),
        g["id"], l["methode_vers"], g["fichier"], l["ligne_source"]]
       for g in G for l in g["francais"]["lignes"]])
    rows = []
    for g in G:
        for a in g["grec"]["apparat"]:
            for s in a["segments"]:
                bibi = any("Bibi" in l["attribution"] or "Bibi" in l["texte"]
                           for e in s["entrees"] for l in e["lecons"])
                retenues = " ; ".join(l["lecon"] + (" (" + l["attribution"] + ")" if l["attribution"] else "")
                                      for e in s["entrees"] for l in e["lecons"] if l["retenue"])
                rows.append([a["id"], s["vers"], s["debut"], a["plage"], g["id"], s["texte"],
                             retenues, "oui" if bibi else "", s["latex"], g["fichier"],
                             a["ligne_source"]])
    w("apparat.tsv", ["id", "vers", "premier_vers", "plage_apparat", "groupe", "texte",
                      "lecon_retenue", "Bibi", "latex", "fichier", "ligne_source"], rows)
    rows = []
    for g in G:
        for cote in ("grec", "francais"):
            for c in g[cote]["commentaires"]:
                rows.append([c["id"], c["plage"], c["lemme"], c["longueur"], c["debut"], c["fin"],
                             len(c["notes"]), g["id"], cote, g["fichier"], c["ligne_source"]])
    w("commentaires.tsv", ["id", "plage", "lemme", "longueur", "premier_vers", "dernier_vers",
                           "notes", "groupe", "cote", "fichier", "ligne_source"], rows)
    rows = []
    for g in G:
        for cote in ("grec", "francais"):
            for t in g[cote]["testimonia"]:
                rows.append([t["id"], t["plage"], cote, "actif", t["texte"], g["id"], g["fichier"],
                             t["ligne_source"]])
            for d in g[cote]["desactives"]:
                if d["type"] == "testimonia" and d.get("args"):
                    rows.append(["", d["args"][0], cote, "désactivé", d.get("texte", ""), g["id"],
                                 g["fichier"], d["ligne_source"]])
    w("testimonia.tsv", ["id", "plage", "cote", "etat", "texte", "groupe", "fichier", "ligne_source"], rows)
    w("anomalies.tsv", ["code", "gravite", "groupe", "vers", "fichier", "ligne_source", "message"],
      [[a["code"], a["gravite"], a["groupe"], a["vers"], a["fichier"], a["ligne_source"], a["message"]]
       for a in res["anomalies"]])


def verifier_masquage(sortie, rx):
    if rx is None:
        return
    for nom in os.listdir(sortie):
        with open(os.path.join(sortie, nom), encoding="utf-8") as f:
            if rx.search(f.read()):
                raise SystemExit("ERREUR : donnée personnelle non masquée dans " + nom)


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    depot_def = os.path.abspath(os.path.join(ici, "..", ".."))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=depot_def)
    ap.add_argument("--sortie", default=None)
    a = ap.parse_args()
    sortie = a.sortie or os.path.join(a.depot, "edition", "donnees", "travaux_anterieurs")
    res = extraire(a.depot, sortie)
    s = res["statistiques"]
    print(json.dumps(s, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
