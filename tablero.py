#!/usr/bin/env python3
"""
VILLUMINATIONS — Tablero
------------------------
Una sola página que enseña el estado real del sistema: lo que hay compuesto,
lo que se vende, en cuántas lenguas habla cada cosa y qué forma tiene el grafo
de conocimiento.

No se escribe a mano. Se genera desde el repositorio:

    python3 tablero.py            # escribe tablero/index.html

Lo que sale del repositorio se lee del repositorio. Lo que solo vive en la
tienda —los menús, las traducciones registradas, las políticas— no se puede
consultar sin credenciales, así que va en TIENDA con la fecha en que se
comprobó. Si la fecha se queda vieja, el tablero lo dice él mismo en vez de
fingir que sabe.

La paleta no es nueva: son los mismos tokens de `planes/assets/brand.css`, que
a su vez salieron del tema de la tienda. Un tablero con colores propios sería
un cuarto sistema de diseño.
"""

from __future__ import annotations

import html
import json
import math
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
SALIDA = RAIZ / "tablero" / "index.html"

# ---------------------------------------------------------------------------
# Estado de la tienda, comprobado contra la API y fechado
# ---------------------------------------------------------------------------
# Esto no se puede deducir del repositorio: vive en Shopify. Se anota aquí con
# la fecha de la comprobación y el tablero avisa cuando envejece.
TIENDA = {
    "comprobado": "2026-08-15",
    "dominio": "villuminations.com",
    "moneda": "CAD",
    "idioma_primario": "es",
    "idiomas_publicados": ["es", "en", "fr", "de", "ja"],
    "idiomas_traducidos": ["es", "en", "fr"],
    "canales": ["Tienda en línea", "Shop", "Punto de venta", "Google & YouTube"],
    "colecciones": {
        "suplementos": 10, "equipo": 13, "ropa": 4,
        "conocimiento": 8, "planes": 3, "cuidado-personal": 2,
    },
    "menu_principal": [
        "Inicio", "Libros y planes", "Suplementos", "Equipo", "Ropa",
        "Diario", "VI.P", "Todo el catálogo",
    ],
    "menu_pie": [
        "Cómo se hace lo que vendemos", "Diario", "Contacto", "Buscar",
        "Política de privacidad", "Política de reembolso",
        "Condiciones del servicio", "Envíos", "Aviso legal",
        "Tus opciones de privacidad",
    ],
}

# Qué habla tres lenguas y qué no. (concepto, alcance, es, en, fr, nota)
LENGUAS = [
    ("Fichas propias", "11 productos", 1, 1, 1, "título, cuerpo, SEO y handle"),
    ("Títulos de proveedor", "29 productos", 1, 1, 1, ""),
    ("Metaetiquetas de proveedor", "29 productos", 1, 1, 1, "lo que enseña el buscador"),
    ("Cuerpos de proveedor", "29 productos", 1, 0, 0, "el tramo grande que queda"),
    ("Colecciones", "6", 1, 1, 1, "título, cuerpo, SEO y handle"),
    ("Menús", "18 enlaces", 1, 1, 1, ""),
    ("Diario (el blog)", "título y SEO", 1, 1, 1, ""),
    ("Artículos del Diario", "8", 1, 0, 0, "escritos en castellano"),
    ("Página «Cómo se hace»", "1", 1, 0, 0, ""),
    ("Página «Contacto»", "1", 1, 1, 1, ""),
    ("Políticas de la tienda", "6", 0, 1, 0, "redactadas en inglés; falta permiso de API"),
]

# Las guardas que se niegan a construir. Están en el código; aquí solo se listan.
GUARDAS = [
    ("Cobertura < 100 %", "libros/tools/cargar-traducciones.py",
     "Un libro medio traducido. Sale «Incompleto» y no se escribe el PDF."),
    ("Ancho de lámina", "libros/tools/cargar-traducciones.py",
     "Una etiqueta traducida que no cabe y rompe el dibujo."),
    ("comprobar_laminas()", "libros/build.py",
     "Que la prosa prometa siete láminas y haya seis. Pasó, en tres idiomas."),
    ("datos_oficiales.comprobar()", "libros/datos_oficiales.py",
     "Que una tabla no cuadre con su fuente."),
]

