"""Mapas do TSH: versão do Módulo 1 (quatro mapas, anexo de M1.4) e versão completa (nove mapas, anexo de M5.1).
Gera HTML e imprime em PDF A4 com o Chrome headless."""
import subprocess, os, sys, html
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/build_m2v/mapas"
os.makedirs(OUT, exist_ok=True)

NOT, PET, EST, OURO, BEGE, CARD, LINHA, MUTED = "#082A45", "#173F52", "#245E78", "#C99A64", "#F4EFEA", "#FBF8F4", "#E2D8CC", "#5A6B74"

# ---------- ícones (SVG simples, um por mapa) ----------
def svg(body, w=64, h=64):
    return f'<svg viewBox="0 0 64 64" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="{EST}" stroke-width="2.2" stroke-linecap="round">{body}</svg>'
IC = {
 "percurso": svg(f'<line x1="8" y1="32" x2="56" y2="32" stroke="{OURO}"/><circle cx="10" cy="32" r="5" fill="{NOT}" stroke="none"/><circle cx="32" cy="32" r="5" fill="{NOT}" stroke="none"/><circle cx="54" cy="32" r="5" fill="{PET}" stroke="none"/><path d="M20 22 q12 -12 24 0" stroke="{OURO}"/>'),
 "janelas": svg(''.join(f'<rect x="{6+i*11}" y="22" width="8" height="20" rx="1.5"/>' for i in range(5)) + f'<line x1="4" y1="48" x2="60" y2="48" stroke="{OURO}"/>'),
 "cartografia": svg(f'<path d="M10 40 q10 -18 22 -6 t22 -10"/><path d="M10 50 q12 -14 24 -4 t20 -8" stroke="{OURO}"/><circle cx="34" cy="28" r="3" fill="{NOT}" stroke="none"/>'),
 "centro": svg(f'<circle cx="32" cy="32" r="22" stroke="{LINHA}"/><circle cx="32" cy="32" r="13"/><circle cx="32" cy="32" r="4" fill="{OURO}" stroke="none"/><line x1="32" y1="4" x2="32" y2="60" stroke="{OURO}"/>'),
 "niveis": svg(''.join(f'<line x1="{14+i*2}" y1="{10+i*7}" x2="{50-i*2}" y2="{10+i*7}" stroke="{OURO if i in (0,6) else EST}"/>' for i in range(7))),
 "shen": svg(''.join(f'<circle cx="{32+20*__import__("math").sin(i*1.2566)}" cy="{33-20*__import__("math").cos(i*1.2566)}" r="5" fill="{OURO if i==0 else "none"}"/>' for i in range(5)) + '<circle cx="32" cy="33" r="20" stroke-dasharray="2 4"/>'),
 "tantien": svg(f'<line x1="32" y1="6" x2="32" y2="58" stroke="{LINHA}"/><circle cx="32" cy="14" r="5"/><circle cx="32" cy="31" r="6"/><circle cx="32" cy="49" r="7" fill="{OURO}" stroke="none"/>'),
 "partes": svg(f'<circle cx="24" cy="26" r="12"/><circle cx="40" cy="26" r="12"/><circle cx="32" cy="40" r="12" stroke="{OURO}"/>'),
 "eus": svg(f'<line x1="32" y1="4" x2="32" y2="60" stroke="{OURO}"/><circle cx="32" cy="14" r="7"/><circle cx="32" cy="32" r="7"/><circle cx="32" cy="50" r="7" fill="{PET}" stroke="none"/>'),
}

