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

### 5.1 Vue d'ensemble

L'apparat de 2023 contient **42 leçons actives signées « Bibi »**, réparties sur 41 segments (vers) de
36 macros `\apparat` (requête : colonne `Bibi` de `apparat.tsv`). Toutes sont imprimées dans le texte
sauf une (v. 1069, proposée mais non adoptée). Par nature :

| Nature | Nombre | Vers |
|---|---:|---|
| Émendations modifiant les lettres du texte | 27 | 50 (×2), 162, 163, 217, 289, 291, 446, 477, 557, 704, 710, 711, 721, 822-3, 839, 895, 910, 1031, 1041, 1071, 1074, 1079, 1091, 1150-1, 1198, 1215 |
| Relecture des mêmes lettres (accent, esprit, coupe, majuscule) | 6 | 30-1, 100, 638, 781, 853, 1078 |
| Vers suppléé (réplique omise par R) | 1 | 1093 |
| Attributions de répliques | 6 | 71-4, 264, 637-40, 642-3, 1090, 1092 |
| Ponctuation | 1 | 1153 |
| Proposition non adoptée dans le texte | 1 | 1069 |

L'instrument est le plus souvent lexicographique : Hésychius fonde ou appuie 10 de ces 42 leçons
(vv. 50, 100, 291, 704, 781, 853, 910, 1041, 1069, 1215), Photius une (710), la Souda une (163), Pollux
une (291) ; les scholies sont invoquées pour 71-4, 711, 1090 ; les « matrices métaphoriques » et
l'article de J. Taillardat pour 704 et 721 ; la langue proverbiale pour 822-3 (αὐτῷ κανῷ) et 895 (πόᾳ
λίθον ἐκβάλλει) ; Willems pour 217 et 710. Neuf de ces leçons (vv. 1069-1093) se concentrent dans la
scène d'Écho, où l'auteur restitue les réponses « moqueuses » (ἐπικοκκάστρια) de la nymphe jouée par
Euripide.

**Contrôle par sondage des gloses citées** (éd. minor d'Hésychius par M. Schmidt, 1867, OCR et image de
la page, via `outils/corpus/chercher.py`) : θάλλικα· σάκκου εἶδος, Μύρμηκος ἀτραπός…, ἑλένη· λαμπάς,
δετή, λαίφια· ῥάκη, τορεῖν· τορῆσαι, τρῆσαι, τεμεῖν, Ὀλυμπία· δοκός, δίκανα· ποικίλα ἱμάτια sont
attestées ; †ἐξαρῆξαι· ἐκφορῆσαι et †ψεφαυγοῦς· σκοτεινῆς sont imprimées sous croix par Schmidt ;
pour π 3188 et σ 2137, Schmidt normalise (πραινοῖ· πρηνίζει. καταστρέφει ; συβίνη) mais son apparat
donne la leçon du manuscrit que cite l'auteur (infinitifs -ειν -ειν ; συμβίνης). Photius η 88 ἥκειν·
ἀντὶ τοῦ ἥκων (éd. Naber, I p. 256) et Apostolius XIV 72 (CPG II p. 620) sont exacts. La numérotation
des gloses (Latte, Hansen–Cunningham) reste à contrôler sur ces éditions.

### 5.2 Liste complète (état 2023), avec la justification de l'auteur résumée

Abréviations : « nov. 2022 » = état de la version de novembre 2022 (et de l'« Index des corrections
proposées », qui reflète cet état) ; « nouv. 2023 » = absente de nov. 2022, présente dès mars 2023.
Les justifications se lisent dans le commentaire du vers indiqué (`commentaires.tsv`).

**Émendations et relectures**

1. **30-1** — Ἀγάθων (bis) R → Ἁγάθων (v. 30, crase) et **ἀγαθῶν** (v. 31 : ἔστιν τις ἀγαθῶν;).
   Jeu sur le nom (*nomen omen*) : pour le rustre Mnésiloque, un « homme de bien » est un gaillard
   hâlé (μῶν ὁ μέλας ὁ καρτερός;). Le v. 32 est rendu en entier à Euripide d'après une scholie et
   une indication de personnage grattée. *(nov. 2022 : ἀγαθῶν; au seul v. 31.)*
