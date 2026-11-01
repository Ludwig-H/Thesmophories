# Aristophane, *Les Thesmophories* — édition sur le *Ravennas*

Nouvelle édition philologique des *Thesmophories* (Θεσμοφοριάζουσαι), fondée sur le
seul témoin médiéval de la pièce, le *Ravennas* (Ravenne, Biblioteca Classense,
ms. 429, milieu du Xᵉ siècle, ff. 162v–177r) : transcription diplomatique, apparat,
*loci paralleli*, commentaire critique, texte établi, traduction et commentaire.

> **Chantier en cours** (novembre 2026). Le livre se compile déjà en entier (texte, traduction,
> commentaire). L'[étude graphologique](ravennas/ETUDE_GRAPHOLOGIQUE.md) et la recension sont
> terminées ; la transcription diplomatique des 30 pages, la scansion, l'apparat et les
> *loci paralleli* sont en cours. Le PDF de l'édition sera déposé ici dès la première version.

## Conception : une unité de quatre pages (et plus) par folio du manuscrit

1. **Double page I** — à gauche, la transcription diplomatique de la page de R
   (disposition, sigles, corrections, abréviations expliquées ; une couleur par main ;
   fautes évidentes et d'accentuation corrigées), l'apparat critique dans le prolongement
   des lignes, puis les *loci paralleli* et le commentaire critique ; à droite, le
   fac-similé de la page, aussi grand que possible.
2. **Double page(s) II** — à gauche, le texte grec établi (structure, mètres,
   scansion des parties chantées) ; à droite, la traduction (didascalies) ; au bas des
   deux pages, le commentaire de la pièce.

Format 230 × 310 mm, marges réduites ; polices libres : EB Garamond (français),
GFS Porson (grec établi), Cardo (transcription du manuscrit).

## Organisation du dépôt

| Dossier | Contenu |
|---|---|
| [`edition/`](edition/) | l'édition : classe LuaLaTeX `thesmo.cls`, document maître `thesmophories.tex`, un dossier par folio (`folios/fXXX/` : `diplo.tex`, `apparat.tex`, `paralleles.tex`, `critique.tex`, `texte.tex`, `commentaire.tex`), données (`donnees/`), [conventions](edition/CONVENTIONS.md) |
| [`ravennas/`](ravennas/) | le manuscrit : [étude graphologique](ravennas/ETUDE_GRAPHOLOGIQUE.md), [guide de transcription](ravennas/GUIDE_TRANSCRIPTION.md), segmentation des pages, transcription diplomatique (format XML : [spécification](ravennas/FORMAT_TRANSCRIPTION.md)) |
| [`recherche/`](recherche/) | recension : éditions et sources des conjectures, numérotation des vers, dossier sur le manuscrit, *Monacensis* gr. 492, scholies, papyri, testimonia, métrique, études, corpus numériques |
| [`outils/`](outils/) | scripts : images (recadrage, segmentation, versions améliorées), corpus grec local et moteur de recherche, extraction des travaux antérieurs, transcription |
| [`latex/`](latex/) | travaux de l'auteur, version de 2023 (texte, apparat, traduction, commentaire, introduction, annexes, index, figures), source de la présente édition |
| [`ravennas_1904_bnf/`](ravennas_1904_bnf/) | planches du fac-similé phototypique de 1904 (ff. 162v–163r), manifeste IIIF de la Classense |
| [`dossier_ravennas_thesmophories/`](dossier_ravennas_thesmophories/) | images haute définition des 30 pages (`folios_individuels_ff162v-177r/`) |

Les documents sous droits utilisés pour le travail (éditions et commentaires modernes,
etc.) ne sont pas versionnés.

## Compiler

```sh
outils/installer_environnement.sh     # une fois (TeX Live LuaTeX, outils Python)
edition/compiler.sh thesmophories.tex 2
edition/compiler_folio.sh f162v       # un folio seul, pour essai
```
