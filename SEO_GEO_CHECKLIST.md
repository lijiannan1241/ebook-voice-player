# SEO / GEO checklist

Run this before the first deploy and again after any content change.
Replace `SITE` with the deployed URL (for example
`https://nannan2008.github.io/ebook-voice-player`).

## 1. Before you push

- [ ] `site.config.json` → `storeUrl` points at the live product page
      (`https://apps.microsoft.com/detail/9nlhln1sjnbr?cid=DevShareMCLPCS`)
      and every store badge/button opens it.
- [ ] `site.config.json` → `siteUrl` is empty (auto-detect) or set to the final
      canonical URL. If using a custom domain, set `customDomain` and enable
      **Enforce HTTPS** in GitHub Pages.
- [ ] App version in `site.config.json` matches the Store package (`1.0.1.0`).
- [ ] `python build.py` reports no unresolved placeholders and no broken links.
- [ ] `_site/` contains `.nojekyll`, `sitemap.xml`, `robots.txt`, `llms.txt`,
      `404.html`, `index.html`, `zh/index.html`.
- [ ] Every page has exactly one `<h1>` and a unique `<title>` (50–60 chars) and
      `meta description` (140–160 chars).
- [ ] Facts agree across the site, the Store listing and the promo article:
      formats, platform, voice count, languages, internet requirement.
      *Known mismatch to fix:* the current Store listing says "229 voices /
      56 languages", while the live service reports 322 voices / 142 locales /
      75 languages (the site says "300+ / 70+"). Update the Store listing or
      align the wording before submitting GEO tests.

## 2. After the first deploy

### Crawlability

```bash
curl -sI  SITE/robots.txt
curl -s   SITE/robots.txt
curl -sI  SITE/sitemap.xml
curl -s   SITE/sitemap.xml | head
curl -sI  SITE/llms.txt
curl -sI  SITE/assets/img/og-image.png
```

- [ ] `robots.txt` returns 200 and contains the correct `Sitemap:` line.
- [ ] `sitemap.xml` returns 200, uses absolute URLs, and lists `/`, `/zh/`,
      `/support.html`, `/privacy.html`.
- [ ] `https://SITE/nonexistent-page` serves `404.html` with `noindex`.
- [ ] No mixed content and no redirect chains.

### Search engines

- [ ] Add the site to **Google Search Console** (domain or URL-prefix
      property). Verify by DNS TXT or the HTML file/tag method.
- [ ] Submit `SITE/sitemap.xml` in Search Console → Sitemaps.
- [ ] URL Inspection → request indexing for `/` and `/zh/`.
- [ ] Add the site to **Bing Webmaster Tools** (you can import from Search
      Console) and submit the same sitemap. Bing feeds Copilot.
- [ ] After 3–7 days, check `site:SITE` and the Page indexing report.

### Structured data

- [ ] [Rich Results Test](https://search.google.com/test/rich-results?url=SITE)
      detects `SoftwareApplication`, `FAQPage`, `VideoObject` and
      `BreadcrumbList` with no errors.
- [ ] [Schema Markup Validator](https://validator.schema.org/#url=SITE) parses
      all blocks.
- [ ] Local parse check (catches trailing commas that browsers ignore):

```bash
python - <<'PY'
import json, re, urllib.request
html = urllib.request.urlopen("SITE").read().decode()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
for i, block in enumerate(blocks, 1):
    json.loads(block)
    print("JSON-LD block", i, "OK")
PY
```

> PowerShell does not support heredocs; save the snippet to a `.py` file and
> run it there, or use `python -c` with single-line code.

### Social previews

- [ ] [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
      → scrape `SITE` and confirm title, description and 1200×630 image.
- [ ] [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
      refreshes the cache.
- [ ] X/Twitter card preview looks correct (use a card validator or a draft
      post).

### Performance / accessibility

- [ ] PageSpeed Insights (mobile) — target LCP < 2.5 s, CLS < 0.1, INP < 200 ms.
      The page is static, uses system fonts and defers the only script.
- [ ] Lighthouse Accessibility ≥ 95: check contrast, focus states, the skip
      link, `alt` text (all decorative art is CSS or `aria-hidden`).
- [ ] Keyboard-only pass: tab through header, hero, FAQ (`details/summary`),
      video controls and footer.
- [ ] `prefers-reduced-motion` disables the reveal animation.

### Internationalisation

- [ ] `/` declares `hreflang="en"`, `/zh/` declares `hreflang="zh-Hans"`, both
      declare `x-default` → `/`.
- [ ] Canonicals are self-referential on each page, not cross-language.
- [ ] Language switch keeps the reader on the equivalent page.

## 3. GEO checks (AI search / assistants)

`llms.txt` and the FAQ are the main levers. Verify they are reachable and that
the facts are quoted correctly:

- [ ] `SITE/llms.txt` returns 200 with `text/plain` and contains the product
      definition, key facts and page links.
- [ ] `robots.txt` does not block `OAI-SearchBot`, `ChatGPT-User`,
      `PerplexityBot`, `ClaudeBot` or `Claude-User`.
- [ ] Ask each assistant the same five questions and compare answers with the
      site (use a fresh chat so results are not cached):

  1. "What is Ebook Voice Player and which ebook formats does it support?"
  2. "Does Ebook Voice Player work offline?"
  3. "How many voices and languages does Ebook Voice Player have?"
  4. "Can Ebook Voice Player export audiobooks to MP3?"
  5. "Is Ebook Voice Player safe for private books — is my book uploaded?"

- [ ] Every answer mentions the correct formats (TXT, DOCX, PDF, EPUB, HTML),
      the internet requirement for synthesis, and MP3 export.
- [ ] The site is cited/linked, or at least summarised without invented
      features. If an assistant hallucinates a feature, add a short, explicit
      sentence to the FAQ or facts table that rules it out.
- [ ] Check referral traffic from `chatgpt.com`, `perplexity.ai`,
      `copilot.microsoft.com` and `gemini.google.com` in analytics — the site
      itself ships no analytics, so use Search Console or a privacy-friendly
      external tool if needed.

### Improving GEO over time

- Keep one canonical fact per sentence: "Ebook Voice Player opens TXT, DOCX,
  PDF, EPUB and HTML." Avoid marketing ambiguity in the facts table.
- Add dated release notes (version + date) so assistants can tell which
  information is current.
- When the Store listing changes, update `site.config.json`,
  `src/index.html`, `src/zh/index.html` and `src/llms.txt` in the same commit.
- Re-run `build.py` after edits — `lastmod` in the sitemap updates
  automatically.

## 4. Quick local audit script

Save as `tools/audit.py` and run `python tools/audit.py http://localhost:8080`
after `build.py`:

```python
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

base = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:8080"
html = urllib.request.urlopen(base + "/").read().decode("utf-8")

print("title       :", re.search(r"<title>(.*?)</title>", html, re.S).group(1))
print("description :", len(re.search(r'name="description" content="(.*?)"', html).group(1)), "chars")
print("h1 count    :", len(re.findall(r"<h1[ >]", html)))
print("canonical   :", re.search(r'rel="canonical" href="(.*?)"', html).group(1))
print("json-ld     :", len(re.findall(r'application/ld\+json', html)), "blocks")
for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
    json.loads(block)
print("json-ld     : all blocks parse")
print("images w/o alt:", len(re.findall(r"<img(?![^>]*\balt=)[^>]*>", html)))
```

Expected: one `<h1>`, description 140–160 characters, canonical absolute, all
JSON-LD blocks parsing, zero `<img>` without `alt`.
