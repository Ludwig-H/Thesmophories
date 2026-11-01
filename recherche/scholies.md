# Scholies des *Thesmophories* — recension

> État : **version de travail** (26/10/2026, revue le 28/10/2026, puis le 01/11/2026 : relevé complet des scholies comme témoins du texte, §§ 3, 5, 6 et 7 ; collation de Holzinger). Le relevé est dans `edition/donnees/scholies_temoins.tsv`. Chaque affirmation renvoie à la source où elle a été lue ; ce qui n'a pas pu être contrôlé est marqué *[à vérifier]*. Les éditions anciennes citées sont dans `.sources/web/editions/`, `.sources/web/scholies/` et `.sources/web/etudes/holzinger/` (domaine public, non versionnées) ; l'édition moderne (Regtuit 2007) n'est pas disponible localement.

## 1. Conventions et sources consultées

- **Σ** = scholies anciennes (*vetera*) du Ravennas ; **R** = Ravenne, Biblioteca Classense, ms. 429 ; numérotation usuelle des vers (voir `recherche/papyrus.md`, § 1).
- Sources lues pour cette notice :
  - F. Dübner, *Scholia Graeca in Aristophanem*, Paris, Didot, 1842 : préface (datée « exeunte anno MDCCCXLI »), préface de W. Dindorf réimprimée, scholies des *Thesm.* pp. 264-272, *adnotatio* pp. 507-512 (elle ne s'arrête pas à la p. 510 ; dernier article : v. 1190) (`.sources/web/editions/1842_Paris_Dubner_scholia/`) ;
  - W. G. Rutherford, *Scholia Aristophanica*, I (1896), introduction pp. v-xv ; II (1896), scholies des *Thesm.* pp. 441-509 (`.sources/web/scholies/`). Pour le t. II, le scan Google n'a pas d'OCR pour la plupart des pages paires ; j'ai pris l'exemplaire de la BSB (`bsb11798157`, images 453-521 ; page imprimée + 12), copié dans `.sources/web/scholies/rutherford2_bsb/` et océrisé avec tesseract (`.travail/scholies_temoins/ruth/ocr/`). En bas de page, l'indication de place **suit** chaque scholie (`ext.`, `int.`, `supr.`, `infr.`, `inter.`, `intermarg.`) ;
  - A. Martin, *Les scolies du manuscrit d'Aristophane à Ravenne*, Paris, 1882, *Thesm.* pp. 196-209 (`.sources/drive/ravennas/Martin_1882_OCR_tesseract.txt` et PDF de même nom ; Martin ne donne que les écarts par rapport à Dübner, avec le folio et la place : Ext., Int., Sup., Inf.) ;
  - C. R. von Holzinger 1882 et K. Holzinger 1883 (voir § 5) ;
  - inventaires graphologiques des 30 pages de R (`ravennas/graphologie/folios/`) et images de R, pour chaque cas retenu dans le relevé.
- **Prudence sur l'OCR.** Les OCR de Dübner et de Martin confondent β, θ et δ : ils donnent λαθεῖν au v. 419 là où les deux imprimés portent λαβεῖν. Toute citation du relevé a été prise sur R ou sur le bas de page de Rutherford, et les points litigieux sur l'image.
  - K. Zacher, *Die Handschriften und Classen der Aristophanesscholien*, Leipzig, 1888 (*Jahrbücher für classische Philologie*, Suppl. 16) (`.sources/web/editions/1888_Leipzig_Zacher/`) ;
  - Invernizi–Beck–Dindorf, *Aristophanis Comoediae*, t. XI = *Scholia Graeca* (« Odoardi Biseti et Aegidii Bourdini scholia continens »), Leipzig, Weidmann (`.sources/web/editions/1823_Leipzig_Invernizi_t11_scholies_Biset/`) ;
  - R. Tordoff, compte rendu de l'édition de Groningue, *BMCR* 2008.09.24 (copie : `.travail/recension/web2/bmcr_26108.html`).

## 2. Le corpus

### 2.1 Un seul témoin

- Les scholies des *Thesm.* ne sont transmises que par R. Dindorf (préface reproduite par Dübner 1842, p. II-III) : « Propria huic codici sunt scholia Thesmophoriazusarum, Lysistrataeque versuum 818-889, 1099-1228, 1260-1278, 1297-1311 ». Le Venetus Marcianus 474 (V), le plus riche en scholies après R, n'a pas la pièce (« desunt enim Acharnenses, Ecclesiazusae, Thesmophoriazusae, Lysistrata », ibid.) ; l'Aldine de 1498, première édition des scholies, « caret enim Thesmophoriazusis et Lysistrata » (ibid.). Tordoff (*BMCR* 2008.09.24) : sans R, ces scholies seraient perdues « except for those preserved in the indirect tradition in the lexica ».
- Dans R, la pièce occupe les ff. 162v-177r, **sans hypothesis** (Zacher 1888 : « f. 162 v — 177 r. Thesmophoriazusae. Keine hypotheses ») ; le corpus s'ouvre sur une courte notice (Προλογίζει Μνησίλοχος κηδεστὴς Εὐριπίδου. ὁ χορὸς ἐκ θεσμοφοριαζουσῶν…, Dübner p. 264).
- Disposition (Zacher 1888, à propos des trois dernières pièces de R, *Guêpes*, *Thesm.*, *Assemblée*) : les *Thesm.* sont « am reichsten mit Scholien bedacht » ; les scholies occupent surtout les marges extérieure et intérieure (la seconde avec des notes moins nombreuses et plus courtes) ; les lemmes n'apparaissent qu'à la première page de la pièce, ensuite isolément. Zacher (§ 12) attribue les différences de présentation des scholies au modèle de R, non aux deux copistes du manuscrit. Pour la paléographie (main des scholies, gloses interlinéaires), voir `recherche/ravennas_dossier.md`.
- Rutherford (I, p. VI, n. 2) signale que, dans les *Thesm.* et l'*Assemblée*, il est parfois difficile de distinguer scholies et simples indications jointes au texte (γραῦς, ἡ ἑτέρα…) ; Graeven a tenté de trancher, Martin non.
- Volume : neuf pages à deux colonnes chez Dübner (pp. 264-272) ; une soixantaine de pages, traduction anglaise comprise, chez Rutherford (II, pp. 440-509 environ).

### 2.2 Contenu remarquable (relevé non exhaustif)

- **v. 162** : la note la plus savante, avec des restes d'Aristophane de Byzance et de Didyme (Tordoff ; « 162a » dans l'édition de Regtuit).
- **v. 389** : Diodore (Διόδωρος οὐ μεταφορικὴν, ἀλλ' ἐξ ἔθους γλωσσηματικὴν…), lu chez Dübner p. 267 ; Rutherford corrige σκώπτειν en σκήπτειν, correction que Tordoff regrette de ne pas voir mentionnée par Regtuit.
- **v. 870** : la scholie attribue οἶσθ' οὖν ὃ δρᾶσον au *Polyidos* d'Euripide ; Regtuit maintient *Polyidos* contre Nauck et Kannicht (TrGF V.2), qui y voient *Hécube* 225 (*Polydoros*) (Tordoff ; Regtuit, prolégomènes, pp. 12-13).
- **v. 491** : mots tardifs βουρδωνάριος et σταβλίτης (Dindorf, préface, dans Dübner p. III).
- Symmaque est nommé deux fois dans les scholies des *Thesm.* (décompte de Dindorf, *ibid.*, p. VII).

### 2.3 Scholies « récentes » et autres témoins

- Il n'existe pas de recension byzantine (Tzetzès, Thomas Magister, Triclinius) pour cette pièce, faute de tradition hors de R.
- **Claude Dupuy (Puteanus)** : Dübner a utilisé un exemplaire de l'édition de Froben (Bâle) annoté par Dupuy et conservé à la Bibliothèque royale (sigle *Put.* : « Apographum scholiorum in Lysistratam et Thesmophoriazusas a Claudio Puteano factum, ante nos incognitum »). Pour la *Lysistrata*, ces scholies viennent d'un livre « Ravennatis simillimo » ; pour les *Thesm.*, Dupuy « scholia quaedam adscripsit aliunde ducta et recentiora » (*adnotatio*, p. 507). Dübner en cite plusieurs (vv. 21, 392, 702 : note « κατὰ Ἀνδρέαν », rapprochée d'une note à *Lys.* 1087). Cote de l'exemplaire *[à identifier à la BnF]*.
- **Mu2** (Monacensis gr. 492), apographe de R pour la pièce (Wilson, OCT II, liste des sigles) : présence de scholies *[à vérifier]*.
- **Tradition indirecte** : la Souda puise dans les scholies d'Aristophane (« Suidam haec scholia expilare solitum », Dübner, préface) ; pour les *Thesm.*, de nombreuses notices de la Souda reproduisent la scholie de R (ex. : Souda α 1330 = Σ 2 ἀλοῶν, « excerpsit Suidas sub Ἀλοῶ, verbis leviter mutatis », Dübner, *adnotatio*, p. 507) ou en donnent une forme plus complète. Enger (1844) a ajouté au corpus d'autres scholies anciennes (Tordoff) *[nature et source de ces ajouts à vérifier dans l'édition d'Enger]*. Voir `recherche/testimonia.md`, où les notices de la Souda qui citent la pièce sont relevées vers par vers.

### 2.4 Scholies à d'autres auteurs qui citent la pièce

Relevé fait pour `recherche/testimonia.md` (texte lu, référence vérifiée sauf mention contraire) : Σ *Ach.* 79 (vv. 53-57, citation abrégée avec ἁψῖδας ; scholie absente de R, Dübner p. 5) ; Σ *Ach.* 1201 (vv. 131-132, glose μανδαλωτόν) ; Σ *Vesp.* 1158 (v. 142, pièce nommée) ; Σ *Vesp.* 175 (v. 928, proverbe) ; Σ *Eq.* 435 dans l'Aldine (v. 566, interpolée de la Souda selon Dübner) ; Σ *Plut.* 453 (vv. 696-697, pièce nommée) ; Σ *Il.* 1, 135-137 (vv. 536-537, Dindorf et Maass) ; Σ Eur. *Hec.* 225 (v. 870, ἡμέρας pour ἐλπίδος, d'après Grégoire de Corinthe) ; Σ Lucien, *Alex.* 4 (v. 861, Φρυνώνδας, pièce nommée ; non relevée par l'auteur). Non vérifiées : Σ Platon (*Gorg.* 457b, *Hipp. min.* 365d, *Théag.* 127c, *Hipparque* 229d ; vv. 390-391 et 447-449 ; éd. Greene 1938, archive.org `scholia-platonica-1838_1838`), Σ Hésiode, *Op.* 227-229 (v. 300), Σ *Av.* 307 et 1295 (vv. 393 et 168).

## 3. Éditions

| Année | Éditeur | Ouvrage | Nature | Copie locale |
|---|---|---|---|---|
| 1545 | G. Bourdin (*Aegidius Burdinus*) | Τὰ τοῦ Αἰγιδίου Βουρδίνου σχόλια εἰς τὴν … Θεσμοφοριαζουσῶν κωμῳδίαν, Paris (J. L. Tiletanus) | scholies grecques **humanistes** (commentaire de Bourdin, non antique) | Drive de l'auteur (« Bourdin 1540 », Gallica bpt6k857402r, non encore téléchargé) ; réimpression dans Portus 1607 et Invernizi t. XI (PDF 283-345) |
| 1607 | Aem. Portus, avec les scholies d'O. Biset | *Comoediae undecim*, Genève | « scholia » de Biset (sur toutes les pièces, tirés surtout de la Souda et d'Eustathe) et de Bourdin | `1607_Geneve_Portus_Biset/` |
| 1710 | L. Kuster | *Comoediae undecim … cum scholiis antiquis*, Amsterdam | scholies de la *Lysistrata* « ex cod. Vossiano nunc primum » ; pour les *Thesm.*, Biset et Bourdin (jugement de Kuster sur Bourdin : « nil nisi tritum et vulgare ») | `1710_Amsterdam_Kuster/` (extraits) |
| 1822-1826 | W. Dindorf | *Scholia Graeca in Aristophanis comoedias* = Invernizi–Beck–Dindorf t. X-XII, Leipzig | Aldine corrigée ; *Lys.* d'après Kuster ; Biset et Bourdin d'après l'édition de 1607 (Rutherford I, p. XIV, n.) | `1823_Leipzig_Invernizi_t11_scholies_Biset/` |
| 1829 | I. Bekker | *Aristophanis comoediae cum scholiis et varietate lectionis*, Londres, t. II | **editio princeps** des scholies de R aux *Thesm.* (collation de R en 1818, mise en forme par A. Seidler) | `1829_Londres_Bekker_t2_scholies/` |
| 1832 | B. Thiersch | *Thesmophoriazusae cum scholiis cod. Ravennatis*, Halberstadt | texte et scholies (d'après Bekker) | `1832_Halberstadt_Thiersch/` |
| 1834 | (Invernizi–Beck–Dindorf) | t. IX, 2ᵉ partie | réimpression des scholies des *Thesm.* « ex edit. Londin. a. 1829 » (Rutherford I, p. XIV, n.) | — |
| 1838 | F. V. Fritzsche | *Thesmophoriazusae*, Leipzig | avec les scholies (Tordoff) | `1838_Leipzig_Fritzsche/` |
| 1838 | W. Dindorf | *Aristophanis comoediae*, Oxford, t. IV, 3ᵉ partie | scholies ; selon W. G. Clark, nouvelle transcription de R faite en 1837 par E. Miller ; Fritzsche dit Dindorf tributaire de la collation de Bekker-Seidler (Rutherford I, p. XIV, n.) | `1838_Oxford_Dindorf_t4-3_scholies/` |
| 1842 | F. Dübner | *Scholia Graeca in Aristophanem*, Paris, Didot | texte de Dindorf revu ; *adnotatio* de Dübner sur les scholies de *Lys.* et des *Thesm.* ; scholies de Puteanus | `1842_Paris_Dubner_scholia/` |
| 1844 | R. Enger | *Aristophanis Thesmophoriazusae*, Bonn | texte et scholies, avec d'autres scholies anciennes ajoutées (Tordoff) | `1844_Bonn_Enger/` (images) |
| 1882 | A. Martin | *Les scolies du manuscrit d'Aristophane à Ravenne*, Paris (BEFAR 27) | collation (faite à l'été 1880) ; folio et place de chaque note, écarts par rapport à Dübner | `.sources/drive/ravennas/` ; index OCR (`ia:lesscoliesdumanu00martuoft`) |
| 1882 | C. R. von Holzinger | « Beiträge zur Kenntniss der Ravennasscholien zu Aristophanes », *Wiener Studien* 4, pp. 1-32 ; *Thesm.* : pp. 22-23 | collation (décembre 1881), rapportée au texte de Dübner, moins détaillée que celle de Martin (Rutherford I, p. VI, n. 1) | `.sources/web/etudes/holzinger/` |
| 1896 | W. G. Rutherford | *Scholia Aristophanica*, I-II, Londres, Macmillan | scholies de R seules, avec traduction ; transcription contrôlée sur le manuscrit par H. Graeven ; t. III (1905) : *A Chapter in the History of Annotation* | `.sources/web/scholies/` (t. I, II, III) ; t. II BSB dans `rutherford2_bsb/` |
| 2007 | R. F. Regtuit | *Scholia in Aristophanem*, Pars III (*Scholia in Thesmophoriazusas, Ranas, Ecclesiazusas et Plutum*), fasc. 2-3 : *Scholia in Thesmophoriazusas et Ecclesiazusas*, Groningue, Egbert Forsten (titres de la Pars III et du fascicule d'après *BMCR* 2008.09.24 et la notice Zenon du DAI) | **seule édition critique moderne** ; dernier fascicule de l'édition de Groningue (1960-2007) ; numérotation propre des scholies (ex. « 162a ») | non disponible *[ISBN non établi : la notice Zenon de la Pars III énumère plusieurs ISBN sans les attribuer aux fascicules ; seul 978-90-6980-173-5 a le format en usage à partir de 2007]* |

Remarques :
- **Ce que vaut chaque édition pour le texte.** Dübner reste commode, mais il place parfois mal les notes (v. 203 pour 196, v. 214 pour 207, v. 397 pour 390) et omet souvent les lemmes de R. Rutherford est seul à séparer le texte établi (avec ses lemmes de rédacteur, souvent absents de R) et la transcription de R en bas de page. Les vrais lemmes de R se lisent donc dans ce bas de page et chez Martin, pas dans le texte imprimé.
- **Collation de Holzinger** (*WS* 4, 1882, pp. 22-23). Une cinquantaine de corrections à Dübner et à Dindorf, sous forme « vers, ligne ». Elles touchent le texte des scholies, presque jamais celui d'Aristophane. Reprises dans le relevé : τερατολογίαν (135, 14) ; ἐποίησεν (162, 37) ; ἔσσοιτο (126, 50) ; ἐκ σοφῆς Μελανίππης (272, 54) ; gloses λέγειν (178) et Μνησίλοχος (266) ; σὺν τῷ Ν̄, « offenbar entstanden aus σὺν τῶι Ῑ » (346, 49) ; σμώσχειν, puis ἄλλως… ἐπισμῇ (389, 27) ; ὁμοῦ ἀντί (572, 44) ; et surtout une scholie absente de Dübner, au v. 566 : καταγελάσει μου χωρὶς ζημίας· προῖκα γὰρ ἔλεγον τὴν ζημίαν. Sur tous ces points, Martin et Rutherford concordent avec lui, sauf détail. Elle n'apporte aucune variante d'Aristophane que Martin n'ait pas.
- Le Ravennas, provenant de la bibliothèque d'Urbino, a servi de modèle à la Juntine (Florence, 1515) pour la *Lysistrata* et les *Thesm.* (identité établie par Velsen, *Über den Codex Urbinas der Lysistrata und der Thesmophoriazusen*, Halle, 1871 ; rappel chez Zacher 1888) ; il fut retrouvé à Ravenne vers 1790 (Invernizi, cité par Rutherford I, p. XIV, n.).
- Selon Tordoff, ni Dübner ni Enger n'ont revu R eux-mêmes ; Rutherford fut le premier à fonder une édition sur une étude complète du manuscrit ; l'édition de Regtuit le remplace, avec un parti pris conservateur.
- Des chercheurs ont continué à citer Dübner pour ces scholies (bibliographie du *Center for Hellenic Studies*, résultat de recherche du 26/10/2026) : pour l'édition, citer Regtuit avec, au besoin, la concordance Dübner.

## 4. Versions numériques

| Ouvrage | Accès libre | Local |
|---|---|---|
| Dübner 1842 | archive.org `scholiagraecain00unkngoog` (Google) et `scholiagraecaina00dbuoft` | PDF + texte ; index du corpus (« Σ Ar. (Dübner) », colonnes rétablies) |
| Rutherford 1896-1905 | archive.org `scholiaaristopha01ruthuoft` (I), `scholiaaristoph00ruthgoog` (II), `scholiaaristopha03ruthuoft` (III) ; BSB `bsb11798156` (I), `bsb11798157` (II) | PDF + texte ; index (« Rutherford, Schol. Ar. I-II ») ; pp. 440-510 du t. II en images BSB |
| Martin 1882 | archive.org `lesscoliesdumanu00martuoft` | index (« Martin 1882 ») ; PDF et OCR dans `.sources/drive/ravennas/` |
| Holzinger 1882 ; 1883 | archive.org `wienerstudien04unkngoog` ; `berdieparepigra00holzgoog` | PDF + texte dans `.sources/web/etudes/holzinger/` |
| Bekker 1829, Thiersch 1832, Fritzsche 1838, Dindorf 1838, Enger 1844, Invernizi t. XI, Portus 1607, Kuster 1710 | archive.org, Google Books, BSB (voir `recherche/bibliographie_editions.md`) | `.sources/web/editions/` |
| Bourdin 1545 | Gallica, bpt6k857402r (accès automatisé bloqué par Cloudflare) | Drive de l'auteur (téléchargement en cours) |
| Regtuit 2007 | aucun | — |
| R (images) | serveur IIIF de la Classense | `dossier_ravennas_thesmophories/` |

## 5. Études

- O. Schneider, *De veterum in Aristophanem scholiorum fontibus*, Stralsund, 1838 (cité par Dübner, *adnotatio*, p. 507) *[non consulté]*.
- A. Martin 1882 et C. R. von Holzinger 1882 (ci-dessus) : collations et description de R.
- K. Holzinger, *Über die Parepigraphae zu Aristophanes. Eine Scholienstudie*, Vienne, 1883 (lu ; archive.org `berdieparepigra00holzgoog`). Il définit les parépigraphes comme d'anciennes notes interlinéaires de contenu scénique, écrites au-dessus du vers (pp. 19, 22 n. 1). R en garde sept : deux aux *Acharniens* (vv. 113-115), deux aux *Grenouilles* (vv. 312, 1264), une aux *Oiseaux* (v. 222), deux aux *Thesm.* (après les vv. 129 et 276) (pp. 19-22). Pour les *Thesm.* : (a) ὀλολύζει n'est tiré ni du v. 130, ni de la scholie, qui ne fait que le paraphraser ; il est donc plus ancien qu'elle (pp. 20-21) ; (b) après le v. 276, la scholie παρεπιγραφή· ἐκκυκλεῖται ἐπὶ τὸ ἔξω τὸ θεσμοφόριον omet ὀλολύζουσι et récrit le reste : ses mots ne sont pas la parépigraphe, contre Droysen (pp. 21-22) ; (c) le v. 100 donne l'exemple d'une parépigraphe sortie du texte et déjà contestée (p. 22 n. 1) ; παρεπιγράφεται s'y comprend comme une ligne écrite le long d'une autre et au-dessus d'elle. Il refuse d'attribuer ces notes au poète, contre Fritzsche (p. 23), et y voit des remarques de lecteurs sur le jeu, tirées du souvenir de la représentation et entrées dans les copies que reçurent les Alexandrins (pp. 24-26).
- K. Zacher, *Die Handschriften und Classen der Aristophanesscholien* (1888) : description codicologique de R et de la disposition des scholies (lu).
- W. G. Rutherford, *Scholia Aristophanica* III (1905) : histoire de l'annotation *[non dépouillé pour les Thesm.]*.
- R. Tordoff, *BMCR* 2008.09.24 (lu) : bilan de l'édition de Groningue et de l'histoire éditoriale des scholies des *Thesm.*
- À dépouiller : prolégomènes de Regtuit (2007) ; introduction d'Austin–Olson (2004) sur la tradition (Drive, non téléchargé) ; manuels généraux (E. Dickey, *Ancient Greek Scholarship*, 2007 ; travaux de F. Montana sur les corpus scoliastiques) *[non consultés, pages à préciser]*.

## 6. Apports pour l'édition

Relevé complet : `edition/donnees/scholies_temoins.tsv`, 170 lignes (106 paraphrases ou gloses, 24 lemmes, 16 attributions, 12 variantes explicites, 5 citations, 4 notes de métrique, 3 parépigraphes). Colonnes : vers (numérotation du texte de l'auteur), type, texte de la scholie (d'après R), leçon impliquée, leçon de R (folio, ligne), références à Dübner, Rutherford II et Martin avec la place dans R, présence dans les apparats de Velsen, Wilson, Enger et de l'auteur (« R seul » : l'apparat donne la leçon de R sans la scholie), statut, contrôle sur l'image, remarque. Le relevé retient les scholies qui touchent au texte, non les gloses banales qui ne font que confirmer un mot sûr. La leçon de R est contrôlée sur l'image pour 128 lignes ; pour les 42 autres, elle vient de Velsen ou des inventaires, et la colonne `verif_image` le dit.

Les scholies ne gardent donc pas un seul cas de variante, comme le disait la version précédente de cette notice, mais une douzaine de variantes déclarées et plus de trente leçons qui s'écartent de R.

### 6.1 Variantes explicites

| v. | Formule | Leçon de la scholie | R | Apparats |
|---|---|---|---|---|
| 99-100 | ἀξιοῦσί τινες γράφειν | parépigraphe μινυρισμός | rien | Enger seul |
| 141 | γρ. | σύ τ' αὐτός | τίς δ' αὐτός | tous |
| 162 | ἐν ἐνίοις… τὰ παλαιότερα ἀντίγραφα | Ἀχαιός ; Ἀλκαῖος dû à Aristophane de Byzance | κ' ἀλκαῖος | tous |
| 346 | γρ. ἔν τισιν ; ἐὰν μὲν ἄνευ τοῦ ι… | ἑταίρα, à côté de ἑταίρᾳ | ἑταῖρα | Enger, auteur |
| 393 | τὰ πλεῖστα… ἔχει | οἰνοπίπους (et οἰνοπίπας) | οἰνοπότιδας | Wilson, Enger, auteur |
| 567 | sans formule | ποκάδας, puis πλοκάδας implicite | ποκάδας | Wilson, auteur |
| 838 | ἐὰν δέ… | ὑστάτην | ὑστέραν (corr. ex ὕστερον) | Wilson, Enger, auteur |
| 917 | τὸ χ παράκειται… Καλλίστρατος | τῇ λαμπάδι / τῇ δᾳδί (texte lacunaire) | τῇ λαμπάδι | Enger |
| 1040 | γρ. | φῶτα ἀντομένα(ν) | φῶτα λιτομέναν | tous sauf Velsen |
| 1051 | δι(χῶς) | τὸν ἄθλιον | τὸν βάρβαρον | Velsen, Wilson, Enger |
| 1083 | χωρὶς τοῦ ε γράφεται | λαλῖς | λαλεῖς corrigé par R² | Wilson, Enger, auteur ; Velsen sans la scholie |
| 1176 | δι(χῶς) | κωμοδρίαν | κωμοτίς | Wilson, Enger, auteur |

Les vv. 162 et 346 montrent que le scholiaste compare des exemplaires et date les leçons. Au v. 162, R a le texte d'Aristophane de Byzance. Au v. 1051, Velsen rapporte διχῶς à la double explication du v. 1050 : ce cas n'est donc pas sûr. Même doute au v. 1176, où Enger voit l'explication d'une faute.

### 6.2 Lemmes

R n'a de lemmes que sur quelques notes (24 relevés). Ils concordent avec le texte, à l'orthographe près (vv. 168, 1007), sauf deux fois :

- v. 3 : οἷόν τε, contre οἷόν τι ; le lemme est aujourd'hui illisible sous une tache de réactif et repose sur Martin et Rutherford ;
- v. 21 : οἷόν γε ποὔστιν, contre οἷόν τε π' οὔστιν (lu sur l'image en marge inférieure).

