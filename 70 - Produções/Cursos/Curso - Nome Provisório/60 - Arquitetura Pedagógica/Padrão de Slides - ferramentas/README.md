# Padrão de Slides - ferramentas

Apoio técnico ao documento [[TSH - Padrão de Slides, Notas e Roteiros das Aulas]].

- `tsh_lib.py` — paleta, fontes e funções de layout (cartões, linhas, linha do EIXO, símbolo, fundos).
- `modelo_aula_M1.2.py` — exemplo completo de padronização de uma aula (capa, tipos de tela, encerramento).
- `anim.py` — transições de esmaecimento, entradas progressivas por clique e marcas [CLIQUE] nas notas.
- `assets/` — marca nuclear e símbolo com fundo transparente, extraídos do Manual v1.0. Substituir pelos PNG/SVG oficiais quando disponíveis.

Uso (Python 3 com python-pptx, lxml, numpy, Pillow), a partir desta pasta:

    python modelo_aula_M1.2.py entrada.pptx saida.pptx
    python anim.py saida.pptx final.pptx <modo>

Cada aula tem estrutura própria: copie o modelo e ajuste os tipos de tela conforme o padrão.
