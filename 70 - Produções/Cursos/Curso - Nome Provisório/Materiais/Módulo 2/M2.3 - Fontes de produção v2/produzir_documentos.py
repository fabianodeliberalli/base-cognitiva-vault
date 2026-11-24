from pathlib import Path
import json
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

R=Path(__file__).resolve().parent;O=R/'entrega';O.mkdir(exist_ok=True)
spec=json.loads((R/'m23_v2.json').read_text())
# Mesma composição de consulta, já conferida em M2.2.
exec((R/'setup_documentos.py').read_text())
d=Document();setup(d)
d.core_properties.title='M2.3 — Prática guiada e integração'
foot=d.sections[0].footer.paragraphs[0];r=foot.add_run('TRADUZINDO O SER HUMANO · M2.3 · ');r.font.name='Inter';r.font.size=Pt(8)
f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'PAGE');foot._p.append(f)
for start in range(0,len(spec['slides']),2):
 if start:d.add_page_break()
 else:
  d.add_paragraph('M2.3 · Prática guiada e integração','Title')
  p=d.add_paragraph('Conferir uma certeza e recuperar outras pistas');p.paragraph_format.space_after=Pt(12)
 for s in spec['slides'][start:start+2]:
  d.add_paragraph(f"Slide {s['number']} · {s['title']}",'Heading 2')
  for line in s['notes'].splitlines():
   p=d.add_paragraph(line)
   if not line:p.paragraph_format.line_spacing=.25;p.paragraph_format.space_after=Pt(4)
   elif line=='PAUSA' or (line.isupper() and len(line)<40):
    for r in p.runs:r.bold=True;r.font.color.rgb=RGBColor.from_string('8B6236');r.font.size=Pt(9)
d.save(O/'TSH_M2_3_Pratica_Guia_v2.docx')

d=Document(next((R/'origem/apoio').glob('*.docx')))
def before(anchor,txt,style=None):
 node=OxmlElement('w:p');anchor._p.addprevious(node);p=Paragraph(node,anchor._parent)
 if style:p.style=style
 p.add_run(txt);return p

start=next(p for p in d.paragraphs if p.text=='Exploração: conferir a leitura e acompanhar o vivido')
nextheading=next(p for p in d.paragraphs if p.text=='Clareza, acesso e expressão na vida')
node=start._p.getnext();image_anchor=None
while node is not nextheading._p:
 if node.xpath('.//w:drawing'):
  image_anchor=Paragraph(node,start._parent);break
 node=node.getnext()
assert image_anchor is not None,'Preservar a figura comparativa do apoio.'
node=start._p
while node is not image_anchor._p:
 nxt=node.getnext();node.getparent().remove(node);node=nxt

