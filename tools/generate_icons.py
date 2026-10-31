"""Generate original, simplified inventory illustrations; requires Pillow.

These are interpretations, not scans of the commercial labels. Fonts are taken
from the local DejaVu font installation. Run from the repository root.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('PolishAlcohol/42/media/textures')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
# id, label, bottle colour, label background, lettering, accent, kind
ITEMS = [
 ('Zywiec','ŻYWIEC','#60401c','#f7ead0','#a62125','#d8ad4f','beer'),
 ('Tyskie','TYSKIE','#583719','#f5f0dc','#a5282b','#c7a552','beer'),
 ('Lech','LECH','#31542d','#f2ecd5','#145033','#dbba65','beer'),
 ('Zubr','ŻUBR','#51411c','#174b2c','#f5e9ca','#c8ae64','beer'),
 ('Kustosz','KUSTOSZ','#ae7a24','#f0eee5','#283e6b','#cba754','beer'),
 ('Romper','ROMPER','#523b22','#221f20','#f5f1df','#ad3029','beer'),
 ('Imperator','IMPERATOR','#563b21','#272321','#eeddae','#b18a40','beer'),
 ('Karpackie','KARPACKIE','#543b22','#184977','#f3f4ec','#bca050','beer'),
 ('Tatra','TATRA','#58401e','#eed88d','#2a2721','#bb9b54','beer'),
 ('Harnas','HARNAŚ','#563b25','#f2e9c9','#b32625','#b7a276','beer'),
 ('Zubrowka','ŻUBRÓWKA','#cad2b4','#ece8c9','#284a29','#bd9b56','vodka'),
 ('Wyborowa','WYBOROWA','#c6d3d6','#f4f2e8','#1b3757','#b22833','vodka'),
 ('Soplica','SOPLICA','#cbd2cf','#efe4c9','#7a2528','#be9b5b','vodka'),
 ('AdamMickiewicz','ADAM|MICKIEWICZ','#c9d0cd','#e8e9e3','#333b3c','#9fa6a1','vodka'),
 ('Chopin','CHOPIN','#c8cfcb','#edeee9','#252627','#353535','vodka'),
 ('Wratislavia','WRATISLAVIA','#c5d1d2','#e8e3d3','#2d4248','#a18459','vodka'),
]
S=3

def font(size,bold=True): return ImageFont.truetype(FONT if bold else REG,size*S)
def box(coords): return tuple(int(x*S) for x in coords)
def text_center(d, text, y, color, max_width=58, size=13, bold=True):
    f=font(size,bold)
    while d.textbbox((0,0),text,font=f)[2] > max_width*S and size>5:
        size-=1; f=font(size,bold)
    d.text((64*S,y*S),text,font=f,fill=color,anchor='mt',stroke_width=0)

def generate(row):
    ident, name, glass, paper, ink, accent, kind=row
    im=Image.new('RGBA',(128*S,128*S),(0,0,0,0)); d=ImageDraw.Draw(im)
    # Bottle silhouette and highlights. Both use 500 mL as in the item scripts.
    d.rounded_rectangle(box((54,8,74,39)),radius=4*S,fill=glass,outline='#292822',width=2*S)
    d.rounded_rectangle(box((53,7,75,14)),radius=2*S,fill=accent,outline='#292822',width=S)
    d.polygon([tuple(S*x for x in p) for p in [(54,33),(47,41),(42,48),(42,110),(44,117),(84,117),(86,110),(86,48),(81,41),(74,33)]],fill=glass,outline='#292822',width=2*S)
    d.line([box((47,49,47,108))[:2], box((47,49,47,108))[2:]], fill='#ffffff55',width=2*S)
    d.rounded_rectangle(box((42,58,86,95)),radius=2*S,fill=paper,outline=accent,width=2*S)
    d.line([box((45,63,83,63))[:2],box((45,63,83,63))[2:]],fill=accent,width=S)
    d.line([box((45,90,83,90))[:2],box((45,90,83,90))[2:]],fill=accent,width=S)
    lines=name.split('|')
    if len(lines)==1: text_center(d,lines[0],70,ink,max_width=39,size=10)
    else:
        text_center(d,lines[0],65,ink,max_width=39,size=8)
        text_center(d,lines[1],74,ink,max_width=39,size=7)
    text_center(d,'PIWO' if kind=='beer' else 'WÓDKA',83,ink,max_width=36,size=5,bold=False)
    # No ABV printed: vanilla Beer/Vodka fluid determines in-game strength.
    im.resize((128,128),Image.Resampling.LANCZOS).save(OUT/f'Item_Polish{ident}.png',optimize=True)

if __name__ == '__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    for row in ITEMS: generate(row)
