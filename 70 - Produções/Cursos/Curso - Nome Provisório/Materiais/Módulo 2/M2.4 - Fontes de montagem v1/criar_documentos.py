from pathlib import Path
import json
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT

R=Path(__file__).resolve().parent;OUT=R/'entrega'
def document(size=11):
 d=Document();s=d.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7)
 s.top_margin=Cm(1.7);s.bottom_margin=Cm(1.5);s.left_margin=Cm(1.8);s.right_margin=Cm(1.8)
 normal=d.styles['Normal'];normal.font.name='Inter';normal.font.size=Pt(size);normal.font.color.rgb=RGBColor.from_string('082A45')
 normal.paragraph_format.line_spacing=1.12;normal.paragraph_format.space_after=Pt(7)
 for st,sz in [('Title',27),('Heading 1',22),('Heading 2',17),('Heading 3',13)]:
  x=d.styles[st];x.font.name='EB Garamond';x.font.size=Pt(sz);x.font.color.rgb=RGBColor.from_string('082A45');x.paragraph_format.keep_with_next=True;x.paragraph_format.space_before=Pt(8);x.paragraph_format.space_after=Pt(7)
 for st in d.styles:
  if st.type==1 and st.font.name:
   rp=st.element.get_or_add_rPr();f=rp.find(qn('w:rFonts'))
   if f is None:f=OxmlElement('w:rFonts');rp.insert(0,f)
   for a in list(f.attrib):
    if 'theme' in a.lower():del f.attrib[a]
   for a in ['ascii','hAnsi','eastAsia','cs']:f.set(qn('w:'+a),st.font.name)
  pp=st.element.find(qn('w:pPr'))
  if pp is not None:
   for b in list(pp.findall(qn('w:pBdr'))):pp.remove(b)
 foot=s.footer.paragraphs[0];run=foot.add_run('TRADUZINDO O SER HUMANO  ·  M2.4  ·  ');run.font.name='Inter';run.font.size=Pt(8);run.font.color.rgb=RGBColor.from_string('245E78')
 field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');foot._p.append(field)
 return d
def para(d,t,style=None):return d.add_paragraph(t,style)
def heading(d,t):return para(d,t,'Heading 1')
def page(d,t):d.add_page_break();heading(d,t)
def caption(d,t):
 p=para(d,t);p.paragraph_format.space_after=Pt(9)
 for r in p.runs:r.font.size=Pt(9);r.font.color.rgb=RGBColor.from_string('245E78')
def image(d,name,width):d.add_picture(str(R/'figuras'/name),width=Cm(width))
def table(d,headers,rows,widths=None):
 t=d.add_table(rows=1,cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 for i,h in enumerate(headers):t.rows[0].cells[i].text=h
 for row in rows:
  for c,txt in zip(t.add_row().cells,row):c.text=txt
 for ri,row in enumerate(t.rows):
  for ci,c in enumerate(row.cells):
   if widths:c.width=Cm(widths[ci])
   c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
   tcpr=c._tc.get_or_add_tcPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'173F52' if ri==0 else ('F4EFEA' if ri%2 else 'DEE9EB'));tcpr.append(sh)
   borders=OxmlElement('w:tcBorders');edge=OxmlElement('w:right');edge.set(qn('w:val'),'single');edge.set(qn('w:sz'),'10');edge.set(qn('w:color'),'FFFFFF');borders.append(edge);tcpr.append(borders)
   for p in c.paragraphs:
    p.paragraph_format.space_after=Pt(5);p.paragraph_format.space_before=Pt(5)
    for r in p.runs:r.font.size=Pt(10);r.font.color.rgb=RGBColor.from_string('F4EFEA' if ri==0 else '082A45');r.bold=ri==0
   trpr=row._tr.get_or_add_trPr();stay=OxmlElement('w:cantSplit');trpr.append(stay)
 return t
def lines(d,label,n=2):
 p=para(d,label);p.paragraph_format.keep_with_next=True
 for r in p.runs:r.bold=True;r.font.size=Pt(10)
 for _ in range(n):
  p=para(d,'________________________________________________________________________________');p.paragraph_format.space_after=Pt(7)
  for r in p.runs:r.font.color.rgb=RGBColor.from_string('C4CED0');r.font.size=Pt(9)

