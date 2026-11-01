#!/usr/bin/env python3
"""Vérification adversariale du chapitre 4 (interventions) : mesures indépendantes.

Protocole distinct de celui du chapitre (outils/graphologie/encres_interventions.py) :
- pixels de trait = fond local (flou gaussien 15 px de la luminance) - luminance > seuil,
  sans condition de teinte ;
- absorbances par canal rapportées au fond local du même canal ; rapports G/R et B/R
  (médianes) ;
- comparaison par classes de CONTRASTE (fond - luminance : 25-40, 40-55, 55-70, 70-90,
  90-130), et non par classes d'absorbance rouge ;
- deux témoins : (1) écrits sur grattage d'autres mains (effet du support gratté) ;
  (2) petits signes isolés de T (effet de taille : sous-échantillonnage de la chrominance
  JPEG) ; plus la variabilité locale de T (fenêtres de 60 px le long des lignes).

Usage : python3 outils/graphologie/verif_ch4.py  (écrit
ravennas/graphologie/chapitres/4_verification_mesures.json ; durée : quelques minutes).
"""
import os, json, colorsys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

R = '/workspaces/Thesmophories'
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
PAGES = {f.split('_')[1]: os.path.join(SRC, f) for f in os.listdir(SRC) if f.endswith('.jpg')}
_c, _s = {}, {}


def page(f):
    if f not in _c:
        _c[f] = Image.open(PAGES[f]).convert('RGB')
    return _c[f]


def seg(f):
    if f not in _s:
        _s[f] = json.load(open(os.path.join(R, 'ravennas', 'segmentation', f + '.json')))
    return _s[f]


def pix(f, box, seuil=25, marge=40, flou=15):
    x0, y0, x1, y1 = box
    im = page(f); W, H = im.size
    X0, Y0, X1, Y1 = max(0, x0 - marge), max(0, y0 - marge), min(W, x1 + marge), min(H, y1 + marge)
    c = np.asarray(im.crop((X0, Y0, X1, Y1))).astype(float)
    L = 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]
    Lb = np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(flou))).astype(float)
    F = np.stack([np.asarray(Image.fromarray(c[..., i].astype(np.uint8)).filter(ImageFilter.GaussianBlur(flou))).astype(float)
                  for i in range(3)], -1)
    sl = (slice(y0 - Y0, y1 - Y0), slice(x0 - X0, x1 - X0))
    d = (Lb - L)[sl]; m = d > seuil
    rgb = c[sl][m]; fb = F[sl][m]
    A = -np.log10(np.clip(rgb, 1, 255) / np.clip(fb, 1, 255))
    s = np.array([colorsys.rgb_to_hsv(*(p / 255))[1] for p in rgb]) if len(rgb) else np.zeros(0)
    return dict(A=A, d=d[m], s=s)


def cat(Ps):
    return dict(A=np.concatenate([p['A'] for p in Ps]), d=np.concatenate([p['d'] for p in Ps]),
                s=np.concatenate([p['s'] for p in Ps]))


def med(P):
    A = P['A']; ok = A[:, 0] > 0.03
    if ok.sum() < 4:
        return None
    return dict(n=int(len(P['d'])), contraste=round(float(np.median(P['d'])), 1),
                GR=round(float(np.median(A[ok, 1] / A[ok, 0])), 2), BR=round(float(np.median(A[ok, 2] / A[ok, 0])), 2))


CL = [(25, 40), (40, 55), (55, 70), (70, 90), (90, 130)]


def classes(P):
    out = []
    for a, b in CL:
        k = (P['d'] >= a) & (P['d'] < b) & (P['A'][:, 0] > 0.03)
        if k.sum() < 6:
            out.append(None); continue
        A = P['A'][k]
        out.append((float(np.median(A[:, 1] / A[:, 0])), float(np.median(A[:, 2] / A[:, 0]))))
    return out


def delta(Pi, Pt):
    dg, db = [], []
    for a, b in zip(classes(Pi), classes(Pt)):
        if a and b:
            dg.append(a[0] - b[0]); db.append(a[1] - b[1])
    if not dg:
        return None
    return dict(dGR=round(float(np.mean(dg)), 2), dBR=round(float(np.mean(db)), 2), classes=len(dg))