Lemmes qui valent preuve pour R : v. 80 ἐπεὶ τρίτη 'στί, avec toute la discussion sur « troisième » et « du milieu », contre ἐπείπερ ἐστί de Nauck, imprimé par Wilson et par l'auteur ; v. 135 Λυκουργίας ; v. 168 φιλοκλεῖς ; v. 389 οὐκ ἐπισμῇ ; v. 811 τάλαντα. Le lemme du v. 33 confirme le vers suppléé en marge.

### 6.3 Paraphrases qui supposent une autre leçon

- **Déjà dans les apparats** : vv. 39 λαός (citation), 179 καινῇ, 220 ξυροδόκης, 273 Ἱπποκράτους, 289 χοιρίον, 300 sans τῇ Γῇ, 834 Στηνίοισι, 910 ἰφύων, 947 παίσωμεν, 1044 ἀμφέδυσεν, 1102 Γόργος, 1190 οὐκὶ πιλῆσι, 1197 συβήνην, 1203 ταυτί, 1214 διέβαλε.
- **Absentes des quatre apparats comme témoignages sur le texte, à ajouter** :
  - v. 53 : ὡς ἀπὸ τῶν οἰκούντων (Bekker οἰκοδομούντων) ne convient qu'à ἁψῖδας, non à ἀσπίδας de R ;
  - v. 61 : συγκάψας (Dindorf συγκάμψας) appuie le composé συγγογγύλας d'Enger, contre γογγυλίσας de R (Rutherford l'avait vu) ;
  - v. 790 : παρακύπτουσαν appuie ἐκκύψασαν de Reiske, contre ἐγκύψασαν ;
  - v. 804 : δῆλα τὰ ἔργα garantit δῆλα, contre δηλαδῆ de R ;
  - v. 941 : μετὰ κροκωτοῦ suppose μὴ 'ν, contre μὴν de R ;
  - v. 173 : κακὸς ἤμην donne au moins la 1re personne, pour ἦν / ἦ.
