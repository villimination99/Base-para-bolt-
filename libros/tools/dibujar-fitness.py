#!/usr/bin/env python3
"""
CÓDICES DE FITNESS — generador del repertorio gráfico
=====================================================
Escribe cuatro sprites de una vez: mesa.svg, carga.svg, voluntad.svg y
descanso.svg. Dibujo original de VILLUMINATION 99.

Un solo generador para los cuatro libros porque comparten todo el andamiaje
—barras, ejes, silueta, bisel de cubierta— y tenerlo cuatro veces sería tenerlo
cuatro veces mal. Lo que cambia entre libros es el acento y los datos.

Los datos vienen de tools/datos_oficiales.py y NO se teclean aquí. Ese módulo
se comprueba antes de dibujar: si una tabla no cuadra, no se escribe nada.

    python3 tools/dibujar-fitness.py
"""

import importlib.util
import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "datos_oficiales", Path(__file__).with_name("datos_oficiales.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)

CLARO = "#c9cfe0"
APAGADO = "#8a93ab"
ALERTA = "#ff7a7a"          # se reserva para límites y avisos

ACENTOS = {                 # libro: (principal, secundario)
    "mesa":     ("#00ff88", "#ffd75c"),
    "carga":    ("#ff7a3c", "#ffd75c"),
    "voluntad": ("#ff4fd8", "#5cd6ff"),
    "descanso": ("#00e5c0", "#a97bff"),
}

MITAD = ("M72 30 L52 36 L42 44 L36 74 L30 114 L35 120 L43 80 L49 50 "
         "L47 96 L43 128 L39 180 L43 197 L41 243 L53 248 L55 243 "
         "L59 197 L63 151 L72 139")


# ── Utilidades ────────────────────────────────────────────────────────
def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, g):
    a = math.radians(g - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def txt(x, y, s, clase="et", tam=11, color=CLARO, anchor="middle"):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}">{s}</text>')


def barra(x, y, w, h, color, op=".22", borde=True, rx=3):
    p = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(max(w, 0.5))}" '
         f'height="{f(h)}" rx="{rx}" fill="{color}" opacity="{op}"/>']
    if borde:
        p.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(max(w, 0.5))}" '
                 f'height="{f(h)}" rx="{rx}" fill="none" stroke="{color}" '
                 'stroke-width=".8" opacity=".6"/>')
    return "".join(p)


def flecha(x, y, ang, lado=8, color=CLARO):
    return (f'<g transform="translate({f(x)},{f(y)}) rotate({f(ang)})" '
            f'fill="{color}"><path d="M{f(lado)} 0 L{f(-lado*.6)} {f(lado*.62)} '
            f'L{f(-lado*.6)} {f(-lado*.62)} Z"/></g>')


def pie(ancho, alto, texto, color=APAGADO):
    return txt(ancho / 2, alto - 4, texto, "rot", 7.8, color)


def simbolo_cubierta(clave, cuerpo):
    """Bisel común de cubierta: la colección se lee como serie."""
    p = [f'<symbol id="r-{clave}" viewBox="0 0 240 240">',
         '<circle cx="120" cy="120" r="112" fill="none" stroke="var(--acento)" '
         'stroke-width="1.2" opacity=".32"/>',
         '<circle cx="120" cy="120" r="102" fill="none" stroke="var(--acento)" '
         'stroke-width="2.4" opacity=".85"/>']
    marcas = []
    for k in range(36):
        largo = 11 if k % 9 == 0 else 6
        x1, y1 = pol(120, 120, 102, k * 10)
        x2, y2 = pol(120, 120, 102 - largo, k * 10)
        marcas.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    p.append(f'<path d="{" ".join(marcas)}" fill="none" stroke="var(--acento)" '
             'stroke-width="1.2" opacity=".5"/>')
    p.append(cuerpo)
    p.append("</symbol>")
    return "".join(p)


def sprite(clave, piezas):
    pri, sec = ACENTOS[clave]
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'style="position:absolute;width:0;height:0;overflow:hidden" '
        'aria-hidden="true">',
        f"""
<!-- ════════════════════════════════════════════════════════════════
     CÓDICE · {clave.upper()} · repertorio gráfico
     Dibujo original de VILLUMINATION 99 — generado por
     tools/dibujar-fitness.py. No editar a mano.
     Los datos vienen de tools/datos_oficiales.py y se comprueban.
     ════════════════════════════════════════════════════════════ -->""",
        "<style>"
        "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
        " letter-spacing:.1em }"
        "svg .num{ font-family:'Orbitron',sans-serif; font-weight:600 }"
        "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
        "</style>",
        *piezas,
        "</svg>",
    ]) + "\n"


# ══════════════════════════════════════════════════════════════════════
#  CÓDICE DE LA MESA
# ══════════════════════════════════════════════════════════════════════
def me_amdr():
    """Los tres rangos aceptables, dibujados a escala sobre el 100 %."""
    PRI, SEC = ACENTOS["mesa"]
    # El raíl de la izquierda tiene que caber el nombre más largo escrito en
    # Orbitron a 9,6: con X0 en 156 quedan 142 unidades, y "Hidratos de
    # carbono" ocupa unas 110. La nota NO va en ese raíl —no cabe— sino debajo
    # de la barra, donde hay ancho de sobra.
    X0, ANCHO, FILA = 156, 290, 62
    ALTO = 46 + len(D.AMDR) * FILA + 40
    p = [f'<symbol id="me-amdr" viewBox="0 0 464 {ALTO}">']
    for k in range(0, 101, 10):
        x = X0 + ANCHO * k / 100
        p.append(f'<path d="M{f(x)} 30 V{46 + len(D.AMDR)*FILA - 14}" '
                 f'fill="none" stroke="{APAGADO}" stroke-width=".5" '
                 'opacity=".3"/>')
        if k % 20 == 0:
            p.append(txt(x, 22, f"{k} %", "num", 8.4, APAGADO))
    for i, (nombre, lo, hi, nota) in enumerate(D.AMDR):
        y = 46 + i * FILA
        p.append(txt(X0 - 12, y + 20, nombre, "rot", 9.6, PRI, "end"))
        corto = nota[:62] + ("…" if len(nota) > 62 else "")
        p.append(txt(X0, y + 46, corto, "et", 9.2, APAGADO, "start"))
        x = X0 + ANCHO * lo / 100
        w = ANCHO * (hi - lo) / 100
        p.append(barra(x, y + 2, w, 26, PRI, ".2"))
        p.append(txt(x + w / 2, y + 19, f"{lo} – {hi} %", "num", 11, PRI))
        # extremos marcados
        for v in (lo, hi):
            xv = X0 + ANCHO * v / 100
            p.append(f'<path d="M{f(xv)} {y-2} V{y+32}" fill="none" '
                     f'stroke="{PRI}" stroke-width="1.4"/>')
    p.append(txt(232, ALTO - 22,
                 "LOS TRES RANGOS ADMITEN EL 100 % EN ALGÚN PUNTO",
                 "rot", 8.2, SEC))
    p.append(pie(464, ALTO, "RANGOS DE DISTRIBUCIÓN · DIETARY REFERENCE INTAKES"))
    p.append("</symbol>")
    return "".join(p)


