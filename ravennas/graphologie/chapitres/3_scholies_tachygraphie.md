# Chapitre 3 — Scholies et gloses : mains, disposition, tachygraphie

*Étude graphologique de R (Ravenne, Biblioteca Classense, ms. 429, olim 137, 4, A), Thesmophories, ff. 162v–177r.*

> **État** : chapitre rédigé le 28 oct. 2026 (sections 0 à 10). Les lectures citées et les points marqués [à vérifier] restent à contrôler sur l'original.
>
> **Sources.** (1) Les 30 inventaires de page (`ravennas/graphologie/folios/fXXX.md` et `fXXX.jsonl`) : 267 observations « scholie », 107 « glose », 46 « signal », et les observations « sigle », « forme » et « piège » qui touchent la main des scholies ; le résumé `ravennas/graphologie/resume_pages.json`. (2) Mes contrôles sur les images à pleine résolution (`dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/`), avec mes propres découpes et mesures d'encre (`.travail/chap3/`, non versionné) ; le fac-similé de 1904 pour le f. 162v (`ravennas_1904_bnf/`) ; le PDF intégral du manuscrit pour une comparaison avec le f. 14r (`ravennas_1904_bnf/Ravennas_MS429_INTEGRAL_11_Comedies_Tome1_planches_001-100.pdf`). (3) La littérature réunie dans `recherche/ravennas_dossier.md` et `recherche/scholies.md`, et les sources elles-mêmes, lues dans `.sources/` : Martin 1882 (préface, pp. xiv–xix, et collation des *Thesm.*, pp. 196–209), Zacher 1888 (pp. 534–538), Rutherford 1896 (I, pp. xxvii–xxix), Allen 1896 et Orsini 2011 (cités d'après le dossier).
>
> **Conventions.** « l. » = ligne de la colonne de texte de la page ; « v. » = vers (numérotation du texte de l'auteur de l'édition) ; coordonnées en pixels de l'image de la page (1 px ≈ 0,12 mm). Marges : sur un recto, la marge extérieure (« ext. ») est à droite et l'intérieure (« int. ») à gauche ; sur un verso, c'est l'inverse. « inv. fXXX » renvoie à l'inventaire de la page ; « vérifié » signale un point que j'ai contrôlé moi-même sur l'image ; les affirmations des auteurs sont suivies de leur référence. Dans les transcriptions, « ^ » note une lettre suscrite, les parenthèses le développement d'une abréviation. **T** = copiste du texte ; **S2** = main des scholies (« B » d'Allen, « schol. m. » de Velsen 1871, R² de Velsen 1883 et de Martin 1882) ; **main de 1516** = la main qui prépare la copie d'impression de la Juntine (« 2 m. » de Velsen 1871, attribuée à Euphrosynus Boninus).
>
> **Illustrations.** Quatre planches, générées par `outils/graphologie/planches_chap3.py` à partir des images de page : `../planches/ch3_pl1_ecritures.jpg`, `../planches/ch3_pl2_abreviations.jpg`, `../planches/ch3_pl3_renvois.jpg`, `../planches/ch3_pl4_pieges.jpg`. Les spécimens des inventaires (`../specimens/fXXX/…`) sont cités par leur chemin ; ce dossier est ignoré par git et se régénère à partir des boîtes des `.jsonl`.
>
> **Chapitres voisins.** Le classement général des mains et des encres est au chapitre 1 (`1_mains_encres.md`) ; l'écriture et les abréviations de T au chapitre 2 (`2_ecriture_copiste.md`) ; les corrections au chapitre 4 (`4_interventions.md`) ; le système des *notae personarum* au chapitre 5 (`5_mise_en_page_signes.md`). Ce chapitre-ci ne traite des sigles de personnages que pour ce qu'ils disent de l'écriture de S2 (§ 5).

## Conclusions principales

1. **Une main pour l'essentiel.** Près de quatre cents notes (scholies, gloses, indications de jeu) sont toutes de S2, sauf deux scholies en minuscule de la marge intérieure du f. 162v (§ 2.4). S2 écrit trois registres : une semi-onciale inclinée pour les scholies ; de petites majuscules plus droites pour les gloses ; une minuscule pour les vers suppléés, pour quelques gloses et, au f. 162v seulement, pour toute une série de scholies.
2. **Le f. 162v.** La minuscule de la marge supérieure et de la marge extérieure est bien celle de S2, comme le pensait Allen : elle porte des lemmes en semi-onciale, et S2 mêle de même les deux écritures dans le supplément des vv. 1102–1103 (f. 175v). La minuscule ronde et droite de la marge intérieure (scholies aux vv. 27 et 30–32) est autre chose. Elle a l'alphabet de T, et l'encre de T pour la note du v. 27. C'est la « troisième main » d'Orsini. Un premier essai de comparaison la rapproche de la minuscule détachée des restitutions marginales du *Ploutos* (f. 14r), que Martin donne au copiste et Orsini au premier scholiaste ; rien n'est démontré à ce stade.
3. **Disposition.** S2 n'emploie que rarement l'espace réglé des marges supérieure et inférieure. Il écrit chaque note au droit de son vers, après le texte et après les paragraphoi de T, qu'il contourne. Il ouvre souvent la note par un tiret en vedette et la ferme par ÷ (ou « :– »). Les lemmes ne sont réguliers qu'au f. 162v ; ailleurs ils sont sporadiques et ne se distinguent pas du reste de la note.
4. **Renvois.** S2 en emploie, contrairement à ce que disent Zacher et Orsini, mais seulement quand une note est loin de son vers ou coupée entre deux marges : ∈, ·϶· et ✕ au f. 164r, ·×· au f. 169r, un trait et ·✓· au f. 166v, auxquels s'ajoutent les signes des vers suppléés (ff. 164v, 170r, 175v). Le « sigma pointé » que l'inventaire du f. 163v prenait pour un renvoi est en réalité la finale -ος de T : un grand sigma lunaire qui enferme un ο, comme au f. 164r, l. 40 (§ 3.6, vérifié).
5. **Répertoire tachygraphique.** S2 se sert des compendia ordinaires de la minuscule, dont plusieurs sont d'origine tachygraphique. Le répertoire, établi au § 4 avec 40 entrées, comprend : ϗ = καί, que S2 trace comme son κ en deux pièces muni d'une queue (« Ις », « ιʒ ») ; « ʒ » = δέ quand le signe est isolé, -αι ou -ται quand il est attaché à la lettre précédente ; ·/· = ἐστί ; ·//· = εἰσί ; λ̸ = λείπει ; ἀν^τ τ̆ = ἀντὶ τοῦ ; φ^η = φησί ; γρ = γράφεται ; σ^η = σημαίνει ; σύν + τ sur barre = σύνταξις ; ἄλλ̄ ou tilde marginal = ἄλλως ; ο suscrit réduit à un point pour -ος ; trait montant pour -ιν ou -ειν, etc. Je n'ai relevé dans les *Thesm.* aucun des signes « purement tachygraphiques » que Martin signale chez le premier scholiaste des *Oiseaux* et de la *Paix*.
6. **Corrections des inventaires** (§ 8), vérifiées sur l'image. Au f. 175r, le signe initial lu « ʒ (ἤγουν ?) » est λ(είπει), comme le lisent Martin et Rutherford. Au f. 165r (v. 231), le « ἢ ·/· » non résolu se lit δ(έ) ἐστι. Au f. 167r, le « compendium en θ barré » n'est que le θ de S2, à barre débordante. Au f. 176r, la glose ὅπου est en semi-onciale de S2, et non « de la main du texte » comme l'écrit Martin. Les gloses du f. 171r sont en petites majuscules, non en minuscule. Au f. 162v, la ligne effacée puis « ravivée » au réactif bleu, sous πρόσεχε, dans la marge extérieure, existe bien : Martin, et sans doute Allen, y voyaient le v. 28. On ne peut donc pas dire qu'il n'y a « aucune copie marginale » du v. 28.
7. **Encres.** Le plus souvent, l'encre de S2 ne se distingue pas de celle de T. Quelques campagnes distinctes se laissent pourtant isoler. Au f. 168r, les gloses de la marge intérieure ont l'encre de T. Des notes de personnage de la forme de S2 sont à l'encre orangée : je mesure au f. 174r τοξ(ότης) à A_G/A_R 1,60, A_B/A_R 3,09, contre 1,37 et 2,50 pour la scholie voisine. Au f. 175v, l'écart ne prouve rien dans la tache d'humidité, où les scholies brunes de S2 mesurent aussi « orangé » (§ 2.6).

## 0. Objet, sources et méthode

**Objet.** Les scholies des *Thesmophories* ne sont transmises que par R (Dindorf, préface reproduite par Dübner 1842, II–III ; voir `recherche/scholies.md`, § 2.1). Leur transcription diplomatique se fait donc tout entière sur ce manuscrit, sans contrôle par un autre témoin. Ce chapitre réunit ce qu'il faut savoir pour les lire sans erreur : qui les a écrites, où et comment elles sont placées, quelles abréviations et quels signes elles emploient, et quels pièges de lecture leur sont propres.

**Démarche.** J'ai lu les synthèses de page (section « Scholies et gloses » de chaque `fXXX.md`) et toutes les observations des `.jsonl` qui concernent les notes marginales ou la main S2 ; le relevé brut est dans `.travail/chap3/obs_scholies.tsv` et `.travail/chap3/abrev_brut.txt`. J'ai ensuite contrôlé sur l'image les points décisifs : les écritures du f. 162v, les signes ambigus, les renvois et les cas où les inventaires restaient indécis. J'ai repris les découpes (PIL, `crop` puis agrandissement LANCZOS ×2 à ×5) et les mesures d'encre. Pour ces mesures (`.travail/chap3/encre.py`), j'ai calculé les absorbances relatives au fond local de la zone, A_c = log₁₀(fond_c / pixel_c), sur les pixels d'encre (A_R > 0,10), puis les rapports A_G/A_R et A_B/A_R sur le cœur des traits (les 40 % de pixels d'encre les plus absorbants). Ces valeurs ne se comparent qu'à l'intérieur d'une même page et d'une même zone : une tache d'humidité, un fond jauni ou un trait trop fin les déplacent (§ 6, n° 16).

**Limites.** La photographie ne permet pas de voir les grattages légers, l'ordre des tracés ni la superposition de deux encres de teinte voisine. Il faudrait pour cela une lumière rasante, des UV ou une imagerie multispectrale. Les lectures de scholies citées ici servent seulement à identifier les signes ; elles ne remplacent pas une édition, et elles ont été confrontées à Martin 1882, Rutherford 1896 et Dübner 1842 (lu par OCR, donc à vérifier sur l'imprimé).

## 1. Le corpus des notes marginales

### 1.1 Volume et nature

