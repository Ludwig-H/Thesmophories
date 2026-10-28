# Études modernes sur les *Thesmophories* — recension

> **État** (28 octobre 2026) : recension complète dans ses six parties (reprise après interruption du
> 26 octobre : sections 2.4 à 6 rédigées, index par vers généré). Ce qui n'a pas pu être contrôlé sur le document
> lui-même est marqué **[à vérifier]** ; la liste des points ouverts est au § 6. Les éditions et commentaires sont
> recensés dans `recherche/bibliographie_editions.md`, les sources des conjectures des critiques des XVIe-XIXe s.
> dans `recherche/conjectures_sources.md`, les papyrus dans `recherche/papyrus.md`, la métrique dans
> `recherche/metrique_structure.md`, les ressources du Drive dans `recherche/drive_ressources.md` : on n'y revient
> ici que par renvoi.

## Plan

0. Conventions, sources de la recension, accès
1. Critique textuelle
   1.1 Études d'ensemble, comptes rendus d'éditions
   1.2 Critiques des XVIIIe-XIXe s. et premiers XXe s. (renvois ; notes du *Rheinisches Museum*)
   1.3 Notes et articles sur des passages précis (ordre chronologique)
   1.4 Attribution des répliques ; le nom du parent d'Euripide (Mnésiloque ou Kèdestès)
   1.5 Papyrus, scholies, tradition (renvois)
2. Interprétation, mise en scène, contexte
   2.1 Monographies, synthèses, recueils
   2.2 Date (411), contexte politique ; les *Secondes Thesmophories*
   2.3 La fête des Thesmophories ; femmes, religion, rite
   2.4 Les parodies d'Euripide (*Télèphe*, *Palamède*, *Hélène*, *Andromède*) ; paratragédie
   2.5 Agathon, Clisthène ; travestissement, genre, mimèsis
   2.6 Le Scythe et son grec
   2.7 Mise en scène, acteurs, costumes ; chœur, parabase, musique
   2.8 Langue, style, realia
3. Iconographie (cratère de Würzburg H 5697 et autres documents)
4. Index par vers des discussions textuelles et exégétiques
5. Accès libres téléchargés (`.sources/web/etudes/`)
6. Lacunes et vérifications à faire

## 0. Conventions, sources de la recension, accès

### 0.1 Forme des notices

Chaque notice donne : **clé** (auteur année, reprise dans l'index du § 4) — référence complète — résumé en
une ligne — *Vers* concernés — *Accès* — marque de vérification.

### 0.2 Marques de vérification

- **[lu]** : référence et contenu contrôlés sur le document (fichier local ou page en ligne) ;
- **[méta]** : référence contrôlée sur les métadonnées de l'éditeur ou d'un agrégateur (DOI enregistré chez
  Crossref, OpenAlex, Persée, JSTOR), contenu non lu ; le résumé vient alors du titre ou du résumé de
  l'auteur ;
- **[P]**, **[AO]**, **[S]**, **[A]**, **[CR]** : référence reprise d'une bibliographie imprimée, non
  contrôlée sur l'original : Prato 2001, *Indicazioni bibliografiche*, p. XLIII-LXXIX (extrait textuel
  `.sources/drive/ravennas/Prato_2001_LeDonneAlleTesmoforie_textrep.txt`) ; Austin–Olson 2004,
  *Abbreviations and Bibliography* et notes de l'introduction (extrait
  `.sources/drive/ravennas/AustinOlson_2004_Thesm_textrep.txt`) ; Sommerstein 1994, *Select Bibliography* et
  notes (extrait `.sources/drive/ravennas/Sommerstein_1994_Thesm_textrep.txt`) ; « Bibliographie [de
  C. Austin] 1964-2010 », *Eikasmos* 22 (2011) (`AR/C._Austin._Bibliographie_1964-2010_Eikas.pdf`) ;
  compte rendu cité dans la notice ;
- **[à vérifier]** : point précis non contrôlé (pagination, vers, contenu).

### 0.3 Accès (abréviations de chemins)

- `AR/` = `.sources/drive/fichiers/Grec/Aristophane/` ; `TH/` = `AR/Thesmophories/` ;
  `EU/` = `.sources/drive/fichiers/Grec/Euripide/` ; `DR/` = `.sources/drive/` (copies du Drive de
  l'auteur, documents sous droits, **non versionnés**) ;
- `W/` = `.sources/web/etudes/` (accès libres téléchargés pour cette recension, § 5) ;
  `ED/` = `.sources/web/editions/` et `ME/` = `.sources/web/metrique/` (téléchargés par d'autres chantiers) ;
- « DOI » seul = article sous abonnement (JSTOR, éditeur) ; « libre : URL » = accès libre en ligne non
  téléchargé (Persée et OpenEdition bloquent le téléchargement automatique par un défi anti-robot) ;
- « — » = aucun accès identifié.

### 0.4 Sources de la recension

1. Les articles du Drive de l'auteur, identifiés dans `recherche/drive_ressources.md` (§ 3.2-3.4, 4.3-4.5,
   5-7) et relus ici pour les vers et le résumé.
2. Les bibliographies de Prato 2001 (la plus complète pour 1880-2000 ; section 7, *Contributi filologici*,
   pour la critique textuelle), d'Austin–Olson 2004 et de Sommerstein 1994, et la bibliographie d'Austin.
3. Les comptes rendus des éditions (BMCR, *CR*, *Gnomon*, *Prometheus*, *Emerita*, etc.), qui discutent des
   leçons précises.
4. Une interrogation systématique d'OpenAlex (titres contenant *Thesmophoriazusae*, *Thesmophoriazusen*,
   *Tesmoforiazuse*, *Thesmophories*, *Tesmoforiantes*, *Thesmophoria*, etc. ; 333 notices, dont
   `.travail/etudes/oa_titles.tsv`) et des vérifications ponctuelles sur Crossref
   (`.travail/etudes/crossref_r1.tsv`).

### 0.5 Abréviations des ouvrages cités souvent

AO = C. Austin, S. D. Olson, *Aristophanes. Thesmophoriazusae*, Oxford, 2004 ; S. = A. H. Sommerstein,
*Aristophanes. Thesmophoriazusae*, Warminster, 1994 ; P. = C. Prato (éd.), D. Del Corno (trad.),
*Aristofane. Le donne alle Tesmoforie*, Milan, 2001 ; W. = N. G. Wilson, *Aristophanis fabulae*, t. II,
Oxford, 2007 ; Coulon = V. Coulon, H. van Daele, *Aristophane*, t. IV, Paris, CUF, 1928.

## 1. Critique textuelle

### 1.1 Études d'ensemble, comptes rendus d'éditions

**Études d'ensemble sur le texte**

- **Austin 1987** — C. Austin, « Textual Problems in Ar. *Thesm.* », *Δωδώνη* (Philologie) 16.2 (1987),
  p. 61-92 (avec *postscript*, p. 91-92). Histoire des contributions humanistes (Biset, Ellebodius,
  Casaubon, Le Fèvre, Bentley, Daubuz, l'« Anonymus Parisinus » de Raphelengius), puis répertoire vers par
  vers des conjectures anticipées (la priorité réelle d'une correction) et des notes inédites de Kaibel (cours
  d'Oxford, notes manuscrites), de Wilamowitz (séminaire « Graeca », d'après l'exemplaire de van Leeuwen
  annoté par P. Maas) et de Maas lui-même. Base indispensable pour attribuer les conjectures dans l'apparat.
  *Vers* : la pièce entière (plus de cent lieux, du v. 1 au v. 1231 ; propositions propres notamment aux
  vv. 113, 967). *Accès* : `TH/Textual problems in Ar Thesm Austin 1987.pdf` (= `DR/thesmophories/` et
  `DR/ravennas/`) ; libre : dépôt de l'Université de Ioannina, DOI 10.26268/heal.uoi.5377. [lu]
- **Austin 1990** — C. Austin, « Observations critiques sur les *Thesmophories* d'Aristophane », *Δωδώνη*
  (Philologie) 19.2 (1990), p. 9-29 (volume à la mémoire de I. Kambitsis). Discussion suivie d'une trentaine
  de lieux difficiles, avec critique des choix de Coulon et de Gannon. *Vers* : 2 (ἀλοῶν), 23-24, 34, 45,
  59-62, 64-65, 80, 120-122, 137-138, 158, 209-210, 247-248, 280-281, 289, 325-326, 365-369, 569,
  663-664, 696-697, 702-703, 710-713, 721-725, 902, 910 (ἐκ τῶν ἱστίων), 982-995, 1018-1019, 1050-1051,
  1226. *Accès* : `AR/1. Observations critiques sur les Thesmophories d' Aristophane.pdf` (couche texte du
  début du fascicule inutilisable, article lisible) ; libre : DOI 10.26268/heal.uoi.5411. [lu]
- **Austin 2002** — C. Austin, « Seven *cruces* in Aristophanes (*Acharnians* and *Thesmophoriazusae*) »,
  *QUCC* n.s. 72.3 (2002), p. 73-76. *Vers* : [à relever]. *Accès* : DOI 10.2307/20546745. [méta] [A]
- **Austin 2011** — C. Austin, « A baker's dozen: *Thesm.* 12, *Clouds* 1 », dans N. Almazova, O. Budaragina,
  S. Egorova *et al.* (éd.), *Variante loquella. Alexandro Gavrilov septuagenario*, Saint-Pétersbourg, 2011
  (= *Hyperboreus* 16-17, 2010-2011), p. 264-270. Note sur le v. 12, que Wilson supprime après van Herwerden.
  *Vers* : 12. *Accès* : — [A]
- **Gannon 1982-1988** — J. F. Gannon, *Thesmophoriazusae restitutae. An Essay in Annotation and
  Interpretation*, thèse, Yale University, 1982 [P] ; *Aristophanes' Thesmophoriazusae. Commentary* et
  *Text*, Bryn Mawr, 1987-1988 (Bryn Mawr Greek Commentaries) [P] [lu : cités par Austin 1990, p. 9 n. 3] ;
  *Notes on Selected Passages of Aristophanes' Thesmophoriazusae*, Bedford Hills (N.Y.), 1988 [S]. Texte
  souvent corrigé (« scripsi »), sévèrement jugé par Austin 1990. *Vers* : la pièce ; S. lui reprend
  ἐπίτρεχ' au v. 1214 et cite sa lecture du v. 710. *Accès* : —
- **Coulon 1933** — V. Coulon, *Essai sur la méthode de la critique conjecturale appliquée au texte
  d'Aristophane*, Paris, 1933. Plaidoyer conservateur de l'éditeur de la CUF, fréquemment cité pour la
  défense du texte de R. *Accès* : — [AO] [P]
- **Wilson 2007b** — N. G. Wilson, *Aristophanea. Studies on the Text of Aristophanes*, Oxford, 2007. Volume
  compagnon de l'OCT : justification des choix, chapitre propre aux *Thesmophories*. *Accès* : — (absent du
  Drive, cf. `recherche/drive_ressources.md` § 9.5). [méta] Comptes rendus : S. D. Olson, *CR* 60 (2010),
  p. 354-357, DOI 10.1017/S0009840X10000119 [méta] ; *Emerita* (2009), avec l'OCT (libre :
  emerita.revistas.csic.es, article 320, téléchargement automatique impossible) [à vérifier].

