---
tipo: aprendizado-operacional
status: memoria-evolutiva-sob-demanda
atualizado_em: 2026-09-07
escopo: ChatGPT-Codex-Claude-Obsidian-GitHub
---

# Aprendizado operacional e melhoria contínua

## Função

Preservar aprendizados comprovados sobre a forma de trabalhar, sem transformar cada conversa em regra e sem entrar na carga inicial dos assistentes.

Consultar esta nota somente quando:

- Fabiano pedir melhoria do fluxo;
- o mesmo atrito reaparecer;
- houver troca de assistente ou mudança estrutural no repositório;
- uma auditoria revelar retrabalho, perda, duplicação ou dificuldade recorrente de localização.

Não consultar por padrão em tarefas comuns de criação.

## O que merece registro

Um aprendizado operacional deve ter pelo menos uma destas bases:

- correção explícita de Fabiano;
- problema repetido em mais de uma interação;
- evidência técnica verificável;
- mudança testada que reduza carga, ambiguidade, perda ou retrabalho.

Ideias isoladas, explorações criativas e preferências momentâneas não viram regra.

## Destino do aprendizado

- aprendizado específico de um projeto: atualizar apenas sua ficha mínima;
- aprendizado comum a vários assistentes: atualizar o guia comum;
- evidência, diagnóstico e resultado de teste: registrar nesta nota;
- conteúdo autoral: manter no próprio projeto, nunca converter em regra técnica.

Aplicar a menor mudança capaz de resolver o problema. Se não produzir melhora observável, revisar ou retirar.

## Aprendizados longitudinais já confirmados

| Atrito observado | Aprendizado | Ajuste realizado | Evidência de melhora |
|---|---|---|---|
| retomadas exigiam relatório e aprovação antes de qualquer contribuição | começar pela demanda atual e pausar apenas diante de conflito real | ritual de retomada desativado; mediação proporcional | redução de interrupções e aprovações desnecessárias |
| duas estruturas do curso passaram a disputar autoridade | distinguir arquitetura atual de patrimônio consultável | 9 módulos e 54 aulas como referência atual; 7 módulos e 14 aulas preservados como fonte | instruções de entrada reconciliadas sem apagar títulos ou conteúdos |
| estados como “canônico”, “final” e “congelado” bloquearam criação e foram frequentemente produzidos pelas próprias IAs | estados documentais são fotografias revisáveis, não limites à autoria | guia e skill impedem que a IA crie rigidez e permitem revisão por Fabiano | testes de comportamento passaram |
| muitos documentos eram carregados antes de responder | usar contexto mínimo e recuperação progressiva | guia comum, ficha do projeto e adaptadores curtos | carga inicial reduzida em aproximadamente 84% |
| instruções diferentes entre ChatGPT e Claude criavam sobreposição | manter uma orientação compartilhada e adaptadores mínimos | arquivos de entrada apontam para a mesma fonte | ausência de duplicação extensa nos adaptadores |
| respostas do formulário de tráfego pago poderiam se perder nos chats | arquivar fontes recuperadas com estatuto claro e uso contextual | respostas preservadas no projeto como fonte qualificada | conteúdo recuperável sem governar automaticamente outras áreas |
| a carga inicial foi reduzida, mas a porta de estado e o Dossiê ainda abriam rotas extensas e contraditórias | medir também o contexto recuperado em tarefas recorrentes, não apenas a abertura geral | preservar as versões extensas como snapshots e substituir as entradas ativas por referências curtas e coerentes | rotas recorrentes reduzidas em aproximadamente 79% a 80%; verificador ampliado para impedir regressão |
| referências internas antigas dificultavam navegação no Obsidian | reparar apenas links com destino inequívoco e não inventar arquivos ausentes | doze referências reparadas; seis ativos vetoriais ausentes documentados | nenhum link quebrado novo introduzido |
| o verificador protegia arquivos conhecidos, mas aceitava um novo documento ativo que recriasse exclusividade e a arquitetura antiga | examinar dinamicamente arquivos novos ou alterados e distinguir referências ativas de acervo histórico | detecção de autoridade exclusiva, bloqueio de revisão, 7/14 governante e novas portas extensas; verificação automática em propostas de mudança | teste negativo com caminho acentuado passou a ser recusado por três motivos independentes |
| sessões longas podem acumular decisões sem ponto claro de retomada | registrar continuidade apenas em gatilhos reais e atualizar a nota que já cumpre a função | gatilhos de decisão durável, troca de ambiente, risco de perda e correção repetida incorporados ao guia e à skill | reduz perda sem recriar relatório obrigatório ou nova nota por conversa |
| o projeto Posicionamento Profissional e Autoridade exigia treze documentos iniciais e repetia precedência em dezesseis arquivos | uma porta curta deve rotear por tarefa, enquanto currículos, matrizes, bios e comprovantes permanecem referências revisáveis com funções distintas | porta de entrada e prompt reduzidos; nota antiga de precedência preservada como histórico; adaptadores do ChatGPT/Codex e Claude apontam para o mesmo contexto | carga inicial caiu de 21.191 para menos de mil palavras e a repetição de instruções foi retirada sem apagar dados curriculares |
| a auditoria inicial da ramificação principal não incluiu duas propostas antigas ainda abertas, deixando conteúdo exclusivo fora do Obsidian sincronizado | auditorias de encerramento estrutural devem verificar também propostas abertas e ramificações divergentes, sem transformar essa checagem em ritual de tarefas comuns | conteúdo exclusivo recuperado; fatos atuais reconciliados; versões antigas preservadas como histórico | propostas antigas podem ser encerradas sem perda e sem restaurar instruções superadas |

## Organização leve no Obsidian

- usar uma ficha mínima como porta de entrada de cada projeto;
- manter conteúdo no local em que já possui contexto, evitando reorganização apenas estética;
- pesquisar antes de criar uma nova nota;
- atualizar uma fonte existente quando ela já cumprir a função;
- usar poucas propriedades, somente quando ajudarem busca ou leitura;
- distinguir referência atual, versão de trabalho, histórico e substituído sem impedir revisão;
- usar links para fontes realmente úteis, não para formar cadeias obrigatórias de leitura;
- não exigir plugin, painel, modelo ou configuração do Obsidian para o fluxo funcionar;
- preservar materiais brutos e históricos, recuperando-os sob demanda.

## Sinais de que o fluxo precisa ser revisto

- Fabiano precisa corrigir repetidamente a mesma interpretação;
- o assistente pede aprovações que não envolvem conflito real;
- uma versão anterior é tratada como impedimento à criação;
- a resposta exige leitura excessiva antes de contribuir;
- a mesma orientação aparece em vários arquivos;
- conteúdo existente não é encontrado e acaba sendo recriado;
- o Obsidian acumula notas com a mesma função;
- uma ferramenta responde de forma incompatível com outra.

## Revisão proporcional

Quando um desses sinais surgir:

1. localizar a evidência mínima;
2. decidir se é caso isolado ou padrão;
3. propor o menor ajuste;
4. testar o efeito;
5. registrar somente o aprendizado que permanecer útil.

Não criar revisão periódica obrigatória. O aprendizado é acionado pela necessidade real.