# Guias do apresentador: texto idêntico às notas, uma frase por parágrafo.
for part in [1,2]:
 spec=json.loads((R/f'parte{part}_v1.json').read_text());d=document(11.5)
 for start in range(0,len(spec['slides']),2):
  if start:d.add_page_break()
  if start==0:
   caption(d,'TRADUZINDO O SER HUMANO')
   para(d,f'M2.4 · Parte {part}', 'Title')
   para(d,'Compreensão e fundamentos' if part==1 else 'Prática guiada e integração')
  for s in spec['slides'][start:start+2]:
   para(d,f"Slide {s['number']}  {s['title']}",'Heading 2')
   p=para(d,s['moment'].upper());p.paragraph_format.keep_with_next=True
   for run in p.runs:run.font.size=Pt(8);run.font.color.rgb=RGBColor.from_string('245E78');run.bold=True
   for line in s['notes'].split('\n'):
    p=para(d,line);p.paragraph_format.space_after=Pt(2 if line else 4)
    if not line:p.paragraph_format.line_spacing=0.25
    if line=='PAUSA':
     for r in p.runs:r.bold=True;r.font.color.rgb=RGBColor.from_string('A8743C')
 d.save(OUT/f'TSH_M2_4_Parte_{part}_Guia_de_gravacao_v1.docx')

# Apoio autônomo do aluno.
d=document(11)
caption(d,'TRADUZINDO O SER HUMANO  ·  MÓDULO 2  ·  AULA 4')
para(d,'O que mantém a repetição de uma resposta?','Title')
para(d,'Síntese da aula, prática e registro para acompanhar a vida.')
heading(d,'Uma compreensão nova precisa encontrar sustentação')
para(d,'Uma pessoa pode compreender uma situação de outra maneira e continuar sentindo, antecipando e respondendo de um modo conhecido. Investigar essa diferença permite reconhecer o que mantém uma resposta e o que pode abrir outra participação: uma experiência, uma capacidade, um apoio ou uma mudança nas condições.')
para(d,'Na M2.1, acompanhamos a formação da percepção. Na M2.2, a relação entre forma sensível e elaboração. Na M2.3, a força de certeza de uma interpretação e sua conferência. Nesta aula, perguntamos o que ficou disponível para viver e fazer depois dessa compreensão.')
para(d,'Em um exemplo cotidiano, uma pessoa sabe que pode negociar as condições de um trabalho. Diante de um novo pedido com prazo apertado, sente aperto, imagina decepcionar e aceita depressa. O alívio vem agora. Depois aparecem a sobrecarga e a falta de espaço para o descanso ou uma criação própria. Precisamos investigar também o risco, a história da relação e a margem real de negociação.')
image(d,'escada.png',7.2)
caption(d,'Ver uma passagem e encontrar condições de percorrê-la são trabalhos diferentes. A escada permite perguntar por posição de partida, passos e apoios. Fotografia @scripz, acervo visual TSH.')

page(d,'O que se organiza antes da resposta')
para(d,'Chamamos de configuração a maneira como corpo, afeto, imagem, memória, elaboração, relação e participação se articulam numa ocasião. Uma imagem de decepção pode acompanhar o aperto; a explicação “vou perder meu lugar” pode intensificá-lo; aceitar pode trazer alívio e influenciar a próxima ocasião. Essa organização é uma parte da experiência, e não uma definição da pessoa.')
para(d,'Nos dois tempos da Tradução, algo encontra forma como sensação, afeto, imagem ou disposição, e procuramos elaborar o que vivemos. No mapa funcional dos Eus, o Eu Básico participa da forma sensível e das referências aprendidas; o Eu Médio nomeia, relaciona, raciocina e orienta escolhas. O diálogo entre essas funções permite investigar a distância entre compreender uma alternativa e conseguir vivê-la.')
para(d,'Bion contribui para pensar como a experiência emocional se torna disponível ao pensamento. Reconhecer “tenho receio de perder meu lugar se negociar” dá contorno a uma urgência antes pouco diferenciada. Uma escuta que acolhe, uma imagem, um gesto ou uma palavra pode participar desse trabalho. A precisão importa pelo que ajuda a sentir, compreender e sustentar.')
image(d,'circularidade.png',16.8)
caption(d,'A expectativa orienta a participação. Os efeitos do encontro podem reforçar ou modificar a expectativa. Diagrama didático do TSH em diálogo com a recursividade de Morin.')
para(d,'Ao aceitar repetidamente sem conversar, a pessoa pode levar o outro a contar com essa disponibilidade. Investigar a participação ajuda a localizar possibilidades de ação. O outro permanece responsável por sua conduta, e as imposições externas precisam entrar na compreensão do processo.')

