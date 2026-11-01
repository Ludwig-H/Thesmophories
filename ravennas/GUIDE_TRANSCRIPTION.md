# Guide de transcription du *Ravennas* (*Thesmophories*, ff. 162v–177r)

> **Statut** : rédigé le 1er novembre 2026 à partir des cinq chapitres vérifiés de l'étude graphologique (`ravennas/graphologie/chapitres/`), des trente inventaires de page (`ravennas/graphologie/folios/`) et de contrôles nouveaux sur les images. Syntaxe du format : `ravennas/FORMAT_TRANSCRIPTION.md` (DiploXML v1).
>
> **Hiérarchie des autorités** : l'image ; puis ce guide ; puis les chapitres (partie vérifiée) ; puis les inventaires ; enfin les imprimés (Velsen, Coulon…) et le texte de référence, qui ne sont que des listes de points à contrôler. Quand ce guide tranche entre deux chapitres, il le dit (§ 3.8). Les travaux de Gemini ne sont jamais une source.

## 0. Avant de commencer

**Six règles.**

1. **L'image d'abord.** Aucun texte imprimé, aucune vulgate avant la fin de la lecture (§ 5).
2. **Le signe, non sa fonction.** Un dicolon se transcrit « : », qu'il y ait ou non changement de personnage. Une paragraphos se transcrit même si elle est « fausse ». L'interprétation appartient à l'apparat.
3. **Rien de normalisé, rien de restitué.** Fautes, accents doubles ou absents, apostrophes parasites, barbarismes du Scythe : tels quels. Le texte attendu ne sert qu'à provoquer un recontrôle. L'auteur a décidé que le livre corrigerait les fautes évidentes et d'accentuation : cela se fait **après** la vérification, par une couche `<corr>` qui laisse intacte la leçon de R (`ravennas/FORMAT_TRANSCRIPTION.md`) ; lecteurs, arbitre et vérificateur n'y touchent pas : ils établissent ce que porte le parchemin. Noter `signe=` à chaque compendium : le livre imprime le signe.
4. **Une marque, un objet.** La paragraphos de T et le sigle de 1516 posé dessus sont deux objets, encodés séparément, chacun avec sa main.
5. **L'encre ne décide que dans trois cas** (§ 1.3). Partout ailleurs, la forme tranche, ou l'attribution reste `R?`.
6. **Le doute se balise.** `<unclear>`, `R?`, `<note>` ; jamais une lecture plausible sans balise.

**Références.** « l. » = rang de la ligne **d'écriture** sur la page, de haut en bas, titres et lignes de chant compris (une réglure vide ne compte pas). « v. » = numérotation usuelle (celle de Brunck et de l'auteur : colonne `usuel` de `edition/donnees/concordance_vers.tsv` ; les clés de `.sources/corpus/thesmo_hall_geldart.tsv`, numérisation Perseus, en diffèrent par endroits : voir `recherche/numerotation_vers.md`). Coordonnées en pixels de l'image pleine résolution (1 px ≈ 0,116 mm). « vu » = revu sur l'image pour ce guide. « inv. » = repris d'un inventaire, non revu ici : à contrôler sur place.

**Spécimens.** `[id]` renvoie à `ravennas/graphologie/planches/specimens_guide.tsv` (coordonnées), aux découpes `ravennas/graphologie/specimens/guide/<id>.png` (régénérables par `python3 outils/graphologie/specimens_guide.py`) et aux planches versionnées `ravennas/graphologie/planches/guide_pl1.jpg` (lettres), `guide_pl2.jpg` (ligatures), `guide_pl3.jpg` (faux signes, abréviations de T), `guide_pl4.jpg` (lignes des exemples). Abécédaire complet de T : `ch2_pl1_abecedaire_1.png`, `ch2_pl2_abecedaire_2.png`. Écritures et abréviations de S2 : `ch3_pl1_ecritures.jpg`, `ch3_pl2_abreviations.jpg`, `ch3_pl3_renvois.jpg`, `ch3_pl4_pieges.jpg` (même dossier). Sigles : `5_planche_sigles_parent.jpg`. Encres : `../chapitres/planches/1_pl1_ecritures.jpg`, `1_pl2_encre_orangee.jpg`, `4_groupe_Rn.png`.

---

## 1. Les mains

### 1.1 Tableau définitif

Étiquettes du chapitre 1, § 9. Le chapitre 1, § 9.4 fixe les couleurs d'impression (elles sont encore à reporter dans `edition/thesmo.cls`).

| `main` | Imprimé | Couleur | Qui | Ce qui en relève |
|---|---|---|---|---|
| `R1` | R | noir #161616 | T, le copiste (milieu du Xe s.) | texte, titres, parépigraphes, paragraphoi, dicola, ponctuation, accents de première main, signaux |
| `R1c` | R^pc | vert-de-gris #4F5D2F | T qui se corrige | biffures et exponctuations en écrivant ; lettres suscrites de même module et de même encre ; μέντοι (v. 630, présumée) |
| `R2` | R² | carmin #B2182B | S2, scholiaste et correcteur ancien | scholies, gloses, sigles à lettre suscrite, vers suppléés, suscriptions, renvois |
| `R2` + `repasse="Rrec"` | R² (rep. R^XVI) | carmin, pointillé orange | contenu de S2, encre de 1516 | notes de forme S2 à l'encre orangée, attestées par M (§ 1.5) |
| `R3` | R³ | violet #7A3E9D | correcteur ancien à l'encre brun-noir, antérieur à M | vv. 646, 939 ; 493, 874 (§ 1.5) |
| `Rsch` | R^sch | sarcelle #00727A | main de la marge intérieure, troisième main ancienne | deux scholies de la marge intérieure du f. 162v (vv. 27, 30–32), rien d'autre |
| `Rrec` | R^XVI | orange brûlé #A85400 | campagne de 1516 (« Boninus » n'est pas démontré : écrire « main de 1516 ») | sigles imprimables, corrections et « ; » orangés, signes d'insertion, paragraphoi barrées, grattages de sigles |
| `Rrec` + `instrument="mine"` | — | idem, pointillé | atelier de 1516 | repères de pages de la Juntine, barre grise du v. 1076 |
| `Rmod` | R^mod | bleu #1D4E89 | mains modernes | foliotations, signature « 22 » (encre brune), crayons rouge et bleu |
| `R?` | R^? | gris #707070 | indéterminée | tout ce que ni la forme ni l'encre ne permettent d'attribuer |

### 1.2 Critères de reconnaissance

**T (`R1`).** Minuscule ronde et liée, écrite sous la réglure. Lettres rondes de 16–18 px, corps de 13–16 px (1,5–1,9 mm), interligne de 42–44 px. Chaînes de ligatures par le haut ; longues hampes qui se croisent d'une ligne à l'autre ; formes onciales réglées par la position (Η, Ν, Є, Ο agrandi, C dans -ος). Encre brune homogène sur toute la pièce. Une seule rupture d'ensemble : décalage des mesures à partir du f. 176r, sans changement de main. T n'écrit **aucun nom de personnage**.

**T qui se corrige (`R1c`).** Même module, même ductus, même encre : ἐκ^κλησίαν (l. 39, f. 166v), ⟦τί⟧ φέρε (v. 768). Une lettre suscrite sans forme distinctive peut être de S2 : `R1c` n'est alors que probable, et on le dit en note ; sans critère, `R?`.

**S2 (`R2`), quatre registres.**
- *Semi-onciale inclinée* des scholies : majuscules disjointes et anguleuses de 11–14 px (1,3–1,6 mm), ε et σ lunaires, Κ fait d'une haste et d'un « c », Ν à diagonale basse, accents posés sur les majuscules, compendia accentués.
- *Petites majuscules plus droites* des gloses (Π, Ρ, Τ, Γ, Υ en Y, Κ en deux pièces).
- *Sigles* en petites majuscules ou semi-onciale, à lettre suscrite, à gauche de la paragraphos sans la recouvrir, ou dans l'interligne au-dessus d'un dicolon.
- *Minuscule* : série continue de scholies à lemmes semi-onciaux au f. 162v (marges supérieure et extérieure ; un peu inclinée, irrégulière, à capitales mêlées) ; lettres et mots ajoutés au texte ; grande minuscule penchée à capitales des vv. 1102–1103.

Un changement d'écriture dans une note n'est pas un changement de main (f. 175r, l. 10 ; f. 162v). Marques communes : esprit en équerre « ⊢ », circonflexe en « ^ », θ suscrit en lentille barrée.

**M (`Rsch`).** Minuscule **ronde et droite**, lettres espacées et régulières, plume assez épaisse, corps de 10–14 px, ν final plongeant, κ en « lc », ξ en « ʒ » à longue queue. Elle se distingue de la minuscule à lemmes de S2 par l'axe et l'espacement, non par le module. Elle n'existe qu'à la marge intérieure du f. 162v, aux l. 28–29 (λεί^π(ει) τὸ ἔνθα…) et 30–33 (ἐπειδὴ οὐ πάλαι…). L'encre n'y discrimine pas. Noter en `<note>` « T ? ».

**R3.** Lettres entières à l'encre nettement plus neutre et plus sombre, à densité égale, que T et S2 (ΔB/R ≤ −0,3). Écriture droite, espacée, mixte : Κ en deux traits, Π à barre, Α triangulaire, ε lunaire, mais η en « h » et ν minuscule plongeant (ἥκει πάλιν, [ex1b]). Antérieur à M pour les leçons. La position relative par rapport à S2 est inconnue.

**Main de 1516 (`Rrec`).** Encre orangée, visible à l'œil ; sigles de **grand module** (30–45 px) ; Γ en grand crochet à longue haste, souvent greffé sur le dicolon ou la paragraphos de T (Γϋ, avec tréma) ; ν suscrit en V, η suscrit en Η capital (μν^η) ; κ en croix ; εὐ en Є barré ; σκ à longue queue ; Ηχ à grand χ ; point abréviatif. Elle imite parfois S2 : le monogramme χορ du v. 1170 et « ὡς περσεύς » du v. 871 sont d'elle, malgré la forme.

**Mine de 1516.** Matière gris neutre, sans charge d'encre (G/R ≈ 1,0–1,2) : traits fins et chiffres humanistiques (« 4 » ouvert) qui coïncident avec les pages de la Juntine (a 12, a 14, b 1, c 5… : chap. 1, § 6.5). Ni paragraphos, ni biffure, ni chiffre du texte. Certains repères sont à l'encre pâle presque neutre (ff. 165v, 170r, 170v, 171v).

**Modernes (`Rmod`).** Foliotation au crayon, angle extérieur, celle de la Classense, décalée de +2 ; foliotation à l'encre, angle intérieur, ancienne (celle de la littérature et de nos fichiers) ; signature « 22 » (f. 167r) ; crayon rouge (trait ondulé sous ὀλολύζεις γέρων, f. 164r l. 8) ; crayon bleu.

### 1.3 Ce que l'encre permet

Mesure : `outils/graphologie/encres_mesure_uniforme.py mesure fXXX x0 y0 x1 y1` (écart à T de la même page, à densité égale). L'œil suffit le plus souvent.

| Opposition | Critère | Portée |
|---|---|---|
| orangé / brun | ΔB/R ≥ +0,4 sur une centaine de pixels de cœur au moins | décisif pour un sigle ou un mot |
| gris neutre / encre | G/R ≈ 1,0–1,2, sans charge | décisif pour la mine et le crayon |
| brun-noir / brun | ΔB/R ≤ −0,3 sur des lettres entières et denses | décisif pour des lettres, **jamais pour un accent ou un point** |

