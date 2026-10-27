import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

base = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:8080"
# If base ends with .html, don't add trailing slash
url = base if base.endswith(".html") else base + "/"
html = urllib.request.urlopen(url).read().decode("utf-8")

print("title       :", re.search(r"<title>(.*?)</title>", html, re.S).group(1))
print("description :", len(re.search(r'name="description" content="(.*?)"', html).group(1)), "chars")
print("h1 count    :", len(re.findall(r"<h1[ >]", html)))
print("canonical   :", re.search(r'rel="canonical" href="(.*?)"', html).group(1))
print("json-ld     :", len(re.findall(r'application/ld\+json', html)), "blocks")
for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
    json.loads(block)
print("json-ld     : all blocks parse")
print("images w/o alt:", len(re.findall(r"<img(?![^>]*\balt=)[^>]*>", html)))