- **Attestation du vers contre une athétèse** : vv. 12 (van Herwerden), 38 (Dindorf), 242 (Cobet), 575 (Cobet), 1083-1085 (Velsen).
- **Confirmation de R contre le texte imprimé** : v. 105 εὐπίστως, contre εὐπείστως de Wilson et de l'auteur ; v. 419 ἐκ τοῦ ταμείου λαβεῖν, contre λαθεῖν de Velsen et de Wilson ; v. 533 Ἀγραύλου, contre Ἄγλαυρον de tous les éditeurs ; v. 781 τὸ ῥῶ, contre τορῶ de l'auteur ; v. 1085 σί, contre τί de Coulon ; v. 557 σῖτον, contre οἶνον, car κατεχρήσατο suppose la leçon de R.
- **Notes de grammairien utiles** : v. 500 (βίαιοι συστολαί), v. 547 (anapeste au dernier pied, qui garantit Πηνελόπην δέ), v. 282 (duel περικαλλέε), v. 828 (confusion στρατιά / στρατεία), v. 1001 et 1007 (barbarismes du Scythe), vv. 295 ss. (prose).

### 6.4 Points où les apparats vont au-delà de R

- v. 125 : on écrit « δόκιμον Σ ». Aucune scholie de R n'a δόκιμον : R a δοκίμῳ, puis δοκίμου οὔσης, d'où Dindorf a tiré δόκιμον (image, marge sup. de f164r).
- v. 299 : « Πλούτωνι Σ » (Velsen, Enger, Prato ; Wilson : « cf. sch. »). La scholie dit seulement ὡς ἀνδρὶ τῆς Περσεφόνης.
- v. 1214 : « διέβαλέ Σ ». Il n'y a pas de lemme ; on infère l'aoriste de la glose ἐξηπάτησε.
- v. 1227 : Wilson écrit « πέπαισται lm. sch. R », Velsen « scholiasta ». La marge de R porte πέπαικτ(αι), glose en forme commune : ni lemme, ni πέπαισται. L'entrée correspondante de l'auteur est mal numérotée (1127).
- v. 1019-1020 : κατάνευσον R : ἀπόπασον Σ (Prato) n'est pas une variante ; la scholie cite Euripide.

