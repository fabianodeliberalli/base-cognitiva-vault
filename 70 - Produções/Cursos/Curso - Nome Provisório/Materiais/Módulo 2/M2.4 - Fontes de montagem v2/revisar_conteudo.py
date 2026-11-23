from pathlib import Path
import json,hashlib,copy
R=Path(__file__).resolve().parent
p1=json.loads((R/'fontes/parte1_v1.json').read_text());p2=json.loads((R/'fontes/parte2_v1.json').read_text())
for i,s in enumerate(p1['slides']):s['previous_index']=i
def notes(number,text):p1['slides'][number-1]['notes']=text.strip()
notes(4,'''O corpo se prepara, uma imagem antecipa decepção e o pensamento diz “vou perder meu lugar”.
Essa organização participa do que a pessoa consegue perceber e fazer.
Também entram o tom do pedido, quem decide e a história da relação.

Chamamos de configuração essa maneira de os elementos se articularem numa ocasião.
Uma parte pode reforçar outra: o aperto dá força à imagem de ameaça, e a imagem intensifica a urgência.
Aceitar pode aliviar esse conjunto por um instante.

Uma explicação nova pode modificar a leitura e ainda alcançar pouco essa organização.
Por isso vamos acompanhar tanto o que a pessoa compreende quanto a maneira de viver e participar do encontro.''')
notes(5,'''Nos dois tempos da Tradução, algo ganha forma na experiência e procuramos elaborar o que vivemos.
No mapa funcional apresentado, o Eu Básico participa da sensibilidade, das imagens e das referências aprendidas.
O Eu Médio nomeia, relaciona, raciocina e orienta escolhas.

Posso sentir conscientemente um aperto e ainda não encontrar palavras para compreendê-lo.
Uma imagem pode acrescentar algo à primeira explicação, e uma palavra mais precisa pode modificar o que consigo sentir.
Essas funções se entrelaçam.

Ao pensar “é possível negociar”, posso continuar vivendo o pedido como risco de rejeição.
A questão é como essa possibilidade alcança a experiência e encontra sustentação.
O mapa ajuda a acompanhar esse diálogo, sem separar a pessoa em duas partes independentes.''')
notes(6,'''Às vezes, percebemos apenas aperto e urgência para responder.
Ao acompanhar essa experiência, podemos reconhecer receio, vergonha, raiva ou algo ainda difícil de nomear.

O psicanalista Wilfred Bion investigou como aprendemos com a experiência emocional.
Sua contribuição aqui é compreender como impressões sensíveis e emocionais encontram formas que permitem pensá-las.

“Tenho receio de perder meu lugar se negociar” dá um contorno à pressão.
Podemos investigar o que esse receio reúne, como se manifesta e o que na relação atual o sustenta.
Uma escuta que acolhe, uma imagem, um gesto ou uma palavra pode ajudar nesse trabalho.

Se a nova frase explica a pressão, mas a pessoa continua sem conseguir acompanhá-la, a elaboração precisa continuar.
O retorno ao vivido permite conferir o que de fato ganhou forma e o que ficou disponível.''')
new8={'previous_index':3,'title':'Como o passado participa do que parece presente?','moment':'Cozolino e a formação da experiência','notes':'''Ao receber um pedido, uma pessoa pode já se sentir em falta e se preparar para concordar.
Quando procura explicar essa resposta, encontra uma experiência que começou a se organizar antes dessa explicação.

Cozolino chama de “meio segundo vital” a diferença de tempo com que descreve processos rápidos e o acesso consciente à experiência.
Durante esse processamento, referências da memória, do corpo e das emoções participam da formação do presente.
Na relação, uma expectativa de perder o lugar pode orientar como o pedido é recebido.

O ponto para nossa investigação é que a experiência já pode chegar à reflexão com uma direção que parece evidente.
O intervalo apresentado pelo autor é aproximado; não funciona como um relógio igual para toda percepção ou escolha.

Que parte dessa organização responde às condições deste encontro?
Que parte reencontra algo aprendido, e o que ainda não conseguimos distinguir?
Essas perguntas mantêm a história e a realidade atual dentro da investigação.''','edits':{'configuration':'Sentido\nque se forma','dimension-0':'Memória e associações','dimension-1':'Corpo e afeto','dimension-2':'Expectativas','dimension-3':'Relação atual','not-identity':'Meio segundo vital · Cozolino'}}
new9={'previous_index':1,'title':'Como uma impressão ganha o aval da certeza?','moment':'Cozolino, Kahneman e a Tradução','notes':'''Retomemos a pessoa que já se sente em falta diante do pedido.
“Estou sentindo culpa” e “tenho uma dívida com essa pessoa” oferecem pontos de investigação diferentes.
Uma experiência sentida pode ganhar o estatuto de descrição do que aconteceu.

Kahneman ajuda a investigar esse aval dado às impressões e às associações disponíveis.
O pensamento pode conferir suas bases ou encontrar explicações que as mantenham.
Como vimos na M2.3, a busca de confirmação pode estreitar ainda mais o campo.

Na articulação com Cozolino, acompanhamos a formação da experiência e a elaboração que pode confirmá-la ou modificá-la.
São contribuições de recortes diferentes, em diálogo com os dois tempos da Tradução.

Sentir culpa merece investigação, e os acordos precisam ser conhecidos para avaliar se algo foi descumprido.
O corpo vivido e a conferência da situação oferecem informações que precisam conversar.
Compreender melhor pode modificar a experiência ou mostrar o que ainda falta para sustentar outra resposta.''','edits':{'reading-label':'EXPERIÊNCIA SENTIDA','reading':'“Sinto que\ndecepcionei.”','lived-label':'CONCLUSÃO SOBRE O ENCONTRO','lived':'“Eu decepcionei.”','investigation':'O que foi vivido?\nQue pistas sustentam a conclusão?'}}
old8=p1['slides'][7]
old8['title']='Aprender modifica o que se torna disponível'
old8['notes']='''Essa formação rápida da experiência também participa de capacidades desenvolvidas.
No shakuhachi, escuta, sopro e gesto podem se articular sem explicar cada ajuste enquanto ele acontece.
O aprendizado refina o que se percebe e como se responde.

Kahneman e Gary Klein investigaram condições em que a intuição especializada se desenvolve.
Oportunidades de aprender regularidades e receber retorno sobre os resultados fazem diferença.
Apenas repetir uma resposta ou sentir muita confiança não garante precisão.

No TSH, isso permite retomar a competência incorporada e o retorno com aquisição.
Uma compreensão trabalhada na experiência pode passar a participar do que fica disponível diante de uma nova ocasião.
O cultivo acompanha os efeitos, os apoios e as condições em que essa possibilidade se sustenta.

Precisamos distinguir uma capacidade existente pouco acessível, uma habilidade ainda por desenvolver e uma condição externa que pede mudança.'''
old8['edits']={'both':'Habilidades refinadas\nRespostas conhecidas','learn':'Aprender, experimentar e conferir os efeitos.'}
p1['slides']=p1['slides'][:7]+[new8,new9]+p1['slides'][7:]
p1['slides'][17]['notes']='''Este é o percurso da prática que será conduzida no segundo vídeo.
Primeiro reconhecemos o início de uma resposta conhecida.
Depois retornamos a outras referências, damos presença a um recurso e reencontramos o começo com esse apoio.

Essa organização dialoga com o metapadrão trabalhado por Melissa Tiers na hipnose integrativa.
Vamos investigar o que se modifica quando a situação encontra outra sustentação vivida.
O recurso precisa ser pertinente à alternativa e ganhar alguma presença na experiência.

Conferiremos tanto o vivido quanto a participação que se torna possível, inclusive quando não aparece mudança.
O ensaio oferece uma referência, e seus efeitos precisam ser acompanhados nas condições reais.

Aqui estamos conhecendo o percurso.
As instruções de realização estarão no vídeo da prática.'''
# A antiga tela 16 ocupa o índice 17; a antiga tela 17 ocupa o índice 18.
percurso=p1['slides'][17]['notes']
p1['slides'][17]['notes']='''Um recurso ajuda a perceber, sustentar ou realizar uma possibilidade naquela situação.
Sua função orienta a escolha.

Na negociação do prazo, pode ser conseguir permanecer na conversa enquanto consulta a agenda.
A firmeza vivida numa relação confiável pode oferecer uma referência para esse ensaio.
Falta de informação pede informação, e uma habilidade ainda não desenvolvida pede aprendizagem.

A questão é conferir se a referência de firmeza ganha presença diante do pedido.
A tensão pode continuar e surgir maior condição de escutar e responder.
Isso é diferente de apenas escolher uma frase mais adequada.

Uma capacidade interna, um apoio relacional e uma condição material podem precisar trabalhar juntos.
O ensaio vai ajudar a reconhecer o que ficou disponível e o trabalho que precisa continuar.'''
p1['slides'][18]['notes']=percurso
p2['slides'][14]['notes']='''A experiência pode ter mudado sem eliminar toda a tensão.
Talvez tenha surgido maior condição de sustentar uma pergunta ou um limite.

A comparação distingue compreender uma alternativa, senti-la de outra maneira e conseguir dar sustentação a uma participação.
Essas diferenças ajudam a escolher por onde o trabalho continua.

Se a capacidade ficou disponível, vale escolher onde experimentá-la e acompanhar os efeitos.
Se apareceu e se perdeu facilmente, pode pedir cultivo, tempo e apoio.
Se algo impediu continuar, investigamos a pertinência do recurso, a capacidade necessária e as condições concretas.

Esse acompanhamento dá sentido ao retorno com aquisição.
Reconhecemos o que foi aprendido pelo que se torna mais disponível para perceber, sustentar e realizar.'''
p2['slides'][15]['notes']='''O ensaio oferece uma referência, e o encontro real traz informações que ainda não temos.
Na negociação de um prazo, conseguir permanecer na conversa precisa se articular com conhecer prioridades e formular uma proposta viável.

Um próximo passo pode ser consultar um acordo, preparar a conversa, buscar apoio ou reservar espaço para criar.
Depois acompanhamos como participamos, como o outro respondeu e que consequências apareceram.
Essas informações podem ampliar ou corrigir o ensaio.

É assim que o cultivo se relaciona com a aprendizagem.
Repetimos com atenção aos efeitos e às condições, ajustando o que não se sustenta.
O objetivo é ampliar o que se torna disponível para participar das próximas ocasiões.'''
for part,obj in [(1,p1),(2,p2)]:
 obj['version']='2.0';obj['date']='2026-11-23';obj['source_version']='1.0';obj.pop('native_sequence',None)
 for i,s in enumerate(obj['slides'],1):
  s['number']=i;s['notes']=s['notes'].strip();s['notes_sha256']=hashlib.sha256(s['notes'].encode()).hexdigest();s.pop('screen_text',None)
 (R/f'parte{part}_v2.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2))
 print(part,len(obj['slides']))