Trois avertissements, tous vérifiés.
- **T et S2 ne se séparent pas par l'encre** pour un trait isolé. S2 est en moyenne à peine plus jaune (+0,14), l'écart varie selon la note et disparaît dans la colonne.
- **Un petit signe mesure « gris » quelle que soit la main** (points et accents de T jusqu'à −0,6). Inversement, les petites corrections de 1516 mesurent souvent comme T.
- **Les chiffres absolus ne valent que dans une page**, à hauteur égale de la colonne : le parchemin alterne d'une ouverture à l'autre, et une auréole d'humidité fait virer les encres à l'orangé (scholies brunes « orangées » dans la tache du f. 175v). Des bords plus gris qu'un cœur orangé ne prouvent rien.

### 1.4 Ordre d'attribution

1. Tracé orangé : `Rrec`. S'il a la forme de S2 et que M l'atteste : `R2` + `repasse="Rrec"`. S'il n'a pas la forme de S2 mais que M a un sigle au même lieu : `Rrec`, note « sigle attesté par M » (vv. 211, 295, 380, 443, 582, 584, 1002, 1084–1085, 1165, 1218). L'absence dans M ne donne jamais à elle seule un tracé brun à `Rrec`.
2. Matière grise sans charge : `Rrec` + `instrument="mine"` si elle coïncide avec une coupure de la Juntine ; sinon `Rmod` + `instrument="crayon"`.
3. Encre brun-noir sur lettres entières : `R3`.
4. Sinon, la forme : semi-onciale, Ν oncial, esprit en équerre, minuscule penchée à capitales → `R2` ; même module et même ductus que le texte → `R1c` ; minuscule ronde détachée de la marge intérieure du f. 162v → `Rsch`. L'absence de ces traits n'exclut pas S2.
5. À défaut : `R?`, avec l'attribution de la littérature en note (« R² Velsen »). On n'adopte jamais une attribution de Velsen que l'image ne permet pas de contrôler.

M se consulte dans `.sources/web/ravennas/apographes/Monacensis_gr_492/` ; un relevé (`.travail/mu2/lectures_G.tsv`) sert de guide, non d'autorité. Ses images sont en niveaux de gris, et ses sigles au minium sont pâles : la pâleur n'y dit rien de l'encre de R.

### 1.5 Attributions déjà fixées

À appliquer sans les rediscuter, sauf fait nouveau sur l'image, à signaler.

| Lieu | Encodage | Fondement |
|---|---|---|
| ἥκει πάλιν (v. 646), υ de ἀποδύσαντα (v. 939) | `R3` sûrs | ΔB/R −0,44 à −0,66 ; lettres entières |
| κιν (v. 493), ι de ποίου (v. 874) | `R3`, note « probable » | forme (Κ en deux traits) pour le v. 493 ; ι presque noir pour le v. 874 |
| grave du v. 54, aigu du v. 650, esprit du v. 1149 | `R?`, note « R³ ? » | petits signes |
| vv. 661, 820 (accents) | `R?` | non démontré |
| vv. 33, 169, 647 (suppléés) | `R2`, note « attribution de la littérature » | vv. 33 et 169 ont les formes de T, à module réduit ; v. 647 petit et abrégé |
| vv. 1102–1103 (suppléés) | `R2` | grande minuscule penchée à capitales |
| v. 33, lignes (b)–(c) | `R2` + `repasse="Rrec"` ; ligne (a) `R2` ; εὐ et « ; » `Rrec` | orangé mesuré |
| v. 169 | `R2`, note « repassage douteux » | écriture trop pâle pour conclure |
| « +: » des vv. 1102–1103 | `R?`, note « orangé » | renvoi de S2 repassé, ou de 1516 |
| ÷ ondulés et ·/· du v. 647 | `R?` | encre proche de T |
| μέντοι (v. 630) | `R1c`, note « présumée » | petite minuscule rapide, μ à longue haste |
| βοώιη (v. 506) | `R2`, note « encre de T ; Velsen » | § 6, ex. 3 |
| κύβδ᾽ (v. 489), Β de βάρβιτος (v. 137) | β fermé noté ; `R?` | déjà dans M ; encre de T : pas 1516 |
| κατα (v. 60), καί (v. 306) | `R?` | absents de M et de la Juntine, sans trait de main |
| ὀλίγων (v. 443), παρα (v. 803), πρὸς (v. 806), καὶ (v. 1097), σκ ὸ (v. 1191) | `Rrec` | orangé mesuré |
| v. 1180 (graves) | `R?`, note « 1516 selon Velsen 1871 » | non orangés |
| virgules « ; » des vv. 193, 252 | `<add main="Rrec">` | orangées |
| virgule du v. 222 | `<add main="R?">`, note | brune à ×5, contre Velsen 1871 |
| hastes des « + » des ff. 165v, 175v, 176v, 177r | `<del type="biffure" main="Rrec">` | orangées, ou orangé pâle aux ff. 165v, 176v |
| hastes des vv. 232, 234, 246 (f. 165r) | `main="R?"`, note | brunes ; M a le trait simple aux vv. 232, 246 |
| barres des vv. 608, 620, 926 | `main="R?"` | brunes |
| barre du v. 1076 ; du v. 1078 | `Rrec` + `instrument="mine"` ; `R?` (pâle, roussâtre) | mesure |
| monogramme χορ (v. 1170), ὡς περσεύς (v. 871) | `Rrec` | orangés, absents de M, imitation de S2 |
| notes orangées de forme S2 dans M : vv. 5, 19, 39, 45b–46, 101, 104, 114, 117, 210, 533, 592, 655, 659 (sauf Ημι, brun), 689, 730, 785, 846, 852, 855, 871 (εὐρι^π seul), 936, 939, 1001, 1083, 1098, 1107, 1108, 1207 | `R2` + `repasse="Rrec"` | chap. 1, § 6.4 |
| v. 574 | κλει : `R2` ; σ θενησ : `Rrec` | complément, M n'a que l'abréviation |
| μνη du v. 1063b | `R?`, note « orangé ; absent de M ; R² Velsen » | |

### 1.6 À quoi s'attendre par page

Tableau complet : chap. 1, § 8.2. En bref :
- **pas de sigle de 1516** aux ff. 166v, 170r, 171v, 172r, 174r ; sigles rares aux ff. 166r, 167r, 167v, 168r, 168v, 169v, 170v ;
- **sigles de 1516 très nombreux** aux ff. 162v, 164v, 165r, 165v, 169r, 173r, 175r, 175v, 176v ;
- **aucune marque de T** aux ff. 166r, 166v (ni paragraphos, ni dicolon) ; f. 167r : le seul dicolon du v. 380 ; f. 167v : une paragraphos au v. 443, d'encre de type S2 ; f. 172r : parabase, un seul locuteur ; f. 174r : aucune paragraphos ;
- **réactif bleu-vert** sur les débuts de lignes de scholies, aux ff. 162v, 164r, 164v, 165r, 165v, 166v, 168v, 170v, 171r, 174v, 176v, 177r, et au f. 176r par transparence depuis le f. 176v ;
- **réglures vides** : f. 162v (la 2e, sous le titre) et f. 177r (la 24e et les cinq dernières).

### 1.7 Ce qui n'est pas une main

État matériel, à signaler en `<note>` s'il gêne la lecture, jamais à encoder comme intervention : réactif bleu-vert ; auréoles d'humidité ; décalques et transparences (f. 176v imprimé en miroir au f. 177r, f. 172v au f. 173r, f. 169r au f. 169v, f. 168v au f. 168r) ; pièces de restauration, tulle (f. 165v) ; plis, rides, follicules ; empreintes grises d'imprimeur (f. 173v, l. 26–27, 38–39).

---

## 2. Conventions de transcription

Ces conventions tranchent les points laissés ouverts par les chapitres 2 et 5. Chaque choix doit donner le même XML à deux lecteurs indépendants ; quand c'est impossible, il dit qui décide.

### 2.1 Lignes, numérotation, zones

- **Une `<l>` par ligne d'écriture de la colonne.** `n` suit les inventaires : réglures vides non comptées. Au f. 162v, l. 1 = titre, l. 2 = v. 1. Au f. 177r, l. 1–23 = vv. 1211–1231, l. 24 = ligne ornementale, l. 25 = titre de l'*Assemblée*, l. 26–37 = hypothesis (`zone="titre"`, `zone="hypothesis"`). Signaler les réglures vides dans `<notes>`.
- **Segmentation fautive** (`ravennas/segmentation/`) : elle ne fait pas foi. f. 168r : 42 lignes, l. 43 manquée. f. 171r : 42 lignes, l. 3 omise, donc index + 1 à partir de là (table corrigée : `.travail/graphologie/f171r/lignes_ms.json`). f. 175v : 45 lignes, dont les deux lignes des vv. 1102–1103, qui ne sont pas des `<l>`. f. 177r : 34 lignes, plusieurs fusionnées. Compter les lignes sur l'image.
- **`v`** : clés du TSV de référence (« 439a » comprise), tous les vers qui commencent sur la ligne (« 1093,1094 »). Rien pour une ligne de suite. Si un vers n'a pas de clé (684, 688, 718, 965, 1081, 1084), garder le numéro de l'auteur et le dire en note.
- **Lignes qui ne sont pas des vers** : `<l>` de plein droit, `v` vide ou partie de vers : parépigraphes (f. 164r l. 8 ; f. 165v l. 26), ligne supplémentaire (f. 176v l. 20), ligne biffée (f. 173v l. 15), ligne exponctuée (f. 176r l. 17), mots en débord (ἀθρῆσαι, f. 170r l. 23 ; ἁπαξ ἁπάσας, f. 168v l. 43).
- **Vers suppléés en marge** : jamais une `<l>`. `<add place="mg-d" main="R2">` à la fin de la ligne après laquelle le vers s'insère, avec `<lb/>` à chaque fin de ligne du supplément et, en `<note>`, la position sur la page.
- **Titre** : pas de `<hi rend="rouge">`. Pas de rubrique dans la pièce. Les deux points du titre sont des points séparateurs (`· ·`) ; ornement : `<signe type="ornement">`.

### 2.2 Lettres

- **Minuscules partout**, noms propres et initiales compris, chez toutes les mains (`ζεῦ`, `ευρι`).
- **Aucun allographe** : Η, « h », « н » = η ; Ν = ν ; Є = ε ; C = σ ; Γ = γ ; Π, ϖ = π ; ϐ, Β, β en « u » = β. Deux exceptions, en `<note>` seulement : un **β fermé** dans la colonne (il signale une intervention), une forme qui explique une leçon fausse (Η de βοώιη, lu ν par la Juntine).
- **σ partout, même en finale.** T n'a pas de ς (vérifié sur 25 finales de six pages) ; S2 écrit C. Ce choix remplace le ς positionnel du format v0 : ni le comparateur ni la collation n'en sont affectés. Ne garder ς que pour un ς réellement tracé (main de 1516), après contrôle.
- **Initiale agrandie** : `<hi rend="grand">` seulement si elle est nettement hors module (ω de ὦ, f. 162v l. 2 ; Ο de οὐκοῦν, f. 164r l. 32 ; Ο, f. 168v l. 25, 36 ; Φ, f. 169r l. 25). Ce n'est jamais un indice de changement de personnage.

### 2.3 Accents

- **Tels qu'écrits**, y compris doubles (κ᾽ ἄλλός), absents (ἐξαιρε) ou fautifs (πάσαν). Écrire le mot sans accent quand aucun n'est visible, et le dire en note si le mot compte.
- **Accent déporté** : le poser sur la voyelle qu'il coiffe par fonction, non sur la lettre qu'il surplombe : T déporte à droite, parfois jusqu'au pied de la ligne supérieure. Note seulement si l'attribution à une voyelle change la lecture.
- **Circonflexe réduit à un point** (φῶς, δεῖ, ποῦ, f. 164r ; πρᾶο, νῦν, f. 177r) : c'est un circonflexe, si la voyelle en appelle un et que rien d'autre ne l'explique ; sinon `<unclear>`. Jamais une ponctuation.
- **Aigu ou grave indiscernable** (trait trop court) : `<unclear cert="moyenne">`.
- **Accent corrigé** : au niveau de la lettre, jamais d'accent isolé.
  - Grave de T, aigu ajouté, grave non gratté (accent en V, ✓ ou croix) : `καιν<subst main="R?"><del type="surcharge">ὸ</del><add place="ligne">ό</add></subst>ν`. Note : forme (« ✓ soudé » ou « deux traits séparés »).
  - Accent annulé : `<del type="biffure" main="Rrec">ὰ</del>` suivi de l'`<add>` de la lettre nue, dans un `<subst>`.
  - Accent gratté : `<subst main="R?"><del type="grattage">ῖ</del><add place="ligne">ι</add></subst>`.
- **Correction que seul Velsen signale**, invisible sur l'image : ne pas l'encoder ; note « corr. sec. Velsen 1883, non visible ».

### 2.4 Esprits

- **Forme** : coins, triangles, points, virgules. Sur la plupart des pages, **rude et doux ne se distinguent pas**.
- **Règle** : si la forme est lisible, transcrire ce qui est écrit, même fautif. Si un esprit est présent mais d'espèce indiscernable, écrire l'esprit attendu et ajouter, une fois par page, la note « esprits d'espèce indistincte » : la valeur doux/rude de cette page n'est alors pas une donnée. Quand l'espèce change la lecture (ὁ/ὅ, ἡ/ἥ, οἱ/οἷ, ὧν/ὦν, et les crases ἀνήρ, ἀδελφός, ἄνδρες, f. 167r), `<unclear>` et note « esprit indistinct » : ne pas restituer la crase des éditions.
- **Pas d'esprit visible** : pas d'esprit (`εμοῦ`, `εστιν`, `η`). C'est fréquent ; ne jamais en ajouter un.
- **Esprit rejeté à gauche**, jusque dans la bande des sigles : il se transcrit sur sa voyelle ; note si la position peut tromper.
- **Sur une diphtongue** : sur la seconde voyelle, sauf si R fait autrement (ὀὐμὸσ, f. 172v l. 33).

### 2.5 Iota adscrit, tréma

- **ι écrit sur la ligne** : ι dans le mot (`τῆι`, `ὁρᾶισ`), plein, réduit ou détaché (`ταυτῶι` pour ταυτῶ ι, note si détaché). **Jamais de souscrit**, ni dans le texte ni par commodité : `ᾳ`, `ῃ`, `ῳ` n'existent pas dans la transcription de T. Pas d'ι visible : rien (`τραγωδῶ`, `ταύτη`). `avertir()` signale les oublis.
- **ι en deux touches** : c'est un ι, non un dicolon (f. 173r l. 18 [P_klop] ; f. 163v l. 31 [P_gai] ; f. 172v l. 8). Si le doute subsiste entre ι et ponctuation, `<unclear>`.
- **Tréma** : `ϊ`, `ϋ`, `ΐ`, `ῒ` tels qu'écrits. Il tombe souvent sur l'υ qui suit un β en « u » (ἴβϋκος, f. 164r l. 40 ; βεβϋσμένον, f. 168r l. 41, § 6, ex. 3), et ailleurs sans règle. Deux points côte à côte formés par un esprit et un accent, ou une apostrophe et un esprit, ne sont pas un tréma (f. 168v l. 14, 26).

### 2.6 Ponctuation

Un signe par signe vu, **collé au mot qui précède**, même s'il en est loin (la distance se note s'il le faut). Rien n'est converti en ponctuation moderne.

| Sur le parchemin | Écrire | Remarque |
|---|---|---|
| point, quelle que soit sa hauteur | `·` | hauteur en note si elle importe |
| point haut + virgule descendante | `;` | interrogation ou pause ; **à distinguer du dicolon** : [P_pv646] contre [P_dic645] |
| deux points égaux et superposés | `:` | dicolon, avec ou sans changement de personnage. Le caractère ⁚ proposé au chap. 5 n'est pas retenu : le « : » moderne n'existant pas dans la transcription, il n'y a pas d'ambiguïté |
| virgule sous la ligne | `,` | pause ou hypodiastole, valeur non décidée |
| tiret ou point allongé de fin de période | `—` | f. 173r l. 25 ; f. 174r l. 3, 39 ; παῖ —, f. 166r l. 27 |
| dicolon + tiret | `:—` | f. 174r l. 29 ; fin de l'hypothesis |
| trois points alignés | `···` | devant ταύτην, f. 166r l. 16 |
| trait d'union de fin de ligne | `-` | un seul : μεταβαλοῦ-, f. 171r l. 3 |

- Ponctuation d'une autre main : `<add place="ligne" main="Rrec">,</add>` (la virgule qui fait d'un point un « ; » : écrire `·` puis l'`<add>`, l'état premier reste lisible).
- Point sous un sigle ou dicolon sous un sigle : l'écrire à sa place, puis le sigle.
- Point ou dicolon présumé d'après Velsen, invisible : ne pas l'écrire ; `<note>`.
- **Traits de remplissage** (langue de l'ε, sortie de l'α, tête du σ prolongées) : ne pas les transcrire.

### 2.7 Coupe des mots : la règle des trois zones

Les chapitres 2 (« garder les blancs ») et 5 (« normalisée ») divergeaient. Mesure faite (8 124 blancs de sept pages, dans la bande du corps des lettres), la largeur des blancs est **continue** : aucun seuil naturel ne sépare blanc de mot et blanc de lettre. Or les coupes de R expliquent des leçons (ἀρ ἀπό τε ; τι στρέψεται de M). D'où une règle à trois zones, jugée sur l'image (×2) et mesurée en cas de divergence :

