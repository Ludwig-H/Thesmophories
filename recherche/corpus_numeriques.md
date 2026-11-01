# Corpus numériques de la littérature grecque — couverture, fiabilité, lacunes

*Document de travail du chantier « corpus » (octobre–novembre 2026). Les textes sont dans
`.sources/corpus/` (non versionné) ; les scripts et leur notice dans `outils/corpus/`
([README](../outils/corpus/README.md)). Statistiques : voir § 6 (mises à jour à chaque
reconstruction de l'index).*

Objet : disposer en local d'un corpus aussi large que possible des textes grecs (auteurs,
lexicographes, parémiographes, scholiastes, fragments) et d'un moteur de recherche
(`outils/corpus/chercher.py`) pour **trouver** loci paralleli et testimonia des
*Thesmophories*, puis les **vérifier**. L'index ne remplace jamais l'édition : toute
référence se contrôle sur l'imprimé (ou sur l'image de la page, lien fourni pour l'OCR).

## 1. Méthode

1. Reprise de l'existant après l'interruption : dépôts git complets et propres
   (Perseus, First1KGreek, LSJ, DCLP), Diorisis décompressé (820 fichiers), 20 ouvrages
   OCR d'archive.org intègres (gzip et JSON vérifiés) ; index partiel abandonné et
   reconstruit.
2. Contrôle de la qualité de chaque OCR (part des mots grecs de 4 lettres et plus
   attestés dans les textes TEI) : archive.org n'a souvent appliqué qu'une langue par
   volume, si bien que le grec des volumes « latins » (CPG I, Pollux de Bethe I, Mélanges
   de Miller, Anecdota de Bekker) est du charabia. Ces exemplaires ont été remplacés par
   d'autres numérisations mieux lues, ou réocérisés localement (Tesseract grc+lat).
3. Pages à deux colonnes serrées (Hésychius, Souda de Bekker, Zonaras, scholies de
   Dübner) : l'OCR fusionnait les lignes des deux colonnes ; l'ordre de lecture est
   rétabli d'après les coordonnées des mots (hOCR), puis les lexiques sont découpés en
   articles (référence « col. 199, s.v. ἀπόκυνον »).
4. Index SQLite FTS5 sur 8 processus : texte original + forme normalisée (sans
   diacritiques, minuscules, σ = ς, apostrophes et coronis supprimées) ; jointures entre
   passages consécutifs (expressions à cheval sur deux vers) ; index « souple » de l'OCR
   neutralisant les confusions systématiques (κ lu χ, lettres latines au milieu des mots
   grecs, ς final lu ζ) ; étiquette de fiabilité par œuvre.
5. Polices à encodage propre (éditions De Gruyter composées en Kleinlogel : Hésychius,
   Synagoge) : le texte est rétabli d'après les glyphes, l'OCR ne servant que de contrôle
   (§ 7).

## 2. Corpus disponibles

### 2.1 Textes établis (TEI, numérisations corrigées)

| Corpus | Contenu | Licence |
|---|---|---|
| Perseus, `canonical-greekLit` | 814 éditions grecques (poésie, théâtre complet, histoire, philosophie, orateurs, Athénée de Kaibel avec pages de Casaubon, Harpocration…) | CC BY-SA 4.0 |
| Open Greek and Latin, `First1KGreek` | 1 126 éditions : Souda (Adler, incomplète, voir § 3), CPG I (Zénobius, Diogénien, Plutarque, Grégoire de Chypre, Appendix), scholies (Euripide, Sophocle, Homère, Pindare, Lucien, Nicandre, Isocrate), Hérodien, Ammonius, patristique… | CC BY-SA 4.0 |
| LSJ (Perseus) | Liddell–Scott–Jones, 9e éd., entrée par entrée | CC BY-SA 4.0 |
| DCLP (papyri.info) | papyrus littéraires et paralittéraires (EpiDoc), texte et métadonnées | CC BY 3.0 |
| Diorisis | corpus lemmatisé (10 millions de mots) : table forme → lemme pour la recherche `--lemme` | CC BY 4.0 |

### 2.2 Ouvrages du domaine public, OCR (archive.org ou local)

Liste maintenue dans `outils/corpus/sources_ocr.tsv` (identifiant, sigle, description,
options). Taux = part des mots grecs reconnus (voir § 4).

