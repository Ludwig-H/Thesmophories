# f175r (vv. 1045–1081) — répartition commentaire critique / commentaire de la pièce

État : **terminé** — 15 articles : 6 CRITIQUES (déplacés en entier), 2 MIXTES (scindés), 7 PIÈCE (restés
au commentaire) ; `critique.tex` compte donc 8 articles `\cc`, `commentaire.tex` 9 articles `\comm`.
Le folio compile (`./edition/compiler_folio.sh f175r` : 7 pages, sans erreur ; quatre boîtes trop pleines
de 1 à 9 pt dans les colonnes étroites, préexistantes).
Contrôles : `.travail/repartition/f175r/verifier.py` (réunion `\cc` + `\comm` = articles d'origine, aux
modifications déclarées près : « TOUT EST CONFORME ») et `outils/controle/repartition_commentaire.py f175r`
(mots perdus = uniquement les corrections déclarées ci-dessous).

Source : `edition/folios/f175r/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex`, l. 4231–4547 ; passages désactivés
examinés sur toute l'étendue du folio, l. 4183–4560).
Règles : `edition/CONVENTIONS.md` § 3 et § 7. Articles critiques : `critique.tex` (`\cc`) ;
commentaire de la pièce : `commentaire.tex` (`\comm`). Rien n'est supprimé. Copie de l'original :
`.travail/repartition/f175r/commentaire.orig.tex` (non versionné ; identique à la révision git db90b04).

## Articles

