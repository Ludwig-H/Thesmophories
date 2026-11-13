#!/usr/bin/env bash
# Installation des outils du chantier.
# La machine de travail est reconstruite à chaque redémarrage : seuls /workspaces et le dossier
# personnel persistent. Les modules Python vont donc dans le site utilisateur (pip --user), et
# les paquets système (TeX Live, poppler, tesseract…), à réinstaller après chaque redémarrage,
# sont gardés dans un cache persistant pour ne pas être retéléchargés.
# Usage : outils/installer_environnement.sh   (sans danger à relancer)
set -euo pipefail
RACINE="$(cd "$(dirname "$0")/.." && pwd)"

# 1. modules Python (persistants)
python3 -m pip install -q --user pillow numpy pymupdf lxml fonttools opencv-python-headless scipy scikit-image
U=$(python3 -m site --user-site); mkdir -p "$U"
cat > "$U/usercustomize.py" <<'PY'
# Machine partagée : pas de tempête de fils de calcul dans les petits scripts.
import os
for v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS',
          'VECLIB_MAXIMUM_THREADS', 'OPENCV_FOR_THREADS_NUM'):
    os.environ.setdefault(v, '2')
PY

# 2. paquets système (cache des .deb persistant)
CACHE="$HOME/.cache/apt-thesmophories"; mkdir -p "$CACHE/partial"
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
  -o Dir::Cache::archives="$CACHE" \
  texlive-luatex texlive-xetex texlive-latex-base texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-lang-greek texlive-lang-french texlive-humanities texlive-science \
  lmodern fontconfig fonts-freefont-otf fonts-freefont-ttf poppler-utils djvulibre-bin unzip jq rclone \
  tesseract-ocr tesseract-ocr-grc tesseract-ocr-ell tesseract-ocr-lat tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-ita

# 3. OCR à faible priorité, un fil par page (machine partagée)
printf '#!/bin/sh\nOMP_THREAD_LIMIT=1 exec nice -n 15 /usr/bin/tesseract "$@"\n' | sudo tee /usr/local/bin/tesseract >/dev/null
sudo chmod +x /usr/local/bin/tesseract

# 4. base des polices de l'édition pour LuaTeX
OSFONTDIR="$RACINE/edition/polices" luaotfload-tool --update --force

# 5. identité Git anonyme (règle 1 de CLAUDE.md). Coder injecte GIT_AUTHOR_* / GIT_COMMITTER_*
#    (adresse personnelle), qui l'emportent sur .git/config : commiter avec outils/git_anonyme.sh ;
#    les crochets pre-commit et pre-push refusent toute autre identité.
git -C "$RACINE" config --local user.name "Ludwig-H"
git -C "$RACINE" config --local user.email "158177790+Ludwig-H@users.noreply.github.com"
install -m 755 "$RACINE/outils/git_hooks/pre-commit" "$RACINE/outils/git_hooks/pre-push" "$RACINE/.git/hooks/"

# 6. restauration éventuelle de la configuration rclone (Google Drive, hors git)
if [ -f "$RACINE/.travail/.rclone.conf" ] && [ ! -f "$HOME/.config/rclone/rclone.conf" ]; then
  mkdir -p "$HOME/.config/rclone"
  cp "$RACINE/.travail/.rclone.conf" "$HOME/.config/rclone/rclone.conf"
  chmod 600 "$HOME/.config/rclone/rclone.conf"
fi
echo "Environnement prêt."
