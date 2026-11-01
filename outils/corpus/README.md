# Corpus grec local et moteur de recherche

Outils pour **trouver puis vérifier** loci paralleli et testimonia des *Thesmophories* dans
un corpus local de la littérature grecque (auteurs, lexicographes, parémiographes,
scholiastes). Les textes et l'index sont dans `.sources/corpus/` (non versionné) ; seuls
les scripts et cette notice sont versionnés. Bilan de la couverture et de la fiabilité :
[`recherche/corpus_numeriques.md`](../../recherche/corpus_numeriques.md).

> **Règle d'usage.** L'index sert à *trouver*. Une référence ne se cite qu'après
> vérification sur l'édition imprimée (ou sur l'image de la page pour l'OCR, lien fourni
> par `chercher.py`). Les numérisations TEI elles-mêmes contiennent des coquilles
> (Perseus, *Thesm.* 4 : « πυφέσθαι » pour πυθέσθαι).

## Fichiers

| Fichier | Rôle |
|---|---|
| `telecharger.py` | collecte : dépôts git (Perseus, First1KGreek, LSJ, DCLP), Diorisis, OCR archive.org |
| `sources_ocr.tsv` | ouvrages du domaine public pris sur archive.org (OCR), avec options de mise en page |
| `hocr_colonnes.py` | rétablit l'ordre de lecture des pages à deux colonnes d'après le hOCR (Hésychius, Souda, Zonaras, Dübner) |
| `adler.py` | Souda d'Adler (OCR archive.org, `.sources/web/testimonia/adler/`) : pages rangées pour l'index, doubles pages du t. III séparées |
| `kleinlogel.py`, `kleinlogel.tsv` | polices Kleinlogel des éditions De Gruyter : table glyphe → caractère (sans texte des éditions), réécriture du /ToUnicode en mémoire |
| `ocr_hesychius.py` | Hésychius de Latte–Hansen–Cunningham : OCR reprenable, décodage des polices, découpage en gloses, qualité, tests, contrôle sur l'image |
| `sources_drive.py` | dresse la liste locale (non versionnée) des fichiers du Drive de l'auteur à indexer |
| `indexer.py` | construit `.sources/corpus/index.sqlite` (SQLite FTS5), sur 8 processus |
| `chercher.py` | recherche (mots, expressions, préfixes, NEAR, filtres, contexte, JSON) |
| `exporter_vulgate.py` | exporte les *Thesmophories* de Perseus (Hall–Geldart) vers par vers : `.sources/corpus/thesmo_hall_geldart.tsv` |
| `grec.py` | normalisation, « pliage » OCR, conversion du Beta Code |
| `abreviations.tsv` | abréviations d'auteurs et d'œuvres pour l'affichage (« Eur. Hel. 255 ») |

## Installation

Python 3 avec `lxml` (et, pour les PDF du Drive, `pymupdf` et `fonttools`), `git`, accès
réseau ; Tesseract 5 avec les modèles `grc` et `lat` pour l'OCR d'Hésychius. Place disque :
environ 5 Go pour les textes (dont 2,5 Go pour Diorisis décompressé) et 2 à 3 Go pour
l'index (6 Go libres exigés au lancement).

## Construire ou mettre à jour

Dans l'ordre (chaque étape réutilise ce qui est déjà présent ; tout est relançable après
une interruption) :

```sh
python3 outils/corpus/telecharger.py            # --maj pour mettre à jour les dépôts git
python3 outils/corpus/hocr_colonnes.py --tous   # pages à deux colonnes (télécharge les hOCR)
python3 outils/corpus/sources_drive.py          # si le Drive a été (re)téléchargé
python3 outils/corpus/ocr_hesychius.py ocr      # reprenable (2 465 pages, ≈ 1 h sur 8 processus)
python3 outils/corpus/ocr_hesychius.py decoder  # texte de l'éditeur, zone par zone (≈ 2 min)
python3 outils/corpus/ocr_hesychius.py gloses   # une glose par ligne, numéro et page
python3 outils/corpus/adler.py                  # si les volumes d'Adler sont présents
python3 outils/corpus/indexer.py                # ≈ 15 min sur 8 processus
python3 outils/corpus/ocr_hesychius.py qualite  # mesures (qualite.json)
python3 outils/corpus/ocr_hesychius.py tester   # gloses attendues, recherche/testimonia.md
python3 outils/corpus/tester.py                 # requêtes de contrôle de l'index
python3 outils/corpus/exporter_vulgate.py       # vulgate Hall–Geldart pour la collation
```

