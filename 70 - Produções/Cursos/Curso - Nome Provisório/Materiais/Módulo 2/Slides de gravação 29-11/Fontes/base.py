"""Tipos de tela do TSH para M2 (pontes, práticas e teorias novas).
Usa a paleta e as funções de tsh_lib (ferramentas do repositório).
Quadro 13,333 x 7,5 pol.; área da câmera livre: x > 10,7 e y < 2,4."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from tsh_lib import *
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from anim import transition

W, H = 13.333, 7.5


class Deck:
    def __init__(self, code, kind):
        self.prs = Presentation()
        self.prs.slide_width = Inches(W); self.prs.slide_height = Inches(H)
        self.code = code; self.kind = kind; self.n = 0
        self.blank = self.prs.slide_layouts[6]
        self.guide = []  # (n, title, cue, notes)

    # ---------- base ----------
    def _new(self, dark=False):
        s = self.prs.slides.add_slide(self.blank)
        self.n += 1
        if dark: bg_grad(s)
        else: bg_solid(s, BEGE)
        transition(s)
        return s

    def _chrome(self, s, title, dark=False):
        label(s, 0.6, 0.32, 6, 0.3, "TRADUZINDO O SER HUMANO", size=9,
              color=(OURO if dark else EST), bold=True, spc=150)
        t = label(s, 0.6, 0.62, 9.9, 0.9, title, font=SERIF, size=34,
                  color=("FFFFFF" if dark else NOT), bold=False, anchor="t")
        rect(s, 0.62, 1.55, 0.55, 0.035, fill=OURO)
        corner(s, dark)

    def _footer(self, s, dark=False):
        label(s, 0.6, 6.95, 6, 0.3, f"{self.code} · {self.kind}", size=10,
              color=(BEGE if dark else MUTED), bold=False)

    def notes(self, s, title, cue, lines, nxt=None):
        """Notas: uma função no topo, frases curtas, blocos separados,
        citações literais entre « », e a passagem para a tela seguinte."""
        out = [f"[{cue}]", ""]
        out += lines
        if nxt: out += ["", f"→ {nxt}"]
        txt = "\n".join(out)
        s.notes_slide.notes_text_frame.text = txt
        self.guide.append((self.n, title, cue, txt))

    def text(self, s, x, y, w, h, lines, size=20, color=NOT, font=SANS, bold=False,
             align="l", line=1.15, after=6, anchor="t", italic=None):
        t = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tf = t.text_frame
        lines = lines if isinstance(lines, list) else [lines]
        tf.text = lines[0]
        for l in lines[1:]:
            tf.add_paragraph().text = l
        frame(t, anchor)
        style(t, font, size, color, bold=bold, align=align, line=line * 100, after=after, italic=italic)
        return t

    def save(self, path):
        self.prs.save(path)

    # ---------- tipos ----------
    def capa(self, title, subtitle, cue, lines, nxt=None, tag=None):
        s = self._new(dark=True)
        self.text(s, 0.8, 1.6, 7.6, 0.4, tag or f"{self.code} · {self.kind}".upper(),
                  size=13, color=OURO, bold=True)
        self.text(s, 0.8, 2.15, 8.0, 2.2, title, size=44, color="FFFFFF", font=SERIF, line=1.0)
        self.text(s, 0.8, 4.45, 7.6, 1.0, subtitle, size=18, color=BEGE, line=1.2)
        self.text(s, 0.8, 6.3, 6, 0.4, "Fabiano Deliberalli", size=14, color=BEGE)
        pic(s, A + "mark_gold.png", 9.55, 2.6, h=2.9)
        self.notes(s, title, cue, lines, nxt)
        return s

    def frase(self, title, quote, source, cue, lines, nxt=None, dark=False, lead=None):
        s = self._new(dark)
        self._chrome(s, title, dark)
        eixo(s, 1.0, 2.15, 6.3, OURO)
        y = 2.3
        if lead:
            self.text(s, 1.5, y, 8.8, 0.6, lead, size=18, color=(BEGE if dark else EST))
            y += 0.75
        self.text(s, 1.5, y, 9.2, 3.0, f"“{quote}”", size=32, font=SERIF, italic=True,
                  color=("FFFFFF" if dark else NOT), line=1.12)
        self.text(s, 1.5, 6.05, 9.0, 0.5, source, size=14, color=OURO, bold=True)
        self._footer(s, dark)
        self.notes(s, title, cue, lines, nxt)
        return s

    def historia(self, title, origem, beats, moral, cue, lines, nxt=None):
        s = self._new()
        self._chrome(s, title)
        self.text(s, 0.62, 1.8, 6.5, 0.4, origem, size=14, color=OURO, bold=True)
        x = 0.85; y0 = 2.5; step = min(0.95, 3.9 / max(1, len(beats)))
        vline(s, x, y0 + 0.12, y0 + step * (len(beats) - 1) + 0.12, OURO, 1.25)
        for i, b in enumerate(beats):
            dot(s, x, y0 + i * step + 0.12, 0.17, OURO)
            self.text(s, 1.2, y0 + i * step - 0.05, 5.9, step, b, size=18, color=NOT, line=1.05)
        rect(s, 7.6, 2.6, 4.9, 3.7, fill=PET, rounded=0.06)
        self.text(s, 7.95, 2.9, 4.2, 3.1, moral, size=24, font=SERIF, color="FFFFFF", line=1.12,
                  anchor="ctr")
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def cartoes(self, title, cards, cue, lines, nxt=None, foot=None, lead=None, dark_idx=()):
        """cards: [(cabeça, texto)]; 2 a 4 cartões numa linha."""
        s = self._new()
        self._chrome(s, title)
        y = 2.55
        if lead:
            self.text(s, 0.62, 1.85, 11.5, 0.6, lead, size=18, color=EST)
            y = 2.75
        n = len(cards); gap = 0.3; w = (12.1 - gap * (n - 1)) / n
        h = 2.75 if n <= 3 else 3.2
        ts = 18 if n <= 3 else 16
        for i, (hd, tx) in enumerate(cards):
            x = 0.62 + i * (w + gap)
            dk = i in dark_idx
            rect(s, x, y, w, h, fill=(PET if dk else CARD), line=(None if dk else LINHA), rounded=0.05)
            self.text(s, x + 0.25, y + 0.25, w - 0.5, 0.9, hd, size=20, font=SERIF,
                      color=(OURO if dk else EST), line=1.0)
            self.text(s, x + 0.25, y + 1.1, w - 0.5, h - 1.25, tx, size=ts,
                      color=("FFFFFF" if dk else NOT), line=1.12)
        if foot:
            self.text(s, 0.62, y + h + 0.25, 11.8, 0.5, foot, size=16, color=EST, italic=True)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def sequencia(self, title, steps, cue, lines, nxt=None, foot=None, lead=None):
        s = self._new()
        self._chrome(s, title)
        if lead:
            self.text(s, 0.62, 1.85, 11.5, 0.6, lead, size=18, color=EST)
        n = len(steps); yc = 3.45
        lw = min(2.9, 11.9 / n - 0.2)
        x0 = 0.62 + lw / 2; x1 = 12.52 - lw / 2
        c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x0), Inches(yc), Inches(x1), Inches(yc))
        c.line.color.rgb = rgb(OURO); c.line.width = Pt(1.25); add_back(s, c)
        dx = (x1 - x0) / (n - 1) if n > 1 else 0
        for i, st in enumerate(steps):
            cx = x0 + i * dx
            dot(s, cx, yc, 0.62, fill=(PET if i == n - 1 else NOT))
            self.text(s, cx - 0.3, yc - 0.25, 0.6, 0.5, str(i + 1), size=18, color="FFFFFF",
                      font=SERIF, align="ctr", anchor="ctr")
            self.text(s, cx - lw / 2, yc + 0.55, lw, 1.9, st, size=18, color=NOT, align="ctr", line=1.08)
        if foot:
            self.text(s, 0.62, 5.95, 11.8, 0.6, foot, size=17, color=EST, italic=True)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def dois(self, title, a, b, seta, cue, lines, nxt=None, foot=None, volta=None):
        """Dois polos (a, b = (rótulo, legenda)) ligados por seta; opcional seta de volta."""
        s = self._new()
        self._chrome(s, title)
        for i, (lb, lg) in enumerate((a, b)):
            x = 1.1 if i == 0 else 7.6
            o = rect(s, x, 2.75, 4.6, 1.75, fill=(CARD if i == 0 else PET), line=(LINHA if i == 0 else None),
                     kind=MSO_SHAPE.OVAL)
            self.text(s, x + 0.3, 2.95, 4.0, 1.35, lb, size=22, font=SERIF, align="ctr", anchor="ctr",
                      color=(NOT if i == 0 else "FFFFFF"), line=1.0)
            self.text(s, x, 4.7, 4.6, 0.9, lg, size=16, align="ctr", color=MUTED, line=1.1)
        c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(5.85), Inches(3.45), Inches(7.45), Inches(3.45))
        c.line.color.rgb = rgb(OURO); c.line.width = Pt(1.5)
        c.line._get_or_add_ln().append(etree.fromstring(
            '<a:tailEnd xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" type="triangle"/>'))
        add_back(s, c)
        self.text(s, 5.6, 2.85, 2.1, 0.5, seta, size=13, color=EST, align="ctr", bold=True)
        if volta:
            c2 = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(7.45), Inches(3.85), Inches(5.85), Inches(3.85))
            c2.line.color.rgb = rgb(EST); c2.line.width = Pt(1.25)
            c2.line._get_or_add_ln().append(etree.fromstring(
                '<a:tailEnd xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" type="triangle"/>'))
            add_back(s, c2)
            self.text(s, 5.6, 3.92, 2.1, 0.5, volta, size=13, color=EST, align="ctr", bold=True)
        if foot:
            self.text(s, 0.62, 5.95, 11.8, 0.6, foot, size=17, color=EST, italic=True, align="ctr")
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def roda(self, title, centro, rotulos, cue, lines, nxt=None, foot=None, dark=False):
        """Centro com quatro rótulos ao redor (eixo, retorno)."""
        s = self._new(dark)
        self._chrome(s, title, dark)
        rect(s, 4.1, 2.45, 5.1, 3.2, fill=None, line=OURO, lw=1.25, kind=MSO_SHAPE.OVAL)
        rect(s, 5.15, 3.45, 3.0, 1.2, fill=(OURO if dark else NOT), kind=MSO_SHAPE.OVAL)
        self.text(s, 5.15, 3.5, 3.0, 1.1, centro, size=22, font=SERIF, align="ctr", anchor="ctr",
                  color=(NOT if dark else "FFFFFF"), line=1.0)
        pos = [(1.0, 2.6, "r"), (9.5, 2.6, "l"), (1.0, 4.85, "r"), (9.5, 4.85, "l")]
        for (x, y, al), r in zip(pos, rotulos):
            self.text(s, x, y, 2.9, 0.9, r, size=18, color=(BEGE if dark else EST),
                      align=al, line=1.05, anchor="ctr")
        if foot:
            self.text(s, 0.62, 6.0, 11.8, 0.6, foot, size=17, color=(OURO if dark else EST),
                      italic=True, align="ctr")
        self._footer(s, dark)
        self.notes(s, title, cue, lines, nxt)
        return s

    def passo(self, title, pergunta, apoio, cue, lines, nxt=None, registro=None,
              pausa="Pause o vídeo para perceber e registrar."):
        """Tela estável durante a realização: uma pergunta grande e o nome do registro."""
        s = self._new()
        self._chrome(s, title)
        rect(s, 0.62, 2.2, 7.6, 3.5, fill="FFFFFF", line=LINHA, rounded=0.04)
        vline(s, 0.95, 2.55, 5.35, OURO, 2.0)
        self.text(s, 1.25, 2.4, 6.7, 3.1, pergunta, size=32, font=SERIF, color=NOT, anchor="ctr", line=1.1)
        self.text(s, 8.7, 2.6, 3.9, 2.4, apoio, size=17, color=EST, line=1.15)
        if registro:
            rect(s, 8.7, 4.95, 3.9, 0.7, fill=PET, rounded=0.1)
            self.text(s, 8.85, 5.0, 3.6, 0.6, f"Registro: {registro}", size=16, color="FFFFFF",
                      bold=True, anchor="ctr", align="ctr")
        if pausa:
            self.text(s, 0.62, 6.0, 11.8, 0.5, pausa, size=16, color=OURO, bold=True)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def comparar(self, title, lead, rows, cue, lines, nxt=None, foot=None):
        """rows: [(rótulo, texto, escuro?)]"""
        s = self._new()
        self._chrome(s, title)
        self.text(s, 0.62, 1.85, 11.5, 0.5, lead, size=18, color=EST)
        y = 2.6
        for lb, tx, dk in rows:
            rect(s, 0.62, y, 11.9, 0.95, fill=(PET if dk else CARD), line=(None if dk else LINHA), rounded=0.06)
            self.text(s, 0.9, y + 0.08, 3.0, 0.8, lb, size=14, bold=True, color=(OURO if dk else EST),
                      anchor="ctr")
            self.text(s, 4.0, y + 0.08, 8.2, 0.8, tx, size=20, color=("FFFFFF" if dk else NOT), anchor="ctr")
            y += 1.15
        if foot:
            self.text(s, 0.62, y + 0.1, 11.8, 0.6, foot, size=16, color=EST, italic=True)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def imagem(self, title, path, legenda, credito, texto, cue, lines, nxt=None):
        s = self._new()
        self._chrome(s, title)
        p = pic(s, path, 0.62, 1.95, h=4.6, back=False)
        self.text(s, 0.62, 6.58, 7.2, 0.35, credito, size=10, color=MUTED)
        self.text(s, 8.0, 2.5, 4.6, 0.6, legenda, size=14, color=OURO, bold=True)
        self.text(s, 8.0, 3.1, 4.6, 3.0, texto, size=20, color=NOT, line=1.15)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s

    def fechamento(self, title, frase, linhas, cue, lines, nxt=None):
        s = self._new(dark=True)
        self._chrome(s, title, dark=True)
        self.text(s, 0.62, 2.1, 9.8, 2.4, linhas, size=20, color=BEGE, line=1.2, after=8)
        rect(s, 0.62, 4.75, 11.9, 1.15, fill=NOT, rounded=0.08)
        self.text(s, 0.9, 4.8, 11.4, 1.05, frase, size=28, font=SERIF, color=OURO, italic=True,
                  anchor="ctr", align="ctr")
        self._footer(s, dark=True)
        self.notes(s, title, cue, lines, nxt)
        return s

    # ---------- telas de imagem ----------
    def ilustra(self, title, img, origem, cue, lines, nxt=None, dark=True, legenda=None):
        """Imagem em tela cheia; só o nome da história e a tradição. A condução fica nas notas."""
        s = self._new(dark)
        pic(s, img, 0, 0, w=W, back=False)
        cor_t = "FFFFFF" if dark else NOT
        self.text(s, 0.6, 6.05, 9.0, 0.35, origem, size=13, color=OURO, bold=True)
        self.text(s, 0.6, 6.38, 9.5, 0.6, title, size=28, font=SERIF, color=cor_t, line=1.0)
        if legenda:
            self.text(s, 7.2, 7.05, 5.6, 0.3, legenda, size=10, color=(BEGE if dark else MUTED), align="r")
        corner(s, dark)
        self.notes(s, title, cue, lines, nxt)
        return s

    def niveis(self, title, grupos, cue, lines, nxt=None, lead=None, foot=None):
        """grupos: [(rótulo do grupo, [(nome, subtítulo)])], numeração contínua, uma linha por grupo."""
        s = self._new()
        self._chrome(s, title)
        if lead:
            self.text(s, 0.62, 1.8, 11.5, 0.5, lead, size=17, color=EST)
        y = 2.35; k = 1
        for gi, (rot, itens) in enumerate(grupos):
            self.text(s, 0.62, y, 11.9, 0.4, rot.upper(), size=13, color=OURO, bold=True)
            n = len(itens); gap = 0.25; w = (11.9 - gap * (n - 1)) / n
            dk = gi == len(grupos) - 1
            for i, (nome, sub) in enumerate(itens):
                x = 0.62 + i * (w + gap)
                rect(s, x, y + 0.42, w, 1.5, fill=(PET if dk else CARD), line=(None if dk else LINHA), rounded=0.06)
                self.text(s, x + 0.2, y + 0.5, w - 0.4, 0.5, f"{k}  {nome}", size=20, font=SERIF,
                          color=(OURO if dk else EST))
                self.text(s, x + 0.2, y + 1.05, w - 0.4, 0.8, sub, size=15, color=("FFFFFF" if dk else NOT), line=1.05)
                k += 1
            y += 2.1
        if foot:
            self.text(s, 0.62, 6.5, 11.8, 0.4, foot, size=15, color=EST, italic=True)
        self._footer(s)
        self.notes(s, title, cue, lines, nxt)
        return s
