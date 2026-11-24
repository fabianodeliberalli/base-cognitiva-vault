from pathlib import Path
from shutil import copy2
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
import json
R=Path(__file__).resolve().parent;O=R/'entrega';O.mkdir(exist_ok=True)
exec((R.parent/'m23_producao_20261124/setup_documentos.py').read_text())
items=[('M22','01_M2_2_Pratica','M2.2 · Prática guiada'),('M23','02_M2_3_Pratica','M2.3 · Prática guiada'),('M24P2','04_M2_4_Pratica','M2.4 · Prática guiada')]
for key,folder,title in items:
 p=O/folder;p.mkdir(exist_ok=True);d=Document();setup(d)
 spec=json.loads((R/(key+'_v3.json')).read_text())
 d.core_properties.title=title+' — condução reorganizada'
 footer=d.sections[0].footer.paragraphs[0];rr=footer.add_run('TRADUZINDO O SER HUMANO · '+title+' · ');rr.font.name='Inter';rr.font.size=Pt(8)
 fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
 for start in range(0,len(spec['slides']),2):
  if start:d.add_page_break()
  else:d.add_paragraph(title,'Title')
  for s in spec['slides'][start:start+2]:
   d.add_paragraph(f"Slide {s['number']} · {s['title']}",'Heading 2')
   for line in s['notes'].splitlines():
    pp=d.add_paragraph(line)
    if not line:pp.paragraph_format.line_spacing=.25;pp.paragraph_format.space_after=Pt(4)
    elif line=='PAUSA' or(line.isupper() and len(line)<60):
     for rr in pp.runs:rr.bold=True;rr.font.color.rgb=RGBColor.from_string('8B6236');rr.font.size=Pt(9)
 d.save(p/(key+'_Guia_v3.docx'))
 # Trilha pesquisável idêntica às notas.
 md=['# '+title+' v3','']
 for s in spec['slides']:md+=['## '+str(s['number'])+'. '+s['title'],'','```text',s['notes'],'```','']
 (R/(key+'_Trilha_v3.md')).write_text('\n'.join(md))
# Teoria M2.4: preservar os suportes completos de 21 telas.
p=O/'03_M2_4_Teoria';p.mkdir(exist_ok=True)
old=R.parent/'profundidade_tsh_20261123/entrega'
for suffix in ['docx','pdf']:copy2(old/('TSH_M2_4_Parte_1_Guia_de_gravacao_v2.'+suffix),p/('M24P1_Guia_v2.'+suffix))
# Apoios M2.2/M2.3: os conteúdos e registros não mudaram.
a=O/'Apoios_do_aluno';a.mkdir(exist_ok=True)
for key,folder,nm in [('M22','producao_20261124','TSH_M2_2_Apoio_do_Aluno_v2'),('M23','m23_producao_20261124','TSH_M2_3_Apoio_do_Aluno_v2')]:
 for ext in ['docx','pdf']:copy2(R.parent/folder/'entrega'/(nm+'.'+ext),a/(nm+'.'+ext))
# M2.4: ensinar os meios de acesso ao recurso e corresponder ao novo encerramento.
d=Document(old/'TSH_M2_4_Apoio_do_Aluno_v2.docx')
pars=d.paragraphs
p=next(p for p in pars if p.text.startswith('3. Dar presença ao recurso.'))
p.text='3. Dar presença ao recurso. Procure uma ocasião concreta em que conseguiu sustentar uma qualidade pertinente à alternativa. Se precisa de firmeza, pode lembrar uma relação em que manteve sua posição sem perder o contato. Se nenhuma ocasião vier, procure uma experiência menor, de outra área da vida, em que tenha conseguido algo dessa qualidade: numa criação, numa prática corporal ou com apoio de alguém. O recurso é escolhido pela função que pode oferecer à situação.'
def after(anchor,txt):
 n=OxmlElement('w:p');anchor._p.addnext(n);p=Paragraph(n,anchor._parent);p.style='Normal';p.add_run(txt);return p
p=after(p,'Situe onde estava, o que fazia e o que permitia participar daquele modo. Deixe a situação difícil de lado e aproxime essa experiência de recurso: postura, ritmo, imagem ou presença de alguém. Se um gesto, uma posição ou uma palavra ajudava, experimente discretamente e confira o apoio que ganha presença agora. Não é necessário reproduzir a experiência inteira.')
after(p,'Se a referência continuar sendo apenas uma ideia, tente outra conhecida ou pause para retomar o Sorriso Interior, já ensinado no M1.3. Ao voltar, confira se esse apoio ajuda a sustentar a alternativa escolhida. Sentir algum alívio e conseguir participar pedem essa conferência. Se não houver apoio acessível, conserve o presente e siga sem reencontrar a cena; registre o que precisa ser aprendido ou buscado.')
p=next(p for p in d.paragraphs if p.text.startswith('Retorne ao presente. Compare primeiro'))
p.text='Encerre a exploração deixando a cena e o ensaio de lado. Reconheça o ambiente, os apoios do corpo e retome seus movimentos. A partir desse momento, sem voltar à cena, compare primeiro os dois registros do vivido e depois os dois da participação. Reconheça diferenças, permanências e o que impediu continuar, se for o caso. Elabore o que ficou disponível e o trabalho que precisa continuar.'
inside=False
for pp in d.paragraphs:
 if pp.text=='A prática: reconhecer, retornar, dar presença e reencontrar':inside=True
 elif pp.text=='Registro da exploração':inside=False
 if inside and pp.text and pp.style.name=='Normal':pp.paragraph_format.space_after=Pt(4)
# Converter quebras vazias herdadas em quebra de seção no próximo parágrafo.
pars=list(d.paragraphs)
for ii,pp in enumerate(pars):
 if not pp.text and pp._p.xpath('.//w:br[@w:type="page"]') and not pp._p.xpath('.//w:drawing'):
  target=next((qq for qq in pars[ii+1:] if qq.text or qq._p.xpath('.//w:drawing')),None)
  if target is not None:target.paragraph_format.page_break_before=True
  pp._p.getparent().remove(pp._p)
d.core_properties.title='M2.4 — O que mantém a repetição de uma resposta?';d.save(a/'TSH_M2_4_Apoio_do_Aluno_v3.docx')
print('Guias compostos: M2.2, M2.3, M2.4 prática; teoria preservada; apoio M2.4 alinhado.')
