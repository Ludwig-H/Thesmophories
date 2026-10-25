#!/usr/bin/env bash
# Compile un seul folio (ou plusieurs) dans un document d'essai : ./compiler_folio.sh f162v [f163r ...]
# Le PDF est écrit dans .travail/folios/<premier folio>.pdf ; les erreurs sont affichées.
set -euo pipefail
cd "$(dirname "$0")"
export OSFONTDIR="$PWD/polices"
export TEXINPUTS="$PWD:$PWD/images:${TEXINPUTS:-}"
out="../.travail/folios"; mkdir -p "$out"
nom="$1"
{
  echo '\documentclass{thesmo}'
  echo '\graphicspath{{images/}}'
  echo '\begin{document}'
  for f in "$@"; do echo "\\input{folios/$f}"; done
  echo '\end{document}'
} > "$out/$nom.tex"
if lualatex -interaction=nonstopmode -halt-on-error -output-directory="$out" "$out/$nom.tex" > /dev/null; then
  echo "OK : $out/$nom.pdf ($(python3 -c "import pymupdf,sys;print(pymupdf.open(sys.argv[1]).page_count)" "$out/$nom.pdf" 2>/dev/null) pages)"
  grep -E "Overfull|Missing character" "$out/$nom.log" | sort | uniq -c | sort -rn | head -5 || true
else
  echo "ÉCHEC — extrait du journal :"; grep -n "^!" -A8 "$out/$nom.log" | head -30; exit 1
fi
