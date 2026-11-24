from pathlib import Path
import json

R=Path(__file__).resolve().parent
S=[]
def slide(title,moment,notes,screen=None,**kw):
    S.append(dict(number=len(S)+1,title=title,moment=moment,notes=notes.strip(),screen=screen or {},**kw))

slide('O que cada pergunta destaca?','Apresentação', '''APRESENTAÇÃO DA PRÁTICA

Na primeira parte, acompanhamos como algo ganha importância e encontra uma forma de expressão.
Agora vamos experimentar como a pergunta participa desse processo.

Vamos guardar uma observação inicial e uma de cada pergunta para comparar depois.
O registro pode ser uma palavra, um traço ou a descrição de um gesto.

Reserve um momento em que possa dedicar atenção à prática.
Se estiver dirigindo, faça depois.
Você pode adaptar ou interromper quando precisar e guardar os registros só para você.

Primeiro vou mostrar um exemplo breve.
Depois começamos a sua exploração.''',{'practice-path':'Perceber o vivido\nMudar a pergunta\nLevar o aprendizado à vida'})

slide('Um convite para dançar','Demonstração', '''DEMONSTRAÇÃO

Vamos imaginar um convite para dançar.
Antes de decidir, uma pessoa pode reconhecer vontade de ir e um movimento de se recolher.
Isso já pode aparecer num gesto, sem uma explicação pronta.

Ao perguntar o que precisa resolver, ela percebe o horário disponível e uma tensão nos ombros ao pensar em se expor.
Com a pergunta sobre uma possibilidade de vida, pode reconhecer o prazer de se mover e o mesmo receio de exposição.

Estamos acompanhando o que cada pergunta tornou perceptível e como isso foi vivido.
As observações podem se sobrepor e nenhuma precisa ser mais positiva.
São possibilidades deste exemplo, e a sua experiência pode seguir outro caminho.

O exemplo termina aqui.
Agora vamos começar pela sua situação.''',visual='Três observações lado a lado, sem direção de progresso.',origin='cópia adaptada da tela de comparação da prática v1')

slide('Escolha uma situação','Início da realização', '''PRÁTICA

Retome uma situação da aula anterior ou escolha algo que queira acompanhar agora.
Pode ser uma relação, uma criação ou uma direção importante para você.
Escolha algo que consiga explorar neste momento.

Situe em uma frase o que está acontecendo.
Essa será a mesma situação ao longo da prática.

Pause o vídeo para escolher e retome quando terminar.

PAUSA''')

slide('Antes das perguntas','Realização', '''Traga a situação escolhida à atenção.
Como é estar diante dela agora?

Acompanhe o que aparece em você antes de procurar explicar.
Pode chegar uma sensação, um afeto, uma imagem, uma palavra ou uma vontade de se mover.
Fique com o que conseguir reconhecer.

Guarde uma expressão breve dessa experiência com o nome “Antes das perguntas”.
Se usar uma palavra, confira se ela corresponde ao que percebe.

Pause o vídeo para perceber e registrar.
Retome quando terminar.

PAUSA''',{'receive':'Como é estar\ndiante dessa situação?','receive-support':'Uma expressão breve\ndo que você reconhece.','pause-cue':'Pause para perceber e registrar.'})

slide('Resolver','Realização', '''Mantenha a mesma situação.
Pergunte: o que eu preciso resolver aqui?

Dê tempo para perceber o que essa pergunta traz.
Além da resposta em palavras, acompanhe como é estar diante disso agora.

Guarde uma expressão breve com o nome “Resolver”.

Pause o vídeo para perceber e registrar.
Retome quando terminar.

PAUSA''')

slide('Possibilidade','Realização', '''Volte à mesma situação com esta outra pergunta.
Que possibilidade de vida procura expressão aqui?

Permaneça um pouco com essa pergunta.
Perceba também como você se sente e se dispõe diante dessa situação.
Pode surgir algo diferente, continuar parecido ou ainda ficar sem resposta.

Guarde uma expressão breve com o nome “Possibilidade”.

Pause o vídeo para perceber e registrar.
Retome quando terminar.

PAUSA''')

slide('O que mudou e o que permaneceu?','Comparação', '''Retome as três observações: Antes das perguntas, Resolver e Possibilidade.

Compare o que ganhou destaque e como você viveu cada aproximação.
Houve diferença no corpo, no afeto, na imagem ou no impulso de agir que você reconheceu?
O que permaneceu?

As perguntas podem destacar aspectos diferentes ou conduzir à mesma necessidade.

Pause o vídeo para comparar.
Retome quando terminar.

PAUSA''',{'after-comparison':'O que ganhou destaque?\nComo foi vivido?'})

