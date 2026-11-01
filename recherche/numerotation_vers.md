# Numérotation des vers des *Thesmophories* — systèmes, concordance, recommandation

> État : **complet** (1er nov. 2026). Données : `edition/donnees/concordance_vers.tsv` (une ligne par vers usuel,
> une colonne par édition, incipit, notes) ; relevé des numéros imprimés : `edition/donnees/concordance_marges.tsv` ;
> conversion : `outils/controle/concordance.py` (`--verifier` pour les contrôles) ; intermédiaires, scripts et lectures :
> `.travail/concordance/` (non versionné ; notes de lecture : `notes/lectures.md`).

## 1. Objet et résultat

Le chantier devait lever une contradiction : `edition/folios/*/texte.tex` donne 373 à ἄκουε πᾶσ᾽, 434 à οὔπω ταύτης,
687 à οὐχ ὁρῶμεν γοῦν, 1016 à φίλαι παρθένοι ; le texte de l'auteur et les livrables de recherche donnent 372, 433, 688, 1015.

1. **La numérotation usuelle est celle de Brunck 1783.** Elle compte les lignes de son édition. Les éditeurs suivants ont
   recoupé les parties lyriques en gardant ses numéros : d'où, chez Coulon ou Wilson, plus de lignes que de numéros en certains
   endroits et moins en d'autres. De Brunck à Prato, les numéros imprimés concordent à ±1 ligne, sauf exceptions du § 3.
2. **La colonne `vers` de `texte_grec.tsv` (« auteur ») suit cette numérotation.** Elle ne s'en écarte que par 12 lignes à deux
   numéros et quelques numéros sans ligne (§ 4.2). `texte.tex` ne la suit pas : 84 vers usuels y portent un autre numéro ou un autre
   découpage que chez l'auteur (§ 4.2).
3. **`texte.tex` ne suit pas non plus l'imprimé de Hall–Geldart, mais sa numérisation Perseus** (colonne `vers_HG`). Perseus
   s'écarte de l'imprimé à neuf numéros marginaux (§ 4.3). Le saut de 372 n'existe pas dans l'imprimé : celui-ci n'a en regard
   de ces vers que 370, 375, 379. La mention « numérotation de l'auteur » de `edition/donnees/structure.md` (l. 9) et le
   rapprochement « usuelle (Hall–Geldart) » de `outils/controle/renumeroter.py` sont donc à corriger (§ 5).
4. **Le 375 de Coulon et de Wilson est imprimé une ligne trop haut**, en regard de Λύσιλλ᾽ (374 au compte de leurs propres
   apparats). L'erreur se lit dès Dindorf 1835, puis chez Meineke, Hall–Geldart, Coulon, Wilson. Brunck, Bekker, Enger, Bergk,
   Dindorf 1869, Blaydes, Velsen, van Leeuwen et Prato placent 375 à ἐκκλησίαν.
5. **« Coulon = Wilson » est faux par endroits** : 435 (Coulon à πολυπλοκωτέρας, Wilson à οὐδὲ), 685-689 (οὐχ ὁρῶμεν vaut 688
   chez Coulon et Prato, 687 au compte de Wilson), 305 (lignes de la prose). Wilson suit alors Brunck ou Hall–Geldart.
   Austin–Olson n'a pu être contrôlé que sur l'extrait textuel (§ 7).
6. **Quatre autres systèmes existent** : Kuster 1710 = Bergler 1760 = chiffres entre parenthèses de Dindorf 1835 (+4 à +13 ;
   c'est le « 804 » de Dobree pour 797) ; Invernizi 1794 (+4 à +7) ; Bothe 1830 (−1 à −67) ; Fritzsche 1838 (−1 et −2 entre
   345 et 440 environ).

La recommandation à soumettre à l'auteur est au § 6 : adopter la numérotation usuelle dans `texte.tex`, en plaçant 375 à ἐκκλησίαν.

## 2. Méthode et pages consultées

