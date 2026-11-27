import subprocess, unicodedata, re, sys
sys.path.insert(0, '/home/claude/hot')
from dados import LINHA, MOD, AULAS, MINIMO
from docx import Document
from docx.shared import Pt

OUT = '/home/claude/hot/docs'
import os; os.makedirs(OUT, exist_ok=True)

def slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^A-Za-z0-9]+', '_', t).strip('_')
    return t[:60].rstrip('_')

def bloco(texto):
    return '\n'.join('> ' + l if l else '>' for l in texto.split('\n'))

for m, d in MOD.items():
    L = []
    L.append(f'---\ntitle: "{d["nome"]}"\nsubtitle: "O que cadastrar na Hotmart"\n---\n')
    L.append(f'![](/home/claude/hot/mapa_M{m}.png){{width=6.3in}}\n')
    L.append('**Liberação:** ' + d['lib'] + '. Encontro ao vivo do módulo: ' + d['enc'] + '.\n')
    L.append('O texto recuado é para copiar e colar como está. O resto são orientações de cadastro.\n')
    L.append('# 1. Nome do módulo\n')
    L.append(bloco(d['nome'].replace(' — ', ' - ')) + '\n')
    L.append('# 2. Descrição do módulo\n')
    desc = LINHA + '\\\nVocê está em: ' + d['pos'] + '\n\n' + '\n\n'.join(d['desc']) + '\n\n' + MINIMO[m]
    L.append('\n'.join('> ' + l if l else '>' for l in desc.split('\n')) + '\n')
    L.append('A imagem do mapa acima, com o Módulo ' + str(m) + ' destacado, está no pacote em PNG. Se a área de membros aceitar imagem de capa do módulo, ou imagem no corpo da primeira aula, ela pode ir junto.\n')
    L.append('# 3. Aulas, na ordem da plataforma\n')
    aulas = AULAS[m]
    for i, a in enumerate(aulas, 1):
        if m == 2:
            cod, tit, ds, origem, mat = a
        else:
            cod, tit0, ds = a
            tit = f'Aula {cod} - {tit0}'
            origem, mat = 'A gravar', ('Apoio do aluno de uma página (pronto, PDF)' if m == 3 else 'Apoio do aluno (a produzir)')
        pref = {'abertura': '2_0a', 'zhan': '2_0b'}.get(cod, cod.rstrip('p').replace('.', '_'))
        arq = 'TSH_M' + pref + '_' + slug(tit.split(' - ', 1)[-1]) + '.mp4'
        L.append(f'## {i}. {tit}\n')
        L.append('**Título**\n')
        L.append(bloco(tit) + '\n')
        L.append('**Descrição da aula**\n')
        L.append(bloco(ds) + '\n')
        L.append(f'- **Vídeo:** {origem}. Nome do arquivo sugerido: `{arq}`')
        L.append(f'- **Liberação:** com o módulo, {d["lib"].split(" (")[0].lower()}')
        L.append(f'- **Material complementar:** {mat}\n')
    L.append('# 4. Antes de publicar\n')
    chk = ['Nome e descrição do módulo colados.',
           f'{len(aulas)} itens cadastrados, na ordem acima, com título e descrição.',
           'Data de liberação programada em cada aula.',
           'Vídeos conferidos: som, início e fim, sem nomes nem imagens de participantes.',
           'Materiais complementares anexados nas aulas indicadas.']
    if m != 2:
        chk.append(f'Se houver corte do encontro de {d["enc"]} (abertura ou prática), ele entra antes da primeira aula, como no Módulo 2.')
    L += [f'- [ ] {c}' for c in chk]
    md = '\n'.join(L) + '\n'
    base = f'{OUT}/TSH - Hotmart - Módulo {m}'
    open(base + '.md', 'w').write(md)
    subprocess.run(['pandoc', base + '.md', '-o', base + '.docx'], check=True)
    doc = Document(base + '.docx')
    for s in doc.styles:
        try:
            if s.font is not None: s.font.name = 'Calibri'
        except Exception: pass
    doc.styles['Normal'].font.size = Pt(11)
    doc.save(base + '.docx')
    print(base)
