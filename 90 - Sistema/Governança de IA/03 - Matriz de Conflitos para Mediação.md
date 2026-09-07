---
tipo: matriz-de-conflitos
status: aguardando-mediacao
autoridade_final: Fabiano Deliberalli
baseline: 0efe9721b0954d5eb8a06a33f0575b4dcc41edee
atualizado_em: 2026-09-07
---

# Matriz de conflitos para mediação

Nenhum item abaixo será corrigido antes da decisão de Fabiano.

## C-001 — Ritual obrigatório de retomada

**Evidência A:** `01 - Protocolo de Continuidade Integral e Abertura de Novos Chats.md`, seção de abertura de novo chat, ainda determina “emitir Relatório de Retomada e aguardar deliberação autoral antes de modificar documentos”.

**Evidência B:** `Protocolo de Elaboração Curricular Viva e Continuidade Leve.md` declara prevalecer sobre regras anteriores de ritmo, relatórios, aprovações, portões e checklists; também determina iniciar sem novo Relatório de Retomada e sem pacotes de aprovação.

**Atenuante:** o protocolo antigo contém, no topo, aviso de que o protocolo leve prevalece operacionalmente. A contradição continua presente no corpo e pode induzir IAs a obedecerem à cláusula ultrapassada.

**Impacto:** respostas lentas, rituais desnecessários, solicitações repetidas de aprovação e consumo de contexto.

**Recomendação:** preservar o documento integral, mas marcar as cláusulas operacionais ultrapassadas como substituídas e encaminhar para um contrato operacional único e curto.

**Estado:** bloqueado, aguardando decisão.

## C-002 — Configuração de IA dentro do vault

**Evidência A:** o `README.md` afirma que “o vault não contém agentes, scripts ou configurações técnicas do Codex”.

**Evidência B:** para ChatGPT/Codex e Claude interpretarem automaticamente a mesma hierarquia, a solução convencional usa adaptadores mínimos no repositório, como `AGENTS.md` e `CLAUDE.md`, apontando para um contrato comum. Skills e validadores também são artefatos técnicos.

**Impacto:** sem adaptadores, o vault permanece conceitualmente limpo, mas depende de instrução manual a cada novo chat. Com adaptadores, a retomada é mais automática, porém altera uma regra arquitetônica explícita.

**Recomendação:** permitir apenas adaptadores mínimos e um validador claramente delimitado, mantendo conteúdo autoral em `90 - Sistema` e proibindo duplicação de regras nos adaptadores.

**Estado:** bloqueado, aguardando decisão.

## Formato da decisão

Para cada item, registrar:

- opção escolhida;
- justificativa autoral, se houver;
- data;
- alcance;
- documentos autorizados a mudar;
- restrições adicionais.
