from base import *

OUT = "/home/claude/out/encontro"
os.makedirs(OUT, exist_ok=True)
MAPA_TSH = "../../../../../../90 - Anexos/Mapas Conceituais/Mapa do TSH - Espiral, Eixo, Pêndulo e Espelho.png"
SEMENTE = "img/semente-1.png"
PAUSA_AO_VIVO = "Faça comigo agora. Não precisa escrever."

d = Deck("Encontro 28/11", "Ao vivo")

def marcador(fim, segue):
    """Tela escura só com a marca: na gravação, aparece como um quadro escuro fácil de achar na edição."""
    s = d._new(dark=True)
    pic(s, A + "mark_gold.png", (W - 2.2) / 2, 2.3, h=2.2)
    d.notes(s, "Marcador de edição", "MARCADOR",
            [f"[MARCADOR] {fim}",
             "Esta tela escura não entra em nenhum vídeo: na edição, ela mostra onde cortar.",
             "Deixe-a na tela por 2 ou 3 segundos e avance."],
            "Próximo: " + segue + ".")


# ======================= PRIMEIRA HORA =======================
d.capa("Encontro ao vivo · 28 de novembro",
       "Primeira hora: o Módulo 1 em prática guiada e as suas dúvidas. Segunda hora: a abertura do Módulo 2.",
       "ACOLHER",
       ["[9h00] Antes de tudo: gravação do Zoom ligada.",
        "Boas-vindas. Esperar dois ou três minutos pela entrada.",
        "",
        "«Hoje temos duas horas.",
        "Na primeira, vamos fazer juntos o Módulo 1 em prática, sem escrever nada, e depois abrir para as suas dúvidas.",
        "Na segunda, abrimos o Módulo 2, que fica disponível amanhã.»",
        "",
        "Avisar: «a primeira parte fica gravada no Módulo 1, para quem quiser fazer de novo.»"],
       "Próximo: não existe atraso.", tag="TRADUZINDO O SER HUMANO · ENCONTRO AO VIVO")

d.frase("Antes de começar",
        "Não existe atraso no TSH.",
        "As mesmas práticas dos apoios de cada aula, agora em sequência, com uma só situação.",
        "ABRIR · CORTE 0 COMEÇA AQUI",
        ["[CORTE 0 · início] Marque o horário para a edição.",
         "",
         "«Não existe atraso no TSH.",
         "Se você não conseguiu fazer tudo do Módulo 1, este é o caminho mínimo.",
         "Vamos juntos, em sete passos, um para cada aula. Sem escrever nada.»",
         "",
         "«Cada passo é a prática de uma aula do Módulo 1, a mesma que está no apoio de uma página daquela aula.",
         "Aqui fazemos em sequência, com uma só situação, para você sentir o módulo como um caminho.",
         "Depois, você pode fazer qualquer passo sozinho, quando quiser, pelo apoio da aula.»",
         "",
         "«Se puder, sente com os pés no chão.»"],
        "Próximo: passo 1.", lead="Módulo 1 em prática guiada · 10 a 12 minutos")