| Blanc | Décision |
|---|---|
| **net**, ≥ 15 px, largeur d'un ο (≈ 1,7 mm) | **garder le blanc, où qu'il tombe**, même à l'intérieur d'un mot ou à contre-sens de la coupe grammaticale : `ἐπι δημεῖ`, `ἀν ἔτι κτε`, `γεγηθὼ σ`, `οὐ κενγεταυθι`, `ἴ δω` |
| **nul** : trait continu, ou moins de 5 px | **souder**, même par-dessus une frontière de mots : `ἀλλουγὰρ`, `διατοῦτο`, `ἐπαυτὸν`, `ταύτηγ᾽`, `τοῖσχοροῖσιν` |
| **intermédiaire**, 5–14 px | coupe grammaticale ordinaire, sans note |

En cas d'hésitation, la coupe ordinaire. Les divergences d'espaces sont de dernière priorité à l'arbitrage et n'entrent pas dans le contrôle contre la référence (`comparer.py` les ignore). Une coupe qui touche une leçon se signale en `<note>`.

Signes d'union sous une coupe (virgule sous καθῆ σθαι, f. 172v l. 6 ; deux virgules sous ἐν ἱ ερῶ, f. 174r l. 6) : `<signe type="autre">`, note.

**Fin de ligne.** Le mot coupé reste coupé, une partie par `<l>`, sans trait d'union ajouté (`δρυογόνοι` / `σι`).

### 2.8 Élision, crase, apostrophe

- **Un seul caractère** : `᾽` (U+1FBD), jamais `'` ni `ʼ`.
- **Telle qu'écrite** : présente, on l'écrit, y compris après consonne finale (`ῥήτωρ᾽`) ; absente, on ne la restitue pas (`λέξουσ`, `εὐφημί ἔστω`, `ἀνίστασ`).
- **οὐκ᾽, οὐχ᾽** : apostrophe sûre seulement quand l'esprit du mot suivant se voit à part (κ᾽ οὐκ᾽ ἐκύησα, f. 170r l. 6). Une seule marque entre les deux mots : l'écrire comme esprit du mot suivant (`οὐκ οὖν`), note « apostrophe ou esprit ».
- **Crase** : ce que montre R : `κ᾽ ἀλκαῖος` (élision graphique), `κᾆτ᾽` (crochet de crase, à ne pas lire comme une brève).

### 2.9 Paragraphoi, dicola, blancs, sigles

**Bande des sigles.** Ordre fixe dans `<l>`, quel que soit le dessin : `<parag/>`, puis les `<nota>`, du plus ancien au plus récent. Le LaTeX les range dans la colonne de gauche.

