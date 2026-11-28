"""Checklist clicável da produção (HTML único, progresso salvo no navegador)."""
import sys, html, json
OUT = sys.argv[1]
H = "../TSH-2-Hotmart/"

# (seção, subtítulo, [(texto, detalhe, link ou None)])
S = [
 ("Hoje, sexta 27/11", "Preparar o encontro de amanhã", [
  ("Enviar a mensagem à turma no grupo", "Texto pronto: copie e cole.", "00-Mensagem-para-a-turma.txt"),
  ("Imprimir ou deixar aberto o roteiro de bolso", "Uma página: horários, telas e os cortes para marcar.", "01-Sab-28-11-Encontro/Encontro-28-11-roteiro-de-bolso.pdf"),
  ("Abrir os slides do encontro no modo apresentador", "22 telas; as notas de condução ficam só para você.", "01-Sab-28-11-Encontro/Encontro-28-11-slides.pptx"),
  ("Se quiser o texto completo: o roteiro do encontro", "O mesmo conteúdo das notas, em documento.", "01-Sab-28-11-Encontro/Roteiro-encontro-28-11.docx"),
  ("Conferir o Zoom: gravação ligada, link no grupo", "A gravação vira quatro vídeos.", None),
  ("Separar um lugar para ficar de pé na segunda hora", "A árvore e a prática de 30 min são de pé.", None),
 ]),
 ("Sábado 28/11, 9h às 11h", "Encontro ao vivo · gravar tudo", [
  ("Iniciar a gravação do Zoom", "", None),
  ("Módulo 1 em prática guiada (10 a 12 min)", "Vira o corte 0: aula nova no fim do Módulo 1.", None),
  ("Dúvidas de M0 e M1 (resto da primeira hora)", "Duas falas opcionais estão no roteiro.", None),
  ("Abertura do Módulo 2 (10 min)", "Corte 1.", None),
  ("O eixo no corpo: Zhan Zhuang (10 min)", "Corte 2: entra no M2 e no M0 («Comece pelo corpo»).", None),
  ("Prática «Do primeiro sinal ao eixo» (30 min)", "Corte 3.", None),
  ("Pergunta de progresso, Cultivo do Eixo e Caderno", "Sem corte.", None),
  ("Salvar a gravação e anotar os horários de início de cada bloco", "Facilita a edição dos quatro cortes.", None),
 ]),
 ("Sábado à tarde e domingo cedo", "Gravar o Módulo 2 · siga o guia", [
  ("Abrir o guia de gravação do M2", "Cada tela tem a nota do que dizer.", "02-M2-gravar-ate-29-11/M2-Guia-de-gravacao.docx"),
  ("Gravar a ponte de 2.1 (3 a 4 min)", "Mostra o mapa O Caminho da Semente; vai antes da teoria já gravada de 2.1.", "02-M2-gravar-ate-29-11/M2-1-Ponte.pptx"),
  ("Gravar a ponte de 2.2 (3 a 4 min)", "Vai antes da teoria já gravada de 2.2.", "02-M2-gravar-ate-29-11/M2-2-Ponte.pptx"),
  ("Gravar a ponte de 2.3 (3 a 4 min)", "Vai antes da teoria já gravada de 2.3.", "02-M2-gravar-ate-29-11/M2-3-Ponte.pptx"),
  ("Gravar a prática de 2.2 (8 a 10 min)", "", "02-M2-gravar-ate-29-11/M2-2-Pratica.pptx"),
  ("Gravar a prática de 2.3 (10 a 12 min)", "", "02-M2-gravar-ate-29-11/M2-3-Pratica.pptx"),
  ("Gravar a teoria de 2.4 (15 a 18 min)", "", "02-M2-gravar-ate-29-11/M2-4-Teoria.pptx"),
  ("Gravar 2.5 (12 a 14 min)", "", "02-M2-gravar-ate-29-11/M2-5-Acontecimento-experiencia.pptx"),
  ("Gravar 2.6 (12 a 14 min)", "", "02-M2-gravar-ate-29-11/M2-6-Traducao-provisoria.pptx"),
 ]),
 ("Domingo 29/11", "Editar e publicar", [
  ("Dividir a teoria de 2.1 em duas partes de cerca de 19 min", "No ponto em que a aula passa da explicação para a exploração.", None),
  ("Colocar cada ponte no início da teoria já gravada (2.1, 2.2, 2.3)", "", None),
  ("Editar os quatro cortes do encontro (0, 1, 2 e 3)", "", None),
  ("Nomear os vídeos como indicado em cada aula.txt", "", H + "LEIA.txt"),
  ("Hotmart · M0: aula nova «Comece pelo corpo» (corte 2) com anexos", "", H + "M0/alteracoes.txt"),
  ("Hotmart · M1: as quatro alterações, a aula nova (corte 0) e os anexos", "Inclui o mapa do Módulo 1 na aula 1.4.", H + "M1/alteracoes.txt"),
  ("Hotmart · M2: nome, descrição e capa do módulo", "", H + "M2/modulo.txt"),
  ("Hotmart · M2: as 12 aulas, na ordem, com vídeo e anexos", "Pastas A01 a A12.", H + "M2/"),
  ("Hotmart · M2: liberação em 29/11", "", None),
  ("Avisar a turma que o Módulo 2 está liberado", "", None),
 ]),
 ("Depois de 29/11, sem pressa", "Quando houver espaço", [
  ("Gravar a aula complementar do Módulo 0 (6 a 8 min)", "Roteiro e slides prontos.", "04-M0-aula-complementar/M0-Roteiro.docx"),
  ("Publicar a aula complementar logo depois da 0.1", "", H + "M0/A-nova-depois-da-0-1-O-percurso/aula.txt"),
  ("Roteiro do encontro de 12/12 (encontro do Módulo 2)", "Pedir à IA na próxima rodada.", None),
  ("Revisar o Módulo 3 com calma, antes de gravar", "Rascunho completo; nada a gravar ainda. Liberação marcada para 13/12.", "03-M3-EM-REVISAO-nao-gravar/"),
  ("Decidir a triagem de materiais (proposta registrada)", "Retomar com a IA depois de 29/11.", None),
  ("Recolher dos alunos: qual mapa ajudou, e qual confundiu?", "Ajusta as páginas de mapas.", None),
 ]),
]

