#!/usr/bin/env python3
"""Planches du chapitre 3 de l'étude graphologique (scholies, gloses, abréviations).

Chaque vignette est découpée dans l'image pleine résolution de la page
(dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/), agrandie
(PIL, LANCZOS) et légendée ; les boîtes sont en pixels de l'image de la page.
Usage : python3 outils/graphologie/planches_chap3.py [nom_planche ...]
Sortie : ravennas/graphologie/planches/ch3_*.png
"""
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
OUT = os.path.join(R, 'ravennas', 'graphologie', 'planches')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

_pages = {}
def page(fol):
    if fol not in _pages:
        _pages[fol] = Image.open(glob.glob(os.path.join(SRC, f'*_{fol}_*.jpg'))[0]).convert('RGB')
    return _pages[fol]

def vignette(fol, box, h=None, sc=None, maxw=1360):
    im = page(fol).crop(tuple(box))
    w0, h0 = im.size
    s = sc if sc else (h / h0 if h else 2.0)
    if w0 * s > maxw:
        s = maxw / w0
    return im.resize((max(1, int(w0 * s)), max(1, int(h0 * s))), Image.LANCZOS)

def planche(titre, items, nom, W=1400, marge=16, gap=14):
    f = ImageFont.truetype(FONT, 15); fb = ImageFont.truetype(FONTB, 20)
    tiles = []
    for it in items:
        fol, box, cap = it[0], it[1], it[2]
        kw = it[3] if len(it) > 3 else {}
        v = vignette(fol, box, **kw)
        lignes = cap.split('\n')
        th = 19 * len(lignes) + 4
        t = Image.new('RGB', (max(v.width, 10), v.height + th), 'white')
        d = ImageDraw.Draw(t)
        for k, l in enumerate(lignes):
            d.text((0, 19 * k), l, font=f, fill=(20, 20, 20))
        t.paste(v, (0, th))
        tiles.append(t)
    # mise en rangées
    rows, cur, cw = [], [], 0
    for t in tiles:
        if cur and cw + gap + t.width > W - 2 * marge:
            rows.append(cur); cur, cw = [], 0
        cur.append(t); cw += (gap if cw else 0) + t.width
    if cur: rows.append(cur)
    H = marge + 34 + sum(max(t.height for t in r) + gap for r in rows) + marge
    P = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(P)
    d.text((marge, marge), titre, font=fb, fill=(0, 0, 0))
    y = marge + 34
    for r in rows:
        x = marge
        for t in r:
            P.paste(t, (x, y)); x += t.width + gap
        y += max(t.height for t in r) + gap
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, nom)
    P.save(p, quality=88, optimize=True)
    return p, P.size

PLANCHES = {}

PLANCHES['ch3_pl1_ecritures.jpg'] = ("Ch. 3, planche 1 — Les écritures des notes marginales (R, Thesmophories)", [
    ('f162v', (230, 172, 1790, 330), "a. f. 162v, marge sup. : notice sur la pièce et « προλογίζ(ει) μνησίλοχ(ος) κηδεστὴς εὐριπίδου » (minuscule)", {'sc': 0.86}),
    ('f162v', (320, 815, 720, 905), "b. f. 162v, marge ext., l. 9-10 : lemme oncial ΑΚΟΥΕΙΝ + minuscule (S2)", {'sc': 2.4}),
    ('f162v', (1585, 1655, 1800, 1795), "c. f. 162v, marge int., vv. 30-32 :\nἐπειδὴ οὐ πάλαι… (minuscule ronde)", {'sc': 2.4}),
    ('f162v', (700, 1595, 1300, 1650), "d. f. 162v, l. 30, texte de T (comparaison avec c)", {'sc': 1.6}),
    ('f162v', (1380, 1790, 1815, 1915), "e. f. 162v, v. 33 suppléé par S2 (grande minuscule penchée)", {'sc': 1.5}),
    ('f175v', (240, 2150, 1010, 2240), "f. f. 175v, marge inf. : vv. 1102-1103 suppléés (minuscule de S2), renvoi +:", {'sc': 1.4}),
    ('f162v', (600, 2238, 1480, 2312), "g. f. 162v, marge inf. : semi-onciale inclinée de S2 (scholie au v. 21)", {'sc': 1.4}),
    ('f174v', (1460, 1325, 1800, 1405), "h. f. 174v, marge ext. : semi-onciale plus droite\n(module ordinaire, 12-13 px)", {'sc': 2.0}),
    ('f171r', (40, 600, 330, 660), "i. f. 171r, marge int. : petites majuscules\ndroites (πρὸ(ς) τ(ὰς) γυναῖκας)", {'sc': 2.2}),
    ('f171r', (10, 995, 330, 1045), "j. f. 171r : glose ὦ μέθυσοι", {'sc': 2.2}),
    ('f164r', (600, 1080, 720, 1112), "k. f. 164r : glose ζωνάριον\n(minuscule, Ζ capital)", {'sc': 3.0}),
    ('f176r', (110, 1538, 195, 1578), "l. f. 176r : glose ὅπου\n(petite majuscule, S2 probable)", {'sc': 3.5}),
])

