# Le *Codex Ravennas 429 (137, 4, A)* et l'édition critique des *Thesmophories* d'Aristophane

Ce dossier réunit l'intégralité des planches haute définition du ***Codex Ravennas 429* (olim *137, 4, A*)** relatives aux ***Thesmophories* (*Θεσμοφοριάζουσαι*, vv. 1–1231, ff. 162v–177r)**, découpées **planche par planche** et **folio par folio**, ainsi qu'une **étude codicologique, stemmatique et paléographique complète** spécialement conçue pour servir d'instrument de travail à l'édition critique et au commentaire de la pièce.

---

## Sommaire

1. [Structure du dossier et accès rapide aux fichiers](#1-structure-du-dossier-et-accès-rapide-aux-fichiers)
2. [Notice codicologique et stemmatique sur le *Codex Ravennas 429*](#2-notice-codicologique-et-stemmatique-sur-le-codex-ravennas-429)
   - [2.1. Fiche signalétique du manuscrit](#21-fiche-signalétique-du-manuscrit)
   - [2.2. Contenu du manuscrit et place des *Thesmophories*](#22-contenu-du-manuscrit-et-place-des-thesmophories)
   - [2.3. Histoire du codex : de Constantinople à Ravenne via Pise et Florence](#23-histoire-du-codex--de-constantinople-à-ravenne-via-pise-et-florence)
   - [2.4. Statut stemmatique : le *Ravennas* comme *unicodex* des *Thesmophories*](#24-statut-stemmatique--le-ravennas-comme-unicodex-des-thesmophories)
3. [Étude paléographique de l'écriture du *Ravennas* (appliquée à l'édition des *Thesmophories*)](#3-étude-paléographique-de-lécriture-du-ravennas-appliquée-à-lédition-des-thesmophories)
   - [3.1. Distinction des deux mains : $\text{R}^1$ (texte) et $\text{R}^2$ (argument, didascalies, scholies, révisions)](#31-distinction-des-deux-mains--textr1-texte-et-textr2-argument-didascalies-scholies-révisions)
   - [3.2. Attribution des répliques (*notae personarum*) et didascalies scéniques (*parepigraphai*)](#32-attribution-des-répliques-notae-personarum-et-didascalies-scéniques-parepigraphai)
   - [3.3. Morphologie des lettres et confusions paléographiques récurrentes](#33-morphologie-des-lettres-et-confusions-paléographiques-récurrentes)
     - [A. Confusions nées de la minuscule bouletée du Xᵉ siècle](#a-confusions-nées-de-la-minuscule-bouletée-du-xᵉ-siècle)
     - [B. Confusions héritées de l'onciale ancienne (transcription *majuscule $\to$ minuscule*)](#b-confusions-héritées-de-lonciale-ancienne-transcription-majuscule-to-minuscule)
   - [3.4. Abréviations tachygraphiques, ligatures et signes diacritiques](#34-abréviations-tachygraphiques-ligatures-et-signes-diacritiques)
   - [3.5. Orthographe byzantine, iotacismes, élisions et crases dans le *Ravennas*](#35-orthographe-byzantine-iotacismes-élisions-et-crases-dans-le-ravennas)
   - [3.6. Relevé critique des grattages (*in rasura*) et corrections ($\text{R}^1 / \text{R}^2$) dans les *Thesmophories*](#36-relevé-critique-des-grattages-in-rasura-et-corrections-textr1--textr2-dans-les-thesmophories)
4. [Répertoire analytique planche par planche et folio par folio (`ff. 162v–177r`)](#4-répertoire-analytique-planche-par-planche-et-folio-par-folio-ff-162v177r)
   - [4.1. Tableau des 15 planches doubles (bifolios ouverts, vues 166 à 180)](#41-tableau-des-15-planches-doubles-bifolios-ouverts-vues-166-à-180)
   - [4.2. Répertoire détaillé des 30 folios individuels (`f. 162v` à `f. 177r`, vv. 1–1231)](#42-répertoire-détaillé-des-30-folios-individuels-f-162v-à-f-177r-vv-11231)
5. [Bibliographie de référence sur le *Codex Ravennas 429*](#5-bibliographie-de-référence-sur-le-codex-ravennas-429)

---

## 1. Structure du dossier et accès rapide aux fichiers

Ce répertoire (`dossier_ravennas_thesmophories/`) contient :

* **[`folios_individuels_ff162v-177r/`](folios_individuels_ff162v-177r/)** : les **30 folios individuels** (`f. 162v` à `f. 177r`, résolutions de `2011 × 2832 px` par page) découpés un par un et nommés avec leur numéro d'ordre (`01` à `30`), la foliotation de référence de van Leeuwen (1904), la foliotation moderne de la Biblioteca Classense (`164v` à `179r`) et les **numéros exacts des vers contenus sur chaque page** (`vv. 0001–1231`).
* **[`planches_doubles_ff162v-177r/`](planches_doubles_ff162v-177r/)** : les **15 planches doubles originales** en haute définition (`4023 × 2832 px`), présentant chaque bifolio ouvert (*verso* à gauche, *recto* à droite) tel qu'il apparaît à la consultation du codex à Ravenne (vues IIIF `166` à `180`).
* **[`Notice_Ravennas_Codicologie_et_Paleographie.tex`](Notice_Ravennas_Codicologie_et_Paleographie.tex)** : version LaTeX prête à compiler ou à intégrer dans l'introduction de l'édition critique.
* Pour mémoire, les volumes PDF assemblés se trouvent dans [`../ravennas_1904_bnf/`](../ravennas_1904_bnf/) :
  * [`Ravennas_MS429_Thesmophoriazusae_COMPLET_30_folios_individuels_ff162v-177r_HD.pdf`](../ravennas_1904_bnf/Ravennas_MS429_Thesmophoriazusae_COMPLET_30_folios_individuels_ff162v-177r_HD.pdf) (30 pages individuelles avec signets PDF par folio et par vers).
  * [`Ravennas_MS429_Thesmophoriazusae_COMPLET_15_planches_doubles_ff162v-177r_HD.pdf`](../ravennas_1904_bnf/Ravennas_MS429_Thesmophoriazusae_COMPLET_15_planches_doubles_ff162v-177r_HD.pdf) (15 planches doubles HD).

---

## 2. Notice codicologique et stemmatique sur le *Codex Ravennas 429*

### 2.1. Fiche signalétique du manuscrit

| Rubrique | Description |
| :--- | :--- |
| **Lieu de conservation** | Ravenne (Italie), Istituzione Biblioteca Classense |
| **Cote actuelle** | **Ms. 429** |
| **Ancienne cote** | **137, 4, A** (cote de l'abbaye camaldule de Classe) |
| **Sigle critique** | **$\text{R}$** (avec distinction de la première main **$\text{R}^1$** et du réviseur/scholiaste contemporain **$\text{R}^2$**) |
| **Date de copie** | **Milieu du Xᵉ siècle** (env. 950 apr. J.-C., période de la « Renaissance macédonienne » sous Constantin VII Porphyrogénète) |
| **Origine et scriptorium** | **Constantinople**, dans le cercle du célèbre calligraphe **Éphrem le Moine** ($\text{Ἐφραίμ μοναχός}$, actif vers 948–962), copiste du *Marcianus gr. 454* (Venetus A de l'*Iliade*), du *Vaticanus gr. 124* (Polybe) et de l'*Athous Lavra* $\text{B 64}$ (Nouveau Testament). L'écriture de $\text{R}^1$ présente d'étroites affinités avec le *Laurentianus Plut. 32.9* (Sophocle, Eschyle, Apollonios de Rhodes) et le *Laurentianus Plut. 32.24*. |
| **Support matériel** | Parchemin de bonne qualité (quelques feuillets plus épais ou jaunis côté poil, quelques piqûres d'humidité marginales et plis de vélin). |
| **Dimensions** | Env. **$322 \times 210\text{ mm}$** (justification de la colonne poétique : env. $225 \times 110\text{ mm}$). |
| **Nombre de feuillets** | **191 folios** de parchemin (+ feuillets de garde modernes). Attention au **décalage de 2 unités** entre la foliotation traditionnelle (celle de l'édition phototypique de J. van Leeuwen, 1904 : `ff. 1–191`) et la numérotation mécanique moderne au crayon de la Biblioteca Classense (`ff. 3–193`, qui compte les deux gardes initiales). Dans ce dossier, les deux numérotations sont systématiquement indiquées : **les *Thesmophories* occupent les `ff. 162v–177r` (Leeuwen 1904) = `ff. 164v–179r` (Classense)**. |
| **Cahiers (quaternions)** | Composé majoritairement de **quaternions réguliers** (cahiers de 4 bifolios = 8 feuillets = 16 pages), signés par le copiste dans la marge inférieure ou supérieure. Les *Thesmophories* s'étendent sur la fin du 21ᵉ cahier, la totalité du 22ᵉ cahier et le début du 23ᵉ cahier. |
| **Mise en page** | Texte poétique copié sur **une seule colonne** à raison de **38 à 44 lignes par page** (le plus souvent **42 ou 43 lignes** dans les *Thesmophories*), réglé à la pointe sèche. Les parties lyriques et anapestiques sont fréquemment signalées par un léger retrait (*eisthesis*) ou dépassement (*ekthesis*) par rapport à l'alignement vertical des trimètres iambiques. Les marges latérales, supérieure et inférieure reçoivent les scholies anciennes ($\Sigma^{\text{R}}$). |

### 2.2. Contenu du manuscrit et place des *Thesmophories*

Le *Codex Ravennas 429* est le **seul manuscrit médiéval au monde à contenir les onze comédies conservées d'Aristophane**. Alors que les autres grands témoins anciens (notamment le *Venetus Marcianus gr. 474* [$\text{V}$, XIᵉ–XIIᵉ s.]) n'en contiennent que sept ou huit, le *Ravennas* présente les pièces dans l'ordre suivant :

1. **La « triade byzantine »** (pièces les plus lues à l'école) :
   1. *Ploutos* (`ff. 1r–16r`)
   2. *Les Nuées* (`ff. 16v–36v`)
   3. *Les Grenouilles* (`ff. 36v–56v`)
2. **Les huit autres comédies** (classées approximativement dans l'ordre inverse de l'alphabet grec ou selon les regroupements de deux corporations de libraires antiques) :
   4. *Les Oiseaux* (`ff. 56v–82r`)
   5. *Les Cavaliers* (`ff. 82v–102v`)
   6. *La Paix* (`ff. 103r–120r`)
   7. *Lysistrata* (`ff. 120v–136v`)
   8. *Les Acharniens* (`ff. 137r–152v`)
   9. *Les Guêpes* (`ff. 153r–162v`)
   10. ***Les Thesmophories*** (**`ff. 162v–177r`** [Classense `164v–179r`], soit **30 pages** exactement, pour **1231 vers**)
   11. *L'Assemblée des femmes* (*Ecclesiazusae*, `ff. 177r–191v`)

### 2.3. Histoire du codex : de Constantinople à Ravenne via Pise et Florence

1. **Copie à Constantinople (vers 950)** : Le manuscrit est copié sur un modèle issu de la translittération d'un codex antique en onciale doté de scholies marginales issues du commentaire alexandrin (Didyme, Symmaque, Héliodore pour la colométrie).
2. **Arrivée en Italie et épisode pisano-florentin (1515–1516)** :
   - Au début du XVIᵉ siècle, le codex se trouve à Urbino (probablement dans la bibliothèque ducale des Montefeltro), d'où il est emporté en 1515 à **Pise** au monastère camaldule de **San Michele in Borgo** par l'archevêque **Antonio Surian** (patriarche latin de Venise, ancien moine camaldule).
   - En 1515, l'imprimeur florentin **Bernardo Giunta (Filippo et Bernardo Giunti)** prépare à Florence une réédition d'Aristophane par les soins de l'humaniste **Eufrosino Bonini (Euphrosynus Boninus)**. Apprenant l'existence à Pise d'un très vieux manuscrit contenant deux comédies totalement inconnues de l'édition princeps aldine de Marcus Musurus (Venise, 1498 : qui ne comptait que 9 pièces, sans *Lysistrata* ni les *Thesmophories*), Bonini obtient communication du texte ou d'une copie rapide et publie en **janvier 1516** à Florence l'appendice juntin contenant l'***editio princeps* de *Lysistrata* et des *Thesmophories***.
   - C'est également de ce séjour italien du début du XVIᵉ siècle que dérive la copie humaniste de Munich, le ***Monacensis gr. 492*** (**$\text{Mu}$**, jadis *Augustanus*), qui ne contient que *Lysistrata* et les *Thesmophories* et qui est un **apographe direct (ou par un intermédiaire perdu) du *Ravennas*** : il n'a donc aucune valeur stemmatique indépendante, si ce n'est pour quelques conjectures faciles d'humaniste.
3. **Acquisition par Pietro Canneti et entrée à Ravenne (1712)** :
   - Après deux siècles d'oubli, le grand abbé camaldule et bibliophile **Pietro Canneti (1659–1730)** rachète le codex en Toscane en **1712** pour enrichir la bibliothèque du **monastère de Classe** à Ravenne (d'où son ancienne cote *137, 4, A* et son nom définitif de *Codex Ravennas*).
4. **Redécouverte philologique moderne (1794–1904)** :
   - **Filippo Invernizi** publie en **1794** à Leipzig la première édition d'Aristophane fondée sur une collation du *Ravennas* (réalisée à Ravenne en 1791), révélant à l'Europe savante sa supériorité écrasante sur l'Aldine et la Juntine, particulièrement pour les *Thesmophories*.
   - **Adolf von Velsen** réalise une collation minutieuse qui aboutit à son édition critique des *Thesmophoriazusae* (Leipzig, Teubner, **1883**), où la distinction entre $\text{R}^1$ et $\text{R}^2$ ainsi que les lectures sous grattage (*in rasura*) sont systématiquement établies.
   - En **1904**, **Johannes van Leeuwen** publie à Leyde (Sijthoff) la monumentale reproduction phototypique intégrale en grand in-folio : *Codex Aristophaneus Ravennas 137, 4, A phototypice editus*.
   - Aujourd'hui, le manuscrit est conservé à l'**Istituzione Biblioteca Classense** de Ravenne sous la cote **Ms. 429** et a fait l'objet d'une numérisation couleur haute définition.

### 2.4. Statut stemmatique : le *Ravennas* comme *unicodex* des *Thesmophories*

Pour les dix autres comédies d'Aristophane, l'éditeur dispose d'au moins deux ou trois manuscrits indépendants (par ex. $\text{R}$ et $\text{V}$ pour *Guêpes*, *Paix*, *Oiseaux* ; $\text{R}$, $\text{ \Gamma}$ [*Laurentianus 31.15* + *Leidensis Voss. gr. F 52*] et $\text{B}$ pour *Lysistrata* ; $\text{R}$, $\text{ \Gamma}$ et $\text{ \Lambda}$ pour *L'Assemblée des femmes*).

**Pour les *Thesmophories*, en revanche, le *Codex Ravennas 429* ($\text{R}$) est le SEUL manuscrit médiéval indépendant (*codex unicus*)** :

```
                      [ Archétype antique en onciale (IVᵉ–Vᵉ s.) ]
                                         │
              ┌──────────────────────────┴──────────────────────────┐
              ▼                                                     ▼
   [ Témoins antiques directs ]                        [ Hyparchétype médiéval ]
   • Π¹ : PSI XI 1194 (IIᵉ s., vv. 139–146,                     (IXᵉ–Xᵉ s.)
          237–246, 272–288, 594–596, 804–809)                       │
   • Π² : P.Oxy. LVI 3839 (IIᵉ–IIIᵉ s.,                             ▼
          vv. 5, 7–13, 19–22, 65–72, 77–96)           ╔═══════════════════════════╗
   • Π³ : P.Oxy. LVI 3840 (IVᵉ s.,                    ║  CODEX RAVENNAS 429 (R)   ║
          vv. 942–956, 958–979, 991–1000)             ║  Constantinople, ca. 950  ║
   • Π⁴ : P.Köln X 402 (Iᵉʳ–IIᵉ s.,                   ║   ff. 162v–177r (R¹ + R²) ║
          vv. 655–664)                                ╚═════════════╤═════════════╝
   • Π⁵ : P.Berol. 13231 + 21201 (Vᵉ–VIᵉ s.,                        │
          vv. 326–334, 360–369)                        ┌────────────┴────────────┐
                                                       ▼                         ▼
                                            [ Monacensis gr. 492 ]     [ Édition Juntine ]
                                              (Mu, XVIᵉ s., copie)     (Bonini, janv. 1516)
```

Il en résulte trois conséquences méthodologiques majeures pour l'édition critique :
1. **Toute leçon des *Thesmophories* qui ne provient ni des cinq courts fragments papyrologiques ($\Pi^1$–$\Pi^5$, qui ne couvrent ensemble qu'environ 115 vers souvent mutilés) ni de la tradition indirecte (Souda, Hésychius, Photius, Pollux, Athénée, scholies de Platon) repose exclusivement sur le témoignage de $\text{R}$.**
2. **La critique conjecturale des *Thesmophories* est avant tout une critique paléographique du *Ravennas*** : lorsqu'un vers est corrompu ou amétrique dans $\text{R}$, l'éditeur doit diagnostiquer si la faute remonte :
   - à une mélecture de l'**écriture minuscule bouletée du Xᵉ siècle** (modèle immédiat de $\text{R}^1$ ou distraction de $\text{R}^1$ lui-même),
   - ou à une mélecture antérieure de l'**écriture onciale antique** lors de la translittération du IXᵉ siècle,
   - ou encore à une **retouche malheureuse de $\text{R}^2$** qui a gratté la leçon authentique de $\text{R}^1$.
3. **Les papyrus d'Oxyrhynque et de Cologne confirment à la fois l'excellence globale de $\text{R}$ et l'ancienneté de certaines corruptions**, tout en apportant parfois la vraie leçon contre une faute de $\text{R}$ : par exemple au **v. 657**, où $\text{R}$ a `εἰσελήλυθεν` (amétrique au début d'un tétramètre trochaïque), le papyrus de Cologne $\Pi^4$ (*P.Köln* X 402) confirme la conjecture de Hermann `ἐπελήλυθε(ν)` (confusion d'onciale `ΕΠΕΛΗΛΥΘΕ` $\to$ `ΕΙϹΕΛΗΛΥΘΕ`).

---

## 3. Étude paléographique de l'écriture du *Ravennas* (appliquée à l'édition des *Thesmophories*)

### 3.1. Distinction des deux mains : $\text{R}^1$ (texte) et $\text{R}^2$ (argument, didascalies, scholies, révisions)

L'examen direct des planches `ff. 162v–177r` impose de distinguer avec la plus grande rigueur **deux mains contemporaines du milieu du Xᵉ siècle**, qui travaillent dans le même atelier constantinopolitain mais avec des écritures, des encres et des fonctions bien distinctes :

#### 1. La première main ($\text{R}^1$) : le copiste du texte poétique
* **Type d'écriture** : **Minuscule livresque penchée à tendance « bouletée »** (*sloping bouletée minuscule*), caractéristique des années 940–960 à Constantinople. Le tracé est souple, régulier, légèrement incliné vers la droite, avec de petits renflements (« boules ») à l'extrémité des hastes et des traits d'attaque.
* **Étendue de son travail dans les *Thesmophories*** :
  - $\text{R}^1$ a copié **uniquement le texte poétique des vers 1 à 1231**, à l'encre brune moyenne.
  - $\text{R}^1$ n'a copié **ni l'Argument (*Hypothesis*)** du `f. 162v` (il avait laissé un espace blanc d'environ 13 lignes en haut du `f. 162v` après le titre), **ni les noms des personnages en marge**, **ni les scholies**.
* **Signalisation des changements d'interlocuteur par $\text{R}^1$** :
  - Fidèle à l'usage des manuscrits antiques et des papyrus dramatiques, $\text{R}^1$ n'écrit pas le nom du personnage qui parle : il indique simplement le changement de locuteur :
    1. **En début de vers** par une ***paragraphos*** (`—`), petit trait horizontal tracé dans la marge gauche juste sous le début du vers où commence ou finit une réplique ;
    2. **À l'intérieur d'un vers (*antilabè*)** par le ***dikolon*** (`:`), double point suivi d'un léger blanc (souvent accompagné d'une *paragraphos* en marge gauche).
* **Habitudes graphiques propres à $\text{R}^1$** :
  - **Iota muet toujours adscrit (jamais souscrit)** lorsqu'il est noté (`τῶι`, `ῆι`, `αύτηι`), mais très fréquemment omis.
  - **Bêta** presque toujours de forme minuscule cursive (`u` fermé ou à deux boucles), rarement oncial (`Β`) sauf à l'initiale de vers ou en ligature.
  - **Kappa** le plus souvent minuscule à deux temps, parfois agrandi.
  - **Nu** minuscule (`μ` à jambage droit remontant), extrêmement proche du **mu** (`μ`), ce qui explique les innombrables confusions `μ / ν` (notamment aux désinences `-ον / -ομ` ou à l'intérieur des mots).

#### 2. La seconde main ($\text{R}^2$) : le réviseur, rubricateur et scholiaste
* **Type d'écriture** : **Semi-onciale de glose (*Kleinoziale* / *scholia-uncial*)** mêlée d'éléments minuscules et de nombreuses **abréviations tachygraphiques** (syllabes finales surélevées, signes spéciaux pour `-ος`, `-ον`, `-ων`, `-αι`, `-ης`, `καί`). Le module est plus petit, le tracé plus redressé et anguleux que celui de $\text{R}^1$, avec une encre souvent légèrement plus foncée ou jaunâtre selon les campagnes de révision.
* **Étendue de son travail dans les *Thesmophories*** :
  1. **L'Argument (*Hypothesis*) et la liste des personnages** en tête du [`f. 162v`](folios_individuels_ff162v-177r/01_f162v_classense164v_vv0001-0042.jpg) : c'est $\text{R}^2$ qui a rempli l'espace laissé par $\text{R}^1$ en copiant en semi-onciale l'argument alexandrin où le Parent d'Euripide (*Κηδεστής*) est appelé **Mnésiloque** (`Μνησίλοχος`, `κηδεστὴς Εὐριπίδου Μνησίλοχος`).
  2. **Les sigles des personnages (*notae personarum*)** dans les marges et au-dessus des *dikola* internes aux vers (`κηδ/`, `μνησ/`, `ευρ/`, `θερ/`, `αγαθ/`, `χορ/`, `γυν/`, `κλεισθ/`, `κρiτ/`, `τοξ/`).
  3. **Les didascalies scéniques (*parepigraphai*)** insérées dans le texte ou en marge (voir § 3.2).
  4. **Les scholies marginales et gloses interlinéaires ($\Sigma^{\text{R}}$)** : abondantes aux `ff. 162v–170v`, plus clairsemées dans le dernier tiers de la pièce (`ff. 171r–177r`).
  5. **La révision du texte poétique de $\text{R}^1$** : $\text{R}^2$ a relu le texte en le collationnant (soit sur le modèle même de $\text{R}^1$, soit sur un second exemplaire), ajoutant des lettres omises au-dessus de la ligne, corrigeant des esprits et accents, et **grattant au canif (*in rasura*)** de nombreux passages de $\text{R}^1$ pour y substituer une autre leçon (voir le relevé complet au § 3.6).

---

### 3.2. Attribution des répliques (*notae personarum*) et didascalies scéniques (*parepigraphai*)

Ce point est **capital pour l'apparat critique et le commentaire des *Thesmophories*** :

1. **Autorité très faible des noms de personnages ($\text{R}^2$) par rapport aux signes de coupure ($\text{R}^1$)** :
   - Les *paragraphoi* (`—`) et *dikola* (`:`) de $\text{R}^1$ remontent à la tradition antique (même s'il arrive qu'une *paragraphos* glisse d'un vers vers le haut ou vers le bas, ou qu'un *dikolon* ponctue une simple pause syntaxique).
   - En revanche, les noms abrégés ajoutés par $\text{R}^2$ (`κηδ/`, `μνησ/`, `ευρ/`, `γυν/`) résultent souvent d'une **interprétation personnelle ou scolaire tardive** et fourmillent d'erreurs manifestes :
     - **Flottement entre `Κηδεστής` et `Μνησίλοχος`** : dans le texte des *Thesmophories*, Aristophane ne nomme jamais le Parent d'Euripide « Mnésiloque » (il l'appelle simplement `κηδεστής` aux vv. 74, 210, 584, 1165). Le nom de `Μνησίλοχος` (emprunté au beau-père historique d'Euripide, mentionné par Aristophane dans les *Télémessiens* fr. 559 K.-A.) vient de l'*Hypothesis* et des scholies copiées par $\text{R}^2$. Dans les marges, $\text{R}^2$ alterne entre `κηδ/` et `μνησ/`.
     - **Confusions de locuteurs dès le prologue** : aux **vv. 1–28** ([`f. 162v`](folios_individuels_ff162v-177r/01_f162v_classense164v_vv0001-0042.jpg)), la répartition des répliques entre Euripide et le Parent est gravement brouillée par les signes et attributions de $\text{R}^2$, notamment aux vv. 4–6 (`οἷόν τε...`) et 21–24 (`πῶς ἂν οὖν...`).
     - **Scène d'Agathon (`ff. 163v–165r`, vv. 101–265)** : lors de la monodie d'Agathon (vv. 101–129, [`f. 163v`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0001-0122.jpg)–[`f. 164r`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg)), Agathon chante à la fois le rôle de la coryphée troyenne et celui du chœur troyen ; $\text{R}^2$ (ou son modèle) y insère à tort des indications `χορός` comme si le chœur des Thesmophories entrait déjà en scène.
     - **Assemblée des femmes (`ff. 166r–170r`, vv. 295–654)** : la distinction entre la Héraut (`Κηρύκαινα`), le Coryphée, Mika (Première Femme) et Kritylla (Deuxième Femme) est très confuse dans les sigles de $\text{R}^2$.

2. **Les quatre grandes *parepigraphai* (didascalies scéniques internes) conservées dans $\text{R}$** :
   Les *Thesmophories* font partie des très rares textes dramatiques grecs (avec les *Acharniens*, les *Oiseaux* et les *Limiers* de Sophocle) à avoir conservé dans la colonne même du texte d'anciennes **indications scéniques (*parepigraphai*)** notant un jeu de scène muet ou un bruitage :
   - **Entre les vv. 99 et 100 ([`f. 163v`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0001-0122.jpg))** : **`μινυρισμός`** (*« fredonnement à bouche fermée / prélude vocal aigu d'Agathon »* avant le début de son chant au v. 101).
   - **Entre les vv. 129 et 130 ([`f. 164r`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg))** : **`ὀλολύζει ὁ γέρων`** (*« le vieillard [le Parent] pousse un cri rituel d'ololyguè »* à la fin du chant d'Agathon).
   - **Au v. 276 / 277 ([`f. 165v`](folios_individuels_ff162v-177r/07_f165v_classense167v_vv0252-0294.jpg))** : **`ὀλολύζει· τὸ ἱερὸν ὠθεῖται`** (*« on pousse l'ololyguè ; le sanctuaire [le Thesmophorion sur l'ekkuklèma] est poussé vers l'extérieur »*). Didascalie d'une valeur inestimable pour la machinerie théâtrale du Vᵉ siècle !
   - **Après le v. 1187 ([`f. 176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg))** : **`ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημένος·`** (c'est-à-dire `ἀνακύπτει καὶ παρακύπτει ἀπεψωλημένος`, *« il [l'Archer scythe] se redresse et se penche de côté, le gland découvert [en érection] »* pendant la danse de la jeune joueuse de flûte Élaphion). Comme démontré dans le commentaire du v. 1187, cette phrase en prose non métrique est une *parepigraphè* antique insérée entre les vv. 1187 et 1188, exactement parallèle à `ὀλολύζει` (v. 276).

---

### 3.3. Morphologie des lettres et confusions paléographiques récurrentes

Pour justifier ou évaluer une conjecture dans l'apparat critique et le commentaire des *Thesmophories*, il faut distinguer **deux strates paléographiques de fautes** dans le *Ravennas* :

#### A. Confusions nées de la minuscule bouletée du Xᵉ siècle

Dans l'écriture minuscule de $\text{R}^1$ et de son modèle immédiat :

| Lettres confondues | Mécanisme paléographique dans la minuscule de $\text{R}$ | Exemples typiques dans les *Thesmophories* (`ff. 162v–177r`) |
| :---: | :--- | :--- |
| **`μ` $\leftrightarrow$ `ν`** | En minuscule du Xᵉ s., le `ν` s'écrit avec deux jambages liés par le bas comme un `μ` dont la hampe gauche descend et le trait droit remonte légèrement : dans la vitesse du ductus, `μ` et `ν` sont **quasi indiscernables**. | • **v. 50** ([`f. 163r`](folios_individuels_ff162v-177r/02_f163r_classense165r_vv0043-0079.jpg)) : $\text{R}$ `πρόμοις` pour `πρόνοις` (`προχύταις` ou `προόδοις`).<br>• **v. 162** ([`f. 164r`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg)) : $\text{R}$ `ἐχυμώισαν` (`ἐχύμωσαν`) corrigé par Toup en `ἐκόσμησαν` (combiné avec confusion `κ/χ`).<br>• **v. 164** ([`f. 164r`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg)) : $\text{R}$ `τοῦτομ γὰρ` (assimilation phonétique mais aussi tracé ambigu `μ/ν`). |
| **`β` (`u`) $\leftrightarrow$ `κ` $\leftrightarrow$ `μ`** | Le bêta minuscule (`u` fermé en haut) ressemble étroitement à un `κ` minuscule à boucle fermée ou à un `μ` dont la haste est courte. | • Nombreuses variantes byzantines entre `β` et `κ` à l'intérieur des mots (ex. formes de `βάλλω / καλέω`, `βλέπω / κλέπτω`). |
| **`α` $\leftrightarrow$ `ο` $\leftrightarrow$ `ω` $\leftrightarrow$ `ου`** | Le `α` minuscule à une boucle suivi d'un trait de liaison se confond avec `ο` ou avec un `ω` fermé (en 8 couché) ou la ligature `ου`. | • **v. 117** ([`f. 163v`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0080-0122.jpg)) : $\text{R}$ `ἀεισάτω` $\to$ `ἀείσατ'` ou `κλῄζουσα`.<br>• **v. 1174** ([`f. 176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg)) : $\text{R}$ `κωμάσδο` (barbarisme scythe) pour `κωμάζω / κωμάσδω`.<br>• **v. 1198** ([`f. 176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg)) : $\text{R}$ `καλῶς` en fin de vers (répété du v. 1196) au lieu de `ταχὺ` / `λαβών`. |
| **`ι` $\leftrightarrow$ `ς` / `-οισ` $\leftrightarrow$ `-οι`** | Le sigma lunaire ou final lié à `ι` (`ις`) se réduit facilement à un simple trait vertical ou inversement. | • **v. 50** ([`f. 163r`](folios_individuels_ff162v-177r/02_f163r_classense165r_vv0043-0079.jpg)) : finale `-οις / -οι`.<br>• Désinences de datif pluriel `-οισι(ν)` / `-οις` constamment flottantes selon le mètre. |
| **`γ` $\leftrightarrow$ `τ` $\leftrightarrow$ `π`** | La barre horizontale supérieure du `γ`, du `τ` et du `π` minuscules est identique ; un jambage effacé ou trop court fait passer de l'un à l'autre. | • **v. 702** ([`f. 170v`](folios_individuels_ff162v-177r/17_f170v_classense172v_vv0679-0720.jpg)) : confusion entre `τ` et `γ` / abréviation de `δ`. |
| **Prothèse, haplographie ou métathèse de `σ`** | Au contact d'une dentale (`τ`, `θ`), d'une gutturale (`κ`, `χ`) ou d'une labiale (`π`, `φ`), le copiste ajoute ou omet fréquemment une sifflante. | • **v. 557** ([`f. 169r`](folios_individuels_ff162v-177r/14_f169r_classense171r_vv0551-0589.jpg)) : $\text{R}$ `στλεγγίδας` (avec `σ` initial).<br>• **v. 1114** ([`f. 175v`](folios_individuels_ff162v-177r/27_f175v_classense177v_vv1082-1127.jpg)) : $\text{R}$ `σκυτο` (dans le grec écorché de l'Archer scythe) pour `κύστο(ν)` (`κύσθον`), par métathèse de la sifflante (`κυστο` $\to$ `σκυτο`) sous l'influence de `Σκύθης / σκῦτος`. |

#### B. Confusions héritées de l'onciale ancienne (transcription *majuscule $\to$ minuscule*)

Beaucoup des fautes les plus profondes de $\text{R}$ s'expliquent par la lecture fautive d'un **archétype en écriture onciale (`Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Ϲ Τ Υ Φ Χ Ψ Ω`) en *scriptio continua*** :

| Lettres onciales confondues | Mécanisme en écriture majuscule (*scriptio continua*) | Exemples décisifs dans les *Thesmophories* (`ff. 162v–177r`) |
| :---: | :--- | :--- |
| **`Α` $\leftrightarrow$ `Δ` $\leftrightarrow$ `Λ`** et **`ΛΙ` $\leftrightarrow$ `Ν` $\leftrightarrow$ `Μ`** | En onciale, `Α`, `Δ` et `Λ` sont trois triangles qui ne diffèrent que par leur barre horizontale (souvent très fine ou effacée). De plus, la séquence `ΛΙ` ou `ΑΙ` collée en *scriptio continua* forme exactement le dessin d'un `Ν` (`ΛΙ` = `Ν`). | • **v. 910** ([`f. 173r`](folios_individuels_ff162v-177r/22_f173r_classense175r_vv0876-0919.jpg)) : $\text{R}$ donne le monstre **`ἀπὸ λαιφίων`** (`ΑΠΟΛΑΙΦΙΩΝ`), brillamment corrigé par Louis Hauseux en **`ἀπ' ἀφύων`** (`ΑΠΑΦΥΩΝ`, *« au retour du marché aux anchois »*, cf. Hésychius $\alpha\ 8779$) par diplographie triangulaire `ΑΠΑ` $\to$ `ΑΠΟΛΑΙ` et iotacisme `υ` $\to$ `ι`.<br>• **v. 1039** ([`f. 174v`](folios_individuels_ff162v-177r/25_f174v_classense176v_vv1001-1043.jpg)) : $\text{R}$ **`λιτομέναν`** (`ΛΙΤΟΜΕΝΑΝ`), que la Souda cite sous la forme **`ἀντομέναν`** (`ΑΝΤΟΜΕΝΑΝ`) : en onciale, **`ΛΙ`** et **`ΑΝ`** ont été confondus ! |
| **`Π` $\leftrightarrow$ `Τ` $\leftrightarrow$ `Γ`** | En onciale, un `Π` dont le jambage droit est effacé devient `Γ` ou `Τ` ; inversement, un `Τ` proche d'un `Ι` (`ΤΙ`) est lu `Π`. | • **v. 834** ([`f. 172r`](folios_individuels_ff162v-177r/20_f172r_classense174r_vv0800-0837.jpg)) : $\text{R}$ **`Τηνίοισι`** (`ΤΗΝΙΟΙϹΙ`, *« aux habitants de Ténos »*) au lieu du jeu de mots comique sur la bobine **`Πηνίοισι`** (`ΠΗΝΙΟΙϹΙ`), par confusion d'onciale `Π` / `Τ`. |
| **`Π` $\leftrightarrow$ `ΙϹ`** | En onciale lunaire, la séquence `ΙϹ` (iota + sigma lunaire serrés) se confond avec `Π` (et inversement `ΕΠΕ-` est lu `ΕΙϹΕ-`). | • **v. 657** ([`f. 170r`](folios_individuels_ff162v-177r/16_f170r_classense172r_vv0635-0678.jpg)) : $\text{R}$ a **`εἰσελήλυθεν`** (`ΕΙϹΕΛΗΛΥΘΕΝ`, amétrique), là où le papyrus de Cologne $\Pi^4$ (*P.Köln* X 402) donne la vraie leçon **`ἐπελήλυθε(ν)`** (`ΕΠΕΛΗΛΥΘΕ`). |
| **`Ε` $\leftrightarrow$ `Θ` $\leftrightarrow$ `Ο` $\leftrightarrow$ `Ϲ`** | Les quatre lettres rondes de l'onciale grecque (`Ε`, `Θ`, `Ο`, `Ϲ` = sigma lunaire) ne se distinguent que par leur barre médiane ou leur ouverture à droite. | • **v. 700** ([`f. 170v`](folios_individuels_ff162v-177r/17_f170v_classense172v_vv0679-0720.jpg)) : nombreuses corruptions dans les chœurs lyriques (vv. 667–725, 959–1000, 1015–1055, 1136–1159) dues à la confusion des rondes onciales. |
| **`Η` $\leftrightarrow$ `Ν` $\leftrightarrow$ `Π` $\leftrightarrow$ `ΙΙ`** | Deux hastes verticales reliées par une barre horizontale (`Η`), oblique (`Ν`) ou supérieure (`Π`). | • Confusions fréquentes entre les particules `ἦ / ἤ` et `νῦν / νυν`, ou entre `π` et `η` dans les mots rares. |

---

### 3.4. Abréviations tachygraphiques, ligatures et signes diacritiques

Si $\text{R}^1$ écrit presque tous les mots en toutes lettres (à l'exception de quelques fins de lignes trop longues où il abrège `-ν` par un trait horizontal supérieur ou `-αι / -ος`), **$\text{R}^2$ emploie tout l'arsenal tachygraphique constantinopolitain du Xᵉ siècle** (et certaines corruptions de $\text{R}^1$ prouvent que son modèle comportait déjà des abréviations) :

1. **Abréviations de finales par suspension et superposition** :
   - **Trait horizontal supérieur (`¯`)** = **`ν`** (surtout en fin de ligne ou de mot : `τῶ¯` = `τῶν`, `μὲ¯` = `μέν`).
   - **Accent circonflexe ou double crochet en exposant (`˜` / `ς`)** = **`-αι`** (`γυναῖκ˜` = `γυναῖκες` ou `-αι`).
   - **Cercle en exposant (`°`)** = **`-ος`** ; **cercle barré ou double trait** = **`-ον`** ; **oméga suscrit (`ω`)** = **`-ων`**.
   - **Signe en forme de `s` ou d'esprit rude inversé en exposant** = **`-ης`** ou **`-εις`**.
   - **Signe en forme de `4` ou de `Ϙ` barré** = **`καί`**.
2. **Signes tachygraphiques spéciaux (syllabiques)** :
   - Un cas particulièrement remarquable mis en lumière dans le commentaire du **v. 702 ([`f. 170v`](folios_individuels_ff162v-177r/17_f170v_classense172v_vv0679-0720.jpg))** est le signe tachygraphique du **delta surmonté d'un tréma ($\ddot{\delta}$)** pour la syllabe **`δι-`** (et les préverbes `δια-`), dont la mélecture explique les corruptions sur les composés en `δια-` / `διδ-`.
3. **Signes critiques et métriques hérités d'Alexandrie** :
   - Au [`f. 162v`](folios_individuels_ff162v-177r/01_f162v_classense164v_vv0001-0042.jpg), le titre `※ ἀριστοφάνους θεσμοφοριάζουσαι —` est encadré par l'**astérisque (`※`)** à gauche et la *paragraphos* à droite.
   - Dans les marges de plusieurs passages lyriques figurent encore des vestiges de la **colométrie d'Héliodore** (*diple obelismene* `>—`, *koronis* marquant la fin d'une strophe ou de la parabase au [`f. 171v`](folios_individuels_ff162v-177r/19_f171v_classense173v_vv0765-0799.jpg) / [`f. 172r`](folios_individuels_ff162v-177r/20_f172r_classense174r_vv0800-0837.jpg)).

---

### 3.5. Orthographe byzantine, iotacismes, élisions et crases dans le *Ravennas*

L'éditeur des *Thesmophories* ne doit pas alourdir inutilement son apparat critique avec de simples variantes orthographiques byzantines, mais doit en connaître les lois constantes dans $\text{R}$ :

1. **Iotacismes constants** (prononciation médiévale en `/i/` de `ι, η, ει, οι, υ, ῃ`) :
   - **`ει` $\leftrightarrow$ `ι` $\leftrightarrow$ `η`** : omniprésent dans $\text{R}^1$, souvent corrigé au-dessus de la ligne par $\text{R}^2$. Par ex. au **v. 1083 ([`f. 175v`](folios_individuels_ff162v-177r/27_f175v_classense177v_vv1082-1127.jpg))**, $\text{R}$ écrit `τί λαλῖς` pour `τί λαλεῖς` ; au **v. 1187 ([`f. 176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg))**, la *parepigraphè* écrit `ἀνακύπτη· καὶ παρακύπτι·` pour `ἀνακύπτει καὶ παρακύπτει`.
   - **`αι` $\leftrightarrow$ `ε`** (prononcés tous deux `/e/`) : fréquent dans les désinences verbales médio-passives (`-εσθαι` / `-εσθε`) et les infinitifs.
   - **`οι` $\leftrightarrow$ `υ` $\leftrightarrow$ `η`** : par ex. `σοι / συ`, `μοι / με`, ou dans le grec barbare du Scythe (`ff. 174v–177r`).
2. **Atticismes authentiques conservés ou altérés par $\text{R}$** :
   - **`πο-` sans iota pour `ποι-` devant voyelle (`ποῶ`, `ποεῖς`, `ποεῖν`)** : en attique du Vᵉ siècle, le verbe `ποιέω` perd souvent son iota intervocalique lorsque la première syllabe doit être brève (`˘`). Le *Ravennas* a parfois conservé cette graphie ou l'a corrompue en un autre mot : ainsi au **v. 815 ([`f. 172r`](folios_individuels_ff162v-177r/20_f172r_classense174r_vv0800-0837.jpg))**, où le sens et le mètre appellent `ποοῦντας` (*« faisant »*), $\text{R}$ a lu `ποθοῦντας` (*« désirant »*) par insertion fautive d'un `θ` dans la forme attique `ποοῦντας` !
   - **`ξύν` vs `σύν`**, **`ἐς` vs `εἰς`**, **`αἰεί` vs `ἀεί`** : $\text{R}$ conserve souvent la forme attique ancienne (`ξυν-`, `ἐς`, `αἰεί`), mais la remplace parfois par la forme de la *koinè* même contre le mètre.
   - **Nu éphelcystique (`-ν`)** : ajouté systématiquement par $\text{R}^1$ en fin de vers ou devant consonne, parfois contre le mètre, ou omis devant voyelle.
3. **Scriptio plena, élisions et crases** :
   - Très souvent, $\text{R}^1$ écrit les deux mots en entier (**scriptio plena**, ex. `δὲ ἐγώ` au lieu de `δ' ἐγώ`, `τὰ ἀγαθά` au lieu de `τἀγαθά`), laissant au lecteur le soin de faire l'élision ou la crase à la scansion, ou bien il note l'apostrophe tout en conservant la voyelle élidée (surtout corrigée par $\text{R}^2$).
   - **Prodelision (aphérèse)** : fréquemment méconnue par $\text{R}^1$ (par ex. `'στὶ` après `-η` au **v. 80**, [`f. 163v`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0080-0122.jpg) : `τρίτη 'στὶ Θεσμοφορίων ἡ μέση`).
4. **Le cas particulier du grec barbare de l'Archer scythe (`ff. 174v–177r`, vv. 1001–1225)** :
   - Dans les scènes finales, l'Archer scythe (`Τοξότης`) parle un grec pidgin caractérisé par :
     - la **psilose des aspirées** (`κ, π, τ` au lieu de `χ, φ, θ` : ex. v. 1126 [`f. 175v`](folios_individuels_ff162v-177r/27_f175v_classense177v_vv1082-1127.jpg) `τὸ κεπαλή` pour `τὴν κεφαλήν`, v. 1210 [`f. 176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg) `ὡς καρίεντό σοι τὸ τυγάτριον` pour `ὡς χαρίεν σου τὸ θυγάτριον`),
     - l'emploi de `-ι` ou `-ο` comme désinence passe-partout,
     - la confusion des genres et des cas.
   - **Intérêt paléographique crucial** : $\text{R}^1$ a fidèlement conservé la plupart de ces barbarismes phonétiques comiques, tandis que $\text{R}^2$ (ou des éditeurs postérieurs) a parfois tenté à tort de « normaliser » l'orthographe attique du Scythe ! L'examen direct des planches `25` à `30` (`ff. 174v–177r`) est donc indispensable pour distinguer la main de $\text{R}^1$ des retouches normalisatrices de $\text{R}^2$.

---

### 3.6. Relevé critique des grattages (*in rasura*) et corrections ($\text{R}^1 / \text{R}^2$) dans les *Thesmophories*

Sur les reproductions haute définition en couleur de la Biblioteca Classense réunies dans ce dossier, on distingue beaucoup mieux que sur le fac-similé en noir et blanc de 1904 les endroits où le parchemin a été gratté au canif (*in rasura*) par $\text{R}^2$. Voici les principaux lieux critiques à inspecter folio par folio :

| Folio (Leeuwen / Classense) | Vers | État du *Ravennas* ($\text{R}^1$, $\text{R}^2$, *in rasura*) et intérêt pour l'édition |
| :--- | :---: | :--- |
| **[`01_f162v`](folios_individuels_ff162v-177r/01_f162v_classense164v_vv0001-0042.jpg)** (`164v`) | *Hyp.* + vv. 1–42 | • *Hypothesis* entière de la main de $\text{R}^2$ (donne le nom `Μνησίλοχος`).<br>• **vv. 2–6, 23–25** : grattages et surcharges sur les signes d'attribution des répliques (`ευρ/`, `μνησ/`) et sur la ponctuation.<br>• **v. 38** : scholie marginale de $\text{R}^2$ expliquant `προθυσόμενος`. |
| **[`02_f163r`](folios_individuels_ff162v-177r/02_f163r_classense165r_vv0043-0079.jpg)** (`165r`) | vv. 43–79 | • **v. 50** : $\text{R}^1$ `πρόμοις` (confusion `μ/ν`).<br>• **vv. 65–79** : passage recoupé par le papyrus d'Oxyrhynque $\Pi^2$ (*P.Oxy.* LVI 3839). |
| **[`03_f163v`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0080-0122.jpg)** (`165v`) | vv. 80–122 | • **v. 99/100** : *parepigraphè* `μινυρισμός` au milieu de la colonne.<br>• **vv. 101–122** : début de la monodie d'Agathon, avec colométrie lyrique en retrait (*eisthesis*) et indications marginales `χορός` ajoutées à tort par $\text{R}^2$. |
| **[`04_f164r`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg)** (`166r`) | vv. 123–164 | • **v. 129/130** : *parepigraphè* `ὀλολύζει ὁ γέρων`.<br>• **v. 134** : problèmes d'aspiration et de crase.<br>• **v. 162** : $\text{R}$ `ἐχυμώισαν` (corrigé en `ἐκόσμησαν`), avec longue scholie sur Ibycos, Anacréon et Alcée. |
| **[`05_f164v`](folios_individuels_ff162v-177r/05_f164v_classense166v_vv0165-0207.jpg)** (`166v`) | vv. 165–207 | • **v. 168** : corruption célèbre sur Philoclès (`ἃ δ' ἂν φιλοκλῆς αἰσχρὸς ὢν αἰσχρῶς ποιεῖ`). |
| **[`07_f165v`](folios_individuels_ff162v-177r/07_f165v_classense167v_vv0252-0294.jpg)** (`167v`) | vv. 252–294 | • **v. 276/277** : *parepigraphè* `ὀλολύζει· τὸ ἱερὸν ὠθεῖται`.<br>• **v. 289** : grattage sur le nom de la fille (`Θρᾷττα`). |
| **[`08_f166r`](folios_individuels_ff162v-177r/08_f166r_classense168r_vv0295-0336.jpg)** (`168r`) | vv. 295–336 | • **vv. 295–311** : prière en prose de la Héraut (`Κηρύκαινα`) disposée en lignes longues comme des vers.<br>• **vv. 326–334** : recoupé par le papyrus de Berlin $\Pi^5$ (*P.Berol.* 13231). |
| **[`11_f167v`](folios_individuels_ff162v-177r/11_f167v_classense169v_vv0423-0465.jpg)** (`169v`) | vv. 423–465 | • **vv. 433–458** : premier chœur et discours de Couronne-de-Myrte (Deuxième Femme). |
| **[`14_f169r`](folios_individuels_ff162v-177r/14_f169r_classense171r_vv0551-0589.jpg)** (`171r`) | vv. 551–589 | • **v. 557** : $\text{R}$ `στλεγγίδας` (avec `σ` initial).<br>• **v. 574** : entrée de Clisthène. |
| **[`16_f170r`](folios_individuels_ff162v-177r/16_f170r_classense172r_vv0635-0678.jpg)** (`172r`) | vv. 635–678 | • **v. 657** : $\text{R}$ `εἰσελήλυθεν` (corrigé par $\Pi^4$ en `ἐπελήλυθε`). |
| **[`17_f170v`](folios_individuels_ff162v-177r/17_f170v_classense172v_vv0679-0720.jpg)** (`172v`) | vv. 679–720 | • **vv. 700–702** : passage lyrique très altéré (rondes d'onciale et abréviation tachygraphique $\ddot{\delta}$). |
| **[`20_f172r`](folios_individuels_ff162v-177r/20_f172r_classense174r_vv0800-0837.jpg)** (`174r`) | vv. 800–837 | • **vv. 800–845** : *Epirrhèma* de la parabase (éloge des femmes, jeu de mots sur les noms propres).<br>• **v. 815** : $\text{R}$ `ποθοῦντας` pour `ποοῦντας`.<br>• **v. 834** : $\text{R}$ `Τηνίοισι` pour `Πηνίοισι` (confusion onciale `Π/Τ`). |
| **[`22_f173r`](folios_individuels_ff162v-177r/22_f173r_classense175r_vv0876-0919.jpg)** (`175r`) | vv. 876–919 | • **vv. 850–928** : parodie de l'*Hélène* d'Euripide.<br>• **v. 910** : $\text{R}$ `ἀπὸ λαιφίων` (corrigé en `ἀπ' ἀφύων` : diplographie d'onciale `ΑΠΑ` $\to$ `ΑΠΟΛΑΙ`). |
| **[`24_f174r`](folios_individuels_ff162v-177r/24_f174r_classense176r_vv0959-1000.jpg)** (`176r`) | vv. 959–1000 | • **vv. 959–1000** : ronde chorale des femmes (recoupée par $\Pi^3$, *P.Oxy.* LVI 3840). |
| **[`25_f174v`](folios_individuels_ff162v-177r/25_f174v_classense176v_vv1001-1043.jpg)** (`176v`) | vv. 1001–1043 | • **v. 1001** : première intervention de l'Archer scythe (`ὦ τοξόθ', ἱκετεύω σε · μή μ' ἱκετεῦσι σύ`).<br>• **vv. 1015–1055** : monodie parodique d'*Andromède*.<br>• **v. 1039** : $\text{R}$ `λιτομέναν` (Souda : `ἀντομέναν`, confusion d'onciale `ΛΙ/ΑΝ`). |
| **[`26_f175r`](folios_individuels_ff162v-177r/26_f175r_classense177r_vv1044-1081.jpg)** (`177r`) | vv. 1044–1081 | • **vv. 1056–1097** : scène d'Écho (`Ἠχώ`), avec répétition systématique des fins de vers. |
| **[`27_f175v`](folios_individuels_ff162v-177r/27_f175v_classense177v_vv1082-1127.jpg)** (`177v`) | vv. 1082–1127 | • **v. 1114** : $\text{R}$ `σκυτο` (dans la bouche du Scythe) pour `κύστο(ν)` (`κύσθον`). |
| **[`29_f176v`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg)** (`178v`) | vv. 1169–1210 | • **v. 1187/1188** : célèbre *parepigraphè* `ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημένος·` copiée sur une ligne propre dans la colonne poétique.<br>• **v. 1198** : $\text{R}$ `καλῶς` répété par saut du même au même depuis le v. 1196. |
| **[`30_f177r`](folios_individuels_ff162v-177r/30_f177r_classense179r_vv1211-1231_fin.jpg)** (`179r`) | vv. 1211–1231 | • **vv. 1227–1231** : *exodos* anapestique du Chœur (`ἀλλὰ πέπαισται μετρίως ἡμῖν... τὼ Θεσμοφόρω δ' ἡμῖν ἀγαθὴν / τούτων χάριν ἀνταποδοίτην`).<br>• Suivi immédiatement d'un bandeau ornemental et de l'*Hypothesis* de *L'Assemblée des femmes* (*Ecclesiazusae*). |

---

## 4. Répertoire analytique planche par planche et folio par folio (`ff. 162v–177r`)

### 4.1. Tableau des 15 planches doubles (bifolios ouverts, vues 166 à 180)

Chaque planche double présente à gauche le *verso* d'un feuillet et à droite le *recto* du feuillet suivant (`4023 × 2832 px`) :

| N° | Fichier (lien cliquable) | Vue IIIF | Folios (Leeuwen 1904) | Folios (Classense) | Vers des *Thesmophories* |
| :-: | :--- | :-: | :---: | :---: | :---: |
| **01** | [`01_planche166_ff162v-163r_vv0001-0079.jpg`](planches_doubles_ff162v-177r/01_planche166_ff162v-163r_vv0001-0079.jpg) | 166 | **ff. 162v – 163r** | `164v – 165r` | *Hypothesis* + **vv. 1 – 79** |
| **02** | [`02_planche167_ff163v-164r_vv0080-0164.jpg`](planches_doubles_ff162v-177r/02_planche167_ff163v-164r_vv0080-0164.jpg) | 167 | **ff. 163v – 164r** | `165v – 166r` | **vv. 80 – 164** |
| **03** | [`03_planche168_ff164v-165r_vv0165-0251.jpg`](planches_doubles_ff162v-177r/03_planche168_ff164v-165r_vv0165-0251.jpg) | 168 | **ff. 164v – 165r** | `166v – 167r` | **vv. 165 – 251** |
| **04** | [`04_planche169_ff165v-166r_vv0252-0336.jpg`](planches_doubles_ff162v-177r/04_planche169_ff165v-166r_vv0252-0336.jpg) | 169 | **ff. 165v – 166r** | `167v – 168r` | **vv. 252 – 336** |
| **05** | [`05_planche170_ff166v-167r_vv0337-0422.jpg`](planches_doubles_ff162v-177r/05_planche170_ff166v-167r_vv0337-0422.jpg) | 170 | **ff. 166v – 167r** | `168v – 169r` | **vv. 337 – 422** |
| **06** | [`06_planche171_ff167v-168r_vv0423-0508.jpg`](planches_doubles_ff162v-177r/06_planche171_ff167v-168r_vv0423-0508.jpg) | 171 | **ff. 167v – 168r** | `169v – 170r` | **vv. 423 – 508** |
| **07** | [`07_planche172_ff168v-169r_vv0509-0589.jpg`](planches_doubles_ff162v-177r/07_planche172_ff168v-169r_vv0509-0589.jpg) | 172 | **ff. 168v – 169r** | `170v – 171r` | **vv. 509 – 589** |
| **08** | [`08_planche173_ff169v-170r_vv0590-0678.jpg`](planches_doubles_ff162v-177r/08_planche173_ff169v-170r_vv0590-0678.jpg) | 173 | **ff. 169v – 170r** | `171v – 172r` | **vv. 590 – 678** |
| **09** | [`09_planche174_ff170v-171r_vv0679-0764.jpg`](planches_doubles_ff162v-177r/09_planche174_ff170v-171r_vv0679-0764.jpg) | 174 | **ff. 170v – 171r** | `172v – 173r` | **vv. 679 – 764** |
| **10** | [`10_planche175_ff171v-172r_vv0765-0837.jpg`](planches_doubles_ff162v-177r/10_planche175_ff171v-172r_vv0765-0837.jpg) | 175 | **ff. 171v – 172r** | `173v – 174r` | **vv. 765 – 837** |
| **11** | [`11_planche176_ff172v-173r_vv0838-0919.jpg`](planches_doubles_ff162v-177r/11_planche176_ff172v-173r_vv0838-0919.jpg) | 176 | **ff. 172v – 173r** | `174v – 175r` | **vv. 838 – 919** |
| **12** | [`12_planche177_ff173v-174r_vv0920-1000.jpg`](planches_doubles_ff162v-177r/12_planche177_ff173v-174r_vv0920-1000.jpg) | 177 | **ff. 173v – 174r** | `175v – 176r` | **vv. 920 – 1000** |
| **13** | [`13_planche178_ff174v-175r_vv1001-1081.jpg`](planches_doubles_ff162v-177r/13_planche178_ff174v-175r_vv1001-1081.jpg) | 178 | **ff. 174v – 175r** | `176v – 177r` | **vv. 1001 – 1081** |
| **14** | [`14_planche179_ff175v-176r_vv1082-1168.jpg`](planches_doubles_ff162v-177r/14_planche179_ff175v-176r_vv1082-1168.jpg) | 179 | **ff. 175v – 176r** | `177v – 178r` | **vv. 1082 – 1168** |
| **15** | [`15_planche180_ff176v-177r_vv1169-1231_fin.jpg`](planches_doubles_ff162v-177r/15_planche180_ff176v-177r_vv1169-1231_fin.jpg) | 180 | **ff. 176v – 177r** | `178v – 179r` | **vv. 1169 – 1231 (Fin)** |

---

### 4.2. Répertoire détaillé des 30 folios individuels (`f. 162v` à `f. 177r`, vv. 1–1231)

Chaque page individuelle (`2011 × 2832 px`) est répertoriée ci-dessous avec son **incipit** (première ligne de la page dans $\text{R}$) et son **explicit** (dernière ligne de la page dans $\text{R}$) :

| N° | Folio (Leeuwen / Classense) | Vers contenus | Incipit (1re ligne du folio) | Explicit (dernière ligne du folio) | Fichier individuel (lien cliquable) |
| :-: | :---: | :---: | :--- | :--- | :--- |
| **01** | **f. 162v** (`164v`) | **Hyp. + vv. 1–42** | `※ ἀριστοφάνους θεσμοφοριάζουσαι —` / `ὦ Ζεῦ· χελιδὼν ἆρά ποτε φανήσεται` | `τῶν μελωδῶν ᾀσμάτων μελοποιῶν` | [`01_f162v_classense164v_vv0001-0042.jpg`](folios_individuels_ff162v-177r/01_f162v_classense164v_vv0001-0042.jpg) |
| **02** | **f. 163r** (`165r`) | **vv. 43–79** | `ἐχέτω· γένος λέγοντος ὁνήσεται αἰθήρ` | `μέλλει δικάζειν· οὔτε γὰρ ἐκκλησία` | [`02_f163r_classense165r_vv0043-0079.jpg`](folios_individuels_ff162v-177r/02_f163r_classense165r_vv0043-0079.jpg) |
| **03** | **f. 163v** (`165v`) | **vv. 80–122** | `ἐπεὶ τρίτη 'στὶ Θεσμοφορίων ἡ μέση` | `ποδὶ παράρυθμ' εὔρυθμα Φρυγίων / διανεύματα Χαρίτων` | [`03_f163v_classense165v_vv0080-0122.jpg`](folios_individuels_ff162v-177r/03_f163v_classense165v_vv0080-0122.jpg) |
| **04** | **f. 164r** (`166r`) | **vv. 123–164** | `σέβομαι Λατώ τ' ἄνασσαν` | `καὶ Φρύνιχος — τοῦτον γὰρ οὖν ἀκήκοας` | [`04_f164r_classense166r_vv0123-0164.jpg`](folios_individuels_ff162v-177r/04_f164r_classense166r_vv0123-0164.jpg) |
| **05** | **f. 164v** (`166v`) | **vv. 165–207** | `αὐτός τε καλὸς ἦν καὶ καλῶς ἠμπέσχετο` | `τί οὖν; ποιήσεις ταῦτα; — μὴ δόκει γε σύ` | [`05_f164v_classense166v_vv0165-0207.jpg`](folios_individuels_ff162v-177r/05_f164v_classense166v_vv0165-0207.jpg) |
| **06** | **f. 165r** (`167r`) | **vv. 208–251** | `ὦ τρισκακοδαίμων, ὡς ἀπόλωλ' Εὐριπίδης` | `λαμβάνετε καὶ χρῆσθ'· οὐ γὰρ φθονῶ` | [`06_f165r_classense167r_vv0208-0251.jpg`](folios_individuels_ff162v-177r/06_f165r_classense167r_vv0208-0251.jpg) |
| **07** | **f. 165v** (`167v`) | **vv. 252–294** | `τί οὖν λάβω; — ὅ τι; τὸν κροκωτὸν πρῶτον ἐνδύου` | `κἀγὼ 'κκλησιάσουσ' ἐν τοῖς ῥήτορσιν` | [`07_f165v_classense167v_vv0252-0294.jpg`](folios_individuels_ff162v-177r/07_f165v_classense167v_vv0252-0294.jpg) |
| **08** | **f. 166r** (`168r`) | **vv. 295–336** | `εὐφημία 'στω · εὐφημία 'στω` | `τῷ τῶν γυναικῶν ἢ 'πικηρυκεύεται` | [`08_f166r_classense168r_vv0295-0336.jpg`](folios_individuels_ff162v-177r/08_f166r_classense168r_vv0295-0336.jpg) |
| **09** | **f. 166v** (`168v`) | **vv. 337–379** | `Εὐριπίδῃ Μήδοις τ' ἐπὶ βλάβῃ τινὶ` | `τίς ἀγορεύειν βούλεται;` | [`09_f166v_classense168v_vv0337-0379.jpg`](folios_individuels_ff162v-177r/09_f166v_classense168v_vv0337-0379.jpg) |
| **10** | **f. 167r** (`169r`) | **vv. 380–422** | `ἐγώ. — περίθου νυν τόνδε πρῶτον πρὶν λέγειν` | `τοῖς ἀνδράσιν` | [`10_f167r_classense169r_vv0380-0422.jpg`](folios_individuels_ff162v-177r/10_f167r_classense169r_vv0380-0422.jpg) |
| **11** | **f. 167v** (`169v`) | **vv. 423–465** | `πρὸ τοῦ μὲν οὖν ἦν ἀλλ' ὑποῖξαι τὴν θύραν` | `πολυπλοκωτέρας` | [`11_f167v_classense169v_vv0423-0465.jpg`](folios_individuels_ff162v-177r/11_f167v_classense169v_vv0423-0465.jpg) |
| **12** | **f. 168r** (`170r`) | **vv. 466–508** | `τὸ μὲν, ὦ γυναῖκες, ὀξυθυμεῖσθαι σφόδρα` | `ἤδη γὰρ ἁνήρ μοι δοκεῖ` | [`12_f168r_classense170r_vv0466-0508.jpg`](folios_individuels_ff162v-177r/12_f168r_classense170r_vv0466-0508.jpg) |
| **13** | **f. 168v** (`170v`) | **vv. 509–550** | `τέξειν· τὸ γὰρ ἦτρον τῆς χύτρας ἐλάκτισεν` | `Φαίδρας / ἁπαξαπάσας` | [`13_f168v_classense170v_vv0509-0550.jpg`](folios_individuels_ff162v-177r/13_f168v_classense170v_vv0509-0550.jpg) |
| **14** | **f. 169r** (`171r`) | **vv. 551–589** | `ἀκούετ', ὦ γυναῖκες, οἷ' εἴρηκεν ἡ πανοῦργος` | `ἐκκλησιάζουσ'` | [`14_f169r_classense171r_vv0551-0589.jpg`](folios_individuels_ff162v-177r/14_f169r_classense171r_vv0551-0589.jpg) |
| **15** | **f. 169v** (`171v`) | **vv. 590–634** | `ἠλίθιος ὅστις τιλλόμενος ἠνείχετο` | `σκάφιον Ξένυλλ' ᾔτησεν· οὐ γὰρ ἦν ἀμίς` | [`15_f169v_classense171v_vv0590-0634.jpg`](folios_individuels_ff162v-177r/15_f169v_classense171v_vv0590-0634.jpg) |
| **16** | **f. 170r** (`172r`) | **vv. 635–678** | `ἀπόδυσον αὐτόν· οὐδὲν ὑγιὲς γὰρ λέγει` | `ταῦτα ποιήσω` | [`16_f170r_classense172r_vv0635-0678.jpg`](folios_individuels_ff162v-177r/16_f170r_classense172r_vv0635-0678.jpg) |
| **17** | **f. 170v** (`172v`) | **vv. 679–720** | `αὐτῶν ὅταν ληφθῇ τις ὅσια δρῶν` | `λόγοισίν τε καὶ ἔργοισιν` | [`17_f170v_classense172v_vv0679-0720.jpg`](folios_individuels_ff162v-177r/17_f170v_classense172v_vv0679-0720.jpg) |
| **18** | **f. 171r** (`173r`) | **vv. 721–764** | `ἀθέοις ἔργοις γὰρ ἀνταμει-` | `καλέσασθαι` | [`18_f171r_classense173r_vv0721-0764.jpg`](folios_individuels_ff162v-177r/18_f171r_classense173r_vv0721-0764.jpg) |
| **19** | **f. 171v** (`173v`) | **vv. 765–799** | `ἄγε δὴ τίς ἔσται μηχανὴ σωτηρίας;` | `παρακύπτωμεν...` | [`19_f171v_classense173v_vv0765-0799.jpg`](folios_individuels_ff162v-177r/19_f171v_classense173v_vv0765-0799.jpg) |
| **20** | **f. 172r** (`174r`) | **vv. 800–837** | `ἡμεῖς μὲν οὖν ἐσμὲν χείρους` | `δίδοσθαι Τηνίοισι` | [`20_f172r_classense174r_vv0800-0837.jpg`](folios_individuels_ff162v-177r/20_f172r_classense174r_vv0800-0837.jpg) |
| **21** | **f. 172v** (`174v`) | **vv. 838–875** | `ὑστέραν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην` | `ἐπεὶ τέθνηκε Πρωτέας ἔτη δέκα` | [`21_f172v_classense174v_vv0838-0875.jpg`](folios_individuels_ff162v-177r/21_f172v_classense174v_vv0838-0875.jpg) |
| **22** | **f. 173r** (`175r`) | **vv. 876–919** | `ποίαν δὲ χώραν εἰσεκέλσαμεν σκάφει;` | `τὴν Τυνδάρειον παῖδ' ἐπὶ Σπάρτην ἄγειν;` | [`22_f173r_classense175r_vv0876-0919.jpg`](folios_individuels_ff162v-177r/22_f173r_classense175r_vv0876-0919.jpg) |
| **23** | **f. 173v** (`175v`) | **vv. 920–958** | `οἴμ' ὡς πανοῦργος καὐτὸς εἶναί μοι δοκεῖς` | `κυκλοῦσαν ὄμμα χρὴ χοροῦ κατάστασιν` | [`23_f173v_classense175v_vv0920-0958.jpg`](folios_individuels_ff162v-177r/23_f173v_classense175v_vv0920-0958.jpg) |
| **24** | **f. 174r** (`176r`) | **vv. 959–1000** | `μέλπε καὶ γέραιρε φωνῇ πᾶσα χορομανεῖ τρόπῳ` | `πρὸς τὴν αἰθρίαν` | [`24_f174r_classense176r_vv0959-1000.jpg`](folios_individuels_ff162v-177r/24_f174r_classense176r_vv0959-1000.jpg) |
| **25** | **f. 174v** (`176v`) | **vv. 1001–1043** | `ὦ τοξόθ', ἱκετεύω σε, μή μ' ἱκετεῦσι σύ` | `ὃς ἐμὲ κροκόεντ' ἐνέδυσεν` | [`25_f174v_classense176v_vv1001-1043.jpg`](folios_individuels_ff162v-177r/25_f174v_classense176v_vv1001-1043.jpg) |
| **26** | **f. 175r** (`177r`) | **vv. 1044–1081** | `ἐπὶ δὲ τοῖσδε τόδ' ἀνέπεμψεν` | `οἴμωζε — οἴμωζε` | [`26_f175r_classense177r_vv1044-1081.jpg`](folios_individuels_ff162v-177r/26_f175r_classense177r_vv1044-1081.jpg) |
| **27** | **f. 175v** (`177v`) | **vv. 1082–1127** | `ὀτότυζε — ὀτότυζε / οὖτος τί λαλῖς;` | `τὸ κεπαλή σ' ἄρα` | [`27_f175v_classense177v_vv1082-1127.jpg`](folios_individuels_ff162v-177r/27_f175v_classense177v_vv1082-1127.jpg) |
| **28** | **f. 176r** (`178r`) | **vv. 1128–1168** | `αἰαῖ· τί δράσω; πρὸς τίνας στρεφθῶ λόγους;` | `ἃ νῦν ὑποικουρεῖτε τοῖσιν ἀνδράσιν` | [`28_f176r_classense178r_vv1128-1168.jpg`](folios_individuels_ff162v-177r/28_f176r_classense178r_vv1128-1168.jpg) |
| **29** | **f. 176v** (`178v`) | **vv. 1169–1210** | `ἀπὸ τῆς στρατιᾶς παροῦσιν ὑμῶν διαβαλῶ` | `ὦ γρᾴδι', ὡς καρίεντό σοι τὸ τυγάτριον` | [`29_f176v_classense178v_vv1169-1210.jpg`](folios_individuels_ff162v-177r/29_f176v_classense178v_vv1169-1210.jpg) |
| **30** | **f. 177r** (`179r`) | **vv. 1211–1231 (Fin)** | `κοὐ δύσκολον, ἀλλὰ πρᾶον· ποῦ τὸ γρᾴδιο;` | `τούτων χάριν ἀνταποδοίτην.` (+ *Hyp. Eccl.*) | [`30_f177r_classense179r_vv1211-1231_fin.jpg`](folios_individuels_ff162v-177r/30_f177r_classense179r_vv1211-1231_fin.jpg) |

---

## 5. Bibliographie de référence sur le *Codex Ravennas 429*

* **Allen, Thomas W.** (1896), « On the Composition of Some Greek Manuscripts, II. The Ravenna Aristophanes », *Journal of Philology* 24, p. 300–326.
* **Austin, Colin & Olson, S. Douglas** (2004), *Aristophanes: Thesmophoriazusae*, edited with introduction and commentary, Oxford, Oxford University Press (notamment p. lxxviii–xcviii : « The Transmission of the Text »).
* **Billerbeck, Margarethe** (2013), « Le *Codex Ravennas 429* d'Aristophane », dans C. Brockmann et al., *Handschriften- und Textforschung heute*, Wiesbaden.
* **Diller, Aubrey** (1953), « The Lost *Codex Ravennas* of Aristophanes » / « The History of the *Codex Ravennas* », *Transactions of the American Philological Association*.
* **Irigoin, Jean** (1959), « Pour une étude des centres de copie byzantins (II) : le scriptorium d'Éphrem », *Scriptorium* 13, p. 177–209.
* **Leeuwen, Johannes van** (1904), *Codex Aristophaneus Ravennas 137, 4, A phototypice editus*, Lugduni Batavorum, A. W. Sijthoff.
* **Martin, Albert** (1882), *Les scolies du manuscrit d'Aristophane à Ravenne : étude et collation*, Paris, Ernest Thorin (Bibliothèque des Écoles françaises d'Athènes et de Rome, fasc. 27).
* **Mioni, Elpidio** (1965), *Catalogo di manoscritti greci esistenti nelle biblioteche italiane*, vol. II, Roma, Poligrafico dello Stato (notice codicologique officielle du *Ravennas 429*).
* **Prato, Carlo** (2001), *Aristofane : Le Donne alle Tesmoforie*, trad. D. Del Corno, Milano, Fondazione Lorenzo Valla / Mondadori.
* **Regtuit, Remco F.** (2007), *Scholia in Aristophanis Thesmophoriazusas et Ecclesiazusas* (*Scholia in Aristophanem*, Pars III, Fasc. 2/3), Groningen, Egbert Forsten.
* **Velsen, Adolf von** (1883), *Aristophanis Thesmophoriazusae*, Lipsiae, B. G. Teubner.
* **Wilson, Nigel G.** (2007), *Aristophanis Fabulae*, Tomus II, Oxford, Clarendon Press (OCT).
