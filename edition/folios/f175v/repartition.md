# f175v (vv. 1082–1126) — répartition commentaire critique / commentaire de la pièce

État : **terminé** (2026-10-26). 14 articles : **7 CRITIQUE** (1083, 1086, 1090, 1091, 1093, 1094, 1114)
déplacés ; **aucun MIXTE** ; **7 PIÈCE** conservés. `critique.tex` compte 7 articles `\cc`, `commentaire.tex`
7 articles `\comm`. Compilation (`./edition/compiler_folio.sh f175v`) : OK, 7 pages.

Source : `edition/folios/f175v/commentaire.tex` (conversion de `latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex` :
articles aux l. 4561–4830 ; passages désactivés examinés sur toute l'étendue du folio, l. 4545–4870).
Règles : `edition/CONVENTIONS.md` § 3 et § 7. Copie de l'original : `.travail/repartition/f175v/commentaire.orig.tex`
(non versionné ; l'original est aussi dans git, commit 5ae2914). Contrôle mot à mot
(`.travail/repartition/f175v/comparer.py`) : les 14 articles d'origine sont tous présents, texte et notes
inchangés, sauf les modifications énumérées ci-dessous. Rien n'a été supprimé.
Classement : CRITIQUE (discute le texte), PIÈCE (interprétation, langue, realia, mise en scène…), MIXTE (scindé).

## Tableau des articles

| n° | Plage | Lemme (abrégé) | Classement | Action |
|---|---|---|---|---|
| 1 | 1082 | ὀτότυζ᾽ --- ὀτότυζ᾽ | PIÈCE | Conservé (jeu de consonance Ὀτοτύξιοι / Ὀλοφύξιοι des *Oiseaux* : question d'interprétation, aucune leçon discutée ; voir, aux passages signalés, la conjecture désactivée ὀλόφυγ᾽). « nous espérons » → « j'espère ». |
| 2 | 1083 | λαλῖς | CRITIQUE | Déplacé tel quel → `\cc{1083}` (scholie sur la graphie sans ε : témoignage sur l'orthographe à imprimer, λαλῖς). |
| 3 | 1085 | σί κακόν; | PIÈCE | Conservé (glose du scholiaste sur le jargon scythe ; la scholie se lit en marge droite de R, l. 4 : ἀντὶ τοῦ σοὶ κακόν). |
| 4 | 1086 | πρωτε το πωνη; | CRITIQUE | Déplacé tel quel → `\cc{1086}`, avec sa note (leçon de R πρωτε, correction πωτε d'une main postérieure, contre l'interprétation πόθεν de la scholie). |
| 5 | 1089 | κακκασκι μοι; | PIÈCE | Conservé (équivalent attique ; *Guêpes* 721 et la scholie). |
| 6 | 1090 | μὰ Δί᾽ ἀλλὰ γυνὴ πλησίον αὕτη | CRITIQUE | Déplacé tel quel → `\cc{1090}` (attribution de la réplique au chœur, d'après la scholie, contre les éditeurs). |
| 7 | 1091 | πλησίον αὕτη | CRITIQUE | Déplacé → `\cc{1091}` (justification de la conjecture de l'auteur πλήξασ᾿ αὕτη, imprimée dans `texte.tex` ; l'analyse du jeu de scène est l'argument de la conjecture et la suit donc). « il nous semble » → « il me semble ». |
| 8 | 1093 | ποῖ ποῖ φεύγεις; | CRITIQUE | Déplacé → `\cc{1093}`, avec sa note (lacune ; restitution de la réplique d'Écho ποῖ ποῖ πέτει, imprimée dans `texte.tex` ; la mise en scène — envol par la μηχανή — et les onomatopées des *Oiseaux* sont les arguments de la restitution). Deux coquilles corrigées. |
| 9 | 1094 | <οὐ καιρήσεις.> --- οὐκ᾽ αἰρήσεις | CRITIQUE | Déplacé tel quel → `\cc{1094}` (réplique omise par R, restituée d'après la scholie). |
| 10 | 1098–102 | ὦ θεοὶ … κάρα κομίζων | PIÈCE | Conservé (source parodiée : scholie ; *Andromède* fr. 124 Kannicht en note). |
| 11 | 1102–3 | τί λέγι; τὴ Γόργος πέρι / … | PIÈCE | Conservé (jargon ramené à l'attique ; scholie sur Gorgos ; jeu Γοργών / Γόργων). L'article ne discute pas les données textuelles de ces vers (absents du texte de R, ajoutés dans la marge inférieure, ce que montre l'image ; Γόργος Σ, Bothe : apparat de l'auteur). |
| 12 | 1105 | ἔα· τίν᾽ ὄχθον τόνδ᾽ ὁρῶ καὶ παρθένον | PIÈCE | Conservé (texte parodié, *Andromède* fr. 125 Kannicht, d'après la scholie). |
| 13 | 1106 | ναῦν ὅπως ὡρμισμένην; | PIÈCE | Conservé (même image dans *Héraclès* 1094–1097). |
| 14 | 1114 | σκέψαι τὸ σκύτο· | CRITIQUE | Déplacé → `\cc{1114}` (faute de R σκύτο pour κύστο, métathèse du σ comme au v. 557 ; scholie ; σ de première main devant ποστίον au v. « 1187 »). Une coquille corrigée. |

<!-- fin du tableau -->

## « nous » d'auteur changés en « je »

- Commentaire 1082 : « Signalons à l'attention du lecteur -- que **nous espérons** exégète à ses heures -- » → « que **j'espère** exégète à ses heures ».
- Critique 1091 : « Après un long calvaire […], il **nous** semble enfin saisir le sel ἐπικοκκάστρια de la réplique d'Écho » → « il **me** semble » (la conjecture πλήξασ᾿ αὕτη est celle de l'auteur).

<!-- fin nous-je -->

## « nous » conservés

- Commentaire 1082 : « Signalons à l'attention du lecteur » — cas limite : l'impératif ne désigne ici que l'auteur (le lecteur est le destinataire), mais il ne peut passer au singulier sans récrire la phrase (« Je signale à l'attention du lecteur ») ; conservé, comme les « Signalons » de f164r et f169r et le cas limite de f172v. À changer si l'auteur le souhaite.
- Critique 1093 : « ne nous étonnons donc pas », « Remettons-nous bien la scène » (impératifs qui associent le lecteur) ; « nous ne sommes pas tout-à-fait démunis puisque nous possédons une comédie entière » (« nous » générique : les lecteurs modernes d'Aristophane) ; « dans notre passage » (possessif commun).

<!-- fin nous conservés -->

## Coquilles corrigées

- Critique 1093 : « on comprend mieux pourquoi lorqu'Iris descend du ciel » → « lorsqu'Iris ».
- Critique 1093 : « (cf. le vers 1094 ; où la lacune est certaine » → « (cf. le vers 1094, où la lacune est certaine » (point-virgule fautif devant la relative).
- Critique 1114 : « τὸ \textbf{σ}ποστίον à la de τὸ πόστιον » → « à la place de τὸ πόστιον » (mot omis ; la source porte déjà « à la de », l. 4830).

<!-- fin coquilles -->

## Renvois ajoutés

Aucun (pas d'article MIXTE).

<!-- fin renvois -->

## Passages signalés (conservés tels quels)

### Passages `\eff` et brouillons désactivés de la source

- l. 4757, dans l'article 1102–3, après la scholie (désactivé par `%`, donc absent de la conversion) : `\eff{mais la scansion ?..}` — doute de l'auteur sur la scansion (Γόργος dans le trimètre ?). C'est le seul `\eff` de l'étendue du folio.
- l. 4560 (v. 1081b) : entrée d'apparat désactivée « ὀτότυζ᾽ R : ὀλόφυγ᾽ Bibi », conjecture de l'auteur qui répond à la question de l'article 1082 (« Y a-t-il ici un jeu analogue ? ») ; si l'auteur la reprend, l'article deviendra critique (ou mixte).
- Autres brouillons désactivés, non convertis : 1086, à la suite de l'article (l. 4605) et dans sa note (l. 4608–4610) : « Faut-il aller chercher une explication du côté d'Hésychius ? (γ 962) : γρωθώνη· σαπρὰ γραῦς· οἱ δὲ τὴν παλαιὰν ὄνον ἢ σῦν » ; 1086, réplique d'Écho (l. 4617) : `\commentaire{1086}{}{Hésychius : πρόπωνα: …}` ; 1088 (l. 4638) : `\commentaire{1088}{}{Hésychius 2856 κλᾶις:μοχλός 2881 χλαῦσιν:ἀγῶνα,ἄνθοςτι}` ; 1119 (l. 4846) : `\commentaire{1019}{τῶ πρωκτῶ}{Le prokton peut donc être (mal-)employé au pluriel. \cf la scène où Mnésiloque a le feu aux fesses.}` (numéroté 1019 pour 1119).

### Leçons de R contrôlées sur l'image (f175v ; f176v pour le v. 1188)

Découpes : `.travail/repartition/f175v/images/` (`v_*.jpg`, `f176v_*.jpg`).

- 1086 : aux deux occurrences de la l. 5, π, puis un trait horizontal, puis ωτε ; aucun ρ visible (ρ gratté et intervalle comblé par un trait) : compatible avec « le *Ravennas* comporte πρωτε », corrigé en πωτε (de même von Velsen 1883 : « πρῶτε R corr. in πωτε R² »).
- 1090 : dans la marge gauche de la l. 9, R porte le sigle **σκ** (Σκύθης), de même forme qu'aux l. 8 et 11 ; la Juntine, imprimée sur R, donne elle aussi le vers à l'archer (Enger 1844, p. 181 : « Σκ. praefig. Junt. »). L'article n'en dit rien. Enger corrige par ailleurs la scholie en « τοῦτο ἡ ἠχὼ ἢ ὁ γέρων » (R : τοῦτο ὁ χο(ρὸς) ἢ ὁ γέρων, χο abrégé). Ces deux données sont à intégrer à la discussion et à l'apparat. « Aucun éditeur cependant n'a suivi la première hypothèse du scholiaste » : affirmation non contrôlée [à vérifier].
- 1094 : à la l. 12, R écrit à la suite, après le signe +, ποῖ ποῖ φεύγεις ου κ‿αιρήσεις : la menace n'y figure qu'une fois, d'où la lacune. La coupe οὐκ᾽ αἰρήσεις du lemme est plausible (deux signes au-dessus de κα / αι, apostrophe et esprit ?), mais elle n'est pas sûre à cette résolution (κ lié à α). Scholie en marge droite : ἀντὶ τοῦ οὐ χαιρήσεις (χα retouché).
- 1114 : σκέψαι τὸ σκύτο μῆτι· μικτὸν… se lit bien ainsi dans R, et la scholie de la marge gauche porte bien δείκνυσιν αὐτῷ τὸ αἰδοῖον.
- 1114, « Second fait remarquable » : sur f176v, devant ποστί(ον), trace pâle d'une lettre grattée (σ) : compatible avec τὸ σποστίον de première main. Mais ce vers est le **1188** (εἶεν· καλὴ τὸ σκῆμα περὶ τὸ πόστιον), dans la numérotation de Hall–Geldart, dans `texte.tex` et dans l'apparat de l'auteur lui-même (« 1188 τὸ \inRas{σ}{}ποστίον \Rpc », source l. 5214), et non le 1187 : renvoi à corriger (non corrigé, puisque c'est une référence).

### Renvois et références

- Critique 1094 : « \italique{Confer} la note \italique{supra} au vers 1056 » : la discussion visée (scholie ἀντὶ τοῦ οὐ χαιρήσεις, menace οὐ καιρήσεις et écho οὐχ αἱρήσεις, Wilamowitz) se trouve à l'article **1059** (Ἠχὼ λόγων ἀντῳδὸς ἐπικοκκάστρια), passé au commentaire critique de f175r (`f175r/critique.tex`, `\cc{1059}`). Renvoi à corriger ; non corrigé.
- Critique 1086, note (« la seconde note du commentaire au vers 1080 ») et critique 1114 (« cf. le commentaire à ce vers », v. 557) : les articles visés existent (`f175r/critique.tex`, `\cc{1080}`, 2e note ; `f169r/critique.tex`, `\cc{556–7}`). Ils sont désormais au commentaire critique, et les renvois restent valables.
- Commentaire 1082 : « au vers 1043 des *Oiseaux* … Ὀλοφύξιοι (v. 1042) » : dans Hall–Geldart (corpus local, Perseus), Ὀλοφύξιοι est au v. 1041 et ὡτοτύξιοι au v. 1042 [à vérifier sur l'édition suivie par l'auteur].
- Critique 1093 : « En *Oiseaux* 226 … ἐποποποῖ ποποῖ, ποποποποῖ ποποῖ » et « au vers 310 … ποποποποποπο ποῦ μ' ὃς ἐκάλεσε; ». Hall–Geldart donne au v. 226 οὕποψ μελῳδεῖν αὖ παρασκευάζεται, puis le chant au v. 227 (ἐποποῖ ποποποποποποποῖ), et aux vv. 310–311 ποποποποποποποποποποῖ ποῦ μʼ ἄρʼ ὃς / ἐκάλεσε; (ἄρ᾽ manque dans la citation). Citations à collationner sur l'édition suivie (la graphie des onomatopées varie selon les éditions).
- Vérifiés sans écart : *Oiseaux* 1199 (αὕτη σύ, ποῖ ποῖ ποῖ πέτει;) ; *Guêpes* 721 (ἐγχάσκειν) ; *Héraclès* 1094–1097 (la citation omet seulement le ἰδού initial du v. 1094) ; L. Di Virgilio, « Some thoughts on humor and music in Aristophanes' plays », *Mediterranean World* 24 (2019), p. 31–60 (« pp. 36 sqq. » est donc compatible).

### Remarques de forme (non corrigées : ce ne sont pas de simples fautes de frappe)

- Commentaire 1089 : « $=$ καὶ ἐγχάσκει μοι » est à la 3e personne, alors que la scholie (καταγελᾷς μοι) et la traduction (« Tu te gausses de moi ») comprennent une 2e personne (ἐγχάσκεις ?).
- Critique 1086 : « la correction `πωτε' (qu'une main postérieure a corrigé sur le manuscrit…) » : tournure (et accord) à revoir (« a introduite » ?).
- Critique 1093 : « C'est ce coup qu'il est bon de partir » : il manque sans doute « à » (« C'est à ce coup… »). Dans « Euripide de déloger sans trompette (καὶ δὴ φεύγει) mais non sans abandonner sa verve moqueuse », le sens demande « mais sans abandonner » (ou « non sans garder »).
- Commentaire 1102–3 : dans la scholie « ὁ δὲ Γόργος γραμματεὺς, ἀλλὰ καὶ βάρβαρος », l'accent grave devant la virgule devrait être aigu (γραμματεύς,).

### Hors du champ de la tâche (pour mémoire)

- Numérotation : les plages 1082 (ὀτότυζ᾽ : v. 1081b chez Hall–Geldart et dans `texte.tex`), 1083 (λαλῖς : v. 1082 de `texte.tex`) et 1089 (κακκασκι : v. 1088 de `texte.tex`) suivent la numérotation de l'auteur, décalée d'un vers. Elles ne sont pas modifiées (à harmoniser). Sur l'image, f175v s'ouvre (l. 1) sur ὀτότυζε· ηχ ὀτότυζε·, alors que `texte.tex` range cette réplique à la fin de f175r (rangées `[suite]` du v. 1081) : borne de folio à revoir.
- `texte.tex`, v. 1104 : la colonne française reproduit le grec « ἔγωγε φημί. » au lieu de le traduire.
- Les remarques de mise en scène des articles 1091 (coup porté par Euripide) et 1093 (envol d'Écho par la μηχανή) ne figurent plus qu'au commentaire critique. Si l'auteur le souhaite, un renvoi bref pourra être ajouté au commentaire de la pièce.

<!-- fin signalés -->