slide('A situação concreta','Conferência', '''Deixe as perguntas em segundo plano e volte à situação concreta.

O que mais precisa entrar nessa compreensão?
Considere o que você vive e também as pessoas, os acordos e as condições envolvidas.

Pode aparecer um acréscimo ou uma pergunta que ainda precisa de informação.
Conserve isso junto dos registros, se for útil.

Pause o vídeo para essa conferência.
Retome quando estiver pronto para concluir.

PAUSA''')

slide('Concluir a exploração','Encerramento', '''ENCERRAMENTO

Vamos concluir a exploração.
Deixe a situação de lado.
Reconheça o ambiente em que está agora.
Perceba os apoios do corpo e retome seus movimentos.

PAUSA

A exploração termina aqui.
Agora vamos elaborar o que foi possível reconhecer e pensar na continuidade.''')

slide('Dar forma permite continuar','Elaboração', '''ELABORAÇÃO

Uma expressão conserva algo que conseguimos reconhecer e permite trabalhar com ele.
Ao voltar ao vivido, conferimos se a palavra ou a imagem alcançou o que estava acontecendo.
É o diálogo entre forma vivida e elaboração que chamamos de dois tempos da Tradução.

A imagem do artesão ajuda a acompanhar esse movimento.
Enquanto dá forma, ele percebe diferenças que orientam o próximo gesto.
Na nossa investigação, a expressão também pode ser ajustada pelo contato com a experiência.

Resolver pode ter mostrado um compromisso que precisa ser cuidado.
Possibilidade pode ter revelado um desejo, um limite ou a importância de uma solução concreta.
Uma formulação permanece aberta ao que a situação ainda pode mostrar.

O que você reconheceu pede qual trabalho agora?''',visual='Imagem do artesão recuperada da teoria M2.2, com a função de expressão/conferência.',origin='M2.2 v0.5, tela 8')

slide('Uma próxima ação com retorno','Continuidade', '''CONTINUIDADE

Escolha uma próxima ação que utilize algo do que reconheceu.
Pode ser fazer uma pergunta numa conversa ou dar uma primeira forma a algo que deseja criar.

Defina o que vai fazer e em qual ocasião próxima.
Se for uma conversa, prepare a pergunta e deixe espaço para a resposta da outra pessoa.
Se for uma criação, reserve uma ocasião para experimentar um primeiro gesto, traço ou som.

Depois dessa experiência, volte ao registro.
O que conseguiu fazer e o que aconteceu em você e na situação?
Esse retorno mostra o que pede ajuste, mais prática ou outra condição.

Reconhecer uma possibilidade e começar a desenvolvê-la fazem parte do trabalho de expressar a singularidade na vida.''',visual='Registro de continuidade com ação, ocasião e retorno, sem escala de sucesso.',origin='adaptação da tela Cartografia da prática v1')

slide('A Cartografia conserva o percurso','Integração', '''INTEGRAÇÃO

Aproveite os registros na mesma Cartografia que já estamos construindo.

Na Situação, conserve o que escolheu e seu contexto.
Na Manifestação, guarde as três observações e o que percebeu ao compará-las.
Na Tradução provisória, escreva o que compreende e o que permanece por conferir.
Na Orientação possível, registre a próxima ação e a ocasião em que pretende realizá-la.

Quando voltar depois dessa experiência, acrescente o que ela mostrou.
Assim, o aprendizado continua no encontro com a vida e na expressão das possibilidades da Essência.

Na próxima aula, vamos investigar como uma interpretação ganha força de certeza e como conferir o que a sustenta.''')

spec={'lesson':'M2.2','part':2,'version':'2','date':'2026-11-24','pageId':'page_b4a2a7c376008191b2e89f8f7d1119b3','title':'O que cada pergunta destaca?','canvas':{'width':1280,'height':720},'slides':S,'sourceTheory':'M2.2 v0.5, parte teórica editada 28min13s','stableObservations':['Antes das perguntas','Resolver','Possibilidade'],'cartographyFields':['Situação','Manifestação','Tradução provisória','Orientação possível'],'status':'material-produzido','productionOrder':['M2.2 prática','M2.3 prática','M2.1 ajustes localizados','M2.4 duas partes','M2.5','M2.6','M1.6 prática','demais ajustes M0/M1','M3 em diante']}
(R/'m22_v2.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
lines=['# M2.2 — Prática guiada e integração v2','', '## Percurso','', 'Parte teórica editada preservada. A prática trabalha a relação entre pergunta, forma vivida, elaboração e uso na vida. A demonstração termina antes da escolha pessoal. Há três observações estáveis e os mesmos quatro campos da Cartografia.','']
for s in S:
    lines += [f"## Tela {s['number']} — {s['title']}",'',f"Momento: {s['moment']}.",'','```text',s['notes'],'```','']
(R/'M2.2 - Prática guiada - Trilha e notas v2.md').write_text('\n'.join(lines))
print('12 telas e notas compostas; palavras:',sum(len(s['notes'].split()) for s in S))