page(d,'Função, expressão e condições concretas')
para(d,'Uma resposta pode preservar renda, vínculo, continuidade ou uma referência conhecida. Pode também seguir um costume ou evitar um risco real. Sua função precisa ser investigada em cada situação. Algumas restrições foram impostas e nunca protegeram a pessoa.')
para(d,'A pergunta inclui o que fica sem expressão: descanso, desejo, criação, limite, contribuição e sentido. No TSH, esse horizonte se relaciona ao reconhecimento, à integração e à expressão das possibilidades da Essência nas condições concretas da singularidade. Uma possibilidade de ser pode pedir apoio e cultivo, mesmo quando ainda não aparece como um problema definido.')
para(d,'O estudo de Milgram publicado em 1963 ajuda a manter a autoridade e a situação dentro da pergunta. Quarenta homens acreditavam aplicar choques crescentes num contexto de pesquisa. O aprendiz era colaborador e não recebia as descargas anunciadas. Vinte e seis participantes chegaram ao nível máximo indicado; quatorze interromperam antes. Muitos dos que continuaram demonstraram tensão. O resultado pertence àquela condição experimental e permite distinguir conflito vivido de interrupção da ação.')
para(d,'No cotidiano, precisamos conhecer quem decide, o que acontece diante da discordância e que alternativas existem. Uma condição interna de segurança precisa encontrar a realidade da relação.')
table(d,['O que investigar','O que isso pode exigir'],[
 ('Pessoa','Capacidade de permanecer na conversa; estado e acesso às referências já desenvolvidas.'),
 ('Relação','Informação sobre acordos, autoridade, consequências, apoio e possibilidade de discordância.'),
 ('Condições','Tempo, descanso, renda, recursos, alternativas e mudanças materiais necessárias.')],[4,13.3])
para(d,'No exemplo do prazo, a pessoa pode precisar aprender a negociar. Pode também precisar obter informação, construir apoio, rever um acordo ou preparar uma saída. A investigação do vivido ajuda a reconhecer qual trabalho faz sentido.')

page(d,'Estado, percurso e recurso pertinente')
image(d,'pendulo_espiral.png',16.8)
caption(d,'O pêndulo acompanha variações numa ocasião. A espiral permite comparar reencontros, condições e participação. Adaptação de foco do mapa mestre do TSH, com suas cores semânticas preservadas.')
para(d,'Numa conversa, posso passar da abertura à pressa e recuperar alguma referência. Em outra conversa, posso sentir tensão semelhante e conseguir pedir tempo. Compare as ocasiões junto de descanso, informação, autonomia, apoio e risco. O retorno de um tema deixa aberta a pergunta sobre o que foi aprendido.')
para(d,'Aprendizagens podem aparecer como prontidão antes de uma explicação consciente. Isso sustenta capacidades e também respostas que hoje restringem possibilidades. Cozolino contribui para compreender a aprendizagem implícita; Kahneman, a participação do familiar no julgamento. Antecipar também permite habilidade, adaptação e continuidade.')
para(d,'Um recurso ajuda a perceber, sustentar ou realizar uma possibilidade naquela situação. Se a pessoa aceita antes de conferir o prazo, pode precisar permanecer na conversa enquanto consulta a agenda. A firmeza vivida numa relação confiável pode oferecer referência para um ensaio. Informação ausente precisa ser obtida; habilidade ainda não desenvolvida pede aprendizagem.')
para(d,'Na prática, a referência é pertinente pelo que permite viver e sustentar. Uma imagem pode oferecer apoio se ganhar alguma presença na experiência. A tensão pode continuar e, ainda assim, existir maior condição de escutar e responder. O ensaio permite conferir essa diferença.')

