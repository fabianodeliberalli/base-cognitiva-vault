from pathlib import Path
from copy import deepcopy
import json,re,shutil,hashlib,zipfile,gzip
from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
import fitz

R=Path(__file__).resolve().parent
REG=R/'registro'
BASE='70 - Produções/Cursos/Curso - Nome Provisório/Materiais/Módulo 2/'
def write(path,text):
 p=REG/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

plan=(R/'fontes/plano_m2.md').read_text().lstrip('+').replace('versao: "0.12"','versao: "0.13"').replace('data: 2026-11-22','data: 2026-11-23')
a=plan.index('Fabiano adotou');b=plan.index('## M2.1')
plan=plan[:a]+'''Fabiano adotou, em 22/11/2026, duas partes de gravação a partir de M2.2 nas aulas com prática autônoma: compreensão/fundamentos e prática guiada/integração, mantendo a mesma aula. [[M2.2 - Prática guiada v1]], [[M2.3 - Avaliação da gravação e edição parte 1 v1]] e [[M2.3 - Prática guiada v1]] e [[M2.4 - Produção em duas partes v2]] localizam as aplicações. [[00 - Estado e Continuidade da Produção M2]] é a entrada para materiais atuais e genealogia. As montagens integradas anteriores permanecem históricas.

**Correção recorrente de profundidade — 23/11/2026.** As fontes autorais, teóricas e experienciais precisam ser transformadas em desenvolvimento da questão da aula, antes da condensação para slides e notas. A conferência localiza a contribuição efetivamente ensinada e sua relação com a prática. Recuperar autores ou verificar arquivos não sustenta, por si, uma avaliação de profundidade. Aplicar a base autoral v1.6 e o padrão v2.11 durante a execução, sem depender de novo lembrete de Fabiano. A objetividade retira repetição e desvios; conserva as distinções e relações necessárias ao aluno. Não há quota fixa de autores, imagens ou telas.

M2 desenvolve a constituição da experiência, relevância/simbolização, experiência de certeza, repetição, distinção entre vivido/sentido/origem e Tradução recursiva. As situações e metáforas participam da elaboração; não substituem fundamentos. M2.5–M2.6 mantêm orientação estrutural e aguardam composição final. O módulo conserva seis aulas, Cartografia comum e estudo assíncrono suficiente; a arquitetura completa continua nove módulos e 59 aulas. Não se infere execução do encontro ao vivo a partir de seu planejamento.

'''+plan[b:]
plan=plan.replace('[[M2.3 - Trilha de exposição v0.2]], revisão produzida para avaliação:','[[M2.3 - Avaliação da gravação e edição parte 1 v1]] e [[M2.3 - Prática guiada v1]] localizam os materiais atuais e a condução separada. A revisão substantiva anterior desenvolveu:')
plan=plan.replace('Meio segundo como imagem, sem duração universal.','Meio segundo atribuído à síntese de Cozolino, sem duração universal e sem equivalência entre cronologia neural, certeza e transe cotidiano.')
needle='## M2.5 — Acontecimento, experiência e interpretação'
pos=plan.index(needle)
plan=plan[:pos]+'''**Aplicação substantiva atual — v2, 23/11/2026:** [[M2.4 - Produção em duas partes v2]] tem 21 telas de compreensão/fundamentos e 18 de prática/integração. Parte 1/8 desenvolve como memória, corpo, afeto, expectativa e relação participam do presente, com Cozolino. Parte 1/9 distingue experiência sentida e aval da conclusão, em diálogo editorial com Kahneman. Parte 1/10 desenvolve competência incorporada, aprendizagem de regularidades e retorno sobre resultados, com Kahneman/Klein e o retorno com aquisição autoral. Os dois tempos da Tradução são forma vivida/elaboração em reciprocidade; não são compartimentos separados por 500 ms. A escolha do recurso e a comparação ganham esse fundamento em 18–19 e Parte 2/15–16. A realização da prática, Parte 2/3–14, conserva sua operação já corrigida. Guias e apoio do aluno foram atualizados. A composição não declara demonstração de reconsolidação nem equivalência entre os modelos dos autores e os Três Eus.

'''+plan[pos:]
plan=plan.replace('## Revisão de exposição e condução — M2.3/M2.4 v0.3','## Etapa histórica de exposição e condução — M2.3/M2.4 v0.3')
plan=plan.replace('são as referências atuais para exposição;','registram a etapa integrada anterior;')
write(BASE+'01 - Plano de produção das seis aulas M2.md',plan)

