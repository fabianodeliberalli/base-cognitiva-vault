"""M1.1 — padronização no sistema visual da Masterclass TSH.
Regras do caderno de produção v0.2: diagramas simples, sem foto de pessoa do caso,
sem antecipar EIXO/pêndulo/espiral/árvore/Cinco Janelas; tela 3 sem sequência causal; tela 6 sem setas anatômicas."""
import sys, re, copy
from tsh_lib import *

SRC, OUT = sys.argv[1], sys.argv[2]
prs = Presentation(SRC); S = prs.slides

def texts(slide):
    return [s for s in slide.shapes if s.has_text_frame]

def parts(slide):
    t = texts(slide)
    return t[0], t[1], t[2:-1], t[-1]   # cabeçalho, título, itens, rodapé

def drop_logo(slide):
    for p in [s for s in slide.shapes if s.shape_type == 13]:
        p._element.getparent().remove(p._element)

def header(h, dark=False):
    place(h, 0.92, 0.42, 7, 0.32); frame(h, "t"); style(h, SANS, 12, OURO if dark else EST, bold=True, spc=220)
    for r in h.text_frame.paragraphs[0].runs: r.text = r.text.upper()

def footer(f, slide, dark=False, mark=True):
    place(f, 0.92, 6.88, 3, 0.3); frame(f, "t"); style(f, SANS, 11, "8FA0AC" if dark else MUTED, spc=100)
    if mark: corner(slide, dark)

def title_top(t, size=40):
    place(t, 0.92, 0.8, 11.5, 1.25); frame(t, "b"); style(t, SERIF, size, NOT, line=95)

def split_bullet(shape):
    """'Verbo • pergunta' vira dois parágrafos (verbo / pergunta)"""
    p = shape.text_frame.paragraphs[0]; r = p.runs[0]
    a, _, b = r.text.partition("•")
    r.text = a.strip()
    for extra in p.runs[1:]: p._p.remove(extra._r)
    newp = copy.deepcopy(p._p); p._p.addnext(newp)
    shape.text_frame.paragraphs[1].runs[0].text = b.strip()

def light(slide):
    drop_logo(slide); bg_solid(slide, BEGE)
    h, t, items, f = parts(slide); header(h); footer(f, slide)
    return t, items

def cards(slide, items, y=2.45, h=3.4, n=None):
    n = n or len(items); gap = 0.28; cw = (11.5 - gap * (n - 1)) / n
    xs = [0.92 + k * (cw + gap) for k in range(n)]
    for x in xs: rect(slide, x, y, cw, h, fill=CARD, line=LINHA, rounded=0.05)
    return xs, cw

SUB_CURSO = "DA COMPREENSÃO ACUMULADA À PRESENÇA QUE SUSTENTA"

def triad(slide, cur):
    words = ["SABER", "ACESSAR", "SUSTENTAR"]
    for k, w in enumerate(words):
        x = 8.6 + k * 1.35
        on = k == cur
        dot(slide, x, 0.58, 0.14 if on else 0.1, fill=OURO if on else None, line=None if on else MUTED)
        label(slide, x + 0.13, 0.43, 1.2, 0.32, w, size=11, color=EST if on else MUTED, bold=on, spc=150)

def split(slide, t, items, size=24, font=SANS):
    place(t, 0.92, 0.9, 4.75, 5.6); frame(t, "ctr"); style(t, SERIF, 40, NOT, line=95)
    top, bottom = 1.5, 6.1; row = (bottom - top) / len(items)
    for k, it in enumerate(items):
        y = top + k * row
        place(it, 6.5, y, 5.9, row); frame(it, "ctr"); style(it, font, size, NOT if font == SERIF else PET, line=110)
        dot(slide, 6.05, y + row / 2, 0.15 if k == 0 else 0.11)
    vline(slide, 6.05, top + row / 2, top + row * (len(items) - 0.5))
    tree = slide.shapes._spTree; ln = tree[2 + len(items)]; tree.remove(ln); tree.insert(2, ln)

# 1 capa
s = S[0]; drop_logo(s); bg_grad(s)
h, t, items, f = parts(s)
place(h, 0.92, 0.8, 7, 0.4); frame(h, "t"); style(h, SANS, 14, OURO, bold=True, spc=250)
for r in h.text_frame.paragraphs[0].runs: r.text = r.text.upper()
place(t, 0.92, 1.35, 7.5, 3.0); frame(t, "b"); style(t, SERIF, 52, "FFFFFF", line=92)
code, q = items
place(code, 0.95, 4.75, 7, 0.4); frame(code, "t"); style(code, SANS, 16, OURO, bold=True, spc=120)
place(q, 0.95, 5.3, 7.2, 0.6); frame(q, "t"); style(q, SERIF, 26, BEGE, italic=True)
pic(s, A + "mark_gold.png", 8.95, 0.9, h=4.15)
label(s, 8.62, 5.25, 4.65, 0.35, SUB_CURSO, size=8.5, color="E9E2D8", bold=False, align="ctr", spc=120)
f._element.getparent().remove(f._element)

