from PIL import Image
from pathlib import Path

sizes = [1600, 1200, 800, 400]
root = Path(__file__).resolve().parent.parent / 'images'
source_png = root / 'hero.png'

if not source_png.exists():
    print('Source hero.png not found at', source_png)
    raise SystemExit(1)

img = Image.open(source_png).convert('RGBA')
for w in sizes:
    # calculate height to preserve aspect ratio
    ratio = w / img.width
    h = int(img.height * ratio)
    resized = img.resize((w, h), Image.LANCZOS)
    webp_path = root / f'hero-{w}.webp'
    png_path = root / f'hero-{w}.png'
    resized.save(webp_path, 'WEBP', quality=85)
    resized.save(png_path, 'PNG', optimize=True)
    print('Saved', webp_path.name, png_path.name)
print('Done')
