#!/usr/bin/env python3
"""Build the static GitHub Pages site.

Reads ``src/`` and writes a deployment-ready ``_site/`` directory:

* substitutes ``{{TOKEN}}`` placeholders with values from ``site.config.json``
  (and from the GitHub Actions environment, when present),
* generates ``sitemap.xml`` with hreflang alternates,
* writes ``robots.txt``, ``.nojekyll`` and an optional ``CNAME``,
* verifies that no placeholder is left behind and that every internal
  link points at a file that exists in the output.

Usage::

    python build.py
    SITE_URL=https://example.com/ python build.py

Only the Python standard library is required.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "_site"
TEXT_SUFFIXES = {".html", ".css", ".js", ".txt", ".xml", ".json", ".webmanifest", ".svg"}
TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")

FALLBACK_SITE_URL = "https://nannan2008.github.io/ebook-voice-player/"


def load_config() -> dict:
    with open(ROOT / "site.config.json", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_site_url(config: dict) -> str:
    """Return an absolute site URL with a trailing slash.

    Priority: SITE_URL env var -> site.config.json ``siteUrl`` ->
    the GitHub Actions repository -> a documented fallback.
    """
    url = (os.environ.get("SITE_URL") or config.get("siteUrl") or "").strip()
    if not url:
        domain = (config.get("customDomain") or "").strip()
        if domain:
            url = f"https://{domain}/"
    if not url:
        repo = os.environ.get("GITHUB_REPOSITORY", "")
        if "/" in repo:
            owner, name = repo.split("/", 1)
            url = f"https://{owner.lower()}.github.io/{name}/"
    if not url:
        url = FALLBACK_SITE_URL
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url if url.endswith("/") else url + "/"


def build_tokens(config: dict, site_url: str) -> dict[str, str]:
    build_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return {
        "SITE_URL": site_url,
        "SITE_URL_NO_SLASH": site_url.rstrip("/"),
        "SITE_HOST": urlsplit(site_url).netloc,
        "APP_NAME": config["appName"],
        "APP_VERSION": config["appVersion"],
        "PUBLISHER": config["publisher"],
        "STORE_URL": config["storeUrl"],
        "REPO_URL": config.get("repoUrl") or site_url,
        "YEAR": str(datetime.now().year),
        "BUILD_DATE": build_date,
        "OG_IMAGE": site_url + "assets/img/og-image.png",
        "VIDEO_URL": site_url + "assets/video/ebook-voice-player-trailer.mp4",
        "VIDEO_POSTER": site_url + "assets/img/trailer-poster.png",
    }


def apply_tokens(text: str, tokens: dict[str, str]) -> str:
    for key, value in tokens.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def generate_sitemap(config: dict, site_url: str, build_date: str) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for page in config["pages"]:
        loc = site_url + page["path"]
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{build_date}</lastmod>")
        lines.append(f"    <changefreq>{page['changefreq']}</changefreq>")
        lines.append(f"    <priority>{page['priority']}</priority>")
        # Only the two home pages are translations of each other.
        if page["path"] in ("", "zh/"):
            lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{site_url}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="zh-Hans" href="{site_url}zh/"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{site_url}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def check_internal_links(out_dir: Path) -> list[str]:
    """Return a list of broken relative href/src references."""
    problems: list[str] = []
    attr_re = re.compile(r'(?:href|src)="([^"]+)"')
    for html_file in out_dir.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        for raw in attr_re.findall(text):
            if raw.startswith(("#", "mailto:", "tel:", "data:", "http://", "https://", "//")):
                continue
            target = unquote(urlsplit(raw).path)
            if not target:
                continue
            resolved = (html_file.parent / target).resolve()
            try:
                resolved.relative_to(out_dir.resolve())
            except ValueError:
                problems.append(f"{html_file.relative_to(out_dir)} -> {raw} (outside site)")
                continue
            if resolved.is_dir():
                resolved = resolved / "index.html"
            if not resolved.exists():
                problems.append(f"{html_file.relative_to(out_dir)} -> {raw}")
    return problems


def main() -> int:
    config = load_config()
    site_url = resolve_site_url(config)
    tokens = build_tokens(config, site_url)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT)

    for path in OUT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8")
            path.write_text(apply_tokens(text, tokens), encoding="utf-8")

    (OUT / "sitemap.xml").write_text(
        generate_sitemap(config, site_url, tokens["BUILD_DATE"]), encoding="utf-8"
    )
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    custom_domain = (config.get("customDomain") or "").strip()
    if custom_domain:
        (OUT / "CNAME").write_text(custom_domain + "\n", encoding="utf-8")

    # Placeholders that survive substitution are a build error.
    leftovers: list[str] = []
    for path in OUT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            for match in TOKEN_RE.findall(path.read_text(encoding="utf-8")):
                leftovers.append(f"{path.relative_to(OUT)}: {match}")
    if leftovers:
        print("Unresolved placeholders:", *leftovers, sep="\n  ", file=sys.stderr)
        return 1

    broken = check_internal_links(OUT)
    if broken:
        print("Broken internal links:", *broken, sep="\n  ", file=sys.stderr)
        return 1

    files = [p for p in OUT.rglob("*") if p.is_file()]
    size = sum(p.stat().st_size for p in files)
    print(f"Built {len(files)} files ({size / 1024:.1f} KiB) into {OUT}")
    print(f"Site URL : {site_url}")
    print(f"Pages    : {', '.join('/' + p['path'] for p in config['pages'])}")
    if custom_domain:
        print(f"CNAME    : {custom_domain}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
