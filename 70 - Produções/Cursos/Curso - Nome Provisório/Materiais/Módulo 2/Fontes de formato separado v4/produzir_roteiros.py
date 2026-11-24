from pathlib import Path
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import json,re
R=Path(__file__).resolve().parent;O=R/'entrega';O.mkdir(exist_ok=True)
exec((R.parent/'m23_producao_20261124/setup_documentos.py').read_text())
for key in ['M22','M23','M24P1','M24P2']:
 a=json.loads((R/(key+'_formato.json')).read_text());F=O/a['folder'];F.mkdir(exist_ok=True)
 d=Document();setup(d,12.1)
 d.styles['Normal'].paragraph_format.line_spacing=1.02;d.styles['Normal'].paragraph_format.space_after=Pt(2.2)
 d.styles['Heading 2'].font.size=Pt(17);d.styles['Heading 2'].paragraph_format.space_before=Pt(9);d.styles['Heading 2'].paragraph_format.space_after=Pt(6)
 p=d.sections[0].footer.paragraphs[0];r=p.add_run('TSH · '+a['title']+' · ');r.font.name='Inter';r.font.size=Pt(8)
 f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'PAGE');p._p.append(f)
 header=d.sections[0].header.paragraphs[0];rr=header.add_run(a['subtitle']);rr.font.name='Inter';rr.font.size=Pt(8);rr.font.color.rgb=RGBColor.from_string('245E78')
 for gi,group in enumerate(a['groups']):
  if gi==0:
   d.add_paragraph(a['title'],'Title')
   pp=d.add_paragraph(a['brief']);pp.paragraph_format.space_after=Pt(8)
  for jj,idx in enumerate(group):
   s=a['slides'][idx]
   pp=d.add_paragraph(f"Slide {s['number']} · {s['title'].replace(chr(10),' ')}",'Heading 2')
   if gi and jj==0:pp.paragraph_format.page_break_before=True
   for li,line in enumerate(s['briefing']):
    line_for_doc=re.sub(r'([.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])',r'\1\n',line)
    pp=d.add_paragraph(line_for_doc)
    pp.paragraph_format.keep_together=True;pp.paragraph_format.keep_with_next=li<len(s['briefing'])-1
    if line.isupper() or line.startswith('PAUSAR'):
     for rr in pp.runs:rr.bold=True;rr.font.color.rgb=RGBColor.from_string('8B6236')
 d.core_properties.title=a['title']+' — roteiro separado de apoio';d.core_properties.subject='Briefing e direção das ideias. Não é fala integral predeterminada.'
 d.save(F/(key+'_Roteiro_de_apoio_v'+a['version']+'.docx'))
 md=['# '+a['title']+' — roteiro separado','',a['brief'],'','**Ganho pretendido:** '+a['gain'],'','Estimativa de planejamento: '+a['estimated']+'.','']
 for s in a['slides']:md+=['## Slide '+str(s['number'])+' · '+s['title'].replace('\n',' '),'']+[re.sub(r'([.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])',r'\1\n',x)for x in s['briefing']]+['']
 (R/(key+'_Roteiro_de_apoio_v'+a['version']+'.md')).write_text('\n'.join(md))
 # Fonte de desenvolvimento mantém o raciocínio e a genealogia, sem ser material de consulta durante gravação.
 base=['# '+a['title']+' — base de desenvolvimento','', 'Esta fonte conserva o desenvolvimento que precedeu a condensação. O suporte de gravação atual é o roteiro separado, com função própria.','']
 for s in a['slides']:base+=['## '+str(s['number'])+' · '+s['title'].replace('\n',' '),'',s['development'],'']
 (R/(key+'_Base_de_desenvolvimento.md')).write_text('\n'.join(base))
print('Quatro roteiros separados produzidos, com base de desenvolvimento preservada.')