# 2 cena em três momentos
s = S[1]; t, items = light(s); title_top(t)
xs, cw = cards(s, items, y=2.5, h=2.9)
for k, (x, it) in enumerate(zip(xs, items)):
    label(s, x + 0.3, 2.75, 1, 0.35, f"0{k + 1}", size=13, color=OURO, spc=150)
    place(it, x + 0.3, 3.2, cw - 0.6, 2.0); frame(it, "t"); style(it, SERIF, 30, NOT, line=100)
    if k < 2: rect(s, x + cw + 0.08, 3.95, 0.12, 0.26, fill=OURO, kind=MSO_SHAPE.CHEVRON)
label(s, 0.92, 5.7, 6, 0.35, "SITUAÇÃO FICTÍCIA", size=12, color=MUTED, spc=200)

# 3, 4, 5 — a tríade, com marcador de posição
for si, cur, font, size in ((2, 0, SERIF, 30), (3, 1, SERIF, 30), (4, 2, SERIF, 30)):
    s = S[si]; t, items = light(s); split(s, t, items, size=size, font=font); triad(s, cur)

# 6 usar e revisar: quatro perguntas
s = S[5]; t, items = light(s); title_top(t)
xs, cw = cards(s, items, y=2.45, h=3.2)
for k, (x, it) in enumerate(zip(xs, items)):
    label(s, x + 0.28, 2.68, 1, 0.35, f"0{k + 1}", size=13, color=OURO, spc=150)
    place(it, x + 0.28, 3.1, cw - 0.5, 2.4); frame(it, "t"); style(it, SERIF, 28, NOT, line=100)

# 7 três situações que podem coexistir (sem setas)
s = S[6]; t, items = light(s); title_top(t, 38)
xs, cw = cards(s, items, y=2.6, h=3.2)
c = s.shapes.add_connector(1, Inches(xs[0] + 0.45), Inches(2.6), Inches(xs[-1] + 0.45), Inches(2.6))
c.line.color.rgb = rgb(OURO); c.line.width = Pt(1); add_back(s, c)
for x, it in zip(xs, items):
    dot(s, x + 0.45, 2.6, 0.16)
    place(it, x + 0.3, 3.0, cw - 0.5, 2.6); frame(it, "t"); style(it, SERIF, 28, NOT, line=100)

# 8 condições de cultivo em linhas
s = S[7]; t, items = light(s); title_top(t)
rect(s, 0.92, 2.3, 11.5, 4.25, fill=CARD, line=LINHA, rounded=0.03)
for k, it in enumerate(items):
    y = 2.45 + k * 1.0
    if k: rect(s, 1.3, y - 0.02, 10.74, 0.015, fill=LINHA)
    dot(s, 1.4, y + 0.48, 0.12)
    place(it, 1.75, y + 0.15, 10.3, 0.7); frame(it, "ctr"); style(it, SERIF, 30, NOT)

# 9 investigação breve: contexto à esquerda, perguntas em destaque
s = S[8]; t, items = light(s)
place(t, 0.92, 0.9, 5.0, 1.4); frame(t, "b"); style(t, SERIF, 40, NOT, line=95)
ctx, qs = items[0], items[1:]
place(ctx, 0.92, 2.55, 4.9, 1.4); frame(ctx, "t"); style(ctx, SERIF, 24, EST, italic=True, line=110)
rect(s, 6.35, 0.9, 6.07, 5.6, fill=CARD, line=LINHA, rounded=0.03)
for k, it in enumerate(qs):
    y = 1.35 + k * 1.65
    label(s, 6.8, y + 0.02, 0.5, 0.6, str(k + 1), font=SERIF, size=32, color=OURO, bold=False)
    place(it, 7.3, y, 4.8, 1.4); frame(it, "t"); style(it, SERIF, 30, NOT, line=100)

# 10 registro: quatro campos (folha)
s = S[9]; t, items = light(s); title_top(t)
rect(s, 0.92, 2.25, 11.5, 4.3, fill="FFFFFF", line=LINHA, rounded=0.02)
cells = [(1.35, 2.55), (6.95, 2.55), (1.35, 4.45), (6.95, 4.45)]
for k, ((x, y), it) in enumerate(zip(cells, items)):
    label(s, x, y + 0.04, 0.5, 0.5, str(k + 1), font=SERIF, size=28, color=OURO, bold=False)
    place(it, x + 0.45, y, 4.6, 0.6); frame(it, "t"); style(it, SERIF, 27, NOT)
    for j in range(2): rect(s, x + 0.45, y + 1.08 + j * 0.42, 4.6, 0.015, fill=LINHA)

# 11 encerramento
s = S[10]; drop_logo(s); bg_grad(s)
h, t, items, f = parts(s); header(h, dark=True); footer(f, s, dark=True, mark=False)
place(t, 0.92, 0.85, 7.8, 2.0); frame(t, "b"); style(t, SERIF, 44, "FFFFFF", line=95)
for k, it in enumerate(items):
    y = 3.3 + k * 0.85
    dot(s, 1.05, y + 0.3, 0.13)
    place(it, 1.35, y, 7.2, 0.7); frame(it, "t"); style(it, SERIF, 30, BEGE, italic=True)
pic(s, A + "sym_gold.png", 8.55, 0.85, h=5.8, alpha=0.22)

for m_ in prs.slide_masters:
    th = m_.part.part_related_by("http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme")
    x = th.blob.decode("utf8")
    x = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*"', r'\1EB Garamond"', x)
    x = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*"', r'\1Inter"', x)
    th._blob = x.encode("utf8")
prs.save(OUT); print("ok")
