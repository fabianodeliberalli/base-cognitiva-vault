from base import *

OUT = "/home/claude/build_m2v/out_m3"
os.makedirs(OUT, exist_ok=True)

CULT3 = [("Na árvore", "Respire passando pelos três centros: baixo ventre, peito, testa."),
         ("Se quiser", "Sustentar o Céu, três vezes."),
         ("O recurso do dia", "Escolha o recurso de retorno que vai levar com você.")]


def cultivo(d, tie, nxt="Próximo: o fechamento."):
    d.cartoes("Cultivo do Eixo desta quinzena", CULT3, "CONVIDAR",
              ["Todos os dias desta quinzena, de três a cinco minutos: o Cultivo do Eixo, versão do Módulo 3.",
               "A árvore com a respiração passando pelos três centros: baixo ventre, peito, testa.",
               "Se quiser, Sustentar o Céu três vezes. E a escolha do recurso de retorno do dia.",
               "",
               tie,
               "",
               "No primeiro sinal: Retorno ao Eixo, trinta segundos.",
               "Uma vez por quinzena, antes do encontro, um reencontro no Caderno.",
               "Falhar um dia não desfaz nada. Retome no seguinte."],
              nxt, lead="Todos os dias, de três a cinco minutos",
              foot="No primeiro sinal: Retorno ao Eixo (30 s). Uma vez por quinzena: um reencontro no Caderno.",
              dark_idx=(0,))


# =====================================================================
# M3.1
# =====================================================================
d = Deck("M3.1", "Aula")
d.capa("Estado corporal e acesso às respostas", "O corpo muda o que fica acessível",
       "ABRIR",
       ["Começa a segunda direção do percurso: ganhar eixo e presença.",
        "Ela começa pelo corpo, porque algumas camadas não estão nas ideias.",
        "",
        "A pergunta desta aula: por que a mesma pessoa, na mesma situação, responde de modos diferentes?"],
       "Próximo: uma cena no trânsito.", tag="M3.1 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.historia("Uma cena no trânsito", "VIVÊNCIA DO AUTOR",
           ["No trânsito de São Paulo, a vontade de acelerar.",
            "Um recurso breve: o Sorriso Interior.",
            "Outra resposta aparece: adiar a viagem em vez de acelerar."],
           "A situação era a mesma. O estado mudou o que ficou acessível.",
           "CONTAR",
           ["Conte com as suas palavras. Registro: guia de condução da Masterclass, versão 2.6.",
            "",
            "A cena: o trânsito de São Paulo e a vontade de acelerar.",
            "Com o Sorriso Interior, outra resposta ficou disponível: adiar a viagem em vez de acelerar.",
            "",
            "Nada mudou na rua. Mudou o estado, e com ele o que eu conseguia ver e escolher.",
            "Voltaremos a essa cena na última aula do módulo, quando o recurso for escolhido de propósito."],
           "Próximo: o que eu escrevi sobre isso.")

d.frase("Antes de perceber",
        "Carregamos padrões que estão funcionando antes de termos capacidade consciente de percebê-los.",
        "Fabiano Deliberalli · Padrões e ressonância, 10/11/2026",
        "LER",
        ["«Carregamos padrões que estão funcionando antes de termos capacidade consciente de percebê-los.»",
         "«Então nos apropriarmos de nosso corpo, de nossa respiração, de nossa energia, de nosso campo de ressonância é uma tarefa das mais importantes e fundamentais na existência humana!»",
         "",
         "No Módulo 2 traduzimos o que aparece.",
         "Agora, o lugar onde o padrão começa a funcionar antes da palavra: o corpo."],
        "Próximo: o que o estado muda.")

d.cartoes("O que o estado muda",
          [("O campo de ação", "As opções que você enxerga naquele momento."),
           ("A memória acessível", "O que vem à lembrança, e o que some."),
           ("A ambivalência suportável", "Quanto de dúvida você aguenta sem decidir às pressas.")],
          "EXPLICAR",
          ["Três coisas mudam com o estado do corpo.",
           "",
           "O campo de ação: cansado ou ameaçado, você enxerga menos saídas.",
           "A memória acessível: o que você sabe pode não vir à lembrança. É o «saber e não acessar» do Módulo 1.",
           "A ambivalência suportável: quanto de dúvida você tolera antes de decidir para acabar com ela.",
           "",
           "Fundamentação, se quiser citar: Varela e Castellanos, sobre a experiência corporificada."],
          "Próximo: a corda.", lead="Não é só cansado ou descansado")

d.frase("A corda",
        "Uma corda, aonde qualquer uma das duas pontas que for puxada, refletirá na outra.",
        "Fabiano Deliberalli · monografia de Medicina Chinesa, 2004",
        "LER",
        ["Em 2004, na monografia de Medicina Chinesa, usei esta imagem para a relação entre o corpo e o Shen, a mente e o espírito.",
         "«Podemos imaginar numa analogia, uma corda, aonde qualquer uma das duas pontas que for puxada, refletirá na outra.»",
         "",
         "É uma via de duas mãos.",
         "Puxe pela ponta do corpo, e a mente muda. Puxe pela ponta da mente, e o corpo muda.",
         "Este módulo puxa pela ponta do corpo."],
        "Próximo: dentro ou fora.", lead="Uma via de duas mãos")

d.comparar("Dentro ou fora",
           "Às vezes o que muda o acesso não está dentro de você",
           [("Recurso interno", "Respirar, a árvore, o Sorriso Interior.", False),
            ("Mudança de condição", "Dormir, comer, pedir ajuda, adiar, mudar de lugar.", False),
            ("A pergunta", "O que esta situação pede: um recurso meu ou outra condição?", True)],
           "EXPLICAR",
           ["Um recurso interno muda o estado por dentro.",
            "Uma mudança de condição muda o que está em volta: o sono, a comida, o apoio, o tempo, o lugar.",
            "",
            "As duas valem. Nenhuma é mais espiritual que a outra.",
            "Quando a condição é o problema, insistir só no recurso interno vira cobrança."],
           "Próximo: um cuidado.")