items = []
blocos = []
for si, (tit, sub, its) in enumerate(S):
    lis = []
    for ii, (t, d, link) in enumerate(its):
        k = f"s{si}i{ii}"; items.append(k)
        a = f' <a href="{html.escape(link)}">abrir</a>' if link else ""
        dd = f'<div class="d">{html.escape(d)}</div>' if d else ""
        lis.append(f'<li><label><input type="checkbox" data-k="{k}"><span class="t">{html.escape(t)}{a}{dd}</span></label></li>')
    blocos.append(f'<section><h2>{html.escape(tit)}<small>{html.escape(sub)}</small><span class="c" data-s="{si}"></span></h2><ul>{"".join(lis)}</ul></section>')

doc = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TSH · checklist de produção até 29/11</title>
<style>
body{{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:#F4EFEA;color:#082A45}}
.w{{max-width:820px;margin:0 auto;padding:28px 22px 60px}}
.m{{font-size:11px;letter-spacing:.18em;font-weight:700;color:#245E78}}
h1{{font-family:'EB Garamond',Georgia,serif;font-weight:400;font-size:34px;margin:6px 0 4px}}
.sub{{color:#245E78;margin-bottom:16px}}
.bar{{position:sticky;top:0;background:#F4EFEA;padding:10px 0 12px;z-index:2}}
.track{{height:12px;background:#E2D8CC;border-radius:6px;overflow:hidden}}
.fill{{height:100%;background:#C99A64;width:0;transition:width .3s}}
.pt{{font-size:14px;margin-top:6px;display:flex;justify-content:space-between}}
section{{background:#FBF8F4;border:1px solid #E2D8CC;border-radius:12px;margin:16px 0;padding:6px 18px 10px}}
h2{{font-family:'EB Garamond',Georgia,serif;font-weight:500;font-size:24px;margin:12px 0 6px;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}
h2 small{{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:13px;color:#5A6B74;font-weight:400}}
h2 .c{{margin-left:auto;font-family:Inter,Segoe UI,Arial,sans-serif;font-size:12px;color:#173F52;background:#ECE5DC;padding:2px 10px;border-radius:10px}}
h2 .c.ok{{background:#173F52;color:#fff}}
ul{{list-style:none;margin:0;padding:0}}
li{{border-top:1px solid #ECE5DC}}
label{{display:flex;gap:12px;padding:11px 2px;cursor:pointer;align-items:flex-start}}
input{{width:22px;height:22px;accent-color:#173F52;flex:none;margin-top:1px;cursor:pointer}}
.t{{font-size:16px;line-height:1.35}}
.d{{font-size:13px;color:#5A6B74;margin-top:2px}}
a{{color:#245E78;font-size:13px;margin-left:6px}}
input:checked + .t{{color:#8a979e;text-decoration:line-through}}
.tools{{margin-top:22px;font-size:13px;color:#5A6B74}}
button{{font:inherit;background:none;border:1px solid #C99A64;color:#173F52;border-radius:8px;padding:6px 12px;cursor:pointer;margin-right:8px}}
@media print{{.bar,.tools{{display:none}} section{{break-inside:avoid}}}}
</style></head><body><div class="w">
<div class="m">TRADUZINDO O SER HUMANO</div>
<h1>Checklist de produção</h1>
<div class="sub">Do encontro de 28/11 à liberação do Módulo 2, em 29/11. Marque cada passo; o progresso fica salvo neste computador.</div>
<div class="bar"><div class="track"><div class="fill" id="f"></div></div><div class="pt"><span id="p"></span><span>Os links «abrir» funcionam com as duas pastas extraídas lado a lado.</span></div></div>
{"".join(blocos)}
<div class="tools"><button onclick="window.print()">Imprimir</button><button onclick="if(confirm('Desmarcar tudo?')){{try{{localStorage.removeItem(K)}}catch(e){{}};location.reload()}}">Recomeçar</button>
Versão de 27/11/2026.</div>
</div>
<script>
const K='tsh-checklist-27-11c';const ALL={json.dumps(items)};let st={{}};
try{{st=JSON.parse(localStorage.getItem(K)||'null');if(!st){{const o=JSON.parse(localStorage.getItem('tsh-checklist-27-11b')||'{{}}');const mv={{'s0i1':'s0i3','s0i2':'s0i4','s0i3':'s0i5'}};st={{}};for(const k in o){{st[mv[k]||k]=o[k]}};localStorage.setItem(K,JSON.stringify(st))}}}}catch(e){{st=st||{{}}}}
const boxes=[...document.querySelectorAll('input[data-k]')];
function upd(){{const n=boxes.filter(b=>b.checked).length;document.getElementById('f').style.width=(100*n/boxes.length)+'%';
document.getElementById('p').textContent=n+' de '+boxes.length+' passos';
document.querySelectorAll('h2 .c').forEach(c=>{{const s=c.dataset.s;const bs=boxes.filter(b=>b.dataset.k.startsWith('s'+s+'i'));const k=bs.filter(b=>b.checked).length;c.textContent=k+'/'+bs.length;c.classList.toggle('ok',k===bs.length)}})}}
boxes.forEach(b=>{{b.checked=!!st[b.dataset.k];b.addEventListener('change',()=>{{st[b.dataset.k]=b.checked;try{{localStorage.setItem(K,JSON.stringify(st))}}catch(e){{}};upd()}})}});upd();
</script></body></html>"""
open(OUT, "w", encoding="utf-8").write(doc)
print(len(items), "passos")
