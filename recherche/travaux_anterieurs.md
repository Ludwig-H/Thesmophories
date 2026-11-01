# Travaux antérieurs de l'auteur (dossier `latex/`) — analyse et extraction

> État : **complet** (3ᵉ reprise, 2026-10-26 ; § 9-10 réécrits le 2026-11-01 sur tous les états du Drive). Sections 1-11
> rédigées ; chiffres recalculés sur la dernière extraction (reproductible à l'identique : `python3
> outils/extraction/extraire_travaux.py && python3 outils/extraction/comparer_versions.py`, contrôle :
> `python3 outils/extraction/verifier_recuperables.py`).
> Sources : `latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `… vv 642-fin-bis.tex` (version de
> référence, dite ici « Harmattan 2023 ») ; pour les § 9-10, les 54 états de travail du Drive (juillet 2020 - avril 2024,
> printemps 2020 compris) et les `Introduction`, `Annexes` et `Index` du Drive, plus complets que leurs copies de `latex/`.
> Les fichiers « Edition 4 pages Ravennas » (Gemini) sont exclus. Les citations du commentaire de l'auteur sont données
> ici à titre d'analyse ; le nom réel de l'auteur (présent dans `\author{}` et dans les annexes) n'est jamais reproduit.

## 1. Architecture des fichiers et des macros

### 1.1 Fichiers

| Fichier | Lignes | Contenu |
|---|---:|---|
| `Harmattan 2023 vv 1-641.tex` | 6 886 | vv. 1-638 (le dernier groupe est 637-8, malgré le nom) |
| `Harmattan 2023 vv 642-fin-bis.tex` | 7 729 | vv. 639-1231 (`\setcounter{page}{151}`) |
| `Harmattan mars 2023.tex` | 10 307 | copie tronquée au v. 946 (541 groupes) ; la version complète est sur le Drive (§ 10.1) |
| `nov 2022.tex` | 13 092 | pièce entière (773 groupes) ; antérieure à la version du Drive (§ 10.1) |
| `Introduction.tex` | 421 | date, synopsis, bibliographie commentée, dossier Mnésiloque, témoins (sigles), personnages ; Drive : 435 lignes (§ 9) |
| `Annexes.tex` | 1 869 | Willems (notice, bibliographie, 28 notes sur les *Thesmophories*), papyrus, iconographie, polémique ; Drive : 2 036 lignes (§ 9) |
| `Index.tex` | 441 | quatre index (allusions proverbiales, gloses d'Hésychius, corrections proposées, passages expliqués) ; Drive : 453 lignes (§ 9) |

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
| Numérotation | `\ligne{n}` = `\setline{n}\hidenumbering`, `\passeLigne` = `\skipnumbering`, `\fin` (rejet : saut de ligne non compté + `[`), `\linenumberlist{…}` (numéros imprimés) | voir § 2.3 |
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
- `outils/extraction/comparer_versions.py` : extraction de tous les états du Drive et de `latex/` avec le même
  analyseur, doublons écartés par empreinte, comparaison avec Harmattan 2023 (chaque élément ancien reçoit un
  statut : conservé, remanié, désactivé, déplacé, disparu… ; les parties commentées `%` sont prises en compte),
  lignées des contenus perdus, Introduction, Annexes et Index du Drive (§ 9-10).
- `outils/extraction/verifier_recuperables.py` : contrôle de `contenus_recuperables.tsv` sur les fichiers sources (§ 10.2).
- `outils/extraction/sources_citees.py` : comptage des sources citées (§ 8).

Commande : `python3 outils/extraction/extraire_travaux.py` (≈ 15 s), `python3 outils/extraction/comparer_versions.py`
(≈ 3 min ; il lit le Drive dans `.sources/`, puis `python3 outils/extraction/sources_citees.py`). Les sorties sont identiques
octet pour octet d'une exécution à l'autre (contrôlé). Le nom réel de l'auteur est lu dans `\author{}` et masqué dans toutes
les sorties (contrôle bloquant).

### 2.2 Sorties (`edition/donnees/travaux_anterieurs/`)

| Fichier | Contenu |
|---|---|
| `thesmo.json` | 777 groupes : ordre, étiquette `%% v.`, vers couverts, personnages, types de vers et mètres, en-têtes, strophes, lignes grecques (vers, partie, texte brut et LaTeX, n° reledmac, méthode d'attribution, vers HG), apparat (brut, découpé par vers, entrées, leçons, leçon retenue), testimonia, commentaires (plage, lemme, LaTeX, texte, appels `\marqueur`, notes rattachées avec numéro), parties commentées (`%`) internes aux commentaires, notes, apparats et testimonia (`desactive_interne`), notes orphelines, macros désactivées ; côté français : lignes par vers, didascalies, testimonia ; + `statistiques` (dont répartition par type de vers et par personnage) et `anomalies` |
| `texte_grec.tsv` | une ligne par vers ou partie de vers : `vers, partie, vers_fin, personnage, texte, groupe, type, metre, n_reledmac, vers_HG, methode_vers, fichier, ligne_source` |
| `traduction.tsv` | idem pour la traduction (`didascalies`, méthode d'appariement) |
| `apparat.tsv` | une ligne par segment d'apparat (vers) : texte, leçon(s) retenue(s), drapeau `Bibi`, LaTeX |
| `commentaires.tsv` | `id, plage, lemme, longueur, premier_vers, dernier_vers, notes, groupe, cote, fichier, ligne_source` |
| `testimonia.tsv` | testimonia actifs et désactivés, des deux côtés |
| `anomalies.tsv` | rapport de vérification (§ 11) |
| `comparaison_versions.json/.tsv` | comparaison de tous les états (§ 10) |
| `contenus_recuperables.tsv` | contenus absents de la version active de 2023 : version, fichier, ligne, type, vers, extrait, statut (§ 10.4) |

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
   La numérotation de l'auteur est celle de l'usage moderne : contrôle sur l'OCT de N. G. Wilson (2007, scan
   local, numéros seulement) aux repères 372-380, 724-726, 1015-1019, 1025-1030, 1080, 1085-1090, 1135-1145,
   1155 et 1160, où l'auteur et Wilson concordent alors que HG s'en écarte le plus souvent ; seuls les
   vv. 1081-1084 font difficulté (§ 11.1-11.2) ;
5. **contrôle les renvois internes** : la leçon de chaque segment d'apparat bref doit se lire dans la ligne
   du vers indiqué (399 segments vérifiés, 397 concordants, 2 décalés) et le lemme de chaque commentaire bref
   dans une ligne de sa plage ou dans l'apparat de ces vers (223 commentaires vérifiés, 219 concordants,
   4 décalés) : `statistiques.controle_apparat_numerotation` et `controle_commentaires_numerotation`.

Résultat : 1 400 lignes grecques numérotées, 1 208 numéros de vers distincts de 1 à 1231 ; 6 étiquettes de
groupe seulement (sur 777) restent en désaccord avec le numéro attribué, toutes des étiquettes périmées
(copiées d'un groupe voisin ou non mises à jour après un changement de répartition).

### 2.4 Alignement grec / français

Appariement groupe à groupe (777/777) puis ligne à ligne : identité du nombre de lignes dans 764 groupes ;
pour les 13 autres, alignement par programmation dynamique sur les longueurs (fusions 2:1, 1:2, 3:1 ;
didascalie isolée rattachée au vers précédent). Méthode tracée dans `traduction.tsv` (`methode_vers`).
Cas particulier : aux vv. 3-4, le grec est imprimé dans l'ordre 4-3 (§ 11.1) alors que la traduction suit
l'ordre usuel ; l'appariement se fait sur l'ordre usuel (« Y a-t-il moyen, avant que perdre tout de bon la
rate » = v. 3, οἷόν τε…), ce que signale `methode_vers`. Contrôle global : les 1 400 lignes grecques et
les 1 407 lignes françaises sont toutes rattachées à un vers ; chaque vers grec a sa traduction (quatre
lignes françaises valent deux vers : 59-60, 295-296, 309-310, 836-837) ; tout groupe pourvu d'un nom de
personnage côté grec l'a aussi côté français, sauf deux (vv. 663-666, § 11.1).

## 3. Statistiques (Harmattan 2023)

| Élément | Nombre |
|---|---:|
| Groupes (de chaque côté) | 777 (375 + 402) |
| Lignes grecques / françaises | 1 400 / 1 407 |
| Vers distincts numérotés | 1 208 (1-1231) ; 1 220 numéros couverts (lignes valant deux numéros comprises) ; 11 numéros absents : vv. 23 et 500 supprimés, 9 sauts de numérotation (conventions, sauf 1082 : § 11.1-11.2) |
| Répartition des lignes grecques | trimètres 884 (+ 1 catalectique) ; parties chorales `\chantChoeur` 181 (+ 1 saisie par erreur avec `\chantChoeurFr`, v. 330) ; anapestes 86 + dimètres 37 + tétramètres 35 ; tétramètres iambiques catalectiques 52 (+ 2 acatalectes) ; trochaïques 31 ; monodie paratragique 40 ; chant d'Agathon 30 ; prose (prière 295-311) 16 ; dochmiaques 4 |
| Locuteurs (lignes) | Mnésiloque 418, Chœur 236, Euripide 229 (Écho comprise), Mika 123, Coryphée 96, Agathon 80, Archer scythe 71, Clisthène 42, Critylla 35, Serviteur 25, Coryphée-prêtresse 16, Marchande de couronnes 16, Prytane 9, second Coryphée 4 |
| Commentaires | 357 (181 dans le premier fichier, 176 dans le second ; 356 côté grec, 1 côté français) — 335 689 caractères ; médiane 439 ; plus longs : 455-6 (15 449 c.), 101-29 (6 079), 1031 (5 563), 291 (5 500), 1174 (5 395), 643, 738, 556-7, 1059, 839 |
| Notes de commentaire | 541 (130 896 caractères), réparties entre 176 commentaires |
| Apparat | 425 macros, 536 segments (un par vers), 629 entrées, 1 345 leçons ; 532 vers pourvus d'apparat ; 36 macros contiennent en outre des entrées commentées (`%`, 59 fragments) |
| Leçons signées « Bibi » (actives) | 42 (§ 5) |
| Testimonia actifs | 244 (71 côté grec, 173 côté français) ; 175 testimonia désactivés |
| Vers couverts par au moins un commentaire | 854 |
| Didascalies repérées dans la traduction | 63 (indications entre parenthèses) |
| Macros désactivées (lignes `%`) | 175 testimonia, 79 apparats, 60 commentaires, 145 notes (+ 15 `\debutNote`, 3 noms de personnages) |

## 4. Conspectus siglorum de l'auteur

D'après `Introduction.tex` (« Témoins de la pièce ») et les macros :

| Sigle | Témoin (description de l'auteur) |
|---|---|
| R | *Ravennas*, codex gr. 429 de la Biblioteca Classense, Xᵉ s. — avec R^ac, R^pc, R² (main correctrice), « in mg. », « supra lin. » |
| M | *Monacensis*, codex gr. 492 de la BSB, copie du *Ravennas*, XVᵉ s. |
| PSI-1194 | *PSI* XI 1194 : vv. 145-156 ; 237-245 ; 273-288 ; 594-596 ; 804-809 ; 1231 (et 133-144, *PSI* XIV p. XV), IIᵉ s. |
| POxy-3839 | *P. Oxy.* LVI 3839 : vv. 742-766 (fr. 1) ; 941-953 (fr. 2), *c.* 200 — *sic* : le fr. 2 contient les vv. 941-956 (voir `recherche/papyrus.md`) |
| POxy-3840 | *P. Oxy.* LVI 3840 : vv. 1185-1193, IVᵉ s. |
| POxy-4935 | *P. Oxy.* LXXIII 4935 : vv. 1043-1051 (fr. 1) ; 1201-1210 (fr. 2), IIᵉ s. |
| POxy-1176 | *P. Oxy.* IX 1176 (Satyros, *Vie d'Euripide*), fr. 39 col. XII : vv. 335-337 ; 373-375, IIᵉ s. |
| Suid. | *Souda* (éd. Adler), Xᵉ s. |
| Σ | scholies (Σ¹, Σ², Σ^T, Σ^bT…) ; « ed. Iuntina » ; « Divus » (traduction latine) |

Critiques et éditeurs nommés dans l'apparat (attributions, occurrences ; `statistiques.apparat_classement`
de `thesmo.json`) : Brunck 49, Bentley 45, Biset 33 (+ 1 « Bizet »), Zanetti 24, Dindorf 23, Scaliger 22,
Grynaeus 21 (+ 2 « Gryaneus », « Gryaneaus »), Hermann 21, Ellebodius 16, Küster 16, Meineke 13, Fritzsche 13,
Bothe 13, Dobree 12, Enger 11, Austin 10 (dont 1 « Austin & Olson »), Porson 10, Bergk 9, Willems 8, Burges 8,
Daubuz 8 (+ 1 « Daubruz »), Faber 8, Elmsley 7, von Velsen 7 (dont 1 « van Velsen »), Cobet 7, Gelenius 5,
Wilamowitz 5, Rogers 5, Blaydes 5, van Herwerden 5, Boissonade 4, Reiske 4, Bonini 4, van Leeuwen 4,
Thiersch 4, Sommerstein 4, Casaubon 4, Kaibel 3, Reisig 3, puis (≤ 2) Tyrwhitt, Bourdin, Voss, Hirschig,
Jackson, Denniston, Hall–Geldart, Valckenaer, Nauck, Markland, Wecklein, Schöne, Nietzsche, Dover, Toup,
Medaglia, Hunt, Kappeyne, Dawes, Bekker, Schaefer, Handley, Beer, Richards, Hamaker, Lobeck, Kaye, Maas,
Lenting, Grégoire, Rau, Musgrave (écrit « Mugrave »), Coulon, Bachmann, Taillardat… (liste complète par
`apparat.tsv`). Les « anonymus Parisinus » et « anonymus Romanus », la Juntine (« ed. pr. », « ed.
Iuntina ») et « edd. plerique / omnes » complètent les autorités.

## 5. Conjectures signées « Bibi »

### 5.1 Vue d'ensemble

L'apparat de 2023 contient **42 leçons actives signées « Bibi »**, réparties sur 41 segments (vers) de
37 macros `\apparat` (requête : colonne `Bibi` de `apparat.tsv`). Toutes sont imprimées dans le texte
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

Abréviations : « nov. 2022 » = état de la version de novembre 2022 (que reflète aussi, pour les leçons
qu'il recense, l'« Index des corrections proposées », § 5.4) ; « nouv. 2023 » = absente de nov. 2022,
présente dès mars 2023 (pour les vv. 1-946, la version de mars 2023 contient déjà toutes les leçons
« Bibi » de 2023).
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

Depuis novembre 2022 (liste complète, tous états confondus : § 10.3).

| Vers | Conjecture | Statut |
|---|---|---|
| 1 | Χελιδὼν (nom propre, « ap. Clements ») | active en nov. 2022 ; supprimée dès mars 2023 (la note sur l'article d'A. Clements a disparu) |
| 702 | διπλὰ (pour ἔργα R) | active en nov. 2022 ; commentée (`%`) dès mars 2023 ; le texte imprime †πλέα† (Souda) |
| post 870 | < οἶσθ' οὖν ὃ δρᾶσον; > restitué « ap. Σ » (cf. Eur. *Hél.* 325) | active en nov. 2022 ; désactivée ensuite |
| 1072 | θαλάττης τέμνον (pour θανάτου τλήμων) | désactivée (`%`) en nov. 2022 comme en 2023 (mars 2023 s'arrête au v. 946) |
| 1082 | ὀλόφυγ' (pour ὀτότυζ') | désactivée (`%`) en nov. 2022 comme en 2023 |
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

L'« Index des corrections proposées » (fichier `Index.tex`, 32 entrées pour les *Thesmophories*) est
antérieur à la version de 2023 : il donne encore les leçons de novembre 2022 (Χελιδών, ἀγαθῶν; au seul
v. 31, πραῖνοι, δίκανον, θάλικα, ἐγκύμων, διπλὰ), ignore les leçons nouvelles de 2023 (vv. 30 Ἁγάθων,
162, 264, 289, 642-3, 895), et omet aussi neuf leçons déjà présentes en novembre 2022 (vv. 100, 477,
1069, 1090, 1091, 1092, 1153, 1198, 1215) ; il contient en revanche trois entrées qui ne sont pas des
leçons « Bibi » de l'apparat (743, répartition d'après P. Oxy. 3839 ; 1197, συμβήνην R maintenu ;
Σ 1174, τὸ ἄκρως βαδίζειν « ap. Zonaras »). Ce paragraphe décrit la copie de `latex/` ; la version du Drive ajoute le v. 1198
et Sappho (§ 9.3), sans mettre à jour les leçons de novembre 2022.

## 6. Principes d'établissement du texte

Les principes ne sont exposés nulle part de façon suivie (l'Introduction ne contient ni *praefatio* ni
note sur l'édition) ; ils se déduisent de la page de titre, de l'apparat et des déclarations éparses
du commentaire.

**1. Un « Urtext » reconstruit à partir de R.** La page de titre annonce « Les *Thesmophories*
d'Aristophane. *Urtext* avec commentaire, traduction, apparats (critique & témoins) ». Le mot revient
dans le commentaire (vv. 80, 822-3 : « l'*Urtext* — comportait certainement au vers 822 le terme
κανοῦν ») et dans l'Index des gloses d'Hésychius « qui ont servi au rétablissement de l'*Urtext* ».
R est « notre unique source pour la version complète » ; M (Monacensis gr. 492) est traité comme une
copie de R, utile pour ses corrections (≈ 70 mentions dans l'apparat, 37 leçons retenues) ; les papyrus
(PSI 1194, P. Oxy. 3839, 3840, 4935, 1176) apparaissent dans 23 entrées ; la tradition indirecte est très
présente (occurrences dans l'apparat : Souda 89, scholies 53 — « Σ » ou « Schol. » —, Hésychius 7,
Photius 4).

**2. Un apparat positif, un segment par vers.** Forme constante : leçon de R, deux-points, leçon
retenue en gras (`\lecon`) suivie de son autorité, autres conjectures. Sur 629 entrées, 585 marquent
une leçon retenue (classement heuristique par l'autorité de la leçon retenue,
`statistiques.apparat_classement`) : 342 adoptent la correction d'un critique nommé (Brunck 34,
Bentley 32, Biset 25, Zanetti 19, Dindorf 18, Scaliger 17, Grynaeus 15, Küster 14, Ellebodius 12,
Meineke 9…, soit surtout les éditions de la Renaissance et la critique des XVIIIᵉ-XIXᵉ s.), 107
conservent R contre une ou plusieurs conjectures citées, 58 suivent la tradition indirecte ou un
papyrus, 37 M, 41 « Bibi » ; 44 entrées sont purement descriptives (corrections de R, ajouts
marginaux, sigles de personnages). Les
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

**8. Numérotation.** Celle de l'usage moderne (contrôlée sur Wilson 2007, § 2.3), non celle de Hall–Geldart, dont elle
s'écarte dans plusieurs parties lyriques et aux vv. 372-379 ; dans les parties lyriques, l'auteur suit sa
propre colométrie et recale sa numérotation au moyen de `\ligne{n}` (§ 2.3 et § 11.2).

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
| Langue proverbiale | « proverbe/proverbial » dans 29 articles (93 occurrences, pour moitié dans les notes) ; Érasme, *Adages*, dans 21 articles (41 occurrences, presque toutes en note) ; parémiographes (Zénobius 8 articles, Apostolius 8, Diogénien 4, Macarius 2, *Corpus Paroemiographorum* 6) ; Tosi 7 ; Index des allusions proverbiales : 38 entrées ; 106 passages latins balisés `\latin` |
| Images | J. Taillardat, *Les images d'Aristophane*, dans 44 articles (61 occurrences) ; méthode des « matrices métaphoriques » appliquée à l'établissement du texte (vv. 704, 1069) |
| Modèle | Alphonse Willems dans 89 articles (126 occurrences, plus 8 dans l'apparat) : « Lisez Willems ! aucune excuse » ; ses notes sur les *Thesmophories* sont reproduites en annexe et la traduction française de l'auteur est, selon l'Annexe, « la quasi-intégralité » celle de Willems retouchée |

### 7.2 Forme

357 articles (moyenne 940 caractères, médiane 439 ; 49 dépassent 2 000 caractères, 98 en ont moins de
200 ; le plus long, 455-6, « Dossier sur la mère d'Euripide, la vendeuse d'herbes », atteint 15 449
caractères hors notes et traite aussi du scandix et de *Cav.* 19-20), dont 176
pourvus de notes (541 notes numérotées par article, appelées par `\marqueur`). 344 citations en bloc
(`\citComm`), le grec presque toujours suivi d'une traduction française ; 13,6 % des lettres du
commentaire sont grecques. Un article type : lemme grec ; énoncé du problème (« Le vers pèche contre le
mètre », « La répartition des répliques de ce passage fluctue d'une édition à l'autre ») ; revue des
corrections antérieures ; témoin décisif (glose d'Hésychius, scholie mal comprise, proverbe) ;
explication paléographique ; texte restitué et traduit ; souvent reconstitution du jeu de scène ;
pointe finale.

### 7.3 Voix et ton

- **Énonciation.** Alternance du « je » (≈ 200 occurrences) et du « nous » d'auteur (≈ 250, plus
  ≈ 145 « notre/nos ») ; une fois « je [Bibi] » et « N.D.É. » (note 3 au v. 721-5) ; 28 adresses au
  « lecteur ». Ton oral : 210 points d'exclamation, 205 points d'interrogation, ≈ 190 points de
  suspension (sans compter 35 « .. », presque toujours après un point d'exclamation ou d'interrogation :
  « !.. », « ?.. »).
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

Pour ces trois ensembles, le texte à suivre est celui du dossier de travail du Drive (`GCA/`, voir § 10.1) :
il est plus récent et plus complet que les copies de `latex/`. Aucun état du corps de l'édition ne contient
d'introduction ni d'annexes : hors des pages parallèles, ils n'ont qu'un titre (au plus 366 caractères actifs).
Le détail des écarts est dans `contenus_recuperables.tsv` (types `introduction`, `annexes`, `index`) et le
bilan dans `comparaison_versions.json` (`introduction_annexes_index`).

| Fichier | `latex/` | `GCA/` | Ce que `GCA/` apporte |
|---|---:|---:|---|
| `Introduction.tex` | 421 l., 49 729 o | 435 l., 50 923 o | 6 passages ajoutés ou récrits, 1 figure |
| `Annexes.tex` | 1 869 l., 281 876 o | 2 036 l., 346 018 o | 1 long article de Willems, 1 figure, 1 intertitre, 1 vers corrigé |
| `Index.tex` | 441 l., 22 815 o | 453 l., 24 003 o | 9 entrées de plus, 4 entrées complétées, 1 index renommé |

### 9.1 Introduction (`GCA/Aristophane-Thesmo Introduction.tex`, 435 lignes)

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

Écarts avec la copie de `latex/` (numéros de ligne de la version du Drive) :

- l. 172 : note ajoutée à la présentation de la pièce sur les éditions récentes des fragments (M. Pellegrino,
  2015 ; K. Amaral Sacconi, 2020) ;
- l. 278 : phrase récrite (« ce manuscrit qui, croyait-on, allait combler lacunes & pertes définitive[s] ») ;
- l. 332 : note du dossier Mnésiloque complétée (Mnésiloque en marge des *Thesmophories*, dans de nombreuses
  scholies et dans une scholie au v. 332 des *Acharniens*) ;
- l. 337 : « raillés par les poètes et dont le masque comique ou quelque trait particulier suffisait à le faire
  reconnaître des spectateurs », au lieu de « joués par les poètes comiques […] » ;
- l. 426-429 : figure finale, la première page des *Thesmophories* dans R (`Premiere page sans bord.png`) ;
- supprimé : un début de phrase inachevé de la copie de `latex/` (l. 257 de cette copie).

Hors de ce fichier, `GCA/Présentation Thesmophories.txt` (aussi `.odt`, `.pdf`) est un texte de présentation
en deux pages (résumé, contexte historique, « Προλεγόμενα ») dont 236 mots sur 657 ne se lisent nulle part
ailleurs, en particulier la définition de l'édition comme « synopse » (apparat en regard du vers : savoir
« instantanément » si l'on lit Aristophane ou l'« Aristophane travesti » de quelque éditeur) et le parallèle
entre *Nuées*/Délion et *Thesmophories*/Sicile (6 lignes du tableau).

### 9.2 Annexes (`GCA/Aristophane-Thesmo Annexes.tex`, 2 036 lignes)

Préambule : « La quasi-intégralité de la traduction proposée des *Thesmophories* ainsi que les notes qui
composent ces annexes sont tirées de l'œuvre d'Alphonse Willems ».

| Ensemble | Contenu | Taille (caractères actifs) |
|---|---|---:|
| Dossier Willems | portrait ; notice par Maurice Leroy ; bibliographie de Willems (Leroy) ; « Alphonse Willems. Notes d'un vieil élève » (Charles Lacomblé) | ≈ 66 000 |
| Notes de Willems sur les *Thesmophories* (*Bull. Acad. roy. de Belgique*, Classe des lettres, nov. 1908) | introduction et **28 notes** : vv. 16-18, 21, 22-24, 217, 230, 263, 280-281, 289-291, 352-354, 365-367, 400-401, 418-420, 499-501, 509-510, 531-532, 569, 575-576, 592-593, chœur 655-686, 656, 710-712, 773-774, 808-809, 811-812, 1019-1020, 1050-1051, 1052-1055, 1181 | ≈ 87 000 |
| Autres textes de Willems | introduction aux notes sur la *Paix* (1899) ; note sur *Nuées* 83 ; « Le nu dans la Comédie ancienne des Grecs » (1901) ; note sur *Guêpes* 1341 | ≈ 60 000 |
| **« Aristophane et la démocratie athénienne »** (Willems, *Bull. Acad. roy. de Belgique*, Classe des lettres, n° 5, mai 1907 ; repris dans l'*Aristophane* de 1919, t. III, p. 445-473, d'après la note de l'auteur) | **seulement dans la version du Drive** (l. 1489-1635) : 10 594 mots | ≈ 60 000 |
| Papyrus | PSI 1194, P. Oxy. 3839, 4935, 3840 : photographies et pages d'édition (figures), insérées à la place de leurs vers | ≈ 3 100 |
| Iconographie | coupe d'Onésimos (Bâle BS 440, d'après Boardman ; cf. v. 557), ἔγκυκλον à franges pourpres, crocote transparente, cratère de Würzburg (égorgement de l'outre, vv. 754-757) ; **dans la version du Drive seulement**, « La nymphe Écho se drapant sous son manteau » (l. 1341-1349 : vase n° 7864 du *Corpus Vasorum Antiquorum* de Beazley, indications de l'auteur) | ≈ 1 400 |
| Polémique | « Un commentaire du commentaire et son droit de réponse (ou la *Passion de Philologus*) » : les « Impressions » d'un lecteur (avril 2021) sur les « Nouvelles notes thesmophoriennes » que l'auteur avait publiées dans ὁ λύχνος (*Connaissance hellénique*), n° 158 (mars 2021), et la saynète satirique de l'auteur en réponse (personnages : Philologus, Bibi, Pluton, le fantôme d'Aristophane, chœur sur la *Passion selon saint Matthieu*) | ≈ 39 000 |

Autres écarts : intertitre « Portrait d'Alphonse Willems » (l. 189) ; dans la note 21 de Willems, le premier
vers cité est corrigé (ἀλλ᾽ οὖν ἥκεις ὅθεν ἥκεις, l. 1017). Aucun passage de la copie de `latex/` n'a disparu.

Les notes de Willems sont celles auxquelles renvoie le commentaire (« note 4 », « 21ᵉ note », etc.) ;
deux des leçons « Bibi » en dérivent directement (vv. 217, 710).

### 9.3 Index (`GCA/Aristophane-Thesmo Index.tex`, 453 lignes)

Quatre index actifs, renvoyant au commentaire par plage de vers (« 49-50 n. 2 ») ; un « Index des
auteurs cités » et un « Index général » sont commentés (ébauches vides).

| Index | Entrées `latex/` → Drive | Remarque |
|---|---:|---|
| Allusions proverbiales | 38 → 40 | renvoi liminaire à la liste des proverbes de Platon dressée par Jowett ; ajouts : *Paix* 289-291 Λυδὸς [= Δᾶτις] ἐν μεσημβρίᾳ (633 n. 2) ; *Gren.* 840 ἄληθες ὦ παῖ τῆς ἀρουραίας θεοῦ ~ *terrae filius*, Érasme n° 786 (455-6) |
| Gloses d'Hésychius utiles pour l'établissement et la compréhension du texte | 18 → 19 | ajout : *Thesm.* 1197, σ 2137 συμβίνης (1196-217) |
| Corrections proposées | 41 → 42 | ajouts : *Thesm.* 1198 (Τοξότ.) κομίζι σ᾽ αὐτίκ᾽ ; Sappho fr. 70 Reinach-Puech / 125 Voigt αὐτὰ κόραις στεφαναπλόκεο (400-1). Reste un état antérieur à 2023 : il donne encore Χελιδών, πραῖνοι, δίκανον, θάλικα, ἐγκύμων, διπλὰ (§ 5.4) |
| Passages spécialement étudiés (`latex/` : « davantage explicités ») | 60 → 65 | ajouts : *Cav.* 19-20 (455-6) ; *Cav.* 1370 (605 n. 9) ; *Nuées* 55 (738) ; *Nuées* 508 εἰς Τροφωνίου (570) ; *Thesm.* 853/858 τὴν Ἑλένην = τὸ φῶς (853). Entrées précisées : *Lys.* 681 αὐχήν = πέος ; *Thesm.* 643 ἔγκυκλον = jupe courte ; *Thesm.* 647 ἰσθμός |

## 10. Comparaison des versions

Tous les états conservés sont comparés à la version de référence, Harmattan 2023 : dossier de travail du Drive,
série du printemps 2020, archive de juillet 2020, copies de `latex/`. Abréviations de chemins (celles de
`recherche/drive_ressources.md`) : `TH/` = `.sources/drive/fichiers/Grec/Aristophane/Thesmophories/` ;
`GCA/` = `TH/Grec - commentaire - traduction - apparat/`. Sorties, dans `edition/donnees/travaux_anterieurs/` :
`comparaison_versions.json` (inventaire, états, statistiques), `comparaison_versions.tsv` (un élément non conservé
à l'identique par ligne, avec les états où il figure), `contenus_recuperables.tsv` (§ 10.4).

**En bref.** 54 états distincts, de mars 2020 à avril 2024. Le commentaire culmine dans l'état « décembre 2021 » (396 articles,
367 576 caractères, contre 357 et 335 689 en 2023) ; deux élagages l'ont réduit, entre mai et septembre 2022, puis pour la version Harmattan. Mais
l'essentiel n'est pas perdu : sur ce qui manque à la version active de 2023, 20 000 mots sont seulement commentés (`%`) dans les
fichiers de 2023, contre 11 500 mots réellement disparus, à reprendre dans les états anciens ; 8 450 mots de brouillons, dont 3 811
rédigés, n'ont jamais été imprimés par aucun état. `contenus_recuperables.tsv` donne chaque passage, avec son lieu et son statut.

### 10.1 Inventaire et chronologie des états

**Inventaire.** 88 fichiers `.tex` : 56 fichiers analysés, qui forment 54 états distincts ; 8 doublons écartés
par empreinte SHA-256 (`GCA/Aristophane-Thesmophories (copie).tex` = `AT 18 aout 2020.tex` ;
`GCA/… 18 aout 2020.tex` = `… avril 2021.tex` ; `GCA/… mai 2022.tex` = `… decembre 2021.tex` ; `… avec page
break manuel.tex` = `… avec page break.tex` ; `TH/Versions/… 21 mars 2020 - Copie.tex` = `… 21 mars 2020.tex` ;
`TH/Versions/… 25 mars 2020 - Copie.tex` = `TH/… 21 mars 2020 - Copie.tex` ; les deux fichiers Harmattan 2023 de
`GCA/` = leurs homonymes de `latex/`). Sont hors comparaison : 6 fichiers d'introduction, d'annexes et d'index
(§ 9), 9 articles de l'auteur (`recherche/drive_ressources.md` § 8.2), 4 fichiers de Gemini, et 5 fichiers sans
contenu comparable :

- `TH/overleaf/…/main.tex` (1er mars 2020) et `TH/thesm.tex` : texte grec seul, sans apparat ni commentaire, malgré
  le nom du dossier ; `TH/myEdition/myEdition.tex` : essai de mise en page ;
- `TH/Versions/version 2 mai.tex` : copie de `version 2 2 mai.tex` réenregistrée en codage 8 bits (le grec y est
  remplacé par des « ? »), identique par ailleurs : la question laissée ouverte dans `drive_ressources.md` § 8.1 est
  ainsi réglée ;
- `TH/texte - traduction - commentaire - Copie.tex` : fichier corrompu (octets nuls), à récupérer de nouveau sur le
  Drive ; sa taille le place vers le 21-25 mars 2020, dont les états voisins sont conservés.

**Dates.** Une date interne (`\date`) n'existe que depuis « juin 2022 » (IX 2022 jusqu'à « nov 2022 », III 2023 ensuite).
Pour les fichiers récents, l'inventaire du Drive conserve la date d'enregistrement : `… decembre 2021.tex` et `… mai 2022.tex`, 26 mai 2022 ; `… juin 2022.tex` et
`… sept 2022.tex`, 24 septembre 2022 ; `… oct 2022.tex`, 25 septembre 2022 ; `… nov 2022.tex` et `… Harmattan mars
2023.tex`, 22 août 2023. Les noms ne sont donc pas des dates de travail : l'état « décembre 2021 » va jusqu'en mai
2022, et les PDF `… nov 2022 (copie 1).pdf`, `(copie 2)` sont du 27 septembre 2022. Les autres fichiers portent la date de
leur dépôt (24 octobre 2026), sans valeur. L'ordre retenu repose donc sur le contenu : nombre de lignes communes
entre états (sériation), noms de fichiers, et, à partir de 2022, ces dates. La version du Drive de novembre 2022
(Σ pour « Schol. », comme en 2023) est postérieure à la copie de `latex/` ; la version complète de mars 2023 contient
celle de `latex/`, qui s'arrête au v. 946, sur les deux pages (le dernier `\ligne` explicite y est le v. 939).

**Limite.** Sur le Drive, les 42 PDF compilés sélectionnés n'ont pas été copiés (`drive_ressources.md`). Trois au moins
pourraient répondre à un état sans source conservée : `… août 2022.pdf` (5 août 2022), `… septembre 2022.pdf`
(16 septembre 2022), `… V1 avec index.pdf` (27 septembre 2022). Ils n'ont pas pu être comparés.

**Phases.**

1. *Février-mars 2020, le texte seul* : essai de mise en page, puis texte grec sans annotation.
2. *Mars-juin 2020, série « texte - traduction - commentaire »* (19 états) : la traduction est complète dès le premier
   état ; les 121 commentaires de celui-ci (19 711 caractères) sont pour l'essentiel les notes de la traduction de
   Willems, reconnaissables à leurs renvois (« Bull. cité, note 14, ci-après », « t. I, p. 477, note 1 ») et aux
   mentions « Note de Willems » [à vérifier sur Willems 1919, absent de `.sources/`], avec les premières remarques de
   l'auteur (« Je lis ἀλλ᾽ ἦ », v. 97). L'apparat naît entre le 11 et le 29 mars : 6 entrées, 141 le 27 mars, 451 le
   28, 476 le 29. Fin de la série : 227 commentaires, 100 499 caractères, 64 notes.
3. *Été 2020* : l'état du 3 juillet (seulement dans l'archive) fait un bond (146 439 caractères, 145 notes). L'été se
   partage en deux branches : A (`main2` → 1er août → `main`), sans suite ; B (12 juillet, 2 août, 3 août : ces
   fichiers ne diffèrent que de 1 à 5 lignes), qui se poursuit dans `Aristophane-Thesmophories.tex` et les copies du
   18 août (177 007 caractères, 239 notes).
