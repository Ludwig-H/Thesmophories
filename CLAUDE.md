# Édition des *Thesmophories* d'Aristophane — consignes de travail

## Règles absolues

- **Nom de l'auteur** : ne jamais écrire le nom réel de l'auteur de l'édition, nulle part (sources, PDF, notes, commits). Dans l'apparat critique, ses conjectures sont signées « Bibi » ; dans les commentaires, il parle à la première personne (« je »).
- **Dépôt public** : le dépôt GitHub est public. Ne jamais y versionner de document sous droits (éditions et commentaires modernes, articles, livres téléchargés du Drive, etc.). Ces fichiers vont dans `.sources/` (ignoré par git). Ne sont versionnés que : nos propres données et sources, les ressources du domaine public utiles, les PDF de l'édition.
- **Esprit critique** : ne jamais tenir pour acquis le texte établi (ni Gemini, ni les éditions modernes, ni même les travaux antérieurs de l'auteur). Toute leçon du *Ravennas* se vérifie sur l'image.
- **Travaux de Gemini** : `dossier_ravennas_thesmophories/` et les fichiers `latex/Aristophane-Thesmo Edition 4 pages Ravennas*.tex` (et PDF associés) ont été produits par un précédent assistant ; peu fiables, ne jamais les citer comme autorité.
- **Exactitude des références** : toute référence (loci paralleli, testimonia, scholies, bibliographie) doit être vérifiée sur un texte source (corpus local, scan, édition). Jamais de référence inventée ; dans le doute, ne pas citer ou marquer `[à vérifier]`.
- **Persistance** : le codespace redémarre souvent et `/tmp` est alors vidé : **ne jamais utiliser `/tmp`** (ni le répertoire temporaire du système) ; tout fichier intermédiaire va dans `.travail/` (persistant, ignoré par git), tout résultat dans le dépôt. Écrire ses livrables **au fil de l'eau** (pas seulement à la fin) : une tâche interrompue doit pouvoir être reprise à partir des fichiers.
- **Git** : une seule branche, `main`. Pas de branches parasites. Les sous-agents ne committent pas (l'orchestrateur s'en charge).
- **Langue** : documents de travail et édition en français.

## Arborescence

- `recherche/` — recension : bibliographie, ressources, synthèses.
- `ravennas/` — étude graphologique, segmentation des folios, transcription diplomatique.
- `edition/` — nouvelle édition LaTeX (classe, contenus par folio, compilation).
- `outils/` — scripts (images, corpus, extraction).
- `latex/` — travaux antérieurs de l'auteur ; versions les plus récentes du corps de l'édition : `Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `Aristophane-Thesmo Harmattan 2023 vv 642-fin-bis.tex` (texte, apparat, testimonia, traduction, commentaire, notes). Aussi : `Introduction.tex`, `Annexes.tex`, `Index.tex`, versions antérieures (`nov 2022`, `Harmattan mars 2023`).
- `.sources/` (non versionné) — documents téléchargés (Drive, web), corpus numériques.
- `.travail/` (non versionné) — intermédiaires (découpes d'images, caches).

## Manuscrit

- **R** = Ravenne, Biblioteca Classense, ms. 429 (olim 137, 4, A), *Thesmophories* aux ff. 162v–177r (vv. 1–1231).
- Images à la résolution maximale disponible (identique au serveur IIIF de la Classense) : `dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/` (un fichier par page), `dossier_ravennas_thesmophories/planches_doubles_ff162v-177r/` (doubles pages).
- Fac-similé phototypique de 1904 (BnF) pour ff. 162v–163r : `ravennas_1904_bnf/`.

## Environnement

- Python 3.14 (`python3`) avec PIL, numpy, pymupdf, lxml ; TeX Live (lualatex, xelatex, reledmac) ; polices GFS (Didot, Porson, Bodoni…), EB Garamond, Libertinus.
- Drive : outils MCP `mcp__claude_ai_Google_Drive__*` (charger via ToolSearch). Un téléchargement trop volumineux est enregistré dans un fichier JSON dont le chemin figure dans le message d'erreur : décoder avec `jq -r .content FICHIER | base64 -d > destination`.
- Web : `WebSearch` / `WebFetch` (via ToolSearch) et `curl`.
