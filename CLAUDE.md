# CLAUDE.md: read this first

This is **lutherwilliamson.co.uk**, Luther Williamson's personal website: indie game developer, freelance 3D modeller, WSET Level 3 sake educator and Dassai Sake Prize winner (2026). It is a hand-written static site (HTML, one CSS file, a little vanilla JS), served by GitHub Pages from the root of `main` in the repo `NestedLoof/NestedLoof.github.io`.

The site was redesigned in November 2026 over many rounds of feedback. **The decisions, preferences and mistakes from that work are written down so you don't have to rediscover them.** Read the docs below before changing anything.

| Read | For |
|---|---|
| [docs/design.md](docs/design.md) | Visual language, tokens, layout, components, accessibility, the "avoid AI tells" rules |
| [docs/content.md](docs/content.md) | Verified facts about Luther, what must **never** be claimed, tone of voice, copyright rules, page-by-page content decisions |
| [docs/workflow.md](docs/workflow.md) | Git/PR/merge process, how to test, asset pipeline, deployment checks, gotchas |
| [docs/decisions.md](docs/decisions.md) | Chronological log of what was decided and why (and what was tried and rejected) |
| [docs/roadmap.md](docs/roadmap.md) | Known follow-ups, things waiting on Luther, ideas not yet chosen |
| [README.md](README.md) | File layout and how to add a tasting, a tasting note, etc. |
| [CREDITS.md](CREDITS.md) | Licence and permission register for every asset. **Update it whenever you add an asset.** |
| [tools/README.md](tools/README.md) | Build scripts: fonts, images, seal, link-preview images |

## Hard rules (set by Luther, do not break)

1. **Never modify the repo `NestedLoof/PortfolioWebsite`.** Only this repo.
2. **Never commit directly to `main`.** Work on a branch, open a pull request, and **merge only after Luther says so** in that round (he normally answers "Yes, merge it"). Don't merge on your own initiative.
3. **Never change DNS, GitHub Pages settings, or the `CNAME` file.** Don't edit or remove `CNAME`.
4. **Factual accuracy.** Don't imply he runs an import business, works for or represents Dassai or any brewery, has visited breweries he hasn't, taught events he hasn't, or has testimonials/awards he doesn't. Details in [docs/content.md](docs/content.md).
5. **Copyright.** No brewery logos or promotional images, no stock or AI-generated images, don't post the WSET results letter/certificate, don't use the Dassai polishing card. Every photo needs a row in `CREDITS.md` with its permission status. Don't name other companies' games as inspiration (the Kurushi mention was removed for legal reasons).
6. **The repo is public and every file is served at the site.** Don't put private information (birth date, phone numbers beyond what's already on the contact section, credentials, tokens) in code, docs or commit messages.

## Luther's style preferences (learned the hard way)

- He **dislikes anything that looks AI-generated**: numbered sections ("01 / 02"), slogan headlines, an italic accent word in a headline, full stops at the end of titles, repeating the same credentials everywhere, small all-caps labels that repeat their heading, arrows on every link, placeholder boxes ("Photograph to follow"), filler like "I'm always happy to hear from people". Prefer plain headings and specific, slightly unexpected real details in his own voice. See [docs/design.md](docs/design.md#avoid-the-ai-look).
- He reviews work visually and by **approving numbered lists of proposed changes**. For subjective changes, propose before/after wording and let him pick.
- He gives short feedback ("the formatting looks wrong", "needs centering"). When something looks wrong, look at it in the browser at several widths before fixing; the cause is often a CSS slip of yours.
- He wants **facts checked against what he actually told you**. When unsure of a fact (a date, a credit), ask rather than invent.
- Keep replies plain and concise. Say what changed, what you checked, and what is still unverified.

## Quick facts for working here

- Local preview: `python -m http.server 8000` from the repo root, then http://localhost:8000/. Root-relative URLs (`/assets/...`) don't work over `file://`.
- Git on this Windows machine needs `git -c safe.directory=*` on each command (the drive doesn't record ownership). `gh` is not installed: create/merge PRs with the GitHub REST API, token from `git credential fill` (never print it). See [docs/workflow.md](docs/workflow.md).
- Pages share header/footer markup: a nav change must be made in **all four** pages (`index.html`, `games/index.html`, `sake/index.html`, `404.html`).
- All colours/fonts/spacing come from the tokens at the top of `assets/css/site.css`. Don't hard-code new values.
- After merging, GitHub Pages takes about 30-60 seconds. Verify the **live** site, with a cache-busting query string.
- Prior art: `Phase-1-Plan.md` (outside the repo, in the parent folder) is the original audit and plan. It is historical and partly superseded; the docs here are current.