# ---------- conteúdo ----------
# (chave, nome, onde, objetivo, pergunta, na prática, o que acrescenta)
M = {
 "percurso": ("Mapa do percurso", "Módulo 0 e a abertura de cada módulo",
   "Situar você no caminho.",
   "Onde estou no percurso, e para onde ele vai?",
   "Veja em qual das três direções o módulo atual trabalha: traduzir, ganhar eixo e presença ou ocupar o próprio espaço.",
   "Orientação. Cada módulo tem um lugar, e voltar a um tema não é andar para trás: as três direções se alimentam."),
 "janelas": ("As Cinco Janelas", "Aula 1.5",
   "Ampliar a leitura de uma situação.",
   "Por onde mais posso olhar o que aconteceu?",
   "Passe pelas cinco janelas (corpo, emoção, mente, relações, espiritualidade), uma palavra para cada. Note qual mostrou algo novo.",
   "Você sai da explicação única e encontra a janela que costuma ficar fechada."),
 "cartografia": ("A Cartografia", "Aula 1.6",
   "Registrar as camadas de uma situação.",
   "Que camadas tem esta situação, e que forma ela toma?",
   "Escolha um detalhe da janela que mostrou algo novo e dê a ele uma forma: uma palavra, um desenho, um gesto. Confira se combina com o que você sente.",
   "A experiência sai só da cabeça e ganha um registro que você pode rever depois, para perceber o que mudou."),
 "centro": ("Estado, eixo e referência profunda", "Aula 1.7",
   "Distinguir o que oscila do que permanece.",
   "Quando perco o eixo, o que mudou, e o que continuou possível?",
   "Passe pelas quatro entradas: estado (como estou agora?), movimento (para onde a experiência está indo?), referência (o que me ajuda a me orientar?) e participação (o que consigo fazer agora?).",
   "O pêndulo mostra que o estado oscila; a espiral, que um tema pode voltar sem que você esteja no mesmo ponto. Oscilar não é perder a Essência."),
 "niveis": ("Os sete níveis da experiência", "Aula 2.5",
   "Separar o vivido da interpretação, da explicação e dos efeitos.",
   "O que eu vivi, o que eu entendi, que explicação eu dou, e o que isso produz na minha vida?",
   "Diante de uma experiência marcante, situe cada frase sua num nível: o fenômeno vivido, a tradução, a interpretação, as hipóteses, as implicações, as condições de integração e a incorporação.",
   "Você acolhe a experiência sem precisar decidir de imediato a sua origem, e não passa direto do vivido para a conclusão."),
 "shen": ("Os Cinco Shen", "Aula 3.5; retomados em 2.6, 4.6, 5.2, 5.5, 5.6 e 5.8",
   "Ler o ser humano pela Medicina Chinesa e pelo Taoísmo, a partir da formação de Fabiano com o mestre Liu Chih Ming, da linhagem de Liu Pai Lin.",
   "Que aspecto da vitalidade e do espírito está em jogo agora?",
   "Note se a situação pede reunir (Shen, Coração), imaginar (Hun, Fígado), sentir no corpo (Po, Pulmão), discernir e assimilar (Yi, Baço) ou sustentar a vontade (Zhi, Rim).",
   "Uma leitura que liga órgãos, emoções e consciência, e que dá a cada capacidade um lugar no corpo e um cultivo."),
 "tantien": ("Os três Tan Tien", "Aulas 3.5 e 3.6; linha do Hara em 4.6",
   "Dar ao eixo um endereço no corpo.",
   "Onde, no corpo, a minha presença se apoia agora?",
   "Na postura da árvore, respire passando pelos três centros: baixo ventre, peito, testa. Note qual está mais vivo e qual está mais distante.",
   "O eixo deixa de ser só uma ideia e passa a ser sentido. Prepara a linha do Hara, que liga os três centros numa intenção."),
 "partes": ("As partes", "Aula 4.5",
   "Escutar partes internas em conflito.",
   "Que parte de mim reage, e o que ela protege?",
   "Olhe para a parte que reage, converse com ela e fale como ela, com compaixão. Volte ao eixo antes de decidir.",
   "Padrões passam a ser vistos como proteção aprendida, e não como defeito. O conflito interno vira diálogo."),
 "eus": ("Os Três Eus", "Aula 5.1",
   "Reconhecer qual dimensão está conduzindo, e como elas podem conversar.",
   "Que dimensão de mim está conduzindo agora?",
   "Note o Eu Básico (corpo, impulso, emoção), o Eu Médio (reflexão, escolha) e o Eu Superior (sentido, valores, Essência). O eixo é a comunicação entre os três.",
   "Reúne os mapas anteriores numa só leitura, e a Essência volta como referência para as escolhas."),
}

