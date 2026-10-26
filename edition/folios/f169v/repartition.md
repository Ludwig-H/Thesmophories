# f169v (vv. 593–635) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f169v/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 4320–4588 ; articles
C0173–C0180 de `edition/donnees/travaux_anterieurs/commentaires.tsv`). Version d'origine de la
conversion : commit 478170c (inchangée à `HEAD`), copiée dans `.travail/f169v/commentaire.orig.tex`.
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**Bilan.** 8 articles : 1 CRITIQUE (déplacé en entier), 7 PIÈCE (restés), aucun MIXTE.
`critique.tex` compte 1 article (`\cc{593}`) ; `commentaire.tex` en garde 7.
Compilation (`./edition/compiler_folio.sh f169v`) : OK, 7 pages. Les trois « Overfull \hbox »
(2,7 à 6,8 pt) des colonnes du commentaire existaient déjà avec la version d'origine (compilation
séparée de la version `HEAD`, dans `.travail/f169v/build_orig/`). Contrôle automatique
(`python3 outils/controle/repartition_commentaire.py HEAD f169v`) : 1973 mots avant et après ; les
4 mots « perdus » et les 4 « ajoutés » sont exactement les coquilles corrigées (dresse, publique,
dernière, menacait). Comparaison mot à mot avec la conversion d'origine : rien d'autre n'a changé
que les 8 corrections listées ci-dessous.

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0173 | 593 | ἠλίθιος ὅστις τιλλόμενος ἠνείχετο; | CRITIQUE (leçon de R défendue, d'après la note 18 de Willems : ἠνείχετο contre ἠνείχετ᾽ ἄν de Brunck et de van Leeuwen) | déplacé en entier dans `critique.tex` (`\cc{593}`), inchangé |
| 2 | C0174 | 602 | ὦ πρόξενε. | PIÈCE (realia : les proxènes ; note de Willems) | reste dans `commentaire.tex`, inchangé |
| 3 | C0175 | 605 | Κλεωνύμου γυνή. | PIÈCE (prosopographie et satire : les railleries contre Cléonyme, décrets, ῥίψασπις ; polémique contre Storey ; le rejet du v. 1166 des *Acharniens* par certains critiques, évoqué comme argument, porte sur une autre pièce) | reste dans `commentaire.tex` ; 4 coquilles corrigées |
| 4 | C0176 | 609 | τίτθη. | PIÈCE (realia : condition des nourrices ; note de Willems) | reste dans `commentaire.tex`, inchangé |
| 5 | C0177 | 616 | κάρδαμον | PIÈCE (realia, botanique : identification du κάρδαμον ; note de Willems et complément de l'auteur sur les dictionnaires) | reste dans `commentaire.tex` ; 2 coquilles corrigées |
| 6 | C0178 | 619 | τὸν ἐκ Κοθωκιδῶν; | PIÈCE (realia : le dème des Kothokides, tribu Oinéis) | reste dans `commentaire.tex`, inchangé |
| 7 | C0179 | 624 | συσκηνήτρια. | PIÈCE (realia : les tentes des Thesmophories, cf. v. 658) | reste dans `commentaire.tex`, inchangé |
| 8 | C0180 | 633 | σκάφιον Ξένυλλ᾽ ᾔτησεν… | PIÈCE (interprétation de la réplique : σκάφιον « coupe » / « urinoir », ἀμίς ; proverbe ἄμας ἀπῄτουν, οἱ δ᾽ ἀπηρνοῦντο σκάφας et parémiographes) | reste dans `commentaire.tex` ; 2 coquilles corrigées |

## « nous » d'auteur changés en « je »

Aucun : l'auteur dit déjà « je » dans ce folio (605, note 9 : « je tiens pour nulle… », « je lui
saurais gré » ; « M. Storey ne me fera pas accroire » ; 633 : « je dirais même plus », note 1 :
« je renvoie », note 3 : « à ma connaissance »).

Gardés, parce qu'ils associent le lecteur ou sont collectifs : 605 « Cet Athénien nous est autrement
connu », « Aristophane nous présente », « nos éminents professeurs », « chez nous », « celle de nos
passages », « nos modernes brigands », « Revenons », « Citons » ; 616 « ajoutons » ; 619 « cette
raison nous reste obscure » ; 633 « notre pauvre Mnésiloque », « Apprécions ». Non touchés : ceux
de Willems dans ses notes citées (609 « Remarquons » ; 616 « je crois », « Mettez cela d'accord »).

## Coquilles corrigées

- 605 : « est l'occasion de dresse un bref résumé » → « de dresser ».
- 605 : « bien avant les dernière traces archéologiques » → « les dernières traces ».
- 605 : « dont la panse menacait de crever » → « menaçait ».
- 605 : « exposé à l'opprobre publique le couard » → « l'opprobre public » (*opprobre* est masculin ;
  faute d'accord isolée, la même dans toutes les versions des fichiers de l'auteur).
- 616 : « \latin{Lepidium sativum} »,\italique{cresson alénois} » → « », \italique{cresson alénois} »
  (espace manquante après la virgule).
- 616 : « …mit bitterem Kraut} ».Pour aller dans le sens de Willems » → « ». Pour aller » (espace
  manquante : dans la source, la ligne se termine par `%` juste après « ». »).
- 633, note 3 : « Les latins et leur solide bon sens » → « Les Latins » (nom de peuple ; l'auteur
  écrit « les Latins » dans `vv 642-fin-bis`).
- 633, note 3 : parenthèse fermante orpheline en fin de note (« …in penuria constitit}.) ») supprimée :
  la parenthèse ouvrante « %(contrairement à un lieu commun par trop répandu dont » a été mise en
  commentaire par l'auteur dans la source (l. 4586).

## Passages signalés

### Affirmation sur R (article critique)

- 593 : la leçon que défend Willems, ἠνείχετο sans ἄν, est bien celle de R : vérifiée sur l'image
  (f169v, l. 1 : ἠλίθιος· ὅστις τιλλόμενος ἠνείχετο ; découpe dans `.travail/f169v/ligne01.png`).

### Par article

- 593 : « à retrouver à la fin » renvoie aux annexes de l'édition antérieure
  (`latex/Aristophane-Thesmo Annexes.tex`, « Note 18 aux *Thesmophories* : vers 592-593 »,
  l. 957–970 : Brunck lit ἠνείχετ᾽ ἄν, van Leeuwen rétablit ἄν, G. Hermann et Sobolewski défendent
  la vulgate). Renvoi à ajuster selon que la nouvelle édition garde ou non ces annexes ; gardé tel
  quel. L'article ne nomme pas la leçon en cause (ἄν de Brunck) : à compléter par l'auteur s'il le
  juge utile.
- 605 : « une laideur repoussante (v. 822 des *Guêpes*, ) » : virgule suivie d'un blanc, une seconde
  référence semble manquer ; laissé tel quel.
- 605 : « le crime était théoriquement puni de mort » (note 3 : Andocide, I, 74) : le passage cité
  range ceux qui ont jeté leur bouclier (ἢ τὴν ἀσπίδα ἀποβάλοιεν) parmi les ἄτιμοι τὰ σώματα
  (atimie, perte des droits civiques), non parmi les condamnés à mort (vérifié sur le corpus local,
  Perseus, Andoc. 1, 74) ; la même prémisse revient dans le résumé de l'argument de Storey
  (« Cléonyme serait mort – condamné à mort – »). Non modifié ; à revoir par l'auteur [à vérifier
  sur l'article de Storey]. La note 2 (Andoc. 1, 27 : décret de Cléonyme, 1000 drachmes ; Pisandre,
  10000) est conforme au texte (même contrôle).
