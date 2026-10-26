# f174r (vv. 959–1001) — répartition commentaire critique / commentaire de la pièce

Source : `commentaire.tex` (conversion de `latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex`,
l. 3300–3305 et 3407–3416). Règles : `edition/CONVENTIONS.md` § 3 et § 7. Articles critiques :
`critique.tex` (`\cc`) ; commentaire de la pièce : `commentaire.tex` (`\comm`). Rien n'a été supprimé.
État initial (révision db90b04) sauvegardé dans `.travail/f174r/commentaire.orig.tex`. L'article sans lemme
947–1000 (chant et danse ; structure du passage), qui couvre aussi les vv. 959–1000, est rangé au f173v (scindé :
la structure est dans `f173v/critique.tex`).

**État** : **terminé** (2026-10-26). 3 articles : **0 CRITIQUE**, **0 MIXTE**, **3 PIÈCE** (982, 1001, 1001),
tous conservés dans `commentaire.tex` ; `critique.tex` ne contient aucun article `\cc` (seulement un en-tête en
commentaire LaTeX ; le registre vide n'est pas imprimé). Compilation : `./edition/compiler_folio.sh f174r` — OK,
7 pages ; deux avertissements préexistants, étrangers à la répartition (ils se produisent à l'identique avec le
`commentaire.tex` du début de la reprise) : `Missing character ͡ (U+0361) in cmmi10` (signe métrique du v. 994,
`texte.tex`) et un `Overfull \hbox` de 2,0 pt au début du second alinéa de l'article 1001 τοξότης (« À Athènes,
comme partout ailleurs… »). Contrôle : `outils/controle/repartition_commentaire.py db90b04 f174r` → 319 mots
→ 319, 3 disparus (μὲν, σιμή, cette) et 3 ajoutés (μὴν, σιμὴ, cet), soit exactement les trois coquilles
corrigées ; accolades équilibrées (18/18), 3 `\comm`, 1 `\nc`, comme dans l'original.