### 6.5 Parépigraphes

Trois lieux : ὀλολύζει (après le v. 129, R ὀλολύζεις γέρων, Souda ὀλολύζει ὁ γέρων) ; ὀλολύζουσί τε ἱερὸν ὠθεῖται (après le v. 276, attesté aussi par ολολυ[ de PSI 1194) ; μινυρισμός (v. 100, seulement dans la scholie). Velsen fait venir ἔκ de ἔκσπευδε (v. 277) de la parépigraphe. La ligne ἀνακύπτη καὶ παρακύπτι ἀπεψωλημένος (après le v. 1187) est, selon Rutherford, une indication de jeu ; Holzinger ne la compte pas. Proposition pour l'édition : les imprimer dans le texte en petit corps, avec renvoi à Holzinger, et discuter la lecture de Fritzsche (ὀλολύζουσι· τὸ ἱερὸν ὠθεῖται).

### 6.6 Autres usages

1. **Scholies et Souda** : la Souda transmet des scholies à la pièce, souvent plus complètes que celles de R ; elles servent à corriger la scholie et parfois le texte (voir `recherche/testimonia.md`). Il ne faut pas compter deux fois un même témoignage : au v. 910, l'ἰφύων de la Souda vient de la scholie.
2. **Transcription diplomatique** : Martin et le bas de page de Rutherford permettent de contrôler la lecture des scholies sur les images de R. Au v. 179, avant μεγάλῃ, restent sous la tache les lettres ..νη, peut-être un lemme perdu *[à vérifier sur l'original]*. Plusieurs marges sont aujourd'hui moins lisibles qu'au temps de Martin, à cause d'un réactif moderne (ff. 162v, 164v et autres : `ravennas/graphologie/chapitres/3_scholies_tachygraphie.md`, § 8).
3. **Données dramatiques** : notices initiales, sigles et indications de personnages ; 16 cas sont au relevé (vv. 32, 71, 263, 295, 383, 603, 760, 868, 1056, 1063, 1090, 1172, etc.).
4. **Scholies récentes de Dupuy** : à ne pas confondre avec R. Elles donnent ὅπου (v. 376), ἐσχάρας (v. 912), κλαύσαις ἄν (v. 1088), οὐ φιλήσεις (v. 1190).

## 7. Vérifications à faire

Faits le 01/11/2026 : Holzinger 1882 et 1883 lus ; confrontation des lemmes, variantes et paraphrases avec Dübner, Rutherford II, Martin, R et les quatre apparats (`edition/donnees/scholies_temoins.tsv`).

1. Obtenir Regtuit 2007 (ISBN, numérotation des scholies, prolégomènes ; intitulé établi d'après *BMCR* et Zenon) : c'est l'édition à citer. Le relevé devra être repris sur son texte et recevoir sa numérotation.
2. Bourdin : contrôler la date (1545, d'après Kuster et Dindorf ; le fichier du Drive porte « 1540 ») sur la page de titre de l'exemplaire Gallica.
3. Dupuy (Puteanus) : identifier l'exemplaire annoté de l'édition de Froben (BnF) et relever ses scholies aux *Thesm.*
4. Mu2 (Monacensis gr. 492) : présence et nature des scholies.
5. Enger 1844 : nature des scholies ajoutées (Souda ?).
6. Concordance des numéros de scholies (Regtuit) avec Dübner et Rutherford pour les scholies citées dans l'apparat et le commentaire de l'auteur.
7. Sur l'original de R ou sur de meilleures images : lemme du v. 3 (tache) ; lettres ..νη au v. 179 ; absence du signe χ au v. 917 ; lecture τεριπό / στεριπό au v. 1185 (Wilson et Velsen divergent).
8. Lire le renvoi de Dindorf à *Vesp.* 1390 pour le v. 917 (imprimé peu net chez Dübner, p. 512).
9. Dans l'apparat de l'auteur : corriger le numéro de l'entrée πέπυσται / πέπαισται (1127 pour 1227) et ajouter les témoignages du § 6.3, à discuter avec lui.
