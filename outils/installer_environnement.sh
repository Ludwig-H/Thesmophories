#!/usr/bin/env bash
# Installation des dépendances système du chantier (à relancer après un changement de machine).
set -euo pipefail
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
  texlive-luatex texlive-xetex texlive-latex-base texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-lang-greek texlive-lang-french texlive-humanities texlive-science \
  lmodern fontconfig fonts-freefont-otf fonts-freefont-ttf poppler-utils djvulibre-bin unzip jq \
  tesseract-ocr tesseract-ocr-grc tesseract-ocr-ell tesseract-ocr-lat tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-ita
python3 -m pip install -q pillow numpy pymupdf lxml fonttools opencv-python-headless scipy scikit-image
OSFONTDIR="$(dirname "$0")/../edition/polices" luaotfload-tool --update --force
# Machine partagée : pas de tempête de fils de calcul (Python) ni d'OCR gourmand
U=$(python3 -m site --user-site); mkdir -p "$U"
cat > "$U/usercustomize.py" <<'PY'
import os
for v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS',
          'VECLIB_MAXIMUM_THREADS', 'OPENCV_FOR_THREADS_NUM', 'OMP_THREAD_LIMIT'):
    os.environ.setdefault(v, '2')
PY
printf '#!/bin/sh\nOMP_THREAD_LIMIT=1 exec nice -n 15 /usr/bin/tesseract "$@"\n' | sudo tee /usr/local/bin/tesseract >/dev/null
sudo chmod +x /usr/local/bin/tesseract
