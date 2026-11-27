import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NOT = RGBColor(0x08, 0x2A, 0x45); OURO = RGBColor(0xC9, 0x9A, 0x64); MUTED = RGBColor(0x5A, 0x6B, 0x74)

def base(doc):
    for s in doc.styles:
        try:
            if s.font is not None: s.font.name = 'Calibri'
        except Exception: pass
    doc.styles['Normal'].font.size = Pt(11)
    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = Cm(2); sec.left_margin = sec.right_margin = Cm(2.2)

def h(doc, text, size=18, color=NOT, before=0, after=6):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = color
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    return p

def par(doc, text, size=11, italic=False, color=None, after=4):
    p = doc.add_paragraph(); r = p.add_run(text); r.font.size = Pt(size); r.italic = italic
    if color: r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(after); return p

def campo(doc, rotulo, linhas=2):
    t = doc.add_table(rows=1, cols=1); t.style = 'Table Grid'
    c = t.rows[0].cells[0]; c.paragraphs[0].add_run(rotulo).bold = True
    for _ in range(linhas): c.add_paragraph('')
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def checks(doc, n=14):
    t = doc.add_table(rows=2, cols=7); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i in range(n):
        c = t.rows[i // 7].cells[i % 7]; c.paragraphs[0].add_run(f'dia {i+1}  ☐').font.size = Pt(9)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def quebra(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def progresso(doc, momento):
    h(doc, f'Pergunta de progresso — {momento}', 13, OURO, 6, 4)
    par(doc, 'Pense numa situação recente em que um padrão seu foi ativado.')
    par(doc, '1. Quanto do que você já sabe sobre si ficou disponível naquele momento?')
    t = doc.add_table(rows=1, cols=11); t.style = 'Table Grid'
    for i in range(11): t.rows[0].cells[i].paragraphs[0].add_run(str(i)).font.size = Pt(10)
    par(doc, '0 = nada · 10 = o que eu precisava', 9, True, MUTED)
    par(doc, '2. Quanto tempo você levou para perceber e voltar?   ☐ dias   ☐ horas   ☐ minutos   ☐ no próprio momento')
    campo(doc, '3. O que ajudou ou dificultou?', 2)

VERSOES = {
 2: ('Percepção e tradução da experiência', 'A forma básica: árvore, a pergunta «o que está me vivendo agora?» e três respirações no baixo ventre.'),
 3: ('Corpo, vitalidade e práticas de cultivo', 'Acrescente: na árvore, respire passando pelos três centros (baixo ventre, peito, testa); se quiser, Sustentar o Céu três vezes; escolha o recurso de retorno do dia.'),
 4: ('Emoções, padrões de proteção e novas respostas', 'Acrescente: a linha do Hara para a intenção do dia (aula 4.6) e dê nome à emoção do momento, conferindo no corpo.'),
 5: ('Valores, criação e espiritualidade', 'Acrescente: um minuto de quietude e a pergunta «o que o Amor, o Poder e a Sabedoria pedem hoje?».'),
 6: ('Integração da experiência e práticas de cultivo', 'No lugar da intenção: a pequena circulação (aula 6.3) ou o Chong Mai (aula 6.6), como aprendido no módulo.'),
 7: ('Comunicação, vínculos, limites e reparação', 'Antes de uma conversa importante: a linha do Hara e, se quiser, o ensaio da nova resposta em auto-hipnose.'),
 8: ('Aprendizagens, autonomia e continuidade', 'Monte a sua versão com o que funcionou e anote-a aqui; projete-a, em auto-hipnose, nas situações que virão.'),
}

ORIGEM = {2: 'Zhan Zhuang (abertura do Módulo 2)', 3: 'Três Tan Tien (3.5 e 3.6), Qi Gong (3.7), retorno (3.8)', 4: 'Linha do Hara (4.6)', 5: 'Quietude (5.4) e valores (5.3)', 6: 'Pequena circulação (6.3) e Chong Mai (6.6)', 7: 'O Hara na relação (7.1 e 7.5)', 8: 'Repertório (8.2)'}

def caderno(path):
    doc = Document(); base(doc)
    p = h(doc, 'Caderno de Reencontros', 30, NOT, 120, 4)
    par(doc, 'Traduzindo o Ser Humano', 14, False, OURO, 30)
    par(doc, 'Fabiano Deliberalli', 11, False, MUTED, 40)
    campo(doc, 'Nome', 1); campo(doc, 'Comecei este caderno em', 1)
    quebra(doc)
    h(doc, 'Como usar este caderno', 16)
    for t in ['Todos os dias: faça o Cultivo do Eixo (três a cinco minutos) e marque o dia. Falhar um dia não desfaz nada; retome no seguinte.',
              'No momento real: quando perceber o seu primeiro sinal, faça o Retorno ao Eixo (trinta segundos).',
              'Uma vez por quinzena, antes do encontro ao vivo: registre um reencontro com o seu padrão (dez minutos). Traga o caderno ao encontro.',
              'Em M2, M4 e M8: responda à pergunta de progresso.',
              'A versão do Cultivo do Eixo de cada quinzena traz para o dia a dia a prática que o módulo acabou de ensinar: a árvore, os três centros, o Qi Gong, a linha do Hara, a quietude, a circulação.',
              'Escreva só o que quiser. Este caderno é seu e não precisa ser mostrado a ninguém.']:
        doc.add_paragraph(t, style='List Bullet')
    h(doc, 'Retorno ao Eixo, no momento real', 13, OURO, 8, 4)
    for t in ['Notar o primeiro sinal.', 'Sentir os pés: a raiz.', 'Três respirações no baixo ventre.', 'Perguntar: o que está ao meu alcance agora?']:
        doc.add_paragraph(t, style='List Number')
    quebra(doc)
    h(doc, 'Ponto de partida', 16)
    campo(doc, 'A minha pergunta inicial (da aula 0.1)', 3)
    campo(doc, 'O meu plano: «Quando eu perceber ________ (meu primeiro sinal), vou fazer o Retorno ao Eixo.»', 2)
    progresso(doc, 'início (abertura do Módulo 2)')
    for m in range(2, 9):
        quebra(doc)
        nome, versao = VERSOES[m]
        h(doc, f'Módulo {m} — {nome}', 16)
        h(doc, 'Cultivo do Eixo desta quinzena', 12, OURO, 2, 2)
        par(doc, versao)
        checks(doc)
        h(doc, 'Reencontro da quinzena', 12, OURO, 4, 2)
        campo(doc, 'O que aconteceu (a situação real)', 5)
        campo(doc, 'O primeiro sinal (no corpo, na emoção, no pensamento)', 3)
        campo(doc, 'O que eu fiz (fiz o Retorno ao Eixo? sim / não / em parte)', 3)
        campo(doc, 'O que estava ao meu alcance', 3)
        campo(doc, 'Uma frase de Tradução', 3)
        if m == 4:
            progresso(doc, 'meio do percurso (Módulo 4)')
        if m == 6:
            quebra(doc)
            h(doc, 'Comparar reencontros (aula 6.8)', 16)
            par(doc, 'Releia os reencontros dos módulos 2 a 6.')
            t = doc.add_table(rows=4, cols=3); t.style = 'Table Grid'
            for i, x in enumerate(['O que voltou', 'O que desta vez foi diferente', 'O que estava ao meu alcance']):
                t.rows[0].cells[i].paragraphs[0].add_run(x).bold = True
            doc.add_paragraph()
        if m == 8:
            progresso(doc, 'fim do percurso (Módulo 8)')
            quebra(doc)
            h(doc, 'Revisão do percurso (aula 8.1)', 16)
            campo(doc, 'A minha pergunta inicial, hoje', 3)
            campo(doc, 'O que já está disponível para mim', 2)
            campo(doc, 'O que ainda está em cultivo', 2)
            campo(doc, 'Compare as três respostas da pergunta de progresso: o que mudou?', 2)
            campo(doc, 'A minha versão do Cultivo do Eixo, para depois do curso', 2)
    doc.save(path)

def guia(path):
    doc = Document(); base(doc)
    sec = doc.sections[0]; sec.top_margin = sec.bottom_margin = Cm(1.4); sec.left_margin = sec.right_margin = Cm(1.8)
    doc.styles['Normal'].font.size = Pt(10.5)
    h(doc, 'Cultivo do Eixo', 24, NOT, 0, 2)
    par(doc, 'Traduzindo o Ser Humano · a prática diária do percurso · Fabiano Deliberalli', 10, True, OURO, 10)
    par(doc, '«Ou trabalhamos voluntariamente ou somos vividos pelos padrões que carregamos.» O Cultivo do Eixo é o trabalho voluntário de todos os dias, para que o eixo esteja disponível quando o padrão chegar.', 10.5, True, None, 2)
    par(doc, 'A base é a árvore que você conheceu na aula 1.3 e aprende pelo nome, Zhan Zhuang, na abertura do Módulo 2. A cada módulo, o Cultivo do Eixo acrescenta, em poucos minutos, a prática que a aula acabou de ensinar. A aula ensina, o Cultivo repete todos os dias da quinzena, e o encontro ao vivo pratica junto.', 10.5, False, None, 2)
    h(doc, 'Todos os dias (três a cinco minutos)', 13, OURO, 8, 4)
    for t in ['Enraizar: um a três minutos de árvore (Zhan Zhuang), em pé, sentado ou apoiado.',
              'Perceber: pergunte «o que está me vivendo agora?».',
              'Retornar: três respirações no baixo ventre e uma frase de intenção para o dia.']:
        doc.add_paragraph(t, style='List Number')
    h(doc, 'No momento real: Retorno ao Eixo (trinta segundos)', 13, OURO, 8, 4)
    for i, t in enumerate(['Notar o primeiro sinal.', 'Sentir os pés: a raiz.', 'Três respirações no baixo ventre.', 'Perguntar: o que está ao meu alcance agora?'], 1):
        q = par(doc, f'{i}. {t}'); q.paragraph_format.left_indent = Cm(0.6)
    par(doc, 'Escreva no Caderno de Reencontros: «Quando eu perceber ________, vou fazer o Retorno ao Eixo.»', 11)
    h(doc, 'Uma versão por módulo', 13, OURO, 8, 4)
    t = doc.add_table(rows=1, cols=3); t.style = 'Table Grid'
    for i, x in enumerate(['Módulo', 'Prática que o módulo ensina', 'O que a versão acrescenta']): t.rows[0].cells[i].paragraphs[0].add_run(x).bold = True
    for m in range(2, 9):
        r = t.add_row().cells; r[0].text = f'M{m}'; r[1].text = ORIGEM[m]; r[2].text = VERSOES[m][1]
    t.autofit = False
    for row in t.rows:
        for k, w in enumerate([Cm(1.6), Cm(5.6), Cm(10.2)]): row.cells[k].width = w
    for k, w in enumerate([Cm(1.6), Cm(5.6), Cm(10.2)]): t.columns[k].width = w
    grid = t._tbl.tblGrid
    for k, gc in enumerate(grid.findall(qn('w:gridCol'))): gc.set(qn('w:w'), str(int([1.6,5.6,10.2][k]*567)))
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for run in p.runs: run.font.size = Pt(9)
    h(doc, 'Cuidados', 13, OURO, 8, 4)
    par(doc, 'Pare se houver tontura, dor ou falta de ar. Não force a duração: um minuto por dia vale mais que dez minutos uma vez. Falhar um dia não desfaz nada; retome no dia seguinte. Em sofrimento intenso, procure ajuda profissional (CVV: 188, gratuito, 24 horas).')
    doc.save(path)

if __name__ == "__main__":
    caderno(sys.argv[1]); guia(sys.argv[2])
