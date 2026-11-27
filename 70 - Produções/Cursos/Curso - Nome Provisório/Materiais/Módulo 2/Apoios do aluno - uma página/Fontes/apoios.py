import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'Percurso - Cultivo do Eixo e Caderno de Reencontros', 'Fontes'))
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from caderno import base, h, par, NOT, OURO, MUTED

MAPA = 'Mapa do percurso: Traduzir → Ganhar eixo e presença → Ocupar o próprio espaço · Você está em: Traduzir (a prática)'
CULTIVO = 'Cultivo do Eixo desta quinzena (todos os dias, 3 a 5 minutos): árvore; a pergunta «o que está me vivendo agora?»; três respirações no baixo ventre. No momento real, o Retorno ao Eixo: notar o primeiro sinal, sentir os pés, três respirações, «o que está ao meu alcance agora?».'

AULAS = [
 ("2.1", "Como se forma o que você percebe?",
  "Perceber não é copiar o mundo: atenção, estado do corpo, aprendizagem e contexto participam do que você percebe.",
  "«Essa Essência vai ficando soterrada por camadas de vivências, como suas emoções, crenças, imagens, memórias e corpos.» — Fabiano, workshop Essência",
  ["Escolha uma situação recente que ainda mexe com você.", "Volte a ela por um minuto, com os pés no chão.", "Pergunte: desde então, o que mudou — o acontecimento, a minha atenção ou a minha leitura?", "Anote uma palavra para cada."],
  "No campo «o primeiro sinal», note o que você percebeu primeiro na situação: no corpo, na emoção ou no pensamento."),
 ("2.2", "Por que alguns sinais ganham mais importância?",
  "Notar, destacar, identificar o que se sente e comunicar são passos diferentes. O Eu Básico sente e mostra; o Eu Médio nomeia e escolhe.",
  "«Seu problema não é sentir demais, mas não ser traduzida.» — Fabiano, Arquitetura Invisível. O Eu Básico «chora, mas não sabe falar».",
  ["Volte a uma situação recente.", "Pergunte primeiro: «o que eu sinto no corpo?» e anote.", "Depois pergunte: «o que isso quer de mim?» e anote.", "Compare: cada pergunta trouxe para a frente algo diferente."],
  "Escreva o que ganhou mais importância na situação e o que ficou em segundo plano."),
 ("2.3", "Interpretações e certezas: recuperar outras pistas",
  "Uma interpretação pode parecer a própria realidade. Voltar ao corpo e ao ambiente devolve as pistas que a certeza tinha apagado.",
  "«O problema muitas vezes não vem da experiência em si, mas da interpretação que fazemos dela.» — Fabiano",
  ["Escreva uma certeza que você teve numa situação (por exemplo: «ele não se importa»).", "Pés no chão, três respirações, olhe ao redor.", "Pergunte: que outras pistas existiam?", "Formule uma pergunta que poderia trazer informação nova."],
  "No campo «uma frase de Tradução», escreva a certeza e uma leitura alternativa possível."),
 ("2.4", "O que mantém a repetição de uma resposta?",
  "Respostas familiares voltam mesmo quando já as entendemos: somos «vividos» por padrões que funcionam como transes que não escolhemos. O primeiro sinal é a porta para voltar.",
  "«Somos ‘vividos’ e não vivemos!» — Fabiano, workshop Essência. «A Essência é o destino. O EIXO é o caminho.»",
  ["Lembre uma situação em que a resposta de sempre apareceu.", "Encontre o primeiro sinal: no corpo, na emoção ou no pensamento.", "Faça o Retorno ao Eixo: pés, três respirações no baixo ventre, «o que está ao meu alcance agora?».", "Imagine o que poderia acontecer depois disso."],
  "Escreva o seu plano: «Quando eu perceber ________, vou fazer o Retorno ao Eixo.»"),
 ("2.5", "Acontecimento, experiência e interpretação",
  "O que aconteceu, o que foi vivido e o que foi interpretado são coisas diferentes, também diante de experiências espirituais ou incomuns. Acolher não é confirmar.",
  "A vivência espiritual «deve ser ‘agregadora’, de sentido e significados que sejam incorporados na vida do indivíduo que a experiencia». — Fabiano, monografia em Psicologia Transpessoal",
  ["Escolha uma experiência marcante; pode ser espiritual ou incomum.", "Escreva separadamente: o que aconteceu, o que você viveu, o que você concluiu.", "Marque o que é certeza e o que é hipótese.", "Pergunte: que efeito essa experiência teve na minha vida?"],
  "Nos campos «o que aconteceu» e «uma frase de Tradução», mantenha separados o fato e a leitura."),
 ("2.6", "Como construir e revisar uma Tradução provisória",
  "Uma Tradução é provisória: com dados novos, expressão e diálogo, ela se revê. Traduzir é o primeiro movimento do percurso.",
  "«Precisamos primeiro traduzir o que temos em nossos padrões e depois trabalhar para ganhar eixo e presença suficientes para ocupar nosso real espaço.» — Fabiano",
  ["Retome a Cartografia ou a página do caderno de uma situação.", "O que você sabe hoje que não sabia antes?", "O que mudaria a sua leitura?", "Escolha um próximo gesto pequeno e possível."],
  "Preencha o «Reencontro da quinzena» do Módulo 2 antes do encontro de 12/12 e traga o caderno."),
]

for cod, tit, ideia, raiz, passos, cad in AULAS:
    doc = Document(); base(doc)
    par(doc, 'Traduzindo o Ser Humano · Módulo 2 · Apoio do aluno', 9, False, OURO, 2)
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
    doc.save(f'TSH_M2_{cod.replace(".", "_")}_Apoio_do_aluno.docx')
print('ok')
