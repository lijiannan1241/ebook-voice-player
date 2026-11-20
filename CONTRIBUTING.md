# Contributing to Ebook Voice Player

Thanks for helping improve Ebook Voice Player. This repository hosts the **product website and the bilingual guide library** (Jekyll / GitHub Pages). The Windows application itself is distributed as a signed MSIX package on the Microsoft Store; its source is not in this repository.

That means the most valuable contributions here are **guides, translations, documentation fixes, and accessibility/SEO improvements** — no app source access is required.

## Ways to contribute

| Contribution | Good for | Where |
|---|---|---|
| Fix a typo, broken link, or outdated fact | Everyone | Any `.md` / `.html` file |
| Improve a guide (EPUB→MP3, TTS voices, etc.) | Writers | `articles/` |
| Add or refine a translation | Bilingual readers | `*.zh.md` / `*.en.md` pairs |
| Report a website bug | Everyone | GitHub Issues |
| Suggest a feature for the app | Users | GitHub Discussions / Issues |

## Ground rules (please read before writing)

1. **Keep facts accurate and current.** Voice/language counts must match the live service: **322 neural voices, 75 languages, 142 regional locales**. Do not reintroduce older figures (300+, 229/56, 80+).
2. **No fabricated claims.** Do not invent pricing, ratings, review counts, or benchmark numbers. Ratings in structured data must come from real Store reviews.
3. **Preserve language parity.** Guides exist in Chinese (`.md`) and English (`.en.md`) pairs. If you edit one, please update the other, or note in the PR that translation is pending.
4. **Links must work under `baseurl`.** Use `{{ site.baseurl }}` for internal links (site is deployed at a subpath: `/ebook-voice-player/`).
5. **Respect the reader.** No keyword stuffing, no misleading claims, no affiliate spam.

## Workflow

1. **Open an issue first** for anything beyond a small typo fix, so we can agree on scope.
2. **Fork** the repository and create a branch: `git checkout -b fix/guide-typo` or `add/zh-guide`.
3. **Edit** the relevant file(s). Guides live in `articles/`; each article has front matter (`title`, `description`, `lang`, `hreflang_en` / `hreflang_zh`).
4. **Check locally** (if you have Ruby/Jekyll):
   ```bash
   bundle install
   bundle exec jekyll serve
   ```
   If you don't have Jekyll, you can still contribute — a maintainer will build it. Just re-read your Markdown for broken links and balanced HTML tags.
5. **Commit** with a clear message: `fix(guide): correct EPUB export steps` or `docs(zh): add sleep timer guide`.
6. **Open a Pull Request** describing what changed and why. Link the issue if there is one.

## Front matter template for a new guide

```yaml
---
layout: default
title: "Your guide title"
description: "One-line summary used in search and social previews."
lang: en                    # 'en' or 'zh-Hans'
hreflang_zh: "/articles/your-slug/"       # on English articles
# hreflang_en: "/articles/your-slug.en/"  # on Chinese articles
---
```

Name the file `articles/your-slug.md` (Chinese) and `articles/your-slug.en.md` (English), so the two languages pair correctly in hreflang tags.

## Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful and constructive.

## Questions?

Open a GitHub Issue or Discussion. For app-specific support (not this website), use the [Support page](https://lijiannan1241.github.io/ebook-voice-player/support/) or the Microsoft Store listing's support link.