# 1. Écrits sur grattage : groupe Rⁿ et témoins (boîte de l'intervention ; boîtes de T voisin)
GRATTAGES = [
    ('Rn', 646, 'ἥκει πάλιν', 'f170r', (790, 825, 1045, 880), [(260, 825, 760, 880), (250, 860, 1080, 925)]),
    ('Rn', 493, 'κιν', 'f168r', (836, 1530, 908, 1570), [(660, 1525, 830, 1575), (915, 1525, 1060, 1575)]),
    ('Rn', 874, 'ι de ποίου', 'f172v', (830, 2104, 848, 2134), [(760, 2100, 828, 2140), (870, 2100, 1100, 2140)]),
    ('Rn', 939, 'υ de ἀποδύσαντα', 'f173v', (1455, 1302, 1485, 1330), [(1100, 1295, 1450, 1335), (1490, 1295, 1560, 1335)]),
    ('témoin', '57b', 'αι de λαικάζει (S2)', 'f163r', (420, 1240, 448, 1268), [(258, 1235, 415, 1275), (450, 1235, 555, 1275)]),
    ('témoin', 370, '-εῖν de παραστατεῖν (S2)', 'f166v', (1405, 1780, 1460, 1815), [(933, 1775, 1400, 1820)]),
    ('témoin', 468, 'εῖ de ἐπιζεῖν', 'f168r', (750, 478, 790, 512), [(600, 475, 745, 520), (795, 475, 1000, 520)]),
    ('témoin', 935, 'υ de ὀλίγου (S2)', 'f173v', (886, 1078, 916, 1106), [(766, 1075, 880, 1115), (925, 1075, 1240, 1115)]),
]

# 2. Accents et petits signes (mesure brute ; rang parmi les petits signes isolés de T de la page)
ACCENTS = [
    ('Rn', 54, 'grave du 2e τάδε', 'f163r', (784, 1047, 801, 1066)),
    ('T', 54, 'grave du 1er τάδε', 'f163r', (411, 1057, 431, 1073)),
    ('T', 54, 'point de T après τορνεύει (même ligne)', 'f163r', (667, 1067, 685, 1083)),
    ('Rn', 650, 'aigu de ἐγώ', 'f170r', (1089, 948, 1106, 972)),
    ('T', 650, 'grave de ἐγὼ (à côté)', 'f170r', (1070, 948, 1087, 966)),
    ('Rn?', 820, 'grave mince de εἰσὶν', 'f172r', (608, 1568, 630, 1588)),
    ('T', 820, 'aigu de T de εἰσίν (à côté)', 'f172r', (585, 1574, 602, 1594)),
    ('Rn', 1149, 'esprit rude de ἅλσος', 'f176r', (534, 1366, 556, 1386)),
    ('T', 1149, 'aigu de ἅλσος (à côté)', 'f176r', (550, 1356, 570, 1378)),
]

