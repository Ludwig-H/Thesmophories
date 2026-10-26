# f169r (vv. 551–592) : répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f169r/commentaire.tex` (conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 4016–4289 ; articles
C0163–C0172 de `edition/donnees/travaux_anterieurs/commentaires.tsv` ; l'article C0173,
v. 593, est rattaché à f169v). Version d'origine de la conversion : `HEAD` (commit 5ae2914),
copiée dans `.travail/f169r/commentaire.orig.tex`. Règles : `edition/CONVENTIONS.md` § 3 et § 7.
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**État** : terminé (10 articles sur 10). Le travail a été fait en deux passes : la première a traité
l'art. 1, la seconde les art. 2 à 10. `./edition/compiler_folio.sh f169r` : OK (7 pages, ni
« Overfull » ni « Missing character »). Deux notes manquent pourtant dans le PDF, à cause d'un
défaut de la classe (voir « Composition » à la fin).

**Bilan** : CRITIQUE 2 (569 ; 575–6) ; MIXTE 1 (556–7) ; PIÈCE 7 (558–9, 568, 570, 578, 579–87,
582–3, 585). `critique.tex` : 3 articles `\cc` (556–7, 569, 575–6) ; `commentaire.tex` : 8 articles
`\comm`. 3 « nous » changés en « je » ; 13 coquilles corrigées.

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0163 | 556–7 | ὁρᾷς ὡς τλεγγίδας λαβοῦσαι / … τὸν σῖτον | MIXTE. Texte, classé CRITIQUE : la correction τὸν οἶνον de Küster, réfutée avec l'argument qu'Austin & Olson tirent d'Aristote ; la conjecture de l'auteur τὸν κύσθον pour τὸν σῖτον de R, fondée sur le sens obscène de σιφωνίζω (*Cycl.*, σίφων), sur la métathèse et sur le parallèle du v. 1114 (σκύτο R / κύστο Scaliger). Reste, classé PIÈCE : griefs des femmes contre Euripide, coupe d'Onésimos, jeu de scène de ὁρᾷς | Scindé avant « Profitons-en pour remarquer… ». Va dans `critique.tex` (`\cc{556–7}`, lemme d'origine) tout l'argument, de « Voilà un trait… » à la citation parodique du *Gorgias* (notes 1–2), suivi de « Pour la suite (la coupe d'Onésimos, et l'explication d'un ami qui garde τὸν σῖτον), voir le commentaire de la pièce. ». Reste dans `commentaire.tex` (`\comm{556–7}`, même lemme) la fin, de « Profitons-en pour remarquer… » au jeu de scène, avec la longue note sur la coupe d'Onésimos, précédée de « Pour le texte (τὸν κύσθον pour τὸν σῖτον de R) et le sens de σιφωνίζω, voir le commentaire critique. ». 1 « nous » → « je » ; 5 coquilles corrigées |
| 2 | C0164 | 558–9 | ὥς τ᾽ αὐτὰ κρέ᾽ ἐξ Ἀπατουρίων… / ἔπειτα τὴν γαλῆν φαμεν | PIÈCE (mœurs : viandes des Apaturies et procureuses ; la belette, « bouc émissaire » proverbial : *Paix* 1150–1152 et 793–795, Carcinos et ses *Souris*, La Fontaine, Delvau) | reste dans `commentaire.tex` ; 1 « nous » → « je » ; 2 coquilles corrigées |
| 3 | C0165 | 568 | λαβὲ θοἰμάτιον Φιλίστη | PIÈCE (realia : on ôte le manteau avant d'en venir aux mains : *Guêpes* 408, Hipponax contre Boupalos d'après la note de Willems ; « [θοιμάτιον codd.] » porte sur le texte d'Hipponax, non sur celui d'Aristophane) | reste dans `commentaire.tex` ; 2 coquilles corrigées (accents) |
| 4 | C0166 | 569 | πρόσθες μόνον | CRITIQUE (leçon de R πρόσθες ; πρόσθιγε de Willems, πρόσιθι de Cobet ; défense de πρόσθες par l'ellipse πρόσθες [τὴν χεῖρα] et ses parallèles ; ἅψαι μόνον, *Lys.* 365) | déplacé en entier dans `critique.tex` (`\cc{569}`, avec sa note `\nc`) ; 1 coquille corrigée (numéro de vers) |
| 5 | C0167 | 570 | τὸν σησαμοῦνθ᾽ ὃν κατέφαγες… | PIÈCE (realia et langue : le gâteau de sésame mangé le jour du jeûne ; les *mylles* de Syracuse, Athénée XIV 647a ; la peur et le ventre ; les gâteaux astringents, *Nuées* 506–508, Τροφωνίου / στρόφος, Athénée I 4d ; la συρμαία purgative, *Danaïdes*) | reste dans `commentaire.tex` ; 1 coquille corrigée |
| 6 | C0168 | 575–6 | (sans lemme) | CRITIQUE (suppression de vers proposée par d'autres critiques ; l'auteur garde les vers et renvoie à la note 17 de Willems) | déplacé en entier dans `critique.tex` (`\cc{575–6}`, lemme vide), inchangé |
| 7 | C0169 | 578 | ὀλίγῳ τι πρότερον κατ᾽ ἀγορὰν λαλούμενον | PIÈCE (dramaturgie : d'où vient la fuite ? pas d'Euripide ; vanité des hypothèses des commentateurs) | reste dans `commentaire.tex` ; 1 « nous » → « je » ; 2 coquilles corrigées |
| 8 | C0170 | 579–87 | ἥκω φράσων… | PIÈCE (style paratragique de Clisthène : redoublements eschyléens, *Grenouilles* 1153 sqq.) | reste dans `commentaire.tex`, inchangé |
| 9 | C0171 | 582–3 | τί δ᾽ ἔστιν ὦ παῖ; … ψιλὰς ἔχῃς | PIÈCE (parallèle : *Guêpes* 1297–1298) | reste dans `commentaire.tex`, inchangé |
| 10 | C0172 | 585 | ἀναπέμψαι | PIÈCE (topographie : le Thesmophorion sur la Pnyx ; cf. v. 658) | reste dans `commentaire.tex`, inchangé |

## « nous » d'auteur changés en « je »

- 556–7 (désormais dans `critique.tex`) : « c'est donc à nous que revient la tâche » → « c'est donc à
  moi que revient la tâche » (l'auteur enchaîne : « Muses, venez m'aider… je ne peux même pas… »).
- 558–9 : « Nous ne nous attarderons pas sur ce que pouvaient bien procurer les procureuses… » →
  « Je ne m'attarderai pas sur ce que… » (l'auteur choisit ce dont il traite ; même parti qu'en
  f162v pour « Nous nous efforcerons »).
