# Corpus numériques de la littérature grecque — couverture, fiabilité, lacunes

*Document de travail du chantier « corpus » (octobre 2026). Les textes sont dans
`.sources/corpus/` (non versionné) ; les scripts et leur notice dans `outils/corpus/`
([README](../outils/corpus/README.md)). Statistiques : voir § 6 (mises à jour à chaque
reconstruction de l'index).*

Objet : disposer en local d'un corpus aussi large que possible des textes grecs (auteurs,
lexicographes, parémiographes, scholiastes, fragments) et d'un moteur de recherche
(`outils/corpus/chercher.py`) pour **trouver** loci paralleli et testimonia des
*Thesmophories*, puis les **vérifier**. L'index ne remplace jamais l'édition : toute
référence se contrôle sur l'imprimé (ou sur l'image de la page, lien fourni pour l'OCR).

## 1. Méthode

1. Reprise de l'existant après l'interruption : dépôts git complets et propres
   (Perseus, First1KGreek, LSJ, DCLP), Diorisis décompressé (820 fichiers), 20 ouvrages
   OCR d'archive.org intègres (gzip et JSON vérifiés) ; index partiel abandonné et
   reconstruit.
2. Contrôle de la qualité de chaque OCR (part des mots grecs de 4 lettres et plus
   attestés dans les textes TEI) : archive.org n'a souvent appliqué qu'une langue par
   volume, si bien que le grec des volumes « latins » (CPG I, Pollux de Bethe I, Mélanges
   de Miller, Anecdota de Bekker) est du charabia. Ces exemplaires ont été remplacés par
   d'autres numérisations mieux lues, ou réocérisés localement (Tesseract grc+lat).
3. Pages à deux colonnes serrées (Hésychius, Souda de Bekker, Zonaras, scholies de
   Dübner) : l'OCR fusionnait les lignes des deux colonnes ; l'ordre de lecture est
   rétabli d'après les coordonnées des mots (hOCR), puis les lexiques sont découpés en
   articles (référence « col. 199, s.v. ἀπόκυνον »).
4. Index SQLite FTS5 sur 8 processus : texte original + forme normalisée (sans
   diacritiques, minuscules, σ = ς, apostrophes et coronis supprimées) ; jointures entre
   passages consécutifs (expressions à cheval sur deux vers) ; index « souple » de l'OCR
   neutralisant les confusions systématiques (κ lu χ, lettres latines au milieu des mots
   grecs, ς final lu ζ) ; étiquette de fiabilité par œuvre.

## 2. Corpus disponibles

### 2.1 Textes établis (TEI, numérisations corrigées)

| Corpus | Contenu | Licence |
|---|---|---|
| Perseus, `canonical-greekLit` | 814 éditions grecques (poésie, théâtre complet, histoire, philosophie, orateurs, Athénée de Kaibel avec pages de Casaubon, Harpocration…) | CC BY-SA 4.0 |
| Open Greek and Latin, `First1KGreek` | 1 126 éditions : Souda (Adler, incomplète, voir § 3), CPG I (Zénobius, Diogénien, Plutarque, Grégoire de Chypre, Appendix), scholies (Euripide, Sophocle, Homère, Pindare, Lucien, Nicandre, Isocrate), Hérodien, Ammonius, patristique… | CC BY-SA 4.0 |
| LSJ (Perseus) | Liddell–Scott–Jones, 9e éd., entrée par entrée | CC BY-SA 4.0 |
| DCLP (papyri.info) | papyrus littéraires et paralittéraires (EpiDoc), texte et métadonnées | CC BY 3.0 |
| Diorisis | corpus lemmatisé (10 millions de mots) : table forme → lemme pour la recherche `--lemme` | CC BY 4.0 |

### 2.2 Ouvrages du domaine public, OCR (archive.org ou local)

Liste maintenue dans `outils/corpus/sources_ocr.tsv` (identifiant, sigle, description,
options). Taux = part des mots grecs reconnus (voir § 4).

| Domaine | Ouvrages |
|---|---|
| Lexiques | Hésychius, éd. minor de M. Schmidt (1867), en articles ; Souda, éd. Bekker (1854), en articles ; Photius, éd. Porson (1822) et Naber (1864–1865) ; Pollux, éd. Dindorf (1824, texte complet) et Bethe II (l. VI–X, 1931) ; Etymologicum magnum (Sylburg, réimpr. 1816) ; Zonaras, éd. Tittmann I (1808) ; Lexica Segueriana (Bekker, *Anecdota* I, 1814 : Antiatticiste, Λέξεις ῥητορικαί, Συναγωγή…, OCR local) |
| Parémiographes | CPG I (avec les notes) et II (Leutsch–Schneidewin, 1839–1851) ; Gaisford, *Paroemiographi* (1836) ; Miller, *Mélanges* (1868 : Zénobius de l'Athous) |
| Florilèges | Stobée, *Florilegium* (Meineke, 1855–1857) ; *Anthologium* III (Hense, 1894) |
| Scholies | Dübner, *Scholia Graeca in Aristophanem* (1842) ; Rutherford, *Scholia Aristophanica* I–II (1896 : scholies du Ravennas) ; A. Martin, *Les scolies du manuscrit d'Aristophane à Ravenne* (1882) |
| Fragments | Kock, CAF I–III ; Meineke, FCG I–IV ; Kaibel, CGF I.1 ; Nauck, TGF² (1889) ; Bergk, PLG⁴ II–III (élégiaques, iambographes, méliques, 1882) |
| Éditions, commentaires | Hall–Geldart II (1907) ; Fritzsche (1838) ; Velsen (1883) |

### 2.3 PDF du Drive de l'auteur (usage local, sous droits)

`outils/corpus/sources_drive.py` dresse, à partir de la sélection du chantier Drive, la
liste (non versionnée) des éditions modernes à indexer par leur couche texte :
Hésychius de Latte–Hansen–Cunningham, Photius de Theodoridis, Souda d'Adler, Pollux de
Bethe, CPG, Kassel–Austin (PCG), TrGF, scholies de Groningue, Zonaras, Synagoge,
Harpocration (Keaney), Moeris (Hansen), Phrynichus (Fischer), Tosi… Seuls les fichiers
déjà téléchargés sont indexés (collection « drive ») ; les PDF dont le grec est illisible
(police non Unicode, OCR latin) sont écartés automatiquement. Relancer
`sources_drive.py` puis `indexer.py` quand le téléchargement du Drive aura avancé.

## 3. Couverture des fonds prioritaires

*(à compléter)*

## 4. Fiabilité

*(à compléter)*

## 5. Lacunes et pistes

*(à compléter)*

## 6. Statistiques de l'index et tests

*(à compléter)*
