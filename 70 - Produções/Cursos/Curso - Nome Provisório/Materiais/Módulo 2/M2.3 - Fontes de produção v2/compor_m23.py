from pathlib import Path
import json

R=Path(__file__).resolve().parent
S=[]
def step(title,moment,notes,source_index,screen=None,kind='existing'):
 S.append(dict(number=len(S)+1,title=title,moment=moment,notes=notes.strip(),sourceIndex=source_index,screen=screen or {},kind=kind))

step('Conferir uma certeza e recuperar outras pistas','Apresentação', '''APRESENTAÇÃO

Na primeira parte, investigamos como uma interpretação ganha força de certeza.
Agora vamos aprender a conferir essa leitura e acompanhar como vivemos a situação.

Ao final, teremos duas comparações: a conclusão antes e depois e o vivido antes e depois.
A leitura pode se confirmar, mudar ou permanecer em aberto.

Primeiro vou mostrar como distinguir esses registros e formular uma pergunta.
Depois começamos a sua exploração.''',0)

step('O percurso da prática','Preparação', '''PREPARAÇÃO

O mapa acompanha perceber, recuperar presença, diferenciar, orientar e aprender com o retorno.
Vamos percorrer esses movimentos numa mesma situação.

Separe um lugar para registros breves, na Cartografia ou no caderno.
Vamos guardar a conclusão e uma expressão do vivido, antes e depois.
Os registros podem permanecer só com você.

Reserve um momento em que possa dedicar atenção à prática.
Se estiver dirigindo, faça depois.
Você pode adaptar ou interromper quando precisar.
Se interromper, deixe a situação de lado, reconheça o ambiente e retome seus movimentos.

Vamos ver primeiro um exemplo.''',1)

step('Conclusão e vivido','Demonstração', '''DEMONSTRAÇÃO

Vamos usar o exemplo da proposta de trabalho.
Uma pessoa apresenta uma proposta e ouve: precisamos conversar melhor sobre isso.

Ela pode concluir que houve rejeição e sentir um aperto, com vontade de guardar a proposta.
“Minha proposta foi rejeitada” é a conclusão.
O aperto e o movimento de se retirar pertencem ao vivido.

O vivido precisa ser reconhecido.
Para conferir a conclusão, precisamos também conhecer o que foi dito e o que está acontecendo na relação.
Separar os registros permite perceber o que muda em cada um.

Como perguntar sem colocar a conclusão dentro da própria pergunta?''',12,kind='demo_records')

step('Uma pergunta que aceita surpresa','Demonstração', '''DEMONSTRAÇÃO

Quando a pessoa pergunta “por que você rejeitou minha proposta?”, a rejeição já entrou como fato.
“Sobre quais pontos da proposta você quer conversar?” permite descobrir o que o outro tem a dizer.

A resposta pode confirmar uma preocupação ou mostrar algo que ainda não havia sido considerado.
Fazer a pergunta e escutar a resposta oferecem informação para continuar.
Uma resposta apenas imaginada ainda precisa de conferência.

O exemplo termina aqui.
Agora começamos pela sua situação.''',8,kind='demo_question')

step('A situação escolhida','Início da realização', '''PRÁTICA

Escolha uma situação em que você tenha chegado a uma conclusão bastante firme.
Pode retomar algo que já vem investigando.
Escolha uma situação significativa que consiga acompanhar agora.

Registre brevemente o que aconteceu e quem participava.
Essa será a mesma situação durante toda a prática.

Pause o vídeo para escolher e situar o acontecimento.
Retome quando terminar.

PAUSA''',2)

step('Conclusão antes','Realização', '''Volte à situação que acabou de registrar.
Complete a frase: diante disso, concluí que...
Escreva a conclusão que você realmente vem sustentando.

Identifique como “Conclusão antes”.
Vamos voltar a esse registro no final.

Pause o vídeo para registrar.
Retome quando a conclusão estiver anotada.

PAUSA''',3,{'reading':'Conclusão\nantes'})

step('Vivido antes','Realização', '''Ao trazer essa mesma situação à atenção, como é estar diante dela?
Acompanhe o que aparece no corpo, no afeto, nas imagens ou no impulso de agir, conforme conseguir reconhecer.

Encontre uma expressão breve, por palavra, desenho ou descrição de um gesto.
Identifique como “Vivido antes”.
Guarde junto da conclusão, mantendo os dois registros reconhecíveis.

Pause o vídeo para perceber e registrar.
Retome quando terminar.

PAUSA''',4,{'record-name':'Registro: Vivido antes'})

step('As bases da conclusão','Realização', '''Retome “Conclusão antes”.
Que pistas do acontecimento sustentam essa leitura?
Há alguma diferença entre o que você observou e o que associou ou imaginou?

Anote as bases e o que ainda não tem como conferir.
Junte essas observações ao registro da conclusão.

Pause o vídeo para fazer essa conferência.
Retome quando terminar.

PAUSA''',5)