4. *2021* : « avril 2021 » (le même fichier s'appelle aussi « 18 août 2020 » : son contenu le place après l'état du 18
   août et juste avant mai 2021), mai 2021 (`TH/Versions`, puis `GCA/`), août 2021 (270 433 caractères, 395 notes, avec
   5 essais de mise en page qui n'en sont que des extraits), enfin « décembre 2021 », enregistré en mai 2022 : **le
   commentaire atteint son maximum** (396 commentaires, 367 576 caractères, 504 notes, 45 leçons « Bibi »).
5. *2022, élagage et testimonia* : « juin 2022 » (fichier de septembre) crée `\testimonia` (239), ramène le commentaire
   à 356 articles et double le volume des parties commentées (de 84 000 à 170 000 caractères) ; « sept » et « oct » n'y
   changent presque rien (découpage en deux volumes, sauts de page) ; « nov 2022 » ajoute 10 groupes.
6. *2023* : « Harmattan mars 2023 » (266 macros désactivées contre 145 ; dossier 455-6 récrit d'après `GCA/note.txt`) ;
   `… vv 642-fin.tex`, début du second volume ; Harmattan 2023, en deux fichiers, où les testimonia passent en page
   française (`\Xonlyside[A]{R}` : sur les 175 testimonia désactivés, 174 sont sur la page grecque, et 173 d'entre eux
   ont leur homologue actif, de même plage, sur la page française).
7. *13 avril 2024* : copie du second volume, avec de simples bascules de macros ; aucune différence de commentaire,
   de notes ni de texte.

Les 54 états, dans l'ordre retenu (*ttc* = `texte - traduction - commentaire`, *%-macros* = commentaires, notes,
apparats et testimonia désactivés ; statistiques complètes dans `comparaison_versions.json`) :

| Clé | État | Fichier(s) | Groupes | Comm. (car.) | Notes | Apparat | Bibi | Test. (g./d.) | %-macros |
|---|---|---|---:|---:|---:|---:|---:|---|---:|
| 2020-03a | mars 2020 (avant le 11) | `TH/Versions/ttc - Copie.tex` | 533 | 121 (19 711) | 0 | 0 | 0 | 0/0 | 0 |
| 2020-03-11 | 11 mars 2020 | `TH/Versions/ttc - Copie 11 mars.tex` | 533 | 125 (31 752) | 7 | 6 | 1 | 0/0 | 0 |
| 2020-03-21 | 21 mars 2020 | `TH/Versions/ttc 21 mars 2020.tex` | 533 | 134 (38 845) | 3 | 10 | 4 | 0/0 | 5 |
| 2020-03-21b | 21-25 mars 2020 | `TH/ttc 21 mars 2020 - Copie.tex` | 533 | 143 (53 675) | 14 | 26 | 6 | 0/0 | 0 |
| 2020-03-25 | 25 mars 2020 | `TH/Versions/ttc 25 mars 2020.tex` | 533 | 148 (55 943) | 15 | 30 | 6 | 0/0 | 0 |
| 2020-03-26 | 26 mars 2020 | `TH/Versions/ttc 26 mars 2020.tex` | 533 | 166 (60 486) | 17 | 57 | 6 | 0/0 | 0 |
| 2020-03-27 | 27 mars 2020 | `TH/Versions/ttc 27 mars 2020.tex` | 533 | 171 (60 769) | 17 | 141 | 7 | 0/0 | 0 |
| 2020-03-27b | 27 mars 2020 (2) | `TH/Versions/ttc 27 mars 2020 2.tex` | 533 | 172 (60 694) | 19 | 193 | 7 | 0/0 | 0 |
| 2020-03-28 | 28 mars 2020 | `TH/ttc 28 mars 2020.tex` | 533 | 177 (61 385) | 19 | 451 | 7 | 0/0 | 0 |
| 2020-03-29 | 29 mars 2020 | `TH/ttc 29 mars 2020.tex` | 533 | 177 (61 385) | 19 | 476 | 7 | 0/0 | 0 |
| 2020-04-11 | 11 avril 2020 | `TH/ttc 11 avril 2020.tex` | 533 | 177 (61 377) | 20 | 510 | 7 | 0/0 | 0 |
| 2020-04-12 | 12 avril 2020 | `TH/ttc 12 avril 2020.tex` | 533 | 177 (61 381) | 20 | 510 | 7 | 0/0 | 0 |
| 2020-04-19 | 19 avril 2020 | `TH/ttc 19 avril 2020.tex` | 533 | 176 (62 803) | 20 | 511 | 7 | 0/0 | 0 |
| 2020-04-25 | 25 avril 2020 | `TH/ttc 25 avril 2020.tex` | 533 | 179 (64 750) | 20 | 512 | 7 | 0/0 | 0 |
| 2020-04-30 | 30 avril 2020 | `TH/ttc 30 avril 2020.tex` | 533 | 188 (76 234) | 35 | 516 | 7 | 0/0 | 0 |
| 2020-05-02 | 2 mai 2020 | `TH/Versions/version 2 2 mai.tex` | 538 | 197 (79 472) | 38 | 516 | 7 | 0/0 | 0 |
| 2020-05a | mai 2020 (copie 2) | `TH/ttc - Copie (2).tex` | 538 | 206 (84 315) | 40 | 514 | 7 | 0/0 | 0 |
| 2020-05b | mai 2020 (copie 3) | `TH/ttc - Copie (3).tex` | 538 | 226 (98 461) | 59 | 515 | 8 | 0/0 | 0 |
| 2020-06 | mai-juin 2020 | `TH/ttc.tex` | 538 | 227 (100 499) | 64 | 515 | 8 | 0/0 | 0 |
| 2020-07-03 | 3 juillet 2020 (archive) | `TH/Thesmophories Grec – Traduction – Commentaire  – Apparat.zip:main.tex` | 625 | 269 (146 439) | 145 | 583 | 12 | 0/0 | 1 |
| 2020-07-11 | 11 juillet 2020 | `GCA/copie 11 juillet 2020.tex` | 625 | 269 (146 622) | 146 | 585 | 12 | 0/0 | 1 |
| 2020-07m2 | été 2020 (main2) [branche A] | `GCA/main2.tex` | 646 | 266 (147 077) | 146 | 590 | 12 | 0/0 | 1 |
| 2020-07-12 | 12 juillet 2020 | `GCA/copie 12 juillet 2020.tex` | 648 | 269 (149 251) | 151 | 589 | 12 | 0/0 | 1 |
| 2020-08-01 | 1er août 2020 [branche A] | `GCA/copie 1er aout 2020.tex` | 646 | 266 (147 077) | 146 | 589 | 12 | 0/0 | 1 |
| 2020-08m | août 2020 (main) [branche A] | `GCA/main.tex` | 646 | 267 (149 315) | 153 | 589 | 12 | 0/0 | 1 |
| 2020-08-02 | 2 août 2020 | `GCA/copie 2 aout 2020.tex` | 648 | 268 (149 215) | 151 | 589 | 12 | 0/0 | 1 |
| 2020-08-03 | 3 août 2020 | `GCA/copie 3 aout 2020.tex` | 648 | 269 (149 251) | 151 | 589 | 12 | 0/0 | 1 |
| 2020-08a | août 2020 | `GCA/Aristophane-Thesmophories.tex` | 658 | 293 (177 007) | 239 | 599 | 15 | 0/0 | 3 |
| 2020-08-18 | 18 août 2020 | `GCA/AT 18 aout 2020.tex` | 658 | 293 (177 007) | 239 | 599 | 15 | 0/0 | 3 |
| 2021-04 | avril 2021 | `GCA/… avril 2021.tex` | 658 | 293 (176 999) | 239 | 599 | 15 | 0/0 | 3 |
| 2021-05a | mai 2021 (TH/Versions) | `TH/Versions/… mai 2021.tex` | 656 | 292 (182 796) | 255 | 603 | 18 | 0/0 | 10 |
| 2021-05 | mai 2021 | `GCA/… mai 2021.tex` | 657 | 298 (203 923) | 308 | 618 | 18 | 0/0 | 11 |
| 2021-08 | août 2021 | `GCA/… aout 2021.tex` | 656 | 326 (270 433) | 395 | 639 | 28 | 0/0 | 21 |
| 2021-08e1 | août 2021, essai 1 [essai] | `GCA/… aout 2021 test.tex` | 266 | 135 (112 040) | 164 | 212 | 8 | 0/0 | 9 |
| 2021-08e2 | août 2021, essai 2 [essai] | `GCA/… aout 2021 test 2.tex` | 251 | 116 (89 373) | 121 | 174 | 8 | 0/0 | 8 |
| 2021-08e3 | août 2021, essai 3 [essai] | `GCA/… aout 2021 test 3.tex` | 228 | 107 (81 717) | 103 | 161 | 8 | 0/0 | 8 |
| 2021-08e4 | août 2021, essai 4 [essai] | `GCA/… aout 2021 test 4.tex` | 1 | 3 (1 179) | 4 | 4 | 0 | 0/0 | 0 |
| 2021-08e5 | août 2021, essai 5 [essai] | `GCA/… aout 2021 test 5.tex` | 1 | 1 (442) | 0 | 3 | 0 | 0/0 | 0 |
| 2021-12s | août-décembre 2021 (sauvegarde) [sauvegarde] | `GCA/… decembre 2021.tex~` | 656 | 326 (270 433) | 395 | 639 | 28 | 0/0 | 21 |
| 2021-12 | décembre 2021 | `GCA/… decembre 2021.tex` | 759 | 396 (367 576) | 504 | 689 | 45 | 0/0 | 45 |
| 2022-06 | juin 2022 | `GCA/… juin 2022.tex` | 763 | 356 (337 131) | 558 | 671 | 39 | 239/0 | 136 |
| 2022-09 | septembre 2022 | `GCA/… sept 2022.tex` | 763 | 356 (337 131) | 558 | 671 | 39 | 239/0 | 136 |
| 2022-09v | septembre 2022 (deux volumes) [variante] | `GCA/… sept 2022 1 vv 1-633.tex` + `GCA/… sept 2022 2 vv 634-1231.tex` | 763 | 356 (337 131) | 558 | 671 | 39 | 239/0 | 136 |
| 2022-09e | septembre 2022, essai (vv. 372-698) [essai] | `GCA/Test.tex` | 162 | 86 (84 396) | 136 | 181 | 5 | 76/0 | 33 |
| 2022-10 | octobre 2022 | `GCA/… oct 2022.tex` | 763 | 356 (337 132) | 558 | 671 | 39 | 239/0 | 136 |
| 2022-10p | octobre 2022 (sauts de page) [variante] | `GCA/… oct 2022  avec page break.tex` | 763 | 356 (337 132) | 558 | 671 | 39 | 239/0 | 136 |
| 2022-11L | novembre 2022 (latex/) | `latex/… nov 2022.tex` | 773 | 356 (337 166) | 558 | 671 | 39 | 239/0 | 137 |
| 2022-11 | novembre 2022 (Drive) | `GCA/… nov 2022.tex` | 773 | 356 (336 415) | 559 | 671 | 39 | 239/0 | 145 |
| 2023-03 | mars 2023 (Drive) | `GCA/… Harmattan mars 2023.tex` | 778 | 358 (340 745) | 556 | 630 | 42 | 245/0 | 266 |
| 2023-03L | mars 2023 (latex/, tronqué) [variante] | `latex/… Harmattan mars 2023.tex` | 541 | 289 (284 313) | 466 | 454 | 27 | 225/0 | 214 |
| 2023-03s | mars 2023 (sauvegarde) [sauvegarde] | `GCA/… Harmattan mars 2023.tex~` | 1 | 3 (3 316) | 6 | 4 | 1 | 1/0 | 5 |
| 2023p | Harmattan 2023, vol. 2 (état partiel) [variante] | `GCA/… Harmattan 2023 vv 642-fin.tex` | 61 | 21 (26 017) | 49 | 47 | 5 | 6/1 | 18 |
| 2023 | Harmattan 2023 (référence) | `latex/… Harmattan 2023 vv 1-641.tex` + `latex/… Harmattan 2023 vv 642-fin-bis.tex` | 777 | 357 (335 689) | 541 | 629 | 42 | 71/173 | 459 |
| 2024-04-13 | copie du 13 avril 2024 [variante] | `latex/… Harmattan 2023 vv 1-641.tex` + `GCA/… Harmattan 2023 vv 642-fin-copie13-4-2024.tex` | 777 | 357 (335 689) | 541 | 629 | 42 | 71/173 | 459 |

### 10.2 Méthode et statuts

Chaque état est extrait avec l'analyseur de `extraire_travaux.py` (`outils/extraction/comparer_versions.py`, ≈ 3 min sur
deux cœurs ; sorties identiques d'une exécution à l'autre). Le commentaire et les notes sont comparés **au mot près** : un
mot ancien est couvert s'il appartient à une suite de quatre mots présente dans le commentaire actif de 2023 (îlots d'au
moins 6 mots) ; toute suite non couverte d'au moins 8 mots, ou tout élément plus court non retrouvé tel quel, est un
passage perdu, qualifié ainsi, dans l'ordre :

