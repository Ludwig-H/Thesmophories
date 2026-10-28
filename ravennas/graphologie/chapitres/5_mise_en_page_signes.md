# Chapitre 5 — Mise en page, notae personarum, ponctuation, accentuation, colométrie

*Étude graphologique de R (Ravenne, Biblioteca Classense, ms. 429), Thesmophories, ff. 162v–177r (vv. 1–1231).*

> **État** : chapitre rédigé le 28 octobre 2026 (sections 1–11), à partir des trente inventaires de page et de contrôles propres sur les images ; § 10 : contrôles effectués ; § 11 : corrections apportées aux inventaires. À soumettre à la vérification adversariale du chantier.

## Sources, conventions, méthode

- **Inventaires de page** : `../folios/fXXX.md` (synthèse) et `../folios/fXXX.jsonl` (une observation par ligne). Je cite une observation par « fXXX #n », n étant le rang de la ligne dans le JSONL (à partir de 0). Spécimens : `../specimens/fXXX/` ; planches de ce chapitre : `../planches/5_*.jpg` ; vues de contrôle (non versionnées) : `.travail/chap5/vues/`.
- **Littérature** : d'après `recherche/ravennas_dossier.md` (§§ 8, 11, 12), cité « Velsen 1871, p. », « Velsen 1883 », « van Leeuwen 1904 », « Coulon 1928 », etc. Je sépare toujours ce que j'observe (« sur l'image ») de ce qu'affirment les auteurs.
- **Folios et lignes** : foliotation ancienne de la littérature (ff. 162v–177r), qui est aussi celle des fichiers ; la Classense numérote au crayon +2 (« 164v » pour f. 162v). « l. » = ligne de texte de la colonne, comptée de 1 à 43 sur chaque page. Vers : numérotation de l'édition (texte de l'auteur), qui suit Velsen 1883 / Hall–Geldart, sauf mention.
- **Mains** (étiquettes du chapitre 1 et de `ravennas/FORMAT_TRANSCRIPTION.md`) : **T** = copiste du texte (`R1`) ; **S2** = main des scholies, correcteur ancien (`R2` ; « schol. m. » de Velsen 1871, « R² » de Velsen 1883, « corrector » de van Leeuwen) ; **main de 1516** = main du XVIe siècle qui prépare la copie d'impression de la Juntine (`Rrec` ; « 2 m. » de Velsen 1871, « manus recens » de van Leeuwen, « B16 », « main rousse » ou « main tardive » dans certains inventaires ; l'attribution à Euphrosynus Boninus n'est pas démontrée, dossier § 0, 7). **G** = Monacensis gr. 492 (XVe s.), copié sur R avant 1516 : une note de R que G reproduit est donc antérieure à la main de 1516.
- **Mesures** : rapports d'absorbance G/R et B/R des inventaires (encre brune de T et de S2 ≈ 1,2–1,45 / 1,8–2,6 ; encre orangée de 1516 ≈ 1,45–1,9 / 2,5–4,0, selon les pages). 1 px ≈ 0,116 mm (0,125 mm sur certaines images).
- **Statistiques** : les comptages des §§ 3–4 proviennent d'un dépouillement semi-automatique des tableaux de sigles des inventaires (`.travail/chap5/parse_T.py` → `.travail/chap5/marques_T.tsv`), confronté aux attributions de l'édition (`edition/donnees/travaux_anterieurs/texte_grec.tsv`) par `.travail/chap5/convention.py`, puis relu à la main. Ils sont donnés en ordre de grandeur.

## Conclusions principales

1. **Cadre fixe.** Chaque page est réglée à la pointe sèche pour **43 lignes** (y compris le f. 162v, où la 2e réglure reste blanche sous le titre) ; justification ≈ 103–104 mm ; double verticale à gauche, qui ménage une **bande des sigles** de 6–7 mm où T pose ses paragraphoi ; écriture **suspendue** sous la réglure.
2. **Pas d'apparat de titre** : titre de T en majuscule de distinction, à l'encre du texte, **sans rubrique**, sans hypothesis ni liste de personnages ; pas de souscription finale. La notice et le « προλογίζει μνησίλοχος κηδεστὴς εὐριπίδου » de la marge supérieure du f. 162v sont de la main des scholies.
3. **Colométrie** : un côlon par ligne, renfoncement (eisthesis) variable des parties lyriques, ekthesis des vers longs ; les fins de ligne de R coïncident avec les relevés de Velsen 1883 (« RG ») dans les quatorze passages contrôlés, et la Juntine les reproduit. Quinze mots sont coupés en fin de ligne, un seul avec trait d'union. La scène d'Écho est mise en page sur deux « colonnes » séparées par une paragraphos en milieu de ligne.
4. **T ne nomme aucun personnage.** Ses seules marques sont la paragraphos (en tête de ligne), le dicolon (dans la ligne ou en fin de ligne), et parfois un blanc ou un point simple. Il omet beaucoup : environ un tiers des changements en tête de vers n'ont pas de paragraphos.
5. **La paragraphos de T garde des traces de l'usage antique** : dans environ deux cas possibles sur cinq (25 sur 61), elle se trouve en tête du vers qui *suit* un changement intérieur, c'est-à-dire sous la ligne où le changement a lieu. Dix-sept paragraphoi tenues pour « fausses » (barrées ou grattées par la main de 1516, ou jugées telles par les inventaires) s'expliquent ainsi ; d'autres marquent une division du discours. Une paragraphos en tête du v. *n* ne prouve donc pas un changement de locuteur en tête du v. *n*.
6. **Trois couches de sigles** : aucune de T ; des sigles abrégés à lettre suscrite de S2 (Xe s., encre brune, semi-onciale) ; des sigles « imprimables » de la main de 1516 (encre orangée), qui sont ceux de la Juntine et n'ont aucune valeur de tradition.
7. **Le nom du Parent.** S2 l'appelle surtout **Μνησίλοχος** (près de trente sigles et notes : μνη^σ, μνησι^λο, μ·…) et seulement cinq fois **κηδ(εστής)** (vv. 466, 540, 603, 1107, 1207), comme dans sa notice initiale qui donne les deux noms. La main de 1516 écrit μν partout, sauf aux vv. 466–604 et 1209, où elle reprend le κηδ de S2 voisin. R ne donne donc aucun appui à « Κηδ. R passim » (Coulon 1928) : la désignation dominante du manuscrit est Μνησίλοχος, et les deux désignations sont byzantines, non de T.
8. **Ponctuation de T** : point (surtout médian), point-virgule « ; » (interrogation ou pause), virgule basse, dicolon de pause, tirets de fin ; à transcrire signe pour signe, en distinguant les vrais dicola des faux (ι adscrit en deux touches, esprit ou accent de la ligne voisine).
9. **Accentuation complète mais non normalisée** : graves et aigus fautifs, doubles accents, esprits souvent omis ou indistincts (doux/rude), parfois rejetés dans la bande des sigles ; un correcteur ancien a changé une quinzaine de graves en aigus devant ponctuation ou enclitique (accents « en V », « en ✓ » ou « en croix »). **Iota adscrit** sur la ligne, irrégulier, jamais souscrit. **Apostrophe** notée de façon irrégulière, et ajoutée après οὐκ / οὐχ (οὐκ᾽), habitude du copiste.

---

## 1. Mise en page

### 1.1 Le cadre : réglure, lignes, justification

