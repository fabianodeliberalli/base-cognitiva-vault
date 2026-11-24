from pathlib import Path
import json,re
from copy import deepcopy
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

R=Path(__file__).resolve().parent;OUT=R/'entrega';OUT.mkdir(exist_ok=True)
spec=json.loads((R/'m22_v2.json').read_text())

def setup(d,size=11.5):
 s=d.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7)
 s.top_margin=Cm(1.65);s.bottom_margin=Cm(1.5);s.left_margin=Cm(1.9);s.right_margin=Cm(1.9)
 for name in ['Normal','Body Text']:
  st=d.styles[name];st.font.name='Inter';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string('082A45');st.paragraph_format.line_spacing=1.12;st.paragraph_format.space_after=Pt(3)
 for name,sz in [('Title',26),('Heading 1',22),('Heading 2',19),('Heading 3',13)]:
  st=d.styles[name];st.font.name='EB Garamond';st.font.size=Pt(sz);st.font.color.rgb=RGBColor.from_string('173F52');st.paragraph_format.space_before=Pt(12);st.paragraph_format.space_after=Pt(8);st.paragraph_format.keep_with_next=True
 for st in d.styles:
  if st.type==1 and st.font.name:
   fonts=st.element.get_or_add_rPr().rFonts
   if fonts is not None:
    for a in list(fonts.attrib):
     if 'theme' in a.lower():del fonts.attrib[a]
    for a in ['ascii','hAnsi','eastAsia','cs']:fonts.set(qn('w:'+a),st.font.name)
  for node in list(st.element.xpath('.//w:pBdr')):node.getparent().remove(node)
 d.core_properties.author='Fabiano Deliberalli'

d=Document();setup(d)
d.core_properties.title='M2.2 — Prática guiada e integração'
foot=d.sections[0].footer.paragraphs[0];rr=foot.add_run('TRADUZINDO O SER HUMANO · M2.2 · ');rr.font.name='Inter';rr.font.size=Pt(8)
f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'PAGE');foot._p.append(f)
for start in range(0,12,2):
 if start:d.add_page_break()
 else:
  d.add_paragraph('M2.2 · Prática guiada e integração','Title')
  p=d.add_paragraph('O que cada pergunta destaca?');p.paragraph_format.space_after=Pt(12)
 for s in spec['slides'][start:start+2]:
  d.add_paragraph(f"Slide {s['number']} · {s['title']}",'Heading 2')
  # Os avisos de momento fazem parte das notas, sem uma segunda camada de bastidores.
  for line in s['notes'].splitlines():
   p=d.add_paragraph(line)
   if not line:p.paragraph_format.line_spacing=.25;p.paragraph_format.space_after=Pt(4)
   elif line=='PAUSA' or (line.isupper() and len(line)<40):
    for rr in p.runs:rr.bold=True;rr.font.color.rgb=RGBColor.from_string('8B6236');rr.font.size=Pt(9)
 d.add_paragraph().paragraph_format.space_after=Pt(0)
d.save(OUT/'TSH_M2_2_Prática_Guia_v2.docx')

# O apoio atual é a origem: preserva marca, texto conceitual, relações, fontes e tabela.
p=next((R/'origem/apoio').glob('*.docx'));d=Document(p)
def before(anchor,text,style=None):
 node=OxmlElement('w:p');anchor._p.addprevious(node);p=Paragraph(node,anchor._parent)
 if style:p.style=style
 p.add_run(text);return p

anchor=next(p for p in d.paragraphs if p.text=='Os dois tempos da Tradução')
before(anchor,'O organismo também antecipa o que pode acontecer para se preparar, aprender habilidades e responder ao conhecido. Essa capacidade participa da sobrevivência. A investigação pergunta como as antecipações acompanham a situação presente e o que deixam menos visível. Atualizar uma leitura inclui reconhecer previsões úteis e condições reais de vida.')

