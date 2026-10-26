# Audit des productions du précédent assistant (Gemini)

*Document de travail, rédigé au fil des contrôles (2e reprise après interruption, 26 oct. 2026). État : §§ 2 et 3.1 terminés ; §§ 3.2–3.5 en cours ; §§ 1, 4–6 à rédiger en fin d'audit.*

**Périmètre.** `dossier_ravennas_thesmophories/` (README.md, Analyse_Graphologique…, Manuel_Dechiffrement…, Notice…, Scholies_et_Gloses…, generer_planches_dechiffrement.py, planches) et `latex/Aristophane-Thesmo Edition 4 pages Ravennas*.tex` (versions simple, Integrale, vv 1-641, vv 642-fin).

**Méthode.** Contrôle direct sur les images des folios (`dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/`) : découpes agrandies (×1,3 à ×3) puis lecture à l'œil. Les leçons sont aussi confrontées à la collation de von Velsen (1883, domaine public, `.sources/web/ravennas/collations/aristophanisthe00velsgoog.pdf`, océrisé dans `.travail/audit_gemini/velsen/`), aux scholies de Dübner (1842) et aux éditions modernes présentes dans `.sources/`. Les intermédiaires (découpes, notes) sont dans `.travail/audit_gemini/`.

**Numérotation.** Les vers sont cités dans la numérotation de l'édition de l'auteur (`latex/Aristophane-Thesmo Harmattan 2023 *.tex`), celle que Gemini prétend suivre. Elle ne diffère de celle de Hall–Geldart (Perseus) qu'en quelques endroits (ex. 678 auteur = 677 H.-G. ; 1082 auteur = 1081d H.-G.).

## 1. Verdict global

