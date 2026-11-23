from pathlib import Path
import json,hashlib,zipfile,shutil,gzip,io
from PIL import Image,ImageChops
from docx import Document
import fitz

R=Path(__file__).resolve().parent;REG=R/'registro'
BASE='70 - Produções/Cursos/Curso - Nome Provisório/Materiais/Módulo 2/'
DEST=REG/(BASE+'M2.4 - Fontes de montagem v2')
uploads=json.loads((R/'upload_result.json').read_text())['results']
assert len(uploads)==9
assert all(u['status']=='succeeded' and u['current_version_number']==1 and u['local_metadata_applied'] for u in uploads)
byname={u['file_name']:u for u in uploads}
def url(name):return 'https://chatgpt.com/library?file_id='+byname[name]['library_file_id']+'&account_id=personal'
metrics=json.loads((R/'qa/file_metrics.json').read_text())
checks={}
for part in [1,2]:
 spec=json.loads((R/f'parte{part}_v2.json').read_text())
 native=json.loads(Path(f'/tmp/depth_m24_p{part}_notes_final.json').read_text())
 assert len(spec['slides'])==len(native)==(21 if part==1 else 18)
 assert all(s['notes']==n['notes'] for s,n in zip(spec['slides'],native))
 assert all(hashlib.sha256(s['notes'].encode()).hexdigest()==s['notes_sha256'] for s in spec['slides'])
 d=Document(R/f'entrega/TSH_M2_4_Parte_{part}_Guia_de_gravacao_v2.docx')
 pars=[p.text for p in d.paragraphs]
 cursor=0
 for s in spec['slides']:
  for line in s['notes'].split('\n'):
   if line:
    cursor=pars.index(line,cursor)+1
 pdf=fitz.open(R/f'entrega/TSH_M2_4_Parte_{part}_Slides_v2.pdf')
 assert len(pdf)==len(spec['slides'])
 for i,page in enumerate(pdf):
  imgs=page.get_images();assert len(imgs)==1
  embedded=Image.open(io.BytesIO(pdf.extract_image(imgs[0][0])['image'])).convert('RGB')
  original=Image.open(R/f'qa/parte{part}/slide-{i+1}.png').convert('RGB')
  assert embedded.size==original.size and ImageChops.difference(embedded,original).getbbox() is None
 checks[f'parte{part}']={'telas':len(native),'notas_lidas_da_pagina_iguais_ao_json':True,'guia_word_com_notas_completas_em_ordem':True,'pdf_de_slides_pixel_identico_ao_render_nativo':True,'sequencia_nativa':4}
v1=json.loads((R/'fontes/parte2_v1.json').read_text());v2=json.loads((R/'parte2_v2.json').read_text())
assert all(v1['slides'][i]['notes']==v2['slides'][i]['notes'] for i in range(2,14))
checks['pratica']={'operacao_telas_3_a_14_preservada_textualmente':True,'elaboracao_ampliada_telas':[15,16]}
with zipfile.ZipFile(R/'entrega/TSH_M2_4_Kit_de_gravacao_v2.zip') as z:
 assert len(z.namelist())==9 and z.testzip() is None
checks['kit']={'entradas':9,'crc_correto':True}
report={'aula':'M2.4','versao':'2.0','data':'2026-11-23','arquitetura':'9 módulos e 59 aulas; M2 mantém seis aulas; M2.4 continua uma aula em dois vídeos','avaliacao_substantiva':[
 {'problema':'Fontes nomeadas sem desenvolver sua contribuição','aplicacao':'Parte 1/8 explica como memória, corpo, afeto, expectativas e relação atual participam da formação do presente; 9 distingue sensação e conclusão e ensina o aval da impressão; 10 desenvolve aprendizagem e competência incorporada com condições de retorno sobre resultados.','alcance':'Leitura editorial comparada com as notas conceituais e as fontes primárias; não se declara equivalência entre modelos, cronômetro universal ou estudo de eficácia do curso.'},
 {'problema':'Descontinuidade entre teoria e prática','aplicacao':'Parte 1/18–19 relaciona recurso e comparação ao que precisa ganhar sustentação; Parte 2/15 distingue acesso, cultivo e condições; 16 liga ensaio e retorno do encontro real ao retorno com aquisição.','alcance':'A operação da prática já corrigida permanece; a elaboração acrescenta fundamento sem interromper a realização.'},
 {'problema':'Objetividade confundida com redução do pensamento','aplicacao':'Duas novas telas de desenvolvimento foram incluídas por necessidade do raciocínio; as notas mantêm uma frase por linha e blocos separados. O apoio recebeu uma página conectada, antes de função/expressão/condições.','alcance':'A contagem não é evidência de profundidade. A avaliação se apoia nas relações ensinadas nas passagens indicadas.'},
 {'problema':'Integração restrita à última intervenção do autor','aplicacao':'AGENTS, base autoral v1.6, padrão v2.11, ficha v0.61, estado e plano M2 registram a correção como recorrente e geral; caminhos antigos foram atualizados.','alcance':'Isso não declara M2.1–M2.3 ou outros materiais refeitos nem garante o comportamento de aplicativos que não recuperem a base.'}
 ],'verificacao_tecnica':checks,'revisao_visual':{'slides':'39 telas finais examinadas em contatos e telas centrais individualmente; hierarquia, diagramas, legibilidade e região da câmera conferidos.','documentos':'11 páginas do guia 1, 9 do guia 2 e 9 do apoio renderizadas; documentos revistos em contatos, com página de elaboração da prática inspecionada individualmente.','limite':'Revisão visual e integridade verificam apresentação e correspondência; não medem aprendizagem nem eficácia.'},'arquivos':metrics,'registros_de_salvamento':[{k:u[k] for k in ['file_name','library_file_id','file_id','current_version_number','status','local_metadata_applied']} for u in uploads]}
