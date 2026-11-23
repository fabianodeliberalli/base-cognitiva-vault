async({presentation})=>{
 const fs=await import('node:fs/promises'),z=await import('node:zlib');
 const root='/workspace/scratch/4909a93c8194/profundidade_tsh_20261123';
 const part=__PART__;
 const spec=JSON.parse(await fs.readFile(root+'/parte'+part+'_v2.json','utf8'));
 if(part===1){
  const source=[...presentation.slides.items];if(source.length!==19)throw Error('Expected source v1 of 19 slides');
  const set=(s,n,t,size=30,color='#082A45',font='Inter',pos)=>{const sh=s.shapes.items.find(x=>x.name===n);if(!sh)throw Error('Missing '+n);sh.text=t;sh.text.style={fontSize:size,color,typeface:font,wrap:'square',autoFit:'none',insets:0};if(pos)sh.position=pos;return sh;};
  for(const s of spec.slides){
   const sl=presentation.slides.addCopy(source[s.previous_index].copy());sl.speakerNotes.text=s.notes;
   const dark=[0,6,9,13,16,18].includes(s.previous_index);
   if(s.number>1){set(sl,'headline',s.title,48,dark?'#F4EFEA':'#082A45','EB Garamond');set(sl,'lesson-footer','M2.4 · Parte 1 · '+s.number+' / '+spec.slides.length,15,dark?'#F4EFEA':'#245E78','Inter',{left:72,top:673,width:460,height:22});}
   if(s.number===8){
    const sh=set(sl,'configuration',s.edits.configuration,33,'#F4EFEA');sh.text.style={fontSize:33,typeface:'Inter',color:'#F4EFEA',alignment:'center',verticalAlignment:'middle',wrap:'square',autoFit:'none',insets:0};
    for(let i=0;i<4;i++){const sh=set(sl,'dimension-'+i,s.edits['dimension-'+i],27,'#245E78');sh.text.style={fontSize:27,typeface:'Inter',color:'#245E78',alignment:'center',verticalAlignment:'middle',wrap:'square',autoFit:'none',insets:0};}
    const sh2=set(sl,'not-identity',s.edits['not-identity'],23,'#245E78','Inter',{left:95,top:604,width:1090,height:40});sh2.text.style={fontSize:23,typeface:'Inter',color:'#245E78',alignment:'center',wrap:'square',autoFit:'none',insets:0};
   }
   if(s.number===9){
    set(sl,'reading-label',s.edits['reading-label'],22,'#245E78');set(sl,'lived-label',s.edits['lived-label'],22,'#245E78');set(sl,'reading',s.edits.reading,42);set(sl,'lived',s.edits.lived,42);
    const t=set(sl,'investigation',s.edits.investigation,31,'#245E78');t.text.style={fontSize:31,typeface:'Inter',color:'#245E78',alignment:'center',wrap:'square',autoFit:'none',insets:0};
   }
   if(s.number===10){set(sl,'both',s.edits.both,36);const x=set(sl,'learn',s.edits.learn,25,'#245E78');x.text.style={fontSize:25,typeface:'Inter',color:'#245E78',alignment:'center',wrap:'square',autoFit:'none',insets:0};}
  }
  presentation.slides.delete(source.map((_,i)=>i));
 }else{
  if(presentation.slides.items.length!==18)throw Error('Expected 18 practice slides');
  for(let i=0;i<spec.slides.length;i++)presentation.slides.getItem(i).speakerNotes.text=spec.slides[i].notes;
 }
 // A versão final usa a face Bold de EB Garamond nos títulos, preservando Inter no corpo.
 for(const slide of presentation.slides.items){for(const shape of slide.shapes.items){if(['headline','cover-title'].includes(shape.name))shape.text.bold=true;}}
 await fs.writeFile('/tmp/depth_m24_p'+part+'_after.json.gz',z.gzipSync(Buffer.from(JSON.stringify(presentation.toProto()))));
 await fs.writeFile('/tmp/depth_m24_p'+part+'_final.json',JSON.stringify(presentation.slides.items.map((s,i)=>({number:i+1,notes:s.speakerNotes.text.toString(),screen_text:s.shapes.items.filter(x=>x.text?.toString()).map(x=>({name:x.name,text:x.text.toString()}))})),null,2));
 return {part,count:presentation.slides.items.length};
}
