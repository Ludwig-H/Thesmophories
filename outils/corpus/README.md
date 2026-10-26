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
| `sources_drive.py` | dresse la liste locale (non versionnée) des PDF du Drive de l'auteur à indexer |
| `indexer.py` | construit `.sources/corpus/index.sqlite` (SQLite FTS5), sur 8 processus |
| `chercher.py` | recherche (mots, expressions, préfixes, NEAR, filtres, contexte, JSON) |
| `exporter_vulgate.py` | exporte les *Thesmophories* de Perseus (Hall–Geldart) vers par vers : `.sources/corpus/thesmo_hall_geldart.tsv` |
| `grec.py` | normalisation, « pliage » OCR, conversion du Beta Code |
| `abreviations.tsv` | abréviations d'auteurs et d'œuvres pour l'affichage (« Eur. Hel. 255 ») |

## Installation

Python 3 avec `lxml` (et `pymupdf` pour les PDF du Drive), `git`, accès réseau. Place
disque : environ 5 Go pour les textes (dont 2,5 Go pour Diorisis décompressé) et 2 à 3 Go
pour l'index.

## Construire ou mettre à jour

Dans l'ordre (chaque étape réutilise ce qui est déjà présent ; tout est relançable après
une interruption) :

```sh
python3 outils/corpus/telecharger.py            # --maj pour mettre à jour les dépôts git
python3 outils/corpus/hocr_colonnes.py --tous   # pages à deux colonnes (télécharge les hOCR)
python3 outils/corpus/sources_drive.py          # si le Drive a été (re)téléchargé
python3 outils/corpus/indexer.py                # ≈ 15 min sur 8 processus
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
# toutes les formes d'un lemme chez les comiques et les lexicographes
python3 outils/corpus/chercher.py --lemme 'χελιδών' -a Ar. -c 1
# vérification diacritique stricte
python3 outils/corpus/chercher.py 'ὀρθρογόη' --exact
```

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
