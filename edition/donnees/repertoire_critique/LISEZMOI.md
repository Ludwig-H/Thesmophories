# Répertoire critique des *Thesmophories*

Relevé, vers par vers, de ce que les éditions et les collations rapportent : leçons de R
(et de ses correcteurs), de la Juntine et des autres imprimés, papyri, testimonia, et
toutes les conjectures avec leur auteur et le lieu où elles ont été publiées.

Un fichier JSONL par édition et par tranche de vers : `<edition>_<v0>-<v1>.jsonl`, une
entrée par ligne :

```json
{"v": "18", "lemme": "ἀκοὴν δὲ χοάνης", "lecon": "ἀκοῆς δὲ χοάνην", "type": "conjecture",
 "auteurs": ["Biset"], "temoins": [], "adoptee_par_edition": false,
 "edition": "Velsen 1883", "page": "p. 3 (PDF 21)", "citation": "ἀκοῆς δὲ χοάνην Bisetus",
 "remarque": ""}
```

- `type` : `R` (leçon de R ou d'un correcteur, à préciser dans `temoins` : R, R^ac, R^pc, R², Rγρ…),
  `imprime` (Juntine, Aldine…), `papyrus`, `testimonium`, `scholie`, `conjecture`,
  `deletion`, `transposition`, `lacune`, `attribution` (répartition des répliques),
  `ponctuation`, `note` (remarque de l'éditeur sans leçon).
- `citation` : transcription fidèle de l'entrée de l'apparat (latin ou autre), pour contrôle.
- `adoptee_par_edition` : l'édition imprime-t-elle cette leçon dans son texte ?

La fusion par vers (avec résolution des attributions contradictoires) est dans
`repertoire_critique.json` (produit ultérieurement).