step('O que seria difícil rever?','Realização', '''Se essa conclusão precisasse ser revista, o que isso colocaria em jogo para você?
Dê tempo para reconhecer o que aparece.

Pode haver algo importante que procura cuidado ou preservação.
O que precisa de cuidado e o que pode pedir revisão?

Conserve o que fizer sentido junto das observações que já está reunindo.
Pause o vídeo e retome quando tiver acompanhado essa pergunta.

PAUSA''',6)

step('Retomar o presente','Realização', '''Deixe a situação de lado por um momento.
Olhe para o lugar onde está agora.
Reconheça um detalhe desse ambiente.
Perceba o apoio dos pés ou do assento, conforme sua posição.
Se ajudar, ajuste a postura e deixe a respiração acontecer.

Permaneça um pouco nesse contato.
O critério é reconhecer onde está e ter alguma disponibilidade para considerar a questão.
Pode continuar havendo tensão.

Se ainda não houver disponibilidade, deixe a situação de lado e conclua por hoje, retomando o ambiente e seus movimentos.

Pause o vídeo agora.
Retome quando tiver reconhecido o lugar, algum apoio e condições de seguir.

PAUSA''',7,{'questao-preservada':'Aqui,\nagora'})

step('A informação que falta','Realização', '''Conserve algum contato com o ambiente e retome a mesma situação.

O que você precisaria saber para conferir sua conclusão?
Formule uma pergunta que permita descobrir essa informação e aceite uma resposta diferente da esperada.

Se puder consultar essa informação agora, confira e conserve o que encontrou.
Se depender de uma conversa ou de outra ocasião, guarde a pergunta e como pretende buscar a resposta.
O que ainda não foi obtido permanece em aberto.

Pause o vídeo para formular a pergunta e fazer a conferência possível agora.
Retome quando terminar.

PAUSA''',8)

step('Conclusão depois','Comparação da conclusão', '''Retome “Conclusão antes”.
Com o que foi possível conferir, o que você consegue concluir agora?

Registre como “Conclusão depois”, incluindo suas bases e o que ainda precisa conhecer.
Compare com a conclusão inicial.
Ela pode mudar, permanecer sustentada ou continuar em aberto.

Pause o vídeo para registrar e comparar.
Retome quando terminar.

PAUSA''',9)

step('Vivido depois','Comparação do vivido', '''Agora retome “Vivido antes”.
Ao voltar à mesma situação, como é estar diante dela neste momento?

Encontre uma expressão breve e registre como “Vivido depois”.
Compare os dois registros do vivido.
O que mudou e o que permaneceu?

Pause o vídeo para perceber, registrar e comparar.
Retome quando estiver pronto para concluir.

PAUSA''',10)

step('Encerrar a exploração','Encerramento', '''ENCERRAMENTO

Vamos concluir.
Deixe a situação e os registros de lado.
Reconheça o ambiente em que está.
Perceba os apoios do corpo e retome seus movimentos.

PAUSA

A exploração termina aqui.
Agora vamos elaborar o que essa comparação mostrou e como continuar.''',11)

step('O que a comparação mostrou?','Elaboração', '''ELABORAÇÃO

Uma conclusão revista pode coexistir com o mesmo aperto ou impulso de se retirar.
Também podemos viver a situação de outro modo e ainda precisar conferir sua interpretação.
A conclusão e o vivido podem mudar de maneiras diferentes.

Os dois tempos da Tradução ajudam a acompanhar essa relação.
A forma vivida participa da elaboração, e o que compreendemos volta à experiência para ser conferido.

Conseguir sustentar uma pergunta ou escutar algo inesperado já oferece uma possibilidade de participação.
O que permaneceu difícil mostra onde pode ser necessário outro recurso ou uma capacidade a desenvolver.
Na próxima aula, vamos trabalhar essa passagem com mais profundidade.''',12)

step('Conferir no encontro real','Continuidade', '''CONTINUIDADE

Se a pergunta ainda depende de outra ocasião, defina uma fonte e um momento possível para conferi-la.
Pode ser consultar um acordo ou conversar com quem participa da situação.

Se for conversar, retome primeiro algum contato com o ambiente e os apoios, como experimentamos aqui.
Faça a pergunta que preparou e escute a resposta que a pessoa realmente oferece.
Se ficar dúvida, devolva em poucas palavras o que entendeu e pergunte se corresponde ao que ela quis dizer.

Ao voltar ao registro, diferencie o que soube, o que continua supondo e como viveu esse encontro.
É esse retorno que permite aprender com a situação e rever a próxima participação.''',5,kind='real_check')

