from base import *

OUT = "/home/claude/out/m0"
os.makedirs(OUT, exist_ok=True)
# Imagem: pdftoppm -r 170 -png -f 1 -l 1 "80 - Mapas Conceituais/PDF/2026-07-18/O-caminho-da-semente.pdf" img/semente
# (o PNG original no repositório está corrompido; usar o PDF). Usa base.py de "Módulo 2/Slides de gravação 29-11/Fontes".
SEMENTE = "img/semente-1.png"

d = Deck("M0", "Boas-vindas · complementar")

# 1
d.capa("O percurso e a prática de todos os dias",
       "Para onde o curso vai, e o que você faz entre uma aula e outra",
       "ABRIR",
       ["Esta aula vem logo depois da aula de boas-vindas.",
        "Ali você conheceu a minha trajetória e escreveu a sua pergunta inicial.",
        "",
        "Aqui, em poucos minutos: para onde o percurso vai, e o que você vai fazer todos os dias.",
        "E já vamos praticar juntos, um minuto, antes do fim."],
       "Próximo: a pergunta do curso.", tag="MÓDULO 0 · BOAS-VINDAS · AULA COMPLEMENTAR")

# 2
d.frase("A pergunta do curso",
        "Ou trabalhamos voluntariamente ou somos vividos pelos padrões que carregamos.",
        "Fabiano Deliberalli · anotação de 17/07/2021",
        "LER",
        ["A pergunta que atravessa o curso: por que entendemos os nossos padrões e continuamos repetindo?",
         "",
         "«Ou trabalhamos voluntariamente ou somos vividos pelos padrões que carregamos.»",
         "",
         "Ser vivido por um padrão não é falta de inteligência nem de esforço.",
         "O padrão age antes de a compreensão chegar. Por isso o curso trabalha com o corpo, com a prática e com a vida, e não só com ideias."],
        "Próximo: o mapa que eu desenhei para esse caminho.", lead="Por que entendemos os nossos padrões e continuamos repetindo?")

# 3 — O Caminho da Semente (mapa do autor, julho de 2026)
s = d._new()
d._chrome(s, "O Caminho da Semente")
pic(s, SEMENTE, 0.62, 1.8, h=5.0, back=False)
d.text(s, 4.35, 1.95, 8.2, 0.9, "A Essência é o destino. O eixo é o caminho.", size=26, font=SERIF, color=EST)
d.text(s, 4.35, 2.95, 8.0, 1.6,
       "«A vida acontece, e nos afastamos do nosso centro. O caminho de volta é lembrar, integrar e expressar quem realmente somos.»",
       size=19, color=NOT, italic=True, line=1.15)
rect(s, 4.35, 4.65, 8.15, 1.45, fill=PET, rounded=0.06)
d.text(s, 4.6, 4.72, 7.7, 1.3,
       "Não é uma escada. Vamos e voltamos. Perder o eixo não significa perder o percurso.",
       size=19, color="FFFFFF", anchor="ctr", line=1.12)
d.text(s, 4.35, 6.35, 8.0, 0.35, "Mapa de Fabiano Deliberalli, julho de 2026", size=10, color=MUTED)
d._footer(s)
d.notes(s, "O Caminho da Semente", "MOSTRAR",
        ["Este é um mapa que eu fiz em julho de 2026: O Caminho da Semente.",
         "«A Essência é o destino. O eixo é o caminho.»",
         "",
         "A Essência está presente desde o início. Ao longo da vida, ela vai sendo soterrada por camadas:",
         "padrões automáticos, feridas, defesas e máscaras, desconexão entre corpo e mente, sobrecarga, condicionamentos.",
         "O eixo é o caminho de volta a ela.",
         "",
         "Um cuidado: o desenho parece uma escada, mas o percurso não é linear.",
         "Vamos e voltamos, como um pêndulo; voltamos aos mesmos temas em outro lugar, como numa espiral.",
         "Perder o eixo não significa perder o percurso."],
        "Próximo: as três direções do curso.")

# 4
d.sequencia("O mapa do percurso",
            ["Traduzir\nMódulos 1 e 2", "Ganhar eixo e presença\nMódulos 3 a 6", "Ocupar o próprio espaço\nMódulos 7 e 8"],
            "MOSTRAR",
            ["Nas minhas palavras: «precisamos primeiro traduzir o que temos em nossos padrões e depois trabalhar para ganhar eixo e presença suficientes para ocupar nosso real espaço».",
             "",
             "Traduzir, nos Módulos 1 e 2: reconhecer o que acontece em você, em camadas.",
             "Ganhar eixo e presença, do 3 ao 6: corpo, emoções, valores e espiritualidade, integração.",
             "Ocupar o próprio espaço, no 7 e no 8: relações, limites, autonomia.",
             "",
             "As três direções se alimentam. Traduzir ajuda a ganhar eixo, e o eixo ajuda a traduzir."],
            "Próximo: uma habilidade que atravessa as três direções.",
            lead="Nove módulos, 59 aulas, três direções",
            foot="As três direções não são etapas em fila: elas se alimentam.")