# 3. Main de 1516 : corrections et marques (mesure brute + T de la ligne)
M1516 = [
    (443, 'ὀλίγων : boucle droite (ajoutée)', 'f167v', (898, 1226, 912, 1252), 18),
    (443, 'ὀλίγων : boucle gauche (T)', 'f167v', (882, 1228, 897, 1252), 18),
    (443, 'T, l. 21', 'f167v', [(640, 1225, 860, 1265), (935, 1225, 1300, 1265)], 25),
    (803, 'croix : branche haut-droite (barre)', 'f172r', (287, 534, 303, 549), 15),
    (803, 'croix : branche haut-gauche (grave de T)', 'f172r', (268, 536, 284, 550), 15),
    (803, 'T, l. 5', 'f172r', [(330, 560, 1060, 615)], 25),
    (806, 'grave de πρὸς', 'f172r', (232, 768, 256, 796), 12),
    (806, 'T, l. 10', 'f172r', [(270, 795, 1060, 850)], 25),
    (1097, 'grave de καὶ', 'f175v', (980, 1012, 999, 1028), 18),
    (1097, 'T, l. 16', 'f175v', [(789, 1028, 975, 1062), (1010, 1028, 1400, 1062)], 25),
    (1180, 'grave de κατὰ', 'f176v', (1418, 857, 1440, 878), 15),
    (1180, 'grave de τὸ', 'f176v', (1458, 865, 1480, 885), 15),
    (1180, 'T, l. 12', 'f176v', [(1100, 880, 1420, 905), (1490, 880, 1700, 905)], 25),
    (1191, 'σκ : boucle du σ', 'f176v', (1293, 1372, 1312, 1396), 20),
    (1191, 'σκ : masse du κ', 'f176v', (1318, 1372, 1333, 1399), 20),
    (1191, '3e ο (T, non corrigé)', 'f176v', (1343, 1376, 1363, 1398), 20),
    (1191, 'T, l. 24', 'f176v', [(733, 1370, 1250, 1405), (1380, 1370, 1600, 1405)], 25),
    ('c 13', 'repère de la page c 13 (f174v)', 'f174v', (1722, 954, 1792, 966), 12),
    ('c 13', 'scholie de S2 voisine', 'f174v', (1435, 965, 1790, 1060), 18),
]

# 4. Vers suppléés (vv. 33, 169) et voisinage
SUPPL = [
    (33, '(a) μῶν', 'f162v', (1490, 1805, 1560, 1835)),
    (33, '(a) ὁ δασυπώγων sans le δ', 'f162v', (1625, 1805, 1810, 1840)),
    (33, '(a) δ de δασυπώγων', 'f162v', (1595, 1795, 1625, 1835)),
    (33, '(b) εὐ', 'f162v', (1480, 1850, 1525, 1880)),
    (33, '(b) οὐχ ἑόρακας πώ-', 'f162v', (1530, 1845, 1800, 1885)),
    (33, '(c) -ποτε', 'f162v', (1590, 1890, 1680, 1925)),
    (33, 'texte de T, l. 33', 'f162v', (740, 1765, 1400, 1820)),
    (33, 'scholie voisine', 'f162v', (1560, 1700, 1820, 1790)),
    (169, 'tiret initial', 'f164v', (130, 575, 200, 592)),
    (169, 'ὁ δ᾽ αὖ', 'f164v', (220, 560, 300, 600)),
    (169, 'ξενο-', 'f164v', (305, 555, 390, 605)),
    (169, '-κλῆς ὢν', 'f164v', (390, 560, 500, 605)),
    (169, 'κακὸς κακῶς', 'f164v', (500, 560, 700, 605)),
    (169, 'ποεῖ (2e ligne)', 'f164v', (560, 610, 680, 645)),
    (169, 'scholie voisine (ξενοκλέης…)', 'f164v', (240, 505, 640, 530)),
    (169, 'texte de T', 'f164v', (240, 650, 1200, 700)),
]

# 5. Paragraphoi barrées : haste et trait horizontal
PARAGRAPHOI = [
    ('f165r', 232, 'haste', (168, 1383, 178, 1394)), ('f165r', 232, 'paragraphos', (145, 1393, 163, 1401)),
    ('f165r', 234, 'haste', (170, 1480, 180, 1490)), ('f165r', 234, 'paragraphos', (145, 1475, 165, 1484)),
    ('f165r', 234, 'sigle orangé voisin', (166, 1420, 200, 1440)),
    ('f169v', 608, 'haste', (705, 1030, 716, 1062)), ('f169v', 608, 'paragraphos', (718, 1040, 735, 1050)),
    ('f169v', 608, 'sigle κλ orangé voisin', (660, 1035, 700, 1060)),
    ('f176v', 1194, 'haste', (746, 1480, 758, 1492)), ('f176v', 1194, 'paragraphos', (733, 1490, 745, 1504)),
    ('f176v', 1204, 'haste', (760, 1878, 772, 1890)), ('f176v', 1204, 'paragraphos', (735, 1895, 755, 1905)),
    ('f176v', 1184, 'haste', (748, 1048, 760, 1060)), ('f176v', 1184, 'paragraphos', (728, 1058, 746, 1072)),
]