Les inventaires comptent 374 observations « scholie » ou « glose », dont certaines regroupent plusieurs notes. Au total, il y a de 400 à 425 notes, inégalement réparties : de 4 notes au f. 176r à 24 au f. 164r. La pièce est la plus annotée des trois dernières du manuscrit (Zacher 1888, 538, à propos des *Guêpes*, des *Thesm.* et de l'*Assemblée*). Les notes se rangent en cinq types :

- **scholies** proprement dites : explication, histoire, citation, comme celle de Didyme et d'Aristophane de Byzance au v. 162 (f. 164r, marge inf.) ou celle d'Agathon aux vv. 30–32 ;
- **gloses**, équivalents d'un ou deux mots (ζωνάριον pour στρόφιον, f. 164r, l. 18 ; ὦ μέθυσοι, f. 171r, l. 15) ;
- **notes sur le texte** : γρ(άφεται) σύ τ' αὐτό(ς) (f. 164r, l. 20, v. 141) ; γρ(άφεται) κ(αὶ) φῶτα ἀντομένα (f. 174v, v. 1040) ; χωρ(ὶς) τ(οῦ) ε γρ(άφεται) (f. 175v, l. 1, v. 1083) ; πέπαικτ(αι) en face de πέπυσται (f. 177r, l. 20) ;
- **indications de jeu et de personnage** rédigées en mots, qui se distinguent mal des sigles (Rutherford 1896, I, vi n. 2) : πρὸ(ς) τ(ὰς) γυναῖκας (f. 171r, l. 6, v. 726) ; ἄλλη γυ(νή) (f. 171r, l. 40, v. 760) ; τοῦτο ὁ χ(ορὸς) ἢ ὁ γέρων (f. 175v, l. 9, v. 1090) ; ἠρέμα ὁ κηδεστ(ής) πρὸς τ(ὸν) εὐρι(πίδην) (f. 175r, l. 19) ; τοῦ προλόγου ἀνδρομέδας εἰσβολή (f. 175r, l. 21) ;
- **notices** du haut du f. 162v : « … καὶ τοῦτο τὸ δρᾶμα τῶν κατ' Εὐριπίδου πεποιημένων… » et « προλογίζ(ει) μνησίλοχ(ος) κηδεστὴς εὐριπίδου ».

Les vers que S2 supplée en marge (vv. 33, 169, 647, 1102–1103) ne sont pas des scholies, mais je décris leur écriture au § 2.3, parce que c'est le meilleur témoin de la minuscule de S2.

### 1.2 Tableau par page

Lecture du tableau : « ext. », « int. », « sup. », « inf. » = marges ; « col. » = notes écrites dans la colonne ou dans l'interligne. Le nombre de notes est celui des synthèses de page et reste approximatif là où des notes s'enchaînent. Pour l'ouverture et la clôture, voir le § 3.4 ; pour les renvois, le § 3.6.

| Page (vers) | Marges | Notes | Ouverture / clôture | Lemmes | Renvois et particularités |
|---|---|---|---|---|---|
| 162v (1–42) | sup., ext., int., inf. | ≈ 12 | ÷ | **oui, réguliers** (souvent en semi-onciale) | trois écritures (§ 2.4) ; ligne ravivée au réactif sous πρόσεχε (§ 8) ; aucun renvoi |
| 163r (43–79) | ext., int., col. | 19 | point simple | non | χωνεύει écrit dans la ligne du v. 57a |
| 163v (80–122) | sup. (6 l.), int., ext., inf. | 15 | point, ÷ | Σ 80 (ἐπεὶ τρίτη ᾽στί) | numéraux ια΄, ιβ΄ ; le « renvoi » de la l. 17 est la finale -ος de T (§ 3.6) |
| 164r (123–164) | sup. (3 l.), ext., int., inf. (8 l.) | 24 | ÷ | ἄρσενι·, Γενετυλλίδες·, λυκουργίας·, ὀλολύζει· | **trois renvois** ∈, ·϶·, ✕ ; scholie coupée entre deux marges (v. 131) |
| 164v (165–208) | sup. (2 l.), ext., int. | 11 | ÷ | non | croix pour le v. 169 suppléé |
| 165r (209–251) | ext. (11), int. (1) | 12 | point, tiret ou trait tiré depuis la fin du vers / « :– » | non | traînées de réactif sur les fins de ligne |
| 165v (252–293) | ext. (12), int. (7), interligne | 20 | tiret / ÷ | non | glose ὁ μνησίλοχ(ος) dans l'interligne |
| 166r (294–336) | int. (5), ext. (6) | 12 | un tiret / ÷ | δαίμων (?) | 1re ligne de la scholie au v. 329 d'une encre grise |
| 166v (337–379) | ext., int. | 15 | ÷ | non | scholie au v. 339 répartie sur les deux marges, avec un trait de renvoi ; ·✓· |
| 167r (380–422) | ext., int. | ≈ 17 | « – » / ÷ | non | lemme οἰνοπίπας ≠ texte οἰνοπότιδας |
| 167v (423–465) | sup. (2 l.), ext., int. | 16 | « – » / « :– » | non | gloses intérieures d'encre intermédiaire |
| 168r (466–508) | ext. (12), int. (3) | 15 | tiret / ÷ | non | gloses intérieures à l'encre de T |
| 168v (509–550) | sup. (1 l.), int., ext. | 10 | ÷ | non | débuts emportés par une bande effacée |
| 169r (551–592) | ext., int. | ≈ 17 | tiret / ÷ | non | **renvoi ·×·** ; même glose écrite deux fois (vv. 562, 564) ; doublet partiel (v. 585) |
| 169v (593–635) | ext., int. | 13 | tiret / ÷ | non | mots coupés sans trait d'union ; S2 raccourcit ses lignes devant les paragraphoi de T |
| 170r (636–678) | ext., int. | ≈ 10 | tiret / ÷ ou « :- » | non | signes ÷ ondulés pour le v. 647 suppléé |
| 170v (679–720) | ext., int., col. | ≈ 13 | point ou tiret / ÷ | non | scholie au v. 717 qui commente le v. 693, sans renvoi ; gloses dans le blanc des lignes lyriques |
| 171r (721–763) | ext., int. | ≈ 17 | tiret / ÷ | ἀπὸ ἔθους (?) | indications de scène ; rature dans la scholie au v. 758 |
| 171v (764–800) | ext., int. | 12 | tiret / ÷ | non | fin de scholie « …εὐρι^π ÷ » contre la colonne (§ 6, n° 10) ; flèche (?) |
| 172r (801–834) | sup. (3 l. ½), ext., int., inf. (2 l.) | ≈ 13 | tiret / ÷ | ναυσιμάχης μέν·, κλεοφῶν·, ~ τάλαντα ~ | tilde marginal pour ἄλλ(ως) ; points « • » devant les explications |
| 172v (835–876) | ext. (15), int. (2) | 17 | un tiret / « :– » | αἰκάλλει (glose) | débuts effacés par l'humidité |
| 173r (877–919) | ext., int. | 11 | tiret / ÷ | non | gloses dans le blanc des côla renfoncés ; décalque du f. 172v |
| 173v (920–958) | ext., int., col. | 15 | tiret / ÷ | ἡ σπάρτ(ος) | scholie dans le blanc de la colonne (l. 18) |
| 174r (959–1001) | int. (3), ext. (5) | 8 | tiret / ÷ | non | — |
| 174v (1002–1044) | ext. (12), int. (5), col. (3) | 21 | ÷, une fois un trait ondulé | [π]ορμὸς | correction ἐνέ → ἀμφέ en écrivant |
| 175r (1045–1081) | int., ext., col. | 16 | tiret / ÷ | non | gloses à droite des vers ; λ(είπει) |
| 175v (1081–1126) | ext. (11), int. (6), inf. | 17 | tiret / ÷ | non | vv. 1102–1103 suppléés, renvoi « +: » |
| 176r (1127–1168) | ext., int. | 4 | ÷ | non | aucune abréviation |
| 176v (1169–1210) | ext., int. | 16 | ÷ | non | scholie au v. 1197 commencée dans la marge intérieure et poursuivie dans l'extérieure |
| 177r (1211–1231) | int. (3), ext. (6) | 9 | ÷ | non | décalque du f. 176v dans la marge extérieure |

## 2. Les mains

### 2.1 La semi-onciale de S2 (scholies)

**Description.** Les inventaires concordent, et je l'ai vérifié sur les ff. 162v, 165r, 165v, 166v, 169r, 171v, 173v, 174v et 177r (planche 1, g et h ; planche 2). C'est une majuscule inclinée à droite, aux lettres disjointes, courtes et carrées. Le module varie de 10 à 16 px, soit 1,2 à 2 mm : 10–12 px aux ff. 163v et 166r, 1,6–1,9 mm au f. 164r, environ 2 mm aux ff. 168r et 177r. Au f. 174v, l'écriture est plus droite et plus grande, 18–20 px (planche 1, h). Les formes caractéristiques sont les suivantes :

- ε et σ lunaires ;
- Μ, Ν, Η, Λ, Κ onciales ;
- Κ en deux pièces, une haste et un C (aspect « Ις » ou « ιc ») ;
- Υ en Y, Δ à base débordante ;
- ξ en Z à queue (proche du ζ) ;
- θ ovale à barre débordant des deux côtés (au f. 167r, l. 1–3, planche 4, n° 6) ;
- esprits anguleux, l'esprit rude en « ͱ » (f. 172r, l. 34) ;
- accents posés sur les majuscules, compendia accentués.

Cela correspond aux descriptions publiées : « maiuscola ad asse inclinato a destra, con altezza delle lettere mediamente di mm 1,7 », au « disegno … angoloso e spezzato » (Orsini 2011, 327) ; « coarser and thicker … the letters are short, square, without tails » (Allen 1896, 320) ; scribe qui « commonly accents the compendia of accented syllables » (Rutherford 1896, I, xxvii).

**Ductus.** La mise en page est relâchée : les lignes ne suivent pas la réglure (inv. f165v), les mots sont coupés en fin de ligne sans trait d'union (inv. f169v : χρῶν|ται), et l'écriture se resserre et s'amincit quand la place manque. C'est le « thin and shaky » d'Allen. Dans une même note, S2 passe parfois à la minuscule en fin de ligne (f. 175r, l. 10 : « …δαιμόν^ν^ων τὰ ἄχη », planche 4, n° 5). Ce changement d'écriture ne signale donc pas un changement de main (§ 6, n° 15).

### 2.2 Les gloses en petites majuscules droites

Les gloses courtes de la marge intérieure, et souvent les notes de personnage, sont en petites majuscules plus droites que la semi-onciale des scholies. L'inventaire du f. 164v le note pour κακ(ὸς) ἤμην (l. 8), ἐὰν τ(οῦ)το ποιήσω(μεν) (l. 31) et ἀληθῶς (l. 42). C'est aussi le cas au f. 171r. L'inventaire de cette page parle de « petite minuscule droite » ; j'y vois des majuscules (vérifié ; planche 1, i et j). Dans πρὸ(ς) τ(ὰς) γυ|ναῖκας, σπινθῆρ(α), ὦ μέθυσοι, τρεῖς κο|τύλας οἴν(ου) | χωροῦν, on trouve Π, Ρ, Τ, Γ, Υ, Ν en « Н », Κ en deux pièces, C lunaire, Θ barré, avec seulement quelques formes minuscules (ω, ρ). La glose ὅπου du f. 176r (l. 28) est du même type (Π à barre débordante, Υ en Y ; vérifié, planche 1, l).

### 2.3 La minuscule de S2

S2 écrit aussi en minuscule, dans trois cas.

1. **Vers suppléés et corrections du texte.** Le v. 33 (f. 162v, marge int.) est en grande minuscule penchée, à plume fine (planche 1, e ; vérifié). C'est le « very large, sloped to the right, and fine » d'Allen 1896, 320. Les autres exemples sont le v. 169 (f. 164v, marge ext., « minuscule penchée »), le v. 647 (f. 170r, « minuscule de grand module inclinée »), τινα suscrit au v. 833 (f. 172r, l. 42, petite minuscule inclinée, ν en Ν onciale), περ au v. 938 (f. 173v, l. 21) et οι suscrit au v. 1127 (f. 176r, l. 1). Le supplément des vv. 1102–1103 (f. 175v, marge inf.) commence en minuscule (κάρα κομίζ(ων)), puis passe à des formes de semi-onciale : Π, Λ, Η, Ν, Γ, Ο, Ρ dans « … τὴν γοργόνος πέρι » (vérifié ; planche 1, f). Le mot βοώιη, ajouté dans une lacune au v. 506 (f. 168r, l. 41), mêle de même un Η majuscule et un β fermé.
2. **Quelques gloses**, par exemple ζωνάριον (f. 164r, l. 18, planche 1, k). Le f. 174v a aussi des notes courtes en « minuscule mêlée (ω en w) » (inv. f174v).
3. **Une série de scholies au f. 162v** (§ 2.4).

Ce mélange de formes est l'indice le plus sûr pour attribuer une minuscule à S2. Ce scribe de semi-onciale garde dans sa minuscule des capitales et des formes de semi-onciale.

### 2.4 Le cas du f. 162v : trois écritures dans les marges

Le f. 162v est la seule page où les notes ne sont pas toutes dans la semi-onciale de S2. Les sources s'opposent sur ce point. Pour Allen 1896, 320–321, toutes les scholies en minuscule sont de B, « an experiment on the part of B », avec les mêmes lettres disjointes et la même teinte d'encre. Pour Orsini 2011, 327 n. 24, la scholie au v. 32, dans le bas de la marge intérieure, est d'une troisième main contemporaine (dossier, § 4.3). J'ai comparé les écritures sur l'image (planche 1, a–g ; spécimen `../specimens/f162v/f162v_comparaison_mains_scholies.png`).

**(a) Marge supérieure et marge extérieure, vv. 1–24 : minuscule de S2.** La notice du haut, « προλογίζ(ει) … », et les scholies de la marge gauche (ὦ ζεῦ χελιδών·…, ἔξωθεν ἐν κύκλῳ περιάγων…, οἷόν τε· δυνατὸν ἐρωτηματικῶ(ς), ἀκούειν· ὁ μὲν τραγικώτερ(ον)…, ξυνετέκνου·…) sont écrites dans une minuscule de petit module (10–15 px), un peu inclinée, aux lettres disjointes et non liées. Les lemmes y sont en semi-onciale : ΑΚΟΥΕΙΝ, avec Ε lunaire et Ν capital (vérifié, planche 1, b), Ζ capital dans ὦ Ζεῦ. Les suspensions sont marquées par un trait (τραγικώτερ(ον), ταπεινότερ(ον)). L'encre ne se distingue pas de celle de S2 (inv. f162v : 1,29–1,34 ; 2,02–2,23). Seule la notice du haut est un peu plus jaune (1,38–1,42 ; 2,30–2,35). Le mélange de la minuscule et de la semi-onciale est celui des vers que S2 supplée (§ 2.3). **Je retiens l'attribution d'Allen** : c'est S2 qui écrit ici en minuscule.

**(b) Marge intérieure, vv. 27 et 30–32 : une minuscule ronde et droite, d'une autre facture.** Les deux notes de la marge droite, « λεί^π(ει) τὸ ἔνθα· οἷον σιω(πῶ) | διὰ τὸ θύριον | ἔπαιξ(ε) δ(έ)· » (v. 27) et « ἐπειδὴ οὐ πάλαι | ἤρξατο διδάσκ(ειν) | ἀλλὰ τρισὶν πρὸ | τούτων ἔτεσιν » (vv. 30–32 ; Martin 1882, 196 : « 32. Ἐπειδὴ — ἔτεσιν. Int. »), sont d'un module plus grand (environ 16 px) que (a). Elles sont droites, rondes et espacées, sans lemme en capitales (vérifié, planche 1, c). Leur répertoire de formes est celui de T :

- π en ϖ ;
- κ en « lc » ;
- λ à longue diagonale ;
- ξ à longue queue ;
- δ à boucle haute ;
- ligature ε-π.

L'encre de la note du v. 27 est celle de T (1,28 ; 1,96–2,01) ; celle de la note des vv. 30–32 est un peu plus jaune (1,32–1,33 ; 2,15–2,18) (inv. f162v). Ce n'est pas la grande minuscule penchée des suppléments de S2 (comparer planche 1, c et e) : le module est voisin, mais l'axe et les proportions diffèrent. **Conclusion.** Ces deux notes sont la « troisième main » d'Orsini, qui vise expressément la scholie au v. 32. Par l'alphabet et, pour l'une des deux notes, par l'encre, cette main se rapproche de T, qui écrirait ici en lettres détachées. On rejoindrait alors la thèse de Martin 1882, xiv–xvi et de Zacher 1888, 535, pour qui le copiste du texte a écrit lui-même les scholies des cinq premières pièces. L'hypothèse reste à éprouver. J'ai fait un premier essai sur le f. 14r, d'après le PDF intégral du dépôt (`ravennas_1904_bnf/Ravennas_MS429_INTEGRAL_11_Comedies_Tome1_planches_001-100.pdf`, planche 17, soit environ 0,2 mm par pixel ; vue de travail `.travail/chap3/vues/cmp2_f14r_f162v.png`). Les vv. 1129–1130 du *Ploutos* y sont restitués deux fois (Martin 1882, xv–xvi). Dans la marge extérieure, c'est la minuscule liée du texte. Dans la marge supérieure, c'est une minuscule ronde, droite et détachée, que Martin dit écrite « d'après le système d'écriture des scolies », par le copiste lui-même (R¹ ; mais S1, distinct de T, selon Allen 1896, 318–319 et Orsini 2011, 327). À cette résolution, la minuscule de la marge intérieure du f. 162v ressemble à cette seconde restitution plus qu'à la première. La « troisième main » serait alors celle qui écrit en minuscule les notes et les restitutions de la première partie du manuscrit, T ou S1 selon l'opinion qu'on adopte, et non S2. Il faudra le vérifier à pleine résolution, avec la scholie à Ploutos 509 qu'Orsini donne à la même troisième main (f. 6v).

**(c) Semi-onciale de S2.** Elle couvre le bas de la marge extérieure (δασυπώγων·…, avec le lemme du v. 33 que T omet), πρόσεχε· ἀν^τ τ^ου μνῆσαι, les deux scholies au v. 38 (marge int.), la scholie de six lignes au v. 21 (marge inf. : οἷόν γε ποῦ ᾽στιν αἱ σοφαί·…, planche 1, g) et ὁ ἱερὸς χορός. Pour la glose, Martin 1882, 196 lit μνῆσαι, l'inventaire νοῆσαι ; sur l'image, je lis plutôt μνῆσαι.

Allen 1896, 321 constate que la « feeble » minuscule disparaît au f. 163v et revient au f. 164v. Je ne retrouve de minuscule de scholie au f. 164v que dans le supplément du v. 169, et au f. 164r que dans la glose ζωνάριον. Après le f. 162v, S2 n'écrit donc plus de scholie suivie en minuscule.

### 2.5 Ce qui n'est pas de T

Deux notes ont été attribuées à la main du texte. La glose ὅπου du f. 176r (l. 28, v. 1152–1153) est « de la main du texte » selon Martin 1882, 208 (« 1151. Ὅπου. Main du texte »). Sur l'image, c'est une très petite semi-onciale : ο rond, Π à barre débordante, ο, Υ en Y. On n'y trouve aucune forme de T, ni le π en ϖ, ni la minuscule liée (vérifié, planche 1, l ; `../specimens/f176r/f176r_glose_l28_opou.jpg`). Elle est de S2, comme le propose l'inventaire. La glose χωνεύει, écrite dans la ligne même du v. 57a (f. 163r, l. 20 : « καὶ χοανεύει χωνεύει »), est en semi-onciale de S2, avec un petit ω suscrit au χ (`../specimens/f163r/f163r_gl_l20_choneuei.jpg`). Le scholiaste a utilisé le blanc de la ligne : ce n'est pas une glose entrée dans le texte.

### 2.6 Encres et campagnes d'écriture

**Règle générale.** Sur la plupart des pages, l'encre de S2 et celle de T se recouvrent, et seule la forme les sépare. C'est le cas aux ff. 162v, 163r (même teinte, densité plus forte chez S2), 164v, 165r, 165v, 168v, 169r, 169v, 170v, 171r, 175r, 176r et 177r. S2 est parfois un peu plus roux ou plus jaune, mais seulement à densité égale et dans une même zone : au f. 168r (B/R 2,45–2,69 contre 2,18–2,28 pour T), au f. 173v (courbes de densité décalées de +0,15), aux ff. 167v, 172v et 174v. Les traits fins, les accents et les points mesurent « gris » quelle que soit la main (inv. f169v, f174r). Rien ne permet donc d'attribuer à S2 ou à T une petite correction d'après sa seule couleur.

**Campagnes distinctes à l'intérieur de S2.**

- Les **gloses de la marge intérieure** et le supplément βοώιη du f. 168r ont l'encre de T (B/R 2,21–2,47), et non celle des scholies de la marge extérieure (2,45–2,69), alors que l'écriture est la semi-onciale de S2 (inv. f168r, `../specimens/f168r/f168r_l07_08_gloses_detail.jpg`). Les gloses du f. 167r (l. 7, 33) et du f. 167v (ὀδόντ(ας), φανερῶς) sont d'une encre intermédiaire. Au f. 163v, les scholies de la marge intérieure (B/R ≈ 2,4) diffèrent de celles des marges supérieure et extérieure (≈ 2,8–3,0). Gloses et scholies ne semblent donc pas avoir été écrites dans la même séance.
- Au f. 166r, la **1re ligne de la scholie gauche du v. 329** est d'une encre gris-brun (1,24–1,26 ; 1,61–1,67) ; la 2e ligne a l'encre ordinaire (1,33 ; 2,20). L'écriture est la même.

**Notes de personnage de la forme de S2 à l'encre orangée.** Plusieurs sigles et notes ont la forme et les abréviations de S2, mais une encre orangée, proche de celle de la main de 1516 :

- χ^ρ (l. 19) et ἡμι^χ γυν^αικῶν (l. 24) au f. 170r ;
- χ^ορ au f. 171v, l. 22 ;
- les sigles du « groupe A » du f. 172v ;
- τοξ(ότης) au f. 174r, l. 43 ;
- ηχω, εὐρι^π ὡς περσεύς, κ^η^δ ὡς ἀνδρομε^δ et σκυ^θ au f. 175v ;
- μνη^σι au f. 171r, l. 10.

J'ai mesuré moi-même les cas suivants, en comparant chaque fois avec un témoin de la même zone :

| Page, élément | A_G/A_R | A_B/A_R | Témoins de la même zone |
|---|---|---|---|
| 174r, τοξ(ότης), l. 43 | 1,60 | 3,09 | scholie de S2, même ligne : 1,37 / 2,50 ; texte de T : 1,37 / 2,33 |
| 171v, χ^ορ, l. 22 | 1,59 | 2,99 | scholie de S2, même ligne : 1,44 / 2,87 ; T : 1,34 / 2,26 |
| 175v, ηχω, l. 2 (hors tache) | 1,55 | 2,86 | σκυ^θ de S2, l. 2–3 : 1,30 / 2,23 ; T : 1,37 / 2,40 ; Ηχ de 1516, l. 3 : 1,44 / 2,53 |
| 175v, εὐρι^π ὡς περσεύς, l. 17 (dans la tache) | 1,60 | 2,97 | scholie brune de S2, même hauteur, dans la tache : 1,40 / 2,76 |
| 175v, κηδ ὡς ἀνδρομεδ, l. 24 (dans la tache) | 1,57 | 3,02 | scholie de S2, l. 24–25 : 1,45 / 3,02 |

La différence est nette pour τοξ(ότης) au f. 174r et pour ηχω au f. 175v. Elle est faible pour le χ^ορ du f. 171v. Dans la tache d'humidité du f. 175v, elle ne prouve rien, puisque les scholies brunes de S2 y mesurent elles aussi « orangé ». L'inventaire du f. 175v l'avait déjà noté (« B/R 0,517 hors tache, 0,429 dedans »).

Plusieurs de ces notes figurent déjà dans le Monacensis gr. 492 (G), copié au XVe s. : celles du f. 175v, le χορ̊ du f. 171v et les sigles du f. 170r (inv. f170r, f171v, f175v). Elles existaient donc avant 1516. Trois hypothèses restent possibles : (1) S2, dans une campagne de *notae personarum* faite avec une autre encre ; (2) une main médiévale qui imite S2 ; (3) un sigle brun de S2 repassé en 1516. Le cas (3) est démontré au f. 168v pour γυ^νη τίς (v. 533), dont les bords sont bruns et le cœur orangé (inv. f168v). Je n'ai pas pu reproduire ce test de manière probante : au f. 174r, les bords de τοξ sont plus orangés que son cœur, mais c'est aussi le cas des scholies brunes, parce qu'à cette échelle la compression JPEG mêle les couleurs au bord des traits. La question relève du chapitre 1 et d'un examen aux UV. Pour la transcription, il suffit de noter la forme (celle de S2) et la couleur, sans conclure sur la main.

## 3. Disposition : espaces, ancrage, ouverture et clôture, lemmes, renvois

### 3.1 L'espace réglé et son usage

Zacher 1888, 534–535 décrit la réglure de R. Le cadre du texte mesure en moyenne 0,103 × 0,22 m ; il est limité par deux verticales de chaque côté et porte 43 lignes, 42 dans les trois premiers cahiers. Les espaces des scholies sont réglés sur les marges supérieure (0,025 m de hauteur), extérieure (0,055 m) et inférieure (0,04 m), par une horizontale en haut et en bas et une verticale au bord extérieur. La marge intérieure n'est pas réglée (largeur libre d'environ 0,033 m) ; les notes qu'on y lit « erscheinen somit mehr als glossen ». Les inventaires retrouvent ces doubles verticales du cadre (ff. 165r, 165v, 169v, 170v, 174v) et constatent, au f. 165v, que les scholies ne suivent pas la réglure horizontale.

