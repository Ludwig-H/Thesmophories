# Conventions de l'édition

Document de référence pour tous les contributeurs (humains ou agents). Il complète
`CLAUDE.md` (règles générales), `ravennas/FORMAT_TRANSCRIPTION.md` et
`ravennas/GUIDE_TRANSCRIPTION.md` (transcription diplomatique).

## 1. Architecture d'une unité (un folio de R)

| page | contenu | fichier(s) |
|---|---|---|
| I gauche | transcription diplomatique de R ; apparat critique dans le prolongement des lignes ; en bas : *loci paralleli* puis commentaire critique | `diplo.tex` (généré depuis `ravennas/transcription/fXXX.xml`), `apparat.tex`, `paralleles.tex`, `critique.tex` |
| I droite | fac-similé du folio | `edition/images/fXXX.jpg` |
| II, III… gauche | texte grec établi (structure, mètres, scansion des parties chantées) | `texte.tex` |
| II, III… droite | traduction française (didascalies, structure) | `texte.tex` |
| bas des pages II, III… | commentaire de la pièce (quatre colonnes par double page) | `commentaire.tex` |

Tous les fichiers sont dans `edition/folios/fXXX/`. L'apparat et le commentaire
sont ancrés par numéro de vers ; les scholies par numéro de ligne du manuscrit.

## 2. L'apparat critique

### 2.1 Principe

L'apparat est en regard de la transcription diplomatique, qui montre déjà l'état
exact de R (orthographe, accents, esprits, ponctuation, corrections et mains). Il ne
répète donc pas ces minuties : il dit, pour chaque lieu où **le texte établi**
s'écarte de R, d'où vient la leçon retenue, et il signale les leçons et conjectures
qui comptent pour la constitution du texte. Le lecteur sait ainsi d'un coup d'œil
s'il lit Aristophane selon R ou selon un éditeur — c'est l'intention première de
l'édition.

Ne figurent **pas** dans l'apparat (visibles dans la transcription, normalisés en
silence dans le texte établi) : fautes d'accent et d'esprit de R, iota souscrit ou
adscrit, apostrophes et élisions graphiques, ν éphelcystique, ponctuation (sauf
incidence sur le sens), répartition des mots, fautes d'orthographe sans portée
(iotacismes, ο/ω, αι/ε) — sauf si un éditeur en a tiré une leçon.

### 2.2 Forme

Apparat **positif** : numéro du vers en gras, lemme (leçon du texte établi) suivi de
sa ou ses sources, deux-points, leçon(s) rejetée(s) avec leurs sources ; entrées
séparées par « ‖ » quand elles se suivent dans un même vers.

```
\app{18}{\vv{18} ἀκοὴν δὲ χοάνης R : ἀκοῆς δὲ χοάνην Biset : ἀκοῇ δὲ χοάνην Boissonade}
\app{1}{\vv{1} ἆρά ποτε Biset : ἄρα πότε R}
```

