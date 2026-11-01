# Étiquettes métriques des parties récitées (vv. 1-1231) — section s00

*Chantier « métrique », section s00. Données : `edition/donnees/metrique/s00_etiquettes.json` (33 entrées). Rédigé le 28/10/2026 ; vérifié et mis à jour le 1/11/2026 (§ 9). Les références ont été lues sur les sources (§ 8). Les images de R ont été contrôlées pour 162 (f. 164r), 233 (f. 165r), 295-311 (f. 166r), 531 et 547 (f. 168v), 947-952 (f. 173v), 1222-1231 (f. 177r). Découpes et scripts : `.travail/metrique/s00/`.*

## 1. Objet et conventions

- **Une étiquette par passage récité**, stichique ou systématique, portée par sa première rangée de `texte.tex`, sans schéma (`schema` et `colon` vides). Étiquettes : **ia³** (trimètres iambiques), **ia⁴∧** (tétramètres iambiques catalectiques), **tr⁴∧** (tétramètres trochaïques catalectiques), **an⁴∧** (tétramètres anapestiques catalectiques), **an.** (système anapestique), **prose**. Aucune étiquette n'est répétée tant que le mètre ne change pas : `edition/CONVENTIONS.md`, § 5, demande une étiquette « à chaque changement ».
- **Clés.** `v` suit la numérotation de `texte.tex`. C'est la clé que lit `outils/extraction/appliquer_metrique.py`, et c'est celle de la numérisation Perseus de Hall–Geldart, non celle de l'imprimé (§ 6). `v_usuel` donne le numéro usuel (l'auteur, Coulon, Prato ; Wilson compte autrement en 687-689). `bornes` donne le passage en numérotation usuelle. `partie` vaut "" pour une rangée numérotée et "b" pour une rangée `suite`, comme dans le script.
- **Champ supplémentaire.** Une seule entrée a un `renfoncement` : 1226, ramené à 0 (§ 4.13).
- **Passages situés dans les sections des autres agents.** Seize clés de s00 sont doublées par une autre section : 39 (s01) ; 655, 659, 686 (s09) ; 688 b, 702, 726 (s10) ; 785, 814, 830 (s12) ; 947, 949 (s14) ; 1056 (s16) ; 1160, 1226, 1227 (s18). Le script charge les fichiers par ordre alphabétique, et l'entrée de même clé d'un fichier sNN écrase celle de s00. Ces seize entrées ne servent donc que de sécurité ; la simulation du script (1/11/2026) ne donne aucune étiquette divergente. Les dix-sept autres clés ne sont définies qu'ici.
- **Non étiquetés ici** : les parties lyriques des autres sections. Cela comprend les anapestes chantés 707-713, 776-784 et 1065-1072, ainsi que 714 (tr⁴∧) et 717 (ia³∧), qui appartiennent à l'amébée 707-725. Les anapestes 1073-1097, récités selon s16, y portent l'étiquette « an. ». Les cris hors mètre n'ont pas d'étiquette propre : 688 ἆ ἆ, Ἀρταμουξία aux rangées 1213 b et 1223, οἴμοι au début de la rangée 1216. ἔα ἔα (699) reçoit de s10 l'étiquette « do », qui couvre 699-701. Ἀρταμουξία à la rangée 1216 b n'est pas un cri hors mètre : il achève le trimètre (§ 4.13).

## 2. Tableau des passages de toute la pièce

Les lignes en gras sont les passages récités étiquetés par s00 seul. Les autres renvoient au fichier de la section, avec l'étiquette qu'il porte au 1/11/2026.