S2 n'exploite pas cet espace comme le faisait le premier scholiaste, qui l'utilisait « a cornice chiusa », sur les quatre marges (Orsini 2011, 328). Il écrit surtout dans les marges extérieure et intérieure (Zacher 1888, 538 ; Orsini 2011, 328), ce que confirment les 30 inventaires. La marge supérieure ne sert que sur sept pages (ff. 162v, 163v, 164r, 164v, 167v, 168v, 172r) ; elle reçoit soit une longue scholie qui ne tient pas ailleurs (Σ 80 sur six lignes au f. 163v ; Σ 804–805 sur trois lignes et demie au f. 172r), soit une note qui ouvre la pièce (f. 162v). La marge inférieure reçoit les longues scholies des ff. 162v (v. 21, six lignes) et 164r (vv. 161–162, huit lignes), le débordement de Σ 120 au f. 163v, deux lignes au f. 172r et le supplément des vv. 1102–1103 au f. 175v. La marge intérieure porte en général moins de notes, et plus courtes (Zacher 1888, 538). Quelques pages font exception, avec une longue scholie dans cette marge : Σ 101b sur neuf lignes au f. 163v, Σ 274 sur neuf lignes au f. 165v, Σ 567 sur onze lignes au f. 169r.

### 3.2 Ancrage des notes

**Au droit du vers.** Chaque note est écrite en face du vers qu'elle commente, parfois avec un décalage d'une ou deux lignes (f. 168r : la note au v. 487 est à la l. 23, celle au v. 505 deux lignes plus haut ; f. 173v : celle au v. 944 en face des l. 28–29). Quand plusieurs notes se suivent, elles forment un bloc continu, « eine scheinbar zusammenhangend fortlaufende masse » (Zacher 1888, 536). Seuls les tirets et les ÷ les séparent alors (§ 3.4).

**Les notes sont postérieures au texte.** S2 s'adapte à des lignes déjà écrites :

- les scholies commencent là où finit la ligne du vers (f. 168r : « x ≈ 945–1240 ») ;
- au f. 163v (l. 4), une ligne de scholie commence plus à droite pour éviter le ΟΝ final de τήμερον ;
- au f. 169v, S2 raccourcit deux lignes de la scholie au v. 616 devant les paragraphoi de T des vv. 617–618.

S2 travaille donc après T, et après les paragraphoi de T. Cela concorde avec l'idée d'un commentaire ajouté dans une phase ultérieure, sans plan de mise en page commun (Orsini 2011, 328).

**Notes déplacées, coupées ou doublées.**

- **Notes déplacées.** Quand la marge est pleine, S2 déplace la note et, le plus souvent, pose un renvoi : au f. 164r, la scholie au v. 135 (✕) ; au f. 169r, celle au v. 566, renvoyée en haut de la marge extérieure (·×·). Au f. 170v, la note « κάθηται ἐπὶ βωμοῦ ὡς ἱκε(τεύων)… » est écrite à la hauteur du v. 717 alors qu'elle commente le v. 693, sans renvoi ; Rutherford l'édite au v. 693.
- **Notes coupées entre les deux marges.** Au f. 164r, la scholie au v. 131 commence dans la marge gauche et finit dans la droite, avec le renvoi ·϶·. Au f. 166v, celle au v. 339 est répartie de la même façon, avec un trait de renvoi. Au f. 169v, l'explication du v. 624 occupe les deux marges ; au f. 176v, la scholie au v. 1197 commence dans la marge intérieure et se poursuit dans l'extérieure.
- **Notes doublées.** Au f. 169r, la même glose ὡς ϗ τ(ού)τ(ου) πάλ(ιν) γενομένου est écrite deux fois, pour les vv. 562 et 564. La scholie au v. 585 a un doublet partiel dans la marge intérieure. Au f. 173v, R sépare en deux morceaux, chacun clos par ÷, des scholies que Dübner donne d'un seul tenant (vv. 928, 935).

### 3.3 Notes dans la colonne et dans l'interligne

