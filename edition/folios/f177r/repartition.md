# f177r (vv. 1211–1231) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f177r/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex`, l. 5416 ; article C0355 de
`edition/donnees/travaux_anterieurs/commentaires.tsv`). Copie de la conversion d'origine :
`.travail/f177r/commentaire.orig.tex`. Règles : `edition/CONVENTIONS.md` § 3 et § 7.
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**État** : terminé. La conversion ne donnait à ce folio qu'un article : 1 CRITIQUE (1216),
déplacé en entier dans `critique.tex` ; 0 PIÈCE, 0 MIXTE. `commentaire.tex` ne contient donc plus
aucun article (seulement des lignes de commentaire TeX qui expliquent ce vide). Le folio compile
(voir « Composition ») ; `.travail/f177r/controle.py` vérifie que `critique.tex` et
`commentaire.tex` redonnent exactement l'article d'origine (`\cc` lu comme `\comm`).
Un second article de l'auteur relève de ce folio (vv. 1229–31), mais la conversion l'a rangé en
f176r à cause d'une coquille de plage dans la source : voir « Article égaré ».

Reprise : aucune exécution antérieure pour ce folio (ni `critique.tex`, ni `repartition.md`, ni
`.travail/f177r/` au départ).

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0355 | 1216 | οἴμοι, τί δράσει; ποῖ τὸ γράδιο· | CRITIQUE (métrique : il manque un pied au vers ; le lemme cite la leçon de R, δράσει, γράδιο) | déplacé en entier dans `critique.tex` (`\cc{1216}`), inchangé |

## Article égaré (vv. 1229–31, actuellement en f176r)

- Dans la source (l. 5471, au v. 1229 οἴκαδ᾽ ἑκάστῃ. τὼ Θεσμοφόρω δ᾽), l'article C0356 porte la
  plage « 1129-31 » : coquille pour 1229–31, puisque son lemme cite les vv. 1229–1231 (τὼ
  Θεσμοφόρω δ᾽ / ἡμῖν ἀγαθὴν / τούτων χάριν ἀνταποδοίτην). Même plage dans
  `latex/Aristophane-Thesmo nov 2022.tex` (l. 8798). La conversion, qui range les articles d'après le premier vers de la plage,
  l'a placé dans `edition/folios/f176r/commentaire.tex` (`\comm{1129–31}{…}`), où l'agent
  chargé de f176r, au travail en même temps que moi, l'a inscrit comme article 8 « 1129–31
  (sic) », « à traiter ».
- Je n'ai pas modifié `f176r/commentaire.tex`, qu'un autre agent est en train de traiter (risque
  de conflit d'écriture), et je ne l'ai pas recopié ici (pas de doublon).
- Classement proposé : **PIÈCE** (la fin de la pièce : souhait de succès, la victoire au concours
  comique ; aucune discussion du texte).
- Action proposée à l'orchestrateur, une fois f176r terminé : déplacer l'article de
  `f176r/commentaire.tex` dans `f177r/commentaire.tex`, avec la plage corrigée `1229–31`, et
  retirer de ce dernier les trois lignes de commentaire TeX devenues inexactes. Coquilles évidentes
  à corriger à cette occasion (signalées, non corrigées) : « Artistophane » → « Aristophane » ;
  « conclue sa pièce » → « conclut sa pièce » ; « bien-sûr » → « bien sûr ». Pas de « nous »
  d'auteur.

## « nous » d'auteur changés en « je »

Aucun : l'article 1216 ne contient ni « nous » ni « je » (l'article égaré des vv. 1229–31 non plus).

## Coquilles corrigées

Aucune. Le lemme de 1216 (οἴμοι, τί δράσει; ποῖ τὸ γράδιο·) reproduit à dessein la leçon de R
(δράσει, γράδιο, point final) et non le texte établi (οἴμοι, τί δρᾶσι; ποῖ τὸ γρᾴδιο; — δρᾶσι
Blaydes, γρᾴδιο M, d'après l'apparat de la source, l. 5414) : ce n'est pas une coquille.

## Passages signalés (non modifiés)

