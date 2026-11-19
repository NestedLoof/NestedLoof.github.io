"""Draw the ルーサー name seal as pure SVG paths (no font dependency at runtime).

    python tools/seal.py

Writes assets/img/brand/seal.svg and assets/favicon.svg from Shippori Mincho B1 Bold glyph outlines
(SIL OFL 1.1 allows embedding glyph outlines in artwork). Needs tools/fontsrc/shipporiminchob1/ and fontTools.
The PNG/ICO favicons (assets/favicon.ico, assets/apple-touch-icon.png) were rasterised from the same design with Pillow.
"""
import os, sys
from _paths import ASSETS, FONTSRC
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
SRC = os.path.join(FONTSRC, 'shipporiminchob1', 'ShipporiMinchoB1-Bold.ttf')
OUT = ASSETS + os.sep
f=TTFont(SRC); gs=f.getGlyphSet(); cmap=f.getBestCmap()
SHU='#B23A25'; PAPER='#F5F0E6'
def glyph(ch, x, y, size, rotate=False):
    pen=SVGPathPen(gs)
    s=size/1000.0
    # font units: y up, em box 0..1000 with baseline ~ 120 from bottom (descender -120 approx)
    if rotate:  # vertical prolonged sound mark: rotate 90° clockwise about cell centre
        t=(0, -s, -s, 0, x+size/2+ (500*s) - 500*s + size/2 - (880-500)*s*0, y+size/2+500*s)
        # derived below more simply
    g=gs[f.getBestCmap()[ord(ch)]]
    if not rotate:
        tp=TransformPen(pen,(s,0,0,-s,x,y+880*s))
    else:
        # map font point (u,v) -> (x + size/2 + (v-380)*s, y + size/2 + (u-500)*s)  (approx centred)
        cx,cy=500,380
        tp=TransformPen(pen,(0,s,s,0,x+size/2-cy*s, y+size/2-cx*s))
    g.draw(tp); return pen.getCommands()
cell=38; pad=10
# right column (read first): ル over ー ; left column: サ over ー
parts=[glyph('ル',50+1,pad,cell), glyph('ー',50+1,50+1,cell,True), glyph('サ',pad+1,pad,cell), glyph('ー',pad+1,50+1,cell,True)]
d=' '.join(parts)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="ルーサー seal">
<rect x="2" y="2" width="96" height="96" rx="7" fill="{SHU}"/>
<rect x="6.5" y="6.5" width="87" height="87" rx="4" fill="none" stroke="{PAPER}" stroke-width="1.6"/>
<path fill="{PAPER}" d="{d}"/>
</svg>'''
os.makedirs(OUT+'img/brand',exist_ok=True)
open(OUT+'img/brand/seal.svg','w',encoding='utf-8').write(svg)
open(OUT+'favicon.svg','w',encoding='utf-8').write(svg.replace(' role="img" aria-label="ルーサー seal"',''))
print(len(svg))