practice=[
 ('Prática: conferir uma certeza e recuperar outras pistas','Heading 1'),
 ('O trabalho conserva duas comparações: Conclusão antes e Conclusão depois; Vivido antes e Vivido depois. O acontecimento e a situação escolhida continuam sendo os mesmos. O registro da conclusão reúne o que você entende e suas bases; o registro do vivido permite reencontrar como é estar diante dessa situação. Você pode organizar tudo na mesma Cartografia ou num caderno, sem preencher outra ficha.',None),
 ('Um exemplo para compreender o procedimento','Heading 2'),
 ('Uma pessoa apresenta uma proposta de trabalho e ouve: “Precisamos conversar melhor sobre isso”. Ela pode concluir “minha proposta foi rejeitada” e reconhecer aperto, com vontade de guardar a proposta. O aperto e o impulso pertencem ao vivido; a rejeição é a conclusão que precisa ser conferida também no encontro e na relação. Os registros permitem perceber o que muda em cada dimensão.',None),
 ('“Por que você rejeitou minha proposta?” já inclui a rejeição como fato. “Sobre quais pontos da proposta você quer conversar?” permite descobrir o que o outro tem a dizer. A resposta pode confirmar uma preocupação, modificar a leitura ou mostrar que algo permanece indefinido. Essa demonstração se encerra antes da sua exploração. Durante a realização, mantenha a própria situação como referência.',None),
 ('Preparação','Heading 2'),
 ('Reserve um momento em que possa dedicar atenção à prática e fazer registros breves. Se estiver dirigindo, faça depois. Você pode manter os olhos abertos, adaptar, interromper e guardar os registros só para você. Escolha algo significativo que consiga acompanhar agora. Ao interromper ou concluir, deixe a situação de lado, reconheça o ambiente e os apoios do corpo e retome os movimentos.',None),
 ('1. Situação e conclusão de antes','Heading 2'),
 ('Escolha uma situação em que uma conclusão ficou bastante firme. Registre o que aconteceu e quem participava. Conserve a mesma situação durante toda a prática. Complete “Diante disso, concluí que...” com a leitura que você realmente vem sustentando e identifique como Conclusão antes. No vídeo, pause para realizar cada passo e retome depois de concluí-lo.',None),
 ('2. Vivido de antes','Heading 2'),
 ('Ao trazer a situação à atenção, como é estar diante dela? Acompanhe o que aparece no corpo, no afeto, nas imagens ou no impulso de agir, conforme conseguir reconhecer. Encontre uma expressão breve, por palavra, desenho ou descrição de um gesto, e identifique como Vivido antes. Guarde junto da conclusão, mantendo os dois registros reconhecíveis.',None),
 ('3. Bases e o que seria difícil rever','Heading 2'),
 ('Retome Conclusão antes. Que pistas do acontecimento sustentam essa leitura? Diferencie o que observou do que associou ou imaginou e anote o que ainda não tem como conferir. Em seguida, acompanhe: se essa conclusão precisasse ser revista, o que isso colocaria em jogo? Pode haver algo importante que procura cuidado ou preservação. Reconheça o que precisa de cuidado e o que pode pedir revisão. Conserve essas observações junto da conclusão.',None),
 ('4. Retomar o presente','Heading 2'),
 ('Deixe a situação de lado por um momento. Olhe para o lugar onde está e reconheça um detalhe do ambiente. Perceba o apoio dos pés ou do assento, conforme sua posição. Ajuste a postura se ajudar e deixe a respiração acontecer. Permaneça um pouco nesse contato. O critério para seguir é reconhecer onde está e ter alguma disponibilidade para considerar a questão; pode continuar havendo tensão. Se ainda não houver disponibilidade, conclua por hoje retomando o ambiente e seus movimentos.',None),
 ('5. Uma informação que permita conferir','Heading 2'),
 ('Conservando algum contato com o ambiente, retome a mesma situação. O que você precisaria saber para conferir sua conclusão? Formule uma pergunta que permita descobrir essa informação e aceite uma resposta diferente da esperada. Se puder consultá-la agora, confira e conserve o que encontrou. Se depender de uma conversa ou de outra ocasião, guarde a pergunta e como pretende buscar a resposta. A informação ainda não obtida permanece em aberto; uma resposta imaginada não ocupa esse lugar.',None),
 ('6. Conclusão depois','Heading 2'),
 ('Volte a Conclusão antes. Com o que foi possível conferir, o que consegue concluir agora? Registre como Conclusão depois, incluindo as bases e o que ainda precisa conhecer. Compare as duas conclusões. A leitura pode mudar, continuar sustentada ou permanecer em aberto.',None),
 ('7. Vivido depois','Heading 2'),
 ('Retome Vivido antes e volte à mesma situação. Como é estar diante dela neste momento? Encontre uma expressão breve e registre como Vivido depois. Compare os dois registros do vivido: o que mudou e o que permaneceu? Essa comparação é separada da comparação entre as conclusões.',None),
 ('8. Encerrar e elaborar','Heading 2'),
 ('Deixe a situação e os registros de lado. Reconheça o ambiente e os apoios do corpo e retome seus movimentos. A exploração termina aqui. Depois, elabore o que foi possível reconhecer. Uma conclusão revista pode coexistir com o mesmo aperto; uma experiência diferente pode coexistir com uma interpretação que ainda precisa de conferência. A figura a seguir permite retomar as duas dimensões.',None)
]
for txt,st in practice:before(image_anchor,txt,st)

# Atualizar a figura comparativa preservando posição, dimensão e o primeiro diagrama.
comparative=d.inline_shapes[-1]
rid=comparative._inline.graphic.graphicData.pic.blipFill.blip.embed
d.part.related_parts[rid]._blob=(R/'comparacoes_v2.png').read_bytes()

last=next(p for p in d.paragraphs if p.text.startswith('Conserve o registro inicial. Depois de buscar'))
before(last,'Conferência no encontro real','Heading 2')
before(last,'Se a pergunta ainda depende de outra ocasião, defina uma fonte e um momento possível para conferi-la. Pode ser consultar um acordo ou conversar com quem participa. Se for conversar, retome antes algum contato com o ambiente e os apoios, faça a pergunta preparada e escute a resposta real. Se ficar dúvida, devolva em poucas palavras o que entendeu e pergunte se corresponde ao que a pessoa quis dizer. A resposta tem lugar para modificar seu entendimento.')
last.text='Conserve os registros iniciais. Depois dessa conferência, volte à Cartografia: o que soube, o que continua supondo e como viveu o encontro? Compare o que passou a compreender e o que conseguiu fazer. Pode haver a aquisição de sustentar uma pergunta, aceitar surpresa ou continuar presente numa conversa; pode permanecer a necessidade de outro recurso ou de uma capacidade a desenvolver. A continuidade acompanha essas diferenças no encontro com a vida.'
t=d.tables[0]
values=['O acontecimento, quem participa e o contexto.',
 'Vivido antes e Vivido depois, com suas formas, diferenças e permanências.',
 'Conclusão antes e Conclusão depois, suas bases, informação obtida e o que falta conferir.',
 'Pergunta a conferir, fonte ou pessoa, ocasião possível e retorno ao que a experiência mostrar.']