start=next(p for p in d.paragraphs if p.text=='Exploração de uma questão significativa')
end=next(p for p in d.paragraphs if p.text=='Elaborar na Cartografia')
node=start._p
while node is not end._p:
 nxt=node.getnext();node.getparent().remove(node);node=nxt
practice=[
 ('Prática: o que cada pergunta destaca?','Heading 1'),
 ('A prática acompanha uma mesma situação para reconhecer como as perguntas participam do que ganha importância e da maneira de vivê-la. São três observações: Antes das perguntas, Resolver e Possibilidade. O registro pode ser breve, por palavras, desenho ou descrição de um gesto. Se surgir uma imagem ou sensação, procure conservar algo que permita reencontrar sua qualidade. Uma palavra pode ajudar, e o retorno ao vivido permite conferir o que ela alcança.',None),
 ('Um exemplo antes de começar','Heading 2'),
 ('Imagine um convite para dançar. Antes das perguntas, uma pessoa pode reconhecer vontade de ir e um gesto de se recolher. Ao perguntar o que precisa resolver, pode perceber o horário disponível e uma tensão ao pensar em se expor. Ao perguntar que possibilidade de vida procura expressão, pode reconhecer o prazer de se mover e o mesmo receio de exposição. A comparação inclui o que se destacou e como isso foi vivido. São possibilidades desse exemplo, não resultados que você precisa reproduzir.',None),
 ('Preparação','Heading 2'),
 ('Reserve um momento em que possa parar e dedicar atenção à exploração. Não pratique dirigindo. Você pode adaptar ou interromper quando precisar e manter os registros privados. Se algo ficar intenso demais para acompanhar agora, deixe a situação de lado, reconheça o ambiente e os apoios do corpo e retome a atividade. Experiências desestabilizadoras podem pedir outro momento e acompanhamento.',None),
 ('Escolha uma situação da aula anterior ou algo que queira acompanhar: uma relação, uma criação, uma direção importante. Situe brevemente o que está acontecendo. Conserve a mesma situação durante a prática e dê tempo para cada observação; no vídeo, pause nos momentos indicados e retome depois de realizar o passo.',None),
 ('1. Antes das perguntas','Heading 2'),
 ('Traga a situação à atenção. Como é estar diante dela agora? Acompanhe o que aparece antes de procurar uma explicação. Pode chegar uma sensação, um afeto, uma imagem, uma palavra ou um impulso de movimento. Guarde uma expressão breve dessa experiência com o nome Antes das perguntas. Se usar uma palavra, confira se corresponde ao que percebe. Você não precisa preencher todas as modalidades.',None),
 ('2. Resolver','Heading 2'),
 ('Com a mesma situação, pergunte: “O que eu preciso resolver aqui?”. Dê tempo para perceber o que essa pergunta traz. Além da resposta em palavras, acompanhe como é estar diante da situação agora. Guarde uma expressão breve com o nome Resolver.',None),
 ('3. Possibilidade','Heading 2'),
 ('Volte à mesma situação com a pergunta: “Que possibilidade de vida procura expressão aqui?”. Permaneça um pouco com essa pergunta e acompanhe como se sente e se dispõe. Pode surgir algo diferente, continuar parecido ou ainda ficar sem resposta. Guarde uma expressão breve com o nome Possibilidade.',None),
 ('4. Comparar','Heading 2'),
 ('Retome as três observações. Compare o que ganhou destaque e como você viveu cada aproximação. Reconheça diferenças e permanências no que efetivamente apareceu. As perguntas podem iluminar aspectos distintos ou conduzir à mesma necessidade. Possibilidade não recebe um estatuto de resposta mais verdadeira, profunda ou positiva. Uma solução prática pode ser justamente o que permite cuidar de algo significativo.',None),
 ('5. Conferir a situação concreta','Heading 2'),
 ('Deixe as perguntas em segundo plano. O que mais precisa entrar nessa compreensão? Considere o que você vive e também as pessoas, os acordos e as condições envolvidas. Pode aparecer um acréscimo ou uma pergunta que precisa de informação real. Conserve isso, se for útil. Não é necessário produzir uma quarta síntese para concluir a prática.',None),
 ('6. Encerrar','Heading 2'),
 ('Deixe a situação de lado. Reconheça o ambiente e os apoios do corpo e retome os movimentos. A exploração termina aqui. Depois, com a atenção novamente disponível ao ambiente, elabore o que foi possível reconhecer e pense na continuidade.',None),
 ('O que estamos aprendendo','Heading 2'),
 ('Os dois tempos da Tradução operam na relação entre uma forma vivida e sua elaboração. A pergunta pode ajudar algo a encontrar expressão e também orientar o que passa despercebido. Voltar ao vivido permite conferir a palavra ou a imagem e ajustar a compreensão. Na metáfora do artesão, dar forma permite perceber diferenças e orientar o próximo gesto. Na experiência pessoal, a correspondência se constrói pelo que você reconhece e pelo encontro com a situação.',None),
 ('A composição educacional do TSH dialoga com o envolvimento e a reflexão, a contribuição de Bion para pensar a experiência emocional e a atenção de Naranjo à intenção, ao esforço e à atitude durante a prática. Ela desenvolve essas interlocuções em uma exploração própria. O exemplo oferece apoio para compreender o procedimento e termina antes da experiência pessoal.',None),
]
for txt,st in practice:before(end,txt,st)