for filename,source in [('Meio Segundo Vital - Transe que Não se Escolhe e os Três Eus.md','cozolino_fundamento.md'),('Kahneman e Cozolino - Dois Sistemas e o Meio Segundo no TSH.md','kahneman_fundamento.md')]:
 text=(R/'fontes'/source).read_text();text=re.sub(r'atualizado_em: \d{4}-\d{2}-\d{2}','atualizado_em: 2026-11-23',text,count=1)
 idx=text.index('\n## ')
 current='''
## Orientação vigente de uso nas aulas — 23/11/2026

O registro abaixo conserva a formulação e a exploração histórica de Fabiano. Para compor aulas, aplicar esta precisão: Cozolino oferece uma síntese clínica sobre a participação de memória, corpo e emoção na formação do presente; os tempos citados são atribuídos ao autor e não são uma duração universal de toda percepção ou decisão. O diálogo com Kahneman é uma correlação editorial do TSH entre formação da experiência, julgamento e aprendizagem, não uma identidade entre modelos nem uma explicação de toda a deliberação dentro de um intervalo de 500 ms. Eu Básico/Eu Médio e os dois tempos da Tradução são mapas funcionais em diálogo, sem localização anatômica ou correspondência rígida com Sistema 1/Sistema 2. Uma sensação pode ser consciente antes de ser verbalmente elaborada.

A antecipação e os processos menos deliberados também sustentam adaptação, habilidades e competência incorporada. A intuição especializada exige oportunidades de aprender regularidades e receber retorno sobre resultados; repetição, confiança ou familiaridade isoladas não demonstram acerto. A prática educacional não demonstra alteração neural, reconsolidação ou superação empírica das limitações de outro autor. Essas distinções conservam a amplitude do TSH e qualificam a fundamentação, sem transportar o debate de pesquisa à condução da prática.

**Aplicação efetiva:** [[M2.4 - Produção em duas partes v2]], Parte 1/8–10, ensina a formação do vivido, o aval da impressão e a aprendizagem incorporada; 18–19 e Parte 2/15–16 conectam essas relações ao recurso, à comparação e à continuidade. M2.3 investiga o fechamento da leitura e o resgate de outras pistas; M2.4 acrescenta o que continua organizando a participação e o que precisa ganhar sustentação. Os títulos e destinos históricos abaixo não substituem [[01 - Plano de produção das seis aulas M2]] nem [[00 - Estado e Continuidade da Produção M2]].

Fontes primárias conferidas nesta revisão: [trecho de Cozolino publicado pelo autor](https://www.drloucozolino.com/neuroscience/the-vital-half-second); [Kahneman e Klein, 2009](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf), DOI 10.1037/a0016755; [Guggisberg e Mottaz, 2013](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2013.00385/full), DOI 10.3389/fnhum.2013.00385, para os limites da inferência temporal. A leitura dirigida dessas fontes não é uma nova leitura integral das obras citadas no histórico.

## Registro histórico e correlações a recuperar com essa precisão
'''
 text=text[:idx]+current+text[idx:]
 if source=='cozolino_fundamento.md':
  text=text.replace('### 1. O dado neurocientífico (Cozolino)','### 1. A síntese neurocientífica apresentada por Cozolino')
  text=text.replace('Os dois mapas coincidem no ponto que importa para o curso: o que responde primeiro guarda a memória e recebe a sugestão; o que chega depois explica.','A aproximação histórica privilegia a relação entre referências aprendidas e elaboração. A aplicação atual conserva as diferenças entre os mapas, sem reduzir memória, sugestão, consciência ou escolha a esse par.')
 else:
  text=text.replace('Cozolino explica **quando** o passado assume o presente (o meio segundo entre o sistema rápido e o lento). Kahneman explica **por que** o sistema lento quase sempre deixa (o Sistema 2 economiza esforço e endossa o que o Sistema 1 já montou). Juntos, respondem à pergunta da aula: por que entender um padrão não impede que ele se repita.','Cozolino ajuda a investigar como referências anteriores participam da experiência presente. Kahneman ajuda a investigar o aval dado às impressões e o custo de examiná-las. No TSH, esse diálogo amplia a pergunta sobre por que uma compreensão pode mudar sem que outra participação já esteja disponível.')
  text=text.replace('processamento neural: 10–50 ms contra 500–600 ms','síntese clínica/neurocientífica com tempos aproximados atribuídos ao autor').replace('dado sobre o intervalo','participação de memória, corpo e emoção na formação do vivido').replace('linguagem sobre o que acontece no intervalo','julgamento, atenção e aprendizagem, sem confiná-los ao intervalo')
  text=text.replace('A correspondência com os Três Eus continua **funcional**: o que responde primeiro e guarda o aprendido (Sistema 1, sistema rápido, Eu Básico, *unihipili* de Long); o que chega depois, explica e escolhe (Sistema 2, sistema lento, Eu Médio, *uhane*).','A correspondência com os Três Eus é uma aproximação **funcional**, não uma equivalência: processos rápidos também incluem habilidades refinadas, e a elaboração não é um controlador separado do corpo e das relações. As nomenclaturas históricas de Long permanecem no acervo com seu contexto.')
  text=text.replace('**Proposta:** o TSH vai além desse ponto por outro caminho — o corpo. Respiração, regulação, atenção treinada, experiência repetida e reconsolidação da memória atuam no sistema rápido diretamente, não só pelo controle do lento. Kahneman fundamenta o diagnóstico; a proposta de treino é do TSH.','**Proposta formativa do TSH:** articular reflexão, experiência corporal, atenção, relações e continuidade para investigar o que se torna disponível na participação. É uma elaboração pedagógica do TSH; uma prática isolada não demonstra atuação direta sobre um sistema cognitivo, reconsolidação ou superioridade empírica em relação à proposta de Kahneman.')
 write('20 - Notas Conceituais/'+filename,text)

