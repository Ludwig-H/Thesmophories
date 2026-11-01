# Étiquettes métriques des parties récitées (vv. 1-1231) — section s00

*Chantier « métrique », section s00. Données : `edition/donnees/metrique/s00_etiquettes.json` (33 entrées). Rédigé le 28/10/2026. Les références ont été lues sur les sources (§ 8). Les images de R ont été contrôlées pour 295-311 (f. 166r), 531 et 547 (f. 168v), 1222-1231 (f. 177r). Découpes et scripts : `.travail/metrique/s00/`.*

## 1. Objet et conventions

- **Une étiquette par passage récité**, stichique ou systématique, portée par sa première rangée de `texte.tex`, sans schéma (`schema` et `colon` vides). Étiquettes : **ia³** (trimètres iambiques), **ia⁴∧** (tétramètres iambiques catalectiques), **tr⁴∧** (tétramètres trochaïques catalectiques), **an⁴∧** (tétramètres anapestiques catalectiques), **an.** (système anapestique), **prose**. Aucune étiquette n'est répétée tant que le mètre ne change pas : `edition/CONVENTIONS.md`, § 5, demande une étiquette « à chaque changement ».
- **Clés.** `v` suit la numérotation de `texte.tex`. C'est la clé que lit `outils/extraction/appliquer_metrique.py`, et c'est celle de Hall–Geldart, reprise du texte Perseus (§ 6). `v_usuel` donne le numéro de Coulon et de Wilson. `bornes` donne le passage en numérotation usuelle. `partie` vaut "" pour une rangée numérotée et "b" pour une rangée `suite`, comme dans le script.
- **Champ supplémentaire.** Une seule entrée a un `renfoncement` : 1226, ramené à 0 (§ 4.13).
- **Passages situés dans les sections des autres agents.** Les passages récités des sections s01, s09, s10 et s12 portent ici une entrée « de sécurité » (39, 655, 659, 686, 688 b, 702, 726, 785, 814, 830). Le script charge les fichiers par ordre alphabétique, et l'entrée de même clé d'un fichier sNN écrase celle de s00. Ces entrées ne servent donc que si la section ne définit pas la clé. Pour 947, 949 et 1227, sections encore sans données (s14, s18), ce sont les entrées de s00 qui s'appliquent pour l'instant.
- **Non étiquetés ici** : les parties lyriques des autres sections. Cela comprend les anapestes chantés 707-713, 776-784 et 1065-1097, ainsi que 714 (tr⁴∧) et 717 (ia³∧), qui appartiennent à l'amébée 707-725. Les cris hors mètre ne sont pas étiquetés non plus : 688 ἆ ἆ, 699 ἔα ἔα, et Ἀρταμουξία aux rangées 1213 b, 1216 b et 1223 de `texte.tex`.

## 2. Tableau des passages de toute la pièce

