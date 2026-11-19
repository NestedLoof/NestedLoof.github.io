# Roadmap and open items

Status as of **19 November 2026**. Update this file when something is done or a new follow-up appears.

## Time-triggered

- **After 3 December 2026: the Dassai brewery visit (Yamaguchi).** In `sake/index.html` (Japan section): change the status line from "Upcoming" to past tense, rewrite "The visit is scheduled for 3 December 2026" to what happened, and replace "I'll write about the visit here afterwards" with a real write-up and **Luther's own photos** as `<figure>`s (see the tasting note markup; credit them in `CREDITS.md`). Also update the contents link, the meta description ("an upcoming visit to Dassai") and the homepage sake band text if they still say "visit" in the future tense. If it grows beyond a few entries, give it its own page (for example `/sake/dassai/`) and add it to `sitemap.xml`. **Only describe what he tells you actually happened.**
- **2027: Hive Mind release.** Add a Steam wishlist/store link when a store page exists; update "Release 2027" to the real date.

## Waiting on Luther

- **Replace the CV.** The `.docx` in `assets/docs/` is from 2024 and includes a phone number. Ask for an updated **PDF**; then remove the old file, update the link and the "last updated" label on the homepage. (Until then it was left as is, by his choice.)
- **New hero portrait:** if Luther supplies another, export it with `tools/images.py` and rebuild the home link-preview image with `python tools/og.py`.
- **Death with Dice:** concept art or screenshots to replace the "In development" box.
- **Hive Mind:** screenshots or a short looping clip would strengthen the games page.
- **Freelance 3D modelling:** currently a single line with no images; renders (with client permission) would help.
- **More tasting notes** (currently one). Ask for sake, date, place and his own description. Copy the `<article class="note">` block.
- **More classes/tastings**, with real dates, when they happen (only list events that took place). The Piko Kitchen and private tastings are undated.
- **Native-speaker check** of the Japanese copy (tagline 日本酒の魅力を、英国へ。 and the LINE line), and possibly a short Japanese introduction for breweries.
- **Offbeat:** if teammates provide anything else, credit them. The game page lives at `vilis.itch.io/offbeat`.
- **Chimera Noodle Run** (trailer on his YouTube channel) is not on the site. Ask whether to add it as a project.

## Technical follow-ups

- In Google Search Console (verified via the root HTML file): submit `sitemap.xml`. Keep `googlea2066997de2fe5dd.html`.
- Test on **Safari, Firefox and a real iPhone** (only Chromium was tested).
- Keep `sitemap.xml` `lastmod` current when pages change.
- Dead CSS: `.band-night + .games` (the dark band no longer sits directly above the games band) and any rules left from removed blocks can be pruned; check by looking, not by search alone.
- If GoatCounter is ever replaced, update `CREDITS.md` ("Visitor statistics") and every page's snippet.
- Check the `<head>` meta descriptions when content changes, especially the sake page's.

## Ideas (not chosen; only if Luther asks)

Mailing-list sign-up (Buttondown/MailerLite), contact form (Formspree/Web3Forms), "book a call" (Cal.com), Steam wishlist button, auto-updating YouTube section, a Japanese version of the sake page, separate pages per tasting note, a pinned "latest from YouTube" strip. Each would need an outside account, so Luther would sign up and Claude would prepare the site side.
