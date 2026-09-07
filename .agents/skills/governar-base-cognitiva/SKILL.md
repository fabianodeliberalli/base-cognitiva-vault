---
name: governar-base-cognitiva
description: Auditar e alterar com segurança governança de IA, protocolos de continuidade, fichas de contexto e hierarquia documental no vault Base Cognitiva. Usar para reformas de governança e contexto; não usar para redação comum de conteúdo.
---

# Governar a Base Cognitiva

Produza mudanças mínimas, reversíveis e verificáveis, preservando a autoridade autoral de Fabiano.

## Preparação

1. Leia `90 - Sistema/Governança de IA/10 - Contrato Comum de Contexto para Assistentes de IA.md`.
2. Leia somente a ficha mínima do projeto afetado.
3. Confirme repositório, branch, commit-base e escopo antes de escrever.
4. Inventarie os arquivos diretamente afetados e suas referências; não carregue o vault inteiro.

## Porta de conflito

Se duas fontes produzirem decisões diferentes sobre conteúdo, significado, prioridade, identidade, promessa, arquitetura, versão vigente ou preservação:

- não altere o item;
- apresente a Fabiano as evidências, o impacto, uma recomendação e duas ou três alternativas;
- aguarde a decisão e registre-a na matriz de conflitos.

Questões técnicas reversíveis podem avançar em branch isolada com registro.

## Implementação

- Prefira uma fonte normativa comum e adaptadores que apenas apontem para ela.
- Preserve documentos históricos; marque precedência ou estado em vez de apagar.
- Não mova nem renomeie antes de verificar referências.
- Não integre à `main` sem homologação explícita de Fabiano.
- Registre apenas mudanças duráveis, decisões e pendências.

## Validação

Execute `python3 .agents/skills/governar-base-cognitiva/scripts/validate_governance.py` na raiz do repositório.

Falhas bloqueantes devem ser corrigidas antes do diff final. Avisos exigem revisão humana, mas não autorizam mudanças de conteúdo.