| Cas | Encodage |
|---|---|
| paragraphos de T | `<parag/>` |
| paragraphos présumée sous un sigle de 1516, invisible | `<unclear cert="faible"><parag/></unclear>`, note « sec. Velsen » |
| paragraphos barrée | `<del type="biffure" main="Rrec"><parag/></del>` (main : § 1.5) |
| paragraphos grattée | `<del type="grattage" main="R?"><parag/></del>` |
| paragraphos en milieu de ligne (scène d'Écho) | `<sp n="4"/><parag/>texte d'Écho`, dans la même `<l>` |
| trait de sortie, barre de π ou de τ à gauche | rien |
| dicolon sous un sigle | `:` à sa place, puis `<nota>` |
| blanc de réplique | `<sp n="2"/>` |
| sigle de S2 | `<nota main="R2">μνη<hi rend="sus">σ</hi></nota>` |
| sigle dans la ligne, au-dessus d'un dicolon | à sa place, après le `:` |
| sigle de 1516 greffé sur une paragraphos | `<parag/><nota main="Rrec">μν</nota>` |
| sigle de S2 repassé | `<nota main="R2" repasse="Rrec">…</nota>` |
| sigle de S2 complété en 1516 | `<nota main="R2">κλει</nota><nota main="Rrec">σθενησ</nota>` |
| sigle gratté, illisible, connu de M | `<del type="grattage" main="R?"><gap n="3" unite="lettres" raison="grattage"/></del>`, note « M : κη^δ ευ^ριπ » |
| sigle de 1516 gratté plus tard (f. 163r) | idem, note « Juntine : Μν » |
| indication de jeu à la place d'un sigle | `<nota>` (ἠρέμα ὁ κηδεστ(ής)…, si elle tient lieu de sigle) ; sinon `<sch>` |

La lettre suscrite d'un sigle est `<hi rend="sus">`, non `<add>` : elle n'ajoute rien au sigle (les brouillons en `<add>` restent valides, l'arbitre uniformise). Le monogramme χ + ρ s'écrit `<hi rend="monogramme">χρ</hi>`.

Une paragraphos de T en tête du v. *n* ne prouve pas un changement en tête du v. *n* : T garde en partie l'usage antique (chap. 5, § 3.3). Un sigle de 1516 n'a aucune autorité. On transcrit, on n'interprète pas.

### 2.10 Colométrie, retraits

Le départ de la ligne se mesure au premier trait d'encre, contre l'alignement des trimètres de la même page (`retrait` = écart en px ÷ 25, arrondi à l'entier). **Négatif pour une saillie** : vers en ekthesis, bande des sigles (f. 171v vv. 785–800 ; f. 174r l. 3, 10, 30, 43 ; f. 170r l. 19–22, 26, 31). Pas de `retrait` si l'écart est inférieur à une unité. Répartition des côla : celle de R, jamais celle des éditions, même quand deux côla sont réunis (f. 173v l. 40–41 ; f. 174r l. 14, 22, 30 ; f. 170r l. 29, 31) ou quand le lyrique n'est pas renfoncé (f. 170r, 663 ss.).

### 2.11 Scholies, gloses, notes

- **Lecteur distinct.** Les lecteurs A et B ne transcrivent pas les scholies, mais ils transcrivent ce qui porte sur le texte : ajouts marginaux, corrections.
- **Élément** : `<sch n ancre place main lemme>`. `ancre` = la ligne de la colonne en face de laquelle la note **commence** ; marge supérieure : 1 ; marge inférieure : dernière ligne. `place` : `mg-g`, `mg-d` (physiques) ; `mg-sup`, `mg-inf` ; `interl` (dans l'interligne) ; `col` (dans un blanc de la colonne : χωνεύει, f. 163r l. 20 ; ff. 170v l. 2, 7 ; 173r l. 37 ; 173v l. 18 ; 174v l. 17, 20, 33 ; 175r).
- **Ordre** : par ancre, puis gauche avant droite.
- **Fins de ligne** : `<lb/>` entre deux mots, `<lb coupe="oui"/>` dans un mot (S2 coupe sans trait d'union).
- **Note coupée** entre deux marges (ff. 164r v. 131, 166v v. 339, 169v v. 624, 176v v. 1197) : deux `<sch>`, renvoi croisé en `<note>`.
- **Blocs** : S2 enchaîne les notes ; les séparer aux signes d'ouverture et de clôture, ou, à défaut, au changement de vers commenté (note).
- **Ouverture et clôture** : se transcrivent. Tiret en vedette `—`, point initial `·`, `÷`, `:—`, `~ … ~`. Le trait fin qui relie un vers à sa scholie (f. 165r, fin des l. 19, 23, 41) : `<signe type="renvoi" main="R2">—</signe>`.
- **Lemme** : attribut `lemme`, en plus du texte de la note, seulement s'il reprend bien un mot du texte. Il diffère souvent de R : ne jamais aligner l'un sur l'autre.
- **Renvois** : `<signe type="renvoi">` aux deux bouts, dans la `<l>` et dans la `<sch>`. Liste vérifiée : § 3.6.
- **Gloses** : `<sch>` avec `place` adéquat. Aucune glose interlinéaire stricte, au-dessus du mot, n'est connue dans la pièce (chap. 3, § 3.3) ; `<gl>` reste disponible si l'image en montre une.
- **Abréviations** : § 4. L'accent d'un mot abrégé se garde tel qu'il est écrit, y compris sur le signe : c'est souvent un signe de suspension.
- **Décalques, transparences** : pas de `<sch>`. Contrôle : miroir de la page opposée (§ 5.5).
- **Ce qui est illisible reste illisible** : ligne marginale ravivée du f. 162v (sous πρόσεχε, marge extérieure) : `<gap>` et note, sans restitution du v. 28. Les débuts de lignes effacés (ff. 168v, 172v, 176v) peuvent être suppléés d'après Enger, Dübner ou Rutherford **uniquement** en `<note>`.

### 2.12 Interventions

| Cas | Encodage |
|---|---|
| lettre suscrite par un correcteur | `ἐκ<add place="dessus" main="R1c">κ</add>λησίαν` |
| lettres finales surélevées par T, faute de place | `ἀγορεύ<hi rend="sus">ει</hi>` : pas une correction |
| mot en marge | `<add place="mg-d" main="R1c">μέντοι</add>` |
| biffure en écrivant | `<del type="biffure" main="R1c">τί</del>` |
| biffure et points de deux mains | `<del type="exponctuation" main="R2"><del type="biffure" main="R1c">…</del></del>` |
| exponctuation | `<del type="exponctuation" main="R?">…</del> ` |
| grattage sans récriture | `<del type="grattage" main="R?">σ</del>` si la lettre se lit encore, sinon `<gap>` à l'intérieur |
| écrit sur grattage | `<ras main="R3">…</ras>` ; grattage plus long que la récriture : `<del type="grattage"><gap …/></del>` à la suite |
| surcharge sans grattage | `<subst main="R2"><del type="surcharge">ο</del><add place="ligne">ω</add></subst>` |
| lettre refaite en écrivant | `<subst main="R1c">`, ou rien si la première lettre est illisible (note) |
| lacune laissée par T, comblée | `<add place="ligne" main="R2">βοώιη</add>` |
| lacune laissée par T, restée vide | `<sp n="…"/>` |
| signal de T | `<signe type="signal" main="R1">…</signe>` en tête ou en fin de ligne |
| signe d'insertion de 1516 | `<signe type="insertion" main="Rrec">^</signe>`, le sigle marginal en `<nota>` |
| lettres de transposition α–δ (f. 162v) | `<signe type="transposition" main="Rrec">`, note « série peut-être antérieure à M » ; γ brun : `main="R?"` |
| repère de la Juntine | `<signe type="repere" main="Rrec" instrument="mine">14</signe>`, non imprimé |

`main` de `<del>` ou de `<subst>` : l'auteur de la suppression, s'il est connu ; un grattage ne garde pas d'encre, donc `R?` par défaut. Velsen donne `R²` à beaucoup d'accents : `R?`, note « R² Velsen ». L'état premier doit rester lisible dans `<del>` chaque fois qu'il l'est sur le parchemin ; `texte_brut(l, 'ac')` le reconstitue.

### 2.13 Abréviations de T

T abrège très peu. Liste connue (chiffre minimal pour ϗ : deux pages seulement ont été balayées) :

| Abréviation | Lieu | Encodage |
|---|---|---|
| ϗ | f. 166r l. 15 ; f. 169v l. 7 ; f. 170r l. 21, 22 ; f. 171v l. 27 ; f. 172r l. 43 ; f. 174r l. 39 | `<abbr signe="ϗ" dev="καί"/>` ; accent du signe en note |
| ἀθηναί(ων) | f. 166r l. 14 (sûre) | `<abbr signe="⌒" dev="ων">ἀθηναί</abbr>` |
| διαλυμαίνετ(αι) ; διδοῦσ(αι) ; βαδίζ(ειν) | f. 166v l. 12 ; f. 169r l. 8 ; f. 177r l. 20 (probables) | `<abbr signe="~" dev="αι">διαλυμαίνετ</abbr>` |
| εἶ(ναι) ou εἶν(αι) | f. 172r l. 17 (signe en X = ν en « x » ?) | `<abbr dev="ναι">εἶ</abbr>` ou `<unclear>` ; note |
| ἀποκεκαρμέν(ην) ; ἀποδύσ(ας) | f. 172v l. 4 ; f. 170r l. 20 (possibles) | note obligatoire |
| π̅η̅ρ | f. 172v l. 27 | `<abbr signe="¯" dev="πατήρ"/>`, note « π, η, ρ écrits, trait sur η » |

Le mot se développe dans `dev`. Ne pas confondre avec ce qui n'est pas une abréviation : traits de remplissage, ligature τε à ε surélevé, γ^ε de γέρων, blanc de γρ αμματέως, circonflexe étiré de θρᾶττ᾽.

### 2.14 Doutes et lacunes

- `<unclear cert="moyenne">` : lecture probable, une seule hypothèse sérieuse. `<unclear cert="faible">` : plusieurs hypothèses, données dans une `<note>`.
- `<gap n unite="lettres" raison>` quand rien n'est lisible : compter les lettres d'après la largeur (≈ 25 px par lettre dans la colonne, ≈ 16 px dans les scholies).
- Une lettre lue seulement grâce au texte attendu est `cert="faible"`.
- Ne pas confondre `<unclear>` (image insuffisante) et `<note>` (lecture sûre, mais surprenante).

### 2.15 Notes

`<note ligne="n">`, ou `sch="n"`, en français, brèves. Y mettre : chaque divergence confirmée avec la vulgate ou un imprimé (« R a … ; Velsen 1883 : … ») ; chaque attribution qui n'est pas évidente, avec son critère ; la mesure d'encre s'il y en a une ; ce qui est présumé ; l'état matériel gênant. Coordonnées en px pour tout détail difficile. Pas de discussion philologique : elle appartient au commentaire.

---

## 3. Table des pièges de lecture

Les tableaux vont de ce que l'on croit voir à ce qu'il faut lire. Les exemples donnés avec un `[id]` ont été revus sur l'image pour ce guide. Les autres viennent des chapitres vérifiés ou, marqués « inv. », d'un inventaire : ce sont des lieux à regarder, non des lectures à recopier.

### 3.1 Lettres

| On croit voir | C'est peut-être | Critère | Exemples réels |
|---|---|---|---|
| **μ** | **ν** | μ : deux arceaux, le second en crochet ; ν : un arceau, puis une pointe montante. Les deux ont un premier jambage plongeant. Devant lettre liée, compter les arceaux. À la finale, penser d'abord ν | [n_2] νὴ et [m_2] ἐμοὶ, f. 165r l. 32 ; νὴ δία, f. 164v l. 41 ; τὸμ μυχὸμ pour τὸν μυχὸν, f. 168r l. 36 ; μόμημ pour μόνην, f. 169v l. 22 ; ἵμα pour ἵνα, f. 176r l. 28 |
| **μμ** | **νν**, **λλ** | νν : deux jambages plongeants ; λλ : deux diagonales sans arceau | [L_nn] γεννα-, f. 165r l. 12 ; ἐλιννύειν, f. 169v l. 6 ; [ll_obl] δύσκολλ᾽ ἀλλὰ, f. 177r l. 1 ; ἀλλὰ, f. 170r l. 11 |
| **λ**, trait de renvoi | **ν final** en queue | longue oblique descendante en fin de vers, sans lettre après | [n_q] εἰδότων, f. 169v l. 4 ; κοθωκιδῶν, l. 28 |
| **χ** | **ν final** en « x » | fin de mot ; comparer à un χ à longues diagonales | [n_x] πόρον, f. 171v l. 6 ; πάρεστιν, l. 42 ; πρώκτισον, f. 175v l. 41 |
| **ρ** | **ν final** | ν à jambage plongeant en fin de mot | ὁπόθερ pour ὁπόθεν, f. 168v (inv.) ; f. 163v l. 17 |
| **ω** | **π** en ϖ | barre de tête, même pâle ou absorbée par une ligature ; deux panses sous une barre | [p_varpi] πνοὰς, f. 163r l. 1 ; ὅωως pour ὅπως ; τὸ πόπανον, f. 165v l. 35 ; ἀπο- lu αὐτο-, f. 173v l. 21 |
| **ϖ** | **ω** | l'inverse existe : pas de barre propre | ῥήτωρ, f. 168v l. 22 (inv.) ; [w_1] |
| **ω** | **υν** | arceau ouvert à gauche ; contexte | [L_un] νῦν, f. 165v l. 4 ; οὖν ; ἁ νῦν lu ἀμῶ, f. 176r l. 43 |
| **οο** | **ω** réduit ; **σο** | deux petites boucles | f. 172v l. 17, 20, 37 ; εἰσορᾶν, f. 176r l. 26 |
| **κ**, **υ**, **ιι**, **ια**, **μ** | **β** en « u » | β : deux jambages ouverts en haut, d'ordinaire sans haste ; κ : haste haute. Ce n'est qu'une tendance : à défaut, le contexte | [b_u2] λαμβάνετε, f. 165v l. 1 ; [b_k] ἀσεβοῦσ᾽, f. 166v l. 31 contre [k_lu] ; βραχὺ lu ἱεραχύ, f. 173v l. 21 ; [ex4a] βάλλουσαι, f. 172r l. 5 ; ὑμρίζειν pour ὑβρίζειν, f. 168v l. 27 |
| **β fermé** | une **intervention** | T n'a que le β en « u » : un β fermé dans la colonne se signale, sans désigner son auteur | [b_corr] κύβδ᾽, f. 168r l. 24 ; βοώιη, l. 41 ; premier β de βάρβιτος, f. 164r l. 16 |
| **lc**, **ic**, **lu**, **ιε**, **ου** | **κ** en deux temps | une haste suivie d'une panse vaut κ | [k_lu] ; κροκωτοῖς lu ἱεροκωτοῖς, f. 173v l. 24 ; [L_kekopsoi] κεκό, f. 176r l. 1 ; σκεῦος, f. 167r l. 23 |
| **ζ** | **ξ** | ζ : deux lobes ronds (« 3 ») ; ξ : barre de tête plate et zigzag, longue queue. Critère sans exception connue chez T ; S2 écrit le ξ comme un ζ (§ 3.6) | [z_3] Ζεῦ, f. 172v l. 36 ; [x_4] ξένους, l. 38 ; ὀτότυζε, f. 175v l. 1 ; ἀρτομουξία, f. 176v l. 34 |
| **ζ**, **ς** | **ϗ** | S couché, à queue, parfois accentué ; un mot à lui seul | [A_kaizeta] ϗ ζητεῖν, f. 169v l. 7 ; [A_kai1] |
| **ν**, **υ** | **γ** en v plongeant | deux branches, sans arceau | [g_v] ; [P_su_ge] σύ γε lu σὺν, f. 172v l. 31 ; [P_ochl] ὀχληρά γ᾽ lu ὀχληρὰν, f. 175r l. 34 |
| **τ**, **π** | **Γ** oncial ; **γι** en Π | barre liée à la lettre suivante | [g_gi] γινώσκομεν, f. 169v l. 15, lu πνώσκομεν ou τινώσκομεν ; γλαυκόν, f. 163r l. 3 |
| **τ**, **+**, **†** | **ψ** en croix | haste haute traversée par une barre ou une courbe | [y_3] ὄψιν, f. 176r l. 29 ; ψηφίσματα, f. 166v l. 25 ; ψιλός, f. 165r l. 24 ; τρέψεται, f. 169v l. 11 |
| **ι** | **ψ** réduit | haste confondue avec un ι | ἐξέθρεψε lu ἐξέθρει χώρα, f. 168v l. 14 [P_exethr] |
| **μ**, **ρ** | **λ** | diagonale descendant à gauche, sans second arc | [l_2] ; [P_lathein] λαθεῖν lu μαθεῖν, f. 167r l. 29 ; λῆρον, f. 173r l. 4 |
| **μ** | **λ + ι** | | πολιός, f. 164v l. 25 ; ἠλιθίου, f. 165v l. 40 |
| **ο** | **σ** fermé | trait de tête qui file vers la lettre suivante | [P_skaph] σκάφιον lu οἰκάφιον, f. 169v l. 41 ; [P_su_kiss] σὺ lu οὐ, f. 174r l. 30 ; σῶσον, f. 174v l. 13 |
| **ζ** | **σ** initial | σ rond à queue horizontale | [s_init] σωστράτη, f. 166v l. 38 : **R n'a pas Ζωστράτη** |
| **σ**, **θ**, **β** | **ε** fermé ou en « 6 » | boucle haute, langue liée | φερε σε, f. 173r l. 39 ; οὐπώποτ᾽ εἶπεν, f. 168r l. 32 ; εὐριπίδου lu βυριπίδου, f. 167r l. 8 |
| **ι**, paragraphos verticale | **ι** initial long | continuité avec le mot | [i_j1] ἱκέτης, f. 164v l. 15 ; ἴβυκος, f. 164r l. 40 ; ἰδεῖν, f. 171v l. 40 |
| **κ**, **ιι** | **η** en « h » | | [h_h] ; η ᾽στί lu « καί », f. 177r l. 6 |
| **ν** | **Η** oncial, **н** étroit | barre médiane ; la barre de Ν descend | [h_H2] ; [n_N2] ; [L_demeter] δη μήτηρ, f. 170r l. 7 ; βοώιη lu βοῶν par la Juntine |
| **ι** | **υ** étroit | | δρυόχους, f. 163r l. 15 ; τοὺς, f. 166v l. 23 ; τυῖς, f. 166r l. 41 : à garder |
| **δο**, **θ** | **φ** à boucle haute | petite boucle posée sur la panse | φύλαξ, f. 174v l. 25 |
| **δ**, **ψ** | **θ** cursif ouvert | hampe vers la droite (δ : vers la gauche) ; « 4 » ouvert au f. 173v | θεσμοφορίοις, f. 164v l. 17 ; ἀποθανουμένῳ, f. 173v |
| **λ**, **δη**, **δγ** | **δ** ; **δι** | panse basse ; ι en queue du δ | μὴ δαμῶς, f. 165r l. 20 ; [L_di] διὰ, f. 167r l. 35 ; διάρριψον, f. 170r l. 30 |
| point | **ο** plein | disque de la taille d'une lettre | [o_plein] προ, f. 167v l. 2 ; προαγωγὸς, f. 166v l. 5 |
| lettre suscrite | lettre finale surélevée ; **C** montant | ligne serrée | ἀγορεύ^ει, f. 171v l. 23 ; ἐπουρίσασ, f. 177r l. 19 |

### 3.2 Ligatures et groupes

| On croit voir | C'est peut-être | Critère | Exemples réels |
|---|---|---|---|
| **α**, **ο**, **φ**, **q**, **ἢ**, **ἡ** | **ει** en « q » | boucle triangulaire, haste descendant à gauche ; sous un accent ou un esprit, penser d'abord à ει | [L_ei_q2] εἴ τις, f. 166v l. 7 ; [P_eiper] εἴπερ lu ἤπερ, f. 171v l. 27, 32 ; εῖ, f. 169v l. 11 ([ex2a]) : **R n'a pas ἡ** ; εἶδεσ, f. 177r l. 10 |
| **ξ**, **ζ**, **φ** | **ει** à ι descendant | zigzag sous la ligne | [L_ei_xi] χορομανεῖ, f. 174r l. 3 ; παίζει ; κατεῖπε, f. 166v l. 4 ; εἰσὶν, f. 174v l. 8 |
| chiffre **4** | **ει** ; **θ** ouvert | ε anguleux, ι croisé | [L_ei_4] δείξει, f. 170r l. 38 ; ποιεῖν ; φεύγεισ, f. 175v l. 12 ([ex5a]) |
| **η** | **ει** à boucle et pied | le η de T est « h », Η ou « н », jamais cette forme | [L_ei_v] φεύγεις, f. 170v l. 12 |
| **α** à crochet, **ἕ** | **ει** | | κλεισθένης, προτείνειν, ἀφείλετ᾽, f. 173v l. 10, 17, 20 |
| accent | **ι** long oblique de ει | | εἰσὶν, f. 167r l. 12 |
| **α** accentué | **στ** | boucle fermée en haut par un trait qui file vers la lettre suivante (barre du τ) ; l'α n'a qu'un court trait vertical. L'« accent » est celui de la voyelle suivante | [L_st_a2] ὥστ᾽, f. 167r l. 32 ; [L_strephei] στρέφει ; [L_nesteuomen] νηστεύωμεν lu μὴ ἀθεο μεν, f. 174r l. 26 ; οὗτοσ τί, f. 175v l. 2 ; [ex2b] τρέψεται précédé de σ, f. 169v l. 11 |
| un mot en moins | **στ** à cheval sur deux mots | le σ final du premier mot est lié au τ du second | αὐτός τε lu αὐτὸ πτε, f. 164v l. 1 ; [ex4a] τῆσ τε, f. 172r l. 5 ; διώκοισ ταυτηΐ, f. 177r l. 13 |
| **ϛ**, **q**, **δα** | autres **στ** | | ἐστιν, f. 164v l. 18 ; ᾽στί, f. 177r l. 6 ; εστιν lu δαιμ, f. 173r l. 28 |
| **τ** isolé (sans fût) | **στ**, τ réduit à sa barre | barre qui sort du σ | τρίτη στί, f. 163v l. 1 |
| **ω**, tache + **π** | **σπ** | trois panses sous la barre, contre deux pour ϖ | [L_sp2] σπογγιεῖ, f. 165r l. 39 ; σπέος, f. 164r l. 21 : **R a σπέος**, M πέος |
| lettre omise | **σχ** | σ final soudé au χ | [L_sch] τοῖσ χοροῖσιν, f. 174r l. 17 |
| **τ** + lettre | **σ** final lié au mot suivant | | [P_ti_sem] τί σ ἐμὸν lu σεμὸν, f. 175r l. 4 (d'où τὶ σεμνὸν dans M, inv.) |
| **θ** | **ετ** | boucle de l'ε au-dessus de la barre | [L_et2] ἔρχετ᾽, f. 176v l. 10 ; ἔτι, l. 35 |
| **θ**, **M** | **επ** | | ἐπ᾽ ἀναφύσα, δ᾽ ἐπὶ lu δθὶ, f. 176v l. 7, 14 |
| **ε** barré | **επ** | | ἐπειδή, f. 164r l. 24 |
| **πρι**, **πάρι** | **ερ** | ε en crochet sur le ρ | [L_peri] περὶ, f. 166r l. 14 |
| **β**, **δ** | **εγ**, **γε**, **εμ** | | ἄγε lu ἀβ ; ἐμοὶ lu βμοὶ, f. 165r ; δκυκλον, f. 165v l. 4 |
| **γ** seul | **ττ** | premier τ réduit à sa barre, second en γ, forme constante | [L_tt4] φύλαττε lu φύλαγε, f. 173v l. 13 ; πάτταλον, f. 165r l. 14 ; ἄττα, f. 167v l. 1 |
| **ψ**, **ш** | **γγ** en W | deux v liés | [L_gg2] σπογγιεῖ ; γογγυλίσας, f. 163r l. 25 |
| **χχ**, **ψ**, **μμ**, biffure | **λλ** | deux diagonales de même longueur, croisées ou parallèles | [ll_X1] πολλοὺς, f. 164v l. 13 ; [ll_obl] ; πόλλ᾽, f. 168r l. 12 ; f. 172r l. 39 |
| **ζλ** | **λλ**, premier λ recourbé | | τιλλομένην, f. 168v l. 35 |
| **ρ** ; ⊙, © | **-ος** de fin de ligne | petit ο, parfois plein, dans un grand C lunaire ou une spirale, suivi d'un point ; le mot est incomplet sans lui. Ni renvoi, ni sigle | [L_os1] τήϊος, f. 164r l. 40 ; [L_os4] γοργόνοσ, f. 175v l. 20 ; οὑκκυκλούμενος, f. 163v l. 17 ; λιγνύος, f. 165v l. 31 ; ἀπεψωλημένοσ, f. 176v l. 20 |
| **ιρο** | **ου** à υ réduit | | κουροτρόφωι, f. 166r l. 7 |
| **ἐάνη** | **τι** en « н » | | [L_ti] ἐάν τις, f. 167r l. 21 |
| **ὤιιτλρασ** | **κτει** | | [L_oktiras] ὤκτειρασ, f. 175r l. 14 |
| **ταυτὸ** | **θ** cursif lié à ο | | [P_tauth] ταῦθ᾽ ὁρᾶισ, f. 168r l. 31 |

### 3.3 Faux signes

| On croit voir | C'est peut-être | Critère | Exemples réels |
|---|---|---|---|
| **point** devant un mot | goutte d'attaque du τ ; esprit rejeté | contact avec la lettre ; 4–6 px ; la paragraphos fait 25–42 px | [tau_g] τῶν, f. 165v l. 42 ; f. 167r l. 10, 15 ; [D_spir2] ἐξεπίτηδες, f. 168v l. 38 ; f. 168r l. 20, 22, 23, 32, 37, 42 |
| **point** au-dessus | circonflexe réduit | § 2.3 | φῶς, f. 164r l. 4 ; νῦν, f. 177r l. 19 |
| **point** noir | souillure, follicule | bien plus sombre que l'encre, hors de toute lettre | f. 166v l. 4 ; f. 173v l. 39–43 |
| **virgule** | sortie du ρ ; accent de la ligne suivante | | f. 167r l. 34, 37 ; [ex3a] sous βο- |
| **dicolon** | ι adscrit en deux touches | deux touches dans l'axe d'un ι, en fin de mot en -η, -ω, -α | [P_gai] γᾶι, f. 163v l. 31 ; [P_klop] κλοπῆι, f. 173r l. 18 ; τῆι, l. 41 ; τινι·, f. 172v l. 8 |
| **dicolon** | point + esprit ou accent de la ligne suivante | vérifier que le point inférieur ne coiffe pas une lettre de la ligne inférieure | f. 164v l. 25 ; f. 169v l. 19 ; f. 171r l. 29 ; f. 172v l. 17 ; f. 177r l. 16 ; f. 170r l. 18 |
| **dicolon** | **point-virgule** | virgule à queue sous le point : deux objets inégaux | [P_pv646] f. 170r l. 11, v. 646 : point et virgule, ΔB/R −0,16, encre de T ; **le « : » de Velsen et de l'inventaire est à revoir** ; f. 164r l. 15 |
| **dicolon** | apostrophe + point | | θ᾽ :, f. 167r l. 31 |
| **dicolon** | clôture ÷ ou :– d'une scholie tombée au bord de la colonne | petit module, encre des scholies | f. 172v l. 16 ; f. 167v l. 25, 36 |
| un **point**, à tort | vrai dicolon, dont un point est faible | ne pas réduire | f. 172v l. 40 ; f. 175v l. 1 |
| **biffure** | barre de τ, π, θ, langue de ε, tête de σ, prolongées | continuité avec la lettre ; une vraie biffure est posée par-dessus, épaisse, et n'a pas d'attache | [P_euch] εὔχεσθε, f. 166r l. 4, 17, 38 ; f. 176r passim ; f. 174v l. 14, 26, 28, 31, 36 ; f. 173v l. 34–36 ; vraies biffures : f. 173v l. 15, 17, 25, 33 ; f. 172r l. 42 ; f. 175r l. 28 |
| **paragraphos** | barre de π ou de τ débordant à gauche ; tiret de S2 ; esprit | en massue, à mi-hauteur, entre le filet et le texte ; S2 ne met de tiret qu'en tête de note | f. 162v vv. 4, 22, 38 ; f. 163r l. 13, 37 ; f. 164v l. 8, 18, 37 ; f. 171r l. 13 ; f. 171v l. 6, 9 |
| absence de **paragraphos** | paragraphos soudée à une glose ; grattée | | f. 171r l. 24, 38 ; f. 176v l. 26, 33 |
| **+**, crux | paragraphos barrée ; ψ ; accent biffé ; signe de la Juntine | encre de la haste ; contexte | f. 165r l. 24 ; f. 165v l. 13, 22, 23, 26 ; f. 175v l. 11–13 ; f. 176v l. 16, 27, 28, 37 ; le × de f. 172r l. 5 ([ex4a]) ; εἰσιὼν, f. 168r l. 30 |
| **signal** √ du copiste | accent en ✓ | c'est dans la ligne, sur une voyelle ; le signal est en marge | [D_accV] καινόν, f. 174r l. 9 ; ἀεί, f. 169r l. 27 |
| **circonflexe** | accent en V | | δυσμενήσ, f. 171r l. 37 ; σύ, f. 169v l. 11 |
| **tréma** | esprit + accent | | χ ἥτις, f. 168v l. 14 |
| **tiret**, **renvoi**, **abréviation** | trait de remplissage ; fioriture | prolonge la dernière lettre | [D_fill] δεκα, f. 172v l. 43 ; ὁρᾶις, f. 168r l. 31 ; queue de πόδα, f. 170r l. 24 ; f. 173r l. 36 ; f. 174v l. 18, 24, 36 |
| **renvoi**, accolade, trait marginal | hampe démesurée | φ, ρ, ξ, χ, ι des fins de page | [r_q] σπάρτην, f. 173r l. 43 ; φορμὸν, f. 172r l. 21 ; ξ de λέξεις, f. 170v l. 43 ; ἄρα, f. 175v l. 43 |
| **chrisme**, **astérisque** | monogramme χ + ρ | sigle du chœur | f. 170r l. 19 ; f. 170v l. 22–23, 28, 38 ; f. 169v |
| **abréviation** | circonflexe étiré | | [D_circ2] θρᾶττ᾽, f. 165v l. 43 |
| texte **ajouté** | encre épuisée, puis reprise | même main, même ductus | [D_ink] οὖν δρ-, f. 176v l. 28 |
| **vers** du texte | note de S2 au bord de la colonne ; glose | petit module, semi-onciale | ·ἀεὶ γ(ὰρ), f. 163v l. 14 ; εὐρι^π ÷, f. 171v l. 12 ; χωνεύει, f. 163r l. 20 |

### 3.4 Bande des sigles

| Piège | Exemples | Règle |
|---|---|---|
| sigle de 1516 lu comme lettre du texte | ἀγ, f. 164v l. 6, 7 (« ἅπασ ἀγ ἀνάγκη ») ; εὐ intérieur lu ά, f. 165v l. 1 ; f. 162v v. 12 : εὐ orangé + mot εὖ ; μν^η collé à ἄπειμι, f. 165v l. 29 ; Ηχ + οὗτος, f. 175v l. 2 | encre et module ; relire la ligne sans le sigle |
| sigle fusionné avec la marque de T | Γϋ sur dicolon, f. 171r l. 22–28 ; f. 173v l. 16 ; f. 176v l. 26 (lu τϋ, ἵϋ) ; μ sur paragraphos, f. 163r l. 34 ; f. 165r ; ε sur dicolon, f. 163r l. 34 | séparer le brun de l'orangé, chaque marque à part |
| sigle de 1516 à forme trompeuse | εὐ lu σύ, σα, στ (f. 168r l. 1 ; f. 172v l. 41 ; f. 173r l. 28 ; f. 175v l. 21, 22, 38, 43) ; Γ en crochet lu accolade, f. 167r l. 1 ; σκ lu paragraphos ornée, f. 175v l. 9, 11 | Velsen 1871, liste de la « 2 m. » |
| Η suscrit de μν^η | à ne pas confondre avec un Η du texte, f. 164r l. 26, 38 ; f. 165v l. 9 | encre orangée |
| fin de scholie prise pour un sigle | σύντ(αξις) en « T », f. 173v l. 25 ; « …πολ- » contre μν, l. 23 ; f. 168v ; f. 174v | semi-onciale de petit module = scholie |
| sigle au bout d'une scholie | γυ^ν(η), f. 170v l. 11 ; μνη^σ, l. 15 ; γυ^ν enroulé dans la glose, f. 170r l. 13 | la scholie finit avant |
| θ barré suscrit de ΑΓΑ^θ lu ÷ ou + | f. 164v l. 38 ; f. 163v | |
| σ suscrit de μνη^σ logé dans la ligne du dessus | f. 169v l. 22–23 | |
| ʒ (δέ, -αι, S2) contre ϗ (καί, T) | | ne pas les confondre |
| Sigle de T | **il n'y en a pas** : ΜΝΗΣΙ^λο du v. 130 est de S2 (forme) | |

### 3.5 Accidents matériels

| Accident | Lieux | Règle |
|---|---|---|
| plis et rides qui imitent des traits | f. 163r l. 33–37 ; f. 163v l. 25–28 ; f. 172r l. 27–29 ; f. 176r l. 32 ; f. 176v l. 32 | vérifier en lumière normale : le pli n'a pas d'encre |
| filets de réglure à la pointe | f. 163v l. 18 ; f. 176v l. 43 | sillon sans encre |
| taches, empâtements | ω de τῶν, f. 164r l. 31 ; goutte, f. 165v l. 13 ; tache étoilée, f. 173v l. 10 ; f. 176v l. 41 | pas une lettre, pas une correction |
| réactif : lettres noircies | § 1.6 | ni autre encre, ni correction ; lire sur le canal bleu ou rouge |
| bandes d'humidité, effacements | ff. 168v, 172v, 176v (marges) ; f. 163r (sigles déjà illisibles en 1904) | `<gap>` |
| transparence, décalque | § 1.7 | miroir (§ 5.5) |
| grattage clair qui n'en est pas un | croissant clair, f. 169v l. 21–32 | les fins de vers sont de première main |

### 3.6 Scholies

| On croit voir | C'est | Exemples | Règle |
|---|---|---|---|
| **Μ** | **ΛΛ** lié ; inversement Μ lu ΛΛ | ἀπόλλων(ος) lu ἀπόμων, f. 166r l. 34 ; καλλιλεξία, f. 167r l. 4 ; διαβάλλεται, f. 172v, f. 177r l. 6 ; δημήτηρ, f. 177r l. 22 | comparer avec les Μ sûrs de la note |
| **Η** | **Ν** à diagonale presque horizontale | ναῖκας, f. 171r l. 6 ; ν suscrit, f. 165v l. 12 ; ἀνδρομέδας, f. 175r l. 21 | l'Η de S2 a souvent la barre haute |
| deux lettres | **Κ** en deux pièces | κίνησιν, f. 166r l. 31 ; σκυ^θ, f. 176v l. 43 | haste + C ouvert = κ |
| **ζ** | **ξ** de S2 | ξιφομάχαιρα, f. 176r l. 1 ; ἐσπάραξαν, f. 172v | par le sens |
| **ις**, **ἐξ**, **εἰς** | **ϗ** en « Ις » | ff. 171v, 176v, 167v, 164v, 165v | entre deux mots : καί |
| **ζ**, **ξ**, **ἢ** | **ʒ** = δέ ou -αι, ou **λ̸** = λείπει | § 4 | position ; contrôler si le premier trait est un Λ |
| **÷** | quatre signes | ÷ droit, clôture ; ·/· oblique, ἐστί ; ·//· εἰσί ; ÷ ondulé, renvoi du v. 647 ; signal de T (rare) | dans une ligne de scholie, l'oblique pointé entre deux mots vaut ἐστί ; en fin de note, clôture |
| esprit, ponctuation | **-ος** en point | ἀπόλλων(ος), f. 166r l. 34 ; εἶδ(ος), f. 163v l. 14, lu ἐκ δ(ὲ) | sur la dernière lettre d'un mot tronqué |
| ponctuation | **ι** adscrit | f. 166r l. 2, 7–9 ; φυλάξηι, κωμωδίαι, f. 174v ; ἡλίωι, f. 163r | noter tel quel, `<unclear>` |
| **renvoi** | **-ος** de T | f. 163v l. 17 : **ce folio n'a aucun renvoi** | |
| **renvoi** | **∞** de στρῶμα | f. 165v l. 10–11 | ω suscrit |
| **« γρ »** | χ^ρ | f. 167v l. 37 | Velsen, contre Allen |
| **θ barré** compendium | θ de S2 à barre débordante | στεφανοῦσθαι, f. 167r l. 1–3 | |
| **autre main** | changement d'écriture | f. 175r l. 10 ; f. 162v | une note, une main |
| lemme = texte de R | souvent non | δουροδόκης, f. 165r ; οἰνοπίπας, f. 167r ; ἰφύων, f. 173r ; πέπαικτ(αι), f. 177r | jamais d'alignement |
| note d'une autre page | décalque | f. 173r, marge ext. ; f. 177r ; f. 169v, marge sup. | § 5.5 |

**Renvois vrais** (chap. 3, § 3.6) : ∈ … ∈ (f. 164r, fin l. 5 / l. 7) ; ·϶· … ·϶· (f. 164r, fin l. 10 / marge dr. l. 19) ; ·×· … ·×· (f. 169r, interligne 15/16 / haut de la marge) ; ✕ (f. 164r, appariement probable) ; ·✓· (f. 166v) ; → (f. 171v, l. 18) ; croix du v. 168 (f. 164v) ; ÷ ondulés du v. 647 ; « —+:— » / « +: » (f. 175v, orangés). Incertains : trait sous κηφέα (f. 175r, l. 12) ; croix du f. 175r (l. 20/21) et du f. 173v (l. 7).

### 3.7 Fiches de page

À lire avant d'entamer la page, avec son inventaire (`ravennas/graphologie/folios/fXXX.md`, sections « Formes et pièges »). Chaque point est à revoir sur l'image : une fiche n'est pas une lecture à recopier. Les faits généraux des tableaux ci-dessus ne sont pas répétés.

| Page (vv.) | Disposition | Points d'attention |
|---|---|---|
| 162v (1–42) | titre, 41 vers ; 2e réglure vide ; vv. 39–42 renfoncés | ἀρ ἀπό τε (l. 2) ; προσμάθοι· μὴ (l. 25) ; ἐπι δημεῖ (l. 40) ; v. 28 dans la colonne, après le v. 30 (ordre 27, 29, 30, 28, lettres α Γ δ β en marge) ; v. 33 suppléé, marge droite, l. 34–36 ; signal au v. 4 ; « ~ » sur χωρὶς (l. 12), non résolu ; scholies en trois écritures |
| 163r (43–79) | anapestes en côla (l. 1–26) | ε absorbé par χ dans ἐχέτω (l. 1) ; λεγει sur rasure (l. 5) ; deux points de πάσΗ et de τάχα (l. 29, 30) : ι ou ponctuation, à trancher ; le « μ » de la l. 39 est une biffure de paragraphos ; pli diagonal (l. 33–37) ; κατα (l. 24) ; zone frottée à gauche : sigles déjà illisibles en 1904 |
| 163v (80–122) | lyrique renfoncé (l. 22–43) | **aucun renvoi** ; τρίτη στί (l. 1) ; ΟΝ de τήμερον contre la scholie (l. 4) ; δί᾽ και᾽ ἂν (l. 7) ; ποῖο sans ς (l. 17) ; ·ἀεὶ γ(ὰρ) = scholie (l. 14) ; ombres de plis (l. 25–28) ; deux états de ΑΓΑ^θ : brun (v. 107), orangé (vv. 101, 114) |
| 164r (123–164) | parépigraphe (l. 8), trait rouge moderne | πότνια, φῶς ; ΜΝΗΣΙ^λο = S2 ; κρο⟦τ⟧κωτῶι, ψό⟦ι⟧γον ; Β de βάρβιτος ; σπέος (l. 21) ; ἃ δεῖ ποεῖν continu (l. 29) ; τιμᾶι (l. 6) est de T ; renvois ∈, ·϶·, ✕ |
| 164v (165–208) | v. 169 suppléé en marge | sigles de 1516 dans les vers ; τοῖ(ς) παθήμασιν (l. 34, 36) : pas de σ vu ; faux dicolon (l. 25), vrais (l. 29, 34) ; κοινὴ (l. 14), la scholie glose καινῇ |
| 165r (209–251) | trimètres | signes ^ et √ de 1516 (l. 8, 14, 16) ; « + » bruns (l. 24, 26, 38) ; dicola de pause (l. 21, 24, 36) ; tirets de S2 en fin de vers (l. 19, 23, 41) ; repère « 14 » |
| 165v (252–293) | parépigraphe (l. 26) ; tulle | l. 39 : δοκεῖν biffé, τυχεῖν en marge ; l. 40 : ἄλ^λως (le λ pâle est ajouté) ; πρὸ σθάλη κον (l. 41) ; ν suscrit, l. 12 |
| 166r (294–336) | prière en prose (l. 2–16) ; aucune marque de T | ϗ (l. 15) ; trois points (l. 16) ; κόρα̅ι̅ (l. 24, à noter sans résoudre) ; παῖ — (l. 27) ; τ᾽ ὀρείπλαγκτοι (l. 33) ; τυῖς (l. 41) ; τῶι τῶν, abréviation apparente (l. 43) |
| 166v (337–379) | chant renfoncé (l. 16–35) ; aucune marque de T ; fin de cahier | huit ἢ de trois formes ; σωστράτη (l. 38) ; τοὺς (l. 23) ; traits finaux de T à la coupure b 2/b 3 (l. 27) ; ἐκεῖνον· : un seul point (l. 42) ; -εῖν oncial sur grattage (l. 34) |
| 167r (380–422) | signature « 22 » | sigle Γυνὴ τίς sur grattage (l. 1) ; καλλιλεξία γυ^ν (l. 4) ; ἀποκεκρυμμένος (l. 18) : volute, ο plein ; esprits des crases (l. 24–30) ; blancs dans οἰ νο πό τι δας |
| 167v (423–465) | chants 434–442, 459–465 | ὀλίγον de T, ω de 1516 (l. 21) ; πο suscrit (l. 11) ; σὐν- sur grattage (l. 36) ; χ^ρ, non γρ (l. 37) ; trait de mine (l. 18) |
| 168r (466–508) | transparence du f. 168v en marge sup. | ἐπιζεῖν, εῖ récrit, encre de T (l. 3) ; κιν (l. 28) ; εἰσιὼν : aigu biffé (l. 30) ; κᾆτ᾽, κᾆθ᾽ ; κύβδ᾽ (l. 24) ; βοώιη (l. 41, ex. 3) |
| 168v (509–550) | chant, tétramètres ; ἁπαξ ἁπάσας seul (l. 43) | σ finals détachés (l. 2, 30, 31) ; signes de fin de ligne venus de la ligne suivante (l. 14, 20) ; ὠόμην ; mots soudés (l. 17, 23, 26, 27, 35) |
| 169r (551–592) | tétramètres ; v. 567 sur deux lignes | points simples (l. 12–13), non dicola ; ἀχαρνικὴ (l. 13) ; Φ en ekthesis (l. 25) ; grands χ de 1516 (l. 37, 40) ; pièce ; κλει + σθενησ |
| 169v (593–635) | trimètres | **l. 11, ex. 2** ; ϗ ζητεῖν (l. 7) ; γι en Π (l. 14, 15, 22) ; ἐχθεσ, trait douteux (l. 24) ; groupe de quatre points (l. 26) ; τι δέ με τοῦτο (l. 39) ; μέντοι (l. 38) ; barres brunes (l. 16, 28) |
| 170r (636–677) | v. 647 suppléé ; ἀθρῆσαι seul (l. 23) ; ekthesis (l. 19–22, 26, 31) ; lyrique non renfoncé | **l. 11, ex. 1** ; δη μήτηρ (l. 7) ; τὸ δὶ δὴ ἔκυψε (l. 9) ; dicola de pause (l. 22, 30, 34) ; point simple au changement (l. 16) ; ἀνίστασ , ὀρθός (l. 8) ; ἅπασιν biffé (l. 34) |
| 170v (679–720) | ἄ α· (l. 11), ἔα ἔα (l. 22) centrés ; gloses dans le blanc (l. 2, 7) | ὁσια (l. 1) ; φεύγεις (l. 12) ; ἀφεῖτ᾽ et Η suscrit (l. 16) ; ἔοιχ᾽, ι pincé (l. 9) ; esprits à gauche (l. 4, 5, 9, 23, 39) |
| 171r (721–763) | fin de chant renfoncée | μεταβαλοῦ- (l. 3) ; Γϋ sur dicola (l. 22–28) ; τυνοῦτον (l. 25) ; ἴωμεν : ι long (l. 8) ; pas de dicolon au v. 741 ; τὸ biffé (v. 754) |
| 171v (764–800) | monodie ; tétramètres en saillie, six débordements | **sigles : aucun de 1516**, sauf χ^ορ repassé ; ὑ en « ϒ » ; ἐπαυτὸν (l. 6) ; δ barré (l. 16) ; ἰδεῖν, ἰδέσθαι ; lettres finales surélevées (l. 23, 24, 39) ; εὐρι^π ÷ fin de scholie (l. 12) |
| 172r (801–834) | neuf tétramètres sur deux lignes ; pnigos | **l. 5, ex. 4** ; signal devant le v. 807 (l. 12, [P_signal]) ; ποτε biffé, τινα (l. 42) ; εἶ(ναι) (l. 17) ; σαλλαβακχοῦσ, second λ exponctué (v. 805) |
| 172v (835–876) | v. 874 sur deux lignes | π̅η̅ρ (l. 27) ; ποίου : σ gratté, ι de R3 (l. 41) ; ψακάδοσ (l. 22) ; σύ γε (l. 31) ; ὡς περσεύς de 1516 (l. 37–39) ; dicolon réel (l. 40) ; groupe orangé de S2 |
| 173r (877–919) | côla renfoncés (l. 37–38) ; décalque marge ext. | ἠξώπιος (l. 5, 8) ; μν barrés par la paragraphos : non biffés (l. 34, 36) ; εστιν (l. 28) ; ε de ευ lu σ (l. 28) ; grattages d'accents |
| 173v (920–958) | l. 15 biffée ; ἱστιορράφος seul (l. 18) | barres brunes (l. 7) ; σύντ(αξις) (l. 25) ; ·//· (l. 17) ; υ de R3 (l. 22) ; θ en « 4 » ; empreintes grises (l. 26–27, 38–39) |
| 174r (959–1001) | presque tout lyrique | accents ✓ (l. 9, 13, 16 ; celui de ἁγνήν monte très haut) ; νηστεύωμεν (l. 26) ; τοῖσ χοροῖσιν (l. 17) ; ἐν ἱ ερῶ (l. 6) ; trémas ; τοξ orangé (l. 43) ; ἐνταῦτα νῦν |
| 174v (1002–1044) | monodie renfoncée (l. 14–43) | κακοδαίμω^ν (l. 5) ; σωσον/σῶσον (l. 13) ; ἐνπεπλεγμένη (l. 31) ; gloses dans la colonne (l. 17, 20, 33) ; l. 41–43 : relever chaque signe ; φ à boucle |
| 175r (1045–1081) | scène d'Écho (l. 21–43) | ἀν ἔτι κτε (l. 3) ; τί σ ἐμὸν (l. 4) ; -στρεϊα, quatre points (l. 15) ; ι détachés (l. 16–17) ; λ(είπει) (l. 10, 30) ; ἐξ ⟦ἐλέγχων⟧ (l. 28) ; barres vv. 1076, 1078 |
| 175v (1081–1126) | Écho sur deux colonnes (l. 1–16) ; vv. 1102–1103 en marge inf. | ὀτότυζε (l. 1) ; **l. 12, ex. 5** ; πα^θ^ρνον (l. 22) ; γοργόνοσ (l. 20) ; tache d'humidité : mesures trompeuses |
| 176r (1127–1168) | hymne renfoncé ; l. 17 exponctuée | barres de liaison partout : aucune biffure (l. 8–42) ; ὅπου, glose (l. 28) ; transparence du f. 176v ; ἐφ᾽ ὧι τ᾽ (l. 37) ; κομίσωμαι : (l. 41) ; ἅλσος (l. 24) |
| 176v (1169–1210) | ligne supplémentaire (l. 20) | ἔφρα^ζ^ον ; ο ο ο corrigé en σκ ὸ (v. 1191) ; paragraphoi grattées (l. 26, 33) et fausses conservées (l. 25, 32) ; ἀρτομουξία (l. 34) ; encre épuisée (l. 28) |
| 177r (1211–1231) | titre et hypothesis de l'*Assemblée* (l. 25–37) ; réglures vides | δύσκολλ᾽ (l. 1) ; ἀρταμουξία en ligne propre (l. 4, 8, 15), en deux tronçons ; βαδίζ(ειν) (l. 20) ; décalque du f. 176v ; signes remontés de la ligne suivante (l. 4, 8, 14, 16) |

### 3.8 Corrections : ce qu'il ne faut pas recopier

**Décisions entre chapitres.** Ch. 1 prévaut sur ch. 2 et 5 pour le titre : minuscule de titre, non « majuscule de distinction ». Ch. 1, § 4 prévaut sur ch. 3 pour la main de la marge intérieure : corps de 10–14 px, minuscule à lemmes égale ou plus grande. Ch. 3, § 3.6 prévaut sur ch. 5, § 1.2 : le f. 163v n'a aucun renvoi. Ch. 1, § 13 prévaut sur ch. 4 et ch. 5 pour : v. 33 (M omet tout le vers), v. 169 (repassage douteux), repère c 13 (barre de ΕΥΡΙ^Π, non repère orangé), κατα et καί (`R?`), virgule du v. 222 (brune). Le § 2.7 ci-dessus prévaut sur ch. 2, § 7.4 et ch. 5, § 6.7 pour la coupe des mots ; le § 2.2, sur le format v0 pour σ final.

**Erreurs connues des inventaires et des imprimés.**
- « ς final prolongé » (inv. f167r, f168r) : σ rond ; il n'y a pas de ς chez T.
- Κ oncial de T (inv. f165v) : il n'y en a pas, hors des titres.
- « ὀτότυξε » de Velsen (inv. f175v, répertoire critique) : faute de la couche OCR ; Velsen a ὀτότυζε R.
- β « en 6 » de διέβαλλε, ζ de βαδίζ(ειν) de forme ξ (inv. f177r) : β en « u » ; ζ en « 3 ».
- « ʒ (ἤγουν ?) » du f. 175r : λ̸ = λείπει. « ἢ ·/· » du f. 165r : δ(έ) ἐστι. « compendium en θ barré » du f. 167r : θ de S2. νοῆσαι (f. 162v, l. 26) : μνῆσαι.
- Sigma pointé « de renvoi » (inv. f163v) : finale -ος.
- Le pseudo-dicolon de ἐνγεταυθι (v. 646 ; inv. f170r ; Velsen 1883) : point-virgule de T ([P_pv646], contrôle du 1er nov.).
- « paragraphoi de milieu de ligne » des vv. 1093, 1095 (chap. 5, § 2.3) : aux l. 12–13 du f. 175v, le « + » est dans la bande des sigles, à gauche de la ligne ([ex5a]).
- Texte de référence : ce n'est pas un témoin. Le TSV contient lui-même des coquilles (πυφέσθαι, v. 4 ; Scythe en π dans des vers où R a φ, v. 1093).

---

## 4. Répertoire des abréviations des scholies

Source : chap. 3, § 4 ; † = vérifié sur l'image dans ce chapitre. Vignettes : `ch3_pl2_abreviations.jpg` (« pl. 2, n° »). Répertoire de S2 : celui de la minuscule commune, sans signe « purement tachygraphique » (sondage, non preuve). Ces signes valent pour S2 ; T n'a que ceux du § 2.13.

**Encodage.** Une **suspension** garde les lettres écrites dans l'élément et met les lettres suppléées dans `dev` ; la lettre suscrite est `<hi rend="sus">` ; le trait ou le signe de suspension, s'il a une forme propre, va dans `signe`. Un **compendium** (signe qui remplace toute la syllabe ou tout le mot) est un élément vide : `signe` + `dev`. L'accent porté par l'abréviation se garde. Quand un signe a deux valeurs, le développement est une décision : le dire en note s'il n'est pas assuré.

Valeurs d'usage pour les signes difficiles à saisir : `ʒ` (δέ, -αι), `ϗ` (καί), `·/·` (ἐστί), `·//·` (εἰσί), `˘` (ου), `¯` (trait), `⌒` (arc), `°` (ο en point ou bouclé).

| # | Signe | Forme dans R | Valeur | Encodage | Exemples | Piège |
|---|---|---|---|---|---|---|
| 1 † | ϗ | κ de S2 en deux pièces et queue : « Ις », « ιʒ » | καί | `<abbr signe="ϗ" dev="καί"/>` | f. 165v l. 27–29 ; f. 171v l. 5–12 ; f. 176v v. 1203 ; f. 177r l. 22 ; pl. 2, n° 1, 2, 16 | lu εἰς, ις, ἐξ. Une seule forme chez S2 |
| 2 | κ̀, κ pointé | κ + grave ou point | καί | `<abbr dev="αί">κ̀</abbr>` | f. 174r l. 15–17, 28 ; f. 175v l. 17–18 | ne pas lire κ(ατά) |
| 3 † | ʒ isolé | trait de tête, longue queue oblique, blancs autour ; variantes « ʒ᾽ », « ϶ », δ à crochet | δέ | `<abbr signe="ʒ" dev="δέ"/>` | f. 165v l. 4–5, 7–12 ; f. 166r l. 31 ; f. 174v (« ϶ ») ; f. 176v v. 1197 ; pl. 2, n° 3, 6 | ne pas lire ζ, ξ, ἤ |
| 4 † | ʒ attaché | même signe, lié à un τ ou θ **écrits** | -αι | `<abbr signe="ʒ" dev="αι">καλεῖτ</abbr>` | f. 165r l. 30–31, 37–38 ; f. 165v l. 26–29 ; f. 169v v. 600 ; f. 174v l. 31–32 ; pl. 2, n° 4–5 | **καλεῖτ(αι)**, non καλεῖ(ται) : dix cas contrôlés |
| 5 † | ·/· | oblique entre deux points ; réduit « /· », « ʹ/ » | ἐστί(ν) | `<abbr signe="·/·" dev="ἐστί"/>` | f. 166v l. 37–41 ; f. 165r l. 24 ; f. 171v l. 18 ; pl. 2, n° 3, 6 | se confond avec ÷ et avec le renvoi ·/· du f. 170r |
| 6 † | ·//· | deux obliques entre deux points | εἰσί(ν) | `<abbr signe="·//·" dev="εἰσί"/>` | f. 173v l. 17 ; pl. 2, n° 7 | aspect « % » |
| 7 † | λ̸ | λ dont la jambe droite se prolonge sous la ligne en crochet vers la gauche | λείπει | `<abbr signe="λ̸" dev="λείπει"/>` | f. 168r l. 20 ; f. 175r l. 10, 30 ; pl. 2, n° 8–9 | lu ʒ (ἤγουν ?) par l'inventaire. Ailleurs λεί^π(ει) (f. 162v) |
| 8 † | -ος | ο suscrit, souvent réduit à un point plein ; petit signe bouclé | -ος | `<abbr signe="°" dev="ος">ἀπόλλων</abbr>` | f. 166r l. 34 ; f. 165v l. 11 ; f. 169v (vv. 603, 616, 620) ; f. 163v l. 14 ; pl. 2, n° 14 | point pris pour un esprit ; boucle prise pour δέ |
| 9 | -ον | trait suscrit, apex, ο suscrit | -ον | `<abbr dev="ον">τραγικώτερ</abbr>` | f. 162v, marge ext. ; f. 168r ; f. 171v (v. 771) | |
| 10 † | -ου | ου suscrit, ȣ, petit arc sur τ : τ̆ | -ου ; τοῦ | `<abbr signe="˘" dev="οῦ">τ</abbr>` | f. 170r l. 6, 13 ; f. 174v ; f. 166r ; f. 175v l. 12 (ex. 5) ; pl. 2, n° 10, 14, 15 | τ̆ n'est pas un τ accentué |
| 11 | -ων | arc ou circonflexe sur la dernière lettre | -ῶν, -ων | `<abbr signe="⌒" dev="ῶν">θεσμοφοριαζουσ</abbr>` | f. 166r l. 21 ; f. 173v l. 8–9 ; f. 163r (τ(ῶν)) | pris pour l'accent |
| 12 | -ιν, -ειν | trait courbe montant | -ιν, -ειν (aussi -ην) | `<abbr signe="⌒" dev="ειν">λαμβάν</abbr>` | f. 166r l. 2 ; f. 174v l. 18–19 | même signe pour trois finales : contexte |
| 13 | -ης, -ις | petit signe en « ς » suscrit | -ης, -εις, -ις | `<abbr dev="ης">κλίν</abbr>` | f. 165v l. 10–11 ; f. 163r | idem |
| 14 | -α | lettre suscrite + point, trait | -α | `<abbr dev="α">πάντ</abbr>` | f. 165v l. 8 ; f. 171r l. 9 | |
| 15 | -μεν, -μεθα | μ surligné ; θ suscrit | | `<abbr dev="εν">παίσωμ</abbr>` ; `<abbr dev="α">ἐδεξιούμε<hi rend="sus">θ</hi></abbr>` | f. 173v ; f. 174v ; f. 169v l. 39 | |
| 16 | -αι, -ες suscrits | lettres en fin de mot | | `μόν<hi rend="sus">αι</hi>` | f. 170r l. 21–22 | pas d'abréviation : rien dans `dev` |
| 17 † | ἀν^τ, ἀν^τ τ̆ | α + ν, τ suscrit ou barre à petite haste | ἀντί ; ἀντὶ τοῦ | `<abbr dev="ὶ">ἀν<hi rend="sus">τ</hi></abbr>` | f. 162v l. 26 ; f. 170r l. 6, 13 ; f. 174v ; f. 175v l. 4, 12 ; pl. 2, n° 10 | ouvre beaucoup de gloses |
| 18 | γ᾽, γ̄ | γ + apostrophe ou trait | γάρ | `<abbr dev="άρ">γ</abbr>` | f. 164r ; f. 169v v. 616 ; f. 174r l. 15–17 | à distinguer de δ(έ) : Σ 98, f. 163v, en note |
| 19 | π^ε ; π(ερι)- | π + ε ; π suscrit | περί | `<abbr dev="ρί">π<hi rend="sus">ε</hi></abbr>` | f. 163v ; f. 164v l. 12 ; f. 177r l. 16–17 ; pl. 2, n° 16 | non ἐπ- |
| 20 | πρ^ο | π + ρ, ο suscrit | πρός, πρό | `<abbr dev="ς">πρ<hi rend="sus">ο</hi></abbr>` | f. 164r, marge inf. ; f. 171r l. 6 | |
| 21 † | φ^η | φ, parfois barré, η suscrit | φησί(ν) | `<abbr dev="σί">φ<hi rend="sus">η</hi></abbr>` | f. 169v ; f. 173v ; f. 177r l. 14 ; pl. 2, n° 11 | v. 852 : φη(σί) ou φασί |
| 22 | φ^α | φ, α suscrit | φασί(ν) | `<abbr dev="σί">φ<hi rend="sus">α</hi></abbr>` | f. 164r ; f. 172r | |
| 23 | εἶ^π | εἶ, π suscrit | εἶπεν | `<abbr dev="εν">εἶ<hi rend="sus">π</hi></abbr>` | f. 170v l. 4 | |
| 24 | σ^η | σ couché, η suscrit | σημαίνει | `<abbr dev="μαίνει">σ<hi rend="sus">η</hi></abbr>` | f. 176v l. 5–6 | |
| 25 † | γρ | Γ dont le ρ pend sous la ligne, + signe | γράφεται | `<abbr dev="άφεται">γρ</abbr>` | f. 164r l. 20 ; f. 174v l. 38–41 ; f. 175v l. 1 ; pl. 2, n° 12 | χ^ρ au f. 167v l. 37 ; v. 126 douteux |
| 26 | ἄλλ̄ ; tilde marginal | ἄλλ surligné ; tilde | ἄλλως | `<abbr signe="¯" dev="ως">ἄλλ</abbr>` | f. 166v ; f. 168r l. 41–43 ; f. 171r l. 27–31 ; f. 172r, marge sup. | |
| 27 † | σύντ | σύν + τ sur une barre | σύνταξις | `<abbr dev="αξις">σύν<hi rend="sus">τ</hi></abbr>` | f. 173v l. 25 | tombe dans la bande des sigles |
| 28 | τ^ου(το) | τ + υ + το ; τοῦ^τ | τοῦτο | `<abbr dev="ο">τοῦ<hi rend="sus">τ</hi></abbr>` | f. 164v ; f. 171r l. 26, 34, 36 ; f. 177r l. 10 ; pl. 2, n° 15 | |
| 29 | τ̀, τ surligné, τ à crochet | | τόν, τό, τήν, τάς, τῆς, τῶν | `<abbr signe="¯" dev="όν">τ</abbr>` | f. 165v l. 13 ; f. 171r l. 6 ; f. 174v ; f. 175r ; pl. 2, n° 2 | le crochet n'est pas un accent ; valeur d'après la syntaxe |
| 30 | αὐτ^ου, αὐτ̀, αὐ^τ | | αὐτοῦ, αὐτόν, αὐτῷ | `<abbr dev="όν">αὐτ̀</abbr>` | f. 165v ; f. 170v ; f. 174v ; f. 177r l. 16 | |
| 31 † | ὁδ᾽ | δ + accent de suspension | ὁδόν | `<abbr dev="όν">ὁδ᾽</abbr>` | f. 177r l. 14, 16 ; pl. 2, n° 11 | |
| 32 | suspensions simples | trait, apex, apostrophe | finale à restituer | `<abbr dev="ον">ἔλεγ</abbr>` | f. 164v l. 12 ; f. 170v (κροκωτ᾽, ἱκε᾽, θυγα᾽, ἔ᾽ = ἔξεστιν) ; f. 172r ; pl. 2, n° 16 | d'après le contexte |
| 33 † | εὐρι^π | ευρι + π suscrit à longue barre (« ΤΤ ») | Εὐριπίδης, -ου | `<abbr dev="ίδου">εὐρι<hi rend="sus">π</hi></abbr>` | ff. 163v, 164v, 171v, 172v, 175r, 177r ; pl. 2, n° 13 | |
| 34 | ἀγά^θ | θ barré suscrit | Ἀγάθων | `<abbr dev="ων">ἀγα<hi rend="sus">θ</hi></abbr>` | f. 163v l. 19–30 | lu ÷ ou + |
| 35 † | χ^ο ; χ bouclé | χ + ο ou boucle | χορός | `<abbr dev="ορός">χ<hi rend="sus">ο</hi></abbr>` | f. 164r ; f. 166r l. 19 ; f. 175v l. 9 ; f. 177r l. 9 ; pl. 2, n° 13 | ni χ isolé, ni sigle |
| 36 | noms propres | suspension, lettre suscrite | | κηδεστ(ής), μνησίλοχ(ος), σύμμαχ(ος), ἀνδρομέδ(ας), εὔπ(ολις), θουκυ^δ(ίδου) | ff. 165v, 167r, 169v, 170v, 171r, 174v, 175r | |
| 37 | surligné | lettres extrêmes sous un trait | ἄν(θρωπ)οι ; π(ατέ)ρα | `<abbr signe="¯" dev="ἄνθρωποι"/>`, note « αν, οι écrits » | f. 170v l. 4 ; f. 171v l. 9 ; f. 172v | type *nomen sacrum* |
| 38 | chiffres, lettres nommées | lettre surlignée, apex | nombre ; nom de lettre | `θ̄`, tel quel | f. 163v, marge sup. ; f. 172r, marge inf. ; f. 171v ; f. 175v l. 1 ; f. 171r v. 728 : ᾱ = alpha long | pas d'`<abbr>` |
| 39 | lettres au-dessus du mot | voyelle ou syllabe suscrite, faute de place | | `στρ<hi rend="sus">ῶ</hi>μα` ; oubli corrigé : `<add>` | f. 165v l. 10–11 ; f. 166r l. 2 ; f. 175r l. 10 ; f. 177r l. 9 | le « ∞ » n'est pas un renvoi |
| 40 | ὅτι | ὅ + τ suscrit ; « ΟΠ » | ὅτι | `<abbr dev="ι">ὅ<hi rend="sus">τ</hi></abbr>` | f. 166v l. 27 ; f. 174r l. 10 | d'ordinaire en toutes lettres |

**Développements non résolus** : γ(άρ) ou δ(έ), Σ 98 (f. 163v) ; γρ(άφοντες), v. 126 (f. 164r) ; πλ^ι, v. 232 (f. 165r) ; petit signe final de πέπαικτ(αι) (f. 177r l. 20) ; φη(σί) ou φασί, v. 852 (f. 172v). Les laisser en `<note>`, avec le développement minimal dans `dev`.

**Sigles de personnage de S2** (chap. 3, § 5 ; chap. 5, § 4.2) : μνη^σ, μνησι^λο, μ· ; κη^δ ; ευ^ρ, ευρι^π ; αγα^θ ; κλεισ^θ, κλει ; γυ^ν, γυ^ν μία, γυ^νη τίς ; χ^ο, χ^ρ, monogramme ; κη^ρ (héraut) ; σκυ^θ, τοξ^ότης ; θερά^π ; ΠΡΥΤΑΝΙϹ ; ηχω. Sigles de 1516 : Εὐ, Μν, Ἀγ, Γυ, Γϋ, Κλ, Κηδ, Σκ, Ηχ, Χο, θερ. Dans `<nota>`, la forme écrite suffit, sans `<abbr>` : `<nota main="R2">κλεισ<hi rend="sus">θ</hi></nota>`.

---

## 5. Protocole

### 5.1 Principe

Trois lecteurs indépendants (A, B, scholies), un arbitre, un vérificateur. **Personne ne confronte avant d'avoir lu.** A et B ne consultent ni le brouillon de l'autre, ni `folios/fXXX_texte.jsonl`. Le guide et l'inventaire de la page se lisent avant ; aucune édition.

Images : page pleine résolution (`dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/`) ; versions améliorées `.travail/ameliorations/fXXX/` (`clahe.jpg`, `ds_lab.jpg`, `bleu.jpg`, `encre.png`) ; planches de ligne `.travail/lignes/fXXX/` ; fac-similé de 1904 pour ff. 162v–163r (`ravennas_1904_bnf/`), utile pour ce qui s'est effacé depuis.

### 5.2 Lecture A (directe)

1. Lire ligne à ligne, sur les planches (demi-ligne ×2), sans aucun texte. Écrire chaque ligne dès qu'elle est lue.
2. Agrandir tout groupe douteux à ×3–×4, sur l'original et sur une version améliorée. Image de 1500 px de large au plus. Au-delà de ×6, le JPEG pixellise et n'apprend plus rien.
3. Une ligne d'abord pour les lettres ; puis accents, esprits, ι, apostrophes ; puis ponctuation et marques ; puis mains.

### 5.3 Lecture B (par passes)

1. Lettres, segments de 3 à 5 mots à ×3.
2. Diacritiques, mot par mot.
3. Ponctuation, sigles, paragraphoi, corrections, grattages, doutes.
4. Confrontation.

### 5.4 Confrontation : seulement après

Quand la page est lue :

```
python3 outils/transcription/comparer.py ravennas/transcription/brouillons/fXXX_A.xml ravennas/transcription/brouillons/fXXX_B.xml --ref .sources/corpus/thesmo_hall_geldart.tsv --json .travail/fXXX_cmp.json
```

Pour **chaque** divergence avec la référence, puis, pour B, avec `edition/donnees/travaux_anterieurs/texte_grec.tsv` et les leçons de R du répertoire critique (`edition/donnees/repertoire_critique/*.jsonl`, type « R ») :

1. découper le mot et ses voisins à ×4, sur l'original et sur une version améliorée ;
2. relire **lettre par lettre**, en s'aidant du § 3, sans penser au mot attendu ;
3. décider : garder ce que porte le manuscrit ; corriger si on avait mal lu ; `<unclear>` si l'image ne permet pas de décider ;
4. noter la divergence confirmée dans `<notes>`.

Une lecture qui **coïncide** avec la vulgate n'est pas vérifiée pour autant : le piège le plus dangereux est de voir ce qu'on attend. Les leçons où R diffère de la référence sont le plus souvent justes (ex. 2 : εῖ ; ex. 3 : βεβϋσμένον), mais l'inverse existe : un imprimé peut se tromper sur R (ex. 1 : « : »), et un lecteur peut s'être laissé prendre par une ligature.

### 5.5 Contrôles à fort grossissement

Devant tout **point, dicolon, trait ou croix** :
- *forme* : dicolon à deux points égaux et superposés ; paragraphos en massue, 25–42 px, à mi-hauteur ; esprit rejeté de 4–6 px ;
- *ligne* : le signe appartient-il à la ligne voisine ? Regarder s'il coiffe une lettre de la ligne inférieure, ou s'il prolonge un trait de la ligne supérieure ;
- *encre* : orangée ou grise ? Mesurer si l'objet a 100 pixels de cœur ; sinon, seule la forme compte (§ 1.3) ;
- *couches* : brun sous orangé ? Noter deux objets ;
- *témoins* : Velsen 1871 pour les sigles de 1516, M pour les notes orangées, seulement après.

Une **barre sur le mot** : vérifier qu'elle part d'une lettre. Un **pli** n'a pas d'encre : à ×3, le trait disparaît sur `encre.png`. **Décalque** : retourner en miroir la zone de la page en regard et superposer. Ne jamais transcrire ce qui se superpose.

Commandes utiles :

```
python3 outils/graphologie/encres_mesure_uniforme.py mesure f170r 775 822 1105 880
python3 -c "import sys; sys.path.insert(0,'outils/transcription'); from diploxml import *; r=lire('…'); print(valider(r)); print(avertir(r))"
```

### 5.6 Scholies

Transcription sur l'image d'abord, avec le § 4. Ensuite seulement, confrontation avec Rutherford 1896 et Dübner 1842 (lu par OCR : voir l'imprimé). Les scholies des *Thesmophories* ne sont transmises que par R : aucune erreur n'y serait rattrapée par un autre témoin. Consigner les notes absentes des éditions et leurs fausses lectures.

### 5.7 Arbitrage

Priorités, dans cet ordre : lettres ; marques de T (paragraphos, dicolon, point) ; accents et esprits ; ponctuation ; mains et types d'intervention ; coupes. Chaque divergence A/B ou divergence avec la référence se revoit sur l'image à ×4, sans préjugé pour la vulgate ni pour le lecteur « le plus plausible ». L'arbitre uniformise les encodages selon le § 2 (`hi rend="sus"` dans les `<nota>`, σ final, apostrophe `᾽`), tient son journal (`ravennas/transcription/arbitrages/fXXX.md` : ligne, vers, A, B, décision, justification, spécimen) et écrit `ravennas/transcription/fXXX.xml`. Une lecture rapportée par un éditeur et contredite s'explique : qui a raison, et pourquoi.

### 5.8 Vérification

Recontrôle sur l'image : toutes les divergences avec la référence ; huit lignes au hasard ; toutes les lignes à intervention ; tous les points de la fiche de page (§ 3.7) ; cinq scholies au hasard. Puis `valider` (zéro problème), `avertir` (chaque avertissement examiné), `python3 outils/transcription/xml_vers_latex.py fXXX`.

### 5.9 Quand s'arrêter

Une lecture indécidable sur la photographie reste `<unclear>`, avec les hypothèses en note. Elle va dans la liste des points à revoir sur l'original (lumière rasante, UV) : on ne la tranche pas par la vulgate.

---

## 6. Exemples : cinq lignes difficiles

Lignes relues le 1er novembre 2026 sur les images à ×2, ×4 et ×8 (planche `guide_pl4.jpg`, spécimens [ex1a]–[ex5c]), puis confrontées au texte de référence et à Velsen 1883. Chaque exemple donne le XML, puis ce qui a été décidé et pourquoi. Blancs mesurés dans la bande du corps des lettres.

### Exemple 1 : f. 170r, l. 11 (v. 646) — [ex1a], [ex1b], [P_pv646]

Récriture sur grattage de R3, point-virgule pris pour un dicolon, λλ pris pour μ.

```xml
<l n="11" v="646"><parag/>οὐ κενγεταυθι; ἀλλὰ δεῦρ᾽ <ras main="R3">ἥκει πάλιν</ras>·<del type="grattage" main="R?"><gap n="3" unite="lettres" raison="grattage"/></del><signe type="renvoi" main="R?">÷</signe></l>
<note ligne="11">« ; » après ἐνγεταυθι : point haut et virgule à queue, encre de T (queue ΔB/R −0,16) ; Velsen 1883 et l'inventaire ont « : ». εν- sans esprit ni accent visibles (Velsen : ἐνγεταυθι) ; le trait pâle au-dessus du γ est sans doute la queue d'une lettre de la l. 10. Blanc de 17 px entre ου et κ, κ lié à ε. ἥκει πάλιν de R3 (ΔB/R −0,44 à −0,66) ; grattage plus long que la récriture, jusqu'à x ≈ 1100. ÷ : renvoi du v. 647, dans le blanc au-dessus de la fin de ligne.</note>
```

- **Lettres.** κ en haste + panse (« lc ») ; ε à boucle haute ; ν à jambage plongeant ; γ en long V ; ἀλλὰ se lit d'abord « ἀμαδ- » : les deux λ sont deux obliques parallèles, sans arceau.
- **Diacritiques.** Dans δεῦρ᾽, deux points : circonflexe réduit et apostrophe en point, non un tréma. Esprit de οὐ en point, entre ο et υ.
- **R3.** Κ en deux traits, Α triangulaire, Π à barre, ε lunaire, mais η en « h » et ν minuscule : écriture mixte.
- **Référence** : ἐνγεταυθί. | μἀλλὰ. La conjecture de Bentley n'a rien à faire ici : R a ἀλλὰ.

### Exemple 2 : f. 169v, l. 11 (v. 603) — [ex2a], [ex2b]

Ligature ει lue ἡ, sigles de S2 à deux étages, accent en V, σ lié au mot suivant.

```xml
<l n="11" v="603"><parag/><nota main="R2">κλεισ<hi rend="sus">θ</hi></nota>φέρ᾽ ἴ δω τί σ εῖ πρώτη σ<subst main="R?"><del type="surcharge">ὺ</del><add place="ligne">ύ</add></subst>:<nota main="R2">κη<hi rend="sus">δ</hi></nota> ποῖ τ<unclear cert="moyenne">ί</unclear>στρέψεται·</l>
<note ligne="11">εῖ : ligature ει en « q », surmontée d'un seul signe (circonflexe triangulaire) ; R n'a pas l'article ἡ de la vulgate (Velsen 1883 : εῖ R). σύ : accent en ✓ soudé, trait court et délié montant (corr. ex σὺ, Velsen) ; main indécise. κη^δ de S2 dans l'interligne, au-dessus du dicolon de T ; le κλεισ^θ de la bande a le θ barré. τίσ τρέψεται : le σ final est lié au τ par la ligature στ en « α », à 8 px seulement de l'ι ; M a τι στρέψεται (Velsen), mélecture de ce groupe ; on lit aussi « τι ἀρε- ». Accent de τί peu distinct de la haste de l'ι.</note>
```

- **Lettres.** Sans le § 3.2, on lit τι + α + ρ, ou ἡ pour εῖ. ψ en croix : la haste traverse une longue barre qui court sur -εται.
- **Coupes.** Blancs de 21 px (ἴ | δω) et de 18 et 16 px (τί | σ | εῖ) : gardés. 8 px entre ι et σ : zone intermédiaire ; σ et τ liés : soudés.
- **Ordre.** `<parag/>`, puis le sigle : κλεισ^θ est à gauche du trait, sans le recouvrir. Le dicolon reste dans la ligne, le sigle suit.
- **Référence** : τίς ἡ πρώτη σύ; | ποῖ τις τρέψεται; Ponctuation entièrement moderne : on écrit `·` en fin de ligne.

### Exemple 3 : f. 168r, l. 41 (v. 506) — [ex3a], [ex3b]

Lacune de T comblée par un autre module, β fermé, tréma inattendu.

```xml
<l n="41" v="506">ἵνα μή <add place="ligne" main="R2">βοώιη·</add> κηρίωι βεβϋσμένον</l>
<note ligne="41">Lacune laissée par T, comblée en petit module (Velsen 1883 : omisit lacuna relicta R, supplevit R²). β fermé, Η oncial : la Juntine a lu βοῶν. L'encre de βοώιη ne se distingue pas de celle de T (chap. 2) : l'attribution repose sur la forme et sur la littérature. βεβϋσμένον : deux points égaux au-dessus de l'υ, non relevés jusqu'ici ; comparer ἴβϋκος, f. 164r l. 40 : υ après β en « u ». La virgule sous βο- appartient à la l. 42.</note>
```

- **Lettres.** βεβϋσμένον a deux β en « u », lus ιι ; σμ et ν finaux à jambage plongeant. ω de βοώιη en « ∞ » serré, à ne pas lire φ.
- **ι adscrits** : βοώιη, κηρίωι. Ils ne se déduisent pas : ils se voient.
- **Coupes.** Blancs irréguliers dans ἵνα μή, ligne espacée : hésitation, donc coupe ordinaire (§ 2.7).
- **Référence** : le TSV a « βό η » (sic), κηρίῳ βεβυσμένον ; Velsen imprime βοῴη. R a μή, le Η, deux ι adscrits et le tréma.

### Exemple 4 : f. 172r, l. 5 (v. 803) — [ex4a], [ex4b]

Accent annulé par 1516, β lu ια, στ à cheval sur deux mots.

```xml
<l n="5" v="803">παρ<subst main="Rrec"><del type="biffure">ὰ</del><add place="ligne">α</add></subst>βάλλουσαι τῆστεγυναικὸσ· καὶ τἀνδρὸσ</l>
<note ligne="5">Petit × au-dessus de ρ|α (x 278–298, y 540–559) : grave de T barré d'un trait orangé ; il fait lire παραβάλλουσαι (Velsen : παρὰ βάλλουσαι R). Pas de blanc entre α et β : la coupe de R n'est pas celle de son accent. τῆσ τε : blanc de 6 px devant σ, στ en « α », ε lié au γ. Point bas après γυναικὸσ, sous la fin du trait du σ. Trait de remplissage après τἀνδρὸσ, non transcrit. Fin du vers à la l. 6.</note>
```

- **Lettres.** β en « u », deux jambages sans haste : on lit « αιιαλλο ». Aigu de βάλλ- déporté au-dessus des λ. υ de -ουσαι étroit comme un ι.
- **Faux signes.** Le × n'est pas un signe critique : c'est un accent barré.
- **Référence** : παραβάλλουσαι τῆς τε γυναικὸς καὶ τἀνδρὸς τοὔνομʼ ἑκάστου. Lettres d'accord pour cette partie du vers ; la fin (τοὔνομ᾽ ἑκάστου) est à la l. 6.

### Exemple 5 : f. 175v, l. 12 (vv. 1093–1094) et sa glose — [ex5a], [ex5b], [ex5c]

Paragraphos barrée, ει en « 4 », coupe à interpréter ; scholie avec abréviations et surcharge.

```xml
<l n="12" v="1093,1094"><del type="biffure" main="Rrec"><parag/></del>ποῖ ποῖ φεύγεισ οὐ κ᾽αἰρήσεισ·</l>
<sch n="9" ancre="12" place="mg-d" main="R2"><abbr dev="ὶ">ἀν<hi rend="sus">τ</hi></abbr> <abbr signe="˘" dev="οῦ">τ</abbr> οὐ <subst main="R2"><del type="surcharge"><gap n="2" unite="lettres" raison="surcharge"/></del><add place="ligne" main="R2">χα</add></subst>ιρήσεισ ÷</sch>
<note ligne="12">« + » : paragraphos de T barrée d'une haste orangée (Rrec). Blanc de 17 px entre οὐ et κ ; κ lié à α. Au-dessus de κα-, deux marques : à x ≈ 1232, tache ronde (apostrophe de οὐκ᾽ ?) ; à x ≈ 1254, tiret oblique (esprit de αἰ- ?). D'où οὐκ᾽ αἰρήσεις de Velsen ; S2 a compris οὐ καιρήσεις, c'est-à-dire οὐ χαιρήσεις. L'écho des vv. 1093b et 1094b manque. Point bas après -εισ ; le long trait au-dessus est la queue d'une lettre de la l. 11.</note>
<note sch="9">χα nettement plus sombre et plus épais que le reste : surcharge probable (κα ?). Esprit de οὐ en équerre, de S2.</note>
```

- **Lettres.** φ et non π : R ne prête pas ici au Scythe la graphie en π du texte de référence (πεύγεις). ει en « 4 ». σ final rond à longue tête.
- **Numéro.** Le `n` de `<sch>` suit l'ordre de la page : 9 n'est qu'un exemple.
- **Glose.** ΑΝ surmonté d'une barre à petite haste : τ suscrit. Τ surmonté d'une barre et d'un petit arc : τ(οῦ). Elle commence à droite du vers, dans la marge : `mg-d`.
- **Référence** : ποῖ ποῖ πεύγεις; οὐ καιρήσεις; Velsen donne φεύγεις pour R : vu.

---

## Annexe : caractères

| Objet | Caractère | Code |
|---|---|---|
| point (toutes hauteurs) | · | U+00B7 (U+0387 se normalise en U+00B7) |
| point-virgule | ; | U+003B (U+037E se normalise en U+003B) |
| dicolon | : | U+003A |
| virgule basse | , | U+002C |
| tiret | — | U+2014 |
| obèle pointé | ÷ | U+00F7 |
| apostrophe | ᾽ | U+1FBD |
| esprits et accents | précomposés | NFC ; l'aigu de `ά` est U+03AC |
| ϗ, dans `signe` | ϗ | U+03D7 |
| ʒ, dans `signe` | ʒ | U+0292 |
| trait, arc, ου, ο en point, dans `signe` | ¯ ⌒ ˘ ° | U+00AF, U+2312, U+02D8, U+00B0 |

Le XML est en UTF-8. Ne jamais employer d'entités, de capitales grecques, de `ς` (§ 2.2) ni de lettres latines d'aspect voisin (ο latin, ν latin) : le comparateur les prendrait pour des divergences.

## Points laissés ouverts

Ils ne se tranchent pas à la transcription. Les signaler en note, et les reporter dans la liste à contrôler sur l'original : nature de R3 ; repassage de 1516 (aucun tracé brun n'a été vu sous l'orangé) ; main de la marge intérieure ; vers suppléés 33 et 169 ; ligne ravivée du f. 162v (v. 28 ?) ; 51 corrections attestées par Velsen seul ; main des accents en V ; signaux du copiste (vv. 4, 807, 1135, 1176) ; petits signes inexpliqués (« ~ » du v. 11, trois points du f. 166r l. 16, deux virgules du f. 174r l. 6, paires « // » du f. 170r). Questions complètes : chap. 1, § 12 ; chap. 3, § 10 ; chap. 4, § 8 ; chap. 5, § 8.
