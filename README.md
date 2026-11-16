# lutherwilliamson.co.uk

This is Luther Williamson's personal website. It's plain static HTML, CSS and a little vanilla JavaScript, served by GitHub Pages from the root of `main`. The custom domain is set in `CNAME`; don't edit or remove it.

## Structure
```
index.html          Homepage (/)
sake/index.html     Japanese sake section (/sake/)
404.html            Not-found page
assets/css/site.css Design system: tokens, layout, components (one file)
assets/js/site.js   Mobile nav, image dialog, gentle reveal (no dependencies)
assets/fonts/       Self-hosted WOFF2 subsets + OFL licences
assets/img/         brand/, home/, sake/, work/, og/ (responsive WebP)
CREDITS.md          Asset & licence register: update it whenever you add an asset
```

## Conventions
- **Always use root-relative URLs** (`/assets/...`, `/sake/`). They work the same from every page, however deeply nested.
- Pages share the same header and footer markup. If you change one, change it in `index.html`, `sake/index.html` and `404.html`.
- Use colours, fonts and spacing from the tokens at the top of `site.css`. Don't hard-code new values.
- Japanese text goes in an element with `lang="ja"`. The Japanese font is a **subset**, so adding new Japanese characters means regenerating `shippori-mincho-subset.woff2`. Until then, those characters fall back to the system mincho font.
- Images: crop and resize to WebP at a few widths (for example 640/1280/1920), strip metadata, set `width`/`height`, and use `loading="lazy"` below the fold.

## Local preview
Root-relative paths don't work over `file://`, so run a small server from the repository root:
```
python -m http.server 8000
```
Then open http://localhost:8000/.

## Adding a tasting or class
Copy an `<li>` in the "Other tastings" list on `sake/index.html`. For a fuller entry, copy the `<article class="event">` block. Only list events that actually happened.

## The Dassai visit journal
The three "Photograph to follow" plates in the Japan section are placeholders. After the visit, replace each `.plate` with a `<figure>` (see the notebook grid for the markup). If the journal grows beyond a few entries, consider moving it to its own pages, for example `/sake/journal/dassai/`.
