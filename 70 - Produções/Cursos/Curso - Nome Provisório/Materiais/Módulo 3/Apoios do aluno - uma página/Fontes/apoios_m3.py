import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm
from caderno import base, h, par, NOT, OURO, MUTED
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apoios_m3')
MAPA = 'Mapa do percurso: Traduzir → Ganhar eixo e presença → Ocupar o próprio espaço · Você está em: Ganhar eixo e presença (1 de 4)'
CULTIVO = 'Cultivo do Eixo desta quinzena (todos os dias, 3 a 5 minutos): na árvore, respire passando pelos três centros (baixo ventre, peito, testa); se quiser, Sustentar o Céu três vezes; escolha o recurso de retorno do dia. No momento real, o Retorno ao Eixo: notar o primeiro sinal, sentir os pés, três respirações, «o que está ao meu alcance agora?».'
AULAS = [
 ("3.1", "Estado corporal e acesso às respostas",
  "O corpo muda o que fica acessível: as opções que você enxerga, o que vem à lembrança e quanto de dúvida você suporta. Às vezes ajuda um recurso interno; às vezes, mudar uma condição.",
  "«Carregamos padrões que estão funcionando antes de termos capacidade consciente de percebê-los.» — Fabiano, Padrões e ressonância. «Uma corda, aonde qualquer uma das duas pontas que for puxada, refletirá na outra.» — Fabiano, monografia de Medicina Chinesa, 2004",
  ["Note o estado do corpo agora, em uma palavra.", "Pense numa situação de hoje ou amanhã.", "Que resposta parece fácil? Qual parece longe?", "Escolha uma mudança: um recurso interno ou uma condição (sono, comida, apoio, tempo, lugar)."],
  "Anote: estado, resposta fácil, resposta distante e a mudança escolhida."),
 ("3.2", "Interocepção: perceber e interpretar sinais internos",
  "O sinal do corpo, a atenção que damos a ele e o que concluímos dele são três coisas diferentes. Descrever antes de concluir abre espaço para escolher.",
  "O Eu Básico «percebe antes de simbolizar, capta antes de narrar e sente antes que a separação entre sujeito e objeto esteja claramente estabelecida». — Fabiano, Arquitetura Invisível",
  ["Observe a respiração sem mudar nada, por trinta segundos.", "Conduza uma respiração confortável, um pouco mais longa na saída, por trinta segundos.", "Escreva a sensação com palavras de corpo (quente, apertado, leve).", "Em outra linha, escreva o que você concluiu dela."],
  "Separe em duas linhas: «o que eu sinto» e «o que eu concluo». Se olhar para dentro trouxer aflição, volte aos pés e aos sons do ambiente."),
 ("3.3", "Como o organismo antecipa necessidades e distribui recursos",
  "O organismo prevê e se prepara antes que a demanda chegue. Isso protege, e cobra um preço quando a exigência não para. Descanso e apoio devolvem capacidade.",
  "«Algumas técnicas tratam apenas do espírito e se esquecem do corpo e da energia.» — Fabiano, Visão Taoísta. Na Medicina Chinesa, a pergunta é: o que desgasta, o que nutre e o que permite recompor?",
  ["Escolha a demanda desta semana que mais pesa.", "Escolha algo que nutre: uma pessoa, um momento, uma prática.", "Escolha uma mudança: diminuir uma demanda, pedir um apoio ou incluir uma prática.", "Só uma das três."],
  "Anote a demanda, o recurso que nutre e a mudança escolhida, e confira na próxima semana."),
 ("3.4", "Sistema nervoso autônomo: mobilização, sobrecarga e repouso",
  "Mobilização útil, sobrecarga e repouso com conexão: um mapa que serve para dosar o que fazer, não para classificar. O sistema nervoso também se regula no outro.",
  "«Sem regulação, segurança e integração, a abertura torna-se instável.» — Fabiano, Arquitetura Invisível",
  ["Lembre um episódio recente de intensidade média.", "Onde houve mobilização útil? Passou do ponto?", "O que ajudou a voltar, ou o que teria ajudado: movimento, pausa, um contato, menos estímulo?", "Se a lembrança pesar, pare, sinta os pés e olhe o ambiente."],
  "Escreva o episódio e a dosagem que ajudaria da próxima vez."),
 ("3.5", "Qi, Jing e Shen: vitalidade e cultivo na Medicina Chinesa",
  "A Medicina Chinesa como leitura do ser humano. Os Três Tesouros: Jing (a reserva; na tradição, inclui a energia sexual), Qi (o que circula e transforma) e Shen (a mente e o espírito). Os Cinco Shen: Shen (Coração), Hun (Fígado, as imagens), Po (Pulmão, o corpo que sente), Yi (Baço, a inteligência), Zhi (Rim, a vontade).",
  "«Somos espírito vestido de matéria. Ou seja, nunca deixamos de ser espírito e nunca habitamos totalmente a matéria.» — Fabiano, monografia de Medicina Chinesa, 2004. Jing e a Essência do TSH não são a mesma coisa.",
  ["Sente-se ou fique de pé, confortável.", "Um sorriso leve nos olhos e nos lábios.", "Leve esse sorriso ao coração e depois ao baixo ventre.", "Três respirações no baixo ventre."],
  "Anote o que o Sorriso Interior mudou: no corpo, na emoção ou no pensamento."),
 ("3.6", "Zhan Zhuang: aprender a postura da árvore",
  "Zhan Zhuang: «permanecer quieto como uma árvore». O eixo como postura: raiz nos pés, linha do alto da cabeça ao períneo, os três centros. Os nove princípios da linhagem Pai Lin: respeito, serenidade, estabilidade, relaxamento (Song), suavidade, movimento circular, lentidão, equilíbrio e alinhar o corpo.",
  "«Nós seres humanos somos como as árvores: temos uma extremidade enraizada no solo e outra estendendo-se para o céu.» — Lowen, citado por Fabiano na palestra Aterramento, 2022",
  ["Wu Chi: em pé, pés na largura do quadril, joelhos destravados.", "Raiz: o peso desce pelos pés.", "A árvore: braços em roda; respire passando pelos três centros.", "Feche com as mãos no baixo ventre, três respirações. Sentado também vale."],
  "Anote o que sustenta você na postura e um esforço a mais que conseguiu soltar."),
 ("3.7", "Qi Gong: postura, movimento, respiração e intenção",
  "A árvore em movimento, entre o Céu e a Terra: Sustentar o Céu e Separar Céu e Terra. No mesmo movimento, três modos de participar: conduzir, sustentar e acompanhar. Entrar por escolha nesse estado de atenção é o transe escolhido, a auto-hipnose.",
  "«Temos que aprender conscientemente a traduzir, o que hoje chamamos de energia, como nossos sentidos internos originais.» — Fabiano, palestra Aterramento, 2022",
  ["Um minuto de árvore.", "Sustentar o Céu, três vezes.", "Separar Céu e Terra, três vezes de cada lado.", "Feche no baixo ventre; para sair, conte um, dois, três e sinta os pés."],
  "Anote como você participou: conduzindo, sustentando ou acompanhando."),
 ("3.8", "Retorno à orientação: escolher e adaptar recursos",
  "Cada recurso serve a uma finalidade: orientar (pés, olhar, 5-4-3-2-1), acalmar (respiração, Sorriso Interior), mobilizar (Qi Gong) ou sustentar (árvore, as duas mãos). Escolher é perguntar o que a situação pede, quanto e quando parar.",
  "«Retornar não é regredir.» — Fabiano, Registro Mestre. «Onde está, no teu ambiente, a sensação de tranquilização?» — Fabiano",
  ["Escolha uma situação da próxima semana que costuma tirar você do eixo.", "O que ela pede: orientar, acalmar, mobilizar ou sustentar?", "Escolha um recurso, a dose e o sinal para parar ou trocar.", "Se couber, uma condição a mudar."],
  "Preencha o «Reencontro da quinzena» do Módulo 3 antes do encontro de 09/01 e traga o caderno."),
]
for cod, tit, ideia, raiz, passos, cad in AULAS:
    doc = Document(); base(doc)
    par(doc, 'Traduzindo o Ser Humano · Módulo 3 · Apoio do aluno', 9, False, OURO, 2)
    h(doc, f'Aula {cod} — {tit}', 18, NOT, 0, 4)
    par(doc, MAPA, 8.5, True, MUTED, 10)
    h(doc, 'A ideia', 12, OURO, 4, 2); par(doc, ideia)
    h(doc, 'Raiz', 12, OURO, 6, 2); par(doc, raiz, 11, True)
    h(doc, 'Prática', 12, OURO, 6, 2)
    for i, t in enumerate(passos, 1):
        q = par(doc, f'{i}. {t}'); q.paragraph_format.left_indent = Cm(0.6)
    h(doc, 'No Caderno de Reencontros', 12, OURO, 6, 2); par(doc, cad)
    h(doc, 'Cultivo do Eixo', 12, OURO, 6, 2); par(doc, CULTIVO, 10)
    par(doc, 'Se algo mobilizar demais, pare, faça o Retorno ao Eixo e, se precisar, procure ajuda profissional.', 9, True, MUTED, 0)
    doc.save(os.path.join(OUT, f'TSH_M3_{cod.replace(".", "_")}_Apoio_do_aluno.docx'))
print('ok')
