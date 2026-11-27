import os, re, shutil, sys, importlib.util, unicodedata
C="/home/claude/base-cognitiva-vault/70 - Produções/Cursos/Curso - Nome Provisório/Materiais/"
OUT=sys.argv[1]
spec=importlib.util.spec_from_file_location("dados", C+"Hotmart - Cadastro dos Módulos 2 a 8/Fontes/dados.py")
D=importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
P=C+"Percurso - Cultivo do Eixo e Caderno de Reencontros/"
GUIA=P+"TSH - Cultivo do Eixo - guia da prática diária.pdf"; CAD=P+"TSH - Caderno de Reencontros.pdf"; CAL=P+"TSH - Calendário da turma.pdf"
ZZ=C+"Módulo 2/TSH_M2_Guia_Zhan_Zhuang_a_arvore.pdf"
AP2=C+"Módulo 2/Apoios do aluno - uma página/"
AP3="/home/claude/build_m2v/apoios_m3/"
IMG=C+"Hotmart - Cadastro dos Módulos 2 a 8/Imagens do percurso/"
def clean(t): return re.sub(r'\*\*','',t)
def safe(t): return re.sub(r'[\\/*"<>|]','-',t.replace(':',' -').replace('?','')).strip()
def slug(t):
    t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+','_',t).strip('_')
def w(path,txt):
    os.makedirs(os.path.dirname(path),exist_ok=True); open(path,'w',encoding='utf-8').write(txt.strip()+"\n")
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
# ---- LEIA
w(f"{OUT}/00 - LEIA - como cadastrar.txt", """TSH - materiais organizados para a Hotmart (26/11/2026)

Cada pasta de módulo tem:
- 00 - Módulo: o nome do módulo (nome.txt), a descrição (descricao.txt) e a imagem do mapa do percurso (capa).
- Uma pasta por aula, na ordem da plataforma: título (titulo.txt), descrição (descricao.txt), o vídeo a subir (VIDEO.txt diz o nome do arquivo e de onde ele vem) e os anexos (pasta "anexos", quando houver).

Para cadastrar: copie o texto de cada .txt para o campo correspondente, suba o vídeo indicado e os anexos.

Módulo 0 e Módulo 1 já estão publicados: as pastas trazem só o que muda.
Módulos 4 a 8: textos prontos; vídeos e apoios do aluno serão produzidos ao longo do calendário.

Datas de liberação (calendário quinzenal): M2 em 29/11/2026; M3 em 13/12/2026; M4 em 10/01/2027; M5 em 24/01/2027; M6 em 14/02/2027; M7 em 28/02/2027; M8 em 14/03/2027.

A imagem de capa está em PNG. Confira na Hotmart a medida pedida para a capa do módulo; se for diferente, a imagem pode ir no corpo da primeira aula.

Arquivos antigos que este pacote substitui (pode descartar): "TSH - Hotmart - Cadastro dos Módulos 2 a 8.zip" (26/11, manhã), "TSH_Cadastro_Hotmart_Copiar_Colar.txt", "TSH_Texto_Hotmart_Programa_54_Aulas_Ampliado.txt" e "TSH_Programacao_Hotmart.xlsx".
""")
# ---- M0
m0=f"{OUT}/Módulo 0 - alterações (já publicado)/01 - Nova aula - Comece pelo corpo"
w(f"{m0}/titulo.txt","Comece pelo corpo: a postura da árvore")
w(f"{m0}/descricao.txt","Antes de seguir, uma prática curta para começar pelo corpo: a postura da árvore (Zhan Zhuang), com Wu Chi, a árvore e o fechamento com a respiração no baixo ventre. É a base do Cultivo do Eixo, a prática de três a cinco minutos que acompanha você todos os dias do curso. Em anexo, o guia do Cultivo do Eixo, o Caderno de Reencontros e o calendário da turma.")
w(f"{m0}/VIDEO.txt","Arquivo sugerido: TSH_M0_Comece_pelo_corpo.mp4\nOrigem: encontro de 28/11/2026, corte 2 (o mesmo vídeo de 'O eixo no corpo: Zhan Zhuang' do Módulo 2), cerca de 10 min.\nPosição: depois da última aula do Módulo 0.")
for f in (GUIA,CAD,CAL): shutil.copy(f, f"{m0}/anexos/") if os.path.isdir(f"{m0}/anexos") else (os.makedirs(f"{m0}/anexos"), shutil.copy(f, f"{m0}/anexos/"))
# ---- M1
m1=f"{OUT}/Módulo 1 - alterações (já publicado)"
w(f"{m1}/acrescentar ao fim da descrição de cada aula.txt","Antes desta aula, três minutos de Cultivo do Eixo: o vídeo está no Módulo 0 (Comece pelo corpo) e o guia está em anexo na aula 1.1.")
os.makedirs(f"{m1}/Aula 1.1 - anexo novo",exist_ok=True); shutil.copy(GUIA,f"{m1}/Aula 1.1 - anexo novo/")
# ---- M2..M8
for m in range(2,9):
    md=D.MOD[m]; base=f"{OUT}/Módulo {m} - {safe(md['nome'].split('—',1)[1].strip())}"
    w(f"{base}/00 - Módulo/nome.txt", md['nome'].replace('—','-'))
    desc=D.LINHA+"\nVocê está em: "+clean(md['pos'])+"\n\n"+"\n\n".join(md['desc'])
    w(f"{base}/00 - Módulo/descricao.txt",desc)
    w(f"{base}/00 - Módulo/liberacao.txt", f"Liberação: {md['lib']}. Encontro ao vivo do módulo: {md['enc']}.")
    shutil.copy(IMG+f"Mapa do percurso - Módulo {m}.png", f"{base}/00 - Módulo/capa - Mapa do percurso - Módulo {m}.png")
    for i,a in enumerate(D.AULAS[m],1):
        cod,tit=a[0],a[1]; descr=a[2]
        titulo = tit if m==2 else f"Aula {cod} - {tit}"
        pasta=f"{base}/{i:02d} - {safe(titulo)}"
        w(f"{pasta}/titulo.txt",titulo); w(f"{pasta}/descricao.txt",descr)
        anexos=[]
        if m==2:
            origem=a[3]; arq='TSH_M2_'+slug(titulo.replace('Aula ',''))+'.mp4'
            w(f"{pasta}/VIDEO.txt",f"Arquivo sugerido: {arq}\nOrigem: {origem}.")
            if cod=='zhan': anexos=[ZZ,GUIA,CAD]
            elif re.fullmatch(r'2\.\d',cod): anexos=[AP2+f"TSH_M2_{cod.replace('.','_')}_Apoio_do_aluno.pdf"]
        else:
            arq=f"TSH_M{cod.replace('.','_')}_"+slug(tit)+'.mp4'
            w(f"{pasta}/VIDEO.txt",f"Arquivo sugerido: {arq}\nOrigem: a gravar (slides e guia de gravação na pasta de produção)." if m==3 else f"Arquivo sugerido: {arq}\nOrigem: a produzir no calendário do módulo.")
            if m==3: anexos=[AP3+f"TSH_M3_{cod.replace('.','_')}_Apoio_do_aluno.pdf"]
        for f in anexos:
            os.makedirs(f"{pasta}/anexos",exist_ok=True); shutil.copy(f,f"{pasta}/anexos/")
print('ok')