2. **50** — πράμος ἡμέτερος R → **πρανοῦν προτέρους** (δρυόχους). πράμος n'est attesté nulle part
   et doit se scander ∪∪ ; πρόμος (Grynaeus) n'explique pas la saillie μῶν βινεῖσθαι; et μέλλει
   attend un infinitif ; Hésychius π 3188 (†πραῖνοι†· πρηνίζειν, καταστρέφειν) atteste un verbe
   πρανόω « jeter en avant », mais aussi « se mettre tête baissée » (d'où la plaisanterie) ; mécoupure
   πρανοῦν → πρανοι ν → πραμος ημ- ; προτέρους d'après la variante ἑτέρας/προτέρας de *Nuées* 562
   (R contre V). *(nov. 2022 : πραῖνοι.)*
3. **100** — μύρμ(ηκος) R → **Μύρμ(ηκος)**, nom propre : Hésychius μ 1904 (sentier de Myrmex au dème
   des Scambonides) ; allusion possible à Philoxène de Cythère, surnommé Μύρμηξ (Souda φ 393).
4. **162** — ἐχύμησαν R → **ἐκεχήνεσαν**. Les trois poètes « pédérastes » portent la ceinture lâche
   (Souda ε 989 : μίτραις… ζώναις) ; χάσκειν + ἁρμονία (*Cav.* 533 τῶν θ' ἁρμονιῶν διαχασκουσῶν),
   double sens de περιχάσκειν (ouvrir une ceinture, Héliodore ap. Oribase) ; iotacisme η/υ, μ/ν,
   haplographie εκεχ → εχ. *(nouv. 2023.)*
5. **163** — διεκίνων R (contre le mètre) → **διέκειντ'**. La Souda glose le mot par περιεπάτουν
   (« vivre de telle façon »), ce qui exclut διεκλῶντ' (Toup) ; διάκειμαι + Ἰωνικῶς = « être enclin
   à la mollesse ionienne ». *(nov. 2022 : δίκανον, d'après Hésychius δ 1805 δίκανα· ποικίλα ἱμάτια.)*
6. **217** — διδόναι γ' αὐτὸν R (contre le mètre) → **διδόναι γ' ἑαυτὸν**, « auctore Willems » :
   Willems (note 4) défendait ἑμαυτόν, sans doute trompé par Dindorf ; διδόναι ἑαυτόν τινι est la
   formule ordinaire (*Cav.* 740, Soph. *Phil.* 84, etc.).
7. **289** — χοῖρον R (Σ : χοιρίον) → **Χοιρίλ'** : la fille de Mnésiloque, première femme
   d'Euripide, s'appelle Χοιρίλη dans la biographie ; refus de l'interprétation obscène au milieu
   d'une prière aux Thesmophores ; confusion Ν/Λ sur un nom propre rare. *(nouv. 2023.)*
8. **291** — πρὸς θάληκον R → **πρὸς θυλάκιον**. Contre Ποσθαλίσκον (Dindorf), avec Willems
   (suffixe -αλισκος non grec, ignoré des lexicographes) ; Hésychius θ 50 θάλλικα· σάκκου εἶδος
   serait une métathèse de θυλάκιον ; Pollux X 152 cite comme des *Thesmophories* σακίον, ἐν οἷσπερ
   τἀργύριον ταμιεύεται (fr. 343 K.-A. selon l'auteur, fr. 328 dans la numérotation que cite LSJ),
   que l'auteur rattache au v. 291 comme glose de θυλάκιον ; idée de la bourse du ménage suggérée
   par J.-V. Vernhes. *(nov. 2022 : πρὸς θάλικα.)*
9. **446** — ἐν Κύπρῳ R → **ἔγκυος** : ni l'interprétation scabreuse (aucun lexique) ni le sens
   littéral (chronologie des expéditions de Chypre) ne tiennent ; aucune scholie ; lieu commun
   pathétique de la veuve enceinte. *(nov. 2022 : ἐγκύμων.)*
10. **477** — πολλ' R (un pied manque) → **πολλά γ'· ἀλλ'** : saut du même au même (ΠΟΛΛΑΓ'ΑΛΛ' →
    ΠΟΛΛ'), contre δεινὰ πολλ' (Bentley) et πολλὰ δείν' (Dawes).
11. **557** — τὸν σῖτον R, Σ, Souda → **τὸν κύσθον**, cf. v. 1114 (σκέψαι τὸ σκύτο → τὸ κύστο,
    Scaliger) : σίφων = πέος (Eur. *Cycl.* 339), d'où σιφωνίζω ; usage détourné du strigile, que
    l'auteur croit illustré par une coupe d'Onésimos (Bâle BS 440) ; métathèse du σ et iotacisme.
12. **638** — χάλᾳ R → **χαλᾷ**, subjonctif délibératif dans la bouche de Mnésiloque (« il défait
    mon strophion ! ») : le iota adscrit est nettement écrit dans R ; χάλα (Grynaeus) supposait un
    ordre de Clisthène (voir n° 38).
13. **704** — ἐξάρξω R (une syllabe manque) → **ἐξαρήξω**. « Briser l'arrogance » serait une image
    unique (Taillardat § 628), « chasser, repousser » un sentiment est courant (αὐθαδίαν αὐθαδίᾳ,
    Antiphane ap. Athénée II 44a ; Eur. fr. 339 Kannicht) ; Hésychius ε 3599 †ἐξαρῆξαι· ἐκφορῆσαι ;
    méthode des « matrices métaphoriques » de Taillardat.
14. **710** — ἥκεις τ' R → **ἥκειν γ'**, après ἥκων γ' de Willems (note 21) : Photius η 88 ἥκειν·
    ἀντὶ τοῦ ἥκων ; simple permutation ν/ς.
15. **711** — οὐ λέξεις R, Souda → **οὐκ ἔξει.** : λέξεις n'a pas de complément ; confusion Κ/Λ ;
    la scholie ἥκεις… ὅθεν οὐ φεύξῃ glose οὐκ ἔξει ; le v. 712 se rattache au v. 713.
16. **721** — ἀθέοις ἔργοις γὰρ R (défaut métrique) → **ξὺν ἀθέοις ἔργοις γὰρ**, « ap. Taillardat,
    cf. v. 716 » : datif d'accompagnement selon l'interprétation de J. Taillardat (résumé dans *REG*
    101, 1988, Actes, p. XVIII-XIX), parallèle de ξὺν ἀδίκοις ἔργοις (v. 716) ; Enger ajoutait ἐπ'.
17. **781** — τὸ ῥῶ R → **τορῶ** : aoriste homérique τορεῖν « percer » (Hésychius τ 1162 τορεῖν·
    τορῆσαι, τρῆσαι, τεμεῖν) ; Mnésiloque grave au couteau son message sur les tablettes de bois ;
    remarque due à J.-V. Vernhes.
18. **822-3** — τἀντίον ὁ κανὼν οἱ καλαθίσκοι / τὸ σκιάδειον R → **ταὐτὸ κανοῦν καὶ τὸ σκιάδειον**.
    Liste hétéroclite dont seuls κανών et σκιάδειον sont repris ensuite, quatre brèves au v. 822 ;
    proverbe αὐτῷ κανῷ (Zénobius II 31 ; Platon com. fr. 15 K.-A. ; Érasme, *Adages* 1088), écho
    de l'αὐτῇ λόγχῃ du v. 826 ; οἱ καλαθίσκοι serait une glose de κανοῦν ; image de procession
    (canéphores, skirophores).
19. **839** — ὦ πόλεις R → **ωὖπολι** (= ὦ Εὔπολι) : hommage à Eupolis, mort selon N. Kyriakidi
    (2007) à Cynossema en 411, peu avant la pièce ; rapprochement avec le commentaire du *Maricas*
    (fr. 192 K.-A.).
20. **853** — Ἑλένη R → **ἑλένην**, nom commun : Hésychius ε 1995 ἑλένη· λαμπάς, δετή ; Critylla
    menace Mnésiloque d'un coup de torche (cf. v. 858).
21. **895** — βαϋζα R → **κόνυζα** (la conyze) : βάϋζε (Zanetti) est inintelligible ; suffixe -υζα
    des noms de plantes ; κ et β semblables ; ψόγῳ mis παρὰ προσδοκίαν pour λίθῳ, d'après le proverbe
    πόᾳ λίθον ἐκβάλλει (Apostolius XIV 72). *(nouv. 2023.)*
22. **910** — ἀφύων R (Σ, Souda : ἰφύων) → **λαιφίων** : Ménélas reconnu à ses haillons (Fritzsche,
    Grégoire : ἀμφίων ; C. Austin, *Dodone* 19.2, 1990) ; Hésychius λ 171 λαίφια· ῥάκη ; chute du λ
    initial, d'où αιφιων lu ἀφύων ou ἰφύων.
23. **1031** — κημὸν ἕστηκ' ἔχουσ' R → **ἕστηκ' ἔχουσα κημόν** (cf. Σ *Vesp.* 674c) : expression
    consacrée du joueur prêt à lancer les dés (fragment d'Hermippe καὶ πρὸς κύβους ἕστηκ' ἔχων <τὸ>
    κήθιον) ; κημός = cornet (Pollux X 150), non urne de vote ; responsion avec les vers précédents ;
    l'auteur s'en remet aux métriciens.
24. **1041** — φεύγουσαν R → **ψεφαυγοῦς** (génitif dorique) : Hésychius ψ 135 ψεφαυγοῦς·
    σκοτεινῆς, glose σκοτεινήν égarée au v. 1054 ; goût d'Euripide pour les composés en -αυγής ;
    chute de ψε- et finale -αν analogique de λιτομέναν ; contre χέουσα (Rau) et φλέγουσαν (Musgrave).
25. **1071** — μέρος ἐξέλαχον; R → **μόρος ἔξελ' ἄχος.** : réponse d'Écho (« la Mort ôte la
    douleur ») ; cf. Soph. fr. 698 Radt.
26. **1074** — στωμυλωμένη R (στωμυλλωμένη au v. 1073) → **στωμυλιομενής** : la différence
    d'orthographe λλ/λ dans R serait l'indice d'un mot différent ; composé sur le modèle de
    στωμυλιοσυλλεκτάδης (*Gren.* 839).
27. **1078** — (Εὐρ.) παῦσαι R → **'παΰσαι** (ἐπαΰω, Eschyle, *Choéph.* 828) : Écho « crie dessus ».
28. **1079** — βάλλ' ἐς κόρακας R → **βάλλε σύ κόρακας** : κόρακες = crochets, marteaux (Pollux X
    22) ; même jeu supposé en *Nuées* 133.
29. **1091** — πλησίον αὕτη R → **πλήξασ' αὕτη** : Écho-Euripide frappe l'archer, d'où sa fureur
    (ποῦ 'στ' ἠ μιαρά;).
30. **1150-1** — (οὐ) θεμιτὸν R → **θεμιτεύετον** (duel) : Eur. *Bacch.* 79 ὄργια… θεμιτεύων ;
    haplographie ; responsion avec le v. 1158.
31. **1198** — κ⟦ω⟧ομίζεις αὐτοῖς Rᵖᶜ → (Τοξ.) **κομίζι σ' αὐτίκ'** (= κομίζω σοι αὐτίκα) : l'archer
    ira chercher la drachme ; confusion ις/κ ; les sigles de personnages en marge (γϋ.) sont tardifs
    (main d'Euphrosynus Boninus selon von Velsen).
32. **1215** — συβήνη R → **συμβήνη**, cf. v. 1197 (où R a συμβήνην, conservé contre tous les
    éditeurs) et Hésychius σ 2137 (συμβίνης· καπροβόλον, ἐμβόλιον) : une lance, non un carquois ou
    un étui à flûte ; jeu de mots avec καταβηνῆσι.

**Vers suppléé, proposition non adoptée, ponctuation**

33. **1093** — réplique omise par R : **(Εὐρ.) ποῖ ποῖ πέτει** suppléée (cri d'oiseau d'Écho qui
    s'envole sur la μηχανή ; cf. *Oiseaux* 226, 310, 1199).
34. **1069** — δι' Ὀλύμπου R (conservé dans le texte) ; proposé : †δι'† **ὀλυμπίας**, d'après
    Hésychius ο 649 (Ὀλυμπία· δοκός : « poutre » = pendaison), autre réplique moqueuse d'Écho.
35. **1153** — λαμπάσι R → **λαμπάσι.** : ponctuation forte, liée à la structure strophique proposée
    pour 1136-1159 (deux paires strophe/antistrophe séparées par des mésodes : 1143-4 et 1154).

**Attributions de répliques**

36. **71-4** — R : Mnésiloque 71, Euripide 72-4 → **Mnésiloque 71-4** : pendant exact du quatrain
    1-4 (invocation à Zeus puis question) ; la scholie τὸ σημεῖον· οὐ μόνον κηδεστὴς ὁ ἐκδιδούς, ἀλλὰ
    καὶ ὁ λαμβάνων montrerait que le signe ne marque pas de changement de locuteur.
37. **264** — R sans changement d'interlocuteur → **(Ἀγάθ.) ἀλλ'…** : Agathon, excédé par la pique
    σὺ τοῦτο γίγνωσκ', se fait rentrer par l'eccyclème (commentaire du v. 263). *(nouv. 2023.)*
38. **637-40** — R : Mnésiloque sans autre signe → **Mnésiloque 637-8, Mika 639-40** (contre Brunck
    et la vulgate : Clisthène 638, la femme 639-40) : un seul paragraphos à rétablir ; Clisthène est
    déjà en train de déshabiller Mnésiloque sur l'ordre de Mika (v. 636).
39. **642-3** — R : Mnésiloque 641-3 → **Clisthène 642-3** (un changement au lieu de deux). *(nouv.
    2023.)*
40. **1090** et 41. **1092** — (Μνη.) chez la plupart des éditeurs → **(Χορ.)**, d'après la scholie
    τοῦτο ὁ χορὸς ἢ ὁ γέρων : Mnésiloque ne dénoncerait pas son complice.

(Le 42ᵉ élément est la seconde leçon du v. 50, προτέρους, comptée à part dans l'apparat.)

### 5.3 Conjectures abandonnées ou désactivées

| Vers | Conjecture | Statut |
|---|---|---|
| 1 | Χελιδὼν (nom propre, « ap. Clements ») | active en nov. 2022 ; supprimée dès mars 2023 (la note sur l'article d'A. Clements a disparu) |
| 702 | διπλὰ (pour ἔργα R) | active en nov. 2022 ; commentée (`%`) dès mars 2023 ; le texte imprime †πλέα† (Souda) |
| post 870 | < οἶσθ' οὖν ὃ δρᾶσον; > restitué « ap. Σ » (cf. Eur. *Hél.* 325) | active en nov. 2022 ; désactivée ensuite |
| 1072 | θαλάττης τέμνον (pour θανάτου τλήμων) | désactivée dans toutes les versions |
| 1082 | ὀλόφυγ' (pour ὀτότυζ') | désactivée dans toutes les versions |
| Eur. fr. 228 Kannicht | καλλήϊον Γαιᾶ (pour κάλλιστον ἐκ γαίας) | active dans le commentaire de 855-7 en nov. 2022 ; commentée (`%`) dès mars 2023 |
| 50, 163, 291, 446 | πραῖνοι, δίκανον, πρὸς θάλικα, ἐγκύμων | remplacées en 2023 par πρανοῦν, διέκειντ', θυλάκιον, ἔγκυος |

### 5.4 Conjectures sur d'autres textes (Index des corrections proposées)

Présentes dans le commentaire de 2023 : *Cav.* 20 ἀπόκυνον (codd. ἀπόκινον ; Hésychius α 6416 ; comm.
455-6) ; *Gren.* 19-20 οὐ κε ῥεῖ (codd. οὐκ ἐρεῖ ; comm. 647-8) ; Diogénien IV 78 ταὐτότητι (comm. 489) ;
Eustathe, *Il.* 976.13 σφῇσιν (comm. 643) ; Hipponax fr. 30 Masson / 42 Degani οὔ μοι δίκᾳ ὡς μοιχός
(comm. 894) ; Sappho fr. 125 Voigt αὐτὰ κόραις στεφαναπλόκεο (comm. 400-1) ; Σ *Thesm.* 1174 τὸ ἄκρως
βαδίζειν « ap. Zonaras » (comm. 1174) ; Eupolis fr. 192.96 K.-A. (commentaire du *Maricas* sur
papyrus ; rangé par erreur sous Aristophane dans l'Index) ἄ[ργυρον (comm. 839) ; *Lys.* 104 et 114 attribués à la même femme (comm. 643) ; *Thesm.* 743,
répartition des répliques d'après P. Oxy. 3839 (τρικότυλον; ἢ πῶς. — εἰπέ μοι· τί μ' ἠργάσω;).

L'Index (fichier `Index.tex`) reflète l'état de novembre 2022 : il ignore les leçons nouvelles de 2023
(vv. 100, 162, 264, 289, 477, 642-3, 895, 1090-1092, 1153, 1198) et donne encore πραῖνοι, δίκανον,
θάλικα, ἐγκύμων, διπλὰ et Χελιδών.

## 6. Principes d'établissement du texte

Les principes ne sont exposés nulle part de façon suivie (l'Introduction ne contient ni *praefatio* ni
note sur l'édition) ; ils se déduisent de la page de titre, de l'apparat et des déclarations éparses
du commentaire.

**1. Un « Urtext » reconstruit à partir de R.** La page de titre annonce « Les *Thesmophories*
d'Aristophane. *Urtext* avec commentaire, traduction, apparats (critique & témoins) ». Le mot revient
dans le commentaire (vv. 80, 822-3 : « l'*Urtext* — comportait certainement au vers 822 le terme
κανοῦν ») et dans l'Index des gloses d'Hésychius « qui ont servi au rétablissement de l'*Urtext* ».
R est « notre unique source pour la version complète » ; M (Monacensis gr. 492) est traité comme une
copie de R, utile pour ses corrections (64 mentions, 35 leçons retenues) ; les papyrus (PSI 1194,
P. Oxy. 3839, 3840, 4935, 1176) apparaissent 23 fois ; la tradition indirecte est très présente (Souda
89 mentions, scholies 53, Hésychius et Photius 11).

**2. Un apparat positif, un segment par vers.** Forme constante : leçon de R, deux-points, leçon
retenue en gras (`\lecon`) suivie de son autorité, autres conjectures. Sur 628 entrées, 584 marquent
une leçon retenue : 350 adoptent la correction d'un critique nommé (Brunck 34, Bentley 34, Biset 26,
Dindorf 19, Zanetti 19, Scaliger 17, Grynaeus 15, Küster 15, Ellebodius 12, Meineke 9…, soit surtout
les éditions de la Renaissance et la critique des XVIIIᵉ-XIXᵉ s.), 106 conservent R contre une ou
plusieurs conjectures citées, 52 suivent la tradition indirecte ou un papyrus, 35 M, 41 « Bibi » ; 44
entrées sont purement descriptives (corrections de R, ajouts marginaux, sigles de personnages). Les
attributions fines aux premières éditions (Zanetti, Grynaeus, Gelenius, Divus…) supposent un appui sur
les apparats modernes (Prato, Austin–Olson, Wilson), que l'auteur ne cite pas comme tels.

**3. Conservatisme revendiqué, conjecture assumée.** Les modèles sont Willems, « en guerre perpétuelle
contre les retoucheurs de texte », et Coulon, qui « s'est astreint à conserver le plus possible les
leçons des manuscrits contre les conjectures des philologues ». L'auteur défend R contre la vulgate
quand il le peut (v. 18 ἀκοὴν δὲ χοάνης avec Willems ; v. 638 χάλᾳ, « le iota adscrit est nettement
écrit » ; v. 1197 συμβήνην, « nous nous garderons bien de biffer le μ ») et raille les corrections qui
laissent le texte aussi obscur. Mais quand R lui paraît corrompu, il conjecture hardiment, en
s'imposant trois exigences : (a) la correction doit expliquer la faute (iotacisme, confusions μ/ν, κ/β,
Κ/Λ, Ν/Λ, ις/κ, haplographie, saut du même au même, métathèse, mécoupure, glose entrée dans le texte) ;
(b) elle doit être appuyée par un témoin ancien, de préférence une glose d'Hésychius ou une scholie
mal comprise ; (c) elle doit restituer un sens comique ou une image attestée. Il écarte pour cette
raison les corrections « banales » qui n'expliquent pas l'erreur (v. 1041 : χέουσα « est le mot banal
qu'on attendait, il paraît alors très difficile qu'un scribe s'y soit trompé »). Il signale souvent la
part d'hypothèse (v. 291 « pour séduisante que soit cette reconstruction, elle n'en demeure pas moins
conjecturale » ; v. 1031 « je laisse le soin d'en juger à des métriciens compétents » ; v. 1069 « je
m'arrête ici, au bord de la reconstruction tentatrice »).

**4. Le sens comique et la « décence » d'Aristophane comme critères.** Les interprétations obscènes
jugées gratuites sont rejetées avec véhémence (vv. 263, 289, 446, 910, 1197-1216 ; formule récurrente,
placée sous l'autorité de Willems : « Mais pour qui prennent-ils Aristophane ? »), ce qui oriente certaines émendations
(289 Χοιρίλ', 446 ἔγκυος) ; à l'inverse, une obscénité jugée démontrée est introduite (557 κύσθον).

**5. Répartition des répliques.** L'auteur part des signes de R, dont il donne une typologie
(paragraphos en début de vers, dicolon ou abréviation du nom en milieu de vers ; note au v. 637-40) et
s'efforce de « respecter le découpage des vers du manuscrit de Ravenne, sans tailler ni fusionner » (v.
255) ; les noms de personnages ajoutés tardivement en marge sont récusés (v. 1198 : main du XVIᵉ s.) ;
les arguments sont le caractère des personnages, le jeu de scène et les scholies (6 attributions
« Bibi », § 5). Écho est attribuée à Euripide (« Euripide — qui joue dans ce passage la nymphe Écho »),
d'où l'absence de personnage Ἠχώ dans l'extraction.

**6. Métrique et colométrie.** Chaque côlon des parties lyriques forme un groupe pourvu d'une étiquette
métrique (`\typeVers`, 288 étiquettes). La métrique sert d'argument (vv. 217, 477, 704, 721, 1031,
1150-1), mais l'auteur s'en remet aux métriciens (L. P. E. Parker, qu'il appelle « Lætitia », Prato,
Dale, White) et refuse de forcer la responsion (1136-1159).

**7. Signes critiques dans le texte.** 30 lignes portent des croix (†), dont 18 dans la scène d'Écho
(1069-1096) : l'auteur y marque comme corrompues les « répétitions » d'Écho, qu'il suppose avoir été à
l'origine des déformations moqueuses. Une lacune est notée avec son schéma métrique (v. 994 : < × ∪∪ ∪ >,
« lacunam statuit Hermann ») ; une glose est mise entre accolades (v. 828 { ἐν ταῖς στρατιαῖς }, sans
note d'apparat) ; deux vers sont supprimés et exclus du texte numéroté (v. 23, del. Willems ; v. 500,
del. van Herwerden) ; deux répliques sont suppléées (v. 1093, Bibi ; v. 1094 οὐ καιρήσεις, Brunck ap. Σ).

**8. Numérotation.** Celle de la vulgate (Hall–Geldart), avec des écarts locaux dans les parties
lyriques, où l'auteur numérote d'après sa propre colométrie au moyen de `\ligne{n}` (§ 2.3 et § 11).

## 7. Style et ton du commentaire

### 7.1 Les deux axes revendiqués

L'Introduction (partie « Parémiographie ») le dit en toutes lettres : « Mon commentaire possède deux
principaux mérites : celui d'avoir dépouillé Hésychius à chaque difficulté et de recourir massivement
— et même parfois abusivement — à ce qu'il nous est parvenu de la langue proverbiale grecque ». Une
note signale elle-même le risque de cercle (justifier un vers par un proverbe que les parémiographes ont
tiré… de ce vers, ex. v. 702), et l'auteur recourt au latin comme « langue voisine » pour identifier
images et proverbes (v. 19 : *nec aures me credo habere nec tango*). Le dépouillement se mesure :

| Axe | Indicateurs (Harmattan 2023) |
|---|---|
| Hésychius | cité dans 41 articles (74 occurrences dans le commentaire et ses notes, 49 références « lettre + numéro », 46 gloses distinctes), 73 fois dans les testimonia ; 10 des 42 leçons « Bibi » reposent sur lui (§ 5) ; Index des gloses d'Hésychius : 18 entrées ; « le plus utile des lexicographes pour les *Thesmophories* », « ce bon vieil Hésychius ne nous ayant jamais trahi » |
| Langue proverbiale | « proverbe/proverbial » dans 29 articles (94 occurrences, pour moitié dans les notes) ; Érasme, *Adages*, dans 21 articles (41 occurrences, presque toutes en note) ; parémiographes (Zénobius 8 articles, Apostolius 8, Diogénien 4, Macarius 2, *Corpus Paroemiographorum* 6) ; Tosi 7 ; Index des allusions proverbiales : 38 entrées ; 106 passages latins balisés `\latin` |
| Images | J. Taillardat, *Les images d'Aristophane*, dans 44 articles (61 occurrences) ; méthode des « matrices métaphoriques » appliquée à l'établissement du texte (vv. 704, 1069) |
| Modèle | Alphonse Willems dans 89 articles (126 occurrences, plus 8 dans l'apparat) : « Lisez Willems ! aucune excuse » ; ses notes sur les *Thesmophories* sont reproduites en annexe et la traduction française de l'auteur est, selon l'Annexe, « la quasi-intégralité » celle de Willems retouchée |

### 7.2 Forme

357 articles (moyenne 940 caractères, médiane 439 ; 49 dépassent 2 000 caractères, 98 en ont moins de
200 ; le plus long, 455-6, « Dossier sur la mère d'Euripide, la vendeuse d'herbes », atteint 15 449
caractères hors notes et traite aussi du scandix et de *Cav.* 19-20), dont 176
pourvus de notes (541 notes numérotées par article, appelées par `\marqueur`). 344 citations en bloc
(`\citComm`), le grec presque toujours suivi d'une traduction française ; 13,7 % des lettres du
commentaire sont grecques. Un article type : lemme grec ; énoncé du problème (« Le vers pèche contre le
mètre », « La répartition des répliques de ce passage fluctue d'une édition à l'autre ») ; revue des
corrections antérieures ; témoin décisif (glose d'Hésychius, scholie mal comprise, proverbe) ;
explication paléographique ; texte restitué et traduit ; souvent reconstitution du jeu de scène ;
pointe finale.

### 7.3 Voix et ton

- **Énonciation.** Alternance du « je » (≈ 200 occurrences) et du « nous » d'auteur (≈ 250, plus
  ≈ 145 « notre/nos ») ; une fois « je [Bibi] » et « N.D.É. » (note 3 au v. 721-5) ; 28 adresses au
  « lecteur ». Ton oral : 210 points d'exclamation, 205 points d'interrogation, 195 points de
  suspension.
- **Érudition enjouée.** Jeux de mots français (le coureur « dé-raté », v. 3 ; « (Re-)prends ton habit
  Grégoire ! », v. 910), pastiches de comptines et de chansons (v. 557), Brassens, La Fontaine,
  Molière, Villon, Rabelais ; anecdotes contemporaines (Félix Faure, v. 446 ; la « carte de crédit »
  de J.-V. Vernhes, v. 291) ; hommages appuyés (« l'immense Jean Taillardat », « le grand Alphonse
  Willems »).
- **Polémique.** Vive hostilité aux « modernes scholiastes » qui voient partout l'obscénité et à
  plusieurs commentateurs récents (Austin–Olson, Henderson, un auteur désigné par un sobriquet au v.
  910), avec un vocabulaire d'invective concentré dans quelques articles (vv. 263, 455-6, 738, 910,
  1063, 1197-1216) ; le scholiaste byzantin, « ignare », est opposé à « l'alexandrin » Hésychius.
- **Digressions personnelles.** Remarques politiques ou d'actualité (v. 1031 sur la démocratie, v.
  637-40 sur « l'administration française » ; dans l'Annexe polémique, une injure visant un chef d'État).

Pour une édition de référence « beaucoup plus sobre », c'est la part la plus à reprendre : conserver
les arguments, la documentation et les trouvailles, éliminer l'invective, les attaques *ad hominem* et
les digressions d'actualité, et unifier la voix (« je », conformément aux consignes).

## 8. Sources les plus citées

Comptes produits par `outils/extraction/sources_citees.py` → `edition/donnees/travaux_anterieurs/sources_citees.tsv`
(96 sources ; nombre d'articles de commentaire où la source apparaît, notes comprises, et occurrences
dans le commentaire, les notes, les testimonia et l'apparat ; motifs simples, à lire comme des ordres de
grandeur).

| Source | Articles | Occurrences (comm. + notes / testimonia / apparat) |
|---|---:|---|
| Scholies, scholiaste | 108 | 181 / 19 / 46 |
| Euripide (auteur et personnage) | 107 | 267 / 3 / 0 |
| Willems | 89 | 126 / 0 / 8 |
| Taillardat, *Images d'Aristophane* | 44 | 61 / 0 / 1 |
| Hésychius | 41 | 74 / 73 / 7 |
| Souda | 37 | 67 / 140 / 89 |
| Autres pièces d'Aristophane | *Gren.* 35, *Guêpes* 34, *Ach.* 29, *Nuées* 29, *Lys.* 25, *Paix* 23, *Ois.* 22, *Cav.* 19, *Ploutos* 13, *Assemblée* 11 | — |
| Kassel–Austin (*PCG*) | 30 | 35 / 3 / 0 |
| « proverbe », « proverbial » | 29 | 93 / 1 / 0 |
| Athénée | 26 | 38 / 1 / 0 |
| Platon | 23 | 30 / 0 / 0 |
| Homère | 22 | 43 / 0 / 0 |
| Érasme, *Adages* | 21 | 41 / 0 / 0 |
| Photius | 20 | 26 / 47 / 4 |
| Jouan–van Looy (fragments d'Euripide, CUF) | 18 | 22 / 0 / 0 |
| Sophocle | 18 | 20 / 0 / 0 |
| Kannicht (*TrGF* V) | 17 | 19 / 2 / 0 |
| Eschyle | 17 | 31 / 0 / 0 |
| Thucydide | 16 | 25 / 0 / 0 |
| Fritzsche | 14 | 16 / 0 / 13 |
| Plutarque | 14 | 17 / 0 / 0 |
| Pollux | 11 | 17 / 21 / 5 |
| Parker (« Lætitia »), LSJ | 11 chacun | 17 ; 12 |

Les éditions modernes de la pièce sont peu citées dans le commentaire (Austin–Olson 6 articles,
Prato 6, Sommerstein 5, Coulon 4, Rogers 3, van Leeuwen 5, Enger 4, von Velsen 7), sinon pour être
contredites ; les instruments de travail le sont un peu plus (Daremberg–Saglio 10, Chantraine 9,
Radt 9, Bailly 5). Dans les testimonia, la tradition lexicographique domine : Souda (140 occurrences),
Hésychius (73), Photius (47), Eustathe (29), Pollux (21), Moeris (20), Zonaras (18), *Synagoge* et
*Etymologica* (11 chacun), Aelius Dionysius et Phrynichus (10 chacun).

## 9. Introduction, annexes et index

### 9.1 Introduction (`Introduction.tex`, 421 lignes)

Date (Grandes Dionysies de 410, avec Rogers ; critique interne privilégiée sur les scholies) ;
synopsis (le procès d'Euripide, le contexte historique) ; « Bibliographie thématique (et sélective) à
l'usage de l'apprenti-chercheur » : éditions (Juntine 1516, Fritzsche 1838, Willems 1919, fac-similé
de van Leeuwen 1904, Rogers 1904, Coulon 1928, Sommerstein 1994, Prato 2001, Austin–Olson 2004/2008,
Wilson 2007, Saetta Cottone 2016), scholies (Dübner ; Koster, Regtuit 2007), lexicographie (Hésychius
de Latte–Cunningham et de Schmidt, Souda d'Adler, Photius de Theodoridis, *Synagoge* de Cunningham,
Pollux de Bethe), parémiographie (CPG de Leutsch–Schneidewin, Gaisford, Tosi, Érasme éd. Saladin,
Taillardat ; c'est là que figurent les « deux principaux mérites » cités au § 7.1), outils (Logeion,
Perseus, TLG, Courtaud–Diverneresse) et encyclopédies (Daremberg–Saglio, *RE*) ; « Le dossier
Mnésiloque » (identification du Parent avec Mnésiloque, beau-père d'Euripide : Téléclide fr. 40 K.-A.,
usage onomastique attesté par Démosthène, *Vies* d'Euripide) ; « Témoins de la pièce » (§ 4) ; liste des
personnages (avec les muets Μανία, Ἐλάφιον, Τερηδών). Les jugements sur les éditeurs y sont
tranchés (la traduction de Van Daele dans la CUF serait celle de Willems retouchée ; la « conspiration
du silence » autour de Willems).

### 9.2 Annexes (`Annexes.tex`, 1 869 lignes)

Préambule : « La quasi-intégralité de la traduction proposée des *Thesmophories* ainsi que les notes qui
composent ces annexes sont tirées de l'œuvre d'Alphonse Willems ».

| Ensemble | Contenu | Taille (caractères actifs) |
|---|---|---:|
| Dossier Willems | notice par Maurice Leroy ; bibliographie de Willems (Leroy) ; « Alphonse Willems. Notes d'un vieil élève » (Charles Lacomblé) | ≈ 66 000 |
| Notes de Willems sur les *Thesmophories* (*Bull. Acad. roy. de Belgique*, Classe des lettres, nov. 1908) | introduction et **28 notes** : vv. 16-18, 21, 22-24, 217, 230, 263, 280-281, 289-291, 352-354, 365-367, 400-401, 418-420, 499-501, 509-510, 531-532, 569, 575-576, 592-593, chœur 655-686, 656, 710-712, 773-774, 808-809, 811-812, 1019-1020, 1050-1051, 1052-1055, 1181 | ≈ 87 000 |
| Autres textes de Willems | introduction aux notes sur la *Paix* (1899) ; note sur *Nuées* 83 ; « Le nu dans la Comédie ancienne des Grecs » (1901) ; note sur *Guêpes* 1341 | ≈ 60 000 |
| Papyrus | PSI 1194, P. Oxy. 3839, 4935, 3840 : photographies et pages d'édition (figures), insérées à la place de leurs vers | ≈ 3 100 |
| Iconographie | coupe d'Onésimos (Bâle BS 440, d'après Boardman ; cf. v. 557), ἔγκυκλον à franges pourpres, crocote transparente, cratère de Würzburg (égorgement de l'outre, vv. 754-757) | ≈ 1 400 |
| Polémique | « Un commentaire du commentaire et son droit de réponse (ou la *Passion de Philologus*) » : les « Impressions » d'un lecteur (avril 2021) sur les « Nouvelles notes thesmophoriennes » que l'auteur avait publiées dans ὁ λύχνος (*Connaissance hellénique*), n° 158 (mars 2021), et la saynète satirique de l'auteur en réponse (personnages : Philologus, Bibi, Pluton, le fantôme d'Aristophane, chœur sur la *Passion selon saint Matthieu*) | ≈ 39 000 |

Les notes de Willems sont celles auxquelles renvoie le commentaire (« note 4 », « 21ᵉ note », etc.) ;
deux des leçons « Bibi » en dérivent directement (vv. 217, 710).

### 9.3 Index (`Index.tex`, 441 lignes)

Quatre index actifs, renvoyant au commentaire par plage de vers (« 49-50 n. 2 ») ; un « Index des
auteurs cités » et un « Index général » sont commentés (ébauches vides).

| Index | Entrées | Remarque |
|---|---:|---|
| Allusions proverbiales | 38 | 30 pour les *Thesmophories*, 8 pour d'autres pièces ; renvoi liminaire à la liste des proverbes de Platon dressée par Jowett |
| Gloses d'Hésychius utiles pour l'établissement et la compréhension du texte | 18 | 14 pour les *Thesmophories*, 1 *Cav.*, 1 *Ois.*, 2 Eur. fr. 228 |
| Corrections proposées | 41 | état de novembre 2022 (voir § 5.3-5.4) |
| Passages davantage explicités | 60 | dont les grands dossiers (chant d'Agathon, monodie d'Andromède, chant ibycéen 1136-59, 1197-1216) |

## 10. Comparaison des versions

*(section en cours de rédaction)*

## 11. Anomalies relevées

*(section en cours de rédaction)*