anchor=next(p for p in d.paragraphs if p.text=='Continuidade')
before(anchor,'Uma próxima ação com retorno','Heading 2')
before(anchor,'Escolha uma ação pequena que use algo do que reconheceu e defina uma ocasião próxima para realizá-la. Se houver algo a conferir numa conversa, formule a pergunta, escolha com quem e quando poderá conversar e deixe espaço para uma resposta que modifique sua leitura. Se uma criação pedir desenvolvimento, reserve uma ocasião para experimentar um primeiro gesto, traço ou som. O propósito é produzir experiência com a qual continuar aprendendo.')
before(anchor,'Depois dessa ação, retome a Cartografia: o que conseguiu fazer, o que aconteceu em você e como a situação respondeu? O retorno pode mostrar uma capacidade disponível, uma aprendizagem que precisa de mais prática ou uma condição externa a alterar. Uma intenção que não chegou a ser realizada também oferece informação sobre o que faltou. Definir a ação, realizá-la e voltar ao resultado torna a continuidade acompanhável.')
before(anchor,'Uma possibilidade da Essência pode ganhar reconhecimento e começar a encontrar expressão por esse trabalho. Seu desenvolvimento envolve a singularidade concreta: corpo, afetos, imagens, relações, condições de vida e sentido. Uma boa formulação permite continuar esse percurso, sem funcionar como garantia de transformação.')

# A Cartografia continua a mesma. As três observações pertencem à Manifestação.
t=d.tables[0]
new=['Que situação ou possibilidade foi investigada e em qual contexto?',
 'O que reconheci Antes das perguntas, em Resolver e em Possibilidade? O que mudou e o que permaneceu?',
 'O que compreendo agora, em que isso se apoia e o que ainda precisa ser conferido?',
 'Qual ação vou realizar, em qual ocasião e quando voltarei para reconhecer o que ela mostrou?']