- 605, note 5 : Storey, *RhM* 132 (1989), p. 247-261 : volume, année et pages confirmés par une
  bibliographie en ligne (*Fragmenta Comica*, digi.hadw-bw.de), qui écrit le nom « Cleonymos » dans
  le titre ; graphie du titre (« Kleonymus ») [à vérifier] ; non modifiée.
- 605, notes 6 et 10 : piques politiques datées, étrangères au texte (Élysée, Matignon, palais Bourbon
  et du Luxembourg pris pour des prisons ; « M. Ciotti-le-bien-nommé », avec une allégation nominative
  sur son service militaire, et le calembour « Chiotti ») : conservées telles quelles ; à reconsidérer
  par l'auteur avant publication.
- 616 : la parenthèse « (Note de Willems. Les dictionnaires… donner du courage.) » mêle la fin de la
  note de Willems et le complément de l'auteur ; dans la source, ce complément formait une note à part
  (`\note{1}`, désormais en commentaire `%`, avec « (\italique{cresson alénois}) » entre parenthèses),
  et la rédaction active l'a fait entrer dans la parenthèse. Gardé tel quel.
- 619 : le lemme τὸν ἐκ Κοθωκιδῶν appartient au v. 620 (plage « 619 » de la source, gardée) ; il finit
  par un point d'interrogation, alors que `texte.tex` ponctue d'un point (la source porte, en
  commentaire, un apparat « add. signum interrogationis Canini ») ; lemme laissé tel quel.
