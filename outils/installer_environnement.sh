#!/usr/bin/env bash
# Installation des dépendances système du chantier (à relancer après reconstruction du codespace).
set -euo pipefail
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq texlive-luatex djvulibre-bin tesseract-ocr tesseract-ocr-grc tesseract-ocr-ell tesseract-ocr-lat tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-ita rclone
python3 -m pip install -q fonttools
luaotfload-tool --update
python3 -m pip install -q opencv-python-headless scipy scikit-image