Les lignes en gras sont les passages récités étiquetés par s00. Les autres renvoient au fichier de la section lyrique, avec l'étiquette qu'il porte au 28/10/2026 (« — » : section encore sans données ; l'étiquette déjà présente dans `texte.tex` s'applique alors).

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
| **372-380** | trimètres (décret) | **ia³** | f166v, 373 (= 372) | s00 | White p. 448 ; Mazon p. 129 |
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
| **689-698** | trimètres (Mika) | **ia³** | f170v, 688 *suite* (= 689) | s00, **écrasé par s10** (§ 4.7) | White p. 449 ; Mazon p. 132 ; Schroeder p. 63 ; Prato p. 351 |
| 699-701 | cri, dochmiaques | do | f170v, 699 | s10 | — |
| 702-706 | tétramètres trochaïques catalectiques | tr⁴ (s10) / tr⁴∧ (s00) | f170v, 702 | s10 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Schroeder p. 63 ; Prato p. 351 |
| 707-725 | amébée (an., 714 tr⁴∧, do, 717 ia³∧, iambes lyriques, do) | an., tr⁴, do, ia³ cat., lyr. | f170v, 707-719 | s10 | — |
| 726-727 | tétramètres trochaïques catalectiques | tr⁴ (s10) / tr⁴∧ (s00) | f171r, 726 | s10 (s00 en doublon) | White p. 449 ; Mazon p. 132 ; Muff p. 163 ; Prato p. 352 |
| **728-775** | trimètres | **ia³** | f171r, 728 | s00 | White p. 449 ; Mazon p. 132-133 ; Prato p. 352 |
| 776-784 | anapestes chantés | an. lyr. | f171v, 776 | s11 | — |
| 785-813 | tétramètres anapestiques catalectiques | an⁴∧ | f171v, 785 | s12 (s00 en doublon) | White p. 449 ; Mazon p. 133 ; Schroeder p. 64 ; Prato p. 352 |
| 814-829 | pnîgos (dimètres anapestiques) | an. | f172r, 814 | s12 (s00 en doublon) | White p. 449 ; Muff p. 164 ; Prato p. 352 |
| 830-845 | tétramètres trochaïques catalectiques | tr⁴∧ | f172r, 830 | s12 (s00 en doublon) | White p. 449 ; Mazon p. 133 ; Muff p. 164 ; Prato p. 352 |
| **846-912** | trimètres (Hélène) | **ia³** | f172v, 846 | s00 | White p. 449 |
| 913-915 | dochmiaques | do | f173r, 914 (= 913-914) | s13 | — |
| **916-946** | trimètres | **ia³** | f173r, 916 | s00 | White p. 449 ; Prato p. 352 |
| **947-948** | tétramètres anapestiques catalectiques | **an⁴∧** | f173v, 947 | s00 (s14 à venir) | Zimmermann p. 75 ; Muff p. 164 ; Mazon p. 134 ; Prato p. 352 ; White p. 449 |
| **949-952** | système anapestique | **an.** | f173v, 949 | s00 (s14 à venir) | Prato p. 352 ; Mazon p. 134 ; Muff p. 164 |
| 953-1000 | danse chorale | lyr. (texte.tex) | f173v, 953 | — (s14) | — |
| **1001-1014** | trimètres (le Scythe) | **ia³** | f174r, 1001 | s00 | White p. 450 ; Prato p. 353 |
| 1015-1055 | monodie d'Andromède | lyr. (texte.tex) | f174v, 1016 (= 1015) | — (s15) | — |
| **1056-1064** | trimètres (Écho) | **ia³** | f175r, 1056 | s00 | White p. 450 ; Prato p. 355 |
| 1065-1097 | anapestes (chantés, puis récités selon Sommerstein) | an. (texte.tex) | f175r, 1065 | — (s16) | — |
| **1098-1135** | trimètres (Persée) | **ia³** | f175v, 1098 | s00 | White p. 450 ; Prato p. 355 |
| 1136-1159 | hymne | lyr. (texte.tex) | f176r, 1136 | — (s17) | — |
| **1160-1226** | trimètres, avec trois cris hors mètre | **ia³** | f176r, 1160 | s00 | White p. 450 ; Prato p. 356 ; Muff p. 165 |
| **1227-1231** | système anapestique final | **an.** | f177r, 1227 | s00 (s18 à venir) | White p. 450 ; Prato p. 356 ; Mazon p. 136 ; Muff p. 165 |

**Bilan** (numérotation usuelle) : 300 vers lyriques, 931 vers récités. Ces derniers se répartissent ainsi :
- 756 trimètres en dix-sept séries. White, p. 447-450, en compte 757, parce qu'il garde le v. 1187ᵃ de Hall–Geldart, que l'auteur supprime avec Ellebodius. Le texte de l'auteur a aussi deux trimètres de moins, 23 (supprimé avec Willems) et 500 (avec van Herwerden) ;
- 45 tétramètres iambiques catalectiques ;
- 29 tétramètres trochaïques catalectiques récités (30 avec 714) ;
- 35 tétramètres anapestiques catalectiques ;
- 49 numéros en systèmes anapestiques récités (39-62, 814-829, 949-952, 1227-1231) ;
- 17 numéros de prose.

## 3. Ce que R dit de la métrique des parties récitées

