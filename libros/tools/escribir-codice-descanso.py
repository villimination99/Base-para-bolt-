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
        C1, C2, C3,       # I · La noche por dentro
        C4, C5, C6,       # II · Lo que se puede hacer
        C7, C8, C9,       # III · El oficio
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
