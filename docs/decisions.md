# Decisions log

A chronological record of how the site reached its current state: what Luther asked for, what was decided, what was tried and rejected, and mistakes worth not repeating. Newest rounds last. PR numbers refer to `NestedLoof/NestedLoof.github.io`.

## Phase 1: audit and plan (before any code)

Original site: the **"Virtual Folio" template** (MACode ID, CC BY 4.0) on Bootstrap 4, jQuery and about nine plugins, with demo pages in `/html/`, unverified stock images, a Google Maps script pointing at the template's Jakarta coordinates, and personal-info fields (age, gender, GCSEs, empty skill bars, "currently enrolled" bootcamp copy) that were wrong or unwanted. The plan (`Phase-1-Plan.md`, outside the repo) recommended replacing it with a hand-written static site, adding a substantial sake section, and recording provenance for every asset.

Luther's answers to the open questions shaped everything after:
- He became an **indie developer after quitting the medical software job** (not via the bootcamp first).
- The Dassai prize is for the **two highest-scoring students worldwide** on WSET Level 3 Sake.
- He taught a **2-hour class** for 12 guests (slides, tasting sheets, technical Q&A), with **Jennifer Yeung** supplying and serving the sake; plus a wine-vs-sake tasting with **Piko Kitchen** (about 15 people) and private tastings.
- The **X account is inactive** (removed). **CV left as is for now.** All supplied photos have permission, but **don't post the WSET results letter/certificate**, and **don't use or redraw the Dassai polishing card**.
- He is "actually 29": age is not displayed (a deliberate privacy choice).

## Phase 2: build (PR #1, merged)

Checkpoints: (1) homepage and design system, (2) sake page, (3) visual refinement with browser testing, (4) review (accessibility, links, licensing) and PR.

- **No framework or build step.** Plain HTML, one CSS file (`assets/css/site.css`), ~100 lines of vanilla JS. GitHub Pages serves it as is; `.nojekyll` added. Root-relative URLs so pages work at any depth. Bootstrap, jQuery, icon fonts, template demo pages, `LICENSE.txt`/`Credits.txt` and stock photos were all removed (originals remain in git history).
- **Design concept "polished to the core"**, with warm paper, ink, a muted vermilion, Japanese-editorial typography and a ルーサー name seal as logo/favicon (see [design.md](design.md)).
- **Fonts:** self-hosted OFL subsets (no Google Fonts requests). Plex renamed "LW Sans/Mono" because of the Reserved Font Name. Japanese font subset to just the characters used.
- **Provenance:** `CREDITS.md` records every asset; photos cropped to remove Instagram UI, converted to responsive WebP, metadata stripped.
- **Extras:** `404.html`, `sitemap.xml`, `robots.txt`, Open Graph/Twitter images (1200x630), canonical URLs, JSON-LD `Person`, skip link, focus styles, native `<dialog>` lightbox, reduced-motion support.
- **Sake page** was built as a substantial section: why sake, recognition, classes, tasting, Japan, producers & UK, contact. Framed with care to say only what's true (see [content.md](content.md)).

First round of Luther's feedback (all applied before merging):
- Combine the homepage "sake" and "recognition" facts into one entry: "Sake / Educator and enthusiast / Dassai prize + WSET distinction".
- Add **WhatsApp** next to LINE.
- Rename the **Work** tab to **Games**.
- Reword the Dassai sentence (WSET Pass with Distinction, one of the two highest scorers, which led to the prize and the bursary).
- Glossary: **ginjo** instead of shubo.
- Remove the second prize/certificate photo; fix a gallery caption that another photo covered.
- Turn "Sakes I've tasted" into **tasting notes** (blog-like), starting with the Tamagawa Red Label ("bacon and almonds").
- Simplify the industry section to: he doesn't currently run the business, is interested in talking, the UK needs more sake and wider styles, contact link.
- Add the Dassai visit date (3 December 2026).

Luther then approved publishing ("I'm happy to update the website with this version"), and PR #1 was merged. The original brief said not to merge; **merging after his explicit approval each round became the working rule.** Verified live: pages, assets, `CNAME` intact, old template pages return 404.

## Round 1 (PR #2): navigation, Games page, new projects