old=(R/'fontes/localizador_v1.md').read_text().replace('status: materiais-revisados','status: historico-substituido-pela-v2')
old=old.replace('**Fonte atual para a gravação:**','**Registro histórico — substituído em 23/11/2026 por [[M2.4 - Produção em duas partes v2]].** As páginas editáveis e os links de arquivos abaixo agora abrem a revisão v2. A v1 é recuperável pelo histórico Git, seus JSONs e snapshots próprios, e pelo histórico das versões dos arquivos. A descrição seguinte documenta o que foi entregue naquela etapa.\n\n**Composição da v1:**',1)
write(BASE+'M2.4 - Produção em duas partes v1.md',old)

for part in [1,2]:
 spec=json.loads((R/f'parte{part}_v2.json').read_text())
 lines=['---','tipo: trilha-de-exposicao','projeto: Traduzindo o Ser Humano','aula: M2.4',f'parte: {part}','versao: "2.0"','data: 2026-11-23','---','',f'# M2.4 — Parte {part} — {spec["title"]}','',f'{len(spec["slides"])} telas. Fonte efetivamente salva na apresentação nativa, sequência 4. [[M2.4 - Produção em duas partes v2]] localiza o conjunto.','']
 for s in spec['slides']:
  lines += [f'## {s["number"]}. {s["title"]}','',f'**Momento:** {s["moment"]}','','**Na tela**','']
  lines += [f'- {v["text"]}' for v in s['screen_text'] if v['name'] not in ['lesson-footer','brand-label']]
  lines += ['','**Notas do apresentador**','',s['notes'],'']
 write(BASE+f'M2.4 - Parte {part} - Trilha e notas v2.md','\n'.join(lines))
 target=REG/(BASE+'M2.4 - Fontes de montagem v2');target.mkdir(parents=True,exist_ok=True)
 for name in [f'parte{part}_v2.json',f'fontes/parte{part}_snapshot_v2.json.gz']:shutil.copyfile(R/name,target/Path(name).name)

