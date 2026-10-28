# Éditions, commentaires et traductions des *Thesmophories* (1515–2026)

> État : **version de travail** (28 oct. 2026, troisième reprise : E18, E18b, E19, E25, E29b complétés et
> téléchargés, intégrité recontrôlée ; complétée au fil des vérifications).
> Chaque donnée a été lue sur l'exemplaire numérisé (page citée) ou sur une notice de catalogue (BnF,
> B3Kat), ou dans une bibliographie imprimée nommément citée ; « [à vérifier] » signale ce qui n'a pas pu
> être contrôlé. Compagnon : `recherche/conjectures_sources.md` (où trouver les conjectures des critiques).
> Pour les scholies, voir `recherche/scholies.md` ; pour le manuscrit, `recherche/ravennas_dossier.md`.

## Plan

1. Conventions et légende
2. Tableau chronologique des éditions (texte grec)
3. Notices détaillées
   1. De l'*editio princeps* à Ravestein (1516–1670)
   2. Le XVIIIᵉ siècle : Küster, Bergler, Brunck, Invernizi (1710–1794)
   3. Le XIXᵉ siècle (1810–1898)
   4. XXᵉ et XXIᵉ siècles (1901–2025)
   5. Éditions anciennes qui ne contiennent pas les *Thesmophories*
4. Commentaires séparés, notes *variorum*, scholies et travaux préparatoires
5. Traductions (par langue)
6. Contrôle d'intégrité des fichiers locaux
7. Manques, erreurs relevées et pistes

## 1. Conventions et légende

- **Fichiers locaux** : chemins relatifs à la racine du dépôt ; `ED/` = `.sources/web/editions/`
  (non versionné : documents téléchargés). « Drive » = Drive de l'auteur (`Mon Drive/Grec/Aristophane/…`),
  copié peu à peu dans `.sources/drive/fichiers/Grec/Aristophane/…` par le chantier « Drive » ; les
  extraits textuels déjà disponibles sont dans `.sources/drive/ravennas/` et `.sources/drive/editions/`.
- **Pages** : « PDF n » = rang de l'image dans le fichier local (1 = première image) ; « p. n » =
  pagination imprimée ; « f. » = foliotation. Pour les exemplaires numérisés à rebours (1542, 1548), le
  rang PDF décroît quand on avance dans le texte (« PDF 97→53 »).
- **Nature** : T = texte grec ; A = apparat ou notes critiques ; C = commentaire ; Sch = scholies ;
  Tr = traduction ; I = introduction développée.
