#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère l'image d'aperçu social (Open Graph) og.png 1200x630."""
import sys
from PIL import Image, ImageDraw, ImageFont
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

W, H = 1200, 630
BG = (15, 23, 32)
CARD = (23, 34, 48)
ACCENT = (45, 212, 191)
INK = (238, 243, 248)
MUTED = (159, 176, 195)
LINE = (38, 56, 75)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

bold = "C:/Windows/Fonts/arialbd.ttf"
reg = "C:/Windows/Fonts/arial.ttf"

f_title = font(bold, 92)
f_sub = font(reg, 38)
f_badge = font(bold, 28)
f_url = font(bold, 30)

# barre d'accent à gauche
d.rectangle([0, 0, 16, H], fill=ACCENT)

# badge "GRATUIT · SANS INSCRIPTION"
badge = "GRATUIT · SANS INSCRIPTION"
bw = d.textlength(badge, font=f_badge)
d.rounded_rectangle([70, 90, 70 + bw + 48, 150], radius=30, fill=(15, 42, 40), outline=ACCENT, width=2)
d.text((70 + 24, 102), badge, font=f_badge, fill=ACCENT)

# titre
d.text((70, 200), "Temps de Conduite", font=f_title, fill=INK)

# sous-titre (2 lignes)
d.text((70, 320), "Calculateur temps de conduite · pauses · repos", font=f_sub, fill=MUTED)
d.text((70, 372), "Test tachygraphe 2026 · règles du cabotage", font=f_sub, fill=MUTED)

# pictos chiffres clés (cartes)
cards = [("9h", "conduite/jour"), ("4h30", "puis pause 45min"), ("11h", "repos")]
x = 70
y = 470
for big, small in cards:
    cw = 240
    d.rounded_rectangle([x, y, x + cw, y + 110], radius=16, fill=CARD, outline=LINE, width=1)
    d.text((x + 24, y + 18), big, font=font(bold, 46), fill=ACCENT)
    d.text((x + 24, y + 74), small, font=font(reg, 24), fill=MUTED)
    x += cw + 24

# url en bas à droite
url = "temps-de-conduite"
uw = d.textlength(url, font=f_url)
d.text((W - uw - 70, 110), url, font=f_url, fill=ACCENT)

img.save("og.png")
print("og.png généré (1200x630)")
