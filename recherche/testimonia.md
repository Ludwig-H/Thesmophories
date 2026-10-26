# Tradition indirecte (testimonia) des *Thesmophories* — recension

> État : **version de travail** (26/10/2026). Le fichier est produit à partir des relevés de `.travail/recension/testimonia/` (script `generer_md.py`) et complété au fil des vérifications. Rien n'est marqué « vérifié » sans avoir été lu dans un texte ; la colonne « Vérifié » dit où.

## 1. Conventions et méthode

**Numérotation.** Vers dans la numérotation usuelle (voir `recherche/papyrus.md`, § 1).

**Références.** Souda = Adler ; Hésychius = Latte (α–ο), Hansen (π–σ), Cunningham (τ–ω) ; Photius = Theodoridis (α–φ), Porson (χ–ω) ; Pollux = Bethe ; Moeris = Hansen ; Aelius Dionysius = Erbse ; Phrynichus, *Praep. soph.* = de Borries ; Antiatticiste = Bekker, *Anecdota* I (page.ligne) ; Zonaras = Tittmann (colonnes) ; Eustathe = pages de l'édition de Rome ; *Etymologicum magnum* = pages de Sylburg (reprises par Gaisford).

**Types.** *citation* : au moins deux mots consécutifs du texte, dans l'ordre (éventuellement avec omissions ou variantes) ; *lemme* : expression du texte prise comme lemme d'une notice ; *glose* : explication d'un mot du texte (souvent issue d'une scholie à la pièce), sans citation. Les notices qui se bornent à gloser un mot fréquent ont été écartées (§ 4).

**Leçons.** On indique les divergences de la citation par rapport au texte transmis : « R » = leçon du Ravennas d'après l'apparat de l'auteur (`edition/donnees/travaux_anterieurs/apparat.tsv`, non revérifié sur l'image) ; « texte » = texte imprimé par l'auteur (Harmattan 2023) quand l'apparat est muet. Les différences purement graphiques (ν éphelcystique, élision notée ou non, accentuation de la SOL) ne sont pas relevées. « — » : pas de divergence. Les variantes des manuscrits de la Souda (apparat d'Adler) n'ont pas pu être contrôlées : la SOL ne donne que le texte d'Adler.

**Vérification.** « oui (SOL) » : texte grec d'Adler lu sur la *Suda On Line* (notices téléchargées dans `.sources/web/testimonia/sol/adler/`, alignées mot à mot sur le texte de la pièce) ; « oui (First1K) » : texte d'Adler de First1KGreek ; pour les autres sources, l'édition lue est nommée (TEI Perseus/First1K, OCR d'une édition du domaine public contrôlé sur l'image de la page, PDF du Drive de l'auteur). « non » : référence reprise de l'auteur ou d'une source secondaire, non contrôlée.

**Méthode.** (a) Testimonia de l'auteur (macro `\testimonia` des fichiers `latex/` Harmattan 2023, extraits dans `edition/donnees/travaux_anterieurs/testimonia.tsv`) ; (b) recherche directe dans le corpus local `.sources/corpus/` (suites de mots communes avec le texte de la pièce : `outils/corpus/citations_thesmo.py`, 6 163 groupes candidats, revus à la main) ; (c) interrogation de la Suda On Line (notices dont les notes renvoient aux *Thesmophories*) ; (d) alignement automatique de chaque citation sur le texte de la pièce (Smith–Waterman mot à mot), puis contrôle à la main des divergences.

## 2. Bilan

455 témoignages retenus (165 notices de la Souda, 135 autres sources) ; 284 vérifiés dans un texte, 171 non vérifiés.

## 3. Tableau vers par vers