Ordre des sources : R et ses mains (R¹, R², R³, R^XVI), papyri, scholies,
testimonia, apographe (M), imprimés anciens (Iunt.), puis éditeurs et critiques dans
l'ordre chronologique. Conjectures non retenues mais dignes d'être connues : après les
leçons rejetées (« fort. … Bibi », « … Blaydes »). Abréviations latines usuelles en
italique : *om.*, *add.*, *del.*, *transp.*, *suppl.*, *coni.*, *fort.*, *in ras.*,
*s. l.* (supra lineam), *in mg.*, *ac*/*pc* (ante/post correctionem), *γρ.*, *dub.*,
*cf.* Le reste est en grec ou par sigles ; aucune phrase française dans l'apparat
(les discussions vont au commentaire critique).

### 2.3 Sigles (provisoires, à arrêter avec l'étude graphologique)

- **R** — Ravenne, Classense 429 (milieu du Xe s.) ; R¹ : le copiste ; R^ac / R^pc :
  avant / après correction (correcteur indéterminé) ; **R²** : la main des scholies
  (S2 d'Orsini), correcteur ancien ; R³ : main médiévale postérieure (si attestée) ;
  **R^XVI** : main du XVIe s. (préparation de la copie d'imprimerie de 1516 ;
  attribuée à Euphrosynus Boninus, attribution non démontrée) ; R^γρ : variante notée
  γρ(άφεται).
- **Σ** — scholies de R (Σ^lem : lemme d'une scholie).
- **Π** — papyri (numérotation et contenu : `recherche/papyrus.md`).
- **M** — Monacensis gr. 492 (XVe s.), apographe de R : ses leçons propres ne valent
  que comme conjectures.
- **Iunt.** — *editio princeps*, Florence, Giunta, 28 janvier 1516 (imprimée sur R).
- **Bibi** — conjectures de l'auteur de la présente édition.
- Éditeurs et critiques : par leur nom (liste et lieux de publication :
  `recherche/conjectures_sources.md` et `edition/donnees/repertoire_critique/`).
- Testimonia : Suid., Phot., Hsch., EM, EGud., Poll., Ath., Eust., etc.

### 2.4 Attributions

Une conjecture est attribuée à celui qui l'a publiée le premier, avec, en cas de
doute ou de désaccord des éditeurs modernes, une discussion au commentaire critique.
Ne jamais reprendre une attribution sans l'avoir contrôlée dans au moins deux
sources (répertoire critique) — les erreurs d'attribution de Coulon sont connues
(Austin 1987).

## 3. Le commentaire critique

- En français ; l'auteur parle à la première personne du singulier (« je »).
- Article = numéro(s) de vers en gras, lemme grec, « ] », discussion :
  `\cc{18}{ἀκοὴν δὲ χοάνης}{…}`.
- Contenu : témoignage de R (renvoi à la transcription et au fac-similé : ligne,
  main, état), leçons et conjectures, arguments (sens, mètre, usage avec parallèles
  vérifiés, paléographie), décision.
- Y vont : les discussions textuelles du commentaire antérieur de l'auteur (leçons,
  conjectures, attributions de répliques, suppressions, transpositions, colométrie),
  et toute nouvelle décision textuelle.

## 4. Les *loci paralleli*

- Abondants, mais tous **vérifiés** sur un texte source (corpus local
  `.sources/corpus/`, scan, édition) avec référence exacte ; citation brève du grec
  pertinent. Aucune référence de seconde main non contrôlée.
- Article : vers et lemme en gras, puis les parallèles groupés et dans cet ordre :
  *Test.* (tradition indirecte : citations du vers) ; Aristophane (pièces, puis
  fragments K.-A.) ; autres comiques ; tragiques (paratragédie, Euripide en tête) ;
  autres poètes ; prose ; scholies et lexicographes (Hésychius en particulier) ;
  parémiographes et proverbes (CPG, Tosi).
  `\lp{1 χελιδών]}{Hes. \textit{Op.} 568 ὀρθρογόη Πανδιονὶς ὦρτο χελιδών ; …}`
- Abréviations des auteurs et œuvres : celles du LSJ (et de Kassel–Austin pour les
  comiques, Kannicht–Radt–Snell pour les tragiques).

## 5. Le texte grec établi

- Orthographe attique normalisée (iota souscrit, ξυν-/συν- selon l'usage du poète et
  les éditeurs récents, crase et élision notées), ponctuation moderne, majuscule aux
  noms propres seulement.
- Personnages : abréviations grecques en petites capitales espacées (liste dans les
  liminaires) ; le « Parent » d'Euripide est nommé Μνησίλοχος, conformément au parti
  de l'auteur (dossier dans l'introduction ; R porte tantôt κηδ., tantôt μνη.).
- Mètres : étiquette en marge à chaque changement ; schéma métrique (⏑ – ⏓ ⏕ …) à droite
  des vers chantés ; renfoncements selon le type de vers ; rubriques de structure.

## 6. La traduction

- Celle de l'auteur, alignée vers à vers ; révisée seulement là où le texte change.
- Didascalies sobres, en italique, limitées à ce que le texte implique ou que la
  critique a établi (entrées, sorties, accessoires, machines), sans invention.

## 7. Le commentaire de la pièce

- Celui de l'auteur, conservé au maximum (style, ton, références), sans les
  discussions purement textuelles (passées au commentaire critique, avec renvoi si
  nécessaire).
- « je » pour l'auteur ; jamais son nom.
- Ses deux axes : la langue proverbiale (grecque et latine) et le dépouillement
  d'Hésychius.