- 578 : « voilà bien des détails sans importance sur lesquels Aristophane n'a pas daigné s'arrêter ;
  nous aurions fait de même si les professeurs… » → « j'aurais fait de même… » (l'auteur s'oppose aux
  professeurs).

« nous » conservés, parce qu'ils associent le lecteur, sont génériques ou appartiennent à une
citation :
- impératifs de la 1re personne du pluriel : « Attelons-nous y donc ! » (556–7, `critique.tex`) ;
  « Profitons-en pour remarquer », « Reconnaissons tout d'abord », « profitons-en donc pour
  suggérer », « Refermons cette parenthèse et retournons à notre coupe » (556–7, `commentaire.tex`) ;
  « Contentons-nous de renvoyer » (558–9, note 1) ; « Signalons » (570, note 2) ;
- « nous » génériques ou inclusifs : « c'est Euripide lui-même qui nous donnera la clef »,
  « dans notre pièce », « dans nos langues modernes » (556–7 et 569, `critique.tex`) ; « Pline nous
  confirme » (556–7) ; « notre *bouc-émissaire* », « notre chat », « Nous en sommes à Carcinos &
  Fils » (on suit le passage de la *Paix*), « Le scholiaste nous est ici précieux », « ne nous ait
  pas conservé », « notre Carcinos » (558–9) ; « nous a d'ailleurs été transmis », « nous a
  conservé » (568, d'après Willems) ; « nous apprend », « nous rapporte », « l'essentiel nous
  échappe encore », « que nous allons voir » (570) ; « il nous l'aurait fait comprendre » (578) ;
- dans les citations : « nous saisissons… nous siphonnons » (556–7, traduction du vers).

## Coquilles corrigées

- 556–7 (`critique.tex`) : « Aristote a dit un jour (`\italique{Tropiques}`,145a24) » →
  « (`\italique{Topiques}`, 145a24) » (titre ; espace après la virgule). Contrôlé sur le corpus
  local : Arist. *Top.* 6, 6 (145a), τῇ δὲ στλεγγίδι κἂν ἀρύσαιτό τις· ἀλλ᾿ ὅμως εἴ τις ὁρίσαιτο τὴν
  στλεγγίδα ὄργανον πρὸς τὸ ἀρύειν, ἡμάρτηκεν, la phrase que cite l'auteur.
- 556–7 (`commentaire.tex`) : « le détournement à fin lubrique du strigile se retrouve illustrée » →
  « illustré » (accord avec « détournement »).
- 556–7, note (coupe d'Onésimos) : « En parcourant le livre de Boardmann » → « Boardman » (graphie de la
  même note, « John Boardman »).
- 556–7, même note : « Refermons cette parenthèses » → « cette parenthèse ».
- 556–7, même note : « (notamment lorsqu'elle provenaient de virils athlètes) » → « lorsqu'elles
  provenaient » (les raclures).
- 558–9 (citation de La Fontaine, *Fables* VIII, 2) : « Il eut pour hôte les soucis » → « Il eut
  pour hôtes les soucis » (contrôlé sur Wikisource, éd. Bernardin-Béchet 1874 : « Il eut pour hôtes
  les soucis, / Les soupçons, les alarmes vaines »).
- 558–9, note 4 : « la belette (γαλῆ) est accusé d'avoir étranglé » → « est accusée ».
- 568 (vers d'Hipponax) : « λάβετε μευ ταἰμάτια […], κόψω Βουπάλου τον οφθαλμόν » → « λάβετέ μευ […]
  τὸν ὀφθαλμόν » (accent d'enclise ; accents et esprit omis : 2 corrections). Contrôlé sur Suid.
  β 452 (corpus local) : « λάβετέ μου θοιμάτιον, κόψω Βουπάλου τὸν ὀφθαλμόν ». Les formes ioniennes
  μευ et ταἰμάτια de l'auteur sont gardées.
- 569 (`critique.tex`) : « au vers 1669 des *Phéniciennes* » → « au vers 1699 » (chiffre erroné).
  Contrôlé sur le corpus local (Perseus) : Eur. *Phoen.* 1699 πρόσθες τυφλὴν χεῖρ᾽ ἐπὶ πρόσωπα
  δυστυχῆ. Le v. 1669 (ἀλλ᾽ ἀμφὶ τραύματ᾽ ἄγρια τελαμῶνας βαλεῖν) ne convient pas.
- 570, note 4 : « Érasme l'a recensé (*Adages* n° 677) » → « … n° 677). » (point final omis ;
  les autres notes en ont un).
- 578 : « introduit chez les femmes pou plaider sa cause » → « pour plaider ».
- 578 : « 1° Si Aristophane, l'avait imaginé ainsi » → « Si Aristophane l'avait imaginé ainsi »
  (virgule entre le sujet et le verbe).

## Passages signalés

### Par article

- 556–7, lemme « ὡς τλεγγίδας » (dans `critique.tex` et dans `commentaire.tex`) : ce n'est pas une
  coquille de l'auteur. R n'écrit qu'un σ, ὡστλεγγίδας (l. 6, contrôlé sur l'image ; Velsen 1883,
  p. 41 : « ὡς στλεγγίδας] ὡστλεγγίδας R »), et la Juntine imprime τλεγγίδας (Enger 1844, p. 101).
  Le texte établi porte ὡς στλεγγίδας. Lemme laissé tel quel.
- 556–7 (`critique.tex`) : l'article ne dit rien de Pollux VI 19, qui cite σιφωνίζειν chez
  Aristophane parmi les mots du vin qu'on puise. Fritzsche, Enger 1844 (p. 101) et Velsen 1883
  (p. 41) l'allèguent pour οἶνον. L'auteur le connaissait (testimonia de 557, mis en commentaire
  dans la source). Argument à discuter dans l'article critique ; rien n'a été ajouté.
- 556–7, note sur la coupe d'Onésimos : « (Le lecteur pourra la retrouver aux annexes de ce
  livre.) » renvoie aux annexes de l'édition de 2023 (`latex/Aristophane-Thesmo Annexes.tex`,
  « Coupe d'Onésime », l. 931 sqq.). Ce renvoi devient obsolète si l'annexe n'est pas reprise.
