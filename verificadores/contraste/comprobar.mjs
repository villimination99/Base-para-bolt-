/* Mide el contraste REAL de cada texto contra el fondo que de verdad tiene
   detras, subiendo por los padres hasta encontrar uno con color. Un tema
   oscuro con acentos de neon es justo donde esto se tuerce sin que se note.

   Uso:
     npm install playwright --no-save
     node verificadores/contraste/comprobar.mjs

   La pagina de prueba tiene que usar los nombres de clase REALES del tema. La
   primera version invente cuatro (.badge, .footer-bottom-text) que no existen,
   heredaron el color del body y dieron 1.04:1: cuatro fallos que no eran
   fallos. Antes de creerse un resultado malo, comprobar que la clase existe. */
import path from 'path'; import { fileURLToPath } from 'url';
const AQUI = path.dirname(fileURLToPath(import.meta.url));
import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport:{width:1280,height:900} });
await p.goto('file://' + AQUI + '/pagina.html');
await p.waitForTimeout(300);
const r = await p.evaluate(() => {
  const lum = c => { const m=c.match(/[\d.]+/g).map(Number); const f=x=>{x/=255;return x<=.03928?x/12.92:Math.pow((x+.055)/1.055,2.4)}; return .2126*f(m[0])+.7152*f(m[1])+.0722*f(m[2]); };
  const fondoDe = e => { let a=e; while(a && a!==document.documentElement){ const bg=getComputedStyle(a).backgroundColor;
      if(bg && !/rgba\(0, 0, 0, 0\)|transparent/.test(bg)) return bg; a=a.parentElement; } return 'rgb(0, 0, 0)'; };
  const out=[];
  for (const e of document.querySelectorAll('p,h3,span,a,s')) {
    const t=(e.textContent||'').trim(); if(!t || e.children.length) continue;
    const cs=getComputedStyle(e); const fg=cs.color, bg=fondoDe(e);
    const L1=lum(fg), L2=lum(bg);
    const ratio=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
    const px=parseFloat(cs.fontSize), grande = px>=24 || (px>=18.66 && parseInt(cs.fontWeight)>=700);
    const min = grande?3:4.5;
    out.push({ clase:(typeof e.className==='string'?e.className.split(' ')[0]:e.tagName)||e.tagName,
               txt:t.slice(0,26), r:+ratio.toFixed(2), min, px:Math.round(px), ok:ratio>=min });
  }
  return out;
});
const mal=r.filter(x=>!x.ok);
console.log(`elementos de texto medidos: ${r.length} | por debajo del minimo WCAG AA: ${mal.length}\n`);
mal.sort((a,b)=>a.r-b.r).forEach(x=>console.log(`  ${String(x.r).padStart(5)}:1  (min ${x.min})  ${x.px}px  .${x.clase.padEnd(22)} "${x.txt}"`));
if(!mal.length) console.log('  todos cumplen');
console.log('\nlos mas ajustados que SI cumplen:');
r.filter(x=>x.ok).sort((a,b)=>a.r-b.r).slice(0,4).forEach(x=>console.log(`  ${String(x.r).padStart(5)}:1  .${x.clase}`));
await b.close();
process.exit(mal.length ? 1 : 0);