L'index est construit dans `index.sqlite.tmp` puis renommé : une recherche en cours n'est
jamais perturbée, et une construction interrompue se relance simplement.

**Ajouter un ouvrage OCR** : ajouter une ligne à `sources_ocr.tsv` (identifiant
archive.org, catégorie, sigle, description, options), lancer `telecharger.py ocr`, puis
`hocr_colonnes.py <identifiant>` si la mise en page est à deux colonnes, et réindexer.
Vérifier d'abord la qualité de l'OCR : archive.org n'a souvent reconnu qu'une langue par
livre, si bien que le grec d'un volume « latin » (ou le latin d'un volume « grec ») est
illisible ; choisir alors un autre exemplaire numérisé. Le taux de mots grecs reconnus
(`chercher.py --oeuvres …`) donne une première mesure.

## Chercher

```sh
python3 outils/corpus/chercher.py 'REQUÊTE' [options]
```

Les mots de la requête sont **normalisés comme l'index** : accents, esprits, tréma,
iota souscrit, apostrophes d'élision et coronis sont ignorés ; σ = ς ; majuscules =
minuscules ; variantes orthographiques ξυν-/συν-, ττ/σσ, ρρ/ρσ, γιγν-/γιν- admises.

| Syntaxe | Effet |
|---|---|
| `πυθοῦ χελιδών` | tous les mots dans le même passage (vers, section, article, page) |
| `"σοφοὶ τύραννοι"` | expression (mots consécutifs ; aussi à cheval sur deux vers ou deux pages) |
| `ὀρθρογ*` | préfixe |
| `χελιδών OR ἀηδών`, `NOT`, parenthèses | opérateurs booléens |
| `NEAR(πυθοῦ χελιδών, 3)` | proximité (au plus 3 mots entre les termes) |

| Option | Effet |
|---|---|
| `--exact` | respecter accents, esprits, iota souscrit (grave = aigu) : filtre appliqué après la recherche |
| `--sans-variantes` | refuser ξυν-/συν-, ττ/σσ, etc. |
| `--strict` | ne pas utiliser l'index « souple » de l'OCR (où χ = κ, lettres latines translittérées, ζ final = σ) |
| `--lemme` | étendre chaque mot à toutes ses formes attestées (table Diorisis) |
| `-a Eur`, `-o Hel` | filtres sur l'auteur et l'œuvre (abréviation, nom, numéro TLG, URN ; sans accents) |
| `--collection perseus first1k ocr lsj dclp drive`, `--sans-ocr` | filtres sur les collections |
| `--toutes-editions` | inclure les éditions secondaires d'une même œuvre (une seule par défaut) |
| `-c 2` | deux passages de contexte avant et après |
| `-n 200`, `--complet`, `--json` | nombre de résultats, passages entiers, sortie JSON |
| `--oeuvres Hsch`, `--stats` | œuvres indexées correspondant au motif ; statistiques |

Chaque résultat donne la **référence lisible** (« Eur. Hel. 1 », « Sud. α 1002 »,
« Hsch. (Schmidt min.) col. 199, s.v. ἀπόκυνον »), l'**URN** (CTS pour les textes TEI :
`urn:cts:greekLit:tlg0006.tlg014.perseus-grc2:1` ; `ia:<identifiant>#n<feuillet>` pour
l'OCR) et un lien (lecteur Scaife, page du scan sur archive.org, papyri.info). Pour l'OCR et
les PDF s'ajoute l'étiquette de fiabilité avec le taux de mots grecs reconnus.

### Exemples