(REG/(BASE+'M2.4 - Conferência de conteúdo e arquivos v2.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))
for name in ['consultas_20261123.json']:
 shutil.copyfile(R/'fontes'/name,DEST/name)
shutil.copyfile(R/'conferir_e_localizar.py',DEST/'conferir_e_localizar.py')
kit=url('TSH_M2_4_Kit_de_gravacao_v2.zip')
locator='''---
tipo: localizador-de-producao
projeto: Traduzindo o Ser Humano
aula: M2.4
versao: "2.0"
data: 2026-11-23
status: materiais-revisados
---

# M2.4 — Produção em duas partes v2

**Composição atual:** 21 telas de compreensão/fundamentos e 18 de prática guiada/integração. Uma aula em dois vídeos; arquitetura de nove módulos e 59 aulas preservada. A v1 e a montagem integrada v0.3 permanecem históricas. Usar guias e slides v2 em conjunto.

[Baixar todo o kit em um arquivo]('''+kit+''') — dois PDFs de slides, dois guias Word/PDF, apoio do aluno Word/PDF e orientação de uso. Nove entradas. Os arquivos atuais foram atualizados preservando a identidade dos links; revisão de conteúdo v2 corresponde à versão de arquivo 1. A versão anterior de arquivo 0 permanece histórica.

| Parte | Apresentação editável | Slides | Guia |
| --- | --- | --- | --- |
'''
for part,page in [(1,'page_fd5f861d69b08191ba03a33bc6898fb9'),(2,'page_b9880588aff481919268e4851f70ab05')]:
 locator+=f'| {part} | [Abrir](https://chatgpt.com/space/{page}), sequência 4 | [PDF]({url(f"TSH_M2_4_Parte_{part}_Slides_v2.pdf")}) | [Word]({url(f"TSH_M2_4_Parte_{part}_Guia_de_gravacao_v2.docx")}) / [PDF]({url(f"TSH_M2_4_Parte_{part}_Guia_de_gravacao_v2.pdf")}) |\n'
locator+='\n[Apoio do aluno em PDF]('+url('TSH_M2_4_Apoio_do_Aluno_v2.pdf')+') / [Word]('+url('TSH_M2_4_Apoio_do_Aluno_v2.docx')+') — nove páginas; ficha de registro nas páginas 7–8. Guias: 11 páginas na Parte 1 e nove na Parte 2.\n'
locator+='''
## Correção aplicada ao conteúdo

Fabiano reiterou que a simplificação é recorrente desde o início, não restrita a Cozolino. As orientações já pediam profundidade; o material anterior resumiu relações que precisavam ser ensinadas. A base autoral v1.6 e o padrão v2.11 orientam desenvolver antes de condensar e localizar a contribuição efetiva no produto. Conferência técnica não demonstra integração teórica.

| Questão ensinada | Aplicação na aula e contribuição das fontes |
| --- | --- |
| Como a experiência chega organizada | Parte 1/4–6 desenvolve configuração, forma/elaboração e a contribuição de Bion; 8 ensina a participação de memória, corpo, afeto, expectativas e relação, com a síntese de Cozolino. O presente não é reduzido ao passado. |
| Como a impressão ganha aval | Parte 1/9 distingue “sinto que decepcionei” e “eu decepcionei”. O diálogo com Kahneman orienta conferir o que foi vivido e as pistas da conclusão; elaboração pode investigar ou justificar a impressão. É uma correlação editorial, sem identidade entre os modelos ou os Eus. |
| O que aprender transforma | Parte 1/10 desenvolve adaptação, habilidade e prontidão; Kahneman/Klein entram pelas condições de aprendizagem e retorno sobre resultados. O shakuhachi serve ao gesto e à escuta aprendidos, sem autobiografia inventada. Competência incorporada e retorno com aquisição dão direção à continuidade. |
| Como o recurso participa | Parte 1/18–19 investiga a função e a sustentação vivida do recurso, em lugar de apenas escolher uma frase. Parte 2/15–16 diferencia acesso, cultivo e condições concretas e articula ensaio e encontro real. |
| O que a resposta preserva e o que pede expressão | Parte 1/7 e 11–17 conserva circularidade/Morin, escada do acervo, singularidade/Essência, Milgram e condições relacionais e materiais. Pêndulo e espiral mantêm funções diferentes. |
| O que a prática permite investigar | Parte 2/3–14 mantém a mesma situação e o mesmo começo, com registros de vivido e participação antes/depois. Retorno, recurso, reencontro, comparação e encerramento permanecem reconhecíveis. A elaboração ampliada começa em 15, depois do encerramento em 14. |

Os dois tempos da Tradução não são dois compartimentos separados por 500 ms. A pessoa pode sentir conscientemente antes de conseguir elaborar em palavras. Os tempos de Cozolino são atribuídos à síntese do autor e não são duração universal de toda percepção ou decisão. O ensaio não demonstra reconsolidação ou mecanismo neural. As distinções qualificam a fundamentação sem ocupar a condução prática com observações de pesquisa.

## Fontes, genealogia e recuperação

[[M2.4 - Parte 1 - Trilha e notas v2]], [[M2.4 - Parte 2 - Trilha e notas v2]] e [[M2.4 - Apoio do aluno v2]] conservam o conteúdo completo realmente entregue. `M2.4 - Fontes de montagem v2/parte1_v2.json` e `parte2_v2.json` contêm textos de tela, notas, ordem e hashes; os snapshots nativos comprimidos conservam o estado editável da sequência 4.

As notas-mãe [[Meio Segundo Vital - Transe que Não se Escolhe e os Três Eus]], [[Kahneman e Cozolino - Dois Sistemas e o Meio Segundo no TSH]] e [[O Caminho de Descida, Subida e Retorno com Aquisição]] fundamentam a ampliação. Foram conferidos o trecho primário de Cozolino, o artigo de Kahneman/Klein de 2009 e a revisão de Guggisberg/Mottaz de 2013, conforme referências opcionais do apoio. A contribuição e os limites entram na explicação; bibliografia completa fica no aprofundamento do aluno.

`consultas_20261123.json` localiza a consulta dirigida às bases e notas atuais, com SHAs. As passagens da monografia, TCC, mapas e fontes da composição anterior continuam localizadas em `M2.4 - Fontes de montagem v1/fontes/consultas_desta_revisao.json`; esta revisão não declara nova leitura integral dessas obras. Imagens e estilos de origem permanecem na v1, sem duplicar ou descaracterizar os mapas.

Os scripts v2 documentam as adaptações e dependem dos dados v1 indicados: especificações anteriores, gerador de documentos, kit anterior e snapshots. Ao recuperar em outra máquina, ajustar a raiz local, recuperar as dependências pelos seus registros e carregar as faces Inter regular/negrito e EB Garamond negrito antes da montagem. `aplicar_m24.js` usa a versão nativa v1 de 19/18 telas; não aplicá-lo à v2 já salva. Os JSONs finais são suficientes para recuperar o conteúdo, sem executá-los novamente.

[[M2.4 - Conferência de conteúdo e arquivos v2.json]] separa a avaliação substantiva da conferência técnica, com localizações e limites. Não se afirma que M2.1–M2.3 ou outras aulas foram refeitas nesta entrega. [[01 - Plano de produção das seis aulas M2]] e [[00 - Estado e Continuidade da Produção M2]] localizam a progressão atual e o que permanece por produzir.

## Uso na Hotmart

Dois vídeos da mesma aula, primeiro compreensão/fundamentos, depois prática guiada/integração. Um apoio reúne as duas partes; os guias destinam-se à gravação. A produção dos arquivos não confirma upload ou publicação.
'''
(REG/(BASE+'M2.4 - Produção em duas partes v2.md')).write_text(locator)
print(json.dumps({'checks':checks,'saved_files':len(uploads),'staged_files':len([x for x in REG.rglob('*') if x.is_file()]),'kit':kit},ensure_ascii=False))
