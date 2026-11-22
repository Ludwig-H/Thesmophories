# f163r (vv. 43–79) — vérification des *loci paralleli*

Contrôle exhaustif du registre `edition/folios/f163r/paralleles.tex` (21 nov. 2026), en cours. Chaque
parallèle (entrée principale et témoin fusionné « idem ») est retrouvé dans sa source et contrôlé :
(1) référence (auteur, œuvre, livre, vers ou section, numéro d'article des lexiques), (2) texte grec (ou
latin) cité, (3) pertinence pour le lemme.

## Méthode

- **Textes TEI** (Perseus, First1KGreek, Perseus latin ; index `outils/corpus/`) : chaque fragment de la
  citation imprimée (séparateurs « … », « / », « — ») est localisé dans le fichier TEI, mots exacts
  (accents et esprits compris, grave = aigu), et la ponctuation intérieure est comparée ; les jalons du
  début et de la fin (vers, livre, chapitre, section ; pages de Stephanus, de Casaubon, de Bekker, de
  l'édition de Plutarque) sont confrontés à la référence imprimée. Les cas non concordants sont repris un à
  un. Scripts : `.travail/f163r_lp_verif/` (`items.py`, `verif_auto.py`, `revue.py`).
- **Hésychius** : glose de l'édition Latte–Hansen–Cunningham (texte décodé, numéro et page).
- **Éditions numérisées** (OCR d'archive.org, PDF du Drive) : lecture de la page (image ; couche texte
  native quand elle existe).
- Corrections portées directement dans `paralleles.tex`, journalisées dans
  `.travail/f163r_lp_verif/corrections.json`. **Attention** : le registre est engendré par
  `.travail/f163r_lp_redac/rediger.py` ; une nouvelle génération effacerait ces corrections tant qu'elles
  ne sont pas reportées dans le plan (`plan.py`) et les collectes.

## Résultats par vers

### v. 43 (articles 43–45, 43–48, 43 ; 8 articles ; 79 parallèles + 6 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : Adler II p. 493 (Suid. ε 3997) et Tittmann col. 941 (Zonaras) ;
Bergk, PLG⁴ III p. 57 (Alcm. fr. 60 ; n° 89 PMG d'après Sommerstein 1994 ad 43–50) ; Jan, *Musici
scriptores*, Suppl. p. 24 (péan de Liménios, avec les voyelles redoublées de l'inscription : ἀελλωῶν,
Νηηρέως, οεῖδμ᾽) et p. 48–49 (Mésomède) ; Migne, PG 66 col. 1594–1595 (Synésios, *Hymne* III 72–83 ;
Κρανααὶ sic) ; Dübner p. 264 (Σ 43 ἐπεχέτω) et p. 309 (Σ *Ran.* 1309) ; CPG I p. 14, 62, 186 et CPG II
p. 389 (Apostol. 6.88d) ; Érasme, LB II 178 A et 601 B–C ; Tosi n° 1702 ; Theodoridis III (Phot. ν 190).
Arist. *HA* 542b (Simonide) confirmé par LSJ (ἀλκυόνειος, εὐδιεινός : 542b5–6). Dans Σ Eur. *Hec.* 533
(Dindorf, *recentiora*), le n° 536 du TEI est un numéro d'ordre : la scholie est bien sous « 533. νήνεμον ».
Ar. *Av.* 1397 : ἀνέμων juste (Perseus imprime ἀνεμων). Corrections :

- **Suid. ε 3997** (citation) : texte d'Adler rétabli (Ἐχέτω: κρατείτω … νήνεμος αἰθήρ· κῦμα …) ; la
  citation suivait la ponctuation de Bekker et ajoutait des guillemets.
- **Alcm. fr. 60 Bergk** (citation) : ὀϊωνῶν (Bergk, image agrandie), non οἰωνῶν.
- **Luc. *Trag.* 129–133** (référence) → 129–132 : la citation s'arrête à βαίνει δαίμων (v. 132).
- **Verg. *Aen.* 4.522–527** (référence) → 4.522–525 : vv. 526–527 non cités.
- **Zen. 3.17** (citation) : θηρᾷς: … ἀνοήτως τι ποιούντων (CPG I p. 62) ; « ; » et « τὸ » venaient du
  TEI First1KGreek.
- **Zen. 1.39** (citation) : ἐρέσσειν: (CPG I p. 14), non « ; » (même origine).
- **Σ Ar. *Ran.* 1309** (citation) : le crochet de Dübner ne se ferme qu'après la phrase suivante, non
  citée : « κυμάτων. …] ».
- Pertinence : faible mais signalée comme telle (P1) pour Zen. 1.38 et Érasme I.iv.85 (« parler au vent »)
  sous νήνεμος αἰθήρ ; gardés.

### v. 44 (2 articles ; 35 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles notables : Synag. κ 263 (Cunningham p. 296), Suid. κ 1278–1281 (κ 1278 :
lemme seul, Κελαδείτω), Hsch. κ 2130 sur l'image (Latte II p. 579), Eur. *HF* 678–679 (ἀοι-/δὸς
κελαδεῖ, coupe du mot dans Perseus), Pratinas chez Athénée (texte de Gulick). Corrections :

