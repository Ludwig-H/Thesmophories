#!/usr/bin/env python3
"""Dresse la liste des PDF du Drive de l'auteur à indexer (couche texte), sans la versionner.

Les fichiers du Drive sont téléchargés par un autre chantier dans .sources/drive/fichiers/
(sélection : .sources/drive/selection.json). Beaucoup sont des éditions sous droits
(Latte–Hansen–Cunningham, Theodoridis, Adler, Kassel–Austin…) : ils restent dans .sources/
(non versionné) et l'index qui en dérive aussi. Pour ne rien exposer dans le dépôt public,
la liste nominative est écrite dans .sources/corpus/sources_drive.tsv ; ce script ne contient
que des motifs.

  python3 outils/corpus/sources_drive.py        # puis relancer indexer.py

Colonnes du TSV : chemin (relatif à .sources/drive/fichiers/) | categorie | sigle | description | present
"""

import json
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
DRIVE = RACINE / ".sources" / "drive"
SORTIE = RACINE / ".sources" / "corpus" / "sources_drive.tsv"

# (motif sur le chemin, catégorie, sigle — {1}, {2} = groupes du motif)
REGLES = [
    (r"Lexiques/Hesychius/Hesychius Latte-Cuningham complet", "lexiques", "Hsch. (Latte–Hansen–Cunningham)"),
    (r"Lexiques/Photius/Photii Patriarchae Lexicon A-D", "lexiques", "Phot. (Theodoridis) I"),
    (r"Lexiques/Photius/.*Vol\. 2\. E - M", "lexiques", "Phot. (Theodoridis) II"),
    (r"Lexiques/Photius/.*N - Phi", "lexiques", "Phot. (Theodoridis) III"),
    (r"Lexiques/Photius/.*Porson", "lexiques", "Phot. (Porson) π–ω"),
    (r"Lexiques/Souda/01 Alpha", "lexiques", "Sud. (Adler) I"),
    (r"Lexiques/Souda/Suidae Lexicon, Pars II", "lexiques", "Sud. (Adler) II"),
    (r"Lexiques/Souda/Adler A\., Suidae Lexicon 3", "lexiques", "Sud. (Adler) III"),
    (r"Lexiques/Souda/04 Pi", "lexiques", "Sud. (Adler) IV"),
    (r"Lexiques/Pollux/Libres I - V", "lexiques", "Poll. (Bethe) I"),
    (r"Lexiques/Pollux/Libres Vi - X", "lexiques", "Poll. (Bethe) II"),
    (r"Lexiques/Proverbes/Corpus paroemiographorum", "paremiographes", "CPG (Leutsch–Schneidewin)"),
    (r"Proverbes/Paroemiographi graeci Gaisford", "paremiographes", "Gaisford, Paroem. (PDF)"),
    (r"Proverbes/.*Tosi.*\.txt$", "paremiographes", "Tosi, Dict. des sentences"),
    (r"Proverbes/De_usu_proverbiorum", "paremiographes", "De usu proverbiorum apud Ar."),
    (r"Proverbes/De_proverbiis_aliisque", "paremiographes", "Bauck, De proverbiis Ar."),
    (r"Lexiques/Zonarae lexicon ed\. Tittmann/(\d)\.pdf", "lexiques", "Zonar. (Tittmann) {1}"),
    (r"Lexiques/Synagoge/", "lexiques", "Synag. (Cunningham)"),
    (r"Lexiques/Harpocration/.*Keaney", "lexiques", "Harp. (Keaney)"),
    (r"Lexiques/Athénée/Athenaei", "auteurs", "Ath. (Kaibel, PDF)"),
    (r"Untersuchungen zu den Attizistischen", "lexiques", "Erbse, Attiz. Lexika"),
    (r"Lexiques/Moeris/", "lexiques", "Moer. (Hansen)"),
    (r"Phrynichos Ekloge", "lexiques", "Phryn. (Fischer)"),
    (r"rutherford 1881", "lexiques", "Phryn. (Rutherford)"),
    (r"Lexica Segueriana", "lexiques", "Lex. Seg. (PDF)"),
    (r"Etymologicum magnum/.*Lasserre", "lexiques", "Et. Gen. (Lasserre–Livadaras)"),
    (r"Sturzius 1818", "lexiques", "Et. Gud. (Sturz)"),
    (r"Poetae Comici Graeci & testimonia & fragmenta/Kock (\d)", "fragments", "Kock {1} (PDF)"),
    (r"Poetae Comici Graeci & testimonia & fragmenta/Meineke (\d) (\d)", "fragments", "Meineke {1}.{2} (PDF)"),
    (r"Poetae Comici.*Vol\. 1 Comoedia Dorica", "fragments", "PCG I"),
    (r"Poetae comici Graeci Agathenor", "fragments", "PCG II"),
    (r"Aristophanes-Testimonia-Et-Fragmenta\.pdf", "fragments", "PCG III.2"),
    (r"Poetae Comici.*Volumen IV", "fragments", "PCG IV"),
    (r"Poetae Comici.*Volumen V", "fragments", "PCG V"),
    (r"Menander\. Testimonia", "fragments", "PCG VI.2"),
    (r"Poetae comici Graeci VII", "fragments", "PCG VII"),
    (r"Supplementum comicum", "fragments", "Suppl. com. (Demiańczuk)"),
    (r"Tragicorum Graecorum Fragmenta, Vol(?:ume|\.)\s*(\d)", "fragments", "TrGF {1}"),
    (r"Scholies/Scholia in Aristophanem, Pars II, Fasc\. III", "scholies", "Σ Ar. Av. (Holwerda)"),
    (r"Scholies/Scholia in Aristophanem, Pars III, Fasc\. 1b", "scholies", "Σ rec. Ar. Ran. (Chantry)"),
    (r"Scholies/Scholia in Aristophanem, Pars III, Fasc\. IVa", "scholies", "Σ vet. Ar. Plut. (Chantry)"),
    (r"Scholies/Scholia in Aristophanem, Pars III, Fasc\. IVb", "scholies", "Σ rec. Ar. Plut. (Chantry)"),
    (r"Scholies/Scholia recentiora in Aristophanis Nubes", "scholies", "Σ rec. Ar. Nub. (Koster)"),
    (r"Eustathe de Thessalonique/.*Odysseam\. Vol\. 1", "auteurs", "Eust. Od. (Stallbaum) I"),
    (r"Eustathe de Thessalonique/.*Odysseam, vol\. 2", "auteurs", "Eust. Od. (Stallbaum) II"),
    (r"Eustathe de Thessalonique/Iliade (\d+ ?- ?\d+) ?Eustathii archiepiscopi", "auteurs", "Eust. Il. (van der Valk) {1}"),
    (r"Eustathe de Thessalonique/Iliade 5-9Commentarii", "auteurs", "Eust. Il. (van der Valk) 5-9"),
]


def main():
    sel = json.load(open(DRIVE / "selection.json", encoding="utf-8"))
    lignes = []
    for x in sel:
        chemin = x["path"]
        if chemin.startswith("Mon Drive/"):
            chemin = chemin[len("Mon Drive/"):]
        if not re.search(r"\.(pdf|txt)$", chemin, re.I):
            continue
        for motif, cat, sigle in REGLES:
            m = re.search(motif, chemin)
            if m:
                s = sigle.format(None, *m.groups()) if m.groups() else sigle
                present = (DRIVE / "fichiers" / chemin).exists()
                desc = x.get("reason", "").split(" (doublons")[0]
                lignes.append((chemin, cat, s, desc, "oui" if present else "non"))
                break
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write("chemin\tcategorie\tsigle\tdescription\tpresent\n")
        for l in lignes:
            f.write("\t".join(c.replace("\t", " ") for c in l) + "\n")
    n = sum(1 for l in lignes if l[4] == "oui")
    print(f"{len(lignes)} fichiers retenus, dont {n} déjà téléchargés → {SORTIE}")


if __name__ == "__main__":
    main()
