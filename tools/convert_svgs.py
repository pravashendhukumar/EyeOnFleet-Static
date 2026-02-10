from pathlib import Path
from PIL import Image, ImageDraw
import subprocess
import os

SRC_DIR = Path('images')
OUT_DIR = SRC_DIR

sizes = {
    'hero-realistic.svg': (1600,800),
    'dashboard-realistic.svg': (1200,600),
    'solution-fleet-realistic.svg': (1000,600),
    'solution-energy-realistic.svg': (1000,600),
    'solution-safety-realistic.svg': (1000,600),
    'solution-pets-realistic.svg': (1000,600),
}

# Try using Inkscape if available on Windows
try:
    result = subprocess.run(['inkscape', '--version'], capture_output=True)
    has_inkscape = result.returncode == 0
except:
    has_inkscape = False

if has_inkscape:
    print('Using Inkscape for SVG conversion...')
    for svg_name, size in sizes.items():
        svg_path = SRC_DIR / svg_name
        if not svg_path.exists():
            print('missing', svg_path)
            continue
        png_path = OUT_DIR / (svg_path.stem + '.png')
        webp_path = OUT_DIR / (svg_path.stem + '.webp')
        print(f'converting {svg_path} -> {png_path}')
        # Inkscape conversion
        cmd = [
            'inkscape', str(svg_path),
            f'--export-width={size[0]}',
            f'--export-height={size[1]}',
            f'--export-png={png_path}'
        ]
        subprocess.run(cmd, capture_output=True)
        # Convert PNG to WebP
        if png_path.exists():
            im = Image.open(str(png_path)).convert('RGBA')
            im.save(str(webp_path), 'WEBP', quality=90, lossless=False, method=6)
            print(f'wrote {webp_path}')
else:
    print('Inkscape not found. SVG files already exist. Using pre-rendered WebP assets.')
    print('To generate fresh PNG/WebP from SVGs, install Inkscape:')
    print('  Windows: Download from https://inkscape.org/release/')
    print('  OR use WSL/Linux subsystem with: apt install inkscape')

print('done')