S2 se sert des blancs de la colonne :

- à la fin d'une ligne courte : χωνεύει au f. 163r, l. 20 ; les gloses des l. 2 et 7 du f. 170v, dans le blanc des lignes lyriques ; πάλιν ἐξ ἀνδρομέδ(ας), ὡς ἐν κωμωδίαι ÷ et κ(αὶ) τοῦτο ἐξ ἀνδρομέδας ÷ au f. 174v, l. 17, 20 et 33 ; τοῦ προλόγου ἀνδρομέδας εἰσβολή ÷, λ(είπει) μέλλουσα τυχεῖν et φλυαροῦσα à droite des vers du f. 175r ;
- dans le renfoncement d'une ligne lyrique : glose du v. 913 au f. 173r, l. 37 ; scholie au v. 935 à droite de ἱστιορράφος, seul sur la l. 18 du f. 173v ;
- dans l'interligne, près de la marge : ὁ μνησίλοχ(ος) au f. 165v, l. 15 ; λαλεῖς au f. 175v, l. 13–14 ; ἀντὶ τῆς ἐνθουσιαστικῆ(ς) au f. 164r, l. 4–5.

Ce sont les « intermarg. » de Rutherford 1896, I, xxviii. Je ne trouve aucune glose interlinéaire au sens strict, c'est-à-dire écrite au-dessus du mot glosé à l'intérieur de la ligne (inv. f162v, f165r, f173r). Allen ne prête à B que de « rare glosses » (Allen 1896, 320).

### 3.4 Ouverture, séparation et clôture

| Signe | Fonction | Exemples (page, ligne, vers) | Remarques |
|---|---|---|---|
| tiret « – » en vedette, à gauche du début | ouvre une note, surtout quand elle commence au droit d'une ligne de texte | 165v (vv. 261, 278, 282, 291, parépigraphe) ; 166r, l. 7 (v. 300 ; seul cas de la page, `../specimens/f166r/f166r_l07_scholie_tiret_initial.jpg`) ; presque toutes les notes du f. 167r et de la marge gauche du f. 167v ; 168r, 169v, 170r, 170v (v. 682), 171r (l. 26, 27, 40), 171v, 172r, 173r (l. 21–23), 173v, 174r (v. 1001), 175r (l. 12–13) | contredit l'absence de séparations chez S2 (Orsini 2011, 328 ; Zacher 1888, 536), comme le note déjà l'inv. f173r ; se confond avec une paragraphos de T (§ 6, n° 11) |
| point « · » initial | même fonction | 165r (v. 224, 237) ; 170v (v. 693) ; 175v (vv. 1096, 1118) ; « ·– » au f. 170r (v. 658) ; « ·:· » au f. 169r (v. 585) | — |
| trait fin tiré depuis la fin du vers jusqu'à la note | relie le vers à sa scholie | 165r, fin des l. 19, 23 et 41 (`../specimens/f165r/l23_trait_ouverture_scholie.jpg`) | à ne pas prendre pour une marque de la Juntine (inv. f165r) |
| « ÷ » (obèle pointé) | ferme la note | presque toutes les pages, du f. 162v au f. 177r | ressemble au signal ÷ de T et à un dicolon (§ 6, n° 7) ; quand la note finit au bord de la colonne, il tombe dans la bande des sigles (167v, 169v, 172v, 173v, 174v) |
| « :– » (dicolon et tiret) | ferme la note | 165r, 167v, 172v ; « :- » au f. 170r | Rutherford 1896, I, xxviii : S2 termine d'ordinaire par un point haut ; « At parts, however, e.g. Thesmo. ll. 100 ff, he employs the sign :— ». ÷ et :– sont deux formes du même signe final |
| point simple | ferme la note | 163r (ἡλίῳ·, ᾠδαῖς·) ; 176r, l. 1 (sans signe) ; 168r, l. 16 (sans signe) | — |
| trait ondulé | ferme la note | 174v, v. 1040 (marge g.) | — |
| ÷ à l'intérieur d'une ligne | sépare deux scholies qui se suivent | 163v (« …παρεπιγράφεται ÷ ὁ ἀγάθων… ») ; 167r | — |
| ἄλλ(ως), et tilde marginal | introduit une seconde explication | 166v (v. 346) ; 168r (v. 506) ; 171r (v. 747) ; 173v (v. 948) ; tilde dans la marge au f. 172r (v. 804–805) | — |
| points « • » ; « ~ … ~ » | devant les explications introduites par ἢ ; lemme encadré | 172r, scholie A (v. 808) ; « ~ τάλαντα ~ » au f. 172r (v. 811) | — |

### 3.5 Lemmes

**Au f. 162v, les lemmes sont réguliers.** Les scholies en minuscule de la marge extérieure en ont presque toutes, souvent en semi-onciale : ὦ ζεῦ χελιδών·, ΑΚΟΥΕΙΝ·, εὖ ἴσθ᾽ ὅτι·, ξυνετέκνου·. Les scholies en semi-onciale en ont aussi : δασυπώγων·, πρόσεχε·, οἷόν γε ποῦ ᾽στιν αἱ σοφαί·. Martin 1882, 196 sépare de même lemme et note (« Ὦ Ζεῦ, χελιδών · ἐπεὶ εἰώθασιν… »). Cela confirme Zacher 1888, 538 : dans ces trois pièces, les lemmes ne se trouvent qu'à la première page des *Thesm.*, puis « nur vereinzelt ».

**Ailleurs, les lemmes sont sporadiques et ne se distinguent pas du reste de la note.** Le premier mot de la note reprend le mot du texte, suivi d'un point haut : Σ 80 (ἐπεὶ τρίτη ᾽στί) au f. 163v ; ἄρσενι· εὐτόνω·, Γενετυλλίδες·, λυκουργίας·, ὀλολύζει· au f. 164r ; ναυσιμάχης μέν·, κλεοφῶν·, ~ τάλαντα ~ au f. 172r ; αἰκάλλει σαίνει au f. 172v ; ἡ σπάρτ(ος) au f. 173v ; [π]ορμὸς au f. 174v. Comme l'écrit Zacher 1888, 536, S2 « hat die lemmata durch nichts als solche gekennzeichnet », souvent sans même un point. Le lemme n'aide donc pas à repérer la note : il faut se fier à sa position.

**Lemme et texte de R diffèrent souvent.** C'est l'un des pièges de lecture (§ 6, n° 12) et une donnée pour l'apparat :

- γε (lemme) et τε (texte) au v. 21, f. 162v ;
- lemme δασυπώγων alors que T omet le v. 33 ;
- la scholie au v. 220 du f. 165r lit δουροδόκης, contre ξυροδίκησ dans R ;
- οἰνοπίπας, οἰνοπίπους contre οἰνοπότιδας, f. 167r, v. 393 ;
- ἰφύων contre ἀφύων, f. 173r, v. 910 ;
- πυλάξηι contre πυλάξι, f. 174v, v. 1007 ;
- la scholie des l. 21–23 du f. 175v cite κάρα κομίζων (v. 1102), que T omet ;
- πέπαικτ(αι) en face de πέπυσται, f. 177r, v. 1227 ;
- au f. 164v, la scholie du v. 179 glose καινῇ alors que R a κοινὴ.

### 3.6 Renvois : vrais et faux

**Ce que disent les sources.** S2 n'aurait ni lemmes, ni séparations, ni signes de renvoi (Orsini 2011, 328 : S2 « non utilizza né modalità simbolica né modalità verbale » ; Zacher 1888, 536). Rutherford 1896, I, xxvii est plus nuancé : quand la note ne peut pas être placée en face de son vers, S2 se fie d'ordinaire à un lemme ; « It is only now and again (e.g. Eq. 166 : Lys. 108) that he uses a sign to place the note correctly ».

**Ce que montrent les images.** Rutherford a raison, et les inventaires ajoutent des exemples dans les *Thesm.* Les renvois sont rares et chaque fois motivés : la note est loin de son vers, coupée entre deux marges, ou il s'agit d'un vers suppléé.

| Page, vers | Signe dans le texte | Signe en tête de la note | Motif | Contrôle |
|---|---|---|---|---|
| 164r, v. 127 (fin de la l. 5) | ∈ (ε lunaire à langue prolongée), après ὀπός | même ∈ devant « πάλιν φῶς ἐγένετο αὐτοῖς… » (l. 7) | note décalée de deux lignes | vérifié (planche 3, 1a–1b) |
| 164r, v. 131 (fin de la l. 10) | ·϶· (point, antisigma, point) | même signe devant « πολλαῖς γλώτταις… » (marge dr., l. 19) | scholie commencée dans la marge g. (l. 11–13) | inv. f164r ; `../specimens/f164r/f164r_l10_renvoi.jpg` |
| 164r, v. 135 (interligne 13/14) | petit signe au-dessus de λυ- | ✕ à bouts bouclés (marge dr., l. 21) | note déplacée vers le bas | inv. f164r (probable, formes inégales) |
| 166v, v. 339 | petit trait oblique après παιδίον (fin de la l. 3) | — | seconde moitié de la scholie dans l'autre marge | inv. f166v |
| 166v, v. 370 | — | ·✓· devant la glose συμμαχεῖν | glose au bout de la ligne | inv. f166v (`../specimens/f166v/f166v_l34_renvoi_glose.jpg`) |
| 169r, v. 566 (interligne 15/16) | ·×· au-dessus de θεὼ | ·×· devant « ὡς τὼ χεῖρε· οὐκέτι δ(ὲ) μὰ τοῖν θεοῖν… » (en haut de la marge ext.) | marge voisine occupée par les scholies des vv. 557–565 | vérifié (planche 3, 2a–2b) |
| 164v, v. 169 | croix pointée (brune) prolongée d'un trait orangé | — | vers suppléé en marge | inv. f164v |
| 170r, v. 647 | ÷ à barre ondulée après la l. 11 ; ·/· devant la l. 12 | même ÷ en tête du vers marginal | vers suppléé ; signe plus proche de l'encre de T | inv. f170r (`../specimens/f170r/f170r_renvois_l12_m647_l11.jpg`) |
| 175v, v. 1101 (l. 20) | « —+:— » | « +: » en tête des vv. 1102–1103 (marge inf.) | vers suppléés ; encre orangée | vérifié (planche 3, 3 ; planche 1, f). Allen 1896, 317 dit le signe « erased by Giunta » : les deux sont visibles |

Deux cas restent incertains. Au f. 175r, un trait horizontal sous κη- de κηφέα (l. 12) pourrait répondre au tiret de la scholie « — πατὴρ γὰρ τῆς ἀνδρομέδας ὁ κηφεύς ÷ » (inv. f175r). Au f. 171v, une « flèche » d'encre de S2 passe sous la fin de la l. 18, vers la glose de la marge intérieure (inv. f171v).

**Faux renvois : la finale -ος de T.** En fin de ligne, T écrit souvent -ος sous la forme d'un grand sigma lunaire de 5 à 6 mm qui enferme un petit ο, suivi d'un point. Le signe ressemble à « Ͼ », « ⊙ » ou « © » :

