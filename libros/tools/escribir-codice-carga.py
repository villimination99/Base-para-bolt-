#!/usr/bin/env python3
"""
CÓDICE DE LA CARGA — obra original de VILLUMINATIONS
======================================================
Sexto libro de la colección y segundo de la serie de fitness. Entrenamiento
adulto a partir de fuentes públicas y libres: Physical Activity Guidelines for
Americans (2.ª ed.), FM 7-22 del Ejército de Estados Unidos, la ecuación de
levantamiento del NIOSH y la investigación en descarga de la NASA. Todas ellas
son obra del gobierno federal estadounidense y por tanto no están sujetas a
copyright (17 U.S.C. § 105).

Las cifras NO se teclean aquí: vienen de tools/datos_oficiales.py, que se
comprueba antes de escribir nada.

    python3 tools/escribir-codice-carga.py && python3 build.py carga
"""

import importlib.util
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"

_spec = importlib.util.spec_from_file_location(
    "datos_oficiales", Path(__file__).with_name("datos_oficiales.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
D.comprobar()

A = D.ACTIVIDAD
MET = {n: (m, b) for n, m, b in D.MET}


# ── Atajos ────────────────────────────────────────────────────────────
def p(t):        return {"t": "p", "x": t}
def h(t):        return {"t": "h2", "x": t}
def ficha(tit, filas): return {"t": "ficha", "tit": tit, "x": filas}
def lista(*i):   return {"t": "lista", "x": list(i)}
def pasos(*i):   return {"t": "pasos", "x": list(i)}
def nota(tit, t): return {"t": "nota", "tit": tit, "x": t}
def sep():       return {"t": "sep"}


def fig(simbolo, tit, pie, clase=""):
    return {"t": "figura", "x": simbolo, "tit": tit, "pie": pie, "clase": clase}


def cap(titulo, *bloques):
    return {"titulo": titulo, "bloques": [b for b in bloques if b]}


def dec(x):
    """Coma decimal, que es la que corresponde en español. Sin esto los MET
    salían impresos como «3.5» en un libro escrito en castellano."""
    return f"{x:g}".replace(".", ",")


def kcal(met, peso, minutos):
    """Gasto aproximado: un MET es una kcal por kilo y hora. Se calcula, no se
    teclea, para que ningún ejemplo del texto contradiga la escala."""
    return round(met * peso * minutos / 60)


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · LA DOSIS
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "Existe una dosis, y está escrita",
    p("Hay una cifra de actividad física establecida por un gobierno, publicada "
      "en un documento gratuito de varios cientos de páginas, revisada por un "
      "comité científico y actualizada por última vez en 2018. Casi todo el mundo "
      "ha oído su titular y casi nadie ha leído lo que hay debajo, que es donde "
      "están las cosas útiles."),
    h("La afirmación de este libro"),
    p("El entrenamiento tiene una dosis mínima conocida, un tramo especialmente "
      "rentable y una forma de curva. Saber esas tres cosas cambia por completo "
      "las decisiones de alguien que empieza, porque la mayor parte del beneficio "
      "no está donde la gente cree que está: está en los primeros minutos, no en "
      "los últimos."),
    ficha("La dosis, en una tabla", [
        ("Actividad moderada", f"de {A['moderada_min']} a {A['moderada_max']} "
                               "minutos por semana"),
        ("Actividad vigorosa", f"de {A['vigorosa_min']} a {A['vigorosa_max']} "
                               "minutos por semana"),
        ("Equivalencia", f"un minuto vigoroso cuenta como "
                         f"{A['equivalencia']} moderados"),
        ("Fuerza", f"al menos {A['fuerza_dias']} días por semana, todos los "
                   "grandes grupos musculares"),
    ]),
    h("Lo que este libro no afirma"),
    lista(
        "No es un programa de entrenamiento personalizado. Es el marco dentro "
        "del cual cualquier programa razonable cae, y una manera de juzgar los "
        "que te ofrezcan.",
        "No promete resultados estéticos ni plazos. Ninguna cifra de aquí lleva "
        "asociada una fecha, y cualquier plan que sí la lleve está inventándola.",
        "No sustituye a un profesional. Si tienes una enfermedad cardiovascular, "
        "respiratoria o metabólica conocida, si estás embarazada, si te has "
        "operado hace poco o si has estado meses sin actividad, la conversación "
        "empieza en una consulta y no en un libro.",
        "No trata el entrenamiento de alto rendimiento. Las guías están escritas "
        "para la salud de la población, y ese es exactamente su valor: son la "
        "base sobre la que se construye todo lo demás.",
    ),
    nota("La señal de alarma que se explica una sola vez",
         "Dolor en el pecho, opresión, dolor que baja por el brazo o la "
         "mandíbula, falta de aire desproporcionada al esfuerzo, mareo o "
         "palpitaciones irregulares durante el ejercicio: se para y se consulta "
         "el mismo día. Ninguna sesión merece la duda. Es la única frase de este "
         "libro que hay que recordar de memoria."),
    sep(),
    h("De dónde sale todo lo que sigue"),
    p("De cuatro fuentes públicas del gobierno federal de Estados Unidos, que por "
      "ley no están sujetas a copyright: las guías de actividad física, el manual "
      "de campo de salud y preparación física del Ejército, la ecuación de "
      "levantamiento del instituto nacional de seguridad laboral y la "
      "investigación de la agencia espacial sobre lo que le ocurre a un cuerpo al "
      "que se le quita el peso. Las cuatro se citan por su nombre en el capítulo "
      "de comprobación, con indicación de dónde se descargan."),
    p("Y una cosa más: las cifras de estas páginas no se teclearon en el texto. "
      "Viven en un módulo de datos que se verifica antes de componer el libro. Si la equivalencia entre minutos moderados y "
      "vigorosos no cuadrase, o si alguna actividad de la escala metabólica "
      "cayese fuera de la banda de intensidad que declara, el libro no se "
      "escribiría."),
)

C2 = cap(
    "La forma de la curva",
    p("El titular de las guías es la cifra de ciento cincuenta minutos. La parte "
      "que casi nadie cita es cómo se comporta el beneficio a lo largo del rango, "
      "y esa forma es la información más accionable de todo el documento."),
    fig("ca-dosis",
        "La curva de respuesta: el tramo rentable está al principio",
        "El beneficio no crece en línea recta con los minutos: sube muy deprisa "
        "al principio y se va aplanando. La zona marcada hasta los ciento "
        "cincuenta minutos es la de mayor rendimiento por minuto invertido; a "
        "partir de los trescientos el beneficio sigue creciendo, pero cada minuto "
        "añadido rinde menos que el anterior. La curva dibuja la forma que "
        "describen las guías, no un ajuste de datos concretos."),
    h("Las tres lecturas de esta lámina"),
    ficha("", [
        ("Primera", "No existe un umbral por debajo del cual no haya beneficio. "
                    "La curva empieza a subir desde el minuto uno, y el mayor "
                    "salto de toda la gráfica ocurre entre no hacer nada y hacer "
                    "poco."),
        ("Segunda", "El tramo más rentable es el que va de cero a la "
                    "recomendación. Quien está en cuarenta minutos semanales y "
                    "sube a noventa gana más que quien está en trescientos y sube "
                    "a trescientos cincuenta."),
        ("Tercera", "Pasarse de la recomendación no es malo. Por encima del "
                    "máximo del rango el beneficio sigue subiendo; simplemente "
                    "deja de compensar tanto, y el coste de tiempo y de lesión "
                    "empieza a pesar."),
    ]),
    p("De aquí sale el consejo más contraintuitivo del libro para alguien que "
      "empieza: no diseñes la semana que te gustaría hacer. Diseña la que harás "
      "aunque salga mal, porque los primeros minutos son los que más valen y son "
      "precisamente los que se pierden cuando el plan es demasiado ambicioso y se "
      "abandona en la semana tres. Cuánto se cumple pesa más que qué se elige, "
      "y por eso el capítulo de la semana da tres plantillas de tamaños "
      "distintos en vez de una sola."),
    sep(),
    h("Lo que cambió en la segunda edición, y que casi nadie sabe"),
    p("Durante años se recomendó que la actividad se acumulara en tandas de al "
      "menos diez minutos, y esa regla se repitió tanto que sigue viva en "
      "aplicaciones y en gimnasios. La segunda edición de las guías la eliminó: "
      "ahora cuenta toda la actividad, desde el primer minuto."),
    p("El cambio parece administrativo y no lo es. Convierte en válidas las "
      "escaleras en vez del ascensor, los siete minutos andando hasta la parada "
      "siguiente, los cuatro minutos de subir la compra. Para una persona con "
      "poco tiempo, esa regla derogada era la que hacía inalcanzable la "
      "recomendación, y su desaparición es probablemente la noticia más útil de "
      "todo el documento."),
    lista(
        "También se reforzó el mensaje sobre el tiempo sentado: reducirlo tiene "
        "beneficio propio, y parte del riesgo asociado al sedentarismo se atenúa "
        "con actividad, aunque no se elimina del todo.",
        "Y se subrayó que algunos beneficios aparecen de forma inmediata —una "
        "sola sesión mejora el sueño de esa noche, la ansiedad, la sensibilidad a "
        "la insulina y la presión arterial durante horas—, no solo después de "
        "meses de constancia. Es un argumento distinto al habitual y funciona "
        "mejor con quien no cree en los plazos largos.",
    ),
)

C3 = cap(
    "La moneda de la intensidad",
    p("Para poder sumar minutos hay que saber cuáles cuentan, y para eso existe "
      "una unidad: el equivalente metabólico. Un MET es el gasto en reposo "
      "sentado. Todo lo demás se expresa como un múltiplo de eso."),
    fig("ca-met",
        "La escala metabólica con sus dos umbrales oficiales",
        f"Un MET equivale al gasto en reposo. La actividad se considera moderada "
        f"a partir de {str(D.UMBRAL_MET['moderada']).replace('.', ',')} MET y "
        f"vigorosa a partir de "
        f"{str(D.UMBRAL_MET['vigorosa']).replace('.', ',')}. Los dos umbrales son "
        "los que usan las guías para clasificar, y son la razón por la que un "
        "paseo tranquilo no cuenta y uno a paso vivo sí."),
    ficha("Los dos umbrales", [
        ("Ligera", f"por debajo de {str(D.UMBRAL_MET['moderada']).replace('.', ',')} "
                   "MET. Cuenta para reducir el tiempo sentado, no para la dosis "
                   "semanal."),
        ("Moderada", f"de {str(D.UMBRAL_MET['moderada']).replace('.', ',')} a "
                     f"{str(D.UMBRAL_MET['vigorosa']).replace('.', ',')} MET. Es "
                     "la moneda de la recomendación."),
        ("Vigorosa", f"a partir de {str(D.UMBRAL_MET['vigorosa']).replace('.', ',')} "
                     f"MET. Cada minuto vale por {A['equivalencia']}."),
    ]),
    h("La prueba del habla, que no necesita reloj"),
    p("Los umbrales tienen una traducción práctica que funciona sorprendentemente "
      "bien y que no requiere pulsómetro ni tabla:"),
    lista(
        "Si puedes hablar pero no cantar, estás en moderada.",
        "Si no puedes decir más de unas pocas palabras seguidas sin coger aire, "
        "estás en vigorosa.",
        "Si puedes cantar cómodamente, estás en ligera y no cuenta para la dosis.",
    ),
    p("Esta prueba tiene una ventaja sobre el valor de la tabla: es relativa a "
      "quien la hace. Los MET son un promedio poblacional, y caminar a cinco "
      "kilómetros por hora es moderado para el adulto medio y vigoroso para "
      "alguien muy desentrenado o de edad avanzada. La intensidad que cuenta para "
      "la salud es la relativa, y las guías lo dicen explícitamente."),
    sep(),
    h("Para qué sirve de verdad un MET"),
    p("Sirve para estimar el gasto, porque un MET equivale aproximadamente a una "
      "kilocaloría por kilo de peso y por hora. La fórmula completa cabe en una "
      "línea: MET por kilos por horas."),
    ficha("Media hora, en una persona de 70 kilos", [
        (nombre, f"{dec(MET[nombre][0])} MET · unas "
                 f"{kcal(MET[nombre][0], 70, 30)} kcal · {MET[nombre][1]}")
        for nombre in ("Caminar a paso vivo · 5 km/h", "Pesas, sesión general",
                       "Bicicleta · 20 km/h", "Trotar · 8 km/h",
                       "Correr · 11 km/h")
    ]),
    nota("Por qué estas cifras son más pequeñas de lo que esperabas",
         "Porque casi todas las máquinas de gimnasio exageran, y porque el "
         "número que interesa es el gasto NETO —lo que se gasta de más respecto a "
         "estar sentado— y no el bruto. Media hora de carrera decente ronda las "
         "cuatrocientas kilocalorías en una persona de setenta kilos, no las "
         "ochocientas del display. Esta es la aritmética que explica por qué "
         "intentar compensar la comida con ejercicio sale casi siempre mal: el "
         "cuerpo gasta despacio y come rápido."),
)

C4 = cap(
    "El corazón y la zona que no existe",
    p("Cualquier máquina de gimnasio dibuja en su pantalla una franja rotulada "
      "«zona de quema de grasa», siempre por debajo de la franja de al lado. Es "
      "verdad y es inútil a la vez, y la mezcla de las dos cosas la convierte en "
      "la desinformación más extendida del entrenamiento."),
    h("Lo que sí es cierto"),
    p("A intensidad baja, la proporción de la energía que el cuerpo saca de las "
      "grasas es mayor. A intensidad alta, esa proporción baja y sube la de los "
      "hidratos. Eso está bien establecido y es lo que la pantalla dibuja."),
    h("Lo que la pantalla no dibuja"),
    p("Que lo que importa no es la proporción sino la cantidad total. Media hora "
      "a intensidad baja quema un porcentaje alto de una tarta pequeña; media "
      "hora a intensidad alta quema un porcentaje menor de una tarta bastante "
      "más grande, y el trozo suele ser mayor. A eso se suma que el gasto "
      "elevado se prolonga después del esfuerzo intenso y que la contabilidad "
      "del día no distingue de dónde salió cada kilocaloría."),
    p("La conclusión no es que haya que entrenar siempre fuerte. Es que la "
      "elección de intensidad se hace por otros motivos —tiempo disponible, "
      "recuperación, gusto, articulaciones— y no por el sustrato. Cualquiera de "
      "las dos franjas de la pantalla sirve; la que se sostenga en el tiempo "
      "sirve más."),
    sep(),
    h("La fórmula que todo el mundo usa y que casi nadie sabe que es mala"),
    p("Doscientos veinte menos la edad es la estimación de frecuencia cardíaca "
      "máxima que llevan casi todas las máquinas y casi todos los relojes. Es una "
      "regla de andar por casa cuyo error típico ronda los diez o doce latidos "
      "por minuto en cualquier dirección, y esa desviación es más ancha que las "
      "franjas que la propia máquina dibuja encima."),
    p("En la práctica significa que una persona de cuarenta años cuya máxima real "
      "sea 195 estará entrenando en la zona equivocada durante toda la sesión si "
      "sigue el número de la pantalla, que le habrá calculado 180. Por eso las "
      "guías oficiales no reparten la actividad por franjas de pulso: la "
      "clasifican por intensidad relativa, que es lo que mide la prueba del habla "
      "del capítulo anterior."),
    ficha("Tres formas de medir la intensidad, de peor a mejor para el público "
          "general", [
        ("Franjas de pulso calculadas", "Cómodo y sistemáticamente inexacto para "
                                        "cualquiera cuya máxima real no coincida "
                                        "con la fórmula, que son casi todos."),
        ("Esfuerzo percibido", "Puntuar de uno a diez lo duro que se hace. "
                               "Subjetivo y, precisamente por eso, relativo a "
                               "quien entrena. Se correlaciona bastante bien con "
                               "la intensidad real."),
        ("Prueba del habla", "Hablar sí, cantar no, es moderada; frases cortas "
                             "solamente, es vigorosa. Gratis, inmediata, y "
                             "coincide con los umbrales oficiales."),
    ]),
    nota("Para qué sirve entonces el pulsómetro",
         "Para dos cosas buenas. La primera, comparar sesiones contigo mismo a lo "
         "largo de los meses: si el mismo recorrido al mismo ritmo te sale a "
         "menos pulsaciones, has mejorado, y eso es un dato limpio "
         "independientemente de que tu máxima sea la que sea. La segunda, "
         "detectar irregularidades que merecen consulta. Para lo que no sirve es "
         "para decirte en qué franja debes estar hoy."),
)

C4B = cap(
    "La fuerza no es opcional",
    p("En la lista de recomendaciones oficiales hay una línea que se cita mucho "
      "menos que la de los minutos y que está exactamente al mismo nivel "
      "jerárquico: trabajo de fuerza de todos los grandes grupos musculares, al "
      "menos dos días por semana."),
    p("No es un añadido para quien quiera, ni una recomendación de segunda. "
      "Figura en el mismo bloque que la actividad aeróbica y no se sustituye por "
      "ella: correr más no cubre el requisito de fuerza, y levantar peso no "
      "cubre el aeróbico. Son dos adaptaciones distintas de dos sistemas "
      "distintos."),
    h("Qué cuenta como trabajo de fuerza"),
    ficha("Los grandes grupos, y una opción para cada uno", [
        ("Piernas", "Sentadilla, prensa, zancada, subir escaleras con carga, "
                    "puente de glúteo"),
        ("Cadera y zona lumbar", "Peso muerto en cualquier variante, bisagra de "
                                 "cadera, extensión de cadera"),
        ("Pecho", "Press de banca, flexiones, fondos, press con mancuerna"),
        ("Espalda", "Remo, dominadas, jalón, remo con banda"),
        ("Hombros", "Press por encima de la cabeza, elevaciones"),
        ("Brazos", "Curl, extensión de tríceps. Reciben mucho trabajo indirecto: "
                   "son los que menos atención específica necesitan"),
        ("Abdomen y tronco", "Plancha, antirrotaciones, cargadas y transportes"),
    ]),
    p("El material es indiferente. Las guías no distinguen entre barra, "
      "mancuerna, máquina, banda elástica o peso corporal: lo que cuenta es que "
      "el músculo trabaje contra una resistencia que suponga un esfuerzo real. "
      "Quien no pisa un gimnasio puede cumplir la recomendación entera en el "
      "suelo de su casa, y esa es una información que la industria del fitness "
      "no tiene ningún incentivo en difundir."),
    sep(),
    h("La única variable que hay que respetar: la progresión"),
    p("Un músculo se adapta a lo que se le exige, y deja de adaptarse cuando la "
      "exigencia deja de subir. La progresión no tiene que ser rápida ni "
      "constante, pero tiene que existir, y hay más de una manera de conseguirla:"),
    lista(
        "Más peso con las mismas repeticiones.",
        "Más repeticiones con el mismo peso.",
        "Más series del mismo ejercicio.",
        "Mismo trabajo con menos descanso entre series.",
        "Mismo trabajo con mejor técnica y más recorrido, que es la progresión "
        "que más se subestima y la que más rinde en los primeros meses.",
    ),
    p("Y una regla de sensatez que no está en ningún documento oficial pero que "
      "evita la mayoría de las lesiones de quien empieza: sube una variable cada "
      "vez, y sube poco. La prisa en las primeras semanas es la causa más común "
      "de parar en las siguientes, y parar cuesta mucho más que ir despacio."),
    nota("Lo que dice la doctrina militar sobre esto",
         "El manual de salud y preparación física del Ejército de Estados Unidos "
         "—publicado íntegro y descargable— organiza el entrenamiento en fases y "
         "dedica una cantidad notable de páginas a la progresión gradual y a la "
         "prevención de lesiones por sobreuso. Una institución que entrena a "
         "cientos de miles de personas a la vez no puede permitirse lesionarlas, "
         "y por eso su doctrina es bastante más conservadora que el discurso "
         "habitual del gimnasio. Merece leerse por eso."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LO QUE PASA CUANDO NO HAY CARGA
# ══════════════════════════════════════════════════════════════════════

C5 = cap(
    "El experimento de quitar el peso",
    p("Para saber para qué sirve la carga, lo más limpio es quitarla del todo y "
      "mirar qué pasa. Eso es exactamente lo que llevan décadas haciendo los "
      "programas de investigación en vuelo espacial y en reposo en cama "
      "prolongado, y sus resultados son de acceso público."),
    fig("ca-descarga",
        "Lo que le ocurre a un cuerpo sin carga",
        "Las zonas señaladas son las que más pierden: lo que sostiene el cuerpo "
        "contra la gravedad. La columna da el ritmo de cada pérdida.",
        "media"),
    p("Son órdenes de magnitud de la literatura de reposo en cama y de vuelo "
      "espacial. Los estudios difieren en la cifra según la duración, la "
      "población y el método de medida; en lo que no difieren es en el signo, y "
      "esa coincidencia es lo que hace fiable el conjunto."),
    ficha("Los cinco efectos", [(que, f"{ritmo} · {nt}")
                                for que, ritmo, nt in D.DESCARGA]),
    h("El orden importa más que las cifras"),
    p("Lo primero que se va no es el músculo: es la fuerza. Y se va antes porque "
      "una parte de la fuerza es nerviosa —la capacidad de reclutar y coordinar "
      "las fibras— y el sistema nervioso desaprende antes de que el tejido "
      "encoja. Esa misma asimetría explica por qué las primeras semanas de "
      "entrenamiento de un principiante producen ganancias de fuerza "
      "espectaculares sin que casi cambie su aspecto: está aprendiendo, no "
      "creciendo todavía."),
    p("Lo último que se va, y lo último que vuelve, es el hueso. La densidad "
      "mineral responde a la carga mecánica con una lentitud que no tiene "
      "comparación con el resto: se pierde a lo largo de meses y se recupera a lo "
      "largo de más meses, y en algunos casos no del todo. Es la razón por la que "
      "el entrenamiento de fuerza es una inversión a plazo largo con un "
      "componente que no se puede improvisar a los sesenta años."),
    sep(),
    h("Y de aquí sale un principio general"),
    p("El tejido que soporta la carga es exactamente el que la carga mantiene. "
      "Los brazos apenas pierden densidad ósea en reposo en cama porque tampoco "
      "la tenían por soportar peso; la cadera, la columna lumbar y el talón "
      "pierden mucho porque su estructura es el resultado de años de estar de "
      "pie."),
    p("Lo que esto significa para alguien que no va a ir al espacio es directo: "
      "estar sentado once horas al día es una versión lenta y parcial del mismo "
      "experimento. No con la misma intensidad, no con el mismo ritmo, pero en la "
      "misma dirección. La descarga no es un fenómeno exótico de astronautas: es "
      "el nombre técnico de lo que le pasa a una vida sedentaria."),
    nota("La consecuencia práctica que sí está en las guías",
         "Interrumpir el tiempo sentado tiene beneficio propio, además de la "
         "actividad estructurada. Levantarse cada media hora, aunque sea dos "
         "minutos, y sustituir parte del tiempo sentado por tiempo de pie o "
         "andando es una recomendación explícita de la segunda edición. No "
         "sustituye a los ciento cincuenta minutos; se suma a ellos."),
)

C6 = cap(
    "Perder y recuperar",
    p("La otra cara de la descarga es lo que ocurre al parar de entrenar unas "
      "semanas, que es una situación mucho más frecuente que un vuelo espacial: "
      "una gripe, una mudanza, un examen, un viaje largo, una lesión de otra "
      "cosa."),
    h("La escala real del desentrenamiento"),
    ficha("Qué se pierde y en cuánto tiempo", [
        ("Primeros días", "Baja el volumen plasmático y con él parte de la "
                          "capacidad aeróbica aparente. Es el cambio más rápido y "
                          "también el que más rápido vuelve."),
        ("Una o dos semanas", "Descenso medible de la capacidad aeróbica. La "
                              "fuerza, en cambio, se conserva bastante bien en "
                              "este plazo."),
        ("Tres a cuatro semanas", "Empieza a notarse la pérdida de fuerza. El "
                                  "tamaño muscular aguanta más de lo que la gente "
                                  "teme."),
        ("Meses", "Ahí sí hay pérdida de masa apreciable, y empieza a moverse la "
                  "densidad ósea, que es lo más lento de todo."),
    ]),
    p("La conclusión práctica es tranquilizadora y conviene decirla, porque el "
      "miedo a perderlo todo es la causa de que mucha gente entrene lesionada: "
      "dos semanas parado no destruyen nada. Un mes tampoco. Lo que destruye el "
      "progreso es entrenar sobre una lesión hasta convertirla en crónica, y "
      "entonces sí desaparecen los meses."),
    sep(),
    h("La reanudación, que es lo que casi todo el mundo hace mal"),
    p("Al volver, la sensación es engañosa: la fuerza vuelve deprisa —parte de "
      "ella era nerviosa y se reaprende— mientras que los tendones, las fascias y "
      "el tejido conectivo se adaptan mucho más despacio que el músculo. Ese "
      "desfase es una fábrica de tendinopatías. El músculo ya puede tirar de un "
      "peso que el tendón todavía no está listo para soportar."),
    pasos(
        "Vuelve con la mitad del volumen que hacías, no con el mismo peso.",
        "Sube un escalón por semana durante tres o cuatro semanas hasta el punto "
        "de partida.",
        "Si la pausa fue por lesión o enfermedad, el escalón lo marca quien te "
        "trató, no este libro.",
        "Espera agujetas desproporcionadas en la primera semana y no las "
        "interpretes como señal de nada, salvo que duren más de tres o cuatro "
        "días o vengan con orina oscura, que es motivo de consulta inmediata.",
    ),
    nota("El fenómeno que juega a tu favor",
         "Recuperar es más rápido que construir por primera vez. Quien tuvo masa "
         "muscular la recupera antes que quien nunca la tuvo, y esto se observa de "
         "forma consistente. Es un buen argumento contra la idea de que "
         "abandonar dos meses tira por tierra dos años: no lo hace."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · LEVANTAR
# ══════════════════════════════════════════════════════════════════════

C7 = cap(
    "La ecuación del levantamiento",
    p("Existe una ecuación oficial que calcula cuánto peso es razonable levantar "
      "en una situación concreta. La publicó el instituto nacional de seguridad y "
      "salud laboral de Estados Unidos, se usa en inspección de trabajo en medio "
      "mundo, es de acceso libre, y prácticamente nadie que entrene la ha visto."),
    fig("ca-niosh",
        "El peso recomendado y los seis factores que lo reducen",
        f"Se parte de una carga constante de {D.NIOSH['carga_constante']} "
        "kilogramos en condiciones ideales y se multiplica por seis factores que "
        "valen entre cero y uno. Ningún factor puede mejorar el resultado: solo "
        "reducirlo. El que más penaliza, con diferencia, es la distancia "
        "horizontal de la carga al cuerpo."),
    p(D.NIOSH["nota"]),
    ficha("Los seis factores", [(f"{sig} · {nombre}", glosa)
                                for sig, nombre, glosa in D.NIOSH["factores"]]),
    h("La consecuencia que cambia cómo se levanta"),
    p("Como los factores se multiplican, dos condiciones mediocres a la vez no "
      "suman: se componen. Un factor de 0,7 y otro de 0,7 dan 0,49, es decir, "
      "menos de la mitad del peso recomendado. Por eso levantar algo lejos del "
      "cuerpo y girando el tronco a la vez es tan desproporcionadamente peor que "
      "hacer cualquiera de las dos cosas por separado, y por eso las lesiones de "
      "espalda ocurren casi siempre en gestos combinados y no en levantamientos "
      "grandes y limpios."),
    p("La distancia horizontal es la palanca principal. Un peso pegado al cuerpo "
      "y uno con los brazos estirados son, mecánicamente, cargas distintas sobre "
      "la columna aunque la báscula diga lo mismo. Esa es toda la explicación "
      "técnica del consejo popular de «pegarse la caja al pecho», y saberla la "
      "convierte en algo que se recuerda."),
    sep(),
    h("Lo que la ecuación NO dice, y que hay que decir"),
    p("No dice que doblar la espalda sea la causa de las lesiones. La ecuación no "
      "contiene ningún factor de curvatura lumbar; contiene distancia, altura, "
      "recorrido, giro, frecuencia y agarre. El mantra de «espalda recta» es una "
      "simplificación útil para principiantes, pero la evidencia sobre la postura "
      "concreta como causa de lesión es mucho menos concluyente de lo que se "
      "repite."),
    p("Lo que sí está establecido es lo otro: cuanto más lejos, más alto, más "
      "girado, más repetido y con peor agarre, peor. Esas cinco cosas se pueden "
      "cambiar en cualquier situación real, y cambiarlas rinde bastante más que "
      "obsesionarse con la forma de la columna."),
    nota("Cómo se usa esto en el gimnasio",
         "El peso muerto y el remo llevan la carga tan cerca del cuerpo como "
         "permite la anatomía, y eso no es casualidad estética: es el factor "
         "horizontal llevado a su óptimo. Cuando en un peso muerto la barra se "
         "separa de las piernas, el ejercicio se vuelve, literalmente, más "
         "pesado. La ecuación explica por qué la técnica cambia lo que la barra "
         "cuesta sin cambiar lo que la barra pesa."),
)

C8 = cap(
    "Cómo se organiza una semana",
    p("Con la dosis, la escala de intensidad y la regla de la fuerza, ya hay "
      "todo lo necesario para construir una semana. Este capítulo da tres, según "
      "el tiempo disponible, y ninguna es la de nadie: son plantillas para "
      "modificar."),
    h("Semana de tres horas · el mínimo que cumple"),
    ficha("", [
        ("Lunes", "Fuerza, cuerpo entero, 45 min. Piernas, empuje, tirón, tronco"),
        ("Martes", "Caminar a paso vivo, 30 min. Prueba del habla: hablar sí, "
                   "cantar no"),
        ("Miércoles", "Descanso o paseo tranquilo"),
        ("Jueves", "Fuerza, cuerpo entero, 45 min. Los mismos patrones, otras "
                   "variantes"),
        ("Viernes", "Caminar a paso vivo, 30 min"),
        ("Sábado", "Algo que te guste, 45 min. Bici, monte, pádel, baile"),
        ("Domingo", "Descanso"),
    ]),
    p(f"Suma: unos {30+30+45} minutos de aerobio moderado más dos sesiones de "
      "fuerza. Se queda algo corto del rango moderado y lo compensa la sesión del "
      "sábado. Es el esqueleto mínimo que cumple las dos recomendaciones a la "
      "vez, y cabe en tres horas."),
    h("Semana de cinco horas · el rango cómodo"),
    ficha("", [
        ("Lunes", "Fuerza, tren inferior y tronco, 50 min"),
        ("Martes", "Aerobio moderado continuo, 40 min"),
        ("Miércoles", "Fuerza, tren superior, 45 min"),
        ("Jueves", "Aerobio, 30 min, con algún tramo vigoroso"),
        ("Viernes", "Fuerza, cuerpo entero, 45 min"),
        ("Sábado", "Actividad larga y agradable, 60 a 90 min"),
        ("Domingo", "Descanso o movilidad"),
    ]),
    p("Aquí se entra de lleno en el tramo de beneficio adicional de la curva, con "
      "tres sesiones de fuerza en vez de dos. Es probablemente el mejor "
      "equilibrio entre resultado y vida para la mayoría de los adultos."),
    h("Semana de hora y media · cuando no hay más"),
    ficha("", [
        ("Dos días", "Fuerza de cuerpo entero, 30 min, sin descansos largos"),
        ("Tres días", "Diez minutos de escaleras, cuesta o caminata rápida"),
        ("Todos los días", "Levantarse cada media hora del asiento. No cuenta "
                           "para la dosis y cuenta para otra cosa"),
    ]),
    p("Esta semana no llega a la recomendación, y va incluida a propósito. La "
      "curva del capítulo dos dice que el salto de cero a esto es el más rentable "
      "de toda la gráfica; el salto de esto a la recomendación completa rinde "
      "menos. Un libro honesto tiene que decir que la versión pequeña vale mucho, "
      "porque la alternativa real no suele ser la versión grande: es nada."),
    nota("Sobre el calentamiento y el estiramiento",
         "Calentar sirve, y sirve sobre todo para rendir mejor en las primeras "
         "series: cinco o diez minutos de movimiento general y unas series "
         "ligeras del ejercicio que vas a hacer. Estirar antes, en cambio, no "
         "previene lesiones —la evidencia sobre eso es bastante mala— y el "
         "estiramiento estático prolongado justo antes reduce un poco la fuerza "
         "disponible. Si te gusta estirar, hazlo después o en otro momento del "
         "día."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE IV · EL OFICIO
# ══════════════════════════════════════════════════════════════════════

C9 = cap(
    "Cómo comprobarlo tú mismo",
    p("Las cuatro fuentes de este libro son gratuitas y están en línea. Este "
      "capítulo dice cuáles son y qué se busca en cada una, porque un libro que "
      "no se puede verificar tampoco se puede corregir."),
    ficha("Las fuentes de este libro", [(n, d) for n, d in D.FUENTES]),
    sep(),
    h("Las cuatro que sostienen específicamente este libro"),
    ficha("Rutas concretas", [
        ("La dosis de actividad", "Physical Activity Guidelines for Americans, "
                                  "segunda edición, en health.gov. Busca el "
                                  "capítulo de adultos y el resumen del informe "
                                  "científico del comité asesor, que es donde "
                                  "está la discusión de la curva de respuesta."),
        ("La doctrina de entrenamiento", "FM 7-22, Holistic Health and Fitness, "
                                         "en la biblioteca de publicaciones del "
                                         "Ejército de Estados Unidos. Publicado "
                                         "entero. Sus cinco dominios de "
                                         "preparación —física, nutricional, "
                                         "mental, del sueño y espiritual— "
                                         "explican por qué un plan de "
                                         "entrenamiento impecable no rinde "
                                         "cuando falla cualquiera de los otros "
                                         "cuatro."),
        ("La ecuación de levantamiento", "NIOSH, en cdc.gov/niosh. Busca la "
                                         "ecuación revisada de levantamiento y su "
                                         "manual de aplicación, que trae ejemplos "
                                         "resueltos."),
        ("La descarga", "Programa de Investigación Humana de la NASA. Busca los "
                        "estudios de reposo en cama y los riesgos documentados de "
                        "pérdida muscular y ósea; están descritos en abierto."),
    ]),
    h("Y cómo se comprueba este libro a sí mismo"),
    p("Las cifras de estas páginas viven en un módulo de datos que el programa de "
      "composición verifica antes de escribir. Para este libro, las "
      "comprobaciones relevantes son dos:"),
    lista(
        f"Que la equivalencia entre intensidades cuadre en los dos extremos: "
        f"{A['vigorosa_min']} × {A['equivalencia']} = {A['moderada_min']} y "
        f"{A['vigorosa_max']} × {A['equivalencia']} = {A['moderada_max']}. Si "
        "alguna de las dos fallara, el libro no se compondría.",
        "Que cada actividad de la escala metabólica caiga dentro de la banda de "
        "intensidad que declara, contra los umbrales oficiales. Esta comprobación "
        "cazó un error real durante la escritura: yo había clasificado una "
        "intensidad como moderada cuando su valor la ponía justo en el umbral de "
        "vigorosa. Se corrigió el dato, no la comprobación.",
    ),
    p("Además, los gastos energéticos que aparecen en el capítulo de la escala "
      "metabólica no están escritos a mano: se calculan a partir de la misma "
      "tabla que dibuja la lámina. No hay manera de que el texto y el dibujo "
      "digan cosas distintas."),
)

C10 = cap(
    "Cuaderno de la carga",
    p("Cuatro semanas. No es un plan de entrenamiento: es una medición. Sirve "
      "para saber dónde estás en la curva del capítulo dos, que es un dato que "
      "casi nadie tiene y que decide qué conviene hacer a continuación."),
    h("Semana 1 · Contar lo que ya haces"),
    pasos(
        "Anota cada día los minutos de actividad que superan la prueba del "
        "habla. Solo los que la superan.",
        "Anota aparte los minutos de fuerza, sean del tipo que sean.",
        "Anota una estimación gruesa de horas sentado. No hace falta precisión: "
        "basta con saber si son seis o son doce.",
        "No cambies nada. Esta semana es la línea de base y se estropea si "
        "intervienes.",
    ),
    h("Semana 2 · Situarte en la curva"),
    pasos(
        f"Suma los minutos moderados de la semana 1 y añade los vigorosos "
        f"multiplicados por {A['equivalencia']}.",
        f"Compara con los {A['moderada_min']} minutos de la recomendación. Ese "
        "cociente es tu posición en la gráfica.",
        "Si estás por debajo, tu objetivo de este mes es acercarte, y cada minuto "
        "que añadas vale mucho.",
        "Si ya estás por encima, tu objetivo no es sumar minutos: es que aparezcan "
        f"los {A['fuerza_dias']} días de fuerza si faltan, que es el hueco más "
        "común en quien ya hace aerobio.",
    ),
    h("Semana 3 · Una variable, un escalón"),
    pasos(
        "Elige UNA cosa que subir: minutos, días de fuerza, o peso en un "
        "ejercicio. Una.",
        "Súbela un escalón pequeño y sostenlo la semana entera.",
        "Anota cómo llegas al final de la semana: sueño, ganas de la sesión "
        "siguiente, dolores que duran más de dos días.",
        "Si alguno de esos tres empeoró de forma clara, el escalón era demasiado "
        "grande. Bájalo y repite. Esto no es un fracaso: es la información que "
        "buscabas.",
    ),
    h("Semana 4 · La auditoría de la técnica de carga"),
    pasos(
        "Durante una semana, en cada objeto pesado que levantes —dentro y fuera "
        "del gimnasio— comprueba los dos factores que más pesan: ¿está la carga "
        "cerca del cuerpo? ¿estás girando el tronco?",
        "Anota las veces que la respuesta fue mala. Casi siempre son las mismas "
        "situaciones: sacar algo del maletero, coger a un niño del suelo, mover "
        "una caja de una estantería alta.",
        "Arregla la peor de esas situaciones cambiando la logística, no la "
        "postura: acerca la caja antes de levantarla, gira los pies en vez del "
        "tronco, baja la estantería.",
        "Compara la primera semana con esta. Si los minutos subieron y las "
        "situaciones malas bajaron, el mes valió por más que cualquier "
        "entrenamiento suelto.",
    ),
    nota("Qué esperar del cuaderno",
         "Un mes no cambia un cuerpo, y prometerlo sería mentir. Lo que sí "
         "cambia es que al final tendrás tres datos que ahora no tienes: cuánto "
         "haces de verdad, dónde caes en la curva, y cuáles son las dos o tres "
         "situaciones cotidianas en las que cargas mal. Con eso, la decisión "
         "siguiente se toma sola."),
)

C11 = cap(
    "Lo que no se le pide a una guía",
    p("Cierre, y los límites. Las guías de actividad física son un documento de "
      "salud pública, y hay preguntas que no responden ni pretenden responder."),
    h("Cinco cosas que este libro no puede darte"),
    lista(
        "Un programa para tu caso. Las guías dan un marco poblacional. Una "
        "lesión previa, una patología, una competición o un objetivo estético "
        "concreto exigen a alguien que te vea.",
        "Una promesa de composición corporal. El ejercicio cambia la salud de "
        "forma muy robusta y el peso de forma bastante modesta; la mayor parte "
        "del cambio de peso se decide en la cocina y no en el gimnasio.",
        "Una respuesta sobre suplementos deportivos. Están fuera de las fuentes "
        "de este libro. Lo que se puede afirmar legalmente sobre ellos en Europa "
        "consta en un registro público de declaraciones de propiedades "
        "saludables, y es bastante menos de lo que sugiere la publicidad: "
        "conviene consultarlo antes de comprar nada.",
        "Un veredicto sobre qué método es mejor. Series largas o cortas, "
        "frecuencia alta o baja, máquinas o peso libre: dentro de un rango "
        "razonable, todo funciona si se hace con progresión y constancia. La "
        "variable dominante no es el método: es cuánto lo cumples.",
        "Permiso para ignorar el dolor. Molestia muscular difusa que dura uno o "
        "dos días es normal. Dolor articular localizado, dolor que aparece "
        "siempre en el mismo gesto, o dolor que empeora sesión a sesión, no lo es.",
    ),
    sep(),
    h("Glosario"),
    ficha("", [
        ("Aerobio", "Actividad sostenida que eleva la frecuencia cardíaca y la "
                    "respiración durante un tiempo prolongado."),
        ("Descarga", "Ausencia de carga mecánica sobre el esqueleto. El término "
                     "viene de la investigación en vuelo espacial y reposo en "
                     "cama."),
        ("Desentrenamiento", "Pérdida progresiva de las adaptaciones al dejar de "
                             "entrenar."),
        ("MET", "Equivalente metabólico. Múltiplo del gasto energético en "
                "reposo. Un MET equivale aproximadamente a una kilocaloría por "
                "kilo y hora."),
        ("Progresión", "Aumento gradual de alguna variable del entrenamiento. "
                       "Sin ella, la adaptación se detiene."),
        ("Prueba del habla", "Método para estimar la intensidad relativa: hablar "
                             "sí y cantar no equivale a moderada."),
        ("Sobreuso", "Lesión por acumulación de carga repetida sin recuperación "
                     "suficiente, no por un accidente puntual."),
        ("Volumen", "Cantidad total de trabajo: series por repeticiones por peso, "
                    "o minutos totales en el caso aeróbico."),
    ]),
    sep(),
    p("Y con esto se cierra el libro. Tiene una dosis con su curva, una escala "
      "para medir la intensidad, ocho patrones con los que auditar cualquier "
      "semana, seis variables para progresar cuando el peso no sube, una "
      "ecuación para levantar, una batería para medirse y una descripción de lo "
      "que le pasa a un cuerpo cuando no hay nada de todo eso."),
    p("Lo que no tiene es un programa cerrado, y es a propósito: el programa "
      "depende de tu horario, de tu material y de tu historial. El problema de "
      "casi todo el mundo no es elegir el programa correcto, sino cumplir "
      "cualquiera de los razonables durante el tiempo suficiente. Con lo que hay "
      "en estas páginas puedes construir el tuyo, auditarlo cada semana y "
      "corregirlo con datos en vez de con impresiones. Eso vale más que "
      "cualquier plantilla."),
)



# ══════════════════════════════════════════════════════════════════════
#  CAPÍTULOS AÑADIDOS EN LA SEGUNDA EDICIÓN
# ══════════════════════════════════════════════════════════════════════

CE1 = cap(
    "Los ocho patrones",
    p("Un programa de fuerza no se organiza por músculos: se organiza por "
      "patrones de movimiento. Son ocho, cubren todo lo que un cuerpo humano "
      "hace contra una resistencia, y una semana que los toca todos no deja "
      "huecos por definición. Es la manera más rápida de auditar cualquier plan, "
      "incluido uno que te vendan."),
    fig("ca-patrones",
        "Los ocho patrones y una opción para cada uno",
        "Organizados por lo que hace la articulación y no por el músculo que se "
        "quiere «trabajar». Cualquier ejercicio conocido cae en uno de los ocho, "
        "y si tu semana deja alguno vacío, ahí está tu hueco."),
    ficha("Los ocho, con ejemplos",
          [(nombre, f"{que} · {ejemplos}")
           for nombre, que, ejemplos in D.PATRONES]),
    h("Por qué esta forma de organizar y no la de las revistas"),
    p("El reparto clásico por grupos musculares —lunes pecho, martes espalda— "
      "viene del culturismo de competición y sirve razonablemente para su "
      "propósito, que es hipertrofiar zonas concretas con mucho volumen y mucha "
      "frecuencia semanal de gimnasio. Para casi todo el mundo, ese no es el "
      "propósito."),
    p("Organizar por patrones tiene tres ventajas prácticas. La primera: se "
      "detectan los huecos de un vistazo, y el hueco típico de un gimnasio "
      "entero es la bisagra de cadera y el transporte. La segunda: cada patrón "
      "admite decenas de variantes, así que una lesión o una máquina ocupada no "
      "rompen la sesión. Y la tercera: son los movimientos que la vida pide "
      "fuera del gimnasio, que es literalmente para lo que sirve todo esto."),
    sep(),
    h("El hueco más común, y el más caro"),
    p("La bisagra de cadera. Es el patrón de recoger algo del suelo, y es el que "
      "más gente evita porque el peso muerto tiene mala fama inmerecida. La "
      "consecuencia es previsible: musculatura posterior débil en una población "
      "que pasa el día sentada, en el mismo movimiento en el que se producen la "
      "mayoría de los sustos de espalda. La ecuación del NIOSH del capítulo "
      "siguiente explica por qué entrenarlo importa tanto."),
    p("El segundo hueco es el transporte: sostener peso y andar. No aparece en "
      "casi ningún programa, no requiere técnica y entrena agarre, tronco y "
      "postura a la vez. La compra pesada del supermercado es el ejercicio "
      "funcional que nadie tuvo que inventar."),
    nota("Cómo se audita una semana en dos minutos",
         "Escribe los ocho patrones en una columna y pon al lado los ejercicios "
         "que hiciste la semana pasada. Los que queden vacíos son tu programa "
         "real, y casi nunca coinciden con el que crees que estás haciendo."),
)

CE2 = cap(
    "Las seis variables",
    p("Un entrenamiento solo tiene seis cosas que se puedan mover. Conocerlas "
      "sirve para dos cosas: para progresar cuando el peso no sube, y para no "
      "cometer el error más habitual de todos, que es subir dos a la vez."),
    fig("ca-variables",
        "Las seis variables del entrenamiento",
        "Cada una modifica el estímulo por su cuenta. Se sube una y se sostiene "
        "unas semanas; subir dos a la vez multiplica la carga real sin que uno "
        "se dé cuenta, y es la fábrica de lesiones del mes dos."),
    ficha("Las seis", [(nombre, glosa) for nombre, glosa in D.VARIABLES]),
    h("La que más rinde en los primeros meses"),
    p("El recorrido. Media sentadilla con el doble de peso no es más "
      "entrenamiento que una sentadilla completa con la mitad: es otro "
      "ejercicio, y bastante peor. La amplitud completa produce más adaptación "
      "en la parte del músculo que trabaja estirada, mantiene la movilidad de la "
      "articulación y, de paso, obliga a usar un peso honesto."),
    p("Es también la variable que más se sacrifica por vanidad, porque bajar el "
      "peso para completar el recorrido se siente como retroceder. No lo es. Es "
      "la única forma de que el número que apuntas signifique algo."),
    h("La que casi nadie cuenta bien: el volumen"),
    p("La cuenta que predice la ganancia de tamaño son las series efectivas por "
      "músculo y por semana, no el tiempo en el gimnasio ni el número de "
      "ejercicios. Una serie efectiva es la que se lleva cerca del fallo "
      "técnico: con cuatro o cinco repeticiones de margen sobrando, el estímulo "
      "es escaso por muchas series que se hagan."),
    p("De ahí que una sesión de cuarenta y cinco minutos bien apretada rinda más "
      "que dos horas de deambular entre máquinas, y de ahí también que "
      "aumentar el volumen sin límite deje de funcionar: llega un punto en que "
      "lo que se añade no se recupera, y lo que no se recupera no adapta."),
    sep(),
    h("La escala de esfuerzo, que resuelve el problema de los porcentajes"),
    p("Programar por porcentaje del máximo exige conocer el máximo, y el máximo "
      "cambia con el sueño, el estrés y la semana. La alternativa práctica es "
      "puntuar cuántas repeticiones te quedaban en reserva al terminar la serie:"),
    ficha("Repeticiones en reserva", [
        ("0", "No podías hacer ni una más. Se usa poco y con criterio"),
        ("1 a 2", "La zona de trabajo de las series de fuerza y de tamaño"),
        ("3 a 4", "Estímulo válido y mucho menos coste de recuperación"),
        ("5 o más", "Calentamiento, técnica o volumen de relleno"),
    ]),
    p("Con esta escala, un mal día se ajusta solo: el peso que hoy te deja a dos "
      "repeticiones puede ser menor que el de la semana pasada, y aun así la "
      "sesión ha sido correcta. Programar por porcentaje fijo obliga a fallar o "
      "a mentir."),
    nota("La regla de progresión que evita casi todo",
         "Una variable, un escalón, y sostenerlo dos o tres semanas antes de "
         "tocar otra. Si el rendimiento baja tres sesiones seguidas, o si "
         "aparece dolor articular, el escalón anterior era el bueno: se vuelve "
         "y se sostiene más tiempo. Bajar no es retroceder; es lo que hace "
         "posible seguir subiendo el año que viene."),
)

CE3 = cap(
    "Calentar, enfriar y lo que no sirve",
    p("El calentamiento es la parte del entrenamiento con más mitología por "
      "minuto invertido. Lo que sigue separa lo que tiene respaldo razonable de "
      "lo que se repite por costumbre."),
    h("Un calentamiento que sí hace algo, en tres actos"),
    pasos(
        "Cinco o diez minutos de movimiento general que suba la temperatura y "
        "la frecuencia cardíaca. Andar rápido, bici suave, cuerda ligera. "
        "Cualquier cosa que no sea estirar.",
        "Movilidad activa de las articulaciones que vas a usar. Círculos, "
        "balanceos, sentadillas sin peso, rotaciones. Movimiento, no posturas "
        "sostenidas.",
        "Series de aproximación del primer ejercicio: la barra vacía, después "
        "la mitad del peso, después algo por debajo del peso de trabajo. Es la "
        "parte del calentamiento que más rinde y la que más gente se salta.",
    ),
    p("El objetivo no es prevenir lesiones —la evidencia sobre eso es más floja "
      "de lo que se dice— sino rendir mejor en las primeras series, que es un "
      "efecto inmediato y comprobable: la primera serie después de calentar bien "
      "se siente distinta, y eso ya justifica los diez minutos."),
    sep(),
    h("El estiramiento estático, en su sitio"),
    lista(
        "Antes de entrenar, sostener un estiramiento largo reduce ligeramente la "
        "fuerza disponible durante los minutos siguientes. Si lo haces, que sea "
        "breve y no justo antes de la serie pesada.",
        "No previene lesiones de forma demostrada, y llevamos décadas "
        "intentando demostrarlo.",
        "No previene ni cura las agujetas. Esto está bastante bien establecido y "
        "sigue apareciendo en todas partes.",
        "Sí mejora el rango de movimiento si se hace de forma regular, y eso "
        "tiene valor propio. Hazlo porque quieres más movilidad, no porque creas "
        "que te protege.",
    ),
    h("Las agujetas, que no son lo que la gente cree"),
    p("Aparecen sobre todo tras trabajo excéntrico —la fase de bajada— y tras "
      "ejercicios nuevos, alcanzan su punto máximo entre veinticuatro y "
      "cuarenta y ocho horas después y se van solas. No son un indicador de que "
      "la sesión haya sido buena: un programa bien llevado produce cada vez "
      "menos agujetas mientras el rendimiento sigue subiendo, y perseguirlas es "
      "perseguir la señal equivocada."),
    p("Lo que mejor las alivia es moverse suave. Lo que no las quita es "
      "estirar. Y si duran más de cuatro o cinco días, o si vienen con hinchazón "
      "marcada y orina oscura después de una sesión inusualmente dura, eso ya no "
      "son agujetas y es motivo de consulta el mismo día."),
    nota("Enfriar",
         "Bajar el ritmo cinco minutos al final no acelera la recuperación de "
         "forma apreciable, pero evita el mareo de parar en seco tras un "
         "esfuerzo intenso y es un buen momento para el trabajo de movilidad, "
         "porque el tejido está caliente. Es un hábito barato con dos ventajas "
         "pequeñas; no le pidas más."),
)

CE4 = cap(
    "El aerobio por dentro",
    p("«Hacer cardio» describe tan poco como «comer comida». Bajo esa etiqueta "
      "caben tres cosas distintas que producen adaptaciones distintas y cuestan "
      "recuperaciones distintas, y saber cuál es cuál cambia el resultado de una "
      "temporada."),
    ficha("Los tres tipos", [
        ("Base", "Conversación posible durante toda la sesión. Volumen "
                 "cómodo, de treinta minutos a dos horas. Construye la "
                 "capacidad de fondo y apenas cuesta recuperación."),
        ("Umbral", "Ritmo sostenido en el que las frases se acortan. Bloques "
                   "de diez a veinte minutos. Mejora el ritmo que puedes "
                   "sostener mucho tiempo."),
        ("Intervalos", "Esfuerzos cortos muy intensos con descanso. Mejoran el "
                       "techo, cuestan bastante recuperación y son los que más "
                       "se abusan."),
    ]),
    h("El error de vivir en el medio"),
    p("La trampa más común del aerobio amateur es hacerlo todo a una intensidad "
      "intermedia: demasiado fuerte para acumular volumen sin fatiga y demasiado "
      "suave para producir la adaptación de la intensidad alta. Es cómodo, se "
      "siente productivo y rinde poco por lo que cuesta."),
    p("La corrección es sencilla y funciona: que la mayor parte del volumen sea "
      "claramente fácil —de verdad fácil, hablando cómodamente— y que la parte "
      "dura sea claramente dura y ocupe poco. Los extremos hacen el trabajo; el "
      "medio acumula fatiga."),
    sep(),
    h("¿Interfiere el aerobio con la fuerza?"),
    p("La pregunta lleva décadas en el aire y la respuesta razonable es: mucho "
      "menos de lo que teme el gimnasio, y algo más que cero. Lo que se sabe con "
      "cierta solidez es que la interferencia aparece sobre todo con volúmenes "
      "muy altos de aerobio, con las dos cosas en la misma sesión y con poca "
      "recuperación entre ellas."),
    lista(
        "Si puedes, separa las dos sesiones por varias horas o ponlas en días "
        "distintos.",
        "Si tienen que ir juntas, haz primero lo que sea prioritario para ti.",
        "Correr interfiere más que pedalear, probablemente por el componente "
        "excéntrico de la zancada.",
        "Para la inmensa mayoría de la gente, que hace tres o cuatro horas "
        "semanales en total, esta discusión es puramente teórica.",
    ),
    nota("Lo que el aerobio hace y la fuerza no",
         "Cambia el corazón y el sistema vascular de una manera que el "
         "entrenamiento de fuerza no reproduce, y esos cambios son los que mejor "
         "se asocian con vivir más años y con vivirlos mejor. Por eso las guías "
         "piden las dos cosas y no dejan elegir: no son sustitutos."),
)

CE5 = cap(
    "Dolor: cómo se distingue",
    p("Este capítulo existe porque la alternativa a tenerlo es que la gente "
      "aprenda a distinguir por el método caro. No sustituye a un diagnóstico; "
      "da criterios para saber cuándo seguir, cuándo cambiar y cuándo parar y "
      "consultar."),
    ficha("Tres cosas que se confunden", [
        ("Molestia muscular difusa", "Repartida por el vientre del músculo, "
                                     "simétrica, aparece a las horas, mejora al "
                                     "moverse y se va en dos o tres días. Es "
                                     "normal."),
        ("Dolor articular localizado", "Se puede señalar con un dedo, aparece "
                                       "siempre en el mismo gesto y en el mismo "
                                       "punto del recorrido, no mejora al "
                                       "calentar. No es normal."),
        ("Dolor que crece sesión a sesión", "Empieza al final del entrenamiento, "
                                            "luego al principio, luego en la "
                                            "vida diaria. Es el guion clásico de "
                                            "una lesión por sobreuso, y cuanto "
                                            "antes se corta, menos cuesta."),
    ]),
    h("Qué hacer con cada uno"),
    pasos(
        "Molestia muscular: seguir, moverse suave y no medir la calidad de una "
        "sesión por cuánto duele después.",
        "Dolor en un gesto concreto: cambiar el gesto, no abandonar el patrón. "
        "Si duele el press de banca, prueba con mancuernas o con otro ángulo; "
        "casi siempre hay una variante que no duele, y seguir entrenando el "
        "patrón es mejor que dejarlo.",
        "Dolor que crece: reducir la carga de ese patrón un escalón grande "
        "durante dos semanas, mantener el resto y observar. Si en dos semanas no "
        "mejora, consulta.",
        "Cualquier dolor con hinchazón, pérdida de fuerza súbita, bloqueo "
        "articular, hormigueo o pérdida de sensibilidad: consulta directamente y "
        "sin fase de prueba.",
    ),
    sep(),
    h("Y las señales que paran una sesión en el acto"),
    lista(
        "Dolor u opresión en el pecho, o dolor que irradia al brazo, al cuello o "
        "a la mandíbula.",
        "Falta de aire desproporcionada al esfuerzo que estás haciendo.",
        "Mareo, visión borrosa, palpitaciones irregulares o sensación de "
        "desmayo.",
        "Dolor de cabeza súbito e intenso durante un esfuerzo.",
        "Orina de color oscuro tras una sesión inusualmente dura, sobre todo si "
        "va con dolor muscular desproporcionado e hinchazón.",
    ),
    p("Estas cinco no son «escuchar al cuerpo»: son motivo de atención médica el "
      "mismo día. Ninguna sesión de ningún plan de ningún libro merece la duda, "
      "y esta es la página que conviene recordar de todo el volumen."),
    nota("La regla de las setenta y dos horas",
         "Si algo duele igual o peor tres días después de haber reducido la "
         "carga, ha dejado de ser un asunto de programación. Lo que sigue no es "
         "elegir otro ejercicio: es que alguien te vea."),
)

CE6 = cap(
    "Entrenar a partir de los sesenta",
    p("Las guías de actividad física tienen una sección específica para adultos "
      "mayores, y contiene la única recomendación de todo el documento que no "
      "aparece para el resto de la población. Merece un capítulo porque casi "
      "nadie la conoce y porque es la que más años de autonomía compra."),
    ficha("Lo que añaden las guías para adultos mayores", [
        ("Equilibrio", "Trabajo de equilibrio como componente propio, además "
                       "del aerobio y de la fuerza. Es la recomendación "
                       "adicional y va dirigida a lo que de verdad quita "
                       "autonomía, que son las caídas."),
        ("Fuerza", "Igual de necesaria que a cualquier edad, y más urgente: la "
                   "pérdida de masa muscular con los años es lo que convierte "
                   "una caída en una fractura y una fractura en una vida "
                   "distinta."),
        ("Aerobio", "La misma dosis, con la coletilla de que quien no pueda "
                    "alcanzarla debe ser tan activo como su condición le "
                    "permita. El listón se adapta; no se cancela."),
        ("Adaptación", "Ajustar el esfuerzo al nivel de forma, con especial "
                       "atención a las condiciones crónicas. Adaptar no es "
                       "rebajar a cero."),
    ]),
    h("El equilibrio se entrena, y es barato"),
    lista(
        "Sostenerse sobre una pierna mientras te lavas los dientes. Dos minutos "
        "al día que no ocupan tiempo nuevo.",
        "Caminar en línea, talón contra punta, unos metros por el pasillo.",
        "Levantarse de una silla sin usar los brazos, varias veces seguidas. Es "
        "a la vez fuerza y equilibrio, y es la prueba que mejor predice la "
        "autonomía a diez años.",
        "Cambios de dirección y de superficie al andar: hierba, cuesta, "
        "arena. El equilibrio se entrena obligándolo a corregir.",
        "Todo esto se hace con un apoyo cerca al principio. La progresión es "
        "quitar el apoyo, no empezar sin él.",
    ),
    sep(),
    h("La pérdida de músculo con la edad, en su tamaño real"),
    p("A partir de la mediana edad se pierde masa muscular de forma continua si "
      "no se hace nada al respecto, y la fuerza se pierde todavía más deprisa "
      "que la masa. Ese proceso no es una fatalidad biológica que haya que "
      "aceptar: responde al entrenamiento de fuerza a cualquier edad, y hay "
      "programas documentados que producen ganancias en personas de más de "
      "ochenta años."),
    p("El error más común es el contrario del que se supone: no es entrenar "
      "demasiado fuerte, es entrenar demasiado suave. Un peso que se puede "
      "levantar treinta veces sin esfuerzo no produce adaptación a ninguna edad. "
      "La progresión tiene que existir también aquí, con más cuidado en la "
      "técnica y más margen en el descanso, pero tiene que existir."),
    nota("La proteína en esta etapa",
         "El suelo poblacional de 0,8 gramos por kilo se queda corto para frenar "
         "la pérdida de masa a partir de cierta edad, y la literatura geriátrica "
         "maneja cifras claramente mayores. Esa cifra no sale de las tablas de "
         "referencia y lo digo: sale de otra literatura. Es una conversación que "
         "merece tenerse con un profesional, sobre todo si hay función renal "
         "comprometida, donde la respuesta puede ser la contraria."),
)

CE7 = cap(
    "Una batería para medirse, y es pública",
    p("El peso corporal oscila varios kilos en cuestión de días por agua, sal, "
      "glucógeno y contenido intestinal, así que medir el progreso con la "
      "báscula es reaccionar a ruido. Medirlo con pruebas físicas es mucho "
      "mejor, y existe una batería completa, descrita al detalle y de acceso "
      "libre, que el Ejército de Estados Unidos publica entera."),
    fig("ca-acft",
        "Seis pruebas, seis cualidades distintas",
        "La batería está construida para que ninguna prueba se pueda compensar "
        "con otra: hay un mínimo por prueba. Esa regla es la lección "
        "transferible, aunque nunca vayas a hacer ninguna de las seis."),
    ficha("Qué mide cada una",
          [(nombre, f"{como} · mide {mide.lower()}")
           for nombre, como, mide in D.ACFT]),
    p(D.ACFT_PUNTOS["nota"]),
    h("Por qué esto es interesante para alguien que no es militar"),
    p("Por el diseño, no por las pruebas concretas. Una batería que exige un "
      "mínimo en seis cualidades distintas está diciendo algo que el gimnasio "
      "medio ignora: que un cuerpo bien preparado no es el que destaca en una "
      "cosa, sino el que no falla en ninguna. Alguien que levanta mucho y no "
      "puede correr dos millas tiene un hueco, y ese hueco no se tapa levantando "
      "más."),
    p("El segundo motivo es que es un objetivo de proceso disfrazado de "
      "resultado. Puntuar mejor en seis pruebas es una diana clara, medible y "
      "que depende enteramente de lo que hagas, a diferencia del peso corporal, "
      "que depende de media docena de cosas que no controlas."),
    sep(),
    h("Una versión casera de la misma idea"),
    p("No hace falta un trineo ni una barra hexagonal. Lo que hace falta es "
      "elegir cinco o seis pruebas que cubran cualidades distintas, medirlas hoy "
      "y repetirlas cada tres meses en las mismas condiciones:"),
    ficha("Batería casera", [
        ("Fuerza de piernas", "Sentadillas en un minuto, o peso de tu serie de "
                              "cinco repeticiones"),
        ("Fuerza de empuje", "Flexiones máximas con técnica completa"),
        ("Fuerza de tirón", "Dominadas, o remo invertido máximo"),
        ("Tronco", "Plancha sostenida, en segundos"),
        ("Aerobio", "Distancia en doce minutos, o tiempo en un recorrido fijo "
                    "que puedas repetir"),
        ("Equilibrio", "Segundos sobre una pierna con los ojos cerrados"),
    ]),
    p("Anota los seis números y guárdalos. Dentro de tres meses tendrás algo que "
      "ninguna báscula da: seis pruebas de que el trabajo hizo algo, o seis "
      "señales de dónde no lo hizo. Y a diferencia del peso, estos números no "
      "oscilan tres kilos según lo que cenaste."),
    nota("Cómo NO se hace esta medición",
         "No se hace en un mal día para castigarse, ni el mismo día de una "
         "sesión dura, ni cambiando las condiciones entre una vez y la "
         "siguiente. Se hace descansado, con el mismo protocolo, y se apunta "
         "aunque salga peor que la vez anterior. Un resultado peor es un dato "
         "sobre el plan, no un veredicto sobre la persona."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-carga",
    "titulo": "Códice de la Carga",
    "subtitulo": "La dosis oficial de actividad, la escala que la mide, la ecuación de levantar y lo que le pasa a un cuerpo sin peso",
    "autor": "Villuminations",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-carga",
    "acento": "carga",
    "original": True,
    "laminas": ["carga.svg"],
    "claves": ["entrenamiento", "actividad física", "MET", "fuerza", "NIOSH",
               "descarga", "desentrenamiento", "villuminations"],
    "capitulos": [
        C1, C2, C3, C4, C4B,       # I · La dosis
        CE1, CE2, CE3, CE4,        # II · El oficio de entrenar
        C5, C6, CE5,               # III · Lo que pasa cuando no hay carga
        C7, C8, CE6,               # IV · Levantar y durar
        CE7, C9, C10, C11,         # V · El oficio
    ],
}


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    destino = SRC / f"{LIBRO['id']}.json"
    destino.write_text(json.dumps(LIBRO, ensure_ascii=False, indent=1))
    palabras = sum(
        len(b["x"].split()) if isinstance(b.get("x"), str) else
        sum(len(" ".join(map(str, i)).split()) if isinstance(i, (list, tuple))
            else len(str(i).split()) for i in b["x"])
        if isinstance(b.get("x"), list) else 0
        for c in LIBRO["capitulos"] for b in c["bloques"]
    )
    print(f"  {LIBRO['titulo']}: {len(LIBRO['capitulos'])} capítulos · "
          f"{palabras:,} palabras · {len(D.MET)} intensidades comprobadas · "
          f"→ {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
