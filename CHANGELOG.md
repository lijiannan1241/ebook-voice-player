# Changelog

All notable changes to the **Ebook Voice Player website and guide library** (this repository) are documented here. The Windows application itself is distributed separately on the Microsoft Store; its version is tracked by `site.app_version` in `_config.yml`.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Documentation
- Added `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CITATION.cff` to improve repository discoverability and trust signals.

## [1.0.1.0] - 2026-10-25

> Website/app baseline release. Product figures reflect the live speech service.

### Added
- Bilingual guide library: 10 Chinese + 10 English hands-on articles covering EPUB/PDF/TXT/DOCX to MP3, neural voice selection, commute listening, English learning, low-vision reading, sleep timer, privacy and more.
- AI-discovery assets: `llms.txt`, AI-crawler-friendly `robots.txt`, structured data (SoftwareApplication, FAQPage, HowTo, Article/BlogPosting, VideoObject, BreadcrumbList).
- Multi-language SEO: canonical URLs, reciprocal `hreflang` (en / zh-Hans) across home, support, privacy and all guides.

### Changed
- Unified all first-party product figures to the live service values: **322 neural voices / 75 languages / 142 regional locales**.
- Standardized all Microsoft Store links to the canonical URL with `hl=zh-CN&gl=CN`.
- Rewrote `sitemap.xml` to 26 real URLs with `lastmod`/`changefreq`/`priority`; removed 404 and verification-file entries.

### Fixed
- Corrected `hreflang` pairs that previously pointed every page at the homepage and produced duplicate/self-referential tags.
- Fixed internal links broken by `permalink: pretty` (`/support.html` → `/support/`, same for privacy).
- Corrected guide front matter where `hreflang_en` pointed to the Chinese URL instead of the `.en` counterpart.

[Unreleased]: https://github.com/lijiannan1241/ebook-voice-player/compare/v1.0.1.0...HEAD
[1.0.1.0]: https://github.com/lijiannan1241/ebook-voice-player/releases/tag/v1.0.1.0