d.frase("Um cuidado",
        "A sensação mostra o estado. Não mostra o cérebro.",
        "Para ler o corpo sem transformar a sensação em diagnóstico",
        "EXPLICAR",
        ["Ao perceber um estado, evite traduzi-lo em linguagem de cérebro: «é a minha amígdala», «estou no simpático».",
         "A sensação é uma informação valiosa. Ela mostra o estado, não a estrutura que o produz.",
         "",
         "O que nos interessa aqui é o efeito no acesso: o que ficou disponível, o que sumiu."],
        "Próximo: a prática.", dark=True)

d.passo("Prática", "O que está acessível para mim agora?",
        ["Note o estado do corpo.", "Note uma resposta que parece fácil e uma que parece longe.",
         "", "Uma mudança de recurso ou de condição."],
        "AGORA REALIZAR",
        ["Pare um instante. Como está o corpo agora? Uma palavra basta.",
         "Pense numa situação que você vai viver hoje ou amanhã.",
         "Que resposta parece fácil? Qual parece longe?",
         "",
         "Uma mudança possível: um recurso interno ou uma mudança de condição.",
         "",
         "[PAUSA] Pause o vídeo para escrever."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Estado e acesso")

cultivo(d, "Nesta quinzena, note também o estado em que você faz o Cultivo: ele muda o que a árvore oferece.")

d.fechamento("Para guardar",
             ["Quando sustentado com base suficiente, o eixo cria condições para aprofundar a experiência com segurança."],
             ["O corpo muda o que fica acessível.",
              "Recurso interno ou mudança de condição: os dois contam.",
              "Próxima aula: perceber e interpretar sinais internos."],
             "ENCERRAR",
             ["O corpo muda o que fica acessível: o campo de ação, a memória, a ambivalência.",
              "Às vezes o recurso é interno; às vezes a condição precisa mudar.",
              "",
              "«Quando sustentado com base suficiente, ele cria as condições para que um movimento de aprofundamento, ou verticalização, da experiência do ser possa ocorrer de forma segura e integrada.» (Arquitetura Invisível, sobre o eixo)",
              "",
              "Na próxima aula: os sinais internos, e a diferença entre sentir e interpretar."],
             frase_size=22)
d.save(f"{OUT}/TSH · M3.1 · Estado corporal e acesso às respostas.pptx")

# =====================================================================
# M3.2
# =====================================================================
d = Deck("M3.2", "Aula")
d.capa("Interocepção: perceber e interpretar sinais internos", "Sentir e interpretar não são a mesma coisa",
       "ABRIR",
       ["O corpo manda sinais o tempo todo: batimento, respiração, aperto, calor, fome.",
        "Hoje vamos separar três coisas: o sinal, a atenção que damos a ele e o que concluímos dele."],
       "Próximo: o Eu Básico percebe primeiro.", tag="M3.2 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.frase("O Eu Básico percebe primeiro",
        "Percebe antes de simbolizar, capta antes de narrar e sente antes que a separação entre sujeito e objeto esteja claramente estabelecida.",
        "Fabiano Deliberalli · Arquitetura Invisível, cap. 2",
        "LER",
        ["Sobre o Eu Básico, escrevi em Arquitetura Invisível:",
         "«percebe antes de simbolizar, capta antes de narrar e sente antes que a separação entre sujeito e objeto esteja claramente estabelecida.»",
         "",
         "As camadas que o corpo carrega chegam primeiro como sensação.",
         "No mapa da Semente: «Vivemos no piloto automático, longe das sensações e emoções.»"],
        "Próximo: um caso real.")

d.historia("Uma experiência para reconhecer", "ANTES DE UMA CONVERSA IMPORTANTE",
           ["O coração acelera.",
            "Em segundos, isso vira: «estou com medo».",
            "Ou: «isso vai dar errado».",
            "O sinal era só o coração acelerado."],
           "O corpo sente. A mente conclui depressa.",
           "CONTAR",
           ["Se quiser, troque por uma vivência sua com a mesma estrutura.",
            "O caso da dor facial do Banco Fenomenológico ainda está em coleta, sem consentimento confirmado: não usar por enquanto.",
            "",
            "Antes de uma conversa importante, o coração acelera.",
            "Em segundos, a mente já concluiu: «estou com medo», «vai dar errado».",
            "O sinal era o coração acelerado. O resto foi interpretação.",
            "",
            "Sensações incomuns também podem aparecer na prática: perceber e nomear, sem se assustar e sem concluir às pressas."],
           "Próximo: três sentidos.")

d.cartoes("Três sentidos",
          [("Interocepção", "O que vem de dentro: batimento, respiração, fome, aperto."),
           ("Propriocepção", "Onde o corpo está: postura, peso, apoio, movimento."),
           ("Exterocepção", "O que vem de fora: sons, luz, cheiros, o toque.")],
          "EXPLICAR",
          ["Três fontes de informação trabalham juntas.",
           "Interocepção: o que vem de dentro.",
           "Propriocepção: onde o corpo está, o peso, o apoio.",
           "Exterocepção: o que vem de fora.",
           "",
           "Nenhuma vale mais que as outras. Para algumas pessoas, olhar para dentro aumenta a aflição.",
           "Nesses momentos, voltar ao apoio dos pés ou aos sons do ambiente também é cuidar de si."],
          "Próximo: sinal, atenção, interpretação.")

d.sequencia("Sinal, atenção, interpretação",
            ["O sinal: o que o corpo produz", "A atenção: o que você nota", "A interpretação: o que você conclui"],
            "EXPLICAR",
            ["O sinal existe antes de você notar.",
             "A atenção decide o que chega à consciência.",
             "A interpretação dá um sentido: «estou ansioso», «isso é perigo», «é intuição».",
             "",
             "Muitas vezes saltamos do sinal à interpretação sem passar pela descrição.",
             "Coração acelerado vira «estou com medo» antes de ser «coração acelerado».",
             "Fundamentação, se quiser citar: Castellanos e Herrero, sobre interocepção e respiração."],
            "Próximo: a instrução muda o que se sente.",
            foot="Descrever antes de concluir.")

d.frase("A instrução muda o que se sente",
        "A imaginação também muda o corpo.",
        "Hipnose, placebo e expectativa",
        "EXPLICAR",
        ["Uma imagem pode mudar a fisiologia: imaginar o gelo esfria a mão de muita gente.",
         "A expectativa muda a dor: é o que a pesquisa sobre placebo e sobre analgesia hipnótica mostra.",
         "",
         "Isso vale para esta aula: a forma como eu conduzo a atenção muda o que você sente.",
         "Por isso a pergunta não é «sinto certo?», e sim «o que muda quando a instrução muda?»."],
        "Próximo: a prática.", dark=True)

d.passo("Prática", "O que eu sinto, e o que eu concluo?",
        ["Observe a respiração sem mudar nada.", "Depois, conduza uma respiração confortável.",
         "", "Anote a sensação e, à parte, a interpretação."],
        "AGORA REALIZAR",
        ["Primeiro, observe a respiração como está, sem mudar nada. Trinta segundos.",
         "Depois, conduza uma respiração confortável, um pouco mais longa na saída. Trinta segundos.",
         "",
         "O que mudou? Escreva a sensação numa linha, com palavras de corpo: quente, apertado, leve.",
         "Em outra linha, a interpretação: o que você concluiu dela.",
         "Se olhar para dentro trouxer aflição, volte aos pés e aos sons do ambiente.",
         "",
         "[PAUSA] Pause o vídeo para fazer e escrever."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Sensação e interpretação")

cultivo(d, "Na pergunta «o que está me vivendo agora?», comece pela sensação, com palavras de corpo, antes da interpretação.")

d.fechamento("Para guardar",
             ["Sentir é uma coisa. Concluir é outra."],
             ["Sinal, atenção, interpretação.",
              "Dentro, posição e fora: três fontes que se apoiam.",
              "Próxima aula: como o organismo antecipa necessidades."],
             "ENCERRAR",
             ["O corpo sente antes de narrar.",
              "Separar o sinal, a atenção e a interpretação dá espaço para escolher o que fazer com o que se sente.",
              "",
              "Na próxima aula: o organismo como quem prevê e distribui recursos, e o que isso tem a ver com cansaço e descanso."])
d.save(f"{OUT}/TSH · M3.2 · Interocepção - perceber e interpretar sinais internos.pptx")

# =====================================================================
# M3.3
# =====================================================================
d = Deck("M3.3", "Aula")
d.capa("Como o organismo antecipa necessidades e distribui recursos", "Demandas, descanso e capacidade disponível",
       "ABRIR",
       ["O organismo não espera o problema chegar para reagir: ele prevê e se prepara.",
        "Isso protege, e também cobra um preço quando a exigência não para."],
       "Próximo: uma frase de uma palestra minha.", tag="M3.3 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.frase("Preparar, preparar, preparar",
        "Eixo HPA disparado = stress constante!",
        "Fabiano Deliberalli · palestra Qi Gong e Medicina Chinesa, Além das Fronteiras",
        "LER",
        ["Numa palestra sobre Qi Gong e Medicina Chinesa, resumi assim:",
         "«Eixo HPA disparado = stress constante!»",
         "",
         "O eixo do estresse prepara o corpo para lutar ou fugir.",
         "Útil diante de um perigo. Desgastante quando a corrida não termina.",
         "As camadas também são isso: economia de recursos de um organismo que aprendeu a se proteger."],
        "Próximo: regular antecipando.")

d.cartoes("Regular antecipando",
          [("Prever", "O organismo estima o que vem e se prepara antes."),
           ("Distribuir", "Os recursos vão para onde a previsão aponta."),
           ("Recompor", "Descanso, sono, comida e apoio devolvem capacidade.")],
          "EXPLICAR",
          ["A regulação do corpo é sobretudo antecipatória. Na pesquisa, chama-se alostase.",
           "O organismo prevê a demanda e distribui recursos antes que ela chegue.",
           "Lisa Feldman Barrett chama isso de orçamento do corpo.",
           "",
           "Quando a previsão de ameaça não se desliga, o orçamento fica sempre no vermelho.",
           "Descanso não é prêmio: é a parte do orçamento que devolve capacidade."],
          "Próximo: a leitura da Medicina Chinesa.")

d.frase("A leitura da Medicina Chinesa",
        "Algumas técnicas tratam apenas do espírito e se esquecem do corpo e da energia.",
        "Fabiano Deliberalli · Visão Taoísta, tela 25",
        "LER",
        ["Na apresentação Visão Taoísta, escrevi:",
         "«Todos os seres possuem uma quantidade limitada de energia.»",
         "«Temos um limite para armazenamento de energia, sem vazão.»",
         "«Algumas técnicas tratam apenas do espírito e se esquecem do corpo e da energia.»",
         "",
         "Na Medicina Chinesa, o Jing é a reserva. Uma parte vem antes de nós, a pré-celestial; outra se recompõe pela respiração e pelo alimento, a pós-celestial.",
         "A pergunta útil não é «quanto me resta?», e sim «o que me desgasta, o que me nutre e o que me deixa recompor?».",
         "Não é um saldo de vida nem um prognóstico."],
        "Próximo: a sua semana.")

d.comparar("A sua semana",
           "Quatro coisas diferentes, que costumam se misturar",
           [("Aprender", "Exige energia nova: é investimento.", False),
            ("Recuperar-se", "Devolve capacidade: tem valor próprio.", False),
            ("Rever exigências", "Às vezes é preciso pedir menos de si.", False),
            ("Construir apoios", "Pessoas, condições e acordos que dividem a carga.", True)],
           "EXPLICAR",
           ["Olhe para a sua semana com quatro perguntas.",
            "Onde estou aprendendo, e pagando o preço da novidade?",
            "Onde me recupero, de verdade?",
            "Que exigência poderia rever?",
            "Que apoio poderia construir?",
            "",
            "Uma prática individual ajuda. Mudar uma demanda ou um apoio às vezes ajuda mais."],
           "Próximo: a prática.")

d.passo("Prática", "O que desgasta, o que nutre, o que permite recompor?",
        ["Uma demanda da semana.", "Um recurso que nutre.",
         "", "Uma mudança: de demanda, de apoio ou de prática."],
        "AGORA REALIZAR",
        ["Escolha uma demanda desta semana que mais pesa.",
         "Escolha algo que nutre: uma pessoa, um momento, uma prática.",
         "",
         "Agora uma mudança possível: diminuir uma demanda, pedir um apoio ou incluir uma prática.",
         "Escolha uma. Não as três.",
         "",
         "[PAUSA] Pause o vídeo para escrever."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Demanda, recurso e mudança")

cultivo(d, "O Cultivo do Eixo é recomposição: três a cinco minutos que devolvem, não que cobram.")

d.fechamento("Para guardar",
             ["O organismo protege antecipando. Descanso também é parte do caminho."],
             ["Prever, distribuir, recompor.",
              "Uma mudança de demanda ou de apoio vale tanto quanto uma prática.",
              "Próxima aula: mobilização, sobrecarga e repouso."],
             "ENCERRAR",
             ["O organismo regula antecipando, e as camadas também são economia de recursos.",
              "Recompor tem valor próprio.",
              "",
              "Na próxima aula: o sistema nervoso autônomo, e como um mapa pode ajudar a dosar o que fazemos."],
             frase_size=24)
d.save(f"{OUT}/TSH · M3.3 · Como o organismo antecipa necessidades e distribui recursos.pptx")

# =====================================================================
# M3.4
# =====================================================================
d = Deck("M3.4", "Aula")
d.capa("Sistema nervoso autônomo: mobilização, sobrecarga e repouso", "Um mapa para dosar, não para classificar",
       "ABRIR",
       ["O sistema nervoso autônomo regula o que não decidimos: coração, respiração, digestão, prontidão.",
        "Hoje, um mapa dele, com limites, para escolher melhor o que fazer."],
       "Próximo: uma cena de um workshop.", tag="M3.4 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.historia("Um workshop com Siegel", "VIVÊNCIA DO AUTOR",
           ["Um workshop de Daniel Siegel para terapeutas de trauma.",
            "Movimentos de Qi Gong no meio do trabalho.",
            "Quem cuida da dor dos outros também precisa se regular."],
           "O sistema nervoso também se regula em grupo.",
           "CONTAR",
           ["Conte com as suas palavras. Registro: roteiro de abertura da Masterclass e nota falada de M1.1.",
            "",
            "A cena: um workshop de Siegel para terapeutas de trauma, com movimentos de Qi Gong.",
            "Conte o que você viu e viveu ali.",
            "O que a cena mostra para esta aula: regulação não é só individual.",
            "O sistema nervoso também se regula no outro e no grupo. Isso é corregulação."],
           "Próximo: três estados.")

d.cartoes("Três estados",
          [("Mobilização útil", "Prontidão para agir: energia, foco, movimento."),
           ("Sobrecarga", "Agitação que não decide, ou um apagamento que paralisa."),
           ("Repouso e conexão", "Segurança para descansar, digerir e se relacionar.")],
          "EXPLICAR",
          ["Um mapa simples de três estados.",
           "Mobilização útil: o corpo se prepara para agir, e age.",
           "Sobrecarga: a mobilização passa do ponto, ou o corpo desliga.",
           "Repouso e conexão: há segurança para descansar e estar com o outro.",
           "",
           "Fundamentação: a teoria polivagal, de Stephen Porges, e o trabalho de Deb Dana.",
           "A teoria tem críticas científicas, em especial sobre a anatomia e a evolução do vago. Aqui a usamos como mapa clínico útil, não como prova."],
          "Próximo: um mapa precisa mudar a escolha.")

d.dois("Um mapa precisa mudar a escolha",
       ("Classificar", "«Estou no vermelho»"), ("Dosar", "«O que este estado pede agora?»"),
       "em vez de",
       "EXPLICAR",
       ["Mapas de cores são populares, e podem virar rótulo.",
        "«Estou no vermelho», e pronto.",
        "",
        "Um mapa só ajuda se muda o que você faz: mais movimento, menos estímulo, uma pausa, um contato.",
        "Na última aula do módulo, você vai escolher recursos com essa pergunta."],
       "Próximo: o eixo como condição.",
       foot="Nenhum estado vale mais que o outro. Eles não medem o progresso espiritual de ninguém.")

d.frase("O eixo como condição",
        "Sem regulação, segurança e integração, a abertura torna-se instável.",
        "Fabiano Deliberalli · Arquitetura Invisível",
        "LER",
        ["«Sem regulação, segurança e integração, a abertura torna-se instável.»",
         "Nas raízes da Árvore do Eixo: «Sem segurança não há desenvolvimento.»",
         "",
         "Não se trata de ficar sempre em repouso.",
         "O eixo é a condição para que uma abertura, um aprendizado ou uma experiência forte possam ser integrados."],
        "Próximo: no outro.")

d.frase("No outro",
        "O sistema nervoso também se regula no outro.",
        "Corregulação · TCC de neurociências, PUCRS, 2026",
        "EXPLICAR",
        ["No meu TCC de neurociências, a corregulação é um dos eixos do modelo:",
         "experiências intensas se integram melhor quando encontram sustentação relacional.",
         "",
         "Por isso o curso tem encontros ao vivo, e por isso o Módulo 7 trata das relações.",
         "A voz de alguém, uma presença calma, um grupo que respira junto: isso também regula."],
        "Próximo: a prática.", dark=True)

d.passo("Prática", "Num episódio recente, o que o meu corpo pediu?",
        ["Um momento de mobilização.", "Quando passou do ponto, se passou.",
         "", "O que ajudou a voltar, ou o que teria ajudado."],
        "AGORA REALIZAR",
        ["Lembre um episódio recente, de intensidade média. Não o mais difícil.",
         "Onde houve mobilização útil? Passou do ponto em algum momento?",
         "O que ajudou a voltar, ou o que teria ajudado: movimento, pausa, um contato, menos estímulo?",
         "",
         "Se a lembrança pesar, pare, sinta os pés e olhe o ambiente.",
         "",
         "[PAUSA] Pause o vídeo para escrever."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Episódio e dosagem")

cultivo(d, "Se o dia estiver agitado, a árvore pode ser mais curta e a respiração mais lenta: dosar também é praticar.")

d.fechamento("Para guardar",
             ["Um mapa só ajuda quando muda o que você faz."],
             ["Mobilização, sobrecarga, repouso e conexão.",
              "O eixo é condição para integrar a abertura.",
              "Próxima aula: Qi, Jing e Shen, a vitalidade na Medicina Chinesa."],
             "ENCERRAR",
             ["O sistema nervoso autônomo prepara, sobrecarrega e repousa. E se regula também no outro.",
              "O mapa serve para dosar.",
              "",
              "Na próxima aula, outro mapa do mesmo corpo: a vitalidade na Medicina Chinesa."])
d.save(f"{OUT}/TSH · M3.4 · Sistema nervoso autônomo - mobilização, sobrecarga e repouso.pptx")

# =====================================================================
# M3.5
# =====================================================================
d = Deck("M3.5", "Aula")
d.capa("Qi, Jing e Shen: vitalidade e cultivo na Medicina Chinesa", "Uma leitura do ser humano, e não só uma técnica",
       "ABRIR",
       ["Mais de trinta anos de prática corporal e Medicina Chinesa estão por trás desta aula.",
        "Hoje, a Medicina Chinesa como leitura do ser humano: Qi, Jing e Shen, e os Cinco Shen."],
       "Próximo: de onde vem o que eu ensino.", tag="M3.5 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.cartoes("De onde vem o que eu ensino",
          [("A linhagem", "Mestre Liu Pai Lin, que unificou o conhecimento de escolas taoístas, e seus sucessores Liu Chih Ming e Kenichi Shioda."),
           ("A formação", "Com Liu Pai Lin, Kenichi Shioda, Liu Chih Ming, Miguel Martín e Ernesto Garcia; acupuntura com o mestre Liu Chih Ming."),
           ("A clínica", "Vinte e cinco anos de consultório de shiatsu e acupuntura; a monografia de 2004.")],
          "CONTAR",
          ["Conte com as suas palavras a sua trajetória.",
           "",
           "A linhagem: o mestre Liu Pai Lin unificou o conhecimento de escolas taoístas; Liu Chih Ming e Kenichi Shioda são seus sucessores.",
           "A formação: com Liu Pai Lin, Shioda, Liu Chih Ming, Miguel Martín e Ernesto Garcia; a acupuntura com o mestre Liu Chih Ming.",
           "A clínica: vinte e cinco anos de consultório de shiatsu e acupuntura.",
           "",
           "O que eu ensino neste curso vem desse caminho, traduzido para o TSH."],
          "Próximo: o que é o Qi.", dark_idx=(0,))

d.frase("O que é o Qi",
        "Energia é uma medida de transformação.",
        "Marcelo Gleiser, físico, citado na apresentação Visão Taoísta",
        "EXPLICAR",
        ["O ideograma do Qi mostra um grão de arroz sendo cozido, com o vapor subindo.",
         "O arroz é o material, Yin. O vapor é o intangível que sobe, Yang.",
         "Uma panela sobre o fogo: o Qi pode estar em vários estados, como a água.",
         "",
         "Gleiser, físico: «energia é uma medida de transformação».",
         "Por isso falamos do Qi pelo que ele faz: aquecer, mover, transformar, sustentar.",
         "Não é preciso aderir a uma cosmologia para cultivá-lo."],
        "Próximo: os Três Tesouros.", lead="O arroz que cozinha e o vapor que sobe")

d.cartoes("Os Três Tesouros",
          [("Jing", "A reserva: o mais denso. Uma parte vem antes de nós; outra se recompõe."),
           ("Qi", "A energia que circula, aquece e transforma."),
           ("Shen", "A mente e o espírito: o mais sutil.")],
          "EXPLICAR",
          ["Na monografia de 2004: «a integração corpo/mente… é realçada e entendida pelos conceitos de Shen, Tchi e Jing, chamados de Três Tesouros».",
           "E eles «têm uma interação dinâmica onde o estado de um afeta diretamente o outro». É a corda da primeira aula.",
           "",
           "Jing: a reserva, o mais denso. Na tradição, inclui a energia sexual, parte da vitalidade que se conserva e se transforma.",
           "Qi: o que circula e transforma.",
           "Shen: a mente e o espírito, o mais sutil.",
           "",
           "Um cuidado de palavras: na monografia, Jing aparece traduzido como «Essência».",
           "No TSH, a Essência tem outro sentido: o centro que as camadas soterram. Jing e Essência não são a mesma coisa."],
          "Próximo: espírito vestido de matéria.")

d.frase("Espírito vestido de matéria",
        "Somos espírito vestido de matéria. Ou seja, nunca deixamos de ser espírito e nunca habitamos totalmente a matéria.",
        "Fabiano Deliberalli · monografia de Medicina Chinesa, 2004",
        "LER",
        ["«Somos espírito vestido de matéria. Ou seja, nunca deixamos de ser espírito e nunca habitamos totalmente a matéria.»",
         "",
         "O Shen dá a dimensão espiritual do corpo.",
         "A tradição fala de um Shen pré-celestial, não consciente, e de um pós-celestial, consciente.",
         "Cultivar é deixar essas dimensões conversarem."],
        "Próximo: os Cinco Shen.", dark=True)

d.cartoes("Os Cinco Shen",
         [("Shen", "Coração. A mente que reúne."), ("Hun", "Fígado. As imagens, a alma etérea."),
          ("Po", "Pulmão. O corpo que sente, a alma corpórea."), ("Yi", "Baço. A inteligência, o crivo."),
          ("Zhi", "Rim. A força de vontade.")],
         "EXPLICAR",
         ["Na monografia: o Shen «indica o complexo de todos os cinco aspectos mentais e espirituais do ser humano».",
          "",
          "Shen, no Coração: a mente que reúne.",
          "Hun, no Fígado: a alma etérea, o depósito de nossas imagens.",
          "Po, no Pulmão: a alma corpórea, o sentir do corpo.",
          "Yi, no Baço: a inteligência, o crivo que analisa, assimila e integra.",
          "Zhi, no Rim: a força de vontade.",
          "",
          "Hoje é uma visão geral. Cada um volta no curso:",
          "Yi na Tradução e nas escolhas; Zhi na linha do Hara; Hun nos símbolos e na criação; Hun e Po nas experiências incomuns.",
          "É uma leitura própria da tradição, ao lado dos Três Eus, sem ser a mesma coisa."],
         "Próximo: o Sorriso Interior.",
         lead="Uma leitura do ser humano na Medicina Chinesa; cada um volta ao longo do curso",
         foot="Uma leitura da tradição, ao lado dos Três Eus, sem ser a mesma coisa.", dark_idx=(0,))

d.passo("Prática: o Sorriso Interior", "Sorria para dentro.",
        ["Um sorriso leve nos olhos e nos lábios.", "Leve esse sorriso ao coração e ao baixo ventre.",
         "", "Três respirações no baixo ventre."],
        "AGORA REALIZAR",
        ["Sente-se ou fique de pé, confortável.",
         "Um sorriso leve nos olhos e nos lábios, como quem reencontra alguém querido.",
         "Leve esse sorriso para dentro: ao coração, depois ao baixo ventre.",
         "Três respirações no baixo ventre.",
         "",
         "É a mesma prática das aulas abertas e de M1.3, agora com o seu lugar na Medicina Chinesa.",
         "",
         "[PAUSA] Pause o vídeo para praticar dois minutos."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="O que o sorriso mudou",
        pausa="Pause o vídeo para praticar dois minutos.")

cultivo(d, "Na respiração pelos três centros, você passa pelos lugares do Jing, do Qi e do Shen.")

d.fechamento("Para guardar",
             ["Somos espírito vestido de matéria."],
             ["Qi, Jing e Shen: a vitalidade em três tesouros.",
              "Os Cinco Shen: uma leitura do ser humano.",
              "Próxima aula: a postura da árvore."],
             "ENCERRAR",
             ["Qi, Jing e Shen se afetam o tempo todo, como as pontas da corda.",
              "Os Cinco Shen são uma leitura do ser humano que vai voltar ao longo do percurso.",
              "",
              "Na próxima aula, a forma corporal do eixo: o Zhan Zhuang, a postura da árvore."])
d.save(f"{OUT}/TSH · M3.5 · Qi, Jing e Shen - vitalidade e cultivo na Medicina Chinesa.pptx")

# =====================================================================
# M3.6
# =====================================================================
d = Deck("M3.6", "Prática")
d.capa("Zhan Zhuang: aprender a postura da árvore", "O eixo como postura",
       "ABRIR",
       ["Você já esteve na árvore: nas aulas abertas, em M1.3 e no encontro de abertura de M2.",
        "Hoje ela ganha estrutura: raiz, soltura, eixo e os três centros."],
       "Próximo: como as árvores.", tag="M3.6 · PRÁTICA · ZHAN ZHUANG")

d.frase("Como as árvores",
        "Nós seres humanos somos como as árvores: temos uma extremidade enraizada no solo e outra estendendo-se para o céu.",
        "Alexander Lowen, citado por Fabiano na palestra Aterramento, 2022",
        "LER",
        ["Na palestra Aterramento, em 2022, citei Lowen:",
         "«Nós seres humanos somos como as árvores: temos uma extremidade enraizada no solo e outra estendendo-se para o céu.»",
         "",
         "Zhan Zhuang: «permanecer quieto como uma árvore».",
         "É o eixo como postura."],
        "Próximo: os princípios da prática.")

d.cartoes("Os princípios da prática",
          [("Estabilidade", "Os pés sustentam; o peso desce."),
           ("Song", "Soltar o que não é necessário para ficar de pé."),
           ("Lentidão", "Sem pressa de chegar a uma forma."),
           ("Alinhar o corpo", "Do alto da cabeça ao períneo, uma linha.")],
          "EXPLICAR",
          ["Na linhagem do mestre Liu Pai Lin, a prática tem nove princípios, que ele desenhou em caligrafia:",
           "respeito, serenidade, estabilidade, relaxamento, suavidade, movimento circular, lentidão, equilíbrio e alinhar o corpo.",
           "",
           "Hoje usamos quatro.",
           "Estabilidade: os pés sustentam.",
           "Song, o relaxamento: soltar o esforço que não é necessário.",
           "Lentidão: sem pressa.",
           "Alinhar o corpo: uma linha do alto da cabeça ao períneo.",
           "Os nove estão no apoio do aluno."],
          "Próximo: a sequência.", lead="Quatro dos nove princípios da linhagem Pai Lin")

d.sequencia("A sequência",
            ["Wu Chi: em pé, parado", "Raiz: o peso nos pés", "A árvore: braços em roda", "Os três centros", "Fechar no baixo ventre"],
            "DEMONSTRAR",
            ["Demonstre cada passo, devagar.",
             "",
             "Wu Chi: em pé, pés na largura do quadril, joelhos destravados.",
             "Raiz: sinta o peso descer pelos pés, como raízes.",
             "A árvore: braços em roda à frente do peito, como abraçando um tronco.",
             "Os três centros: baixo ventre, peito, testa, um de cada vez.",
             "Fechar: mãos sobre o baixo ventre, três respirações.",
             "",
             "Alternativas: sentado numa cadeira, ou com os braços mais baixos. A versão viável é a certa."],
            "Próximo: onde há esforço a mais.")

d.comparar("Onde há esforço a mais",
           "Sustentar não é se esforçar",
           [("Sustentação", "O que mantém você de pé: pés, pernas, a linha do eixo.", False),
            ("Esforço dispensável", "Ombros, mandíbula, testa, respiração presa.", False),
            ("O ajuste", "Mude uma coisa, e observe o efeito no conjunto.", True)],
           "EXPLICAR",
           ["Na árvore, perceba o que sustenta e o que é esforço a mais.",
            "Ombros subindo, mandíbula presa, testa franzida, respiração curta.",
            "",
            "Ajuste uma coisa por vez e observe o efeito no corpo todo.",
            "Não há postura ideal obrigatória. A repetição aprofunda a percepção; não precisa de movimentos espetaculares."],
           "Próximo: a prática.")

d.passo("Prática: três minutos de árvore", "O que me sustenta?",
        ["Wu Chi, raiz, árvore.", "Passe pelos três centros.",
         "", "Feche no baixo ventre."],
        "AGORA REALIZAR",
        ["Vamos juntos, três minutos.",
         "Wu Chi. Raiz. A árvore.",
         "Respire passando pelos três centros: baixo ventre, peito, testa.",
         "Perceba um esforço a mais e solte um pouco.",
         "Feche com as mãos no baixo ventre, três respirações.",
         "",
         "Se surgir tontura ou dor, sente-se e continue sentado.",
         "",
         "[PAUSA] Ou pause o vídeo e pratique no seu ritmo."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="O que me sustenta",
        pausa="Pratique junto com o vídeo, ou pause e faça no seu ritmo.")

cultivo(d, "A árvore desta aula é o centro do Cultivo do Eixo do Módulo 3.")

d.fechamento("Para guardar",
             ["A árvore não mede o seu progresso espiritual. Ela é um lugar para voltar."],
             ["Estabilidade, Song, lentidão, alinhar o corpo.",
              "Uma versão viável, todos os dias.",
              "Próxima aula: o Qi Gong em movimento."],
             "ENCERRAR",
             ["A árvore organiza o eixo no corpo: raiz embaixo, céu em cima, os três centros na linha.",
              "Os três centros preparam a linha do Hara, que vem em M4.6.",
              "",
              "Na próxima aula: a árvore entra em movimento, com Sustentar o Céu e Separar Céu e Terra."],
             frase_size=24)
d.save(f"{OUT}/TSH · M3.6 · Zhan Zhuang - aprender a postura da árvore.pptx")

# =====================================================================
# M3.7
# =====================================================================
d = Deck("M3.7", "Prática")
d.capa("Qi Gong: postura, movimento, respiração e intenção", "Sustentar o Céu e Separar Céu e Terra",
       "ABRIR",
       ["A árvore entra em movimento.",
        "Dois movimentos do Ba Duan Jin, na versão que eu ensino: Sustentar o Céu, já vivido em M1.3, e Separar Céu e Terra."],
       "Próximo: traduzir a energia.", tag="M3.7 · PRÁTICA · QI GONG")

d.frase("Traduzir a energia",
        "Temos que aprender conscientemente a traduzir o que hoje chamamos de energia como nossos sentidos internos originais.",
        "Fabiano Deliberalli · palestra Aterramento, 2022",
        "LER",
        ["Na palestra Aterramento, em 2022:",
         "«Temos que aprender conscientemente a traduzir, o que hoje chamamos de energia, como nossos sentidos internos originais.»",
         "",
         "O Qi Gong é isso: postura, movimento, respiração e intenção juntos, para perceber por dentro."],
        "Próximo: entre o Céu e a Terra.")

d.dois("Entre o Céu e a Terra",
       ("Céu", "Braços voltados para cima: recebem"), ("Terra", "Pés voltados para baixo: recebem"),
       "o ser humano no meio",
       "EXPLICAR",
       ["Uma figura antiga da tradição mostra o ser humano entre o Céu e a Terra.",
        "Com as extremidades de cima voltadas ao céu, recebe a energia do Céu, Yang.",
        "Com as de baixo voltadas à terra, recebe a energia da Terra, Yin.",
        "No meio, uma balança em equilíbrio dinâmico.",
        "",
        "É o sentido dos dois movimentos de hoje."],
       "Próximo: Sustentar o Céu.",
       foot="Uma balança em equilíbrio dinâmico.")

d.sequencia("Sustentar o Céu",
            ["Mãos entrelaçadas à frente do ventre", "Subir pelas linhas do corpo", "Palmas para o céu, inspirando", "Descer pelos lados, expirando"],
            "DEMONSTRAR",
            ["Demonstre na sua versão; os passos da tela são só o resumo. De frente e de lado.",
             "",
             "Mãos entrelaçadas à frente do baixo ventre.",
             "Subir pela frente do corpo; na altura do peito, girar as palmas.",
             "Palmas para o céu, inspirando, como quem sustenta o céu.",
             "Soltar e descer pelos lados, expirando.",
             "",
             "Ajuste a amplitude: braços mais baixos valem. Repetir de três a seis vezes."],
            "Próximo: Separar Céu e Terra.")

d.sequencia("Separar Céu e Terra",
            ["Mãos à frente do ventre", "Uma sobe, a outra desce", "Empurrar o céu e a terra", "Trocar os lados"],
            "DEMONSTRAR",
            ["Demonstre na sua versão; os passos da tela são só o resumo.",
             "",
             "Mãos à frente do baixo ventre, palmas para cima.",
             "Uma mão sobe e empurra o céu; a outra desce e empurra a terra.",
             "Inspire ao separar; expire ao voltar.",
             "Troque os lados. De três a seis vezes de cada lado.",
             "",
             "Se o ombro reclamar, faça menor."],
            "Próximo: conduzir, sustentar, acompanhar.")

d.cartoes("Conduzir, sustentar, acompanhar",
          [("Conduzir", "Você dirige o movimento e a respiração."),
           ("Sustentar", "Você mantém a forma e a atenção."),
           ("Acompanhar", "Você deixa o movimento acontecer e observa.")],
          "EXPLICAR",
          ["No mesmo movimento, três modos de participar.",
           "Conduzir: você dirige.",
           "Sustentar: você mantém.",
           "Acompanhar: você deixa acontecer e observa.",
           "",
           "Entrar por escolha nesse estado de atenção concentrada é o transe escolhido, a auto-hipnose que você começa a praticar neste módulo.",
           "Para sair: conte de um a três, sinta os pés, abra os olhos."],
          "Próximo: a prática.")

d.passo("Prática: os dois movimentos", "Como estou participando agora?",
        ["Árvore por um minuto.", "Sustentar o Céu, três vezes.", "Separar Céu e Terra, três de cada lado.",
         "Fechar no baixo ventre."],
        "AGORA REALIZAR",
        ["Vamos juntos.",
         "Um minuto de árvore.",
         "Sustentar o Céu, três vezes.",
         "Separar Céu e Terra, três de cada lado.",
         "Feche no baixo ventre, três respirações.",
         "",
         "Ao fim: você conduziu, sustentou ou acompanhou?",
         "Para sair: um, dois, três, sinta os pés, abra os olhos.",
         "",
         "[PAUSA] Ou pause o vídeo e pratique no seu ritmo."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Como participei",
        pausa="Pratique junto com o vídeo, ou pause e faça no seu ritmo.")

cultivo(d, "Sustentar o Céu, três vezes, entra no seu Cultivo do Eixo, se quiser.")

d.fechamento("Para guardar",
             ["Postura, movimento, respiração e intenção: o eixo em movimento."],
             ["Sustentar o Céu e Separar Céu e Terra.",
              "Conduzir, sustentar, acompanhar.",
              "Próxima aula: escolher e adaptar recursos de retorno."],
             "ENCERRAR",
             ["O Qi Gong organiza o eixo em movimento, entre o Céu e a Terra.",
              "A mesma sequência vai voltar em M4, M5 e M7, com outras perguntas.",
              "",
              "Na próxima aula: reunir o que você aprendeu e escolher um recurso de retorno."],
             frase_size=24)
d.save(f"{OUT}/TSH · M3.7 · Qi Gong - postura, movimento, respiração e intenção.pptx")

# =====================================================================
# M3.8
# =====================================================================
d = Deck("M3.8", "Aula")
d.capa("Retorno à orientação: escolher e adaptar recursos", "Retornar não é regredir",
       "ABRIR",
       ["Fecha o Módulo 3.",
        "Você aprendeu vários recursos. Hoje, como escolher, dosar e adaptar o que a situação pede."],
       "Próximo: retornar não é regredir.", tag="M3.8 · GANHAR EIXO E PRESENÇA · 1 DE 4")

d.frase("Retornar não é regredir",
        "Retornar não é regredir.",
        "Fabiano Deliberalli · Registro Mestre de Formulações",
        "LER",
        ["«Retornar não é regredir.»",
         "No caminho de descida, subida e retorno, o retorno vem «refinado»: «o retorno da consciência, mas com a experiência incorporada».",
         "",
         "Voltar ao eixo é um recurso escolhido, não uma regra.",
         "Lembra a cena do trânsito, na primeira aula? Agora o recurso é escolhido de propósito."],
        "Próximo: o seu repertório.")

d.cartoes("O seu repertório",
          [("Orientar", "Os pés, o olhar no ambiente, a contagem 5-4-3-2-1 pelos sentidos."),
           ("Acalmar", "Três respirações no baixo ventre; o Sorriso Interior."),
           ("Mobilizar", "Sustentar o Céu; Separar Céu e Terra."),
           ("Sustentar", "A árvore; as duas mãos, uma no peito e outra no ventre.")],
           "EXPLICAR",
           ["Orientar: voltar ao aqui. Os pés, o olhar, a técnica 5-4-3-2-1: cinco coisas que vejo, quatro que ouço, três que toco, duas que cheiro, uma que provo.",
            "Acalmar: respiração no baixo ventre, o Sorriso Interior.",
            "Mobilizar: os movimentos do Qi Gong.",
            "Sustentar: a árvore; as duas mãos, uma no peito e outra no baixo ventre, como cuidado do Eu Básico.",
            "",
            "Opcional, para quem gosta: o relaxamento progressivo de Jacobson, ou a pressão de um cobertor pesado."],
           "Próximo: a pergunta que escolhe.", lead="Cada recurso serve a uma finalidade", dark_idx=(3,))

d.sequencia("A pergunta que escolhe",
            ["O que esta situação pede?", "Qual recurso responde a isso?", "Quanto, e por quanto tempo?", "Quando parar ou trocar?"],
            "EXPLICAR",
            ["Quatro perguntas para escolher.",
             "O que a situação pede: orientar, acalmar, mobilizar, sustentar?",
             "Qual recurso responde a isso?",
             "Quanto: um minuto, três, dez?",
             "Quando parar ou trocar: se piorar, se não mudar nada, se precisar de outra pessoa.",
             "",
             "E lembre da primeira aula: às vezes a resposta é mudar uma condição, não usar um recurso."],
            "Próximo: um ponto no ambiente.")

d.frase("Um ponto no ambiente",
        "Onde está, no teu ambiente, a sensação de tranquilização?",
        "Fabiano Deliberalli · prática de 05/07/2025",
        "EXPLICAR",
        ["Uma pergunta que uso desde 2025:",
         "«Onde está, no teu ambiente, a sensação de tranquilização?»",
         "",
         "Deixe o olhar encontrar um ponto que acalma. Fique nele algumas respirações.",
         "É um recurso de bolso: cabe numa reunião, no trânsito, numa conversa difícil.",
         "Programe antes o tempo: «três respirações, e volto»."],
        "Próximo: a prática.", dark=True)

d.passo("Prática", "Qual é o meu recurso de bolso?",
        ["Escolha uma situação da semana.", "O que ela pede.",
         "Um recurso, uma dose, um sinal para parar."],
        "AGORA REALIZAR",
        ["Escolha uma situação da próxima semana que costuma tirar você do eixo.",
         "O que ela pede: orientar, acalmar, mobilizar ou sustentar?",
         "Escolha um recurso, a dose e o sinal para parar ou trocar.",
         "E, se couber, uma condição a mudar.",
         "",
         "[PAUSA] Pause o vídeo para escrever."],
        "Próximo: o Cultivo do Eixo desta quinzena.", registro="Meu recurso de bolso")

cultivo(d, "Escolha, a cada dia, o recurso de retorno que vai levar: ele é a última parte do Cultivo do Eixo deste módulo.")

d.fechamento("Fecho do Módulo 3",
             ["Algumas camadas estão no corpo. Agora você tem lugares para voltar."],
             ["O corpo muda o que fica acessível.",
              "Árvore, Qi Gong e recursos escolhidos.",
              "No Módulo 4: emoções e padrões que um dia protegeram."],
             "ENCERRAR",
             ["Neste módulo, o corpo: o estado, os sinais internos, o orçamento do organismo, o sistema nervoso, a Medicina Chinesa, a árvore e o Qi Gong.",
              "Foi o começo da segunda direção do percurso: ganhar eixo e presença.",
              "",
              "No Módulo 4, as emoções: dar expressão, distinguir, nomear, e olhar para os padrões que um dia protegeram.",
              "",
              "«A Essência é o destino. O EIXO é o caminho.»"],
             frase_size=24)
d.save(f"{OUT}/TSH · M3.8 · Retorno à orientação - escolher e adaptar recursos.pptx")
print("ok")
