---
tipo: auditoria-e-reavaliacao
projeto: Traduzindo o Ser Humano
status: proposta-para-validacao-de-fabiano
data: 2026-11-26
pedido: "Fabiano, 26/11/2026, 22h59: revisar e auditar todas as PRs incorporadas desde a avaliação e usar o mesmo pedido inicial como parâmetro do que o TSH era, do que é agora e do que pode ser"
relacionado:
  - "[[TSH - Avaliação do produto e do curso - 26-11-2026]]"
  - "[[TSH - Alinhamentos para a disponibilidade na vida real - 26-11-2026]]"
  - "[[TSH - Decisões de 26-11-2026 - aplicação e respostas]]"
  - "[[TSH - Medicina Chinesa no TSH - verificação de contribuições e destinos]]"
---

# Auditoria das PRs e reavaliação do TSH: antes, agora e o que pode ser

O pedido inicial de avaliação (26/11, manhã) serve aqui de régua. **Antes** é o estado descrito na avaliação da manhã. **Agora** é o estado da `main` depois da PR #130. **Pode ser** é o que o material já permite, sem exigir nova arquitetura.

## Em uma página

**O que mudou.** De manhã, o TSH entregava a promessa no conteúdo, mas não na forma: o centro da promessa (ter disponível na vida o que já se compreendeu) dependia da iniciativa do aluno. À noite, o curso tem uma estrutura para isso:

- **Cultivo do Eixo:** a prática diária, com uma versão por módulo ligada à trilha corporal.
- **Retorno ao Eixo:** a versão de trinta segundos.
- **Caderno de Reencontros:** o registro.
- **Pergunta de progresso:** em M2, M4 e M8.
- **Encontros quinzenais:** cada um fecha um módulo.

O Raio X descreve o produto real: 59 aulas, o mapa, a auto-hipnose, a Medicina Chinesa e o Taoísmo como leitura do ser humano, e o calendário. A sua identidade autoral está muito mais presente:
- a monografia de 2004 como raiz;
- a linhagem de Liu Chih Ming;
- as três frases do percurso;
- as experiências incomuns como fio;
- a auto-hipnose como habilidade do aluno.

**O risco principal mudou de lugar.** De manhã, faltavam elementos. Agora, sobram para a forma de aula. Em um dia, cada aula recebeu até quatro camadas novas no dossiê (trilha, Cultivo do Eixo, Medicina Chinesa, sexualidade, fio das experiências incomuns), além das elaborações anteriores. A aula de M2.4 tem 646 palavras de base no dossiê; M3.5 tem quatro acréscimos datados. O modelo de aula é de 12 a 18 minutos. Sem uma triagem do que vai à tela, a riqueza vira sobrecarga, e o ciclo de muitas versões por aula, visto em M2, volta.

**Três outros riscos:**
1. **O sistema de disponibilidade ainda não foi testado com alunos.** A primeira evidência vem no encontro de 12/12, com a pergunta de progresso.
2. **O repositório continua público,** com casos clínicos anonimizados; a mudança fica com Fabiano. Os consentimentos escritos dos casos de M2.4 e M2.6 foram confirmados por Fabiano em 26/11/2026.
3. **A governança estava no limite:** as duas notas de entrada estavam cheias de registros antigos. **Consolidadas em 26/11, 23h:** as duas trazem só o estado atual e as decisões de 26/11, inclusive a dos Cinco Shen; os registros datados foram preservados num registro histórico.

**A auditoria encontrou e corrigiu, nesta PR:**
- sete pontes do dossiê que ainda apontavam a numeração anterior à reorganização de M4 a M6;
- o destino do poema de Portia Nelson (agora M6.7);
- um rótulo do Raio X que dizia "à espera" para algo já integrado.

## 1. As PRs auditadas

