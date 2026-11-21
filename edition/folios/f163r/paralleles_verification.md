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
