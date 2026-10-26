# f166r (vv. 294–336) — répartition commentaire critique / commentaire de la pièce

Source : `commentaire.tex` (conversion automatique de `latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex`, l. 2718–2864).
Articles critiques déplacés dans `critique.tex` (`\cc`) ; articles de la pièce laissés dans `commentaire.tex` (`\comm`) ; articles mixtes scindés.
Texte et notes conservés mot pour mot, sauf les corrections listées ci-dessous. Original sauvegardé dans `.travail/f166r/commentaire.orig.tex`.

**État** : terminé. 5 articles : 0 CRITIQUE, 2 MIXTE (312–30, 336–7 : scindés), 3 PIÈCE (295–311, 307–8, 330). `critique.tex` compte 2 articles `\cc`, `commentaire.tex` 5 articles `\comm` (dont les 2 restes de scission). Le folio compile (`./edition/compiler_folio.sh f166r` : 5 pages). `.travail/f166r/controle.py` vérifie que `commentaire.tex` et `critique.tex` redonnent exactement l'original, aux corrections, renvois et adaptations déclarés près.

Reprise : une première exécution, arrêtée vers 16 h 11 avant la fin du compte rendu, avait classé les articles, fait les scissions et les corrections. J'ai contrôlé ce travail (comparaison avec l'original, compilation) sans rien déplacer de nouveau. J'ai ajouté le renvoi en tête de `\cc{336–7}` (voir « Adaptations ») et complété le présent compte rendu.

## Articles

