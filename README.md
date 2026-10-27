# Ebook Voice Player — official website

[![Get it from Microsoft Store](https://img.shields.io/badge/Microsoft_Store-Get_the_app-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN)

Static landing site for **Ebook Voice Player**, built for GitHub Pages with **Jekyll** and
structured for both classic SEO and generative-engine optimisation (GEO).
No frameworks, no build dependencies, no external requests at runtime.

**📱 Download the app:** [Ebook Voice Player on Microsoft Store](https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN)

```
ebook-voice-player/
├─ .github/workflows/deploy.yml   # Jekyll build + deploy on push to main
├─ _layouts/default.html          # Main layout template
├─ _config.yml                    # Jekyll configuration (site URL, app facts, store link)
├─ index.html                     # English landing page (with front matter)
├─ zh/index.html                  # Simplified Chinese landing page
├─ support.html                   # Support page
├─ privacy.html                   # Privacy policy page
├─ 404.html                       # Custom 404 page
├─ robots.txt                     # Robots.txt with AI crawler allowances
├─ llms.txt                       # Plain-language summary for AI crawlers (GEO)
├─ site.webmanifest               # PWA manifest
├─ assets/{css,js,img,video}/     # Static assets
├─ SEO_GEO_CHECKLIST.md           # Post-deploy verification steps
├─ Gemfile                        # Ruby dependencies (jekyll, plugins)
└─ _site/                         # Generated output (git-ignored)
```

## 1. Build locally

### Prerequisites
- Ruby 3.1+
- Bundler (`gem install bundler`)

### Install dependencies
```bash
bundle install
```

### Build and serve
```bash
bundle exec jekyll serve
# open http://localhost:4000/ebook-voice-player
```

The site uses `baseurl: "/ebook-voice-player"` for GitHub Pages project site deployment. For local development, Jekyll serves at `http://localhost:4000/ebook-voice-player/`.

## 2. Configure

Edit `_config.yml`:

| Key | Meaning | Default |
|---|---|---|
| `url` | Base URL for the site (no trailing slash). | `https://lijiannan1241.github.io` |
| `baseurl` | Project subpath for GitHub Pages. | `/ebook-voice-player` |
| `app_name` | Product name shown across the site and in structured data. | `Ebook Voice Player` |
| `app_version` | Version shown in facts and footer. | `1.0.1.0` |
| `publisher` | Publisher name used in copyright and `Organization`. | `nannan2008` |
| `store_url` | Microsoft Store link used by every download button and badge. | `https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS&hl=zh-CN&gl=CN` |
| `repo_url` | Optional repository URL. | `https://github.com/lijiannan1241/ebook-voice-player` |

The default `store_url` is the live product page with the developer-share campaign ID `cid=DevShareMCLPCS` and locale parameters `hl=zh-CN&gl=CN` for Chinese market promotion.

### Custom domain
To use a custom domain:
1. Set `url: "https://your-domain.com"` and `baseurl: ""` in `_config.yml`
2. Add a `CNAME` file to the repository root with your domain
3. Configure DNS records as shown in GitHub Pages settings
4. Enable **Enforce HTTPS** in repository Settings → Pages

## 3. Deploy to GitHub Pages

1. Create a repository (e.g., `ebook-voice-player`)
2. Push this folder's contents to the repository root
3. In the repository: **Settings → Pages → Build and deployment → Source = GitHub Actions**
4. The workflow (`.github/workflows/deploy.yml`) runs `jekyll-build-pages` and publishes `_site/`
5. The URL will be `https://<owner>.github.io/<repo>/` (or your custom domain)

No `gh-pages` branch is created; deployment uses the Pages artifact API.

## 4. What is included for SEO and GEO

**SEO**

- One `<h1>` per page, semantic landmarks, descriptive `title`/`meta description`
- Canonical URL, `hreflang` for `en`, `zh-Hans` and `x-default`
- Open Graph and Twitter card metadata with a 1200×630 image
- `sitemap.xml` with `lastmod`, `robots.txt` (via `jekyll-sitemap` plugin)
- `BreadcrumbList`, `WebSite`, `Organization`, `SoftwareApplication`, `VideoObject` and `FAQPage` JSON-LD
- Visible FAQ text that matches the `FAQPage` markup
- Fast by construction: one CSS file, one small JS file, system fonts, lazy video (`preload="none"`), compressed images

**GEO (generative engine optimisation)**

- `llms.txt` with a one-paragraph definition, key facts, page index and links
- A "Quick facts" table that answers the questions an assistant is likely to ask
- Self-contained FAQ answers that make sense when quoted out of context
- Explicit, consistent facts: formats, platform, version, voice count, internet requirement, data handling
- `robots.txt` explicitly welcomes `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot` and `Claude-User`
- No content hidden behind JavaScript; everything is in the HTML source

See `SEO_GEO_CHECKLIST.md` for the post-deploy verification steps.

## 5. Editing content

- English page: `index.html` (front matter + HTML content)
- Chinese page: `zh/index.html`
- Support page: `support.html`
- Privacy page: `privacy.html`
- Shared styling: `assets/css/styles.css`
- Layout template: `_layouts/default.html`
- Site configuration: `_config.yml` (version, store link, year, etc.)

After editing, run `bundle exec jekyll build` to verify locally.

## 6. Notes

- The hero reading view is a **CSS illustration** of the interface, not a screenshot. The marketing screenshots captured during Store certification contain a font-rendering defect, so they are intentionally not used.
- The trailer is copied from `store_listing_assets/trailer/` (MP4, 1920×1080, 109 s). Re-copy it if the trailer is re-rendered.
- The site loads no third-party fonts, analytics or cookies; GitHub Pages may keep standard access logs (see `privacy.html`).
- Jekyll plugins used: `jekyll-sitemap`, `jekyll-seo-tag`, `jekyll-feed` (configured in `_config.yml` and `Gemfile`).