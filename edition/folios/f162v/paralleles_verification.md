# f162v (vv. 1–42) — vérification des *loci paralleli*

Contrôle exhaustif du registre `edition/folios/f162v/paralleles.tex` (21 nov. 2026). Chaque parallèle
(entrée principale, témoin fusionné « idem », entrée reprise dans une note) a été retrouvé dans sa
source : (1) référence (auteur, œuvre, livre, vers ou section, numéro d'article), (2) texte grec cité,
(3) pertinence pour le lemme.

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