def me_micro():
    """El RDA y el UL de los diecinueve, que es la tabla que nadie imprime
    entera: casi todas las divulgativas dan el RDA y se callan el techo."""
    PRI, SEC = ACENTOS["mesa"]
    FILA = 26
    ALTO = 40 + len(D.MICRO) * FILA + 18
    p = [f'<symbol id="me-micro" viewBox="0 0 464 {ALTO}">']
    cols = ((172, "UNIDAD"), (238, "HOMBRE"), (300, "MUJER"), (382, "TECHO · UL"))
    for x, etq in cols:
        p.append(txt(x, 18, etq, "rot", 7.4, PRI, "end"))
    p.append(f'<path d="M8 24 H452" fill="none" stroke="{PRI}" '
             'stroke-width=".9" opacity=".45"/>')
    for i, (nombre, unidad, rh, rm, ul, nota) in enumerate(D.MICRO):
        y = 40 + i * FILA
        if i % 2 == 0:
            p.append(f'<rect x="8" y="{f(y-13)}" width="444" height="{FILA-2}" '
                     f'rx="3" fill="{PRI}" opacity=".045"/>')
        p.append(txt(10, y + 3, nombre, "et", 10.8, CLARO, "start"))
        p.append(txt(172, y + 3, unidad, "et", 9.8, APAGADO, "end"))
        p.append(txt(238, y + 3, f"{rh:g}", "num", 10, PRI, "end"))
        p.append(txt(300, y + 3, f"{rm:g}", "num", 10, PRI, "end"))
        if ul is None:
            p.append(txt(382, y + 3, "sin techo", "et", 9.8, APAGADO, "end"))
        else:
            p.append(txt(382, y + 3, f"{ul:g}", "num", 10, ALERTA, "end"))
        # margen: cuántas veces cabe el RDA dentro del techo
        if ul:
            veces = ul / max(rh, rm)
            ancho = min(58, 6 + math.log10(max(veces, 1.05)) * 30)
            p.append(barra(392, y - 6, ancho, 12, ALERTA,
                           ".5" if veces < 5 else ".2", False, 2))
            p.append(txt(452, y + 3, f"×{veces:.0f}", "num", 8.6, APAGADO, "end"))
    p.append(pie(464, ALTO,
                 "RDA A LA IZQUIERDA · LÍMITE TOLERABLE A LA DERECHA · "
                 "BARRA = MARGEN"))
    p.append("</symbol>")
    return "".join(p)


def me_margen():
    """Los nutrientes ordenados por estrechez de margen. Es un cálculo, no una
    tabla copiada: el margen es el techo dividido por la necesidad, y decide
    cuáles se pueden suplementar a ciegas y cuáles no."""
    PRI, SEC = ACENTOS["mesa"]
    conmargen = [(n, ul / max(rh, rm)) for n, u, rh, rm, ul, _ in D.MICRO if ul]
    conmargen.sort(key=lambda t: t[1])
    FILA, X0, ANCHO = 28, 168, 250
    ALTO = 44 + len(conmargen) * FILA + 42
    p = [f'<symbol id="me-margen" viewBox="0 0 464 {ALTO}">']
    tope = max(v for _, v in conmargen)
    for k in (1, 5, 10, 25, 50, 100):
        if k > tope:
            break
        x = X0 + ANCHO * math.log10(k) / math.log10(tope)
        p.append(f'<path d="M{f(x)} 30 V{44 + len(conmargen)*FILA - 6}" '
                 f'fill="none" stroke="{APAGADO}" stroke-width=".5" '
                 'opacity=".35"/>')
        p.append(txt(x, 22, f"×{k}", "num", 8.2, APAGADO))
    for i, (nombre, veces) in enumerate(conmargen):
        y = 44 + i * FILA
        estrecho = veces < 6
        col = ALERTA if estrecho else PRI
        p.append(txt(160, y + 12, nombre, "et", 10.8, col, "end"))
        w = ANCHO * math.log10(max(veces, 1.02)) / math.log10(tope)
        p.append(barra(X0, y + 2, w, 18, col, ".3" if estrecho else ".18"))
        p.append(txt(X0 + w + 8, y + 15, f"×{veces:.0f}", "num", 9.6, col,
                     "start"))
    p.append(txt(232, ALTO - 26,
                 "EN ROJO, MARGEN MENOR DE SEIS VECES", "rot", 8.2, ALERTA))
    p.append(pie(464, ALTO, "ESCALA LOGARÍTMICA · TECHO DIVIDIDO POR NECESIDAD"))
    p.append("</symbol>")
    return "".join(p)