| plage | lemme (abrégé) | classement | action |
|---|---|---|---|
| 295–311 | (sans lemme) | PIÈCE (prière en prose, d'après la scholie ; parallèle des *Oiseaux* 864–888) | reste dans `commentaire.tex` ; coquille corrigée |
| 307–8 | τὸν δῆμον τῶν Ἀθηναίων… | PIÈCE (plaisanterie παρὰ προσδοκίαν) | reste dans `commentaire.tex` |
| 312–30 | Chant du chœur. | MIXTE : colométrie (refrain énoplien de Parker aux vv. 315, 320, 325 ; choix de la colométrie de Prato, « plus proche du manuscrit de Ravenne ») / contenu du chant (citation de Prato sur les divinités invoquées) | scindé : Parker et le choix de la colométrie, avec les deux notes `\nc`, dans `critique.tex` ; la citation de Prato reste dans `commentaire.tex`, précédée du renvoi « Pour la métrique et la colométrie, voir le commentaire critique. » ; coquille corrigée |
| 330 | εὐγενεῖς γυναῖκες. | PIÈCE (realia : seules les citoyennes assistent aux Thesmophories ; renvoi au v. 294) | reste dans `commentaire.tex` |
| 336–7 | ἢ 'πικηρυκεύεται / Εὐριπίδῃ Μήδοις… | MIXTE : parodie des imprécations de l'ecclésie contre les Mèdes (Isocrate, *Panég.* 157), Euripide en ennemi héréditaire / Μήδοις suspect d'interpolation, témoignage de P.Oxy. IX 1176 (Satyros), τ᾽ de Biset | scindé : Isocrate et la substitution comique restent dans `commentaire.tex`, précédés de « Pour le texte, voir le commentaire critique. » ; de « Remplacé ? pas tout-à-fait… » à la fin, avec les quatre notes `\nc`, dans `critique.tex` ; deux coquilles corrigées |

## Coquilles corrigées

- 295–311 : scholie citée, « χρῶντα οἱ κωμικοὶ » → « χρῶνται οἱ κωμικοὶ » (contrôlé dans Dübner, *Scholia graeca in Aristophanem*, 1842, schol. *Thesm.* 295 : πεζῇ εὐφημίᾳ χρῶνται οἱ κωμικοὶ, ἐπειδὰν εὐχὴν ἢ ψήφισμα εἰσάγωσιν ; `.sources/web/scholies/scholiagraecain00unkngoog_djvu.txt`). L'accent grave devant la virgule (κωμικοὶ,) est celui de Dübner : conservé.
- 312–30 : citation de Prato, « dell' ecclesia » → « dell'ecclesia » (espace parasite après l'apostrophe ; texte de Prato non contrôlé).
- 336–7 : traduction d'Isocrate, « des imprécations coutre celui des citoyens » → « contre celui des citoyens ».
- 336–7, note 1 : « ed. Arthur S. Dunt » → « ed. Arthur S. Hunt ». Le volume IX des *Oxyrhynchus Papyri* (1912) est « edited with translations and notes by Arthur S. Hunt » (page de titre, `.sources/web/papyrus/POxy_IX/`). L'article lui-même nomme Hunt, et la note jumelle de l'auteur à l'art. 373 (`f166v/commentaire.tex` ; source, l. 3028) porte « ed. Arthur S. Hunt ».

## Adaptations imposées par les scissions

- 312–30 : dans la source, la citation de Prato est introduite par un deux-points (« … plus proche du manuscrit de Ravenne : «~Il Coro accoglie… » »). La scission la détache : l'article critique finit donc par un point (« … plus proche du manuscrit de Ravenne. ») et la citation, dans `commentaire.tex`, suit le renvoi. Le renvoi dit « la métrique et la colométrie » plutôt que « le texte », puisque c'est ce qui est passé au commentaire critique.
- 336–7 : au commentaire, le renvoi « Pour le texte, voir le commentaire critique. » est en tête de l'article (Isocrate, puis « L'ennemi héréditaire… est remplacé… par Euripide. »). L'article critique commence à « Remplacé ? pas tout-à-fait », dont l'antécédent est resté au commentaire. Je l'ai donc fait précéder du renvoi « Sur la substitution d'Euripide aux Mèdes, voir le commentaire de la pièce. », comme pour f171v (782) et f172v (839). Le texte de l'auteur n'est pas modifié.

## « nous » d'auteur changés en « je »

Aucun. L'auteur dit déjà « je » (312–30 : « j'ai préféré pour ma part » ; 336–7, note 1 : « Je me réfère aussi »). Je conserve :
- 336–7 : « Or nous possédons un papyrus d'Oxyrhynque » et « le vers qui nous intéresse » (nous inclusif : l'auteur, le lecteur, les philologues) ;
- 336–7, note 2 : « notre manuscrit de Ravenne » (le manuscrit commun à l'édition et au lecteur ; cf. « notre unicodex », conservé en f165r) ;
- 336–7 : « Nos pères… dans nos assemblées » : c'est la traduction d'Isocrate, non l'auteur.

## Passages signalés

### Passage marqué `\eff` (orange) dans la source

Un seul, dans des lignes que l'auteur a mises en commentaire (`%`). La conversion ne l'a pas repris et je ne l'ai pas réintroduit. Il s'agit de la conjecture de Bibi au v. 337, qui prolonge l'article 336–7 après « …Μήδοις τ᾽ » (source, l. 2852–2858) :
- « La lecture probable d'un υ avant le τ laisse à penser qu'il faut compléter ainsi la lacune : [τα]ῦτ᾽. Il suffit alors de faire la simple hypothèse de la chute d'un êta -- je la fais : ευριπιδ<η>ι pour que le passage devienne intelligible ». Suivent la restitution du papyrus (ηεπικη|ρυκευετ[αι]ευρι|πιδ<η>ιωι̣[τα]υ̣τ|επιβλαβηι̣τι|νι [τῇ τῶν γυναικῶν]), le texte proposé (« ἢ 'πικηρυκεύεται / Εὐριπίδῃ ᾧ ou bien ws ταῦτ᾽ ἐπὶ βλάβῃ τινὶ / τῇ τῶν γυναικῶν »), une traduction (« ou s'il envoie un ambassadeur à Euripide qui [utilise] ces informations au détriment des femmes ») et la remarque « (Avec le redoublement Εὐριπίδῃ / ᾧ repris plus loin avec τινὶ / τῇ ; pastiche du style de la procédure ecclésiastique.) ».
- Ce passage va avec la note 5, elle aussi en commentaire (l. 2864) : ταῦτ᾽ ἐπικηρυκεύομαι au v. 1163 et trois passages d'Hérodote, et avec la fin, en commentaire, de la ligne d'apparat (l. 2841) : « Εὐριπίδῃ ᾧ ταῦτ᾽ Bibi ». Le texte établi garde les obèles : †Εὐριπίδῃ Μήδοις τ᾽† (`f166v/texte.tex`).
- J'ai contrôlé les références de la note 5 dans le corpus (Perseus). *Thesm.* 1163 (κακὸν τὸ λοιπόν. ταῦτ᾽ ἐπικηρυκεύομαι) est exact, de même qu'Hdt. IV 80 (ταῦτά οἱ πέμψας ὁ Σιτάλκης ἐπεκηρυκεύετο) et VI 97 (ταῦτα μὲν ἐπεκηρυκεύσατο τοῖσι Δηλίοισι). En revanche, « ταῦτα δι᾽ ἀγγέλων ἐπεκηρυκεύετο » est en **I 69**, 3 et non en I 60. Si l'auteur reprend la note, il faut aussi lire « conclut » pour « conclue » (« lorsqu'Euripide conclue la paix »).
- Ce passage déciderait de l'article critique 336–7 (la lacune du papyrus, puis la conjecture) : à l'auteur de dire s'il le réintroduit.

### Autres passages mis en commentaire (`%`) par l'auteur, non repris (pour mémoire)

