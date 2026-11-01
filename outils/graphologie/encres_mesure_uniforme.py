#!/usr/bin/env python3
"""Mesure uniforme des encres du Ravennas (Thesmophories, ff. 162v–177r) — outil du chapitre 1
de l'étude graphologique (ravennas/graphologie/chapitres/1_mains_encres.md).

Méthode : masque d'encre brune (outils/images/recadrer_facsimile.py : masque_encre), fond local par
convolution normalisée hors encre, absorbances A = -log10(I/fond) par canal, rapports A_G/A_R et
A_B/A_R ; « écart à T » = médiane de (B/R − B/R de T à la même densité A_R), T étant mesuré sur les
lignes de la colonne de la même page (segmentation ravennas/segmentation/fXXX.json).

Usage :
  python3 outils/graphologie/encres_mesure_uniforme.py pages        # T et S2 par page -> ravennas/graphologie/chapitres/donnees/1_encres_pages.json
  python3 outils/graphologie/encres_mesure_uniforme.py obs          # toutes les observations munies d'une boîte -> .../1_ecarts_observations.tsv
  python3 outils/graphologie/encres_mesure_uniforme.py mesure f170r 775 822 1105 880 [...]
"""

import sys, os, json, glob, re
import numpy as np, cv2
from PIL import Image
sys.path.insert(0, '/workspaces/Thesmophories/outils/images')
from recadrer_facsimile import masque_encre

R = '/workspaces/Thesmophories'
SRC = os.path.join(R, 'dossier_ravennas_thesmophories', 'folios_individuels_ff162v-177r')
PAGES = {f.split('_')[1]: os.path.join(SRC, f) for f in os.listdir(SRC) if f.endswith('.jpg')}
BINS = [(0.10, 0.20), (0.20, 0.30), (0.30, 0.45), (0.45, 2.0)]


def charge(folio):
    im = Image.open(PAGES[folio]).convert('RGB')
    a = np.asarray(im).astype(np.float32)
    m, lum = masque_encre(im)
    return im, a, m


def fond(a, m, sigma=12):
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    md = cv2.dilate(m.astype(np.uint8), k) > 0
    w = (~md).astype(np.float32)
    den = cv2.GaussianBlur(w, (0, 0), sigma)
    out = np.empty_like(a)
    for c in range(3):
        num = cv2.GaussianBlur(a[..., c] * w, (0, 0), sigma)
        out[..., c] = num / np.maximum(den, 1e-3)
    # là où le fond n'est pas estimable (den très faible), flou plus large
    bad = den < 0.05
    if bad.any():
        den2 = cv2.GaussianBlur(w, (0, 0), sigma * 3)
        for c in range(3):
            num2 = cv2.GaussianBlur(a[..., c] * w, (0, 0), sigma * 3)
            out[..., c][bad] = (num2 / np.maximum(den2, 1e-3))[bad]
    return out


def absorb(a, f):
    return -np.log10(np.clip(a, 1, 255) / np.clip(f, 1, 255))


def stats(A, sel):
    """A : absorbances (H,W,3) ; sel : masque booléen des pixels retenus."""
    n = int(sel.sum())
    if n < 30:
        return dict(n=n)
    ar, ag, ab = A[..., 0][sel], A[..., 1][sel], A[..., 2][sel]
    ok = ar > 0.04
    ar, ag, ab = ar[ok], ag[ok], ab[ok]
    if len(ar) < 30:
        return dict(n=int(len(ar)))
    gr, br = ag / ar, ab / ar
    d = dict(n=int(len(ar)), AR=round(float(np.median(ar)), 3),
             GR=round(float(np.median(gr)), 3), BR=round(float(np.median(br)), 3),
             BR_q=[round(float(x), 3) for x in np.percentile(br, [10, 25, 75, 90])],
             # rapport des moyennes (moins bruité que la médiane des rapports)
             GRm=round(float(ag.mean() / ar.mean()), 3), BRm=round(float(ab.mean() / ar.mean()), 3))
    tr = {}
    for lo, hi in BINS:
        s = (ar >= lo) & (ar < hi)
        if s.sum() >= 30:
            tr['%.2f-%.2f' % (lo, hi)] = [int(s.sum()), round(float(np.median(gr[s])), 3), round(float(np.median(br[s])), 3)]
    d['tranches'] = tr
    return d


