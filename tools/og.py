"""Build the 1200x630 Open Graph (link-preview) images: assets/img/og/{home,sake,games}.jpg

    python tools/og.py

Composed from the site's own photos and fonts (tools/fontsrc/). Rebuild home.jpg when the hero portrait changes.
Text uses the same palette as the site. Check the output by eye: long titles can overflow.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
from _paths import ASSETS, IMG, FONTSRC

OUT = os.path.join(IMG, 'og'); os.makedirs(OUT, exist_ok=True)
PAPER = (245, 240, 230); INK = (30, 28, 25); SOFT = (90, 84, 75); SHU = (178, 58, 37)
KOJI = (205, 185, 143); INDIGO = (24, 32, 45); INDIGO_SOFT = (183, 192, 204)

def serif(size, w=360):
    f = ImageFont.truetype(os.path.join(FONTSRC, 'newsreader', 'Newsreader[opsz,wght].ttf'), size)
    try: f.set_variation_by_axes([72, w])
    except Exception as e: print('variation axes:', e)
    return f
sans = ImageFont.truetype(os.path.join(FONTSRC, 'ibmplexsans', 'IBMPlexSans[wdth,wght].ttf'), 26)
mono = ImageFont.truetype(os.path.join(FONTSRC, 'ibmplexmono', 'IBMPlexMono-Regular.ttf'), 20)
mincho = lambda s: ImageFont.truetype(os.path.join(FONTSRC, 'shipporiminchob1', 'ShipporiMinchoB1-Medium.ttf'), s)
seal = Image.open(os.path.join(ASSETS, 'apple-touch-icon.png')).convert('RGBA').resize((64, 64), Image.LANCZOS)

def photo(path, w, h, centering=(.5, .4)):
    return ImageOps.fit(Image.open(path).convert('RGB'), (w, h), Image.LANCZOS, centering=centering)

def base(bg):
    c = Image.new('RGB', (1200, 630), bg); c.paste(seal, (72, 64), seal); return c, ImageDraw.Draw(c)

# Home
c, d = base(PAPER)
c.paste(photo(os.path.join(IMG, 'home', 'portrait-1200.webp'), 420, 630, (.5, .3)), (780, 0))
d.text((72, 170), 'LEEDS, UNITED KINGDOM', font=mono, fill=SOFT)
d.text((68, 205), 'Luther', font=serif(112), fill=INK); d.text((68, 315), 'Williamson', font=serif(112), fill=INK)
d.text((72, 470), 'Games, software and Japanese sake.', font=serif(38, 340), fill=INK)
d.text((72, 530), 'WSET Level 3 in Sake \u00b7 Dassai Sake Prize 2026', font=sans, fill=SOFT)
c.save(os.path.join(OUT, 'home.jpg'), quality=86)

# Sake
c, d = base(PAPER)
c.paste(photo(os.path.join(IMG, 'sake', 'hero-bottle-1500.webp'), 420, 630), (780, 0))
d.text((72, 175), '\u65e5\u672c\u9152\u306e\u9b45\u529b\u3092\u3001\u82f1\u56fd\u3078\u3002', font=mincho(54), fill=INK)
d.text((72, 262), 'SHARING THE APPEAL OF JAPANESE SAKE WITH THE UK', font=mono, fill=SOFT)
d.text((68, 330), 'Japanese sake', font=serif(92), fill=INK)
d.text((72, 450), 'Luther Williamson', font=serif(40, 380), fill=SHU)
d.text((72, 520), 'WSET Level 3 in Sake \u00b7 Dassai Sake Prize 2026', font=sans, fill=SOFT)
c.save(os.path.join(OUT, 'sake.jpg'), quality=86)

# Games (indigo, with an Offbeat screenshot)
c, d = base(INDIGO)
c.paste(photo(os.path.join(IMG, 'work', 'offbeat-party-1600.webp'), 560, 630, (.45, .5)), (640, 0))
d.line([(640, 0), (640, 630)], fill=KOJI, width=2)
d.text((72, 170), 'GAMES \u00b7 3D \u00b7 SOFTWARE', font=mono, fill=KOJI)
d.text((68, 205), 'Games, 3D', font=serif(96), fill=PAPER); d.text((68, 305), 'and software.', font=serif(96), fill=PAPER)
d.text((72, 455), 'Luther Williamson', font=serif(40, 380), fill=KOJI)
d.text((72, 525), 'Hive Mind \u00b7 Offbeat \u00b7 Death with Dice', font=sans, fill=INDIGO_SOFT)
c.save(os.path.join(OUT, 'games.jpg'), quality=86)
print('wrote', sorted(os.listdir(OUT)))
