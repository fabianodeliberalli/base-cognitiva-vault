---
tipo: matriz-de-conflitos
status: mediado-em-implementacao
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


# Decisões de mediação — 2026-09-07

## C-001 — decisão

**Opção adotada:** marcar e redirecionar.

**Justificativa operacional:** preserva o protocolo histórico e sua memória substantiva, elimina a instrução contraditória no ponto de execução e concentra o ritual vigente no protocolo leve e no contrato comum. Auditorias passam a ocorrer em marcos de consolidação, não como barreira a cada conversa.

**Alcance autorizado:** ajustar marcação e redação operacional do protocolo antigo sem apagar seu conteúdo autoral.

## C-002 — decisão

**Opção adotada:** permitir adaptadores mínimos.

**Justificativa operacional:** possibilita que Codex e Claude encontrem automaticamente a mesma governança, enquanto uma fonte comum impede divergência entre instruções. O README passa a permitir somente adaptadores mínimos e exige justificativa e homologação para qualquer skill ou script adicional.

**Alcance autorizado:** criar `AGENTS.md`, `CLAUDE.md`, contrato comum e fichas mínimas de projeto; alterar a regra correspondente do README.

**Restrição:** adaptadores não devem reproduzir protocolos, decisões autorais ou contexto extenso.


# Segundo pacote de mediação — decisões recuperadas dos chats

## C-003 — 7/14 substituído ou coexistente com 9/54

**Evidência A:** o repositório no baseline, atualizado em 22–23/08/2026, afirma que 7 módulos/14 unidades governam desenvolvimento, integração e rastreabilidade, enquanto 9 módulos/54 aulas governam entrega e comunicação; nenhuma estrutura substitui automaticamente a outra.

**Evidência B:** o arquivo externo `relatorio-auditoria-vault-para-execucao.md`, recuperado do contexto dos chats, descreve 7/14/12 semanas como superado pelo Raio-X vigente. Outro registro de comunicação exige nota-ponte e reconhece 7/14 como arquitetura profunda até reconciliação formal.

**Impacto:** declarar substituição pode apagar a rastreabilidade de conteúdo; declarar coexistência sem confirmação pode perpetuar uma estrutura interna que Fabiano pretendia abandonar.

**Recomendação:** confirmar a coexistência funcional já documentada no repositório, tratando “12 semanas” separadamente e não como parte necessária de 7/14.

**Estado:** bloqueado, aguardando decisão.

## C-004 — definição das Unidades 2.1 e 2.2

**Evidência disponível:** relatório externo registra “reconciliação de numeração” e determina levar a Fabiano qual definição de 2.1/2.2 prevalece. Os trechos recuperados não contêm os títulos, as duas versões nem as alternativas concretas.

**Impacto:** qualquer correção agora seria inferência e poderia trocar conteúdos de lugar.

**Recomendação:** manter bloqueado e recuperar os documentos/fontes completos antes de apresentar alternativas substantivas.

**Estado:** bloqueado por evidência insuficiente e aguardando orientação de Fabiano.

## C-005 — subtítulo-base da oferta

**Evidência A:** o repositório no baseline fixa `Da compreensão acumulada à mudança vivida` como subtítulo-base, com headlines variáveis.

**Evidência B:** decisão registrada em chat de 06/09/2026 deixou o nome como `Traduzindo o Ser Humano — Da compreensão acumulada à presença que sustenta`. Na mesma revisão, Fabiano aprovou o resultado `Perceber o automático mais cedo, recuperar clareza e responder com mais coerência`.

**Impacto:** manter duas formulações como subtítulo-base gera inconsistência entre curso, briefing, formulário e peças de comunicação.

**Recomendação:** adotar `Da compreensão acumulada à presença que sustenta` como subtítulo-base atual, preservando `mudança vivida` como formulação histórica ou headline quando adequada.

**Estado:** bloqueado, aguardando decisão.
