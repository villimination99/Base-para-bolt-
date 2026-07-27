#!/usr/bin/env python3
"""
CÓDICE DE LAS INVOCACIONES — obra original de VILLUMINATION 99
==============================================================
Redacción propia sobre material de dominio público y de tradición común: el
«Dogma y ritual de la alta magia» de Éliphas Lévi (1856), la «Clavícula de
Salomón» en sus traducciones antiguas, las tablas de correspondencias
renacentistas y la práctica ritual que la Golden Dawn puso por escrito a
finales del XIX. Nada de esto es propiedad de nadie; el desarrollo, la
estructura, las prácticas y el encuadre sí son de esta casa.

    python3 tools/escribir-codice-invocaciones.py && python3 build.py invoca
"""

import json
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"


# ── Atajos de escritura ───────────────────────────────────────────────
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
#  PARTE I · ANTES DE EMPEZAR
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "Lo que este libro es",
    p("Este es un manual de práctica ritual. Conviene decir en la primera "
      "página, y sin rodeos, en qué marco se ofrece — porque el material que "
      "sigue se ha presentado durante siglos envuelto en promesas que no puede "
      "cumplir, y ese envoltorio ha hecho más daño que bien."),
    h("La afirmación de este libro"),
    p("El rito es una tecnología de la atención. Un conjunto de gestos, palabras "
      "y objetos ordenados en una secuencia fija, repetidos con regularidad, que "
      "produce en quien los ejecuta un estado mental distinto del ordinario: más "
      "concentrado, más deliberado, más presente. Ese efecto es real, es "
      "reproducible y no necesita ninguna explicación sobrenatural. Es el mismo "
      "mecanismo por el que un músico afina antes de tocar y un cirujano se lava "
      "las manos en un orden invariable: la secuencia prepara al operante."),
    h("Lo que este libro no afirma"),
    lista(
        "No afirma que los ritos produzcan efectos físicos en el mundo exterior. "
        "Nada de lo que aquí se describe mueve objetos, cura enfermedades, "
        "modifica el comportamiento de terceros ni altera acontecimientos.",
        "No afirma la existencia de entidades independientes de quien las "
        "invoca. Cuando en estas páginas se habla de «los cuatro custodios» o de "
        "«el nombre», se habla de estructuras de la propia mente que el rito "
        "personifica para poder trabajarlas — y se dirá así cada vez.",
        "No sustituye tratamiento médico ni psicológico de ninguna clase. Si "
        "atraviesas una crisis, tomas medicación psiquiátrica o tienes "
        "antecedentes de episodios disociativos, la práctica intensiva de "
        "visualización y de privación sensorial no es para ti sin supervisión "
        "profesional. Esto no es una cláusula de estilo: va en serio.",
        "No pide fe. Puedes ejecutar todo lo que sigue considerándolo teatro "
        "deliberado y obtendrás el mismo resultado. La eficacia del rito no "
        "depende de que creas en su cosmología.",
    ),
    nota("Por qué entonces conservar el lenguaje antiguo",
         "Porque funciona mejor. Se podría reescribir todo esto en vocabulario "
         "de psicología cognitiva y quedaría más respetable y menos eficaz. Las "
         "imágenes tradicionales —el círculo, el arma, el nombre, el custodio del "
         "este— están construidas para ser memorables y para movilizar atención, "
         "y llevan siglos afinándose para eso. Se conservan porque son buenas "
         "herramientas, no porque se les atribuya poder propio."),
    sep(),
    h("De dónde sale el material"),
    p("Todo lo que este libro desarrolla proviene de fuentes de dominio público o "
      "de tradición común, y se dirá siempre cuál. El «Dogma y ritual de la alta "
      "magia» que Éliphas Lévi publicó en 1856 es la fuente moderna principal: "
      "está en dominio público desde hace mucho y su autor lleva muerto desde "
      "1875. La «Clavícula de Salomón», compilada a lo largo de la Edad Media y "
      "el Renacimiento, no tiene autor conocido y circula en traducciones "
      "antiguas también libres. Las tablas de correspondencias planetarias —día, "
      "metal, color, hora— son patrimonio compartido de la astrología y la "
      "alquimia europeas. Los cuadrados numéricos son aritmética, y la aritmética "
      "no es de nadie."),
    p("Lo que aquí es propio: la redacción entera, la estructura del libro, el "
      "orden de las operaciones, las fórmulas en castellano, el encuadre "
      "psicológico, las seis láminas dibujadas para esta edición y los ejercicios "
      "de registro. No se reproduce texto de ningún autor moderno."),
    h("Cómo leerlo"),
    pasos(
        "Lee la primera parte entera antes de ejecutar nada. Son tres capítulos y "
        "te ahorran los errores que se cometen por impaciencia.",
        "Estudia la segunda parte con las láminas delante. Los instrumentos hay "
        "que entenderlos antes de usarlos.",
        "Ejecuta la tercera parte en orden. El rito menor del pentagrama antes "
        "que cualquier otra cosa, durante un mes, todos los días. Sin esa base, "
        "el resto es coleccionismo.",
        "Lleva el diario desde el primer día. Es la parte que separa una práctica "
        "de un pasatiempo.",
    ),
)

C2 = cap(
    "La tradición de la que viene",
    p("Merece la pena saber de dónde sale lo que uno hace, aunque solo sea para "
      "no atribuirle una antigüedad que no tiene. La historia de este material es "
      "más corta y mucho más interesante de lo que suele contarse."),
    h("Los grimorios: entre el siglo XIV y el XVII"),
    p("Los manuales de operación ritual que hoy llamamos grimorios se compilan en "
      "Europa entre finales de la Edad Media y el Barroco. La «Clavícula de "
      "Salomón» es el más influyente: un cuerpo de textos de autoría desconocida "
      "atribuido por convención al rey Salomón, que describe círculos, "
      "pentáculos, nombres y horarios con una minuciosidad de manual técnico. No "
      "es un libro antiguo pese a lo que dice de sí mismo, y esa es su primera "
      "lección: la tradición mágica se legitima siempre inventándose una "
      "genealogía. Conviene saberlo y seguir leyendo."),
    p("Junto a ella circulan la «Filosofía oculta» de Agrippa (1533), que ordena "
      "las correspondencias en tablas por primera vez de forma sistemática, y "
      "docenas de manuscritos menores que se copian, se mezclan y se contradicen "
      "entre sí sin ningún pudor."),
    h("Lévi, 1856: el momento en que todo se reordena"),
    p("Alphonse Louis Constant, sacerdote francés que firmaba como Éliphas Lévi, "
      "publica en 1856 el «Dogma y ritual de la alta magia» y cambia el asunto "
      "por completo. Lo que hace es doble y las dos cosas importan."),
    lista(
        "Sintetiza. Toma el material disperso de los grimorios y lo ordena en un "
        "sistema coherente, cruzando la cábala, el tarot y las correspondencias "
        "planetarias en una sola arquitectura.",
        "Interioriza. Y esto es lo decisivo: Lévi es el primero en escribir con "
        "claridad que las operaciones no actúan sobre el mundo sino sobre el "
        "operante. Su magia es una disciplina de la voluntad y de la imaginación. "
        "Todo lo que este libro afirma en su primer capítulo está ya en él, con "
        "otro vocabulario.",
    ),
    nota("La frase que conviene recordar",
         "Lévi insistía en que el instrumento de la operación es el propio "
         "operante y que sin trabajo sobre uno mismo el aparato ritual es "
         "mobiliario. Siglo y medio después sigue siendo el mejor resumen "
         "posible de para qué sirve todo esto — y el mejor filtro para "
         "distinguir un maestro de un vendedor."),
    h("La Golden Dawn: el rito se vuelve método"),
    p("A finales del siglo XIX, un grupo de ocultistas británicos toma el sistema "
      "de Lévi y lo convierte en un plan de estudios: grados, exámenes, rituales "
      "escritos con precisión de partitura y una insistencia nueva en la práctica "
      "diaria. De esa cocina salen los ritos menores del pentagrama y del "
      "hexagrama tal como hoy se ejecutan en casi todo el mundo. Duró poco y "
      "acabó, como suele, en cisma; pero fijó la forma."),
    p("Casi todo lo que se publica hoy sobre práctica ritual occidental desciende "
      "de esa línea: grimorios medievales, síntesis de Lévi, método de la Golden "
      "Dawn. Este libro también, y lo dice."),
    h("Lo que se hereda y lo que se descarta"),
    ficha("Balance honesto de la herencia", [
        ("Se conserva", "La estructura ritual: círculo, cuartos, armas, nombres, "
                        "apertura y cierre. Es un armazón de atención "
                        "extraordinariamente bien diseñado."),
        ("Se conserva", "Las correspondencias planetarias como sistema "
                        "mnemotécnico. Ordenan la semana y dan a cada operación "
                        "un contexto reconocible."),
        ("Se conserva", "La exigencia de registro escrito. La Golden Dawn "
                        "obligaba al diario, y en eso tenía toda la razón."),
        ("Se descarta", "La jerarquía iniciática y los grados secretos. Producen "
                        "dependencia y no producen práctica."),
        ("Se descarta", "Toda afirmación sobre efectos físicos, curaciones o "
                        "influencia sobre terceros. No hay evidencia y el daño "
                        "potencial es real."),
        ("Se descarta", "El secretismo. Nada de lo que hay en este libro necesita "
                        "estar oculto; solo necesita estar bien explicado."),
    ]),
)