PASSOS = [
 ("1 · Uma situação", "Uma situação em que você entende o seu padrão e ainda assim repete.",
  "Aula 1.1\n\nSó escolha. Não precisa contar a ninguém.\n\nSinta os pés. Três respirações no baixo ventre.",
  ["[1 min 30]",
   "«Escolha uma situação em que você entende o seu padrão e ainda assim repete.",
   "Só escolha. Não precisa contar a ninguém.»",
   "[PAUSA] 20 segundos em silêncio.",
   "«Sinta os pés. Três respirações no baixo ventre.» Respire junto: um… dois… três."]),
 ("2 · Saber, acessar, sustentar", "Eu sei o que fazer? Consigo acessar na hora? Consigo sustentar?",
  "Aula 1.2\n\nNote onde está a dificuldade.\n\nEla não diz quem você é. Diz onde praticar.",
  ["[1 min 30]",
   "«Nessa situação: eu sei o que fazer?» [PAUSA breve]",
   "«Consigo acessar isso na hora?» [PAUSA breve]",
   "«Consigo sustentar?» [PAUSA breve]",
   "«Note onde está a dificuldade. Ela não diz quem você é; diz onde praticar.»"]),
 ("3 · O que o corpo aprende", "Um sorriso leve nos olhos e nos lábios.",
  "Aula 1.3 · Sorriso Interior\n\nLeve ao coração.\nLeve ao baixo ventre.\nTrês respirações.",
  ["[1 min 30] Sorriso Interior.",
   "«Um sorriso leve nos olhos e nos lábios.» [PAUSA]",
   "«Leve esse sorriso ao coração.» [PAUSA]",
   "«Leve ao baixo ventre.» [PAUSA]",
   "«Três respirações.»",
   "«O que mudou, mesmo que pouco?»"]),
 ("4 · Território e mapa", "Primeiro, só o que você sente. Depois, a explicação.",
  "Aula 1.4\n\nQue outra explicação também caberia?",
  ["[1 min]",
   "«Volte à situação. Primeiro, só o que você sente.» [PAUSA]",
   "«Agora, a explicação que você costuma dar.» [PAUSA]",
   "«Que outra explicação também caberia?»"]),
 ("5 · As Cinco Janelas", "Corpo · emoção · mente · relações · espiritualidade",
  "Aula 1.5\n\nUma palavra para cada, em silêncio.\n\nQual janela mostrou algo novo?",
  ["[2 min] Uma janela por vez, devagar, com 10 a 15 segundos entre elas.",
   "«Corpo…» «emoção…» «mente…» «relações…» «espiritualidade.»",
   "«Uma palavra para cada, em silêncio.»",
   "«Qual janela mostrou algo novo?»"]),
 ("6 · A primeira Cartografia", "Dessa janela, um detalhe. Dê a ele uma forma.",
  "Aula 1.6\n\nUma palavra, um gesto, uma imagem.\n\nCombina com o que você sente? Ajuste.",
  ["[1 min]",
   "«Dessa janela, um detalhe. Dê a ele uma forma: uma palavra, um gesto, uma imagem.» [PAUSA]",
   "«Ela combina com o que você sente? Ajuste.»",
   "«Quem quiser, desenha ou escreve isso depois no Caderno.»"]),
 ("7 · Perder o eixo não é perder o percurso", "Uma vez em que você perdeu o eixo e voltou. O que ajudou?",
  "Aula 1.7\n\nEsse recurso é seu.\n\nTrês respirações no baixo ventre.",
  ["[1 min 30]",
   "«Lembre uma vez em que você perdeu o eixo e voltou.» [PAUSA]",
   "«O que ajudou a voltar?» [PAUSA]",
   "«Esse recurso é seu. Perder o eixo não significa perder o percurso.»",
   "Fechar com três respirações no baixo ventre, respirando junto.",
   "",
   "[CORTE 0 · fim] Marque o horário. «Isso fica no Módulo 1, com os apoios de uma página de cada aula.»"]),
]
for i, (t, perg, apoio, notas) in enumerate(PASSOS):
    d.passo(t, perg, apoio, "CONDUZIR", notas,
            "Próximo: " + (PASSOS[i + 1][0] if i + 1 < len(PASSOS) else "dúvidas."), pausa=PAUSA_AO_VIVO)

marcador("Fim do corte 0 (Módulo 1 em prática guiada).", "dúvidas")

d.cartoes("Suas dúvidas sobre o Módulo 0 e o Módulo 1",
          [("Pergunte", "O que ficou difícil, o que não ficou claro, o que você notou na vida."),
           ("Não existe atraso", "Cada módulo terá um caminho mínimo: duas aulas e a prática diária."),
           ("O percurso cresceu", "De 54 para 59 aulas: entraram aulas práticas de cultivo.")],
          "RESPONDER · FORA DOS VÍDEOS",
          ["[Até 10h] Dúvidas. Esta parte não entra nos vídeos.",
           "",
           "Aviso, se couber: o percurso ganhou aulas práticas de cultivo e passou de 54 para 59 aulas.",
           "",
           "Fala opcional sobre a aula 1.7, o pêndulo (sua monografia de 2004): «nada é absoluto Yin ou Yang… o equilíbrio é dinâmico e constantemente variável». Na tradição chinesa, a polaridade não é oposição nem conflito: é o pêndulo do curso, numa linguagem que muitos já conhecem.",
           "",
           "Fala opcional sobre a aula 1.3 (sua monografia transpessoal de 2010): estado não é estágio. Uma vivência pode alcançar um estado «disponível em qualquer estágio», mas isso não quer dizer que ele se instale para sempre. Por isso o curso tem prática diária: o Cultivo do Eixo, que apresento no fim de hoje.",
           "",
           "Pedido para os mapas: «Quem já olhou os mapas do Módulo 1: qual ajudou, e qual confundiu?»"],
          "Próximo: segunda hora, a abertura do Módulo 2.", dark_idx=(1,))

