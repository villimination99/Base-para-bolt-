/* CONTRASTE DEL TEXTO SOBRE UN FONDO QUE SE MUEVE.
   ------------------------------------------------------------------
   Ninguna otra bateria puede con esto. axe lee colores computados: sobre un
   lienzo WebGL no hay color computado que leer, asi que da el hero por bueno
   sin mirarlo. Y la bateria de degradados compara contra los dos extremos de
   un degradado CSS, que aqui tampoco existe.

   Un fondo animado no tiene UN contraste: tiene un peor caso a lo largo del
   tiempo. Asi que se fotografia la pagina compuesta en diez fotogramas, se
   muestrea la caja de cada texto y se guarda el pixel MAS CLARO -- el peor
   para texto claro. Se mide a 900 y a 390 px, porque el shader se reencuadra
   con la proporcion de pantalla y no da lo mismo.

   COMO SE ESCONDE LA TINTA, QUE ES DONDE ME EQUIVOQUE DOS VECES:
     1. La primera version leia el lienzo con gl.readPixels. Devuelve negro
        en cuanto el fotograma se ha compuesto, salvo con preserveDrawingBuffer.
        Daba 21:1 en todo y el MISMO resultado en los dos fondos, que es la
        senal de que no estaba midiendo nada.
     2. La segunda escondia .hero-shader-hint entera con visibility:hidden...
        y con ella su disco oscuro de fondo. Medi el shader desnudo y me
        salio que el arreglo habia empeorado las cosas.
   Se esconden los HIJOS del contenido y el <svg> de la flecha; los fondos de
   los contenedores se quedan, porque son parte de lo que ve el visitante.

   Lo que encontro el dia que empezo a funcionar: la flecha de bajar del
   marco pulsante, que lleva publicada desde siempre, estaba a 1,40:1 en un
   movil. Cian sobre el neon cian del propio marco. No es poco contraste: es
   no verse.

   Uso:  node verificadores/hero/comprobar.mjs                              */
import { chromium } from 'playwright';
import http from 'http'; import fs from 'fs'; import path from 'path';
import { e, prepararFuente, contextoDeSeccion } from '../liquid.mjs';
const T=process.env.TEMA || path.resolve(path.dirname(new URL(import.meta.url).pathname),'../../theme');
const TMP=fs.mkdtempSync('/tmp/med-');
fs.mkdirSync(path.join(TMP,'assets'),{recursive:true});
for(const a of fs.readdirSync(path.join(T,'assets'))) fs.copyFileSync(path.join(T,'assets',a),path.join(TMP,'assets',a));
const src=fs.readFileSync(path.join(T,'sections/hero-shader.liquid'),'utf8');
const {ctx}=contextoDeSeccion('hero-shader',src); e.options.globals=ctx;
for (const modo of ['marco','remolino']) {
  ctx.section.settings.fondo=modo;
  let html=(await e.parseAndRender(prepararFuente(src),ctx)).replace(/\/\/cdn\/([\w.-]+)/g,'/assets/$1');
  fs.writeFileSync(path.join(TMP,modo+'.html'),
    `<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="/assets/villumination.css"><style>body{margin:0;background:#0A0A0A}</style></head><body>${html}
<script src="/assets/base.js" defer></script></body></html>`);
}
const TIPO={'.html':'text/html','.js':'text/javascript','.css':'text/css'};
const srv=http.createServer((rq,rs)=>{const f=path.join(TMP,decodeURIComponent(rq.url.split('?')[0]));
  if(!fs.existsSync(f)){rs.writeHead(404);return rs.end();}
  rs.writeHead(200,{'Content-Type':TIPO[path.extname(f)]||'application/octet-stream'});rs.end(fs.readFileSync(f));});
await new Promise(r=>srv.listen(0,r));
const base='http://127.0.0.1:'+srv.address().port+'/';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
let fallos=0;
const lum=([r,g,bb])=>{const f=x=>{x/=255;return x<=.03928?x/12.92:Math.pow((x+.055)/1.055,2.4)};
  return .2126*f(r)+.7152*f(g)+.0722*f(bb);};