**Comptes rendus des éditions (leçons discutées : voir l'index du § 4)**

- *Coulon 1928* : A. Willem, *RBPh* 8 (1929), p. 548-550 [méta] ; G. Dalmeyda, *REG* 43 (1930), p. 218-220
  [méta] (Persée).
- *Sommerstein 1994* :
  - **Olson 1995** — S. D. Olson, *BMCR* 1995.02.21 (libre : bmcr.brynmawr.edu/?p=20656). Liste serrée de
    leçons : défend R aux vv. 140, 164, 314, 532, 794, 1203 ; discute 117-118, 288, 476, 500, 557, 581,
    809 (Ἄνυτος de Maas), 1013, 1114, 1197, 1215. [lu]
  - C. Austin, *CR* n.s. 45 (1995), p. 431-432, DOI 10.1017/S0009840X00294626 [méta] ; N. V. Dunbar, *JHS*
    116 (1996), p. 196-197, DOI 10.2307/631983 [méta] ; A. Blanchard, *REG* 109 (1996), p. 750-751 [méta] ;
    B. Vancamp, *AC* 64 (1995), p. 282 [méta] ; V. Gray, *Prudentia* 28 (1996), p. 74-76 [méta].
- *Prato 2001* :
  - **Olson 2002** — S. D. Olson, *BMCR* 2002.03.13 (libre : bmcr.brynmawr.edu/?p=22891) : édition « stop-gap »
    en attendant Austin ; date (Lénéennes) mal défendue. [lu]
  - **Macía Aparicio 2002** — L. M. Macía Aparicio, *Emerita* 70.2 (2002), p. 335-339 : discute la date
    (vv. 356-367, 840 : Prato place la pièce aux Lénéennes) ; signale des omissions dans la liste des écarts
    avec Coulon (v. 91) et dans la bibliographie. Libre : emerita.revistas.csic.es (article 117). [lu]
  - **Melandri 2004** — E. Melandri, *Prometheus* 30 (2004), p. 282-285 : attribution des vv. 276-279
    (coronis de PSI 1194), identification Écho-Euripide (vv. 1018-1021, 1056-1073), désaccords entre
    traduction, didascalies et commentaire (vv. 126, 662, 809, 875, 930-932, 1172-1177). *Accès* :
    `W/cr_Prato2001_Prometheus30_2004.pdf` ; libre : oaj.fupress.net. [lu]
- *Austin–Olson 2004* :
  - **Storey 2006** — I. C. Storey, *BMCR* 2006.01.05 (libre : bmcr.brynmawr.edu/?p=25137) : vv. 80 (R
    conservé), 87 (εἰς ταύτας de Sandbach préféré), 365-366 (obèles), 373 (Archikleia de Satyros), 557
    (οἶνον), 809 (Ἄνυτος), 910 (ἀμφίων de Grégoire, ἱστίων d'Austin 1990), quatrième acteur aux vv. 923-944.
    [lu] — Réponse : **Olson 2006**, *BMCR* 2006.03.33 (libre : bmcr.brynmawr.edu/?p=24591) : quatre acteurs,
    Euripide-personnage, vv. 387, 443-458, 561-562, *Thesm. II* (fr. 346). [lu]
  - J. Henderson, *CR* n.s. 56 (2006), p. 28-30, DOI 10.1017/S0009840X05000156 [méta] ; G. Mastromarco,
    *Gnomon* 80 (2008), p. 193-198, DOI 10.17104/0017-1417_2008_3_193 [méta] ; V. Tammaro, *Eikasmos* 17
    (2006), p. 490-494 (« osservazioni critico-testuali ed esegetiche ») [méta ; tomaison à vérifier] ;
    E. W. Scharffenberger, *AJPh* 127 (2006), p. 140-144, DOI 10.1353/ajp.2006.0020 [méta] ; J. M. Labiano
    Ilundain, *Exemplaria Classica* 10 (2006), p. 317-323 (libre : uhu.es, serveur injoignable lors du
    téléchargement) [méta] ; J.-M. Carbon, *Scholia Reviews* n.s. 15 (2006), n° 8 (`W/Carbon_2006_cr_Austin-Olson.pdf`)
    [lu] ; M. L. Lech, *Aigis* 5.1 (2005), en danois (`W/Lech_2024_Aigis_cr_Austin-Olson.pdf`) [lu] ;
    N. Arai, *Journal of Classical Studies* (Japon) 54 (2006), p. 121-124 [méta].
- *Wilson 2007 (OCT)* :
  - **Liberman 2008** — G. Liberman, *BMCR* 2008.07.50 : sur les *Thesm.*, v. 12 (suppression d'après van
    Herwerden adoptée par Wilson), v. 295 (conjecture d'Austin–Olson), v. 646 (désaccord texte/apparat), v. 1014
    (ἥκει, déjà Bothe) ; traitement des attributions jugé inégal. [lu]
  - H.-G. Nesselrath, *JHS* 131 (2011), p. 185-186, DOI 10.1017/S0075426911000279 [méta].

### 1.2 Critiques des XVIIIe-XIXe s. et premiers XXe s. (renvois)

Le détail (pages, vers, éditions relais) est dans `recherche/conjectures_sources.md` ; Austin 1987 reste la
source première pour les annotations manuscrites des humanistes et des XVIIe-XVIIIe s. Les ouvrages ci-dessous
sont déjà téléchargés par d'autres chantiers.

| Critique | Travaux utiles pour les *Thesm.* | Accès local |
|---|---|---|
| R. Bentley | *Emendationes ineditae in Aristophanem*, *Classical Journal* 13-14 (1816) ; voir Austin 1987, p. 66-67 | `AR/emendations thesmophories valpy barker*.pdf` ; `ED/1816_Classical_Journal_13`, `_14` |
| R. Porson | *Adversaria* (1812) ; *Tracts* (1815) ; *Aristophanica* (1820, éd. P. P. Dobree) | `ED/1812_Cambridge_Porson_Adversaria`, `ED/1815_Londres_Porson_Tracts`, `ED/1820_Cambridge_Porson_Notae` |
| P. Elmsley | *Quarterly Review* 7 (1812), p. 454 ; *Acharnenses* (1830) | `ED/1812_Quarterly_Review_7_Elmsley`, `ED/1830_Leipzig_Elmsley_Acharnenses` |
| P. P. Dobree | *Adversaria*, éd. J. Scholefield, t. II, Cambridge, 1833, p. 236-241 (P.) ; réimpr. 1843, éd. G. Wagner 1874 | `ED/1843_Dobree_Adversaria_t2`, `ED/1874_Dobree_Adversaria_Wagner` |
| G. Hermann | c. r. de Fritzsche, *ZfAW* 1838 ; c. r. d'Enger, *ZfAW* 1845 = *Opuscula* VIII (1877), p. 288-308 | `ED/1838_ZfAW_5_Hermann_Fritzsche`, `ED/1877_Hermann_Opuscula_VIII`, `TH/Godofredi Hermanni Opuscula*.pdf` |
| R. Enger | « Beiträge zur Kritik und Erklärung der *Thesmophoriazusen* … und der Scholien », *RhM* 2 (1843) ; « Zu Aristophanes *Thesmophoriazusen* », *RhM* 5 (1846) ; éd. 1844 | `ED/1843_Enger_Beitraege_RhM`, `ED/1846_Enger_Zu_Thesm_RhM`, `ED/1844_Bonn_Enger` |
| J. Lenting ; G. A. Hirschig ; J. H. Voss | *Observationes criticae* (1839) ; *Annotationes in Aristophanem* (1849) ; *Anmerkungen und Randglossen* (1838), p. 115 | `ED/1839_Zutphen_Lenting_Observationes`, `ED/1849_Utrecht_Hirschig_Annotationes`, `ED/1838_Leipzig_Voss_Anmerkungen` |
| C. G. Cobet | « Variae lectiones », *Mnemosyne* 2 (1853), p. 210-213 ; *Novae lectiones* (1858) ; *Variae lectiones*² (1873) | `ED/articles_jstor/4423862.pdf`, `ED/1858_Cobet_Novae_lectiones`, `ED/1873_Cobet_Variae_lectiones` |
| H. G. Hamaker | « Aanteekeningen op eenige plaatsen van Aristophanes », *Mnemosyne* 5 (1856), p. 291-306 | `ED/articles_jstor/4423940.pdf` |
| A. Meineke | *Vindiciarum Aristophanearum liber*, Leipzig, 1865 (*Thesm.* p. 143-161) | `ED/1865_Leipzig_Meineke_Vindiciae` |
| H. van Herwerden | *Analecta critica* (1868) ; « Ad comicos Graecos », *Mnemosyne* 10 (1882), p. 86 [P] ; *Vindiciae Aristophaneae*, Leyde, 1906 (1900 selon P.) | `ED/1868_Herwerden_Analecta`, `ED/1906_Leyde_Herwerden_Vindiciae` |
| A. von Velsen | « Zur Kritik des Aristophanes » (1865) ; *Über den Codex Urbinas* (1871) ; éd. 1878, 1883 | `ED/articles_jstor/41249869.pdf`, `ED/1871_Halle_Velsen_Codex_Urbinas`, `ED/1883_Leipzig_Velsen` |
| O. Bachmann | *Coniecturarum observationumque Aristophanearum specimen* I, Göttingen, 1878 ; « Zur Kritik der Komödien des Aristophanes », *Philologus* Suppl. 5 (1889), p. 231-260 [P] | `ED/1878_Goettingen_Bachmann` |
| F. H. M. Blaydes | éd. 1880 (*Addenda* p. 260-271) ; *Adversaria critica in Aristophanem*, Halle, 1899 | `ED/1880_Halle_Blaydes`, `ED/1899_Halle_Blaydes_Adversaria` |
| G. Kaibel | « Sententiarum liber quartus », *Hermes* 22 (1887), p. 497-500 : v. 162 (χλιδαῖς θ' ὅσοιπερ ἁρμονίαν ἐχύμισαν pour κἀλκαῖος ὅσπερ), vv. 498-501 (interpolation), vv. 31-33 (un vers interpolé) ; notes manuscrites et cours inédits (vers 1890) sur l'éd. de Velsen, connus par Austin 1987, p. 68 | `ED/1887_Hermes_22_Kaibel` [lu] |
| W. Lange | *Quaestiones in Aristophanis Thesmophoriazusas*, diss. Göttingen, 1891 | `ED/1891_Goettingen_Lange`, `ME/langequaestionesinaristopha` |
| K. Zacher | *Kritisch-grammatische Parerga zu Aristophanes*, Leipzig, 1899 [P] | — |
| C. O. Zuretti | « Osservazioni all'*Alcesti* di Euripide e alle *Tesmoforiazuse* di Aristofane », *RFIC* 29 (1901), p. 529-566 [P] | — |
| V. Coulon | *Quaestiones criticae in Aristophanis fabulas*, Strasbourg, 1907 | `ED/1907_Strasbourg_Coulon_Quaestiones` |
| H. Richards | *Aristophanes and Others*, Londres, 1909 | `ED/1909_Londres_Richards` |
| U. von Wilamowitz-Moellendorff | « Die Zeit der *Thesmophoriazusen* », *Aristoteles und Athen* II (1893), p. 343-355 ; *Griechische Verskunst* (1921) ; « Lesefrüchte », *Hermes* 64 (1929), p. 467-469 (v. 1047 : ἂν ἔτικτε pour l'ἀνέτικτε de R, p. 467, d'après Coulon 1957 ; v. 295, p. 468-469, d'après S.) ; *Kleine Schriften* IV (1962), p. 484-488 (P.) [contenu à identifier] ; suggestions orales du séminaire « Graeca » (fin des années 1920) transmises par les notes de P. Maas (Austin 1987 ; Sansone 1987, p. 226 n. 15 : ἀπὸ γνώμης au v. 148) | `ME/wilamowitz1893_AuA2`, `ME/griechischeversk00wila` |

*Notes du* Rheinisches Museum *(XIXe s., accès libre, téléchargées pour cette recension)*

- **Schöne 1847** — F. W. Schöne, « Zu Aristophanes (Thesm.) », *RhM* 5 (1847), p. 627-628. DOI
  10.18716/ojs/rhm/1847.5.4125. *Vers* : [à relever : texte en Fraktur mal océrisé]. *Accès* :
  `W/Schoene_1847_RhM5_Zu_Ar_Thesm.pdf`. [méta]
- **Ritschl 1862** — F. Ritschl, « Zu Aristophanes (Thesm.) », *RhM* 17 (1862), p. 460-462 : partage des
  répliques aux vv. 8-10 et ἀκοῆς δὲ χοάνην au v. 18 (contre l'objection de G. Hermann, *ZfAW* 1838, p. 672 ;
  1845, p. 906). DOI 10.18716/ojs/rhm/1862.17.4822. *Vers* : 8-10, 18. *Accès* : `W/Ritschl_1862_RhM17_Zu_Ar_Thesm.pdf`. [lu, OCR
  médiocre]
- **Anonyme 1863** — « Zu Aristophanes' Thesm. », *RhM* 18 (1863), p. 155-156 : réponse à Ritschl 1862 sur le
  v. 18 et la scholie (χοάνη). DOI 10.18716/ojs/rhm/1863.18.4870. *Vers* : 18. *Accès* :
  `W/Anonyme_1863_RhM18_Zu_Ar_Thesm.pdf`. [lu, OCR médiocre]
- **Ritschl 1867** — F. Ritschl, « Zu Aristophanes (Thesm.) », *RhM* 22 (1867), p. 638 : responsion du chant
  d'Agathon et des Muses : au v. 106, μάκαρας pour δαίμονας (répétition maladroite après δαιμόνων, responsion
  avec le v. 113). DOI 10.18716/ojs/rhm/1867.22.5266. *Vers* : 106, 113. *Accès* :
  `W/Ritschl_1867_RhM22_Zu_Ar_Thesm.pdf`. [lu, OCR médiocre]

### 1.3 Notes et articles sur des passages précis (ordre chronologique)

**1900-1959**

- **Willems 1908** — A. Willems, « Notes sur les *Thesmophories* et le *Ploutos* d'Aristophane », *Bulletins
  de l'Académie royale de Belgique* (Classe des lettres), n° 11 (novembre 1908), p. 625-693 (tiré à part
  paginé 3-71) = *Aristophane. Traduction avec notes et commentaires critiques*, Paris-Bruxelles, 1919,
  t. II, p. 535-579. Vingt-huit notes, presque toujours pour défendre R contre les corrections. *Vers* :
  16-18, 21, 22-24, 60, 217, 230, 263, 280-281, 289-291, 352-354, 365-367, 400-401, 418-420, 499-501,
  509-510, 531-532, 569, 575-576, 592-593, 655-686 (chœur), 656, 710-712, 773-774, 808-809, 811-812,
  1019-1020, 1050-1051, 1052-1055, 1181. *Accès* : tiré à part, `W/willems1908/Willems_1908_Notes_Thesm_Ploutos_BullAcadBelg.pdf`
  (domaine public, dépôt de l'ULB) ; texte repris dans les annexes de l'auteur (`latex/Aristophane-Thesmo Annexes.tex`, cf. `recherche/travaux_anterieurs.md` § 9.2). [lu]
- **Maas 1913** — P. Maas, « Zu Aristophanes *Thesmophoriazusen* », *RhM* 68 (1913), p. 355-360 (=
  *Kleine Schriften*, Munich, 1973, p. 54-58). v. 2 : ἀλύων pour ἀλοῶν (appuyé sur la scholie) ; vv. 275-279 :
  la leçon ἔκσπευδε n'a jamais été sérieusement défendue ; vv. 601-605 : transposition du v. 604 avant le v.
  603 (adoptée par S.) ; vv. 808-809 : Ἄνυτος pour αὐτός (le stratège de 410/09). *Accès* :
  `W/Maas_1913_RhM68_Zu_Ar_Thesm.pdf` ; libre : DOI 10.18716/ojs/rhm/1913.68.8332. [lu]
- **Coulon 1926** — V. Coulon, « Notes critiques sur deux hyperbates dans le *Plutus* (v. 119 et 512) et sur
  un passage des *Thesmophoriazusai* (v. 241-47) d'Aristophane », *REG* 39 (1926), p. 90-96. *Vers* :
  241-247. *Accès* : libre (Persée), DOI 10.3406/reg.1926.5236. [méta]
- **Coulon 1929** — V. Coulon, « Notes sur quelques passages de *Lysistrata* et sur *Thesm.* 450-52 et 460
  et *Cav.* 975 d'Aristophane », *REG* 42 (1929), p. 11-19. *Vers* : 450-452, 460. *Accès* : libre
  (Persée), DOI 10.3406/reg.1929.6920. [méta]
- **Coulon 1930, 1931** — V. Coulon, « Notes supplémentaires sur quelques passages d'Aristophane », *REG* 43
  (1930), p. 295-308, DOI 10.3406/reg.1930.6982 ; « Notes critiques et exégétiques sur Aristophane, Ménandre
  et Anacréon », *REG* 44 (1931), p. 8-33, DOI 10.3406/reg.1931.6999. *Vers* : 1047 (1931, p. 13 : approuve
  l'ἂν ἔτικτε de Wilamowitz, d'après Coulon 1957) [autres vers à relever]. *Accès* : libre (Persée). [méta]
- **Coulon 1934a** — V. Coulon, « Notes sur Aristophane et sur deux passages d'une inscription chrétienne
  d'Asie-Mineure », *REG* 47 (1934), p. 421-443. *Vers* : 63, 280-281, 706, 941-945, 1030, 1224.
  *Accès* : `AR/Coulon notes sur Aris et sur deux passages.pdf` ; libre (Persée), DOI 10.3406/reg.1934.7186.
  [lu]
- **Coulon 1934b** — V. Coulon, « Interprétation d'un passage d'Aristophane imité par les conteurs du moyen
  âge », dans *Mélanges Bidez*, t. II, Bruxelles, 1934, p. 122-134. *Vers* : [à identifier]. [P]
- **Allen 1935** — J. T. Allen, « Notes on Aristophanes », *CPh* 30 (1935), p. 262-264. *Vers* : [à relever].
  *Accès* : DOI 10.1086/361857. [méta] [P]
- **Coulon 1937** — V. Coulon, « Notes critiques et exégétiques sur Aristote, *Poétique*, 1450 a 12, 1450
  a 29, sur Thucydide, I, 1, 2 et sur cinq passages d'Aristophane », *REG* 50 (1937), p. 443-458 (*Thesm.* :
  p. 454-458 selon P.). Chant d'Agathon. *Vers* : 126-129, 1170. *Accès* : `AR/Coulon notes criti et ex chant agathon Nietsche.pdf` ; libre (Persée), DOI 10.3406/reg.1937.8180. [lu]
- **Gordziejew 1937** — W. Gordziejew, « De prologo *Thesmophoriazusarum* », *Eos* 38 (1937), p. 296-324.
  *Vers* : 1-294. *Accès* : — [AO] [P]
- **Moreau 1938** — J. Moreau, « Note sur le vers 1174 des *Thesmophories* d'Aristophane », *AC* 7 (1938),
  p. 227-231. *Vers* : 1174. *Accès* : libre (Persée), DOI 10.3406/antiq.1938.3169. [méta]
- **Grégoire 1938** — H. Grégoire, « De l'utilité du grec moderne », *Byzantion* 13 (1938), p. 396-399 :
  ἐκ τῶν ἀμφίων au v. 910 (d'après Storey 2006, qui regrette qu'AO ne l'aient pas discutée). *Vers* : 910.
  *Accès* : — [P] [CR] [à vérifier : Crossref ne connaît, de Grégoire en 1938, que « Utilité et charme du grec
  moderne », *RBPh* 17 (1938), p. 5-26]
- **Goossens 1941** — R. Goossens, « Notes sur quelques papyrus littéraires », *Chronique d'Égypte* 16
  (n° 31, janvier 1941), p. 105-106 (d'après `recherche/papyrus.md`) : I. *Thesm.* 242 (PSI 1194). *Vers* : 242. *Accès* : `DR/papyrus/Notes sur quelques papyrus littéraires PSI1194 Thesmophories.pdf`. [lu, d'après `recherche/drive_ressources.md` § 3.3]
- **Coulon-Tauber 1943** — V. Coulon-Tauber, « Beiträge zur Interpretation des Aristophanes », *Philologus*
  95 (1943 ; daté 1942 dans P.), p. 31-54. *Vers* : [à relever]. *Accès* : DOI 10.1524/phil.1943.95.14.31.
  [méta]
- **Campbell 1949** — A. Y. Campbell, « Aristophanes *Thesmophoriazusae* 855-7 and Euripides *Helena* 1-3 »,
  *CR* 63 (1949), p. 81-83 : lire λεύκῃ νοτίζει (λεύκη, la « lèpre blanche », endémique en Égypte) pour λευκῆς
  νοτίζει, en gardant πέδον et le datif de van Herwerden (μελανοσυρμαίῳ λεῴ). *Vers* : 855-857. *Accès* :
  `AR/thesmophories 855 10.1017_S0009840X00095068.pdf`. [lu]
- **Coulon 1953** — V. Coulon, « Notes critiques et exégétiques sur divers passages controversés d'Aristophane
  et sur Sophocle, *Antigone* 613-614 », *REG* 66 (1953), p. 34-55. *Vers* : 100, 142, 166-168, 217, 285,
  806, 995. *Accès* : `AR/Coulon notes critiques et exégétiques.pdf` ; libre (Persée), DOI
  10.3406/reg.1953.3304. [lu]
- **Koster 1955** — W. J. W. Koster, « Ad Aristophanis *Thesmophoriazusarum* fragmenta in PSI 1194 servata :
  de coronide ; de parepigrapha ; de proceleusmatico », *Acme* 8 (1955), p. 93-103. *Vers* : 273-288
  (fragment de PSI XI 1194 ; coronis après le v. 276, cf. Melandri 2004). *Accès* : — [P]
- **Jackson 1955** — J. Jackson, *Marginalia scaenica*, Oxford, 1955. Conjectures dispersées sur la tragédie
  et la comédie ; pour les *Thesm.*, p. ex. κατ' αὐτοὺς ἐς au v. 1226 (apparat de S.). *Accès* : — [AO] [S]
- **Grassi 1956** — E. Grassi, « Nuovi papiri fiorentini. III. Aristophanes, *Thesmoph.* 139-144 », *SIFC*
  27-28 (1956), p. 48 (= PSI XIV, p. XV). *Vers* : 133-144. *Accès* : — [P] ; voir `recherche/papyrus.md`.
- **Coulon 1957** — V. Coulon, « Aristophanes, *Thesmophoriazusen* 1015-1055 », *RhM* 100 (1957), p. 186-198 :
  monodie d'Andromède (texte, colométrie, interprétation). *Vers* : 1015-1055. *Accès* :
  `W/Coulon_1957_RhM100_Thesm_1015-1055.pdf` ; libre : DOI 10.18716/ojs/rhm/1957.100.9392. [lu]
- **Wycherley 1959** — R. E. Wycherley, « *Thesmophoriazusae* 986 », *CR* n.s. 9 (1959), p. 205-206.
  *Vers* : 986. *Accès* : `AR/thesmophories 986 wycherley1959.pdf`. [lu, d'après `recherche/drive_ressources.md`]

**1960-1999**

- **Taillardat 1961** — J. Taillardat, « Ποσθαλίων et ποσθαλίσκος (Ar. *Thesm.* 291) », *RPh* 35 (1961),
  p. 249-250. *Vers* : 291. *Accès* : — [P]
- **Fraenkel 1962** — E. Fraenkel, *Beobachtungen zu Aristophanes*, Rome, 1962 (Storia e letteratura 84) ;
  c. r. de K. J. Dover, « Notes on Aristophanes », *CR* n.s. 13 (1963), p. 272-274 (`AR/Notes Dover sur Fraenkel*.pdf`). *Vers* : [chapitres sur les *Thesm.* à relever]. [AO] [lu pour Dover]
- **Box 1964** — H. Box, « Aristophanes: *Birds* 785-96, and *Thesmophoriazusae* 450-1 », *CR* n.s. 14
  (1964), p. 241-242 : la plainte de la tresseuse de couronnes (« Euripide a persuadé les hommes que les dieux
  n'existent pas ») suppose des femmes au théâtre tragique. *Vers* : 450-451. *Accès* : `AR/thesmophories 450.pdf`. [lu]
- **Marzullo 1964** — B. Marzullo, « Aristophanea (II). Osservazioni critiche sul testo di Aristofane », dans
  J. Irmscher *et al.* (éd.), *Miscellanea critica* I, Leipzig, 1964, p. 129-138. [P]
- **Kamerbeek 1967** — J. C. Kamerbeek, « Notes sur quelques passages des *Thesmophories* d'Aristophane », dans
  *Κωμῳδοτραγήματα. Studia Aristophanea viri Aristophanei W. J. W. Koster in honorem*, Amsterdam, 1967,
  p. 74-81. *Vers* : 18 (p. 74 : défense de l'ἀκοῆς δὲ χοάνην de Biset, d'après Austin 1987, p. 70) [autres
  vers à relever]. [P]
- **Taillardat 1972** — J. Taillardat, communication à l'Association pour l'encouragement des études grecques
  (défense du texte transmis), résumée dans les « Actes de l'Association », *REG* 85 (1972), p. IX-XXXI.
  *Vers* : 123-127. *Accès* : `TH/thesm 123-7 Taillardat*.pdf`. [lu, d'après `recherche/drive_ressources.md`]
- **Thomsen 1973** — O. Thomsen, « Some Notes on the *Thesmophoriazusae* 947-1000 », dans *Classica et
  Mediaevalia F. Blatt septuagenario dedicata* (C&M Dissertationes 9), Copenhague, 1973, p. 27-46. Ode de
  danse (structure, texte : vv. 967-968, 995). *Vers* : 947-1000. *Accès* : — [S] [P] ; cité par Austin 1987.
- **Austin 1974** — C. Austin, « Adnotatiunculae in *Thesmophoriazusas* », *PCPhS* n.s. 20 (1974), p. 1-2 ;
  p. ex. κατὰ γνώμην au v. 148 (Sansone 1987, p. 225 n. 1). *Vers* : 148 [autres à relever]. *Accès* : DOI
  10.1017/S0068673500001425. [méta] [A]
- **Austin 1975** — C. Austin, « Aristophane, *Thesmophories*, vers 500 », dans J. Bingen, G. Cambier,
  G. Nachtergael (éd.), *Le Monde grec. Pensée, littérature, histoire, documents. Hommages à Claire Préaux*,
  Bruxelles, 1975, p. 126-127. *Vers* : 500. [A] [P]
- **Austin 1971-1974** — C. Austin, « Le rôle de la coryphée dans les *Thesmophories* », *Dioniso* 45
  (1971-1974), p. 316-325. Attribution de répliques à la coryphée (cf. § 1.4). [A] [P]
- **Marzullo 1975-1977** — B. Marzullo, « Aristoph. *Thesm.* 499-501 », *MCr* 10-12 (1975-1977), p. 141-142.
  *Vers* : 499-501. [P]
- **Tammaro 1975-1977** — V. Tammaro, « Aristoph. *Thesm.* 813 », *MCr* 10-12 (1975-1977), p. 147-150.
  *Vers* : 813. [P]
- **Austin 1977** — C. Austin, « Aristophanes, *Thesmophoriazusae* 242 », *ZPE* 26 (1977), p. 64. *Vers* :
  242. [A] [P]
- **Dover 1977** — K. J. Dover, article dans *ICS* 2 (1977), p. 147-148 (v. 1187b, parépigraphe d'origine
  ancienne) et p. 150-156 (variantes d'auteur, à propos des vv. 11-18) d'après S. [titre et pagination à
  vérifier]. [S]
- **Marzullo 1978-1982** — B. Marzullo, *MCr* 13-14 (1978-1979), p. 219 sqq. ; « Aristoph. *Thesm.* 242 »,
  *MCr* 15-17 (1980-1982), p. 219-221. *Vers* : 242. [P]
- **Residori 1979** — D. Residori, « Note sceniche alle *Tesmoforiazuse* di Aristofane », *Studi e Ricerche
  dell'Istituto di Latino* (Gênes) 2 (1979), p. 163-170. *Vers* : 295 (nom de la héraut, d'après S.) [autres
  à relever]. [P] [S]
- **Austin 1980** — C. Austin, « The Florence Papyrus of Ar. *Thesm.* », dans R. Pintaudi (éd.),
  *Miscellanea papyrologica* [in memoriam H. C. Youtie] (Papyrologica Florentina 7), Florence, 1980,
  p. 11-12, pl. I. [A] ; voir `recherche/papyrus.md`.
- **Seager 1981** — R. Seager, « Notes on Aristophanes », *CQ* 31 (1981), p. 244-251 : v. 33 (énoncé, non
  question) ; vv. 754-757 (jeu de scène de l'outre, adopté par S.) ; autres pièces. *Accès* : DOI
  10.1017/S0009838800009563. [méta] [S]
- **Medaglia 1982-1996** — S. M. Medaglia, « Note sui testi comici », *Bollettino dei Classici* s. III, 3
  (1982), p. 154-164 (S. : p. 154-159) ; « Postilla », *ibid.* 4 (1983), p. 137 ; « Nuova postilla », *ibid.*
  17 (1996), p. 96-100. Lecture de PSI 1194 qui résout la crux du v. 242 (« definitively solved », S.) ;
  approuvée par Austin 1984. *Vers* : 242. [P] [S] — avec M. Manfredi, *ibid.* 4 (1983), p. 137 [P].
- **Seager 1983** — R. Seager, « Aristophanes *Thes.* 493-496 and the Comic Possibilities of Garlic »,
  *Philologus* 127 (1983), p. 139-142. *Vers* : 493-496. [P]
- **Austin 1984** — C. Austin, « Aristophanes, *Thesmophoriazusae* 242 again », *ZPE* 57 (1984), p. 58.
  *Vers* : 242. *Accès* : capture d'écran `AR/ZPE LVII 1984.png`. [lu, d'après `recherche/drive_ressources.md`]
- **Marzullo 1984-1985** — B. Marzullo, « Aristoph. *Thesm.* 277-294 », *MCr* 19-20 (1984-1985), p. 93-97.
  *Vers* : 277-294. [P]
- **Blanc–Taillardat 1986** — A. Blanc, J. Taillardat, « Aristophane, *Thesmophories*, v. 366 : τῆς χώρας
  οὕνεκα et l'ambition des oligarques dans l'hiver de 412-411 », *RPh* 60 (1986), p. 183-186 (discuté par
  Austin 1987, p. 77, et Austin 1990 ; AO impriment le passage entre obèles). *Vers* : 365-366. *Accès* :
  `TH/Thesmophories_v.366.pdf` (image). [lu, d'après `recherche/drive_ressources.md`]
- **Hose 1986-1987** — M. Hose, « Aristoph. *Thesm.* 1015 », *MCr* 21-22 (1986-1987), p. 143-144. *Vers* :
  1015. [P]
- **Sansone 1987** — D. Sansone, « Aristophanes, *Thesmophoriazusae* 148 », *CQ* 37 (1987), p. 224-227 :
  ἅμα γνώμῃ est sans parallèle ; lire ἀπὸ γνώμης (« de propos délibéré »), déjà suggéré au séminaire de
  Wilamowitz (n. 15). *Vers* : 148. *Accès* : `AR/Aristophanes_Thesmophoriazusae_148.pdf` (= `AR/thesmophories 148.pdf`) ; DOI 10.1017/S0009838800031815. [lu]
- **Taillardat 1988** — J. Taillardat, communication résumée dans les « Actes de l'Association », *REG* 101
  (1988), p. IX-XXVIII (*Thesm.* p. XVI-XIX selon P.) : essai d'interprétation du texte transmis. *Vers* : 247,
  289, 721-725. *Accès* : `AR/reg_0035-2039_1988_num_101_482_1536.pdf`. [lu, d'après
  `recherche/drive_ressources.md`]
- **Thomsen 1988** — O. Thomsen, « Drei Emendationen zu den *Thesmophoriazusen* des Aristophanes : 369, 1019,
  1051 », *C&M* 39 (1988), p. 15-18. *Vers* : 369, 1019, 1051. [P]
- **Viketos 1989** — E. Viketos, « Aristophanes, *Thesmophoriazusae* 148-152 », *Hermes* 117 (1989), p. 359 :
  ἐμῇ γνώμῃ pour ἅμα γνώμῃ (ἅμα venu de δράματα au v. 150). *Vers* : 148. *Accès* : `AR/Thesmophories 148-152 4476703.pdf`. [lu]
- **Ciriello–Imperio 1991** — S. Ciriello, O. Imperio, « Nota ad Aristofane, *Tesmoforiazuse* 57b-62 », *AFLB*
  34 (1991), p. 89-93. *Vers* : 57-62. [P]
- **Mureddu 1992** — P. Mureddu, « La "incomunicabilità" gorgiana in una parodia di Aristofane ? Nota a
  *Thesm.* 5, 21 », *Lexis* 9-10 (1992), p. 1-6. *Vers* : 5, 21. [P]
- **Prato 1993-1999** — C. Prato, « Note al testo delle *Tesmoforiazuse* », dans R. Pretagostini (éd.),
  *Tradizione e innovazione nella cultura greca da Omero all'età ellenistica. Scritti in onore di B. Gentili*,
  t. II, Rome, 1993, p. 695-701 [P] ; « La cosiddetta "versione lirica" dell'ἀρά nelle *Tesmoforiazuse*
  (vv. 352-371) », dans B. Gentili, F. Perusino (éd.), *Mousike. Metrica, ritmica e musica greca in memoria di
  G. Comotti*, Pise-Rome, 1995, p. 277-285 [P] ; « Annotazioni linguistiche e filologiche al testo delle
  *Tesmoforiazuse* », *Rudiae* 9 (1997), p. 223-227 (221-228 selon OpenAlex) [P] [méta] ; « Note critiche ed
  esegetiche al testo delle *Tesmoforiazuse* », *QUCC* n.s. 58 (1998), p. 69-74, DOI 10.2307/20546529 [méta] ;
  « Note esegetico-testuali alle *Tesmoforiazuse* di Aristofane », *RCCM* 39 (1998), p. 269-273 [P] ;
  « Osservazioni linguistiche e filologiche sul testo delle *Tesmoforiazuse* », dans *Per Carlo Corbato.
  Scritti di filologia greca e latina*, Pise, 1999, p. 73-79 [P]. Notes préparatoires à l'édition de 2001.
  *Vers* : 352-371 [autres à relever].
- **Marzullo 1994** — B. Marzullo, « Aristoph. *Thesm.* 241 s. », *MCr* 29 (1994), p. 181-183. *Vers* :
  241-242. [P]
- **Notsu 1995** — H. Notsu, « Ar. *Thesm.* 295-382 : problem of attribution re-examined » (en japonais),
  *Journal of Classical Studies* (Japon) 43 (1995), p. 12-21, DOI 10.20578/jclst.43.0_12. *Vers* : 295-382.
  [méta]
- **Degani 1996** — E. Degani, « Ar. *Thesm.* 638 », *Eikasmos* 7 (1996), p. 119-120. *Vers* : 638.
  *Accès* : — (le fichier `AR/Eikasmos VII Deganis Ar Thesm 638.pdf` ne contient pas la note : voir
  `recherche/drive_ressources.md` § 3.3). [P]
- **Bierl 1999** — A. Bierl, « Doppeltanz oder doppelte Freude ? Gedanken zum umstrittenen διπλῆν
  (Ar. *Thesm.* 982) aus einer performativen Perspektive », dans *Der Chor im antiken und modernen Drama*,
  Stuttgart-Weimar, Metzler, 1999, p. 27-47 [éditeurs du volume à vérifier] ; libre : edoc.unibas.ch/13145
  (métadonnées du dépôt). *Vers* : 982. [méta]

**2000-2026**

- **Lourenço 2000** — F. Lourenço, « Metrical Notes on "Andromeda's Lament" in *Thesmophoriazusae* »,
  *Euphrosyne* n.s. 28 (2000), p. 321-324, DOI 10.1484/J.EUPHR.5.123914. *Vers* : 1015-1055. [méta] ; voir
  `recherche/metrique_structure.md`.
- **Hartwig 2008** — A. Hartwig, « Interpretive Notes on Aristophanes' *Thesmophoriazusae* », *Philologus*
  152 (2008), p. 49-64 : lecture phallique du v. 910 ; v. 982 = prière aux dieux et non auto-exhortation
  du chœur ; v. 984 = allusion au jeûne des choreutes ; authenticité du v. 1187b (non parépigraphe). *Vers* :
  910, 982, 984, 1187b. *Accès* : `AR/thesmophor 910.pdf` ; DOI 10.1524/phil.2008.0013. [lu]
- **Cowan 2008** — R. Cowan, « Nothing to do with Phaedra ? Aristophanes, *Thesmophoriazusae* 497-501 »,
  *CQ* 58 (2008), p. 315-320 : l'amant qui s'échappe la tête enveloppée (ἐγκεκαλυμμένον) pendant que la femme
  montre l'ἔγκυκλον à son mari n'appelle pas de correction (contre van Leeuwen et l'εὖ κεκαλυμμένον d'Austin) :
  le détail, juste après le nom de Phèdre, évoque l'*Hippolyte voilé* d'Euripide. *Vers* : 497-501. *Accès* :
  `AR/thesmophories 497-501.pdf` ; DOI 10.1017/S000983880800027X. [lu]
- **Hartwig 2009** — A. Hartwig, « Feasting and Flattering the Crows : A Reinterpretation of Aristophanes,
  *Thesmophoriazusae* 942 », *Mnemosyne* 62 (2009), p. 90-93 : κόραξιν est complément de γέλωτα παρέχω
  (contre AO) et ἑστιῶν, en fin de vers, fait du Parent exposé l'« hôte » qui régale les corbeaux. *Vers* : 942. *Accès* : `AR/thesmophories 942 10.2307@27736297.pdf` ; DOI 10.1163/156852508X252920. [lu]
- **Hartwig 2009b** — A. Hartwig, « A πῶλος Joke in Aristophanes ? (*Thesm.* 1210-11) », *RhM* 152 (2009),
  p. 218-220 : l'archer décrit Élaphion (« faon ») comme une pouliche, πῶλος, animal rétif, d'où un jeu de mots
  sur la courtisane. DOI 10.18716/ojs/rhm/2009.152.11213. *Vers* : 1210-1211. *Accès* :
  `W/Hartwig_2009_RhM152_polos_1210-1211.pdf` ; libre (RhM). [lu]
- **Méndez Dosuna 2010** — J. V. Méndez Dosuna, « Aristófanes, *Tesmoforiantes* 1054-1055 : ¿un raudo viaje
  al Hades o una abigarrada danza macabra ? » [volume à identifier]. *Vers* : 1054-1055. [méta]
- **Di Bari 2010, 2013** — M. F. Di Bari, « Note ai finali dei *Cavalieri* e delle *Tesmoforiazuse* di
  Aristofane », *RFIC* 138 (2010), p. 34-62 ; *Scene finali di Aristofane. Cavalieri, Nuvole, Tesmoforiazuse*
  (Prosopa 7), Lecce, 2013 (c. r. F. Montana, *RFIC* 143, 2015, p. 500-504 ; E. Solimando, *Maia* 67, 2015,
  p. 205-209). *Vers* : 1160-1231. [méta]
- **Boccaccini 2012** — C. Boccaccini, « Il training attoriale del parente. A proposito di Ar. *Thesm.* 624s. »,
  *Annali online di Lettere* (Università di Ferrara) 4 [année et pagination à vérifier ; p. 155 sqq. selon
  OpenAlex], 8 p. : partage des
  répliques des vv. 624-625 selon Wilson ; le Parent prend conscience de son rôle d'acteur. *Vers* : 624-625.
  *Accès* : `W/Boccaccini_2012_Thesm_624.pdf` ; DOI 10.15160/1826-803X/199. [lu]
- **Capra 2013** — A. Capra, « La bimba senza bambola e l'enigma bizantino dell'otre (Aristofane,
  *Tesmoforiazuse* 689 ss. e *Appendix Graeca* 7.57 Cougny) », p. 83-91 [publication à identifier]. *Vers* :
  689-759. [méta]
- **Palerm 2014** — V. R. Palerm, « El mito era un timo : Aristófanes, *Las Tesmoforiantes* 850 ss. »,
  p. 489-496 [publication à identifier]. *Vers* : 850-928. [méta]
- **Méndez Dosuna 2016a** — J. V. Méndez Dosuna, « Menelaus' Thriving Shrub of Lavender and his Double-Edged
  Sword : Aristophanes, *Thesmophoriazusae* 910 and *Lysistrata* 156 », *Philologus* 160 (2016), p. 163-171 :
  double sens du dernier mot du v. 910 (poils pubiens), après Hartwig 2008. *Vers* : 909-910. *Accès* :
  `AR/thesm 910.pdf` ; DOI 10.1515/phil-2016-0008. [lu]
- **Méndez Dosuna 2016b** — J. V. Méndez Dosuna, « El secreto de sus ojos : niñas y pupilas en Homero,
  *Ilíada* 8.168 y Aristófanes, *Tesmoforiantes* 406 », *Studia Philologica Valentina* 18, n.s. 15 (2016),
  p. 229-240 : κόρη au v. 406 joue sur « jeune fille » et « pupille, œil ». *Vers* : 406. *Accès* :
  `W/MendezDosuna_2016_SPhV18_Thesm406.pdf`. [lu, résumé]
- **Tammaro 2022** — V. Tammaro, « Un passo ancora problematico (Ar. *Thesm.* 910) », dans *Chorodidaskalia*
  [Festschrift, Göttingen, Vandenhoeck & Ruprecht, 2022], p. 367-372, DOI 10.13109/9783949189449.367.
  *Vers* : 910. [méta]
- **Stepantsov 2022** — S. A. Stepantsov, « Был ли меч ? К комментарию на "Фесмофории" Аристофана, ст. 134-140 »
  [Y avait-il une épée ?], *Studia Litterarum* 7.3 (2022), p. 66-83 : l'épée du v. 140 vient de la parodie des
  *Édoniens* d'Eschyle plutôt que d'un accessoire visible ; contre S. *Vers* : 134-140, 154-155. *Accès* :
  `W/Stepantsov_2022_StudLitt7_vv134-140.pdf`. [lu]
- **Nicolosi 2023** — A. Nicolosi, « Ar. *Thesm.* 517-530 e Archil. fr. 122 W.² : un esempio di memoria
  letteraria », *MH* 80 (2023), DOI 10.24894/2673-2963.00063 (libre : e-periodica, DOI 10.5169/seals-1042192).
  *Vers* : 517-530. [méta]
- **Stepantsov 2024** — S. A. Stepantsov, « Есть ли пословичное выражение в начале "Фесмофорий" Аристофана ? »
  [Y a-t-il une expression proverbiale au début des *Thesm.* ?], *Izvestija RAN. Serija literatury i jazyka*
  83.5 (2024), p. 96-102 : l'hirondelle du v. 1 n'est pas proverbiale (avec van Leeuwen). *Vers* : 1.
  *Accès* : `W/Stepantsov_2024_Izvestija83_proverbe_debut.pdf`. [lu, résumé]
- **Abramovich 2026** — M. A. Abramovich, « "Гекатина" или "шестидневная" луна в схолии к стиху 80… »
  [La lune « d'Hécate » ou « de six jours » dans la scholie au v. 80], *Indoevropejskoe jazykoznanie i
  klassičeskaja filologija* 30.1 (2026), p. 9-16 : dans sch. *Thesm.* 80a, préférer ἑκταία (Dindorf,
  Schneider) à ἑκαταία. *Vers* : 80 (scholie). *Accès* : `W/Abramovich_2026_IELCP30_schol_v80.pdf`. [lu, résumé]

### 1.4 Attribution des répliques ; le nom du parent d'Euripide (Mnésiloque ou Kèdestès)

**Les données** (détail et sources dans `recherche/ravennas_dossier.md` § 8.2 ; à établir sur l'image) :

- R n'a ni hypothesis ni liste des personnages (Zacher 1888, p. 531 ; Velsen 1883, p. 8 : « Deest index
  personarum in codd. »). Le copiste marque seulement le changement d'interlocuteur (paragraphos, dicolon) ;
  les sigles de noms ont été ajoutés par la main des scholies (S2), puis par la main qui a préparé
  l'impression de 1516 (Velsen 1871, p. 7-23 ; van Leeuwen 1904, p. 1-2 n.).
- Pour le parent, on lit tantôt κηδ(εστής), tantôt μνη(σίλοχος) : « Κηδ. R passim, Σ compluribus locis : Μνη. R
  compluribus locis, Σ passim » (Coulon 1928, app. au v. 1) ; « R et sch. saepe eum ita [scil. κηδεστήν]
  nominant, saepe autem Mnesilochum » (Wilson 2007, II, p. 71, app. au v. 1). Au f. 162v, S2 emploie μνησι- / μ·,
  et la ligne de tête des scholies donne les deux noms : « προλογίζει Μνησίλοχος κηδεστὴς Εὐριπίδου »
  (`ravennas/graphologie/folios/f162v.md`). Les scholies nomment Mnésiloque aux vv. 266, 603, 1065 ; d'autres
  disent ὁ κηδεστής ou ὁ γέρων (vv. 129, 469, 633, 756, 760, 1031, 1064, 1090, 1199 : relevé de Hiller 1874).
- Tradition biographique : la *Vie* d'Euripide (Euripide gendre de Mnésiloque, dont il épouse la fille
  Χοιρίλη/Χοιρίνη ; Mnésiloque collaborateur du poète d'après Téléclide : « Μνησίλοχός ἐστ' ἐκεῖνος ὃς φρύγει
  τι δρᾶμα καινὸν / Εὐριπίδῃ… », fr. 39 Kock [numéro K.-A. à vérifier ; 40 selon l'auteur]) et la Souda
  (ε 3695, d'après S.) ; la *Vie* donne aussi à Euripide un fils Mnésiloque, acteur. Textes vérifiés dans le
  corpus local (*Vita Euripidis*, First1KGreek ; Kock, *CAF* I, p. 217-218).

**Études**

- **Hiller 1874** — E. Hiller, « Über einige Personenbezeichnungen griechischer Dramen », *Hermes* 8 (1874),
  p. 442-456 (*Thesm.* : p. 449-453). Thèse fondatrice de la désignation « Kèdestès » : une partie des
  commentateurs anciens ignorait le nom de Mnésiloque (scholies citées ci-dessus) ; le public n'aurait pu
  reconnaître un particulier ni nommé ni caractérisé ; le Mnésiloque de Téléclide, collaborateur lettré
  d'Euripide, ne ressemble pas au rustre du prologue ; Aristophane aurait exploité les déboires conjugaux
  d'Euripide s'il avait mis en scène son beau-père. *Accès* : `W/hermes8/hermeswies08wies_djvu.txt` (OCR du
  volume, archive.org `hermeswies08wies`). [lu]
- **Velsen 1878, 1883** — premier éditeur à remplacer « Mnesilochus » par Κηδεστής, « à l'instigation de
  Hiller » (van Leeuwen 1904, p. 2 n., d'après `recherche/ravennas_dossier.md`). `ED/1883_Leipzig_Velsen`.
- **Kaibel 1887** — garde le nom par commodité : « Mnesilochum (licebit enim hoc nomine appellare eum qui
  apud Aristophanem nomen non habet) » (*Hermes* 22, p. 498). [lu]
- **Sommerstein 1994**, note « INLAW » (p. 157) : κηδεστής désigne tout parent par alliance ; le personnage
  est trop vieux pour être le gendre, trop peu respecté pour être le beau-père, sans doute un beau-frère ;
  l'identification antique avec Mnésiloque (*Vie* 5, Souda ε 3695 ; sigles sporadiques de R) n'a « ni autorité
  ni probabilité » ; le personnage ne représente peut-être personne de réel. [lu, extrait textuel]
- **Austin–Olson 2004**, *Dramatis personae* et note au v. 74 (p. 74, 76-77, d'après Kanavou 2010) : « Inlaw » ;
  κηδεστής terme générique ; importance des alliés par alliance. [à vérifier sur l'édition]
- **Kanavou 2010** — N. Kanavou, *Aristophanes' Comedy of Names. A Study of Speaking Names in Aristophanes*,
  Berlin-New York, 2010 (Sozomena 8), ch. 8 « *Thesmophoriazusae* », p. 146-158 : le nom de Mnésiloque, ajouté
  en marge par des commentateurs portés à nommer les anonymes, repose sur une identification spéculative ;
  l'anonymat est voulu et met en relief le lien d'alliance avec Euripide (vv. 74, 210, 584, 1165) ; recense
  aussi les noms des femmes (Mika, Critylla, etc.). *Accès* : `AR/[Nikoletta_Kanavou]_Aristophanes'_Comedy_of_Names*.pdf` ;
  DOI 10.1515/9783110247077.146. [lu]
- **Olson 1992** — S. D. Olson, « Names and Naming in Aristophanic Comedy », *CQ* n.s. 42 (1992), p. 304-319 :
  les noms des personnages (S. cite les p. 316-318 au v. 574, Clisthène). *Accès* : DOI
  10.1017/S0009838800015949. [méta] ; **Sommerstein 1980** — A. H. Sommerstein, « The Naming of Women in Greek
  and Roman Comedy », *QS* 11 (1980), p. 393-418 [tomaison : « II » dans l'extrait d'AO, « VI » chez P. ; à vérifier] (repris dans *Talking about Laughter*, Oxford, 2009, p. 43 sqq.)
  : noms des femmes de la pièce (Mika, Critylla, Philista…). [méta] [AO]
- **Zimmermann, *DNP* « Mnesilochos »** — B. Zimmermann, art. « Mnesilochos », *Der Neue Pauly* (trad. angl.
  *Brill's New Pauly*), DOI 10.1163/1574-9347_dnp_e807710. [méta]
- **L'auteur** — « Le dossier Mnésiloque », `latex/Aristophane-Thesmo Introduction.tex` : défend
  l'identification (personnage réel justement parce qu'il n'est pas nommé, comme le Paphlagonien des
  *Cavaliers* ; Téléclide ; usage onomastique attesté par Démosthène 43, 74, appliqué aux fils d'Euripide).
  À confronter aux arguments de Hiller 1874 et de Sommerstein 1994.

**Attribution des répliques (études de méthode et de lieux)**

- **Holzinger 1883** — K. Holzinger, *Über die Parepigraphae zu Aristophanes*, Vienne, 1883 : indications
  scéniques et noms marginaux des manuscrits. [P]
- **Lowe 1962, 1967** — J. C. B. Lowe, « The Manuscript Evidence for Changes of Speaker in Aristophanes »,
  *BICS* 9 (1962), p. 27-42, DOI 10.1111/j.2041-5370.1962.tb00694.x [méta] ; « Some Questions of Attribution in
  Aristophanes », *Hermes* 95 (1967), p. 53-71 (« XLV » chez P., sans doute pour XCV) [P] [tomaison à vérifier].
- **Austin 1971-1974** (rôle de la coryphée), **Notsu 1995** (vv. 295-382), **Melandri 2004** (vv. 276-279),
  **Boccaccini 2012** (vv. 624-625) : voir § 1.1 et 1.3.
- **Thiercy 1992** — P. Thiercy, « Problèmes de distribution et d'attribution des répliques chez Aristophane »,
  *Pallas* 38 (1992), p. 289-300 : méthode (paragraphoi, sigles, logique dramatique). *Accès* : `AR/Problèmes de distribution et d'attribution des répliques chez Aristophane.pdf`. [lu, d'après `recherche/drive_ressources.md`]
- **Wilson 2007** — l'apparat exclut volontairement les attributions des manuscrits : « Ratio et res ipsa » doivent
  décider (t. I, p. viii) ; Liberman 2008 juge l'application inégale.
- **Nombre d'acteurs** — J. A. Dane, « Aristophanic Parody : *Thesmophoriazusae* and the Three-Actor Rule »,
  *Theatre Journal* 36 (1984), p. 75-84 [pagination à vérifier ; DOI 10.2307/3207361] [méta] ; AO, p. lxviii-lxx :
  quatre acteurs (défendu par Olson 2006 contre Storey 2006).

### 1.5 Papyrus, scholies, tradition indirecte (renvois)

- Papyrus (PSI 1194, P.Oxy. 3839, 3840 + 4935 + 5132, P.Oxy. 1176) et études : `recherche/papyrus.md` ; notes
  ci-dessus : Goossens 1941, Koster 1955, Grassi 1956, Austin 1977, 1980, 1984, Medaglia 1982-1996, Marzullo
  1980-1982 et 1994 ; W. E. H. Cockle, « An Unpublished Papyrus of Aristophanes from Oxyrhynchus », dans
  E. M. Craik (éd.), *'Owls to Athens'. Essays on Classical Subjects Presented to Sir Kenneth Dover*, Oxford,
  1990, p. 51-60 (vv. 25 ?, 742-766, 941-956), DOI 10.1093/oso/9780198144786.003.0006 [méta] ; P. Mertens,
  « Les papyrus d'Aristophane. Actualisation des données bibliologiques et bibliographiques », dans M. S. Funghi
  (éd.), *Ὁδοὶ διζήσιος. Le vie della ricerca. Studi in onore di F. Adorno*, Florence, 1996, p. 335-343 [P].
- Scholies et leur histoire : `recherche/scholies.md`. Études récentes à ajouter : **Germain 2023** —
  C. Germain, *Scholies aux Thesmophories d'Aristophane*, Grenoble, UGA Éditions, 2023 (traduction annotée ;
  annexes sur les scholies citant les *Secondes Thesmophories* et sur l'eccyclème) ; libre : OpenEdition Books,
  books.openedition.org/ugaeditions/33098 (téléchargement automatique bloqué) [méta] ; **Gavazza 2022** —
  B. Gavazza, « Musica in scena ed erudizione musicale negli scolî al prologo delle *Tesmoforiazuse* di
  Aristofane », dans *Nuove volute di versi* [Festschrift, Göttingen, 2022], p. 37-48, DOI
  10.13109/9783949189326.37 [méta] ; **Abramovich 2026** (sch. 80a) : § 1.3.
- Tradition byzantine, excerpta, histoire du texte imprimé : Koster 1963, White 1906, Dovico 2016, Orsini 2011,
  Schreiber 1975 (« Unpublished Renaissance Emendations of Aristophanes », *TAPhA* 105, 1975, p. 313-332 [P]) :
  voir `recherche/drive_ressources.md` § 3.4 et `recherche/ravennas_dossier.md`.

## 2. Interprétation, mise en scène, contexte

### 2.1 Monographies, synthèses, recueils

- **Clements 2014** — A. Clements, *Aristophanes' Thesmophoriazusae. Philosophizing Theatre and the Politics
  of Perception in Late Fifth-Century Athens*, Cambridge, 2014 (Cambridge Classical Studies) : la pièce comme
  critique « parménidienne » de l'illusion tragique (réalité et apparence, Gorgias, Empédocle), lue comme
  avertissement politique dans les mois qui précèdent le coup d'État de 411 ; ch. 2 « Rereading the prologue »
  (p. 12-27) ; index des passages cités aux p. 221-223. *Vers* : surtout 1-294. *Accès* : `AR/Aristophanes Thesmophoriazusae  philosophizing theatre*.pdf` ; DOI 10.1017/CBO9781139629386. [lu, table des matières]
- **Zeitlin 1981** — F. I. Zeitlin, « Travesties of Gender and Genre in Aristophanes' *Thesmophoriazousae* »,
  *Critical Inquiry* 8 (1981), p. 301-327, DOI 10.1086/448156 ; aussi dans H. P. Foley (éd.), *Reflections of
  Women in Antiquity*, New York-Londres, 1981, p. 169-217 ; version revue dans *Playing the Other. Gender and
  Society in Classical Greek Literature*, Chicago, 1996, p. 375-416. Étude fondatrice : travestissement,
  mimèsis et genres (comédie / tragédie, féminin / masculin), la pièce comme réflexion sur le théâtre. [méta] [AO]
- **Bobrick 1997** — E. Bobrick, « The Tyranny of Roles : Playacting and Privilege in Aristophanes'
  *Thesmophoriazusae* », dans G. W. Dobrov (éd.), *The City as Comedy. Society and Representation in
  Athenian Drama*, Chapel Hill-Londres, 1997, p. 177-197. [AO] *Accès* : — (non récupéré du Drive :
  `recherche/drive_ressources.md` § 9.2).
- **Hansen 1976** — H. Hansen, « Aristophanes' *Thesmophoriazusae* : Theme, Structure, and Production »,
  *Philologus* 120 (1976), p. 165-185 : unité thématique, découpage, réalisation scénique (Écho jouée par
  l'acteur d'Euripide, etc.). DOI 10.1524/phil.1976.120.1.165. [méta] [S]
- **Taaffe 1993** — L. K. Taaffe, *Aristophanes and Women*, Londres-New York, 1993 (réimpr. 2018), ch.
  « Men as Women : *Thesmophoriazusae* », p. 74-102 (S. ; p. 88-116 dans la réimpression). [méta] [S]
- **Bowie 1993** — A. M. Bowie, *Aristophanes. Myth, Ritual and Comedy*, Cambridge, 1993, ch.
  « *Thesmophoriazusae* », p. 205-227 : lecture rituelle (Thesmophories, mythe de Déméter). DOI
  10.1017/CBO9780511518362.010. [méta] *Accès* : — (non récupéré du Drive).
- **MacDowell 1995** — D. M. MacDowell, *Aristophanes and Athens. An Introduction to the Plays*, Oxford,
  1995, ch. « Women at the Thesmophoria », p. 251-273. [méta]
- **Russo 1962/1994** — C. F. Russo, *Aristofane autore di teatro*, Florence, 1962 (2e éd. 1984) ; trad. angl.
  *Aristophanes. An Author for the Stage*, Londres, 1994, ch. « *Thesmophoriazusae* » (éd. 2002, p. 200-211).
  [méta] [AO]
- **Paduano 1982** — G. Paduano, « Le *Tesmoforiazuse* : ambiguità del fare teatro », *QUCC* n.s. 11 (1982),
  p. 103-127, DOI 10.2307/20538730. [méta] [P]
- **Bonanno 1990** — M. G. Bonanno, *L'allusione necessaria. Ricerche intertestuali sulla poesia greca e
  latina*, Rome, 1990, p. 241-276 (sur les *Thesm.*, d'après S.). [S] [P]
- **Bierl 2001** — A. Bierl, *Der Chor in der Alten Komödie. Ritual und Performativität* (Beiträge zur
  Altertumskunde 126), Munich-Leipzig, 2001, ch. I « Der komische Chor in den *Thesmophoriazusen* »,
  p. 105-299 : le chœur des Thesmophoriazuses entre rite et performance. DOI 10.1515/9783110956719.105.
  [méta] [AO] [traduction anglaise à vérifier]
- **AJPh 123.3 (2002)**, numéro consacré aux *Thesmophoriazousai* (éd. B. K. Gold) : Tzanetou, Stehle (§ 2.3,
  2.5), G. Van Steen (réception grecque moderne), E. W. Scharffenberger (traduction d'Arrowsmith), M.-K. Gamel
  (mise en scène). [méta]
- **Kanellakis 2020** — D. Kanellakis, *Aristophanes and the Poetics of Surprise*, Berlin-Boston, 2020
  (Trends in Classics, Suppl. 96) : « *Thesmophoriazusae* » p. 114-117 (mythes détournés), et passim (*para
  prosdokian*, surprises théâtrales). *Accès* : `AR/Aristophanes and the Poetics of Surprise*.pdf`. [lu, table]
- **Platter 2007** — Ch. Platter, *Aristophanes and the Carnival of Genres*, Baltimore, 2007, ch. 5 « The
  Return of Telephus : *Acharnians*, *Thesmophoriazusae*, and the Dialogic Background », p. 143-175 (lecture
  bakhtinienne). *Accès* : `AR/*Platter*Carnival*.pdf`. [lu, table]
- **Saetta Cottone 2005** — R. Saetta Cottone, « Euripide, il nemico delle donne. Studio sul tema comico delle
  *Tesmoforiazuse* di Aristofane », *Lexis* 23 (2005), p. 131-156. [méta] ; **Saetta Cottone 2015** — « Le monde
  à l'envers. Renversement paratragique et mimèsis dans les *Thesmophories* d'Aristophane », dans M. Bastin-Hammou
  *et al.* (dir.), Besançon, ISTA, 2015, p. 101-114 [volume à préciser] [méta] ; traduction commentée :
  *Aristophane, Les Thesmophories ou La Fête des femmes*, Paris, De Boccard, 2016 (c. r. S. Pagni, *Lexis* 35,
  2017, p. 458-465 : `TH/Recensione_a_Aristophane_Les_Thesmophori.pdf`).
- **Fabrini 2018** — Ch. Fabrini, *La paratragedia in Aristofane : ricerche sulla ricezione del tragico nel V
  sec. a.C.*, thèse (dir. A. M. Belardinelli), a.a. 2017-2018 : répertoire des citations et parodies
  tragiques, dont *Thesm.* 21 (Soph. *Ajax locrien* fr. 14), 134-137 (Esch. *Édoniens* fr. 61), 869-870 (Soph.
  *Pélée* fr. 493). *Accès* : `AR/Tesi_dottorato_Fabrini.pdf`. [lu, index]
- **Yoon 2019** — F. Yoon, « The Mirrored Structure of *Thesmophoriazusae* : Hero, Plot, and Themes »,
  *Phoenix* 73 (2019), p. 262-278 : la pièce bascule à mi-parcours, Euripide et son kèdestès échangeant les
  rôles de héros et de victime ; composition en anneau (genre par le « genre », puis l'inverse). DOI
  10.1353/phx.2019.0025. [méta, résumé]
- **Lourenço [1995 ?]** — F. Lourenço, « Tema(s) e desenvolvimento temático nas *Tesmoforiantes* de
  Aristófanes », *Humanitas* (Coimbra) 47 (t. 1) [année à vérifier : 1995 pour ce tome ; 2014 selon OpenAlex,
  date de mise en ligne]. Libre : digitalis-dsp.uc.pt (certificat du serveur invalide, téléchargement impossible).
  [méta]
- **Zumbrunnen 2012** — J. Zumbrunnen, *Aristophanic Comedy and the Challenge of Democratic Citizenship*,
  Boydell & Brewer, 2012, ch. 2 « Ordinary Citizens, High Culture, and the Salvation of the City : *Clouds*, *Women at the
  Thesmophoria*, and *Frogs* », p. 41-59. DOI 10.1515/9781580467711-004. [méta]
- **Drumond 2020** — G. F. Drumond, « A queda do herói cômico : o papel do protagonista em *Nuvens*, *Vespas* e
  *Tesmoforiantes* », *Dramaturgias* 13 (2020), p. 59-86 : la défaite du protagoniste comique (le Parent) dans
  trois pièces. DOI 10.26512/dramaturgias.vi13.31057. *Accès* : `W/Drumond_2020_Dramaturgias13_heroi.pdf`. [lu,
  titre et résumé]
- **Ouvrages généraux** souvent utiles : K. J. Dover, *Aristophanic Comedy*, Londres, 1972 ; M. S. Silk,
  *Aristophanes and the Definition of Comedy*, Oxford, 2000 ; T. K. Hubbard, *The Mask of Comedy*, Ithaca, 1991
  (parabase ; appendice 4 sur la chronologie de *Lys.* et *Thesm.*, p. 243-245, DOI 10.7591/9780801466915-015) ;
  D. Harvey, J. Wilkins (éd.), *The Rivals of Aristophanes*, Londres, 2000. [AO] [méta]

### 2.2 Date (411), contexte politique ; les *Secondes Thesmophories*

- **Débat sur la fête** : Dionysies de 411 (AO, p. xxxiii-xlv ; S., *Introductory Note* ; la majorité) ou
  Lénéennes (Prato 2001, p. XI-XVII, à partir des vv. 356-367 et 840 ; critiqué par Olson 2002 et Macía Aparicio
  2002, § 1.1). Points d'appui : la mort de Lamachos et de Hyperbolos (v. 840-841), les probouloi et le conseil
  « de l'an dernier » (vv. 808-809), la représentation d'*Hélène* et d'*Andromède* « l'an dernier » (vv. 850,
  1060-1061), le serment contre ceux qui appellent les Mèdes et convoitent la tyrannie (vv. 356-367).
- **Wilamowitz 1893** — U. von Wilamowitz-Moellendorff, « Die Zeit der *Thesmophoriazusen* », *Aristoteles und
  Athen*, t. II, Berlin, 1893, p. 343-355. *Accès* : `ME/wilamowitz1893_AuA2`. [méta]
- **Sommerstein 1977** — A. H. Sommerstein, « Aristophanes and the Events of 411 », *JHS* 97 (1977),
  p. 112-126 : chronologie de *Lys.* et *Thesm.* par rapport aux étapes du coup d'État ; vv. 808-809 (S. y
  renvoie, p. 116-117). DOI 10.2307/631026. [méta] [S]
- **Wysocki 1988** — L. Wysocki, « Aristophanes, Thucydides, B. VIII and the Political Events of 413-411 B.C. »,
  *Eos* 76 (1988), p. 237-248. [P]
- **Blanc–Taillardat 1986** (v. 366 : « l'ambition des oligarques dans l'hiver 412-411 ») : § 1.3.
- **Vickers 1989, 2015** — M. Vickers, « Alcibiades on Stage : *Thesmophoriazusae* and *Helena* », *Historia* 38
  (1989), p. 41-65 [P] ; repris et développé dans *Aristophanes and Alcibiades. Echoes of Contemporary History in
  Athenian Comedy*, Berlin-Boston, 2015, ch. 9 « Alcibiades in Gaol : *Thesmophoriazusae* », p. 129-148, DOI
  10.1515/9783110427912-011 [méta] : lecture allégorique très contestée (le Parent = Alcibiade).
- **Munn 2000** — M. Munn, *The School of History. Athens in the Age of Socrates*, Berkeley, 2000, appendice B
  « Euripides' *Helen* and Aristophanes' *Thesmophoriazusae* », p. 333-334. [méta]
- **Tsakmakis 2011** — A. Tsakmakis, « Persians, Oligarchs, and Festivals : The Date of *Lysistrata* and
  *Thesmophoriazusae* », dans *Crisis on Stage. Tragedy and Comedy in Late Fifth-Century Athens*, Berlin-Boston,
  2011, p. 291-302, DOI 10.1515/9783110271560.291 [méta ; éditeurs scientifiques à vérifier].
- **Faria 2010** — M. de Oliveira Faria, *Quando as mulheres estão no poder : ambiguidades, obscuridades e
  referências políticas em As Tesmoforiantes de Aristófanes*, mémoire, Université de São Paulo, 2010 ; article
  tiré : « As Tesmoforiantes : peça com menos referência política de Aristófanes ? », *Codex* 2.1 (2010), p. 59 sqq.
  (libre : teses.usp.br ; revistas.ufrj.br). [méta]
- **Thesm. II (la seconde pièce, perdue)** :
  - **Butrica 2001** — J. L. Butrica, « The Lost *Thesmophoriazusae* of Aristophanes », *Phoenix* 55 (2001),
    p. 44-76, DOI 10.2307/1089023 [méta] ; débat avec **Olson–Austin 2003-2004** — S. D. Olson, C. Austin, « On the
    Date and Plot of Aristophanes' Lost *Thesmophoriazusae II* », *Leeds International Classical Studies* 3.5
    (2003-2004), 11 p. [A] (réplique de Butrica dans la même revue, citée par Storey 2006 [à localiser]) ;
  - AO, introduction, § VI « *Thesmophoriazusae II* », p. lxxvii-lxxxviii (traduction de l'extrait arabe de
    Galien sur la parabase, fr. 346) ; **Deichgräber 1956** — K. Deichgräber, *Parabasenverse aus Thesmophoriazusen
    II des Aristophanes bei Galen* (SB Berlin), Berlin, 1956, DOI 10.1515/9783112725917 [méta] ;
  - **Torchio 1999-2000** — M. C. Torchio, études philologiques sur les fragments, *Quaderni del Dipartimento di
    Filologia, Linguistica e Tradizione classica* (Turin) 13 (1999), p. 99-114, et 14 (2000), p. 33-66 [AO ;
    titres à vérifier] ; **fr. 333** : « Aristofane, *Tesmoforiazuse seconde*, fr. 333 », dans *Utopie e immagini
    gastronomiche nei frammenti dell'Archaia*, Bologne, Pàtron, 2000, p. 157-172, DOI 10.2307/jj.29844527.12
    [méta ; auteur (M. Pellegrino ?) à vérifier] ;
  - **Imperio 2023** — O. Imperio, *Aristophanes. Eirene II – Lemniai (fr. 305-391)* (Fragmenta Comica 10.6),
    Göttingen, 2023, « Θεσμοφοριάζουσαι β' », p. 92-226 : commentaire de référence des fragments. DOI
    10.13109/9783949189807.92. [méta]
  - Scholies citant les *Secondes Thesmophories* : Germain 2023, annexe II (§ 1.5).

### 2.3 La fête des Thesmophories ; femmes, religion, rite

*Dans la pièce*

- **Habash 1997** — M. Habash, « The Odd Thesmophoria of Aristophanes' *Thesmophoriazusae* », *GRBS* 38 (1997),
  p. 19-40 : Aristophane garde assez d'éléments réels de la fête (à partir du v. 277) pour la rendre
  reconnaissable, mais la remodèle (assemblée, procès, châtiment) au service de l'intrigue. *Accès* :
  `W/Habash_1997_GRBS38_Odd_Thesmophoria.pdf`. [lu, début]
- **Tzanetou 2002** — A. Tzanetou, « Something to Do with Demeter : Ritual and Performance in Aristophanes'
  *Women at the Thesmophoria* », *AJPh* 123 (2002), p. 329-367 : correspondances entre l'intrigue et le
  calendrier rituel (Nesteia, rapt de Corè, retour). DOI 10.1353/ajp.2002.0045. [méta] [AO]
- **Haldane 1965** — J. A. Haldane, « A Scene in the *Thesmophoriazusae* (295-371) », *Philologus* 109 (1965),
  p. 39-46 : prière et malédiction de l'assemblée des femmes. DOI 10.1524/phil.1965.109.14.39. [méta] [AO]
- **Prato 2000** — C. Prato, « La parodia di preghiere, culti e riti nelle *Tesmoforiazuse* di Aristofane », dans
  *Poesia e religione in Grecia. Studi in onore di G. Aurelio Privitera*, Naples, 2000, p. 565-570. [P]
- **Giacomoni 1999** — A. Giacomoni, « Rito e trasgressione erotica : Aristoph. *Thesm.* 466 ss. », *QUCC* n.s.
  63 (1999), p. 91-95 (titre de P. : « … nella ῥῆσις di Mnesiloco ») : le discours du Parent et la licence
  verbale rituelle. *Vers* : 466-519. *Accès* : `TH/thesm 466 sq giacomoni1999.pdf` ; DOI 10.2307/20546611.
  [lu, d'après `recherche/drive_ressources.md`]
- **Germain 2021** — C. Germain, « Espace sacré, espace scénique et espace comique dans les *Thesmophories*
  d'Aristophane », *REA* 123 (2021), p. 201-219 : le Thesmophorion comme lieu scénique (déplacement au v. 277,
  usage de la skènè). DOI 10.3406/rea.2021.6984 ; libre : HAL hal-03355961. [méta]
- **Valdés Guía 2017** — M. Valdés Guía, « Fêtes de citoyennes, délibération et justice féminine sur l'Aréopage
  (Athènes, Ve siècle av. J.-C.) », *Clio. Femmes, genre, histoire* 45 (2017), p. 279-307 : l'assemblée des
  femmes de la pièce et ses fondements institutionnels. *Accès* : `TH/areopage *.pdf`. [lu, d'après
  `recherche/drive_ressources.md`]
- **Rolley 1966** — Cl. Rolley, communication résumée dans les « Actes de l'Association », *REG* 79 (1966),
  p. IX-XXVI : l'outre « sacrifiée » (vv. 740 sqq.) et le sacrifice du porcelet. *Accès* : `TH/thesmophories 740 sacrifice*.pdf`. [lu, d'après `recherche/drive_ressources.md`]
- **Foley 2024** — H. P. Foley, « Women at the Thesmophoria », dans *A Companion to Aristophanes*, Hoboken,
  Wiley-Blackwell, 2024, p. 212-227, DOI 10.1002/9781119622963.ch14 [méta ; éditeurs à vérifier] (accès libre
  annoncé chez l'éditeur, téléchargement automatique refusé).

*La fête (sources et synthèses)*

- L. Deubner, *Attische Feste*, Berlin, 1932, p. 50-60 ; M. P. Nilsson, *Griechische Feste von religiöser
  Bedeutung*, Leipzig, 1906, p. 313 sqq. ; H. W. Parke, *Festivals of the Athenians*, Londres, 1977 ;
  A. C. Brumfield, *The Attic Festivals of Demeter and their Relation to the Agricultural Year*, New York, 1981 ;
  E. Simon, *Festivals of Attica*, Madison, 1983 ; W. Burkert, *Greek Religion*, Cambridge (Mass.), 1985 ;
  M. Dillon, *Girls and Women in Classical Greek Religion*, Londres, 2002. [AO] [P]
- S. Eitrem, « Les Thesmophoria, les Skirophoria et les Arrhetophoria », *SO* 23 (1944), p. 32-45, DOI
  10.1080/00397674408590377 [méta] ; J. Prytz Johansen, « The Thesmophoria as a Women's Festival », *Temenos*
  11 (1975) (libre : journal.fi) [méta].
- M. Detienne, « Violentes "eugénies". En pleines Thesmophories : des femmes couvertes de sang », dans
  M. Detienne, J.-P. Vernant (dir.), *La Cuisine du sacrifice en pays grec*, Paris, 1979 (trad. angl. 1989,
  p. 129-147 selon AO) [AO ; titre à vérifier] ; H. S. Versnel, « The Festival for Bona Dea and the
  Thesmophoria », *G&R* 39 (1992), p. 31-55, DOI 10.1017/S0017383500023974, développé dans *Inconsistencies in
  Greek and Roman Religion* II, Leyde, 1993, p. 228-288 [méta] ; N. D. Robertson, « The Sequence of Days at the
  Thesmophoria and at the Eleusinian Mysteries », *Échos du monde classique / Classical Views* 43, n.s. 18
  (1999), p. 1-33 [méta] ; N. J. Lowe, « Thesmophoria and Haloa : Myth, Physics and Mysteries », dans S. Blundell,
  M. Williamson (éd.), *The Sacred and the Feminine in Ancient Greece*, Londres, 1998, p. 149-173 [A] [méta].
- R. Parker, *Polytheism and Society at Athens*, Oxford, 2005, ch. 13 « Women's Festivals : *Thesmophoria* and
  *Adonia* », p. 270-289 [méta] ; C. Trümpy, « Die Thesmophoria, Brimo, Deo und das Anaktoron », *Kernos* 17
  (2004) (libre : OpenEdition) [méta] ; H. Pierre, « Réflexions autour de la Nesteia des Thesmophories
  athéniennes », *Pallas* 76 (2008), p. 85-94 [méta] ; A. B. Stallsmith, « Interpreting the Athenian
  Thesmophoria », *Classical Bulletin* 84 (2009), p. 28-47 [méta] ; K. R. L. McLardy, « Local Variation in the
  Thesmophoria Festival », dans *The Local Horizon of Ancient Greek Religion*, Cambridge, 2023, p. 205-231 [méta].
- Topographie : O. Broneer, « The Thesmophorion in Athens », *Hesperia* 11 (1942), p. 250-274, DOI 10.2307/146735 ;
  H. A. Thompson, « Pnyx and Thesmophorion », *Hesperia* 5 (1936), p. 151-200, DOI 10.2307/146542 (le Thesmophorion
  était-il sur la Pnyx ? question posée à partir des vv. 656-658 ; S. au v. 656) [méta] [S].
- Épigraphie : décret du dème de Cholargos sur les Thesmophories (*CGRN* 79, libre : DOI 10.54510/cgrn79 ;
  É. Michon, *CRAI* 1913, p. 30-31, et *Mémoires… AIBL* 13, 1923, p. 1-24) [méta].


### 2.4 Les parodies d'Euripide (*Télèphe*, *Palamède*, *Hélène*, *Andromède*) ; paratragédie

*Identification des parodies, études d'ensemble*

- **Schlesinger 1937** — A. C. Schlesinger, « Identification of Parodies in Aristophanes », *AJPh* 58 (1937),
  p. 294-305 : critères de reconnaissance des parodies tragiques. [P]
- **Miller 1946** — H. W. Miller, « Some Tragic Influences in the *Thesmophoriazusae* of Aristophanes », *TAPhA*
  77 (1946), p. 171-182 : relevé des échos tragiques hors des grandes scènes de parodie. DOI 10.2307/283454.
  [méta] [AO]
- **Prato 1955** — C. Prato, *Euripide nella critica di Aristofane*, Galatina, 1955. [P]
- **Pucci 1961** — P. Pucci, « Aristofane ed Euripide : ricerche metriche e stilistiche », *Memorie
  dell'Accademia dei Lincei* s. VIII, 10 (1961), p. 277-423 : la langue et la métrique euripidiennes dans les
  parodies. [P]
- **Harriott 1962** — R. Harriott, « Aristophanes' Audience and the Plays of Euripides », *BICS* 9 (1962), p. 1-8 :
  ce que le public pouvait reconnaître des pièces parodiées. [P]
- **Rau 1967, 1975** — P. Rau, *Paratragodia. Untersuchung einer komischen Form des Aristophanes*, Munich, 1967
  (Zetemata 45), ouvrage de référence pour l'analyse des parodies (*Télèphe*, *Palamède*, *Hélène*, *Andromède*)
  [AO] [P] [pages des *Thesm.* à relever] ; « Das Tragödienspiel in den *Thesmophoriazusen* », dans
  H.-J. Newiger (éd.), *Aristophanes und die alte Komödie* (Wege der Forschung 265), Darmstadt, 1975, p. 339-356.
  [P]
- **Moulton 1981** — C. Moulton, *Aristophanic Poetry*, Göttingen, 1981 (Hypomnemata), ch. 4 « Poetry and
  Imitation in the *Thesmophoriazusae* », p. 108-143. DOI 10.13109/9783666251641.108. [méta]
- **Bonanno 1987, 1990** — M. G. Bonanno, « ΠΑΡΑΤΡΑΓΩΙΔΙΑ in Aristofane », *Dioniso* 57 (1987), p. 135-167 [P] ;
  *L'allusione necessaria*, Rome, 1990, p. 241-276 (§ 2.1). [S] [P]
- **Hunzinger 2000** — Chr. Hunzinger, « Aristophane, lecteur d'Euripide », dans *Le théâtre grec antique : la
  comédie* (Cahiers de la Villa Kérylos 10), Paris, 2000, p. 99-110. *Accès* : `AR/Aristophane lecteur d'Euripide7.pdf`. [lu, d'après `recherche/drive_ressources.md` § 7.3]
- **Voelke 2004** — P. Voelke, « Euripide, héros et poète comique : à propos des *Acharniens* et des
  *Thesmophories* d'Aristophane », *Études de Lettres* 2004 (numéro « Poétique d'Aristophane et langue d'Euripide en
  dialogue »), p. 117-138 : Euripide personnage, metteur en scène de ses propres pièces, devient un poète
  « comique ». *Accès* : `TH/EuripideAristophane.pdf`. [lu, début]
- **Saetta Cottone 2003, 2005, 2015** : § 2.1 et 2.5 ; **Saetta Cottone 2007/2010** — R. Saetta Cottone, « Penteo
  spettatore di tragedia : le *Baccanti* e la risposta alle *Tesmoforiazuse* », *Argos* 31 (2007), p. 43-65 ;
  version française : « Penthée spectateur de tragédie. Les *Bacchantes* et la réponse aux *Thesmophories* », dans
  *La philologie au présent. Pour Jean Bollack*, Villeneuve-d'Ascq, Presses universitaires du Septentrion, 2010,
  p. 201-221, DOI 10.4000/books.septentrion.9353 : les analogies de structure et de thèmes entre les
  *Bacchantes* (Penthée travesti) et les *Thesm.* font de la tragédie une réponse d'Euripide à la comédie.
  *Accès* : `W/SaettaCottone_2007_Argos31_Penteo.pdf` ; libre (OpenEdition Books) pour la version française. [lu]
- **Fletcher 2012** — J. Fletcher, *Performing Oaths in Classical Greek Drama*, Cambridge, 2012 (en ligne 2011),
  ch. « How to Do Things with Euripides : Aristophanes' *Thesmophoriazusae* », p. 203-219 : le serment d'Euripide
  (vv. 269-276) et l'écho du vers d'*Hippolyte* 612 sur la langue et l'esprit. DOI
  10.1017/CBO9781139005272.009. [méta ; vers d'après le titre et le sujet, à vérifier]
- **Quijada Sagredo 2012** — M. Quijada Sagredo, « Intriga cómica versus intriga trágica en *Tesmoforiantes* de
  Aristófanes », *Emerita* 80 (2012), p. 257-274 : comment l'intrigue comique enchâsse et retourne les intrigues
  tragiques de délivrance. DOI 10.3989/emerita.2012.13.1120 ; libre : emerita.revistas.csic.es. [méta]
- **Nelson 2016** — S. Nelson, *Aristophanes and His Tragic Muse*, Leyde-Boston, 2016, ch. « *Women at the Thesmophoria* and *Frogs* : Aristophanes on Tragedy and
  Comedy », p. 241-284. DOI 10.1163/9789004310919_009. [méta]
- **Farmer 2017** — M. C. Farmer, *Tragedy on the Comic Stage*, Oxford-New York, 2017, ch. 4 « Euripides in the
  Echo Chamber », p. 155-194 : les parodies jouées par Euripide lues à partir de sa conversation avec Agathon dans
  le prologue ; Aristophane fait ressortir les éléments comiques de la tragédie euripidienne, et les deux poètes,
  « tardifs », fondent comédie et tragédie. DOI 10.1093/acprof:oso/9780190492076.003.0005. [méta, résumé de
  l'éditeur]
- **Jendza 2020** — C. Jendza, *Paracomedy. Appropriations of Comedy in Greek Tragedy*, New York, 2020, ch. 3
  « From Rags to Drag », p. 82-118 (dialogue entre Aristophane et Euripide sur le costume : héros en haillons,
  travestissement ; *Hélène* répond aux *Acharniens*, les *Thesm.* à *Hélène*, les *Bacchantes* aux *Thesm.*), et
  ch. 4 sur la structure d'*Hélène*, p. 119-166. DOI 10.1093/oso/9780190090937.003.0004. [méta, résumé de
  l'éditeur]
- **Bierl 2020** — A. Bierl, « Paratragic Fragmentation and Patchwork-Citation as Comic Aesthetics : The Potpourri
  Use of Euripides' *Helen* and *Andromeda* in Aristophanes' *Thesmophoriazusae* and Their Symbolic Meaning », dans
  A. A. Lamari, F. Montanari, A. Novokhatko (éd.), *Fragmentation in Ancient Greek Drama* (Trends in Classics,
  Suppl. 84), Berlin-Boston, 2020, p. 453-480. DOI 10.1515/9783110621693-025. *Vers* : 846-928, 1009-1135.
  [méta]
- Voir aussi Mureddu 1982-1983 (§ 2.5), Fabrini 2018 et Platter 2007 (§ 2.1), Mastromarco 2016 (§ 2.7).

*Télèphe (vv. 689-764 : l'enfant pris en otage, l'outre)*

- **Brizi 1928** — G. Brizi, « Il mito di Telefo nei tragici greci », « *AR* » 7 (1928), p. 95-145 (abréviation de
  P., revue à identifier). [P]
- **Miller 1948** — H. W. Miller, « Euripides' *Telephus* and the *Thesmophoriazusae* of Aristophanes », *CPh* 43
  (1948), p. 174-183 : l'influence du *Télèphe* dépasse la scène de l'otage. DOI 10.1086/363107. [méta]
- **Handley–Rea 1957** — E. W. Handley, J. Rea, *The Telephus of Euripides* (BICS Suppl. 5), Londres, 1957. [AO] [P]
- **Heath 1987a** — M. Heath, « Euripides' *Telephus* », *CQ* 37 (1987), p. 272-280 : reconstruction de la pièce ;
  S. y renvoie pour les échos du *Télèphe* dans le discours du Parent (vv. 466-519) et pour la scène de l'otage
  (vv. 689-758). DOI 10.1017/S0009838800030494. *Vers* : 466-519, 689-758. [méta] [S]
- **Collard–Cropp–Lee 1995** — C. Collard, M. J. Cropp, K. H. Lee (éd.), *Euripides. Selected Fragmentary Plays*,
  t. I, Warminster, 1995 (*Télèphe*). [AO]
- Capra 2013 (l'outre, vv. 689 sqq.) : § 1.3.
- **Romani 2006** — S. Romani, « Il corpo inventato : i bambini rapiti di *Acarnesi* e *Tesmoforiazuse* », t. 67,
  p. 107-124 [revue à identifier]. *Vers* : 689-764. [méta]
- Iconographie de la scène (cratère de Würzburg) : § 3.

*Palamède (vv. 765-784 : les messages sur les rames)*

- **Scodel 1980** — R. Scodel, *The Trojan Trilogy of Euripides* (Hypomnemata 60), Göttingen, 1980 : reconstruction
  du *Palamède* (415), dont la scène des rames s'inspire. [AO]
- Pas d'étude propre à la scène repérée ; voir Rau 1967 et les commentaires (AO, S., P.).

*Mélanippe, Phèdre, Sthénébée : le procès d'Euripide (vv. 383-432, 466-519, 545-548) et la parabase*

- **Miller 1947** — H. W. Miller, « On the Parabasis of the *Thesmophoriazusae* of Aristophanes », *CPh* 42 (1947),
  p. 180-181 : vv. 531-532 parodient un vers de la *Mélanippe captive* (« rien de pire qu'une mauvaise femme… »),
  et la défense des femmes de la parabase (vv. 785-845) s'inspire du plaidoyer de Mélanippe. *Accès* :
  `AR/parabase des thesmophories.pdf`. [lu]
- **Assaël 1985** — J. Assaël, « Misogynie et féminisme chez Aristophane et chez Euripide », *Pallas* 32 (1985)
  (p. 94-95 citées par Blanchard 2001) : la « mauvaise foi » d'Aristophane envers Euripide. [cité par
  Blanchard 2001 ; pagination complète à vérifier]
- **Blanchard 2001** — A. Blanchard, « L'art de la mauvaise foi dans les *Thesmophories* d'Aristophane », dans
  *Dieux, héros et médecins grecs. Hommage à Fernand Robert* (ISTA 790), Besançon, 2001, p. 97-106 : déformation
  des héroïnes euripidiennes (vv. 547-548 : Mélanippe et Phèdre, jamais Pénélope) et perfidie de la parabase où les
  femmes se défendent elles-mêmes. *Accès* : `AR/Lart de la mauvaise foi dans les Thesmophories.pdf` ; libre
  (Persée). [lu, début]
- **Cowan 2008** (vv. 497-501, *Hippolyte voilé*) et **Giacomoni 1999** (vv. 466-519) : § 1.3 et 2.3.
- **Lefkowitz 1989** — M. R. Lefkowitz, « "Impiety" and "Atheism" in Euripides' Dramas », *CQ* 39 (1989),
  p. 70-82 : la réputation d'impiété d'Euripide (v. 450 : il a persuadé les hommes que les dieux n'existent pas)
  vient de la comédie et des biographes. DOI 10.1017/S0009838800040489. *Vers* : 450-451. [méta] [S]
- **Ruck 1975** — C. Ruck, « Euripides' Mother : Vegetables and the Phallos in Aristophanes », *Arion* n.s. 2
  (1975), p. 13-58 : la mère « marchande de légumes » (vv. 387, 456, 910). [P]
- Tradition biographique (mère d'Euripide, Mnésiloque) : Delcourt 1933, Saïd 2001, Villacèque 2014, Campos Daroca
  *et al.* 2007, voir `recherche/drive_ressources.md` § 4.3 et 7.3 ; Cl. Nancy, *Euripide et le parti des
  femmes*, Paris, 2016 (c. r. R. Saetta Cottone, *Aretè* 2, 2017 : `AR/CLAIRE_NANCY_Euripide_et_le_parti_des_fe.pdf`).

*Hélène (vv. 846-928)*

- **Campbell 1949** (vv. 855-857) : § 1.3.
- **Vickers 1989, 2015** — M. Vickers, « Alcibiades on Stage : *Thesmophoriazusae* and *Helena* », *Historia* 38
  (1989), p. 41-65 [P] ; *Aristophanes and Alcibiades*, Berlin-Boston, 2015, ch. 7 « "The Woman of Old" :
  Euripides' *Helen* and *Andromeda* », p. 89-108, DOI 10.1515/9783110427912-009 [méta]. Lecture allégorique
  contestée (§ 2.2).
- **Munn 2000** — appendice B « Euripides' *Helen* and Aristophanes' *Thesmophoriazusae* » : § 2.2.
- **Nieddu 2004** — G. F. Nieddu, « A Poet at Work : The Parody of *Helen* in the *Thesmophoriazusae* », *GRBS*
  44 (2004), p. 331-360 : la scène comme document sur le « poète au travail » (comparé à Agathon, vv. 101-129) ;
  procédés de sélection, de montage et de déformation du texte d'*Hélène* ; détail des vv. 855-916. *Vers* :
  846-928 (notamment 859-878, 902-922). *Accès* : `W/Nieddu_2004_GRBS44_Parody_of_Helen.pdf` ; libre (GRBS). [lu]
- **Wright 2005** — M. Wright, *Euripides' Escape-Tragedies. A Study of Helen, Andromeda and Iphigenia among the
  Taurians*, Oxford, 2005 ; c. r. A. Blanchard, *REG* 119 (2006), p. 798-800 (`TH/Blanchard Euripides' Escape-Tragedies*.pdf`). [lu pour le c. r.]
- Palerm 2014 (vv. 850 sqq.) : § 1.3.
- **Esteban Santos 2016** — A. Esteban Santos, « Helena o la parodia de una parodia : Homero en Eurípides y en
  *Tesmoforiantes* de Aristófanes », p. 201-210 [publication à identifier]. *Vers* : 846-928. [méta]
- **Jendza 2020**, **Bierl 2020** : ci-dessus.

*Andromède (vv. 1009-1135) et Écho*

- **Mitsdörffer 1954** — W. Mitsdörffer, « Das Mnesilochoslied in Aristophanes' *Thesmophoriazusen* »,
  *Philologus* 98 (1954), p. 59-93 : reconstruction de la monodie d'« Andromède » chantée par le Parent ; discutée
  par Coulon 1957. DOI 10.1524/phil.1954.98.12.59. *Vers* : 1015-1055. [méta] [P]
- **Webster 1965** — T. B. L. Webster, « The *Andromeda* of Euripides », *BICS* 12 (1965), p. 29-33. [P ;
  référence à vérifier : « BICS Suppl. XII » dans l'extrait de P.]
- **Tessier 1974** — A. Tessier, « Euripide, *Andromeda* fr. 118 N² », *BIFG* 1 (1974), p. 128-135 : le
  fragment parodié aux vv. 1065 sqq. [P ; vers à vérifier]
- **Mureddu 1987** — P. Mureddu, « Un caso singolare di "teatro nel teatro" : la scena di Eco nelle
  *Tesmoforiazuse* », *AFLC* 6 (1987), p. 15-22. *Vers* : 1056-1097. [P]
- **Bubel 1991** — F. Bubel, *Euripides. Andromeda*, Stuttgart, 1991. [P] ; **Klimek-Winter 1993** —
  R. Klimek-Winter, *Andromedatragödien. Sophokles, Euripides, Livius Andronicus, Ennius, Accius* (Beiträge zur
  Altertumskunde 21), Stuttgart, 1993. [AO] [P] Éditions commentées des fragments d'*Andromède*, avec la parodie
  aristophanienne.
- **Coulon 1957** (vv. 1015-1055 ; v. 1047 : ἂν ἔτικτε de Wilamowitz), **Hose 1986-1987** (v. 1015),
  **Lourenço 2000** (métrique), **Méndez Dosuna 2010** (vv. 1054-1055) : § 1.3.
- **Mastromarco 2008** — G. Mastromarco, « La parodia dell'*Andromeda* euripidea nelle *Tesmoforiazuse* di
  Aristofane », *Cuadernos de Filología Clásica. Estudios griegos e indoeuropeos* 18 (2008), p. 177-188 : reprise
  de la langue, de la métrique, de la musique et de la mise en scène du modèle (vv. 1009-1135). DOI
  10.5209/rev_CFCG.2008.v18.32005 ; libre. *Accès* : `EU/la parodia dell andromeda*.PDF`. [lu, d'après
  `recherche/drive_ressources.md` § 4.3]
- **Major 2013** — W. E. Major, « Staging *Andromeda* in Aristophanes and Euripides », *CJ* 108 (2013),
  p. 385-403 : ce que la parodie révèle de la mise en scène de l'*Andromède* (rocher, liens, Écho, Persée). DOI
  10.5184/classicalj.108.4.0385. [méta]
- **Assaël 2014** — J. Assaël, « L'Éther initiatique dans l'*Andromède* d'Euripide », *Loxias* 45 (2014). *Accès* :
  `EU/L'Éther initiatique dans l'Andromède d'Euripide loxias-7817.pdf`. [lu, d'après `recherche/drive_ressources.md`]
- **Di Virgilio 2019** — L. Di Virgilio, « Some Thoughts on Humor and Music in Aristophanes' Plays » [revue à
  identifier ; version antérieure dans H. Kato, L. Lomiento (éd.), *The Mediterranean as a Plaza* (EPHESO 6),
  Cisalpino, 2018, p. 27-47] : effets comiques de la musique et du mètre, avec la colométrie de l'auteure pour
  la monodie d'Andromède. *Vers* : 1015-1055. *Accès* : `TH/Thesm vv 1015 1051 pp24sqq.pdf`. [lu, début]
- **Melzer 2022** — A. Melzer, « Comic Echopoetics in Aristophanes' *Thesmophoriazousai* », *AJPh* 143 (2022),
  p. 385-412 : la scène d'Écho comme poétique de la répétition et de l'appropriation. DOI 10.1353/ajp.2022.0016.
  *Vers* : 1056-1097. [méta]
- Hors des *Thesm.*, mais utiles pour la réception de l'*Andromède* : R. F. Moorton, « Euripides' *Andromeda* in
  Aristophanes' *Frogs* », *AJPh* 108 (1987), p. 434-436 [pagination à vérifier], DOI 10.2307/294665 ;
  P. Sfyroeras, « πόθος Εὐριπίδου : Reading *Andromeda* in Aristophanes' *Frogs* », *AJPh* 129 (2008), p. 299-317,
  DOI 10.1353/ajp.0.0014. [méta]

*Iphigénie et le dénouement (vv. 1160-1231)*

- **Bobrick 1991** — E. Bobrick, « Iphigeneia Revisited : *Thesmophoriazusae* 1160-1225 », *Arethusa* 24 (1991),
  p. 67-76 : le dénouement (Euripide en entremetteuse, la danseuse et le Scythe) mis en rapport avec
  l'*Iphigénie* d'Euripide. *Accès* : `TH/IPHIGENEIA REVISITED*.pdf` (image sans couche texte). [S ; résumé
  d'après le titre, article à lire]
- **Di Bari 2010, 2013** (§ 1.3), **Totaro 2022** (§ 2.7), **Hall 1989** (§ 2.6 : rapprochement de la scène
  finale avec l'*Iphigénie en Tauride*).

### 2.5 Agathon, Clisthène ; travestissement, genre, mimèsis

*Le prologue et la scène d'Agathon (vv. 1-279)*

- **Roberts 1900** — W. Rhys Roberts, « Aristophanes and Agathon », *JHS* 20 (1900), p. 44-56 : le portrait
  d'Agathon et ce qu'il dit de son style. DOI 10.2307/623742. [méta]
- **Lévêque 1955** — P. Lévêque, *Agathon* (Annales de l'Université de Lyon, 3e s., Lettres 26), Paris, 1955 :
  monographie de référence (vie, fragments, la parodie des *Thesm.*). [AO] [P]
- **Cantarella 1967** — R. Cantarella, « Agatone e il prologo delle *Tesmoforiazuse* », dans *Κωμῳδοτραγήματα.
  Studia Aristophanea… W. J. W. Koster in honorem*, Amsterdam, 1967, p. 7-15 [pagination à vérifier] (= *Scritti
  minori sul teatro greco*, Brescia, 1970, p. 325-333 ; trad. all. dans Newiger 1975, p. 324-338). [P]
- **Snyder 1974** — J. McIntosh Snyder, « Aristophanes' Agathon as Anacreon », *Hermes* 102 (1974), p. 244-246 :
  la mise d'Agathon (vv. 136-145, 159-163) imite l'iconographie d'Anacréon. [AO] [P ; vers à vérifier]
- **West 1992** — M. L. West, article de *ZPE* 92 (1992), p. 47-50 [titre à vérifier] : parallèles hymniques
  d'époque impériale (Mésomède) à la prière du serviteur d'Agathon (vv. 43-50), d'après S. *Vers* : 43-50. [S]
- **Pretagostini 1977** — R. Pretagostini, « L'omosessualità di Agatone nelle *Tesmoforiazuse* di Aristofane e la
  figura del κελητίζειν (v. 153) », dans *ΜΟΥΣΑ. Scritti in onore di G. Morelli*, Bologne, 1977, p. 117-122. *Vers* :
  153. [P]
- **Muecke 1982a** — F. Muecke, « A Portrait of the Artist as a Young Woman », *CQ* n.s. 32 (1982), p. 41-55 :
  la théorie de la mimèsis d'Agathon (vv. 146-172) et son costume. DOI 10.1017/S0009838800022783. [méta] [AO] [S]
- **Chirico 1989, 1990** — M. L. Chirico, article de *PP* 44 (1989), p. 174-183 [titre à vérifier] (costume
  d'Agathon, vv. 161-162, d'après S.) ; « Per una poetica di Aristofane », *PP* 45 (1990), p. 95-115. *Vers* :
  161-162. [S]
- **Blanchard 1994** — A. Blanchard, « La parodie d'Agathon et la structure des "Bucoliques" de Virgile.
  Aristophane, *Thesmophories*, 101-130 », dans *Storia, poesia e pensiero nel mondo antico. Studi in onore di
  M. Gigante*, Naples, 1994, p. 49-61 : structure amébée du chant d'Agathon. *Vers* : 101-130. [P]
- **Stohn 1993** — G. Stohn, « Zur Agathonszene in den *Thesmophoriazusen* des Aristophanes », *Hermes* 121
  (1993), p. 196-205. *Vers* : 95-265. [S] [P]
- **Saetta Cottone 2003** — R. Saetta Cottone, « Agathon, Euripide et le thème de la ΜΙΜΗΣΙΣ dramatique dans les
  *Thesmophories* d'Aristophane », *REG* 116 (2003), p. 445-469 : la dialectique Agathon-Euripide reproduit la
  scène des *Acharniens* (le héros emprunte un déguisement au poète tragique) ; le procès des femmes rappelle le
  procès de Cléon contre Aristophane ; la parodie vise le « réalisme » euripidien. DOI 10.3406/reg.2003.4546.
  *Accès* : `AR/agarh eur et le theme de vla mimesis dans les thesmophories.pdf` ; libre (Persée). [lu, résumé]
- **Mauduit–Saetta Cottone 2014** — Chr. Mauduit, R. Saetta Cottone, « Voir ou entendre : faut-il choisir ? Une
  analyse de la réception théâtrale dans le prologue des *Thesmophories* », *Cahiers des études anciennes* 51
  (2014), p. 45-73 : le dialogue initial sur la vue et l'ouïe (vv. 5-21) comme réflexion sur la réception du
  spectacle ; au v. 5, ὅσ' (M) préféré à ὅς (R). *Vers* : 1-24. *Accès* : `AR/Voir_ou_entendre_faut-il_choisir_Une_ana.pdf`
  ; libre (OpenEdition, HAL). [lu, début]
- **Micalella 2005** — D. Micalella, « Euripide e Agatone nelle *Tesmoforiazuse* di Aristofane : due poetiche a
  confronto », *SIFC* s. IV, 3.2 (2005), p. 188-194. [méta]
- **Duncan 2006** — A. Duncan, *Performance and Identity in the Classical World*, Cambridge, 2006, ch. 1 « Drag
  Queens and In-Betweens : Agathon and the Mimetic Body », p. 25-57 : l'acteur et le corps mimétique ; version
  préalable : « Agathon, Essentialism, and Gender Subversion in Aristophanes' *Thesmophoriazusae* » (2001, dépôt de
  l'Université du Nebraska, digitalcommons.unl.edu, classicsfacpub 83 ; téléchargement bloqué). [méta]
- **Nieddu 2010** — G. F. Nieddu, « Il canto di Agatone nelle *Tesmoforiazuse* : "deificazione" della musica e
  vanificazione del contenuto », *Incontri triestini di filologia classica* 8 (2008-2009), p. 239-253 : le chant
  d'Agathon (vv. 101-129), musique « divinisée » au détriment du contenu. Libre : openstarts.units.it (serveur
  injoignable lors du téléchargement). *Vers* : 101-129. [méta]
- **Sissa 2012** — G. Sissa, « Agathon and Agathon. Male Sensuality in Aristophanes' *Thesmophoriazusae* and
  Plato's *Symposium* », *EuGeStA* 2 (2012), p. 25-70 : l'Agathon efféminé de la comédie
  et l'Agathon du *Banquet*, deux images de la sensualité masculine. *Accès* : `W/Sissa_2012_EuGeStA2_Agathon.pdf`.
  [lu, début]
- **Kyriakou 2013** — P. Kyriakou, « Poetic Representation and Nature in the Agathon Scene of Aristophanes'
  *Thesmophoriazusae* », *C&M* 64 (2013), p. 139-159 ; libre : ikee.lib.auth.gr (serveur injoignable). [méta]
- **Navarro Martínez 2013** — V. L. Navarro Martínez, « La *Agathonszene* : una teoría poética en *Tesmoforiantes*
  de Aristófanes », n° 1, p. 55-74 [revue à identifier ; dépôt RODERIC, Valence, protégé par un défi anti-robot].
  [méta]
- **Di Virgilio 2018** — L. Di Virgilio, « Che cosa sta componendo Agatone nelle *Tesmoforiazuse* di
  Aristofane », p. 71-101 [revue à identifier ; Fabrizio Serra, DOI 10.19272/201806501004]. *Vers* : 101-129.
  [méta]
- **Gavazza 2020, 2022** — B. Gavazza, « Der Tragiker Agathon bei Aristophanes und Platon : der dramatische Aufbau
  eines devianten Verhaltens », dans *Transgression und Devianz in der antiken Welt*, Stuttgart, 2020, p. 7-20,
  DOI 10.1007/978-3-476-05508-8_2 ; version anglaise dans *Transgression and Deviance in the Ancient World*, 2022,
  p. 5-17, DOI 10.1007/978-3-476-05873-7_2. [méta]
- **Celotto 2022** — G. Celotto, « Agathon's *Iliupersis* in Aristophanes' *Thesmophoriazusae* », *SO* 97 (2022),
  p. 65-74 : le sujet troyen du chant d'Agathon. DOI 10.1080/00397679.2022.2125222. *Vers* : 101-129. [méta]
- **Saetta Cottone 2023** — R. Saetta Cottone, « Agathon élève de Gorgias élève d'Empédocle. Généalogies
  intellectuelles entre Aristophane (*Thesmophories*) et Platon (*Banquet*) » [chapitre d'ouvrage diffusé par
  Cairn ; volume à identifier]. [méta]
- Voir aussi **Clements 2009** (vv. 1-2, 277-279, 376 : χελιδών désigne aussi une étoile visible avant l'aube en
  avril 411 ; l'action commence avant l'aube et dure vingt-quatre heures), *Mnemosyne* 62 (2009), p. 535-547, DOI
  10.1163/156852509X339905, `TH/Chelidon Ashley Clements Thesmophoriazusae Two Dawns.pdf` [lu, résumé] ;
  **Clements 2014** (§ 2.1) ; **Beall 2001** (réfutation de l'étoile Χελιδών, `recherche/drive_ressources.md`
  § 4.5) ; **Mureddu 1992**, **Stepantsov 2022, 2024**, **Sansone 1987**, **Viketos 1989** (§ 1.3) ; **Gavazza
  2022** (scholies au prologue, § 1.5).

*Clisthène (vv. 571-654)*

- Pas d'étude spécifique repérée : voir Olson 1992 (noms, p. 316-318, cité par S. au v. 574) et Kanavou 2010
  (§ 1.4), Taaffe 1993 (§ 2.1), Kilmer 1982 (ci-dessous) ; pour le v. 605 (Kléonymos), **Storey 1989** —
  I. C. Storey, « The "Blameless Shield" of Kleonymos », *RhM* 132 (1989), p. 247-261 : contre l'interprétation
  littérale des plaisanteries sur le bouclier jeté. *Accès* : `.sources/drive/fichiers/thesm v 605 Cleonyme Storey.pdf` ; libre (RhM, Cologne). [lu, début]

*Travestissement, genre, femmes*

- **De Wit-Tak 1968** — Th. M. De Wit-Tak, « The Function of Obscenity in Aristophanes' *Thesmophoriazusae* and
  *Ecclesiazusae* », *Mnemosyne* 21 (1968), p. 357-365. DOI 10.1163/156852568X00428. [méta] [P]
- **Oeri 1948** — H. G. Oeri, *Der Typ der komischen Alten in der griechischen Komödie*, diss. Bâle, 1948. [AO] [P]
- **Kilmer 1982** — M. Kilmer, « Genital Phobia and Depilation », *JHS* 102 (1982), p. 104-112 (épilation du
  Parent, vv. 213-265). [P ; vers à vérifier]
- **Muecke 1982b** — F. Muecke, « Costume and Disguise in Fifth-century Drama », *Antichthon* 16 (1982), p. 17-34
  [P] ; **Muecke 1977** — « Playing with the Play : Theatrical Self-Consciousness in Aristophanes », *Antichthon* 11
  (1977), p. 52-67 [P].
- **Saïd 1987** — S. Saïd, « Travestis et travestissements dans les comédies d'Aristophane », *Cahiers du GITA* 3
  (1987), p. 217-248. [S]
- **Henderson 1987, 1991** — J. Henderson, « Older Women in Attic Old Comedy », *TAPhA* 117 (1987), p. 105-129 ;
  « Women and the Athenian Dramatic Festivals », *TAPhA* 121 (1991), p. 133-147 (présence des femmes au théâtre ;
  cf. Box 1964, § 1.3). [P]
- **Gardner 1989** — J. F. Gardner, « Aristophanes and Male Anxiety – The Defence of the *Oikos* », *G&R* 36
  (1989), p. 51-62. DOI 10.1017/S0017383500029338. [méta] [S]
- **Loraux 1993** — N. Loraux, « Aristophane, les femmes d'Athènes et le théâtre », dans J. M. Bremer,
  E. W. Handley (éd.), *Aristophane* (Entretiens sur l'Antiquité classique 38), Vandœuvres-Genève, 1993,
  p. 203-253. [P]
- **Høibye 1995** — A.-B. Høibye, « A Joke with the Inevitable : Men as Women and Women as Men in Aristophanes'
  *Thesmophoriazousai* and *Ekklesiazousai* » (chapitre, 1995 ; dépôt NORA, hdl 1956/24326). [méta]
- **McClure 1999** — L. K. McClure, *Spoken Like a Woman. Speech and Gender in Athenian Drama*, Princeton, 1999,
  ch. 6 « Obscenity, Gender, and Social Status in Aristophanes' *Thesmophoriazusae* and *Ecclesiazusae* »,
  p. 205-259. DOI 10.1515/9781400832446-008. [méta] [AO]
- **Stehle 2002** — E. Stehle, « The Body and its Representations in Aristophanes' *Thesmophoriazousai* : Where
  Does the Costume End ? », *AJPh* 123 (2002), p. 369-406. [AO]
- **Gherchanoc 2003** — F. Gherchanoc, « Les atours féminins des hommes : quelques représentations du
  masculin-féminin dans le monde grec antique », *Revue historique* 628 (2003), p. 739-791 (le travestissement du
  Parent et d'Agathon). *Accès* : `AR/F._Gherchanoc_Les_atours_feminins_des_ho.pdf`. [lu, d'après
  `recherche/drive_ressources.md` § 7.4]
- **Jay-Robert 2006** — G. Jay-Robert, « Rôle de la femme dans *Lysistrata*, les *Thesmophories* et l'*Assemblée
  des femmes* d'Aristophane, ou Les femmes et la création théâtrale », *Euphrosyne* 34 (2006), p. 35-50. DOI
  10.1484/J.EUPHR.5.124301. [méta]
- **Zerba 2012** — M. Zerba, *Doubt and Skepticism in Antiquity and the Renaissance*, Cambridge, 2012, ch.
  « Skeptical Inversions of Gender and Genre in Aristophanes' *Women of the Thesmophoria* and Shakespeare's *As You
  Like It* », p. 111-142. DOI 10.1017/CBO9781139175883.008. [méta]
- **Delli Pizzi 2012** — A. Delli Pizzi, « Les femmes aux Thesmophories, entre autorité et railleries : une
  déformation masculine ? » (communication, 2012 ; dépôt ORBi, Liège). [méta]
- **Compton-Engle 2015** — G. Compton-Engle, *Costume in the Comedies of Aristophanes*, Cambridge, 2015, ch. 3
  « Disguise, Gender, and the Poet », p. 88-109. DOI 10.1017/CBO9781316018217.004. [méta]
- **Boscà Cuquerella 2017** — A. Boscà Cuquerella, « Tres travestismos : tres tratamientos y tres finalidades
  diferentes en las *Tesmoforiantes* de Aristófanes », n° 5, p. 7-28 [revue à identifier ; dépôt RODERIC] : les
  travestissements d'Agathon, du Parent et d'Euripide. [méta]
- **Sells 2019** — [D. Sells ?, auteur à vérifier], *Parody, Politics and the Populace in Greek Old Comedy*,
  Londres, Bloomsbury, 2019, ch. « The Feminine Mistake : Household Economy in Aristophanes' *Thesmophoriazusae* ».
  DOI 10.5040/9781350060548.ch-006. [méta]
- **Cardoso 2020** — E. Vitório Cardoso, « Do rito ao palco : inversão de gênero e performance nas
  *Tesmoforiantes*, de Aristófanes », *Nuntius Antiquus* 15.2 (2020), p. 27-48. DOI 10.17851/1983-3636.15.2.27-48.
  *Accès* : `W/Cardoso_2020_NuntiusAntiquus15_rito_palco.pdf`. [lu, début]
- **Ruffell 2020** — I. Ruffell, « Poetics, Perversions, and Passing : Approaching the Transgender Narratives of
  *Thesmophoriazousai* », *ICS* 45.2 (2020), p. 333-367. DOI 10.5406/illiclasstud.45.2.0333 ; libre chez
  l'éditeur (téléchargement automatique bloqué). [méta]
- **Deihr 2022** — L. Deihr, « Aristophanes, *Women at the Thesmophoria* — Reality and the Egg : An Oviparody of
  Euripides », dans S. Olsen, M. Telò (éd.), *Queer Euripides. Re-Readings in Greek Tragedy*, Londres, 2022.
  DOI 10.5040/9781350249653.ch-020. [méta]
- **Volpi 2024** — P. Volpi, « Diotima : An Improved Female Paradigm Against Aristophanes' *Thesmophoriazusae* »,
  *Elephant & Castle* 34 (2024), p. 28-36. DOI 10.62336/unibg.eac.34.544 ; libre. [méta]
- **Philippides 2018** — K. Philippides, « Women Chattering about a Ritual : Plautus' *Poenulus* in the Light of
  Theocritus (*Id.* XV), Herondas (*Mim.* IV) and Aristophanes (*Thesm.*) », *Latomus* 77 (2018), p. 1033-1052.
  *Accès* : `TH/Peeters.pdf`. [lu, d'après `recherche/drive_ressources.md` § 4.5]
- Voir aussi Zeitlin 1981, Bobrick 1997, Taaffe 1993, Saetta Cottone 2005 (§ 2.1), Valdés Guía 2017 (§ 2.3) et
  les études sur le vêtement féminin (Perusino 2002, § 2.8).

### 2.6 Le Scythe et son grec (vv. 923-946, 1001-1007, 1083-1135, 1172-1225)

- **Plassart 1913** — A. Plassart, « Les archers d'Athènes », *REG* 26 (1913), p. 151-213 : le corps des archers
  scythes, esclaves publics. [P] [cité par Hall 1989] ; libre (Persée).
- **Friedrich 1918** — J. Friedrich, « Das Attische im Munde von Ausländern bei Aristophanes », *Philologus* 75
  (n.F. 29) (1918), p. 274-303 : étude fondatrice du grec des étrangers (le Scythe, le Triballe, Pseudartabas). [P]
  [cité par Hall 1989]
- **Vos 1963** — M. F. Vos, *Scythian Archers in Archaic Attic Vase-Painting* (Archaeologica Traiectina 6),
  Groningue, 1963. [AO]
- **Long 1986** — T. Long, *Barbarians in Greek Comedy*, Carbondale-Edwardsville, 1986. [cité par Hall 1989]
- **Hall 1989** — E. M. Hall, « The Archer Scene in Aristophanes' *Thesmophoriazusae* », *Philologus* 133 (1989),
  p. 38-54 : seul personnage barbare au langage longuement caricaturé ; un « pidgin » cohérent (phonétique,
  morphologie, genre et cas), à condition de corriger quelques normalisations de copistes (v. 1005 μᾶλλο pour
  l'amétrique μᾶλλον ; v. 1215 συβίνη de Brunck, jeu de mots avec καταβινεῖν) ; l'archer comme image des esclaves
  publics ; rapprochement de la scène finale avec l'*Iphigénie en Tauride*. DOI 10.1524/phil.1989.133.12.38.
  *Accès* : `TH/the archer scene in thesmophoriazusae.pdf`. [lu] Version revue : **Hall 2006** — « The Scythian
  Archer in Aristophanes' *Thesmophoriazusae* », dans *The Theatrical Cast of Athens. Interactions between Ancient
  Greek Drama and Society*, Oxford, 2006, p. 225-254, DOI 10.1093/acprof:oso/9780199298891.003.0008. [méta]
- **Brixhe 1988** — C. Brixhe, contribution sur la langue des étrangers chez Aristophane [titre à vérifier], dans
  R. Lonis (éd.), *L'Étranger dans le monde grec*, Nancy, 1988, p. 113-138. *Vers* : 1001-1225. [S]
- **Sier 1992** — K. Sier, « Die Rolle des Skythen in den *Thesmophoriazusen* des Aristophanes », dans
  C. W. Müller, K. Sier, J. Werner (éd.), *Zum Umgang mit fremden Sprachen in der griechisch-römischen Antike*,
  Stuttgart, 1992, p. 63-83. [S] [P]
- **Colvin 1999** — S. Colvin, *Dialect in Aristophanes and the Politics of Language in Ancient Greek Literature*,
  Oxford, 1999 (dialectes non attiques et parlers étrangers ; ch. « Old Comedy : Shorter Passages and Fragments »,
  p. 264-295). DOI 10.1093/oso/9780198152491.001.0001. [méta ; pages sur le Scythe à vérifier]
- **Willi 2002, 2003** — A. Willi, « Languages on Stage : Aristophanic Language, Cultural History, and Athenian
  Identity », dans A. Willi (éd.), *The Language of Greek Comedy*, Oxford, 2002, p. 111-149 [méta] ; *The
  Languages of Aristophanes. Aspects of Linguistic Variation in Classical Attic Greek*, Oxford, 2003 (c. r.
  R. M. Rosen, *JHS* 2005 ; E. Crespo, *Kratylos* 52, 2007, p. 70-75) [méta ; chapitres à vérifier]. AO n'ont pu
  utiliser le second (AO, p. x).
- **Ivantchik 2006** — A. Ivantchik, « "Scythian" Archers on Archaic Attic Vases : Problems of Interpretation »,
  *Ancient Civilizations from Scythia to Siberia* 12 (2006), p. 197-271 (contexte historique : les archers scythes
  d'Athènes). DOI 10.1163/157005706779851408. [méta]
- **Totaro 2022** (le trio Euripide-Térédon-Élaphion et le Scythe, vv. 1160-1231) : § 2.7.

### 2.7 Mise en scène, acteurs, costumes, accessoires ; chœur, parabase, musique

*Espace scénique, machines, acteurs*

- **Dover 1966, 1967** — K. J. Dover, « The Skene in Aristophanes », *PCPhS* n.s. 12 (1966), p. 2-17 (repris dans
  Newiger 1975, p. 99-123) ; « Portrait-Masks in Aristophanes », dans *Κωμῳδοτραγήματα*, Amsterdam, 1967,
  p. 16-28. [P]
- **Dearden 1976** — C. W. Dearden, *The Stage of Aristophanes*, Londres, 1976. [P]
- **Taplin 1977** — O. Taplin, « Did Greek Dramatists Write Stage Instructions ? », *PCPhS* n.s. 23 (1977),
  p. 121-130 (cf. la parépigraphe du v. 1187b, § 1.3 : Dover 1977, Hartwig
  2008). [P]
- **Hansen 1976**, **Russo 1962/1994** : § 2.1 ; **Residori 1979** (notes scéniques), **Seager 1981**
  (vv. 754-757) : § 1.3.
- **Dane 1984**, **AO** p. lxviii-lxx, **Storey 2006**, **Olson 2006** (nombre d'acteurs), **Boccaccini 2012**
  (vv. 624-625) : § 1.1, 1.3, 1.4.
- **Newiger 1989** — H.-J. Newiger, « Ekkyklema e mechané nella messa in scena del dramma greco », *Dioniso* 59
  (1989), p. 173-185 (l'eccyclème d'Agathon, vv. 95-96, 265 ; cf. Germain 2023, annexe III). [P]
- **Marzullo 1989** — B. Marzullo, « Lo "spazio scenico" in Aristofane », *Dioniso* 59 (1989), p. 187-200. [P]
- **Rehm 1988** — R. Rehm, article de *GRBS* 29 (1988), p. 263-307 [titre à vérifier ; libre : GRBS] : S. le
  suit pour placer l'autel de la scène de l'otage au centre de l'orchestre (vv. 689-758). *Vers* : 689-758. [S]
- **Thiercy 1986, 1987** — P. Thiercy, *Aristophane : fiction et dramaturgie*, Paris, 1986 ; « Il ruolo del
  pubblico nella commedia di Aristofane », *Dioniso* 57 (1987), p. 170-185. [P]
- **Chapman 1983** — G. A. H. Chapman, « Some Notes on Dramatic Illusion in Aristophanes », *AJPh* 104 (1983),
  p. 1-23. [P]
- **Stone 1980** — L. M. Stone, *Costume in Aristophanic Comedy*, Salem (N.H.), 1980 (New York, 1981). [AO] [P]
- **Revermann 2006** — M. Revermann, *Comic Business. Theatricality, Dramatic Technique, and Performance Contexts
  of Aristophanic Comedy*, Oxford, 2006 (méthode de la *performance criticism* ; *Thesm.* passim, pas de chapitre
  propre). DOI 10.1093/oso/9780198152712.001.0001. [méta]
- **Compton-Engle 2015**, **Stehle 2002** (costume) : § 2.5 ; **Germain 2021** (espace sacré et scénique) :
  § 2.3.
- **Mastromarco 2016** — G. Mastromarco, « Osservazioni sulle *Tesmoforiazuse* e sulle *Ecclesiazuse* di
  Aristofane », *Studia Philologica Valentina* 18, n.s. 15 (2016), p. 207-216 (même fascicule que Méndez Dosuna
  2016b). Libre : roderic.uv.es (hdl 10550/58927 ; défi anti-robot). [méta]
- **Scharffenberger 2024** — E. W. Scharffenberger, « The Dynamics of *Didaskalia* in Aristophanes'
  *Thesmophoriazusae* 846-1159 », *Logeion* 14.2 (2024) : les odes des vv. 947-1000 et 1136-1159 répondent au
  débat des vv. 383-430 sur ce qu'« enseigne » la tragédie euripidienne ; le chœur, ému mais lucide, oppose un
  modèle « constructiviste » d'apprentissage au modèle passif du premier épisode. DOI 10.26225/ghtc-t538.
  *Accès* : `W/Scharffenberger_2025_didaskalia_846-1159.html`. [lu, résumé]
- **Totaro 2022** — P. Totaro, « Note sceniche sulla *performance* orchestico-musicale del trio
  Euripide/Teredon/Elaphion nel finale delle *Tesmoforiazuse* di Aristofane », dans B. Zimmermann, A. Gostoli
  (éd.), *Nuove volute di versi*, Göttingen, 2022, p. 49-68. DOI 10.13109/9783949189326.49. *Vers* : 1160-1231.
  [méta]
- Réception moderne et mises en scène : *AJPh* 123.3 (2002), articles de G. Van Steen (productions grecques
  modernes), M.-K. Gamel (« The Julie Thesmo Show »), E. W. Scharffenberger (traduction d'Arrowsmith) [méta] ;
  J. Maitland, J. Buch, « Translating the Metaphor : Problems Solved and Circumvented in Staging Aristophanes'
  *Thesmophoriazusae* », dans *Griechisch-römische Komödie und Tragödie* II (Drama 5), Stuttgart-Weimar, 1997,
  p. 153-169, DOI 10.1007/978-3-476-04271-2_12 [méta ; série à vérifier] ; AO, introduction (productions modernes
  recensées par l'*Archive of Performances of Greek and Roman Drama*, Oxford).

*Chœur, prières, hymnes*

- **Kleinknecht 1937** — H. Kleinknecht, *Die Gebetsparodie in der Antike* (Tübinger Beiträge 28), Stuttgart,
  1937. [AO] [P] ; **Horn 1970** — W. Horn, *Gebet und Gebetsparodie in den Komödien des Aristophanes* (Erlanger
  Beiträge 38), Nuremberg, 1970. [AO] [P] Prières des vv. 295-371, 947-1000, 1136-1159.
- **Haldane 1965** (vv. 295-371) et **Prato 2000** (parodie de prières et de rites) : § 2.3.
- **Kaimio 1970** — M. Kaimio, *The Chorus of Greek Drama within the Light of the Person and Number Used*
  (Commentationes Humanarum Litterarum 46), Helsinki, 1970. [AO]
- **Zimmermann 1984** — B. Zimmermann, « The *Parodoi* of the Aristophanic Comedies », *SIFC* 2 (1984)
  [pagination à vérifier]. [P]
- **Anderson 1995** — C. A. Anderson, *Athena's Epithets. Their Structural Significance in Plays of Aristophanes*
  (Beiträge zur Altertumskunde), Stuttgart-Leipzig, 1995, ch. 3 « Athena in *Thesmophoriazusae* », p. 57-68
  (hymne des vv. 1136-1159). DOI 10.1515/9783110952261.57. [méta]
- **Bierl 1999, 2001** — A. Bierl, « Doppeltanz oder doppelte Freude ? Gedanken zum umstrittenen διπλῆν (Ar.
  *Thesm.* 982) aus einer performativen Perspektive », dans *Der Chor im antiken und modernen Drama*,
  Stuttgart-Weimar, Metzler, 1999, p. 27-47 [éditeurs du volume à vérifier] (libre : edoc.unibas.ch/13145) [méta] ;
  *Der Chor in der Alten Komödie* (2001), § 2.1.
- **Thomsen 1973** (vv. 947-1000), **Wycherley 1959** (v. 986), **Hartwig 2008** (vv. 982, 984), **Austin
  1971-1974** (la coryphée) : § 1.3.

*Parabase (vv. 785-845)*

- **Miller 1947** (§ 2.4), **Blanchard 2001** (§ 2.4) ; **Mastromarco 1987** — G. Mastromarco, « La parabasi
  aristofanea tra realtà e poesia », *Dioniso* 57 (1987), p. 75-93 [P] ; **Sifakis 1971** — G. M. Sifakis,
  *Parabasis and Animal Choruses*, Londres, 1971 [AO] ; **Hubbard 1991** (*The Mask of Comedy*, § 2.1) [AO].

*Musique et mètre* (renvoi : `recherche/metrique_structure.md`)

- **Di Virgilio 2026** — L. Di Virgilio, « Il docmio nelle *Tesmoforiazuse* di Aristofane », dans S. Cardinali,
  G. Galvani, R. M. Danese (éd.), *μελιγάρυες ὕμνοι. Studi offerti dagli allievi di dottorato a Liana Lomiento*
  (Incontri e percorsi), Urbino, Urbino University Press, 2026, p. 95-120 : inventaire des dochmies d'après la
  colométrie de R, avec des formes nouvelles ; révise Parker 1997. *Vers* : 676, 699-725, 913-914, 1015-1055,
  1136-1159. *Accès* : `W/DiVirgilio_2026_docmio_Thesm.pdf`. [lu, résumé]
- **Moutsopoulos 2000** — E. A. Moutsopoulos, « La musique dans l'œuvre d'Aristophane », dans *Le théâtre grec
  antique : la comédie* (Cahiers de la Villa Kérylos 10), Paris, 2000, p. 59-82. *Accès* : `AR/La musique dans l'oeuvre d'Aristophane.pdf`. [lu, début]
- Parker 1997, Lourenço 2000, Di Virgilio 2019 (§ 2.4), Gavazza 2022 (§ 1.5), Totaro 2022 (ci-dessus).

### 2.8 Langue, style, realia

*Langue et style*

- **Taillardat 1962** — J. Taillardat, *Les Images d'Aristophane. Études de langue et de style* (Annales de
  l'Université de Lyon, 3e s., Lettres 36), Paris, 1962 (2e éd. 1965). [AO] [P]
- **Komornicka 1964, 1967, 1981** — A. M. Komornicka, *Métaphores, personnifications et comparaisons dans l'œuvre
  d'Aristophane*, Wrocław, 1964 ; « Quelques remarques sur la parodie dans les comédies d'Aristophane », *QUCC* 3
  (1967), p. 51-74 [pagination à vérifier] ; « Sur le langage érotique de l'ancienne Comédie attique », *QUCC*
  n.s. 9 (1981), p. 55-83. [P]
- **Henderson 1975/1991** — J. Henderson, *The Maculate Muse. Obscene Language in Attic Comedy*, New Haven,
  1975 (2e éd. 1991). [AO] [P] ; **Jocelyn 1980** — H. D. Jocelyn, « A Greek Indecency and its Students :
  ΛΑΙΚΑΖΕΙΝ », *PCPhS* n.s. 26 (1980), p. 12-66 [P] ; **Bain 1991** — D. Bain, « Six Greek Verbs of Sexual
  Congress », *CQ* 41 (1991), p. 51-77 [P] ; **Guzmán Carsí 2015** (mémoire, `recherche/drive_ressources.md`
  § 7.1).
- **Moulton 1979** — C. Moulton, « The Lyric of Insult and Abuse in Aristophanes », *MH* 36 (1979), p. 23-48
  (= *Aristophanic Poetry*, p. 18-47). [P]
- **Morenilla-Talens 1988** — C. Morenilla-Talens, « Beiträge zum Studium der Metaphern bei Aristophanes :
  *Thesmophoriazusae* 49-62 », *Eranos* 86 (1988), p. 160-174. *Vers* : 49-62. [P]
- **Halliwell 1990** — S. Halliwell, « The Sounds of the Voice in Old Comedy », dans E. M. Craik (éd.), *'Owls to
  Athens'*, Oxford, 1990, p. 69-79. [P]
- **Sommerstein 1995** — A. H. Sommerstein, « The Language of Athenian Women », dans F. De Martino,
  A. H. Sommerstein (éd.), *Lo spettacolo delle voci*, t. II, Bari, 1995, p. 61-85 ; **McClure 1995** — « Female
  Speech and Characterization in Euripides », *ibid.*, p. 35-60. [P]
- **Willi 2002, 2003** : § 2.6 ; **López Eire 1986, 1996** — A. López Eire, « La lengua de la comedia
  aristofánica », *Emerita* 54 (1986), p. 237-274 [P] ; *La lengua coloquial de la comedia aristofánica*, Murcie,
  1996 [AO].
- **Clements 2013** — A. Clements, « "Looking Mustard" : Greek Popular Epistemology and the Meaning of δριμύς »,
  dans S. Butler, A. Purves (éd.), *Synaesthesia and the Ancient Senses*, Durham, 2013, p. 71 sqq. *Accès* :
  `AR/Lookink mustard*.pdf`. [lu, d'après `recherche/drive_ressources.md` § 7.1 ; vers à relever]
- Méndez Dosuna 2016b (κόρη au v. 406) : § 1.3.
- Vocabulaire médical : S. Byl, « Le vocabulaire hippocratique dans les comédies d'Aristophane », *RPh* 64
  (1990), p. 151-162 [P] ; Jouanna 2000, Soleil 2011 (`recherche/drive_ressources.md` § 7.3).
- Noms propres : Olson 1992, Sommerstein 1980, Kanavou 2010 (§ 1.4) ; F. Bechtel, *Die attischen Frauennamen*,
  Göttingen, 1902. [P]
- Proverbes : R. Bauck, *De proverbiis aliisque locutionibus ex usu vitae communis petitis in Aristophanis
  comoediis*, diss. Königsberg, 1880 (`.sources/drive/fichiers/Grec/Proverbes/De_proverbiis*.pdf`) [titre d'après
  le fichier, lieu et date à vérifier] ; Stepantsov 2024 (§ 1.3).

*Realia*

- **Perusino 2002** — F. Perusino, « L'ἔγκυκλον, un mantello femminile nelle commedie di Aristofane », *QUCC* n.s.
  72 (2002), p. 129-133 (ἔγκυκλον aux vv. 261 et 499). *Accès* : `TH/Encycle.pdf`. [lu, d'après
  `recherche/drive_ressources.md` § 7.2] — l'auteur de la présente édition a proposé d'y voir une
  jupe (article de *Kentron*, 2023 ; voir `recherche/drive_ressources.md` § 8.2).
- **Milne–von Bothmer 1953** — M. J. Milne, D. von Bothmer, « Καταπύγων, καταπύγαινα », *Hesperia* 22 (1953),
  p. 215-224 (καταπύγων au v. 200). [P]
- **Rolley 1966** (l'outre « sacrifiée », vv. 740 sqq.), **Rolley 1974**, **Henderson 1972** (lécythe), **Zucker
  2012** (coquillages), **Fournet–Redon** (bain) : `recherche/drive_ressources.md` § 4.5 et 7.4.
- **Brun 1987** — P. Brun, « Hyperbolos, la création d'une "légende noire" », *DHA* 13 (1987), p. 183-198 (v. 840).
  *Accès* : `AR/dha_0755-7256_1987_num_13_1_1756.pdf`. [lu, d'après `recherche/drive_ressources.md` § 7.3]
- **J. Vickers 2019** — Jonathan Vickers, « The Lion Cub *Ainos*, Suppositious Children, and *Thesmophoriazusae* »,
  *RhM* 162 (2019), p. 1-34 : l'enfant supposé appelé « lion » (vv. 514-516) évoque la fable
  du lionceau élevé dans la maison, ruineux quand sa nature se révèle ; thème de l'authenticité dans toute la pièce.
  *Vers* : 502-516. *Accès* : `W/JVickers_2019_RhM162_Lion_Cub_Ainos.pdf` ; libre (RhM). [lu, résumé]

## 3. Iconographie

*Le cratère de Würzburg (Martin-von-Wagner-Museum H 5697)* — cratère en cloche apulien, vers 370 av. J.-C.,
attribué au peintre de Schiller (A. D. Trendall, *The Red-Figured Vases of Apulia*, Oxford, 1978, p. 65, d'après
Csapo 1986) : un homme mal rasé, couronné d'un bandeau, menace d'un couteau une outre chaussée de petits souliers ;
une femme accourt avec un vase pour recueillir le « sang » ; un miroir figure au-dessus du couteau. Identifié à la
scène des vv. 689-759 (plus précisément vv. 750-755 selon AO, 753-756 selon S.).

- **Kossatz-Deissmann 1980** — A. Kossatz-Deissmann, « Telephus travestitus », dans H. A. Cahn, E. Simon (éd.),
  *Tainia. Festschrift für Roland Hampe*, Mayence, 1980, p. 281-290, pl. 60 : publication du vase, lu comme une
  farce italiote parodiant le *Télèphe* d'Euripide, influencée par les *Thesm.* [cité par Csapo 1986 et AO]
- **Csapo 1986** — E. Csapo, « A Note on the Würzburg Bell-Crater H5697 ("Telephus Travestitus") », *Phoenix* 40
  (1986), p. 379-392 : le vase illustre les *Thesm.* elles-mêmes (bandeau emprunté à Agathon, vv. 257-260 ; barbe
  mal rasée, vv. 221-231 ; miroir, vv. 233-235) ; conséquences pour la thèse de Webster sur les vases « phlyaques »
  et les reprises de la comédie attique en Italie du Sud. DOI 10.2307/1088168. *Accès* : `AR/a note on the wurzburg bell-crater csapo1986.pdf`. [lu]
- **Taplin 1987** — O. Taplin, « Phallology, Phlyakes, Iconography and Aristophanes », *PCPhS* n.s. 33 (1987),
  p. 92-104 ; version revue : « Classical Phallology, Iconographic Parody and Potted Aristophanes », *Dioniso* 57
  (1987), p. 95-109 : conclusions voisines de celles de Csapo, obtenues indépendamment ; « parodie iconographique »
  du schéma tragique de la femme qui fuit. [AO] [P] [Csapo 1986, postscriptum]
- **Taplin 1993** — O. Taplin, *Comic Angels and Other Approaches to Greek Drama through Vase-Paintings*, Oxford,
  1993, p. 36-40 (et p. 30-36, 41-47 sur les reprises de comédies attiques en Italie du Sud). [AO] [S]
- **Green 1994** — J. R. Green, *Theatre in Ancient Greek Society*, Londres, 1994, p. 65-67. [AO]
- **Commentaires** : AO, introduction, § V.E « The Würzburg "Telephos" Krater », p. lxxv-lxxvii et pl. 1 (le vase
  comme « récit visuel » qui rappelle aussi la scène du rasage) [lu, extrait textuel] ; S., frontispice et notes
  aux vv. 733-734 et 754-757 (indications scéniques tirées du vase) [lu, extrait] ; P., jaquette (vv. 754-755).
- Contexte (vases « phlyaques » et comédie attique) : T. B. L. Webster, « South Italian Vases and Attic Drama »,
  *CQ* 42 (1948), p. 15-27 [cité par Csapo 1986 et AO] ; A. D. Trendall, *Phlyax Vases*², Londres, 1967 (BICS
  Suppl. 19) [Csapo] ; A. D. Trendall, T. B. L. Webster, *Illustrations of Greek Drama*, Londres, 1971 [P] ;
  T. B. L. Webster, *Monuments Illustrating Old and Middle Comedy* (BICS Suppl. 23), 2e éd. 1969, 3e éd. revue par
  J. R. Green (BICS Suppl. 39), 1978 [P] [AO] ; B. A. Sparkes, « Illustrating Aristophanes », *JHS* 95 (1975),
  p. 122-135 [AO] [P].

*Autres documents*

- **Todisco 2012, 2017** — L. Todisco, « Il vaso di New York MMA 24.97.104 e le *Tesmoforiazuse* di Aristofane »,
  p. 187-198 [publication à identifier], et « Un'ulteriore osservazione sul rapporto tra la scena del cratere di New
  York, MMA 24.97.104 e le *Tesmoforiazuse* di Aristofane », p. 439-441 [publication à identifier] : propose un
  second vase lié à la pièce. [méta]
- **Luce 1918** — S. B. Luce, « A Scene from Aristophanes on a Greek Vase-Painting », *CW* 11 (1918), p. 186-188.
  [P ; scène et pièce à vérifier]
- Archers scythes dans la céramique attique : Vos 1963, Ivantchik 2006 (§ 2.6).
- Thesmophories et culte de Déméter : E. Simon, *Festivals of Attica*, Madison, 1983 [AO] [P] ; L. Beschi, art.
  « Demeter », *LIMC* IV (1988), p. 844-871 [P] ; M. Sguaitamatti, *L'Offrante de porcelet dans la coroplathie
  géléenne*, Mayence, 1983 [P] ; A. Muller, *Les Terres cuites votives du Thesmophorion : de l'atelier au
  sanctuaire* (Études thasiennes 17), Athènes-Paris [1996 ?], c. r. L. Burn, *CR* 1998 [méta] ; S. Lewis, *The Athenian Woman.
  An Iconographic Handbook*, Londres-New York, 2002 [AO].
- Images réunies par l'auteur (cratère de Würzburg, « Écho voilée » Beazley 7864, vase Beazley 204020, crocote,
  encycle, M. Bieber, *Griechische Kleidung*, pl. VIII 1 ; Millin, Bröndsted) : `recherche/drive_ressources.md`
  § 7.4.

## 4. Index par vers des discussions textuelles et exégétiques

Conventions. Chaque entrée renvoie aux clés des notices des § 1 à 3 (où se trouve la référence complète). Sans
mention particulière, la discussion porte sur le texte (leçon, conjecture, colométrie, ponctuation) ; *attribution*
= partage des répliques ; *mètre* = analyse métrique ou colométrique ; *interprétation* = exégèse, mise en scène,
contexte. « Austin 1987, p. N » renvoie au répertoire vers par vers de « Textual Problems in Ar. *Thesm.* »
(*Δωδώνη* 16, 1987, p. 69-86 : antériorité des conjectures, notes inédites de Kaibel, Wilamowitz et Maas) ; il
a été relevé automatiquement sur l'extrait textuel (`.sources/drive/ravennas/Austin_1987_*.txt`, script
`.travail/etudes/scripts/austin1987_index.py`), puis contrôlé à la main pour les entrées douteuses : quelques
lemmes peuvent manquer. Les vers des commentaires (AO, S., P., Wilson) ne sont pas indexés ici ; les éditions
anciennes sont dans `recherche/conjectures_sources.md`. « *Apparat de Wilson* » signale, pour mémoire, les
conjectures de critiques des XXe-XXIe s. (et de Kaibel, van Leeuwen, Richards) citées dans l'apparat de l'OCT, d'après
le répertoire critique du dépôt (`edition/donnees/repertoire_critique/wilson2007_*.jsonl`, état du 28 octobre 2026,
certaines tranches étant encore en cours de saisie) : le lieu de publication
de ces conjectures est à chercher parmi les notices ci-dessus (Austin 1987, 1990 ; S. ; AO…). Index produit par
`.travail/etudes/scripts/index_vers.py` (données manuelles : `.travail/etudes/index_manuel.tsv`).

- **v. 1** : Austin 1987, p. 69 ; Stepantsov 2024
- **vv. 1-2** : *interprétation* : Clements 2009, χελιδών, étoile du petit matin
- **vv. 1-24** : *interprétation* : Mauduit–Saetta Cottone 2014
- **vv. 1-294** : Gordziejew 1937 — *interprétation* : Clements 2014
- **v. 2** : Austin 1987, p. 69 ; Austin 1990, ἀλοῶν, p. 11 ; Maas 1913, ἀλύων
- **v. 5** : Mauduit–Saetta Cottone 2014, ὅσ' de M contre ὅς de R ; Mureddu 1992 — *apparat de Wilson* : Sommerstein, ὅς γ'
- **vv. 8-10** : Ritschl 1862
- **v. 11** : Austin 1987, p. 70
- **vv. 11-18** : Dover 1977, variantes d'auteur
- **v. 12** : Austin 2011 ; Liberman 2008, suppression d'après van Herwerden, adoptée par Wilson
- **vv. 16-18** : Willems 1908
- **v. 18** : Anonyme 1863 ; Austin 1987, p. 70 ; Kamerbeek 1967 ; Ritschl 1862
- **v. 21** : Mureddu 1992 ; Willems 1908
- **vv. 22-24** : Willems 1908
- **v. 23** : Austin 1987, p. 70
- **vv. 23-24** : Austin 1990
- **v. 30** : Austin 1987, p. 70
- **v. 33** : Seager 1981, énoncé, non question — *apparat de Wilson* : R. J. Seager, ponctuation
- **v. 34** : Austin 1987, p. 70 ; Austin 1990 — *apparat de Wilson* : Kaibel, οὔτοι μὰ τὸν Δί' omisso γ'
- **vv. 43-50** : *interprétation* : West 1992
- **v. 44** : *apparat de Wilson* : Austin, τε
- **v. 45** : Austin 1990
- **vv. 49-62** : *interprétation* : Morenilla-Talens 1988
- **vv. 57-62** : Ciriello–Imperio 1991
- **v. 58** : Austin 1987, p. 71
- **vv. 59-62** : Austin 1990
- **v. 60** : Austin 1987, p. 71 ; Willems 1908
- **vv. 60-62** : Austin 1990, p. 13-14
- **v. 63** : Coulon 1934a
- **vv. 64-65** : Austin 1990
- **v. 69** : Austin 1987, p. 71
- **v. 74** : Austin 1987, p. 71
- **v. 80** : Abramovich 2026 ; Austin 1990 ; Storey 2006, R conservé
- **v. 83** : Austin 1987, p. 71
- **v. 86** : Austin 1987, p. 71
- **v. 87** : Storey 2006, εἰς ταύτας, Sandbach — *apparat de Wilson* : Sandbach, εἰς ταύτας
- **v. 90** : Austin 1987, p. 72
- **v. 91** : Austin 1987, p. 72 ; Macía Aparicio 2002, écart avec Coulon non signalé par P.
- **v. 95** : Austin 1987, p. 72 — *apparat de Wilson* : Kaibel, τί
- **vv. 95-265** : *interprétation* : Stohn 1993
- **v. 96** : Austin 1987, p. 72
- **v. 97** : Austin 1987, p. 72
- **v. 99** : Austin 1987, p. 72 — *apparat de Wilson* : Austin (1987), ἢν
- **v. 100** : Coulon 1953
- **vv. 101-129** : *interprétation* : Celotto 2022 ; Di Virgilio 2018 ; Nieddu 2010
- **vv. 101-130** : *interprétation* : Blanchard 1994
- **v. 103** : Austin 1987, p. 73
- **v. 106** : Ritschl 1867
- **v. 107** : Austin 1987, p. 73
- **v. 111** : Austin 1987, p. 74
- **v. 113** : Ritschl 1867 — *apparat de Wilson* : Wilson, προφέρω
- **v. 115** : Austin 1987, p. 74
- **vv. 117-118** : Olson 1995
- **v. 118** : *apparat de Wilson* : Sommerstein, ὀλβίαν τε
- **v. 120** : Austin 1987, p. 74
- **vv. 120-122** : Austin 1990
- **vv. 123-127** : Taillardat 1972
- **v. 126** : Melandri 2004, traduction et commentaire de P.
- **vv. 126-129** : Coulon 1937
- **v. 127** : Austin 1987, p. 74
- **v. 128** : *apparat de Wilson* : Austin (1987), ἀγάλλετε
- **vv. 133-144** : Grassi 1956
- **vv. 134-140** : Stepantsov 2022
- **vv. 137-138** : Austin 1990
- **v. 138** : Austin 1990, βάρβιτος, p. 17-18
- **v. 139** : *apparat de Wilson* : van Leeuwen, ξύμφορα
- **v. 140** : Olson 1995, R défendu — *apparat de Wilson* : Dover, κατρόπτου
- **v. 142** : Coulon 1953
- **v. 148** : Austin 1974 ; Austin 1987, p. 74 ; Sansone 1987 ; Viketos 1989
- **vv. 149-150** : *interprétation* : Muecke 1982a, théorie de la mimèsis
- **v. 153** : *interprétation* : Pretagostini 1977, κελητίζειν
- **vv. 154-155** : Stepantsov 2022
- **v. 158** : Austin 1990
- **v. 159** : Austin 1987, p. 75
- **vv. 161-162** : *interprétation* : Chirico 1989, 1990 ; Snyder 1974, Agathon et Anacréon
- **v. 164** : Olson 1995, R défendu — *apparat de Wilson* : Sommerstein, τούτου
- **v. 165** : Austin 1987, p. 75
- **vv. 166-168** : Coulon 1953
- **v. 200** : *interprétation* : Milne–von Bothmer 1953, καταπύγων
- **v. 204** : Austin 1987, p. 75
- **vv. 209-210** : Austin 1990
- **v. 217** : Austin 1987, p. 75 ; Coulon 1953 ; Willems 1908
- **v. 219** : Austin 1987, p. 75
- **v. 223** : Austin 1987, p. 75
- **v. 230** : Austin 1987, p. 76 ; Willems 1908
- **v. 232** : Austin 1987, p. 76
- **v. 234** : Austin 1987, p. 76 — *apparat de Wilson* : Barrett, ponctuation
- **v. 235** : Austin 1987, p. 76
- **vv. 241-242** : Marzullo 1994
- **vv. 241-247** : Coulon 1926
- **v. 242** : Austin 1977 ; Austin 1984 ; Austin 1987, p. 76 ; Goossens 1941 ; Marzullo 1978-1982 ; Medaglia 1982-1996 — *apparat de Wilson* : Medaglia, papyrus
- **v. 247** : Taillardat 1988
- **vv. 247-248** : Austin 1990
- **v. 256** : *apparat de Wilson* : van Leeuwen, σκέλει
- **v. 261** : Austin 1987, p. 76 — *interprétation* : Perusino 2002, ἔγκυκλον
- **v. 263** : Willems 1908
- **vv. 273-288** : Koster 1955
- **vv. 275-279** : Maas 1913, ἔκσπευδε
- **vv. 276-279** : *attribution* : Melandri 2004, coronis de PSI 1194, attribution
- **v. 277** : *apparat de Wilson* : Maas, ἔα· σπεῦδε
- **vv. 277-294** : Marzullo 1984-1985
- **vv. 280-281** : Austin 1990 ; Coulon 1934a ; Willems 1908
- **v. 282** : *apparat de Wilson* : Hall & Geldart, περικαλλεῖ ; Kaibel, περικαλλεῖ
- **v. 285** : Coulon 1953
- **v. 287** : Austin 1987, p. 76
- **v. 288** : Olson 1995
- **v. 289** : Austin 1990 ; Taillardat 1988
- **vv. 289-291** : Willems 1908
- **v. 291** : Taillardat 1961
- **v. 295** : Liberman 2008, conjecture d'Austin–Olson ; Residori 1979 ; Wilamowitz 1929, « Lesefrüchte », p. 468-469, d'après S. — *apparat de Wilson* : Austin & Olson, attribution ; Sommerstein, attribution
- **vv. 295-382** : Notsu 1995
- **v. 306** : *apparat de Wilson* : van Leeuwen, καὶ
- **v. 307** : Austin 1987, p. 76
- **v. 314** : Olson 1995, R défendu
- **v. 324** : *apparat de Wilson* : Wilamowitz, ἰχθυόεντα
- **v. 325** : Austin 1987, p. 77
- **vv. 325-326** : Austin 1990
- **v. 326** : *apparat de Wilson* : Austin, ὀρίπλαγκτοι
- **v. 337** : Austin 1987, p. 77
- **vv. 339-340** : *interprétation* : Gardner 1989, enfants supposés
- **v. 344** : Austin 1987, p. 77
- **v. 345** : *interprétation* : Henderson 1987, la « veuve joyeuse »
- **v. 347** : Austin 1987, p. 77
- **v. 352** : Austin 1987, p. 77
- **vv. 352-354** : Willems 1908
- **vv. 352-371** : Prato 1993-1999
- **v. 354** : *apparat de Wilson* : Willems, ἀποτελεῖσθαι
- **vv. 356-367** : *interprétation* : Macía Aparicio 2002, date
- **v. 357** : Austin 1987, p. 77
- **v. 365** : Austin 1987, p. 77
- **vv. 365-366** : Blanc–Taillardat 1986 ; Storey 2006, obèles d'AO — *apparat de Wilson* : Austin, τῆς ἀρχῆς; τῶν κερδῶν
- **vv. 365-367** : Willems 1908
- **vv. 365-369** : Austin 1990
- **v. 369** : Thomsen 1988
- **v. 373** : Storey 2006, Archikleia, d'après Satyros
- **v. 380** : *apparat de Wilson* : Sommerstein, attribution
- **v. 386** : *interprétation* : Henderson 1991, femmes au théâtre
- **v. 387** : *interprétation* : Olson 2006
- **v. 392** : Austin 1987, p. 78
- **v. 394** : Austin 1987, p. 78
- **v. 400** : Austin 1987, p. 78 — *apparat de Wilson* : Austin, ⟨δή⟩ τις
- **vv. 400-401** : Willems 1908
- **v. 406** : Méndez Dosuna 2016b
- **vv. 418-420** : Willems 1908
- **v. 437** : *apparat de Wilson* : Austin, πάντα δ' εἶδ' ἐξήτασέν τε
- **v. 443** : Austin 1987, p. 78
- **vv. 443-458** : *interprétation* : Olson 2006
- **v. 449** : Austin 1987, p. 79
- **vv. 450-451** : Box 1964 — *interprétation* : Lefkowitz 1989
- **vv. 450-452** : Coulon 1929
- **v. 460** : Coulon 1929
- **vv. 466-519** : *interprétation* : Giacomoni 1999 ; Heath 1987a
- **v. 467** : Austin 1987, p. 79
- **v. 474** : Austin 1987, p. 79
- **v. 476** : Olson 1995
- **v. 488** : Austin 1987, p. 79
- **vv. 493-496** : Seager 1983
- **v. 495** : Austin 1987, p. 79
- **vv. 497-501** : Cowan 2008
- **vv. 499-501** : Marzullo 1975-1977 ; Willems 1908
- **v. 500** : Austin 1975 ; Austin 1987, p. 79 ; Olson 1995 — *apparat de Wilson* : Austin, εὖ κεκαλυμμένον
- **v. 501** : Austin 1987, p. 79
- **vv. 502-516** : *interprétation* : J. Vickers 2019
- **vv. 509-510** : Willems 1908
- **v. 512** : Austin 1987, p. 80
- **vv. 514-516** : *interprétation* : J. Vickers 2019, le « lion », enfant supposé
- **vv. 517-530** : Nicolosi 2023
- **vv. 531-532** : Willems 1908 — *interprétation* : Miller 1947, *Mélanippe captive*
- **v. 532** : Olson 1995, R défendu
- **v. 533** : Austin 1987, p. 80
- **v. 537** : Austin 1987, p. 80
- **v. 545** : Austin 1987, p. 80
- **vv. 547-548** : *interprétation* : Blanchard 2001, Mélanippe, Phèdre, Pénélope
- **v. 557** : Olson 1995 ; Storey 2006, οἶνον
- **vv. 561-562** : *interprétation* : Olson 2006
- **v. 569** : Austin 1990 ; Willems 1908 — *apparat de Wilson* : Willems, πρόσθιγε
- **v. 574** : *interprétation* : Olson 1992, Clisthène, p. 316-318
- **vv. 575-576** : Willems 1908
- **v. 580** : Austin 1987, p. 80
- **v. 581** : Olson 1995
- **vv. 592-593** : Willems 1908
- **v. 594** : Austin 1987, p. 80
- **v. 596** : Austin 1987, p. 80
- **vv. 601-605** : Maas 1913, transposition du v. 604 avant 603
- **v. 604** : *apparat de Wilson* : Maas, ζητητέον τἄρ' ἐστί; transposition ; Wilson, transposition
- **v. 605** : *interprétation* : Storey 1989, Kléonymos
- **vv. 624-625** : Boccaccini 2012
- **v. 632** : Austin 1987, p. 80 — *apparat de Wilson* : Austin, τρίτον δὲ τί;
- **v. 638** : Degani 1996 — *apparat de Wilson* : Degani, attribution
- **v. 642** : *apparat de Wilson* : van Leeuwen, νυνδὴ δὲ
- **v. 646** : Liberman 2008, texte et apparat de Wilson
- **v. 653** : Austin 1987, p. 80
- **vv. 655-686** : Willems 1908
- **v. 656** : Willems 1908
- **vv. 656-658** : *interprétation* : Broneer 1942, Thesmophorion, d'après S. ; Thompson 1936, Pnyx et Thesmophorion, d'après S.
- **v. 657** : Austin 1987, p. 80 — *apparat de Wilson* : Handley, ἐπελήλυθε
- **v. 658** : Austin 1987, p. 81
- **v. 662** : Austin 1987, p. 81 ; Melandri 2004 — *apparat de Wilson* : Austin, ⟨μ'⟩
- **vv. 663-664** : Austin 1990
- **v. 666** : Austin 1987, p. 81 — *apparat de Wilson* : Kaibel, ⟨καὶ τὰ κεῖσε⟩
- **v. 676** : *mètre* : Di Virgilio 2026
- **v. 679** : *apparat de Wilson* : Richards, τούτων
- **v. 682** : Austin 1987, p. 81
- **vv. 689-758** : *interprétation* : Heath 1987a ; Rehm 1988
- **vv. 689-759** : Capra 2013 — *interprétation* : Csapo 1986, cratère de Würzburg ; Taplin 1987, cratère de Würzburg
- **vv. 689-764** : *interprétation* : Romani 2006
- **vv. 696-697** : Austin 1990
- **vv. 699-725** : *mètre* : Di Virgilio 2026
- **vv. 702-703** : Austin 1990
- **v. 706** : Austin 1987, p. 81 ; Coulon 1934a
- **v. 710** : Gannon 1982-1988
- **vv. 710-712** : Willems 1908
- **vv. 710-713** : Austin 1990
- **vv. 721-725** : Austin 1990 ; Taillardat 1988
- **v. 729** : *apparat de Wilson* : Sommerstein, ἦ 'γώ
- **v. 736** : *apparat de Wilson* : Wilson, ἀεὶ
- **v. 741** : Austin 1987, p. 81
- **vv. 754-757** : *interprétation* : Seager 1981, jeu de scène de l'outre
- **v. 758** : *apparat de Wilson* : Austin & Olson, ἱερέας
- **v. 759** : *apparat de Wilson* : Austin & Olson, ἱερέας
- **v. 768** : Austin 1987, p. 81
- **v. 771** : Austin 1987, p. 82
- **v. 772** : *apparat de Wilson* : Austin, ⟨φέρε⟩ ; Sandbach, ⟨πλάται;⟩ placé avant πόθεν
- **v. 773** : Austin 1987, p. 82
- **vv. 773-774** : Willems 1908
- **v. 776** : Austin 1987, p. 82
- **v. 783** : Austin 1987, p. 82
- **v. 784** : Austin 1987, p. 83
- **v. 789** : Austin 1987, p. 83
- **v. 794** : Olson 1995, R défendu — *apparat de Wilson* : Richards, οἴκοθεν
- **v. 795** : *apparat de Wilson* : Richards, ἀλλήλων; ἀλλοτρίῳ
- **v. 797** : Austin 1987, p. 83
- **v. 802** : *apparat de Wilson* : Richards, καθ'
- **v. 804** : Austin 1987, p. 83
- **v. 805** : Austin 1987, p. 83
- **v. 806** : Coulon 1953
- **vv. 808-809** : Maas 1913, Ἄνυτος pour αὐτός ; Willems 1908 — *interprétation* : Sommerstein 1977, date, probouloi
- **v. 809** : Melandri 2004 ; Olson 1995, Ἄνυτος ; Storey 2006, Ἄνυτος — *apparat de Wilson* : Maas, Ἄνυτος
- **vv. 811-812** : Willems 1908
- **v. 813** : Tammaro 1975-1977
- **v. 815** : Austin 1987, p. 83
- **v. 819** : *apparat de Wilson* : Denniston, δή που
- **v. 825** : Austin 1987, p. 83
- **v. 839** : Austin 1987, p. 83
- **v. 840** : *interprétation* : Brun 1987, Hyperbolos ; Macía Aparicio 2002, date
- **v. 842** : Austin 1987, p. 83
- **vv. 846-928** : *interprétation* : Bierl 2020 ; Esteban Santos 2016 ; Nieddu 2004
- **vv. 850-928** : Palerm 2014
- **v. 852** : Austin 1987, p. 83
- **vv. 855-857** : Campbell 1949
- **v. 860** : Austin 1987, p. 83
- **v. 875** : Melandri 2004
- **v. 887** : *apparat de Wilson* : Denniston, κακῶς γ' ἄρ' ; Lowe, κακῶς γὰρ ; van Leeuwen, κάκιστ' ἄρ'
- **v. 889** : Austin 1987, p. 83
- **v. 891** : *apparat de Wilson* : van Leeuwen, συμμεῖξαι
- **v. 902** : Austin 1990, p. 27
- **vv. 909-910** : Méndez Dosuna 2016a
- **v. 910** : Austin 1990 ; Grégoire 1938 ; Hartwig 2008 ; Storey 2006, ἀμφίων de Grégoire, ἱστίων d'Austin 1990 ; Tammaro 2022 — *apparat de Wilson* : Austin, ἱστίων
- **vv. 913-914** : *mètre* : Di Virgilio 2026
- **vv. 923-944** : *attribution* : Storey 2006, quatrième acteur
- **vv. 930-932** : Melandri 2004
- **vv. 941-945** : Coulon 1934a
- **v. 942** : Hartwig 2009
- **v. 943** : Austin 1987, p. 83
- **v. 945** : Austin 1987, p. 83
- **v. 947** : Austin 1987, p. 84
- **vv. 947-1000** : Thomsen 1973
- **v. 952** : Austin 1987, p. 84
- **v. 956** : *apparat de Wilson* : Austin, πᾶσ' ὕπαγε
- **v. 966** : Austin 1987, p. 84
- **v. 967** : Austin 1987, p. 84 — *apparat de Wilson* : Austin, ὡς πρὸς
- **vv. 967-968** : Thomsen 1973
- **v. 968** : Austin 1987, p. 84
- **v. 982** : Bierl 1999 ; Hartwig 2008 — *apparat de Wilson* : Sommerstein, χαρᾷ avec πόδας pour διπλῆν
- **vv. 982-995** : Austin 1990
- **v. 984** : Hartwig 2008
- **v. 986** : Wycherley 1959
- **v. 989** : *apparat de Wilson* : Sommerstein, σε
- **v. 994** : *apparat de Wilson* : Austin, ⟨ἡδόμενος⟩
- **v. 995** : Austin 1987, p. 85 ; Coulon 1953 — *apparat de Wilson* : Wilamowitz, συγκτυπεῖται
- **v. 1001** : Austin 1987, p. 85
- **vv. 1001-1225** : *interprétation* : Brixhe 1988
- **v. 1005** : Austin 1987, p. 85 ; Hall 1989, μᾶλλο pour μᾶλλον
- **vv. 1009-1135** : *interprétation* : Bierl 2020
- **v. 1011** : Austin 1987, p. 85
- **v. 1013** : Austin 1987, p. 85 ; Olson 1995 — *apparat de Wilson* : Sommerstein, ⟨ἤδη⟩
- **v. 1014** : Liberman 2008, ἥκει, déjà chez Bothe
- **v. 1015** : Hose 1986-1987
- **vv. 1015-1055** : Coulon 1957 ; Mitsdörffer 1954, reconstruction de la monodie — *mètre* : Di Virgilio 2026 ; Lourenço 2000 — *interprétation* : Di Virgilio 2019 ; Mitsdörffer 1954
- **v. 1017** : Austin 1987, p. 85
- **vv. 1018-1019** : Austin 1990
- **vv. 1018-1021** : *attribution* : Melandri 2004, Écho-Euripide
- **v. 1019** : Thomsen 1988 — *apparat de Wilson* : Sommerstein, ἀϋταῖς
- **vv. 1019-1020** : Willems 1908
- **v. 1026** : *apparat de Wilson* : Austin, ⟨δὴ⟩
- **v. 1028** : *apparat de Wilson* : Austin, ἐφέστηκε κῶλοον
- **v. 1030** : Coulon 1934a
- **v. 1034** : Austin 1987, p. 85
- **v. 1041** : Austin 1987, p. 85 — *apparat de Wilson* : Rau, χέουσα
- **v. 1047** : Austin 1987, p. 85 ; Coulon 1930, 1931 ; Coulon 1957 ; Wilamowitz 1929, ἂν ἔτικτε pour l'ἀνέτικτε de R, *Hermes* 64, p. 467, d'après Coulon 1957
- **vv. 1050-1051** : Austin 1990 ; Willems 1908
- **v. 1051** : Thomsen 1988
- **v. 1052** : Austin 1987, p. 85
- **vv. 1052-1055** : Willems 1908
- **vv. 1054-1055** : Méndez Dosuna 2010
- **vv. 1056-1073** : *attribution* : Melandri 2004, Écho-Euripide
- **vv. 1056-1097** : *interprétation* : Melzer 2022 ; Mureddu 1987
- **v. 1061** : Austin 1987, p. 85 — *apparat de Wilson* : Richards, καὐτῷ
- **v. 1070** : Austin 1987, p. 85
- **v. 1085** : *apparat de Wilson* : Coulon, τί bis
- **v. 1086** : Austin 1987, p. 85
- **v. 1088** : *apparat de Wilson* : Austin, κλαῦσ' ἔτι ; Rogers, κλαύσαι
- **v. 1101** : Austin 1987, p. 85
- **v. 1109** : *apparat de Wilson* : Kaibel, λαλῆς
- **v. 1114** : Austin 1987, p. 86 ; Olson 1995 — *apparat de Wilson* : Sommerstein, σῦκο
- **v. 1115** : Austin 1987, p. 86
- **v. 1119** : Austin 1987, p. 86
- **v. 1124** : Austin 1987, p. 86
- **v. 1129** : Austin 1987, p. 86
- **v. 1132** : Austin 1987, p. 86
- **v. 1133** : Austin 1987, p. 86
- **vv. 1136-1159** : *mètre* : Di Virgilio 2026
- **vv. 1150-1151** : *apparat de Wilson* : Austin, note
- **v. 1157** : *apparat de Wilson* : van Leeuwen, εἰ
- **vv. 1160-1226** : *interprétation* : Gelzer 1993, scène finale : Th. Gelzer, Entretiens Hardt 38, 1993, p. 84, d'après S.
- **vv. 1160-1231** : Di Bari 2010, 2013 — *interprétation* : Totaro 2022
- **v. 1170** : Coulon 1937
- **vv. 1172-1177** : Melandri 2004
- **v. 1174** : Moreau 1938
- **v. 1181** : Austin 1987, p. 86 ; Willems 1908 — *apparat de Wilson* : Maas, ἀνῶμεν
- **v. 1187** : Dover 1977, 1187b, parépigraphe ancienne ; Hartwig 2008 — *apparat de Wilson* : Austin, κλαῦσ' ἔτ'
- **v. 1197** : Olson 1995
- **v. 1198** : Austin 1987, p. 86
- **v. 1203** : Olson 1995, R défendu
- **vv. 1210-1211** : Hartwig 2009b
- **v. 1214** : Gannon 1982-1988 — *apparat de Wilson* : Austin, ὀ γραῦς με διέβαλ' ; Gannon, ἐπίτρεκ'
- **v. 1215** : Hall 1989, συβίνη de Brunck, jeu sur καταβινεῖν ; Olson 1995 — *apparat de Wilson* : Austin, συβήνη δ' ἦν ; Sommerstein, κατεβείνησι
- **v. 1224** : Coulon 1934a
- **v. 1226** : Austin 1990 ; Jackson 1955, κατ' αὐτοὺς ἐς — *apparat de Wilson* : Jackson, κατ' αὐτοὺς
- **v. 1231** : Austin 1987, p. 86

## 5. Accès libres téléchargés (`.sources/web/etudes/`)

Fichiers téléchargés pour cette recension (non versionnés ; manifeste avec taille, empreinte SHA-256 tronquée, URL
et date : `.sources/web/etudes/MANIFESTE.tsv`). Les copies du Drive (`AR/`, `TH/`, `EU/`, `DR/`) et les éditions
anciennes (`ED/`, `ME/`) sont décrites dans `recherche/drive_ressources.md` et `recherche/bibliographie_editions.md`.

| Fichier | Notice | Taille | Source |
|---|---|---:|---|
| `Maas_1913_RhM68_Zu_Ar_Thesm.pdf` | Maas 1913 | 1154 Kio | journals.ub.uni-koeln.de |
| `Coulon_1957_RhM100_Thesm_1015-1055.pdf` | Coulon 1957 | 2566 Kio | journals.ub.uni-koeln.de |
| `JVickers_2019_RhM162_Lion_Cub_Ainos.pdf` | J. Vickers 2019 | 804 Kio | journals.ub.uni-koeln.de |
| `Habash_1997_GRBS38_Odd_Thesmophoria.pdf` | Habash 1997 | 1024 Kio | grbs.library.duke.edu |
| `Nieddu_2004_GRBS44_Parody_of_Helen.pdf` | Nieddu 2004 | 151 Kio | grbs.library.duke.edu |
| `Sissa_2012_EuGeStA2_Agathon.pdf` | Sissa 2012 | 1443 Kio | www.peren-revues.fr |
| `Carbon_2006_cr_Austin-Olson.pdf` | Carbon 2006 (c. r. AO) | 80 Kio | orbi.uliege.be |
| `Lech_2024_Aigis_cr_Austin-Olson.pdf` | Lech 2005 (c. r. AO, mis en ligne en 2024) | 112 Kio | tidsskrift.dk |
| `Stepantsov_2022_StudLitt7_vv134-140.pdf` | Stepantsov 2022 | 239 Kio | doi.org |
| `Stepantsov_2024_Izvestija83_proverbe_debut.pdf` | Stepantsov 2024 | 151 Kio | journals.rcsi.science |
| `Boccaccini_2012_Thesm_624.pdf` | Boccaccini 2012 | 1316 Kio | annali.unife.it |
| `Abramovich_2026_IELCP30_schol_v80.pdf` | Abramovich 2026 | 630 Kio | doi.org |
| `DiVirgilio_2026_docmio_Thesm.pdf` | Di Virgilio 2026 (volume entier) | 1999 Kio | press.uniurb.it |
| `Scharffenberger_2025_didaskalia_846-1159.html` | Scharffenberger 2024 (page HTML) | 45 Kio | doi.org |
| `SaettaCottone_2007_Argos31_Penteo.pdf` | Saetta Cottone 2007 | 1558 Kio | bibliotecavirtual.unl.edu.ar |
| `willems1908/Willems_1908_Notes_Thesm_Ploutos_BullAcadBelg.pdf` | Willems 1908 | 4726 Kio | dipot.ulb.ac.be |
| `cr_Prato2001_Prometheus30_2004.pdf` | Melandri 2004 (c. r. P.) | 153 Kio | oaj.fupress.net |
| `MendezDosuna_2016_SPhV18_Thesm406.pdf` | Méndez Dosuna 2016b | 309 Kio | dialnet.unirioja.es |
| `Cardoso_2020_NuntiusAntiquus15_rito_palco.pdf` | Cardoso 2020 | 325 Kio | periodicos.ufmg.br |
| `Drumond_2020_Dramaturgias13_heroi.pdf` | Drumond 2020 | 542 Kio | periodicos.unb.br |
| `Schoene_1847_RhM5_Zu_Ar_Thesm.pdf` | Schöne 1847 | 430 Kio | journals.ub.uni-koeln.de |
| `Ritschl_1862_RhM17_Zu_Ar_Thesm.pdf` | Ritschl 1862 | 700 Kio | journals.ub.uni-koeln.de |
| `Anonyme_1863_RhM18_Zu_Ar_Thesm.pdf` | Anonyme 1863 | 203 Kio | journals.ub.uni-koeln.de |
| `Ritschl_1867_RhM22_Zu_Ar_Thesm.pdf` | Ritschl 1867 | 186 Kio | journals.ub.uni-koeln.de |
| `Hartwig_2009_RhM152_polos_1210-1211.pdf` | Hartwig 2009b | 46 Kio | journals.ub.uni-koeln.de |
| `hermes8/hermeswies08wies_djvu.txt` (+ métadonnées) | Hiller 1874 (*Hermes* 8, OCR du volume) | 1269 Kio | archive.org |

26 documents. Accès libres repérés mais non téléchargés (défi anti-robot, certificat invalide ou serveur
injoignable) : Persée (Coulon 1926-1953, Blanc–Taillardat, Saetta Cottone 2003, Blanchard 2001, Plassart 1913),
OpenEdition (Germain 2023 ; Saetta Cottone 2010 ; Trümpy 2004), HAL (Germain 2021, hal-03355961), *Emerita*
(Macía Aparicio 2002, Quijada Sagredo 2012), RODERIC Valence (Mastromarco 2016, Navarro Martínez 2013, Boscà
Cuquerella 2017), *Humanitas* (Lourenço), OpenstarTs (Nieddu 2010), IKEE (Kyriakou 2013), *Elephant & Castle*
(Volpi 2024), *ICS* (Ruffell 2020), dépôt du Nebraska (Duncan 2001), *Temenos* (Prytz Johansen 1975), *BMCR*
(comptes rendus lus en ligne).

## 6. Lacunes et vérifications à faire

*Références incomplètes (marquées [à vérifier], [à relever] ou [à identifier] dans les notices)*

- Vers discutés à relever : Austin 2002 (« Seven *cruces* », *QUCC* 72), Coulon 1930 et 1931 (hors v. 1047), Allen
  1935, Coulon-Tauber 1943, Fraenkel 1962 (chapitres sur les *Thesm.*), Kamerbeek 1967 (hors v. 18), Austin 1974,
  notes de Prato 1993-1999, Schöne 1847, Clements 2013, Rau 1967 (pages des *Thesm.*).
- Titres ou supports à établir : Dover 1977 (*ICS* 2), Brixhe 1988, Rehm 1988, Chirico 1989, West 1992 (*ZPE* 92),
  Webster 1965 (*BICS* 12 ou Suppl.), Brizi 1928 (« *AR* »), Luce 1918 (scène représentée), Todisco 2012 et 2017,
  Capra 2013, Romani 2006, Palerm 2014, Esteban Santos 2016, Méndez Dosuna 2010, Navarro Martínez 2013, Boscà
  Cuquerella 2017, Di Virgilio 2018 et 2019, Saetta Cottone 2023, Sells 2019 (auteur), éditeurs de *Der Chor im
  antiken und modernen Drama* (Bierl 1999) et de *Chorodidaskalia* (Tammaro 2022), Lourenço (*Humanitas* 47 :
  année), Torchio 1999-2000 (titres), réplique de Butrica à Olson–Austin (*LICS*), Grégoire 1938 (support : *RBPh*
  ou *Byzantion* ?), tomaison de Sommerstein 1980 (*QS*) et de Lowe 1967 (*Hermes* 95).
- Divergences de date ou de pagination entre bibliographies : Mureddu, scène d'Écho (*AFLC* 6 : 1985 chez S., 1987
  chez P.) ; Coulon-Tauber (1942 chez P., 1943 chez l'éditeur) ; Austin, « Le rôle de la coryphée » (*Dioniso* 45,
  1971-1974).

*Documents à lire ou à récupérer*

- À lire en priorité pour l'apparat et le commentaire : Rau 1967 (parodies), Wilson 2007b (*Aristophanea*, absent du
  Drive), Austin 2002 et 2011, Degani 1996 (le fichier du Drive ne contient pas la note), Kamerbeek 1967, Thomsen
  1973 et 1988, Medaglia 1982-1996, Marzullo (*MCr*), Prato 1993-1999, Mitsdörffer 1954, Hall 2006, Farmer 2017
  (ch. 4), Bierl 2001 et 2020, Major 2013, Melzer 2022.
- Bobrick 1991 : le fichier du Drive (`TH/IPHIGENEIA REVISITED*.pdf`) est une image sans couche texte ; à océriser
  (tesseract, anglais) avant lecture.
- Ouvrages signalés comme non récupérés du Drive (`recherche/drive_ressources.md` § 9.2) : Bobrick 1997, Bowie 1993 ;
  absents du fonds : Zeitlin 1981/1996, Taaffe 1993, Tzanetou 2002, Stehle 2002 (accès par JSTOR, Project MUSE).
- Accès libres non téléchargés (défis anti-robot, certificats) : voir la fin du § 5.

*Fichiers du Drive examinés et écartés (hors sujet ou mal intitulés)*

- `AR/v 249 Taillardat Collectanea_Philologica*.pdf` : J. Taillardat, « Une ambiguïté voulue : *pompholugopaphlasmata*
  (Aristophane, *Ranae*, v. 249) », *Collectanea Philologica* 2 (Łódź, 1995), p. 253-258 — porte sur les
  *Grenouilles*, non sur les *Thesm.*
- `AR/thesmophories 1-176.pdf` : I. Fletcher, « Aristophanes' *Thesmophoriazusae* (1-176) », *Arion* 2.3 (1963),
  p. 78-85 — traduction anglaise en vers, non une étude (à ranger avec les traductions).
- `TH/Aristophanes_THESMOPORIAZUSAE_a_translat.pdf` : traduction de T. L. Pangle (sans date) ; `Grec/283556.pdf` :
  H. W. Miller, « A Note on ὁ κωμικός in Eustathius », *TAPhA* 73 (1942), p. 353-357 (tradition indirecte, à
  verser au dossier des testimonia) ; `Grec/RCR_*.pdf` : H. Bornecque, *Précis de prosodie et métrique grecque et
  latine*, Paris, 1933.

*Critiques nommés dans la commande et non trouvés pour les* Thesm.

- Aucune note propre aux *Thesmophories* de J. Diggle, C. W. Willink, D. Kovacs ni N. Dunbar (hors son compte rendu
  de S., *JHS* 116, 1996) n'a été repérée dans les bibliographies d'AO, de S. et de P., dans OpenAlex ni dans
  Crossref ; leurs conjectures éventuelles sont à chercher dans l'apparat de Wilson (aucune occurrence de leurs noms
  dans le répertoire critique du dépôt) et dans *Aristophanea*. J. Gibert a relu l'introduction et le commentaire
  d'AO (AO, p. x) ; aucune étude de lui sur la pièce n'a été trouvée. P. Sfyroeras : seulement l'article sur
  l'*Andromède* dans les *Grenouilles* (§ 2.4).

*Travaux de l'auteur de la présente édition*

- Ses notes sur les *Thesmophories* (articles de *Λύχνος*, 2020-2022 ; article de *Kentron*, 2023, sur l'encycle ;
  dossier « Mnésiloque » de l'introduction) sont recensées dans `recherche/drive_ressources.md` § 8.2 et
  `recherche/travaux_anterieurs.md` ; leurs vers ne sont pas repris dans l'index du § 4.

*Suites possibles*

- Compléter l'index du § 4 par les lemmes des commentaires d'AO, de S. et de P. (renvois aux études par vers), et par
  les pages d'Austin 1990 (repérées seulement pour les vv. 2, 60-62, 138, 902).
- Contrôler le relevé automatique d'Austin 1987 sur le PDF (quelques lemmes peuvent manquer).
