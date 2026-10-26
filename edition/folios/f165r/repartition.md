# f165r (vv. 209–251) — répartition commentaire critique / commentaire de la pièce

Source : `commentaire.tex` (conversion automatique de `latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 2023–2348).
Articles critiques déplacés dans `critique.tex` (`\cc`) ; articles de la pièce laissés dans `commentaire.tex` (`\comm`).
Texte et notes conservés mot pour mot, sauf les corrections listées ci-dessous.

État : terminé. 14 articles : 4 CRITIQUE (209, 217, 230, 234), 10 PIÈCE, 0 MIXTE. Le folio compile (`./edition/compiler_folio.sh f165r` : 7 pages).
J'ai contrôlé par script que `commentaire.tex` et `critique.tex` redonnent exactement l'original, aux corrections déclarées près. Les outils de travail sont dans `.travail/f165r/`.

## Articles

| plage | lemme (abrégé) | classement | action |
|---|---|---|---|
| 209 | ὦ τρισκακόδαιμον… Εὐριπίδης | CRITIQUE (attribution et découpe des répliques ; Εὐριπίδης / Εὐριπίδη) | déplacé dans `critique.tex` |
| 217 | ἢ μὴ διδόναι γ' αὐτὸν… | CRITIQUE (mètre ; correction γ' ἑαυτόν d'après Willems) | déplacé dans `critique.tex` |
| 224 | οὗτος σὺ ποῖ θεῖς; | PIÈCE (formule ; parallèle *Guêpes* 854, contrôlé dans le corpus Perseus) | reste dans `commentaire.tex` (pourra aussi nourrir les *loci paralleli*) |
| 224 | εἰς τὸ τῶν σεμνῶν θεῶν | PIÈCE (scholie : asile des Érinyes) | reste dans `commentaire.tex` ; coquille corrigée |
| 230 | ἔχ᾽ ἀτρέμα σαυτὸν κἀνάκυπτε | CRITIQUE (leçon de R défendue contre ἀτρέμας αὐτοῦ de Dobree / van Leeuwen ; note de Willems) | déplacé dans `critique.tex`, avec ses deux notes `\nc` |
| 232 | ψιλὸς αὖ στρατεύσομαι | PIÈCE (double sens de ψιλός ; digression sur Soph. *Ajax* 1120 sqq.) | reste dans `commentaire.tex` |
| 234 | βούλει θεάσασθαι σεαυτόν; — εἰ δοκεῖ, φέρε | CRITIQUE (mètre ; correction αὑτόν de Fritzsche) | déplacé dans `critique.tex` |
| 235 | Κλεισθένην | PIÈCE (Clisthène, cible d'Aristophane) | reste dans `commentaire.tex` |
| 237 | δελφάκιον | PIÈCE (lexique ; image du porc flambé ; *Souda* δ 205) | reste dans `commentaire.tex` ; coquille corrigée |
| 239 | τὴν κέρκον φυλάττου νυν ἄκραν | PIÈCE (image ; *olisbos*) | reste dans `commentaire.tex` |
| 241–2 | οἴμοι τάλας… τῆς φλογός | PIÈCE (parodie d'un appel au secours ; incendie ; Horace, Tosi) | reste dans `commentaire.tex` ; coquilles corrigées |
| 243 | θάρρει — τί θαρρῶ; | PIÈCE (parallèle : Plaute, *Curculio* IV, 3, 21, déjà cité par Fritzsche 1838 *ad loc.*, contrôlé sur son édition) | reste dans `commentaire.tex` |
| 247 | μὴ φροντίσῃς· ἕτερος… σπογγιεῖ | PIÈCE (éponges ; le voisin d'à côté, d'après Taillardat) | reste dans `commentaire.tex` |
| 248 | οἰμώξετ᾽ ἄρ᾽… πλυνεῖ | PIÈCE (sens de πλύνειν ; proverbes πλίνθον πλύνειν, πρωκτὸς λουτροῦ περιγιγνόμενος) | reste dans `commentaire.tex` ; note 1 remise à son appel ; coquille corrigée |

## « nous » d'auteur changés en « je »

Aucun : sur ce folio, l'auteur dit déjà « je » (« me semble », « me sera l'occasion », « J'emprunte »). Je conserve, parce qu'ils associent le lecteur :
- 209 : « le texte de notre unicodex » (le manuscrit unique, commun aux éditeurs et aux lecteurs) ;
- 248 : « Le sel de la boutade de Mnésiloque nous échappe » (nous, lecteurs modernes).

Les « on » de la citation de Willems (art. 230) ne sont pas touchés.

## Coquilles corrigées

- 209 : « Philogues, réfrénez… » → « Philologues, réfrénez… ».
- 217 : « \italique{Cavaliers}., 740 » → « \italique{Cavaliers}, 740 ». Le point est un reste de l'abréviation : le texte de Willems porte « *Cav.*, 740 » (note 4, `latex/Aristophane-Thesmo Annexes.tex`, l. 670).
- 217 : même citation, « διδόναι ἑαυτὸν τινι » → « διδόναι ἑαυτόν τινι » (aigu devant l'enclitique, comme dans le texte de Willems, *ibid.*).
- 224 (σεμνῶν) : scholie citée, « εἶχον οἵ καταλαμβάνοντες » → « εἶχον οἱ καταλαμβάνοντες » (article ; contrôlé dans Dübner, *Scholia graeca in Aristophanem*, 1842, p. 266 : οἱ καταλαμβάνοντες).
- 230, note 2 : « ll est vrai » (deux l minuscules) → « Il est vrai ».
- 237 : « c'est celle de de viande de cochon » → « c'est celle de viande de cochon » (mot répété).
- 241–2 : Horace, « paries cum priximus ardet » → « paries cum proximus ardet » (*Epist.* 1, 18, 84).
- 241–2 : « non d'οἶκός mais de πρωκτός » → « non d'οἶκος mais de πρωκτός » (accent aigu parasite).
- 248 : dans la source, l'appel de la note 1 (« Voir Photius ο 360… ») est un `\marqueur{}` vide (pour `\marqueur{1}`) après « laver une brique ». La conversion avait donc laissé cet appel vide et rejeté la note en fin d'article, après la note 2, avec une numérotation inversée. J'ai remis le `\nc` à la place de l'appel ; le texte de la note est inchangé.
- 248, même note : « \italique{s.v} » → « \italique{s.v.} ».

## Passages signalés

### Moteur LaTeX

- `\cc` ne composait pas les notes `\nc` : leur texte était perdu sans erreur, car les affectations de `\nc` sont locales à la boîte du commentaire critique. J'ai ajouté `\thesmo_flush_cnotes:` à la définition de `\cc` dans `edition/thesmo.cls` (une ligne, comme dans `\comm`). Les notes de l'article 230 sont désormais composées à la fin de l'article. Modification partagée par tous les folios : à valider par l'orchestrateur.
- Défaut antérieur, non corrigé (moteur partagé) : un `\nc` placé à l'intérieur de `\citComm` est perdu. C'est le cas de la note 2 de l'art. 241–2 (« J'emprunte la traduction… Renzo Tosi… »). `\citComm` ouvre un groupe et les affectations de `\nc` y restent locales. Le texte de la note manque donc dans le PDF, et l'appel suivant (« monde latin et roman ») reçoit lui aussi le numéro 2. Correction proposée : affectations globales dans `\nc` (`\int_gincr:N`, `\tl_gput_right:Nx`) et remise à zéro globale dans `\thesmo_flush_cnotes:`. Tout `\nc` placé dans un groupe (`\citComm{…}`, `\italique{…}`) est exposé au même défaut, sur les autres folios aussi.
- Dépassement de 3,6 pt (Overfull) : le long lemme grec de l'art. 209 dans la colonne étroite du commentaire critique (cosmétique).

### Passages marqués `\eff` (orange) dans la source

Les trois passages sont dans des lignes que l'auteur a mises en commentaire (`%`). La conversion ne les a pas repris et je ne les ai pas réintroduits :
- 231 (source, l. 2181) : article en projet, `\commentaire{231}{τί μύζεις;}{\eff{Érasme 702}}`. Simple pense-bête : sans doute les *Adages* d'Érasme (non vérifié).
- 234–5 (l. 2217) : article en projet sur le miroir. « Sur le τόπος comique du miroir, \cf Platon, \italique{Alcibiade}, I, 132. » est suivi, en `\eff`, de « Remarquons que ce doit être à ce moment que Mnésiloque saisit le miroir que l'on retrouve quelques scènes plus loin sur le cratère de Würtzburg. Et le poignard serait-il le rasoir ? ». L'hypothèse de mise en scène (cratère de Würzburg) est laissée en suspens ; la référence à Platon n'est pas vérifiée.
- 247 (l. 2322–2324) : `\eff{Ranae Ἐγώ; (486) Πῶς δειλὸς ὅστις σπογγιὰν ᾔτησά σε; Οὐ τἂν ἕτερός γ᾽ αὔτ᾽ εἰργάσατ᾽ ἀνήρ.}`, rapprochement avec *Grenouilles* 486 sqq. (ἕτερος et l'éponge).

### Autres passages mis en commentaire (`%`) par l'auteur, non repris (pour mémoire)

- 217 (l. 2078) : « Cette correction est d'autant plus facile à accepter si l'on s'imagine une version en onciales, ΓΕΑΥΤΟΝ ; un scribe ayant malencontreusement lu γε αυτον avant d'élider le γε. » Cet argument paléographique pourrait servir au commentaire critique. Voir aussi l'ancienne note sur Dindorf et le manuscrit de Munich (l. 2081), et, côté traduction, le renvoi « Cf. sur le texte de ce passage, v. 217, Bull. cité, note 4, ci-après » (l. 5554).
- 232 (l. 2190) : « Il n'y a donc pas lieu de corriger le texte : le « αὖ » sert au jeu de mots. » C'est une réponse à οὖν de von Velsen, que l'apparat de la source enregistre. Si l'auteur le reprend, l'article 232 deviendrait MIXTE.
- 237 (l. 2238) : Hésychius δ 599 (δελφάκιον = γυναικεῖον [αἰδοῖον]), « Mais ne nous égarons pas ! ».
- 241–2 (l. 2261) : plaisanterie écartée (« À l'eau ! Non mais, Allô quoi ! »).
- 247 (l. 2304–2320, 2329–2330) : citation de *Grenouilles* 481–490 avec un début de traduction ; « Retournons à notre vers : » ; remarque « encore énigmatique » (μελάμπυγος), corrigée en marge par « Pas énigmatique : Cf. Willems !! ».
- 248 (l. 2341–2343, 2349) : « Ce n'est pas au sens dérivé mais bien au sens propre qu'il faut prendre ici πλύνειν » ; les écuries d'Augias et l'hydre de Lerne ; « L'exégèse est de mon cru… ».

### Lemmes et texte établi (à harmoniser ; je n'ai rien changé)

- 209 : le lemme porte τρισκακόδαιμον (leçon de R, accent correct du vocatif), `texte.tex` τρισκακοδαίμον (accent fautif).
- 217 et 234 : les lemmes donnent la leçon de R (γ' αὐτὸν ; θεάσασθαι σεαυτόν), non le texte établi (γ' ἑαυτὸν ; θεάσασθ᾽ αὑτόν). Je les conserve ; à l'auteur de dire s'il faut les aligner sur le texte établi (CONVENTIONS § 3).
- 235 : le lemme porte Κλεισθένην (R et Suid. κ 1756, selon l'apparat de la source), le texte établi Κλεισθένη (Brunck).
- 241–2 : le lemme et `texte.tex` portent « ἓτερον » (esprit et accent fautifs, pour ἕτερον). D'après l'apparat de la source, le mot manque dans R et vient de PSI 1194 (restitution de Medaglia) : c'est le « 242e vers, lacunaire » de la note de l'art. 247. Aucun article critique ne traite ce lieu.
- 248 : le lemme porte « ἄρ᾽ », `texte.tex` « ἆρ᾽ ». À trancher, notamment sur l'image de R (non vérifié).

### Graphies à revoir (non corrigées : ce sont des fautes d'usage plutôt que de frappe)

- 232 : « Τεύκρος » (3 fois) pour Τεῦκρος ; « en terme d'armements » (→ en termes d'armements).
- 239 : « bien-sûr » (→ bien sûr).

### Divers

- 217 : « Willems (voir sa note 4 en annexe) » renvoie aux annexes de l'édition antérieure (`Annexes.tex`, « Note 4 aux *Thesmophories* : vers 217 »). Renvoi à garder ou à adapter selon les annexes de la nouvelle édition.
- 230 : l'article reproduit presque mot pour mot la note 5 de Willems (`Annexes.tex`, l. 682–685) ; d'où « M. van Leeuwen » et le « on » de l'auteur cité. L'annexe imprime ἀτρέμα αὐτοῦ, le commentaire ἀτρέμας αὐτοῦ. C'est cette seconde forme que Velsen 1883 (p. 22) donne pour la conjecture de Dobree (`edition/donnees/repertoire_critique/`) : je l'ai laissée.