def me_plato():
    """El plato repartido y la mano como medida: la única báscula que se lleva
    siempre encima."""
    PRI, SEC = ACENTOS["mesa"]
    ALTO = 300
    p = [f'<symbol id="me-plato" viewBox="0 0 464 {ALTO}">']
    cx, cy, r = 116, 106, 80
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r+8}" fill="none" stroke="{PRI}" '
             'stroke-width="1" opacity=".3"/>')
    # Los nombres NO caben dentro de los sectores a un tamaño legible: van en
    # una leyenda debajo, con la misma tinta y opacidad que su porción.
    sect = [(0, 180, "Verdura y fruta", "½", PRI, ".26"),
            (180, 270, "Proteína", "¼", SEC, ".26"),
            (270, 360, "Cereal o tubérculo", "¼", PRI, ".12")]
    for a0, a1, etq, frac, col, op in sect:
        x1, y1 = pol(cx, cy, r, a0)
        x2, y2 = pol(cx, cy, r, a1)
        grande = 1 if a1 - a0 > 180 else 0
        p.append(f'<path d="M{cx} {cy} L{f(x1)} {f(y1)} A{r} {r} 0 {grande} 1 '
                 f'{f(x2)} {f(y2)} Z" fill="{col}" opacity="{op}" '
                 f'stroke="{col}" stroke-width="1.2"/>')
        mx, my = pol(cx, cy, r * 0.56, (a0 + a1) / 2)
        p.append(txt(mx, my + 6, frac, "rot", 17, col))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{PRI}" '
             'stroke-width="2"/>')
    p.append(txt(cx, 206, "EL PLATO", "rot", 10.4, PRI))
    for i, (_, _, etq, frac, col, op) in enumerate(sect):
        y = 222 + i * 22
        p.append(f'<rect x="20" y="{y-9}" width="16" height="13" rx="3" '
                 f'fill="{col}" opacity="{op}"/>')
        p.append(f'<rect x="20" y="{y-9}" width="16" height="13" rx="3" '
                 f'fill="none" stroke="{col}" stroke-width="1"/>')
        p.append(txt(44, y + 1, frac, "num", 12, col, "start"))
        p.append(txt(64, y + 1, etq, "et", 10.6, CLARO, "start"))
    # la mano
    manos = [("Palma sin dedos", "Proteína", "una ración"),
             ("Puño cerrado", "Verdura", "una o dos"),
             ("Mano en cuenco", "Cereal", "una ración"),
             ("Pulgar entero", "Grasa", "una ración")]
    for i, (parte, que, cuanta) in enumerate(manos):
        y = 34 + i * 52
        p.append(f'<rect x="234" y="{y}" width="220" height="42" rx="8" '
                 f'fill="{PRI}" opacity=".055"/>')
        p.append(f'<circle cx="252" cy="{y+21}" r="7" fill="none" '
                 f'stroke="{SEC}" stroke-width="1.6"/>')
        p.append(txt(252, y + 25, str(i + 1), "num", 9, SEC))
        p.append(txt(270, y + 18, parte, "rot", 8.8, PRI, "start"))
        p.append(txt(270, y + 33, f"{que} · {cuanta}", "et", 10.4, CLARO,
                     "start"))
    p.append(txt(344, 262, "LA MANO ESCALA CON EL CUERPO", "rot", 7.6, SEC))
    p.append(pie(464, ALTO, "SIN BÁSCULA · SIN CONTAR · SIN APLICACIÓN"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  CÓDICE DE LA CARGA
# ══════════════════════════════════════════════════════════════════════
def ca_dosis():
    """La curva de respuesta de las guías: el tramo rentable está al principio.

    La curva se dibuja con una saturación exponencial, que es la forma que
    describen las guías cualitativamente. No es un ajuste de datos: es la forma,
    y el pie de la lámina lo dice.
    """
    PRI, SEC = ACENTOS["carga"]
    A = D.ACTIVIDAD
    X0, Y0, ANCHO, ALTO_G = 56, 40, 380, 190
    p = ['<symbol id="ca-dosis" viewBox="0 0 464 300">']
    p.append(f'<path d="M{X0} {Y0} V{Y0+ALTO_G} H{X0+ANCHO}" fill="none" '
             f'stroke="{APAGADO}" stroke-width="1"/>')
    maxmin = 450
    pts = []
    for k in range(0, maxmin + 1, 5):
        # saturación: rinde mucho al principio y se aplana
        v = 1 - math.exp(-k / 130)
        x = X0 + ANCHO * k / maxmin
        y = Y0 + ALTO_G - ALTO_G * 0.92 * v
        pts.append((x, y))
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in pts)
             + f'" fill="none" stroke="{PRI}" stroke-width="2.6" '
               'stroke-linejoin="round"/>')
    # zonas
    for lo, hi, etq, col, op in ((0, A["moderada_min"], "TRAMO MÁS RENTABLE",
                                  PRI, ".14"),
                                 (A["moderada_min"], A["moderada_max"],
                                  "BENEFICIO ADICIONAL", SEC, ".1")):
        x = X0 + ANCHO * lo / maxmin
        w = ANCHO * (hi - lo) / maxmin
        p.append(f'<rect x="{f(x)}" y="{Y0}" width="{f(w)}" height="{ALTO_G}" '
                 f'fill="{col}" opacity="{op}"/>')
        p.append(txt(x + w / 2, Y0 + ALTO_G + 30, etq, "rot", 7.4, col))
    for v, etq in ((A["moderada_min"], "150 min"), (A["moderada_max"], "300 min")):
        x = X0 + ANCHO * v / maxmin
        p.append(f'<path d="M{f(x)} {Y0} V{Y0+ALTO_G+6}" fill="none" '
                 f'stroke="{SEC}" stroke-width="1.4" stroke-dasharray="4 3"/>')
        p.append(txt(x, Y0 + ALTO_G + 18, etq, "num", 9.6, SEC))
    p.append(txt(X0, Y0 - 8, "BENEFICIO", "rot", 8, APAGADO, "start"))
    p.append(txt(X0 + ANCHO, Y0 + ALTO_G + 18, "min/semana", "et", 10, APAGADO,
                 "end"))
    p.append(txt(232, 22,
                 f"{A['moderada_min']}–{A['moderada_max']} MIN MODERADOS · O "
                 f"{A['vigorosa_min']}–{A['vigorosa_max']} VIGOROSOS",
                 "rot", 9, PRI))
    p.append(pie(464, 300,
                 "FORMA DE LA CURVA SEGÚN LAS GUÍAS · NO ES UN AJUSTE DE DATOS"))
    p.append("</symbol>")
    return "".join(p)


