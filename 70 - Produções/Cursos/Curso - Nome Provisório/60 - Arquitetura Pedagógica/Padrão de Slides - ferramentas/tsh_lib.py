"""Redesenho do deck TSH segundo o Manual de Identidade Visual v1.0.
Mantém todas as formas animadas (mesmos ids, mesmos parágrafos); só move, redimensiona e reestiliza.
Elementos novos são estáticos e entram atrás do conteúdo."""
import sys, re, io, copy
import numpy as np
from PIL import Image
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

A = "assets/"

# ---------- paleta oficial ----------
NOT = "082A45"; PET = "173F52"; EST = "245E78"; OURO = "C99A64"; BEGE = "F4EFEA"
CARD = "FBF8F4"; LINHA = "E2D8CC"; MUTED = "5A6B74"; CARD2 = "ECE5DC"
SERIF = "EB Garamond"; SANS = "Inter"


def rgb(h): return RGBColor.from_string(h)
def sh(slide, sid):
    for s in slide.shapes:
        if s.shape_id == sid: return s
    raise KeyError(sid)

def to_back(slide, shape, pos=None):
    tree = slide.shapes._spTree
    el = shape._element
    tree.remove(el)
    # depois de nvGrpSpPr e grpSpPr
    idx = 2 if pos is None else pos
    tree.insert(idx, el)

_back_counter = {}
def add_back(slide, shape):
    """empilha elementos estáticos atrás do conteúdo, na ordem de criação"""
    n = _back_counter.get(id(slide), 0)
    to_back(slide, shape, 2 + n)
    _back_counter[id(slide)] = n + 1

# ---------- fundos ----------
def bg_solid(slide, color):
    f = slide.background.fill; f.solid(); f.fore_color.rgb = rgb(color)

def bg_grad(slide):
    cSld = slide._element.find(qn("p:cSld"))
    old = cSld.find(qn("p:bg"))
    if old is not None: cSld.remove(old)
    xml = (f'<p:bg xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
           f'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:bgPr>'
           f'<a:gradFill rotWithShape="1"><a:gsLst>'
           f'<a:gs pos="0"><a:srgbClr val="{EST}"/></a:gs>'
           f'<a:gs pos="45000"><a:srgbClr val="{PET}"/></a:gs>'
           f'<a:gs pos="100000"><a:srgbClr val="{NOT}"/></a:gs>'
           f'</a:gsLst><a:lin ang="5400000" scaled="0"/></a:gradFill><a:effectLst/></p:bgPr></p:bg>')
    cSld.insert(0, etree.fromstring(xml))

# ---------- texto ----------
def place(s, x, y, w, h):
    s.left, s.top, s.width, s.height = Inches(x), Inches(y), Inches(w), Inches(h)

def frame(s, anchor="t", inset=0.0):
    tf = s.text_frame
    bp = tf._txBody.find(qn("a:bodyPr"))
    bp.set("anchor", anchor); bp.set("wrap", "square")
    for k in ("lIns", "rIns", "tIns", "bIns"): bp.set(k, str(int(Inches(inset))))
    for tag in ("a:normAutofit", "a:spAutoFit", "a:noAutofit"):
        for e in bp.findall(qn(tag)): bp.remove(e)
    etree.SubElement(bp, qn("a:noAutofit"))

def set_run(r, font=None, size=None, color=None, bold=None, italic=None, spc=None):
    rPr = r._r.get_or_add_rPr()
    if size: rPr.set("sz", str(int(size * 100)))
    if bold is not None: rPr.set("b", "1" if bold else "0")
    if italic is not None: rPr.set("i", "1" if italic else "0")
    if spc is not None: rPr.set("spc", str(int(spc)))
    if color:
        for e in rPr.findall(qn("a:solidFill")): rPr.remove(e)
        sf = etree.SubElement(rPr, qn("a:solidFill")); c = etree.SubElement(sf, qn("a:srgbClr")); c.set("val", color)
        # solidFill precisa vir antes de latin
        rPr.remove(sf); rPr.insert(0, sf)
    if font:
        for tag in ("a:latin", "a:ea", "a:cs"):
            for e in rPr.findall(qn(tag)): rPr.remove(e)
        for tag in ("a:latin", "a:cs"):
            e = etree.SubElement(rPr, qn(tag)); e.set("typeface", font)

def set_para(p, align=None, line=None, after=None, before=None):
    pPr = p._p.get_or_add_pPr()
    if align: pPr.set("algn", align)
    def sp(tag, val, kind):
        for e in pPr.findall(qn(tag)): pPr.remove(e)
        el = etree.Element(qn(tag)); c = etree.SubElement(el, qn(kind)); c.set("val", str(val))
        # ordem: lnSpc, spcBef, spcAft
        order = ["a:lnSpc", "a:spcBef", "a:spcAft"]
        pos = 0
        for i, t in enumerate(order):
            if t == tag: break
            pos += len(pPr.findall(qn(t)))
        pPr.insert(pos, el)
    if line: sp("a:lnSpc", int(line * 1000), "a:spcPct")
    if before is not None: sp("a:spcBef", int(before * 100), "a:spcPts")
    if after is not None: sp("a:spcAft", int(after * 100), "a:spcPts")
    # tamanho também no endParaRPr para linhas vazias
    return pPr

def style(s, font, size, color, bold=False, italic=None, align="l", line=None, after=None, before=None, spc=None):
    for p in s.text_frame.paragraphs:
        set_para(p, align=align, line=line, after=after, before=before)
        for r in p.runs: set_run(r, font, size, color, bold, italic, spc)
        epr = p._p.find(qn("a:endParaRPr"))
        if epr is None:
            epr = etree.SubElement(p._p, qn("a:endParaRPr"))
        epr.set("sz", str(int(size * 100)))