# ======================= SEGUNDA HORA =======================
marcador("Fim das dúvidas. A seguir começa o corte 1 (abertura do Módulo 2).", "abertura do Módulo 2")

d.capa("Módulo 2 · Percepção e tradução da experiência",
       "O que acontece entre o que vivemos e o que fazemos.",
       "ABRIR · CORTE 1 COMEÇA AQUI",
       ["[10h00 · CORTE 1 · início] Marque o horário. Fale para quem vai assistir depois, sem nomes de participantes.",
        "",
        "«Hoje começamos o Módulo 2.»",
        "O Módulo 2 olha para o que acontece entre o que vivemos e o que fazemos: como percebemos, o que ganha importância, de onde vêm as certezas e por que certas respostas voltam.",
        "",
        "O mapa do percurso, com as suas palavras: «Precisamos primeiro traduzir o que temos em nossos padrões e depois trabalhar para ganhar eixo e presença suficientes para ocupar nosso real espaço.»",
        "Traduzir: os fundamentos no Módulo 1 e a prática neste módulo. Ganhar eixo e presença: Módulos 3 a 6. Ocupar o próprio espaço: Módulos 7 e 8. Uma direção alimenta a outra."],
       "Próximo: o mapa O Caminho da Semente.", tag="ABERTURA DO MÓDULO 2")

# Tela: o mapa inteiro, ampliado
s = d._new()
mh = 7.1; mw = mh * 2048 / 3072
# img/semente-v2.jpg: cópia de 80 - Mapas Conceituais/Originais/2026-11-28/O-caminho-da-semente-v2.jpg
pic(s, "img/semente-v2.jpg", (W - mw) / 2, 0.2, h=mh, back=False)
d.text(s, 0.55, 0.6, 3.4, 0.4, "TRADUZINDO O SER HUMANO", size=10, color=EST, bold=True)
d.text(s, 0.55, 1.1, 3.5, 1.6, "O Caminho da Semente", size=32, font=SERIF, color=NOT, line=1.0)
d.text(s, 0.55, 2.9, 3.4, 1.6, "A Essência é o destino. O eixo é o caminho.", size=19, color=EST, italic=True, line=1.15)
d.text(s, 9.4, 2.4, 3.5, 2.4, "Todos nós nascemos com um potencial único. A vida acontece, e nos afastamos do nosso centro.", size=16, color=NOT, line=1.2)
d.text(s, 9.4, 6.6, 3.5, 0.5, "Mapa de Fabiano Deliberalli, versão de novembro de 2026", size=10, color=MUTED)
d.notes(s, "O Caminho da Semente", "LER O MAPA · 1 MIN 30",
        ["O mapa inteiro, ampliado. Leia de baixo para cima, devagar.",
         "",
         "«Todos nós nascemos com um potencial único. A vida acontece, e nos afastamos do nosso centro. O caminho de volta é lembrar, integrar e expressar quem realmente somos.»",
         "«A Essência é o destino. O eixo é o caminho.»",
         "",
         "Embaixo, a semente, no caos. No alto, a árvore: «Você. Inteiro. No mundo.» No meio, o eixo.",
         "",
         "Ao longo do eixo, a luz: a Essência acompanha todo o caminho. Não é um degrau a alcançar no fim.",
         "Os oito movimentos de volta, de baixo para cima: regulação, presença, observação, tradução, integração, liberdade, expressão, contribuição.",
         "«Não é uma escada: vamos e voltamos», como o pêndulo e a espiral da aula 1.7.",
         "",
         "Se alguém perguntar: a Tradução é o que fazemos nos Módulos 1 e 2; a Liberdade é ocupar o próprio espaço sem romper o vínculo."],
        "Próximo: de perto, a coluna das camadas.")