Selon `recherche/metrique_structure.md` (§ 4.1), R n'a « pas de scholies métriques » pour les *Thesmophories*. C'est vrai des parties lyriques, qui n'ont aucune colométrie héliodoréenne. Mais trois scholies de R qualifient des parties récitées. On les lit dans Dübner et dans les marges de R :

1. **Σ 295** (Dübner 1842, p. 266 ; marge droite de R, f. 166r) : γυνὴ μιμουμένη κήρυκα. πεζῇ εὐφημίᾳ χρῶνται οἱ κωμικοί, ἐπειδὰν εὐχὴν ἢ ψήφισμα εἰσάγωσιν. C'est l'autorité antique de l'étiquette « prose » ; l'auteur la citait déjà dans son commentaire.
2. **Σ 531** (Dübner 1842, p. 268 ; marge droite de R, f. 168v, en onciales) : τοῦτο ἰαμβικὸν τετράμετρον καταλῆγον. Dans R, la note est abrégée (τοῦ<sup>τ</sup> ἰαμβικ(ὸν) τετράμετρ(ον) καταλῆγον) ; elle est suivie de la glose de 532 (εἰ μὴ ἄλλη γυνή). L'agent de la section s07 l'avait repérée sur l'image, avec une lecture « à contrôler » ; le texte de Dübner la confirme.
3. **Σ 547** (Dübner 1842, p. 268 ; marge gauche de R, f. 168v) : τοῦτο μόνον τὸ τετράμετρον ἰαμβεῖον ἀνάπαιστον ἔχει τὸν καταλήγοντα· ἄξιον οὖν αὐτὸν τηρῆσαι. Dans le texte de l'auteur, le second hémistiche de 547 (Φαίδρας τε· Πηνελόπην δὲ) a un anapeste au septième pied, νελόπην (⏑⏑–), devant la syllabe finale. La scholie relève cette licence, due au nom propre, et recommande de la garder.

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
- 372-380 : la première rangée porte `n=373` dans `texte.tex`. Hall–Geldart numérote en effet 373-379 les vers 372-378 de Coulon et met deux vers sous le n° 379 ; la seconde rangée « 379 », sans `n=`, est le v. 379 usuel. Prato 2001, p. 346, étend sa parodos à 380, mais n'énumère que 295-371 ; il ne nomme pas les trimètres 372-380, que White (p. 448) range dans la « Scene I ».

### 4.4 381-382 et 531-573 : tétramètres iambiques catalectiques
- Les deux passages ont la même étiquette, **ia⁴∧**. Elle remplace « ia⁴ » (381) et « ia⁴ cat. » (531), issues de la conversion. Les 45 tétramètres ont tous de 15 à 18 syllabes (contrôle automatique).
- **381-382** : « recitative iambic tetrameters » (White, p. 448) ; « Deux tétramètres iambiques (381-382) marquent la conclusion de cette partie » (Mazon, p. 129 n. 6) ; « von der Chorführerin gesprochen » (Muff, p. 162) ; « tetrametri giambici catalettici » (Prato, p. 348) ; « iambic tetrameters » (Sommerstein, n. *ad* 381-2).
- **531-573** : la scholie de R (§ 3) ; White, p. 448 : 531-532 et 571-573 « recitative » (la coryphée), 533-570 « melodramatic iambic tetrameters » (la querelle de Mika et de Mnésiloque) ; Prato, p. 350, distingue de même 531-532 et 571-573 de 533-570, avec le même mètre ; Muff, p. 163, attribue 531-532 et 571-573 à la coryphée ; Schroeder, p. 61 (« 531-73 tetrametris iamb XLIII ») ; Mazon, p. 130 ; Sommerstein, n. *ad* 531-573. White et Prato distinguent un mode d'exécution, pas un mètre : une seule étiquette.

### 4.5 383-519 : les trois discours
Trimètres de 383-432, 443-458 et 466-519, entre l'ode (s07), le chant 459-465 (s08) et l'antode (s07). L'édition antérieure de l'auteur ne marquait pas le retour aux trimètres en 466 (« trim. iamb. » en 383 et 443, rien en 466) : l'étiquette est ajoutée.

