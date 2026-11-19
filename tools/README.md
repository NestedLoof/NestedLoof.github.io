# Build tools

Small Python scripts that generated the site's assets. The site itself needs none of this at runtime; use them only when changing fonts, images or link-preview images. All paths are relative to the repository, so run them from anywhere.

## Setup (once)

```
pip install pillow
pip install --target tools/pylib fonttools brotli      # needed by fonts.py and seal.py (git-ignored)
```

Download the font sources (SIL OFL 1.1) from https://github.com/google/fonts into `tools/fontsrc/` (git-ignored), keeping one folder per family:

```
tools/fontsrc/newsreader/Newsreader[opsz,wght].ttf   (and Newsreader-Italic[opsz,wght].ttf)
tools/fontsrc/ibmplexsans/IBMPlexSans[wdth,wght].ttf
tools/fontsrc/ibmplexmono/IBMPlexMono-Regular.ttf
tools/fontsrc/shipporiminchob1/ShipporiMinchoB1-Medium.ttf  and  ...-Bold.ttf
```

On Windows set `PYTHONIOENCODING=utf-8` so Japanese characters print.

## Scripts

| Script | Use | Output |
|---|---|---|
| `fonts.py ja` | **Run whenever you add Japanese/Chinese characters to any HTML.** Subsets Shippori Mincho to exactly the CJK characters in the HTML. | `assets/fonts/shippori-mincho-subset.woff2` |
| `fonts.py all` | Rebuild every font. **Rarely needed**: the Latin outputs change byte-for-byte on every run, so discard (`git checkout`) any Latin font you didn't mean to change. | `assets/fonts/*.woff2` |
| `images.py SRC PREFIX W1,W2 [--crop x0,y0,x1,y1]` | Crop, strip metadata, export responsive WebP. Run `python tools/images.py` for the docstring/example. | `PREFIX-<width>.webp` |
| `og.py` | Rebuild the 1200x630 link-preview images (home, sake, games) from the site's photos and fonts. Check by eye; titles can overflow. | `assets/img/og/*.jpg` |
| `seal.py` | Redraw the ルーサー seal from Shippori Bold outlines. | `assets/img/brand/seal.svg`, `assets/favicon.svg` |
| `lowpoly.py` | Regenerate the seeded low-poly wireframe behind the Games band. | `assets/img/brand/lowpoly.svg` |

`seal.py` and `lowpoly.py` reproduce the committed files byte for byte. The PNG/ICO favicons (`assets/favicon.ico`, `assets/apple-touch-icon.png`) were rasterised from the seal with Pillow and aren't scripted; `og.py` reads the apple-touch icon for the small seal in the previews.

## Not here

Original photographs are **not** in the repo (they live in `F:\Misc\Portfolio website\` on Luther's machine). The committed WebP files are the masters. Record every new image in `/CREDITS.md`.