# Tela: a coluna das camadas, de perto
s = d._new()
d._chrome(s, "O que nos afasta do centro")
hh = 4.55; hw = hh * 459 / 451
x0 = (W - (2 * hw + 0.35)) / 2
pic(s, "img/semente-camadas-1.png", x0, 1.7, h=hh, back=False)
pic(s, "img/semente-camadas-2.png", x0 + hw + 0.35, 1.7, h=hh, back=False)
d.text(s, 0.62, 6.38, 12.0, 0.5, "As camadas também protegeram. Reconhecê-las não é culpar a história. Cada uma volta ao longo do curso.",
       size=16, color=EST, align="ctr")
d._footer(s)
d.notes(s, "O que nos afasta do centro", "PERCORRER A COLUNA · 2 MIN",
        ["Percorra a coluna de cima para baixo, uma camada por vez:",
         "padrões automáticos («Repetimos sem perceber porque aprendemos a sobreviver»);",
         "feridas e traumas; defesas e máscaras; desconexão corpo-mente; sobrecarga e caos; condicionamentos.",
         "",
         "Com a voz do workshop: «Essa Essência vai ficando soterrada por camadas de vivências, como suas emoções, crenças, imagens, memórias e corpos.»",
         "Retomar 1.1: «Ou trabalhamos voluntariamente ou somos vividos pelos padrões que carregamos.»",
         "As camadas também protegeram; reconhecê-las não é culpar a história.",
         "«Cada uma delas volta ao longo do curso.»",
         "",
         "Opcional, 45 segundos: o Buda de Ouro de Wat Traimit, em Bangkok. Coberto de gesso, provavelmente para escapar de invasores, e esquecido por séculos. Em 1955, ao ser removido, caiu, o gesso rachou e o ouro apareceu. A camada protegeu; depois escondeu. O ouro não precisou ser fabricado."],
        "Próximo: o eixo como caminho de volta.")

d.frase("O eixo como caminho de volta",
        "Há uma parte do Ser que pede retorno ao lar! E o EIXO é um caminho para que isso possa acontecer.",
        "Fabiano Deliberalli",
        "2 MIN",
        ["Ler a frase.",
         "«A Essência é o destino. O EIXO é o caminho.»",
         "",
         "Lembrar o que já foi praticado nas aulas abertas do Módulo 0: o eixo, o apoio e os três ajustes; a árvore, o Tan Tien e Yongquan; o eixo no cotidiano; o Sorriso Interior.",
         "«Hoje a árvore ganha nome e sequência, e vai acompanhar o curso inteiro.»"],
        "Próximo: o Mapa do TSH.", lead="A Essência é o destino. O eixo é o caminho.")

s = d._new()
pic(s, MAPA_TSH, 0, 0, w=W, back=False)
d.notes(s, "Mapa do TSH — o caminho em espiral", "PRÉVIA · 3 MIN",
        ["Só uma prévia; o mapa volta em partes ao longo do curso.",
         "",
         "A espiral sobe em torno do eixo: os mesmos temas voltam, em outro nível.",
         "De perto, a espiral é o pêndulo do dia a dia.",
         "O espelho muda a pergunta de «de novo isso?» para «o que mudou desde a última vez?».",
         "«Os padrões voltam em outro nível. A volta não é o fracasso do caminho: é a ocasião da obra.»"],
        "Próximo: o que vem no módulo.")

