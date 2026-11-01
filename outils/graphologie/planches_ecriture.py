#!/usr/bin/env python3
"""Spécimens et planches du chapitre 2 de l'étude graphologique de R
(« L'écriture du copiste : alphabet, ligatures, abréviations du texte »).

Entrée : ravennas/graphologie/planches/specimens_ch2.tsv
  (id, folio, x0, y0, x1, y1 en px de l'image pleine résolution, ligne, vers, lettre, légende).
Sorties :
  - ravennas/graphologie/specimens/ch2/<id>.png : découpe agrandie (LANCZOS), ≤ 600 px de large ;
  - ravennas/graphologie/planches/ch2_*.png : planches (mosaïques légendées) ;
  - .travail/ch2/controle_*.png : planches de contrôle (identifiants), avec --controle.
Usage : python3 outils/graphologie/planches_ecriture.py [--controle] [--seulement id1,id2]
"""
import argparse, csv, glob, os
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
TSV = os.path.join(R, 'ravennas', 'graphologie', 'planches', 'specimens_ch2.tsv')
SPEC = os.path.join(R, 'ravennas', 'graphologie', 'specimens', 'ch2')
PLA = os.path.join(R, 'ravennas', 'graphologie', 'planches')
CTRL = os.path.join(R, '.travail', 'ch2')
FD = '/home/codespace/.local/share/fonts/'
F_TIT = ImageFont.truetype(FD + 'LibertinusSerif-Semibold.otf', 30)
F_ROW = ImageFont.truetype(FD + 'LibertinusSerif-Semibold.otf', 24)
F_LEG = ImageFont.truetype(FD + 'LibertinusSerif-Regular.otf', 17)
F_REF = ImageFont.truetype(FD + 'LibertinusSerif-Italic.otf', 15)
F_NOTE = ImageFont.truetype(FD + 'LibertinusSerif-Regular.otf', 16)
MM = 0.116  # mm par pixel de l'image source

_pages = {}


def page(folio):
    if folio not in _pages:
        f = [p for p in glob.glob(os.path.join(SRC, '*.jpg')) if f'_{folio}_' in os.path.basename(p)][0]
        _pages[folio] = Image.open(f).convert('RGB')
    return _pages[folio]


def lire():
    with open(TSV, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh, delimiter='\t'))
    d = {}
    for r in rows:
        for k in ('x0', 'y0', 'x1', 'y1'):
            r[k] = int(r[k])
        d[r['id']] = r
    return rows, d


def decoupe(r, echelle):
    c = page(r['folio']).crop((r['x0'], r['y0'], r['x1'], r['y1']))
    w, h = c.size
    return c.resize((max(1, int(w * echelle)), max(1, int(h * echelle))), Image.LANCZOS)


def ref(r):
    f = r['folio'][1:]
    s = f"f. {f}, l. {r['ligne']}"
    if r['vers']:
        s += f", v. {r['vers']}"
    return s


def specimens(rows):
    os.makedirs(SPEC, exist_ok=True)
    for r in rows:
        w = r['x1'] - r['x0']
        e = min(4.0, 600 / w)
        decoupe(r, e).save(os.path.join(SPEC, r['id'] + '.png'))


def controle(rows, n=24):
    os.makedirs(CTRL, exist_ok=True)
    for k in range(0, len(rows), n):
        tiles = []
        for r in rows[k:k + n]:
            c = decoupe(r, 2.5)
            t = Image.new('RGB', (max(c.size[0], 150), c.size[1] + 20), 'white')
            t.paste(c, (0, 20))
            ImageDraw.Draw(t).text((2, 1), r['id'], fill='red', font=F_REF)
            tiles.append(t)
        W = 1500
        x = y = rowh = 0
        pos = []
        for t in tiles:
            if x + t.size[0] > W:
                x = 0; y += rowh + 6; rowh = 0
            pos.append((x, y)); x += t.size[0] + 6; rowh = max(rowh, t.size[1])
        out = Image.new('RGB', (W, y + rowh), (180, 180, 180))
        for t, p in zip(tiles, pos):
            out.paste(t, p)
        out.save(os.path.join(CTRL, f'controle_{k // n + 1:02d}.png'))
        print(os.path.join(CTRL, f'controle_{k // n + 1:02d}.png'))