page(d,'A prática: reconhecer, retornar, dar presença e reencontrar')
para(d,'Esta exploração dialoga com o metapadrão desenvolvido por Melissa Tiers na hipnose integrativa. No TSH, os quatro passos apoiam investigação, elaboração e participação. Forghieri contribui com a alternância entre envolvimento na experiência e reflexão que mantém vínculo com o vivido.')
para(d,'Prepare um lugar para registrar e reconheça uma referência de retorno: ambiente, apoios do corpo e movimentos. Escolha algo que consiga acompanhar agora. Pode manter os olhos abertos, adaptar ou interromper. Reserve a prática para um momento em que não esteja dirigindo nem realizando uma atividade que exija atenção ao ambiente.')
para(d,'Escolha uma ocasião recente em que compreendia uma alternativa e respondeu de maneira conhecida. Registre o acontecimento, a alternativa e o começo que vai acompanhar. Conserve a mesma situação durante a exploração.')
para(d,'1. Reconhecer. Aproxime brevemente o instante anterior à resposta. O que viu, ouviu ou imaginou? Como esse começo é vivido agora? Registre “Início — vivido”. Em seguida, reconheça que resposta se impunha e que alternativa era difícil de sustentar. Registre “Início — participação”.')
para(d,'2. Retornar. Deixe a cena de lado. Reconheça o ambiente, os apoios e algum movimento. Dê tempo para recuperar outras referências. Se a cena continuar tomando todo o campo, mantenha o retorno e encerre a aproximação. Pode acompanhar o restante sem voltar à cena.')
para(d,'3. Dar presença ao recurso. Procure uma experiência em que conseguiu sustentar uma qualidade pertinente à alternativa. Aproxime sua expressão no corpo, no ritmo, na imagem ou na relação. Confira o apoio que fica disponível. Se nenhum recurso estiver acessível, registre a necessidade de apoio ou aprendizagem e siga sem reencontrar a cena.')
para(d,'4. Reencontrar. Com recurso acessível e disponibilidade, aproxime apenas o mesmo começo. Registre como é vivido agora em “Reencontro — vivido”. Depois acompanhe o gesto ou resposta que consegue sustentar e registre “Reencontro — participação”. Se perder o apoio, deixe a cena e retorne. A resposta da outra pessoa ainda será conhecida na vida real.')
para(d,'Retorne ao presente. Compare primeiro os dois registros do vivido e depois os dois da participação. Reconheça diferenças, permanências e o que impediu continuar, se for o caso. Conclua deixando a questão de lado, reconhecendo o ambiente e retomando os movimentos. Depois elabore o que observou.')

page(d,'Registro da exploração')
para(d,'Use esta página junto da prática ou conserve os mesmos nomes na sua Cartografia. Os registros descrevem como a ocasião é vivida ao ser retomada agora. Palavras, desenhos e imagens podem ajudar a expressar a experiência.')
lines(d,'Situação escolhida e alternativa já compreendida',2)
lines(d,'Começo que será acompanhado: o que chegou logo antes?',1)
table(d,['Início — vivido','Reencontro — vivido'],[('\n\n\n\n','\n\n\n\n')],[8.65,8.65])
para(d,'Compare o vivido: o que mudou e o que permaneceu?')
lines(d,'',1)
table(d,['Início — participação','Reencontro — participação'],[('\n\n\n\n','\n\n\n\n')],[8.65,8.65])
para(d,'Compare a participação: o que se impunha e o que conseguiu sustentar?')
lines(d,'',1)
lines(d,'Recurso escolhido, sua função e o apoio que ficou disponível',2)
caption(d,'Se não houve reencontro, registre até onde foi possível acompanhar e o que faltou. O registro conserva a investigação sem exigir um resultado de mudança.')

page(d,'Do ensaio ao encontro real')
para(d,'Compreensão, vivido e participação podem mudar de maneiras diferentes. A diferença observada ajuda a escolher a continuidade. Ela precisa ser compreendida junto do recurso usado, do momento e das condições.')
table(d,['O que apareceu','Como o trabalho pode continuar'],[
 ('Capacidade disponível','Escolher onde experimentar e acompanhar seus efeitos.'),
 ('Possibilidade ainda frágil','Cultivar com tempo, experiência e apoio.'),
 ('Algo impediu continuar','Investigar pertinência do recurso, capacidade ainda por construir ou condição que precisa mudar.')],[5.3,12])
