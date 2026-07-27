#!/usr/bin/env python3
"""
VILLUMINATION 99 — Emblemas de portada
======================================
Escribe partials/emblemas.svg: una insignia por documento.

Sustituyen a las poses de mascota que había antes. El motivo es de criterio:
un personaje simpático rebaja un producto que se vende como material técnico,
y once poses de un mismo muñeco no comunican once contenidos distintos. Una
insignia sí: cada una lleva en el centro el DATO del documento —la onda del
ciclado, el escalón del HIIT, los cinco ciclos de sueño, la espiral de las
respiraciones— dibujado con la misma geometría que las figuras del interior.

Todas comparten armazón para que la colección se lea como una serie:
bisel exterior con marcas, anillo de conteo con el número que importa
(semanas, días, rutinas) y el signo del contenido en el núcleo.

    python3 tools/dibujar-emblemas.py
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "partials" / "emblemas.svg"

CAJA = 200                     # todas las insignias en 200×240
CX, CY = 100, 112              # centro del bisel
R_EXT, R_INT = 92, 78          # bisel


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, grados):
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def txt(x, y, s, clase="rot", tam=9, color="var(--ink-2)", anchor="middle"):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}">{s}</text>')


def bisel(marcas=48, conteo=None, unidad=""):
    """Armazón común: dos circunferencias, marcas de grado y anillo de conteo.

    `conteo` es el número que define el documento (8 semanas, 21 días, 10
    rutinas). Se dibuja como arco de puntos: se puede contar con el dedo, que
    es exactamente lo que hace que una insignia informe y no solo decore.
    """
    p = [f'<circle cx="{CX}" cy="{CY}" r="{R_EXT}" fill="none" '
         'stroke="var(--accent)" stroke-width="1.1" opacity=".38"/>',
         f'<circle cx="{CX}" cy="{CY}" r="{R_INT}" fill="none" '
         'stroke="var(--accent)" stroke-width="2" opacity=".9"/>',
         f'<circle cx="{CX}" cy="{CY}" r="{R_INT - 7}" fill="none" '
         'stroke="var(--accent)" stroke-width=".6" opacity=".22"/>']
    d = []
    for k in range(marcas):
        largo = 8 if k % (marcas // 4) == 0 else 4
        x1, y1 = pol(CX, CY, R_EXT, k * 360 / marcas)
        x2, y2 = pol(CX, CY, R_EXT - largo, k * 360 / marcas)
        d.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    p.append(f'<path d="{" ".join(d)}" fill="none" stroke="var(--accent)" '
             'stroke-width=".8" opacity=".45"/>')
    if conteo:
        # Arco de conteo en la mitad inferior, de 120° a 360° pasando por abajo.
        # Va al filo del anillo fuerte y el rótulo por dentro: si el contador se
        # mete hacia el centro, pisa el núcleo — que es lo que pasaba antes.
        for k in range(conteo):
            ang = 120 + (240 * k / max(1, conteo - 1))
            px, py = pol(CX, CY, R_INT - 4, ang)
            p.append(f'<circle cx="{f(px)}" cy="{f(py)}" r="2.2" '
                     'fill="var(--accent)" opacity=".85"/>')
        p.append(txt(CX, CY + 58, f"{conteo} {unidad}".strip(),
                     "rot", 9.5, "var(--accent)"))
    return "".join(p)


def rotulo(linea1, linea2=""):
    p = [txt(CX, 212, linea1, "rot", 11, "var(--accent)")]
    if linea2:
        p.append(txt(CX, 228, linea2, "et", 12, "var(--ink-2)"))
    return "".join(p)


def emblema(clave, cuerpo, linea1, linea2="", conteo=None, unidad="", marcas=48):
    return (f'<symbol id="{clave}" viewBox="0 0 {CAJA} 240">'
            + bisel(marcas, conteo, unidad)
            + f'<g class="nucleo" transform="translate(0,-14)">{cuerpo}</g>'
            + rotulo(linea1, linea2)
            + "</symbol>")


# ══════════════════════════════════════════════════════════════════════
#  NÚCLEOS · el dato de cada documento
# ══════════════════════════════════════════════════════════════════════
def nucleo_volumen():
    """Escalera ascendente: la progresión de carga en superávit."""
    p = []
    for k in range(5):
        h = 10 + k * 11
        x = 56 + k * 19
        p.append(f'<rect x="{x}" y="{f(CY + 28 - h)}" width="13" height="{f(h)}" '
                 f'rx="2" fill="var(--accent)" opacity="{.22 + k * .13:.2f}"/>')
    p.append(f'<path d="M52 {CY + 32} H148" fill="none" stroke="var(--accent)" '
             'stroke-width="1.4" opacity=".7"/>')
    p.append(f'<path d="M56 {CY + 4} L142 {CY - 40}" fill="none" '
             'stroke="var(--accent-2)" stroke-width="1.6" stroke-dasharray="4 3"/>')
    p.append(f'<path d="M142 {CY - 40} l-11 2 l4 8 z" fill="var(--accent-2)"/>')
    return "".join(p)


def nucleo_ciclado():
    """Onda de siete días: tres altos, tres bajos y uno medio."""
    dias = [1.0, 0.25, 0.25, 0.62, 1.0, 0.25, 0.25]
    p = [f'<path d="M46 {CY + 30} H154" fill="none" stroke="var(--accent)" '
         'stroke-width="1.2" opacity=".55"/>']
    puntos = []
    for k, v in enumerate(dias):
        x = 50 + k * 17
        y = CY + 26 - v * 48
        puntos.append((x, y))
        p.append(f'<rect x="{f(x - 5)}" y="{f(y)}" width="10" '
                 f'height="{f(CY + 30 - y)}" rx="1.6" fill="var(--accent)" '
                 f'opacity="{.18 + v * .35:.2f}"/>')
    p.append('<path d="M' + " L".join(f"{f(x)} {f(y)}" for x, y in puntos)
             + '" fill="none" stroke="var(--accent-2)" stroke-width="1.8" '
               'stroke-linejoin="round" stroke-linecap="round"/>')
    for x, y in puntos:
        p.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2.4" fill="var(--accent-2)"/>')
    return "".join(p)


def nucleo_suplementacion():
    """Retícula hexagonal con la cápsula en el centro: forma y dosis."""
    p = []
    for anillo, r in ((6, 34), (6, 52)):
        for k in range(anillo):
            ang = k * 60 + (30 if r == 52 else 0)
            hx, hy = pol(CX, CY, r, ang)
            p.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="4.5" fill="none" '
                     'stroke="var(--accent)" stroke-width="1" opacity=".5"/>')
            p.append(f'<path d="M{CX} {CY} L{f(hx)} {f(hy)}" fill="none" '
                     'stroke="var(--accent)" stroke-width=".7" opacity=".22"/>')
    p.append(f'<rect x="{CX - 26}" y="{CY - 11}" width="52" height="22" rx="11" '
             'fill="none" stroke="var(--accent)" stroke-width="2"/>')
    p.append(f'<path d="M{CX} {CY - 11} V{CY + 11}" fill="none" '
             'stroke="var(--accent)" stroke-width="1.4"/>')
    p.append(f'<path d="M{CX - 26} {CY - 11} a11 11 0 0 0 0 22 H{CX} V{CY - 11} Z" '
             'fill="var(--accent)" opacity=".45"/>')
    return "".join(p)


def nucleo_dos_fases():
    """Dos triángulos opuestos: definición y volumen en la misma pieza."""
    p = [f'<path d="M{CX - 8} {CY - 44} L{CX - 8} {CY + 8} L{CX - 54} {CY + 8} Z" '
         'fill="var(--accent)" fill-opacity=".18" stroke="var(--accent)" '
         'stroke-width="1.8" stroke-linejoin="round"/>',
         f'<path d="M{CX + 8} {CY + 44} L{CX + 8} {CY - 8} L{CX + 54} {CY - 8} Z" '
         'fill="var(--accent-2)" fill-opacity=".18" stroke="var(--accent-2)" '
         'stroke-width="1.8" stroke-linejoin="round"/>',
         f'<path d="M{CX - 58} {CY + 22} L{CX + 58} {CY - 22}" fill="none" '
         'stroke="var(--accent)" stroke-width=".9" stroke-dasharray="3 3" '
         'opacity=".5"/>']
    p.append(txt(CX - 30, CY + 26, "DEF", "rot", 8, "var(--accent)"))
    p.append(txt(CX + 30, CY - 18, "VOL", "rot", 8, "var(--accent-2)"))
    return "".join(p)


def nucleo_registro():
    """Cuadrícula de datos con la línea de tendencia."""
    p = []
    for k in range(5):
        y = CY - 40 + k * 20
        p.append(f'<path d="M{CX - 52} {f(y)} H{CX + 52}" fill="none" '
                 'stroke="var(--accent)" stroke-width=".7" opacity=".28"/>')
    for k in range(6):
        x = CX - 52 + k * 21
        p.append(f'<path d="M{f(x)} {CY - 40} V{CY + 40}" fill="none" '
                 'stroke="var(--accent)" stroke-width=".7" opacity=".18"/>')
    serie = [(0, 28), (1, 14), (2, 18), (3, -2), (4, -12), (5, -30)]
    pts = [(CX - 52 + k * 21, CY + v * 0.85) for k, v in serie]
    p.append('<path d="M' + " L".join(f"{f(x)} {f(y)}" for x, y in pts)
             + '" fill="none" stroke="var(--accent-2)" stroke-width="2.2" '
               'stroke-linejoin="round" stroke-linecap="round"/>')
    for x, y in pts:
        p.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="var(--accent-2)"/>')
    return "".join(p)


def nucleo_plato():
    """El plato repartido: la proporción mediterránea, no una comida dibujada."""
    p = [f'<circle cx="{CX}" cy="{CY}" r="46" fill="none" stroke="var(--accent)" '
         'stroke-width="2"/>',
         f'<circle cx="{CX}" cy="{CY}" r="38" fill="none" stroke="var(--accent)" '
         'stroke-width=".7" opacity=".3"/>']
    # mitad verdura, un cuarto proteína, un cuarto cereal
    sectores = [(0, 180, "var(--accent)", .3), (180, 270, "var(--accent-2)", .3),
                (270, 360, "var(--accent)", .14)]
    for a0, a1, color, op in sectores:
        x1, y1 = pol(CX, CY, 46, a0)
        x2, y2 = pol(CX, CY, 46, a1)
        grande = 1 if a1 - a0 > 180 else 0
        p.append(f'<path d="M{CX} {CY} L{f(x1)} {f(y1)} A46 46 0 {grande} 1 '
                 f'{f(x2)} {f(y2)} Z" fill="{color}" opacity="{op}" '
                 f'stroke="{color}" stroke-width="1.2"/>')
    p.append(txt(CX + 26, CY - 8, "½", "rot", 13, "var(--accent)"))
    p.append(txt(CX - 24, CY + 20, "¼", "rot", 11, "var(--accent-2)"))
    p.append(txt(CX + 22, CY + 20, "¼", "rot", 11, "var(--accent)"))
    return "".join(p)


def nucleo_hiit():
    """Escalón de trabajo y descanso con la curva de pulso encima."""
    p = [f'<path d="M46 {CY + 34} H154" fill="none" stroke="var(--accent)" '
         'stroke-width="1.2" opacity=".5"/>']
    x = 50
    onda = []
    for k in range(4):
        onda += [(x, CY + 32), (x, CY - 6), (x + 12, CY - 6), (x + 12, CY + 32)]
        p.append(f'<rect x="{f(x)}" y="{f(CY - 6)}" width="12" height="38" '
                 'rx="1.6" fill="var(--accent)" opacity=".3"/>')
        x += 26
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in onda)
             + '" fill="none" stroke="var(--accent)" stroke-width="1.8" '
               'stroke-linejoin="miter"/>')
    pulso = [(48, CY - 24), (60, CY - 44), (74, CY - 20), (86, CY - 48),
             (100, CY - 22), (112, CY - 50), (126, CY - 24), (140, CY - 46),
             (152, CY - 28)]
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in pulso)
             + '" fill="none" stroke="var(--accent-2)" stroke-width="1.8" '
               'stroke-linejoin="round" stroke-linecap="round"/>')
    p.append(txt(CX, CY + 46, "TRABAJO · DESCANSO", "rot", 7.2, "var(--ink-3)"))
    return "".join(p)


def nucleo_barra():
    """Barra y discos reducidos a geometría: la única figura que sí es objeto."""
    p = [f'<path d="M{CX - 62} {CY} H{CX + 62}" fill="none" '
         'stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>']
    for signo in (-1, 1):
        for k, (dx, h) in enumerate(((44, 46), (52, 34), (58, 22))):
            x = CX + signo * dx
            p.append(f'<rect x="{f(x - 3.5)}" y="{f(CY - h / 2)}" width="7" '
                     f'height="{f(h)}" rx="2" fill="var(--accent)" '
                     f'opacity="{.85 - k * .2:.2f}"/>')
        p.append(f'<rect x="{f(CX + signo * 36 - 2.5)}" y="{f(CY - 9)}" width="5" '
                 'height="18" rx="1.5" fill="var(--accent-2)" opacity=".8"/>')
    p.append(f'<path d="M{CX - 26} {CY - 22} H{CX + 26}" fill="none" '
             'stroke="var(--accent)" stroke-width=".8" stroke-dasharray="3 3" '
             'opacity=".45"/>')
    return "".join(p)


def nucleo_respiracion():
    """Espiral de la respiración pautada, con los cuatro tiempos marcados."""
    p = []
    pasos = []
    for k in range(220):
        t = k / 219
        r = 12 + t * 44
        ang = t * 720
        x, y = pol(CX, CY, r, ang)
        pasos.append(f"{'M' if k == 0 else 'L'}{f(x)} {f(y)}")
    p.append(f'<path d="{" ".join(pasos)}" fill="none" stroke="var(--accent)" '
             'stroke-width="1.6" opacity=".8"/>')
    for k, etq in enumerate(("4", "7", "8")):
        px, py = pol(CX, CY, 66, 90 + k * 120)
        p.append(f'<circle cx="{f(px)}" cy="{f(py)}" r="9" fill="none" '
                 'stroke="var(--accent-2)" stroke-width="1.4"/>')
        p.append(txt(px, py + 3.4, etq, "rot", 9, "var(--accent-2)"))
    p.append(f'<circle cx="{CX}" cy="{CY}" r="4" fill="var(--accent)"/>')
    return "".join(p)


def nucleo_sueno():
    """Cinco ciclos de sueño: el hipnograma comprimido a insignia."""
    fases = [0, -1, -2, -3, -2, -1, 0, -1, -3, -2, -1, 0, -1, -2, -1, 0, -1, -1, 0]
    p = [f'<path d="M46 {CY - 40} H154" fill="none" stroke="var(--accent)" '
         'stroke-width=".7" opacity=".25"/>']
    pts = []
    for k, v in enumerate(fases):
        x = 48 + k * 5.7
        y = CY - 38 + (-v) * 19
        pts.append((x, y))
    p.append('<path d="M' + " L".join(f"{f(a)} {f(b)}" for a, b in pts)
             + '" fill="none" stroke="var(--accent)" stroke-width="1.8" '
               'stroke-linejoin="round"/>')
    for k in range(4):
        y = CY - 38 + k * 19
        p.append(f'<path d="M44 {f(y)} H50" fill="none" stroke="var(--accent-2)" '
                 'stroke-width="1.2" opacity=".7"/>')
    p.append(f'<path d="M124 {CY - 40} A34 34 0 1 1 124 {CY + 28} '
             f'A26 26 0 1 0 124 {CY - 40} Z" fill="var(--accent-2)" '
             'opacity=".16"/>')
    p.append(txt(CX, CY + 46, "5 CICLOS · 90 MIN", "rot", 7.2, "var(--ink-3)"))
    return "".join(p)


def nucleo_coaching():
    """Dos anillos enlazados y un eje: el que guía y el que ejecuta."""
    p = [f'<circle cx="{CX - 20}" cy="{CY}" r="34" fill="none" '
         'stroke="var(--accent)" stroke-width="2"/>',
         f'<circle cx="{CX + 20}" cy="{CY}" r="34" fill="none" '
         'stroke="var(--accent-2)" stroke-width="2"/>',
         f'<circle cx="{CX - 20}" cy="{CY}" r="26" fill="none" '
         'stroke="var(--accent)" stroke-width=".7" opacity=".3"/>',
         f'<circle cx="{CX + 20}" cy="{CY}" r="26" fill="none" '
         'stroke="var(--accent-2)" stroke-width=".7" opacity=".3"/>']
    p.append(f'<path d="M{CX} {CY - 52} V{CY + 52}" fill="none" '
             'stroke="var(--accent)" stroke-width="1" stroke-dasharray="4 3" '
             'opacity=".5"/>')
    p.append(f'<circle cx="{CX}" cy="{CY}" r="5" fill="var(--accent)"/>')
    p.append(txt(CX - 46, CY + 50, "GUÍA", "rot", 8, "var(--accent)"))
    p.append(txt(CX + 46, CY + 50, "TÚ", "rot", 8, "var(--accent-2)"))
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
EMBLEMAS = [
    ("em-volumen", nucleo_volumen, "SUPERÁVIT", "Volumen limpio", 4, "semanas"),
    ("em-ciclado", nucleo_ciclado, "CICLADO", "Siete días", 7, "días"),
    ("em-suplementacion", nucleo_suplementacion, "SUPLEMENTOS", "Dosis y momento", None, ""),
    ("em-dos-fases", nucleo_dos_fases, "DOS FASES", "Definir y construir", 8, "semanas"),
    ("em-registro", nucleo_registro, "REGISTRO", "Medir para corregir", 12, "semanas"),
    ("em-plato", nucleo_plato, "MEDITERRÁNEA", "El plato repartido", 4, "semanas"),
    ("em-hiit", nucleo_hiit, "INTERVALOS", "Trabajo y descanso", 10, "rutinas"),
    ("em-barra", nucleo_barra, "PROGRESIÓN", "Carga y descarga", 8, "semanas"),
    ("em-respiracion", nucleo_respiracion, "ATENCIÓN", "Respiración pautada", 21, "días"),
    ("em-sueno", nucleo_sueno, "DESCANSO", "Cinco ciclos", 7, "noches"),
    ("em-coaching", nucleo_coaching, "ACOMPAÑAMIENTO", "Guía semanal", 12, "semanas"),
]


def main():
    piezas = ['<svg xmlns="http://www.w3.org/2000/svg" '
              'style="position:absolute;width:0;height:0;overflow:hidden" '
              'aria-hidden="true">',
              """
<!-- ════════════════════════════════════════════════════════════════
     VILLUMINATION 99 · emblemas de portada
     Dibujo original — generado por tools/dibujar-emblemas.py.
     No editar a mano.
     ════════════════════════════════════════════════════════════ -->""",
              '<style>'
              "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
              ' letter-spacing:.12em }'
              "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
              '</style>']
    for clave, nucleo, l1, l2, conteo, unidad in EMBLEMAS:
        piezas.append(emblema(clave, nucleo(), l1, l2, conteo, unidad))
    piezas.append("</svg>")
    DESTINO.write_text("\n".join(piezas) + "\n")
    print(f"  {DESTINO.relative_to(RAIZ)}: {len(EMBLEMAS)} emblemas · "
          f"{DESTINO.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