| Vers (usuels) | Mètre | Étiquette | Rangée de texte.tex | Donnée | Autorités principales |
|---|---|---|---|---|---|
| **1-38** | trimètres | **ia³** | f162v, 1 | s00 | White p. 447 ; Prato p. 345 |
| 39-62 | systèmes anapestiques (récitatif) | an. | f162v, 39 | s01 (s00 en doublon) | Mazon p. 127 n. 1 ; White p. 447 ; Prato p. 345 |
| **63-100** | trimètres | **ia³** | f163r, 63 | s00 | White p. 447 ; Prato p. 345 |
| 101-129 | chant d'Agathon | lyr. | f163v, 101 | s02 | — |
| **130-294** | trimètres | **ia³** | f164r, 130 | s00 | Mazon p. 128 ; White p. 447 ; Prato p. 345 |
| **295-311** | prose (proclamation) | **prose** | f166r, 295 | s00 | Σ R 295 (Dübner p. 266) ; White p. 448 ; Mazon p. 129 n. 1 ; Prato p. 346 |
| 312-330 | premier chant | lyr. | f166r, 312 | s04 | — |
| **331-351** | trimètres (ἀρά) | **ia³** | f166r, 331 | s00 | White p. 448 ; Conradt p. 50 ; Prato p. 346 |
| 352-371 | second chant | lyr. | f166v, 352 | s05 | — |
| **372-380** | trimètres (décret) | **ia³** | f166v, 373 (= 372) | s00 | White p. 448 |
| **381-382** | tétramètres iambiques catalectiques | **ia⁴∧** | f167r, 381 | s00 | White p. 448 ; Mazon p. 129 n. 6 ; Muff p. 162 ; Prato p. 348 ; Sommerstein *ad loc.* |
| **383-432** | trimètres (Mika) | **ia³** | f167r, 383 | s00 | Mazon p. 129 ; White p. 448 ; Prato p. 348 |
| 433-442 | ode | lyr. str. | f167v, 434 (= 433) | s07 | — |
| **443-458** | trimètres | **ia³** | f167v, 443 | s00 | White p. 448 ; Prato p. 348 |
| 459-465 | chant | lyr. | f167v, 459 | s08 | — |
| **466-519** | trimètres (Mnésiloque) | **ia³** | f168r, 466 | s00 | White p. 448 ; Prato p. 348 |
| 520-530 | antode | lyr. ant. | f168v, 520 | s07 | — |
| **531-573** | tétramètres iambiques catalectiques | **ia⁴∧** | f168v, 531 | s00 | Σ R 531 (Dübner p. 268) ; White p. 448 ; Mazon p. 130 ; Muff p. 163 ; Schroeder p. 61 ; Prato p. 350 ; Sommerstein *ad loc.* |
| **574-654** | trimètres (Clisthène) | **ia³** | f169r, 574 | s00 | Mazon p. 131 ; White p. 448 ; Prato p. 350 |
| 655-658 | tétramètres anapestiques catalectiques | an⁴∧ | f170r, 655 | s09 (s00 en doublon) | White p. 449 ; Mazon p. 131 ; Muff p. 163 ; Prato p. 350 |
| 659-662 | tétramètres trochaïques catalectiques | tr⁴∧ | f170r, 659 | s09 (s00 en doublon) | Mazon p. 131 ; Muff p. 163 ; Prato p. 350 |
| 663-686 | chant de la battue | lyr. | f170r, 663 | s09 | — |
| 687-688 | tétramètres trochaïques catalectiques | tr⁴∧ | f170v, 686 (= 687) | s09 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Muff p. 163 ; Prato p. 351 |
| 689-698 | trimètres (Mika) | ia³ | f170v, 688 *suite* (= 689) | s10 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Schroeder p. 63 ; Prato p. 351 |
| 699-701 | cri, dochmiaques | do | f170v, 699 | s10 | — |
| 702-706 | tétramètres trochaïques catalectiques | tr⁴∧ | f170v, 702 | s10 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Schroeder p. 63 ; Prato p. 351 |
| 707-725 | amébée (an., 714 tr⁴∧, do, 717 ia³∧, iambes lyriques, do) | an. lyr., tr⁴∧, do, ia³∧, lyr. | f170v, 707-719 | s10 | — |
| 726-727 | tétramètres trochaïques catalectiques | tr⁴∧ | f171r, 726 | s10 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Muff p. 163 ; Prato p. 352 |
| **728-775** | trimètres | **ia³** | f171r, 728 | s00 | White p. 449 ; Mazon p. 132-133 ; Prato p. 352 |
| 776-784 | anapestes chantés | an. lyr. | f171v, 776 | s11 | — |
| 785-813 | tétramètres anapestiques catalectiques | an⁴∧ | f171v, 785 | s12 (s00 en doublon) | White p. 449 ; Mazon p. 133 ; Schroeder p. 64 ; Prato p. 352 |
| 814-829 | pnîgos (dimètres anapestiques) | an. | f172r, 814 | s12 (s00 en doublon) | White p. 449 ; Muff p. 164 ; Prato p. 352 |
| 830-845 | tétramètres trochaïques catalectiques | tr⁴∧ | f172r, 830 | s12 (s00 en doublon) | White p. 449 ; Muff p. 164 ; Prato p. 352 |
| **846-912** | trimètres (Hélène) | **ia³** | f172v, 846 | s00 | White p. 449 |
| 913-915 | dochmiaques | do | f173r, 914 (= 913-914) | s13 | — |
| **916-946** | trimètres | **ia³** | f173r, 916 | s00 | White p. 449 ; Prato p. 352 |
| 947-948 | tétramètres anapestiques catalectiques | an⁴∧ | f173v, 947 | s14 (s00 en doublon) | Zimmermann p. 75 ; Muff p. 164 ; Mazon p. 134 ; Prato p. 352 ; White p. 449 |
| 949-952 | système anapestique | an. | f173v, 949 | s14 (s00 en doublon) | Prato p. 352 ; Mazon p. 134 ; Muff p. 164 |
| 953-1000 | danse chorale | lyr. ; str. α, ant. α, més., str. β, ant. β, més., str. γ, ant. γ | f173v, 953 | s14 | — |
| **1001-1014** | trimètres (le Scythe) | **ia³** | f174r, 1001 | s00 | White p. 450 ; Prato p. 353 |
| 1015-1055 | monodie d'Andromède | lyr. | f174v, 1016 (= 1015) | s15 | — |
| 1056-1064 | trimètres (Écho) | ia³ | f175r, 1056 | s16 (s00 en doublon) | White p. 450 ; Prato p. 355 |
| 1065-1072 | anapestes chantés | an. lyr. | f175r, 1065 | s16 | — |
| 1073-1097 | anapestes récités (Sommerstein, s16) | an. | f175r, 1073 | s16 | — |
| **1098-1135** | trimètres (Persée) | **ia³** | f175v, 1098 | s00 | White p. 450 ; Prato p. 355 |
| 1136-1159 | hymne | lyr. | f176r, 1136 | s17 | — |
| 1160-1226 | trimètres, avec trois cris hors mètre | ia³ | f176r, 1160 | s18 (s00 en doublon) | White p. 450 ; Prato p. 356 ; Muff p. 165 |
| 1227-1231 | système anapestique final | an. | f177r, 1227 | s18 (s00 en doublon) | White p. 450 ; Prato p. 356 ; Mazon p. 136 ; Muff p. 165 |

