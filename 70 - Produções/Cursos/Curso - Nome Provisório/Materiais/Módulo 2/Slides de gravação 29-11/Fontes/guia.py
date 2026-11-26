import glob, os, sys
from pptx import Presentation
D = "/home/claude/out/slides"
ordem = ["Pontes", "M2.2", "M2.3", "M2.4", "M2.5", "M2.6"]
tempo = {"Pontes": "3 a 4 min por ponte", "M2.2": "8 a 10 min", "M2.3": "10 a 12 min",
         "M2.4": "15 a 18 min", "M2.5": "12 a 14 min", "M2.6": "12 a 14 min"}
files = sorted(glob.glob(f"{D}/*.pptx"), key=lambda f: [i for i, k in enumerate(ordem) if k in f][0])
md = [open("/home/claude/build/guia_intro.md").read()]
for f in files:
    k = [k for k in ordem if k in f][0]
    nome = os.path.basename(f)[:-5].replace("TSH · ", "")
    p = Presentation(f)
    md.append(f"\n# {nome}\n\nEstimativa: {tempo[k]}. {len(p.slides)} telas.\n")
    for i, s in enumerate(p.slides, 1):
        titulo = ""
        for sh in s.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip() and sh.text_frame.text.strip() != "TRADUZINDO O SER HUMANO":
                titulo = sh.text_frame.text.strip().split("\n")[0]; break
        n = s.notes_slide.notes_text_frame.text
        linhas = n.split("\n")
        md.append(f"\n## Tela {i} · {titulo}\n")
        for l in linhas:
            md.append((l if l else "") + ("  " if l else ""))
open("/home/claude/out/guia/guia.md", "w").write("\n".join(md))