*(à rédiger en fin d'audit)*

## 2. Inventaire des productions

| Fichier(s) | Taille | Contenu annoncé |
|:--|:--|:--|
| `dossier_ravennas_thesmophories/README.md` | 216 Ko, 1 483 l. | « Dossier codicologique, paléographique, stemmatique et iconographique complet » : fiche du manuscrit, « atelier d'Éphrem », histoire, ordre des pièces (§ 1) ; stemma, papyrus Ψ¹–Ψ⁵, tradition indirecte, « dossier Mnésiloque » (§ 2) ; trois mains, alphabet, *notae personarum*, « quatre *parepigraphai* », typologie des fautes, « tableau exhaustif des grattages », conjectures « Bibi » (§ 3) ; tableau et notices des 30 folios (§ 4) ; IIIF (§ 5) ; bibliographie (§ 6). |
| `Analyse_Graphologique_Historique_et_Philologique_Ravennas.{md,tex,pdf}` | 165 Ko (md), 55 p. | Monographie en trois parties : histoire du texte, « graphologie comparée » de R¹, R² et Boninus avec un « atlas » de 16 planches, « stratigraphie des fautes » et « répertoire intégral des 38 lieux *in rasura* ». |
| `Manuel_Dechiffrement_Ecriture_Ravennas.{md,tex,pdf}` | 88 Ko (md), 29 p. | Cours de lecture du manuscrit : « 4 registres d'écriture », abécédaire, « pièges », ligatures, abréviations, exercices corrigés ; renvoie aux 24 planches. |
| `Notice_Ravennas_Codicologie_et_Paleographie.{tex,pdf}` | 172 Ko (tex), 35 p. | Notice codicologique et paléographique, folio par folio. |
| `Scholies_et_Gloses_Ravennas_Thesmophories.{md,tex,pdf}` | 664 Ko (md), 96 p. | « Atlas et édition intégrale » de 386 scholies et gloses : position sur la page, texte grec, « tracé diplomatique » avec abréviations, traduction, commentaire ; « collation diplomatique ligne par ligne » de chaque folio. |
| `generer_planches_dechiffrement.py` | 148 Ko, 2 337 l. | Génère les planches de `exemples_dechiffrement/` (coordonnées de découpe et légendes codées en dur). |
| `exemples_dechiffrement/` (24 JPEG), `specimens_paleographiques/` (16 JPEG) | 15 + 15 Mo | Planches annotées (lettres, ligatures, « pièges », grattages, *parepigraphai*, exercices) et détails recadrés. |
| `folios_individuels_ff162v-177r/` (30 JPEG, ≈ 1 921 × 2 780 px), `planches_doubles_ff162v-177r/` (15 JPEG, 3 946 × 2 780 px) | 41 + 36 Mo | Images de la Classense (serveur IIIF), nommées avec les vers supposés de chaque page. |
| `latex/Aristophane-Thesmo Edition 4 pages Ravennas.tex` ; `… - Integrale.tex` ; `… vv 1-641.tex` ; `… vv 642-fin.tex` (+ `latex/folios_recadres_ff162v-177r/`, PDF dans `pdf/`) | 1,5 Mo ; 1,6 Mo ; 0,76 Mo ; 0,80 Mo | « Édition synoptique » en 30 étalements de 4 pages : « transcription diplomatique corrigée de R » (1 238 lignes `\ligneRav` : numéro, sigle, texte, apparat), *loci paralleli*, scholies du folio ; fac-similé recadré ; texte établi et traduction. Les quatre variantes ne diffèrent que par l'habillage et le découpage. |

**Remarque générale.** Le nom réel de l'auteur de l'édition figure plus d'un millier de fois dans ces fichiers, tous versionnés : README (118 occurrences), Scholies (md 565, tex 192, pdf 190), Notice (tex 82, pdf 80), Analyse (md 26, tex 26, pdf 26), éditions LaTeX (19 à 39 chacune), et les copies PDF de `pdf/` (26 à 190). Seul le Manuel n'en contient pas. C'est contraire à la règle absolue de `CLAUDE.md`, sur un dépôt public.

## 3. Tableau des contrôles

### 3.1 Correspondance folios ↔ vers (30 folios contrôlés)

On a lu sur l'image la **première et la dernière ligne de la colonne de texte** de chacun des 30 folios. Ces bornes conditionnent les noms des fichiers images (`01_f162v_classense164v_vv0001-0042.jpg`…), le tableau synoptique du README (§ 4.1), les en-têtes des notices folio par folio, la répartition des lignes dans la « transcription diplomatique » des fichiers `latex/…Edition 4 pages Ravennas*.tex` et le découpage de `Scholies_et_Gloses…`.

| N° | Folio (Classense) | Vers selon Gemini | Vers lus sur l'image (1re → dernière ligne) | Verdict |
|:-:|:-:|:-:|:--|:-:|
| 01 | 162v (164v) | 1–42 | 1 « ὦ ζεῦ χελιδὼν ἄρα πότε φανήσεται » → 42 « τῶν δεσποσύνων μελοποιῶν » | exact |
| 02 | 163r (165r) | 43–79 | 43 « ἐχέτω δὲ πνοὰς… » → 79 « μέλλει δικάζειν οὔτε βουλῆς ἐσθ' ἕδρα » | exact |
| 03 | 163v (165v) | 80–122 | 80 « ἐπεὶ τρίτη 'στὶ… » → 122 « διανεύματα χαρίτων » | exact |
| 04 | 164r (166r) | 123–164 | 123 « σέβομαι λατὼ τ' ἄνασσαν » → 164 « καὶ φρύνιχος τοῦτον γὰρ οὖν ἀκήκοας » | exact |
| 05 | 164v (166v) | 165–207 | 165 « αὐτός τε καλὸς ἦν… » → **208** « τί οὖν ποιήσεις ταῦτα· μὴ δόκει γε σύ » | **faux** |
| 06 | 165r (167r) | 208–251 | **209** « ὦ τρισκακοδαίμων ὡς ἀπόλωλ' εὐριπίδης » → 251 « καὶ στρόφιον… » | **faux** |
| 07 | 165v (167v) | 252–294 | 252 « λαμβάνετε καὶ χρῆσθ'… » → **293** « ἵν' ἐξακούω… » | **faux** |
| 08 | 166r (168r) | 295–336 | **294** « δούλοις γὰρ οὐκ ἔξεστ' ἀκούειν τῶν λόγων » → 336 « τῷ τῶν γυναικῶν ἢ 'πικηρυκεύεται » | **faux** |
| 09 | 166v (168v) | 337–379 | 337 « εὐριπίδη μήδοις ἐπὶ βλάβηι τινί » → 379 « …τίς ἀγορεύειν βούλεται » | exact |
| 10 | 167r (169r) | 380–422 | 380 « ἐγώ : περίθου νυν τόνδε… » → 422 « αὐτοὶ φοροῦσι κρυπτὰ κακοηθέστατα » | exact |
| 11 | 167v (169v) | 423–465 | 423 « λακωνίκ' ἄττα… » → 465 (une seule ligne) | exact |
| 12 | 168r (170r) | 466–508 | 466 « τὸ μὲν ὦ γυναῖκες… » → 508 « ἄπελθ' ἄπελθ'… » | exact |
| 13 | 168v (170v) | 509–550 | 509 « τέξειν· τὸ γὰρ ἦτρον… » → 550 « …ἁπαξαπάσας » | exact |
| 14 | 169r (171r) | 551–589 | 551 « ἀκούετ' ὦ γυναῖκες… » → **592** « πείθεσθε τούτωι ταῦτα… » | **faux** |
| 15 | 169v (171v) | 590–634 | **593** « ἠλίθιος ὅστις τιλλόμενος… » → **635** « ὅδ' ἐστὶν ἁνὴρ… : τί οὖν ποιῶ » | **faux** |
| 16 | 170r (172r) | 635–678 | **636** « ἀπόδυσον αὐτόν… » → 678 « κἂν μὴ ποιῶσι ταῦτα τοιάδ' ἔσται » | **faux** |
| 17 | 170v (172v) | 679–720 | 679 « αὐτῶν ὅταν ληφθῇ… » → 720 « λόγους τε λέξεις ἀνοσίους » | exact |
| 18 | 171r (173r) | 721–764 | 721 « ἀθέοις ἔργοις… » → **763** « φύλαξον αὐτὸν ἵνα λαβοῦσα κλεισθένη » | **faux** |
| 19 | 171v (173v) | 765–799 | **764** « τοῖσιν πρυτάνεσιν… » → **800** « ὑμῶν ἐσμὲν πολὺ βελτίους… » | **faux** |
| 20 | 172r (174r) | 800–837 | **801** « βάσανον δῶμεν… » → **834** « προεδρίαν… τηνίοισι καὶ σκίροις » | **faux** |
| 21 | 172v (174v) | 838–875 | **835** « ἔν τε ταῖς ἄλλαις ἑορταῖς… » → **876** « ἐπεὶ τέθνηκε πρωτέας ἔτη δέκα » | **faux** |
| 22 | 173r (175r) | 876–919 | **877** « ποίαν δὲ χώραν εἰσεκέλσαμεν σκάφει » → 919 « τὴν τυνδάρειον παῖδ'… » | **faux** |
| 23 | 173v (175v) | 920–958 | 920 « οἴμ' ὡς πανοῦργος… » → 958 « κυκλοῦσαν ὄμμα… » | exact |
| 24 | 174r (176r) | 959–1000 | 959 « ἅμα δὲ καὶ » → **1001** « ἐνταῦτα νῦν οἰμῶζ' εἰ πρὸς τὴν αἰτρίαν » | **faux** |
| 25 | 174v (176v) | 1001–1043 | **1002** « ὦ τοξόθ' ἱκετεύω σε… » → **1044** « ὃς ἐμὲ κροκόεντ' ἐνέδυσεν » | **faux** |
| 26 | 175r (177r) | 1044–1081 | **1045** « ἐπὶ δὲ τοῖσδε τόδ' ἀνέπεμψεν » → 1081 « οἴμωζε : ηχ οἴμωζε » | **faux** |
| 27 | 175v (177v) | 1082–1127 | 1082 « ὀτότυζε : ηχ ὀτότυζε » → **1126** « καὶ μὴν ποιήσω τοῦτο· τὸ κεπαλῆσ ἄρα » (+ 1102–1103 en marge inf.) | **faux** |
| 28 | 176r (178r) | 1128–1168 | **1127** « τὸ ξιπομάκαιραν ἀποκεκόψι τουτοΐ » → 1168 « ἃ νῦν ὑποικουρεῖτε… » | **faux** |
| 29 | 176v (178v) | 1169–1210 | 1169 « ἀπὸ τῆς στρατιᾶς… » → 1210 « …τὸ τυγάτριον » | exact |
| 30 | 177r (179r) | 1211–1231 | 1211 « κοὐ δύσκολ' ἀλλὰ πρᾶο… » → 1231 « τούτων χάριν ἀνταδοῖτον » | exact |

**Bilan.** Les bornes sont fausses pour **17 folios sur 30** (ff. 164v, 165r, 165v, 166r, 169r, 169v, 170r, 171r, 171v, 172r, 172v, 173r, 174r, 174v, 175r, 175v, 176r) (décalage d'un à trois vers, aux deux bouts dans plusieurs cas). Gemini n'a pas lu les pages : il a réparti les vers à partir d'un nombre moyen de lignes. Toute la chaîne qui en dépend est fausse : noms des fichiers images, tableau du README (§ 4.1–4.2), notices folio par folio, répartition des « 1 238 lignes » dans la transcription LaTeX (ex. v. 208 imprimé en tête du f. 165r, v. 1127 en fin du f. 175v), attribution des scholies aux folios.

**Incipit/explicit du README (§ 4.1).** Sur 60 mots-repères, une dizaine seulement figure à la place indiquée. Les autres sont absents de la ligne, voire du folio ou du texte. Exemples : f. 164r incipit « τᾶς Ἀσιάδος » (pas sur ce folio) ; f. 164v « αὐτὸς κἀγάθων » (R : αὐτός τε καλὸς) ; f. 165r « τί οὖν ἐμοὶ » et explicit « λάβωμεν » (mots absents) ; f. 166v « ἐπὶ κέρδεσιν… βουλεύσομεν » (absents) ; f. 167r explicit « κλεῖδας » (R : κλῄδια, v. 421) ; f. 168r explicit « τὸ ἦτρον (v. 508) » (v. 509, folio suivant) ; f. 168v incipit « τὸ δ' εἰσέφερε » (v. 505, folio précédent) ; f. 175v explicit « πέπυσται (v. 1127) » (πέπυσται est au v. 1227, f. 177r) ; f. 177r incipit « ὦ δύσκολλ' » (R : κοὐ δύσκολ').

### 3.2 Lectures diplomatiques (≥ 40)

*(en cours)*

### 3.3 Scholies et gloses transcrites (≥ 20)

*(en cours)*

### 3.4 Affirmations paléographiques

*(en cours)*

### 3.5 Affirmations historiques et bibliographiques

*(en cours)*

## 4. Ce qui est récupérable, et à quelles conditions

*(à rédiger)*

## 5. Erreurs typiques à éviter

*(à rédiger)*

## 6. Données utiles

*(à rédiger)*
