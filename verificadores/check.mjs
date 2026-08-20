/* Verificadores del tema Villumination 3D.
   Cada uno nacio de un fallo real encontrado en la tienda. Viven en el
   repositorio (no en una carpeta temporal) para que no se pierdan.
   Uso:  node verificadores/check.mjs        */
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { toLiquidHtmlAST } from '@shopify/liquid-html-parser';

const T = 'theme';
const walk = (d, ext, out = []) => {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, ext, out);
    else if (ext.test(e.name)) out.push(p);
  }
  return out;
};
const liquids = () => walk(T, /\.liquid$/);
const jsons = () => walk(T, /\.json$/);
const read = f => fs.readFileSync(f, 'utf8');
const stripBlocks = s => s.replace(
  /\{%-?\s*(schema|comment|javascript|stylesheet|style)\s*-?%\}[\s\S]*?\{%-?\s*end\1\s*-?%\}/g,
  m => '\n'.repeat((m.match(/\n/g) || []).length));
const line = (s, i) => s.slice(0, i).split('\n').length;

const results = [];
const check = (name, fn) => {
  let out;
  try { out = fn() || []; } catch (e) { out = ['el verificador fallo: ' + e.message]; }
  results.push({ name, problems: out });
};

/* 1 — Liquid: el parser oficial de Shopify */
check('Liquid (parser de Shopify)', () => {
  const bad = [];
  for (const f of liquids()) {
    try { toLiquidHtmlAST(read(f)); }
    catch (e) { bad.push(`${f}: ${e.message.split('\n')[0]}`); }
  }
  return bad;
});

/* 2 — Llaves literales dentro de una etiqueta Liquid.
   El importador de Shopify DESCARTA el archivo entero sin avisar. */
check('Llaves literales en etiquetas Liquid', () => {
  const bad = [];
  for (const f of liquids()) {
    const s = read(f);
    for (const m of s.matchAll(/\{\{-?([\s\S]*?)-?\}\}|\{%-?([\s\S]*?)-?%\}/g)) {
      const b = m[1] !== undefined ? m[1] : m[2];
      if (/[{}]/.test(b)) bad.push(`${f}:${line(s, m.index)} -> ${m[0].slice(0, 60)}`);
    }
  }
  return bad;
});

/* 3 — JSON valido */
check('JSON', () => {
  const bad = [];
  for (const f of jsons()) { try { JSON.parse(read(f)); } catch (e) { bad.push(`${f}: ${e.message}`); } }
  return bad;
});

/* 4 — Sintaxis JS */
check('Sintaxis JS', () => {
  const bad = [];
  for (const f of walk(`${T}/assets`, /\.js$/)) {
    try { execSync(`node --check "${f}"`, { stdio: 'pipe' }); }
    catch (e) { bad.push(`${f}: ${String(e.stderr).split('\n')[0]}`); }
  }
  return bad;
});

/* 5 — Llaves de CSS equilibradas */
check('CSS equilibrado', () => {
  const bad = [];
  for (const f of walk(`${T}/assets`, /\.css$/)) {
    const s = read(f);
    const o = (s.match(/\{/g) || []).length, c = (s.match(/\}/g) || []).length;
    if (o !== c) bad.push(`${f}: ${o} aperturas / ${c} cierres`);
  }
  return bad;
});

