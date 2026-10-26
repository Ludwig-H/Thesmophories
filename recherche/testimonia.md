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

165 témoignages retenus (165 notices de la Souda, 0 autres sources) ; 165 vérifiés dans un texte, 0 non vérifiés.

## 3. Tableau vers par vers

| Vers | Source | Référence | Type | Texte cité (extrait) | Leçon (divergences) | Remarques | Vérifié |
|---|---|---|---|---|---|---|---|
| 2 | Souda | Souda α 1330 | citation | ἀπολεῖ μ' ἀλοῶν ἄνθρωπος ἐξ ἑωθινοῦ | ἄνθρωπος (= R ; ἅνθρωπος Boissonade) |  | oui (SOL) |
| 36 | Souda | Souda π 3024 | citation | ἀλλ' ἐκποδὼν πτήξωμεν | — |  | oui (SOL) |
| 39-41 | Souda | Souda ε 3792 | citation | εὔφημος πᾶς ἔστω λεὼς … θίασος Μουσῶν ἔνδον μελάθρων | λεώς (= R ; λαός Σ) ; συγκλείσας (texte συγκλῄσας) ; ἐνδημεῖ (texte ἐπιδημεῖ) | l'auteur cite « ε 3791 » dans ses testimonia (= Ἐφείλιξαν) mais « ε 3792 » dans son apparat | oui (SOL) |
| 40-42 | Souda | Souda θ 378 | citation | ἐπιδημεῖ γὰρ θίασος Μουσῶν … τῶν δεσποσύνων μελοποιῶν | — |  | oui (SOL) |
| 43-45 | Souda | Souda ε 3997 | citation | ἐχέτω δὲ πνοὰς νήνεμος αἰθήρ · κῦμα δὲ πόντου μὴ κελαδείτω γλαυκόν | — | l'auteur cite « ε 3792 » : lire ε 3997 (SOL) | oui (SOL) |
| 44 | Souda | Souda κ 1278 | lemme | Κελαδείτω | — | lemme seul | oui (SOL) |
| 45, 48, 223, 231, 945 | Souda | Souda ε 2807 | glose | βομβάξ … βομβαλομβάξ … ἀττατατατατταῖ … μῦ μῦ … ἰαππαπαιάξ | βομβαλομβάξ (texte βομβαλοβομβάξ, v. 48) ; ἀττατατατατταῖ (texte ἀτταταῖ ἰατταταῖ, v. 223) ; μῦ μῦ (texte μυμῦ, v. 231) | notice Ἐποποῖ (interjections d'Aristophane) | oui (SOL) |
| 52-57 | Souda | Souda δ 1547 | citation | Ἀγάθων ἄρχεται δρυόχους τιθέναι … καὶ χιανεύει καὶ λαικάζει | ἁψῖδας (R ἀσπίδας) ; τορεύει (texte τορνεύει) ; γογγυλίζει (= R ; γογγύλλει Porson) ; χιανεύει (texte χοανεύει) | cf. χ 297, λ 181 | oui (SOL) |
| 52-57 | Souda | Souda χ 297 | citation | Ἀγάθων ἄρχεται δρυόχους τιθέναι … καὶ χιανεύει καὶ λαικάζει | comme δ 1547 |  | oui (SOL) |
| 53-57 | Souda | Souda λ 181 | citation | κάμπτει δὲ νέας ἀψῖδας ἐπῶν, τὸ δὲ τορείη καὶ γογγυλίζει καὶ λαικάζει | citation abrégée ; τὸ δὲ τορείη (texte τὰ δὲ τορνεύει) |  | oui (SOL) |
| 55 | Souda | Souda α 2754 | glose | Ἀντονομάζει | — | glose (scholie au v. 55, SOL) | oui (SOL) |
| 56 | Souda | Souda γ 361 | glose | Γογγυλίζει, ἀντὶ τοῦ μεταστρέφει | γογγυλίζει (= R ; γογγύλλει Porson) | la citation qui suit (ὥσπερ γυναικὶ γογγύλην μεμαγμένην) est d'une autre pièce (Paix 28 selon la SOL) | oui (SOL) |
| 74 | Souda | Souda κ 1487 | citation | οὐ χρῆν σε κρύπτειν ὄντα κηδεστὴν ἐμόν | — |  | oui (SOL) |
| 93 | Souda | Souda κ 2025 | citation | τὸ πρᾶγμα κομψὸν καὶ σφόδρ' ἐκ τοῦ σοῦ τρόπου | — | « καὶ αὖθις » | oui (SOL) |
| 93-94 | Souda | Souda τ 439 | citation | τὸ πρᾶγμα κομψὸν καὶ σφόδρ' ἐκ τοῦ σοῦ τρόπου · τοῦ γὰρ τεχνάζειν ἡμέτερος ὁ πυραμοῦς | — |  | oui (SOL) |
| 94 | Souda | Souda π 3192 | citation | ἡμέτερος ὁ πυραμοῦς | — | cf. τ 439 | oui (SOL) |
| 100 | Souda | Souda μ 1445 | citation | μυρμήκων ἀτραποὺς ἤ τί διαμινυρίζεται | μυρμήκων (R μύρμηκος) ; διαμινυρίζεται (texte διαμινύρεται) |  | oui (SOL) |
| 105 | Souda | Souda σ 175 | glose | Σεβίσαι, ἀντὶ τοῦ εὐλογῆσαι | — | tiré de la scholie au v. 105 (SOL) | oui (SOL) |
| 105-106 | Souda | Souda σ 178 | citation | εὐπίστως τοὐμὸν δαίμονας ἔχει σεβίσαι | εὐπίστως (= R) ; om. δέ ; ἔχει (R ἔχεις) |  | oui (SOL) |
| 105-106 | Souda | Souda σ 183 | citation | εὐπίστως δὲ τοὐμὸν δαίμονας ἔχει σεβίσαι | εὐπίστως (= R ; εὐπείστως Reiske) ; ἔχει (R ἔχεις) |  | oui (SOL) |
| 120 | Souda | Souda α 4147 | lemme | Ἀσιάδος κρούματα, τῆς κιθάρας · οὕτως Ἀριστοφάνης | ordre Ἀσιάδος κρούματα (texte κρούματά τ' Ἀσιάδος) | cf. EM 153, 21 ; Photius α 2957 ; Συναγωγή α 2226 (renvois de l'auteur, voir ces sources) | oui (SOL) |
| 125 | Souda | Souda α 4016 | lemme | Ἄρσενι βοᾷ δοκίμῳ | δοκίμῳ (= R) |  | oui (SOL) |
| 127 | Souda | Souda δ 891 | lemme | Δι' αἰφνιδίου ὀπός | — | cf. ο 471 | oui (SOL) |
| 127 | Souda | Souda ο 471 | lemme | δι' αἰφνιδίου ὀπός | — | cf. δ 891 | oui (SOL) |
| 129-130 | Souda | Souda ο 194 | glose | Ὀλολύζει ὁ γέρων … | — | tiré de la scholie au v. 129 ; selon la SOL, R porte dans le texte une indication semblable (ὀλολύζεις γέρων), à contrôler sur l'image | oui (SOL) |
| 130-132 | Souda | Souda γ 141 | citation | ἡδὺ τὸ μέλος, ὦ πότνιαι Γενετυλλίδες … καὶ μανδαλωτόν | — |  | oui (SOL) |
| 131 | Souda | Souda κ 912 | citation | θηλυδριῶδες καὶ κατεγλωττισμένον | — |  | oui (SOL) |
| 131-132 | Souda | Souda μ 134 | citation | θηλυδριῶδες καὶ κατεγλωττισμένον καὶ μανδαλωτόν | — |  | oui (SOL) |
| 132-133 | Souda | Souda γ 63 | citation | ὥστ' ἐμοῦ γ' ἀκροωμένου τοῦ μέλους … ὑπῆλθε γάργαλος | add. τοῦ μέλους | l'auteur cite « γ 83 » (= Γαιήοχος) : lire γ 63 | oui (SOL) |
| 136 | Souda | Souda γ 504 | citation | ποδαπὸς ὁ γύννις; τίς πάτρα; | — |  | oui (SOL) |
| 136-140 | Souda | Souda β 110 | citation | τίς ἡ στολή; … τίς δὲ κατόπτρου καὶ ξίφους κοινωνία; | ἀξύμφορον (R οὐ ξύμφορον ; Adler suit ici M selon l'apparat de l'auteur) ; δὲ (texte δαί) | l'apparat de l'auteur cite par erreur « Suid. β 190 » au v. 139 | oui (SOL) |
| 141-142 | Souda | Souda π 987 | citation | πότερον, ὡς ἀνὴρ τρέφῃ; ποῦ δὲ τὸ πέος; | τρέφῃ (texte τρέφει) ; ποῦ δὲ τὸ πέος (texte καὶ ποῦ πέος) | « καὶ αὖθις » | oui (SOL) |
| 142 | Souda | Souda λ 63 | citation | ποῦ τὸ πέος; ποῦ χλαῖνα; ποῦ Λακωνικαί; | τὸ πέος (texte καὶ ποῦ πέος) |  | oui (SOL) |
| 146-147 | Souda | Souda α 1097 | citation | ὦ πρέσβυ, πρέσβυ, τοῦ φθόνου τὸν ψόγον … οὐ παρεσχόμην | om. μέν ; τὴν δὲ (texte τὴν δ') |  | oui (SOL) |
| 159-160 | Souda | Souda α 350 | citation | ἄλλως τ' ἄμουσόν ἐστι … ἀγρεῖον ὄντα καὶ δασύν | — | « καὶ αὖθις » ; reprise de α 1633 | oui (SOL) |
| 159-161 | Souda | Souda α 1633 | citation | ἄλλως τ' ἄμουσόν ἐστι … κ' Ἀνακρέων ὁ Τήϊος | κ' Ἀνακρέων (texte κἀνακρέων) | suivi de « καὶ τὰ ἑξῆς » | oui (SOL) |
| 161-162 | Souda | Souda ε 4049 | citation | Ἀνακρέων, Ἀλκαῖος, οἵπερ ἁρμονίαν ἐχύμισαν | ἐχύμισαν (R ἐχύμησαν) ; Ἀνακρέων, Ἀλκαῖος (texte κἀνακρέων … κἀλκαῖος) |  | oui (SOL) |
| 162-163 | Souda | Souda ε 989 | citation | κ' Ἀλκαῖος, οἵπερ ἁρμονίαν ἐχύμισαν … διεκίνουν Ἰωνικῶς | ἐχύμισαν (R ἐχύμησαν) ; διεκίνουν (R διεκίνων) |  | oui (SOL) |
| 163 | Souda | Souda ι 495 | citation | ἐμιτροφόρουν τε καὶ διεκίνουν Ἰωνικῶς | διεκίνουν (R διεκίνων) |  | oui (SOL) |
| 165 | Souda | Souda η 362 | glose | Ἠμπέσχετο | — | glose (texte ἠμπέσχετο ; source incertaine selon la SOL) | oui (SOL) |
| 173 | Souda | Souda β 192 | citation | βαΰζων · καὶ γὰρ ἐγὼ τοιοῦτος ἦν | ἦν (= R) |  | oui (SOL) |
| 175 | Souda | Souda ζ 63 | citation | οὐ ζηλῶ σε τῆς παιδεύσεως | — |  | oui (SOL) |
| 177-178 | Souda | Souda οι 154 | citation | σοφοῦ πρὸς ἀνδρός, ὅστις ἐν βραχεῖ … οἷός τε συντέμνειν λόγους | — | « καὶ αὖθις » | oui (SOL) |
| 177-180 | Souda | Souda σ 792 | citation | σοφοῦ πρὸς ἀνδρός … ἱκέτης ἀφῖγμαι πρὸς σέ | συντεμεῖν (texte συντέμνειν) ; κοινῇ (= R ; καινῇ Biset) |  | oui (SOL) |
| 179 | Souda | Souda κ 2556 | citation | ἐγὼ δὲ κοινῇ ξυμφορᾷ πεπληγμένος | κοινῇ (= R ; καινῇ Biset) |  | oui (SOL) |
| 191 | Souda | Souda ε 1871 | glose | Ἐξυρημένος | — | glose (source possible : v. 191, SOL) | oui (SOL) |
| 195-197 | Souda | Souda υ 709 | citation | μὴ νῦν ἐλπίσῃς τὸ σὸν κακὸν … οἰκείως φέρε | add. ἄν (καὶ γὰρ ἂν μαινοίμεθ' ἄν ; R καὶ γὰρ μαινοίμεθ' ἄν) ; om. ἀλλ' |  | oui (SOL) |
| 198-201 | Souda | Souda τ 440 | citation | τὰς συμφορὰς γὰρ οὐχὶ τοῖς τεχνάσμασι … ἀλλὰ τοῖς παθήμασιν | — |  | oui (SOL) |
| 215-216 | Souda | Souda α 4565 | citation | ἀποξυρεῖν ταδί, τὰ κάτω δ' ἀφαύειν | ἀφαύειν (R ἀφεύειν) | sous Ἀφαυανθήσομαι (… καὶ Ἀφαύειν, καίειν) | oui (SOL) |
| 227 | Souda | Souda η 334 | citation | τὴν ἡμίκραιραν τὴν ἑτέραν ψιλὴν ἔχων | — |  | oui (SOL) |
| 231 | Souda | Souda μ 1383 | citation | τί μύζεις; πάντα πεποίηται καλῶς | lemme Μῦ, μῦ (texte μυμῦ) |  | oui (SOL) |
| 232 | Souda | Souda ψ 105 | citation | οἴμοι κακοδαίμων · ψιλὸς αὖ στρατεύσομαι | αὖ (= R) |  | oui (SOL) |
| 236-237 | Souda | Souda α 4594 | glose | Ἀφευθεὶς τὸν πρωκτόν · Ἀριστοφάνης ἀντὶ τοῦ φλογισθείς | — | tiré de la scholie (cf. δ 205) | oui (SOL) |
| 237 | Souda | Souda δ 205 | citation | οἴμοι κακοδαίμων, δελφάκιον γέγονα | γέγονα (texte γενήσομαι) | suivi d'une scholie (ἀφευθεὶς τὸν πρωκτόν) | oui (SOL) |
| 245 | Souda | Souda α 3473 | glose | Ἀποπεπόνηκας | — | glose (scholie au v. 245 selon Adler) | oui (SOL) |
| 245 | Souda | Souda α 4132 | citation | φεῦ, ἰοὺ τῆς ἀσβόλου | — |  | oui (SOL) |
| 246 | Souda | Souda αι 135 | glose | Αἰθός | — | glose | oui (SOL) |
| 246 | Souda | Souda τ 903 | citation | αἰθὸς γεγένημαι πάντα τὰ περὶ τὸν τράμιν | γεγένημαι (R γεγέννημαι) ; τόν (texte τήν) |  | oui (SOL) |
| 257-258 | Souda | Souda π 1165 | citation | ἥδιον μὲν οὖν κεφαλὴ περίθετος, ἣν ἐγὼ νύκτωρ φορῶ | ἥδιον (texte ἡδί) |  | oui (SOL) |
| 261 | Souda | Souda ε 135 | citation | φέρ' ἔγκυκλον · τουτὶ λάμβαν' ἀπὸ τῆς κλινίδος | τουτί (R τοῦτι) ; λάμβαν' (= R ; λάβ' Daubuz) | « καὶ ἀλλαχοῦ » ; cf. κ 1809 | oui (SOL) |
| 261 | Souda | Souda κ 1809 | citation | ἔγκυκλον · τουτὶ λάμβαν' ἀπὸ τῆς κλινίδος | τουτί (R τοῦτι) ; λάμβαν' (= R) |  | oui (SOL) |
| 263 | Souda | Souda χ 7 | citation | χαλαρὰ γοῦν χαίρεις φορῶν ὑποδήματα | χαίρεις (= R ; χαίροις codd. FV de la Souda, imprimé par l'auteur) ; add. ὑποδήματα |  | oui (SOL) |
| 274 | Souda | Souda α 3806 | glose | Ἄρδην | — | glose (scholie au v. 274, SOL) | oui (SOL) |
| 277-278 | Souda | Souda σ 325 | citation | ὡς τὸ τῆς ἐκκλησίας σημεῖον ἐν τῷ Θεσμοφόρῳ φαίνεται | Θεσμοφόρῳ (R Θεσμοφορίῳ) |  | oui (SOL) |
| 295 | Souda | Souda ε 3797 | lemme | Εὐφημία ἔστω | — | formule (scholie au v. 295 selon la SOL) | oui (SOL) |
| 322-324 | Souda | Souda οι 181 | citation | σύ τε Πόντιε Πόσειδον, προλιπὼν μυχὸν ἰχθυόεντ' οἰστροδόνητον | om. σεμνέ et ἁλιμέδον ; ἰχθυόεντ' (= R) |  | oui (SOL) |
| 336 | Souda | Souda ε 2375 | glose | Ἐπικηρυκεύεται | — | glose générique (Thucydide selon la SOL) ; l'auteur la range au v. 336 | oui (SOL) |
| 341 | Souda | Souda ε 1271 | citation | προαγωγὸς οὖσ' ἐνετρύλλισε τῷ δεσπότῃ | — |  | oui (SOL) |
| 341 | Souda | Souda π 2307 | glose | Προαγωγός | — | glose | oui (SOL) |
| 347-348 | Souda | Souda χ 394 | citation | εἴ τις κάπηλος ἢ καπηλὶς τοῦ χοὸς … διαλυμαίνεται | εἴ (texte κεἴ) ; χοός (= R) | l'apparat de l'auteur cite par erreur « Suid. λ 394 » | oui (SOL) |
| 363-364 | Souda | Souda α 3501 | citation | ἀπόρρητά τε τοῖσιν ἐχθροῖσι τοῖς ἡμετέροις λέγουσιν | ἀπόρρητά (texte τἀπόρρητα) ; ἐχθροῖσι (texte ἐχθροῖς) ; λέγουσιν (= R ; λέγουσ' Bentley) |  | oui (SOL) |
| 369-371 | Souda | Souda π 444 | citation | ὥσθ' ἡμῖν θεοὺς παραστατεῖν καίπερ γυναιξὶν οὔσαις | — | attribué par erreur au Ploutos (« Ἀριστοφάνης Πλούτῳ ») | oui (SOL) |
| 373-374 | Souda | Souda ε 2616 | citation | Τιμόκλει' ἐπιστάτει · Λύσιλλ' ἐγραμμάτευε | Τιμόκλει' (= R ; Ἀρ[χίκλ]ει' P.Oxy. 1176) ; ἐπιστάτει (texte ἐπεστάτει) |  | oui (SOL) |
| 377-378 | Souda | Souda χ 481 | citation | καὶ χρηματίζειν πρῶτα περὶ Εὐριπίδου, ὅ τι χρὴ παθεῖν | — |  | oui (SOL) |
| 380 | Souda | Souda π 1166 | citation | περίθου νῦν τόνδε πρότερον, πρὶν λέγειν | πρότερον (R πρῶτον) |  | oui (SOL) |
| 383-384 | Souda | Souda φ 431 | citation | φιλοτιμίᾳ μὲν οὐδεμιᾷ, μὰ τὼ θεώ, λέξουσ' ἀνέστην, ὦ γυναῖκες | — |  | oui (SOL) |
| 389 | Souda | Souda ε 2592 | citation | τί γὰρ οὗτος ἡμᾶς οὐκ ἐπισμῇ τῶν κακῶν | — | avec la scholie (Diodore) | oui (SOL) |
| 389 | Souda | Souda σ 747 | glose | Σμώχειν · τὸ λοιδορεῖν | — | reste de la scholie au v. 389 (SOL ; cf. ε 2592) | oui (SOL) |
| 390-391 | Souda | Souda ε 955 | citation | ποῦ δ' οὐχὶ διαβέβληχ' ὅπου περ ἔμβραχυ εἰσὶ θεαταί; | ἔμβραχυ (R ἐν βραχύ) | cf. οι 128 | oui (SOL) |
| 390-394 | Souda | Souda οι 128 | citation | ποῦ δ' οὐχὶ διαβέβληχ' … τὰς μέγ' ἀνδράσι κακόν | ἔμβραχυ (R ἐν βραχύ) ; οἷς θέα καὶ τραγῳδία (texte εἰσὶν θεαταὶ καὶ τραγῳδοί) | suivi d'une note de Symmaque (παρὰ τὸ πιπίζειν) | oui (SOL) |
| 395-396 | Souda | Souda ι 275 | citation | ὥστ' εὐθὺς εἰσιόντες ἀπὸ τῶν ἰκρίων ὑποβλέπουσ' ἡμᾶς | — |  | oui (SOL) |
| 421-427 | Souda | Souda κ 159 | citation | οἱ γὰρ ἄνδρες ἤδη κλειδία φοροῦσι … ἐδίδαξε θριπηδέστατα | κλειδία (texte κλῄδια) ; om. αὐτοί ; Λακωνικά (texte Λακωνίκ') ; om. ᾡκότριψ Εὐριπίδης ; θριπηδέστατα (texte θριπήδεστ') | sous Κακοηθέστατα ; cf. λ 64 | oui (SOL) |
| 421-428 | Souda | Souda λ 64 | citation | οἱ γὰρ ἄνδρες ἤδη κλειδία φοροῦσι … σφραγῖδα ἐξαψαμένους | κλειδία ; om. αὐτοί, τρεῖς, ᾡκότριψ Εὐριπίδης ; Λακωνίκα ; ἐδίδαξε (R -ξεν) ; θριπηδέστατ' (texte θριπήδεστ') ; σφραγῖδα (texte σφραγίδια) | l'auteur cite « λ 54 » (= Λακιδέας) : lire λ 64 | oui (SOL) |
| 427 | Souda | Souda θ 503 | glose | Θριπηδέστατον | — | tiré de la scholie au v. 427 (SOL) ; texte θριπήδεστ' | oui (SOL) |
| 428-429 | Souda | Souda κ 2771 | citation | ἐμοὶ τούτῳ δοκεῖ, ὄλεθρόν τινα κυρκανᾶν ἀμωσγέπως | τινα, om. ἡμᾶς ; ἀμωσγέπως (= R) |  | oui (SOL) |
| 429 | Souda | Souda α 1645 | glose | Ἀμωσγέπως : ὁπωσδήποτε … | — | glose (même notice dans Σ Plat. Phaedr. 228c selon la SOL) | oui (SOL) |
| 437-439 | Souda | Souda ε 22 | citation | πάσας δ' ἰδέας ἐξήτασε … πυκνῶς τε ποικίλως λόγους ἀνεῦρεν | ἰδέας (R εἰδέας) ; ἐξήτασε, ἐβάστασε (R -σεν) ; ποικίλως (texte ποικίλους) ; ἀνεῦρεν (= R ; ἀνηῦρεν Meineke) |  | oui (SOL) |
| 449 | Souda | Souda τ 321 | citation | τέως μὲν οὖν, ἀλλ' ἡμικάκως ἐβοσκόμην | — |  | oui (SOL) |
| 457-458 | Souda | Souda σ 1591 | citation | δεῖ γὰρ ἀνδράσι πλέξαι στεφάνους συνθηματιαίους εἴκοσι | — |  | oui (SOL) |
| 459-460 | Souda | Souda λ 441 | citation | ἕτερον αὖ τι λῆμα τοῦτο κομψότερον ἔτ' ἢ τὸ πρότερον ἀναπέφηνε | — | « καὶ αὖθις » | oui (SOL) |
| 469 | Souda | Souda ο 330 | citation | καὐτὴ γὰρ ἐγώ, οὕτως ὀναίμην τῶν τέκνων | ἐγώ (texte ἔγωγ') ; ὀναίμην (R ὀνοίμην) |  | oui (SOL) |
| 470 | Souda | Souda μ 328 | citation | μισῶ τἄνδρ' ἐκεῖνον, εἰ μὴ μαίνομαι | τἄνδρ' (texte τὸν ἄνδρ') |  | oui (SOL) |
| 473-474 | Souda | Souda τ 683 | citation | τί ταῦτ' ἔχουσαι κεῖνον αἰτιώμεθα βαρέως τε φέρομεν; | κεῖνον (= R ; 'κεῖνον Meineke) |  | oui (SOL) |
| 480 | Souda | Souda δ 591 | glose | Διακορεῦσαι | — | glose (texte διεκόρησεν ; διεκόρευσεν Pollux III 42) | oui (SOL) |
| 481 | Souda | Souda ε 520 | citation | οὗτος πόθῳ μου 'κνυεν ἐλθὼν τὴν θύραν | — |  | oui (SOL) |
| 486 | Souda | Souda σ 1712 | citation | κᾆθ' ὁ μὲν ἔτριβε κεδρίδας, ἄνηθον, σφάκον | ἄνηθον (= R ; ἄννηθον Dindorf) |  | oui (SOL) |
| 493-494 | Souda | Souda λ 434 | citation | μάλισθ' ὅταν ὑπό του ληκώμεθα τὴν νύχθ' ὅλην | ὅταν après μάλισθ' (texte ὅταν μάλισθ') ; ληκώμεθα (= Rac ; κινώμεθα Rpc) ; add. ὅλην |  | oui (SOL) |
| 509 | Souda | Souda η 637 | citation | τὸ γὰρ ἦτρον τῆς χύτρας ἐλάκτισεν | — |  | oui (SOL) |
| 514-516 | Souda | Souda λ 271 | citation | λέων, λέων σοι γέγονεν ἔκμαγμα σόν … στρεβλὸν ὥσπερ κύτταρον | ἔκμαγμα (R αὖτ' ἔκμαγμα ; αὐτέκμαγμα Reiske) | lemme (v. 514) et citation (515-516) ; cf. π 2114 | oui (SOL) |
| 514-516 ; 254 | Souda | Souda π 2114 | citation | λέων, λέων σοι γέγονεν ἔκμαγμα σόν … ὥσπερ κύτταρον στρεβλόν ; νὴ τὴν Ἀφροδίτην, ἡδύ γ' ὄζει ποσθίου | ἔκμαγμα (R αὖτ' ἔκμαγμα) ; ὥσπερ κύτταρον στρεβλόν (texte στρεβλὸν ὥσπερ κύτταρον) |  | oui (SOL) |
| 515-516 | Souda | Souda κ 2787 | citation | πόσθιον τῷ σῷ προσόμοιον, στρεβλὸν ὥσπερ κύτταρον | — |  | oui (SOL) |
| 527-530 | Souda | Souda α 1073 | citation | ἀλλ' ἅπαν γένοιτ' ἂν ἤδη … μὴ δάκῃ ῥήτωρ ἀθρεῖν | ἀλλ' ἅπαν (= R ; ἀλλὰ πᾶν Cobet) | lemme et citation ; suit le proverbe ὑπὸ παντὶ λίθῳ σκορπίος εὕδει | oui (SOL) |
| 531-532 | Souda | Souda α 1349 | citation | ἀλλ' οὐ γάρ ἐστι τῶν ἀναισχύντων … πλὴν ἄλλαι γυναῖκες | ἄλλαι (R ἄρ' εἰ) | le texte de l'auteur porte ἀναισχύτων (coquille ?) | oui (SOL) |
| 557 | Souda | Souda σ 512 | citation | σιφωνίζομεν τὸν σῖτον | τὸν σῖτον (= R ; τὸν κύσθον conj. de l'auteur) |  | oui (SOL) |
| 560 | Souda | Souda κ 996 | citation | ἑτέρα τὸν ἄνδρα τῷ πελέκει κατεσπόδησε | ἑτέρα en tête, om. γυνή (R τὸν ἄνδρα τῷ πελέκει γυνή) |  | oui (SOL) |
| 566 | Souda | Souda κ 730 | citation | οὔτοι, μὰ τὼ θεώ, σὺ καταπροίξῃ λέγουσα ταυτί | καταπροίξῃ (texte καταπροίξει) |  | oui (SOL) |
| 567 | Souda | Souda ε 588 | citation | ἐκποκιῶ σου τὰς ποκάδας | ποκάδας (= R) |  | oui (SOL) |
| 572-573 | Souda | Souda ο 292 | citation | πρὶν οὖν ὁμοῦ γενέσθαι, σιγᾶθ', ἵν' αὐτῆς πυθώμεθα | om. κοσμίως |  | oui (SOL) |
| 574 | Souda | Souda ξ 83 | lemme | Ξυγγενεῖς τοὐμοῦ τρόπου | — |  | oui (SOL) |
| 576 | Souda | Souda π 2541 | lemme | Προξενῶ θ' ὑμᾶς ἀεί | ὑμᾶς (R ὑμῶν) |  | oui (SOL) |
| 601-602 | Souda | Souda π 2540 | citation | καὶ σὺ ξυνέξευρ' αὐτόν … αὐτήν τε κἀκείνην ἔχῃς, ὦ πρόξενε | ξυνέξευρ' (R συνέξευρ') ; αὐτήν (R ταύτην) |  | oui (SOL) |
| 616 | Souda | Souda σ 1163 | citation | στραγγουριῶ · χθὲς γὰρ ἔφαγον κάρδαμα | χθὲς γάρ (texte γάρ · ἐχθές) |  | oui (SOL) |
| 630-631 | Souda | Souda π 2563 | citation | φέρ' ἴδω, τί μέντοι πρῶτον ἦν; … προὐπίνομεν | μέντοι (= Rpc in mg.) ; μετά (R με) |  | oui (SOL) |
| 641 | Souda | Souda σ 1049 | glose | Στερίφη · στεῖρα, μὴ τεκοῦσα | — | glose ; cf. Hésychius σ 1769, Συναγωγή σ 214, Photius σ 532 (SOL) | oui (SOL) |
| 647-648 | Souda | Souda ι 640 | citation | ἰσθμόν τιν' ἔχεις, ἄνθρωπ', … πυκνότερον Κορινθίων | ἄνθρωπ' (R ὦνθρωπε) | suivi de la scholie (διϊσθμονίσαι) | oui (SOL) |
| 648 | Souda | Souda δ 1048 | glose | Διισθμονίσαι | — | tiré de la scholie au v. 648 (cf. ι 640) | oui (SOL) |
| 659 | Souda | Souda ε 3 | glose | Ἔα δή · ἄγε δή | ἔα δή (texte εἶα δή) | glose ; cf. Hésychius ε 8, Photius ε 1, Συναγωγή ε 1 (renvois de l'auteur) | oui (SOL) |
| 692 | Souda | Souda κ 1260 | glose | Κέκραθι · κράξον | — | glose (texte κέκραχθι) | oui (SOL) |
| 701 | Souda | Souda ν 222 | glose | τέρας νεοχμόν · Ἀριστοφάνης | ordre τέρας νεοχμόν (texte νεοχμὸν αὖ τέρας) | rapprochement incertain (la SOL renvoie à Photius ν 154) | oui (SOL) |
| 702 | Souda | Souda α 2902 | lemme | Ἅπαντα τόλμης πλέα κἀναισχυντίας | ἅπαντα (R ἅπαν γὰρ ἐστὶν) ; πλέα (R ἔργα) | emploi proverbial (ἐπὶ τῶν ἰταμῶν) ; cf. CPG, Append. I 35 | oui (SOL) |
| 710-713 | Souda | Souda η 170 | citation | ἀλλ' οὖν ἥκεις γ' ὅθεν ἥκεις … λήψῃ δὲ κακόν | ἥκεις γ' (R ἥκεις τ') ; φαύλως τ' … οὐ λέξεις (= R) ; λήψῃ (texte λήψει) |  | oui (SOL) |
| 729 | Souda | Souda θ 547 | glose | Θυμάλωπες | — | glose (aussi Ach. 321) | oui (SOL) |
| 730-731 | Souda | Souda κ 2408 | citation | σὺ δὲ τὸ Κρητικὸν ἀπόδυθι ταχέως | σὺ δὲ τὸ (R σὺ τόδε τὸ) |  | oui (SOL) |
| 735, 737 | Souda | Souda θ 251 | citation | ὦ θερμόταται γυναῖκες, μέγα καπήλοις καλόν, ἡμῖν δὲ κακόν | om. ὦ ποτίσταται … πιεῖν (735-736) et ὦ (737) ; καλόν (texte ἀγαθόν) ; δέ (texte δ' αὖ) |  | oui (SOL) |
| 747 | Souda | Souda δ 1168 | citation | (ἐξ αὐτοῦ) σχεδὸν τοσοῦτον, ὅσον ἐκ Διονυσίων | ὅσον (R et P.Oxy. 3839 καὶ ὅσον ; χὤσον Bentley) | cité comme proverbe | oui (SOL) |
| 749 | Souda | Souda ε 1018 | glose | Ἐμπίπραται · ἐμπυρίζεται | — | glose générique (texte ἐμπίμπρατε) | oui (SOL) |
| 754 | Souda | Souda σ 1702 | glose | Σφαγεῖον | — | tiré de la scholie au v. 754 (SOL) | oui (SOL) |
| 769-775 | Souda | Souda π 45 | citation | οἶδα δ' ἐγὼ καὶ δὴ πότερον ἐκ τοῦ Παλαμήδους … κἀκεῖν' ἦν ξύλον | οἶδα δ' (texte οἶδ') ; πότερον (texte πόρον) ; om. 771b ; γ' ἔκειντο (R γένοιτ' ἄν) ; om. πόθεν; πόθεν; τί δ' ἂν εἰ ; ταδὶ τἀγάλματα (R εἶτα διὰ τἀγάλματ') ; om. τῶν | citation entrecoupée de la scholie | oui (SOL) |
| 770-771 | Souda | Souda π 1702 | citation | ὥσπερ Παλαμήδης τὰς πλάτας ῥίψω γράφων Ναυπλίῳ | ὥσπερ Παλαμήδης (texte ἐκ τοῦ Παλαμήδους · ὡς ἐκεῖνος) ; add. Ναυπλίῳ | version négligée de la scholie (SOL, cf. π 45) | oui (SOL) |
| 777 | Souda | Souda π 2064 | citation | ἐγχειρεῖν χρὴ ἔργῳ πορίμῳ | χρή (= R ; χρῆν Bentley) |  | oui (SOL) |
| 778-779 | Souda | Souda σ 742 | citation | ἄγε δὴ πινάκων ξεστῶν δέλτοι, δέξασθε σμίλης ὁλκούς | — |  | oui (SOL) |
| 805 | Souda | Souda κ 2692 | glose | Κύννα καὶ Σαλαβακχώ | — | onomastique (la citation est de Cav. 765) | oui (SOL) |
| 808-809 | Souda | Souda β 431 | citation | τίς βουλευτής ἐστι, παραδοὺς ἑτέρῳ τὴν βουλείαν; | om. ἀμείνων |  | oui (SOL) |
| 816 | Souda | Souda γ 72 | glose | Γάστρις | — | glose (texte γάστριδας) ; cf. Photius γ 40 (renvoi de l'auteur) | oui (SOL) |
| 834 | Souda | Souda σ 1089 | glose | Στήνια καὶ Σκίρα · ἑορταὶ γυναικῶν | — | tiré de la scholie au v. 834 (SOL) | oui (SOL) |
| 846 | Souda | Souda ι 323 | citation | ἴλλος γεγένημαι · ὁ δ' οὐδέπω | om. προσδοκῶν |  | oui (SOL) |
| 852 | Souda | Souda κ 2534 | citation | τί αὖ σὺ κυρκανᾷς, ἢ τί κοικύλλεις ἔχων; | ἢ τί (= R ; τί Faber) |  | oui (SOL) |
| 857 | Souda | Souda μ 459 | lemme | Μελανοσυρμαῖον λεών | — |  | oui (SOL) |
| 861 | Souda | Souda φ 770 | glose | Φρυνώνδας | — | onomastique (la citation est de l'Amphiaraos) ; l'auteur cite « φ 700 » (= Φρενήρης) : lire φ 770 | oui (SOL) |
| 863 | Souda | Souda γ 496 | citation | πρὶν τῆς ἑτέρας γυναικίσεως δίκην δοῦναι | δοῦναι après δίκην (R après ἑτέρας) |  | oui (SOL) |
| 868 | Souda | Souda τ 648 | lemme | Τί οὖν ἔτι ζῇ τῶν κοράκων πονηρίᾳ | ζῇ (texte ζῶ) |  | oui (SOL) |
| 869 | Souda | Souda αι 161 | citation | αἰκάλλει τι καρδίαν ἐμήν | — |  | oui (SOL) |
| 870 | Souda | Souda ψ 62 | citation | μὴ ψεῦσον, ὦ Ζεῦ, τῆς ἐπιούσης ἐλπίδος | — | attribué à Sophocle (« καὶ ὁ Σοφοκλῆς ») ; cf. Grégoire de Corinthe et Σ Eur. Hec. 225 (voir ces sources) | oui (SOL) |
| 878 | Souda | Souda οι 1 | citation | ὦ δύστηνος, οἷ πεπλώκαμεν; | — |  | oui (SOL) |
| 902 | Souda | Souda α 2617 | lemme | ἀνταυγεῖς κόρας · στρέψον ἀνταυγεῖς κόρας | — |  | oui (SOL) |
| 910 | Souda | Souda ι 778 | citation | ἐγὼ δὲ Μενέλεων ὅσον ἐκ τῶν ἰφύων | Μενέλεων (R Μενέλαον) ; ὅσον (R ὅσα γ') ; ἰφύων (R ἀφύων ; = Σ) |  | oui (SOL) |
| 922 | Souda | Souda αι 75 | glose | Αἰγυπτιάζειν | — | glose (texte ᾐγυπτιάζετ') ; cf. Photius α 518, Συναγωγή α 494 (renvois de l'auteur) | oui (SOL) |
| 926 | Souda | Souda η 379 | lemme | Ἢν ἐμπνέω · ἕως οὗ ζῶ | ἥν (texte ἤνπερ) |  | oui (SOL) |
| 928 | Souda | Souda α 4475 | citation | αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασε | — | proverbe ; cf. μ 978 | oui (SOL) |
| 928 | Souda | Souda μ 978 | citation | αὕτη μὲν ἡ μήρινθος οὐδὲν ἔσπασεν | — | proverbe | oui (SOL) |
| 935 | Souda | Souda ι 691 | citation | ὀλίγου ταύτην ἱστιορράφος | ταύτην (texte μ' ἀφείλετ' αὐτόν) | citation abrégée ou corrompue | oui (SOL) |
| 942 | Souda | Souda ε 3215 | citation | τοῖς κόραξιν ἑστιῶν | — |  | oui (SOL) |
| 942 | Souda | Souda ε 3227 | glose | Ἑστιῶν · ἀριστοποιῶν | — | glose ; même notice dans Συναγωγή ε 875, Photius ε 2031, Hésychius ε 6411 (SOL) | oui (SOL) |
| 948 | Souda | Souda α 2364 | citation | ὅταν ὄργια σεμνὰ θεαῖν ἱεραῖς ὥραις ἀνέχωμεν | θεαῖν (= R ; θεοῖν Cobet) | l'auteur date le passage du v. 947 ; variantes des manuscrits de la Souda (θεῶν, θεεῖν…) relevées par l'auteur d'après Adler, non contrôlées | oui (SOL) |
| 973 | Souda | Souda τ 271 | glose | Τελεία · Ἥρα Τελεία … | — | tiré de la scholie au v. 973 (SOL) | oui (SOL) |
| 986 | Souda | Souda τ 789 | citation | τόρευε πᾶσαν ᾠδήν | — |  | oui (SOL) |
| 1054 | Souda | Souda αι 245 | glose | Αἰόλαν · σκοτεινήν | — | glose | oui (SOL) |
| 1059 | Souda | Souda η 686 | lemme | Ἠχὼ λόγων ἀντῳδὸς ἐπικοκκάστρια | — | variantes des manuscrits de la Souda (ἐπικαγχάστρια…) relevées par l'auteur d'après Adler, non contrôlées | oui (SOL) |
| 1066-1067 | Souda | Souda ι 531 | citation | ὡς μακρὸν ἵππευμα διώκεις ἀστεροειδέα νῶτα διφρεύουσ' αἰθέρος | — |  | oui (SOL) |
| 1067-1068 | Souda | Souda αι 122 | citation | ἀστεροειδέα νῶτα διφρεύουσ' αἰθέρος ἱερᾶς | — | « καὶ αὖθις » (sous Αἰθήρ) | oui (SOL) |
| 1174 | Souda | Souda κ 263 | glose | Καλπάζειν · τὸ ἁβρῶς βαδίζειν | — | lu dans First1KGreek (Adler) ; l'auteur cite « κ 623 » (= Κατάληψις) : lire κ 263 | oui (First1K) |
| 1175 | Souda | Souda τ 340 | citation | σὺ δ', ὦ Τερηδών, ἐπαναφύσα Περσικόν | Τερηδών (= R ; Τερηδόν, codd. VMpc de la Souda, est imprimé par l'auteur) | « καὶ αὖθις » ; l'auteur écrit « Suidas τ » sans numéro | oui (SOL) |
| 1197 | Souda | Souda σ 1273 | citation | ἀλλ' οὐκ ἔχω οὐδέν · ἀλλὰ συβήνην λάβε | ἔχω οὐδέν (R ἔκ' ὠδέν) ; om. τό ; συβήνην (R συμβήνην ; = Σ) |  | oui (SOL) |
| 1214 | Souda | Souda δ 892 | citation | διέβαλέ μ' ἡ γραῦς | διέβαλε (R διέβαλλε) ; ἡ γραῦς (R ὁ γραῦς) |  | oui (SOL) |
| 1217 | Souda | Souda π 1502 | citation | τὴν γραῦν ἐρωτᾷς, ἣ 'φέρεν τὰς πηκτίδας; | γραῦν (R γραῦ) |  | oui (SOL) |

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

## 5. Testimonia de l'auteur : concordance et corrections *(à compléter)*

## 6. Vérifications à faire *(à compléter)*
