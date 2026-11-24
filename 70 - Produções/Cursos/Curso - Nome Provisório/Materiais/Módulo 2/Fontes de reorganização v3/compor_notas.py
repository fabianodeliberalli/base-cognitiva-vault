from pathlib import Path
import json,re
R=Path(__file__).resolve().parent

def entry(source,title,notes,screen=None):return {'sourceIndex':source,'title':title,'notes':notes.strip(),'screenChanges':screen or {}}
M22=[
entry(1,'O que cada pergunta destaca?', '''APRESENTAÇÃO E DEMONSTRAÇÃO

Vamos experimentar como uma pergunta modifica o que percebemos e como vivemos a mesma situação.
Separe um lugar para registros breves e escolha um momento em que possa dedicar atenção à prática.
Você pode adaptar ou interromper; nesse caso, deixe a situação de lado e reconheça o ambiente.

Primeiro, um exemplo de convite para dançar.
Antes de decidir, uma pessoa pode sentir vontade de ir e um movimento de se recolher.
Ao perguntar o que precisa resolver, percebe o horário e a tensão de se expor.
Ao perguntar que possibilidade procura expressão, reconhece o prazer de se mover, junto do mesmo receio.
A pergunta muda o destaque; a experiência pode seguir outra direção.

O exemplo termina aqui.
Agora começamos pela sua situação.''',{'after-comparison':'O que cada pergunta torna perceptível?','pause-cue':'O exemplo termina antes da prática pessoal.'}),
entry(2,'A situação escolhida', '''INÍCIO DA PRÁTICA

Retome uma situação da aula anterior ou algo que queira acompanhar agora.
Pode ser uma relação, uma criação ou uma direção importante.
Escolha algo significativo que consiga explorar neste momento.

Situe em uma frase o que está acontecendo.
Mantenha essa mesma situação durante a prática.
Pause o vídeo para escolher e registrar.

PAUSA'''),
entry(3,'Antes das perguntas', '''Traga a situação à atenção.
Como é estar diante dela agora?
Acompanhe o que aparece no corpo, no afeto, nas imagens ou no impulso de agir.

Guarde uma expressão breve: palavra, traço ou descrição de um gesto.
Se usar uma palavra, confira se corresponde ao que percebe.
Identifique como “Antes das perguntas”.
Pause para perceber e registrar; retome quando terminar.

PAUSA'''),
entry(4,'Resolver', '''Mantenha a mesma situação e pergunte: o que eu preciso resolver aqui?
Dê um tempo para perceber o que a pergunta traz.
Acompanhe também como é estar diante disso.

Guarde uma expressão breve com o nome “Resolver”.
Pause para perceber e registrar.

PAUSA'''),
entry(5,'Possibilidade', '''Volte à mesma situação com outra pergunta.
Que possibilidade de vida procura expressão aqui?

Permaneça um pouco com a pergunta e acompanhe como se sente e se dispõe.
Pode surgir algo diferente, continuar parecido ou ficar sem resposta.
Guarde uma expressão breve com o nome “Possibilidade”.
Pause para perceber e registrar.

PAUSA'''),
entry(6,'Comparar e conferir a situação', '''Retome as três observações: Antes das perguntas, Resolver e Possibilidade.
Compare o que ganhou destaque e como viveu cada aproximação.
O que mudou e o que permaneceu?
As duas perguntas podem encontrar a mesma necessidade.

Agora confira a situação concreta.
Que pessoas, acordos ou condições ainda precisam entrar nessa compreensão?
Conserve o acréscimo ou a informação que falta conhecer.
Pause para comparar e conferir.

PAUSA''',{'after-comparison':'O que ganhou destaque? Como foi vivido?','pause-cue':'Confira também as pessoas, os acordos e as condições.'}),
entry(8,'Encerrar a exploração', '''ENCERRAMENTO

Deixe a situação de lado.
Reconheça o ambiente, perceba os apoios do corpo e retome seus movimentos.

PAUSA

A exploração termina aqui.
Vamos olhar para o que reconheceu e como continuar.'''),
entry(9,'Dar forma e continuar na vida', '''ELABORAÇÃO E CONTINUIDADE

Uma expressão conserva algo do vivido e permite trabalhar com ele.
Como o artesão, voltamos à forma e ajustamos o próximo gesto pelo que percebemos.
É o diálogo entre forma vivida e elaboração que chamamos de dois tempos da Tradução.

O que você reconheceu pede qual trabalho agora?
Escolha uma ação possível e uma ocasião: uma pergunta numa conversa ou um primeiro gesto de criação, por exemplo.
Se for conversar, deixe espaço para a resposta real.

Conserve as observações na Manifestação da Cartografia, a compreensão na Tradução provisória e a ação com sua ocasião na Orientação possível.
Depois de realizar, volte ao que aconteceu em você e na situação.
Esse retorno orienta ajustes e o cultivo das possibilidades da sua singularidade.
Na M2.3, vamos conferir como uma interpretação ganha força de certeza.''',{'form-expression':'Uma forma que\npermite reconhecer','form-return':'Uma próxima ação\nUma ocasião\nRetorno à experiência'})
]
M23=[
entry(0,'Conferir uma certeza e recuperar outras pistas', '''APRESENTAÇÃO E PREPARAÇÃO

Vamos conferir uma interpretação e acompanhar como vivemos a situação.
Guardaremos dois pares: Conclusão antes e depois; Vivido antes e depois.
A leitura pode se confirmar, mudar ou permanecer aberta.

Separe a Cartografia ou um caderno para registros breves.
Reserve um momento de atenção à prática; você pode adaptar ou interromper, retomando o ambiente e seus movimentos.
Primeiro vou demonstrar o procedimento.
Depois começamos a sua exploração.'''),
entry(3,'Uma pergunta que aceita surpresa', '''DEMONSTRAÇÃO

Uma pessoa apresenta uma proposta de trabalho e ouve: precisamos conversar melhor sobre isso.
Ela sente aperto e vontade de guardar a proposta: esse é o vivido.
“Minha proposta foi rejeitada” é a conclusão.
O vivido merece reconhecimento; a conclusão precisa de bases também no encontro.

“Por que você rejeitou minha proposta?” já inclui a rejeição como fato.
“Sobre quais pontos da proposta você quer conversar?” permite descobrir o que o outro tem a dizer.
A resposta pode confirmar a preocupação ou modificar a leitura.
Uma resposta imaginada ainda precisa de conferência.

O exemplo termina aqui.
Agora começamos pela sua situação.'''),
entry(4,'A situação escolhida', '''INÍCIO DA PRÁTICA

Escolha uma situação em que tenha chegado a uma conclusão bastante firme.
Pode retomar algo que já vem investigando e que consiga acompanhar agora.

Registre o que aconteceu e quem participava.
Mantenha a mesma situação até o fim.
Pause para escolher e situar o acontecimento.

PAUSA'''),
entry(5,'Conclusão antes', '''Volte à situação e complete: diante disso, concluí que...
Escreva a leitura que realmente vem sustentando.

Identifique como “Conclusão antes” e conserve para comparar depois.
Pause para registrar.

PAUSA'''),
entry(6,'Vivido antes', '''Ao trazer essa mesma situação à atenção, como é estar diante dela?
Acompanhe o que reconhece no corpo, no afeto, nas imagens ou no impulso de agir.

Guarde uma expressão breve, por palavra, desenho ou descrição de um gesto.
Identifique como “Vivido antes” e mantenha separado da conclusão.
Pause para perceber e registrar.

PAUSA'''),
entry(7,'Bases da conclusão e custo da revisão', '''Retome “Conclusão antes”.
Que pistas do acontecimento sustentam essa leitura?
Diferencie o que observou do que associou ou imaginou e anote o que falta conferir.

Se essa conclusão precisasse ser revista, o que isso colocaria em jogo?
Reconheça o que precisa de cuidado e o que pode pedir revisão.
Conserve essas observações junto da conclusão.
Pause para acompanhar essas questões.

PAUSA''',{'row-title-1':'Revisão e cuidado','row-body-1':'O que seria difícil rever?\nO que precisa de cuidado?','conserve-bases':'Conserve as bases e a informação que ainda falta.'}),
entry(9,'Retomar o presente', '''Deixe a situação de lado por um momento.
Olhe para onde está e reconheça um detalhe do ambiente.
Perceba o apoio dos pés ou do assento e ajuste a postura, se ajudar.
Deixe a respiração acontecer e permaneça um pouco nesse contato.

Para seguir, reconheça onde está e se há alguma disponibilidade para considerar a questão.
Pode continuar havendo tensão.
Se não houver disponibilidade, conclua por hoje retomando o ambiente e seus movimentos.
Pause e retome quando puder seguir.

PAUSA'''),
entry(10,'A informação que falta', '''Com algum contato com o presente, retome a mesma situação.
O que precisa saber para conferir sua conclusão?
Formule uma pergunta que aceite uma resposta diferente da esperada.

Se puder consultar a informação agora, confira e conserve o que encontrou.
Se depender de outra ocasião, guarde a pergunta e onde poderá buscar a resposta.
A informação ainda não obtida permanece em aberto.
Pause para essa conferência possível agora.

PAUSA'''),
entry(11,'Conclusão depois', '''Retome “Conclusão antes”.
Com o que foi possível conferir, o que consegue concluir agora?

Registre como “Conclusão depois”, incluindo as bases e o que ainda falta conhecer.
Compare as duas conclusões: a leitura pode mudar, continuar sustentada ou permanecer aberta.
Pause para registrar e comparar.

PAUSA'''),
entry(12,'Vivido depois', '''Volte à mesma situação: como é estar diante dela agora?
Guarde uma expressão breve como “Vivido depois”.

Compare com “Vivido antes”.
O que mudou e o que permaneceu?
Essa é a comparação do vivido, separada da comparação das conclusões.
Pause para perceber e registrar.

PAUSA'''),
entry(13,'Encerrar a exploração', '''ENCERRAMENTO

Deixe a situação e os registros de lado.
Reconheça o ambiente, perceba os apoios e retome seus movimentos.

PAUSA

A exploração termina aqui.
Agora vamos elaborar e organizar a continuidade.'''),
entry(15,'Conferir no encontro real', '''ELABORAÇÃO E CONTINUIDADE

Rever uma conclusão pode coexistir com o mesmo aperto.
O vivido e a compreensão podem mudar de maneiras diferentes.
Sustentar uma pergunta ou escutar algo inesperado já pode ampliar sua participação; o que continuar difícil orienta o próximo trabalho.

Se falta informação, defina fonte e ocasião para conferir.
Antes da conversa, retome o contato com o presente, faça a pergunta e escute a resposta real.
Se ficar dúvida, devolva brevemente o que entendeu e pergunte se corresponde ao que a pessoa quis dizer.

Na mesma Cartografia, conserve os pares de registros, as bases, a pergunta e a ocasião de retorno.
Depois do encontro, diferencie o que soube, o que ainda supõe e como viveu a situação.
Essa aprendizagem participa da expressão das suas possibilidades na vida.
M2.4 trabalhará o que continua organizando a resposta mesmo quando a compreensão mudou.''')
]
M24=[
entry(0,'Experimentar outra sustentação para responder', '''APRESENTAÇÃO E PREPARAÇÃO

Vamos acompanhar uma situação e experimentar um recurso que ajude a sustentar outra participação.
Guardaremos referências do vivido e da participação, no início e no reencontro.

Separe a Cartografia ou uma folha.
Reconheça o ambiente e os apoios do corpo.
Escolha um momento de atenção à prática; você pode manter os olhos abertos, adaptar ou interromper retomando o presente.
Pause o vídeo sempre que precisar de mais tempo para realizar ou registrar.

Agora começamos pela sua situação.'''),
entry(2,'Uma situação e uma alternativa já compreendida', '''INÍCIO DA PRÁTICA

Escolha uma ocasião recente em que compreendia uma alternativa e respondeu de maneira conhecida.
Pode retomar algo da sua Cartografia que consiga acompanhar agora.

Registre o que aconteceu e qual alternativa reconhecia.
Guarde o instante em que a resposta começa: reencontraremos esse mesmo começo.
Pause para escolher e registrar.

PAUSA'''),
entry(3,'Como esse começo é vivido?', '''Aproxime brevemente o instante anterior à resposta conhecida.
O que viu, ouviu ou imaginou logo antes?
Como esse começo é vivido agora?

Guarde uma expressão breve por palavras ou desenho, como “Início — vivido”.
Se estiver intenso demais, deixe a cena e retome o presente.
Pause para perceber e registrar.

PAUSA'''),
entry(4,'Que resposta esse começo organiza?', '''Ainda nessa ocasião, que resposta se impunha?
Que alternativa ficava difícil de sustentar?

Registre como tendia a participar, com o nome “Início — participação”.
Guarde ao lado de “Início — vivido”.
Pause para registrar; depois deixaremos a cena de lado.

PAUSA'''),
entry(5,'Retomar outras referências', '''Deixe a cena de lado.
Reconheça o lugar onde está, os apoios do corpo e algum movimento que ajude a retomar o presente.

Para seguir, reconheça onde está e alguma disponibilidade para considerar outra referência.
A tensão não precisa desaparecer.
Se a cena continuar tomando todo o campo, conserve o presente e acompanhe sem voltar a ela.
Pause para retornar.

PAUSA'''),
entry(6,'Uma experiência que ofereça sustentação', '''Agora procure uma ocasião em que conseguiu sustentar algo pertinente à alternativa.
Se precisa de firmeza, pode lembrar uma relação em que conseguiu manter sua posição sem perder o contato.
Escolha pela função que essa experiência pode oferecer.

Se nenhuma ocasião vier, procure uma experiência menor, de outra área da vida, em que tenha conseguido algo dessa qualidade.
Pode ter ocorrido numa criação, numa prática corporal ou com apoio de alguém.
O apoio não precisa ter sido produzido sozinho.

Situe uma ocasião concreta: onde estava, o que fazia e o que permitia participar daquele modo?
Anote a referência e o que ela ajudaria a sustentar nesta situação.
Pause para encontrá-la; depois vamos aproximar essa experiência.

PAUSA''',{'resource':'Sustentar\na alternativa','resource-0':'Uma ocasião concreta','resource-1':'Qualidade pertinente','resource-2':'Apoio recebido','resource-3':'Função nesta situação'}),
entry(7,'Dar presença à experiência de recurso', '''Deixe a situação difícil de lado e aproxime a experiência de recurso escolhida.
Reencontre como era participar naquela ocasião: a postura, o ritmo, a imagem ou a presença de alguém.
Perceba o que disso ganha alguma presença agora.

Se um gesto, uma posição ou uma palavra ajudava, experimente discretamente e confira se oferece apoio.
Permaneça um pouco com o que for reconhecível, sem precisar reproduzir a experiência inteira.

Que diferença esse apoio faz na sua disponibilidade para sustentar a alternativa?
Se continuar sendo apenas uma ideia, tente outra referência conhecida ou pause para retomar o Sorriso Interior, já ensinado no M1.3.
Ao voltar, confira se esse apoio ajuda a sustentar a alternativa escolhida.
Sentir algum alívio e conseguir participar pedem essa conferência.
Pause para acompanhar.
Se não houver apoio acessível, siga sem voltar à cena e conserve o que precisa ser aprendido ou buscado.

PAUSA''',{'resource-function':'Como esse apoio\nganha presença agora?','resource-action':'Experimente e confira\no que fica disponível.'}),
entry(8,'Reencontrar o começo com esse apoio', '''Se o recurso estiver acessível e houver disponibilidade, aproxime só o começo da mesma situação.
Conserve contato com o apoio.
Como aquele começo é vivido agora?

Guarde uma expressão como “Reencontro — vivido”.
Se perder o apoio ou a cena tomar conta, deixe-a de lado e retorne ao presente.
Pause para acompanhar e registrar.

PAUSA'''),
entry(9,'Que participação se torna possível?', '''Com esse apoio, que gesto ou resposta consegue sustentar diante daquele começo?
Confira como essa participação é vivida, além da frase que gostaria de dizer.

Registre como “Reencontro — participação”.
A resposta real da outra pessoa continua desconhecida.
Se não realizou o reencontro, conserve até onde acompanhou e o que faltou.
Pause para registrar.

PAUSA'''),
entry(10,'Encerrar a exploração e retomar o presente', '''ENCERRAMENTO DA EXPLORAÇÃO

Deixe a cena e o ensaio de lado.
Reconheça o ambiente, os apoios do corpo e retome seus movimentos.
Dê tempo para se localizar neste momento.

PAUSA

A exploração termina aqui.
Agora vamos olhar para os registros, sem voltar à cena.''',{'agency':'Disponibilidade\npara elaborar','cue-pause':'ENCERRAMENTO ANTES DA COMPARAÇÃO'}),
entry(11,'O que mudou no vivido?', '''Compare “Início — vivido” e “Reencontro — vivido”.
O que mudou e o que permaneceu na maneira de viver a mesma situação?

Registre a diferença que reconhece, mesmo pequena ou ausente.
Se não houve reencontro, conserve o que impediu continuar.
Pause para comparar os registros do vivido.

PAUSA'''),
entry(12,'O que mudou na participação?', '''Agora compare “Início — participação” e “Reencontro — participação”.
Que resposta se impunha e o que conseguiu sustentar no ensaio?

Conserve a diferença junto do apoio e das condições que participaram dela.
Uma intenção pode surgir sem ainda se tornar sustentação vivida.
Pause para comparar os registros da participação.

PAUSA'''),
entry(14,'Cada resultado orienta um trabalho diferente', '''ELABORAÇÃO

A tensão pode continuar e haver mais condição de sustentar uma pergunta ou um limite.
Compreender, viver de outro modo e conseguir participar oferecem referências diferentes.

Se a capacidade ficou disponível, escolha onde experimentá-la e acompanhe os efeitos.
Se apareceu e se perdeu facilmente, pode pedir cultivo, tempo e apoio.
Se algo impediu continuar, investigue a pertinência do recurso, uma habilidade a desenvolver ou condições externas que precisam mudar.

O ensaio oferece uma referência; o encontro real poderá ampliá-la ou corrigi-la.
A aprendizagem se mostra no que fica mais disponível para perceber, sustentar e realizar.'''),
entry(17,'Cartografia e continuidade na vida', '''Na Situação, conserve o acontecimento e as condições.
Na Manifestação, guarde vivido e participação, no início e no reencontro.
Na Tradução provisória, registre o que compreende e o que falta conferir.
Na Orientação possível, escolha uma ação, seus apoios e uma ocasião.

Depois do encontro real, volte aos registros: como participou, como o outro respondeu e o que aconteceu?
Se o tema voltar, compare as condições e a participação desta vez.
Essa é a contribuição da espiral: acompanhar diferenças sem presumir progresso.
O percurso inclui integrar e expressar possibilidades da Essência nas condições da sua vida.

M2.5 distinguirá acontecimento, experiência e interpretação.''')
]
for key,page,slides in [('M22','page_b4a2a7c376008191b2e89f8f7d1119b3',M22),('M23','page_85cb82566f6c8191a65ca24c77508761',M23),('M24P2','page_b9880588aff481919268e4851f70ab05',M24)]:
 d={'lesson':key,'version':'3','date':'2026-11-24','pageId':page,'slides':slides}
 for i,s in enumerate(slides,1):s['number']=i
 (R/(key+'_v3.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
 words=sum(len(re.findall(r'\b[\wÀ-ÿ]+(?:[’\'-][\wÀ-ÿ]+)*\b','\n'.join(l for l in s['notes'].splitlines() if not(l.isupper() and len(l)<60)))) for s in slides)
 print(key,len(slides),'telas',words,'palavras')