# 6. Additions tardives et μέντοι
AUTRES = [
    (60, 'κατα suscrit', 'f163r', (585, 1340, 665, 1368), [(310, 1365, 580, 1410), (670, 1365, 912, 1410)], 18),
    (306, 'compendium de καί suscrit', 'f166r', (703, 890, 723, 918), [(350, 905, 690, 945), (760, 905, 1000, 945)], 14),
    (630, 'μέντοι en marge', 'f169v', (600, 1958, 700, 2000), [(760, 1960, 1490, 2000)], 25),
]


def petits_signes(f, amin=15, amax=90, seuil=25):
    """Petits signes isolés (accents, points) de la colonne : population de référence de T."""
    im = page(f); c = np.asarray(im).astype(float)
    L = 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]
    Lb = np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(15))).astype(float)
    m = (Lb - L) > seuil
    x0, y0, x1, y1 = seg(f)['colonne']['boite']
    sub = np.zeros_like(m); sub[y0:y1, x0:x1] = m[y0:y1, x0:x1]
    lab, n = ndi.label(sub, structure=np.ones((3, 3)))
    areas = ndi.sum(sub, lab, index=np.arange(1, n + 1)); res = []
    for i, (sl, a) in enumerate(zip(ndi.find_objects(lab), areas)):
        if not (amin <= a <= amax):
            continue
        if sl[0].stop - sl[0].start > 22 or sl[1].stop - sl[1].start > 22:
            continue
        Y0, Y1, X0, X1 = sl[0].start - 4, sl[0].stop + 4, sl[1].start - 4, sl[1].stop + 4
        if (sub[Y0:Y1, X0:X1] & (lab[Y0:Y1, X0:X1] != i + 1)).sum() > 3:
            continue
        r = med(pix(f, (X0 + 2, Y0 + 2, X1 - 2, Y1 - 2), seuil=seuil))
        if r and r['n'] >= 8:
            res.append(r)
    return res


def variabilite_T(f):
    """Écart de fenêtres de 60 px de T au reste de leur ligne (une ligne sur trois)."""
    out = []
    for l in seg(f)['lignes']:
        if l['type'] != 'texte' or l['index'] % 3:
            continue
        x0, y0, x1, y1 = l['texte']
        if x1 - x0 < 400:
            continue
        for xs in range(x0 + 40, x1 - 100, 150):
            Pw = pix(f, (xs, y0, xs + 60, y1))
            if len(Pw['d']) < 120:
                continue
            d = delta(Pw, cat([pix(f, (x0, y0, xs - 10, y1)), pix(f, (xs + 70, y0, x1, y1))]))
            if d and d['classes'] >= 3:
                out.append(d)
    dB = np.array([o['dBR'] for o in out]); dG = np.array([o['dGR'] for o in out])
    return dict(fenetres=len(out), dBR_p5=round(float(np.percentile(dB, 5)), 2), dBR_min=round(float(dB.min()), 2),
                dGR_p5=round(float(np.percentile(dG, 5)), 2), dGR_min=round(float(dG.min()), 2))


def contours(f, box, seuil=18, flou=15, limite=2.45):
    """Part des pixels de bord (masque moins son érosion) dont B/R < limite, et du cœur."""
    x0, y0, x1, y1 = box; m = 40
    c = np.asarray(page(f).crop((x0 - m, y0 - m, x1 + m, y1 + m))).astype(float)
    L = 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]
    Lb = np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(flou))).astype(float)
    F = [np.asarray(Image.fromarray(c[..., i].astype(np.uint8)).filter(ImageFilter.GaussianBlur(flou))).astype(float) for i in range(3)]
    A = [-np.log10(np.clip(c[..., i], 1, 255) / np.clip(F[i], 1, 255)) for i in range(3)]
    mask = ((Lb - L) > seuil)[m:-m, m:-m]
    br = np.where(A[0] > 0.02, A[2] / np.maximum(A[0], 1e-3), 0)[m:-m, m:-m]
    coeur = ndi.binary_erosion(mask, iterations=1); bord = mask & ~coeur
    return dict(bord_brun=round(float(np.mean(br[bord] < limite)), 2), coeur_brun=round(float(np.mean(br[coeur] < limite)), 2),
                BR_coeur=round(float(np.median(br[coeur])), 2))


