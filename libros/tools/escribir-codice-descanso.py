#!/usr/bin/env python3
"""
CÓDICE DEL DESCANSO — obra original de VILLUMINATION 99
=======================================================
Octavo libro de la colección y cuarto de la serie de fitness. El sueño y la
recuperación tratados como parte del entrenamiento y no como lo que sobra del
día.

Base pública y libre: el dominio de sueño del FM 7-22 del Ejército de Estados
Unidos, las recomendaciones de salud pública sobre duración del sueño, la
investigación de la NASA en descarga y reposo, y las Physical Activity
Guidelines en lo que respecta al efecto agudo del ejercicio sobre el sueño.
Todas ellas son obra del gobierno federal estadounidense y por tanto no están
sujetas a copyright (17 U.S.C. § 105).

Las cifras vienen de tools/datos_oficiales.py y se comprueban antes de escribir.

    python3 tools/escribir-codice-descanso.py && python3 build.py descanso
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

S = D.SUENO
FASE = {f[0]: f for f in S["fases"]}


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


# La cuenta que sostiene todo el libro, calculada y no tecleada.
CICLO_MIN, CICLO_MAX = S["ciclos_noche"]
HORAS_MIN = CICLO_MIN * S["ciclo_min"] / 60
HORAS_MAX = CICLO_MAX * S["ciclo_min"] / 60


def hh(x):
    return f"{x:g}".replace(".", ",")


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · LA NOCHE POR DENTRO
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "La mitad del día que nadie entrena",
    p("Un adulto que sigue las recomendaciones de actividad dedica unas cuatro "
      "horas semanales a entrenar. Ese mismo adulto pasa entre cuarenta y "
      "cincuenta horas semanales durmiendo, o intentándolo. Es, con diferencia, "
      "la actividad a la que más tiempo dedica en su vida, y la única que casi "
      "nadie considera parte de su preparación física."),
    h("La afirmación de este libro"),
    p("El sueño no es lo que sobra del día: es la fase en la que ocurre casi todo "
      "lo que el entrenamiento y la comida solo preparan. Y a diferencia de la "
      "motivación, tiene una estructura conocida, medible y bastante manipulable "
      "con decisiones sencillas."),
    ficha("La recomendación, y de dónde sale", [
        ("Adulto", f"{S['adulto_horas']} horas o más por noche, de forma "
                   "habitual"),
        ("Ciclo", f"unos {S['ciclo_min']} minutos"),
        ("Ciclos por noche", f"de {CICLO_MIN} a {CICLO_MAX}"),
        ("La cuenta", f"{CICLO_MAX} ciclos de {S['ciclo_min']} minutos son "
                      f"{hh(HORAS_MAX)} horas; {CICLO_MIN} ciclos son "
                      f"{hh(HORAS_MIN)}. La recomendación de "
                      f"{S['adulto_horas']} horas cae exactamente dentro de ese "
                      "rango, y no por casualidad."),
    ]),
    h("Lo que este libro no afirma"),
    lista(
        "No trata trastornos del sueño. Apnea, insomnio crónico, síndrome de "
        "piernas inquietas y narcolepsia son diagnósticos médicos con "
        "tratamiento, y ninguno se arregla con higiene del sueño. El capítulo "
        "final dice cómo reconocer que hay que consultar.",
        "No promete que vayas a dormir mejor esta noche. Casi todo lo de aquí "
        "actúa en semanas, y perseguir el resultado de una noche concreta es una "
        "de las cosas que peor funcionan.",
        "No da una hora óptima para acostarse. Existe variación individual real en "
        "el cronotipo, y forzar a alguien de tendencia nocturna a madrugar sin "
        "más no le convierte en madrugador.",
        "No incluye suplementos ni fármacos. Eso es terreno de quien te receta, y "
        "la melatonina en particular es un caso donde la dosis, la hora y el "
        "motivo importan más de lo que la venta libre sugiere.",
    ),
    nota("Lo que sí está establecido y conviene tener presente",
         "La privación de sueño sostenida se asocia a peor rendimiento cognitivo, "
         "peor control de la glucosa, más apetito, más riesgo de accidente y peor "
         "recuperación del entrenamiento. Es de las relaciones más consistentes de "
         "toda la salud pública, y es la razón por la que una institución tan "
         "poco sentimental como un ejército trata el sueño como munición y no "
         "como debilidad."),
)

C2 = cap(
    "La arquitectura de una noche",
    p("Dormir no es un estado: son cuatro, que se alternan en un orden que no es "
      "aleatorio y que se repite en ciclos. Ese orden es la información más útil "
      "de este libro, porque explica qué se pierde exactamente cuando se duerme "
      "poco."),
    fig("de-hipnograma",
        "El recorrido de una noche completa",
        f"De {CICLO_MIN} a {CICLO_MAX} ciclos de unos {S['ciclo_min']} minutos. "
        "El sueño profundo se concentra en la primera mitad de la noche y los "
        "tramos de sueño con movimientos oculares rápidos se alargan en cada "
        "ciclo, dominando la segunda mitad. La noche no es simétrica, y esa "
        "asimetría es la clave de todo el capítulo."),
    h("Las cuatro fases"),
    fig("de-fases",
        "Qué hace cada fase",
        "Los dos primeros estados son sueño ligero; el tercero es el profundo, "
        "asociado a la recuperación física; el cuarto es el de los movimientos "
        "oculares rápidos. Un despertar breve entre ciclos es normal y no indica "
        "que algo vaya mal."),
    ficha("En una tabla", [(f"{sig} · {nombre}", f"{cuanto} · {hace}")
                           for sig, nombre, cuanto, hace in S["fases"]]),
    sep(),
    h("La consecuencia que casi nadie ha oído"),
    p("Si la noche fuera homogénea, recortar una hora costaría lo mismo por "
      "cualquiera de los dos extremos. No lo es. Como el sueño profundo va "
      "delante y el de movimientos oculares rápidos va detrás, quitar la última "
      "hora no quita un poco de cada cosa: quita casi exclusivamente el segundo, "
      "que es el que más crece precisamente en los últimos ciclos."),
    p("Eso significa que quien duerme cinco horas conserva la mayor parte de su "
      "sueño profundo y pierde una fracción enorme del otro. Y explica algo que "
      "mucha gente ha notado sin saber por qué: después de una noche corta uno "
      "puede sentirse físicamente aceptable y estar claramente peor de humor, de "
      "concentración y de memoria."),
    p("Al revés también funciona, y es más importante para quien entrena: "
      "acostarse tarde y levantarse a la misma hora se come el sueño de la "
      "segunda mitad; acostarse a la hora y levantarse antes hace lo mismo. Las "
      "dos formas habituales de recortar atacan al mismo lado de la noche."),
    nota("Por qué el mito de despertarse entre ciclos funciona a medias",
         "Es cierto que despertarse en mitad de un tramo profundo produce esa "
         "sensación pastosa de aturdimiento, y que despertarse en sueño ligero es "
         "más agradable. Lo que no es cierto es que las aplicaciones que dicen "
         "calcular tu ciclo desde el móvil en la mesilla puedan hacerlo con "
         "precisión: los ciclos no duran exactamente noventa minutos ni son "
         "iguales entre sí ni entre personas. La forma fiable de despertarse en "
         "sueño ligero es dormir lo suficiente, porque los últimos ciclos son casi "
         "todo sueño ligero y REM."),
)

C3 = cap(
    "La deuda",
    p("La expresión «deuda de sueño» suena a metáfora y describe bastante bien lo "
      "que ocurre: el déficit se acumula, produce efectos medibles antes de que "
      "uno se dé cuenta, y no se salda de una vez."),
    fig("de-deuda",
        "Una semana normal y lo que deja detrás",
        f"Cinco noches por debajo del objetivo de {S['adulto_horas']} horas y dos "
        "de recuperación el fin de semana. La deuda de la semana no se cancela: "
        "dormir de más el sábado recupera parte del déficit —sobre todo del "
        "profundo, que tiene prioridad— pero no todo, y a cambio desplaza el "
        "horario y hace más difícil el lunes."),
    h("Los tres hechos que hacen peligrosa a la deuda"),
    ficha("", [
        ("Se acumula", "Varias noches de seis horas producen un deterioro "
                       "comparable al de noches enteras sin dormir, alcanzado "
                       "poco a poco."),
        ("No se percibe", "La percepción subjetiva de somnolencia se aplana "
                          "mientras el rendimiento sigue cayendo. Quien lleva una "
                          "semana durmiendo poco cree haberse adaptado, y lo que "
                          "ha hecho es perder la capacidad de notarlo."),
        ("Se paga con recargo", "El cuerpo prioriza recuperar el sueño profundo, "
                                "y en las noches de recuperación aparece más "
                                "cantidad de la habitual. El de la segunda mitad "
                                "se recupera peor, y es el que se había perdido."),
    ]),
    p("El segundo punto es el que más consecuencias tiene fuera del gimnasio. La "
      "sensación de estar bien no es un indicador fiable de estar bien, y la "
      "situación en la que eso importa de verdad es al volante. Conducir con "
      "sueño acumulado deteriora la atención y el tiempo de reacción de forma "
      "documentada, y a diferencia de otras causas de mala conducción, esta no se "
      "compensa con voluntad."),
    sep(),
    h("El fin de semana: qué recupera y qué estropea"),
    p("Dormir más el sábado y el domingo es mejor que no hacerlo, y conviene "
      "decirlo porque el consejo de mantener horarios rígidos suena a que dormir "
      "de más está mal. No lo está. Lo que ocurre es que tiene un coste: "
      "levantarse tres horas más tarde el domingo es, para el reloj interno, "
      "parecido a viajar a otro huso horario, y el domingo por la noche el sueño "
      "llega tarde. Es la causa más común del insomnio del domingo y del lunes "
      "espantoso."),
    lista(
        "Recuperar sí, pero acotado: hasta una hora más de lo habitual mueve poco "
        "el reloj; tres horas lo mueven bastante.",
        "Es mejor adelantar la hora de acostarse el fin de semana que retrasar la "
        "de levantarse. Consigues las mismas horas sin desplazar el ancla.",
        "La hora de levantarse es el ancla más fuerte del reloj interno, sobre "
        "todo si va acompañada de luz. Si solo puedes fijar una cosa de tu "
        "horario, fija esa.",
    ),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LO QUE SE PUEDE HACER
# ══════════════════════════════════════════════════════════════════════

C4 = cap(
    "La cuenta atrás",
    p("La higiene del sueño suele presentarse como una lista de consejos "
      "desordenada y de eficacia desigual. Ordenada en el tiempo funciona mucho "
      "mejor, porque cada elemento tiene una hora a la que deja de poder "
      "arreglarse."),
    fig("de-ventana",
        "Qué se corta y cuándo, contando hacia atrás desde la hora de acostarse",
        "Los tiempos son órdenes de magnitud razonables, no umbrales exactos. El "
        "de la cafeína sale de su vida media, que ronda las cinco horas en un "
        "adulto medio: a las diez horas queda todavía cerca de un octavo de la "
        "dosis circulando."),
    h("La cafeína, con su aritmética"),
    p("La vida media es el tiempo que tarda el cuerpo en eliminar la mitad. Con "
      "unas cinco horas de vida media, un café de las cinco de la tarde deja la "
      "mitad de su cafeína a las diez de la noche y la cuarta parte a las tres de "
      "la madrugada. No impide dormirse necesariamente, y sí reduce la cantidad "
      "de sueño profundo de esa noche, que es un efecto que no se percibe."),
    p("Hay además una variación individual grande en la velocidad de eliminación: "
      "hay quien metaboliza la cafeína al doble de velocidad que otro. Por eso el "
      "argumento «a mí no me afecta» puede ser literalmente cierto en unas "
      "personas y ser un error de percepción en otras. La forma de saberlo es "
      "quitarla dos semanas y comparar, no razonarlo."),
    h("El alcohol, que es el engaño más extendido"),
    p("El alcohol acorta el tiempo que se tarda en dormirse, y de ahí viene su "
      "fama de ayudar a dormir. Lo que hace después es lo contrario: fragmenta la "
      "segunda mitad de la noche y suprime parte del sueño con movimientos "
      "oculares rápidos, que ya vimos que es justo el que vive ahí. El resultado "
      "es una noche que empieza fácil y termina mal, con más despertares y peor "
      "sensación de descanso."),
    sep(),
    h("Luz y temperatura, que son las dos palancas grandes"),
    ficha("Las dos señales que el reloj interno lee de verdad", [
        ("Luz por la mañana", "Es la señal más potente para fijar el reloj. Diez "
                              "o quince minutos de luz exterior poco después de "
                              "levantarse hacen más que cualquier ritual "
                              "nocturno, y es el consejo más subestimado del "
                              "capítulo."),
        ("Oscuridad por la noche", "Luz tenue y cálida en la última hora. El "
                                   "problema de las pantallas no es solo la luz: "
                                   "es lo que se hace en ellas, que activa."),
        ("Temperatura", "Dormir es un proceso que necesita que la temperatura "
                        "central baje. Habitación fresca ayuda; una ducha "
                        "caliente un par de horas antes también, porque provoca "
                        "una caída posterior."),
        ("Ruido y horario", "El ruido fragmenta el sueño aunque no despierte del "
                            "todo. Y un horario estable vale más que cualquier "
                            "otra medida de esta tabla."),
    ]),
    nota("La única regla no negociable de la lista",
         "La última hora sin trabajo y sin pantallas de contenido activante. No "
         "porque la luz azul sea un veneno —ese titular está exagerado— sino "
         "porque el correo, las noticias y las discusiones producen activación "
         "cognitiva, y el sueño no llega mientras el sistema está resolviendo "
         "algo. Se puede leer en una pantalla; no se puede trabajar en ella y "
         "dormirse cinco minutos después."),
)

C5 = cap(
    "Sueño y entrenamiento, en las dos direcciones",
    p("La relación entre las dos cosas es de ida y vuelta, y las dos direcciones "
      "están documentadas en fuentes públicas. Conviene tratarlas por separado "
      "porque las consecuencias prácticas son distintas."),
    h("Lo que el ejercicio le hace al sueño"),
    p("Las guías de actividad física incluyen la mejora del sueño entre los "
      "beneficios que aparecen tras una sola sesión, no después de meses. Es uno "
      "de los efectos agudos mejor descritos, y es un argumento útil para "
      "cualquiera que quiera un premio inmediato por entrenar: la noche de un día "
      "activo es mejor que la de un día sedentario, y eso se comprueba esa misma "
      "noche."),
    p("La excepción conocida es el entrenamiento muy intenso muy cerca de la hora "
      "de acostarse, que en algunas personas retrasa el sueño por la activación y "
      "la temperatura. En otras no pasa nada. Es una de esas cosas que se "
      "resuelven probando dos semanas y no discutiendo."),
    h("Lo que el sueño le hace al entrenamiento"),
    ficha("Lo que se deteriora al dormir poco", [
        ("Recuperación", "El tejido se repara sobre todo durante el descanso. Un "
                         "déficit sostenido alarga el tiempo que se tarda en "
                         "estar listo para la sesión siguiente."),
        ("Rendimiento", "Cae más la parte que depende de la coordinación, la "
                        "atención y la tolerancia al esfuerzo que la fuerza "
                        "máxima bruta. Se nota antes en un deporte técnico que en "
                        "una sentadilla."),
        ("Apetito y elecciones", "El déficit de sueño se asocia a más hambre y a "
                                 "peores elecciones de comida. Es una de las "
                                 "razones por las que dormir mal sabotea una "
                                 "dieta sin que la persona sepa por qué."),
        ("Lesión", "Menos atención y peor tiempo de reacción es exactamente el "
                   "escenario en el que ocurren los accidentes en entrenamiento, "
                   "y también fuera de él."),
    ]),
    p("La conclusión práctica es incómoda para quien duerme cinco horas y madruga "
      "para entrenar: en una semana muy justa de sueño, cambiar una sesión por "
      "una hora más de sueño no es pereza, es una decisión defendible. La sesión "
      "de mañana existirá; esta noche solo hay una."),
    sep(),
    h("La descarga y el descanso no son lo mismo"),
    p("Vale la pena distinguir dos cosas que la palabra «descanso» confunde. El "
      "Códice de la Carga describe qué le pasa a un cuerpo al que se le retira la "
      "carga mecánica: pierde músculo, fuerza y hueso. Eso es descarga, y es "
      "deterioro."),
    ficha("Los cinco efectos de la descarga, para no confundirlos con descansar",
          [(que, ritmo) for que, ritmo, _ in D.DESCARGA]),
    p("El descanso de este libro es lo contrario: es el intervalo entre cargas "
      "durante el cual la adaptación ocurre. Sin él, la carga no produce mejora "
      "sino acumulación. Un día sin entrenar dentro de una semana con "
      "entrenamiento es descanso; tres meses en el sofá son descarga. Es la misma "
      "quietud con dos significados opuestos, y depende enteramente de lo que "
      "haya alrededor."),
    nota("Lo que dice la doctrina sobre esto",
         "El manual de salud y preparación física del Ejército de Estados Unidos "
         "trata el sueño como uno de sus cinco dominios de preparación, al mismo "
         "nivel que el físico y el nutricional, y describe prácticas de gestión "
         "—horarios, siestas planificadas, control de cafeína y luz— para "
         "sostener el rendimiento en condiciones donde dormir bien no siempre es "
         "posible. Es probablemente el documento gratuito más práctico que existe "
         "sobre el asunto, y casi nadie fuera de esa institución lo ha abierto."),
)

C6 = cap(
    "La siesta, bien hecha",
    p("La siesta es una herramienta con instrucciones, y usarla mal produce "
      "exactamente el efecto que sus detractores describen. Con dos parámetros "
      "bien elegidos —duración y hora— hace lo que promete."),
    ficha("Las dos duraciones que funcionan", [
        ("De 10 a 20 minutos", "Se sale de sueño ligero, sin aturdimiento, y "
                               "mejora la alerta durante unas horas. Es la "
                               "siesta por defecto y la que sirve para casi "
                               "todo."),
        ("Unos 90 minutos", "Un ciclo completo, así que se despierta al final "
                            "del ciclo y no en mitad del sueño profundo. Solo "
                            "tiene sentido con déficit acumulado o antes de una "
                            "noche que se sabe corta."),
        ("Entre 30 y 60 minutos", "La franja mala: bastante probabilidad de "
                                  "despertar en sueño profundo, con la sensación "
                                  "pastosa que dura media hora."),
    ]),
    h("La hora"),
    p("A primera hora de la tarde hay un descenso natural de alerta que no se "
      "debe a la comida —ocurre igual sin comer— y ese es el momento en el que "
      "una siesta corta encaja sin coste. A partir de media tarde empieza a "
      "restarle presión de sueño a la noche, y ahí sí compite con lo importante."),
    p("La regla práctica: siesta corta, temprana, y solo si duermes bien por la "
      "noche. Quien tiene insomnio debería evitarla, porque parte del tratamiento "
      "del insomnio consiste precisamente en concentrar toda la presión de sueño "
      "en la noche."),
    nota("La siesta de café, que suena a truco y no lo es",
         "Tomar un café inmediatamente ANTES de una siesta de quince minutos "
         "funciona porque la cafeína tarda del orden de veinte a treinta minutos "
         "en hacer efecto: la siesta ocurre antes de que llegue y los dos efectos "
         "se suman al despertar. Es una práctica que también aparece en contextos "
         "de gestión de la fatiga profesional, y es la única cosa de este libro "
         "que se puede probar hoy mismo."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · EL OFICIO
# ══════════════════════════════════════════════════════════════════════

C7 = cap(
    "Cómo comprobarlo tú mismo",
    p("Como en el resto de la colección, aquí van las fuentes con nombre y con "
      "indicación de dónde se consultan, para que este libro se pueda verificar y "
      "corregir."),
    ficha("Las fuentes de la colección", [(n, d) for n, d in D.FUENTES]),
    sep(),
    h("Las que sostienen específicamente este libro"),
    ficha("Rutas concretas", [
        ("El dominio del sueño", "FM 7-22, Holistic Health and Fitness, en la "
                                 "biblioteca de publicaciones del Ejército de "
                                 "Estados Unidos. Publicado entero. Busca el "
                                 "capítulo de sleep readiness: horarios, siestas "
                                 "planificadas, cafeína y luz."),
        ("Duración recomendada", "Las recomendaciones de salud pública sobre "
                                 "duración del sueño en adultos, difundidas por "
                                 "los Centros para el Control y la Prevención de "
                                 "Enfermedades en cdc.gov, con su apartado de "
                                 "higiene del sueño."),
        ("Sueño y ejercicio", "Physical Activity Guidelines for Americans, "
                              "segunda edición, en health.gov. La mejora del "
                              "sueño figura entre los beneficios agudos de una "
                              "sola sesión."),
        ("Descarga y reposo", "Programa de Investigación Humana de la NASA. "
                              "Estudios de reposo en cama, que son la fuente de "
                              "la distinción entre descarga y descanso."),
    ]),
    h("Y cómo se comprueba este libro a sí mismo"),
    p("Las cifras de sueño de estas páginas viven en el mismo módulo de datos que "
      "los otros tres libros, y una de las comprobaciones que se ejecutan antes "
      "de componer es específica de aquí:"),
    lista(
        f"Que {CICLO_MAX} ciclos de {S['ciclo_min']} minutos —{hh(HORAS_MAX)} "
        f"horas— alcancen la recomendación de {S['adulto_horas']} horas. Si la "
        "duración del ciclo o el número de ciclos se cambiaran a valores que no "
        "cuadran con la recomendación, el libro no se escribiría.",
        "Que las cuatro fases estén completas con sus cuatro campos, que es lo "
        "que garantiza que la tabla del texto y la lámina digan lo mismo.",
        "Y las comprobaciones compartidas con los otros libros: rangos de "
        "macronutrientes, coherencia de la fibra, techos de micronutrientes, "
        "equivalencia de intensidades y bandas metabólicas.",
    ),
    p("Los números de horas que aparecen en el capítulo primero no están "
      "tecleados: se calculan multiplicando ciclos por duración. Es una precaución "
      "pequeña con un efecto concreto, que es que el texto no pueda envejecer mal "
      "si algún día se corrige el dato de partida."),
)

C8 = cap(
    "Cuaderno del descanso",
    p("Cuatro semanas. La primera mide, la segunda ancla el horario, la tercera "
      "retira lo que estorba y la cuarta pone a prueba lo aprendido. Ninguna "
      "requiere comprar nada."),
    h("Semana 1 · Medir sin cambiar"),
    pasos(
        "Anota cada día tres cosas: a qué hora te acostaste, a qué hora te "
        "levantaste, y una nota de una palabra sobre cómo estabas por la tarde.",
        "Anota también la hora del último café y la del último alcohol, si los "
        "hubo.",
        "No uses una app de seguimiento del sueño. Su estimación de fases es poco "
        "fiable y produce ansiedad de rendimiento sobre algo que empeora "
        "precisamente al intentarlo.",
        "Al final de la semana, calcula tu media de horas y tu deuda contra las "
        f"{S['adulto_horas']} recomendadas. Ese número es el diagnóstico.",
    ),
    h("Semana 2 · Fijar el ancla"),
    pasos(
        "Elige una hora de levantarte y mantenla los siete días, incluido el fin "
        "de semana. Los siete.",
        "Sal a la luz exterior diez o quince minutos dentro de la primera hora "
        "tras levantarte. Aunque esté nublado: la luz de un día gris sigue siendo "
        "muchísimo más intensa que la de una habitación.",
        "No toques la hora de acostarte todavía. Se ajusta sola cuando el ancla "
        "está puesta.",
        "Anota si te cuesta menos dormirte al final de la semana. Suele notarse "
        "hacia el cuarto o quinto día.",
    ),
    h("Semana 3 · Retirar"),
    pasos(
        "Aplica la cuenta atrás: cafeína fuera diez horas antes, comida grande y "
        "alcohol tres, entrenamiento fuerte dos, trabajo y pantallas activantes "
        "una.",
        "Si no puedes con todas, aplica solo dos: la cafeína y la última hora. "
        "Son las que más rinden.",
        "Baja la luz de la casa en esa última hora. Lámparas en vez del techo. Es "
        "un cambio de dos minutos con efecto real.",
        "Anota los despertares nocturnos que recuerdes. Compara con la semana 1.",
    ),
    h("Semana 4 · La prueba de la noche mala"),
    pasos(
        "Habrá una noche mala. Cuando llegue, no compenses al día siguiente "
        "quedándote más en la cama ni acostándote mucho antes: mantén el ancla.",
        "Sí puedes usar una siesta corta y temprana, de diez a veinte minutos.",
        "Anota cuánto tardas en volver a tu media. Con el ancla puesta suele ser "
        "una noche; sin ella, varias.",
        "Compara la semana 4 con la 1: media de horas, despertares y estado de la "
        "tarde. Si las tres mejoraron sin comprar nada, el cuaderno cumplió.",
    ),
    nota("Qué esperar",
         "La mayoría de la gente que hace estas cuatro semanas no descubre un "
         "problema exótico: descubre que se acuesta cuarenta minutos más tarde de "
         "lo que cree, que el café de las cinco no era inocente y que la hora fija "
         "de levantarse arregla más que todos los rituales nocturnos juntos. Si "
         "en tu caso las cuatro semanas no mejoran nada, eso también es "
         "información valiosa, y es la que hay que llevar a una consulta."),
)

C9 = cap(
    "Cuándo esto no es higiene del sueño",
    p("Cierre, y el límite. La higiene del sueño resuelve el sueño de una persona "
      "sana con malas costumbres. No resuelve un trastorno, y confundir las dos "
      "cosas hace que gente con un problema tratable pase años pensando que le "
      "falta disciplina."),
    h("Señales de que hay que consultar y no leer"),
    lista(
        "Ronquido fuerte con pausas respiratorias que alguien haya presenciado, o "
        "despertarse ahogándose. Con somnolencia diurna marcada, dolor de cabeza "
        "al despertar o tensión arterial difícil de controlar, apunta a apnea del "
        "sueño, que es frecuente, infradiagnosticada y muy tratable.",
        "Dificultad para dormirse o mantenerse dormido al menos tres noches por "
        "semana durante más de tres meses, con repercusión de día. Eso es "
        "insomnio crónico, y tiene un tratamiento de primera línea que es "
        "psicológico y no farmacológico.",
        "Necesidad irresistible de mover las piernas al acostarse, que mejora al "
        "moverlas. Tiene nombre, causas identificables —el hierro entre ellas— y "
        "tratamiento.",
        "Somnolencia diurna grave pese a dormir suficiente, ataques de sueño "
        "irresistibles o pérdida súbita de tono muscular con la emoción.",
        "Actuar los sueños físicamente, con movimientos bruscos o gritos. Merece "
        "valoración y no es una curiosidad.",
        "Dormir mal junto con ánimo bajo persistente, pérdida de interés o "
        "ansiedad continua. Ahí el sueño es un síntoma y tratarlo aislado no "
        "funciona.",
    ),
    p("Ninguna de estas seis se arregla con una habitación más fresca. Todas "
      "tienen una consulta como primer paso, y la mayoría tienen un tratamiento "
      "que funciona bien."),
    sep(),
    h("Glosario"),
    ficha("", [
        ("Ancla", "La hora de levantarse, que es la señal más potente para fijar "
                  "el reloj interno."),
        ("Ciclo", f"Recorrido completo por las fases del sueño. Unos "
                  f"{S['ciclo_min']} minutos."),
        ("Cronotipo", "Tendencia individual a funcionar mejor por la mañana o por "
                      "la noche. Tiene base biológica y no se cambia a voluntad."),
        ("Deuda de sueño", "Déficit acumulado respecto a la necesidad. Se paga "
                           "solo en parte."),
        ("Hipnograma", "Gráfico del recorrido de las fases a lo largo de la "
                       "noche. Es la primera lámina de este libro."),
        ("N3", FASE["N3"][3]),
        ("Presión de sueño", "Tendencia acumulada a dormirse, que crece con las "
                             "horas despierto y se descarga durmiendo. Es lo que "
                             "una siesta larga a media tarde consume."),
        ("REM", FASE["REM"][3]),
        ("Vida media", "Tiempo que tarda el cuerpo en eliminar la mitad de una "
                       "sustancia. En la cafeína, unas cinco horas en un adulto "
                       "medio."),
    ]),
    sep(),
    p("Y con esto se cierra la serie de fitness y, con ella, los ocho Códices de "
      "VILLUMINATION 99. Cuatro libros para el cuerpo —la mesa, la carga, la "
      "voluntad y el descanso— construidos sobre material público que casi nadie "
      "abre, con las cifras comprobadas antes de imprimirlas y con las fuentes "
      "puestas por su nombre para que puedas llevarle la contraria al libro."),
    p("No prometen ningún resultado y no traen ningún método secreto. Traen la "
      "tabla entera en vez de la mitad publicitable, y la costumbre de comprobar. "
      "Con eso, las decisiones que tomes serán tuyas, que es lo máximo que un "
      "libro honesto puede ofrecer."),
)



# ══════════════════════════════════════════════════════════════════════
#  CAPÍTULOS AÑADIDOS EN LA SEGUNDA EDICIÓN
# ══════════════════════════════════════════════════════════════════════

CE1 = cap(
    "El reloj interno",
    p("Detrás del sueño hay un reloj que no mide horas del reloj de pared sino "
      "un ciclo propio de algo más de un día, y que se pone en hora todas las "
      "mañanas con la luz. Casi todos los problemas de sueño de gente sana son, "
      "en realidad, problemas de ese reloj."),
    fig("de-reloj",
        "El día biológico, hito por hito",
        "Las horas van contadas desde el despertar habitual y corresponden a un "
        "cronotipo intermedio. Ninguno de estos hitos se decide a voluntad: se "
        "arrastran cambiando la hora de levantarse y la exposición a la luz."),
    ficha("Los hitos del día",
          [(f"{'+' if h >= 0 else ''}{h:g} h".replace(".", ",") + f" · {nombre}",
            glosa) for h, nombre, glosa in D.CIRCADIANO]),
    h("Los tres que más se pueden usar"),
    p("El mínimo de temperatura central cae unas dos horas antes de la hora "
      "habitual de despertar, y es el peor momento posible para levantarse. "
      "Quien adelanta el despertador dos horas un día suelto no está robando "
      "dos horas de sueño cualquiera: está despertando en el fondo del pozo, y "
      "de ahí la sensación desproporcionada."),
    p("La zona de mantenimiento de la vigilia es el hito que más consuela "
      "conocer. Las dos o tres horas anteriores a la hora habitual de dormirse "
      "son, paradójicamente, de las más difíciles del día para dormirse: el "
      "reloj empuja hacia arriba justo antes de soltar. Por eso irse a la cama "
      "dos horas antes de lo normal la víspera de un madrugón casi nunca "
      "funciona, y por eso no significa que tengas insomnio."),
    p("Y el inicio de la melatonina, que ocurre con luz tenue un par de horas "
      "antes de dormirse, es el que explica la última hora sin pantallas fuertes "
      "y sin luz de techo. No porque una pantalla envenene: porque la luz "
      "intensa a esa hora retrasa el inicio, y el retraso se paga a la mañana "
      "siguiente."),
    sep(),
    h("El cronotipo, y por qué no es una excusa"),
    p("Existe una variación individual real en la preferencia horaria y tiene "
      "base biológica: hay personas cuyo reloj corre naturalmente adelantado y "
      "otras cuyo reloj corre atrasado. No es una cuestión de disciplina y "
      "burlarse de ello es tan sensato como burlarse de la altura."),
    p("Lo que sí es cierto es que el reloj se puede desplazar dentro de un "
      "margen, y que la herramienta para hacerlo es la luz: luz intensa poco "
      "después de despertar adelanta el reloj; luz intensa por la noche lo "
      "atrasa. Quien quiera madrugar mejor tiene ahí su palanca, y no en "
      "acostarse antes a mirar el techo."),
    nota("Cuándo el desfase deja de ser un cronotipo",
         "Si la preferencia horaria es tan extrema que impide dormir en horarios "
         "socialmente viables durante meses, con repercusión seria en el trabajo "
         "o en los estudios, eso tiene nombre clínico y tratamiento, que incluye "
         "pautas de luz con horarios concretos. No se arregla con fuerza de "
         "voluntad y merece una consulta."),
)

CE2 = cap(
    "Cafeína, alcohol y nicotina",
    p("Tres sustancias legales, dos de ellas de consumo diario para media "
      "población, y las tres actúan sobre el sueño de maneras distintas y "
      "predecibles. La cafeína merece el grueso del capítulo porque es la que "
      "más se subestima."),
    fig("de-cafeina",
        "La curva de eliminación de la cafeína",
        "Cada vida media se lleva la mitad de lo que quedaba. Con unas cinco "
        "horas de vida media, a las diez horas queda una cuarta parte y a las "
        "quince, una octava. Las cifras se calculan a partir de la vida media, "
        "no están escritas a mano."),
    p(D.CAFEINA["nota"]),
    h("Las cuatro cosas que hay que saber de la cafeína"),
    ficha("", [
        ("No impide dormirse necesariamente", "Puede dejarte dormir y aun así "
                                              "recortar el sueño profundo de esa "
                                              "noche. Ese efecto no se percibe, "
                                              "y de ahí el «a mí no me afecta»."),
        ("La velocidad varía muchísimo", f"La vida media va de unas "
                                         f"{D.CAFEINA['rango_vida_media'][0]} a "
                                         f"{D.CAFEINA['rango_vida_media'][1]} "
                                         "horas entre personas sanas. Hay quien "
                                         "la elimina al doble de rápido que su "
                                         "vecino."),
        ("Tarda en actuar", f"Del orden de {D.CAFEINA['efecto_min']} a treinta "
                            "minutos. Es lo que hace posible la siesta con café "
                            "del capítulo de la siesta."),
        ("Se acumula", "El café de las cinco se suma a lo que queda del de las "
                       "once. La cuenta del día importa más que la última taza."),
    ]),
    p("La prueba para saber si te afecta no es razonarlo: es quitarla dos "
      "semanas y comparar el registro. Cualquier otra respuesta es una opinión "
      "sobre uno mismo, y en esto las opiniones sobre uno mismo son "
      "notoriamente malas."),
    h("Y la abstinencia, que existe"),
    p("Quitar la cafeína de golpe produce dolor de cabeza, irritabilidad y "
      "cansancio durante unos días en quien la consume a diario. No es un signo "
      "de nada grave y se pasa; conviene saberlo para no confundirlo con «me "
      "sienta mal dejar el café». Bajar de forma escalonada a lo largo de una "
      "semana lo evita casi por completo."),
    sep(),
    h("El alcohol: el engaño mejor mantenido"),
    p("Acorta el tiempo que se tarda en dormirse, y de ahí su fama de ayudar. "
      "Después hace lo contrario: fragmenta la segunda mitad de la noche y "
      "suprime parte del sueño con movimientos oculares rápidos, que es "
      "exactamente el que vive ahí. La noche empieza fácil y termina mal, con "
      "más despertares, más sed y peor sensación de descanso."),
    p("Se suma un segundo efecto que interesa a cualquiera que ronque: el "
      "alcohol relaja la musculatura de la vía aérea superior y empeora los "
      "episodios de apnea. Alguien con apnea no diagnosticada tiene sus peores "
      "noches precisamente después de beber, y suele atribuirlas a otra cosa."),
    h("La nicotina"),
    p("Es un estimulante, aunque el gesto de fumar se viva como relajante. "
      "Alarga el tiempo que se tarda en dormirse y, en consumo alto, produce "
      "despertares de madrugada por la caída de niveles: una abstinencia en "
      "miniatura en mitad de la noche. Los primeros días de dejarlo el sueño "
      "empeora, y eso conviene anticiparlo para no interpretarlo como una razón "
      "para volver."),
    nota("Y una que casi nadie mira: los medicamentos",
         "Varios fármacos de uso común alteran el sueño: algunos "
         "antihipertensivos, algunos antidepresivos, los corticoides, los "
         "descongestionantes y los broncodilatadores, entre otros. Si tu sueño "
         "empeoró de forma clara al empezar un tratamiento, eso se comenta con "
         "quien te lo recetó. A menudo hay una alternativa o un cambio de hora "
         "de la toma que lo resuelve, y es una conversación de dos minutos."),
)

CE3 = cap(
    "La habitación",
    p("La higiene del sueño se ocupa de la conducta; este capítulo se ocupa del "
      "sitio. Es la parte más barata de arreglar y la que más gente ignora "
      "mientras compra suplementos."),
    ficha("Las cuatro variables físicas", [
        ("Temperatura", "Fresca. Dormirse requiere que la temperatura central "
                        "baje, y una habitación caliente lo impide. Es la "
                        "variable con más efecto y la más fácil de cambiar."),
        ("Luz", "Oscuridad real. Las persianas que dejan pasar la farola, el "
                "piloto del televisor y el móvil boca arriba en la mesilla "
                "cuentan. Un antifaz cuesta poco y funciona."),
        ("Ruido", "El ruido fragmenta el sueño aunque no llegue a despertar, y "
                  "ese despertar parcial no se recuerda por la mañana. Tapones, "
                  "o ruido de fondo constante que enmascare los picos."),
        ("Superficie", "Que no duela. Más allá de eso, la industria del colchón "
                       "promete bastante más de lo que puede demostrar: la "
                       "mejor almohada es la que mantiene el cuello alineado en "
                       "tu postura habitual, y eso no depende del precio."),
    ]),
    h("La regla que convierte la cama en una señal"),
    p("Este es el punto más importante del capítulo y viene del tratamiento no "
      "farmacológico del insomnio, donde se llama control de estímulos. La idea "
      "es que la cama sea una señal inequívoca de dormir, y para eso no puede "
      "ser también el sitio donde se trabaja, se ve una serie, se discute o se "
      "da vueltas durante una hora sin dormir."),
    pasos(
        "La cama es para dormir y para el sexo. Nada más: ni portátil, ni "
        "papeleo, ni noticias.",
        "A la cama solo cuando hay sueño de verdad, no solo cansancio.",
        "Si llevas unos veinte minutos despierto y empiezas a agobiarte, "
        "levántate y ve a otra habitación con luz tenue a hacer algo aburrido. "
        "Vuelve cuando vuelva el sueño. Sí, aunque sea la tercera vez.",
        "Nada de mirar el reloj. Saber la hora no ayuda a dormir y sí alimenta "
        "la cuenta atrás mental, que es lo que mantiene despierto.",
        "La hora de levantarse no cambia por una mala noche. Es el ancla, y "
        "moverla convierte una noche mala en una semana mala.",
    ),
    p("Estas cinco reglas parecen severas y son la parte que de verdad funciona. "
      "Levantarse de la cama a las tres de la madrugada resulta contraintuitivo, "
      "y es precisamente lo que rompe la asociación entre la cama y la "
      "frustración, que es lo que sostiene un insomnio una vez instalado."),
    sep(),
    h("Compartir cama"),
    p("Dos personas con horarios, temperaturas preferidas y ronquidos distintos "
      "en el mismo espacio es un problema de ingeniería, no de romanticismo. Las "
      "soluciones que funcionan son poco glamurosas: mantas separadas, tapones, "
      "colchón con menos transmisión de movimiento y, cuando hace falta, "
      "habitaciones separadas algunas noches. Dormir mal por costumbre social "
      "tiene un coste real sobre la salud de los dos."),
    nota("Las mascotas",
         "Un animal en la cama produce microdespertares que no se recuerdan y "
         "que aparecen en cuanto se mide. Si duermes bien, no hay ningún motivo "
         "para cambiar nada. Si duermes mal y tienes un animal en la cama, es "
         "una de las variables más fáciles de probar durante dos semanas."),
)

CE4 = cap(
    "Cuando el sueño no llega: lo que de verdad funciona",
    p("Este capítulo trata el insomnio que no es un trastorno diagnosticado sino "
      "una racha, y describe el enfoque que la evidencia respalda como primera "
      "línea, que no es un fármaco. Si la situación es persistente, el capítulo "
      "final dice cuándo hay que consultar, y hay que hacerlo."),
    h("El bucle que lo mantiene"),
    p("Casi todos los insomnios empiezan por una causa —un disgusto, un cambio "
      "de horario, una enfermedad— y se mantienen después por otra distinta: por "
      "lo que la persona hace para compensarlos. Es un bucle reconocible:"),
    ficha("Cómo se instala", [
        ("Duermo mal una noche", "Causa cualquiera. Hasta aquí, normal"),
        ("Compenso", "Me acuesto antes, me levanto más tarde, echo una siesta "
                     "larga, cancelo cosas"),
        ("Paso más tiempo en la cama sin dormir", "La cama pasa a asociarse con "
                                                  "estar despierto y "
                                                  "frustrado"),
        ("Me preocupa no dormir", "La preocupación activa, y la activación es lo "
                                  "contrario de dormir"),
        ("Duermo peor", "Y vuelta al segundo escalón, ahora con más "
                        "convicción"),
    ]),
    p("La clave del bucle está en el segundo escalón, y es contraintuitiva: "
      "compensar empeora. Pasar diez horas en la cama para conseguir seis de "
      "sueño produce un sueño más fragmentado y menos profundo que pasar siete "
      "para conseguir seis y media."),
    h("Las dos palancas que funcionan"),
    ficha("", [
        ("Control de estímulos", "Las cinco reglas del capítulo de la habitación. La "
                                 "cama vuelve a significar dormir."),
        ("Restricción del tiempo en cama", "Ajustar el tiempo en la cama a lo "
                                           "que realmente se duerme, y "
                                           "ampliarlo poco a poco a medida que "
                                           "el sueño se consolida. Es la parte "
                                           "que más funciona y la que peor "
                                           "suena."),
    ]),
    pasos(
        "Durante una semana anota a qué hora te acuestas, a qué hora te "
        "levantas y cuánto crees que dormiste.",
        "Calcula la media de sueño real. Digamos que sale seis horas.",
        "Fija una ventana en la cama de esa cifra más media hora, con la hora "
        "de levantarse fija. Seis y media, ni más ni menos.",
        "Cuando durante una semana duermas la mayor parte de esa ventana, "
        "amplíala quince o veinte minutos. Y así.",
        "No bajes nunca de cinco horas de ventana, y no hagas esto por tu cuenta "
        "si conduces profesionalmente, si tienes epilepsia, trastorno bipolar o "
        "apnea sin tratar. En esos casos se hace acompañado.",
    ),
    p("Las primeras noches se duerme peor y se está más cansado durante el día: "
      "es lo esperado y es el mecanismo, porque lo que se está haciendo es "
      "acumular presión de sueño hasta que la noche se consolide. Suele "
      "empezar a notarse en una o dos semanas."),
    sep(),
    h("Lo que no funciona, aunque lo parezca"),
    lista(
        "Quedarse en la cama «descansando» sin dormir. Alimenta el bucle "
        "entero.",
        "Recuperar con siestas largas. Consume la presión de sueño que "
        "necesitas por la noche. Con insomnio, la siesta se suspende.",
        "Acostarse mucho antes. La zona de mantenimiento de la vigilia "
        "garantiza que no vas a dormirte, y añade una hora de frustración en la "
        "cama.",
        "Beber para dormir. El capítulo de la cafeína y el alcohol explica por "
        "qué es exactamente la peor idea de la lista.",
        "Comprobar el móvil «ya que estoy despierto». Luz, activación y hora en "
        "la pantalla, los tres a la vez.",
    ),
    nota("Sobre los fármacos y la melatonina",
         "Los hipnóticos tienen indicaciones concretas, plazos cortos y efectos "
         "adversos, y esa conversación es con quien receta y no con un libro. La "
         "melatonina no es un somnífero: es una señal horaria, y su utilidad "
         "depende de la dosis y sobre todo de la hora a la que se toma, que es "
         "lo que casi nadie tiene en cuenta. Tomarla al acostarse «para dormir» "
         "es el uso más común y el que menos respaldo tiene."),
)

CE5 = cap(
    "Turnos, viajes y noches rotas",
    p("Todo lo anterior supone una vida con horarios estables. Buena parte de la "
      "población no la tiene, y merece un capítulo en vez de la recomendación "
      "inútil de «mantén un horario regular»."),
    h("Trabajo por turnos"),
    p("Trabajar de noche obliga a dormir cuando el reloj interno empuja hacia "
      "arriba, y a estar despierto cuando empuja hacia abajo. No hay manera de "
      "que eso salga gratis, y conviene decirlo con claridad porque la "
      "literatura es consistente: el trabajo nocturno prolongado se asocia a "
      "peor salud metabólica y cardiovascular. Lo que sigue reduce el daño; no "
      "lo elimina."),
    ficha("Lo que ayuda", [
        ("Luz durante el turno", "Ambiente bien iluminado en la primera mitad "
                                 "del turno ayuda a mantener la alerta."),
        ("Gafas oscuras al volver", "Al salir con luz de día, la luz de la "
                                    "mañana ordena al reloj despertarse. "
                                    "Filtrarla en el trayecto a casa ayuda a "
                                    "dormir después."),
        ("Habitación a oscuras total", "Aquí el antifaz y las persianas dejan de "
                                       "ser un lujo."),
        ("Cafeína al principio", "Al principio del turno, no al final. La cuenta "
                                 "de la vida media sigue valiendo aunque sea de "
                                 "noche."),
        ("Siesta antes del turno", "Una siesta profiláctica antes de entrar "
                                   "rinde más que intentar aguantar y compensar "
                                   "después."),
        ("Rotación hacia delante", "Si el turno rota, hacia delante —mañana, "
                                   "tarde, noche— se tolera mejor que hacia "
                                   "atrás. Es más fácil retrasar el reloj que "
                                   "adelantarlo."),
    ]),
    sep(),
    h("Viajes con cambio de huso"),
    p("El desfase horario tiene una regla útil: al viajar hacia el este hay que "
      "adelantar el reloj, y adelantarlo cuesta más que atrasarlo. Por eso los "
      "viajes hacia el este sientan peor que los viajes hacia el oeste con el "
      "mismo número de husos."),
    pasos(
        "Ponte en hora de destino en cuanto subas al avión: el reloj, las "
        "comidas y el sueño.",
        "Al llegar, sal a la luz del día en el horario que le toca al destino. "
        "La luz es la que pone el reloj en hora; el resto es acompañamiento.",
        "Hacia el este, busca luz por la mañana en destino y evítala a última "
        "hora. Hacia el oeste, al revés: luz por la tarde y evitarla temprano.",
        "Cuenta con aproximadamente un día por huso para ajustarte del todo. Un "
        "viaje de tres días a seis husos no da tiempo a nada: en ese caso a "
        "veces conviene NO ajustarse y mantener el horario de origen.",
        "El alcohol del vuelo empeora todo lo anterior, y la deshidratación de "
        "la cabina no ayuda.",
    ),
    h("La noche rota que no se elige"),
    p("Un bebé, una guardia, un familiar enfermo. Aquí no hay optimización "
      "posible y sí hay tres cosas que reducen el daño: dormir en bloques "
      "aunque sean cortos en vez de estar despierto en vigilancia continua, "
      "repartir las noches con alguien si es posible, y proteger la seguridad —no "
      "conducir con sueño acumulado— por encima de cualquier otra "
      "consideración."),
    nota("La regla que no se negocia",
         "La somnolencia al volante deteriora la atención y el tiempo de "
         "reacción de forma comparable a otras causas que sí están perseguidas "
         "por ley, y a diferencia de ellas no se compensa con voluntad. Si "
         "llevas una racha de sueño corto, esa es la parte de este libro que "
         "puede salvarte la vida: no conduzcas, o para y duerme veinte minutos "
         "antes de seguir."),
)

CE6 = cap(
    "Recuperación: lo que se puede comprar y lo que no",
    p("La palabra recuperación se ha convertido en una categoría comercial: "
      "botas de compresión, crioterapia, pistolas de masaje, bebidas, "
      "dispositivos. Este capítulo ordena todo eso por lo que se sabe de cada "
      "cosa, y el orden es incómodo para el sector."),
    ficha("Por orden de importancia real", [
        ("1 · Dormir suficiente", "Sin discusión y sin sustituto. Es la "
                                  "intervención de recuperación con mejor "
                                  "respaldo, la más barata y la que menos se "
                                  "hace."),
        ("2 · Comer suficiente", "Energía total y proteína. Un déficit "
                                 "sostenido convierte cualquier programa en "
                                 "acumulación de fatiga."),
        ("3 · Programar bien la carga", "Semanas de menos, variación de "
                                        "intensidad, un día fácil después de "
                                        "uno duro. La recuperación se diseña "
                                        "antes de necesitarla."),
        ("4 · Moverse suave los días de descanso", "Andar, nadar, pedalear "
                                                   "flojo. Barato y con efecto "
                                                   "modesto y real sobre cómo se "
                                                   "llega al día siguiente."),
        ("5 · Todo lo demás", "Masaje, frío, compresión, dispositivos. Efectos "
                              "pequeños, sobre todo en la sensación, y ninguno "
                              "compensa un fallo en los cuatro primeros."),
    ]),
    h("El caso del frío, que merece un párrafo aparte"),
    p("Meterse en agua fría después de entrenar reduce la sensación de agujetas, "
      "y eso está bastante bien descrito. Lo que también está descrito es que, "
      "usado de forma sistemática justo después del entrenamiento de fuerza, "
      "puede atenuar parte de la adaptación que ese entrenamiento buscaba: la "
      "inflamación que se está apagando es, en parte, la señal."),
    p("La lectura práctica: si el objetivo es rendir mañana en una competición, "
      "el frío tiene sentido. Si el objetivo es ganar masa y fuerza a lo largo "
      "de meses, apagar la señal cada día no parece buena idea. Es un ejemplo "
      "limpio de que una herramienta puede ser útil para un objetivo y "
      "contraproducente para otro."),
    sep(),
    h("La semana de menos"),
    p("Programar una semana de carga reducida cada cierto tiempo —cuatro a ocho "
      "semanas, según lo dura que sea la etapa— no es perder el tiempo: es lo "
      "que permite que la adaptación acumulada se exprese. Se reduce el volumen "
      "más o menos a la mitad, se mantiene algo de intensidad para no perder el "
      "punto, y se descansa de verdad."),
    lista(
        "Las señales de que hace falta antes de lo previsto: el rendimiento baja "
        "tres sesiones seguidas, el sueño empeora, las ganas de entrenar "
        "desaparecen y las molestias articulares se acumulan.",
        "Esas cuatro señales aparecen en ese orden más o menos, y las dos "
        "primeras son las que se ven en el cuaderno.",
        "Bajar antes de romperse cuesta una semana. Bajar después de romperse "
        "cuesta meses. Es toda la aritmética del asunto.",
    ),
    nota("Los dispositivos que miden el sueño",
         "Estiman las fases con una fiabilidad bastante limitada, y producen un "
         "efecto secundario documentado: la ansiedad por la puntuación del "
         "sueño, que empeora precisamente lo que se está intentando medir. "
         "Sirven razonablemente para una cosa —estimar la duración total y ver "
         "tendencias de semanas— y bastante mal para el resto. Si el número de "
         "la mañana te condiciona el día, apágalo."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-descanso",
    "titulo": "Códice del Descanso",
    "subtitulo": "La arquitectura de una noche, la deuda que deja una semana corta y la diferencia entre descansar y descargarse",
    "autor": "Villumination 99",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-descanso",
    "acento": "calma",
    "original": True,
    "laminas": ["descanso.svg"],
    "claves": ["sueño", "recuperación", "hipnograma", "deuda de sueño",
               "higiene del sueño", "siesta", "cafeína", "villuminations"],
    "capitulos": [
        C1, CE1, C2, C3,       # I · La noche por dentro
        C4, CE2, CE3, C6,      # II · Lo que se puede hacer
        CE4, CE5,              # III · Cuando no llega
        C5, CE6,               # IV · Entrenamiento y recuperación
        C7, C8, C9,            # V · El oficio
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
          f"{palabras:,} palabras · {CICLO_MAX} ciclos × {S['ciclo_min']} min = "
          f"{hh(HORAS_MAX)} h comprobadas · → {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
