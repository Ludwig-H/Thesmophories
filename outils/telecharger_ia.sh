#!/usr/bin/env bash
# Télécharge depuis archive.org le PDF, la couche OCR (_djvu.txt) et les métadonnées d'un item.
# Usage : telecharger_ia.sh DOSSIER_LOCAL IDENTIFIANT_IA
# Les fichiers sont placés dans .sources/web/editions/DOSSIER_LOCAL/
set -u
BASE=/workspaces/Thesmophories/.sources/web/editions
dest="$BASE/$1"; id="$2"
mkdir -p "$dest"
meta="$dest/${id}_metadata.json"
[ -s "$meta" ] || curl -sL --retry 5 -m 120 "https://archive.org/metadata/$id" -o "$meta"
python3 -I - "$meta" <<'PY' > "$dest/.files_$id.txt"
import json,sys
d=json.load(open(sys.argv[1]))
for f in d.get('files',[]):
    n=f['name']
    if (n.endswith('.pdf') and not n.endswith('_text.pdf')) or n.endswith('_djvu.txt'):
        print(n)
PY
while read -r f; do
  [ -z "$f" ] && continue
  out="$dest/$f"
  if [ -s "$out" ]; then continue; fi
  curl -sL --retry 5 --retry-delay 5 -m 3600 "https://archive.org/download/$id/$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$f")" -o "$out.part" && mv "$out.part" "$out"
done < "$dest/.files_$id.txt"
echo "OK $1 $id $(ls "$dest" | wc -l) fichiers"
