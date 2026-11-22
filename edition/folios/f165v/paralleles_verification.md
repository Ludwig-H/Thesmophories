# f165v (vv. 252–293) — vérification des *loci paralleli*

Contrôle exhaustif du registre `edition/folios/f165v/paralleles.tex` (22 nov. 2026), en cours. Chaque
parallèle (entrée principale et témoin fusionné « idem ») est retrouvé dans sa source et contrôlé :
(1) référence (auteur, œuvre, livre, vers ou section, numéro d'article des lexiques), (2) texte grec (ou
latin) cité, (3) pertinence pour le lemme.

## Méthode

- **Textes TEI** (Perseus, First1KGreek, Perseus latin ; index `outils/corpus/`) : chaque fragment de la
  citation imprimée (séparateurs « … », « / », « — ») est localisé dans le fichier TEI, mots exacts
  (accents et esprits compris, grave = aigu), et la ponctuation intérieure est comparée ; les jalons du
  début et de la fin (vers, livre, chapitre, section ; pages de Stephanus, de Casaubon, de Bekker, de
  l'édition de Plutarque) sont confrontés à la référence imprimée. Les cas non concordants sont repris un à
  un. Les textes latins qui manquaient au corpus (Apulée, Aulu-Gelle, Cicéron, Horace *Ep.*, Lucrèce,
  Martial, Ovide *Fast.* et *Her.*, Plaute *Curc.*, *Merc.*, *Most.*, Stace *Ach.*, Suétone *Cal.*) ont été
  pris chez Perseus (`canonical-latinLit`, dans `.sources/web/latin_perseus/`). Scripts :
  `.travail/f165v_lp_verif/` (`items.py`, `verif_auto.py`, `revue.py`, `v2.py`, `voir.py`).
- **Les *Thesmophories*** : les vers repérés dans le TEI de Perseus (numérotation de Hall–Geldart) sont
  convertis dans la numérotation usuelle (`edition/donnees/concordance_vers.tsv`, CONVENTIONS § 5) avant
  comparaison avec la référence imprimée.
- **Hésychius** : glose de l'édition Latte–Hansen–Cunningham (texte décodé, numéro et page).
- **PDF à couche texte native** (Photius de Theodoridis, PCG de Kassel–Austin, *Synagoge* de Cunningham…) :
  comparaison graphème par graphème, diacritiques compris (`v2.py`).
- **Éditions numérisées** (OCR d'archive.org : Dübner, Kock, CPG, Adler, Pollux, Nauck, Bergk, Eustathe…) :
  lecture de la page sur l'image (`voir.py` découpe la zone de la citation).
- Corrections portées directement dans `paralleles.tex`, journalisées dans
  `.travail/f165v_lp_verif/corrections.json`. **Attention** : le registre est engendré par
  `.travail/f165v_lp_redac2/rediger.py` ; une nouvelle génération effacerait ces corrections tant qu'elles
  ne sont pas reportées dans le plan (`plan.py`) et les collectes.

## Résultats par vers

### v. 252 (3 articles ; 30 parallèles)

Tout retrouvé. Contrôles notables : Zen. 4.79 (CPG I, image) ; Tosi n° 433 ; Suid. φ 511 (Adler IV
p. 743, image) ; Alciphr. 2.12 Schepers (III 15 de l'ancienne numérotation, notée dans le TEI) ; D. 42.22.
Correction :

- **Pl. *La.* 200b** (référence) → 200b–c (δεῖσθαι μαθεῖν est en 200c).

### v. 253 (5 articles ; 83 parallèles + 3 témoins fusionnés)

Tout retrouvé. Contrôles sur l'image : Dübner p. 84 (Σ *Nub.* 70), 249 (Σ *Lys.* 51, entre parenthèses
chez Dübner), 257 (Σ *Lys.* 645), 268 (Σ *Thesm.* 689), 271 (Σ *Thesm.* 1044), 276 (Σ *Ran.* 46) ; Adler I
p. 235 (Suid. α 2657 : Κωμαστῇ), p. 506 (γ 34), Adler III p. 192 (κ 2460 : γαλῆ ; le TEI porte τὀν),
p. 503–504 (ξ 169), p. 589 (ο 929) ; CPG I p. 56 (Zen. 2.93 : l'édition imprime la coquille χιτώντον,
non reproduite), p. 336 (Plu. *Prov. Alex.* 101, numéro en marge) ; CPG II p. 197 (Macar. 6.65), p. 338
(Apostol. 5.25) ; Gaisford p. 126 (*Prov. Coisl.* 64) ; Bethe II p. 69 (Poll. 7.65, Araros fr. 4 Kock :
κροσωτούς, « que d'autres écrivent au lieu de κροκωτούς ») et p. 67 (Poll. 7.55) ; Dindorf (Poll. 4.117) ;
Kock I p. 746 (Theopomp. fr. 52) ; PCG III.2 p. 171 (Ar. fr. 305.4) ; Érasme, *Adages* I ii 72 (n° 172).
Juv. 6, O 22–23 (= 388O–389O du TEI de Perseus) ; Lys. 219–220 (vers dit puis répété par Calonice) ;
Cic. *Har.* 44 (la virgule après fasceolis est séparée du mot par une note dans le TEI). Corrections :

- **Ar. *Lys.* 44** → 43–44 ; **Ar. *Thesm.* 941** → 941–942 ; **Ar. *Thesm.* 1044** → 1043–1044 ;
  **Ar. *Ran.* 46** → 45–46 ; **Ar. *Eccl.* 332** → 331–332 (références : la citation commence au vers
  précédent ou finit au suivant).
- **Cratin. fr. 40 K.-A.** (référence, citation) : la source est Macrobe, *Sat.* 5.21.6 (PCG IV p. 142 ;
  Kock I p. 23), non Athénée (le texte de Gulick l'insère en 11.475a d'après Macrobe) ; texte de K.-A.
  rétabli : τίν᾽ εἶχε (et non εἶχεν).
- **Σ Ar. *Ran.* 46** (citation) : la glose κροκωτῷ, γυναικείῳ ἐκ πήνης ἐνδύματι est entre crochets chez
  Dübner ; crochets rétablis.
- **Clem. Al. *Paed.* 2.10** (référence) → 2.10.109 (section de Stählin).
- **Apul. *Apol.* 13** (citation) : tragoedi[i] syrmate (Helm supprime le second i).
- **« Babr. fr. (Crusius, append. 3.1.39) »** (référence) → Ignat. Diac. *Tetrast.* 1.39 Crusius (= Babr.
  32) : tétrastique iambique d'Ignace le Diacre, imprimé dans le Babrius de Crusius (1897, p. 279), et non
  un fragment de Babrius.

### v. 254 (4 articles ; 60 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Crates fr. 2 K.-A. (PCG IV p. 86, où Bergk rapproche déjà *Thesm.* 254) ;
Pherecr. fr. 73 K.-A. (PCG VII p. 137) ; Phoenicid. fr. 4 K.-A. (PCG VII p. 391) ; Ar. fr. 325 K.-A.
(PCG III.2 p. 180) ; Phot. π 1113–1114 (Theodoridis III p. 256, couche texte native) ; *Synag.* π 829
(Cunningham p. 425, image) ; Σ *Thesm.* 254 (Dübner p. 266, image) ; Hsch. π 3096 ; Tosi n° 305 (l'OCR du
Drive porte « alet » ; l'image porte olet) et n° 2095 (image) ; Gell. 11.6.1 ; Plaut. *Most.* 273. Corrections :

- **Crates fr. 2 K.-A.** (référence) : Ath. 15.690d (et non 690e), comme K.-A.
- **Pherecr. fr. 67 Kock** (référence, citation) → fr. 73.5 K.-A. (= 67.5 Kock), texte de K.-A. : τράγηι.
- **Phoenicid. fr. 4.1 K.-A.** (référence) → 4.1–2 (ἑταιρεῖν est au v. 2) ; source précisée : Stob. 3.6.13
  (Hense III p. 282).
- **Ar. fr. 325 K.-A.** (citation) : τούτωι (iota adscrit de K.-A.).
- **Ar. *Ran.* 338** → 337–338 ; **X. *Smp.* 2.3–4** → 2.3 ; **Plu. *Dem.* 8.3–4** → 8.3 (références).
- ***Synag.* π 829** (citation) : Cunningham imprime ἀναγωγός (la forme ἀνάγωγος est la correction de
  Kock) ; leçon de l'édition rétablie, avec *sic*.

### v. 255 (6 articles ; 44 parallèles + 3 témoins fusionnés)

Tout retrouvé. Contrôles notables : Σ *Nub.* 635 (Dübner p. 112) et Σ *Vesp.* 30 (entre parenthèses chez
Dübner), images ; Poll. 7.67 (Bethe II p. 71, image) ; Ar. fr. 332 et 664 K.-A. (PCG III.2 p. 183–185 et
344, images) ; *Synag.* σ 261 (Cunningham p. 447, image), Phot. σ 639 (Theodoridis III p. 405) ; Hes. *Op.*
76 (vers athétisé, entre crochets dans le TEI comme dans la citation) ; Hes. *Th.* 574 ἀργυφέῃ (le TEI omet
l'iota souscrit). Corrections :

- **Ar. fr. 332 K.-A. (= 320 Kock ; Poll. 7.95 ; Clem. Al. *Paed.* 2.12)** (référence, citation) : la citation
  reproduisait la liste en prose de Clément sous le numéro de K.-A. ; or K.-A. impriment au v. 4 στρόφον
  (Poll. 7.95, codd. BC), στρόφιον étant la leçon de Clément (*Paed.* 2.12.124) et de Poll. 5.96. Entrée
  refaite : fr. 332.4 K.-A. μύρον, κίσηριν, στρόφον, ὀπισθοσφενδόνην (στρόφιον Clem., Poll. 5.96).
- **Ar. fr. 664 K.-A.** (citation) : K.-A. impriment ᾽ξέπιπτεν ; ἐξέπιπτεν (Pollux) passe au micro-apparat.
- ***Synag.* σ 261** (citation) : la *Synagogè* donne aussi la citation de *Lys.* 931 (τὸ στρόφιον ἤδη
  λύομαι) ; le micro-apparat la présentait à tort comme une addition de Photius et de la Souda.
- **Ar. *Vesp.* 1158** (référence) → 1157–1158.

### v. 256 (3 articles ; 36 parallèles + 2 témoins fusionnés)

Tout retrouvé. Contrôles notables : Σ *Nub.* 497 (Dübner p. 104, image) ; Apollod. Com. fr. 19 K.-A. (PCG
II p. 515, image) ; Harp. s.v. ἀμφιδέαι ; Hsch. π 1865 (β⟨ρ⟩ακ[κ]ία, signes de l'éditeur) ; Stat. *Ach.*
(TEI latin ajouté). Corrections (références) :

- **Eur. *Ba.* 938** → 937–938 ; **Stat. *Ach.* 1.325–329** → 1.326–329 (iniecitque sinus est le v. 326) ;
  **Apollod. Com. fr. 19.2 K.-A.** → 19.1–2 (les deux vers sont cités).