| Domaine | Ouvrages |
|---|---|
| Lexiques | Hésychius, éd. minor de M. Schmidt (1867), en articles ; Souda, éd. Adler (1928–1938, 5 t. : OCR d'archive.org, page par page, `outils/corpus/adler.py`) et éd. Bekker (1854), en articles ; Photius, éd. Porson (1822) et Naber (1864–1865) ; Pollux, éd. Dindorf (1824, texte complet) et Bethe II (l. VI–X, 1931) ; Etymologicum magnum (Sylburg, réimpr. 1816) ; Zonaras, éd. Tittmann I (1808) ; Lexica Segueriana (Bekker, *Anecdota* I, 1814 : Antiatticiste, Λέξεις ῥητορικαί, Συναγωγή…, OCR local) |
| Parémiographes | CPG I (avec les notes) et II (Leutsch–Schneidewin, 1839–1851) ; Gaisford, *Paroemiographi* (1836) ; Miller, *Mélanges* (1868 : Zénobius de l'Athous) |
| Florilèges | Stobée, *Florilegium* (Meineke, 1855–1857) ; *Anthologium* III (Hense, 1894) |
| Scholies | Dübner, *Scholia Graeca in Aristophanem* (1842) ; Rutherford, *Scholia Aristophanica* I–II (1896 : scholies du Ravennas) ; A. Martin, *Les scolies du manuscrit d'Aristophane à Ravenne* (1882) |
| Fragments | Kock, CAF I–III ; Meineke, FCG I–IV ; Kaibel, CGF I.1 ; Nauck, TGF² (1889) ; Bergk, PLG⁴ II–III (élégiaques, iambographes, méliques, 1882) |
| Éditions, commentaires | Hall–Geldart II (1907) ; Fritzsche (1838) ; Velsen (1883) |

### 2.3 Fichiers du Drive de l'auteur (usage local, sous droits)

`outils/corpus/sources_drive.py` dresse la liste (non versionnée,
`.sources/corpus/sources_drive.tsv`) des fichiers à indexer dans la collection « drive » :
d'une part les ouvrages de référence attendus (présents ou non), d'autre part tout autre
fichier réellement présent (PDF, EPUB, `.txt` sans PDF jumeau), en catégorie « etudes »
(références préfixées « Étude : »). Les doublons exacts (MD5) et les dossiers de travail de
l'auteur sont exclus ; l'indexeur écarte les fichiers sans couche texte exploitable.

- **Hésychius de Latte–Hansen–Cunningham** : les quatre fichiers couvrent tout le lexique
  (Α–Ω) ; texte rétabli et découpé en gloses numérotées, apparats à part (§ 7).
- **Synagoge de Cunningham** : même composition en polices Kleinlogel ; texte rétabli par la
  même table (§ 7.2), mais indexé page par page (l'index du 26 octobre n'en contenait que
  du charabia, taux de 3 %).
- **Photius de Theodoridis, t. III (Ν–Φ)**, Tosi, Bauck, et les études et articles présents.
- Photius de Porson (π–ω, réimpr. 2010) : couche texte inutilisable, écarté ; l'exemplaire
  d'archive.org est dans la collection « ocr ».

## 3. Couverture des fonds prioritaires

| Fonds | Couverture dans l'index | Remarques |
|---|---|---|
| Théâtre (Aristophane, tragiques, Ménandre) | complète (Perseus, textes TEI) | Thesmophories : Hall–Geldart (vulgate de collation exportée dans `.sources/corpus/thesmo_hall_geldart.tsv`) |
| Fragments comiques | Kock (CAF), Meineke (FCG), Kaibel (CGF), OCR | Kassel–Austin (PCG) présent sur le Drive mais non téléchargeable (> 10 Mo) : vérifier les numéros K.-A. sur les éditions papier ou les concordances |
| Fragments tragiques | Nauck, TGF² (OCR) | TrGF (Snell, Kannicht, Radt) : Drive, non téléchargeable |
| Hésychius | **Latte–Hansen–Cunningham, Α–Ω, complet** : 51 231 gloses numérotées, texte de l'éditeur, apparats à part (§ 7) ; éd. minor de Schmidt (1867), en articles (OCR, colonnes rétablies) | le fichier du t. II (1014 p. PDF) n'a que la page de titre du t. IIa, mais contient aussi Κ–Ο (pagination continue, κ 1 = p. 491) : rien ne manque |
| Souda | Adler : First1KGreek (partielle, texte corrigé) et les cinq tomes de l'édition (OCR d'archive.org, page par page, apparat compris) ; Bekker (1854, OCR, en articles) | l'OCR d'Adler n'est pas découpé par article : trouver le numéro sur la page |
| Photius, Pollux, Etymologica, Zonaras, Lexica Segueriana, Synagoge | Theodoridis III (Ν–Φ, Drive) ; Porson et Naber ; Dindorf et Bethe II ; *Etymologicum magnum* (Sylburg) ; Tittmann I ; Bekker, *Anecdota* I (OCR) ; Synagoge de Cunningham (Drive, texte rétabli) | Theodoridis I–II (Α–Μ) absents du disque |
| Parémiographes | CPG I (First1KGreek et OCR) et II (OCR) ; Gaisford ; Miller | |
| Scholies d'Aristophane | Dübner 1842 ; Rutherford 1896 (scholies de R) ; Martin 1882 (OCR) | éd. de Groningue (Regtuit 2007 pour les *Thesm.*) : non disponible |
| Florilèges | Stobée (Meineke ; Hense III) | |
| Papyrus | DCLP (papyri.info) | |

## 4. Fiabilité

Les textes TEI (Perseus, First1KGreek) sont fiables mais non exempts de coquilles (ex. *Thesm.* 4 « πυφέσθαι » chez Perseus). Les OCR sont signalés comme tels par `chercher.py`, avec le taux de mots grecs reconnus et le lien vers l'image de la page : **toute citation tirée d'un OCR doit être vérifiée sur l'image**. L'index « souple » neutralise les confusions systématiques de l'OCR (κ/χ, lettres latines, ς/ζ).

Trois degrés, donc : **TEI** (corrigé, à contrôler sur l'édition) ; **texte rétabli d'après les polices** (Hésychius de Latte–Hansen–Cunningham, Synagoge de Cunningham : texte de l'éditeur, sans erreur de lecture, § 7.3) ; **OCR** (Schmidt, Bekker, Adler, etc. : à vérifier sur l'image). L'OCR d'Adler, de bonne tenue pour un grec à sigma lunaire (84 à 88 % de mots reconnus), reste un OCR : l'apparat y est moins sûr que le texte, et `recherche/testimonia.md` ne doit citer Adler qu'après lecture de l'image (lien fourni).

## 5. Lacunes et pistes

- Éditions de référence présentes sur le Drive de l'auteur mais absentes du disque (limite de l'outil de copie : 10 Mo en principe, 6,3 Mo en pratique ; `recherche/drive_ressources.md`, § 9) : Kassel–Austin, TrGF, Photius de Theodoridis t. I–II (Α–Μ), Pollux de Bethe, volumes de scholies de Groningue. Si l'auteur les rend accessibles (partage par lien ou accès `rclone`), relancer `sources_drive.py` puis `indexer.py`. Les scholies aux *Thesmophories* de l'édition de Groningue (Regtuit 2007) ne figurent pas à l'inventaire du Drive. **Correction de la première version de ce document**, qui disait Latte et Theodoridis « non téléchargeables » : l'Hésychius de Latte–Hansen–Cunningham est sur le disque au complet, et le t. III (Ν–Φ) de Theodoridis aussi (`recherche/drive_ressources.md`, § 4.1, qui tient lui-même à tort le t. IIb, Κ–Ο, pour absent : voir § 3 et § 7.1).
- Numérotations : citer les lexiques dans la numérotation de l'édition de référence (Latte pour Hésychius α–ο, Schmidt pour π–ω, numérotation reprise par Hansen et Cunningham : § 7.1 ; Adler pour la Souda, Theodoridis pour Photius α–φ) ; pour Hésychius l'index la donne directement ; ailleurs il donne souvent celle d'une édition ancienne (Bekker) : convertir avec prudence. Attention : pour α–ο, les colonnes de l'éd. minor de Schmidt indexée (OCR) ne donnent pas le numéro de Latte.

## 6. Statistiques de l'index et tests

Index reconstruit le 1er novembre 2026 en 676 s sur 6 processus : **4 314 œuvres, 918 730 passages, 54,1 millions de mots** ; base `.sources/corpus/index.sqlite` (2,1 Go ; construite dans `index.sqlite.tmp`, puis renommée). Le 26 octobre : 4 188 œuvres, 817 823 passages, 49,2 millions de mots.

| Collection | Œuvres | Passages | Mots |
|---|---:|---:|---:|
| Perseus | 814 | 290 914 | 10 586 934 |
| First1KGreek | 1 126 | 257 858 | 23 472 228 |
| OCR (dont Adler, 5 tomes, 3 067 pages, nouveaux) | 40 | 138 990 | 10 007 807 |
| Drive | 125 | 100 953 | 4 812 888 |
| LSJ | 1 | 116 497 | 4 380 805 |
| DCLP | 2 208 | 13 518 | 791 617 |

Collection « drive » (4 œuvres le 26 octobre, 125 aujourd'hui) :

- Hésychius de Latte–Hansen–Cunningham : 8 œuvres ; gloses, 51 351 passages (dont 121 pages liminaires), 393 882 mots, taux de mots reconnus 85 % ; apparats, 40 646 passages, 612 737 mots, 62 à 70 %.
- Synagoge : 765 pages, taux de mots reconnus passé de **3 % à 93 %** par le rétablissement des polices. Photius de Theodoridis III (92 %), Tosi, Bauck, inchangés.
- Études et articles (catégorie « etudes ») : 113 fichiers, 5 843 pages. Le dossier du Drive n'a reçu aucun fichier depuis le 26 octobre à 13 h 16 (date du dernier arrivé, l'EPUB d'Érasme, désormais indexé) ; ces fichiers étaient là, mais hors des règles de `sources_drive.py`.
- Écartés, faute de couche texte exploitable : 9 fichiers, soit 8 images (Sommerstein, *Acharniens*, *Cavaliers*, *Guêpes*, *Paix* ; Boissonade ; extrait de Wilson ; *Eikasmos* VII ; Blanc–Taillardat sur *Thesm.* 366) et Photius de Porson (OCR latin). 48 ouvrages de référence attendus restent absents du disque (§ 5).

Souda d'Adler (OCR d'archive.org) : taux de mots reconnus de 84 à 88 % (index du t. V : 80 %). Pages contrôlées sur les numéros de page d'archive.org (t. I, II, IV, V) et sur les titres courants (t. III, doubles pages séparées).

Tests (`outils/corpus/tester.py`, à relancer à chaque reconstruction) : **13 sur 13**, dont « Νείλου μὲν αἵδε καλλιπάρθενοι ῥοαί » (Eur. *Hel.* 1, *Thesm.* 855), « σοφοὶ τύραννοι » (Aristide 46, 288 ; Platon, *Théagès* 125b ; *Rép.* 568b intercale εἰσι et n'est pas trouvée comme expression), « πυθοῦ χελιδών » (Harpocration s.v. ἄττα, CPG, Fritzsche, Kock), « ἀπόκυνον » (Schmidt, Latte), χοάνη = Hsch. χ 576, ἀϋτή = Hsch. α 8382, κάμπτειν = Hsch. κ 617, Synagoge (p. 95), Adler (t. I, p. 171). Deux attentes périmées de l'ancien jeu de tests ont été rectifiées : ὀρθρογόη n'est pas dans Hésychius (mais dans Photius et la Souda), et l'abréviation du *Théagès* est `Pl. Thg.`.

## 7. Hésychius de Latte–Hansen–Cunningham (texte rétabli, gloses numérotées)

*Chantier des 28 octobre et 1er novembre 2026. Script : `outils/corpus/ocr_hesychius.py`
(sous-commandes `ocr`, `decoder`, `gloses`, `qualite`, `tester`, `echantillon`, `voir`).
Résultats, non versionnés car tirés d'éditions sous droits : `.sources/corpus/hesychius/`.*

### 7.1 Fichiers et couverture

Les fichiers (`.sources/drive/fichiers/Grec/Lexiques/Hesychius/`, jamais versionnés) couvrent
**tout le lexique, Α–Ω**. Contrairement à ce qu'on a cru d'abord (et à ce que dit encore
`drive_ressources.md`, § 4.1 et § 9.1), rien ne manque : le fichier du t. II n'a que les pages
de titre du t. IIa (Ε–Ι), mais il contient aussi tout Κ–Ο (κ 1 = p. 491, p. 503 du PDF ;
pagination continue jusqu'à ο 2109, p. 1000).

| Tome | Lettres | Édition | Pages du PDF | Page = PDF − | Gloses (entrées) |
|---|---|---|---|---|---|
| I | Α–Δ | K. Latte, 2e éd. I. C. Cunningham, De Gruyter, 2018 (SGLG 11/1) | 698 | 38 | 14 301 |
| II | Ε–Ο | K. Latte, 2e éd. I. C. Cunningham, 2020 (SGLG 11/2) | 1 014 | 12 | 23 016 |
| III | Π–Σ | P. A. Hansen, 2005 (SGLG 11/3 ; deux copies identiques) | 440 | 34 | 8 280 |
| IV | Τ–Ω | P. A. Hansen et I. C. Cunningham, 2009 (SGLG 11/4) | 313 | 32 | 5 634 |

Soit **51 231 entrées** (numéros suffixés et numéros groupés compris, « vacat » compris) pour
2 465 pages. **Deux numérotations**, qu'il ne faut pas confondre :

- **α–ο (t. I–II) : numérotation de Latte**, qui a renuméroté tout le lexique et que la 2e édition
  garde (« The numbering of the glosses is unchanged, occasional errors being noted » : Cunningham,
  t. I, Prolegomena § VII, p. XII) ;
- **π–ω (t. III–IV) : numérotation de M. Schmidt** (editio maior), conservée telle quelle par Hansen
  et Cunningham (t. III, p. XXXI, n. 5 ; t. IV, Prolegomena, p. XVI) : les suffixes *a, b, c* sont de
  Schmidt, *x, y, z* des éditeurs ; un numéro sans glose porte « vacat » ; les écarts d'ordre sont
  expliqués dans l'apparat (ainsi τ 142, 141). Une référence π–ω se lit donc aussi dans Schmidt.

Derniers numéros : α 9002, β 1410, γ 1046, δ 2765, ε 7757, ζ 269, η 1038, θ 1032, ι 1214, κ 4905,
λ 1541, μ 2078, ν 818, ξ 204, ο 2109, π 4524, ρ 600, σ 3115, τ 1763, υ 961, φ 1142, χ 883,
ψ 327, ω 531. Les pages données pour les t. I et II sont celles de la 2e édition, et le libellé
« Latte I », « Latte II » de la référence désigne cette édition révisée. L'astérisque signale les
gloses tirées du lexique de Cyrille ; les sigles qui les suivent (`vg8Br9`, `AS110`…) renvoient à ses
manuscrits (t. I, p. XII).

### 7.2 Méthode

1. **OCR.** Pages rendues à 400 dpi en niveaux de gris (ces PDF n'ont aucune image), Tesseract 5
   (grc+lat, `--psm 4`), 8 processus, reprenable page par page (`ocr`) : 2 465 pages, 1 030 580 mots,
   conservés avec boîtes et confiance dans `ocr/`. L'OCR sert de **contrôle**, non de texte.
2. **Décodage de la couche texte.** Elle n'est pas perdue : les polices Kleinlogel (Type 1/CFF)
   portent des noms de glyphes brouillés (le glyphe « epsilongrave » est un β, « alpha » le point
   en haut, « nonbreakingspace » un ἠ…), mais le lien nom → dessin est constant dans les cinq PDF
   de ces éditions (Hésychius I, II, III, IV ; Synagoge), ce que prouve l'empreinte des contours
   (recalculée le 1er novembre, sous-programmes résolus : 1 627 couples famille-nom, un seul
   contour pour chacun). D'où une table nom → caractère
   (`outils/corpus/kleinlogel.tsv`, 233 entrées, sans aucun texte des éditions), proposée par le
   vote de l'OCR aligné sur les glyphes puis contrôlée glyphe par glyphe sur l'image, et un module
   (`outils/corpus/kleinlogel.py`) qui réécrit en mémoire le /ToUnicode des polices et rattache à
   leur lettre les signes superposés (iota souscrit, brève, tréma, point souscrit, trait suscrit).
   Le texte obtenu est celui de l'éditeur, accents et esprits compris. Les 2,39 millions de
   glyphes Kleinlogel des quatre tomes ont tous une valeur dans la table (dénombrement de tous
   les glyphes de toutes les pages).
   Corrigé le 1er novembre : le glyphe « three » n'est pas un ϋ, mais le tréma seul (contour limité à
   la hauteur des points) : « ἀ ϋυτή » → ἀϋτή.
3. **Découpage en gloses** (`decoder`, `gloses`). D'après la mise en page : numéro en gras en tête de
   glose, signes de source dans la marge (`D`, `Hom.`, `Ap. S.`…), corps et deux filets séparant
   texte, testimonia et apparat critique. PyMuPDF morcelant les lignes (numéro, texte, demi-crochets
   et exposants à part), les fragments sont regroupés en lignes visuelles avant lecture ; sans cela le
   texte d'une glose passait à la précédente et les notes d'apparat changeaient de numéro. Sont
   traités : numéros de ligne des longues gloses (écartés), césures, notes communes à plusieurs
   gloses, numéro groupé (« 710/11 »), iota souscrit resté sur le fragment précédent, lettres latines
   et grecques de même dessin confondues par la composition (« Bερενικίδες », « Ηerod. », « (H 316) »).
4. **Index.** Une œuvre « gloses » et une œuvre « apparats » par tome, dans la collection « drive »
   (forme de recherche : signes éditoriaux retirés à l'intérieur des mots ; pas de pliage OCR, le
   texte n'en ayant pas besoin). Référence : « Hsch. χ 576 (Hansen–Cunningham IV, p. 223) » ; le
   signe de la marge s'affiche à sa suite. `ocr_hesychius.py voir χ 576` donne apparats et image.
   Les pages liminaires (prolégomènes, sigles, lettre à Eulogios) sont indexées page par page.

### 7.3 Qualité

*Sur le texte indexé (`qualite.json`, sous-commande `qualite`).* Taux de mots grecs reconnus =
part des mots grecs de 4 lettres et plus attestés dans les textes TEI (même mesure qu'à l'indexation,
848 076 formes), sur les pages entières, apparats compris :

| Mesure | t. I | t. II | t. III | t. IV |
|---|---:|---:|---:|---:|
| mots grecs (4 lettres et plus) lus par l'OCR | 66 656 | 104 766 | 43 060 | 25 970 |
| taux de mots reconnus, **OCR** | 76,1 % | 76,4 % | 77,1 % | 77,3 % |
| mots grecs du texte décodé | 70 654 | 112 717 | 46 046 | 27 840 |
| taux de mots reconnus, **texte décodé** | 79,6 % | 79,7 % | 79,4 % | 80,8 % |
| mots décodés retrouvés tels quels dans l'OCR de la page | 87,4 % | 85,5 % | 87,4 % | 85,7 % |
| parmi eux, diacritiques identiques | 98,0 % | 98,3 % | 98,6 % | 98,0 % |

Lecture. Le taux n'est pas ici une mesure d'erreur : même exact, le texte d'Hésychius plafonne vers
80 %, parce qu'un lexique est fait de mots rares, absents des textes TEI (85 % sur les gloses seules,
62 à 70 % sur les apparats, qui citent les leçons corrompues du manuscrit). L'OCR seul fausserait
13 à 15 % des mots grecs et ne doit pas tenir lieu de texte : il est conservé comme témoin
indépendant. Le texte de référence est le texte décodé.

*Échantillon contrôlé sur l'image* (`echantillon`, graine 20261101) : **60 gloses tirées au sort**,
réparties selon les tomes, lues une à une sur planches à 230 dpi contre le texte décodé :
**60 conformes** (lettres, accents, esprits, iota souscrits, signes critiques, sigles, références).
Un seul écart, de pure typographie, corrigé depuis : traits suscrits de ν̅α̅ (κ 4462) reportés sur une
seule lettre. Apparats : trois pages relues sur l'image (t. I, p. 588 ; t. III, p. 201 ; t. IV, p. 164,
soit environ 80 notes), conformes, une fois réglés l'ordre des fragments et les césures.

*Numérotation et pagination.*

- Tous les numéros de 1 au dernier sont présents dans chaque lettre, sauf **κ 183** : l'imprimé passe
  de 182 à 184, alors que l'apparat a une note 183 (`κατοπτρον Kc`). La glose manque à l'édition, non à
  l'extraction (vérifié sur l'image et par l'OCR).
- Les titres courants (premier et dernier numéro de chaque page) concordent sur les 2 331 pages qui
  en ont un : 2 328 strictement ; les 3 autres sont des titres fautifs ou de forme particulière de
  l'imprimé (φ « 3–1076–3–1096 », χ « 465–6–481 », ω « 531–15 »). Le décalage page du PDF → page
  imprimée est constant sur chaque tome.
- 47 ruptures de la suite (`anomalies.tsv`) : κ 183, et 46 ruptures dues à 16 gloses que Hansen et
  Cunningham impriment hors de l'ordre numérique, en gardant le numéro de Schmidt (t. III–IV : π 208
  avant π 206, τ 142 avant τ 141…) ; « variations in the order are explained in the apparatus » (t. IV,
  p. XVI). Ordre vérifié dans l'imprimé, sur l'image et par l'OCR.
- Corrections : coquilles de numéros (α 3078, α 3600, ε 4171, κ 4072 ; apparat : α 7472/3, λ 520/521) ;
  η 66, dont le numéro manque à l'impression (la ligne y est, et l'apparat le donne) ; κ 1941, numéro
  entre crochets sans texte (glose absente de H, ajoutée par Latte dans l'apparat). Une note d'apparat
  n'a pu être rattachée à une glose précise (t. II, p. 177, « 4387–4485 », transposition de colonnes).

*Limites.* Exposants aplatis (`IG 13` pour *IG* 1³, `vg8Br9`) ; signes éditoriaux conservés dans le texte
affiché ; une quinzaine de capitales à esprit fautif dans l'imprimé, gardées telles quelles (« ʹΕρμῆς »,
« ᾿Ράριον ») ; 175 entrées sans lemme séparé (*vacat*, gloses sans point en haut), citables par leur
numéro ; le numéro d'une note d'apparat suit l'imprimé même quand elle touche plusieurs gloses.
**Comme pour tout le corpus, on ne cite qu'après contrôle sur la page** : `ocr_hesychius.py voir χ 576`.