| Statut (`statut_2023`) | Critère |
|---|---|
| désactivé (commenté) en 2023 | 60 % au moins du passage se lit dans une partie commentée (`%`) des fichiers de 2023 ; `proche_2023` donne le fichier et la ligne |
| déplacé en 2023 | 60 % au moins se lit ailleurs : apparat, testimonia, traduction, autre partie du corps, Introduction, Annexes, Index du Drive |
| remanié en 2023 | même suite de mots à 50 % (trigrammes), ou 75 % au moins des mots rares du passage (5 mots rares au moins) dans le commentaire de 2023 sur ces vers (± 3) : même idée, autre rédaction |
| disparu | ni l'un ni l'autre. `proche_2023` signale le commentaire de 2023 sur ces vers s'il reprend 30 % au moins des mots rares : le sujet peut survivre sous une autre forme |
| disparu (déjà désactivé dans cet état) | commenté dans l'état ancien, absent de 2023 même commenté |

Pour le reste : entrées d'apparat appariées par lemme et autorités (± 2 vers), sigles anciens rapportés à ceux de 2023
(Mu2 = M ; P13, P14, P68, P4935, P50 = PSI-1194, POxy-3839, POxy-3840, POxy-4935, POxy-1176 ; Schol. = Σ) ; une entrée
sans leçon grecque (« suppl. Bentley ») est tenue pour remaniée si le même critique figure au vers (± 1) ; testimonia
appariés par mots grecs et nombres ; texte grec vers par vers, après recalage des numérotations décalées des états de 2020
(un vers est rapporté au vers voisin dont le texte lui ressemble nettement mieux) ; une différence qui ne tient qu'à la
colométrie (le même texte se lit à la suite dans les vers voisins, ± 3, des deux côtés) n'est pas une leçon ; traduction
retenue seulement si elle ressemble à moins de 75 % à celle de 2023, y compris à ± 8 vers ; remarques entre parenthèses
de la traduction retenues à part ; analyses métriques comparées notation mise à part.

