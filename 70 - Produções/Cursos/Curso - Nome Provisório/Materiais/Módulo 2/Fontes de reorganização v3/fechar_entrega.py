from pathlib import Path
from shutil import copy2
from zipfile import ZipFile,ZIP_DEFLATED
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
from PIL import Image
import fitz,json,base64,hashlib,re
R=Path(__file__).resolve().parent;O=R/'entrega';S=R/'fontes_finais';S.mkdir(exist_ok=True)
items=[('M22','01_M2_2_Pratica',8,8,'M2.2','3'),('M23','02_M2_3_Pratica',12,6,'M2.3','3'),('M24P1','03_M2_4_Teoria',21,4,'M2.4','2'),('M24P2','04_M2_4_Pratica',14,5,'M2.4','3')]
checks=[];models={}
for key,folder,n,sequence,lesson,version in items:
 folder=O/folder;renders=json.loads((R/('render_'+key+'.json')).read_text())['files'];assert len(renders)==n
 c=canvas.Canvas(str(folder/(key+'_Slides_v'+version+'.pdf')),pagesize=(960,540))
 for a in renders:c.drawImage(ImageReader(a['path']),0,0,960,540);c.showPage()
 c.save()
 if key!='M24P1':
  src=R/'qa'/('guia_'+key)/(key+'_Guia_v3.pdf');copy2(src,folder/(key+'_Guia_v3.pdf'))
  d=json.loads((R/'depois'/(key+'.json')).read_text());data=(R/'depois'/(key+'.json.gz')).read_bytes()
 else:
  before=json.loads((R/'antes'/(key+'.json')).read_text());d={'slides':[{**a,'title':a['shapes'][1]['text'] if a['shapes'][1]['name']=='headline' else a['shapes'][2]['text'],'screenActual':a['shapes']} for a in before]};data=(R/'antes'/(key+'.json.gz')).read_bytes()
 d.update(lesson=lesson,productionKey=key,version=version,nativeSequence=sequence,date='2026-11-24')
 d['nativeSnapshot']={'encoding':'base64+gzip','format':'JSON de presentation.toProto()','data':base64.b64encode(data).decode()}
 d['sourceRecovery']={'repository':'fabianodeliberalli/base-cognitiva-vault','parentCommit':'46981ea2ef66f66dad9f412fa78947370bb2ac8e','priorVersion':'M2.2/M2.3 prática v2; M2.4 partes 1 e 2 v2','mapping':'sourceIndex usa índice zero da apresentação anterior. A teoria M2.4 foi preservada integralmente.','notes':'Composição autoral e trilha das notas em compor_notas.py. A montagem conserva layouts, figuras, marcas e relações.'}
 models[key]=d;(S/(key+'_Conteudo_e_notas_v'+version+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
 doc=Document(folder/(key+'_Guia_v'+version+'.docx'));pars=[p.text for p in doc.paragraphs]
 missing=[line for s in d['slides'] for line in s['notes'].splitlines() if line and line not in pars]
 assert not missing,(key,missing[:3])
 pdf=fitz.open(folder/(key+'_Slides_v'+version+'.pdf'))
 matches=[]
 for i,p in enumerate(pdf):
  pix=fitz.Pixmap(pdf,p.get_images()[0][0]);im=Image.open(renders[i]['path']).convert('RGB');matches.append(pix.samples==im.tobytes())
 assert all(matches)
 words=sum(len(re.findall(r'\b[\wÀ-ÿ]+(?:[’\'-][\wÀ-ÿ]+)*\b','\n'.join(l for l in s['notes'].splitlines() if not(l.isupper() and len(l)<60)))) for s in d['slides'])
 checks.append({'key':key,'slides':n,'nativeSequence':sequence,'notesAndGuideMatch':True,'slidePdfPixelsMatch':True,'guidePages':len(fitz.open(folder/(key+'_Guia_v'+version+'.pdf'))),'spokenWords':words})
copy2(R/'qa/apoio_M24_final2/TSH_M2_4_Apoio_do_Aluno_v3.pdf',O/'Apoios_do_aluno/TSH_M2_4_Apoio_do_Aluno_v3.pdf')
# Texto pesquisável do apoio M2.4, conservando referências e imagens da fonte Git.
support=(R/'fontes/M2.4 - Apoio do aluno v2.md').read_text()
doc=Document(O/'Apoios_do_aluno/TSH_M2_4_Apoio_do_Aluno_v3.docx')
original=Document(R.parent/'profundidade_tsh_20261123/entrega/TSH_M2_4_Apoio_do_Aluno_v2.docx')
a=next(p.text for p in original.paragraphs if p.text.startswith('3. Dar presença ao recurso.'))
pa=[p.text for p in doc.paragraphs];idx=next(i for i,p in enumerate(pa) if p.startswith('3. Dar presença ao recurso.'))
assert a in support
support=support.replace(a,'\n\n'.join(pa[idx:idx+3]))
a=next(p.text for p in original.paragraphs if p.text.startswith('Retorne ao presente. Compare primeiro'))
b=next(p.text for p in doc.paragraphs if p.text.startswith('Encerre a exploração deixando'))
assert a in support;support=support.replace(a,b).replace('v2','v3',1)
(S/'M2.4 - Apoio do aluno v3.md').write_text(support)
readme='''# TSH — Ordem de gravação até M2.4

Abra as pastas numeradas nesta ordem. Cada pasta contém slides PDF e guia Word/PDF. As apresentações editáveis incluem as mesmas notas e podem ser exportadas como PowerPoint.

| Ordem | Gravação | Slides | Estimativa do vídeo |
| --- | --- | --- | --- |
| 1 | M2.2 — Prática guiada | 8 | 6–8 minutos |
| 2 | M2.3 — Prática guiada | 12 | 8–10 minutos |
| 3 | M2.4 — Compreensão e fundamentos | 21 | 25–35 minutos, conforme a exposição |
| 4 | M2.4 — Prática guiada e integração | 14 | 12–15 minutos |

As estimativas consideram a extensão das notas, fala sem pressa e breves silêncios de percepção. São referências de planejamento; não foram cronometradas em nova gravação. O aluno pode pausar para escrever e realizar etapas demoradas. Você preserva os pequenos silêncios necessários à condução, sem esperar todo o tempo de preenchimento.

Apresentações com notas:
- M2.2 prática: https://chatgpt.com/space/page_b4a2a7c376008191b2e89f8f7d1119b3
- M2.3 prática: https://chatgpt.com/space/page_85cb82566f6c8191a65ca24c77508761
- M2.4 teoria: https://chatgpt.com/space/page_fd5f861d69b08191ba03a33bc6898fb9
- M2.4 prática: https://chatgpt.com/space/page_b9880588aff481919268e4851f70ab05

M2.2 e M2.3: grave a prática completa com encerramento e elaboração. As teorias editadas de 28min13s e 24min55s continuam como primeiras partes. Elas não precisam ser gravadas outra vez por esta reorganização.

M2.4: grave a teoria completa e, em separado, a prática. A exposição preserva seus fundamentos e 21 telas. A prática distingue os registros antes/depois, ensina escolher e aproximar o recurso e encerra a exploração antes da comparação e elaboração.

M2.1: o vídeo editado de 34min43s continua aproveitável. Esta entrega não acrescenta uma gravação obrigatória nem refaz seus materiais.

Os apoios do aluno estão na pasta correspondente. M2.2/M2.3 conservam os fundamentos e operações já entregues; M2.4 recebeu a orientação de acesso ao recurso e o encerramento alinhado à prática atual. Guias são materiais de produção.

As notas atuais substituem as conduções longas anteriores. Nos momentos de demonstração, termine o exemplo antes da situação pessoal. Durante a prática, mantenha a mesma situação. Os avisos de pausa e encerramento estão no ponto de uso. Use o guia correspondente ao conjunto atual.
'''
(O/'00_Leia_primeiro_Ordem_de_gravacao.md').write_text(readme)
# Fonte de reprodução inclui a correção do contexto visual da primeira tela M2.2.
p=R/'aplicar_reorganizacao.js';txt=p.read_text();needle="shape(presentation.slides.getItem(0),'demo-observation-0').text.fontSize=29;"
extra="\n  const context=presentation.slides.getItem(0).shapes.add({name:'demo-context',geometry:'textbox',position:{left:80,top:233,width:920,height:30},fill:'none',line:{style:'solid',fill:'none',width:0}});context.text='Exemplo: um convite para dançar';context.text.style={fontSize:22,typeface:'Inter',color:'#245E78',wrap:'square',autoFit:'none',insets:0};"
if "name:'demo-context'" not in txt:p.write_text(txt.replace(needle,needle+extra))
(S/'conferencia_final.json').write_text(json.dumps({'decks':checks,'supportM24Pages':len(fitz.open(O/'Apoios_do_aluno/TSH_M2_4_Apoio_do_Aluno_v3.pdf')),'scope':'Conferência de correspondência e inspeção visual dos suportes, junto da revisão da ferramenta e da progressão. Não mede aprendizagem nem confirma gravação ou publicação.'},ensure_ascii=False,indent=2))
# Pacotes por aula atualizam os endereços existentes; o conjunto geral reúne a ordem completa.
for key,folder,lesson in [('M22','01_M2_2_Pratica','M2_2'),('M23','02_M2_3_Pratica','M2_3'),('M24','03_M2_4_Teoria','M2_4')]:
 zpath=R/('TSH_'+lesson+'_Gravacao_Conjunto_v3.zip')
 with ZipFile(zpath,'w',ZIP_DEFLATED) as z:
  folders=[O/folder]+([O/'04_M2_4_Pratica'] if key=='M24' else [])
  for f in folders:
   for p in f.iterdir():z.write(p,f.name+'/'+p.name)
  for p in (O/'Apoios_do_aluno').glob('TSH_'+lesson+'_*'):z.write(p,'Apoio_do_aluno/'+p.name)
  z.write(O/'00_Leia_primeiro_Ordem_de_gravacao.md','00_Leia_primeiro.md')
  for p in S.glob('*'):
   if p.name.startswith(key) or (key=='M24' and p.name.startswith('M2.4')):z.write(p,'Fontes_de_producao/'+p.name)
  for name in ['compor_notas.py','aplicar_reorganizacao.js','produzir_guias.py']:z.write(R/name,'Fontes_de_producao/'+name)
 with ZipFile(zpath) as z:assert z.testzip() is None
with ZipFile(O/'TSH_Gravacoes_M2_2_a_M2_4_v3.zip','w',ZIP_DEFLATED) as z:
 for p in O.rglob('*'):
  if p.is_file() and p.suffix!='.zip':z.write(p,p.relative_to(O))
 for p in S.iterdir():z.write(p,'Fontes_de_producao/'+p.name)
 for name in ['compor_notas.py','aplicar_reorganizacao.js','produzir_guias.py']:z.write(R/name,'Fontes_de_producao/'+name)
with ZipFile(O/'TSH_Gravacoes_M2_2_a_M2_4_v3.zip') as z:assert z.testzip() is None
print(json.dumps(checks,ensure_ascii=False,indent=2));print('Entregas e pacotes montados.')