CONTOURS = [
    (1207, 'κη^δ de forme S2, orangé (G l\'a)', 'f176v', (675, 1980, 775, 2065)),
    ('l. 17', 'σκ orangé de 1516', 'f176v', (755, 1118, 800, 1150)),
    ('l. 19', 'σκ orangé de 1516', 'f176v', (755, 1175, 815, 1200)),
    (608, 'κλ orangé de 1516', 'f169v', (655, 1030, 705, 1065)),
]
ZONES_939 = [(1100, 1295, 1440, 1335), (1490, 1295, 1600, 1335), (1400, 1250, 1500, 1290),
             (1500, 1250, 1660, 1290), (1400, 1340, 1500, 1380), (1500, 1340, 1660, 1380)]


def main():
    res = {}
    U = pix('f173v', (1455, 1302, 1485, 1330))
    res['v939_contre_six_zones_de_T'] = [dict(zone=z, delta=delta(U, pix('f173v', z))) for z in ZONES_939]
    res['contours'] = [dict(v=v, objet=lab, page=f, **contours(f, b)) for v, lab, f, b in CONTOURS]
    res['grattages'] = []
    for g, v, lab, f, b, rb in GRATTAGES:
        Pi, Pt = pix(f, b), cat([pix(f, x) for x in rb])
        res['grattages'].append(dict(groupe=g, v=v, objet=lab, page=f, mesure=med(Pi), T=med(Pt), delta=delta(Pi, Pt)))
    pages = sorted({a[3] for a in ACCENTS} | {'f168r', 'f172v', 'f173v'})
    pop = {f: petits_signes(f) for f in pages}
    res['petits_signes_T'] = {}
    for f in pages:
        N = np.array([x['n'] for x in pop[f]]); BR = np.array([x['BR'] for x in pop[f]])
        k = (N >= 15) & (N < 30)
        res['petits_signes_T'][f] = dict(nombre=len(N), BR_med_15_30px=round(float(np.median(BR[k])), 2),
                                         part_BR_inf_1_9_15_30px=round(float(np.mean(BR[k] < 1.9)), 2))
    res['accents'] = []
    for g, v, lab, f, b in ACCENTS:
        r = med(pix(f, b))
        comp = [x for x in pop[f] if abs(x['n'] - r['n']) <= 12 and abs(x['contraste'] - r['contraste']) <= 20]
        GR = np.array([x['GR'] for x in comp]); BR = np.array([x['BR'] for x in comp])
        res['accents'].append(dict(groupe=g, v=v, objet=lab, page=f, mesure=r, comparables=len(comp),
                                   rang_GR=round(float(np.mean(GR <= r['GR'])), 2), rang_BR=round(float(np.mean(BR <= r['BR'])), 2)))
    res['variabilite_T'] = {f: variabilite_T(f) for f in ['f163r', 'f168r', 'f170r', 'f172r', 'f172v', 'f173v', 'f176r']}
    res['1516'] = []
    for v, lab, f, b, s in M1516:
        P = cat([pix(f, x, seuil=s) for x in b]) if isinstance(b, list) else pix(f, b, seuil=s)
        res['1516'].append(dict(v=v, objet=lab, page=f, mesure=med(P)))
    res['vers_suppleés'] = [dict(v=v, objet=lab, page=f, mesure=med(pix(f, b, seuil=22))) for v, lab, f, b in SUPPL]
    res['paragraphoi'] = [dict(page=f, v=v, objet=lab, mesure=med(pix(f, b, seuil=15))) for f, v, lab, b in PARAGRAPHOI]
    res['autres'] = []
    for v, lab, f, b, rb, s in AUTRES:
        Pi, Pt = pix(f, b, seuil=s), cat([pix(f, x) for x in rb])
        res['autres'].append(dict(v=v, objet=lab, page=f, mesure=med(Pi), T=med(Pt), delta=delta(Pi, Pt)))
    out = os.path.join(R, 'ravennas', 'graphologie', 'chapitres', '4_verification_mesures.json')
    json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