### 4.6 574-654 : scène de Clisthène
« Le trimètre iambique succède au tétramètre » (Mazon, p. 131) ; White, p. 448 (81 trimètres) ; Prato, p. 350. La rangée 612 (σὺ δ' οὖν ποίει τοῦτ'…) est codée `suite` de 611 dans `texte.tex`. Or c'est un trimètre complet, prononcé par Clisthène, le v. 612 de toutes les éditions et de l'édition antérieure (`\apparat{612}`). Ainsi codé, il serait imprimé comme la seconde moitié de 611. C'est sans effet sur l'étiquette, mais c'est à corriger (§ 7).

### 4.7 655-764 : la battue et l'otage
- Les tétramètres récités de ce groupe sont déjà étiquetés par s09 (655 an⁴∧, 659 tr⁴∧, 686 = 687 usuel tr⁴∧) et par s10 (702 et 726 « tr⁴ »). Muff, p. 163, les attribue tous à la coryphée. Schroeder, p. 63, résume la seconde moitié : « Interiecta sunt strophis trim iamb III IV III, dein praemissis vocibus ἔα ἔα dochmiorum trias (700/1), tum tetram troch II I II ».
- **689-698 (conflit).** Les trimètres de Mika commencent à la rangée `suite` de 688 (ποῖ ποῖ σὺ φεύγεις…), après le cri ἆ ἆ hors mètre. s10 a laissé cette rangée sans étiquette, « selon l'usage actuel de texte.tex » : il renvoie la décision au présent relevé (`s10_689-727.md`, § 7). s00 lui donne **ia³**. Mais l'entrée (688, b) de s10, sans étiquette, écrase celle de s00. Sans correction, 689-698 resteraient sous l'étiquette tr⁴∧ de 687-688 (simulation du script, § 7).
- **Harmonisation.** s10 écrit « tr⁴ » (702, 714, 726) et « ia³ cat. » (717). s09, s12 et s00 écrivent « tr⁴∧ ». Les tétramètres de 702-706, 714 et 726-727 sont catalectiques (Prato, p. 351-352 ; Mazon, p. 132) : « tr⁴∧ » partout.

### 4.8 728-775 : une seule série de trimètres
White (p. 449) range 728-764 dans la « Syzygy » et 765-775 dans la « Scene III ». Mazon (p. 132-133) les sépare aussi : 765-784 est pour lui une « scène de transition », et il imprime à la p. 133 « (729-776, trimètres iambiques) », coquille pour 765-775. Prato, p. 352 : « 728-75 trimetri giambici ». Le mètre ne change pas en 765 : une seule étiquette, en 728. La rubrique de scène relève de `structure.json`.

### 4.9 Parabase (785-845)
Étiquetée par s12 (785 an⁴∧, 814 an., 830 tr⁴∧). Le *kommation* de 785 (Mazon, p. 133 ; Schroeder, p. 64 ; Prato, p. 352) ne demande pas d'étiquette distincte : c'est déjà un tétramètre anapestique catalectique. Les entrées de s00 doublent celles de s12, avec les mêmes étiquettes.

### 4.10 846-946 : parodie d'*Hélène*
Deux séries de trimètres (846-912, 916-946 : White, p. 449, « trimeters (98) ») autour des dochmiaques 913-915 (s13). La rangée 916 commence par λαβὼν ταχὺ πάνυ, fin de la phrase de 915 ; l'édition antérieure y plaçait déjà « trim. iamb. ». Prato, p. 352, passe de l'épirrhème (830-845) aux vv. 913-915 sans nommer 846-912 : c'est une omission de sa liste.