- Graphies flottantes, non harmonisées : « Mika » (556–7) / « Mica » (570, deux fois) ; le texte
  et la traduction portent Mika. « Onésimos » / « Onésime » (556–7).
- 558–9, lemme « ὥς τ᾽ αὐτὰ » : c'est la leçon de R (apparat de l'auteur : « ὥς τ᾽ αὐτὰ R : ὥς ταῦτα
  M : ὥς τ᾽ αὖ τὰ Zanetti »). Le texte établi porte ὥς τ᾽ αὖ τὰ. L'article ne discute pas le texte ;
  lemme laissé tel quel.
- 569 (`critique.tex`), « dans la 16e note reproduite à la fin » : c'est la note 16 de Willems, dans
  les annexes de 2023 (`Annexes.tex`, « Note 16 aux *Thesmophories* : vers 569 »). Renvoi à
  adapter si ces notes ne sont pas reproduites dans la nouvelle édition.
- 569, note : « le fragment 309(277) (éd. K.-A. = *Zonarae lexikon* p.1168) » n'est pas
  d'Aristophane, contrairement à ce que laisse croire une liste d'exemples aristophaniens. Il est de
  Cratinos : Kock I, p. 95, fr. 277, d'après Zonaras p. 1168 (« Κρατῖνος· τὴν χεῖρα… κάθῃ »),
  soit Cratin. fr. 309 K.-A. [numéro K.-A. à vérifier]. Le nom du poète manque ; non modifié.
