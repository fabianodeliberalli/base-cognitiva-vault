async ({presentation}) => {
 const fs=await import('node:fs/promises');const z=await import('node:zlib');
 const root='/workspace/scratch/4909a93c8194/m23_producao_20261124';
 const spec=JSON.parse(await fs.readFile(root+'/m23_v2.json','utf8'));
 if(presentation.slides.items.length!==14)throw Error('A fonte mudou: esperadas 14 telas da prática v1.');
 const old=[...presentation.slides.items];
 const demoRecords=presentation.slides.addCopy(old[12].copy());demoRecords.moveTo(2);
 const demoQuestion=presentation.slides.addCopy(old[8].copy());demoQuestion.moveTo(3);
 const realCheck=presentation.slides.addCopy(old[5].copy());realCheck.moveTo(15);
 const get=(s,n)=>{const x=s.shapes.items.filter(x=>x.name===n);if(x.length!==1)throw Error(n+': '+x.length);return x[0]};
 const text=(s,n,t)=>{get(s,n).text=t};
 const add=(s,n,t,pos,size=30,color='#082A45')=>{const x=s.shapes.add({name:n,geometry:'textbox',position:pos,fill:'none',line:{style:'solid',fill:'none',width:0}});x.text=t;x.text.style={fontSize:size,typeface:'Inter',color,wrap:'square',autoFit:'none',insets:0};return x};
 const expected=[old[0],old[1],demoRecords,demoQuestion,...old.slice(2,13),realCheck,old[13]];
 if(expected.some((s,i)=>s.id!==presentation.slides.getItem(i).id))throw Error('Ordem de composição divergente.');
 for(let i=0;i<spec.slides.length;i++){
  const s=presentation.slides.getItem(i),d=spec.slides[i];
  s.speakerNotes.text=d.notes;
  if(i){text(s,'headline',d.title);text(s,'lesson-footer',`M2.3 · Prática · ${i+1} / ${spec.slides.length}`);}
  for(const [n,t] of Object.entries(d.screen))text(s,n,t);
 }
 // Duas demonstrações distintas, encerradas antes da escolha pessoal.
 add(demoRecords,'demo-context','Proposta de trabalho: “Precisamos conversar melhor sobre isso.”',{left:80,top:246,width:1120,height:54},27);
 text(demoRecords,'forma-vivida','Vivido');text(demoRecords,'elaboracao','Conclusão');
 text(demoRecords,'forma-exemplo','Aperto\nVontade de guardar a proposta');
 text(demoRecords,'elaboracao-exemplo','Minha proposta\nfoi rejeitada');
 for(const n of ['forma-exemplo','elaboracao-exemplo'])get(demoRecords,n).text.fontSize=30;
 text(demoRecords,'reforco','O vivido é reconhecido. A conclusão pede bases no encontro.');get(demoRecords,'reforco').text.fontSize=26;
 text(demoQuestion,'closed','Por que você rejeitou\nminha proposta?');
 text(demoQuestion,'closed-role','A rejeição já entra como fato.');
 text(demoQuestion,'open','Sobre quais pontos\nda proposta você\nquer conversar?');
 text(demoQuestion,'open-role','A resposta pode alterar a leitura.');
 text(demoQuestion,'action','Depois deste exemplo, começamos a sua situação.');
 for(const n of ['closed','open'])get(demoQuestion,n).text.fontSize=32;
 for(const n of ['closed-role','open-role'])get(demoQuestion,n).text.fontSize=23;
 get(demoQuestion,'action').text.fontSize=27;
 // As quatro referências são produzidas antes de cada comparação.
 const conclusionAfter=presentation.slides.getItem(11);
 text(conclusionAfter,'leitura-label','CONCLUSÃO ANTES');text(conclusionAfter,'vivido-label','CONCLUSÃO DEPOIS');
 get(conclusionAfter,'leitura-label').text.fontSize=20;get(conclusionAfter,'vivido-label').text.fontSize=20;
 const livedAfter=presentation.slides.getItem(12);
 text(livedAfter,'leitura-label','VIVIDO ANTES');text(livedAfter,'vivido-label','VIVIDO DEPOIS');
 get(livedAfter,'leitura-label').text.fontSize=20;get(livedAfter,'vivido-label').text.fontSize=20;
 text(presentation.slides.getItem(10),'closed','O que estou\nconcluindo');get(presentation.slides.getItem(10),'closed').text.fontSize=36;
 text(presentation.slides.getItem(9),'outras-referencias','Respiração\ncomo acontece');
 // Conferência real em continuidade, com a mesma gramática dos registros da aula.
 text(realCheck,'row-title-0','Pergunta que vou levar');
 text(realCheck,'row-body-0','Fonte e ocasião\npara conferir');
 text(realCheck,'row-title-1','Retorno ao registro');
 text(realCheck,'row-body-1','O que soube, o que supus\ne como vivi o encontro');
 for(const n of ['row-title-0','row-title-1'])get(realCheck,n).text.fontSize=32;
 for(const n of ['row-body-0','row-body-1'])get(realCheck,n).text.fontSize=30;
 text(realCheck,'conserve-bases','Resposta real e interpretação ficam reconhecíveis.');get(realCheck,'conserve-bases').text.fontSize=26;
 const cart=presentation.slides.getItem(16);
 text(cart,'record-body-1','Vivido antes e vivido depois');
 text(cart,'record-body-2','Conclusão atual, bases e questões abertas');
 text(cart,'record-body-3','Pergunta, fonte e ocasião de retorno');
 for(let i=0;i<4;i++)get(cart,'record-body-'+i).text.fontSize=26;
 // Preservar marca, onda autoral, relações e cores. Corrigir fontes de títulos.
 for(const s of presentation.slides.items){
  for(const x of s.shapes.items){
   if(!String(x.text))continue;
   x.text.typeface=['headline','cover-title'].includes(x.name)?'EB Garamond':'Inter';
   if(['headline','cover-title'].includes(x.name)){x.text.bold=true;x.text.fontSize=x.name==='cover-title'?64:51;}
  }
 }
 const saved={...spec,slides:spec.slides.map((d,i)=>({...d,nativeSlideId:presentation.slides.getItem(i).id,screenActual:presentation.slides.getItem(i).shapes.items.filter(x=>String(x.text)).map(x=>({name:x.name,text:String(x.text),position:x.position}))}))};
 await fs.writeFile(root+'/m23_v2_aplicado.json',JSON.stringify(saved,null,2));
 await fs.writeFile(root+'/snapshots/m23_pratica_v2.json.gz',z.gzipSync(JSON.stringify(presentation.toProto())));
 return {slides:presentation.slides.items.length,notesMatch:presentation.slides.items.every((s,i)=>s.speakerNotes.text===spec.slides[i].notes)};
}