**Réglure.** Elle est faite à la pointe sèche, sans encre, et n'est visible qu'en lumière rasante numérique (filtre passe-haut, CLAHE, canal bleu). Le schéma est le même sur toutes les pages où les inventaires ont pu la suivre (par ex. f163r #66, f164v #90, f165r #1, f169r #3, f170v #31, f172v #2, f175r #1, f176v #1, f177r #1) :

| Élément | Position | Remarques |
|---|---|---|
| horizontales | pas de 42,0–43,8 px, soit ≈ 4,9–5,1 mm | prolongées dans les marges ; deux horizontales marginales en tête et en pied (par ex. f172v, f174v, f177r) |
| double verticale gauche | écart ≈ 50–60 px (6–7 mm) | la ligne intérieure porte le début des trimètres ; la bande entre les deux est la **bande des sigles**, où T place ses paragraphoi (f164v #90, f165r #1, f166v #1, f176r #55) |
| double verticale droite | même écart | les vers longs (tétramètres) la dépassent souvent (f169r, f171r, f172v) |
| verticale de la marge extérieure | à ≈ 50–60 mm du texte | borne la colonne des scholies (f163v, f174v, f176v #80) |

La justification (de la verticale intérieure gauche à la verticale droite) mesure ≈ 886–896 px, soit **≈ 103–104 mm** (f169v #47, f170v #31), ce qui concorde avec les 0,103 m de Zacher 1888, 534. Le copiste écrit **suspendu sous la réglure** (sur toutes les pages), les scholies ne suivent pas la réglure du texte (≈ 25 px par ligne, f165v).

**Nombre de lignes.** Toutes les pages sont réglées pour **43 lignes**, et toutes les 43 sont écrites sauf aux ff. 162v et 177r :
- **f. 162v** : l'inventaire compte « 42 lignes réglées » (titre + 41 vers). Le titre est sur la première réglure (sillon à y ≈ 370–372, f162v #2) ; la ligne de base du v. 1 est à y ≈ 490, soit **deux pas** plus bas. Sur un profil passe-haut du canal bleu, mesuré dans trois bandes verticales de la marge (x 1500–1600, 1600–1700, 1730–1800), on retrouve un sillon horizontal à y ≈ 409–416, entre le titre et le v. 1, puis à y ≈ 454–458 (réglure du v. 1). La page a donc, comme les autres, **43 réglures, dont la 2e est restée vide** sous le titre (vue de contrôle `.travail/chap5/vues/f162v_titre_reglure_hp.png` ; correction de f162v #19, à confirmer sur l'original).
- **f. 177r** : 23 lignes pour les vv. 1211–1231, une réglure vide, une ligne ornementale, le titre de l'*Assemblée*, 12 lignes d'hypothesis et 5 réglures vides (f177r #0, #45 ; § 1.3).
- Les nombres différents de la segmentation automatique (`ravennas/segmentation/`) sont des erreurs de celle-ci : 42 lignes au f. 168r (l. 43 manquée), 42 au f. 171r (l. 3 omise ; table corrigée dans `.travail/graphologie/f171r/lignes_ms.json`), 45 au f. 175v (les deux lignes des vv. 1102–1103 ajoutées dans la marge inférieure), 34 au f. 177r (lignes fusionnées).

**Bornes des pages.** Les noms des fichiers d'images sont souvent faux (dossier § 1). Contenu vérifié par les inventaires :

| Folio | Vers | Particularités de mise en page |
|---|---|---|
| 162v | titre, 1–42 | titre (l. 1, réglure 2 vide) ; v. 33 omis, suppléé en marge droite (S2) ; vv. 27–30 copiés 27, 29, 30, 28, remis en ordre par α–δ ; anapestes 39–42 renfoncés |
| 163r | 43–79 | anapestes 43–62 en côla (ll. 1–26) |
| 163v | 80–122 | lyrique 101–122 renfoncé (ll. 22–43) |
| 164r | 123–164 | fin du chant (ll. 1–7) ; **parépigraphe** ὀλολύζεις γέρων (l. 8) |
| 164v | 165–208 | v. 169 omis, suppléé en marge extérieure |
| 165r | 209–251 | trimètres seuls |
| 165v | 252–293 | **parépigraphe** ὀλολύζουσί τε· ἱερὸν ὠθεῖται (l. 26) |
| 166r | 294–336 | prière en prose (ll. 2–16), formule finale en saillie (ll. 17–18), chant (ll. 19–37) |
| 166v | 337–379 | chant 352–371 renfoncé ; dernière page du cahier XXI |
| 167r | 380–422 | trimètres et deux tétramètres (381–382) non distingués ; signature « 22 » (moderne) en pied |
| 167v | 423–465 | chants 434–442 et 459–465 |
| 168r | 466–508 | trimètres |
| 168v | 509–550 | chant 520–530 ; tétramètres 531–550 ; ἁπαξ ἁπάσας seul, centré et souligné (l. 43) |
| 169r | 551–592 | v. 567 coupé en deux lignes à la réplique (ll. 17–18) |
| 169v | 593–635 | trimètres |
| 170r | 636–678 (Velsen ; HG 636–677) | v. 647 omis, suppléé en marge droite ; ἀθρῆσαι seul, centré (l. 23) ; v. 675 sur trois lignes |
| 170v | 679–720 | interjections ἄ α· (l. 11) et ἔα ἔα (l. 22) seules, centrées |
| 171r | 721–763 | fin de chant renfoncée (ll. 1–5) |
| 171v | 764–800 | monodie 776–784 ; tétramètres anapestiques en saillie, six débordements sur ligne courte |
| 172r | 801–834 | neuf tétramètres coupés en deux lignes ; pnigos ; signal ⋎ de T (l. 12) |
| 172v | 835–876 | v. 874 coupé en deux lignes à la réplique (ll. 40–41) |
| 173r | 877–919 | deux côla dochmiaques renfoncés (ll. 37–38) |
| 173v | 920–958 | l. 15 annulée (anticipation de 934) ; ἱστιορράφος seul (l. 18) ; anapestes et lyrique (ll. 30–43) |
| 174r | 959–1001 | page presque entièrement lyrique |
| 174v | 1002–1044 | monodie d'Andromède (ll. 14–43), dernière page du cahier XXII |
| 175r | 1045–1081 (οἴμωζ᾽) | monodie (ll. 1–11), trimètres, scène d'Écho (ll. 21–43) |
| 175v | 1081 (ὀτότυζ᾽)–1126 | scène d'Écho (ll. 1–16) ; vv. 1102–1103 omis, suppléés en marge inférieure |
| 176r | 1127–1168 | hymne 1136–1159 (ll. 10–34), avec une ligne exponctuée (l. 17) |
| 176v | 1169–1210 | **ligne supplémentaire** ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημένοσ· après 1187 (l. 20) |
| 177r | 1211–1231 ; titre et hypothesis de l'*Assemblée* | ἀρταμουξία en ligne propre (ll. 4, 8, 15) |

### 1.2 Marges et répartition des notes

Sur un verso, la marge extérieure (large) est à gauche et la marge intérieure (étroite, contre le pli) à droite ; c'est l'inverse sur un recto. La disposition est constante :
- **scholies de S2** dans la marge extérieure, ancrées à la hauteur du vers commenté ; elles commencent souvent par un tiret « en vedette » et finissent par « ÷ » (f166r #55 ; f163v #57) ; elles sont écrites après le texte, en partant de la fin de la ligne de texte (f168r) ;
- **gloses et scholies courtes** dans la marge intérieure ; parfois dans un blanc de la colonne : l. 20 du f. 163r (χωνεύει), ll. 2 et 7 du f. 170v (à droite d'une ligne lyrique courte), l. 37 du f. 173r (dans le renfoncement), l. 18 du f. 173v ;
- **marges supérieure et inférieure** rarement employées : notice du f. 162v, six lignes en tête du f. 163v, trois en tête et huit en pied du f. 164r, deux en tête des ff. 164v et 167v, une en tête du f. 168v, scholie de six lignes en pied du f. 162v.

Les signes de renvoi de S2 sont rares mais réels (ff. 163v l. 17 ; 164r ll. 5, 10, 14 ; 166v ; 169r ll. 15–16 ; 170r ; 175r l. 12 ; 175v l. 20) : leur relevé relève du chapitre 3 (`3_scholies_tachygraphie.md`).

### 1.3 Titre, absence d'hypothesis et de liste de personnages, fin de la pièce

**Le titre (f. 162v, l. 1 ; planche `../planches/5_planche_mise_en_page.jpg`).** « ἀριστοφάνους· ·θεσμοφοριάζουσαι », en **majuscule de distinction** de T (semi-onciale inclinée : σ et ε lunaires, ν en N, ζ en Ƶ, φ à boucle fermée, α final en d), de module plus grand que le texte (≈ 25 px contre 18–20 px), précédé d'un **ornement en astérisque** (quatre traits incurvés autour de trois ou quatre points) et suivi d'un trait montant (f162v #0, #1 ; spécimens `../specimens/f162v/f162v_l01_aristophanous.png`, `../specimens/f162v/f162v_l01_ornement.png`, `../specimens/f162v/f162v_l01_trait_final.png`). Les deux points entre les mots sont des points séparateurs, non un dicolon (f162v #2, `../specimens/f162v/f162v_l01_points.png`). Le titre est accentué. **Il est à l'encre du texte : il n'y a aucune rubrique** dans les *Thesmophories* de R (vu sur l'image ; aucune source ne signale de rubrication dans R, dossier § 8.1). Le titre « Θεσμοφοριάζουσαι πρότεραι » prêté à R par Fritzsche et Enger ne s'y lit pas (dossier § 0, 14).

**Pas d'hypothesis ni de liste de personnages de T.** La marge supérieure porte une notice de deux lignes et demie sur la pièce (début effacé ; « … καὶ τοῦτο τὸ δρᾶμα τῶν κατ᾽ Εὐριπίδου πεποιημένων ἀπὸ τῶν Θεσμοφορίων … »), puis, centrée au-dessus du titre, la ligne **« προλογίζ(ει) μνησίλοχ(ος) κηδεστ(ὴς) εὐριπίδου »**, toutes deux dans la minuscule des scholies, que les indices (lemmes en semi-onciale, Z majuscule) rattachent à S2 (f162v #54, #55 ; `../specimens/f162v/f162v_marge_sup_hypothesis.png`). Ce ne sont pas des éléments de la mise en page de T, mais des notes du scholiaste.

**Fin de la pièce (f. 177r).** Après le v. 1231 (τούτων χάριν ἀνταδοῖτον·), **pas de souscription** (τέλος …) : la 24e réglure reste vide ; à la 25e, une **ligne ornementale** (tirets et petits crochets, avec un fleuron en plume aux deux bouts) ; à la 26e, le **titre de l'*Assemblée*** : « ὑπ(όθεσις) ἐκκλησιαζουσῶν ἀριστοφάν(ους) :– », en majuscule de titre mêlée de minuscules et terminé par un dicolon et un tiret ; puis l'**hypothesis** de l'*Assemblée*, en 12 lignes de la minuscule de T, sur toute la largeur de la colonne, close par « ὦ λαμπρὸν ὄμμα :— » ; les cinq dernières réglures sont vides (f177r #0, #45 ; `../specimens/f177r/f177r_mep_ornement_titre.jpg` ; vue `.travail/chap5/vues/f177r_fin_titre_eccl.png`). Le contraste est net : l'*Assemblée* s'ouvre sur une hypothesis copiée par T, les *Thesmophories* n'en ont aucune de sa main.

**Conséquence pour la transcription.** Le titre est une ligne `<l zone="titre">` de la main R1, sans `<hi rend="rouge">` (l'exemple de `ravennas/FORMAT_TRANSCRIPTION.md` est à corriger sur ce point pour les *Thesmophories*) ; l'ornement est un `<signe type="autre">`. La notice et le « προλογίζει » sont des `<sch place="mg-sup" main="R2">`.

### 1.4 Vers omis, transposés ou ajoutés ; lignes qui ne sont pas des vers

**Vers omis par T et suppléés en marge**, chaque fois avec un signe de renvoi (sauf au v. 33) :

| Vers | Folio | Lieu de l'ajout | Main | Renvoi |
|---|---|---|---|---|
| 33 | 162v | marge droite, en trois lignes, à la hauteur des ll. 34–36 | S2 (minuscule de grand module, inclinée) ; sigles εὐ et « ; » de 1516 | aucun visible (f162v #31) |
| 169 | 164v | marge extérieure, à la hauteur des ll. 5–6 | S2 | croix « × » après le v. 168 (f164v #85) |
| 647 | 170r | marge droite, à la hauteur des ll. 9–10 | S2 | « ÷ » à barre ondulée en tête du vers ajouté et après la l. 11, « ·/· » devant la l. 12 (f170r #31, #39, #56) |
| 1102–1103 | 175v | marge inférieure, deux lignes | S2 (signes de renvoi : S2 ou main tardive) | « —+:— » après la l. 20 et « +: » en tête de l'ajout (f175v #24, #25) |

**Transposition** : vv. 27, 29, 30, 28 (f162v ll. 28–31), ordre rétabli par des lettres numérales α–δ dans la marge droite ; γ est brun (S2 ?), α, β, δ orangés (1516) (f162v #29). Le v. 28 n'est pas un ajout marginal, contrairement à Allen 1896, 316 (dossier § 0, 14).

**Lignes de la colonne qui ne sont pas des vers des éditions** :
- **parépigraphes** copiées par T comme des lignes du texte, en retrait comme les lignes lyriques : ὀλολύζεις γέρων· (f164r l. 8, départ x ≈ 345 ; sans sigle ni paragraphos ; soulignée par un lecteur postérieur d'un trait ondulé rouge pâle, matière non ferro-gallique, crayon ou craie rouge ? f164r #17, #18, `../specimens/f164r/f164r_l08_parepigraphe_trait_rouge.jpg`) et ὀλολύζουσί τε· ἱερὸν ὠθεῖται. (f165v l. 26, départ x ≈ 895 contre 770 ; précédée d'une paragraphos de T barrée par la main de 1516, f165v #57, `../specimens/f165v/f165v_l26_parepigraphe.jpg`) ;
- **ligne supplémentaire** ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημένοσ· (f176v l. 20), copiée après le v. 1187 comme un trimètre ordinaire, sans marque (Velsen 1883, 85) ;
- **ligne annulée** f173v l. 15 (anticipation du début du v. 934, barrée et exponctuée), puis l. 18 ἱστιορράφος seul (fin du v. 935 récrite après ἱστιοφόρον barré, l. 17) ;
- **ligne exponctuée** στυγνᾶς ὦσσε (f176r l. 17), ligne de plein droit dans la colonne ;
- **mots en débord** centrés sur une ligne propre : ἀθρῆσαι (f170r l. 23, fin du v. 658), ἁπαξ ἁπάσας (f168v l. 43, fin du v. 550, souligné d'un trait ondulé, f168v #47) ;
- **vers coupés en deux lignes à la réplique** : v. 567 (f169r ll. 17–18, la seconde réplique sur une ligne courte) et v. 874 (f172v ll. 40–41).

Chacune de ces lignes est une ligne `<l>` de plein droit dans la transcription (attribut `v` vide ou parties de vers ; `retrait` pour les parépigraphes).

### 1.5 Initiales agrandies et ekthesis

T n'a ni initiales ornées ni lettrines, mais il **agrandit ou fait saillir l'initiale** de certaines répliques ou sections, sans régularité :
- ω de ὦ en tête de la pièce (f162v l. 2, x 689 contre ≈ 740) ;
- ω de ὦ πρέσβυ (f164r l. 25, v. 146), grands Ο de Οὐκοῦν et de Ὅταν (ll. 32, 36 ; vv. 153, 157) ;
- **Ο agrandi de module triple, en saillie**, aux deux entrées de la première femme (f168v vv. 533, 544) ; mais aussi, sans changement, au v. 548 ;
- **Φ** de φίλαι en ekthesis, à longue queue fine, à l'entrée de Clisthène (f169r l. 25, v. 574), répondant à la queue en S du ξ de λέξει qui clôt les tétramètres (l. 24) : c'est la seule « marque de section » de la page (f169r #2, #46 ; `../specimens/f169r/l25_phi_initial.jpg`, `../specimens/f169r/l24_queue_xi.jpg`) ;
- **Η** initial agrandi au début des anapestes du chœur (f170r l. 19, v. 655) ;
- Π de παραδοὺς et φ de φορμὸν (f172r ll. 15, 21), dans les anapestes de la parabase.

Ce sont des indices d'appoint : ni systématiques, ni réservés aux changements de locuteur. Pour la transcription, ils ne relèvent que d'une `<note>` (ou d'un attribut de saillie s'il est adopté, § 7).

---

## 2. Colométrie des parties lyriques et anapestiques

### 2.1 Les principes observés

La colonne ne change jamais de largeur ; c'est le **point de départ des lignes** qui distingue les mètres. Les inventaires l'ont mesuré page par page (abscisse du premier trait, sur le masque d'encre ou sur des vues à règle) :

1. **Trimètres** : alignés sur la verticale intérieure de gauche, un vers par ligne, fin de ligne libre.
2. **Parties lyriques** : **un côlon par ligne**, en **renfoncement** (eisthesis) de 3–4 lettres (f163v) à 14–20 mm (f166v), souvent irrégulier à l'intérieur d'un même chant ; les côla longs repartent de l'alignement des trimètres (f164r ll. 4–6 ; f167v ll. 18, 20, 41, 43).
3. **Vers longs** (tétramètres) : soit simplement plus longs, débordant la double verticale de droite (f167r vv. 381–382 ; f169r vv. 551–573 ; f171r vv. 726–727), soit **en saillie** (ekthesis) sur la verticale extérieure (f171v vv. 785–800, 3–4 mm ; f172v vv. 835–845 ; f170v), soit, sur une page lyrique, dans la bande des sigles (f174r ll. 3, 10, 30, 43).
4. **Débordements** : la fin d'un tétramètre trop long est reportée sur la ligne suivante, renfoncée vers le milieu de la colonne (f171v : six cas, φέρε δὴ νῦν l. 26, εἴπερ ἀληθῶς l. 32, λαμβάνετ᾽ ἔνδον l. 34, καὶ κοπιῶσαι l. 36, ἐπιδήλως l. 41, ἰδέσθαι l. 43 ; f172r : neuf tétramètres sur 13 aux vv. 801–813 ; f173v : vv. 947–948). Ailleurs, T serre la fin de ligne et surélève les dernières lettres (ἀγορεύ^ει, ἅπαν^τα, ἐπιθυμ^εῖ, f171v ll. 23, 24, 39).
5. **Extra metrum** et répliques brèves sur une ligne propre : γλαυκόν, βομβάξ, σίγα· τί λέγει;, etc. (f163r ll. 3–21) ; ἄ α· et ἔα ἔα, centrés (f170v ll. 11, 22) ; πρῶ, seul et en ekthesis (f174r l. 10) ; ἀρταμουξία (f177r ll. 4, 8, 15, en retrait, mais pas au v. 1225, l. 18).
6. **Mots coupés en fin de ligne** : quinze cas, **sans trait d'union** sauf un ; T coupe aussi bien après une consonne que dans un groupe consonantique.

| Folio, lignes | Coupe |
|---|---|
| 163v, 35/36 et 36/37 | δρυογόνοι\|σι ; ἄρ\|τεμιν |
| 166v, 21/22, 27/28, 33/34 | παραβαίνου\|σί ; ἐ\|χθροῖς (l'ε prolongé en long trait horizontal) ; ὥσ\|θ᾽ |
| 171r, 3/4 | μεταβαλοῦ-\|σ᾽ (**seul trait d'union de T** : court trait à mi-hauteur, f171r #10, `../specimens/f171r/l03_trait_union.jpg`) |
| 173v, 32/33 | ἀνέχω\|μεν |
| 174r, 17/18 et 25/26 | ἐμ\|παίζει ; οἱ\|άπερ |
| 174v, 30/31 et 33/34 | ἔχου\|σ᾽ ; ξυμ\|παιῶνι |
| 175r, 23/24 | διφρεύου\|σ᾽ |
| 176r, 20/21, 28/29, 33/34 | γυναι\|κῶν ; φαι\|νετον ; ἀφίκε\|σθον |

Au f. 166r, l. 27, un **tiret** après παῖ relie la fin de ligne au côlon suivant (λατοῦς χρυσώπιδος ἔρνος), « παῖ — (sic) R » chez Velsen 1883 (f166r #24, `../specimens/f166r/f166r_l27_pai_tiret.jpg`).

**Concordance avec Velsen 1883.** Velsen consigne, passage par passage, les mots qui terminent chaque ligne de R et de G (« ita distributa sunt, ut singuli versus finiantur vocibus… RG », dossier § 8.4). Les inventaires ont vérifié sur l'image que les fins de ligne de R sont celles de Velsen pour les vv. 45–57 (f163r), 101–129 (f163v–164r), 295–330 (f166r), 352–371 (f166v), 434–442 et 459–465 (f167v), 520–530 (f168v), 721–725 (f171r), 947–958 (f173v), 959–1001 (f174r, sur les 43 lignes), 1065–1077 (f175r), 1081–1097 (f175v), 1136–1159 (f176r) et 1229–1231 (f177r). La concordance n'est pas affirmée pour les vv. 655–688 (f170r) et 1015–1055 (f174v–175r), dont la colométrie est décrite comme « propre à R ». Le sigle « RG » de Velsen montre que G reproduit les fins de ligne de R ; la **Juntine** les reproduit aussi ligne pour ligne aux vv. 295–337 (pages a 16 / b 1, f166r) et 1015–1040 (page c 13, coupures de mots et ponctuation comprises, f174v).

### 2.2 Relevé par passage

| Vers | Folio, lignes | Disposition dans R | Particularités |
|---|---|---|---|
| 39–42 | 162v, 39–42 | quatre anapestes renfoncés d'≈ 15 mm, sans changement de module | seul renfoncement de la page |
| 43–62 | 163r, 1–26 | un côlon par ligne, renfoncement variable (x ≈ 230–330 contre 205–220) | répliques brèves sur une ligne propre |
| 101–122 | 163v, 22–43 | renfoncement de 3–4 lettres, irrégulier | deux mots coupés ; dicolon en fin de l. 34 |
| 123–129 | 164r, 1–7 | ll. 1–2 très renfoncées, l. 3 moins, ll. 4–6 longues à la justification, l. 7 renfoncée | parépigraphe en retrait (l. 8) |
| 295–309 | 166r, 2–16 | prière en prose, un membre par ligne, renfoncée (x ≈ 330–385) | trois points devant ταύτην (l. 16, f166r #12) |
| 310–311 | 166r, 17–18 | **en saillie**, à l'alignement des trimètres | formule finale et péan |
| 312–330 | 166r, 19–37 | un côlon par ligne, renfoncé (x ≈ 340–365) | tiret après παῖ (l. 27) |
| 352–371 | 166v, 16–35 | renfoncement de 14–20 mm | trois mots coupés ; χ^ο de S2 logé dans le blanc du retrait (l. 16) |
| 381–382 | 167r, 2–3 | tétramètres non distingués, sauf par la longueur | — |
| 434–442 ; 459–465 | 167v, 11–20 ; 37–43 | renfoncement variable (x ≈ 910–950) ; lignes longues à l'alignement des trimètres | la l. 43 déborde à droite pour finir la strophe sur la page |
| 520–530 | 168v, 12–22 | renfoncement (x ≈ 864–901 contre 756–790) | vv. 526–527 sur la seule l. 18 |
| 531–550 | 168v, 23–43 | tétramètres longs | ἁπαξ ἁπάσας seul, centré, souligné (l. 43) |
| 551–573 | 169r, 1–24 | tétramètres longs, débordant à droite | queue en S du ξ de λέξει (l. 24) et Φ en ekthesis (l. 25) |
| 655–688 | 170r, 19–43 | anapestes 655–658 **en ekthesis** de 8–9 mm ; **lyrique 663 ss. non renfoncé** | ἀθρῆσαι seul, centré (l. 23) ; vv. 664 + 664a (l. 29) et 666 + 667 (l. 31) réunis ; v. 675 sur trois lignes ; ekthesis des ll. 26 et 31 |
| 679–688 ; 700–701 ; 707–713 ; 718–720 | 170v, 1–8, 23–24, 30–36, 41–43 | renfoncement ; trimètres sur le filet intérieur ; tétramètres légèrement en saillie | ἄ α· et ἔα ἔα centrés ; deux gloses écrites dans le blanc de lignes courtes (ll. 2, 7) |
| 721–725 | 171r, 1–5 | renfoncement (x ≈ 262–285 contre 200) | trait d'union de T (l. 3) |
| 776–784 | 171v, 13–21 | renfoncement d'≈ 17 mm | dicolon en fin de l. 21 (fin de la monodie) |
| 785–800 | 171v, 22–43 | tétramètres en saillie de 3–4 mm ; six débordements renfoncés | lettres finales surélevées |
| 801–813 | 172r, 1–22 | neuf tétramètres coupés en deux lignes, la fin renfoncée vers le milieu | départs de plus en plus à gauche (x 250 → 162) ; Π et φ agrandis (ll. 15, 21) |
| 814–829 | 172r, 23–38 | pnigos, un vers par ligne, léger retrait | monomètres aux ll. 32, 37 ; points de pause |
| 830–845 | 172r, 39–43 ; 172v, 1–11 | tétramètres trochaïques à gauche (sur la verticale extérieure au f. 172v) | — |
| 913–914 | 173r, 37–38 | deux côla dochmiaques renfoncés (x ≈ 350) | glose de S2 dans le blanc (l. 37) |
| 947–958 | 173v, 30–43 | tétramètres débordants, fins renfoncées ; dimètres et côla renfoncés | deux côla des éditions réunis (ll. 40, 41) ; ἀνέχω\|μεν |
| 959–1000 | 174r, 1–42 | côla renfoncés (x ≈ 300–380) ; vers longs en ekthesis dans la bande des sigles | deux mots coupés ; trois lignes réunissent deux côla (ll. 14, 22, 30) |
| 1015–1055 | 174v, 14–43 ; 175r, 1–11 | trente lignes toutes renfoncées (x ≈ 880–910), puis onze (x ≈ 305–335) | colométrie propre à R, reproduite par la Juntine ; κλύεισ ὦ seul (f174v l. 17) |
| 1056–1097 | 175r, 12–43 ; 175v, 1–16 | scène d'Écho (§ 2.3) | — |
| 1136–1159 | 176r, 10–34 | lignes courtes renfoncées (x ≈ 290–325) | trois mots coupés ; l. 17 exponctuée ; aucun sigle de demi-chœur |
| 1213–1231 | 177r, 4–23 | ἀρταμουξία en ligne propre renfoncée ; ll. 21–23 renfoncées | vv. 1227–1228 sur une seule ligne débordante (l. 20) |

**Exceptions et incohérences.** Le copiste n'applique pas ses principes partout : les lyriques 663 ss. du f. 170r ne sont pas renfoncés (alors que les anapestes qui précèdent sont en saillie) ; les tétramètres des ff. 167r et 169r ne sont distingués que par la longueur ; certaines lignes réunissent deux côla des éditions (f173v ll. 40–41 ; f174r ll. 14, 22, 30 ; f170r ll. 29, 31). Ces écarts sont des faits de tradition à relever dans l'apparat métrique ou dans l'introduction, non des fautes à corriger dans la transcription.

### 2.3 La scène d'Écho (vv. 1056–1097)

La mise en page de la scène est la plus élaborée de la pièce (planche `../planches/5_planche_mise_en_page.jpg` ; vues `.travail/chap5/vues/f175r_l30-43.png` et `.travail/chap5/vues/f175v_l1-16.png` ; `../specimens/f175r/f175r_sigles_l26_37.png`, `../specimens/f175v/f175v_mep_blocs.jpg`) :

- **f. 175r, ll. 21–43** (vv. 1065–1081) : lignes courtes, commençant vers x ≈ 335, précédées d'une large bande de sigles (x ≈ 250–335). Les répliques de Mnésiloque et d'Écho occupent chacune une ligne ; T met une paragraphos devant la plupart des lignes qui commencent une réplique (il n'en met pas aux vv. 1065 et 1074, ni, dans les trimètres qui précèdent, aux vv. 1058, 1059 et 1064), mais aussi devant λίαν (l. 35, v. 1076a) et παῦσαι (l. 39, v. 1078a), qui terminent des répliques de Mnésiloque : il a pris ces mots, que l'écho va répéter, pour des répliques séparées (paragraphoi barrées d'un trait gris, sans doute pour l'impression).
- **f. 175r, ll. 39–43, et f. 175v, ll. 1–16** : **deux répliques par ligne**. La première (Mnésiloque, puis le Scythe) commence à la justification ; après un blanc, la répétition d'Écho forme une **seconde colonne** (vers x ≈ 600 au f. 175r, x ≈ 1050–1250 au f. 175v), introduite par une **paragraphos de T en milieu de ligne** — trait mince, plus pâle que le texte (A_R 0,14–0,16, f175v). Exceptions : ff. 175v ll. 9–12 et 16, sans répétition ; le v. 1095 sur deux lignes (ll. 13–14) ; les répétitions d'Écho aux vv. 1093–1094 manquent dans R (l. 12).
- **Sigles.** S2 écrit des notes développées : εὐρι(πίδης) ἠχώ (f175r l. 12, v. 1056 : Euripide joue Écho), ηχω (f175r l. 26 ; f175v l. 2), ὁ μνησίλ(ο)χ(ος) ὡς ἀνδρομέδα (f175r l. 21), et la note de jeu ἠρέμα ὁ κηδεστ(ής), [τὸ] πρὸς τ(ὸν) εὐρι(πίδην) (f175r l. 19, f175r #64). La main de 1516 pose Ηχ et μν (μ réduit à un crochet aux ll. 41–43) sur les paragraphoi de T, ou greffe sur elles les hastes du Η (f175r ll. 39–43 ; f175v ll. 6–7).
- **Annulations de 1516.** La main de 1516 barre d'une haste orangée la paragraphos de milieu de ligne du v. 1092b et celles des vv. 1093 et 1095 (f175v ll. 11–13, f175v #11, `../specimens/f175v/f175v_l12_13_paragraphoi_biffees.jpg`) : ce sont pourtant de vrais changements de locuteur dans le texte de l'édition ; la Juntine n'imprime simplement pas de sigle à ces endroits.

**Conséquence pour la transcription.** La paragraphos de milieu de ligne s'encode à sa place dans la ligne (`<parag/>` suivi du texte d'Écho), précédée d'un blanc `<sp/>` ; la ligne reste une seule `<l>`.

---

## 3. Les marques de réplique du copiste : paragraphos, dicolon, blanc, point

Bekker l'avait vu : « interlocutores ubi mutantur, lineola versui praefigitur, qui Platonicis quoque codicibus mos est » (Bekker 1829, vi) ; Velsen précise que la première main marque l'entrée d'un nouveau personnage « vor dem Verse durch einen Strich (—) und in der Mitte des Verses durch zwei Punkte (:) » (Velsen 1871, 8 ; dossier § 8.2). L'image confirme ce système et en montre les limites.

### 3.1 Les formes

- **Paragraphos** : trait horizontal de 25 à 42 px (3–5 mm), **à mi-hauteur du corps des lettres**, dans la bande des sigles, juste avant le premier mot ; attaque épaissie à gauche (« en massue », « en goutte »), fin effilée à droite ; parfois à crochet initial (f162v v. 1 ; f170v ll. 38, 40). Encre du texte (par ex. 1,22/1,81 au f. 169r, l. 22 ; 1,30/2,11 au f. 164v, l. 37 ; 1,30/2,09 au f. 168v, l. 32). Spécimens : `../specimens/f162v/f162v_l15_paragraphos.png`, `../specimens/f164v/l37_paragraphos_T.jpg`, `../specimens/f170v/l28_chor_paragraphos.jpg`.
- **Dicolon** : deux points égaux superposés, dans le blanc ménagé entre deux répliques (forme « pure » au f. 162v, v. 31, f162v #72, `../specimens/f162v/f162v_l32_dicolon_T.png` ; ff. 165v l. 4, 174v ll. 1–5).
- **Dicolon en fin de ligne**, devant un changement en tête de la ligne suivante : f163v l. 34 (v. 113, `../specimens/f163v/f163v_l34_dicolon_fin.png`), f164v vv. 194 et 199 (`../specimens/f164v/l29_l34_dicolon_final.jpg`, non relevés par Velsen 1883), f171v l. 21 (χρή :, fin de la monodie), f172v l. 40 (μέλαθρα :, non relevé par Velsen) ; au f. 162v, v. 6, « φράσον : — » (dicolon suivi d'un trait, f162v #14).
- **Blanc** (« spat. rel. » de Velsen 1871) à la place du dicolon : f165r ll. 26, 35 ; f165v ll. 6, 17, 19 ; f171r v. 746.
- **Point simple** au lieu du dicolon : f169r vv. 562–563 ; f169v v. 621 (ποῖον·) ; f170r l. 16 (δρῶμεν·) ; f171r v. 752 ; f173r v. 878b ; f173v v. 939b ; et en fin de ligne dans le chant d'Agathon (f163v ll. 24, 27, 31, 40).
- **Paragraphos en milieu de ligne** dans la scène d'Écho (§ 2.3).

### 3.2 Fréquence et omissions

T ne marque rien sur des pages entières : f166r (prière et chant : aucune paragraphos, aucun dicolon), f166v (aucune marque), f167r (le seul dicolon du v. 380), f167v (une seule paragraphos, au v. 443, d'encre de type S2, f167v §3), f172r (parabase, un seul locuteur), f174r (aucune paragraphos ; au v. 1001 un trait oblique fin). Ailleurs, il omet souvent. Confrontées aux attributions de l'édition, les marques relevées par les inventaires donnent, en ordre de grandeur (pages dont les tableaux ont pu être dépouillés, soit toutes sauf ff. 167r, 167v, 172r, 174r et 175v) :

| Changement de locuteur (texte de l'édition) | Marque de T |
|---|---|
| **en tête de vers** (≈ 305 cas) | paragraphos vue : ≈ 160 ; présumée sous un sigle de 1516 (Velsen) ou douteuse : ≈ 35 ; barrée ou grattée après coup : ≈ 14 ; **aucune : ≈ 97 (≈ 32 %)** |
| **à l'intérieur du vers** (≈ 125 cas renseignés) | dicolon (souvent sous un sigle de 1516) : ≈ 83 ; point simple : ≈ 10 ; blanc : ≈ 4 ; rien : ≈ 9 ; indéterminé : ≈ 18 |

Ces chiffres reposent sur les attributions modernes et sur la visibilité actuelle des marques ; ils suffisent à montrer qu'**une absence de marque de T ne vaut pas attribution** (dossier § 8.2 : Velsen 1883 note « om. R » à chaque fois).

### 3.3 Survivance de l'usage antique : la paragraphos sous la ligne du changement

Plusieurs inventaires ont relevé des paragraphoi « fausses » ou « décalées » : en tête d'un vers où le locuteur ne change pas (f162v vv. 7, 14 ; f165r vv. 217, 225 ; f169v vv. 622, 623 ; f173v vv. 926, 935, 940 ; f176v vv. 1184, 1192, 1194, 1195…). L'inventaire du f. 173v a proposé d'y voir la convention antique, où la paragraphos est tracée **sous la ligne qui contient le changement**, le dicolon marquant le point exact (f173v § 3). Je l'ai éprouvée sur toute la pièce (`.travail/chap5/convention.py` ; planche `../planches/5_planche_paragraphos.jpg`) :

- **cas discriminants** : un changement à l'intérieur du v. *n*−1, aucun en tête du v. *n* ; on en compte une soixantaine sur les pages renseignées ;
- **résultat** : T met une paragraphos en tête du v. *n* dans **25 cas sur 61** (≈ 40 %), et rien dans les autres.

| Paragraphos devant le v. | Folio, l. | Changement intérieur au vers précédent | Sort de la paragraphos |
|---|---|---|---|
| 7 | 162v, 8 | 6 (Euripide → Parent) | laissée |
| 14 | 162v, 15 | 13 (Parent → Euripide) | laissée (vue : `../specimens/f162v/f162v_l15_paragraphos.png`) |
| 216 | 165r, 8 | 215 (Parent → Euripide) | laissée (changement aussi dans le v. 216) |
| 217 | 165r, 9 | 216 (Euripide → Parent) | laissée |
| 225 | 165r, 17 | 224 (Euripide → Parent) | laissée |
| 246 | 165r, 38 | 245 (Euripide → Parent) | barrée par 1516 (`../specimens/f165r/l38_paragraphos_barree.jpg`) |
| 620 | 169v, 28 | 619 (Clisthène → Parent) | annulée en ⊥ d'**encre brune** (T ou S2, f169v #74) |
| 622 | 169v, 30 | 621 (Clisthène → Parent) | laissée (vue) |
| 623 | 169v, 31 | 622 (Parent → Clisthène) | laissée (vue) |
| 742 | 171r, 22 | 741 (Parent → Mica ; **sans dicolon** dans le v. 741) | laissée (1516 pose ses Γϋ sur les dicola intérieurs du v. 742) |
| 744 | 171r, 24 | 743 (Parent → Mica) | laissée |
| 750 | 171r, 30 | 749 (Mica → Parent) | laissée |
| 875 | 172v, 42 | 874 (Parent → Critylla) | 1516 y greffe Γϋ |
| 898 | 173r, 22 | 897 (Parent → Critylla) | sous la barre du Γϋ de 1516 (vue par Velsen 1871 ; f173r n° 80) |
| 926 | 173v, 7 | 925 (Parent → Euripide) | barrée (main indéterminée) |
| 935 | 173v, 17 | 934 (prytane → Critylla) | barrée (1516 selon Velsen 1871) |
| 940 | 173v, 23 | 939 (prytane → Parent) | 1516 y pose μν, que la Juntine n'imprime pas |
| 1006 | 174v, 5 | 1005 (archer → Parent) | laissée |
| 1119 | 175v, 36 | 1118 (Euripide → archer) | laissée |
| 1184 | 176v, 16 | 1183 (Euripide → archer) | barrée par 1516 (deux encres, f176v #9) |
| 1192 | 176v, 25 | 1191 (Euripide → archer) | laissée (vue) |
| 1194 | 176v, 27 | 1193 (archer → Euripide) | barrée par 1516 (vue) |
| 1195 | 176v, 28 | 1194 (Euripide → archer) | barrée par 1516 (vue) |
| 1219 | 177r, 11 | 1218 (archer → coryphée) | sous le σκ de 1516 (Velsen) |
| 1221 | 177r, 13 | 1220 (archer → coryphée) | barrée par 1516 |

Deux détails confirment l'interprétation :
- au v. 742, T ne met **aucun dicolon** dans le v. 741, mais une paragraphos en tête du v. 742 : c'est la paragraphos seule qui signale le changement intérieur de la ligne précédente ;
- au v. 875, T a coupé le v. 874 en deux lignes à la réplique (ll. 40–41, avec un tiret devant la seconde) et garde *en plus* la paragraphos du v. 875 : il la tient d'un modèle où le v. 874 tenait sur une ligne et où la paragraphos, sous cette ligne, signalait son changement intérieur.

**Paragraphoi de division du discours.** D'autres paragraphoi, sans aucun changement de locuteur, tombent à une articulation du sens, comme la paragraphos antique dans un texte continu : f168r vv. 498 et 502, dans le discours de Mnésiloque (après la pause intérieure du v. 497, οὐπώποτ᾽ εἶπεν. εἰ δὲ Φαίδραν…, puis au début d'une nouvelle anecdote, ἑτέραν δ᾽ ἐγᾦδ᾽…), où l'inventaire les note « tirets » et recommande de les transcrire sans les interpréter ; f169v v. 601 (le coryphée se tourne vers Clisthène) et v. 635 (après le δεῦρ᾽ ἐλθὲ … ὦ Κλείσθενες du v. 634) ; f176v vv. 1199 et 1204 (changements d'interlocuteur adressé dans la scène de l'archer).

**Résidu inexpliqué** : f163r v. 72 (paragraphos nette, sans changement dans le texte reçu ; le modèle répartissait-il autrement les vv. 70–72 ?), f165r v. 234 (barrée par 1516), f176v vv. 1193 et 1200 (grattées ; l'Augustanus a encore celle du v. 1200, Velsen 1883) et v. 1198 (?). Les vv. 234, 1193 et 1200 contiennent eux-mêmes un changement intérieur : la paragraphos y est rattachée à la ligne du changement plutôt que placée sous elle.

**Interprétation.** Le système de T est **mixte**. La paragraphos sert d'abord, comme dans les éditions modernes, à signaler une réplique qui commence en tête de ligne ; mais dans deux cas sur cinq, elle suit encore la règle antique, et quelques fois elle marque une simple division du discours. Le plus vraisemblable est que T (ou un ancêtre proche) a reporté en tête de ligne, à mi-hauteur, une paragraphos qui, dans un modèle plus ancien, était tracée **entre** deux lignes : selon qu'il la rattachait à la ligne d'au-dessus ou à celle d'au-dessous, elle tombe en tête de la réplique nouvelle ou en tête du vers qui suit le changement. Le système n'était déjà plus compris au Xe siècle : une paragraphos de type antique (v. 620), et une autre qui marque pourtant un vrai changement (v. 608, « ipsa I m. delevit », Velsen 1871, 11), sont annulées à l'encre brune ; la main de 1516, qui ne connaît que la convention de la Juntine, barre ou couvre les autres.

**Conséquences.** Une paragraphos en tête du v. *n* signifie seulement : « changement de locuteur en tête du v. *n*, ou à l'intérieur du v. *n*−1, ou articulation du discours ». Elle ne justifie pas à elle seule une attribution nouvelle (c'était déjà la prudence de l'inventaire du f. 162v pour les vv. 7 et 14). Dans l'apparat des attributions, il faut citer la marque telle qu'elle est (« — R ante v. *n* »), à la manière de Coulon 1928 (sigle « par. »), et non la traduire en nom de personnage.

### 3.4 Le dicolon : changement, pause, ponctuation

Le dicolon marque d'abord le changement à l'intérieur du vers. Mais T l'emploie aussi :
- **en fin de ligne** devant une réplique qui commence à la ligne suivante (§ 3.1) ;
- **comme pause forte, sans changement de locuteur** : f165r ll. 21 (με : χώρει, v. 229 ; vu, `.travail/chap5/vues/f165r_l21.png`), 24 (κακοδαίμων : ψιλὸς), 36 (σοι : τὰ, `../specimens/f165r/l36_dicolon_ta.jpg`) ; f168r l. 12 (πόλλ᾽ ⁚) ; f169v v. 605 (ἤρου :) ; f170r ll. 22, 30, 34 ; f171v l. 9 (πλάται : πόθεν) ; f173v l. 14 (αὐτόν : ἀλλὰ) ; f176r l. 41 (κομίσωμαι :, où Velsen 1883 imprime « · ») ; f176v l. 18 (avant ἔτι) ;
- **comme ponctuation lyrique** : f174r ll. 12, 14, 24, 29 (μέλπουσα :, ἑκάεργε : ὄπαζε…), f173v l. 41 ;
- en clôture : « :– » à la fin de la l. 29 du f. 174r, « :— » à la fin de l'hypothesis de l'*Assemblée*, « :– » après le titre de celle-ci.

Il faut donc transcrire le dicolon comme un signe, sans préjuger de sa valeur. Inversement, beaucoup de « dicola » apparents n'en sont pas (§ 5.3).

### 3.5 La réception du système : S2 et la main de 1516

- **S2** complète le système là où T n'a rien mis, ou à côté de la paragraphos (sans la recouvrir), ou au-dessus du dicolon, dans l'interligne (f169v ll. 11, 23 ; f170r l. 14) ; il n'annule jamais une marque de T, sauf peut-être aux vv. 608 et 620 (encre brune indiscernable de celle de T).
- **La main de 1516** transforme les marques muettes de T en sigles imprimables (§ 4.2) : elle écrit le sigle **sur la paragraphos**, qui devient la barre du Є, le corps du μ, la barre du Γ ou la traverse du Η (f165r, f165v, f175r, f176v) ; **sur le dicolon**, dont les deux points deviennent la haste d'un Γ (Γϋ, f171r ll. 22–28 ; f173v l. 16 ; f176v l. 26) ou les extrémités d'un ε (f163r l. 34) ; dans le blanc ménagé par T. Là où T n'a rien marqué au milieu du vers, elle met le sigle **en marge avec un signe d'insertion** « ^ » ou « √ » dans la ligne (f165r ll. 8, 14, 16 ; f169r v. 552, renvoi en croix vers la marge supérieure ; f176v ll. 11, 19). Elle **barre d'une haste verticale** les paragraphoi qui ne conviennent pas aux attributions de la Juntine (« + », « I m. del. 2 m. » de Velsen 1871) et **gratte** parfois paragraphoi et dicola (f162v v. 32 ; f175v v. 1114 ; f176v vv. 1193, 1200).

Paragraphoi annulées après coup, et ce qu'en dit le texte de l'édition :

| Vers | Folio, l. | Annulation | Changement dans le texte de l'édition ? |
|---|---|---|---|
| 75 | 163r, 39 | biffure ondulée, 1516 (`../specimens/f163r/f163r_l39_biffure_paragraphos.jpg`) | **oui** (Parent → Euripide) |
| 232 | 165r, 24 | haste, 1516 (`../specimens/f165r/l24_paragraphos_barree.jpg`) | **oui** (Euripide → Parent) |
| 234 | 165r, 26 | haste, 1516 | non (changement intérieur au v. 234) |
| 246 | 165r, 38 | haste, 1516 | non, mais changement intérieur au v. 245 (§ 3.3) |
| 264, 273, 274 | 165v, 13, 22, 23 | haste, 1516 (deux encres, f165v #39, #53) | **oui** dans les trois cas |
| parépigraphe | 165v, 26 | haste, 1516 | changement entre 276 et 277 |
| 608 | 169v, 16 | trait vertical brun (T selon Velsen 1871) | **oui** (coryphée → Clisthène) |
| 620 | 169v, 28 | ⊥ brun (T ou S2) | non, mais changement intérieur au v. 619 |
| 926, 935 | 173v, 7, 17 | haste (935 : 1516 selon Velsen 1871) | non, mais changement intérieur aux vv. 925, 934 |
| 1076a, 1078a | 175r, 35, 39 | trait gris | non (erreur de T dans la scène d'Écho) |
| 1092b, 1093, 1095 | 175v, 11–13 | haste orangée | **oui** dans les trois cas |
| 1114 | 175v, 31 | grattée | **oui** (Euripide → archer) |
| 1184, 1194, 1195 | 176v, 16, 27, 28 | haste orangée | non, mais changement intérieur aux vv. 1183, 1193, 1194 |
| 1193, 1200 | 176v, 26, 33 | grattées (1200 après la copie de G) | non (changement intérieur au v. lui-même) |
| 1204 | 176v, 37 | haste | non (articulation du discours) |
| 1221 | 177r, 13 | haste roussâtre, 1516 | non, mais changement intérieur au v. 1220 |

Sur ces vingt-cinq annulations, dix suppriment donc un **vrai** changement de locuteur, et huit une paragraphos de type antique : la main de 1516 corrige T d'après la Juntine, non d'après le sens. Ses barres ne doivent jamais être lues comme le signal « + » du copiste (piège signalé par tous les inventaires concernés).

---

## 4. Les notae personarum

### 4.1 Trois couches

1. **T n'écrit aucun nom de personnage.** Aucun inventaire n'a trouvé de sigle de sa main. Le seul cas allégué, « μνησι^λο » devant le v. 130, que van Leeuwen 1904 donne au copiste (dossier § 8.2), est un sigle de S2 : petites majuscules ΜΝΗΣΙ et λ suscrit enfermant un ο, de l'encre des scholies (1,39/2,33, contre 1,33–1,36/2,13–2,27 pour T ; f164r #71) ; vérifié sur l'image (`.travail/chap5/vues/f164r_l7-10.png`).
2. **S2** (Xe s.) écrit des sigles **abrégés par suspension**, avec une lettre suscrite (μνη^σ, κη^δ, ευρι^π, αγα^θ, κλεισ^θ, γυ^ν, σκυ^θ, χ^ρ…), en petites majuscules ou en semi-onciale, de l'encre brune des scholies, à gauche de la paragraphos de T sans la recouvrir, ou dans l'interligne au-dessus du dicolon ; parfois des **notes développées** (καλλιλεξία γυ^ν, v. 383 ; γυ^ν μία, v. 605 ; ΠΡΥΤΑΝΙϹ, v. 929 ; εὐρι^π ὡς περσεύς, v. 1098 ; ὁ μνησίλ(ο)χ(ος) ὡς ἀνδρομέδα, v. 1065 ; κη^δ ὡς ἀνδρομε^δ, v. 1107 ; ευρι^π ὡς γραῦς, vv. 1177, 1181) et des **indications de jeu** (πρὸ(ς) τ(ὰς) γυναῖκας, v. 726 ; ἠρέμα ὁ κηδεστ(ής), [τὸ] πρὸς τ(ὸν) εὐρι(πίδην), v. 1063b).
3. **La main de 1516** écrit des sigles « **imprimables** » (Εὐ, Μν, Ἀγ, Γυ, Κλ, Σκ, Ηχ, Χο…), d'encre orangée, souvent suivis d'un point d'abréviation, pour l'imprimeur de la Juntine, qui les reproduit tels quels (Velsen 1871, 7–26) ; elle repasse ou gratte parfois les sigles de S2 (f162v vv. 5, 19, 39 repassés ; v. 34 gratté et récrit ; f163r vv. 45b–c repassés ; f165r v. 210 repassé ; f168r v. 466 gratté et récrit) ; d'autres sigles, dont certains de sa main que la Juntine imprime, ont été grattés plus tard (f163r vv. 57b, 58, 63, 77 ; f175v v. 1116).

**Attention à l'encre.** L'orangé n'est pas, à lui seul, la signature de 1516. Plusieurs notes de **forme S2**, que **G reproduit déjà** (donc antérieures à 1516), sont d'encre orangée : χ^ρ et ἡμι^χ γυν^αικ^ῶν (f170r vv. 655, 659), χ^ορ (f171v v. 785), τοξ^ότης (f174r v. 1001), ηχω, εὐρι^π ὡς περσεύς, κη^δ ὡς ἀνδρομε^δ, σκυ^θ (f175v ll. 2, 17, 24, 25), κη^δ (f176v v. 1207). S2 a donc écrit avec au moins deux encres, ou un correcteur ancien à l'encre rougeâtre est intervenu (cf. Clark 1871, 159–160, cité au dossier § 5.1) ; à moins d'un repassage en 1516. Pour attribuer un sigle, l'ordre des critères est : **forme** (suspension et semi-onciale pour S2 ; sigle imprimable, Η capital, grand χ descendant, σκ à queue pour 1516) ; **témoignage de G** ; **position** ; **encre** en dernier (f175v #50). La question relève du chapitre 1 (`1_mains_encres.md`).

### 4.2 Répertoire des sigles par personnage

| Personnage | S2 (brun, suspension) | Main de 1516 (orangé, « imprimable ») |
|---|---|---|
| Euripide | ευ^ρ (vv. 5, 202, 249), ευ· (32), ευρι^π / ΕΥΡΙ^π (877, 885, 889, 896, 902, 918, 924, 1015, 1160, 1208…), εὐρι(πίδης) ἠχώ (1056), εὐρι^π ὡς περσεύς (1098 ; au v. 871, ὡς περσεύς est ajouté par 1516 après l'εὐρι^π de S2), ευρι^π ὡς γραῦς (1177, 1181) | Εὐ, εὐ, Єὐ, Єυ·, ευρ (84) |
| le Parent | μνη^σ, μνη^σι, μνησι^λο, ΜΝΗΣΙ^λο, μ· (≈ 27, § 4.4) ; κη^δ (5) | μν, μν^η, Μν, μ^ν, μν·, μ réduit à un crochet (≈ 90) ; κηδ, κη^δ, Κη^δ (9) |
| Agathon | αγα^θ / ΑΓΑ^θ, θ en lentille barrée (101, 107, 114, 146, 203) | ἀγ, Αγ, αγ |
| le serviteur | θερά^π (39) | θερ (46), θε· (66) |
| le chœur, le coryphée | χ^ο (Χ et ο suscrit), monogramme χ + ρ « en astérisque » ou « en chrisme » (χ^ρ, χορ), χ^ορ | χ^ο, grand χο, monogramme χορ (vv. 582, 586, 589, 1170, 1223, 1226), χο au milieu des vers (1218–1220) |
| demi-chœur | ἡμι^χ γυν^αικ^ῶν (659, orangé, G) | — |
| le héraut | κη^ρ (372 ; à lire κη^ρ, non κ^ρη, contre Velsen 1883) ; κη^ρυξ abrégé au v. 295, gratté (G) | κήρυξ en toutes lettres sur grattage (295), κηρ (331) |
| les femmes | γυ^ν (626, 649, 652, 689 ?, 706, 852, 879, 882, 892), γυ^ν μία (605), γυ^νη τίς (533), καλλιλεξία γυ^ν (383), ἄλλη γυ(νή) (760) | Γυνὴ τίς (380), ἑτ(έρα) γυνή (443), Γυνη (544, 551, 554), Γυ, Γϋ (avec tréma), Γυ^η |
| Clisthène | κλεισ^θ, κλεσ^θ, κλει(σ) (574, 595, 603, 606, 610, 615, 645) | κλ, κλ· ; complète κλει(σ) de S2 en Κλεισθένης (574) |
| le prytane | ΠΡΥΤΑΝΙϹ (929), ΠΡΥ (939, forme S2, encre de 1516) | πρυ (943) |
| l'archer scythe | τοξ^ότης (1001), σκυ^θ (1083, 1084, 1108, 1133, 1135, 1176, 1210…) | τοξ (1002, 1003, 1006), σκ |
| Écho | ηχω (1069b ; f175v l. 2) | Ηχ, ἠχ |

### 4.3 Répartition par page

Le relevé ligne par ligne (marque de T, sigle de S2, sigle de 1516, témoignage de Velsen) est dans la section « sigles » de chaque inventaire (`../folios/fXXX.md`, § 3 ou § c) ; les marques de T en ont été extraites vers par vers dans `.travail/chap5/marques_T.tsv`. Les nombres ci-dessous sont des ordres de grandeur.

| Folio | Marques de T | Sigles de S2 | Sigles de 1516 | Remarques |
|---|---|---|---|---|
| 162v | paragraphoi, dicola | 5 | ≈ 24 | 1516 repasse, gratte et récrit |
| 163r | paragraphoi, dicola | 1–2 (repassés) | ≈ 10 | sigles grattés aux vv. 57b, 58, 63, 77, dont des sigles de 1516 que la Juntine imprime |
| 163v | paragraphoi ; presque rien dans le chant | ≈ 6 (ΑΓΑ^θ, χ^ο, χορ) | ≈ 17 | Euripide et le Parent intervertis par 1516 jusqu'au v. 92 |
| 164r | 3 paragraphoi | 2 | 4 | — |
| 164v | paragraphoi, dicola, dicola de fin de ligne | 3 | ≈ 24 | — |
| 165r | paragraphoi, dicola, blancs | 1 (+1 repassé) | ≈ 35 | insertions en marge avec « ^ » ou « √ » |
| 165v | paragraphoi, dicola, blancs | 0 | ≈ 25 | — |
| 166r | rien | 1 (χ^ρ) | 2 (κήρυξ, κηρ) | — |
| 166v | rien | 2 (χ^ο, κη^ρ) | 0 | — |
| 167r | 1 dicolon | 1 | 1 | — |
| 167v | 1 paragraphos (encre de type S2) | 2 | 1 | — |
| 168r | tirets de division | 0 (note grattée au v. 466) | 1 (κηδ ευ) | — |
| 168v | paragraphoi, Ο agrandis | 3 | 2 | — |
| 169r | paragraphoi, dicola | 2 (+ 592 ?) | ≈ 18 | — |
| 169v | 25 paragraphoi, 13 dicola | 13 | 2 | 1516 n'ajoute plus rien des vv. 618 à 649 (Velsen 1871) |
| 170r | paragraphoi, dicola | ≈ 6 (+ 2 orangés, G) | 0 | aucun sigle de 1516 des vv. 608 à 710 (Velsen 1871) |
| 170v | 7 paragraphoi, 1 dicolon | 8–9 | 1 | « nearly all the dram. pers. are by B » (Allen 1896, 316) |
| 171r | paragraphoi, dicola | 3 | 11 (Γυ seulement, vv. 739–751) | — |
| 171v | 1 paragraphos, 2 dicola | 1 (+ χ^ορ orangé, G) | 0 | — |
| 172r | rien (un seul locuteur) | 0 | 0 | — |
| 172v | paragraphoi, dicolon final | 4 | ≈ 10 | — |
| 173r | paragraphoi, dicola | 12 (ll. 1–20, 26, 42) | 16 | 1516 n'écrit jamais là où S2 a écrit |
| 173v | paragraphoi, dicola | 3–5 | ≈ 8 | — |
| 174r | rien | 1 (τοξ, orangé) | 0 | — |
| 174v | paragraphoi, dicola (ll. 1–5) | 3 | 5 | — |
| 175r | paragraphoi (Écho) | 4 notes | ≈ 25 | — |
| 175v | paragraphoi (Écho), dicola | ≈ 8 notes | ≈ 25 | — |
| 176r | paragraphoi | 6 | 3 | — |
| 176v | paragraphoi, dicola | 6 | ≈ 25 | 1516 n'ajoute rien là où S2 a écrit |
| 177r | paragraphoi, dicola | 0–1 | ≈ 10 | — |

Les deux couches sont **complémentaires** : là où S2 a pourvu le texte de sigles lisibles (ff. 169v–171v, haut du f. 173r, ff. 176r–176v), la main de 1516 s'abstient ou presque ; là où S2 manque, elle transforme les marques muettes de T. Velsen l'avait observé pour les listes de la « 2 m. », qui sautent les vv. 608–710 et 751–858 (dossier § 8.2 ; f169v, f170r, f171v). Ses sigles reproduisent ceux de la Juntine, y compris ses erreurs : interversion d'Euripide et du Parent jusqu'au v. 93 (« Euripidis et Mnesilochi personae perversae sunt in R sicut in Junt. », Velsen 1871, 31 ; f163r, f163v), ἀγ aux vv. 173, 208, 209, 253 ; εὐ aux vv. 206, 252 (intérieur), 254 ; μν^η au v. 265 ; Γυ au v. 710 et devant des répliques du Parent aux vv. 742–748 ; γϋ au v. 928 ; σκ aux vv. 1125, 1179, 1188 ; μν au v. 1128 ; γυ après πυγή (v. 1187). Velsen 1871, 30 juge ce travail « flüchtig ». **Les sigles de 1516 n'ont aucune autorité de tradition** : ce sont les attributions de l'*editio princeps*, à citer comme telles (« Junt. ») et non comme leçons de R.

### 4.4 Le nom du « Parent » d'Euripide

**La question.** Les éditeurs nomment le personnage tantôt Μνησίλοχος, tantôt Κηδεστής. Coulon écrit : « Κηδ. R passim, Σ compluribus locis : Μνη. R compluribus locis, Σ passim » ; Wilson : « R et sch. saepe eum ita nominant, saepe autem Mnesilochum » ; Sommerstein parle d'abréviations de Μνησίλοχος qui « appear sporadically » dans R ; Velsen est le premier éditeur à écrire Κηδεστής, à l'instigation de Hiller (van Leeuwen 1904, 1–2 n. 2) (citations d'après le dossier § 8.2). Il fallait établir sur l'image quelle main écrit κηδ. et quelle main écrit μν(η).

**Relevé complet** (planche `../planches/5_planche_sigles_parent.jpg`) :

*a) S2 — le nom propre (≈ 27 occurrences)*

| Vers | Folio, l. | Forme | Remarques |
|---|---|---|---|
| 19 | 162v, 20 | μνη^σι | repassé μνη par 1516 |
| 33 | 162v, marge | μ· | en tête du vers suppléé |
| 45b | 163r, 4 | μνησι^λο | λό brun (S2), μνησι repassé en orangé (f163r #12) |
| 130 | 164r, 9 | ΜΝΗΣΙ^λο | vu ; non de T (§ 4.1) |
| 200 | 164v, 35 | μνη^σ | — |
| 210 | 165r, 2 | μνη^σ | R² selon Velsen 1883 ; encre actuelle de 1516 (repassé) |
| 615, 630 | 169v, 23, 38 | μνη^σ | au-dessus du dicolon ; en marge |
| 637, 650 | 170r, 2, 14 | μνη^σ | au v. 650, dans l'interligne au-dessus du dicolon |
| 692, 704, 709, 714 | 170v, 15, 27, 32, 37 | μνη^σ (σ en c suscrit) | v. 692 vu (`.travail/chap5/vues/f170v_l15.png`) ; au v. 709, Κ et zigzag orangés sur μνη |
| 730 | 171r, 10 | μνη^σι | forme de S2, encre actuelle orangée |
| 765 | 171v, 2 | μνη^σ | « corrector » chez van Leeuwen |
| 846, 855 | 172v, 12, 21 | μνη^σ | — |
| 878, 886, 895 | 173r, 2, 10, 19 | μνη^σ | — |
| 925a, 936 | 173v, 6, 19 | μνη^σ | v. 936 : forme de S2, encre de 1516 |
| 1002, 1022 | 174v, 1, 21 | μνη (petit c suscrit), μνη^ϲ | — |
| 1065 | 175r, 21 | ὁ μνησίλ(ο)χ(ος) ὡς ἀνδρομέδα ÷ | note ; 1516 écrit μν sur sa fin |
| 1134 | 176r, 8 | μνη^σ | — |

*b) S2 — la parenté (5 sigles et une note)*

| Vers | Folio, l. | Forme | Remarques |
|---|---|---|---|
| 466 | 168r, 1 | note **grattée** ; G : κή^δ εὐ^ριπ (Velsen 1871, 10) | récrite par 1516 κηδ : ευ· (§ c) |
| 540 | 168v, 32 | **κη^δ** : Κ en deux pièces, Η barré d'une longue oblique, δ suscrit souligné ; brun (1,26/1,91) | vu (`../specimens/f168v/f168v_l32_sigle_ked_paragraphos.jpg`) ; seul κηδ du « corrector » chez van Leeuwen |
| 603 | 169v, 11 | **κη^δ** suscrit au-dessus du dicolon, Κ en \|c, Η oncial, petit Δ ; brun | vu (`.travail/chap5/vues/f169v_l11-12.png`) ; G : « κηδ. minio superscriptum » (Velsen 1883) : antérieur à 1516, contre Velsen 1871, 21 et van Leeuwen |
| 1063b | 175r, 19 | ἠρέμα ὁ κηδεστ(ής) πρὸς τ(ὸν) εὐρι(πίδην) | indication de jeu servant de note de personnage |
| 1107 | 175v, 24 | κ^η^δ ὡς ἀνδρομε^δ, encre orangée | G : κη^δ ανδρο^μδ : antérieur à 1516 (contre van Leeuwen, « manus recens ») |
| 1207 | 176v, 40 | κη^δ, capitales de grand module, encre orangée empâtée, restes bruns | G : κη^δ ; note de S2 repassée en 1516 ? (f176v #72) |
| (592) | 169r, 43 | κη^Δ | R² selon Velsen 1883 ; encre actuelle de 1516 : à trancher |

*c) Main de 1516*

- **μν** (μν, μν^η, μ^ν, Μν, μν·, μ) : environ 90 fois, de la première page (vv. 6–34) à la scène d'Écho (vv. 1058–1081 ; v. 1082 au f. 175v) et au v. 1128.
- **κηδ** seulement aux vv. **466** (κηδ : ευ·, κηδ(εστὴς) Εὐ(ριπίδου), sur le grattage de la note de S2 ; vu, `.travail/chap5/vues/f168r_l1.png`), **549** (κηδ), **552** (κη^δ dans la marge supérieure, avec renvoi en croix), **555, 558, 560** (κη^δ), **592** (?), **604** (κη + Λ, dans le vers ; vu) et **1209** (Κη^δ, dans le vers). Le κηδ que van Leeuwen donne à la « manus recens » aux vv. 567 s. n'a pas été retrouvé par l'inventaire du f. 169r.

*d) Scholies et gloses de S2* : notice initiale « προλογίζ(ει) μνησίλοχ(ος) κηδεστ(ὴς) εὐριπίδου » (f162v, marge supérieure) ; glose ὁ μνησίλοχ(ος) sur οὑτοσί (f165v l. 15, v. 266) ; scholie au v. 603 « μνησίλοχ(ος) τοῦτο διὰ τὸ μέλλειν ἔρευναν γίνεσθαι » (f169v #34) ; scholie au v. 633 « … τί εἴπη ὁ κηδεστ(ὴς) … » (f169v #44).

**Ce qu'on en tire.**
1. **Aucune des deux désignations n'est de T.** Le copiste du texte n'a transmis aucun nom de personnage ; R ne contient pas de liste des personnages des *Thesmophories*. Les noms sont l'œuvre du scholiaste du Xe siècle, puis de la main de 1516.
2. **S2 connaît les deux** et les emploie indifféremment, comme sa notice initiale qui les juxtapose (« Μνησίλοχος, κηδεστὴς Εὐριπίδου ») : à la même page, il suscrit κη^δ au v. 603 et μνη^σ aux vv. 615 et 630, il écrit μνησίλοχος dans la scholie au v. 603 et ὁ κηδεστής dans la scholie au v. 633 (f169v) ; pour le même rôle, il note ὁ μνησίλοχος ὡς ἀνδρομέδα au v. 1065 et κηδ ὡς ἀνδρομέδα au v. 1107. Mais le **nom propre domine nettement** : environ 27 sigles contre 5.
3. Les κηδ de **1516** ne sont pas une donnée indépendante : ils se concentrent dans le passage où S2 a lui-même écrit κηδ (vv. 466–604 : 466, 540, 603) et au v. 1209, deux vers après le κη^δ de S2 au v. 1207 ; partout ailleurs, la main de 1516 écrit μν. Elle a donc suivi localement l'usage de S2, et la Juntine imprime en conséquence Κηδ. à ces endroits (Velsen 1871, 10 et 33 : « 466 κηδ. εὐ. 2 m. in rasura R Κηδ. Junt. »).
4. Le relevé **contredit** la formule de Coulon pour R : toutes mains confondues, la désignation dominante du manuscrit est Μν(ησίλοχος) (≈ 117 sigles contre ≈ 14) ; dans les scholies, les deux noms apparaissent à égalité. Il corrige aussi van Leeuwen, qui ne donne au « corrector » que le κηδ du v. 540 : ceux des vv. 466, 603, 1107 et 1207 sont antérieurs à 1516, puisque G les connaît.
5. Pour l'édition, R n'apporte donc **aucun argument de tradition** en faveur de Κηδεστής contre Μνησίλοχος, ni l'inverse : les deux désignations appartiennent à l'exégèse byzantine, la seconde est la plus fréquente dans le manuscrit, et le texte lui-même ne désigne le personnage que par sa parenté (Εὐριπίδην … ἄνδρα κηδεστήν τινα, v. 584 ; κηδεστὴς ἐμός, v. 1165 ; le mot s'applique aussi, en sens inverse, à Euripide aux vv. 74 et 210) : le nom de Μνησίλοχος vient de l'exégèse. Le choix du nom relève de la convention éditoriale ; l'apparat des personnages peut s'en tenir à « μνη^σ R² passim, κη^δ R² 466, 540, 603, 1107, 1207 ».

### 4.5 Conséquences pour la transcription et l'apparat

- Chaque sigle est un `<nota>` avec sa main (`R2`, `Rrec`) ; la lettre suscrite se transcrit à sa place, par exemple `<nota main="R2">μνη<add place="dessus" main="R2">σ</add></nota>`, ou, si le guide préfère, avec `<abbr>` (le développement entre parenthèses ne doit pas masquer la forme suscrite, qui est un critère d'attribution).
- Un sigle de S2 repassé par 1516 doit garder les deux mains (main d'origine `R2` et une note, ou un attribut à définir, par ex. `retouche="Rrec"`) ; un sigle gratté sous un sigle de 1516 s'encode `<del type="grattage">` avec `<gap/>` et, quand G le connaît, une `<note>` (« G : κή^δ εὐ^ριπ »).
- La marque de T (paragraphos, dicolon) et le sigle posé dessus sont **deux objets** : la paragraphos sous un μν ou un Γ de 1516 se transcrit `<parag/>` (avec `<unclear>` si elle est seulement présumée d'après Velsen), le dicolon sous un Γϋ se transcrit « : » à sa place, puis le sigle.
- Dans l'apparat critique, seules les marques de T sont des données de R au sens strict ; les sigles de S2 sont des témoignages de l'exégèse ancienne (R²) ; ceux de 1516 sont la Juntine (« Junt. »).

---

## 5. La ponctuation

Planche : `../planches/5_planche_accents_ponctuation.jpg`.

### 5.1 Les signes de T

| Signe | Forme et place | Emplois relevés | Exemples |
|---|---|---|---|
| point | surtout **à mi-hauteur** ; parfois haut ; le point final est souvent détaché loin à droite (f172v ll. 5, 18, 20, 31, 43) | fin de phrase, de vers ou de côlon ; après un vocatif ; **à la place du point d'interrogation** ; pauses intérieures du pnigos | ὦ ζεῦ· … φανήσεται· (f162v v. 1, vu) ; τούτοις·, μᾶλλον·, βωμολόχους· (f172r ll. 25–27) ; points de pause du pnigos (f172r #23) |
| point-virgule « ; » | point haut et virgule descendante | **interrogation** le plus souvent ; parfois simple pause | σίγα· τί λέγει; (f163r l. 5) ; τί σ πάτρα; (f164r l. 15, vu) ; ἐπινοεῖ; (f166v l. 2) ; στρέφει; (f169v l. 18) ; ἡμᾶσ; (f172r l. 3) ; με; (f176v l. 23, vu) ; pause : συγκλείσας ; (f162v v. 40, `../specimens/f162v/f162v_l40_semicolon_epi.png`) ; après γυναικὸς et λεγούσης, sans question (f167v l. 13) |
| virgule basse | sous la ligne de base | valeur incertaine : hypodiastole (séparation) ou pause | καθῆ σθαι, γεγένημαι, πικρὰν, ἐμοὶ (f172v ll. 6, 12, 19, 25) ; ἀνίστασ , ὀρθός (f170r l. 8) ; σὲ (f174r l. 31) ; ἐμέ, (f176v l. 26, vu) |
| dicolon | deux points superposés | changement de locuteur ; pause forte ; question (§ 3.4) | κέκραγας : (f165r l. 14), changé en « ; » par 1516 |
| tiret, point allongé | trait horizontal à mi-hauteur en fin de ligne | fin de période | f173r l. 25 (v. 901) ; f174r ll. 3, 39 |
| « :– », « :— » | dicolon et tiret | clôture | f174r l. 29 ; titre et fin de l'hypothesis de l'*Assemblée* (f177r) |
| trois points | trois petits points alignés | renvoi ou rattachement ? | devant ταύτην νικᾶν (f166r l. 16, f166r #12, `../specimens/f166r/f166r_l16_trois_points.jpg`) |

La ponctuation est **fréquente mais non systématique** : beaucoup de fins de vers n'en ont pas (f168v ll. 1, 13), et le point peut couper ce que les éditions lient (« προσμάθοι· μὴ » pour προσμάθοιμι, f162v v. 24, f162v #46). Le **point d'interrogation moderne** n'est pas en usage de façon régulière : T emploie indifféremment le point, le point-virgule ou le dicolon après une question.

**Interventions de la main de 1516.** Elle ajoute une virgule orangée sous un point ou un dicolon de T pour en faire un « ; » à l'usage de l'imprimeur : v. 193 (f164v l. 28, `../specimens/f164v/l28_point_interrogation_1516.jpg`), v. 222 (κέκραγας : → κέκραγας;, Velsen 1871, `../specimens/f165r/l14_kekragas_point_interrogation.jpg`), v. 252 (f165v l. 1, non signalé par Velsen), vv. 32 et 33 (πώποτε· → πώποτε;, Velsen 1871, 25 ; au v. 33 suppléé, le « ; » est orangé, f162v #31) ; elle gratte le dicolon du v. 32 (f162v #51). Ces signes sont la ponctuation de la Juntine, non de R.

**La ponctuation des scholies** (quatre points, hypodiastole, point haut avant les citations : Rutherford 1896, I, xxix, dossier § 8.3) est traitée au chapitre 3.

### 5.2 Ce qui ressemble à de la ponctuation et n'en est pas

Les inventaires signalent sur presque chaque page de faux points et de faux dicola. Les plus fréquents :
- **ι adscrit** tracé en deux touches, ou court, au-dessus d'un accent de la ligne suivante (f163v l. 31 γᾶι ; f173r ll. 18, 41 κλοπῆι, τῆι ; f163r ll. 29–30, à trancher) ;
- **esprits et accents de la ligne suivante**, qui montent dans l'interligne : f164v l. 25 (point de T et esprit de εὐ- : faux dicolon) ; f168v l. 14 ; f169v l. 19 (l'apostrophe de τοῦτ᾽ de la l. 20) ; f171r l. 29 ; f172v l. 17 ; f177r l. 16 (« : » après δίωκε) ;
- **esprits initiaux rejetés à gauche**, en point, dans la bande des sigles (f166v l. 15, vu, `../specimens/f166v/f166v_l15_esprit_rejete.jpg` ; f167r ll. 20, 28, 35, 42 ; f167v ll. 5–7, 24, `../specimens/f167v/f167v_l05-07_esprits_initiaux.jpg` ; f168r ll. 20, 22, 23, 32, 37, 42 ; f168v ll. 38, 39, 41 ; f170v ll. 4, 5, 9, 23, 39 ; f165r l. 22) ;
- **goutte d'attaque du τ**, isolée devant la lettre (f163r l. 13 ; f167r ll. 10, 15 ; f167v ll. 8, 10, 11) ;
- **apostrophe + point** (θ᾽ :, f167r l. 31) ; **sortie du ρ** en virgule (f167r ll. 34, 37) ; **ο plein** pris pour un point (f166v l. 5 ; f167v l. 2) ;
- **clôtures de scholies** « ÷ » ou « :– » tombées au bord de la colonne (f172v l. 16) ; souillures (f166v l. 4).

Il faut donc, devant chaque point ou dicolon douteux, vérifier à fort grossissement la forme (deux points égaux et superposés pour le dicolon de T), la hauteur, et l'appartenance à la ligne.

### 5.3 Conséquences pour la transcription

- Transcrire **chaque signe tel qu'il est** : « · » pour le point (quelle que soit sa hauteur, la hauteur pouvant être précisée en `<note>` quand elle importe), « ; » pour le point-virgule, « : » pour le dicolon, « , » pour la virgule basse, « — » pour le tiret ; ne rien ajouter, ne rien convertir en ponctuation moderne.
- Distinguer la main : les « ; » complétés par la main de 1516 s'encodent `<add main="Rrec">`.
- Ne jamais interpréter un dicolon comme changement de locuteur dans la transcription : l'interprétation appartient à l'apparat.

---

## 6. Accentuation, esprits, iota adscrit, élision, tréma, coupe des mots

### 6.1 Les accents

**T accentue presque tous les mots, titre compris.** Formes : aigu en simple trait oblique ; grave ; circonflexe arrondi, anguleux ou en crochet, souvent **réduit à un point** (φῶς, δεῖ, ποῦ, τῶν, f164r ll. 4, 21, 29, 31 ; πρᾶο, νῦν, f177r ll. 1, 19), parfois en long trait horizontal surmonté d'une pointe (θρᾶττ᾽, f165v l. 43). Les accents sont souvent **déportés vers la droite** (νήνεμος, αἰθήρ, f163r l. 27 ; esprit rude et aigu de ἅμα au-dessus du μ, f174r l. 1), ou **très hauts**, jusqu'au pied de la ligne précédente (f168v l. 12 ; f169v l. 2 θεώ).

**Accentuation propre à R, à ne pas normaliser** : doubles accents (κ᾽ ἄλλός et περὶθρέξαι, f170r l. 21 ; ἔργόν, f176v v. 1172 ; μὴδὲν, f163r l. 30) ; mots sans accent (βαϋζα, f173r l. 19 ; ἐξαιρε et δε, f174r ll. 23, 37 ; επηκοω, f176r ; τι δέ με τοῦτο, f169v l. 39 ; λάλο…, f175v v. 1097) ; accents « fautifs » (ἐπι δημεῖ, f162v v. 40 ; πάσαν:, f170r l. 22 ; κριτύλλά, f173r l. 22). Velsen 1883 en signale beaucoup d'autres, que les inventaires n'ont pas tous contrôlés (f171v §e, f172r §e).

**La règle de l'oxyton et sa correction.** T met parfois le grave sur une finale oxytone même devant une ponctuation ou un enclitique. Un correcteur ancien a corrigé une quinzaine de ces graves en aigus (une vingtaine si l'on compte les corrections que Velsen 1883 signale et que l'image ne montre pas), **sans gratter le grave** : il trace un aigu qui part du pied du grave, d'où un accent « **en V** », « **en ✓** » ou « **en croix** » :

| Mot | Folio, l. (v.) | Forme | Source |
|---|---|---|---|
| καινόν·, ἁγνήν·, εἰκός· | 174r, 9, 13, 16 (967, 971, 974) | « ✓ » : grave épais et court, aigu long et mince | f174r #10, #50 ; Velsen 1883 « corr. ex καινὸν· » ; vu (`../specimens/f174r/f174r_l09_kainon_accent.png`) |
| ἐγώ·, καιρός (devant ἐστι) | 170r, 14, 26 (650, 661) | V : grave de T et aigu à l'encre neutre | f170r §d (contre Velsen 1883, qui donne le sens inverse au v. 650) |
| ἀεί | 169r, 27 | V | f169r §e |
| κακόν, παρών | 164v, 30, 23 (195, 188) | croix ; aigu seul | f164v §d |
| σεαυτόν | 165r, 26 (234) | croix | f165r #36 |
| κακά, γυνή, διός, δυσμενήσ | 167r l. 9 (388) ; 166v l. 9 (345) ; 165v l. 21 (272) ; 171r l. 37 (757) | aigu à tête épaissie ou V | inventaires correspondants |
| τουτί | 163r, 37 (73) | grave et aigu superposés en V | f163r §4 |
| ἐγώ | 164r, 37 (158) | aigu à tête épaissie | f164r §d |

Dans l'autre sens, un aigu est barré et un grave posé au-dessus (εἰσιὼν, f168r l. 30), un grave est ajouté à côté de l'aigu de T (εἰσὶν, f172r l. 29) ; la main de 1516 ajoute un grave orangé sur πρὸς (f172r l. 10) et barre celui de παρὰ pour obtenir παραβάλλουσαι (f172r l. 5, d'où le « × » de la ligne). La main du correcteur (T en relecture, S2, ou un « correcteur à l'encre neutre » au f. 170r) ne se laisse pas trancher par l'encre, les accents étant trop petits pour une mesure fiable.

**Pièges** : l'accent en V n'est pas un circonflexe ; l'accent en « ✓ » n'est pas le signal √ du copiste (qui est en marge) ; l'accent en croix n'est pas un signe critique (f167r l. 15 ἀνδράσι ; f172r l. 5).

### 6.2 Les esprits

- **Formes.** Sur les premières pages, esprits **triangulaires** ou en **coin anguleux** (┤, ⊢), qui ne distinguent pas toujours le rude du doux (f162v, f163r, f167v ll. 11, 34, 41) ; crochet en « ↄ » (f163v l. 19, ἄνδρ᾽) ; ailleurs, **petits points ou virgules arrondies**, doux et rude indistincts (f172v ; f167r #75 pour les crases ἀνὴρ, ἀδελφὸς, ἄνδρες, que Velsen 1883 et Wilson lisent avec l'esprit doux). L'esprit et l'accent sont deux signes séparés (en « flèche » sur ἤδη, f167r l. 6 ; deux points juxtaposés qui imitent un tréma, f167v, f168v l. 14).
- **Place.** En haut à gauche de la voyelle initiale, parfois bas et loin à gauche (f163v l. 19), jusque dans la bande des sigles en tête de vers (§ 5.2). Sur une diphtongue, sur la seconde voyelle ; une fois sur les deux (ὀὐμὸσ, f172v l. 33).
- **Omissions** fréquentes : περὶ εμοῦ, δ᾽ εστιν, εστὶν, ὴ, ειμὶ (f163v) ; η, article, sans esprit (f163v l. 1) ; όσαις (f166v l. 19) ; αλιμέδον (f166r) ; εφέποντας, εσται (f170r ll. 40, 43) ; ἐπαυτὸν (f171v l. 6) ; ἑαυτῷ (f173v v. 952) ; επηκοω (f176r) ; ἠν avec le seul doux (f163r l. 33).
- **Corrections** signalées par Velsen 1883 (ἐξεύροιμ᾽, v. 23 ; esprit ajouté sur ᾧ, v. 16) : la seconde est visible (petit esprit rude à gauche du circonflexe, S2 selon Velsen, f162v), la première ne l'est pas à cette résolution.

### 6.3 L'iota adscrit

T écrit l'iota **sur la ligne**, comme une lettre pleine (f172v, f174v) ou réduite à un trait court (f167r), parfois **détachée** du mot (ταυτῶ ι, χωρίω ι, εὐριπίδη ι, f175r ll. 16–17). **Jamais souscrit.** Il est **irrégulier** :
- *présent* : ὀλέθρωι, ξυνελευθέραι, γᾶι (f163v) ; τέχνηι, τῆι (f163r, f167v) ; προδῶισ, ὤιμοι, σιωπᾶισ, δᾶιδ᾽, φροντίσηισ (f165r) ; θεσμοφόρωι, ἠραρμόσηι (f165v) ; τραγωιδίαις, δρᾶι (f167v) ; τῶι κορινθίωι ξένωι (f167r l. 25) ; στεριφῆι, πανταχῆι, κύκλωι, λάθηι, τούτωι (f170r) ; σ᾽ οὐξηιρήσατο (f171r l. 41) ; ἔργωι πορίμωι, πολλῆι σπουδῆι (f171v) ; τρόπωι, φωνῆι, κύκλωι (f174r) ; δρᾶισ, ὁρᾶισ, γαμηλίωι, δεσμίωι, γλαυκέτηι (f174v) ; κλοπῆι, τῆι (f173r) ; ἐφ᾽ ὧι (f176r v. 1162) ; γρᾶιδιο, γρᾶιο (f177r) ; βοώιη (f168r l. 41, dont la Juntine a lu le Η comme un Ν : βοῶν) ;
- *absent* : τραγωδῶ, λάθρα (f163v) ; ἐλπίσης (f164v l. 30) ; ἱερῶ (f174r l. 6) ; δάκη, ὑπο λίθω (f168v vv. 529–530) ; γρᾶ́διο, ταύτη (f177r) ; τῆ μιαρά à côté de τῆι (f175v v. 1096).

Dans les scholies, Rutherford imprime des ι adscrits là où l'image montre de petits signes de valeur incertaine (f166r, vv. 295, 300) : à étudier au chapitre 3.

### 6.4 Élision, apostrophe, crase

- **L'apostrophe est notée le plus souvent** (γ᾽, τ᾽, θ᾽, δεῦρ᾽, εἶτ᾽, f163r) ; formes : petit crochet, chevron (πότ᾽, f168v l. 18), point (τάδ᾽ εὔγματα, f166v l. 18).
- **Elle manque souvent** : μὴδὲν, ἱκέτευ (f163r l. 30) ; εὐφημί ἔστω, deux fois (f166r ll. 2–3) ; λέξουσ, ποοῦσ (f167r) ; λακωνὶκ ἄττα (f167v l. 1) ; χ ἥτις, ὧδ (f168v vv. 522, 525) ; ἀνίστασ (f170r l. 8, « RG ») ; μὸ (f177r l. 5).
- **Apostrophe ajoutée après une consonne finale**, surtout **οὐκ᾽ / οὐχ᾽**, habitude du copiste déjà notée par Martin 1882, xiii (dossier ; f162v vv. 5, 7, 8 selon Velsen 1883) : οὐκ᾽ οὖν (f165r l. 18), οὐχ᾽ (f165v l. 9), οὐκ᾽ (f164v l. 23 ; f167v ll. 29, 40 ; f168v ll. 18, 41), κ᾽ οὐκ᾽ ἐκύησα (f170r l. 6 ; l'apostrophe de οὐκ᾽ est visible, `.travail/chap5/vues/f170r_l6_ouk.png`), κ᾽ οὐκ᾽ ἔστιν (f173v v. 946) ; aussi ῥήτωρ᾽ (f168v l. 22), ἀπόλλω᾽ (f165v). Au f. 174r l. 7, l'apostrophe que Velsen lit après οὐκ n'est pas distincte.
- **Crase.** T écrit souvent la crase de καί comme une élision : κ᾽ ἀλκαῖος, κ᾽ ανακρέων (f164r l. 42), κ᾽ ἄλλός (f170r l. 21), κ᾽ ἀξ, κ᾽ ἀπάγορεύετε (f171v ll. 24, 28), κ᾽ ἀνδραποδιστάς (f172r l. 27) ; ailleurs avec le crochet de crase (κᾆτ᾽, κᾆθ᾽, f168r ll. 17, 21 : ce n'est pas une brève, contre l'impression de Velsen 1883). ὠϋριπίδη (f162v v. 4), avec tréma, est accompagné en marge du signal ÷ de T (f162v #11).

### 6.5 Le tréma

T met le tréma sur ι et υ après voyelle ou en tête de mot, sans régularité : ἴβϋκος et τηΐος (f164r l. 40), ϊκρίων (f167r l. 16), τουτωῒ (f165r l. 42 ; Velsen 1883 l'omet), ϊὴ παιών (f166r l. 18), εὐΐον, συῒ (f174r ll. 32, 36, 37), -στρεϊα (f175r l. 15), ταυτηΐ (f177r l. 13), βαϋζα (f173r l. 19), ὠϋριπίδη (f162v v. 4). Le Γϋ de la main de 1516 porte lui aussi un tréma.

### 6.6 La coupe des mots

La minuscule de T groupe les mots selon l'accent plus que selon le lexique :
- **préverbes détachés** : ἐπι δημεῖ (f162v v. 40), περί θου, ἀν ἔστην (f167r), πρὸ σαγαγοίμην (f172v l. 15), ὑπερ ἀποκρίνῃ (f164v l. 21), ὑπο λίθω (f168v v. 529) ;
- **mots soudés** : ἅμαδὲκαὶ (f174r l. 1), ἐνβραχὺ, κἀνεκβάληι, προτοῦ (f167r), ἐπαυτὸν (f171v l. 6), κατόρεα (f174r l. 34), προσεμε (f176r v. 1161) ;
- **blancs fortuits** : κλαί ειν, δή μητρα, ἡμί κραι ραν (f165r), πο ο ῦσ᾽, οἰ νο πό τι δας (f167r), ἑορ ταῖσ, τῆ στὸν, καθῆ σθαι (f172v), πρὸ σθάλη κον (f165v l. 41) ;
- **coupes qui produisent une autre lecture** : ἀρ ἀπό τε pour ἆρα πότε (f162v v. 1, f162v #6, `../specimens/f162v/f162v_l02_ara_pote.png`) ; προσμάθοι· μὴ (v. 24) ; δημήτηρ pour δὲ μήτηρ (f170r l. 7) ; τὸ δὶ δὴ ἔκυψε (f170r l. 9) ; δι εκίνων (f164r l. 42) ; ἐν ἱ ερῶ, avec deux petites virgules sous la coupe (signe d'union ? f174r l. 6).

`ravennas/FORMAT_TRANSCRIPTION.md` prescrit une coupe normalisée, sauf quand elle importe à une leçon. Les cas de la dernière liste relèvent de l'exception : la coupe de R y doit être conservée (ou signalée en `<note>`), parce qu'elle est à l'origine de leçons des collations et de la Juntine.

### 6.7 Conséquences pour la transcription

- **Accents et esprits tels qu'écrits**, y compris fautifs, doubles ou absents ; un accent corrigé s'encode `<subst>` (état premier lisible : grave de T, aigu ajouté), avec la main `R?` si elle n'est pas tranchée ; un esprit rejeté dans la bande des sigles se transcrit sur sa voyelle (c'est sa fonction), avec une `<note>` si la position peut tromper.
- **Iota adscrit** : écrire ι sur la ligne là où R l'a (τῆι), ne jamais l'ajouter ni le convertir en souscrit ; l'ι détaché reste attaché au mot dans la transcription.
- **Apostrophe** : noter celle de R, y compris οὐκ᾽, et ne pas en restituer quand elle manque (λέξουσ, εὐφημί ἔστω).
- **Tréma** : transcrire ϊ, ϋ.
- **Coupe des mots** : normalisée, sauf les cas qui touchent la leçon (liste ci-dessus), où l'on garde la séparation ou la soudure de R.

---

## 7. Conséquences pour la transcription diplomatique (synthèse)

Ces règles complètent `ravennas/FORMAT_TRANSCRIPTION.md` ; les points marqués « proposition » demandent une décision du guide de transcription (`ravennas/GUIDE_TRANSCRIPTION.md`).

**Lignes et zones**
1. **43 `<l>` par page**, dans l'ordre de la colonne : une réglure vide se note par une `<l>` vide ou une `<note>` (f162v, réglure 2 ; f177r, réglures 24 et 39–43) ; le titre, la ligne ornementale, le titre et l'hypothesis de l'*Assemblée* sont des `<l>` avec `zone="titre"` ou `zone="hypothesis"`.
2. Les lignes qui ne sont pas des vers (parépigraphes, ligne supplémentaire du f. 176v, lignes annulées ou exponctuées, mots en débord centrés) sont des `<l>` de plein droit ; les vers omis et suppléés en marge sont des ajouts marginaux (`<add place="mg-g|mg-d">` ou `<sch>` selon le guide), jamais des `<l>`.
3. Pour les parties lyriques, noter le **renfoncement** (`retrait`, en lettres) ; **proposition** : admettre une valeur négative (ou un attribut `saillie`) pour les vers en ekthesis et les initiales sorties dans la bande des sigles.
4. Les **mots coupés** en fin de ligne restent coupés (une partie par `<l>`), avec le trait d'union quand il y en a un (μεταβαλοῦ-, f171r l. 3) ; le tiret de παῖ — (f166r l. 27) se transcrit.

**Marques de T**
5. `<parag/>` en tête de `<l>` pour toute paragraphos de T, qu'elle corresponde ou non à un changement de locuteur dans les éditions ; à sa place dans la ligne pour la paragraphos de milieu de ligne (scène d'Écho) ; `<unclear>` quand elle n'est que présumée sous un sigle (« selon Velsen »).
6. Paragraphos barrée : `<del type="biffure" main="Rrec"><parag/></del>` (ou `main="R?"`/`"R1"` pour les annulations brunes des vv. 608, 620, 926) ; grattée : `<del type="grattage">`.
7. Dicolon : « : » à sa place dans la ligne (y compris en fin de ligne) ; blanc de réplique : `<sp/>` ; point simple : « · ». **Proposition** : un caractère distinct (« ⁚ », U+205A) pour le dicolon de T, afin de le séparer sans ambiguïté des deux-points de la ponctuation moderne lors des conversions.

**Sigles**
8. `<nota main="R2|Rrec">` pour chaque sigle, avec la lettre suscrite transcrite comme ajout au-dessus (§ 4.5) ; sigle repassé : main d'origine et **proposition** d'attribut `retouche="Rrec"` ; sigle gratté : `<del type="grattage">` + `<note>` citant G quand il le connaît.
9. Les indications de jeu et notes développées de S2 (πρὸ(ς) τ(ὰς) γυναῖκας ; ἠρέμα ὁ κηδεστ(ής)…) sont des `<sch>` ou des `<nota>` selon leur place ; les signes d'insertion de 1516 (« ^ », « √ », croix de renvoi) sont des `<signe type="renvoi" main="Rrec">`.

**Ponctuation, accents, esprits**
10. Ponctuation, accents, esprits, iota adscrit, apostrophes, trémas : **tels qu'écrits**, sans normalisation ni restitution (§§ 5.3, 6.7).
11. Corrections d'accent : `<subst>` (grave de T → aigu ajouté), main `R?` si elle n'est pas tranchée ; virgules de 1516 qui transforment un point en « ; » : `<add main="Rrec">`.

**Protocole de lecture**
12. Devant tout point, dicolon, trait ou croix de la bande des sigles, vérifier à fort grossissement : (a) forme (paragraphos en massue, dicolon à deux points égaux) ; (b) appartenance à la ligne (signes de la ligne voisine) ; (c) encre (orangé = 1516 ou note ancienne d'encre rougeâtre, § 4.1) ; (d) témoignage de Velsen 1871 et de G. Ne jamais restituer une marque d'après le texte attendu.

---

## 8. Questions à trancher sur l'original

1. **Réglure du f. 162v** : la 2e réglure est-elle bien vide (sillon à y ≈ 414) ? Le titre est-il écrit sur la réglure, et non suspendu dessous comme le texte ?
2. **Paragraphoi présumées sous les sigles de 1516** (vv. 22, 26 au f. 162v ; ff. 164v, 173r, 175r, 175v, 177r) : sont-elles réellement présentes ? Une lumière rasante ou une image UV séparerait l'encre de T de l'orangé.
3. **Annulations brunes** des vv. 608, 620 (f169v) et 926 (f173v) : T en relecture ou S2 ? L'ordre des traits (paragraphos, puis barre) se lit-il au microscope ?
4. **Notes de forme S2 à l'encre orangée** (vv. 655, 659, 785, 1001, 1107, 1207 ; f175v) : seconde encre de S2, autre correcteur ancien, ou repassage de 1516 ? La présence dans G des vv. 655, 785, 1107 et 1207 exclut une création de 1516.
5. **κη^Δ du v. 592** : sigle de S2 repassé, ou de 1516 ? κηδ des vv. 567 s. signalé par van Leeuwen : existe-t-il ?
6. **v. 72** : la paragraphos nette du f. 163r témoigne-t-elle d'une autre répartition des vv. 70–72 dans le modèle ?
7. **Dicolon et trait à la fin du v. 6** (« φράσον : — ») : marque d'un changement en tête du v. 7 dans le modèle, ou ponctuation forte suivie d'un trait de remplissage ?
8. **Petits signes inexpliqués** : « ·ʃ· » de l'interligne 7/8 du f. 162v ; « ~ » sur χωρὶς (v. 11) ; trois points devant ταύτην (f166r l. 16) ; deux virgules sous ἱ|ερῶ (f174r l. 6) ; point isolé de la bande des sigles (f173r l. 29) ; paires de traits « // » du f. 170r.
9. **Corrections d'accents** : quelle main (T en relecture, S2, « correcteur à l'encre neutre ») ? Les corrections que Velsen 1883 donne pour sûres et que l'image ne montre pas (παρεστώς, ἐξεύροιμ᾽, ἰδού au f. 162v ; τέως au f. 167v) existent-elles ?
10. **Colométrie des vv. 655–688 et 1015–1055** : à confronter ligne à ligne à Velsen 1883 (pp. 49 et 75–79) et, pour la première, à la Juntine.

---

## 9. Planches et spécimens du chapitre

Planches (`../planches/`), composées à partir des images à pleine résolution par `.travail/chap5/planches.py` :
- `../planches/5_planche_paragraphos.jpg` — la paragraphos de T sous la ligne du changement (ff. 162v, 169v, 173v, 176v) ;
- `../planches/5_planche_sigles_parent.jpg` — Μνησίλοχος et κηδεστής : notice initiale, sigles de S2 et de 1516 (ff. 162v, 164r, 168r, 168v, 169v, 170v) ;
- `../planches/5_planche_mise_en_page.jpg` — titre, fin de la pièce et titre de l'*Assemblée*, scène d'Écho sur deux colonnes, renfoncement lyrique (ff. 162v, 177r, 175r, 166v) ;
- `../planches/5_planche_accents_ponctuation.jpg` — accent corrigé en crochet et en V, esprit rejeté, iota adscrit, οὐκ᾽, point-virgule, dicolon de pause, dicolon pur (ff. 174r, 170r, 166v, 164v, 164r, 165r, 162v).

Spécimens individuels (≤ 600 px) : `../specimens/chap5/5_*.png` (24 fichiers, un par panneau des planches). Les autres spécimens cités viennent des inventaires (`../specimens/fXXX/`).

---

## 10. Contrôles effectués sur les images

J'ai vérifié moi-même, sur les images à pleine résolution (vues `.travail/chap5/vues/`), les points dont dépendent les conclusions :

| Point contrôlé | Lieu | Résultat |
|---|---|---|
| titre, ornement, absence de rubrique ; notice « προλογίζει » | f162v l. 1 et marge sup. | confirmé |
| nombre de réglures du f. 162v | f162v, profils passe-haut du canal bleu (x 1500–1800, y 300–640) | sillon à y ≈ 409–416 entre le titre et le v. 1 : 43 réglures, la 2e vide (correction) |
| paragraphoi des vv. 7, 8, 9, 12, 14 ; absence au v. 11 | f162v ll. 8–15 | confirmé ; celle du v. 14 est nette, sans changement en tête |
| paragraphos annulée (⊥) du v. 620, paragraphoi des vv. 621–623, dicola | f169v ll. 26–31 | confirmé |
| paragraphoi barrées des vv. 926 et 935 ; dicolon du v. 935 ; ligne annulée | f173v ll. 5–8, 15–18 | confirmé |
| paragraphoi des vv. 1184 (barrée), 1192 (intacte), 1194–1195 (barrées) | f176v ll. 15–17, 23–29 | confirmé |
| ΜΝΗΣΙ^λο du v. 130 : S2, non T | f164r l. 9 | confirmé (petites majuscules, encre des scholies) ; contre van Leeuwen 1904 |
| parépigraphe ὀλολύζεις γέρων, trait ondulé rouge | f164r l. 8 | confirmé |
| κη^δ de S2 au v. 540 (brun) | f168v l. 32 (spécimen de l'inventaire) | confirmé |
| κη^δ de S2 suscrit au v. 603 ; κη + Λ orangé de 1516 au v. 604 | f169v ll. 11–12 | confirmé |
| κηδ : ευ· orangé de 1516 au v. 466 | f168r l. 1 | confirmé |
| μνη^σ de S2 au v. 692 | f170v l. 15 | confirmé |
| scène d'Écho sur deux colonnes ; paragraphoi de milieu de ligne ; paragraphoi barrées des vv. 1076a, 1078a, 1092b, 1093, 1095 | f175r ll. 30–43 ; f175v ll. 1–16 | confirmé |
| fin de la pièce, ligne ornementale, titre et hypothesis de l'*Assemblée* | f177r ll. 20–29 | confirmé |
| point-virgule interrogatif τί σ πάτρα; | f164r l. 15 | confirmé |
| dicolon de pause με : χώρει | f165r l. 21 | confirmé |
| esprit doux rejeté en point devant εὔχεσθε | f166v l. 15 | confirmé |
| apostrophe de οὐκ᾽ dans κ᾽ οὐκ᾽ ἐκύησα | f170r l. 6 | apostrophe après οὐκ visible ; celle de κ᾽ est moins nette |
| accent en crochet de καινόν· | f174r l. 9 (spécimen) | confirmé |
| dicolon pur du v. 31 | f162v l. 32 | confirmé (deux points pâles, égaux) |

---

## 11. Corrections et compléments aux inventaires de page

- **f. 162v** : la page a **43 réglures** (et non 42) : la 2e, sous le titre, est restée vide (§ 1.1).
- **Paragraphoi « fausses »** (ff. 162v, 165r, 169v, 171r, 172v, 173r, 173v, 174v, 175v, 176v, 177r) : vingt-cinq d'entre elles suivent la convention antique (§ 3.3) et six marquent une division du discours ; l'inventaire du f. 169v (suivi par le chapitre 4, tableau B), qui juge « juste » l'annulation du v. 620, et ceux des ff. 175v et 176v, qui parlent de marques « fautives » aux vv. 1119, 1184, 1192, 1194, 1195, sont à nuancer en ce sens. L'hypothèse de l'inventaire du f. 173v est confirmée sur toute la pièce, avec la réserve d'un système mixte.
- **Sigles κηδ de S2** : ceux des vv. 603, 1107 et 1207 sont antérieurs à 1516 (G) ; il faut corriger en ce sens Velsen 1871, 21 (v. 603) et van Leeuwen 1904 (« manus recens » aux vv. 603 s., 1107, 1207). Le κηδ ευ de 1516 au v. 466 récrit une note de S2 que G a conservée.
- **Dicola de fin de ligne** non relevés par Velsen 1883 : vv. 194, 199 (f164v), 874 (f172v) — déjà notés par les inventaires, à reporter dans l'apparat des attributions.
- **Encre orangée** : elle ne suffit pas à attribuer un sigle à 1516 (§ 4.1) ; les inventaires des ff. 170r, 171v, 174r, 175v, 176v l'avaient vu chacun pour sa page : c'est un fait général.
