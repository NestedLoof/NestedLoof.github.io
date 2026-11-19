"""Build the self-hosted WOFF2 font subsets in assets/fonts/.

    python tools/fonts.py ja      # ONLY the Japanese subset (use this when you add new Japanese/Chinese characters)
    python tools/fonts.py all     # all fonts (rarely needed; see warning)

WARNING: re-running the Latin builds produces different bytes each time (non-deterministic). Do NOT commit
changed Latin fonts unless you meant to change them: `git checkout -- assets/fonts/<file>` to discard.
Only shippori-mincho-subset.woff2 normally needs updating.

Sources (SIL OFL 1.1) go in tools/fontsrc/<family>/ (git-ignored). Download from https://github.com/google/fonts :
    ofl/newsreader/  ofl/ibmplexsans/  ofl/ibmplexmono/  ofl/shipporiminchob1/
Needs fontTools + brotli:  pip install --target tools/pylib fonttools brotli

"Plex" is a Reserved Font Name, so the modified IBM Plex subsets are renamed "LW Sans" / "LW Mono" (OFL 1.1).
The Japanese subset contains only the CJK characters found in the site's HTML (Japanese and Chinese names).
"""
import glob, io, os, re, sys
from _paths import REPO, ASSETS, FONTSRC
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

OUT = os.path.join(ASSETS, 'fonts')
LATIN = ('U+0000-00FF,U+0100-017F,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,'
         'U+2122,U+2190-2193,U+2212,U+2215,U+2715,U+FEFF,U+FFFD')

def rename(font, family):
    for rec in font['name'].names:
        if rec.nameID in (1, 4, 16, 21):
            rec.string = family + ('' if rec.nameID in (1, 16, 21) else ' Regular')
        if rec.nameID == 6: rec.string = family.replace(' ', '') + '-Regular'
        if rec.nameID == 3: rec.string = family + ' (subset of IBM Plex, OFL-1.1)'

def build(src, out, unicodes=None, text=None, family=None, limits=None,
          features='kern,liga,calt,onum,lnum,tnum,pnum,ss01,vert,vrt2,vkna'):
    font = TTFont(os.path.join(FONTSRC, src), lazy=False)
    opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = features.split(',')
    opts.name_IDs = ['*']; opts.notdef_outline = True
    s = subset.Subsetter(opts)
    s.populate(unicodes=subset.parse_unicodes(unicodes) if unicodes else [], text=text or '')
    s.subset(font)
    if limits:   # subset first, then pin variable axes (the other order fails on Plex)
        b = io.BytesIO(); font.flavor = None; font.save(b); b.seek(0)
        font = instancer.instantiateVariableFont(TTFont(b), limits)
    if family: rename(font, family)
    font.flavor = 'woff2'
    path = os.path.join(OUT, out); font.save(path)
    print(out, os.path.getsize(path) // 1024, 'KB')

def japanese():
    html = ''.join(open(f, encoding='utf-8').read() for f in glob.glob(os.path.join(REPO, '**', '*.html'), recursive=True))
    ja = ''.join(sorted(set(re.findall(r'[　-ヿ㐀-鿿＀-￯]', html))))
    print('CJK characters used:', ja)
    if ja:
        build('shipporiminchob1/ShipporiMinchoB1-Medium.ttf', 'shippori-mincho-subset.woff2', text=ja)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode not in ('ja', 'all'):
        sys.exit(__doc__)
    os.makedirs(OUT, exist_ok=True)
    if mode == 'all':
        build('newsreader/Newsreader[opsz,wght].ttf', 'newsreader-roman.woff2', LATIN, limits={'wght': (300, 600)})
        build('newsreader/Newsreader-Italic[opsz,wght].ttf', 'newsreader-italic.woff2', LATIN, limits={'wght': (300, 500)})
        build('ibmplexsans/IBMPlexSans[wdth,wght].ttf', 'lw-sans.woff2', LATIN, family='LW Sans', limits={'wdth': 100, 'wght': (400, 600)})
        build('ibmplexmono/IBMPlexMono-Regular.ttf', 'lw-mono.woff2', LATIN, family='LW Mono')
    japanese()
