from pathlib import Path
from copy import deepcopy
import json,zipfile
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt,RGBColor
R=Path(__file__).resolve().parent;OUT=R/'entrega';OUT.mkdir(exist_ok=True)
# Reutiliza a composição verificada do guia, sem gerar novamente o apoio anterior.
source=(R/'fontes/criar_documentos_v1.py').read_text()
functions=source[:source.index('# Guias do apresentador')]
namespace={'__file__':str(R/'atualizar_documentos.py')};exec(functions,namespace)
document,para,caption=namespace['document'],namespace['para'],namespace['caption']
for part in [1,2]:
 spec=json.loads((R/f'parte{part}_v2.json').read_text());d=document(11.5)
 for start in range(0,len(spec['slides']),2):
  if start:d.add_page_break()
  if start==0:caption(d,'TRADUZINDO O SER HUMANO');para(d,f'M2.4 · Parte {part}','Title');para(d,'Compreensão e fundamentos' if part==1 else 'Prática guiada e integração')
  for s in spec['slides'][start:start+2]:
   para(d,f"Slide {s['number']}  {s['title']}",'Heading 2');p=para(d,s['moment'].upper());p.paragraph_format.keep_with_next=True
   for rr in p.runs:rr.font.size=Pt(8);rr.bold=True;rr.font.color.rgb=RGBColor.from_string('245E78')
   for line in s['notes'].split('\n'):
    p=para(d,line);p.paragraph_format.space_after=Pt(2 if line else 4)
    if not line:p.paragraph_format.line_spacing=0.25
    if line=='PAUSA':
     for rr in p.runs:rr.bold=True;rr.font.color.rgb=RGBColor.from_string('A8743C')
 d.save(OUT/f'TSH_M2_4_Parte_{part}_Guia_de_gravacao_v2.docx')

d=Document(R/'origem/v1/TSH_M2_4_Apoio_do_Aluno_v1.docx')
new=[
('Como a experiência já chega organizada','Heading 1'),
('Ao receber um pedido, uma pessoa pode já se sentir em falta e preparar-se para concordar. Quando procura explicar essa resposta, encontra corpo, expectativa, imagem do outro e necessidade de aceitar que parecem fazer sentido juntos. As referências aprendidas participam da maneira como o encontro atual é vivido.',None),
('Cozolino usa a expressão “meio segundo vital” para descrever uma diferença aproximada de tempo entre processos rápidos e acesso consciente à experiência. Seu interesse, aqui, é mostrar como memória, corpo e emoções participam da formação do presente. Uma expectativa de perder o lugar pode orientar a percepção das intenções do outro. O tempo apresentado pelo autor não funciona como duração universal de toda percepção ou escolha.',None),
('Kahneman ajuda a investigar o aval dado às impressões e associações disponíveis. “Sinto culpa” e “descumpri um acordo” oferecem perguntas diferentes. A sensação pode orientar uma investigação; o que aconteceu precisa ser relacionado aos acordos e às condições do encontro. A elaboração pode conferir a impressão ou encontrar justificativas que a mantenham.',None),
('No diálogo com os dois tempos da Tradução, acompanhamos a forma vivida e sua elaboração sem tratá-las como dois compartimentos separados por um cronômetro. Posso sentir conscientemente um aperto e ainda não encontrar palavras para compreendê-lo. A contribuição de Bion ajuda a acompanhar esse trabalho de dar forma; o retorno à experiência permite conferir o que as palavras alcançam.',None),
('A aprendizagem também refina o que fica disponível antes de explicar cada movimento. Kahneman e Klein relacionam a intuição especializada às oportunidades de aprender regularidades e receber retorno sobre os resultados. Na competência incorporada e no retorno com aquisição do TSH, investigamos como uma compreensão trabalhada na experiência passa a participar da percepção e da resposta. A continuidade precisa acompanhar efeitos e condições reais.',None),
('Na prática desta aula, essa articulação dá sentido ao recurso e à comparação. Vamos observar a configuração conhecida, retomar outras referências, dar presença a uma qualidade pertinente e reencontrar o mesmo começo. O vivido e a participação são comparados separadamente para reconhecer o que ficou disponível e o que pede outro trabalho.',None)]
body=d.element.body;target=next(p for p in d.paragraphs if p.text=='Função, expressão e condições concretas')._p
items=[]
for text,style in new:
 p=d.add_paragraph(text,style);items.append(p._p)
p=d.add_paragraph();br=OxmlElement('w:br');br.set(qn('w:type'),'page');p.add_run()._r.append(br);items.append(p._p)
index=list(body).index(target)
for offset,item in enumerate(items):body.remove(item);body.insert(index+offset,item)
for p in d.paragraphs:
 if p.text.startswith('Aprendizagens podem aparecer como prontidão antes de uma explicação consciente.'):
  p.text='Aprendizagens podem aparecer como prontidão antes de uma explicação consciente. Isso sustenta capacidades e também respostas que hoje restringem possibilidades. A antecipação participa da habilidade, da adaptação e da continuidade. O trabalho de cultivo inclui distinguir a capacidade existente pouco acessível, a habilidade ainda por desenvolver e a condição externa que precisa mudar.'
 # A nota de aprofundamento é ligada à afirmação temporal, sem transportar essa discussão à condução.
 if p.text.startswith('A Tradução, a finalidade ligada à Essência e à singularidade'):
  p.text+=' A síntese temporal de Cozolino e os experimentos sobre consciência têm recortes e métodos próprios. O exercício da aula não mede esse intervalo.'
 # Acrescenta o texto primário junto à referência já existente.
 if p.text.startswith('Aprendizagem implícita e participação das relações na transformação.'):
  p.text+=' Trecho publicado pelo autor: https://www.drloucozolino.com/neuroscience/the-vital-half-second'
# Registro bibliográfico da revisão metodológica, sem criar novo requisito para o aluno.
p=d.add_paragraph('Guggisberg, A. G.; Mottaz, A. Timing and awareness of movement decisions: does consciousness really come too late? Frontiers in Human Neuroscience, 7, 385, 2013.')
for rr in p.runs:rr.bold=True;rr.font.size=Pt(10)
p=d.add_paragraph('Revisão dos marcadores e métodos usados para investigar o tempo de decisões e consciência. DOI: https://doi.org/10.3389/fnhum.2013.00385')
for rr in p.runs:rr.font.size=Pt(10)
d.save(OUT/'TSH_M2_4_Apoio_do_Aluno_v2.docx')
print('Guias e apoio atualizados')