# 5
d.comparar("A auto-hipnose no percurso",
           "Os padrões funcionam como transes que não escolhemos. A auto-hipnose ensina a escolher.",
           [("TRADUZIR", "Reconhecer o transe que não se escolhe.", False),
            ("GANHAR EIXO", "Praticar o transe escolhido: atenção concentrada, por escolha.", False),
            ("OCUPAR O ESPAÇO", "Ensaiar a nova resposta e projetá-la no futuro.", True)],
           "EXPLICAR",
           ["«Somos vividos pelos padrões que carregamos.» Um padrão funciona como um transe que não escolhemos.",
            "A auto-hipnose é uma habilidade que você aprende: entrar, por escolha, num estado de atenção concentrada.",
            "",
            "Ela acompanha as três direções:",
            "ao traduzir, você reconhece o transe que não escolheu;",
            "ao ganhar eixo, pratica o transe escolhido;",
            "ao ocupar o seu espaço, ensaia a nova resposta e a projeta no futuro.",
            "",
            "As induções são conduzidas nos encontros ao vivo e retomadas nos módulos.",
            "Cuidado: não pratique dirigindo ou operando máquinas. Em crise, dissociação grave ou trauma desestabilizado, converse antes com o seu profissional de saúde."],
           "Próximo: a prática de todos os dias, agora.")

# 6
d.passo("Cultivo do Eixo: um minuto, agora",
        "O que está me vivendo agora?",
        ["De pé, os pés na largura dos ombros.", "Joelhos soltos, braços em roda: a árvore.",
         "Três respirações no baixo ventre."],
        "CONDUZIR",
        ["[PRÁTICA, cerca de 1 min 30] Conduza do começo ao fim. Tela parada.",
         "",
         "«Fique de pé, se puder. Os pés na largura dos ombros. Joelhos soltos.»",
         "«Os braços em roda, como se abraçassem uma árvore.»",
         "[PAUSA] 15 segundos em silêncio.",
         "«Pergunte para si: o que está me vivendo agora?»",
         "[PAUSA] 15 segundos em silêncio.",
         "«Três respirações no baixo ventre.» Respire junto, em voz baixa: «um… dois… três».",
         "«Isso é o Cultivo do Eixo. Todos os dias, de três a cinco minutos. A versão completa está na aula Comece pelo corpo.»"],
        "Próximo: o Caderno e o Retorno ao Eixo.",
        pausa="Faça comigo agora.")

# 7
d.cartoes("Entre uma aula e outra",
          [("Cultivo do Eixo", "Todos os dias, de três a cinco minutos. Cada módulo traz uma versão."),
           ("Retorno ao Eixo", "No momento real, 30 segundos: o primeiro sinal, os pés, três respirações."),
           ("Caderno de Reencontros", "Uma página por quinzena. Escrever é opcional; o Caderno é só seu.")],
          "APRESENTAR",
          ["Três coisas acompanham você entre as aulas.",
           "",
           "O Cultivo do Eixo, todos os dias, de três a cinco minutos. A cada módulo, uma versão nova.",
           "O Retorno ao Eixo, no momento em que a vida acontece: notar o primeiro sinal, sentir os pés, três respirações no baixo ventre, e perguntar «o que está ao meu alcance agora?».",
           "O Caderno de Reencontros: a sua pergunta inicial, um reencontro por quinzena e, em três momentos do curso, a pergunta de progresso.",
           "",
           "Escrever é sempre opcional. A prática é o que conta."],
          "Próximo: como seguir.", dark_idx=(0,))

# 8
d.cartoes("Como seguir",
          [("Um módulo por quinzena", "As aulas são curtas. A prática vem guiada nos vídeos: é só fazer junto."),
           ("Encontros ao vivo", "Um por módulo: dúvidas na primeira hora, prática na segunda. A gravação fica aqui."),
           ("Caminho mínimo", "Pouco tempo? Cada módulo indica duas aulas e o Cultivo do Eixo. Não existe atraso.")],
          "ORIENTAR",
          ["Um módulo por quinzena. O calendário da turma está em anexo.",
           "As práticas vêm guiadas dentro dos vídeos: é só fazer junto comigo.",
           "",
           "Um encontro ao vivo por módulo: a primeira hora para dúvidas, a segunda para prática. A gravação fica na plataforma.",
           "",
           "E se a quinzena apertar: a descrição de cada módulo indica um caminho mínimo, duas aulas e o Cultivo do Eixo.",
           "Não existe atraso. Um pouco por dia vale mais do que tudo de uma vez.",
           "",
           "Este curso é educacional. Não substitui psicoterapia nem cuidados de saúde."],
          "Próximo: o fechamento.")

# 9
d.fechamento("Para começar",
             "Perder o eixo não significa perder o percurso.",
             ["A próxima aula é «Comece pelo corpo»: a postura da árvore, completa.",
              "Depois, o Módulo 1: traduzir."],
             "FECHAR",
             ["A próxima aula é «Comece pelo corpo»: a postura da árvore, por inteiro.",
              "Depois, o Módulo 1.",
              "",
              "E se em algum momento você perder o ritmo, lembre:",
              "«Perder o eixo não significa perder o percurso.»",
              "",
              "Seja bem-vindo, seja bem-vinda."])

d.save(f"{OUT}/TSH · M0 · O percurso e a prática de todos os dias.pptx")
import json
json.dump(d.guide, open(f"{OUT}/guia.json", "w"), ensure_ascii=False)
print("ok", d.n)
