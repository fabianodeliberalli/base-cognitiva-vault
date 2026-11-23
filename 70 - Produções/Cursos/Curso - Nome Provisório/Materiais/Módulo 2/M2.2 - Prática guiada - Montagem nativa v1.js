async ({presentation})=>{
 const fs=await import('node:fs/promises');
 const templates=JSON.parse(await fs.readFile('/tmp/tsh-m22-slide-materials.json','utf8'));
 const Copy=presentation.slides.items[0].copy().constructor;
 const specs=[{"number":1,"title":"O que cada pergunta destaca?","sourceSlide":1,"notes":"Na primeira parte da aula, acompanhamos como algo ganha importância e encontra uma forma de expressão.\nAgora vamos observar como duas perguntas modificam o que ganha destaque numa mesma situação.\n\nVamos conservar uma observação inicial e um registro de cada pergunta para comparar depois.\nVocê pode usar palavras, desenho ou gesto.\nEscolha uma forma que consiga retomar ao longo da prática.\nOs registros podem permanecer só com você.\n\nFaça a prática num momento em que possa dedicar atenção a ela.\nSe estiver dirigindo, reserve para depois.\nVocê pode adaptar ou interromper a exploração quando precisar.\n\nNa próxima tela, começamos pela escolha da situação."},{"number":2,"title":"Escolha uma situação","sourceSlide":14,"notes":"Retome uma situação da aula anterior ou escolha uma que queira compreender agora.\nPode ser uma relação, uma criação ou algo que deseja desenvolver.\nEscolha algo que consiga acompanhar neste momento.\n\nSitue brevemente o que está acontecendo.\nGuarde essa situação como referência para toda a prática.\n\nPause o vídeo agora e retome quando tiver feito sua escolha.\n\nPAUSA"},{"number":3,"title":"Como essa situação aparece agora?","sourceSlide":14,"notes":"Traga a situação escolhida à atenção.\nComo ela se apresenta agora?\nPerceba o que acontece em você ao olhar para ela.\n\nEncontre uma expressão breve para o que reconheceu.\nGuarde como sua observação de antes das perguntas.\n\nPause o vídeo agora para fazer esse primeiro registro.\nRetome quando terminar.\n\nPAUSA"},{"number":4,"title":"Primeira pergunta","sourceSlide":15,"notes":"Mantenha a mesma situação em mente.\nAgora pergunte: o que eu preciso resolver aqui?\nObserve o que essa pergunta coloca em primeiro plano.\n\nRegistre brevemente essa observação como “Resolver”.\n\nPause o vídeo agora e retome quando terminar esse registro.\n\nPAUSA"},{"number":5,"title":"Segunda pergunta","sourceSlide":15,"notes":"Volte à mesma situação com esta outra pergunta.\nQue possibilidade de vida procura expressão aqui?\nAcompanhe o que aparece.\n\nRegistre essa observação como “Possibilidade”.\n\nPause o vídeo agora e retome quando terminar esse registro.\n\nPAUSA"},{"number":6,"title":"O que cada aproximação mostrou?","sourceSlide":17,"notes":"Retome os três registros: antes das perguntas, Resolver e Possibilidade.\nO que ganhou destaque em cada aproximação?\n\nCompare o que mudou e o que permaneceu.\nOs registros podem mostrar diferenças ou apontar para algo que continuou igual.\n\nPause o vídeo para conferir essas observações.\nRetome quando terminar a comparação.\n\nPAUSA"},{"number":7,"title":"O que mais precisa ser considerado?","sourceSlide":16,"notes":"Agora deixe os registros de lado por um momento.\nVolte à situação concreta que escolheu.\n\nHá algo importante que ainda não foi considerado?\nDê espaço ao que aparece, sem precisar forçar uma resposta.\nSe houver um acréscimo, conserve junto dos registros.\n\nPause o vídeo para fazer essa última conferência.\nRetome quando estiver pronto para concluir.\n\nPAUSA"},{"number":8,"title":"Concluir a prática","sourceSlide":14,"notes":"Vamos concluir a prática.\nDeixe a situação de lado.\nReconheça o ambiente em que está agora.\nPerceba o apoio do corpo e retome seus movimentos.\n\nPAUSA\n\nA prática termina aqui.\nAgora vamos elaborar o que foi possível reconhecer."},{"number":9,"title":"O que a experiência permite compreender?","sourceSlide":18,"notes":"A pergunta sobre resolver pode ter evidenciado um compromisso, um limite ou uma condição que precisa mudar.\nA pergunta sobre uma possibilidade de vida pode ter dado espaço a um desejo ou mostrado a importância de uma solução prática.\nAs duas perguntas podem revelar diferenças ou apontar para a mesma necessidade.\n\nUma cobrança de trabalho pode envolver um compromisso real e a necessidade de negociar um limite.\nUma vontade de dançar pode pedir espaço para experimentar e condições que ajudem a participar.\n\nO que ganhou importância depende da situação e também da maneira como nos aproximamos dela.\nNa linguagem dos dois tempos da Tradução, o que apareceu encontrou uma forma, foi elaborado e pôde ser conferido de novo na experiência.\nÉ essa participação que estamos investigando.\n\nEsse reconhecimento faz parte do caminho de integrar e expressar possibilidades da Essência na vida concreta."},{"number":10,"title":"A Cartografia conserva o percurso","sourceSlide":19,"notes":"Aproveite esses registros na Cartografia que já estamos construindo.\n\nNa Situação, conserve o que escolheu investigar e seu contexto.\nNa Manifestação, guarde a primeira observação e as diferenças que reconheceu durante a prática.\nNa Tradução provisória, registre o que compreendeu e o que ainda permanece em aberto.\nNa Orientação possível, escolha uma condição ou um próximo passo que permita continuar.\n\nPode ser buscar uma informação, conversar, negociar um limite ou desenvolver uma capacidade.\nA continuidade depende do que sua experiência pede.\n\nNa próxima aula, vamos investigar como uma leitura se torna certeza e como recuperar outras pistas para conferi-la."}];
 const set=(s,n,t,size=36,font='Inter',color='#082A45',pos)=>{const z=s.shapes.items.find(x=>x.name===n);if(!z)throw Error('Missing '+n);z.text=t;z.text.style={fontSize:size,typeface:font,color,wrap:'square',autoFit:'none',insets:0};if(pos)z.position=pos;return z;};
 const add=(s,n,t,pos,size=28,font='Inter',color='#245E78')=>{const z=s.shapes.add({name:n,geometry:'textbox',position:pos,fill:'none',line:{fill:'none',width:0}});z.text=t;z.text.style={fontSize:size,typeface:font,color,wrap:'square',autoFit:'none',insets:0};return z;};
 const del=(s,n)=>{const z=s.shapes.items.find(x=>x.name===n);if(z)z.delete();};
 const made=[];
 for(const spec of specs){
   const m=structuredClone(templates.find(x=>x.sourceIndex===spec.sourceSlide-1).material);
   const images=new Map(m.images.map(x=>[x.proto.id,x]));
   for(const x of images.values())if(x.proto.data && !(x.proto.data instanceof Uint8Array))x.proto.data=new Uint8Array(Object.values(x.proto.data));
   const charts=new Map(m.charts.map(x=>[x.id,x]));
   const provider={getImageById:id=>{const x=images.get(id);return x?{toProto:()=>x.proto,localSourcePath:x.localSourcePath}:undefined},getChartById:id=>charts.has(id)?{toProto:()=>charts.get(id)}:undefined};
   const s=presentation.slides.addCopy(new Copy(provider,m.slide,m.composeRuns));
   s.size={width:1280,height:720};
   s.speakerNotes.text=spec.notes;
   if(spec.number===1){
      set(s,'cover-label','M2.2 · PARTE 2\nPRÁTICA GUIADA',22,'Inter','#F4EFEA');
      set(s,'cover-title','O que cada pergunta\ndestaca?',64,'EB Garamond','#F4EFEA',{left:72,top:240,width:825,height:205});
      set(s,'presenter','Fabiano Deliberalli',23,'Inter','#F4EFEA',{left:72,top:618,width:760,height:42});
      add(s,'practice-path','Observar · Mudar a pergunta · Conferir',{left:72,top:501,width:830,height:80},27,'Inter','#F4EFEA');
   }else{
      set(s,'headline',spec.title,48,'EB Garamond');
      set(s,'footer','M2.2 · Prática · '+spec.number+' / 10',15,'Inter','#245E78',{left:72,top:673,width:440,height:22});
   }
   if(spec.number===2){
      set(s,'receive','Qual situação você\nquer compreender?',39,'EB Garamond');
      set(s,'receive-support','Mantenha a mesma situação\nao longo da prática.',27);
   }
   if(spec.number===3){
      set(s,'receive','Perceba e encontre\numa expressão breve.',39,'EB Garamond');
      set(s,'receive-support','Guarde como sua observação\nde antes das perguntas.',27);
   }
   if(spec.number===4||spec.number===5){
      const first=spec.number===4;
      del(s,first?'focus-second':'focus-first');
      del(s,'between-questions');del(s,'question-two');
      set(s,'question-one',first?'O que eu preciso\nresolver aqui?':'Que possibilidade de vida\nprocura expressão aqui?',first?46:42,'EB Garamond','#082A45',{left:662,top:285,width:535,height:165});
      add(s,'record-label',first?'Registro: Resolver':'Registro: Possibilidade',{left:662,top:489,width:520,height:55},27);
   }
   if(spec.number===6){
      for(const z of [...s.shapes.items])if(z.name==='')z.delete();
      const labels=[['first','Antes das perguntas'],['questions','Resolver'],['return','Possibilidade']];
      for(const [n,t] of labels){const z=set(s,n,t,28,'Inter');z.fill='#DEE9EB';}
      set(s,'after-comparison','O que mudou?\nO que permaneceu?',42,'EB Garamond');
      del(s,'continuity');
   }
   if(spec.number===7){
      set(s,'reopen','Há algo importante\nque ainda não foi\nconsiderado?',38,'EB Garamond','#082A45',{left:662,top:275,width:535,height:180});
      set(s,'return-to-whole','Volte à situação concreta.',27,'Inter','#245E78',{left:662,top:490,width:535,height:65});
   }
   if(spec.number===8){
      for(const n of ['practice-field','first-outline','receive','receive-support'])del(s,n);
      add(s,'set-aside','Deixe a situação de lado.',{left:100,top:278,width:1050,height:70},31);
      add(s,'room','Reconheça o ambiente.',{left:100,top:371,width:1080,height:90},54,'EB Garamond','#082A45');
      add(s,'movement','Retome seus movimentos.',{left:100,top:490,width:1080,height:70},31);
   }
   if(spec.number===9){
      set(s,'demand','Uma demanda que chega',32,'EB Garamond','#082A45');
      set(s,'demand-question','Compromisso e limite\nO que precisa ser negociado?',29,'Inter','#082A45');
      set(s,'possibility','Uma possibilidade\nque procura espaço',32,'EB Garamond','#F4EFEA');
      set(s,'possibility-question','Desejo e proteção\nO que precisa ser desenvolvido?',29,'Inter','#F4EFEA');
      set(s,'action','A continuidade depende do que a experiência pede.',27);
   }
   if(spec.number===10){
      set(s,'record-body-0','Situação escolhida e contexto',25);
      set(s,'record-body-1','Primeira observação e diferenças percebidas',25);
      set(s,'record-body-2','Compreensão e perguntas que permanecem',25);
      set(s,'record-body-3','Uma condição ou um próximo passo',25);
      for(let j=0;j<4;j++)set(s,'record-title-'+j,['Situação','Manifestação','Tradução provisória','Orientação possível'][j],29,'EB Garamond','#245E78');
   }
   if(spec.number>=2&&spec.number<=7)add(s,'pause-cue',spec.number===2?'Pause o vídeo para escolher.':'Pause o vídeo para perceber e registrar.',{left:662,top:588,width:535,height:43},21);
   made.push(s);
 }
 presentation.slides.delete([0]);
 for(let i=0;i<presentation.slides.items.length;i++){const s=presentation.slides.getItem(i);for(const n of i===0?['course-signature','official-subtitle']:['course']){const z=s.shapes.items.find(x=>x.name===n);if(z)z.text.style={typeface:'Inter'};}}
 for(const [i,t] of [[2,'Pause o vídeo para o primeiro registro.'],[5,'Pause o vídeo para comparar.'],[6,'Pause o vídeo para conferir.']])presentation.slides.getItem(i).shapes.items.find(x=>x.name==='pause-cue').text=t;
 return {slides:presentation.slides.items.length,notes:presentation.slides.items.map(s=>s.speakerNotes.text),refs:presentation.getPreviewImageReferences({kind:'slides',slideIds:made.slice(0,2).map(s=>s.id)}).filter(x=>x.startsWith('library-file:'))};
}