def ca_met():
    """La escala MET con los dos umbrales oficiales marcados."""
    PRI, SEC = ACENTOS["carga"]
    FILA, X0, ANCHO = 28, 196, 216
    ALTO = 42 + len(D.MET) * FILA + 34
    tope = max(m for _, m, _ in D.MET) + 1
    p = [f'<symbol id="ca-met" viewBox="0 0 464 {ALTO}">']
    COLOR_B = {"reposo": APAGADO, "ligera": APAGADO, "moderada": PRI,
               "vigorosa": SEC}
    for umbral, etq in ((D.UMBRAL_MET["moderada"], "MODERADA · 3 MET"),
                        (D.UMBRAL_MET["vigorosa"], "VIGOROSA · 6 MET")):
        x = X0 + ANCHO * umbral / tope
        p.append(f'<path d="M{f(x)} 30 V{42 + len(D.MET)*FILA - 4}" fill="none" '
                 f'stroke="{SEC}" stroke-width="1.2" stroke-dasharray="4 3" '
                 'opacity=".75"/>')
        p.append(txt(x, 22, etq, "rot", 7.4, SEC))
    for i, (nombre, met, banda) in enumerate(D.MET):
        y = 42 + i * FILA
        col = COLOR_B[banda]
        p.append(txt(188, y + 14, nombre, "et", 10.6, col, "end"))
        w = ANCHO * met / tope
        p.append(barra(X0, y + 3, w, 18, col, ".26"))
        p.append(txt(X0 + w + 7, y + 17, f"{met:g}", "num", 9.6, col, "start"))
    p.append(txt(232, ALTO - 20,
                 "UN MINUTO VIGOROSO CUENTA COMO DOS MODERADOS",
                 "rot", 8.2, SEC))
    p.append(pie(464, ALTO, "EQUIVALENTE METABÓLICO · VECES EL GASTO EN REPOSO"))
    p.append("</symbol>")
    return "".join(p)


def ca_descarga():
    """Lo que le pasa a un cuerpo sin carga. La silueta señala qué se va
    primero; la columna, a qué ritmo."""
    PRI, SEC = ACENTOS["carga"]
    K, OX, OY = 1.06, 16, 30
    # El alto lo manda la más alta de las dos columnas: la silueta o la pila de
    # fichas. Antes solo miraba la silueta y la última ficha pisaba el pie.
    FILA_D, ALTO_D = 62, 52
    ALTO = int(max(OY + 262 * K, 34 + (len(D.DESCARGA) - 1) * FILA_D + ALTO_D)
               + 30)
    p = [f'<symbol id="ca-descarga" viewBox="0 0 464 {ALTO}">']
    p.append(f'<defs><g id="cd-mitad"><path d="{MITAD}"/></g></defs>')
    p.append(f'<g transform="translate({OX},{OY}) scale({f(K)})">')
    for rell, trazo, op in ((PRI, "none", ".07"), ("none", PRI, ".45")):
        p.append(f'<g fill="{rell}" fill-opacity="{op}" stroke="{trazo}" '
                 f'stroke-width=".9" stroke-opacity="{op}" '
                 'stroke-linejoin="round" stroke-linecap="round">'
                 '<circle cx="72" cy="17" r="11"/><use href="#cd-mitad"/>'
                 '<use href="#cd-mitad" transform="translate(144,0) scale(-1,1)"/>'
                 "</g>")
    p.append("</g>")
    # zonas que más pierden, marcadas sobre la silueta
    centro = OX + 72 * K
    for y_local, etq in ((104, "Lumbares"), (150, "Glúteo"), (190, "Cuádriceps"),
                         (222, "Gemelo")):
        y = OY + y_local * K
        p.append(f'<rect x="{f(centro-40)}" y="{f(y-7)}" width="80" height="14" '
                 f'rx="7" fill="{SEC}" opacity=".2"/>')
        p.append(f'<path d="M{f(centro+42)} {f(y)} H176" fill="none" '
                 f'stroke="{SEC}" stroke-width=".8" stroke-dasharray="3 3" '
                 'opacity=".6"/>')
        p.append(txt(180, y + 4, etq, "et", 10, SEC, "start"))
    for i, (que, ritmo, nota) in enumerate(D.DESCARGA):
        y = 34 + i * FILA_D
        p.append(f'<rect x="248" y="{y}" width="208" height="{ALTO_D}" rx="8" '
                 f'fill="{PRI}" opacity=".055"/>')
        p.append(txt(258, y + 16, que.upper(), "rot", 8.4, PRI, "start"))
        p.append(txt(258, y + 30, ritmo, "et", 10.4, ALERTA, "start"))
        # 198 unidades de ancho útil: a 8,8 en Rajdhani entran unas 40 letras.
        corto = nota[:40].rstrip() + ("…" if len(nota) > 40 else "")
        p.append(txt(258, y + 44, corto, "et", 8.8, APAGADO, "start"))
    p.append(pie(464, ALTO,
                 "REPOSO EN CAMA Y VUELO ESPACIAL · ÓRDENES DE MAGNITUD"))
    p.append("</symbol>")
    return "".join(p)