### 4.11 947-952 : anapestes de la coryphée
- Deux tétramètres (**an⁴∧**, 947), puis un système de trois dimètres et un parémiaque (**an.**, 949). Ce sont les étiquettes de l'édition antérieure (« 4 an. cat. », « dim. anap. », « paroem. ») et de `texte.tex` (« an⁴ », « an. »).
- **Récités ou mélodiques ?** « rezitierte Anapäste (Prokerygma) » (Zimmermann 1987, p. 75) ; « von der Chorführerin recitirt » (Muff, p. 164, qui rapporte la récitation mélodramatique supposée par Westphal) ; Mazon, p. 134 : « deux tétramètres anapestiques suivis d'un système ». White, p. 449 et § 589, en fait la première période (aab, 4 4 8) du stasimon. Le choix de l'étiquette n'en dépend pas.
- Si s14 définit ces clés, ses entrées prévaudront.
- **Problème textuel en 948.** Le texte de l'auteur porte παραχώρει ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχωμεν, ἅπερ καὶ, soit 25 syllabes. C'est trop pour un tétramètre anapestique catalectique. Sans παραχώρει, il reste 21 syllabes et un an⁴∧ régulier : ὅταν ὄρ- | για σεμ- | νὰ θεαῖν | ἱεραῖς ‖ ὥραις | ἀνέχω- | μεν ἅπερ | καί. Le mot manque dans R (image, f. 173v : ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχω- | μεν ἅπερ καὶ) et dans Hall–Geldart. La traduction de l'auteur ne le rend pas, et l'apparat de l'édition antérieure n'en dit rien. Il figure déjà dans la version de novembre 2022 (`latex/Aristophane-Thesmo nov 2022.tex`). Il s'agit vraisemblablement d'une scorie de saisie, à retirer du texte établi. À signaler à s14 et à l'établissement du texte.

### 4.12 1001-1135
Trimètres en 1001-1014, 1056-1064 et 1098-1135 (White, p. 450, « trimeters (61) » ; Prato, p. 353 et 355), entre la monodie (s15) et les anapestes d'Écho (s16). Dans `texte.tex`, le v. 1014 porte le n° 1015, et la monodie commence à la rangée 1016 (= 1015) : décalage de Hall–Geldart. L'édition antérieure n'avait pas d'étiquette en 1056 ; elle plaçait « trim. iamb. » à la rangée 1063 b.