# Texto completo do apoio realmente entregue, em ordem de corpo, figuras e tabelas.
doc=Document(R/'entrega/TSH_M2_4_Apoio_do_Aluno_v2.docx')
body=doc.element.body;lines=['---','tipo: apoio-do-aluno','projeto: Traduzindo o Ser Humano','aula: M2.4','versao: "2.0"','data: 2026-11-23','---','','# M2.4 — Apoio do aluno','','Texto do apoio Word/PDF v2. As quebras de página são próprias da versão diagramada. [[M2.4 - Produção em duas partes v2]] localiza os arquivos.','']
figures=['escada.png','circularidade.png','pendulo_espiral.png'];fi=0
for element in body:
 if element.tag==qn('w:p'):
  p=Paragraph(element,doc);t=p.text.strip()
  if t:
   st=p.style.name;prefix='# ' if st=='Title' else ('## ' if st=='Heading 1' else ('### ' if st=='Heading 2' else ''))
   lines += [prefix+t,'']
  if element.xpath('.//a:blip'):
   if fi>=len(figures):raise ValueError('Extra figure')
   lines += ['![Figura do acervo TSH](M2.4%20-%20Fontes%20de%20montagem%20v1/figuras/'+figures[fi]+')',''];fi+=1
 elif element.tag==qn('w:tbl'):
  rows=[[c.text.replace('\n',' / ').replace('|','\\|') for c in row.cells] for row in Table(element,doc).rows]
  if rows:
   lines += ['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*len(rows[0]))+' |']
   lines += ['| '+' | '.join(row)+' |' for row in rows[1:]]+['']
assert fi==3,fi
write(BASE+'M2.4 - Apoio do aluno v2.md','\n'.join(lines))
for name in ['aplicar_m24.js','atualizar_documentos.py','revisar_conteudo.py','finalizar_registros.py','corrigir_base.py']:
 shutil.copyfile(R/name,REG/(BASE+'M2.4 - Fontes de montagem v2')/name)

readme='''TRADUZINDO O SER HUMANO — M2.4 — KIT DE GRAVAÇÃO V2
23/11/2026

Uma aula, duas partes.
1. Compreensão e fundamentos: 21 slides, guia com 11 páginas.
2. Prática guiada e integração: 18 slides, guia com 9 páginas.
Apoio do aluno: 9 páginas; ficha para registro nas páginas 7 e 8.

Use os guias v2 com os slides v2. As notas têm uma frase por linha e espaço entre os blocos.
A Parte 1 apresenta e explica; a Parte 2 conduz a prática, encerra e elabora.
A prática termina na tela 14 da Parte 2; a elaboração começa na tela 15.

A revisão desenvolve a formação da experiência, o diálogo Cozolino/Kahneman,
a competência incorporada e a relação desses fundamentos com recurso,
comparação e continuidade. A operação da prática já corrigida foi preservada.

Apresentações editáveis e exportação pelo menu da página:
Parte 1: https://chatgpt.com/space/page_fd5f861d69b08191ba03a33bc6898fb9
Parte 2: https://chatgpt.com/space/page_b9880588aff481919268e4851f70ab05

Para a Hotmart: dois vídeos da mesma aula e um apoio do aluno.
Os guias destinam-se à gravação.
'''
(R/'entrega/LEIA_PRIMEIRO.txt').write_text(readme)
entries=[f'TSH_M2_4_Parte_{p}_{kind}_v2.{ext}' for p in [1,2] for kind,ext in [('Slides','pdf'),('Guia_de_gravacao','docx'),('Guia_de_gravacao','pdf')]]+['TSH_M2_4_Apoio_do_Aluno_v2.docx','TSH_M2_4_Apoio_do_Aluno_v2.pdf','LEIA_PRIMEIRO.txt']
zip_path=R/'entrega/TSH_M2_4_Kit_de_gravacao_v2.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
 for name in entries:archive.write(R/'entrega'/name,name)
with zipfile.ZipFile(zip_path) as archive:assert len(archive.namelist())==9 and archive.testzip() is None
metrics={}
for file in R.joinpath('entrega').iterdir():
 if file.suffix in ['.zip','.docx','.pdf']:
  d={'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
  if file.suffix=='.pdf':
   pdf=fitz.open(file);d['pages']=len(pdf);pdf.close()
  metrics[file.name]=d
(R/'qa/file_metrics.json').write_text(json.dumps(metrics,indent=2,ensure_ascii=False))
print(json.dumps({'files_staged':len([x for x in REG.rglob('*') if x.is_file()]),'zip_entries':len(entries),'files':metrics},ensure_ascii=False))