- 569 : πρόσιθι est attribué à Cobet. Seule source contrôlée : la note 16 de Willems (« Cobet
  propose πρόσιθι »). Ni Enger 1844 ni Velsen 1883 (répertoire critique) n'ont d'entrée pour cette
  conjecture [à vérifier dans une seconde source, CONVENTIONS § 2.4]. Le lemme (πρόσθες, leçon de R)
  diffère du texte établi (πρόσθιγε, Willems) : c'est normal pour un article critique.
- 570 : « le gâteau de sésame par toi engueulé ». L'article écrit deux fois « engoulé » plus haut :
  probable coquille pour « engoulé », à moins d'un jeu de mots voulu. Non modifié.
- 575–6 (`critique.tex`) : « voir la note de Willems n° 17 » renvoie aux annexes de 2023 (même
  remarque que pour 569). « ces deux vers que d'aucuns auraient voulu biffer » : selon cette note
  et selon Velsen 1883 (p. 43 : « v. 575 versum spurium esse intellexit Cobetus », vers mis entre
  crochets), Cobet, suivi de van Leeuwen, ne supprime que le v. 575. Enger 1844 (p. 105) signale en
  outre une transposition de Fritzsche (ὅτι μὲν φίλος ὑμῖν, εἴμ᾽ ἐπίδηλος). Non modifié.