- **1216, leçon de R contrôlée sur l'image**
  (`dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/30_f177r_classense179r_vv1211-1231_fin.jpg`,
  ligne 6 de `ravennas/segmentation/f177r.json`) : R écrit οἴ μοι· τί δράσει· ποῖ τὸ γραδιο·, puis
  ἀρταμουξία· sur une ligne à part, centrée. δράσει est confirmé (σ et ει en ligature) ; sur l'α de
  γραδιο, un trait horizontal accompagné d'un aigu, tracé semblable à celui de γραιδιο au v. 1211
  (ligne 1), alors qu'au v. 1213 (ligne 3) le circonflexe est ondulé. Le lemme γράδιο se défend ;
  je n'y touche pas.
- **1216, portée de la remarque « Il manque un pied à ce vers »** : elle vaut pour la colométrie de
  R et du texte établi (`texte.tex`), où οἴμοι est dans le vers et Ἀρταμουξία à part :
  οἴμοι, τί δρᾶσι; ποῖ τὸ γρᾴδιο; = – – ⏑ – | ⏑ – ⏑ – | ⏑ ⏓, dix syllabes, un trimètre auquel
  manque un iambe. Hall–Geldart (Oxford, 1907 ; texte Perseus du corpus local,
  `.sources/corpus/canonical-greekLit/data/tlg0019/tlg008/tlg0019.tlg008.perseus-grc2.xml`)
  disposent autrement : οἴμοι isolé hors du vers (ligne numérotée 1215a dans Perseus), puis
  τί δρᾶσι; ποῖ τὸ γρᾴδι᾽; Ἀρταμουξία (v. 1216), trimètre complet
  (⏑ – ⏑ – | ⏑ – ⏑ – | ⏑ – ⏑ ⏓) où rien ne manque. L'article, d'une ligne, ne discute pas cette
  disposition et ne propose aucun supplément ; le texte établi n'imprime ni signe de lacune ni
  supplément, et l'apparat de la source n'a, pour ce vers, que δρᾶσι Blaydes et γρᾴδιο M. Décision
  à prendre par l'auteur (lacune à marquer, ou colométrie de Hall–Geldart) ; à développer dans le
  commentaire critique.
- **Discussions voisines rangées ailleurs** : la conjecture de Bibi συμβήνη au v. 1215 (R :
  συβήνη, sans μ, contrôlé sur l'image, ligne 5) est discutée dans l'article « 1197-216 » (C0352), resté en f176v d'après son premier
  vers ; l'article « 1203-11 » (C0354, papyrus d'Oxyrhynque) s'étend jusqu'au v. 1211 et reste aussi
  en f176v. Rien à déplacer.

### Passages marqués en orange (`\eff`) dans la source

Aucun dans l'étendue du folio : ni dans la partie grecque (l. 5405–5476, groupes « v. 1210-1216 »
à « v. 1226-1231 »), ni dans la traduction (l. 7657–7724). Aucun article désactivé (`%\commentaire`)
non plus. Seuls passages désactivés : deux bouts d'apparat (l. 5433, v. 1219 : « Σκ. ante versum in
mg. et Χορ. ante καὶ γέρον in R » ; l. 5469 : doublon de l'entrée de 1227), sans objet pour le
commentaire.

### Remarques hors tâche (fichiers non modifiés)

- Apparat de la source, l. 5468 : `\ligneApp{1127}` pour 1227 (πέπυσται R : πέπαισται Σ), même
  coquille de centaine que pour l'article 1229–31 ; la conversion a rangé cette entrée au v. 1127
  (`edition/donnees/travaux_anterieurs/apparat.tsv`, A0424). À rattacher au v. 1227 (f177r).
- `texte.tex` : le v. 1216 porte `n=1215` (doublon du v. 1215) ; l'Ἀρταμουξία du v. 1222 porte
  `n=1223` (doublon du v. 1223, ὀρθὴν ἄνω δίωκε), alors que la source met `\ligne{1222}` sur cette
  ligne ; le sigle ΤΟ. est répété devant les Ἀρταμουξία des vv. 1213 et 1216, au milieu d'une
  réplique de l'Archer (la source n'a pas de nouveau groupe à ces endroits).

## Composition

`./edition/compiler_folio.sh f177r` : OK, 5 pages (`.travail/folios/f177r.pdf`), aucun
débordement ni caractère manquant signalé. L'article `\cc{1216}` est composé sous la rubrique
« commentaire critique » en bas de la page de la transcription (p. 2, encore vide faute de
`diplo.tex`) ; `commentaire.tex`, sans article, ne produit aucune rubrique vide sous le texte et la
traduction (pp. 4–5).