**Chaîne.** (1) Rendu des pages et OCR tesseract (`grc+eng`). (2) Détection des nombres de marge, puis relecture de la colonne
de marge en chiffres seuls. (3) **Lecture sur l'image** : chaque numéro est découpé et présenté sur une planche-contact, à côté de
sa valeur attendue ; les cases discordantes sont corrigées à la main. 3 705 numéros imprimés ont été lus ainsi, pour 18 séries
(`concordance_marges.tsv`). Les planches ont corrigé des lectures OCR acceptées auparavant : chez Bergk, 465 et non 466 à δίκην,
1090 et non 1096 à ΜΝΗ. μὰ Δί᾽. (4) Alignement de chaque ligne sur le texte Perseus, qui ne sert que de repère de position.
(5) Pour chaque numéro imprimé, vers usuel de la ligne porteuse ; compte des lignes entre deux numéros. (6) Lecture sur montage
multi-éditions des zones décisives (369-380, 430-445, 682-690 : `.travail/concordance/apercus2/`). (7) Contrôle : sur 3 672 numéros
servant d'ancres, 11 ne se retrouvent pas dans la cellule du vers de leur ligne, à ±1 vers près : dix dans la prière en prose, un chez
Dindorf 1869 (726).

**Définition de la colonne `usuel`.** Une ligne par numéro de 1 à 1231. Les débuts de vers sont ceux du texte de l'auteur, contrôlés
sur les numéros imprimés de Coulon et sur son apparat ; `.travail/concordance/usuel_corrections.tsv` donne les cas où le texte de
l'auteur ne suffit pas. Sommerstein 1994 (commentaire : « 372-9 », « 375 at sunrise », « 434 intricate », « 1018-9 ») et
Austin–Olson 2004 (« 372-82 ») confirment ces repères.

**Colonnes du TSV.** `usuel`, `incipit`, `auteur` (`texte_grec.tsv`), `texte_tex`, `hg_perseus`, `hg1907`, `coulon1928`, `wilson2007`, `prato2001`, `velsen1883`, `blaydes1880`, `meineke1860`, `bergk1872`, `dindorf1869`, `enger1844`, `fritzsche1838`, `dindorf1835`, `bekker1829`, `invernizi1794`, `brunck1783`, `dindorf1835_anc` (numérotation ancienne), `bothe1830`, `vanleeuwen1904`, `notes`. L'incipit vient du texte de l'auteur, sinon de Perseus (marque `[HG]`).

**Notation des cellules.** `N` : ligne ou compte de l'édition. `N–M` : le vers couvre deux lignes, ou la ligne vaut deux numéros.
`(N)` : le vers commence à l'intérieur de la ligne N. `~N` : valeur conventionnelle ou approchée. `N*` : un autre numéro est imprimé en
regard (colonne `notes`). `—` : pas de ligne propre pour ce numéro (297-299, 303-304, 308-309, 723, 1138).

| Édition | Fichier local | Pages PDF | Pages imprimées | Numéros lus |
|---|---|---:|---:|---:|
| Kuster 1710 | `ED/1710_Amsterdam_Kuster/kuster1710_extraits_Thesm.pdf` | 44-94 | 474-524 | 12 (sondage) |
| Bergler 1760 | `ED/1760_Leyde_Bergler_Burman_t2/bub_gb_kRH7s1SMeIUC.pdf` | 434-522 | [999]-1087 | 18 (sondage) |
| Brunck 1783 | `ED/1783_Strasbourg_Brunck/aristophaniscom02arisgoog.pdf` | 97-159 | 74-136 | 161 |
| Invernizi 1794 | `ED/1794_Leipzig_Invernizi_t2_texte/comoediaearis02aris.pdf` | 431-522 | [423]-514 | 106 |
| Bekker 1829 | `ED/1829_Londres_Bekker_t1_texte/aristophanouskm03bekkgoog.pdf` | 388-432 | 361-405 | 210 |
| Bothe 1830 | `ED/1830_Leipzig_Bothe1/comoediaebothe03aris.pdf` | 339-422 | IV, [1]-84 | 199 |
| Dindorf 1835 | `ED/1835_Oxford_Dindorf_t2_texte/aristophaniscom06dindgoog.pdf` | 4-41 | [415]-452 | 194 + 164 entre parenthèses |
| Fritzsche 1838 | `ED/1838_Leipzig_Fritzsche/thesmophoriazusa00aris.pdf` | 25-597 | — | 175 |
| Enger 1844 | `ED/1844_Bonn_Enger/bsb10232531.pdf` | 7-211 | 1-205 | 234 |
| Meineke 1860 | `ED/1860_Leipzig_Meineke_t2/aristophaniscom00meingoog.pdf` | 330-427 | — | 237 |
| Dindorf 1869 | `ED/1869_Leipzig_Dindorf_Fabulae/aristophanisfab00dindgoog.pdf` | 130-144 | — | 191 |
| Bergk 1872 | `ED/1867_Leipzig_Bergk_t2/aristophaniscomo02aris.pdf` (= t. II, 1872) | 153-196 | 123-166 | 222 |
| Blaydes 1880 | `ED/1880_Halle_Blaydes/comoediaeblaydes01aris.pdf` | 15-140 | — | 212 |
| Velsen 1883 | `ED/1883_Leipzig_Velsen/aristophanisthe00velsgoog.pdf` | 12-93 | — | 234 |
| van Leeuwen 1904 | `ED/1904_Leyde_van_Leeuwen/aristophanisthe00leeugoog.pdf` | 26-179 | — | 246 |
| Hall–Geldart 1907 | `ED/1907_Oxford_Hall_Geldart_t2_ed2_reimpr/bwb_P9-BTV-995_2.pdf` | 66-110 | — | 239 |
| Coulon 1928 | `.sources/drive/fichiers/Grec/Aristophane/Œuvres complètes/Gec_seulement_…pdf` | 1-56 | 16-71 | 210 |
| Prato 2001 | `.sources/drive/editions_commentaires/Prato_2001_LeDonneAlleTesmoforie.pdf` | 91-221 | — | 243 |
| Wilson 2007 | `.sources/drive/thesmophories/Wilson_2007_OCT_II.pdf` | 71-126 | — | 228 |

