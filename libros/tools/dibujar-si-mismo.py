#!/usr/bin/env python3
"""
CÓDICE DEL SÍ MISMO — generador del repertorio gráfico
======================================================
Escribe partials/si-mismo.svg. Dibujo original de VILLUMINATION 99.

Seis láminas sobre atención y observación de sí: la atención dividida, los
tres centros, el bucle de identificación, el reloj de los recuerdos, las dos
respiraciones pautadas y el mapa de las cuatro emociones difíciles.

    python3 tools/dibujar-si-mismo.py
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "partials" / "si-mismo.svg"

VIO = "#a97bff"        # el acento de este libro
CLARO = "#c2c9dc"
APAGADO = "#8a93ab"
CALIDO = "#ffb35c"     # se reserva para señalar la salida del bucle

# Media silueta, la misma que en las otras láminas de la casa: se dibuja un
# lado y se refleja, así la figura es simétrica y solo hay un contorno.
MITAD = ("M72 30 L52 36 L42 44 L36 74 L30 114 L35 120 L43 80 L49 50 "
         "L47 96 L43 128 L39 180 L43 197 L41 243 L53 248 L55 243 "
         "L59 197 L63 151 L72 139")


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, grados):
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def txt(x, y, s, clase="et", tam=11, color=CLARO, anchor="middle"):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}">{s}</text>')


def flecha(x, y, ang, lado=9, color=VIO):
    return (f'<g transform="translate({f(x)},{f(y)}) rotate({f(ang)})" '
            f'fill="{color}"><path d="M{f(lado)} 0 L{f(-lado * .6)} {f(lado * .62)} '
            f'L{f(-lado * .6)} {f(-lado * .62)} Z"/></g>')


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 1 · LA ATENCIÓN DIVIDIDA
# ══════════════════════════════════════════════════════════════════════
def lamina_atencion():
    p = ['<symbol id="sm-atencion" viewBox="0 0 464 268">']
    for lado, (titulo, glosa) in enumerate((
            ("ATENCIÓN CORRIENTE", "toda hacia fuera · nadie en casa"),
            ("ATENCIÓN DIVIDIDA", "una parte en la tarea, otra en quien la hace"))):
        ox = lado * 232
        p.append(f'<rect x="{ox + 10}" y="10" width="212" height="182" rx="10" '
                 f'fill="{VIO}" opacity=".05"/>')
        yo_x, yo_y = ox + 48, 100
        obj_x = ox + 176
        # el que observa
        p.append(f'<circle cx="{yo_x}" cy="{yo_y}" r="17" fill="none" '
                 f'stroke="{VIO}" stroke-width="1.6"/>')
        p.append(f'<circle cx="{yo_x}" cy="{yo_y}" r="4.5" fill="{VIO}"/>')
        p.append(txt(yo_x, yo_y + 34, "YO", "rot", 8.6, VIO))
        # la tarea
        p.append(f'<rect x="{obj_x - 24}" y="{yo_y - 22}" width="48" height="44" '
                 f'rx="6" fill="none" stroke="{APAGADO}" stroke-width="1.4"/>')
        p.append(txt(obj_x, yo_y + 44, "LA TAREA", "rot", 8.6, APAGADO))
        if lado == 0:
            p.append(f'<path d="M{yo_x + 22} {yo_y} H{obj_x - 36}" fill="none" '
                     f'stroke="{VIO}" stroke-width="4"/>')
            p.append(flecha(obj_x - 30, yo_y, 0, 10))
        else:
            # el haz se reparte: una rama sigue, otra vuelve sobre sí
            p.append(f'<path d="M{yo_x + 22} {yo_y} H{obj_x - 36}" fill="none" '
                     f'stroke="{VIO}" stroke-width="2.4"/>')
            p.append(flecha(obj_x - 30, yo_y, 0, 9))
            p.append(f'<path d="M{yo_x + 30} {yo_y - 4} C{yo_x + 62} {yo_y - 46} '
                     f'{yo_x - 12} {yo_y - 52} {yo_x - 6} {yo_y - 20}" fill="none" '
                     f'stroke="{CALIDO}" stroke-width="2.4"/>')
            p.append(flecha(yo_x - 5, yo_y - 22, 104, 9, CALIDO))
            p.append(txt(yo_x + 24, yo_y - 56, "y me veo hacerlo", "et", 10.6, CALIDO))
        p.append(txt(ox + 116, 220, titulo, "rot", 10.4, VIO))
        p.append(txt(ox + 116, 240, glosa, "et", 10.6, CLARO))
    p.append(txt(232, 262, "LA DIFERENCIA ENTRE LAS DOS ES TODO ESTE LIBRO",
                 "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 2 · LOS TRES CENTROS
# ══════════════════════════════════════════════════════════════════════
CENTROS = [
    ("INTELECTUAL", 22, "Cabeza", "El más lento",
     "Piensa, compara, decide. Llega tarde a todo."),
    ("EMOCIONAL", 70, "Pecho", "El más rápido",
     "Valora antes de entender. Ya ha reaccionado."),
    ("MOTOR E INSTINTIVO", 150, "Vientre y miembros", "El más constante",
     "Postura, respiración, hábito. Nunca se detiene."),
]


def lamina_centros():
    K, OX, OY = 1.18, 24, 34
    ALTO = int(OY + 262 * K + 26)
    p = [f'<symbol id="sm-centros" viewBox="0 0 464 {ALTO}">']
    p.append(f'<defs><g id="sc-mitad"><path d="{MITAD}"/></g></defs>')
    p.append(f'<g transform="translate({OX},{OY}) scale({f(K)})">')
    for relleno, trazo, op in ((VIO, "none", ".08"), ("none", VIO, ".5")):
        p.append(f'<g fill="{relleno}" fill-opacity="{op}" stroke="{trazo}" '
                 f'stroke-width=".9" stroke-opacity="{op}" '
                 'stroke-linejoin="round" stroke-linecap="round">'
                 '<circle cx="72" cy="17" r="11"/>'
                 '<use href="#sc-mitad"/>'
                 '<use href="#sc-mitad" transform="translate(144,0) scale(-1,1)"/>'
                 "</g>")
    p.append("</g>")

    centro_x = OX + 72 * K
    for i, (nombre, y_local, sede, ritmo, glosa) in enumerate(CENTROS):
        y = OY + y_local * K
        alto_banda = 34 if i < 2 else 96
        p.append(f'<rect x="{f(centro_x - 46)}" y="{f(y - 12)}" width="92" '
                 f'height="{alto_banda}" rx="10" fill="{VIO}" opacity=".13"/>')
        p.append(f'<path d="M{f(centro_x + 48)} {f(y + 4)} H206" fill="none" '
                 f'stroke="{VIO}" stroke-width=".8" stroke-dasharray="3 3" '
                 'opacity=".6"/>')
        p.append(f'<circle cx="{f(centro_x)}" cy="{f(y + 4)}" r="3" fill="{VIO}"/>')
        p.append(txt(214, y - 2, nombre, "rot", 10.4, VIO, "start"))
        p.append(txt(214, y + 13, f"{sede} · {ritmo}", "et", 10.6, CLARO, "start"))
        p.append(txt(214, y + 27, glosa, "et", 10.6, APAGADO, "start"))
    p.append(txt(232, ALTO - 6,
                 "TRES VELOCIDADES DISTINTAS EN EL MISMO CUERPO", "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 3 · EL BUCLE DE IDENTIFICACIÓN
# ══════════════════════════════════════════════════════════════════════
NODOS = [
    ("1", "ESTÍMULO", "algo pasa"),
    ("2", "REACCIÓN", "el cuerpo ya ha respondido"),
    ("3", "JUSTIFICACIÓN", "y además tenía razón"),
    ("4", "«SOY ASÍ»", "queda confirmado"),
]


def lamina_identificacion():
    """El bucle en cadena vertical.

    Se probó en anillo, con los cuatro nodos en cruz, y no funciona: las
    etiquetas de este y oeste no caben a los lados y la flecha de la pausa
    sale justo encima del rótulo de la reacción. En columna cada nodo tiene su
    ancho entero y la salida queda despejada a la derecha.
    """
    X, W, ALTO_F = 20, 268, 74
    p = ['<symbol id="sm-identificacion" viewBox="0 0 464 344">']
    for i, (num, nombre, glosa) in enumerate(NODOS):
        y = 14 + i * ALTO_F
        p.append(f'<rect x="{X}" y="{y}" width="{W}" height="54" rx="9" '
                 f'fill="{VIO}" opacity=".07"/>')
        p.append(f'<rect x="{X}" y="{y}" width="{W}" height="54" rx="9" '
                 f'fill="none" stroke="{VIO}" stroke-width=".9" opacity=".45"/>')
        p.append(f'<circle cx="{X + 28}" cy="{y + 27}" r="15" fill="none" '
                 f'stroke="{VIO}" stroke-width="1.3"/>')
        p.append(txt(X + 28, y + 32, num, "num", 14, VIO))
        p.append(txt(X + 54, y + 22, nombre, "rot", 10.4, VIO, "start"))
        p.append(txt(X + 54, y + 40, glosa, "et", 10.6, CLARO, "start"))
        if i < 3:
            p.append(f'<path d="M{X + 28} {y + 54} V{y + ALTO_F - 4}" fill="none" '
                     f'stroke="{VIO}" stroke-width="2"/>')
            p.append(flecha(X + 28, y + ALTO_F - 2, 90, 8))
    # El lazo de vuelta: del último nodo al primero, por la derecha del bloque.
    ult = 14 + 3 * ALTO_F + 27
    p.append(f'<path d="M{X + W} {ult} H{X + W + 22} V41 H{X + W}" fill="none" '
             f'stroke="{VIO}" stroke-width="1.6" opacity=".55"/>')
    p.append(flecha(X + W + 2, 41, 180, 8))
    p.append(txt(X + W + 34, 200, "y vuelve a empezar", "et", 10.4, APAGADO, "start"))
    # La salida, entre el 1 y el 2 y en el color reservado para ella.
    yp = 14 + ALTO_F - 20
    p.append(f'<path d="M{X + 34} {f(yp)} H400" fill="none" stroke="{CALIDO}" '
             'stroke-width="2.2" stroke-dasharray="6 4"/>')
    p.append(flecha(404, yp, 0, 9, CALIDO))
    p.append(txt(400, yp - 14, "LA PAUSA", "rot", 10.4, CALIDO, "end"))
    p.append(txt(456, yp + 18, "el único punto", "et", 10.4, CALIDO, "end"))
    p.append(txt(456, yp + 32, "con salida", "et", 10.4, CALIDO, "end"))
    p.append(txt(232, 338, "EL BUCLE SE CIERRA SOLO · LA PAUSA HAY QUE PONERLA",
                 "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 4 · EL RELOJ DE LOS RECUERDOS
# ══════════════════════════════════════════════════════════════════════
RECUERDOS = [
    (7,  "Al despertar"),
    (10, "Antes de empezar"),
    (13, "Antes de comer"),
    (16, "A media tarde"),
    (19, "Al terminar"),
    (23, "Antes de dormir"),
]
SUENO = (23.5, 7)          # tramo de descanso


def lamina_reloj():
    cx, cy, r = 232, 168, 100
    p = ['<symbol id="sm-reloj" viewBox="0 0 464 340">']

    def ang(hora):
        return (hora % 24) * 15      # 24 h en 360°

    # tramo de sueño, como sector tenue
    a0, a1 = ang(SUENO[0]), ang(SUENO[1]) + 360
    pasos_arco = []
    for k in range(int(a1 - a0) + 1):
        x, y = pol(cx, cy, r, a0 + k)
        pasos_arco.append(f"{'M' if k == 0 else 'L'}{f(x)} {f(y)}")
    p.append(f'<path d="{" ".join(pasos_arco)}" fill="none" stroke="{APAGADO}" '
             'stroke-width="22" opacity=".18" stroke-linecap="butt"/>')

    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{VIO}" '
             'stroke-width="1.4" opacity=".55"/>')
    # marcas horarias
    marcas = []
    for hora in range(24):
        largo = 11 if hora % 6 == 0 else 6
        x1, y1 = pol(cx, cy, r, ang(hora))
        x2, y2 = pol(cx, cy, r - largo, ang(hora))
        marcas.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    p.append(f'<path d="{" ".join(marcas)}" fill="none" stroke="{VIO}" '
             'stroke-width="1" opacity=".45"/>')
    for hora in (0, 6, 12, 18):
        hx, hy = pol(cx, cy, r - 22, ang(hora))
        p.append(txt(hx, hy + 4, f"{hora:02d}", "num", 10, APAGADO))

    for hora, etiqueta in RECUERDOS:
        px, py = pol(cx, cy, r, ang(hora))
        p.append(f'<circle cx="{f(px)}" cy="{f(py)}" r="7" fill="{CALIDO}"/>')
        # El sector decide el lado: a la derecha, a la izquierda o centrada
        # arriba y abajo. Sin este reparto las etiquetas de las tres y de las
        # nueve se salen de la lámina.
        a = ang(hora)
        ex, ey = pol(cx, cy, r + 18, a)
        if 20 < a < 160:
            p.append(txt(ex, ey + 4, etiqueta, "et", 10.6, CALIDO, "start"))
        elif 200 < a < 340:
            p.append(txt(ex, ey + 4, etiqueta, "et", 10.6, CALIDO, "end"))
        else:
            p.append(txt(ex, ey + (16 if 90 < a < 270 else -6), etiqueta,
                         "et", 10.6, CALIDO))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="30" fill="none" stroke="{VIO}" '
             'stroke-width="1" opacity=".4"/>')
    p.append(txt(cx, cy - 2, "SEIS", "rot", 10, VIO))
    p.append(txt(cx, cy + 13, "AL DÍA", "rot", 10, VIO))
    p.append(txt(232, 332, "MISMAS HORAS TODOS LOS DÍAS · TREINTA SEGUNDOS CADA UNA",
                 "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 5 · LAS DOS RESPIRACIONES
# ══════════════════════════════════════════════════════════════════════
PAUTAS = [
    ("4 · 7 · 8", "para bajar", [("Inhalar", 4, VIO), ("Retener", 7, APAGADO),
                                 ("Exhalar", 8, CALIDO)]),
    ("4 · 4 · 4 · 4", "para sostener", [("Inhalar", 4, VIO), ("Retener", 4, APAGADO),
                                        ("Exhalar", 4, CALIDO), ("Vacío", 4, APAGADO)]),
]


def lamina_respiracion():
    p = ['<symbol id="sm-respiracion" viewBox="0 0 464 236">']
    for i, (nombre, para, tramos) in enumerate(PAUTAS):
        y = 34 + i * 108
        total = sum(t[1] for t in tramos)
        ancho = 340
        x = 100
        p.append(txt(92, y + 22, nombre, "rot", 11, VIO, "end"))
        p.append(txt(92, y + 38, para, "et", 10.6, APAGADO, "end"))
        for etiqueta, cuentas, color in tramos:
            w = ancho * cuentas / total
            p.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w - 3)}" height="34" '
                     f'rx="5" fill="{color}" opacity=".2"/>')
            p.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w - 3)}" height="34" '
                     f'rx="5" fill="none" stroke="{color}" stroke-width="1"/>')
            p.append(txt(x + w / 2 - 1.5, y + 21, str(cuentas), "num", 12, color))
            p.append(txt(x + w / 2 - 1.5, y + 50, etiqueta, "rot", 8, color))
            x += w
        p.append(f'<path d="M100 {f(y + 62)} H440" fill="none" stroke="{VIO}" '
                 'stroke-width=".6" opacity=".25"/>')
    p.append(txt(232, 228, "SE CUENTA A UN TIEMPO POR SEGUNDO · CUATRO CICLOS",
                 "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 6 · LAS CUATRO DIFÍCILES
# ══════════════════════════════════════════════════════════════════════
EMOCIONES = [
    ("MIEDO", "Pecho apretado, respiración alta", "Avisa de un riesgo",
     "Anticipar lo que no ha pasado"),
    ("IRA", "Mandíbula, puños, calor en la cara", "Avisa de un límite pisado",
     "Convertirse en juicio sobre alguien"),
    ("TRISTEZA", "Peso, garganta, ganas de retirarse", "Avisa de una pérdida",
     "Volverse relato sobre uno mismo"),
    ("VERGÜENZA", "Calor, ganas de desaparecer", "Avisa de una norma propia",
     "Extenderse de un acto a la identidad"),
]


def lamina_emociones():
    p = ['<symbol id="sm-emociones" viewBox="0 0 464 344">']
    for i, (nombre, cuerpo, avisa, riesgo) in enumerate(EMOCIONES):
        x = 10 + (i % 2) * 228
        y = 12 + (i // 2) * 152
        p.append(f'<rect x="{x}" y="{y}" width="216" height="138" rx="10" '
                 f'fill="{VIO}" opacity=".06"/>')
        p.append(f'<rect x="{x}" y="{y}" width="216" height="138" rx="10" '
                 f'fill="none" stroke="{VIO}" stroke-width=".9" opacity=".4"/>')
        p.append(txt(x + 14, y + 24, nombre, "rot", 11.5, VIO, "start"))
        p.append(f'<path d="M{x + 14} {y + 32} H{x + 202}" fill="none" '
                 f'stroke="{VIO}" stroke-width=".7" opacity=".35"/>')
        for k, (rot, valor, color) in enumerate((
                ("EN EL CUERPO", cuerpo, CLARO),
                ("PARA QUÉ SIRVE", avisa, CALIDO),
                ("DÓNDE SE TUERCE", riesgo, APAGADO))):
            yy = y + 52 + k * 30
            p.append(txt(x + 14, yy, rot, "rot", 7.2, color, "start"))
            p.append(txt(x + 14, yy + 13, valor, "et", 10.2, color, "start"))
    p.append(txt(232, 336,
                 "NI EXPRESARLAS NI REPRIMIRLAS · MIRARLAS HASTA QUE PASEN",
                 "rot", 8.4, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
def main():
    piezas = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'style="position:absolute;width:0;height:0;overflow:hidden" '
        'aria-hidden="true">',
        """
<!-- ════════════════════════════════════════════════════════════════
     CÓDICE DEL SÍ MISMO · repertorio gráfico
     Dibujo original de VILLUMINATION 99 — generado por
     tools/dibujar-si-mismo.py. No editar a mano.
     ════════════════════════════════════════════════════════════ -->""",
        '<style>'
        "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
        ' letter-spacing:.1em }'
        "svg .num{ font-family:'Orbitron',sans-serif; font-weight:600 }"
        "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
        '</style>',
        lamina_atencion(),
        lamina_centros(),
        lamina_identificacion(),
        lamina_reloj(),
        lamina_respiracion(),
        lamina_emociones(),
        "</svg>",
    ]
    DESTINO.write_text("\n".join(piezas) + "\n")
    print(f"  {DESTINO.relative_to(RAIZ)}: 6 láminas · "
          f"{DESTINO.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