def ca_niosh():
    """La ecuación de levantamiento: por qué el mismo peso es seguro pegado al
    cuerpo y no lo es con los brazos estirados."""
    PRI, SEC = ACENTOS["carga"]
    p = ['<symbol id="ca-niosh" viewBox="0 0 464 296">']
    p.append(f'<rect x="14" y="12" width="436" height="46" rx="9" '
             f'fill="{PRI}" opacity=".07"/>')
    p.append(txt(232, 32, f"PESO RECOMENDADO = {D.NIOSH['carga_constante']} kg "
                          "× SEIS FACTORES", "rot", 10.4, PRI))
    p.append(txt(232, 48, "cada factor vale entre 0 y 1 · nunca los mejora",
                 "et", 10.6, CLARO))
    for i, (sig, nombre, glosa) in enumerate(D.NIOSH["factores"]):
        c, r = i % 2, i // 2
        x = 14 + c * 222
        y = 72 + r * 62
        p.append(f'<rect x="{x}" y="{y}" width="214" height="52" rx="8" '
                 f'fill="{SEC}" opacity=".05"/>')
        p.append(f'<circle cx="{x+22}" cy="{y+26}" r="14" fill="none" '
                 f'stroke="{SEC}" stroke-width="1.4"/>')
        p.append(txt(x + 22, y + 30, sig, "rot", 9, SEC))
        p.append(txt(x + 44, y + 20, nombre.upper(), "rot", 8.4, PRI, "start"))
        corto = glosa[:44] + ("…" if len(glosa) > 44 else "")
        p.append(txt(x + 44, y + 36, corto, "et", 9.8, CLARO, "start"))
    p.append(f'<rect x="14" y="262" width="436" height="24" rx="6" '
             f'fill="{ALERTA}" opacity=".08"/>')
    p.append(txt(232, 278, "ALEJAR LA CARGA DEL CUERPO ES LO QUE MÁS PENALIZA",
                 "rot", 8.4, ALERTA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  CÓDICE DE LA VOLUNTAD
# ══════════════════════════════════════════════════════════════════════
def vo_adherencia():
    """Dos dietas distintas con la misma adherencia dan lo mismo; la misma
    dieta con adherencias distintas, no. La lámina dice cuál es la variable."""
    PRI, SEC = ACENTOS["voluntad"]
    X0, Y0, ANCHO, ALTO_G = 60, 44, 372, 168
    p = ['<symbol id="vo-adherencia" viewBox="0 0 464 288">']
    p.append(f'<path d="M{X0} {Y0} V{Y0+ALTO_G} H{X0+ANCHO}" fill="none" '
             f'stroke="{APAGADO}" stroke-width="1"/>')
    for i, (etq, adher, col) in enumerate((("Cumplida al 90 %", .9, PRI),
                                           ("Cumplida al 60 %", .6, SEC),
                                           ("Cumplida al 30 %", .3, APAGADO))):
        pts = []
        for k in range(0, 25):
            x = X0 + ANCHO * k / 24
            y = Y0 + ALTO_G - ALTO_G * 0.88 * adher * (k / 24)
            pts.append((x, y))
        p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in pts)
                 + f'" fill="none" stroke="{col}" stroke-width="2.4"/>')
        ex, ey = pts[-1]
        p.append(f'<circle cx="{f(ex)}" cy="{f(ey)}" r="3.4" fill="{col}"/>')
        p.append(txt(X0 + ANCHO - 4, ey - 8, etq, "et", 10.4, col, "end"))
    p.append(txt(X0 - 8, Y0 + 10, "RESULTADO", "rot", 8, APAGADO, "end"))
    p.append(txt(X0 + ANCHO, Y0 + ALTO_G + 18, "semanas", "et", 10, APAGADO,
                 "end"))
    p.append(txt(232, 26,
                 "LAS TRES LÍNEAS SON LA MISMA DIETA", "rot", 10, PRI))
    p.append(f'<rect x="60" y="242" width="344" height="26" rx="6" '
             f'fill="{PRI}" opacity=".08"/>')
    p.append(txt(232, 259,
                 "LA VARIABLE NO ES EL MÉTODO · ES CUÁNTO SE CUMPLE",
                 "rot", 8.6, PRI))
    p.append(pie(464, 288, "ESQUEMA CONCEPTUAL · NO SON DATOS DE UN ESTUDIO"))
    p.append("</symbol>")
    return "".join(p)


def vo_habito():
    """El bucle del hábito con los tres puntos donde se puede intervenir."""
    PRI, SEC = ACENTOS["voluntad"]
    NODOS = [("SEÑAL", "lo que lo dispara", "Cambiar el entorno"),
             ("RUTINA", "lo que se hace", "Sustituir, no suprimir"),
             ("PREMIO", "lo que lo mantiene", "Hacerlo inmediato")]
    X, W, FILA = 20, 250, 82
    ALTO = 16 + 3 * FILA + 24
    p = [f'<symbol id="vo-habito" viewBox="0 0 464 {ALTO}">']
    for i, (nombre, que, palanca) in enumerate(NODOS):
        y = 14 + i * FILA
        p.append(f'<rect x="{X}" y="{y}" width="{W}" height="58" rx="9" '
                 f'fill="{PRI}" opacity=".07"/>')
        p.append(f'<rect x="{X}" y="{y}" width="{W}" height="58" rx="9" '
                 f'fill="none" stroke="{PRI}" stroke-width=".9" opacity=".45"/>')
        p.append(f'<circle cx="{X+30}" cy="{y+29}" r="16" fill="none" '
                 f'stroke="{PRI}" stroke-width="1.4"/>')
        p.append(txt(X + 30, y + 34, str(i + 1), "num", 14, PRI))
        p.append(txt(X + 56, y + 24, nombre, "rot", 10.4, PRI, "start"))
        p.append(txt(X + 56, y + 42, que, "et", 10.6, CLARO, "start"))
        # la palanca, en el color de la salida
        p.append(f'<path d="M{X+W} {f(y+29)} H{X+W+26}" fill="none" '
                 f'stroke="{SEC}" stroke-width="2" stroke-dasharray="5 3"/>')
        p.append(flecha(X + W + 28, y + 29, 0, 7, SEC))
        p.append(txt(X + W + 38, y + 26, "PALANCA", "rot", 7.4, SEC, "start"))
        p.append(txt(X + W + 38, y + 40, palanca, "et", 10.2, SEC, "start"))
        if i < 2:
            p.append(f'<path d="M{X+30} {y+58} V{y+FILA-4}" fill="none" '
                     f'stroke="{PRI}" stroke-width="2"/>')
            p.append(flecha(X + 30, y + FILA - 2, 90, 7, PRI))
    ult = 14 + 2 * FILA + 29
    p.append(f'<path d="M{X} {ult} H{X-8} V43 H{X}" fill="none" '
             f'stroke="{PRI}" stroke-width="1.6" opacity=".55"/>')
    p.append(flecha(X - 2, 43, 0, 7, PRI))
    p.append(pie(464, ALTO, "SE INTERVIENE EN LA SEÑAL Y EN EL PREMIO · "
                            "LA RUTINA ES LA MÁS DIFÍCIL"))
    p.append("</symbol>")
    return "".join(p)