**Reprise** (2026-10-26) : une première exécution avait classé les trois articles (tous PIÈCE, d'après
l'en-tête de `critique.tex`), traité l'article 982 et corrigé deux coquilles dans sa citation de Pollux. Je
contrôle ces corrections (exactes : voir « Coquilles corrigées »), je traite les deux articles du v. 1001 et
je complète le compte rendu.

## Articles

| n° | Plage | Lemme (abrégé) | Classement | Action |
|---|---|---|---|---|
| 1 | 982 | διπλῆν | PIÈCE (danse : la διπλῆ, figure de la danse tragique ; Pollux, Hésychius) — la leçon χαίρειν de R (χάριν Ellebodius dans l'apparat antérieur) n'y est pas discutée | reste dans `commentaire.tex` ; 2 coquilles corrigées dans la citation de Pollux (première exécution ; contrôlées sur Bethe) |
| 2 | 1001 | τοξότης | PIÈCE (le personnage : jargon mi-scythe mi-grec, note de Willems ; realia : les archers scythes, police d'Athènes aux ordres des prytanes, *Ach.* 54, *Prot.* 319c, bibliographie ; Platon et les gardiens de la Cité, *Quis custodiet…*) — aucune question textuelle | reste dans `commentaire.tex` avec sa note `\nc` ; 1 coquille corrigée ; passages signalés (voir plus bas) |
| 3 | 1001 | ἐνταῦτα νῦν οἰμῶξι πρὸς τὴν αἰτρίαν | PIÈCE (langue : transposition en attique du parler barbare de l'archer, = ἐνταῦθα νῦν οἴμωζε πρὸς τὴν αἰθρίαν ; jeu de scène : « le sadisme proprement argousin de l'archer ») — la leçon de R (« οἰμώξει R : οἰμῶξι Brunck » dans l'apparat antérieur ; οἰμώζει selon l'inventaire graphologique) n'y est pas discutée | reste dans `commentaire.tex`, inchangé ; voir « Passages signalés » |
<!-- fin du tableau -->

## « nous » d'auteur changés en « je »

Aucun : les trois articles n'ont pas de « nous » d'auteur (ni « je ») ; les « nous » présents sont génériques ou
associent le lecteur (voir ci-dessous).
<!-- fin nous changés -->

## « nous » conservés

- **982** « Hésychius (δ 1948) ne nous apprend rien davantage » ; « Il nous est difficile de reconstituer,
  même grossièrement, la chorégraphie » (nous génériques : les modernes, le lecteur compris).
- **1001** (τοξότης), note : « c'est assez bien établi par notre pièce » (la pièce commentée, commune à
  l'auteur et au lecteur ; cf. « notre passage », conservé aux folios précédents).
<!-- fin nous conservés -->

## Coquilles corrigées

- **982**, Pollux IV 105 : « Καὶ μ**ὲ**ν τραγικῆς ὀρχήσεως » → « Καὶ μ**ὴ**ν » ; « σιμ**ή** χείρ » → « σιμ**ὴ**
  χείρ » (grave devant un mot). Corrections de la première exécution, contrôlées sur E. Bethe, *Pollucis
  Onomasticon*, I (1900), p. 232, l. 10 (OCR d'archive.org `pollucisonomasti01polluoft`, grec translittéré :
  « Kai ^fjv TpaTiKfic ^pxfjceiuc cxf|jLiaTa ci)ufi x^ip », soit καὶ μὴν τραγικῆς ὀρχήσεως σχήματα σιμὴ χείρ ;
  copie dans `.travail/f174r/telech/`). Le reste de la citation concorde avec Bethe (καλαθίσκος, χεὶρ
  καταπρανής, ξύλου παράληψις, διπλῆ, θερμαυστρίς, κυβίστησις, παραβῆναι … τέτταρα).
- **1001** (τοξότης) : « C'est ce**tte** inquiétant contraste » → « C'est ce**t** inquiétant contraste »
  (*contraste* est masculin ; la source, l. 3408, porte la même faute).
<!-- fin coquilles -->

## Passages signalés (non modifiés)

- **982** : références contrôlées. Pollux IV 105 (Bethe, voir ci-dessus) ; Hésychius δ 1948 διπλῆ· ὀρχήσεως
  εἶδος, ἢ κρούματος, texte identique à celui de Latte–Cunningham, t. I (2018), p. 621, où l'apparat des sources
  renvoie à « Poll. 4,105 » (`.sources/drive/fichiers/Grec/Lexiques/Hesychius/Latte_I_alpha-delta.pdf`, page lue
  sur l'image, la couche texte du PDF étant illisible).
- **1001** (τοξότης) : « une sorte de **parler nègre** » (note de Willems, reprise telle quelle) : expression
  datée, aujourd'hui blessante ; à reconsidérer par l'auteur. La note n'a pu être contrôlée sur la traduction de
  Willems (1919), absente de `.sources/` [à vérifier].
- **1001** (τοξότης) : « un contingent de 300 **mercenaires** Scythes » : les trois cents archers scythes ont été
  achetés par la cité (Andocide, III 5 : τοξότας τριακοσίους Σκύθας ἐπριάμεθα ; Eschine, II 173 : τριακοσίους
  Σκύθας ἐπριάμεθα ; vérifiés dans le corpus local, Perseus) ; c'étaient des esclaves publics, comme le dit le
  titre de l'article de Couvenhes cité dans la note. « Mercenaires » est donc inexact. Non modifié.
- **1001** (τοξότης), note : « l'article plus ancien d'**Agnès** Plassart « Les archers d'Athènes » » : l'article
  (*REG* 26, 1913, n° 117, p. 151-213 : pages exactes) est d'**André** Plassart (1889-1978). Persée l'indexe sous
  « Plassart, Agnès », avec « Plassart, André » comme autre forme du nom (notice d'autorité 236502), d'où sans
  doute l'erreur ; Couvenhes écrit « A. Plassart ». Erreur de référence, non de frappe : non modifiée [à corriger
  par l'auteur].
- **1001** (τοξότης), note : l'article de J.-Chr. Couvenhes s'intitule en entier « L'introduction des archers
  scythes, esclaves publics, à Athènes : la date et l'agent d'un transfert culturel », dans B. Legras (dir.),
  *Transferts culturels et droits dans le monde grec et hellénistique*, Paris, Publications de la Sorbonne, 2012,
  p. 99-118 (page de l'éditeur sur OpenEdition, `books.openedition.org/psorbonne/9542`). Les pages sont exactes ;
  le sous-titre et le nom de l'éditeur scientifique manquent. Non modifié.
- **1001** (τοξότης) : « \latin{Quis custodiet custodes?} » : Juvénal, VI 347-348, porte *sed quis custodiet
  ipsos / custodes?* (texte de The Latin Library, où ces vers sont entre crochets). La citation, abrégée et sans nom
  d'auteur, est laissée telle quelle.
- **1001** (τοξότης), note : références contrôlées dans le corpus local (Perseus). *Acharniens* 54 : οὐ γὰρ
  διδόασιν οἱ πρυτάνεις. — ΚΗ. οἱ τοξόται (le héraut appelle les archers ; « 54b » chez Hall–Geldart) ;
  Platon, *Protagoras* 319c : ἢ οἱ τοξόται αὐτὸν ἀφελκύσωσιν ἢ ἐξάρωνται κελευόντων τῶν πρυτάνεων.
- **1001** (τοξότης) : graphie « Scythes » avec majuscule pour l'adjectif (« mercenaires Scythes », « archers
  Scythes ») ; minuscule dans le titre de Couvenhes (« archers scythes »). Question d'usage, non de frappe : non
  modifié.
- **1001** (ἐνταῦτα…) : la glose « $=$ … οἴμωζε … » fait de οἰμῶξι un impératif présent ; la traduction de
  l'auteur (« Ici maintenant, tu vas crier, en plein air », `texte.tex`) rend plutôt un futur. Pour R, l'apparat
  antérieur porte « οἰμώξει R : οἰμῶξι Brunck », mais l'inventaire graphologique de la page
  (`ravennas/graphologie/folios/f174r.jsonl`, l. 43) lit **οἰμώζει** (certitude « probable ») et rappelle que ξ et ζ
  se ressemblent dans cette main (ξ de ἔξαιρε, l. 23 ; ζ de παίζει, l. 18). À trancher sur l'image pour l'apparat et
  le texte ; si la leçon est discutée, ce sera au commentaire critique. L'article, qui ne fait que gloser la forme
  imprimée, reste au commentaire de la pièce.
- **1001** (ἐνταῦτα…), source l. 3414 : suite de l'article mise en commentaire (`%`) par l'auteur, non imprimée en
  2023 et non reprise : « : il dit à Mnésiloque qu'il va pouvoir gémir au grand air (οἰμῶξι πρὸς τὴν αἰτρίαν) au
  moment même où il lui coupe le sifflet et serre la vis qui l'étrangle. » (elle développait « Noter le sadisme
  proprement argousin de l'archer »). Source l. 3412 : note vide `%\note{2}{}`, désactivée, sans appel dans l'article.

### Passages marqués en orange (`\eff`) dans la source

Un seul `\eff` dans la partie de la source qui correspond à ce folio (vv. 959–1001), dans une ligne désactivée
(`%`) : il n'était pas imprimé en 2023 et la conversion ne l'a pas repris. Rien n'a été ajouté au commentaire.

- **990** (l. 3343, ébauche d'article sans lemme) : `%\commentaire{990}{}{\eff{Hésychius ε 6909 εὐΐων·
  Διονυσιακῶν} (Ευρ. Βαϲϲ 791...) εὐϊάζω = εὐάζω Eur. Cycl. 495.}` : notes pour un article sur εὔιον (v. 990, que
  le texte établi imprime entre obèles). Références contrôlées : Hésychius ε 6909 εὐΐων· Διονυσιακῶν (Eur. Bacch.
  791), dans Latte–Cunningham, t. IIa (2020), p. 288 (page lue sur l'image) ; Euripide, *Bacchantes* 791 (κινοῦντα
  βάκχας σ᾽ εὐίων ὀρῶν ἄπο) et *Cyclope* 495 (μάκαρ ὅστις εὐιάζει), corpus local (Perseus). « Ευρ. Βαϲϲ » =
  Eur. *Bacch.*, abréviation écrite en lettres grecques.
- Hors folio : le `\eff` de la l. 3425 (`%\commentaire{}{}{\eff{Souda} Σχάσον}`) se rapporte au v. 1003
  (χάλασον τὸν ἧλον), qui est au f. 174v ; il relève du compte rendu de ce folio.

### Autres passages mis en commentaire (`%`) par l'auteur, non repris (pour mémoire)

Entrées d'apparat désactivées dans la même partie de la source ; elles concernent le futur apparat et, le cas
échéant, le commentaire critique, non le commentaire de la pièce : 967 `ὥσπερ R : ὡς πρὸς Austin` (l. 3229) ;
987 `γ᾽ ὧδ᾽ suspectum` (l. 3324) ; 990 `εὔιον R : Εὔιε Enger : Εὐοῖ Hermann (1845)` (l. 3341) ; 993
`(Gr. Versk. p.476)` après Wilamowitz (l. 3356) ; 994 `εὔιον εὔιον R : ὦ Εὔι Εὔι' Hermann` (l. 3357 ; l'entrée
complète, déplacée, subsiste désactivée à la l. 3362) ; 995 `συγκτυπεῖται Wilamowitz` (l. 3373).
<!-- fin signalés -->