def boite_masque(shape, boites):
    mm = np.zeros(shape, bool)
    for x0, y0, x1, y1 in boites:
        x0, y0 = max(0, int(x0)), max(0, int(y0))
        mm[y0:int(y1), x0:int(x1)] = True
    return mm


def page_mesures(folio):
    seg = json.load(open(os.path.join(R, 'ravennas/segmentation/%s.json' % folio)))
    im, a, m = charge(folio)
    f = fond(a, m)
    A = absorb(a, f)
    H, W = m.shape
    ero = cv2.erode(m.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    sig = seg['colonne'].get('zone_sigles') or [0, 0]
    blocs = [b['boite'] for b in seg['blocs']]
    zb = boite_masque(m.shape, blocs)
    # T : lignes de texte, hors zone des sigles (bande de 100 px à gauche de la colonne)
    tb = []
    for l in seg['lignes']:
        x0, y0, x1, y1 = l['texte']
        x0 = max(x0, sig[1] + 8)
        if x1 > x0:
            tb.append([x0, y0, x1, y1])
    zt = boite_masque(m.shape, tb) & ~zb
    res = dict(folio=folio)
    res['T'] = stats(A, m & zt)
    res['T_coeur'] = stats(A, ero & zt)
    zs = zb & ~boite_masque(m.shape, tb)
    res['S2'] = stats(A, m & zs)
    res['S2_coeur'] = stats(A, ero & zs)
    par = {}
    for reg in ('gauche', 'droite', 'haut', 'bas'):
        bb = [b['boite'] for b in seg['blocs'] if b['region'] == reg]
        if bb:
            z = boite_masque(m.shape, bb) & ~boite_masque(m.shape, tb)
            par[reg] = stats(A, ero & z)
    res['S2_regions'] = par
    # fond : teinte du parchemin (pour mémoire)
    res['fond_rgb_T'] = [round(float(np.median(f[..., c][zt])), 1) for c in range(3)]
    res['fond_rgb_S2'] = [round(float(np.median(f[..., c][zs])), 1) for c in range(3)] if zs.any() else None
    return res, A, m, ero, zt




# ---------------------------------------------------------------- page et écart à T
_cache = {}


def page(folio):
    """Renvoie (image PIL, absorbances A (H,W,3), masque d'encre, masque érodé, référence T)."""
    if folio in _cache:
        return _cache[folio]
    im, a, m = charge(folio)
    f = fond(a, m)
    A = absorb(a, f)
    ero = cv2.erode(m.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    seg = json.load(open(os.path.join(R, 'ravennas/segmentation/%s.json' % folio)))
    sig = seg['colonne'].get('zone_sigles') or [0, 0]
    tb = []
    for l in seg['lignes']:
        x0, y0, x1, y1 = l['texte']
        x0 = max(x0, sig[1] + 8)
        if x1 > x0:
            tb.append([x0, y0, x1, y1])
    zb = boite_masque(m.shape, [b['boite'] for b in seg['blocs']])
    zt = boite_masque(m.shape, tb) & ~zb
    # référence T : médiane et dispersion de A_B/A_R par tranche fine de A_R (0,02)
    sel = ero & zt & (A[..., 0] > 0.06)
    ar = A[..., 0][sel]; br = A[..., 2][sel] / ar; gr = A[..., 1][sel] / ar
    edges = np.arange(0.06, 0.62, 0.02)
    ref = []
    for lo in edges:
        s = (ar >= lo) & (ar < lo + 0.02)
        if s.sum() >= 50:
            q = np.percentile(br[s], [50, 90, 97.5])
            g = np.percentile(gr[s], [50, 90])
            ref.append((lo, float(q[0]), float(q[1]), float(q[2]), float(g[0]), float(g[1]), int(s.sum())))
    _cache[folio] = (im, A, m, ero, ref, zt)
    return _cache[folio]


def ref_interp(ref, ar, col):
    xs = np.array([r[0] + 0.01 for r in ref]); ys = np.array([r[col] for r in ref])
    return np.interp(ar, xs, ys)


def ecart_T(folio, A, sel):
    """Écart à T (même page, même densité) : médiane de (B/R - médiane_T(A_R)) et de G/R."""
    _, _, _, _, ref, _ = page(folio)
    ar = A[..., 0][sel]
    ok = ar > 0.06
    ar = ar[ok]
    if len(ar) < 15:
        return None
    br = A[..., 2][sel][ok] / ar; gr = A[..., 1][sel][ok] / ar
    dbr = br - ref_interp(ref, ar, 1)
    dgr = gr - ref_interp(ref, ar, 4)
    p90 = ref_interp(ref, ar, 2)
    return dict(n=int(len(ar)), AR=round(float(np.median(ar)), 3), dBR=round(float(np.median(dbr)), 3),
                dGR=round(float(np.median(dgr)), 3), frac_sup_p90T=round(float((br > p90).mean()), 2))


def mesure(folio, box, coeur=True):
    im, A, m, ero, ref, zt = page(folio)
    z = boite_masque(m.shape, [box])
    sel = (ero if coeur else m) & z
    if sel.sum() < 15:  # traits trop minces : on prend le masque complet
        sel = m & z
    d = stats(A, sel)
    e = ecart_T(folio, A, sel)
    return d, e


def fmt(d, e):
    if not d or d.get('n', 0) < 30:
        s = 'n=%s (trop peu)' % (d or {}).get('n')
    else:
        s = 'n=%5d AR=%.3f G/R=%.2f B/R=%.2f (moy. %.2f/%.2f)' % (d['n'], d['AR'], d['GR'], d['BR'], d['GRm'], d['BRm'])
    if e:
        s += ' | écart à T (même densité) : dB/R=%+.2f dG/R=%+.2f, part > p90(T)=%.2f' % (e['dBR'], e['dGR'], e['frac_sup_p90T'])
    return s


def carte(folio, x0, y0, x1, y1):
    """Image RGB : pixels d'encre colorés selon l'écart de B/R à T (bleu = comme T, rouge = plus orangé)."""
    im, A, m, ero, ref, zt = page(folio)
    sub = A[y0:y1, x0:x1]; mm = m[y0:y1, x0:x1]
    ar = sub[..., 0]
    br = sub[..., 2] / np.maximum(ar, 1e-3)
    med = ref_interp(ref, ar, 1); p975 = ref_interp(ref, ar, 3)
    z = np.clip((br - med) / np.maximum(p975 - med, 0.05), -1, 3)
    out = np.full(sub.shape, 255, np.uint8)
    # échelle : z<=0.5 bleu-gris (T), 0.5..1 violet, >1 orange-rouge
    col = np.zeros(sub.shape, np.float32)
    t = np.clip((z - 0.3) / 1.2, 0, 1)[..., None]
    col = (1 - t) * np.array([60, 90, 170]) + t * np.array([230, 80, 0])
    out[mm] = col[mm].astype(np.uint8)
    return Image.fromarray(out)


def vue(folio, x0, y0, x1, y1, ech, sortie, avec_carte=False):
    im = page(folio)[0]
    c = im.crop((x0, y0, x1, y1))
    w, h = c.size
    c = c.resize((int(w * ech), int(h * ech)), Image.LANCZOS)
    if avec_carte:
        k = carte(folio, x0, y0, x1, y1).resize(c.size, Image.NEAREST)
        out = Image.new('RGB', (c.size[0], c.size[1] * 2 + 6), 'white')
        out.paste(c, (0, 0)); out.paste(k, (0, c.size[1] + 6))
        c = out
    c.save(sortie)
    return sortie




# ---------------------------------------------------------------- observations des inventaires
R = '/workspaces/Thesmophories'
K16 = ['1516', 'xvie', 'xvi', 'boninus', 'b16', 'rrec', 'tardive', 'rousse', '2 m.', 'juntine']
KGR = ['crayon', 'mine', 'graphite', 'plomb', 'foliot']


def groupe(o):
    """Regroupe la main déclarée par l'inventaire (champ libre) en : T, S2, S2?, B16 (1516), S2/B16, gris, indet, autre."""
    m = (o.get('main') or '').lower()
    cat = o.get('categorie')
    if any(k in m for k in KGR) or cat == 'imprimeur':
        return 'gris'
    if 'orangée' in m and not any(k in m for k in K16):
        return 'orange?'
    has16 = any(k in m for k in K16)
    hasS2 = ('s2' in m) or ('r²' in m) or ('main des scholies' in m)
    if m.startswith('indéterm') or m.startswith('?') or m.startswith('—') or m == '' or m.startswith('-'):
        return 'indet'
    if has16 and hasS2:
        return 'S2/B16'
    if has16:
        return 'B16'
    if hasS2:
        head = m.split('(')[0]
        return 'S2' if (m.startswith('s2') and ' ou ' not in head) else 'S2?'
    if re.match(r'^\s*t\b', m) and ' ou ' not in m and '/' not in m:
        return 'T'
    return 'autre'


def main_obs():
    res = []
    fichiers = sorted(glob.glob(os.path.join(R, 'ravennas/graphologie/folios/f*.jsonl')))
    fichiers = [f for f in fichiers if re.search(r'/f\d{3}[rv]\.jsonl$', f)]
    for f in fichiers:
        folio = os.path.basename(f)[:5]
        n = 0
        for i, line in enumerate(open(f)):
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            b = o.get('bbox')
            if not b or len(b) != 4:
                continue
            x0, y0, x1, y1 = map(int, b)
            if (x1 - x0) * (y1 - y0) > 400000 or x1 <= x0 or y1 <= y0:
                continue  # boîtes de page entière ou de colonne
            g = groupe(o)
            im, A, m, ero, ref, zt = page(folio)
            z = boite_masque(m.shape, [[x0, y0, x1, y1]])
            sel = ero & z
            if sel.sum() < 15:
                sel = m & z
            e = ecart_T(folio, A, sel)
            res.append(dict(folio=folio, idx=i, ligne=o.get('ligne'), vers=o.get('vers'), cat=o.get('categorie'),
                            main=o.get('main'), groupe=g, bbox=[x0, y0, x1, y1], ecart=e,
                            desc=(o.get('description') or '')[:160]))
            n += 1
        _cache.clear()
        print(folio, n, flush=True)
    json.dump(res, open(os.path.join(R, '.travail/ch1/ecarts_obs.json'), 'w'), ensure_ascii=False, indent=0)




def cmd_pages():
    folios = sorted(PAGES, key=lambda s: (int(s[1:4]), s[4]))
    res = {}
    for fo in folios:
        r, *_ = page_mesures(fo)
        res[fo] = r
        print(fo, flush=True)
    d = os.path.join(R, 'ravennas/graphologie/chapitres/donnees'); os.makedirs(d, exist_ok=True)
    json.dump(res, open(os.path.join(d, '1_encres_pages.json'), 'w'), ensure_ascii=False, indent=1)


def cmd_obs():
    main_obs()
    res = json.load(open(os.path.join(R, '.travail/ch1/ecarts_obs.json')))
    d = os.path.join(R, 'ravennas/graphologie/chapitres/donnees'); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, '1_ecarts_observations.tsv'), 'w') as f:
        f.write('folio\tobs\tligne\tvers\tcategorie\tmain_inventaire\tgroupe\tx0\ty0\tx1\ty1\tn_px\tA_R\tdB_R\tdG_R\n')
        for r in res:
            e = r['ecart'] or {}
            f.write('\t'.join(str(x) for x in [r['folio'], r['idx'], r['ligne'], r['vers'], r['cat'], (r['main'] or '').replace('\t', ' '), r['groupe'], *r['bbox'], e.get('n', ''), e.get('AR', ''), e.get('dBR', ''), e.get('dGR', '')]) + '\n')


if __name__ == '__main__':
    c = sys.argv[1] if len(sys.argv) > 1 else ''
    if c == 'pages':
        cmd_pages()
    elif c == 'obs':
        cmd_obs()
    elif c == 'mesure':
        folio = sys.argv[2]; nums = [int(x) for x in sys.argv[3:]]
        for i in range(0, len(nums), 4):
            print(nums[i:i + 4], fmt(*mesure(folio, nums[i:i + 4])))
    else:
        print(__doc__)
