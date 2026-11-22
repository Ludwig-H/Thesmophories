# f162v (vv. 1–42) — vérification des *loci paralleli*

Contrôle exhaustif du registre `edition/folios/f162v/paralleles.tex` (vv. 1–39 le 21 nov. 2026,
vv. 40–42 le 22 nov. ; bilan en fin de document). Chaque parallèle (entrée principale, témoin fusionné
« idem », entrée reprise dans une note) a été retrouvé dans sa source : (1) référence (auteur, œuvre,
livre, vers ou section, numéro d'article), (2) texte grec cité, (3) pertinence pour le lemme.

## Méthode

- **Textes TEI de l'index** (Perseus, First1KGreek ; `outils/corpus/`) : chaque fragment de la
  citation imprimée (séparateurs « … », « / », « — ») est recherché, accents et esprits compris
  (grave = aigu), dans le passage désigné, puis dans tout l'ouvrage ; la ligne trouvée est comparée à la
  référence imprimée. Pages de Stephanus, de Casaubon, de Bekker et de l'édition de Plutarque : jalons
  (`milestone`) des fichiers TEI. Scripts : `.travail/f162v_lp_verif/` (`check_cts.py`, `loc_tei.py`,
  `fiche.py`).
- **Hésychius** : texte de l'édition Latte–Hansen–Cunningham (gloses décodées, numéro et page).
- **Éditions numérisées** (Kock, Nauck, Bergk, Dübner, CPG, Diels–Kranz, Photius de Theodoridis,
  Souda d'Adler, EM, Eustathe de van der Valk, PCG III.2 de Kassel–Austin, Tosi…) : lecture de la page
  (image ; couche texte native pour Theodoridis et Kassel–Austin).
- Corrections portées directement dans `paralleles.tex` ; elles sont journalisées dans
  `.travail/f162v_lp_verif/corrections.json`. **Attention** : le fichier était engendré par
  `.travail/f162v_lp_redac/rediger.py` ; une nouvelle génération effacerait ces corrections tant
  qu'elles ne sont pas reportées dans les collectes (`paralleles_1-21.json`, `paralleles_22-42.json`)
  et dans `plan.py`.

## Résultats par vers

### v. 1 (6 articles ; 47 parallèles + 17 témoins fusionnés)

Tout retrouvé. Contrôles notables : Ar. fr. 617 K.-A. sur PCG III.2 p. 327 ; Chionid. fr. 8 Kock
(Kock I p. 6) ; Eust. 148.46 sur van der Valk I p. 228 (la citation est à la l. 46) ; EM 167.46 sur
l'éd. de Sylburg (Leipzig 1816, col. 151–152 : la citation commence à la l. 46) ; Phot. π 1519 et
ο 469 sur Theodoridis III ; Tosi n° 705 et 2058 ; Pervig. Ven. 89–90 ; Eur. fr. 773.23–26 N.²
(numérotation de Nauck : v. 25 ὀρθρευομένα γόοις). Corrections :

- **Σ Ar. Thesm. 1** (citation) : pas de virgule après ἐν ἤθει (Dübner).
- **Anacreont. 9 Bergk** (référence) : 9.2, 8–10 (et non 9.1–2) : le v. 1 n'est pas cité.
- **Hsch. χ 325** (citation) : ἀσύν[θ]ετον, comme l'imprime Hansen–Cunningham.
- **Carm. pop. ap. Ath. 8.360c** (citation) : texte de Kaibel rétabli, καλὰς ὧρας ἄγουσα, /
  καλοὺς ἐνιαυτούς. La citation mêlait Kaibel (coupe des vers) et Gulick (καὶ καλούς), et
  « corrigeait » ὧρας en ὥρας alors que les deux éditions numérisées impriment ὧρας (accent dorien).
- Pertinence faible mais gardée : Hsch. α 1226 (ἀδωνηίς, nom de l'hirondelle) sous « χελιδών (ὄρθρος) ».

### v. 2 (6 articles ; 49 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Ar. fr. 932 K.-A. (= 661 Kock) sur PCG III.2 p. 419 ; Antiph.
fr. 222.8 et Alex. fr. 173.15, 257.4–5 Kock (Kock II p. 109, 362, 391) ; Pherecr. fr. 90 Kock (et
Suid. π 1125) ; Soph. fr. 19 N.² (TGF² p. 135) ; Pl. *Phdr.* 230d–e, 227a, 228b, *Thg.* 124a,
*Lg.* 722c (jalons de Stephanus) ; Babr. 98.15–16. Correction :

- **Herod. 2.34** (référence) → 2.33–34 : κἠμὲ τὸν ξεῖνον finit le v. 33 (Nairn 1904, p. 20).

### vv. 3–4 (7 articles ; 39 parallèles + 1 entrée reprise)

Tout retrouvé. Contrôles notables : Plaute (*Amph.* 903b, *Men.* 466, *Pers.* 287, *Rud.* 424,
*Merc.* 123b–125, *Cas.* 414–415) et Pline (*HN* 11.205, 26.83) sur les TEI latins de Perseus ;
Plu. *Mor.* 831c, Pl. *Ti.* 72c–d, *Smp.* 215d (jalons) ; Arist. *HA* 496b16–17 (lignes de Bekker
recoupées par LSJ s.v. φρήν, πλευρόν, τερατώδης) ; Herod. 3.70 (Nairn p. 39) ; Apostol. 8.25
(CPG II p. 433, οἱ sic) ; Alex. fr. 99 Kock. Corrections :

- **Nicopho fr. 12 Kock** (citation, référence) → fr. 12.2–4, avec la coupe des vers et la ponctuation
  de Kock (I p. 776) : πυρετὸς εὐθέως / ἥκει τρέχων, οὐκ ἄξιος τριωβόλου· / κᾆθ᾽ οὗτος …
- **Suid. κ 1999** (citation) : Adler imprime Κομιδῆ (III p. 150, image) ; la « correction » en
  Κομιδῇ est retirée.
- **Luc. *DMar.* 8.3** (référence) → 6.3 (8.3 Macleod) : 8.3 est la numérotation de Macleod ; la
  numérotation usuelle (Jacobitz, LSJ) est 6.3.

### vv. 5–6 (6 articles ; 43 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Plaut. *Truc.* 489–490, Hor. *Ars* 180–182, Sen. *Ep.* 6.5
(TEI latins) ; Tosi n° 1943 ; Apostol. 18.71 (CPG II p. 744) ; Aristomen. fr. 2.1–2 Kock ;
Eur. fr. 413.1 N.². Corrections :

- **Emp. 31 B 3 DK** (référence, citation) → 3.9–11 (et non 9–10) : la citation va jusqu'à ἢ ἀκοὴν
  ἐρίδουπον …, début du v. 11 (DK I⁶) ; coupe des vers rétablie.
- **Antipho Soph. 87 B 44 DK** (référence, citation) → col. 2.30–3.5 : νε|νομοθέτηται commence à la
  fin de la l. 30 ; Diels imprime ὀφθαλμ[ι]οῖς (Vors.⁴ II, Nachträge p. XXXII–XXXIII).
- **Pl. *Tht.* 201b** (référence) → 201b–c.

### vv. 7–8 (5 articles ; 22 parallèles + 7 témoins fusionnés)

Tout retrouvé (Greg. Cypr. L 2.79 et Macar. 5.90 sur CPG II p. 80 et 188 ; Tosi n° 1526 ; Pl. *Prt.*
343b, *Chrm.* 165a). Les deux parallèles de Blaydes pour la place de ἄν (*Thesm.* 554, *Eccl.* 1087)
sont faibles mais signalés comme tels par lui (p. 130) : gardés. Corrections :

- **Eur. *Hipp.* 345a** (référence) → 345 : « 345a » est un artefact de Perseus (φεῦ extra metrum
  coté à part).
- **Hsch. α 303** (citation) : πάνυ [μνώδης], πολύ… (Latte I p. 16) ; le mot athétisé avait été omis.

### vv. 9–10 (5 articles ; 35 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Epich. fr. 12 (éd. Diels = 23 B 12 DK) et Apostol. 12.13 (CPG II
p. 545) ; Men. *Mon.* 39 Meineke (FCG IV p. 340–341, v. 39) ; Plu. *Mor.* 13e ; Pl. *Lg.* 666a,
*Smp.* 176b, *Phd.* 65b. Corrections :

- **Stratt. fr. 1.2 Kock** (référence) → 1.1–2 (Kock I p. 711).
- **Ar. *Plut.* 1052b** (référence) → 1052 (artefact de Perseus, comme *Hipp.* 345a).
- **Emp. 31 B 2 DK** (référence, citation) → B 2.7–8, avec la coupe des vers (DK I⁶ p. 309).

### vv. 11–12 (5 articles ; 28 parallèles + 5 témoins fusionnés)

Tout retrouvé et exact : Σ *Thesm.* 11, 12 (Dübner) ; Apostol. 18.45, 18.47 (CPG II p. 730) ;
Greg. Cypr. 3.99 ; Σ Luc. 31.21 Rabe ; Plu. *Mor.* 122c ; Pl. *Phlb.* 44a, *Sph.* 245c ; Semon.
fr. 7.1–2 Bergk ; Anaxag. 59 B 6 DK (texte de Simplicius). Aucune correction.

### v. 13 (4 articles ; 33 parallèles)

Tout retrouvé et exact : Eur. fr. 484.2–3 et 839.12–14 N.² (numérotation de Nauck) ; Anaxag. 59 B 13
DK dans Simplicius (la césure ἐκί-νησεν du TEI expliquait l'échec de la recherche automatique) ;
Ov. *Met.* 1.6 ; Pl. *Prt.* 320c ; la note « τέως ; cf. van Leeuwen ad l. » (Plut. 834) est conforme à
van Leeuwen 1904 (v. 13 : *olim*, renvoi à Plut. 834). Aucune correction.

### v. 14 (3 articles ; 38 parallèles + 3 témoins fusionnés)

Tout retrouvé. Contrôles notables : Emp. 31 A 49 DK (DK I⁶ p. 292 : Aët. II 6, 3) ; Anaxag. 59 B 2,
8, 12 DK (Simplicius) ; Eur. fr. 52.3–4, 487, 839.1–3, 877, 941, 1023, 330.1–2 N.² ; Aesch. fr. 70 N.²
(TGF² p. 24). Corrections :

- **Emp. 31 A 49 DK ([Plu.] *Plac.* 2.6)** (référence) → 887a–b (et non 887c), d'après les jalons de
  Stephanus.
- **Ar. *Av.* 1400a** (référence) → 1400 (artefact de Perseus ; LSJ s.v. ἀλίμενος).
- **Pl. *Phd.* 109b** (référence) → 109b–c.

### vv. 15–16 (3 articles ; 25 parallèles)

Tout retrouvé. Contrôles notables : Emp. 31 B 86, 87 DK (DK I⁶ p. 343, Simp. in Cael. 529.21, 24) ;
Eur. fr. 839.3–5 et 898.7–12 N.² ; Aesch. fr. ap. Ath. 13.600b ; Pl. *Phd.* 96b, *Ti.* 45b, *R.*
507c, *Smp.* 212a. Correction :

- **Eur. fr. 484 N.²** (référence, citation) → 484.3–6 (et non 3–5) : γένος τε θνητῶν est le v. 6 chez
  Nauck (TGF² p. 511), que le TEI réunit au v. 5 ; coupe rétablie.

### v. 17 (3 articles ; 32 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Eratosth. *Cat.* 13 (Robert 1878, p. 98) ; Alcid. ap. Arist.
*Rh.* 1406a29 (LSJ s.v. ἀντίμιμος) ; Hsch. α 5460 ; Eur. fr. 185.3 N.² ; Pl. *R.* 508b. Corrections :

- **Emp. 31 B 84.7–8 DK** (citation) : λεπτῆισίν ⟨τ᾽⟩ ὀθόνηισι, iota adscrit de DK (I⁶ p. 342).
- **Sopat. ap. Ath. 6.230f** (référence, citation) → 230e ; coupe des trimètres rétablie.
- **Anaximand. ap. [Plu.] *Plac.* 2.20** (référence) → 889f–890a.
- **Ar. fr. ap. Ath. 9.372a (*Aiolosikon* II)** (référence, citation) → Ar. fr. 5 K.-A. (PCG III.2
  p. 37) ; coupe des deux vers rétablie.

### v. 18 (5 articles ; 40 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Pherecr. fr. 113.30–31 K.-A. (= 108 Kock) sur PCG VII p. 159
et Kock I p. 174, avec Poll. 10.75 (Bethe II p. 211) ; Moer. p. 212 Bekker (l. 27) ; Soph. fr. 774.1–2
N.² ; Poll. 10.147 ; Hsch. χ 575–577, λ 960, 965–966 ; Pl. *R.* 411a, Plu. *Mor.* 502d, Ath. 10.436e.
Corrections :

- **Soph. fr. 35 R.** (référence, citation) : le grec cité est la glose d'Hésychius γ 653 qui contient
  le mot de Sophocle → « (ap. Hsch. γ 653) » ajouté ; crux de Latte rétablie (†γλίδου).
- **Emp. 31 B 84.9 DK** (citation) : χοάνηισι … θεσπεσίηισιν (iota adscrit de DK).
- **Pl. *Phdr.* 235d** (référence) → 235c–d.
- ***AP* 4.3** (référence) → 4.3.14 : numéro du vers ajouté (l'épigramme a plus de cent vers).
- **Thphr. *Sens.* 41** (citation) : le texte de Wimmer (First1KGreek, avec la coquille αἰ pour αἱ)
  est remplacé par celui de Diels, *Doxographi Graeci* p. 511 (λεπταὶ καθάπερ† τῇ αἰσθήσει καὶ τῇ
  ἀκοῇ τέτρηται …).

### vv. 19–20 (4 articles ; 17 parallèles + 5 témoins fusionnés)

Tout retrouvé. Contrôles notables : Tosi n° 1971 et 2035 ; Stob. *Flor.* 29.24 Meineke (= 3.29.24
Hense) ; Sol. ap. Pl. *Amat.* 133c, Plu. *Sol.* 31.3, Zen. 3.4, Diogenian. 3.80, Suid. γ 246.
Corrections :

- **Parm. 28 B 6.7 DK** (référence, citation) → B 6.6–7, avec la coupe du vers (DK I⁶).
- **Aesch. fr. 396 R.** (référence) → fr. 396 N.² : numéro vérifié chez Hense (« fr. 396 N.² ») et
  dans LSJ, qui suivent Nauck ; Radt n'est pas accessible pour contrôler la concordance.

### v. 21 (5 articles ; 27 parallèles + 17 témoins fusionnés ou repris)

Tout retrouvé. Contrôles notables : Eup. fr. 342 K.-A. (= 314 Kock) sur PCG V ; Soph. fr. 14 R.
(= 13 N.², TGF² p. 133 ; numéro de Radt confirmé par K.-A. ad Eup. fr. 342) avec ses témoins
(Pl. *Thg.* 125b, *R.* 568a–b, Aristid., Stob. *Flor.* 48.5 Meineke, Gell. 13.19.1–2, Lib. *Ep.* 35.3,
Zen. 5.98, App. Prov. 4.76, Macar. 7.76, Apostol. 15.58, Suid. σ 823) ; Them. *Or.* 6, p. 72c,
jusque-là lu chez Nauck seulement, vérifié sur l'édition de Hardouin (1684, p. 72) ; note « ἐν δὲ
τοῖς Ἥρωσιν = Ar. fr. 323 K.-A. » vérifiée (PCG III.2) ; Thgn. 35–36 et ses témoins ; Luc. *DMort.*
11.4 (numérotation usuelle, = 21.4 Macleod) ; Sen. *Ep.* 94.40. Corrections :

- **Eup. fr. 342 K.-A.** (citation) : οἷόν γε πού ᾽στι (γε atone chez K.-A.).
- **Pl. *R.* 568b** (témoin fusionné, référence) → 568a–b.

### vv. 22–24 (8 articles ; 44 parallèles + 6 témoins fusionnés)

Tout retrouvé. Contrôles notables : Ar. *Vesp.* 166 (Hall–Geldart, image) ; Σ Soph. *Ant.* 31 ;
Σ Pi. *N.* 7.127c ; Com. adesp. fr. 610 Kock et ses témoins (Macar. 6.90, Apostol. 2.94 : CPG II
p. 200, 286 ; Tosi n° 1647, 461) ; Timocl. fr. 6.15 Kock ; Pl. *Smp.* 190d ; [Plu.] *Mor.* 4a.
Corrections :

- **Ar. *Thesm.* 1015–1018** (référence) → 1015–1017 : la référence mêlait la numérotation usuelle
  (début) et celle de Hall–Geldart (fin). Le même contrôle, étendu à toutes les références aux
  *Thesmophories* du registre (table `edition/donnees/concordance_vers.tsv`), a fait corriger
  **Ar. *Thesm.* 376 → 375** (v. 2, ἐκκλησίαν ποιεῖν : numéro de Hall–Geldart, cf. CONVENTIONS § 5).
- **Soph. *Ant.* 31** (référence) → 31–32 (κἀμοί est au v. 32).
- **Ar. fr. 53 Kock** (référence) → fr. 57 K.-A. (53 Kock), d'après PCG III.2 p. 59.

### vv. 25–26 (7 articles ; 36 parallèles)

Tout retrouvé et exact : Cratin. fr. 315 K.-A. (= 284 Kock) et Soph. fr. 815 R. (= 1014 N.²), dont
la Synagogue α 808 de Cunningham (p. 583) donne le texte et les numéros, et Synag. α 762 (p. 580) ;
Mnesim. fr. 4.21–23 Kock ; Σ *Thesm.* 25 ; Pl. *Cri.* 47b, *Euthphr.* 4a, *Smp.* 213b. Aucune
correction.

### vv. 27–28 (4 articles ; 18 parallèles)

Tout retrouvé. Contrôles notables : Ar. *Thesm.* 45 (Hall–Geldart : τί λέγει, le TEI porte τι) ;
Σ *Thesm.* 27 ; Thgn. 421–422 (Bergk) ; X. *Smp.* 6.10 ; Plu. *De fac.* 940f ; Pl. *Alc.* 1 127b,
*Cri.* 47d. Correction :

- **Ar. *Thesm.* 279** (citation) : δεῦρό νυν ὦ Θρᾷτθ᾽ ἕπου (élision aspirée, Hall–Geldart), et non
  Θρᾷττ᾽.

### vv. 29–30 (9 articles ; 43 parallèles)

Tout retrouvé. Contrôles notables : Ar. fr. 341 K.-A. (= 326 Kock, PCG III.2) ; Pherecr. fr.
155.19–21 K.-A. (= 145 Kock, PCG VII p. 181, où K.-A. rapprochent eux-mêmes *Thesm.* 29 sq.) ;
Σ *Ran.* 83–84 ; Herod. 6.48 (Nairn p. 75) ; Stesich. fr. 5 Bergk ; Pl. *Smp.* 173a, 175e, 223d ;
Ath. 5.217a, 6.224a ; Arist. *Po.* 1456a29–30, *Rh.* 1406b1–2, 1413b14 ; Plu. *Mor.* 645e.
Corrections :

- **Eur. *El.* 327** (référence) → 326–327.
- **Timocl. fr. 12.4 Kock** (citation, référence) : ὁ ποῖος οὗτος Βριάρεως est la conjecture
  d'Elmsley adoptée par Gulick ; Kock et Kassel–Austin impriment ὁ ποῖος; … ὁ Βριάρεως. L'entrée
  cite désormais K.-A. (PCG VII p. 764) et donne la conjecture entre parenthèses.

### v. 31 (6 articles ; 52 parallèles + 11 témoins fusionnés)

Tout retrouvé. Contrôles notables : Archil. fr. 178 W. (numéro de West donné par Latte à Hsch.
μ 1277) et ses témoins ; Alex. fr. 322 K.-A. et Eust. 863.29 (confirmés par PCG II) ; Eub. fr. 61
(= 61 K.-A., PCG V p. 224) ; Suet. *Blasph.* 53 Taillardat (Miller, *Mélanges* p. 415) ; App. Prov.
3.61–62 (CPG I p. 429) ; Σ *Il.* 4.141, Σ *Od.* 16.175 (césure σω-μάτων) ; Σ *Lys.* 802, 804 ;
Pl. *Prt.* 315d–e, *Smp.* 174b, *R.* 474e, 556d, *Phdr.* 239c–d. Hsch. ν 152 : Latte–Cunningham
imprime Κρατίνος (coquille de l'édition, non reproduite). Corrections :

- **Ar. *Eccl.* 60–67** (référence) → 60–66.
- **[Arist.] *Phgn.* 6.32** (référence) → 812a (pagination de Bekker ; « 6.32 » est le découpage du TEI).

### vv. 32–34 (9 articles ; 40 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Poll. 2.88 (Dindorf I p. 97, image : la phrase précède le § 89) ;
Archil. fr. 58 Bergk ; [Arist.] *Phgn.* 808a23 et Ps.-Polem. *Phgn.* 70 ; Plu. *Mor.* 177a–b ;
Σ *Thesm.* 32, 33 ; Tosi n° 2183 ; Plaut. *Epid.* 638, Ter. *Hec.* 863 ; Pl. *Tht.* 145a ; Luc.
*DMeretr.* 10.1 (même numérotation chez Jacobitz et Macleod). Corrections :

- **Eup. fr. 182 Kock** (référence) → fr. 195 K.-A. (182 Kock), PCG V p. 416.
- **Ephipp. fr. 14.7 Kock (ap. Ath. 11.509)** (référence) → fr. 14.7 K.-A. (= Kock), Ath. 11.509d.

### v. 35 (5 articles ; 31 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Ar. *Thesm.* 200–201 (Hall–Geldart, image : σύ γ᾽, le TEI porte
οὐ) ; Suid. β 287–288 ; Hsch. β 466–467 ; Pl. Epigr. (D.L. 3.32) ; Pl. *Smp.* 193b–c ; Ael. *VH*
2.21, 13.4 ; X. *Smp.* 8.32. Corrections :

- **Pherecr. fr. 7 Kock** (citation, référence) : τῶν γὰρ προτενθῶν ἐσμεν· (Kock I p. 146, PCG VII
  p. 108), et non ἐσμέν, (texte de Gulick) ; numéro K.-A. et source (Ath. 4.171e) ajoutés.
- **Pl. *Smp.* 177d** (référence) → 177d–e.

### v. 36 (6 articles ; 42 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Suid. π 3024, ε 586, Σ *Thesm.* 36 ; Phryn. Trag. fr. 17 N.²
(TGF² p. 724) ; Thgn. 1015 ; Carm. pop. (Hybrias) ap. Ath. 15.696a ; Ar. *Thesm.* 70 (Hall–Geldart :
ἐξέρχεται ; le TEI omet l'accent) et 293 (Θρᾷττ᾽ devant ἐκποδών). Corrections :

- **Ar. *Pax* 232–235** (référence) → 232–234.
- **Eur. *El.* 107–111** (référence) → 107–109.
- **Eur. *Ion* 76–81 et 94–101** (référence) → 76–80 et 94–98.
- **Ar. *Thesm.* 233** (citation) : μὴ φροντίσῃς· (Hall–Geldart ; le TEI porte φροντίσῃ).

### vv. 37–38 (10 articles ; 43 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Pherecr. fr. 155.10–12 K.-A. (PCG VII p. 180) ; Σ *Eq.* 964,
Σ *Plut.* 660, Σ *Thesm.* 38 (Dübner) ; Poll. 1.27–28 (Dindorf), 6.108 (Bethe) ; Hsch. α 1762,
μ 1915, 1917, 1926 ; Ar. *Av.* 908–909 (Hall–Geldart numérote 908 la ligne Μουσάων θεράπων ὀτρηρός,
que LSJ cite comme 909 : référence gardée) ; Pl. *Cra.* 401d, *Ion* 531d, *Smp.* 205b–c. Correction :

- **Hes. *Th.* 99–100** (référence) → 100.

### v. 39 (8 articles ; 38 parallèles + 3 témoins fusionnés)

Contrôles notables : Suid. ε 3792 (Adler II, p. 477, image : texte exact, λεώς) ; Hsch. ε 7264 et
λ 792 (Latte, images) ; Σ Eur. *Hec.* 532 (Dindorf 1863) ; Σ *Thesm.* 39 (Dübner) ; Mesom.
*Hymn. Sol.* 1, 5–6 sur Jan, *Musici scriptores Graeci*, p. 462 (image : Jan imprime « 5 » en
regard de ἦχοι, mais ses n°s 7–8 suivants confirment la numération usuelle, μέλλει = 5) ; Hor.
*Carm.* 3.1.1–4 et Tosi n° 2083 (« Favete linguis! ») ; Aesch. *Eum.* 1035 (Perseus saute 1034).
*Vesp.* 323–324 et *Pax* 974–975 (prières en dimètres anapestiques) et *Eccl.* 1019 (ἔστω de
décret) : parallèles faibles mais fondés, gardés. Corrections :

- **Ar. *Ach.* 395–400** (référence) → 396–400 (le v. 395 n'est pas cité).
- **Eur. fr. 773.43–73 N.²** (référence) → 773.44–75 (Nauck, TGF², p. 603–604, image : κόσμον =
  44, ἔχειν χρὴ / στόμ᾽ = 61–62, Ὠκεανοῦ … λαοί = 66–69, ἀλλὰ σῖγ᾽ ἔστω λεώς = 75) ; (citation)
  barre rétablie entre Ὠκεανοῦ πεδίων οἰκήτορες, / εὐφαμεῖτ᾽, ὦ (deux vers).
- **Eur. *Hec.* 530–533** (référence) → 531–533.
- **Call. *Ap.* 17** (citation) : ἀοιδῇ → ἀοιδῆι (iota adscrit de l'édition source, Wilamowitz ;
  de même Pfeiffer).

### vv. 40–42 (10 articles ; 67 parallèles + 1 témoin fusionné)

Contrôle du 22 nov. 2026 (reprise après l'interruption du 21 nov.). Tout retrouvé. Contrôles
notables : *Test.* Suid. θ 378 (Adler II, p. 718, image : la Souda cite les vv. 40–42 depuis
ἐπιδημεῖ γάρ, sans variante) ; Eur. *Hipp.* 498, *Phoen.* 865, *Hec.* 664, Soph. *OC* 1051–1053 ;
Ar. fr. 407 K.-A. (= 390 Kock ; PCG III.2, p. 223, où K.-A. rapprochent eux-mêmes Pi. *P.* 4.5) ;
Call. *Ap.* 12–13 ; Pl. *Prt.* 309d, 318b, 326a (jalons de Stephanus) ; X. *Mem.* 1.2.61 ;
Th. 1.136.3 ; D. 18.260, 33.25 ; Luc. *Symp.* 7 ; [Plu.] *De mus.* 2 (1131e) ; Ael. fr. 11 Hercher
(= Philem. test. 6 K.-A., PCG VII) ; Σ *Thesm.* 41 (Dübner, p. 264) ; Hsch. ε 2777, ε 4722, θ 572–573,
μ 623, μ 1742, π 2891 (Latte–Cunningham et Hansen, images) ; Zen. 1.89 et Diogenian. 6.50 (CPG I,
p. 29 et 277, images) ; les tragiques pour θίασος, μέλαθρα et δεσπόσυνος (TEI Perseus) ; Ar. *Thesm.*
67 et 874 (numérotation usuelle d'après `edition/donnees/concordance_vers.tsv`). La plupart de ces
rapprochements viennent de la note d'Austin–Olson ad 39–42 (p. 66–67), relue sur leur texte.
Corrections (13 ; journal `.travail/f162v_lp_verif/c_v40_42.json`) :

- **Phot. p. 145 Porson** (référence, citation) → Phot. κ 762, numéro de Theodoridis (II, p. 410,
  image), que donnent aussi Austin–Olson ad 40 ; texte de Theodoridis : κλῆισαι οἱ ἀρχαῖοι λέγουσιν,
  οὐ κλεῖσαι· καὶ κλῆιδα· … La citation reprenait Porson (p. 145, image) sans son astérisque après
  λέγουσιν ; les autres articles de Photius du registre suivent déjà Theodoridis.
- **Ar. fr. 348 K.-A.** (citation) : ἐς χορὸν, comme l'impriment Kassel–Austin (PCG III.2, p. 198,
  image ; var. lect. ἐς/εἰς chez Héphestion et Chéroboscos), et non εἰς (texte de Consbruch).
- **Zen. 2.70** (citation) : παῤῥησιάζεσθαι, graphie de CPG I, p. 51 (image), comme ἀῤῥένων en
  Zen. 4.27 dans le même registre.
- **Suid. θ 379–380**, témoin fusionné avec Σ *Thesm.* 41 (citation) : le micro-apparat ne disait pas
  que θ 379 omet l'article (Θίασος: ἱερὸς χορός, Adler II, p. 718) ; θ 380, glose distincte (venue
  d'Harpocration selon Adler), n'est pas une variante de la scholie : elle est désormais citée à part
  (Suid. θ 380 Θίασος: τὸ ἀθροιζόμενον πλῆθος …).
- **Suid. θ 381** (citation) : οἱ Κλεισθέναι καὶ Τίμαρχοι (Adler II, p. 718, image ; de même κ 2171 et
  Bekker), et non Κλεισθένεις (Gaisford).
- **Σ Ar. *Ran.* 93** (citation) : coupe des deux vers d'Euripide (*Alcmène*) rétablie, εὐφυὴς κλάδος, /
  χελιδόνων μουσεῖον (Dübner, p. 277, image).
- **Zen. 4.27** (citation) : lemme du proverbe rétabli en tête (Θάμυρις μαίνεται: … Ὁ Θάμυρις …) ;
  texte conforme à CPG I, p. 91 (image : κιθαρῳδίαν ; le TEI de First1KGreek porte la coquille
  χιθαρῳδίαν).
- **Pl. *Ion* 533e–534b** (référence) → 534a–b : le jalon 534a précède οὐκ ἔμφρονες ὄντες ὀρχοῦνται,
  et rien de 533e n'est cité ; ἐκ Μουσῶν κήπων … φέρουσιν est en 534b.
- **Anaxandr. fr. 41.33 Kock (= 42.33 K.-A.)** (référence, citation) → fr. 42.32–34 K.-A. (= 41 Kock) :
  même numérotation des lignes dans PCG II, p. 262 et chez Kock II, p. 152 (images) ; la citation
  couvre les vv. 32–34 (δεσποσύνοις au v. 33) ; coupe des dimètres rétablie : τούτων δ᾽ ἔσται πολὺ
  σεμνότερον / καὶ λαμπρότερον παρὰ δεσποσύνοις / τοῖς ἡμετέροις.
- **Eur. *Hec.* 1293–1294** (pertinence) → 1293–1295 : la citation s'arrêtait avant μόχθων, dont τῶν
  δεσποσύνων est l'épithète, et faisait croire à un emploi substantivé ; l'hyperbate de fin de vers est
  justement celle de *Thesm.* 41–42.
- ***h.Cer.* 144** (pertinence, référence) → 143–144 καί κε λέχος στορέσαιμι μυχῷ θαλάμων εὐπήκτων /
  δεσπόσυνον : l'adjectif qualifie λέχος (LSJ s.v. δεσπόσυνος : « λέχος h.Cer. 144 ») ; la suite citée
  (καί κ᾽ ἔργα διδασκήσαιμι γυναῖκας) était sans rapport avec le lemme.
- **Tyrt. fr. 6.2 Bergk** (citation) : ἀναγκαίης ὕπο λυγρῆς (anastrophe ; PLG⁴ II, p. 12, image), et
  non ὑπὸ, texte de Pausanias 4.14.5 (Perseus).
- **Tim. *Pers.* 136 (= PMG 791.125)** (référence, citation) → 135–136 (= PMG 791.124–125) : Ματρὸς
  οὐρείας = 791.124, δεσπόσυνα γόνατα πεσεῖν = 791.125 (Page, p. 409, image) ; chez Wilamowitz 1903
  (archive.org `timotheosdiepers0000uvwi`) οὐρεί-|ας chevauche 135–136 (index : οὐρείας 135, γόνατα
  136) ; barre placée selon la colométrie de Page.

Pertinence : rien à supprimer. Parallèles faibles mais gardés, au rang P1 ou P2 qu'ils occupent :
Hsch. ε 2777 (ἐνδημία, glose tirée de Grégoire de Nazianze), Diogenian. 6.50 et Zen. 4.27 (proverbes
sur les Muses), Hes. *Th.* 22–23, Hsch. π 2891 (μελοποιός substantif, alors que μελοποιῶν est ici un
participe : Austin–Olson ad 42).

Hors registre, à signaler : le commentaire (`commentaire.tex`, vv. 41–42) renvoie au « *Phaéton*,
v. 796 » pour ἀσπιδοφέρμονα θίασον ; c'est Eur. *Phén.* 796 (le registre a la bonne référence). Pistes
relevées mais non vérifiées, donc non ajoutées : pour δεσπόσυνος, Austin–Olson ad 42 citent aussi
Ar. fr. 734 K.-A. et Eur. *Phaéth.* 88 ; pour Phot. κ 762, Theodoridis renvoie à Suid. κ 1772 + 1775 et
Ael. Dion. κ 29.

## Bilan

- **Contrôlés** : tout le registre, soit 149 articles, 929 parallèles, 86 témoins fusionnés (« idem »)
  et 3 entrées reprises dans une note (vv. 1–39 le 21 nov. 2026, vv. 40–42 le 22 nov.). Le registre
  compte désormais 930 parallèles et 85 témoins fusionnés (Suid. θ 380 cité à part, v. 41).
- **Introuvables** : aucun ; **suppressions** : aucune.
- **Corrections** : 70 (57 pour les vv. 1–39, 13 pour les vv. 40–42), dont 47 portent sur la référence
  (vers, section de Stephanus ou de Bekker, numérotation d'édition — Kock → Kassel–Austin, Porson →
  Theodoridis, Macleod → numérotation usuelle —, artefacts de Perseus comme « 345a »), 33 sur le
  grec cité (texte d'une autre édition que celle de la référence, coupe des vers, iota adscrit,
  coquilles du TEI, micro-apparat incomplet) et 2 sur la pertinence (citation tronquée avant le nom
  que l'adjectif qualifie) ; plusieurs touchent à la fois la référence et la citation.
- Toutes les corrections sont portées dans `paralleles.tex` et journalisées dans
  `.travail/f162v_lp_verif/corrections.json` ; voir l'avertissement de la section « Méthode » sur
  la régénération par `rediger.py`.
