async ({presentation}) => {
 const fs=await import('node:fs/promises'),z=await import('node:zlib');
 const R='/workspace/scratch/4909a93c8194/reorganizacao_gravacoes_20261124';
 const key=TASK_KEY;
 const spec=JSON.parse(await fs.readFile(R+'/'+key+'_v3.json','utf8'));
 const before=JSON.parse(await fs.readFile(R+'/antes/'+key+'.json','utf8'));
 if(presentation.slides.items.length!==before.length)throw Error('A apresentação de origem mudou.');
 if(presentation.slides.items.some((s,i)=>s.speakerNotes.text!==before[i].notes))throw Error('Notas de origem alteradas; conferir antes de aplicar.');
 const keep=spec.slides.map(s=>s.sourceIndex);
 presentation.slides.delete(before.map((_,i)=>i).filter(i=>!keep.includes(i)).sort((a,b)=>b-a));
 if(presentation.slides.items.some((s,i)=>s.id!==before[keep[i]].id))throw Error('Ordem divergente.');
 const shape=(s,n)=>{const a=s.shapes.items.filter(x=>x.name===n);if(a.length!==1)throw Error(n+': '+a.length);return a[0]};
 for(let i=0;i<spec.slides.length;i++){
  const s=presentation.slides.getItem(i),d=spec.slides[i];s.speakerNotes.text=d.notes;
  const heading=s.shapes.items.find(x=>x.name==='headline');if(heading)heading.text=d.title;
  for(const [name,t]of Object.entries(d.screenChanges))shape(s,name).text=t;
  const footer=s.shapes.items.find(x=>x.name==='footer'||x.name==='lesson-footer');
  if(footer)footer.text=(key==='M22'?'M2.2 · Prática':key==='M23'?'M2.3 · Prática':'M2.4 · Parte 2')+' · '+(i+1)+' / '+spec.slides.length;
 }
 if(key==='M22'){
  shape(presentation.slides.getItem(0),'demo-observation-0').text.fontSize=29;
  const context=presentation.slides.getItem(0).shapes.add({name:'demo-context',geometry:'textbox',position:{left:80,top:233,width:920,height:30},fill:'none',line:{style:'solid',fill:'none',width:0}});context.text='Exemplo: um convite para dançar';context.text.style={fontSize:22,typeface:'Inter',color:'#245E78',wrap:'square',autoFit:'none',insets:0};
  shape(presentation.slides.getItem(5),'after-comparison').text='O que ganhou destaque?\nComo foi vivido?';
  shape(presentation.slides.getItem(5),'pause-cue').position={left:105,top:592,width:1080,height:42};
  shape(presentation.slides.getItem(5),'pause-cue').text.fontSize=24;
 }
 if(key==='M23'){
  const s=presentation.slides.getItem(1);
  const x=s.shapes.add({name:'demo-lived-conclusion',geometry:'textbox',position:{left:80,top:244,width:1120,height:50},fill:'none',line:{style:'solid',fill:'none',width:0}});
  x.text='Aperto e vontade de se retirar: vivido. Rejeição: conclusão.';
  x.text.style={fontSize:25,typeface:'Inter',color:'#245E78',wrap:'square',autoFit:'none',insets:0};
 }
 if(key==='M24P2')shape(presentation.slides.getItem(5),'resource-0').text.fontSize=28;
 await fs.mkdir(R+'/depois',{recursive:true});
 const data=spec.slides.map((d,i)=>({...d,nativeSlideId:presentation.slides.getItem(i).id,screenActual:presentation.slides.getItem(i).shapes.items.filter(x=>String(x.text)).map(x=>({name:x.name,text:String(x.text),position:x.position}))}));
 await fs.writeFile(R+'/depois/'+key+'.json',JSON.stringify({...spec,slides:data},null,2));
 await fs.writeFile(R+'/depois/'+key+'.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
 return {slides:presentation.slides.items.length,notesMatch:presentation.slides.items.every((s,i)=>s.speakerNotes.text===spec.slides[i].notes)};
}
