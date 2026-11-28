"""Tela reutilizável «Onde estamos no mapa»: a coluna das camadas do Caminho da Semente
com a camada da aula em destaque. Use: from tela_camada import tela_camada; tela_camada(d, "2.4")."""
from base import *

# índice da camada no mapa (de cima para baixo) e texto do mapa, palavra por palavra
CAMADAS = {
 "2.4": (1, "Padrões automáticos", "Repetimos sem perceber porque aprendemos a sobreviver.",
         "O que mantém a repetição de uma resposta?"),
 "3.1": (2, "Feridas e traumas", "Experiências não elaboradas que ficam presas no corpo e na emoção.",
         "Estado corporal e acesso às respostas"),
 "4.4": (3, "Defesas e máscaras", "Estruturas que criamos para nos proteger, mas que nos afastam de quem somos.",
         "Padrões de proteção: história e necessidades atuais"),
 "3.2": (4, "Desconexão corpo-mente", "Vivemos no piloto automático, longe das sensações e emoções.",
         "Interocepção: perceber e interpretar sinais internos"),
 "3.4": (5, "Sobrecarga e caos", "O sistema nervoso sob pressão gera ansiedade, confusão e exaustão.",
         "Sistema nervoso autônomo: mobilização, sobrecarga e repouso"),
 "5.2": (6, "Condicionamentos", "Crenças, crenças limitantes e programações que reduzem nossa liberdade de escolha.",
         "Escolhas diante de necessidades e impulsos"),
}

def tela_camada(d, aula, img_dir="img"):
    n, nome, texto, titulo = CAMADAS[aula]
    s = d._new()
    d._chrome(s, "Onde estamos no mapa")
    h = 5.15; w = h * 459 / 902
    pic(s, f"{img_dir}/camada-{n}.png", 0.62, 1.7, h=h, back=False)
    x = 0.62 + w + 0.6
    d.text(s, x, 1.9, 12.7 - x, 0.4, "O CAMINHO DA SEMENTE · O QUE NOS AFASTA DO CENTRO", size=11, color=OURO, bold=True)
    d.text(s, x, 2.4, 12.7 - x, 0.9, nome, size=34, font=SERIF, color=NOT)
    d.text(s, x, 3.35, 12.7 - x, 1.2, f"“{texto}”", size=20, color=EST, italic=True, line=1.15)
    rect(s, x, 4.75, 12.7 - x, 1.25, fill=PET, rounded=0.06)
    d.text(s, x + 0.25, 4.8, 12.7 - x - 0.5, 1.15, f"Nesta aula: {titulo}", size=18, color="FFFFFF", anchor="ctr", line=1.12)
    d._footer(s)
    d.notes(s, "Onde estamos no mapa", "SITUAR · 20 A 30 SEGUNDOS",
            ["«Lembra do mapa O Caminho da Semente, da abertura do Módulo 2? Hoje estamos aqui.»",
             f"Ler a camada: «{nome}: {texto}»",
             "Uma frase sua ligando a camada à aula de hoje.",
             "As camadas também protegeram: reconhecê-las não é culpar a história.",
             "(Mapa de Fabiano Deliberalli, julho de 2026.)"],
            "Próximo: a aula.")
    return s

if __name__ == "__main__":
    d = Deck("Protótipo", "Onde estamos no mapa")
    for a in ["2.4", "3.1", "3.2", "3.4", "4.4", "5.2"]:
        tela_camada(d, a)
    os.makedirs("out_proto", exist_ok=True)
    d.save("out_proto/Prototipo-onde-estamos-no-mapa.pptx")
    print("ok", d.n)