d.sequencia("O que vem no Módulo 2",
            ["Como as camadas\nformam o que percebo", "O que ganha\nimportância", "A certeza que\nocupa o campo",
             "Por que a resposta\nse repete", "Experiência e\ninterpretação", "Construir uma\nTradução"],
            "1 MIN · CORTE 1 TERMINA AQUI",
            ["Uma frase por aula:",
             "2.1 como as camadas formam o que percebo;",
             "2.2 o que ganha importância, e o Eu Básico que pede Tradução;",
             "2.3 a certeza que ocupa o campo;",
             "2.4 por que a resposta se repete;",
             "2.5 experiência, interpretação e origem, inclusive a espiritual;",
             "2.6 como construir e revisar uma Tradução.",
             "",
             "«Até aqui acompanhamos uma cena-exemplo. Daqui em diante, vou trazer histórias reais, minhas e de pessoas que acompanhei, com cuidado de anonimato.»",
             "",
             "[CORTE 1 · fim] Marque o horário."],
            "Próximo: Zhan Zhuang.", lead="Seis aulas, uma pergunta cada")

marcador("Fim do corte 1 (abertura do Módulo 2). A seguir, o corte 2 (Zhan Zhuang).", "Zhan Zhuang")

d.sequencia("O eixo no corpo: Zhan Zhuang",
            ["Wu Chi\nde pé, braços soltos", "A árvore\nbraços em arco", "Fechamento\nmãos no baixo ventre"],
            "CONDUZIR DE PÉ · CORTE 2 · 10 MIN",
            ["[CORTE 2 · início] Marque o horário.",
             "",
             "IMPORTANTE: mostre esta tela só no Z1, para dar o nome e a sequência. Do Z2 ao Z4, PARE DE COMPARTILHAR A TELA: assim a gravação mostra você de corpo inteiro, que é a melhor imagem da postura. Volte a compartilhar depois do fechamento, no marcador seguinte.",
             "",
             "Em pé, se possível. Quem precisar: sentado na borda da cadeira, ou em pé com uma mão apoiada. Mostre de frente e, se der, de lado.",
             "",
             "Z1 · O nome (1 min): Zhan Zhuang, «ficar em pé como uma estaca», a postura de pé do Qi Gong. É a árvore que já praticaram. Sequência fixa: Wu Chi, árvore, fechamento. Não há o que alcançar; há o que perceber.",
             "",
             "Z2 · Wu Chi (3 min), um princípio por vez: pés paralelos na largura dos ombros, peso perto de Yongquan; joelhos soltos; quadril assentado, como quem começa a sentar; topo da cabeça suspenso por um fio, queixo levemente recolhido; ombros soltos, braços ao lado do corpo; respiração natural; atenção abaixo do umbigo. Silêncio de 30 a 60 segundos.",
             "",
             "Z3 · A árvore (3 min): braços em arco à frente do peito, como quem abraça um tronco, palmas para o peito; axilas abertas, ombros soltos, cotovelos um pouco abaixo das mãos; raiz para baixo pelos pés, topo da cabeça para cima. 1 a 2 minutos. Se cansar, baixar os braços e seguir em Wu Chi.",
             "«O eixo não é rigidez. É o que permite oscilar sem cair.»",
             "",
             "Z4 · Fechamento (3 min): baixar os braços devagar; mãos sobrepostas no baixo ventre. Respirar como um fole, sem forçar. Cinco respirações em silêncio. Soltar as mãos; perceber os pés e o corpo inteiro.",
             "«Essa é a base que vamos usar nas práticas do módulo: o eixo, o centro e a respiração.» O guia de uma página está na aula do Zhan Zhuang.",
             "",
             "[CORTE 2 · fim] Marque o horário."],
            "Próximo: marcador; volte a compartilhar a tela.",
            lead="Não há o que alcançar. Há o que perceber.",
            foot="Sentado na borda da cadeira ou com uma mão apoiada, se precisar.")

s = d._new()
d._chrome(s, "Zhan Zhuang: de frente e de lado")
fh = 4.75; fw = fh * 535 / 385
# img/zz-fotos.png: Liu Pai Lin em foto do livro de Kenichi Shioda (recorte do slide de Fabiano; não versionada, por ser imagem de livro publicado)
pic(s, "img/zz-fotos.png", 0.62, 1.8, h=fh, back=False)
d.text(s, 0.62 + fw + 0.45, 2.0, 12.7 - (0.62 + fw + 0.45), 3.5,
       "Joelhos soltos\n\nBraços em arco, palmas para o peito\n\nOmbros soltos, cotovelos baixos\n\nTopo da cabeça suspenso",
       size=18, color=NOT, line=1.1)
