#!/usr/bin/env python3
"""Rebuild the edited M2.2 Part 1 from the preserved original and two PNG assets.
Requires FFmpeg/ffprobe, Inter-Regular.ttf and the exact input specified by the EDL.
All intervals refer to the ORIGINAL recording, in seconds; no time stretching.
"""
from pathlib import Path
import argparse, json, subprocess, hashlib

INTERVALS = [(2.00,320.72),(344.64,460.84),(482.96,759.88),
             (772.64,1102.80),(1119.40,1565.20),(1572.48,1773.60)]
LI_START, LI_END = 1553.04, 1580.36

def make_command(source, li_image, end_image, output, font, progress):
    cmd=['ffmpeg','-hide_banner','-y','-filter_complex_threads','2']
    for start,end in INTERVALS:
        cmd += ['-threads','1','-ss',f'{start:.2f}','-t',f'{end-start:.2f}','-i',str(source)]
    cmd += ['-i',str(li_image),'-loop','1','-framerate','25','-t','4','-i',str(end_image)]
    filters=['[6:v]split=2[li4][li5]']
    for i,(start,end) in enumerate(INTERVALS):
        duration=end-start
        filters += [f'[{i}:v]trim=duration={duration:.2f},setpts=PTS-STARTPTS,split=2[m{i}][c{i}]',
                    f'[m{i}]crop=2880:1620:0:90,scale=1920:1080:flags=lanczos,setsar=1[b{i}]',
                    f'[c{i}]crop=448:252:2432:0,scale=300:168:flags=lanczos,setsar=1[cam{i}]']
        base=f'b{i}'
        if i in (4,5):
            on=max(0,LI_START-start); off=min(duration,LI_END-start)
            filters.append(f'[{base}][li{i}]overlay=0:0:eof_action=repeat:enable=\'between(t,{on:.2f},{off:.2f})\'[g{i}]')
            base=f'g{i}'
        filters.append(f'[{base}][cam{i}]overlay=1620:0:eof_action=repeat[vpre{i}]')
        suffix=''
        if i == 0:
            # Cover label ends at the original slide change, 43.32 seconds.
            suffix=f",drawtext=fontfile='{font}':text='PARTE 1  COMPREENSÃO E FUNDAMENTOS':fontsize=28:fontcolor=0xF4EFEA:x=108:y=137:enable='lt(t,41.32)'"
        if i == len(INTERVALS)-1:
            suffix += f',fade=t=out:st={duration-0.16:.2f}:d=0.16'
        filters.append(f'[vpre{i}]fps=25,format=yuv420p{suffix}[v{i}]')
        # The 8 ms microfades avoid clicks; the final fade follows the completed last word.
        fadeout=0.12 if i == len(INTERVALS)-1 else 0.008
        filters.append(f'[{i}:a]atrim=start=0:end={duration:.2f},asetpts=PTS-STARTPTS,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,afade=t=in:st=0:d=0.008,afade=t=out:st={duration-fadeout:.3f}:d={fadeout}[a{i}]')
    filters += ['[7:v]trim=duration=4,setpts=PTS-STARTPTS,setsar=1,fps=25,format=yuv420p,fade=t=in:st=0:d=0.16[v6]',
                'anullsrc=r=48000:cl=stereo,atrim=duration=4,asetpts=PTS-STARTPTS[a6]']
    filters.append(''.join(f'[v{i}][a{i}]' for i in range(7))+'concat=n=7:v=1:a=1[video][rawaudio]')
    filters.append('[rawaudio]asetpts=N/SR/TB,volume=1.9dB,alimiter=limit=0.841395:level=false:latency=true[audio]')
    graph=';\n'.join(filters)
    output.parent.mkdir(parents=True,exist_ok=True)
    graph_path=output.parent/'filtros_m22.txt'
    graph_path.write_text(graph)
    cmd += ['-filter_complex_script',str(graph_path),'-map','[video]','-map','[audio]',
            '-c:v','libx264','-preset','veryfast','-crf','18','-threads','4','-pix_fmt','yuv420p','-r','25',
            '-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',
            '-c:a','aac','-b:a','160k','-ar','48000','-ac','2',
            '-movflags','+faststart','-metadata','title=M2.2 | Parte 1 | Compreensão e fundamentos',
            '-metadata','artist=Fabiano Deliberalli | Traduzindo o Ser Humano',
            '-progress',str(progress),'-nostats',str(output)]
    return cmd

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--li-image',type=Path,required=True)
    ap.add_argument('--end-image',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--font',default='/home/agent/.local/share/fonts/tsh-trilha/Inter-Regular.ttf')
    args=ap.parse_args()
    cmd=make_command(args.source,args.li_image,args.end_image,args.output,args.font,args.output.with_suffix('.progress'))
    print(json.dumps({'main_duration':sum(e-s for s,e in INTERVALS),'total_duration':sum(e-s for s,e in INTERVALS)+4,'intervals':INTERVALS},indent=2),flush=True)
    subprocess.run(cmd,check=True)
    result={'sha256':hashlib.file_digest(args.output.open('rb'),'sha256').hexdigest(),
            'size_bytes':args.output.stat().st_size,
            'probe':json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(args.output)]))}
    args.output.with_suffix('.probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='probe'}),flush=True)
if __name__=='__main__': main()
