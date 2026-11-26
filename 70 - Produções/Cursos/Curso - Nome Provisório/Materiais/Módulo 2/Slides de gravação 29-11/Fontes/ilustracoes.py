"""Ilustrações originais, minimalistas, na paleta do TSH (1920 x 1080).
Gera SVG e converte para PNG com sharp (node)."""
import os, subprocess
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)
NOT, PET, EST, OURO, BEGE, LINHA, CARD2 = "#082A45", "#173F52", "#245E78", "#C99A64", "#F4EFEA", "#E2D8CC", "#ECE5DC"

def dark_bg(extra=""):
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{EST}"/><stop offset="0.5" stop-color="{PET}"/><stop offset="1" stop-color="{NOT}"/></linearGradient>
<radialGradient id="halo"><stop offset="0" stop-color="{OURO}" stop-opacity="0.9"/><stop offset="0.35" stop-color="{OURO}" stop-opacity="0.35"/><stop offset="1" stop-color="{OURO}" stop-opacity="0"/></radialGradient>
{extra}</defs><rect width="1920" height="1080" fill="url(#bg)"/>'''

def light_bg(extra=""):
    return f'''<defs>
<linearGradient id="lbg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#FBF8F4"/><stop offset="1" stop-color="{CARD2}"/></linearGradient>
{extra}</defs><rect width="1920" height="1080" fill="url(#lbg)"/>'''

def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">{body}</svg>'

IMG = {}

# 1. Os homens e o elefante: um elefante velado; três pontos de contato
el = "#3B6A80"
IMG["elefante"] = svg(dark_bg('''<radialGradient id="veu" cx="0.55" cy="0.48" r="0.6">
<stop offset="0.25" stop-color="#082A45" stop-opacity="0"/><stop offset="1" stop-color="#082A45" stop-opacity="0.85"/></radialGradient>''') + f'''
<g fill="{el}" opacity="0.9">
<ellipse cx="1110" cy="500" rx="340" ry="215"/>
<circle cx="780" cy="420" r="160"/>
<rect x="860" y="560" width="95" height="260" rx="40"/>
<rect x="980" y="580" width="95" height="245" rx="40"/>
<rect x="1220" y="580" width="95" height="245" rx="40"/>
<rect x="1330" y="560" width="95" height="260" rx="40"/>
</g>
<path d="M690 470 C 610 540, 600 660, 640 780" stroke="{el}" stroke-width="78" fill="none" stroke-linecap="round" opacity="0.9"/>
<ellipse cx="860" cy="420" rx="120" ry="165" fill="#4A7A90" opacity="0.95"/>
<path d="M1440 470 C 1470 520, 1470 600, 1455 660" stroke="{el}" stroke-width="12" fill="none" stroke-linecap="round"/>
<path d="M705 520 C 690 560, 700 590, 730 600" stroke="{BEGE}" stroke-width="16" fill="none" stroke-linecap="round" opacity="0.85"/>
<circle cx="745" cy="385" r="9" fill="{NOT}"/>
<rect width="1920" height="1080" fill="url(#veu)"/>
<circle cx="640" cy="790" r="70" fill="url(#halo)"/><circle cx="640" cy="790" r="13" fill="{OURO}"/>
<circle cx="910" cy="800" r="70" fill="url(#halo)"/><circle cx="910" cy="800" r="13" fill="{OURO}"/>
<circle cx="890" cy="330" r="70" fill="url(#halo)"/><circle cx="890" cy="330" r="13" fill="{OURO}"/>
''')

# 2. Nasrudin e a chave: o poste com luz; a casa no escuro, a chave junto à porta
IMG["nasrudin"] = svg(dark_bg('''<linearGradient id="cone" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#E8C48F" stop-opacity="0.55"/><stop offset="1" stop-color="#C99A64" stop-opacity="0.12"/></linearGradient>''') + f'''
<g fill="{BEGE}" opacity="0.7"><circle cx="300" cy="160" r="3"/><circle cx="520" cy="110" r="2"/><circle cx="760" cy="200" r="2.5"/>
<circle cx="1000" cy="90" r="2"/><circle cx="1620" cy="150" r="3"/><circle cx="1780" cy="260" r="2"/></g>
<line x1="0" y1="830" x2="1920" y2="830" stroke="#2C5468" stroke-width="3"/>
<polygon points="1335,330 1110,830 1560,830" fill="url(#cone)"/>
<ellipse cx="1335" cy="830" rx="240" ry="26" fill="#E8C48F" opacity="0.35"/>
<rect x="1262" y="300" width="12" height="530" fill="#0E3550"/>
<path d="M1268 300 Q 1268 270 1300 270 L 1335 270" stroke="#0E3550" stroke-width="10" fill="none"/>
<path d="M1310 275 L 1360 275 L 1350 330 L 1320 330 Z" fill="#0E3550"/>
<circle cx="1335" cy="322" r="12" fill="#F6DDB0"/>
<g stroke="{BEGE}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round">
<circle cx="1385" cy="665" r="24" fill="{BEGE}" stroke="none"/>
<path d="M1380 690 C 1365 730, 1370 760, 1395 780"/>
<path d="M1395 780 L 1380 828 M1395 780 L 1420 828"/>
<path d="M1378 715 C 1350 750, 1340 780, 1335 805"/>
</g>
<g fill="#0B3049" stroke="#2C5468" stroke-width="4">
<polygon points="260,560 420,450 580,560"/>
<rect x="290" y="560" width="260" height="270"/></g>
<rect x="385" y="680" width="70" height="150" fill="#05192A"/>
<rect x="320" y="600" width="50" height="45" fill="#05192A"/>
<g transform="translate(470 812)"><circle r="22" fill="url(#halo)"/>
<circle cx="-8" cy="0" r="6" fill="none" stroke="{OURO}" stroke-width="3"/>
<line x1="-2" y1="0" x2="14" y2="0" stroke="{OURO}" stroke-width="3"/>
<line x1="10" y1="0" x2="10" y2="5" stroke="{OURO}" stroke-width="3"/></g>
''')

# 3. A corda e a serpente: o mesmo traço, ao entardecer e à luz
S = "M140 720 C 260 560, 400 860, 540 720 S 760 560, 840 650"
IMG["corda"] = svg(f'''<defs>
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{EST}"/><stop offset="1" stop-color="{NOT}"/></linearGradient>
<linearGradient id="day" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBF8F4"/><stop offset="1" stop-color="{CARD2}"/></linearGradient></defs>
<rect width="960" height="1080" fill="url(#dusk)"/><rect x="960" width="960" height="1080" fill="url(#day)"/>
<line x1="960" y1="80" x2="960" y2="1000" stroke="{OURO}" stroke-width="2"/>
<path d="{S}" stroke="#3E6E84" stroke-width="30" fill="none" stroke-linecap="round"/>
<path d="M140 720 L 110 745" stroke="#3E6E84" stroke-width="14" stroke-linecap="round"/>
<ellipse cx="868" cy="640" rx="46" ry="26" fill="#3E6E84" transform="rotate(-18 868 640)"/>
<circle cx="880" cy="628" r="5" fill="{OURO}"/>
<path d="M910 630 l 26 -8 m -26 8 l 24 10" stroke="#B5524A" stroke-width="3" fill="none"/>
<g transform="translate(960 0)">
<path d="{S}" stroke="#B8946A" stroke-width="30" fill="none" stroke-linecap="round"/>
<path d="{S}" stroke="#8C6B45" stroke-width="30" fill="none" stroke-dasharray="5 15"/>
<path d="M840 650 l 30 -12 M840 650 l 34 6 M840 650 l 26 22 M140 720 l -30 -8 M140 720 l -26 20 M140 720 l -10 30" stroke="#8C6B45" stroke-width="4"/>
</g>
''')

# 4. O homem que fugia da sombra: pegadas que se apressam; a sombra da árvore
fp = ""
x = 120.0; step = 70.0; i = 0
while x < 1180:
    y = 840 + (14 if i % 2 else -14)
    fp += f'<ellipse cx="{x:.0f}" cy="{y}" rx="16" ry="9" fill="#9AA9B2" opacity="0.8"/>'
    x += step; step *= 1.09; i += 1
IMG["sombra"] = svg(light_bg() + f'''
<line x1="0" y1="860" x2="1920" y2="860" stroke="{LINHA}" stroke-width="3"/>
<ellipse cx="1490" cy="862" rx="330" ry="40" fill="#D8CCBD"/>
{fp}
<rect x="1470" y="560" width="44" height="300" rx="10" fill="#5A4A3A"/>
<g fill="{EST}"><circle cx="1490" cy="480" r="150"/><circle cx="1375" cy="550" r="105"/><circle cx="1605" cy="550" r="105"/></g>
<g fill="{PET}"><circle cx="1410" cy="800" r="22"/><path d="M1390 822 Q 1410 812 1430 822 L 1445 858 L 1375 858 Z"/></g>
''')

# 5. Talvez: o mesmo caminho sobe e desce
pts = [(260, 640, True), (680, 760, False), (1100, 600, True), (1520, 780, False)]
nodes = ""
for (x, y, up) in pts:
    if up: nodes += f'<circle cx="{x}" cy="{y}" r="60" fill="url(#halo)"/><circle cx="{x}" cy="{y}" r="22" fill="{OURO}"/>'
    else: nodes += f'<circle cx="{x}" cy="{y}" r="22" fill="none" stroke="{OURO}" stroke-width="5"/>'
IMG["talvez"] = svg(dark_bg() + f'''
<path d="M0 860 L 220 760 L 420 830 L 700 720 L 980 820 L 1300 700 L 1600 800 L 1920 740 L 1920 1080 L 0 1080 Z" fill="#0B3049" opacity="0.7"/>
<path d="M60 700 C 160 560, 360 560, 470 700 S 620 840, 680 760 S 980 520, 1100 600 S 1400 880, 1520 780 S 1780 640, 1880 690"
 stroke="{OURO}" stroke-width="4" fill="none" stroke-dasharray="2 14" stroke-linecap="round"/>
{nodes}
''')

# 6. Sulcos: a água corre por onde já correu; um sulco novo começa
gro = ""
for k, off in enumerate([0, 70, 140, 210, 280]):
    d = f"M-40 {380+off} C 500 {300+off}, 900 {560+off}, 1960 {520+off*0.6:.0f}"
    gro += f'<path d="{d}" stroke="#D6C6B2" stroke-width="34" fill="none"/>'
    gro += f'<path d="{d}" stroke="#C4B19A" stroke-width="12" fill="none" transform="translate(0 6)"/>'
IMG["sulcos"] = svg(light_bg() + f'''{gro}
<path d="M-40 520 C 500 440, 900 700, 1960 604" stroke="{OURO}" stroke-width="7" fill="none" transform="translate(0 6)"/>
<path d="M980 640 C 1120 570, 1280 470, 1480 400" stroke="{EST}" stroke-width="5" fill="none" stroke-dasharray="14 12" stroke-linecap="round"/>
<circle cx="1480" cy="400" r="10" fill="{EST}"/>
''')

# 7. Três membranas: frágil, rígida, permeável
def dots(cx, cy, inside, outside, col):
    s = ""
    for (dx, dy) in inside: s += f'<circle cx="{cx+dx}" cy="{cy+dy}" r="9" fill="{col}"/>'
    for (dx, dy) in outside: s += f'<circle cx="{cx+dx}" cy="{cy+dy}" r="9" fill="{col}" opacity="0.55"/>'
    return s
mb = ""
mb += f'<circle cx="420" cy="500" r="190" fill="none" stroke="#9FB3BF" stroke-width="4" stroke-dasharray="10 26"/>'
mb += dots(420, 500, [(-60, -40), (50, 20), (-20, 90), (90, -90), (-120, 60), (10, -120), (130, 80)], [], "#7C93A0")
mb += f'<circle cx="960" cy="500" r="190" fill="none" stroke="{NOT}" stroke-width="44"/>'
mb += f'<circle cx="960" cy="500" r="30" fill="{EST}" opacity="0.5"/>'
mb += dots(960, 500, [], [(-270, -60), (260, 90), (40, -280), (-120, 270), (250, -170)], "#7C93A0")
mb += f'<circle cx="1500" cy="500" r="190" fill="none" stroke="{EST}" stroke-width="8" stroke-dasharray="150 40"/>'
mb += f'<circle cx="1500" cy="500" r="168" fill="none" stroke="{EST}" stroke-width="4" stroke-dasharray="130 50"/>'
mb += f'<circle cx="1500" cy="500" r="60" fill="url(#halo)"/><circle cx="1500" cy="500" r="20" fill="{OURO}"/>'
mb += dots(1500, 500, [(-80, 60), (70, -70)], [(-260, -40), (250, 60)], OURO)
mb += f'<path d="M1270 470 L 1330 480" stroke="{OURO}" stroke-width="4" marker-end="url(#ar)"/>'
mb += f'<path d="M1690 540 L 1740 555" stroke="{OURO}" stroke-width="4" marker-end="url(#ar)"/>'
lab = "".join(f'<text x="{x}" y="800" font-family="Inter" font-size="40" fill="{EST}" text-anchor="middle">{t}</text>'
              for x, t in [(420, "frágil"), (960, "rígida"), (1500, "permeável")])
IMG["membranas"] = svg(light_bg(f'''<radialGradient id="halo"><stop offset="0" stop-color="{OURO}" stop-opacity="0.9"/><stop offset="1" stop-color="{OURO}" stop-opacity="0"/></radialGradient>
<marker id="ar" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{OURO}"/></marker>''') + mb + lab)

