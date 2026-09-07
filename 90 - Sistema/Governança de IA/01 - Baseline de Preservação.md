---
tipo: baseline-preservacao
status: congelado
capturado_em: 2026-09-07
repositorio: fabianodeliberalli/base-cognitiva-vault
branch_origem: main
commit_origem: 0efe9721b0954d5eb8a06a33f0575b4dcc41edee
arvore_truncada: false
---

# Baseline de preservação

## Ponto de restauração

- Commit: `0efe9721b0954d5eb8a06a33f0575b4dcc41edee`
- Mensagem: `Arquiva versões finais do lançamento TSH e registro de continuidade`
- Data do commit: 2026-08-25T01:36:23Z
- Branch de trabalho: `refactor/governanca-contexto-ia-2026-09`

## Inventário global da árvore Git

| Medida | Valor |
|---|---:|
| Entradas rastreadas | 641 |
| Arquivos (blobs) | 561 |
| Diretórios (trees) | 80 |
| Tamanho lógico dos arquivos | 444.104.826 bytes |
| Resposta de árvore truncada | não |

## Tipos de arquivo mais frequentes

| Extensão | Quantidade |
|---|---:|
| Markdown | 340 |
| PDF | 65 |
| PNG | 60 |
| JPEG | 45 |
| DOCX | 33 |
| SVG | 13 |
| PPTX | 3 |

## Distribuição por área principal

| Área | Entradas |
|---|---:|
| 70 - Produções | 357 |
| Imported | 89 |
| 00 - Caixa de Entrada | 67 |
| 80 - Mapas Conceituais | 44 |
| 90 - Anexos | 19 |
| 20 - Notas Conceituais | 11 |
| 90 - Sistema | 11 |
| 60 - Sessões | 10 |
| 80 - Fontes Bibliográficas | 10 |

## Garantia operacional

Este baseline é a referência quantitativa e de restauração da reforma. Antes de qualquer proposta de integração à `main`, a auditoria deverá:

1. comparar a árvore final com este commit;
2. justificar todo arquivo adicionado, alterado, movido ou removido;
3. comprovar que movimentos preservaram conteúdo e referências;
4. listar perdas aparentes como falha bloqueante;
5. permitir restauração integral a partir do commit de origem.

A listagem Git completa permanece registrada no próprio objeto de árvore do commit-base. O SHA de cada arquivo é recuperável pela API Git e será usado na regressão final.