step('Registro e continuidade','Integração', '''INTEGRAÇÃO

Aproveite os registros na mesma Cartografia.

Na Situação, conserve o acontecimento e o contexto.
Na Manifestação, guarde “Vivido antes” e “Vivido depois”.
Na Tradução provisória, conserve a conclusão atual, suas bases e o que ainda falta conferir.
Na Orientação possível, registre a pergunta, onde poderá conferi-la e a ocasião de voltar ao resultado.

Depois do encontro real, acrescente o que ele mostrou, inclusive no seu modo de participar.
Esse trabalho dá continuidade ao reconhecimento e à expressão das possibilidades da Essência nas condições da sua vida.

M2.4 vai investigar o que mantém uma resposta conhecida, mesmo quando já compreendemos alguma coisa de outro modo.''',13)

spec={'lesson':'M2.3','part':2,'title':'Conferir uma certeza e recuperar outras pistas','version':'2','date':'2026-11-24','pageId':'page_85cb82566f6c8191a65ca24c77508761','canvas':{'width':1280,'height':720},'status':'material-produzido','sourceTheory':'M2.3 v0.3 e vídeo editado de 24min55s','stableRecords':['Conclusão antes','Vivido antes','Conclusão depois','Vivido depois'],'cartographyFields':['Situação','Manifestação','Tradução provisória','Orientação possível'],'slides':S,
'substantiveDevelopment':{
 'questao':'Como uma interpretação que organiza corpo, afeto e participação pode ser conferida sem apagar o vivido, e o que fica disponível depois dessa investigação?',
 'progressao':'M2.1 ensinou aproximação, forma expressiva e conferência. M2.2 investigou a participação da pergunta na relevância e na forma vivida. M2.3 acrescenta discriminar convicção e sustentação, recuperar presença suficiente, formular pergunta corrigível e comparar conclusão e vivido separadamente. M2.4 recebe o que continua organizado mesmo depois da revisão.',
 'ferramenta':'Distinguir e conservar conclusão e vivido, reconhecer bases e custo de revisão, reencontrar contato com presente, buscar informação e aprender com a resposta real. As comparações não exigem melhora ou mudança de opinião.',
 'fundamentos_em_uso':{
  'Tradução e Eus':'Forma vivida e elaboração se influenciam na convicção. A prática conserva cada dimensão e retorna a seus efeitos, sem equiparar o mapa autoral a anatomia ou aos sistemas de Kahneman.',
  'Kahneman e confirmação':'Conferir a sustentação da impressão e distinguir observação, associação e informação em aberto. Perguntar de modo que a resposta possa mudar a leitura, inclusive quando a primeira leitura era mais agradável.',
  'Festinger':'A pergunta sobre o que seria difícil rever alcança investimento, pertencimento e proteção. Reconhecer o custo da revisão não invalida uma convicção e não equivale a diagnosticar toda tensão como dissonância.',
  'Erickson e transe cotidiano':'Recuperar o que ficou significativo na experiência e abrir outra possibilidade de atenção e participação. Retomar ambiente e apoio amplia referências sem exigir calma ideal. A prática não mede transe nem demanda aprofundamento hipnótico.',
  'Mapa de retorno e espiral':'Preservar o mapa autoral e aprender com o reencontro, incluindo efeitos, capacidade de participar e necessidade de outro trabalho. Uma frase nova não representa por si aquisição incorporada.',
  'Naranjo e relação':'A conferência no encontro real acolhe uma resposta que corrige o entendimento. Devolver em poucas palavras e permitir correção deriva do trabalho de escuta do acervo, em desenvolvimento educacional TSH; não é um protocolo clínico nem uma transcrição de Naranjo.',
  'Essência e singularidade':'A finalidade é ampliar discernimento e participação para integrar e expressar possibilidades em condições corporais, afetivas, relacionais e materiais concretas, conservando a dimensão espiritual do TSH.'},
 'forma':'Demonstração breve termina antes da situação pessoal. Realização mantém referente, nomes e pausas. Encerramento antecede elaboração e continuidade. O material do aluno conserva os fundamentos e as duas imagens atuais.'}}
(R/'m23_v2.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
lines=['# M2.3 — Prática guiada e integração v2','','## Pergunta e percurso','',spec['substantiveDevelopment']['questao'],'',spec['substantiveDevelopment']['progressao'],'',spec['substantiveDevelopment']['ferramenta'],'']
for s in S:lines += [f"## Tela {s['number']} — {s['title']}",'',f"Momento: {s['moment']}.",'','```text',s['notes'],'```','']
(R/'M2.3 - Prática guiada - Trilha e notas v2.md').write_text('\n'.join(lines))
print('17 telas; palavras nas notas:',sum(len(s['notes'].split()) for s in S))