def vo_recaida():
    """La bifurcación: un fallo es un fallo, y el derrumbe es una decisión
    distinta que se toma después."""
    PRI, SEC = ACENTOS["voluntad"]
    p = ['<symbol id="vo-recaida" viewBox="0 0 464 292">']
    X0, Y0 = 40, 112
    p.append(f'<path d="M{X0} {Y0} H150" fill="none" stroke="{PRI}" '
             'stroke-width="2.6"/>')
    p.append(f'<circle cx="150" cy="{Y0}" r="7" fill="{ALERTA}"/>')
    # Las dos etiquetas del punto van claramente por encima del eje: a −18 y −4
    # la segunda cruzaba la recta y el círculo de decisión.
    p.append(txt(146, Y0 - 34, "EL FALLO", "rot", 8.6, ALERTA))
    p.append(txt(146, Y0 - 20, "un día, una comida", "et", 10, APAGADO))
    # rama alta: se retoma
    p.append(f'<path d="M157 {Y0} C210 {Y0} 230 {Y0-46} 300 {Y0-52} '
             f'L430 {Y0-58}" fill="none" stroke={chr(34)}{PRI}{chr(34)} '
             'stroke-width="2.6"/>')
    # La rama alta termina en Y0−58: las dos etiquetas van encima de ella, no
    # a caballo del trazo.
    p.append(txt(430, Y0 - 84, "SE RETOMA", "rot", 9.6, PRI, "end"))
    p.append(txt(430, Y0 - 68, "el fallo queda en un dato del cuaderno",
                 "et", 10.2, CLARO, "end"))
    # rama baja: se derrumba
    p.append(f'<path d="M157 {Y0} C210 {Y0} 230 {Y0+50} 300 {Y0+62} '
             f'L430 {Y0+78}" fill="none" stroke="{APAGADO}" '
             'stroke-width="2.6" stroke-dasharray="7 4"/>')
    p.append(txt(430, Y0 + 96, "SE ABANDONA", "rot", 9.6, APAGADO, "end"))
    p.append(txt(430, Y0 + 112, "«ya que lo he roto» · esto sí es la decisión",
                 "et", 10.2, APAGADO, "end"))
    # el punto de decisión
    p.append(f'<circle cx="196" cy="{Y0}" r="16" fill="none" stroke="{SEC}" '
             'stroke-width="1.6" stroke-dasharray="4 3"/>')
    p.append(txt(196, Y0 + 40, "AQUÍ", "rot", 8.6, SEC))
    p.append(txt(196, Y0 + 54, "está la elección", "et", 10, SEC))
    p.append(pie(464, 292, "EL FALLO NO ES LA RECAÍDA · LA RECAÍDA VIENE DESPUÉS"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  CÓDICE DEL DESCANSO
# ══════════════════════════════════════════════════════════════════════
def de_hipnograma():
    """La asimetría de la noche: el profundo va delante y el REM detrás. Es el
    dato que explica por qué recortar por el final no cuesta lo mismo que
    recortar por el principio."""
    PRI, SEC = ACENTOS["descanso"]
    # X0 a 70: la etiqueta más larga del eje es «Despierto» y anclada al final
    # en 56 se salía del viewBox por la izquierda.
    X0, Y0, ANCHO, ALTO_G = 70, 44, 370, 150
    NIVEL = {"Despierto": 0, "REM": 1, "N1": 2, "N2": 3, "N3": 4}
    curva = [("Despierto", 0), ("N1", 5), ("N2", 15), ("N3", 40), ("N2", 60),
             ("REM", 75), ("N2", 95), ("N3", 120), ("N2", 145), ("REM", 165),
             ("N2", 190), ("N3", 205), ("N2", 225), ("REM", 255), ("N2", 285),
             ("REM", 320), ("N2", 355), ("REM", 400), ("N1", 425),
             ("Despierto", 435)]
    total = 450
    p = ['<symbol id="de-hipnograma" viewBox="0 0 464 296">']
    for etq, n in NIVEL.items():
        y = Y0 + ALTO_G * n / 4
        p.append(f'<path d="M{X0} {f(y)} H{X0+ANCHO}" fill="none" '
                 f'stroke="{APAGADO}" stroke-width=".5" opacity=".3"/>')
        p.append(txt(X0 - 8, y + 4, etq, "rot", 7.6, APAGADO, "end"))
    # mitades de la noche
    for lo, hi, etq, col in ((0, total / 2, "PRIMERA MITAD · MANDA EL PROFUNDO",
                             PRI),
                             (total / 2, total, "SEGUNDA MITAD · MANDA EL REM",
                              SEC)):
        x = X0 + ANCHO * lo / total
        w = ANCHO * (hi - lo) / total
        p.append(f'<rect x="{f(x)}" y="{Y0}" width="{f(w)}" '
                 f'height="{ALTO_G}" fill="{col}" opacity=".08"/>')
        p.append(txt(x + w / 2, Y0 + ALTO_G + 26, etq, "rot", 7.4, col))
    pts = [(X0 + ANCHO * m / total, Y0 + ALTO_G * NIVEL[fase] / 4)
           for fase, m in curva]
    escalon = [pts[0]]
    for a, b in zip(pts, pts[1:]):
        escalon += [(b[0], a[1]), b]
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in escalon)
             + f'" fill="none" stroke="{PRI}" stroke-width="2.2" '
               'stroke-linejoin="round"/>')
    for h in range(0, 8):
        x = X0 + ANCHO * h * 60 / total
        if x <= X0 + ANCHO:
            p.append(txt(x, Y0 + ALTO_G + 14, f"{h} h", "num", 8.2, APAGADO))
    p.append(txt(232, 26,
                 f"{D.SUENO['ciclos_noche'][0]} A {D.SUENO['ciclos_noche'][1]} "
                 f"CICLOS DE UNOS {D.SUENO['ciclo_min']} MINUTOS",
                 "rot", 9.4, PRI))
    p.append(f'<rect x="{X0}" y="266" width="{ANCHO}" height="24" rx="6" '
             f'fill="{SEC}" opacity=".08"/>')
    p.append(txt(232, 282,
                 "RECORTAR POR EL FINAL SE COME EL REM, NO EL PROFUNDO",
                 "rot", 8.4, SEC))
    p.append("</symbol>")
    return "".join(p)


