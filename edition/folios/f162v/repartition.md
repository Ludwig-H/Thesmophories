# f162v (vv. 1–42) — répartition commentaire critique / commentaire de la pièce

Source : `commentaire.tex` (conversion de `latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 518–903).
Les articles critiques passent dans `critique.tex` (`\cc`), les articles de la pièce restent dans
`commentaire.tex` (`\comm`) ; les articles mixtes sont scindés, avec un renvoi « Pour le texte, voir le
commentaire critique. » à la fin de la partie restée dans le commentaire.

**État** : terminé (18 articles traités) ; `./edition/compiler_folio.sh f162v` : OK, 7 pages, sans erreur. Le
texte des notes `\nc` des articles critiques est bien composé (`\cc` vide désormais les notes à la fin de
l'article, comme `\comm` : modification de `thesmo.cls` faite par un autre agent, contrôlée dans le PDF).

**Récapitulatif** : 18 articles, dont 2 CRITIQUES (30–3, 35), 2 MIXTES (16–8, 22–4) et 14 PIÈCE.
`critique.tex` contient 4 articles (16–8, 22–4, 30–3, 35), dans l'ordre des vers.

## Articles

| n° | Plage | Lemme (abrégé) | Classement | Action |
|---|---|---|---|---|
| 1 | 1–10 | ὦ Ζεῦ … οὐχ ἅ γ᾽ ἂν ἀκούειν δέῃ | PIÈCE | reste (jeu ἅ γ᾽ ἂν / ἄγαν, amphibologie) ; coquilles corrigées |
| 2 | 1–4 | ὦ Ζεῦ … κομιδῇ μ᾽ ἐκβαλεῖν | PIÈCE | reste (hirondelle / coq des *Nuées*, proverbe) ; coquille corrigée |
| 3 | 2 | ἀλοῶν | PIÈCE | reste (image agricole, Taillardat) ; coquille corrigée |
| 4 | 3 | πρὶν τὸν σπλῆνα … ἐκβαλεῖν | PIÈCE | reste (la rate, « dé-raté ») ; inchangé |
| 5 | 13–8 | (sans lemme) | PIÈCE | reste (pastiche de cosmogonie, Empédocle) ; inchangé |
| 6 | 16–8 | πρῶτα ἐμηχανήσατο … διετετρήνατο | MIXTE | scindé : → `critique.tex` le renvoi à Willems sur ce « passage diversement retouché au gré des éditeurs » (+ parenthèse sur ses notes en annexe) et la construction διετετρήνατο δὲ ἀκοὴν (ὡς) χοάνης ὦτα (défense de R contre Biset, Boissonade) ; reste l'image de la fonderie (ὦτα = godets du moule) + renvoi |
| 7 | 19 | διὰ τὴν χοάνην … μήθ᾽ ὁρῶ | PIÈCE | reste (saillie de Mnésiloque, proverbe *Nec aures…*) ; « nous » → « je » |
| 8 | 21 | οἷόν τέ που 'στιν … ξυνουσίαι | PIÈCE | reste (paternité du mot σοφοὶ τύραννοι…, renvoi à Willems sur le sens de γέ που) ; coquille corrigée ; voir signalements |
| 9 | 22–4 | πῶς ἂν οὖν … χωλὸς εἶναι τὼ σκέλει | MIXTE | scindé : → `critique.tex` la phrase « (Voir là-dessus la 3e note d'Alphonse Willems […] qui justifie la suppression du vers 23 […].) » ; reste le proverbe du boiteux, χωλοποιός, la pointe τὼ σκέλει et la scholie + renvoi ; coquilles corrigées |
| 10 | 27–8 | σίγα νυν — σιωπῶ τὸ θύριον … | PIÈCE | reste (« Le trait d'esprit de Mnésiloque nous échappe. ») ; inchangé ; voir `\eff` l. 734 |
| 11 | 29 | Ἀγάθων | PIÈCE | reste (Agathon, sa victoire de 416, parallèle des *Acharniens*) ; inchangé |
| 12 | 30–3 | ποῖος οὗτος Ἁγάθων; … οὐχ ἑόρακας πώποτε | CRITIQUE | déplacé en entier dans `critique.tex` (répartition des répliques, conjecture ἀγαθῶν de Bibi, état de R au v. 32, scholie) ; « nous » → « je » ; coquille corrigée |
| 13 | 35 | καὶ μὴν βεβίνηκας … ἴσως | CRITIQUE | déplacé en entier dans `critique.tex` (*crux* sur βεβίνηκας : ton, absence de scholie, leçon originelle perdue ; la note sur la scholie du v. 258 fait partie de l'argument) ; inchangé |
| 14 | 37 | μυρρίνας | PIÈCE | reste (rameaux de myrte des sacrifices) ; inchangé |
| 15 | 39–62 | Passage en dimètres anapestiques | PIÈCE | reste (description métrique et emploi du mètre, sans discussion de colométrie) ; inchangé |
| 16 | 39–40 | εὔφημος πᾶς ἔστω λέως / στόμα συγκλῄσας | PIÈCE | reste (formule rituelle, tour tragique) ; coquille corrigée ; voir signalements |
| 17 | 40 | ἐπιδημεῖ | PIÈCE | reste (sens de ἐπιδημεῖ, μελοποιῶν au sens du futur ; note de Willems, dont le « me » n'est pas celui de l'auteur) ; coquilles corrigées |
| 18 | 41–2 | θίασος Μουσῶν … μελοποιῶν | PIÈCE | reste (le thiase, inversion relevée par Sommerstein) ; coquille corrigée ; voir signalements |

## « nous » d'auteur changés en « je »

- 19 : « **Nous nous efforcerons** au contraire, et selon **nos** moyens, de souligner… » → « **Je m'efforcerai** au contraire, et selon **mes** moyens, de souligner… ».
- 30–3 (désormais dans `critique.tex`) : « À l'instar du manuscrit de Ravenne, **nous laissons** à Mnésiloque le début du vers 31 » → « **je laisse** ».

« nous » ambigu, conservé : 35 « à défaut d'avoir une proposition alternative solidement étayée, il faut
**nous** résoudre à *crux*-désespérer… » — la décision d'obéliser est celle de l'éditeur (on attendrait
« me »), mais la phrase prolonge la maxime générale « on ne détruit que ce que l'on remplace ». À trancher par
l'auteur.

« nous » conservés parce qu'ils associent le lecteur (ou désignent les lecteurs modernes en général) :
1–10 « Nous sommes au tout début de la pièce », « C'est là que nous arrivons », « Le scholiaste nous met sur
la piste » ; 13–8 « Aristophane nous peint Euripide » ; 16–8 « plus parlante aux spectateurs de l'époque qu'à
nous » ; 19 « comme nous l'allons voir en chemin », « le jeu de mots exact […] nous échappe » ; 21
« Aulu-Gelle […] nous rapporte » ; 22–4, note 4 « Nous ne sommes pas dans la chanson de Nadaud » ; 27–8 « Le
trait d'esprit de Mnésiloque nous échappe » ; impératifs 30–3 « Tâchons d'y voir plus clair ! », « lisons » ;
35 « nos commentateurs », « nos modernes » ; possessifs « notre poète », « notre passage », « notre
scholiaste », « notre manuscrit », « notre *tribulation* », « notre “Qui fréquente le boiteux…” ». Le « me »
de l'art. 40 (« tel me paraît bien le sens ») est celui de Willems (« Note de Willems ») : non touché.

## Coquilles corrigées

- 1–10 : οὐχ ἅ γ᾽ ἂν **μέλῃς** ὁρᾶν (deux fois) et οὐκ ἄγαν **μέλῃς** ὁρᾶν → **μέλλῃς** (texte établi μέλλῃς ; R μέλλεις selon Velsen et Enger ; la traduction de l'auteur « tu es sur le point de voir » suppose μέλλω).
- 1–10 : `οὐχ ἅ **γ** ἂν …' → ἅ **γ᾽** ἂν ; **οὐδ ἆρ** ὁρᾶν δεῖ μ᾽ → **οὐδ᾽ ἆρ᾽** (élisions, comme au v. 8 du texte).
- 1–4 : « à **un** expression proverbiale » → « à **une** expression proverbiale ».
- 2 : « la même image **en avec** notre *tribulation* » → « la même image **avec** notre *tribulation* » (mot surnuméraire).
- 21 : « **Anthistène** » → « **Antisthène** » (fr. 59 Decleva Caizzi).
- 22–4, note 1 : « Leutsch & **Schneidewim** » → « **Schneidewin** ».
- 22–4 : « c'est **bien-sûr** Euripide » → « **bien sûr** ».
- 22–4, note 4 : « διεληλυθώς(v. 825) » → « διεληλυθώς (v. 825) » (espace).
- 30–3 : « cela fait trois **année** qu'il monte des pièces » → « trois **années** ».
- 39–40, note 2 : *Cavaliers* 1316 « στόμα **κλείεν** » → « **κλείειν** » (ι manquant ; le texte Hall–Geldart du corpus local porte κλῄειν).
- 40 : « Cf. **ἐπιχωρτάζει**, *venit ibique commoratur* » → « **ἐπιχωριάζει** » (ἐπιχωρτάζει n'existe pas ; LSJ s.v. ἐπιχωριάζω « to be in the habit of visiting », qui répond à la glose latine ; ἐπιχορτάζω « supply with provender » ne convient pas). La même faute est dans toutes les versions antérieures (`latex/`) : à confirmer sur Willems 1919 si besoin.
- 40 : « **M**ελοποιῶν » (M latin) → « **Μ**ελοποιῶν » (Μ grec).
- 41–2 : « l'inversion est totale : **un** lieu d'un cortège » → « **au** lieu d'un cortège ».

Laissés tels quels (orthographe ou style plutôt que frappe, ou correction incertaine) : 1–4 « bien trop
tôt.. » ; 19 « poètereaux » (pour « poétereaux ») ; 21 « Cela n'empêche pas moins notre scholiaste […]
d'accorder » (croisement de deux tours) et « à priori » ; 35 « presqu'autant ».

## Passages signalés

### Passages entourés de `\eff` dans la source (marqués en orange par l'auteur)

Tous sont, dans la source, à l'intérieur de lignes mises en commentaire (`%`) : la conversion ne les a donc pas
repris. Ils ne sont pas réintroduits ; les voici pour mémoire (numéros de ligne de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`).

- l. 529 (art. 1–10, note 2, après « …et le vers 291. ») — PIÈCE : « Il n'y a aucune raison de mettre en doute l'existence historique de Mnésiloque ainsi que le lien de parenté qu'il entretenait avec lui. S'il est vrai que les indices internes au texte d'Aristophane sont ténus L'arbre généalogique d'Euripide chez Kannicht concorde avec l'usage d'appeler son premier fils du nom du grand-père paternel et second de celui maternel. Cf. Willems Démosthène ? » (brouillon inachevé).
- l. 569 (art. 3, fin) — PIÈCE : « ventre à terre, rendre les boyaux » (piste d'équivalents français).
- l. 650 (art. 19, parmi des hypothèses abandonnées) — PIÈCE : « Nοῦς ὁρᾷ, καὶ νοῦς ἀκούει: ?Érasme 2500 ; n° 1971 du Dictionnaire des sentences latines et grecques. » (piste parémiographique ; Érasme 2500 et Tosi 1971 sont déjà cités dans la note 2).
- l. 666 (art. 21, note 4, après « …vol 5. ») — PIÈCE : « chez Jouan - van Looy ? » (vérifier si le fr. 888b Kannicht figure dans l'Euripide des Belles Lettres).
- l. 734 (article abandonné `\commentaire{27}{σιωπῶ τὸ θύριον}`) — **CRITIQUE** : « Lire σιω πῶ τὸ θύριον; ? du verbe σείω ? puis a-krouw ? » — idée de conjecture restée à l'état de note (coupe σιω πῶ rattachée à σείω ; « a-krouw » non développé) ; elle touche au « trait d'esprit » que l'art. 27–8 dit ne pas saisir. Juste au-dessus (l. 733), un apparat lui aussi mis en commentaire : « θύριον R : θύριον; Dindorf » (ponctuation interrogative).
- l. 869 (fin de l'art. 35, dans un brouillon en commentaire) — **CRITIQUE** : « Le ton est inhabituel dans la bouche d'Euripide.... si bien que l'on se demande s'il ne vaudrait pas mieux lire bainw, piétiner, et le public d'interpréter différemment. Quoi qu'il en soit, ce vers semble confirmer » — idée de conjecture (un parfait de βαίνω au lieu de βεβίνηκας), phrase inachevée.

### Autres passages signalés

- 1–10 : « Aristophane ayant mis à dessein ces particules dans un ordre inhabituel. » — phrase sans verbe principal (inachevée ?), laissée telle quelle.
- 21 : le lemme porte οἷόν **τέ** που (leçon de R selon l'apparat de l'auteur : « τε R : γε Σ ») alors que le texte établi imprime **γε**. Laissé tel quel ; à harmoniser. Laissé aussi au commentaire de la pièce, parce qu'il est formulé sur le *sens*, le renvoi final à la 2e note de Willems : or cette note est aussi une défense textuelle (« Telle est la leçon du manuscrit, confirmée par le scholiaste », contre les conjectures de Brunck, Fritzsche et van Leeuwen). Willems donne donc γέ που comme leçon du manuscrit, l'apparat τε : **leçon de R à vérifier sur l'image**, et la question τε / γε mérite un article critique.
- 21, note 4 : « Aulu-Gelle (*Nuits attiques*, XIII, 18) » — chapitre à contrôler (XIII, 19 ?) ; le corpus local ne contient pas de texte latin d'Aulu-Gelle [à vérifier].
- 21, note 4 : « Aristote (Περὶ ποιητικῆς, XIII, 1458b22) » — le passage cité (φαγέδαιναν ἥ μου σάρκας ἐσθίει ποδός…) est au chapitre **22** de la *Poétique* (1458b19–24 ; vérifié sur le texte Perseus du corpus local), non XIII. Non corrigé (référence).
- 30–3 : l'explication du jeu sur le nom d'Agathon (« Mnésiloque joue sur le nom d'Agathon ; *nomen omen* […] aux dépens de l'original bien connu.) ») est passée au commentaire critique avec le reste, parce qu'elle porte l'argument en faveur de ἀγαθῶν. Le commentaire de la pièce n'a donc plus rien pour les vv. 30–33, alors que la traduction (« Est-ce l'un de ces honnêtes hommes… ») suppose ce jeu de mots : l'auteur voudra peut-être en garder une version brève dans le commentaire.
- 30–3 : faits de R à **vérifier sur l'image** (CLAUDE.md) : au v. 32, indication de personnage μ(ν)η grattée (*ut videtur*), οὐχ ἑόρακα (sans ς), scholie ἐπειδὴ οὐ πάλαι… écrite au-dessus du vers ; d'après l'apparat de l'auteur, v. 33 omis par R^ac et ajouté en marge.
- 30–3 : « [sept, en réalité, et selon la façon grecque de compter] » — à vérifier : de la victoire d'Agathon (416) aux *Thesmophories* (411), on compte cinq ans, six en compte inclusif. Peut-être l'auteur compte-t-il depuis les débuts d'Agathon et non depuis sa victoire [à vérifier].
- 30–3 : « Le signe mis pour signifier un changement d'interlocuteur […] ayant par la suite été gratté (*ut videtur*). » — phrase sans verbe principal, laissée telle quelle.
- 35 : l'article ne dit pas que βεβίνηκας est, dans R, **corrigé de βεαίνηκας** (Velsen 1883 : « βεβίνηκας] corr. ex βεαίνηκας R », d'après le répertoire critique). Ce fait touche directement la *crux* et la piste βαίνω (`\eff` l. 869). L'auteur l'avait développé dans un long brouillon mis en commentaire (l. 821–868 : remarque de Velsen ; ΒΕΒΑΙΝΗΚΑC ; passages recopiés : *Lys.* 56 sqq. et 966 καὶ μὴ βινῶν τοὺς ὄρθρους, *Héraclides* 101–105, *Eccl.* 911 sqq. ; numéros vérifiés sur le corpus local). **À vérifier sur l'image**, puis à intégrer au commentaire critique.
- 39–40 : le lemme porte **λέως** (R et Suid. codd. AF selon l'apparat de l'auteur), le texte établi **λαός** (Σ, Suid. codd. GIVM). La note 1 (scholie : παρὰ τοῖς τραγικοῖς οὕτω λέγεται, « πᾶς ἔστω λαός ») est le seul appui de ce choix, mais l'article n'en discute pas : lemme à harmoniser, et la question λέως / λαός mérite un article critique.
- 41–2 : « une meute de guerriers (*Phaéton*, v. 796) » — le passage est *Phéniciennes* 796 ἀσπιδοφέρμονα θίασον ἐνόπλιον (vérifié sur le texte Perseus du corpus local, comme *IA* 1059 et *IT* 1146 cités juste avant). Non corrigé (référence).
- Lemmes (mineur) : 1–4 s'arrête au v. 3 (… ἐκβαλεῖν) ; 16–8 porte πρῶτα (R) là où le texte imprime πρῶτ᾽ (Grynaeus).