/* 6 — render / section / asset_url que no resuelven (error 500 en tienda) */
check('Referencias render, section y asset_url', () => {
  const bad = [];
  const has = p => fs.existsSync(p);
  for (const f of [...liquids(), ...jsons()]) {
    const s = read(f);
    for (const m of s.matchAll(/\{%-?\s*(?:render|include)\s+'([^']+)'/g))
      if (!has(`${T}/snippets/${m[1]}.liquid`)) bad.push(`${f}:${line(s, m.index)} falta snippet '${m[1]}'`);
    for (const m of s.matchAll(/\{%-?\s*section\s+'([^']+)'/g))
      if (!has(`${T}/sections/${m[1]}.liquid`)) bad.push(`${f}:${line(s, m.index)} falta seccion '${m[1]}'`);
    for (const m of s.matchAll(/'([^']+\.(?:css|js|png|jpg|jpeg|svg|webp|woff2?|json))'\s*\|\s*asset_url/g))
      if (!has(`${T}/assets/${m[1]}`)) bad.push(`${f}:${line(s, m.index)} falta asset '${m[1]}'`);
  }
  for (const f of jsons()) {
    let j; try { j = JSON.parse(read(f)); } catch { continue; }
    for (const k in (j.sections || {})) {
      const t = j.sections[k] && j.sections[k].type;
      if (t && !has(`${T}/sections/${t}.liquid`)) bad.push(`${f}: seccion '${t}' no existe`);
    }
  }
  return bad;
});

/* 7 — Variables CSS usadas con var() pero nunca definidas */
check('Variables CSS definidas', () => {
  const defined = new Set(), used = new Map();
  for (const f of walk(T, /\.(css|liquid|js|json)$/)) {
    const s = read(f);
    for (const m of s.matchAll(/(--[\w-]+)\s*:/g)) defined.add(m[1]);
    for (const m of s.matchAll(/var\(\s*(--[\w-]+)\s*([,)])/g)) {
      if (m[2] === ',') continue;              // tiene valor de respaldo
      if (!used.has(m[1])) used.set(m[1], f);
    }
  }
  return [...used].filter(([v]) => !defined.has(v)).map(([v, f]) => `${v} usada en ${f}`);
});

/* 8 — Ajustes globales definidos pero que no usa nadie */
check('Ajustes globales en uso', () => {
  const sch = JSON.parse(read(`${T}/config/settings_schema.json`));
  let src = '';
  for (const f of walk(T, /\.(liquid|js)$/)) if (!f.includes('settings_schema')) src += read(f) + '\n';
  const bad = [];
  for (const p of sch) for (const s of (p.settings || [])) {
    if (!s.id) continue;
    if (!new RegExp('settings\\.' + s.id + '(?![\\w])').test(src)) bad.push(`${s.id} (panel ${p.name})`);
  }
  return bad;
});

/* 9 — Ajustes de seccion y de bloque sin usar en su propio archivo */
check('Ajustes de seccion y bloque en uso', () => {
  const bad = [];
  for (const f of walk(`${T}/sections`, /\.liquid$/)) {
    const s = read(f);
    const m = s.match(/\{%-?\s*schema\s*-?%\}([\s\S]*?)\{%-?\s*endschema\s*-?%\}/);
    if (!m) continue;
    let j; try { j = JSON.parse(m[1]); } catch { continue; }
    const body = s.replace(m[0], '');
    for (const st of (j.settings || [])) if (st.id && !new RegExp('section\\.settings\\.' + st.id + '(?![\\w])').test(body))
      bad.push(`${f}: section.settings.${st.id}`);
    for (const b of (j.blocks || [])) for (const st of (b.settings || []))
      if (st.id && !new RegExp('(block|b)\\.settings\\.' + st.id + '(?![\\w])').test(body))
        bad.push(`${f}: block[${b.type}].settings.${st.id}`);
  }
  return bad;
});

/* 10 — Ajustes fantasma: el codigo los LEE pero no existen (salen vacios) */
check('Ajustes fantasma', () => {
  const sch = JSON.parse(read(`${T}/config/settings_schema.json`));
  const ids = new Set();
  for (const p of sch) for (const s of (p.settings || [])) if (s.id) ids.add(s.id);
  const bad = [];
  for (const f of walk(T, /\.(liquid|json)$/)) {
    if (f.includes('settings_schema') || f.includes('settings_data')) continue;
    const s = read(f);
    for (const m of s.matchAll(/(^|[^\w.])settings\.([a-z0-9_]+)/gi))
      if (!ids.has(m[2])) bad.push(`${f}:${line(s, m.index)} settings.${m[2]}`);
  }
  return [...new Set(bad)];
});

/* 11 — Claves de traduccion presentes en TODOS los idiomas */
check('Traducciones completas', () => {
  const flat = (o, p = '', out = {}) => {
    for (const k in o) {
      const key = p ? `${p}.${k}` : k;
      if (o[k] && typeof o[k] === 'object') flat(o[k], key, out); else out[key] = o[k];
    }
    return out;
  };
  const locales = {};
  for (const f of fs.readdirSync(`${T}/locales`).filter(x => x.endsWith('.json') && !x.includes('schema')))
    locales[f] = flat(JSON.parse(read(`${T}/locales/${f}`)));
  const bad = [];
  for (const f of liquids()) {
    const s = read(f);
    for (const m of s.matchAll(/'([a-z0-9_]+(?:\.[a-z0-9_?]+)+)'\s*\|\s*t\b/gi)) {
      for (const [loc, keys] of Object.entries(locales))
        if (!(m[1] in keys)) bad.push(`'${m[1]}' falta en ${loc} (usada en ${f}:${line(s, m.index)})`);
    }
  }
  return [...new Set(bad)];
});

/* 12 — Traducciones con hueco ({{ count }}) a las que no se pasa el valor */
check('Variables de traduccion', () => {
  const flat = (o, p = '', out = {}) => {
    for (const k in o) {
      const key = p ? `${p}.${k}` : k;
      if (o[k] && typeof o[k] === 'object') flat(o[k], key, out); else out[key] = o[k];
    }
    return out;
  };
  const locales = {};
  for (const f of fs.readdirSync(`${T}/locales`).filter(x => x.endsWith('.json') && !x.includes('schema')))
    locales[f] = flat(JSON.parse(read(`${T}/locales/${f}`)));
  const bad = [];
  for (const f of liquids()) {
    const s = read(f);
    for (const m of s.matchAll(/'([a-z0-9_]+(?:\.[a-z0-9_?]+)+)'\s*\|\s*t([^}%]*)/gi)) {
      for (const keys of Object.values(locales)) {
        const val = keys[m[1]];
        if (typeof val !== 'string') continue;
        for (const v of new Set([...val.matchAll(/\{\{\s*([a-z0-9_]+)\s*\}\}/gi)].map(x => x[1])))
          if (!new RegExp('\\b' + v + '\\s*:').test(m[2] || ''))
            bad.push(`'${m[1]}' necesita ${v}: en ${f}:${line(s, m.index)}`);
      }
    }
  }
  return [...new Set(bad)];
});

/* 13 — Texto visible escrito a mano (no se traduce nunca).
   El que solo aparece dentro del editor (request.design_mode) esta permitido. */
check('Texto visible sin traducir', () => {
  const ES = /[áéíóúñ¿¡]|\b(el|la|los|las|para|con|tu|tus|sin|más|desde|hasta|todos|envío|gratis|carrito|compra|producto|productos|precio|añadir|agregar|comprar|oferta|talla)\b/i;
  const bad = [];
  for (const f of liquids()) {
    let s = stripBlocks(read(f));
    s = s.replace(/\{%-?\s*if\s+request\.design_mode\s*-?%\}[\s\S]*?\{%-?\s*endif\s*-?%\}/g,
      m => '\n'.repeat((m.match(/\n/g) || []).length));
    s.split('\n').forEach((ln, i) => {
      const t = ln.replace(/\{\{[\s\S]*?\}\}/g, '').replace(/\{%[\s\S]*?%\}/g, '');
      for (const m of t.matchAll(/>([^<>]+)</g)) {
        const txt = m[1].replace(/&[a-z]+;/gi, ' ').trim();
        if (txt.length >= 4 && ES.test(txt)) bad.push(`${f}:${i + 1} "${txt.slice(0, 60)}"`);
      }
    });
  }
  return bad;
});

/* 14 — Accesibilidad y escapado */
check('Accesibilidad y escapado', () => {
  const bad = [];
  const SAFE = /^(settings\.color_|request\.locale|canonical_url|og_type|cart\.currency|\d)|divided_by|\.price\b|iso_code/;
  for (const f of liquids()) {
    const s = stripBlocks(read(f));
    for (const m of s.matchAll(/<img\b[^>]*>/g))
      if (!/\balt\s*=/.test(m[0])) bad.push(`${f}:${line(s, m.index)} <img> sin alt`);
    for (const m of s.matchAll(/<a\b[^>]*target\s*=\s*["']_blank["'][^>]*>/g))
      if (!/rel\s*=\s*["'][^"']*noopener/.test(m[0])) bad.push(`${f}:${line(s, m.index)} target=_blank sin rel=noopener`);
    for (const m of s.matchAll(/<button\b([^>]*)>([\s\S]{0,220}?)<\/button>/g)) {
      if (/aria-label|aria-labelledby/.test(m[1])) continue;
      const text = m[2].replace(/\{[\{%][\s\S]*?[\}%]\}/g, '').replace(/<[^>]*>/g, '').replace(/&[a-z]+;/gi, 'x').trim();
      if (!text && !/\{\{[\s\S]*?\}\}/.test(m[2])) bad.push(`${f}:${line(s, m.index)} <button> sin texto ni aria-label`);
    }
    for (const m of s.matchAll(/(alt|title|aria-label|placeholder|content)\s*=\s*"\{\{\s*([^}]+?)\s*\}\}"/g)) {
      const e = m[2].trim();
      if (!/\|\s*(escape|escape_once|json|money|t\b|date|image_url|handle|strip_html)/.test(e) && !SAFE.test(e))
        bad.push(`${f}:${line(s, m.index)} ${m[1]}="{{ ${e.slice(0, 40)} }}" sin escape`);
    }
  }
  return bad;
});

/* 15 — aria-controls / for que apuntan a un id inexistente */
check('Referencias aria y for', () => {
  const ids = new Set();
  for (const f of liquids()) for (const m of read(f).matchAll(/\sid="([^"]+)"/g)) ids.add(m[1]);
  const bad = [];
  for (const f of liquids()) {
    const s = read(f);
    for (const m of s.matchAll(/\s(aria-controls|aria-labelledby|aria-describedby|for)="([^"]+)"/g)) {
      if (m[2].includes('{{') || m[2].includes('{%')) continue;
      for (const ref of m[2].split(/\s+/)) if (ref && !ids.has(ref))
        bad.push(`${f}:${line(s, m.index)} ${m[1]}="${ref}"`);
    }
  }
  return bad;
});

/* 16 — Anidamientos HTML invalidos */
check('Anidamiento HTML', () => {
  const VOID = ['br','img','input','meta','link','hr','source','path','circle','line','polygon','rect','use','stop'];
  const bad = [];
  for (const f of liquids()) {
    const s = stripBlocks(read(f));
    const stack = [];
    for (const m of s.matchAll(/<(\/?)([a-z][a-z0-9-]*)\b([^>]*)>/gi)) {
      const close = m[1] === '/', tag = m[2].toLowerCase(), attrs = m[3] || '';
      if (/\/$/.test(attrs) || VOID.includes(tag)) continue;
      if (!close) {
        if (tag === 'a' && stack.includes('a')) bad.push(`${f}:${line(s, m.index)} <a> dentro de <a>`);
        if (tag === 'button' && stack.includes('a')) bad.push(`${f}:${line(s, m.index)} <button> dentro de <a>`);
        const parent = stack[stack.length - 1];
        if ((parent === 'ul' || parent === 'ol') && !['li','script','template'].includes(tag))
          bad.push(`${f}:${line(s, m.index)} <${tag}> como hijo directo de <${parent}>`);
        stack.push(tag);
      } else { const i = stack.lastIndexOf(tag); if (i >= 0) stack.length = i; }
    }
  }
  return [...new Set(bad)];
});

/* 17 — richtext dentro de un contenedor que no admite parrafos ni listas */
check('Richtext en contenedor valido', () => {
  const LINEA = new Set(['p','span','a','button','li','h1','h2','h3','h4','h5','h6','label','strong','em','td','th','option']);
  const NOTEXTO = new Set(['ul','ol','table','tbody','thead','tr','select','dl']);
  const bad = [];
  for (const f of walk(`${T}/sections`, /\.liquid$/)) {
    const s = read(f);
    const m = s.match(/\{%-?\s*schema\s*-?%\}([\s\S]*?)\{%-?\s*endschema\s*-?%\}/);
    if (!m) continue;
    let j; try { j = JSON.parse(m[1]); } catch { continue; }
    const rich = new Set(), plain = new Set();
    const collect = a => { for (const st of (a || [])) { if (!st.id) continue;
      (['richtext','html','inline_richtext'].includes(st.type) ? rich : plain).add(st.id); } };
    collect(j.settings); for (const b of (j.blocks || [])) collect(b.settings);
    for (const id of plain) rich.delete(id);          // mismo id con dos tipos: ambiguo
    if (!rich.size) continue;
    const body = s.replace(m[0], '');
    for (const mm of body.matchAll(/\{\{\s*(?:section|block)\.settings\.([a-z0-9_]+)\s*\}\}/gi)) {
      if (!rich.has(mm[1])) continue;
      const stack = [];
      for (const t of body.slice(0, mm.index).matchAll(/<(\/?)([a-z][a-z0-9-]*)\b[^>]*>/gi)) {
        const tag = t[2].toLowerCase();
        if (['br','img','input','meta','link','hr','source'].includes(tag)) continue;
        if (t[1] === '/') { const i = stack.lastIndexOf(tag); if (i >= 0) stack.length = i; } else stack.push(tag);
      }
      const parent = stack[stack.length - 1];
      if (parent && (NOTEXTO.has(parent) || LINEA.has(parent)))
        bad.push(`${f}:${line(body, mm.index)} ${mm[1]} (richtext) dentro de <${parent}>`);
    }
  }
  return bad;
});

/* 18 — JSON-LD valido con las condiciones en verdadero Y en falso.
   Una coma sobrante en una rama es invisible hasta que Google la rechaza. */
check('JSON-LD', () => {
  const render = (src, cond) => {
    let s = src;
    s = s.replace(/\{%-?\s*comment\s*-?%\}[\s\S]*?\{%-?\s*endcomment\s*-?%\}/g, '');
    s = s.replace(/\{%-?\s*(assign|liquid|capture|endcapture)[\s\S]*?-?%\}/g, '');
    s = s.replace(/\{%-?\s*unless\s+forloop\.last\s*-?%\},?\{%-?\s*endunless\s*-?%\}/g, '');
    s = s.replace(/\{%-?\s*for\s[^%]*-?%\}/g, '').replace(/\{%-?\s*endfor\s*-?%\}/g, '');
    s = s.replace(/\{%-?\s*render\s+'([^']+)'\s*-?%\}/g, (m, n) => {
      const p = `${T}/snippets/${n}.liquid`;
      return fs.existsSync(p) ? render(read(p), cond) : '';
    });
    let prev = null;
    while (prev !== s) {
      prev = s;
      s = s.replace(/\{%-?\s*if\s[^%]*?-?%\}((?:(?!\{%-?\s*(?:if|endif)\s)[\s\S])*?)\{%-?\s*endif\s*-?%\}/g,
        (m, body) => {
          const parts = body.split(/\{%-?\s*(?:elsif\s[^%]*?|else)\s*-?%\}/);
          return cond ? parts[0] : (parts.length > 1 ? parts[parts.length - 1] : '');
        });
    }
    s = s.replace(/\{\{[^}]*\|\s*json\s*\}\}/g, '"v"').replace(/\{\{[^}]*\}\}/g, '1');
    return s;
  };
  const bad = [];
  let n = 0;
  for (const f of liquids()) {
    const src = read(f);
    if (!/application\/ld\+json/.test(src)) continue;
    for (const cond of [true, false]) {
      for (const m of render(src, cond).matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
        n++;
        try { JSON.parse(m[1]); }
        catch (e) { bad.push(`${f} (condiciones ${cond ? 'verdaderas' : 'falsas'}): ${e.message}`); }
      }
    }
  }
  return bad.length ? bad : (n ? [] : ['no se encontro ningun bloque JSON-LD']);
});

/* 19 — Animaciones que fuerzan recalculo de maquetacion en cada fotograma */
check('Rendimiento de animaciones', () => {
  const css = read(`${T}/assets/villumination.css`);
  const CARAS = /^(width|height|top|left|right|bottom|margin|padding|inset)$/;
  const bad = [];
  for (const m of css.matchAll(/@keyframes\s+([\w-]+)\s*\{/g)) {
    let i = m.index + m[0].length - 1, depth = 0, k = i;
    while (k < css.length) { if (css[k] === '{') depth++; else if (css[k] === '}') { depth--; if (!depth) break; } k++; }
    const props = new Set();
    for (const p of css.slice(i + 1, k).matchAll(/(?:^|[{;])\s*([a-z-]+)\s*:/g)) props.add(p[1]);
    const caras = [...props].filter(p => CARAS.test(p));
    // Las barras de progreso animan el ancho a proposito y una sola vez.
    if (caras.length && !/loaderFill|shipFill/i.test(m[1]))
      bad.push(`@keyframes ${m[1]} anima ${caras.join(', ')}`);
  }
  return bad;
});

/* 20 — Reglas de Shopify para settings_schema.json.
   Si se incumplen, "Parametros del tema" sale EN BLANCO sin ningun mensaje. */
check('Esquema de ajustes (reglas de Shopify)', () => {
  const raw = fs.readFileSync(`${T}/config/settings_schema.json`);
  const bad = [];
  if (raw[0] === 0xEF && raw[1] === 0xBB && raw[2] === 0xBF) bad.push('el archivo empieza por BOM');
  const txt = raw.toString('utf8');
  for (let i = 0; i < txt.length; i++) {
    const c = txt.charCodeAt(i);
    if ((c < 32 && ![10, 13, 9].includes(c)) || [0x200b, 0x200e, 0x200f, 0xfeff, 0x2028, 0x2029].includes(c)) {
      bad.push(`caracter invisible o de control en la posicion ${i}`); break;
    }
  }
  let d; try { d = JSON.parse(txt); } catch (e) { return ['JSON invalido: ' + e.message]; }
  if (!Array.isArray(d)) return ['la raiz debe ser una lista'];
  if (!(d[0] && d[0].name === 'theme_info')) bad.push('theme_info debe ser el PRIMER elemento');
  for (const k of ['theme_name', 'theme_version', 'theme_author']) if (d[0] && !d[0][k]) bad.push('theme_info sin ' + k);
  const VALID = new Set(['text','textarea','image_picker','radio','select','checkbox','range','color','color_background',
    'font_picker','collection','collection_list','product','product_list','blog','page','link_list','url','richtext','html',
    'article','video','video_url','liquid','header','paragraph','number','inline_richtext','color_scheme','text_alignment']);
  const EXPECT = { checkbox:'boolean', range:'number', number:'number', text:'string', textarea:'string',
    select:'string', radio:'string', color:'string', font_picker:'string', richtext:'string', html:'string', url:'string' };
  const ids = new Map();
  for (const p of d) {
    if (p.name === 'theme_info') continue;
    if (!Array.isArray(p.settings)) { bad.push(`panel "${p.name}" sin lista de ajustes`); continue; }
    for (const s of p.settings) {
      const w = `"${p.name}" / ${s.id || s.type}`;
      if (!VALID.has(s.type)) bad.push(`${w}: tipo "${s.type}" no existe`);
      if (['header', 'paragraph'].includes(s.type)) { if (!s.content) bad.push(`${w}: sin "content"`); continue; }
      if (!s.id) { bad.push(`${w}: falta "id"`); continue; }
      if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(s.id)) bad.push(`${w}: id no valido`);
      ids.set(s.id, (ids.get(s.id) || 0) + 1);
      if (!s.label) bad.push(`${w}: falta "label"`);
      if (s.type === 'range') {
        const step = s.step == null ? 1 : s.step;
        if (s.min == null || s.max == null) bad.push(`${w}: range sin min/max`);
        else {
          const pasos = (s.max - s.min) / step;
          if (pasos > 101) bad.push(`${w}: ${Math.round(pasos)} pasos (maximo 101)`);
          if (Math.abs(pasos - Math.round(pasos)) > 1e-9) bad.push(`${w}: step ${step} no divide exacto`);
          if (s.default == null) bad.push(`${w}: range SIN default`);
          else if (s.default < s.min || s.default > s.max) bad.push(`${w}: default fuera del intervalo`);
          else if (Math.abs(((s.default - s.min) / step) - Math.round((s.default - s.min) / step)) > 1e-9)
            bad.push(`${w}: default ${s.default} no cae en un paso`);
        }
      }
      if (['select', 'radio'].includes(s.type)) {
        const opts = (s.options || []).map(o => o && o.value);
        if (!opts.length) bad.push(`${w}: sin opciones`);
        if (s.default !== undefined && !opts.includes(s.default)) bad.push(`${w}: default no esta entre las opciones`);
      }
      if (s.default !== undefined && EXPECT[s.type] && typeof s.default !== EXPECT[s.type])
        bad.push(`${w}: default es ${typeof s.default}, deberia ser ${EXPECT[s.type]}`);
    }
  }
  for (const [k, v] of ids) if (v > 1) bad.push(`id "${k}" repetido ${v} veces`);
  const dp = `${T}/config/settings_data.json`;
  if (fs.existsSync(dp)) {
    let dd; try { dd = JSON.parse(read(dp)); } catch (e) { bad.push('settings_data.json invalido'); }
    if (dd && typeof dd.current === 'string') bad.push('settings_data.json: "current" apunta a un preset por nombre');
  }
  return bad;
});

/* 21 — Bloques dentro de {% liquid %}. En el layout tumba la tienda ENTERA. */
check('Bloques dentro de {% liquid %}', () => {
  const MAL = ['comment','endcomment','raw','endraw','schema','style','javascript','stylesheet','form','paginate'];
  const bad = [];
  for (const f of liquids()) {
    const s = read(f);
    for (const m of s.matchAll(/\{%-?\s*liquid\b([\s\S]*?)-?%\}/g))
      for (const kw of MAL)
        if (new RegExp('^\\s*' + kw + '\\b', 'm').test(m[1]))
          bad.push(`${f}:${line(s, m.index)} '${kw}' dentro de {% liquid %}`);
  }
  return bad;
});

/* 22 — Caracteres de riesgo en nombres que el editor lista.
   Una barra en el nombre de un panel dejo "Parametros del tema" en blanco. */
check('Nombres de panel y seccion', () => {
  const MALOS = /[\/\\(){}\[\]<>|"'`#?&=:;*%$@!~^]/;
  const bad = [];
  const scan = (n, w) => {
    if (!n) return;
    const m = [...new Set([...n].filter(c => MALOS.test(c)))];
    if (m.length) bad.push(`${w}: "${n}" contiene ${m.map(c => `"${c}"`).join(', ')}`);
  };
  for (const p of JSON.parse(read(`${T}/config/settings_schema.json`)))
    if (p.name !== 'theme_info') scan(p.name, 'panel');
  for (const f of walk(`${T}/sections`, /\.liquid$/)) {
    const m = read(f).match(/\{%-?\s*schema\s*-?%\}([\s\S]*?)\{%-?\s*endschema\s*-?%\}/);
    if (!m) continue;
    let j; try { j = JSON.parse(m[1]); } catch { continue; }
    scan(j.name, f);
    for (const p of (j.presets || [])) scan(p.name, f + ' (preset)');
  }
  return bad;
});

check('Reglas CSS pisadas por una animacion', () => {
  /* Una @keyframes que anima una propiedad la impone por encima de cualquier
     declaracion normal del mismo selector: esa declaracion queda muerta y el
     efecto que promete no ocurre nunca. Fue el fallo de la flecha del hero,
     cuya opacidad de scroll no se veia porque la animacion tambien la movia. */
  const css = read(`${T}/assets/villumination.css`).replace(/\/\*[\s\S]*?\*\//g, '');
  const kf = {};
  for (const m of css.matchAll(/@keyframes\s+([\w-]+)\s*\{/g)) {
    let depth = 0, end = m.index + m[0].length - 1;
    for (let j = m.index + m[0].length - 1; j < css.length; j++) {
      if (css[j] === '{') depth++;
      else if (css[j] === '}') { depth--; if (depth === 0) { end = j; break; } }
    }
    const props = new Set();
    for (const d of css.slice(m.index + m[0].length, end).matchAll(/(^|[{;\s])([a-z-]+)\s*:/g)) props.add(d[2]);
    kf[m[1]] = props;
  }
  const bySel = {};
  for (const m of css.matchAll(/([^{}@][^{}]*)\{([^{}]*)\}/g)) {
    const decls = {};
    for (const d of m[2].split(';')) { const k = d.indexOf(':'); if (k > 0) decls[d.slice(0, k).trim()] = d.slice(k + 1).trim(); }
    for (const sel of m[1].split(',').map(x => x.trim()).filter(Boolean)) {
      if (/^\d|^(from|to)$/.test(sel)) continue;
      (bySel[sel] = bySel[sel] || []).push(decls);
    }
  }
  const bad = [];
  for (const [sel, list] of Object.entries(bySel)) {
    const animated = new Set();
    for (const d of list) {
      const a = d.animation || d['animation-name'];
      if (!a) continue;
      for (const tok of a.split(/[\s,]+/)) if (kf[tok]) for (const p of kf[tok]) animated.add(p);
    }
    if (!animated.size) continue;
    for (const d of list) {
      if (d.animation || d['animation-name']) continue;
      for (const p of Object.keys(d))
        if (animated.has(p) && !/!important/.test(d[p]))
          bad.push(`${sel} { ${p}: ${d[p].slice(0, 40)} } lo pisa su propia @keyframes`);
    }
  }
  return bad;
});

check('Transform pisado por data-reveal', () => {
  /* .reveal-init.is-visible aplica transform:none con especificidad 0-2-0.
     Cualquier regla de igual o menor peso escrita antes queda anulada mientras
     el elemento conserve reveal-init. Fue el fallo del contenido del hero. */
  const css = read(`${T}/assets/villumination.css`).replace(/\/\*[\s\S]*?\*\//g, '');
  const posReveal = css.indexOf('.reveal-init.is-visible{');
  if (posReveal < 0) return [];
  const spec = sel => (sel.match(/#[\w-]+/g) || []).length * 100
    + (sel.match(/\.[\w-]+|\[[^\]]+\]|:[a-z-]+(?!\()/g) || []).length * 10;
  const rules = [];
  for (const m of css.matchAll(/([^{}@][^{}]*)\{([^{}]*)\}/g)) {
    const decls = {};
    for (const d of m[2].split(';')) { const k = d.indexOf(':'); if (k > 0) decls[d.slice(0, k).trim()] = d.slice(k + 1).trim(); }
    for (const sel of m[1].split(',').map(x => x.trim()).filter(Boolean)) {
      if (/^\d|^(from|to)$/.test(sel)) continue;
      rules.push({ pos: m.index, sel, decls });
    }
  }
  const clases = new Set();
  for (const f of liquids())
    for (const tag of read(f).matchAll(/<\w+\b[^>]*data-reveal[^>]*>/g)) {
      const cm = tag[0].match(/class="([^"]*)"/);
      if (cm) for (const c of cm[1].split(/\s+/)) if (/^[\w-]+$/.test(c)) clases.add(c);
    }
  const bad = [];
  for (const c of clases)
    for (const r of rules) {
      if (!r.sel.startsWith('.' + c)) continue;
      const rest = r.sel.slice(c.length + 1);
      if (/^[\w-]/.test(rest) || /[\s>+~]/.test(rest)) continue;
      for (const p of ['transform', 'opacity']) {
        if (!r.decls[p] || /!important/.test(r.decls[p])) continue;
        const sp = spec(r.sel);
        if (sp < 20 || (sp === 20 && r.pos < posReveal))
          bad.push(`${r.sel} { ${p} } lo anula .reveal-init.is-visible`);
      }
    }
  return [...new Set(bad)];
});

check('Transform declarado dos veces en el mismo selector', () => {
  /* Dos reglas con el MISMO selector que declaran transform: la primera no se
     ve nunca. Suele ser un rediseno a medias que dejo viva la promesa de un
     efecto que ya no ocurre (paso con .btn-primary:hover y .btn-outline:hover,
     donde el scale(1.05) estaba muerto desde hacia rondas). */
  const css = read(`${T}/assets/villumination.css`).replace(/\/\*[\s\S]*?\*\//g, '');
  // Fuera los bloques @: @keyframes tiene pasos "50%" que no son selectores y
  // @media es otro contexto, comparar entre contextos daria falsos positivos.
  const top = [];
  for (let i = 0; i < css.length;) {
    while (i < css.length && /\s/.test(css[i])) i++; // sin esto, un @ precedido de un salto de linea se colaba como selector
    if (css[i] === '@') {
      const j = css.indexOf('{', i);
      if (j < 0) break;
      let d = 0, k = j;
      for (; k < css.length; k++) {
        if (css[k] === '{') d++;
        else if (css[k] === '}') { d--; if (d === 0) break; }
      }
      i = k + 1; continue;
    }
    const j = css.indexOf('{', i);
    if (j < 0) break;
    const close = css.indexOf('}', i);
    if (close >= 0 && close < j) { i = close + 1; continue; }
    const k = css.indexOf('}', j);
    if (k < 0) break;
    top.push([css.slice(i, j), css.slice(j + 1, k)]);
    i = k + 1;
  }
  const bySel = {};
  for (const [group, body] of top) {
    const m = body.match(/(^|;)\s*transform\s*:\s*([^;]+)/);
    if (!m) continue;
    for (const sel of group.split(',').map(x => x.trim()).filter(Boolean))
      (bySel[sel] = bySel[sel] || []).push(m[2].trim());
  }
  const bad = [];
  for (const [sel, vals] of Object.entries(bySel)) {
    if (vals.length < 2) continue;
    for (let i = 0; i < vals.length - 1; i++)
      if (vals[i] !== vals[i + 1] && !/!important/.test(vals[i]))
        bad.push(`${sel}: "${vals[i].slice(0, 38)}" no se ve, lo redefine "${vals[i + 1].slice(0, 38)}"`);
  }
  return bad;
});

check('Clases usadas dentro de las traducciones', () => {
  /* Los textos de locales/ pueden traer HTML con clases propias (por ejemplo
     el resalte del mensaje de envio gratis). Como esas clases no aparecen en
     ningun .liquid, un barrido de clases huerfanas las da por muertas y se
     borran sin querer: paso de verdad con .cart-ship-hl. Aqui se comprueba al
     reves — que toda clase citada en una traduccion siga teniendo estilo. */
  const css = read(`${T}/assets/villumination.css`);
  const bad = [];
  for (const f of walk(`${T}/locales`, /\.json$/)) {
    const crudo = read(f);
    for (const m of crudo.matchAll(/class=\\?"([^"\\]+)\\?"/g))
      for (const c of m[1].trim().split(/\s+/)) {
        if (!/^[A-Za-z][\w-]*$/.test(c)) continue;
        if (!new RegExp(`\\.${c}(?![\\w-])`).test(css))
          bad.push(`${f}: la traduccion usa .${c} y el CSS no la define`);
      }
  }
  return [...new Set(bad)];
});

check('Esquemas que dejarian el editor en blanco', () => {
  /* Reglas que Shopify aplica en silencio: si alguna falla no da error, se
     limita a no pintar el panel. Asi fue como "Parametros del tema" aparecio
     entero en blanco durante varias rondas por una simple barra en un nombre.
     Se revisan aqui los ajustes globales y los de las 44 secciones. */
  const bad = [];
  const RIESGO = /[/\\<>{}"\[\]\n\r\t]/g;
  const VALIDOS = new Set(['text','textarea','number','range','checkbox','radio','select','color',
    'color_background','font_picker','collection','collection_list','product','product_list','blog',
    'page','link_list','url','video','video_url','richtext','inline_richtext','html','article',
    'image_picker','liquid','header','paragraph','color_scheme','color_scheme_group','metaobject',
    'text_alignment']);

  const revisar = (lista, donde) => {
    const vistos = new Set();
    for (const s of lista || []) {
      const t = s.type;
      if (!VALIDOS.has(t)) bad.push(`${donde}: tipo desconocido "${t}"`);
      if (t === 'header' || t === 'paragraph') {
        if ('id' in s) bad.push(`${donde}: ${t} no debe llevar id`);
        continue;
      }
      if (!s.id) { bad.push(`${donde}: ajuste ${t} sin id`); continue; }
      if (!/^[a-z0-9_]+$/.test(s.id)) bad.push(`${donde}: id con formato invalido "${s.id}"`);
      if (vistos.has(s.id)) bad.push(`${donde}: id repetido "${s.id}"`);
      vistos.add(s.id);
      if (t === 'range') {
        const { min: mn, max: mx } = s, st = s.step === undefined ? 1 : s.step;
        if (mn === undefined || mx === undefined) bad.push(`${donde}: range "${s.id}" sin min/max`);
        else if (!(st > 0) || Math.abs(((mx - mn) / st) % 1) > 1e-6)
          bad.push(`${donde}: range "${s.id}" (max-min)/step no es entero`);
        else if (s.default === undefined) bad.push(`${donde}: range "${s.id}" sin default`);
        else if (s.default < mn || s.default > mx) bad.push(`${donde}: range "${s.id}" default fuera de rango`);
        else if ((mx - mn) / st > 100) bad.push(`${donde}: range "${s.id}" con mas de 101 pasos`);
        else if (Math.abs(((s.default - mn) / st) % 1) > 1e-9) {
          // Shopify exige que el default caiga EXACTAMENTE en un paso, no solo
          // dentro del rango: "default doit etre une etape dans la plage".
          // Si no, rechaza el archivo entero de la seccion sin avisar, y
          // cualquier plantilla que la use se cae con ella. Asi es como la
          // portada acabo sirviendo un 404: el hero tenia default 126 en un
          // rango de 80 a 200 de cinco en cinco.
          const cerca = mn + Math.round((s.default - mn) / st) * st;
          bad.push(`${donde}: range "${s.id}" default ${s.default} no cae en un paso (min ${mn}, step ${st}) -> usa ${cerca}`);
        }
      }
      if (t === 'select' || t === 'radio') {
        const vals = (s.options || []).map(o => o.value);
        if (!vals.length) bad.push(`${donde}: ${t} "${s.id}" sin opciones`);
        else if ('default' in s && !vals.includes(s.default))
          bad.push(`${donde}: ${t} "${s.id}" default fuera de las opciones`);
      }
    }
    return vistos;
  };

  // --- ajustes globales ---
  const glob = JSON.parse(read(`${T}/config/settings_schema.json`));
  if (glob[0] && glob[0].name !== 'theme_info') bad.push('settings_schema: theme_info no es el primer panel');
  const idsGlob = new Set(), nombres = new Set();
  for (const p of glob) {
    if (p.name === 'theme_info') continue;
    if (!p.name) { bad.push('settings_schema: panel sin nombre'); continue; }
    const m = p.name.match(RIESGO);
    if (m) bad.push(`settings_schema: panel "${p.name}" contiene ${m.join(' ')}`);
    if (nombres.has(p.name)) bad.push(`settings_schema: panel repetido "${p.name}"`);
    nombres.add(p.name);
    for (const id of revisar(p.settings, `panel "${p.name}"`)) {
      // los ids globales tienen que ser unicos en TODO el archivo, no solo por panel
      if (idsGlob.has(id)) bad.push(`settings_schema: id "${id}" repetido entre paneles`);
      idsGlob.add(id);
    }
  }

  // --- esquemas de seccion ---
  for (const f of walk(`${T}/sections`, /\.liquid$/)) {
    const m = read(f).match(/\{%-?\s*schema\s*-?%\}([\s\S]*?)\{%-?\s*endschema\s*-?%\}/);
    if (!m) continue;
    let j; try { j = JSON.parse(m[1]); } catch (e) { bad.push(`${f}: schema con JSON invalido`); continue; }
    if (!j.name) bad.push(`${f}: seccion sin name`);
    else {
      if (j.name.length > 25) bad.push(`${f}: name de ${j.name.length} caracteres, Shopify corta en 25`);
      const mm = j.name.match(RIESGO);
      if (mm) bad.push(`${f}: name contiene ${mm.join(' ')}`);
    }
    revisar(j.settings, f);
    const tipos = new Set();
    for (const b of j.blocks || []) {
      if (tipos.has(b.type)) bad.push(`${f}: tipo de bloque repetido "${b.type}"`);
      tipos.add(b.type);
      // @app y @theme son bloques especiales de Shopify: no llevan name ni settings
      if (b.type !== '@app' && b.type !== '@theme') {
        if (!b.name) bad.push(`${f}: bloque "${b.type}" sin name`);
        revisar(b.settings, `${f} bloque ${b.type}`);
      }
    }
    for (const pr of j.presets || [])
      for (const pb of (Array.isArray(pr.blocks) ? pr.blocks : []))
        if (pb.type && !tipos.has(pb.type)) bad.push(`${f}: preset usa el bloque inexistente "${pb.type}"`);
  }
  return bad;
});

/* ---------------- informe ---------------- */
let fails = 0;
console.log('');
for (const r of results) {
  const ok = r.problems.length === 0;
  if (!ok) fails++;
  console.log(`${ok ? ' OK ' : 'FALLA'}  ${r.name}${ok ? '' : `  (${r.problems.length})`}`);
  for (const p of r.problems.slice(0, 12)) console.log(`        ${p}`);
  if (r.problems.length > 12) console.log(`        ... y ${r.problems.length - 12} mas`);
}
console.log('');
console.log(fails === 0
  ? `Las ${results.length} comprobaciones en verde.`
  : `${fails} de ${results.length} comprobaciones con problemas.`);
process.exit(fails === 0 ? 0 : 1);