Les contenus perdus sont regroupés d'un état à l'autre en **lignées** : du plus récent au plus ancien, chaque contenu se
rattache à une lignée (vers voisins, texte inclus à 75 % au moins dans son représentant) ou en ouvre une ; ce qu'une forme
ancienne a en propre forme une ligne à part. Une ligne = une forme distincte : `version` est l'état le plus récent où elle
se lit, `premiere_version` le premier, `nb_versions` le nombre d'états, et `remarque` dit à partir de quel état de la filiation
principale elle manque (« absent à partir de », « plus actif à partir de »). Les formes successives d'un même
dossier ont donc chacune leur ligne, et les totaux de mots qui suivent distinguent mots cumulés et mots distincts.

**Contrôles** (reproductibles : `outils/extraction/verifier_recuperables.py`). (1) Chaque ligne du tableau est rapprochée de
son fichier et de sa ligne : sur 1 775 lignes, 10 seulement ne sont pas validées par le script, à cause d'un
collage de macros (`\cf v. 288`, `Bentley\Rpc`), et ont été vérifiées à la main ; les 51 attributions et les figures ne
sont pas testées. (2) Aucun passage « disparu » de 8 mots au moins ne se lit, même à moitié, dans le texte actif de 2023.
(3) Les 506 renvois à une partie commentée de 2023 tombent sur une ligne en `%` et le texte se lit à cet endroit (504 par le
script, 2 à la main) ; 12 lignes désactivées, de trop peu de mots, n'ont pas de renvoi. (4) Audit de complétude : le texte actif
et commenté de tous les états a été confronté, ligne à ligne, à 2023 et au tableau ; ne restent que des fragments de moins
de 8 mots, de légères retouches de la traduction et les lignes qui mêlent vers, mètre et apparat, propres à cette lecture. (5) Les 31 lignes de conjectures ont été relues une
à une. Le statut reste une mesure de surface : « disparu » veut dire que le texte n'y est plus, non que l'idée a disparu ;
et le remaniement d'un passage peut échapper au seuil de 75 % (voir `proche_2023`).

