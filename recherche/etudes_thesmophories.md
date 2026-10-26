# Études modernes sur les *Thesmophories* — recension

> **État** (26 octobre 2026) : rédaction en cours, par sections ; ce qui n'a pas pu être contrôlé sur le
> document lui-même est marqué **[à vérifier]**. Les éditions et commentaires sont recensés dans
> `recherche/bibliographie_editions.md`, les sources des conjectures des critiques des XVIe-XIXe s. dans
> `recherche/conjectures_sources.md`, les papyrus dans `recherche/papyrus.md`, la métrique dans
> `recherche/metrique_structure.md`, les ressources du Drive dans `recherche/drive_ressources.md` : on n'y
> revient ici que par renvoi.

## Plan

0. Conventions, sources de la recension, accès
1. Critique textuelle
   1.1 Études d'ensemble, comptes rendus d'éditions
   1.2 Critiques des XVIIIe-XIXe s. et premiers XXe s. (renvois)
   1.3 Notes et articles sur des passages précis (ordre chronologique)
   1.4 Attribution des répliques ; le nom du parent d'Euripide (Mnésiloque ou Kèdestès)
   1.5 Papyrus, scholies, tradition (renvois)
2. Interprétation, mise en scène, contexte
3. Iconographie
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
| U. von Wilamowitz-Moellendorff | « Die Zeit der *Thesmophoriazusen* », *Aristoteles und Athen* II (1893), p. 343-355 ; *Griechische Verskunst* (1921) ; « Lesefrüchte », *Hermes* 64 (1929), p. 468-469 (S., au v. 295) ; *Kleine Schriften* IV (1962), p. 484-488 (P.) [contenu à identifier] ; suggestions orales du séminaire « Graeca » (fin des années 1920) transmises par les notes de P. Maas (Austin 1987 ; Sansone 1987, p. 226 n. 15 : ἀπὸ γνώμης au v. 148) | `ME/wilamowitz1893_AuA2`, `ME/griechischeversk00wila` |

### 1.3 Notes et articles sur des passages précis (ordre chronologique)

**1900-1959**

