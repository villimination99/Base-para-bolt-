/* EL BANCO DE FOTOS Y EL SERVIDOR DE PRUEBAS.
   ------------------------------------------------------------------
   Sirve una tienda de mentira que se comporta como la de verdad: cada foto
   pesa lo que Shopify entregaria, el texto viaja comprimido como lo sirve
   Shopify, y todo pasa por una linea 4G lenta. Sin esto, en localhost los
   megabytes son gratis y cualquier medida de velocidad es una fantasia.

   Vive aqui, y no dentro de una bateria, porque lo usan dos: la que mide el
   LCP de la portada y la que recorre TODAS las plantillas. Cuando estaba
   duplicado, arreglar el modelo en una dejaba la otra midiendo lo de antes.

   Uso tipico:
     const banco = crearBanco(TMP);
     ...
     banco.pincel = await b.newPage();     // hace falta para dibujar las fotos
     const base = await banco.escuchar();
                                                                            */
import fs from 'fs';
import path from 'path';
import http from 'http';
import zlib from 'zlib';

/* ================= LO QUE PESA UNA FOTO DE LA TIENDA =================
   Nada de esto es a ojo: fotos-de-la-tienda.json lleva el ancho, el alto y los
   bytes REALES de cada imagen subida, consultados al panel. Con eso:

   - Proporcion. Si la plantilla pide solo el ancho, el alto sale de la foto
     original, no de suponerla cuadrada. Un logotipo de 1600x400 pedido a 900
     px son 900x225, no 900x900.
   - PNG (o el WebP que el CDN de Shopify sirve solo en su lugar). El peso baja
     con los pixeles: bytes x (pixeles pedidos / pixeles del original), y por
     0,7 de la conversion a WebP. La foto del gimnasio, 1536x2752 y 5,95 MB,
     pedida a 1400x2217 son 3,1 MB; a 900x1425, 1,26 MB.
   - pjpg. JPEG de calidad alta: 0,11 bytes por pixel en una foto y 0,04 en un
     dibujo plano, que se distinguen por la densidad del original. La misma
     foto del gimnasio a 900x1425 son 141 KB.

   Nueve veces menos por cambiar una palabra en la plantilla. Esa es la razon
   de que exista este modelo: sin el, en localhost los megabytes son gratis y
   la bateria daba luz verde a una portada que en un movil tardaba 4,3 s.

   La imagen se dibuja de verdad (degradado oscuro con vetas de neon, que
   comprime parecido a una foto de gimnasio) para que el navegador pague el
   coste real de decodificarla, y despues se rellena hasta el peso del modelo.
   Los bytes de mas van detras del final del archivo, donde todo decodificador
   los ignora. */
const AQUI = path.dirname(new URL(import.meta.url).pathname);
const CATALOGO = JSON.parse(fs.readFileSync(path.join(AQUI, '..', 'verificadores/lcp/fotos-de-la-tienda.json'), 'utf8'));
export function medidasDe(src, wPedido, hPedido, fmt) {
  const o = CATALOGO[src] || CATALOGO.generica;
  const [ow, oh, obytes] = o;
  const w = wPedido || ow;
  const h = hPedido || Math.max(1, Math.round(w * oh / ow));
  const px = w * h;
  const densidad = obytes / (ow * oh);          // bytes por pixel del original
  let bytes;
  if (fmt === 'pjpg' || fmt === 'jpg') bytes = px * (densidad > 0.5 ? 0.11 : 0.04);
  else bytes = Math.min(obytes, obytes * px / (ow * oh)) * 0.7;
  return { w, h, bytes: Math.round(bytes) };
}

/* Un banco por bateria: cada una tiene su carpeta temporal y su contador de
   bytes, y dos baterias en paralelo no se pisan. */