d.text(s, 0.62, 6.62, 8.0, 0.35, "Mestre Liu Pai Lin, em foto do livro de Kenichi Shioda", size=10, color=MUTED)
d._footer(s)
d.notes(s, "Zhan Zhuang: de frente e de lado", "MOSTRAR NO Z1 · A LINHAGEM",
        ["Mostre por alguns segundos no Z1, para que todos vejam a postura de frente e de lado. Depois, pare de compartilhar.",
         "",
         "Conte com as suas palavras quem é: o Mestre Liu Pai Lin, da linhagem em que você se formou, posando para o livro do professor Kenichi Shioda, também seu professor de Qi Gong.",
         "A linhagem completa e a sua formação são ensinadas em M3.5 e M3.6; aqui basta uma frase."],
        "Próximo: pare de compartilhar e conduza Z2 a Z4.")

marcador("Fim do corte 2 (Zhan Zhuang). Volte a compartilhar a tela. A seguir, o corte 3.", "a prática do primeiro sinal ao eixo")

d.cartoes("Do primeiro sinal ao eixo · combinados",
          [("Você escolhe", "Até onde vai. Pode abrir os olhos e parar a qualquer momento."),
           ("Intensidade até 4", "Uma situação recente, não a mais difícil: até 4 em 10."),
           ("Cuidado", "Não praticar dirigindo. Em muita desorganização, faça só a respiração e o retorno.")],
          "CORTE 3 COMEÇA AQUI · B1 A B3",
          ["[10h20 · CORTE 3 · início] Marque o horário. Conduza de modo que a gravação funcione sozinha: quem assistir depois faz junto, no ritmo da prática.",
           "",
           "B1 · O transe que não se escolhe (3 min): na sua formulação, todos vivemos hipnotizados em algum grau; o trabalho não é colocar em transe, é sair do transe que não escolhemos. A reação que se repete é um desses transes: quando percebemos, já entramos. Entre o sentir e o agir há um espaço. Hoje vamos treinar perceber que entramos, e voltar.",
           "",
           "B2 · Combinados (1 min): os três cartões.",
           "",
           "B3 · Escolher a situação (2 min): uma situação recente em que uma reação conhecida voltou. Intensidade até 4 em 10. Uma palavra que a lembre; quem quiser, anota."],
          "Próximo: o retorno.", dark_idx=(2,))

d.sequencia("Aprender a voltar antes de entrar",
            ["Contar\n1, 2, 3", "Olhos\nabertos", "Data e\nlugar", "Corpo e\nrespiração"],
            "B4 E B5 · 7 MIN",
            ["B4 · Sentar com o eixo (3 min): da árvore para a cadeira. Pés apoiados, bacia, coluna, topo da cabeça suspenso: os três ajustes do Módulo 0. Mãos no baixo ventre, algumas respirações como um fole. Perceber o apoio dos pés e o centro.",
             "",
             "B5 · O retorno, antes de entrar (4 min): aprender a sair antes de entrar.",
             "Contagem de 1 a 3; ao 3, olhos abertos.",
             "Dizer por dentro a data e o lugar. Sentir o corpo e a respiração.",
             "Fazer o retorno uma vez, só para aprender."],
            "Próximo: os dois ciclos.", lead="Retorno: o que vamos usar em toda prática")

