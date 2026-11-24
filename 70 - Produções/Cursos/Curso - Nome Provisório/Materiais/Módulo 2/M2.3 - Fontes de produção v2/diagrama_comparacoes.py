from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz
R=Path(__file__).resolve().parent
F=R.parent/'producao_20261124/fonts'
for name,file in [('Inter','Inter-Regular.ttf'),('Inter-Bold','Inter-Bold.ttf'),('EB','EBGaramond-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(F/file)))
p=R/'comparacoes_v2.pdf';c=canvas.Canvas(str(p),pagesize=(1280,720))
c.setFillColorRGB(244/255,239/255,234/255);c.rect(0,0,1280,720,fill=1,stroke=0)
def txt(x,y,t,font,size,color):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,t)
navy='#082A45';blue='#245E78';copper='#C99A64'
txt(62,666,'TRADUZINDO O SER HUMANO','Inter-Bold',14,blue)
txt(62,584,'Duas comparações, a mesma situação','EB',49,navy)
c.setStrokeColor(copper);c.setLineWidth(4);c.line(62,553,145,553)
for x,w,col,title in [(62,554,'#173F52','CONCLUSÃO'),(662,554,copper,'VIVIDO')]:
 c.setFillColor(col);c.rect(x,450,w,60,fill=1,stroke=0)
 txt(x+22,470,title,'Inter-Bold',25,'#F4EFEA' if title=='CONCLUSÃO' else navy)
for x,bg,lines in [(62,'#DDE8EB',[('Conclusão antes','O que eu havia concluído'),('Conclusão depois','O que compreendo agora')]),(662,'#ECE2D6',[('Vivido antes','Como era viver a situação'),('Vivido depois','Como é vivê-la agora')])]:
 for idx,(label,body) in enumerate(lines):
  y=286-idx*148;c.setFillColor(bg);c.rect(x,y,554,126,fill=1,stroke=0)
  txt(x+22,y+80,label,'Inter-Bold',29,navy);txt(x+22,y+31,body,'Inter',27,navy)
txt(62,73,'Compare conclusão com conclusão; vivido com vivido.','Inter',28,blue)
c.save();d=fitz.open(p);d[0].get_pixmap().save(R/'comparacoes_v2.png')
print('Diagrama comparativo produzido com quatro referências explícitas.')