export function crearBanco(TMP, TIPO) {
  const banco = { pincel: null, cuenta: [] };
  const fotos = new Map();
  async function foto(w, h, fmt, bytes) {
  const clave = w + 'x' + h + fmt + bytes;
  if (fotos.has(clave)) return fotos.get(clave);
  const tipo = (fmt === 'pjpg' || fmt === 'jpg') ? 'image/jpeg' : 'image/png';
  /* Se dibuja en JPEG y bajando la calidad hasta caber por debajo del peso del
     modelo, porque al cuerpo solo se le puede ANADIR relleno. Sin este ajuste,
     un PNG sintetico de 1200x2133 pesaba 1,5 MB el solo y la bateria acusaba a
     una foto de algo que era culpa del pincel. La calidad que sobrevive es la
     mas alta que cabe, asi que cuando el modelo dice "esto son 1,2 MB" el
     navegador tambien paga una descodificacion de verdad. */
  const dataUrl = await banco.pincel.evaluate(([w, h, tipo, tope]) => {
    const c = document.createElement('canvas');
    c.width = w; c.height = h;
    const x = c.getContext('2d');
    const g = x.createLinearGradient(0, 0, w, h);
    g.addColorStop(0, '#0b0f18'); g.addColorStop(0.5, '#18202e'); g.addColorStop(1, '#070a10');
    x.fillStyle = g; x.fillRect(0, 0, w, h);
    /* Pocas formas y grandes: lo dibujado tiene que pesar MENOS que el modelo,
       porque al cuerpo solo se le puede anadir relleno, no quitarlo. Con sesenta
       vetas finas un logotipo de 450 px se iba a 39 KB el solo. */
    for (let i = 0; i < 8; i++) {
      x.globalAlpha = 0.07 + (i % 4) * 0.03;
      x.fillStyle = i % 3 === 0 ? '#00d4ff' : (i % 3 === 1 ? '#ff2ecb' : '#7b2fff');
      x.fillRect((i * 211) % w, (i * 307) % h, w / 3, h / 6);
    }
    x.globalAlpha = 1;
    let mejor = c.toDataURL('image/jpeg', 0.92);
    for (const q of [0.92, 0.7, 0.5, 0.3, 0.15, 0.05]) {
      const d = c.toDataURL('image/jpeg', q);
      mejor = d;
      if (d.length * 0.75 <= tope) break;
    }
    return mejor;
  }, [w, h, tipo, bytes]);
  let cuerpoImg = Buffer.from(dataUrl.split(',')[1], 'base64');
  if (bytes > cuerpoImg.length) cuerpoImg = Buffer.concat([cuerpoImg, Buffer.alloc(bytes - cuerpoImg.length, 0)]);
  /* El cuerpo es JPEG siempre, tambien cuando la plantilla pide PNG: lo que
     se esta midiendo es lo que cuesta en red y en descodificar, y el peso ya lo
     fija el modelo. Se declara lo que de verdad se envia. */
  const r = { cuerpo: cuerpoImg, tipo: 'image/jpeg' };
  fotos.set(clave, r);
  return r;
  }

  /* Shopify sirve todo el texto comprimido, asi que aqui tambien. Sin esto la
   hoja de estilos viajaba con sus 206 KB en crudo -- un segundo entero de 4G
   solo para ella -- y la bateria medía un problema que la tienda no tiene.
   Los bytes que de verdad cruzan la red se apuntan por URL, que es la unica
   forma honesta de explicar despues de donde sale el numero. */
  const TEXTO = new Set(['text/html', 'text/javascript', 'text/css', 'application/json']);
  const srv = http.createServer(async (req, res) => {
  const [ruta, busca] = req.url.split('?');
  const u = decodeURIComponent(ruta);
  /* El navegador pide el icono de la pestana por su cuenta, sin que ninguna
     plantilla se lo diga. Devolverle un 404 hacia que la bateria acusara a la
     plantilla de tener un recurso roto que no era suyo. */
  if (u === '/favicon.ico') { res.writeHead(204); res.end(); return; }
  if (u === '/foto') {
    const q = new URLSearchParams(busca || '');
    const fmt = q.get('format') || 'png';
    const m = medidasDe(q.get('src') || 'generica',
                        parseInt(q.get('width') || '0', 10) || 0,
                        parseInt(q.get('height') || '0', 10) || 0, fmt);
    const f = await foto(m.w, m.h, fmt, m.bytes);
    banco.cuenta.push({ u: (q.get('src') || '?').slice(0, 34) + ' ' + m.w + 'x' + m.h + ' ' + fmt, n: f.cuerpo.length });
    res.writeHead(200, { 'content-type': f.tipo, 'cache-control': 'public, max-age=600' });
    res.end(f.cuerpo);
    return;
  }
  const f = path.join(TMP, u.replace(/^\//, ''));
  fs.readFile(f, (err, d) => {
    if (err) { res.writeHead(404); res.end('no ' + u); return; }
    const tipo = TIPO[path.extname(f)] || 'application/octet-stream';
    const cab = { 'content-type': tipo };
    let salida = d;
    if (TEXTO.has(tipo) && /\bbr\b/.test(req.headers['accept-encoding'] || '')) {
      salida = zlib.brotliCompressSync(d);
      cab['content-encoding'] = 'br';
    }
    banco.cuenta.push({ u, n: salida.length });
    res.writeHead(200, cab);
    res.end(salida);
  });
  });

  banco.srv = srv;
  banco.escuchar = () => new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));
  banco.pesados = (n = 4) => banco.cuenta.slice().sort((a, b) => b.n - a.n).slice(0, n);
  banco.total = () => banco.cuenta.reduce((a, x) => a + x.n, 0);
  return banco;
}

/* La 4G lenta de Lighthouse: 1,6 Mb/s y 150 ms de ida y vuelta. Es la red en
   la que Google recoge sus numeros de campo. */
export async function frenar(ctx, p) {
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', {
    offline: false, latency: 150,
    downloadThroughput: 1.6 * 1024 * 1024 / 8, uploadThroughput: 750 * 1024 / 8,
  });
}
