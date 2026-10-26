# Travaux antérieurs de l'auteur (dossier `latex/`) — analyse et extraction

> État : **version de travail** (reprise le 2026-10-26 après interruption). Sections 1-4 rédigées et
> revérifiées (l'extraction est reproductible à l'identique) ; sections 5-11 en cours de rédaction.
> Sources : `latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `… vv 642-fin-bis.tex` (version de
> référence, dite ici « Harmattan 2023 »), versions antérieures `… nov 2022.tex` et `… Harmattan mars 2023.tex`,
> `… Introduction.tex`, `… Annexes.tex`, `… Index.tex`. Les fichiers « Edition 4 pages Ravennas » (Gemini) sont
> exclus. Les citations du commentaire de l'auteur sont données ici à titre d'analyse ; le nom réel de l'auteur
> (présent dans `\author{}` et dans les annexes) n'est jamais reproduit.

## 1. Architecture des fichiers et des macros

### 1.1 Fichiers

| Fichier | Lignes | Contenu |
|---|---:|---|
| `Harmattan 2023 vv 1-641.tex` | 6 886 | vv. 1-638 (le dernier groupe est 637-8, malgré le nom) |
| `Harmattan 2023 vv 642-fin-bis.tex` | 7 729 | vv. 639-1231 (`\setcounter{page}{151}`) |
| `Harmattan mars 2023.tex` | 10 307 | vv. 1-946 (état intermédiaire, 541 groupes) |
| `nov 2022.tex` | 13 092 | pièce entière (773 groupes) |
| `Introduction.tex` | 421 | date, synopsis, bibliographie commentée, dossier Mnésiloque, témoins (sigles), personnages |
| `Annexes.tex` | 1 869 | Willems (notice, bibliographie, 28 notes sur les *Thesmophories*), papyrus, iconographie, polémique |
| `Index.tex` | 441 | quatre index (allusions proverbiales, gloses d'Hésychius, corrections proposées, passages expliqués) |

Classe `book` 12 pt, `fontspec` + `polyglossia` (français ; grec en Unicode direct, police GFS Bodoni),
`reledmac` (option `parapparatus`) et `reledpar` (`parledgroup`, `nomaxlines`), `fancyhdr`, `geometry`
(format Harmattan : 12 × 22,5 cm). Les deux fichiers 2023 ont le même préambule (à trois détails près :
`\Xonlyside[A]{R}` — testimonia imprimés en page de droite seulement — et `\setcounter{page}{151}` dans le
second ; `\GregCor` et `\anglais` redéfinis).

### 1.2 Structure du corps

```
\begin{pages}
  \begin{Leftside} \beginnumbering
     %% v. 1-4                      ← étiquette (commentaire) avant chaque groupe
     \begin{groupe}                 ← = \pstart\ledgroup … \pend  (un paragraphe reledmac)
        \enTeteG{…}  \personnageGrec{Μνησίλοχος}
        \typeVers{$3$ ia.}\trimIamb{ vers 1 \apparat{1}{…} \\
                                     vers 2 \commentaire{1-10}{lemme}{texte} \debutNote{1-10} \note{1}{…} … \\
                                     … \\ \passeLigne }
     \end{groupe}
     …
  \endnumbering \end{Leftside}
  \begin{Rightside} … mêmes groupes, en français (\personnageFr, \trimIambFr, \testimonia{…}) … \end{Rightside}
