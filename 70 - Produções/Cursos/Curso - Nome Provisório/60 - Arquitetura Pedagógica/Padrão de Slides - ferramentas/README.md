# Padrão de Slides - ferramentas

Apoio técnico ao documento [[TSH - Padrão de Slides, Notas e Roteiros das Aulas]].

- `tsh_lib.py` — paleta, fontes e funções de layout (cartões, linhas, linha do EIXO, símbolo, fundos).
- `modelo_aula_M1.2.py` — exemplo completo de padronização de uma aula (capa, tipos de tela, encerramento).
- `anim.py` — transições de esmaecimento e entradas progressivas por clique, preservando as notas de fala. O mapa de cliques e as instruções de operação pertencem ao caderno de preparação.
- `assets/` — marca nuclear e símbolo com fundo transparente, extraídos do Manual v1.0. Substituir pelos PNG/SVG oficiais quando disponíveis.

Uso (Python 3 com python-pptx, lxml, numpy, Pillow), a partir desta pasta:

    python modelo_aula_M1.2.py entrada.pptx saida.pptx
    python anim.py saida.pptx final.pptx <modo>

Cada aula tem estrutura própria: copie o modelo e ajuste os tipos de tela conforme o padrão.

## Uniformidade da produção a partir de 22 de novembro de 2026

Aplicar a versão vigente de [[TSH - Padrão de Slides, Notas e Roteiros das Aulas]]: paleta oficial, EB Garamond nos títulos e Inter em todo texto didático, pergunta, instrução, rótulo e rodapé. As notas da apresentação e o roteiro de gravação contêm somente fala natural, em blocos curtos; fontes, condução, tempos e mapa de cliques ficam na preparação.

O exemplo M1.2 demonstra uma composição histórica de aula. A aplicação recuperável de [[M2.1 - Conteúdo das telas e notas v0.3.json]] registra a produção atual padronizada. Adaptar a função dos layouts ao conteúdo e conferir a área de câmera, o ativo original da marca e as fontes reais no arquivo final. Os valores e posições do exemplo não são um protocolo numérico obrigatório para todas as aulas.

Os scripts não são autorização para substituir arquivos de aulas já gravadas nem para reintroduzir rubricas na locução. Uma cópia de trabalho deve preservar a fonte original.