### 4.13 Exodos (1160-1231)
- **1160-1226 : trimètres** (White, p. 450 : « 1160-1187ᵃ, 1187ᵇ-1213, 1214-5, 1216-22, 1223-6 : trimeters (68) » ; Prato, p. 356 : « 1160-226 trimetri giambici » ; Muff, p. 165, pour les vers de la coryphée). Le Scythe y lance des cris hors mètre. Prato, p. 356, en compte trois (« 1213b ; 1215b ; 1222b extra metrum ») ; White, p. 450, les appelle anaphonemata. Dans `texte.tex`, ce sont les rangées « Ἀρταμουξία » 1213 b, 1216 b et 1223. Ils relèvent de s18. L'auteur note dans son commentaire, sur 1216 (οἴμοι, τί δρᾶσι; ποῖ τὸ γρᾴδιο;), qu'« il manque un pied à ce vers », et tient οἴμοι pour *extra metrum*. Hall–Geldart fait entrer Ἀρταμουξία dans le trimètre (τί δρᾶσι; ποῖ τὸ γρᾴδι'; Ἀρταμουξία). Problème pour s18 et le commentaire critique.
- **1226 : correction.** L'édition antérieure ouvre le groupe « v. 1226-1231 » (la coryphée) par `\typeVers{anap.}\anap{…}`. `texte.tex` en a hérité l'étiquette « an. » et un renfoncement de 3 em sur 1226. Mais 1226 est un trimètre iambique, le dernier de la série : τρέχε νυν κατ' αὐτοὺς ἐς κόρακας ἐπουρίσας, ⏖–⏑– ––⏑⏖ ⏑–⏑– (deux résolutions, césure penthémimère après αὐτούς). C'est ce que disent White (« 1223-6 : trimeters »), Prato (« 1160-226 ») et Muff (1226 parmi les trimètres de la coryphée). R l'écrit à la marge, comme les trimètres, et les anapestes ne commencent qu'à la ligne suivante (image, f. 177r). L'entrée de s00 pour 1226 supprime l'étiquette et ramène le renfoncement à 0 ; il reste à retirer `findent=1.8em` dans `texte.tex`. Point à mentionner dans le commentaire critique, car il corrige l'édition antérieure.
- **1227-1231 : système anapestique, an.** Ainsi White, p. 450 et § 291 (« non-antistrophic period », tétramètre et pentamètre) ; Prato, p. 356 (« metri anapestici ») ; Mazon, p. 136 (« court système anapestique ») ; Muff, p. 165 (« ein anapästisches System, vom Chore gesungen ») ; Sommerstein, n. *ad* 1227-31 (« anapaestic »). Désaccord : Schroeder, p. 67, y voit deux tétramètres de la coryphée (« Clauditur fabula duobus coryphaeae tetrametris anapaesticis »).
- **Colométrie de 1227-1231.** R écrit ἀλλὰ πέπ(αισται) μετρίως ἡμῖν ὥσθ' ὥρα δή 'στι βαδίζειν sur une seule ligne, à la marge : c'est un tétramètre catalectique, dimètre et parémiaque. Suivent, en retrait, οἴκαδ' ἑκάστη | τὼ Θεσμοφόρω δ' ἡμῖν ἀγαθὴν | τούτων χάριν ἀνταδοῖτον. Les cinq rangées de l'auteur sont celles de Hall–Geldart (dimètre, parémiaque, dimètre, monomètre, parémiaque). Elles coupent après Θεσμοφόρω δ', alors que R coupe après ἑκάστη, à la fin de la phrase. La coupe de R vaut d'être signalée à s18. L'étiquette « an. » ne dépend pas de ce choix.

## 5. Désaccords des autorités (synthèse)

| Passage | Point | Positions |
|---|---|---|
| 295-311 | prose entière ou acclamations en vers | prose : Σ R, White, Mazon, Prato, l'auteur ; εὐφημία ἔστω ×2 en vers : Conradt ; acclamations scandées : Schroeder |
| 531-573 | un seul mode ou deux | une seule étiquette (mètre unique) ; White et Prato distinguent 531-532 + 571-573 (récitatif) de 533-570 (« melodramatic ») |
| 659-662 | tétramètres isolés ou début de la période 659-666 | tétramètres récités : Mazon, Muff, Prato, Sommerstein ; période unique 659-666 : White § 221 |
| 728-775 | une ou deux séries | une série (Prato) ; deux unités dramatiques (White, Mazon) : sans effet sur l'étiquette |
| 947-952 | récités ou première période du stasimon | récités : Zimmermann, Muff ; période du stasimon : White § 589 |
| 1226 | anapestes ou trimètre | trimètre : White, Prato, Muff, R ; anapestes : édition antérieure de l'auteur |
| 1227-1231 | système ou deux tétramètres | système : White, Prato, Mazon, Muff, Sommerstein ; deux tétramètres : Schroeder |

## 6. Numérotation de texte.tex et clés

`texte.tex` suit la numérotation de Hall–Geldart (texte Perseus, `.sources/corpus/thesmo_hall_geldart.tsv`), avec ses particularités. Pour les clés de s00, cela donne :
- 373 = 372 usuel ;
- 686 = 687 ;
- 688 *suite* = 689 ;
- 1015 = 1014 (rangée sans étiquette ici).

Autres particularités relevées en passant :
- la rangée sans `n=` qui suit 379 est le v. 379 usuel ;
- les rangées en double de la prose (295, 297, 302, 307) ;
- 914 = 913-914 ;
- 23 et 500 sont absents : l'auteur les supprime (23 avec Willems, 500 avec van Herwerden). Il supprime aussi le v. 1187ᵃ de Hall–Geldart, avec Ellebodius.

Le champ `v_usuel` permettra de reporter les clés si `texte.tex` est renuméroté selon Coulon et Wilson.

## 7. Problèmes et recommandations

1. **s10, rangée (688, b) = v. 689** : ajouter `"etiquette": "ia³"` à l'entrée de `s10_689-727.json`. L'autre solution est d'adapter le script (point 3). Sans cela, les trimètres 689-698 n'ont pas d'étiquette.
2. **Harmonisation des étiquettes de s10** : « tr⁴ » → « tr⁴∧ » (702, 714, 726) et « ia³ cat. » → « ia³∧ » (717), comme dans s09, s12 et s00.
3. **`outils/extraction/appliquer_metrique.py`** :
   - (a) quand l'entrée de section n'a pas d'étiquette, reprendre celle de s00 au lieu de l'écraser ;
   - (b) ne poser l'étiquette que sur la première rangée qui porte la clé : sinon la rangée sans `n=` qui suit 295 reçoit « prose » une seconde fois ;
   - (c) traiter les parties « a », déjà demandé par s01, s02, s08 et s10.
4. **`texte.tex`** :
   - 1226 : retirer `findent=1.8em`, l'entrée de s00 ramenant `indent` à 0 ;
   - 612 : en faire une rangée numérotée et non une `suite` de 611 ;
   - numéroter les rangées de la prose 295-311 d'après l'édition antérieure (296 pour le second εὐφημία ἔστω, etc.), ce qui résout aussi le point 3 (b).
5. **Recension** (`recherche/metrique_structure.md`, § 4.1) : nuancer « pas de scholies métriques ». R a les scholies métriques 295, 531 et 547 sur des parties récitées (§ 3).
6. **Pour le commentaire critique et l'établissement du texte** :
   - 948 : παραχώρει, absent de R et de Hall–Geldart, rend le tétramètre faux (§ 4.11) ;
   - 1226 (trimètre, contre l'étiquette de l'édition antérieure) ;
   - 547 (anapeste au septième pied, que Σ R signale et recommande de garder) ;
   - 1216 (vers incomplet dans le texte de l'auteur ; s18) ;
   - 1227-1231 (coupe de R après ἑκάστη).

## 8. Sources consultées

- **R** : images du dossier Ravennas, ff. 166r, 168v et 177r. Découpes : `.travail/metrique/s00/f166r_*.png`, `f168v_547.png`, `f177r_1222-1231.png`, et `.travail/metrique/s07/R_f168v_marge531.png`.
- **F. Dübner**, *Scholia Graeca in Aristophanem*, Paris 1842, p. 266 (Σ 295) et 268 (Σ 531, Σ 547) : lu sur l'image (`.sources/web/editions/1842_Paris_Dubner_scholia/`, index PDF 344 et 346).
- **J. W. White**, *The Verse of Greek Comedy*, London 1912, « Table of Structure and Rhythms », p. 447-450 (texte archive.org ; p. 448 contrôlée sur l'image) ; §§ 221, 291, 589 d'après la même source.
- **C. Prato**, *Aristofane. Le donne alle Tesmoforie*, Milano 2001, « Appendice metrica », p. 345-356 : lu sur les images (`.sources/drive/editions_commentaires/prato2001_ocr/pages/idx431-442.png`).
- **P. Mazon**, *Essai sur la composition des comédies d'Aristophane*, Paris 1904, p. 127-136 (texte archive.org ; p. 133 contrôlée sur l'image).
- **Chr. Muff**, *Über den Vortrag der chorischen Partieen bei Aristophanes*, Halle 1872, p. 162-165.
- **O. Schroeder**, *Aristophanis cantica*, Lipsiae 1909, p. 59, 61, 63 (image), 64, 67.
- **C. Conradt**, *Die metrische und rhythmische Komposition der Komödien des Aristophanes* I, Greifenberg 1910, p. 50 (index PDF 49).
- **B. Zimmermann**, *Untersuchungen zur Form und dramatischen Technik der Aristophanischen Komödien* III, Frankfurt 1987, p. 75.
- **A. H. Sommerstein**, *Aristophanes. Thesmophoriazusae*, Warminster 1994 : notes « Metre » *ad* 381-2, 531-573, 655-8, 659-666, 687-8, 702-6, 726-7, 785-845, 947-952, 1065-97, 1227-31. Lu dans l'extrait textuel sans pagination (`.sources/drive/ravennas/Sommerstein_1994_Thesm_textrep.txt`) ; cité par lemme, non par page.
- **Hall–Geldart 1907** (texte Perseus) pour la numérotation.
- **Édition antérieure de l'auteur** (`latex/Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `… vv 642-fin-bis.tex`) : étiquettes `\typeVers`, apparat et commentaire.
- **Données des autres sections** : `s01`, `s09`, `s10`, `s12` (collisions de clés) et `s10_689-727.md`, § 7 (étiquette de 689 laissée à la décision d'ensemble).
