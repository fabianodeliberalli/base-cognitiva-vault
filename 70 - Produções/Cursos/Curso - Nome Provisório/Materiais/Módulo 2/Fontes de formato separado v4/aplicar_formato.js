async ({presentation})=>{
 const fs=await import('node:fs/promises'),z=await import('node:zlib');const R='/workspace/scratch/4909a93c8194/formato_gravacao_20261124';const key=TASK_KEY;
 const spec=JSON.parse(await fs.readFile(R+'/'+key+'_formato.json','utf8'));
 await fs.mkdir(R+'/antes',{recursive:true});await fs.mkdir(R+'/nativo',{recursive:true});
 await fs.writeFile(R+'/antes/'+key+'.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
 if(key==='M22'||key==='M23'){
  const old=JSON.parse(await fs.readFile('/workspace/scratch/4909a93c8194/reorganizacao_gravacoes_20261124/'+key+'_v3.json','utf8'));
  if(presentation.slides.items.length!==old.slides.length||presentation.slides.items.some((s,i)=>s.speakerNotes.text!==old.slides[i].notes))throw Error('A fonte mudou.');
  const imported=presentation.importSlides(JSON.parse(await fs.readFile(R+'/fontes/mapa_dois_tempos.json','utf8')));
  presentation.slides.getItem(presentation.slides.items.length-1).moveTo(key==='M22'?0:1);
 }else if(presentation.slides.items.length!==spec.slides.length)throw Error('Quantidade divergente.');
 for(let i=0;i<spec.slides.length;i++){
  const s=presentation.slides.getItem(i),d=spec.slides[i];s.speakerNotes.text='';
  const h=s.shapes.items.find(x=>x.name==='headline');if(h){h.text=d.title;h.text.typeface='EB Garamond';h.text.fontSize=48;}
  const f=s.shapes.items.find(x=>x.name==='footer'||x.name==='lesson-footer');if(f)f.text=(key==='M22'?'M2.2 · Prática':key==='M23'?'M2.3 · Prática':key==='M24P1'?'M2.4 · Parte 1':'M2.4 · Prática')+' · '+(i+1)+' / '+spec.slides.length;
 }
 if(key==='M24P1'){const s=presentation.slides.getItem(7);s.shapes.items.find(x=>x.name==='next').text='Retorno\nAlívio agora, sobrecarga depois';s.shapes.items.find(x=>x.name==='return').text='Próximo encontro\nJá esperam minha disponibilidade';}
 const data=spec.slides.map((d,i)=>({...d,nativeSlideId:presentation.slides.getItem(i).id,screenActual:presentation.slides.getItem(i).shapes.items.filter(x=>String(x.text)).map(x=>({name:x.name,text:String(x.text),position:x.position}))}));
 await fs.writeFile(R+'/nativo/'+key+'.json',JSON.stringify({...spec,slides:data},null,2));await fs.writeFile(R+'/nativo/'+key+'.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
 return{slides:presentation.slides.items.length,notesEmpty:presentation.slides.items.every(s=>s.speakerNotes.text===''),retomada:key==='M22'?1:key==='M23'?2:'Mapas no percurso teórico'};
}
