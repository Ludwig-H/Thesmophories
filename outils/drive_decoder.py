#!/usr/bin/env python3
"""Décode un fichier téléchargé du Drive via l'outil MCP download_file_content.

Quand le résultat est trop volumineux, l'outil l'enregistre dans un fichier JSON
({content: base64, id, mimeType, title}) dont le chemin figure dans le message
d'erreur. Ce script le décode vers la destination, vérifie le fichier, extrait la
couche texte des PDF (page par page) et supprime le JSON intermédiaire.

Usage : python3 outils/drive_decoder.py JSON_RESULTAT DESTINATION [--garder-json]
Sortie : une ligne JSON {ok, destination, octets, type, pages, couche_texte, remarque}.
"""
import base64, json, os, subprocess, sys


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    src, dst = sys.argv[1], sys.argv[2]
    garder = '--garder-json' in sys.argv
    res = {'ok': False, 'destination': dst}
    try:
        data = json.load(open(src, encoding='utf-8'))
        contenu = data.get('content', '')
        os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
        brut = base64.b64decode(contenu)
        with open(dst, 'wb') as f:
            f.write(brut)
        res['octets'] = len(brut)
        res['type'] = subprocess.run(['file', '-b', dst], capture_output=True, text=True).stdout.strip()[:120]
        if dst.lower().endswith('.pdf') or 'PDF' in res['type']:
            import pymupdf
            doc = pymupdf.open(dst)
            res['pages'] = doc.page_count
            n_txt = 0
            with open(os.path.splitext(dst)[0] + '.txt', 'w', encoding='utf-8') as out:
                for i, page in enumerate(doc):
                    t = page.get_text()
                    if t.strip():
                        n_txt += 1
                    out.write(f'\n===== p. {i + 1} =====\n{t}')
            res['couche_texte'] = n_txt > 0.3 * max(1, doc.page_count)
            if not res['couche_texte']:
                os.remove(os.path.splitext(dst)[0] + '.txt')
                res['remarque'] = 'PDF scanné sans couche texte'
        elif dst.lower().endswith('.djvu'):
            try:
                t = subprocess.run(['djvutxt', dst], capture_output=True, text=True, timeout=600).stdout
                if t.strip():
                    open(os.path.splitext(dst)[0] + '.txt', 'w', encoding='utf-8').write(t)
                    res['couche_texte'] = True
            except Exception as e:  # noqa
                res['remarque'] = f'djvutxt : {e}'
        res['ok'] = res['octets'] > 0
        if res['ok'] and not garder:
            os.remove(src)
    except Exception as e:
        res['remarque'] = f'erreur : {e}'
    print(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    main()
