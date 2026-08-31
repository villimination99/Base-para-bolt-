/* Genera la imagen que sale al pegar el enlace de la tienda en WhatsApp,
   Facebook, X, Discord, Slack o LinkedIn.
   ------------------------------------------------------------------
   1200x630 es la medida que piden todas esas plataformas. Sin ella, la
   tarjeta cae al logo, que es apaisado y estrecho: sale recortado o rodeado
   de relleno, y una tarjeta pobre baja el porcentaje de clics de un enlace
   compartido mucho mas de lo que parece.

   Usa el mismo lenguaje visual que la tienda (haces, marco de neon,
   tipografia Orbitron) para que quien la vea reconozca la marca.

   Uso:  node estudio/imagen/portada-social.mjs                             */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const SALIDA = path.join(AQUI, 'villumination-compartir.png');

const fuente = fs.readFileSync(path.join(RAIZ, 'estudio/video/fuente.b64'), 'utf8').trim();

const PAGINA = `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:1200px;height:630px;background:#05060a;overflow:hidden}
  body{font-family:Orbitron,"Arial Black",system-ui,sans-serif;color:#fff}
  #fondo{position:absolute;inset:0}
  .capa{position:absolute;inset:0;display:flex;flex-direction:column;
        align-items:center;justify-content:center;gap:18px;padding:0 90px;text-align:center}
  .marca{font-weight:900;font-size:26px;letter-spacing:.5em;
    background:linear-gradient(100deg,#00f0ff,#8b5cf6 45%,#ff2ecb);
    -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
  .titulo{font-weight:900;font-size:82px;line-height:.98;letter-spacing:-.01em;
    text-shadow:0 0 46px rgba(0,240,255,.42)}
  .titulo em{font-style:normal;background:linear-gradient(100deg,#00f0ff,#ff2ecb);
    -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
  .sub{font-family:system-ui,sans-serif;font-weight:400;font-size:24px;
       color:rgba(255,255,255,.72);max-width:26ch;line-height:1.4;margin-top:6px}
  .pie{position:absolute;bottom:44px;left:0;right:0;text-align:center;
       font-family:system-ui,sans-serif;font-weight:700;font-size:20px;
       letter-spacing:.24em;color:#00f0ff}
</style></head><body>
  <canvas id="fondo" width="1200" height="630"></canvas>
  <div class="capa">
    <div class="marca">VILLUMINATION</div>
    <div class="titulo">NO TE <em>CONFORMES</em></div>
    <div class="sub">Equipo, ropa y suplementos para quienes entrenan en serio.</div>
  </div>
  <div class="pie">VILLUMINATIONS.COM</div>
</body></html>`;

const navegador = await chromium.launch({ executablePath: CHROME });
const ctx = await navegador.newContext({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
const p = await ctx.newPage();
const errores = [];
p.on('pageerror', e => errores.push(e.message));
await p.setContent(PAGINA);

await p.evaluate(async (b64) => {
  const cara = new FontFace('Orbitron', `url(data:font/woff2;base64,${b64}) format('woff2')`);
  await cara.load();
  document.fonts.add(cara);
  await document.fonts.ready;
}, fuente);

// El fondo: los mismos haces y el mismo marco que la tienda, en un instante fijo
await p.evaluate(() => {
  const c = document.getElementById('fondo');
  const g = c.getContext('2d');
  const W = c.width, H = c.height, t = 3.4;
  g.fillStyle = '#05060a'; g.fillRect(0, 0, W, H);

  g.globalCompositeOperation = 'screen';
  for (let i = 0; i <= 11; i++) {
    const x = (i / 11) * W, fase = t * 0.9 + i * 0.7;
    const alto = H * (0.62 + 0.34 * Math.sin(fase));
    const an = W * 0.045;
    const a = 0.16 + 0.13 * Math.sin(fase * 1.3 + 1);
    const col = ['rgba(0,240,255,', 'rgba(139,92,246,', 'rgba(255,46,203,'][i % 3];
    const gr = g.createLinearGradient(x, H, x, H - alto);
    gr.addColorStop(0, col + a.toFixed(3) + ')');
    gr.addColorStop(1, col + '0)');
    g.fillStyle = gr;
    g.beginPath();
    g.moveTo(x - an * 0.5, H); g.lineTo(x + an * 0.5, H);
    g.lineTo(x + an * 1.6, H - alto); g.lineTo(x - an * 1.6, H - alto);
    g.fill();
  }
  g.globalCompositeOperation = 'source-over';

  // Vineta: el texto tiene que despegarse de los haces
  const vin = g.createRadialGradient(W / 2, H * 0.46, 90, W / 2, H * 0.46, W * 0.72);
  vin.addColorStop(0, 'rgba(5,6,10,0.52)');
  vin.addColorStop(0.5, 'rgba(5,6,10,0.34)');
  vin.addColorStop(1, 'rgba(5,6,10,0.94)');
  g.fillStyle = vin; g.fillRect(0, 0, W, H);

  // Marco de neon, el motivo del hero
  const m = 34;
  g.lineWidth = 3; g.lineJoin = 'round';
  g.strokeStyle = 'rgba(0,240,255,0.45)';
  g.shadowColor = 'rgba(0,240,255,0.55)'; g.shadowBlur = 22;
  g.strokeRect(m, m, W - m * 2, H - m * 2);
});

await p.waitForTimeout(300);
await p.screenshot({ path: SALIDA });
await navegador.close();

if (errores.length) { console.error('  errores: ' + errores.join(' | ')); process.exit(1); }
const kb = fs.statSync(SALIDA).size / 1024;
console.log(`  Listo: ${path.relative(RAIZ, SALIDA)}  1200x630  ${kb.toFixed(0)} KB`);
