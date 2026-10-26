# f167r (vv. 380–422) — répartition commentaire critique / commentaire de la pièce

Source : `edition/folios/f167r/commentaire.tex`, conversion automatique de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` (l. 3061–3193 ; articles C0114–C0124
de `edition/donnees/travaux_anterieurs/commentaires.tsv`). Copie de l'état initial :
`.travail/f167r/commentaire_original.tex`.
Résultat : `critique.tex` (macros `\cc`) et `commentaire.tex` (macros `\comm`).

Classement : **CRITIQUE** (discussion du texte), **PIÈCE** (interprétation, langue,
realia, mise en scène, parodie…), **MIXTE** (scindé).

**État** : terminé (11 articles traités). Contrôle automatique : une fois remises bout à bout
(sans le renvoi), les parties de `critique.tex` et de `commentaire.tex` redonnent le texte
initial, aux corrections listées près. `./edition/compiler_folio.sh f167r` : OK, 7 pages, sans
erreur. Il reste une boîte trop pleine de 5,5 pt, sur la ligne « … Diogène Laërce\nc{…} : » de
l'art. 401–4 ; elle existait déjà avant la correction.

**Récapitulatif** : 11 articles. On compte 2 CRITIQUES (400, 418–20), 1 MIXTE (393) et 8 PIÈCE.
`critique.tex` contient 3 articles (393, 400, 418–20), dans l'ordre des vers.

## Articles

| # | id | plage | lemme (abrégé) | classement | action |
|---|---|---|---|---|---|
| 1 | C0114 | 381 | χρέμπτεται | PIÈCE (langue : « tousser » et non « cracher » ; note de Willems, d'Aubigné) | reste dans `commentaire.tex`, inchangé |
| 2 | C0115 | 393 | τὰς οἰνοπίπας | MIXTE (leçon : οἰνοπίπας de la tradition indirecte contre οἰνοπότιδας de R, d'après la scholie et le sens de -οπίπης / ὀπιπεύειν ; puis thème du vin dans la pièce) | scindé : le 1er alinéa (scholie, Symmaque, rapprochement avec παιδοπίπης, ὀπιπεύειν, Hésychius) → `critique.tex` (`\cc{393}`) ; la dernière phrase (« Aristophane ne va pas manquer de surenchérir… ») reste dans `commentaire.tex`, précédée du renvoi |
| 3 | C0116 | 394 | τὰς οὐδὲν ὑγιές | PIÈCE (proverbe : Érasme, *Adages*) | reste dans `commentaire.tex`, inchangé |
| 4 | C0117 | 400 | τοὺς ἄνδρας ἡμῶν· ὥστ᾽ ἐάν τις πλέκῃ | CRITIQUE (mètre ; supplément ξυμπλέκῃ de Willems, adopté dans le texte) | déplacé dans `critique.tex` (`\cc{400}`), inchangé |
| 5 | C0118 | 400–1 | ὥστ᾽ ἐάν τις πλέκῃ / γυνὴ στέφανον… | PIÈCE (realia : couronnes tressées pour l'être aimé ; scholie citant Sappho, Athénée) | reste dans `commentaire.tex`, inchangé ; la note (texte corrompu de la citation de Sappho dans la scholie, lecture de l'auteur) touche au texte de la scholie, non à celui d'Aristophane : laissée à son appel (voir les signalements) |
| 6 | C0119 | 401–4 | κἂν ἐκβάλῃ … τῷ Κορινθίῳ ξένῳ | PIÈCE (paratragédie : *Sthénébée* d'Euripide, fr. 664 Kannicht ; Aristophane, *Héros*, fr. 320 K.-A., chez Diogène Laërce) | reste dans `commentaire.tex` (2 notes) ; 1 coquille corrigée |
| 7 | C0120 | 405–6 | εὐθὺς ἁδελφὸς λέγει… | PIÈCE (interprétation ; paratragédie : citation d'une pièce d'Euripide non identifiée, l'absence de résolution au v. 406 servant d'indice, non d'argument textuel) | reste dans `commentaire.tex`, inchangé |
| 8 | C0121 | 406–7 | γυνή τις ὑποβαλέσθαι βούλεται… | PIÈCE (thème de la supposition d'enfants ; Satyros, *Vie d'Euripide* ; *Phén.* 28–31, *Alc.* 639) | reste dans `commentaire.tex` (2 notes) ; 5 coquilles corrigées ; plage fautive signalée |
| 9 | C0122 | 413 | δέσποινα γὰρ γέροντι νυμφίῳ γυνή | PIÈCE (paratragédie : source du vers, Euripide, *Phénix*, fr. 804 Kannicht, chez Stobée ; maxime française) | reste dans `commentaire.tex` (1 note) ; 1 coquille corrigée |
| 10 | C0123 | 416–7 | Μολοττικοὺς / τρέφουσι μορμολυκεῖα… | PIÈCE (paratragédie : *Hippolyte* 645–648 ; note de Willems) | reste dans `commentaire.tex`, inchangé |
| 11 | C0124 | 418–20 | ἃ δ᾽ ἦν ἡμῖν πρὸ τοῦ… | CRITIQUE (v. 419 : conjecture λαθεῖν de Scaliger rejetée, renvoi à la note 12 de Willems) | déplacé dans `critique.tex` (`\cc{418–20}`), inchangé |

## « nous » d'auteur changés en « je »

Aucun : la plage ne contient pas de « nous » d'auteur. L'auteur parle déjà à la première personne
du singulier : 400–1, note (« La lecture proposée est de mon cru ») ; 413, note (« Je reprends leur
traduction ») ; 418–20 (« Je renvoie… », désormais dans `critique.tex`).

« nous » conservés (tous généraux : la postérité, les lecteurs, les philologues) :
- 393 (désormais dans `critique.tex`) : « c'est le scholiaste […] qui **nous** permet de revenir à
  la leçon originale ». Comme « Le scholiaste nous met sur la piste » (f162v), le « nous » associe
  le lecteur à l'éditeur ; à changer en « me » si l'auteur l'entend de lui seul.
- 401–4 : « Athénée (X, 427e) **nous** a conservé ce fragment ».
- 406–7 : « La tradition ne **nous** a rapporté qu'une seule supposition d'enfants chez Euripide ».
- 413 : « Stobée (IV, 22a109) **nous** a conservé la fameuse citation d'Euripide ».

## Coquilles corrigées

- 401–4 : « rapporté par Diogène **Laërte** » → « Diogène **Laërce** ». Graphie isolée : partout
  ailleurs dans les fichiers de l'auteur, « Laërce » (`latex/Aristophane-Thesmo Harmattan 2023 vv
  642-fin-bis.tex`, note de Fustel de Coulanges) ; la référence elle-même (D. L. VIII 34) est exacte
  (contrôlée sur le texte Perseus du corpus local).
- 406–7, citation de Satyros : « τὰ συνέχοντα τα τὴν νεωτέραν κωμῳδίαν » → « τὰ συνέχοντα τὴν
  νεωτέραν κωμῳδίαν ». Le « τα » est une dittographie née de la coupe de ligne du papyrus
  (συνέχον|τα τὴν) ; contrôlé sur l'*editio princeps* (*P. Oxy.* IX, 1912, n° 1176, fr. 39,
  col. vii, texte et traduction de Hunt, OCR archive.org `oxyrhynchuspapyr09gren`).
- 406–7, même citation : « Εὐρπίδης » → « Εὐριπίδης » (même contrôle).
- 406–7, note 2 : « *The Oxyrhynchus Papyri*, IX.1776 » → « IX.1176 ». Le tome IX ne contient
  pas de n° 1776, et l'auteur cite ailleurs ce papyrus sous le bon numéro
  (`latex/Aristophane-Thesmo Introduction.tex`, l. 379 : « IX n° 1176, fr. 39 » ; version de
  nov. 2022, l. 2467 et 2627). Contrôlé sur l'*editio princeps* (même source).
- 406–7, traduction de Satyros : « éléments qu'Euripide avait conduit au sommet » →
  « … avait conduits au sommet » (accord du participe avec le COD antéposé).
- 406–7, note 1 : « font passer pour leur des enfants » → « font passer pour leurs des
  enfants » (accord).
- 413, citation d'Euripide : « δέςποινα γὰρ γέροντι νυμφίῳ γυνή » → « δέσποινα… » (sigma final
  au milieu du mot ; le même vers est le v. 413 du texte établi).

Les deux corrections d'accord de 406–7 (« conduits », « leurs ») relèvent de la grammaire
plutôt que de la frappe : à rétablir si l'auteur le souhaite.

## Passages signalés

### Passages entourés de `\eff` dans la source (marqués en orange par l'auteur)

Aucun dans la plage : les lignes de la source qui répondent à f167r (l. 3046–3200 de
`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`) n'en contiennent pas. Les plus proches
sont aux l. 2894 (f166v) et 3736.

### Passage mis en commentaire (`%`) par l'auteur

- 418–20, fin de l'article (source, l. 3195) : « % ; contre-sens pourtant encore repris par
  certains éditeurs modernes...) ». C'est la suite, abandonnée, de la parenthèse sur Scaliger. La
  conversion ne l'a pas reprise et je ne la réintroduis pas. Elle est exacte au moins pour
  Hall–Geldart, qui imprime λαθεῖν au v. 419 (`.sources/corpus/thesmo_hall_geldart.tsv`). D'après
  le répertoire critique (Enger 1844), Brunck voulait λαθεῖν et Bothe l'a imprimé.

### Plage et lemmes

- 406–7 : **plage fautive**. Le lemme (γυνή τις ὑποβαλέσθαι βούλεται / ἀποροῦσα παίδων…)
  correspond aux vv. **407–8**, aussi bien dans le texte établi (`texte.tex`) que chez
  Hall–Geldart. La plage est laissée telle quelle ; elle est à corriger en 407–8.
- 418–20 (critique) : le lemme porte ταμιεύεσθαι, leçon de R, alors que le texte établi imprime
  ταμιεῦσαι καὶ (Reiske). L'article ne discute que λαβεῖν / λαθεῖν. La correction de Reiske n'est
  justifiée que par le renvoi à la note 12 de Willems, qui l'approuve (`latex/Aristophane-Thesmo
  Annexes.tex`, « Note 12 aux *Thesmophories* : vers 418-420 »). Il faut donc harmoniser le
  lemme ou compléter l'article.
- 400 (critique) et 400–1 (pièce) : le lemme porte πλέκῃ (R), le texte établi ξυμπλέκῃ (Willems).
  C'est normal pour l'article critique. Pour l'article de la pièce, le lemme est à harmoniser si
  l'auteur le souhaite.

### Contrôles

- **R vérifié sur l'image** (f. 167r) pour les leçons que supposent les articles critiques :
  v. 393 οἰνοπότιδας ; v. 400 τις πλέκῃ ; v. 419 ταμιεύεσθαι … προαιρούσαις λαβεῖν ; aussi,
  v. 417 μυχοῖς. La scholie au v. 393, en marge droite, commence bien par ὁ Σύμμαχός φησι παρὰ
  τὸ πιπίζειν… Elle est conforme au résumé de l'article (texte de Dübner, p. 267 : ἄμεινον οὖν,
  ὥσπερ παιδοπίπης λέγεται, οὕτω καὶ οἰνοπίπης).
- Renvois aux notes 11 et 12 de Willems « reproduite[s] à la fin » : exacts (`latex/Aristophane-Thesmo
  Annexes.tex`, notes 11, vv. 400–401, et 12, vv. 418–420). Dans la note 12, il y a une coquille
  (« 4Mais qu'avons-nous… », chiffre parasite) ; ce fichier sort du champ de la tâche et je ne
  l'ai pas corrigé.
- Contrôlés sur le corpus local (textes Perseus et First1K) :
  - *Cavaliers* 407 (πυροπίπην) ;
  - Athénée X 427e (fragment de la *Sthénébée*) et le passage cité de XV 669d–670f ;
  - Eur. fr. 664 (*Sthénébée*) et fr. 804 (*Phénix*, transmis par Stobée : Meineke, *Flor.* 71, 1) ;
  - D. L. VIII 34 ; *Phén.* 28–31 ; *Alc.* 639 ; *Hipp.* 645–648 ;
  - renvois internes aux vv. 340, 502–516 et 564–565 ;
  - v. 406 sans résolution, comme le dit l'art. 405–6.
- **Non contrôlés** (sources absentes du corpus local) [à vérifier] :
  - 381 : D'Aubigné, *Avent. du baron de Foeneste*, « I. IV, ch. 10 » (citation de Willems ;
    « I. » est sans doute « l. », livre) ;
  - 393 : le numéro d'Hésychius, ο 1006 (Latte). Chez Schmidt, la glose se lit ὀπιπᾷ· ἐξαπατᾷ.
    ἀπατεών, ἢ ἀπατῶν (ὀπῖπα) ; l'article cite ὀπῖπα· ἐξαπατᾷ, ἀπατεών, ἢ ἀπατῶν ;
  - 394 : Érasme, *Adages*, n° 738 ;
  - 400–1 : Sappho fr. 70 Reinach–Puech et fr. 125 Voigt ;
  - 401–4 : fr. 3 Jouan–van Looy, fr. 883 Mette ; Ar. fr. 320 K.-A. (= 305 Kock) ;
  - 413 : « Stobée (IV, 22a109) » (numérotation de Hense), fr. 1139 Mette.

### Questions de fond

- 393 : depuis la scission, le sens de οἰνοπίπας (famille de ὀπιπεύειν, « guigner ») n'est plus
  expliqué que dans le commentaire critique. Or la traduction (« sujettes au vin ») rend plutôt
  οἰνοπότιδας, la leçon de R que l'article écarte. Il faut revoir la traduction, ou remettre une
  glose brève au commentaire de la pièce.
- 393 : selon le répertoire critique (Enger 1844), Dindorf gardait οἰνοπότιδας parce qu'il jugeait
  improbable un féminin en -πίπας chez Aristophane. L'article ne répond pas à cette objection. La
  forme imprimée, οἰνοπίπας, est d'ailleurs celle de la Souda. La scholie, elle, plaide pour
  οἰνοπίπης, puis ajoute (ἄλλως) τὰ πλεῖστα οἰνοπίπους ἔχει (apparat de l'auteur : « -πίπους
  Σ »).
- 400–1, note 1 : elle porte sur le texte de la scholie (citation corrompue de Sappho, lecture de
  l'auteur), non sur celui d'Aristophane ; je la laisse donc au commentaire de la pièce. La
  citation de la scholie imprime directement la lecture de l'auteur (αὐτὰ κόραις στεφαναπλόκεο).
  En outre, R semble porter, en marge gauche, στεφα|νηπλοκεῖν (ainsi Bergk), là où l'article
  imprime στεφανοπλοκεῖν (Dübner, Rutherford) [à vérifier sur l'image].
- 416–7 : le lemme porte μοιχοῖς, correction de M ; R a μυχοῖς. Aucun article ne discute cette
  correction, qui touche au sens.
- Plusieurs lieux de la plage ne sont traités que dans l'apparat de l'auteur, sans article
  critique :
  - attributions des vv. 380 et 383 (Μίκα, Rogers) ;
  - 386 ἡμᾶς (Cobet) ; 390 ἔμβραχυ (Souda) ; 392 μοιχοτρόπους, ἀνδρεραστρίας (Souda) ;
  - 398 ὧνπερ (Küster) ; 412 ἐθέλει (Kappeyne van de Coppello) ; 417 μοιχοῖς (M) ;
    419 ταμιεῦσαι καὶ (Reiske).

  L'auteur dira si certains méritent un article.
- `texte.tex` (hors du champ de la tâche) : v. 407 « εἶἑν » pour εἶεν. La faute est déjà dans la
  source (l. 3145) ; je ne l'ai pas corrigée.