- f. 164r, l. 40, τήιος ; l'inventaire y voit déjà la finale et non un renvoi ;
- f. 169v, l. 8, ἐγκαθήμενος (correction 4 de l'inv. f169v) ;
- f. 167r, l. 18, ἀποκεκρυμμένος, proposé par l'inventaire ;
- f. 175v, l. 20, γοργόνος (planche 3, 3, à gauche du renvoi « —+:— ») ;
- f. 165v, l. 31, λιγνύος, en spirale.

L'inventaire du f. 163v prend le même signe, à la fin de la l. 17 (v. 96, après οὑκκυκλούμεν-), pour un « sigma pointé, signe de renvoi » qui relierait le mot à Σ 96. Il ajoute que « la terminaison du mot … finit avant (-μενος) ». Sur l'image, le mot s'arrête sur le ν de T à jambage plongeant, qui ressemble à un ρ. Le grand C enfermant un ο et suivi d'un point est la finale -ος, exactement comme au f. 164r, l. 40 (vérifié ; planche 3, 5a–5b). La scholie commence ensuite, sans signe de renvoi. Le f. 163v n'a donc **aucun** renvoi (correction, § 8).

## 4. Répertoire des abréviations et des signes tachygraphiques

### 4.1 Principes

Les scholies abrègent beaucoup plus que le texte (Martin 1882, xvi). S2 combine quatre procédés :

1. la **suspension**, marquée par un trait, un apex ou un accent ;
2. la **lettre suscrite**, qui donne la terminaison ;
3. les **compendia** : signes conventionnels hérités de la tachygraphie, qui notent une syllabe ou un mot entier (ϗ, « ʒ », ·/·, λ̸…) ;
4. le **trait suscrit** sur des mots fréquents et sur les chiffres.

Comme l'a vu Rutherford 1896, I, xxvii, S2 accentue ses abréviations. L'accent de la syllabe supprimée se pose sur le signe, ou il tient lieu à lui seul de signe de suspension : ὁδ' = ὁδ(όν), αὐτ̀ = αὐτ(όν), τ̀ = τ(όν) ou τ(ό), κ̀ = κ(αί). Il faut donc lire l'accent d'une abréviation comme une indication de développement, et non comme une faute d'accentuation.

### 4.2 Tableau

Les exemples renvoient à la page, à la ligne (ou à la marge) et au vers commenté ; « pl. 2, n° » renvoie aux vignettes de la planche `../planches/ch3_pl2_abreviations.jpg`. Les entrées marquées † ont été vérifiées sur l'image pour ce chapitre ; les autres reposent sur les inventaires de page.

| # | Signe | Forme dans R | Développement | Exemples (page, ligne ou marge, vers) | Illustration | Remarques, pièges |
|---|---|---|---|---|---|---|
| 1 † | ϗ | chez S2, le κ en deux pièces (haste + C) suivi d'une queue descendante : aspect « Ις », « ιʒ » ou « ις » ; décrit aussi comme un « S couché avec point » | καί | 164v, marge sup. (v. 168) et l. 12–14 (vv. 177, 179) ; 165v, l. 27–29 (v. 278) ; 167v, l. 7 (v. 429) ; 171v, l. 5–12 (vv. 770–773) ; 176v (vv. 1197, 1203) ; 177r, l. 22 (v. 1229) | pl. 2, n° 1, 2, 16 ; pl. 3, n° 4 ; `../specimens/f176v/f176v_sch_v1203_kai_compendium.jpg` | se lit à tort εἰς, ις, ἰξ ou ἐξ (inv. f171v, f176v). Dans le texte de T, ϗ a la forme d'un « S » (166r, l. 15 ; 170r, l. 21–22 ; 171v, l. 27) |
| 2 | κ̀, κ pointé | κ surmonté d'un grave ou d'un point | καί (suspension accentuée) | 174r, l. 15–17 (vv. 974–975, deux fois) et l. 28 (v. 986) ; 175v, l. 17–18 (v. 1098) | — | à ne pas lire κ(ατά) |
| 3 † | « ʒ » isolé | trait de tête et longue queue oblique, séparé par des blancs ; variantes « ʒ » suivi d'une apostrophe, « ϶ », δ à crochet suscrit, δ' | δέ | 165v, l. 4–5 (v. 254, deux fois), l. 7–12 (v. 258), l. 12–14 (v. 263) ; 166r, l. 31 (v. 324) ; 166v, l. 37 (v. 373) ; 171r, l. 14 (v. 734) ; 174v, l. 1–2, 13–15, 38–41 (vv. 1003, 1016, 1040 : forme « ϶ ») ; 175v, l. 21–23 (v. 1102) ; 176v (v. 1197) | pl. 2, n° 3, 6 ; `../specimens/f166r/f166r_l31_scholie_de_compendium.jpg` | même forme que n° 4 : le signe isolé, qui suit un mot complet, vaut δέ (inv. f165v) ; ne pas lire ζ, ξ ni ἤ (le « ἢ » de l'inv. f165r, v. 231, est un δ(έ), § 8) |
| 4 † | « ʒ » attaché | le même signe, lié à un τ ou à un θ final, ou réduit à un crochet | -αι, -ται | 165r, l. 30–31, 37–38 (-ζοντ(αι), καλεῖ(ται), vv. 237, 245) ; 165v, l. 26–29 (ἐκκυκλεῖ(ται), γίνεσθ(αι), τίθετ(αι), μιμεῖ(ται), vv. 277–279) ; 166r, l. 2 et 35–36 (χρῶντ(αι), γενέσθ(αι), vv. 295, 329) ; 169v (κρύπτετ(αι), v. 600) ; 171v (ἀγάλλετ(αι), v. 773) ; 173r (« -ται en ζ », vv. 898, 917) ; 177r, l. 5 et 20 (παρακελεύετ(αι), πέπαικτ(αι)) | pl. 2, n° 4–5 | à ne pas lire comme une lettre ; dans la note du v. 1227 (177r, l. 20), le petit signe final en « τ » est encore à interpréter |
| 5 † | ·/· | trait oblique entre deux points (obèle couché) ; forme réduite « /· » après δέ | ἐστί(ν) | 166v, l. 37–39 et 40–41 (vv. 373 deux fois, 377) ; 165r, l. 24 (v. 231 : μύζειν δ(έ) ἐστι…) ; 171v, l. 18, marge int. (v. 781 : ἐν ᾧ τὸ ρ̄ ἐστί) ; 162v, marge inf. (v. 21, avant σοφοκλ-) ; 164r, l. 12 (v. 131, après ἡδύ ; probable) ; 165v, l. 4 (v. 254, forme réduite) | pl. 2, n° 3, 6 ; pl. 4, n° 4 ; `../specimens/f166v/f166v_sch_g_373_esti.jpg` | se confond avec le ÷ final (obèle droit pointé), avec le signal ÷ de T et avec le renvoi ·/· du f. 170r (l. 12). Le texte garantit la lecture : Martin 1882, 205 (« ἐν ᾧ τὸ ρ ἔστι ») ; Dübner 1842, lu par OCR (« χρηματίζειν ἐστὶ… », « ἐπιστάτις ἐστὶν… ») |
| 6 † | ·//· | deux traits obliques entre deux points (aspect « % ») | εἰσί(ν) | 173v, l. 17 (v. 935 : λινοποιοί εἰσιν) | pl. 2, n° 7 ; `../specimens/f173v/f173v_sch_935_marge_g.png` | doublement du signe de ἐστί pour le pluriel |
| 7 † | λ̸ | Λ traversé d'un trait oblique, ou λ dont la jambe droite se prolonge en crochet vers le bas et la gauche | λείπει | 168r, l. 20, marge int. (v. 485 : λ(είπει) τὸ ἔφη) ; 175r, l. 10, marge ext. (v. 1054 : λ(είπει)· ἔσχον ἐκ τῶν δαιμόνων τὰ ἄχη…) et l. 30 (v. 1072 : λ(είπει) μέλλουσα τυχεῖν) | pl. 2, n° 8–9 ; pl. 4, n° 5 | au f. 175r, l'inventaire y voit un « ʒ (ἤγουν ?) » : la lecture λείπει est celle de Martin 1882, 207–208 (« Λείπει — ἄχη ἔσχον », « Λείπει μέλλουσα τυχεῖν ») et de Rutherford, qui traduit « supply » (§ 8) ; ailleurs, λεί^π(ει) par suspension (162v, marge int., vv. 27, 38) |
| 8 † | -ος | ο suscrit, souvent réduit à un point plein ; petit signe bouclé ; ο au-dessus d'un τ barré | -ος | 166r, l. 34 (ἀπόλλων(ος), v. 327) ; 164r, marge sup. (ἀπόλλω^ν(ος), v. 125) ; 165v, l. 11 (κροκωτ^ο(ς), v. 261) ; 168r (vv. 487, 489) ; 169v (μνησίλοχ^ο(ς), πτύσματ^ο(ς), οἰνηΐδ^ο(ς), vv. 603, 616, 620) ; 163v, l. 14 (εἶδ(ος), πλακοῦντ(ος), v. 94) | pl. 2, n° 14 ; `../specimens/f163v/f163v_scholie_S94_eidos.png` | le point se prend pour un esprit ou une ponctuation ; le signe bouclé, pour un ε ou pour δέ (« ἐκ δ(ὲ) », première lecture fautive de l'inv. f163v) |
| 9 | -ον | trait suscrit, apex, ο suscrit | -ον | 162v, marge ext. (τραγικώτερ(ον), ταπεινότερ(ον)) ; 168r (ἐλελίσφακ(ον), v. 486) ; 169v (οὐροδόχ^ο(ν), v. 633) ; 171v (θάνατ̄ = θάνατ(ον), v. 771) ; 165v (σημεῖ(ον), v. 278) | pl. 1, b | — |
| 10 † | -ου | ου suscrit, ȣ, ou petit arc (« ˘ ») au-dessus du τ : τ̆ | -ου ; τ^ου = τοῦ | 164v, l. 31 (τ^ȣ(το), v. 196) ; 165v (τ(οῦ), αὐτ(οῦ), μωρ(οῦ), vv. 254, 258, 290) ; 170r, l. 6 et 13 (τ̆, vv. 641, 649) ; 174v (τ̆, vv. 1007, 1022, 1041) ; 166r (τ^ου, vv. 300, 327) | pl. 2, n° 10, 14, 15 | τ̆ n'est pas un τ accentué : l'arc est le signe de ου |
| 11 | -ων | arc ou circonflexe posé sur la dernière lettre écrite | -ῶν, -ων | 166r, l. 21 (θεσμοφοριαζουσ(ῶν), v. 312) ; 173v, l. 8–9 (ἐπιχειρούντ(ων), v. 928) ; 163r (τ(ῶν) : τ + circonflexe, vv. 53, 68) ; 168v (ἀναφερομέν(ων), v. 529) | — | le circonflexe d'abréviation se prend pour l'accent du mot |
| 12 | -ιν, -ειν | trait courbe montant | -ιν, -ειν | 166r, l. 2 (εἰσάγωσ(ιν), v. 295) ; 174v, l. 18–19 (λαμβάν(ειν), v. 1019) | — | même signe pour -ην, -ειν et -ιν dans tout R (Martin 1882, xvii) |
| 13 | -ης, -ις | petit signe en « ς » suscrit ; ς suscrit | -ης | 165v, l. 10–11 (τ(ῆς) κλίν(ης), v. 261) ; 163r, l. 31–35 (ἀριστοφάν(ης), vv. 67–69) | `../specimens/f165v/f165v_sch261_int_klinis.jpg` | Martin 1882, xvii : le même signe sert pour -ης, -εις et -ις |
| 14 | -α | lettre suscrite suivie d'un point, ou suspension | -α | 165v, l. 8 (πάντ(α), v. 259) ; 171r, l. 9 (σπινθῆρ(α), v. 729) ; 165r (ταῦ^τ(α), v. 215) | — | Martin 1882, xvi : dans les scholies de R, l'α est d'ordinaire abrégé par un trait horizontal |
| 15 | -μεν, -μεθα | μ surligné ; θ suscrit | -μεν ; -μεθα | 173v (παίσωμ(εν), v. 947) ; 174v (λάβωμ(εν), v. 1040) ; 169v, l. 39 (ἐδεξιούμε^θ(α), v. 631) | — | — |
| 16 | -αι, -ες suscrits | lettres suscrites en fin de mot | -αι, -ες | 170r, l. 21–22 (μόν^αι, γυναῖκ^ες, vv. 656–658) | — | — |
| 17 † | ἀν^τ, ἀν^τ τ̆ | α + ν, avec τ suscrit (parfois αν et τ surlignés), suivi de τ^ου ou τ̆ | ἀντί ; ἀντὶ τοῦ | 162v, l. 26 (πρόσεχε· ἀν^τ τ^ου μνῆσαι, v. 25) ; 169v (v. 600) ; 170r, l. 6 et 13 (vv. 641, 649) ; 174r, l. 43 (v. 1001) ; 174v, l. 5–6, 10, 40 (vv. 1007, 1011, 1041) ; 175v, l. 4 et 12 (vv. 1085, 1094) ; 176v, l. 2 (v. 1170) | pl. 2, n° 10 | ouvre de nombreuses gloses : c'est presque la marque du genre |
| 18 | γ', γ̄, γ suscrit | γ suivi d'une apostrophe ou surmonté d'un trait | γάρ | 164r (vv. 126, 129, 131) ; 164v, l. 25 (v. 190) ; 169v (v. 616) ; 173v (v. 948) ; 174r, l. 15–17 (v. 975, là où Dübner imprime δὲ) ; 174v, l. 10–11 (v. 1012) ; 175v, l. 19 (v. 1099) | — | à distinguer de δ(έ) (inv. f163v, Σ 98 : δ(ὲ) ou γ(ὰρ) ?) |
| 19 | π^ε ; π(ερι)- | π surmonté d'un ε ; π suscrit en composé | περί | 163v (v. 98) ; 164v, l. 12 (v. 177) ; 166r, l. 6 (v. 299) ; 172v (π(ερι)βλέπεσθ(αι), v. 852) ; 173r (v. 917) ; 177r, l. 16–17 (v. 1224) | pl. 2, n° 16 | — |
| 20 | πρ^ο | π + ρ, avec ο suscrit | πρός, πρό | 163v (v. 101) ; 164r, marge inf. (πρ(ὸς) λύραν, v. 161) ; 171r, l. 6 (πρὸ(ς) τ(ὰς), v. 726) ; 175r, l. 27 (προ suscrit dans τοῦ προλόγου, v. 1070) | pl. 1, i | — |
| 21 † | φ^η | φ, parfois barré, avec η suscrit | φησί(ν) | 163r (vv. 67–69) ; 164r (v. 130) ; 169v (vv. 616, 633) ; 170v (v. 710) ; 172v (v. 852) ; 173r (v. 917) ; 173v (vv. 940, 948) ; 174v (v. 1031) ; 175v (vv. 1118, 1119) ; 177r, l. 14 (v. 1222) | pl. 2, n° 11 | au v. 852, Enger 1844 imprime φασίν (inv. f172v) [à vérifier] |
| 22 | φ^α | φ avec α suscrit | φασί(ν) | 164r (v. 130) ; 172r, marge inf. (v. 834) | — | — |
| 23 | εἶ^π | εἶ avec π suscrit, ou un signe | εἶπεν | 170v, l. 4 (v. 682) | — | — |
| 24 | σ^η | σ couché surmonté d'un η | σημαίνει | 176v, l. 5–6 (v. 1174) | — | Dübner 1842 : « σημαίνει δὲ τὸ ἁδρῶς βαδίζειν » (l'image a ἁβρῶς, inv. f176v) |
| 25 † | γρ | Γ dont le ρ pend sous la ligne, suivi d'un signe | γράφεται | 164r, l. 20 (v. 141 : γρ(άφεται) σύ τ' αὐτό(ς)) ; 166v (v. 346) ; 174v, l. 38–41 (v. 1040 : γρ(άφεται) κ(αὶ) φῶτα ἀντομένα) ; 175v, l. 1 (v. 1083) | pl. 2, n° 12 ; `../specimens/f164r/f164r_sch_g_141_gr.jpg` | se confond avec le sigle χ^ρ (χορός) ; au f. 167v, l. 37, c'est χ^ρ (Velsen ; inv. f167v), et non « γρ. » (Allen). Au v. 126 (164r), « γρ(άφοντες) » reste [à vérifier] |
| 26 | ἄλλ̄, ἄλλ(ως) ; tilde marginal | ἄλλ surligné, ou tilde dans la marge en face de la seconde explication | ἄλλως | 166v (v. 346) ; 168r, l. 41–43 (v. 506) ; 171r, l. 27–31 (v. 747) ; 172r, marge sup. (v. 804–805, tilde) ; 173v, l. 31–35 (v. 948) | `../specimens/f171r/sch_747_abrev_eupolis_allos.jpg` | — |
| 27 † | σύντ(αξις) | σύν + τ suscrit sur une barre horizontale (aspect « T ») | σύνταξις | 173v, l. 25 (ἀττικὴ ἡ σύντ(αξις), v. 942) | `../specimens/f173v/f173v_l25_syntaxis_bande_sigles.png` | tombe dans la bande des sigles, devant γέλωτα : à ne pas prendre pour une paragraphos ni pour un sigle |
| 28 | τ^ου(το), τοῦ^τ(ο), τ(οῦ)τ(ο) | τ surmonté de υ, puis το ; ou τοῦ avec τ suscrit | τοῦτο | 164v (v. 196) ; 168r ; 169v, l. 11 (v. 603) ; 171r, l. 26, 34, 36 (vv. 746, 754, 756) ; 175r, l. 26 (v. 1069) ; 177r, l. 10 (v. 1217) | pl. 2, n° 15 | — |
| 29 | τ̀, τ surligné, τ à crochet | τ surmonté d'un trait, d'un grave ou d'un crochet | τόν, τό, τήν, τάς, τῆς, τῶν | 165v, l. 13 (τ(όν), v. 263) ; 171r, l. 6 (τ(ὰς), v. 726) ; 171v, l. 5–12 (τ(ὸν), v. 771) ; 174v, l. 18–19 (τ̀ = τ(ὸ), v. 1019) ; 175r, l. 6–7 (τ̀ = τ(ὸν), v. 1050) | pl. 2, n° 2 | le crochet se prend pour un accent (inv. f171r) |
| 30 | αὐτ^ου, αὐτ̀, αὐ^τ | lettres suscrites ou accent de suspension | αὐτοῦ, αὐτόν, αὐτῷ | 165v (vv. 254, 261, 289, 290) ; 170v (αὐ^τ = αὐτῷ) ; 174v, l. 1–2 et 23–24 (αὐτ̀ = αὐτ(ὸν), vv. 1003, 1024) ; 177r, l. 16 (αὐτ^ου, v. 1223) | — | — |
| 31 † | ὁδ' | δ suivi d'un accent qui sert de suspension | ὁδόν | 177r, l. 14 et 16 (vv. 1222, 1223) | pl. 2, n° 11 | — |
| 32 | suspensions simples | trait, apex ou apostrophe après la dernière lettre écrite | finale à restituer | 164v, l. 12 (ἔλεγ(ον), σοφιστ(άς), v. 177) ; 170r, l. 12–15 (εἷλκ(ον), ἐκάλ(ουν), v. 648) ; 170v (κροκωτ', παιδί', ἱκε', θυγα', ἔ' = ἔξεστιν) ; 171r (μην(ῶν), οἴν(ου)) ; 172r (Κλεώνυμ(ον), αἰνίττε(ται), v. 829) | pl. 2, n° 16 | le développement se fait d'après le contexte : le noter entre parenthèses |
| 33 † | εὐρι^π | ευρι + π suscrit, à longue barre (parfois en forme de « ΤΤ ») ; ou εὐρι(πίδης), εὐριπ(ίδης) | Εὐριπίδης, -ου, -ην | 163v (v. 93) ; 164v, l. 25 et 28 (vv. 190, 194) ; 165v (v. 272) ; 171v (vv. 770–781) ; 172v (vv. 855, 870, 871) ; 173r (v. 910) ; 175r (vv. 1056, 1059, 1063b) ; 177r, l. 9–12 (v. 1217) | pl. 2, n° 13 ; `../specimens/f164v/mgg_l28_scholie.jpg` | même abréviation que dans les notes de personnage de S2 (§ 5) |
| 34 | ἀγάθ(ων) | θ barré suscrit | Ἀγάθων | 163v, l. 19–30 (vv. 98, 101) | — | même forme que le sigle ΑΓΑ^θ du texte |
| 35 † | χ^ο ; χ bouclé | χ surmonté d'un ο, ou d'une petite boucle | χορός | 164r, marge sup. (v. 125) ; 166r, l. 19 (v. 312) ; 163v (χ^ο(ρὸν), v. 101) ; 175v, l. 9 (v. 1090) ; 177r, l. 9 (v. 1217) | pl. 2, n° 13 | à ne pas lire χ isolé ni sigle (inv. f166r) |
| 36 | autres noms propres et mots fréquents | suspension ou lettre suscrite | — | κηδεστ(ής), τ suscrit barré (169v, v. 633 ; 175r, v. 1063b) ; μνησίλοχ(ος) (165v, v. 266 ; 169v, v. 603) ; Σύμμαχ(ος) (167r, v. 393) ; Σθενεβοί(ας) (167r, v. 404) ; ἀνδρομέδ(ας), δ suscrit et virgule (174v, v. 1018) ; Ἀλέξαν^δ(ρος), Θουκυ^δ(ίδου) (170v, v. 682) ; Ἡσιόδ(οις) (164v, v. 168) ; εὔπ(ολις), π surmonté d'un grand Λ (171r, v. 747) ; παλ(αμήδει) (171v, v. 772) | pl. 2, n° 1 | — |
| 37 | mots surlignés | lettres extrêmes surmontées d'un trait | ἄν(θρωπ)οι ; π(ατέ)ρα | 170v, l. 4 (ἀνοι surligné, v. 682) ; 171v, l. 9 (π̄ρ̄ᾱ, v. 771) ; 172v (v. 840) | pl. 2, n° 2 | abréviations du type *nomina sacra* |
| 38 | chiffres et lettres nommées | lettre surlignée ou suivie d'un apex | nombre ; nom de lettre | 163v, marge sup. (ια΄, ιβ΄, Σ 80 : jours du mois) ; 172r, marge inf. (θ̄ = le 9 de Pyanepsion, v. 834) ; 171v, marge int. (ρ̄, la lettre ρ dont parle la note, v. 781) ; 175v, l. 1 (χωρ(ὶς) τ(οῦ) ε̅, v. 1083) | — | au f. 171r (v. 728), « ἔχει τὸ ᾱ » désigne l'alpha long, non un chiffre (inv. f171r) |
| 39 | lettres écrites au-dessus du mot | voyelle ou syllabe suscrite, faute de place ou par oubli | — | 165v, l. 10–11 (στρ^ῶ^μα, ω suscrit en « ∞ », v. 261) ; 166r, l. 2 (ἐπ^ει^δὰν, v. 295) ; 175r, l. 10 (δαιμόν^ν^ων, v. 1054) ; 177r, l. 9 (ἐμπαίζ^ει, v. 1217) | pl. 4, n° 5 | le « ∞ » se prend pour un signe de renvoi (inv. f165v) |
| 40 | ὅτι | ὅ suivi de τ suscrit ; ligature ο + τι en « ΟΠ » | ὅτι | 166v, l. 27 (« δηλοῖ ἐνταῦθ(α) ὅ(τι) λέγου(σι) », v. 363) ; 174r, l. 10, marge int. (« ΟΠ » = ὅτι, v. 968) | — | d'ordinaire en toutes lettres (165r, v. 231 ; 168r, vv. 501, 505), ce qui concorde avec Martin 1882, xiv : l'abréviation de ὅτι est « rare chez R² » |

### 4.3 Interprétation : quelle « tachygraphie » ?

**Origine des signes.** La plupart des abréviations régulières de la minuscule viennent de la tachygraphie, qui notait la prononciation et non l'orthographe. Un même signe servait donc pour des syllabes homophones : -ην, -ειν et -ιν d'un côté, -ης, -εις et -ις de l'autre (Martin 1882, xvi–xvii). On retrouve ce caractère chez S2 :

- un trait montant note -ιν et -ειν (n° 12) ;
- un même « ʒ » vaut δέ ou -αι / -ται selon sa position (n° 3–4) ;
- le signe de ἐστί, doublé, donne celui de εἰσί (n° 5–6) ;
- κ(αί) prend la forme de la lettre κ telle que S2 la trace (n° 1).

**Ce que je ne trouve pas.** Martin 1882, xviii–xix décrit une « échappée sur le terrain tachygraphique » : des abréviations « purement tachygraphiques », non passées dans la minuscule, du type ὕπξ = ὑπέρ, ὥσπξ = ὥσπερ, et le signe de -ευς. Elles appartiennent toutes au premier scholiaste (R¹), à la fin des *Oiseaux* et au début de la *Paix* ; un seul passage, douteux, est dans la *Lysistrata*. Dans les quelque quatre cents notes des *Thesm.*, ni les inventaires ni mes contrôles n'en relèvent aucune. Le répertoire de S2 est celui de la minuscule commune, abondant mais banal. La seule singularité est la forme graphique de certains signes (ϗ en « Ις », λ̸ à crochet), qui suit la semi-onciale de S2.

**Conséquence pour la transcription.** Une transcription diplomatique doit garder chaque signe tel qu'il est écrit, avec son accent, et noter le développement entre parenthèses. Il faut s'en tenir au contexte pour les signes à double valeur (n° 3–4, 12–13) et signaler en note les développements incertains : γ(άρ) ou δ(έ) au f. 163v (Σ 98) ; « γρ(άφοντες) » au f. 164r (v. 126) ; « πλ^ι » au f. 165r (v. 232).

## 5. Les notes de personnage de S2 : écriture et abréviations

Le système des marques de changement de locuteur est étudié au chapitre 5. On ne retient ici que ce que les notes de personnage de S2 apprennent sur son écriture.

**Répertoire des formes** (inventaires de page ; vérifié sur les ff. 164v, 169v, 170v, 171r, 173v, 175v, 177r) :

| Personnage | Forme chez S2 | Exemples (page, ligne, vers) |
|---|---|---|
| le Parent | μνη^σ, avec σ lunaire suscrit et souvent un trait de fuite oblique sous l'Η ; μνη^σι ; μνησί^λο, ΜΝΗΣΙ^λο | 164v, l. 35 (v. 200) ; 169v, l. 23 et 38 (vv. 615, 630) ; 170r, l. 2 et 13–14 (vv. 637, 650) ; 170v, l. 15, 27, 32, 37 (vv. 692, 704, 709, 714) ; 172v, l. 12 (v. 846) ; 173r, l. 10 (v. 886) ; 174v, l. 21 (v. 1022) ; 162v, l. 20 (v. 19, μνη^σι) ; 163r, l. 4 (v. 45b) ; 164r, l. 9 (v. 130) |
| le Parent | κη^δ : Κ en deux pièces, Η, δ suscrit souligné | 168v, l. 32 (v. 540) ; 169v, l. 11 (v. 603, au-dessus du dicolon de T) ; 176v, l. 40 (v. 1207) |
| Euripide | ευ^ρ ; εὐρι^π, π suscrit à longue barre ; « εὐρι^π ὡς περσεύς », « εὐρι^π ὡς γραῦς » | 164v, l. 37 (v. 202) ; 165r, l. 41 (v. 249) ; 173v, l. 5 (v. 924) ; 174v, l. 14 (v. 1015) ; 175v, l. 17 (v. 1098) ; 176v, l. 9, 13, 41 (vv. 1177, 1181, 1208) |
| Agathon | ΑΓΑ surmonté d'un θ ovale barré (« lentille barrée ») | 163v, l. 22, 28, 35 (vv. 101, 107, 114) ; 164r (v. 146) ; 164v, l. 38 (v. 203) |
| Clisthène | κλεισ^θ, κλε(ι)σ^θ, θ barré suscrit | 169v (vv. 595, 603, 606, 610, 615) ; 170r, l. 10 (v. 645) ; κλει au f. 169r, l. 25 (v. 574), complété en 1516 |
| femmes | γυ^ν (Γ à barre prolongée, Υ en Y, ν suscrit) ; γυ^ν μία ; γυ^νη τίς ; καλλιλεξία γυ^ν ; ἄλλη γυ(νή) | 169v, l. 13 et 34 (vv. 605, 626) ; 170r, l. 16 (v. 652) ; 170v, l. 29 (v. 706) ; 173r, l. 3 et 6 (vv. 879, 882) ; 168v, l. 25 (v. 533, repassé en 1516) ; 167r, l. 4 (v. 383) ; 171r, l. 40 (v. 760) |
| chœur | χ^ο ; monogramme χ traversé par la haste d'un ρ (aspect d'astérisque) | 163v, l. 25 et 32 (vv. 104, 111) ; 166r, l. 19 (v. 312) ; 166v, l. 16 (v. 352) ; 167v, l. 11 et 37 (vv. 434, 459) ; 168v, l. 12 (v. 520) ; 169v, l. 5, 15, 21 (vv. 597, 607, 613) ; 170v, l. 22–23, 28, 38 (vv. 699, 705, 715) ; 173v, l. 30 (v. 947) ; 176r, l. 10 (v. 1136) ; 177r, l. 9 (v. 1217, attribution probable) |
| autres | κη^ρ (héraut) ; σκυ^θ (Scythe) ; ·ΠΡΥΤΑΝΙC ; θερά^π, θερ (serviteur) ; τοξ°της, à l'encre orangée ; ηχω, à l'encre orangée | 166v, l. 36 (v. 372) ; 175v, l. 2–3 (vv. 1083–1084) et 176v, l. 43 (v. 1210) ; 173v, l. 10 (v. 929) ; 162v, l. 39 (v. 39) et 163r (v. 46) ; 174r, l. 43 (v. 1001) ; 175v, l. 2 |