C3 = cap(
    "El vocabulario del oficio",
    p("Los términos que van a aparecer, definidos antes de usarlos. Es un "
      "capítulo para volver a él."),
    ficha("A – E", [
        ("Arma", "Cada uno de los cuatro objetos rituales: vara, copa, espada y "
                 "disco. Representan las cuatro funciones del operante, no cuatro "
                 "poderes."),
        ("Banir · despedir", "Cerrar una operación deshaciendo lo que se abrió. "
                             "Tan obligatorio como abrir, y mucho más olvidado."),
        ("Círculo", "El espacio delimitado de la operación. No protege de nada "
                    "exterior: delimita la atención del operante. Es la pieza más "
                    "malinterpretada de todo el sistema."),
        ("Correspondencia", "Vínculo simbólico entre un planeta, un metal, un "
                            "color, un día y una función. Sistema de "
                            "clasificación, no de causalidad."),
        ("Cuarto", "Cada uno de los cuatro puntos cardinales del círculo, con su "
                   "elemento y su custodio."),
        ("Custodio", "La figura que se sitúa en cada cuarto. En este libro se "
                     "entiende siempre como personificación de una función "
                     "propia: cuerpo, aliento, voluntad, memoria."),
    ]),
    ficha("F – P", [
        ("Hexagrama", "Estrella de seis puntas formada por dos triángulos. Se "
                      "usa para el trabajo con los siete planetas."),
        ("Hora planetaria", "División desigual del día: doce partes de amanecer a "
                            "atardecer y doce de atardecer a amanecer, cada una "
                            "con su regente."),
        ("Kamea", "Cuadrado numérico asociado a un planeta. Cada fila, columna y "
                  "diagonal suman lo mismo. Es aritmética y sirve como soporte "
                  "de concentración."),
        ("Nombre", "Fórmula vocalizada que se sostiene en una sola exhalación. Su "
                   "efecto es respiratorio y atencional, y así se explica aquí."),
        ("Pentagrama", "Estrella de cinco puntas: cuatro elementos y el vértice "
                       "superior. Se traza en dos direcciones, una para abrir y "
                       "otra para cerrar."),
        ("Pentáculo", "Disco o lámina con un dibujo trazado sobre él. En este "
                      "libro, el arma de Tierra."),
    ]),
    ficha("Q – Z", [
        ("Sefirá", "Cada uno de los diez números del árbol. Plural: sefirot. "
                   "Diez estaciones de un mismo recorrido, de la abstracción al "
                   "cuerpo."),
        ("Sendero", "Cada una de las veintidós líneas que unen dos sefirot."),
        ("Sigilo", "Trazo abreviado que designa un planeta o una idea. Los siete "
                   "planetarios se usan en todo este libro."),
        ("Templo", "El sitio donde se opera, sea una habitación entera o un metro "
                   "cuadrado de suelo despejado."),
        ("Triángulo", "Figura situada FUERA del círculo. En este libro es el "
                      "lugar donde se pone lo que se quiere examinar sin "
                      "identificarse con ello."),
        ("Vibrar", "Sostener una vocalización en el pecho hasta agotar el aire. "
                   "Técnica respiratoria, descrita como tal en el capítulo 10."),
    ]),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LOS INSTRUMENTOS
# ══════════════════════════════════════════════════════════════════════

C4 = cap(
    "El círculo y los cuatro cuartos",
    p("El círculo es la primera pieza y la peor entendida. La imagen popular —el "
      "operante encerrado en un trazo de tiza para que no lo alcance lo que ha "
      "llamado— es literatura del siglo XIX y no resiste dos minutos de examen. "
      "Si nada exterior acude, no hay de qué protegerse."),
    p("Lo que el círculo hace es otra cosa, y es mucho más útil: establece un "
      "dentro y un fuera. Mientras estás dentro, esto es lo que haces; cuando "
      "sales, has terminado. Un límite físico convierte una intención difusa en "
      "un acto con principio y final, y esa conversión es la mitad del trabajo."),
    fig("am-circulo", "Lám. 1",
        "El círculo con sus cuatro cuartos, cada uno con su elemento, su función "
        "y su hora. En el centro, el operante. A la derecha, fuera del trazo, el "
        "triángulo de examen."),
    h("Los cuatro cuartos"),
    p("Cada punto cardinal lleva asignado un elemento, y cada elemento nombra una "
      "función del operante. La correspondencia es tradicional y se ha mantenido "
      "notablemente estable desde el Renacimiento."),
    ficha("Los cuatro cuartos y lo que nombran", [
        ("Este · Aire", "El aliento. La respiración, la palabra, el pensamiento "
                        "que se articula. Hora: el amanecer."),
        ("Sur · Fuego", "La voluntad. Lo que se decide y se sostiene. Hora: el "
                        "mediodía."),
        ("Oeste · Agua", "La memoria. Lo que se siente y lo que se recuerda. "
                         "Hora: el atardecer."),
        ("Norte · Tierra", "El cuerpo. Lo que pesa, lo que se cansa, lo que "
                           "sostiene todo lo demás. Hora: la medianoche."),
    ]),
    p("El recorrido de los cuatro cuartos en una operación no es decorativo: es un "
      "inventario. Se pasa por el aliento, por la voluntad, por la memoria y por "
      "el cuerpo, y en cada parada se comprueba en qué estado están. Hecho con "
      "atención, el simple recorrido ya cambia el estado de partida."),
    h("El triángulo, y por qué va fuera"),
    p("Los grimorios sitúan siempre el triángulo fuera del círculo: lo que se "
      "convoca se pone ahí, a la vista y a distancia. Leído en clave "
      "psicológica, el gesto es de una precisión notable. Poner algo fuera del "
      "círculo es mirarlo sin ser eso: nombrar un miedo, una obsesión o una "
      "cólera, colocarla enfrente y examinarla desde una posición que no es la "
      "suya. Es exactamente lo contrario de identificarse."),
    nota("La regla del triángulo",
         "Nunca se examina algo estando dentro de ello. Si al poner un asunto en "
         "el triángulo notas que sigues dentro del asunto —que se te acelera el "
         "pulso, que empiezas a discutir mentalmente—, la operación de ese día ha "
         "terminado: cierra y vuelve mañana. Forzarlo no produce lucidez, produce "
         "agitación."),
    h("Cómo se traza en la práctica"),
    pasos(
        "Despeja un espacio en el que puedas girar con los brazos extendidos sin "
        "tocar nada. Metro y medio de diámetro es suficiente.",
        "Sitúa el este. Si no sabes dónde está, cualquier brújula de teléfono "
        "sirve; y si te da igual, decide uno y no lo cambies nunca.",
        "Marca los cuatro cuartos con algo mínimo y estable: cuatro objetos, "
        "cuatro velas, cuatro señales en el suelo. Lo importante no es el "
        "material: es que siempre estén en el mismo sitio.",
        "Traza el círculo caminándolo. Una vuelta completa en el sentido de las "
        "agujas del reloj, empezando y acabando en el este, con la mano derecha "
        "extendida hacia el borde.",
        "Al terminar la operación, deshaz el círculo caminándolo en sentido "
        "contrario. El espacio vuelve a ser una habitación.",
    ),
)

C5 = cap(
    "Las cuatro armas",
    p("Cuatro objetos, uno por elemento. La tradición los rodea de "
      "prescripciones sobre maderas, metales y fases lunares que se pueden "
      "atender o no; lo que no es opcional es que cada uno esté asociado a una "
      "función y que el operante sepa cuál."),
    fig("am-armas", "Lám. 2",
        "Las cuatro armas con su elemento y la función que nombran. El dibujo es "
        "esquemático a propósito: lo que importa es la asociación, no el modelo."),
    ficha("Las cuatro y lo que sostienen", [
        ("La vara · Fuego", "La voluntad. Se empuña para decidir y para dirigir. "
                            "Se usa apuntando."),
        ("La copa · Agua", "El sentimiento. Se sostiene con las dos manos y se "
                           "usa recibiendo, no dirigiendo."),
        ("La espada · Aire", "El pensamiento. Corta, distingue, separa lo que "
                             "estaba mezclado. Es el arma del análisis."),
        ("El disco · Tierra", "El cuerpo y lo concreto. Se apoya, no se levanta. "
                              "Es el arma del resultado."),
    ]),
    h("Qué usar de verdad"),
    p("Nada de esto exige compras. Una rama recta y lisa es una vara "
      "perfectamente digna; un vaso liso que no se use para nada más es una copa; "
      "un abrecartas o incluso una regla metálica hacen de espada; un disco de "
      "madera, una piedra plana o una baldosa sirven de pentáculo. Lo que hace "
      "que un objeto funcione como arma no es su precio: es que esté dedicado "
      "exclusivamente a esto y que siempre esté en el mismo sitio."),
    nota("La única regla que importa",
         "Un objeto ritual que se usa también para otra cosa deja de ser un "
         "objeto ritual. Ese es todo el secreto de la consagración, y el capítulo "
         "14 no dirá nada más profundo que esto: la dedicación exclusiva es lo "
         "que carga un objeto de significado, porque cada vez que lo tomas tu "
         "cabeza sabe para qué es."),
    h("El orden de las cuatro"),
    p("Las armas se toman siempre en el mismo orden y ese orden es un mapa. "
      "Espada, vara, copa, disco: pensar, querer, sentir, hacer. O en el orden "
      "inverso, cuando el trabajo va de lo concreto a lo abstracto. Lo que no se "
      "hace nunca es tomarlas al azar: la secuencia es parte de la información."),
    h("El error de las armas"),
    p("Hay una trampa muy frecuente y muy cara en tiempo: confundir el equipo con "
      "la práctica. Es enormemente cómodo dedicar meses a fabricar instrumentos "
      "hermosos, porque fabricar es agradable y practicar es aburrido. El operante "
      "con cuatro armas magníficas y tres semanas de diario no ha empezado. El "
      "operante con una rama, un vaso y ocho meses de registro diario sí."),
)

C6 = cap(
    "El pentagrama: las dos direcciones",
    p("La estrella de cinco puntas es la figura central de la práctica occidental "
      "moderna, y su interés está entero en un detalle que casi nunca se explica "
      "bien: se traza de un solo movimiento, y el orden en que se recorren las "
      "cinco puntas cambia lo que la figura hace."),
    fig("am-pentagrama", "Lám. 3",
        "Las dos direcciones del trazo. El punto marca dónde se empieza y la "
        "flecha, hacia dónde va el primer movimiento. La figura resultante es la "
        "misma; el recorrido no."),
    h("Las cinco puntas"),
    p("Cuatro puntas son los cuatro elementos y la quinta —la superior— es lo que "
      "la tradición llama espíritu y este libro llama, con menos poesía y más "
      "precisión, la atención que observa a las otras cuatro. Cuerpo, aliento, "
      "voluntad y memoria abajo y a los lados; arriba, quien las mira."),
    ficha("Atribución de las puntas", [
        ("Superior", "Espíritu · la atención que observa"),
        ("Superior izquierda", "Aire · el aliento y el pensamiento"),
        ("Superior derecha", "Agua · la memoria y el sentimiento"),
        ("Inferior izquierda", "Tierra · el cuerpo"),
        ("Inferior derecha", "Fuego · la voluntad"),
    ]),
    h("Invocar: de Tierra a Espíritu"),
    p("El trazo de apertura empieza en la punta inferior izquierda —Tierra, el "
      "cuerpo— y sube hacia el vértice superior. El gesto dice algo muy concreto: "
      "se parte de donde uno está, que es un cuerpo en una habitación, y se sube "
      "desde ahí. Cualquier práctica que empiece por arriba se está saltando el "
      "único punto de partida disponible."),
    h("Despedir: de Espíritu a Tierra"),
    p("El trazo de cierre invierte el primer movimiento: baja del vértice "
      "superior a Tierra. Se vuelve al cuerpo y a la habitación. Es el gesto de "
      "terminar, y es el que más se omite y el que más falta hace: sin cierre, la "
      "operación no acaba, se disuelve — y lo que se disuelve deja residuo."),
    nota("Por qué el cierre no es opcional",
         "Una sesión de concentración intensa que termina sin transición deja al "
         "operante en un estado intermedio: absorto, algo irritable, con la "
         "sensación de no estar del todo en lo que hace. Cualquiera que haya "
         "salido de golpe de cuatro horas de trabajo profundo lo reconoce. El "
         "rito de cierre es un procedimiento de aterrizaje, y funciona por la "
         "misma razón por la que un corredor no se para en seco."),
    h("El trazo, paso a paso"),
    pasos(
        "De pie, mirando al cuarto que toque. Brazo derecho extendido, dedos "
        "índice y medio juntos, el resto recogido. O el arma que corresponda.",
        "Sitúa mentalmente los cinco vértices en un cuadro imaginario del tamaño "
        "de tu propio cuerpo: la punta superior a la altura de la frente, las "
        "inferiores a la de las caderas.",
        "Empieza en la cadera izquierda y sube a la frente. Ese es el primer "
        "trazo y el que marca la dirección de todo lo demás.",
        "Continúa: frente → cadera derecha → hombro izquierdo → hombro derecho → "
        "cadera izquierda. Cinco trazos, sin levantar la mano.",
        "Cierra el circuito volviendo al punto de partida y detén ahí la mano un "
        "instante antes de bajarla. La figura queda cerrada; un pentagrama a "
        "medio trazar no vale.",
    ),
    nota("Sobre la visualización",
         "Se recomienda ver la figura trazada en luz. Si no la ves —y mucha gente "
         "no visualiza, es una variación normal y no un defecto—, basta con "
         "sostener la intención y ejecutar el gesto con precisión. La eficacia "
         "está en la secuencia motora y en la atención sostenida, no en la "
         "calidad de la imagen mental."),
)

C7 = cap(
    "El hexagrama y los siete",
    p("Donde el pentagrama ordena los cuatro elementos, el hexagrama ordena los "
      "siete planetas. Es la figura del trabajo con las funciones más generales: "
      "el límite, la expansión, el empuje, la identidad, el vínculo, la palabra y "
      "el ritmo."),
    fig("am-hexagrama", "Lám. 4",
        "Los seis planetas en las puntas y el Sol en el centro. Los dos "
        "triángulos entrelazados son la misma figura vista dos veces: lo que "
        "asciende y lo que desciende."),
    h("Por qué seis fuera y uno dentro"),
    p("Los siete cuerpos clásicos no caben en una figura de seis puntas, y esa "
      "aparente torpeza es en realidad la mejor parte del diseño. El Sol va al "
      "centro porque no es una función más: es el punto de referencia respecto "
      "del cual las otras seis se ordenan. En el vocabulario de este libro, el "
      "centro es la identidad del operante y las seis puntas son las funciones "
      "que orbitan alrededor de ella."),
    ficha("Los siete y lo que nombran", [
        ("Saturno", "El límite. Lo que se acaba, lo que se estructura, lo que "
                    "dice no. Plomo. Sábado."),
        ("Júpiter", "La expansión. Lo que crece, lo que se abre, lo que se "
                    "concede. Estaño. Jueves."),
        ("Marte", "El empuje. Lo que corta, lo que insiste, lo que se defiende. "
                  "Hierro. Martes."),
        ("Sol", "La identidad. El centro, la vitalidad, lo que se reconoce como "
                "propio. Oro. Domingo."),
        ("Venus", "El vínculo. Lo que atrae, lo que valora, lo que reconcilia. "
                  "Cobre. Viernes."),
        ("Mercurio", "La palabra. Lo que se dice, se ordena y se traduce. "
                     "Azogue. Miércoles."),
        ("Luna", "El ritmo. Lo que fluctúa, lo que recuerda, lo que se repite. "
                 "Plata. Lunes."),
    ]),
    h("Los dos triángulos"),
    p("El triángulo con la punta arriba y el que la tiene abajo se leen "
      "tradicionalmente como lo que sube y lo que baja: la aspiración y la "
      "manifestación, el fuego y el agua, lo que uno quiere y lo que uno hace. "
      "Que estén entrelazados y no simplemente superpuestos es la parte "
      "importante del dibujo: no se elige entre los dos."),
    nota("Cuándo se usa el hexagrama",
         "Después del pentagrama, nunca antes. El pentagrama pone en orden los "
         "cuatro elementos del operante; el hexagrama trabaja funciones más "
         "generales sobre esa base ya ordenada. Hacerlo al revés es como afinar "
         "después del concierto: se puede, y no sirve para nada."),
)

C8 = cap(
    "El árbol de los diez números",
    p("La cábala aporta al sistema occidental su columna vertebral: un diagrama "
      "de diez estaciones y veintidós caminos que organiza todo lo demás. Lo que "
      "sigue es una presentación práctica, no teológica, y se limita a lo que "
      "sirve para operar."),
    fig("am-arbol", "Lám. 5",
        "El árbol: diez números repartidos en tres columnas y unidos por "
        "veintidós senderos. A la izquierda el rigor, a la derecha la clemencia, "
        "en el centro el equilibrio."),
    h("Diez estaciones de lo abstracto a lo concreto"),
    p("Leído de arriba abajo, el árbol describe un descenso: de lo indeterminado "
      "a lo determinado, de la idea al objeto, del impulso al hecho. Leído de "
      "abajo arriba describe el camino inverso, que es el que recorre el "
      "operante. Ambos sentidos importan y el diagrama sirve para los dos."),
    ficha("Los diez números", [
        ("1 · Kéter", "La corona. El impulso antes de tener forma."),
        ("2 · Jojmá", "La sabiduría. La chispa que aún no se ha delimitado."),
        ("3 · Biná", "La inteligencia. La forma que delimita la chispa."),
        ("4 · Jésed", "La clemencia. Lo que se da y se expande."),
        ("5 · Guevurá", "El rigor. Lo que se recorta y se pone en su sitio."),
        ("6 · Tiféret", "La belleza. El equilibrio de los dos anteriores; el "
                        "centro del árbol y el lugar del operante consciente."),
        ("7 · Nétsaj", "La victoria. Lo que persiste, el impulso sostenido."),
        ("8 · Hod", "La gloria. La forma acabada, el detalle, el estilo."),
        ("9 · Yesod", "El fundamento. Donde todo lo anterior se reúne antes de "
                      "concretarse. La imaginación."),
        ("10 · Maljut", "El reino. El cuerpo, el hecho, el mundo. Donde una "
                        "operación se comprueba o no se comprueba."),
    ]),
    h("Las tres columnas"),
    p("La columna de la derecha expande, la de la izquierda limita y la del "
      "centro equilibra. Es la misma estructura que aparece en el pentagrama "
      "—voluntad frente a memoria, con la atención arriba— y en el hexagrama "
      "—Júpiter frente a Saturno, con el Sol en medio—. El sistema repite su "
      "figura básica en todas las escalas, y esa coherencia es lo que lo hace "
      "utilizable."),
    nota("Cómo usar el árbol sin estudiar cábala diez años",
         "Para operar basta con una cosa: saber que toda operación empieza en "
         "Maljut, el cuerpo y la habitación, y que si el resultado no vuelve a "
         "Maljut la operación no ha ocurrido. Es la mejor defensa contra la "
         "espiritualidad de salón. Si algo cambió, se nota en la vida concreta; "
         "si no se nota en ninguna parte, no cambió."),
    h("Los veintidós senderos"),
    p("Las veintidós líneas que unen los números llevan atribuidas "
      "tradicionalmente las veintidós letras del alfabeto hebreo y los "
      "veintidós arcanos mayores del tarot. Es un sistema de correspondencias "
      "vasto y bello, y queda fuera de este libro por una razón práctica: no hace "
      "falta para nada de lo que aquí se propone, y meterlo sin desarrollarlo "
      "sería decoración. Si sigues por tu cuenta, ese es el paso siguiente."),
)

C9 = cap(
    "Los cuadrados planetarios",
    p("Cada planeta lleva asociado un cuadrado de números en el que todas las "
      "filas, todas las columnas y las dos diagonales suman exactamente lo mismo. "
      "Son los kameas, aparecen en Agrippa y en los grimorios posteriores, y "
      "tienen la particularidad de ser la única pieza de este libro que se puede "
      "verificar con un lápiz."),
    fig("am-kameas", "Lám. 6",
        "Los cuatro primeros cuadrados: Saturno de tres, Júpiter de cuatro, "
        "Marte de cinco y el Sol de seis. Cada uno con su suma constante. Los de "
        "Venus, Mercurio y la Luna siguen la misma lógica en siete, ocho y nueve.",
        "media"),
    ficha("Los siete cuadrados", [
        ("Saturno", "3×3 · números del 1 al 9 · suma constante 15"),
        ("Júpiter", "4×4 · del 1 al 16 · suma 34"),
        ("Marte", "5×5 · del 1 al 25 · suma 65"),
        ("Sol", "6×6 · del 1 al 36 · suma 111"),
        ("Venus", "7×7 · del 1 al 49 · suma 175"),
        ("Mercurio", "8×8 · del 1 al 64 · suma 260"),
        ("Luna", "9×9 · del 1 al 81 · suma 369"),
    ]),
    p("La progresión no es casual: el orden del cuadrado sigue el orden caldeo de "
      "los planetas, del más lento al más rápido. Saturno, el más lento, recibe "
      "el cuadrado más pequeño; la Luna, la más rápida, el más grande. Y la suma "
      "constante de cada uno se calcula con una fórmula sencilla que puedes "
      "comprobar tú mismo: para un cuadrado de orden n, la suma es n·(n²+1)/2."),
    h("Para qué sirven, honestamente"),
    p("La tradición los usa para construir sigilos: se traza una línea que une "
      "los números correspondientes a las letras de un nombre y el trazo "
      "resultante se convierte en el signo de la operación. Es un procedimiento "
      "elegante y no tiene ningún poder por sí mismo."),
    p("Su utilidad real es otra y no es pequeña. Un cuadrado mágico es un objeto "
      "de concentración excepcional: obliga a una atención sostenida, "
      "verificable y con una recompensa inmediata —la suma cuadra o no cuadra—. "
      "Recorrer un cuadrado de nueve por nueve sumando cada fila es un ejercicio "
      "de atención de primer orden, y a diferencia de casi todos los ejercicios "
      "de atención, este te dice si lo has hecho bien."),
    pasos(
        "Elige el cuadrado del planeta con cuya función quieras trabajar.",
        "Cópialo a mano en el diario. A mano: el gesto de escribir cada número "
        "es la mitad del ejercicio.",
        "Comprueba las filas, luego las columnas, luego las dos diagonales. Si "
        "algo no cuadra, has copiado mal — y localizar dónde es la otra mitad del "
        "ejercicio.",
        "Traza sobre él la línea de tu operación, uniendo en orden los números "
        "que hayas decidido asociar a ella. Guarda el trazo. Es tu signo para "
        "esa operación y no tiene por qué significar nada para nadie más.",
    ),
    nota("La honestidad sobre los sigilos",
         "Un sigilo funciona como funciona una firma o un nudo en el pañuelo: es "
         "un ancla de memoria. Cada vez que lo ves, recuperas de golpe todo el "
         "contexto de la operación. Eso es mucho, y es todo. Atribuirle más es "
         "innecesario y además rebaja lo que sí hace."),
)

C10 = cap(
    "Los nombres y la voz",
    p("La vocalización de nombres es la parte de la práctica que más se ha "
      "envuelto en misterio y la que tiene la explicación más limpia. Merece un "
      "capítulo entero porque, bien hecha, es la técnica más eficaz del "
      "repertorio, y mal hecha es un ruido."),
    h("Qué se hace exactamente"),
    p("Se toma una fórmula breve —un nombre tradicional, una palabra, una frase "
      "de cuatro o cinco sílabas— y se sostiene en voz baja y grave durante toda "
      "una exhalación, hasta agotar el aire, sintiendo la resonancia en el pecho "
      "y no en la garganta. Se repite entre tres y siete veces, con una "
      "inhalación completa entre cada una."),
    h("Por qué funciona"),
    p("Por tres razones, todas ellas comprobables y ninguna sobrenatural."),
    pasos(
        "La exhalación prolongada. Alargar la espiración por encima de la "
        "inspiración es la maniobra respiratoria más simple para bajar la "
        "activación fisiológica. No hace falta nombre alguno para que funcione; "
        "el nombre simplemente da algo que hacer con el aire.",
        "La vibración torácica. Una nota sostenida en registro grave produce una "
        "sensación física localizada en el pecho. Esa sensación es un anclaje "
        "somático: da a la atención un lugar concreto donde posarse, y la "
        "atención con lugar es mucho más estable que la atención sin él.",
        "La repetición pautada. Un número fijo de repeticiones convierte una "
        "práctica difusa en una tarea con final. Se sabe cuándo se ha terminado, "
        "y eso elimina la deriva.",
    ),
    nota("La cuestión de qué nombre usar",
         "La tradición emplea nombres divinos hebreos, uno por cuarto y uno por "
         "planeta, y este libro los conserva porque son cortos, sonoros y están "
         "cargados de siglos de uso. Pero conviene decir la verdad: la eficacia "
         "de la técnica está en la respiración, en la vibración y en la "
         "repetición, no en la palabra concreta. Si el vocabulario religioso te "
         "incomoda o te resulta ajeno, elige fórmulas propias de cuatro o cinco "
         "sílabas abiertas y trabajarán igual de bien. Lo que no funciona es "
         "cambiarlas cada semana."),
    h("Las fórmulas de los cuatro cuartos"),
    p("Las que se usan en este libro, con su significado y su reparto. Se dan "
      "vocalizadas al castellano, para que se puedan pronunciar sin conocer el "
      "hebreo, y con la advertencia de que toda transliteración es una "
      "aproximación."),
    ficha("Una fórmula por cuarto", [
        ("Este · Aire", "IE-VE-HÚ · «el que es». Cuatro sílabas abiertas, muy "
                        "cómoda de sostener."),
        ("Sur · Fuego", "EL-O-HÍM · plural que se traduce en singular; la "
                        "tradición lo asocia al poder."),
        ("Oeste · Agua", "EL · la más breve de las cuatro; se sostiene en una "
                         "sola nota larga."),
        ("Norte · Tierra", "A-DO-NÁI · «mi señor»; la que mejor resuena en el "
                           "pecho de las cuatro."),
    ]),
    h("La técnica, paso a paso"),
    pasos(
        "De pie, hombros bajos, mandíbula suelta. La postura importa más que "
        "el volumen.",
        "Inhala por la nariz contando hasta cuatro, llenando el abdomen antes "
        "que el pecho.",
        "Vocaliza la fórmula en voz baja y grave, repartiendo las sílabas por "
        "toda la exhalación. No se grita: se sostiene. Si al terminar te falta "
        "el aire bruscamente, has ido demasiado rápido.",
        "Deja un segundo de silencio con los pulmones vacíos antes de volver a "
        "inhalar. Ese silencio es parte de la fórmula.",
        "Repite tres veces por cuarto en las operaciones diarias; siete en las "
        "operaciones largas. Nunca más de siete seguidas: la hiperventilación no "
        "es un estado alterado, es un mareo.",
    ),
    nota("Aviso concreto",
         "Si notas hormigueo en las manos o alrededor de la boca, sensación de "
         "irrealidad o mareo, para inmediatamente y respira normal. Son signos de "
         "hiperventilación, no de progreso. Si estás embarazada, tienes epilepsia, "
         "hipertensión no controlada o un trastorno de pánico, consulta antes con "
         "tu médico: los ejercicios respiratorios intensos no son inocuos en "
         "esas condiciones."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · LAS OPERACIONES
# ══════════════════════════════════════════════════════════════════════

C11 = cap(
    "La preparación",
    p("Nueve de cada diez sesiones fallidas fallan antes de empezar. La "
      "preparación no es un preliminar: es la mitad de la operación, y es la "
      "parte donde el principiante ahorra tiempo y el practicante no."),
    h("El sitio"),
    lista(
        "Siempre el mismo. Un rincón de la misma habitación basta. La constancia "
        "del lugar es la que hace que entrar en él ya signifique algo.",
        "Despejado de verdad: nada en el suelo, nada encendido, nada que pueda "
        "sonar. Un aviso de teléfono a mitad de operación no la interrumpe: la "
        "cancela.",
        "Con los cuartos marcados de forma estable. Si tienes que decidir dónde "
        "está el este cada día, el este no está en ninguna parte.",
        "A media luz. Ni oscuridad total —que produce somnolencia— ni luz de "
        "trabajo, que impide que el gesto se sienta distinto de cualquier otro.",
    ),
    h("El cuerpo"),
    lista(
        "Ni recién comido ni con hambre. Dos horas después de comer es el "
        "intervalo cómodo. Operar con el estómago lleno da somnolencia y con "
        "hambre da irritabilidad; ninguna de las dos es un estado místico.",
        "Sin alcohol y sin nada que altere la percepción. Este punto no admite "
        "matices: la práctica ritual busca precisión atencional, y todo lo que "
        "reduce la precisión trabaja en contra.",
        "Aseado y con ropa limpia reservada para esto. El baño previo aparece en "
        "todos los grimorios y no es superstición: es una transición sensorial "
        "que le dice al cuerpo que empieza otra cosa.",
        "Vejiga vacía, teléfono en otra habitación, y avisado quien viva contigo. "
        "Suena prosaico y es exactamente lo que separa una sesión de un intento.",
    ),
    h("La hora"),
    p("La tradición prescribe horas planetarias —el sistema de doce divisiones "
      "desiguales de amanecer a atardecer, cada una con su regente— y son "
      "utilizables si te interesa el detalle. Pero para la práctica diaria, la "
      "hora que funciona es una mucho más simple: la misma todos los días."),
    ficha("Los siete días y su función", [
        ("Lunes · Luna", "Ritmo, repetición, memoria, lo doméstico"),
        ("Martes · Marte", "Empuje, lo que da pereza, lo que hay que cortar"),
        ("Miércoles · Mercurio", "Palabra, orden, estudio, lo que hay que decir"),
        ("Jueves · Júpiter", "Expansión, generosidad, lo que debe crecer"),
        ("Viernes · Venus", "Vínculo, reconciliación, lo que se valora"),
        ("Sábado · Saturno", "Límite, cierre, revisión, lo que hay que soltar"),
        ("Domingo · Sol", "Identidad, centro, descanso real"),
    ]),
    nota("Lo que de verdad hace la hora fija",
         "No hay ninguna cualidad astral en las siete de la mañana. Lo que hay es "
         "un mecanismo perfectamente conocido: una conducta repetida a la misma "
         "hora en el mismo lugar deja de requerir decisión, y una conducta que no "
         "requiere decisión sobrevive a las semanas malas. Toda la eficacia del "
         "horario ritual está ahí, y es más que suficiente."),
    h("La secuencia mínima de preparación"),
    pasos(
        "Tres minutos antes: apaga y aparta el teléfono, avisa, cierra la puerta.",
        "Dos minutos antes: lávate las manos y la cara. Ponte la ropa de operar.",
        "Un minuto antes: de pie en el centro, con los brazos a los lados, cuenta "
        "diez respiraciones completas sin hacer nada más.",
        "Empieza. Y si en las diez respiraciones has decidido que hoy no, cierra "
        "la puerta y vete: una sesión ejecutada de mala gana enseña al cuerpo que "
        "esto se puede hacer de mala gana.",
    ),
)

C12 = cap(
    "El rito diario",
    p("Este es el capítulo central del libro y el único que hay que ejecutar sin "
      "falta. Es una operación corta —entre siete y diez minutos— construida sobre "
      "el rito menor del pentagrama que la Golden Dawn puso por escrito, con las "
      "fórmulas en castellano y el encuadre de esta casa. Se hace todos los días "
      "durante un mes antes de intentar cualquier otra cosa."),
    h("La estructura"),
    p("Cuatro movimientos, siempre en el mismo orden. Aprenderlos de memoria es "
      "el primer trabajo: mientras haya que consultar el libro, no hay atención "
      "disponible para lo demás."),
    pasos(
        "El eje. De pie en el centro, mirando al este. Se recorre el propio "
        "cuerpo de arriba abajo y de lado a lado, nombrando cada punto.",
        "Los cuatro pentagramas. Uno en cada cuarto, empezando por el este y "
        "girando en el sentido de las agujas del reloj, con su fórmula "
        "vocalizada en cada uno.",
        "Los cuatro custodios. Vuelto al centro, brazos en cruz, se nombran las "
        "cuatro funciones en su sitio.",
        "El eje otra vez. Se repite el primer movimiento y se cierra.",
    ),
    sep(),
    h("Movimiento primero · El eje"),
    p("De pie, pies paralelos, hombros bajos, mirando al este. Con los dedos "
      "índice y medio de la mano derecha se toca cada punto y se nombra en voz "
      "baja mientras se toca."),
    ritual(
        "Frente — lo que está por encima de mí.",
        "Pecho — lo que está por debajo de mí.",
        "Hombro derecho — lo que está a mi derecha.",
        "Hombro izquierdo — lo que está a mi izquierda.",
        "Manos juntas al pecho — y yo, aquí, en el centro.",
    ),
    p("El movimiento dura menos de un minuto y hace algo muy concreto: sitúa. Un "
      "operante que no sabe dónde está su propio cuerpo en el espacio no puede "
      "sostener atención sobre nada más."),
    h("Movimiento segundo · Los cuatro pentagramas"),
    p("Se camina al este. Se traza el pentagrama de apertura —de la cadera "
      "izquierda a la frente y de ahí el recorrido completo—, se apunta al centro "
      "de la figura con los dos dedos y se vocaliza la fórmula del cuarto. Luego "
      "se gira al sur, al oeste y al norte, en ese orden, repitiendo lo mismo."),
    ficha("El recorrido y su fórmula", [
        ("Este", "Pentagrama de apertura · IE-VE-HÚ · tres veces"),
        ("Sur", "Pentagrama de apertura · EL-O-HÍM · tres veces"),
        ("Oeste", "Pentagrama de apertura · EL · tres veces"),
        ("Norte", "Pentagrama de apertura · A-DO-NÁI · tres veces"),
    ]),
    nota("El detalle que casi todos hacen mal",
         "Entre un cuarto y el siguiente el brazo se mantiene extendido, "
         "trazando con los dedos una línea a la altura del hombro mientras se "
         "camina. No se bajan los brazos hasta haber cerrado el cuarto círculo en "
         "el este. Suena a manía y no lo es: mantener el brazo extendido es lo "
         "que impide que el recorrido se convierta en cuatro gestos sueltos."),
    h("Movimiento tercero · Los cuatro custodios"),
    p("Vuelto al centro y mirando al este, brazos extendidos en cruz. Se nombra "
      "cada función en su sitio, sin girar, dejando un par de segundos entre una "
      "y otra."),
    ritual(
        "Delante de mí, el aliento: lo que respiro y lo que digo.",
        "A mi derecha, la voluntad: lo que decido y sostengo.",
        "Detrás de mí, la memoria: lo que siento y lo que recuerdo.",
        "A mi izquierda, el cuerpo: lo que me sostiene y se cansa.",
        "Y en el centro, quien mira las cuatro.",
    ),
    nota("Qué son los custodios y qué no",
         "No se está llamando a nadie. Se está nombrando en voz alta y en un "
         "orden fijo las cuatro funciones del propio operante, situándolas en el "
         "espacio para poder mirarlas de una en una. Es un inventario, y hacerlo "
         "en voz alta y de pie funciona mucho mejor que hacerlo pensando, por la "
         "misma razón por la que una lista escrita funciona mejor que una lista "
         "recordada."),
    h("Movimiento cuarto · El cierre"),
    p("Se repite el movimiento del eje, exactamente igual que al principio, y se "
      "termina con las manos juntas al pecho y tres respiraciones completas. "
      "Después se camina el círculo en sentido contrario a las agujas del reloj, "
      "una vuelta, y se sale."),
    p("Y ya está. Entre siete y diez minutos, todos los días. La tentación de "
      "añadir cosas aparecerá la segunda semana: no le hagas caso hasta el mes."),
    h("Qué esperar del primer mes"),
    lista(
        "Primera semana: torpeza y sensación de ridículo. Es lo normal y no "
        "significa nada. Se ejecuta igual.",
        "Segunda semana: la secuencia empieza a salir sin pensarla y aparece el "
        "aburrimiento. Es el tramo donde se abandona, y es el tramo que hay que "
        "atravesar.",
        "Tercera semana: la primera señal real. Entrar en el sitio ya produce un "
        "cambio de estado antes de haber hecho nada. Eso es el condicionamiento "
        "funcionando, y es todo el efecto que el rito promete.",
        "Cuarta semana: se nota cuándo falta. Ese es el indicador de que la "
        "práctica está instalada, y el momento de pasar al capítulo siguiente.",
    ),
)

C13 = cap(
    "La operación planetaria",
    p("Con el rito diario instalado, se puede trabajar sobre una función "
      "concreta. La operación planetaria es una sesión más larga —de veinte a "
      "treinta minutos— dedicada a una sola de las siete funciones, en su día, y "
      "con un objetivo escrito de antemano."),
    h("La estructura de la sesión"),
    pasos(
        "Rito diario completo. Sin excepción: es la apertura.",
        "Hexagrama del planeta en el este, con su sigilo trazado en el centro de "
        "la figura.",
        "Vocalización del nombre del planeta, siete veces.",
        "El trabajo: veinte minutos sobre el asunto elegido, con el cuadrado del "
        "planeta y el diario delante.",
        "Cierre del hexagrama y rito diario otra vez, completo. La sesión no "
        "termina hasta esto.",
    ),
    h("Las siete operaciones"),
    p("Una por función. La columna del objetivo es lo que se pone por escrito "
      "antes de empezar: sin objetivo escrito la sesión se convierte en "
      "divagación con velas."),
    ficha("Saturno · sábado", [
        ("Función", "El límite y el cierre"),
        ("Se trabaja", "Lo que hay que terminar, soltar o decir no"),
        ("El objetivo se escribe así", "«Voy a cerrar ___» o «voy a dejar de ___»"),
        ("Soporte", "Cuadrado de 3×3 · suma 15 · color negro o plomo"),
    ]),
    ficha("Júpiter · jueves", [
        ("Función", "La expansión y la generosidad"),
        ("Se trabaja", "Lo que debe crecer; lo que uno retiene sin motivo"),
        ("El objetivo se escribe así", "«Voy a abrir ___» o «voy a dar ___»"),
        ("Soporte", "Cuadrado de 4×4 · suma 34 · color púrpura o azul"),
    ]),
    ficha("Marte · martes", [
        ("Función", "El empuje y la defensa"),
        ("Se trabaja", "Lo que se posterga por miedo; el límite que no se pone"),
        ("El objetivo se escribe así", "«Voy a hacer hoy ___» o «voy a decir ___»"),
        ("Soporte", "Cuadrado de 5×5 · suma 65 · color rojo"),
    ]),
    ficha("Sol · domingo", [
        ("Función", "La identidad y el centro"),
        ("Se trabaja", "Lo que se reconoce como propio; lo que se hace por "
                       "encargo ajeno"),
        ("El objetivo se escribe así", "«Voy a reconocer ___» o «esto no es mío: ___»"),
        ("Soporte", "Cuadrado de 6×6 · suma 111 · color oro"),
    ]),
    ficha("Venus · viernes", [
        ("Función", "El vínculo y el valor"),
        ("Se trabaja", "Lo que se ha descuidado en una relación; lo que se "
                       "valora de verdad"),
        ("El objetivo se escribe así", "«Voy a atender ___» o «voy a reparar ___»"),
        ("Soporte", "Cuadrado de 7×7 · suma 175 · color verde o cobre"),
    ]),
    ficha("Mercurio · miércoles", [
        ("Función", "La palabra y el orden"),
        ("Se trabaja", "Lo que hay que decir y no se dice; lo que está sin ordenar"),
        ("El objetivo se escribe así", "«Voy a decir ___» o «voy a ordenar ___»"),
        ("Soporte", "Cuadrado de 8×8 · suma 260 · color naranja o mezcla"),
    ]),
    ficha("Luna · lunes", [
        ("Función", "El ritmo y la repetición"),
        ("Se trabaja", "El hábito que falta y el que sobra; el sueño; la casa"),
        ("El objetivo se escribe así", "«Voy a repetir ___ durante ___ días»"),
        ("Soporte", "Cuadrado de 9×9 · suma 369 · color plata o blanco"),
    ]),
    nota("La regla de la comprobación",
         "Toda operación planetaria termina con una acción concreta en el mundo, "
         "fijada antes de cerrar y ejecutada en las veinticuatro horas "
         "siguientes. Una llamada, una frase dicha, un cajón vaciado, una hora de "
         "sueño más. Sin esa bajada a lo concreto la sesión no ha ocurrido — es "
         "la regla de Maljut del capítulo 8, y es la que impide que todo esto se "
         "convierta en entretenimiento."),
)

C14 = cap(
    "La dedicación de las armas",
    p("Los grimorios dedican páginas enteras a la fabricación y consagración de "
      "instrumentos: maderas cortadas en día y hora, metales fundidos, tintas "
      "preparadas, ceremonias de horas. Es material fascinante y aquí se reduce "
      "deliberadamente a lo que hace efecto."),
    h("Qué hace efecto"),
    p("Que el objeto no se use para nada más. Eso es todo, y es mucho. Un vaso "
      "que solo se toca dentro del círculo se convierte, en cuestión de semanas, "
      "en un disparador fiable: cogerlo trae consigo el estado entero de la "
      "operación. Un vaso que además sirve para el agua de la mesilla no "
      "dispara nada, aunque lo hayas consagrado en luna nueva con siete velas."),
    h("La ceremonia mínima"),
    pasos(
        "Elige el objeto y decide que es esa arma y no otra. Si dudas entre dos "
        "usos posibles, no es el objeto.",
        "Límpialo físicamente. Agua y un paño. No es simbólico: es que lo "
        "estás mirando de cerca por primera vez.",
        "Dentro del círculo, después del rito diario, sostenlo en el cuarto que "
        "le corresponde y di en voz alta para qué es y para qué no es. En tus "
        "propias palabras, sin fórmula prestada.",
        "Vocaliza la fórmula del cuarto tres veces con el objeto en la mano.",
        "Anótalo en el diario con la fecha. Ese apunte es la consagración: es la "
        "prueba de que hubo un antes y un después.",
        "Guárdalo en su sitio y no lo uses para nada más. Aquí empieza lo "
        "difícil, y es lo único que de verdad importa.",
    ),
    nota("Si rompes la regla",
         "Ocurre: un día se usa la copa para beber agua porque estaba a mano. No "
         "hay ninguna consecuencia mágica y sí una consecuencia real: el objeto "
         "ha perdido parte de su capacidad de disparar. Se repara del único modo "
         "posible, que es repetir la dedicación y anotar también eso. Un diario "
         "que solo registra los aciertos no sirve para nada."),
    h("El orden en que se dedican"),
    p("Una por mes, y en este orden: disco, copa, espada, vara. De lo concreto a "
      "lo abstracto. Se empieza por el cuerpo porque es donde uno está, y se "
      "acaba por la voluntad porque es la que menos se conoce. Cuatro meses para "
      "cuatro objetos parece lento y es exactamente el ritmo: el objetivo no es "
      "tener el equipo completo, es que cada objeto haya tenido tiempo de "
      "significar algo."),
)

C15 = cap(
    "Qué se invoca de verdad",
    p("Este capítulo aborda de frente la pregunta que el título del libro plantea "
      "y que sería deshonesto esquivar. Cuando se ejecuta una invocación, ¿qué "
      "acude?"),
    h("La respuesta de este libro"),
    p("Acude una parte del operante que normalmente no está disponible. Ni más "
      "ni menos que eso — y conviene ver que «ni menos» es una afirmación fuerte, "
      "porque lo que normalmente no está disponible es la mayor parte de "
      "nosotros."),
    p("La operación ritual hace tres cosas a la vez: fija la atención con una "
      "secuencia motora, satura los canales de distracción con gesto, voz y "
      "respiración, y personifica una función interna dándole un nombre, un sitio "
      "y una voz. Ese último paso es el que produce el fenómeno que la tradición "
      "describe como presencia. Al dirigirse a la propia cólera como si fuera "
      "alguien que está enfrente, se obtiene acceso a información sobre ella que "
      "de otro modo no aparece, porque dejar de ser algo es la condición para "
      "poder verlo."),
    nota("El nombre técnico de esto",
         "La psicología contemporánea trabaja con este mecanismo desde hace "
         "décadas con nombres distintos: diálogo entre partes, silla vacía, "
         "trabajo con voces internas. Todos comparten el hallazgo básico: dar voz "
         "y lugar a un contenido interno produce un cambio de perspectiva que la "
         "reflexión silenciosa no produce. La tradición ritual llegó a lo mismo "
         "varios siglos antes y con mejor puesta en escena."),
    h("Lo que esto excluye"),
    lista(
        "Excluye que la entidad tenga existencia propia, intenciones propias o "
        "conocimiento que el operante no posea. Si en una operación aparece "
        "información que no tenías, revisa de dónde la sacaste antes de "
        "atribuirla a nadie.",
        "Excluye el pacto, la orden y la obligación. No se puede obligar a nada "
        "porque no hay nada externo a lo que obligar; toda la literatura de "
        "sometimiento de espíritus es, leída así, una descripción bastante "
        "exacta de la lucha contra uno mismo.",
        "Excluye la influencia sobre terceros. Ninguna operación de este libro "
        "actúa sobre otra persona. Si lo que buscas es eso, este no es tu libro y "
        "probablemente lo que buscas sea una conversación.",
    ),
    h("Y lo que esto permite"),
    p("Permite mucho más de lo que parece. Permite examinar una obsesión sin "
      "estar dentro de ella. Permite darle voz a la parte que se resiste y "
      "escuchar qué dice, que casi nunca es lo que uno suponía. Permite separar "
      "una emoción de la interpretación que la acompaña. Permite, con "
      "constancia, un grado de conocimiento del propio funcionamiento que la "
      "introspección informal no alcanza, porque la introspección informal la "
      "hace el mismo que está siendo examinado y sin ninguna estructura que lo "
      "impida."),
    h("El límite, y es serio"),
    p("Personificar contenidos internos es una técnica potente y no es inocua "
      "para todo el mundo. Si tienes antecedentes de episodios psicóticos, de "
      "disociación, de trastorno de identidad o estás en una crisis aguda, esta "
      "clase de práctica puede desestabilizar y debe hacerse, si se hace, con "
      "acompañamiento profesional. No hay ningún mérito en atravesar solo lo que "
      "requiere ayuda, y este libro no va a sugerir lo contrario."),
    ritual(
        "Regla única de esta práctica:",
        "si al terminar no puedes volver a la habitación,",
        "no era una operación. Era un episodio.",
        "Se cierra, se anota y se consulta.",
    ),
)

C16 = cap(
    "El triángulo: el trabajo de examen",
    p("La operación más útil del libro es también la más incómoda, y consiste en "
      "poner algo propio fuera del círculo para poder mirarlo."),
    h("La operación"),
    pasos(
        "Rito diario completo.",
        "Escribe en una hoja, en una sola frase, lo que vas a examinar. Una "
        "cólera concreta, un miedo concreto, una conducta que repites y no "
        "entiendes. Una sola cosa y en una sola frase: si no cabe en una frase, "
        "todavía no sabes qué es.",
        "Coloca la hoja fuera del círculo, en el este, sobre el triángulo si lo "
        "tienes trazado o simplemente en el suelo si no.",
        "Vuelve al centro. Mírala desde dentro del círculo, en silencio, durante "
        "cinco minutos. Sin analizar y sin resolver: mirar.",
        "Habla con ella en voz alta. Pregúntale tres cosas: qué quiere, de qué "
        "protege y qué necesitaría para aflojar.",
        "Responde en voz alta, como si respondiera ella. Esta parte da vergüenza "
        "y es la parte que funciona.",
        "Vuelve al silencio un minuto. Después recoge la hoja, anota en el diario "
        "lo que se ha dicho y cierra con el rito diario completo.",
    ),
    nota("Las tres preguntas, y por qué esas",
         "«Qué quiere» descubre la intención, que casi nunca es la que se le "
         "atribuye. «De qué protege» descubre la función, porque casi todo "
         "patrón sostenido durante años protege de algo que en su momento hizo "
         "falta. «Qué necesitaría» descubre la vía de salida, y suele ser mucho "
         "más pequeña de lo esperado. En ese orden: intención, función, vía."),
    h("Errores frecuentes en esta operación"),
    lista(
        "Examinar dos cosas a la vez. No funciona: se mezclan y se pierde el "
        "hilo. Una por sesión.",
        "Discutir con ella. No es un juicio, es una entrevista. El operante que "
        "discute está otra vez dentro.",
        "Buscar una conclusión en la primera sesión. Un patrón de veinte años no "
        "se examina en veinte minutos. Tres o cuatro sesiones sobre el mismo "
        "asunto, separadas por semanas, rinden mucho más que una sesión larga.",
        "No cerrar. Este es el error grave. Una sesión de examen que termina sin "
        "el rito de cierre deja el asunto abierto y dando vueltas el resto del "
        "día. Se cierra siempre, incluso —sobre todo— cuando ha ido mal.",
    ),
    h("Cuándo parar"),
    p("Cuando aparece llanto que no se puede sostener, cuando el pulso no baja, "
      "cuando la sesión deja de ser un examen y se convierte en revivir. En "
      "cualquiera de esos tres casos se cierra inmediatamente, se anota qué pasó "
      "y no se vuelve a ese asunto en solitario. No es un fracaso de la técnica: "
      "es la técnica informando de que ese material necesita a otra persona en la "
      "habitación, y esa persona es un profesional."),
)

C17 = cap(
    "El cierre y por qué nunca se omite",
    p("Todos los manuales insisten en el cierre y casi ningún practicante lo hace "
      "bien. Merece capítulo aparte porque es el punto donde una práctica sana se "
      "distingue de una práctica que desgasta."),
    h("Qué es el cierre"),
    p("Una secuencia fija que deshace lo hecho, en orden inverso y sin prisa: se "
      "despiden los cuartos, se traza el pentagrama en la dirección contraria, se "
      "repite el eje, se camina el círculo al revés y se sale. Tres minutos, "
      "siempre los mismos."),
    h("Qué hace, en términos comprobables"),
    lista(
        "Marca un final. Sin final explícito, una sesión intensa se prolonga "
        "difusamente en el resto del día: la cabeza sigue en la operación sin "
        "estar en ella.",
        "Devuelve al cuerpo. La secuencia de cierre es física y termina en la "
        "habitación, con las manos en el pecho y tres respiraciones. Es un "
        "procedimiento de aterrizaje.",
        "Enseña al sistema nervioso que esto tiene límites. Un estado alterado "
        "que se sabe reversible se explora con mucha más libertad que uno que se "
        "teme. El cierre es lo que hace segura la apertura.",
        "Protege la práctica a largo plazo. La gente que abandona después de "
        "meses casi siempre abandona por acumulación: sesiones que no acabaron y "
        "dejaron residuo. El cierre es mantenimiento.",
    ),
    nota("La regla sin excepciones",
         "Si abriste, cierras. Si te interrumpen, cierras — aunque sea en "
         "treinta segundos y de pie. Si la sesión ha ido mal, cierras con más "
         "cuidado, no con menos. Si te has dormido a mitad, cierras al "
         "despertar. No hay ningún caso en que salir sin cerrar sea la opción "
         "correcta."),
    h("El cierre de emergencia"),
    p("Para cuando hay que salir ya: alguien llama, suena una alarma, algo se ha "
      "torcido. Veinte segundos, de pie, en el centro."),
    ritual(
        "Manos al pecho.",
        "«Esto queda cerrado.»",
        "Tres respiraciones completas, largas.",
        "Un paso fuera del círculo, mirando al norte.",
        "Y se anota después, aunque sea una línea.",
    ),
    p("No es tan bueno como el cierre completo y es infinitamente mejor que nada. "
      "Que exista un procedimiento de emergencia es, además, lo que permite "
      "operar tranquilo sabiendo que se puede salir."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE IV · EL OFICIO SOSTENIDO
# ══════════════════════════════════════════════════════════════════════

C18 = cap(
    "El diario del operante",
    p("Si de este libro solo pudieras conservar una práctica, conserva esta. El "
      "diario no es un accesorio de la práctica: es el instrumento que convierte "
      "sesiones sueltas en conocimiento acumulado."),
    h("Por qué sin diario no hay práctica"),
    p("Por una razón muy simple y bastante humillante: la memoria de los propios "
      "estados internos es malísima. A las dos semanas no recuerdas cómo fue una "
      "sesión, y lo que recuerdas está reescrito por lo que ha pasado desde "
      "entonces. Sin registro escrito no puedes saber si algo está funcionando, y "
      "por tanto no puedes corregir nada. Estás repitiendo, no practicando."),
    h("Qué se anota"),
    ficha("Entrada mínima por sesión", [
        ("Fecha y hora", "La hora real, no la prevista"),
        ("Duración", "Minutos efectivos"),
        ("Operación", "Rito diario / planetaria / examen / dedicación"),
        ("Estado antes", "Una palabra. No un párrafo: una palabra"),
        ("Estado después", "Otra palabra"),
        ("Qué falló", "El olvido, la interrupción, la prisa, la desgana"),
        ("Qué apareció", "Solo si apareció algo. Casi nunca aparece nada, y "
                         "anotar que no apareció nada también es un dato"),
        ("La acción concreta", "Lo que vas a hacer en las próximas 24 horas"),
    ]),
    nota("Contra el diario literario",
         "La tentación de escribir bonito arruina el registro. Las entradas "
         "útiles son cortas, feas y precisas: «17/03, 7:10, 9 min, rito diario, "
         "antes: disperso, después: igual, falló la prisa en el norte». Eso, "
         "repetido cien veces, revela patrones que ningún párrafo elegante "
         "revela."),
    h("La revisión, que es donde está el valor"),
    pasos(
        "Cada domingo, relee la semana entera. Diez minutos.",
        "Cuenta las sesiones hechas frente a las previstas. El número, sin "
        "excusas al lado.",
        "Busca el patrón de los fallos: siempre falla el mismo día, la misma "
        "hora, el mismo movimiento.",
        "Cada tres meses, relee el trimestre completo y escribe media página. "
        "Aquí es donde se ve lo que ninguna sesión individual muestra.",
        "Cada año, relee el año. Es la práctica más incómoda del libro y la que "
        "más enseña.",
    ),
)

C19 = cap(
    "Los errores del principiante",
    p("Recogidos sin piedad, porque son predecibles y cuestan años."),
    h("Los siete errores"),
    pasos(
        "Coleccionar en lugar de practicar. Leer diez libros, comprar cuatro "
        "armas, aprender doce sistemas y no haber hecho treinta días seguidos de "
        "nada. Es el error más común y el más cómodo, porque estudiar es "
        "agradable y repetir no.",
        "Empezar por lo complicado. La operación espectacular antes del rito "
        "diario. Sin la base instalada no hay atención disponible para nada "
        "elaborado, y lo elaborado sin atención es disfraz.",
        "Cambiar de sistema al primer aburrimiento. El aburrimiento de la segunda "
        "semana no es una señal de que el sistema no sirve: es exactamente el "
        "tramo que hay que atravesar, y cambiar de método en ese punto garantiza "
        "atravesarlo nunca.",
        "Buscar fenómenos. Esperar visiones, voces, sensaciones. La práctica bien "
        "hecha produce sobre todo una cosa muy poco vistosa: más atención "
        "disponible en la vida ordinaria. Quien busca espectáculo se acaba "
        "convenciendo de que lo ha visto, y ahí empieza el autoengaño.",
        "No cerrar. Ya dicho en el capítulo 17, y se repite porque es el error "
        "que más desgasta a largo plazo.",
        "Practicar en crisis. La práctica intensiva no es el sitio donde resolver "
        "una crisis aguda; en el mejor de los casos no ayuda y en el peor la "
        "amplifica. En crisis se reduce a lo mínimo, se sostiene el rito diario "
        "corto y se busca ayuda.",
        "El secreto y la superioridad. La sensación de pertenecer a una minoría "
        "que sabe algo es la trampa más antigua del oficio. Es agradable, es "
        "falsa y aísla. Todo lo que hay en este libro está publicado desde el "
        "siglo XIX.",
    ),
    sep(),
    h("La prueba de realidad"),
    p("Hay una manera muy simple de saber si una práctica ritual está haciendo su "
      "trabajo, y no tiene nada que ver con lo que se sienta durante la sesión. "
      "Pregunta a quien vive contigo si te nota distinto, y en qué. Si llevas seis "
      "meses de práctica diaria y nadie a tu alrededor ha notado nada en ninguna "
      "dirección, algo no está pasando donde tendría que pasar."),
    nota("Y la prueba inversa",
         "Si lo que notan es que estás más raro, más aislado o más irritable, la "
         "práctica está haciendo daño y hay que parar y revisar. Una disciplina "
         "de atención bien llevada hace a la gente más presente y más fácil de "
         "tratar, no menos. Cualquier camino que te aleje de los tuyos y te "
         "convenza de que eso es progreso está mal construido."),
)

C20 = cap(
    "El cuerpo del operante",
    p("Los grimorios prescriben ayunos, vigilias, abstinencias y baños, y esa "
      "parte del material se suele leer como folclore devoto. Es un error: son "
      "prescripciones sobre el estado fisiológico del operante, y lo que "
      "buscaban —a tientas y sin fisiología— sigue siendo exactamente lo que "
      "hace falta."),
    nota("El encuadre de este capítulo",
         "Lo que sigue son hábitos de sentido común orientados a tener atención "
         "disponible. No es una pauta dietética ni un programa de entrenamiento "
         "individualizado, y no considera patologías. Si tienes una condición "
         "médica, tomas medicación, estás embarazada o tienes antecedentes de "
         "trastorno alimentario, nada de este capítulo se aplica sin que lo "
         "revise antes tu profesional sanitario. El ayuno, en particular, está "
         "contraindicado en varios casos y no es negociable."),
    h("El sueño, que es lo primero"),
    p("No hay técnica de atención que compense dormir mal. Es el factor con más "
      "peso de todo este capítulo y el más ignorado, porque no tiene ningún "
      "atractivo esotérico. Un operante con cinco horas de sueño no tiene "
      "atención que dirigir: tiene un déficit."),
    lista(
        "Hora fija de acostarse, incluido el fin de semana. La regularidad pesa "
        "más que la cantidad total.",
        "La última hora sin pantalla y sin trabajo. Si solo puedes cambiar una "
        "cosa de este capítulo, cambia esta.",
        "Habitación fresca y a oscuras. Es barato y funciona.",
        "Si la sesión es por la mañana —lo recomendable—, se levanta media hora "
        "antes, no se recorta el sueño por el otro extremo.",
    ),
    h("La comida, en clave de atención"),
    p("El criterio aquí no es la composición corporal: es la estabilidad. Lo que "
      "interesa es evitar los dos estados que arruinan una sesión, que son la "
      "somnolencia posprandial y la irritabilidad del hambre."),
    lista(
        "Operar dos horas después de comer o antes de desayunar. En los dos "
        "casos el estómago está tranquilo.",
        "Proteína y verdura en la comida previa; azúcar rápido, no. El bajón "
        "posterior cae justo en la sesión.",
        "Cafeína, si se usa, temprano y en cantidad fija. Es el hábito que más "
        "distorsiona la percepción del propio estado, y una práctica que "
        "consiste en observar el propio estado no se lleva bien con eso.",
        "Agua a mano y bebida antes, no durante. Levantarse a beber a mitad de "
        "una operación es la interrupción más tonta y la más frecuente.",
        "Alcohol, no. El día de la sesión y el anterior. No por pureza: porque "
        "arrasa el sueño profundo y el efecto se nota al día siguiente.",
    ),
    h("El ayuno tradicional, revisado"),
    p("Los manuales antiguos prescriben ayunar antes de las operaciones "
      "importantes. Lo que produce el ayuno breve es un estado de alerta "
      "ligeramente aumentada que, en efecto, favorece la concentración. Lo que "
      "también produce, pasado cierto punto, es irritabilidad, mala regulación "
      "emocional y decisiones peores. La versión utilizable es la más modesta: "
      "operar en ayunas por la mañana, antes del desayuno. Eso es todo. Los "
      "ayunos de tres días de los grimorios no producen lucidez, producen "
      "hipoglucemia — y en varias condiciones médicas son peligrosos."),
    h("El movimiento"),
    p("La tradición no dice nada de esto y debería. Una sesión de veinte minutos "
      "de pie, girando, con los brazos extendidos y sosteniendo la voz exige una "
      "condición física mínima, y el operante que se cansa deja de tener atención "
      "libre. No hace falta nada heroico."),
    lista(
        "Caminar cuarenta minutos al día. Es la base, y es suficiente para lo "
        "que aquí se pide.",
        "Movilidad de hombro y de cadera antes de operar: tres minutos. Los "
        "brazos extendidos durante el recorrido de los cuartos se notan en el "
        "trapecio a la segunda semana.",
        "Algo de fuerza dos veces por semana, con lo que tengas. La postura de "
        "pie sostenida es una demanda de fuerza, no de flexibilidad.",
        "Respiración: los ejercicios del capítulo 10, fuera de la sesión, tres "
        "minutos al día. Es lo que hace que la vocalización no se quede corta de "
        "aire.",
    ),
    ficha("Lo que la tradición prescribía y lo que era en realidad", [
        ("El baño previo", "Transición sensorial. Funciona, se conserva."),
        ("El ayuno", "Alerta aumentada. Se conserva en su versión breve; los "
                     "ayunos largos se descartan."),
        ("La vigilia nocturna", "Privación de sueño. Se descarta: perjudica "
                                "exactamente lo que se busca."),
        ("La abstinencia", "Reducción de estímulo. Se conserva como reducción "
                           "voluntaria y temporal de distracción, no como norma "
                           "moral."),
        ("La ropa reservada", "Disparador condicionado. Funciona muy bien, se "
                              "conserva."),
        ("El incienso", "Anclaje olfativo, que es el más potente de todos. Se "
                        "conserva, con ventilación."),
    ]),
    nota("El resumen del capítulo",
         "Duerme a la misma hora, come dos horas antes, no bebas alcohol el día "
         "anterior, camina todos los días y opera en el mismo sitio a la misma "
         "hora. Eso es el noventa por ciento del trabajo corporal del oficio, y "
         "no tiene absolutamente nada de misterioso. La parte misteriosa es que "
         "casi nadie lo hace."),
)

C21 = cap(
    "El año de práctica",
    p("Un plan de doce meses, para quien quiera uno. No es obligatorio y es "
      "mejor que improvisar."),
    ficha("Los cuatro trimestres", [
        ("Meses 1–3", "Solo el rito diario, todos los días, y el diario. Nada "
                      "más. Se dedica el disco en el mes 2 y la copa en el 3."),
        ("Meses 4–6", "Se añade una operación planetaria por semana, empezando "
                      "por Saturno y bajando por el orden caldeo. Se dedican la "
                      "espada y la vara."),
        ("Meses 7–9", "Se añade una operación de examen al mes, sobre un solo "
                      "asunto, tres sesiones separadas. Se sigue con las "
                      "planetarias."),
        ("Meses 10–12", "Se sostiene todo lo anterior sin añadir nada. El último "
                        "trimestre es el que de verdad prueba si hay práctica: "
                        "no trae novedades."),
    ]),
    h("Los tres indicadores"),
    p("Cómo saber si el año ha servido. Ninguno de los tres tiene que ver con lo "
      "que se sienta durante las sesiones."),
    pasos(
        "El número. Sesiones hechas frente a sesiones previstas, sacado del "
        "diario. Por encima del setenta por ciento hay práctica; por debajo del "
        "cincuenta, hay intención.",
        "La recuperación. Cuánto tardas en volver después de una interrupción de "
        "una semana. Al principio son semanas; con el año instalado son días. "
        "Ese es el indicador más fiable de todos.",
        "El testimonio ajeno. Lo que nota la gente que convive contigo, "
        "preguntado directamente y sin sugerir la respuesta."),
    nota("Y una advertencia sobre el segundo año",
         "El riesgo del segundo año no es abandonar: es la comodidad. Un rito "
         "que se ejecuta perfectamente y sin ninguna atención es un hábito "
         "motor, no una práctica. La señal de alarma es dejar de anotar «qué "
         "falló» porque ya nunca falla nada. Cuando llegues ahí, cambia algo: la "
         "hora, el sitio, la fórmula. La incomodidad es parte del método."),
)

C22 = cap(
    "Cuaderno de registro",
    p("Estas páginas son para escribir. La parte de este libro que produce "
      "resultados no es la que se lee."),
    h("Ficha de partida"),
    ficha("Antes de empezar", [
        ("Fecha de inicio", "________________________"),
        ("Sitio elegido", "________________________"),
        ("Dónde está el este", "________________________"),
        ("Hora fija de la sesión", "________________________"),
        ("Lo que espero de esto", "________________________"),
        ("Lo que temo de esto", "________________________"),
    ]),
    nota("Sobre la última línea",
         "Escríbela. Casi nadie lo hace y es la más informativa de las seis. "
         "Dentro de un año, releerla explicará bastante de lo que haya pasado en "
         "medio."),
    h("Plantilla de sesión"),
    ficha("Se copia una por día", [
        ("Fecha y hora real", "____________"),
        ("Minutos", "____________"),
        ("Operación", "diaria · planetaria · examen · dedicación"),
        ("Antes / después", "________ / ________"),
        ("Qué falló", "____________"),
        ("Acción en 24 h", "____________"),
    ]),
    h("Revisión trimestral"),
    ficha("Cada tres meses", [
        ("Sesiones previstas / hechas", "________ / ________"),
        ("El fallo que más se repite", "____________"),
        ("Lo que ha cambiado en la vida concreta", "____________"),
        ("Lo que no ha cambiado y esperaba que cambiara", "____________"),
        ("Qué toco el trimestre que viene", "____________"),
    ]),
    h("Cierre del año"),
    ficha("A los doce meses", [
        ("Porcentaje de cumplimiento", "____________"),
        ("Tiempo de recuperación tras una interrupción", "____________"),
        ("Lo que ha dicho quien convive conmigo", "____________"),
        ("La operación que más me costó", "____________"),
        ("La que sigo haciendo un año después", "____________"),
        ("Lo que dejo de hacer y por qué", "____________"),
    ]),
    sep(),
    p("Un último apunte, y con esto el libro ha hecho su trabajo. Todo lo que hay "
      "aquí está construido para producir una sola cosa: más atención disponible "
      "en la vida ordinaria. No poder, no conocimiento secreto, no pertenencia a "
      "ninguna minoría iluminada. Atención — que resulta ser, cuando se examina "
      "de cerca, lo único que teníamos para gastar."),
    p("Si al final del año tienes doce meses de registro escrito con tu letra y "
      "la gente que te rodea te encuentra un poco más presente, el oficio ha "
      "funcionado. Y si además te has dado cuenta de que ninguna de las seis "
      "láminas de este libro hacía nada por sí sola, entonces ha funcionado del "
      "todo."),
)



C23 = cap(
    "La tabla completa de las horas planetarias",
    p("El capítulo 11 explicó el sistema de horas y dio el reparto de los siete "
      "días. Aquí va la tabla entera: ciento sesenta y ocho casillas, las "
      "veinticuatro horas de cada uno de los siete días con su regente. No la he "
      "encontrado impresa completa en ningún manual moderno, y es la pieza que "
      "convierte el sistema de una curiosidad en una herramienta utilizable."),
    fig("am-horas", "Lám. 7",
        "Las 168 horas planetarias. Cada fila es un día; cada casilla, una hora "
        "desde el amanecer. La línea vertical separa las doce horas de día de las "
        "doce de noche. En destacado, las cuatro horas de cada día que pertenecen "
        "al planeta que le da nombre."),
    h("Cómo leerla"),
    pasos(
        "Localiza tu día en la columna de la izquierda.",
        "Cuenta las horas desde el amanecer, no desde medianoche. La hora 1 empieza "
        "cuando sale el Sol; la hora 13, cuando se pone.",
        "Recuerda que no son horas de sesenta minutos. Divide la duración real del "
        "día entre doce y la de la noche entre doce: en verano las diurnas son "
        "largas y las nocturnas cortas, y al contrario en invierno. Solo coinciden "
        "en los equinoccios.",
        "Las casillas destacadas son las horas del regente del día. Son cuatro por "
        "día —la 1, la 8, la 15 y la 22— y son el momento clásico para la "
        "operación de ese planeta.",
    ),
    nota("El dato que la tabla demuestra sola",
         "Mira la primera casilla de cada fila y luego cuenta veinticuatro. La "
         "casilla veinticinco —que es la primera del día siguiente— cae siempre en "
         "el regente del día siguiente. Domingo empieza en el Sol, su hora 24 es "
         "Mercurio, y la 25 es la Luna: lunes. Esa es toda la explicación del "
         "orden de la semana, y la tabla la contiene sin necesidad de "
         "argumentarla. El generador de esta lámina comprueba precisamente eso "
         "antes de dibujarla: si la hora 25 no cayera donde tiene que caer, se "
         "negaría a escribir el fichero."),
    h("Por qué las cuatro horas propias están donde están"),
    p("Porque siete no divide a veinticuatro. Si el ciclo caldeo tiene siete "
      "puestos y el día tiene veinticuatro horas, el regente del día vuelve a "
      "tocar en la hora 1, la 8, la 15 y la 22 —de siete en siete—, y la 24 cae "
      "siempre dos puestos antes de cerrar la vuelta. Toda la irregularidad "
      "aparente del sistema viene de ese resto de tres, y una vez visto ya no se "
      "olvida."),
    ficha("Las cuatro horas propias de cada día", [
        ("Hora 1", "Al amanecer. La más usada de las cuatro y la más fácil de "
                   "situar sin cálculo."),
        ("Hora 8", "Media mañana o mediodía según la estación."),
        ("Hora 15", "Ya de noche: la tercera hora tras el atardecer."),
        ("Hora 22", "Noche cerrada. La que la tradición reserva para el trabajo "
                    "largo."),
    ]),
    nota("Y la honestidad de este capítulo",
         "Ninguna de estas horas tiene propiedad alguna. Lo que tiene es "
         "estructura: un reparto fijo, público y verificable que permite decidir "
         "cuándo se hace qué sin volver a decidirlo cada semana. Ese es el valor, "
         "y por eso este libro da la tabla completa en vez de insinuar que hay "
         "algo más."),
)

C24 = cap(
    "Las veintidós letras y sus números",
    p("El sistema occidental hereda de la cábala un alfabeto de veintidós letras "
      "que son a la vez signos, números y categorías. Es la pieza que permite pasar "
      "de una palabra a un número y de un número a un trazo sobre el cuadrado "
      "planetario, y sin ella el capítulo de los kameas queda a medias."),
    fig("am-alfabeto", "Lám. 8",
        "Las veintidós letras con su valor numérico y su correspondencia según el "
        "reparto tres-siete-doce. En amarillo las tres madres, en naranja las "
        "siete dobles y en gris las doce simples."),
    h("El reparto tres, siete y doce"),
    p("El «Sefer Yetsirá» —un texto brevísimo, de fecha discutida y en cualquier "
      "caso muy anterior al año 1000— divide las veintidós letras en tres grupos, "
      "y la división es de una economía notable: tres madres para los tres "
      "elementos que no son la tierra, siete dobles para los siete planetas y doce "
      "simples para los doce signos. Tres, siete y doce: exactamente las tres "
      "cifras sobre las que está construido todo lo demás en este libro."),
    ficha("Los tres grupos", [
        ("Tres madres", "Álef, Mem y Shin · Aire, Agua y Fuego. La tierra no "
                        "recibe letra: en este esquema es lo que resulta de las "
                        "otras tres, no un cuarto elemento."),
        ("Siete dobles", "Bet, Guímel, Dálet, Kaf, Pe, Resh y Tav · los siete "
                         "planetas. Se llaman dobles porque en hebreo admiten dos "
                         "pronunciaciones, una dura y una suave."),
        ("Doce simples", "Las doce restantes · los doce signos, en el orden de la "
                         "rueda, de He para Aries a Qof para Piscis."),
    ]),
    h("Los números"),
    p("Cada letra vale un número, y la serie es de una regularidad total: las nueve "
      "primeras van del uno al nueve, las nueve siguientes de diez en diez hasta "
      "el noventa, y las cuatro últimas de cien en cien hasta el cuatrocientos. "
      "Nueve unidades, nueve decenas, cuatro centenas: veintidós letras que cubren "
      "todo el sistema de numeración."),
    p("La suma de los veintidós valores es 1 495. Es un dato comprobable con una "
      "calculadora y sirve como verificación: si copias la tabla a tu diario y no "
      "te sale esa cifra, has copiado mal alguna fila."),
    h("Para qué sirve, en concreto"),
    pasos(
        "Escribe la palabra o el nombre de tu operación en letras hebreas "
        "transliteradas, o simplemente asigna a cada letra de tu alfabeto el "
        "valor de la letra hebrea equivalente. Lo segundo es menos ortodoxo y "
        "perfectamente utilizable.",
        "Suma los valores. Obtienes un número.",
        "Reduce ese número al rango del cuadrado del planeta con el que trabajas: "
        "si el cuadrado es de 3×3, los números van del 1 al 9; si es de 9×9, del "
        "1 al 81.",
        "Traza sobre el cuadrado la línea que une, en orden, los números de cada "
        "letra. Ese trazo es el sigilo de tu operación.",
    ),
    nota("Lo que este procedimiento es y lo que no",
         "Es una técnica de condensación: convierte una intención larga en un "
         "trazo corto que se puede mirar de un golpe. Funciona como ancla de "
         "memoria, y ya se dijo en el capítulo 9. Lo que no es: un procedimiento "
         "para obtener nombres verdaderos de nada, ni un sistema de "
         "correspondencias con valor demostrado. La gematría es un juego "
         "combinatorio muy antiguo y muy fértil, y tratado como juego rinde; "
         "tratado como prueba, no."),
)

C25 = cap(
    "Las escalas de los números",
    p("Cierro la parte de instrumentos con la tabla más ambiciosa de la tradición "
      "renacentista: la que ordena TODO por número. Agrippa la publicó en 1533 y "
      "es, en el fondo, la idea que sostiene el sistema entero — que las mismas "
      "cifras se repiten en todos los planos, y que reconocer la cifra es "
      "reconocer el plano."),
    h("La escala del uno al cuatro"),
    ficha("Las primeras cuatro", [
        ("Uno", "Lo indivisible. El punto, el centro del círculo, el operante. En "
                "la práctica: la intención única de cada sesión."),
        ("Dos", "La primera división y la primera tensión. La línea, el eje, lo "
                "diurno y lo nocturno, invocar y despedir."),
        ("Tres", "Lo que resuelve el dos. El triángulo, las tres madres, los tres "
                 "grupos del alfabeto. En la práctica: los tres movimientos de "
                 "cualquier rito —abrir, trabajar, cerrar—."),
        ("Cuatro", "La forma estable. El cuadrado, los cuatro cuartos, los cuatro "
                   "elementos, las cuatro armas, las cuatro semanas. Es el número "
                   "de este libro en casi todo lo práctico."),
    ]),
    h("Del cinco al siete"),
    ficha("Las tres siguientes", [
        ("Cinco", "El pentagrama: los cuatro elementos más quien los observa. El "
                  "número del capítulo 6 y del rito diario."),
        ("Seis", "El hexagrama y el equilibrio de contrarios: dos triángulos "
                 "entrelazados, seis puntas alrededor de un centro."),
        ("Siete", "Los planetas, los días, los metales, los cuadrados, el orden "
                  "caldeo. El número que estructura el tiempo en todo el sistema."),
    ]),
    h("Del ocho al doce"),
    ficha("Las últimas cinco", [
        ("Ocho", "Las fases de la Luna y el cuadrado de Mercurio. El número del "
                 "ciclo que se repite."),
        ("Nueve", "El cuadrado de la Luna y las nueve esferas de la cosmología "
                  "antigua. Tres veces tres: la forma cerrada."),
        ("Diez", "Las diez sefirot del árbol y el sistema decimal. El número de la "
                 "escala completa, de la abstracción al cuerpo."),
        ("Once", "El número sin sitio. No tiene figura, ni planeta, ni grupo. La "
                 "tradición lo trata como exceso del diez y defecto del doce, y "
                 "conviene fijarse en que la tabla tenga un hueco reconocido."),
        ("Doce", "Los signos, los meses, las horas de cada mitad del día, las "
                 "veinticuatro divisiones del ciclo. El número del año."),
    ]),
    nota("Cómo NO usar esta tabla",
         "Buscando en ella una explicación de por qué las cosas son como son. La "
         "escala de los números es una mnemotecnia magnífica y no es una física. "
         "Que el cuatro aparezca en los elementos, en los cuartos, en las armas y "
         "en las semanas no demuestra que haya una cuaternidad en la naturaleza: "
         "demuestra que quien construyó el sistema tenía criterio y lo aplicó de "
         "forma consistente. Reconocer eso no le quita valor al sistema; le quita "
         "la superstición, que es lo único que le sobraba."),
    h("Y para qué sirve de verdad"),
    p("Para navegar. Cuando en cualquier tratado clásico encuentres una lista de "
      "siete, ya sabes que estás en el registro planetario y del tiempo; una de "
      "cuatro, en el de los elementos y la forma; una de doce, en el del año. La "
      "escala convierte una biblioteca dispersa en un catálogo con signatura, y en "
      "eso —y solo en eso— es una herramienta de primer orden."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-invocaciones",
    "titulo": "Códice de las Invocaciones",
    "subtitulo": "Manual de práctica ritual: el círculo, las armas, los nombres y el trabajo sobre uno mismo",
    "autor": "Villumination 99",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-pentagrama",
    "acento": "oro",
    "original": True,
    "laminas": ["alta-magia.svg"],
    "claves": ["alta magia", "ritual", "pentagrama", "hexagrama", "cábala",
               "cuadrados mágicos", "atención", "villuminations"],
    "capitulos": [
        # I · Antes de empezar
        C1, C2, C3,
        # II · Los instrumentos
        C4, C5, C6, C7, C8, C9, C10, C23, C24, C25,
        # III · Las operaciones
        C11, C12, C13, C14, C15, C16, C17,
        # IV · El oficio sostenido
        C18, C19, C20, C21, C22,
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
          f"{palabras:,} palabras · → {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