def bullets(s, char="•", color=OURO, indent=0.32, font=SANS):
    for p in s.text_frame.paragraphs:
        if not p.text.strip(): continue
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", str(int(Inches(indent)))); pPr.set("indent", str(-int(Inches(indent))))
        for t in ("a:buClr", "a:buFont", "a:buChar", "a:buNone", "a:buAutoNum"):
            for e in pPr.findall(qn(t)): pPr.remove(e)
        c = etree.SubElement(pPr, qn("a:buClr")); x = etree.SubElement(c, qn("a:srgbClr")); x.set("val", color)
        f = etree.SubElement(pPr, qn("a:buFont")); f.set("typeface", font)
        b = etree.SubElement(pPr, qn("a:buChar")); b.set("char", char)

def numbered(s, color=OURO, indent=0.62):
    for p in s.text_frame.paragraphs:
        if not p.text.strip(): continue
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", str(int(Inches(indent)))); pPr.set("indent", str(-int(Inches(indent))))
        for t in ("a:buClr", "a:buFont", "a:buChar", "a:buNone", "a:buAutoNum", "a:buSzPct"):
            for e in pPr.findall(qn(t)): pPr.remove(e)
        c = etree.SubElement(pPr, qn("a:buClr")); x = etree.SubElement(c, qn("a:srgbClr")); x.set("val", color)
        f = etree.SubElement(pPr, qn("a:buFont")); f.set("typeface", SERIF)
        b = etree.SubElement(pPr, qn("a:buAutoNum")); b.set("type", "arabicPeriod")

# ---------- formas estáticas ----------
def rect(slide, x, y, w, h, fill=None, line=None, lw=0.75, rounded=0.0, kind=None):
    k = kind or (MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE)
    r = slide.shapes.add_shape(k, Inches(x), Inches(y), Inches(w), Inches(h))
    if rounded and k == MSO_SHAPE.ROUNDED_RECTANGLE: r.adjustments[0] = rounded
    if fill: r.fill.solid(); r.fill.fore_color.rgb = rgb(fill)
    else: r.fill.background()
    if line: r.line.color.rgb = rgb(line); r.line.width = Pt(lw)
    else: r.line.fill.background()
    r.shadow.inherit = False
    if r.has_text_frame: r.text_frame.text = ""
    add_back(slide, r)
    return r

def dot(slide, cx, cy, d, fill=OURO, line=None):
    return rect(slide, cx - d / 2, cy - d / 2, d, d, fill=fill, line=line, kind=MSO_SHAPE.OVAL)

def vline(slide, x, y0, y1, color=OURO, w=1.0):
    c = slide.shapes.add_connector(1, Inches(x), Inches(y0), Inches(x), Inches(y1))
    c.line.color.rgb = rgb(color); c.line.width = Pt(w)
    add_back(slide, c); return c

def label(slide, x, y, w, h, text, font=SANS, size=14, color=EST, bold=True, align="l", spc=0, anchor="t"):
    t = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    t.text_frame.text = text
    frame(t, anchor)
    style(t, font, size, color, bold=bold, align=align, spc=spc)
    add_back(slide, t); return t

def pic(slide, path, x, y, h=None, w=None, alpha=None, back=True):
    p = slide.shapes.add_picture(path, Inches(x), Inches(y), Inches(w) if w else None, Inches(h) if h else None)
    if alpha is not None:
        blip = p._element.find(".//" + qn("a:blip"))
        a = etree.SubElement(blip, qn("a:alphaModFix")); a.set("amt", str(int(alpha * 100000)))
    if back: add_back(slide, p)
    return p

def eixo(slide, x, y0, y1, color=OURO):
    """motivo do EIXO: linha vertical fina com os pontos do símbolo no alto"""
    vline(slide, x, y0 + 0.62, y1, color, 1.0)
    dot(slide, x, y0 + 0.06, 0.07, color)
    dot(slide, x, y0 + 0.30, 0.13, color)

def corner(slide, dark=False):
    pic(slide, A + ("sym_gold.png" if dark else "sym_blue.png"), 12.36, 6.72, h=0.5)

# ---------- imagens ----------
def fill_crop(p, x, y, w, h):
    iw, ih = p.image.size
    target = w / h; src = iw / ih
    p.crop_left = p.crop_right = p.crop_top = p.crop_bottom = 0
    if src > target:
        c = (1 - target / src) / 2; p.crop_left = c; p.crop_right = c
    else:
        c = (1 - src / target) / 2; p.crop_top = c; p.crop_bottom = c
    place(p, x, y, w, h)

def match_bg(p):
    """ajusta canais para que o fundo claro da ilustração coincida com o bege leitura"""
    blip = p._element.find(".//" + qn("a:blip")); rid = blip.get(qn("r:embed"))
    part = p.part.related_part(rid)
    im = Image.open(io.BytesIO(part.blob)).convert("RGB"); a = np.asarray(im).astype(float)
    corners = np.concatenate([a[:20, :20].reshape(-1, 3), a[:20, -20:].reshape(-1, 3), a[-20:, :20].reshape(-1, 3), a[-20:, -20:].reshape(-1, 3)])
    bg = np.median(corners, 0); tgt = np.array([0xF4, 0xEF, 0xEA], float)
    a = np.clip(a * (tgt / bg), 0, 255).astype(np.uint8)
    buf = io.BytesIO(); Image.fromarray(a).save(buf, "PNG"); part._blob = buf.getvalue()