| n° | Plage | Lemme (abrégé) | Classement | Action | Avancement |
|---|---|---|---|---|---|
| 1 | 1054–5 | λαιμότμητ᾽ ἄχη δαιμόνων … | CRITIQUE (leçon δαιμόνων de R, correction δία μένων de Willems retenue) | déplacé en entier dans `critique.tex` (`\cc{1054–5}`), inchangé | fait |
| 2 | 1059 | ἀντῳδὸς ἐπικοκκάστρια | PIÈCE (note de Willems : épigramme d'Archias ; note de l'éditeur sur l'oiseau) | reste dans `commentaire.tex` ; 1 coquille corrigée | fait |
| 3 | 1059 | Ἠχὼ λόγων ἀντῳδὸς ἐπικοκκάστρια | MIXTE (Écho dans l'*Andromède*, mise en scène, sens d'ἐπικοκκάστρια, scholies, polémique contre Austin–Olson : PIÈCE ; exemple du v. 1094 — lacune comblée par la scholie, leçon et attribution de R, répartition des répliques chez les éditeurs, Wilamowitz / Sommerstein — et principe de reconstruction des répliques d'Écho et des *cruces* : CRITIQUE) | scindé : le paragraphe « Il est étonnant que les modernes éditions… » jusqu'à « … Εὐριπίδης : « οὐχ αἱρήσεις ». » (avec ses notes 5 et 6) et le dernier paragraphe « C'est -- reconnaissons-le -- … ne pas avoir démérité d'Aristophane. » → `critique.tex` (`\cc{1059}`, lemme d'origine), précédés de « Pour le sens d'ἐπικοκκάστρια, voir le commentaire de la pièce. » ; le reste demeure dans `commentaire.tex`, avec « Pour le texte, voir le commentaire critique. » à la place du paragraphe déplacé (avant « Bref ! ») ; 1 « nous » → « moi » (commentaire), 6 « nous » → « je » (critique) ; 5 coquilles corrigées (dont 2 esprits dans la scholie citée, corrigés à la reprise) | fait |
| 4 | 1060 | πέρυσιν | PIÈCE (date de l'*Andromède*, scholie) | reste dans `commentaire.tex`, inchangé | fait |
| 5 | 1063 | σὲ δ᾽ ἐπικλάειν ὕστερον | PIÈCE (sens du préfixe ἐπι-, menace de Mnésiloque) | reste dans `commentaire.tex`, inchangé (lemme : voir les passages signalés) | fait |
| 6 | 1065–72 | ὦ νὺξ ἱερὰ κτλ. | PIÈCE (début du prologue de l'*Andromède* d'après la scholie ; anapestes de lamentation : description du mètre, sans discussion de colométrie) | reste dans `commentaire.tex`, inchangé | fait |
| 7 | 1067 | ἀστεροειδέα νῶτα | PIÈCE (note de Willems : sens) | reste dans `commentaire.tex`, inchangé | fait |
| 8 | 1069 | τοῦ σεμνοτάτου δι᾽ Ὀλύμπου; --- δι᾽ Ὀλύμπου | CRITIQUE (rétablissement de la réplique d'Écho : méthode, glose d'Hésychius ο 649 ὀλυμπία· δοκός à l'appui de la conjecture « †δι᾽† ὀλυμπίας Bibi » de l'apparat de l'auteur, *crux* ; tentation, écartée, de corriger le vers d'Andromède en Ζεὺς Ὀλύμπιος ; tous les parallèles servent l'argument) | déplacé en entier dans `critique.tex` (`\cc{1069}`) ; 4 « nous » → « je » ; 7 coquilles corrigées (dont 2 accents graves, corrigés à la reprise) | fait |
| 9 | 1071 | μέρος ἐξέλαχον; | MIXTE (conjecture μόρος ἔξελ᾽ ἄχος de Bibi, avec ses deux notes — aoriste gnomique, μόρος = θάνατος chez les lexicographes : CRITIQUE ; sens de la réplique, scholie κακοστένακτος, parallèles gnomiques — Sophocle fr. 698 Radt, La Fontaine : PIÈCE) | scindé : la phrase d'introduction et la citation « μέρος ἐξέλαχον --- μόρος ἔξελ(ε) ἄχος / La Mort extirpe la douleur » → `critique.tex` (`\cc{1071}`), suivies de « Pour le sens et les parallèles, voir le commentaire de la pièce. » ; « Andromède se plaint… » et les parallèles demeurent dans `commentaire.tex`, précédés de « Pour le texte, voir le commentaire critique. » ; inchangé par ailleurs | fait |
| 10 | 1072 | θανάτου τλήμων… | PIÈCE (parodie : fin du vers original de l'*Andromède* connue par la scholie λείπει « μέλλουσα τυχεῖν » ; aucune discussion du texte d'Aristophane) | reste dans `commentaire.tex`, inchangé | fait |
| 11 | 1073–5 | ὦ γραῦ στωμυλλωμένη — στωμυλωμένη — νὴ Δί᾽ | CRITIQUE (deux graphies de R, -λλ- au v. 1073 et -λ- au v. 1074 ; conjecture στωμυλιομενής de Bibi : morphologie, composé des *Grenouilles*, appui de la concessive du v. 1075) | déplacé en entier dans `critique.tex` (`\cc{1073–5}`) ; 2 « nous » → « je » ; 1 coquille corrigée | fait |
| 12 | 1078 | καὶ χαριεῖ μοι παῦσαι --- παῦσαι | CRITIQUE (conjecture ᾽παΰσαι de Bibi pour la réplique d'Écho : sens, ἐπαΰω chez Eschyle, appui du contexte — l'emportement de Mnésiloque au v. 1079) | déplacé en entier dans `critique.tex` (`\cc{1078}`), inchangé | fait |
| 13 | 1079 | βάλλ᾽ ἐς κόρακας — βάλλ᾽ ἐς κόρακας | CRITIQUE (conjecture βάλλε σύ κόρακας de Bibi pour la réplique d'Écho : l'imprécation ἐς κόρακας et ses emplois chez Aristophane, digression sur *Nuées* 133 — lecture Βάλλε κόρακας, κόρακες « marteaux de porte » —, application au passage ; tout l'article sert la conjecture) | déplacé en entier dans `critique.tex` (`\cc{1079}`) ; 1 « nous » → « je » ; 1 coquille corrigée (voir aussi les passages signalés : le commentaire de la pièce n'a plus de note sur le v. 1079) | fait |
| 14 | 1080 | τί τὸ κακόν; | CRITIQUE (leçon de R *contra metrum*, suppression de τὸ par Bentley rejetée, usage d'Aristophane, polémique sur le v. 1085, *crux*) | déplacé en entier dans `critique.tex` (`\cc{1080}`) ; 1 « nous » → « je » ; 1 coquille corrigée | fait |
| 15 | 1080–2 | τί τὸ κακόν; […] ὀτότυζ᾽ | PIÈCE (jeu de scène : Euripide-Écho près de Mnésiloque, voile, envol par la μηχανή ; iconographie) | reste dans `commentaire.tex` ; 1 coquille corrigée | fait |

## « nous » d'auteur changés en « je »

- 1059 (Ἠχὼ…, partie restée au commentaire) : « le préfixe ἐπι- apporte **selon nous** sa nuance
  d'hostilité » → « **selon moi** ».
- 1059 (Ἠχὼ…, partie critique), note sur les indications de personnages : « Von Velsen […] ne les fit
  pas apparaître dans son apparat critique. **Nous l'avons suivi** en cela. » → « **Je l'ai suivi** en
  cela. » (décision de l'éditeur ; voir aussi les passages signalés).
- 1059 (Ἠχὼ…, partie critique), dernier paragraphe : « lorsque l'ἐπικοκκάστρια d'une réplique **nous
  est** demeurée celée, et que malgré **nos** efforts les seules propositions que **nous avions** à
  présenter […], **nous lui avons apposé** la *croix du désespoir* †.. Charge à d'autres de compléter
  **notre** ébauche ! je pense, pour ma part, … » → « **m'est** demeurée celée », « malgré **mes**
  efforts », « que **j'avais** à présenter », « **je lui ai apposé** », « compléter **mon** ébauche »
  (l'éditeur seul a fait les propositions et posé les *cruces* ; la phrase s'achève d'ailleurs sur
  « je pense, pour ma part »).
- 1069 (désormais dans `critique.tex`) : « En bonne rigueur philologique, **nous devons nous
  demander** sur quels éléments probants s'appuyer dans **notre** aventureuse entreprise de
  rétablissement de l'*Urtext* » → « **je dois me demander** […] dans **mon** aventureuse
  entreprise » ; « encore faut-il apporter des indices de ce que **nous avançons** » → « de ce que
  **j'avance** » ; « **Nous avons** déjà évoqué des bribes de scholies » → « **J'ai** déjà évoqué » ;
  « Hésychius […], dont **nous avons** assez montré toute l'importance » → « dont **j'ai** assez
  montré » (l'éditeur parle de son propre travail : rétablissement du texte, dépouillement
  d'Hésychius).
- 1073–5 (désormais dans `critique.tex`) : « c'est ce que **nous allons** tenter de montrer » →
  « ce que **je vais** tenter de montrer » ; « **Notre** conjecture est renforcée » → « **Ma**
  conjecture » (στωμυλιομενής est une conjecture de l'auteur, « Bibi » dans son apparat).
- 1079 (désormais dans `critique.tex`) : « Dans **notre** entreprise fort périlleuse de dénicher des
  jeux de mots tout au long de ce passage » → « Dans **mon** entreprise » (la recherche des jeux de
  mots qui fonde les conjectures est celle de l'éditeur) ; gardé : « qui va **nous** permettre de
  reprendre haleine » (le lecteur est associé).
- 1080 (désormais dans `critique.tex`) : « et pour **notre** part **nous nous résignons** à
  *crux*-désespérer † » → « pour **ma** part **je me résigne** » (décision de l'éditeur).
- Gardés (« nous » qui associe le lecteur ou désigne les lecteurs et philologues en général) : au
  commentaire de la pièce, « notre comédie », « notre `cocasse' », « nos traditions orales », « Le
  scholiaste nous est ici précieux », « un avantage indéniable sur nous », « Aristophane nous
  prévient », « nous dit lui-même », « notre poète », « le sel attique nous en a échappé », « Une autre
  scholie nous permet », « Nous savons par une scholie », « l'iconographie qui nous fournit la
  réponse » ; au commentaire critique, « une scholie nous indiquait », « notre pièce », « notre
  scribe », « qui va nous permettre de reprendre haleine », « notre « [va] au diable ! » », « le passage
  qui nous intéresse », et, au v. 1069, « nous en croiserons d'autres en route » et « nous fournira
  aussi une amorce philologique » (le lecteur fait route avec l'éditeur ; une lecture d'auteur est
  possible, à trancher comme le « nous devons » du v. 1059 signalé plus bas) ; les impératifs
  « Revenons », « Scrutons », « rappelons-le », « reconnaissons-le », « digressons », « signalons »,
  « Gardons-nous ».

## Coquilles corrigées

- 1059 (ἀντῳδὸς ἐπικοκκάστρια), note : « l'oiseau dont **il question** dans cette épigramme » →
  « dont **il est question** » (mot omis).
- 1059 (Ἠχὼ…) : « *Confer* **le** magistrale note de Willems » → « **la** magistrale note ».
- 1059 (Ἠχὼ…) : parenthèse ouverte et jamais fermée, « (Soit dit en passant, on retrouve les mêmes
  traits […] le coucou chantait les événements fâcheux (dont en premier lieu, bien-sûr, le
  cocufiage)¹. » → parenthèse fermante ajoutée après le point final : « …le cocufiage)¹.) ».
- 1059 (Ἠχὼ…) : espace parasite avant la virgule après l'appel de la note sur Austin–Olson
  (« »⁴ , c'est que ») → « »⁴, c'est que ».
- 1069 : « Car il ne suffit de partir à l'aventure » → « il ne suffit **pas** de partir » (négation
  incomplète).
- 1069 : « toutes brides de **l'imaginations** abattues » → « de **l'imagination** ».
- 1069 : « pour qu'y **apparaisse** certains détournements » → « **apparaissent** » (accord avec le
  sujet inversé).
- 1069 : « voyons cela avec première réplique ἐπικοκκάστρια » → « avec **la** première réplique »
  (article omis).
- 1069, note 2 : « 528 K.-A.(515 Kock) » → « 528 K.-A. (515 Kock) » (espace).
- 1073–5 : « ou bien preuve **q'il** recopiait » → « **qu'il** ».
- 1079, citation de *Nuées* 133 : « Τίς ἐσθ᾽ ὁ κόψας **τήν** θύραν; » → « **τὴν** θύραν; » (accent aigu
  pour grave ; la seconde citation du même vers, quelques lignes plus bas, porte bien τὴν).
- 1080 : « La leçon du *Ravennnas* » → « *Ravennas* ».
- 1080–2 : « Il me semble qu'on **peut peut** y répondre » → « qu'on **peut** y répondre » (mot
  redoublé).
- 1059 (Ἠχὼ…, partie restée au commentaire), scholie citée : « τὴν **Ἡχὼ** » → « τὴν **Ἠχὼ** » (esprit
  rude pour doux ; l'article écrit partout ailleurs Ἠχὼ) et « ἐν τῇ **Ανδρομέδᾳ** » → « **Ἀνδρομέδᾳ** »
  (esprit omis ; cf. 1060 « <ἡ> Ἀνδρομέδα », 1065–72 « Ἀνδρομέδας »). Corrigés à la reprise.
- 1069 (critique) : « une mention de **Ζεύς** Ὀλύμπιος » → « **Ζεὺς** Ὀλύμπιος » et, en note,
  « **Διός** Ὀλυμπίου » → « **Διὸς** Ὀλυμπίου » (aigu pour grave devant un mot ; même article :
  « Διὸς ἀστήρ », « Διὸς ἀστερωπὸς »). Corrigés à la reprise.

## Renvois ajoutés

- Commentaire 1059 (Ἠχὼ…) : « Pour le texte, voir le commentaire critique. » à la place du paragraphe
  déplacé (avant « Bref ! »).
- Critique 1059, en tête : « Pour le sens d'ἐπικοκκάστρια, voir le commentaire de la pièce. »
- Commentaire 1071, en tête : « Pour le texte, voir le commentaire critique. »
- Critique 1071, en fin d'article : « Pour le sens et les parallèles, voir le commentaire de la pièce. »

## Passages signalés

### Par article

- 1054–5 : le lemme reproduit la leçon de R (δαιμόνων) ; le texte établi imprime δία μένων
  (Willems). Laissé tel quel. Leçon de R contrôlée sur l'image (f. 175r, l. 10 : « λαιμό τμή τ' ἄχη
  δαιμόνων αἰόλαν », lecture aussi de l'inventaire graphologique `ravennas/graphologie/folios/f175r.jsonl`) :
  R porte bien δαιμόνων. L'article dit que la note de
  Willems « n'emporte pas pour autant ma conviction » et retient pourtant sa correction : les
  réserves de l'auteur (paléographiques : passage de l'ε de μένων à l'ο de δαιμόνων ; piste
  ἀδημονῶν) ne sont plus que dans des lignes mises en commentaire dans la source (voir les passages
  `\eff` ci-dessous).
- 1059 (Ἠχὼ…, partie critique), note sur les indications de personnages : « la *Juntina* (**Venise**,
  1516) » — l'*editio princeps* a été imprimée à **Florence** chez Giunta (`CONVENTIONS.md`, § 2.3).
  Non corrigé (contenu, non coquille).
- Même note : la politique « Von Velsen […] ne les fit pas apparaître dans son apparat critique. Je
  l'ai suivi en cela. » est **obsolète** au regard des conventions de la nouvelle édition, où la main
  du XVIe s. figure dans l'apparat sous le sigle R^XVI, et où son attribution à Euphrosynus Boninus
  est donnée comme « non démontrée » (`CONVENTIONS.md`, § 2.3). Conservé ; à revoir par l'auteur.
- Même paragraphe (v. 1094, folio f175v) : faits de R — absence de la menace du Scythe, réplique
  οὐκ αἰρήσεις attribuée à l'archer — **à vérifier sur l'image** du f. 175v. Premier examen de l'image
  (à la reprise) : la ligne porte, après ποῖ ποῖ φεύγεις et dans la même réplique, ΟΥ ΚΑΙΡΗΣΕΙΣ, avec en
  marge droite la scholie ἀντὶ τοῦ οὐ χαιρήσεις ; la séparation des mots et les signes suscrits (οὐ
  καιρήσεις ou οὐκ αἱρήσεις ?) sont à examiner à fort grossissement dans l'étude de f175v. L'attribution de la
  répartition « Τοξ. οὐ καιρήσεις — Εὐρ. οὐχ αἱρήσεις » (Wilamowitz, *Kleine Schriften* IV, 1962,
  p. 486 ; Sommerstein) est à contrôler dans deux sources au moins (`CONVENTIONS.md`, § 2.4).
- Renvoi venu de f175v : dans `edition/folios/f175v/critique.tex`, l'article `\cc{1094}` renvoie à
  « la note *supra* au vers 1056 » : il s'agit de cet article (v. 1059), dont la partie sur le
  v. 1094 est désormais au commentaire critique. « 1056 » semble un lapsus pour 1059 (non modifié :
  fichier d'un autre folio).
- 1059 (Ἠχὼ…, partie critique) : « pour Aristophane, **nous devons** cependant impérieusement **nous
  y livrer** puisqu'il vient de **nous** prévenir que les échos seraient *moqueurs* » — « nous »
  conservé : il prolonge le « reconnaissons-le » et le « nous » des lecteurs d'Aristophane ; on
  pourrait aussi le lire comme un « nous » d'auteur (c'est l'éditeur qui reconstruit). À trancher
  par l'auteur.
- 1059 (Ἠχὼ…, partie critique) : « ce que les répliques d'Écho-Euripide pouvaient avoir **d'amusantes
  ou de méchantes** » — tour fautif (« avoir d'amusant ou de méchant ») ; non corrigé (faute de langue,
  non de frappe).
- 1063 : le lemme porte « σὲ δ᾽ ἐπικλάειν ὕστερον » (forme ἐπικλάειν, celle de Brunck), alors que le
  texte établi (`texte.tex`) et l'apparat de l'auteur (source, l. 4302 : « κλαίειν et ἐπικλαίειν R :
  κλάειν et ἐπικλάειν Brunck ») impriment ἐπικλαίειν, leçon de R contrôlée sur l'image (l. 19 :
  κλαίειν … ἐπικλαίειν). Lemme non modifié, à harmoniser par l'auteur. La discussion des deux formes
  n'existe que dans des lignes désactivées de la source (voir plus bas) : aucune matière critique
  active à déplacer.
- 1069 (critique) : « Dans les *Oiseaux*, après avoir poutré l'importun chresmologue Hiéroclès, on
  l'envoie se faire pendre εἰς Ἐλύμνιον (vers 1126) » : Hiéroclès et le vers οὐκ ἀποπετήσει θᾶττον εἰς
  Ἐλύμνιον; sont de la *Paix* (v. 1126, contrôlé dans le corpus local) ; « *Oiseaux* » est une erreur de
  titre, non corrigée (référence). Même paragraphe : « ἐλύμνιαι· δοκοὶ ὀρόφιναι (Hésychius δ 2227) » :
  un lemme en ε ne peut avoir un numéro de la lettre δ (sans doute ε 2227 ; numéro non vérifiable ici,
  l'édition Latte n'étant pas dans le corpus local ; le LSJ, s.v. ἐλύμνιαι, cite « δοκοὶ ὀροφῆναι,
  Hsch. ») — non corrigé [à vérifier].
- 1073–5 (critique) : « στωμυλιο-συλλεκτάδης, hapax qu'Aristophane mit dans la bouche d'Eschyle au
  vers 839 des *Grenouilles* » : le mot est au v. 841 (Hall–Geldart, Perseus ; c'est bien Eschyle qui
  parle) — non corrigé (référence). L'argument repose sur les deux graphies de R : au v. 1074 (l. 33),
  στωμυλωμένη à un seul λ se lit bien sur l'image ; au v. 1073 (l. 32), des deux λ de στωμυλλωμένη,
  le premier est d'une encre nettement plus pâle et plus grise que le reste du mot (mesure sommaire
  des rapports de couleur : intermédiaire entre l'encre du copiste et le gris des marques de 1516), et
  une trace grise du type de ces marques se voit juste au-dessus (zone ≈ [776, 1688, 822, 1732] px de
  l'image) : un λ ajouté après coup n'est pas exclu. À examiner dans l'étude graphologique de f175r
  avant de fonder l'argument sur deux graphies du copiste.
- 1079 (critique) : l'article étant passé en entier au commentaire critique, le commentaire de la pièce
  n'a plus rien sur le v. 1079, alors que l'explication de l'imprécation ἐς κόρακας (« [va] au
  diable ! ») et de ses emplois avec βάλλειν (*Guêpes* 835, *Ploutos* 782, *Nuées* 133 : contrôlés)
  relève de la langue proverbiale, l'un des deux axes du commentaire (`CONVENTIONS.md`, § 7). Non
  scindé : la phrase enchaîne sans coupure sur la digression des *Nuées*, qui sert la conjecture ; une
  brève note au commentaire de la pièce pourrait reprendre ces deux phrases, si l'auteur le souhaite.
- 1080 (critique) : leçon de R contrôlée sur l'image (f. 175r, l. 41 : τί τὸ κακόν· ηχ τί τὸ κακόν·) ;
  au v. 1085 (f. 175v, l. 4), R porte bien σί κακόν, comme le dit la note 2. Ton polémique de la note 2
  (« ces faussaires », « double forfaiture ») : conservé ; de même la note sur Austin–Olson au
  commentaire 1059.
- 1080–2 (commentaire), note : « vase attique à figure rouge du IVe siècle av. J.-C. (n° 7864 au
  catalogue de Beazley) » : numéro non contrôlé [à vérifier] (base Beazley ?).
- Traduction (`texte.tex`, hors du présent partage) : les répliques d'Écho y sont rendues comme de
  simples échos (1071 « En partage. », 1074 « Ton babil. », 1079 « Va-t'en aux corbeaux. »), et non
  selon les conjectures que défend le commentaire critique (« La Mort extirpe la douleur », « [je suis]
  de tempérament prolixe », « Et toi mets bas le fermoir ! ») : à harmoniser par l'auteur
  (`CONVENTIONS.md`, § 6).

### Passages `\eff` de la source (marqués en orange par l'auteur)

Tous sont dans des lignes désactivées (`%`) de la source : la conversion ne les a pas repris, et rien
n'en figurait dans `commentaire.tex` avant le partage. Numéros de ligne de
`latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex`.

- l. 4235 (1054–5, fin de l'article, aujourd'hui au commentaire critique) : `\eff{Retoucher ! MAsculin
  adhmonwn ? ὡς marque l'exclamation ?}` — à rapprocher de la fin désactivée de l'article (l. 4234 :
  « je préfère y voir le verbe ἀδημονέω (ἀδαιμονέω DGE) ») et de la note 2 désactivée (l. 4239 : la
  conjecture de Willems satisfait le sens, mais le passage de l'ε de μένων à l'ο de δαιμόνων
  s'explique mal, alors que Η → Ε → ΑΙ est naturel). L'article actif retient δία μένων.
- l. 4270 (1059, Ἠχὼ…, partie restée au commentaire) : après « …où était enchaînée Andromède. »,
  `\eff{sûr ? cf. représentation}` — l'auteur doutait lui-même que l'acteur d'Écho restât invisible
  dans l'*Andromède* ; l'affirmation demeure au commentaire sans ce doute.
- l. 4314 (1063) : article désactivé `\commentaire{1063}{σὲ δ᾽ ἐπικλαίειν ὕστερον.}{\eff{Émouvoir ?}}`
  (piste de sens pour ἐπικλαίειν).
- l. 4344 (1069, aujourd'hui au commentaire critique) : après « Réponse : ce n'est pas impossible ! »,
  `\eff{Hum..}` — doute de l'auteur sur l'hypothèse d'un Hésychius témoin d'un texte mieux conservé.
- l. 4374 (1069, note 2, au commentaire critique) : `\eff{(Le \LSJ est à corriger sur ce point.)}` — à
  propos de la distinction δοκός / δόκος.
- l. 4378 (1069–72) : dans un article entièrement désactivé, `\commentaire{1069-72}{δι᾽ Ὀλύμπου —
  μέρος ἐξέλαχον — θανάτου τλήμων.}`, `\eff{Jeu du diable boîteux voir Louis Beck de Fouqières}`. Cet
  article (Hésychius ε 2507 Ἔμπουσα et ε 1264 ἑκάτη « carcan » : δι᾽ Ὀλύμπου → διάλυ(ε) (ἔ)μπουσ(αν) ;
  μέρος ἐξέλαχον → μέρος ἐκ σέλαχος « la part du requin » ; θανάτου τλήμων → θαλάττης τέμνον), que
  l'auteur jugeait « Pas très satisfaisant... à retoucher ! », a été remplacé par les articles actifs
  1069 et 1071 ; l'apparat désactivé du v. 1072 (l. 4422 : « θανάτου τλήμων R : θαλάττης τέμνον
  Bibi ») en est la trace. Note désactivée attenante (l. 4378–4379) : *Grenouilles* 293 et scholie,
  Tosi 2202, *Lysistrata* 700–705, Érasme n° 394.
- l. 4404–4407 (1071, fin de l'article, partie restée au commentaire) : `\eff{maux sans guère de répit /
  La mort guérit des maux / la malheur t'a guère de répit / la mâle-mort à son heure/ oeuvre}` — essais
  de traduction de la réplique d'Écho (voir plus haut la remarque sur la traduction).
- l. 4490 (1079, aujourd'hui au commentaire critique) : `\eff{Nous avons déjà analysé au vers 942
  comment Aristophane jouait avec le mot κόραξ et ses deux sens possibles : le corbeau ou bien le
  crochet qui entrave Mnésiloque.}` — l'article actuel sur les vv. 939–42 (`f173v/commentaire.tex`)
  parle des corbeaux (κόραξιν) mais non du sens « crochet » : le renvoi n'aurait plus d'appui.

### Autres passages désactivés de la source (non repris par la conversion)

- l. 4192 (1047) : `\commentaire{1047}{ἰώ μοι μοίρας.}` — parallèle *Andromaque* 824, ἰώ μοί μοι.
- l. 4232–4233 (1054–5) : « ὡς ἐκρεμάσθην = depuis que j'ai été attaché ? » ; « D'abord, la traduction
  λαιμότμητ᾽ ἄχη reporter à la note de Willems […], le texte en est corrompu, certainement en cet
  étonnant †δαιμόνων† ».
- l. 4274 (1059) : parenthèse sur les composés en ἐπι- (succession temporelle et hostilité).
- l. 4290 (1059, note 3) : début désactivé « Une fois n'est pas coutume ! […] » sur la qualité des
  scholies de la pièce.
- l. 4309–4313 (1063) : matière critique désactivée — scholie ἠρέμα ὁ κηδεστὴς τοῦτο πρὸς τὸν
  Εὐριπίδην (Mnésiloque parlerait « à part », ce que dément la réponse d'Euripide ; une note marginale
  de S2 en face de la l. 19, qui écrit κηδεστ(ής), est relevée dans l'inventaire graphologique) ;
  « le verbe ἐπικλαίειν n'est pas autrement attesté à l'époque classique, au contraire
  d'ἐπικλάειν », avec une note sur la quantité indifférente de la syllabe en cause.
- l. 4333 (1068) : `\commentaire{1068}{δι᾽ Ὀλύμπου.}` — Hésychius (ο 654) Ὀλύμπιος· οὐράνιος.
- l. 4340 (1069) : « Prov : Ὀλυμπικὴ στοά: ἐπὶ τοῦ λάλου, ἢ ὅτι εἰκὸς ἔχειν τὴν στοὰν ἀντῳδὸν ἠχὼ […] »
  — proverbe sans référence dans la source ; c'est l'*Appendix proverbiorum* IV 19 (CPG I, p. 439 ;
  contrôlé dans le corpus local), utile à l'axe proverbial du commentaire.
- l. 4356–4370 (1069) : hypothèse διαλάμπου (« Plus haut ! ») d'après Aristote, *Problemata* 922a ;
  liste de lemmes d'Hésychius à finale -ου altérée ; « 279 crux ἱέρας· σημεῖον ».
- l. 4398 (1071) : fragment de Moschion (Ταῖς νόσοις ὁ θάνατος […]), sans référence.
- l. 4433 (1073) : « Même scansion qu'aithéros iéras ».
- l. 4457 et 4465–4476 (1078) : apparat désactivé « Μνη. χαριεῖ μοι παῦσαι --- Εὐρ. παῦσαι R : Μνη.
  χαριεῖ μοι ᾽παΰσαι --- simul Μνη. et Εὐρ. παῦσαι Bibi » ; discussion désactivée (deux παῦσαι, *Oiseaux*
  1382, adesp. 601 K.-A. = Photius π 519, ponctuation de la plupart des éditeurs entre χαριεῖ μοι et
  παῦσαι, Sophocle, *Électre* 987, *Odyssée* XXIV 384 ; traduction « Abrège ! »).
- l. 4514–4516 (1080) : notes de travail (κάγκελον, καγχάζω, Hésychius †κακόρας· κατακόψας).
- l. 4560 (1081, dernière réplique d'Écho ; `\apparat{1082}` dans la source) : apparat désactivé
  « ὀτότυζ᾽ R : ὀλόφυγ᾽ Bibi ».

### Références contrôlées à la reprise (corpus local `.sources/corpus/`)

- Exactes : *Thesm.* 272 (αἰθέρ᾽ οἴκησιν Διός) ; *Ran.* 100 (αἰθέρα Διὸς δωμάτιον) ; *Nub.* 133,
  *Plut.* 782, *Vesp.* 835 (βάλλ᾽ ἐς κόρακας) ; *Thesm.* 610, *Pax* 322, *Av.* 1213 (τί τὸ κακόν),
  *Vesp.* 1136 (τουτὶ τὸ κακὸν τί ἐστι), *Pax* 181 ; *Thesm.* 1090 (γυνὴ πλησίον αὕτη) ; Eschyle,
  *Choéphores* 828 (ἐπαΰσας) ; *Anth. Pal.* VII 191 (Archias, la κίσσα ; les deux vers cités sont aussi
  dans la Souda, α 2757 et κ 1422) ; Pollux X 22 (κόρακες parmi les pièces de la porte ; cf. VII 111) ;
  Souda μ 1257 (μόρος· ὀδύνη, πόνος, θάνατος) ; Euripide, *Ion* 1078–1079 (l'auteur : « v. 1077 sq. »).
- Erronées (non corrigées ; voir ci-dessus) : « *Oiseaux* … vers 1126 » (= *Paix* 1126) ; *Grenouilles*
  « 839 » (= 841) ; Hésychius « δ 2227 » pour ἐλύμνιαι.
- Non contrôlables ici : numéros d'Hésychius (ο 649, δ 2129, μ 1683), Photius μ 538, *Synagoge* μ 267,
  Ar. fr. 528 K.-A., Sophocle fr. 698 Radt, Stobée IV 52, 26, Apostolius II 52c, Chantraine p. 106-7,
  *The Songs of Aristophanes* p. 57, Beazley n° 7864, Wilamowitz, *Kleine Schriften* IV, p. 486.