def de_fases():
    """Las cuatro fases con lo que hace cada una."""
    PRI, SEC = ACENTOS["descanso"]
    FILA = 58
    ALTO = 20 + len(D.SUENO["fases"]) * FILA + 22
    p = [f'<symbol id="de-fases" viewBox="0 0 464 {ALTO}">']
    for i, (sig, nombre, cuanto, hace) in enumerate(D.SUENO["fases"]):
        y = 16 + i * FILA
        col = SEC if sig == "REM" else PRI
        p.append(f'<rect x="14" y="{y}" width="436" height="48" rx="9" '
                 f'fill="{col}" opacity=".06"/>')
        p.append(f'<rect x="26" y="{y+10}" width="46" height="28" rx="5" '
                 f'fill="none" stroke="{col}" stroke-width="1.4"/>')
        p.append(txt(49, y + 29, sig, "rot", 11, col))
        p.append(txt(86, y + 20, nombre.upper(), "rot", 8.8, col, "start"))
        p.append(txt(86, y + 36, hace, "et", 10.4, CLARO, "start"))
        p.append(txt(444, y + 29, cuanto, "et", 10, APAGADO, "end"))
    p.append(pie(464, ALTO, "ARQUITECTURA DEL SUEÑO · CUATRO ESTADOS, NO UNO"))
    p.append("</symbol>")
    return "".join(p)


def de_deuda():
    """La deuda se acumula y no se paga en una noche."""
    PRI, SEC = ACENTOS["descanso"]
    X0, Y0, ANCHO, ALTO_G = 52, 42, 388, 150
    objetivo = D.SUENO["adulto_horas"]
    noches = [6, 5.5, 6, 5, 6.5, 9, 8]
    dias = ["L", "M", "X", "J", "V", "S", "D"]
    p = ['<symbol id="de-deuda" viewBox="0 0 464 288">']
    tope = 10
    for h in range(0, tope + 1, 2):
        y = Y0 + ALTO_G - ALTO_G * h / tope
        p.append(f'<path d="M{X0} {f(y)} H{X0+ANCHO}" fill="none" '
                 f'stroke="{APAGADO}" stroke-width=".5" opacity=".3"/>')
        p.append(txt(X0 - 8, y + 4, f"{h} h", "num", 8, APAGADO, "end"))
    yobj = Y0 + ALTO_G - ALTO_G * objetivo / tope
    p.append(f'<path d="M{X0} {f(yobj)} H{X0+ANCHO}" fill="none" '
             f'stroke="{SEC}" stroke-width="1.6" stroke-dasharray="5 3"/>')
    # La etiqueta del objetivo va al principio de la línea: al final caía
    # encima de las dos barras del fin de semana.
    p.append(txt(X0 + 4, yobj - 8, f"OBJETIVO · {objetivo} h", "rot", 7.6,
                 SEC, "start"))
    w = ANCHO / len(noches) - 10
    deuda = 0
    for i, (d, h) in enumerate(zip(dias, noches)):
        x = X0 + i * (ANCHO / len(noches)) + 5
        alto = ALTO_G * h / tope
        falta = objetivo - h
        deuda += max(falta, 0) if falta > 0 else max(falta, -2) * 0.5
        col = ALERTA if falta > 0 else PRI
        p.append(barra(x, Y0 + ALTO_G - alto, w, alto, col, ".26"))
        p.append(txt(x + w / 2, Y0 + ALTO_G + 16, d, "rot", 9, col))
        p.append(txt(x + w / 2, Y0 + ALTO_G - alto - 6,
                     f"{h:g}".replace(".", ","), "num", 8.6, col))
    p.append(txt(232, 24, "DEUDA ACUMULADA EN LA SEMANA: "
                 + f"{deuda:.1f}".replace(".", ",") + " HORAS",
                 "rot", 9.4, ALERTA))
    p.append(f'<rect x="52" y="252" width="388" height="26" rx="6" '
             f'fill="{ALERTA}" opacity=".08"/>')
    p.append(txt(246, 269,
                 "DORMIR DE MÁS EL FIN DE SEMANA RECUPERA PARTE · NO TODA",
                 "rot", 8.2, ALERTA))
    p.append("</symbol>")
    return "".join(p)