- 624 : « à proximité du Pnyx » : l'auteur écrit ailleurs « la colline de la Pnyx » (vv. 1-641, l. 3892
  et 4289 ; vv. 642-fin-bis, l. 5316), Willems « le Pnyx » (notes reproduites dans les annexes) ; la
  phrase suit peut-être Willems. Non corrigé (« de la Pnyx » ?).
- 633, note 2 : « le scholiaste de Théocrite (*Idylles*, IV, 10) cite aussi de ce proverbe » : « de » de
  trop, ou reste d'une autre tournure (« se souvient aussi de ce proverbe ») ; non corrigé, la
  correction n'étant pas univoque. (Scholie de Théocrite non vérifiable sur le corpus local.)
- 633, note 2 : « le scholiaste de la *Paix*… le cite encore à propos de la chanson de Datis le Lydien
  aux vers 289-291 » : d'après l'OCR de Dübner (*Scholia graeca in Aristophanem*, p. 179–180), le
  proverbe est cité dans la scholie au v. 299 (ὡς τάχιστ᾽ ἄμας λαβόντες…), à propos des ἄμαι ; la
  scholie au v. 289 (τὸ Δάτιδος μέλος, barbarisme χαίρομαι) ne le cite pas [à vérifier sur l'image ou
  sur Holwerda] ; non modifié. Les autres références de la note, contrôlées sur le corpus local, sont
  justes : Souda α 1504 et α 1574 ; Zénobius 1, 83 ; Plutarque, *De garrulitate* 512e (§ 20).
- 633 : « interprétée par Mica » : le personnage est « Mika » dans `texte.tex` (l'auteur emploie les
  deux graphies : 3 « Mica » et 28 « Mika » dans `vv 1-641`, 28 et 26 dans `vv 642-fin-bis`) ; à
  harmoniser globalement ; non corrigé.

### Passages `\eff` de la source (marqués en orange par l'auteur)

Deux dans les vv. 593–635, tous deux mis en commentaire (`%`) dans la source et donc absents de la
conversion ; non repris, à décider par l'auteur :

- 616 (l. 4464), avant le texte de l'article sur le κάρδαμον : « \eff{Érasme 754} » — piste vers un
  adage d'Érasme (n° 754) [à vérifier ; les *Adages* ne sont pas dans le corpus local].
- 605, note 6 (l. 4382), dans une phrase elle-même en commentaire (calembour sur « Matignon ») :
  « noter la eff{demander à Alexandre + exemples} » (marque sans barre oblique inverse).

### Autres passages mis en commentaire (`%`) par l'auteur dans la source (non convertis)

- 605 (l. 4372) : début d'une rédaction abandonnée de la note (« Cette note sur l'occasion de tordre le
  cou à l'une des traditions philologiques les plus tenaces… »), inachevé.
