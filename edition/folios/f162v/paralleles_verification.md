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