d.sequencia("Do primeiro sinal ao eixo",
            ["O primeiro\nsinal", "Baixo ventre:\ntrês respirações", "Retorno:\n1, 2, 3", "Uma resposta\npossível"],
            "B6 A B9 · 16 MIN",
            ["B6 · Primeiro ciclo: perceber que entrou (6 min).",
             "1. Olhos fechados ou baixos. Lembrar a situação por 30 a 60 segundos, só até o primeiro sinal.",
             "2. Onde aparece no corpo? O que acontece com a respiração? O que se estreita?",
             "3. Perceber: «entrei». É esse momento que o curso vai ensinar a reconhecer cada vez mais cedo.",
             "4. Voltar ao baixo ventre: três respirações como um fole.",
             "5. Retorno: 1, 2, 3; data e lugar; corpo e respiração.",
             "",
             "B7 · Registro rápido (3 min), escrever é opcional: o que percebi primeiro? O que mudou com a respiração e o retorno?",
             "",
             "B8 · Segundo ciclo: do eixo, uma resposta possível (5 min).",
             "1. A mesma situação, mais breve, até o primeiro sinal.",
             "2. Baixo ventre e eixo: pés, centro, três respirações.",
             "3. «Daqui, que resposta é possível agora?» Pedir tempo, esclarecer, estabelecer um limite, ou outra nas palavras de cada um.",
             "4. Ensaiar só a primeira frase dessa resposta, por dentro, com a postura do eixo.",
             "5. Retorno: 1, 2, 3; data e lugar; corpo e respiração.",
             "",
             "B9 · Duas perguntas (2 min), sem obrigação de compartilhar: «O que essa reação protegeu?» «O que de você ficou sem lugar?»"],
            "Próximo: o fechamento e o Cultivo do Eixo.", lead="Perceber que entrou, e voltar")

d.cartoes("Daqui em diante, um pouco todos os dias",
          [("Cultivo do Eixo", "3 a 5 min por dia: a árvore, «o que está me vivendo agora?», três respirações."),
           ("Retorno ao Eixo", "No momento real: o primeiro sinal, os pés, três respirações."),
           ("Caderno de Reencontros", "Uma vez por quinzena, antes do encontro. Escrever é opcional.")],
          "B10 · FECHAMENTO · CORTE 3 TERMINA AQUI",
          ["B10 · Fechamento (2 min).",
           "Retorno completo; tudo o que foi sugerido no corpo volta ao habitual.",
           "",
           "«Até aqui, entendemos. Daqui em diante, praticamos um pouco todos os dias.»",
           "",
           "Cultivo do Eixo, todos os dias, de três a cinco minutos. Cada módulo acrescenta um passo.",
           "Retorno ao Eixo, no momento real.",
           "Caderno de Reencontros: o guia e o caderno estão na Hotmart, na aula do Zhan Zhuang.",
           "Pergunta do espelho para a quinzena: o que mudou desde a última vez?",
           "",
           "[CORTE 3 · fim] Marque o horário."],
          "Próximo: o ponto de partida.", dark_idx=(0,))

marcador("Fim do corte 3 (Do primeiro sinal ao eixo).", "o ponto de partida")

d.frase("O seu ponto de partida",
        "Numa situação recente em que um padrão foi ativado: quanto do que você sabe ficou disponível, de 0 a 10? Quanto tempo levou para perceber e voltar?",
        "Dias, horas, minutos ou no próprio momento · a mesma pergunta volta nos Módulos 4 e 8",
        "C0 · 5 MIN · FORA DOS VÍDEOS",
        ["[Fora dos vídeos] Cada pessoa escreve na capa do Caderno de Reencontros, ou no formulário com link no chat.",
         "",
         "«Pense numa situação recente em que um padrão seu foi ativado. Quanto do que você já sabe sobre si ficou disponível naquele momento, de 0 a 10? Quanto tempo você levou para perceber e voltar: dias, horas, minutos ou no próprio momento?»",
         "",
         "Ninguém precisa mostrar a resposta. A mesma pergunta volta no Módulo 4 e no Módulo 8.",
         "",
         "Depois, compartilhamento livre até 11h. Relatos só entram em vídeo com consentimento expresso, sem dados que identifiquem."],
        "Próximo: até a próxima.", lead="Pergunta de progresso")

d.fechamento("Até o próximo encontro",
             "Perder o eixo não significa perder o percurso.",
             ["O Módulo 2 abre amanhã, 29/11.", "Próximo encontro: sábado, 12/12, das 9h às 11h."],
             "ENCERRAR",
             ["«O Módulo 2 abre amanhã. Comecem pela abertura e pelo Zhan Zhuang.",
              "Se a quinzena apertar, o caminho mínimo está na descrição do módulo.",
              "Próximo encontro: 12/12.»",
              "",
              "Encerrar e salvar a gravação."])

d.save(f"{OUT}/Encontro-28-11-slides.pptx")
import json
json.dump(d.guide, open(f"{OUT}/guia.json", "w"), ensure_ascii=False)
print("ok", d.n)
