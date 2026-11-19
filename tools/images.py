"""Export a photo as responsive WebP: optional crop, metadata stripped, several widths.

    python tools/images.py SOURCE OUTPUT_PREFIX WIDTH[,WIDTH...] [--crop x0,y0,x1,y1]

Example (crop a 4:5 area out of a phone photo, then export 600px and 1000px wide):
    python tools/images.py ../20260606_211312.jpg assets/img/sake/note-tamagawa 600,1000 --crop 0,700,2252,3515

Writes OUTPUT_PREFIX-<width>.webp for each width (never wider than the source) and prints sizes.
Pillow only writes EXIF if asked, so location and device data are not carried over.
Crop out any screenshot UI (e.g. Instagram bars) before publishing. Add a row to CREDITS.md.
"""
import os, sys
from PIL import Image, ImageOps
from _paths import REPO

def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    src, prefix, widths = argv[0], argv[1], [int(w) for w in argv[2].split(',')]
    box = None
    if '--crop' in argv:
        box = tuple(int(v) for v in argv[argv.index('--crop') + 1].split(','))
    prefix = prefix if os.path.isabs(prefix) else os.path.join(REPO, prefix)
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if box:
        im = im.crop(box)
    os.makedirs(os.path.dirname(prefix), exist_ok=True)
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        out = f'{prefix}-{w}.webp'
        im.resize((w, h), Image.LANCZOS).save(out, 'WEBP', quality=80, method=6)
        print(f'{os.path.relpath(out, REPO)}  {w}x{h}  {os.path.getsize(out)//1024} KB')

if __name__ == '__main__':
    main(sys.argv[1:])