### 10.3 Ce qui a disparu, et quand

Ordre de grandeur : le commentaire actif de 2023 compte 56 696 mots et ses notes 22 126. Par rapport à ce total de 78 800
mots, **11 500 mots distincts ont disparu** (13 400 mots cumulés), **20 000 mots distincts sont désactivés mais présents dans
les fichiers de 2023** (21 700 cumulés), et 750 sont remaniés. Il faut y ajouter 8 450 mots de brouillons commentés que
n'imprime aucun état (3 811 mots rédigés, 4 639 mots de sources grecques copiées, § 10.4).

Le tableau suivant donne, pour chaque état, ce dont il est le **dernier témoin** : ce qui manque ou n'est plus actif à
l'état suivant (commentaire et notes : lignées / mots cumulés ; autres types : lignées).

| Dernier état où se lit le contenu | comm.+notes disparus (lignées / mots) | remaniés | désactivés | Bibi | apparat | texte grec | attrib. | mètre | trad. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mars 2020 (avant le 11) | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 6 | 1 |  | 4 |
| 11 mars 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 3 |  |  |  |
| 21 mars 2020 | 3 / 41 | 0 / 0 | 1 / 62 |  | 1 | 3 |  |  |  |
| 25 mars 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 9 | 1 |  | 1 |
| 26 mars 2020 | 2 / 32 | 0 / 0 | 0 / 0 |  |  | 4 | 4 |  | 2 |
| 27 mars 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  | 1 | 1 |  |  |  |
| 27 mars 2020 (2) | 0 / 0 | 0 / 0 | 0 / 0 |  | 2 | 17 |  |  |  |
| 28 mars 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 3 |  |  |  |
| 29 mars 2020 | 1 / 9 | 0 / 0 | 0 / 0 |  |  | 2 |  |  |  |
| 12 avril 2020 | 1 / 19 | 0 / 0 | 0 / 0 |  |  |  |  |  |  |
| 19 avril 2020 | 2 / 11 | 0 / 0 | 0 / 0 |  |  | 1 |  |  |  |
| 25 avril 2020 | 1 / 7 | 1 / 18 | 0 / 0 |  | 6 | 7 |  |  | 1 |
| 30 avril 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 2 |  |  |  |
| 2 mai 2020 | 1 / 11 | 1 / 20 | 0 / 0 |  | 5 | 4 |  |  |  |
| mai 2020 (copie 2) | 2 / 31 | 0 / 0 | 0 / 0 |  | 4 | 4 |  |  | 1 |
| mai-juin 2020 | 60 / 2 303 | 6 / 72 | 4 / 362 |  | 23 | 42 | 16 |  | 46 |
| 3 juillet 2020 (archive) | 2 / 21 | 0 / 0 | 0 / 0 |  | 2 | 1 |  |  |  |
| 11 juillet 2020 | 8 / 105 | 0 / 0 | 1 / 24 |  | 12 | 12 | 4 |  | 1 |
| été 2020 (main2) | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 1 |  |  |  |
| août 2020 (main) | 2 / 31 | 0 / 0 | 0 / 0 |  |  |  |  |  | 2 |
| 3 août 2020 | 22 / 704 | 1 / 57 | 1 / 13 |  | 17 | 17 | 2 |  | 8 |
| 18 août 2020 | 0 / 0 | 0 / 0 | 0 / 0 |  |  | 2 | 1 |  | 1 |
| avril 2021 | 19 / 851 | 0 / 0 | 3 / 149 | 1 | 6 | 7 | 2 |  |  |
| mai 2021 (TH/Versions) | 8 / 775 | 0 / 0 | 2 / 342 | 2 | 15 | 7 | 2 |  |  |
| mai 2021 | 19 / 539 | 3 / 44 | 9 / 705 | 3 | 24 | 38 | 4 | 3 | 8 |
| août 2021 | 29 / 1 692 | 5 / 50 | 12 / 769 | 3 | 52 | 72 | 5 |  | 14 |
| décembre 2021 | 96 / 2 436 | 21 / 238 | 109 / 10 716 | 12 | 72 | 36 | 5 | 9 | 58 |
| octobre 2022 | 0 / 0 | 0 / 0 | 0 / 0 |  |  |  | 1 |  |  |
| novembre 2022 (latex/) | 1 / 5 | 0 / 0 | 3 / 369 |  | 1 |  |  |  |  |
| novembre 2022 (Drive) | 57 / 3 620 | 13 / 276 | 108 / 6 373 | 7 | 86 | 13 | 3 | 2 | 17 |
| mars 2023 (Drive) | 7 / 176 | 0 / 0 | 25 / 1 798 |  | 1 |  |  |  | 1 |

Par période (commentaire et notes) :

| Dernier état | Disparus | Désactivés |
|---|---:|---:|
| mars - juin 2020 | 73 lignées, 2 464 mots | 5 lignées, 424 mots |
| juillet - août 2020 | 34 lignées, 861 mots | 2 lignées, 37 mots |
| avril - août 2021 | 75 lignées, 3 857 mots | 26 lignées, 1 965 mots |
| « décembre 2021 » (mai 2022) | 96 lignées, 2 436 mots | 109 lignées, 10 716 mots |
| octobre - novembre 2022 | 58 lignées, 3 625 mots | 111 lignées, 6 742 mots |
| mars 2023 | 7 lignées, 176 mots | 25 lignées, 1 798 mots |

- **Sortie de la série du printemps 2020 (mai-juin → 3 juillet 2020)** : le commentaire est récrit. Disparaissent les
  renvois et notes brèves venus de Willems (26 lignes du tableau portent la mention « note ou renvoi de Willems »), le
  premier dossier sur 2-3 (821 mots, d'après l'article d'A. Clements) et des pages plus libres sur 241 (οἴμοι τάλας,
  θάλασσ᾽), 246 (αἰθός), 232, 489. Le dossier de 2-3 reparaît, récrit, mais commenté (791 mots), de juillet 2020 à
  novembre 2022.