PLANCHES['ch3_pl2_abreviations.jpg'] = ("Ch. 3, planche 2 — Abréviations et signes tachygraphiques des scholies (S2)", [
    ('f164v', (1150, 165, 1490, 218), "1. αἰσχρὸς ϗ(αὶ) τηλεκλείδης ἡσιόδ(οις),\nf. 164v, marge sup.", {'sc': 2.6}),
    ('f171v', (196, 640, 750, 700), "2. ϗ = καί en « Ις » (κ de S2 en deux pièces + queue) :\nαὐτοῦ ϗ ἀπαγγεῖλαι ; π̄ρ̄ᾱ = π(ατέ)ρα ; τ̆ = τ(ὸν), f. 171v", {'sc': 2.0}),
    ('f165v', (245, 535, 640, 600), "3. δ(έ) en « ʒ » isolé et ἐστί (·/· réduit) :\nπόσθιον δ(ὲ) (ἐστι) τὸ αἰδοῖον, f. 165v", {'sc': 2.4}),
    ('f165v', (280, 1490, 680, 1630), "4. -(αι) en « ʒ » attaché au τ ou au θ écrits :\nἐκκυκλεῖτ(αι), γίνεσθ(αι), τίθετ(αι), f. 165v", {'sc': 1.9}),
    ('f177r', (40, 555, 200, 605), "5. παρακελεύετ(αι),\nf. 177r", {'sc': 3.0}),
    ('f166v', (290, 1905, 750, 2015), "6. ·/· = ἐστί (deux fois), δ(ὲ) en ʒ, τιν(ός) :\nἐπιστάτις ·/· ἡ τιμόκλεια· ἀρχὴ δ(ὲ) τίς ·/·…, f. 166v", {'sc': 2.4}),
    ('f173v', (250, 1040, 740, 1125), "7. ·//· = εἰσί(ν) (λινοποιοί εἰσιν), ÷ final ;\nà droite, paragraphos barrée (non S2), f. 173v", {'sc': 2.2}),
    ('f168r', (40, 1185, 200, 1245), "8. λ̸ = λείπει :\nλ(είπει) τὸ ἔφη, f. 168r", {'sc': 3.0}),
    ('f175r', (780, 1610, 1050, 1680), "9. même signe : λ(είπει) μέλλουσα τυχεῖν,\nf. 175r (et non « ἤγουν »)", {'sc': 2.6}),
    ('f170r', (35, 590, 220, 665), "10. ἀν^τ τ̆ = ἀντὶ τοῦ\n(στεῖρα), f. 170r", {'sc': 2.6}),
    ('f177r', (1100, 975, 1410, 1015), "11. ποίαν ὁδ(ὸν) φη(σὶ) : φ barré + η suscrit,\nὁδ' (suspension accentuée), f. 177r", {'sc': 2.6}),
    ('f164r', (35, 1180, 200, 1230), "12. γρ(άφεται) σύ τ' αὐτό(ς),\nf. 164r", {'sc': 3.0}),
    ('f177r', (5, 735, 160, 880), "13. ὁ χ^ο(ρὸς) ἐμπαίζ^ει…\nεὐρι^π(ίδης), f. 177r", {'sc': 2.2}),
    ('f166r', (1235, 1755, 1435, 1800), "14. ἢ τ^ου ἀπόλλων(ος) : -ος réduit\nà un point ; ΛΛ en « Μ », f. 166r", {'sc': 3.0}),
    ('f164v', (1612, 1640, 1775, 1688), "15. τ^ȣ = τοῦ :\nἐὰν τ(οῦ)το, f. 164v", {'sc': 3.0}),
    ('f164v', (235, 855, 700, 985), "16. ϗ(αὶ), π^ε = περί, suspensions ἔλεγ(ον), σοφιστ(άς) ; ÷ final, f. 164v", {'sc': 2.0}),
])

