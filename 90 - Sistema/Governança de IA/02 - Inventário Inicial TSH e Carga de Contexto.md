---
tipo: auditoria-inicial
status: em-andamento
capturado_em: 2026-09-07
baseline: 0efe9721b0954d5eb8a06a33f0575b4dcc41edee
escopo: Traduzindo o Ser Humano
---

# Inventário inicial do TSH e carga de contexto

## Escopo físico

Pasta auditada: `70 - Produções/Cursos/Curso - Nome Provisório/`.

| Medida | Valor |
|---|---:|
| Entradas | 286 |
| Arquivos | 250 |
| Diretórios | 36 |
| Tamanho lógico | 349.849.570 bytes |
| Markdown | 160 |
| PDF | 52 |
| DOCX | 28 |
| SVG | 4 |
| PNG | 4 |
| PPTX | 2 |

## Carga mínima de retomada atualmente prescrita

A seção “Ordem mínima de leitura” do `LEIA PRIMEIRO` exige seis documentos para qualquer retomada. No baseline, eles somam 73.783 bytes de texto Markdown, estimados em aproximadamente 18 mil tokens antes da solicitação real do usuário.

| Documento | Bytes |
|---|---:|
| LEIA PRIMEIRO | 27.787 |
| Diretriz de espiritualidade e não neutralização | 16.135 |
| Continuidade Leve | 8.746 |
| Nota-Ponte 7/14–9/54 | 6.242 |
| Matriz de Incorporação 9/54 | 11.685 |
| Estado e Continuidade da Produção M1 | 3.188 |

A estimativa em tokens é apenas indicativa; varia por modelo e tokenizador. O volume bruto, porém, demonstra que a retomada consome contexto substancial antes de a IA interpretar a tarefa corrente.

## Arquivos Markdown mais pesados no TSH

| Bytes | Arquivo |
|---:|---|
| 199.246 | Transcrição integral — Partes 1 a 5 — Aula 0.1 |
| 122.703 | Roteiro Integral Recuperado — Aula 0.1 |
| 107.548 | Montagem Literal Mais Recente — Partes 1 a 5 — Aula 0.1 |
| 82.047 | Dossiê de Contexto e Arquitetura Mestre |
| 63.478 | Roteiro Consolidado v1.0 — Aula 0.1 |
| 62.384 | Montagem Integrada Candidata v0.2 — Aula 0.1 |
| 61.735 | Guia de Condução da Masterclass v1.1 |
| 48.928 | Registro Mestre de Formulações Estruturantes |
| 42.600 | Guia Mestre de Incorporação e Rastreabilidade |
| 41.119 | Protocolo de Continuidade Integral |

Esses arquivos não devem ser eliminados. A correção proposta é impedir carregamento automático indiscriminado, usando índices leves e recuperação sob demanda.

## Duplicação binária confirmada

Foram encontrados dois grupos de arquivos com SHA idêntico:

1. Copy Canônica da Página e Checkout em `10 - Raio X do Produto/Consultoria` e `Mentoria/Arquivos Finais` — 4.606 bytes cada.
2. DOCX do Raio-X público em `Consultoria` e `Vigente` — 42.096 bytes cada.

A duplicação pode ser intencional por função de pasta. Nenhuma remoção será proposta sem mapear os links e consultar Fabiano.

## Diagnóstico funcional

O problema principal não é a quantidade total de conteúdo. É a ausência de separação suficiente entre:

- memória histórica;
- decisão vigente;
- estado operacional;
- instrução para a IA;
- material de consulta sob demanda;
- artefato de entrega.

A solução deverá reduzir o conjunto obrigatório de partida e preservar o acervo como fonte recuperável, sem transformar todo o vault em prompt permanente.

## Próxima etapa

Concluir a matriz de autoridade e conflitos. Somente após mediação autoral serão definidos o contrato comum de contexto e os adaptadores para ChatGPT/Codex e Claude.
