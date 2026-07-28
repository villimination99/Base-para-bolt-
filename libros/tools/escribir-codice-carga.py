#!/usr/bin/env python3
"""
CÓDICE DE LA CARGA — obra original de VILLUMINATION 99
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
    p("Y como en el resto de la colección, las cifras de estas páginas no se "
      "teclearon en el texto: viven en un módulo de datos que se verifica antes "
      "de componer el libro. Si la equivalencia entre minutos moderados y "
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
      "abandona en la semana tres. El Códice de la Voluntad trata ese problema "
      "entero."),
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
        (nombre, f"{MET[nombre][0]} MET · unas {kcal(MET[nombre][0], 70, 30)} kcal "
                 f"· {MET[nombre][1]}")
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
    ficha("Las fuentes de la colección", [(n, d) for n, d in D.FUENTES]),
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
                                         "mental, del sueño y espiritual— son el "
                                         "esqueleto de esta serie de cuatro "
                                         "libros."),
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
        "del cambio de peso se decide en la mesa, que es el libro anterior.",
        "Una respuesta sobre suplementos deportivos. Están fuera de estas "
        "fuentes. Lo poco que se puede afirmar legalmente sobre ellos está en el "
        "capítulo del registro europeo del Códice de la Mesa, y es menos de lo "
        "que la publicidad sugiere.",
        "Un veredicto sobre qué método es mejor. Series largas o cortas, "
        "frecuencia alta o baja, máquinas o peso libre: dentro de un rango "
        "razonable, todo funciona si se hace con progresión y constancia. La "
        "variable dominante es otra, y tiene su propio libro.",
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
    p("Y con esto se cierra el segundo Códice de fitness. Tiene una dosis, una "
      "escala para medirla, una ecuación para levantar y una descripción de lo "
      "que pasa cuando no hay nada de todo eso. No tiene un programa, porque el "
      "programa depende de ti y porque el problema de casi todo el mundo no es "
      "elegir el programa correcto."),
    p("El problema de casi todo el mundo es cumplirlo, y de eso trata el "
      "siguiente."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-carga",
    "titulo": "Códice de la Carga",
    "subtitulo": "La dosis oficial de actividad, la escala que la mide, la ecuación de levantar y lo que le pasa a un cuerpo sin peso",
    "autor": "Villumination 99",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-carga",
    "acento": "carga",
    "original": True,
    "laminas": ["carga.svg"],
    "claves": ["entrenamiento", "actividad física", "MET", "fuerza", "NIOSH",
               "descarga", "desentrenamiento", "villuminations"],
    "capitulos": [
        C1, C2, C3, C4, C4B,  # I · La dosis
        C5, C6,               # II · Lo que pasa cuando no hay carga
        C7, C8,               # III · Levantar
        C9, C10, C11,         # IV · El oficio
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