- **Aesch. *PV* 1048–1049** (référence) → 1048–1050 (ἄστρων διόδους, v. 1050).
- ***Od.* 2.420–421** (référence) → 2.421.
- **Ar. *Ran.* 384–385** (référence) → 385 ; **Ar. *Ran.* 1525–1527** → 1526–1527.
- **Pratin. ap. Ath. 14.617c** (référence) → 14.617d : dans l'édition citée (Gulick), ἐμός, ἐμὸς ὁ Βρόμιος
  suit immédiatement le jalon 617d.
- **Hsch. κ 2130** (citation) : κελαδων sans accent, comme l'imprime Latte (lemme d'accentuation douteuse,
  cf. son apparat).

### v. 45 (5 articles ; 84 parallèles + 4 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : Dübner p. 294 (Σ *Ran.* 665, l. 44–47) et p. 264 (Σ 45) ; Stallbaum II
p. 19 (Eustathe) ; Adler I p. 479 (Suid. β 370, 372, 375 : ἢ τὸ βησίον, le TEI porte ἡ par erreur) ; CPG II p. 539
(Apostol. 11.92) et p. 650 (15.85b, centurie XV) ; Érasme, LB II 605 F – 606 A (*Adag.* 2.6.71) ; Tosi n° 2072 ;
PCG VII p. 451 (Pl. Com. fr. 46) ; Nauck² p. 21 (Aesch. fr. 57). Theodoridis III p. 303 (Phot. π 1543) et
Cunningham p. 154 (*Synag.* γ 50) sur la couche texte native. Plaut. *Pseud.* 365 (parties b–d du vers dans le
TEI). Corrections :

- **Ar. *Ran.* 1285–1289** (référence) → 1285–1288.
- **Pl. Com. ap. Ath. 15.666d** (référence) → Pl. Com. fr. 46.9–10 K.-A. ap. Ath. 15.666e (numéro du fragment
  ajouté ; les vers cités suivent le jalon 666e).
- **Ar. *Vesp.* 106–108** (référence) → 107–108.
- **Pl. *R.* 8.564d** (référence) → 8.564d–e.
- **Plu. *Praec. ger. reip.* 32** (référence) → 32, 823f ; **Plu. *De garr.* 4 (503d–504c)** → 4, 503f–504a
  (étendue du chapitre remplacée par celle de la citation).
- **Eust. 1718.9–11** (référence) → 1718 (ad *Od.* 12.204 ; Stallbaum II p. 19.28–30) : la ligne de Rome où
  commence la citation n'est pas déterminable sûrement d'après les astérisques de Stallbaum ; (citation)
  βομβυλιός → βομβυλίος, comme imprime Stallbaum.