- 336–7 (l. 2847) : « (Plutôt que d'une plaisanterie παρὰ προσδοκίαν, l'on devrait plus proprement parler d'une plaisanterie μετὰ προσδοκίας.) », après « …le trait comique... ».
- 336–7 (l. 2848) : « Interpolation, alors ? c'est ce que nous allons pouvoir essayer de montrer grâce à un papyrus d'Oxyrhynque ! ».
- 295 (l. 2716) : l'apparat de l'auteur sur le personnage qui parle, mis en commentaire : `\inRas{Κῆρυξ}{} \Rdeux : \auDessus{κη}{ρυ} \Mon : γυνὴ μιμουμένη κήρυκα Σ : Κρίτυλλα Sommerstein` (Κῆρυξ barré, R² ; κη surmonté de ρυ, M). Aucun article critique de ce folio ne traite de l'attribution de 295–311 (« coryphée-prêtresse » dans l'art. 295–311 ; ΚΟ. dans `texte.tex`). Sur Critylla prêtresse, voir f171r, art. 759.

### Lemmes et texte établi (à harmoniser ; je n'ai rien changé)

- 307–8 : le lemme porte « τῶν Ἀθηναίων », leçon de R (lu sur l'image du f. 166r : τὸν δῆμον τῶν ἀθηναί(ων)) ; le texte établi (`texte.tex`) imprime τὸν Ἀθηναίων (Grynaeus, selon l'apparat de la source). Aucun article critique ne traite ce lieu.
- 336–7 : le lemme porte la leçon de R (Εὐριπίδῃ Μήδοις, sans τ᾽). Le texte établi imprime †Εὐριπίδῃ Μήδοις τ᾽† (`f166v/texte.tex`, v. 337), avec le τ᾽ de Biset et les obèles, conformément à l'article critique (Μήδοις suspect d'interpolation).

### Références à vérifier ou à compléter (non modifiées)

- 336–7, note 1 : « Stefan Schorn, *Satyros aus Kallatis* (2002) ». `recherche/papyrus.md` date ce livre de 2004 (Basel, Schwabe), d'après la bibliographie du DCLP (de seconde main) *[à vérifier]*.
- 336–7 : la transcription du papyrus (ευριπιδιωι̣[. .]υ̣τ|επιβλαβηι̣τι|νι) n'est pas celle de Hunt (P.Oxy. IX, p. 155 : ευρι|πιδιω[. . .] . τ) ; d'après les notes 3 et 1, elle vient sans doute de Schorn. La remarque de Hunt sur laquelle s'appuie l'article est exacte : « there is not room for Μήδοις between ι and τ » (p. 178, contrôlé dans `.sources/web/papyrus/POxy_IX/` ; voir aussi `recherche/papyrus.md`, § 3.4). Schorn n'est pas consultable dans `.sources/` : lecture à contrôler sur l'image du papyrus.
- 336–7, note 2 : R daté « IXe ou Xe s. » ; `edition/CONVENTIONS.md` (§ 2.3) dit « milieu du Xe s. ». À harmoniser avec l'introduction et l'étude graphologique.
- 312–30, note 1 : Parker, *The Songs of Aristophanes* (1997), « pp. 406-409 » : livre absent de `.sources/`, pages non contrôlées. La citation de Prato n'a pas de page (Prato 2001, commentaire aux vv. 312–330 ?) ; le commentaire n'est pas dans l'extrait local (`.sources/drive/textes_metrique/Prato_2001_LeDonAllTes_readcontent.txt`) *[à compléter]*.
- Contrôlés et exacts : Isocrate, *Panég.* 157 (texte grec cité identique à celui de Perseus, `tlg0010.tlg011`) ; *Oiseaux* 864–888 (la prière du prêtre commence au v. 865, après le v. 864, δράσω τάδ᾽…, qui l'introduit).
- 336–7 : la traduction d'Isocrate, sans nom de traducteur, rend Πέρσαις par « aux Mèdes ». Je la laisse telle quelle.

### Moteur LaTeX (défaut préexistant, non corrigé)

- Le `\nc` placé à l'intérieur de `\citComm` (note 3 de l'art. 336–7 : « Schorn indique que la présence d'un c est moins probable… », appelée sur le υ douteux) est perdu à la composition : la note manque dans le PDF et l'appel suivant (Μήδοις τ᾽) porte lui aussi le numéro 3. Le défaut, déjà décrit en f165r (art. 241–2), tient au moteur partagé : `\nc` fait des affectations locales et `\citComm` ouvre un groupe. La correction proposée est la même qu'en f165r : `\int_gincr:N` et `\tl_gput_right:Nx` dans `\nc`, remise à zéro globale dans `\thesmo_flush_cnotes:`. Je n'ai pas touché `edition/thesmo.cls` ; c'est à l'orchestrateur de décider.
- Dépassements cosmétiques : 2,1 pt sur la première ligne de `\cc{312–30}` (colonne étroite du commentaire critique) ; 1,8 pt sur l'art. 330 du commentaire (déjà présent avant la répartition).

### Graphies à revoir (non corrigées : usage ou style, non frappe)

- 336–7 : « pas tout-à-fait » (→ tout à fait).
- 312–30 : « \italique{The Songs of Aristophanes} » dans le texte, « \italique{The songs of Aristophanes} » dans la note 1.
