"""Transições (esmaecimento) em todos os slides + entradas progressivas por clique com marcas nas notas."""
import sys
from lxml import etree
from pptx import Presentation
from pptx.util import Inches
from pptx.oxml.ns import qn

P = "http://schemas.openxmlformats.org/presentationml/2006/main"

def transition(slide):
    el = slide._element
    for t in el.findall(qn("p:transition")): el.remove(t)
    tr = etree.fromstring(f'<p:transition xmlns:p="{P}" spd="med"><p:fade/></p:transition>')
    # ordem: cSld, clrMapOvr, transition, timing
    anchor = el.find(qn("p:clrMapOvr"))
    idx = list(el).index(anchor) + 1 if anchor is not None else 1
    el.insert(idx, tr)

def timing(slide, groups):
    """groups: lista de listas de shape ids; cada grupo aparece num clique (esmaecer, 0,5 s)"""
    el = slide._element
    for t in el.findall(qn("p:timing")): el.remove(t)
    nid = [2]
    def i():
        nid[0] += 1; return nid[0]
    pars = []
    for g in groups:
        effs = []
        for k, sid in enumerate(g):
            node = "clickEffect" if k == 0 else "withEffect"
            effs.append(
                f'<p:par><p:cTn id="{i()}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="{node}">'
                f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                f'<p:set><p:cBhvr><p:cTn id="{i()}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
                f'<p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
                f'<p:to><p:strVal val="visible"/></p:to></p:set>'
                f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{i()}" dur="500"/>'
                f'<p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl></p:cBhvr></p:animEffect></p:childTnLst></p:cTn></p:par>')
        pars.append(f'<p:par><p:cTn id="{i()}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
                    f'<p:childTnLst><p:par><p:cTn id="{i()}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
                    f'<p:childTnLst>{"".join(effs)}</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    blds = "".join(f'<p:bldP spid="{sid}" grpId="0"/>' if True else "" for g in groups for sid in g)
    # bldP só vale para formas com texto; para as demais o PowerPoint aceita sem bldLst
    xml = (f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
           f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{"".join(pars)}</p:childTnLst></p:cTn>'
           f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
           f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
           f'</p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')
    tm = etree.fromstring(xml)
    tr = el.find(qn("p:transition"))
    idx = list(el).index(tr) + 1 if tr is not None else len(el)
    el.insert(idx, tm)

def mark_notes(slide, anchors):
    tf = slide.notes_slide.notes_text_frame
    done = []
    for a in anchors:
        for p in tf.paragraphs:
            hit = False
            for r in p.runs:
                if a in r.text:
                    r.text = r.text.replace(a, "[CLIQUE] " + a, 1); hit = True; break
            if hit: done.append(a); break
    missing = [a for a in anchors if a not in done]
    if missing: raise SystemExit(f"âncora não encontrada: {missing}")
    # aviso na condução
    ps = list(tf.paragraphs)
    for idx, p in enumerate(ps):
        if p.text.strip().startswith("CONDUÇÃO"):
            nxt = ps[idx + 1]
            nxt.runs[-1].text = nxt.runs[-1].text.rstrip() + f" Esta tela tem {len(anchors)} clique(s) interno(s), marcados como [CLIQUE] na fala."
            break

def ids_by_name(slide, *names):
    m = {s.name: s.shape_id for s in slide.shapes}
    return [m[n] for n in names]

def ids_in_box(slide, x0, y0, x1, y1, exclude_text=True):
    """formas estáticas (sem nome de conteúdo) cujo centro cai na caixa, em polegadas"""
    out = []
    for s in slide.shapes:
        cx = (s.left + s.width / 2) / 914400; cy = (s.top + s.height / 2) / 914400
        if x0 <= cx <= x1 and y0 <= cy <= y1: out.append(s.shape_id)
    return out

if __name__ == "__main__":
    src, out, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    prs = Presentation(src); S = prs.slides
    for s in S: transition(s)
    if mode == "m02":
        s = S[1]
        timing(s, [ids_by_name(s, "resource-1", "function-1"), ids_by_name(s, "resource-2", "function-2"), ids_by_name(s, "choice")])
        mark_notes(s, ["A ficha permite", "O guia ajuda", "Você pode começar pelo recurso"])
        s = S[4]
        timing(s, [ids_by_name(s, f"dimension-{k}", f"example-{k}") for k in (1, 2, 3)])
        mark_notes(s, ["Na dimensão mental", "Na dimensão relacional", "E há condições concretas"])
        s = S[6]
        timing(s, [ids_by_name(s, "open")])
        mark_notes(s, ["Você pode começar por uma impressão"])
        s = S[8]
        dark = [x for x in ids_in_box(s, 0.9, 3.7, 12.5, 6.45) if x not in ids_by_name(s, "qualification")]
        timing(s, [dark, ids_by_name(s, "qualification")])
        mark_notes(s, ["Ao olhar o desenho", "Esse é um desenvolvimento possível"])
        s = S[9]
        timing(s, [ids_by_name(s, "field-1", "answer-1"), ids_by_name(s, "field-2", "answer-2"), ids_by_name(s, "permission")])
        mark_notes(s, ["Depois, em “O que permanece aberto?”", "E o próximo passo pode ser", "A necessidade de descanso pode ser legítima"])
        s = S[11]
        g = ids_by_name(s, "specific-guidance") + ids_in_box(s, 0.95, 6.1, 1.15, 6.3)
        timing(s, [ids_by_name(s, "mode-1", "use-1"), ids_by_name(s, "mode-2", "use-2"), g])
        mark_notes(s, ["Quando surge uma dúvida", "Na prática acompanhada", "Nas atividades corporais"])
    if mode == "m03":
        s = S[2]
        qid = ids_by_name(s, "questions") + ids_in_box(s, 0.95, 4.8, 1.15, 5.05)
        timing(s, [qid, ids_by_name(s, "foot")])
        mark_notes(s, ["Antes de transformar isso", "Para começar, escolha"])
        s = S[8]
        big = {x.shape_id for x in s.shapes if x.width > Inches(8)}
        rows = [[i for i in ids_in_box(s, 1.3, 2.45 + k * 1.25, 12.3, 2.45 + k * 1.25 + 1.0) if i not in big] for k in (1, 2)]
        timing(s, rows + [ids_by_name(s, "pause")])
        mark_notes(s, ["Segundo:", "Terceiro:", "Você pode pausar o vídeo agora"])
    if mode == "m11":
        def col(s, x0, x1, y0, y1):
            return [sh.shape_id for sh in s.shapes
                    if x0 <= (sh.left + sh.width / 2) / 914400 <= x1 and y0 <= (sh.top + sh.height / 2) / 914400 <= y1
                    and not (sh.width > Inches(2) and sh.height > Inches(1) and not (sh.has_text_frame and sh.text_frame.text.strip()))]
        s = S[1]; cw = (11.5 - 0.84) / 4
        timing(s, [col(s, 0.92 + k * (cw + 0.28) - 0.28, 0.92 + k * (cw + 0.28) + cw, 2.5, 5.2) for k in (1, 2, 3)])
        mark_notes(s, ["Ela lê, sente um aperto", "responde quase imediatamente", "Pouco depois, olha para a agenda"])
        cw3 = (11.5 - 0.56) / 3
        for si, anc in ((8, ["Depois, diferenciar", "Expressar: que palavra"]), (9, ["Rever: o que está claro", "E participar:"])):
            s = S[si]
            timing(s, [col(s, 0.92 + k * (cw3 + 0.28), 0.92 + k * (cw3 + 0.28) + cw3, 2.45, 5.95) for k in (1, 2)])
            mark_notes(s, anc)
        s = S[10]
        cells = [(6.95, 2.55), (1.35, 4.45), (6.95, 4.45)]
        timing(s, [col(s, x, x + 5.1, y, y + 1.6) for x, y in cells])
        mark_notes(s, ["No segundo, registre", "Esse é o terceiro espaço", "Por fim: o que quero"])
    if mode == "m12":
        def col(s, x0, x1, y0, y1):
            return [sh.shape_id for sh in s.shapes
                    if x0 <= (sh.left + sh.width / 2) / 914400 <= x1 and y0 <= (sh.top + sh.height / 2) / 914400 <= y1
                    and not sh.name.startswith("Connector") and not (sh.width > Inches(2) and sh.height > Inches(1) and not (sh.has_text_frame and sh.text_frame.text.strip()))]
        cw3 = (11.5 - 0.56) / 3
        s = S[1]
        timing(s, [col(s, 0.92 + k * (cw3 + 0.28) - 0.28, 0.92 + k * (cw3 + 0.28) + cw3, 2.5, 5.4) for k in (1, 2)])
        mark_notes(s, ["Ela percebe um aperto", "Mais tarde, pensa"])
        s = S[6]
        timing(s, [col(s, 0.92 + k * (cw3 + 0.28), 0.92 + k * (cw3 + 0.28) + cw3, 2.5, 5.8) for k in (1, 2)])
        mark_notes(s, ["Reconhecer essa vontade não significa", "Em outro momento, ela já consegue"])
    prs.save(out); print("ok", out)
