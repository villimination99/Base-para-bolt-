#!/usr/bin/env python3
"""
CÓDICE DE LA VOLUNTAD — obra original de VILLUMINATIONS
=========================================================
Séptimo libro de la colección y tercero de la serie de fitness. La mentalidad
del entrenamiento tratada como un problema de ingeniería de conducta y no de
motivación.

Base pública y libre: el FM 7-22 del Ejército de Estados Unidos —que dedica un
dominio entero a la preparación mental y publica sus habilidades de rendimiento
sin reservarse nada— y el capítulo de cambio de conducta de las Physical
Activity Guidelines. Ambas son obra del gobierno federal estadounidense y no
están sujetas a copyright (17 U.S.C. § 105). Donde este libro usa material que
NO viene de esas fuentes, lo dice en la misma frase.

    python3 tools/escribir-codice-voluntad.py && python3 build.py voluntad
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


# ── Atajos ────────────────────────────────────────────────────────────
def p(t):        return {"t": "p", "x": t}
def h(t):        return {"t": "h2", "x": t}
def ficha(tit, filas): return {"t": "ficha", "tit": tit, "x": filas}
def lista(*i):   return {"t": "lista", "x": list(i)}
def pasos(*i):   return {"t": "pasos", "x": list(i)}
def nota(tit, t): return {"t": "nota", "tit": tit, "x": t}
def sep():       return {"t": "sep"}
def ritual(*l):  return {"t": "ritual", "x": list(l)}


def fig(simbolo, tit, pie, clase=""):
    return {"t": "figura", "x": simbolo, "tit": tit, "pie": pie, "clase": clase}


def cap(titulo, *bloques):
    return {"titulo": titulo, "bloques": [b for b in bloques if b]}


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · LA VARIABLE QUE MANDA
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "El libro que no habla de motivación",
    p("Cuánto comer y cuánto moverse son preguntas resueltas: hay cifras, y son "
      "públicas. Este libro trata del problema que hace que esas cifras no sirvan "
      "de nada, que es que casi nadie las cumple más de unas semanas. Y lo trata "
      "sin apelar ni una sola vez a la fuerza de voluntad, porque la fuerza de "
      "voluntad es exactamente lo que no está disponible el martes por la noche a "
      "las once."),
    h("La afirmación de este libro"),
    p("El cumplimiento no es un rasgo de carácter: es el resultado de un diseño. "
      "Quien cumple no suele tener más voluntad que quien abandona; tiene menos "
      "decisiones que tomar, menos fricción en el camino y un plan que sobrevive "
      "a los días malos porque estaba construido contando con ellos."),
    p("Eso convierte el problema en algo que se puede trabajar. La motivación no "
      "se puede fabricar a demanda; el entorno, el tamaño del compromiso, el "
      "momento del día y la respuesta a un fallo, sí."),
    h("Lo que este libro no afirma"),
    lista(
        "No es psicología clínica y no trata trastornos. Si hay un trastorno de "
        "la conducta alimentaria, una depresión, un trastorno de ansiedad o una "
        "adicción de por medio, este libro no es la herramienta y puede incluso "
        "estorbar. La herramienta es un profesional de salud mental.",
        "No promete que vayas a querer entrenar. Ninguna técnica de aquí fabrica "
        "ganas, y la mayoría están pensadas precisamente para funcionar cuando no "
        "las hay.",
        "No convierte la disciplina en una virtud moral. Fallar un plan no dice "
        "nada sobre quién eres, y buena parte de este libro consiste en "
        "desactivar esa lectura, que es la que más gente ha sacado del gimnasio.",
        "No mide nada del cuerpo. Aquí no hay kilos, ni porcentajes, ni fotos de "
        "antes y después.",
    ),
    nota("Dónde se separa este libro de sus fuentes",
         "Un libro sobre nutrición o sobre entrenamiento se apoya casi entero en "
         "cifras oficiales. Aquí eso solo es posible en parte: la doctrina de "
         "preparación mental del Ejército de "
         "Estados Unidos es pública y da un armazón sólido, y las guías de "
         "actividad física tienen un apartado de estrategias de cambio de "
         "conducta. Pero varias de las ideas más útiles de este campo vienen de "
         "literatura académica que NO es de dominio público. Cuando use una de "
         "ellas, lo diré en la misma frase y no la disfrazaré de recomendación "
         "gubernamental. Es la diferencia entre citar y aparentar."),
    sep(),
    h("Cómo está construido lo que sigue"),
    p("El capítulo siguiente presenta el marco de los cinco dominios de "
      "preparación, que es el armazón de todo el libro y la mejor herramienta "
      "de diagnóstico que conozco para saber POR DÓNDE empezar. "
      "Después vienen la variable que domina el resultado, la mecánica de una "
      "conducta repetida, el plan que sobrevive al día malo y la distinción "
      "entre un fallo y un abandono, que es el capítulo que más gente habría "
      "necesitado leer antes de dejarlo."),
    p("Los cuatro últimos tratan lo que rodea a todo eso: el entorno, la "
      "comparación, el regreso después de meses parado y los límites de lo que "
      "un libro como este puede arreglar. Ese último capítulo es, con "
      "diferencia, el más importante del libro."),
)

C2 = cap(
    "La única variable que domina",
    p("Hay una discusión que ocupa la mitad de internet y que está mal planteada "
      "desde la primera línea: cuál es la mejor dieta, cuál es el mejor método de "
      "entrenamiento. La respuesta, en cuanto se mira lo que ocurre a lo largo de "
      "meses y no de semanas, es siempre la misma y es incómoda para todos los "
      "que venden algo."),
    fig("vo-adherencia",
        "La misma dieta, tres grados de cumplimiento",
        "Las tres líneas representan el mismo método aplicado con distinto "
        "cumplimiento. La distancia entre ellas es mayor que la que suele haber "
        "entre dos métodos razonables distintos. Es un esquema conceptual y no "
        "los datos de un estudio concreto: dice qué variable manda, no cuánto "
        "exactamente."),
    h("Lo que esta lámina significa"),
    p("Dos planes distintos, ambos razonables, cumplidos igual de bien, tienden a "
      "dar resultados parecidos. El mismo plan cumplido al noventa por ciento y "
      "al treinta da resultados que no se parecen en nada. Por lo tanto, la "
      "pregunta «¿cuál es mejor?» es menos útil que la pregunta «¿cuál voy a "
      "cumplir?», y esa segunda pregunta solo la puedes contestar tú porque "
      "depende de tu horario, tu cocina, tu trabajo y lo que te gusta comer."),
    p("De aquí sale un criterio de elección que va contra todo el marketing del "
      "sector: entre dos planes, elige el peor de los dos si es el que vas a "
      "sostener. Un plan mediocre ejecutado durante dos años gana por goleada a "
      "uno óptimo ejecutado durante cinco semanas, y ese es el escenario real de "
      "la mayoría de la gente, no una hipótesis."),
    sep(),
    h("Las tres causas por las que un plan bueno se cae"),
    ficha("", [
        ("Demasiado grande", "El compromiso inicial se dimensiona con el "
                             "entusiasmo del primer día, que es un estado "
                             "temporal. Cuando el entusiasmo baja al nivel "
                             "normal, el plan sigue teniendo el tamaño del día "
                             "uno y ya no cabe."),
        ("Demasiada fricción", "Cada paso previo a la conducta es una "
                               "oportunidad de que no ocurra. Un gimnasio a "
                               "cuarenta minutos, una comida que exige comprar "
                               "cuatro cosas raras, una app que hay que abrir y "
                               "actualizar. La fricción no se nota el primer día "
                               "y decide el mes tres."),
        ("Todo o nada", "El plan no contempla el fallo, así que el primer fallo "
                        "lo invalida entero. Es la causa más común y la más fácil "
                        "de arreglar, y tiene su propio capítulo."),
    ]),
    nota("Lo que sí dicen las guías oficiales sobre esto",
         "Las guías de actividad física dedican espacio a las estrategias de "
         "cambio de conducta y mencionan, entre otras, el establecimiento de "
         "objetivos, el autorregistro, el apoyo social y la modificación del "
         "entorno. No es un descubrimiento de este libro: es un apartado poco "
         "leído de un documento muy citado."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LA MECÁNICA
# ══════════════════════════════════════════════════════════════════════

C3 = cap(
    "El bucle y sus tres palancas",
    p("Una conducta repetida tiene una estructura muy simple: algo la dispara, "
      "algo se hace, y algo mantiene el conjunto. Las tres piezas se pueden "
      "tocar, pero no cuestan lo mismo, y casi todo el mundo intenta tocar "
      "precisamente la más difícil."),
    fig("vo-habito",
        "El bucle con los tres puntos donde se puede intervenir",
        "La señal, la rutina y el premio. La rutina es la parte visible y la más "
        "difícil de cambiar por decisión directa; la señal y el premio son "
        "manipulables con mucho menos esfuerzo y son los que de verdad mueven el "
        "bucle."),
    h("La señal: cambiar el entorno en vez de la persona"),
    p("Una conducta que depende de acordarse es una conducta frágil. Una que está "
      "atada a algo que ya pasa todos los días no lo es. Por eso la intervención "
      "más rentable no es proponerse entrenar más: es decidir a qué señal "
      "existente se engancha el entrenamiento."),
    lista(
        "Al salir del trabajo, antes de llegar a casa. Entrar en casa es una "
        "señal potentísima de que la jornada terminó, y muy poca gente vuelve a "
        "salir.",
        "Justo después de dejar a los niños, de la primera reunión, de cerrar el "
        "portátil. La estructura del día ya tiene bisagras: se usan esas.",
        "La ropa preparada la noche anterior a la vista. Suena trivial y elimina "
        "una decisión completa de la mañana.",
    ),
    h("El premio: hacerlo inmediato"),
    p("El problema estructural del ejercicio y de comer bien es que el premio "
      "llega meses después y el coste llega ahora. Ninguna conducta se sostiene "
      "así de forma natural, y por eso hay que fabricar una consecuencia "
      "inmediata que sí exista."),
    lista(
        "Marcar la casilla en un calendario a la vista. Ridículamente simple y de "
        "las cosas mejor documentadas: el registro visible es una de las "
        "estrategias que las propias guías mencionan.",
        "Atar el entrenamiento a algo agradable que solo ocurra ahí: una serie, "
        "un disco, un pódcast que no se escuche en ningún otro momento.",
        "Fijarse en cómo se está treinta minutos DESPUÉS de la sesión, no "
        "durante. La mejora de humor y de energía posterior a una sesión es "
        "inmediata y está descrita en las guías entre los beneficios agudos. Es "
        "un premio real, y hay que aprender a notarlo.",
    ),
    h("La rutina: la parte que casi no se toca"),
    p("Suprimir una conducta deja un hueco, y el hueco se vuelve a llenar con lo "
      "mismo. Sustituirla funciona mucho mejor: la señal y el premio siguen "
      "siendo los mismos y lo que cambia es lo de en medio. Quien pica por la "
      "tarde por aburrimiento no deja de picar prohibiéndoselo; deja de picar "
      "cuando en ese momento hay otra cosa que hacer que cumple la misma función."),
    nota("De dónde viene esta idea y de dónde no",
         "El esquema de señal, rutina y recompensa es material clásico de la "
         "psicología del aprendizaje y no procede de las fuentes gubernamentales "
         "de este libro. Lo uso porque es el armazón más limpio que conozco y "
         "lo digo para que quede claro qué parte del libro está respaldada por un "
         "organismo oficial y qué parte es un marco conceptual de uso común."),
)

C4 = cap(
    "El plan que sobrevive al día malo",
    p("Todo plan tiene dos versiones: la que se hace cuando todo va bien y la que "
      "se hace cuando no. Casi nadie escribe la segunda, y la segunda es la que "
      "decide el resultado, porque los días malos no son la excepción: son "
      "aproximadamente un tercio de los días."),
    h("El mínimo innegociable"),
    p("La técnica más útil de este libro cabe en una frase: define una versión "
      "diminuta de tu plan que se cumpla siempre, pase lo que pase, y trátala "
      "como innegociable. No es el objetivo; es el suelo."),
    ficha("Ejemplos de suelo", [
        ("Entrenamiento", "Diez minutos. Ponerte la ropa y hacer diez minutos. Si "
                          "después quieres parar, paras y cuenta igual."),
        ("Comida", "Que en la comida principal haya verdura y proteína. El resto "
                   "del día que sea lo que pueda ser."),
        ("Sueño", "Acostarse a la misma hora aunque no se duerma bien. La hora es "
                  "lo innegociable, no las horas."),
        ("Registro", "Una línea en el cuaderno. Aunque la línea diga que hoy no "
                     "hiciste nada."),
    ]),
    p("El suelo hace dos cosas a la vez. Mantiene viva la conducta —que es lo que "
      "de verdad se está protegiendo, más que el efecto fisiológico de esos diez "
      "minutos— y elimina la categoría mental de «día perdido», que es la que "
      "arrastra a los días siguientes."),
    p("Y tiene un efecto lateral que no se busca pero ocurre: bastantes de esos "
      "días en que solo ibas a hacer diez minutos acaban en la sesión completa, "
      "porque la resistencia estaba en empezar y no en el esfuerzo. Los que no, "
      "también valen."),
    sep(),
    h("El plan si-entonces"),
    p("La segunda técnica consiste en decidir por adelantado qué se hará en la "
      "situación concreta que suele descarrilar el plan, en forma de una frase "
      "con dos mitades: si ocurre X, entonces hago Y."),
    lista(
        "Si salgo tarde del trabajo, entonces hago la sesión corta en casa en vez "
        "de ir al gimnasio.",
        "Si en la cena hay algo que no encaja, entonces me sirvo una vez y no "
        "repito, y no cambio nada más del día.",
        "Si me despierto sin ganas, entonces me pongo la ropa y salgo diez "
        "minutos antes de decidir nada.",
        "Si fallo dos días seguidos, entonces el tercero es el suelo y no la "
        "sesión completa.",
    ),
    p("Lo que hace esta técnica es trasladar la decisión de un momento malo —con "
      "prisa, cansancio y hambre— a un momento bueno, que es cuando escribes la "
      "frase. Decidir es caro y en el momento crítico no hay presupuesto. Lo dejo "
      "escrito otra vez: esta idea viene de literatura de psicología que no es de "
      "dominio público; el mecanismo que describe es de sentido común y por eso "
      "está aquí."),
    nota("Cómo se escribe un si-entonces que funcione",
         "Concreto en las dos mitades. «Si tengo poco tiempo, entonces me "
         "organizo mejor» no es un plan: no dice qué situación ni qué conducta. "
         "«Si a las siete no he salido de la oficina, entonces hago la sesión de "
         "veinte minutos del salón» sí lo es. Un si-entonces útil se puede "
         "ejecutar sin pensar, y eso es todo lo que se le pide."),
)

C5 = cap(
    "El fallo y la recaída no son lo mismo",
    p("Este es el capítulo más importante del libro, y el que más gente habría "
      "necesitado leer antes de abandonar. Un fallo y un abandono son dos cosas "
      "distintas separadas por una decisión, y esa decisión se toma después del "
      "fallo, no durante."),
    fig("vo-recaida",
        "La bifurcación que viene después del fallo",
        "El fallo es un punto, no una dirección. Lo que decide el resultado es lo "
        "que ocurre en las horas siguientes: retomar deja el fallo en un dato del "
        "cuaderno; el razonamiento de «ya que lo he roto» convierte un día en una "
        "temporada. La elección está marcada después del punto, no en él."),
    h("El razonamiento que hace el daño"),
    p("Tiene una forma reconocible: «ya que me he saltado la dieta, hoy ya da "
      "igual». «Ya he perdido la semana, empiezo el lunes». «Ya no soy de los "
      "que entrenan». Las tres frases convierten un dato aislado en una "
      "identidad, y la identidad sí dura."),
    p("Es un error de lógica antes que un problema de voluntad. Saltarse una "
      "comida de veintiuna no cambia la semana de forma apreciable; lo que la "
      "cambia es abandonar las veinte restantes. El daño no está en el fallo: "
      "está enteramente en la reacción al fallo, y la aritmética es tan clara que "
      "vale la pena hacerla en voz alta la próxima vez."),
    sep(),
    h("El protocolo de las veinticuatro horas"),
    pasos(
        "Registra el fallo en el cuaderno. Sin adjetivos: qué pasó y en qué "
        "situación. Registrarlo lo convierte en dato en vez de en juicio.",
        "No compenses. No entrenes el doble, no saltes la comida siguiente, no "
        "hagas ayuno de castigo. Compensar refuerza la idea de que hubo una "
        "deuda moral, y esa idea es el problema.",
        "Vuelve al plan en la comida siguiente o en el día siguiente, sin esperar "
        "al lunes. La palabra «lunes» es la señal de alarma de este capítulo.",
        "Al cabo de una semana, mira el registro y busca el patrón. Los fallos se "
        "repiten en las mismas situaciones —el viernes, el viaje, la cena fuera, "
        "el día que duermes mal—, y una situación repetida no se arregla con más "
        "voluntad: se arregla con un si-entonces escrito para ella.",
    ),
    nota("La frase que resume el capítulo",
         "Un fallo es información sobre el plan; un abandono es una decisión "
         "sobre uno mismo. Solo la segunda tiene consecuencias, y solo la segunda "
         "es evitable a voluntad."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · LA DOCTRINA
# ══════════════════════════════════════════════════════════════════════

C6 = cap(
    "Las habilidades de rendimiento, según un manual público",
    p("Aquí es donde este libro sí puede citar una fuente oficial y bastante "
      "poco conocida. El manual de salud y preparación física del Ejército de "
      "Estados Unidos dedica un dominio entero a la preparación mental y "
      "describe un conjunto de habilidades entrenables. Está publicado íntegro y "
      "se descarga gratis, y su contenido es mucho menos épico y mucho más útil "
      "de lo que sugiere su procedencia."),
    ficha("Las habilidades que describe la doctrina", [
        ("Fijación de objetivos", "Objetivos concretos, medibles y escalonados, "
                                  "con un objetivo de proceso —lo que harás— "
                                  "además del de resultado."),
        ("Imaginería o ensayo mental", "Repasar mentalmente la ejecución antes de "
                                       "hacerla, en primera persona y con detalle "
                                       "sensorial."),
        ("Diálogo interno", "Lo que uno se dice durante el esfuerzo. Es "
                            "entrenable y se cambia sustituyendo, no "
                            "suprimiendo."),
        ("Control de la activación", "Subir o bajar el nivel de activación a "
                                     "voluntad. La respiración lenta es la "
                                     "herramienta de bajada; el ritmo, el volumen "
                                     "y la postura, las de subida."),
        ("Control de la atención", "Elegir dónde se pone el foco y devolverlo ahí "
                                   "cuando se va, que es lo que de verdad se "
                                   "entrena."),
        ("Confianza", "En la doctrina no es un estado de ánimo: es el producto "
                      "acumulado de haber cumplido cosas pequeñas. Se construye "
                      "por abajo."),
    ]),
    h("La que más rinde en el gimnasio: el objetivo de proceso"),
    p("Un objetivo de resultado —perder ocho kilos, levantar cien— depende de "
      "cosas que no controlas del todo y solo te da una respuesta al final. Un "
      "objetivo de proceso —tres sesiones esta semana, verdura en la comida "
      "principal— lo controlas entero y te da una respuesta todos los días."),
    p("La recomendación práctica es tener los dos y puntuarte solo por el "
      "segundo. El de resultado marca la dirección; el de proceso es el que "
      "produce la conducta, y castigarse por un objetivo de resultado que se "
      "mueve despacio es la forma más eficiente de abandonar mientras se está "
      "haciendo todo bien."),
    sep(),
    h("Diálogo interno: cómo se cambia de verdad"),
    p("La instrucción de «pensar en positivo» no funciona porque no se puede "
      "dejar de pensar algo por decisión. Lo que sí se puede es tener preparada "
      "otra frase, corta y concreta, y usarla como sustitución. La doctrina "
      "insiste en frases instruccionales —que dicen qué hacer— por encima de las "
      "motivacionales."),
    ficha("Sustituciones", [
        ("«No puedo con esto»", "«Dos repeticiones más y reevalúo»"),
        ("«Estoy fatal hoy»", "«Hoy es día de suelo. Diez minutos»"),
        ("«Voy demasiado lento»", "«Voy. Y esto es lo que hace la diferencia»"),
        ("«Ya lo he roto»", "«Un dato. Siguiente comida, plan normal»"),
    ]),
    nota("Por qué una institución militar sirve de fuente aquí",
         "Por dos motivos concretos. El primero, que no vende nada: no hay un "
         "producto detrás de su doctrina, lo cual es raro en este sector. El "
         "segundo, que opera a una escala en la que las cosas que solo funcionan "
         "con gente muy motivada no sirven, porque tiene que entrenar a todo el "
         "mundo, incluida la mayoría que no quiere estar allí. Ese requisito "
         "produce un método robusto, y es exactamente el requisito de cualquiera "
         "que quiera sostener un hábito diez años."),
)

C7 = cap(
    "Medirse sin castigarse",
    p("El registro es una de las estrategias de cambio de conducta que las guías "
      "mencionan explícitamente, y a la vez es el sitio donde más gente se hace "
      "daño. La diferencia está en qué se registra y cómo se lee."),
    h("El problema de la báscula"),
    p("El peso corporal oscila varios kilos en cuestión de días por motivos que "
      "no tienen nada que ver con la grasa: agua, sal, glucógeno, contenido "
      "intestinal, ciclo hormonal, calor. Alguien que se pesa a diario y se toma "
      "cada cifra en serio está reaccionando emocionalmente a ruido, y el ruido "
      "es más grande que la señal en cualquier ventana corta."),
    lista(
        "Si te pesas, hazlo siempre en las mismas condiciones y mira la media de "
        "siete días contra la media de la semana anterior. Nunca un día contra "
        "otro día.",
        "Si la báscula te estropea el día, la solución correcta es dejar de "
        "pesarte. No es evitar el problema: es que la báscula es una herramienta "
        "opcional y hay otras.",
        "Medidas de cintura, cómo sienta la ropa y una foto mensual en las mismas "
        "condiciones dan mejor información con mucho menos ruido emocional.",
    ),
    h("Lo que sí conviene registrar"),
    ficha("Tres registros que valen más que el peso", [
        ("Cumplimiento", "Cuántas sesiones y cuántas comidas del plan, sobre las "
                         "previstas. Es la variable que manda, así que es la que "
                         "hay que mirar."),
        ("Rendimiento", "Peso levantado, repeticiones, tiempo de un recorrido "
                        "conocido. Sube antes que cualquier cambio visible y es "
                        "un premio inmediato de los que este libro pide fabricar."),
        ("Estado", "Sueño, energía, ganas de la sesión siguiente, dolor. Tres "
                   "palabras al día bastan, y es lo que avisa antes de que algo "
                   "se rompa."),
    ]),
    p("El objetivo del registro no es juzgarte: es tener datos con los que "
      "cambiar el plan. Un cuaderno que produce culpa y no decisiones está mal "
      "diseñado, y hay que reducirlo hasta que produzca decisiones."),
    sep(),
    h("El horizonte correcto"),
    p("Cualquier cosa que se juzgue en menos de un mes se está juzgando con "
      "ruido. La composición corporal se mueve en meses; la fuerza, en semanas; "
      "el humor y el sueño, en días. Conviene saber a qué velocidad se mueve cada "
      "cosa para no revisar la báscula con la frecuencia con la que se revisa el "
      "estado de ánimo."),
    ficha("A qué velocidad cambia cada cosa", [
        ("Horas", "Humor y ansiedad tras una sesión, calidad del sueño de esa "
                  "noche, sensibilidad a la insulina"),
        ("Semanas", "Fuerza, resistencia percibida, técnica, tensión arterial"),
        ("Meses", "Composición corporal, tamaño muscular, capacidad aeróbica "
                  "medida"),
        ("Años", "Densidad ósea, riesgo cardiovascular, autonomía en la vejez"),
    ]),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE IV · EL OFICIO
# ══════════════════════════════════════════════════════════════════════

C8 = cap(
    "Diseñar el entorno antes que la fuerza de voluntad",
    p("Este capítulo se resume en una idea: la voluntad es un recurso agotable y "
      "el entorno no. Cada decisión que consigas eliminar del día es una decisión "
      "que no se puede perder."),
    h("Fricción: quitarla donde quieres ir y ponerla donde no"),
    ficha("La regla de los veinte segundos", [
        ("Para lo que quieres hacer", "Reduce a menos de veinte segundos el "
                                      "tiempo de empezar. Ropa preparada, bolsa "
                                      "hecha, mancuernas a la vista, gimnasio en "
                                      "el camino y no en un desvío."),
        ("Para lo que no", "Añade veinte segundos. Lo que no quieras comer a "
                           "diario, que no esté en casa; si está, que esté en un "
                           "armario alto y en un envase opaco. No es fuerza de "
                           "voluntad: es distancia."),
    ]),
    p("Esto suena a truco menor y es probablemente la intervención con mejor "
      "relación entre esfuerzo y resultado de todo el libro, porque actúa cientos "
      "de veces sin consumir nada. La compra es el momento en que se decide casi "
      "toda la alimentación de la semana, y se hace una vez, en un estado "
      "razonable, con tiempo. Ahí es donde hay que poner el esfuerzo, no en la "
      "cocina a las diez de la noche."),
    sep(),
    h("Las personas también son entorno"),
    p("El apoyo social aparece entre las estrategias que mencionan las guías, y "
      "en la práctica funciona por dos vías distintas que conviene no confundir: "
      "la compañía —hacerlo con alguien, que hace que la sesión ocurra— y el "
      "compromiso público —decirlo, que hace que cueste no ir—. La primera "
      "funciona para casi todo el mundo; la segunda funciona bien con unos y "
      "produce vergüenza y abandono en otros."),
    lista(
        "Si eres de los segundos, comprométete con una sola persona y no con un "
        "grupo, y comprométete al proceso —«voy tres días»— y no al resultado.",
        "Una cita con alguien es más difícil de cancelar que una cita contigo "
        "mismo. Esa asimetría es una herramienta y no un defecto.",
        "Y una advertencia: el entorno también empuja en contra. Si en tu casa o "
        "en tu trabajo hay presión para comer o beber de una manera, eso es un "
        "obstáculo real y merece un si-entonces escrito, no fuerza de voluntad "
        "improvisada.",
    ),
    nota("La versión corta de todo el capítulo",
         "No decidas bien: decide menos. Cada cosa que dejes resuelta de "
         "antemano —la compra, la ropa, el horario, la frase para el momento "
         "malo— es una batalla que no tendrás que ganar en el peor momento del "
         "día."),
)

C9 = cap(
    "Cómo comprobarlo tú mismo",
    p("De todo lo que trata esta obra, la conducta es lo que menos respaldo "
      "oficial tiene disponible, y por eso este capítulo es indispensable. Aquí queda separado, línea "
      "por línea, qué viene de una fuente pública y qué es un marco conceptual "
      "de uso común."),
    ficha("Las fuentes de este libro", [(n, d) for n, d in D.FUENTES]),
    sep(),
    h("Lo que en este libro viene de una fuente oficial"),
    lista(
        "Los cinco dominios de preparación y las habilidades de rendimiento "
        "mental —objetivos, ensayo mental, diálogo interno, control de la "
        "activación, atención y confianza— están en el FM 7-22, Holistic Health "
        "and Fitness, publicado íntegro por el Ejército de Estados Unidos y "
        "descargable en su biblioteca de publicaciones.",
        "Las estrategias de cambio de conducta —objetivos, autorregistro, apoyo "
        "social, modificación del entorno— aparecen en las Physical Activity "
        "Guidelines for Americans, segunda edición, en health.gov.",
        "Los beneficios agudos de una sola sesión sobre humor, ansiedad, sueño y "
        "sensibilidad a la insulina están en esas mismas guías, y son la base del "
        "consejo de fabricar un premio inmediato.",
        f"La dosis de referencia que se usa como objetivo —{A['moderada_min']} a "
        f"{A['moderada_max']} minutos moderados y {A['fuerza_dias']} días de "
        "fuerza— sale del módulo de datos comprobados que este libro ejecuta "
        "antes de componerse, no de una cifra escrita a mano en el texto.",
    ),
    h("Lo que NO viene de una fuente oficial, y se dice"),
    lista(
        "El esquema de señal, rutina y premio es material clásico de psicología "
        "del aprendizaje, no una recomendación gubernamental.",
        "Los planes si-entonces vienen de literatura académica de psicología de "
        "la motivación que no es de dominio público. Aquí se describe el "
        "mecanismo, que es de sentido común, sin reproducir ningún texto.",
        "El fenómeno de «ya que lo he roto» está descrito en la literatura de "
        "prevención de recaídas, tampoco de dominio público. La lámina y el "
        "protocolo de este libro son propios.",
        "La regla práctica de los veinte segundos de fricción es una "
        "formulación divulgativa de uso común, útil y sin respaldo institucional.",
    ),
    p("Hago esta separación porque un libro que envuelve todo en la palabra "
      "«científicamente probado» te está pidiendo que confíes sin comprobar, y "
      "este libro está construido sobre lo contrario. La parte "
      "conceptual de este libro vale lo que valga por sí misma, no por quién la "
      "firma."),
)

C10 = cap(
    "Cuaderno de la voluntad",
    p("Cuatro semanas. No mide el cuerpo: mide la conducta y las situaciones que "
      "la rompen. Es incómodo de llevar y es el que más decisiones cambia."),
    h("Semana 1 · El registro sin juicio"),
    pasos(
        "Cada día, dos líneas: qué hiciste del plan y qué no.",
        "Junto a cada fallo, la situación —no la excusa—: dónde estabas, qué hora "
        "era, con quién, cómo habías dormido.",
        "Prohibido usar adjetivos sobre ti mismo en el cuaderno. «No fui» es un "
        "dato; «soy un desastre» no es nada.",
        "No cambies el plan esta semana.",
    ),
    h("Semana 2 · Definir el suelo"),
    pasos(
        "Escribe tu versión mínima innegociable, para entrenamiento y para "
        "comida. Que sea tan pequeña que te dé un poco de vergüenza.",
        "Comprométete solo con el suelo durante toda la semana. Todo lo que hagas "
        "por encima es extra y no cuenta para nada.",
        "Marca cada día en un calendario a la vista. Es un premio inmediato "
        "barato y funciona mejor de lo que parece.",
        "Al final de la semana, cuenta los días. Si no fueron siete, el suelo era "
        "demasiado alto: bájalo. Sí, otra vez.",
    ),
    h("Semana 3 · Los si-entonces"),
    pasos(
        "Vuelve a la semana 1 y busca las tres situaciones donde se repiten los "
        "fallos.",
        "Escribe un si-entonces para cada una. Concreto en las dos mitades y "
        "ejecutable sin pensar.",
        "Ponlos donde los veas: la nevera, el fondo del móvil, la puerta.",
        "Cuando una de las tres situaciones ocurra, anota si el si-entonces se "
        "activó o no. Si no se activó, casi siempre es porque era demasiado "
        "abstracto.",
    ),
    h("Semana 4 · La prueba del fallo"),
    pasos(
        "Esta semana el objetivo no es cumplir: es practicar el retorno. Cuando "
        "falles —y fallarás, para eso está la semana—, aplica el protocolo de "
        "veinticuatro horas.",
        "Registra el fallo, no compenses, vuelve en la comida o el día siguiente.",
        "Anota cuánto tardaste en volver. Ese número, y no el de fallos, es la "
        "medida real de tu adherencia a doce meses vista.",
        "Compara la semana 4 con la 1. Lo que buscas no es menos fallos: es "
        "retornos más rápidos.",
    ),
    nota("Qué esperar del cuaderno",
         "No te va a hacer más disciplinado, porque la disciplina no es lo que "
         "está fallando. Lo que te va a dar es un suelo que aguanta, tres frases "
         "escritas para tus tres situaciones difíciles y la costumbre de volver "
         "en un día en vez de en un mes. Con eso, el plan que elijas —cualquiera "
         "razonable— empieza a tener efecto, que era el problema desde el "
         "principio."),
)

C11 = cap(
    "Lo que no se arregla con un plan",
    p("Cierre, y el límite más importante del libro entero. Hay cosas que "
      "parecen falta de disciplina y no lo son, y tratarlas como si lo fueran "
      "hace daño."),
    h("Cuándo esto deja de ser un tema de fitness"),
    lista(
        "Si comer se ha vuelto una fuente constante de culpa, si hay episodios de "
        "atracón, si hay conductas compensatorias —vómito, laxantes, ejercicio "
        "como castigo—, o si contar comida ocupa la cabeza casi todo el día, eso "
        "es un trastorno de la conducta alimentaria y no un problema de "
        "adherencia. Este libro no ayuda ahí y puede empeorarlo. Se busca ayuda "
        "profesional, y cuanto antes mejor: el pronóstico depende mucho de eso.",
        "Si no puedes parar de entrenar aunque estés lesionado o enfermo, si "
        "saltarte una sesión produce angustia intensa, o si el ejercicio ha "
        "desplazado el trabajo y las relaciones, eso tampoco es virtud. Es el "
        "mismo mecanismo con otro signo.",
        "Si la falta de energía y de ganas dura semanas y afecta a todo, no solo "
        "al gimnasio, la pregunta no es cómo motivarse: es si hay una depresión o "
        "un problema médico detrás. Un análisis y una consulta antes que un plan.",
        "Si el sueño es malo de forma persistente pese a hacer las cosas bien, "
        "hay causas médicas frecuentes y tratables: apnea, insomnio crónico, "
        "síndrome de piernas inquietas. Ninguna se arregla con disciplina y "
        "todas tienen tratamiento. Eso se consulta.",
    ),
    p("Digo esto en el libro de la mentalidad y no en otro sitio a propósito, "
      "porque es aquí donde la industria del fitness dice «solo te faltan ganas» "
      "y donde esa frase hace más daño. Ninguna de las cuatro situaciones de "
      "arriba se resuelve con un cuaderno, y todas se resuelven razonablemente "
      "bien con la ayuda adecuada."),
    sep(),
    h("Glosario"),
    ficha("", [
        ("Adherencia", "Grado en que se cumple lo planeado. La variable que "
                       "domina el resultado a largo plazo."),
        ("Autorregistro", "Anotar la propia conducta. Una de las estrategias de "
                          "cambio mencionadas por las guías oficiales."),
        ("Fricción", "Todo lo que hay entre la intención y la conducta. Se mide "
                     "en pasos y en segundos."),
        ("Objetivo de proceso", "Objetivo sobre lo que se hace, no sobre lo que "
                                "se consigue. Es el único que se controla."),
        ("Plan si-entonces", "Frase que ata una situación concreta a una conducta "
                             "concreta, decidida por adelantado."),
        ("Señal", "Lo que dispara una conducta. La palanca más barata del bucle."),
        ("Suelo", "Versión mínima innegociable del plan. Protege la conducta, no "
                  "el resultado."),
    ]),
    sep(),
    p("Y con esto se cierra el libro. No trae motivación, porque la motivación "
      "no se puede regalar en un libro. Trae lo otro: una rueda para saber por "
      "dónde empezar, un suelo que aguanta los días malos, frases escritas de "
      "antemano para las situaciones que te rompen el plan, un protocolo de "
      "veinticuatro horas para después de un fallo, y la idea —que es la más "
      "útil de todas— de que un fallo no significa nada hasta que decides que "
      "sí."),
    p("Si dentro de un año sigues teniendo un suelo definido y la costumbre de "
      "volver al día siguiente en vez de al lunes, este libro habrá hecho su "
      "trabajo. Todo lo demás es andamiaje para llegar a esas dos cosas."),
)



# ══════════════════════════════════════════════════════════════════════
#  CAPÍTULOS AÑADIDOS EN LA SEGUNDA EDICIÓN
# ══════════════════════════════════════════════════════════════════════

CE1 = cap(
    "Los cinco dominios",
    p("La doctrina pública de la que se nutre este libro no organiza la "
      "condición de una persona en «cuerpo y mente». La organiza en cinco "
      "dominios que se sostienen unos a otros, y la idea de fondo es la única "
      "que explica por qué tanta gente hace todo bien en uno y aun así no "
      "avanza."),
    fig("vo-dominios",
        "Los cinco dominios y lo que se rompe en cada uno",
        "La rueda no es un índice: es una herramienta de diagnóstico. La "
        "columna de abajo dice qué falla primero cuando ese dominio está bajo, y "
        "el dominio más bajo es siempre por donde hay que empezar. El quinto se "
        "nombra y no se desarrolla: no es asunto de un libro de fitness decirle "
        "a nadie qué le da sentido a su vida."),
    ficha("Los cinco, y qué se rompe cuando cada uno está bajo",
          [(nombre, f"{que}. Si está bajo: {cae[0].lower() + cae[1:]}")
           for nombre, que, cae in D.DOMINIOS]),
    h("La regla que hace útil el modelo"),
    p("Un dominio en mal estado limita a los demás, y lo hace de forma "
      "silenciosa. Quien duerme cinco horas no rinde en el gimnasio por mucho "
      "que su programa sea excelente. Quien come mal no recupera. Quien tiene la "
      "cabeza en otra parte no sostiene ningún hábito por bueno que sea el "
      "diseño. El eslabón que falla no se compensa apretando los otros: los "
      "arrastra."),
    p("De ahí sale el consejo de diagnóstico más útil de este libro: cuando algo "
      "no funciona, la pregunta correcta no es «¿cómo me esfuerzo más?» sino "
      "«¿cuál de los cinco está roto?». Nueve de cada diez veces es el sueño, y "
      "casi nadie lo mira primero."),
    sep(),
    h("El quinto dominio, y por qué no lo trato"),
    p("La doctrina original incluye un dominio de sentido, valores y propósito. "
      "Lo menciono porque omitirlo sin avisar sería contar mal la fuente, y no "
      "lo desarrollo porque no me corresponde. Un libro que te vende "
      "entrenamiento no tiene ninguna autoridad para decirte para qué vives, y "
      "la industria del fitness lleva años cruzando esa línea con resultados "
      "que van del ridículo al daño."),
    p("Lo único que diré es que la conexión existe y está en la doctrina: la "
      "gente sostiene mejor los hábitos que encajan con algo que le importa de "
      "verdad, y peor los que solo encajan con una imagen que quiere dar. Qué "
      "te importa de verdad es tuyo y no de este libro."),
    nota("Cómo usar esto de forma práctica",
         "Puntúate del uno al cinco en los cuatro primeros dominios, hoy, sin "
         "pensarlo mucho. El más bajo es donde está tu "
         "siguiente mes de trabajo, y casi nunca es el que estabas a punto de "
         "elegir."),
)

CE2 = cap(
    "Objetivos que sirven para algo",
    p("La fijación de objetivos figura en la doctrina pública de preparación "
      "mental y en el apartado de cambio de conducta de las guías de actividad "
      "física. También es lo que peor se hace: casi todos los objetivos que la "
      "gente se pone incumplen al menos dos de las condiciones que los harían "
      "útiles."),
    h("Los tres pisos"),
    ficha("Un objetivo tiene tres alturas y hacen falta las tres", [
        ("Resultado", "Adónde quieres llegar. Depende en parte de cosas que no "
                      "controlas y solo te contesta al final. Sirve para "
                      "orientar, no para puntuarte."),
        ("Rendimiento", "Una marca concreta y medible en algo que sí depende de "
                        "ti: un peso, un tiempo, un número de repeticiones. Es "
                        "el puente entre los otros dos."),
        ("Proceso", "Lo que vas a hacer esta semana. Lo controlas entero y te "
                    "contesta todos los días. Es el único por el que hay que "
                    "puntuarse."),
    ]),
    p("El error universal es tener solo el primero. «Quiero perder ocho kilos» "
      "no dice qué hacer el martes, no te felicita por hacerlo y encima te "
      "castiga por una cifra que oscila por motivos ajenos a tu conducta. Es un "
      "objetivo diseñado para desmoralizar a alguien que lo está haciendo bien."),
    sep(),
    h("Cómo se escribe uno de proceso"),
    pasos(
        "Conducta concreta, no intención. «Tres sesiones de fuerza» y no "
        "«entrenar más».",
        "Cantidad y plazo cortos. Semana, no trimestre. Un objetivo a tres meses "
        "no corrige nada hasta que ya es tarde.",
        "Ambición calibrada al peor escenario de la semana, no al mejor. Si "
        "solo se cumple cuando todo va bien, está mal dimensionado.",
        "Con un criterio de éxito binario. Al final de la semana la respuesta "
        "tiene que ser sí o no, sin interpretación.",
        "Escrito. Un objetivo que solo existe en la cabeza se renegocia solo, y "
        "siempre a la baja.",
    ),
    h("Y una cosa más, que es la que casi nadie hace"),
    p("Escribe también qué harás cuando NO se cumpla. No como castigo, sino como "
      "procedimiento: si esta semana salen dos de tres, ¿bajo el objetivo, lo "
      "mantengo, o cambio lo que estorbaba? Decidirlo por adelantado evita la "
      "conversación que de verdad hace daño, que es la que empieza con «entonces "
      "esto no es para mí»."),
    nota("La revisión mensual, en cuatro preguntas",
         "¿Qué se cumplió? ¿Qué no? ¿Qué situación concreta lo impidió más "
         "veces? ¿Qué UNA cosa cambio el mes que viene? Cuatro preguntas, diez "
         "minutos, una vez al mes. Es más de lo que hace el noventa por ciento "
         "de la gente que lleva años entrenando."),
)

CE3 = cap(
    "La activación y la respiración",
    p("El control de la activación es una de las habilidades que la doctrina "
      "pública describe como entrenables, y es la más inmediata de todas: se "
      "nota en el primer intento, a diferencia del resto de este libro."),
    h("Activación no es lo mismo que motivación"),
    p("La activación es cuánto está encendido el sistema: pulso, tensión "
      "muscular, velocidad del pensamiento. Hay un nivel demasiado bajo —apático, "
      "lento, sin chispa— y un nivel demasiado alto —acelerado, disperso, con "
      "la técnica rota— y entre los dos hay una franja donde se rinde mejor. La "
      "franja no es la misma para todo: una serie máxima de fuerza pide un nivel "
      "alto; una sesión técnica o una conversación difícil piden bastante menos."),
    ficha("Las dos direcciones", [
        ("Para subir", "Respiración corta y rápida, movimiento, música, "
                       "postura erguida, palmadas, frases de acción. Sirve para "
                       "la serie pesada y para el día sin ganas."),
        ("Para bajar", "Espiración larga, respiración lenta y contada, aflojar "
                       "mandíbula y hombros, foco en una sola cosa. Sirve antes "
                       "de dormir, después de una discusión y entre series de "
                       "una sesión que se ha desbocado."),
    ]),
    fig("vo-respiracion",
        "El compás cuadrado",
        "Cuatro tiempos iguales: inspirar, sostener, espirar, sostener. Lo que "
        "baja la activación es alargar la espiración y sostener sin tensión, no "
        "llenar mucho los pulmones."),
    p(D.RESPIRACION["nota"]),
    pasos(
        f"Inspira por la nariz contando {D.RESPIRACION['segundos']}.",
        f"Sostén {D.RESPIRACION['segundos']}, sin apretar.",
        f"Espira {D.RESPIRACION['segundos']}, despacio, como si soplaras una "
        "vela sin apagarla.",
        f"Sostén {D.RESPIRACION['segundos']} y vuelve a empezar. "
        f"{D.RESPIRACION['rondas'][0]} a {D.RESPIRACION['rondas'][1]} rondas "
        "bastan.",
    ),
    p("Si cuatro tiempos te resultan largos, empieza por tres. Si te marea, es "
      "que estás llenando demasiado: el objetivo no es respirar mucho, es "
      "respirar despacio y con un ritmo fijo."),
    sep(),
    h("Dónde usarlo de verdad"),
    lista(
        "En los últimos minutos antes de acostarte, que es donde más rinde y "
        "donde más se nota al día siguiente.",
        "Entre series, si la sesión se ha vuelto frenética y la técnica se está "
        "cayendo.",
        "Antes de una situación que sabes que te acelera: una prueba, una "
        "presentación, una conversación.",
        "Después de un fallo del plan, ANTES de decidir qué haces. El capítulo "
        "de la recaída dice que la decisión importante viene después del fallo; "
        "esta es la herramienta para tomarla con la cabeza fría.",
    ),
    nota("Lo que no es",
         "No es meditación, no cura la ansiedad y no sustituye a un tratamiento. "
         "Es una palanca fisiológica sencilla que baja la activación durante "
         "unos minutos. Si la ansiedad es persistente e interfiere con tu vida, "
         "eso es motivo de consulta y ninguna técnica de respiración lo resuelve."),
)

CE4 = cap(
    "Identidad, comparación y el ruido de fuera",
    p("Los capítulos anteriores tratan la mecánica. Este trata dos cosas que la "
      "rodean y que deciden más de lo que parece: cómo te describes a ti mismo y "
      "con quién te comparas."),
    h("La diferencia entre hacer y ser"),
    p("«Estoy intentando entrenar» y «soy de los que entrenan» describen la "
      "misma conducta y se comportan de forma distinta ante un fallo. La primera "
      "convierte cada sesión perdida en una prueba de que el intento no va bien. "
      "La segunda la convierte en una excepción de alguien que, en general, "
      "entrena."),
    p("Y esto no es autoengaño ni pensamiento positivo, porque la frase se gana "
      "con datos: dos meses de cuaderno con la mayoría de las casillas marcadas "
      "es la prueba. La secuencia correcta va de la conducta a la identidad y no "
      "al revés. Primero se acumulan pruebas pequeñas, después la descripción "
      "cambia sola, y a partir de ahí el mantenimiento cuesta mucho menos."),
    lista(
        "Empieza por conductas tan pequeñas que la prueba sea inmediata. El "
        "suelo del capítulo cuatro sirve exactamente para esto.",
        "Cuenta lo que haces en presente y sin adjetivos épicos: «entreno tres "
        "días» dice más y aguanta mejor que «estoy en una transformación».",
        "Cuando falles, describe el hecho y no la persona. «No fui el martes» es "
        "un dato; «no tengo constancia» es una profecía.",
    ),
    sep(),
    h("La comparación, que es el impuesto de esta época"),
    p("Compararse con otros es inevitable y no siempre es malo: alguien un poco "
      "por delante es una referencia útil. El problema es con quién se compara "
      "uno cuando la referencia la elige un algoritmo, porque lo que ve no es "
      "una muestra de gente: es una selección de los casos extremos, editada, "
      "con luz favorable y sin los años que hay detrás."),
    ficha("Tres correcciones que funcionan", [
        ("Compárate con tu registro", "El cuaderno del mes pasado es la única "
                                      "comparación con la que puedes hacer algo."),
        ("Ajusta lo que consumes", "Si una cuenta te deja peor cada vez que la "
                                   "ves, deja de verla. No es debilidad: es "
                                   "modificación del entorno, que es la "
                                   "estrategia mejor documentada de todo el "
                                   "libro."),
        ("Desconfía de los plazos", "Cualquier transformación con fecha oculta "
                                    "años previos, genética, circunstancias o "
                                    "directamente farmacología. El plazo es la "
                                    "parte que casi siempre miente."),
    ]),
    h("Y el ruido de cerca, que pesa más"),
    p("La familia, la pareja y el trabajo influyen bastante más que cualquier "
      "cuenta de internet, y no siempre a favor. Hay entornos donde comer de una "
      "manera concreta o irse a entrenar genera fricción real, y fingir que eso "
      "se resuelve con voluntad es no haber vivido en ninguno."),
    p("Lo que sí funciona es tratarlo como lo que es —una situación previsible— "
      "y escribirle su si-entonces: qué haces exactamente en la cena familiar, "
      "en la comida de empresa, en el fin de semana en casa de tus padres. "
      "Decidido de antemano, en frío, y sin convertirlo en un asunto moral con "
      "nadie."),
    nota("Un límite honesto",
         "Si el entorno no es solo poco favorable sino activamente hostil —si "
         "hay control, burla sistemática o presión sobre lo que comes o sobre tu "
         "cuerpo— eso ya no es un problema de adherencia y este libro no es la "
         "herramienta. Es una conversación distinta, y a veces es una "
         "conversación con un profesional."),
)

CE5 = cap(
    "Volver después de meses",
    p("Todos los capítulos anteriores tratan de sostener algo. Este trata de la "
      "otra situación, que es más frecuente: llevas meses o años sin hacer nada "
      "y quieres volver. Merece su propio capítulo porque las reglas son "
      "distintas y porque casi todo el mundo lo hace igual de mal."),
    h("Los tres errores del regreso"),
    ficha("", [
        ("Empezar donde lo dejaste", "La memoria guarda el mejor momento, no el "
                                     "promedio. Volver al peso o al ritmo de "
                                     "entonces es la vía rápida a la lesión de "
                                     "la segunda semana, porque el músculo "
                                     "recupera antes que el tendón."),
        ("Empezar con todo a la vez", "Dieta, gimnasio, sueño, suplementos y "
                                      "aplicación nueva el mismo lunes. Cinco "
                                      "cambios simultáneos es cero cambios "
                                      "sostenidos, y además impide saber cuál "
                                      "funcionaba."),
        ("Empezar por castigo", "Volver como penitencia por los meses perdidos "
                                "garantiza que la actividad quede asociada a "
                                "una emoción que nadie repite voluntariamente."),
    ]),
    h("El protocolo de las cuatro semanas"),
    pasos(
        "Semana 1: solo aparecer. Dos sesiones muy fáciles, la mitad de lo que "
        "crees que puedes. El objetivo es que existan, no que sirvan.",
        "Semana 2: las mismas dos sesiones, un escalón más. Añade una sola cosa "
        "de comida, la más fácil de todas.",
        "Semana 3: tres sesiones si las dos anteriores salieron. Si no salieron, "
        "repite la semana 2 sin dramatismo: el plan era demasiado grande y ahora "
        "lo sabes.",
        "Semana 4: mide algo. Un peso, un tiempo, una prueba de la batería "
        "sencilla: flexiones máximas, plancha en segundos o distancia en doce "
        "minutos. Ese número es tu punto de partida real, "
        "y a partir de aquí ya estás entrenando y no volviendo.",
    ),
    p("Cuatro semanas parecen pocas para un regreso de dos años y son "
      "exactamente las que hacen falta: lo que se está construyendo no es "
      "condición física, es la costumbre de aparecer. La condición viene después "
      "y viene sola si la costumbre aguanta."),
    sep(),
    h("Lo que juega a tu favor y casi nadie te cuenta"),
    p("Recuperar es más rápido que construir por primera vez. Quien tuvo masa "
      "muscular la recupera antes que quien nunca la tuvo, y esto se observa de "
      "forma bastante consistente. Los primeros dos meses de un regreso suelen "
      "ser sorprendentemente buenos, y conviene saberlo por dos razones: para "
      "empezar con menos pereza, y para no confundir esa velocidad inicial con "
      "el ritmo normal y frustrarse cuando se estabilice."),
    nota("Si el parón fue por una lesión o una enfermedad",
         "Entonces el escalón lo marca quien te trató y no este libro. El "
         "protocolo de arriba sirve para un parón por vida ocupada, no para una "
         "vuelta tras una cirugía, un episodio cardíaco, un embarazo o una "
         "enfermedad prolongada. En esos casos la primera sesión es una "
         "consulta."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-voluntad",
    "titulo": "Códice de la Voluntad",
    "subtitulo": "Adherencia, hábito y regreso: por qué los planes buenos se caen y cómo se construye uno que sobreviva a los días malos",
    "autor": "Villuminations",
    "fuente": "Obra original · Primera edición, 2026",
    # Sobre qué material común se apoya ESTE libro y cómo debe leerse.
    # Va por libro y no en la plantilla: cuando estaba en la plantilla,
    # los libros de fitness citaban en sus créditos los decanatos.
    "base": """El material del que parte pertenece al <strong>dominio público</strong>:
     los manuales de instrucción física y de preparación mental publicados por
     el Gobierno de los Estados Unidos —entre ellos el FM 7-22 del Ejército—
     no están sujetos a derechos de autor conforme al 17 U.S.C. § 105. Lo que
     aquí se ofrece —la redacción, la estructura en cinco partes, los
     ejercicios de registro, las tablas y las ilustraciones— es trabajo propio
     y está protegido como tal.""",
    "lectura": """<strong>Cómo leer este libro.</strong> Es un libro sobre
     <em>adherencia</em>: sobre por qué un plan correcto se abandona y qué se
     puede construir para que sobreviva a los días malos. No es un tratado de
     psicología clínica. Nada de lo que sigue diagnostica ni trata un trastorno
     de la conducta alimentaria, una depresión ni una adicción, y no sustituye
     la atención de un profesional sanitario colegiado. Si te reconoces en algo
     de eso, ese es el primer paso, no este libro.""",
    "mascota": "r-voluntad",
    "acento": "fuerza",
    "original": True,
    "laminas": ["voluntad.svg"],
    "claves": ["adherencia", "hábito", "mentalidad fitness", "recaída",
               "preparación mental", "FM 7-22", "cambio de conducta",
               "villuminations"],
    "capitulos": [
        C1, CE1, C2,               # I · La variable que manda
        C3, C4, C5,                # II · La mecánica
        C6, CE2, CE3, C7,          # III · La doctrina
        C8, CE4, CE5,              # IV · El entorno y el regreso
        C9, C10, C11,              # V · El oficio
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
          f"{palabras:,} palabras · fuentes oficiales y no oficiales separadas · "
          f"→ {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
