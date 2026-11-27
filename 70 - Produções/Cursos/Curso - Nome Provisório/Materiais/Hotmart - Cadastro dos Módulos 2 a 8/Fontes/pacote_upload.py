import os, re, shutil, sys, importlib.util
C="/home/claude/base-cognitiva-vault/70 - Produções/Cursos/Curso - Nome Provisório/Materiais/"
OUT=sys.argv[1]
spec=importlib.util.spec_from_file_location("dados", C+"Hotmart - Cadastro dos Módulos 2 a 8/Fontes/dados.py")
D=importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
P=C+"Percurso - Cultivo do Eixo e Caderno de Reencontros/"
GUIA=(P+"TSH - Cultivo do Eixo - guia da prática diária.pdf","TSH-Cultivo-do-Eixo-guia.pdf")
CAD=(P+"TSH - Caderno de Reencontros.pdf","TSH-Caderno-de-Reencontros.pdf")
CAL=(P+"TSH - Calendário da turma.pdf","TSH-Calendario-da-turma.pdf")
ZZ=(C+"Módulo 2/TSH_M2_Guia_Zhan_Zhuang_a_arvore.pdf","TSH-Guia-Zhan-Zhuang.pdf")
B="/home/claude/build_m2v/"
MAPA1=(B+"mapas/TSH-Mapas-do-Modulo-1.pdf","TSH-Mapas-do-Modulo-1.pdf")
MAPA9=(B+"mapas/TSH-Mapas-do-TSH-completo.pdf","TSH-Mapas-do-TSH.pdf")
def ap(m,cod): return (f"{B}apoios_m{m}/TSH_M{m}_{cod.replace('.','_')}_Apoio_do_aluno.pdf", f"TSH-Apoio-aula-{cod.replace('.','-')}.pdf")
IMG=C+"Hotmart - Cadastro dos Módulos 2 a 8/Imagens do percurso/"
def clean(t): return re.sub(r'\*\*','',t)
def w(path,txt):
    os.makedirs(os.path.dirname(path),exist_ok=True); open(path,'w',encoding='utf-8-sig').write(txt.strip().replace('\n','\r\n')+"\r\n")
def anexar(pasta,lst):
    for src,nome in lst:
        os.makedirs(f"{pasta}/anexos",exist_ok=True); shutil.copy(src,f"{pasta}/anexos/{nome}")
def aula(pasta,titulo,desc,video,lst=()):
    t=f"TÍTULO\n{titulo}\n\nDESCRIÇÃO\n{desc}\n\nVÍDEO\n{video}\n\nANEXOS\n"+("\n".join(n for _,n in lst) if lst else "nenhum")
    w(f"{pasta}/aula.txt",t); anexar(pasta,lst)
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
w(f"{OUT}/LEIA.txt", """TSH - materiais para a Hotmart (versão de 27/11/2026)

Uma pasta por módulo (M0 a M8). Dentro:
- modulo.txt: nome, descrição e data de liberação do módulo (copie e cole).
- capa.png: imagem do mapa do percurso com o módulo destacado.
- Uma pasta por aula, na ordem da plataforma (A01, A02...). Em cada uma, aula.txt traz título, descrição, o vídeo a subir e a lista de anexos; os anexos estão na pasta "anexos".

M0 e M1 já estão publicados: as pastas trazem só o que muda (alteracoes.txt diz o quê).\nM3: os textos podem mudar na revisão do módulo. Cadastre M3 só depois dela.
M4 a M8: textos prontos; vídeos e apoios serão produzidos ao longo do calendário.

Liberações: M2 em 29/11/2026; M3 em 13/12/2026; M4 em 10/01/2027; M5 em 24/01/2027; M6 em 14/02/2027; M7 em 28/02/2027; M8 em 14/03/2027.

Os nomes das pastas e arquivos são curtos e sem acentos para o Windows abrir sem erro. Os títulos completos, com acentos, estão dentro dos arquivos .txt.
""")
# M0
m0=f"{OUT}/M0"
w(f"{m0}/alteracoes.txt","""Módulo 0 (já publicado): duas aulas novas.

1. ATÉ 29/11: «Comece pelo corpo», depois da última aula do módulo. Pasta A-nova-Comece-pelo-corpo.
2. DEPOIS DE GRAVAR (sem pressa): «O percurso e a prática de todos os dias», logo depois da aula de boas-vindas (0.1). Pasta A-nova-depois-da-0-1-O-percurso.""")
aula(f"{m0}/A-nova-depois-da-0-1-O-percurso","O percurso e a prática de todos os dias",
 "Para onde o curso vai e o que você faz entre uma aula e outra: o Caminho da Semente, o mapa do percurso com as suas três direções, a auto-hipnose ao longo do caminho, o Cultivo do Eixo (praticado junto, um minuto), o Retorno ao Eixo e o Caderno de Reencontros. Em anexo, o guia do Cultivo do Eixo e o calendário da turma.",
 "Arquivo sugerido: TSH_M0_O_percurso_e_a_pratica.mp4\nOrigem: a gravar (slides e roteiro na pasta TSH-1-Gravar, 04-M0-aula-complementar), 6 a 8 min.\nPosição: logo depois da aula 0.1.",[GUIA,CAL])
