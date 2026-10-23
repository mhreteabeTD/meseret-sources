"""Split a textbook PDF into unit PDFs and render page images.
usage: python3 split.py full.pdf "u1:5-40" "u2:41-78" --out textbooks/g8/maths --dpi 110
"""
import sys, subprocess, pathlib
from pypdf import PdfReader, PdfWriter
args = sys.argv[1:]; src = args[0]; out = pathlib.Path(args[args.index('--out') + 1]); dpi = args[args.index('--dpi') + 1] if '--dpi' in args else '110'
r = PdfReader(src)
for spec in [a for a in args[1:] if ':' in a and '-' in a]:
    name, rng = spec.split(':'); a, b = map(int, rng.split('-')); d = out / name; (d / 'pages').mkdir(parents=True, exist_ok=True)
    w = PdfWriter(); [w.add_page(r.pages[i - 1]) for i in range(a, b + 1)]; w.write(d / f'{name}.pdf')
    subprocess.run(['pdftoppm', '-r', dpi, '-png', str(d / f'{name}.pdf'), str(d / 'pages' / 'p')], check=True)
    print(name, a, b, '→', d)
