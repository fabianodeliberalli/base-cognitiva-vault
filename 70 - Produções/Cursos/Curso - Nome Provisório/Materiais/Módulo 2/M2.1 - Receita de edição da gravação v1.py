from pathlib import Path
import json, subprocess

root = Path(__file__).resolve().parent
source = root.parent / 'upload/M2.1.mp4'
out = root / 'entrega/TSH_M2_1_Aula_editada_v1.mp4'
out.parent.mkdir(parents=True, exist_ok=True)
still = root / 'video_qa/fechamento_16x9.png'
still.parent.mkdir(parents=True, exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-ss','2240','-i',str(source),'-frames:v','1','-vf','crop=2880:1620:0:90','-y',str(still)],check=True)

intervals = [(1.8,21.40),(39.12,177.72),(180.20,1646.76),(1782.88,1838.96),(1867.28,1873.24),(1879.52,2276.08)]
cuts = [
 {'start':0,'end':1.8,'reason':'Silêncio de abertura.'},
 {'start':21.4,'end':39.12,'reason':'Compartilhamento de tela e comentários operacionais.'},
 {'start':177.72,'end':180.20,'reason':'Comentário de preenchimento sobre a própria explicação.'},
 {'start':1646.76,'end':1782.88,'reason':'Antecipação repetida da prática, que incluía realização e conferência antes da condução por etapas. Escolha da questão e mapa visual permanecem antes da aproximação efetiva.'},
 {'start':1838.96,'end':1867.28,'reason':'Reexplicação conceitual durante a realização. Fundamento já desenvolvido preservado na parte conceitual.'},
 {'start':1873.24,'end':1879.52,'reason':'Recomeço e comentário sobre a condução antes da pergunta completa, que permanece.'},
 {'start':2276.08,'end':2276.12,'reason':'Cauda técnica após a despedida.'}
]
filters = [
 '[0:v]split=2[mainraw][camraw]',
 '[mainraw]crop=2880:1620:0:90[main]',
 '[camraw]crop=448:252:2432:0[cam]',
 '[1:v]format=yuv420p[still]',
 "[main][still]overlay=0:0:enable='between(t,2257.28,2270.40)':eof_action=repeat[fixed]",
 "[fixed][cam]overlay=2432:0:enable='between(t,21,2270.40)'[framed]",
 '[framed]split=6'+''.join(f'[vs{i}]' for i in range(6)),
 '[0:a]asplit=6'+''.join(f'[as{i}]' for i in range(6))
]
for i,(start,end) in enumerate(intervals):
 filters.append(f'[vs{i}]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}]')
 filters.append(f'[as{i}]atrim=start={start}:end={end},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.008,afade=t=out:st={end-start-0.008:.6f}:d=0.008[a{i}]')
filters.append(''.join(f'[v{i}][a{i}]' for i in range(6))+'concat=n=6:v=1:a=1[v][acat]')
filters.append('[acat]asetpts=N/SR/TB,volume=1.9dB,alimiter=limit=0.841395:level=false:latency=true[a]')
filter_path=root/'edicao_m21.ffscript'
filter_path.write_text(';\n'.join(filters)+'\n')
plan={'source':'M2.1.mp4','source_library_file_id':'libfile_fde3_f-ef41abcc15cc8191bcc22248f18e9e7c_ad925f8fadbc81918eab9ef0eafee9a9','source_duration':2276.12,'keep_intervals':intervals,'cuts':cuts,'expected_duration':sum(b-a for a,b in intervals),'video':{'width':2880,'height':1620,'fps':25,'crop':'Removidas barras horizontais; câmera preservada por reenquadramento separado, sem cortar o topo da imagem.','blackout_repair':{'start':2257.28,'end':2270.40,'method':'Último slide visível recomposto sob a câmera original em movimento.'}},'audio':'Voz original, nível ajustado e microfades de 8ms nos cortes; sem voz sintética ou mudança de velocidade.'}
(root/'Plano_de_edicao_M21.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
cmd=['ffmpeg','-hide_banner','-nostdin','-threads','4','-i',str(source),'-loop','1','-framerate','25','-i',str(still),'-filter_complex_threads','2','-filter_complex_script',str(filter_path),'-map','[v]','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','25','-threads','4','-c:a','aac','-b:a','160k','-ar','48000','-movflags','+faststart','-metadata','title=TSH M2.1 - Como se forma o que você percebe? - edição 1','-t',str(plan['expected_duration']),'-progress',str(root/'encode_progress.txt'),'-nostats','-y',str(out)]
with (root/'encode.log').open('w') as log:
 result=subprocess.run(cmd,stdout=log,stderr=log)
print(json.dumps({'exit_code':result.returncode,'path':str(out),'expected_duration':plan['expected_duration']},ensure_ascii=False),flush=True)
raise SystemExit(result.returncode)
