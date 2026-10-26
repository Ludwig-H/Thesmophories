# Format de la transcription diplomatique du *Ravennas* (DiploXML, v0)

Un fichier par page : `ravennas/transcription/fXXX.xml` (ex. `f162v.xml`). Format XML
inspiré de la TEI (noms d'éléments francisés, sous-ensemble réduit), converti en LaTeX
par `outils/transcription/xml_vers_latex.py`, et vérifié par
la fonction `valider` de `outils/transcription/diploxml.py`. Les mains (`main="…"`) sont
définies par l'étude graphologique (`ravennas/graphologie/`, `ravennas/GUIDE_TRANSCRIPTION.md`) ;
étiquettes à employer (correspondance avec la littérature : `recherche/ravennas_dossier.md`) :

| étiquette | main | littérature |
|---|---|---|
| `R1` | le copiste du texte | T (Allen), I m. (Velsen) |
| `R1c` | correction du copiste lui-même (en écrivant ou en relisant) | — |
| `R2` | la main des scholies des *Thesmophories*, correcteur ancien (Xe s.) : vers omis ajoutés, sigles de personnages | S2 (Orsini), B (Allen), R² (Velsen 1883), schol. m. (Velsen 1871) |
| `R3` | autre main médiévale (troisième main contemporaine ? « paullo recentior » de Velsen) | R³ (Velsen 1883) |
| `Rsch` | main de scholies distincte de R2 (si l'image l'impose) | — |
| `Rrec` | main du XVIe siècle (préparation de l'impression de 1516 : sigles « imprimables », chiffres et traits renvoyant à la Juntine, grattages de signes) ; imprimée R^XVI | 2 m. (Velsen 1871), « Boninus » |
| `Rmod` | main moderne (XVIIIe–XIXe s. : corrections, crayon, foliotation) | — |
| `R?` | main indéterminable | — |

## Principes

- **Ce que montre le manuscrit, et seulement cela** : orthographe, accents, esprits,
  iota adscrit (ou son absence), ponctuation, élisions telles qu'écrites, même fautives.
- **Lettres** : formes normalisées (σ médian / ς final selon la position ; pas de
  distinction des allographes). **Coupe des mots** : normalisée, sauf si elle importe à une
  leçon (le signaler en `<note>`).
- **Une ligne du manuscrit = un élément `<l>`**, dans l'ordre de la page, y compris titres,
  hypothesis, listes de personnages et lignes de chant coupées.
- **Doute** : toute lettre douteuse est dans `<unclear>` ; rien n'est « deviné » sans
  balise.

## Structure

```xml
<page folio="162v" image="01_f162v_classense164v_vv0001-0042.jpg" vers="1-42">
  <lignes>
    <l n="1" zone="titre"><hi rend="rouge">ἀριστοφάνους θεσμοφοριάζουσαι</hi></l>
    <l n="2" v="1"><nota main="R1">κη</nota>ὦ ζεῦ χελιδὼν ἆρα πότε φανήσεται·</l>
    <l n="3" v="2">ἀπολεῖ μ' ἀλοῶν …</l>
  </lignes>
  <scholies>
    <sch n="1" ancre="2" place="mg-g" main="R1" lemme="ὦ ζεῦ χελιδών">…</sch>
  </scholies>
  <notes>
    <note ligne="3">Remarque du transcripteur (encre, doute, état du parchemin…)</note>
  </notes>
</page>
```

Attributs de `<l>` : `n` (numéro de ligne sur la page, à partir de 1), `v` (vers qui
commencent sur la ligne : « 6 », « 6,7 »), `zone` (`texte` par défaut, `titre`,
`hypothesis`, `personnages`, `marge-sup`, `marge-inf`), `retrait` (renfoncement en
nombre de lettres), `main` (si la ligne entière est d'une autre main).

Attributs de `<sch>` : `n`, `ancre` (numéro de la ligne `<l>` en face de laquelle elle
commence), `place` (`mg-g`, `mg-d`, `mg-sup`, `mg-inf`, `interl`), `main`, `lemme`
(lemme écrit par le scholiaste, s'il y en a un).

## Éléments en ligne (dans `<l>` et `<sch>`)

| élément | sens | exemple |
|---|---|---|
| `<nota main="R1">κη</nota>` | sigle de personnage (*nota personae*) | `<nota>ευ</nota>` |
| `<parag/>` | paragraphos (trait sous le début de ligne) | |
| `<add place="dessus" main="R2">ε</add>` | ajout (`dessus`, `dessous`, `ligne`, `mg-g`, `mg-d`) | |
| `<del type="grattage" main="R2">ι</del>` | suppression (`grattage`, `biffure`, `exponctuation`, `surcharge`) ; contenu vide ou `<gap/>` si illisible | |
| `<subst main="R2"><del type="surcharge">ο</del><add place="ligne">ω</add></subst>` | correction par substitution | |
| `<ras main="R1">ᾗ</ras>` | écrit sur grattage (*in rasura*) | |
| `<unclear cert="faible">α</unclear>` | lecture douteuse (`cert` : `faible`, `moyenne`) | |
| `<gap n="3" unite="lettres" raison="illisible"/>` | lettres illisibles ou perdues | |
| `<abbr dev="αί">κ</abbr>` | abréviation : `dev` = lettres suppléées, imprimées entre parenthèses | κ(αί) |
| `<gl sur="χοάνης" main="R1">χώνης</gl>` | glose interlinéaire au-dessus du mot `sur` | |
| `<hi rend="rouge">…</hi>` | mise en valeur (`rouge`, `grand`, `monogramme`) | |
| `<sp n="2"/>` | blanc laissé par le copiste | |
| `<signe type="renvoi">⁙</signe>` | signe (`renvoi`, `transposition`, `coronis`, `diple`, `autre`) | |
| `<note>…</note>` | (dans `<notes>` seulement) remarque du transcripteur | |

## Rendu LaTeX (aperçu)

Couleur de la main pour tout ce qui n'est pas de `R1` ; ajouts au-dessus en petit corps ;
`⟦ ⟧` pour le gratté ; texte barré pour la biffure ; point souscrit pour le douteux ;
parenthèses pour les abréviations ; sigles et paragraphoi dans la colonne de gauche ;
scholies dans la colonne des scholies, à la hauteur de leur ligne d'ancrage.