**Ce que ces formes montrent.**

1. **Même écriture, mêmes abréviations que les scholies.** Les notes sont en petites majuscules de semi-onciale : Κ en deux pièces, Η, σ lunaire, θ en lentille barrée. Certaines sont en minuscule fine : μνη^σ dans l'interligne au f. 169v, l. 23 ; μνη^σι au f. 171r, l. 10 ; μνη^σ aux ff. 173r, l. 10 et 174v, l. 21. Les noms sont abrégés comme dans les scholies : εὐρι^π, κηδεστ(ής) avec τ suscrit, μνησίλοχ(ος), χ^ο(ρός), ἀγάθ(ων) avec θ barré suscrit. L'inventaire du f. 163v le constate (« mêmes abréviations dans les sigles et dans les scholies »). C'est l'argument le plus solide pour attribuer ces notes à S2 quand l'encre ne tranche pas.
2. **Ces formes ne sont pas « imprimables ».** Les abréviations de S2 étaient inutilisables pour un compositeur (Velsen 1871, 8, d'après le dossier, § 5.4) ; la main de 1516 les double ou les remplace par μν, εὐ, γυ, κηδ, σκ, Ηχ, χο. La forme suffit à séparer les deux systèmes, même quand l'encre est orangée dans les deux cas (§ 2.6).
3. **Place.** S2 écrit ses notes dans la bande des sigles (x ≈ 590–800), à gauche de la paragraphos de T ou à sa place. Pour une réplique qui commence au milieu d'un vers, il les écrit dans l'interligne, au-dessus du dicolon de T (169v, v. 603 ; 170r, v. 650 ; 169v, v. 615). Il les écrit donc après les marques de T.
4. **Pièges.** Le θ barré suscrit de αγα^θ ressemble à un ÷ ou à un + (164v, l. 38). Le monogramme χ + ρ ressemble à un astérisque (169v, 170v). La fin d'une note de personnage se colle au bout d'une ligne de scholie (170v, l. 11 et 15). Le σ suscrit de μνη^σ se loge dans le γι de la ligne au-dessus (169v, l. 22–23). Inversement, une fin de scholie qui arrive dans la bande des sigles passe pour une note de personnage (§ 6, n° 10).

## 6. Difficultés de lecture propres aux scholies

Les pièges de l'écriture de T sont traités au chapitre 2. Voici ceux qui tiennent à la main S2 et à la position des notes. Les numéros renvoient aux vignettes de la planche 4 (`../planches/ch3_pl4_pieges.jpg`) et de la planche 2.

| # | Piège | Exemples (page, ligne, vers) | Règle de lecture |
|---|---|---|---|
| 1 † | ΛΛ lié en « Μ », et Μ qui ressemble à ΛΛ | ἀπόλλων(ος) lu « ἀπόμων » (166r, l. 34, v. 327) ; ἀλλὰ μὰ ταῖν θεαῖν (169r, marge sup., v. 566) ; καλλιλεξία lu « καμιλεξία » (167r, l. 4) ; προβάλλει, πολλὰ, διαβάλλεται, αἰκάλλει (172v) ; τὸν ἀπόλλωνα (174r, l. 11) ; διαβάλλεται, et inversement δημήτηρ (177r, l. 6 et 22) | se fier au sens et comparer avec les Μ sûrs de la même note (pl. 4, n° 1 ; pl. 2, n° 14) |
| 2 † | Ν à diagonale presque horizontale, pris pour Η | ναῖκας lu « ηαικας » (171r, l. 6) ; ν suscrit en Ν pris pour un Η (165v, l. 12, ὀῦ^ν) ; Ν de S2 proche de Η (168r, l. 26–27 ; 175r) | comparer avec les Ν et les Η sûrs de la même note ; l'Η de S2 a souvent la barre haute (inv. f163v) (pl. 4, n° 2) |
| 3 | Κ en deux pièces (« Ις », « ιc ») lu comme deux lettres | κίνησιν (166r, l. 31) ; σκυ^θ lu « ϲικυ » (176v, l. 43) ; κ en « ιc » (177r) | une haste suivie d'un C ouvert vaut κ |
| 4 | ξ en Z à queue, proche de ζ | ξιφομάχαιρα (176r, l. 1) ; ἐσπάραξαν (172v) ; v. 329 (166r) ; καλλιλεξία (167r) | trancher d'après le sens ; S2 écrit ξ comme un ζ |
| 5 † | ϗ en « Ις » ou « ιʒ », lu comme des lettres | εἰς, ἰξ ou ἐξ au lieu de καί (171v, 176v, 167v, 164v, 165v) | entre deux mots, ce groupe vaut καί (§ 4, n° 1) |
| 6 † | « ʒ » à triple valeur | δέ quand il est isolé, -αι ou -ται quand il est attaché (165v, 166r, 177r) ; au f. 175r, λ̸ = λείπει lu « ʒ » (inv.) ; δέ lu ἤ (inv. f165r, v. 231) | décider par la position ; vérifier si le premier trait est un Λ (λείπει) |
| 7 † | quatre signes en obèle | ÷ final (obèle droit pointé) ; ·/· = ἐστί (oblique pointé) ; ·//· = εἰσί ; ·/· ou ÷ ondulé pour un renvoi (170r, l. 11–12) ; et le signal ÷ de T, rare dans la pièce (f. 162v, v. 4, sous une forme inclinée ; peut-être les ÷ ondulés du v. 647, f. 170r) | dans une ligne de scholie, l'oblique pointé entre deux mots vaut ἐστί ; en fin de note, l'obèle vaut clôture |
| 8 | -ος réduit à un point, ou en petit signe bouclé | ἀπόλλων(ος) (166r, l. 34) ; εἶδ(ος) d'abord lu « ἐκ δ(ὲ) » (163v, l. 14) ; ο de ἀπὸ en forme de « e » (166r, l. 19, `../specimens/f166r/f166r_l19_scholie_apo_omicron_en_e.jpg`) | un point au-dessus de la dernière lettre d'un mot tronqué note une terminaison, non un esprit |
| 9 | ι adscrit ou ponctuation | petits traits hauts après πεζῆ et après γῆ, τῆ, ἑστία (166r, l. 2 et 7–9 : ι adscrits selon Rutherford) | S2 écrit l'ι adscrit (φυλάξηι, πυλάξηι, τῆι ἑλένηι, κωμωδίαι, 174v ; ἡλίωι, 163r) : noter le signe tel quel |
| 10 † | note placée au bord de la colonne et rattachée au texte, ou prise pour un sigle | « ·ἀεὶ γ(ὰρ) », début de Σ 93, sur la ligne même du v. 93 (163v, l. 14) ; « …ἅτε εὐρι^π ÷ » au bord de la l. 12 (171v), d'où vient sans doute le « ευρί^π ὦ » de G au v. 776 (inv. f171v ; pl. 4, n° 3) ; σύντ(αξις) en « T » dans la bande des sigles (173v, l. 25) ; ÷ dans la bande des sigles (174v, l. 29–30 ; 167v, l. 36 ; 172v, l. 16) ; fins de scholies relevées comme « sigles » par la segmentation automatique (168v, 174v) | toute écriture de petit module en semi-onciale appartient aux scholies, même si elle touche la colonne |
| 11 | tiret d'ouverture et paragraphos de T | trait final de la scholie au v. 600, ou paragraphos du v. 601 (169v, l. 9 : paragraphos selon la correction de l'inv.) ; paragraphoi des vv. 617–618 en bout des lignes de la scholie au v. 616 (169v) ; paragraphos soudée à la glose χωροῦν (171r, l. 24) ; tiret de S2 croisé par un μ de 1516 (172v, l. 30) | un trait en massue placé entre x ≈ 650 et 725, à mi-hauteur d'une ligne du texte, est a priori une paragraphos de T (inv. f169v) ; un tiret plus mince, en tête d'une ligne de scholie, est de S2 |
| 12 | lemme ou citation qui diffère du texte | voir la liste du § 3.5 (οἰνοπίπας et οἰνοπότιδας, ἰφύων et ἀφύων, πέπαικτ(αι) et πέπυσται…) | ne jamais aligner le texte de R sur la scholie, ni l'inverse ; ces écarts vont à l'apparat |
| 13 † | altérations matérielles | réactif bleu-vert ou gris-bleu qui noircit les débuts ou les fins de ligne (162v, 164v, 165r, 165v, 166v, 168v, 170v, 171r, 174v, 177r ; pl. 4, n° 4) ; bandes d'humidité qui effacent les débuts de ligne (168v, 172v, 176v : restitution d'après Enger, Dübner ou Rutherford, à signaler) ; tulle (165v) ; pièces de restauration (169r, 171r) | une lettre noircie par le réactif n'est ni une autre encre ni une correction (inv. f168v) ; lire sur le canal bleu ou rouge |
| 14 | transparence et décalque | scholie du f. 169r vue au verso (169v, marge sup.) ; décalque des scholies du f. 172v (173r, marge ext.) et du f. 176v (177r, marge ext.) ; transparence du f. 176v (176r) et du f. 168v (168r) | ne pas transcrire ; contrôler en retournant l'image en miroir (méthode de l'inv. f177r) |
| 15 | changement d'écriture dans une même note | passage à la minuscule en fin de ligne (175r, l. 10) ; lemmes en capitales dans une note en minuscule (162v) ; supplément mixte (175v) | ne pas en conclure à un changement de main |
| 16 | mesures d'encre trompeuses | dans la tache du f. 175v, les scholies brunes mesurent « orangé » (1,40–1,45 ; 2,76–3,02) ; les traits fins mesurent « gris » (169v, 174r) ; la notice du haut du f. 162v est plus jaune | comparer avec un témoin de la même zone (§ 2.6) |