`ED/` = `.sources/web/editions/`. « — » : pagination imprimée non relevée ici (voir `recherche/bibliographie_editions.md`).
Sondages sans colonne (lecture antérieure sur image, `notes/lectures.md`) : Brunck, réimpr. Oxford 1810, Dindorf 1825 et Thiersch 1832
concordent avec l'usage ; Tauchnitz 1814 porte le numéro entre parenthèses dans le titre courant.

## 3. Les systèmes de numérotation

| Série | Système (N = numéro de l'édition, U = usuel) | Numéros irréguliers imprimés |
|---|---|---|
| **Kuster 1710 ; Bergler 1760 ; parenthèses de Dindorf 1835** (`dindorf1835_anc`) | numérotation « ancienne » : +4 vers 51, +5 vers 54, +6 de 59 à 124, +7 de 153 à 943, +9 de 951 à 1076, +11 de 1084 à 1139, +12 ou +13 ensuite ; fin vers 1243 | (59), (986) chez Dindorf |
| **Brunck 1783** | origine de la numérotation usuelle ; compte de ses lignes | aucun |
| **Invernizi 1794** | numéros à gauche ; +4 vers 51, +5 vers 55, +6 de 69 à 969, +7 de 983 à 1028, +6 ensuite ; 1235 à οἴκαδ᾽, fin vers 1237 | aucun relevé |
| **Bekker 1829** | usuelle ; +1 à +3 à la fin (1216, 1221, 1225 pour 1215, 1219, 1223) | 181, 216, 261, 379, 409, 441, 554, 559, 569, 574, 614, 626, 634, 694, 786, 831, 859, 924, 1124, 1196, 1216, 1221 |
| **Bothe 1830** | système propre : 0 jusqu'à 120, −1 de 126 à 291, −20 vers 320, −29 de 374 à 439, −35 de 540 à 665, −42 de 727 à 912, −54 vers 1010, −62 de 1102 à 1137, −67 de 1162 à 1212 ; 1165 à τὼ Θεσμοφόρω, fin vers 1167 | aucun |
| **Dindorf 1835** (chiffres simples) | usuelle ; 375 et 740 une ligne trop haut, 210 aussi | 442, 724, 726 |
| **Fritzsche 1838** | usuelle, sauf 345-445 : 360 à ἢ ψηφίσματα (U 361), 365 (U 366), −2 de 372 à 437 (370 à ἄκουε, 375 à καὶ χρηματίζειν), 440 à Ξενοκλέης (U 441), retour à l'usage à 445 | aucun |
| **Enger 1844** | usuelle | 439, 441, 442, 461, 527, 667, 973, 981, 988 |
| **Meineke 1860** | usuelle ; 375 trop haut | 442, 973a, 973b, 981a, 981b, 982 |
| **Dindorf 1869** | usuelle ; 210 trop haut ; numéros repoussés par les vers rentrés (830, 839) | 269, 294, 312, 381, 411, 442, 534, 561, 576, 611, 616, 626, 679, 722, 724, 726, 784, 846, 861, 914, 924, 1079, 1196 |
| **Bergk 1872** | usuelle ; +1 à 100 et 105 (ΕΥΡ. σίγα ; ΧΟΡ. τίνι δαιμόνων) | 96, 181, 256, 271, 411, 442, 536, 786, 829, 856, 982, 1124 |
| **Blaydes 1880** | usuelle | 442, 982 |
| **Velsen 1883** | usuelle ; colométrie propre en 1150-1159 | 96, 181, 256, 271, 442, 611, 829, 859, 926, 982, 1124 |
| **van Leeuwen 1904** | usuelle | 11, 13, 37, 39, 241, 243, 757, 759, 808 |
| **Hall–Geldart 1907** | usuelle aux numéros imprimés ; 375 trop haut ; 1016 à φίλαι (saut de 1014) | 181, 236, 256, 271, 379, 442, 466, 521, 546, 551, 566, 571, 616, 626, 646, 654, 724, 746, 794, 801, 809, 861, 926, 966, 982, 991, 993b, 996, 1016, 1124, 1139, 1144, 1156, 1187b |
| **Coulon 1928** | référence de la colonne `usuel` ; 375 trop haut | 442, 466, 546, 551, 566, 571, 654, 724, 982, 991, 996, 1139, 1156 |
| **Prato 2001** | usuelle, lettres propres dans les parties lyriques ; 375 à sa place | 103a, 103b, 115/6, 324a, 436, 437b, 438, 439a, 439b, 441b, 442a, 459, 460a, 465b, 465c, 466, 521, 664a, 666a, 675/6, 955a, 972a, 972b, 991, 992a, 993a, 996, 1039b, 1048b, 1092a, 1139, 1144, 1156 |
| **Wilson 2007** | usuelle, avec écarts de Coulon aux lieux du § 1 ; transpose 604 après 607 ; 375 trop haut | 442, 466, 521, 544, 564, 571, 603, 607, 654, 966, 991, 994a, 996, 1187b |

La colonne `dindorf1835_anc` repose sur les parenthèses de Dindorf. Elle a été contrôlée sur la marge de Kuster et de Bergler en
30 points, sans écart : 130 à κίθαρίν τε, 335 à ἡμετέραις, 475, 625, 675, 685, 775, 845, 935, 1065, 1075, 1115, 1125, 1135, 1140, 1145, 1155.
Les alias `kuster`, `bergler`, `dobree` et `ancienne` de `concordance.py` y renvoient. Parmi les références de
`recherche/conjectures_sources.md`, seul le « 804 » de Dobree (§ 6, Kaye) est signalé en numérotation ancienne ; les autres citations
de critiques antérieurs à Brunck n'ont pas été passées en revue [à vérifier].

## 4. Zones de divergence

### 4.1 Numérotation usuelle : où les imprimés se séparent

| Zone | Constat sur les imprimés |
|---|---|
| 101-129 | 115-116 sur une ligne (Coulon, Bergk) ou sur deux (Hall–Geldart, Perseus), Prato « 115/6 » ; 102-103 recoupés ; 126-128 différents selon les éditions. |
| 295-311 (prose) | Les numéros sont conventionnels. 300 tombe à καὶ τῇ Κουροτρόφῳ (Brunck, Bekker, Enger), τῇ Κουροτρόφῳ (Coulon), τῇ Γῇ (Meineke, Bergk, Hall–Geldart), καὶ τῷ Ἑρμῇ (Blaydes, Velsen). 305 : τυχηρῶς (Bekker, Enger, Velsen), Ἀθηναίων (Coulon, Meineke, Bergk), πολυωφελῶς (Wilson, van Leeuwen). 310 : ταῦτ᾽ εὔχεσθε (Brunck, Bekker, Enger, Meineke, Coulon), la ligne précédente (Hall–Geldart, Bergk, Blaydes) ou la suivante (Velsen). Cellules notées `~`. |
| 352-371 | Fritzsche dérive (−1). Wilson réunit 369-370 (Ζεῦ… ἡμῖν θεοὺς / παραστατεῖν, 370 à cette ligne). |
| 372-379 | Lignes identiques partout ; seul 375 change de place (§ 1, point 4). Bekker et Hall–Geldart impriment 379 à ἡμῖν ἁπάσαις. |
| 433-442 | Brunck coupe 433 οὐπώποτε ταύτης / 434 ἤκουσα πολυπλοκωτέρας / 435 γυναικὸς οὐδὲ… 435 est à οὐδὲ chez Enger, van Leeuwen, Wilson ; à πολυπλοκωτέρας chez Dindorf 1835, Meineke, Velsen, Hall–Geldart, Coulon. 440 et 442 sont fixes (Enger imprime 439, 441, 442 ; Prato 439a-b, 441b, 442a). Plus de lignes que de numéros chez les modernes. |
| 459-466 | 460a, 465b, 465c chez Prato ; 465 et 466 distincts chez Coulon, Hall–Geldart, Wilson ; 465 à δίκην chez Bergk. |
| 520-530 | Coupes différentes ; 530 à μὴ δάκῃ. Fritzsche imprime 530 sur τὴν παλαιάν (U 529). |
| 655-730 | 663-686 : colométrie variable. 685 : à θεὸς ἀποτίνεται (Brunck : ἀποτίνεται seul ; Dindorf 1835, Dindorf 1869, Enger, Hall–Geldart, Wilson), à ὅτι τὰ παράνομα (Coulon, Prato « 684/5 »). Brunck a une ligne de plus (παραχρῆμά τε τίνεται) : d'où 688 οὐχ ὁρῶμεν, 689 ἆ ἆ. Hall–Geldart et Enger ont une ligne de moins et un numéro sans ligne. 707-725 : 719-720 varient ; 723 sans ligne chez Coulon, 724 imprimé à τάχα δέ chez Coulon et Hall–Geldart. |
| 776-845 | Aucune divergence de compte dans la numérotation usuelle ; numérotation ancienne constante à +7. 829 chez Bergk et Velsen ; 830 et 839 repoussés par des vers rentrés chez Dindorf 1869. |
| 900-1000 | 913-914 sur une ligne chez l'auteur. 959-960 réunis chez l'auteur, séparés ailleurs. 965 à la ligne ἐν ἱερῷ… (Dindorf, Meineke) ou ἄνδρας (Enger) ; 973, 981, 982 varient (973a-b, 981a-b chez Meineke ; 972a-b chez Prato ; 994a chez Wilson ; 993b chez Hall–Geldart et Prato 992a-993a). |
| 1015-1056 | 1015 à φίλαι (Brunck, Velsen, Wilson, etc.), sauf Hall–Geldart (1016 : saut de 1014). 1018-1019 sur une ligne (Coulon, auteur). 1026-1029 recoupés. 1040 à φῶτα λιτομένα (Hall–Geldart, Velsen, Wilson), à πολυδάκρυτον (Coulon). 1039b, 1048b chez Prato. |
| 1081-1084 | 1082 sans ligne chez l'auteur, qui réunit οἴμωζ᾽ et ὀτότυζ᾽ ; Perseus : 1081, 1081b, 1082, 1083 pour 1081-1084 usuels. |
| 1136-1159 | 1138 sans ligne ; 1143-1144 ; 1150-1151 et 1152-1153 sur une ligne ; 1156 à Θεσμοφόρω (Hall–Geldart, Coulon, Prato, Wilson) ; 1155 à cette même ligne chez Meineke ; 1158 sans ligne chez l'auteur. |
| 1214-1231 | Numéros de fin : 1230 à τὼ Θεσμοφόρω (Brunck, Dindorf, Bergk, Blaydes, Fritzsche) ou à ἡμῖν ἀγαθὴν (Meineke, Velsen, Coulon, Prato, Wilson). Bekker dérive de +1 à +3. |

### 4.2 `texte.tex` et la numérotation usuelle

| Usuel | `texte.tex` | Incipit | Remarque |
|---|---|---|---|
| 358-359 | 357-358 | ὅρκους… | suit Perseus |
| 372-378 | 373-379 | ἄκουε πᾶσ᾽… | suit Perseus (§ 4.3) ; 379 réuni à la ligne 379 |
| 433-434 | 434-435 | οὔπω ταύτης… | suit Perseus |
| 438 | 439 | πάντα δ᾽ ἐβάστασεν | suit Perseus |
| 527-528 | 528-529 | | suit Perseus |
| 667 | 668 | | suit Perseus |
| 676-679 | 675-678 | μηδομένους… | suit Perseus |
| 682-689 | 681-688 (685 = 683) | ἔσται… οὐχ ὁρῶμεν, ἆ ἆ | suit Perseus |
| 718-719 | 719-720 | | suit Perseus |
| 724 | 723 | τάχα δέ | Perseus contre l'imprimé (724) |
| 823 | 822 | | ligne double chez l'auteur |
| 913 | 914 | λαβέ με | suit Perseus |
| 1014-1018 | 1015-1019 | ἥξει… φίλαι παρθένοι… | suit Hall–Geldart |
| 1029 | 1030 | | suit Perseus |
| 1049 | 1048 | | suit Perseus |
| 1069 | 1068a | | suit Perseus |
| 1083-1084 | 1082-1083 | οὖτος τί λαλῖς… | suit Perseus |
| 1089 | 1088 | | suit Perseus |
| 1139 | 1138 | παρθένον ἄζυγα | Perseus contre l'imprimé (1139) |
| 1151-1157 | 1150-1155 | ὄργια σεμνὰ… Θεσμοφόρω | Perseus contre l'imprimé (1156) |

S'y ajoutent des cellules `(N)` (23, 116, 500, 612, 960, 1028, 1048, 1082, 1088, 1144, 1158, 1159) : le vers usuel n'y commence pas une
rangée de `texte.tex`. Liste exhaustive : `python3 outils/controle/concordance.py --zones texte_tex usuel`.

Écarts de l'auteur (`auteur`) à l'usage : lignes à deux numéros (115-116, 357-358, 434-435, 675-676, 681-682, 684-685, 822-823, 913-914,
959-960, 1026-1027, 1150-1151, 1152-1153), 1018 et 1028 (numéro suivant), 1082 et 1143 (sans ligne), 1158 (réuni).

### 4.3 Perseus et l'imprimé de Hall–Geldart

Perseus (`.sources/corpus/thesmo_hall_geldart.tsv`) donne un numéro à chaque ligne, alors que l'imprimé n'en donne qu'un sur cinq environ.
Neuf numéros imprimés n'y sont pas reproduits :

| Imprimé (lu sur l'image) | Perseus |
|---|---|
| 440 | 440a |
| 442 | 442a |
| 530 | 530a |
| 724 | 723 |
| 982 | 982a |
| 993b | 993a |
| 1139 | 1138 |
| 1156 | 1154 |
| 1187b | 1187a |

Aux vv. 370-380, l'imprimé donne 370, 375 (Λύσιλλ᾽), 379 (ἡμῖν ἁπάσαις) : quatre unités pour cinq lignes entre les deux derniers.
Perseus saute 372 et réunit 378-379 sous 379, ce qui s'accorde à ces deux chiffres. Citer « 373 Hall–Geldart » pour ἄκουε revient donc à citer
un choix de la numérisation, non un chiffre imprimé. La colonne `hg1907` reprend les rangées Perseus, sauf aux lieux où l'imprimé les
contredit ; elle reste conjecturale entre deux numéros imprimés.

## 5. Numérotation employée par chaque fichier du dépôt

Méthode : pour chaque mention « numéro + mot grec » tombant dans une zone discriminante, on regarde dans quelle numérotation le mot se lit
au vers cité (`.travail/concordance/scripts/numerotation_md.py`, `numerotation_fichiers.py`). Les nombres donnent les occurrences
concordant avec chaque hypothèse ; les listes complètes sont dans `.travail/concordance/resultats/`. Pour le répertoire, la prière 295-311
est exclue et un lemme peut satisfaire plusieurs hypothèses.

| Fichier ou groupe | Numérotation | Fondement |
|---|---|---|
| `edition/folios/*/texte.tex` | Perseus (`vers_HG`) | `outils/extraction/vers_edition.py` ; 1 400 rangées |
| `edition/folios/*/commentaire.tex` | usuelle, surtout | 9 usuelle ; 3 Perseus (f166r 307 ; f166v 373, 376) |
| `edition/donnees/travaux_anterieurs/texte_grec.tsv` | `vers` = auteur ; `vers_HG` = Perseus | colonnes distinctes |
| `edition/donnees/structure.json` et `.md` | `v` = `texte.tex` ; `v_usuel` = usuelle | l. 9 de `structure.md` à corriger |
| `edition/donnees/repertoire_critique/enger1844_*` | Enger, soit l'usuelle | 131 Enger, 141 usuelle, 65 `texte.tex`, sur 174 entrées discriminantes |
| `edition/donnees/repertoire_critique/velsen1883_*` | Velsen, soit l'usuelle | 111 Velsen, 108 usuelle, 67 `texte.tex`, sur 143 |
| `edition/donnees/repertoire_critique/wilson2007_*` | Wilson, soit l'usuelle | 43 Wilson, 50 usuelle, 23 `texte.tex`, sur 54 |
| `edition/donnees/repertoire_critique/prato2001_*` | Prato, soit l'usuelle | 106 Prato, 103 usuelle, 52 `texte.tex`, sur 113 |
| `edition/donnees/repertoire_critique.json` | celle de chaque édition | 59 usuelle, 17 Perseus |
| `edition/donnees/repertoire_decalages.tsv` | écarts au texte Perseus et à `texte.tex` | `outils/repertoire/controle_numerotation.py`, dont la référence n'est pas la numérotation usuelle |
| `edition/donnees/metrique/s*` | rangées de `texte.tex` ; renvois aux autorités en usuelle | mixte : par ex. s14 1/11, s09 40/32, s15 15/21 |
| `edition/folios/folios.json`, `ravennas/segmentation/*.json` | noms de fichiers d'images (bornes) | 678/679 (f170r/v) et 959 (f174r) sont dans une zone où `auteur` ≠ `texte.tex` |
| `recherche/papyrus.md`, `testimonia.md`, `scholies.md` | usuelle (déclarée) | testimonia 8/2 ; papyrus 1/2, où les mentions Perseus sont citées comme telles |
| `recherche/metrique_structure.md` | usuelle (déclarée) ; White en Hall–Geldart | 19/10 |
| `recherche/travaux_anterieurs.md` | auteur = usuelle | 12/7 : les mentions Perseus sont des exemples d'écart |
| `recherche/conjectures_sources.md`, `etudes_thesmophories.md`, `audit_gemini.md`, `monacensis_492.md` | usuelle ou numérotation de l'auteur | 3/0, 1/0, 3/0, 1/0 |
| `recherche/ravennas_dossier.md` | auteur, avec noms de fichiers d'images | 2/2 |
| `ravennas/graphologie/folios/*.md` | majoritairement usuelle, mélange local | f166v 9/1 ; f167v 0/2 (434 οὔπω) ; f175v 1/1 |
| `ravennas/graphologie/chapitres/*.md` | majoritairement usuelle | ch. 4 : 11/3 ; ch. 5 : 0/1 |

Répertoire critique, fichier par fichier (`edition/donnees/repertoire_critique/<édition>_<tranche>.jsonl`) : entrées discriminantes : concordant avec l'usuelle / avec `texte.tex`. La tranche 776-930 n'a aucune entrée discriminante, car `texte.tex` et l'usuelle y coïncident presque partout.

| Tranche | enger1844 | velsen1883 | wilson2007 | prato2001 |
|---|---:|---:|---:|---:|
| 1-155 | 16 : 7 / 6 | 8 : 6 / 6 | 8 : 7 / 6 | 16 : 16 / 14 |
| 156-310 | — | — | 2 : 2 / 2 | — |
| 311-465 | 32 : 26 / 10 | 33 : 25 / 15 | 11 : 10 / 5 | 22 : 22 / 10 |
| 466-620 | 20 : 20 / 4 | 11 : 9 / 3 | 8 : 8 / 2 | 11 : 11 / 2 |
| 621-775 | 19 : 18 / 3 | 23 : 16 / 12 | 7 : 5 / 0 | 14 : 14 / 5 |
| 776-930 | — | — | — | — |
| 931-1085 | 57 : 40 / 37 | 45 : 32 / 27 | 10 : 10 / 6 | 30 : 20 / 15 |
| 1086-1231 | 30 : 30 / 5 | 23 : 20 / 4 | 8 : 8 / 2 | 20 : 20 / 6 |

Conclusion : chaque fichier suit la numérotation de son édition, soit l'usuelle ; aucun ne suit `texte.tex`.

Sans incidence : `recherche/bibliographie_editions.md`, `drive_ressources.md` et `corpus_numeriques.md` ne citent presque pas de vers.

Trois outils emploient des appellations trompeuses, à reformuler quelle que soit l'option retenue :
`outils/repertoire/controle_numerotation.py` (compare à Hall–Geldart et à `texte.tex` sous le nom d'« auteur »),
`outils/controle/renumeroter.py` (« numérotation usuelle (Hall–Geldart…) »), `outils/extraction/vers_edition.py` (prend `vers_HG`).

## 6. Options et recommandation à soumettre à l'auteur

**Option A — numérotation usuelle (`auteur`) dans `texte.tex`.** Elle concorde avec Brunck, Enger, Velsen, Coulon, Prato, les
travaux de 2023 et tous les livrables de recherche. Coût : remplacer 84 numéros ou découpages de `texte.tex`, recalculer `v` dans
`structure.json`, relire les rangées de `edition/donnees/metrique/s*`, reprendre au moins 3 renvois de commentaire (f166r, f166v) et vérifier les
bornes 678/679 et 959. La conversion est mécanique : `texte_grec.tsv` donne le numéro de chaque rangée.

**Option B — garder `texte.tex` tel quel.** Pas de travail immédiat, mais l'édition imprimerait une numérotation qui n'existe dans
aucun imprimé : 373 pour ἄκουε, 1154 pour Θεσμοφόρω. Tous les renvois des livrables, du répertoire critique et de la bibliographie
seraient à convertir, et le lecteur ne pourrait confronter l'édition ni à Coulon ni à Wilson.

**Option C — suivre strictement Wilson 2007 (dernière OCT).** Avantage : citation directe de l'édition de référence internationale.
Inconvénients : il faudrait reprendre son 375 mal placé, son compte de 685-689 et ses lignes de 433-442, et la transposition de 604 ne
convient pas si l'auteur ne l'adopte pas.

**Recommandation : option A.** Quatre points restent à décider par l'auteur :

1. **375** : l'imprimer à ἐκκλησίαν ποιεῖν (Brunck, Enger, Velsen, Prato), en signalant dans l'introduction l'écart de la marge de Coulon et de
   Wilson. Les apparats de ces deux éditions comptent déjà ainsi.
2. **433-442 et 684-689** : garder les lignes actuelles de l'auteur (Coulon, Prato) ; 435 reste alors à πολυπλοκωτέρας et 688 à οὐχ ὁρῶμεν.
   Une note devra indiquer que Wilson compte autrement.
3. **Lignes à deux numéros et numéros sans ligne** : les conserver à la manière de Coulon, ou adopter des lettres à la manière de Prato (103a-b).
   La première solution garde la colométrie de l'auteur ; la seconde évite les trous mais introduit des numéros absents de Coulon et de Wilson.
4. **1081-1084** : rétablir 1082 à ὀτότυζ᾽ comme Coulon et Wilson, ou garder la ligne réunie en la numérotant 1081-1082
   (`recherche/travaux_anterieurs.md`, § 11.1).

Aucun fichier de `edition/folios/`, ni `structure.md`, ni aucun outil n'a été modifié par ce chantier : la décision revient à l'auteur.

## 7. Limites et points à vérifier

- **Valeurs `~`** : 150 à 330 cellules par colonne (16 pour `hg1907`), presque toutes en parties lyriques ou dans la prière. Là, l'édition ne numérote pas ligne à
  ligne, ou le compte des lignes OCR ne tombe pas juste ; la valeur reste exacte aux numéros imprimés voisins, mais elle est conventionnelle entre eux.
- **Zones lues sur montage** : seulement 369-380, 430-445, 682-690 (plusieurs éditions) et 1009-1026 (Brunck), avec des bandes pour les numéros isolés. Les autres zones ont été
  établies d'après les numéros lus et les lignes OCR.
- **Positions `(N)`** : elles dépendent de l'alignement OCR et peuvent être décalées d'un mot, surtout pour Dindorf 1835, Bekker et Invernizi.
- **Invernizi** : 106 numéros lus sur environ 240 ; **Kuster et Bergler** : 30 points de contrôle seulement.
- **Parenthèses de Dindorf** : la colonne ancienne n'est sûre qu'aux 164 numéros imprimés ; entre eux, le compte est interpolé (`~`).
- **Fritzsche, zone 345-445** : numéros lus sur l'image, mais lignes en partie perdues par l'OCR (commentaire intercalé) : cellules `~`.
- **Austin–Olson 2004** : le PDF n'est pas encore en local ; seul l'extrait textuel a été consulté (« 372-82 »). À contrôler sur le texte aux vv. 375, 435, 685-689, 1040.
- **Numéros 723, 1018, 1028, 1082, 1138, 1143, 1158** : leur place dans la numérotation usuelle dépend de Coulon (texte et apparat) ; Hall–Geldart et Wilson diffèrent parfois.
- **Second exemplaire de Hall–Geldart** (`ED/1907_Oxford_Hall_Geldart_t2/aristophaniscomo02arisuoft.pdf`) : océrisé, mais non comparé ligne à ligne à la réimpression utilisée ici.
