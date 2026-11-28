import sys
from docx import Document
from docx.shared import Cm, Pt
from docx.oxml.ns import qn
f=sys.argv[1]; d=Document(f)
for s in d.sections:
    s.top_margin=s.bottom_margin=Cm(1.2); s.left_margin=s.right_margin=Cm(1.8)
for p in d.paragraphs:
    pf=p.paragraph_format; pf.space_after=Pt(2); pf.space_before=Pt(4 if p.style.name.startswith('Heading') else 0)
    for r in p.runs:
        if not p.style.name.startswith(('Heading','Title')): r.font.size=Pt(10)
W=[[1.5,1.6,11.6,2.7],[8,4.7,4.7]]
for t,w in zip(d.tables,W):
    t.autofit=False
    for e in t._tbl.tblPr.findall(qn('w:tblW')): e.set(qn('w:type'),'dxa'); e.set(qn('w:w'),str(int(sum(w)*567)))
    for gc,wd in zip(t._tbl.tblGrid.findall(qn('w:gridCol')),w): gc.set(qn('w:w'),str(int(wd*567)))
    for row in t.rows:
        for c,wd in zip(row.cells,w):
            c.width=Cm(wd)
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0)
                for r in p.runs: r.font.size=Pt(9.5)
d.save(f)
