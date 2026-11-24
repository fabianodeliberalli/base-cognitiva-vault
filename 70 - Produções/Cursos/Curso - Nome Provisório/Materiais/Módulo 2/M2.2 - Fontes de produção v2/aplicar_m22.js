async ({presentation}) => {
  const fs=await import('node:fs/promises');
  const z=await import('node:zlib');
  const root='/workspace/scratch/4909a93c8194/producao_20261124';
  const spec=JSON.parse(await fs.readFile(root+'/m22_v2.json','utf8'));
  if(presentation.slides.items.length!==10)throw new Error('A fonte mudou: esperadas 10 telas da prática v1.');
  await fs.mkdir(root+'/snapshots',{recursive:true});
  await fs.writeFile(root+'/snapshots/m22_pratica_antes.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
  const old=[...presentation.slides.items];
  const demo=presentation.slides.addCopy(old[5].copy());
  demo.moveTo(1);
  const action=presentation.slides.addCopy(old[9].copy());
  action.moveTo(10);
  const get=(s,name)=>{const x=s.shapes.items.filter(x=>x.name===name);if(x.length!==1)throw new Error('Forma '+name+': '+x.length);return x[0]};
  const txt=(s,name,t)=>{get(s,name).text=t};
  const add=(s,name,t,position,fontSize=30,color='#082A45')=>{const x=s.shapes.add({name,geometry:'textbox',position,fill:'none',line:{style:'solid',fill:'none',width:0}});x.text=t;x.text.style={fontSize,typeface:'Inter',color,wrap:'square',autoFit:'none',insets:0};return x};
  for(let i=0;i<spec.slides.length;i++){
    const s=presentation.slides.getItem(i),d=spec.slides[i];
    s.speakerNotes.text=d.notes;
    if(i){txt(s,'headline',d.title);txt(s,'footer',`M2.2 · Prática · ${i+1} / ${spec.slides.length}`);}
    for(const [n,t] of Object.entries(d.screen))txt(s,n,t);
  }
  // A demonstração usa a mesma comparação visual que o aluno encontrará depois.
  txt(demo,'first','Antes das perguntas');txt(demo,'questions','Resolver');txt(demo,'return','Possibilidade');
  const names=['first','questions','return'];
  const values=['Vontade de ir\nGesto de recolhimento','Horário disponível\nTensão ao se expor','Prazer de se mover\nReceio de exposição'];
  for(let i=0;i<3;i++){
    const h=get(demo,names[i]);h.position={left:80+395*i,top:263,width:330,height:77};h.text.fontSize=27;
    add(demo,'demo-observation-'+i,values[i],{left:82+395*i,top:367,width:320,height:139},29);
  }
  txt(demo,'after-comparison','Uma mesma situação. Outras diferenças à vista.');
  get(demo,'after-comparison').position={left:78,top:541,width:1110,height:65};get(demo,'after-comparison').text.fontSize=29;
  txt(demo,'pause-cue','Demonstração antes da sua exploração.');
  get(demo,'pause-cue').position={left:78,top:611,width:1100,height:30};get(demo,'pause-cue').text.fontSize=20;
  // O campo constante nas telas de realização representa a mesma situação.
  txt(presentation.slides.getItem(4),'record-label','Registro: Resolver');
  txt(presentation.slides.getItem(5),'record-label','Registro: Possibilidade');
  // Na elaboração, recuperar o artesão já apresentado na teoria, em vez de outra metáfora.
  const elab=presentation.slides.getItem(9);
  for(const n of ['demand-area','possibility-area','demand','demand-question','possibility','possibility-question','action'])get(elab,n).delete();
  elab.images.add({path:'library-file:fde1_bGliZmlsZV81Z3ZRTW9nRkNaRWN3b1ZPNW1aS2JR_FileDrive_ad925f8fadbc81918eab9ef0eafee9a9',fit:'cover',position:{left:72,top:265,width:566,height:352},alt:'Artesão modelando uma peça de cerâmica, imagem recuperada da teoria M2.2.'});
  add(elab,'form-expression','Uma forma que\npermite reconhecer',{left:691,top:277,width:515,height:120},38,'#245E78');
  add(elab,'form-return','O retorno ao vivido\npermite conferir\ne continuar.',{left:691,top:443,width:510,height:150},33);
  // A continuidade é um uso da Cartografia existente, sem criar mais uma ficha.
  for(const n of ['record-title-3','record-body-3','record-line-2'])get(action,n).delete();
  const labs=['Ação','Ocasião','Retorno'];
  const bodies=['O que vou experimentar?','Quando e em qual situação?','O que a experiência mostrou?'];
  for(let i=0;i<3;i++){
    txt(action,'record-title-'+i,labs[i]);txt(action,'record-body-'+i,bodies[i]);
    get(action,'record-title-'+i).position={left:124,top:286+i*101,width:300,height:55};
    get(action,'record-body-'+i).position={left:495,top:286+i*101,width:662,height:72};
    get(action,'record-title-'+i).text.fontSize=33;get(action,'record-body-'+i).text.fontSize=30;
    if(i<2)get(action,'record-line-'+i).position={left:124,top:371+i*101,width:1035,height:1};
  }
  // Quatro campos legítimos, com as três observações dentro de Manifestação.
  const cart=presentation.slides.getItem(11);
  txt(cart,'record-body-1','Três observações e diferenças percebidas');
  txt(cart,'record-body-3','Ação, ocasião e retorno da experiência');
  for(let i=0;i<4;i++)get(cart,'record-body-'+i).text.fontSize=26;
  // Fontes reais, títulos Garamond e corpo Inter, preservando as figuras da fonte.
  for(const s of presentation.slides.items){
    for(const x of s.shapes.items){
      if(!String(x.text))continue;
      x.text.typeface=['headline','cover-title'].includes(x.name)?'EB Garamond':'Inter';
      if(['headline','cover-title'].includes(x.name)){x.text.bold=true;if(x.name==='headline')x.text.fontSize=51;}
    }
  }
  spec.nativeSequencePending=true;
  spec.slides=spec.slides.map((d,i)=>({...d,nativeSlideId:presentation.slides.getItem(i).id,screenActual:presentation.slides.getItem(i).shapes.items.filter(x=>String(x.text)).map(x=>({name:x.name,text:String(x.text),position:x.position}))}));
  await fs.writeFile(root+'/m22_v2_aplicado.json',JSON.stringify(spec,null,2));
  await fs.writeFile(root+'/snapshots/m22_pratica_v2.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
  return {slides:presentation.slides.items.length,notesMatch:presentation.slides.items.every((s,i)=>s.speakerNotes.text===spec.slides[i].notes),snapshot:root+'/snapshots/m22_pratica_v2.json.gz'};
}