para(d,'Escolha um passo que caiba nas condições atuais e indique sua sustentação. Depois do encontro, acompanhe a própria participação, a resposta do outro e as consequências. Essas informações podem ampliar ou corrigir o ensaio. Quando o tema voltar, considere também o que mudou nas condições.')
table(d,['Campo da Cartografia','O que conservar'],[
 ('Situação','Acontecimento, relação, condições e o que está em jogo.'),
 ('Manifestação','Vivido e participação, no início e no reencontro.'),
 ('Tradução provisória','Compreensão da configuração e questões ainda por conferir.'),
 ('Orientação possível','Recurso, cultivo, apoio, limite ou mudança de condição.')],[5.3,12])
lines(d,'Meu próximo passo e as condições para realizá-lo',2)
lines(d,'Depois do encontro: como participei, como o outro respondeu e que efeito apareceu?',2)
para(d,'Na M2.5, vamos diferenciar acontecimento, experiência e interpretação. Uma sensação ou imagem pode produzir efeitos relevantes e ainda deixar em aberto sua origem e o que permite concluir.')

page(d,'Para investigar mais')
para(d,'A Tradução, a finalidade ligada à Essência e à singularidade e a articulação dos mapas integram a elaboração autoral do TSH. Eu Básico e Eu Médio dialogam com a Huna moderna de Max Freedom Long e descrevem funções nesse mapa. Essas funções não correspondem a regiões cerebrais. As fontes abaixo iluminam questões distintas; o ensaio educacional não demonstra, por si, uma mudança neural específica ou reconsolidação da memória.')
refs=[
('Bion, W. R. Learning from Experience. London: Heinemann, 1962.','A experiência emocional tornando-se disponível ao pensamento. Registro da obra: https://melanie-klein-trust.org.uk/resources/learning-from-experience/'),
('Forghieri, Y. C. Psicologia fenomenológica: fundamentos, método e pesquisas. São Paulo: Pioneira Thomson Learning, 2004.','Envolvimento existencial e distanciamento reflexivo, com retorno ao vivido para conferir a descrição.'),
('Morin, E. Introdução ao pensamento complexo. Porto Alegre: Sulina, 2005.','A recursividade ajuda a examinar como efeitos também participam da continuidade de um processo.'),
('Cozolino, L. Why Therapy Works: Using Our Minds to Change Our Brains. New York: W. W. Norton, 2016.','Aprendizagem implícita e participação das relações na transformação. A aplicação à aula é uma articulação educacional do TSH.'),
('Kahneman, D. Rápido e devagar: duas formas de pensar. Tradução de Cássio de Arantes Leite. Rio de Janeiro: Objetiva, 2012.','Contribuição para investigar familiaridade e julgamento. Os dois sistemas são um modelo funcional, sem equivalência anatômica direta.'),
('Kahneman, D.; Klein, G. Conditions for intuitive expertise: a failure to disagree. American Psychologist, 64(6), 515–526, 2009.','Aprendizagem de regularidades e retorno dos efeitos na intuição especializada. DOI: https://doi.org/10.1037/a0016755'),
('Milgram, S. Behavioral study of obedience. Journal of Abnormal and Social Psychology, 67(4), 371–378, 1963.','Procedimento, amostra e condição histórica apresentados na aula. DOI: https://doi.org/10.1037/h0040525'),
('Tiers, M. Integrative Hypnosis: A Comprehensive Course in Change. 2010, cap. 14.','Metapadrão em diálogo com o trabalho de John Overdurf, retomado junto do repertório de hipnose do TSH.')]
for ref,contribution in refs:
 p=para(d,ref)
 for r in p.runs:r.bold=True;r.font.size=Pt(10)
 p=para(d,contribution)
 for r in p.runs:r.font.size=Pt(10)
d.save(OUT/'TSH_M2_4_Apoio_do_Aluno_v1.docx')
print('3 documentos criados')
