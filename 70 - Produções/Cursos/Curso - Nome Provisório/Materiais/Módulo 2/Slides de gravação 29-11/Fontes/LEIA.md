# Fontes dos slides de gravação de M2 (25/11/2026)

- `base.py`: tipos de tela (capa, frase, história, cartões, sequência, dois polos, eixo, passo de prática, comparação, imagem, fechamento). Usa `tsh_lib.py`, `anim.py` e `assets/` de [[Padrão de Slides - ferramentas/README|Padrão de Slides - ferramentas]] e a imagem da escada de `40 - Fundamentos e Patrimônio`.
- `decks_a.py`: pontes de M2.1 a M2.3 e teoria de M2.4. `decks_b.py`: práticas de M2.2 e M2.3. `decks_c.py`: M2.5 e M2.6.
- `ilustracoes.py`: gera as oito ilustrações originais (pasta `Ilustrações/`), em SVG convertido para PNG com sharp. Histórias e metáforas aparecem só como imagem; a condução e as correlações ficam nas notas (versão 2, 25/11/2026).
- `guia.py` e `guia_intro.md`: geram o guia de gravação a partir das notas dos arquivos PowerPoint.

Para reconstruir, copie `tsh_lib.py`, `anim.py`, `assets/` e as imagens como `img/escada.png` e `img/<nome>.png` para a pasta dos scripts e rode `python decks_a.py`, `decks_b.py`, `decks_c.py` e `guia.py`. Os caminhos de saída estão no início de cada script.

Forma das notas: função entre colchetes na primeira linha; uma frase por linha; « » para o que se diz como está; [PAUSA] onde o aluno pausa; → para a tela seguinte. As telas não têm animação por clique.