USO = [
 ("Comece pelo vivido", "A experiência vem primeiro. O mapa vem depois, para ajudar a olhar."),
 ("Escolha pela pergunta", "Não pelo mapa. Qual é a sua pergunta agora? Use o mapa que responde a ela."),
 ("Um mapa por vez", "Misturar mapas confunde. Termine um olhar antes de começar outro."),
 ("Nenhum mapa é você", "Se um mapa não ajuda, outro pode ajudar. Os mapas servem a você, e não o contrário."),
 ("Escrever é opcional", "Se quiser, anote no Caderno de Reencontros. Se não, só faça a pergunta e sinta a resposta."),
]

SELETOR = [
 ("me situar no curso", "percurso"),
 ("entender algo que aconteceu", "janelas"),
 ("guardar o que percebi, para rever depois", "cartografia"),
 ("voltar depois de perder o eixo", "centro"),
 ("cuidar de uma experiência marcante ou incomum", "niveis"),
 ("cuidar da vitalidade e da presença no corpo", "tantien"),
 ("ler a situação pela Medicina Chinesa", "shen"),
 ("entender uma reação mais forte do que eu", "partes"),
 ("decidir com sentido", "eus"),
]

CSS = f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family: Inter, Arial, sans-serif; color:{NOT}; background:{BEGE}; }}
.page {{ width:210mm; height:297mm; padding:14mm 14mm 12mm; position:relative; page-break-after:always; overflow:hidden; }}
.page:last-child {{ page-break-after:auto; }}
.marca {{ font-size:7.5pt; letter-spacing:.18em; font-weight:700; color:{EST}; }}
h1 {{ font-family:'EB Garamond', Georgia, serif; font-weight:400; font-size:28pt; margin:3mm 0 1mm; line-height:1.05; }}
.sub {{ font-size:10.5pt; color:{EST}; margin-bottom:2mm; }}
.fio {{ width:14mm; height:1mm; background:{OURO}; margin:2.5mm 0 4mm; }}
.lead {{ font-size:11.5pt; line-height:1.45; margin-bottom:5mm; max-width:170mm; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:4.5mm; }}
.card {{ background:{CARD}; border:0.3mm solid {LINHA}; border-radius:3mm; padding:5mm 5.5mm 4mm; break-inside:avoid; }}
.card .top {{ display:flex; gap:3.5mm; align-items:center; margin-bottom:2.5mm; }}
.card h2 {{ font-family:'EB Garamond', Georgia, serif; font-weight:500; font-size:18pt; margin:0; line-height:1.05; }}
.card .onde {{ font-size:8.5pt; color:{OURO}; font-weight:700; letter-spacing:.06em; text-transform:uppercase; margin-top:1mm; }}
.q {{ background:{PET}; color:white; border-radius:2mm; padding:3mm 3.5mm; font-family:'EB Garamond', Georgia, serif; font-size:14pt; line-height:1.15; margin:2.5mm 0 3mm; }}
.row {{ font-size:10pt; line-height:1.36; margin-bottom:2.4mm; }}
.row b {{ display:block; font-size:8pt; letter-spacing:.1em; text-transform:uppercase; color:{EST}; margin-bottom:.4mm; }}
.uso {{ display:grid; grid-template-columns:1fr; gap:3.5mm; margin-top:4mm; }}
.uso div {{ background:{CARD}; border:0.3mm solid {LINHA}; border-radius:2.5mm; padding:4.5mm 6mm; font-size:12pt; line-height:1.4; display:grid; grid-template-columns:52mm 1fr; gap:5mm; align-items:center; }}
.uso b {{ font-family:'EB Garamond', Georgia, serif; font-size:17pt; font-weight:500; color:{EST}; line-height:1.05; }}
.foot {{ position:absolute; bottom:8mm; left:14mm; right:14mm; font-size:7.5pt; color:{MUTED}; display:flex; justify-content:space-between; }}
.trilha {{ display:grid; grid-template-columns: 1fr 1.4fr 1.6fr; gap:4mm; margin-top:2mm; }}
.dir {{ border-radius:3mm; padding:5mm; }}
.dir h3 {{ font-size:8.5pt; letter-spacing:.14em; text-transform:uppercase; margin:0 0 3mm; }}
.dir .m {{ display:flex; gap:3mm; align-items:flex-start; margin-bottom:7mm; }}
.dir .m .t {{ font-family:'EB Garamond', Georgia, serif; font-size:15.5pt; line-height:1.05; }}
.dir .m .p {{ font-size:10pt; line-height:1.35; margin-top:1.2mm; }}
.sel {{ width:100%; border-collapse:collapse; font-size:10.5pt; }}
.sel td {{ padding:2.3mm 3mm; border-bottom:0.3mm solid {LINHA}; vertical-align:middle; }}
.sel td:first-child {{ color:{EST}; width:48%; }}
.sel td:last-child {{ font-family:'EB Garamond', Georgia, serif; font-size:14pt; }}
.nota {{ font-size:10pt; line-height:1.4; color:{MUTED}; margin-top:4mm; }}
.box {{ background:{PET}; color:white; border-radius:3mm; padding:5mm 6mm; font-family:'EB Garamond', Georgia, serif; font-size:17pt; line-height:1.25; margin-top:6mm; }}
"""

def card(k):
    n, onde, obj, q, pr, ac = M[k]
    e = html.escape
    return f'''<div class="card"><div class="top">{IC[k]}<div><h2>{e(n)}</h2><div class="onde">{e(onde)}</div></div></div>
<div class="row"><b>Para quê</b>{e(obj)}</div>
<div class="q">{e(q)}</div>
<div class="row"><b>Na prática</b>{e(pr)}</div>
<div class="row"><b>O que acrescenta</b>{e(ac)}</div></div>'''

def head(titulo, sub):
    return f'<div class="marca">TRADUZINDO O SER HUMANO</div><h1>{titulo}</h1><div class="sub">{sub}</div><div class="fio"></div>'

def foot(txt, n):
    return f'<div class="foot"><span>{txt}</span><span>{n}</span></div>'

def uso_html():
    return '<div class="uso">' + ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in USO) + '</div>'

def render(name, pages):
    h = f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    p = f"{OUT}/{name}.html"; open(p, "w", encoding="utf-8").write(h)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={OUT}/{name}.pdf", p], check=True, capture_output=True)
    print(name)

# ======== Versão do Módulo 1 ========
rod1 = "Traduzindo o Ser Humano · Os mapas do Módulo 1 · anexo da aula 1.4"
p1 = f'''<div class="page">{head("Os mapas do Módulo 1", "A experiência é o território. As explicações são mapas.")}
<div class="lead">No Módulo 1 você encontra quatro mapas. Cada um serve para uma pergunta diferente. Nenhum descreve você por inteiro: são instrumentos para olhar, e você escolhe qual usar conforme a pergunta do momento.</div>
<div class="grid">{card("percurso")}{card("janelas")}{card("cartografia")}{card("centro")}</div>
{foot(rod1, "1/2")}</div>'''
p2 = f'''<div class="page">{head("Como usar os mapas", "Cinco cuidados simples")}
{uso_html()}
<div class="box">Um exemplo. Algo aconteceu e você reagiu como sempre. Primeiro, as quatro entradas da aula 1.7: como estou, para onde estou indo, o que me orienta, o que consigo fazer agora? Depois, se quiser entender, as Cinco Janelas. Se quiser guardar, a Cartografia.</div>
<div style="margin-top:9mm" class="row"><b>Os mapas que virão</b>Ao longo do curso, outros mapas se juntam a estes: os sete níveis da experiência (aula 2.5), os Cinco Shen e os três Tan Tien (Módulo 3), as partes (aula 4.5) e os Três Eus (aula 5.1). Na aula 5.1 você recebe a versão completa desta página.</div>
<div class="nota">Escrever é opcional. As práticas de cada mapa são guiadas nos vídeos das aulas.<br>Conte no próximo encontro: qual mapa ajudou você, e qual confundiu? A sua resposta vai ajustar estas páginas.</div>
{foot(rod1, "2/2")}</div>'''
render("TSH-Mapas-do-Modulo-1", [p1, p2])

# ======== Versão completa ========
rod2 = "Traduzindo o Ser Humano · Os mapas do TSH · anexo da aula 5.1"
def dirbox(titulo, cor_bg, cor_tx, keys, dark=False):
    itens = ''.join(f'<div class="m">{IC[k].replace(EST, "#FFFFFF") if dark else IC[k]}<div><div class="t">{M[k][0]}</div><div class="p">{html.escape(M[k][3])}</div></div></div>' for k in keys)
    return f'<div class="dir" style="background:{cor_bg};color:{cor_tx}"><h3 style="color:{OURO}">{titulo}</h3>{itens}</div>'
q1 = f'''<div class="page">{head("Os mapas do TSH", "Nove mapas, nove perguntas. A experiência é o território.")}
<div class="lead">Cada mapa responde a uma pergunta. Eles aparecem ao longo do percurso, na ordem em que você precisa deles. Esta página reúne todos, com a pergunta que cada um ajuda a responder.</div>
<div class="trilha">
{dirbox("Entrada · Módulo 0", CARD, NOT, ["percurso"])}
{dirbox("Traduzir · Módulos 1 e 2", CARD, NOT, ["janelas", "cartografia", "centro", "niveis"])}
{dirbox("Ganhar eixo e presença · Módulos 3 a 6", PET, "#FFFFFF", ["shen", "tantien", "partes", "eus"], dark=True)}
</div>
<div class="box">Os Três Eus, na aula 5.1, reúnem os mapas anteriores numa só leitura: o eixo como a comunicação entre o corpo, a reflexão e a Essência.</div>
{foot(rod2, "1/5")}</div>'''
q2 = f'<div class="page">{head("Traduzir", "Mapa do percurso · Cinco Janelas · Cartografia · Estado, eixo e referência")}<div class="grid">{card("percurso")}{card("janelas")}{card("cartografia")}{card("centro")}</div>{foot(rod2, "2/5")}</div>'
q3 = f'<div class="page">{head("Traduzir e ganhar eixo", "Sete níveis · Cinco Shen · três Tan Tien · partes")}<div class="grid">{card("niveis")}{card("shen")}{card("tantien")}{card("partes")}</div>{foot(rod2, "3/5")}</div>'
sel = ''.join(f'<tr><td>Se você quer {a}…</td><td>{M[k][0]}</td></tr>' for a, k in SELETOR)
q4 = f'''<div class="page">{head("Os Três Eus e a escolha do mapa", "Qual mapa usar, conforme a sua pergunta")}
{card("eus")}<div style="height:6mm"></div><table class="sel">{sel}</table>
<div class="nota">O Mapa dos Três Eus é uma cartografia pedagógica do curso: não é uma divisão literal da mente nem uma verdade que você precise adotar.</div>
{foot(rod2, "4/5")}</div>'''
q5 = f'''<div class="page">{head("Como usar os mapas", "Cinco cuidados simples")}
{uso_html()}
<div class="box">Um exemplo. Uma reação forte, de novo. Estado, eixo e referência: o que mudou, e o que continuou possível? Os três Tan Tien: onde o corpo pode se apoiar agora? Depois, com calma, as partes: que parte reagiu, e o que ela protegia? Por fim, os Três Eus: o que a Essência pede desta escolha?</div>
<div class="nota">Escrever é opcional. As práticas de cada mapa são guiadas nos vídeos das aulas indicadas.<br>Conte no próximo encontro: qual mapa ajudou você, e qual confundiu? A sua resposta vai ajustar estas páginas.</div>
{foot(rod2, "5/5")}</div>'''
render("TSH-Mapas-do-TSH-completo", [q1, q2, q3, q4, q5])
