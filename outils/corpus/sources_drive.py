#!/usr/bin/env python3
"""Dresse la liste des fichiers du Drive de l'auteur à indexer, sans la versionner.

Les fichiers du Drive sont téléchargés par un autre chantier dans .sources/drive/fichiers/
(sélection : .sources/drive/selection.json). Beaucoup sont des éditions sous droits
(Latte–Hansen–Cunningham, Theodoridis, Adler, Kassel–Austin…) : ils restent dans .sources/
(non versionné) et l'index qui en dérive aussi. Pour ne rien exposer dans le dépôt public,
la liste nominative est écrite dans .sources/corpus/sources_drive.tsv ; ce script ne contient
que des motifs.

La liste réunit :
  - les ouvrages de référence attendus (REGLES), présents ou non (sélection du chantier Drive) ;
  - tout autre fichier réellement présent (PDF, EPUB, ou .txt sans PDF jumeau) : catégorie
    « etudes » ; l'indexeur écarte ceux dont la couche texte n'est pas exploitable.
Sont exclus les doublons exacts (MD5) et les dossiers de travail de l'auteur (EXCLUS).

La colonne « traitement » dit comment lire le fichier : « couche » (couche texte du PDF, avec
rétablissement automatique des polices Kleinlogel) ou « hesychius:<tome> » (gloses découpées
par ocr_hesychius.py : .sources/corpus/hesychius/gloses.jsonl.gz).

  python3 outils/corpus/sources_drive.py        # puis relancer indexer.py

Colonnes du TSV : chemin (relatif à .sources/drive/fichiers/) | categorie | sigle | description | present | traitement
"""

import hashlib
import json
import os
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
DRIVE = RACINE / ".sources" / "drive"
SORTIE = RACINE / ".sources" / "corpus" / "sources_drive.tsv"

# Dossiers de travail de l'auteur (brouillons, articles) : jamais indexés
EXCLUS = re.compile(r"/Articles/|Grec - commentaire - traduction - apparat/")

# (motif sur le chemin, catégorie, sigle — {1}, {2} = groupes du motif — et traitement éventuel)
# Catégorie None : fichier à ne jamais lire par sa couche texte.
REGLES = [
    (r"Lexiques/Hesychius/Hesychius Latte-Cuningham complet", None, ""),  # couche texte brouillée
    (r"Lexiques/Hesychius/Latte_I_alpha-delta", "lexiques", "Hsch. (Latte) I", "hesychius:I"),
    (r"Lexiques/Hesychius/Hesychii Alexandrini Lexicon, Volumen II", "lexiques", "Hsch. (Latte) II", "hesychius:II"),
    (r"Lexiques/Hesychius/Hansen_III_pi-sigma", "lexiques", "Hsch. (Hansen) III", "hesychius:III"),
    (r"Lexiques/Hesychius/03 Latte Pi - Sigma", "lexiques", "Hsch. (Hansen) III", "hesychius:III"),
    (r"Lexiques/Hesychius/04 Latte Tau", "lexiques", "Hsch. (Hansen–Cunningham) IV", "hesychius:IV"),
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


def md5(chemin):
    h = hashlib.md5()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sigle_etude(chemin):
    """Sigle lisible d'un fichier sans règle : nom du fichier, sans les mentions parasites."""
    n = Path(chemin).stem
    n = re.sub(r"\s*\(z-lib\.org\)|\s*\(BookLid\.org\)|\s*\(\d\)$", "", n)
    n = re.sub(r"[_\s]+", " ", n).strip()
    return n[:60]


def regle_de(chemin):
    for r in REGLES:
        m = re.search(r[0], chemin)
        if m:
            s = r[2].format(None, *m.groups()) if m.groups() else r[2]
            return r[1], s, (r[3] if len(r) > 3 else "couche")
    return None


def main():
    sel = json.load(open(DRIVE / "selection.json", encoding="utf-8"))
    racine = DRIVE / "fichiers"
    lignes, vus = [], set()
    # 1. ouvrages attendus (sélection du chantier Drive)
    for x in sel:
        chemin = x["path"]
        if chemin.startswith("Mon Drive/"):
            chemin = chemin[len("Mon Drive/"):]
        if not re.search(r"\.(pdf|txt)$", chemin, re.I):
            continue
        r = regle_de(chemin)
        if r and r[0]:
            present = (racine / chemin).exists()
            desc = x.get("reason", "").split(" (doublons")[0]
            lignes.append([chemin, r[0], r[1], desc, "oui" if present else "non", r[2]])
            vus.add(chemin)
    # 2. tout ce qui est réellement présent
    presents = []
    for dp, _, fn in os.walk(racine):
        for f in fn:
            presents.append(os.path.relpath(os.path.join(dp, f), racine))
    presents.sort()
    empreintes = {}
    for l in lignes:
        if l[4] == "oui":
            empreintes[md5(racine / l[0])] = l[0]
    for chemin in presents:
        suffixe = Path(chemin).suffix.lower()
        if chemin in vus or suffixe not in (".pdf", ".epub", ".txt") or EXCLUS.search("/" + chemin):
            continue
        if suffixe == ".txt" and any((racine / chemin).with_suffix(e).exists() for e in (".pdf", ".PDF")):
            continue   # texte extrait d'un PDF voisin
        r = regle_de(chemin)
        if r and not r[0]:
            continue
        e = md5(racine / chemin)
        if e in empreintes:
            continue
        empreintes[e] = chemin
        cat, sigle, trait = r or ("etudes", sigle_etude(chemin), "couche")
        lignes.append([chemin, cat, sigle, "", "oui", trait])
    # 3. doublons exacts parmi la sélection (Hsch. III en deux exemplaires…)
    garde, deja = [], set()
    for l in lignes:
        if l[4] == "oui":
            e = md5(racine / l[0])
            if e in deja:
                continue
            deja.add(e)
        garde.append(l)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write("chemin\tcategorie\tsigle\tdescription\tpresent\ttraitement\n")
        for l in garde:
            f.write("\t".join(c.replace("\t", " ") for c in l) + "\n")
    n = sum(1 for l in garde if l[4] == "oui")
    print(f"{len(garde)} fichiers retenus, dont {n} présents → {SORTIE}")


if __name__ == "__main__":
    main()