## 7. Confrontation avec la littérature

| Auteur | Affirmation | Ce que montrent les images et les inventaires | Verdict |
|---|---|---|---|
| Martin 1882, xiv | R² (S2) a écrit les scholies des *Thesm.* ; R³ et R⁴ n'y ont qu'une part « des plus faibles » | toutes les notes sont de S2, sauf deux au f. 162v (§ 2.4) | confirmé |
| Martin 1882, xiv | l'abréviation de ὅτι est rare chez R² | ὅτι est presque toujours écrit en toutes lettres ; ὅ(τι) une fois au f. 166v, la ligature « ΟΠ » une fois au f. 174r | confirmé |
| Martin 1882, xvi–xvii | un même signe sert pour -ην, -ειν, -ιν, un autre pour -ης, -εις, -ις | trait montant pour -ιν et -ειν chez S2 (166r, 174v) | confirmé (petit nombre de cas) |
| Martin 1882, xviii–xix | abréviations « purement tachygraphiques », toutes chez R¹ (*Oiseaux*, *Paix*) | aucune dans les *Thesm.* | confirmé par défaut |
| Martin 1882, 196 | v. 25 : « πρόσεχε… main ordinaire de R² ; au-dessous, à moitié effacé…, le vers 28, qui manque au texte » | πρόσεχε est bien de S2. La ligne effacée existe : c'est la bande bleuie de la l. 28, une ligne de minuscule que je ne lis pas. Mais le v. 28 ne manque pas au texte : T l'a copié après le v. 30 (lettres α–δ) | à moitié confirmé (§ 8, n° 7) |
| Martin 1882, 208 | « 1151. Ὅπου. Main du texte » | semi-onciale de S2 (176r, l. 28) | infirmé |
| Zacher 1888, 534–535 | réglure des espaces de scholies ; marge intérieure non réglée, dont les notes « erscheinen … mehr als glossen » | S2 écrit surtout dans les marges ext. et int. ; la marge intérieure reçoit les gloses et les notes courtes, avec des exceptions (§ 3.1) | confirmé |
| Zacher 1888, 536 | S2 ne marque pas les lemmes, sépare mal ses notes ; ses scholies forment une masse continue | lemmes non marqués, blocs continus ; mais tirets d'ouverture et ÷ de clôture fréquents | à nuancer |
| Zacher 1888, 538 | lemmes à la seule première page des *Thesm.*, puis « nur vereinzelt » | lemmes réguliers au f. 162v, sporadiques ensuite | confirmé |
| Rutherford 1896, I, xxvii | S2 accentue ses compendia ; il se fie en général au lemme et n'emploie que « now and again » un signe de renvoi | compendia accentués (ὁδ', αὐτ̀, τ̀, κ̀) ; renvois rares et motivés (§ 3.6) | confirmé ; c'est la description la plus juste |
| Rutherford 1896, I, xxviii | S2 termine ses notes par un point haut, mais vers le v. 100 des *Thesm.* par « :— » | point simple au f. 163r ; ÷ ou :– ensuite, et déjà au f. 162v | confirmé, avec l'exception du f. 162v |
| Allen 1896, 320–321 | la minuscule du f. 162v est un « experiment » de B ; même teinte d'encre | vrai pour la marge sup. et la marge ext. ; faux pour les deux scholies de la marge int. (§ 2.4) | à moitié confirmé |
| Allen 1896, 316 | v. 28 « om. T, add. in marg. B in minusc. [This v. has perished, and been partly revived] » | le v. 28 est dans la colonne, transposé ; il existe pourtant une ligne de minuscule « ravivée » au réactif dans la marge extérieure (§ 8, n° 7) | à revoir |
| Allen 1896, 317 | v. 1102–1103 : « the sign … has been erased by Giunta » | les deux signes « +: » sont visibles (175v) | infirmé, ou il s'agit d'un troisième signe gratté (§ 10) |
| Orsini 2011, 327 n. 24 | une troisième main contemporaine, en minuscule, écrit la scholie au v. 32 (marge intérieure du f. 162v) | confirmé : la minuscule des vv. 27 et 30–32 n'est pas celle de S2 ; elle a l'alphabet de T | confirmé ; identité avec T à éprouver |
| Orsini 2011, 328 | S2 : ni lemmes, ni séparations, ni renvois ; marges ext. et int. seulement | lemmes rares, séparations et renvois réels mais rares ; marges sup. et inf. occasionnelles | à nuancer |
| Invernizi 1794, I, xi (d'après le dossier, § 8.3) | des « lineolae » qui font office de signes critiques sont en fait des renvois vers les scholies | les renvois de S2 sont des signes figurés (∈, ·϶·, ✕, ·×·, ·✓·), mais un trait relie aussi une note à son vers au f. 166v (v. 339) et peut-être au f. 175r (v. 1056) ; les longs traits qui partent de la fin du vers au f. 165r jouent le même rôle | plausible |

## 8. Corrections apportées aux inventaires de page

Tous les points ci-dessous ont été vérifiés sur l'image ; les découpes sont dans `.travail/chap3/vues/` et, pour la plupart, sur les planches.

1. **f. 175r, l. 10 (v. 1054) et l. 30 (v. 1072).** Le signe initial des deux notes n'est pas un « ʒ (ἤγουν ?) ». C'est λ̸ = λείπει, de même forme que celui du f. 168r, l. 20 (pl. 2, n° 8–9). Martin 1882, 207–208 lit « Λείπει » dans les deux cas ; Rutherford traduit « supply ». Lire : λ(είπει)· ἔσχον ἐκ τῶν δαιμόν^ν^ων τὰ ἄχη ἔσχον ÷ ; λ(είπει) μέλλουσα τυχεῖν.
2. **f. 165r, l. 22–25 (v. 231).** Le passage « ζειν· ἢ ·/· τὸ τοῖς μυκτῆρσι… » se lit μύζειν δ(έ) ·/· (= ἐστι) τὸ τοῖς μυκτῆρσι…. Le « ἢ » est le « ʒ » de δέ ; ·/· est le compendium de ἐστί (pl. 4, n° 4). Martin 1882, 199 donne « μύζειν δέ ἐστι τὸ τοῖς μυκτῆρσι ».
3. **f. 163v, l. 17 (v. 96).** Le « sigma pointé, signe de renvoi » est la finale -ος de οὑκκυκλούμενος : grand C qui enferme un ο, suivi d'un point, comme au f. 164r, l. 40 (pl. 3, n° 5a–5b). La page n'a aucun renvoi, et l'entrée « piège » qui parle d'un « -ος semblable à un ρ » vise en fait le ν de T à jambage plongeant. Le résumé du f. 163v est à corriger dans le même sens.
4. **f. 167r, l. 1–3 (v. 380).** Le « compendium en θ barré [à identifier] » n'est pas un compendium : c'est le θ de S2, à barre débordante, dans στεφανοῦ(σ)θαι et dans περί|θου (pl. 4, n° 6). Dübner 1842 donne le texte : « ἔθος γὰρ ἦν τοῖς λέγουσι στεφανοῦσθαι πρῶτον. τὸ δὲ περίθου, ὅπερ ἡμῖν σύνηθες ἐπίθου λέγειν ». Le premier mot se lit ἀντὶ τὸν, comme chez Martin 1882, 200 (« Ἀντὶ τὸν στέφανον »), là où Dübner a ἀντὶ τοῦ.
5. **f. 171r, marge int.** Les gloses πρὸ(ς) τ(ὰς) γυναῖκας, σπινθῆρ(α), ὦ μέθυσοι et τρεῖς κοτύλας οἴν(ου) χωροῦν ne sont pas en « petite minuscule droite ». Ce sont de petites majuscules droites, avec quelques formes minuscules (ω, ρ), comme les gloses du f. 164v (pl. 1, i–j).
6. **f. 176r, l. 28.** L'inventaire attribue la glose ὅπου à « S2 probable ». C'est juste, contre Martin 1882, 208 (« main du texte ») : Π à barre débordante, Υ en Y, aucune forme de T (pl. 1, l).
7. **f. 162v, marge ext., l. 28.** L'inventaire ne lisait que « ὑπὸ … » dans la ligne de minuscule teintée de bleu-vert, sous πρόσεχε. Le dossier (`recherche/ravennas_dossier.md`, §§ 0, 5.3, 11, 12) et l'inventaire en concluent que la notice d'Allen sur le v. 28 (« perished, partly revived ») « convient au v. 33 », et qu'il n'existe « aucune copie marginale ». Or Martin 1882, 196 situe au même endroit (« au-dessous » de πρόσεχε, marge extérieure) une ligne « à moitié effacée et presque illisible » qu'il prend pour le v. 28. C'est exactement la ligne ravivée par le réactif. Le v. 28 est bien dans la colonne, transposé après le v. 30, et Martin comme Allen se trompent en le disant omis. Mais la ligne marginale existe, et on ne peut pas exclure que ce soit un doublet du v. 28 écrit par S2. Elle reste illisible sur la photographie, même sur les canaux rouge et bleu, même après rehaussement de contraste. Le fac-similé de 1904 la montre déjà aussi effacée, à une résolution plus faible ; Allen la disait déjà « partly revived » en 1896. Il faut la lire aux UV avant de trancher.
8. **f. 162v, l. 26 (glose πρόσεχε).** Je lis ἀν^τ τ^ου μνῆσαι, comme Martin 1882, 196, plutôt que νοῆσαι (inv. f162v). Le fac-similé de 1904 (`ravennas_1904_bnf/Ravennas_1904_f162v_Thesmophoriazusae_vv1-42.png`), où la glose est nette, confirme ΜΝΗCΑΙ.
9. **f. 164v, marge sup. et l. 12–14.** Le ϗ « en S couché avec point » est la même forme « Ις » que celle de S2 sur les autres pages : κ en deux pièces suivi d'une queue (pl. 2, n° 1 et 16). Il n'y a pas deux formes de καί chez S2, mais des réalisations plus ou moins liées d'une seule.
10. **Variantes de description d'un même signe**, à unifier dans le guide des transcripteurs : « ϶ » au f. 174v et « ʒ » ou « δ en ʒ + apostrophe » ailleurs désignent le même compendium de δέ ; « τ̆ » (f. 170r, f. 174v) est τ surmonté du signe de ου ; « ʹ/ » et « ʒ' » pour ἐστί (f. 165v) sont des formes réduites de ·/·.

## 9. Planches

Les quatre planches sont générées par `outils/graphologie/planches_chap3.py`. Chaque vignette y est découpée dans l'image pleine résolution de la page, à des coordonnées en pixels écrites dans le script, agrandie de ×1,4 à ×3,5 et légendée.

- **Planche 1** (`../planches/ch3_pl1_ecritures.jpg`) — Les écritures des notes marginales. (a) Notice de la marge supérieure du f. 162v ; (b) minuscule de S2 à lemme oncial ΑΚΟΥΕΙΝ, 162v ; (c) minuscule ronde de la marge intérieure, 162v (troisième main) ; (d) texte de T, 162v, l. 30, pour comparaison ; (e) v. 33 suppléé par S2, 162v ; (f) vv. 1102–1103 suppléés par S2, 175v ; (g) semi-onciale de S2, 162v, marge inf. ; (h) semi-onciale plus droite, 174v ; (i–j) petites majuscules des gloses, 171r ; (k) ζωνάριον en minuscule, 164r ; (l) ὅπου, 176r.
- **Planche 2** (`../planches/ch3_pl2_abreviations.jpg`) — Abréviations et signes tachygraphiques. (1–2) ϗ ; (3) δ(έ) isolé et ἐστί réduit ; (4–5) -ται / -αι attachés ; (6) ·/· = ἐστί ; (7) ·//· = εἰσί ; (8–9) λ̸ = λείπει (168r, 175r) ; (10) ἀν^τ τ̆ ; (11) φ^η et ὁδ' ; (12) γρ(άφεται) ; (13) χ^ο, εὐρι^π, ἐμπαίζ^ει ; (14) -ος en point et ΛΛ en « Μ » ; (15) τ^ȣ ; (16) ϗ, π^ε, suspensions, ÷.
- **Planche 3** (`../planches/ch3_pl3_renvois.jpg`) — Délimitation et renvois. (1a–1b) ∈, 164r ; (2a–2b) ·×·, 169r ; (3) —+:—, 175v, à côté de la finale -ος de γοργόνος ; (4) tiret initial, ϗ et clôture, 167v ; (5a–5b) faux renvoi : la finale -ος de T, 163v et 164r.
- **Planche 4** (`../planches/ch3_pl4_pieges.jpg`) — Pièges. (1) ΛΛ = « Μ » ; (2) Ν = « Η » ; (3) fin de scholie prise pour un sigle ; (4) réactif et ·/· ; (5) λ(είπει), passage à la minuscule, lettre suscrite ; (6) θ à barre débordante.

Spécimens des inventaires les plus utiles pour ce chapitre (dossier `../specimens/`, non versionné) : `f162v/f162v_comparaison_mains_scholies.png`, `f162v/f162v_marge_g_lemmes_onciaux.png`, `f162v/f162v_marge_d_scholie_epeide.png`, `f164r/f164r_renvoi_e_texte_l05.jpg`, `f164r/f164r_renvoi_e_scholie_l07.jpg`, `f164r/f164r_l10_renvoi.jpg`, `f164r/f164r_renvoi_x_scholie.jpg`, `f164v/haut_kai_hesiod_abrev.jpg`, `f164v/mgg_l13_signe_final_scholie.jpg`, `f165v/f165v_sch254_ext.jpg`, `f165v/f165v_sch276_278_ext.jpg`, `f165v/f165v_sch261_int_klinis.jpg`, `f166r/f166r_l31_scholie_de_compendium.jpg`, `f166r/f166r_l34_scholie_apollonos_lambda.jpg`, `f166v/f166v_sch_g_373_esti.jpg`, `f166v/f166v_l34_renvoi_glose.jpg`, `f168r/f168r_l20_glose_leipei.jpg`, `f169r/renvoi_l15_texte.jpg`, `f169r/renvoi_l15_scholie_l1.jpg`, `f170r/f170r_renvois_l12_m647_l11.jpg`, `f171v/f171v_scholies_bloc1.jpg`, `f171v/f171v_euripi_fin_scholie_l12-13.jpg`, `f173v/f173v_sch_935_marge_g.png`, `f173v/f173v_l25_syntaxis_bande_sigles.png`, `f174v/f174v_sch1003_marge_g_l1-2.png`, `f175r/f175r_gl_l30_ellousa.png`, `f175v/f175v_l20_signe_renvoi.jpg`, `f175v/f175v_margeinf_signe_renvoi.jpg`, `f176r/f176r_glose_l28_opou.jpg`, `f176v/f176v_sch_v1203_kai_compendium.jpg`, `f177r/f177r_glose_l22_demeter.jpg`.

## 10. Questions ouvertes

1. **La minuscule de la marge intérieure du f. 162v** (vv. 27, 30–32) : T qui écrit en lettres détachées, S1 (le scholiaste des premières pièces), ou troisième main contemporaine ? Le premier essai sur le f. 14r (§ 2.4) la rapproche de la restitution de Ploutos 1129–1130 dans la marge supérieure. Il faut reprendre la comparaison à pleine résolution (images IIIF de la Classense, ou fac-similé de 1904) sur les ff. 4r, 6v et 14r : le PDF intégral du dépôt ne donne qu'environ 0,2 mm par pixel.
2. **La ligne ravivée du f. 162v** (marge extérieure, l. 28) : doublet du v. 28 de la main de S2, ou scholie ? Lecture aux UV ou en imagerie multispectrale (§ 8, n° 7).
3. **Les notes de personnage de la forme de S2 à l'encre orangée** (170r, 171v, 172v, 174r, 175v) : seconde encre de S2, main médiévale imitatrice, ou sigles bruns repassés en 1516 ? Il faut chercher une double couche aux UV et confronter systématiquement avec le Monacensis gr. 492.
4. **Le signe gratté « by Giunta »** pour les vv. 1102–1103 (Allen 1896, 317) : les deux signes « +: » étant visibles, Allen visait-il un troisième signe, gratté dans la colonne ?
5. **Développements incertains** : γ(άρ) ou δ(έ) dans la Σ 98 (163v) ; γρ(άφοντες) au v. 126 (164r) ; πλ^ι au v. 232 (165r) ; le petit signe final de πέπαικτ(αι) (177r, l. 20) ; φη(σί) ou φασί au v. 852 (172v).
6. **Renvois incertains** : le trait sous κηφέα (175r, l. 12) ; la « flèche » du f. 171v (l. 18) ; la croix marginale du f. 175r (l. 20/21) et celle du f. 173v (l. 7), qui n'ont pas de répondant.
7. **Gloses et scholies : une ou deux campagnes ?** Aux ff. 167r, 167v, 168r et 163v, les gloses de la marge intérieure n'ont pas l'encre des scholies de la marge extérieure. Il faudrait étendre la mesure à densité égale (outil `.travail/graphologie/f168r_inv3/densite.py`) à toutes les pages.
