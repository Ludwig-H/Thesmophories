# Métrique, colométrie et structure dramatique des *Thesmophories* — recension

*Document de travail (chantier « métrique-structure »). État : **en cours** — squelette créé le 26/10/2026, repris et complété le 26/10/2026 après interruption. Les mentions « [à compléter] » signalent ce qui reste à dépouiller ; « [non consulté] » ce qui n'a pas pu être vu ; « [à vérifier] » ce qui demande un contrôle sur la source.*

Ce document rassemble, partie par partie, les analyses métriques **publiées** des sections lyriques et des systèmes non iambiques des *Thesmophories*, la structure dramatique proposée par les principales autorités et l'état de la colométrie de R face à celle des éditeurs. Il ne propose pas de scansion nouvelle : la scansion vers par vers de l'édition sera faite à partir de ce relevé (workflow `.travail/workflows/metrique.js`).

Règles suivies : toute référence (auteur, page, schéma) a été lue sur la source elle-même (fichier local indiqué au § 1) ; ce qui est rapporté de seconde main est dit tel (« d'après X »). Les ouvrages sous droits restent dans `.sources/` (non versionné). Les notes de dépouillement détaillées (avec citations) sont dans `.travail/metrique/notes/` (non versionné).

**Numérotation des vers** : celle de Coulon 1928, reprise par Zimmermann, Sommerstein, Austin–Olson, Wilson. White 1912 suit Hall–Geldart (différence surtout dans le chant d'Agathon : H.-G. 129 = Coulon 130 ; voir § 3.2). Les éditions du XIXe s. (Enger, Velsen, Blaydes) ont leur propre numérotation dans les parties lyriques ; les renvois à ces éditions sont convertis quand c'est possible.

**Abréviations métriques** (celles de Zimmermann et de West) : ia iambe, tr trochée, cr crétique, ba bacchée, mol molosse, sp spondée, an anapeste, dact dactyle, io ionique, ch choriambe, do dochmiaque, hypod hypodochmiaque, p péon, gl/glyc glyconien, pher phérécratien, tel télésilléen, reiz reizianum, ar aristophanien, hipp hipponactéen, lec lécythion, ith ithyphallique, enh énoplien, D hémiépès ; 2ia = dimètre iambique ; ∧ catalexe ; anacl anaclase ; ‖ fin de période.

## Plan

1. Sources : état d'accès et sigles
2. Structure dramatique de la pièce (tableau comparatif)
3. Analyses métriques, section par section
4. Colométrie de R face à celle des éditeurs
5. Ressources numériques de scansion
6. Désaccords majeurs et problèmes ouverts (synthèse pour l'édition)

## 1. Sources : état d'accès et sigles

Fichiers locaux : `.sources/web/metrique/` (abrégé `web/metrique/`), `.sources/drive/` (Drive de l'auteur, téléchargé par un autre chantier), `.sources/web/editions/`. Notes de lecture détaillées (citations, numéros de lignes des fichiers texte) : `.travail/metrique/notes/*.md`.

### 1.1 Consultés (analyses métriques ou colométrie lues sur la source)

| Sigle | Référence | Fichier local | Ce qui sert pour les *Thesm.* |
|---|---|---|---|
| Hermann 1816 | G. Hermann, *Elementa doctrinae metricae*, Lipsiae 1816 | `web/metrique/godofredihermann00herm/` | texte restitué et responsions de 1136-1159 (p. 541-542) ; chants comiques avec proode et mésode (p. 730) |
| Fritzsche 1838 | F. V. Fritzsche, *Aristophanis Thesmophoriazusae*, Lipsiae 1838 | `web/metrique/thesmophoriazus00fritgoog/` | notes métriques *ad* 101 ss., 312 ss., 352 ss. (cité *ad loc.* : scan Google, numéros de page illisibles) |
| Muff 1872 | Chr. Muff, *Über den Vortrag der chorischen Partieen bei Aristophanes*, Halle 1872 | `web/metrique/berdenvortragd00muff/` | relevé des parties chorales et de leur exécution, p. 162-165 |
| Christ 1879 | W. Christ, *Metrik der Griechen und Römer*, 2e éd., Leipzig 1879 | `web/metrique/metrikdergriech00chrigoog/` | exemples ponctuels (p. 141, 282-283, 286, 291, 316-317) |
| Velsen 1883 | A. von Velsen, *Aristophanis Thesmophoriazusae*, Lipsiae 1883 | Drive : `fichiers/Grec/Aristophane/Thesmophories/Aristophanis_Thesmophoriazusae Von Velsen 1883.{pdf,txt}` ; `web/editions/1883_Leipzig_Velsen/` | **fins de ligne de R** dans les parties lyriques et anapestiques (« Scripturae discrepantia ») ; relevé partiel déjà dans `edition/donnees/repertoire_critique/velsen1883_*.jsonl` |
| Zielinski 1885 | Th. Zielinski, *Die Gliederung der altattischen Komoedie*, Leipzig 1885 | `web/metrique/diegliederungder00ziel/` | structure (§ 10, p. 79-108 ; tableau p. 214) ; prières de la parodos, chant d'Agathon |
| Rossbach 1889 | A. Rossbach (R. Westphal), *Theorie der musischen Künste der Hellenen*, 3e éd., III 2 : *Griechische Metrik*, Leipzig 1889 | `web/metrique/rossbach_westphal_III2_1887/` | 667-686 = 707-725 (p. 172-173), systèmes trochaïques (p. 193-194), 969 = 977 (p. 244-245), monodie (p. 320-322), 1136-1159 (p. 653, 667), dochmiaques (p. 806-807) ; = « R. et W. » de Mazon |
| Wilamowitz 1893 | U. von Wilamowitz-Moellendorff, *Aristoteles und Athen*, II, Berlin 1893 | `web/metrique/wilamowitz1893_AuA2/` (texte archive.org) | **analyse de 312-330 et 352-371**, p. 352-355 (la référence de Mazon et de Prato) |
| Masqueray 1899 | P. Masqueray, *Traité de métrique grecque*, Paris 1899 | `web/metrique/masqueray1899/` (texte archive.org) | ioniques d'Agathon, § 227 (p. 229-230) |
| Mazon 1904 | P. Mazon, *Essai sur la composition des comédies d'Aristophane*, Paris 1904 | `web/metrique/essaisurlacompos00mazouoft/` | structure et indications métriques, p. 126-137 (tableau p. 136) |
| Rogers 1904 | B. B. Rogers, *The Thesmophoriazusae of Aristophanes*, London 1904 | `web/metrique/thesmophoriazus00rogegoog/` | notes métriques (p. 14, 40-41, 49, 71-72, 102-103, 110, 122) ; appendice p. 197 |
| Hall–Geldart 1907 | F. W. Hall – W. M. Geldart, *Aristophanis Comoediae* II, Oxford 1907 | `.sources/corpus/thesmo_hall_geldart.tsv` (texte Perseus) | colométrie et numérotation de l'OCT ancien (suivie par White) |
| Schroeder 1909 | O. Schroeder, *Aristophanis cantica digessit…*, Lipsiae (Teubner) 1909 | `web/metrique/schroeder1909_cantica/` (UB Wuppertal, domaine public ; = « Aristophanis Cantica » du Drive) | **colométrie et schémas de toutes les parties lyriques**, p. 58-67 |
| Conradt 1910 | C. Conradt, *Die metrische und rhythmische Komposition der Komödien des Aristophanes* I, Programm Greifenberg 1910 | `web/metrique/conradt_963/` | décisions colométriques et comptes de « Reihen », p. 48-58 (Thesm.) |
| White 1912 | J. W. White, *The Verse of Greek Comedy*, London 1912 | `web/metrique/verseofgreekcome00whituoft/` | « Table of Structure and Rhythms » (p. 447-450) et analyses par périodes (§§ cités) |
| Wilamowitz 1921 | U. von Wilamowitz-Moellendorff, *Griechische Verskunst*, Berlin 1921 | `web/metrique/griechischeversk00wila/` | 101 ss., 312, 352, 433/459/520, 663-685, 953-958, 1136-1159 (pages citées au § 3) |
| Coulon 1928 | V. Coulon – H. Van Daele, *Aristophane* IV, Paris (CUF) 1928 (5e tirage 1962) | Drive : `fichiers/Grec/Aristophane/Œuvres complètes/Gec_seulement_…pdf` (texte grec seul, couche OCR) ; `drive/ravennas/Coulon_1928_…_textrep.txt` (jusqu'au v. 780) | colométrie, indications *Str./Ant.* ; texte de base de Zimmermann et de Prato |
| Zimmermann 1987 | B. Zimmermann, *Untersuchungen zur Form und dramatischen Technik der Aristophanischen Komödien*, III : *Metrische Analysen*, Frankfurt a. M. 1987 | `web/metrique/untersuchungen-03/` | **analyse colon par colon de toutes les parties lyriques**, p. 69-80 (renvois aux vol. I-II) |
| West 1987 | M. L. West, *Introduction to Greek Metre*, Oxford 1987 | `web/metrique/west-1987-introduction-to-greek-metre/` | ioniques d'Agathon, p. 62 |
| Sommerstein 1994 | A. H. Sommerstein, *Aristophanes. Thesmophoriazusae*, Warminster 1994 | `drive/ravennas/Sommerstein_1994_Thesm_textrep.txt` | notes « Metre » en tête de chaque section (p. 160-237) |
| Prato 2001 | C. Prato (éd.), D. Del Corno (trad.), *Aristofane. Le donne alle Tesmoforie*, Milano (Fondazione Valla) 2001 | `drive/ravennas/Prato_2001_…_textrep.txt` (= `drive/textes_metrique/`) : introduction et bibliographie seulement | remarques métriques de l'introduction (p. XIV n. 1, XVI n. 6) ; **l'« Appendice metrica » (p. 343-358) n'est pas dans l'extrait** |
| Austin–Olson 2004 | C. Austin – S. D. Olson, *Aristophanes. Thesmophoriazusae*, Oxford 2004 | `drive/ravennas/AustinOlson_2004_Thesm_textrep.txt` : préface et introduction seulement | préface (renvoi systématique à Parker 1997), distribution des rôles (p. lxix-lxx) ; **commentaire (analyses métriques) non disponible** |
| Wilson 2007 | N. G. Wilson, *Aristophanis Fabulae* II, Oxford 2007 | `drive/editions/Wilson II pp 50-140 …_ocred 2 greek.pdf` (p. 50-140, couche OCR ; page imprimée = index PDF + 48) | colométrie et quelques notes métriques de l'apparat (p. 76, etc.) |
| Di Virgilio 2026 | L. Di Virgilio, « Il docmio nelle *Tesmoforiazuse* di Aristofane », in S. Cardinali, G. Galvani, R. M. Danese (a cura di), *μελιγάρυες ὕμνοι. Studi offerti dagli allievi di dottorato a Liana Lomiento*, Urbino 2026, p. 95-120 (accès libre, CC-BY) | `web/metrique/articles/DiVirgilio_2026_docmio_Tesmoforiazuse.{pdf,txt}` | **toutes les sections dochmiaques lues dans la colométrie de R** (699-701, 707-725, 913-914, 1015-1055, 1136-1159) ; rapporte les analyses de Parker 1997 |
| Perrot 2022 | S. Perrot, c. r. de L. Di Virgilio, *Le monodie di Aristofane* (2021), *AC* 91 (2022), p. 271 ss. | `web/metrique/articles/Perrot_2022_cr_DiVirgilio_Monodie.{pdf,txt}` | contenu de Di Virgilio 2021 |

### 1.2 Non consultés (à acquérir ou à dépouiller)

- **Parker 1997** = L. P. E. Parker, *The Songs of Aristophanes*, Oxford 1997 : référence de base d'Austin–Olson ; absent du Drive (« lacunes » de `.sources/drive/selection.md`) ; archive.org n'en a qu'un exemplaire en prêt contrôlé (`trent_0116403843448`). Connu ici seulement **d'après Di Virgilio 2026** (pour les dochmiaques). **[non consulté]**
- **Prato 2001, « Appendice metrica » (p. 343-358)** et commentaire : le PDF complet (`Prato LeDonAllTes.pdf`, Drive) est dans la file d'attente du chantier Drive, pas encore téléchargé. **[non consulté]**
- **Mastromarco–Totaro 2006** = G. Mastromarco – P. Totaro, *Commedie di Aristofane* II, Torino (UTET) 2006 : sur le Drive, pas encore téléchargé. **[non consulté]**
- **Koster** = W. J. W. Koster, *Traité de métrique grecque suivi d'un précis de métrique latine*, « deuxième édition augmentée » (titre du fichier Drive ; Di Virgilio 2026 cite « Koster 1962³ », p. 274-277 pour le dochmiaque) : sur le Drive, pas encore téléchargé. **[non consulté]**
- **Gentili–Lomiento 2003** = B. Gentili – L. Lomiento, *Metrica e ritmica. Storia delle forme poetiche nella Grecia antica*, Milano 2003 : non localisé ; connu par Di Virgilio 2026 (formes dochmiaques, p. 235-245). **[non consulté]**
- **Dale 1968** = A. M. Dale, *The Lyric Metres of Greek Drama*, 2e éd., Cambridge 1968 (cité par Sommerstein pour 1136-1159 : « Dale² 165-7 ») : archive.org, prêt contrôlé seulement. **[non consulté]**
- **West 1982** = M. L. West, *Greek Metre*, Oxford 1982 : non localisé. **[non consulté]**
- **Zimmermann 1984-1985** (vol. I *Parodos und Amoibaion*, vol. II *Die anderen lyrischen Partien*) : archive.org, prêt contrôlé ; seuls les renvois de vol. III sont connus. **[non consulté]**
- **Austin–Olson 2004, commentaire** (analyses métriques en tête de section). **[non consulté]**
- Monographies et articles cités par les éditeurs, non localisés : C. Prato, *I canti di Aristofane. Analisi, commento, scolii metrici*, Roma 1962 ; C. Prato, « I metri lirici di Aristofane », *Dioniso* 57 (1987), p. 203-244 ; C. Prato, « La cosiddetta "versione lirica" dell'*arà* nelle *Tesmoforiazuse* (vv. 352-371) », in *Mousike… in memoria di G. Comotti*, Pisa-Roma 1995, p. 277-285 ; E. Mitsdörffer, *Philologus* 98 (1954), p. 59-93 (monodie d'Andromède) ; F. Lourenço, « Metrical Notes on "Andromeda's Lament" in *Thesmophoriazusae* », *Euphrosyne* 28 (2000), p. 321-324 ; R. Pretagostini, « Dizione e canto nei dimetri anapestici di Aristofane », *SCO* 25 (1976), p. 183-212 ; B. Zimmermann, « Ioniker in den Komödien des Aristophanes », *Prometheus* 13 (1987), p. 124-132 ; O. Thomsen, in *Classica et mediaevalia F. Blatt septuagenario dedicata*, Copenhague 1973, p. 27-46 (947-1000) ; M. Pintacuda, *Interpretazioni musicali sul teatro di Aristofane*, Palermo 1981 ; P. Pucci, *Aristofane ed Euripide : ricerche metriche e stilistiche* (1961) ; W. Trachta, *Die Responsionsfreiheiten bei Aristophanes*, Diss. Wien 1968 ; L. Lomiento 2020 (amébée lyrico-épirrhématique, cité par Di Virgilio 2026). Toutes ces références sont reprises de bibliographies (Prato 2001, Austin–Olson 2004, Sommerstein 1994, Di Virgilio 2026) **[à vérifier sur les originaux]**.
- **Di Virgilio 2021** (*Le monodie di Aristofane. Metro musica drammaturgia*, Pisa-Roma 2021 ; analyse de la monodie d'Andromède p. 223-238 d'après Di Virgilio 2026, n. 27) ; **Di Virgilio 2023** (« Un antico modello drammaturgico nelle *Tesmoforiazuse* di Aristofane (Aristoph. *Th.* 655-688 e Aesch. *Eum.* 244-275) », *Bollettino dei Classici* s. III, 44, 2023 : dépôt institutionnel protégé par un contrôle anti-robot, non téléchargé) ; **Di Virgilio 2025** (*Aristofane. Tesmoforiazuse. I canti*, Pisa-Roma, cité dans la bibliographie de Di Virgilio 2026 ; existence non confirmée par la recherche web du 26/10/2026). **[non consultés]**
- Éditions disponibles localement mais **non dépouillées pour la métrique** : Enger 1844, Blaydes 1880, van Leeuwen 1904 (texte OCR inutilisable : le latin a été océrisé en grec), Dindorf, Bergk, Meineke (`.sources/web/editions/`). Leur colométrie n'est citée ici que de seconde main (apparats de Coulon et Zimmermann, notes de White et Rogers).

## 2. Structure dramatique

### 2.1 Tableau comparatif des découpages

Bornes telles que les donnent les auteurs (numérotation de chacun ; elle ne diffère pas de celle de Coulon pour ces bornes). « — » : pas de coupure à cet endroit chez l'auteur.

| Vers | Zielinski 1885, p. 214 (« Übersichtstabelle ») | Mazon 1904, p. 136 (tableau) | White 1912, p. 447-450 | Sommerstein 1994 (notes) |
|---|---|---|---|---|
| 1-294 | Prolog 1-294 | Prologue 1-295 (le texte, p. 126-129, dit 1-294) | Prologue 1-294 | — |
| 295-371/372 | Parodos I 295-371 | Parodos 296-371 (mais p. 129 : « il n'y a point, à proprement parler, de parodos ») | Parode 295-371 | « The parodos » 295-372 (p. 176) |
| 372-530 | Syzygie I 372-530 : épirrhème 372-432, ode 433-442, [443-465 « Einschiebsel »], antépirrhème 466-519, antode 520-530 | Ἀγών 372-530 | Scene I 372-519 | — |
| 531-573 | Agon 531-573 (« agonartige Scene ») | Scène de bataille 531-573 | Debate 520-573 | — |
| 574-654 | Zwischenscene I 574-654 | Scène de transition 574-654 | Scene II 574-654 | — |
| 655-764 | Parodos II 655-688 ; Parodos III 689-727 ; Zwischenscene II 728-784 | Intermède lyrique et orchestique 655-686 ; Péripétie 687-764 | Syzygy 655-764 | — |
| 765-784 | (dans Zwischenscene II) | Scène de transition 765-784 | Scene III 765-784 | — |
| 785-845 | Parabase 785-845 | Parabase 785-845 | Parabasis 785-845 | « Parabasis » 785-845 (p. 204) |
| 846-946 | Epeisodion I 846-946 | Scène de parodie 846-946 | Episode I 846-946 | — |
| 947-1000 | Stasimon I 947-1000 | Seconde parabase 947-1000 | Stasimon I 947-1000 | chant choral, « basically a hymn », 947-1000 (p. 218) |
| 1001-1135 | Epeisodion II 1001-1135 | Scène de parodie 1001-1135 | Episode II 1001-1135 | — |
| 1136-1159 | Stasimon II 1136-1159 | Choricon 1136-1159 | Stasimon II 1136-1159 | — |
| 1160-1231 | Exodos 1160 ss. | Dénouement 1160-1226 ; Exodos 1227-1230 | Exode 1160-1231 | — |

Autres découpages :

- **Muff 1872** (p. 162-165) : « Die πάροδος fehlt, da die Frauen unvermerkt zusammentreten » (renvoi à sa p. 86) ; il appelle *stasima* 668-685 = 707-725, 953-1000 et 1136-1159 ; parabase 785-845 sans antépirrhème.
- **Conradt 1910** (p. 58) : plan numérique en multiples de 25 « Reihen » : A 1(?)-279 (la ligne imprime « 6-279 »), B 280-573, C 574-784, D 785-845 (parabase, 12 × 5), E 846-946, 947-1127, 1128-1230 ; « Das Stück vor der Parabase ist also doppelt so groß wie das hinter ihr ».
- **Zimmermann 1985-1987** : le classement se lit dans les renvois du vol. III aux vol. I-II : sont traités au vol. I (*Parodos und Amoibaion*) 312-330 et 352-371 (« Bd. 1, 113-120 ») et l'amébée 699-701 + 707-725 (« Bd. 1, 231-233 ») ; au vol. II (*Die anderen lyrischen Partien*) 101-130, 459-465, 663-686, 913-915, 947-1000, 1015-1055, 1136-1159 ; 433-442 ≈ 520-530 porte un renvoi sans numéro de volume (« Bd. 143-145 ») (Zimmermann 1987, p. 69-80).
- **Schroeder 1909** : intitule 312-330 et 352-371 « Parodi instar » (p. 59), place la parabase en 785-845 (p. 64) et ne nomme pas les autres parties.
- **Austin–Olson 2004** : pas de tableau de structure dans l'introduction ; la distribution des rôles (p. lxix-lxx) range 39-62 et 101-129 parmi les « lyric parts » du tritagoniste. Les intitulés du commentaire ne sont pas accessibles **[non consulté]**.
- **Prato 2001** : l'introduction (p. XII-XVI) discute la double prière (295-371) et l'hypothèse d'un remaniement, sans tableau de structure.
- **Quijada Sagredo 2012** (« Intriga cómica versus intriga trágica en *Tesmoforiantes* », *Emerita* 80, p. 257-274 ; `web/metrique/articles/`) : défend l'unité organique de la partie postérieure à la parabase (suite des « tragédies de salut ») ; pas de découpage métrique.

### 2.2 Points discutés

1. **Absence de parodos d'entrée.** Le chœur ne chante pas d'entrée : Mazon 1904, p. 129 (« Le chœur sort en silence des tentes ») ; Muff 1872, p. 162 ss. (« Die πάροδος fehlt ») ; Zielinski 1885, p. 84-87 (pas de tétramètres ; deux prières du chœur précédées chacune d'une prière de la héraut). Ceux qui gardent le mot « parodos » l'appliquent au complexe 295-371/372 (proclamation en prose 295-311, chant 312-330, *ara* en trimètres 331-351, chant 352-371) : White 1912, p. 447 ; Sommerstein 1994, p. 176 (« modelled on the procedure at the opening of a meeting of the Assembly… the two songs are not in strophic responsion ») ; Zimmermann (vol. I) ; Schroeder (« Parodi instar »). Zielinski étend les « traces de la parodos » jusqu'au v. 727 (Parodos II 655-688, III 689-727 : p. 209-210, 214).
2. **Agôn.** Zielinski voit en 372-530 une syzygie épirrhématique (épirrhème = discours de Mica, antépirrhème = discours du Parent ; ode 433-442, antode 520-530) suivie d'une « scène de type agonal » 531-573 ; Mazon intitule 372-530 « Ἀγών » mais conclut (p. 136-137) qu'il n'y a « pas d'ἀγών véritable » (discours parodié du *Télèphe* + scène de bataille, comme les *Acharniens*) ; White place la coupure à 520 (« Debate 520-573 »). Le statut de 443-465 (deuxième discours + chant 459-465) divise : « Einschiebsel » (Zielinski), « mésode » (Enger, d'après Rogers 1904, p. 49 ; Schroeder le fait répondre à 663-667, cf. § 3.9).
3. **Groupe 655-764.** White le traite comme une « syzygy » (655-658 / 659-666 / 667-686 = 707-725 / 687-688 ~ 726-727 / 689-706 ~ 728-764, p. 448) ; Rossbach 1889, p. 172-173, y voit une disposition symétrique de tout le groupe ; Mazon le coupe en « intermède lyrique et orchestique » (655-686) et « péripétie » (687-764) sans responsion ; Zielinski, en « Parodos II-III ».
4. **Parabase sans partie lyrique** (785-845) : seulement tétramètres anapestiques (785-813), *pnigos* (814-829) et un épirrhème en tétramètres trochaïques (830-845), sans ode, antode ni antépirrhème : Mazon 1904, p. 133 ; Muff 1872, p. 162 ss. ; Sommerstein 1994, p. 204 (« the only Aristophanic parabasis which contains no lyrics »). Mazon et Schroeder (p. 64) isolent un *kommation* au v. 785 ; Conradt 1910 compte 29 tétramètres (805 supprimé).
5. **947-1000 : stasimon ou seconde parabase ?** « Seconde parabase » pour Mazon (p. 134-135 : « ressemble plus à une seconde parabase qu'à un simple χορικόν ») ; *stasimon* pour Zielinski, White, Muff ; hymne dansé pour Sommerstein (p. 218).
6. **Fin de la pièce.** Mazon distingue « dénouement » (1160-1226) et « exodos » (1227-1230 [*sic*]) ; White et Zielinski commencent l'exode en 1160. Schroeder (p. 67) : « Clauditur fabula duobus coryphaeae tetrametris anapaesticis » ; Muff (p. 165) : 1227-1230 « ein anapästisches System, vom Chore gesungen » ; White, § 291 (p. 116) : tétramètre + pentamètre anapestiques (1227-1231).

## 3. Analyses métriques, section par section

[à compléter]

## 4. Colométrie de R

[à compléter]

## 5. Ressources numériques de scansion

[à compléter]

## 6. Désaccords majeurs et problèmes ouverts

[à compléter]
