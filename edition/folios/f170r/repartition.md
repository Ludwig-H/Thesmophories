# f170r (vv. 636–678) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f170r/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 4615–4636, et
`latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex`, l. 502–703 ; articles
C0181–C0191 de `edition/donnees/travaux_anterieurs/commentaires.tsv`).
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**Bilan.** 11 articles : 4 CRITIQUE (déplacés en entier), 6 PIÈCE (restés), 1 MIXTE
(scindé). `critique.tex` compte 6 articles (`\cc{637–40}`, `\cc{642–3}`, `\cc{655–86}`,
`\cc{656}`, `\cc{657}`, `\cc{664}`), rangés par vers ; `commentaire.tex` en garde 7.
Compilation (`./edition/compiler_folio.sh f170r`) : OK, 7 pages ; les notes `\nc` des articles
critiques sont bien composées en fin d'article. Contrôle automatique (comparaison mot à mot
avec la conversion d'origine, copiée dans `.travail/f170r/commentaire.orig.tex`) : rien n'a été
supprimé ; seuls diffèrent les corrections listées ci-dessous et les renvois ajoutés.

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0181 | 637–40 | κἄπειτ᾽ ἀποδύσετ᾽… | CRITIQUE (attribution des répliques : absence de *paragraphos* dans R, Brunck et les éditeurs ; leçon χάλᾳ R / χάλα / χαλᾷ Bibi ; jeu de scène invoqué comme argument) | déplacé en entier dans `critique.tex` (`\cc{637–40}`) ; 1 « nous » → « je » ; 3 coquilles corrigées |
| 2 | C0182 | 641 | στερίφη γάρ εἰμι | PIÈCE (langue : double sens de στέριφος, « ferme » / « stérile » ; scholie et lexiques) | reste dans `commentaire.tex`, inchangé |
| 3 | C0183 | 642–3 | νῦν· τότε δὲ μήτηρ… | CRITIQUE (attribution des répliques : aucun *paragraphos* dans R aux vv. 642–643 ; distique entier à Clisthène) | déplacé en entier dans `critique.tex` (`\cc{642–3}`) ; 1 coquille corrigée |
| 4 | C0184 | 643 | ἀνίστασ᾽ ὀρθός | PIÈCE (mise en scène : double entente, jeu du phallus ; costume, transparence de la crocote) | reste dans `commentaire.tex` ; 2 coquilles corrigées |
| 5 | C0185 | 643 | Note sur τὸ ἔγκυκλον | PIÈCE (realia : costume, sens de l'ἔγκυκλον ; jeux de mots, *Lysistrata*, *Assemblée*, scholie, Eustathe ; les remarques textuelles portent sur d'autres textes, voir plus bas) | reste dans `commentaire.tex` ; 3 coquilles corrigées |
| 6 | C0186 | 644 | τάλαν | PIÈCE (langue : τάλαν réservé aux femmes) | reste dans `commentaire.tex`, inchangé |
| 7 | C0187 | 647–8 | ἰσθμόν τιν᾽ ἔχεις… | PIÈCE (realia : le δίολκος de Corinthe ; mise en scène ; métaphore ἰσθμός = αὐχήν = τράχηλος = πέος) | reste dans `commentaire.tex`, inchangé |
| 8 | C0188 | 651 | εἰσεκύλισα | PIÈCE (langue, images : κυλίνδειν et composés ; note de Taillardat, § 558) | reste dans `commentaire.tex` ; 1 coquille corrigée |
| 9 | C0189 | 655–86 | Le chœur compris entre les vv. 655-686 | MIXTE (structure et jeu de scène du chœur, note 19 de Willems citée : PIÈCE ; colométrie et responsion, et note de Willems contre l'addition τούτοισι τοῖς au v. 664 : CRITIQUE) | scindé : la phrase sur la colométrie (Lætitia [Parker], *The Songs of Aristophanes*) et la remarque sur la responsion 667–686 / 707–725 → `critique.tex` (`\cc{655–86}`, lemme d'origine) ; la note 7 de la citation de Willems (εἴ τις ἐν τόποις ἑδραῖος, avec le crochet de l'auteur) → `critique.tex` (`\cc{664}`), suivie de « (Note de Willems.) » ; dans `commentaire.tex`, la citation de Willems reste entière, avec « Pour la colométrie et le texte, voir le commentaire critique. » après l'introduction et, à l'appel de l'ancienne note 7, la note « Pour le texte du v. 664 (εἴ τις ἐν τόποις ἑδραῖος), voir le commentaire critique. » |
| 10 | C0190 | 656 | τῶν θ᾽ ἱματίων ἀποδύσας | CRITIQUE (leçon de R défendue contre les correcteurs : ἀποδῦναι + génitif, d'après la note 20 de Willems) | déplacé en entier dans `critique.tex` (`\cc{656}`), inchangé |
| 11 | C0191 | 657 | εἰσελήλυθεν | CRITIQUE (leçon de R *contra metrum* ; conjectures de Faber, Fritzsche, Handley ; réfutation d'Austin) | déplacé en entier dans `critique.tex` (`\cc{657}`), inchangé |

## « nous » d'auteur changés en « je »

- 637–40 (note 1, désormais dans `critique.tex`) : « Par abus de langage, nous utiliserons le
  terme de *paragraphos* » → « j'utiliserai le terme ».

Gardés : les « nous », possessifs et impératifs qui associent le lecteur (« notre manuscrit »,
« nos éditeurs », « notre poète », « interrogeons-nous », « sous nos yeux », « qu'Hésychius… n'a
pas manqué de nous définir », « celle qui nous intéresse présentement », « espérons »,
« Allongeons quelque peu cette note », « délaissons un peu nos primes amours », « Citons »,
« ne citons que ») ; ceux des auteurs cités (Willems, Taillardat, traductions).

## Coquilles corrigées

- 637–40 : « les éditeurs suivent quasi-unanimement Brunck en `rétablissent' deux » →
  « en `rétablissant' deux ».
- 637–40 : « au début du vers 638 (Clistène) » → « (Clisthène) », graphie de partout ailleurs.
- 637–40 : « il n'y a aucune de raison de douter » → « aucune raison ».
- 642–3 : « On ajoute souvent deux changement d'interlocuteurs » → « deux changements ».
- 643 (ἀνίστασ᾽ ὀρθός), note : « Arthur D. Trendall , `\italique{Phlyax Vases}` » →
  « Trendall, » (espace avant la virgule).
- 643 (ἀνίστασ᾽ ὀρθός) : point final manquant après l'appel de note (« …qui la rend
  transparente¹ ») ajouté.
- 643 (ἔγκυκλον) : « Blépyros reproche à sa femme de ne pas s'être acquitté » → « acquittée ».
- 643 (ἔγκυκλον), note 5 : « demande à récupérer l'`\italique{encyle}` » →
  « l'`\italique{encycle}` ».
- 643 (ἔγκυκλον), note 6 (citation de Chantraine) : « dans des inscription de Delphes » →
  « des inscriptions ».
- 651, note 1 : « Le moyen κυλίνδεσθαι se dit de malheur lui-même » → « du malheur lui-même ».

## Passages signalés

### Affirmations sur R à vérifier sur l'image (articles critiques ; non vérifiées ici)

- 637–40 : note marginale μν^ησ au v. 638 ; iota adscrit « nettement écrit » de χάλᾳ (v. 638) ;
  aucun signe de changement de locuteur entre le v. 638 et le v. 641.
- 642–3 : aucun *paragraphos* aux vv. 642–643.
- 655–86 (2°, crochet de l'auteur dans la citation de Willems) : note marginale ἡμιχ. γυν. au
  v. 659, « écrite d'une seconde main », reprise dans M.
- 657 : leçon εἰσελήλυθεν.

### Par article

- 637–40 : lemme « … τίτθος γ᾽ … » (leçon de R) alors que `texte.tex` porte τιτθούς (Iuntina) ;
  lemme laissé tel quel.
- 637–40 : « χαλᾷ est un subjonctif dit *délibératif* » s'accorde mal avec la traduction
  indicative « Il défait mon strophion avec promptitude » (dans l'article et dans `texte.tex`) ;
  à revoir par l'auteur ; non modifié.
- 641 : « cf. l'apparat des témoins » renvoie à l'apparat des *testimonia* de l'édition
  antérieure ; dans la nouvelle, les témoins vont aux *loci paralleli* (*Test.*) : renvoi à
  ajuster quand `paralleles.tex` existera (gardé tel quel).
- 643 (ἀνίστασ᾽ ὀρθός), note : « il est reproduit en annexe » renvoie aux annexes de l'édition
  antérieure (cratère de Sant'Agata dei Goti) ; à confirmer pour la nouvelle édition. Même note :
  « BICS suppl. LXIX (1967) » — *Phlyax Vases*, 2ᵉ éd. (1967), est en principe le suppl. 19 (XIX)
  du BICS : [à vérifier] ; référence non modifiée.
- 643 (ἔγκυκλον) : l'article contient trois interventions textuelles de l'auteur sur d'autres
  textes que les *Thesmophories*, restées dans le commentaire de la pièce parce qu'elles servent
  l'argument sur le costume : attribution de *Lys.* 104 à la femme qui parle aux vv. 112–114 ;
  correction φησίν → σφῇσιν dans Eustathe (*in Il.* 976.13) ; « On lit en épigraphie… » (formes
  épigraphiques sans référence précise) [à vérifier].
- 644 (τάλαν) : liste de la note contrôlée sur le corpus local (Perseus) : toutes les
  occurrences citées sont bien dans une bouche féminine ; *Eccl.* 526 (Praxagora) n'y figure
  pas et pourrait s'y ajouter. Rien de modifié.
- 647–8 : lemme « ὦνθρωπ᾽ » (circonflexe) alors que `texte.tex` porte ὤνθρωπ᾽ ; lemme laissé tel
  quel.
- 647–8, note 3 : « τράχηλος est phallossémique au vers 20 des *Grenouilles* » — τράχηλος est au
  v. 19 (vérifié sur le corpus local), que la note cite d'ailleurs aussitôt (« et puis au vers
  19 ») ; référence non modifiée. La même note contient une conjecture de l'auteur sur *Ra.* 20
  (οὐ κε ῥεῖ pour οὐκ ἐρεῖ) : elle porte sur un autre texte et reste donc dans le commentaire de
  la pièce.
- 651 : « Il est clair que, dans ce cas, ἐμβάλλειν τινὰ εἰς συμφοράς n'est qu'un synonyme
  expressif de ἐμβάλλειν » est tautologique : la note de Taillardat (§ 558) devait opposer
  (εἰσ)κυλίνδειν à ἐμβάλλειν ; passage douteux, laissé tel quel [à vérifier sur Taillardat, *Les
  images d'Aristophane*, non disponible ici].
- 651, note 1 : la citation de *Il.* 11, 347 porte « κυλίνδεσθαι » ; le texte homérique a
  κυλίνδεται (vérifié sur le corpus local) ; non modifié.
- 655–86 → `\cc{664}` : seul ajout au texte déplacé (hors renvois), « (Note de Willems.) » en
  fin d'article, selon l'usage de l'auteur (« Note de Willems », « Note de Taillardat ») : hors
  de la citation, le « nous » et le « je » de Willems (« Qu'avons-nous affaire… », « Je ne vois
  pas… ») auraient été pris pour ceux de l'auteur. Ces « nous » et « je » de Willems, comme ceux
  du corps de la citation (« Avec M. Mazon, je crois… »), n'ont pas été touchés.
- 655–86 (2°) : l'attribution des vv. 659–662 au « parastate » (changement de mètre ; crochet de
  l'auteur sur la note marginale de R, `η\auDessus{μ}{χ}ι γ\auDessus{υ}{ν}`) relève de
  l'attribution des répliques, donc du commentaire critique, mais elle est prise dans la phrase
  de Willems dont dépend tout le 2° (définition du parastate) ; laissée dans la citation pour ne
  pas la briser. À reprendre dans le commentaire critique et l'apparat (l'apparat antérieur
  porte « (Ἡμιχ. γυν.) R^pc ») après vérification sur l'image.
- 655–86 (3°) : « Le morceau qui suit (vv. 663-684) est un hyporchême » alors que le chœur va
  jusqu'au v. 686 (lemme) et que la fin est située aux vv. 687–688 : numérotation de Willems ?
  [à vérifier] ; non modifié.

### Graphies et usages récurrents de l'auteur, non corrigés

Ce ne sont pas des fautes de frappe (on les retrouve dans toutes les versions de ses
fichiers) ; à harmoniser globalement si l'auteur le souhaite :

- « bien-sûr » pour « bien sûr » (4 fois : 643 ἀνίστασ᾽ ὀρθός ; 643 ἔγκυκλον ; 647–8, note 3,
  deux fois) ;
- « conclue » pour « conclut » (637–40 : « l'apostrophe ὦναίσχυντε σύ conclue logiquement », dans
  `critique.tex` ; 643 ἔγκυκλον, note 1 : « Comme le conclue Franca Perusino ») ;
- « soutien gorge » (637–40) ; « manuscrit de Münich » (655–86) ; « un jeu de mot » et « sont
  légions » (643 ἔγκυκλον, corps et note 4) ; « saisissait instamment l'image » (647–8 :
  *instantanément* ?).

### Passage `\eff` de la source (marqué en orange par l'auteur)

Un seul dans les vv. 636–678, mis en commentaire (`%`) dans la source et donc absent de la
conversion :

- 655–86, en fin d'article : « Après cette fine analyse de Willems, s'agit-il de roues (trokhos)
  cf. Daremberg Salvatio 1027a ? τὴν πρώτην τρέχειν χρῆν ὡς τάχιστ᾽ ἤδη κύκλῳ » (piste de
  l'auteur sur τὴν πρώτην… τρέχειν… κύκλῳ ; « Salvatio » est sans doute « Saglio », le
  *Dictionnaire* de Daremberg et Saglio). Non repris ; à décider par l'auteur.

### Autres passages mis en commentaire (`%`) par l'auteur dans la source (non convertis)

- 637–40 : trois paragraphes et deux notes d'une rédaction antérieure, plus polémiques
  (« Les tripatouillomanes ont encore sévi à ce vers !.. »), remplacés par le texte actuel.
- 641 : rapprochement avec Hipponax (fr. 122 Degani : ἀμφιδέξιος γάρ εἰμι κοὐκ ἁμαρτάνω κόπτων),
  « Y a-t-il ici aussi détournement d'un tour proverbial ? » — à considérer pour les *loci
  paralleli*, après vérification.
- 643 (ἀνίστασ᾽ ὀρθός) : « (nous y reviendrons à la fin de cette note) ».
- 643 (ἔγκυκλον) : plusieurs phrases polémiques ; la fin de la note 1 sur un vase à figures
  rouges (Beazley, *ARV*² 378.122) où Perusino reconnaît un ἔγκυκλον ; une ancienne note 7
  contre Perusino.
- 657 : « (on reste circonspect devant de telles explications) », à propos de Fritzsche.
- 662 : ébauche d'article sur τὴν πρώτην (« L'interprétation de Willems me semble bien
  préférable… »).

### Hors commentaire

- `texte.tex` : numérotation fautive dans le chœur (663, 668 et 670 en double ; 664, 667 et 671
  absents) ; sans effet sur `critique.tex` (non ancré), mais un `\comm{664}` y serait mal ancré.
