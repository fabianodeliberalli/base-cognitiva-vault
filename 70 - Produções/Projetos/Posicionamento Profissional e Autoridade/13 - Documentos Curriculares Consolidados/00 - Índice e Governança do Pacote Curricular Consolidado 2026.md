---
id: AUT-PAC-00
titulo: Índice e Governança do Pacote Curricular Consolidado 2026
tipo: pacote-curricular-arquivado
status: vigente
versao: 1.0
data: 2026-08-21
autor: Fabiano Deliberalli
tags:
  - currículo
  - dossiê
  - governança
  - continuidade
  - arquivo-editável
  - reprodutibilidade
---

# Finalidade

Este diretório preserva os arquivos editáveis produzidos após a reconciliação curricular de 21/08/2026 e estabelece como eles devem ser atualizados. O objetivo é permitir download, apresentação formal, futuras derivações para site, mídia, CEEP, palestras e contextos acadêmicos, sem romper a fonte única do vault.

# Conteúdo do pacote — versão 1.0

| Arquivo | Função | Tamanho | SHA-256 | Estado |
|---|---|---:|---|---|
| [[Curriculo_Profissional_Consolidado_Fabiano_Deliberalli_2026.docx]] | Currículo profissional ampliado e consolidado | 43.593 bytes | `fc82a1d9e293e0bdea7dee573e61d357d72641d9a7f0438802c7bce1115cacbb` | vigente |
| [[Dossie_Curricular_Mestre_Fabiano_Deliberalli_2026.docx]] | Dossiê integral de consulta, rastreabilidade e derivação | 53.015 bytes | `9f7cd9ab966f54d304efe91174fa26a1ded15ff99ab15c48e9d9cd1e8aebd014` | vigente |
| [[build_curriculum_docs.py]] | Gerador reproduzível dos dois DOCX | 51.759 bytes | `a37efdf7a08951b4c6ad602e860cacf1b0f84ef2104e9ced0c9629d07899559a` | vigente |
| [[requirements.txt]] | Dependência mínima do gerador | — | — | vigente |

# Hierarquia de governança

1. [[../00 - Governança Curricular - Fonte Única e Derivação por Contexto 2026|Governança Curricular]] — regras procedimentais.
2. [[../22 - Matriz Curricular Detalhada - Eixos Datas Cargas e Evidências 2026|Matriz Curricular Detalhada]] — fonte de conteúdo integral.
3. [[../03 - Formação, Evidências e Fontes Documentais|Formação, Evidências e Fontes Documentais]] e pasta `12 - Documentos Comprobatórios` — natureza e rastreabilidade das fontes.
4. [[../01 - Dossiê Curricular Mestre|Dossiê Curricular Mestre em Markdown]] — síntese extensa e organizada.
5. [[../15 - Currículo Profissional Consolidado 2026|Currículo Profissional Consolidado]] e [[../18 - Currículo Profissional Ampliado Consolidado - Versão Pública 2026|Currículo Público Ampliado]] — fontes narrativas derivadas por contexto.
6. Arquivos DOCX deste diretório — snapshots editoriais para distribuição e edição.

Os arquivos binários não devem governar isoladamente uma nova versão. Se houver divergência, prevalecem a correção explícita mais recente de Fabiano e as fontes em Markdown reconciliadas segundo a ordem acima.

# Decisões consolidadas nesta versão

- identidade: **Fabiano Deliberalli — psicólogo clínico e psicoterapeuta — CRP 06/98630**;
- trajetória: **mais de 30 anos de trajetória no cuidado terapêutico, iniciada nas práticas corporais e integrativas e consolidada com a Psicologia**;
- posicionamento: **corpo, trauma, consciência e espiritualidade na compreensão e tradução da experiência humana**;
- Shiozawa: curso de 100h e estágio de 2.000h mantidos separados;
- Bioenergologia: 114 unidades-aula registradas sem conversão automática para horas;
- primeira Psicanálise Integrativa: uma formação de 294h, certificado em 23/07/2002 e declaração em 31/07/2002;
- Brainspotting: Fases 1 a 5 concluídas;
- grafia canônica: **Sofia Bauer**;
- confirmações diretas de Fabiano não geram pendência de digitalização;
- cargas potencialmente duplicadas, aninhadas ou sobrepostas não são somadas automaticamente.

# Protocolo de atualização

1. Registrar a nova informação na matriz curricular e identificar sua natureza na matriz de evidências.
2. Atualizar o dossiê documental pertinente quando houver diploma, certificado, declaração ou auditoria.
3. Reconciliar o Dossiê Curricular Mestre.
4. Atualizar o currículo consolidado, as bios e somente as versões públicas afetadas.
5. Atualizar `build_curriculum_docs.py` para refletir as fontes vigentes.
6. Executar o gerador com Python e `python-docx`.
7. Renderizar e verificar os DOCX antes de substituir os arquivos deste diretório.
8. Calcular novos hashes SHA-256 e registrar tamanho, data, versão e escopo da mudança neste índice.
9. Atualizar [[../23 - Registro de Reconciliação Curricular e Continuidade 2026|Registro de Reconciliação e Continuidade]].
10. Não editar apenas o DOCX sem repercutir a alteração nas fontes em Markdown.

# Reprodução técnica

Ambiente utilizado nesta versão:

- Python 3.12.13;
- python-docx 1.2.0.

Execução:

```bash
python -m pip install -r requirements.txt
python build_curriculum_docs.py
```

Os arquivos são gerados no diretório local `deliverables/`.

# Controle de qualidade da versão 1.0

- currículo: 5 páginas;
- dossiê: 11 páginas;
- integridade ZIP/OOXML: aprovada;
- auditoria de acessibilidade: 0 achados altos, médios ou baixos;
- hierarquia de títulos: aprovada;
- geometria de tabelas: aprovada;
- renderização visual: revisada;
- termos críticos conferidos: Shiozawa, estágio de 2.000h, Bioenergologia, 294h de Psicanálise Integrativa, Sandra Paulsen, Sofia Bauer e Brainspotting.

# Cópias persistentes externas

As mesmas versões foram mantidas na Biblioteca do ChatGPT, preservando identidade e histórico:

- currículo: `libfile_5b8af3cc906c81919383698d09d93fa9`, versão 1;
- dossiê: `libfile_f39133527914819191443c5bc996130d`, versão 1.

Essas cópias facilitam download e uso em chats, mas o vault GitHub/Obsidian permanece como fonte de governança.

# Proveniência

Pacote incorporado pelo PR [#11](https://github.com/fabianodeliberalli/base-cognitiva-vault/pull/11), no branch `codex/atualiza-curriculo-brainspotting-palas-mtc-autohipnose-20260821`.

A síntese das inclusões e correções está em [[../23 - Registro de Reconciliação Curricular e Continuidade 2026|Registro de Reconciliação Curricular e Continuidade]].
