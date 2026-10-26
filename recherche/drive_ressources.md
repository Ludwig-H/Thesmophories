# Ressources documentaires locales (`.sources/drive/`) — synthèse par usage

> **État** (26 octobre 2026, seconde reprise) : document complet (§ 0 à 9). Les fichiers locaux ont été recontrôlés le 26 au soir : aucun nouveau fichier depuis la reprise précédente (les derniers arrivés, Hésychius et Érasme, sont intégrés au § 4), aucun fichier altéré en dehors du cas signalé au § 8.3. Restent ouverts, faute d'accès aux fichiers eux-mêmes, les points marqués [à vérifier] ou [à identifier] (une douzaine, surtout au § 9.2).

## 0. Conventions

- **Emplacement.** Tous les fichiers décrits ici sont dans `.sources/`, que git ignore (ouvrages sous droits : ne jamais les déplacer dans la partie versionnée). Abréviations de chemins :
  - **`D/`** = `.sources/drive/` (sous-dossiers `ravennas/`, `editions/`, `papyrus/`, `thesmophories/`, `textes/`, `textes_metrique/`) ;
  - **`F/`** = `.sources/drive/fichiers/` ;
  - **`AR/`** = `F/Grec/Aristophane/` ;
  - **`TH/`** = `AR/Thesmophories/` ;
  - **`GCA/`** = `TH/Grec - commentaire - traduction - apparat/` (dossier de travail de l'auteur).
- **Noms de fichiers.** Les noms longs ou porteurs de mentions parasites sont abrégés par un motif shell (`*`). Mettre les chemins entre guillemets (espaces, apostrophes, `||`, `:`).
- **Interrogeable ?** **[T]** = couche texte correcte (un `.txt` du même nom est à côté du PDF ; `grep` possible) ; **[T-]** = couche texte présente mais médiocre (OCR fautif, grec mal reconnu) ; **[I]** = image seule (lecture sur l'image ou OCR à faire) ; **[S]** = source texte native (`.tex`, `.xml`, `.txt`) ; **[X]** = extrait textuel partiel d'un ouvrage dont le PDF n'est pas disponible localement.
- **Pages.** « p. » = pagination imprimée ; « p. PDF » = rang de la page dans le fichier.
- **Identification.** Chaque notice a été établie en ouvrant le fichier (page de titre, en-tête d'article, couche texte, rendu d'images). Les noms de fichiers sont souvent trompeurs (voir les cas signalés) : ne pas s'y fier. Ce qui n'a pas pu être contrôlé est marqué **[à vérifier]**.
- **Doublons.** Une ressource présente en plusieurs exemplaires identiques n'est décrite qu'une fois (« = » signale une copie identique, contrôlée par empreinte ou par taille et contenu).
- **Intégrité** (contrôle du 26 octobre 2026). Sur les 472 fichiers sélectionnés, 283 sont présents localement ; s'y ajoutent 6 fichiers arrivés après coup (quatre tomes de l'Hésychius de Latte-Hansen-Cunningham, dont un en double, et un EPUB d'Érasme, § 4.1-4.2). Tous ont la taille attendue d'après l'inventaire ; les 159 PDF locaux (14 156 pages) s'ouvrent tous. Un seul fichier est corrompu (contenu entièrement nul) : voir § 8.3. Les 189 fichiers manquants sont recensés au § 9.

## 1. Étude graphologique du manuscrit

Aucun manuel de paléographie de référence n'est disponible localement (voir § 9.2), ni le fac-similé phototypique intégral de 1904 (§ 9.4). Ce qui suit sert à cadrer l'étude ; les images de travail du *Ravennas* sont celles du dépôt (`dossier_ravennas_thesmophories/`, `ravennas_1904_bnf/`).

- **P. Orsini, « L'Aristofane di Ravenna. Genesi e formazione tecnica e testuale di un codice »**, *Scriptorium* 65 (2011), p. 321-337, pl. 55-57. — `D/ravennas/L'aristofane di ravenna*.pdf` [T]. Étude codicologique et paléographique du ms. 429 de la Classense (daté du milieu du Xe s. environ) : mise en page, cahiers, mains, constitution textuelle du recueil. Point de départ obligé de l'étude graphologique.
- **G. Bady, *Paléographie grecque. Éléments de cours*** (support de cours, 31 p.). — `F/Grec/Manuscrits (abréviations)/paleo_grecque_cours_GBady.pdf` [T]. Histoire de l'écriture, numération, codicologie (matériaux, cahiers, réglure), abréviations usuelles : aide-mémoire, pas une autorité.
- **Planche du fac-similé de 1904**, page « 163a » (= f. 163r), vv. 43-79 selon le nom du fichier. — `TH/Ravennas Thesmophoriazusae vv 43-79.png` [I] (1208 × 1575 px). Résolution inférieure aux images du dépôt : utile seulement comme témoin du fac-similé (état du parchemin en 1904).
- Pour l'histoire du manuscrit et de sa diffusion (Koster 1963, White 1906, Dovico 2016), voir § 3.4 ; pour les mains des scholies, Martin 1882 (§ 2).

## 2. Transcription diplomatique

- **A. Martin, *Les scolies du manuscrit d'Aristophane à Ravenne. Étude et collation*** (Bibliothèque des Écoles françaises d'Athènes et de Rome, 27), Paris, E. Thorin, 1882. — `D/ravennas/Martin_1882_*.pdf` (= `AR/Scholies/Les scolies du manuscrit d Aristophane Albert Martin.pdf`) [I] ; OCR intégral de bonne qualité (grec et français) : `D/ravennas/Martin_1882_OCR_tesseract.txt` [T] (le `.txt` voisin du PDF ne contient que la page de garde). *Thesmophories* : p. 196-210 (p. PDF 234-248), scholies relevées folio par folio (f. 162v-177r) avec leur position (*Int.*, *Ext.*, *Sup.*, *inf.*), les écarts par rapport à Dübner et les passages illisibles. L'introduction décrit les mains et l'histoire du manuscrit. Indispensable pour transcrire les scholies et les gloses de R.
- **Apparats fondés sur une collation de R** (détail au § 3.1) : Velsen 1883 (distingue R, R² « scholiorum manus » et une main correctrice récente, et cite G = Monacensis 492) ; Wilson 2007.
- **Papyrus** (vérification des lectures de R là où un témoin antique existe) : § 3.4.

## 3. Établissement du texte et apparat critique

### 3.1 Éditions critiques et textes de référence

- **N. G. Wilson, *Aristophanis fabulae*, Oxford (OCT), 2007**, 2 t. — t. I : `D/editions/Wilson I*.pdf` (435 p. ; = `D/ravennas/Wilson_2007_OCT_I.pdf`) ; t. II : `D/editions/Wilson II Aristophanis*.pdf` (328 p. ; = `D/thesmophories/Wilson_2007_OCT_II.pdf`) [I] (les `.txt` voisins sont vides). *Thesmophories* : t. II, p. 66-124 (p. PDF 68-126) ; conspectus p. PDF 70 (papyrus : PSI 1194 = Π13, P.Oxy. 1176 = Π50, P.Oxy. 3839 = Π14, P.Oxy. 3840 = Π68 ; codex : R ; apographe cité : Mu2 = Monacensis gr. 492). Extrait des p. 48-138 : `AR/Wilson II pp 50-140*.pdf` [I] et version océrisée `D/editions/Wilson II pp 50-140*ocred 2 greek.pdf` [T-] (*Thesm.* = p. PDF 19-77 ; grec très fautif, utilisable seulement pour repérer une page).
- **V. Coulon (texte) et H. van Daele (trad.), *Aristophane*, t. IV : *Les Thesmophories. Les Grenouilles*, Paris, CUF, 1928** (5e tirage 1962). — Pages grecques seules : `AR/Œuvres complètes/Gec_seulement_Les Thesmophories*.pdf` [T-] (*Thesm.* = p. PDF 1-60, hypothesis comprise ; *Grenouilles* p. PDF 61-133 ; errata p. PDF 134 ; OCR aux accents fautifs). Extrait textuel : `D/ravennas/Coulon_1928_Thesm_Grenouilles_textrep.txt` [X] (page de titre, sigla, notice p. 9-13, hypothesis, texte et traduction des p. 17-48, soit jusque vers le v. 780).
- **A. von Velsen, *Aristophanis Thesmophoriazusae*, Leipzig, Teubner, 1883.** — Trois numérisations : `TH/Aristophanis_Thesmophoriazusae Von Velsen 1883.pdf` (97 p.), `TH/Aristophanis_Thesmophoriazusae_von Velsen.pdf` (101 p.), `TH/Von Velsen Aristophanis_Thesmophoriazusae.pdf` (37 vues : autre impression de la même édition, compacte, 28 p. à deux colonnes, sans page de titre ni préface ; la description des sigles R, R² et G, donnée ailleurs dans la préface, ouvre ici l'apparat de la p. 1 ; date non indiquée) [T-]. Apparat double (*adnotatio critica*, *scripturae discrepantia*) fondé sur une collation de R : première source à consulter pour les leçons et corrections de R avant vérification sur l'image.
- **J. Fr. Boissonade (éd.), *Aristophanes*, t. III (*Poetarum Graecorum sylloge*, t. XXIII), Paris, Lefèvre, 1826** : *Thesmophories*, *Lysistrata*, *Grenouilles*. — `TH/Boissonade comoediaethesmo00boisgoog.pdf` [I] (341 p.). Texte et brèves notes (Austin 1990 en cite une, v. 1059).
- **Texte TEI de Perseus** d'après F. W. Hall et W. M. Geldart (OCT). — `TH/Perseus_text_1999.01.0041.xml` [S]. Pratique pour les recherches et les alignements ; pas une autorité.
- **Éditions commentées dont seul un extrait textuel est disponible** [X] (les PDF n'ont pas été récupérés, § 9.2) :
  - **C. Austin, S. D. Olson, *Aristophanes. Thesmophoriazusae*, Oxford, 2004.** — `D/ravennas/AustinOlson_2004_Thesm_textrep.txt` (deux copies identiques dans `D/textes/` et `D/thesmophories/`) : pages liminaires, préface, abréviations et bibliographie, introduction (§ I-IV, jusque vers p. lxv), quelques fragments traduits de la seconde *Thesmophories*. Ni texte, ni apparat, ni commentaire.
  - **A. H. Sommerstein, *The Comedies of Aristophanes*, vol. 8 : *Thesmophoriazusae*, Warminster, 1994.** — `D/ravennas/Sommerstein_1994_Thesm_textrep.txt` : « Introductory Note », bibliographie choisie, et l'essentiel des notes du commentaire (jusqu'aux vv. 1227-1231). Texte et traduction absents.
  - **C. Prato (éd.), D. Del Corno (trad.), *Aristofane. Le donne alle Tesmoforie*, Fondazione Lorenzo Valla / Mondadori, 2001.** — `D/ravennas/Prato_2001_LeDonneAlleTesmoforie_textrep.txt` (= `D/textes_metrique/Prato_2001_LeDonAllTes_readcontent.txt`) : quatrième de couverture, introduction (p. XI-XXXIX), *Indicazioni bibliografiche* (p. XLIII-LXXVI). Texte, apparat et commentaire absents.
- **G. Paduano, *Aristofane. La festa delle donne*, Milan, BUR, 1983** (texte de Coulon avec quelques modifications, traduction, notes) : voir § 6.

### 3.2 Critique textuelle : études d'ensemble et conjectures anciennes

- **C. Austin, « Textual Problems in Ar. *Thesm.* »**, *Δωδώνη* 16 (1987), p. 61-92 (avec *postscript* d'octobre 1988). — `TH/Textual problems in Ar Thesm Austin 1987.pdf` (= `D/thesmophories/Austin_1987_*.pdf` = `D/ravennas/Austin_1987_*.pdf`) [T]. Conjectures des savants de la Renaissance et des XVIIe-XVIIIe s. (Biset, Ellebodius, Casaubon, Faber, Bentley, Daubuz…) retrouvées dans les éditions anciennes et les notes inédites : base pour l'attribution exacte des conjectures dans l'apparat.
- **C. Austin, « Observations critiques sur les *Thesmophories* d'Aristophane »**, *Δωδώνη* 19 (1990), p. 9-29 (fascicule à la mémoire de I. Kambitsis). — `AR/1. Observations critiques*.pdf` [T-] (31 p. : couverture et sommaire du fascicule mal océrisés ; texte de l'article lisible). Discussion de nombreux passages, avec renvois aux éditions anciennes (Ellebodius, Boissonade, Coulon…).
- **R. Bentley, *Emendationes ineditae in Aristophanem : in Thesmophoriazusas, in Lysistratam***, éd. dans *The Classical Journal* 14 (1816), p. 130-147 (réimpr. Cambridge, 2013). — `AR/emendations thesmophories valpy barker*.pdf` [T-]. Conjectures de Bentley vers par vers, avec une collation partielle de l'édition de Brubach (Francfort, 1544).
- **G. Hermann, compte rendu d'Enger, *Aristophanis Thesmophoriazusae cum scholiis* (Bonn, 1844)**, repris dans ses *Opuscula*, t. VIII, Leipzig, 1877, p. 288-308. — `TH/Godofredi Hermanni Opuscula*.pdf` [T-]. Conjectures de Hermann et critique de celles d'Enger, de Fritzsche et de Reisig.
- **P. Thiercy, « Problèmes de distribution et d'attribution des répliques chez Aristophane »**, *Pallas* 38 (1992), p. 289-300. — `AR/Problèmes de distribution*.pdf` [T]. Méthode pour les *notae personarum* (question centrale pour R).
- **K. J. Dover, « Notes on Aristophanes »**, compte rendu d'E. Fraenkel, *Beobachtungen zu Aristophanes* (Rome, 1962), *Classical Review* n.s. 13 (1963), p. 272-274. — `AR/Notes Dover sur Fraenkel*.pdf` [T].

### 3.3 Notes critiques sur des passages des *Thesmophories*

Classées dans l'ordre des vers.

- **vv. 63, 280-281, 706, 941-945, 1030, 1224** — V. Coulon, « Notes sur Aristophane et sur deux passages d'une inscription chrétienne d'Asie-Mineure », *REG* 47 (1934), p. 421-443. — `AR/Coulon notes sur Aris et sur deux passages.pdf` [T].
- **vv. 100, 142, 166-168, 217, 285, 806, 995** — V. Coulon, « Notes critiques et exégétiques sur divers passages controversés d'Aristophane et sur Sophocle, *Antigone* 613-614 », *REG* 66 (1953), p. 34-55. — `AR/Coulon notes critiques et exégétiques.pdf` [T].
- **vv. 123-127** — J. Taillardat, communication à l'Association des études grecques (texte transmis défendu), résumée dans les « Actes de l'Association », *REG* 85 (1972), p. IX-XXXI. — `TH/thesm 123-7 Taillardat*.pdf` [T].
- **vv. 126-129 (et 1170)** — V. Coulon, « Notes critiques et exégétiques sur Aristote, *Poétique* 1450 a 12, 1450 a 29, sur Thucydide I, 1, 2 et sur cinq passages d'Aristophane », *REG* 50 (1937), p. 443-458. — `AR/Coulon notes criti et ex chant agathon Nietsche.pdf` [T].
- **v. 148** — D. Sansone, « Aristophanes, *Thesmophoriazusae* 148 », *CQ* 37 (1987), p. 224-227. — `AR/Aristophanes_Thesmophoriazusae_148.pdf` (= `AR/thesmophories 148.pdf`) [T].
- **vv. 148-152** — E. Viketos, « Aristophanes, *Thesmophoriazusae* 148-152 », *Hermes* 117 (1989), p. 359. — `AR/Thesmophories 148-152 4476703.pdf` [T].
- **v. 242** — R. Goossens, « Notes sur quelques papyrus littéraires », *Chronique d'Égypte* 31 (janvier 1941) : I. *Thesm.* 242 (PSI 1194) ; suite sur Satyros. — `D/papyrus/Notes sur quelques papyrus littéraires*.pdf` [T-]. C. Austin, « Aristophanes, *Thesmophoriazusae* 242 again », *ZPE* 57 (1984), p. 58 (approuve la lecture de S. M. Medaglia, *Boll. Class.* 4, 1983) : capture d'écran `AR/ZPE LVII 1984.png` [I].
- **vv. 247, 289, 721 sqq.** — J. Taillardat, communication résumée dans les « Actes de l'Association », *REG* 101 (1988), p. IX-XXVIII (essai d'interprétation du texte transmis). — `AR/reg_0035-2039_1988_*.pdf` [T].
- **v. 366** — A. Blanc, J. Taillardat, « Aristophane, *Thesmophories*, v. 366 : τῆς χώρας οὕνεκα et l'ambition des oligarques dans l'hiver de 412-411 », *Revue de philologie* 60 (1986), p. 183-186. — `TH/Thesmophories_v.366.pdf` [I].
- **vv. 450-451** — H. Box, « Aristophanes : *Birds* 785-96, and *Thesmophoriazusae* 450-1 », *Classical Review* 14 (1964), p. 241-242. — `AR/thesmophories 450.pdf` [T].
- **vv. 497-501** — R. Cowan, « Nothing to do with Phaedra ? Aristophanes, *Thesmophoriazusae* 497-501 », *CQ* 58 (2008), p. 315-320. — `AR/thesmophories 497-501.pdf` [T] (même article dans `AR/Nothing_to_do_with_Phaedra_Aristophanes.pdf`, sans la page de garde de l'éditeur).
- **v. 638** — E. Degani, « Ar. *Thesm.* 638 », *Eikasmos* 7 (1996), p. 119 sqq. **Attention** : le fichier `AR/Eikasmos VII Deganis Ar Thesm 638.pdf` [I] ne contient pas cette note, mais la couverture, le sommaire et l'article de F. Citti sur Horace (p. 261 sqq.) ; la note de Degani reste à trouver.
- **vv. 855-857** — A. Y. Campbell, « Aristophanes *Thesmophoriazusae* 855-7 and Euripides *Helena* 1-3 », *Classical Review* 63 (1949), p. 81-83. — `AR/thesmophories 855*.pdf` [T].
- **v. 910 (et v. 1187b)** — A. Hartwig, « Interpretive Notes on Aristophanes' *Thesmophoriazusae* », *Philologus* 152 (2008), p. 49-64 (défend notamment l'authenticité du v. 1187b). — `AR/thesmophor 910.pdf` [T]. J. Méndez Dosuna, « Menelaus' Thriving Shrub of Lavender and his Double-Edged Sword : Aristophanes, *Thesmophoriazusae* 910 and *Lysistrata* 156 », *Philologus* 160 (2016), p. 163-171. — `AR/thesm 910.pdf` [T].
- **v. 942** — A. Hartwig, « Feasting and Flattering the Crows : A Reinterpretation of Aristophanes, *Thesmophoriazusae* 942 », *Mnemosyne* 62 (2009), p. 90-93. — `AR/thesmophories 942*.pdf` [T].
- **v. 986** — R. E. Wycherley, « *Thesmophoriazusae* 986 », *Classical Review* n.s. 9 (1959), p. 205-206. — `AR/thesmophories 986 wycherley1959.pdf` (= `AR/thesmophories 986 s0009840x00173159.pdf`) [T].
- Notes de l'auteur sur des passages des *Thesmophories* (articles parus dans *Λύχνος* et ailleurs) : § 8.2.

### 3.4 Papyrus, tradition manuscrite et histoire du texte imprimé

- ***The Oxyrhynchus Papyri*, vol. LXXIII, éd. D. Obbink, N. Gonis, Londres, 2009** (Graeco-Roman Memoirs 94) : volume entier, `D/papyrus/Oxyrhynchus Papyri 73*.pdf` [T] (228 p.) ; tiré à part du n° 4935 (*Thesm.* 1043-1051, 1201-1210, éd. princeps), `F/Grec/Papyrus/The Oxyrhynchus papyri/P.Oxy._LXXIII_4935*.pdf` [T] (15 p.).
- ***The Oxyrhynchus Papyri*, vol. LXXVIII, Londres, 2012** (Graeco-Roman Memoirs 99) : extrait textuel OCR `D/papyrus/POxy78_readcontent.txt` [X], dont le n° 5132 (*Thesm.* 1203-1209 ; même rouleau que 3840 et 4935).
- **Images de papyrus** [I] : `TH/POxy 4935*.jpg`, `TH/POxy.v0056.n3839*.jpg`, `TH/PSI XI 1194 r.jpg` ; recadrages et transcriptions figurées de l'auteur dans `GCA/` (`POxy3839*`, `POxy3840 t.png`, `POxy4935*`, `PSI1194.jpg`). Le volume LVI (P.Oxy. 3839, 3840) n'a pas été récupéré (§ 9.2).
- ***Commentaria et lexica Graeca in papyris reperta* (CLGP)** : I 1, 4 (*Aristophanes-Bacchylides*), pages liminaires et table seulement, `D/papyrus/ARISTOPHANES - BACCHYLIDES INDICE CLGP I.1.4.pdf` [T] (3 p. ; le fascicule complet n'a pas été récupéré, § 9.2) ; II 4 (*Comoedia et mimus*, 2009), cinq fichiers dans `F/Grec/Commentaria et lexica Graeca in papyris reperta/` [T] : introduction « Comoedia », section « Comoedia vetus » (96 p.), index des papyrus, index et planches.
- **W. J. W. Koster, « Aristophane dans la tradition byzantine »**, *REG* 76 (1963), p. 381-396. — `D/ravennas/Ar dans la tradition byzantine*.pdf` [T]. Remet en question l'archétype unique ; commentateurs byzantins.
- **J. W. White, « The Manuscripts of Aristophanes. II »**, *Classical Philology* 1 (1906), p. 255-278. — `D/ravennas/the manuscripts of Aristophanes John William White.pdf` [T]. Éditions juntines : l'appendice de B. Giunta qui donne en editio princeps les *Thesmophories* et *Lysistrata* d'après un manuscrit d'Urbino, identifié au *Ravennas* ; la Juntine de 1525. La première partie de l'article (même revue) manque.
- **G. Dovico, « Excerpta manoscritti dalle commedie di Aristofane : per una prima recensio »**, *FuturoClassico* 2 (2016), p. 62-118. — `D/ravennas/Excerpta manoscritti*.pdf` [T]. Tradition indirecte (recueils d'extraits byzantins).
- ***Anabases* 21 (2015)**, numéro entier. — `AR/anabases-5190 (1).pdf` [T]. Y lire S. Beta, « Peut-on traduire "savamment" tout en faisant des bévues incroyables ? Andreas Divus et son Aristophane », et M. Bastin-Hammou, « Paroles de Paix en temps de guerre : Florent Chrestien et la première traduction de la *Paix* d'Aristophane en France (1589) » : histoire des premières traductions latines et de la réception humaniste.

## 4. Loci paralleli et testimonia

La plupart des grands instruments (Souda, Pollux, Athénée, Stobée, Eustathe, Etymologica, *PCG*, Kock, *TrGF*, concordance de Dunbar, CUF des autres pièces) ne sont pas disponibles localement : voir § 9.2 ; Hésychius l'est en partie (§ 4.1). Les corpus numériques du dépôt (`recherche/corpus_numeriques.md`) y suppléent en partie.

### 4.1 Lexicographes et grammairiens (testimonia indirects)

- **Hésychius, *Lexicon***, éd. K. Latte, P. A. Hansen, I. C. Cunningham (Sammlung griechischer und lateinischer Grammatiker 11), Berlin-Boston, De Gruyter. Quatre tomes sur cinq [T-] :
  - t. I (Α-Δ), éd. K. Latte, 2e éd. par I. C. Cunningham, 2018 — `F/Grec/Lexiques/Hesychius/Latte_I_alpha-delta.pdf` (698 p. PDF) ;
  - t. IIa (Ε-Ι), éd. K. Latte, 2e éd. par I. C. Cunningham, 2020 — `F/Grec/Lexiques/Hesychius/Hesychii Alexandrini Lexicon, Volumen II*.pdf` (1014 p. PDF ; le nom du fichier annonce à tort « Iota-Omicron ») ;
  - t. III (Π-Σ), éd. P. A. Hansen, 2005 — `F/Grec/Lexiques/Hesychius/03 Latte Pi - Sigma*.pdf` (440 p. PDF ; = `F/Grec/Lexiques/Hesychius/Hansen_III_pi-sigma.pdf`) ;
  - t. IV (Τ-Ω), éd. P. A. Hansen et I. C. Cunningham, 2009 — `F/Grec/Lexiques/Hesychius/04 Latte Tau - Aumega .pdf` (313 p. PDF).
  
  Le t. IIb (Κ-Ο) manque (§ 9.2). Couche texte : le grec, composé dans une police à encodage propre, est illisible, mais les références des sources et des parallèles (en caractères latins) sont interrogeables : la recherche de « Ar. Thesm. » donne près de 70 occurrences (t. I : 16 ; IIa : 18 ; III : 25 ; IV : 9), point de départ pour les testimonia lexicographiques. Lire les gloses elles-mêmes sur l'image de la page ; citer Hésychius dans la numérotation de cette édition.
- **I. C. Cunningham (éd.), *Synagoge. Συναγωγὴ λέξεων χρησίμων. Texts of the Original Version and of MS. B***, Berlin-New York, De Gruyter, 2003 (SGLG 10). — `F/Grec/Lexiques/Synagoge/Synagoge.pdf` [T] (768 p.).
- **Photius, *Lexicon***, éd. R. Porson et P. P. Dobree, *pars posterior* (π-ω), Cambridge, 1822 (réimpr. Cambridge, 2010). — `F/Grec/Lexiques/Photius/02 Pi - Aumega*.pdf` [T] (476 p.).
- **Photius, *Lexicon***, éd. Chr. Theodoridis, t. III : Ν-Φ, Berlin-Boston, De Gruyter, 2013. — `F/Grec/Lexiques/Photius/Photii Patriarchae Lexicon N - Phi*.pdf` [T] (629 p.). Les t. I-II n'ont pas été récupérés.
- **H. W. Miller, « A Note on ὁ κωμικός in Eustathius »**, *TAPhA* 73 (1942), p. 353-357. — `F/Grec/283556.pdf` [T]. Pour identifier les citations d'Aristophane chez Eustathe.

### 4.2 Proverbes et langue proverbiale

- **R. Tosi, *Dictionnaire des sentences latines et grecques*** (trad. fr. R. Lenoir ; essai liminaire d'U. Eco ; 2286 sentences commentées), Grenoble, J. Millon, 2011 (1789 p. ; notice de la BnF). — OCR intégral seul : `F/Grec/Proverbes/Dictionnaire sentences grecques et latines Tosi ROC/Dictionnaire des sentences*.txt` [T] (4,9 Mo ; le PDF n'a pas été récupéré). Recherche plein texte des proverbes, sources grecques citées.
- **W. L. Bauck, *De proverbiis aliisque locutionibus ex usu vitae communis petitis apud Aristophanem comicum***, Königsberg, 1880. — `F/Grec/Proverbes/De_proverbiis*Bauck.pdf` [T].
- **L. Cohn, *Zu den Paroemiographen. Mitteilungen aus Handschriften*** (Breslauer philologische Abhandlungen II 2), Breslau, 1887. — `F/Grec/Proverbes/Cohn Zu den Paroemiographen.pdf` [I] (couche texte quasi absente).
- **O. Lazer-Pankiv, *Παροιμίαι ἑλληνικαί*. Dictionnaire des proverbes et dictons grecs anciens** (en ukrainien), Kyiv, 2015. — `F/Grec/Proverbes/ΠΑΡΟΙΜΙΑΙ ΕΛΛΗΝΙΚΑΙ*.pdf` [T].
- **Érasme, *Les Adages*** (choix de 21 adages), introduction de J.-Chr. Saladin, Paris, Les Belles Lettres, 2019 (livre numérique ; traductions reprises de l'édition intégrale bilingue dirigée par J.-Chr. Saladin, 2011, 5 vol.). — `F/Grec/Proverbes/Adages - Érasme/Les adages*.epub` [S] (EPUB : texte HTML ; grec translittéré). Intérêt limité : aucun des adages retenus ne cite les *Thesmophories*. L'édition intégrale n'est pas disponible localement (§ 9.2).

### 4.3 Euripide : tragédies parodiées, biographie

- **P. O'Sullivan, C. Collard, *Euripides. Cyclops and Major Fragments of Greek Satyric Drama***, Oxford, Aris & Phillips, 2013. — `F/Grec/Euripide/Euripides_Cyclops_and_Major_Fragments_of.pdf` [T]. Utile pour les rapprochements avec le *Cyclope* (cf. la discussion d'Austin-Olson sur *Cyclope* et *Andromède*).
- **J. Assaël, « L'Éther initiatique dans l'*Andromède* d'Euripide »**, *Loxias* 45 (2014). — `F/Grec/Euripide/L’Éther initiatique*.pdf` [T].
- **G. Mastromarco, « La parodia dell'*Andromeda* euripidea nelle *Tesmoforiazuse* di Aristofane »**, *Cuadernos de Filología Clásica (G)* 18 (2008), p. 177-188. — `F/Grec/Euripide/la parodia dell andromeda*.PDF` [T]. Analyse des vv. 1009-1135 : reprise de la langue, de la métrique, de la musique et de la mise en scène du modèle.
- **A. Blanchard, c. r. de M. Wright, *Euripides' Escape-Tragedies. A Study of Helen, Andromeda and Iphigenia among the Taurians***, *REG* 119 (2006), p. 798-800. — `TH/Blanchard Euripides' Escape-Tragedies*.pdf` [T].
- **M. Delcourt, « Les biographies anciennes d'Euripide »**, *L'Antiquité classique* 2 (1933), p. 271-290. — `TH/Les biographies anciennes vies d Euripide.pdf` [T].
- **F. J. Campos Daroca, F. J. García González, J. L. López Cruces, L. P. Romero Mariscal, *Las personas de Eurípides***, Amsterdam, Hakkert, 2007 (Classical and Byzantine Monographs 65). — `AR/Vidas_de_Euripides_traduccion_y_notas.pdf` [T]. Traduction annotée des *Vies* et témoignages biographiques (la mère d'Euripide marchande de légumes, etc.).
- **S. Saïd, « Entre l'artisan et le politique »**, dans *Dieux, héros et médecins grecs. Hommage à Fernand Robert*, Besançon, 2001, p. 65-96. — `AR/Sur la mère d'euripide fornaro.pdf` [T] (nom de fichier trompeur). Statut social des poètes ; la tradition biographique sur les parents d'Euripide, issue de la comédie, et le démenti de Philochore.
- **Image** : vase corinthien figurant Persée, Andromède et le monstre marin, `F/Grec/Euripide/Corinthian_Vase*.jpg` [I].

### 4.4 Comédie : fragments, autres pièces, commentaires de référence

- **J.-Cl. Carrière, « L'Aristophane perdu. Une introduction aux trente-trois comédies disparues avec un choix de fragments traduits et commentés »**, dans *Le théâtre grec antique : la comédie* (Cahiers de la Villa Kérylos 10), Paris, 2000, p. 197-236. — `AR/L'Aristophane perdu Carrière .pdf` [T].
- **N. Kyriakidi, *Aristophanes und Eupolis. Zur Geschichte einer dichterischen Rivalität***, Berlin-New York, De Gruyter, 2007 (UaLG 85). — Archive `AR/Aristophane Und Eupolis ZurGesEinDicRiv.rar` contenant un seul PDF ; copie extraite (régénérable) : `.travail/drive_synthese/rar_kyriakidi/3110191393.pdf` [T].
- **CLGP II 4, *Comoedia et mimus*** : § 3.4.
- **A. H. Sommerstein, *The Comedies of Aristophanes*** (Warminster, Aris & Phillips) : vol. 3, *Clouds* (1982), complet, `AR/Nuées/Aristophanes Clouds*.pdf` [T] ; vol. 1 *Acharnians*, vol. 2 *Knights*, vol. 4 *Wasps*, vol. 5 *Peace* : photocopies partielles (page de titre, introduction, note sur le texte et notes du commentaire, sans le texte ni la traduction ; addenda), `AR/Acharniens/*Sommerstein*.pdf`, `AR/Cavaliers/*Sommerstein*.pdf`, `AR/Guêpes/*Sommerstein*.pdf`, `AR/Paix/Sommerstein*.pdf` [I] (45, 49, 59 et 37 vues en doubles pages).
- **M. Landfester (éd., trad., comm.), *Aristophanes. Lysistrate***, Berlin-Boston, De Gruyter, 2019 (Griechische Dramen). — `AR/Lysistrata/*Landfester*.pdf` [T]. Commentaire récent de la pièce jumelle (411).
- **S. Halliwell, traduction annotée** de *Nuées*, *Thesmophories*, *Grenouilles* : § 6.

### 4.5 Parallèles divers (langue, realia, textes rapprochés)

- **E. F. Beall, « Notes on Hesiod's *Works and Days*, 383-828 »**, *AJPh* 122 (2001), p. 155-171. — `TH/Notes on Hesiod s Works and Days*.pdf` [T]. **Réfute** l'interprétation astrale de χελιδών en *Trav.* 568-569 proposée par M. Blomberg, « The Meaning of χελιδών in Hesiod », *Opuscula Atheniensia* 19 (1992), p. 49-57 (non récupéré, § 9.2) : argument contraire à peser face à Clements 2009 (§ 7.2) pour le v. 1.
- **K. Philippides, « Women Chattering about a Ritual : Plautus' *Poenulus* in the Light of Theocritus (*Id.* XV), Herondas (*Mim.* IV) and Aristophanes (*Thesm.*) »**, *Latomus* 77 (2018), p. 1033-1052. — `TH/Peeters.pdf` (= `GCA/Peeters.pdf`) [T] (le nom du fichier est celui de l'éditeur).
- **J. Henderson, « The *Lekythos* and *Frogs* 1200-1248 »**, *HSCPh* 76 (1972), p. 133-143. — `F/Grec/The lekythos (= alabastros = phallus)*.pdf` [T].
- **Cl. Rolley, « À propos d'un vase et de quelques injures (*Assemblée des femmes*, v. 1101-1111) »**, *L'Antiquité classique* 43 (1974), p. 166-171. — `AR/Sur le lecythe Claude Rolley.pdf` [T].
- **Cl. Rolley**, communication sur la fin du *Ploutos* (« Les marmites sur la tête ») résumée dans les « Actes de l'Association », *REG* 79 (1966), p. IX-XXVI : rapproche *Thesm.* 740 sqq. (l'outre « sacrifiée ») des gestes du sacrifice éleusinien du porcelet. — `TH/thesmophories 740 sacrifice*.pdf` [T].
- **E. Harris, J.-M. Carbon, « The Documents in Sokolowski's *Lois sacrées des cités grecques* (LSCG) »**, *Kernos* 28 (2015). — `F/Grec/Dictionnaires/Lois sacrées des cités grecques/kernos-2373.pdf` [T]. Concordance des lois sacrées (règlements de fêtes).
- **A. Zucker, « Album mythique des coquillages voyageurs. De l'écume au labyrinthe »**, *Techniques & Culture* 59 (2012), p. 110-125. — `AR/conque coquillage sexe.pdf` [T].

## 5. Métrique et structure

Les ouvrages de base (Koster, *Traité de métrique grecque*, 2e éd. ; White, *The Verse of Greek Comedy* ; *Aristophanis Cantica* ; Mazon, *Essai sur la composition des comédies d'Aristophane*) n'ont pas été récupérés (§ 9.2) ; plusieurs se trouvent dans `.sources/web/metrique/` (voir `recherche/corpus_numeriques.md` et la synthèse métrique).

- **H. Bornecque, *Précis de prosodie et métrique grecque et latine***, nouvelle éd. revue, Paris, De Boccard, 1933. — `F/Grec/RCR_543952103_55305.pdf` [T] (181 p.). Manuel élémentaire (et non le traité de Koster, comme l'indiquait un premier repérage).
- ***Préparation à la scansion d'Aristophane*** (document pédagogique anonyme, 4 p. : le trimètre iambique et ses substitutions). — `AR/Preparation_a_la_scansion_dAristophane.p.pdf` [T].
- **L. Di Virgilio, « Some Thoughts on Humor and Music in Aristophanes' Plays »**, *Mediterranean World* (地中海論集, Mediterranean Studies Group, Université Hitotsubashi, Tokyo) 24 (2019), p. 31-60 (version revue et augmentée d'une communication d'Urbino, 2018, publiée dans H. Kato, L. Lomiento (éd.), *The Mediterranean as a Plaza*, EPHESO 6, 2018, p. 27-47). — `TH/Thesm vv 1015 1051 pp24sqq.pdf` [T]. Colométrie et analyse métrique de passages lyriques (dont *Thesm.* 1015-1055), établies par l'auteure d'après la tradition manuscrite.
- **E. A. Moutsopoulos, « La musique dans l'œuvre d'Aristophane »**, *Cahiers de la Villa Kérylos* 10 (2000), p. 59-82. — `AR/La musique dans l'oeuvre d'Aristophane.pdf` [T].
- **H. W. Miller, « On the Parabasis of the *Thesmophoriazusae* of Aristophanes »**, *CPh* 42 (1947), p. 180-181. — `AR/parabase des thesmophories.pdf` [T].
- Pour la parodie de l'*Andromède* (métrique et musique du modèle) : Mastromarco 2008 (§ 4.3). Pour la structure d'ensemble de la pièce : Fletcher 1963 et Clements 2014 (§ 7).

## 6. Traduction

- **S. Halliwell, *Aristophanes. Clouds, Women at the Thesmophoria, Frogs. A Verse Translation, with Introductions and Notes***, Oxford, Oxford University Press, 2015. — `AR/Halliwel Aristophane*.pdf` [T] (395 p.).
- **G. Paduano, *Aristofane. La festa delle donne***, introduction, traduction et notes, texte grec en regard, Milan, BUR, 1983 (texte grec : Coulon, avec quelques modifications). — `TH/Le donne alle Tesmoforie*.pdf` [T] (le titre réel est *La festa delle donne*).
- **Th. L. Pangle, traduction anglaise des *Thesmophories*** (document dactylographié, 47 p. ; s. d.). — `TH/Aristophanes_THESMOPORIAZUSAE_a_translat.pdf` [T].
- **Traductions accessibles seulement par extraits** [X] : van Daele (CUF, jusque vers le v. 780), Sommerstein 1994 (notes de traduction), Del Corno (Prato 2001, introduction seule) : § 3.1.
- **G. Stenger, « Le sacré et le salace : flâneries traductologiques à travers la Bible et quelques passages d'Aristophane et de Martial »** (39 p. ; texte diffusé en ligne par le laboratoire LAMO de l'Université de Nantes, daté de 2010 par les métadonnées du fichier ; publication imprimée non identifiée). — `AR/Le_sacre_et_le_salace*.pdf` [T]. Traduction des passages obscènes.
- **S. Pagni, c. r. de R. Saetta Cottone, *Aristophane, « Les Thesmophories » ou « La Fête des femmes »*, traduction commentée (Paris, De Boccard, 2016)**, *Lexis* 35 (2017), p. 458-465. — `TH/Recensione_a_Aristophane_Les_Thesmophori.pdf` [T-] (fascicule : couverture et sommaire ; la couche texte du compte rendu est inutilisable, lire l'image). La traduction de Saetta Cottone elle-même n'est pas disponible.

## 7. Commentaire

### 7.1 Monographies, thèses, ouvrages collectifs

- **A. Clements, *Aristophanes' Thesmophoriazusae. Philosophizing Theatre and the Politics of Perception in Late Fifth-Century Athens***, Cambridge, 2014. — `AR/Aristophanes Thesmophoriazusae  philosophizing theatre*.pdf` [T] (246 p.). Monographie consacrée à la pièce : le prologue lu à la lumière de Parménide (réalité et illusion), la politique de la perception.
- **D. Kanellakis, *Aristophanes and the Poetics of Surprise***, Berlin-Boston, De Gruyter, 2020 (Trends in Classics, Suppl. 96). — `AR/Aristophanes and the Poetics of Surprise*.pdf` [T].
- **Ch. Platter, *Aristophanes and the Carnival of Genres***, Baltimore, Johns Hopkins University Press, 2007. — `AR/*Platter*Carnival*.pdf` [T].
- **N. Kanavou, *Aristophanes' Comedy of Names. A Study of Speaking Names in Aristophanes***, Berlin-New York, De Gruyter, 2010 (Sozomena 8). — `AR/*Kanavou*Comedy_of_Names*.pdf` [T].
- **Ch. Fabrini, *La paratragedia in Aristofane : ricerche sulla ricezione del tragico nel V sec. a.C.***, thèse de doctorat (dir. A. M. Belardinelli), a.a. 2017-2018. — `AR/Tesi_dottorato_Fabrini.pdf` [T] (395 p.).
- **S. Butler, A. Purves (éd.), *Synaesthesia and the Ancient Senses***, Durham, Acumen, 2013 ; y lire A. Clements, « "Looking mustard" : Greek popular epistemology and the meaning of δριμύς », p. 71 sqq. — `AR/Lookink mustard*.pdf` [T].
- **M. Guzmán Carsí, *El elemento obsceno en la comedia aristofánica : Lisístrata, Tesmoforiantes y Asambleístas***, mémoire de fin d'études (Universitat de València, 2015). — `AR/Pasajes_y_lexico_obsceno_en_Aristofanes.pdf` [T].
- **F. Baskevitch, *Le vocabulaire du son en grec ancien (étude sémantique et étymologique)*** (texte de recherche, 97 p., 2011-2016). — `AR/Le_vocabulaire_du_son*.pdf` [T].
- **Kyriakidi 2007** (rivalité avec Eupolis) : § 4.4.

### 7.2 Études sur les *Thesmophories*

- **R. Saetta Cottone, « Agathon, Euripide et le thème de la ΜΙΜΗΣΙΣ dramatique dans les *Thesmophories* d'Aristophane »**, *REG* 116 (2003), p. 445-469. — `AR/agarh eur et le theme*.pdf` [T].
- **Chr. Mauduit, R. Saetta Cottone, « Voir ou entendre : faut-il choisir ? Une analyse de la réception théâtrale dans le prologue des *Thesmophories* »**, *Cahiers des études anciennes* 51 (2014), p. 45-73. — `AR/Voir_ou_entendre*.pdf` [T].
- **A. Blanchard, « L'art de la mauvaise foi dans les *Thesmophories* d'Aristophane »**, dans *Dieux, héros et médecins grecs. Hommage à Fernand Robert*, Besançon, 2001, p. 97-106. — `AR/Lart de la mauvaise foi*.pdf` [T].
- **P. Voelke, « Euripide, héros et poète comique : à propos des *Acharniens* et des *Thesmophories* d'Aristophane »**, *Études de Lettres* (revue de la Faculté des lettres de l'Université de Lausanne), 2004, numéro « Poétique d'Aristophane et langue d'Euripide en dialogue » (dir. C. Calame), p. 117-138 (le fascicule se clôt sur la table des matières de l'année 2004, p. 139 ; son numéro reste [à vérifier]). — `TH/EuripideAristophane.pdf` [T-] (avec la couverture et le sommaire du numéro).
- **E. M. Hall, « The Archer Scene in Aristophanes' *Thesmophoriazusae* »**, *Philologus* 133 (1989), p. 38-54. — `TH/the archer scene*.pdf` [T]. Le Scythe et son grec.
- **E. Bobrick, « Iphigeneia Revisited : *Thesmophoriazusae* 1160-1225 »**, *Arethusa* 24 (1991), p. 67-76. — `TH/IPHIGENEIA REVISITED*.pdf` [T].
- **A. Clements, « *Thesmophoriazusae*'s Two Dawns »**, *Mnemosyne* 62 (2009), p. 535-547. — `TH/Chelidon Ashley Clements*.pdf` [T]. Vv. 1-2 (χελιδών).
- **I. Fletcher, « Aristophanes' *Thesmophoriazusae* (1-176) »**, *Arion* 2.3 (1963), p. 78-85. — `AR/thesmophories 1-176.pdf` [T].
- **O. M. Freidenberg, « Folklore in Aristophanes : *Thesmophoriazusae* »**, *Soviet Studies in Literature* 27, 3 (1991), p. 50-60. — `AR/folklore thesmophories*.pdf` [T].
- **A. Giacomoni, « Rito e trasgressione erotica : Aristoph. *Thesm.* 466 ss. »**, *QUCC* n.s. 63 (1999), p. 91-95. — `TH/thesm 466 sq giacomoni1999.pdf` [T].
- **I. C. Storey, « The "Blameless Shield" of Kleonymos »**, *RhM* 132 (1989), p. 247-261. — `F/thesm v 605 Cleonyme Storey.pdf` [T]. Kléonymos chez Aristophane (*Thesm.* 605).
- **M. Valdés Guía, « Fêtes de citoyennes, délibération et justice féminine sur l'Aréopage (Athènes, Ve siècle avant J.-C.) »**, *Clio. Femmes, genre, histoire* 45 (2017), p. 279-307. — `TH/areopage *.pdf` [T]. Dimension politique de la fête.
- **F. Perusino, « L'ἔγκυκλον, un mantello femminile nelle commedie di Aristofane »**, *QUCC* n.s. 72 (2002), p. 129-133. — `TH/Encycle.pdf` [T].
- **G. Mastromarco, « Toponimi e immaginario sessuale nella *Lisistrata* di Aristofane »**, dans S. D. Olson (éd.), *Ancient Comedy and Reception. Essays in Honor of Jeffrey Henderson*, Berlin-Boston, De Gruyter, 2014, p. 69-81 (volume identifié d'après la pagination du fichier et la bibliographie du *Lessico del comico*). — `TH/toponimi-e-immaginario-sessuale*.pdf` [T].
- **R. Saetta Cottone, c. r. de Cl. Nancy, *Euripide et le parti des femmes* (Paris, 2016)**, *Aretè* 2 (2017), p. 345 sqq. — `AR/CLAIRE_NANCY_Euripide_et_le_parti_des_fe.pdf` [T].
- **Pagni 2017** (c. r. de Saetta Cottone 2016) : § 6.

### 7.3 Aristophane, la comédie et son contexte

- ***Le théâtre grec antique : la comédie*** (Cahiers de la Villa Kérylos 10, Paris, 2000) : Chr. Hunzinger, « Aristophane, lecteur d'Euripide », p. 99-110, `AR/Aristophane lecteur d'Euripide7.pdf` [T] ; J. Jouanna, « Maladies et médecine chez Aristophane », p. 171-195, `AR/jouanna maladie*.pdf` [T] ; Carrière (§ 4.4) et Moutsopoulos (§ 5).
- **D. Soleil, « Les mots d'Aristophane et les mots d'Hippocrate : encore une fois sur le vocabulaire médical d'Aristophane »**, *Lucida intervalla* (Belgrade) 40 (2011), p. 31-48. — `AR/Les_mots_dAristophane*.pdf` [T].
- **P. Thiercy, « L'ὕβρις chez Aristophane »**, *Kentron* 23 (2007), p. 179-191. — `AR/kentron-1754.pdf` [T].
- **G. Jay-Robert, « Fonction des dieux chez Aristophane. Exemple de Zeus, d'Hermès et de Dionysos »**, *REA* 104 (2002), p. 11-24. — `AR/rea_0035-2004_2002_*.pdf` [T].
- **S. Byl, « Φροντιστήριον as Μυστήριον »**, *Kernos* 17 (2004). — `AR/kernos-1477.pdf` [T].
- **P. Brun, « Hyperbolos, la création d'une "légende noire" »**, *DHA* 13 (1987), p. 183-198. — `AR/dha_0755-7256_1987_*.pdf` [T].
- **N. Villacèque, « Ta mère ! Insulte et généalogie à la tribune démocratique »**, *Cahiers « Mondes anciens »* 5 (2014). — `AR/ta mere euripide*.pdf` [T].
- **Saïd 2001** (§ 4.3), **Delcourt 1933** (§ 4.3).

### 7.4 Femmes, religion, costume, iconographie

- **F. Gherchanoc, « Les atours féminins des hommes : quelques représentations du masculin-féminin dans le monde grec antique »**, *Revue historique* 628 (2003), p. 739-791. — `AR/F._Gherchanoc*.pdf` [T]. Travestissement (le Parent).
- **Cl. Leduc, P. Schmitt Pantel, « Prostitution et sexualité à Athènes à l'époque classique »**, *Clio. Femmes, genre, histoire* 17 (2003), p. 137-161. — `F/Grec/0Prostitution*.pdf` [T].
- **A. Damet, « La domination masculine dans l'Athènes classique et sa remise en cause dans les crises intrafamiliales »**, *Siècles* 35-36 (2012). — `F/Grec/La_domination_masculine*.pdf` [T].
- **Th. Fournet, B. Redon, « Le bain grec à l'ombre des thermes romains »**, *Les Dossiers d'archéologie* 342, p. 56-63. — `AR/Le_bain_grec*.pdf` [T].
- **E. Csapo, « A Note on the Würzburg Bell-Crater H5697 ("Telephus Travestitus") »**, *Phoenix* 40 (1986), p. 379-392. — `AR/a note on the wurzburg bell-crater csapo1986.pdf` [T]. Le cratère de Würzburg (« Telephus travestitus » : la scène de l'outre).
- **Images** [I] : cratère de Würzburg (`GCA/Cratere de Wurzbourg.png`, `GCA/Wurzburg.jpg`) ; M. Bieber, *Griechische Kleidung*, pl. VIII 1 (`TH/Griechische Kleidung*.jpg`) ; vase de la base Beazley n° 204020 (`TH/204020, ATHENIAN*.html` et `.png`) ; A. L. Millin, *Dictionnaire des beaux-arts*, t. III, Paris, 1806, p. 69 (« parasol », `TH/parasol millin1806bd3-0077.pdf`) ; P. O. Bröndsted, *Reisen und Untersuchungen in Griechenland*, t. II, Paris, 1830, p. 247 (`TH/femmes par paires broendsted1830-0143.pdf`) ; figures de l'édition de l'auteur dans `GCA/` (`Crocote transparente.jpg`, `Echo voilee Beazley 7864.png`, `Encycle.png`, `Onesime.png`, `Willems.png`, `fin.png`) ; capture d'une note allemande sur un vase au motif de l'outre (`AR/Sans titre.png`, source non identifiée).

### 7.5 Bibliographies

- **« Bibliographie [de C. Austin] 1964-2010 »**, éd. E. Esposito, V. Garulli, C. Neri, *Eikasmos* 22 (2011). — `AR/C._Austin._Bibliographie_1964-2010_Eikas.pdf` (= `AR/Bibl._C._Austin.pdf`) [T]. Liste complète des travaux d'Austin, dont ses notes sur les *Thesmophories*.

## 8. Versions de travail de l'auteur

Toutes les sources `.tex` de l'auteur sont présentes localement (aucune ne dépassait la limite de taille) ; les PDF compilés correspondants, eux, n'ont pas été récupérés (§ 9.3). Les dates d'enregistrement des fichiers ne sont pas fiables (beaucoup ont été réenregistrés en bloc en octobre 2026) : la chronologie ci-dessous repose sur la **date portée par le nom du fichier**, à défaut sur la **date interne d'une archive** (« archive »), à défaut sur une **estimation** d'après la taille et le contenu (« est. »). Tailles en octets. Classe LaTeX `book` et `reledmac` sauf mention contraire.

### 8.1 Versions de l'édition (texte, apparat, traduction, commentaire)

| Date | Fichier | Taille | Remarques |
|---|---|---:|---|
| 2020-02-26 (archive) | `TH/myEdition/myEdition.tex` | 9 382 | essai de mise en page (`article`) ; l'archive `TH/myEdition.zip` contient aussi le PDF compilé et le journal |
| 2020-03-01 | `TH/overleaf/Texte grec - apparat critique - commentaire (1er mars 2020)/main.tex` | 158 115 | premier état connu (texte, apparat, commentaire) ; identique au contenu de l'archive `.zip` du même nom |
| mars 2020 (est.) | `TH/Versions/texte - traduction - commentaire - Copie.tex` | 295 423 | antérieur au 11 mars (taille) |
| mars 2020 (est.) | `TH/thesm.tex` | 301 834 | même famille que les états de mars 2020 |
| 2020-03-11 | `TH/Versions/texte - traduction - commentaire - Copie 11 mars.tex` | 310 949 | |
| 2020-03-21 | `TH/Versions/texte - traduction - commentaire 21 mars 2020.tex` | 320 216 | = `… 21 mars 2020 - Copie.tex` (même dossier) |
| 2020-03-21 ou 25 | `TH/texte - traduction - commentaire 21 mars 2020 - Copie.tex` | 339 200 | identique à `TH/Versions/texte - traduction - commentaire 25 mars 2020 - Copie.tex` : l'un des deux noms est inexact |
| 2020-03-25 | `TH/Versions/texte - traduction - commentaire 25 mars 2020.tex` | 342 827 | |
| 2020-03-26 | `TH/Versions/texte - traduction - commentaire 26 mars 2020.tex` | 351 553 | |
| 2020-03-27 | `TH/Versions/texte - traduction - commentaire 27 mars 2020.tex` | 358 154 | variante : `… 27 mars 2020 2.tex` (361 526) |
| 2020-03-28 | `TH/texte - traduction - commentaire 28 mars 2020.tex` | 379 364 | |
| 2020-03-29 | `TH/texte - traduction - commentaire 29 mars 2020.tex` | 381 160 | |
| 2020-04-11 | `TH/texte - traduction - commentaire 11 avril 2020.tex` | 383 405 | |
| 2020-04-12 | `TH/texte - traduction - commentaire 12 avril 2020.tex` | 384 582 | |
| 2020-04-19 | `TH/texte - traduction - commentaire 19 avril 2020.tex` | 386 695 | |
| 2020-04-25 | `TH/texte - traduction - commentaire 25 avril 2020.tex` | 389 667 | |
| 2020-04-30 | `TH/texte - traduction - commentaire 30 avril 2020.tex` | 409 030 | |
| « 2 mai » (2020 ?) | `TH/Versions/version 2 mai.tex`, `TH/Versions/version 2 2 mai.tex` | 343 860 ; 415 542 | même nombre de lignes (7 500), contenus différents [à examiner] |
| mai 2020 (est.) | `TH/texte - traduction - commentaire - Copie (2).tex`, `… - Copie (3).tex`, `TH/texte - traduction - commentaire.tex` | 423 221 ; 446 049 ; 449 376 | postérieurs au 30 avril (taille) |
| — | `TH/texte - traduction - commentaire - Copie.tex` | 337 647 | **fichier corrompu** (voir § 8.3) |
| 2020-07-03 (archive) | `main.tex` dans `TH/Thesmophories Grec – Traduction – Commentaire  – Apparat.zip` | 547 542 | état distinct de tous les autres (seulement dans l'archive) |
| 2020-07-11 | `GCA/copie 11 juillet 2020.tex` | 548 901 | |
| 2020-07-12 | `GCA/copie 12 juillet 2020.tex` | 556 262 | |
| juillet-août 2020 (est.) | `GCA/main.tex`, `GCA/main2.tex` | 556 744 ; 552 582 | |
| 2020-08-01 | `GCA/copie 1er aout 2020.tex` | 552 617 | |
| 2020-08-02 | `GCA/copie 2 aout 2020.tex` | 556 192 | |
| 2020-08-03 | `GCA/copie 3 aout 2020.tex` | 556 259 | |
| 2020-08-18 | `GCA/AT 18 aout 2020.tex` | 628 380 | = `GCA/Aristophane-Thesmophories (copie).tex` |
| août 2020 (est.) | `GCA/Aristophane-Thesmophories.tex` | 627 222 | voisin du précédent |
| 2020-08-18 / 2021-04 | `GCA/Aristophane-Thesmo 18 aout 2020.tex` | 633 859 | **identique** à `GCA/Aristophane-Thesmo avril 2021.tex` : l'une des deux dates est fausse |
| 2021-05 | `GCA/Aristophane-Thesmo mai 2021.tex` | 703 407 | autre état de mai 2021 : `TH/Versions/Aristophane-Thesmo mai 2021.tex` (652 320) |
| 2021-08 | `GCA/Aristophane-Thesmo aout 2021.tex` | 831 900 | essais de mise en page : `… aout 2021 test.tex` (337 778), `test 2` (276 224), `test 3` (253 851), `test 4` (16 591), `test 5` (13 878) |
| 2021-12 | `GCA/Aristophane-Thesmo decembre 2021.tex` | 1 090 855 | **identique** à `GCA/Aristophane-Thesmo mai 2022.tex` ; copie de sauvegarde d'éditeur `… decembre 2021.tex~` (832 109, état antérieur) |
| 2022-06 | `GCA/Aristophane-Thesmo juin 2022.tex` | 1 219 405 | date interne `\date{… IX 2022}` : contenu mis à jour en septembre |
| 2022-09 | `GCA/Aristophane-Thesmo sept 2022.tex` | 1 219 415 | découpage en deux volumes : `… sept 2022 1 vv 1-633.tex` (542 372), `… sept 2022 2 vv 634-1231.tex` (692 088) ; essai `GCA/Test.tex` (294 396, daté IX 2022) |
| 2022-10 | `GCA/Aristophane-Thesmo oct 2022.tex` | 1 219 482 | variante `… oct 2022  avec page break.tex` (1 219 499) = `… avec page break manuel.tex` |
| 2022-11 | `GCA/Aristophane-Thesmo nov 2022.tex` | 1 232 474 | date interne IX 2022 ; **diffère** de `latex/Aristophane-Thesmo nov 2022.tex` (1 222 484 ; environ 300 lignes propres à chacun) |
| 2023-03 | `GCA/Aristophane-Thesmo Harmattan mars 2023.tex` | 1 302 084 | date interne III 2023 ; **plus complet** que `latex/Aristophane-Thesmo Harmattan mars 2023.tex` (1 006 666), qui s'arrête vers le v. 939 pour le texte grec et vers le v. 960 pour la traduction (deux blocs absents : texte et apparat des vv. 956-1231 env., traduction des vv. 963-1231 env.) ; sauvegarde d'éditeur partielle `… mars 2023.tex~` (30 029) |
| 2023 | `GCA/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` | 631 063 | identique à `latex/` (version de référence) |
| 2023 | `GCA/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex` | 711 864 | identique à `latex/` (version de référence) ; état partiel antérieur : `… vv 642-fin.tex` (111 160) |
| 2024-04-13 | `GCA/Aristophane-Thesmo Harmattan 2023 vv 642-fin-copie13-4-2024.tex` | 711 838 | ne diffère de `-bis` que par des bascules de macros (testimonia désactivés, police de l'anglais, numérotation d'un vers) : variante de compilation, pas de révision du contenu |
| non datés | `GCA/Aristophane-Thesmo Introduction.tex`, `… Annexes.tex`, `… Index.tex` | 50 923 ; 346 018 ; 24 003 | classe `book` sans `reledmac` ; tous trois **plus longs** que leurs homonymes de `latex/` (49 729 ; 281 876 ; 22 815) ; les Annexes citent des travaux de mars-avril 2021 |

### 8.2 Articles de l'auteur

Notes philologiques tirées du travail d'édition (sources `.tex`, `.odt`, `.docx` et PDF ; toutes [S]/[T]). Elles contiennent des propositions de texte et d'interprétation à reprendre dans l'apparat et le commentaire (en les vérifiant comme le reste).

| Date | Titre (passages traités) | Fichiers |
|---|---|---|
| 2020 (juin-août) | état ancien de l'article de novembre 2020 | `GCA/Article août 2020.tex` (= `TH/Articles/Article Luchnos novembre 2020/Ancienne version tex.tex`) |
| novembre 2020 | « Notes sur les *Thesmophories* d'Aristophane » (vv. 7-8 ; 70-74 ; 139 ; 288-291 ; 500 ; 556-557 ; 781 ; 858 ; 939-942 ; 1073-1076 ; 1077-1079), *Λύχνος*, avec une introduction à la pièce | `TH/Articles/Article Luchnos novembre 2020/` (`Notes_sur_les_Thesmophories*.pdf`, `.odt`) |
| mars 2021 | « Notes sur les *Thesmophories* d'Aristophane » [2] (vv. 291 ; 455-458 ; 558-559 ; 894 ; 910 ; une version de travail traite les vv. 443-458), *Λύχνος* | `TH/Articles/Article Luchnos mars 2021/` (`.pdf`, `.odt`, `.docx`) |
| octobre 2022 | « Notes sur Aristophane » (*Ach.* 478-479 ; *Cav.* 19-20 ; *Thesm.* 455-456, 910, 939-942 ; *Gren.* 840, 946-947) | `TH/Articles/Articles pour la parution octobre 2022/` (deux titres, même texte) ; brouillon de la note sur la mère d'Euripide : `GCA/note.txt` (code LaTeX d'un `\commentaire` sur les vv. 455-456) |
| novembre 2022 | « Notes sur Aristophane » (*Thesm.* 855-857 ; *Paix* 1253-1254 ; *Thesm.* 556-557, 1190-1217), *Λύχνος* | `TH/Articles/Article Luchnos novembre 2022/` (`.tex`, `.odt`, `.docx`, PDF ; états « Relu », « Rererelu » ; variante « et un fragment d'Euripide ») |
| janvier 2023 | « Philologie pratique : quelques exemples d'images chez Aristophane » (*Nuées* 226-227, 394 ; *Lys.* 681-682 ; *Gren.* 19) | `TH/Articles/Article début Nuées/` (deux titres, même texte) |
| 2023 | « Un appel d'Aristophane à la paix dans *Lysistrata* (et l'identification d'un vêtement : τὸ ἔγκυκλον = une jupe) » (*Thesm.* 855-857 ; Eur. fr. 228 Kannicht ; *Paix* 1253-1254 ; *Thesm.* 556-557), destiné à *Kentron* [publication à vérifier] | `TH/Articles/Article Kentros 2023 (dossier Paix)/` (`.tex`, PDF) |

### 8.3 Autres fichiers de travail ; anomalies

- **Consignes de compilation** : `GCA/Instructions compilation`, `GCA/Instruction sept.txt`, `GCA/Instructions oct.txt`, `GCA/Insctructions nov 2022.txt`, `GCA/Instructions p1.txt`, `GCA/Instructions p2.txt`, `GCA/Instruction mars 23.txt` [S] : suites de commandes `xelatex` (avec réglages de mémoire) pour chaque version ; utiles pour recompiler les anciens états.
- **Présentation de la pièce** (2 p.) : `GCA/Présentation Thesmophories.odt` et `.pdf` [T].
- **Figures** de l'édition (papyrus, iconographie) : § 3.4 et § 7.4.
- **Fichier corrompu** : `TH/texte - traduction - commentaire - Copie.tex` (337 647 octets, tous nuls). Taille conforme à l'inventaire : la copie locale est inutilisable et doit être récupérée de nouveau (le PDF compilé du même nom, non récupéré, en garde peut-être le contenu).
- **Noms trompeurs** : deux paires de fichiers « datés » différemment sont identiques octet pour octet (18 août 2020 = avril 2021 ; décembre 2021 = mai 2022) ; ne pas s'en servir pour dater une leçon sans contrôle.
- **Divergences avec `latex/`** : seules les deux parties « Harmattan 2023 » sont identiques aux copies du dépôt ; `nov 2022`, `Harmattan mars 2023`, `Introduction`, `Annexes` et `Index` diffèrent (voir § 8.1), et la copie de `latex/` de mars 2023 est tronquée. Toute comparaison de versions doit partir des fichiers de `GCA/`.

## 9. Fichiers non récupérés et manques

Les fichiers retenus pour l'édition lors de l'inventaire préparatoire (472 : 428 « essentiels » et 44 « utiles ») n'ont pas tous pu être copiés localement. La limite de l'outil de copie est en principe de 10 Mo par fichier ; en pratique, aucun fichier de plus de 6,3 Mo n'a été obtenu (le plus lourd des fichiers présents pèse 6 302 740 octets), de sorte que les fichiers de 6,3 à 10 Mo manquent aussi. Les fichiers de plus de 200 Mio avaient été écartés dès l'inventaire (§ 9.4).

- **Conventions de ce paragraphe.** Tailles en Mo (10⁶ octets). « (B) » : fichier classé « utile » et non « essentiel ». Substituts : `ED/` = `.sources/web/editions/` (voir `recherche/bibliographie_editions.md`) ; `W/` = `.sources/web/` ; « corpus » = index plein texte de `.sources/corpus/`, interrogeable par `outils/corpus/chercher.py` (voir `recherche/corpus_numeriques.md`) ; un substitut est une autre édition ou un autre exemplaire, à contrôler avant toute citation.
- **Liste de travail.** La correspondance avec les noms et emplacements d'origine des fichiers est tenue dans `.travail/drive_synthese/etat2_absents.tsv` (non versionné ; régénéré par `etat2.py`, même dossier ; tableaux ci-dessous produits par `section9.py`).

### 9.1 Bilan

- **189 fichiers manquent** sur 472 (4,86 Go) : 130 de plus de 10 Mo ; 19 entre 6,3 et 10 Mo ; 40 plus légers, à savoir 39 PDF compilés des versions de l'auteur (§ 9.3) et une version HTML océrisée de l'extrait de Wilson (raison de l'échec inconnue).
- **Ce qui manque le plus** (pas de substitut local équivalent) :
  1. pour le texte et l'apparat : l'édition commentée d'Austin–Olson (2004) et celles de Sommerstein (1994) et de Prato (2001), accessibles seulement par extraits ; le volume complet de la CUF (Coulon) ; l'*editio princeps* de P.Oxy. 3839 et 3840 (P.Oxy. LVI) ; le *Satyros* de Schorn ;
  2. pour les testimonia : la Souda d'Adler, Photius α-μ de Theodoridis, Hésychius κ-ο (Latte), les *PCG* de Kassel–Austin, les *TrGF* (en particulier le t. V, Euripide), Pollux (Bethe, l. I-V), Eustathe, l'*Etymologicum Gudianum* ;
  3. pour la langue et le commentaire : Taillardat, *Les Images d'Aristophane* ; Henderson, *The Maculate Muse* ; Willi, *The Languages of Aristophanes* ; Chantraine (*DELG*, *Formation des noms*) ; Kühner–Blass ;
  4. pour la graphologie : les manuels de paléographie et d'abréviations (Thompson, Gardthausen, Tsereteli, Oikonomides ; tous, sauf Oikonomides, sont librement accessibles en ligne : § 9.2) et le fac-similé de 1904 ;
  5. les notes critiques de Willems : notes océrisées sur les *Thesmophories* (ouvrage d'origine non identifié) ; la traduction annotée de 1919, elle, est librement accessible (§ 9.2) ;
  6. les PDF compilés de l'auteur dépourvus de source homonyme (§ 9.3).
- **Pistes de récupération** : (a) retenter les 40 fichiers légers, dont l'absence ne tient pas à la limite de taille ; (b) à la place de certains PDF trop lourds, prendre les pièces plus petites que le fonds contient déjà et que l'inventaire avait écartées comme doublons : volumes HathiTrust découpés page par page (Willems 1919, t. I-III ; Hall–Geldart, t. II ; Stobée de Wachsmuth–Hense, t. IV), PDF séparés du *Dictionnaire des images du poétique dans l'Antiquité* ; (c) pour les ouvrages du domaine public, télécharger directement les numérisations libres signalées dans la colonne de droite des tableaux (archive.org, HathiTrust, Gallica).
- **Substituts locaux** : les éditions anciennes (Küster, Brunck, Thiersch, Fritzsche, Enger, Hall–Geldart, Rogers), les scholies de Dübner, les fragments comiques (Kock, Meineke, Kaibel) et tragiques (Nauck), les lexiques anciens (Souda de Bekker, Photius de Porson et de Naber, Pollux de Dindorf, Hésychius de Schmidt) et les parémiographes sont disponibles dans d'autres exemplaires du domaine public (colonne de droite des tableaux).

### 9.2 Ouvrages non récupérés, par usage

#### (1) Étude graphologique

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| E. M. Thompson, *An Introduction to Greek and Latin Palaeography*, Oxford, 1912 | 50,7 | numérisation libre : archive.org, `introductiontogr00thomuoft` |
| E. M. Thompson, *Handbook of Greek and Latin Palaeography* (1re éd. 1893) | 22,0 | numérisation libre de l'éd. de 1893 : archive.org, `handbookpale00thom` |
| V. Gardthausen, *Griechische Palaeographie*, 2e éd., t. II : *Die Schrift, Unterschriften und Chronologie im Altertum und im byzantinischen Mittelalter*, Leipzig, Veit, 1913 (le nom du fichier renvoie à la p. 338) | 44,1 | numérisation libre : archive.org, `griechischepalae02gard` |
| G. F. Tsereteli, *Sokrashcheniia v grecheskikh rukopisiakh* (les abréviations dans les manuscrits grecs), Saint-Pétersbourg, 1896 (le nom du fichier renvoie à la p. 156) | 26,1 | numérisation libre : archive.org, `sokrashcheniiavg00tser` |
| Al. N. Oikonomides, *Abbreviations in Greek Inscriptions, Papyri, Manuscripts and Early Printed Books. A Manual* | 41,3 | — |
| Fac-similé phototypique du *Ravennas* (Leyde, Sijthoff, 1904) : préface de J. van Leeuwen, version océrisée | 54,7 | ff. 162v-163r du fac-similé : `ravennas_1904_bnf/` (dans le dépôt) ; PDF intégral et archive d'images : § 9.4 |

#### (2) Transcription diplomatique

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| Fr. Dübner, *Scholia Graeca in Aristophanem*, Paris, 1842 (scholies des *Thesmophories* d'après R) | 161,6 | même édition : `ED/1842_Paris_Dubner_scholia/scholiagraecain00unkngoog.pdf` (OCR indexé dans le corpus) |

#### (3) Établissement du texte et apparat

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| F. V. Fritzsche, *Aristophanis Thesmophoriazusae*, Leipzig, 1838 (deux numérisations) | autre ex. 38,2 (B) ; ex. « propre » 75,1 | `ED/1838_Leipzig_Fritzsche/` (deux exemplaires, OCR) |
| R. Enger, *Aristophanis Thesmophoriazusae cum scholiis*, Bonn, 1844 | 18,5 | `ED/1844_Bonn_Enger/bsb10232531.pdf` |
| B. Thiersch, *Ἀριστοφάνους Θεσμοφοριάζουσαι*, Halberstadt, 1832 | 7,6 | `ED/1832_Halberstadt_Thiersch/thesmophoriazus00arisgoog.pdf` |
| L. Küster, *Aristophanis comoediae undecim, Graece et Latine*, Amsterdam, 1710 | 121,0 | `ED/1710_Amsterdam_Kuster/` (OCR complet et extraits des *Thesm.*) |
| R. F. Ph. Brunck, *Aristophanis comoediae ex optimis exemplaribus emendatae* (deux fichiers ; éditions ou tomes [à identifier]) | « emendatae studio » 18,3 ; « ex optimis exemplaribus » 17,1 | éd. de Strasbourg, 1783 : `ED/1783_Strasbourg_Brunck/` |
| *Aristophanis comoediae undecim* avec les notes de J. Scaliger (Leyde, 1624, ou Amsterdam, 1670 [à vérifier]) | 42,9 | éd. d'Amsterdam, 1670 : `ED/1670_Amsterdam_Ravestein_t1/`, `ED/1670_Amsterdam_Ravestein_t2/` |
| J. Le Paulmier de Grentemesnil, *Exercitationes in optimos fere auctores Graecos* (conjectures) | 49,4 | — |
| G. Bourdin, scholies sur les *Thesmophories* (Paris, 1545 selon `recherche/bibliographie_editions.md` ; le nom du fichier porte « 1540 ») | 28,6 | Gallica (`bpt6k857402r`, d'après le nom du fichier) ; scholies de Bourdin reproduites dans `ED/1823_Leipzig_Invernizi_t11_scholies_Biset/` et dans l'éd. Portus de 1607 (`ED/1607_Geneve_Portus_Biset/`) |
| *Aristophanis Comoediae*, t. II : très probablement l'OCT de Hall–Geldart (le fonds contient aussi, découpé page par page, l'exemplaire HathiTrust `coo.31924024799623`, qui est le t. II de Hall–Geldart, Oxford, [1906] selon la notice du catalogue) | 53,6 | Hall–Geldart, t. II : `ED/1907_Oxford_Hall_Geldart_t2/` ; texte TEI de Perseus (§ 3.1) |
| V. Coulon, H. van Daele, *Aristophane*, t. IV : *Les Thesmophories. Les Grenouilles* (CUF), volume complet | 10,4 | pages grecques seules et extrait textuel (§ 3.1) |
| C. Austin, S. D. Olson, *Aristophanes. Thesmophoriazusae*, Oxford, 2004 (texte, apparat, commentaire) | 26,4 | extrait textuel partiel (§ 3.1) |
| A. H. Sommerstein, *The Comedies of Aristophanes*, vol. 8 : *Thesmophoriazusae*, 1994 (texte, traduction, commentaire) | 7,8 | extrait textuel partiel (§ 3.1) |
| C. Prato (éd.), D. Del Corno (trad.), *Aristofane. Le donne alle Tesmoforie*, 2001 (texte, apparat, commentaire) | 7,8 | extrait textuel partiel (§ 3.1) |
| G. Mastromarco, P. Totaro, *Commedie di Aristofane* (Turin, UTET) : vraisemblablement le vol. II (2006 : *Uccelli*, *Lisistrata*, *Tesmoforiazuse*, *Rane* ; introduction, traduction, notes critiques et commentaire, celui des *Tesmoforiazuse* étant de P. Totaro), qui porte les noms des deux éditeurs, le vol. I (1983) étant de G. Mastromarco seul [à vérifier sur le fichier] | 26,2 | — |
| A. Willems, *Aristophane. Traduction avec notes et commentaires critiques*, 1919, t. I-III | t. I 99,3 ; t. II 88,9 ; t. III 73,7 | exemplaires HathiTrust en accès libre (domaine public aux États-Unis) : `uc1.b4517639` (t. I), `mdp.39015008735469` (t. II), `mdp.39015051095480` (t. III) ; le fonds contient aussi ces trois volumes découpés page par page (654, 604 et 498 fichiers) |
| A. Willems, notes critiques sur les *Thesmophories* (version océrisée ; ouvrage d'origine [à vérifier]) | 30,1 | — |
| B. B. Rogers, *The Thesmophoriazusae* (texte, traduction, commentaire) : trois fichiers, à savoir le vol. III de la Loeb (Londres, Heinemann, 1924 ; `aristophaneswith03arisuoft`), *The Comedies of Aristophanes*, vol. IV (*Lysistrata*, *Thesmophoriazusae*) d'après le nom du fichier, et une troisième numérisation (« Thesmophories, Lysistrata » ; édition [à identifier]) | Loeb III 20,9 ; « Comedies IV » 15,0 ; « Thesmophories, Lysistrata » 35,3 | `ED/1904_Londres_Rogers/` (éd. de 1904) ; `W/metrique/aristophaneswith03arisuoft/` (Loeb, vol. III) |
| C. Austin, « Observations critiques sur les *Thesmophories* d'Aristophane », 1990 (autre exemplaire) | 15,8 | exemplaire plus léger présent : `AR/1. Observations critiques*.pdf` (§ 3.2) |
| A. Nauck, note sur le v. 80 (conjecture ἐπείπερ ἐστί), dans ses *Mélanges gréco-romains tirés du Bulletin de l'Académie impériale des sciences de Saint-Pétersbourg* (extrait ; les travaux antérieurs de l'auteur citent t. II, 1866, p. 468-471 [à vérifier]) | 7,9 | — |
| *The Oxyrhynchus Papyri*, vol. LVI, 1989 : n° 3839 (vv. 742-766, 941-956 ; éd. W. E. H. Cockle) et n° 3840 (vv. 1185-1193 ; éd. P. J. Parsons) | 22,1 | images : `W/papyrus/POxy_LVI_3839_hires.jpg`, `…_3839_couleur.jpg`, `…_3840_hires.jpg` ; voir `recherche/papyrus.md` |
| *The Oxyrhynchus Papyri*, vol. LXXVIII, 2012 : n° 5132 (vv. 1203-1209 ; éd. W. B. Henry) | 19,5 | extrait textuel `D/papyrus/POxy78_readcontent.txt` (§ 3.4) ; image `W/papyrus/POxy_LXXVIII_4935+5132.jpg` |
| *The Oxyrhynchus Papyri*, vol. IX : n° 1176 (Satyros, *Vie d'Euripide* ; Π50 de Wilson), extrait (le nom du fichier renvoie à la p. 155) | 16,4 | volume complet : `W/papyrus/POxy_IX/pt9oxyrhynchuspa00grenuoft.pdf` |
| *Commentaria et lexica Graeca in papyris reperta* (CLGP) I 1, fasc. 4 : *Aristophanes-Bacchylides* (fascicule complet) | 11,6 | pages liminaires et table seulement (§ 3.4) |
| P. Boudreaux, *Le Texte d'Aristophane et ses commentateurs*, ouvrage posthume publié par G. Méautis, Paris, 1919 | 14,5 | — |
| N. G. Wilson, OCT, t. II, p. 50-140 : version océrisée au format HTML (fichier léger, 3,8 Mo, non récupéré pour une raison inconnue) | 3,8 | autre version océrisée du même extrait : `D/editions/Wilson II pp 50-140*ocred 2 greek.pdf` (§ 3.1) |

#### (4) Loci paralleli et testimonia

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| *Suidae Lexicon*, éd. A. Adler, t. I-V | I (Α-Γ) 42,6 ; II (Δ-Θ) 43,1 ; III (Κ-Ο) 45,6 ; IV (Π-Ψ) 29,4 ; V (préface, index) 10,2 | éd. Bekker (1854), OCR découpé en articles, et Adler partielle (First1KGreek) dans le corpus (`recherche/corpus_numeriques.md`) |
| Photius, *Lexicon*, éd. Chr. Theodoridis, t. I (Α-Δ) et II (Ε-Μ) | I 96,1 ; II 19,7 | t. III (Theodoridis) et éd. Porson (π-ω) présents (§ 4.1) ; éd. Naber et Porson en OCR dans le corpus |
| Hésychius, éd. Latte–Hansen–Cunningham : fichier réunissant l'ensemble (contenu exact [à vérifier] ; il pourrait combler la lacune Κ-Ο) | 11,8 | t. I, IIa, III et IV présents (§ 4.1) ; pour Κ-Ο, éd. M. Schmidt (1867), OCR découpé en articles, dans le corpus |
| Pollux, *Onomasticon*, éd. E. Bethe : l. I-V, l. VI-X, index | index 7,5 ; l. I-V 24,9 ; l. VI-X 18,0 | éd. Dindorf (1824, texte complet) et Bethe, l. VI-X, en OCR dans le corpus |
| Athénée, *Deipnosophistae*, éd. G. Kaibel, t. I-III et index | index 32,5 ; texte 93,2 | texte TEI de Perseus (éd. Kaibel) dans le corpus |
| Eustathe, *Commentarii ad Homeri Iliadem*, éd. M. van der Valk, t. II (chants V-IX) ; *Commentarii ad Homeri Odysseam*, t. I-II | Il. II 86,4 ; Od. I 49,6 ; Od. II 37,0 | t. I, III et IV de l'*Iliade* : § 9.4 ; Miller 1942 sur ὁ κωμικός chez Eustathe (§ 4.1) |
| *Etymologicum Graecae linguae Gudianum*, éd. Fr. W. Sturz, Leipzig, 1818 | 110,1 | — |
| *Etymologicum magnum genuinum, Symeonis Etymologicum una cum Magna Grammatica, Etymologicum magnum auctum*, éd. F. Lasserre, N. Livadaras | 25,8 | *Etymologicum magnum* (réimpr. de l'éd. Sylburg) en OCR dans le corpus |
| Zonaras, *Lexicon*, éd. J. A. H. Tittmann, t. I-II | t. I 64,6 ; t. II 47,9 | t. I (1808) en OCR dans le corpus |
| Phrynichos, *Ecloga*, éd. E. Fischer | 41,8 | — |
| W. G. Rutherford, *The New Phrynichus*, 1881 | 17,6 | — |
| Moeris, *Lexique attique* : D. U. Hansen (éd.), *Das attizistische Lexikon des Moeris*, réuni avec K. Hajdú (éd.), *Ps.-Herodian, De figuris. Überlieferungsgeschichte und kritische Ausgabe* (1re éd. 1998) en un volume de la *Sammlung griechischer und lateinischer Grammatiker* (Berlin-Boston, De Gruyter, 2013, d'après la notice de Google Books ; le nom du fichier porte les deux titres) | 8,7 | — |
| Harpocration, *Lexeis of the Ten Orators*, éd. J. J. Keaney | 6,5 | texte de Harpocration dans le corpus Perseus |
| *Lexica Segueriana* : Δικῶν ὀνόματα, Λέξεις ῥητορικαί ; très probablement I. Bekker, *Anecdota Graeca*, t. I, Berlin, 1814, dont les p. 181-194 (pagination citée par le nom du fichier) contiennent les Δικῶν ὀνόματα, les Λέξεις ῥητορικαί commençant p. 195 (contrôlé sur la numérisation archive.org `anecdotagraeca00bekkgoog`) | 40,1 | même édition librement accessible : archive.org, `anecdotagraeca00bekkgoog` (OCR d'archive.org inutilisable pour le grec) ; la version océrisée du corpus n'en contient encore que deux passages |
| H. Erbse, *Untersuchungen zu den attizistischen Lexika* (fragments d'Ælius Dionysius et de Pausanias), Berlin, Akademie-Verlag | 13,3 | — |
| J. Taillardat, *Suétone. Περὶ βλασφημιῶν. Περὶ παιδιῶν* (extraits byzantins ; version océrisée) | 202,1 | — |
| E. L. von Leutsch, F. G. Schneidewin, *Corpus paroemiographorum Graecorum*, t. I-II | 46,5 | OCR des deux tomes dans le corpus ; CPG I en TEI (First1KGreek) |
| Th. Gaisford, *Paroemiographi Graeci*, Oxford, 1836 | 18,9 | OCR dans le corpus |
| *De usu proverbiorum apud Aristophanem* (dissertation ; auteur et date [à vérifier]) | 16,8 | — |
| R. Tosi, *Dictionnaire des sentences latines et grecques* (PDF) | 75,6 | OCR intégral présent (§ 4.2) |
| L. Cohn, *Zu den Paroemiographen* (version océrisée) | 27,6 (B) | image seule présente (§ 4.2) |
| R. Kassel, C. Austin, *Poetae Comici Graeci* (PCG) | I 11,8 ; II 14,4 ; III 2 (Aristophane) 11,7 ; III 2, version océrisée 63,4 (B) ; IV 34,1 ; V 27,9 ; VI 2 (Ménandre) 10,8 ; VII 21,0 | Kock (CAF), Meineke (FCG) et Kaibel (CGF) en OCR dans le corpus ; numéros K.-A. à contrôler sur l'imprimé |
| Th. Kock, *Comicorum Atticorum fragmenta*, t. I-III | I 22,6 ; II 15,2 ; III 20,3 | OCR des trois tomes dans le corpus |
| A. Meineke, *Fragmenta comicorum Graecorum*, t. II 1-2 | II 1 20,1 ; II 2 18,9 | OCR des t. I-IV dans le corpus |
| J. Demiańczuk, *Supplementum comicum* | 9,5 | — |
| *Tragicorum Graecorum Fragmenta* (TrGF) : t. I et II (B. Snell, R. Kannicht), III et IV (S. Radt), V (R. Kannicht : Euripide) | I 18,0 ; II 22,9 ; III 31,2 ; IV 45,6 ; V 61,5 | Nauck, TGF² (1889), en OCR dans le corpus |
| D. L. Page, *Poetae Melici Graeci* | 19,7 | Bergk, *Poetae lyrici Graeci* (OCR) dans le corpus |
| A. S. F. Gow, *Theocritus*, 2 vol. (commentaire ; *Idylle* XV) | 33,8 (B) | — |
| Euripide, t. V : *Hélène. Les Phéniciennes* (CUF) | 52,4 | texte grec d'*Hélène* dans le corpus Perseus |
| St. Schorn, *Satyros aus Kallatis. Sammlung der Fragmente mit Kommentar* | 22,3 | P.Oxy. IX 1176 : `W/papyrus/POxy_IX/pt9oxyrhynchuspa00grenuoft.pdf` |
| R. Knobl, *Biographical Representations of Euripides. Some Examples of their Development from Classical Antiquity to Byzantium*, thèse de doctorat, Durham University, 2008 (identification d'après le titre du fichier) | 12,0 (B) | accès libre : Durham E-Theses (n° 2190) |
| H. Dunbar, *A Complete Concordance to the Comedies and Fragments of Aristophanes* (deux numérisations) | autre ex. 41,2 (B) ; ex. complet 28,1 | recherche plein texte et par lemme dans le corpus (`outils/corpus/chercher.py`) |
| V. Coulon, H. van Daele, *Aristophane* (CUF) : volumes *Acharniens-Cavaliers-Nuées*, *Guêpes-Paix*, *Assemblée des femmes-Ploutos* ; texte grec seul des onze comédies | Ach.-Cav.-Nuées 16,6 ; Assemblée-Ploutos 10,3 ; Guêpes-Paix 8,6 ; grec seul, 11 pièces 25,9 | texte grec des onze comédies (Hall–Geldart) dans le corpus Perseus |
| Commentaires de référence des autres comédies : S. D. Olson, *Acharnians* ; S. D. Olson, *Peace* ; K. J. Dover, *Clouds* ; K. J. Dover, *Frogs* ; A. H. Sommerstein, *Frogs*, *Birds*, *Lysistrata*, *Wealth* ; N. Dunbar, *Birds* ; D. M. MacDowell, *Wasps* ; Z. P. Biles, S. D. Olson, *Wasps* ; J. Henderson, *Lysistrata* | Biles–Olson, Guêpes 27,6 ; Dover, Gren. 32,5 ; Dover, Nuées 16,6 ; Dunbar, Ois. 27,9 ; Henderson, Lys. 12,8 ; MacDowell, Guêpes 9,3 ; Olson, Ach. 33,1 ; Olson, Paix 84,4 ; Sommerstein, Gren. 13,1 ; Sommerstein, Lys. 6,9 ; Sommerstein, Ois. 7,0 ; Sommerstein, Ploutos 9,3 | Sommerstein, *Clouds* (complet) et Landfester, *Lysistrate*, présents (§ 4.4) |
| *Scholia in Aristophanem* (Groningue) : *Aves* (D. Holwerda) ; *Nubes*, scholies récentes (W. J. W. Koster) ; *Ranae*, scholies récentes (M. Chantry) ; *Plutus*, scholies anciennes et récentes (M. Chantry) | Aves 14,7 ; Nubes rec. 7,9 ; Plutus rec. 18,4 ; Plutus vet. 13,3 ; Ranae rec. 13,0 | Dübner 1842 (voir plus haut, usage 2) |
| Plutarque, *Œuvres morales*, t. XII 1 (traités 54-57), éd. M. Cuvigny, G. Lachenaud (CUF), Paris, 1981 : contient le résumé de la *Comparaison d'Aristophane et de Ménandre* (853a-854d) | 19,9 (B) | texte grec de la *Comparaison* (Perseus) dans le corpus |

#### (5) Métrique et structure

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| J. W. White, *The Verse of Greek Comedy* | 24,1 | `W/metrique/verseofgreekcome00whituoft/` |
| O. Schroeder, *Aristophanis cantica*, Leipzig, Teubner, 1909 (2e éd. 1930) ; édition du fichier [à vérifier] | 19,3 | — |
| W. J. W. Koster, *Traité de métrique grecque suivi d'un précis de métrique latine*, 2e éd. augmentée (version océrisée) | 52,7 | M. L. West, *Introduction to Greek Metre* (1987) : `W/metrique/west-1987-introduction-to-greek-metre/` |
| P. Mazon, *Essai sur la composition des comédies d'Aristophane* | 33,3 | `W/metrique/essaisurlacompos00mazouoft/` |
| M. Emmanuel, *La Danse grecque antique d'après les monuments figurés* | 17,3 (B) | Gallica (`bpt6k11810621`, d'après le nom du fichier) |

#### (6) Traduction

Aucun fichier propre à cet usage ne manque ; les traductions non récupérées sont dans des volumes déjà listés : A. Willems, 1919 (français) ; Coulon–van Daele, CUF IV (français) ; B. B. Rogers (anglais) ; A. H. Sommerstein, 1994 (anglais) ; C. Prato, D. Del Corno, 2001 (italien) ; G. Mastromarco, P. Totaro (italien).

#### (7) Commentaire

| Ouvrage | Fichier(s) et taille (Mo) | Substitut local ou accès |
|---|---|---|
| J. Taillardat, *Les Images d'Aristophane. Études de langue et de style* | 40,5 | version océrisée (plus de 200 Mio) : § 9.4 |
| J. Henderson, *The Maculate Muse. Obscene Language in Attic Comedy* | 15,8 | — |
| A. Willi, *The Languages of Aristophanes* | 14,7 | — |
| A. H. Sommerstein (éd.), *The Encyclopedia of Greek Comedy* | 15,5 | — |
| A. M. Bowie, *Aristophanes. Myth, Ritual and Comedy* | 7,1 | — |
| M. Dillon, *Girls and Women in Classical Greek Religion* | 14,7 | — |
| Cl. Rolley, « Le sanctuaire des dieux patrôoi et le Thesmophorion de Thasos », *BCH* 89 (1965), p. 441-483 | 19,6 | accès libre sur Persée |
| J.-J. Maffre, « Comédie et iconographie : les grands problèmes », *Cahiers de la Villa Kérylos* 10 (2000), p. 269-315 | 7,3 | accès libre sur Persée |
| G. Compton-Engle, *Costume in the Comedies of Aristophanes*, Cambridge, 2015 (identification d'après le titre abrégé du fichier) | 6,7 | — |
| A. Willems, « Le nu dans la comédie ancienne » (version océrisée) | 10,4 | — |
| A. Willems, *Notes sur Aristophane*, Bruxelles, 1897 | 18,2 (B) | même numérisation : `ED/1897_Bruxelles_Willems_Notes/notessuraristoph00will.pdf` |
| A. D. Trendall, *Phlyax Vases* | 9,2 | — |
| E. Bobrick, « The Tyranny of Roles : Playacting and Privilege in Aristophanes' *Thesmophoriazusae* », dans G. W. Dobrov (éd.), *The City as Comedy. Society and Representation in Athenian Drama*, Chapel Hill-Londres, 1997, p. 177-197 (le nom du fichier renvoie aux p. 177 sqq. ; titre et pagination d'après la bibliographie d'Austin–Olson) | 22,0 | — |
| M. Blomberg, « The Meaning of χελιδών in Hesiod », *Opuscula Atheniensia* 19 (1992), p. 49-57 (cf. § 4.5) | 12,6 | — |
| Zadi Grekou, *Aristophane. Recherches sur le vocabulaire de la satire sociale* (thèse, 1983) | 16,8 (B) | — |
| C. Couëlle, « Balaneutikè : le bain et les soins du corps dans l'Antiquité gréco-romaine », *Travaux & documents* (Université de La Réunion) 48, p. 259-284 (identification d'après le nom du fichier, « Couelle2-TD48 », et la notice de HAL) | 10,6 (B) | accès libre : HAL, `hal-01885863` |
| J.-Ph. Guez, F. Klein, J. Peigney, É. Prioux (dir.), *Dictionnaire des images du poétique dans l'Antiquité*, Paris, Classiques Garnier, 2025 (2 vol.), PDF complet | 34,7 (B) | les PDF séparés du même dictionnaire (une quarantaine : lettres, bibliographie, index ; 0,1 à 2,1 Mo chacun) sont dans le fonds, écartés comme doublons : à récupérer à la place du PDF complet |
| P. Chantraine, *Dictionnaire étymologique de la langue grecque* | 132,3 | — |
| P. Chantraine, *La Formation des noms en grec ancien* | 142,8 | version océrisée (plus de 200 Mio) : § 9.4 |
| P. Chantraine, *Morphologie historique du grec* | 16,4 | — |
| R. S. P. Beekes, avec L. van Beek, *Etymological Dictionary of Greek*, 2 vol. | 25,8 | — |
| A. Bailly, *Dictionnaire grec-français*, édition revue « Bailly 2020 » | 33,6 | LSJ (Perseus) dans le corpus |
| R. Kühner, F. Blass, *Ausführliche Grammatik der griechischen Sprache*, 1re partie (*Elementar- und Formenlehre*), 3e éd., t. I-II | t. I 55,4 ; t. II (DjVu) 12,6 | — |

### 9.3 PDF compilés des versions de travail de l'auteur

Toutes les sources `.tex` sont présentes (§ 8.1), mais aucun des 42 PDF compilés sélectionnés n'a été copié (0,02 à 15,6 Mo). Trois seulement dépassent la limite : `GCA/Aristophane-Thesmo grec - commentaire - traduction - apparats.pdf` (15,6 Mo), `GCA/Aristophane Thesmophories sept 2022.pdf` (11,9 Mo) et `GCA/Aristophane-Thesmo Annexes.pdf` (7,7 Mo) ; les 39 autres, plus légers, manquent pour une raison non établie.

- **À récupérer en priorité** : les treize PDF qui n'ont pas de source `.tex` du même nom et peuvent donc conserver des états sans source : les deux fichiers lourds cités ci-dessus ; `GCA/Aristophane-Thesmo août 2022.pdf`, `… septembre 2022.pdf`, `… V1 avec index.pdf` ; les copies numérotées `… juin 2022 (copie 1)` à `(copie 5)`, `… oct 2022 (copie 1)`, `… nov 2022 (copie 1)` et `(copie 2)`.
- **Fichier corrompu** : le PDF `TH/texte - traduction - commentaire - Copie.pdf` (0,3 Mo) correspond au `.tex` illisible signalé au § 8.3.
- **Déjà accessible autrement** : `TH/myEdition/myEdition.pdf` est contenu dans l'archive `TH/myEdition.zip` (§ 8.1).
- **Liste complète** (taille en Mo) : `GCA/AT 18 aout 2020.pdf` (0,7) ; `GCA/Aristophane Thesmophories sept 2022.pdf` (11,9) ; `GCA/Aristophane-Thesmo 18 aout 2020.pdf` (0,7) ; `GCA/Aristophane-Thesmo Annexes.pdf` (7,7) ; `GCA/Aristophane-Thesmo Harmattan 2023 vv 1-641.pdf` (0,6) ; `GCA/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.pdf` (0,7) ; `GCA/Aristophane-Thesmo Harmattan 2023 vv 642-fin.pdf` (0,1) ; `GCA/Aristophane-Thesmo Index.pdf` (0,06) ; `GCA/Aristophane-Thesmo Introduction.pdf` (1,9) ; `GCA/Aristophane-Thesmo V1 avec index.pdf` (1,1) ; `GCA/Aristophane-Thesmo aout 2021 test 2.pdf` (0,3) ; `GCA/Aristophane-Thesmo aout 2021 test 3.pdf` (0,3) ; `GCA/Aristophane-Thesmo aout 2021 test 4.pdf` (0,04) ; `GCA/Aristophane-Thesmo aout 2021 test 5.pdf` (0,03) ; `GCA/Aristophane-Thesmo aout 2021 test.pdf` (0,4) ; `GCA/Aristophane-Thesmo aout 2021.pdf` (0,9) ; `GCA/Aristophane-Thesmo août 2022.pdf` (1,1) ; `GCA/Aristophane-Thesmo grec - commentaire - traduction - apparats.pdf` (15,6) ; `GCA/Aristophane-Thesmo juin 2022 (copie 1).pdf` (1,2) ; `GCA/Aristophane-Thesmo juin 2022 (copie 2).pdf` (1,2) ; `GCA/Aristophane-Thesmo juin 2022 (copie 3).pdf` (0,9) ; `GCA/Aristophane-Thesmo juin 2022 (copie 4).pdf` (1,2) ; `GCA/Aristophane-Thesmo juin 2022 (copie 5).pdf` (1,2) ; `GCA/Aristophane-Thesmo juin 2022.pdf` (1,2) ; `GCA/Aristophane-Thesmo mai 2021.pdf` (0,8) ; `GCA/Aristophane-Thesmo mai 2022.pdf` (0,2) ; `GCA/Aristophane-Thesmo nov 2022 (copie 1).pdf` (1,2) ; `GCA/Aristophane-Thesmo nov 2022 (copie 2).pdf` (1,2) ; `GCA/Aristophane-Thesmo nov 2022.pdf` (0,02) ; `GCA/Aristophane-Thesmo oct 2022 (copie 1).pdf` (1,2) ; `GCA/Aristophane-Thesmo oct 2022.pdf` (1,2) ; `GCA/Aristophane-Thesmo sept 2022.pdf` (1,2) ; `GCA/Aristophane-Thesmo septembre 2022.pdf` (1,1) ; `GCA/Aristophane-Thesmophories (copie).pdf` (0,7) ; `GCA/Article août 2020.pdf` (0,1) ; `GCA/copie 12 juillet 2020.pdf` (0,7) ; `TH/Versions/version 2 2 mai.pdf` (0,5) ; `TH/Versions/version 2 mai.pdf` (0,2) ; `TH/myEdition/myEdition.pdf` (0,03) ; `TH/texte - traduction - commentaire - Copie.pdf` (0,3) ; `TH/texte - traduction - commentaire 21 mars 2020 - Copie.pdf` (0,3) ; `TH/texte - traduction - commentaire.pdf` (0,5).

### 9.4 Fichiers de plus de 200 Mio (écartés dès l'inventaire)

53 des fichiers retenus pour l'édition (6 « essentiels », 47 « utiles ») dépassaient 200 Mio (209 715 200 octets) ; aucun n'a été sélectionné.

| Ouvrage | Taille (Mo) | Remarque |
|---|---:|---|
| Fac-similé phototypique intégral du *Ravennas* (Leyde, Sijthoff, 1904 ; exemplaire de la BnF, FOL-FAC SIM-182 (9)) | 330 | ff. 162v-163r : `ravennas_1904_bnf/` (dans le dépôt) ; les images du manuscrit lui-même, à pleine résolution, sont dans `dossier_ravennas_thesmophories/` |
| Archive d'images (BnF) du même fac-similé | 323 | idem |
| Eustathe, *Commentarii ad Homeri Iliadem*, éd. M. van der Valk, t. I (chants I-IV), III (X-XVI), IV (XVII-XXIV) | 243 ; 250 ; 254 | t. II : § 9.2 |
| J. Taillardat, *Les Images d'Aristophane*, version océrisée | 2 809 | version non océrisée : § 9.2 |

Les 47 autres, classés « utiles », sont pour la plupart des versions océrisées très lourdes d'ouvrages listés plus haut (fac-similé de 1904, Dübner, Willems t. I-II, texte grec de la CUF, Chantraine, *Formation des noms*, Eustathe, Hésychius, Photius, Pollux, *Synagoge*, *PMG*, *CPG*, Tosi, *TrGF* V) ou des compilations ; s'y ajoutent l'*Etymologicum magnum* de Gaisford (904 Mo), neuf fichiers du *Dictionnaire des antiquités grecques et romaines* de Daremberg et Saglio (consultable en ligne), un demi-volume de la *Realencyclopädie* (t. XIII 2), un volume des *FGrHist* de Jacoby (II A) et un tome du Stobée de Wachsmuth–Hense (t. III).

### 9.5 Titres absents du fonds

Recherchés sans résultat lors de l'inventaire (le fonds ne les contient pas) ; substituts locaux entre parenthèses :

- **Grammaires et dictionnaires** : LSJ (LSJ de Perseus dans le corpus) ; J. D. Denniston, *The Greek Particles* ; Kühner–Gerth (syntaxe) ; E. Schwyzer, *Griechische Grammatik* ; H. W. Smyth, *Greek Grammar*.
- **Aristophane** : L. P. E. Parker, *The Songs of Aristophanes* ; N. G. Wilson, *Aristophanea* ; l'édition de J. van Leeuwen (`ED/1904_Leyde_van_Leeuwen/`) ; celle de F. H. M. Blaydes (`ED/1880_Halle_Blaydes/`) ; C. Austin, *Comicorum Graecorum Fragmenta in papyris reperta*.
- **Scholies** : W. G. Rutherford, *Scholia Aristophanica* (`ED/1896_Londres_Rutherford_t2/` ; `W/scholies/`, t. I-III) ; K. Zacher, *Die Handschriften und Classen der Aristophanesscholien* (`W/ravennas/scholies/diehandschrifte02zachgoog.pdf`) ; l'édition de Groningue des scholies des *Thesmophories* (aucun substitut).
- **Euripide** : aucun commentaire moderne d'*Hélène* (seule l'édition de la CUF figurait dans le fonds, et elle n'a pas été récupérée) ; pour l'*Andromède* et le *Télèphe*, seulement les *TrGF* V (non récupérés) et quelques articles (§ 4.3).

### 9.6 Fichiers du fonds restés hors sélection

L'inventaire a classé « utiles » sans les retenir 309 fichiers de moins de 200 Mio (doublons, autres exemplaires, ouvrages d'intérêt secondaire). Quelques-uns mériteraient d'être récupérés (identifications d'après le nom des fichiers, non contrôlées sur leur contenu) :

- **Stobée**, éd. C. Wachsmuth et O. Hense, t. I-V (42 à 201 Mo par volume) ; le t. IV existe aussi, découpé page par page, dans l'exemplaire HathiTrust `uc1.b4810319` (domaine public). Substitut local : le *Florilegium* de Meineke et le t. III de Hense, en OCR dans le corpus.
- **A. Nauck, *Mélanges gréco-romains***, volume complet d'où provient la note sur le v. 80 (26,0 Mo ; l'extrait retenu, 7,9 Mo, manque : § 9.2).
- **B. B. Rogers, *The Comedies of Aristophanes*** : six volumes (6,7 à 70,7 Mo), dont un vol. IV (« 4 Lysistrata », 41,3 Mo), sans doute le même ouvrage que le fichier « Comedies IV » du § 9.2 ; et un exemplaire de la Loeb, vol. III (20,9 Mo), probablement identique à `aristophaneswith03arisuoft`.
- **Édition ou traduction hongroise des *Thesmophories*** (numérisation de la bibliothèque de l'Académie hongroise des sciences, « MTA Könyvek » ; 73,8 Mo).
- **Scholies d'Euripide** : éd. E. Schwartz, volume d'*Hécube*, *Oreste* et des *Phéniciennes* (23,8 Mo) ; éd. W. Dindorf, t. IV (10,0 Mo). Substitut local : scholies d'Euripide de First1KGreek dans le corpus.