\end{pages}
\Pages
```

Les groupes grecs et français se répondent un à un (reledpar `parledgroup`) : 375 + 402 = **777 groupes** de
chaque côté, sans écart.

### 1.3 Macros de l'auteur (préambule)

| Famille | Macros | Rôle / rendu |
|---|---|---|
| Types de vers (grec / français) | `\trimIamb`, `\trimIambCat`, `\tetramIamb`, `\tetramIambCat`, `\tetramTroch`, `\tetramAnap`, `\dimAnap`, `\anap`, `\diDoch`, `\chantAgath`, `\chantChoeur`, `\paratragiques`, `\prose` et leurs doublets `…Fr` | indentation (`\hangindent`) propre à chaque mètre ; l'argument contient les vers séparés par `\\` |
| Métrique | `\typeVers{…}` (marge gauche), `\cat` (catalexe), `\decoupeVers{a|b|chiffres}` (aujourd'hui vide ; ancien `\linenumannotation`) | analyse métrique colon par colon dans les parties lyriques |
| Personnages | `\personnageGrec{…}`, `\personnageFr{…}` (`\ledleftnote`), `\strophe{…}`, `\Strophe{…}` | locuteur en marge ; étiquettes strophe/antistrophe/mésode/pnigos |
| Numérotation | `\ligne{n}` = `\setline{n}\hidenumbering`, `\passeLigne` = `\skipnumbering`, `\fin` (rejet : saut de ligne non compté + `[`), `\linenumberlist{…}` (numéros imprimés) | voir § 3.3 |
| Antilabè | `\decalage{texte}` (espace de la largeur du texte), `\decalageN` | seconde moitié de vers décalée |
| Apparat critique | `\apparat{vers}{…}` (`\ledrightnote` : minipage en marge droite), `\lecon{…}` (leçon retenue, gras), `\ligneApp{n}` (vers suivant), `\espApp` (entrée suivante) | apparat **positif** : R : leçon retenue + autorité |
| Commentaire | `\commentaire{plage}{lemme}{texte}` (`\Bfootnote`), `\citComm{…}` (citation en retrait), `\marqueur{n}` (appel) | commentaire continu en bas de page |
| Notes du commentaire | `\debutNote{plage}` puis `\note{n}{…}` (`\Cfootnote`) | notes numérotées par commentaire |
| Testimonia | `\testimonia{vers}{…}` (`\Afootnote`), `\espTest` | côté grec (désormais surtout commentés) et côté français |
| Sigles | `\Rpc`, `\Rac`, `\Rdeux` (R², R^pc, R^ac), `\Mon` (M), `\PsiUn` … `\PsiCinq` (PSI-1194, POxy-3839, POxy-3840, POxy-4935, POxy-1176) | |
| Abréviations | `\Fr` (Ar. fragm. Kassel-Austin), `\Syn`, `\SynB`, `\Eustathe`, `\Phryn`, `\Apostol`, `\Macaire`, `\EtymMagnum`, `\EtymGen`, `\EtymSym`, `\AelDion`, `\Antiatt`, `\Harp`, `\Stobee`, `\GregCor`, `\EpimAlphab`, `\ClemAlex`, `\LSJ`, `\Nauck` | testimonia |
| Graphie | `\douteux` (lettre pointée), `\inRas{a}{b}` (rature), `\auDessus{a}{b}`, `\lettreBreve`, `\synizese`, `\difference` | apparat et commentaire |
| Langues | `\francais`, `\latin`, `\grec`, `\allemand` (Fraktur), `\anglais`, `\italien`, `\espagnol`, `\italique`, `\nieme`, `\expo` | polices distinctes par langue |
| En-têtes | `\enTeteG`, `\enTeteD` | une seule occurrence active (« ΠΡΟΛΟΓΟΣ — Prologue vv. 1-294 ») |
| Brouillon | `\eff{…}` (texte orange : remarque à revoir) | toutes les occurrences sont commentées dans la version 2023 |

## 2. Extraction structurée

### 2.1 Scripts

- `outils/extraction/analyse_latex.py` : suppression des commentaires `%` avec table de correspondance des
  positions, arbre syntaxique (accolades équilibrées, arités lues dans le préambule), conversion en texte brut
  (exposants Unicode, `⟦ ⟧` = rature, lettre pointée = douteuse, `> ` = `\citComm`), normalisation du grec.
- `outils/extraction/extraire_travaux.py` : extraction des deux fichiers Harmattan 2023 (enchaînés),
  numérotation, alignement grec/français, contrôles ; écrit `edition/donnees/travaux_anterieurs/`.
- `outils/extraction/comparer_versions.py` : extraction des versions nov 2022 et mars 2023 avec le même
  analyseur, comparaison avec Harmattan 2023.

Commande : `python3 outils/extraction/extraire_travaux.py && python3 outils/extraction/comparer_versions.py`
(≈ 15 s). Le nom réel de l'auteur est lu dans `\author{}` et masqué dans toutes les sorties (contrôle bloquant).

### 2.2 Sorties (`edition/donnees/travaux_anterieurs/`)

| Fichier | Contenu |
|---|---|
| `thesmo.json` | 777 groupes : ordre, étiquette `%% v.`, vers couverts, personnages, types de vers et mètres, en-têtes, strophes, lignes grecques (vers, partie, texte brut et LaTeX, n° reledmac, méthode d'attribution, vers HG), apparat (brut, découpé par vers, entrées, leçons, leçon retenue), testimonia, commentaires (plage, lemme, LaTeX, texte, appels `\marqueur`, notes rattachées avec numéro, passages commentés internes), notes orphelines, macros désactivées ; côté français : lignes par vers, didascalies, testimonia ; + `statistiques` et `anomalies` |
| `texte_grec.tsv` | une ligne par vers ou partie de vers : `vers, partie, vers_fin, personnage, texte, groupe, type, metre, n_reledmac, vers_HG, methode_vers, fichier, ligne_source` |
| `traduction.tsv` | idem pour la traduction (`didascalies`, méthode d'appariement) |
| `apparat.tsv` | une ligne par segment d'apparat (vers) : texte, leçon(s) retenue(s), drapeau `Bibi`, LaTeX |
| `commentaires.tsv` | `id, plage, lemme, longueur, premier_vers, dernier_vers, notes, groupe, cote, fichier, ligne_source` |
| `testimonia.tsv` | testimonia actifs et désactivés, des deux côtés |
| `anomalies.tsv` | rapport de vérification (§ 12) |
| `comparaison_versions.json/.tsv` | § 11 |

### 2.3 Numérotation des vers : méthode

La numérotation imprimée par reledmac n'est pas lisible directement dans la source. Le script :

1. **émule reledmac** (`n_reledmac`) : chaque ligne de sortie incrémente le compteur, `\ligne{n}` le fixe,
   `\passeLigne` l'annule ; la ligne vide que crée un `\\` final de groupe est comptée si elle n'est pas suivie
   de `\passeLigne` (piège fréquent dans les parties lyriques, où chaque colon forme un groupe) ;
2. **découpe les lignes** sur `\\`, sur les fins de ligne source (la traduction est souvent saisie « un vers par
   ligne » sans `\\`) et sur un `\ligne{n}` placé après du texte (`\\` oublié, ex. v. 295-296) ;
3. **attribue le vers voulu par l'auteur** (`vers`, `partie` a/b/c…, `vers_fin` pour une ligne couvrant
   plusieurs numéros) en combinant : étiquettes `%% v. …` des groupes, `\decoupeVers` (lettre = partie ;
   chiffres = derniers chiffres du vers de fin : `{8}` sur 357 → 357-358), `\ligne{n}`, antilabè
   (`\decalage` + `\ligne` identique), vers supprimés par l'apparat (« del. » retenu : vv. 23, 500), leçons de
   l'apparat retrouvées dans la ligne ; les artefacts (`\ligne{n}` répétant un numéro, `\ligne` erroné sur une
   antilabè, saut réservant le numéro d'un vers supprimé) sont résolus et tracés dans `methode_vers` ;
4. **contrôle** chaque ligne contre le texte de Hall & Geldart (Perseus, `.sources/`, numéros seulement) :
   écarts regroupés en séries de décalage constant ; HG ne prévaut jamais seul contre un numéro explicite de
   l'auteur (HG a lui-même ses lacunes et ses vers « a », et diverge de la numérotation moderne, par ex. à
   1014-1018 : la monodie d'Andromède commence au v. 1015 chez l'auteur comme dans l'usage, au v. 1016 chez HG).

Résultat : 1 400 lignes grecques numérotées, 1 208 numéros de vers distincts de 1 à 1231 ; 6 étiquettes de
groupe seulement (sur 777) restent en désaccord avec le numéro attribué, toutes des étiquettes périmées
(copiées d'un groupe voisin ou non mises à jour après un changement de répartition).

### 2.4 Alignement grec / français

Appariement groupe à groupe (777/777) puis ligne à ligne : identité du nombre de lignes dans 764 groupes ;
pour les 13 autres, alignement par programmation dynamique sur les longueurs (fusions 2:1, 1:2, 3:1 ;
didascalie isolée rattachée au vers précédent). Méthode tracée dans `traduction.tsv` (`methode_vers`).
Limite connue : aux vv. 3-4 le grec est transposé (§ 12) mais la traduction suit l'ordre traditionnel : la
traduction de 3 et 4 est donc croisée dans `traduction.tsv`.

## 3. Statistiques (Harmattan 2023)

| Élément | Nombre |
|---|---:|
| Groupes (de chaque côté) | 777 (375 + 402) |
| Lignes grecques / françaises | 1 400 / 1 407 |
| Vers distincts numérotés | 1 208 (1-1231 ; vv. 23 et 500 supprimés ; autres lacunes = conventions de numérotation, § 12) |
| Répartition des lignes grecques | trimètres 884 ; parties chorales `\chantChoeur` 181 ; anapestes 86 + dimètres 37 + tétramètres 35 ; tétramètres iambiques catalectiques 52 ; trochaïques 31 ; monodie paratragique 40 ; chant d'Agathon 30 ; prose (prière 295-311) 16 ; dochmiaques 4 |
| Locuteurs (lignes) | Mnésiloque 418, Chœur 236, Euripide 229, Mika 123, Coryphée 96, Agathon 80, Archer scythe 71, Clisthène 42, Critylla 35, Serviteur 25, Coryphée-prêtresse 16, Marchande de couronnes 16, Prytane 9 |
| Commentaires | 357 (181 dans le premier fichier, 176 dans le second ; 356 côté grec, 1 côté français) — 335 689 caractères ; médiane 439 ; plus longs : 455-6 (15 449 c.), 101-29 (6 079), 1031 (5 563), 291 (5 500), 1174 (5 395), 643, 738, 556-7, 1059, 839 |
| Notes de commentaire | 541 (130 900 caractères) |
| Apparat | 425 macros, 531 segments (un par vers), 628 entrées, 1 341 leçons ; 529 vers pourvus d'apparat |
| Leçons signées « Bibi » (actives) | 42 (§ 6) |
| Testimonia actifs | 244 (71 côté grec, 173 côté français) ; 175 testimonia désactivés |
| Vers couverts par au moins un commentaire | 854 |
| Didascalies repérées dans la traduction | 60 |
| Macros désactivées (lignes `%`) | 175 testimonia, 79 apparats, 60 commentaires, 145 notes |

## 4. Conspectus siglorum de l'auteur

D'après `Introduction.tex` (« Témoins de la pièce ») et les macros :

| Sigle | Témoin (description de l'auteur) |
|---|---|
| R | *Ravennas*, codex gr. 429 de la Biblioteca Classense, Xᵉ s. — avec R^ac, R^pc, R² (main correctrice), « in mg. », « supra lin. » |
| M | *Monacensis*, codex gr. 492 de la BSB, copie du *Ravennas*, XVᵉ s. |
| PSI-1194 | *PSI* XI 1194 : vv. 145-156 ; 237-245 ; 273-288 ; 594-596 ; 804-809 ; 1231 (et 133-144, *PSI* XIV p. XV), IIᵉ s. |
| POxy-3839 | *P. Oxy.* LVI 3839 : vv. 742-766 (fr. 1) ; 941-953 (fr. 2), *c.* 200 |
| POxy-3840 | *P. Oxy.* LVI 3840 : vv. 1185-1193, IVᵉ s. |
| POxy-4935 | *P. Oxy.* LXXIII 4935 : vv. 1043-1051 (fr. 1) ; 1201-1210 (fr. 2), IIᵉ s. |
| POxy-1176 | *P. Oxy.* IX 1176 (Satyros, *Vie d'Euripide*), fr. 39 col. XII : vv. 335-337 ; 373-375, IIᵉ s. |
| Suid. | *Souda* (éd. Adler), Xᵉ s. |
| Σ | scholies (Σ¹, Σ², Σ^T, Σ^bT…) ; « ed. Iuntina » ; « Divus » (traduction latine) |

Critiques et éditeurs nommés dans l'apparat (attributions, occurrences) : Brunck 49, Bentley 45, Biset 33,
Zanetti 24, Dindorf 23, Scaliger 22, Grynaeus 21 (+ 3 graphies fautives), Hermann 21, Ellebodius 16, Küster 16,
Meineke 13, Fritzsche 13, Bothe 13, Dobree 12, Enger 11, Austin 10, Porson 10, Bergk 9, Willems 8, Burges 8,
Daubuz 8, Faber 8, Elmsley 7, von Velsen 7, Cobet 7, Gelenius 5, Wilamowitz 5, Rogers 5, Blaydes 5,
van Herwerden 5, Boissonade 4, Reiske 4, Bonini 4, Thiersch 4, Sommerstein 4, Casaubon 4, Kaibel 3,
van Leeuwen 3, Reisig 3, puis (≤ 2) Tyrwhitt, Bourdin, Voss, Hirschig, Jackson, Denniston, Valckenaer, Nauck,
Markland, Wecklein, Schöne, Nietzsche, Dover, Toup, Medaglia, Hunt, Kappeyne, Dawes, Bekker, Schaefer, Handley,
Richards, Hamaker, Lobeck, Kaye, Maas, Lenting, Grégoire, Musgrave (écrit « Mugrave »), Olson, Taillardat…
(liste complète par `apparat.tsv`).

## 5. Conjectures signées « Bibi »

*(section en cours de rédaction — liste et justifications)*

## 6. Principes d'établissement du texte

*(section en cours de rédaction)*

## 7. Style et ton du commentaire

*(section en cours de rédaction)*

## 8. Sources les plus citées

*(section en cours de rédaction)*

## 9. Annexes et index

*(section en cours de rédaction)*

## 10. Comparaison des versions

*(section en cours de rédaction)*

## 11. Anomalies relevées

*(section en cours de rédaction)*