def vignette(r, H):
    """Spécimen mis à la hauteur H (px), légendé dessous (lettre en gras, légende, référence)."""
    h0 = r['y1'] - r['y0']
    c = decoupe(r, H / h0)
    leg = r['legende']
    lignes = []
    mots = leg.split(' ')
    cur = ''
    for m in mots:
        t = (cur + ' ' + m).strip()
        if F_LEG.getlength(t) > max(c.size[0], 170) and cur:
            lignes.append(cur); cur = m
        else:
            cur = t
    lignes.append(cur)
    wl = max([F_LEG.getlength(l) for l in lignes] + [F_REF.getlength(ref(r))])
    W = int(max(c.size[0], wl)) + 8
    Ht = c.size[1] + 8 + 20 * len(lignes) + 20
    t = Image.new('RGB', (W, Ht), 'white')
    t.paste(c, ((W - c.size[0]) // 2, 0))
    d = ImageDraw.Draw(t)
    y = c.size[1] + 6
    for l in lignes:
        d.text(((W - F_LEG.getlength(l)) / 2, y), l, fill=(20, 20, 20), font=F_LEG); y += 20
    rr = ref(r)
    d.text(((W - F_REF.getlength(rr)) / 2, y), rr, fill=(90, 60, 30), font=F_REF)
    return t


def planche(nom, titre, rangs, d, H=120, W=1800, note=None):
    """rangs : liste de (titre du rang, [ids])."""
    blocs = []
    for tit, ids in rangs:
        vs = [vignette(d[i], H) for i in ids if i in d]
        blocs.append((tit, vs))
    marge = 30
    y = 80
    places = []
    for tit, vs in blocs:
        places.append(('T', tit, (marge, y)))
        y += 34
        x = marge + 10
        hmax = 0
        for v in vs:
            if x + v.size[0] > W - marge:
                x = marge + 10; y += hmax + 14; hmax = 0
            places.append(('V', v, (x, y)))
            x += v.size[0] + 16
            hmax = max(hmax, v.size[1])
        y += hmax + 22
    if note:
        y += 10
    out = Image.new('RGB', (W, y + (30 * len(note) if note else 0) + 30), (250, 247, 240))
    dr = ImageDraw.Draw(out)
    dr.text((marge, 22), titre, fill=(60, 30, 10), font=F_TIT)
    for kind, obj, (x, yy) in places:
        if kind == 'T':
            dr.text((x, yy), obj, fill=(120, 40, 20), font=F_ROW)
            dr.line([(x, yy + 30), (W - marge, yy + 30)], fill=(200, 180, 150), width=1)
        else:
            out.paste(obj, (x, yy))
            dr.rectangle([x - 1, yy - 1, x + obj.size[0], yy + obj.size[1]], outline=(210, 200, 185))
    if note:
        yy = y
        for l in note:
            dr.text((marge, yy), l, fill=(60, 60, 60), font=F_NOTE); yy += 26
    os.makedirs(PLA, exist_ok=True)
    fn = os.path.join(PLA, nom + '.png')
    out.save(fn, optimize=True)
    print(fn, out.size)


ECH = ("Échelle : chaque découpe est ramenée à la même hauteur (120 px) ; corps des lettres de T ≈ 14–16 px "
       "(≈ 1,6–1,9 mm) sur l'original. Images : Ravenne, Classense, ms. 429 (pleine résolution).")


def planches(d):
    planche('ch2_pl1_abecedaire_1', 'Planche 1 — Abécédaire de T (α–λ) : allographes', [
        ('α', ['a_dia', 'a_pnoas']),
        ('β', ['b_u1', 'b_u2', 'b_u3', 'b_k', 'b_corr']),
        ('γ', ['g_v', 'g_ge', 'g_G', 'g_gi']),
        ('δ', ['d_1', 'd_2', 'L_di']),
        ('ε', ['e_6', 'e_E', 'p_varpi2']),
        ('ζ', ['z_1', 'z_2', 'z_3', 'z_4']),
        ('η', ['h_h', 'h_H1', 'h_H2', 'h_H3', 'L_demeter']),
        ('θ', ['t_1', 'L_et2']),
        ('ι', ['i_j1', 'i_j2']),
        ('κ', ['k_lu', 'k_lc', 'k_2']),
        ('λ', ['l_1', 'l_2', 'll_X1', 'll_X2', 'll_obl']),
    ], d, note=[ECH])
    planche('ch2_pl2_abecedaire_2', 'Planche 2 — Abécédaire de T (μ–ω) : allographes', [
        ('μ', ['m_1', 'm_2', 'm_3']),
        ('ν', ['n_1', 'n_2', 'n_3', 'n_N1', 'n_N2', 'n_ON', 'n_q', 'n_x']),
        ('ξ', ['x_1', 'x_2', 'x_3', 'x_4']),
        ('ο', ['o_O', 'o_plein']),
        ('π', ['p_varpi', 'p_varpi2', 'p_Pi']),
        ('ρ', ['r_q']),
        ('σ', ['s_fin', 's_bar', 's_init']),
        ('τ', ['tau_1', 'tau_g', 'tau_b']),
        ('υ', ['u_init']),
        ('φ', ['f_1', 'f_2', 'f_3']),
        ('χ ψ', ['c_1', 'y_1', 'y_2', 'y_3']),
        ('ω', ['w_1']),
    ], d, note=[ECH])
    planche('ch2_pl3_ligatures', 'Planche 3 — Ligatures et groupes de T', [
        ('ει', ['L_ei_t', 'L_ei_q1', 'L_ei_q2', 'L_ei_xi', 'L_ei_4', 'L_ei_v', 'L_oktiras']),
        ('στ, σπ, σχ', ['L_st_a1', 'L_st_a2', 'L_st_a3', 'L_strephei', 'L_sp1', 'L_sp2', 'L_sch']),
        ('ττ, γγ, νν, λλ', ['L_tt1', 'L_tt2', 'L_tt4', 'L_gg1', 'L_gg2', 'L_nn']),
        ('υν, ου, -ος', ['L_un', 'L_ou', 'L_os1', 'L_os2', 'L_os3', 'L_os4']),
        ('ε + consonne, δι, τι', ['L_peri', 'L_et1', 'L_et2', 'L_ete_patera', 'x_3', 'L_di', 'L_ti']),
    ], d, note=[ECH])
    planche('ch2_pl4_abreviations_signes', 'Planche 4 — Abréviations du texte et signes de lecture de T', [
        ('καί (ϗ)', ['A_kai1', 'A_kai2', 'A_kai3', 'A_kai4', 'A_kaizeta', 'L_ei_kai']),
        ('Finales et mots abrégés', ['A_on', 'A_ai1', 'A_ai2', 'A_pater', 'A_einai', 'A_men']),
        ('Esprits, accents, tréma', ['D_spir1', 'D_spir2', 'D_circ1', 'D_circ2', 'D_accV', 'D_trema1', 'D_trema2']),
        ('ι adscrit, remplissage, encre', ['D_iota1', 'D_iota2', 'D_fill', 's_bar', 'D_ink']),
    ], d, note=[ECH])


def planche_ambigues(d):
    planche('ch2_pl5_formes_ambigues', 'Planche 5 — Formes ambiguës de T : ce qui se confond', [
        ('ν (un arceau, pointe montante) / μ (deux arceaux)', ['n_2', 'm_2', 'n_1', 'm_1', 'n_3', 'm_3']),
        ('π en « ϖ » / ω ; υν en « ω »', ['p_varpi', 'w_1', 'L_un', 'L_sp2']),
        ('β en « u » / κ / υ', ['b_u2', 'b_u1', 'k_lu', 'k_lc', 'b_k']),
        ('ζ (deux lobes, « 3 ») / ξ (barre de tête, zigzag) : même page', ['z_3', 'x_4', 'z_2', 'x_2', 'x_1']),
        ('ει en « q » / η ; ϗ / ζ', ['L_ei_q2', 'h_h', 'L_ei_xi', 'A_kaizeta', 'L_ei_kai']),
        ('στ en « α » / α', ['L_st_a2', 'a_dia', 'L_st_a1', 'a_pnoas']),
        ('γ en « v » / ν ; Γ / τ', ['g_v', 'n_3', 'g_G', 'tau_1']),
        ('θ ouvert / ετ lié / δ', ['t_1', 'L_et2', 'L_et1', 'd_2']),
        ('λλ croisés / χ ; ψ en croix', ['ll_X1', 'c_1', 'y_1', 'y_2']),
        ('Η / Ν onciaux ; -ος en « © »', ['h_H2', 'n_N2', 'n_N1', 'L_os2', 'L_os4']),
    ], d, note=[ECH, "Chaque rang réunit des formes de T que les inventaires de page signalent comme sources de mélecture ; voir le chapitre 2, § 8."])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--controle', action='store_true')
    ap.add_argument('--seulement', default='')
    ap.add_argument('--sans-planches', action='store_true')
    a = ap.parse_args()
    rows, d = lire()
    if a.seulement:
        keep = set(a.seulement.split(','))
        rows = [r for r in rows if r['id'] in keep]
    if a.controle:
        controle(rows)
        return
    specimens(rows)
    if not a.sans_planches:
        planches(d)
        planche_ambigues(d)


if __name__ == '__main__':
    main()
