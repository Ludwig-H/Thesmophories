# Papyrus des *Thesmophories* — recension

> État : **version de travail** (2026-10-26). Rien n'est donné pour acquis sans avoir été lu dans une source (édition, base de données, image) ; la colonne « vérifié » et les mentions *[à vérifier]* disent ce qui reste à contrôler. Les éditions et images sous droits sont dans `.sources/` (non versionné).

## 1. Conventions et sources

- **Numérotation des vers** : numérotation usuelle (Velsen, Coulon, Sommerstein, Austin–Olson ; c'est aussi celle des fichiers `latex/` de l'auteur). Le texte Hall–Geldart de Perseus (`.sources/corpus/thesmo_hall_geldart.tsv`) est décalé d'une unité de 372 à 378 environ (son v. 374 = v. 373 usuel) : les éditeurs anciens qui suivent Hall–Geldart (Hunt 1912) ont donc des numéros décalés.
- **Sigles** : MP³ = Mertens–Pack³ (base CEDOPAL, Liège, consultée en ligne le 26/10/2026, notices `cdp_MP3_display.aspx?numNot=…`) ; LDAB, TM = Leuven Database of Ancient Books, Trismegistos (numéros lus dans les fichiers EpiDoc du DCLP, copie locale `.sources/corpus/idp.data/DCLP/59/`, dépôt du 24/10/2026) ; CGFP = C. Austin, *Comicorum Graecorum fragmenta in papyris reperta* (1973) ; Gelzer = T. Gelzer, art. « Aristophanes », *RE* Suppl. XII (1970), col. 1553 (liste des papyrus).
- **Sources consultées** (copies locales) :
  - P.Oxy. LXXIII (2009), n° 4935, éd. A. Benaissa : `.sources/drive/papyrus/Oxyrhynchus Papyri 73 4935 vers 1043-1051 1201-1210.pdf` (pp. 23-25 imprimées) ;
  - P.Oxy. LXXVIII (2012), n° 5132, éd. W. B. Henry : couche texte seule, `.sources/drive/papyrus/POxy78_readcontent.txt` (OCR ; le PDF complet du Drive n'est pas encore téléchargé) ;
  - P.Oxy. IX (1912), n° 1176 (Satyros), éd. A. S. Hunt : `.sources/web/papyrus/POxy_IX/pt9oxyrhynchuspa00grenuoft.pdf` (archive.org, domaine public), texte p. 155, notes p. 178 ;
  - R. Goossens, « Notes sur quelques papyrus littéraires », *CdÉ* 16, n° 31 (1941), pp. 105-106 : `.sources/drive/papyrus/Notes sur quelques papyrus littéraires PSI1194 Thesmophories.pdf` ;
  - C. Austin, « Observations critiques sur les *Thesmophories* d'Aristophane », *Dodone (philol.)* 19 (1990), 9-29, ici p. 10 n. 4 : `.sources/drive/fichiers/Grec/Aristophane/1. Observations critiques sur les Thesmophories d’ Aristophane.txt` ;
  - CLGP I.1.4 (Aristophanes–Bacchylides, 2ᵉ éd.), table des matières : `.sources/drive/papyrus/ARISTOPHANES - BACCHYLIDES INDICE CLGP I.1.4.pdf` ;
  - fiches en ligne : PSIonline (PSI XI 1194, page sauvegardée `.sources/web/papyrus/PSI_XI_1194_psi-online.html`) ; Oxford, Papyrology (portail SDS, API Figshare) ; Oxyrhynchus Online (pages archivées de `csad.ox.ac.uk/POxy/papyri/vol56/`).
- **Images** (toutes « In Copyright » : usage d'étude, non versionnées) dans `.sources/web/papyrus/` : `PSI_XI_1194_r.jpg`, `POxy_LVI_3839_hires.jpg`, `POxy_LVI_3839_couleur.jpg` (13 080 × 12 866 px), `POxy_LVI_3840_hires.jpg` (petite : 367 × 934 px), `POxy_LXXIII_4935_hires.jpg`, `POxy_LXXVIII_4935+5132.jpg`.
- **Non consultés** (Drive de l'auteur pas encore téléchargé, ou introuvables en libre accès) : P.Oxy. LVI (1989), pp. 72-79 (3839, 3840) ; PSI XI (1935) et XIV (1957) ; Austin–Olson 2004 (introduction, § sur le texte) ; Wilson, OCT (2007) ; Schorn, *Satyros aus Kallatis* (2004). Leurs données sont reprises ici de seconde main et marquées comme telles.

## 2. Tableau récapitulatif

Quatre manuscrits antiques (tous d'Oxyrhynchus, tous des rouleaux) et une citation papyrologique. Aucun ne recoupe un autre.

| Papyrus | MP³ | LDAB / TM | Date | Vers | Éd. princeps | Sigle de l'auteur |
|---|---|---|---|---|---|---|
| PSI XI 1194 + PSI XIV p. XV | 154 | 389 / 59292 | IIᵉ s. (éd., MP³, LDAB) ; Iᵉʳ s. selon L. Del Corso (2002) | 133-144 (fr. Grassi), 145-156, 237-245, 273-288, 594-596, 804-809 ; fr. avec nom d'auteur et titre | PSI XI (1935) ; PSI XIV (1957), p. XV | `\PsiUn` |
| P.Oxy. LVI 3839 | 153.1 | 352 / 59255 | IIᵉ/IIIᵉ s. (éd.) ; début IIIᵉ s. (Orsini) | 25 (?), 742-766 (fr. 1), 941-956 (fr. 2) | W. E. H. Cockle, P.Oxy. LVI (1989), 72-78 | `\PsiDeux` |
| P.Oxy. LVI 3840 + LXXIII 4935 + LXXVIII 5132 (un seul rouleau) | 154.001 (l'ancien 154.01 est supprimé, fusionné) | 362 / 59265 | IIᵉ/IIIᵉ s. (Henry 2012) ; IIᵉ s. (Benaissa 2009) ; IVᵉ s. (Parsons 1989, pour 3840 seul, datation abandonnée) | 1043-1051, 1185-1193 (+ 1187a), 1202-1210 | Parsons, P.Oxy. LVI (1989), 78-79 ; Benaissa, P.Oxy. LXXIII (2009), 23-25 ; Henry, P.Oxy. LXXVIII (2012) | `\PsiTrois` (3840), `\PsiQuatre` (4935) ; 5132 absent |
| P.Oxy. IX 1176 (Satyros, *Vie d'Euripide*), fr. 39, col. XII 1-16 | — (texte de Satyros) | — / 62717 | IIᵉ s. (Hunt) | citation de 373-374 et 335-337 | A. S. Hunt, P.Oxy. IX (1912), 124-182 (n° 1176) | `\PsiCinq` |

Sources du tableau : notices MP³ 153.1, 154, 154.001 (et 154.01 « delendum ») ; DCLP 59255, 59265, 59292, 62717 ; PSIonline ; portail Oxford (dates et éditeurs : 3839 « Second/third century », éd. Cockle ; 3840 « Fourth century », éd. Parsons ; 4935 « Second century », éd. Benaissa ; 5132 « Second / third century », éd. Henry). Le balayage des numéros MP³ voisins (152 à 155.1) confirme qu'il n'y a pas d'autre papyrus des *Thesmophories* dans MP³ : 153 à 153.02 = *Grenouilles*, 154.02 et suivants = *Guêpes*.

## 3. Notices

### 3.1 PSI XI 1194 + PSI XIV p. XV (MP³ 154)

- **Conservation, provenance** : Florence, Biblioteca Medicea Laurenziana, inv. 20939 ; Oxyrhynchus, fouilles d'E. Breccia à Behnesa (Kom Ali el-Gammân), printemps 1932 ; peut-être de la bibliothèque de la famille de Sarapion « dit Apollonianos » (PSIonline).
- **Description** : rouleau, recto ; six fragments (a-f) de 4 × 9,4 cm à 2,7 × 9 cm ; corrections d'une autre main ; le dernier fragment ne porte que le nom de l'auteur et le titre de la pièce (PSIonline). DCLP : « com. with title and stichometry » ; écriture « similar to severe style ». Un fragment supplémentaire (vv. 133-144) a été publié par E. Grassi, *SIFC* n.s. 27-28 (1956), 48 ; l'ensemble est réédité dans PSI XIV (1957), p. XV.
- **Éditions** : PSI XI 1194 ; PSI XIV, p. XV ; CGFP 46 (selon PSIonline ; la notice MP³ porte « CGFP 16 », vraisemblablement une coquille) ; C. Austin, « The Florence Papyrus of Ar. *Thesm.* », dans R. Pintaudi (éd.), *Miscellanea papyrologica* (Pap. Flor. VII), Florence, 1980, 11-12 et pl. I. Gelzer 13 ; Pack² 154.
- **Études** (liste MP³, PSIonline, bibliographie d'Austin) : R. Goossens, *CdÉ* 16 (1941) 105-106 (v. 242) ; W. J. W. Koster, *Acme* 8, 2-3 (1955) 93-103 (coronis, parépigraphes, proceleusmatique) ; C. Austin, *ZPE* 26 (1977) 64 et 57 (1984) 58 (v. 242) ; B. Marzullo, *MCr* 13-14 (1978-1979) 219-221 ; S. Medaglia, *Boll. Class.* 3ᵉ s., 3 (1982) 154-159 et 4 (1983) 137 ; K. McNamee, *Abbreviations in Greek Literary Papyri and Ostraca* (1981), pp. XXXV, 34, 49, 122 ; N. Litinas, *CdÉ* 89 (2014) 325-348 ; L. Del Corso, dans G. Mastromarco et al., *La commedia antica. Forma e contenuti* (Lecce, 2017) 231-279.
- **Images** : PSIonline (copie locale) ; K. J. Dover, *Aristophanic Comedy* (Londres, 1972), pl. 2, p. 6 (vv. 273-288) ; Pap. Flor. VII, pl. I.
- **Leçons notables** (d'après l'apparat de l'auteur, `edition/donnees/travaux_anterieurs/apparat.tsv` ; non revérifiées sur l'éd. princeps, indisponible) :

| Vers | Papyrus | R et éditeurs | Remarque |
|---|---|---|---|
| 141 | σύ τ' (avec Σ) | τίς δ' R | fr. Grassi |
| 154 | ἄν | ἄν R : ἢν Dindorf | confirme R |
| 242 | [ἕ]τερον (restitution Medaglia) | om. R (vers trop court) | Goossens (1941) : les traces excluent le texte de R ; il pense à π[ρό]τερον (ou ὑπέρτερον) et conjecture τοὐπερῷον ; cf. Austin, *ZPE* 26 et 57 |
| après 276 | ολολυ[ (parépigraphe) | ὀλολύζουσι, τὸ ἱερὸν ὠθεῖται R (selon l'apparat de l'auteur) | cf. Koster 1955 |
| 285 | τὰ πόπαν' | τὸ πόπανον R | confirme Porson (Austin 1990, p. 10 n. 4) |
| 287 | Φερρέφαττα | Φερσέφαττα R | confirme Thiersch (Austin 1990, ibid.) |
| 596 | πεπύσμην | πεπύσμην R : 'πεπύσμην Faber | confirme R |
| 807 | Στρατονίκην | στρατωνίκην R | |

### 3.2 P.Oxy. LVI 3839 (MP³ 153.1)

- **Conservation** : Oxford, Bodleian Art, Archaeology and Ancient World Library, Papyrology Rooms, inv. 18 2B.66/F(1)b + 18 2B.66/F(9-10)e.
- **Description** : rouleau ; majuscule biblique (DCLP ; P. Orsini, *Manoscritti in maiuscola biblica*, Rome, 2005, pp. 106-107, pl. 9). MP³ : texte sur le recto, au verso, tête-bêche, MP³ 1218.2 ; « même main que 142.3 ». Le fr. 1, identifié par E. Lobel, était déjà connu comme CGFP 48 et Gelzer 14 (Oxyrhynchus Online).
- **Contenu** : v. 25 (?) ; fr. 1 : 742-766 ; fr. 2 : 941-956 (P.Oxy., MP³, portail d'Oxford). L'introduction de l'auteur (`latex/Aristophane-Thesmo Introduction.tex`, l. 373) donne « 941-953 » : à corriger.
- **Éditions** : W. E. H. Cockle, P.Oxy. LVI (1989) 72-78, pl. IX ; id., « An unpublished papyrus of Aristophanes from Oxyrhynchus : *Thesmophoriazusae* 25 (?), 742-766, 941-956 », dans E. M. Craik (éd.), *Owls to Athens. Essays on Classical Subjects presented to Sir Kenneth Dover*, Oxford, 1990, 51-60 (photographie p. 53).
- **Études** : W. Luppe, *APF* 38 (1992) 76 ; C. Austin, *Dodone* 19 (1990) 10 n. 4 ; W. A. Johnson, *Bookrolls and Scribes in Oxyrhynchus* (2004) ; Litinas 2014 ; Del Corso 2017 (liste MP³).
- **Images** : portail d'Oxford, DOI 10.25446/oxford.21176497 (copies locales, dont une prise de vue en couleur à très haute résolution).
- **Leçons notables** (apparat de l'auteur, d'après l'éd. princeps ; non revérifiées) : 743 τρικοτυλον· η πως ειπε μοι τ[ (R τρικότυλον ἢ πῶς ; εἰπέ μοι — τί μ' εἰργάσω ;) ; 745 τυννοῦτον et τυννοῦτο (Brunck : τυνοῦτον, τυνοῦτο R) et pas de changement d'interlocuteur noté devant μικρόν ; 746 γέγονε (Brunck : γέγονεν R) ; 747 καὶ ὅσον (= R : χὤσον Bentley) ; 754 δός τὸ (Lobeck : δός μοι τὸ R) ; 758-759 ἱερείας (= R : ἱερέας Austin–Olson) ; 760 traces ]απητην.ι.α..υξ[ (R σοὐξῃρήσατο). Austin (1990, p. 10 n. 4) : 3839 et 3840 confirment « les corrections de Brunck aux v. 745 et 746, de Fritzsche au v. 745, de Lobeck au v. 754 et d'Enger au v. 1185 ».

### 3.3 P.Oxy. LVI 3840 + LXXIII 4935 + LXXVIII 5132 (MP³ 154.001)

Un seul rouleau, d'une seule main semi-cursive (Henry, P.Oxy. LXXVIII, introd. à 5132) ; dos blanc.

- **3840** — inv. 87/281(a) ; éd. P. J. Parsons, P.Oxy. LVI (1989) 78-79 ; vv. 1185-1193, avec le vers 1187a (ἀνακύπτῃ καὶ παρακύπτει ἀπεψωλημένος, supprimé par Ellebodius) attesté par μ]ενο[ (apparat de l'auteur) ; un dicolon marque le changement d'interlocuteur au v. 1190 (Henry). Datation de Parsons : IVᵉ s. (portail d'Oxford, MP³) ; l'auteur reprend « IVᵉ siècle », qu'il faut corriger depuis l'identification de la main (IIᵉ/IIIᵉ s.).
- **4935** — inv. 88/287 part ; éd. A. Benaissa, P.Oxy. LXXIII (2009) 23-25 ; fr. 1 : vv. 1043-1051 (aucune marge) ; fr. 2 : vv. 1202-1210, haut de colonne (marge supérieure ≥ 1,4 cm). Même copiste que P.Oxy. LXXVI 5084 (Platon, *Criton*). Benaissa date la main du IIᵉ s. L'auteur écrit « 1201-1210 » : Benaissa et MP³ donnent 1202-1210.
- **5132** — inv. 87/281(c) ; éd. W. B. Henry, P.Oxy. LXXVIII (2012) ; fragment de 2,2 × 4,5 cm qui se place à droite de 4935 fr. 2, dans la même colonne ; vv. 1203-1209 ; IIᵉ/IIIᵉ s. ; dicolon au v. 1209. Henry : « There are no readings of interest. » Il signale que le rouleau est le Π… d'Austin–Olson et le « P68 » (OCR ; sans doute Π68) de l'OCT de Wilson (2007) *[à vérifier sur l'imprimé]*.
- **Études** : W. Luppe, *APF* 38 (1992) 76 (sur 3840) ; M. F. Di Bari, *ZPE* 174 (2010) 33-36 (sur 4935) ; Johnson 2004 ; Litinas 2014 ; Del Corso 2017 (liste MP³).
- **Images** : portail d'Oxford (3840 : DOI 10.25446/oxford.21176500 ; 4935 : 10.25446/oxford.21180460 ; 4935 + 5132 réunis : 10.25446/oxford.21184774).
- **Leçons notables** :

| Vers | Papyrus | R et éditeurs | Source, vérifié |
|---|---|---|---|
| 1047 | ἰὼ μοίρ[ας (sans μοι) | ἰώ μοι μοίρας R : μοι del. Hermann | Benaissa (vérifié) : ω et ρ « virtually certain » ; haplographie du papyrus non exclue |
| 1048-1049 | en ekthesis (de sept et cinq lettres) ; colométrie de R | la plupart des éditeurs répartissent en trois lignes | Benaissa (vérifié) |
| 1051 | τ]ὸν β[άρβαρον | τὸν βάρβαρον R : τὸν δύσμορον Brunck | Benaissa (vérifié) : confirme R |
| 1208 | point en haut devant σὸν ἔργον ; place de six lettres environ | λέλυσο (λέλυσον Rᵃᶜ) R : λέλυσαι Bentley | Benaissa (vérifié) : λέλυσο et λέλυσαι possibles, λέλυσαι « would fit the space comfortably » |
| 1185 | γογγυλί | γογγύλῃ R : γογγυλί Enger | apparat de l'auteur ; Austin 1990 (confirmation d'Enger) ; non revérifié |
| 1187a | μ]ενο[ (le vers est présent) | vers présent dans R ; del. Ellebodius | apparat de l'auteur ; non revérifié |
| 1192 | μέλι (avec le Monacensis) | μέλις R | apparat de l'auteur ; non revérifié |

### 3.4 Citation papyrologique : Satyros, *Vie d'Euripide* (P.Oxy. IX 1176)

- **Le papyrus** : rouleau du IIᵉ s. (Hunt), fr. 39 de 14,2 × 75,5 cm (cols. I-XXIII) ; le livre VI des *Vies* de Satyros, en dialogue. Bibliographie DCLP 62717 : FGrHist 776 ; CGFP 294 ; PCG VIII 1024-1025 ; Schorn, *Satyros aus Kallatis* (2004), texte pp. 86-113, commentaire pp. 181-346 ; TrGF V.2 960 et 1007a-h.
- **Le passage** (fr. 39, col. XII 1-16 ; texte de Hunt, p. 155, lu sur l'image du volume) : après le récit de l'attaque des femmes contre Euripide aux Thesmophories (col. X), l'interlocuteur cite les vv. 373-374 puis 335-337 : [τῇ τῶ]ν γυ[ναι]κῶν· ⟨Τι⟩[μόκλ]ει' ἐπε[στ]άτει, Λυσίλ[λ' ἐ]γραμμάτευεν, εἶπε Σωστράτη. — εἴ τις ἐπιβουλεύει τι τῷ δήμῳ κακὸν τῷ τῶν γυναικῶν ἢ 'πικηρυκεύετ[αι] Εὐριπίδ⟨ῃ Μήδοις⟩ τ' ἐπὶ βλάβῃ τινί. Hunt (p. 178) note « xii. 1-16 = Aristoph. *Thesm.* 374-5, 335-7 » (numéros de Hall–Geldart = 373-374 usuels).
- **Leçons** :
  - **373** : la transcription diplomatique porte ]κωναρ[ : le papyrus avait un autre nom que Τιμόκλει' (R, lu sur l'image du f. 166v), « e.g. Ἀρχίκλεια » (Hunt) ; l'auteur imprime dans son apparat Ἀρ[. . . .]λ̣ ει' (λ̣ « vel α, δ, μ ») et rappelle que Τιμόκλει' est aussi la leçon de Σ et de la Souda (ε 2616) *[à vérifier]* ;
  - **374** : Σωστράτη, comme R (lu sur l'image : σωστράτη) ; Hall–Geldart (Perseus) et l'auteur impriment Ζωστράτη ;
  - **337** : diplomatique de Hunt ευρι|πιδιω[. . .] . τ : le papyrus a τ' (supplément de Biset/Scaliger, absent de R) ; « there is not room for Μήδοις between ι and τ » (Hunt). Austin (1990, p. 10 n. 4, renvoyant à *Dodone* 16, 1987, p. 77) y voit la confirmation du supplément de Biset. L'auteur transcrit ευριπιδιωι̣[. .]υ̣τ, lecture différente de celle de Hunt, dont la source (Schorn 2004 ?) reste à identifier *[à vérifier]*.

## 4. Papyrus apparentés et résultats négatifs

- **Commentaires et lexiques** : la table de CLGP I.1.4 (Aristophanes, nᵒˢ 1-35 et « schede ») ne contient aucun commentaire, aucune note marginale ni aucune glose lexicale portant sur les *Thesmophories*. Aucun papyrus ne transmet de scholies à cette pièce : les scholies ne sont connues que par R (voir `recherche/scholies.md`).
- ***Thesmophories II*** (pièce perdue) : P.Oxy. II 212 + XXXVII 2808 + LXXXVII 5581 (fin du Iᵉʳ s. av. J.-C. ; LDAB/TM 59246 ; CGFP 223 ; PCG VIII 1111 ; 5581 éd. E. Chepel et W. B. Henry, portail d'Oxford, DOI 10.25446/oxford.23611257) : attribué aux *Thesmophories II* ou aux *Lemniennes*. Sans rapport avec la tradition de notre pièce, mais à citer à propos de la seconde pièce.
- **Autres bases** : le DCLP local ne contient aucune transcription (`div type="edition"` vide) pour les trois manuscrits ; pas d'ostracon ni de tablette des *Thesmophories* dans le DCLP.

## 5. Concordance avec les sigles de l'auteur (`latex/`) et corrections

| Macro (Introduction, Annexes) | Désignation de l'auteur | Correction proposée |
|---|---|---|
| `\PsiUn` = PSI-1194 | « vers 145-156 ; 237-245 ; 273-288 ; 594-596 ; 804-809 ; 1231 (et 133-144 PSI XIV, p. XV), IIᵉ siècle » | « 1231 » désigne le fragment du titre final ; ajouter la datation alternative (Iᵉʳ s., Del Corso) |
| `\PsiDeux` = POxy-3839 | « 742-766 (fr. 1) ; 941-953 (fr. 2), circa 200 » | 941-956 ; ajouter 25 (?) ; IIᵉ/IIIᵉ s. |
| `\PsiTrois` = POxy-3840 | « 1185-1193, IVᵉ siècle » | IIᵉ/IIIᵉ s. ; même rouleau que 4935 et 5132 |
| `\PsiQuatre` = POxy-4935 | « 1043-1051 (fr. 1) ; 1201-1210 (fr. 2), IIᵉ siècle » | 1202-1210 ; ajouter 5132 (1203-1209), même colonne que fr. 2 |
| `\PsiCinq` = POxy-1176 (commentaire « P50 ») | « fr. 39, col. XII : vers 335-337 ; 373-375 » | 335-337 et 373-374 ; « P50 » est peut-être le sigle de l'OCT de Wilson *[à vérifier]* ; le fichier du Drive « P50 p 155(171).pdf » correspond sans doute à la p. 155 de P.Oxy. IX (texte de la col. XII) |

## 6. Vérifications à faire

1. Relire sur P.Oxy. LVI (Drive : « Oxyrhynchus Papyri 56 … 3839 et 3840 … ») les leçons de 3839 et 3840 reprises de l'apparat de l'auteur ; contrôler la lecture de 3840 sur une image meilleure que la vignette d'Oxford.
2. Relire PSI XI 1194 et PSI XIV p. XV (et Austin, Pap. Flor. VII) pour les leçons de PSI 1194, notamment 141, 242, 276, 285, 287, 807.
3. Sigles et liste des papyrus chez Austin–Olson (2004, introduction, pp. lxxxix-xcii selon Tordoff, *BMCR* 2008.09.24) et chez Wilson (OCT 2007) ; confirmer « Π68 ».
4. Satyros : texte de Schorn (2004) pour les vv. 337 et 373 (source de la transcription de l'auteur).
5. CGFP 46 ou 16 pour PSI 1194 (PSIonline contre MP³).