for row,val in zip(t.rows[1:],values):row.cells[1].text=val

ref=next(p for p in d.paragraphs if p.text=='Para investigar mais')
d.add_paragraph('Naranjo, C. Entre meditação e psicoterapia. As discussões sobre escuta, projeção e interpretações como hipóteses, recuperadas no acervo do TSH nas pp. 190–202, contribuem para permitir que a outra pessoa confirme ou corrija o entendimento. A condução desta aula constitui uma adaptação educacional do TSH.')
d.add_paragraph('Rossi, E.; Erickson-Klein, R.; Rossi, K. Novel activity-dependent approaches to therapeutic hypnosis and psychotherapy: the general waking trance. American Journal of Clinical Hypnosis, 51(2), 185–200, 2008. DOI: https://doi.org/10.1080/00029157.2008.10401664. Discussão clínica sobre o transe na vigília, em diálogo com atenção e disponibilidade de referências. Resumo: https://pubmed.ncbi.nlm.nih.gov/18998388/.')
# Remover quebras vazias herdadas da versão anterior; as seções recebem quebra própria.
for p in list(d.paragraphs):
 if not p.text and p._p.xpath('.//w:br[@w:type="page"]'):
  p._p.getparent().remove(p._p)
for p in d.paragraphs:
 if p.text and p.style.name=='Normal':p.paragraph_format.keep_together=True;p.paragraph_format.widow_control=True
 if p.text in ['Cartografia e continuidade','Para investigar mais']:p.paragraph_format.page_break_before=True
d.core_properties.author='Fabiano Deliberalli';d.core_properties.title='Interpretações e certezas: recuperar outras pistas'
d.save(O/'TSH_M2_3_Apoio_do_Aluno_v2.docx')

# Preservar a posição das figuras no texto pesquisável para outras IAs.
md=[];image_count=0
figs=['Imagens M2.3/M2.3 - Forma vivida e elaboração v0.2.png','Imagens M2.3/M2.3 - Duas comparações v2.png']
for node in d.element.body:
 if node.tag==qn('w:p'):
  p=Paragraph(node,d)
  if node.xpath('.//w:drawing'):
   if image_count>0:md += ['![Diagrama da aula](<'+figs[image_count-1]+'>)','']
   image_count+=1
  txt=p.text
  if not txt:continue
  sty=p.style.name;prefix='# ' if sty=='Title' else '## ' if sty=='Heading 1' else '### ' if sty=='Heading 2' else ''
  md += [prefix+txt,'']
 elif node.tag==qn('w:tbl'):
  t=Table(node,d)
  for i,row in enumerate(t.rows):
   md.append('| '+' | '.join(c.text.replace('\n',' ') for c in row.cells)+' |')
   if i==0:md.append('| --- | --- |')
  md.append('')
(R/'M2.3 - Apoio do aluno v2.md').write_text('\n'.join(md))
(O/'00_Leia_para_gravar_M2_3.md').write_text('''# M2.3 — Prática guiada e integração

Grave esta prática completa como a segunda parte da mesma aula M2.3.
A teoria já editada, de 24min55s, continua como primeira parte.

Apresentação editável com notas: https://chatgpt.com/space/page_85cb82566f6c8191a65ca24c77508761
Você pode exportá-la como PowerPoint pela apresentação.

1. Telas 1–2: propósito, mapa e preparação.
2. Telas 3–4: demonstração. O exemplo termina antes da situação pessoal.
3. Tela 5: início da realização com a situação escolhida.
4. Telas 6–13: registros, conferência, contato com o presente e comparações separadas.
5. Tela 14: encerramento da exploração.
6. Telas 15–17: elaboração, conferência no encontro real e Cartografia.

As referências são Conclusão antes, Vivido antes, Conclusão depois e Vivido depois.
Mantenha a mesma situação durante toda a realização.
Nos pontos de pausa, dê tempo para a experiência e deixe clara a orientação de pausar o vídeo e retomar depois de realizar o passo.

O PDF dos slides permite apresentar sem editar.
O guia Word/PDF corresponde às notas da apresentação, com uma frase por linha.
O apoio Word/PDF conserva os fundamentos e as figuras e reúne a prática atualizada para o aluno acompanhar as duas partes.

A próxima posição da ordem de produção é a lapidação localizada de M2.1, preservando a gravação aproveitável; depois M2.4 em duas partes.
''')
print('Guia e apoio compostos; três imagens do apoio preservadas, incluindo a marca.')
