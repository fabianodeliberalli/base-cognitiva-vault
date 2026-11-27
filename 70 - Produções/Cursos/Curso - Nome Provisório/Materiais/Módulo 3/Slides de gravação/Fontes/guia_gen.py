import sys, glob, os
from pptx import Presentation
src, out, title, subtitle, ordem_json = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
import json
tempo = json.loads(ordem_json)
intro = open('/home/claude/build_m2v/guia_intro.md').read().split('\n---\n',1)[1]
intro = intro.split('**O que mudou em relação')[0]
md = [f'---\ntitle: "{title}"\nsubtitle: "{subtitle}"\n---\n', intro]
files = sorted(glob.glob(f"{src}/*.pptx"), key=lambda f: [i for i,k in enumerate(tempo) if k in f][0])
for f in files:
    k = [k for k in tempo if k in f][0]
    nome = os.path.basename(f)[:-5].replace("TSH · ", "")
    p = Presentation(f)
    md.append(f"\n# {nome}\n\nEstimativa: {tempo[k]}. {len(p.slides)} telas.\n")
    for i, s in enumerate(p.slides, 1):
        titulo = ""
        for sh in s.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip() and sh.text_frame.text.strip() != "TRADUZINDO O SER HUMANO":
                titulo = sh.text_frame.text.strip().split("\n")[0]; break
        md.append(f"\n## Tela {i} · {titulo}\n")
        for l in s.notes_slide.notes_text_frame.text.split("\n"):
            md.append((l + "  ") if l else "")
open(out, "w").write("\n".join(md))
print(out)