| PR | O que fez | Coerência com o conjunto | Resíduo encontrado |
|---|---|---|---|
| #121 | Texto seu sobre padrões e ressonância; o buraco de Portia Nelson; recursos de Qi Gong em M3.8 | Coerente | O destino "M6.8" do poema ficou desatualizado com a reorganização (é M6.7). **Corrigido** |
| #122 | Fecho de M2.6 com as três direções do mapa, no slide e no roteiro | Coerente | Nenhum |
| #123 | Mapa do percurso explícito nas notas de estruturação | Coerente | Nenhum |
| #124 | Mapa nas descrições da Hotmart (M2 a M8) e no próximo lançamento | Coerente | Nenhum |
| #125 | Cadastro da Hotmart em sete documentos, com a imagem do percurso | Atualizado depois por #128 (datas, M2.1 em duas partes, M4 a M6) | Nenhum; títulos conferidos com os nomes de 22/11 |
| #126 | Avaliação do produto e do curso | Vira fotografia da manhã; esta nota a atualiza | Nenhum |
| #127 | Alinhamentos para a disponibilidade na vida real; Raio X vigente de 26/11; Cultivo do Eixo e Caderno | Coerente; base do sistema de disponibilidade | Nenhum |
| #128 | Decisões de 26/11: lançamento, apoios de M2, calendário quinzenal, reorganização de M4 a M6, trilha de cultivo, experiências incomuns | A reorganização foi aplicada aos títulos e às seções, mas não a todas as pontes entre aulas | Sete pontes do dossiê com números antigos (M1.7, M2.4, M3.3, M4.6, M5.3, M5.6, M6.5). **Corrigidas** |
| #129 | Ligação Cultivo do Eixo–trilha; Medicina Chinesa no TSH, revisada com as três apresentações | Coerente | Nenhum |
| #130 | Raio X com a Medicina Chinesa e o Taoísmo como leitura; três frases; sexualidade; Cinco Shen restaurados | Coerente com a sua decisão definitiva | No Raio X, o arco ainda dizia "proposta à espera". **Corrigido** |

**O que a auditoria conferiu e está consistente:**
- as 59 aulas aparecem no dossiê e no Raio X;
- os títulos da Hotmart coincidem com os de 22/11;
- o calendário quinzenal é o mesmo no Raio X, na Hotmart, no calendário da turma e nas notas de estado, sem datas antigas restantes;
- a conferência do repositório passa.

**O que ficou aberto e não se corrige com edição:**
- **Títulos de M0 e M1 no Raio X.** O Raio X usa os títulos já publicados de M0 e M1; a revisão de 22/11 propõe títulos novos para a próxima turma. Não é erro, mas é uma decisão sua para quando M0 e M1 forem revistos.
- **Três links quebrados na nota "LEIA PRIMEIRO",** desde 14/11 (Ely Britto, Naranjo, empatia e compaixão). **Resolvido na consolidação:** a nota foi reescrita com os links certos; o texto antigo está preservado no registro histórico, com a indicação dos nomes atuais.
- **Notas de entrada.** A "LEIA PRIMEIRO" estava a 25 bytes do limite de 12.000 que a conferência impõe, e ainda trazia o calendário antigo (último encontro em 30/01/2027). A de contexto mínimo não tem esse limite na conferência (a afirmação anterior de que ela recusava alterações estava errada), mas estava desatualizada. **Consolidadas em 26/11, 23h:** 6,4 mil e 9,1 mil bytes.
- **O guia da Masterclass de novembro também está acima do limite e congelado.** As três frases ficaram na nota do próximo lançamento.

## 2. O mesmo pedido em três tempos