**Bilan** (numérotation usuelle) : 275 vers lyriques, 956 vers récités (300 et 931 si l'on compte tout 1065-1097 comme chanté, avec White, § 288 ; ici, 1073-1097 suit s16). Les vers récités se répartissent ainsi :
- 756 trimètres en dix-sept séries. White, p. 447-450, en compte 757, parce qu'il garde le v. 1187ᵃ de Hall–Geldart, que l'auteur supprime avec Ellebodius. Le texte de l'auteur a aussi deux trimètres de moins, 23 (supprimé avec Willems) et 500 (avec van Herwerden) ;
- 45 tétramètres iambiques catalectiques ;
- 29 tétramètres trochaïques catalectiques récités (30 avec 714) ;
- 35 tétramètres anapestiques catalectiques ;
- 74 numéros en systèmes anapestiques récités (39-62, 814-829, 949-952, 1073-1097, 1227-1231) ;
- 17 numéros de prose.

## 3. Ce que R dit de la métrique des parties récitées

Selon `recherche/metrique_structure.md` (§ 4.1), R n'a « pas de scholies métriques » pour les *Thesmophories*. C'est vrai des parties lyriques, qui n'ont aucune colométrie héliodoréenne. Mais trois scholies de R qualifient des parties récitées. On les lit dans Dübner et dans les marges de R :

1. **Σ 295** (Dübner 1842, p. 266 ; marge droite de R, f. 166r) : γυνὴ μιμουμένη κήρυκα. πεζῇ εὐφημίᾳ χρῶνται οἱ κωμικοί, ἐπειδὰν εὐχὴν ἢ ψήφισμα εἰσάγωσιν. C'est l'autorité antique de l'étiquette « prose » ; l'auteur la citait déjà dans son commentaire.
2. **Σ 531** (Dübner 1842, p. 268 ; marge droite de R, f. 168v, en onciales) : τοῦτο ἰαμβικὸν τετράμετρον καταλῆγον. Dans R, la note est abrégée (τοῦ<sup>τ</sup> ἰαμβικ(ὸν) τετράμετρ(ον) καταλῆγον) ; elle est suivie de la glose de 532 (εἰ μὴ ἄλλη γυνή). L'agent de la section s07 l'avait repérée sur l'image, avec une lecture « à contrôler » ; le texte de Dübner la confirme.
3. **Σ 547** (Dübner 1842, p. 268 ; marge gauche de R, f. 168v) : τοῦτο μόνον τὸ τετράμετρον ἰαμβεῖον ἀνάπαιστον ἔχει τὸν καταλήγοντα· ἄξιον οὖν αὐτὸν τηρῆσαι. Dans le texte de l'auteur, le second hémistiche de 547 (Φαίδρας τε· Πηνελόπην δὲ) a un anapeste au septième pied, νελόπην (⏑⏑–), devant la syllabe finale. La scholie relève cette licence : ἄξιον οὖν αὐτὸν τηρῆσαι, « il vaut donc la peine de le remarquer » (τηρῆσαι peut aussi se comprendre « le conserver »). Elle n'en donne pas la cause ; le nom propre est une explication possible, pas un dire du scholiaste. Son « μόνον » est exact : aucun autre des 45 tétramètres iambiques de la pièce n'a d'anapeste à cette place (§ 9).

La **mise en ligne de R** suit le mètre dans ces passages :
- la prose 295-309 est écrite en retrait (17 lignes pour 295-311) ; 310 (ταῦτ' εὔχεσθε…) et 311 (ἰὴ παιών…) reviennent à la marge des trimètres ;
- les tétramètres iambiques de 531 ss. tiennent chacun sur une ligne ;
- les tétramètres anapestiques de 801-813 et 947-948 débordent sur une seconde ligne (relevé de `recherche/metrique_structure.md`, § 4.1, d'après Velsen 1883, p. 69, et les images) ;
- 1226 est écrit à la marge comme les trimètres. 1227-1228 forment une seule ligne, à la marge, et 1229-1231 sont en retrait (§ 4.13).

## 4. Remarques par passage

### 4.1 Prologue (1-294)
Trois séries de trimètres (1-38, 63-100, 130-294), séparées par les anapestes du Serviteur (s01) et par le chant d'Agathon (s02). Aucune autorité ne les discute. Le v. 23 manque dans `texte.tex` : l'auteur le supprime avec Willems (apparat de l'édition antérieure). Ce n'est pas une lacune de numérotation.

### 4.2 295-311 : prose
- **Étiquette** : « prose », déjà portée par `texte.tex` et par l'édition antérieure de l'auteur. Autorités : la scholie (§ 3) ; White 1912, p. 448 (« 295-311 : prose ») ; Mazon 1904, p. 129 n. 1 (« En prose ») ; Prato 2001, p. 346 (« 295-311 prosa »).
- **Désaccords.** Conradt 1910, p. 50, compte εὐφημία ἔστω, εὐφημία ἔστω comme un vers et fait commencer la prose à εὔχεσθε : il rapproche la formule de l'εὐφημεῖτε (*Ach.* 237), compté comme vers. Schroeder 1909, p. 59, scande comme cola les acclamations qui encadrent l'allocution (εὐφημία 'στω deux fois, ἰὴ παιών, χαίρωμεν : « tum allocutione pedestri sermone interiecta »). Ces formules rituelles ont un rythme, mais elles n'appartiennent à aucun mètre stichique. Une étiquette « prose » sur la première rangée les couvre ; le commentaire pourra signaler le rythme des acclamations.
- **Mise en ligne.** Les seize rangées de l'auteur suivent les 17 lignes de R. Il en manque une, parce que l'auteur retranche la ligne τῇ Δήμητρι καὶ τῇ Κόρῃ (avec Blaydes) ; il retranche aussi τῇ Γῇ en fin de ligne (avec Dobree, d'après Σ). ταύτην νικᾶν, qui a une ligne propre dans R, est codée chez l'auteur comme rangée « suite ».
- **Numérotation.** Les rangées de `texte.tex` (295, 295, 296, 297, 297, 300, 301, 302, 302, 305, 306, 307, 307, 307 b, 310, 311) reprennent les numéros épars de Hall–Geldart, qui imprime la prose en lignes continues. Ils ne correspondent pas aux `\ligne{}` de l'édition antérieure (295, 296, 297, 299, 300, 301, 302, 303, 304, 305, 306, 307, 309, 309, 310, 311). Conséquence : la seconde rangée « εὐφημία ἔστω. », sans `n=`, a la même clé (295, "") que la première ; avec le script actuel, elle reçoit aussi l'étiquette (§ 7).

### 4.3 331-351 et 372-380 : trimètres
- 331-351 : White 1912, p. 448 (« trimeters (21) ») ; Conradt 1910, p. 50 (« das Gebet mit 21 Trimetern ») ; Mazon 1904, p. 129 n. 4 ; Prato 2001, p. 346.
- 372-380 : la première rangée porte `n=373` dans `texte.tex`. La numérisation Perseus numérote en effet 373-379 les vers usuels 372-378 et met deux vers sous le n° 379 ; la seconde rangée « 379 », sans `n=`, est le v. 379 usuel. L'imprimé de Hall–Geldart n'a pas ce 373 (`recherche/numerotation_vers.md`, § 4.3). Prato 2001, p. 346, étend sa parodos à 380, mais n'énumère que 295-371 ; il ne nomme pas les trimètres 372-380, que White (p. 448) range dans la « Scene I ». Mazon, p. 129, décrit la lecture de l'ordre du jour sans nommer le mètre.

### 4.4 381-382 et 531-573 : tétramètres iambiques catalectiques
- Les deux passages ont la même étiquette, **ia⁴∧**. Elle remplace « ia⁴ » (381) et « ia⁴ cat. » (531), issues de la conversion. Les 45 tétramètres ont tous de 15 à 18 syllabes (19, 16, 6 et 4 vers ; contrôle automatique, § 9).
- **381-382** : « recitative iambic tetrameters » (White, p. 448) ; « Deux tétramètres iambiques (381-382) marquent la conclusion de cette partie » (Mazon, p. 129 n. 6) ; « von der Chorführerin gesprochen » (Muff, p. 162) ; « tetrametri giambici catalettici » (Prato, p. 348) ; « iambic tetrameters » (Sommerstein, n. *ad* 381-2).
- **531-573** : la scholie de R (§ 3) ; White, p. 448 : 531-532 et 571-573 « recitative » (la coryphée), 533-570 « melodramatic iambic tetrameters » (la querelle de Mika et de Mnésiloque) ; Prato, p. 350, distingue de même 531-532 et 571-573 de 533-570, avec le même mètre ; Muff, p. 163, attribue 531-532 et 571-573 à la coryphée ; Schroeder, p. 61 (« 531-73 tetrametris iamb XLIII ») ; Mazon, p. 130 ; Sommerstein, n. *ad* 531-573. White et Prato distinguent un mode d'exécution, pas un mètre : une seule étiquette.

### 4.5 383-519 : les trois discours
Trimètres de 383-432, 443-458 et 466-519, entre l'ode (s07), le chant 459-465 (s08) et l'antode (s07). L'édition antérieure de l'auteur ne marquait pas le retour aux trimètres en 466 (« trim. iamb. » en 383 et 443, rien en 466) : l'étiquette est ajoutée.

### 4.6 574-654 : scène de Clisthène
« Le trimètre iambique succède au tétramètre » (Mazon, p. 131) ; White, p. 448 (81 trimètres) ; Prato, p. 350. La rangée 612 (σὺ δ' οὖν ποίει τοῦτ'…) est codée `suite` de 611 dans `texte.tex`. Or c'est un trimètre complet, prononcé par Clisthène, le v. 612 de toutes les éditions et de l'édition antérieure (`\apparat{612}`). Ainsi codé, il serait imprimé comme la seconde moitié de 611. 611 et 612 scandent chacun comme trimètre complet. C'est sans effet sur l'étiquette, mais c'est à corriger (§ 7).

### 4.7 655-764 : la battue et l'otage
- Les tétramètres récités de ce groupe sont étiquetés par s09 (655 an⁴∧, 659 tr⁴∧, 686 = 687 usuel tr⁴∧) et par s10 (702 et 726 tr⁴∧). Muff, p. 163, attribue à la coryphée 655-662, 687-688, 702-703, 705 et 726-727 : ni 704 (Mnésiloque) ni 706 (Mika dans `texte.tex`). Schroeder, p. 63, résume la seconde moitié : « Interiecta sunt strophis trim iamb III IV III, dein praemissis vocibus ἔα ἔα dochmiorum trias (700/1), tum tetram troch II I II ».
- **689-698.** Les trimètres de Mika commencent à la rangée `suite` de 688 (ποῖ ποῖ σὺ φεύγεις…), après le cri ἆ ἆ hors mètre. Le conflit de clés relevé le 28/10 est réglé : l'entrée (688, b) de s10 porte désormais **ia³**, comme celle de s00.
- **Harmonisation.** Faite par s10 le 1/11/2026 : « tr⁴∧ » (702, 714, 726) et « ia³∧ » (717). Les tétramètres de 702-706, 714 et 726-727 sont catalectiques (Prato, p. 351-352 ; Mazon, p. 132).
- **702.** Faux tel qu'imprimé : †πλέα† (⏑–) tombe aux positions 9-10, qui veulent –⏑. L'étiquette n'en dépend pas : ἔργα (R) ou μεστά (Porson ; Hall–Geldart, Wilson) donnent un tétramètre régulier (`s10_689-727.json`, entrée 702).

### 4.8 728-775 : une seule série de trimètres
White (p. 449) range 728-764 dans la « Syzygy » et 765-775 dans la « Scene III ». Mazon (p. 132-133) les sépare aussi : 765-784 est pour lui une « scène de transition », et il imprime à la p. 133 « (729-776, trimètres iambiques) », coquille pour 765-775. Prato, p. 352 : « 728-75 trimetri giambici ». Le mètre ne change pas en 765 : une seule étiquette, en 728. La rubrique de scène relève de `structure.json`.

### 4.9 Parabase (785-845)
Étiquetée par s12 (785 an⁴∧, 814 an., 830 tr⁴∧). Le *kommation* de 785 (Mazon, p. 133 ; Schroeder, p. 64 ; Prato, p. 352) ne demande pas d'étiquette distincte : c'est déjà un tétramètre anapestique catalectique. Les entrées de s00 doublent celles de s12, avec les mêmes étiquettes.

### 4.10 846-946 : parodie d'*Hélène*
Deux séries de trimètres (846-912, 916-946 : White, p. 449, « trimeters (98) ») autour des dochmiaques 913-915 (s13). La rangée 916 commence par λαβὼν ταχὺ πάνυ, fin de la phrase de 915 ; l'édition antérieure y plaçait déjà « trim. iamb. ». Prato, p. 352, passe de l'épirrhème (830-845) aux vv. 913-915 sans nommer 846-912 : c'est une omission de sa liste.

### 4.11 947-952 : anapestes de la coryphée
- Deux tétramètres (**an⁴∧**, 947), puis un système de trois dimètres et un parémiaque (**an.**, 949). Ce sont les étiquettes de l'édition antérieure (« 4 an. cat. », « dim. anap. », « paroem. ») et de `texte.tex` (« an⁴ », « an. »).
- **Récités ou mélodiques ?** « rezitierte Anapäste (Prokerygma) » (Zimmermann 1987, p. 75) ; « von der Chorführerin recitirt » (Muff, p. 164, qui rapporte la récitation mélodramatique supposée par Westphal) ; Mazon, p. 134 : « deux tétramètres anapestiques suivis d'un système ». White, p. 449 et § 589, en fait la première période (aab, 4 4 8) du stasimon. Le choix de l'étiquette n'en dépend pas.
- s14 définit ces clés, avec les mêmes étiquettes, et prévaut.
- **Problème textuel en 948.** Le texte de l'auteur porte παραχώρει ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχωμεν, ἅπερ καὶ, soit 25 syllabes. C'est trop pour un tétramètre anapestique catalectique. Sans παραχώρει, il reste 21 syllabes et un an⁴∧ régulier : ὅταν ὄρ- | για σεμ- | νὰ θεαῖν | ἱεραῖς ‖ ὥραις | ἀνέχω- | μεν ἅπερ | καί. Le mot manque dans R (image, f. 173v : ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχω- | μεν ἅπερ καὶ) et dans Hall–Geldart. La traduction de l'auteur ne le rend pas, et l'apparat de l'édition antérieure n'en dit rien. Il figure dans la version de novembre 2022 (`latex/Aristophane-Thesmo nov 2022.tex`), mais manque dans les états de mars 2020 à décembre 2021 (`edition/donnees/travaux_anterieurs/comparaison_versions.tsv`, entrées de 948 : « ∅ → παραχώρει »). Il s'agit vraisemblablement d'une scorie de saisie, à retirer du texte établi. s14 reprend le constat ; reste la correction de `texte.tex`.

### 4.12 1001-1135
Trimètres en 1001-1014, 1056-1064 et 1098-1135 (White, p. 450, « trimeters (61) » ; Prato, p. 353 et 355), entre la monodie (s15) et les anapestes d'Écho (s16). Dans `texte.tex`, le v. 1014 porte le n° 1015, et la monodie commence à la rangée 1016 (= 1015) : décalage de la numérisation Perseus. L'édition antérieure n'avait pas d'étiquette en 1056 ; elle plaçait « trim. iamb. » à la rangée 1063 b.

### 4.13 Exodos (1160-1231)
- **1160-1226 : trimètres** (White, p. 450 : « 1160-1187ᵃ, 1187ᵇ-1213, 1214-5, 1216-22, 1223-6 : trimeters (68) » ; Prato, p. 356 : « 1160-226 trimetri giambici » ; Muff, p. 165, pour les vers de la coryphée). Le Scythe y lance des cris hors mètre. Prato, p. 356, en compte trois (« 1213b ; 1215b ; 1222b extra metrum ») ; White, p. 450, les appelle anaphonemata (« 1213, 1215ᵇ, 1222 »). Ce sont Ἀρταμουξία (rangée 1213 b), **οἴμοι** (début de la rangée 1216 ; ligne à part chez Prato, p. 130, et 1215a chez Perseus) et Ἀρταμουξία (rangée 1223). Ils relèvent de s18. Ἀρταμουξία à la rangée 1216 b n'est pas un cri : il achève le trimètre τί δρᾶσι; ποῖ τὸ γρᾴδι᾽; Ἀρταμουξία, ⏑–⏑– ⏑–⏑– ⏑–⏑⏓, proposé par Lenting (Prato, p. 130, apparat), repris par Hall–Geldart et Prato. Il faut alors lire γρᾴδι᾽ : `texte.tex` imprime γρᾴδιο, dont le -ο ne compte pas. L'auteur note dans son commentaire, sur 1216, qu'« il manque un pied à ce vers », et tient οἴμοι pour *extra metrum* : le pied manquant est fourni par Ἀρταμουξία, que R isole sur sa ligne. Problème pour s18 et le commentaire critique.
- **1226 : correction.** L'édition antérieure ouvre le groupe « v. 1226-1231 » (la coryphée) par `\typeVers{anap.}\anap{…}`. `texte.tex` en a hérité l'étiquette « an. » et un renfoncement de 3 em sur 1226. Mais 1226 est un trimètre iambique, le dernier de la série : τρέχε νυν κατ' αὐτοὺς ἐς κόρακας ἐπουρίσας, ⏖–⏑– ––⏑⏖ ⏑–⏑– (deux résolutions, césure penthémimère après αὐτούς). C'est ce que disent White (« 1223-6 : trimeters »), Prato (« 1160-226 ») et Muff (1226 parmi les trimètres de la coryphée). R l'écrit à la marge, comme les trimètres, et les anapestes ne commencent qu'à la ligne suivante (image, f. 177r). L'entrée de s00 pour 1226 supprime l'étiquette et ramène le renfoncement à 0 ; il reste à retirer `findent=1.8em` dans `texte.tex`. Point à mentionner dans le commentaire critique, car il corrige l'édition antérieure.
- **1227-1231 : système anapestique, an.** Ainsi White, p. 450 et § 291 (« non-antistrophic period », tétramètre et pentamètre) ; Prato, p. 356 (« metri anapestici ») ; Mazon, p. 136 (« court système anapestique ») ; Muff, p. 165 (« ein anapästisches System, vom Chore gesungen ») ; Sommerstein, n. *ad* 1227-31 (« anapaestic »). Désaccord : Schroeder, p. 67, y voit deux tétramètres de la coryphée (« Clauditur fabula duobus coryphaeae tetrametris anapaesticis »).
- **Colométrie de 1227-1231.** R écrit ἀλλὰ πέπυσται μετρίως ἡμῖν ὥσθ' ὥρα δή 'στι βαδίζειν sur une seule ligne, à la marge (πέπαισται, le texte établi, est le lemme de Σ : Prato, p. 132, apparat) : c'est un tétramètre catalectique, dimètre et parémiaque. Suivent, en retrait, οἴκαδ' ἑκάστη | τὼ Θεσμοφόρω δ' ἡμῖν ἀγαθὴν | τούτων χάριν ἀνταδοῖτον. Les cinq rangées de l'auteur sont celles de Hall–Geldart (dimètre, parémiaque, dimètre, monomètre, parémiaque). Elles coupent après Θεσμοφόρω δ', alors que R coupe après ἑκάστη, à la fin de la phrase. s18 discute cette coupe (`s18_1160-1231.md`, § 4). L'étiquette « an. » ne dépend pas de ce choix.

## 5. Désaccords des autorités (synthèse)

| Passage | Point | Positions |
|---|---|---|
| 295-311 | prose entière ou acclamations en vers | prose : Σ R, White, Mazon, Prato, l'auteur ; εὐφημία ἔστω ×2 en vers : Conradt ; acclamations scandées : Schroeder |
| 531-573 | un seul mode ou deux | une seule étiquette (mètre unique) ; White et Prato distinguent 531-532 + 571-573 (récitatif) de 533-570 (« melodramatic ») |
| 659-662 | tétramètres isolés ou début de la période 659-666 | tétramètres récités : Mazon, Muff, Prato, Sommerstein ; période unique 659-666 : White § 221 |
| 728-775 | une ou deux séries | une série (Prato) ; deux unités dramatiques (White, Mazon) : sans effet sur l'étiquette |
| 947-952 | récités ou première période du stasimon | récités : Zimmermann, Muff ; période du stasimon : White § 589 |
| 1073-1097 | récités ou chantés | récités : Sommerstein, n. *ad* 1065-97, s16 ; « probably all melic » : White, § 288 |
| 1213-1223 | cris hors mètre | 1213 b, οἴμοι (1215 b), 1222 b : White, Prato ; détail et autres avis : `s18_1160-1231.md` |
| 1226 | anapestes ou trimètre | trimètre : White, Prato, Muff, R ; anapestes : édition antérieure de l'auteur |
| 1227-1231 | système ou deux tétramètres | système : White, Prato, Mazon, Muff, Sommerstein ; deux tétramètres : Schroeder |

## 6. Numérotation de texte.tex et clés

`texte.tex` suit la numérisation Perseus de Hall–Geldart (`.sources/corpus/thesmo_hall_geldart.tsv`), qui s'écarte de l'imprimé par endroits (`recherche/numerotation_vers.md`, §§ 1 et 4.3). Pour les clés de s00, cela donne :
- 373 = 372 usuel ;
- 686 = 687 ;
- 688 *suite* = 689 ;
- 1015 = 1014 (rangée sans étiquette ici).

Autres particularités relevées en passant :
- la rangée sans `n=` qui suit 379 est le v. 379 usuel ;
- les rangées en double de la prose (295, 297, 302, 307) ;
- 914 = 913-914 ;
- 23 et 500 sont absents : l'auteur les supprime (23 avec Willems, 500 avec van Herwerden). Il supprime aussi le v. 1187ᵃ de Hall–Geldart, avec Ellebodius.

Le champ `v_usuel` donne le report à faire si l'auteur retient la numérotation usuelle (option A de `recherche/numerotation_vers.md`, § 6 ; table `edition/donnees/numerotation_texte.tsv`) : 373 → 372, 686 → 687, (688, b) → (689, b).

## 7. Problèmes et recommandations

1. **s10, rangée (688, b) = v. 689** : fait (s10, 1/11/2026).
2. **Harmonisation des étiquettes de s10** : faite (s10, 1/11/2026). Reste l'écart des noms de cola (§ 9).
3. **`outils/extraction/appliquer_metrique.py`** :
   - (a) quand l'entrée de section n'a pas d'étiquette, reprendre celle de s00 au lieu de l'écraser : sans objet aujourd'hui, utile comme garde-fou ;
   - (b) ne poser l'étiquette que sur la première rangée qui porte la clé : sinon la rangée sans `n=` qui suit 295 reçoit « prose » une seconde fois ;
   - (c) traiter les parties « a » et « c », déjà demandé par s01, s02, s08 et s10 : toutes les rangées `suite` d'un vers prennent la clé « b », de sorte que 45 c de s01 n'est jamais lu et que sa rangée recevrait le schéma de 45 b.
4. **`texte.tex`** :
   - 1226 : retirer `findent=1.8em`, l'entrée de s00 et celle de s18 ramenant `indent` à 0 ;
   - 233 : φροντίσῃ → φροντίσῃς (§ 9) ;
   - 948 : retirer παραχώρει (§ 4.11) ;
   - 1216 : γρᾴδιο → γρᾴδι᾽ devant Ἀρταμουξία, si l'on garde le trimètre de Lenting ;
   - 612 : en faire une rangée numérotée et non une `suite` de 611 ;
   - numéroter les rangées de la prose 295-311 d'après l'édition antérieure (296 pour le second εὐφημία ἔστω, etc.), ce qui résout aussi le point 3 (b).
5. **Recension** (`recherche/metrique_structure.md`, § 4.1) : nuancer « pas de scholies métriques ». R a les scholies métriques 295, 531 et 547 sur des parties récitées (§ 3).
6. **Pour le commentaire critique et l'établissement du texte** :
   - 948 : παραχώρει, absent de R et de Hall–Geldart, rend le tétramètre faux (§ 4.11) ;
   - 233 : coquille φροντίσῃ, héritée de Perseus (§ 9) ;
   - 162 : la conjecture de l'auteur donne trois anapestes de suite (§ 9) ;
   - 1226 (trimètre, contre l'étiquette de l'édition antérieure) ;
   - 547 (anapeste au septième pied, que Σ R signale) ;
   - 1216 (οἴμοι hors mètre, Ἀρταμουξία dans le trimètre ; s18) ;
   - 1227-1231 (coupe de R après ἑκάστη).

## 8. Sources consultées

- **R** : images du dossier Ravennas, ff. 164r, 165r, 166r, 168v, 173v et 177r. Découpes : `.travail/metrique/s00/f166r_*.png`, `f168v_547.png`, `f177r_1222-1231.png`, `.travail/metrique/s00/verif/R_*.png`, et `.travail/metrique/s07/R_f168v_marge531.png`.
- **F. Dübner**, *Scholia Graeca in Aristophanem*, Paris 1842, p. 266 (Σ 295) et 268 (Σ 531, Σ 547) : lu sur l'image (`.sources/web/editions/1842_Paris_Dubner_scholia/`, index PDF 344 et 346).
- **J. W. White**, *The Verse of Greek Comedy*, London 1912, « Table of Structure and Rhythms », p. 447-450 (texte archive.org ; p. 448 contrôlée sur l'image) ; §§ 221, 288, 291, 589 d'après la même source ; § 124, p. 49 (image).
- **C. Prato**, *Aristofane. Le donne alle Tesmoforie*, Milano 2001, « Appendice metrica », p. 345-356 : lu sur les images (`.sources/drive/editions_commentaires/prato2001_ocr/pages/idx431-442.png`) ; texte et apparat de 1198-1231, p. 130 et 132 (idx216, idx218).
- **P. Mazon**, *Essai sur la composition des comédies d'Aristophane*, Paris 1904, p. 127-136 (texte archive.org ; p. 133 contrôlée sur l'image).
- **Chr. Muff**, *Über den Vortrag der chorischen Partieen bei Aristophanes*, Halle 1872, p. 162-165.
- **O. Schroeder**, *Aristophanis cantica*, Lipsiae 1909, p. 59, 61, 63 (image), 64, 67.
- **C. Conradt**, *Die metrische und rhythmische Komposition der Komödien des Aristophanes* I, Greifenberg 1910, p. 50 (index PDF 49).
- **B. Zimmermann**, *Untersuchungen zur Form und dramatischen Technik der Aristophanischen Komödien* III, Frankfurt 1987, p. 75.
- **A. H. Sommerstein**, *Aristophanes. Thesmophoriazusae*, Warminster 1994 : notes « Metre » *ad* 381-2, 531-573, 655-8, 659-666, 687-8, 702-6, 726-7, 785-845, 947-952, 1065-97, 1227-31. Lu dans l'extrait textuel sans pagination (`.sources/drive/ravennas/Sommerstein_1994_Thesm_textrep.txt`) ; cité par lemme, non par page.
- **Hall–Geldart 1907** (texte Perseus) pour la numérotation ; `recherche/numerotation_vers.md` et `edition/donnees/concordance_vers.tsv` pour l'écart entre Perseus et l'imprimé.
- **Coulon 1928** (extrait textuel) et **Wilson 2007** (couche OCR) pour 233.
- **LSJ** (corpus local), s.v. νῦν, II.
- **Édition antérieure de l'auteur** (`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `… vv 642-fin-bis.tex`) : étiquettes `\typeVers`, apparat et commentaire.
- **Données des autres sections** : `s01`, `s09`, `s10`, `s12`, `s14`, `s15`, `s16`, `s17`, `s18` (clés, étiquettes, schémas), états du 1/11/2026.

## 9. Vérification (1/11/2026)

**Méthode.** s00 n'a pas de schémas ligne à ligne : le contrôle a donc porté sur ce que chaque étiquette affirme, vers par vers. Un scanseur de contrôle (`.travail/metrique/s00/verif/scan.py`, résultats dans `scansion_recitee.tsv`) réunit rangées et suites de `texte.tex`, puis cherche pour chaque vers une lecture conforme au mètre annoncé. Il tient compte des quantités, de la position, de la correption attique, de l'élision, de la crase, de la synizèse, des résolutions et des pieds admis à chaque place. Ce scanseur n'est pas une autorité : toutes les licences qu'il réclame ont été relues à la main. Il retrouve les dispositions que White, p. 49, donne pour Th. 91 et 483.

| Étiquette | Vers contrôlés | Acceptés | Rejets |
|---|---:|---:|---|
| ia³ | 754 | 749 | 611-612, 688, 1213, 1216, 1223 |
| ia⁴∧ | 45 | 45 | — |
| tr⁴∧ (avec 714) | 30 | 29 | 702 |
| an⁴∧ | 35 | 34 | 948 |
| an. (systèmes de s00) | 48 | 48 | — |
| **Total** | **912** | **905** | **7** |

**Résultat : aucune étiquette de s00 n'est à changer, ni aucune borne.** Les sept rejets s'expliquent tous :
- 611-612 : deux trimètres réunis par le codage `suite` (§ 4.6) ;
- 688 : ἆ ἆ hors mètre, codé avec le trimètre 689 ;
- 702 : †πλέα† (§ 4.7) ;
- 948 : παραχώρει (§ 4.11) ;
- 1213 : trimètre complet suivi du cri Ἀρταμουξία ;
- 1216 : οἴμοι hors mètre, puis trimètre, avec élision de γρᾴδιο (§ 4.13) ;
- 1223 : cri seul.

Autres contrôles : Σ 547 dit vrai (seul anapeste au 7e pied des ia⁴∧) ; le compte des 756 trimètres, des 45, 29 et 35 tétramètres et les 33 entrées du JSON sont exacts. Croisement automatique : les 198 vers récités (hors 1073-1097) pour lesquels s01, s09, s10, s12, s14, s16 et s18 donnent un schéma ou une scansion s'accordent avec le grec. Seuls écarts : 948 et 1216, déjà signalés par s14 et s18 ; 688 et 1213, où le cri hors mètre est codé avec le vers ; 45, effet de la limite du script (§ 7).

### Erreurs de s00 trouvées et corrigées

1. **Cris hors mètre (§§ 1 et 4.13, JSON 1160).** s00 prenait Ἀρταμουξία de la rangée 1216 b pour le « 1215b » de Prato et le « 1215ᵇ » de White. C'est **οἴμοι** (Prato, p. 130 ; Perseus 1215a). Ἀρταμουξία appartient au trimètre 1216. Erreur relevée d'abord par s18, confirmée sur les sources.
2. **Σ 547 (§§ 3 et 7).** « recommande de la garder » forçait ἄξιον αὐτὸν τηρῆσαι, et « due au nom propre » n'est pas dans la scholie.
3. **R en 1227 (§ 4.13).** R n'a pas πέπ(αισται) mais πέπυσται (Prato, Wilson, apparat de l'auteur).
4. **Numérotation (§§ 1, 4.3, 4.12, 6, JSON 373, 686, 1001).** Le décalage est celui de la numérisation Perseus, non de l'imprimé de Hall–Geldart. `v_usuel` n'est pas toujours le numéro de Wilson (687-689).
5. **Muff (§ 4.7).** Il ne donne pas « tous » les tétramètres à la coryphée : 704 et 706 en sont exclus.
6. **Mazon.** Cité à tort pour le mètre de 372-380 (p. 129) et de 830-845 (p. 133) : il n'en parle pas (§ 4.3, JSON 373, 830).
7. **Bilan (§ 2).** 300/931 et 49 supposaient tout 1065-1097 chanté ; avec l'étiquette « an. » de s16 en 1073 : 275/956 et 74.
8. **État périmé.** Tableau du § 2, §§ 1, 4.7, 4.11, 7, notes du JSON : s14 à s18 existent, le conflit (688, b) et l'harmonisation sont réglés. Seize clés sont des doublons, aucune ne diverge.

### Erreurs de `texte.tex` décelées, non corrigées ici

- **233 φροντίσῃ** : coquille de Perseus, reprise par l'édition antérieure. R a φροντίσης (image, f. 165r, l. 25), Coulon et Wilson φροντίσῃς. La forme imprimée crée un hiatus (φροντίσῃ | ὡς), le seul des trimètres de la pièce sans justification.
- **948 παραχώρει**, **1216 γρᾴδιο**, **612 en `suite`**, **1226 `findent`** : § 7.
- **1213 b en `suite`** : le codage fait lire le cri comme fin de vers (s18).

### Licences relues, sans erreur

- **Hiatus** : τί (70, 193, 208, 252, 635, 733, 852, 868, 892, 902, 904, 1193, 1200), περί (162, 378, 577), εὖ (12), interjections (223, 245, 1005), changement de locuteur (562, 646), parler du Scythe (1179, 1218, 1225 ; s18).
- **Synizèses** : -κλέα (26), Πρωτέως (874, 891), Μενέλεων (901), θεοί (905, 1098), ὅτι ἡ (275), μὴ ἀ- et μὴ ἡ- (288, 536), Ἀπόλλω οὔκ (269).
- **Abrègement interne** : ποι-, τοι- (une trentaine de vers), ῳ et ῃ devant -ί déictique (250, 1221).
- **Voyelle brève allongée devant muta cum liquida** : deux cas seulement, πατρίς (859, parodie d'*Hélène*) et τυγάτριον (1184, le Scythe ; s18).
- **νυν long** (239, 279, 947) : régulier en comédie (LSJ s.v. νῦν, II : « ū in Com. »).
- **Dichrona longs exigés par le mètre** : tous relus, sans difficulté (Εὐρῑπίδης, δρᾱ-, ὑμ-, -ί déictique, -ᾱς, ῑμάτιον en 656 : LSJ ; Λᾱμαχ- en 841). κεκρύφαλος a ῡ en 138 et 257 : le mètre l'exige, LSJ ne note pas cette quantité.
- **Anapestes coupés** : tous après prépositif, devant enclitique ou au changement de locuteur, sauf 1184 et 1198 (parler du Scythe ; pour 1184, s18). En 231, πεποίηται avec ποι- bref donne un tribraque.

### Points discutables

- **162 (conjecture de l'auteur).** οἳ περὶ ἁρμονίαν ἐκεχήνεσαν scande, avec hiatus régulier après περί : ––⏑– ⏖–⏖– ⏖–⏑⏓. Cela fait trois anapestes de suite (pieds 3-5), sans autre exemple dans les trimètres de la pièce d'après ce contrôle. White, p. 49, compte 54 trimètres à trois anapestes chez Aristophane, surtout aux pieds 1, 2, 4 et 2, 4, 5. Le mètre n'exclut donc pas la leçon, mais la signale.
- **Schémas sur les vers récités.** `CONVENTIONS.md`, § 5, réserve le schéma aux vers chantés. s00, s09 et s16 (1056-1064) s'y tiennent. s01, s10 (689-698, 702-706, 726-727), s12, s14 (947-952), s16 (1073-1097) et s18 remplissent `schema` pour des vers récités, qui seraient donc imprimés. À trancher pour toute la pièce.
- **Noms de cola.** Pour le même mètre récité, s10 écrit `4tr∧`, s12 et s14 `tr⁴∧`. L'étiquette de marge est harmonisée, le champ `colon` ne l'est pas.
- **1073-1097.** Le bilan dépend du choix de s16 (récité) contre White, § 288 (« probably all melic »).
- **310.** « Prose » couvre ce vers, que R ramène à la marge des trimètres : il ne scande pourtant pas comme trimètre (εὔχεσθε donne une longue à la 3e position). La mise en ligne de R n'est pas ici un indice métrique.
- **τηρῆσαι (Σ 547).** « Remarquer » est retenu ; « conserver » reste possible si la scholie vise une correction.
