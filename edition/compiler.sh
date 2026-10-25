#!/usr/bin/env bash
# Compile un document de l'édition avec LuaLaTeX (polices locales via OSFONTDIR).
# Usage : ./compiler.sh fichier.tex [passes]
set -euo pipefail
cd "$(dirname "$0")"
export OSFONTDIR="$PWD/polices"
export TEXINPUTS="$PWD:$PWD/images:${TEXINPUTS:-}"
f="$1"; n="${2:-1}"
for i in $(seq 1 "$n"); do
  lualatex -interaction=nonstopmode -halt-on-error -output-directory="$(dirname "$f")" "$f" > /dev/null || { tail -40 "${f%.tex}.log"; exit 1; }
done
grep -E "^!|Missing character|Overfull" "${f%.tex}.log" | sort | uniq -c | sort -rn | head -20 || true
