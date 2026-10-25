# Aristophane, *Les Thesmophories* — édition sur le *Ravennas*

Nouvelle édition philologique des *Thesmophories* (Θεσμοφοριάζουσαι), fondée sur le
seul témoin médiéval de la pièce, le *Ravennas* (Ravenne, Biblioteca Classense,
ms. 429, milieu du Xᵉ siècle, ff. 162v–177r) : transcription diplomatique, apparat,
*loci paralleli*, commentaire critique, texte établi, traduction et commentaire.

> **Chantier en cours** (octobre 2026). Le livre se compile déjà en entier ; la
> transcription diplomatique, l'apparat et les *loci paralleli* sont en préparation.

## Conception : une unité de quatre pages (et plus) par folio du manuscrit

1. **Double page I** — à gauche, la transcription la plus diplomatique possible de la
   page de R (disposition, sigles, corrections ; une couleur par main), l'apparat
   critique dans le prolongement des lignes, puis les *loci paralleli* et le
   commentaire critique ; à droite, le fac-similé de la page, aussi grand que possible.
2. **Double page(s) II** — à gauche, le texte grec établi (structure, mètres,
   scansion des parties chantées) ; à droite, la traduction (didascalies) ; au bas des
   deux pages, le commentaire de la pièce.

Format 230 × 310 mm, marges réduites ; polices libres : EB Garamond (français),
GFS Porson (grec établi), Cardo (transcription du manuscrit).

## Organisation du dépôt

| Dossier | Contenu |
|---|---|
| [`edition/`](edition/) | l'édition : classe LuaLaTeX `thesmo.cls`, document maître `thesmophories.tex`, un dossier par folio (`folios/fXXX/` : `diplo.tex`, `apparat.tex`, `paralleles.tex`, `critique.tex`, `texte.tex`, `commentaire.tex`), données (`donnees/`), [conventions](edition/CONVENTIONS.md) |
| [`ravennas/`](ravennas/) | le manuscrit : étude graphologique, segmentation des pages, transcription diplomatique (format XML : [spécification](ravennas/FORMAT_TRANSCRIPTION.md)) |
| [`recherche/`](recherche/) | recension : éditions et conjectures, dossier sur le manuscrit, scholies, papyri, testimonia, métrique, études, corpus numériques |
| [`outils/`](outils/) | scripts : images (recadrage, segmentation, versions améliorées), corpus grec local et moteur de recherche, extraction des travaux antérieurs, transcription |
| [`latex/`](latex/) | travaux antérieurs de l'auteur (texte, apparat, traduction, commentaire, introduction, annexes, index), source de la présente édition |
| [`pdf/`](pdf/) | PDF des versions antérieures |
| [`ravennas_1904_bnf/`](ravennas_1904_bnf/) | planches du fac-similé phototypique de 1904 (ff. 162v–163r), PDF complets du manuscrit, manifeste IIIF de la Classense |
| [`dossier_ravennas_thesmophories/`](dossier_ravennas_thesmophories/) | images haute définition des pages (`folios_individuels…`, `planches_doubles…`) ; les autres fichiers de ce dossier, produits par un précédent assistant, ne sont pas fiables (voir [l'audit](recherche/audit_gemini.md)) et seront archivés |

Les documents sous droits utilisés pour le travail (éditions et commentaires modernes,
etc.) ne sont pas versionnés.

## Compiler

```sh
outils/installer_environnement.sh     # une fois (TeX Live LuaTeX, outils Python)
edition/compiler.sh thesmophories.tex 2
edition/compiler_folio.sh f162v       # un folio seul, pour essai
```
