# Workflow

How changes were made, tested and shipped during the redesign, and the gotchas hit along the way. Follow this and you'll avoid repeating the mistakes.

## The loop (one round of feedback)

1. Create a branch from the latest `main`: `feature/<short-name>` (or `docs/...`, `chore/...`).
2. Make the change. Edit **all four pages** when touching shared markup (header, footer, nav).
3. **Test in the browser** (see below), at desktop, tablet and mobile widths. Look at it; don't assume.
4. Commit with a clear message. Add the co-author trailer your session instructions give you (it names the current model).
5. Push and open a pull request to `main` with a description of *what* and *why*, and what you tested.
6. Tell Luther what changed, what you checked, and what is unverified. **Ask before merging**; he normally replies "Yes, merge it".
7. After he agrees: merge, wait for GitHub Pages, **verify the live site**, then delete the merged branch (remote and local).

For subjective changes (wording, design) propose the options first and let him approve by number, then implement. This worked well for the "AI look" clean-up.

## Git and GitHub on this machine

- The drive doesn't record ownership, so Git refuses by default. Use `git -c safe.directory=*` on every Git command (don't change the global config).
- Pushing works through Git Credential Manager (no prompts).
- **`gh` is not installed.** Create and merge PRs with the GitHub REST API from Python, with the token from `git credential fill` (`printf "protocol=https\nhost=github.com\n\n" | git credential fill`). Never print or log the token. Pattern:
  - `POST /repos/NestedLoof/NestedLoof.github.io/pulls` with `title`, `head`, `base: main`, `body`.
  - Poll `GET /pulls/<n>` until `mergeable` is true (a fresh PR can return `mergeable: null`, and merging immediately gives HTTP 405; wait a few seconds and retry).
  - `PUT /pulls/<n>/merge` with `{"merge_method":"merge","sha":<head sha>}`.
- The Claude desktop app's PR tools can't bind this repo (it isn't the session's origin); skip them.
- The line-ending warnings ("LF will be replaced by CRLF") are harmless. Files are written with LF.
- Delete merged branches afterwards: `git push origin --delete <branch>`, then `git branch -d <branch>`; fast-forward local `main` to `origin/main`.
- **Never** touch the repo `NestedLoof/PortfolioWebsite`, `CNAME`, DNS or Pages settings.

## Pull request text

End PR descriptions with the attribution line your session instructions specify. Keep PRs small and themed; the history is readable (`git log --oneline`), and each round's rationale is in [decisions.md](decisions.md).

## Testing checklist

Local server: `python -m http.server 8000` from the repo root (or the Claude preview named `site`, configured in the parent folder's `.claude/launch.json` with `--directory site`). Root-relative paths need a server.

- **Widths:** 1440, about 820 (tablet; this is where the contents bar once wrapped), and 375 (mobile). Resize the browser pane; use the mobile preset for the menu.
- **Overflow:** `document.documentElement.scrollWidth` must equal `innerWidth` on every page at 375.
- **Console:** no errors (ignore errors caused by the preview server being down mid-test).
- **Assets and anchors:** every `href`/`src`/`srcset` returns 200; every `#anchor` resolves; cross-page anchors resolve in the target page. A short script that fetches each page, parses it and checks these is quick to write in the page's JS context.
- **Look at every changed section** in a screenshot. Zoom into small things (nav marker, labels).
- **Keyboard:** skip link on first Tab; focus outlines visible; the Menu toggle works and Escape closes it; the image dialog opens with focus on Close.
- **Interactive bits:** collapse/expand "Earlier projects"; a link to `/games/#hungry-bunny` opens the collapsed section; YouTube click-to-play loads the iframe; sticky contents bar highlights the right section.
- **Browser pane caching:** the pane caches CSS/JS aggressively and a normal reload may show stale files. Force it: `await fetch('/assets/css/site.css',{cache:'reload'}); location.reload()` (repeat for JS/HTML you changed).
- **Which site am I looking at?** The pane sometimes holds the *live* site from an earlier check. Verify the address bar says `localhost:8000` before judging local work.
- Chromium only was tested. Safari, Firefox and a real iPhone were not; ask Luther to check on his phone for big changes.

## Deployment and verification

- Pages deploys `main` in about 30-60 seconds after a merge. Poll the live URL with a cache-busting query (`?x=1`, `?x=2`, ...) until a string from the change appears; **a first check right after merging can still show old content**, so re-check before declaring success.
- Then confirm: `/`, `/games/`, `/sake/`, `/404.html` return 200; changed CSS/JS/images return 200; `/CNAME` still says `lutherwilliamson.co.uk`; the old `/html/index-2.html` (removed template page) returns 404; no console errors on the live pages.
- Remind Luther that a hard refresh (Ctrl+F5) clears his cached copy, and that link previews on LinkedIn/WhatsApp cache the old image for a while.

## Assets

Scripts and instructions are in [../tools/README.md](../tools/README.md).

- **Photos:** crop (remove any app UI), export responsive WebP (about 640/1000/1500 widths), strip metadata, set `width`/`height`, `loading="lazy"` below the fold, meaningful `alt`. Add a `CREDITS.md` row. Originals live **outside** the repo in `F:\Misc\Portfolio website\` (not committed); the committed WebPs are the masters.
- **Fonts:** only regenerate the Japanese subset (`python tools/fonts.py ja`) when CJK characters are added. Re-running the Latin builds changes the bytes non-deterministically, so **discard** changed Latin fonts (`git checkout -- assets/fonts/<file>`) and commit only the Shippori subset.
- **Link-preview images:** `python tools/og.py`. Rebuild `home.jpg` when the portrait changes. Check by eye.
- **Sitemap:** add new pages to `sitemap.xml`, with `lastmod`. `robots.txt` allows crawling and links the sitemap.
- Verification/analytics files at the root: `googlea2066997de2fe5dd.html` (Google Search Console; **keep it**) and the GoatCounter script (`woffus.goatcounter.com`) before `</body>` on each page; add it to any new page.

## Editing tips and gotchas learned

- **A stray CSS fragment can silently break a different section.** After removing or rewriting a block in the middle of `site.css`, check brace balance and look at the *neighbouring* sections in the browser. (A leftover from the old contents-bar media query once collapsed the "Why sake" text column to 65px. Luther spotted it.)
- When removing page content, remove its CSS too (dead rules were cleaned up for the journal placeholders), and check spacing where the removed block used to be (the Japan section needed explicit bottom spacing).
- Windows Python defaults to cp1252: set `PYTHONIOENCODING=utf-8` for scripts that print Japanese, write files with `encoding="utf-8", newline="\n"`, and prefer `\uXXXX` escapes or the Write tool for strings with CJK/typographic characters inside shell heredocs.
- Prefer plain Python scripts or the Edit tool for multi-line replacements; `sed` is fine for one-liners.
- Use apostrophes/quotes as typographic characters (’ “ ”) in visible text, consistent with the rest of the copy.
- Keep `style="..."` inline attributes out of new markup; add classes to `site.css`.
- Respect `prefers-reduced-motion` in anything animated.

## Privacy while working

Don't put Luther's personal details (birth date, phone number, passwords, tokens) into code, docs, commits or PR text. The repo is public and the whole repo is served by Pages. Documents in `docs/` and `tools/` are publicly readable (they are disallowed in `robots.txt` to discourage indexing, which does not hide them).