### v. 46 (3 articles ; 33 parallèles)

Tout retrouvé. Contrôles sur l'image : Mœris p. 192, l. 37 Bekker ; CPG II p. 197 (Macar. 6.69) ; PCG II p. 288
(Anaxilas). Eur. *Ba.* 561–564 (ἔν-/θα coupé entre deux vers dans le TEI) et Verg. *Aen.* 8.26–27 (TEI latin)
conformes. Corrections :

- **Pi. *P.* 1.6–9** (référence) → 1.6–7.
- **Anaxil. ap. Ath. 13.558a** (référence) → Anaxil. fr. 22.5 K.-A. ap. Ath. 13.558a (numéro du fragment ajouté).

### vv. 47–48 (5 articles ; 42 parallèles + 1 témoin fusionné)

Tout retrouvé. Contrôles sur l'image : Stallbaum, *Iliade* II p. 315 et *Odyssée* II p. 19 (Eustathe) ;
Dübner p. 264 (Σ 48). Theodoridis III p. 242 (Phot. π 982, couche texte native) ; Catull. 63.72 (TEI latin).
Corrections :

- **Eur. *Alc.* 578–586** (référence) → 578–579 (la citation s'arrête à λύγκες).
- **Eust. 790.13** (référence) → 790 (ad *Il.* 10.67 ; Stallbaum II p. 315.32–33) ; **Eust. 1718.10–11** → 1718
  (ad *Od.* 12.204 ; Stallbaum II p. 19.30) : mêmes raisons qu'au v. 45.

### v. 49 (3 articles ; 35 parallèles + 3 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : CPG I p. 2 (Zen. 1.2) ; Érasme, LB II 543 E (*Adag.* 2.4.63). Suid. α 125
(mot coupé, α ὔλησις, dans le TEI) conforme. Pertinence faible mais défendable (contraste) pour App. Prov. 3.43
(Καπνίας ποιητής) ; gardé. Corrections :

- **Érasme, *Adag.* 2.4.63** (citation) : Ἀγαθώνειος → Ἀγαθώνιος, que porte LB (ligature -ος).
- **Pl. *Smp.* 201c** (référence) → 201b–c ; **Pi. *N.* 7.20–21** → 7.21.

### vv. 50–51 (6 articles ; 59 parallèles + 3 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : Bergk, PLG⁴ II p. 392 (Archil. fr. 32) ; Kock III p. 400 (adesp. 12–14) ;
CPG II p. 197 (Macar. 6.74) ; Coulon, CUF I, apparat de *Nub.* 562. Theodoridis III p. 118 et 258 (Phot. ο 609,
π 1138, couche texte native) ; Ter. *An.* 267 et Plaut. *Amph.* 331 (TEI latins). Corrections :

- **Ar. *Nub.* 562** (pertinence) : le parallèle ne vaut pour προτέρους (conjecture du v. 50) que par la variante de
  V ; ajoutée d'après l'apparat de Coulon : (ἑτέρας RΦ : προτέρας V, Coulon). Le même apparat donne au v. 553
  πρότερον R pour πρώτιστον VΦ, autre exemple de la confusion (non ajouté : à l'auteur de juger).
- **Archil. fr. 32 Bergk ap. Ath. 10.447a–d** (référence) → Ath. 10.447b.
- **Ar. *Eq.* 877–879** (référence) → 877 ; **Eur. *Cyc.* 672–675** → 672.
- Pertinence faible (P1, gardés) : Lib. *Decl.* 26.34 et Zen. 6.5 (le chaudron de Dodone, bavardage) sous νήνεμος
  αἰθήρ.

### v. 52 (6 articles, dont 52–57 ; 72 parallèles + 8 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : Adler II p. 143 (Suid. δ 1547), III p. 240 (λ 181) et IV p. 805 (χ 297) ;
Tittmann col. 569 (Zonaras) ; Dübner p. 5 (Σ *Ach.* 79) et p. 264 (Σ 52) ; Bethe II p. 84 (Poll. 7.117) et
Nauck² p. 167 (Soph. fr. 162) ; Kock I p. 217 et PCG VII p. 683–684 (Téléclide) ; Dindorf, *Schol. Eur.* I p. 2
(Vita Euripidis) ; Stallbaum, *Odyssée* II p. 221 (Eustathe) ; EM p. 288 (Sylburg, réimpr. 1816) ; Tosi n° 59 ;
Érasme, LB II 85 (*Adag.* 1.2.39). Σ *Od.* 19.574 (Dindorf II p. 686, TEI) conforme. Corrections :

- **Suid. δ 1547** (citation) : ἁψίδας → ἀψίδας (Adler ; coquille du TEI).
- **Telecl. fr. 39–40 Kock ap. Vit. Eur.** (référence) → Telecl. fr. 41 K.-A. (39 Kock) ap. Vit. Eur. p. 2 Dindorf :
  le fr. 40 Kock (= 42 K.-A.) est Εὐριπίδας σωκρατογόμφους, non cité ; (citation) Εὑριπίδῃ → Εὐριπίδῃ (coquille
  du TEI).
- **Eust. 1879** (référence) → 1878 (ad *Od.* 19.574 ; Stallbaum II p. 221.2–3) : le passage précède le début de
  la page 1879 de Rome.
- **Ar. *Eq.* 461–470** (référence) → 461–469, et « … » au lieu de « — » entre 463 et 468 (vv. 464–467 omis).
- **Ar. *Ran.* 799–801** → 799–800 ; **Ar. *Eq.* 542–544** → 542–543 ; **Theoc. 7.45–48** → 7.45–47 ;
  **Pl. *Lg.* 7.803a–b** → 7.803a ; **Pl. *R.* 2.377a** → 2.377a–b ; **Plu. *De fort. Rom.* 9** → 9, 321e
  (références).
- **Pl. *Phlb.* 56b–c** (citation) : changements d'interlocuteur marqués (… — πῇ; — κατά τε…).

### vv. 53–54 (5 articles ; 74 parallèles + 4 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : PCG VII p. 180–182 (Pherecr. fr. 155) ; Bethe II p. 85 (Poll. 7.119) ;
Bergk, PLG⁴ II p. 189 (Thgn. 805–806) ; CPG II p. 223 (Macar. 8.58) ; Adler IV p. 573 (Suid. τ 789) ; Tosi n° 30 ;
Érasme, LB II 217 (*Adag.* 1.5.92), 645 (2.8.30), 688 (2.10.16) ; Dübner p. 264 (Σ 53, 54). Theodoridis III p. 485
(Phot. τ 391, 396) et Cunningham p. 700 (*Synag.* B α 2625) sur la couche texte native. Prop. 2.34.43 = 2.34b.19 du
TEI (numérotation continue juste). Corrections :

- **Pherecr. fr. 155 K.-A.** (références) : vers précisés, 155.14–15 (Phrynis) et 155.27–28 (« Philoxène »), avec
  les pages de Stephanus du *De musica* (1141f, 1142a).
- **Timoth. ap. Ath. 3.122c** (référence) → 3.122d ; (pertinence) citation complétée : … τὰ παλαιά· καινὰ γὰρ μάλα
  κρείσσω.
- **Pi. *O.* 9.48–49** (pertinence) : citation complétée par νεωτέρων (v. 49), mot qui fait le parallèle.
- **Ar. *Ran.* 818–821** → 819–821 ; **Eur. *Cyc.* 661** → 661–662 ; **Jul. *Or.* 3.112a** → 3.111d–112a ;
  **Pi. *N.* 7.77–79** → 7.77–78 ; **Plu. *De glor. Ath.* 350e** → 8, 350d–e (références).
- **Érasme, *Adag.* 2.10.16** (citation) : « rem absurdum » et « descalpi », comme LB (la citation portait absurdam,
  desculpi).