| Critério do pedido | Antes (manhã de 26/11) | Agora (noite de 26/11) | O que ainda pode ser |
|---|---|---|---|
| **Congruência** entre produto, oferta e identidade | A oferta descrevia outro produto (54 aulas, nomes antigos, sem Qi Gong nem mapa) | Raio X, Hotmart e currículo descrevem o mesmo curso | Uma só formulação em todas as peças do próximo lançamento, a partir do Raio X |
| **Percurso** | Mapa de três direções recém-nomeado | Mapa em todas as peças; três frases suas que o dizem; auto-hipnose nas três direções | O mapa vivido em atos: cada módulo com uma aula que volta explicitamente a uma direção anterior |
| **Coerência interna** | M5 com nove temas; M6 misturando reflexão e três práticas avançadas; M7 sem interlocutor | M5 em três arcos, com os Três Eus na abertura; Hara em M4.6 e circulações alternadas em M6; interlocutor para M7 decidido | Uma página que mostre como os mapas do curso se relacionam (ver seção 4) |
| **Profundidade** | Forte em M2, M3, M5.7–M5.9 e M7.7 | Ampliada: a monografia como raiz; o Taoísmo como leitura; os Cinco Shen; a Flor de Ouro; as experiências incomuns como fio | Está no limite do que cabe; o ganho agora vem de escolher, não de acrescentar |
| **Promessa e entrega** | Entrega parcial no centro da promessa: sem prática entre as aulas | Há estrutura: prática diária com versões, retorno de 30 s, caderno, progresso, encontros | Entrega comprovada: a pergunta de progresso respondida em M2, M4 e M8 mostra se o acesso aumentou |
| **Objetivo desejado e realizado** | Desejado: compreensão disponível na vida. Realizado: conteúdo | Desejado igual. Realizado: desenho completo, mas ainda no papel; M0 e M1 publicados e lançamento do caderno em 28/11 | Realizado na vida do aluno: o primeiro teste é o encontro de 12/12 |
| **O que estava presente e o que faltava** | Faltavam prática contínua, registro, interlocutor, segurança e progresso | Presentes: prática, registro, interlocutor e progresso. Segurança dispensada por você, com os cuidados dentro das aulas | Depoimentos verificáveis a partir da pergunta de progresso |
| **Identidade autoral** | Sua voz só a partir de M2; experiências incomuns ausentes | Monografia, linhagem, três frases, experiências incomuns (nova M5.8), auto-hipnose, uma cena sua por aula no padrão | A assinatura pública do TSH: Medicina Chinesa como leitura, experiências incomuns com discernimento, auto-hipnose como habilidade |
| **Comunicação** | "Mapa simples para sair do automático" dizia pouco do seu diferencial | Diferencial explícito; três frases para a Masterclass; ressalvas na seção "Para quem não é" | Masterclass com a dor, as três frases e uma demonstração curta da árvore |
| **Produção** | 46 aulas em oito semanas; muitas versões por aula em M2 | Calendário quinzenal até 03/04; modelo mínimo de aula; apoios de uma página | Uma triagem por aula antes de escrever (seção 4); um arquivo vivo por aula |
| **Sustentabilidade** | Não avaliada em detalhe | Encontros quinzenais com hora de prática; suporte pelo grupo da turma | Encontros gravados como acervo reutilizável; escada de ofertas (seção 5) |
| **Governança** | Repositório público com casos; notas de entrada cheias | Igual. Decisões registradas, mas as notas de entrada não comportam mais | Consolidar as notas de entrada; repositório privado |

## 3. O que mudou de verdade e o que mudou só no papel

Quase tudo o que mudou hoje está em documentos: Raio X, dossiê, notas, cadastro da Hotmart, caderno, guia e calendário. Para o aluno, ainda nada mudou: ele tem M0 e M1. A primeira mudança que ele vai viver é o encontro de 28/11, com o lançamento do Cultivo do Eixo e do caderno, e a liberação de M2 em 29/11.

Isso não diminui o trabalho feito, mas muda a pergunta certa. Até agora era "o curso está bem desenhado?", e a resposta é sim, bem mais do que de manhã. A partir de 28/11, a pergunta é "o aluno faz o Cultivo do Eixo na segunda semana?". O desenho da disponibilidade depende de adesão, e adesão é o que costuma cair entre a segunda e a quarta semana.

Duas medidas baratas protegem esse ponto:
- uma mensagem curta no grupo no meio de cada quinzena, com a versão do Cultivo do Eixo do módulo;
- os primeiros dez minutos de cada encontro dedicados ao caderno, com a pergunta "o que voltou e como foi desta vez?".

## 4. Riscos novos e como reduzi-los

**O excesso por aula.** É o risco principal. Antes de escrever cada roteiro de M3 em diante, separar o que o dossiê traz em quatro destinos:
1. **Núcleo da tela:** uma pergunta, uma distinção, uma prática, uma cena sua.
2. **Fala opcional:** uma frase da monografia, de uma tradição ou de um autor.
3. **Material do aluno:** o apoio de uma página.
4. **Fundamentação sua:** o que você sabe e não precisa dizer.

M3.5 é o primeiro teste. Hoje ela reúne:
- Qi como transformação;
- a linhagem;
- os Três Tesouros;
- os Cinco Shen;
- o Sorriso Interior;
- o Jing com a energia sexual;
- a trilha prática.

