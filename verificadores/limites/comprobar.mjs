/* LAS REGLAS DE SHOPIFY, ESCRITAS Y COMPROBADAS.
   ------------------------------------------------------------------
   Un tema no se rechaza al subirlo porque sea feo: se rechaza porque pasa un
   limite. Y los limites no avisan mientras vas holgado -- avisan el dia que
   anades la seccion veintiseis, cuando ya has cerrado la version y estas
   subiendo el zip. Esto los pone por delante.

   Los numeros no son inventados ni "por si acaso": son los que publica
   Shopify. Cuando un limite tiene margen, se avisa ANTES de rozarlo (al 80 %),
   porque enterarse de que quedan dos secciones libres es util y enterarse de
   que no queda ninguna, no.

   Tambien vigila una cosa que no es un limite sino una rotura silenciosa: una
   regla CSS que pide url(algo.png) de un archivo que no esta en assets. Eso no
   da error en ningun sitio; simplemente no se pinta, y nadie lo ve hasta que
   un cliente mira una tarjeta sin fondo.

   Uso:  node verificadores/limites/comprobar.mjs                          */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');

/* Los limites publicados por Shopify para un tema de Online Store 2.0. */
const LIMITE = {
  seccionesPorPlantilla: 25,   // secciones en una plantilla JSON
  bloquesPorSeccion: 50,       // bloques dentro de una seccion
  archivoSuelto: 20 * 1024 * 1024,   // 20 MB por archivo de assets
  zip: 50 * 1024 * 1024,             // 50 MB el paquete entero
  ajustes: 1024 * 1024,              // 1 MB settings_data.json
};

let mal = 0, avisos = 0;
const decir = (ok, txt) => { if (!ok) mal++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };
const rozando = (txt) => { avisos++; console.log(`  AVISO ${txt}`); };
const kb = (n) => (n / 1024).toFixed(0) + ' KB';

const leerJSON = (f) => JSON.parse(fs.readFileSync(f, 'utf8'));
const listar = (d, ext) => fs.existsSync(d)
  ? fs.readdirSync(d).filter(f => f.endsWith(ext)).map(f => path.join(d, f)) : [];

console.log('\n--- Secciones y bloques por plantilla ---');
let peorSec = 0, peorBloq = 0;
for (const f of [...listar(path.join(T, 'templates'), '.json'), ...listar(path.join(T, 'sections'), '.json')]) {
  const d = leerJSON(f);
  const secciones = Object.keys(d.sections || {});
  peorSec = Math.max(peorSec, secciones.length);
  for (const [id, s] of Object.entries(d.sections || {})) {
    const n = Object.keys(s.blocks || {}).length;
    peorBloq = Math.max(peorBloq, n);
    if (n > LIMITE.bloquesPorSeccion) decir(false, `${path.basename(f)} · ${id}: ${n} bloques, el limite son ${LIMITE.bloquesPorSeccion}`);
  }
  if (secciones.length > LIMITE.seccionesPorPlantilla)
    decir(false, `${path.basename(f)}: ${secciones.length} secciones, el limite son ${LIMITE.seccionesPorPlantilla}`);
}
decir(peorSec <= LIMITE.seccionesPorPlantilla,
  `la plantilla mas cargada tiene ${peorSec} secciones (limite ${LIMITE.seccionesPorPlantilla})`);
decir(peorBloq <= LIMITE.bloquesPorSeccion,
  `la seccion mas cargada tiene ${peorBloq} bloques (limite ${LIMITE.bloquesPorSeccion})`);
if (peorSec > LIMITE.seccionesPorPlantilla * 0.8) rozando(`quedan solo ${LIMITE.seccionesPorPlantilla - peorSec} secciones libres en la plantilla mas cargada`);

console.log('\n--- Peso ---');
const archivos = [];
(function recorrer(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) recorrer(p); else archivos.push(p);
  }
})(T);
const total = archivos.reduce((s, f) => s + fs.statSync(f).size, 0);
const mayor = archivos.map(f => [fs.statSync(f).size, f]).sort((a, b) => b[0] - a[0])[0];
decir(mayor[0] <= LIMITE.archivoSuelto,
  `el archivo mayor es ${path.relative(T, mayor[1])} con ${kb(mayor[0])} (limite 20 MB)`);
console.log(`        ${archivos.length} archivos · ${(total / 1024 / 1024).toFixed(2)} MB sin comprimir`);

const ajustes = path.join(T, 'config/settings_data.json');
decir(fs.statSync(ajustes).size <= LIMITE.ajustes,
  `settings_data.json pesa ${kb(fs.statSync(ajustes).size)} (limite 1 MB)`);

/* Si hay un zip construido al lado, se mide tambien: es lo que de verdad se
   sube, y es el unico numero que Shopify mira al recibirlo. */
const zips = fs.readdirSync(RAIZ).filter(f => /^villumination-3d-theme-.*\.zip$/.test(f));
if (zips.length) {
  const z = zips.sort()[zips.length - 1];
  const t = fs.statSync(path.join(RAIZ, z)).size;
  decir(t <= LIMITE.zip, `${z} pesa ${kb(t)} (limite 50 MB)`);
} else {
  console.log('        (todavia no hay zip construido; se medira cuando lo haya)');
}

console.log('\n--- Lo que el CSS pide y no esta ---');
/* url(#algo) son referencias a filtros SVG del propio documento y url(data:)
   lleva el archivo dentro: ni una ni otra piden nada al servidor. */
const faltan = [];
for (const f of listar(path.join(T, 'assets'), '.css')) {
  const css = fs.readFileSync(f, 'utf8');
  for (const m of css.matchAll(/url\(\s*(['"]?)([^'")]+)\1\s*\)/g)) {
    const u = m[2].trim();
    if (u.startsWith('data:') || u.startsWith('#') || u.startsWith('%23') || /^https?:/.test(u)) continue;
    const nombre = u.split('/').pop().split('?')[0];
    if (!fs.existsSync(path.join(T, 'assets', nombre))) faltan.push(`${path.basename(f)} pide ${u}`);
  }
}
decir(faltan.length === 0, faltan.length
  ? `el CSS pide ${faltan.length} archivo(s) que no estan: ${faltan.slice(0, 3).join(' · ')}`
  : 'todo lo que el CSS pide con url() esta en assets o viaja dentro del propio archivo');

console.log(mal
  ? `\n  ${mal} en rojo contra las reglas de Shopify.\n`
  : `\nEl tema cabe de sobra en lo que Shopify permite${avisos ? `, con ${avisos} aviso(s) de margen` : ''}.\n`);
process.exit(mal ? 1 : 0);
