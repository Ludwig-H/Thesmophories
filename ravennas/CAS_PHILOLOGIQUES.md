# Cas philologiques du *Ravennas* — dossier

*Demande de l'auteur (novembre 2026), à partir d'un exemple qu'il a relevé sur l'image : au v. 489, κυνδ᾽ corrigé en κύβδ᾽. Relever systématiquement les lieux de ce genre et les instruire. Document de travail, tenu au fil de l'eau.*

## 1. Ce qu'on relève

Un lieu entre dans le dossier quand l'état de R ou de sa tradition apprend quelque chose sur le texte, sur le manuscrit ou sur son histoire :

1. **Correction dans R** dont la leçon première (R^a.c.) est autre chose qu'une faute mécanique : un mot ou une forme réels, une variante connue ailleurs, une leçon reprise par un témoin postérieur.
2. **Date relative d'une intervention.** M (Monac. gr. 492, copié sur R par Paolo Canal vers 1505 : `recherche/monacensis_492.md`) et la Juntine (1516, préparée sur R) montrent ce que R portait à ces dates. Une correction déjà copiée dans M est antérieure à 1505 ; une leçon de la Juntine contraire à la correction pose la question de ce que ses éditeurs ont lu.
3. **Variante ancienne** : lemme ou *u.l.* des scholies, papyrus, Souda, lexicographes (Hésychius, Photius, Pollux), différents de R.
4. **Faute révélatrice** : confusion de lettres qui renseigne sur l'écriture du modèle (β en « u » et ν, onciale ou minuscule), itacisme, haplographie, glose entrée dans le texte.
5. **Désaccord des éditeurs sur ce que porte R** (Velsen, Prato, Wilson, Enger…), à trancher sur l'image.
6. **Mot rare ou forme isolée** qu'un lexicographe glose ou que R est seul à donner.

## 2. Méthode

- **Liste des lieux à examiner** : `ravennas/cas/lieux_a_examiner.tsv`, produite par `outils/transcription/lieux_a_examiner.py`. Elle rassemble, vers par vers :
  - ce que rapportent les éditeurs (répertoire critique : R^a.c., R^p.c., R², « a pr. m. », R douteux ; la Juntine, M, les scholies, les papyrus et les testimonia quand ils s'écartent de R) ;
  - les corrections relevées par l'étude graphologique ;
  - les interventions de la transcription.

  La colonne « alerte » signale, en premier lieu, une correction rapportée par un éditeur alors que la transcription n'en porte aucune. C'était le cas du v. 489 : les deux lectures indépendantes ont lu κύβδ᾽ sans voir le ν dessous. La correspondance des numéros de vers y est approximative dans les passages lyriques : la liste indique des lieux à examiner, elle ne conclut rien.
- **Premier geste, pour tout lieu litigieux : les lexiques et les proverbes** (consigne de l'auteur, 20 nov. 2026).
  - *Lexiques* : Hésychius (Latte–Hansen–Cunningham ; texte décodé dans `.sources/corpus/hesychius/gloses.jsonl.gz`, page en image par `python3 outils/corpus/ocr_hesychius.py voir <lettre> <numéro>`), Photius, Souda, *Synagoge*, *Etymologica*, Pollux, Harpocration, Zonaras.
  - *Proverbes* : *Corpus paroemiographorum Graecorum*, Gaisford, Tosi (formes grecques et latines), Bauck (proverbes chez Aristophane), et les équivalents latins (Érasme, *Adages* ; Otto).
  - *Outil* : `python3 outils/corpus/lexiques_proverbes.py <vers>` interroge ces seules sources sur chaque mot du vers, de la leçon de R et des variantes.
  - *Pourquoi* : au v. 489, la glose d'Hésychius (κυνδός, voisine de κυνδάλη) et le proverbe du jeu des chevilles (ἥλῳ τὸν ἧλον, chez Cicéron *clavo clavum*) ont orienté toute l'instruction du cas.
- **Instruction de chaque lieu** :
  - sur l'image (cliché de la Classense, versions améliorées, fac-similé de 1904) ;
  - mains et encres selon `ravennas/GUIDE_TRANSCRIPTION.md` ;
  - date relative par M et la Juntine ;
  - confrontation aux éditeurs, aux scholies, aux lexicographes et aux papyrus.

  Toute référence est vérifiée sur la source.
- **Notice** (§ 3), toujours dans le même ordre : lieu ; ce que porte R ; témoins anciens et tradition imprimée ; lexique ; discussion ; conséquences pour le texte, l'apparat et le commentaire ; pièces.
- La transcription diplomatique est corrigée en conséquence (`ravennas/transcription/fXXX.xml`). L'apparat et le commentaire critique reprennent le cas au moment de l'établissement du texte.

## 3. Notices et index

Les notices sont rangées par page, dans `ravennas/cas/fXXX.md` ; la première, celle du v. 489 (`ravennas/cas/f168r.md`), sert de modèle. L'index ci-dessous est produit par `outils/transcription/index_cas.py` à partir de ces fichiers (titres « ## v. N — … »).

<!-- index : début -->
| Vers | Page | Cas | Notice |
|---|---|---|---|
| v. 45 | f163r | f. 163r, l. 5 : λέγεισ R^a.c. → λέγει (σ gratté) ; λέγεις Juntine | [`cas/f163r.md`](cas/f163r.md) |
| v. 426 | f167v | f. 167v, l. 4 : ὦ κότριψ᾽ R (crase de ὁ οἰκότριψ) | [`cas/f167v.md`](cas/f167v.md) |
| v. 427 | f167v | f. 167v, l. 5 : θριπήδεστα R ~ θριπηδέστατ(α) Su. | [`cas/f167v.md`](cas/f167v.md) |
| v. 428 | f167v | f. 167v, l. 6 : τοῦτο R^a.c. → τούτω R^p.c. | [`cas/f167v.md`](cas/f167v.md) |
| v. 430 | f167v | f. 167v, l. 8 : μίᾶι γέτω R (double accent) ~ μίᾳ γέ τῃ Iunt. | [`cas/f167v.md`](cas/f167v.md) |
| v. 433 | f167v | f. 167v, l. 11 : οὔπω τε R^a.c. → οὐπώποτε R² | [`cas/f167v.md`](cas/f167v.md) |
| v. 437 | f167v | f. 167v, l. 14 : εἰδέας R ~ ἰδέας Su. | [`cas/f167v.md`](cas/f167v.md) |
| v. 443 | f167v | f. 167v, l. 21 : ὀλίγον R^a.c. → ὀλίγων R^XVI ; ἑτέρα γυνή ; ἕνεκ᾽ αὐτῆ | [`cas/f167v.md`](cas/f167v.md) |
| v. 456 | f167v | f. 167v, l. 34 : ἀγρίοισι λαχάνοις (τοῖς om. R) ; αὐτοστραφεὶς R | [`cas/f167v.md`](cas/f167v.md) |
| v. 458 | f167v | f. 167v, l. 36 : σὐνθηματιαίους (σ de R³ sur un οὐν- de T) | [`cas/f167v.md`](cas/f167v.md) |
| v. 489 | f168r | f. 168r, l. 24 : κυνδ᾽ R^a.c. → κύβδ᾽ R^p.c. | [`cas/f168r.md`](cas/f168r.md) |
<!-- index : fin -->
