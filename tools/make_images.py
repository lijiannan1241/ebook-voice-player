#!/usr/bin/env python3
"""Generate the raster assets used by the site (icons, OG image, poster).

Run from the ``github-pages`` folder:

    python tools/make_images.py

Requires Pillow. Output is written to ``src/assets/img``.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

FONTS = Path(r"C:\Windows\Fonts")
SERIF_BOLD = FONTS / "georgiab.ttf"
SERIF = FONTS / "georgia.ttf"
SANS = FONTS / "segoeui.ttf"
SANS_BOLD = FONTS / "segoeuib.ttf"

NAVY = (16, 23, 38)
NAVY_2 = (24, 33, 52)
PAPER = (246, 241, 230)
AMBER = (224, 163, 62)
TEAL = (43, 140, 133)
MUTED = (176, 181, 191)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def rounded(draw: ImageDraw.ImageDraw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size)
    draw = ImageDraw.Draw(image)
    for y in range(height):
        t = y / max(height - 1, 1)
        color = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (width, y)], fill=color)
    return image


def glow(size: tuple[int, int], center: tuple[int, int], radius: int, color: tuple[int, int, int], strength: int) -> Image.Image:
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    steps = 26
    for step in range(steps, 0, -1):
        r = int(radius * step / steps)
        alpha = int(strength * (1 - step / steps) ** 1.7)
        draw.ellipse(
            [center[0] - r, center[1] - r, center[0] + r, center[1] + r],
            fill=color + (alpha,),
        )
    return layer.filter(ImageFilter.GaussianBlur(radius // 6))


def draw_brand_mark(draw: ImageDraw.ImageDraw, x: int, y: int, size: int, radius: int | None = None):
    """Draw the book + sound-wave mark at (x, y)."""
    scale = size / 64
    r = radius if radius is not None else round(14 * scale)
    rounded(draw, [x, y, x + size, y + size], r, fill=NAVY)

    def p(px, py):
        return (x + px * scale, y + py * scale)

    # Book body
    draw.polygon([p(14, 15.5), p(17.5, 12), p(48, 12), p(48, 47), p(17.5, 47), p(14, 50.5)], fill=PAPER)
    rounded(draw, [*p(14, 12), *p(18, 51)], round(3.5 * scale), fill=PAPER)
    # Text lines
    draw.line([p(22, 22), p(38, 22)], fill=NAVY, width=max(2, round(3.2 * scale)))
    draw.line([p(22, 29), p(34, 29)], fill=NAVY, width=max(2, round(3.2 * scale)))
    # Sound waves
    draw.line([p(43, 33), p(43, 47)], fill=AMBER, width=max(2, round(3.6 * scale)))
    draw.line([p(50, 38), p(50, 44)], fill=AMBER, width=max(2, round(3.6 * scale)))


def make_icon(size: int, path: Path, pad_ratio: float = 0.0):
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    pad = round(size * pad_ratio)
    draw_brand_mark(draw, pad, pad, size - pad * 2, radius=round(size * 0.22))
    canvas.save(path)


def make_favicon_32():
    # Small sizes read better with a tighter crop and thicker strokes.
    size = 32
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    rounded(draw, [0, 0, size - 1, size - 1], 7, fill=NAVY)
    draw.polygon([(6, 8), (8, 6), (25, 6), (25, 25), (8, 25), (6, 26)], fill=PAPER)
    rounded(draw, [6, 6, 9, 26], 2, fill=PAPER)
    draw.line([(11, 11), (21, 11)], fill=NAVY, width=2)
    draw.line([(11, 15), (18, 15)], fill=NAVY, width=2)
    draw.line([(23, 17), (23, 24)], fill=AMBER, width=2)
    draw.line([(27, 19), (27, 22)], fill=AMBER, width=2)
    image.save(OUT / "favicon-32.png")


def make_og_image():
    width, height = 1200, 630
    base = vertical_gradient((width, height), (14, 21, 35), (19, 28, 45)).convert("RGBA")
    base.alpha_composite(glow((width, height), (120, 40), 620, AMBER, 90))
    base.alpha_composite(glow((width, height), (1080, 620), 560, TEAL, 95))
    draw = ImageDraw.Draw(base)

    card = (772, 96, 1140, 536)
    border = (54, 65, 84)
    bar_idle = (78, 88, 105)
    amber_bar_bg = (74, 62, 42)
    track_bg = (76, 86, 103)

    # Top brand row
    draw_brand_mark(draw, 72, 58, 44, radius=11)
    draw.text((130, 66), "EBOOK VOICE PLAYER", font=font(SANS_BOLD, 17), fill=(205, 210, 220))

    # Headline — size chosen to stay clear of the card
    headline = font(SERIF_BOLD, 66)
    draw.text((72, 150), "Turn any book", font=headline, fill=(250, 246, 236))
    draw.text((72, 228), "into an audiobook.", font=headline, fill=(250, 246, 236))

    # Sub line
    draw.text(
        (74, 330),
        "Read TXT, DOCX, PDF, EPUB and HTML aloud on Windows.",
        font=font(SANS, 24),
        fill=(186, 192, 203),
    )

    # Pills
    pill_font = font(SANS_BOLD, 19)
    x = 74
    for label in ("300+ voices", "70+ languages", "MP3 export"):
        text_width = draw.textlength(label, font=pill_font)
        box_width = text_width + 38
        rounded(draw, [x, 396, x + box_width, 442], 23, fill=(30, 40, 59), outline=(62, 73, 92), width=1)
        draw.text((x + 19, 405), label, font=pill_font, fill=(236, 231, 220))
        x += box_width + 12

    # Footer
    draw.text((74, 542), "Windows 10 & 11  ·  Microsoft Store", font=font(SANS, 19), fill=(150, 157, 170))

    # Reading card
    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        [card[0] + 8, card[1] + 18, card[2] + 8, card[3] + 18], radius=22, fill=(0, 0, 0, 120)
    )
    base.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
    draw = ImageDraw.Draw(base)

    rounded(draw, card, 22, fill=(22, 31, 48), outline=border, width=1)
    # Window bar
    draw.line([(card[0] + 1, card[1] + 44), (card[2] - 1, card[1] + 44)], fill=(44, 54, 72))
    for i, color in enumerate(((217, 116, 95), AMBER, (90, 167, 159))):
        cx = card[0] + 24 + i * 17
        draw.ellipse([cx, card[1] + 18, cx + 9, card[1] + 27], fill=color)

    # Text bars
    draw.text((card[0] + 26, card[1] + 66), "Chapter 1", font=font(SANS_BOLD, 14), fill=AMBER)
    draw.text((card[0] + 26, card[1] + 88), "The Raven", font=font(SERIF_BOLD, 30), fill=(248, 244, 235))

    y = card[1] + 150
    widths = (270, 300, 230, 290, 205, 250, 185)
    for index, bar_width in enumerate(widths):
        if index == 2:
            rounded(draw, [card[0] + 18, y - 7, card[0] + 18 + bar_width + 26, y + 15], 6, fill=amber_bar_bg)
            draw.rectangle([card[0] + 18, y - 7, card[0] + 21, y + 15], fill=AMBER)
            draw.rounded_rectangle([card[0] + 30, y, card[0] + 30 + bar_width, y + 7], 3, fill=(250, 246, 235))
        else:
            draw.rounded_rectangle([card[0] + 30, y, card[0] + 30 + bar_width, y + 7], 3, fill=bar_idle)
        y += 30

    # Player bar
    draw.line([(card[0] + 1, card[3] - 62), (card[2] - 1, card[3] - 62)], fill=(44, 54, 72))
    draw.ellipse([card[0] + 24, card[3] - 46, card[0] + 56, card[3] - 14], fill=AMBER)
    draw.polygon(
        [(card[0] + 36, card[3] - 38), (card[0] + 36, card[3] - 22), (card[0] + 49, card[3] - 30)],
        fill=(35, 23, 0),
    )
    track_y = card[3] - 32
    draw.rounded_rectangle([card[0] + 70, track_y - 2, card[2] - 24, track_y + 2], 2, fill=track_bg)
    draw.rounded_rectangle([card[0] + 70, track_y - 2, card[0] + 70 + 110, track_y + 2], 2, fill=TEAL)

    base.convert("RGB").save(OUT / "og-image.png", optimize=True)
    return base


def make_trailer_poster():
    width, height = 1920, 1080
    base = vertical_gradient((width, height), (13, 20, 33), (20, 30, 48)).convert("RGBA")
    base.alpha_composite(glow((width, height), (300, 120), 900, AMBER, 80))
    base.alpha_composite(glow((width, height), (1650, 980), 850, TEAL, 80))
    draw = ImageDraw.Draw(base)

    # Top brand row
    draw_brand_mark(draw, 120, 96, 64, radius=16)
    draw.text((204, 110), "EBOOK VOICE PLAYER", font=font(SANS_BOLD, 24), fill=(205, 210, 220))

    # Headline
    draw.text((120, 330), "Turn any book", font=font(SERIF_BOLD, 108), fill=(250, 246, 236))
    draw.text((120, 450), "into an audiobook.", font=font(SERIF_BOLD, 108), fill=(250, 246, 236))
    draw.text(
        (124, 600),
        "Open a book. Choose a voice. Press play.",
        font=font(SANS, 34),
        fill=(186, 192, 203),
    )

    # Play button
    cx, cy, radius = 1520, 540, 120
    draw.ellipse([cx - radius - 18, cy - radius - 18, cx + radius + 18, cy + radius + 18],
                 outline=(255, 255, 255, 36), width=2)
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=AMBER)
    draw.polygon([(cx - 32, cy - 52), (cx - 32, cy + 52), (cx + 62, cy)], fill=(35, 23, 0))

    # Footer facts
    draw.text((120, 880), "300+ neural voices   ·   70+ languages   ·   TXT DOCX PDF EPUB HTML",
              font=font(SANS, 27), fill=(160, 167, 180))
    draw.text((120, 934), "Product trailer  ·  1 min 49 s  ·  Windows 10 & 11",
              font=font(SANS, 24), fill=(120, 128, 142))

    base.convert("RGB").save(OUT / "trailer-poster.png", optimize=True)
    return base


def main():
    make_favicon_32()
    make_icon(180, OUT / "apple-touch-icon.png")
    make_icon(192, OUT / "icon-192.png")
    make_icon(512, OUT / "icon-512.png")
    make_og_image()
    make_trailer_poster()

    for path in sorted(OUT.glob("*")):
        print(f"{path.name:24s} {path.stat().st_size / 1024:8.1f} KiB")


if __name__ == "__main__":
    main()