### 7.4 Tests

- **Gloses attendues** (`ocr_hesychius.py tester`) : 11 sur 11, dont **χ 576 = χοάνη** (« χοάνη· χώνη,
  τύπος, εἰς ὃν μεταχεῖται τὸ χωνευόμενον (Ar. Thesm. 18) », Hansen–Cunningham IV, p. 223) et les cas
  difficiles (π 205 et π 208 transposées, λ 403, λ 415, η 66, α 8382, α 2626).
- **Références de `recherche/testimonia.md`** : 74 références à Hésychius, confrontées glose par glose
  (`controle_testimonia.tsv`) : **73 fois le lemme cité est bien à ce numéro**, 1 fois sous une autre forme
  (κ 4747, κύτταροι pour κύτταρον). Les 16 références κ–ο que `testimonia.md` marque « non contrôlé »
  ou « vol. II absent » sont ainsi toutes confirmées : κ 472, 617, 1980, 2549, 3218, 3232, 3629, 3865,
  4087, 4691, 4747 ; λ 225 ; μ 224, 1904 ; ο 265(-266), 852.
- **Gloses que l'édition rapporte aux *Thesmophories* et que `testimonia.md` ne relève pas : 25**
  (`thesmophories_hors_testimonia.tsv`, à intégrer au chantier des testimonia après contrôle).
  Dans le texte des gloses (16) : α 612 (v. 533), α 835 (115), α 3763 (159), δ 599 (237), π 682 (370 ?),
  π 2470 (772), π 2839 (1040), ρ 548 (108), σ 844 (387), σ 884 (834), σ 2044 (638), σ 2136 (1197, 1215),
  σ 2841 (486), τ 730 (449), τ 890 (543), φ 781 (813). Dans les apparats (9) : α 263, α 1906, α 5234,
  γ 177, θ 765, ι 1132, π 2338, σ 158, τ 1388.
- **Index** (`outils/corpus/tester.py`) : 13 sur 13 (§ 6). `chercher.py 'χοάνη' -a Hsch. -o gloses` rend
  « Hsch. χ 576 (Hansen–Cunningham IV, p. 223) [D] » et λ 966 ; `chercher.py Thesm -a Hsch. -o gloses`,
  les 55 gloses où l'édition renvoie aux *Thesmophories* ; `-a 'Hsch. app.'`, les 19 notes d'apparat.