```sh
# Eur. Hel. 1 et ses échos (Thesm. 855, scholies…)
python3 outils/corpus/chercher.py '"Νείλου μὲν αἵδε καλλιπάρθενοι ῥοαί"'
# un vers proverbial cité sous deux graphies (ξυν-/συν-)
python3 outils/corpus/chercher.py '"σοφοὶ τύραννοι τῶν σοφῶν ξυνουσίᾳ"'
# une glose d'Hésychius (OCR de Schmidt, article par article)
python3 outils/corpus/chercher.py 'ἀπόκυνον' -a Hsch
# une glose dans l'édition de référence (numéro de l'édition, page imprimée, signes de la marge)
python3 outils/corpus/chercher.py 'χοάνη' -a 'Hsch.' -o gloses
# son image et ses apparats, pour la citer
python3 outils/corpus/ocr_hesychius.py voir χ 576
# tout ce qu'Hésychius rapporte aux Thesmophories : texte des gloses, puis apparats
python3 outils/corpus/chercher.py 'Thesm' -a 'Hsch.' -o gloses -n 400
python3 outils/corpus/chercher.py 'Thesm' -a 'Hsch. app.' -n 400
# toutes les formes d'un lemme chez les comiques et les lexicographes
python3 outils/corpus/chercher.py --lemme 'χελιδών' -a Ar. -c 1
# vérification diacritique stricte
python3 outils/corpus/chercher.py 'ὀρθρογόη' --exact
```

## Hésychius : deux voies, une référence

Les PDF de Latte–Hansen–Cunningham sont vectoriels et composés en polices Kleinlogel, aux noms de
glyphes brouillés (couche texte : charabia). `ocr_hesychius.py` mène deux voies de front :
**OCR** Tesseract à 400 dpi (`ocr/`, page par page, reprenable, sert de contrôle) et **décodage**
des glyphes par `kleinlogel.tsv`, qui rend le texte exact de l'éditeur, accents compris : c'est lui
qui est indexé, et il n'est pas plié (pas de χ = κ dans ces œuvres).

| Œuvre de l'index | Passages | Référence |
|---|---|---|
| `Hsch.`, `abr_titre` « gloses, t. I » … « t. IV » | une glose ; pages liminaires à part | `Hsch. χ 576 (Hansen–Cunningham IV, p. 223)` ; la colonne `locuteur` porte les signes de la marge (`[D]`, `[Hom.]`…) |
| `Hsch. app.`, « apparats, t. I » … | testimonia et apparat de la glose | `Hsch. app. χ 576 (Hansen–Cunningham IV, p. 223)` |

La numérotation est celle de l'édition imprimée : celle de Latte pour α–ο, celle de Schmidt (ed. maior)
pour π–ω, que Hansen et Cunningham ont gardée. Les pages de t. I et II sont celles de la 2e édition
(Cunningham, 2018 et 2020), libellées « Latte I », « Latte II ». Dans la forme de recherche, les
signes éditoriaux sont retirés à l'intérieur des mots (`ὄρ⟨ρ⟩ος` se trouve par `ὄρρος`). Sorties
dans `.sources/corpus/hesychius/` : `ocr/`, `texte/`, `gloses.jsonl.gz`, `anomalies.tsv` (suite des
numéros), `qualite.json`, `controle_testimonia.tsv`.

## Structure de la base

- `oeuvres` : une ligne par édition (collection, URN, auteur, titre, abréviations,
  description de l'édition, fiabilité, taux de mots reconnus pour l'OCR, lien source) ;
- `passages` : texte original (NFC), forme normalisée, référence canonique, locuteur
  (théâtre), repère de page (Casaubon, Stephanus), cible (feuillet du scan) ;
- `passages_fts` (FTS5 sur la forme normalisée), `fenetres_fts` (jointures entre
  passages consécutifs), `souple_fts` (forme pliée de l'OCR et des PDF) ;
- `formes` (Diorisis : forme normalisée → lemme), `papyrus` (métadonnées DCLP),
  `collections`, `meta` (statistiques, erreurs, versions des dépôts).

On peut interroger la base directement avec `sqlite3 .sources/corpus/index.sqlite`.