- 605, note 6 (l. 4382–4384) : développement polémique plus long sur l'Élysée, Matignon, le palais
  Bourbon et le Luxembourg (piques contre des personnes vivantes).
- 605, note 9 (l. 4388–4390) : « Les autres passages sont encore moins probants : *Paix* v. 1172-1187
  et *Guêpes* v. 1112-1121 » ; « comme il ne fait pas de doute et comme le scholiaste l'avait déjà
  remarqué » (à propos des vv. 827-829).
- 605, note 10 (l. 4391–4393) : variante de la première phrase ; « *Ubi quae fuerant vitia, mores
  sunt.* »
- 616 (l. 4457–4463) : rédaction antérieure de l'article, à la première personne : objection de Willems
  reprise ; hypothèse que le κάρδαμον serait une moutarde plutôt qu'un cresson, avec Hippocrate
  (*Vict.* II, 54 : κάρδαμον et νᾶπυ qualifiés de θερμόν), Athénée IX, 366d (vers de Nicandre
  Κάρδαμον, ἄρρινόν τε, μελάμφυλλόν τε σίνηπυ) et la glose d'Hésychius ἐρύσιμον· κάρδαμον ἄγριον —
  matière pour les *loci paralleli*, après vérification ; et (l. 4467–4469) l'ancienne note 1 sur les
  dictionnaires, reprise dans la parenthèse finale de l'article actif.
- 633 (l. 4573–4575) : la scholie au v. 633, citée et traduite (« Ce n'est d'ailleurs pas autrement que
  le comprenait le scholiaste : μὴ εὑρίσχων [*sic*] τί εἴπῃ ὁ κηδεστής… ἀμὶς δέ ἐστιν οὐροδόχον
  ἀγγεῖον ») : à reprendre éventuellement parmi les scholies ou les *loci paralleli*, après
  vérification sur R.
- 633, note 3 (l. 4586–4587) : « (contrairement à un lieu commun par trop répandu dont » et « (c'est-à-dire
  bourgeoise) ».

### Hors commentaire (pour le commentaire critique, l'apparat et le texte)

- Apparat en commentaire dans la source, à revoir pour l'apparat et le commentaire critique :
  604 (l. 4356) « ζητητέαι γάρ ἐστε R : ζητητέον τἄρ᾽ ἐστί Maas ‖ 604 ante 603 transp. Maas, post 607
  collocare malui » (transposition jadis proposée par l'auteur, puis abandonnée) ; 610 (l. 4426)
  « τί τὸ κακόν; continuat Clistheni R : Parenti tribuit (cum versu sequenti) R^pc » (sigle marginal
  de R à vérifier sur l'image ; cf. `ravennas/graphologie/folios/f169v.jsonl`, l. 18) ; 620
  (l. 4492) « add. signum interrogationis Canini ».
- 611 (l. 4438) : article en commentaire, « J'attribue à Clisthène la réplique (qui traitera encore
  Mnésiloque au vers 638 d'ἀναίσχυντός) » : position abandonnée, contraire à celle de l'article sur les
  vv. 637–40 (f170r), où l'auteur garde le v. 638 à Mnésiloque et blâme ceux qui donnent à Clisthène
  l'ἀναίσχυντός τις εἶ du v. 611.
- `texte.tex` : le v. 612 (σὺ δ᾽ οὖν ποίει τοῦτ᾽. ἀναμενῶ γὰρ ἐνθάδε.), trimètre entier de Clisthène,
  est codé `\vers[suite]` et composé comme la fin d'un v. 611 partagé (vérifié sur le PDF) ; il
  faudrait `\vers[n=612]`. Dans la source, c'est un vers à part (groupe « v. 611b-612 », avec en
  commentaire la trace d'une ancienne attribution d'ἀναίσχυντός τις εἶ à Clisthène). Non modifié
  (hors du champ de cette tâche).
- En-têtes de `commentaire.tex` et de `texte.tex` : « vv. 590–634 » (bornes d'avant la correction des
  limites de folios ; le folio porte les vv. 593–635) ; commentaires LaTeX sans effet, non modifiés.
