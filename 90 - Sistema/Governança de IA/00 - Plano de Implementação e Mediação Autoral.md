---
tipo: governanca-ia
status: ativo-na-branch
autoridade_final: Fabiano Deliberalli
criado_em: 2026-09-07
baseline_main: 0efe9721b0954d5eb8a06a33f0575b4dcc41edee
branch: refactor/governanca-contexto-ia-2026-09
---

# Plano de implementação e mediação autoral

## Objetivo

Reduzir sobrecarga, redundância e contradições nas instruções usadas por ChatGPT/Codex e Claude, preservando integralmente o conteúdo do vault e melhorando a contribuição ao projeto **Traduzindo o Ser Humano (TSH)** e aos demais trabalhos apoiados por GitHub e Obsidian.

Este documento governa somente a branch de reforma até homologação expressa de Fabiano. Nada desta branch será integrado à `main` sem sua aprovação.

## Autoridade

Fabiano Deliberalli é:

- a autoridade autoral do conteúdo;
- o mediador de conflitos materiais;
- o decisor final sobre significado, prioridade, identidade, promessa, arquitetura pedagógica e versão vigente;
- a única autoridade para homologar a integração à `main`.

Nenhum assistente, agente, protocolo antigo ou arquivo técnico pode substituir essa decisão.

## Critério de excelência

Toda mudança deverá demonstrar melhora verificável em pelo menos um dos seguintes pontos, sem piorar os demais:

1. menor carga de contexto inicial;
2. menor duplicação ou sobreposição de comandos;
3. hierarquia de autoridade mais clara;
4. maior fidelidade às decisões autorais;
5. recuperação mais rápida da versão vigente;
6. compatibilidade previsível entre ChatGPT/Codex, Claude, GitHub e Obsidian;
7. preservação e rastreabilidade do conteúdo histórico;
8. menor probabilidade de retrabalho.

## Classificação de conflitos

### Conflito material — interromper e consultar Fabiano

Existe quando a decisão pode alterar:

- identidade, voz, espiritualidade, promessa ou posicionamento;
- arquitetura pedagógica, comercial ou conceitual;
- significado de EIXO, relação 7/14–9/54 ou outro fundamento;
- qual documento ou decisão representa a versão vigente;
- escopo ou autoridade de protocolos;
- conteúdo de forma irreversível ou com risco de perda;
- regras divergentes que produzam respostas substancialmente diferentes.

O item fica bloqueado. Nenhuma das alternativas será aplicada antes da decisão.

### Questão técnica reversível — prosseguir e registrar

Inclui inventário, checagem de links, medição de tamanho, normalização segura de metadados, criação de relatórios, validações e edições isoladas na branch que não alterem conteúdo autoral. Essas ações serão documentadas no relatório de mudanças.

## Pacote obrigatório para mediação

Cada consulta a Fabiano deverá conter:

1. questão em linguagem direta;
2. evidência A e evidência B, com caminhos e datas quando disponíveis;
3. consequência prática de cada interpretação;
4. recomendação fundamentada;
5. duas ou três alternativas mutuamente exclusivas;
6. indicação explícita de que o item permanece sem alteração até a decisão.

## Regras de preservação

- Não excluir conteúdo nesta fase.
- Não mover ou renomear arquivos antes de mapear referências e links.
- Não sobrescrever arquivos autorais quando uma camada de índice, metadado ou adaptador resolver o problema.
- Diferenciar `ativo`, `histórico`, `referência`, `rascunho` e `substituído` sem apagar o original.
- Toda alteração deve ser reversível por commit.
- Alterações estruturais deverão passar por comparação antes/depois e teste de links.
- A integração à `main` depende de diff legível, testes e homologação de Fabiano.

## Fluxo de implementação

| Fase | Entrega | Porta de saída |
|---|---|---|
| 0 | Baseline e branch isolada | commit-base verificado |
| 1 | Inventário de documentos, decisões e instruções | cobertura e classificação verificadas |
| 2 | Matriz de conflitos e precedência | conflitos materiais decididos por Fabiano |
| 3 | Arquitetura comum de contexto | proposta homologada |
| 4 | Camada ativa do TSH | links e conteúdo preservados |
| 5 | Adaptadores mínimos para as IAs | ausência de duplicação normativa |
| 6 | Skills estritamente justificadas | testes e manutenção documentados |
| 7 | Regressão e auditoria final | aprovação expressa antes da `main` |

## Estado inicial

- Fase 0: concluída.
- Fase 1: em andamento.
- Exclusões, movimentos e renomeações: bloqueados.
- Conflitos materiais conhecidos: serão registrados em matriz própria e submetidos a Fabiano antes de correção.