- **"Why is Sake red with a diamond even when unselected?"** It had been a permanent highlight. *Decision:* the red text and diamond mean "you are here" (`aria-current`), never permanent.
- **Games section theme.** Luther suggested a different look. *Decision:* deep indigo with a rice-straw accent and a faint low-poly wireframe (ties to Polygon Dungeon and 3D work); vermilion stays for sake; screenshots in viewport-style frames.
- **Nav confusion.** Sake was a separate page but Games/About/Contact scrolled the homepage. Options offered: (1) just restyle, or (2) make every nav item the same kind of thing. **Chosen: option 2.** Games got its own page `/games/`; the homepage keeps a teaser band; nav became Games · Sake · About + a **Contact button**. The interim scroll-spy for the homepage nav was removed as unnecessary.
- **New projects** added in chronological order, then **reversed to newest first** by Luther, with **everything before Offbeat collapsed** under "Earlier projects" and **YouTube kept open**. Offbeat (Feb 2026), Hive Mind (solo, release 2027) and Death with Dice (upcoming, working title) were added with the facts in [content.md](content.md). YouTube videos use click-to-play with the no-cookie player.
- The sake contact list's link to the site's own URL was removed ("it shouldn't have a link to this website").
- **Section numbers removed**: first from the games page ("a little AI"), then site-wide on request. The numbered contents bar's wrapping at about 800px was fixed by this.
- The Dassai prize photo was centred.
- Mistakes: the preview pane sometimes showed the live site, so the new Games page wasn't visible to Luther (always check the address bar); research of the YouTube channel was blocked by YouTube's consent page for non-browser fetches (use the browser pane and decline optional cookies).

## Round 2 (PR #3): polish suggestions 1-5

Luther asked what else could be improved; five were approved: (1) **break up the two dark homepage bands** by moving About between them and making Contact light, (2) **sticky sake contents bar** that highlights the section in view and scrolls sideways on phones, (3) a **link-preview image for the games page**, (4) a **dark header for the games page**, (5) a **new portrait**, with the old one moved to About.
- Hive Mind confirmed as **C++ and Unreal Engine 5**.
- **Bug (mine, fixed):** a leftover fragment of the old contents-bar media query broke the CSS after it, collapsing the "Why sake" column. Luther noticed it in the preview. This is why [workflow.md](workflow.md) says to check neighbouring sections after editing the middle of the stylesheet.

## Round 3 (PR #4): hero wording

The homepage's last hero sentence became: "Winner of the 2026 Dassai Sake Prize, and now looking to turn a passion for sake into a career." (Luther wanted to state his career ambition rather than list WSET again.)

## Round 4 (PR #5): removing the "AI look"

Luther asked whether anything looked obviously AI-designed or worded. The audit listed slogan headlines, repeated credentials, stock phrases, lists of three, sales-pitch lines, all-caps labels, italic accent words, arrows everywhere and placeholders. **He approved all 16 proposed changes**, with three additions: *no full stops in titles*; "In my opinion it's the best drink to pair with any food" instead of "brilliant with food"; and replacing some Dassai mentions with "brewery visits". Results are in [design.md](design.md#avoid-the-ai-look) and [content.md](content.md).
- Same PR: a line break after the Japanese name in the sake intro; Chinese name 韋騄瑟 added in the homepage hero (and JSON-LD); the remaining red section labels above headings (Recognition, Classes & tastings, Japan & breweries, About) removed on his prompting ("correct me if I am wrong": he was right, because each heading already says what the section is).
- The Japan section's journal placeholders and the "no public events" line were removed (no empty states).

## Housekeeping

- **PR #6:** Google Search Console HTML verification file added at the root (keep it).
- **PR #7:** GoatCounter visitor statistics (cookie-free; account `woffus`) on every page; `CREDITS.md` and README updated.
- **PR #8:** Hive Mind's inspiration is now "classic puzzle games" (named commercial game removed, for legal safety); the homepage games band title is "Game development".
- All merged branches were deleted from GitHub and locally; the repo has just `main`.
- This documentation set (`CLAUDE.md`, `docs/`, `tools/`) was added so future sessions can continue without the conversation history.

## Ideas offered but not chosen (as of Nov 2026)

Mailing-list sign-up, contact form, Cal.com booking link, Steam wishlist button (once there's a Steam page), automatic YouTube feed, a Japanese-language sake page for breweries, tasting notes as individual pages. Only Search Console and GoatCounter were taken up. See [roadmap.md](roadmap.md).
