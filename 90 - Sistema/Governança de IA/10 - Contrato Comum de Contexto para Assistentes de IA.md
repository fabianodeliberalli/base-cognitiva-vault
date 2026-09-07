---
tipo: contrato-comum-de-contexto
status: proposta-implementada-na-branch
autoridade_final: Fabiano Deliberalli
versao: "0.1"
atualizado_em: 2026-09-07
---

# Contrato comum de contexto para assistentes de IA

## Finalidade

Este é o núcleo único de orientação para ChatGPT/Codex, Claude e outros assistentes que trabalhem com este vault. Adaptadores específicos de ferramenta devem apontar para este documento e não repetir sua governança.

## Ordem de autoridade

Em caso de divergência, aplicar esta ordem:

1. instrução explícita mais recente de Fabiano na tarefa atual;
2. decisão de mediação registrada e homologada por Fabiano;
3. estado ativo mais recente do projeto, dentro do próprio escopo;
4. este contrato comum;
5. protocolos e documentos vigentes específicos do projeto;
6. referências, propostas, rascunhos e patrimônio histórico.

Atualidade não substitui autoridade autoral. Um registro recente de execução não pode reescrever, sozinho, uma decisão de identidade ou arquitetura.

## Princípio de contexto mínimo suficiente

Não carregar o vault inteiro nem uma cadeia fixa de documentos extensos.

1. Identificar projeto, tipo de tarefa e entrega pedida.
2. Ler a ficha de contexto mínimo do projeto.
3. Consultar somente as fontes indicadas para aquela pergunta.
4. Expandir a busca quando houver lacuna, contradição, alegação de inexistência ou risco de produzir algo já existente.
5. Distinguir evidência consultada de inferência da IA.
6. Registrar somente decisões duráveis, mudanças de estado ou artefatos que Fabiano queira preservar.

## Mediação de conflitos

Fabiano é o decisor final. Ao encontrar conflito que possa mudar conteúdo, sentido, prioridade, identidade, promessa, arquitetura, versão vigente ou provocar perda:

- interromper a alteração do item;
- apresentar as duas evidências com caminhos;
- explicar o efeito prático;
- recomendar uma opção;
- oferecer duas ou três alternativas;
- aguardar a decisão.

Questões técnicas reversíveis podem prosseguir em branch isolada, com registro no relatório de mudanças.

## Preservação e Git

- Trabalhar em branch específica.
- Não integrar à `main` sem homologação de Fabiano.
- Não excluir, mover ou renomear antes de mapear referências.
- Não alterar materiais brutos.
- Preferir índice, metadado, ponte ou adaptador a reescrever conteúdo autoral.
- Manter estados explícitos: `ativo`, `histórico`, `referência`, `rascunho`, `substituído`.
- Toda mudança deve ser rastreável e reversível por commit.

## Resposta e contribuição

- Começar pela demanda atual, não por um ritual de retomada.
- Não emitir Relatório de Retomada nem pacote de aprovação por padrão.
- Não reabrir decisões consolidadas sem contradição documentada.
- Declarar incerteza quando a fonte não bastar.
- Separar recomendação da decisão de Fabiano.
- Evitar criar novos protocolos quando uma regra existente puder ser simplificada.
- Evitar gravar a mesma regra em mais de um lugar.

## Encerramento

Ao concluir uma unidade significativa de trabalho, registrar apenas:

- o que mudou;
- decisões autorais novas;
- pendências e conflitos;
- fontes afetadas;
- próximo ponto de ação.

Conversas exploratórias sem mudança durável não exigem registro.
