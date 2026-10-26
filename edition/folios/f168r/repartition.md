# f168r (vv. 466–508) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f168r/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 3611–3777 ; articles C0137–C0149 de
`edition/donnees/travaux_anterieurs/commentaires.tsv`). Copie de la conversion d'origine :
`.travail/f168r/commentaire.orig.tex`. Règles : `edition/CONVENTIONS.md` § 3 et § 7.
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**État** : terminé. 13 articles : 2 CRITIQUE (477, 493), 1 MIXTE (500, scindé), 10 PIÈCE.
`critique.tex` compte 3 articles `\cc` (477, 493, 500) et `commentaire.tex` 11 articles `\comm`,
dont le reste de la scission de 500. Le folio compile (`./edition/compiler_folio.sh f168r` :
7 pages, aucun débordement signalé). `.travail/f168r/controle.py` vérifie que `commentaire.tex`
et `critique.tex` redonnent exactement l'original, aux corrections, « nous » → « je » et renvoi
déclarés ci-dessous près.

Reprise : une première exécution, interrompue, avait traité les articles 466 sqq. à 494
(déplacement de 477 et de 493, cinq coquilles corrigées, signalements). J'ai contrôlé ce travail
(script de contrôle, compilation) sans y rien changer. J'ai ensuite traité 495, 499 et 500
(scission par `.travail/f168r/scinder_500.py`, qui ne fait rien si `\cc{500}` existe déjà) et
achevé le présent compte rendu.

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0137 | 466 sqq. | (sans lemme) scholie ἐπίτηδες ὁ κηδεστὴς… | PIÈCE (caractère et jeu de Mnésiloque, d'après la scholie) | reste dans `commentaire.tex` ; 3 coquilles corrigées dans la scholie |
| 2 | C0138 | 473 | τί ταῦτ᾽ ἔχουσαι κεῖνον… | PIÈCE (parodie : *Ach.* 514, *Télèphe* d'Euripide) | reste dans `commentaire.tex`, inchangé |
| 3 | C0139 | 477 | ξύνοιδ᾽ ἐμαυτῇ πολλ᾽… | CRITIQUE (lacune d'un pied dans R ; suppléments de Bentley et de Dawes ; conjecture de Bibi πολλά γ᾽· ἀλλ᾽, expliquée par un saut du même au même) | déplacé en entier dans `critique.tex` (`\cc{477}`), inchangé |
| 4 | C0140 | 480 | με διεκόρευσεν ἑπτέτιν οὖσαν | PIÈCE (le récit de Mnésiloque ; Quartilla de Pétrone, marquise de Brinvilliers, d'après Willems) | reste dans `commentaire.tex`, inchangé |
| 5 | C0141 | 484 | στρόφος μ᾽ ἔχει τὴν γαστέρ᾽… | PIÈCE (langue : στρόφος, terme médical de la colique ; Hippocrate) | reste dans `commentaire.tex`, inchangé |
| 6 | C0142 | 486 | κᾆθ᾽ ὁ μὲν ἔτριβεν κεδρίδας… | PIÈCE (realia : genévrier, aneth, sauge, remèdes des coliques ; Pline) | reste dans `commentaire.tex` ; 1 coquille corrigée |
| 7 | C0143 | 487 | ἐγὼ δὲ καταχέασα τοῦ στροφέως… | PIÈCE (realia et mise en scène : l'eau sur les gonds ; scholie ; Plaute, *Curculio* ; jeux de mots καταχέω / καταχέζω, στροφεύς / στρόφος) | reste dans `commentaire.tex`, inchangé |
| 8 | C0144 | 489 | παρὰ τὸν Ἀγυιᾶ κύβδ᾽… | PIÈCE (realia : l'Agyieus, autel-pilier ceint de laurier ; Daremberg–Saglio, Hésychius ; posture ; laurier apotropaïque : Ἐφέσια γράμματα, Diogénien ; la remarque « [lire : ταὐτότητι ?] » porte sur le texte de Diogénien, non sur celui d'Aristophane) | reste dans `commentaire.tex` ; 2 coquilles corrigées |
| 9 | C0145 | 493 | μάλισθ᾽ ὑπό του ληκώμεθα | CRITIQUE (leçon de R avant et après correction : ληκώμεθα gratté, κινώμεθα récrit ; κινώμεθα glose substituée à la *lectio difficilior* ; témoignage de la Souda, λ 434) | déplacé en entier dans `critique.tex` (`\cc{493}`), inchangé |
| 10 | C0146 | 494 | ἕωθεν σκόροδα διαμασώμεθα | PIÈCE (mœurs : l'ail contre les soupçons du mari ; Athénée XIII 572c, Xénophon, *Banquet* IV 8) | reste dans `commentaire.tex` ; 1 coquille corrigée |
| 11 | C0147 | 495 | ἀπὸ τοῦ τείχους εἰσιὼν | PIÈCE (realia, contexte historique : la garde des remparts pendant l'occupation de Décélie ; Thucydide VIII 69) | reste dans `commentaire.tex`, inchangé |
| 12 | C0148 | 499 | τοὔγκυκλον | PIÈCE (realia : l'encycle, jupe courte ; renvoi à la note du v. 643) | reste dans `commentaire.tex`, inchangé |
| 13 | C0149 | 500 | ὑπ᾽ αὐγὰς οἷόν ἐστιν ἐγκεκαλυμμένον | MIXTE : texte (leçon de R ; suppression du v. 500 par Willems et van Herwerden ; scholie sur l'abrègement de ὑπ᾽ αὐγὰς ; conjecture de Bibi ᾦον ἐστιν pour οἷόν ἐστιν ; le v. 500, glose du v. 501 ; texte lu sans le v. 500) / pièce (histoire allusive, conte populaire d'après Coulon ; l'encycle, jupe courte, contre les interprétations « loufoques ») | scindé : du début à « Lisons donc avec Willems : » et à la citation des vv. 499 + 501 avec sa traduction (notes 1–3) → `critique.tex` (`\cc{500}`) ; de « Le passage, ici comme ailleurs » à la fin (note 4) reste dans `commentaire.tex`, précédé de « Pour le texte, voir le commentaire critique. » ; 3 « nous » → « je », 3 coquilles corrigées |

Scission (500) : la plage et le lemme sont repris tels quels dans les deux parties ; le renvoi
est en tête de la partie restée au commentaire. La partie critique, qui ouvre l'article, se lit
d'un seul tenant : aucun renvoi n'y a été ajouté. Les notes se répartissent sans reste (1–3 avec
la partie critique, 4 avec la partie restée au commentaire).

## « nous » d'auteur changés en « je »

- 500 (critique) : « Si effectivement interpolation il y a -- ce que **nous allons** essayer de
  démontrer -- » → « ce que **je vais** essayer de démontrer » (même choix en f175r, 1073–5).
- 500 (critique), note 1 : « Le premier à **notre** connaissance à avoir proposé la suppression du
  vers 500 » → « à **ma** connaissance » (l'auteur écrit ailleurs « à ma connaissance » : f169v,
  f171r).
- 500 (pièce) : « Ainsi, il **nous** apparaît plus que plausible qu'Aristophane rapporte ici… » →
  « il **m'**apparaît » (même choix en f163v : « il nous semble » → « il me semble »).

« nous » conservés, parce qu'ils associent le lecteur ou ont une valeur générale :
« Gardons-nous, dans un premier temps, de biffer », « Intéressons-nous y donc ! », « Rappelons
que » (note 2) et « Lisons donc avec Willems » (exhortatifs, comme « Lisons donc » conservé en
f163v) ; « Athénée (II, 57e) nous précise » (générique, comme « Hésychius nous explique » en
f167v) ; « notre scholie devenue le vers 500 » et « notre comédie » (note 3) : la scholie et la
pièce que l'auteur et le lecteur ont sous les yeux ; 489 : « l'attitude de notre libidineuse »
(le personnage en question). Aucun autre « nous » d'auteur dans les articles 466 sqq. à 499 :
l'auteur y dit déjà « je » (477 : « J'en propose une autre » ; 487 : « J'attire l'attention du
lecteur » ; 489 : « je me suis dispensé »).

## Coquilles corrigées

- 466 sqq. (scholie) : « ἐπιτηέδες ὀ κηδεστὴς … ἵνα διὰ τούτου λαθῃ » → « ἐπίτηδες ὁ κηδεστὴς
  … λάθῃ » (lettre en trop, esprit doux sur l'article, accent omis) ; texte contrôlé sur les
  scholies de Dübner, p. 267 (OCR du corpus local : « ἐπίτηδες ὁ κηδεστὴς ὑπὲρ τὰς ἄλλας
  γυναῖκας γυναικίζεται, ἵνα διὰ τούτου λάθη »). Mêmes fautes dans toutes les versions de `latex/`.
- 486 : « pour l'aneth (τό ἄννηθον) » → « (τὸ ἄννηθον) » (aigu pour grave devant un mot).
- 489, note 1 : « l'on peut y voir des représentations d'Agyeus » → « d'Agyieus » (graphie de
  la même phrase : « l'article *Agyieus* »).
- 489 : « pour conjurer le mauvais sort³. : » → « sort³ : » (point parasite devant les
  deux-points ; l'appel de note est conservé).
- 494 (citation d'Athénée XIII 572c) : « μεθ' ῆμῶν » → « μεθ' ἡμῶν » (esprit et accent ;
  texte contrôlé sur le corpus local).
- 500 (critique), note 1 : « Le lecteur pourra utilement se reporter à \nieme{13} note ainsi que
  son introduction » → « se reporter à **sa** \nieme{13} note » (mot omis ; la version antérieure
  de l'article, laissée en commentaire par l'auteur, porte « Willems, dans sa \nieme{13} note
  reproduite en annexe », l. 3766). Faute présente dans toutes les versions de `latex/`.
- 500 (critique) : « l'abrègement violent (συστολή βίαιος) » → « (συστολὴ βίαιος) » (aigu pour
  grave devant un mot, comme en 486).
- 500 (pièce), note 4 (Coulon) : « tome II(1934) » → « tome II (1934) » (espace omise).

## Passages signalés

### Passage marqué `\eff` (orange) dans la source

Un seul, dans une ligne que l'auteur a mise en commentaire (`%`, l. 3736) : la conversion ne l'a
pas repris, et je ne l'ai pas réintroduit.

- `\commentaire{496}{ὁρᾷς}{\eff{Pourquoi Mnésiloque passe-t-il du vouvoiement au tutoiement ?}}`.
  Question restée sans réponse : au v. 490, Mnésiloque dit ὁρᾶτ᾽ (pluriel), au v. 496 ὁρᾷς
  (singulier) ; la traduction de l'auteur rend les deux par « voyez-vous ». Le répertoire
  critique (Enger 1844, Velsen 1883) ne signale aucune conjecture sur ὁρᾷς : la question relève
  du commentaire de la pièce, non du texte. À l'auteur d'y répondre ou de l'abandonner.

### Autres passages mis en commentaire (`%`) par l'auteur, non repris (pour mémoire)

- 471 (l. 3620) : article entier, `\commentaire{471}{ἐν ἀλλήλοισι χρὴ δοῦναι λόγον.}{Même
  expression dans Hérodote (I, 97) : « καὶ ἐδίδοσαν σφίσι λόγον ».}` (PIÈCE ; référence exacte :
  Hdt. I 97, 2, contrôlé sur le corpus local ; le lemme suit R, ἀλλήλοισι, le texte établi porte
  ἀλλήλαισι, de Brunck selon l'apparat de l'auteur).
- 486 (l. 3659–3674) : « À toutes fins utiles pour le lecteur […], nous reproduisons ce que Pline
  l'Ancien nous apprend des vertus de ces plantes », suivi des trois extraits de Pline (latin et
  traduction de Littré), avec la scholie de R σφάκον· ἐλελίσφακον. ὡς ἐπιτήδεια παῦσαι στρόφον,
  et trois notes ; l'article actif n'en garde que les références.
- 489 : « Quoique porté aux *Realia* [par ma formation à l'école de Willems], je me suis
  dispensé… » (l. 3688) ; « …échapper au mauvais œil [d'un flagrant délit d'adultère]. »
  (l. 3696) ; fin de la note 3 (l. 3701), à l'état d'ébauche : « Noter que ce fameux bâton de
  laurier que pouvaient prendre les convives lors de symposies avant d'entonner le chant était
  appelé αἴσακος, qui est aussi le nom d'un centaure..... Nonnios : postérieur ? ».
- 494 (l. 3725–3727) : les deux notes de références (Athénée, XIII, 572c ; Xénophon,
  *Symposium*, IV, 8), passées entre parenthèses dans le texte de l'article ; l'appel
  `\marqueur{2}` resté après la citation de Xénophon n'a pas été repris par la conversion.
- 500 : « J'ai longtemps voulu conserver ὑπ᾽ αὐγὰς *contra metrum* (quitte à le remplacer par des
  formes proches comme ὑπαυγάσ᾽ ou ὑπαυγάσας) car il me semblait donner des indications sur le
  stratagème employé par la pécheresse. » (l. 3750) ; deux bribes après « Le cas me paraît plus
  compliqué. » (l. 3751) ; « …ne seraient pas si compromettantes [pour elles que ne l'étaient
  celles d'Euripide]. » (l. 3763) ; « les hypothèses loufoques [proposées par de savants
  universitaires] » (l. 3764) ; enfin l'ancienne version de l'article (l. 3766–3773) : le v. 500
  gardé avec la conjecture de Hermann ὑπαυγάσ(αι)᾽ οἷόν ἐστιν, ὑπαυγάζειν chez Aristote
  (« *Ars Rhetorica*, 3, 1378 ») et αὐγάζειν « voir » chez Sophocle (*Phil.* 217), ἐγκεκαλυμμένον
  expliqué par Hésychius (ε 186 : ἐγκαλύπτεσθαι· διατρέπεσθαι, αἰσχύνεσθαι ; l'amant sortirait
  « honteux… et nu comme un ver »), avec trois notes (Eur. *Héc.* 1154 d'après Coulon ;
  l'interprétation de l'encycle déployé pour cacher la fuite de l'amant ; Aristote). L'article
  actuel (suppression du v. 500) contredit cette version, qui n'a pas à être reprise ; Hésychius
  ε 186 et Eur. *Héc.* 1154 pourraient servir aux *loci paralleli*. Références de ces lignes non
  contrôlées.

### Par article

- 473 : lemme « κεῖνον » (leçon de R et de la Souda) alors que `texte.tex` porte ᾽κεῖνον
  (Meineke) ; lemme laissé tel quel. *Ach.* 514 (τί ταῦτα τοὺς Λάκωνας αἰτιώμεθα;) contrôlé sur
  le corpus local.
- 477 (critique) : lemme = leçon de R (πολλ᾽), alors que `texte.tex` porte la conjecture de
  l'auteur (πολλά γ᾽· ἀλλ᾽) ; normal pour un article critique, laissé tel quel. Attributions
  conformes au répertoire critique (Enger 1844 : « δεινὰ πόλλ᾽ Bentleius, rectius πολλὰ δεῖν᾽
  Dawesius p. 317 ») ; Enger signale aussi πολλὰ πόλλ᾽ de Bothe, que l'article ne mentionne pas.
- 480 : lemme « με διεκόρευσεν ἑπτέτιν οὖσαν » (leçon et ordre des mots de R) alors que
  `texte.tex` porte ὅσπερ με διεκόρησεν οὖσαν ἑπτέτιν (Pollux) ; l'article ne discute pas le
  texte ; lemme laissé tel quel. « (\italique{Satyrico}, XXV) » : sans doute *Satyricon*, mais
  la phrase est donnée comme de Willems (traduction de 1919, non disponible ici) : non modifié
  [à vérifier] ; la référence elle-même n'a pas pu être contrôlée ici (pas de texte latin dans
  le corpus local).
- 487 : scholie ἵνα ὀλισθηρὸς γενόμενος μὴ ψοφῇ contrôlée (Dübner, p. 267). Citation de Plaute
  (*Curculio*, I, 3, 1 : v. 158 sqq. en numérotation continue [à vérifier]) non contrôlée ici
  (pas de texte latin dans le corpus local) ; « subfundam » pour *suffundam* est peut-être la
  graphie de l'édition suivie par l'auteur [à vérifier] ; non modifié.
- 489, citation de Diogénien (IV 78, CPG I, p. 244 ; texte de l'auteur conforme au corpus
  local) : « ταὐτὸ τῇ [lire : ταὐτότητι ?] ». La correction proposée paraît inutile : ταὐτὸ τῇ
  (s.-ent. παροιμίᾳ) est la formule des parémiographes pour renvoyer à un proverbe de même sens
  (cf. Diogenian. IV 41 : « ταὐτὸ δέ ἐστι τῷ, Ἐπὶ ξυροῦ βαίνειν »). La traduction « En
  répétant : « Je porte la branche de laurier » » serait alors à revoir (« Même sens que : « Je
  porte un bâton de laurier » »). Le proverbe a sa propre entrée, qui confirme l'interprétation
  de l'auteur (le laurier protège) : Diogenian. IV 14 (CPG I, p. 234) Δαφνίνην φορῶ βακτηρίαν·
  ἐπὶ τῶν ὑπό τινων ἐπιβουλευομένων. παρόσον ἀλεξιφάρμακον ἡ δάφνη ; de même Zen. III 12 et
  Suid. δ 100 (contrôlés sur le corpus local). À décider par l'auteur ; rien n'a été modifié.
  Dans la même citation, « …ταὐτότητι ?]·\ » suivi d'un saut de ligne donne une simple espace
  (`\` + fin de ligne) : `\\` (retour à la ligne avant le proverbe) était sans doute voulu ;
  laissé tel quel.
- 489, note 3 : « *Corpus paroemiographorum graecorum*, I, ed. E. L. a Leutsch » — le t. I
  (1839) est de Leutsch et Schneidewin [à vérifier] ; non modifié. *Plut.* 213 et Suid. α 1139
  (Ἀλεξιφάρμακα : Ménandre, Ἐφέσια τοῖς γαμοῦσιν…) contrôlés sur le corpus local.
- 489 : Hésychius α 856 (ἀγυιεύς· ὁ πρὸ τῶν θυρῶν ἑστὼς βωμὸς ἐν σχήματι κίονος) : texte
  contrôlé (éd. Schmidt, col. 26 ; numéro de Latte non contrôlé) ; Théocrite V 116–117 (τᾶς
  δρυὸς εἴχεο) contrôlé.
- 493 (critique) : l'article attribue la correction au copiste lui-même (« Le scribe […] avant
  de gratter les trois premières lettres et de réécrire par dessus κινώμεθα ») ; Enger 1844 la
  donne à un correcteur (« κινώμεθα […] a correctore R. qui pr. m. ληκώμεθα ») et Velsen 1883 à
  R² (« in ras. est κιν ab R² ») ; l'apparat antérieur de l'auteur reste neutre (« ληκώμεθα
  R^ac (?), Suid. : κινώ- R^pc »). Main à vérifier sur l'image. Suid. λ 434 contrôlé (Ληκώμεθα·
  κινώμεθα. Ἀριστοφάνης· μάλισθ᾽ ὅταν ὑπό του ληκώμεθα τὴν νύχθ᾽ ὅλην). Le commentaire de la
  pièce ne dit plus rien du sens de ληκᾶν (la traduction « paillardé » le rend) ; aucun renvoi
  ajouté.
- 494 : citations d'Athénée (XIII 572c ; vers d'Alexis ou d'Antiphane, *Hypnos*) et de
  Xénophon (*Banquet* IV 8) contrôlées sur le corpus local ; Fritzsche (1838, p. 179) les
  rapprochait déjà du passage.
- 495 : lemme « ἀπὸ τοῦ τείχους » = leçon de R (apparat de l'auteur : « ἀπὸ τοῦ R : ἀπὸ Biset »),
  alors que `texte.tex` porte ἀπὸ τείχους ; l'article ne discute pas le texte ; lemme laissé tel
  quel. Pour l'apparat : Enger (1844 : « Bentleius et Reiskius »), Velsen (1883) et Coulon (1928)
  donnent ἀπὸ τείχους à Bentley (Coulon : « 494 et 495 σκόροδα διαμασώμεθα et ὀσφρόμενος et
  τείχους Bentley : … τοῦ τείχους R »), l'apparat de l'auteur à Biset [à vérifier]. Citation de
  Thucydide (VIII 69, 1) conforme au texte de Perseus (Jones–Powell), crochets compris (« ἦσαν
  [δ᾽] Ἀθηναῖοι ») ; le rapprochement remonte à Voss (Enger 1844 : « Apte citat Vossius
  Thucydidem VIII. 69 »). La traduction française n'est pas attribuée (ce n'est pas celle de
  Bétant).
- 499 et 500 (pièce) : doublon de renvoi au v. 643 (499 : « Cf. la note au vers 643 » ; reste
  de 500 : « Voir le commentaire au vers 643 : l'encycle (ἔγκυκλον) est une courte jupe »).
  Laissé tel quel.
- 500, lemme et plage : `texte.tex` omet le v. 500, conformément à l'article critique. Le reste
  laissé au commentaire garde le lemme et la plage du v. 500 (règle des scissions), alors qu'il
  porte sur l'histoire des vv. 499–501 : à l'auteur de dire s'il le rattache aux vv. 499–501 ou
  le fond avec l'article 499.
- 500 (pièce), interprétation : la fin de l'article récuse les hypothèses « où la femme cacherait
  l'amant aux yeux du mari en tendant l'encycle devant l'amant ». Or c'est à peu près la lecture
  de Willems, que la partie critique suit pour le texte (note 13, `latex/Aristophane-Thesmo
  Annexes.tex` : la femme « atteindra plus sûrement son but en ouvrant le manteau devant les
  yeux de son mari qu'en le déployant à la lumière »). À l'auteur de voir s'il veut le préciser ;
  rien n'a été modifié.
- 500 (critique), références contrôlées :
  - scholie de R au v. 500 (Dübner) : « ὅτι καὶ συστολαῖς βιαίοις χρῶνται καὶ ἐκτάσεσι », avec
    en exemple le v. 176. La scholie parle en général des abrègements et allongements forcés ;
    « συστολὴ βίαιος » est une paraphrase de l'auteur, non une citation (Dübner, dans ses notes :
    « de βιαίῳ συστολῇ ») ;
  - Athénée II 57e (Perseus, éd. Kaibel) : « ἐκάλουν δὲ καὶ τὰ νῦν τῶν οἰκιῶν παρ᾽ ἡμῖν
    καλούμενα ὑπερῷα ᾠά, φησὶ Κλέαρχος ἐν Ἐρωτικοῖς » : conforme (Athénée cite Cléarque) ;
  - Σ T *Il.* XVI 184 (Dindorf–Maass, *Scholia graeca in Homeri Iliadem*, scholies du
    Townleianus éditées par Maass ; corpus First1KGreek) : « τὰ μετέωρα δὲ τῶν οἰκημάτων ᾦα
    Λακεδα〈ι〉μόνιοι καλοῦσιν, ἃ νῦν ὑπερῷά φαμεν » (le fichier numérisé porte Λακεδαμόνιοι) :
    conforme. La scholie accentue ᾦα, Athénée et
    LSJ ᾠά, ᾠόν ; l'auteur suit la scholie (ᾦον). Devant l'enclitique, il faudrait strictement
    « ᾦόν ἐστιν » (cf. οἷόν ἐστιν de R) : non modifié (trois occurrences) ;
  - note 3 : la scholie bT à *Il.* I 135 et 137 cite bien les vv. 536–537 (« καὶ ἐν
    Θεσμοφοριαζούσαις (536)· “εἰ μὲν οὖν τις ἔστιν· εἰ δὲ μή, ἡμεῖς τε καὶ τὰ δουλάρια τέφραν
    ποθὲν λαβοῦσαι.” »), conformément aux *testimonia* de l'auteur ;
  - note 1 : la 13e note de Willems (vv. 499–501 : « Il faut supprimer le v. 500, qui tire son
    origine d'une note marginale… » ; « οἷόν ἐστ' est une pure cheville ») et son introduction
    aux *Notes sur la* Paix (« Tels sont aussi le vers 500 des *Thesmophories* sur l'anecdote du
    manteau ») sont bien reproduites dans `latex/Aristophane-Thesmo Annexes.tex` ; pages « t. II,
    pp. 93-99 » non contrôlées.
- 500, non contrôlés [à vérifier] : van Herwerden, *Mnemosyne* N. S. 24 (1896), p. 293, premier
  à supprimer le v. 500 : absent des sources locales ; Coulon (1928) ne le cite pas dans son
  apparat, où il imprime « <ἰδεῖν> ὑπ᾽ αὐγὰς οἷον » (Hermann et Coulon) et renvoie à son article
  de la *REG* 38 (1925), p. 90–94, que l'article ne mentionne pas. Coulon, « Interprétation d'un
  passage d'Aristophane imité par les conteurs du Moyen-Âge », *Mélanges Bidez* (1934),
  p. 121–134 : absent des sources locales.
- 500, note 2 : R daté « IXe ou Xe siècle » ; `edition/CONVENTIONS.md` (§ 2.3) dit « milieu du
  Xe s. » (même remarque en f166r) : à harmoniser. Que R note l'iota adscrit s'accorde avec les
  relevés graphologiques (f167v : τέχνηι, τραγωιδίαις, δρᾶι dans la ligne).
- Apparat de la source (hors commentaire, pour mémoire) : « μυχὸν R : \lecon{μοιχὸν} Gryaneus »
  (l. 3744) : lire Grynaeus.

### Graphies à revoir (non corrigées : usage, style ou habitude de l'auteur)

- 500 : « Intéressons-nous y » (→ Intéressons-nous-y ; même graphie « Attelons-nous y » en
  f169r, laissée telle quelle) ; « tout-à-fait » ; « Moyen-Âge » ; « fait-divers » ; « p.293 »
  (l'auteur écrit d'ordinaire « p.292 », « p.463 »… sans espace) ; « (voir les *testimonia ad
  locum*.). » (point final dans la parenthèse, comme « (Athénée, XIII, 572c.) » en 494) ;
  « qu'elle fît peu ou prou un trimètre iambique et soit alors très tôt intégrée » (concordance
  des temps) ; traduction « Comment la femme qui exhibant l'encycle à son mari / fit échapper son
  amant » (virgules attendues autour de « exhibant l'encycle à son mari »).

### Compilation

- `./edition/compiler_folio.sh f168r` : OK, 7 pages (comme avant la scission), aucun « Overfull ».
  Les notes 1–3 du `\cc{500}` sortent à la fin de l'article critique, la note 4 (Coulon) à la fin
  du reste de 500 dans le commentaire. Aucune `\nc` à l'intérieur d'un `\citComm` dans ce folio :
  le défaut du moteur décrit en f165r et f166r ne joue pas ici.
