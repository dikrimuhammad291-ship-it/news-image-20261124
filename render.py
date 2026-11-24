#!/usr/bin/env python3
"""Render the front page for news-image-20261124.

Draws a 1024x1024 newspaper front page summing up the world news of
Tuesday 24 November 2026 with PIL. Run locally to produce entry.png;
the graded entrypoint (main.py) only copies the committed image.

Deterministic: fixed coordinates, fixed font sizes, no randomness.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (248, 245, 238)
INK = (22, 22, 22)
RED = (178, 34, 34)
GREY = (96, 96, 96)
RULE = (180, 175, 165)
CARD_BG = (255, 255, 255)
CARD_LINE = (205, 200, 190)

FONT_DIR = "/usr/share/fonts/truetype"
SERIF_B = os.path.join(FONT_DIR, "liberation/LiberationSerif-Bold.ttf")
SERIF_R = os.path.join(FONT_DIR, "liberation/LiberationSerif-Regular.ttf")
SANS_B = os.path.join(FONT_DIR, "liberation/LiberationSans-Bold.ttf")
SANS_R = os.path.join(FONT_DIR, "liberation/LiberationSans-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_lead_art(draw, x0, y0, x1, y1):
    """Flat night illustration: the PIF Tower in Riyadh under attack."""
    draw.rectangle([x0, y0, x1, y1], fill=(23, 33, 58))
    # Stars (fixed positions).
    for sx, sy, r in [(14, 18, 2), (70, 42, 1), (150, 14, 2), (210, 60, 1),
                      (260, 26, 2), (300, 80, 1), (40, 90, 1), (180, 100, 1)]:
        draw.ellipse([x0 + sx - r, y0 + sy - r, x0 + sx + r, y0 + sy + r],
                     fill=(240, 240, 220))
    # Distant skyline.
    base = y1 - 8
    for bx, bw, bh in [(0, 46, 60), (50, 38, 88), (92, 52, 52), (150, 40, 76),
                       (250, 48, 66), (282, 38, 96)]:
        draw.rectangle([x0 + bx, base - bh, x0 + bx + bw, base],
                       fill=(38, 50, 78))
    # The tower: tapered shaft with a pointed spire.
    tx = x0 + 190
    draw.polygon([(tx - 34, base), (tx - 22, y0 + 78), (tx + 22, y0 + 78),
                  (tx + 34, base)], fill=(52, 66, 96))
    draw.polygon([(tx - 22, y0 + 78), (tx, y0 + 30), (tx + 22, y0 + 78)],
                 fill=(52, 66, 96))
    draw.line([tx, y0 + 30, tx, y0 + 12], fill=(52, 66, 96), width=4)
    # Lit windows.
    for wy in range(y0 + 110, base - 20, 26):
        for wx in (-12, 2):
            draw.rectangle([tx + wx, wy, tx + wx + 7, wy + 10],
                           fill=(255, 214, 120))
    # Explosion burst near the spire.
    cx, cy = tx - 16, y0 + 60
    for rad, col in [(38, (255, 122, 26)), (26, (255, 176, 32)),
                     (15, (255, 232, 130))]:
        pts = []
        for i in range(16):
            ang = 3.14159 * i / 8
            rr = rad if i % 2 == 0 else rad * 0.55
            pts.append((cx + rr * math.cos(ang),
                        cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=col)
    # Smoke drifting right.
    for ex, ey, er in [(tx + 44, y0 + 52, 22), (tx + 78, y0 + 40, 17),
                       (tx + 104, y0 + 30, 12)]:
        draw.ellipse([ex - er, ey - er // 2, ex + er, ey + er // 2],
                     fill=(120, 120, 128))
    # Caption strip.
    draw.rectangle([x0, y1 - 30, x1, y1], fill=(12, 18, 32))
    cap = font(SANS_B, 17)
    draw.text((x0 + 12, y1 - 26), "PIF TOWER, RIYADH", font=cap,
              fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # side margin

    # ---- Masthead ----
    title = font(SERIF_B, 66)
    t = "THE WORLD TODAY"
    tw = d.textlength(t, font=title)
    d.text(((W - tw) / 2, 24), t, font=title, fill=INK)
    date_f = font(SANS_B, 30)
    dt = "TUESDAY, 24 NOVEMBER 2026"
    dw = d.textlength(dt, font=date_f)
    d.text(((W - dw) / 2, 106), dt, font=date_f, fill=RED)
    sub_f = font(SANS_R, 19)
    st = "The day's world news in one page"
    sw = d.textlength(st, font=sub_f)
    d.text(((W - sw) / 2, 144), st, font=sub_f, fill=GREY)
    d.line([mx, 178, W - mx, 178], fill=INK, width=4)
    d.line([mx, 185, W - mx, 185], fill=INK, width=1)

    # ---- Lead story: text left, art right ----
    tag_f = font(SANS_B, 20)
    d.text((mx, 202), "LEAD STORY  •  MIDDLE EAST", font=tag_f, fill=RED)
    head_f = font(SERIF_B, 46)
    head = wrap(d, "Houthi strike hits Riyadh's tallest tower, 11 hurt",
                head_f, 600)
    y = draw_lines(d, head, mx, 232, head_f, INK, 54)
    body_f = font(SANS_R, 23)
    body = wrap(d, "Yemen's Houthi fighters struck the PIF Tower in the "
                   "Saudi capital for the second time in five days. Saudi "
                   "Civil Defence said 11 people were wounded.",
                body_f, 600)
    y = draw_lines(d, body, mx, y + 14, body_f, INK, 31)
    d.text((mx, y + 10), "Sources: Reuters, Wall Street Journal",
           font=font(SANS_R, 17), fill=GREY)
    draw_lead_art(d, 668, 202, W - mx, 470)

    d.line([mx, 496, W - mx, 496], fill=RULE, width=2)

    # ---- Support stories: 2 columns x 3 rows ----
    cards = [
        ("UKRAINE", (30, 80, 140),
         "Russian strike hits Zaporizhzhia flats, 2 killed",
         "Dozens wounded as a missile hit an apartment block, the regional governor said."),
        ("GAZA", (140, 40, 40),
         "Israeli strikes kill Hamas security chief",
         "Naeem Abu Nahel and six others were killed, officials said."),
        ("SPORT", (30, 110, 70),
         "Senegal reinstated as Africa Cup winners",
         "CAS upheld the appeal, overturning the title award to Morocco."),
        ("CHINA", (150, 90, 20),
         "Beijing probes Shanghai party boss Chen Jining",
         "Fourth Politburo member to fall since 2025, over 'serious violations'."),
        ("DEFENCE", (70, 70, 120),
         "Germany first to access Ukraine's Delta system",
         "Berlin gains access to Kyiv's battlefield awareness platform."),
        ("DIPLOMACY", (100, 60, 100),
         "Abu Dhabi peace talks end in stalemate",
         "Russia rules out territorial concessions; US envoys head to Moscow."),
    ]
    cw, ch, col_gap, row_gap = 462, 148, 28, 6
    tag2 = font(SANS_B, 17)
    h2 = font(SERIF_B, 26)
    b2 = font(SANS_R, 19)
    for i, (tag, col, headline, blurb) in enumerate(cards):
        cx = mx + (i % 2) * (cw + col_gap)
        cy = 516 + (i // 2) * (ch + row_gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD_BG,
                    outline=CARD_LINE, width=1)
        d.rectangle([cx, cy, cx + cw, cy + 6], fill=col)
        d.text((cx + 14, cy + 12), tag, font=tag2, fill=col)
        hl = wrap(d, headline, h2, cw - 28)
        yy = draw_lines(d, hl, cx + 14, cy + 36, h2, INK, 30)
        bl = wrap(d, blurb, b2, cw - 28)
        draw_lines(d, bl, cx + 14, yy + 2, b2, (60, 60, 60), 23)

    # ---- Footer ----
    d.line([mx, 978, W - mx, 978], fill=RULE, width=1)
    foot = font(SANS_R, 16)
    ft = ("All events of Tuesday 24 November 2026  •  Sources: Reuters, AP, "
          "Kyiv Independent, Al Arabiya")
    fw = d.textlength(ft, font=foot)
    d.text(((W - fw) / 2, 988), ft, font=foot, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
