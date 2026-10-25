#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur reproductible des planches didactiques de déchiffrement paléographique
du Codex Ravennas 429 (Aristophane, Thesmophories, ff. 162v-177r).

Ce script produit les planches illustrées dans `exemples_dechiffrement/` à partir
des fac-similés haute résolution (`folios_individuels_ff162v-177r/` et
`specimens_paleographiques/`) avec coordonnées vérifiées au pixel près et
placement anti-collision / anti-rognage des étiquettes pédagogiques.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLIOS_DIR = os.path.join(BASE_DIR, "folios_individuels_ff162v-177r")
SPECS_DIR = os.path.join(BASE_DIR, "specimens_paleographiques")
OUT_DIR = os.path.join(BASE_DIR, "exemples_dechiffrement")

os.makedirs(OUT_DIR, exist_ok=True)

# Chemins des sources
F162V = os.path.join(FOLIOS_DIR, "01_f162v_classense164v_vv0001-0042.jpg")
F163V = os.path.join(FOLIOS_DIR, "03_f163v_classense165v_vv0080-0122.jpg")
F175V = os.path.join(FOLIOS_DIR, "27_f175v_classense177v_vv1082-1127.jpg")
F176V = os.path.join(FOLIOS_DIR, "29_f176v_classense178v_vv1169-1210.jpg")

SPEC01 = os.path.join(SPECS_DIR, "01_f162v_hypothesis_et_titre_semi_onciale.jpg")
SPEC02 = os.path.join(SPECS_DIR, "02_f162v_vv28-35_transposition_rasura_marge_v33_bebinekas.jpg")
SPEC03 = os.path.join(SPECS_DIR, "03_f163r_vv48-62_pramos_aspidas_kata_supralineaire.jpg")
SPEC04 = os.path.join(SPECS_DIR, "04_f163v_v80_et_parepigraphe1_minyrysmos.jpg")
SPEC05 = os.path.join(SPECS_DIR, "05_f164r_parepigraphe2_ololyzei_et_vv160-164.jpg")
SPEC06 = os.path.join(SPECS_DIR, "06_f165v_parepigraphe3_ololyzousi_et_choiron_v289.jpg")
SPEC07 = os.path.join(SPECS_DIR, "07_f166r_v295_rasura_keryx_et_gloses_intruses.jpg")
SPEC08 = os.path.join(SPECS_DIR, "08_f168r_vv488-507_kybda_lekometba_v500_booe.jpg")
SPEC09 = os.path.join(SPECS_DIR, "09_f170r_vv636-670_tachygraphie_et_rasura_hapasin.jpg")
SPEC10 = os.path.join(SPECS_DIR, "10_f172r_vv814-830_pothountas_kanon_skiadeion.jpg")
SPEC11 = os.path.join(SPECS_DIR, "11_f172v_vv838-854_hypereuge_oupoli_kyrkanas.jpg")
SPEC12 = os.path.join(SPECS_DIR, "12_f173r_vv894-912_bauza_aphyon_et_restauration.jpg")
SPEC13 = os.path.join(SPECS_DIR, "13_f175r_vv1055-1081_echo_epikokkastria_stomyllomene.jpg")
SPEC14 = os.path.join(SPECS_DIR, "14_f175v_vv1082-1108_echo_bicolonne_prote_et_marge_vv1102-1103.jpg")
SPEC15 = os.path.join(SPECS_DIR, "15_f176v_parepigraphe4_six_rasurae_et_main_boninus.jpg")
SPEC16 = os.path.join(SPECS_DIR, "16_f177r_exodos_koronis_et_hypothesis_ecclesiazusae.jpg")

# Polices
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SERIF_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SANS_OBLIQUE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_font(path, size, text=""):
    if any(ch in text for ch in ("☉", "☩", "⁘")):
        if "Bold" in path:
            return ImageFont.truetype(FONT_SANS_BOLD, size)
        return ImageFont.truetype(FONT_SANS, size)
    return ImageFont.truetype(path, size)

# Palette graphique
COL_BG = (250, 247, 240)
COL_HEADER = (115, 25, 25)
COL_GOLD = (175, 140, 80)
COL_CARD_BG = (255, 253, 249)
COL_CARD_BORDER = (165, 140, 95)
COL_BOX_BG = (242, 245, 250)
COL_BOX_BORDER = (195, 205, 220)
COL_FOOTER_BG = (248, 242, 228)
COL_TEXT = (30, 30, 30)
COL_MUTED = (95, 85, 75)
COL_DIPLO = (15, 55, 120)
COL_EDIT = (25, 100, 45)

STYLE_COLORS = {
    "red": {
        "outline": (200, 28, 28),
        "fill": (255, 242, 242),
        "text": (160, 15, 15),
    },
    "blue": {
        "outline": (25, 85, 175),
        "fill": (240, 247, 255),
        "text": (15, 55, 135),
    },
    "green": {
        "outline": (25, 130, 65),
        "fill": (240, 255, 245),
        "text": (15, 95, 40),
    },
}

_IMAGE_CACHE = {}

def load_source(path):
    if path not in _IMAGE_CACHE:
        _IMAGE_CACHE[path] = Image.open(path).convert("RGB")
    return _IMAGE_CACHE[path]

def text_size(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]

def wrap_text(draw, text, font, max_w):
    words = text.split()
    if not words:
        return []
    lines = []
    cur = words[0]
    for w in words[1:]:
        test = cur + " " + w
        tw, _ = text_size(draw, test, font)
        if tw <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines

def overlap_area(r1, r2):
    x1 = max(r1[0], r2[0])
    y1 = max(r1[1], r2[1])
    x2 = min(r1[2], r2[2])
    y2 = min(r1[3], r2[3])
    if x2 > x1 and y2 > y1:
        return (x2 - x1) * (y2 - y1)
    return 0

