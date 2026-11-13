# Édition des *Thesmophories* d'Aristophane — consignes de travail

## Règles absolues

- **Nom de l'auteur** : ne jamais écrire le nom réel de l'auteur de l'édition, nulle part (sources, PDF, notes, commits). Dans l'apparat critique, ses conjectures sont signées « Bibi » ; dans les commentaires, il parle à la première personne (« je »).
- **Dépôt public** : le dépôt GitHub est public. Ne jamais y versionner de document sous droits (éditions et commentaires modernes, articles, livres téléchargés du Drive, etc.). Ces fichiers vont dans `.sources/` (ignoré par git). Ne sont versionnés que : nos propres données et sources, les ressources du domaine public utiles, les PDF de l'édition.
- **Esprit critique** : ne jamais tenir pour acquis le texte établi (ni Gemini, ni les éditions modernes, ni même les travaux antérieurs de l'auteur). Toute leçon du *Ravennas* se vérifie sur l'image.
- **Travaux de Gemini** : retirés du dépôt le 1er nov. 2026 (peu fiables) ; ne jamais les citer comme autorité. Des images des 30 pages, seul le dossier `dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/` subsiste. Sa session du 11 nov. 2026 a rapatrié des sources utiles du Drive (`.sources/drive/ThesmoBiblio/`, fac-similé de 1904) ; ses transcriptions sont rangées hors dépôt (`.travail/gemini_20261111/`) comme lecture tierce, à contrôler sur l'image.
- **Dépôt propre et à jour** : pas de fichier périmé, de doublon ni de sortie obsolète ; rien à la racine en dehors de `README.md`, `CLAUDE.md`, `.gitignore` et des dossiers listés ci-dessous. Tout ce qui est remplacé est retiré ; `README.md` décrit l'état réel.
- **Exactitude des références** : toute référence (loci paralleli, testimonia, scholies, bibliographie) doit être vérifiée sur un texte source (corpus local, scan, édition). Jamais de référence inventée ; dans le doute, ne pas citer ou marquer `[à vérifier]`.
- **Persistance** : le codespace redémarre souvent et `/tmp` est alors vidé : **ne jamais utiliser `/tmp`** (ni le répertoire temporaire du système) ; tout fichier intermédiaire va dans `.travail/` (persistant, ignoré par git), tout résultat dans le dépôt. Écrire ses livrables **au fil de l'eau** (pas seulement à la fin) : une tâche interrompue doit pouvoir être reprise à partir des fichiers.
- **Git** : une seule branche, `main`. Pas de branches parasites. Les sous-agents ne committent pas (l'orchestrateur s'en charge). Commiter par `outils/git_anonyme.sh commit …` : l'environnement de travail impose par variables (`GIT_AUTHOR_*`, `GIT_COMMITTER_*`) une identité qui n'est pas anonyme ; des crochets (`outils/git_hooks/`, installés par `outils/installer_environnement.sh`) refusent toute autre identité.
- **Langue** : documents de travail et édition en français.

## Arborescence

- `recherche/` — recension : bibliographie, ressources, synthèses.
- `ravennas/` — étude graphologique, segmentation des folios, transcription diplomatique.
- `edition/` — nouvelle édition LaTeX (classe, contenus par folio, compilation).
- `outils/` — scripts (images, corpus, extraction).
- `latex/` — travaux de l'auteur, versions les plus récentes : `Aristophane-Thesmo Harmattan 2023 vv 1-641.tex` et `… vv 642-fin-bis.tex` (texte, apparat, testimonia, traduction, commentaire, notes), `Introduction.tex`, `Annexes.tex`, `Index.tex`, `figures/`. Versions antérieures et anciens PDF : `.sources/travaux_anterieurs/` (non versionné).
- `.sources/` (non versionné) — documents téléchargés (Drive, web), corpus numériques.
- `.travail/` (non versionné) — intermédiaires (découpes d'images, caches).

## Manuscrit

- **R** = Ravenne, Biblioteca Classense, ms. 429 (olim 137, 4, A), *Thesmophories* aux ff. 162v–177r (vv. 1–1231).
- Images à la résolution maximale disponible (identique au serveur IIIF de la Classense) : `dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/` (un fichier par page).
- Fac-similé phototypique de 1904 (Leyde, Sijthoff) : intégral dans `.sources/drive/ravennas_1904/` (non versionné ; planches par page `planches_thesmo/`, planches recalées sur les clichés de la Classense `.travail/relecture_1904/fXXX/1904_aligned.png`) ; ff. 162v–163r aussi dans `ravennas_1904_bnf/`.

## Environnement

- Python 3.14 (`python3`) avec PIL, numpy, pymupdf, lxml ; TeX Live (lualatex, xelatex, reledmac) ; polices GFS (Didot, Porson, Bodoni…), EB Garamond, Libertinus.
- Drive : outils MCP `mcp__claude_ai_Google_Drive__*` (charger via ToolSearch). Un téléchargement trop volumineux est enregistré dans un fichier JSON dont le chemin figure dans le message d'erreur : décoder avec `jq -r .content FICHIER | base64 -d > destination`.
- Web : `WebSearch` / `WebFetch` (via ToolSearch) et `curl`.
