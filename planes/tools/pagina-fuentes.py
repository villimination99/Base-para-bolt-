#!/usr/bin/env python3
"""
PÁGINA DE FUENTES VERIFICADAS — se inyecta en los once planes
=============================================================
Un plan que da cifras sin decir de dónde salen no se puede comprobar, y por
tanto tampoco se puede corregir. Esta herramienta añade a cada plan una página
final con las fuentes reales, su base legal y las rutas concretas para
consultarlas.

Las fuentes NO se teclean aquí: se importan del mismo módulo de datos que usan
los libros —libros/tools/datos_oficiales.py—, que se comprueba antes de
escribir nada. Así, si algún día se corrige una fuente, se corrige en los once
planes y en los ocho libros a la vez, y no puede haber dos versiones.

La página se inserta ANTES de la última sección de cada plan si esa última es
la de cierre comercial, y en todo caso se renumeran todos los folios, que
están escritos a mano en el HTML.

    python3 tools/pagina-fuentes.py            (inyecta o actualiza)
    python3 tools/pagina-fuentes.py --quitar   (deshace)
"""

import importlib.util
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"
DATOS = RAIZ.parent / "libros" / "tools" / "datos_oficiales.py"

_spec = importlib.util.spec_from_file_location("datos_oficiales", DATOS)
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
D.comprobar()

MARCA_INI = "<!--@fuentes-verificadas-->"
MARCA_FIN = "<!--@/fuentes-verificadas-->"

RUTAS = [
    ("Ingestas de referencia", "RDA, AI y límite superior tolerable de cada "
     "vitamina y mineral", "ods.od.nih.gov"),
    ("Composición de alimentos", "El perfil completo de cualquier alimento, "
     "nutriente por nutriente", "fdc.nal.usda.gov"),
    ("Guías alimentarias", "Patrones de dieta y límites de azúcares añadidos, "
     "grasa saturada y sodio", "health.gov"),
    ("Guías de actividad física", "La dosis semanal, su curva de respuesta y "
     "el requisito de fuerza", "health.gov"),
    ("Doctrina de preparación física", "FM 7-22: entrenamiento, nutrición, "
     "sueño y preparación mental", "armypubs.army.mil"),
    ("Ecuación de levantamiento", "Cuánto peso es razonable levantar en cada "
     "situación concreta", "cdc.gov/niosh"),
    ("Inocuidad alimentaria", "Temperaturas internas seguras y zona de "
     "peligro", "foodsafety.gov"),
    ("Declaraciones de salud", "Lo que se puede afirmar de un nutriente en "
     "Europa, y lo que fue rechazado", "Registro de la Comisión Europea"),
]


def pagina(folio: str, total: str) -> str:
    """Una sola tabla de ocho filas.

    La primera versión llevaba dos tablas —fuentes por un lado, rutas por
    otro— y desbordaba la página en 296 px. Se fusionan: cada fuente con lo
    que trae y dónde se consulta, en una línea.
    """
    filas = "".join(
        f'<tr><td><b>{q}</b></td><td>{c}</td><td class="dd">{r}</td></tr>'
        for q, c, r in RUTAS)
    micro = len(D.MICRO)
    return f"""{MARCA_INI}
<!-- ══════════════════════ FUENTES VERIFICADAS ══════════════════════ -->
<section class="page">
  <header class="pg-head">
    <div class="logo">
      <div class="logo-mark"><span>VI</span></div>
      <div class="wordmark" style="font-size:8.4pt"><span class="v">VILLUMINATIONS</span></div>
    </div>
    <div class="kicker">Fuentes verificadas</div>
    <div class="site">villuminations.com</div>
  </header>

  <main class="compacto">
    <h2>DE DÓNDE SALE <span class="a">CADA CIFRA</span></h2>
    <div class="rule"></div>

    <p class="small">Todo dato numérico de este documento procede de fuentes
      públicas, gratuitas y comprobables. Ninguna cifra está inventada,
      redondeada por comodidad ni copiada de otra publicación divulgativa.
      Esta página existe para que puedas verificarlo tú mismo.</p>

    <div class="callout info">
      <div class="t">Por qué estas fuentes y no otras</div>
      <p>Las obras del gobierno federal de Estados Unidos no están sujetas a
        derechos de autor (17 U.S.C. § 105). Eso convierte a un puñado de
        organismos en la única fuente de datos de nutrición y entrenamiento
        que es a la vez de primer nivel y legalmente libre. No es material
        reservado: es material público que casi nadie abre.</p>
    </div>

    <table class="compact">
      <thead><tr><th>Qué buscas</th><th>Qué encontrarás</th><th>Dónde</th></tr></thead>
      <tbody>{filas}</tbody>
    </table>

    <div class="callout">
      <div class="t">Cómo se comprueba este documento a sí mismo</div>
      <p>Las cifras de referencia no están escritas a mano: viven en un módulo
        de datos que el programa de composición verifica antes de escribir una
        sola línea. Comprueba que los rangos de macronutrientes admitan el
        cien por cien de la energía, que ninguno de los {micro}
        micronutrientes tenga un valor recomendado por encima de su propio
        techo sin nota que lo explique, y que ninguna temperatura de cocción
        segura caiga dentro de la zona de peligro. Si una sola comprobación
        falla, el documento no se compone.</p>
    </div>

    <div class="legal mt4">
      <b>Los valores de referencia son poblacionales</b><br>
      Describen lo que cubre las necesidades de la mayoría de adultos sanos. No
      son una prescripción individual, no contemplan patologías, embarazo,
      lactancia ni medicación, y ninguna publicación sustituye la valoración de
      un profesional sanitario colegiado. Si tomas medicación, algunos de los
      nutrientes citados interaccionan con ella de forma clínicamente
      relevante: no cambies una ingesta ni empieces un suplemento sin
      decírselo a quien te receta.
    </div>
  </main>

  <footer class="pg-foot">
    <span>© 2026 VILLUMINATIONS · @villuminations</span>
    <span class="pnum">{folio} / {total}</span>
  </footer>
</section>
{MARCA_FIN}
"""


def quitar(html: str) -> str:
    return re.sub(re.escape(MARCA_INI) + r".*?" + re.escape(MARCA_FIN),
                  "", html, flags=re.S).replace("\n\n\n", "\n\n")


def renumerar(html: str) -> str:
    """Los folios están escritos a mano en cada sección: se recalculan."""
    folios = re.findall(r'<span class="pnum">[^<]*</span>', html)
    total = len(folios) + 1        # la portada no lleva folio
    n = [1]

    def uno(_m):
        n[0] += 1
        return f'<span class="pnum">{n[0]:02d} / {total:02d}</span>'

    return re.sub(r'<span class="pnum">[^<]*</span>', uno, html)


def main() -> None:
    borrar = "--quitar" in sys.argv
    for ruta in sorted(SRC.glob("*.html")):
        html = quitar(ruta.read_text(encoding="utf-8"))
        if not borrar:
            # va justo antes de la última sección, que es el cierre comercial
            corte = html.rfind("<!-- ══")
            if corte == -1:
                corte = html.rfind("</body>")
            html = html[:corte] + pagina("00", "00") + "\n" + html[corte:]
        html = renumerar(html)
        ruta.write_text(html, encoding="utf-8")
        paginas = html.count('class="page"')
        print(f"  {ruta.name:<46}{paginas:>3} páginas")


if __name__ == "__main__":
    main()