- **2021** : les rédactions anciennes sont remplacées passage par passage : 288-91 (606 mots), 7-8, 5-6, 22-4, 241, 246, 100,
  puis, après août 2021, 855-7 (348 mots), 939-42 (518 mots), 811-2 (Miltiade), 1056-97, 1073-5.
- **« Décembre 2021 » → « juin 2022 » : premier élagage**, le plus important : 10 716 mots passent en `%` (1031, 855-7,
  138, 939-42, 898, 895, 702, 570, 840-1, 616…) et 2 436 disparaissent. Les notes de travail actives
  (`\eff`, « à revoir : … ») disparaissent ou passent en `%`, ainsi que 58 lignes de traduction et de remarques (didascalies,
  doutes sur les attributions). Le nombre de commentaires tombe de 396 à 356 ; 5 leçons « Bibi » sont abandonnées, 6 remplacées,
  et une (1047) est rendue à Hermann.
- **Novembre 2022 → mars 2023 : second élagage**, pour la version Harmattan : 6 373 mots passent en `%` (161-3, 291, 486, 702,
  896 n. 1, 49-50 n. 2…) et 3 620 disparaissent, surtout parce que deux dossiers sont refaits : 455-6, dont la première
  rédaction (1 271 mots) cède la place au dossier de `GCA/note.txt` (3 714 mots, dont 3 681 actifs en 2023 ; le brouillon
  n'a rien en propre), et le dossier Χελιδών d'A. Clements (commentaire de v. 1, 105 mots ; note ; 791 mots déjà commentés ;
  conjecture), retiré tout entier. Reformulés aussi : 1-10, 21, 22-4, 49-50, 56-7, 179, 248, 263.
- **Mars 2023 → 2023** : 49-50 (710 mots : l'ancien dossier †πράμος†, remplacé par πρανοῦν προτέρους), 605 n. 6, notes de 100,
  702, 894, 217 ; 25 lignées en `%`, 7 disparues (176 mots). Le reste est presque identique : 353 commentaires sur 358 et
  533 notes sur 556 conservés tels quels ; une entrée d'apparat désactivée (417 μορμολυκεῖα) ; testimonium 223 désactivé.

**Novembre 2022 (Drive) → 2023**, élément par élément :

| Élément | Conservé | Conservé, rédaction abrégée | Remanié | Désactivé (`%`) | Autres statuts | Absent |
|---|---:|---:|---:|---:|---|---:|
| Commentaires (356) | 294 | — | 43 | 3 | réécrits 9 ; abrégés (partie désactivée) 5 ; reformulé 1 | 1 |
| Notes (559) | 462 | — | 18 | 55 (+ 1 reformulée) | abrégées 8 ; intégrées au commentaire 6 ; reformulées 4 ; réécrites 4 | 1 |
| Apparat, entrées (671) | 526 | 56 | 45 | 39 | transférées dans les testimonia 2 | 3 |
| Testimonia (239) | 225 | 12 | 1 | 1 | — | 0 |

- **Commentaires absents ou désactivés** : v. 1 (seul article véritablement supprimé, avec sa note et la leçon Χελιδών) ;
  désactivés : 45 (βομβάξ, note de Chantraine), 162 (οἵπερ ἁρμονίαν de la Souda, arguments de Coulon), 204 (νυκτερήσια).
  **Réécrits** (même plage, texte largement nouveau) : 1-10, 21, 22-4, 49-50, 56-7, 179, 248, 263, 455-6. **Abrégés** (une
  partie passée en `%`) : 161-3, 247, 291, 486, 702.
- **Notes désactivées** (56, par passage) : 455-6 (14), 161-3 (6), 291 (6), 939-42 (6), 49-50 (3), 702 (3), 100, 162, 643,
  894 (2 chacun), 101-29, 217, 248, 273, 556-7, 605, 704, 711-2, 804, 896 (1 chacun). Ce sont pour beaucoup des digressions ou
  des pointes polémiques (« le rire du soldat allemand dans la *Traversée de Paris* », 455-6 ; « le chef de cette meute »,
  556-7 ; « Aristophane est drôle ! », 804 ; « l'internationale du commentaire », 939-42) et des références bibliographiques
  secondaires : l'auteur a lui-même commencé l'allègement qu'appelle une édition de référence (§ 7.3).
- **Apparat** : les 39 entrées désactivées sont des conjectures écartées, R étant conservé dans le texte (21 : 27, 165,
  245, 277, 305, 353, 389, 440, 461, 511, 516, 536, 562, 687, 768, 771, 782, 967, 990, 994, 1010), des variantes de la
  tradition indirecte (8 : après 129, 390, 391, 439, 481, 486, 494, 910), des corrections pourtant imprimées dans le texte
  (6 : 417 μορμολυκεῖα Dindorf, 537 ποθὲν Küster, 542 ᾽γίγνωσκον Bentley, 798 αἰσχυνθεῖσ᾽ Zanetti, 808 τις Küster, 1014 σώσων M ;
  de même 481 μου ᾽κνυεν de la Souda), deux notes sur les sigles de personnages (295, 372), une entrée récrite (555, réduite
  à « add. γε Faber ») et la restitution « Bibi » après le v. 870 ; deux informations sont passées dans les testimonia (142
  τὸ πέος Suid. λ 63, π 987 ; 162 οἵπερ ἁρμονίαν Suid. ε 989) ; trois entrées ont disparu sans trace : 1 (Χελιδών Bibi ap.
  Clements), 289 (καὶ τὴν θυγατέρα R : del. Willems), 726 (χρῆν σ᾽ R² : χρὴ μ᾽ M).
- **Testimonia** : 50 (la glose d'Hésychius π 3188 passe de πραῖνοι· πρηνίζει, καταστρέφει à †πραῖνοι· πρηνίζειν, καταστρέφειν,
  c'est-à-dire de la leçon normalisée à la leçon du manuscrit) ; 223 (Souda ε 2807, désactivé). Ce sont les deux seules pertes
  de testimonia de toute l'histoire du texte : la catégorie n'existe que depuis juin 2022.
- **Texte grec : 20 vers diffèrent.** Mots (11) : 50 πραῖνοι ἡμέτερος → πρανοῦν προτέρους ; 99 γὰρ → νῦν (Rogers au lieu de
  Burger) ; 162 ἐχύμισαν → ἐκεχήνεσαν ; 163 δίκανον → διέκειντ᾽ ; 263 χαλαρὰ γ᾽ οὐ χαίρεις → (Ἀγάθ.) χαλαρὰ γοῦν χαίροις ; 289 χοιρίον →
  Χοιρίλ᾽ ; 291 θάλικα → θυλάκιον ; 446 ἐγκύμων → ἔγκυος ; 657 ἐπελήλυθ᾽ → ἐπελήλυθε ; 702 διπλὰ → †πλέα† ; 895 βάϋζε → κόνυζα.
  Ponctuation (5) : 3, 27, 28, 52, 264. Accent ou majuscule (2) : 1 Χελιδὼν → χελιδὼν ; 45 τι → τί. Découpage (2) : 913-914 et
  959-960 réunis chacun sur une ligne.
- **Attributions (3 vers)** : 45 (le dernier mot du vers n'est plus rendu à Mnésiloque), 263-264 (Agathon répond dès le v. 263 ;
  l'attribution du v. 264 est signée « Bibi » en 2023).
- **Traduction** : 46 vers retouchés, 17 nettement différents (3 retouchés seulement entre mars 2023 et 2023).

**Sur toute la période** (tableau, types `texte grec`, `attribution`, `traduction`, `analyse métrique`) :

- *Texte grec* : 314 lignées (267 de mots, 47 d'accent, d'esprit ou de majuscule). Beaucoup sont des coquilles des états de
  2020 (Παίδρας pour Φαίδρας, v. 550) ; d'autres sont de vrais choix, à relire : 196 μαινοίμεθα, 555 οὐδέπω, 702 μεστὰ, 864
  Σκαμανδρίαις, 1054 δαιμόνων. L'interversion des vv. 3-4 (§ 11.1) apparaît dans « juin 2022 » : tous les états
  antérieurs ont l'ordre usuel.
- *Attributions* : 51 lignées : 16 prennent fin avec la série du printemps 2020, 20 entre juillet 2020 et août 2021, 9 ensuite.
  Les remarques de la traduction (« Mnésiloque chez Willems », « Willems attribue à Mnésiloque la suite ») montrent que la
  répartition des répliques suivait d'abord Willems.
- *Traduction* : 165 lignées (142 lignes nettement différentes, 3 absentes, 20 remarques ou didascalies), dont 46 s'arrêtent à
  « mai-juin 2020 » et 58 à « décembre 2021 ». Les remarques sont utiles à l'établissement du texte : « l'archer scythe
  n'intervient-il pas peu avant ? » (1078), « D'aucuns – pas Willems – attribuent la réplique… » (745), « Chez W., à Mn. : καὶ δὴ
  πεύγει » (1092).
- *Mètre* : 14 lignées seulement ; les autres écarts ne sont que de notation (`trim. iamb.` / `3 ia.`, `ion. min.` / `io. min.`).

**Conjectures « Bibi » : liste complète**, tous états confondus, de celles qui ne sont pas conservées telles quelles
(complète le § 5.3) :

| Vers | Entrée d'apparat (forme la plus récente) | Présente dans | Devenir |
|---|---|---|---|
| 1 | χελιδὼν R : Χελιδὼν Bibi ap. Clements | mai 2021 (TH/Versions) → novembre 2022 (Drive) | abandonnée |
| 31 | ἔστιν τις ἀγαθῶν (Μνη.) continuat R : (Εὐρ.) M / Ἀγάθων R : ἀγαθῶν; Bibi | commentée en 2023 | désactivée |
| 50 | πράμος R : πρόμος Grynaeus : πραῖνοι Bibi ap. Hesych. π 3188 | juin 2022 → novembre 2022 (Drive) | remplacée : πρανοῦν Bibi ap. Hesych. π 3188 |
| 70-4 | Μνη. et Εὐρ. (70) Μνη. (71) et Εὐρ. (72-4) R : Μνη. et Εὐρ. (70) et Μνη. (71-4) Bibi : alii ali… | 3 juillet 2020 (archive) → décembre 2021 | remplacée : (Μνη.) (71) et (Εὐρ.) (72-4) R : (Μνη.) (71-4) Bibi ap. Σ :  |
| 86 | δίʹ καιʹ R : δίκαιά γ᾽ Grynaeus : διὰ δίκην Bibi | 3 juillet 2020 (archive) → avril 2021 | abandonnée |
| 163 | διεκίνων R : διεκίνουν Suid. ε 989, ι 495 : διεκλῶντ᾽ Toup : δίκανον Bibi ap. Hesych. δ 1805 | juin 2022 → novembre 2022 (Drive) | remplacée : διέκειντ' Bibi |
| 164 | διεκίνων R : διεκίνουν Suid. ε 989, ι 495 : διεκλῶντ᾽ Toup : δίκανα Bibi ap. Hesych. | mai 2021 (TH/Versions) → décembre 2021 | remplacée : διέκειντ' Bibi |
| 288 | λαθεῖν R : λαβεῖν Bibi, cf. v. 1017 | 21-25 mars 2020 → mai 2021 (TH/Versions) | abandonnée |
| 291 | καὶ πρὸς θάληκον R : πρὸς θυλάκιον καὶ Bibi | 27 mars 2020 → mai 2021 (TH/Versions) | remplacée (texte de 2023 : leçon imprimée) : πρὸς θυλάκιον Bibi |
| 291 | πρὸς θάληκον R : Ποσθαλίσκον Dindorf : πρὸς θάλικα Bibi | mai 2021 → novembre 2022 (Drive) | remplacée : πρὸς θυλάκιον Bibi |
| 337 | ευριπιδιωι̣[. .]υ̣τ P50 : Εὐριπίδῃ Μήδοις R : Εὐριπίδῃ Μήδοις τ᾽ Biset : Εὐριπίδῃ ᾧ ταῦτʹ Bibi | mai 2021 → décembre 2021 | abandonnée |
| 446 | ἐν Κύπρῳ R : ἐγκύμων Bibi | août 2021 → novembre 2022 (Drive) | remplacée : ἔγκυος Bibi |
| 500 | ὑπ᾽ αὐγὰς οἷόν R : ὑπαυγάσ᾽ οἷόν Hermann (1838) : ὑπαυγάσοι ὄν Bibi | mai 2020 (copie 3) → mai 2021 | abandonnée |
| 557 | τὸν σῖτον R, Suid. σ 512, legebat sch. : τὴν μᾶζαν Bibi | 11 mars 2020 → décembre 2021 | remplacée : τὸν κύσθον Bibi cf. v.1114 |
| 639-40 | (Μνη.) 639 et (Γυνή) 640 R : (Μίκα) Bibi | commentée en 2023 | désactivée |
| 702 | ἔργα R : πλέα Suid. : δοῦλα cod. Laur. : διπλὰ Bibi | août 2021 → novembre 2022 (Drive) | abandonnée |
| 734 | θερμόταται R, Suid. θ 251 : θερμοπόται Bibi | août 2021 → décembre 2021 | abandonnée |
| 815 | ταῦτα R : ταὐτά Bibi | décembre 2021 | abandonnée (texte de 2023 : leçon imprimée) |
| post v. 870 | < οἶσθ᾽ οὖν ὃ δρᾶσον; - ∪- / ×- ∪- > om. R : restituit ap. Σ Bibi (cf. Eur. Hel.325) | août 2020 → novembre 2022 (Drive) | désactivée |
| 942 | ἑστιῶν R : ἡστίων Bibi | décembre 2021 | abandonnée |
| 1040 | λιτομέναν R : ἀντομένα (et -αν) Schol. : λιτομένα Enger : ἀλιτόμην ἄν Bibi | décembre 2021 | abandonnée |
| 1041 | φεύγουσαν R : χέουσα Rau (Paratragödia, p.75) post Casaubon : φλέγουσαν Mugrave (ad Eur. Or.140… | décembre 2021 | remplacée : ψεφαυγοῦς Bibi, cf Σ ad v.1054, Hesych. ψ 135 |
| 1047 | [ι]ω̣μοιρ̣[ας P4935 : ἰώ μοι μοίρας R : ἰώ μοίρας Bibi | décembre 2021 | attribuée à un autre critique : ἰώ μοίρας Hermann |
| 1069 | δι᾽ Ὀλύμπου R : διό λυποῦ Bibi | 21 mars 2020 → mai 2021 | remplacée : †δι᾽† ὀλυμπίας Bibi ap. Hesych. (ο 649) |
| 1069 | δι᾽ Ὀλύμπου R : διάλυ᾽ ᾽μπουσ᾽ Bibi | août 2021 | remplacée : †δι᾽† ὀλυμπίας Bibi ap. Hesych. (ο 649) |
| 1071 | μέρος ἐξέλαχον R : μέρος ἐκ σέλαχος Bibi | 21 mars 2020 → mai 2021 | remplacée : μόρος ἔξελ᾽ ἄχος. Bibi |
| 1072 | θανάτου τλήμων R : θαλάττης τέμνον Bibi | 21 mars 2020 → août 2021 | désactivée |
| 1074 | στωμυλωμένη R : στωμύλα μένη Bibi | 21-25 mars 2020 → août 2021 | remplacée : στωμυλιομενής Bibi |
| 1078 | Μνη. χαριεῖ μοι παῦσαι — Εὐρ. παῦσαι R : Μνη. χαριεῖ μοι ᾽παΰσαι — simul Μνη. et Εὐρ. παῦσαι Bi… | décembre 2021 | remplacée : (Εὐρ.) ᾽παΰσαι Bibi |
| 1082 | ὀτότυζ᾽ R : ὀλόφυγ᾽ Bibi | commentée en 2023 | désactivée |
| 1093 | (Εὐρ.) ποῖ ποῖ πέτομαι om. R : suppl. Bibi | décembre 2021 | remplacée : (Εὐρ.) ποῖ ποῖ πέτει om. R : suppl. Bibi |

Sur les 42 leçons « Bibi » de 2023, 32 étaient déjà dans « novembre 2022 » ; le nombre maximal, 45, est atteint dans
« décembre 2021 ».

### 10.4 Contenus récupérables

`edition/donnees/travaux_anterieurs/contenus_recuperables.tsv` compte 1 775 lignes. Colonnes : `version` (état le plus récent où le contenu se lit), `fichier`,
`ligne`, `type`, `vers` (entre crochets : déduit du groupe), `extrait`, `statut_2023`, `premiere_version`, `nb_versions`,
`proche_2023` (ce qui lui répond en 2023 : leçon, article, ou ligne commentée), `remarque`, `nature`, `mots`. Le texte du
commentaire et des notes y est complet (les brouillons et les ajouts des Annexes sont abrégés, la ligne source étant donnée) ;
`nature`, automatique, sert au tri : `texte rédigé`, `note de travail`, `note ou renvoi de Willems`, `renvoi`, `matériaux
(textes grecs copiés)`.

| Type | Lignes | Disparu | Désactivé | Remanié, déplacé | Autre |
|---|---:|---:|---:|---:|---|
| commentaire | 464 | 277 (11 199 mots) | 155 (16 719) | 32 (584) | |
| note | 197 | 55 (1 218) | 123 (4 963) | 19 (191) | |
| déjà commenté dans l'état, absent de 2023 | 11 | 11 (1 002) | | | |
| brouillon commenté (2023) | 146 | | 146 (8 450) | | |
| conjecture « Bibi » | 31 | | 5 | | 10 abandonnées, 15 remplacées, 1 attribuée à un autre |
| apparat | 345 | 81 | 90 | 174 | |
| testimonium | 2 | | 1 | 1 | |
| texte grec | 314 | | | | 267 leçons, 47 accents |
| attribution | 51 | | | | abandonnées |
| analyse métrique | 14 | | | | abandonnées |
| traduction | 165 | | | | 142 différentes, 3 absentes, 20 remarques |
| introduction, annexes, index | 35 | 6 (Présentation) | | | ajouts du Drive, § 9 |

**Comment s'en servir.** Pour rétablir un contenu désactivé, il suffit de lever les `%` à la ligne indiquée dans `proche_2023` ;
pour un contenu disparu, de reprendre le texte de la colonne `extrait`, ou la source indiquée (une ligne `[…]` signale un passage
pris au milieu d'un article). Beaucoup de ces pages ont été retirées à dessein (ton polémique, digressions, conjectures
abandonnées) : le tableau les rend disponibles, il ne dit pas qu'il faut les rétablir, et toute référence ou leçon qu'elles
contiennent reste à vérifier (CLAUDE.md).

**Désactivés : les principaux dossiers**, présents dans les fichiers de 2023 :

| Vers | Mots | Dernier état actif | Ligne en 2023 | Sujet |
|---|---:|---|---|---|
| 1031 | 1 322 | décembre 2021 | vv 642-fin-bis, l. 3626 | détour par les *Guêpes* 669-680 : κηθάριον, Κόννου ψῆφον (proposition Χίων ψῆφον), Eudème et la pierre ponce |
| 855-7 | 1 077 | décembre 2021 | vv 642-fin-bis, l. 2235 | prologue de l'*Archélaos* (Eur. fr. 228), καλλήϊον Γαιᾶ ; les Égyptiens et la syrméa ; forme longue |
| 138 | 717 | décembre 2021 | vv 1-641, l. 1594 | τί δὲ λύρα κεκρυφάλῳ : un proverbe (lyre et choucas, Aulu-Gelle) sous le jeu κεκρύφαλος / κόκκυξ |
| 49-50 | 710 | mars 2023 (Drive) | vv 1-641, l. 990 | ancien dossier †πράμος† : πρόμος, πραῖνοι, glose d'Hésychius π 3188, βροντὴ ἀντὶ πορδῆς |
| 939-42 | 532 | décembre 2021 | vv 642-fin-bis, l. 3062 | les corbeaux du v. 942 : dossier de la conjecture ἡστίων (παραχοῖ τοῖς κόραξι νήστιων) |
| 898 | 520 | décembre 2021 | vv 642-fin-bis, l. 2697 | Ἀντιθέου Γαργηττόθεν : un proverbe caché (τις θεῶν … κατώρθωσεν) ; Critylla manieuse de torche |
| 895 | 509 | décembre 2021 | vv 642-fin-bis, l. 2574 | βαϋζα R : objections à βάϋζε ; matériaux sur βρύα, κόνυζα, les pierres et le pic (Élien) |
| 702 | 451 | décembre 2021 | vv 642-fin-bis, l. 908 | le proverbe de l'audace : ἔργα, πλέα, δοῦλα dérivés d'un même διπλά ; Pseudo-Maxime |
| 702 | 293 | novembre 2022 (Drive) | vv 642-fin-bis, l. 905 | même dossier, seconde rédaction |
| 1069-72 | 420 | août 2021 | vv 642-fin-bis, l. 4378 | Empuse (Hésychius ε 2507) : διάλυ᾽ ᾽μπουσ᾽ ; μέρος ἐκ σέλαχος ; θαλάττης τέμνον |
| 161-3 | 414 | novembre 2022 (Drive) | vv 1-641, l. 1712 | la mitre et δίκανον (Hésychius δ 1805), Ibycos, Anacréon, Alcée |
| 500 | 414 | mai 2021 | vv 1-641, l. 3766 | défense du v. 500 : ὑπαυγάσ(αι) d'après Hermann, le stratagème de la femme, ἐγκεκαλυμμένον |
| 570 | 410 | décembre 2021 | vv 1-641, l. 4228 | Athénée XIV 645e (fr. 269 [256]) : ἐγκρίδες, κάθαρμα, querelle des vendeurs |
| 896 n. 1 | 366 | novembre 2022 (Drive) | vv 642-fin-bis, l. 2628 | digression : le Socrate d'Aristophane et celui de Platon (Boutang, Boudou) |
| 452 | 337 | mai 2021 (TH/Versions) | vv 1-641, l. 3341 | la « crise couronnomique » et le double discours de la vendeuse de couronnes |
| 291 | 333 | novembre 2022 (Drive) | vv 1-641, l. 2684 | θάλικα, métonymie du portefeuille ; la question du nom de Mnésiloque |
| 486 | 313 | novembre 2022 (Drive) | vv 1-641, l. 3668 | κεδρίδας, ἄννηθον, σφάκον : vertus de ces plantes d'après Pline (extraits traduits) |
| 49-50 n. 2 | 277 | novembre 2022 (Drive) | vv 1-641, l. 990 | βὴξ ἀντὶ πορδῆς et Sommerstein |
| 1040 | 277 | décembre 2021 | vv 642-fin-bis, l. 4088 | φῶτα λιτομέναν, variante ἀντομένα de la scholie, ἀλιτόμην ἄν |
| 840-1 | 265 | décembre 2021 | vv 642-fin-bis, l. 2063 | la mère d'Hyperbolos et les comiques |
| 616 | 241 | décembre 2021 | vv 1-641, l. 4457 | κάρδαμον : objection de Willems à l'identification au cresson |
| 735 | 202 | décembre 2021 | vv 642-fin-bis, l. 1271 | ὦ θερμόταται γυναῖκες : contre LSJ et Taillardat |

**Disparus : les principaux dossiers**, à reprendre dans l'état indiqué :

| Vers | Mots | État | Lieu | Sujet |
|---|---:|---|---|---|
| 455-6 | 1 271 | novembre 2022 (Drive) | `GCA/… nov 2022.tex`, l. 2911 | première rédaction du dossier : la vendeuse de couronnes, Chypre, Euripide fils de la terre ; remplacée par le dossier actuel (`GCA/note.txt`) |
| 2-3 | 821 | mai-juin 2020 | `TH/ttc.tex`, l. 273 | χελιδών, l'étoile d'A. Clements ; ἐξ ἑωθινοῦ |
| 2-3 | 791 | novembre 2022 (Drive) | `GCA/… nov 2022.tex`, l. 457 | même dossier récrit, avec un exposé de méthode : commenté dès juillet 2020, supprimé en 2023 |
| 288-91 | 606 | mai 2021 (TH/Versions) | `TH/Versions/… mai 2021.tex`, l. 1884 | le texte corrompu, la route de Willems, le porcelet et la glose τὴν θυγατέρα |
| 939-42 | 518 | août 2021 | `GCA/… aout 2021.tex`, l. 5218 | les corbeaux : Hésychius, jeux de mots, première rédaction |
| 855-7 | 348 | août 2021 | `GCA/… aout 2021.tex`, l. 4719 | λευκῆς Αἰγύπτου, les crues du Nil, la syrméa, première rédaction |
| 49-50 | 196 | décembre 2021 | `GCA/… decembre 2021.tex`, l. 698 | objections à la correction πρόμος (confusion Α/Ο, hapax) ; πρηνίζει : première rédaction |
| 178 | 156 | décembre 2021 | `GCA/… decembre 2021.tex`, l. 1380 | κοινῇ / καινῇ : la scholie et la Souda (Κοινολογία) |
| 894 | 152 | 3 août 2020 | `GCA/copie 3 aout 2020.tex`, l. 3768 | ἐπὶ κλοπῇ τοῦ χρυσίου : les bijoux aux cérémonies, *Lysistrata* 1189-1193 |
| 1-10 | 149 | novembre 2022 (Drive) | `GCA/… nov 2022.tex`, l. 440 | ouverture de la pièce : les sentences d'Euripide et la surdité de Mnésiloque |
| 7-8 | 121 | avril 2021 | `GCA/… avril 2021.tex`, l. 407 | seconde amphibologie du dialogue initial |
| 246 | 110 | mai-juin 2020 | `TH/ttc.tex`, l. 1247 | αἰθὸς γεγένημαι : Souda αι 134-135 |
| 1 | 105 | novembre 2022 (Drive) | `GCA/… nov 2022.tex`, l. 453 | Hirondelle avec un H majuscule : l'étoile de Clements |

**Brouillons que n'imprime aucun état** (type `brouillon commenté (2023)`, 146 lignes dont 128 jamais actives) : avant tout la grande
pile de la ligne 3602 du second fichier, sources copiées pour le dossier de κημός et Κόννου ψῆφον (*Guêpes*, scholies, Souda, Hésychius :
18 lignes, 4 121 mots, dont 3 354 de textes grecs) avec quelques remarques rédigées ; et des pages rédigées restées en `%` : 1069 (διαλάμπειν, 330 mots, l. 4356),
35-38 (βεβίνηκας, 350 mots, vol. 1, l. 821), 1172-5 (κἀνακάλπασον, 375 mots, l. 5102-5120), 1197-8 (†αὐτοῖς†, 300 mots, l. 5317-5337),
le dossier Mnésiloque (l. 526 du vol. 1). Les conjectures commentées qui n'ont pas de forme active (31 ἀγαθῶν;, 639-40, 1082 ὀλόφυγ᾽)
figurent au tableau des conjectures ci-dessus.

**Apparat à rétablir.** Les corrections imprimées sans entrée d'apparat (417, 481, 537, 542, 798, 808, 1014 : § 11.1) sont dans le
tableau, avec leur ligne commentée quand elle existe. Les entrées « disparues » sont surtout des corrections ponctuelles, des
indications sur la tradition indirecte et sur les signes de changement de personnage dans R : elles pèsent peu une à une, mais
une édition de référence aura à les reprendre, après vérification sur l'image de R et sur les éditions.

**Introduction, Annexes, Index** : partir des fichiers de `GCA/` (§ 9), et non des copies de `latex/`.

## 11. Anomalies relevées

Le rapport complet est dans `anomalies.tsv` (189 anomalies : code, gravité, groupe, vers, fichier, ligne
source, message ; 22 codes). On distingue ci-dessous les fautes ou incohérences du travail de l'auteur, à corriger ou à
trancher dans la nouvelle édition (§ 11.1), et les conventions de numérotation, qui ne sont pas des fautes
(§ 11.2). Les décomptes « info » (étiquettes `%% v.` divergentes entre pages grecque et française : 72 ;
alignements par longueurs : 13) relèvent du contrôle de l'extraction.

### 11.1 Fautes et incohérences

- **vv. 3-4 transposés sans note** (gravité « grave ») : le texte grec imprime 1, 2, 4 (παρὰ σοῦ
  πυθέσθαι…), 3 (οἷόν τε, πρὶν τὸν σπλῆνα…), depuis l'état « juin 2022 » (les états antérieurs ont l'ordre usuel). R donne l'ordre usuel (vérifié sur
  l'image du f. 162v, où on lit d'ailleurs οἷόν τι, conformément à l'apparat « τι R : τε ») ; la
  traduction suit l'ordre usuel ; l'apparat (« 3 τι R ») et le commentaire de 1-4 (« παρὰ σοῦ πυθέσθαι
  (v. 3) ») se contredisent. Interversion accidentelle ou choix non justifié : à rétablir selon R.
- **Glose entre accolades sans apparat** : v. 828 { ἐν ταῖς στρατιαῖς } (§ 6).
- **Corrections imprimées sans mention dans l'apparat de 2023** (l'entrée de 2022 a été commentée) :
  417, 481, 537, 542, 798, 808, 1014 (§ 10.3) ; à rétablir dans un apparat complet.
- **Apparat** : deux segments rattachés au mauvais vers (`\ligneApp{374}` pour Τιμόκλει᾽, vers numéroté 373
  dans le texte : numéro de Hall–Geldart ; `\apparat{435}` pour δεινότερον, vers 436) ; cinq numéros de
  vers saisis en gras au lieu de `\ligneApp` (135, 169, 179, 581, 658) ; graphies fautives de noms
  d'éditeurs (« Mugrave » pour Musgrave, 1041 ; « Gryaneus », « Gryaneaus », 501 et 733 ; « Daubruz »,
  352 ; « Bizet », 1013 ; « van Velsen », 1176).
- **Notes du commentaire** : appels `\marqueur` répétés dans 7 articles (49-50, 61, 161-3, 365-6, 826,
  839, 1175) ; 5 notes sans appel (134-5, 248, 365-6, 556-7, 943-56) et 5 appels sans note active (248,
  494, 518-9, 556-7, 1151 : la note a été commentée, l'appel est resté) ; au v. 365-6, la seconde partie
  du commentaire forme un article sans plage ni lemme dont les notes (6 à 14) n'ont pas de `\debutNote`
  (14 anomalies `note_sans_debutNote`) ; deux `\debutNote` dont la plage diffère de celle du commentaire
  (943-56 / « 943-56. » ; 1150-53 / 1150-3).
- **Plages de commentaire décalées** : sur 223 commentaires à plage brève dont le lemme a pu être
  cherché dans le texte, 4 ne portent pas le numéro de la ligne où se lit leur lemme : 193 (lemme du
  v. 194), 376-7 (lemme des vv. 375-376 : numérotation de Hall–Geldart restée dans la plage), 619 (lemme
  du v. 620), 1082 (ὀτότυζ᾽, imprimé sur la ligne du v. 1081 ; voir ci-dessous).
- **Vv. 1081-1084 (scène d'Écho)** : le grec place les deux ὀτότυζ᾽ sur la ligne du v. 1081
  (`\ligne{1081}`), mais le commentaire les numérote 1082 et le texte poursuit par οὖτος τί λαλῖς (1083)
  et πρυτάνεις καλέσω (1084) ; or Hall–Geldart et Wilson (apparat « 1082 λαλῖς ») comptent οὖτος τί
  λαλῖς pour le v. 1082, et l'auteur lui-même renvoie aux « vv. 1082 et 1087 » pour λαλῖς dans l'apparat du
  v. 1109. Les numéros 1082-1084 sont à revoir (concordance rétablie au v. 1085).
- **Étiquettes `%% v.` périmées** : six groupes dont l'étiquette ne correspond pas au premier vers (504 :
  « v. 520-530 » ; 528 : « v. 520-5308 » ; 612 ; 668 ; 712 ; 916a) ; sans effet à l'impression.
- **Numérotation** : sept `\ligne{n}` donnent à un vers le numéro du vers précédent (113, 117 — contredit
  aussi par l'apparat —, 119, 264, 739, 758, 759) : reledmac compterait ces lignes une unité trop bas
  (l'extraction rétablit le numéro et le signale dans `methode_vers`) ; le second fichier commence sans
  `\ligne` (compilé seul, il serait numéroté à partir de 1 ; l'extraction enchaîne la numérotation) ; le
  premier fichier, intitulé « vv 1-641 », s'arrête au v. 638.
- **Personnages** : la page française omet le nom du locuteur dans deux groupes (vv. 663-666 : second
  Coryphée, Chœur).
- **Saisie** : v. 330 saisi avec la macro française `\chantChoeurFr` (indentation du français) ; coquille
  « (ll court vers l'entrée de l'orchestre.) » pour « Il », v. 1222b de la traduction.
- **Conspectus** : P. Oxy. 3839 fr. 2 est donné pour les vv. 941-953 dans l'Introduction et dans les
  Annexes ; le fragment contient les vv. 941-956 (voir `recherche/papyrus.md`).
- **Index** : l'« Index des corrections proposées » est antérieur à la version de 2023 et incomplet (§ 5.4).

### 11.2 Numérotation : conventions, non fautes

Onze numéros de 1 à 1231 ne portent aucune ligne : 23 et 500 (vers supprimés, « del. » retenu dans
l'apparat : Willems, van Herwerden) ; 298 et 308 (absents aussi de Hall–Geldart : la prière 295-311 est en
prose et sa numérotation est conventionnelle) ; 1158 (absent aussi de Hall–Geldart ; Wilson numérote 1158 la
ligne ⟨καὶ⟩ νῦν ἀφίκεσθ᾽…, que l'auteur numérote 1159, avant 1160 chez l'un comme chez l'autre) ; 723,
1018, 1028, 1082, 1138 et 1143,
que l'auteur saute par un `\ligne{n}` explicite dans des parties lyriques : sa colométrie réunit sur une
ligne ce que la numérotation usuelle compte pour deux (par exemple φάνηθ᾽ ὦ τυράννους στυγοῦσ᾽ ὥσπερ
εἰκός, numéroté 1144, qui vaut 1143-1144), puis il recale ses numéros sur l'usage (1082 fait exception,
voir § 11.1). Douze lignes valent deux numéros (`vers_fin` de `texte_grec.tsv`, déduit de `\decoupeVers`,
de l'apparat ou du `\ligne` suivant : 115-116, 357-358, 434-435,
675-676, 681-682, 684-685, 822-823, 913-914, 959-960, 1026-1027, 1150-1151, 1152-1153). Les 28 séries
d'écarts avec Hall–Geldart (`numero_diff_HG`) tiennent pour l'essentiel à Hall–Geldart, dont la
numérotation diverge de l'usage moderne dans les parties lyriques et aux vv. 372-379 (Hall–Geldart n'a pas
de v. 372) : aux repères contrôlés sur l'OCT de Wilson (372-380, 724-726, 1015-1019, 1025-1030, 1080,
1085-1090, 1135-1145, 1155, 1160), l'auteur concorde avec Wilson. La nouvelle édition peut donc reprendre la
numérotation de l'auteur, qui est la numérotation usuelle, en corrigeant les vv. 1081-1084 et en vérifiant
les parties lyriques sur une édition moderne.
