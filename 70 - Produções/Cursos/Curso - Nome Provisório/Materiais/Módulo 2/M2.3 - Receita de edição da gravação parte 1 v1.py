#!/usr/bin/env python3
"""Reproduce M2.3 Part 1 from the preserved original and the end-card PNG."""
from pathlib import Path
import subprocess,json,hashlib,argparse
CUTS=[(364.52,385.52),(433.48,446.72),(503.28,507.52),(559.16,566.12),(818.40,819.76),(820.52,822.40)]
START,END=20.72,1560.48
INTERVALS=[];cursor=START
for a,b in CUTS:INTERVALS.append((cursor,a));cursor=b
INTERVALS.append((cursor,END))
CAPTIONS=[(690.0,712.0,'Informações favoráveis ao que já acredito ganham mais passagem.'),
          (1149.0,1164.0,'São formas de reduzir a dissonância.\nCada caminho pode ampliar a compreensão ou preservar a certeza.'),
          (1220.0,1250.0,'A absorção também participa da criação, da música e da contemplação.\nNesta aula, investigamos a fixação em uma leitura.')]

def build(source,endcard,output,font):
 cmd=['ffmpeg','-hide_banner','-y','-filter_complex_threads','2']
 for a,b in INTERVALS:cmd+=['-threads','1','-ss',f'{a:.2f}','-t',f'{b-a:.2f}','-i',str(source)]
 n=len(INTERVALS);cmd+=['-loop','1','-framerate','25','-t','4','-i',str(endcard)]
 filters=[]
 output.parent.mkdir(exist_ok=True,parents=True)
 for i,(a,b) in enumerate(INTERVALS):
  d=b-a
  filters += [f'[{i}:v]trim=duration={d:.2f},setpts=PTS-STARTPTS,split=2[m{i}][c{i}]',f'[m{i}]crop=2880:1620:0:90,scale=1920:1080:flags=lanczos,setsar=1[base{i}]',f'[c{i}]crop=448:252:2432:0,scale=300:168:flags=lanczos,setsar=1[cam{i}]',f'[base{i}][cam{i}]overlay=1620:0:eof_action=repeat[framed{i}]']
  suffix=''
  if i==0:suffix+=f",drawtext=fontfile='{font}':text='PARTE 1  COMPREENSÃO E FUNDAMENTOS':fontsize=28:fontcolor=0xF4EFEA:x=108:y=137:enable='lt(t,{57.0-a:.2f})'"
  for k,(on,off,text) in enumerate(CAPTIONS):
   if off<=a or on>=b:continue
   s=max(0,on-a);e=min(d,off-a)
   txt=output.parent/f'apoio_conceitual_{k}.txt';txt.write_text(text)
   suffix+=f",drawbox=x=108:y=924:w=1510:h=83:color=0x082A45@1:t=fill:enable='between(t,{s:.2f},{e:.2f})',drawtext=fontfile='{font}':textfile='{txt}':fontsize=26:fontcolor=0xF4EFEA:x=128:y=934:line_spacing=8:enable='between(t,{s:.2f},{e:.2f})'"
  if i==n-1:suffix+=f',fade=t=out:st={d-0.16:.2f}:d=0.16'
  filters.append(f'[framed{i}]fps=25,format=yuv420p{suffix}[v{i}]')
  fade=0.12 if i==n-1 else 0.008
  filters.append(f'[{i}:a]atrim=start=0:end={d:.2f},asetpts=PTS-STARTPTS,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,afade=t=in:st=0:d=0.008,afade=t=out:st={d-fade:.3f}:d={fade}[a{i}]')
 filters += [f'[{n}:v]trim=duration=4,setpts=PTS-STARTPTS,setsar=1,fps=25,format=yuv420p,fade=t=in:st=0:d=0.16[v{n}]',f'anullsrc=r=48000:cl=stereo,atrim=duration=4,asetpts=PTS-STARTPTS[a{n}]']
 filters.append(''.join(f'[v{i}][a{i}]' for i in range(n+1))+f'concat=n={n+1}:v=1:a=1[video][rawaudio]')
 filters.append('[rawaudio]asetpts=N/SR/TB,volume=2.0dB,alimiter=limit=0.841395:level=false:latency=true[audio]')
 graph=output.parent/'filtros_m23.txt';graph.write_text(';\n'.join(filters))
 cmd+=['-filter_complex_script',str(graph),'-map','[video]','-map','[audio]','-c:v','libx264','-preset','veryfast','-crf','18','-threads','4','-pix_fmt','yuv420p','-r','25','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','160k','-ar','48000','-ac','2','-movflags','+faststart','-metadata','title=M2.3 | Parte 1 | Compreensão e fundamentos','-metadata','artist=Fabiano Deliberalli | Traduzindo o Ser Humano','-progress',str(output.with_suffix('.progress')),'-nostats',str(output)]
 return cmd

def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--endcard',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--font',default='/home/agent/.local/share/fonts/tsh-trilha/Inter-Regular.ttf');a=p.parse_args()
 print(json.dumps({'intervals':INTERVALS,'duration':sum(y-x for x,y in INTERVALS)+4}),flush=True)
 subprocess.run(build(a.source,a.endcard,a.output,a.font),check=True)
 out={'sha256':hashlib.file_digest(a.output.open('rb'),'sha256').hexdigest(),'size_bytes':a.output.stat().st_size,'probe':json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(a.output)]))}
 a.output.with_suffix('.probe.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='probe'}),flush=True)
if __name__=='__main__':main()