PLANCHES['ch3_pl3_renvois.jpg'] = ("Ch. 3, planche 3 — Délimitation des notes, renvois, et faux renvois", [
    ('f164r', (700, 515, 1010, 575), "1a. f. 164r, fin du v. 127 : renvoi ∈", {'sc': 2.2}),
    ('f164r', (900, 615, 1380, 665), "1b. même signe en tête de la scholie (∈ πάλιν…)", {'sc': 2.2}),
    ('f169r', (480, 990, 760, 1060), "2a. f. 169r, interligne au-dessus de θεὼ (v. 566) : ·×·", {'sc': 2.4}),
    ('f169r', (1180, 360, 1560, 440), "2b. même signe en tête de la scholie déplacée en haut de page", {'sc': 2.2}),
    ('f175v', (1500, 1180, 1800, 1245), "3. f. 175v, fin du v. 1101 : —+:— (vv. 1102-1103 omis ;\nencre orangée, main indéterminée)", {'sc': 2.4}),
    ('f167v', (238, 618, 575, 656), "4. f. 167v : tiret initial, ϗ en « Ις », clôture « :– » (aspect de ÷) : ταράττειν ϗ κινεῖν", {'sc': 2.6}),
    ('f163v', (1290, 1045, 1560, 1120), "5a. FAUX RENVOI : f. 163v, l. 17, οὑκκυκλούμεν + Ͼ = -ος de T", {'sc': 2.4}),
    ('f164r', (760, 2005, 1010, 2075), "5b. comparaison : f. 164r, l. 40, τήι + Ͼ = τήιος (T)", {'sc': 2.4}),
])

PLANCHES['ch3_pl4_pieges.jpg'] = ("Ch. 3, planche 4 — Pièges de lecture propres aux scholies", [
    ('f169r', (1180, 400, 1560, 440), "1. ΛΛ lié = « Μ » : ἀλλὰ μὰ ταῖν θεαῖν, f. 169r", {'sc': 2.6}),
    ('f171r', (40, 600, 330, 660), "2. Ν à diagonale presque\nhorizontale = « Η » (ναῖκας), f. 171r", {'sc': 2.4}),
    ('f171v', (600, 905, 900, 955), "3. fin de scholie « …εὐρι^π ÷ » contre la colonne,\nprise pour un sigle (f. 171v, v. 776)", {'sc': 2.4}),
    ('f165r', (1140, 1290, 1620, 1460), "4. réactif bleu-vert sur les fins de ligne ; ·/· = ἐστί\naprès δ(έ) (μύζειν δ(έ) ἐστι…), f. 165r", {'sc': 1.9}),
    ('f175r', (1075, 795, 1360, 865), "5. λ(είπει) en tête, passage à la minuscule,\nν suscrit (δαιμόν^ν^ων), f. 175r", {'sc': 2.6}),
    ('f167r', (1190, 350, 1620, 445), "6. θ à barre débordante (στεφανοῦσθαι, περίθου) :\nlettre, non compendium, f. 167r", {'sc': 2.2}),
])

if __name__ == '__main__':
    noms = sys.argv[1:] or list(PLANCHES)
    for n in noms:
        t, it = PLANCHES[n]
        print(planche(t, it, n))
