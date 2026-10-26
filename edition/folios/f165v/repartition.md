# f165v (vv. 252–293) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f165v/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 2389–2685 ; articles
C0084–C0097 de `edition/donnees/travaux_anterieurs/commentaires.tsv`).
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).
Texte et notes conservés mot pour mot, sauf les corrections listées ci-dessous.

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé : partie textuelle dans `critique.tex`,
reste dans `commentaire.tex` avec le renvoi « Pour le texte, voir le commentaire critique. »).

État : **terminé** (2026-10-26). 14 articles : **1 CRITIQUE** (255), déplacé ; **4 MIXTE**
(263, 273, 289, 291), scindés ; **9 PIÈCE**, conservés. `critique.tex` compte 5 articles `\cc`
(255, 263, 273, 289, 291), `commentaire.tex` 13 articles `\comm`. Le folio compile
(`./edition/compiler_folio.sh f165v` : 7 pages).

Reprise : la répartition des 14 articles a été faite par une exécution concurrente, dont les
outils sont dans `.travail/f165v/` (original sauvegardé dans `commentaire.orig.tex`, outil de
répartition `repartir.py`, contrôle `verifier.py`). Cette exécution s'est arrêtée avant le
compte rendu. Je l'ai reprise sans dupliquer d'article : j'ai contrôlé la répartition,
corrigé une coquille de plus (263) et rédigé les sections qui suivent le tableau.

## Articles

| # | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|
| 1 | 255 | σύζωσον ἀνύσας — αἶρε νῦν στρόφιον | CRITIQUE (répartition des répliques ; *dicôlon* de R entre ἀνύσας et αἶρε ; σύζωσον ἀνύσας à Agathon, αἶρε νῦν στρόφιον à Euripide, ἰδού à Agathon) | déplacé en entier dans `critique.tex` (`\cc{255}`), inchangé ; les remarques sur l'attitude d'Agathon et le ton de la réplique sont les arguments de l'attribution |
| 2 | 258 | κεφαλὴ περίθετος… νύκτωρ φορῶ | PIÈCE (realia : la perruque, Pollux X, 170 ; la scholie et le v. 35) | reste dans `commentaire.tex` ; 1 « nous » → « je » ; 1 coquille corrigée |
| 3 | 261 | φέρ᾽ ἔγκυκλον | PIÈCE (realia : l'encycle ; renvoi à la note du v. 643) | reste dans `commentaire.tex`, inchangé |
| 4 | 263 | ἆρ᾽ ἁρμόσει μοι — χαλαρὰ γοῦν χαίρεις φορῶν | MIXTE : sens de la réplique et realia (souliers étroits de l'élégant, d'après la note 6 de Willems) / attribution des répliques (χαλαρὰ… à Agathon avec R, contre Brunck ; la scholie ; σὺ τοῦτο γίγνωσκ᾽ à Mnésiloque et changement de locuteur à ἀλλ᾽, répartition de Bibi selon l'apparat de la source) | scindé : `\cc{263}` = « Seulement, Brunck eut l'idée saugrenue… » jusqu'à la fin (sortie d'Agathon comprise, qui découle de la répartition du v. 264) ; `\comm{263}` garde les deux premiers paragraphes et la note 1, puis « Pour le texte, voir le commentaire critique. » ; 2 coquilles corrigées (1 au commentaire, 1 au critique) ; voir passages signalés (`\eff`, attribution à Brunck) |
| 5 | 265 | εἴσω τις… ἐσκυκλησάτω | PIÈCE (mise en scène : sortie par l'eccyclème ; parallèle *Ach.* 409) | reste dans `commentaire.tex`, inchangé |
| 6 | 272 | ὄμνυμι τοίνυν αἰθέρ᾽ οἴκησιν Διός | PIÈCE (parodie : citation de la *Mélanippe* d'Euripide, selon la scholie) | reste dans `commentaire.tex`, inchangé |
| 7 | 273 | τί μᾶλλον ἢ τὴν Ὑποκράτους ξυνοικίαν | MIXTE : la plaisanterie (les fils d'Hippocratès, « porcs » ; note de Willems avec Athénée et Photius) / leçon de R Ὑποκράτους conservée contre Ἱπποκράτους (jeu ὑ-, συ-ῳκία, υ-ἱοί) | scindé : `\cc{273}` = le dernier paragraphe (« Je conserve la leçon du manuscrit de Ravenne… » jusqu'à la fin) ; `\comm{273}` garde le reste et sa note, puis, après le saut de ligne `\\` de la source, « Pour le texte, voir le commentaire critique. » ; 1 coquille corrigée (critique) |
| 8 | 275–6 | ὅτι ἡ φρὴν ὤμοσεν / ἡ γλῶττα… | PIÈCE (parodie d'Eur. *Hipp.* 612 ; Érasme, Tosi ; jeu sur les *o*) | reste dans `commentaire.tex`, inchangé |
| 9 | post 276 | ὀλολύζουσι τε ἱερὸν ὠθεῖται | PIÈCE (mise en scène : changement de décor, eccyclème, signal, ὀλολυγή ; Hérodote, Homère), à la limite du MIXTE : le premier paragraphe décrit la parépigraphe et la coronis de R, la scholie et le papyrus, mais sans discuter le texte ; il sert de prémisse à la reconstitution scénique (« La maison d'Agathon est donc roulée… ») | reste dans `commentaire.tex` ; 1 coquille corrigée ; voir passages signalés |
| 10 | 280 | Θρᾷττα | PIÈCE (nom d'esclave thrace) | reste dans `commentaire.tex`, inchangé |
| 11 | 281 | ὑπὸ τῆς λιγνύος | PIÈCE (langue : ὑπό « avec, accompagné de » ; Photius, *Bibl.*) ; dimension textuelle implicite (voir passages signalés) | reste dans `commentaire.tex`, inchangé |
| 12 | 288 | εἰ δὲ μή, ἀλλὰ νῦν λαθεῖν | PIÈCE (mise en scène : aparté) | reste dans `commentaire.tex`, inchangé |
| 13 | 289 | καὶ τὴν θυγατέρα χοῖρον… | MIXTE : corruption de χοῖρον, leçon χοιρίον de la scholie, conjecture Χοιρίλ' (Bibi), contre les lectures obscènes (Willems) / lecture de la scène qui en résulte (pique de Mnésiloque contre son gendre Euripide) | scindé : `\cc{289}` = tout l'article jusqu'à « …est monnaie courante. », avec ses 4 notes ; `\comm{289}` = « Pour le texte, voir le commentaire critique. Mnésiloque profite donc… (cf. la note ci-dessous.) » ; 1 « nous » → « je » et 3 coquilles corrigés (critique) |
| 14 | 291 | καὶ πρὸς θάληκον νοῦν ἔχειν… | MIXTE : conjecture πρὸς θυλάκιον (Bibi) contre Ποσθαλίσκον (Dindorf) : Willems, Hésychius θ 50 θάλλικα, Pollux X, 152, la scholie / thème aristophanien (les femmes gardiennes de la bourse du ménage ; *Assemblée des femmes*, *Lysistrata*) | scindé : `\cc{291}` = tout l'article, sauf le paragraphe « Thème cher à Aristophane… à ce genre de prière. », avec ses 5 notes. Le paragraphe sur le sens d'après J.-V. Vernhes reste dans la partie critique, car la suite de l'argument y renvoie (« Si J.-V. Vernhes avait dû condenser son propos en grec… »). `\comm{291}` = « Pour le texte, voir le commentaire critique. Thème cher à Aristophane… » ; 1 « nous » → « je » et 3 coquilles corrigés (critique) |

## « nous » d'auteur changés en « je »

- 258 : « comme nous en avons fait l'hypothèse \italique{ad loc.} » → « comme j'en ai fait
  l'hypothèse \italique{ad loc.} » (l'hypothèse sur le v. 35).
- 289 (partie critique) : « Prions les déesses thesmophores de conférer à la nôtre assez de
  force » → « … à la mienne … » : « la nôtre » désigne la note de l'auteur, opposée à celle de
  Willems. « Prions » associe le lecteur et reste.
- 291 (partie critique) : « en montrant que notre conjecture est aussi compatible » → « … que
  ma conjecture … » (la conjecture πρὸς θυλάκιον, « Bibi »).

Gardés, parce qu'ils associent le lecteur ou appartiennent à une citation ou à une traduction :
- 258 : « pas plus renseigné que nous sur la question » (nous, les modernes) ; « notre
  poètereau » (Agathon ; possessif familier).
- 289 : « de nous infliger leur saleté morale » ; « N'allons pas inventer », « reportons-nous
  plutôt », « qui nous sont parvenus » ; « Prions ».
- 291 : « notre πρὸς θάληκον » (le texte transmis) ; « Finissons d'ailleurs cette note » ; « Et
  les mêlant nous dirions » (traduction de Pollux, εἴποιμεν).
- 273 : « je le sais » (traduction d'Athénée, οἶδα) et le « on » de la citation de Willems.

Ailleurs, l'auteur dit déjà « je » : 255 (« J'ai essayé », « J'ai confié », « me semble », « lui
ai-je accordé »), 273 (« Je conserve »), 291 (« que je crois », « j'ai aussi appris », « j'ai
reçu »).

## Coquilles corrigées

- 258 : Pollux X, 170, « καὶ ὡς Ἀριστφάνης ἐν Γηρυτάδῃ » → « Ἀριστοφάνης » (lettre omise).
- 263 (commentaire, citation de Willems) : « faire preuve de d'inélégance » → « faire preuve
  d'inélégance ». C'est la leçon de la note 6 de Willems (`latex/Aristophane-Thesmo Annexes.tex`,
  l. 690).
- 263 (critique) : « allusion aux mœurs sodomotiques d'Agathon » → « sodomitiques ».
- 273 (critique) : « ( littéralement \italique{nature de porc}) » → « (littéralement … » (espace
  parasite).
- post 276 : « c'est à-dire l'espèce » → « c'est-à-dire l'espèce ».
- 289 (critique) : « La preuve en est que scholiaste avait » → « que le scholiaste avait » (mot
  omis) ; « la fille qu'il lui a cédé en mariage » → « cédée » (accord) ; « la présence d'un
  nombre propre (rare) » → « d'un nom propre ».
- 291 (critique) : « Pour ce qui du †θάληκον† » → « Pour ce qui est du » (mot omis) ; « Si
  J.-V. Verhnes avait dû » → « Vernhes », la graphie du paragraphe précédent (« Jean-Victor
  Vernhes ») ; « formé sur τό θάλος » → « τὸ θάλος » (grave, et non aigu, devant le mot
  suivant).

Graphies laissées telles quelles, parce que ce sont des fautes d'usage ou des choix de style
plutôt que des fautes de frappe :
- 258 : « à priori » (a priori), « poètereau » (poétereau) ;
- 280 : « esclaves Thraces » (thraces) ;
- 291, n. 3 : « les \italique{Thesmophories} est la pièce » ;
- 255 : « pour ne pas que ce rustre aille » (tour familier, sans doute voulu).

## Passages signalés

### Passage marqué `\eff` (orange) dans la source

Il n'y en a qu'un pour les vv. 252–293 (j'ai contrôlé les l. 2352–2711). Il se trouve à la fin
de l'article 263, dans une ligne que l'auteur a mise en commentaire (`%`, l. 2472). La
conversion ne l'a pas repris, et je ne l'ai pas réintroduit :

> « En fait la correction est la bonne : Agathon est moqué ailleurs (Gérutades 178) comme mh
> xalara, c'est-à-dire non serré. Évidemment, les allusions scabreuses au trou-du-cul d'Agathon
> ne sont que pure imagination des fouines à ordure. Zénob. I 2 (cf. Diogenianus I 7) »

L'auteur semble y revenir sur la thèse de l'article, qui défend la répartition de R
(χαλαρὰ… à Agathon). « La correction » désigne vraisemblablement l'attribution du vers entier à
Mnésiloque. C'est aussi la solution de Willems (note 6), qui lit en outre γ᾽ οὐ : « M'iront-elles ?
car tu n'aimes pas à te chausser large ». Cette note contredit le texte établi (`texte.tex`
donne χαλαρὰ γοῦν χαίροις φορῶν à Agathon) et l'article critique 263. C'est à l'auteur de
trancher. Références de la note [à vérifier] : Ar. fr. 178 K.-A. (*Gérytadès*), Zénob. I 2,
Diogénien I 7.

### Art. 263 : l'attribution à Brunck est douteuse

L'article dit : « Brunck eut l'idée saugrenue de confier l'intégralité du vers 263 à
Mnésiloque ». Selon Fritzsche 1838 (p. 91–93, pages extraites dans
`.travail/f165v/fritzsche_p114.png` à `fritzsche_p116.png`), c'est autre chose :
- Brunck donnait χαλαρὰ γοῦν χαίρεις φορῶν; à Euripide, qui s'adresse à Mnésiloque (« Recte vero
  personas ordinavit Brunckius, ΜΝ. ἆρ᾽ — μοι; ΕΥΡ. χαλαρὰ — φορῶν; ΑΓΑΘ. σὺ τοῦτο —
  εἰσκυκλησάτω » ; traduction de Brunck : « Quidni? num laxos gestare amas? ») ;
- c'est Reiske qui attribuait le vers entier à Mnésiloque (« Neque enim Reiskius totum versum
  263 in Mnesilochum conferre debebat »).

Velsen 1883 va dans le même sens (répertoire critique, v. 263 : « posteriorem versus partem
Euripidi dedit Brunckius »). L'article (`\cc{263}`) et l'apparat de la source (« (Μνη.) Brunck,
edd. post. ») sont donc à contrôler sur les éditions de Brunck (1783) et de Reiske. Je n'ai rien
corrigé.

### Autres points

- 281 : l'article renvoie à la note 7 de Willems (`Annexes.tex`, l. 696–720). Cette note défend
  ὑπὸ τῆς λιγνύος (R) contre la « soi-disant correction de Reiske : ἀνέρχεται τῆς λιγνύος »,
  acceptée par « les derniers éditeurs » (van Leeuwen). L'article lui-même ne nomme ni Reiske ni
  la correction : il dit seulement le sens de ὑπό. Je l'ai donc laissé au commentaire de la
  pièce. L'apparat de la source n'a pas d'entrée au v. 281. Si l'auteur veut discuter la
  correction, il faudra une entrée d'apparat et un article critique (je n'ai rien rédigé).
- 273 : la note `\nc` « Comprendre : \italique{grossièreté}, \italique{lourdeur}… » (Taillardat,
  § 451 ; Érasme, n° 906) est placée dans `\citComm`, dans la traduction d'Athénée. Elle n'est
  pas composée dans le PDF, où seul l'appel « 1 » apparaît. C'est un défaut connu du moteur : les
  affectations de `\nc` sont locales et se perdent à la sortie du groupe (cf. f165r, art. 241–2).
  Je ne l'ai pas corrigé, car le moteur (`edition/thesmo.cls`) est partagé par tous les folios.
- 273 : la partie critique s'appuie sur « les textes cités par Willems » (ὑωδία, ὑηνία). Ces
  textes sont dans la partie restée au commentaire de la pièce.
- 263 : la partie critique commence par « Seulement, ». Ce mot répond au paragraphe resté au
  commentaire de la pièce (« Rien de plus clair… »). La leçon χαίροις (Suid.) contre χαίρεις (R)
  n'est évoquée qu'en passant, sans discussion : au commentaire (« Tu préférerais (χαίροις
  Suid.)… ») et au critique (« c'est bien Agathon qui prononce `χαλαρὰ γοῦν χαίροις φορῶν' »).
  Le lemme garde la leçon de R (χαίρεις, γ᾽ο\auDessus{ῦ}{ν}). Le répertoire critique note aussi
  la conjecture χαίρει de Velsen, dont l'article ne parle pas.
- 263 : `texte.tex` numérote le v. 263 « 260 » (l. 20 : `\vers[n=260]{ΜΝ.}{Mnésiloque}{ἆρ᾽
  ἁρμόσει μοι;}{Est-ce qu'elles m'iront ?}`). Le numéro 260 figure donc deux fois dans la marge
  du PDF, et `\comm{263}` s'ancre à la rangée du v. 264. C'est hors de mon périmètre : je ne l'ai
  pas corrigé.
- 289 : la parenthèse « (cf. la note ci-dessous.) », restée au commentaire de la pièce, vise
  l'article 291. Or la discussion de cet article (θυλάκιον, le porte-monnaie) est désormais au
  commentaire critique. Au commentaire de la pièce, l'article 291 ne garde que le paragraphe
  « Thème cher à Aristophane… », précédé du renvoi.
- 289 : pour mémoire, l'auteur doutait de Χοιρίλη dans des notes qu'il avait mises en commentaire
  (`%`) et que la conversion n'a pas reprises :
  - ancienne note 11 (l. 2704) : « L'épigraphie fait état de plusieurs Χοιρίνη tandis que le nom
    Χοιρίλη ne semble pas attesté » ;
  - ancienne note 12 (l. 2705) : « Je n'exclue d'ailleurs pas que ce fût peut-être la leçon
    originale ; le iota de `χοιρίον' ayant été ajouté d'après la scholie » (à propos de Χοιρίν᾽) ;
  - l. 2682–2684, sur l'identité du κηδεστής : « La question, pour moi, n'est toujours pas
    tranchée ».

  Le commentaire actuel ne mentionne Χοιρίνη qu'en note (« Certains manuscrits portent
  Χοιρίνη »). À l'auteur de dire si ces réserves doivent revenir au commentaire critique.
- 258 : « \italique{ad loc.} » vise l'hypothèse sur le v. 35. Elle se trouve maintenant au
  commentaire critique de f162v (`\cc{35}`, dont la note 1 renvoie elle-même au v. 258).
- post 276 : l'article est classé PIÈCE, à la limite du MIXTE (voir le tableau). Le lemme
  « ὀλολύζουσι τε » est la transcription de l'auteur. Velsen 1883 donne pour R « ὀλολύζουσί
  τε· » et rapporte la conjecture τὸ de Fritzsche (répertoire critique, au v. 277). L'article ne
  discute pas ce point textuel, et la lecture de R est à vérifier sur l'image.
- Lemmes et texte établi (je n'ai rien modifié) : 263 χαίρεις (R) / χαίροις (texte établi) ;
  289 χοῖρον (R) / Χοιρίλ' ; 291 θάληκον (R) / θυλάκιον. Les lemmes citent R, qui est l'objet de
  la discussion.
- Renvois à suivre quand les folios concernés seront répartis : 261, « la note au vers 643 » ;
  291, n. 5, « Voir au commentaire du vers 1175 un autre exemple ».

### Passages mis en commentaire (`%`) par l'auteur, non repris (pour mémoire)

- Testimonia mis en commentaire (`%\testimonia`) :
  - 254 : Suid. π 2114, Phot. π 1113, Hsch. π 3096 ;
  - 257–8 : Suid. π 1165 ;
  - 258 : Phot. π 690, Eust. 1280.63, Poll. II 35 ;
  - 261 : Suid. ε 135, κ 1809 ;
  - 263 : Suid. χ 7 ;
  - 274 : Hsch. α 7097 ;
  - 275–6 : Eust. 443.37 ;
  - 277–8 : Suid. σ 325 ;
  - 282 : Phot. α 1386, Ael. Dion. α 113 ;
  - 285 : Eust. 437.4 ;
  - 289 : Eur. test. 4, 18 Kannicht ;
  - 291 : Hsch. θ 50, Poll. X 152 ;
  - 292 : Phot. ρ 106.

  Ils sont à reprendre dans les *loci paralleli* (*Test.*), après vérification.
- 263 (l. 2464–2465) : première rédaction du paragraphe sur Brunck et la scholie.
- 273 (l. 2556, 2560) : ancienne note 2, sur la scholie des *Nuées* 1001 (τοῖς Ἱπποκράτους
  υἱέσιν εἴξεις, « Tous les spectateurs comprenant ὑσίν »).
- 289 (l. 2621, 2624–2625, 2631) : « Il en va de son fils (πρὸς θάληκον (??)) » ; deux
  rédactions antérieures ; dans la note 1, « Édition malheureusement désormais introuvable… ».
- 291 (l. 2640, 2653–2654, 2656, 2677–2684) : premières rédactions, et une ancienne conclusion
  qui proposait de lire καὶ πρὸς θάλικα νοῦν ἔχειν μοι καὶ φρένας. Parmi les anciennes notes
  (l. 2687–2705) :
  - n. 1 : la scholie de R porte πεδαρίσκον ;
  - n. 5 : Willems, Hésychius, la *Souda* et πόσθων (*Paix* 1300) ;
  - n. 7 : argument paléographique en faveur de θάλικα (λλ/λ, ι/η, α/ον ; cf. v. 285, τὸ πόπανον
    / τὰ πόπαν᾽) ;
  - n. 8 : ὁ θύλακος, « sac à provisions » ;
  - n. 9–12 : les vv. 74 et 210, la *Souda* s.v. Εὐριπίδης, Χοιρίνη / Χοιρίλη (voir plus haut).

## Vérifications

- Contrôle par script : `commentaire.tex` + `critique.tex` redonnent exactement l'original
  (`.travail/f165v/commentaire.orig.tex`, identique à la version git `HEAD`), aux corrections
  déclarées et aux renvois près. Deux scripts le confirment : `.travail/f165v/verifier.py` et le
  contrôle mot à mot `.travail/f165v/repartition/controle.py`. En dehors des articles, il ne
  reste que les lignes d'en-tête (`%`).
- `python3 outils/controle/repartition_commentaire.py f165v` signale « À VOIR ». C'est attendu :
  les 7 mots « perdus » sont les 7 formes corrigées (Ἀριστφάνης, nôtre, cédé, nombre, Verhnes,
  τό, sodomotiques). Les mots « ajoutés » sont les lemmes répétés des quatre articles scindés,
  les renvois et les formes corrigées.
- PDF : les 9 notes de `\cc{289}` et `\cc{291}` sont composées sous leurs articles (registre du
  commentaire critique, page diplomatique). La note de `\comm{273}` manque, pour la raison
  indiquée plus haut.
- `./edition/compiler_folio.sh f165v` : OK, 7 pages. Il reste deux *Overfull* (3,97 pt et
  0,73 pt) dans `critique.tex`, l. 50 (`\cc{291}`). Ils viennent de la traduction de Pollux,
  en `\citComm` imbriqué, dans la colonne étroite du commentaire critique. C'est cosmétique.
  Le troisième (0,86 pt, dans la note de l'art. 275–6 de `commentaire.tex`) existait avant
  l'intervention.