aula(f"{m0}/A-nova-Comece-pelo-corpo","Comece pelo corpo: a postura da árvore",
 "Antes de seguir, uma prática curta para começar pelo corpo: a postura da árvore (Zhan Zhuang), com Wu Chi, a árvore e o fechamento com a respiração no baixo ventre. É a base do Cultivo do Eixo, a prática de três a cinco minutos que acompanha você todos os dias do curso. Em anexo, o guia do Cultivo do Eixo, o Caderno de Reencontros e o calendário da turma.",
 "Arquivo sugerido: TSH_M0_Comece_pelo_corpo.mp4\nOrigem: encontro de 28/11/2026, corte 2 (o mesmo vídeo de «O eixo no corpo: Zhan Zhuang» do Módulo 2), cerca de 10 min.",[GUIA,CAD,CAL])
# M1
m1=f"{OUT}/M1"
w(f"{m1}/alteracoes.txt",f"""Módulo 1 (já publicado): quatro alterações.

1. DESCRIÇÃO DO MÓDULO: acrescentar ao final
{D.MINIMO[1]}

2. AO FIM DA DESCRIÇÃO DE CADA AULA (1.1 a 1.7): acrescentar
Antes desta aula, três minutos de Cultivo do Eixo: o vídeo está no Módulo 0 (Comece pelo corpo). A prática desta aula é guiada no vídeo «Módulo 1 em prática guiada»; o apoio de uma página está em anexo. Escrever é opcional.

3. ANEXOS NOVOS: em cada aula 1.1 a 1.7, o apoio de uma página correspondente (pasta apoios-por-aula). Na aula 1.1, também o guia do Cultivo do Eixo. Na aula 1.4, também «TSH-Mapas-do-Modulo-1.pdf» (os quatro mapas do módulo, com a pergunta e o uso de cada um).

4. AULA NOVA no fim do módulo: pasta A-nova-M1-pratica-guiada.
""")
for k in range(1,8):
    s,n=ap(1,f"1.{k}"); os.makedirs(f"{m1}/apoios-por-aula",exist_ok=True); shutil.copy(s,f"{m1}/apoios-por-aula/{n}")
shutil.copy(GUIA[0],f"{m1}/apoios-por-aula/{GUIA[1]}"); shutil.copy(MAPA1[0],f"{m1}/apoios-por-aula/{MAPA1[1]}")
aula(f"{m1}/A-nova-M1-pratica-guiada","Módulo 1 em prática guiada",
 "O Módulo 1 inteiro em sete passos, um por aula, conduzidos do começo ao fim. Não precisa escrever nada: é só fazer junto. Se você tiver pouco tempo, este vídeo e o Cultivo do Eixo são o caminho mínimo do módulo. Em anexo, os sete apoios de uma página, para quem quiser rever depois.",
 "Arquivo sugerido: TSH_M1_Pratica_guiada.mp4\nOrigem: encontro de 28/11/2026, corte 0 (primeira hora), 10 a 12 min.",[ap(1,f"1.{k}") for k in range(1,8)]+[MAPA1])
# M2..M8
for m in range(2,9):
    md=D.MOD[m]; base=f"{OUT}/M{m}"
    desc=D.LINHA+"\nVocê está em: "+clean(md['pos'])+"\n\n"+"\n\n".join(md['desc'])+"\n\n"+D.MINIMO[m]
    w(f"{base}/modulo.txt",f"NOME DO MÓDULO\n{md['nome'].replace('—','-')}\n\nDESCRIÇÃO DO MÓDULO\n{desc}\n\nLIBERAÇÃO\n{md['lib']}. Encontro ao vivo do módulo: {md['enc']}.")
    shutil.copy(IMG+f"Mapa do percurso - Módulo {m}.png", f"{base}/capa.png")
    for i,a in enumerate(D.AULAS[m],1):
        cod,tit,descr=a[0],a[1],a[2]
        titulo = tit if m==2 else f"Aula {cod} - {tit}"
        tag={'abertura':'abertura','zhan':'zhan-zhuang'}.get(cod, cod.replace('.','-'))
        pasta=f"{base}/A{i:02d}-{tag}"
        lst=[]
        if m==2:
            vid=f"Arquivo sugerido: TSH_M2_A{i:02d}.mp4\nOrigem: {a[3]}."
            if cod=='zhan': lst=[ZZ,GUIA,CAD]
            elif re.fullmatch(r'2\.\d',cod): lst=[ap(2,cod)]
        elif m==3:
            vid=f"Arquivo sugerido: TSH_M3_{cod.replace('.','_')}.mp4\nOrigem: a gravar depois da revisão do Módulo 3 (rascunho na pasta TSH-1-Gravar, 03-M3)."; lst=[ap(3,cod)]
        else:
            vid=f"Arquivo sugerido: TSH_M{cod.replace('.','_')}.mp4\nOrigem: a produzir no calendário do módulo."
            if cod=='5.1': lst=[MAPA9]
        aula(pasta,titulo,descr,vid,lst)
print('ok')