def render_crop_panel(src_path, crop_box, annotations, target_w, min_vpad_native=22, max_h=None):
    """
    Découpe `crop_box = (x1, y1, x2, y2)` dans `src_path`, ajuste automatiquement
    la marge verticale pour laisser respirer les étiquettes, redimensionne à `target_w`
    et place les cadres et étiquettes sans aucun rognage ni chevauchement.
    Chaque élément de `annotations` est `(bx1, by1, bx2, by2, label, color_key)`.
    """
    im = load_source(src_path)
    cx1, cy1, cx2, cy2 = crop_box

    # S'assurer que toutes les boîtes sont contenues avec une marge pour les badges
    if annotations:
        min_by1 = min(a[1] for a in annotations)
        max_by2 = max(a[3] for a in annotations)
        min_bx1 = min(a[0] for a in annotations)
        max_bx2 = max(a[2] for a in annotations)
        cx1 = min(cx1, min_bx1 - 18)
        cx2 = max(cx2, max_bx2 + 18)
        cy1 = min(cy1, min_by1 - min_vpad_native)
        cy2 = max(cy2, max_by2 + min_vpad_native)

    cx1 = max(0, int(cx1))
    cy1 = max(0, int(cy1))
    cx2 = min(im.width, int(cx2))
    cy2 = min(im.height, int(cy2))

    sub = im.crop((cx1, cy1, cx2, cy2))
    scale = target_w / float(sub.width)
    target_h = int(round(sub.height * scale))

    if max_h is not None and target_h > max_h:
        scale = max_h / float(sub.height)
        target_h = max_h
        resized_w = int(round(sub.width * scale))
        resized = sub.resize((resized_w, target_h), Image.Resampling.LANCZOS)
        # Fond parchemin moyen
        panel = Image.new("RGB", (target_w, target_h), (235, 224, 198))
        offset_x = (target_w - resized_w) // 2
        panel.paste(resized, (offset_x, 0))
    else:
        offset_x = 0
        panel = sub.resize((target_w, target_h), Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(panel)
    f_badge = get_font(FONT_SANS_BOLD, 12)

    scaled_boxes = []
    for bx1, by1, bx2, by2, label, ckey in annotations:
        sx1 = int(round((bx1 - cx1) * scale)) + offset_x
        sy1 = int(round((by1 - cy1) * scale))
        sx2 = int(round((bx2 - cx1) * scale)) + offset_x
        sy2 = int(round((by2 - cy1) * scale))
        sx1 = max(2, min(target_w - 4, sx1))
        sy1 = max(2, min(target_h - 4, sy1))
        sx2 = max(sx1 + 6, min(target_w - 2, sx2))
        sy2 = max(sy1 + 6, min(target_h - 2, sy2))
        scaled_boxes.append((sx1, sy1, sx2, sy2, label, ckey))

    # Dessiner d'abord les rectangles d'encadrement
    for sx1, sy1, sx2, sy2, label, ckey in scaled_boxes:
        st = STYLE_COLORS.get(ckey, STYLE_COLORS["red"])
        draw.rectangle([sx1, sy1, sx2, sy2], outline=st["outline"], width=3)

    # Placer ensuite les étiquettes avec anti-collision et anti-rognage strict
    placed_badges = []
    box_rects = [(b[0], b[1], b[2], b[3]) for b in scaled_boxes]

    for sx1, sy1, sx2, sy2, label, ckey in scaled_boxes:
        if not label:
            continue
        st = STYLE_COLORS.get(ckey, STYLE_COLORS["red"])
        tw, th = text_size(draw, label, f_badge)
        bw = tw + 12
        bh = th + 6
        bw = min(bw, target_w - 6)

        def clamp_x(x):
            return max(3, min(x, target_w - bw - 3))

        def clamp_y(y):
            return max(3, min(y, target_h - bh - 3))

        candidates = [
            # Au-dessus aligné à gauche ou à droite ou centré
            (clamp_x(sx1), sy1 - bh - 3),
            (clamp_x(sx2 - bw), sy1 - bh - 3),
            (clamp_x((sx1 + sx2 - bw) // 2), sy1 - bh - 3),
            # En dessous aligné à gauche ou à droite ou centré
            (clamp_x(sx1), sy2 + 3),
            (clamp_x(sx2 - bw), sy2 + 3),
            (clamp_x((sx1 + sx2 - bw) // 2), sy2 + 3),
            # À gauche ou à droite
            (sx1 - bw - 4, clamp_y(sy1)),
            (sx2 + 4, clamp_y(sy1)),
            # Plus haut / plus bas
            (clamp_x(sx1), sy1 - bh - 22),
            (clamp_x(sx1), sy2 + 22),
            # Bords haut/bas du panneau
            (clamp_x(sx1), 3),
            (clamp_x(sx1), target_h - bh - 3),
            (clamp_x(sx2 - bw), 3),
            (clamp_x(sx2 - bw), target_h - bh - 3),
        ]

        best_cand = None
        best_score = 1e18
        for cx_cand, cy_cand in candidates:
            in_bounds = (2 <= cx_cand and cx_cand + bw <= target_w - 2 and
                         2 <= cy_cand and cy_cand + bh <= target_h - 2)
            rx = clamp_x(cx_cand)
            ry = clamp_y(cy_cand)
            rect = (rx, ry, rx + bw, ry + bh)

            # Pénalités de chevauchement
            badge_ov = sum(overlap_area(rect, pb) for pb in placed_badges)
            box_ov = sum(overlap_area(rect, br) for br in box_rects)
            dist = abs(rx - sx1) * 0.4 + min(abs(ry + bh - sy1), abs(ry - sy2)) * 0.8
            oob_pen = 0 if in_bounds else 2000

            score = badge_ov * 500 + box_ov * 80 + oob_pen + dist
            if score < best_score:
                best_score = score
                best_cand = rect

        lx1, ly1, lx2, ly2 = best_cand
        placed_badges.append(best_cand)

        # Ligne de rappel si l'étiquette est distante de plus de 8px de la boîte
        bx_mid = (sx1 + sx2) // 2
        by_attach = sy1 if (ly2 <= sy1 + 4) else (sy2 if ly1 >= sy2 - 4 else (sy1 + sy2) // 2)
        lx_mid = max(lx1 + 4, min(lx2 - 4, bx_mid))
        ly_attach = ly2 if (ly2 <= sy1 + 4) else (ly1 if ly1 >= sy2 - 4 else (ly1 + ly2) // 2)
        if abs(ly_attach - by_attach) > 6 or abs(lx_mid - bx_mid) > 20:
            draw.line([(lx_mid, ly_attach), (bx_mid, by_attach)], fill=st["outline"], width=2)

        draw.rectangle([lx1, ly1, lx2, ly2], fill=st["fill"], outline=st["outline"], width=2)
        draw.text((lx1 + 6, ly1 + 2), label, fill=st["text"], font=f_badge)

    # Bordure fine autour de l'extrait
    draw.rectangle([0, 0, target_w - 1, target_h - 1], outline=COL_CARD_BORDER, width=1)
    return panel


def draw_header(im, draw, width, title, subtitle):
    draw.rectangle([0, 0, width, 108], fill=COL_HEADER)
    draw.rectangle([0, 108, width, 112], fill=COL_GOLD)
    f_title = get_font(FONT_SERIF_BOLD, 24, title)
    f_sub = get_font(FONT_SANS, 15, subtitle)
    draw.text((28, 22), title, fill=(255, 252, 242), font=f_title)
    draw.text((28, 64), subtitle, fill=(242, 222, 185), font=f_sub)


def draw_footer(draw, width, y_top, title_label, text):
    f_lbl = get_font(FONT_SANS_BOLD, 14)
    f_txt = get_font(FONT_SANS, 14)
    lbl_str = f"{title_label} : "
    lw, _ = text_size(draw, lbl_str, f_lbl)
    lines = wrap_text(draw, text, f_txt, width - 56 - lw - 24)
    box_h = max(48, 20 + len(lines) * 20)
    draw.rectangle([28, y_top, width - 28, y_top + box_h], fill=COL_FOOTER_BG, outline=COL_GOLD, width=2)
    draw.rectangle([28, y_top, 36, y_top + box_h], fill=COL_HEADER)
    draw.text((48, y_top + 13), lbl_str, fill=COL_HEADER, font=f_lbl)
    for i, ln in enumerate(lines):
        draw.text((48 + lw, y_top + 13 + i * 20), ln, fill=COL_TEXT, font=f_txt)
    return y_top + box_h + 22


def render_card_image(card, card_w):
    """
    Construit l'image d'une carte standard (titre, sous-titre, extrait annoté,
    lecture diplomatique, édition & sens, analyse) de largeur `card_w`.
    """
    pad = 14
    inner_w = card_w - 2 * pad
    f_title = get_font(FONT_SERIF_BOLD, 16, card["title"])
    f_sub = get_font(FONT_SERIF_ITALIC, 13, card.get("subtitle", ""))
    f_bold = get_font(FONT_SANS_BOLD, 13)
    f_reg = get_font(FONT_SANS, 13)

    dummy = Image.new("RGB", (10, 10))
    ddraw = ImageDraw.Draw(dummy)

    title_lines = wrap_text(ddraw, card["title"], f_title, inner_w)
    sub_lines = wrap_text(ddraw, card.get("subtitle", ""), f_sub, inner_w) if card.get("subtitle") else []

    crop_panel = render_crop_panel(
        card["src"],
        card["crop"],
        card.get("boxes", []),
        target_w=inner_w,
        min_vpad_native=card.get("vpad", 22),
        max_h=card.get("max_h", 260),
    )

    diplo_lbl = "Lecture diplomatique : "
    edit_lbl = "Édition & sens : "
    dlw, _ = text_size(ddraw, diplo_lbl, f_bold)
    elw, _ = text_size(ddraw, edit_lbl, f_bold)

    diplo_lines = wrap_text(ddraw, card.get("diplo", ""), f_bold, inner_w - 20 - dlw)
    edit_lines = wrap_text(ddraw, card.get("edit", ""), f_reg, inner_w - 20 - elw)

    ana_lbl = "Analyse : "
    alw, _ = text_size(ddraw, ana_lbl, f_bold)
    ana_lines = wrap_text(ddraw, card.get("analyse", ""), f_reg, inner_w - alw - 4)

    y = 6 + 10
    y += len(title_lines) * 21
    if sub_lines:
        y += 2 + len(sub_lines) * 18
    y += 8 + crop_panel.height + 10

    reading_box_h = 12 + max(1, len(diplo_lines)) * 19 + 4 + max(1, len(edit_lines)) * 19
    y += reading_box_h + 10
    y += max(1, len(ana_lines)) * 19 + 14

    card_im = Image.new("RGB", (card_w, y), COL_CARD_BG)
    cdraw = ImageDraw.Draw(card_im)
    cdraw.rectangle([0, 0, card_w - 1, y - 1], outline=COL_CARD_BORDER, width=1)
    cdraw.rectangle([0, 0, card_w - 1, 6], fill=COL_HEADER)

    cy = 14
    for ln in title_lines:
        cdraw.text((pad, cy), ln, fill=COL_HEADER, font=f_title)
        cy += 21
    if sub_lines:
        cy += 2
        for ln in sub_lines:
            cdraw.text((pad, cy), ln, fill=COL_MUTED, font=f_sub)
            cy += 18

    cy += 8
    card_im.paste(crop_panel, (pad, cy))
    cy += crop_panel.height + 10

    # Encadré Lecture diplomatique + Édition
    cdraw.rectangle([pad, cy, pad + inner_w, cy + reading_box_h], fill=COL_BOX_BG, outline=COL_BOX_BORDER, width=1)
    ry = cy + 6
    cdraw.text((pad + 8, ry), diplo_lbl, fill=COL_DIPLO, font=f_bold)
    for i, ln in enumerate(diplo_lines):
        cdraw.text((pad + 8 + dlw, ry + i * 19), ln, fill=COL_DIPLO, font=f_bold)
    ry += max(1, len(diplo_lines)) * 19 + 4
    cdraw.text((pad + 8, ry), edit_lbl, fill=COL_EDIT, font=f_bold)
    for i, ln in enumerate(edit_lines):
        cdraw.text((pad + 8 + elw, ry + i * 19), ln, fill=COL_TEXT, font=f_reg)

    cy += reading_box_h + 10
    cdraw.text((pad, cy), ana_lbl, fill=COL_HEADER, font=f_bold)
    for i, ln in enumerate(ana_lines):
        cdraw.text((pad + alw, cy + i * 19), ln, fill=COL_TEXT, font=f_reg)

    return card_im


def render_standard_plate(filename, title, subtitle, rows, footer_label, footer_text, width=1650):
    """
    Assemble une planche constituée de rangées de cartes (`rows` est une liste de listes de cartes :
    1 carte = pleine largeur 1594px ; 2 cartes = 2 colonnes de 782px).
    """
    margin_x = 28
    gap_x = 30
    gap_y = 22
    full_w = width - 2 * margin_x

    rendered_rows = []
    total_h = 132
    for row_cards in rows:
        n = len(row_cards)
        cw = (full_w - (n - 1) * gap_x) // n
        imgs = [render_card_image(c, cw) for c in row_cards]
        row_h = max(im.height for im in imgs)
        # Égaliser la hauteur des cartes d'une même rangée
        equalized = []
        for im in imgs:
            if im.height < row_h:
                eq = Image.new("RGB", (cw, row_h), COL_CARD_BG)
                eq.paste(im, (0, 0))
                edraw = ImageDraw.Draw(eq)
                edraw.rectangle([0, 0, cw - 1, row_h - 1], outline=COL_CARD_BORDER, width=1)
                edraw.rectangle([0, 0, cw - 1, 6], fill=COL_HEADER)
                equalized.append(eq)
            else:
                equalized.append(im)
        rendered_rows.append(equalized)
        total_h += row_h + gap_y

    total_h += 95
    page = Image.new("RGB", (width, total_h), COL_BG)
    pdraw = ImageDraw.Draw(page)
    draw_header(page, pdraw, width, title, subtitle)

    y = 132
    for row_imgs in rendered_rows:
        x = margin_x
        for im in row_imgs:
            page.paste(im, (x, y))
            x += im.width + gap_x
        y += row_imgs[0].height + gap_y

    end_y = draw_footer(pdraw, width, y, footer_label, footer_text)
    page = page.crop((0, 0, width, end_y))
    out_path = os.path.join(OUT_DIR, filename)
    page.save(out_path, quality=94)
    print(f"[OK] {filename} ({page.width}x{page.height})")


def render_abecedaire_plate(filename, title, subtitle, cards, footer_label, footer_text, width=1680):
    """
    Assemble une planche d'abécédaire en grille 3 colonnes x 4 rangées (12 lettres).
    """
    margin_x = 24
    gap_x = 21
    gap_y = 20
    col_w = (width - 2 * margin_x - 2 * gap_x) // 3
    pad = 12
    inner_w = col_w - 2 * pad

    f_hdr = get_font(FONT_SERIF_BOLD, 15)
    f_freq = get_font(FONT_SANS_OBLIQUE, 12)
    f_bold = get_font(FONT_SANS_BOLD, 12)
    f_reg = get_font(FONT_SANS, 12)

    dummy = Image.new("RGB", (10, 10))
    ddraw = ImageDraw.Draw(dummy)

    def build_letter_card(c):
        crop_panel = render_crop_panel(
            c["src"], c["crop"], c["boxes"], target_w=inner_w, min_vpad_native=c.get("vpad", 24), max_h=150
        )
        l_var = "Variantes : "
        l_tr = "Tracé R1 : "
        l_pi = "Piège : "
        vw, _ = text_size(ddraw, l_var, f_bold)
        tw, _ = text_size(ddraw, l_tr, f_bold)
        pw, _ = text_size(ddraw, l_pi, f_bold)

        var_lines = wrap_text(ddraw, c["variantes"], f_reg, inner_w - vw)
        tr_lines = wrap_text(ddraw, c["trace"], f_reg, inner_w - tw)
        pi_lines = wrap_text(ddraw, c["piege"], f_reg, inner_w - pw)

        h = 34 + 10 + crop_panel.height + 10
        h += max(1, len(var_lines)) * 17 + 6
        h += max(1, len(tr_lines)) * 17 + 6
        h += max(1, len(pi_lines)) * 17 + 12

        im = Image.new("RGB", (col_w, h), COL_CARD_BG)
        dr = ImageDraw.Draw(im)
        dr.rectangle([0, 0, col_w - 1, h - 1], outline=COL_CARD_BORDER, width=1)
        dr.rectangle([0, 0, col_w - 1, 32], fill=COL_HEADER)
        dr.text((12, 7), c["letter"], fill=(255, 250, 240), font=f_hdr)
        fw, _ = text_size(dr, c["freq"], f_freq)
        dr.text((col_w - fw - 12, 9), c["freq"], fill=(240, 220, 185), font=f_freq)

        y = 42
        im.paste(crop_panel, (pad, y))
        y += crop_panel.height + 10

        dr.text((pad, y), l_var, fill=COL_DIPLO, font=f_bold)
        for i, ln in enumerate(var_lines):
            dr.text((pad + vw, y + i * 17), ln, fill=COL_TEXT, font=f_reg)
        y += max(1, len(var_lines)) * 17 + 6

        dr.text((pad, y), l_tr, fill=COL_EDIT, font=f_bold)
        for i, ln in enumerate(tr_lines):
            dr.text((pad + tw, y + i * 17), ln, fill=COL_TEXT, font=f_reg)
        y += max(1, len(tr_lines)) * 17 + 6

        dr.text((pad, y), l_pi, fill=COL_HEADER, font=f_bold)
        for i, ln in enumerate(pi_lines):
            dr.text((pad + pw, y + i * 17), ln, fill=COL_TEXT, font=f_reg)

        return im

    rows_imgs = []
    total_h = 130
    for r in range(0, len(cards), 3):
        rcards = cards[r:r + 3]
        ims = [build_letter_card(c) for c in rcards]
        rh = max(i.height for i in ims)
        eqs = []
        for i in ims:
            if i.height < rh:
                eq = Image.new("RGB", (col_w, rh), COL_CARD_BG)
                eq.paste(i, (0, 0))
                d = ImageDraw.Draw(eq)
                d.rectangle([0, 0, col_w - 1, rh - 1], outline=COL_CARD_BORDER, width=1)
                eqs.append(eq)
            else:
                eqs.append(i)
        rows_imgs.append(eqs)
        total_h += rh + gap_y

    total_h += 95
    page = Image.new("RGB", (width, total_h), COL_BG)
    pdraw = ImageDraw.Draw(page)
    draw_header(page, pdraw, width, title, subtitle)

    y = 130
    for r_ims in rows_imgs:
        x = margin_x
        for im in r_ims:
            page.paste(im, (x, y))
            x += col_w + gap_x
        y += r_ims[0].height + gap_y

    end_y = draw_footer(pdraw, width, y, footer_label, footer_text)
    page = page.crop((0, 0, width, end_y))
    out_path = os.path.join(OUT_DIR, filename)
    page.save(out_path, quality=94)
    print(f"[OK] {filename} ({page.width}x{page.height})")


def gen_plate_01():
    rows = [
        [
            {
                "title": "1. Registre d'apparat : la semi-onciale alexandrine de titre (Auszeichnungsschrift)",
                "subtitle": "f. 162v, haut de page — Fin de l'Hypothesis (R2) et titre monumental de la comédie",
                "src": SPEC01,
                "crop": (360, 140, 1380, 365),
                "max_h": 210,
                "boxes": [
                    (440, 195, 885, 255, "Fin de l'Hypothesis (R2)", "blue"),
                    (670, 260, 1370, 345, "Titre en semi-onciale d'apparat", "red"),
                ],
                "diplo": "προλογίζει μνησίλοχ(ος) κηδεστὴς εὐριπίδου · // ⁘ ΑΡΙϹΤΟΦΑΝΟΥϹ ΘΕϹΜΟΦΟΡΙΑΖΟΥϹΑΙ",
                "edit": "Προλογίζει Μνησίλοχος κηδεστὴς Εὐριπίδου. // ΑΡΙΣΤΟΦΑΝΟΥΣ ΘΕΣΜΟΦΟΡΙΑΖΟΥΣΑΙ",
                "analyse": "Module monumental (4 à 5 mm), tracé bilinéaire lent imitant l'onciale ronde alexandrine : Sigma lunaire (Ϲ), Epsilon lunaire (Є), Alpha à boucle, Phi à grand anneau aplati et grand losange floral (⁘) flanqué de traits.",
            },
            {
                "title": "2. Registre littéraire principal : la minuscule bouletée du Maître R1",
                "subtitle": "f. 162v, vv. 1–3 — Ouverture du dialogue comique (colonne centrale)",
                "src": F162V,
                "crop": (680, 420, 1565, 600),
                "max_h": 210,
                "boxes": [
                    (692, 432, 742, 492, "ὦ initial (en ∞ + circ.)", "red"),
                    (745, 435, 1555, 588, "R1 : minuscule bouletée régulière", "blue"),
                ],
                "diplo": "ὦ ζεῦ· χελιδὼν ἆρά ποτε φανήσεται· / ἀπολεῖ μ' ἀλοῶν ἅνθρωπος ἐξ ἑωθινοῦ· / οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "edit": "ΜΝ. Ὦ Ζεῦ, χελιδὼν ἆρά ποτε φανήσεται; / Ἀπολεῖ μ' ἁλοῶν ἄνθρωπος ἐξ ἑωθινοῦ. / Οἷόν τε, πρὶν τὸν σπλῆνα κομιδῇ μ' ἐκβαλεῖν...",
                "analyse": "Écriture suspendue sous la ligne de réglure, module régulier (2 mm), axe vertical (88°–90°), boules d'attaque aux extrémités des hampes, esprits anguleux ou arrondis et iota muet systématiquement adscrit (κομιδῆι).",
            },
        ],
        [
            {
                "title": "3. Registre scholiographique : la semi-cursive savante du Réviseur R2",
                "subtitle": "f. 162v, marge gauche face aux vv. 1–2 — Scholie ancienne (Σ 1) avec lemme et renvoi",
                "src": F162V,
                "crop": (215, 375, 695, 655),
                "max_h": 230,
                "boxes": [
                    (230, 385, 665, 535, "R2 : semi-cursive à abréviations hautes", "red"),
                    (310, 610, 470, 650, "Clôture du scholie (ἀφίκετο ·)", "blue"),
                ],
                "diplo": "ὦ ζεῦ χελιδών· ἐπὶ τῶ(ν)δ(ε) ἄσμε- / νος τὸ χελιδόνος ἔαρ ὥσπερ τ(ῶν) βαρ(βάρων)... / ... ἀφίκετο ·",
                "edit": "Ὦ Ζεῦ χελιδών : ἐπὶ τῶν... (scholie expliquant le proverbe de l'hirondelle annonciatrice du printemps).",
                "analyse": "Micro-module (1 à 1,2 mm), forte densité d'abréviations par suspension et par lettres supérieures, réintroduction massive de formes semi-onciales (Ν, Η, Λ, Π) et ponctuation de clôture.",
            },
            {
                "title": "4. Registre humaniste tardif : ajouts de la main d'imprimerie (1515)",
                "subtitle": "f. 176v, vv. 1189 et 1198 — Deux ajouts de γυ(νή) par la main de l'atelier de Bernard Junta (1515)",
                "src": SPEC15,
                "crop": (515, 210, 1260, 655),
                "max_h": 230,
                "boxes": [
                    (538, 232, 592, 282, "Main 1515 : γϋ. (= γυνή, v. 1189)", "red"),
                    (538, 582, 592, 635, "Main 1515 : γϋ. (v. 1198)", "red"),
                ],
                "diplo": "[v. 1189] γϋ. καλῶς ἔχει· λαβὲ θοἰμάτιον ὦ παιδίον· / ... / [v. 1198] γϋ. ἔπειτα κ[[ω->ο]]μίζεις αὐτοῖς· [σκ'] ἀκουλούτι τέκνον·",
                "edit": "[Interventions marginales absentes de R1 et de R2, insérées par Euphrosynus Boninus en 1515 pour l'édition Juntine].",
                "analyse": "Encre noire occidentale du XVIe siècle : gamma suivi d'un upsilon surmonté d'un double point (tréma) et d'un point d'abréviation (γϋ.). Ces deux seules notes prouvent le passage du manuscrit chez Euphrosynus Boninus en 1515.",
            },
        ],
    ]
    render_standard_plate(
        "01_les_quatre_registres_ecriture_ravennas.jpg",
        "PLANCHE 01 — LES QUATRE REGISTRES D'ÉCRITURE DU CODEX RAVENNAS 429",
        "Identifier d'un coup d'œil les quatre strates graphiques présentes sur les folios des Thesmophories (ff. 162v–177r)",
        rows,
        "RÈGLE DE DÉCHIFFREMENT N° 1",
        "Avant de lire un mot, identifiez toujours son registre : (1) la semi-onciale de titre se lit lettre à lettre comme des capitales ; (2) la colonne centrale R1 obéit aux ligatures de la minuscule bouletée ; (3) les marges R2 regorgent d'abréviations tachygraphiques ; (4) l'encre grise de 1515 n'appartient pas à la tradition byzantine du Xe siècle.",
    )


def gen_plate_02():
    width = 1650
    margin_x = 28
    full_w = width - 2 * margin_x
    pad = 14
    inner_w = full_w - 2 * pad

    # Panneau supérieur avec les 4 zones Z1..Z4 sur f. 162v vv. 1-2
    im_src = load_source(F162V)
    cx1, cy1, cx2, cy2 = 685, 420, 1480, 560
    sub = im_src.crop((cx1, cy1, cx2, cy2))
    scale = inner_w / float(sub.width)
    th = int(round(sub.height * scale))
    crop_im = sub.resize((inner_w, th), Image.Resampling.LANCZOS)
    cdraw = ImageDraw.Draw(crop_im)

    # Lignes pointillées Z1..Z4 sur la ligne 1 (y natif ~445..495)
    z_lines = [
        (442, "Z3 : Crête des hampes ascendantes (δ, η, θ, κ, λ, φ)", (25, 130, 65)),
        (456, "Z1 : Ligne de tête & potences (réglure aveugle : γ, π, τ, ξ)", (200, 28, 28)),
        (482, "Z2 : Base du noyau médian (α, ε, ι, ν, ο, σ, υ, ω)", (25, 85, 175)),
        (504, "Z4 : Ligne des hampes plongeantes (β, γ, ζ, μ, ξ, ρ, φ, χ, ψ)", (140, 45, 145)),
    ]
    f_z = get_font(FONT_SANS_BOLD, 12)
    for y_nat, z_lbl, z_col in z_lines:
        sy = int(round((y_nat - cy1) * scale))
        for x in range(0, inner_w, 14):
            cdraw.line([(x, sy), (min(inner_w, x + 8), sy)], fill=z_col, width=2)
        tw, th_txt = text_size(cdraw, z_lbl, f_z)
        cdraw.rectangle([inner_w - tw - 14, sy - th_txt // 2 - 2, inner_w - 4, sy + th_txt // 2 + 2],
                        fill=(255, 252, 245), outline=z_col, width=1)
        cdraw.text((inner_w - tw - 9, sy - th_txt // 2), z_lbl, fill=z_col, font=f_z)

    # Boîtes sur lettres témoins (coordonnées natives exactes sur F162V)
    letter_boxes = [
        (692, 432, 742, 490, "ὦ (esprit + circ. Z3)", "blue", "below"),
        (850, 448, 886, 504, "χ (sautoir Z2-Z4)", "red", "above"),
        (1222, 435, 1260, 502, "φ (axe Z3-Z4)", "green", "below"),
        (1302, 488, 1342, 542, "ἐξ (serpentin Z1-Z4)", "red", "left"),
    ]
    f_badge = get_font(FONT_SANS_BOLD, 12)
    for bx1, by1, bx2, by2, lbl, ckey, pos in letter_boxes:
        st = STYLE_COLORS[ckey]
        sx1 = int(round((bx1 - cx1) * scale))
        sy1 = int(round((by1 - cy1) * scale))
        sx2 = int(round((bx2 - cx1) * scale))
        sy2 = int(round((by2 - cy1) * scale))
        cdraw.rectangle([sx1, sy1, sx2, sy2], outline=st["outline"], width=3)
        tw, th_b = text_size(cdraw, lbl, f_badge)
        if pos == "left":
            lx = sx1 - tw - 16
            ly = sy2 - th_b - 4
        elif pos == "below":
            lx = max(4, min(sx1 - 6, inner_w - tw - 16))
            ly = min(th - th_b - 5, sy2 + 4)
        else:
            lx = max(4, min(sx1 - 6, inner_w - tw - 16))
            ly = max(3, sy1 - th_b - 6)
        cdraw.rectangle([lx, ly, lx + tw + 10, ly + th_b + 4], fill=st["fill"], outline=st["outline"], width=2)
        cdraw.text((lx + 5, ly + 2), lbl, fill=st["text"], font=f_badge)

    cdraw.rectangle([0, 0, inner_w - 1, th - 1], outline=COL_CARD_BORDER, width=1)

    # Construction de la page
    page = Image.new("RGB", (width, 1180), COL_BG)
    pdraw = ImageDraw.Draw(page)
    draw_header(
        page,
        pdraw,
        width,
        "PLANCHE 02 — ANATOMIE D'UNE LIGNE DE R1 : SUSPENSION ET SYSTÈME QUADRILINÉAIRE",
        "Comprendre le principe de l'écriture « suspendue » sous la réglure et les quatre zones verticales d'identification",
    )

    top_card_h = 82 + th + 16
    pdraw.rectangle([margin_x, 130, width - margin_x, 130 + top_card_h], fill=COL_CARD_BG, outline=COL_CARD_BORDER, width=1)
    pdraw.rectangle([margin_x, 130, width - margin_x, 136], fill=COL_HEADER)
    pdraw.text((margin_x + pad, 146), "Coupe anatomique de f. 162v, vv. 1–2 : Ὦ Ζεῦ, χελιδὼν ἆρά ποτε φανήσεται; / Ἀπολεῖ μ' ἁλοῶν ἄνθρωπος ἐξ ἑωθινοῦ",
               fill=COL_HEADER, font=get_font(FONT_SERIF_BOLD, 17))
    pdraw.text((margin_x + pad, 172), "Contrairement à l'écriture moderne posée SUR la ligne, la minuscule bouletée du Xe siècle est SUSPENDUE par le haut à la ligne de tête (Z1).",
               fill=COL_MUTED, font=get_font(FONT_SERIF_ITALIC, 14))
    page.paste(crop_im, (margin_x + pad, 200))

    # 4 cartes inférieures (Z1, Z2, Z3, Z4)
    y_cols = 130 + top_card_h + 22
    gap_x = 20
    col_w = (full_w - 3 * gap_x) // 4
    zones_info = [
        ("Z1 : Ligne de tête & Potences", (200, 28, 28),
         "Lettres suspendues : γ, π, τ, ξ, ζ.\n\nC'est l'axe directeur du calame. Les barres horizontales de γ, π et τ courent le long de ce fil invisible et servent de pont de ligature vers la lettre suivante."),
        ("Z2 : Corps moyen (noyau)", (25, 85, 175),
         "Lettres courtes : α, ε, ι, ν, ο, σ, υ, ω.\n\nHauteur régulière de 1,8 à 2 mm. Si une lettre reste intégralement confinée entre Z1 et Z2, son identité se réduit à ces 8 voyelles et consonnes courtes."),
        ("Z3 : Hampes ascendantes", (25, 130, 65),
         "Lettres hautes : δ, η (en h), θ, κ, λ, φ, ε (haut).\n\nLes fûts montent à +2 mm au-dessus de Z1 et portent aussi les esprits, les accents et les lettres supralinéaires d'abréviation."),
        ("Z4 : Hampes plongeantes", (140, 45, 145),
         "Lettres basses : β, γ, ζ, μ, ξ, ρ, φ, χ, ψ.\n\nToute attaque verticale à gauche sous Z2 signe un μ ; un axe central traversant Z3 et Z4 signe un φ ou un ψ ; un serpentin plongeant signe ξ ou ζ."),
    ]
    col_h = 250
    f_ct = get_font(FONT_SERIF_BOLD, 15)
    f_cb = get_font(FONT_SANS, 13)
    for idx, (zt, zcol, ztxt) in enumerate(zones_info):
        cx = margin_x + idx * (col_w + gap_x)
        pdraw.rectangle([cx, y_cols, cx + col_w, y_cols + col_h], fill=COL_CARD_BG, outline=COL_CARD_BORDER, width=1)
        pdraw.rectangle([cx, y_cols, cx + col_w, y_cols + 6], fill=zcol)
        pdraw.text((cx + 12, y_cols + 16), zt, fill=zcol, font=f_ct)
        zy = y_cols + 46
        for para in ztxt.split("\n\n"):
            for ln in wrap_text(pdraw, para, f_cb, col_w - 24):
                pdraw.text((cx + 12, zy), ln, fill=COL_TEXT, font=f_cb)
                zy += 19
            zy += 8

    end_y = draw_footer(
        pdraw,
        width,
        y_cols + col_h + 22,
        "MÉTHODE DE LECTURE TOPOLOGIQUE",
        "Face à un tracé ambigu, posez toujours deux questions géométriques avant de deviner le mot : (1) le glyphe est-il suspendu par une barre horizontale sur Z1 (γ, π, τ) ? (2) franchit-il le plafond Z3 (η, κ, λ, δ, θ) ou le plancher Z4 (μ, ρ, γ, φ, χ, ξ, ψ) ?",
    )
    page = page.crop((0, 0, width, end_y))
    out_path = os.path.join(OUT_DIR, "02_anatomie_ligne_R1_suspension_et_quadrilinearite.jpg")
    page.save(out_path, quality=94)
    print(f"[OK] 02_anatomie_ligne_R1_suspension_et_quadrilinearite.jpg ({page.width}x{page.height})")


def gen_plate_03():
    cards = [
        {
            "letter": "Α / α — ALPHA",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1010, 428, 1320, 504),
            "boxes": [
                (1038, 438, 1090, 495, "ἆρ-", "red"),
                (1090, 442, 1118, 488, "-ά", "red"),
                (1260, 448, 1288, 488, "φαν-", "blue"),
            ],
            "variantes": "(1) Minuscule cursif en goutte d'eau (95 %) ; (2) semi-oncial à boucle ouverte dans les titres et R2.",
            "trace": "Panse ronde fermée à gauche, suivie d'un dard oblique sortant vers la droite qui s'enchaîne directement à la consonne suivante.",
            "piege": "Se confond avec omicron (ο) si le dard de sortie est court, ou avec la base d'un epsilon en as de pique (ε).",
        },
        {
            "letter": "Β / β — BÊTA",
            "freq": "Fréquence R1 : Moyenne",
            "src": F162V,
            "crop": (1320, 525, 1560, 598),
            "boxes": [
                (1422, 540, 1446, 585, "β bilobé (u)", "red"),
            ],
            "variantes": "(1) Minuscule bilobé ouvert en haut « u » (85 %) ; (2) semi-oncial à double boucle fermée « B » à l'initiale ou après grattage.",
            "trace": "Deux cuvettes jumelles posées sur Z2 (forme d'un u latin cursif), sans hampe montante dans le corps des mots.",
            "piege": "PIÈGE MAJEUR : le β ouvert en « u » ressemble à un upsilon (υ) ou à un κ cursif ; le Β fermé se confond avec Κ dans l'archétype.",
        },
        {
            "letter": "Γ / γ — GAMMA",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (765, 882, 1055, 960),
            "boxes": [
                (872, 900, 928, 948, "γὰρ (γ potence)", "red"),
            ],
            "variantes": "(1) Minuscule à potence horizontale et boucle plongeante ; (2) semi-oncial en équerre haute (Γ) en début de vers ou dans R2.",
            "trace": "Fût descendant en Z4 (souvent bouclé) coiffé d'une barre horizontale sur Z1 qui se soude à la lettre suivante (γὰρ, γο).",
            "piege": "Confusion constante avec tau (τ) dont le fût est plus court et droit, et avec pi (π) à deux jambages.",
        },
        {
            "letter": "Δ / δ — DELTA",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (830, 428, 1070, 504),
            "boxes": [
                (945, 438, 975, 488, "δ (χελιδὼν)", "red"),
            ],
            "variantes": "(1) Minuscule à panse ronde et col de cygne montant en Z3 ; (2) triangulaire semi-oncial (Δ) dans les titres et scholies.",
            "trace": "Ventre circulaire posé entre Z1 et Z2, surmonté d'une hampe souple inclinée à gauche puis recourbée à droite en crochet.",
            "piege": "Lorsqu'il entre en ligature (δε, δι, δο), son col s'abaisse et peut imiter un thêta (θ) ou un alpha suivi d'iota.",
        },
        {
            "letter": "Ε / ε — EPSILON",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1240, 478, 1525, 550),
            "boxes": [
                (1302, 488, 1342, 542, "ἐξ (lig. as de pique)", "red"),
                (1350, 488, 1374, 534, "ἑ- (ἑωθινοῦ)", "blue"),
            ],
            "variantes": "(1) Cursif bilobé en « 8 ouvert » ; (2) « as de pique » haut lié par le sommet ; (3) lunaire (ϵ) en fin de mot.",
            "trace": "Lettre caméléon : sa boucle supérieure monte en Z3 pour projeter un trait descendant vers ι, ξ, ρ, σ, τ.",
            "piege": "L'epsilon en « as de pique » (ει, εξ, ερ, εσ) déroute les débutants qui cherchent deux lettres séparées.",
        },
        {
            "letter": "Ζ / ζ — ZÊTA",
            "freq": "Fréquence R1 : Basse",
            "src": F162V,
            "crop": (685, 428, 920, 504),
            "boxes": [
                (745, 445, 780, 498, "ζ (ζεῦ)", "red"),
            ],
            "variantes": "Forme unique en éclair sinueux plongeant sous la ligne de base.",
            "trace": "Barre horizontale d'attaque sur Z1, diagonale courte vers la gauche et longue queue recourbée plongeant profondément en Z4.",
            "piege": "Très proche du xi (ξ) : le ζ n'a qu'un seul repli médian alors que le ξ possède un double zig-zag en serpentin.",
        },
        {
            "letter": "Η / η — ÊTA",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1030, 525, 1365, 598),
            "boxes": [
                (1120, 538, 1148, 585, "ῆ (σπλῆνα)", "red"),
                (1312, 538, 1334, 585, "ῆ (κομιδῆι)", "blue"),
            ],
            "variantes": "(1) Minuscule en « h » latin (90 %) ; (2) semi-oncial en « H » capital dans les titres et scholies R2.",
            "trace": "Long fût vertical descendant de Z3 à Z2, suivi d'une arche ronde à droite qui se pose sur la ligne de base.",
            "piege": "PIÈGE CLASSIQUE : son identité morphologique avec notre « h » latin le fait confondre avec kappa (κ) ou lambda (λ).",
        },
        {
            "letter": "Θ / θ — THÊTA",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (1285, 478, 1535, 550),
            "boxes": [
                (1402, 488, 1428, 534, "θ (ἑωθινοῦ)", "blue"),
            ],
            "variantes": "(1) Ovale haut fermé traversé d'une barre médiane ; (2) θ ouvert cursif en boucle haute lié à droite.",
            "trace": "Grand anneau oblong dépassant en Z3 ; la traverse horizontale déborde souvent à droite pour lier la voyelle suivante.",
            "piege": "Un θ étroit à traverse courte se confond avec omicron (ο), epsilon lunaire (ϵ) ou la panse d'un delta (δ).",
        },
        {
            "letter": "Ι / ι — IOTA",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1185, 525, 1410, 598),
            "boxes": [
                (1275, 542, 1292, 585, "ι (κομιδῆι)", "red"),
                (1332, 542, 1346, 585, "ι adscrit (-ῆι)", "blue"),
            ],
            "variantes": "(1) Trait vertical court avec boule d'attaque ; (2) iota plongeant appendu sous les ligatures (ει, αι, οι).",
            "trace": "Simple fût droit confiné entre Z1 et Z2, sans jamais porter de point (sauf tréma antique sur ϊ/ϋ).",
            "piege": "En fin de dative longue (-ᾶι, -ῆι, -ῶι), l'iota muet adscrit ressemble au déictique comique -ί (ὁδί, ταυτί).",
        },
        {
            "letter": "Κ / κ — KAPPA",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (1185, 525, 1525, 598),
            "boxes": [
                (1198, 538, 1222, 585, "κ- (κομιδῆι)", "red"),
                (1398, 538, 1422, 585, "-κ- (ἐκβαλεῖν)", "blue"),
            ],
            "variantes": "(1) Minuscule à haute hampe (Z3) et accolade droite ; (2) κ court de module moyen.",
            "trace": "Fût vertical identique à celui de η, mais le jambage droit est brisé en son milieu comme une accolade « { ».",
            "piege": "Si l'encre bouche l'angle de l'accolade, κ devient indiscernable de η (en h) ou d'un β bilobé.",
        },
        {
            "letter": "Λ / λ — LAMBDA",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (735, 478, 1085, 550),
            "boxes": [
                (820, 488, 855, 538, "λ (ἀπολεῖ)", "red"),
                (965, 488, 992, 536, "λ (ἁλοῶν)", "blue"),
            ],
            "variantes": "(1) Minuscule à longue hampe oblique et arche gauche ; (2) grand Λ en chevron dans les titres et R2 ; (3) λλ géminé.",
            "trace": "Long trait diagonal descendant de Z3 vers la droite, sous lequel s'arc-boute une petite jambe courbe à gauche.",
            "piege": "En ligature double (λλ), le premier lambda s'imbrique sous le second en formant un dôme trompeur.",
        },
        {
            "letter": "Μ / μ — MU",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1185, 525, 1460, 598),
            "boxes": [
                (1242, 542, 1275, 590, "μ (κομιδῆι)", "red"),
                (1348, 540, 1375, 592, "μ' (μ' ἐκβαλεῖν)", "blue"),
            ],
            "variantes": "Minuscule invariable à longue hampe d'attaque plongeante à gauche.",
            "trace": "Le calame attaque en Z1, plonge verticalement en Z4 à gauche, puis remonte tracer deux ponts arrondis sur Z2.",
            "piege": "CRITÈRE ABSOLU : μ possède TOUJOURS une queue plongeante à gauche, ce qui le distingue du ν minuscule (en v).",
        },
    ]
    render_abecedaire_plate(
        "03_abecedaire_visuel_alpha_a_mu.jpg",
        "PLANCHE 03 — ABÉCÉDAIRE VISUEL DU RAVENNAS 429 (PREMIÈRE PARTIE : Α – Μ)",
        "Spécimens authentiques extraits de la main R1 (f. 162v), variantes allographiques, ductus et pièges de confusion",
        cards,
        "SYNTHÈSE DE L'ABÉCÉDAIRE (Α – Μ)",
        "Retenez les trois marqueurs discriminants de cette première moitié d'alphabet : (1) la queue plongeante gauche du μ ; (2) la cuvette bilobée en « u » du β minuscule ; (3) la triade des trois hampes hautes η (arche ronde), κ (accolade brisée) et λ (jambe diagonale).",
    )


def gen_plate_04():
    cards = [
        {
            "letter": "Ν / ν — NU",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (845, 428, 1120, 504),
            "boxes": [
                (1002, 448, 1030, 488, "-ν (χελιδὼν)", "red"),
            ],
            "variantes": "(1) Minuscule en « v » pointu à droite (92 %) ; (2) semi-oncial en « N » capital en fin de ligne ou dans R2.",
            "trace": "Jambage gauche descendant sur Z2 puis remontée souple vers Z1 terminée par un crochet ou une boule d'arrêt.",
            "piege": "PIÈGE N° 1 DU MANUSCRIT : le ν minuscule ressemble exactement à un « v » ou « u » latin, d'où la confusion constante ν / υ / μ.",
        },
        {
            "letter": "Ξ / ξ — XI",
            "freq": "Fréquence R1 : Moyenne",
            "src": F162V,
            "crop": (1220, 478, 1525, 550),
            "boxes": [
                (1302, 488, 1342, 542, "ξ (ἐξ)", "red"),
            ],
            "variantes": "Serpentin vertical à trois boucles superposées plongeant en Z4.",
            "trace": "Trait d'attaque horizontal sur Z1, double lacet médian en S inversé et longue queue recourbée sous la ligne.",
            "piege": "En ligature avec epsilon (ἐξ), la tête de l'epsilon coiffe directement le serpentin du ξ en un seul glyphe continu.",
        },
        {
            "letter": "Ο / ο — OMICRON",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (725, 525, 1045, 598),
            "boxes": [
                (735, 538, 792, 585, "οἷόν (2 omicron)", "red"),
                (978, 542, 998, 585, "τὸν (ο)", "blue"),
            ],
            "variantes": "Petit anneau fermé, parfois réduit à un micro-cercle suspendu sous la potence d'un τ ou d'un π.",
            "trace": "Tracé circulaire rapide d'un seul jet dans le sens anti-horaire, strictement confiné dans la zone médiane Z2.",
            "piege": "S'échange fréquemment avec alpha (α), sigma lunaire (σ) ou oméga (ω) lorsque la plume s'empâte.",
        },
        {
            "letter": "Π / π — PI",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (845, 525, 1145, 598),
            "boxes": [
                (865, 540, 912, 588, "πρ- (πρὶν)", "red"),
                (1055, 542, 1078, 585, "-π- (σπλῆνα)", "blue"),
            ],
            "variantes": "(1) Minuscule à double panse fermée (forme d'oméga coiffé d'une barre) ; (2) Π à deux colonnes droites.",
            "trace": "Les deux jambages se recourbent vers l'intérieur sur Z2 tandis que la longue barre de tête (Z1) lie la suite.",
            "piege": "Si la barre de tête s'efface, le π minuscule à base arrondie ressemble à s'y méprendre à un oméga (ω).",
        },
        {
            "letter": "Ρ / ρ — RHÔ",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (720, 575, 1450, 645),
            "boxes": [
                (785, 588, 810, 636, "ρ (παρὰ)", "red"),
                (1352, 588, 1374, 636, "ρ (ὠὐριπίδη)", "blue"),
            ],
            "variantes": "Panse ronde sur Z2 et longue hampe verticale plongeant en Z4.",
            "trace": "Tracé d'un seul mouvement partant du haut de la boucle, descendant tout droit en Z4 avec boule terminale.",
            "piege": "En ligature après τ, γ ou π (τρ, γρ, πρ), la boucle du ρ s'accroche directement sous la potence.",
        },
        {
            "letter": "Ϲ / σ / ς — SIGMA",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (1090, 478, 1390, 550),
            "boxes": [
                (1262, 495, 1292, 534, "-σ final (ἅνθρωπος)", "red"),
            ],
            "variantes": "(1) Minuscule fermé à casquette horizontale (σ) ; (2) sigma lunaire ouvert (Ϲ/c) en fin de mot et dans R2.",
            "trace": "R1 ignore notre « ς » final moderne en S : il emploie le sigma rond à casquette ou le croissant lunaire (c).",
            "piege": "La casquette horizontale du σ se soude à π, τ, θ, κ, χ en créant des ligatures très compactes (σπ, στ, σθ).",
        },
        {
            "letter": "Τ / τ — TAU",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (800, 525, 1045, 598),
            "boxes": [
                (818, 540, 855, 585, "τε (τ)", "red"),
                (958, 540, 980, 585, "τὸν (τ)", "blue"),
            ],
            "variantes": "(1) Tau court sous potence Z1 ; (2) tau haut dépassant en Z3 dans les groupes ligaturés (στ, τρ).",
            "trace": "Large traverse horizontale sur Z1 et fût vertical court s'arrêtant net sur Z2 avec un léger crochet.",
            "piege": "Ne descend jamais aussi bas que le gamma (γ) ; en revanche sa barre se confond avec celle de γ et π.",
        },
        {
            "letter": "Υ / υ — UPSILON",
            "freq": "Fréquence R1 : Haute",
            "src": F162V,
            "crop": (830, 575, 1125, 645),
            "boxes": [
                (885, 588, 908, 628, "-ῦ (σοῦ)", "red"),
                (938, 590, 962, 628, "-υ- (πυθέσθαι)", "blue"),
            ],
            "variantes": "(1) Cuvette ronde en « u » sans queue ; (2) forme caliciforme en « Y » dans les titres et R2.",
            "trace": "Simple courbe concave posée sur Z2 ; contrairement au ν minuscule, son bord droit ne se replie pas vers l'intérieur.",
            "piege": "La ressemblance entre υ (en u) et ν (en v) impose de vérifier systématiquement la grammaire de la désinence.",
        },
        {
            "letter": "Φ / φ — PHI",
            "freq": "Fréquence R1 : Moyenne",
            "src": F162V,
            "crop": (1115, 428, 1445, 504),
            "boxes": [
                (1222, 435, 1260, 502, "φ- (φανήσεται)", "red"),
            ],
            "variantes": "Anneau médian (ou double boucle en 8 couché) traversé par la plus longue hampe du manuscrit (Z3–Z4).",
            "trace": "Le fût vertical traverse intégralement les quatre zones quadrilinéaires, offrant un point de repère immédiat.",
            "piege": "Impossible à manquer grâce à sa double extension verticale ; ne peut se confondre qu'avec ψ si l'anneau est ouvert.",
        },
        {
            "letter": "Χ / χ — KHI",
            "freq": "Fréquence R1 : Moyenne",
            "src": F162V,
            "crop": (795, 428, 1055, 504),
            "boxes": [
                (850, 448, 886, 504, "χ- (χελιδὼν)", "red"),
            ],
            "variantes": "Croix de Saint-André asymétrique dont les deux branches plongent sous la ligne de base (Z2–Z4).",
            "trace": "Trait descendant de gauche à droite à forte pente, croisé par une diagonale souple descendant de droite à gauche.",
            "piege": "En réduction supralinéaire dans R2 (μοναχῶς, Μνησίλοχος), le χ est parfois pris pour un simple trait d'abréviation.",
        },
        {
            "letter": "Ψ / ψ — PSI",
            "freq": "Fréquence R1 : Basse",
            "src": F162V,
            "crop": (715, 658, 1030, 735),
            "boxes": [
                (765, 672, 805, 725, "ψ (ὄψει v. 6)", "red"),
            ],
            "variantes": "(1) Trident caliciforme en coupe ouverte ; (2) croix droite à traverse horizontale ou incurvée.",
            "trace": "Long axe vertical couvrant Z3–Z4, embrassé au niveau de Z2 par deux bras relevés vers le ciel.",
            "piege": "Lettre rare mais très lisible grâce à son axe vertical traversant toute la hauteur d'interligne.",
        },
        {
            "letter": "Ω / ω — OMÉGA",
            "freq": "Fréquence R1 : Très haute",
            "src": F162V,
            "crop": (685, 428, 1085, 550),
            "boxes": [
                (692, 432, 742, 490, "ὦ (v. 1 en ∞)", "red"),
                (975, 448, 1002, 488, "-ὼ- (χελιδὼν)", "blue"),
                (1015, 492, 1052, 534, "-ῶ- (ἁλοῶν v. 2)", "green"),
            ],
            "variantes": "(1) Minuscule ouvert en « w » arrondi ; (2) oméga fermé en « 8 couché » (∞) très fréquent en ligature.",
            "trace": "Deux loges jumelles posées sur Z2 ; lorsque les deux boucles se referment au centre, l'ω prend la forme ∞.",
            "piege": "L'oméga fermé en ∞ ressemble à un double omicron (οο) ou à la base d'un pi minuscule (π).",
        },
    ]
    render_abecedaire_plate(
        "04_abecedaire_visuel_nu_a_omega.jpg",
        "PLANCHE 04 — ABÉCÉDAIRE VISUEL DU RAVENNAS 429 (SECONDE PARTIE : Ν – Ω)",
        "Spécimens authentiques extraits de la main R1 (f. 162v), variantes allographiques, ductus et pièges de confusion",
        cards,
        "SYNTHÈSE DE L'ABÉCÉDAIRE (Ν – Ω)",
        "Observez l'opposition fondamentale des lettres basses et rondes : (1) le ν minuscule (en v) n'a jamais de queue plongeante contrairement au μ ; (2) le φ et le ψ traversent les quatre zones verticales (Z3 à Z4) ; (3) l'ω se referme souvent en huit couché (∞).",
    )


def gen_plate_05():
    rows = [
        [
            {
                "title": "1. Comparaison directe sur une même ligne : deux Μ (μ) et trois Ν (ν) côte à côte",
                "subtitle": "f. 162v, v. 3 — οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "src": F162V,
                "crop": (725, 525, 1600, 598),
                "max_h": 195,
                "boxes": [
                    (928, 542, 955, 585, "ν1 (πρὶν)", "blue"),
                    (998, 542, 1025, 585, "ν2 (τὸν)", "blue"),
                    (1242, 542, 1275, 590, "μ1 (κομιδῆι : queue Z4)", "red"),
                    (1348, 540, 1375, 592, "μ2 (μ' : queue Z4)", "red"),
                    (1535, 540, 1585, 588, "ν3 (ἐκβαλεῖν)", "blue"),
                ],
                "diplo": "οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "edit": "Οἷόν τε, πρὶν τὸν σπλῆνα κομιδῇ μ' ἐκβαλεῖν (v. 3 : « Est-il possible, avant que je ne crache complètement ma rate... »)",
                "analyse": "Regardez le plancher de la ligne (Z2) : dans πρὶν (ν1), τὸν (ν2) et ἐκβαλεῖν (ν3), le ν minuscule s'arrête net sur la ligne de base comme un « v » pointu. Au contraire, dans κομιδῆι (μ1) et μ' (μ2), une hampe verticale plonge à gauche sous la ligne (en Z4) avant de remonter former le double pont du μ.",
            }
        ],
        [
            {
                "title": "2. Opposition côte à côte de Ν final (-ν) et Μ médian (-μ-) avec correction sur grattage",
                "subtitle": "f. 163v, v. 94 — τὸ γὰρ τεχνάζειν ἡμέτερος ὁ πυραμοῦς (corr. de πυραμίδος)",
                "src": F163V,
                "crop": (740, 962, 1615, 1042),
                "max_h": 185,
                "boxes": [
                    (1092, 975, 1128, 1028, "-ν (τεχνάζειν : en v)", "blue"),
                    (1180, 975, 1225, 1032, "-μ- (ἡμέτερος : queue Z4)", "red"),
                    (1395, 975, 1605, 1035, "πυραμοῦς (μ + corr. -οῦς)", "red"),
                ],
                "diplo": "τὸ γὰρ τεχνάζειν· ἡμέτερος ὁ πυραμ[[ίδος -> οῦς]]·",
                "edit": "Τὸ γὰρ τεχνάζειν ἡμέτερος ὁ πυραμοῦς (v. 94 : « Car en matière de ruse, le gâteau de victoire est à nous ! »)",
                "analyse": "Juste après la ponctuation haute de τεχνάζειν (terminé par un ν en v sans queue), ἡμέτερος et πυραμοῦς montrent deux μ à longue hampe gauche plongeante. La finale -οῦς a été récrite sur le grattage de la faute -ίδος.",
            },
            {
                "title": "3. Trois Μ (μ) et deux Ν (ν) successifs dans un même hémistiche",
                "subtitle": "f. 175v, v. 1114 — σκέψαι τὸ σῦκο(ν)· μή τι μικρὸν φαίνεται;",
                "src": F175V,
                "crop": (770, 1625, 1555, 1702),
                "max_h": 185,
                "boxes": [
                    (1105, 1640, 1165, 1690, "μή (μ1 à queue gauche)", "red"),
                    (1220, 1640, 1265, 1692, "μι- (μ2 à queue gauche)", "red"),
                    (1345, 1640, 1385, 1688, "-ὸν (ν en v sur Z2)", "blue"),
                ],
                "diplo": "σκέψαι τὸ σῦκο(ν) μή τι· μικρὸν φαίνεται·",
                "edit": "Σκέψαι τὸ κύσθον· μή τι μικρὸν φαίνεται; (v. 1114 : « Regarde sa nature : te paraît-elle petite ? » — R1 a substitué σῦκον).",
                "analyse": "Les deux mots μή et μικρὸν commencent chacun par la longue attaque verticale plongeante du μ (encadrés rouges), tandis que la désinence neutre -ὸν de μικρὸν se referme en « v » court sur la ligne médiane (encadré bleu).",
            },
        ],
    ]
    render_standard_plate(
        "05_piege1_nu_minuscule_vs_mu_minuscule.jpg",
        "PLANCHE 05 — PIÈGE N° 1 : NU MINUSCULE (ν en « v ») CONTRE MU MINUSCULE (μ à queue)",
        "Éliminer définitivement la faute de lecture la plus fréquente des débutants devant la minuscule bouletée du Xe siècle",
        rows,
        "RÈGLE D'OR N° 1 (TEST DE LA QUEUE GAUCHE)",
        "Ne lisez JAMAIS un glyphe en forme de « v » ou « u » comme un upsilon sans vérifier la grammaire : dans 90 % des cas, c'est un NU (ν). Et ne confondez jamais ν et μ : le MU (μ) commence TOUJOURS par une hampe verticale qui plonge sous la ligne de base à gauche (zone Z4).",
    )


def gen_plate_06():
    rows = [
        [
            {
                "title": "1. Bêta minuscule bilobé (« u ») suivi d'un Bêta semi-oncial (« B ») sur grattage",
                "subtitle": "f. 162v, v. 35 — βε[[α->β]]ίνηκας (corrigé de βεαίνηκας in rasura)",
                "src": SPEC02,
                "crop": (420, 445, 1240, 525),
                "max_h": 185,
                "boxes": [
                    (570, 462, 760, 512, "βε[[α->β]]ίνηκας (β1 en u + Β2 en B)", "red"),
                ],
                "diplo": "καὶ προπεφώρακας· σὺ δ' ὦνδρες βε[[α->β]]ίνηκας σὺ·",
                "edit": "... βεβίνηκας σύ (v. 35 : « ... tu as baisé, toi ! »)",
                "analyse": "Ce mot unique réunit côte à côte les deux allographes du bêta : le premier (β-) est le bêta minuscule bilobé en « u » ; le second (-β-), récrit par R2 sur un alpha gratté, adopte la forme semi-onciale haute « B » pour occuper tout l'espace du grattage.",
            },
            {
                "title": "2. Bêta minuscule bilobé (« u ») devant delta dans le groupe consonantique -βδ-",
                "subtitle": "f. 168r, v. 489 — κύβδ' ἐχομένην τῆς δάφνης",
                "src": SPEC08,
                "crop": (140, 60, 900, 148),
                "max_h": 185,
                "boxes": [
                    (465, 85, 565, 135, "κύβδ' (β bilobé en u)", "red"),
                ],
                "diplo": "ἠρειδόμην κύβδ' ἐχομένη τῆς δάφνης",
                "edit": "Ἠρειδόμην κύβδ' ἐχομένη τῆς δάφνης (v. 489 : « Je me faisais besogner courbée en avant, agrippée au laurier »)",
                "analyse": "Dans κύβδ', la cuvette bilobée du β (identique à un u latin à double fond) suit immédiatement l'upsilon (ύ) et s'attache par la base à la panse ronde du delta (δ).",
            },
        ],
        [
            {
                "title": "3. Deux Bêta minuscules initiaux sur une même ligne (βαΰζα et βάλλουσα)",
                "subtitle": "f. 173r, v. 895 — ΠΡ. βαΰζα σὺ... / ΜΝ. βάλλουσα ψόγωι",
                "src": SPEC12,
                "crop": (15, 25, 920, 110),
                "max_h": 185,
                "boxes": [
                    (148, 40, 275, 98, "βαΰζα (β- en u + ϋ tréma)", "red"),
                    (515, 40, 685, 98, "βάλλουσα (β- en u)", "blue"),
                ],
                "diplo": "πρ(ύτανις) βαΰζα σὺ· ... βάλλουσα ψόγωι",
                "edit": "Βάυζε σὺ... βάλλουσα ψόγῳ (v. 895 : « Aboie donc, toi... en me couvrant de blâme »)",
                "analyse": "Même à l'initiale absolue de mot, R1 préfère ici le β minuscule bilobé en « u » ouvert par le haut, suivi immédiatement de l'alpha en goutte d'eau (βα-).",
            },
            {
                "title": "4. Bêta bilobé dans la semi-cursive scholiographique de R2 (ἁβρῶς βαδίζειν)",
                "subtitle": "f. 176v, Σ v. 1174 (marge gauche) — Glose explicative sur le pas de danse perse",
                "src": F176V,
                "crop": (350, 550, 780, 645),
                "max_h": 185,
                "boxes": [
                    (520, 578, 718, 620, "ἁβρῶς βαδίζειν (2 β en u)", "red"),
                ],
                "diplo": "τὸ ἁβρῶς βαδίζειν· ὡς οἱ πέρσαι ÷",
                "edit": "Σ 1174 : Τὸ ἁβρῶς βαδίζειν, ὡς οἱ Πέρσαι (« Marcher délicatement, à la manière des Perses »).",
                "analyse": "Dans la main rapide de R2 comme dans R1, les deux bêta de ἁβρῶς et de βαδίζειν sont tracés comme de petites cuvettes doubles en « u » ouvertes vers le haut.",
            },
        ],
    ]
    render_standard_plate(
        "06_piege2_beta_bilobe_u_vs_B_oncial_kappa_nu.jpg",
        "PLANCHE 06 — PIÈGE N° 2 : LE BÊTA MINUSCULE BILOBÉ (« u ») ET LE BÊTA ONCIAL (« B »)",
        "Reconnaître sans hésitation la lettre la plus déroutante de la minuscule bouletée du Xe siècle",
        rows,
        "RÈGLE D'OR N° 2 (IDENTIFICATION DU BÊTA)",
        "Dans le Ravennas 429, n'attendez pas un « B » majuscule dans le corps des mots : le bêta minuscule (β) est une double cuvette posée sur la ligne médiane, ouverte en haut comme un « u » latin à fond plat ou bilobé. Il se distingue de l'upsilon (υ) par son double lobe basal.",
    )


def gen_plate_07():
    rows = [
        [
            {
                "title": "1. Êta minuscule en « h » et double faute d'onciale corrigée (Η -> ει et Ε -> τ)",
                "subtitle": "f. 163v, v. 80 — ἐπεὶ τρίτη 'στὶ Θεσμοφορίων ἡ μέση",
                "src": SPEC04,
                "crop": (590, 5, 1300, 78),
                "max_h": 185,
                "boxes": [
                    (615, 15, 735, 65, "ἐπεὶ (corr. de ΗΠΕΙ)", "red"),
                    (740, 15, 830, 65, "τρίτη (η en « h »)", "blue"),
                    (832, 15, 885, 65, "'στὶ (corr. de ΕΤΙ)", "red"),
                ],
                "diplo": "ἐπεὶ [ex ἠπεὶ] τρίτη 'στὶ [ex ἐτὶ] θεσμοφορίων ἡ μέση·",
                "edit": "Ἐπεὶ τρίτη 'στὶ Θεσμοφορίων ἡ μέση (v. 80 : « Puisque c'est le troisième jour des Thesmophories, celui du milieu »)",
                "analyse": "Ce vers concentre deux fautes d'onciale corrigées sur place (ΗΠΕΙ -> ἐπεὶ par ajout d'une boucle d'epsilon ; ΕΤΙ -> 'στὶ par transformation d'epsilon en ligature στ) encadrant l'êta minuscule en « h » latin de τρίτη.",
            },
            {
                "title": "2. Confusion d'onciale Α / Ι à l'initiale : ἀφύων (R1) contre γρ(άφεται) ἰφύων (R2)",
                "subtitle": "f. 173r, v. 910 et Σ 910 — ἀπὸ τῶν ἀφύων (texte) vs ἰφύων (variante marginale)",
                "src": SPEC12,
                "crop": (550, 635, 1460, 760),
                "max_h": 185,
                "boxes": [
                    (775, 665, 925, 718, "ἀφύων (R1 : α initial)", "red"),
                    (1015, 645, 1435, 755, "Σ R2 : γρ(άφεται) ἰφύων (ι initial)", "blue"),
                ],
                "diplo": "ἐγὼ γὰρ ἀπὸ τῶν ἀφύων... // [Σ R2] γρ(άφεται) ἰφύων· λάχανον ἄγριον ÷",
                "edit": "Ἐγὼ γὰρ ἀπὸ τῶν ἰφύων... (v. 910 : « Moi, aux feuilles de lavande [ἰφύων] — ou aux anchois [ἀφύων] ! »)",
                "analyse": "Dans l'archétype en majuscules, ΙΦΥΩΝ a été banalisé en ΑΦΥΩΝ (« anchois »). R2 conserve en marge la leçon authentique ἰφύων (« lavande sauvage ») précédée du sigle critique γρ(άφεται).",
            },
        ],
        [
            {
                "title": "3. Confusion Ο / Ε dans la Parabase : ποθοῦντας corrigé de πεθοῦντας",
                "subtitle": "f. 172r, v. 815 — ποθοῦντας ἀργυρίου",
                "src": SPEC10,
                "crop": (150, 125, 880, 215),
                "max_h": 185,
                "boxes": [
                    (580, 148, 825, 202, "ποθοῦντας (ο refait sur ε)", "red"),
                ],
                "diplo": "ἀργυρίου· πο[ex ε]θοῦντας...",
                "edit": "... ποθοῦντας (v. 815 : « ... ceux qui regrettent »)",
                "analyse": "La première syllabe πο- montre un omicron refait par surcharge sur un epsilon (πεθοῦντας -> ποθοῦντας), suivi d'un thêta haut (θ) et de la ligature -οῦν-.",
            },
            {
                "title": "4. Hampes hautes κ / λ et correction de εἶεν en οἷόν",
                "subtitle": "f. 168r, v. 500 — ὑπ' αὐγὰς οἷόν ἐστιν ἐγκεκαλυμμένον",
                "src": SPEC08,
                "crop": (140, 540, 900, 618),
                "max_h": 185,
                "boxes": [
                    (350, 552, 462, 605, "οἷόν (corr. de εἶεν)", "red"),
                    (570, 552, 890, 608, "ἐγκεκαλυμμένον (2 κ + λ + 2 μ)", "blue"),
                ],
                "diplo": "ὑπ' αὐγὰς οἷόν [ex εἶεν] ἐστιν ἐγκεκαλυμμένον",
                "edit": "Ὑπ' αὐγὰς οἷόν ἐστιν ἐγκεκαλυμμένον (v. 500 : « Comme un mari a la tête voilée pendant qu'elle montre sa toile au jour ! »)",
                "analyse": "Outre la correction de εἶεν en οἷόν, le long participe ἐγκεκαλυμμένον offre un exercice idéal pour distinguer les deux kappa à accolade (-γκ-, -κα-), le lambda diagonal (-λ-) et les deux mu à queue plongeante (-μμ-).",
            },
        ],
    ]
    render_standard_plate(
        "07_piege3_eta_kappa_lambda_nu.jpg",
        "PLANCHE 07 — PIÈGE N° 3 : HAMPES HAUTES (η, κ, λ) ET TRÉBUCHEMENTS D'ONCIALE (Η/ΕΙ, Α/Ι, Ο/Ε)",
        "Distinguer la triade des hampes hautes en Z3 et repérer les fautes héritées de l'archétype en majuscules",
        rows,
        "RÈGLE D'OR N° 3 (TRIADE DES HAMPES HAUTES & ARCHÉTYPE)",
        "Quand une hampe monte en Z3, regardez sa base droite sur Z2 : (1) arche ronde = ÊTA (η en h) ; (2) accolade pincée au milieu = KAPPA (κ) ; (3) grande diagonale posée sur une arche gauche = LAMBDA (λ). Soyez aussi attentif aux corrections sur place des fautes d'onciale (Η/ΕΙ, Ε/Τ, Α/Ι, Ο/Ε).",
    )


def gen_plate_08():
    rows = [
        [
            {
                "title": "1. Confusion Alpha (α) / Omicron (ο) corrigée par lettre supralinéaire",
                "subtitle": "f. 172v, v. 838 — ὑστέραν (R1 avait écrit ὑστέρον, corrigé par α au-dessus de ο)",
                "src": SPEC11,
                "crop": (485, 142, 1480, 235),
                "max_h": 185,
                "boxes": [
                    (495, 152, 655, 225, "ὑστέρ[ο->α]ν (α supralinéaire)", "red"),
                ],
                "diplo": "ὑστέρ[ο s.l. α]ν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην",
                "edit": "Ὑστέραν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην (v. 838 : « Qu'elle soit assise au dernier rang, tondue au bol »)",
                "analyse": "En minuscule bouletée rapide, l'alpha (α) dont le dard de sortie est écourté devient identique à l'omicron (ο). R2 a rétabli le féminin ὑστέραν en traçant un alpha cursif juste au-dessus de l'omicron fautif.",
            },
            {
                "title": "2. Confusion d'ouverture et de fermeture des rondes : οὔπολις corrigé en ὦ πόλεις",
                "subtitle": "f. 172v, v. 839 — μιᾶς γ' ἕκατι μηδαμῶς ὦ πόλεις",
                "src": SPEC11,
                "crop": (485, 202, 1545, 292),
                "max_h": 185,
                "boxes": [
                    (1345, 215, 1525, 280, "ὦ πόλεις (corr. de οὔπολις)", "red"),
                ],
                "diplo": "... ὦ πόλεις [ex οὔπολις]",
                "edit": "... ὦ πόλεις (v. 839 : « ... ô cités ! »)",
                "analyse": "Sur le même folio (juste une ligne plus bas), la fausse lecture οὔπολις a été rectifiée par surcharge en ὦ πόλεις : l'oméga initial et la diphtongue -ει- ont été refaits directement sur l'encre de R1.",
            },
        ],
        [
            {
                "title": "3. Surcharge inverse Omicron (ο) au-dessus d'Alpha (α) dans le démonstratif",
                "subtitle": "f. 172v, v. 844 — ἀφαιρεῖσθαι τοδὶ (R1 avait écrit ταδὶ, corrigé par ο supralinéaire)",
                "src": SPEC11,
                "crop": (485, 432, 1475, 525),
                "max_h": 185,
                "boxes": [
                    (1350, 445, 1455, 515, "τ[ὰ->ο]δὶ (ο au-dessus de α)", "red"),
                ],
                "diplo": "χρήματα δανείζων· ἀφαιρεῖσθαι τ[ὰ s.l. ο]δὶ·",
                "edit": "... ἀφαιρεῖσθαι τοδί (v. 844 : « ... qu'on lui retire ceci »)",
                "analyse": "Preuve que la confusion α <-> ο fonctionne dans les deux sens : cinq lignes sous ὑστέρ[ο->α]ν, le scribe a commis la faute inverse τὰδὶ, corrigée par un petit omicron (ο) suspendu au-dessus de l'alpha.",
            },
            {
                "title": "4. Surcharge de consonnes rondes et sifflantes : ἀσπίδας refait sur ἁψῖδας",
                "subtitle": "f. 163r, v. 53 — κάμπτει δὲ νέας ἁψῖδας ἐπῶν (corrigé en ἀσπίδας dans R)",
                "src": SPEC03,
                "crop": (200, 512, 900, 598),
                "max_h": 185,
                "boxes": [
                    (560, 530, 740, 580, "ἀσπίδας (σπ refait sur ψ)", "red"),
                ],
                "diplo": "κάμπτει δὲ νέας ἀσπίδας [ex ἁψῖδας] ἐπῶν·",
                "edit": "Κάμπτει δὲ νέας ἁψῖδας ἐπῶν (v. 53 : « Il cintre de nouvelles voûtes [ἁψῖδας] de vers » — banalisé en ἀσπίδας « boucliers »).",
                "analyse": "La métaphore rare du charron (ἁψῖδας « jantes / voûtes ») a été banalisée par surcharge de la ligature ronde σπ sur le ψ initial, produisant le contresens militaire ἀσπίδας (« boucliers »).",
            },
        ],
    ]
    render_standard_plate(
        "08_piege4_lettres_rondes_alpha_omicron_omega_theta_sigma.jpg",
        "PLANCHE 08 — PIÈGE N° 4 : LES LETTRES RONDES (α, ο, ω, ε, θ, σ) ET LEURS SURCHARGES",
        "Maîtriser les échanges fréquents entre voyelles et consonnes circulaires de la zone médiane Z2",
        rows,
        "RÈGLE D'OR N° 4 (VIGILANCE SUR LES RONDES α / ο / ω)",
        "Dans la minuscule du Xe siècle, alpha (α), omicron (ο) et oméga fermé (ω en ∞) ne diffèrent souvent que d'un demi-millimètre de trait. Regardez toujours au-dessus de la ligne (zone Z3) : R2 y corrige très souvent un ο en α (ou un α en ο) par une minuscule lettre supralinéaire.",
    )


def gen_plate_09():
    rows = [
        [
            {
                "title": "1. Potences (τ, γ, π) et calembour homographique : Ἀγάθων (v. 30) vs ἀγαθῶν (v. 31)",
                "subtitle": "f. 162v, vv. 30–31 — Absence totale de majuscules aux noms propres dans la colonne R1",
                "src": SPEC02,
                "crop": (420, 235, 1260, 405),
                "max_h": 210,
                "boxes": [
                    (475, 252, 745, 298, "τραγωιδοποιός (potences τ, γ, π)", "blue"),
                    (1080, 252, 1205, 298, "ἀγάθων (v. 30 = Ἀγάθων)", "blue"),
                    (590, 342, 725, 388, "ἀγάθων (v. 31 = ἀγαθῶν !)", "red"),
                ],
                "diplo": "ὁ τραγωιδοποιός· ποῖος οὗτος ἀγάθων· / ἔστιν τις ἀγάθων· — μῶν ὁ μέλας ὁ καρτερ@·",
                "edit": "Ὁ τραγῳδοποιός. — Ποῖος οὗτος Ἀγάθων; / Ἔστιν τις ἀγαθῶν; (vv. 30–31 : « Quel Agathon ? Y a-t-il quelqu'un parmi les braves... »)",
                "analyse": "Comme R1 n'emploie jamais de majuscule pour les noms propres, Ἀγάθων (v. 30) et le génitif pluriel ἀγαθῶν (v. 31) sont écrits de manière strictement identique (ἀγάθων avec accent aigu !). Notez aussi dans τραγωιδοποιός l'alignement des potences τ, γ et π sur Z1.",
            },
            {
                "title": "2. Potences (τ, π), sifflante plongeante (ζ) et coupe des mots en semi-continua",
                "subtitle": "f. 163v, v. 100 — μύρμηκος ἀτραπούς, ἢ τί διαμινυρίζεται;",
                "src": SPEC04,
                "crop": (580, 895, 1470, 980),
                "max_h": 210,
                "boxes": [
                    (630, 915, 1035, 962, "μύρμηκος ἀτραπούς (potences τ, π)", "red"),
                    (1145, 915, 1455, 962, "διαμινυρίζεται (ζ plongeant)", "blue"),
                ],
                "diplo": "μύρμηκος ἀτραπούς· ἢ τί διαμινυρίζεται·",
                "edit": "Μύρμηκος ἀτραπούς, ἢ τί διαμινυρίζεται; (v. 100 : « Les sentiers de la fourmi ! Ou que fredonne-t-il là ? »)",
                "analyse": "Dans ἀτραπούς, la barre horizontale du τ se soude à la boucle du ρ et celle du π coiffe l'omicron. À la fin du vers, διαμινυρίζεται montre le grand éclair sinueux du zêta (ζ) plongeant en Z4.",
            },
        ],
        [
            {
                "title": "3. Serpentin plongeant (ξ) et corruption d'un nom propre rare (Χοιρίλ' -> χοῖρον)",
                "subtitle": "f. 165v, vv. 288–289 — ξυνεύχου... καὶ τὴν θυγατέρα Χοιρίον (écrit χοῖρον dans R)",
                "src": SPEC06,
                "crop": (640, 545, 1700, 680),
                "max_h": 200,
                "boxes": [
                    (1050, 560, 1245, 612, "ξυνεύχου (ξ serpentin Z4)", "blue"),
                    (1090, 612, 1225, 665, "χοῖρον (faute pour Χοιρίον)", "red"),
                ],
                "diplo": "καὶ τὴν θυγατέρα χοῖρον ἀνδρός μοι τυχεῖν",
                "edit": "Καὶ τὴν θυγατέρα Χοιρίον ἀνδρός μοι τυχεῖν (v. 289 : « Et que ma fille Khoirion [Cunégonde] me trouve un mari »)",
                "analyse": "Faute de majuscule distinctive pour signaler l'hypocoristique féminin Χοιρίον (diminutif comique de χοῖρος), la tradition a banalisé le nom propre de la fille de Mnésiloque en nom commun χοῖρον (« cochon de lait »). Au vers précédent, notez le beau ξ serpentin initial de ξυνεύχου.",
            },
            {
                "title": "4. Potence du Pi (π) et nom mythologique sans majuscule : τὴν καινὴν Ἑλένην",
                "subtitle": "f. 172v, vv. 852–853 — τὴν δ' αὖ κορωνὴν πικρὰν ἑλένην",
                "src": SPEC11,
                "crop": (460, 785, 1380, 905),
                "max_h": 200,
                "boxes": [
                    (520, 842, 660, 895, "πικρὰν (π à potence Z1)", "blue"),
                    (670, 842, 795, 895, "ἑλένην (= Ἑλένην sans majuscule)", "red"),
                ],
                "diplo": "τί οὐκ ἄγεις / τὴν δ' αὖ κορωνὴν πικρὰν ἑλένην·",
                "edit": "... τὴν καινὴν Ἑλένην (v. 853 : « ... sa nouvelle Hélène ! » — corrompu en κορωνὴν πικρὰν ἑλένην dans R).",
                "analyse": "Le titre de la tragédie d'Euripide (Ἑλένην) s'écrit en minuscules ordinaires (ἑλένην) avec deux êta en « h » encadrant le lambda diagonal. Juste avant, πικρὰν illustre le pi minuscule fermé à potence horizontale.",
            },
        ],
    ]
    render_standard_plate(
        "09_piege5_potences_gamma_pi_tau_et_zeta_xi_psi.jpg",
        "PLANCHE 09 — PIÈGE N° 5 : POTENCES (γ, π, τ), PLONGEANTES (ζ, ξ) ET NOMS PROPRES EN CONTINUA",
        "Lire les lettres suspendues à barre horizontale et déjouer l'absence de majuscules aux noms propres",
        rows,
        "RÈGLE D'OR N° 5 (POTENCES & NOMS PROPRES)",
        "Trois consonnes pendent sous une barre horizontale en Z1 : TAU (τ, fût droit court), GAMMA (γ, long fût plongeant en Z4) et PI (π, double jambage). Rappelez-vous en outre que R1 n'utilise JAMAIS de majuscule pour marquer les noms propres (Ἀγάθων, Ἑλένη, Εὐριπίδης).",
    )


def gen_plate_10():
    rows = [
        [
            {
                "title": "1. La spirale tachygraphique finale en « @ » pour la désinence -ός (καρτερός)",
                "subtitle": "f. 162v, v. 31 — μῶν ὁ μέλας ὁ καρτερ(ός)",
                "src": SPEC02,
                "crop": (420, 325, 1250, 405),
                "max_h": 185,
                "boxes": [
                    (1180, 342, 1228, 388, "Spirale @ = -ός (καρτερ@)", "red"),
                ],
                "diplo": "ἔστιν τις ἀγάθων· — μῶν ὁ μέλας ὁ καρτερ@·",
                "edit": "Μῶν ὁ μέλας, ὁ καρτερός; (v. 31 : « Serait-ce le brun, le costaud ? »)",
                "analyse": "En fin de vers, pour économiser l'espace, R1 remplace la syllabe finale -ός par un grand cercle enroulé en colimaçon autour d'un noyau central (identique à notre arobase @), surmonté de l'accent aigu.",
            },
            {
                "title": "2. Fausse résolution mécanique de la spirale finale : Ξένυλλα changé en ξενύλλ(ος) !",
                "subtitle": "f. 170r, v. 636 — ξενύλλ@ αἴτησον σκάφην",
                "src": SPEC09,
                "crop": (120, 245, 920, 325),
                "max_h": 185,
                "boxes": [
                    (135, 260, 265, 312, "ξενύλλ@ (faute pour Ξένυλλα !)", "red"),
                ],
                "diplo": "ξενύλλ@ αἴτησον σκάφην· ἢν δ' ἀρνῆται",
                "edit": "Ξένυλλ', αἴτησον σκάφην (v. 636 : « Xénylla, demande un bassin ! »)",
                "analyse": "Habitué à abréger les masculins en -ος par la spirale @, le copiste a machinalement affublé le vocatif féminin élidé Ξένυλλ(α) de la spirale masculine -ος (ξενύλλ@), créant un monstre grammatical !",
            },
        ],
        [
            {
                "title": "3. Spirale finale -ος en fin de didascalie scénique (ἀπεψωλημένος)",
                "subtitle": "f. 176v, après le v. 1187 — ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν(ος)·",
                "src": SPEC15,
                "crop": (550, 125, 1480, 205),
                "max_h": 185,
                "boxes": [
                    (1388, 138, 1445, 190, "Spirale @ = -ος (ἀπεψωλημέν@)", "red"),
                ],
                "diplo": "ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν@·",
                "edit": "[Παρεπιγραφή 4] Ἀνακύπτει καὶ παρακύπτει ἀπεψωλημένος (« Il dresse la tête et se penche de côté, le gland décalotté »).",
                "analyse": "À l'extrême droite de la quatrième parépigraphe scénique, le participe ἀπεψωλημένος se termine par une grande spirale @ directement issue du jambage droit du nu (ν).",
            },
            {
                "title": "4. L'idéogramme astronomique du Soleil (☉ = ἥλιος) dans la scholie face au texte",
                "subtitle": "f. 162v, v. 17 et Σ v. 17 — ☉ (= ἡλίωι) dans la marge R2 face à ἡλίου en toutes lettres dans R1",
                "src": F162V,
                "crop": (380, 1125, 1460, 1205),
                "max_h": 185,
                "boxes": [
                    (515, 1142, 555, 1188, "Idéogramme ☉ = ἡλίωι (Σ R2)", "red"),
                    (1195, 1142, 1315, 1192, "ἡλίου en toutes lettres (R1)", "blue"),
                ],
                "diplo": "[Σ R2] ὁμοί(ως) δὲ τῶι ☉ [= ἡλίωι] τὸ περιφερές // [R1 v. 17] ὀφθαλμὸν ἀντίμιμον ἡλίου τροχῶι·",
                "edit": "Σ 17 : Ὁμοίως δὲ τῷ ἡλίῳ τὸ περιφερές // v. 17 : Ὀφθαλμὸν ἀντίμιμον ἡλίου τροχῷ (« L'œil imitant la roue du soleil »).",
                "analyse": "NE CONFONDEZ JAMAIS les deux cercles : dans le texte R1 (à droite, bleu), ἡλίου est écrit en toutes lettres ; mais dans la scholie marginale R2 (à gauche, rouge), le mot ἡλίωι est remplacé par l'idéogramme astronomique antique du Soleil (☉ : cercle centré d'un point et coiffé d'un rayon) !",
            },
        ],
    ]
    render_standard_plate(
        "10_piege6_spirale_finale_os_vs_soleil_helios.jpg",
        "PLANCHE 10 — PIÈGE N° 6 : LA SPIRALE FINALE -ΟΣ (@) CONTRE L'IDÉOGRAMME DU SOLEIL (☉)",
        "Distinguer la boucle tachygraphique de fin de mot (-ος) et le symbole astronomique solaire des scholies",
        rows,
        "RÈGLE D'OR N° 6 (SPIRALE @ VS SOLEIL ☉)",
        "Un cercle enroulé en colimaçon (@) attaché à la dernière consonne d'un mot vaut TOUJOURS la finale -ος (ou -ον). Au contraire, un cercle isolé centré d'un point et muni d'un rayon oblique (☉) dans une scholie est l'idéogramme savant du Soleil (ἥλιος / ἡλίῳ).",
    )


def gen_plate_11():
    rows = [
        [
            {
                "title": "1. Ligature ει (epsilon + iota) : tête d'as de pique et trait vertical plongeant",
                "subtitle": "f. 162v, v. 2 — ἀπολεῖ μ' ἀλοῶν ἅνθρωπος",
                "src": F162V,
                "crop": (730, 478, 1085, 550),
                "max_h": 185,
                "boxes": [
                    (820, 488, 898, 538, "lig. λει (ἀπολεῖ)", "red"),
                ],
                "diplo": "ἀπολεῖ μ' ἀλοῶν ἅνθρωπος ἐξ ἑωθινοῦ·",
                "edit": "Ἀπολεῖ μ' ἁλοῶν ἄνθρωπος ἐξ ἑωθινοῦ (v. 2 : « Cet homme va me tuer à me tourner en rond depuis l'aube ! »)",
                "analyse": "Dans la diphtongue -εῖ de ἀπολεῖ, la boucle supérieure de l'epsilon monte au-dessus de la ligne, se referme en pointe (« as de pique ») et redescend verticalement pour former l'iota sans que le calame quitte le parchemin.",
            },
            {
                "title": "2. Ligature ἐξ (epsilon + xi) : l'as de pique greffé au sommet du serpentin",
                "subtitle": "f. 162v, v. 2 — ἐξ ἑωθινοῦ",
                "src": F162V,
                "crop": (1180, 478, 1525, 550),
                "max_h": 185,
                "boxes": [
                    (1302, 488, 1342, 542, "lig. ἐξ (ε + ξ vertical)", "red"),
                ],
                "diplo": "... ἅνθρωπος ἐξ ἑωθινοῦ·",
                "edit": "... ἐξ ἑωθινοῦ (v. 2 : « ... depuis l'aube »)",
                "analyse": "La préposition ἐξ forme un monogramme vertical spectaculaire : la tête haute de l'epsilon (coiffée de l'esprit doux) ne redescend pas sur la ligne de base mais s'enchaîne directement au triple zig-zag plongeant du xi (ξ).",
            },
        ],
        [
            {
                "title": "3. Ligature τερ (tau + epsilon + rhô) : pont continu sous potence",
                "subtitle": "f. 162v, v. 31 — μῶν ὁ μέλας ὁ καρτερ(ός)",
                "src": SPEC02,
                "crop": (420, 325, 1250, 405),
                "max_h": 185,
                "boxes": [
                    (1132, 342, 1185, 388, "lig. τερ (καρτερ@)", "red"),
                ],
                "diplo": "μῶν ὁ μέλας ὁ καρτερ@·",
                "edit": "Μῶν ὁ μέλας, ὁ καρτερός; (v. 31)",
                "analyse": "Dans la syllabe -τερ- de καρτερός, la barre du tau (τ) alimente la boucle haute de l'epsilon (ε), dont la sortie inférieure s'enroule immédiatement pour tracer l'anneau et la queue plongeante du rhô (ρ).",
            },
            {
                "title": "4. Double ligature τερ + εσ sur une même ligne (θυγατέρα et ἄνδρες)",
                "subtitle": "f. 165v, vv. 289–290 — καὶ τὴν θυγατέρα χοῖρον ἀνδρός μοι τυχεῖν",
                "src": SPEC06,
                "crop": (640, 595, 1700, 680),
                "max_h": 185,
                "boxes": [
                    (920, 612, 1080, 665, "θυγατέρα (lig. τερ)", "red"),
                ],
                "diplo": "καὶ τὴν θυγατέρα χοῖρον ἀνδρός μοι τυχεῖν",
                "edit": "Καὶ τὴν θυγατέρα Χοιρίον ἀνδρός μοι τυχεῖν (v. 289)",
                "analyse": "Dans θυγατέρα, le groupe -τέρα- montre l'enchaînement canonique de l'epsilon en as de pique entre la potence du τ et la boucle plongeante du ρ.",
            },
        ],
    ]
    render_standard_plate(
        "11_ligatures_epsilon_as_de_pique_ei_ex_er_es_et.jpg",
        "PLANCHE 11 — LES LIGATURES D'EPSILON EN « AS DE PIQUE » (ει, εξ, ερ, εσ, ετ)",
        "Comprendre comment l'epsilon (ε) se déforme par le haut pour s'articuler avec la consonne ou voyelle suivante",
        rows,
        "RÈGLE DE DÉCHIFFREMENT DES LIGATURES EN Ε-",
        "Chaque fois que vous voyez une petite boucle pointue perchée en zone haute (Z3) au-dessus d'un trait vertical (ι), d'un serpentin (ξ) ou d'un rhô (ρ), ne cherchez pas une lettre rare : c'est la tête haute d'un EPSILON en « as de pique » (ει, εξ, ερ, εσ, ετ).",
    )


def gen_plate_12():
    rows = [
        [
            {
                "title": "1. Ligature σπ (sigma + pi) : casquette du sigma soudée à la potence du pi",
                "subtitle": "f. 162v, v. 3 — οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "src": F162V,
                "crop": (950, 525, 1345, 598),
                "max_h": 185,
                "boxes": [
                    (1035, 540, 1078, 585, "lig. σπ (σπλῆνα)", "red"),
                ],
                "diplo": "οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "edit": "Οἷόν τε, πρὶν τὸν σπλῆνα κομιδῇ μ' ἐκβαλεῖν (v. 3)",
                "analyse": "Dans σπλῆνα, la panse ronde du sigma (σ) projette sa casquette supérieure horizontalement sur Z1 pour former d'un seul trait la barre de tête du pi (π), immédiatement suivie du lambda (λ) et de l'êta en h (ῆ).",
            },
            {
                "title": "2. Ligature στ (sigma + tau) : arche unique unissant la panse du σ et le fût du τ",
                "subtitle": "f. 163v, v. 80 — ἐπεὶ τρίτη 'στὶ Θεσμοφορίων ἡ μέση",
                "src": SPEC04,
                "crop": (590, 5, 1300, 78),
                "max_h": 185,
                "boxes": [
                    (830, 15, 885, 65, "lig. στ ('στὶ)", "red"),
                ],
                "diplo": "ἐπεὶ τρίτη 'στὶ θεσμοφορίων ἡ μέση·",
                "edit": "Ἐπεὶ τρίτη 'στὶ Θεσμοφορίων ἡ μέση (v. 80)",
                "analyse": "La ligature στ (notre ancien « ϛ » ou « st » typographique) est indissociable dans R1 : le dôme supérieur du sigma monte en Z3 puis redescend tout droit former la hampe verticale du tau.",
            },
        ],
        [
            {
                "title": "3. Ligature σθ (sigma + thêta) : enchaînement de la casquette du σ dans la boucle du θ",
                "subtitle": "f. 162v, v. 4 — παρὰ σοῦ πυθέσθαι ποῖ μ' ἄγεις ὠὐριπίδη",
                "src": F162V,
                "crop": (830, 575, 1295, 645),
                "max_h": 185,
                "boxes": [
                    (1002, 585, 1045, 634, "lig. σθ (πυθέσθαι)", "red"),
                ],
                "diplo": "παρὰ σοῦ πυθέσθαι ποῖ μ' ἄγεις ὠὐριπίδη·",
                "edit": "Παρὰ σοῦ πυθέσθαι ποῖ μ' ἄγεις, ὠὐριπίδη; (v. 4 : « D'apprendre de toi où tu me mènes, Euripide ? »)",
                "analyse": "Extrêmement fréquente dans toutes les désinences médio-passives en -σθαι / -σθε / -σθω, la ligature σθ soude l'anneau bas du sigma au grand ovale vertical du thêta (θ).",
            },
            {
                "title": "4. Ligatures σθ et σκ côte à côte (καθῆσθαι σκάφιον)",
                "subtitle": "f. 172v, v. 838 — ὑστέραν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην",
                "src": SPEC11,
                "crop": (650, 145, 1480, 235),
                "max_h": 185,
                "boxes": [
                    (852, 155, 922, 208, "lig. σθ (καθῆσθαι)", "blue"),
                    (972, 152, 1045, 208, "lig. σκ (σκάφιον)", "red"),
                ],
                "diplo": "... αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην",
                "edit": "... αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην (v. 838)",
                "analyse": "Après la ligature -σθ- de καθῆσθαι, l'initiale de σκάφιον montre comment la casquette du sigma s'élève vers la haute hampe du kappa (κ) avant de redescendre tracer son accolade.",
            },
        ],
    ]
    render_standard_plate(
        "12_ligatures_sigma_sp_st_sth_sk_sch.jpg",
        "PLANCHE 12 — LES LIGATURES DU SIGMA À CASQUETTE (σπ, στ, σθ, σκ, σχ)",
        "Identifier les groupes consonantiques soudés sous la casquette horizontale du sigma minuscule",
        rows,
        "RÈGLE DE DÉCHIFFREMENT DES GROUPES EN Σ-",
        "Dans la minuscule bouletée, le sigma (σ) ne reste presque jamais isolé devant une consonne : sa casquette supérieure sert de tremplin horizontal pour coiffer π (σπ) et τ (στ), ou s'accrocher au flanc des lettres hautes θ (σθ) et κ (σκ).",
    )


def gen_plate_13():
    rows = [
        [
            {
                "title": "1. Ligature αλ / αλλ : le dard de l'alpha enchaîné à la grande arche du lambda",
                "subtitle": "f. 162v, v. 3 — οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "src": F162V,
                "crop": (1195, 525, 1565, 598),
                "max_h": 185,
                "boxes": [
                    (1445, 538, 1498, 585, "lig. αλ (ἐκβαλεῖν)", "red"),
                ],
                "diplo": "... κομιδῆι μ' ἐκβαλεῖν",
                "edit": "... κομιδῇ μ' ἐκβαλεῖν (v. 3)",
                "analyse": "Dans ἐκβαλεῖν, après le bêta bilobé (β), la panse de l'alpha (α) lance son trait de sortie vers le haut pour attaquer directement la longue diagonale descendante du lambda (λ).",
            },
            {
                "title": "2. Ligatures τρ (tau + rhô) et γωι (gamma + oméga + iota adscrit) dans τραγωιδοποιός",
                "subtitle": "f. 162v, v. 30 — ὁ τραγωιδοποιός· ποῖος οὗτος ἀγάθων",
                "src": SPEC02,
                "crop": (420, 238, 1250, 312),
                "max_h": 185,
                "boxes": [
                    (475, 252, 522, 298, "lig. τρ (τραγ-)", "red"),
                    (540, 252, 608, 298, "lig. γωι (-γωι-)", "blue"),
                ],
                "diplo": "ὁ τραγωιδοποιός· ποῖος οὗτος ἀγάθων·",
                "edit": "Ὁ τραγῳδοποιός. — Ποῖος οὗτος Ἀγάθων; (v. 30)",
                "analyse": "Ce mot-clé du théâtre comique montre deux ligatures sous potence : dans τρ-, la boucle du rhô pend sous la barre du tau ; dans -γωι-, la potence du gamma coiffe l'oméga suivi de l'iota adscrit.",
            },
        ],
        [
            {
                "title": "3. Le double Lambda géminé (λλ) en arche imbriquée dans la conjonction ἀλλ'",
                "subtitle": "f. 162v, v. 35 — ἀλλ' ἐκποδὼν πτήξωμεν",
                "src": SPEC02,
                "crop": (420, 445, 1250, 525),
                "max_h": 185,
                "boxes": [
                    (842, 462, 910, 512, "lig. λλ (ἀλλ')", "red"),
                ],
                "diplo": "... ἀλλ' ἐκποδὼν...",
                "edit": "... ἀλλ' ἐκποδὼν πτήξωμεν (v. 36 : « Mais mettons-nous vite à l'abri ! »)",
                "analyse": "Lorsque deux lambda se suivent (λλ), R1 ne trace pas deux lettres séparées : le premier lambda forme une petite arche nichée sous la grande diagonale plongeante du second lambda.",
            },
            {
                "title": "4. Contraste en miroir entre double Lambda (-λλ-) et simple Lambda (-λ-) dans la scène d'Écho",
                "subtitle": "f. 175r, vv. 1073–1074 — στωμυλλομένη (v. 1073, -λλ-) vs στωμυλομένη (v. 1074, -λ-)",
                "src": SPEC13,
                "crop": (220, 835, 1150, 955),
                "max_h": 195,
                "boxes": [
                    (605, 852, 945, 900, "στωμυλλομένη (-λλ- géminé v. 1073)", "red"),
                    (305, 900, 575, 945, "στωμυλομένη (-λ- simple v. 1074)", "blue"),
                ],
                "diplo": "[v. 1073] ὦ γραῦ στωμυλλομένη σὺ· / [v. 1074] ἠχ(ώ) — στωμυλομένη σὺ·",
                "edit": "Ὦ γραῦ, στωμυλλομένη σύ. — Στωμυλλομένη σύ (vv. 1073–1074 : « Ô vieille bavarde ! »)",
                "analyse": "Comparaison idéale sur deux lignes consécutives : au v. 1073 (rouge), Mnésiloque a le double -λλ- en arche imbriquée (στωμυλλομένη), tandis qu'en répétant le mot au v. 1074 (bleu), le copiste a simplifié par haplographie en un seul -λ- (στωμυλομένη).",
            },
        ],
    ]
    render_standard_plate(
        "13_ligatures_alpha_tau_gamma_rho_et_double_lambda.jpg",
        "PLANCHE 13 — LIGATURES D'ALPHA, POTENCES SUR RHÔ (τρ, γρ) ET DOUBLE LAMBDA (λλ)",
        "Décoder les groupes liés αλ, τρ, γρ et reconnaître d'un coup d'œil l'arche imbriquée du double lambda (-λλ-)",
        rows,
        "RÈGLE DE DÉCHIFFREMENT DU DOUBLE LAMBDA (λλ)",
        "Ne prenez jamais le groupe -λλ- (dans ἀλλά, ἄλλος, μᾶλλον, βάλλω, στωμυλλομένη) pour un M ou un H : le premier lambda est réduit à une petite jambe courbe abritée sous le grand toit diagonal du second lambda.",
    )


def gen_plate_14():
    rows = [
        [
            {
                "title": "1. Adscription constante à la finale dative féminine en -ῆι (κομιδῆι = κομιδῇ)",
                "subtitle": "f. 162v, v. 3 — οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "src": F162V,
                "crop": (1035, 525, 1450, 598),
                "max_h": 185,
                "boxes": [
                    (1198, 535, 1346, 588, "κομιδῆι (-ῆι = -ῇ)", "red"),
                ],
                "diplo": "οἷόν τε πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν",
                "edit": "Οἷόν τε, πρὶν τὸν σπλῆνα κομιδῇ μ' ἐκβαλεῖν (v. 3)",
                "analyse": "Le Ravennas 429 ignore totalement l'iota souscrit moderne (inventé au XIIe siècle) : dans κομιδῆι, l'iota muet (ι) est écrit sur la ligne, de plain-pied à droite de l'êta circonflexe (ῆ).",
            },
            {
                "title": "2. Adscription interne dans le radical nominal : τραγωιδοποιός (= τραγῳδοποιός)",
                "subtitle": "f. 162v, v. 30 — ὁ τραγωιδοποιός· ποῖος οὗτος ἀγάθων",
                "src": SPEC02,
                "crop": (420, 238, 1250, 312),
                "max_h": 185,
                "boxes": [
                    (475, 252, 745, 298, "τραγωιδοποιός (-ωι- = -ῳ-)", "red"),
                ],
                "diplo": "ὁ τραγωιδοποιός· ποῖος οὗτος ἀγάθων·",
                "edit": "Ὁ τραγῳδοποιός. — Ποῖος οὗτος Ἀγάθων; (v. 30)",
                "analyse": "Même au milieu d'un mot composé, la diphtongue longue de τραγῳδοποιός est notée -ωι- sur la ligne de base (oméga suivi d'un iota droit).",
            },
        ],
        [
            {
                "title": "3. Adscription au datif masculin singulier en -ωι : ψόγωι (= ψόγῳ)",
                "subtitle": "f. 173r, v. 895 — βάλλουσα ψόγωι",
                "src": SPEC12,
                "crop": (250, 25, 950, 110),
                "max_h": 185,
                "boxes": [
                    (700, 40, 905, 102, "ψόγωι (-ωι = -ῳ)", "red"),
                ],
                "diplo": "... βάλλουσα ψόγωι",
                "edit": "... βάλλουσα ψόγῳ (v. 895 : « ... en me couvrant de blâme »)",
                "analyse": "Dans ψόγωι (qui commence par un beau psi caliciforme ψ), la désinence de datif -ωι aligne l'oméga fermé et l'iota final sur le même niveau Z2.",
            },
            {
                "title": "4. Double datif en -ωι sur une même ligne : τῶι κηρίωι (= τῷ κηρίῳ)",
                "subtitle": "f. 168r, v. 506 — τὸ δ' εἰσέφερε γραῦς ἐν χύτραι τῶι κηρίωι",
                "src": SPEC08,
                "crop": (140, 805, 900, 895),
                "max_h": 185,
                "boxes": [
                    (365, 828, 535, 880, "κηρίωι (= κηρίῳ v. 506)", "red"),
                ],
                "diplo": "... ἐν χύτραι τῶι κηρίωι",
                "edit": "... ἐν χύτρᾳ τῷ κηρίῳ (v. 506 : « ... dans une marmite avec un rayon de miel »)",
                "analyse": "Ce vers aligne trois datifs adscrits consécutifs (χύτραι τῶι κηρίωι). Ne confondez jamais cet iota muet adscrit (après voyelle longue ᾱ, η, ω) avec le déictique comique tonique -ί (ὁδί, τουτί, ταυτί).",
            },
        ],
    ]
    render_standard_plate(
        "14_regle_iota_muet_adscrit_et_piege_deictique.jpg",
        "PLANCHE 14 — LA RÈGLE DE L'IOTA MUET ADSCRIT (-ᾶι, -ῆι, -ῶι) ET LE PIÈGE DU DÉICTIQUE (-ί)",
        "Comprendre pourquoi aucun iota n'est souscrit au Xe siècle et éviter les contresens morphologiques",
        rows,
        "RÈGLE D'OR SUR L'IOTA ADSCRIT",
        "Dans le Ravennas 429, l'iota muet n'est JAMAIS souscrit sous la voyelle : il est adscrit à sa droite (-ᾶι, -ῆι, -ῶι = -ᾳ, -ῃ, -ῳ). Avant de lire un nominatif pluriel en -αι/-οι ou un déictique en -ί, vérifiez toujours si la voyelle précédente est longue (ᾱ, η, ω).",
    )


def gen_plate_15():
    rows = [
        [
            {
                "title": "1. Combinaison d'esprit et de circonflexe (ὦ) et double accentuation d'enclise (ἆρά ποτε)",
                "subtitle": "f. 162v, v. 1 — ὦ ζεῦ· χελιδὼν ἆρά ποτε φανήσεται",
                "src": F162V,
                "crop": (685, 425, 1220, 504),
                "max_h": 185,
                "boxes": [
                    (692, 432, 742, 490, "ὦ (esprit doux + circ.)", "red"),
                    (1038, 438, 1118, 492, "ἆρά (circ. + aigu d'enclise)", "blue"),
                ],
                "diplo": "ὦ ζεῦ· χελιδὼν ἆρά ποτε φανήσεται·",
                "edit": "Ὦ Ζεῦ, χελιδὼν ἆρά ποτε φανήσεται; (v. 1)",
                "analyse": "Dès le premier vers, R1 montre sa maîtrise prosodique : sur ὦ, l'esprit doux est surmonté de l'arche du circonflexe ; sur ἆρά, l'alpha initial porte l'esprit et le circonflexe tandis que l'alpha final reçoit l'aigu d'enclise de ποτε.",
            },
            {
                "title": "2. Scriptio plena et accentuation maintenue devant voyelle : οὔκ ἀλλ'",
                "subtitle": "f. 162v, v. 32 — οὔκ ἀλλ' ἐς οἶκον",
                "src": SPEC02,
                "crop": (420, 372, 1250, 448),
                "max_h": 185,
                "boxes": [
                    (440, 388, 595, 438, "οὔκ ἀλλ' (aigu sur οὔκ)", "red"),
                ],
                "diplo": "ἑόρακας πώποτε· — οὔκ ἀλλ'...",
                "edit": "Οὔκ, ἀλλ'... (v. 32 : « Non, mais... »)",
                "analyse": "Conformément à la doctrine d'Hérodien, la négation οὔκ prise absolument en tête de réplique conserve son accent aigu devant la pause logique, suivie d'ἀλλ' élidé avec apostrophe.",
            },
        ],
        [
            {
                "title": "3. Le tréma organique byzantin (dialytika) sur upsilon : βαΰζα",
                "subtitle": "f. 173r, v. 895 — βαΰζα σὺ",
                "src": SPEC12,
                "crop": (15, 25, 680, 110),
                "max_h": 185,
                "boxes": [
                    (148, 40, 275, 98, "βαΰζα (tréma ϋ + aigu)", "red"),
                ],
                "diplo": "πρ(ύτανις) βαΰζα σὺ·",
                "edit": "Βάυζε σὺ (v. 895 : « Aboie donc, toi ! »)",
                "analyse": "R1 place un double point horizontal (tréma / dialytika) sur l'upsilon de βαΰζα (et sur l'iota d'Ἀΐδης) pour indiquer la diérèse ou isoler visuellement la cuvette étroite de la voyelle.",
            },
            {
                "title": "4. Scriptio plena non élidée dans une parépigraphe scénique : τε ἱερὸν ὠθεῖται",
                "subtitle": "f. 165v, après le v. 276 — ὀλολύζουσι τε ἱερὸν ὠθεῖται",
                "src": SPEC06,
                "crop": (600, 35, 1500, 125),
                "max_h": 185,
                "boxes": [
                    (770, 55, 1465, 105, "ὀλολύζουσι τε ἱερὸν ὠθεῖται (scriptio plena)", "red"),
                ],
                "diplo": "ὀλολύζουσι τε ἱερὸν ὠθεῖται",
                "edit": "[Παρεπιγραφή] Ὀλολύζουσί τε· τὸ ἱερὸν ὠθεῖται (« Elles poussent le cri rituel ; le sanctuaire est poussé en avant »).",
                "analyse": "Le scribe écrit en scriptio plena les mots séparés sans crase ni élision graphique (τε ἱερὸν ὠθεῖται), laissant au lecteur le soin d'opérer la synalèphe métrique dans les vers parlés.",
            },
        ],
    ]
    render_standard_plate(
        "15_esprits_accents_trema_et_scriptio_plena.jpg",
        "PLANCHE 15 — ESPRITS, ACCENTS, TRÉMA ANTIQUE (DIALYTIKA) ET SCRIPTIO PLENA",
        "Lire les signes prosodiques supralinéaires (zone Z3) et comprendre la notation pleine des élisions",
        rows,
        "RÈGLE DE LECTURE PROSODIQUE",
        "Dans le Ravennas, les esprits sont tantôt anguleux (⊢ / ⊣, héritage alexandrin), tantôt arrondis ; le tréma (ϊ, ϋ) surmonte librement ι et υ ; et la scriptio plena écrit souvent en toutes lettres la voyelle finale qu'il faut élider à la scansion.",
    )


def gen_plate_16():
    rows = [
        [
            {
                "title": "1. Le système combiné des changements d'interlocuteur : Paragraphos (—), Dikôlon (:) et Sigle",
                "subtitle": "f. 162v, vv. 6–9 — Alternance rapide entre Euripide et Mnésiloque au début du Prologue",
                "src": F162V,
                "crop": (680, 665, 1500, 855),
                "max_h": 215,
                "boxes": [
                    (705, 708, 748, 738, "Paragraphos marginale (—)", "red"),
                    (1052, 675, 1075, 718, "Dikôlon interne (:) v. 6", "red"),
                    (688, 755, 738, 805, "Sigle Μ[ν] + paragraphos", "blue"),
                ],
                "diplo": "[v. 6] ἀλλ' οὐκ ἀκούειν δεῖ σε πάνθ' ὅσ' αὐτίκα : ὄψει παρεστώς· / [—] πῶς λέγεις· αὖθις φράσον· / οὐκ ἀλλὰ κλύειν... / Μ[ν] — πῶς μοι παραινεῖς...",
                "edit": "ΕΥ. ... αὐτίκα / ὄψει παρεστώς. — ΜΝ. Πῶς λέγεις; αὖθις φράσον (vv. 6–7).",
                "analyse": "Trois outils coopèrent : (1) le dikôlon (:) à l'intérieur du vers signale une coupe ou fin de réplique ; (2) la paragraphos horizontale (—) sous le début du vers avertit que le locuteur a changé ; (3) le monogramme marginal (Μ[ν]) précise le nom du personnage.",
            }
        ],
        [
            {
                "title": "2. La Korônis d'articulation dramatique entre le Prologue et la Parodos",
                "subtitle": "f. 165v, après le v. 276 — Crochet d'oiseau stylisé marquant le changement de tableau scénique",
                "src": SPEC06,
                "crop": (590, 15, 1500, 140),
                "max_h": 185,
                "boxes": [
                    (600, 20, 680, 130, "Korônis scénique en marge gauche", "red"),
                ],
                "diplo": "[Κορωνίς] ὀλολύζουσι τε ἱερὸν ὠθεῖται",
                "edit": "[Fin du Prologue — Ouverture du Thesmophorion (v. 276/277)].",
                "analyse": "En marge gauche de la didascalie scénique, R1 trace une grande korônis formée d'une hampe verticale barrée d'un dard et surmontée d'une volute : c'est le signe alexandrin de changement de scène ou de structure métrique.",
            },
            {
                "title": "3. La grande Korônis ornementale de clôture finale de la comédie",
                "subtitle": "f. 177r, après le v. 1231 — Fin de l'Exodos des Thesmophories avant les Ecclésiazuses",
                "src": SPEC16,
                "crop": (60, 510, 1080, 685),
                "max_h": 185,
                "boxes": [
                    (65, 565, 1060, 675, "Grande korônis finale + trait de clôture", "red"),
                ],
                "diplo": "... ἀλλὰ τῆς ὁδοῦ / καλῶς τ' ἀνύσας· [Grande Korônis finale]",
                "edit": "... Ἀλλὰ τῆς ὁδοῦ... [Fin des Thesmophories, v. 1231].",
                "analyse": "Pour marquer l'explicit de la pièce entière, un immense paraphe horizontal traverse toute la colonne sous le v. 1231, articulé à gauche à une grande korônis ornementale.",
            },
        ],
    ]
    render_standard_plate(
        "16_signes_dialogue_paragraphos_dikolon_koronis.jpg",
        "PLANCHE 16 — LES SIGNES DE DIALOGUE ET DE STRUCTURE : PARAGRAPHOS, DIKÔLON, KORÔNIS",
        "Se repérer dans l'architecture théâtrale du manuscrit : répliques, changements d'interlocuteur et fins de scène",
        rows,
        "RÈGLE DE LECTURE DRAMATIQUE",
        "Attention : dans un manuscrit dramatique ancien, la paragraphos (—) et le dikôlon (:) suffisent souvent à indiquer un changement de locuteur sans que le nom du personnage soit répété ! L'absence de sigle marginal ne signifie donc jamais que le même acteur continue de parler.",
    )


def gen_plate_18():
    rows = [
        [
            {
                "title": "1. Le code tachygraphique de R2 dans une scholie complète : barre -ων (\\), lettres hautes et lemnisque (÷)",
                "subtitle": "f. 162v, Σ v. 1 (marge gauche) — Commentaire de R2 sur le proverbe de l'hirondelle",
                "src": F162V,
                "crop": (215, 375, 695, 655),
                "max_h": 225,
                "boxes": [
                    (505, 385, 565, 428, "\\ = -ων (ἐπὶ τῶν)", "red"),
                    (575, 428, 688, 475, "τ(ῶν) βαρ(βάρων) (suspensions)", "blue"),
                    (492, 558, 525, 592, "Lemnisque interne (÷)", "red"),
                ],
                "diplo": "ὦ ζεῦ χελιδών· ἐπὶ τῶ(ν)δ(ε) ἄσμε- / νος τὸ χελιδόνος ἔαρ ὥσπερ τ(ῶν) βαρ(βάρων)... / ... ἐπὶ τούτου ἀφίκετο ÷",
                "edit": "Σ 1 : Ὦ Ζεῦ χελιδών... ἐπὶ τούτου ἀφίκετο.",
                "analyse": "Ce bloc montre les trois réflexes de R2 : (1) un simple trait oblique descendant (\\) au-dessus du τ ou du ω note la finale de génitif pluriel -ων ; (2) les mots longs sont suspendus avec leur dernière consonne perchée en Z3 ; (3) le lemnisque (÷) clôt chaque note.",
            }
        ],
        [
            {
                "title": "2. Cascade de finales tachygraphiques en marge droite (-ων, -ας, -ης, -ου)",
                "subtitle": "f. 170r, Σ vv. 658–662 (marge droite) — Gloses de R2 sur la course des femmes autour de la Pnyx",
                "src": SPEC09,
                "crop": (990, 865, 1495, 1125),
                "max_h": 215,
                "boxes": [
                    (1030, 880, 1485, 1110, "Terminaisons hautes R2 (-ων, -ας, -ης)", "red"),
                ],
                "diplo": "τῶν ἐγκυκλίων ἀπο- / δυσαμένας ÷ / περιδραμεῖν ÷ / τὴν ἐκκλησίαν περὶ τ(ὴν) / πύκνα...",
                "edit": "Σ 658 : Τῶν ἐγκυκλίων ἀποδυσαμένας· περιδραμεῖν τὴν ἐκκλησίαν...",
                "analyse": "Lorsque R2 manque de place près du bord extérieur du folio, il empile les traits obliques et les sifflantes lunaires supralinéaires tout en séparant chaque sous-lemme par un tiret ou un lemnisque (÷).",
            },
            {
                "title": "3. Glose de variante lexicale et lemnisque final (÷) en marge gauche",
                "subtitle": "f. 165v, Σ v. 289 (marge gauche) — Glose marginale κύστον ἴσως αἰνίττεται ÷ face à χοῖρον",
                "src": SPEC06,
                "crop": (175, 610, 620, 765),
                "max_h": 215,
                "boxes": [
                    (198, 682, 368, 720, "κύστον ἴσως (glose R2)", "red"),
                    (200, 720, 360, 755, "αἰνίττεται ÷ (lemnisque)", "blue"),
                ],
                "diplo": "πρὸς τὸ τῆς θυγατρ(ὸς) / ὄνομα· κύστον ἴσως / αἰνίττεται ÷",
                "edit": "Σ 289 : Πρὸς τὸ τῆς θυγατρὸς ὄνομα· « κύσθον » ἴσως αἰνίττεται (« Il fait sans doute allusion au sexe féminin [κύσθος] »).",
                "analyse": "Dans cette glose marginale expliquant le double sens grivois de χοῖρον au v. 289, R2 suspend la finale de θυγατρ(ὸς) en fin de ligne 1 et clôt son explication à la ligne 3 par le lemnisque classique (÷).",
            },
        ],
    ]
    render_standard_plate(
        "18_tachygraphie_scholies_suspensions_et_finales.jpg",
        "PLANCHE 18 — LA TACHYGRAPHIE DES SCHOLIES (R2) : SUSPENSIONS, FINALES ET PONCTUATION",
        "Apprendre à développer les abréviations de la main scholiographique R2 dans les marges du manuscrit",
        rows,
        "MÉTHODE DE DÉVELOPPEMENT DES ABRÉVIATIONS R2",
        "Dans les marges de R2, ne lisez jamais un mot abrégé sans regarder au-dessus de sa dernière lettre écrite : un trait oblique (\\) = -ων ; un petit omicron/ou haut = -ου ; un c lunaire haut = -ης / -ας ; et le lemnisque (÷) marque la fin de chaque scholie.",
    )


def gen_plate_19():
    rows = [
        [
            {
                "title": "1. Première parépigraphe (avant le v. 100) : μινυρισμός (« fredonnement » d'Agathon)",
                "subtitle": "f. 163v, marge gauche face au v. 100 — Conservée par la scholie R2 : ἐν ἐνίοις δέ· μινυρισμός",
                "src": SPEC04,
                "crop": (130, 845, 1470, 1005),
                "max_h": 185,
                "boxes": [
                    (138, 930, 585, 995, "Σ R2 : ἐν ἐνίοις δέ· μινυρισμός", "red"),
                    (630, 915, 1460, 962, "v. 100 : μύρμηκος ἀτραπούς...", "blue"),
                ],
                "diplo": "[Σ R2] ἐν ἐνίοις δέ· μινυρισμός ÷ // [R1 v. 100] μύρμηκος ἀτραπούς· ἢ τί διαμινυρίζεται·",
                "edit": "[Παρεπιγραφή 1 : Μινυρισμός] — v. 100 : Μύρμηκος ἀτραπούς, ἢ τί διαμινυρίζεται;",
                "analyse": "La première didascalie musicale (« Fredonnement » d'Agathon préludant à son chant) est expressément attestée dans la marge gauche par R2 : « Dans certains exemplaires se trouve la note scénique : μινυρισμός ».",
            },
            {
                "title": "2. Deuxième parépigraphe (après le v. 129) : ὀλολύζει ὁ γέρων (« le vieillard pousse l'ololyge »)",
                "subtitle": "f. 164r, entre les vv. 129 et 130 — Copiée dans la colonne R1 et commentée en marge droite par R2",
                "src": SPEC05,
                "crop": (15, 135, 1480, 285),
                "max_h": 185,
                "boxes": [
                    (270, 145, 645, 195, "R1 : ὀλολύζει ὁ γέρων", "red"),
                    (995, 210, 1465, 265, "Σ R2 : ὀλολύζει· παρεπιγραφὴ...", "blue"),
                ],
                "diplo": "[R1] ὀλολύζει ὁ γέρων· // [Σ R2] ὀλολύζει· παρεπιγραφὴ ἐπὶ τῶι γέροντι ÷",
                "edit": "[Παρεπιγραφή 2] Ὀλολύζει ὁ γέρων (« Le vieillard [Mnésiloque] pousse un cri rituel strident »).",
                "analyse": "Copiée en pleine colonne par R1 comme s'il s'agissait d'un vers, cette indication de jeu d'acteur est aussitôt identifiée en marge droite par R2 sous son nom technique alexandrin : παρεπιγραφή (« note scénique intercalée »).",
            },
        ],
        [
            {
                "title": "3. Troisième parépigraphe (après le v. 276) : ὀλολύζουσι τε ἱερὸν ὠθεῖται",
                "subtitle": "f. 165v, après le v. 276 — Didascalie de machinerie théâtrale précédée d'une korônis",
                "src": SPEC06,
                "crop": (590, 15, 1500, 140),
                "max_h": 185,
                "boxes": [
                    (600, 25, 1465, 125, "Korônis + ὀλολύζουσι τε ἱερὸν ὠθεῖται", "red"),
                ],
                "diplo": "[Κορωνίς] ὀλολύζουσι τε ἱερὸν ὠθεῖται",
                "edit": "[Παρεπιγραφή 3] Ὀλολύζουσί τε· τὸ ἱερὸν ὠθεῖται (« Elles poussent le cri rituel ; le sanctuaire est poussé en avant »).",
                "analyse": "Document exceptionnel sur la machinerie du théâtre grec du Ve siècle : au début de l'assemblée des femmes, le décor du Thesmophorion est poussé en avant (ὠθεῖται) sur l'ekkyklèma au milieu des cris rituels.",
            },
            {
                "title": "4. Quatrième parépigraphe (après le v. 1187) : ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν(ος)·",
                "subtitle": "f. 176v, après le v. 1187 — Didascalie burlesque du jeu de la danseuse et du Scythe",
                "src": SPEC15,
                "crop": (550, 125, 1480, 205),
                "max_h": 185,
                "boxes": [
                    (585, 138, 1445, 190, "ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν@·", "red"),
                ],
                "diplo": "ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν@·",
                "edit": "[Παρεπιγραφή 4] Ἀνακύπτει καὶ παρακύπτει ἀπεψωλημένος (« Il dresse la tête et se penche de côté, le phallus décalotté »).",
                "analyse": "Quatrième et dernière parépigraphe scénique des Thesmophories (confirmée dès le IVe s. par P.Oxy. 3840 μ]ενο[), décrivant le jeu de scène muet de l'Archer scythe pendant la danse d'Élaphion.",
            },
        ],
    ]
    render_standard_plate(
        "19_les_quatre_parepigraphai_sceniques_antiques.jpg",
        "PLANCHE 19 — LES QUATRE PARÉPIGRAPHAI SCÉNIQUES ANTIQUES DES THESMOPHORIES",
        "Un trésor unique de l'histoire du théâtre grec : les quatre seules didascalies scéniques intégrales de l'Antiquité",
        rows,
        "IMPORTANCE PHILOLOGIQUE DES PARÉPIGRAPHAI",
        "Les Thesmophories du Ravennas 429 sont l'une des rarissimes pièces antiques à avoir conservé quatre indications scéniques (παρεπιγραφαί) remontant aux éditions alexandrines d'Aristophane de Byzance : elles prouvent que R1 copiait ces didascalies dans le corps même de la colonne.",
    )


def gen_plate_20():
    rows = [
        [
            {
                "title": "1. Chiffres de réordonnancement (α', γ', δ', β') et restitution d'un vers omis en marge (v. 33)",
                "subtitle": "f. 162v, vv. 28–34 — Double sauvetage philologique opéré par R2 sur une même page",
                "src": SPEC02,
                "crop": (390, 150, 1530, 505),
                "max_h": 245,
                "boxes": [
                    (1215, 160, 1250, 202, "α' (ordre 1)", "blue"),
                    (1212, 208, 1248, 250, "γ' (ordre 3)", "blue"),
                    (1202, 252, 1235, 295, "δ' (ordre 4)", "blue"),
                    (1232, 295, 1262, 340, "β' (ordre 2 : v. 28)", "red"),
                    (1150, 410, 1520, 500, "v. 33 restitué en marge par R2", "red"),
                ],
                "diplo": "[Fin des lignes] ... α' / ... γ' / ... δ' / ... β' // [Marge droite v. 33] μῶν ὁ δασυπώγων· — οὐχ ὁρᾶις πώποτε ÷",
                "edit": "Réordonnancement α' -> β' -> γ' -> δ' (vv. 27–30) et ajout marginal du v. 33 (Μῶν ὁ δασυπώγων; — Οὐχ ἑόρακας πώποτε;).",
                "analyse": "R1 avait copié le v. 28 après le v. 30 et sauté le v. 33 par saut du même au même (πώποτε / πώποτε). Sans rien gratter, R2 rétablit l'ordre exact par les chiffres α', β', γ', δ' à droite des vers et restitue le v. 33 complet dans la marge droite !",
            }
        ],
        [
            {
                "title": "2. Correction supralinéaire d'une préposition : κατὰ restitué au-dessus de καὶ",
                "subtitle": "f. 163r, v. 61 — συγγογγυλίσας καὶ [s.l. κατὰ] τοῦ θριγκοῦ",
                "src": SPEC03,
                "crop": (190, 820, 850, 905),
                "max_h": 195,
                "boxes": [
                    (505, 832, 592, 888, "κατὰ supralinéaire (au-dessus de καὶ)", "red"),
                ],
                "diplo": "τοῦ καλλιέπους· [s.l. κατὰ] καὶ τοῦ θριγκοῦ·",
                "edit": "... κατὰ τοῦ θριγκοῦ (v. 60/61 : « ... à travers la corniche »)",
                "analyse": "R1 avait banalisé la préposition κατὰ en conjonction καὶ ; le réviseur a écrit κατὰ en toutes lettres dans l'interligne supérieur juste au-dessus du καὶ fautif.",
            },
            {
                "title": "3. Signe de renvoi cruciforme (+÷) signalant l'ajout des vv. 1102–1103 en bas de page",
                "subtitle": "f. 175v, fin du v. 1101 — Stauros + lemnisque (+÷) renvoyant aux deux vers omis au bas du folio",
                "src": F175V,
                "crop": (760, 1175, 1790, 1255),
                "max_h": 195,
                "boxes": [
                    (780, 1190, 1625, 1242, "v. 1101 : ... ναυστολῶν τὸ γοργόν@", "blue"),
                    (1655, 1185, 1765, 1240, "Signe de renvoi +÷ (vers le bas du folio)", "red"),
                ],
                "diplo": "περσεὺς πρὸς ἄργος ναυστολῶν τὸ γοργόν@ · +÷",
                "edit": "Περσεὺς πρὸς Ἄργος ναυστολῶν τὸ Γοργόνος (v. 1101) + renvoi aux vv. 1102–1103 copiés dans la marge inférieure.",
                "analyse": "Lorsque l'omission dépasse un vers (ici les vv. 1102–1103 sautés par homéotéleute sur Γοργόνος), R2 place à droite du v. 1101 une croix flanquée d'un lemnisque (+÷) et copie les deux vers manquants au bas du folio avec le même signe d'appel.",
            },
        ],
    ]
    render_standard_plate(
        "20_chiffres_transposition_et_ajouts_marginaux_R2.jpg",
        "PLANCHE 20 — LES INTERVENTIONS DE RÉVISION (R2) : CHIFFRES DE TRANSPOSITION ET RENVOIS",
        "Comprendre comment le réviseur corrige les interversions de vers et répare les sauts du même au même",
        rows,
        "RÈGLE DE LECTURE DES SIGNES DE RÉVISION",
        "Des lettres grecques suivies d'une apostrophe (α', β', γ', δ') en fin de vers ne sont jamais des notes de musique : ce sont des numéros d'ordre rétablissant la succession logique de vers intervertis. Une croix suivie d'un lemnisque (+÷) renvoie toujours à un vers omis copié dans la marge.",
    )


def gen_plate_21():
    rows = [
        [
            {
                "title": "1. Type I — Correction de lettre unique sur grattage : βε[[α->β]]ίνηκας",
                "subtitle": "f. 162v, v. 35 — Bêta semi-oncial (« B ») récrit sur la fibre grattée d'un alpha fautif",
                "src": SPEC02,
                "crop": (420, 445, 1250, 525),
                "max_h": 185,
                "boxes": [
                    (570, 462, 760, 512, "βε[[α->β]]ίνηκας (B in rasura)", "red"),
                ],
                "diplo": "... βε[[α->β]]ίνηκας σὺ·",
                "edit": "... βεβίνηκας σύ (v. 35)",
                "analyse": "On distingue nettement le halo jaunâtre du parchemin gratté au canif sous le second bêta : pour couvrir la cicatrice fibreuse laissée par l'alpha effacé, le correcteur a tracé un grand Β semi-oncial.",
            },
            {
                "title": "2. Type II — Rubrique de personnage récrite sur grattage : [[κῆρυξ]] εὐφημί' ἔστω",
                "subtitle": "f. 166r, v. 295 — Le nom de la Héraut (κῆρυξ) substitué sur grattage en tête de vers",
                "src": SPEC07,
                "crop": (120, 40, 850, 135),
                "max_h": 185,
                "boxes": [
                    (222, 55, 300, 108, "[[κῆρυξ]] (sur grattage)", "red"),
                    (302, 55, 495, 108, "εὐφημί' ἔστω (texte R1)", "blue"),
                ],
                "diplo": "[[κῆρυξ]] εὐφημί' ἔστω· / εὐφημί' ἔστω·",
                "edit": "[ΚΗΡΥΞ] Εὐφημία 'στω, εὐφημία 'στω (v. 295 : « Silence religieux ! Silence religieux ! »)",
                "analyse": "Au début de la proclamation sacrée, la rubrique κῆρυξ a été récrite par R2 en semi-cursive sur une zone grattée juste à gauche du premier εὐφημί' ἔστω.",
            },
        ],
        [
            {
                "title": "3. Type III — Substitution lexicale sur grattage : [[ληκ->κιν]]ώμεθα",
                "subtitle": "f. 168r, v. 493 — La glose courante κινώμεθα substituée au verbe rare ληκώμεθα",
                "src": SPEC08,
                "crop": (140, 230, 990, 330),
                "max_h": 185,
                "boxes": [
                    (695, 262, 955, 312, "[[ληκ->κιν]]ώμεθα (κιν- in rasura)", "red"),
                ],
                "diplo": "ὑπὸ τῶν δούλων τε κὠρεωκόμων [[ληκ->κιν]]ώμεθα·",
                "edit": "... σποδούμεθα / ληκώμεθα (v. 493 : « ... nous nous faisons tringler par les esclaves et les muletiers »)",
                "analyse": "Les trois premières lettres κιν- de κινώμεθα sont écrites d'une encre plus épaisse sur un grattage profond où se devinent encore les vestiges du verbe comique rare ληκώμεθα.",
            },
            {
                "title": "4. Type IV — Grattage d'effacement à blanc d'une dittographie : ἅπασιν [[ἅπασιν]] ἔσται",
                "subtitle": "f. 170r, v. 670 — Seconde occurrence de ἅπασιν grattée au canif sans récriture",
                "src": SPEC09,
                "crop": (120, 1420, 880, 1515),
                "max_h": 185,
                "boxes": [
                    (405, 1448, 565, 1500, "ἅπασιν (1er conservé)", "blue"),
                    (570, 1448, 750, 1500, "[[ἅπασιν]] (2e gratté à blanc)", "red"),
                ],
                "diplo": "ἀγαθὸν πολίταις ἅπασιν [[ἅπασιν]] ἔσται·",
                "edit": "... ἅπασιν ἔσται (v. 670)",
                "analyse": "R1 avait écrit deux fois de suite le mot ἅπασιν (dittographie). Pour sauver le mètre, le réviseur a gratté au canif le second ἅπασιν en laissant une plage blanche caractéristique (fenestra in rasura) dont l'ombre fantôme reste lisible.",
            },
        ],
    ]
    render_standard_plate(
        "21_anatomie_des_grattages_in_rasura_quatre_types.jpg",
        "PLANCHE 21 — ANATOMIE DES GRATTAGES (IN RASURA) : LES QUATRE TYPES D'INTERVENTION",
        "Apprendre à repérer la fibre grattée du parchemin, les surcharges d'encre et les fenêtres d'effacement",
        rows,
        "DIAGNOSTIC VISUEL D'UN GRATTAGE (RASURA)",
        "Trois indices trahissent un grattage au canif sur le parchemin de Ravenne : (1) le grain plus clair et pelucheux de la peau ; (2) l'étalement légèrement baveux de l'encre de seconde main sur la fibre ouverte ; (3) l'espacement anormal des lettres (trop serrées ou laissant un blanc).",
    )


def gen_plate_22():
    rows = [
        [
            {
                "title": "Exercice 1 (Niveau 1 — Débutant) : L'Hypothesis (R2) et le Titre d'apparat (R1) (f. 162v)",
                "subtitle": "f. 162v, haut de page — Lire la semi-onciale de glose de R2 et la grande semi-onciale alexandrine de titre de R1",
                "src": SPEC01,
                "crop": (170, 50, 1630, 360),
                "max_h": 260,
                "vpad": 4,
                "boxes": [],
                "diplo": "l. 1 : ὁ χορὸς ἐκ θεσμοφοριαζουσῶν· καὶ τοῦτο τὸ δρᾶμα τῶν κατ' εὐριπίδου πεποιημένων· ἀπὸ δ(ὲ) τῶν θεσμο- / l. 2 : φορίων, τὰς θεσμοφοριαζούσας γυναῖκας ἐπέγραψεν, ἀφ' ὧν καὶ ὁ χορ(ός)· εὐριπίδου γυνὴ μὲν χοιρίλη, / l. 3–4 : μή(τ)ηρ δὲ κλειτώ :~ // προλογίζει μνησίλοχ(ος) κηδεστὴς εὐριπίδου ÷ // [Titre] ⁘ ΑΡΙϹΤΟΦΑΝΟΥϹ ΘΕϹΜΟΦΟΡΙΑΖΟΥϹΑΙ —",
                "edit": "Ὁ χορὸς ἐκ Θεσμοφοριαζουσῶν... Εὐριπίδου γυνὴ μὲν Χοιρίλη, μήτηρ δὲ Κλειτώ. Προλογίζει Μνησίλοχος κηδεστὴς Εὐριπίδου. // ΑΡΙΣΤΟΦΑΝΟΥΣ ΘΕΣΜΟΦΟΡΙΑΖΟΥΣΑΙ",
                "analyse": "Comparez les petites capitales de glose de l'Hypothesis (R2, lignes 1–4, sans liste séparée des personnages) avec la grande semi-onciale du titre (R1). Repérez en fin de ligne 2 le nom propre χοιρίλη (Χοιρίλη, clé de la restitution Χοιρίλ' de Bibi au v. 289) et en ligne 4 μνησίλοχ(ος).",
            }
        ],
        [
            {
                "title": "Exercice 2 (Niveau 1 — Débutant) : L'ouverture dialoguée en trimètres iambiques (f. 162v, vv. 1–10)",
                "subtitle": "f. 162v, vv. 1–10 — Maîtriser la minuscule bouletée de R1, l'iota adscrit et les signes de changement d'interlocuteur",
                "src": F162V,
                "crop": (650, 420, 1600, 920),
                "max_h": 300,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 1 : ὦ ζεῦ· χελιδὼν ἄρα πότε φανήσεται· | v. 2 : ἀπολεῖ μ' ἀλοῶν ἄνθρωπος ἐξ ἑωθινοῦ· | v. 3 : οἷόν τι πρὶν τὸν σπλῆνα κομιδῆι μ' ἐκβαλεῖν· | v. 4 : παρὰ σοῦ πυθέσθαι ποῖ μ' ἄγεις ὠὐριπίδη· | v. 5 : ἀλλ' οὐκ ἀκούειν δεῖ σε πάνθ' ὅσ' αὐτίκα : | v. 6 : ὄψει παρεστώς : πῶς λέγεις αὖθις φράσον·",
                "edit": "ΜΝ. Ὦ Ζεῦ, Χελιδὼν ἆρά ποτε φανήσεται; / Ἀπολεῖ μ' ἁλοῶν ἄνθρωπος ἐξ ἑωθινοῦ. / Οἷόν τε, πρὶν τὸν σπλῆνα κομιδῇ μ' ἐκβαλεῖν, / παρὰ σοῦ πυθέσθαι ποῖ μ' ἄγεις, ὠὐριπίδη; — ΕΥΡ. Ἀλλ' οὐκ ἀκούειν δεῖ σε πάνθ' ὅσ' αὐτίκα / ὄψει παρεστώς. — ΜΝ. Πῶς λέγεις; αὖθις φράσον.",
                "analyse": "Vérifiez sur ces 10 premières lignes : l'oméga initial en ∞ (ὦ), l'opposition ν en v sans queue (χελιδὼν, πρὶν, τὸν) vs μ à queue plongeante gauche (μ', κομιδῆι), l'iota adscrit de κομιδῆι, le β bilobé en u d'ἐκβαλεῖν, et le jeu combiné du dikôlon (:) et de la paragraphos (—).",
            }
        ],
        [
            {
                "title": "Exercice 3 (Niveau 2 — Intermédiaire) : Les dimètres anapestiques du Serviteur d'Agathon (f. 163r, vv. 49–57)",
                "subtitle": "f. 163r, vv. 49–57 — Déchiffrer les dimètres anapestiques, le double lambda (-λλ-) et les gloses techniques de R2",
                "src": SPEC03,
                "crop": (200, 235, 1300, 680),
                "max_h": 290,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 49 : μέλλει γὰρ ὁ καλλιεπὴς ἀγάθων | v. 50 : πράμος ἡμέτερος· — [v. 51 : μῶν βινεῖσθαι·] | v. 52 : — τίς ὁ φωνήσας· — νήνεμος αἰθήρ· | v. 53 : δρυόχους τιθέναι δράματος ἀρχάς· | v. 54 : κάμπτει δὲ νέας ἁσπίδας ἐπῶν | v. 55 : τὰ δὲ τορνεύει· τὰ δὲ κολλομελεῖ· | v. 56 : καὶ γνωμοτυπεῖ· κἀντονομάζει·",
                "edit": "ΘΕΡ. Μέλλει γὰρ ὁ καλλιεπὴς Ἀγάθων / πρανοῦν προτέρους [Bibi : πρόμος ἡμέτερος edd.] — ΜΝ. Μῶν βινεῖσθαι; / ΘΕΡ. Τίς ὁ φωνήσας; — ΜΝ. Νήνεμος αἰθήρ. / ΘΕΡ. Δρυόχους τιθέναι δράματος ἀρχάς· / κάμπτει δὲ νέας ἁψῖδας ἐπῶν, / τὰ δὲ τορνεύει, τὰ δὲ κολλομελεῖ...",
                "analyse": "Observez la colométrie plus courte des dimètres anapestiques, le double -λλ- imbriqué dans μέλλει, καλλιεπὴς et κολλομελεῖ, la faute de minuscule πράμος (pour πρανοῦν, Bibi), le β bilobé en u de βινεῖσθαι et la faute ἁσπίδας (pour ἁψῖδας) au v. 54.",
            }
        ],
    ]
    render_standard_plate(
        "22_exercice_progressif_niveau1_et_2_f162v_f163r.jpg",
        "PLANCHE 22 — ENTRAÎNEMENT GUIDÉ (NIVEAUX 1 & 2) : DU TITRE EN SEMI-ONCIALE AUX ANAPESTES",
        "Trois exercices progressifs avec transcription diplomatique ligne à ligne et corrigé paléographique",
        rows,
        "CONSEIL DE MÉTHODE (NIVEAUX 1 & 2)",
        "Commencez toujours par identifier les lettres à longues hampes ou hastes (φ, ψ, χ, ζ, ξ, δ, ρ, η, κ, λ), puis résolvez les ligatures d'epsilon (ει, εξ, ερ, εσ, ετ) et de sigma (σθ, σπ, στ).",
    )


def gen_plate_23():
    rows = [
        [
            {
                "title": "Exercice 4 (Niveau 3 — Avancé) : La prière parodique de Mnésiloque au Thesmophorion (f. 165v, vv. 284–291)",
                "subtitle": "f. 165v, vv. 284–291 — Repérer les datifs duels à iota adscrit et les fautes d'onciale/minuscule (χοῖρον, πρὸς θάληκον)",
                "src": SPEC06,
                "crop": (170, 510, 1530, 920),
                "max_h": 280,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 285 : τὸ πόπανον ὅπως λαβοῦσα θύσω ταῖν θεαῖν· | v. 286 : δέσποιναι πολυτίμητε δήμητερ φίλη | v. 287 : καὶ φερρέφαττα· πολλὰ πολλάκις μέ σοι | v. 288 : θύειν ἔχουσαν· εἰ δὲ μὴ ἀλλὰ νῦν λαθεῖν· | v. 289 : καὶ τὴν θυγατέρα χοῖρον ἀνδρός μοι τυχεῖν | v. 290 : πλουτοῦντος· ἄλλως δ' ἠλιθίου κἀβελτέρου· | v. 291 : καὶ πρὸς θάληκον μὴ νοῦν ἔχειν μοι καὶ φρένας·",
                "edit": "ΜΝ. ... τὸ πόπανον ὅπως λαβοῦσα θύσω ταῖν θεαῖν. / Δέσποιναι πολυτίμητε Δήμητερ φίλη / καὶ Φερρέφαττα, πολλὰ πολλάκις μέ σοι / θύειν ἔχουσαν, εἰ δὲ μή, ἀλλὰ νῦν λαθεῖν· / καὶ τὴν θυγατέρα Χοιρίλ' [Bibi : χοῖρον R] ἀνδρός μοι τυχεῖν / πλουτοῦντος, ἄλλως δ' ἠλιθίου κἀβελτέρου...",
                "analyse": "Repérez les iotas adscrits des datifs duels (ταῖν θεαῖν), la géminée -ρρ- de φερρέφαττα, la leçon χοῖρον au v. 289 (glosée en marge gauche γρ(άφεται) χοιρίον... κύσθον, restituée en Χοιρίλ' par Bibi d'après l'Hypothesis) et la métathèse πρὸς θάληκον (pour πρὸς θυλάκιον / θάλικα) au v. 291.",
            }
        ],
        [
            {
                "title": "Exercice 5 (Niveau 3 — Avancé) : L'épirrhème de la Parabase en tétramètres trochaïques (f. 172v, vv. 838–845)",
                "subtitle": "f. 172v, vv. 838–845 — Lire les tétramètres trochaïques, les surcharges vocaliques et la crase corrompue ὦ πόλεις",
                "src": SPEC11,
                "crop": (160, 135, 1480, 495),
                "max_h": 280,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 838 : ὑστέρ[ο->α]ν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην | v. 839 : τῆς τὸν ἀνδρεῖον τεκούσης· τῶι γὰρ εἰκὸς ὦ πόλεις· | v. 840 : τὴν ὑπερβόλου καθῆσθαι μητέρ' ἠμφιεσμένην | v. 841 : λευκὰ καὶ κόμας καθεῖσαν πλησίον τῆς λαμάχου· | v. 842 : καὶ δανείζειν χρήματα· τῆι χρῆν... | v. 844 : ἀλλ' ἀφαιρεῖσθαι βίαι τὰ χρήματα τὰς πόρνας τ[ὰ->ο]δὶ",
                "edit": "ΧΟΡ. ὑστέραν αὐτὴν καθῆσθαι σκάφιον ἀποκεκαρμένην / τῆς τὸν ἀνδρεῖον τεκούσης; Τῷ γὰρ εἰκός, ωὖπολι [Bibi : ὦ πόλεις R], / τὴν Ὑπερβόλου καθῆσθαι μητέρ' ἠμφιεσμένην / λευκὰ καὶ κόμας καθεῖσαν πλησίον τῆς Λαμάχου...",
                "analyse": "Ces longs tétramètres trochaïques côtoient à gauche un dense bloc de scholies historiques sur Hyperbolos et Lamachos. Repérez les deux surcharges vocaliques (ὑστέρ[ο->α]ν au v. 838 et τ[ὰ->ο]δὶ au v. 844) ainsi que la crase corrompue ὦ πόλεις au v. 839 (= ωὖπολι, « ô Eupolis ! », Bibi).",
            }
        ],
        [
            {
                "title": "Exercice 6 (Niveau 4 — Confirmé) : La mise en page bicolonne de la scène d'Écho (f. 175v, vv. 1082–1097)",
                "subtitle": "f. 175v, vv. 1082–1097 — Déchiffrer les répliques en miroir sur deux sous-colonnes et les grattages jumeaux",
                "src": SPEC14,
                "crop": (380, 20, 1380, 815),
                "max_h": 300,
                "vpad": 4,
                "boxes": [],
                "diplo": "Col. gauche (Mnésiloque / Scythe) || Col. droite (Écho) : v. 1082 : μν/ οἴμωζ' || ἠχ/ οἴμωζ' | v. 1083 : σκυ/ οὗτος τί λαλεῖς· || ἠχ/ οὗτος τί λαλεῖς | v. 1084 : σκυ/ πρυτάνεις καλέσω : || ἠχ/ πρυτάνεις καλέσω | v. 1085 : σκυ/ σὶ κακόν : || ἠχ/ σὶ κακόν | v. 1086 : σκυ/ π[[ρ]]ῶτε φωνή : || ἠχ/ π[[ρ]]ῶτε φωνή...",
                "edit": "ΜΝ. Οἴμωζ'. — ΗΧΩ. Ὀλόφυγ' [Bibi : οἴμωζ' R]. — ΤΟΞ. Οὗτος, τί λαλεῖς; — ΗΧΩ. Οὗτος, τί λαλεῖς; — ΤΟΞ. Πρυτάνεις καλέσω. — ΗΧΩ. Πρυτάνεις καλέσω. — ΤΟΞ. Σί κακόν; — ΗΧΩ. Σί κακόν; — ΤΟΞ. †Πῶτε† τὸ πωνή; — ΗΧΩ. †Πῶτε† τὸ πωνή;",
                "analyse": "Pour figurer visuellement le phénomène acoustique de l'écho, R1 a divisé sa colonne en deux sous-colonnes parallèles ! Observez au v. 1086 le double grattage du ρ dans π[[ρ]]ῶτε φωνή sur les deux colonnes, et au v. 1094 la glose marginale droite ἀν(τὶ) τοῦ οὐχ αἱρήσεις.",
            }
        ],
    ]
    render_standard_plate(
        "23_exercice_progressif_niveau3_et_4_f165v_f172v_f175v.jpg",
        "PLANCHE 23 — ENTRAÎNEMENT GUIDÉ (NIVEAUX 3 & 4) : PRIÈRE PARODIQUE, PARABASE ET SCÈNE D'ÉCHO",
        "Déchiffrer des passages combinant scholies denses, surcharges vocaliques et mise en page bicolonne",
        rows,
        "CONSEIL DE MÉTHODE (NIVEAUX 3 & 4)",
        "Confrontez systématiquement la colonne poétique (R1) et les scholies marginales (R2) : bien souvent, la glose marginale conserve la leçon authentique (comme οὐχ αἱρήσεις au v. 1094 ou πέπαικται au v. 1227) ou explique l'origine d'une corruption.",
    )


def gen_plate_24():
    rows = [
        [
            {
                "title": "Exercice 7 (Niveau 5 — Expert) : Le dialecte barbare du Scythe, la 4e parepigraphè, les rasurae et Boninus (f. 176v, vv. 1185–1201)",
                "subtitle": "f. 176v, vv. 1185–1201 — L'épreuve reine : cumuler barbarismes scythes, didascalie scénique, grattages au canif et 3e main humaniste",
                "src": SPEC15,
                "crop": (360, 40, 1490, 745),
                "max_h": 350,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 1187 : κλαυσ[[' ε]]ϊ γ' ἂν μὴ 'νδον μένῃς : | [Parepigraphè 4] ἀνακύπτη· καὶ παρακύπτι· ἀπεψωλημέν@· | v. 1188 : σκ/ εἶεν· καλὴ τὸ σχῆμα περὶ τὸ [[σ]]ποστίον· | v. 1189 : [γϋ. Boninus] καλῶς ἔχει· λαβὲ θοἰμάτιον ὦ παιδίον· | ... | v. 1197 : φύλαξον καὶ τὴν συμβήνην· | v. 1198 : [γϋ. Boninus] ἔπειτα κ[[ω->ο]]μίζεις αὐτοῖς· [σκ'] ἀκουλούτι τέκνον·",
                "edit": "ΤΟΞ. ... κλαυσεῖ γ', ἢν μὴ 'νδον μένῃς. [Παρεπιγραφή 4 : Ἀνακύπτει καὶ παρακύπτει ἀπεψωλημένος.] Εἶεν· καλὴ τὸ σχῆμα περὶ τὸ ποστίον. — ΕΥΡ. Καλῶς ἔχει· λαβὲ θοἰμάτιον, ὦ παιδίον... — ΤΟΞ. ... φύλαξον καὶ τὴν συμβήνην [Bibi]. / Ἔπειτα κομίζι σ' αὐτίκ' [Bibi]. Ἀκολούτι, τέκνον.",
                "analyse": "Ce passage réunit toutes les difficultés du manuscrit : (1) la 4e parepigraphè terminée par la spirale @ = -ος ; (2) les grattages au canif (κλαυσ[[' ε]]ϊ γ', τὸ [[σ]]ποστίον, [[σὺ]] κάρισοσ, κ[[ω->ο]]μίζεις) ; (3) la graphie συμβήνην avec -μ- au v. 1197 (défendue par Bibi) ; (4) les deux notes γϋ. à l'encre noire d'Euphrosynus Boninus (1515).",
            }
        ],
        [
            {
                "title": "Exercice 8 (Niveau 5 — Expert) : L'Exodos des Thesmophories, la korônis finale et l'Hypothesis des Ecclésiazuses (f. 177r, vv. 1222–1231)",
                "subtitle": "f. 177r, vv. 1222–1231 — Lire les derniers vers de la comédie, la korônis de clôture et l'enchaînement avec l'Assemblée des femmes",
                "src": SPEC16,
                "crop": (260, 250, 1380, 960),
                "max_h": 350,
                "vpad": 4,
                "boxes": [],
                "diplo": "v. 1223 : ὀρθὴν ἄνω δίωκε· ποῖ θεῖς· οὐ πάλιν | v. 1224 : τῆιδὶ διώξεις· τοὔμπαλιν τρέχεις σύ γε· | v. 1225 : σκ/ κακόδαιμον ἀλλὰ τρέξι ἀρταμουξία· | v. 1226 : Χ [chœur] τρέχε νυν κατὰ τοὺς κόρακας ἐπουρίσας· | v. 1227 : ἀλλὰ πέπυσται μετρίως ἡμῖν· | vv. 1228–1231 : ὥσθ' ὥρα δή 'στι βαδίζειν / οἴκαδ' ἑκάστη· τὼ θεσμοφόρω δ' / ἡμῖν ἀγαθὴν / τούτων χάριν ἀνταδοῖτον· || [Korônis finale] || Ὑπόθ(εσις) ἐκκλησιαζουσῶν ἀριστοφάν(ους) :~",
                "edit": "ΧΟΡ. Ὀρθὴν ἄνω δίωκε. Ποῖ θεῖς; Οὐ πάλιν / τῃδὶ διώξει 'ς τοὔμπαλιν; Τρέχεις σύ γε. — ΤΟΞ. Κακόδαιμον, ἀλλὰ τρέξι· Ἀρταμουξία. — ΧΟΡ. Τρέχε νυν κατ' αὐτοὺς ἐς κόρακας ἐπουρίσας. / Ἀλλὰ πέπαισται [Σ : πέπυσται R] μετρίως ἡμῖν· / ὥσθ' ὥρα δή 'στι βαδίζειν / οἴκαδ' ἑκάστῃ. Τὼ Θεσμοφόρω δ' / ἡμῖν ἀγαθὴν / τούτων χάριν ἀνταποδοίτην [Bibi : ἀνταδοῖτον R].",
                "analyse": "Après la fuite grotesque de l'Archer scythe et les cinq vers de sortie du Chœur (avec πέπυσται pour πέπαισται au v. 1227 et l'haplographie ἀνταδοῖτον au v. 1231), la grande korônis barrée clôt la comédie, et R1 enchaîne lui-même avec l'Hypothesis des Ecclésiazuses coiffée du monogramme Ὑπόθ(εσις) !",
            }
        ],
    ]
    render_standard_plate(
        "24_exercice_progressif_niveau5_expert_scythe_et_scholies_f176v_f177r.jpg",
        "PLANCHE 24 — ENTRAÎNEMENT GUIDÉ (NIVEAU 5 — EXPERT) : L'ARCHER SCYTHE, BONINUS ET L'EXODOS",
        "L'épreuve ultime du paléographe : cumuler barbarismes scythes, grattages multiples, main humaniste et korônis finale",
        rows,
        "BILAN DU PARCOURS PALÉOGRAPHIQUE",
        "Au terme de ces 24 planches, vous savez distinguer les trois mains du manuscrit (R1, R2, Boninus 1515), déjouer les 6 faux-amis de la minuscule bouletée, résoudre les ligatures et la tachygraphie, et vérifier sur pièce chaque leçon de l'apparat critique.",
    )


def main():
    gen_plate_01()
    gen_plate_02()
    gen_plate_03()
    gen_plate_04()
    gen_plate_05()
    gen_plate_06()
    gen_plate_07()
    gen_plate_08()
    gen_plate_09()
    gen_plate_10()
    gen_plate_11()
    gen_plate_12()
    gen_plate_13()
    gen_plate_14()
    gen_plate_15()
    gen_plate_16()
    gen_plate_18()
    gen_plate_19()
    gen_plate_20()
    gen_plate_21()
    gen_plate_22()
    gen_plate_23()
    gen_plate_24()
    print("Toutes les planches ont été régénérées avec succès.")


if __name__ == "__main__":
    main()
