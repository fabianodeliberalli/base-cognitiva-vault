---
tipo: matriz-de-conflitos
status: decisoes-validadas-e-integradas
autoridade_final: Fabiano Deliberalli
baseline: 0efe9721b0954d5eb8a06a33f0575b4dcc41edee
atualizado_em: 2026-09-07
---

# Matriz de conflitos para mediação

Os itens abaixo preservam a evidência dos conflitos apresentados a Fabiano. As decisões foram validadas e integradas; o registro permanece como memória do processo.

## C-001 — Ritual obrigatório de retomada

**Evidência A:** `01 - Protocolo de Continuidade Integral e Abertura de Novos Chats.md`, seção de abertura de novo chat, ainda determina “emitir Relatório de Retomada e aguardar deliberação autoral antes de modificar documentos”.

**Evidência B:** `Protocolo de Elaboração Curricular Viva e Continuidade Leve.md` declara prevalecer sobre regras anteriores de ritmo, relatórios, aprovações, portões e checklists; também determina iniciar sem novo Relatório de Retomada e sem pacotes de aprovação.

**Atenuante:** o protocolo antigo contém, no topo, aviso de que o protocolo leve prevalece operacionalmente. A contradição continua presente no corpo e pode induzir IAs a obedecerem à cláusula ultrapassada.

**Impacto:** respostas lentas, rituais desnecessários, solicitações repetidas de aprovação e consumo de contexto.

**Recomendação:** preservar o documento integral, mas marcar as cláusulas operacionais ultrapassadas como substituídas e encaminhar para um contrato operacional único e curto.

**Estado:** validado por Fabiano — marcar e redirecionar.

## C-002 — Configuração de IA dentro do vault

**Evidência A:** o `README.md` afirma que “o vault não contém agentes, scripts ou configurações técnicas do Codex”.

**Evidência B:** para ChatGPT/Codex e Claude interpretarem automaticamente a mesma hierarquia, a solução convencional usa adaptadores mínimos no repositório, como `AGENTS.md` e `CLAUDE.md`, apontando para um contrato comum. Skills e validadores também são artefatos técnicos.

**Impacto:** sem adaptadores, o vault permanece conceitualmente limpo, mas depende de instrução manual a cada novo chat. Com adaptadores, a retomada é mais automática, porém altera uma regra arquitetônica explícita.

**Recomendação:** permitir apenas adaptadores mínimos e um validador claramente delimitado, mantendo conteúdo autoral em `90 - Sistema` e proibindo duplicação de regras nos adaptadores.

**Estado:** validado por Fabiano — permitir somente adaptadores mínimos.

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

## C-003 — Estatuto da arquitetura inicial e da arquitetura vigente

**Decisão de Fabiano:** a arquitetura vigente é de **9 módulos e 54 aulas**. A organização inicial de **7 módulos e 14 aulas** não permanece como estrutura ativa. Seus arquivos serão preservados como acervo de títulos e conteúdos para consulta.

As 54 aulas constituem o formato vigente e ainda serão estruturadas para posterior gravação. Conteúdos da organização inicial poderão ser incorporados conforme necessidade e pertinência, sem correspondência obrigatória e sem conservar sua numeração antiga.

A antiga duração de 12 semanas também não governa a arquitetura atual.

**Estado:** validado por Fabiano.

## C-004 — Divergência histórica entre as antigas aulas 2.1 e 2.2

**Evidência:** o `LEIA PRIMEIRO` colocava a aula energética em 2.1; a `Reconciliação Documental dos Fundamentos Transversais e Revisão Curricular` colocava corpo, ritmo e afastamento em 2.1 e a aula energética em 2.2.

**Decisão de Fabiano:** não escolher uma dessas numerações como estrutura vigente. As duas versões pertencem à organização inicial e serão preservadas como registros históricos. Seus conteúdos serão avaliados individualmente quando forem pertinentes à estruturação das 54 aulas atuais.

**Estado:** encerrado como divergência histórica; não é conflito da arquitetura vigente.

## C-005 — Subtítulo-base da oferta

**Versão histórica:** `Da compreensão acumulada à mudança vivida`.

**Decisão de Fabiano:** o subtítulo-base vigente é `Da compreensão acumulada à presença que sustenta`.

A versão anterior permanece preservada como formulação histórica e poderá ser consultada como matéria-prima de comunicação, sem funcionar como subtítulo-base.

**Estado:** validado por Fabiano.