const ratio=(a,c)=>{const L1=lum(a),L2=lum(c);return (Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);};

for (const modo of ['marco','remolino']) {
  for (const vp of [[900,620],[390,780]]) {
    const p=await b.newPage({viewport:{width:vp[0],height:vp[1]},deviceScaleFactor:1});
    await p.goto(base+modo+'.html',{waitUntil:'networkidle'});
    await p.waitForTimeout(1500);
    const objetivos=await p.evaluate(()=>{
      const out=[];
      for(const s of ['.section-eyebrow','.hero-title','.hero-subtitle','.hero-shader-hint svg']){
        const el=document.querySelector('.hero-shader '+s); if(!el) continue;
        const r=el.getBoundingClientRect(), cs=getComputedStyle(el);
        const m=cs.color.match(/[\d.]+/g).map(Number);
        out.push({n:s, color:[m[0],m[1],m[2]], caja:{x:r.left,y:r.top,w:r.width,h:r.height}});}
      return out;});
    // el texto se esconde para fotografiar SOLO el fondo compuesto
    await p.addStyleTag({content:'.hero-shader-content *{visibility:hidden!important}.hero-shader-hint svg{visibility:hidden!important}'});
    const peor={};
    for (let f=0; f<10; f++) {
      await p.waitForTimeout(260);
      const b64=(await p.screenshot({type:'png'})).toString('base64');
      const muestras=await p.evaluate(async ({b64,objetivos})=>{
        const img=new Image(); img.src='data:image/png;base64,'+b64;
        await img.decode();
        const cv=document.createElement('canvas'); cv.width=img.width; cv.height=img.height;
        const g=cv.getContext('2d',{willReadFrequently:true}); g.drawImage(img,0,0);
        const res={};
        for(const o of objetivos){
          let pe=null;
          for(let i=0;i<=10;i++) for(let j=0;j<=2;j++){
            const x=Math.round(o.caja.x+o.caja.w*(i/10)), y=Math.round(o.caja.y+o.caja.h*(j/2));
            if(x<0||y<0||x>=cv.width||y>=cv.height) continue;
            const d=g.getImageData(x,y,1,1).data;
            const px=[d[0],d[1],d[2]];
            if(!pe||px[0]+px[1]+px[2]>pe[0]+pe[1]+pe[2]) pe=px;  // el mas CLARO es el peor caso
          }
          res[o.n]=pe;
        }
        return res;
      }, {b64,objetivos});
      for(const o of objetivos){
        const c=muestras[o.n]; if(!c) continue;
        const r=ratio(o.color,c);
        if(!peor[o.n]||r<peor[o.n].r) peor[o.n]={r,fondo:c};
      }
    }
    console.log(`\n--- ${modo}  ${vp[0]}x${vp[1]} ---`);
    for(const k in peor){
      /* 4,5:1 para texto (criterio 1.4.3). La flecha es un grafico no
         textual y le toca 3:1 (criterio 1.4.11). */
      const min = k.indexOf('svg') >= 0 ? 3.0 : 4.5;
      const ok = peor[k].r >= min;
      if(!ok) fallos++;
      console.log(`  ${ok?'OK   ':'FALLA'} ${k.padEnd(22)} ${peor[k].r.toFixed(2)}:1  (minimo ${min})  fondo mas claro rgb(${peor[k].fondo})`);
    }
    await p.close();
  }
}
await b.close(); srv.close(); fs.rmSync(TMP,{recursive:true,force:true});
console.log(fallos ? `\n  ${fallos} texto(s) por debajo del minimo sobre el fondo animado`
                   : '\nEl texto del hero se lee sobre los dos fondos, en el peor fotograma y en los dos anchos.');
process.exit(fallos ? 1 : 0);
