# Format de la transcription diplomatique du *Ravennas* (DiploXML, v1)

Un fichier par page : `ravennas/transcription/fXXX.xml` (ex. `f162v.xml`). Format XML
inspiré de la TEI (noms d'éléments francisés, sous-ensemble réduit), converti en LaTeX
par `outils/transcription/xml_vers_latex.py`, vérifié par les fonctions `valider`
(erreurs) et `avertir` (écarts au guide) de `outils/transcription/diploxml.py`.

Ce fichier donne la **syntaxe**. Les **règles de lecture et de décision** (quelle main,
quel signe, quel encodage dans chaque cas) sont dans `ravennas/GUIDE_TRANSCRIPTION.md`,
qui prévaut en cas de doute. La v1 reste compatible avec les brouillons en v0 : tout
fichier v0 valide reste valide.

## Mains

Étiquettes définitives (étude graphologique, chapitre 1, § 9 ; critères : guide, § 1).

| étiquette | main | littérature |
|---|---|---|
| `R1` | T, le copiste du texte | T (Allen), I m. (Velsen 1871) |
| `R1c` | T qui se corrige (en écrivant ou en relisant), même module, même encre | — |
| `R2` | S2, scholiaste et correcteur ancien : scholies, gloses, sigles à lettre suscrite, vers suppléés, suscriptions | S2 (Orsini), B (Allen), R² (Velsen 1883, Martin 1882), schol. m. (Velsen 1871) |
| `R3` | correcteur ancien à l'encre brun-noir, antérieur à G (S2 dans une autre campagne ?) : vv. 646, 939 sûrs ; 493, 874 probables | Rⁿ (chap. 4) ; R³ « paullo recentior » (Velsen 1883, préface), défini ici par l'encre |
| `Rsch` | main M, troisième main ancienne en minuscule : deux scholies de la marge intérieure du f. 162v (vv. 27, 30–32), et rien d'autre | 3e main d'Orsini 2011, 327 n. 24 |
| `Rrec` | campagne de 1516 (préparation de la Juntine) : sigles imprimables, encre orangée, barres, signes d'insertion | 2 m. (Velsen 1871), manus recens (van Leeuwen) |
| `Rmod` | mains modernes (foliotations, signature, crayons) | — |
| `R?` | main indéterminée | — |

Deux attributs précisent une main, sur tout élément qui porte `main` :

- `repasse="Rrec"` : tracé de `main` repassé en 1516 (note de forme S2 à l'encre orangée) ;
- `instrument="mine"` ou `"crayon"` : matière autre que l'encre (repères de 1516, crayons).

## Principes

- **Ce que montre le manuscrit, et seulement cela** : orthographe, accents, esprits,
  iota adscrit (ou son absence), ponctuation, élisions telles qu'écrites, même fautives.
- **Lettres** : minuscules, sans majuscule ni distinction des allographes (Η, « h » et
  « н » = η ; Ν = ν ; Є = ε). **σ partout, même en finale** : T n'a pas de ς (chap. 2, § 3).
  **Jamais d'iota souscrit** : ι sur la ligne, s'il est écrit.
- **Coupe des mots** : celle de R quand elle est nette ; règle des trois zones au guide, § 2.7.
- **Une ligne d'écriture du manuscrit = un élément `<l>`**, dans l'ordre de la page, y
  compris titres, hypothesis et lignes de chant coupées. Une réglure laissée vide n'est
  pas une `<l>` : elle se signale dans `<notes>`.
- **Doute** : toute lettre douteuse est dans `<unclear>` ; rien n'est « deviné » sans balise.
- **Caractères** : NFC ; `·` U+00B7, `;` U+003B, `:` U+003A (dicolon), `,` U+002C,
  `—` U+2014, `÷` U+00F7, apostrophe `᾽` U+1FBD.

## Structure

```xml
<page folio="162v" image="01_f162v_classense164v_vv0001-0042.jpg" vers="1-42">
  <lignes>
    <l n="1" zone="titre"><signe type="ornement">⁜</signe> ἀριστοφάνουσ· ·θεσμοφοριάζουσαι <signe type="ornement">—</signe></l>
    <l n="2" v="1"><parag/>ὦ ζεῦ· χελιδὼν ἀρ ἀπό τε φανήσεται·</l>
    <l n="3" v="2">ἀπολεῖ μ᾽ αλοῶν …</l>
  </lignes>
  <scholies>
    <sch n="1" ancre="2" place="mg-g" main="R2" lemme="ὦ ζεῦ χελιδών">…</sch>
  </scholies>
  <notes>
    <note ligne="3">Remarque du transcripteur (encre, doute, état du parchemin…)</note>
  </notes>
</page>
```

(Le titre de la pièce est de T, à l'encre du texte : **aucun `<hi rend="rouge">`** dans les
*Thesmophories*. Les valeurs de cet exemple illustrent la syntaxe ; f. 162v : voir l'image.)

Attributs de `<l>` : `n` (rang de la ligne **d'écriture** sur la page, à partir de 1,
réglures vides non comptées, comme dans les inventaires), `v` (vers qui commencent sur
la ligne, numérotation usuelle de Brunck, colonne `usuel` de `edition/donnees/concordance_vers.tsv` :
« 6 », « 6,7 », « 439a » ; vide pour une ligne qui continue un vers ou qui n'est pas un vers),
`zone` (`texte` par
défaut, `titre`, `hypothesis`, `marge-sup`, `marge-inf`), `retrait` (renfoncement, en
unités de 25 px ; **négatif pour une saillie**, ekthesis), `main` (si la ligne entière
est d'une autre main), `repasse`.

Attributs de `<sch>` : `n`, `ancre` (numéro de la ligne `<l>` en face de laquelle elle
commence), `place` (`mg-g`, `mg-d`, `mg-sup`, `mg-inf`, `interl`, `col` : dans un blanc de
la colonne ; gauche et droite physiques, non intérieure et extérieure), `main`,
`repasse`, `lemme` (lemme écrit par le scholiaste, s'il y en a un).

## Éléments en ligne (dans `<l>` et `<sch>`)

| élément | sens | exemple |
|---|---|---|
| `<nota main="R2">κη<hi rend="sus">δ</hi></nota>` | sigle de personnage (*nota personae*) ou note de personnage à sa place | `<nota main="R2" repasse="Rrec">…</nota>` |
| `<parag/>` | paragraphos ; toujours avant le `<nota>` de la même ligne | `<del type="biffure" main="Rrec"><parag/></del>` |
| `<add place="dessus" main="R2">ε</add>` | ajout d'un correcteur (`dessus`, `dessous`, `ligne`, `mg-g`, `mg-d`) | vers suppléé : `<add place="mg-d" main="R2">…</add>` |
| `<hi rend="sus">σ</hi>` | lettre écrite au-dessus de la ligne **sans être un ajout** : abréviation, sigle, lettre finale surélevée | `<abbr dev="σί">φ<hi rend="sus">η</hi></abbr>` |
| `<del type="grattage" main="R?"/>` | suppression (`grattage`, `biffure`, `exponctuation`, `surcharge`) ; contenu lisible, ou `<gap/>`, ou vide | |
| `<subst main="R2"><del type="surcharge">ο</del><add place="ligne">ω</add></subst>` | substitution ; un accent corrigé se traite au niveau de la lettre | |
| `<ras main="R3">ἥκει πάλιν</ras>` | écrit sur grattage (*in rasura*) | |
| `<unclear cert="faible">α</unclear>` | lecture douteuse (`moyenne` : probable ; `faible` : hypothèse parmi d'autres) | |
| `<gap n="3" unite="lettres" raison="illisible"/>` | lettres illisibles ou perdues (`raison` : `illisible`, `grattage`, `tache`, `reliure`, `surcharge`) | |
| `<abbr dev="αί">κ</abbr>` | suspension : lettres écrites, plus `dev` = lettres suppléées | κ(αί) |
| `<abbr signe="ʒ" dev="δέ"/>` | compendium : `signe` = forme du signe, **imprimée** ; `dev` = tout le mot ou toute la syllabe, imprimés en gris | ʒ(δέ) |
| `<gl sur="χοάνης" main="R2">χώνης</gl>` | glose au-dessus du mot `sur` (rare : voir le guide, § 2.11) | |
| `<hi rend="grand">…</hi>` | mise en valeur (`grand` : initiale agrandie, `monogramme`, `sus`, voir plus haut) | |
| `<sp n="2"/>` | blanc laissé par le copiste (`n` = largeur en lettres) | |
| `<signe type="renvoi" main="R2">∈</signe>` | signe (`renvoi`, `insertion`, `signal`, `transposition`, `ornement`, `repere`, `coronis`, `diple`, `autre`) ; `repere` n'est pas imprimé | |
| `<corr lire="ἆρά ποτε" type="coupe">ἀρ ἀπό τε</corr>` | **couche de correction, posée après la vérification** (jamais par les lecteurs ni l'arbitre) : le contenu reste la leçon de R, le livre imprime `lire` ; `type` : `accent`, `coupe`, `faute` ; ne s'applique qu'à du texte nu | ἆρά ποτε |
| `<lb/>`, `<lb coupe="oui"/>` | fin de ligne dans une scholie ou un vers suppléé ; `coupe` : à l'intérieur d'un mot | |
| `<note>…</note>` | (dans `<notes>` seulement) remarque du transcripteur | |

## Rendu LaTeX (aperçu)

Couleur de la main pour tout ce qui n'est pas de `R1` ; ajouts au-dessus en petit corps ;
`⟦ ⟧` pour le gratté ; texte barré pour la biffure ; point souscrit pour le douteux ;
parenthèses pour les abréviations ; sigles et paragraphoi dans la colonne de gauche ;
scholies dans la colonne des scholies, à la hauteur de leur ligne d'ancrage. Les attributs
`repasse` et `instrument` sont conservés dans les données ; leur rendu (pointillé orange
brûlé, chap. 1, § 9.4) reste à ajouter à `edition/thesmo.cls`, comme la palette du même
paragraphe.
