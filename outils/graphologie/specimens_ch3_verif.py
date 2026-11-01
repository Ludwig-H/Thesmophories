#!/usr/bin/env python3
"""Spécimens de la vérification adversariale du chapitre 3 (scholies), § 11.

Chaque spécimen est une petite découpe (≤ 600 px de large) de l'image pleine
résolution de la page (dossier_ravennas_thesmophories/folios_individuels_ff162v-177r/),
agrandie (PIL, LANCZOS) ; plusieurs bandes peuvent être empilées à la même
échelle. Les boîtes sont en pixels de l'image de la page (1 px ≈ 0,116 mm).
Source « fac1904 » : fac-similé phototypique de 1904 (ravennas_1904_bnf/).
Usage : python3 outils/graphologie/specimens_ch3_verif.py
Sortie : ravennas/graphologie/planches/ch3_verif/*.png et specimens_ch3_verif.tsv
"""
import glob, os
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
FAC = os.path.join(R, 'ravennas_1904_bnf', 'Ravennas_1904_f162v_Thesmophoriazusae_vv1-42.png')
OUT = os.path.join(R, 'ravennas', 'graphologie', 'planches', 'ch3_verif')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
MAXW = 600

_pages = {}
def page(fol):
    if fol not in _pages:
        if fol == 'fac1904':
            _pages[fol] = Image.open(FAC).convert('RGB')
        else:
            _pages[fol] = Image.open(glob.glob(os.path.join(SRC, f'*_{fol}_*.jpg'))[0]).convert('RGB')
    return _pages[fol]

# nom : (échelle, [(folio, boîte, légende), ...], vérification)
SPECIMENS = {
    'v01_f162v_trois_minuscules.png': (1.5, [
        ('f162v', (330, 645, 710, 690), "162v marge ext. : minuscule (a) de S2"),
        ('f162v', (1585, 1660, 1800, 1750), "162v marge int. : minuscule ronde (b)"),
        ('f162v', (1470, 1795, 1800, 1840), "162v : v. 33 suppléé (S2)"),
        ('f162v', (760, 1645, 1140, 1700), "162v l. 30 : T"),
    ], 'V1'),
    'v01_f162v_pi_en_varpi.png': (1.8, [
        ('f162v', (560, 510, 725, 550), "(a) εὐριϖίδου"),
        ('f162v', (1480, 1845, 1800, 1920), "v. 33 : …ϖώ|ποτε"),
        ('f162v', (1585, 1660, 1800, 1705), "(b) ἐπειδὴ οὐ ϖάλαι"),
    ], 'V1'),
    'v03_f162v_mnesai_couleur_1904.png': (1.8, [
        ('f162v', (395, 1512, 720, 1565), "162v l. 26 : πρόσεχε· ἀν^τ τ^ου μνῆσαι"),
        ('fac1904', (380, 783, 530, 810), "fac-similé de 1904 (×3,5)", 3.5),
    ], 'V3'),
    'v07_finale_os_163v_164r.png': (1.6, [
        ('f163v', (1280, 1050, 1640, 1135), "163v l. 17 : -ος de T (faux renvoi)"),
        ('f164r', (760, 2005, 1060, 2080), "164r l. 40 : τήιος"),
    ], 'V7'),
    'v08_f167r_stephanousthai.png': (2.5, [
        ('f167r', (1250, 385, 1480, 420), "167r l. 2 : στεφανοῦσθαι (σ écrit, θ à barre)"),
    ], 'V8'),
    'v09_f164r_renvois.png': (3.0, [
        ('f164r', (900, 525, 990, 560), "fin l. 5 : ∈"),
        ('f164r', (915, 622, 1060, 655), "l. 7 : ∈ πάλιν"),
        ('f164r', (370, 905, 440, 950), "interligne 13/14"),
        ('f164r', (1065, 1218, 1200, 1255), "l. 21 : ✕ λυκουρ-"),
    ], 'V9'),
    'v10_f176r_opou.png': (4.0, [
        ('f176r', (105, 1530, 200, 1582), "176r l. 28 : ὅπου"),
    ], 'V10'),
    'v13_compendium_ai.png': (1.3, [
        ('f165r', (1050, 1912, 1485, 1950), "165r l. 37 : καλεῖτ(αι)"),
        ('f165v', (1595, 1572, 1720, 1604), "165v int. : μιμεῖτ(αι)", 4.0),
        ('f166r', (1050, 1675, 1300, 1715), "166r l. 31 : πᾶσαν δ(ὲ) κίνησιν", 2.3),
    ], 'V13'),
    'v14_f173v_eisi_syntaxis.png': (3.0, [
        ('f173v', (560, 1095, 700, 1145), "173v l. 17 : λινοποιοί ·//·"),
        ('f173v', (590, 1400, 760, 1455), "173v l. 25 : ἀττικὴ δ(ὲ) ἡ σύντ(αξις)"),
    ], 'V14'),
    'v16_f175v_renvois_orange.png': (2.5, [
        ('f175v', (1550, 1190, 1760, 1240), "175v fin l. 20 : —+:— (orangé)"),
        ('f175v', (245, 2140, 330, 2200), "marge inf. : +:"),
    ], 'V16'),
    'v19_f176v_ked_orange.png': (3.0, [
        ('f176v', (670, 1980, 800, 2092), "176v l. 40–41 : ΚΗ orangé ; εὐρι^π brun"),
    ], 'V19'),
    'v21_f168r_sch506.png': (1.0, [
        ('f168r', (1000, 2082, 1565, 2186), "168r Σ 506 : B/R 2,3 (g.) → 2,9–3,3 (dr.)"),
    ], 'V21'),
    'v22_modules_meme_echelle.png': (1.6, [
        ('f174v', (1460, 1330, 1800, 1400), "174v (planche 1, h)"),
        ('f168r', (1000, 2082, 1340, 2140), "168r Σ 506"),
        ('f166r', (1050, 1650, 1400, 1712), "166r Σ 324"),
    ], 'V22'),
}

def faire(nom, sc, bandes):
    f = ImageFont.truetype(FONT, 13)
    tiles = []
    for b in bandes:
        fol, box, leg = b[0], b[1], b[2]
        s = b[3] if len(b) > 3 else sc
        im = page(fol).crop(box)
        w, h = int(im.width * s), int(im.height * s)
        if w > MAXW:
            h = int(h * MAXW / w); w = MAXW
        tiles.append((im.resize((w, h), Image.LANCZOS), leg))
    W = max(t.width for t, _ in tiles)
    H = sum(t.height + 18 for t, _ in tiles)
    P = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(P); y = 0
    for t, leg in tiles:
        d.text((2, y + 2), leg, font=f, fill=(20, 20, 20)); y += 18
        P.paste(t, (0, y)); y += t.height
    os.makedirs(OUT, exist_ok=True)
    P.save(os.path.join(OUT, nom), optimize=True)
    return P.size

if __name__ == '__main__':
    lignes = ['fichier\tverification\tfolio\tboite\tlegende']
    for nom, (sc, bandes, v) in SPECIMENS.items():
        print(nom, faire(nom, sc, bandes))
        for b in bandes:
            lignes.append(f'{nom}\t{v}\t{b[0]}\t{list(b[1])}\t{b[2]}')
    with open(os.path.join(OUT, 'specimens_ch3_verif.tsv'), 'w') as fh:
        fh.write('\n'.join(lignes) + '\n')