Tudo isso cabe no curso, mas não numa aula de 12 a 18 minutos. Uma saída coerente com as suas decisões é apresentar os Cinco Shen em M3.5 como visão geral e desenvolver cada um onde ele já tem linha: Yi em M2.6 e M5.2; Zhi em M4.6; Hun em M5.5 e M5.6; Po e Hun em M5.8.

**A pluralidade de mapas.** O aluno vai encontrar:
- o mapa do percurso;
- Centro, eixo e estado;
- as Cinco Janelas;
- a Cartografia;
- os Três Eus;
- as partes;
- os sete níveis;
- os Cinco Shen;
- os três Tan Tien.

Cada um responde a uma pergunta diferente, e isso é coerente com M1.4 ("a experiência é o território; as explicações são mapas"). Mas o aluno precisa ver isso. Uma página, "os mapas do TSH e a pergunta de cada um", anexada a M1.4 e retomada em M5.1, resolve sem mexer em nenhuma aula.

**O sistema ainda não foi testado.** Tratar a turma atual como primeira medição:
- a pergunta de progresso no início de M2 (encontro de 28/11) e de novo em M4;
- uma pergunta aberta em cada encontro sobre o Cultivo do Eixo, para ajustar as versões dos módulos seguintes.

**A carga do autor.**
- De 13/12 a 03/04: M3 a M8, com 43 aulas, seis encontros e os apoios.
- O ritmo quinzenal comporta isso se o ciclo de versões de M2 não se repetir.
- A triagem acima e o modelo mínimo são a proteção.
- Gravar M3.6 e M3.7 em estúdio, como previsto.

**Privacidade e consentimento.**
- O repositório continua público.
- Os consentimentos escritos dos dois casos de M2.4 e M2.6 foram confirmados por Fabiano em 26/11/2026.
- A mudança para privado é sua, no GitHub, depois de conectar o GitHub ao ChatGPT para não perder o acesso dele.

**Governança.** As duas notas de entrada estão no limite. Vale uma consolidação curta, que retire delas o que é histórico e deixe só o estado atual e os ponteiros. Sem isso, cada nova decisão sua fica em notas que uma IA só encontra se souber procurar.

## 5. O que o TSH pode ser

- **Na próxima turma:**
  - M0 e M1 com corpo e voz desde o início: a nova M0.1 complementar e uma prática curta em cada aula de M1;
  - os títulos revistos de 22/11;
  - "aulas objetivas, com prática guiada" como formato declarado.
- **Como evidência:**
  - a pergunta de progresso, com acesso de 0 a 10, tempo de retorno e uma linha aberta, gera dados honestos para depoimentos;
  - com consentimento, pode gerar um relato observacional da turma, coerente com a sua formação em neurociências.
- **Como escada de ofertas:**
  - o Workshop do TSH como entrada;
  - o curso como percurso;
  - o Laboratório e a Imersão como aprofundamento presencial: alquimia taoísta e sexualidade, circulações avançadas, Cinco Shen em profundidade, prática relacional em grupo.
- **Como assinatura pública,** três temas que nenhum outro curso junta com o mesmo cuidado:
  - a Medicina Chinesa como leitura do ser humano;
  - as experiências incomuns com discernimento;
  - a auto-hipnose ensinada como habilidade do aluno.

## 6. Próximos passos por prazo

**Até 29/11**
- ~~Consentimento escrito dos casos de M2.4 e M2.6~~: confirmado por Fabiano em 26/11.
- Repositório privado: fica com Fabiano.
- M2.1 dividida em duas partes na edição.
- Publicar o cadastro de M2 na Hotmart.
- No encontro de 28/11: lançar o Cultivo do Eixo e o caderno, e aplicar a pergunta de progresso.

**Até a liberação de M3 (13/12)**
- Aplicar a triagem de quatro destinos às oito aulas de M3, começando por M3.5.
- Decidir a nova M0.1 complementar.
- Ler as respostas do encontro de 12/12 e ajustar a versão de M3 do Cultivo do Eixo.

**Antes do próximo lançamento**
- A página "os mapas do TSH e a pergunta de cada um".
- A consolidação das notas de entrada.
- A Masterclass com as três frases e a demonstração da árvore.
- Os depoimentos a partir da pergunta de progresso.