# 8. Páginas matinais: três folhas à mão, ao nascer do dia
def page(x, y, rot):
    lines = "".join(f'<path d="M{x+50} {y+90+k*42} q 40 -10 80 0 t 80 0 t 80 0 t 80 0 t 60 0" stroke="{EST}" stroke-width="3" fill="none" opacity="0.75"/>'
                    for k in range(12))
    return f'<g transform="rotate({rot} {x+230} {y+330})"><rect x="{x}" y="{y}" width="460" height="640" rx="6" fill="#FFFFFF" stroke="{LINHA}" stroke-width="3"/>{lines}</g>'
IMG["paginas"] = svg(f'''<defs><linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#FBF8F4"/><stop offset="0.7" stop-color="#F3E3CC"/><stop offset="1" stop-color="#EBD3B0"/></linearGradient>
<radialGradient id="sun"><stop offset="0" stop-color="#F2C98A"/><stop offset="0.6" stop-color="#E9B877" stop-opacity="0.6"/><stop offset="1" stop-color="#E9B877" stop-opacity="0"/></radialGradient></defs>
<rect width="1920" height="1080" fill="url(#dawn)"/>
<circle cx="1500" cy="980" r="360" fill="url(#sun)"/><circle cx="1500" cy="980" r="130" fill="#F0C27F"/>
<line x1="1000" y1="980" x2="1920" y2="980" stroke="#D9BE98" stroke-width="3"/>
{page(240, 240, -8)}{page(330, 210, -2)}{page(420, 190, 5)}
<path d="M1010 760 L 1120 600" stroke="{NOT}" stroke-width="14" stroke-linecap="round"/>
<path d="M1010 760 L 1000 790 L 1022 770 Z" fill="{NOT}"/>
''')

for k, v in IMG.items():
    p = os.path.join(OUT, f"{k}.svg"); open(p, "w").write(v)
    subprocess.run(["node", "-e", f"require('sharp')('{p}').png().toFile('{OUT}/{k}.png').then(()=>{{}})"], check=True)
print("ok", sorted(IMG))