| Vers | Source | Référence | Type | Texte cité (extrait) | Leçon (divergences) | Remarques | Vérifié |
|---|---|---|---|---|---|---|---|
| 1 | Ar. fr. | Ar. fragm. (Kassel-Austin) 617 πυθοῦ χελιδὼν πηνίκ᾽ ἄττα φαίνεται | — |  |  | référence de l'auteur, non contrôlée | non |
| 2 | Photius | α 1029 | glose | ἀλοῶν (= Synagoge Σᵇ α 984) |  |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge Σᵇ α 984 ; texte de Photius non lu) |
| 2 | Souda | Souda α 1330 | citation | ἀπολεῖ μ' ἀλοῶν ἄνθρωπος ἐξ ἑωθινοῦ | ἄνθρωπος (= R ; ἅνθρωπος Boissonade) |  | oui (SOL) |
| 2 | Synagoge | Σᵇ α 984 | glose | ἀλοῶν · ἀντὶ τοῦ περιάγων, ὡς οἱ ἀλοῶντες βόες. οὕτως Ἀριστοφάνης |  | Aristophane nommé ; parallèle : Photius α 1029 | oui (Cunningham, PDF p. 601, OCR) |
| 18-19 | Hésychius | χ 576 | glose | χοάνη · χώνη, τύπος, εἰς ὃν μεταχεῖται τὸ χωνευόμενον |  | l'éd. renvoie à Thesm. 18 | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 18-9 | Hésychius | Moeris χ 1 Hesychius χ 576 χοάνη | — | χοάνη = χώνη |  | référence de l'auteur, non contrôlée | non |
| 24 | Apostolius | Michael Apostolius II 94 | — |  |  | référence de l'auteur, non contrôlée | non |
| 24 | Macarius | Macarius VI 90 | — |  |  | référence de l'auteur, non contrôlée | non |
| 33 | Pollux | Pollux II 88 | — | δασυπώγων |  | référence de l'auteur, non contrôlée | non |
| 36 | Souda | Souda π 3024 | citation | ἀλλ' ἐκποδὼν πτήξωμεν | — |  | oui (SOL) |
| 39-41 | Souda | Souda ε 3792 | citation | εὔφημος πᾶς ἔστω λεὼς … θίασος Μουσῶν ἔνδον μελάθρων | λεώς (= R ; λαός Σ) ; συγκλείσας (texte συγκλῄσας) ; ἐνδημεῖ (texte ἐπιδημεῖ) | l'auteur cite « ε 3791 » dans ses testimonia (= Ἐφείλιξαν) mais « ε 3792 » dans son apparat | oui (SOL) |
| 40-42 | Souda | Souda θ 378 | citation | ἐπιδημεῖ γὰρ θίασος Μουσῶν … τῶν δεσποσύνων μελοποιῶν | — |  | oui (SOL) |
| 43-45 | Souda | Souda ε 3997 | citation | ἐχέτω δὲ πνοὰς νήνεμος αἰθήρ · κῦμα δὲ πόντου μὴ κελαδείτω γλαυκόν | — | l'auteur cite « ε 3792 » : lire ε 3997 (SOL) | oui (SOL) |
| 43-45 | Zonaras | col. 941 | citation | Ἐχέτω. κρατείτω. Ἀριστοφάνης · ἐχέτω δὲ πνοὰς νήνεμος αἰθήρ · κῦμα δὲ πόντου μὴ κελαδείτω γλαυκόν | — |  | oui (Tittmann I, image de la page) |
| 44 | Souda | Souda κ 1278 | lemme | Κελαδείτω | — | lemme seul | oui (SOL) |
| 45 | Eustathe | Eustathius 1718.9 | — | βομβάξ |  | référence de l'auteur, non contrôlée | non |
| 45 | Hésychius | β 787 | glose | βόμβαξ · τοῦτο παρεμβολοειδές ἐστι. σημαίνει δὲ διασυρμόν |  | l'éd. renvoie à Thesm. 45 | oui (Latte I, OCR de la page) |
| 45, 48, 223, 231, 945 | Souda | Souda ε 2807 | glose | βομβάξ … βομβαλομβάξ … ἀττατατατατταῖ … μῦ μῦ … ἰαππαπαιάξ | βομβαλομβάξ (texte βομβαλοβομβάξ, v. 48) ; ἀττατατατατταῖ (texte ἀτταταῖ ἰατταταῖ, v. 223) ; μῦ μῦ (texte μυμῦ, v. 231) | notice Ἐποποῖ (interjections d'Aristophane) | oui (SOL) |
| 48 | Eustathe | Eustathius 790.13, 1718.13 | — | βομβαλοβομβάξ |  | référence de l'auteur, non contrôlée | non |
| 49 | Philostrate | Philostrate Vit. soph. I 9.1 [ | — | καλλιεπὴς |  | référence de l'auteur, non contrôlée | non |
| 50 | Hésychius | π 3188 | glose | πραῖνοι · πρηνίζειν. καταστρέφειν |  | rapprochement de l'auteur (lemme obscur) | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 52 | Zonaras | Zonaras 569 δρύοχοι | — |  |  | référence de l'auteur, non contrôlée | non |
| 52-57 | Souda | Souda δ 1547 | citation | Ἀγάθων ἄρχεται δρυόχους τιθέναι … καὶ χιανεύει καὶ λαικάζει | ἁψῖδας (R ἀσπίδας) ; τορεύει (texte τορνεύει) ; γογγυλίζει (= R ; γογγύλλει Porson) ; χιανεύει (texte χοανεύει) | cf. χ 297, λ 181 | oui (SOL) |
| 52-57 | Souda | Souda χ 297 | citation | Ἀγάθων ἄρχεται δρυόχους τιθέναι … καὶ χιανεύει καὶ λαικάζει | comme δ 1547 |  | oui (SOL) |
| 53 | Hésychius | κ 617 | glose | κάμπτειν · τὸ ἐν τῇ ᾠδῇ καμπὰς ποιεῖν |  | Schmidt renvoie à Thesm. 68, 73 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 53, 56-57 | Scholie | Σ Ach. 79 (Dübner p. 5) | citation | καὶ ἀλλαχοῦ · κάμπτει δὲ νέας ἁψῖδας ἐπῶν, γογγυλίζει καὶ λαικάζει | citation abrégée ; ἁψῖδας (R ἀσπίδας) ; γογγυλίζει (= R) | scholie absente de R (entre parenthèses chez Dübner) ; cf. Souda λ 181 | oui (Dübner, image de la page) |
| 53-57 | Souda | Souda λ 181 | citation | κάμπτει δὲ νέας ἀψῖδας ἐπῶν, τὸ δὲ τορείη καὶ γογγυλίζει καὶ λαικάζει | citation abrégée ; τὸ δὲ τορείη (texte τὰ δὲ τορνεύει) |  | oui (SOL) |
| 54 | Hésychius | τ 1168 | glose | τορνεύει · γλύφει |  |  | oui (Hansen–Cunningham IV, OCR de la page) |
| 55 | Souda | Souda α 2754 | glose | Ἀντονομάζει | — | glose (scholie au v. 55, SOL) | oui (SOL) |
| 56 | Hésychius | γ 764 | glose | γογγύλλειν · συστρέφειν |  | l'éd. renvoie à Thesm. 56 | oui (Latte I, OCR de la page) |
| 56 | Souda | Souda γ 361 | glose | Γογγυλίζει, ἀντὶ τοῦ μεταστρέφει | γογγυλίζει (= R ; γογγύλλει Porson) | la citation qui suit (ὥσπερ γυναικὶ γογγύλην μεμαγμένην) est d'une autre pièce (Paix 28 selon la SOL) | oui (SOL) |
| 56 | Zonaras | Zonaras 449 γογγυλίζει | — |  |  | référence de l'auteur, non contrôlée | non |
| 57 | Eustathe | Eustathius 1153.40 | — | χοανεύει |  | référence de l'auteur, non contrôlée | non |
| 58 | Hésychius | θ 750 | glose | θριγκοῖς · φραγμοῖς |  | marge de l'éd. : « Hom. » (glose rapportée à Homère) | oui (Cunningham IIa, OCR de la page) ; ligne contrôlée sur l'image |
| 62 | Hésychius | χ 575 | glose | χοανεῦσαι · χωνεῦσαι |  | l'éd. renvoie à Thesm. 62 | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 62 | Moeris | Moeris χ 21 | — | χοανεῦσαι = χωνεῦσαι |  | référence de l'auteur, non contrôlée | non |
| 74 | Souda | Souda κ 1487 | citation | οὐ χρῆν σε κρύπτειν ὄντα κηδεστὴν ἐμόν | — |  | oui (SOL) |
| 80 | Hésychius | τ 1440 | glose | τρίτη Θεσμοφορίων · ζητεῖται πῶς ἅμα μὲν λέγει τρίτην Θεσμοφορίων εἶναι, ἅμα δὲ μέσην, τεττάρων οὐσῶν ἡμερῶν |  | issue de la scholie au v. 80 ; l'éd. renvoie à Thesm. 80 | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 93 | Souda | Souda κ 2025 | citation | τὸ πρᾶγμα κομψὸν καὶ σφόδρ' ἐκ τοῦ σοῦ τρόπου | — | « καὶ αὖθις » | oui (SOL) |
| 93-94 | Souda | Souda τ 439 | citation | τὸ πρᾶγμα κομψὸν καὶ σφόδρ' ἐκ τοῦ σοῦ τρόπου · τοῦ γὰρ τεχνάζειν ἡμέτερος ὁ πυραμοῦς | — |  | oui (SOL) |
| 94 | Souda | Souda π 3192 | citation | ἡμέτερος ὁ πυραμοῦς | — | cf. τ 439 | oui (SOL) |
| 96 | Zonaras | Zonaras 678 ἐκκυκλεῖ | — | οὑκκυκλούμενος |  | référence de l'auteur, non contrôlée | non |
| 100 | Hésychius | μ 1904 | glose | Μύρμηκος ἀτραπούς · Ἀθήνησιν ἐν Σκαμβωνιδῶν ἔστι Μύρμηκος ἀτραπός, ἀπὸ ἥρωος Μύρμηκος ὀνομαζομένη |  | Schmidt renvoie à Thesm. 100 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 100 | Photius | Photius μ 606 Μύρμηκος ἀτραπός | — |  |  | référence de l'auteur, non contrôlée | non |
| 100 | Souda | Souda μ 1445 | citation | μυρμήκων ἀτραποὺς ἤ τί διαμινυρίζεται | μυρμήκων (R μύρμηκος) ; διαμινυρίζεται (texte διαμινύρεται) |  | oui (SOL) |
| 105 | Souda | Souda σ 175 | glose | Σεβίσαι, ἀντὶ τοῦ εὐλογῆσαι | — | tiré de la scholie au v. 105 (SOL) | oui (SOL) |
| 105-106 | Souda | Souda σ 178 | citation | εὐπίστως τοὐμὸν δαίμονας ἔχει σεβίσαι | εὐπίστως (= R) ; om. δέ ; ἔχει (R ἔχεις) |  | oui (SOL) |
| 105-106 | Souda | Souda σ 183 | citation | εὐπίστως δὲ τοὐμὸν δαίμονας ἔχει σεβίσαι | εὐπίστως (= R ; εὐπείστως Reiske) ; ἔχει (R ἔχεις) |  | oui (SOL) |
| 115-6 | Eustathe | Eustathius 361.37 | — | Ἄρτεμιν ἀγροτέραν |  | référence de l'auteur, non contrôlée | non |
| 120 | EM | Etymologicum magnum 153.21 Ἀσιάδος κρούματα· τῆς κιθάρας. οὔτως Αριστοφάνης εἶπε, παρῳδῶν τὸ ἐξ Ἐρεχθέως Εὐριπίδου | — |  |  | référence de l'auteur, non contrôlée | non |
| 120 | Et. Gen. | Etymologicum genuinum (AB) α 1271 ed. Lasserre-Livadaras | — |  |  | référence de l'auteur, non contrôlée | non |
| 120 | Photius | α 2957 | lemme | Ἀσιάδος κρούματα (= Synagoge Σᵇ α 2226) | κρούματος (Photius, selon l'apparat de Cunningham) |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge Σᵇ α 2226 ; texte de Photius non lu) |
| 120 | Souda | Souda α 4147 | lemme | Ἀσιάδος κρούματα, τῆς κιθάρας · οὕτως Ἀριστοφάνης | ordre Ἀσιάδος κρούματα (texte κρούματά τ' Ἀσιάδος) | cf. EM 153, 21 ; Photius α 2957 ; Συναγωγή α 2226 (renvois de l'auteur, voir ces sources) | oui (SOL) |
| 120 | Synagoge | Σᵇ α 2226 | lemme | Ἀσιάδος κρούματα · τῆς κιθάρας. οὕτως Ἀριστοφάνης | ordre Ἀσιάδος κρούματα (texte κρούματά τ' Ἀσιάδος) | parallèles : Souda α 4147, Photius α 2957, Et. Gen. | oui (Cunningham, PDF p. 679, OCR) |
| 125 | Scholie | Scholium | — | ἄρσενι βοᾷ δοκιμῳ |  | référence de l'auteur, non contrôlée | non |
| 125 | Souda | Souda α 4016 | lemme | Ἄρσενι βοᾷ δοκίμῳ | δοκίμῳ (= R) |  | oui (SOL) |
| 127 | Souda | Souda δ 891 | lemme | Δι' αἰφνιδίου ὀπός | — | cf. ο 471 | oui (SOL) |
| 127 | Souda | Souda ο 471 | lemme | δι' αἰφνιδίου ὀπός | — | cf. δ 891 | oui (SOL) |
| 128 | Photius | α 164 | glose | ἀγῆλαι · τιμῆσαι … (ἄγαλλε) (= Σᵇ α 145, 2ᵉ partie) |  |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge Σᵇ α 145 ; texte de Photius non lu) |
| 128 | Synagoge | Σᵇ α 145 | glose | ἀγῆλαι · τιμῆσαι θεόν, ἀγλαΐσαι … καὶ ἄγαλλε καὶ προσαγήλει τὸν θεόν … |  | parallèles : Souda α 217, Photius α 163-164 | oui (Cunningham, PDF p. 539, OCR) |
| 129-130 | Souda | Souda ο 194 | glose | Ὀλολύζει ὁ γέρων … | — | tiré de la scholie au v. 129 ; selon la SOL, R porte dans le texte une indication semblable (ὀλολύζεις γέρων), à contrôler sur l'image | oui (SOL) |
| 130 | Hésychius | γ 343 | glose | Γενετυλλίς · γυναικεία θεός, πεποιημένου τοῦ ὀνόματος παρὰ τὰς γενέσεις … |  |  | oui (Latte I, OCR de la page) |
| 130-132 | Souda | Souda γ 141 | citation | ἡδὺ τὸ μέλος, ὦ πότνιαι Γενετυλλίδες … καὶ μανδαλωτόν | — |  | oui (SOL) |
| 131 | Hésychius | θ 491 | glose | θηλυδριῶδες · τὸ κατακεκλασμένον |  | l'éd. renvoie à Thesm. 131 | oui (Cunningham IIa, OCR de la page) |
| 131 | Pollux | Pollux II.109 | — | κατεγλωττισμένον |  | référence de l'auteur, non contrôlée | non |
| 131 | Souda | Souda κ 912 | citation | θηλυδριῶδες καὶ κατεγλωττισμένον | — |  | oui (SOL) |
| 131-132 | Scholie | Σ Ach. 1201 (Dübner p. 30) | glose | Ἄλλως. μανδαλωτόν, εἶδος φιλήματος ποικίλον καὶ ἡδύ, θηλυδριῶδες, καὶ κατεγλωττισμένον |  | = Souda μ 134 ; entre parenthèses chez Dübner | oui (Dübner, image de la page) |
| 131-132 | Souda | Souda μ 134 | citation | θηλυδριῶδες καὶ κατεγλωττισμένον καὶ μανδαλωτόν | — |  | oui (SOL) |
| 132 | Hésychius | μ 224 | glose | μανδαλωτόν · φίλημα ποιὸν οὕτω καλεῖται |  | Schmidt renvoie à Thesm. 132 et Ach. 1201 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 132 | Photius | Photius μ 86, cf. Photius γ 115 | — |  |  | référence de l'auteur, non contrôlée | non |
| 132-133 | Souda | Souda γ 63 | citation | ὥστ' ἐμοῦ γ' ἀκροωμένου τοῦ μέλους … ὑπῆλθε γάργαλος | add. τοῦ μέλους | l'auteur cite « γ 83 » (= Γαιήοχος) : lire γ 63 | oui (SOL) |
| 132-133 | Zonaras | col. 423 | citation | Γαργαλίζει. κινεῖ, ὑποσημαίνει, προτρέπει, [ἐρεθίζει. ὑπὸ τὴν ἕδραν αὐτὴν ὑπῆλθε γάργαλος.] | — | partie entre crochets chez Tittmann ; non relevé par l'auteur | oui (Tittmann I, image de la page) |
| 133 | Moeris | Moeris γ 23, cf. Phrynichus Praep. soph. 56.9 | — | γάργαλος = γαργαλισμός |  | référence de l'auteur, non contrôlée | non |
| 134 | Hésychius | η 948 | glose | ἥτις · ὅστις |  | glose générique ; rapprochement douteux (« ? » chez l'auteur) | oui (Cunningham IIa, OCR de la page) |
| 136 | Hésychius | γ 1015 | glose | γύννις · δειλός, ἄνανδρος, γυναικώδης · Ἀριστοφάνης |  | Aristophane nommé ; l'éd. renvoie à Thesm. 136 | oui (Latte I, OCR de la page) ; ligne contrôlée sur l'image |
| 136 | Souda | Souda γ 504 | citation | ποδαπὸς ὁ γύννις; τίς πάτρα; | — |  | oui (SOL) |
| 136-140 | Souda | Souda β 110 | citation | τίς ἡ στολή; … τίς δὲ κατόπτρου καὶ ξίφους κοινωνία; | ἀξύμφορον (R οὐ ξύμφορον ; Adler suit ici M selon l'apparat de l'auteur) ; δὲ (texte δαί) | l'apparat de l'auteur cite par erreur « Suid. β 190 » au v. 139 | oui (SOL) |
| 137 | Photius | Hesychius β 211 βάρβιτος, cf. Photius β 62 | — | βάρβιτος |  | référence de l'auteur, non contrôlée | non |
| 141-142 | Souda | Souda π 987 | citation | πότερον, ὡς ἀνὴρ τρέφῃ; ποῦ δὲ τὸ πέος; | τρέφῃ (texte τρέφει) ; ποῦ δὲ τὸ πέος (texte καὶ ποῦ πέος) | « καὶ αὖθις » | oui (SOL) |
| 142 | Hésychius | λ 225 | glose | Λακωνικαί |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 142 | Moeris | Moeris χ 19 χλαῖνα | — |  |  | référence de l'auteur, non contrôlée | non |
| 142 | Photius | Photius λ 57 Λακωνικαί | — | Λακωνικαί |  | référence de l'auteur, non contrôlée | non |
| 142 | Scholie | Σ Vesp. 1158 (Dübner p. 161) | citation | ὡς αὐτὸς Ἀριστοφάνης ἐν Θεσμοφοριαζούσαις · ποῦ τὸ πέος ; ποῦ χλαῖνα ; ποῦ Λακωνικαί ; | τὸ πέος (texte καὶ ποῦ πέος) | pièce nommée ; cf. Souda λ 63 | oui (Dübner, image de la page) |
| 142 | Souda | Souda λ 63 | citation | ποῦ τὸ πέος; ποῦ χλαῖνα; ποῦ Λακωνικαί; | τὸ πέος (texte καὶ ποῦ πέος) |  | oui (SOL) |
| 146-147 | Souda | Souda α 1097 | citation | ὦ πρέσβυ, πρέσβυ, τοῦ φθόνου τὸν ψόγον … οὐ παρεσχόμην | om. μέν ; τὴν δὲ (texte τὴν δ') |  | oui (SOL) |
| 149-150 | Apostolius | XVIII 41h (CPG II p. 729) | citation | Χρὴ γὰρ ποιητὴν ἄνδρα πρὸς τὰ δράμματα ἃ δεῖ ποιεῖν, πρὸς ταῦτα τοὺς τρόπους ἔχειν. Ἀριστοφάνους | δράμματα (sic) | attribué à Aristophane | oui (CPG II, image de la page) |
| 159-160 | Souda | Souda α 350 | citation | ἄλλως τ' ἄμουσόν ἐστι … ἀγρεῖον ὄντα καὶ δασύν | — | « καὶ αὖθις » ; reprise de α 1633 | oui (SOL) |
| 159-161 | Souda | Souda α 1633 | citation | ἄλλως τ' ἄμουσόν ἐστι … κ' Ἀνακρέων ὁ Τήϊος | κ' Ἀνακρέων (texte κἀνακρέων) | suivi de « καὶ τὰ ἑξῆς » | oui (SOL) |
| 161-162 | Souda | Souda ε 4049 | citation | Ἀνακρέων, Ἀλκαῖος, οἵπερ ἁρμονίαν ἐχύμισαν | ἐχύμισαν (R ἐχύμησαν) ; Ἀνακρέων, Ἀλκαῖος (texte κἀνακρέων … κἀλκαῖος) |  | oui (SOL) |
| 162 | Hésychius | ε 7681 | glose | ἐχύμισαν · ἤρτυσαν | ἐχύμισαν (R ἐχύμησαν) | l'éd. renvoie à Thesm. 162 | oui (Cunningham IIa, OCR de la page) |
| 162 | Zonaras | Zonaras 942 οἵπερ ἁρμονίαν ἐχύμισαν | — |  |  | référence de l'auteur, non contrôlée | non |
| 162-163 | Souda | Souda ε 989 | citation | κ' Ἀλκαῖος, οἵπερ ἁρμονίαν ἐχύμισαν … διεκίνουν Ἰωνικῶς | ἐχύμισαν (R ἐχύμησαν) ; διεκίνουν (R διεκίνων) |  | oui (SOL) |
| 162-3 | Zonaras | Zonaras 707 ἐμιτροφόρουν | — | κ' Ἀλκαῖος – Ἰωνικῶς |  | référence de l'auteur, non contrôlée | non |
| 163 | Souda | Souda ι 495 | citation | ἐμιτροφόρουν τε καὶ διεκίνουν Ἰωνικῶς | διεκίνουν (R διεκίνων) |  | oui (SOL) |
| 165 | Souda | Souda η 362 | glose | Ἠμπέσχετο | — | glose (texte ἠμπέσχετο ; source incertaine selon la SOL) | oui (SOL) |
| 168 | Scholie | scholium Aves 1295a.α | — | ὁ Φιλοκλέης αἰσχρὸς = κορυδός |  | référence de l'auteur, non contrôlée | non |
| 173 | Souda | Souda β 192 | citation | βαΰζων · καὶ γὰρ ἐγὼ τοιοῦτος ἦν | ἦν (= R) |  | oui (SOL) |
| 173 | Zonaras | col. 379 | citation | Βαΰζων. ὑλακτῶν. Ἀριστοφάνης · βαΰζων γὰρ καὶ ἐγὼ τοιοῦτος ἦν | γὰρ καί (texte καὶ γάρ) |  | oui (Tittmann I, image de la page) |
| 175 | Souda | Souda ζ 63 | citation | οὐ ζηλῶ σε τῆς παιδεύσεως | — |  | oui (SOL) |
| 176 | Scholie | Scholium v. 500 (sed ἀλλ' εἰπεῖν βούλομαι pro ἔα μ' εἰπεῖν) | — |  |  | référence de l'auteur, non contrôlée | non |
| 177-178 | Souda | Souda οι 154 | citation | σοφοῦ πρὸς ἀνδρός, ὅστις ἐν βραχεῖ … οἷός τε συντέμνειν λόγους | — | « καὶ αὖθις » | oui (SOL) |
| 177-180 | Souda | Souda σ 792 | citation | σοφοῦ πρὸς ἀνδρός … ἱκέτης ἀφῖγμαι πρὸς σέ | συντεμεῖν (texte συντέμνειν) ; κοινῇ (= R ; καινῇ Biset) |  | oui (SOL) |
| 179 | Souda | Souda κ 2556 | citation | ἐγὼ δὲ κοινῇ ξυμφορᾷ πεπληγμένος | κοινῇ (= R ; καινῇ Biset) |  | oui (SOL) |
| 191 | Souda | Souda ε 1871 | glose | Ἐξυρημένος | — | glose (source possible : v. 191, SOL) | oui (SOL) |
| 192 | Pollux | Pollux II 111 | — | γυναικόφωνος |  | référence de l'auteur, non contrôlée | non |
| 193 | Eustathe | Eustathius 4.9 | — | ἐποίησάς ποτε |  | référence de l'auteur, non contrôlée | non |
| 195-197 | Souda | Souda υ 709 | citation | μὴ νῦν ἐλπίσῃς τὸ σὸν κακὸν … οἰκείως φέρε | add. ἄν (καὶ γὰρ ἂν μαινοίμεθ' ἄν ; R καὶ γὰρ μαινοίμεθ' ἄν) ; om. ἀλλ' |  | oui (SOL) |
| 198-201 | Souda | Souda τ 440 | citation | τὰς συμφορὰς γὰρ οὐχὶ τοῖς τεχνάσμασι … ἀλλὰ τοῖς παθήμασιν | — |  | oui (SOL) |
| 215-216 | Souda | Souda α 4565 | citation | ἀποξυρεῖν ταδί, τὰ κάτω δ' ἀφαύειν | ἀφαύειν (R ἀφεύειν) | sous Ἀφαυανθήσομαι (… καὶ Ἀφαύειν, καίειν) | oui (SOL) |
| 215-6 | Clément | Clemens Alexandrinus , Στρώματα VI 26.4 Ἀριστοφάνης δὲ ὁ κωμικὸς ἐν ταῖς πρώταις Θεσμοφοριαζούσαις τὰ ἐκ τῶν Κρατίνου Ἐμπιπραμένων μετήνεγκεν ἔπη | — | ἀποξυρεῖν – ἀφεύειν |  | référence de l'auteur, non contrôlée | non |
| 219-220 | Pollux | X 140 (Bethe II p. 232) | citation | ὡς ἐν Θεσμοφοριαζούσαις Ἀριστοφάνης · χρῆσόν τι ἡμῖν ξυρόν. — αὐτὸς λάμβανε ἐντεῦθεν ἐκ τῆς ξυροδόχης | om. νῦν ; ξυροδόχης (texte ξυροδόκης) | pièce nommée | oui (Bethe II, image de la page) |
| 220 | Eustathe | Eustathius 130.43, 1399.38 | — | ξυροδόκης |  | référence de l'auteur, non contrôlée | non |
| 220 | Pollux | Pollux II 32 | — | ξυροδόκης |  | référence de l'auteur, non contrôlée | non |
| 220 | Scholie | Scholium | — | ξυροδόκης |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 227 | Aelius Dionysius | Aelius Dionysius η 9 | — | ἡμίκραιραν |  | référence de l'auteur, non contrôlée | non |
| 227 | Et. Gen. | Etymologicum genuinum (AB) 150 ed. Miller | — | ἡμίκραιραν |  | référence de l'auteur, non contrôlée | non |
| 227 | Eustathe | Eustathius 710.50, 1127.35 | — | ἡμίκραιραν |  | référence de l'auteur, non contrôlée | non |
| 227 | Hésychius | η 496 | glose | ἡμίκραιρα · ἡμικεφάλαιον. σιαγόνος τὸ ἥμισυ |  | l'éd. renvoie à Thesm. 227 | oui (Cunningham IIa, OCR de la page) |
| 227 | Souda | Souda η 334 | citation | τὴν ἡμίκραιραν τὴν ἑτέραν ψιλὴν ἔχων | — |  | oui (SOL) |
| 231 | Apostolius | Michael Apostolius XVI 60c | — | τί – καλῶς |  | référence de l'auteur, non contrôlée | non |
| 231 | Et. Gen. | B, dans Miller, Mélanges, p. 218 | citation | Μύζεις · παρὰ τὸ μῦ · Ἀριστοφάνης · μῦ μῦ. — Τί μύζεις ; … τί μύζεις ; πάντα πεποίηται καλῶς · Ἀριστοφάνης Θεσμοφοριαζούσαις | μῦ μῦ (texte μυμῦ) | pièce nommée | oui (Miller, image de la page) |
| 231 | Eustathe | Eustathius 440.23 | — | μύζεις |  | référence de l'auteur, non contrôlée | non |
| 231 | Eustathe | Eustathius 723.9 | — | μῦ μῦ |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 231 | Souda | Souda μ 1383 | citation | τί μύζεις; πάντα πεποίηται καλῶς | lemme Μῦ, μῦ (texte μυμῦ) |  | oui (SOL) |
| 232 | Souda | Souda ψ 105 | citation | οἴμοι κακοδαίμων · ψιλὸς αὖ στρατεύσομαι | αὖ (= R) |  | oui (SOL) |
| 236-237 | Souda | Souda α 4594 | glose | Ἀφευθεὶς τὸν πρωκτόν · Ἀριστοφάνης ἀντὶ τοῦ φλογισθείς | — | tiré de la scholie (cf. δ 205) | oui (SOL) |
| 237 | Souda | Souda δ 205 | citation | οἴμοι κακοδαίμων, δελφάκιον γέγονα | γέγονα (texte γενήσομαι) | suivi d'une scholie (ἀφευθεὶς τὸν πρωκτόν) | oui (SOL) |
| 244-245 | Photius | α 2946 | citation | ἄσβολος · θηλυκῶς … Ἀριστοφάνης ἐν Θεσμοφοριαζούσαις · τὰ πλεῖστα γὰρ ἀποπεπόνηκας. φεῦ ἰοὺ τῆς ἀσβόλου | — | glose citée aussi par Naber (Prolegomena, I p. 147, d'après « p. 450, 32 »), qui la rapporte à Aelius Dionysius | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge Σᵇ α 2213 ; texte de Photius non lu) ; texte cité par Naber, contrôlé sur l'image |
| 244-245 | Synagoge | Σᵇ α 2213 | citation | ἄσβολος · θηλυκῶς ἡ ἄσβολος … Ἀριστοφάνης Θεσμοφοριαζούσαις · τὰ πλεῖστα γὰρ ἀποπεπόνηκας. φεῦ ἰοὺ τῆς ἀσβόλου | — | pièce nommée ; parallèles : Photius α 2946, Ael. Dion. α 186 | oui (Cunningham, PDF p. 678, OCR) |
| 244-5 | Aelius Dionysius | Aelius Dionysius α 186 | — | τὰ πλεῖστα – ἀσβόλου |  | référence de l'auteur, non contrôlée | non |
| 245 | Hésychius | α 7634 | glose | ἄσβολος · ἀσβόλη |  |  | oui (Latte I, OCR de la page) |
| 245 | Moeris | Moeris α 17 | — | ἄσβολος = ἀσβόλη |  | référence de l'auteur, non contrôlée | non |
| 245 | Phrynichus | Phrynicus Praep. soph 28.1 (ἄσβολος fem.) | — | ἄσβολος = ἀσβόλη |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 245 | Souda | Souda α 3473 | glose | Ἀποπεπόνηκας | — | glose (scholie au v. 245 selon Adler) | oui (SOL) |
| 245 | Souda | Souda α 4132 | citation | φεῦ, ἰοὺ τῆς ἀσβόλου | — |  | oui (SOL) |
| 246 | Eustathe | Eustathius 1385.59 | — | αἰθὸς |  | référence de l'auteur, non contrôlée | non |
| 246 | Eustathe | Eustathius 83.6, 992.60, 1314.15 | — | αἰθὸς γεγένημαι |  | référence de l'auteur, non contrôlée | non |
| 246 | Hésychius | τ 1243 | glose | τράμις · τὸ ⟨τ⟩ρῆμα τῆς ἕδρας, ὁ ὄρ⟨ρ⟩ος (Hippon. fr. 114a W.) … |  | l'éd. ne renvoie pas aux Thesm. | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 246 | Photius | τ 415 | glose | τράμις · ὁ ὄρρος ἢ ἡ διαγραφή · ἢ τὸ τρῆμα τοῦ ἀρχοῦ |  |  | oui (Theodoridis III, PDF p. 516) |
| 246 | Souda | Souda αι 135 | glose | Αἰθός | — | glose | oui (SOL) |
| 246 | Souda | Souda τ 903 | citation | αἰθὸς γεγένημαι πάντα τὰ περὶ τὸν τράμιν | γεγένημαι (R γεγέννημαι) ; τόν (texte τήν) |  | oui (SOL) |
| 248 | Moeris | Moeris π 79 | — | πλυνεῖ |  | référence de l'auteur, non contrôlée | non |
| 254 | Hésychius | π 3096 | glose | πόσθ[ο]ιον · αἰδοῖον ἀνδρός |  | l'éd. renvoie à Thesm. 254 | oui (Hansen III, OCR de la page) |
| 254 | Photius | π 1113 | glose | πόσθιον · αἰδοῖον · ἢ τὴν Ἀφροδίτην |  |  | oui (Theodoridis III, PDF p. 284) |
| 257-258 | Souda | Souda π 1165 | citation | ἥδιον μὲν οὖν κεφαλὴ περίθετος, ἣν ἐγὼ νύκτωρ φορῶ | ἥδιον (texte ἡδί) |  | oui (SOL) |
| 258 | Eustathe | Eustathius 1280.63 | — |  |  | référence de l'auteur, non contrôlée | non |
| 258 | Photius | π 690 | citation | περίθετος κεφαλή · ἡ περιθετή. Ἀριστοφάνης · „κεφαλὴ περίθετος, ἣν ἐγὼ νύκτωρ φορῶ“ | — | Aristophane nommé | oui (Theodoridis III, PDF p. 239) |
| 258 | Pollux | Pollux II 35 | — | κεφαλὴ περίθετος |  | référence de l'auteur, non contrôlée | non |
| 261 | Souda | Souda ε 135 | citation | φέρ' ἔγκυκλον · τουτὶ λάμβαν' ἀπὸ τῆς κλινίδος | τουτί (R τοῦτι) ; λάμβαν' (= R ; λάβ' Daubuz) | « καὶ ἀλλαχοῦ » ; cf. κ 1809 | oui (SOL) |
| 261 | Souda | Souda κ 1809 | citation | ἔγκυκλον · τουτὶ λάμβαν' ἀπὸ τῆς κλινίδος | τουτί (R τοῦτι) ; λάμβαν' (= R) |  | oui (SOL) |
| 263 | Souda | Souda χ 7 | citation | χαλαρὰ γοῦν χαίρεις φορῶν ὑποδήματα | χαίρεις (= R ; χαίροις codd. FV de la Souda, imprimé par l'auteur) ; add. ὑποδήματα |  | oui (SOL) |
| 274 | Hésychius | α 7097 | glose | ἄρδην · φοράδην. ἢ σφόδρα. ἢ παντελῶς. ἢ ἀθρόως … |  | glose générique | oui (Latte I, OCR de la page) |
| 274 | Souda | Souda α 3806 | glose | Ἄρδην | — | glose (scholie au v. 274, SOL) | oui (SOL) |
| 275-6 | Eustathe | Eustathius 443.37 | — |  |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 277-278 | Souda | Souda σ 325 | citation | ὡς τὸ τῆς ἐκκλησίας σημεῖον ἐν τῷ Θεσμοφόρῳ φαίνεται | Θεσμοφόρῳ (R Θεσμοφορίῳ) |  | oui (SOL) |
| 282 | Aelius Dionysius | Aelius Dionysius α 113 | — |  |  | référence de l'auteur, non contrôlée | non |
| 282 | Photius | Photius α 1386 | — |  |  | référence de l'auteur, non contrôlée | non |
| 285 | Eustathe | Eustathius 437.4 | — | πόπαν᾽ |  | référence de l'auteur, non contrôlée | non |
| 289 | Euripide (test.) | Euripides, testimonia 4, 18 Kannicht Χοιρίλη | — | χοῖρον |  | référence de l'auteur, non contrôlée | non |
| 291 | Hésychius | θ 50 | glose | θάλλικα · σάκκου εἶδος |  | rapprochement de l'auteur avec θάληκον (texte) | oui (Cunningham IIa, OCR de la page) |
| 291 | Pollux | Pollux X 152 θυλάκιον [...] ἐπὶ τοῦ αὐτοῦ δὲ καὶ σακίον, ὅταν φῇ ἐν Θεσμοφοριαζούσαις | — | θάληκον |  | référence de l'auteur, non contrôlée | non |
| 292 | Photius | ρ 106 | glose | ῥήτορα · καὶ τὴν γυναῖκα. Ἀριστοφάνης |  | Aristophane nommé ; l'éd. renvoie à Thesm. 292 | oui (Theodoridis III, PDF p. 349) |
| 295 | Souda | Souda ε 3797 | lemme | Εὐφημία ἔστω | — | formule (scholie au v. 295 selon la SOL) | oui (SOL) |
| 299 | Hésychius | κ 472 | glose | Καλλιγένειαν · οὐ τὴν γῆν, ἀλλὰ τὴν Δήμητραν … |  | Schmidt : « Aristoph. » ; cf. Thesm. II fr. 331 K.-A. (renvoi de l'auteur, à propos de Photius κ 118) ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 299 | Photius | Photius κ 118 (= fr. Aristophanes 331 Kassel-Austin) | — | Καλλιγενείᾳ = Δημήτερι |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 300 | Hésychius | κ 3865 | glose | Κουροτρόφος · παιδοτρόφος. ὑφ' ἑτέρων ἡ Δημήτηρ |  | Schmidt renvoie à Callimaque et à Thesm. 300 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 300 | Scholie | scholium vet. in Hesiodus Opera et dies 227-9 | — | Κουροτρόφῳ = Δημήτηρ |  | référence de l'auteur, non contrôlée | non |
| 322-324 | Souda | Souda οι 181 | citation | σύ τε Πόντιε Πόσειδον, προλιπὼν μυχὸν ἰχθυόεντ' οἰστροδόνητον | om. σεμνέ et ἁλιμέδον ; ἰχθυόεντ' (= R) |  | oui (SOL) |
| 335-7 | Satyros | Satyrus Vit. Euripid. (= The Oxyrhynchus Papyri IX 1176) fr. 39 col. XII 8-16 (Εὐριπιδίῳ pro Εὐριπίδῃ (?)) | — |  |  | référence de l'auteur, non contrôlée | non |
| 336 | EM | Etymologicum magnum 360.21 | — | 'πικηρυκεύεται |  | référence de l'auteur, non contrôlée | non |
| 336 | Et. Gen. | Etymologicum genuinum (B) | — | 'πικηρυκεύεται |  | référence de l'auteur, non contrôlée | non |
| 336 | Hésychius | ε 4853 | glose | ἐπικηρυκεύεται · προκηρύσσεται |  | l'éd. renvoie à Thuc. 7, 83, 2 (« cf. » chez l'auteur) | oui (Cunningham IIa, OCR de la page) |
| 336 | Photius | ε 1580 | glose | ἐπικηρυκεύεται (= Synagoge ε 682 = Souda ε 2375) |  |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge ε 682 ; texte de Photius non lu) |
| 336 | Souda | Souda ε 2375 | glose | Ἐπικηρυκεύεται | — | glose générique (Thucydide selon la SOL) ; l'auteur la range au v. 336 | oui (SOL) |
| 336 | Synagoge | Σ ε 682 | glose | ἐπικηρυκεύεται · διὰ κήρυκός τινος συνθήκας τινὰς ἢ πρεσβείας ποιεῖται |  | parallèles : Souda ε 2375, Photius ε 1580, Et. Gen. | oui (Cunningham, PDF p. 228, OCR) |
| 341 | Hésychius | π 3308 | glose | προαγωγός · διδάσκαλος κακῶν. καὶ μαστροπός. μαυλιστής … |  | l'éd. renvoie à Thesm. 341 | oui (Hansen III, OCR de la page) |
| 341 | Souda | Souda ε 1271 | citation | προαγωγὸς οὖσ' ἐνετρύλλισε τῷ δεσπότῃ | — |  | oui (SOL) |
| 341 | Souda | Souda π 2307 | glose | Προαγωγός | — | glose | oui (SOL) |
| 341 | Zonaras | Zonaras 745 οὔ σ' ἐνετρύλλησεν | — | ἐνετρύλλισεν |  | référence de l'auteur, non contrôlée | non |
| 347-348 | Souda | Souda χ 394 | citation | εἴ τις κάπηλος ἢ καπηλὶς τοῦ χοὸς … διαλυμαίνεται | εἴ (texte κεἴ) ; χοός (= R) | l'apparat de l'auteur cite par erreur « Suid. λ 394 » | oui (SOL) |
| 363-364 | Souda | Souda α 3501 | citation | ἀπόρρητά τε τοῖσιν ἐχθροῖσι τοῖς ἡμετέροις λέγουσιν | ἀπόρρητά (texte τἀπόρρητα) ; ἐχθροῖσι (texte ἐχθροῖς) ; λέγουσιν (= R ; λέγουσ' Bentley) |  | oui (SOL) |
| 369-371 | Souda | Souda π 444 | citation | ὥσθ' ἡμῖν θεοὺς παραστατεῖν καίπερ γυναιξὶν οὔσαις | — | attribué par erreur au Ploutos (« Ἀριστοφάνης Πλούτῳ ») | oui (SOL) |
| 373-374 | Souda | Souda ε 2616 | citation | Τιμόκλει' ἐπιστάτει · Λύσιλλ' ἐγραμμάτευε | Τιμόκλει' (= R ; Ἀρ[χίκλ]ει' P.Oxy. 1176) ; ἐπιστάτει (texte ἐπεστάτει) |  | oui (SOL) |
| 377-378 | Souda | Souda χ 481 | citation | καὶ χρηματίζειν πρῶτα περὶ Εὐριπίδου, ὅ τι χρὴ παθεῖν | — |  | oui (SOL) |
| 377-8 | Lex. Vind. | Lexicon Vindobonense 190.10 | — | καὶ χρηματίζειν – παθεῖν |  | référence de l'auteur, non contrôlée | non |
| 380 | Souda | Souda π 1166 | citation | περίθου νῦν τόνδε πρότερον, πρὶν λέγειν | πρότερον (R πρῶτον) |  | oui (SOL) |
| 381 | Phrynichus | Phrynichus Praep. soph. 126.1 | — | χρέμπτεται |  | référence de l'auteur, non contrôlée | non |
| 383-384 | Souda | Souda φ 431 | citation | φιλοτιμίᾳ μὲν οὐδεμιᾷ, μὰ τὼ θεώ, λέξουσ' ἀνέστην, ὦ γυναῖκες | — |  | oui (SOL) |
| 389 | Hésychius | ε 5195 | glose | ἐπισμῇ · ἐπιτρίβει, ἀπὸ τοῦ σμήχειν ἢ τρίβειν ἢ πλύνειν · λοιδορεῖ, πλήττει … |  | l'éd. renvoie à Thesm. 389 | oui (Cunningham IIa, OCR de la page) |
| 389 | Souda | Souda ε 2592 | citation | τί γὰρ οὗτος ἡμᾶς οὐκ ἐπισμῇ τῶν κακῶν | — | avec la scholie (Diodore) | oui (SOL) |
| 389 | Souda | Souda σ 747 | glose | Σμώχειν · τὸ λοιδορεῖν | — | reste de la scholie au v. 389 (SOL ; cf. ε 2592) | oui (SOL) |
| 390-1 | Scholie | scholium Plato Gorgias 457b | — |  |  | référence de l'auteur, non contrôlée | non |
| 390-1 | Scholie | scholium Plato Hippias min. 365d | — |  |  | référence de l'auteur, non contrôlée | non |
| 390-1 | Scholie | scholium Plato Theages 127c (πῶς pro ποῦ et τραγῳδικοὶ pro τραγῳδοὶ καὶ) | — |  |  | référence de l'auteur, non contrôlée | non |
| 390-391 | Souda | Souda ε 955 | citation | ποῦ δ' οὐχὶ διαβέβληχ' ὅπου περ ἔμβραχυ εἰσὶ θεαταί; | ἔμβραχυ (R ἐν βραχύ) | cf. οι 128 | oui (SOL) |
| 390-394 | Souda | Souda οι 128 | citation | ποῦ δ' οὐχὶ διαβέβληχ' … τὰς μέγ' ἀνδράσι κακόν | ἔμβραχυ (R ἐν βραχύ) ; οἷς θέα καὶ τραγῳδία (texte εἰσὶν θεαταὶ καὶ τραγῳδοί) | suivi d'une note de Symmaque (παρὰ τὸ πιπίζειν) | oui (SOL) |
| 392 | Eustathe | Eustathius 380.15 | — | ἀνδρεραστρίας |  | référence de l'auteur, non contrôlée | non |
| 392 | Phrynichus | Phrynichus Praep. soph. 34.18 | — | ἀνδρεραστρίας |  | référence de l'auteur, non contrôlée | non |
| 392 | Pollux | Pollux III 71 | — | ἀνδρεραστρίας |  | référence de l'auteur, non contrôlée | non |
| 393 | Scholie | scholium Aves 307 | — | οἰνοπίπας |  | référence de l'auteur, non contrôlée | non |
| 395 | Hésychius | ι 501 | glose | ἴκρια · ἡ καθέδρα τοῦ κυβερνήτου … καὶ τὰ ἐπὶ τοῖς ξύλοις κατασκευαζόμενα θεωρεῖα … |  |  | oui (Cunningham IIa, OCR de la page) ; ligne contrôlée sur l'image |
| 395-396 | Souda | Souda ι 275 | citation | ὥστ' εὐθὺς εἰσιόντες ἀπὸ τῶν ἰκρίων ὑποβλέπουσ' ἡμᾶς | — |  | oui (SOL) |
| 404 | Hésychius | κ 3629 | glose | Κορίνθιος ξένος |  | numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 413 | Apostolius | V 93b (CPG II p. 361) | citation | Δέσποινα γὰρ γέροντι νυμφίῳ γυνή. Ἀριστοφάνους | — | vers d'Euripide (fr. 804, 3 Kannicht, γαμοῦντι chez Ménandre selon Leutsch) cité au v. 413 | oui (CPG II, image de la page) |
| 413 | Ménandre | Menandros Monostich. 191 (= Euripides fr. 804.3 ed. Kannicht) | — |  |  | référence de l'auteur, non contrôlée | non |
| 417 | EM | Etymologicum magnum 590.53 | — | μορμολυκεῖα |  | référence de l'auteur, non contrôlée | non |
| 421-427 | Souda | Souda κ 159 | citation | οἱ γὰρ ἄνδρες ἤδη κλειδία φοροῦσι … ἐδίδαξε θριπηδέστατα | κλειδία (texte κλῄδια) ; om. αὐτοί ; Λακωνικά (texte Λακωνίκ') ; om. ᾡκότριψ Εὐριπίδης ; θριπηδέστατα (texte θριπήδεστ') | sous Κακοηθέστατα ; cf. λ 64 | oui (SOL) |
| 421-428 | Souda | Souda λ 64 | citation | οἱ γὰρ ἄνδρες ἤδη κλειδία φοροῦσι … σφραγῖδα ἐξαψαμένους | κλειδία ; om. αὐτοί, τρεῖς, ᾡκότριψ Εὐριπίδης ; Λακωνίκα ; ἐδίδαξε (R -ξεν) ; θριπηδέστατ' (texte θριπήδεστ') ; σφραγῖδα (texte σφραγίδια) | l'auteur cite « λ 54 » (= Λακιδέας) : lire λ 64 | oui (SOL) |
| 422 | Eustathe | Eustathius 974.37, 1108.25, 1603.52 | — | κακοηθέστατα |  | référence de l'auteur, non contrôlée | non |
| 423 | Phrynichus | Phrynichus Praep. soph. 61.1 | — | γομφίους |  | référence de l'auteur, non contrôlée | non |
| 426 | Aelius Dionysius | Aelius Dionysius ο 8-9 | — | οἰκότριψ = οἰκοτραφής |  | référence de l'auteur, non contrôlée | non |
| 426 | Hésychius | ο 265-266 | glose | οἰκότριψ |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 426 | Moeris | Moeris ο 25 | — | οἰκότριψ = οἰκοτραφής |  | référence de l'auteur, non contrôlée | non |
| 427 | Souda | Souda θ 503 | glose | Θριπηδέστατον | — | tiré de la scholie au v. 427 (SOL) ; texte θριπήδεστ' | oui (SOL) |
| 428-429 | Souda | Souda κ 2771 | citation | ἐμοὶ τούτῳ δοκεῖ, ὄλεθρόν τινα κυρκανᾶν ἀμωσγέπως | τινα, om. ἡμᾶς ; ἀμωσγέπως (= R) |  | oui (SOL) |
| 429 | Eustathe | Eustathius 1213.50 | — | κυρκανᾶν |  | référence de l'auteur, non contrôlée | non |
| 429 | Hésychius | α 4182 | glose | ἀμωσγέπως · ὁπωσδήποτε καὶ ἐκ παντὸς τρόπου |  |  | oui (Latte I, OCR de la page) ; ligne contrôlée sur l'image |
| 429 | Hésychius | κ 4691 | glose | κυρκανᾷ · κυκᾷ, ταράσσει |  | Schmidt renvoie à Hippocrate ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 429 | Photius | Photius κ 1254 κυρκανᾶν | — | κυρκανᾶν |  | référence de l'auteur, non contrôlée | non |
| 429 | Souda | Souda α 1645 | glose | Ἀμωσγέπως : ὁπωσδήποτε … | — | glose (même notice dans Σ Plat. Phaedr. 228c selon la SOL) | oui (SOL) |
| 429 | Synagoge | Σ α 449 | glose | ἁμωσγέπως · ὁπωσδήποτε, ἔν γέ τινι, καθ' ὁντιναοῦν τρόπον |  |  | oui (Cunningham, PDF p. 104, OCR) |
| 432 | Eustathe | Eustathius 1484.53 | — | μετὰ τῆς γραμματέως συγγράψομαι |  | référence de l'auteur, non contrôlée | non |
| 432 | Pollux | Pollux IV 19 | — | τῆς γραμματέως |  | référence de l'auteur, non contrôlée | non |
| 437-439 | Souda | Souda ε 22 | citation | πάσας δ' ἰδέας ἐξήτασε … πυκνῶς τε ποικίλως λόγους ἀνεῦρεν | ἰδέας (R εἰδέας) ; ἐξήτασε, ἐβάστασε (R -σεν) ; ποικίλως (texte ποικίλους) ; ἀνεῦρεν (= R ; ἀνηῦρεν Meineke) |  | oui (SOL) |
| 438 | Hésychius | π 4335 | glose | πυκνῶς · συνεχῶς, συχνῶς |  | l'éd. renvoie à Thesm. 438 (e.g.) | oui (Hansen III, OCR de la page) |
| 442 | Aelius Dionysius | Aelius Dionysius α 107 | — | ἄντικρυς |  | référence de l'auteur, non contrôlée | non |
| 442 | Photius | Photius α 2210 ἄντικρυς | — | ἄντικρυς |  | référence de l'auteur, non contrôlée | non |
| 446 | Hésychius | ε 239 | glose | ἔγκυος · ἐγγαστρωμένη γυνή |  | glose générique | oui (Cunningham IIa, OCR de la page) |
| 447-9 | Scholie | scholiumᵀ Plato Hipparch. 229d (μυρίναις pro μυρρίναις et μέν οὐκ ἄν pro μὲν οὖν ἀλλ᾽) | — | μόλις – τέως μὲν οὖν ἀλλ᾽ |  | référence de l'auteur, non contrôlée | non |
| 449 | Pollux | Pollux VI 161 | — | ἡμικάκως |  | référence de l'auteur, non contrôlée | non |
| 449 | Souda | Souda τ 321 | citation | τέως μὲν οὖν, ἀλλ' ἡμικάκως ἐβοσκόμην | — |  | oui (SOL) |
| 453-6 | Aulu-Gelle | Aulus Gellius XV 20.7 | — |  |  | référence de l'auteur, non contrôlée | non |
| 455-456 | Plutarque | Comp. Ar. Men. 1, 853c | citation | ἄγρια γὰρ ἡμᾶς, ὦ γυναῖκες, δρᾷ κακά, ἅτ' ἐν ἀγρίοισι τοῖς λαχάνοις αὐτὸς τραφείς | — | exemple du style d'Aristophane | oui (Perseus, TEI, éd. Bernardakis) |
| 457-458 | Souda | Souda σ 1591 | citation | δεῖ γὰρ ἀνδράσι πλέξαι στεφάνους συνθηματιαίους εἴκοσι | — |  | oui (SOL) |
| 458 | Athénée | XV 680c-d (Kaibel 15, 26) | citation | συνθηματιαῖοι στέφανοι … Ἀριστοφάνης ἐν Θεσμοφοριαζούσαις · πλέξαι στεφάνους συνθηματιαίους εἴκοσιν | — | pièce nommée | oui (Perseus, TEI, pages de Casaubon) |
| 458 | Hésychius | σ 2624 | glose | συνθηματιαῖοι · οἱ ἠργολαβημένοι καὶ ἐκδεδομένοι, ἐκδόσιμοι |  | l'éd. renvoie à Thesm. 458 | oui (Hansen III, OCR de la page) |
| 458 | Pollux | Pollux VII 200 | — | στεφάνους συνθηματιαίους |  | référence de l'auteur, non contrôlée | non |
| 459-460 | Souda | Souda λ 441 | citation | ἕτερον αὖ τι λῆμα τοῦτο κομψότερον ἔτ' ἢ τὸ πρότερον ἀναπέφηνε | — | « καὶ αὖθις » | oui (SOL) |
| 466 | Photius | ο 380 | glose | ὀξυθυμεῖσθαι, οὐχὶ ὀξυθυμεῖν λέγουσιν · τὸ ὀργίζεσθαι ἀκραχόλως |  |  | oui (Theodoridis III, PDF p. 120) |
| 468 | Hésychius | θ 146 | glose | θαυμάσιος · θαυμαστός |  | glose générique | oui (Cunningham IIa, OCR de la page) |
| 468 | Moeris | Moeris θ 16 | — | θαυμάσιον = θαυμαστόν |  | référence de l'auteur, non contrôlée | non |
| 469 | Hésychius | ο 852 | glose | ὀναίμην |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 469 | Photius | ο 332 | glose | ὀναίμην · ἀπολαύσω, ἐπιτύχοιμι | ὀναίμην (R ὀνοίμην) |  | oui (Theodoridis III, PDF p. 114) |
| 469 | Souda | Souda ο 330 | citation | καὐτὴ γὰρ ἐγώ, οὕτως ὀναίμην τῶν τέκνων | ἐγώ (texte ἔγωγ') ; ὀναίμην (R ὀνοίμην) |  | oui (SOL) |
| 469 | Synagoge | Σ ο 162 | glose | ὀναίμην · ἐπιτύχοιμι, ἀπολαύσω |  | parallèles : Souda ο 330, Photius (Porson 335, 25) | oui (Cunningham, PDF p. 372, OCR) |
| 470 | Souda | Souda μ 328 | citation | μισῶ τἄνδρ' ἐκεῖνον, εἰ μὴ μαίνομαι | τἄνδρ' (texte τὸν ἄνδρ') |  | oui (SOL) |
| 473-474 | Souda | Souda τ 683 | citation | τί ταῦτ' ἔχουσαι κεῖνον αἰτιώμεθα βαρέως τε φέρομεν; | κεῖνον (= R ; 'κεῖνον Meineke) |  | oui (SOL) |
| 480 | Hésychius | δ 1558 | glose | διεκόρησε · διέφθειρε κόρην …, διεπαρθένευσε | διεκόρησε (= texte ; διεκόρευσεν Pollux) | l'éd. renvoie à Thesm. 480 (?) | oui (Latte I, OCR de la page) ; ligne contrôlée sur l'image |
| 480 | Pollux | Pollux III 42 (οὗτος pro ὅσπερ et διεκόρησεν cod. A pro διεκόρευσεν) | — |  |  | référence de l'auteur, non contrôlée | non |
| 480 | Souda | Souda δ 591 | glose | Διακορεῦσαι | — | glose (texte διεκόρησεν ; διεκόρευσεν Pollux III 42) | oui (SOL) |
| 481 | Eustathe | Eustathius 1746.6 (μοὔκνυεν ἕλκων pro μου ᾽κνυεν ἐλθὼν) | — |  |  | référence de l'auteur, non contrôlée | non |
| 481 | Hérodien | Περὶ καθολικῆς προσῳδίας (Lentz, GG III.1) | citation | καὶ παρὰ τῷ κωμικῷ ἐν Θεσμοφοριαζούσαις · οὗτος πόθῳ μου ἔκνυεν ἐλθὼν τὴν θύραν | — | pièce nommée ; texte reconstitué par Lentz à partir de sources tardives (cf. Eustathe 1746, 6 chez l'auteur) | oui (First1K, TEI, éd. Lentz) |
| 481 | Souda | Souda ε 520 | citation | οὗτος πόθῳ μου 'κνυεν ἐλθὼν τὴν θύραν | — |  | oui (SOL) |
| 481 | Zonaras | Zonaras 669 ἔκνυεν | — |  |  | référence de l'auteur, non contrôlée | non |
| 484 | Eustathe | Eustathius 503.20 | — | στρόφος |  | référence de l'auteur, non contrôlée | non |
| 486 | Hésychius | κ 1980 | glose | κεδρίδες |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 486 | Photius | Photius κ 1980 κ 517 | — | κεδρίδας |  | référence de l'auteur, non contrôlée | non |
| 486 | Souda | Souda σ 1712 | citation | κᾆθ' ὁ μὲν ἔτριβε κεδρίδας, ἄνηθον, σφάκον | ἄνηθον (= R ; ἄννηθον Dindorf) |  | oui (SOL) |
| 489 | Moeris | Moeris α 13 | — | Ἀγυιᾶ |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 489 | Étienne de Byzance | Stephanus Byzantinus 22.15 | — | Ἀγυιᾶ |  | référence de l'auteur, non contrôlée | non |
| 493-494 | Souda | Souda λ 434 | citation | μάλισθ' ὅταν ὑπό του ληκώμεθα τὴν νύχθ' ὅλην | ὅταν après μάλισθ' (texte ὅταν μάλισθ') ; ληκώμεθα (= Rac ; κινώμεθα Rpc) ; add. ὅλην |  | oui (SOL) |
| 504 | Phrynichus | Phrynichus Praep. soph. 129.3 | — | ὠκυτόκι᾽ |  | référence de l'auteur, non contrôlée | non |
| 504 | Pollux | Pollux II 7 | — | ὠκυτόκι᾽ |  | référence de l'auteur, non contrôlée | non |
| 506 | Hésychius | κ 2549 | glose | κηρίῳ βύσασα |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 506 | Photius | Photius κ 675 κηρίῳ βῦσαι | — | κηρίῳ βεβυσμένον |  | référence de l'auteur, non contrôlée | non |
| 509 | Moeris | Moeris η 14 | — | ἦτρον |  | référence de l'auteur, non contrôlée | non |
| 509 | Souda | Souda η 637 | citation | τὸ γὰρ ἦτρον τῆς χύτρας ἐλάκτισεν | — |  | oui (SOL) |
| 509 | Zonaras | col. 1012 | citation | Ἦτρον … Ἀριστοφάνης · τὸ γὰρ ἦτρον τῆς χύτρας ἐλάκτισε | — |  | oui (Tittmann I, image de la page) |
| 514 | Aelius Dionysius | Aelius Dionysius ε 26 | — |  |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 514 | Eustathe | Eustathius 1857.10, 462.40 | — |  |  | référence de l'auteur, non contrôlée | non |
| 514 | Pollux | Pollux IX 131 (λέων² omisso et αὐτὸ ἔκμαγμα pro αὐτέκμαγμα) | — |  |  | référence de l'auteur, non contrôlée | non |
| 514-516 | Souda | Souda λ 271 | citation | λέων, λέων σοι γέγονεν ἔκμαγμα σόν … στρεβλὸν ὥσπερ κύτταρον | ἔκμαγμα (R αὖτ' ἔκμαγμα ; αὐτέκμαγμα Reiske) | lemme (v. 514) et citation (515-516) ; cf. π 2114 | oui (SOL) |
| 514-516 ; 254 | Souda | Souda π 2114 | citation | λέων, λέων σοι γέγονεν ἔκμαγμα σόν … ὥσπερ κύτταρον στρεβλόν ; νὴ τὴν Ἀφροδίτην, ἡδύ γ' ὄζει ποσθίου | ἔκμαγμα (R αὖτ' ἔκμαγμα) ; ὥσπερ κύτταρον στρεβλόν (texte στρεβλὸν ὥσπερ κύτταρον) |  | oui (SOL) |
| 515-516 | Souda | Souda κ 2787 | citation | πόσθιον τῷ σῷ προσόμοιον, στρεβλὸν ὥσπερ κύτταρον | — |  | oui (SOL) |
| 516 | Hésychius | κ 4747 | glose | κύτταρον |  | référence de l'auteur ; vol. κ–ο de Latte absent, glose non retrouvée dans l'OCR de Schmidt | non |
| 516 | Hésychius | σ 1977 | glose | στρεβλόν · καμπύλον, σκολιόν |  | l'éd. renvoie à Thesm. 516 | oui (Hansen III, OCR de la page) |
| 516 | Photius | Photius κ 1270 | — | κύτταρον |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 527-530 | Souda | Souda α 1073 | citation | ἀλλ' ἅπαν γένοιτ' ἂν ἤδη … μὴ δάκῃ ῥήτωρ ἀθρεῖν | ἀλλ' ἅπαν (= R ; ἀλλὰ πᾶν Cobet) | lemme et citation ; suit le proverbe ὑπὸ παντὶ λίθῳ σκορπίος εὕδει | oui (SOL) |
| 528-530 | Stobée | III 13, 29 (Hense p. 457) | citation | Ἀριστοφάνους · τὴν παροιμίαν ἐπαινῶ τὴν παλαιάν · ὑπὸ λίθῳ γὰρ παντί που χρὴ μὴ δάκῃ ῥήτωρ ἀθρεῖν | om. δ' ; (cod. L : λιθίω, χρῆνα) | attribué à Aristophane | oui (Hense, image de la page) |
| 531-532 | Souda | Souda α 1349 | citation | ἀλλ' οὐ γάρ ἐστι τῶν ἀναισχύντων … πλὴν ἄλλαι γυναῖκες | ἄλλαι (R ἄρ' εἰ) | le texte de l'auteur porte ἀναισχύτων (coquille ?) | oui (SOL) |
| 536-537 | Scholie | Σ B Il. 1, 137 (Dindorf III p. 33) | citation | καὶ πάλιν · εἰ μὲν οὖν ἔστι τις · εἰ δὲ μή, ἡμεῖς τε καὶ τὰ δουλάρια τέφραν ποθὲν ληψόμεθα | ἔστι τις (texte τις ἔστιν) ; ἡμεῖς τε (texte ἡμεῖς αὐταί γε) ; ληψόμεθα (texte λαβοῦσαι) |  | oui (First1K, TEI, éd. Dindorf) |
| 536-537 | Scholie | Σ T Il. 1, 135 (Maass V p. 17) | citation | καὶ ἐν Θεσμοφοριαζούσαις · εἰ μὲν οὖν τις ἔστιν · εἰ δὲ μή, ἡμεῖς τε καὶ τὰ δουλάρια τέφραν ποθὲν λαβοῦσαι | ἡμεῖς τε (texte ἡμεῖς αὐταί γε) | pièce nommée ; = Σ bT Il. 1, 135-137 (Erbse) chez l'auteur | oui (First1K, TEI, éd. Maass) |
| 554 | Et. Gen. | Etymologicum genuinum (A) ᾔδεισθα | — | ᾔδησθ᾽ |  | référence de l'auteur, non contrôlée | non |
| 557 | Souda | Souda σ 512 | citation | σιφωνίζομεν τὸν σῖτον | τὸν σῖτον (= R ; τὸν κύσθον conj. de l'auteur) |  | oui (SOL) |
| 560 | Souda | Souda κ 996 | citation | ἑτέρα τὸν ἄνδρα τῷ πελέκει κατεσπόδησε | ἑτέρα en tête, om. γυνή (R τὸν ἄνδρα τῷ πελέκει γυνή) |  | oui (SOL) |
| 566 | Scholie | Σ Eq. 435 (Ald.), Dübner, adnot. p. 406 | citation | καὶ ἀλλαχοῦ · οὔτοι μὰ τὼ θεὼ σὺ καταπροίξει λέγουσα ταυτί | — | addition de l'Aldine, interpolée de la Souda (κ 730) selon Dübner | oui (Dübner, image de la page) |
| 566 | Souda | Souda κ 730 | citation | οὔτοι, μὰ τὼ θεώ, σὺ καταπροίξῃ λέγουσα ταυτί | καταπροίξῃ (texte καταπροίξει) |  | oui (SOL) |
| 567 | EM | Etymologicum magnum 323.25 | — | ἐκποκιῶ |  | référence de l'auteur, non contrôlée | non |
| 567 | Hésychius | ε 1637 | glose | ἐκποκιῶ · ἐκτιλῶ |  | l'éd. renvoie à Thesm. 567 | oui (Cunningham IIa, OCR de la page) |
| 567 | Hésychius | π 2750 | glose | ποκάδες · τρίχες … ἀπὸ τοῦ πέκεσθαι, ὅθεν καὶ πόκος |  | l'éd. renvoie à Thesm. 567 | oui (Hansen III, OCR de la page) |
| 567 | Photius | π 1010 | glose | πλοκάδες · τρίχες | πλοκάδες (texte ποκάδας) |  | oui (Theodoridis III, PDF p. 272) |
| 567 | Souda | Souda ε 588 | citation | ἐκποκιῶ σου τὰς ποκάδας | ποκάδας (= R) |  | oui (SOL) |
| 567 | Zonaras | col. 672 | citation | [Ἐκποκιῶ. τὰς τρίχας ἐκσπάσω. Ἀριστοφάνης · ἐκποκιῶ σου τὰς ποκάδας …] | — | entre crochets chez Tittmann | oui (Tittmann I, image de la page) |
| 570 | Epim. Hom. | Epimerismi alphabetici in Homerum (ed. Cramer) ε 201 | — | χεσεῖν |  | référence de l'auteur, non contrôlée | non |
| 572-573 | Souda | Souda ο 292 | citation | πρὶν οὖν ὁμοῦ γενέσθαι, σιγᾶθ', ἵν' αὐτῆς πυθώμεθα | om. κοσμίως |  | oui (SOL) |
| 574 | Souda | Souda ξ 83 | lemme | Ξυγγενεῖς τοὐμοῦ τρόπου | — |  | oui (SOL) |
| 576 | Souda | Souda π 2541 | lemme | Προξενῶ θ' ὑμᾶς ἀεί | ὑμᾶς (R ὑμῶν) |  | oui (SOL) |
| 598 | Hésychius | ε 2095 | glose | ἐλινύειν · σχολάζειν, λήγειν, ὀκνεῖν, ἀναπαύεσθαι … |  | glose générique | oui (Cunningham IIa, OCR de la page) |
| 598 | Hésychius | ε 2097 | glose | ἐλινύων · ἀναπαυόμενος |  | l'éd. renvoie à Arrien, An. 4, 30, 1 | oui (Cunningham IIa, OCR de la page) |
| 598 | Moeris | Moeris ε 61 (ἐλινύων = ἀναπαυόμενος) | — | ἐλινύειν |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 601-602 | Souda | Souda π 2540 | citation | καὶ σὺ ξυνέξευρ' αὐτόν … αὐτήν τε κἀκείνην ἔχῃς, ὦ πρόξενε | ξυνέξευρ' (R συνέξευρ') ; αὐτήν (R ταύτην) |  | oui (SOL) |
| 616 | Souda | Souda σ 1163 | citation | στραγγουριῶ · χθὲς γὰρ ἔφαγον κάρδαμα | χθὲς γάρ (texte γάρ · ἐχθές) |  | oui (SOL) |
| 620 | Hésychius | κ 3218 | glose | Κοθωκίδαι · δῆμος |  | Schmidt renvoie à la scholie au v. 620 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 620 | Photius | Photius κ 859 Κοθωκίδαι (ap Scholium) | — | Κοθωκιδῶν |  | référence de l'auteur, non contrôlée | non |
| 630-631 | Souda | Souda π 2563 | citation | φέρ' ἴδω, τί μέντοι πρῶτον ἦν; … προὐπίνομεν | μέντοι (= Rpc in mg.) ; μετά (R με) |  | oui (SOL) |
| 633 | Photius | σ 286 | glose | σκάφιον · τάχα λέγει τὸν καδίσκον, ᾧ καταχέονται αἱ γυναῖκες … |  |  | oui (Theodoridis III, PDF p. 393) |
| 633 | Pollux | X 45 (Bethe II p. 201) | citation | ἄμφω δὲ παράλληλα ἐν Πολυίδῳ Ἀριστοφάνης · σκάφιον Ξένυλλ' ἤτησεν · οὐ γὰρ ἦν ἁμίς | — | attribué par erreur au Polyidos (« immo Thesm. 633 » Bethe) | oui (Bethe II, image de la page) |
| 641 | Hésychius | σ 1769 | glose | στερίφη · στεῖρα, μὴ τεκοῦσα, μηδὲ τίκτουσα |  | l'éd. renvoie à Thesm. 641 | oui (Hansen III, OCR de la page) |
| 641 | Moeris | Moeris σ 46 (στερίφη = στερρά) | — | στερίφη |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 641 | Photius | σ 532 | glose | στερίφη · στεῖρα · μὴ τεκοῦσα · μηδὲ τίκτουσα |  |  | oui (Theodoridis III, PDF p. 421) |
| 641 | Souda | Souda σ 1049 | glose | Στερίφη · στεῖρα, μὴ τεκοῦσα | — | glose ; cf. Hésychius σ 1769, Συναγωγή σ 214, Photius σ 532 (SOL) | oui (SOL) |
| 647-648 | Souda | Souda ι 640 | citation | ἰσθμόν τιν' ἔχεις, ἄνθρωπ', … πυκνότερον Κορινθίων | ἄνθρωπ' (R ὦνθρωπε) | suivi de la scholie (διϊσθμονίσαι) | oui (SOL) |
| 648 | Souda | Souda δ 1048 | glose | Διισθμονίσαι | — | tiré de la scholie au v. 648 (cf. ι 640) | oui (SOL) |
| 659 | Hésychius | ε 8 | glose | ἔα δή · ἄγε δή | ἔα δή (texte εἶα δή) | l'éd. renvoie à Thesm. 659 | oui (Cunningham IIa, OCR de la page) |
| 659 | Photius | ε 1 | glose | ἔα δή · ἄγε δή (= Synagoge ε 1 = Souda ε 3) | ἔα δή (texte εἶα δή) |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge ε 1 ; texte de Photius non lu) |
| 659 | Souda | Souda ε 3 | glose | Ἔα δή · ἄγε δή | ἔα δή (texte εἶα δή) | glose ; cf. Hésychius ε 8, Photius ε 1, Συναγωγή ε 1 (renvois de l'auteur) | oui (SOL) |
| 659 | Synagoge | Σ ε 1 | glose | ἔα δή · ἄγε δή | ἔα δή (texte εἶα δή) | parallèles : Souda ε 3, Photius ε 1 | oui (Cunningham, PDF p. 189, OCR) |
| 692 | Souda | Souda κ 1260 | glose | Κέκραθι · κράξον | — | glose (texte κέκραχθι) | oui (SOL) |
| 696-697 | Scholie | Σ Plut. 453 (Dübner p. 349) | citation | ὡς παρὰ τουτῳῒ τῷ ποιητῇ ἐν Θεσμοφοριαζούσαις · γυναῖκες οὐκ ἀρήξετ' ; οὐ πολλὴν βοὴν στήσεσθε καὶ τροπαῖον ; | — | pièce nommée ; accentuation τροπαῖον discutée par la scholie | oui (Dübner, image de la page) |
| 696-7 | Grégoire de Corinthe | Gregor. Corinth. p.20-22 cf. schol.ᴬˡᵈ Plutus 453c | — | γυναῖκες – τροπαῖον |  | référence de l'auteur, non contrôlée | non |
| 701 | Souda | Souda ν 222 | glose | τέρας νεοχμόν · Ἀριστοφάνης | ordre τέρας νεοχμόν (texte νεοχμὸν αὖ τέρας) | rapprochement incertain (la SOL renvoie à Photius ν 154) | oui (SOL) |
| 702 | CPG | Corpus paroemiographorum Graecorum, Appendices, I, 35 (sed ἔργα omisso) | — | ἅπαντα pro ἅπαν γὰρ ἐστὶν – κἀναισχυντίας |  | référence de l'auteur, non contrôlée | non |
| 702 | Laur. LVIII 24 | Laurentiamus LVIII 24 p. 40 (ed. Cohn) (sed δοῦλα pro ἔργα) | — | ἅπαντα pro ἅπαν γὰρ ἐστὶν – κἀναισχυντίας |  | référence de l'auteur, non contrôlée | non |
| 702 | Souda | Souda α 2902 | lemme | Ἅπαντα τόλμης πλέα κἀναισχυντίας | ἅπαντα (R ἅπαν γὰρ ἐστὶν) ; πλέα (R ἔργα) | emploi proverbial (ἐπὶ τῶν ἰταμῶν) ; cf. CPG, Append. I 35 | oui (SOL) |
| 710 | Photius | Photius η 88 ἥκειν· ἀντὶ τοῦ ἥκων | — |  |  | référence de l'auteur, non contrôlée | non |
| 710-713 | Souda | Souda η 170 | citation | ἀλλ' οὖν ἥκεις γ' ὅθεν ἥκεις … λήψῃ δὲ κακόν | ἥκεις γ' (R ἥκεις τ') ; φαύλως τ' … οὐ λέξεις (= R) ; λήψῃ (texte λήψει) |  | oui (SOL) |
| 729 | Hésychius | θ 862 | glose | θυμάλωψ · ἡ λιγνυώδης τοῦ πυρὸς ἀναφορά … |  |  | oui (Cunningham IIa, OCR de la page) |
| 729 | Photius | Photius θ 256 Θυμάλωψ, Hesychius θ 861 | — | θυμάλωπα |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 729 | Souda | Souda θ 547 | glose | Θυμάλωπες | — | glose (aussi Ach. 321) | oui (SOL) |
| 730-731 | Souda | Souda κ 2408 | citation | σὺ δὲ τὸ Κρητικὸν ἀπόδυθι ταχέως | σὺ δὲ τὸ (R σὺ τόδε τὸ) |  | oui (SOL) |
| 731 | Hésychius | κ 4087 | glose | Κρητικόν · ἱματίδιον λεπτὸν καὶ βραχύ … |  | Schmidt renvoie à Eupolis ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 734 | Eustathe | Eustathius 1522.12 | — | Περσικὰς |  | référence de l'auteur, non contrôlée | non |
| 735 | EM | Etymologicum magnum 31.13 | — | ποτίσταται |  | référence de l'auteur, non contrôlée | non |
| 735 | Et. Sym. | Etymologicum Symeonis α 241 (ed. Lasserre-Livadaras) | — |  |  | référence de l'auteur, non contrôlée | non |
| 735 | Eustathe | Eustathius 1441.23 | — |  |  | référence de l'auteur, non contrôlée | non |
| 735, 737 | Souda | Souda θ 251 | citation | ὦ θερμόταται γυναῖκες, μέγα καπήλοις καλόν, ἡμῖν δὲ κακόν | om. ὦ ποτίσταται … πιεῖν (735-736) et ὦ (737) ; καλόν (texte ἀγαθόν) ; δέ (texte δ' αὖ) |  | oui (SOL) |
| 742 | Antiatticiste | Antiatticista (ed. Bekker) 98.11 | — | ἤνεγκον |  | référence de l'auteur, non contrôlée | non |
| 742 | Phrynichus | Phrynichus Praep. soph. 73.1 | — | ἤνεγκον |  | référence de l'auteur, non contrôlée | non |
| 745 | Hésychius | τ 1645 | glose | τυννοῦ⟨το⟩ν · τὸν μικρόν |  | l'éd. renvoie à Thesm. 745 | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 745 | Photius | τ 552 | glose | τυννοῦτο · δεικτικῶς τὸ μικρόν |  |  | oui (Theodoridis III, PDF p. 535) |
| 747 | Souda | Souda δ 1168 | citation | (ἐξ αὐτοῦ) σχεδὸν τοσοῦτον, ὅσον ἐκ Διονυσίων | ὅσον (R et P.Oxy. 3839 καὶ ὅσον ; χὤσον Bentley) | cité comme proverbe | oui (SOL) |
| 749 | Hésychius | ε 2458 | glose | ἐμπίπραται · καίεται, ἐμπυρίζεται |  | glose générique | oui (Cunningham IIa, OCR de la page) |
| 749 | Souda | Souda ε 1018 | glose | Ἐμπίπραται · ἐμπυρίζεται | — | glose générique (texte ἐμπίμπρατε) | oui (SOL) |
| 749 | Zonaras | Zonaras 709 | — | ἐμπίμπρατε |  | référence de l'auteur, non contrôlée | non |
| 754 | Photius | σ 850 | glose | σφαγεῖον · τὸ ἀγγεῖον εἰς ὃ τὸ αἷμα τῶν σφαζομένων ἱερείων δέχονται · περισπᾶται ἡ δευτέρα συλλαβή |  |  | oui (Theodoridis III, PDF p. 455) |
| 754 | Souda | Souda σ 1702 | glose | Σφαγεῖον | — | tiré de la scholie au v. 754 (SOL) | oui (SOL) |
| 769-775 | Souda | Souda π 45 | citation | οἶδα δ' ἐγὼ καὶ δὴ πότερον ἐκ τοῦ Παλαμήδους … κἀκεῖν' ἦν ξύλον | οἶδα δ' (texte οἶδ') ; πότερον (texte πόρον) ; om. 771b ; γ' ἔκειντο (R γένοιτ' ἄν) ; om. πόθεν; πόθεν; τί δ' ἂν εἰ ; ταδὶ τἀγάλματα (R εἶτα διὰ τἀγάλματ') ; om. τῶν | citation entrecoupée de la scholie | oui (SOL) |
| 770-771 | Souda | Souda π 1702 | citation | ὥσπερ Παλαμήδης τὰς πλάτας ῥίψω γράφων Ναυπλίῳ | ὥσπερ Παλαμήδης (texte ἐκ τοῦ Παλαμήδους · ὡς ἐκεῖνος) ; add. Ναυπλίῳ | version négligée de la scholie (SOL, cf. π 45) | oui (SOL) |
| 777 | Souda | Souda π 2064 | citation | ἐγχειρεῖν χρὴ ἔργῳ πορίμῳ | χρή (= R ; χρῆν Bentley) |  | oui (SOL) |
| 778-779 | Souda | Souda σ 742 | citation | ἄγε δὴ πινάκων ξεστῶν δέλτοι, δέξασθε σμίλης ὁλκούς | — |  | oui (SOL) |
| 778-780 | Pollux | X 58 (Bethe II p. 206) | citation | καὶ Ἀριστοφάνης δὲ ἐν Θεσμοφοριαζούσαις ἔφη · πινάκων ξεστῶν δέξασθε σμίλης ὁλκούς, κήρυκας ἐμῶν μόχθων | om. ἄγε δή et δέλτοι | pièce nommée | oui (Bethe II, image de la page) |
| 800, 810 | Moeris | Moeris β 8 | — | βελτίους = βελτίονες |  | référence de l'auteur, non contrôlée | non |
| 805 | Hésychius | σ 88 | glose | Σαλαβακχώ · πόρνης ὄνομα. ἀπὸ δὲ ταύτης καὶ τὰς καταφερεῖς … οὕτως ἔλεγον Ἀττικοί |  | l'éd. renvoie à Cav. 765 et Thesm. 805 | oui (Hansen III, OCR de la page) |
| 805 | Souda | Souda κ 2692 | glose | Κύννα καὶ Σαλαβακχώ | — | onomastique (la citation est de Cav. 765) | oui (SOL) |
| 808-809 | Souda | Souda β 431 | citation | τίς βουλευτής ἐστι, παραδοὺς ἑτέρῳ τὴν βουλείαν; | om. ἀμείνων |  | oui (SOL) |
| 809 | Antiatticiste | Antiatticista (ed. Bekker) 84.30 | — | παραδοὺς ἑτέρῳ τὴν βουλείαν |  | référence de l'auteur, non contrôlée | non |
| 809 | Harpocration | Harpocration B 19 | — | βουλείαν |  | référence de l'auteur, non contrôlée | non |
| 809 | Hésychius | β 921 | glose | βουλεῖα · [ἡ τοῦ] βουλευτήρια καὶ ⟨ἡ τοῦ⟩ βουλεύειν ἀρχή |  | l'éd. renvoie à Thesm. 809 | oui (Latte I, OCR de la page) ; ligne contrôlée sur l'image |
| 809 | Photius | β Photius β 233 βουλία | — | βουλείαν |  | référence de l'auteur, non contrôlée | non |
| 816 | Aelius Dionysius | Aelius Dionysius γ 3 | — | γάστριδας |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 816 | Photius | Photius γ 40 γάστρις | — | γάστριδας |  | référence de l'auteur, non contrôlée | non |
| 816 | Souda | Souda γ 72 | glose | Γάστρις | — | glose (texte γάστριδας) ; cf. Photius γ 40 (renvoi de l'auteur) | oui (SOL) |
| 834 | Hésychius | σ 1825 | glose | στήνια · ἑορτὴ Ἀθήνησι · καὶ διασκώπτουσι καὶ λοιδοροῦσιν |  | l'éd. renvoie à Thesm. 834 | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 834 | Souda | Souda σ 1089 | glose | Στήνια καὶ Σκίρα · ἑορταὶ γυναικῶν | — | tiré de la scholie au v. 834 (SOL) | oui (SOL) |
| 838 | Aelius Dionysius | Aelius Dionysius σ 23 | — | σκάφιον ἀποκεκαρμένην |  | référence de l'auteur, non contrôlée | non |
| 838 | Eustathe | Eustathius 907.40, 1292.61 | — | σκάφιον ἀποκεκαρμένην |  | référence de l'auteur, non contrôlée | non |
| 838 | Hésychius | σ 879 | glose | σκαφίον · πτύον. καὶ εἶδος κουρᾶς τῆς κεφαλῆς … |  | l'éd. renvoie à Ois. 806 et Thesm. 838 | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 838 | Photius | σ 291 | lemme | σκάφιον ἀποκεκαρμένην · καὶ σκαφιόκουρον τὸν κείροντα | — | l'éd. renvoie à Thesm. 838 | oui (Theodoridis III, PDF p. 393) |
| 838 | Photius | σ 292 | glose | σκάφιον · ἔστιν καὶ εἶδος κουρᾶς, ὡς Ἀντιφῶν καὶ Ἀριστοφάνης |  | l'éd. renvoie à Ar. fr. 153 K.-A., non aux Thesm. | oui (Theodoridis III, PDF p. 394) |
| 846 | Aelius Dionysius | Aelius Dionysius ι 6 | — | ἰλλός |  | référence de l'auteur, non contrôlée | non |
| 846 | Eustathe | Eustathius 768.9 | — | ἰλλός |  | référence de l'auteur, non contrôlée | non |
| 846 | Hésychius | η 257 | glose | ἠίλλοντο · ἐστράβιζον |  |  | oui (Cunningham IIa, OCR de la page) |
| 846 | Hésychius | ι 578 | glose | ἰλλός · στρεβλός, στραβός, διεστραμμένος |  | l'éd. renvoie à Thesm. 846 | oui (Cunningham IIa, OCR de la page) ; ligne contrôlée sur l'image |
| 846 | Pollux | Pollux II 52 | — | ἰλλός |  | référence de l'auteur, non contrôlée | non |
| 846 | Souda | Souda ι 323 | citation | ἴλλος γεγένημαι · ὁ δ' οὐδέπω | om. προσδοκῶν |  | oui (SOL) |
| 846 | Zonaras | Zonaras 1103 ἰλλός | — |  |  | référence de l'auteur, non contrôlée | non |
| 852 | Hésychius | κ 3232 | glose | κοικύλλειν · περιβλέπειν … |  | Schmidt renvoie à Thesm. 852 ; numéro de Latte non contrôlé (vol. II absent) | partiel (glose lue dans Schmidt, éd. minor, OCR ; n° non vérifié) |
| 852 | Photius | Photius κ 860 | — | κοικύλλεις |  | référence de l'auteur, non contrôlée | non |
| 852 | Souda | Souda κ 2534 | citation | τί αὖ σὺ κυρκανᾷς, ἢ τί κοικύλλεις ἔχων; | ἢ τί (= R ; τί Faber) |  | oui (SOL) |
| 857 | Souda | Souda μ 459 | lemme | Μελανοσυρμαῖον λεών | — |  | oui (SOL) |
| 861 | Hésychius | φ 938 | glose | Φρυνώνδας · πονηρούς |  |  | oui (Hansen–Cunningham IV, OCR de la page) |
| 861 | Souda | Souda φ 770 | glose | Φρυνώνδας | — | onomastique (la citation est de l'Amphiaraos) ; l'auteur cite « φ 700 » (= Φρενήρης) : lire φ 770 | oui (SOL) |
| 861 | Synagoge | Σ φ 211 | glose | Φρυνώνδας · τοὺς πονηρούς, ἀπὸ Φρυνώνδα τινός |  | parallèle : Souda φ 770 (et non φ 700) | oui (Cunningham, PDF p. 509, OCR) |
| 863 | Souda | Souda γ 496 | citation | πρὶν τῆς ἑτέρας γυναικίσεως δίκην δοῦναι | δοῦναι après δίκην (R après ἑτέρας) |  | oui (SOL) |
| 868 | Souda | Souda τ 648 | lemme | Τί οὖν ἔτι ζῇ τῶν κοράκων πονηρίᾳ | ζῇ (texte ζῶ) |  | oui (SOL) |
| 869 | Souda | Souda αι 161 | citation | αἰκάλλει τι καρδίαν ἐμήν | — |  | oui (SOL) |
| 869 | Zonaras | Zonaras 91 (τι omisso) | — | αἰκάλλει τι καρδίαν ἐμήν |  | référence de l'auteur, non contrôlée | non |
| 870 | Antiatticiste | Antiatticista (ed. Bekker) 107.31 | — | μὴ ψεῦσον |  | référence de l'auteur, non contrôlée | non |
| 870 | Scholie | Gregor. Corinth. p.14-15 (= scholium^(Mosch.) Euripides, Hecub. 225) (sed ἡμέρας pro ἐλπίδος) | — |  |  | référence de l'auteur, non contrôlée | non |
| 870 | Scholie | Σ Eur. Hec. 225 (Dindorf I p. 273) | citation | τὸ Ἀριστοφάνους ἐν Θεσμοφοριαζούσαις παράδειγμα · μὴ ψεῦσον, ὦ Ζεῦ, τῆς ἐπιούσης ἡμέρας | ἡμέρας (texte ἐλπίδος) | pièce nommée ; scholie tirée de Grégoire de Corinthe p. 14 selon Dindorf | oui (First1K, TEI, éd. Dindorf) |
| 870 | Souda | Souda ψ 62 | citation | μὴ ψεῦσον, ὦ Ζεῦ, τῆς ἐπιούσης ἐλπίδος | — | attribué à Sophocle (« καὶ ὁ Σοφοκλῆς ») ; cf. Grégoire de Corinthe et Σ Eur. Hec. 225 (voir ces sources) | oui (SOL) |
| 878 | Souda | Souda οι 1 | citation | ὦ δύστηνος, οἷ πεπλώκαμεν; | — |  | oui (SOL) |
| 902 | Photius | Photius α 2059 ἀνταυγεῖς κόρας | — | ἀνταυγεῖς κόρας |  | référence de l'auteur, non contrôlée | non |
| 902 | Souda | Souda α 2617 | lemme | ἀνταυγεῖς κόρας · στρέψον ἀνταυγεῖς κόρας | — |  | oui (SOL) |
| 904 | Antiatticiste | Antiatticista (ed. Bekker) 83.9 | — |  |  | référence de l'auteur, non contrôlée | non |
| 904 | Hésychius | α 8572 | glose | ἀφασία · ἀφωνία … στέρησις. σιωπή, ἀναυδία |  | glose générique | oui (Latte I, OCR de la page) |
| 910 | Souda | Souda ι 778 | citation | ἐγὼ δὲ Μενέλεων ὅσον ἐκ τῶν ἰφύων | Μενέλεων (R Μενέλαον) ; ὅσον (R ὅσα γ') ; ἰφύων (R ἀφύων ; = Σ) |  | oui (SOL) |
| 912 | Hésychius | ε 6447 | glose | ἐσχάραι · πυραί … καὶ αἱ τῶν γυναικῶν φύσεις … |  |  | oui (Cunningham IIa, OCR de la page) |
| 912 | Photius | Photius ε 2044 ἐσχάρας | — | ἐσχάρας |  | référence de l'auteur, non contrôlée | non |
| 922 | Photius | Photius α 518 | — | ᾐγυπτιάζετ᾽ |  | référence de l'auteur, non contrôlée | non |
| 922 | Souda | Souda αι 75 | glose | Αἰγυπτιάζειν | — | glose (texte ᾐγυπτιάζετ') ; cf. Photius α 518, Συναγωγή α 494 (renvois de l'auteur) | oui (SOL) |
| 922 | Synagoge | Σᵇ α 494 | glose | αἰγυπτιάζειν · τὸ πανουργεῖν καὶ κακοτροπεύεσθαι |  |  | oui (Cunningham, PDF p. 568, OCR) |
| 926 | Souda | Souda η 379 | lemme | Ἢν ἐμπνέω · ἕως οὗ ζῶ | ἥν (texte ἤνπερ) |  | oui (SOL) |
| 928 | Diogénien | III 35 (CPG I p. 221) | citation | Αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπακεν · ἐπὶ τῶν μηδὲν ἑλκυσάντων | ἔσπακεν (ἔσπασεν Eustathe et alii, d'après la note de Leutsch) | la note de Leutsch énumère d'autres témoins : Grég. Chypr. I 1, Apostol. IV 85, Arsen. 84, Σ Vesp. 175, Σ Thesm. 928, Eust. Il. p. 760, 45, Souda (s. αὕτη, μήρινθος, ὁμοῦ), Bekker, Anecd. I 464, 27, Bachmann, Anecd. I p. 165 | oui (CPG I, image de la page) |
| 928 | Eustathe | Eustathius 760.44 | — |  |  | référence de l'auteur, non contrôlée | non |
| 928 | Grégoire de Chypre | I 1 (CPG I) | citation | Αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασεν · ἀπὸ τῶν ἁλιευτῶν τῶν μηδὲν ἑλκυσάντων εἴρηται | — |  | oui (First1K, TEI) |
| 928 | Grégoire de Chypre | recueil de Moscou I 1 (CPG II p. 93) | citation | Αὕτη ἡ μήρινθος οὐδὲν ἔσπασεν · ἀπὸ τῶν ἁλιευτῶν εἴρηται | om. μέν |  | oui (CPG II, image de la page) |
| 928 | Scholie | Σ Vesp. 175 (Dübner p. 139) | citation | παρὰ τὴν παροιμίαν · αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασεν | — | proverbe | oui (Dübner, image de la page) |
| 928 | Souda | Souda α 4475 | citation | αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασε | — | proverbe ; cf. μ 978 | oui (SOL) |
| 928 | Souda | Souda μ 978 | citation | αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασεν | — | proverbe | oui (SOL) |
| 931 | Aelius Dionysius | Aelius Dionysius σ 7 | — | σανίδι |  | référence de l'auteur, non contrôlée | non |
| 931 | Hésychius | σ 169 | glose | σανίς · θύρα … τίθεται δὲ καὶ ἐπὶ τοῦ ⟨σ⟩ταυροῦ |  | l'éd. renvoie à Thesm. 931, 940 | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 931 | Photius | σ 65 | glose | σανίδα · τὸ δεσμωτικὸν ξύλον |  |  | oui (Theodoridis III, PDF p. 368) |
| 931, 940 | Photius | σ 68 | glose | σανίς · καὶ ἐν ᾗ τοὺς κακούργους ἔδουν, καὶ ἐν ᾗ τὰς δίκας ἐνεχάραττον · τὸ μὲν ἐν Θεσμοφοριαζούσαις, τὸ δὲ ἐν Σφηξὶ δεδήλωται |  | pièce nommée | oui (Theodoridis III, PDF p. 368) |
| 935 | Souda | Souda ι 691 | citation | ὀλίγου ταύτην ἱστιορράφος | ταύτην (texte μ' ἀφείλετ' αὐτόν) | citation abrégée ou corrompue | oui (SOL) |
| 940 | Hésychius | δ 926 | glose | δῆσαι πρὸς σανίδι · Ἀττικῶς · βασανίσαι ἐν τῷ δεσμωτηρίῳ |  | l'éd. renvoie à Thesm. 940 (?) | oui (Latte I, OCR de la page) ; ligne contrôlée sur l'image |
| 942 | Hésychius | ε 6411 | glose | ἑστιῶν · ἀριστοποιῶν |  | l'éd. renvoie à Thesm. 942 | oui (Cunningham IIa, OCR de la page) |
| 942 | Photius | ε 2031 | glose | ἑστιῶν · ἀριστοποιῶν (= Synagoge ε 875 = Souda ε 3227) |  |  | oui (n° et identité de la glose confirmés par l'apparat de Cunningham à la Synagoge ε 875 ; texte de Photius non lu) |
| 942 | Phrynichus | Phrynichus Praep. soph. 66.7 | — | ἑστιῶν |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 942 | Souda | Souda ε 3215 | citation | τοῖς κόραξιν ἑστιῶν | — |  | oui (SOL) |
| 942 | Souda | Souda ε 3227 | glose | Ἑστιῶν · ἀριστοποιῶν | — | glose ; même notice dans Συναγωγή ε 875, Photius ε 2031, Hésychius ε 6411 (SOL) | oui (SOL) |
| 942 | Synagoge | Σ ε 875 | glose | ἑστιῶν · ἀριστοποιῶν |  | parallèles : Souda ε 3227, Photius ε 2031 | oui (Cunningham, PDF p. 239, OCR) |
| 948 | Souda | Souda α 2364 | citation | ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχωμεν | θεαῖν (= R ; θεοῖν Cobet) | l'auteur date le passage du v. 947 ; variantes des manuscrits de la Souda (θεῶν, θεεῖν…) relevées par l'auteur d'après Adler, non contrôlées | oui (SOL) |
| 968 | Hésychius | ε 6929 | glose | εὔκυκλος · εὔχωρος |  |  | oui (Cunningham IIa, OCR de la page) |
| 968 | Photius | Photius ε 2236 | — | εὐκύκλου |  | référence de l'auteur, non contrôlée | non |
| 973 | Hésychius | τ 400 | glose | Τελεία · … ἡ Ἥρα |  | l'éd. renvoie à Esch. Eum. 214 et Thesm. 973 | oui (Hansen–Cunningham IV, OCR de la page) ; ligne contrôlée sur l'image |
| 973 | Souda | Souda τ 271 | glose | Τελεία · Ἥρα Τελεία … | — | tiré de la scholie au v. 973 (SOL) | oui (SOL) |
| 986 | Souda | Souda τ 789 | citation | τόρευε πᾶσαν ᾠδήν | — |  | oui (SOL) |
| 1054 | Souda | Souda αι 245 | glose | Αἰόλαν · σκοτεινήν | — | glose | oui (SOL) |
| 1059 | Eustathe | Eustathius 1761.26 ἐκτίθεται καινοφώνους λέξεις οἷον [ ... ] καὶ τὸ ἐπικοκκάζειν ὕβρει ἤ κατά τινας ἐπιμηκάζειν, ὃθεν παρὰ Ἀριστοφάνει τὸ ‘ἀοιδὸς ἐπικοκκάστρια' | — | ἀντῳδὸς ἐπικοκκάστρια |  | référence de l'auteur, non contrôlée | non |
| 1059 | Souda | Souda η 686 | lemme | Ἠχὼ λόγων ἀντῳδὸς ἐπικοκκάστρια | — | variantes des manuscrits de la Souda (ἐπικαγχάστρια…) relevées par l'auteur d'après Adler, non contrôlées | oui (SOL) |
| 1066-1067 | Souda | Souda ι 531 | citation | ὡς μακρὸν ἵππευμα διώκεις ἀστεροειδέα νῶτα διφρεύουσ' αἰθέρος | — |  | oui (SOL) |
| 1066-8 | Zonaras | Zonaras 1117 | — | ὡς μακρὸν – αἰθέρος |  | référence de l'auteur, non contrôlée | non |
| 1067 | Moeris | Moeris ν 6 | — | νῶτα |  | référence de l'auteur, non contrôlée | non |
| 1067-1068 | Souda | Souda αι 122 | citation | ἀστεροειδέα νῶτα διφρεύουσ' αἰθέρος ἱερᾶς | — | « καὶ αὖθις » (sous Αἰθήρ) | oui (SOL) |
| 1067-8 | Zonaras | Zonaras 67, 78 (sed ἀστρο- pro ἀστερο-) | — |  |  | référence de l'auteur, non contrôlée | non |
| 1125 | Moeris | Moeris δ 28 | — | δεσμά |  | référence de l'auteur, non contrôlée | non |
| 1139 | Phrynichus | Phrynichus Praep. soph. 100.3 | — | ἄζυγα |  | référence de l'auteur, non contrôlée | non |
| 1169 | Photius | σ 608 | glose | στρατιάν · συστέλλοντες τὴν δευτέραν συλλαβὴν … οὕτως Ἀριστοφάνης |  | Aristophane nommé | oui (Theodoridis III, PDF p. 429) |
| 1174 | Photius | Photius α 1514 ἀνακαλπάζει | — | κἀνακάλπασον |  | référence de l'auteur, non contrôlée | non |
| 1174 | Scholie | Scholium | — | κἀνακάλπασον |  | référence de l'auteur, non contrôlée | non |
| 1174 | Souda | Souda κ 263 | glose | Καλπάζειν · τὸ ἁβρῶς βαδίζειν | — | lu dans First1KGreek (Adler) ; l'auteur cite « κ 623 » (= Κατάληψις) : lire κ 263 | oui (First1K) |
| 1174 | Zonaras | Zonaras 1171 καλπάζειν· τὸ ἄκρως βαδίζειν | — | κἀνακάλπασον |  | référence de l'auteur, non contrôlée (« cf. ») | non |
| 1175 | Hésychius | π 2005 | glose | περσικά · … καὶ ὄρχησις Περσική |  | l'éd. renvoie à Thesm. 1175 (cf.) | oui (Hansen III, OCR de la page) |
| 1175 | Pollux | Pollux IV 100 | — | Περσικόν |  | référence de l'auteur, non contrôlée | non |
| 1175 | Souda | Souda τ 340 | citation | σὺ δ', ὦ Τερηδών, ἐπαναφύσα Περσικόν | Τερηδών (= R ; Τερηδόν, codd. VMpc de la Souda, est imprimé par l'auteur) | « καὶ αὖθις » ; l'auteur écrit « Suidas τ » sans numéro | oui (SOL) |
| 1183 | Hésychius | τ 1758 | glose | τὼ πόδε · τοὺς πόδας δυϊκῶς |  |  | oui (Hansen–Cunningham IV, OCR de la page) |
| 1187 | Hésychius | π 4279 | glose | πυγή · τὸ κάθισμα |  | l'éd. renvoie à Thesm. 1187 | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 1197 | Hésychius | σ 2137 | glose | συ[μ]βίνης · καπροβόλον. ἐμβόλιον | συμβίνης (R συμβήνην ; Σ, Souda, Photius συβήνην) |  | oui (Hansen III, OCR de la page) ; ligne contrôlée sur l'image |
| 1197 | Photius | σ 660 | citation | συβήνη · ἡ δερματίνη αὐλοθήκη · ἢ ἡ φαρέτρα. Θεσμοφοριαζούσαις Ἀριστοφάνης · „ἀλλὰ οὐκ ἔχω οὐδέν · ἀλλὰ συβήνην λαβέ“ | ἀλλὰ οὐκ ἔχω οὐδέν (R ἀλλ' οὐκ ἔκ' ὠδέν) ; om. τό ; συβήνην (R συμβήνην) | pièce nommée ; cf. Souda σ 1273 | oui (Theodoridis III, PDF p. 436) |
| 1197 | Souda | Souda σ 1273 | citation | ἀλλ' οὐκ ἔχω οὐδέν · ἀλλὰ συβήνην λάβε | ἔχω οὐδέν (R ἔκ' ὠδέν) ; om. τό ; συβήνην (R συμβήνην ; = Σ) |  | oui (SOL) |
| 1214 | Eustathe | Eustathius 1406.19 | — |  |  | référence de l'auteur, non contrôlée | non |
| 1214 | Souda | Souda δ 892 | citation | διέβαλέ μ' ἡ γραῦς | διέβαλε (R διέβαλλε) ; ἡ γραῦς (R ὁ γραῦς) |  | oui (SOL) |
| 1217 | Souda | Souda π 1502 | citation | τὴν γραῦν ἐρωτᾷς, ἣ 'φέρεν τὰς πηκτίδας; | γραῦν (R γραῦ) |  | oui (SOL) |
| 1231 | Souscription PSI | Subscriptio PSI-1194 fr. 6 ΑΡΙΣΤΟΦΑΝ]ΟΥΣ ΘΕΣΜΟΦΟΡΙ]ΑΖΥΣΑΙ ]ΧΗΗΙ (= 1201, versuum numerus) | — |  |  | référence de l'auteur, non contrôlée | non |

## 4. Notices examinées et écartées

- Souda αι 253 — Αἰόλος : glose générique
- Souda γ 193 — Γεραίρειν : glose générique (cf. v. 961 γέραιρε)
- Souda γ 83 — Γαιήοχος : référence erronée de l'auteur (lire γ 63)
- Souda δ 1320 — Δοθιῆνι … ἠμφιεσμένῳ : sans rapport
- Souda δ 1508 — ὦ Ζεῦ, τί δρασείεις ποθῶν τὸν λεών : vers non identifié, distinct du v. 71 (ὦ Ζεῦ, τί δρᾶσαι διανοεῖ με τήμερον)
- Souda δ 448 — Démocrite : sans rapport
- Souda δ 499 — διαβάλλεταί σ' ὁ θεῖος : citation d'une autre pièce
- Souda δ 500 — Διαβάλλειν : glose générique
- Souda ε 2727 — Ἐπιτριβείη : glose générique (v. 557 ἐπιτριβείης)
- Souda ε 2729 — Ἐπίτριπτος : glose générique
- Souda ε 3237 — Ἐστυκώς : la citation est un fragment comique adespoton (fr. 520 K.-A.), non le v. 158
- Souda ε 3367 — Εὐάθλους δέκα : Holcades
- Souda ε 3695 — Euripide (biographie : mère λαχανόπωλις, cf. v. 387) : témoignage biographique, non citation
- Souda ε 3791 — Ἐφείλιξαν : référence erronée de l'auteur (lire ε 3792)
- Souda ε 93 — Ἐγκέχοδα : Grenouilles
- Souda ει 153 — Εἰνάλιος : glose générique (v. 325 εἰναλίου ; aussi Soph. OC 888)
- Souda θ 379 — Θίασος : glose générique
- Souda θ 610 — Θυρίς : glose générique
- Souda ι 24 — Ἰάμβη : sans rapport
- Souda κ 1756 — Κλεισθένην ὁρῶ : lemme tiré des Acharniens 117-122 (Σ Ach. 118, selon la SOL), que l'auteur range au v. 235
- Souda κ 1757 — Κλεισθένης : citation de Sophocle (?)
- Souda κ 2730 — Κύων Μολοττικός : Aristophane fr. 958 K.-A. (non vv. 416-417, SOL)
- Souda κ 2786 — Κύτταρος : glose générique
- Souda κ 396 — Carcinos (cf. vv. 169, 441) : notice biographique
- Souda κ 623 — Κατάληψις : référence erronée de l'auteur (lire κ 263)
- Souda λ 54 — Λακιδέας : référence erronée de l'auteur (lire λ 64)
- Souda λ 816 — Λύκος ἔχανεν : Thesmophories II (« Θεσμοφοριαζούσαις β' »)
- Souda π 1634 — Πιππίζουσι : glose générique
- Souda π 2113 — Πόσθη : glose générique
- Souda π 2867 — Προτέλειον : glose générique
- Souda π 356 — Παρακεκινδυνευμένον : Grenouilles 96-102 et le vers d'Euripide parodié au v. 272 (ὄμνυμι δ' ἱερὸν αἰθέρ' οἴκησιν Διός)
- Souda σ 441 — Simonide : sans rapport
- Souda σ 823 — Σοφοὶ τύραννοι τῇ τῶν σοφῶν συνουσίᾳ : le vers tragique parodié au v. 21, non une citation de la pièce
- Souda σ 951 — Σπλήν : glose générique
- Souda τ 1235 — Τυχηρότερος : glose générique
- Souda τ 812 — Τοὔγκυκλον : Cavaliers
- Souda φ 379 — Philoclès (cf. v. 168) : notice biographique
- Souda φ 393 — Philoxène : sans rapport
- Souda φ 700 — Φρενήρης : référence erronée de l'auteur (lire φ 770)
- Zonaras (Tittmann I), note de l'éditeur sur θριγκοῖς (v. 58) — relevé par le scan du corpus : il s'agit d'une note de Tittmann (citation de H. Estienne), non du lexique

## 5. Testimonia de l'auteur : concordance et corrections *(à compléter)*

## 6. Vérifications à faire *(à compléter)*