- 578 : « les professeurs parmi les plus admis » : sens douteux (« admirés » ?). Non modifié.
- 585 : « Le suffixe `ἀνα' » : ἀνα- est un préfixe (préverbe). C'est une question de terme, pas une
  faute de frappe ; non modifié. (Le v. 658 cité porte τὴν Πύκνα ; cf. aussi ἀνελήλυθε au v. 657.)

Références contrôlées sur le corpus local, sans écart : *Guêpes* 363–364, 408, 627, 1297–1298 ;
*Paix* 1150–1152 ; *Nuées* 506–508, 933, 1044–1046 ; *Lys.* 365, 435–436, 440 ; *Eccl.* 1059–1062 ;
*Ach.* 350–351 ; *Ois.* 65–68 ; *Gren.* 1153–1157 ; Eur. *Ion* 300 ; Suid. β 452, ο 680, π 3192 ;
Athénée I 4d, XIV 645e et 647a ; Pollux VII 199 (Ar. fr. 265 Kock, *Danaïdes*).

### Passages entourés de `\eff` (orange) dans la source

Le texte courant des articles de ce folio n'en contient aucun. Il y en a trois dans des passages
mis en commentaire (`%`) par l'auteur. Ils sont absents de la conversion comme du livre de 2023, et
n'ont pas été rétablis :
- l. 4043 (556–7, note 3 d'une première version, abandonnée, de la conjecture : τὴν μᾶζαν, glosé τὸν
  σῖτον) : « fragment 28 de l'édition Kassel-Austin ; se reporter aux notes du 6e fragment pour
  l'éclaircissement. \eff{Et chez Masson ?} » (sur Hipponax).
- l. 4128–4129 (article 563 abandonné, sur Ἀχαρνικὴ) : « \eff{Une charbonnière ? qui aura charbonné
  son mari père ? Ou alors : après la hache et le poison, reste la corde (kat)ἀρτῶ à la place de
  katwrucen Τὰ τρία τῶν εἰς θάνατον .} ». Suivent des notes sur κατώρης et la porte d'Acharnes.
  C'est une idée textuelle sur les vv. 562–563 (un verbe de pendaison pour κατώρυξεν) ; si l'auteur
  la reprend, elle ira au commentaire critique.
- l. 4228–4237 (570, développement abandonné sur Athénée XIV 645e, Ar. fr. 269 des *Danaïdes*) :
  conjectures κάθαρμα pour μήτ᾽ αρμα et (συρ)μαιοπώλην pour καὶ ποιητήν, avec les notes 5–6, elles
  aussi en commentaire (Thompson, *Handbook* ; Louyest, *Rursus* 8, 2012). Il s'agit du texte
  d'Athénée, non de celui des *Thesmophories*.

Autres passages en commentaire dans la source, sans `\eff`, non rétablis : l. 4027–4036 (556–7 :
première version de la conjecture, τὴν μᾶζαν ; parenthèse contre Henderson ; *Plutus* 1036–1037 et le
proverbe διὰ δακτυλίου) ; l. 4261–4262 (575–6 : suite sur les « vols d'émendations » dénoncés dans
les notes de bas de page de Willems) ; l. 4294 (586 : « Vers paratragique. ») ; l. 6527 (558, dans
la traduction : renvoi à la note sur la *Paix*, v. 893).

### Composition (défaut commun, hors du périmètre du folio)

Une note `\nc` placée à l'intérieur de `\citComm{…}` disparaît du PDF : son appel est imprimé, mais
ni son texte ni son numéro ne survivent. La cause : `\citComm` (`edition/thesmo-compat.sty`, l. 5)
compose son argument dans un groupe, et `\nc` (`edition/thesmo.cls`, l. 671 sqq.) incrémente le
compteur et ajoute la note par des affectations locales (`\int_incr:N`, `\tl_put_right:Nx`), perdues
à la sortie du groupe. Sur ce folio, deux cas :
- 556–7 (`critique.tex`) : la note « Platon, *Gorgias* 494e. » manque ;
- 558–9 : la note sur *Le Savetier et le Financier* manque, et la note suivante (Μῦες) reçoit le
  même numéro 3.

Le texte des notes est bien dans les sources. On trouve la même construction en f163r, f164r,
f164v, f170r, f172v, f175r et f176v. Correction à faire dans la classe : affectations globales dans
`\nc` et `\thesmo_flush_cnotes:`, ou `\citComm` sans groupe. Elle n'a pas été faite ici parce que
ces fichiers sont communs à tous les folios.