def de_ventana():
    """La cuenta atrás de la noche: qué se corta y cuándo."""
    PRI, SEC = ACENTOS["descanso"]
    HITOS = [("−10 h", "Última cafeína", "Su vida media ronda las 5 horas: a las "
                                        "10 queda un octavo"),
             ("−3 h", "Última comida grande", "La digestión sube la temperatura "
                                              "central"),
             ("−3 h", "Último alcohol", "Adormece y luego fragmenta la segunda "
                                        "mitad"),
             ("−2 h", "Último entrenamiento fuerte", "Salvo que lo lleves bien "
                                                     "probado"),
             ("−1 h", "Fuera pantallas y trabajo", "La única regla no negociable "
                                                   "de la lista"),
             ("0", "Misma hora, todos los días", "Incluido el fin de semana")]
    FILA = 42
    ALTO = 22 + len(HITOS) * FILA + 24
    p = [f'<symbol id="de-ventana" viewBox="0 0 464 {ALTO}">']
    p.append(f'<path d="M78 14 V{22 + len(HITOS)*FILA - 8}" fill="none" '
             f'stroke="{PRI}" stroke-width="1.4" opacity=".4"/>')
    for i, (cuando, que, por) in enumerate(HITOS):
        y = 22 + i * FILA
        ultimo = i == len(HITOS) - 1
        col = SEC if ultimo else PRI
        p.append(txt(66, y + 22, cuando, "num", 11, col, "end"))
        p.append(f'<circle cx="78" cy="{y+18}" r="{6 if ultimo else 4.5}" '
                 f'fill="{col}"/>')
        p.append(f'<rect x="96" y="{y}" width="356" height="34" rx="7" '
                 f'fill="{col}" opacity=".06"/>')
        p.append(txt(108, y + 15, que.upper(), "rot", 8.4, col, "start"))
        p.append(txt(108, y + 29, por, "et", 10, CLARO, "start"))
    p.append(pie(464, ALTO, "CUENTA ATRÁS DESDE LA HORA DE ACOSTARSE"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  SÍMBOLOS DE CUBIERTA
# ══════════════════════════════════════════════════════════════════════
def cubierta_mesa():
    p = ['<g fill="none" stroke="var(--acento)" stroke-linejoin="round">']
    p.append('<circle cx="120" cy="120" r="62" stroke-width="2.6"/>')
    p.append('<circle cx="120" cy="120" r="50" stroke-width=".8" opacity=".4"/>')
    for a0, a1, op in ((0, 180, ".26"), (180, 270, ".18"), (270, 360, ".1")):
        x1, y1 = pol(120, 120, 62, a0)
        x2, y2 = pol(120, 120, 62, a1)
        g = 1 if a1 - a0 > 180 else 0
        p.append(f'<path d="M120 120 L{f(x1)} {f(y1)} A62 62 0 {g} 1 '
                 f'{f(x2)} {f(y2)} Z" fill="var(--acento)" opacity="{op}" '
                 'stroke="var(--acento)" stroke-width="1.2"/>')
    p.append('<path d="M120 58 V182 M120 120 H182" stroke-width="1.6" '
             'opacity=".8"/>')
    p.append("</g>")
    return "".join(p)


def cubierta_carga():
    p = ['<g fill="none" stroke="var(--acento)" stroke-linecap="round">']
    p.append('<path d="M46 120 H194" stroke-width="4"/>')
    for s in (-1, 1):
        for k, (dx, h) in enumerate(((52, 60), (62, 44), (70, 28))):
            x = 120 + s * dx
            p.append(f'<rect x="{f(x-4)}" y="{f(120-h/2)}" width="8" '
                     f'height="{f(h)}" rx="2.5" fill="var(--acento)" '
                     f'opacity="{.9-k*.22:.2f}" stroke="none"/>')
        p.append(f'<rect x="{f(120+s*42-3)}" y="108" width="6" height="24" '
                 'rx="2" fill="var(--acento-2)" stroke="none"/>')
    p.append('<path d="M74 84 H166" stroke-width="1.2" stroke-dasharray="4 3" '
             'opacity=".5"/>')
    p.append("</g>")
    return "".join(p)


def cubierta_voluntad():
    """Un bucle con su salida: la figura del libro."""
    p = ['<g fill="none" stroke="var(--acento)" stroke-linecap="round">']
    arco = []
    for k in range(300):
        x, y = pol(120, 120, 58, 40 + k)
        arco.append(f"{'M' if k == 0 else 'L'}{f(x)} {f(y)}")
    p.append(f'<path d="{" ".join(arco)}" stroke-width="3"/>')
    for g in (40, 130, 220, 310):
        x, y = pol(120, 120, 58, g)
        p.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="6" '
                 'fill="var(--acento)" stroke="none"/>')
    sx, sy = pol(120, 120, 58, 20)
    ex, ey = pol(120, 120, 92, 6)
    p.append(f'<path d="M{f(sx)} {f(sy)} L{f(ex)} {f(ey)}" '
             'stroke="var(--acento-2)" stroke-width="3" stroke-dasharray="7 4"/>')
    p.append(f'<circle cx="{f(ex)}" cy="{f(ey)}" r="6.5" '
             'fill="var(--acento-2)" stroke="none"/>')
    p.append("</g>")
    return "".join(p)


def cubierta_descanso():
    """Cinco ciclos dentro de una luna."""
    p = ['<g fill="none" stroke="var(--acento)" stroke-linejoin="round">']
    p.append('<path d="M150 60 A62 62 0 1 0 150 180 A50 50 0 1 1 150 60 Z" '
             'fill="var(--acento)" opacity=".12" stroke="var(--acento)" '
             'stroke-width="2"/>')
    fases = [0, -1, -2, -3, -2, -1, 0, -1, -3, -2, -1, 0, -1, -2, -1, 0]
    pts = [(64 + k * 6.6, 106 + (-v) * 12) for k, v in enumerate(fases)]
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in pts)
             + '" stroke="var(--acento-2)" stroke-width="2.4"/>')
    p.append("</g>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
def main():
    D.comprobar()
    libros = {
        "mesa": [simbolo_cubierta("mesa", cubierta_mesa()),
                 me_amdr(), me_micro(), me_margen(), me_plato()],
        "carga": [simbolo_cubierta("carga", cubierta_carga()),
                  ca_dosis(), ca_met(), ca_descarga(), ca_niosh()],
        "voluntad": [simbolo_cubierta("voluntad", cubierta_voluntad()),
                     vo_adherencia(), vo_habito(), vo_recaida()],
        "descanso": [simbolo_cubierta("descanso", cubierta_descanso()),
                     de_hipnograma(), de_fases(), de_deuda(), de_ventana()],
    }
    total = 0
    for clave, piezas in libros.items():
        destino = RAIZ / "partials" / f"{clave}.svg"
        destino.write_text(sprite(clave, piezas))
        total += len(piezas) - 1
        print(f"  partials/{clave}.svg: {len(piezas)-1} láminas + cubierta · "
              f"{destino.stat().st_size/1024:.0f} KB")
    print(f"  {total} láminas en total · datos oficiales comprobados")


if __name__ == "__main__":
    main()
