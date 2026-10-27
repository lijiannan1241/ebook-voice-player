# Ebook Voice Player — official website

[![Get it from Microsoft Store](https://img.shields.io/badge/Microsoft_Store-Get_the_app-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN)

Static landing site for **Ebook Voice Player**, built for GitHub Pages and
structured for both classic SEO and generative-engine optimisation (GEO).
No frameworks, no build dependencies, no external requests at runtime.

**📱 Download the app:** [Ebook Voice Player on Microsoft Store](https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN)

```
github-pages/
├─ .github/workflows/deploy.yml   # build + deploy on push to main
├─ src/                           # source templates (tokens in {{...}})
│  ├─ index.html                  # English landing page
│  ├─ zh/index.html               # Simplified Chinese landing page
│  ├─ support.html
│  ├─ privacy.html
│  ├─ 404.html
│  ├─ robots.txt
│  ├─ llms.txt                    # plain-language summary for AI crawlers
│  ├─ site.webmanifest
│  └─ assets/{css,js,img,video}/
├─ site.config.json               # site URL, app facts, store link, pages
├─ build.py                       # stdlib-only static builder
├─ tools/make_images.py           # regenerates icons / OG image / poster (Pillow)
├─ SEO_GEO_CHECKLIST.md           # what to verify after the first deploy
└─ _site/                         # generated output (git-ignored)
```

## 1. Build locally

```bash
python build.py
python -m http.server 8080 --directory _site
# open http://localhost:8080
```

`build.py` copies `src/` to `_site/`, replaces `{{TOKEN}}` placeholders,
generates `sitemap.xml`, writes `.nojekyll` (and `CNAME` when configured),
then fails if any placeholder or internal link is broken.

Python 3.10+ is enough. Pillow is only needed if you want to regenerate images:

```bash
python tools/make_images.py
```

## 2. Configure

Edit `site.config.json`:

| Key | Meaning | Default |
|---|---|---|
| `siteUrl` | Absolute canonical URL. Leave empty in CI to auto-detect from the repository. | auto |
| `customDomain` | Custom domain, e.g. `ebookvoiceplayer.com`. Also writes `CNAME`. | `""` |
| `appName` | Product name shown across the site and in structured data. | `Ebook Voice Player` |
| `appVersion` | Version shown in facts and footer. | `1.0.1.0` |
| `publisher` | Publisher name used in copyright and `Organization`. | `nannan2008` |
| `storeUrl` | Microsoft Store link used by every download button and badge. | `apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN` |
| `repoUrl` | Optional repository URL (empty = canonical site URL). | `""` |
| `pages` | Pages included in `sitemap.xml`. | see file |

The default `storeUrl` is the live product page
(`https://apps.microsoft.com/detail/9nlhln1sjnbr`) with the developer-share
campaign ID `cid=DevShareMCLPCS` and locale parameters `hl=zh-CN&gl=CN`
for Chinese market promotion. The locale parameters ensure visitors see the
Chinese store page; remove them if you want visitors to see their own locale.

### URL resolution order

1. `SITE_URL` environment variable (useful for previews).
2. `siteUrl` in `site.config.json`.
3. `customDomain` (as `https://<domain>/`).
4. `GITHUB_REPOSITORY` → `https://<owner>.github.io/<repo>/` (automatic in Actions).
5. Fallback `https://nannan2008.github.io/ebook-voice-player/`.

All in-page links are relative, so the site works both on a project subpath
(`/<repo>/`) and on a custom domain without changes.

## 3. Deploy to GitHub Pages

1. Create a repository, for example `ebook-voice-player`.
2. Copy the **contents of this folder** to the repository root (the workflow
   must live at `.github/workflows/deploy.yml`).
3. Commit and push to `main`.
4. In the repository: **Settings → Pages → Build and deployment → Source =
   GitHub Actions**.
5. The workflow runs `python build.py` and publishes `_site/`. The URL appears
   in the deployment environment (`https://<owner>.github.io/<repo>/`).
6. If you use a custom domain, set `customDomain` in `site.config.json`,
   configure the DNS records GitHub shows, then enable **Enforce HTTPS**.

No `gh-pages` branch is created; deployment uses the Pages artifact API.

### Automatic canonical URLs

In Actions, `build.py` reads `GITHUB_REPOSITORY` and generates absolute
canonical, Open Graph, sitemap and `llms.txt` URLs for the deployed site. If
you add a custom domain, either set `customDomain` or pass `SITE_URL`:

```yaml
- name: Build static site
  run: python build.py
  env:
    SITE_URL: https://ebookvoiceplayer.com/
```

## 4. What is included for SEO and GEO

**SEO**

- One `<h1>` per page, semantic landmarks, descriptive `title`/`meta description`
- Canonical URL, `hreflang` for `en`, `zh-Hans` and `x-default`
- Open Graph and Twitter card metadata with a 1200×630 image
- `sitemap.xml` with `lastmod`, `robots.txt`, `.nojekyll`
- `BreadcrumbList`, `WebSite`, `Organization`, `SoftwareApplication`,
  `VideoObject` and `FAQPage` JSON-LD
- Visible FAQ text that matches the `FAQPage` markup
- Fast by construction: one CSS file, one small JS file, system fonts,
  lazy video (`preload="none"`), compressed images

**GEO (generative engine optimisation)**

- `llms.txt` with a one-paragraph definition, key facts, page index and links
- A "Quick facts" table that answers the questions an assistant is likely to ask
- Self-contained FAQ answers that make sense when quoted out of context
- Explicit, consistent facts: formats, platform, version, voice count, internet
  requirement, data handling
- `robots.txt` explicitly welcomes `OAI-SearchBot`, `ChatGPT-User`,
  `PerplexityBot`, `ClaudeBot` and `Claude-User`
- No content hidden behind JavaScript; everything is in the HTML source

See `SEO_GEO_CHECKLIST.md` for the post-deploy verification steps.

## 5. Editing content

- English page: `src/index.html`
- Chinese page: `src/zh/index.html`
- Shared styling: `src/assets/css/styles.css`
- Facts used in several places (version, store link, year): `site.config.json`
  or `{{TOKEN}}` placeholders — never hard-code a version number.

After editing, run `python build.py`; it will refuse to finish if a placeholder
or an internal link is broken.

## 6. Notes

- The hero reading view is a **CSS illustration** of the interface, not a
  screenshot. The marketing screenshots captured during Store certification
  contain a font-rendering defect, so they are intentionally not used.
- The trailer is copied from `store_listing_assets/trailer/` (MP4, 1920×1080,
  109 s). Re-copy it if the trailer is re-rendered.
- The site loads no third-party fonts, analytics or cookies; GitHub Pages may
  keep standard access logs (see `src/privacy.html`).
