async ({presentation}) => {
 const fs=await import('node:fs/promises');
 const part=__PART__;
 const root='/workspace/scratch/4909a93c8194/m24_revisao';
 const specs=JSON.parse(await fs.readFile(root+'/parte'+part+'_v1.json','utf8')).slides;
 const originalStyles=JSON.parse(await fs.readFile(root+'/fontes/source_styles.json','utf8'));
 const source=[...presentation.slides.items];
 if(source.length!==29)throw Error('Expected 29 imported source slides');
 const C={navy:'#082A45',petrol:'#173F52',blue:'#245E78',copper:'#C99A64',beige:'#F4EFEA'};
 const dark=[0,6,9,13,16,20,26,28];
 const shape=(s,n)=>{const a=s.shapes.items.find(x=>x.name===n);if(!a)throw Error('Missing '+n);return a;};
 const set=(s,n,t,style={},p)=>{const a=shape(s,n);a.text=t;a.text.style={fontSize:30,typeface:'Inter',color:C.navy,wrap:'square',autoFit:'none',insets:0,...style};if(p)a.position=p;return a;};
 const add=(s,n,t,p,style={})=>{const a=s.shapes.add({name:n,geometry:'textbox',position:p,fill:'none',line:{fill:'none',width:0}});a.text=t;a.text.style={fontSize:23,typeface:'Inter',color:C.blue,wrap:'square',autoFit:'none',insets:0,...style};return a;};
 const made=[];
 for(const spec of specs){
  const s=presentation.slides.addCopy(source[spec.sourceIndex].copy());
  const isDark=dark.includes(spec.sourceIndex),base=isDark?C.beige:C.navy;
  const styles=originalStyles[spec.sourceIndex];
  for(const a of s.shapes.items){
   const text=a.text?.toString();if(!text)continue;
   const orig=styles[a.name]||{};
   const title=['headline','cover-title'].includes(a.name);
   a.text.style={typeface:title?'EB Garamond':'Inter',fontSize:title?48:orig.fontSize||28,color:orig.color||base,alignment:orig.alignment||'left',verticalAlignment:['basic','middle','occasion-a','occasion-b','recognize','return','resource','rehearse','involve','reflect','start','other-support','expectation','form','participation','effects','configuration','first-signal'].includes(a.name)?'middle':'top',wrap:'square',autoFit:'none',insets:0};
  }
  for(const [n,t] of Object.entries(spec.edits)){
   const orig=styles[n]||{};
   set(s,n,t,{color:orig.color||base,fontSize:Math.min(orig.fontSize||30,32),alignment:orig.alignment||'left',verticalAlignment:['occasion-a','occasion-b','involve','reflect','resource','start','other-support'].includes(n)?'middle':'top'});
  }
  if(part===1&&spec.number===6){set(s,'thinkable','“Tenho receio de perder\nmeu lugar se eu negociar.”',{fontSize:34,color:C.navy});}
  s.speakerNotes.text=spec.notes;
  if(spec.number===1){
   set(s,'cover-label','M2.4 · PARTE '+part+'\n'+(part===1?'COMPREENSÃO E FUNDAMENTOS':'PRÁTICA GUIADA E INTEGRAÇÃO'),{fontSize:22,color:C.beige});
   set(s,'cover-title',part===1?'O que mantém a repetição\nde uma resposta?':'Experimentar outra sustentação\npara responder',{fontSize:60,color:C.beige,typeface:'EB Garamond'},{left:72,top:235,width:840,height:220});
   set(s,'presenter','Fabiano Deliberalli',{fontSize:25,color:C.beige});
   set(s,'official-subtitle','Da compreensão acumulada\nà presença que sustenta',{fontSize:18,color:C.beige});
  }else{
   set(s,'headline',spec.title,{fontSize:48,typeface:'EB Garamond',color:base});
   set(s,'lesson-footer','M2.4 · Parte '+part+' · '+spec.number+' / '+specs.length,{fontSize:15,color:isDark?C.beige:C.blue},{left:72,top:673,width:460,height:22});
  }
  if(part===2&&spec.number===3){set(s,'stakes',spec.edits.stakes,{fontSize:32,color:C.navy});}
  if(part===2&&spec.number===4){set(s,'first-signal',spec.edits['first-signal'],{fontSize:32,color:C.beige,alignment:'center',verticalAlignment:'middle'});set(s,'signals',spec.edits.signals,{fontSize:29,color:C.navy});}
  if(part===2&&spec.number===5){
   set(s,'agenda-meaning',spec.edits['agenda-meaning'],{fontSize:32,color:C.navy});
   set(s,'answer',spec.edits.answer,{fontSize:39,typeface:'EB Garamond',color:C.navy});
   set(s,'relief',spec.edits.relief,{fontSize:28,color:C.blue});
   set(s,'cost',spec.edits.cost,{fontSize:27,color:C.blue});
  }
  if(part===2&&[12,13].includes(spec.number)){
   for(const n of ['occasion-a','occasion-b'])set(s,n,spec.edits[n],{fontSize:28,color:C.beige,alignment:'center',verticalAlignment:'middle'});
   for(const n of ['a-context','b-context'])set(s,n,spec.edits[n],{fontSize:31,color:C.navy});
  }
  if(part===2&&spec.number>=3&&spec.number<=13){
   const cues={3:'PAUSE PARA ESCOLHER E REGISTRAR',4:'PAUSE PARA PERCEBER E REGISTRAR',5:'PAUSE PARA REGISTRAR',6:'PAUSE PARA RETORNAR',7:'PAUSE PARA ESCOLHER O RECURSO',8:'PAUSE PARA ACOMPANHAR O RECURSO',9:'PAUSE PARA ACOMPANHAR E REGISTRAR',10:'PAUSE PARA REGISTRAR',11:'PAUSE PARA RETORNAR',12:'PAUSE PARA COMPARAR O VIVIDO',13:'PAUSE PARA COMPARAR A PARTICIPAÇÃO'};
   add(s,'cue-pause',cues[spec.number],{left:72,top:221,width:1020,height:32},{fontSize:20,color:isDark?C.copper:C.blue,bold:true});
  }
  if(part===2&&spec.number===18){add(s,'bridge-next','M2.5 · Acontecimento, experiência e interpretação',{left:80,top:625,width:1110,height:32},{fontSize:22});}
  made.push({number:spec.number,title:spec.title,id:s.id});
 }
 presentation.slides.delete(Array.from({length:source.length},(_,i)=>i));
 const z=await import('node:zlib');
 await fs.writeFile('/tmp/m24_parte'+part+'_snapshot.json.gz',z.gzipSync(Buffer.from(JSON.stringify(presentation.toProto()))));
 await fs.writeFile('/tmp/m24_parte'+part+'_notas.json',JSON.stringify(presentation.slides.items.map((s,i)=>({number:i+1,notes:s.speakerNotes.text.toString()}))));
 return {count:presentation.slides.items.length,slides:made};
}