- **Willems 1908** — A. Willems, « Notes sur les *Thesmophories* et le *Ploutos* d'Aristophane », *Bulletins
  de l'Académie royale de Belgique* (Classe des lettres), n° 11 (novembre 1908), p. 625-693 (tiré à part
  paginé 3-71) = *Aristophane. Traduction avec notes et commentaires critiques*, Paris-Bruxelles, 1919,
  t. II, p. 535-579. Vingt-huit notes, presque toujours pour défendre R contre les corrections. *Vers* :
  16-18, 21, 22-24, 60, 217, 230, 263, 280-281, 289-291, 352-354, 365-367, 400-401, 418-420, 499-501,
  509-510, 531-532, 569, 575-576, 592-593, 655-686 (chœur), 656, 710-712, 773-774, 808-809, 811-812,
  1019-1020, 1050-1051, 1052-1055, 1181. *Accès* : tiré à part, `W/willems1908/Willems_1908_Notes_Thesm_Ploutos_BullAcadBelg.pdf`
  (domaine public, dépôt de l'ULB) ; texte repris dans les annexes de l'auteur (`latex/Aristophane-Thesmo
  Annexes.tex`, cf. `recherche/travaux_anterieurs.md` § 9.2). [lu]
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
  et Anacréon », *REG* 44 (1931), p. 8-33, DOI 10.3406/reg.1931.6999. *Vers* : [à relever]. *Accès* : libre
  (Persée). [méta]
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
  p. 454-458 selon P.). Chant d'Agathon. *Vers* : 126-129, 1170. *Accès* : `AR/Coulon notes criti et ex chant
  agathon Nietsche.pdf` ; libre (Persée), DOI 10.3406/reg.1937.8180. [lu]
- **Gordziejew 1937** — W. Gordziejew, « De prologo *Thesmophoriazusarum* », *Eos* 38 (1937), p. 296-324.
  *Vers* : 1-294. *Accès* : — [AO] [P]
- **Moreau 1938** — J. Moreau, « Note sur le vers 1174 des *Thesmophories* d'Aristophane », *AC* 7 (1938),
  p. 227-231. *Vers* : 1174. *Accès* : libre (Persée), DOI 10.3406/antiq.1938.3169. [méta]
- **Grégoire 1938** — H. Grégoire, « De l'utilité du grec moderne », *Byzantion* 13 (1938), p. 396-399 :
  ἐκ τῶν ἀμφίων au v. 910 (d'après Storey 2006, qui regrette qu'AO ne l'aient pas discutée). *Vers* : 910.
  *Accès* : — [P] [CR] [à vérifier : Crossref ne connaît, de Grégoire en 1938, que « Utilité et charme du grec
  moderne », *RBPh* 17 (1938), p. 5-26]
- **Goossens 1941** — R. Goossens, « Notes sur quelques papyrus littéraires », *Chronique d'Égypte* 16
  (n° 31, janvier 1941) : I. *Thesm.* 242 (PSI 1194). *Vers* : 242. *Accès* : `DR/papyrus/Notes sur quelques
  papyrus littéraires PSI1194 Thesmophories.pdf`. [lu, d'après `recherche/drive_ressources.md` § 3.3]
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
  de coronide ; de parepigrapha ; de proceleusmatico », *Acme* 8 (1955), p. 93-103. *Vers* : passages de PSI
  1194 (coronis après le v. 276 ; cf. Melandri 2004). *Accès* : — [P]
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
  c. r. de K. J. Dover, « Notes on Aristophanes », *CR* n.s. 13 (1963), p. 272-274 (`AR/Notes Dover sur
  Fraenkel*.pdf`). *Vers* : [chapitres sur les *Thesm.* à relever]. [AO] [lu pour Dover]
- **Box 1964** — H. Box, « Aristophanes: *Birds* 785-96, and *Thesmophoriazusae* 450-1 », *CR* n.s. 14
  (1964), p. 241-242 : la plainte de la tresseuse de couronnes (« Euripide a persuadé les hommes que les dieux
  n'existent pas ») suppose des femmes au théâtre tragique. *Vers* : 450-451. *Accès* : `AR/thesmophories
  450.pdf`. [lu]
- **Marzullo 1964** — B. Marzullo, « Aristophanea (II). Osservazioni critiche sul testo di Aristofane », dans
  J. Irmscher *et al.* (éd.), *Miscellanea critica* I, Leipzig, 1964, p. 129-138. [P]
- **Kamerbeek 1967** — J. C. Kamerbeek, « Notes sur quelques passages des *Thesmophories* d'Aristophane », dans
  *Κωμῳδοτραγήματα. Studia Aristophanea viri Aristophanei W. J. W. Koster in honorem*, Amsterdam, 1967,
  p. 74-81. *Vers* : [à relever]. [P]
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
  Wilamowitz (n. 15). *Vers* : 148. *Accès* : `AR/Aristophanes_Thesmophoriazusae_148.pdf` (= `AR/thesmophories
  148.pdf`) ; DOI 10.1017/S0009838800031815. [lu]
- **Taillardat 1988** — J. Taillardat, communication résumée dans les « Actes de l'Association », *REG* 101
  (1988), p. IX-XXVIII (*Thesm.* p. XVI-XIX selon P.) : essai d'interprétation du texte transmis. *Vers* : 247,
  289, 721-725. *Accès* : `AR/reg_0035-2039_1988_num_101_482_1536.pdf`. [lu, d'après
  `recherche/drive_ressources.md`]
- **Thomsen 1988** — O. Thomsen, « Drei Emendationen zu den *Thesmophoriazusen* des Aristophanes : 369, 1019,
  1051 », *C&M* 39 (1988), p. 15-18. *Vers* : 369, 1019, 1051. [P]
- **Viketos 1989** — E. Viketos, « Aristophanes, *Thesmophoriazusae* 148-152 », *Hermes* 117 (1989), p. 359 :
  ἐμῇ γνώμῃ pour ἅμα γνώμῃ (ἅμα venu de δράματα au v. 150). *Vers* : 148. *Accès* : `AR/Thesmophories 148-152
  4476703.pdf`. [lu]
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
  (Ar. *Thesm.* 982) aus einer performativen Perspektive », Stuttgart-Weimar, Metzler, 1999 [volume à
  identifier]. *Vers* : 982. [méta]

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
  (contre AO) et ἑστιῶν, en fin de vers, fait du Parent exposé l'« hôte » qui régale les corbeaux. *Vers* : 942. *Accès* : `AR/thesmophories
  942 10.2307@27736297.pdf` ; DOI 10.1163/156852508X252920. [lu]
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
  *Ilíada* 8.168 y Aristófanes, *Tesmoforiantes* 406 », p. 229-240 [publication à identifier]. *Vers* : 406.
  [méta]
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
  *Pallas* 38 (1992), p. 289-300 : méthode (paragraphoi, sigles, logique dramatique). *Accès* : `AR/Problèmes de
  distribution et d'attribution des répliques chez Aristophane.pdf`. [lu, d'après `recherche/drive_ressources.md`]
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
  (p. 12-27). *Vers* : surtout 1-294 ; index des passages p. 221-223. *Accès* : `AR/Aristophanes
  Thesmophoriazusae  philosophizing theatre*.pdf` ; DOI 10.1017/CBO9781139629386. [lu, table des matières]
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
  p. IX-XXVI : l'outre « sacrifiée » (vv. 740 sqq.) et le sacrifice du porcelet. *Accès* : `TH/thesmophories 740
  sacrifice*.pdf`. [lu, d'après `recherche/drive_ressources.md`]
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

