/* EL LINTER OFICIAL DE SHOPIFY, DENTRO DE LA COMPUERTA.
   ------------------------------------------------------------------
   Esto existe porque durante varias rondas CREIMOS que se estaba pasando y no
   se estaba pasando. El lanzador vivia en un archivo suelto en la raiz,
   tcrun.mjs, y ese nombre esta en .gitignore: no viajaba en el repositorio.
   Al reiniciarse el contenedor desaparecio, `npm run theme-check` empezo a dar
   "Cannot find module" y nadie se entero, porque nada dependia de el.

   Una comprobacion que no esta versionada no es una comprobacion: es una
   costumbre. Por eso ahora vive aqui, con las demas, y entra en la lista de
   baterias del empaquetador. Si desaparece, el zip no se escribe.

   QUE SE EXIGE. Los errores (severidad 0) no se perdonan: son cosas que
   Shopify considera rotas -- un filtro que no existe, un objeto que no se
   puede usar en esa plantilla, un JSON invalido. Los avisos (severidad 1) SI
   se pueden tolerar, pero de uno en uno y POR ESCRITO: cada uno lleva aqui su
   razon, igual que en la bateria de plataformas. Un aviso sin justificar pone
   la bateria en rojo aunque sea "solo un aviso", porque la alternativa --
   tolerarlos todos -- es no mirar.

   Uso:  node verificadores/shopify/comprobar.mjs                          */
import { themeCheckRun } from '@shopify/theme-check-node';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');

/* Avisos tolerados, cada uno con su motivo. El motivo no es decoracion: es lo
   que permite que dentro de seis meses alguien decida si sigue valiendo. */
const TOLERADOS = {
  RemoteAsset:
    'Son las miniaturas de YouTube (i.ytimg.com) y el propio reproductor. No pueden ' +
    'servirse desde el CDN de Shopify porque no son nuestras: las genera YouTube por ' +
    'cada video. El tema ya trae respaldo pintado debajo para cuando el dominio esta ' +
    'bloqueado, que se comprueba en la bateria de medios.',
};

const r = await themeCheckRun(T, undefined, () => {});
const errores = r.offenses.filter(o => o.severity === 0);
const avisos  = r.offenses.filter(o => o.severity !== 0);

let mal = 0;
const decir = (ok, txt) => { if (!ok) mal++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };
const corto = (u) => String(u).replace('file://' + T + '/', '').replace('file://', '');

console.log(`\n--- theme-check de Shopify sobre ${path.basename(T)} ---`);
console.log(`  ${r.theme.length} archivos analizados · ${r.offenses.length} avisos en total\n`);

decir(errores.length === 0, errores.length === 0
  ? 'ningun ERROR: Shopify no considera nada roto'
  : `${errores.length} ERROR(es), que no se perdonan`);
for (const o of errores.slice(0, 10)) {
  console.log(`        ${o.check}  ${corto(o.uri)}:${o.start.line + 1}  ${o.message}`);
}

/* Los avisos se agrupan por tipo: lo que importa no es cuantas veces sale
   RemoteAsset, sino si RemoteAsset esta justificado. */
const porTipo = {};
for (const o of avisos) (porTipo[o.check] = porTipo[o.check] || []).push(o);

for (const [tipo, lista] of Object.entries(porTipo)) {
  const razon = TOLERADOS[tipo];
  decir(!!razon, razon
    ? `${tipo.padEnd(22)} ${String(lista.length).padStart(2)} aviso(s) · tolerado: ${razon}`
    : `${tipo.padEnd(22)} ${lista.length} aviso(s) SIN justificar: ${lista[0].message}`);
  if (!razon) for (const o of lista.slice(0, 4)) {
    console.log(`        ${corto(o.uri)}:${o.start.line + 1}`);
  }
}

/* Y al reves: una tolerancia que ya no hace falta tambien sobra, porque
   invita a dejar de mirar. Si el motivo desaparecio, que se note. */
for (const tipo of Object.keys(TOLERADOS)) {
  if (!porTipo[tipo]) console.log(`  (nota) la tolerancia de ${tipo} ya no hace falta: el tema no lo usa`);
}

console.log(mal
  ? `\n  ${mal} en rojo en el linter de Shopify.\n`
  : '\nEl linter oficial de Shopify no encuentra nada roto, y cada aviso que queda esta justificado por escrito.\n');
process.exit(mal ? 1 : 0);