- **Base manuscrite** : R = Ravenne, Classense 429 (seul témoin médiéval des *Thesm.*) ; G = Munich, BSB,
  Cod. graec. 492 (*Augustanus*, XVᵉ s., copie de R) ; Iunt. = l'*editio princeps* de 1516, imprimée sur R
  (Velsen 1871, p. 3–4) ; vulg. = la vulgate imprimée issue de la Juntine. « R (autopsie) » = l'éditeur a
  lui-même collationné R ; « R (d'après X) » = il dépend de la collation publiée par X.
- **DP** = domaine public (impression antérieure à 1900, ou auteurs et collaborateurs morts depuis plus de
  70 ans) ; « non » = sous droits : le fichier éventuel reste dans `.sources/` ou sur le Drive, jamais dans
  la partie versionnée du dépôt.
- **URL** : BSB = `https://www.digitale-sammlungen.de/view/<identifiant>` ; IA =
  `https://archive.org/details/<identifiant>` (les identifiants `bub_gb_X` sont des numérisations Google
  Books : `https://books.google.com/books?id=X`) ; BnF = notice `https://catalogue.bnf.fr/ark:/12148/<ark>`.
- **Sources des listes** : catalogues BnF (SRU) et B3Kat (SRU), requêtes conservées dans
  `.travail/editions_reprise/catalogues/` ; C. Prato, *Le donne alle Tesmoforie*, Milan, 2001, « Nota sul
  testo e sulle sue edizioni » (p. XXXI–XXXVI) et « Indicazioni bibliografiche », § 2 *Edizioni e commenti*
  et § 3 *Traduzioni* (p. XLIV–XLVII) (extrait textuel : `.sources/drive/ravennas/Prato_2001_LeDonneAlleTesmoforie_textrep.txt`) ;
  liste d'éditions de Blaydes 1880, p. VII–VIII.

## 2. Tableau chronologique des éditions (texte grec)

Les traductions seules sont au § 5, les commentaires et notes séparés au § 4. « — » : pas de fichier local.
Les références complètes, URL et justifications sont dans les notices du § 3 (renvoi par le numéro E…).

| N° | Date | Éditeur | Titre abrégé, lieu, imprimeur | Nature | Base ms. | DP | Fichier local | *Thesm.* dans le fichier |
|---|---|---|---|---|---|---|---|---|
| E01 | 1516 (28 janv.) | E. Boninus | *Cereris sacra celebrantes. Eiusdem Lysistrate*, Florence, B. Giunta (colophon « V kal. Febr. 1515 », style florentin) | T, *editio princeps* | R lui-même | oui | `ED/1515_Florence_Iunta_editio_princeps_Thesm_Lys/bsb10912207.pdf` | PDF 12–61 (non paginé) |
| E02 | 1532 | S. Grynaeus | *Comoediae undecim*, Bâle, A. Cratander et J. Bebel | T | vulg. | oui | `ED/1532_Bale_Cratander_Grynaeus/bsb00024026.pdf` | PDF 446–487 = p. 429–470 |
| E03 | 1538 | B. Zanetti | *Comoediae undecim*, Venise, B. Zanetti pour M. Sessa | T (Sch. pour 9 pièces) | vulg. | oui | `ED/1538_Venise_Zanetti/ARes70622.pdf` | PDF 468–512 |
| E04 | 1540 | (Chr. Wechel, impr.) | *Comoediae undecim*, Paris, Chr. Wechel (11 parties, in-4°) | T | vulg. | oui | `ED/1540_Paris_Wechel/bsb10150263_extraits_Thesm.pdf` (extrait) | PDF 5–53 = p. [469]–517 |
| E05 | 1542 | (Farreus) | *Comoediae undecim*, Venise, Farreus et fratres | T | vulg. (Zanetti) | oui | `ED/1542_Venise_Farreus/bub_gb_Wu5-_TQ_tCoC.pdf` | PDF 97→53 |
| E06 | 1544 | anonyme (« Grynaeus » des apparats) | *Comoediae undecim*, Francfort, P. Brubach | T | vulg. corrigée | oui | `ED/1544_Francfort_Brubach_Grynaeus/bsb10169310.pdf` | PDF 494–539 = f. 240v–263r |
| E07 | 1545 | G. Bourdin | *Τὰ τοῦ Αἰγιδίου Βουρδίνου σχόλια εἰς … Θεσμοφοριαζουσῶν κωμῳδίαν*, Paris, J. L. Tiletanus | T [à vérifier], Sch. humanistes | vulg. | oui | Drive (non encore copié) ; scholies réimprimées : `ED/1607_…`, `ED/1823_…` | — |
| E08 | 1547 | S. Gelenius (attr.) | *Comoediae novem … et duae sine commentariis*, Bâle, Froben | T | vulg. | oui | `ED/1547_Bale_Froben_Gelenius/bub_gb_NVBJxJmhIW8C.pdf` | PDF 546–574 = p. 512–540 |
| E09 | 1548 | A. Caninius (attr.) | *Comoediae undecim, multis metris corruptis … purgatae*, « Ioan. Gryphius excudebat » [Venise] | T | vulg. | oui | `ED/1548_Lyon_Gryphius/bub_gb_LBXPhhHGIUYC.pdf` | PDF 99→55 = f. 233v–255v |
| E10 | 1600 | Chr. Raphelengius | *Comoediae undecim*, Leyde, officina Plantiniana | T | vulg. | oui | `ED/1600_Leyde_Raphelengius/bub_gb_WuyoS4JxpT4C.pdf` | PDF 573–618 = p. 524–569 |
| E11 | 1607 | Aem. Portus, O. Biset | *Comoediae undecim cum scholiis antiquis … novi commentarii*, Genève, Caldoriana societas | T, Tr. lat., Sch. (Biset, Bourdin) | vulg. + corr. de Biset | oui | `ED/1607_Geneve_Portus_Biset/bub_gb_46Rraf1UeBIC.pdf` | PDF 830–910 = p. 760–813 |
| E12 | 1624 | (notes de J. Scaliger) | *Comoediae undecim, Graece et Latine … cum emendationibus … Iosephi Scaligeri*, Leyde, J. Maire | T, Tr. lat., A | vulg. | oui | Drive (« …Scaliger propre.pdf », non contrôlé) | — |
| E13 | 1670 | (J. Ravestein, impr.) | *Comoediae undecim, Graece et Latine … editio novissima*, Amsterdam | T, Tr. lat. (Divus), A | vulg. | oui | `ED/1670_Amsterdam_Ravestein_t2/bsb11088393.pdf` | PDF 70–143 = p. 750–823 ; notes PDF 248–251 = p. 928–931 |
| E14 | 1710 | L. Küster | *Comoediae undecim, Graece et Latine, ex codd. mss. emendatae*, Amsterdam, Th. Fritsch | T, Tr. lat., Sch., C | vulg. | oui | `ED/1710_Amsterdam_Kuster/kuster1710_extraits_Thesm.pdf` (extraits) | PDF 44–94 = p. 474–524 ; notes PDF 102–109 = p. 217–224 (2ᵉ pagin.) |
| E15 | 1760 | St. Bergler, P. Burman II | *Comoediae undecim, Graece et Latine*, Leyde, S. et J. Luchtmans, 2 vol. | T, Tr. lat., C | vulg. | oui | `ED/1760_Leyde_Bergler_Burman_t2/bub_gb_kRH7s1SMeIUC.pdf` | PDF 434–522 = p. [999]–1087 |
| E16 | 1781–1783 | R. F. Ph. Brunck | *Comoediae ex optimis exemplaribus emendatae*, Strasbourg, Treuttel | T, Tr. lat., A, C | G (collation de Brunck) | oui | `ED/1783_Strasbourg_Brunck/aristophaniscom02arisgoog.pdf` | texte PDF 97–159 = p. 74–136 ; notes PDF 400–465 = p. 81–146 |
| E17 | 1794 | Ph. Invernizi | *Comoediae … auctoritate libri praeclarissimi saeculi decimi emendatae*, Leipzig, Weidmann, t. II | T, A | R (première édition fondée sur R) | oui | `ED/1794_Leipzig_Invernizi_t2_texte/comoediaearis02aris.pdf` | PDF 431–522 = p. [423]–514 |
| E18 | 1810 | Brunck (réimpr.) | *Comoediae … cum versione Latina, variis lectionibus, notis et emendationibus*, Oxford, N. Bliss, 4 vol. | T, A, C (t. I) ; Tr. lat. (t. IV) | G (d'après Brunck) | oui | `ED/1810_Oxford_Brunck_reimpr_t1/bub_gb_GC_TY4PiDqQC.pdf` (t. I) | PDF 111–185 = p. [83]–157 |
| E18b | 1823 | Brunck (réimpr.) | *Comoediae ex optimis exemplaribus emendatae, cum versione Latina*, Londres, G. et W. B. Whittaker, 3 vol. | T, Tr. lat. en regard | G (d'après Brunck) | oui | `ED/1823_Londres_Brunck_reimpr_t1/aristophaniscom04brungoog.pdf` (t. I) | PDF 134–240 = p. [123]–229 |
| E19 | 1812–1814 | anonyme (stéréotype Tauchnitz) | *Comoediae ad optimorum librorum fidem accurate editae*, Leipzig, Tauchnitz, 3 vol. (*Thesm.* au t. III, 1814 : c'est l'« ed. Lipsiensis (1814) » de l'apparat de l'auteur) | T | vulg. [à préciser] | oui | `ED/1814_Leipzig_Tauchnitz_t3/bsb10232505_extraits_Thesm.pdf` (extrait) | PDF 9–80 = p. [167]–238 |
| E20 | 1825 | [W. Dindorf] | *Comoediae ad optimorum librorum fidem cum brevi annotatione critica editae*, Leipzig, Teubner, 2 vol. | T, A brève | [à vérifier] | oui | `ED/1825_Leipzig_Teubner_Dindorf_t2/aristophaniscom00passgoog.pdf` | PDF 95–152 = p. [88]–145 |
| E21 | 1826 | J. Fr. Boissonade | *Poetarum Graecorum Sylloge*, Aristophanes t. III, Paris, Lefèvre | T, notules | [à vérifier] | oui | `ED/1826_Paris_Boissonade_t3/comoediaethesmo00boisgoog.pdf` | PDF 10–92 = p. [1]–83 ; notules PDF 314–318 = p. 293–297 |
| E22 | 1829 | I. Bekker | *Comoediae cum scholiis et varietate lectionis*, Londres, Whittaker et al., 5 vol. | T, A, Sch., Tr. lat., C (*variorum*) | R (autopsie, 1818) | oui | `ED/1829_Londres_Bekker_t1_texte/…`, `…_t2_scholies/…`, `…_t4_notes/…` | t. I PDF 388–432 = p. 361–405 ; t. II PDF 152–171, 584–592 ; t. IV PDF 252–328 |
| E23 | 1830 | F. H. Bothe | *Comoediae*, Leipzig, Hahn, t. IV | T, A, C brèves | R (d'après Invernizi) [à préciser] | oui | `ED/1830_Leipzig_Bothe1/comoediaebothe03aris.pdf` | PDF 339–422 = t. IV p. [1]–84 |
| E24 | 1830 | W. Dindorf | *Comoediae, accedunt perditarum fabularum fragmenta*, Leipzig, Weidmann, 2 vol. (tirage à part des *Poetae scenici*) | T | — | oui | — (t. II introuvable en ligne) | — |
| E25 | 1830–1869 | W. Dindorf | *Poetae scenici Graeci* (Leipzig, 1830 ; Oxford, 1846 ; Leipzig, 1851, 1865 ; 5ᵉ éd. 1869) | T | [à vérifier] | oui | `ED/1830_Leipzig_Dindorf_Poetae_scenici/poetaescenicigra00dind.pdf` (1830) | PDF 724–741 = p. 687–704 |
| E26 | 1832 | B. Thiersch | *Thesmophoriazusae cum scholiis cod. Ravennatis et fragm. Thesmoph. poster.*, Halberstadt, Helm | T, A, C, Sch. | G et Iunt. (collations de Thiersch) ; R d'après Bekker 1829 | oui | `ED/1832_Halberstadt_Thiersch/thesmophoriazus00arisgoog.pdf` | préf. PDF 8–16 ; texte PDF 34–147 ; scholies PDF 148–186 ; fragm. PDF 187–199 |
| E27 | 1835–1838 | W. Dindorf | *Comoediae*, Oxford : t. II (texte, 1835), t. III (*Annotationes*, 1837), t. IV 3 (scholies, 1838) | T, A, C, Sch. | R d'après Invernizi et Bekker | oui | `ED/1835_Oxford_Dindorf_t2_texte/…` ; `ED/1837_…_t3_annotationes/…` ; `ED/1838_…_t4-3_scholies/…` | t. II PDF 4–41 = p. [415]–452 ; t. III PDF 710–765 = p. 701–756 ; t. IV 3 PDF 311–335 = p. 310–334 |
| E28 | 1838 | F. V. Fritzsche | *Thesmophoriazusae*, Leipzig, Koehler | T, A, C ample | Iunt., G, R (d'après Invernizi et Bekker–Seidler) | oui | `ED/1838_Leipzig_Fritzsche/thesmophoriazusa00aris.pdf` (+ `thesmophoriazus01fritgoog.pdf`) | préf. PDF 9–24 = p. V–XX ; texte et comm. PDF 25–597 = p. 1–573 |
| E29 | 1838 | Didot (W. Dindorf) | *Comoediae et perditarum fragmenta, ex nova recensione G. Dindorf*, Paris, A. F. Didot | T, Tr. lat. | texte de Dindorf | oui | `ED/1838_Paris_Didot_Dindorf/aristophaniscome00long.pdf` | PDF 300–335 = p. 286–321 |
| E29b | 1842 | C. H. Weise | *Comoediae ad optimorum librorum fidem accurate recensuit C. H. Weise*, *nova editio stereotypa*, Leipzig, Tauchnitz, 2 vol. in-32, t. II (*Pax, Aves, Lysistrata, Thesm.*) | T, notes critiques (variantes) | vulg. | oui | `ED/1842_Leipzig_Tauchnitz_Weise_t2/aristophaniscom00collgoog.pdf` | PDF 290–360 = p. [265]–335 ; notes PDF 368–369 = p. 343–344 |
| E30 | 1844 | R. Enger | *Aristophanis comoediae cum scholiis* I 2 : *Thesmophoriazusae*, Bonn, H. B. König | T, A, C, Sch. | R d'après Bekker 1829 ; G et Iunt. d'après Thiersch et Reisig | oui | `ED/1844_Bonn_Enger/bsb10232531.pdf` | préf. PDF 5–6 = p. V–VI ; texte, scholies et notes PDF 7–211 = p. 1–205 |
| E31 | 1845 | F. H. Bothe | *Comoediae*, 2ᵉ éd., Leipzig, Hahn, t. III | T, A, C brèves | R d'après Bekker, G d'après Brunck | oui | `ED/1845_Leipzig_Bothe2_t3/aristophaniscom00bothgoog.pdf` | PDF 108–191 = p. 97–184 |
| E32 | 1848 ; 1868 | H. A. Holden | *Comoediae quae supersunt cum perditarum fragmentis*, Cambridge–Londres (3ᵉ éd. 1868) | T | — | oui | `ED/1868_Cambridge_Holden/aristophaniscom01arisgoog.pdf` | PDF 546–592 = p. 455–501 |
| E33 | 1852 ; 1872 | Th. Bergk | *Comoedias*, Leipzig, Teubner, 2 vol. ; t. II, *editio altera correctior*, 1872 | T, A (préface) | — | oui | `ED/1867_Leipzig_Bergk_t2/aristophaniscomo02aris.pdf` (= t. II, 1872) | PDF 153–196 = p. 123–166 ; préf. PDF 16–20 = p. XII–XVI |
| E34 | 1860 | A. Meineke | *Comoediae*, Leipzig, Tauchnitz, t. II | T, A (*adnotatio critica*) | — | oui | `ED/1860_Leipzig_Meineke_t2/aristophaniscom00meingoog.pdf` | PDF 330–427 = p. 127–176 ; adn. PDF 36–45 = p. XVII–XXII |
| E35 | 1869 | W. Dindorf | *Aristophanis fabulae superstites et perditarum fragmenta*, Leipzig, Teubner (= *Poetae scenici*, 5ᵉ éd.) | T | — | oui | `ED/1869_Leipzig_Dindorf_Fabulae/aristophanisfab00dindgoog.pdf` | PDF 130–144 = p. [121]–135 |
| E36 | 1878 | A. von Velsen | *Aristophanis Thesmophoriazusae*, Sarrebruck, Hofer (programme) | T | R (autopsie) | oui | — (non numérisé) | — |
| E37 | 1880 | F. H. M. Blaydes | *Aristophanis comoediae* I : *Thesmophoriazusae*, Halle, Orphanotropheum | T, A, C, Sch. | R (collation personnelle « cum ed. Bergk. 1857 ») | oui | `ED/1880_Halle_Blaydes/comoediaeblaydes01aris.pdf` (+ `aristophaniscom01blaygoog.pdf`) | préf. PDF 9–13 ; texte PDF 15–140 = p. 1–126 ; comm. PDF 141–273 = p. 127–259 ; *Addenda* PDF 274–285 = p. 260–271 |
| E38 | 1883 | A. von Velsen | *Aristophanis Thesmophoriazusae*, Leipzig, Teubner | T, A | R (autopsie, 1866–1867), G | oui | `ED/1883_Leipzig_Velsen/aristophanisthe00velsgoog.pdf` | préf. PDF 10–11 = p. 5–6 ; texte PDF 12–93 = p. 7–88 |
| E39 | 1891 | Th. Bergk | *Thesmophoriazusae*, Leipzig, Teubner (tirage séparé ; retirage 1932) | T | — | oui | — | — |
| E40 | 1898 | C. H. Weise | *Aristophanis comoediae ad optimorum librorum fidem*, Leipzig, Holtze, t. II (retirage de E29b) | T | vulg. | oui | — (voir E29b) | — |
| E41 | 1901 ; 1907 | F. W. Hall, W. M. Geldart | *Aristophanis comoediae*, Oxford (OCT), t. II | T, A | R (photographies) | oui | 1901 : `ED/1907_Oxford_Hall_Geldart_t2/aristophaniscomo02arisuoft.pdf` (dossier mal daté) ; 1907 : `ED/1907_Oxford_Hall_Geldart_t2_ed2_reimpr/bwb_P9-BTV-995_2.pdf` | PDF 66–110 (les deux) |
| E42 | 1904 | J. van Leeuwen | *Thesmophoriazusae cum prolegomenis et commentariis*, Leyde, Sijthoff | T, C, A brèves | R (fac-similé de 1904) | oui | `ED/1904_Leyde_van_Leeuwen/aristophanisthe00leeugoog.pdf` | prolég. PDF 10–25 = p. I–XVI ; texte et comm. PDF 26–179 = p. 1–154 |
| E43 | 1904 ; 1924 | B. B. Rogers | *The Thesmophoriazusae*, Londres, Bell ; repris dans la Loeb, t. III, 1924 | T, Tr. angl., C, A | — | oui | `ED/1904_Londres_Rogers/thesmophoriazus00rogegoog.pdf` ; `ED/1924_Londres_Rogers_Loeb_t3/aristophaneswith03arisuoft.pdf` | 1904 : texte PDF 50–227, appendice PDF 228–281 ; 1924 : PDF 135–252 = p. 125–242 |
| E44 | 1928 | V. Coulon, H. Van Daele | *Aristophane* IV, Paris, Les Belles Lettres (CUF) | T, A, Tr. fr. | R | non | Drive (CUF IV) ; extrait : `.sources/drive/ravennas/Coulon_1928_Thesm_Grenouilles_textrep.txt` | — |
| E45 | 1956 | R. Cantarella | *Aristophanis Comoediae* IV, Milan, ISEI | T, A, Tr. it. | — | non | — | — |
| E45b | 1974 | M. Balasch | *Aristòfanes, Comèdies* V : *Les Tesmofòries. Les Granotes*, Barcelone, Fundació Bernat Metge (n° 190), 185 p. | T révisé, Tr. cat. | — | non | — | — |
| E46 | 1983 | G. Paduano | *Aristofane, La festa delle donne*, Milan, BUR | T (Coulon retouché), Tr. it., notes | — | non | Drive (`TH/Le donne alle Tesmoforie…pdf`) | — |
| E47 | 1988 | J. F. Gannon | *Aristophanes' Thesmophoriazusae*, Bryn Mawr | T (+ notes ?) | — | non | — | — |
| E48 | 1994 | A. H. Sommerstein | *Thesmophoriazusae*, Warminster, Aris & Phillips | T, A, Tr. angl., C | R | non | Drive ; extrait : `.sources/drive/ravennas/Sommerstein_1994_Thesm_textrep.txt` | — |
| E49 | 2000 | J. Henderson | *Aristophanes* III (*Birds, Lysistrata, Women at the Thesmophoria*), Cambridge (Mass.), Loeb | T, Tr. angl. | — | non | — | — |
| E50 | 2001 | C. Prato, D. Del Corno | *Le donne alle Tesmoforie*, Milan, Fondazione Valla | T, A, Tr. it., C | R (microfilm ; vérifications sur l'original) | non | Drive ; extrait : `.sources/drive/ravennas/Prato_2001_…textrep.txt` | — |
| E51 | 2003 | B. Marzullo | *Le commedie*, Rome, Newton & Compton (« testo greco integralmente rinnovato e appendice critica ») | T, A (appendice), Tr. it. | — | non | — | — |
| E52 | 2004 | C. Austin, S. D. Olson | *Thesmophoriazusae*, Oxford, OUP | T, A, C | R | non | Drive ; extrait des p. i–lxxix : `.sources/drive/ravennas/AustinOlson_2004_Thesm_textrep.txt` | — |
| E53 | 2006 | G. Mastromarco, P. Totaro | *Commedie di Aristofane* II, Turin, UTET | T, Tr. it., notes, C (Totaro) | — | non | Drive [à vérifier] | — |
| E54 | 2007 | N. G. Wilson | *Aristophanis Fabulae* II, Oxford (OCT) | T, A | R (rapports publiés, contrôlés sur le fac-similé) | non | `.sources/drive/editions/Wilson II …pdf` | — |
| E55 | 2016 | R. Saetta Cottone | *Les Thesmophories ou La fête des femmes*, Paris, De Boccard | T, Tr. fr., I, C | — | non | — | — |
| E56 | 2025 | L. Di Virgilio | *Tesmoforiazuse. I canti*, Pise–Rome, F. Serra | T (parties lyriques), C | — | non | — | — |

## 3. Notices détaillées

Schéma de chaque notice : référence complète (titre abrégé, lieu, imprimeur, date, collation d'après la
notice de catalogue citée) ; nature ; base manuscrite, avec la source de l'information ; DP ; URL ;
fichier local ; pages des *Thesm.* ; remarques.

### 3.1. De l'*editio princeps* à Ravestein (1516–1670)

**E01. 1516 — Euphrosynus Boninus, *editio princeps* (« Iunt. »).**
- Réf. : Ἀριστοφάνους Θεσμοφοριάζουσαι. Τοῦ αὐτοῦ Λυσιστράτη. *In hoc parvo libro haec insunt.
  Aristophanis Cereris sacra celebrantes. Eiusdem Lysistrate*, [Florence, Bernardo Giunta], 54 f., in-8°
  (BnF cb30027205r). Lettre de B. Giunta à Francesco Accolti, « Florentiae X. ianuarii MDXV » ; postface
  « Bernardus Iunta lectori » et colophon « His summa manus imposita est, quinto Kl. Februarii M.D.XV.
  Leonis Papae nostri anno tertio » (textes cités par Velsen 1871, p. 3), soit le 28 janvier 1516 (style
  florentin).
- Nature : T, sans scholies.
- Base : **R lui-même**. Giunta dit avoir tiré les deux comédies « ex urbinate bibliotheca antiquissimum
  Aristophanis exemplar » ; Velsen 1871, p. 3–4, montre que ce *codex Urbinas* est R : les traits et
  chiffres pâles portés dans R aux *Lys.* et *Thesm.* renvoient aux pages des cahiers de la Juntine
  (vérification de R. Schöll à Ravenne, puis de Velsen sur l'exemplaire de Munich) : « Der Codex Urbinas
  der Juntina ist kein anderer, als eben der Ravennas selbst » (p. 4). La main du XVIᵉ s. qui a complété
  les sigles de personnages dans R est celle de Boninus (Velsen 1871, p. 6–7 ; Velsen 1883, p. 5).
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb10912207.
- Fichier : `ED/1515_Florence_Iunta_editio_princeps_Thesm_Lys/bsb10912207.pdf` (122 vues ; manifeste IIIF
  joint). *Thesm.* : PDF 12–61 (titre PDF 5 ; lettre de Giunta PDF 11 ; colophon PDF 115).
- Remarque : la Juntine de septembre 1515 (*Comoediae novem*, Ph. Giunta, `ED/1515_Florence_Iunta_Comoediae_novem/bub_gb_mcdv56pdPcYC.pdf`,
  numérisée à rebours) ne contient pas les *Thesm.* ; la lettre de B. Giunta (PDF 555) y annonce les deux
  pièces inédites promises par Boninus. Elle n'a qu'un intérêt historique.

**E02. 1532 — Simon Grynaeus, Bâle (Cratander et Bebel).**
- Réf. : Ἀριστοφάνους εὐτραπελωτάτου κωμῳδίαι ἕνδεκα. *Aristophanis facetissimi comoediae undecim*,
  Basileae, apud And. Cratandrum et Ioan. Bebelium, 1532, [8]-514 p., in-4° (BnF cb300271133 ;
  cb38754366f). Avis « And. Cratander lectori » (PDF 9), préface « Simon Grynaeus iuveni studioso S. »
  (PDF 10). Première édition des onze comédies.
- Nature : T. Base : vulgate (Aldine pour les neuf, Juntine pour *Lys.* et *Thesm.*) ; Prato 2001,
  p. XXXIII, lui prête en outre un recours ponctuel « per le Tesmoforiazuse » au manuscrit de la Juntine
  [à vérifier].
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb00024026.
- Fichier : `ED/1532_Bale_Cratander_Grynaeus/bsb00024026.pdf` (539 vues). *Thesm.* : PDF 446–487 =
  p. 429–470 (personnages PDF 446 ; *Lys.* p. 471 = PDF 488).
- Remarque : le « Grynaeus » des apparats modernes n'est pas cette édition mais la Brubachiana de 1544
  (E06) : voir `recherche/conjectures_sources.md` § 2 (v. 16 : Bâle 1532 « πρῶτα μηχανήσατο », PDF 446 ;
  Francfort 1544 « πρῶτ' ἐμηχανήσατο »).

**E03. 1538 — Bartolomeo Zanetti, Venise (« Veneta »).**
- Réf. : *Aristophanis facetissimi comoediae undecim*, Venetiis, in aedibus Bartholomaei Zannetti
  Casterzagensis, sumptibus vero D. Melchioris Sessa, 1538, 280 f., in-8° (BnF cb30027115s).
- Nature : T (scholies pour les neuf pièces de l'Aldine ; aucune pour les *Thesm.*). Base : vulgate,
  « abbastanza innovativa » pour les *Thesm.* (Prato 2001, p. XXXII) ; avec la Brubachiana, l'édition qui
  apporte « the best and most numerous » des corrections justes du XVIᵉ s. (Austin 1987, p. 69).
- DP : oui. URL : https://archive.org/details/ARes70622.
- Fichier : `ED/1538_Venise_Zanetti/ARes70622.pdf` (568 vues). *Thesm.* : PDF 468–512 (personnages
  PDF 468 ; *Lys.* PDF 513) ; foliotation non relevée.

**E04. 1540 — Christian Wechel, Paris.**
- Réf. : Κωμῳδίαι ἕνδεκα. *Aristophanis Comoediae undecim. Comoediarum catalogum versa pagella
  indicabit*, Parisiis, apud Christianum Wechelum sub scuto Basiliensi in vico Iacobaeo, et sub scuto
  Iacobaeo et Pegaso in vico Bellovacensi, 1540, « 11 parties », in-4° (BnF cb300271164) ; B3Kat
  BV036018332 (« 567 S. ») ; exemplaire BSB 4 A.gr.a. 128.
- Nature : T. Chaque comédie a sa page de titre (*Thesm.* : « Aristophanis facetissimi comoedia Cereris
  sacra celebrantes, Parisiis, apud Christianum Wechelum … M.D.XL »), mais la pagination est continue.
  Base : vulgate [modèle exact à déterminer]. Citée comme « Parisina Wechelii » par Invernizi (t. I,
  Prooemium, p. VI) et comme « Wech. » par Blaydes 1880, p. VII.
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb10150263.
- Fichier : `ED/1540_Paris_Wechel/bsb10150263_extraits_Thesm.pdf` (56 vues : PDF 1–4 = vues BSB 1–4,
  reliure, garde, titre général, avis « Christianus Wechelus candido lectori » avec la liste des comédies ;
  PDF 5–56 = vues BSB 471–522) et manifeste IIIF. *Thesm.* : PDF 5–53 = p. [469]–517 (titre p. [469],
  personnages p. [470], texte p. 471–517, souscription « Ἀριστοφάνους Θεσμοφοριαζουσῶν τέλος ») ;
  page de titre de *Lys.* PDF 55.

**E05. 1542 — Farreus, Venise.**
- Réf. : *Aristophanis facetissimi comoediae undecim*, Venetiis, 1542, 280 f., in-8° (BnF cb30027118t ;
  « apud Io. Farreum et fratres »).
- Nature : T. Base : réimpression de Zanetti (Prato 2001, p. XXXII). Bergler (1760) collationne encore
  « Ed. Farrei & Brub. » ; Enger adopte au v. 1197 le οὐδέν « exstat in editione Farrei » (p. 199, PDF 205).
- DP : oui. URL : https://books.google.com/books?id=Wu5-_TQ_tCoC ; https://archive.org/details/bub_gb_Wu5-_TQ_tCoC.
- Fichier : `ED/1542_Venise_Farreus/bub_gb_Wu5-_TQ_tCoC.pdf` (574 vues, numérisation **à rebours**).
  *Thesm.* : PDF 97→53 (personnages PDF 97 ; titre courant fautif ΕΚΚΛΗΣΙΑΖΟΥΣΑΙ PDF 96) ; *Lys.* PDF 52→1.

**E06. 1544 — « Brubachiana » (Francfort, P. Brubach) : le « Grynaeus » des apparats.**
- Réf. : *Aristophanis facetissimi comoediae undecim*, Francofurti, apud Pet. Brubachium, anno XLIIII,
  [4]-286 f., in-8° (BnF cb30027114f).
- Nature : T. Base : vulgate, avec des corrections propres : « apportò decisivi miglioramenti al testo della
  nostra commedia » (Prato 2001, p. XXXIII). Elle reprend la préface de Grynaeus († 1541) mais non son
  texte : G. Burges, *Classical Journal* 14 (1816), p. 131 (« Repetitur quidem ibi Grynaei Praefatio, sed
  passim discrepat textus a Basileensi … consentiunt Brubachii lectiones cum iis quas Grynaeo tribuit
  Bentleius ») ; Austin 1987, p. 69 (« the Frankfurt edition, edited by S. Grynaeus »).
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb10169310.
- Fichier : `ED/1544_Francfort_Brubach_Grynaeus/bsb10169310.pdf` (592 vues). *Thesm.* : PDF 494–539 =
  f. 240v–263r (*Lys.* f. 263v = PDF 540).

**E07. 1545 — Gilles Bourdin (Aegidius Burdinus), Paris.**
- Réf. : Τὰ τοῦ Αἰγιδίου Βουρδίνου σχόλια εἰς τὴν τῶν τοῦ Ἀριστοφάνους Θεσμοφοριαζουσῶν κωμῳδίαν,
  Parisiis, apud Ioannem Lodoicum Tiletanum, ex adverso Collegii Remensis, 1545, [8]-71-[1] p.
  (sig. α⁴, A–I⁴), in-4° (BnF cb300272063 : Bourdin « auteur du commentaire » et « éditeur scientifique »).
- Nature : scholies grecques de Bourdin, avec le texte de la pièce si l'on en croit la notice BnF et Prato
  (« autore egli stesso di un'edizioncina della nostra commedia (1545) », p. XXXIV) [à vérifier sur
  l'exemplaire] ; lettre-dédicace grecque à François Iᵉʳ, reprise dans l'édition de 1607 (p. 762).
- DP : oui. URL : Gallica `bpt6k857402r` (https://gallica.bnf.fr/ark:/12148/bpt6k857402r ; inaccessible
  depuis cette machine : blocage Cloudflare).
- Fichier : Drive, `Thesmophories/Bourdin 1540 Ta_tou_Aigidiou_Bourdinou_scholia_[…]bpt6k857402r.pdf`
  (copie de Gallica ; l'année « 1540 » du nom de fichier est fausse : la notice BnF et W. Dindorf,
  Invernizi t. VIII, 1821, préface p. VI, PDF 12, donnent 1545) ; pas encore copié dans `.sources/drive/fichiers/`. Relais locaux des scholies : édition de
  1607 (E11) et Invernizi–Dindorf t. XI, 1823, p. 271–333 (§ 4).

**E08. 1547 — « Frobeniana » (Bâle, Froben), attribuée à Sigismundus Gelenius.**
- Réf. : Ἀριστοφάνους κωμῳδίαι ἐννέα μετὰ σχολίων … καὶ δύο ἄνευ σχολίων. *Aristophanis comoediae novem
  cum commentariis antiquis admodum utilibus, duaeque sine commentariis, adiecto copiosissimo indice*,
  Basileae, in officina Frobeniana, 1547, [11]-571-[23] p., in-fol. (BnF cb300271195 ; cb38754370p porte
  « [Sigis. Gelenius edidit] »).
- Nature : T (les *Thesm.* sans scholies). Base : vulgate ; la lettre dédicatoire de l'exemplaire numérisé
  (PDF 6) a ses noms caviardés ; son auteur, élève de Musurus, promet pour les deux dernières pièces un
  texte « castigatiores … quam antea ». Importance : les exemplaires annotés par Biset, Casaubon, Bentley et
  Daubuz sont des Frobeniana (Austin 1987, p. 62–67 ; voir `conjectures_sources.md`).
- DP : oui. URL : https://books.google.com/books?id=NVBJxJmhIW8C ; https://archive.org/details/bub_gb_NVBJxJmhIW8C.
- Fichier : `ED/1547_Bale_Froben_Gelenius/bub_gb_NVBJxJmhIW8C.pdf` (642 vues). *Thesm.* : PDF 546–574 =
  p. 512–540 (titre sous la fin de l'*Assemblée*, p. 512 ; *Lys.* p. 541 = PDF 575).

**E09. 1548 — édition « de Caninius », « Ioan. Gryphius excudebat ».**
- Réf. : Ἀριστοφάνους κωμῳδιοποιῶν δεξιωτάτου κωμῳδίαι ἕνδεκα. *Aristophanis comoediae undecim, multis
  metris corruptis, mendisque plurimis purgatae, ut emendatiores hactenus non prodierint. Emendationis
  ratio ad calcem libri explicatur*, « Ioan. Gryphius excudebat », 1548 (page de titre, PDF 602 ; sans lieu).
  Attribuée à Angelus Caninius et localisée à Venise par Prato 2001, p. XLIV (« A. Caninius, Venetiis (ap.
  Gryphium) 1548 ») ; Blaydes 1880, p. VII, dit « ap. Gryph. Lugd. », d'où le nom du dossier local.
- Nature : T. Base : vulgate, avec corrections métriques ; l'avis « Typographus lectori » (PDF 7) annonce
  que les *emendationum rationes* promises au titre n'ont pu être jointes. « Editio Caninii » chez Enger
  (v. 3), « Canini » dans l'apparat de l'auteur (vv. 620, 1101).
- DP : oui. URL : https://books.google.com/books?id=LBXPhhHGIUYC ; https://archive.org/details/bub_gb_LBXPhhHGIUYC.
- Fichier : `ED/1548_Lyon_Gryphius/bub_gb_LBXPhhHGIUYC.pdf` (606 vues, numérisation **à rebours**).
  *Thesm.* : PDF 99→55 = f. 233v–255v (personnages PDF 99 ; personnages de *Lys.* PDF 54 = f. 256r).

**E10. 1600 — Christophe Raphelengius, Leyde (officina Plantiniana).**
- Réf. : Ἀριστοφάνους εὐτραπελωτάτου κωμῳδίαι ἕνδεκα. *Aristophanis facetissimi comoediae undecim*,
  Ex officina Plantiniana, apud Christophorum Raphelengium, Academiae Lugduno-Bat. typographum, 1600,
  [2]-620 p., in-16 (BnF cb300271222).
- Nature : T seul. Base : vulgate. Prato 2001, p. XLIV, cite un exemplaire annoté de cette édition
  (« Anonymus Parisinus », début du XVIIᵉ s.) [cote à vérifier].
- DP : oui. URL : https://books.google.com/books?id=WuyoS4JxpT4C ; https://archive.org/details/bub_gb_WuyoS4JxpT4C.
- Fichier : `ED/1600_Leyde_Raphelengius/bub_gb_WuyoS4JxpT4C.pdf` (671 vues). *Thesm.* : PDF 573–618 =
  p. 524–569 (*Lys.* p. 570 = PDF 619).

**E11. 1607 — Aemilius Portus et Odet Biset, Genève (« Caldoriana »).**
- Réf. : Κωμῳδίαι ἕνδεκα … *Aristophanis comoediae undecim, cum scholiis antiquis, quae studio et opera
  nobilis viri Odoardi Biseti Carlaei sunt quam plurimis locis accurate emendata, et perpetuis novis scholiis
  illustrata …*, Aureliae Allobrogum, sumptibus Caldorianae societatis, 1607, XXVI-916-27 p., in-fol.
  (BnF cb30027123d) ; Prato 2001, p. XLIV : « opera et studio … Aem. Fr. Porti Cretensis filii ex Biseti
  autographo exscripti ».
- Nature : T, Tr. lat. (« Sacra Cereris celebrantes »), scholies anciennes, scholies nouvelles de Biset
  (ΒΙΣΕΤΟΣ) et de Bourdin (ΒΟΥΡΔΙΝΟΣ). Base : vulgate, corrigée par Biset.
- DP : oui. URL : https://books.google.com/books?id=46Rraf1UeBIC ; https://archive.org/details/bub_gb_46Rraf1UeBIC.
- Fichier : `ED/1607_Geneve_Portus_Biset/bub_gb_46Rraf1UeBIC.pdf` (1023 vues). *Thesm.* : PDF 830–910 =
  p. 760–813 (p. 760 titre, note « Bisetus », hypothesis, personnages ; p. 762 lettre de Bourdin à
  François Iᵉʳ ; *Lys.* p. 814 = PDF 911).

**E12. 1624 — Leyde, Jean Maire (notes de Joseph Scaliger).**
- Réf. : Κωμῳδίαι ιαʹ. *Aristophanis Comoediae undecim, Graece et Latine, cum indice paroemiarum
  selectiorum et emendationibus virorum doctorum, praecipue Josephi Scaligeri. Accesserunt praeterea
  fragmenta ejusdem ineditarum comoediarum*, Lugduni Batavorum, apud Joannem Maire, 1624, 2 parties en
  1 vol., in-12 (BnF cb300271253) ; B3Kat BV014163411 (« [12] Bl., 935, 56 S. »), BV026284747.
- Nature : T, Tr. lat., notes (Scaliger : p. 917–935 selon Prato 2001, p. LXXIV). Base : vulgate (texte
  de la Caldoriana selon Prato, p. XXXIV). Tanneguy Le Fèvre (Faber) a annoté son exemplaire de cette
  édition (BnF, Rés. Yb. 740 ; Austin 1987, p. 65–66), aux p. 756–816 pour les *Thesm.* d'après Prato
  (p. LXXI) [à vérifier].
- DP : oui. URL : aucune numérisation trouvée (IA, BSB) ; copie numérique sur le Drive.
- Fichier : Drive, `Thesmophories/Aristophanis_Comoediae_Undecim Scaliger propre.pdf` (42,9 Mo ; édition
  de 1624 ou de 1670 [à vérifier]) ; non encore copié localement. Les notes de Scaliger sont réimprimées en
  1670 (E13).

**E13. 1670 — Amsterdam, Johannes Ravestein (« editio novissima »).**
- Réf. : *Aristophanis comoediae undecim, Graece et Latine, ut et fragmenta earum quae amissae sunt …
  cum emendationibus virorum doctorum, praecipue Josephi Scaligeri, et indice paroemiarum selectiorum.
  Accesserunt … notae … ex variis auctoribus collectae …*, Amstelaedami, apud Joannem Ravesteinium, 1670,
  2 parties en 1 vol., in-12 (BnF cb30027127s ; cb387543742).
- Nature : T, Tr. lat. de Divus (« Aristophanis Cerealia celebrantes, interprete Andrea Divo », p. 751),
  notes (Scaliger, Biset…). Base : vulgate.
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb11088393 (t. II) ; bsb11088392 (t. I).
- Fichiers : `ED/1670_Amsterdam_Ravestein_t2/bsb11088393.pdf` (468 vues) ; t. I (sans les *Thesm.*) :
  `ED/1670_Amsterdam_Ravestein_t1/bsb11088392.pdf`. *Thesm.* : t. II, PDF 70–143 = p. 750–823 (*Lys.*
  p. 824 = PDF 144) ; « Notae in Aristophanem … potissimum duobus exemplaribus manu Josephi Scaligeri
  emendatis » p. 917 (PDF 237), section « In Cerealia celebrantes » p. 928–931 (PDF 248–251 ; sigles
  *Scal.*, *Bis.*, *F. C.*, *Ven.*, *Vet.*) ; notes de Faber sur l'*Assemblée* p. 982 sqq.

### 3.2. Le XVIIIᵉ siècle (1710–1794)

**E14. 1710 — Ludolph Küster, Amsterdam (Th. Fritsch).**
- Réf. : *Aristophanis comoediae undecim, Graece et Latine, ex codd. mss. emendatae, cum scholiis antiquis,
  inter quae scholia in Lysistratam ex cod. Vossiano nunc primum in lucem prodeunt. Accedunt notae virorum
  doctorum in omnes comoedias, inter quas nunc primum eduntur Isaaci Casauboni in Equites, illustris.
  Ezech. Spanhemii in tres priores et Richardi Bentleji in duas priores comoedias …*, Amstelodami,
  sumptibus Thomae Fritsch, 1710, [10]-XXVIII-580-[60]-[1]-324 p., in-fol. (BnF cb300271284).
- Nature : T, nouvelle Tr. lat., scholies (dont celles de Bourdin pour les *Thesm.*), notes *variorum* et
  de Küster. Base : vulgate (les manuscrits du titre concernent d'autres pièces ; Brunck, en 1783, ne
  connaît encore pour les *Thesm.* que l'*Augustanus* : « Rarissima sunt hujus fabulae scripta exemplaria »,
  notes p. 81).
- DP : oui. URL : https://archive.org/details/bub_gb_zn074wA_vlIC (texte OCR seul sur IA) ;
  https://books.google.com/books?id=zn074wA_vlIC.
- Fichiers : `ED/1710_Amsterdam_Kuster/kuster1710_extraits_Thesm.pdf` (120 p., extraits faits à partir des
  images d'IA par `outils/ia_pages_vers_pdf.py`) : PDF 1–40 = feuillets IA n1–n40 (titre, préfaces) ;
  PDF 41–97 = p. 471–527 ; PDF 98–111 = 2ᵉ pagination p. 213–226 env. ; PDF 112–120 = p. 317–325 env. ;
  OCR complet : `ED/1710_Amsterdam_Kuster/bub_gb_zn074wA_vlIC_djvu.txt` ; PDF complet sur le Drive
  (« Kuster bub_gb_zn074wA_vlIC.pdf », 121 Mo). *Thesm.* : p. 474–524 = PDF 44–94 (p. 474 : notice
  « Thesmophoriazusae fabula, quando et quo successu acta fuerit », d'après S. Petit, *Miscell.* I 13) ;
  « Notae in Thesmophoriazusas » p. 217–224 (2ᵉ pagination) = PDF 102–109 ; extraits de Bentley
  (« ex epistolis ad L. Kusterum », *Plutus* et *Nuées*) p. 319–324 = PDF 114–119.

**E15. 1760 — Stephan Bergler, éd. Pieter Burman le Jeune, Leyde (Luchtmans).**
- Réf. : *Aristophanis comoediae undecim, Graece et Latine, ad fidem optimorum codicum mss. emendatae, cum
  nova octo comoediarum interpretatione Latina et notis ad singulas ineditis Stephani Bergleri, necnon
  Caroli Andreae Dukeri ad quatuor priores. Accedunt deperditarum comoediarum fragmenta, a Theod. Cantero
  …*, Lugduni Batavorum, apud S. et J. Luchtmans, 1760, 2 vol. in-4° (BnF cb30027129g).
- Nature : T (versos), Tr. lat. de Bergler (rectos), notes de Bergler en bas de page. Base : vulgate ;
  les notes collationnent les éditions anciennes (« Ed. Farrei & Brub. »).
- DP : oui. URL : https://books.google.com/books?id=kRH7s1SMeIUC (t. II) ; https://archive.org/details/bub_gb_kRH7s1SMeIUC ;
  t. I : bub_gb_9A2i_-sTWR0C.
- Fichier : `ED/1760_Leyde_Bergler_Burman_t2/bub_gb_kRH7s1SMeIUC.pdf` (705 vues). *Thesm.* : t. II,
  PDF 434–522 = p. [999]–1087 (titre grec PDF 434, titre latin PDF 436 ; *Lys.* PDF 524). Le t. I
  (`ED/1760_Leyde_Bergler_Burman_t1/`) ne contient pas les *Thesm.*

**E16. 1781–1783 — Richard François Philippe Brunck, Strasbourg (Treuttel).**
- Réf. : *Aristophanis comoediae ex optimis exemplaribus emendatae, studio Rich. Franc. Phil. Brunck*,
  Argentorati, sumtibus J. G. Treuttel, 1781–1783, 3 vol. in-4° (BnF cb300271311) et éd. in-8° (BnF
  cb30027130p).
- Nature : T, Tr. lat., *variae lectiones*, notes et conjectures. Base : **G**, collationné pour la première
  fois par Brunck (Fritzsche 1838, p. VII : « Augustanum librum scito primum a Brunckio conlatum esse » ;
  Prato 2001, p. XXXIV) ; notes « In Thesmophoriazusas » ouvertes par « Rarissima sunt hujus fabulae
  scripta exemplaria ».
- DP : oui. URL : https://archive.org/details/aristophaniscom02arisgoog (t. I et notes) ; t. II :
  aristophaniscom00arisgoog.
- Fichier : `ED/1783_Strasbourg_Brunck/aristophaniscom02arisgoog.pdf` (616 vues ; t. I, ordre de Brunck
  *Lys.*, *Thesm.*, *Gren.*, *Plut.*, relié avec le volume de notes). *Thesm.* : texte PDF 97–159 =
  p. 74–136 ; notes PDF 400–465 = p. 81–146. Le t. II (`…/aristophaniscom00arisgoog.pdf`) ne contient pas
  les *Thesm.*

**E17. 1794 — Filippo Invernizi, Leipzig (Weidmann) : première édition fondée sur R.**
- Réf. : Ἀριστοφάνους κωμῳδίαι. *Aristophanis comoediae auctoritate libri praeclarissimi saeculi decimi
  emendatae a Philippo Invernizio. Accedunt criticae animadversiones, scholia graeca, indices et virorum
  doctorum adnotationes*, Lipsiae, in libraria Weidmannia, 1794–1834, 13 vol. (Prato 2001, p. XLV) ;
  texte des *Thesm.* au t. II (1794) ; commentaires et scholies aux t. VIII (1821) et XI (1823), éd.
  W. Dindorf (§ 4).
- Nature : T, notes critiques. Base : **R**, que lui avait confié « vir doctissimus … exscribendum atque
  tractandum horis subsicivis », et un *Borgianus* du musée du cardinal Stefano Borgia à Velletri
  (Prooemium, t. I, p. VII–VIII, PDF 17–18). Collation jugée très négligente par Thiersch 1832, p. VI,
  Fritzsche 1838, p. VIII et Enger (préface de *Lys.*, 1844, p. X).
- DP : oui. URL : https://archive.org/details/comoediaearis02aris (t. II) ; t. I : comoediainverniz01aris.
- Fichiers : `ED/1794_Leipzig_Invernizi_t2_texte/comoediaearis02aris.pdf` (620 vues) ; t. I :
  `ED/1794_Leipzig_Invernizi_t1/comoediainverniz01aris.pdf` (Prooemium, spécimens de R). *Thesm.* :
  t. II PDF 431–522 = p. [423]–514 (hypothesis PDF 431, personnages PDF 432 ; *Assemblée* p. 515).

### 3.3. Le XIXᵉ siècle (1810–1898)

**E18. 1810 — Réimpression d'Oxford de Brunck (N. Bliss).**
- Réf. : *Aristophanis comoediae ex optimis exemplaribus emendatae, cum versione Latina, variis lectionibus,
  notis et emendationibus. Accedunt deperditarum comoediarum fragmenta, a R. F. Ph. Brunck*, Oxonii, typis et
  sumtu N. Bliss, 1810, 4 vol. (titre du t. I, PDF 5) ; Prato 2001, p. XLV : « Thesm. vol. I, p. 83 sgg. ».
- Nature : t. I : texte grec de *Lys.*, *Thesm.*, *Gren.*… avec les notes de Brunck au bas des pages ; t. IV :
  version latine (*Thesm.* dans les exemplaires IA aristophaniscom00brungoog et bub_gb_aDjB6ScCuA8C, titre
  « Tom. IV », PDF 5 et 8). Base : G (d'après Brunck). DP : oui.
- URL : https://archive.org/details/bub_gb_GC_TY4PiDqQC (t. I ; autre exemplaire : aristophaniscom05brungoog).
- Fichier : `ED/1810_Oxford_Brunck_reimpr_t1/bub_gb_GC_TY4PiDqQC.pdf` (358 vues ; contrôlé sur les images).
  *Thesm.* : PDF 111–185 = p. [83]–157 (faux-titre p. [83], personnages p. [84], texte p. 85 sqq. ; p. 86 =
  PDF 114 ; *Gren.* : hypothesis PDF 186, texte PDF 189).

**E18b. 1823 — Réimpression de Londres de Brunck (Whittaker).**
- Réf. : Ἀριστοφάνους κωμῳδίαι. *Aristophanis comoediae ex optimis exemplaribus emendatae : cum versione
  Latina, a Rich. Franc. Phil. Brunck*, Londini, sumtibus G. et W. B. Whittaker, 1823, 3 vol. (titre du t. I,
  PDF 8 ; « 3 volumes ; 23 cm » d'après les métadonnées d'IA).
- Nature : T et version latine de Brunck en regard (verso grec, recto latin) ; sans les notes. Base : G
  (d'après Brunck). DP : oui.
- URL : https://archive.org/details/aristophaniscom04brungoog (t. I) ; autres tomes et exemplaires :
  aristophaniscom03brungoog, aristophaniscom05arisgoog, aristophaniscom06arisgoog, aristophaniscomo01aris,
  aristophaniscomo02aris_1, aristophaniscomo02aris_2, aristophaniscomo03aris_0, aristophaniscomo03aris_1.
- Fichier : `ED/1823_Londres_Brunck_reimpr_t1/aristophaniscom04brungoog.pdf` (385 vues ; contrôlé sur les
  images). *Thesm.* : PDF 134–240 = p. [123]–229 (faux-titre PDF 134, personnages PDF 136, texte grec p. 127 =
  PDF 138 ; p. 228 = PDF 239 porte le v. 1220 ; *Gren.* : faux-titre PDF 242). *Lys.* précède (PDF 12–132).

**E19. 1812–1814 — Édition stéréotype anonyme, Leipzig, Tauchnitz.**
- Réf. : *Aristophanis comoediae ad optimorum librorum fidem accurate editae*, Lipsiae, sumtu Caroli
  Tauchnitii, 3 vol. : t. I (1812, 286 p. ; BSB `bsb10232503`), t. II (1812, 350 p. ; BSB `bsb10232504`), t. III
  (1814, 311 p. ; BSB `bsb10232505`) ; tirages « ed. stereotypa » de 1819 et 1828 (B3Kat) ; IA
  aristophaniscom09arisgoog (1829) [tome non identifié].
- Contenu (contrôlé sur les images de la BSB) : le **t. III de 1814** contient *Ach.* (canevas 7 sqq.), *Guêpes*
  (85 sqq.), *Thesm.* (173 sqq.) et *Assemblée* (247 sqq.) ; la notice de la BSB attribue à tort ce contenu au
  t. II, dont le volume numérisé contient notamment les *Cavaliers* (jusqu'au canevas 200), la *Paix* (201 sqq.) et la
  *Lysistrata* (277 sqq.).
- Nature : T sans apparat. Base : vulgate [modèle à préciser]. DP : oui.
- C'est l'« ed. Lipsiensis (1814) » que cite l'apparat de l'auteur au v. 1201 (Ἀρταμουξία : t. III, p. 237,
  « μεμνῆσι τοίνυν τοὔνομ᾽· Ἀρταμουξία », PDF 79 de l'extrait local, contrôlé).
- URL : https://www.digitale-sammlungen.de/view/bsb10232505.
- Fichier : `ED/1814_Leipzig_Tauchnitz_t3/bsb10232505_extraits_Thesm.pdf` (84 p. : PDF 1–8 = canevas 1–8,
  titre du t. III PDF 5 ; PDF 9–84 = canevas 173–248) et manifeste IIIF. *Thesm.* : PDF 9–80 = p. [167]–238
  (hypothesis p. [167], personnages p. [168], texte p. 169–238 ; p. n = PDF n+158) ; *Assemblée* PDF 81.

**E20. 1825 — Leipzig, Teubner (anonyme ; W. Dindorf).**
- Réf. : Ἀριστοφάνους κωμῳδίαι. *Aristophanis comoediae ad optimorum librorum fidem cum brevi annotatione
  critica editae*, Lipsiae, sumptibus et typis B. G. Teubneri, 1825, 2 vol. (titre du t. II, PDF 6 de
  l'exemplaire IA). Sans nom d'éditeur ; attribuée à W. Dindorf par Prato 2001, p. XLV (« G. Dindorf,
  Lipsiae 1825 »).
- Nature : T, brève annotation critique. Base : [à vérifier : Invernizi ?]. DP : oui.
- URL : https://archive.org/details/aristophaniscom00passgoog (t. II) ; t. I probablement
  aristophaniscom01berggoog [à vérifier].
- Fichier : `ED/1825_Leipzig_Teubner_Dindorf_t2/aristophaniscom00passgoog.pdf` (459 vues ; t. II :
  *Oiseaux*, *Thesm.*, *Lys.*, *Gren.*, *Assemblée*, *Plutus*). *Thesm.* : PDF 95–152 = p. [88]–145
  (personnages PDF 95, titre et v. 1 sqq. PDF 96 ; *Lys.* PDF 153).

**E21. 1826 — Jean-François Boissonade, Paris (*Poetarum Graecorum Sylloge*).**
- Réf. : Ἀριστοφάνης. *Aristophanes curante Jo. Fr. Boissonade*, t. III, Parisiis, apud Lefèvre
  bibliopolam, 1826 (= *Poetarum Graecorum Sylloge*, t. XXIII ; « excudebat Julius Didot natu major »)
  (PDF 6–8). Prato 2001, p. XLV, date la série de 1824.
- Nature : T sans apparat ; « Notulae » en fin de volume. Base : [à vérifier]. DP : oui.
- URL : https://archive.org/details/comoediaethesmo00boisgoog.
- Fichier : `ED/1826_Paris_Boissonade_t3/comoediaethesmo00boisgoog.pdf` (341 vues ; *Thesm.*, *Lys.*,
  *Gren.*) ; copie identique sur le Drive. *Thesm.* : PDF 10–92 = p. [1]–83 ; « Notulae in
  Thesmophoriazusas » PDF 314–318 = p. 293–297.

**E22. 1829 — Immanuel Bekker, Londres.**
- Réf. : Ἀριστοφάνους κωμῳδίαι. *Aristophanis comoediae cum scholiis et varietate lectionis. Recensuit
  Immanuel Bekkerus … Accedunt versio Latina, deperditarum comoediarum fragmenta, index locupletissimus,
  notaeque Brunckii, Reisigii, Beckii, Dindorfii, Schutzii, Bentleii, Dobreii, Porsoni, Elmsleii, Hermanni
  …*, Londini, sumtibus Whittaker, Treacher et Arnot [etc.], 1829, 5 vol. (titre, t. I, PDF 8).
- Nature : T et *varietas lectionis* (t. I) ; Tr. lat. et scholies (t. II) ; notes *variorum* (t. IV).
  Base : **R (autopsie, 1818)** : « ibi eum ego a. 1818 inspexi » ; « Scholia Thesmophoriazusarum e
  Ravennate sumpsi » (praefatio, t. I, PDF 12–14). Les éditeurs londoniens ont mal imprimé sa collation
  (Thiersch 1832, p. VI ; Fritzsche 1838, p. VIII–IX ; Enger, préf. de *Lys.*, 1844, p. X).
- DP : oui. URL : https://archive.org/details/aristophanouskm03bekkgoog (t. I) ; …km02bekkgoog (t. II) ;
  …km01bekkgoog (t. IV) ; …km04bekkgoog (t. III) ; …km00bekkgoog, …km05bekkgoog (t. V).
- Fichiers : `ED/1829_Londres_Bekker_t1_texte/aristophanouskm03bekkgoog.pdf` (749 vues) : *Thesm.*
  PDF 388–432 = p. 361–405 (hypothesis de Biset p. 363) ; `ED/1829_Londres_Bekker_t2_scholies/aristophanouskm02bekkgoog.pdf` :
  version latine PDF 152–171 = p. 147–166, scholies PDF 584–592 = p. 271–279 ;
  `ED/1829_Londres_Bekker_t4_notes/aristophanouskm01bekkgoog.pdf` : notes PDF 252–328 = p. 253–329.

**E23. 1830 — Friedrich Heinrich Bothe, Leipzig (1ʳᵉ éd.).**
- Réf. : *Aristophanis comoediae*, ed. Fridericus Henricus Bothe, Lipsiae, Hahn, 1828–1830, 4 vol. ;
  t. IV (1830) : *Thesmophoriazusae. Nubes. Index* (B3Kat ; titre PDF 337). Série *Poetae scenici
  Graecorum*.
- Nature : T, notes critiques et explicatives brèves. Base : R cité (« Rav. ») d'après Invernizi et Bekker
  1829 (les notes citent l'édition de Bekker, p. ex. t. IV p. 82, PDF 405). DP : oui.
- URL : https://archive.org/details/comoediaebothe03aris.
- Fichier : `ED/1830_Leipzig_Bothe1/comoediaebothe03aris.pdf` (702 vues : t. III et IV réunis). *Thesm.* :
  PDF 339–422 = t. IV p. [1]–84 (*Nuées* p. 85 = PDF 423).

**E24. 1830 — Wilhelm Dindorf, Leipzig, Weidmann.**
- Réf. : *Aristophanis comoediae, accedunt perditarum fabularum fragmenta, ex recognitione et cum
  annotationibus Guilielmi Dindorfii*, Lipsiae, libraria Weidmannia, 1830, 2 vol. ; tirage à part
  (« mutata chartarum forma ») des comédies de son édition des *Poetae scenici*, préface de février 1830
  (t. I, PDF 8).
- Nature : T, brèves notes. DP : oui. URL : t. I seul trouvé (IA aristophaniscom07dindgoog : *Ach.*, *Cav.*,
  *Nuées*, *Guêpes*, *Paix*, sans les *Thesm.* ; téléchargé puis écarté). Fichier : —.

**E25. 1830–1869 — W. Dindorf, *Poetae scenici Graeci*.**
- Réf. : *Poetae scenici Graeci, accedunt perditarum fabularum fragmenta, recognovit et praefatus est Guil.
  Dindorfius*, Lipsiae, libraria Weidmannia ; Londini, Black, Young et Young, 1830 (xxxi-766-162 p.) ; rééd.
  *Poetarum scenicorum Graecorum … fabulae superstites et perditarum fragmenta*, Oxonii, J. Abrams et
  C. Richards, 1846 ; Lipsiae, 1851 ; 1865 ; 5ᵉ éd., Lipsiae, Teubner, 1869 (citée par Velsen 1871, p. 1).
- Nature : T (deux colonnes). La préface de 1830 discute des leçons de R (« codex Ravennas », à propos du
  v. 494 : PDF 17 de l'exemplaire bub_gb_mGYGAAAAQAAJ). DP : oui.
- URL (IA) : poetaescenicigra00dind, poetaescenicigr00arisgoog, bub_gb_mGYGAAAAQAAJ, bub_gb_rm0MAAAAYAAJ
  (1830) ; poetarumscenico01arisgoog (1846) ; poetarumscenico00dind (1851) ; poetarumsenicor00unkngoog (1865) ;
  poetarumscenicor00dind, poetarumscenic00dind, poetarumscenico00arisgoog, bub_gb_X5UFpxf3aeEC (1869).
- Fichier : `ED/1830_Leipzig_Dindorf_Poetae_scenici/poetaescenicigra00dind.pdf` (972 vues ; OCR d'IA
  exploitable). *Thesm.* : PDF 724–741 = p. 687–704 (*Lys.* p. 667 ; *Gren.* p. 705 = PDF 742) ; fragments des
  *Thesm. secondes* dans les *Fragmenta* (2ᵉ pagination, p. 145–146 dans l'exemplaire bub_gb_mGYGAAAAQAAJ).
  Pour le texte de 1869, voir E35.

**E26. 1832 — Bernhard Thiersch, Halberstadt.**
- Réf. : Ἀριστοφάνους Θεσμοφοριάζουσαι. *Aristophanis Thesmophoriazusae cum scholiis cod. Ravennatis et
  fragm. Thesmoph. poster.*, rec. Bernardus Thiersch, Halberstadii, Helm, 1832 (B3Kat).
- Nature : T, notes critiques et explicatives, scholies de R, fragments des *Thesm. secondes*. Base :
  praefatio, p. III–VI (PDF 8–11) : **G collationné par Thiersch** (« postquam enim codicem Augustanum
  diligenter contuli ») ; la Juntine d'après l'exemplaire de P. Victorius (Munich), dont il relève les notes
  manuscrites ; **R d'après Bekker** (« ab J. Bekkero a. 1818. collatus ») tel que l'a imprimé l'édition de
  Londres, faute d'avoir vu les fiches de Bekker. Fritzsche et Enger ont réutilisé sa collation de G et de
  la Juntine.
- DP : oui. URL : https://archive.org/details/thesmophoriazus00arisgoog.
- Fichier : `ED/1832_Halberstadt_Thiersch/thesmophoriazus00arisgoog.pdf` (223 vues). Préface PDF 8–16 ;
  texte PDF 34–147 ; scholies PDF 148–186 ; fragments PDF 187–199.

**E27. 1835–1838 — W. Dindorf, Oxford.**
- Réf. : *Aristophanis comoediae*, ex rec. G. Dindorfii, Oxonii, e typographeo academico, 1835–1838 :
  t. II (texte, 1835), t. III (*Annotationes*, 1837), t. IV 3 (*Scholia*, 1838).
- Nature : T ; notes *variorum* et de Dindorf ; scholies. Base : R d'après Invernizi et Bekker (les
  *Annotationes* citent « libri » et les éditions) ; pour les scholies, voir `recherche/scholies.md`
  (transcription de E. Miller selon W. G. Clark, dépendance envers Bekker–Seidler selon Fritzsche). DP : oui.
- URL : https://archive.org/details/aristophaniscom06dindgoog (t. II) ; aristophans00unkngoog (t. III) ;
  aristophaniscom04dindgoog (t. IV 3).
- Fichiers : `ED/1835_Oxford_Dindorf_t2_texte/aristophaniscom06dindgoog.pdf` : PDF 4–41 = p. [415]–452
  (le volume s'ouvre sur les *Thesm.*) ; `ED/1837_Oxford_Dindorf_t3_annotationes/aristophans00unkngoog.pdf` :
  PDF 710–765 = p. 701–756 ; `ED/1838_Oxford_Dindorf_t4-3_scholies/aristophaniscom04dindgoog.pdf` :
  PDF 311–335 = p. 310–334.

**E28. 1838 — Franz Volkmar Fritzsche, Leipzig.**
- Réf. : *Aristophanis Thesmophoriazusae, emendavit et interpretatus est Franc. Volc. Fritzsche, in Academia
  Rostochiensi eloquentiae et poesis professor*, Lipsiae, sumptu Francisci Koehleri, 1838 (B3Kat ; autre
  numérisation : BSB `bsb10232639`).
- Nature : T, notes critiques, commentaire ample. Base (praefatio, p. V–IX = PDF 9–13) : la Juntine
  (collation de Th. Bergk, puis l'exemplaire même de G. Hermann, celui de Freytag annoté par C. Cruciger) ;
  G d'après Brunck, puis d'après la collation de Thiersch ; R d'après Invernizi et d'après la collation de
  Bekker recopiée par A. Seidler — Fritzsche juge Bekker très négligent pour les *Thesm.* (p. IX). Compte
  rendu de G. Hermann, *Zeitschrift für die Alterthumswissenschaft* 5 (1838), col. 670 sqq. (Enger 1844,
  p. VI ; voir `conjectures_sources.md`). DP : oui.
- URL : https://archive.org/details/thesmophoriazusa00aris (Toronto) ; thesmophoriazus01fritgoog.
- Fichiers : `ED/1838_Leipzig_Fritzsche/thesmophoriazusa00aris.pdf` (704 vues ; couche texte latine
  inexploitable, préface océrisée dans `.travail/recension_editions/R2/ocr/`) et
  `…/thesmophoriazus01fritgoog.pdf` (707 vues) ; exemplaire « propre » sur le Drive (75 Mo). *Thesm.* :
  préface PDF 9–24 = p. V–XX ; texte et commentaire PDF 25–597 = p. 1–573 (v. 1230 p. 572) ; appendice
  p. 577 sqq. (PDF 601 sqq.) [contenu à vérifier] ; addenda PDF 660–662 = p. 636–638 ; index PDF 664 sqq.

**E29. 1838 — Paris, Firmin Didot (*Scriptorum Graecorum Bibliotheca*), texte de W. Dindorf.**
- Réf. : Ἀριστοφάνους κωμῳδίαι καὶ κωμῳδιῶν ἀποσπασμάτια. *Aristophanis comoediae et perditarum fragmenta,
  ex nova recensione Guilelmi Dindorf. Accedunt Menandri et Philemonis fragmenta auctiora et emendatiora.
  Graece et Latine, cum indicibus*, Parisiis, editore Ambrosio Firmin Didot, 1838 (titre PDF 9 ; mention
  manuscrite « ed. E. P. M. Longueville »).
- Nature : T, Tr. lat. Base : la préface (Paris, « Nonis Maiis 1838 », PDF 11) dit suivre la dernière
  édition de Dindorf, avec des corrections inédites qu'il a communiquées ; version latine de Brunck,
  adaptée au texte. Réimpressions : 1846, 1877 [à vérifier]. DP : oui.
- URL : https://archive.org/details/aristophaniscome00long.
- Fichier : `ED/1838_Paris_Didot_Dindorf/aristophaniscome00long.pdf` (742 vues). *Thesm.* : PDF 300–335 =
  p. 286–321 (*Gren.* p. 322).

**E29b. 1842 — Carl Hermann Weise, Leipzig (Tauchnitz, stéréotype).**
- Réf. : Ἀριστοφάνους κωμῳδίαι. *Aristophanis comoediae ad optimorum librorum fidem accurate recensuit C. H.
  Weise. Nova editio stereotypa*, Lipsiae, sumtibus et typis Caroli Tauchnitii, 1842, 2 vol. in-32 (BnF
  cb41619769x) ; t. II : *Pax, Aves, Lysistrata, Thesmophoriazusae* (titre, PDF 8). Weise (1787–1840) est mort
  avant ce tirage ; date de la première édition [à vérifier]. Retirage : Leipzig, Holtze, 1898 (E40).
- Nature : T ; « Notae criticae » en fin de volume, qui opposent les leçons des éditions anciennes (« Vett. »,
  « Ald. ») et récentes (« Recc. »). Base : vulgate. DP : oui.
- URL : https://archive.org/details/aristophaniscom00collgoog.
- Fichier : `ED/1842_Leipzig_Tauchnitz_Weise_t2/aristophaniscom00collgoog.pdf` (381 vues ; contrôlé sur les
  images). *Thesm.* : PDF 290–360 = p. [265]–335 (faux-titre PDF 290, hypothesis PDF 292, personnages PDF 293,
  texte p. 269 sqq. ; p. n = PDF n−25) ; « Ad Thesmophoriazusas » p. 343–344 = PDF 368–369 (le cahier des
  *Notae* est numérisé deux fois : PDF 361–369 et 371–377).

**E30. 1844 — Robert Enger, Bonn.**
- Réf. : *Aristophanis comoediae cum scholiis. Ex recensione Roberti Enger. Tomus I. Pars II.
  Thesmophoriazusae*, Bonnae, H. B. König, 1844, VI-205 p. (titre, PDF 2–3 ; BSB A.gr.a. 355-1,1/2 ;
  B3Kat BV006766327).
- Nature : T ; sous le texte, scholies de R (« Scholia libri Ravennatis ») et notes critiques et
  exégétiques. Base : praefatio, p. V–VI (PDF 5–6) : R, G et la Juntine, « de quibus libris dictum in
  Praefatione ad Lysistratam » ; collation de G et de la Juntine par Thiersch (prêtée par Fr. Ritschl) et de
  la Juntine par C. Reisig ; préface de *Lys.* (Bonn, 1844, p. X–XI) : R n'est connu que par Invernizi et
  par Bekker, « non ita collatus, ut nihil desideretur », d'où « ex his libris [G, Iunt.] iam etiam de
  Ravennate coniecturam facere licet » (p. X). **Pas de collation nouvelle de R** : Velsen 1871, p. 4 et
  31–43, montre que plus de la moitié des divergences R/Iunt. notées par Enger sont illusoires.
- DP : oui. URL : https://www.digitale-sammlungen.de/view/bsb10232531 ; préface de *Lys.* :
  https://www.digitale-sammlungen.de/view/bsb10232530.
- Fichiers : `ED/1844_Bonn_Enger/bsb10232531.pdf` (212 vues ; p. n = PDF n+6 ; OCR Tesseract lat+grc :
  `.travail/editions_reprise/pages/1844_Bonn_Enger__bsb10232531.pdf.json.gz`) ; préface de *Lys.* :
  `ED/1844_Bonn_Enger_Lysistrata_praefatio/bsb10232530_praefatio.pdf` (36 vues = p. I–XXVIII, 1–8).
  *Thesm.* : préface PDF 5–6 ; texte, scholies et notes PDF 7–211 = p. 1–205. Notes dépouillées dans
  `edition/donnees/repertoire_critique/enger1844_*.jsonl`.

**E31. 1845 — F. H. Bothe, Leipzig (2ᵉ éd.).**
- Réf. : *Aristophanis comoediae. Recensuit et annotatione instruxit Fridericus Henricus Bothe*, editio
  secunda emendatior, Lipsiae, Hahn, 1845, t. III (*Lysistrate, Thesmophoriazusae, Ranae*) (B3Kat).
- Nature : T, notes brèves. Base : p. 102 (PDF 111) : « Rarissima sunt scripta exemplaria huius dramatis,
  quod Brunckius e solo codice Augustano, Bekkerus e solo Ravennate, emendavit » : G d'après Brunck, R
  d'après Bekker. DP : oui. URL : https://archive.org/details/aristophaniscom00bothgoog.
- Fichier : `ED/1845_Leipzig_Bothe2_t3/aristophaniscom00bothgoog.pdf` (649 vues). *Thesm.* : PDF 108–191 =
  p. 97–184 (*Gren.* p. 185 = PDF 192).

**E32. 1848 ; 1868 — Hubert Ashton Holden, Cambridge–Londres.**
- Réf. : *Aristophanis comoediae quae supersunt cum perditarum fragmentis*, ed. H. A. Holden, 3ᵉ éd. en un
  volume, 1868 (exemplaire local daté 1867 par IA) ; 1ʳᵉ éd. 1848 [à vérifier].
- Nature : T (avec résumés et descriptions métriques). Base : éditions antérieures. DP : oui.
- URL : https://archive.org/details/aristophaniscom01arisgoog.
- Fichier : `ED/1868_Cambridge_Holden/aristophaniscom01arisgoog.pdf` (898 vues ; OCR médiocre).
  *Thesm.* : PDF 546–592 = p. 455–501 (« summarium » p. 455–457, personnages p. 458, texte p. 458–501 ;
  descriptions métriques p. 503 sqq.).

**E33. 1852 ; 1872 — Theodor Bergk, Leipzig (Teubner).**
- Réf. : *Aristophanis comoedias edidit Theodorus Bergk*, Lipsiae, Teubner, 1852, 2 vol. (B3Kat : les *Thesm.*
  forment le fasc. « 2,3 ») ; *editio altera correctior* : t. I 1857, t. II 1872 (Prato 2001, p. XLV) ;
  retirages 1886–1888 (BnF cb45027406f), 1892 (B3Kat) ; tirages séparés des *Thesm.* 1891 et 1932
  (B3Kat ; E39).
- Nature : T ; la *Praefatio* du t. II (p. XII–XVI) donne pour les *Thesm.* les leçons modifiées et ses
  conjectures (« fort. »). Base : éditions antérieures. DP : oui.
- URL : https://archive.org/details/aristophaniscomo02aris (IA le date de 1867 à tort : la page de titre,
  PDF 5, porte « Vol. II … Editio altera correctior … MDCCCLXXII »).
- Fichier : `ED/1867_Leipzig_Bergk_t2/aristophaniscomo02aris.pdf` (360 vues ; **dossier mal daté : c'est le
  t. II de 1872**). *Thesm.* : PDF 153–196 = p. 123–166 ; préface PDF 16–20 = p. XII–XVI.

**E34. 1860 — August Meineke, Leipzig (Tauchnitz).**
- Réf. : *Aristophanis comoediae*, ed. Augustus Meineke, Lipsiae, Tauchnitz, 1860, 2 vol.
- Nature : T ; *adnotatio critica* en tête du t. II. Base : éditions antérieures. Voir aussi ses *Vindiciae
  Aristophaneae*, 1865 (`conjectures_sources.md`). DP : oui.
- URL : https://archive.org/details/aristophaniscom00meingoog.
- Fichier : `ED/1860_Leipzig_Meineke_t2/aristophaniscom00meingoog.pdf` (821 vues ; exemplaire interfolié de
  feuillets blancs, quelques notes manuscrites en anglais : deux vues par page imprimée). *Thesm.* :
  PDF 330–427 = p. 127–176 ; *adnotatio* PDF 36–45 = p. XVII–XXII.

**E35. 1869 — W. Dindorf, *Aristophanis fabulae*, Leipzig (Teubner).**
- Réf. : *Aristophanis fabulae superstites et perditarum fragmenta*, ex recensione Guilelmi Dindorfii [titre
  à vérifier], Lipsiae, in aedibus B. G. Teubneri, 1869 (texte sur deux colonnes, mise en page des *Poetae
  scenici*, 5ᵉ éd.).
- Nature : T. Base : éditions antérieures (Dindorf). DP : oui.
- URL : https://archive.org/details/aristophanisfab00dindgoog.
- Fichier : `ED/1869_Leipzig_Dindorf_Fabulae/aristophanisfab00dindgoog.pdf` (241 vues). *Thesm.* :
  PDF 130–144 = p. [121]–135 (*Gren.* p. 136).

**E36. 1878 — Adolf von Velsen, Sarrebruck.**
- Réf. : *Aristophanis Thesmophoriazusae*, recensuit Adolphus von Velsen, Saarbrücken, Hofer, 1878
  (B3Kat) ; Prato 2001, p. XLVI : « Lipsiae 1878 (Lipsiae 1883²) ».
- Nature : T (programme scolaire [à vérifier]). Base : R (autopsie : Velsen 1871, p. 3). DP : oui.
- URL : aucune numérisation trouvée. Fichier : —.

**E37. 1880 — Frederick H. M. Blaydes, Halle.**
- Réf. : *Aristophanis comoediae, annotatione critica, commentario exegetico, et scholiis Graecis instruxit
  Fredericus H. M. Blaydes*, pars I : *Thesmophoriazusae*, Halis Saxonum, in orphanotrophei libraria, 1880
  (B3Kat ; numérisation BSB `bsb11413137`) ; premier volume d'une série en 12 parties (1880–1893).
- Nature : T, notes critiques, commentaire, scholies. Base : p. VII (PDF 11) : « Ex his ipse verbatim et
  accurate contuli R. (cum ed. Bergk. 1857.) » ; liste des éditions anciennes p. VII–VIII. DP : oui.
- URL : https://archive.org/details/comoediaeblaydes01aris (Toronto) ; aristophaniscom01blaygoog.
- Fichiers : `ED/1880_Halle_Blaydes/comoediaeblaydes01aris.pdf` (290 vues ; OCR Tesseract des p. VI–VIII
  dans `.travail/recension_editions/R2/ocr/`) et `…/aristophaniscom01blaygoog.pdf` (332 vues). *Thesm.*
  (exemplaire de Toronto) : préface PDF 9–13 ; texte et notes critiques PDF 15–140 = p. 1–126 ;
  *Commentarius* PDF 141–273 = p. 127–259 ; *Addenda et corrigenda* PDF 274–285 = p. 260–271.

**E38. 1883 — Adolf von Velsen, Leipzig (Teubner).**
- Réf. : *Aristophanis Thesmophoriazusae*, recensuit Adolphus von Velsen, Lipsiae, in aedibus B. G.
  Teubneri, 1883 (dédicace « Societati philologae Bonnensi » ; préface datée « Hanoviae cal. iun.
  MDCCCLXXXIII »).
- Nature : T, apparat. Base : **R (autopsie)** et G ; la préface (p. 5–6) décrit R (mains R², R³, et celle
  d'Euphrosynus Boninus, non notée) et G (Monac. 492). Velsen a collationné R en Italie en 1866–1867
  (Velsen 1871, p. 3 : « während ich den Ravennas collationirte » ; p. 6 : notes prises « vor dem Codex
  selbst in Ravenna »). DP : oui.
- URL : https://archive.org/details/aristophanisthe00velsgoog (Harvard ; Google Books id 6jsTAAAAYAAJ) ;
  numérisation BSB `bsb11536315`.
- Fichiers : `ED/1883_Leipzig_Velsen/aristophanisthe00velsgoog.pdf` (97 vues ; couche texte inexploitable)
  ; trois copies sur le Drive, dont une avec un bon OCR :
  `.sources/drive/fichiers/Grec/Aristophane/Thesmophories/Aristophanis_Thesmophoriazusae Von Velsen 1883.txt`.
  *Thesm.* : préface PDF 10–11 = p. 5–6 ; texte et apparat PDF 12–93 = p. 7–88. Apparat dépouillé dans
  `edition/donnees/repertoire_critique/velsen1883_*.jsonl`.

**E39. 1891 — Th. Bergk, *Thesmophoriazusae*, Leipzig (Teubner), tirage séparé** (B3Kat ; retirage 1932).
T seul ; DP : oui ; pas de numérisation trouvée.

**E40. 1898 — Carl Hermann Weise, Leipzig (Holtze).**
- Réf. : *Aristophanis comoediae ad optimorum librorum fidem accurate rec. Carl Herm. Weise*, Lipsiae, Holtze,
  1898, t. 2 : *Pax, Aves, Lysistrata, Thesmophoriazusae*, 344 p. (B3Kat BV011749333) : retirage de l'édition
  stéréotype de Tauchnitz (E29b). T ; DP : oui ; pas de numérisation trouvée (le tirage de 1842 est local).

### 3.4. XXᵉ et XXIᵉ siècles (1901–2025)

**E41. 1901 ; 1907 — F. W. Hall et W. M. Geldart, Oxford (OCT).**
- Réf. : *Aristophanis comoediae, recognoverunt brevique adnotatione critica instruxerunt F. W. Hall,
  W. M. Geldart*, Oxonii, e typographeo Clarendoniano (*Scriptorum classicorum bibliotheca Oxoniensis*),
  t. I 1900, t. II 1901 ; 2ᵉ éd. t. I 1906, t. II 1907 ; réimpressions 1920, 1928, 1945, 1951, 1954, 1956,
  1959, 1962, 1967 (verso du titre de la réimpression locale, PDF 10).
- Nature : T, apparat bref. Base : **R d'après des photographies** : note de W. M. G. (novembre 1907) :
  « Sicut in volumine primo apparatum criticum ad exemplaria photographica codicum R et V examinavimus.
  Item fragmenta aliquot in appendice adiecimus quae ex novo codice Berolinensi, a R. Reitzenstein edito,
  nuperrime accesserunt ». DP : oui (Hall † 1933, Geldart † 1922).
- URL : https://archive.org/details/aristophaniscomo02arisuoft (Toronto) ; https://archive.org/details/bwb_P9-BTV-995_2.
- Fichiers : `ED/1907_Oxford_Hall_Geldart_t2/aristophaniscomo02arisuoft.pdf` (378 vues) : malgré le nom
  du dossier, **vraisemblablement la 1ʳᵉ éd. (1901)** : page de titre non datée, ni note de 1907 ni appendice
  des fragments de Photius ; `ED/1907_Oxford_Hall_Geldart_t2_ed2_reimpr/bwb_P9-BTV-995_2.pdf` (376 vues) :
  2ᵉ éd. (1907), réimpression de 1967 (note de 1907 PDF 10 ; appendice PDF 345). *Thesm.* : PDF 66–110
  dans les deux (personnages PDF 66 ; *Gren.* PDF 111) ; sigles PDF 12. Texte TEI de Perseus fondé sur
  cette édition : Drive, `Thesmophories/Perseus_text_1999.01.0041.xml`.

**E42. 1904 — Jan van Leeuwen, Leyde (Sijthoff).**
- Réf. : *Aristophanis Thesmophoriazusae cum prolegomenis et commentariis edidit J. van Leeuwen J. f.*,
  Lugduni Batavorum, apud A. W. Sijthoff, 1904 (B3Kat) ; réimpr. 1968.
- Nature : T, commentaire latin, notes critiques brèves. Base : R, dont les notes distinguent les mains
  (« corrector », « manus recens » : p. 1–2) ; la même année, van Leeuwen préface le fac-similé
  phototypique de R chez le même éditeur (*Aristophanis comoediae undecim cum scholiis. Codex Ravennas
  137, 4, A*, Leyde, 1904 ; Prato 2001, p. LXVII ; `recherche/ravennas_dossier.md` § 13). DP : oui
  († 1924).
- URL : https://archive.org/details/aristophanisthe00leeugoog.
- Fichier : `ED/1904_Leyde_van_Leeuwen/aristophanisthe00leeugoog.pdf` (185 vues). Prolégomènes PDF 10–25 =
  p. I–XVI ; texte et commentaire PDF 26–179 = p. 1–154. Ses *Prolegomena ad Aristophanem* (1908) :
  `ED/1908_Leyde_van_Leeuwen_Prolegomena/`.

**E43. 1904 ; 1924 — Benjamin Bickley Rogers, Londres.**
- Réf. : Ἀριστοφάνους Θεσμοφοριάζουσαι. *The Thesmophoriazusae of Aristophanes, acted at Athens in the year
  B.C. 410 ; the Greek text revised, with a free translation into English verse, introduction and
  commentary by Benjamin Bickley Rogers*, London, G. Bell and Sons, 1904 (B3Kat ; réimpr. 1920 ; repris en
  1911 dans *The Comedies of Aristophanes*, t. IV) ; texte et traduction repris dans *Aristophanes, with the
  English translation of Benjamin Bickley Rogers*, t. III (*Lysistrata, Thesmophoriazusae, Ecclesiazusae,
  Plutus*), London–New York, Heinemann–Putnam (Loeb Classical Library), 1924 (réimpr. 1955, 1963, 1972,
  1979, 1991 : B3Kat).
- Nature : T, Tr. angl. en vers, introduction, commentaire, appendice critique (1904) ; T et Tr. (Loeb).
  Base : éditions antérieures [mode non précisé]. DP : oui († 1919).
- URL : https://archive.org/details/thesmophoriazus00rogegoog ; https://archive.org/details/aristophaneswith03arisuoft.
- Fichiers : `ED/1904_Londres_Rogers/thesmophoriazus00rogegoog.pdf` (285 vues) : introduction PDF 11–47,
  texte et traduction PDF 50–227, appendice PDF 228–281 ; `ED/1924_Londres_Rogers_Loeb_t3/aristophaneswith03arisuoft.pdf`
  (496 vues) : *Thesm.* PDF 135–252 = p. 125–242 (*Assemblée* p. 243). Copies sur le Drive.

**E44. 1928 — Victor Coulon et Hilaire Van Daele, Paris (CUF).**
- Réf. : *Aristophane*, t. IV : *Les Thesmophories. Les Grenouilles*, texte établi par Victor Coulon et
  traduit par Hilaire Van Daele, Paris, Les Belles Lettres (Collection des Universités de France), 1928,
  158 p. (texte grec doublant les p. 16–71) ; tirages 1942, 1954, 1962 (5ᵉ), 1967 (6ᵉ), 1973, 1991, 2012
  (11ᵉ) (BnF cb315290704 et suivantes ; B3Kat).
- Nature : T, apparat, Tr. fr., notice. Base : R (sigle « R = Ravennas 137, 4 A, saec. X ») ; mode de
  collation [à vérifier dans le t. I, 1923]. DP : non.
- Fichiers : Drive (volume complet, `Thesmophories/Coulon Les Thesmophories - Les Grenouilles…pdf`) ;
  pages grecques seules : `.sources/drive/fichiers/Grec/Aristophane/Œuvres complètes/Gec_seulement_Les Thesmophories…pdf` ;
  extrait textuel : `.sources/drive/ravennas/Coulon_1928_Thesm_Grenouilles_textrep.txt`. Prato 2001
  (p. XXXVI–XXXIX) donne la liste de ses divergences d'avec Coulon.

**E45. 1956 — Raffaele Cantarella, Milan.**
- Réf. : *Aristophanis comoediae quae extant*, recognovit, adnotatione critica instruxit, Italice reddidit
  R. Cantarella, Milano, Istituto Editoriale Italiano, 1949–1964, 5 vol. ; *Thesm.* au t. IV, 1956 (Prato
  2001, p. XLVI). Nature : T, A, Tr. it. DP : non. Fichier : —.

**E45b. 1974 — Manuel Balasch, Barcelone (Fundació Bernat Metge).**
- Réf. : *Aristòfanes, Comèdies*, vol. V : *Les Tesmofòries. Les Granotes*, text revisat i traducció de Manuel
  Balasch, Barcelona, Fundació Bernat Metge (n° 190 de la collection), 1974, 185 p. (Prato 2001, p. XLVI ;
  numéro, pagination et ISBN 9788472250994 d'après une notice de libraire en ligne).
- Nature : texte grec révisé et traduction catalane en regard (présentation habituelle de la collection)
  [à vérifier sur l'exemplaire]. Base : [à vérifier]. DP : non. Fichier : —.

**E46. 1983 — Guido Paduano, Milan (BUR).**
- Réf. : *Aristofane, La festa delle donne*, introduzione, traduzione e note di G. Paduano, Milano, BUR,
  1983 (Prato 2001, p. XLVII). Nature : T (celui de Coulon, retouché ; `recherche/drive_ressources.md` § 6),
  Tr. it., notes. DP : non. Fichier : Drive (`Thesmophories/Le donne alle Tesmoforie (… Paduano …).pdf`) ;
  copie locale : `.sources/drive/fichiers/Grec/Aristophane/Thesmophories/Le donne alle Tesmoforie (Aristofane, Guido Paduano (editor)) (z-lib.org).pdf`.

**E47. 1988 — Joseph F. Gannon, Bryn Mawr.**
- Réf. : *Aristophanes' Thesmophoriazusae*, ed. by Joseph F. Gannon, Bryn Mawr (Pa.), Thomas Library, Bryn
  Mawr College (Bryn Mawr Greek Commentaries) (B3Kat ; Prato 2001, p. XLVI : « Text, Bryn Mawr,
  Pennsylvania 1988 »). Précédé de *Thesmophoriazusae restitutae. An Essay in Annotation and
  Interpretation*, diss. Yale, 1982 (UMI 1982 et 1986 ; B3Kat). Nature : T [notes ? à vérifier]. DP : non.
  Fichier : —.

**E48. 1994 — Alan H. Sommerstein, Warminster.**
- Réf. : *Aristophanes, Thesmophoriazusae*, edited with translation and notes by Alan H. Sommerstein,
  Warminster, Aris & Phillips, 1994 (*The Comedies of Aristophanes*, vol. 8), XII-237 p. (BnF
  cb35711962r) ; réimpr. corrigée 2001 (B3Kat).
- Nature : T, apparat, Tr. angl., commentaire. Base : R [mode de collation à vérifier]. DP : non.
- Fichier : Drive (`Thesmophories/Sommerstein … vol. 8 Thesmophoriazusae….pdf`) ; extrait textuel :
  `.sources/drive/ravennas/Sommerstein_1994_Thesm_textrep.txt`.

**E49. 2000 — Jeffrey Henderson, Cambridge (Mass.), Loeb.**
- Réf. : *Aristophanes* [III] : *Birds ; Lysistrata ; Women at the Thesmophoria*, edited and translated by
  Jeffrey Henderson, Cambridge (Mass.), Harvard University Press (Loeb Classical Library), 2000, VI-618 p.
  (BnF cb39193461p) ; réimpr. corrigée 2018 (B3Kat). Nature : T, Tr. angl. DP : non. Fichier : —.

**E50. 2001 — Carlo Prato et Dario Del Corno, Milan (Fondazione Valla).**
- Réf. : *Aristofane, Le donne alle Tesmoforie*, a cura di Carlo Prato, traduzione di Dario Del Corno,
  Milano, Fondazione Lorenzo Valla – Mondadori, 2001, LXXXV-372 p. (BnF cb39242238h).
- Nature : T, apparat, Tr. it., commentaire, bibliographie (dont la liste des « Contributi filologici »
  utilisée pour `conjectures_sources.md`). Base : R ; doutes paléographiques résolus par M. D'Agostino et
  G. Prato « sul microfilm o sull'esemplare ravennate » ; apparat relu par C. Austin (p. XXXVI). DP : non.
- Fichier : Drive (`Thesmophories/Prato LeDonAllTes.pdf`) ; extrait textuel :
  `.sources/drive/ravennas/Prato_2001_LeDonneAlleTesmoforie_textrep.txt`.

**E51. 2003 — Benedetto Marzullo, Rome (Newton & Compton).**
- Réf. : *Aristofane, Le commedie : Acarnesi, Cavalieri, Nuvole, Vespe, Pace, Uccelli, Tesmoforiazuse,
  Lisistrata, Rane, Ecclesiazuse, Pluto*, traduzione scenica, testo greco integralmente rinnovato e
  appendice critica di Benedetto Marzullo, Roma, Newton & Compton (Grandi tascabili economici), 2003
  (B3Kat ; Bevegni 2024 : `.sources/web/biblio_tiers/Bevegni_Aristofane_indicazioni_bibliografiche_2024.pdf`).
  Nature : T, appendice critique, Tr. it. DP : non. Fichier : —. (Traduction seule : Bari, Laterza, 1968 ;
  § 5.)

**E52. 2004 — Colin Austin et S. Douglas Olson, Oxford.**
- Réf. : *Aristophanes, Thesmophoriazusae*, edited with introduction and commentary by Colin Austin and
  S. Douglas Olson, Oxford, Oxford University Press, 2004, CVI-363 p. (BnF cb39929872t) ; éd. de poche
  2009 (BnF cb445265213).
- Nature : T, apparat, introduction, commentaire. Base : R [mode de collation à vérifier : la section sur
  le texte n'est pas dans l'extrait local]. DP : non.
- Fichier : Drive (`Thesmophories/Aristophanes Thesmophoriazusae by Colin Austin, S. Douglas Olson (z-lib.org).pdf`) ;
  extrait des p. i–lxxix : `.sources/drive/ravennas/AustinOlson_2004_Thesm_textrep.txt`.

**E53. 2006 — Giuseppe Mastromarco et Piero Totaro, Turin (UTET).**
- Réf. : *Commedie di Aristofane*, a cura di Giuseppe Mastromarco e Piero Totaro, vol. II [*Uccelli,
  Lisistrata, Tesmoforiazuse, Rane*], Torino, UTET (Classici greci), 2006, 709 p. (B3Kat, notice de compte
  rendu ; contenu d'après Bevegni 2024, fichier cité en E51). Vol. I (Mastromarco seul) : 1983, rééd. 2007.
- Nature : T, Tr. it., notes, commentaire. DP : non. Fichier : Drive (26 Mo ; `recherche/drive_ressources.md`)
  [non encore copié].

**E54. 2007 — Nigel G. Wilson, Oxford (OCT).**
- Réf. : *Aristophanis fabulae*, recognovit brevique adnotatione critica instruxit N. G. Wilson, Oxonii, e
  typographeo Clarendoniano, 2007, 2 vol. (t. II : *Lysistrata, Thesmophoriazusae, Ranae, Ecclesiazusae,
  Plutus*) ; accompagné de *Aristophanea. Studies on the Text of Aristophanes*, Oxford, 2007.
- Nature : T, apparat (avec beaucoup de conjectures). Base : préface, t. I, p. vi : rapports publiés,
  vérifiés sur de nombreux points ; « even the Ravenna manuscript, which can be easily consulted in the
  facsimile … had not been correctly reported in all passages » ; p. viii : « no one has taken the trouble
  to compile a repertory of conjectures on the text of this author ». DP : non.
- Fichiers : `.sources/drive/editions/Wilson I …pdf` (435 p.) et `Wilson II …pdf` (328 p., images sans
  couche texte, sans la préface : *Thesm.* PDF 69–126, papyrus et sigles PDF 70, hypothesis PDF 71,
  personnages PDF 72, *Gren.* PDF 127) ; extrait océrisé partiel « Wilson II pp 50-140 … ocred » ; OCR des
  pages liminaires du t. I : `.travail/recension_editions/B_wilson/`.

**E55. 2016 — Rossella Saetta Cottone, Paris (De Boccard).**
- Réf. : *Les Thesmophories ou La fête des femmes*, Aristophane ; texte et traduction nouvelle de Rosella
  [sic] Saetta Cottone, avec la collaboration de Martin Djidou ; introduction et commentaire de Rossella
  Saetta Cottone, Paris, Éditions de Boccard, 2016, 318 p. (BnF cb45023182r). Nature : T, Tr. fr., I, C.
  DP : non. Fichier : —.

**E56. 2025 — Loredana Di Virgilio, Pise–Rome (F. Serra).**
- Réf. : *Aristofane, Tesmoforiazuse. I canti*, a cura di Loredana Di Virgilio, Pisa–Roma, Fabrizio Serra
  editore, 2025 (B3Kat). Nature : T des parties lyriques, analyse métrique, commentaire. DP : non.
  Fichier : —.

### 3.5. Éditions anciennes qui ne contiennent pas les *Thesmophories*

Pour mémoire, et pour éviter les confusions de catalogue : l'Aldine (Venise, 1498 ; neuf pièces) ; la
Juntine de septembre 1515 (neuf pièces ; fichier local ci-dessus, E01) ; la Juntine de 1525 (éd. A.
Francini, neuf pièces avec scholies ; BnF cb30027111d ; BSB `bsb10150262`) ; la Juntine de 1540 (B. Giunta,
neuf pièces ; BnF cb30027117g) ; l'édition de Gourmont (Paris, 1528, neuf pièces ; Blaydes 1880, p. VII) ;
*Plutus, Nubes, Ranae* de C. Néobar (Paris, 1540 ; BnF cb317299881) ; les cinq comédies latines de N.
Frischlin (Francfort, 1586 et 1597 ; BnF cb30027121q). Prato (2001, p. XXXII) rappelle que les Giunta ne
réimprimèrent jamais les *Thesm.* après 1516.

## 4. Commentaires séparés, notes *variorum*, scholies et travaux préparatoires

Commentaires publiés hors des éditions du § 2, recueils de notes, éditions et traductions des scholies,
monographies critiques consacrées à la pièce. Les recueils de conjectures (Dobree, Porson, Cobet, Meineke,
Blaydes, van Herwerden…) sont décrits critique par critique dans `recherche/conjectures_sources.md` ; les
éditions des scholies, plus en détail, dans `recherche/scholies.md`.

| Date | Auteur | Titre, lieu | Nature | Fichier local (ED/…) ou URL | *Thesm.* |
|---|---|---|---|---|---|
| 1777 | F. J. G. La Porte du Theil | « Recherches sur les Thesmophories, pour servir de prolégomène à la comédie d'Aristophane… » (BnF cb38691177g) ; réimpr. dans Invernizi t. VIII (1821) | étude (fête, rites) | `1821_Leipzig_Invernizi_t8_commentaire_Thesm/comoediae08aris.pdf` | p. 513–553 = PDF 525–565 |
| 1820 | A. Wellauer | *De Thesmophoriis dissertatio*, Vratislaviae (Breslau) | dissertation ; extraits dans Invernizi t. VIII, p. 504 sqq. (Enger 1844, p. VI) | — (extraits : même fichier) | — |
| 1821 | W. Dindorf (éd.) | Invernizi–Beck–Dindorf, t. VIII = *Commentarii* VI (*Lys.*, *Thesm.*), Leipzig, Weidmann | notes *variorum* (Brunck, Küster, Bergler, Reiske, Dobree, Reisig, Bentley…) ; préface (p. V–VI) avec bibliographie | `1821_Leipzig_Invernizi_t8_commentaire_Thesm/comoediae08aris.pdf` | p. 290–512 = PDF 302–524 ; préface PDF 11–12 |
| 1823 | W. Dindorf (éd.) | Invernizi–Beck–Dindorf, t. XI = *Scholia Graeca* II, Leipzig | scholies de Biset et de Bourdin aux *Thesm.* (d'après 1607) | `1823_Leipzig_Invernizi_t11_scholies_Biset/comoediae11aris.pdf` | Biset p. 198–270 = PDF 210–282 ; Bourdin p. 271–333 = PDF 283–345 |
| 1829 | I. Bekker (éd.) | *Aristophanis comoediae* … t. IV : *Notae variorum in Pac., Av., Thesm., Lys.*, Londres | notes *variorum* | `1829_Londres_Bekker_t4_notes/aristophanouskm01bekkgoog.pdf` | p. 253–329 = PDF 252–328 |
| 1834 | (Invernizi–Beck–Dindorf) | t. IX, 2ᵉ partie : scholies des *Thesm.* réimprimées d'après l'édition de Londres (Rutherford 1896, I, p. XIV n., cité dans `recherche/scholies.md`) | scholies | — | — |
| 1837 | W. Dindorf | *Aristophanis comoediae*, t. III : *Annotationes*, Oxford | notes *variorum* et de Dindorf | `1837_Oxford_Dindorf_t3_annotationes/aristophans00unkngoog.pdf` | p. 701–756 = PDF 710–765 |
| 1838 | G. Hermann | compte rendu de Fritzsche, *Zeitschrift für die Alterthumswissenschaft* 5 (1838), col. 672–693 (Prato 2001, p. LXXI) | conjectures | `1838_ZfAW_5_Hermann_Fritzsche/` | PDF 341–353 = col. 670–693 (deux colonnes par page : PDF n = col. 2n−13 et 2n−12) |
| 1841 | J. Zastra | *Ueber den Zweck von Aristophanes Thesmophoriazusen*, Breslau, Kupfer (B3Kat) | étude | — | — |
| 1842 | Fr. Dübner | *Scholia Graeca in Aristophanem*, Paris, Didot | scholies, *adnotatio* | `1842_Paris_Dubner_scholia/scholiagraecain00unkngoog.pdf` | p. 264–272 = PDF 343–353 ; *adnotatio* PDF 636–641 |
| 1843 | R. Enger | « Beiträge zur Kritik und Erklärung der Thesmophoriazusen des Aristophanes und der Scholien zu diesem Stücke », *RhM* N. F. 2 (1843) | conjectures, exégèse | `1843_Enger_Beitraege_RhM/41250706.pdf` | 26 p. |
| 1845 | G. Hermann | compte rendu d'Enger, *ZfAW* 1845, col. 905–920 = *Opuscula* VIII, Leipzig, 1877, p. 288–308 | conjectures | `1877_Hermann_Opuscula_VIII/opuscula07hermuoft.pdf` ; copie Drive | *Opuscula* VIII, p. 288–308 = PDF 740–760 |
| 1846 | R. Enger | « Zu Aristophanes Thesmophoriazusen », *RhM* N. F. 4 (1846) | date, critique | `1846_Enger_Zu_Thesm_RhM/41250353.pdf` | 28 p. |
| 1865 | A. von Velsen | « Zur Kritik des Aristophanes », *RhM* 20 (1865), p. 390–400 | critique | `articles_jstor/41249869.pdf` | — |
| 1865 | M. Bamberg | *De Ravennate et Veneto Aristophanis codicibus*, Bonn | manuscrits | `1865_Bonn_Bamberg/deravennateetven00bambuoft.pdf` | — |
| 1871 | A. von Velsen | *Über den Codex Urbinas der Lysistrata und der Thesmophoriazusen des Aristophanes*, Halle | identification R = *Urbinas* de la Juntine ; collation R/Iunt. | `1871_Halle_Velsen_Codex_Urbinas/berdencodexurbi00velsgoog.pdf` | p. 1–53 = PDF 9–61 |
| 1878 | O. Bachmann | *Conjecturarum observationumque Aristophanearum specimen* I, diss. Göttingen | conjectures | `1878_Goettingen_Bachmann/` | — |
| 1878 | O. Bünger | *De Aristophanis Equitum, Lysistratae, Thesmophoriazusarum apud Suidam reliquiis*, Strasbourg | tradition indirecte | `1878_Strasbourg_Buenger/` | — |
| 1882 | A. Martin | *Les scolies du manuscrit d'Aristophane à Ravenne*, Paris | scholies de R | `1882_Paris_Martin_scolies_Ravenne/` | — |
| 1888 | K. Zacher | *Die Handschriften und Classen der Aristophanesscholien*, Leipzig (*Jahrb. f. class. Philol.*, Suppl. 16) | scholies | `1888_Leipzig_Zacher/` | — |
| 1891 | G. Lange | *Quaestiones in Aristophanis Thesmophoriazusas*, diss. Göttingen | critique | `1891_Goettingen_Lange/quaestionesinari00lang.pdf` | — |
| 1896 | W. G. Rutherford | *Scholia Aristophanica* II, Londres | scholies de R, traduites | `1896_Londres_Rutherford_t2/scholiaaristoph00ruthgoog.pdf` | p. 441–509 = PDF 452–520 |
| 1904 | J. van Leeuwen (préf.) | *Aristophanis comoediae undecim cum scholiis. Codex Ravennas 137, 4, A*, Leyde, Sijthoff (fac-similé) | fac-similé de R | `ravennas_1904_bnf/` (planches) ; Drive | ff. 162v–177r |
| 1908 | A. Willems | « Notes sur les *Thesmophories* », *Bull. de l'Acad. royale de Belgique* 1908 = Willems 1919, t. III, p. 535–582 (Prato 2001, p. LXXV) | notes critiques | Drive (Willems 1919, t. III) | — |
| 1982 | J. F. Gannon | *Thesmophoriazusae restitutae. An Essay in Annotation and Interpretation*, diss. Yale (UMI 1982, 1986) | commentaire | — | — |
| 1987 ; 1990 | C. Austin | « Textual Problems in Ar. *Thesm.* », *Dodone* 16.2 (1987), p. 61–92 ; « Observations critiques sur les *Thesmophories* d'Aristophane », *Dodone* 19.2 (1990), p. 9–29 | conjectures, humanistes | `.sources/drive/thesmophories/Austin_1987.txt` ; Drive | — |
| 2007 | R. F. Regtuit | *Scholia in Aristophanem* III : *Scholia in Thesmophoriazusas, Ranas, Ecclesiazusas et Plutum*, fasc. 2/3 *continens Scholia in Aristophanis Thesmophoriazusas et Ecclesiazusas*, Groningue (Egbert Forsten), 2007, 131 p. (B3Kat ; comptes rendus de 2008) | seule édition critique moderne des scholies | — | — |
| 2023 | C. Germain | *Scholies aux « Thesmophories » d'Aristophane : traduction et commentaire*, Grenoble, UGA Éditions (B3Kat) | scholies traduites | — | — |

Les commentaires intégrés aux éditions sont signalés au § 2 (nature « C ») : Küster 1710, Bergler 1760,
Brunck 1783, Thiersch 1832, Fritzsche 1838, Enger 1844, Blaydes 1880, van Leeuwen 1904, Rogers 1904,
Sommerstein 1994, Prato 2001, Austin–Olson 2004, Mastromarco–Totaro 2006, Saetta Cottone 2016,
Di Virgilio 2025 (parties lyriques).

## 5. Traductions (par langue)

Colonne « Contrôle » : notice de catalogue (BnF, B3Kat), numérisation consultée (IA, Gutenberg) ou
bibliographie imprimée (Prato 2001, § 3 *Traduzioni*, p. XLVI–XLVII). Les traductions jointes à une édition
du texte (§ 2) sont rappelées par leur numéro E…. La recension n'est pas close pour les langues autres que
le latin, l'italien, le français, l'allemand et l'anglais (§ 7).

### 5.1. Latin

| Date | Traducteur | Titre, lieu, éditeur | Contrôle | Fichier / URL |
|---|---|---|---|---|
| 1538 | Andreas Divus | *Aristophanis comicorum principis comoediae undecim, e Graeco in Latinum ad verbum translatae*, Venise, Jacob a Burgofrancho, 260 f. | BnF cb38754911t | — |
| 1539 | A. Divus | même titre, Bâle, in aedibus Andreae Cratandri, 560 p. | BnF cb38691121v | `ED/1539_Bale_Divus_traduction_latine/bub_gb_x2Q6rpYwY2sC.pdf` : *Thesm.* PDF 479–524 = p. 467–512 (cahier p. 507–510 relié en désordre ; doublon PDF 526–537) |
| 1597 | A. Divus | *Comoediae Aristophanis … e Graeco in Latinum ad verbum translatae*, Venise, J. B. et J. B. Sessa, 543 p. | BnF cb386911226 | — |
| v. 1570 | Nicasius Ellebodius | *Aristophanis Thesmophoriazusae et Lysistrata Latine redditae cum scholiis*, manuscrit autographe (Milan, Ambrosienne) | Austin 1987, p. 64–65 ; Prato 2001, p. LXX (scholies des *Thesm.* ff. 75–85, version latine ff. 130 sqq. [foliotation à vérifier : extrait OCR défectueux]) | inédit |
| 1607 | Aem. Portus | version latine de l'édition de Genève (E11) | — | `ED/1607_…` |
| 1670 | (Divus) | version de Divus reprise par Ravestein (E13) | — | `ED/1670_Amsterdam_Ravestein_t2/` |
| 1710 | L. Küster | nouvelle version latine (E14) | — | `ED/1710_Amsterdam_Kuster/` |
| 1760 | St. Bergler | version latine (E15) | — | `ED/1760_Leyde_Bergler_Burman_t2/` |
| 1783 | R. F. Ph. Brunck | version latine (E16) ; reprise et adaptée dans Bekker 1829, t. II (E22) et Didot 1838 (E29) | — | `ED/1783_…`, `ED/1829_Londres_Bekker_t2_scholies/` (p. 147–166), `ED/1838_Paris_Didot_Dindorf/` |

### 5.2. Italien

| Date | Traducteur | Titre, lieu, éditeur | Contrôle | Fichier / URL |
|---|---|---|---|---|
| 1545 | Bartolomeo et Pietro Rositini | *Le Comedie del facetissimo Aristofane, tradutte di greco in lingua commune d'Italia*, Venise, V. Valgrisi (« Vaugris ») ; *Thesm.* = « Le Cereali, comedia X » | BnF cb30027161z | `ED/1545_Venise_Rositini_traduction_italienne/bsb10169312.pdf` : PDF 513–563 = f. 254r–279r |
| s. d. | Domenico Capellina | *Commedie di Aristofane tradotte dal professore Domenico Capellina*, Turin, Stamperia Reale | B3Kat [date et contenu à vérifier] | — |
| 1904 | Ettore Romagnoli | *Le Tesmoforiazuse d'Aristofane*, versione poetica con introduzione e note, Piacenza, A. Del Maino | notice reprise par Open Library (OL42930614W) | — |
| 1905 | Augusto Franchetti | *Aristofane, Le donne alle Tesmoforie*, introd. e note di D. Comparetti, Città di Castello | Prato 2001, p. XLVII | — |
| 1907 | Ettore Romagnoli | *Aristofane, Le commedie, tradotte in versi italiani*, Turin ; rééd. (5 vol.) : *Thesm.* au t. IV (Milan, ISEI, 1956 : « Gli uccelli. Lisistrata. Le tesmoforiazuse ») | Prato 2001, p. XLVII ; B3Kat | — |
| 1956 | R. Cantarella | traduction jointe à l'édition (E45) | Prato 2001, p. XLVI | — |
| 1968 | Benedetto Marzullo | *Aristofane, Le commedie*, Bari, Laterza (3ᵉ éd. 1982 ; t. 2 : *Vespe, Pace, Uccelli, Tesmoforiazuse*, 1977, 1982) ; nouvelle éd. avec texte grec, Rome, Newton & Compton, 2003 (E51) | Prato 2001, p. XLVII ; B3Kat | — |
| 1983 | Guido Paduano | *Aristofane, La festa delle donne*, Milan, BUR (E46) | Prato 2001, p. XLVII | Drive |
| 2001 | Dario Del Corno | traduction de l'édition Prato (E50) | BnF | Drive |
| 2006 | G. Mastromarco | traduction du vol. II UTET (E53) | Bevegni 2024 | Drive |

### 5.3. Français

| Date | Traducteur | Titre, lieu, éditeur | Contrôle | Fichier / URL |
|---|---|---|---|---|
| 1784 | Louis Poinsinet de Sivry | *Théâtre d'Aristophane, traduit en français, partie en vers, partie en prose, avec les fragments de Ménandre et de Philémon*, Paris, Didot jeune, 4 vol. (rééd. 1788 ; Desray, 1790) : « Les Fêtes de Cérès, comédie en cinq actes », t. III, p. 205 sqq. (notice p. 206) | BnF cb300271493, cb47656021x ; OCR d'archive.org (`bub_gb_A4lqXgnAl58C`, 1784, vues 211-215 ; aussi `thatredaristoph01sivrgoog`, 1790) | https://archive.org/details/bub_gb_A4lqXgnAl58C |
| 1785–1789 | « M. *** » (A.-Ch. Brotier) | *Théâtre des Grecs, par le P. Brumoy*, nouvelle éd., Paris, t. XII : « Les Thesmophories, ou les fêtes de Cérès et de Proserpine », extrait du P. Brumoy, puis « la même, traduite en entier par M. *** » ; traduction attribuée à Brotier et réimprimée sous le nom de Brotier, revue par L. Humbert, *Théâtre d'Aristophane*, Paris, Garnier, 1882 | table du t. XII (IA thtredesgrec12brum) ; Dindorf 1821, préface p. VI (« Gallica versio legitur in eodem Theatri a Brumoeo editi volumine quo Lysistrata ») ; BnF cb30027156c (1882) | https://archive.org/details/thtredesgrec12brum |
| 1830 | [Nicolas-Louis] Artaud | *Comédies d'Aristophane, traduites du grec*, Paris, Brissot-Thivars, 6 vol. ; 2ᵉ éd. Lefèvre–Charpentier, 1841 : « Les Thesmophories, ou Fêtes de Cérès et de Proserpine », p. 363-402 (notice p. 361, note p. 403) ; 4ᵉ éd. F. Didot, 1855 | BnF cb300271509, cb38691127x, cb30027151n ; 2ᵉ éd. contrôlée sur l'OCR d'archive.org (`bub_gb_YW6O6V9BMlUC`, table des matières et titre de la pièce) | https://archive.org/details/bub_gb_YW6O6V9BMlUC |
| 1860 | C. Poyard | *Aristophane, traduction nouvelle, avec une introduction et des notes*, Paris, Hachette (2ᵉ éd. 1869 ; 4ᵉ 1873 ; 11ᵉ 1903, *Œuvres complètes*) | BnF cb300271520, cb386911288, cb36583211n, cb31729897q ; traduction des *Thesm.* citée par Coulon, *REG* 50 (1937), p. 456 (vv. 126-127) | — |
| 1862 | Amédée Fleury | *Comédies d'Aristophane, essai de traduction*, Paris, Garnier (1864, 1869 avec une table de A. Feuillemorte) | BnF cb30027153b [contenu à vérifier] | — |
| 1889 | Charles Zévort | *Comédies d'Aristophane, traduction nouvelle, avec une introduction et des notes* (achevée et publiée par J. Denis), Paris, Charpentier | BnF cb30027157q [contenu à vérifier] | — |
| 1897 | Eugène Talbot | *Aristophane, traduction nouvelle*, préface de Sully Prudhomme, Paris, Lemerre, 2 vol. ; t. II : « Thesmophoriazouses, ou Les femmes aux fêtes de Dèmètèr » | BnF cb300271582 ; Project Gutenberg n° 20664 (t. II) | https://www.gutenberg.org/ebooks/20664 |
| 1919 | Alphonse Willems | *Aristophane. Traduction avec notes et commentaire critiques*, éd. revue par Ch. Lacomblé et L. Leclère, préface de L. Parmentier, Paris–Bruxelles, 3 vol. (*Thesm.* au t. III) | BnF cb31652128q ; Prato 2001, p. XLVII | Drive (t. I–III, numérisations HathiTrust) |
| 1928 | Hilaire Van Daele | traduction de la CUF (E44) | BnF | Drive |
| 1932–1933 | Marc-Jean Alfonsi | *Théâtre d'Aristophane, traduction nouvelle avec notices et notes*, Paris, Garnier, 2 vol. ; *Théâtre complet*, Garnier-Flammarion, 1966 et 1991 ; éd. augmentée, Flammarion, 2014 ; Classiques Garnier, t. II, 2025 (« les Oiseaux, Lysistrata, les Thesmophories, les Grenouilles, l'Assemblée des femmes, Ploutos ») | BnF cb38691129m, cb31729923f, cb32905972r, cb372823777, cb43910067x, cb48815485p | — |
| 1965–1966 | Victor-Henry Debidour | *Théâtre complet*, Paris, Le Livre de poche, t. 2 (« Les Oiseaux. Lysistrata. Les Thesmophories… ») ; Gallimard (Folio), 1987, t. 2 (1989) | BnF cb32905971d, cb377006633, cb37157061f | — |
| 1997 | Pascal Thiercy | *Théâtre complet*, Paris, Gallimard (Bibliothèque de la Pléiade) | BnF cb361877866 | — |
| 2016 | Rossella Saetta Cottone | traduction jointe à l'édition (E55) | BnF | — |

### 5.4. Allemand

| Date | Traducteur | Titre, lieu, éditeur | Contrôle | Fichier / URL |
|---|---|---|---|---|
| 1821 | Johann Heinrich Voss | traduction complète annoncée par Dindorf (Invernizi t. VIII, 1821, préface p. VI : « Novam Aristophanis fabularum versionem ab se factam nunc ipsum exspectare nos iubet Ioannes Henricus Vossius ») | [notice de catalogue à trouver] | — |
| 1835–1838 | Johann Gustav Droysen | *Des Aristophanes Werke*, Berlin, Veit, 3 vol. ; t. III (1838) : *Die Wolken. Lysistrate. Die Thesmophoriazusen. Die Ekklesiazusen. Die Frösche* ; rééd. Leipzig, Veit, 1869 et 1881, 2 vol. (réimpressions numériques De Gruyter « © 1869 », « © 1881 » : B3Kat) | B3Kat ; BnF cb30027160m | BSB `bsb10232563` (t. III ; IA 10232563bsb) |
| [1843–1846] | Hieronymus Müller | *Die Lustspiele des Aristophanes, übersetzt und erläutert*, Leipzig, Brockhaus | B3Kat [dates et tome à vérifier] | — |
| 1845–1848 | Ludwig Seeger | *Aristophanes*, Frankfurt am Main, Literarische Anstalt, 3 vol. ; t. III (1848) : *Lysistrate. Die Weiber am Thesmophorenfest. Plutos. Die Weibervolksversammlung. Die Fragmente* ; rééd. Stuttgart, Cotta, [vers 1890], [1910] | B3Kat | IA bub_gb_34FNAAAAYAAJ (t. I, 1845) |
| 1861–1862 | Johann Jakob Christian Donner | *Die Lustspiele des Aristophanes, deutsch in den Versmaßen der Urschrift*, Leipzig–Heidelberg, Winter, 3 vol. ; t. III (1862) : « Die Thesmophorienfeier » [titre lu sur un OCR défectueux] | B3Kat ; IA dielustspielede04donngoog, dielustspielede00donngoog | https://archive.org/details/dielustspielede04donngoog |
| s. d. | Jakob Mähly | *Aristophanes's Werke, übersetzt mit Einleitung und Anmerkungen*, Stuttgart–Berlin, Spemann | B3Kat [date et contenu à vérifier] | — |
| 1963 | L. Seeger, rév. Jürgen Werner | *Komödien in zwei Bänden*, Weimar, Volksverlag | B3Kat | — |
| 1963 | L. Seeger, introd. Otto Seel | *Komödien* 3 : *Die Weiber am Thesmophorenfest – Die Frösche – Die Weibervolksversammlung – Plutos*, Munich, Goldmann | B3Kat | — |
| 1968 | L. Seeger, rév. H.-J. Newiger et P. Rau | *Antike Komödien : Aristophanes*, Munich | Prato 2001, p. XLVII | — |
| 2011 | Niklas Holzberg | *Das Frauenfest*, übers. und hrsg., Stuttgart, Reclam | B3Kat | — |

### 5.5. Anglais

| Date | Traducteur | Titre, lieu, éditeur | Contrôle | Fichier / URL |
|---|---|---|---|---|
| 1837 | Charles Apthorp Wheelwright | *The Comedies of Aristophanes, translated into familiar blank verse, with notes*, Oxford, 2 vol. ; *Thesm.* au t. II | IA comediesofaristo02aris (texte, p. 235 sqq.) | https://archive.org/details/comediesofaristo02aris |
| 1853 | William James Hickie | *The Comedies of Aristophanes, a new and literal translation from the revised text of Dindorf*, Londres, Bohn, 2 vol. | BnF cb31729926g, cb31729927t [tome des *Thesm.* à vérifier] | — |
| 1904 ; 1924 | B. B. Rogers | traduction en vers (E43) ; Loeb, t. III | — | `ED/1904_Londres_Rogers/`, `ED/1924_Londres_Rogers_Loeb_t3/` |
| 1912 | anonyme (Athenian Society) | *Aristophanes, The Eleven Comedies*, Londres, Athenian Society, 2 vol. (t. I : … *The Thesmophoriazusae* …) ; rééd. New York, Liveright, 1928 | IA aristophaneselev0001vari_n0q0 ; BnF cb35360944x (1928) | https://archive.org/details/aristophaneselev0001vari_n0q0 |
| 1927–1934 | Arthur S. Way | *Aristophanes in English Verse*, Londres, Macmillan | B3Kat [tome à vérifier] | — |
| 1959 | Dudley Fitts | *Ladies' Day* (*Thesmophoriazusae*) | B3Kat (notice de 1960) | — |
| 1962 | (trad. diverses, éd. Moses Hadas) | *The Complete Plays of Aristophanes*, New York, Bantam Books (rééd. 1968) : contient les *Thesm.* | Open Library (OL31536086W) [traducteur des *Thesm.* à vérifier] | — |
| 1964 | David Barrett | *The Frogs and Other Plays* (*The Wasps, The Poet and the Women, The Frogs*), Harmondsworth, Penguin ; rév. Shomit Dutta, 2007 | B3Kat (éd. 2007) [contenu à vérifier] | — |
| 1994 | A. H. Sommerstein | traduction de l'édition (E48) | BnF | Drive |
| 1996 | Jeffrey Henderson | *Three Plays by Aristophanes : Staging Women*, New York, Routledge | BnF cb37103229h | — |
| 2000 | J. Henderson | Loeb (E49) | BnF | — |
| 2001 | anonyme, éd. W.-A. Landes | *The Women at the Festival of Demeter (Thesmophoriazusae)*, Studio City (Calif.), Players Press | B3Kat | — |
| 2010 | Michael Ewans | *Lysistrata, The Women's Festival, and Frogs*, Norman, University of Oklahoma Press | BnF cb425330766 | — |
| 2015 | Stephen Halliwell | *Aristophanes, Clouds, Women at the Thesmophoria, Frogs : A Verse Translation, with Introductions and Notes*, Oxford, OUP | B3Kat | Drive (`AR/Halliwel Aristophane…pdf`) |
| 2015 | Thomas L. Pangle | *Thesmophoriazusae [Women Celebrating the Festival of the Thesmophoria]*, traduction dactylographiée (PDF daté du 13 août 2015, 47 p.) | Drive (métadonnées du PDF) | `.sources/drive/fichiers/Grec/Aristophane/Thesmophories/Aristophanes_THESMOPORIAZUSAE_a_translat.pdf` |
| 2024 | Diane Arnson Svarlien (trad.), Ian C. Storey (introd. et notes) | *Aristophanes, Lysistrata, Women at the Thesmophoria, Frogs*, Indianapolis, Hackett (Hackett Classics), 416 p. | Open Library ; notice de l'éditeur (ISBN 9781647921859) | — |

### 5.6. Autres langues

| Langue | Date | Traducteur | Titre, lieu, éditeur | Contrôle |
|---|---|---|---|---|
| espagnol | 1880–1881 | Federico Baráibar y Zumárraga | *Comedias de Aristófanes*, Madrid (Biblioteca Clásica), 3 vol. ; *Thesm.* au t. III | IA comediasdearistf00aris (microfilm) |
| espagnol | 1962 ; 1966 | Ángel María Garibay K. | *Las once comedias*, versión directa del griego, México, Porrúa (« Sepan cuantos » ; « Tesmoforias ») | Open Library (OL15101025W, éd. 1966, 367 p., table des matières) |
| espagnol | 2013 | Luis Gil Fernández | *Aristófanes, Comedias* 3 : *Lisístrata. Las tesmoforiantes. Las ranas. Las asambleístas. Pluto*, Madrid, Gredos | B3Kat |
| espagnol | 2012 | [traducteur non relevé] | *Las tesmoforiantes*, Buenos Aires, Losada, 160 p. | Open Library (OL34988753W) [à vérifier] |
| catalan | 1974 | Manuel Balasch | *Aristòfanes, Comèdies* V : *Les Tesmofòries. Les Granotes*, Barcelone (Fundació Bernat Metge), texte révisé et traduction (E45b) | Prato 2001, p. XLVI ; notice de libraire |
| portugais | 1978 ; 2001 | Maria de Fátima Sousa e Silva | *As mulheres que celebram as Tesmofórias*, [Coimbra], 1978 ; Lisbonne, Edições 70, 2001 | B3Kat |
| portugais (Brésil) | 2005 | Adriane da Silva Duarte | *Duas comédias : Lisístrata e As tesmoforiantes*, São Paulo, Martins Fontes | Open Library (OL9158259M) ; bibliographies universitaires (date 2005 la plus fréquente) |
| grec moderne | 1978 | Ilías S. Papalás | Ἀριστοφάνους Θεσμοφοριάζουσαι, λογοτεχνικὴ μετάφρασις, Athènes, 80 p. | Open Library (OL15100950W) |
| grec moderne | 1997 | Pávlos Mátesis | Θεσμοφοριάζουσαι, Athènes, Kastaniotis | BnF cb37685764d |
| grec moderne | 2003 | K. Ch. Myrís (introd. et scholies Ath. Frankoulis) | Θεσμοφοριάζουσαι, Athènes, Patakis | B3Kat |
| grec moderne | 2008 | Theódoros G. Mavrópoulos | Θεσμοφοριάζουσαι, Thessalonique, Zitros | B3Kat |
| tchèque | 1914 | Augustin Krejčí | *Komoedie Aristofanovy* 4 : *Ženy o thesmoforiích*, Prague, Académie | B3Kat |
| hongrois | (1880–1885) | János Arany | traduction complète d'Aristophane, rééditée dans *Arany János összes művei* 9 (*Drámafordítások* 3), Budapest, Akadémiai kiadó, 1961 | BnF cb32905219c [titre hongrois et date de 1ʳᵉ éd. à vérifier] |
| polonais | 1955 | Stefan Srebrny | *Wybór komedii : Osy, Pokój, Ptaki, Tesmoforie*, Varsovie, PIW, 506 p. | Open Library (OL42724723W) |
| russe | 1983 | [A. Piotrovski ou V. Jarkho : à vérifier] | Аристофан, *Комедии* в 2 т., Moscou, Iskousstvo, t. 2 (« Женщины на празднике Фесмофорий ») | notice de libraire citée par une recherche web [à vérifier sur le catalogue de la RGB] |
| hébreu | 1997 | Ziva Caspi (trad.), Dwora Gilula (introd. et commentaire) | *Ḥag ha-nashim : ḳomedyah*, Jérusalem, Magnes, 140 p. | Open Library (OL18118730M) |
| turc | 2022 | Erman Gören, Eser Yavuz | *Thesmophoria'yı Kutlayan Kadınlar*, Istanbul, Türkiye İş Bankası Kültür Yayınları (première traduction turque directe d'après le grec, selon l'éditeur) | Open Library ; notice de libraire (Kitapyurdu) |
| japonais | 2025 | Tobe Jun'ichi (戸部順一) | アリストパネス『喜劇全集 2』, Kyoto, Kyoto University Press (西洋古典叢書) : « 女だけの祭（テスモポリアズサイ） » | notice de la NDL citée par une recherche web [à vérifier] |

## 6. Contrôle d'intégrité des fichiers locaux

Méthode (scripts de `.travail/editions_reprise/scripts/` : `integrite.py`, `pages_texte.py` ; journaux
`integrite1.log`, `integrite2.log`, `integrite3.log` et `.travail/recension_editions/R2/`) : ouverture de
chaque PDF, comparaison du nombre de pages avec les métadonnées de la source (nombre d'images d'archive.org,
nombre de vues du manifeste IIIF de la BSB), rendu d'un échantillon de pages, repérage des *Thesm.* par
mots-clés puis **contrôle visuel** des pages de début et de fin (planches contact dans
`.travail/recension_editions/R2/` et `.travail/editions_reprise/`). Textes par page (couche PDF, hOCR ou
djvu d'archive.org, OCR Tesseract pour les numérisations de la BSB) : `.travail/editions_reprise/pages/`.

Bilan (26 oct. 2026) : **115 PDF contrôlés, tous lisibles, aucune erreur de rendu** ; nouveau contrôle après
redémarrage (28 oct. 2026, `.travail/recension_editions/R3/integrite_reprise3b.tsv`) : **123 PDF**, tous lisibles,
nombres de pages inchangés pour les 115 premiers ; 5 PDF ajoutés le 28 oct. (Brunck 1810 et 1823, Tauchnitz 1814,
Dindorf 1830, Weise 1842 : pages des *Thesm.* contrôlées sur les images) ; 3 doubles en noir et blanc fournis
par archive.org (`*_bw.pdf` : Bamberg 1865, Lange 1891, Willems 1897), identiques aux originaux. Les écarts de 1 à
4 pages avec le décompte d'archive.org correspondent aux mires et feuillets de garde que le PDF d'IA omet.
Particularités :

- **Bons volumes** : tous les fichiers cités au § 2 contiennent bien les *Thesm.* aux pages indiquées.
  Volumes gardés sans les *Thesm.* (contexte, préfaces ou autres pièces) : Juntine de 1515 (*Comoediae
  novem*), Ravestein t. I, Bergler–Burman t. I, Brunck t. II (`aristophaniscom00arisgoog`), Invernizi t. I
  (Prooemium et spécimens de R). Écarté : Dindorf, Leipzig, Weidmann, 1830, t. I (sans les *Thesm.*).
- **Noms de dossier trompeurs** (non renommés pour ne pas casser les renvois existants) :
  `1548_Lyon_Gryphius` (édition sans lieu, « Ioan. Gryphius excudebat », localisée à Venise par Prato) ;
  `1867_Leipzig_Bergk_t2` (= t. II, *editio altera correctior*, **1872**) ; `1907_Oxford_Hall_Geldart_t2`
  (= **1ʳᵉ éd., 1901**, vraisemblablement ; la 2ᵉ éd. de 1907 est dans `…_ed2_reimpr`) ;
  `1843_Dobree_Adversaria_t2` (= éd. Scholefield, Cambridge, 1833 : page de titre PDF 8) ;
  `1874_Dobree_Adversaria_Wagner` (= t. III de l'éd. Wagner, sans les notes sur Aristophane) ;
  `1823_Classical_Journal_27` (vol. 27, sans rapport avec le « n° XXVII » où paraissent les notes de Bentley :
  celles-ci sont dans `1816_Classical_Journal_14`, p. 130–138). Dates d'IA erronées : Invernizi t. VIII et
  XI (« 1794 » pour 1821 et 1823), Dindorf t. IV 3 (« 1835 » pour 1838), Holden (« 1867 » pour 1868).
- **Notice de catalogue erronée** : BSB `bsb10232504` (« Aristophanis Comoediae. 2, Acharnenses, Vespae,
  Thesmophoriazusae, Ecclesiazusae », 1812) contient en fait, entre autres, les *Cavaliers*, la *Paix* et la *Lysistrata* ;
  les *Thesm.* sont au t. III (1814, `bsb10232505`), dont l'extrait est local (E19).
- **Numérisations à rebours** : Juntine de 1515 (*Comoediae novem*), Farreus 1542, édition de 1548.
- **Désordres de reliure ou de numérisation** : Divus 1539 (p. 507–510 reliées avant 507–508 ; doublon
  PDF 526–537) ; Dübner 1842 (nombreuses pages en double) ; Meineke 1860 (exemplaire interfolié : deux vues
  par page).
- **Extraits** (et non volumes complets) : Küster 1710 (120 p. tirées des images d'IA) ; Wechel 1540
  (56 vues) ; préface de la *Lysistrata* d'Enger 1844 (36 vues).
- **Sans couche texte exploitable** : les numérisations de la BSB (Juntine 1516, Bâle 1532, Brubachiana,
  Rositini, Ravestein, Enger 1844, Bothe 1808, Elmsley 1830) ; les trois dernières ont été océrisées
  (Tesseract lat+grc). Les couches texte des numérisations Google de Velsen 1883, Fritzsche 1838, Blaydes
  1880 et Didot 1838 codent le latin en caractères grecs : utiliser l'OCR du Drive (Velsen) ou un OCR
  Tesseract des pages utiles (`.travail/recension_editions/R2/ocrp.py`).

| Fichier (`ED/…`) | Pages PDF | Attendu | Source | Écart | Texte exploitable | Erreurs de rendu |
|---|---|---|---|---|---|---|
| `1515_Florence_Iunta_Comoediae_novem/bub_gb_mcdv56pdPcYC.pdf` | 559 | 559 | IA | 0 | PDF | 0 |
| `1515_Florence_Iunta_editio_princeps_Thesm_Lys/bsb10912207.pdf` | 122 | 122 | BSB | 0 | non | 0 |
| `1532_Bale_Cratander_Grynaeus/bsb00024026.pdf` | 539 | 539 | BSB | 0 | non | 0 |
| `1538_Venise_Zanetti/ARes70622.pdf` | 568 | 568 | IA | 0 | PDF | 0 |
| `1539_Bale_Divus_traduction_latine/bub_gb_x2Q6rpYwY2sC.pdf` | 586 | 586 | IA | 0 | PDF | 0 |
| `1540_Paris_Wechel/bsb10150263_extraits_Thesm.pdf` | 56 | 572 | BSB, extrait | — | non | 0 |
| `1542_Venise_Farreus/bub_gb_Wu5-_TQ_tCoC.pdf` | 574 | 574 | IA | 0 | PDF | 0 |
| `1544_Francfort_Brubach_Grynaeus/bsb10169310.pdf` | 592 | 592 | BSB | 0 | non | 0 |
| `1545_Venise_Rositini_traduction_italienne/bsb10169312.pdf` | 620 | 620 | BSB | 0 | non | 0 |
| `1547_Bale_Froben_Gelenius/bub_gb_NVBJxJmhIW8C.pdf` | 642 | 642 | IA | 0 | PDF | 0 |
| `1548_Lyon_Gryphius/bub_gb_LBXPhhHGIUYC.pdf` | 606 | 606 | IA | 0 | PDF | 0 |
| `1600_Leyde_Raphelengius/bub_gb_WuyoS4JxpT4C.pdf` | 671 | 671 | IA | 0 | PDF | 0 |
| `1607_Geneve_Portus_Biset/bub_gb_46Rraf1UeBIC.pdf` | 1023 | 1023 | IA | 0 | PDF | 0 |
| `1670_Amsterdam_Ravestein_t1/bsb11088392.pdf` | 712 | 712 | BSB | 0 | non | 0 |
| `1670_Amsterdam_Ravestein_t2/bsb11088393.pdf` | 468 | 468 | BSB | 0 | non | 0 |
| `1710_Amsterdam_Kuster/kuster1710_extraits_Thesm.pdf` | 120 | 1021 | IA, extrait | — | non | 0 |
| `1745_Cambridge_Dawes_Miscellanea/bim_eighteenth-century_miscellanea-critica-in-s_dawes-richard_1745.pdf` | 372 | 372 | IA | 0 | PDF | 0 |
| `1760_Leyde_Bergler_Burman_t1/bub_gb_9A2i_-sTWR0C.pdf` | 624 | 625 | IA | -1 | PDF | 0 |
| `1760_Leyde_Bergler_Burman_t2/bub_gb_kRH7s1SMeIUC.pdf` | 705 | 706 | IA | -1 | PDF | 0 |
| `1781_Oxford_Dawes_Miscellanea_Burgess/ricardidawesmisc00dawe.pdf` | 636 | 638 | IA | -2 | PDF | 0 |
| `1783_Strasbourg_Brunck/aristophaniscom00arisgoog.pdf` | 580 | 580 | IA | 0 | hOCR/djvu IA | 0 |
| `1783_Strasbourg_Brunck/aristophaniscom02arisgoog.pdf` | 616 | 616 | IA | 0 | hOCR/djvu IA | 0 |
| `1794_Leipzig_Invernizi_t1/comoediainverniz01aris.pdf` | 656 | 660 | IA | -4 | PDF | 0 |
| `1794_Leipzig_Invernizi_t2_texte/comoediaearis02aris.pdf` | 620 | 624 | IA | -4 | PDF | 0 |
| `1808_Berlin_Hotibius_Bothe_Lectiones/bsb10232652.pdf` | 160 | — | BSB | — | OCR Tesseract | 0 |
| `1810_Oxford_Brunck_reimpr_t1/bub_gb_GC_TY4PiDqQC.pdf` | 358 | 359 | IA | -1 | djvu IA (grec illisible) | 0 |
| `1812_Cambridge_Porson_Adversaria/adversarianotaee00pors.pdf` | 372 | 374 | IA | -2 | PDF | 0 |
| `1812_Quarterly_Review_7_Elmsley/londonquarterly18unkngoog.pdf` | 539 | 539 | IA | 0 | hOCR/djvu IA | 0 |
| `1813_Oxford_Elmsley_Heraclidae/geripdouyrakled00eurigoog.pdf` | 325 | 325 | IA | 0 | hOCR/djvu IA | 0 |
| `1814_Leipzig_Tauchnitz_t3/bsb10232505_extraits_Thesm.pdf` | 84 | 322 | BSB, extrait | — | non | 0 |
| `1815_Classical_Journal_11/classicaljournal1118unse.pdf` | 402 | 404 | IA | -2 | PDF | 0 |
| `1815_Londres_Porson_Tracts/tractsmiscellane00porsuoft.pdf` | 524 | 528 | IA | -4 | PDF | 0 |
| `1816_Classical_Journal_13/classicaljournal1318unse.pdf` | 464 | 466 | IA | -2 | PDF | 0 |
| `1816_Classical_Journal_14/10689.18395.pdf` | 422 | — | — | — | hOCR/djvu IA | 0 |
| `1816_Leipzig_Reisig/carolireisigiit00hermgoog.pdf` | 381 | 381 | IA | 0 | hOCR/djvu IA | 0 |
| `1817_Cambridge_Dawes_Miscellanea_Kidd/miscellaneacriti00daweuoft.pdf` | 736 | 740 | IA | -4 | PDF | 0 |
| `1818_Oxford_Elmsley_Medea/medeaeuripides00euri.pdf` | 328 | 332 | IA | -4 | PDF | 0 |
| `1820_Cambridge_Porson_Notae/ricardiporsonino00porsuoft.pdf` | 628 | 632 | IA | -4 | PDF | 0 |
| `1820_Classical_Journal_22/classicaljournal22londuoft.pdf` | 500 | 504 | IA | -4 | PDF | 0 |
| `1821_Leipzig_Invernizi_t8_commentaire_Thesm/comoediae08aris.pdf` | 654 | 658 | IA | -4 | PDF | 0 |
| `1822_Oxford_Tyrwhitt_Coniecturae/thomaetyrwhittic00tyrw.pdf` | 184 | 186 | IA | -2 | PDF | 0 |
| `1823_Classical_Journal_27/2015.94795.The-Classical-Journal--Vol-27january-And-March1823.pdf` | 404 | — | — | — | non | 0 |
| `1823_Leipzig_Invernizi_t11_scholies_Biset/comoediae11aris.pdf` | 596 | 600 | IA | -4 | PDF | 0 |
| `1823_Londres_Brunck_reimpr_t1/aristophaniscom04brungoog.pdf` | 385 | 385 | IA | 0 | djvu IA (grec illisible) | 0 |
| `1825_Leipzig_Teubner_Dindorf_t2/aristophaniscom00passgoog.pdf` | 459 | 459 | IA | 0 | hOCR/djvu IA | 0 |
| `1826_Paris_Boissonade_t3/comoediaethesmo00boisgoog.pdf` | 341 | 341 | IA | 0 | hOCR/djvu IA | 0 |
| `1829_Londres_Bekker_t1_texte/aristophanouskm03bekkgoog.pdf` | 749 | 749 | IA | 0 | hOCR/djvu IA | 0 |
| `1829_Londres_Bekker_t2_scholies/aristophanouskm02bekkgoog.pdf` | 739 | 739 | IA | 0 | hOCR/djvu IA | 0 |
| `1829_Londres_Bekker_t4_notes/aristophanouskm01bekkgoog.pdf` | 440 | 440 | IA | 0 | hOCR/djvu IA | 0 |
| `1830_Leipzig_Bothe1/comoediaebothe03aris.pdf` | 702 | 706 | IA | -4 | PDF | 0 |
| `1830_Leipzig_Dindorf_Poetae_scenici/poetaescenicigra00dind.pdf` | 972 | 974 | IA | -2 | PDF et hOCR IA | 0 |
| `1830_Leipzig_Elmsley_Acharnenses/bsb10232593.pdf` | 152 | — | BSB | — | OCR Tesseract | 0 |
| `1830_Leipzig_Hanow_Exercitationes/exercitationumc00hanogoog.pdf` | 174 | 174 | IA | 0 | hOCR/djvu IA | 0 |
| `1832_Halberstadt_Thiersch/thesmophoriazus00arisgoog.pdf` | 223 | 223 | IA | 0 | hOCR/djvu IA | 0 |
| `1835_Leipzig_Fritzsche_Quaestiones/quaestionesarist01frit.pdf` | 340 | 344 | IA | -4 | PDF | 0 |
| `1835_Oxford_Dindorf_t2_texte/aristophaniscom06dindgoog.pdf` | 317 | 317 | IA | 0 | hOCR/djvu IA | 0 |
| `1837_Oxford_Dindorf_t3_annotationes/aristophans00unkngoog.pdf` | 845 | 845 | IA | 0 | hOCR/djvu IA | 0 |
| `1838_Leipzig_Fritzsche/thesmophoriazus01fritgoog.pdf` | 707 | 707 | IA | 0 | hOCR/djvu IA | 0 |
| `1838_Leipzig_Fritzsche/thesmophoriazusa00aris.pdf` | 704 | 708 | IA | -4 | PDF | 0 |
| `1838_Leipzig_Voss_Anmerkungen/anmerkungenundr00vossgoog.pdf` | 303 | 303 | IA | 0 | non | 0 |
| `1838_Oxford_Dindorf_t4-3_scholies/aristophaniscom04dindgoog.pdf` | 533 | 533 | IA | 0 | hOCR/djvu IA | 0 |
| `1838_Paris_Didot_Dindorf/aristophaniscome00long.pdf` | 742 | 746 | IA | -4 | PDF | 0 |
| `1838_ZfAW_5_Hermann_Fritzsche/Zeitschrift_für_die_Alterthumswissensch.pdf` | 648 | — | — | — | PDF | 0 |
| `1839_Zutphen_Lenting_Observationes/observationescr00lentgoog.pdf` | 161 | 161 | IA | 0 | hOCR/djvu IA | 0 |
| `1842_Leipzig_Tauchnitz_Weise_t2/aristophaniscom00collgoog.pdf` | 381 | 381 | IA | 0 | djvu IA (grec illisible) | 0 |
| `1842_Paris_Dubner_scholia/scholiagraecain00unkngoog.pdf` | 867 | 867 | IA | 0 | hOCR/djvu IA | 0 |
| `1843_Dobree_Adversaria_t2/petripaulidobre00schogoog.pdf` | 435 | 435 | IA | 0 | hOCR/djvu IA | 0 |
| `1843_Enger_Beitraege_RhM/41250706.pdf` | 26 | — | JSTOR (IA) | — | PDF | 0 |
| `1844_Bonn_Enger_Lysistrata_praefatio/bsb10232530_praefatio.pdf` | 36 | 232 | BSB, extrait | — | non | 0 |
| `1844_Bonn_Enger/bsb10232531.pdf` | 212 | 212 | BSB | 0 | OCR Tesseract | 0 |
| `1845_Leipzig_Bothe2_t3/aristophaniscom00bothgoog.pdf` | 649 | 649 | IA | 0 | hOCR/djvu IA | 0 |
| `1846_Enger_Zu_Thesm_RhM/41250353.pdf` | 28 | — | JSTOR (IA) | — | PDF | 0 |
| `1849_Utrecht_Hirschig_Annotationes/annotationescri00hirsgoog.pdf` | 127 | 127 | IA | 0 | hOCR/djvu IA | 0 |
| `1858_Cobet_Novae_lectiones/novaelectionesqu00cobeuoft.pdf` | 928 | 932 | IA | -4 | PDF | 0 |
| `1860_Leipzig_Meineke_t2/aristophaniscom00meingoog.pdf` | 821 | 821 | IA | 0 | hOCR/djvu IA | 0 |
| `1865_Bonn_Bamberg/deravennateetven00bambuoft.pdf` | 52 | 56 | IA | -4 | PDF | 0 |
| `1865_Leipzig_Meineke_Vindiciae/vindiciarumarist00mein.pdf` | 248 | 252 | IA | -4 | PDF | 0 |
| `1867_Leipzig_Bergk_t2/aristophaniscomo02aris.pdf` | 360 | 364 | IA | -4 | PDF | 0 |
| `1868_Cambridge_Holden/aristophaniscom01arisgoog.pdf` | 898 | 898 | IA | 0 | hOCR/djvu IA | 0 |
| `1868_Herwerden_Analecta/analectacritica00herwgoog.pdf` | 69 | 69 | IA | 0 | hOCR/djvu IA | 0 |
| `1869_Leipzig_Dindorf_Fabulae/aristophanisfab00dindgoog.pdf` | 241 | 241 | IA | 0 | hOCR/djvu IA | 0 |
| `1871_Halle_Velsen_Codex_Urbinas/berdencodexurbi00velsgoog.pdf` | 66 | 66 | IA | 0 | PDF | 0 |
| `1873_Cobet_Variae_lectiones/variaelectionesq00cobe.pdf` | 730 | 732 | IA | -2 | PDF | 0 |
| `1874_Dobree_Adversaria_Wagner/petripaulidobre01dobrgoog.pdf` | 600 | 600 | IA | 0 | hOCR/djvu IA | 0 |
| `1877_Hermann_Opuscula_VIII/opuscula07hermuoft.pdf` | 948 | 952 | IA | -4 | PDF | 0 |
| `1878_Goettingen_Bachmann/conjecturarumob00bachgoog.pdf` | 185 | 185 | IA | 0 | hOCR/djvu IA | 0 |
| `1878_Strasbourg_Buenger/dearistophanise00bngoog.pdf` | 113 | 113 | IA | 0 | hOCR/djvu IA | 0 |
| `1880_Halle_Blaydes/aristophaniscom01blaygoog.pdf` | 332 | 332 | IA | 0 | hOCR/djvu IA | 0 |
| `1880_Halle_Blaydes/comoediaeblaydes01aris.pdf` | 290 | 294 | IA | -4 | PDF | 0 |
| `1882_Paris_Martin_scolies_Ravenne/lesscoliesdumanu00martuoft.pdf` | 272 | 276 | IA | -4 | PDF | 0 |
| `1883_Leipzig_Velsen/aristophanisthe00velsgoog.pdf` | 97 | 97 | IA | 0 | hOCR/djvu IA | 0 |
| `1887_Hermes_22_Kaibel/hermeswies22wies.pdf` | 684 | 688 | IA | -4 | PDF | 0 |
| `1888_Leipzig_Zacher/bub_gb_ezsTAAAAYAAJ.pdf` | 250 | 251 | IA | -1 | PDF | 0 |
| `1891_Goettingen_Lange/quaestionesinari00lang.pdf` | 70 | 74 | IA | -4 | PDF | 0 |
| `1896_Londres_Rutherford_t2/scholiaaristoph00ruthgoog.pdf` | 645 | 645 | IA | 0 | hOCR/djvu IA | 0 |
| `1897_Bruxelles_Willems_Notes/notessuraristoph00will.pdf` | 468 | 470 | IA | -2 | PDF | 0 |
| `1899_Halle_Blaydes_Adversaria/adversariacriti04blaygoog.pdf` | 142 | 142 | IA | 0 | hOCR/djvu IA | 0 |
| `1904_Leyde_van_Leeuwen/aristophanisthe00leeugoog.pdf` | 185 | 185 | IA | 0 | hOCR/djvu IA | 0 |
| `1904_Londres_Rogers/thesmophoriazus00rogegoog.pdf` | 285 | 285 | IA | 0 | hOCR/djvu IA | 0 |
| `1906_Leyde_Herwerden_Vindiciae/vindiciaearistop00herw.pdf` | 190 | 194 | IA | -4 | PDF | 0 |
| `1907_Oxford_Hall_Geldart_t2/aristophaniscomo02arisuoft.pdf` | 378 | 382 | IA | -4 | PDF | 0 |
| `1907_Oxford_Hall_Geldart_t2_ed2_reimpr/bwb_P9-BTV-995_2.pdf` | 376 | 378 | IA | -2 | PDF | 0 |
| `1907_Strasbourg_Coulon_Quaestiones/IA41538722_0058.pdf` | 72 | 72 | IA | 0 | PDF | 0 |
| `1908_Leyde_van_Leeuwen_Prolegomena/prolegomenaadari00leeu.pdf` | 468 | 472 | IA | -4 | PDF | 0 |
| `1909_Londres_Richards/aristophanesothe00richuoft.pdf` | 420 | 424 | IA | -4 | PDF | 0 |
| `1924_Londres_Rogers_Loeb_t3/aristophaneswith03arisuoft.pdf` | 496 | 500 | IA | -4 | PDF | 0 |
| `articles_jstor/41249499.pdf` | 4 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/41249549.pdf` | 2 | — | JSTOR (IA) | — | non | 0 |
| `articles_jstor/41249869.pdf` | 12 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/41250736.pdf` | 7 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/41250936.pdf` | 3 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/41251084.pdf` | 5 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/41251148.pdf` | 4 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423824.pdf` | 17 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423827.pdf` | 55 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423836.pdf` | 15 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423847.pdf` | 15 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423851.pdf` | 14 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423862.pdf` | 39 | — | JSTOR (IA) | — | PDF | 0 |
| `articles_jstor/4423940.pdf` | 57 | — | JSTOR (IA) | — | PDF | 0 |

## 7. Manques, erreurs relevées et pistes

**Éditions non disponibles localement.**
- Accessibles en ligne mais non téléchargées (intérêt limité) : Brunck, Oxford, 1810, t. IV (version latine ;
  IA aristophaniscom00brungoog) ; Brunck, Londres, 1823, t. II–III ; *Poetae scenici* de 1846, 1851, 1865 (IA) ;
  Fritzsche 1838 et Blaydes 1880 en exemplaires BSB (`bsb10232639`, `bsb11413137`), Velsen 1883 (`bsb11536315`),
  doublons possibles de meilleure qualité. Complétés le 28 oct. 2026 : Brunck 1810 t. I (E18), Brunck 1823 t. I
  (E18b), Tauchnitz 1814 t. III (E19, extrait), *Poetae scenici* 1830 (E25), Weise 1842 t. II (E29b).
- Introuvables en ligne : Leyde 1624 (copie sur le Drive, à contrôler : 1624 ou 1670 ?) ; Bourdin 1545
  (Gallica `bpt6k857402r`, bloqué par Cloudflare depuis cette machine ; copie sur le Drive) ; Velsen 1878 ;
  Bergk 1852 (fascicule des *Thesm.* ; seul le t. I de 1852 est numérisé : IA `B-001-001-664`) et 1891 ; Holden
  1848 ; Dindorf, Leipzig, Weidmann, 1830, t. II (le texte est celui des *Poetae scenici* de 1830, E25, local).
- Sous droits (à consulter en bibliothèque ou via le Drive) : Coulon 1928, Cantarella 1956, Paduano 1983,
  Gannon 1988, Sommerstein 1994, Henderson 2000, Prato 2001, Marzullo 2003, Austin–Olson 2004,
  Mastromarco–Totaro 2006, Wilson 2007, Saetta Cottone 2016, Di Virgilio 2025.
- Copies du Drive attendues du chantier « Drive » (non encore dans `.sources/drive/fichiers/`) :
  Austin–Olson, Sommerstein, Prato, CUF IV (Coulon), Mastromarco–Totaro, Willems t. I–III, Küster (PDF
  complet), Fritzsche (« propre »), Leyde 1624 (« Scaliger propre »), Bourdin, Le Paulmier, Brunck (deux
  fichiers), Rogers (trois fichiers), Hall–Geldart t. II.

**Erreurs relevées et corrigées** (par rapport aux versions de travail antérieures et aux métadonnées) :
Enger 1844 n'a **pas** collationné R (il dépend de Bekker ; préface de *Lys.*, p. X–XI) ; le « Grynaeus »
des apparats est la Brubachiana de 1544 ; les scholies de Bourdin sont de 1545 (non 1540) ; le tome local de
Bergk est de 1872 ; le Hall–Geldart de Toronto est la 1ʳᵉ éd. ; l'édition de 1548 est sans lieu ; Blaydes
1880 déclare avoir collationné R lui-même (p. VII) ; la Wechel de 1540 contient bien les *Thesm.*
(p. [469]–517). Ajouts du 28 oct. 2026 : l'« ed. Lipsiensis (1814) » de l'apparat de l'auteur (v. 1201) est le t. III de
l'édition stéréotype de Tauchnitz (E19), et le « Teubner » du v. 632 l'édition anonyme de 1825 (E20), que
le « τί δ' ἦν olim Dindorfius » d'Enger permet d'attribuer à W. Dindorf ; la notice BSB du t. II de Tauchnitz
(1812) décrit en réalité le contenu du t. III ; le t. I de l'Oxford de 1810 contient le texte grec et les notes,
le t. IV la version latine.

**Points à vérifier.** Mode de collation de R par Coulon (préface du t. I de la CUF, 1923), Cantarella,
Gannon, Sommerstein, Austin–Olson (Introduction, § VII « The Manuscript Tradition », p. lxxxix–xcviii, absente de
l'extrait local) ; contenu exact de l'édition de Bourdin (texte complet ou seulement lemmes) ; pages des *Thesm.*
dans l'édition de 1624 (et identité de la « Batava minor » d'Enger : `conjectures_sources.md` § 6) ; date de la
première édition stéréotype de Weise (avant 1840) ; contenu des traductions de Fleury (1862) et de Zévort (1889) ;
notice de la traduction de Voss (1821) ; tome des *Thesm.* chez Hickie (1853 ; numérisations DLI d'archive.org
sans OCR) et Way (1927–1934) ; traducteurs des *Thesm.* dans la Bantam de M. Hadas (1962), chez Losada (2012) et
dans l'Aristophane russe de 1983 (Piotrovski ou Jarkho) ; titre hongrois d'Arany ; présentation (bilingue ou
non) de l'édition Balasch (1974) ; autres traductions (néerlandais, langues scandinaves, roumain, coréen, chinois…)
à rechercher dans KVK et WorldCat. Contrôlés le 28 oct. 2026 : présence des *Thesm.* chez Poinsinet de Sivry
(1784, t. III), Artaud (2ᵉ éd., 1841, p. 363–402) et Poyard (cité par Coulon 1937). Pour les adaptations
scéniques (grec moderne : Solomos 1958, Koun 1985), voir Austin–Olson 2004, p. xxxiii n. 13, qui renvoie à
G. Van Steen, *Venom in Verse* (Princeton, 2000) et à l'*Archive of Performances of Greek and Roman Drama*
(Oxford) ; plus récemment, traduction de P. Boukalas pour la mise en scène de V. Theodoropoulos au festival
d'Épidaure (2018), d'après la presse grecque (*Ta Nea*, 30 juill. 2018) [publication imprimée à vérifier].