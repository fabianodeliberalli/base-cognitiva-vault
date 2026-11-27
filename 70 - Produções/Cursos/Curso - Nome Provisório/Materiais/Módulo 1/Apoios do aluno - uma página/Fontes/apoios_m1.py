import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm
from caderno import base, h, par, NOT, OURO, MUTED
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apoios_m1')
MAPA = 'Mapa do percurso: Traduzir → Ganhar eixo e presença → Ocupar o próprio espaço · Você está em: Traduzir (os fundamentos)'
CULTIVO = 'Cultivo do Eixo (todos os dias, 3 a 5 minutos): a árvore; a pergunta «o que está me vivendo agora?»; três respirações no baixo ventre. O vídeo está no Módulo 0, «Comece pelo corpo». Se tiver pouco tempo: o vídeo «Módulo 1 em prática guiada» e o Cultivo do Eixo bastam para seguir.'
AULAS = [
 ("1.1", "Por que entender um padrão não impede que ele se repita",
  "Entender um padrão e conseguir agir de outro modo são coisas diferentes. A compreensão é o começo; o curso trabalha a passagem dela para a vida.",
  "«Ou trabalhamos voluntariamente ou somos vividos pelos padrões que carregamos.» — Fabiano, anotação de 17/07/2021",
  ["Escolha uma situação em que você entende o padrão e ainda assim repete.", "Só escolha; não precisa explicar.", "Sinta os pés e faça três respirações no baixo ventre.", "Pergunte: o que acontece no corpo quando eu penso nessa situação?"],
  "Se quiser, anote a situação em uma linha. Ela pode acompanhar você pelo curso."),
 ("1.2", "Saber, acessar e sustentar não são a mesma coisa",
  "Saber o que fazer, conseguir acessar isso na hora e conseguir sustentar são três capacidades diferentes. Perder o acesso não é perder o que você sabe.",
  "«Encontrar esse eixo — ou reencontrá-lo — não significa alcançar um estado especial, elevado ou definitivo.» — Fabiano, Arquitetura Invisível",
  ["Volte à situação da aula 1.1.", "Pergunte: eu sei o que fazer?", "Consigo acessar isso no momento em que acontece?", "Consigo sustentar? Note onde está a dificuldade."],
  "Se quiser, marque onde está a dificuldade: saber, acessar ou sustentar."),
 ("1.3", "O que é competência incorporada e o que ela não promete",
  "O que se aprende no corpo fica disponível de outro jeito. Uma prática repetida muda o que você percebe e o que consegue fazer, sem prometer um estado permanente.",
  "«Muitas vezes há apenas um registro subcortical da experiência, não relacionado com cognição.» — Fabiano",
  ["Um sorriso leve nos olhos e nos lábios.", "Leve esse sorriso ao coração e ao baixo ventre.", "Três respirações no baixo ventre.", "Note o que mudou, mesmo que pouco."],
  "Se quiser, anote o que mudou depois do Sorriso Interior."),
 ("1.4", "A experiência é o território, as explicações são mapas",
  "A experiência vem primeiro; as explicações são mapas para olhar para ela. Mapas diferentes permitem perguntas diferentes, e nenhum é a pessoa.",
  "«Ninguém tem a verdade absoluta, portanto todos temos o direito de apresentar algo sobre nossa cota de reflexão e vivências relevantes.» — Fabiano, workshop Essência",
  ["Volte à sua situação.", "Primeiro, só o que você sente: no corpo, na emoção.", "Depois, a explicação que você costuma dar.", "Pergunte: que outra explicação também caberia?"],
  "Se quiser, anote o que você sente e, à parte, a explicação."),
 ("1.5", "As Cinco Janelas, ampliar a leitura do que acontece",
  "Corpo, emoção, mente, relações e espiritualidade são janelas para a mesma experiência. Olhar por mais de uma amplia a leitura sem perder o centro.",
  "«Ampliar o mundo sem perder o centro.» — Fabiano",
  ["Volte à sua situação.", "Passe pelas cinco janelas: corpo, emoção, mente, relações, espiritualidade.", "Uma palavra para cada, em silêncio.", "Qual janela mostrou algo novo?"],
  "Se quiser, anote a janela que mostrou algo novo."),
 ("1.6", "Primeira Cartografia",
  "A Cartografia é um primeiro registro das camadas de uma situação. Seu valor não está em preencher campos, e sim no que ela ajuda a descobrir.",
  "«Sentir amplia a compreensão. Compreender refina o sentir.» — Fabiano",
  ["Da janela que mostrou algo novo, escolha um detalhe.", "Dê a ele uma forma: uma palavra, um desenho, um gesto.", "Volte ao vivido: a forma combina com o que você sente?", "Ajuste, se precisar."],
  "Se quiser, guarde a forma no Caderno: é a sua primeira Cartografia."),
 ("1.7", "Perder o eixo não significa perder o percurso",
  "Oscilar faz parte. O pêndulo vai e volta; a espiral retorna aos mesmos temas em outro lugar. Perder o acesso por um tempo não apaga o caminho feito.",
  "«O eixo é a capacidade de permanecer conectado consigo mesmo, mesmo em meio ao caos.» — Fabiano, O Caminho da Semente",
  ["Lembre uma vez em que você perdeu o eixo e voltou.", "O que ajudou a voltar?", "Sinta os pés e faça três respirações no baixo ventre.", "Diga para si: perder o eixo não significa perder o percurso."],
  "Se quiser, anote o que ajudou você a voltar. É um recurso seu."),
]
for cod, tit, ideia, raiz, passos, cad in AULAS:
    doc = Document(); base(doc)
    par(doc, 'Traduzindo o Ser Humano · Módulo 1 · Apoio do aluno', 9, False, OURO, 2)
    h(doc, f'Aula {cod} — {tit}', 18, NOT, 0, 4)
    par(doc, MAPA, 8.5, True, MUTED, 10)
    h(doc, 'A ideia', 12, OURO, 4, 2); par(doc, ideia)
    h(doc, 'Raiz', 12, OURO, 6, 2); par(doc, raiz, 11, True)
    h(doc, 'Prática (faça junto com o vídeo)', 12, OURO, 6, 2)
    for i, t in enumerate(passos, 1):
        q = par(doc, f'{i}. {t}'); q.paragraph_format.left_indent = Cm(0.6)
    h(doc, 'No Caderno de Reencontros, se quiser', 12, OURO, 6, 2); par(doc, cad)
    h(doc, 'Cultivo do Eixo', 12, OURO, 6, 2); par(doc, CULTIVO, 10)
    par(doc, 'Se algo mobilizar demais, pare, faça o Retorno ao Eixo e, se precisar, procure ajuda profissional.', 9, True, MUTED, 0)
    doc.save(os.path.join(OUT, f'TSH_M1_{cod.replace(".", "_")}_Apoio_do_aluno.docx'))
print('ok')
