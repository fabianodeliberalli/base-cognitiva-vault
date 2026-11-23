from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
def slide(src,title,moment,notes,edits=None):
 return dict(sourceIndex=src,title=title,moment=moment,notes=notes.strip(),edits=edits or {})
theory=[
slide(0,'O que mantém a repetição de uma resposta?','Abertura', '''Na M2.3, investigamos como uma interpretação ganha força de certeza.
Uma leitura pode mudar e o próximo encontro continuar sendo vivido de maneira parecida.

Nesta aula, vamos investigar o que mantém essa maneira de responder.
E o que precisa ganhar presença para que outra participação se torne possível.

Vamos reunir corpo, afeto, memória, elaboração, relação e condições concretas.
Esse trabalho inclui tanto cuidar de uma dificuldade quanto abrir espaço para um desejo, uma criação ou uma possibilidade de ser.
A prática será conduzida em um segundo vídeo.'''),
slide(1,'A compreensão mudou. O que continua acontecendo?','Questão da aula','''Uma pessoa reconhece que pode negociar as condições de um trabalho.
Mesmo assim, diante de um novo pedido, sente aperto e aceita depressa.

A M2.1 mostrou como a percepção se forma no encontro entre corpo, história e contexto.
A M2.2 aprofundou a forma sensível e a elaboração dessa experiência.
A M2.3 investigou a convicção e a conferência da interpretação.

Agora acompanhamos o que ficou disponível para viver e fazer.
A compreensão nova pode conviver com uma expectativa antiga e com condições que continuam iguais.
É essa diferença que vamos investigar.'''),
slide(2,'“Eu sabia que precisava conversar. Acabei aceitando.”','Exemplo e problema','''Vamos acompanhar um pedido de trabalho com prazo apertado.
A pessoa sabe que precisaria conferir suas condições antes de aceitar.

Ao ouvir o pedido, sente aperto, imagina decepcionar e quer encerrar a tensão.
Diz “pode deixar”.
O alívio chega agora, e a sobrecarga aparece depois.
Um trabalho próprio ou o descanso ficam sem espaço.

Também precisamos conhecer a relação e a margem real de negociação.
Uma ameaça, uma dependência financeira ou uma desqualificação anterior participam dessa resposta.
Quando ela aceita, uma organização inteira já está em curso.'''),
slide(3,'O que se repete é uma organização da experiência','Configuração','''O corpo se prepara, uma imagem antecipa decepção e o pensamento diz “vou perder meu lugar”.
Esses elementos se influenciam e participam do que parece possível fazer.
O tom do pedido, quem decide e a história da relação também entram nessa organização.

Vamos chamar de configuração essa maneira de os elementos se articularem numa ocasião.
Ela pode se repetir com diferenças e não resume quem a pessoa é.

Mudar uma explicação pode alcançar o conjunto de modos diferentes.
Por isso acompanhamos o efeito da compreensão no vivido e na participação.'''),
slide(4,'Compreender uma possibilidade e conseguir vivê-la','Dois tempos da Tradução','''Nos dois tempos da Tradução, algo ganha forma na experiência e procuramos elaborar o que vivemos.
No mapa funcional já apresentado, o Eu Básico participa da sensibilidade, das imagens e das referências aprendidas.
O Eu Médio nomeia, relaciona, raciocina e orienta escolhas.
São funções em diálogo nesse mapa.

Posso pensar “é possível negociar” e continuar vivendo o pedido como risco de rejeição.
A alternativa compreendida ainda encontra pouca sustentação vivida.
Uma palavra mais precisa, uma experiência de apoio ou outra condição pode participar desse trabalho.
Vamos conferir o que isso permite sentir, sustentar e realizar.'''),
slide(5,'Quando a pressão encontra uma forma que pode ser pensada','Bion em contribuição','''Às vezes, percebemos apenas aperto e urgência para responder.
Ao acompanhar essa experiência, podemos reconhecer receio, vergonha, raiva ou algo ainda difícil de nomear.

O psicanalista Wilfred Bion investigou como aprendemos com a experiência emocional.
Sua contribuição aqui é compreender como impressões sensíveis e emocionais encontram formas que permitem pensá-las.

“Tenho receio de perder meu lugar se negociar” oferece outra condição de investigação.
Podemos examinar esse receio e a realidade da relação.
Uma escuta que acolhe, uma imagem, um gesto ou uma palavra pode ajudar a dar forma ao vivido.
Nomear ganha valor quando amplia o contato e a elaboração da experiência.'''),
slide(6,'A resposta participa do encontro que virá depois','Circularidade','''Ao aceitar o prazo sem conversar, a pessoa pode levar o outro a contar com essa disponibilidade.
A expectativa organiza o gesto, o gesto participa da relação e o retorno do encontro influencia a próxima expectativa.

Edgar Morin ajuda a pensar essa recursividade: os efeitos também entram na continuidade do processo.
O alívio imediato pode favorecer a resposta conhecida, enquanto o custo aparece depois.
Um acordo nunca revisto ou uma exigência imposta também podem continuar operando.

Investigar nossa participação permite localizar possibilidades de ação.
O outro continua responsável por sua conduta.
Em algumas situações, o trabalho exige mudar condições da relação.'''),
slide(7,'O que foi aprendido pode chegar antes da explicação','Aprendizagem e disponibilidade','''Aprendizagens podem aparecer como prontidão, antes de explicarmos cada movimento.
Cozolino contribui para compreender a presença do aprendizado implícito nas relações e nas respostas atuais.
Kahneman ajuda a investigar a força do familiar no julgamento.

Isso também sustenta capacidades desenvolvidas.
No shakuhachi, escuta, sopro e gesto podem se articular sem uma explicação consciente a cada ajuste.
Antecipar permite continuidade e adaptação.

Uma forma conhecida de evitar conflito também pode chegar depressa quando as condições já mudaram.
O cultivo precisa considerar o que já existe, o que ficou pouco acessível e o que ainda pede aprendizagem.
As condições externas entram nessa avaliação.'''),
slide(8,'Ver uma passagem e encontrar condições de percorrê-la','Metáfora da escada','''Nesta imagem, o olhar alcança vários lances da escada.
Percorrê-los pede um lugar de partida, passos e apoios.

Podemos reconhecer uma possibilidade e ainda precisar construir condições para vivê-la.
O corrimão sustenta, e uma grade pode proteger, delimitar ou impedir uma passagem.
A função depende da situação.

Na experiência, uma organização conhecida pode oferecer continuidade e cobrar um custo de liberdade.
Que passagem a pessoa reconhece e que apoio permitiria outro movimento?
A imagem abre essa investigação sem decidir o sentido da experiência de cada um.'''),
slide(9,'O que a resposta preserva e o que fica sem expressão?','Função e singularidade','''Ao aceitar depressa, a pessoa pode procurar preservar um vínculo, uma renda ou a imagem de alguém com quem se pode contar.
O descanso, a criação ou a própria posição podem ficar sem lugar.

A função precisa ser investigada em cada situação.
Pode haver alívio, costume, risco real ou uma referência conhecida.
Algumas restrições foram impostas e nunca protegeram a pessoa.

Também perguntamos o que procura expressão: um desejo, uma capacidade, uma contribuição ou um sentido.
O TSH relaciona esse horizonte às possibilidades da Essência e às condições concretas da singularidade.
O trabalho inclui reconhecer, integrar e encontrar meios de expressão.'''),
slide(10,'Milgram: autoridade e continuidade da ação','Situação experimental','''Stanley Milgram investigou até onde participantes seguiriam instruções de uma autoridade num laboratório.
Eles acreditavam participar de uma pesquisa sobre memória e aprendizagem.

O participante assumia o papel de professor e deveria aumentar supostos choques a cada erro do aprendiz.
O pesquisador orientava a continuidade.
O aprendiz era um colaborador e não recebia as descargas anunciadas.
Na condição publicada em 1963, ele batia na parede nos níveis mais altos e deixava de responder.

Autoridade institucional, legitimidade da tarefa e pequenos incrementos compunham aquela situação.
O estudo permite examinar a distância entre sentir conflito e interromper uma ação.'''),
slide(11,'Sentir conflito não garante interromper a ação','Alcance do estudo','''Na condição descrita em 1963, participaram quarenta homens.
Vinte e seis chegaram ao nível máximo indicado e quatorze interromperam antes.
Muitos dos que continuaram mostraram tensão.

O desconforto podia coexistir com a continuidade da ação.
Precisamos compreender essa participação junto da autoridade reconhecida, da tarefa e dos compromissos em curso.
Os números pertencem àquele arranjo experimental.

Para nossa aula, a pergunta é: que condições permitem sustentar uma interrupção ou outra resposta?
Reconhecer um conflito ainda deixa aberto o trabalho de conseguir agir diante dele.'''),
slide(12,'Que condições tornam uma alternativa possível?','Pessoa, relação e condições','''Voltemos à pessoa que aceita um prazo apertado.
Ela pode saber negociar e temer uma consequência real.
Pode também ter margem para conversar e ainda não conseguir reconhecê-la.

Quem decide, o que acontece diante da discordância e que apoio existe?
Talvez precise cultivar a capacidade de permanecer na conversa.
Talvez precise obter informação, construir uma aliança, rever um acordo ou preparar uma saída.

Uma condição interna de segurança precisa encontrar a realidade da relação.
É nesse encontro entre pessoa, relação e condições que avaliamos uma alternativa.'''),
slide(13,'Pêndulo e espiral mostram perguntas diferentes','Estado e percurso','''O pêndulo acompanha variações de estado e acesso numa ocasião.
A espiral ajuda a comparar reencontros com um tema ao longo do percurso.

Numa conversa, posso passar da abertura à pressa e depois recuperar alguma referência.
Em duas conversas, posso sentir tensão semelhante e participar de outra maneira.
Talvez reconheça antes, peça tempo ou perceba melhor uma imposição.

O tema voltar deixa aberta a pergunta sobre o que foi aprendido.
Vamos examinar as diferenças de percepção, sustentação e participação junto das condições de cada ocasião.'''),
slide(14,'Duas ocasiões: o que permaneceu e o que mudou?','Comparação situada','''Dois pedidos de trabalho podem parecer semelhantes e acontecer em condições diferentes.
Em cada ocasião, acompanhamos como foi vivido, o que estava disponível e como a pessoa participou.

Descanso, informação, autonomia, apoio e risco podem alterar essa disponibilidade.
Também observamos o que retornou do encontro: alívio, cobrança, conversa ou um limite respeitado.

Reconhecer melhor o que falta já pode orientar outro trabalho.
Comparar ocasiões permite acompanhar a aquisição sem presumir progresso toda vez que um tema retorna.'''),
slide(15,'Um recurso tem função nesta situação','Pertinência do recurso','''Um recurso ajuda a perceber, sustentar ou realizar uma possibilidade naquela situação.
Sua função orienta a escolha.

Na negociação do prazo, pode ser conseguir permanecer na conversa enquanto consulta a agenda.
A firmeza vivida numa relação confiável pode oferecer uma referência para esse ensaio.
Falta de informação pede informação, e uma habilidade ainda não desenvolvida pede aprendizagem.

A tensão pode continuar e surgir maior condição de escutar e responder.
Uma capacidade interna, um apoio relacional e uma condição material podem precisar trabalhar juntos.
No ensaio, vamos conferir o que uma experiência pertinente torna disponível.'''),
slide(16,'Quatro passos para experimentar outra participação','Apresentação do percurso','''Este é o percurso da prática que será conduzida no segundo vídeo.
Primeiro reconhecemos o início de uma resposta conhecida.
Depois retornamos a outras referências, damos presença a um recurso e reencontramos o começo com esse apoio.

Essa organização dialoga com o metapadrão trabalhado por Melissa Tiers na hipnose integrativa.
No TSH, ela serve à investigação do vivido, à elaboração e à participação situada.
O recurso precisa ganhar alguma presença na experiência.
Depois comparamos o que aconteceu, inclusive quando uma diferença ainda não aparece.

Aqui estamos conhecendo o percurso.
As instruções de realização estarão no vídeo da prática.'''),
slide(17,'Envolver-se, refletir e conferir no vivido','Fundamento da investigação','''Forghieri, na investigação fenomenológica, articula envolvimento na experiência e distanciamento para refletir.
A reflexão mantém um elo com o vivido e volta a ele para conferir o que compreendeu.

Na prática, vamos nos aproximar brevemente de um momento e retornar ao presente.
Um recurso será investigado pelo que permite viver e sustentar diante daquele começo.
O ensaio pode modificar a experiência ou mostrar o que ainda falta.

Essa alternância permite investigar sem tomar a primeira explicação como conclusão definitiva.''',{'forghieri':'Forghieri · reflexão em vínculo com a experiência'}),
slide(28,'Da compreensão à participação sustentada','Fechamento da Parte 1','''A repetição envolve uma configuração vivida, aprendizagens, relações e condições.
Outra participação pode pedir elaboração, acesso a uma capacidade, cultivo ou mudança concreta de contexto.

Na segunda parte, vamos acompanhar uma situação pessoal e um recurso pertinente a ela.
Guardaremos referências do vivido e da participação, no início e no reencontro.
A comparação vai ajudar a escolher o próximo trabalho.

O apoio do aluno reúne a síntese, a ficha de registro e as referências para aprofundamento.
Reserve a prática para um momento em que possa dedicar atenção a ela.''',{'closing':'Compreender a organização.\nInvestigar outra sustentação.','next-label':'CONTINUA NA PARTE 2 DESTA AULA','next-title':'Prática guiada\ne integração'})]
practice=[
slide(0,'Experimentar outra sustentação para responder','Apresentação','''Na primeira parte, investigamos o que mantém uma resposta conhecida.
Agora vamos acompanhar uma situação sua e experimentar a presença de um recurso pertinente.

Vamos observar como a situação é vivida e que participação se torna possível.
Essa comparação ajudará a reconhecer o que ficou disponível e o que ainda precisa de trabalho.'''),
slide(17,'Preparar o retorno e os registros','Preparação','''Separe a ficha do apoio do aluno ou uma folha com espaço para registrar.
Vamos acompanhar a mesma situação do começo ao fim.

Reconheça o lugar em que está e os apoios do seu corpo.
Confira se consegue deixar uma questão de lado e retomar o presente.
Esse retorno será usado durante a prática.

Você pode manter os olhos abertos, adaptar ou interromper.
Se estiver dirigindo, reserve para outro momento.
Vamos trabalhar com uma questão que seja possível acompanhar agora.
Pause quando precisar de tempo e retome ao concluir a orientação de cada tela.

Agora vamos escolher a situação.''',{'involve':'Aproximar\nbrevemente','reflect':'Retomar\no presente','check-lived':'A mesma situação ao longo da prática','forghieri':'Registros: vivido e participação, no início e no reencontro.'}),
slide(18,'Uma situação e uma alternativa já compreendida','Escolha','''Escolha uma ocasião recente em que compreendia uma alternativa e respondeu de uma maneira conhecida.
Pode retomar uma situação da sua Cartografia.

Registre o que aconteceu e qual alternativa já reconhecia.
Guarde o instante em que a resposta começa.
Será esse mesmo começo que vamos reencontrar depois.

Pause o vídeo para escolher e situar a ocasião.
Retome quando tiver feito esse registro.

PAUSA''',{'one-moment':'Uma ocasião concreta','stakes':'O que aconteceu?\nQue alternativa você já compreendia?','first-form':'Conserve o mesmo começo para acompanhar e reencontrar.'}),
slide(19,'Como esse começo é vivido?','1 · Reconhecer o início','''Aproxime brevemente o instante anterior à resposta conhecida.
O que você viu, ouviu ou imaginou logo antes?
Perceba como esse começo é vivido agora.

Encontre uma expressão breve por palavras ou desenho.
Identifique como “Início — vivido”.
Guarde o suficiente para reconhecer a experiência.

Se estiver intenso demais, deixe a cena e retome o presente.
Pause para registrar e retome quando terminar.

PAUSA''',{'signal':'O que chegou\nlogo antes?','first-signal':'Como começa\na experiência?','signals':'Sensação, afeto, imagem, palavra ou impulso','brief':'Registro: Início — vivido'}),
slide(2,'Que resposta esse começo organiza?','1 · Reconhecer a participação','''Ainda nessa mesma ocasião, que resposta se impunha?
Que alternativa ficava difícil de sustentar?

Registre brevemente como tendia a participar.
Identifique como “Início — participação”.
Mantenha esse registro ao lado de “Início — vivido”.

Pause o vídeo para registrar.
Na próxima tela, vamos deixar a cena de lado.

PAUSA''',{'agenda-label':'O mesmo começo','agenda-meaning':'O que parecia\npreciso fazer?','answer':'Resposta\nconhecida','relief':'Alternativa\npouco acessível','cost':'Registro:\nInício — participação'}),
slide(20,'Retomar outras referências','2 · Retorno','''Deixe a cena de lado.
Reconheça o lugar onde está agora.
Perceba os apoios do corpo e retome algum movimento, se ajudar.

Dê tempo para recuperar outras referências além da situação lembrada.
Se ela continuar tomando todo o campo, conserve o contato com o presente e encerre a aproximação.
Você poderá acompanhar o restante sem voltar à cena.

Pause o vídeo agora.
Retome quando tiver reconhecido o ambiente e os seus apoios.

PAUSA'''),
slide(15,'Que qualidade daria sustentação à alternativa?','3 · Escolha do recurso','''Agora procure uma experiência em que tenha conseguido sustentar algo pertinente à alternativa que reconheceu.
Pode ser firmeza, curiosidade, apoio, tempo para decidir ou espaço para criar.
Escolha pelo que essa qualidade permite realizar.

Anote qual referência vai usar e o que ela ajudaria a sustentar.
Se nenhuma ficar acessível, registre o apoio ou a aprendizagem de que precisa.
Nesse caso, acompanhe as próximas telas sem reencontrar a cena.

Pause para escolher a referência.
Retome quando terminar.

PAUSA''',{'resource':'Sustentar\na alternativa','resource-0':'Experiência vivida','resource-1':'Qualidade pertinente','resource-2':'Apoio','resource-3':'Condição necessária'}),
slide(21,'Dar presença à experiência de recurso','3 · Recurso vivido','''Aproxime a experiência de recurso que escolheu.
Como essa qualidade aparece no corpo, no ritmo, na imagem ou na relação?
Permita que a referência ganhe presença do modo que for possível.

Confira o que consegue sentir e sustentar agora.
Uma lembrança ou imagem pode ajudar, desde que ofereça algum apoio vivido.

Pause o vídeo e dê tempo a essa aproximação.
Retome quando tiver acompanhado o recurso.
Se ele não ficar disponível, conserve o presente e siga sem voltar à cena.

PAUSA''',{'resource-function':'Como essa qualidade\nganha presença agora?','resource-action':'Observe o apoio que de fato\nfica disponível.'}),
slide(22,'Reencontrar o começo com esse apoio','4 · Reencontro do vivido','''Se o recurso estiver acessível e houver disponibilidade, aproxime apenas o começo da mesma situação.
Conserve contato com esse apoio.

Como aquele começo é vivido agora?
Registre uma expressão breve como “Reencontro — vivido”.

Se perder o apoio ou a cena tomar conta, deixe-a de lado e retorne ao presente.
Você pode seguir para a comparação com o que conseguiu observar.

Pause para acompanhar e registrar.
Retome quando terminar.

PAUSA''',{'start':'O mesmo começo','other-support':'Recurso presente','rehearsal':'Como a situação\né vivida agora?','external':'Registro: Reencontro — vivido'}),
slide(22,'Que participação se torna possível?','4 · Reencontro da participação','''Se estiver acompanhando a cena com apoio, observe que gesto ou resposta consegue sustentar.
Confira como essa participação é vivida, além da frase que gostaria de dizer.

Registre como “Reencontro — participação”.
A resposta real da outra pessoa continua desconhecida.

Se encerrou a aproximação, registre até onde conseguiu acompanhar e o que faltou.
Pause o vídeo para registrar.
Depois vamos deixar a cena de lado.

PAUSA''',{'start':'Situação escolhida','other-support':'Apoio disponível','rehearsal':'Que gesto ou resposta\nconsigo sustentar?','external':'Registro: Reencontro — participação'}),
slide(20,'Retornar antes de comparar','Retorno','''Deixe a cena e o ensaio de lado.
Reconheça novamente o ambiente e os apoios do seu corpo.
Retome os movimentos que precisar.

Vamos olhar para os registros a partir deste momento.
Se não realizou o reencontro, conserve essa informação para compreender o que ainda falta.

Pause o vídeo para retornar.
Retome quando estiver pronto para olhar os registros.

PAUSA''',{'scene':'Ensaio concluído','scene-space':'Em segundo plano','agency':'Disponibilidade\npara comparar'}),
slide(14,'O que mudou no vivido?','Comparação do vivido','''Coloque lado a lado “Início — vivido” e “Reencontro — vivido”.
O que mudou e o que permaneceu na maneira de viver a mesma situação?

Registre a diferença que de fato reconhece.
Ela pode ser pequena, não aparecer ou incluir algo que ficou mais claro.
Se o reencontro não aconteceu, registre o que impediu continuar.

Pause para comparar os registros do vivido.
Retome quando terminar.

PAUSA''',{'occasion-a':'Início — vivido','occasion-b':'Reencontro — vivido','a-context':'Como a situação\nse apresentava','b-context':'Como se apresentou\ncom o recurso','comparison':'O que mudou? O que permaneceu?'}),
slide(14,'O que mudou na participação?','Comparação da participação','''Agora compare “Início — participação” e “Reencontro — participação”.
Que resposta parecia se impor e o que conseguiu sustentar no ensaio?

Registre a diferença junto das condições e do apoio que a tornaram possível.
Uma intenção pode ter aparecido sem ainda se tornar sustentação vivida.
Isso também orienta o trabalho que precisa continuar.

Pause para comparar os registros da participação.
Retome quando estiver pronto para concluir a prática.

PAUSA''',{'occasion-a':'Início — participação','occasion-b':'Reencontro — participação','a-context':'Resposta conhecida\ne alternativa difícil','b-context':'Gesto ou resposta\nque ganhou sustentação','comparison':'Que apoio participou dessa diferença?'}),
slide(28,'Encerrar a prática','Encerramento','''Vamos concluir.
Deixe a questão e os registros de lado.
Reconheça o lugar onde está, movimente-se e confira sua disponibilidade para continuar o dia.

PAUSA

A prática termina aqui.
Agora vamos elaborar o que ela permitiu reconhecer.''',{'closing':'Deixe a questão de lado.\nRetome o contato com o ambiente.','next-label':'RETOME SEUS MOVIMENTOS','next-title':'A prática termina aqui.'}),
slide(24,'Cada resultado orienta um trabalho diferente','Elaboração','''A experiência pode ter mudado sem eliminar toda a tensão.
Talvez tenha surgido maior condição de sustentar uma pergunta ou um limite.

Se a capacidade ficou disponível, vale escolher onde experimentá-la e acompanhar os efeitos.
Se apareceu e se perdeu facilmente, pode pedir cultivo, tempo e apoio.
Se algo impediu continuar, investigamos a pertinência do recurso, a capacidade necessária e as condições concretas.

Compreensão, experiência e participação podem mudar de maneiras diferentes.
O que foi observado ajuda a decidir por onde continuar.'''),
slide(25,'A nova possibilidade precisa encontrar a vida real','Continuidade','''O ensaio oferece uma referência, e o encontro real traz informações que ainda não temos.
Na negociação de um prazo, conseguir permanecer na conversa precisa se articular com conhecer prioridades e formular uma proposta viável.

Um próximo passo pode ser consultar um acordo, preparar a conversa, buscar apoio ou reservar espaço para criar.
Depois acompanhamos como participamos, como o outro respondeu e que consequências apareceram.
Essas informações podem ampliar ou corrigir o ensaio.
O cultivo inclui repetir com atenção aos efeitos e às condições.'''),
slide(26,'O mesmo tema pode voltar com outra participação','Percurso','''Um pedido semelhante pode trazer de volta alguma tensão.
A comparação considera o que voltou, em quais condições e como participamos desta vez.

Talvez reconheçamos antes, consigamos pedir tempo ou percebamos um limite que estava invisível.
Também podemos descobrir que o recurso ou a estratégia precisa de revisão.

A espiral conserva essas diferenças entre ocasiões.
O retorno de um tema deixa abertos os resultados e a direção do trabalho.
A referência é o que se torna mais reconhecível e realizável na vida.'''),
slide(27,'Guardar a investigação na Cartografia','Integração e próxima aula','''Na Situação, conserve o acontecimento, a relação e as condições.
Na Manifestação, guarde o vivido e a participação, no início e no reencontro.
Na Tradução provisória, registre o que compreendeu da organização e o que ainda precisa conferir.
Na Orientação possível, indique o recurso, o cultivo, o apoio ou a condição a buscar.

Depois do encontro real, volte ao registro e acompanhe os efeitos.

Na M2.5, vamos diferenciar acontecimento, experiência e interpretação.
Uma mudança importante no vivido ainda precisa ser compreendida com discernimento.''')]
for name,slides in [('parte1',theory),('parte2',practice)]:
 for i,s in enumerate(slides,1):s['number']=i;s['notes_sha256']=hashlib.sha256(s['notes'].encode()).hexdigest()
 obj={'lesson':'M2.4','version':'1.0','date':'2026-11-22','part':1 if name=='parte1' else 2,'title':'O que mantém a repetição de uma resposta?','slides':slides}
 (P/f'{name}_v1.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2))
 print(name,len(slides),'telas',sum(len(s['notes'].split()) for s in slides),'palavras nas notas')