for row,txt in zip(t.rows[1:],new):row.cells[1].text=txt
d.core_properties.title='Por que alguns sinais ganham mais importância?'
for p in d.paragraphs:
 if p.text.startswith('SEELEY, W. W.'):
  p.text='SEELEY, W. W. et al. Dissociable intrinsic connectivity networks for salience processing and executive control. Journal of Neuroscience, 27, 2349–2356, 2007. DOI: 10.1523/JNEUROSCI.5587-06.2007. Investigação de redes de conectividade que contribui para diferenciar o destaque de sinais e o trabalho de controle. Texto: https://pmc.ncbi.nlm.nih.gov/articles/PMC2680293/'
 if p.text.startswith('BAGBY, R. M.'):
  p.text='BAGBY, R. M.; PARKER, J. D. A.; TAYLOR, G. J. Twenty-five years with the 20-item Toronto Alexithymia Scale. Journal of Psychosomatic Research, 131, 109940, 2020. DOI: 10.1016/j.jpsychores.2020.109940. Revisão dos autores da escala, para aprofundar o conceito de alexitimia. Registro: https://pubmed.ncbi.nlm.nih.gov/32007790/'
 if p.text.startswith('MCCONNELL, B. L.'):
  p.text='MCCONNELL, B. L. et al. Protection from latent inhibition provided by a conditioned inhibitor. Journal of Experimental Psychology: Animal Behavior Processes, 35, 498–508, 2009. DOI: 10.1037/a0014627. Experimentos em ratos sobre inibição latente. A prática educacional desta aula não avalia esse efeito. Texto: https://pmc.ncbi.nlm.nih.gov/articles/PMC2765660/'
for p in d.paragraphs:
 if p.text and p.style.name=='Normal':
  p.paragraph_format.keep_together=True
  p.paragraph_format.widow_control=True
 if p.text=='Elaborar na Cartografia':p.paragraph_format.page_break_before=True
d.save(OUT/'TSH_M2_2_Apoio_do_Aluno_v2.docx')

# Texto pesquisável preservado para resgate por outras IAs.
from docx.table import Table
from docx.oxml.ns import qn
md=[]
for node in d.element.body:
 if node.tag==qn('w:p'):
  p=Paragraph(node,d);txt=p.text
  if not txt:continue
  sty=p.style.name
  prefix='# ' if sty=='Title' else '## ' if sty=='Heading 1' else '### ' if sty=='Heading 2' else ''
  md += [prefix+txt,'']
 elif node.tag==qn('w:tbl'):
  t=Table(node,d)
  for i,row in enumerate(t.rows):
   md.append('| '+' | '.join(c.text.replace('\n',' ') for c in row.cells)+' |')
   if i==0:md.append('| --- | --- |')
  md.append('')
(R/'M2.2 - Apoio do aluno v2.md').write_text('\n'.join(md))

readme='''# Primeiro conjunto de gravação: M2.2, prática guiada

Grave esta prática completa como a segunda parte da aula M2.2.
A parte teórica já editada, de 28min13s, continua sendo a primeira parte.

1. Abra a apresentação editável pelo link abaixo e use suas notas no modo de apresentação, ou acompanhe o guia Word/PDF.
2. A tela 2 é uma demonstração. A experiência pessoal começa na tela 3.
3. As três observações são Antes das perguntas, Resolver e Possibilidade.
4. Nos pontos de pausa, dê tempo para a experiência e mantenha clara a orientação de pausar e retomar o vídeo.
5. A exploração termina na tela 9. As telas 10–12 elaboram e orientam a continuidade.

Apresentação editável com notas: https://chatgpt.com/space/page_b4a2a7c376008191b2e89f8f7d1119b3
Você pode exportá-la como PowerPoint pela apresentação.

O PDF dos slides permite apresentar o material sem editar.
O guia corresponde às notas da apresentação, com uma frase por linha.
O apoio do aluno reúne os fundamentos da aula e a prática atualizada, para acompanhar as duas partes na mesma aula da Hotmart.

## Ordem de produção combinada

M2.2 prática; M2.3 prática; ajustes localizados de M2.1; M2.4 em duas partes; M2.5; M2.6; prática de M1.6; demais ajustes localizados de M0/M1; M3 em diante.

Este conjunto contém M2.2. As demais posições conservam seus materiais e estados próprios até sua produção nessa ordem.
'''
(OUT/'00_Leia_para_gravar_M2_2.md').write_text(readme)
print('Guia e apoio produzidos; teoria do apoio preservada.')
