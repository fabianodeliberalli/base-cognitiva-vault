---
title: "TSH — Ajustes a partir do retorno de uma aluna sobre o Módulo 1"
date: 2026-11-27
status: aplicado na produção de M1 a M3, aguardando integração por Fabiano
---

# Ajustes a partir do retorno de uma aluna sobre o Módulo 1 (27/11/2026)

## O retorno

Uma aluna relatou dificuldade com o Módulo 1: ansiedade por não acompanhar, teoria nos vídeos sem exercícios, material escrito difícil. Sugeriu misturar teoria e exercícios guiados nos vídeos e deixar o escrito como apoio opcional. O ritmo quinzenal, segundo ela, pode ajudar.

## Leitura

O retorno aponta uma incoerência real entre o que o curso diz e o que os vídeos de M1 fazem: o curso afirma que compreensão não basta e que a mudança se dá na experiência, mas M1 entrega sobretudo compreensão e transfere a prática para o escrito, fora do vídeo. A dificuldade não é falta de esforço da aluna; é o formato. Os slides de M2 e M3 já intercalavam práticas, mas pediam "pause o vídeo e registre", o que repete a mesma transferência.

## Os cinco ajustes aprovados por Fabiano

1. **Práticas guiadas no vídeo, escrita opcional (M2 e M3).** Telas de prática dizem "faça comigo agora; anotar é opcional". As notas de fala trocam "pause o vídeo" por 30 a 60 segundos de silêncio com a tela parada, conduzindo, e "se quiser, anote no Caderno; se não, siga comigo". Os apoios de uma página dizem "Prática (faça junto com o vídeo)" e "No Caderno de Reencontros, se quiser".
2. **Módulo 1 em prática guiada.** Bloco de 10 a 12 minutos no início da primeira hora do encontro de 28/11, sete passos sem escrita, um por aula de M1. Gravado como corte 0 e publicado no fim do Módulo 1 como aula nova. Roteiro: `Materiais/Módulo 2/M2 - Encontro de 28-11 - …`, seção "Bloco M1".
3. **Apoios de uma página para as sete aulas de M1**, no modelo de M2, como porta de entrada principal do escrito: `Materiais/Módulo 1/Apoios do aluno - uma página/`. Cada um tem a ideia central, uma frase de Fabiano já registrada, a prática que o vídeo guia e uma linha opcional de registro.
4. **Caminho mínimo por módulo** na descrição de M1 a M8, para quinzenas com pouco tempo: duas aulas (no M1, o vídeo de prática guiada) e o Cultivo do Eixo, com a frase "Nada se perde: o resto continua aqui". Fonte: `MINIMO` em `Hotmart - Cadastro dos Módulos 2 a 8/Fontes/dados.py`.
5. **Mensagem à turma:** não existe atraso. Texto em `Materiais/Módulo 2/M2 - Mensagem à turma de 27-11 - não existe atraso.md`.

## O que fica para depois

- Os vídeos já publicados de M1 não foram regravados. O vídeo de prática guiada cumpre a função de exercício até que Fabiano decida se quer revisar M1.
- De M4 a M8, o mesmo padrão vale na produção: prática conduzida no vídeo, escrita opcional, apoio de uma página.

## Pacotes de entrega

Os pacotes para baixar passaram a ter nomes curtos, sem acentos, e a ser compactados sem a pasta raiz duplicada. O pacote anterior falhava no Windows por dois motivos: os nomes com acento e "·" não estavam marcados como UTF-8 no zip, e vários caminhos passavam de 260 caracteres depois de extraídos. O gerador da Hotmart é `Fontes/pacote_upload.py`.