# Lo que no se puede hacer por API y espera al dueño en el panel.
PENDIENTE = [
    ("App de descargas digitales",
     "Once productos cobran y no entregan el archivo. Los 13 paquetes ZIP "
     "están hechos y esperan a que la app los reciba.", "bloquea ventas"),
    ("El nombre de la cuenta sigue siendo «VIllumination»",
     "Sale en la pestaña del navegador, en el pago y en cada correo. "
     "Ajustes → Detalles de la tienda.", "marca"),
    ("Políticas en inglés y con huecos sin rellenar",
     "Las condiciones del servicio llevan literales «[INSERT TRADING NAME]» "
     "a la vista, y todas escriben mal la marca. La API rechaza el cambio: "
     "pide el permiso write_legal_policies.", "confianza"),
    ("Precio provisional de 9,99 CAD",
     "En los seis libros nuevos.", "decisión"),
    ("Los dos jabones siguen sin publicar",
     "Piden envío y no llevan control de existencias: activarlos significa "
     "poder vender sin stock.", "decisión"),
]

PALETA = ["#00f0ff", "#ff00e5", "#00ff88", "#ff6600", "#ffdd00",
          "#7b2fff", "#00ffcc", "#ff3cac", "#00c8ff", "#a97bff"]


# ---------------------------------------------------------------------------
# Lectura del repositorio
# ---------------------------------------------------------------------------
def _texto(orden: list[str]) -> str:
    try:
        return subprocess.run(orden, cwd=RAIZ, capture_output=True,
                              text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def catalogo() -> dict:
    sys.path.insert(0, str(RAIZ / "tienda"))
    datos = {"fichas": 0, "metas": 0, "articulos": 0, "fuera": []}
    try:
        import catalogo as c
        datos["fichas"] = len(c.FICHAS)
        datos["metas"] = len(getattr(c, "METAS", {}))
        datos["fuera"] += c.comprobar()
    except Exception as e:                                   # pragma: no cover
        datos["fuera"].append(f"catalogo.py no se pudo leer: {e}")
    try:
        import articulos as a
        datos["articulos"] = len(a.ARTICULOS)
        datos["fuera"] += a.comprobar()
    except Exception as e:                                   # pragma: no cover
        datos["fuera"].append(f"articulos.py no se pudo leer: {e}")
    try:
        import seo
        datos["propios"] = len(seo.FICHAS)
        datos["fuera"] += seo.comprobar()
    except Exception:
        datos["propios"] = 11
    return datos


def documentos() -> dict:
    """Cuenta PDFs compuestos y sus páginas, por idioma."""
    salida = {}
    for nombre, base in (("libros", RAIZ / "libros" / "dist"),
                         ("planes", RAIZ / "planes" / "dist")):
        por_lengua = {}
        for lengua, carpeta in (("es", base), ("en", base / "en"), ("fr", base / "fr")):
            if carpeta.is_dir():
                pdfs = sorted(carpeta.glob("*.pdf"))
                por_lengua[lengua] = len(pdfs)
        salida[nombre] = por_lengua
    return salida


def grafo() -> dict | None:
    ruta = RAIZ / "graphify-out" / "graph.json"
    if not ruta.is_file():
        return None
    g = json.loads(ruta.read_text(encoding="utf-8"))
    nodos = g["nodes"]
    indice = {n["id"]: n for n in nodos}
    enlaces, sueltos = [], 0
    for l in g["links"]:
        if l["source"] in indice and l["target"] in indice:
            enlaces.append(l)
        else:
            sueltos += 1
    grados = {n["id"]: 0 for n in nodos}
    for l in enlaces:
        grados[l["source"]] += 1
        grados[l["target"]] += 1
    return {
        "nodos": nodos, "enlaces": enlaces, "indice": indice, "grados": grados,
        "sueltos": sueltos, "hiperaristas": len(g.get("hyperedges", [])),
        "commit": g.get("built_at_commit", "")[:7],
        "deducidos": sum(1 for n in nodos if n.get("_origin") != "ast"),
    }


# ---------------------------------------------------------------------------
# Dibujo del grafo
# ---------------------------------------------------------------------------
def disponer(g: dict, ancho: int = 1180, alto: int = 720) -> tuple[dict, list]:
    """Coloca cada comunidad en su propio disco y los nodos dentro en espiral.

    No es un force-directed: con mil nodos y sin numpy tardaría más de lo que
    vale. Lo que interesa ver aquí es la estructura de comunidades y qué
    enlaces las cruzan, y eso esta disposición lo enseña mejor que una nube.
    """
    comunidades: dict[str, list] = {}
    for n in g["nodos"]:
        comunidades.setdefault(n.get("community_name") or "sin comunidad", []).append(n)
    orden = sorted(comunidades.items(), key=lambda kv: -len(kv[1]))

    cx, cy = ancho / 2, alto / 2
    radio_max = min(ancho, alto) / 2 - 40
    aureo = math.pi * (3 - math.sqrt(5))

    pos, leyenda = {}, []
    for i, (nombre, miembros) in enumerate(orden):
        # Espiral de Vogel para los centros: reparte sin apelmazar el medio.
        t = (i + 0.5) / max(len(orden), 1)
        r = radio_max * math.sqrt(t)
        ang = i * aureo
        ccx, ccy = cx + r * math.cos(ang), cy + r * math.sin(ang)
        radio = 4 + 3.4 * math.sqrt(len(miembros))
        color = PALETA[i % len(PALETA)]
        if i < 10:
            leyenda.append((nombre, len(miembros), color))
        for j, n in enumerate(sorted(miembros, key=lambda m: -g["grados"][m["id"]])):
            tt = (j + 0.5) / len(miembros)
            rr = radio * math.sqrt(tt)
            aa = j * aureo
            pos[n["id"]] = (ccx + rr * math.cos(aa), ccy + rr * math.sin(aa), color)
    return pos, leyenda


def svg_grafo(g: dict) -> str:
    ancho, alto = 1180, 720
    pos, leyenda = disponer(g, ancho, alto)
    partes = [
        f'<svg viewBox="0 0 {ancho} {alto}" class="grafo" role="img" '
        f'aria-label="Grafo de conocimiento: {len(g["nodos"])} nodos '
        f'agrupados en comunidades">'
    ]

    dentro, fuera = [], []
    for l in g["enlaces"]:
        x1, y1, c1 = pos[l["source"]]
        x2, y2, c2 = pos[l["target"]]
        (dentro if c1 == c2 else fuera).append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')

    partes.append('<g class="aristas-dentro">' + "".join(dentro) + "</g>")
    partes.append('<g class="aristas-fuera">' + "".join(fuera) + "</g>")

    puntos = []
    for n in g["nodos"]:
        x, y, color = pos[n["id"]]
        r = 1.5 + min(g["grados"][n["id"]], 22) * 0.16
        puntos.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{color}"/>')
    partes.append('<g class="nodos">' + "".join(puntos) + "</g>")
    partes.append("</svg>")

    filas = "".join(
        f'<li><span class="punto" style="background:{c}"></span>'
        f'<span class="com">{html.escape(nombre)}</span>'
        f'<span class="num">{n}</span></li>'
        for nombre, n, c in leyenda)
    return "".join(partes), f'<ul class="leyenda">{filas}</ul>'


# ---------------------------------------------------------------------------
# Página
# ---------------------------------------------------------------------------
def marca(v: int) -> str:
    return ('<span class="si" title="registrado">●</span>' if v
            else '<span class="no" title="falta">○</span>')


def construir() -> str:
    cat = catalogo()
    docs = documentos()
    g = grafo()
    commit = _texto(["git", "rev-parse", "--short", "HEAD"]) or "—"
    hoy = date.today().isoformat()
    dias = (date.fromisoformat(hoy) - date.fromisoformat(TIENDA["comprobado"])).days

    libros_es = docs["libros"].get("es", 0)
    planes_es = docs["planes"].get("es", 0)
    total_pdf = sum(sum(v.values()) for v in docs.values())

    tiles = [
        ("Productos propios", cat.get("propios", 11),
         f"{libros_es} libros y 3 niveles de planes"),
        ("De proveedor", cat["fichas"], "fichas reescritas en castellano"),
        ("Artículos del Diario", cat["articulos"], "con su fuente en el texto"),
        ("PDF compuestos", total_pdf,
         f"{libros_es + planes_es} documentos × 3 lenguas"),
    ]
    if g:
        tiles.append(("Nodos del grafo", len(g["nodos"]),
                      f'{len(g["enlaces"])} relaciones · {g["hiperaristas"]} hiperaristas'))

    tiles_html = "".join(
        f'<article class="tile"><p class="rotulo">{html.escape(t)}</p>'
        f'<p class="cifra">{v}</p><p class="pie">{html.escape(p)}</p></article>'
        for t, v, p in tiles)

    lenguas_html = "".join(
        f"<tr><th scope=\"row\">{html.escape(q)}</th><td>{html.escape(alc)}</td>"
        f"<td>{marca(es)}</td><td>{marca(en)}</td><td>{marca(fr)}</td>"
        f"<td class=\"nota\">{html.escape(nota)}</td></tr>"
        for q, alc, es, en, fr, nota in LENGUAS)

    guardas_html = "".join(
        f'<li><p class="guarda">{html.escape(n)}</p>'
        f'<p class="donde">{html.escape(d)}</p>'
        f'<p class="que">{html.escape(q)}</p></li>'
        for n, d, q in GUARDAS)

    pend_html = "".join(
        f'<li><span class="etiqueta e-{i}">{html.escape(tipo)}</span>'
        f'<p class="asunto">{html.escape(t)}</p>'
        f'<p class="detalle">{html.escape(d)}</p></li>'
        for i, (t, d, tipo) in enumerate(PENDIENTE))

    if g:
        dibujo, leyenda = svg_grafo(g)
        # La salud del grafo se dice, no se esconde: hubo una época con 116
        # aristas colgando y el tablero las enseñaba.
        salud = (f' Quedan {g["sueltos"]} relaciones apuntando a un extremo que '
                 f'ya no existe.' if g["sueltos"] else
                 ' Ninguna relación apunta a un extremo que ya no exista.')
        nota_grafo = (
            f'<p class="apunte">Cada disco es una comunidad detectada; el tamaño '
            f'del punto es el número de relaciones que tiene ese nodo. Las líneas '
            f'claras cruzan de una comunidad a otra y son las interesantes: ahí es '
            f'donde el repositorio se ata consigo mismo. '
            f'{g["deducidos"]} de los {len(g["nodos"])} nodos no salen del código '
            f'sino de la lectura de documentos.{salud}</p>')
    else:
        dibujo = ('<p class="ausente">No hay grafo construido. '
                  '<code>graphify update .</code> lo rehace.</p>')
        leyenda, nota_grafo = "", ""

    fuera = cat["fuera"]
    estado = ('<p class="ok">Las medidas de buscador cuadran: '
              'ningún título pasa de 60 caracteres ni ninguna descripción de 155.</p>'
              if not fuera else
              '<ul class="mal">' + "".join(
                  f"<li>{html.escape(x)}</li>" for x in fuera) + "</ul>")

    aviso = ""
    if dias > 21:
        aviso = (f'<p class="rancio">El estado de la tienda se comprobó hace '
                 f'{dias} días. Lo de abajo puede haber cambiado.</p>')

    return PLANTILLA.format(
        commit=html.escape(commit),
        grafo_commit=html.escape(g["commit"] if g else "—"),
        hoy=hoy,
        dominio=TIENDA["dominio"],
        tiles=tiles_html,
        lenguas=lenguas_html,
        guardas=guardas_html,
        pendientes=pend_html,
        dibujo=dibujo,
        leyenda=leyenda,
        nota_grafo=nota_grafo,
        estado=estado,
        aviso=aviso,
        menu=" · ".join(html.escape(x) for x in TIENDA["menu_principal"]),
        pie=" · ".join(html.escape(x) for x in TIENDA["menu_pie"]),
        canales=" · ".join(html.escape(x) for x in TIENDA["canales"]),
        comprobado=TIENDA["comprobado"],
    )


PLANTILLA = """<title>Tablero VILLUMINATIONS</title>
<style>
  /* Un solo mundo visual, a propósito: los mismos tokens neón que usan los
     PDF y el tema de la tienda. Todo color se declara aquí, así que la página
     no toma prestado nada del fondo del visor. */
  :root {{
    --bg:#050510; --bg-2:#0a0a1a; --panel:rgba(15,15,42,.62);
    --linea:rgba(255,255,255,.10); --linea-2:rgba(255,255,255,.16);
    --ink:#eef2ff; --ink-2:#c3cbe4; --ink-3:#8b95b5;
    --cyan:#00f0ff; --magenta:#ff00e5; --verde:#00ff88;
    --naranja:#ff6600; --amarillo:#ffdd00; --purpura:#7b2fff;
    --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:var(--sans); line-height:1.6;
    background-image:
      radial-gradient(120% 70% at 50% -10%, rgba(0,240,255,.10) 0%, transparent 60%),
      radial-gradient(90% 50% at 50% 108%, rgba(255,0,229,.08) 0%, transparent 62%);
    background-attachment:fixed;
  }}
  .envoltura {{ max-width:1240px; margin:0 auto; padding:clamp(20px,4vw,52px) clamp(16px,3vw,32px) 72px; }}

  header.cabecera {{ display:flex; flex-wrap:wrap; gap:16px 28px; align-items:baseline;
    border-bottom:1px solid var(--linea-2); padding-bottom:20px; }}
  .marca {{ font-family:var(--mono); font-size:clamp(20px,3.2vw,30px); font-weight:700;
    letter-spacing:.20em; color:var(--ink); margin:0; }}
  .marca span {{ color:var(--cyan); }}
  .sello {{ font-family:var(--mono); font-size:12px; color:var(--ink-3);
    letter-spacing:.06em; margin:0; display:flex; gap:14px; flex-wrap:wrap; }}
  .sello b {{ color:var(--ink-2); font-weight:500; }}

  h2 {{ font-family:var(--mono); font-size:13px; font-weight:600; letter-spacing:.20em;
    text-transform:uppercase; color:var(--cyan); margin:0 0 14px;
    text-wrap:balance; }}
  section {{ margin-top:clamp(34px,5vw,58px); }}
  p {{ margin:0 0 10px; }}

  .rejilla {{ display:grid; gap:14px;
    grid-template-columns:repeat(auto-fit,minmax(178px,1fr)); }}
  .tile {{ background:var(--panel); border:1px solid var(--linea);
    border-radius:4px; padding:16px 18px; }}
  .rotulo {{ font-family:var(--mono); font-size:11px; letter-spacing:.14em;
    text-transform:uppercase; color:var(--ink-3); margin:0; }}
  .cifra {{ font-family:var(--mono); font-size:38px; font-weight:700; line-height:1.1;
    margin:6px 0 4px; color:var(--ink); font-variant-numeric:tabular-nums; }}
  .pie {{ font-size:13px; color:var(--ink-2); margin:0; }}

  .marco {{ background:var(--panel); border:1px solid var(--linea);
    border-radius:4px; padding:clamp(14px,2.4vw,24px); }}
  .grafo {{ width:100%; height:auto; display:block; }}
  .aristas-dentro line {{ stroke:rgba(255,255,255,.055); stroke-width:.5; }}
  .aristas-fuera line {{ stroke:rgba(0,240,255,.20); stroke-width:.6; }}
  .nodos circle {{ opacity:.92; }}
  .leyenda {{ list-style:none; margin:18px 0 0; padding:0; display:grid; gap:6px 22px;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); }}
  .leyenda li {{ display:flex; align-items:center; gap:9px; font-size:13px;
    color:var(--ink-2); }}
  .punto {{ width:9px; height:9px; border-radius:50%; flex:0 0 auto; }}
  .com {{ overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
  .num {{ margin-left:auto; font-family:var(--mono); font-size:12px;
    color:var(--ink-3); font-variant-numeric:tabular-nums; }}
  .apunte {{ font-size:14px; color:var(--ink-2); margin:16px 0 0; max-width:70ch; }}
  .ausente {{ color:var(--ink-3); font-family:var(--mono); font-size:13px; }}

  .tabla-envoltura {{ overflow-x:auto; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; min-width:640px; }}
  th, td {{ text-align:left; padding:9px 12px; border-bottom:1px solid var(--linea);
    vertical-align:top; }}
  thead th {{ font-family:var(--mono); font-size:11px; letter-spacing:.12em;
    text-transform:uppercase; color:var(--ink-3); font-weight:500;
    border-bottom-color:var(--linea-2); }}
  tbody th {{ font-weight:600; color:var(--ink); }}
  td {{ color:var(--ink-2); }}
  .nota {{ color:var(--ink-3); font-size:13px; }}
  .si {{ color:var(--verde); font-size:15px; }}
  .no {{ color:var(--naranja); font-size:15px; }}

  .lista {{ list-style:none; margin:0; padding:0; display:grid; gap:12px;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); }}
  .lista li {{ background:var(--panel); border:1px solid var(--linea);
    border-left:2px solid var(--cyan); border-radius:3px; padding:14px 16px; }}
  .guarda {{ font-family:var(--mono); font-size:13px; color:var(--ink); margin:0 0 4px; }}
  .donde {{ font-family:var(--mono); font-size:11px; color:var(--ink-3); margin:0 0 8px;
    word-break:break-all; }}
  .que {{ font-size:13.5px; color:var(--ink-2); margin:0; }}

  ol.espera {{ list-style:none; margin:0; padding:0; display:grid; gap:12px; }}
  ol.espera li {{ background:var(--panel); border:1px solid var(--linea);
    border-radius:3px; padding:14px 16px; }}
  .etiqueta {{ display:inline-block; font-family:var(--mono); font-size:10px;
    letter-spacing:.14em; text-transform:uppercase; padding:2px 8px;
    border-radius:2px; margin-bottom:8px; }}
  .e-0 {{ background:rgba(255,102,0,.16); color:var(--naranja); }}
  .e-1 {{ background:rgba(255,0,229,.14); color:var(--magenta); }}
  .e-2 {{ background:rgba(255,221,0,.14); color:var(--amarillo); }}
  .e-3, .e-4 {{ background:rgba(123,47,255,.20); color:#c4a6ff; }}
  .asunto {{ font-weight:600; margin:0 0 4px; }}
  .detalle {{ font-size:13.5px; color:var(--ink-2); margin:0; max-width:74ch; }}

  .ok {{ font-size:14px; color:var(--verde); font-family:var(--mono); margin:0; }}
  .mal {{ margin:0; padding-left:20px; color:var(--naranja); font-size:14px; }}
  .rancio {{ font-family:var(--mono); font-size:13px; color:var(--amarillo);
    border:1px solid rgba(255,221,0,.3); border-radius:3px; padding:10px 14px; }}
  .navegacion {{ font-size:14px; color:var(--ink-2); max-width:80ch; }}
  .navegacion b {{ font-family:var(--mono); font-size:11px; letter-spacing:.12em;
    text-transform:uppercase; color:var(--ink-3); font-weight:500;
    display:block; margin-bottom:2px; }}

  footer {{ margin-top:56px; padding-top:18px; border-top:1px solid var(--linea);
    font-family:var(--mono); font-size:11.5px; color:var(--ink-3);
    letter-spacing:.04em; }}
  a {{ color:var(--cyan); }}
  code {{ font-family:var(--mono); font-size:.92em; color:var(--ink-2); }}
</style>

<div class="envoltura">
  <header class="cabecera">
    <h1 class="marca">VILL<span>UMIN</span>ATIONS</h1>
    <p class="sello">
      <span>{dominio}</span>
      <span>rama <b>claude/shopify-diet-plans-9k0wti</b></span>
      <span>código <b>{commit}</b></span>
      <span>grafo <b>{grafo_commit}</b></span>
      <span>generado <b>{hoy}</b></span>
    </p>
  </header>

  <section>
    <h2>Lo que hay</h2>
    <div class="rejilla">{tiles}</div>
  </section>

  <section>
    <h2>El grafo de conocimiento</h2>
    <div class="marco">
      {dibujo}
      {leyenda}
    </div>
    {nota_grafo}
  </section>

  <section>
    <h2>Qué habla tres lenguas y qué no</h2>
    {aviso}
    <div class="tabla-envoltura">
      <table>
        <thead><tr>
          <th scope="col">Qué</th><th scope="col">Alcance</th>
          <th scope="col">ES</th><th scope="col">EN</th><th scope="col">FR</th>
          <th scope="col">Nota</th>
        </tr></thead>
        <tbody>{lenguas}</tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Cómo se llega a cada cosa</h2>
    <p class="navegacion"><b>Menú principal</b>{menu}</p>
    <p class="navegacion"><b>Pie de página</b>{pie}</p>
    <p class="navegacion"><b>Canales de venta</b>{canales}</p>
  </section>

  <section>
    <h2>Las guardas que se niegan a construir</h2>
    <ul class="lista">{guardas}</ul>
  </section>

  <section>
    <h2>Medidas de buscador</h2>
    {estado}
  </section>

  <section>
    <h2>Lo que espera al dueño en el panel</h2>
    <ol class="espera">{pendientes}</ol>
  </section>

  <footer>
    Generado por <code>tablero.py</code> desde el repositorio · estado de la
    tienda comprobado el {comprobado} · el texto de los libros y los planes no
    se edita a mano: vive en <code>libros/src</code> y <code>planes/src</code>.
  </footer>
</div>
"""


if __name__ == "__main__":
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(construir(), encoding="utf-8")
    kb = SALIDA.stat().st_size / 1024
    print(f"\n  {SALIDA.relative_to(RAIZ)} · {kb:.0f} KB\n")
