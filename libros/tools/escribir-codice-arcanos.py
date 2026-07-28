#!/usr/bin/env python3
"""
CÓDICE DE LOS ARCANOS — obra original de VILLUMINATION 99
=========================================================
Cuarto libro de la colección. Redacción propia sobre material de dominio
público: el patrón de Marsella (grabados del XVII y XVIII), el «Dogma y ritual
de la alta magia» de Éliphas Lévi (1856) y «El Tarot de los bohemios» de Papus
(1889), que son las dos obras que ataron el tarot a la cábala y a la
astrología.

No se reproduce ninguna baraja. Los arcanos se describen con palabras y se
representan con emblemas geométricos propios.

La parte de tablas se DEDUCE en tools/dibujar-arcanos.py y se importa aquí, de
modo que el texto y las láminas no puedan contradecirse: los 22 mayores toman
su letra por posición y de ella heredan su atribución; las 36 cartas del 2 al
10 toman su decanato por regla. Las dos deducciones se comprueban.

    python3 tools/escribir-codice-arcanos.py && python3 build.py arcanos
"""

import importlib.util
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"

# Se importa el generador de láminas para reutilizar sus tablas deducidas.
# Duplicarlas aquí sería garantizar que algún día el texto diga una cosa y el
# dibujo otra.
_spec = importlib.util.spec_from_file_location(
    "dibujar_arcanos", Path(__file__).with_name("dibujar-arcanos.py"))
_dib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_dib)
ARCANOS, MENORES = _dib.ARCANOS, _dib.MENORES
POR_NUMERO = {a[0]: a for a in ARCANOS}


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


def arcano(num, imagen, derecho, invertido, pregunta):
    """Un arcano mayor. La ficha se rellena con la deducción, no a mano."""
    n, nombre, letra, valor, clase, rige = POR_NUMERO[num]
    familia = {"madre": "madre · elemento", "doble": "doble · planeta",
               "simple": "simple · signo"}[clase]
    return [
        h(f"{n} · {nombre}"),
        ficha("", [
            ("Letra", f"{letra} · valor {valor} · {familia}"),
            ("Rige", rige),
            ("La lámina", imagen),
        ]),
        p(derecho),
        p(invertido),
        p(f"La pregunta: {pregunta}"),
    ]


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · ANTES DE LAS CARTAS
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "Lo que el tarot es",
    p("Este libro no va a decirte lo que te va a pasar, y conviene despacharlo en "
      "la primera línea porque es lo que casi todo el mundo espera de un libro de "
      "tarot."),
    h("La afirmación de este libro"),
    p("El tarot es un instrumento proyectivo. Setenta y ocho imágenes lo bastante "
      "ricas y lo bastante ambiguas como para que quien las mira encuentre en "
      "ellas su propia situación, y lo bastante fijas como para que no pueda "
      "encontrar cualquier cosa. Esa combinación —ambigüedad acotada— es "
      "exactamente lo que define un buen instrumento proyectivo, y es la razón "
      "por la que funciona."),
    p("Lo que ocurre en una tirada es que un asunto que estaba difuso se "
      "encuentra de golpe con un repertorio de figuras concretas, y al ponerle "
      "esas figuras se articula. No aparece información nueva sobre el mundo: "
      "aparece formulada la que ya tenías y no habías dicho. Es mucho, y no es "
      "adivinación."),
    h("Lo que este libro no afirma"),
    lista(
        "No afirma que las cartas informen del futuro. Nada de lo que sigue "
        "predice acontecimientos, y ninguna tirada de este libro está construida "
        "para intentarlo.",
        "No afirma que el orden en que salen las cartas esté determinado por algo. "
        "Un mazo barajado sale al azar, y el azar es precisamente lo que hace "
        "útil el instrumento: obliga a mirar figuras que uno no habría elegido.",
        "No afirma que el tarot venga de Egipto, ni de los gitanos, ni de ninguna "
        "sabiduría perdida. El capítulo 2 cuenta de dónde viene de verdad, con "
        "fechas.",
        "No sustituye consejo médico, psicológico, jurídico ni financiero. El "
        "capítulo 17 dice exactamente qué no se pregunta a un mazo, y va en serio.",
    ),
    nota("Por qué entonces conservar todo el aparato",
         "Porque el aparato es la mitad del instrumento. Las letras hebreas, los "
         "decanatos, los elementos, los números: todo eso no hace que las cartas "
         "adivinen nada, y sí hace que cada figura tenga un contorno preciso en "
         "vez de significar lo que a uno le convenga. Un tarot sin estructura es "
         "un test de manchas de tinta; con estructura es una lengua. La diferencia "
         "está en que la lengua se puede aprender mal y corregir."),
    sep(),
    h("De dónde sale lo que aquí se enseña"),
    p("Del patrón de Marsella, que son los grabados que se estabilizan en "
      "Francia entre el siglo XVII y el XVIII y que llevan siglos en dominio "
      "público; del «Dogma y ritual de la alta magia» de Éliphas Lévi, 1856, que "
      "es donde por primera vez los veintidós mayores se atan a las veintidós "
      "letras hebreas; y de «El Tarot de los bohemios» de Papus, 1889, que "
      "sistematiza ese atado. Los tres son libres."),
    p("Lo que aquí es propio: la redacción entera, la estructura, las lecturas de "
      "los setenta y ocho, las tres tiradas, el cuaderno y las cinco láminas. Y "
      "una cosa más, que es la que hace de esta colección un sistema y no cuatro "
      "libros sueltos: las tablas se deducen. Cada arcano mayor recibe su "
      "letra por posición y de la letra hereda su atribución; cada carta del dos "
      "al diez recibe su decanato por regla. Nada de eso está teclado a mano, y "
      "el generador de las láminas se niega a dibujar si alguna deducción no "
      "cierra."),
    nota("Cómo encaja con los otros tres Códices",
         "Las veintidós letras de los mayores son las mismas veintidós del Códice "
         "de las Invocaciones, con su mismo reparto de tres madres, siete dobles y "
         "doce simples. Los treinta y seis decanatos de las cartas menores son los "
         "mismos treinta y seis del Códice Zodiacal, con su mismo regente. Y el "
         "modo de leer una tirada sin identificarse con lo que sale es el trabajo "
         "del Códice del Sí Mismo. Los cuatro libros se pueden leer solos; leídos "
         "juntos, cada tabla confirma a las otras."),
)

C2 = cap(
    "La historia real",
    p("La historia que el tarot cuenta de sí mismo es falsa, y la verdadera es "
      "más interesante. Merece un capítulo porque saber de dónde viene una "
      "herramienta es parte de saber usarla."),
    h("Lo que dicen las fechas"),
    ficha("Cronología de lo comprobable", [
        ("Años 1440", "Aparecen en el norte de Italia —Milán, Ferrara, Bolonia— "
                      "los primeros mazos con cartas de triunfos añadidas a una "
                      "baraja corriente. Se llaman trionfi y son un juego de "
                      "cartas, caro y pintado a mano."),
        ("Siglo XVI", "El juego se difunde. La palabra «tarocchi» sustituye a "
                      "«trionfi». No hay una sola mención a adivinación en "
                      "doscientos años de documentos."),
        ("Siglos XVII–XVIII", "Se estabiliza en Francia el patrón que hoy llamamos "
                              "de Marsella: los mismos veintidós triunfos, con los "
                              "mismos nombres y en el mismo orden, grabados en "
                              "madera y baratos."),
        ("1781", "Antoine Court de Gébelin publica un ensayo donde afirma que el "
                 "tarot es un libro egipcio superviviente. No aporta ninguna "
                 "prueba. Es el momento en que nace todo lo demás."),
        ("1780–1790", "Etteilla convierte esa idea en oficio y publica el primer "
                      "método de lectura cartomántica."),
        ("1856", "Éliphas Lévi ata los veintidós mayores a las veintidós letras "
                 "hebreas. Es la aportación estructural decisiva, y es una "
                 "invención del siglo XIX, no una tradición antigua."),
        ("1889", "Papus sistematiza el conjunto en un libro que sigue siendo la "
                 "referencia continental."),
    ]),
    h("Las dos consecuencias de saber esto"),
    p("La primera es de honestidad: cualquiera que te venda el tarot como "
      "sabiduría milenaria egipcia está repitiendo, sin saberlo, una afirmación "
      "que un erudito francés hizo sin pruebas en 1781. Los mazos son europeos, "
      "renacentistas y empezaron siendo un juego de mesa."),
    p("La segunda es más útil y bastante liberadora: si la estructura simbólica "
      "del tarot se construyó en el siglo XIX, entonces es una construcción "
      "deliberada, hecha por gente que sabía lo que hacía y con un criterio que "
      "se puede examinar. Y una construcción examinable es infinitamente más "
      "utilizable que una revelación. Se puede aprender, discutir, y corregir "
      "donde falle."),
    nota("Lo que sí es antiguo",
         "El material con el que Lévi construyó. Las veintidós letras y su reparto "
         "vienen del «Sefer Yetsirá», anterior al año mil. Los cuatro elementos y "
         "los treinta y seis decanatos vienen de la astrología helenística, siglo "
         "II. Las figuras de los triunfos —la Muerte, la Rueda de la Fortuna, la "
         "Templanza— son iconografía medieval corriente, de la que había en "
         "iglesias y en libros. Antiguo es el material; moderno es el montaje. Y "
         "el montaje es bueno."),
)

C3 = cap(
    "La estructura de las setenta y ocho",
    p("Antes de una sola lectura, la arquitectura. Un mazo de tarot no son setenta "
      "y ocho cartas sueltas: son dos sistemas encajados, y confundirlos es el "
      "primer error del principiante."),
    fig("ar-estructura", "Lám. 1",
        "Las setenta y ocho. Arriba, los veintidós mayores como serie única. "
        "Abajo, los cuatro palos, cada uno con su as, sus nueve numerales y sus "
        "cuatro figuras."),
    ficha("Los dos sistemas", [
        ("22 arcanos mayores", "Una serie numerada de I a XXI más El Loco. No hay "
                               "palos ni repeticiones: cada uno es único y ocupa "
                               "un lugar en un itinerario."),
        ("56 arcanos menores", "Cuatro palos de catorce cartas: as, del dos al "
                               "diez, y cuatro figuras. Estructura de baraja "
                               "corriente, con una figura más."),
    ]),
    h("Qué hace cada mitad"),
    p("Los mayores hablan de procesos: etapas, umbrales, cambios de estado. Son "
      "pocos y grandes, y cuando salen en una tirada indican que lo que está en "
      "juego no es una circunstancia sino un tramo del camino."),
    p("Los menores hablan de circunstancias: lo concreto, lo cotidiano, lo que "
      "está pasando esta semana en un área identificable de la vida. Son muchos y "
      "pequeños, y por eso una tirada de solo menores describe una situación y una "
      "tirada cargada de mayores describe un momento."),
    nota("La proporción como dato de lectura",
         "Con veintidós mayores en setenta y ocho cartas, la proporción esperada es "
         "de algo menos de tres por cada diez. Si en una tirada de diez cartas "
         "salen seis mayores, eso ya es información antes de leer ninguna: el "
         "asunto es más de fondo de lo que la pregunta suponía. Y si en una "
         "pregunta que parecía vital no sale ninguno, también: probablemente no era "
         "tan vital."),
    h("El número de cartas y por qué es ese"),
    p("Veintidós no es casual: son las letras del alfabeto hebreo, y ese encaje "
      "es lo que Lévi encontró y lo que hizo del tarot un sistema. Cincuenta y "
      "seis tampoco: son cuatro veces catorce, y catorce es diez más cuatro — las "
      "diez etapas del número y las cuatro figuras. El total, setenta y ocho, es "
      "además la suma de los doce primeros números, que es la clase de "
      "coincidencia que a los constructores del sistema les encantaba y que no "
      "significa nada por sí misma."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LOS VEINTIDÓS MAYORES
# ══════════════════════════════════════════════════════════════════════

C4 = cap(
    "Los mayores y sus letras",
    p("El capítulo que explica de dónde salen las fichas de los cuatro siguientes. "
      "Es la parte técnica y merece leerse antes, porque después ya no se explica "
      "otra vez."),
    fig("ar-mayores", "Lám. 2",
        "Los veintidós con su letra, su valor numérico y lo que rige. El color "
        "dice de qué clase es la letra: amarillo las tres madres, naranja las "
        "siete dobles, azul las doce simples."),
    h("El reparto que este libro usa"),
    p("El arcano I va con la primera letra, el II con la segunda, y así hasta el "
      "XXI con la vigesimoprimera. El Loco, que no lleva número o lleva el cero, "
      "cierra la serie con la letra que queda. Es el reparto de Lévi y de Papus, "
      "el continental, y se elige por dos razones: es el más antiguo de los dos "
      "que existen, y encaja exactamente con el reparto de tres madres, siete "
      "dobles y doce simples que ya trae el Códice de las Invocaciones."),
    p("Ese encaje es lo que hace que cada arcano herede una atribución sin que "
      "nadie tenga que decidirla: tres de los veintidós rigen un elemento, siete "
      "rigen un planeta y doce rigen un signo. No se asigna: se deduce."),
    ficha("Los tres mayores elementales", [
        ("I · El Mago", "Álef · el Aire. El primero de la serie rige el elemento "
                        "del aliento y de la palabra, que es lo que hace un mago."),
        ("XIII · El Arcano sin Nombre", "Mem · el Agua. El arcano de la "
                                        "transformación rige el elemento que "
                                        "disuelve."),
        ("XXI · El Mundo", "Shin · el Fuego. El último numerado rige el elemento "
                           "que consuma."),
    ]),
    nota("El otro reparto, y por qué no se usa aquí",
         "La tradición inglesa de finales del XIX empieza la serie por El Loco con "
         "la primera letra y corre todo lo demás un puesto, además de intercambiar "
         "la Justicia y la Fuerza entre el VIII y el XI. Es un sistema coherente y "
         "muy extendido, y si has aprendido con él todo lo de este libro sigue "
         "siendo utilizable: solo cambia la columna de la letra. Lo que no se "
         "puede es mezclar los dos, y por eso aquí se elige uno y se mantiene de "
         "principio a fin. Este libro usa el orden de Marsella: la Justicia en el "
         "VIII y la Fuerza en el XI."),
    h("Cómo leer las fichas de los capítulos siguientes"),
    lista(
        "«Letra» da el nombre, el valor numérico y la clase. El valor sirve para "
        "la gematría del Códice de las Invocaciones; la clase, para saber qué "
        "familia de atribución le toca.",
        "«Rige» es el elemento, planeta o signo heredado. No es un adorno: es lo "
        "que conecta el arcano con las tablas de los otros libros.",
        "«La lámina» describe con palabras la imagen del patrón de Marsella. Se "
        "describe y no se reproduce, porque este libro dibuja lo suyo.",
        "Después van tres párrafos: lo que dice la carta derecha, lo que dice "
        "invertida, y la pregunta que plantea. La pregunta es la parte útil.",
    ),
)

C5 = cap(
    "Del I al VI · la salida",
    p("Los seis primeros arcanos describen el equipo con el que se sale: la "
      "capacidad de obrar, la de saber, la de crear, la de ordenar, la de "
      "aprender y la de elegir."),
    *arcano("I",
            "Un hombre de pie ante una mesa con objetos dispares, una mano "
            "arriba y otra abajo.",
            "Derecho: tienes los medios y todavía no has empezado. Es la carta del "
            "que puede, y por eso es la más incómoda de las veintidós: no admite "
            "la excusa de la falta de recursos. La mesa está puesta.",
            "Invertido: habilidad sin dirección. Mucho talento repartido en "
            "demasiadas cosas, o destreza usada para quedar bien en vez de para "
            "hacer. También el charlatán, que es el mago que se quedó en el "
            "gesto.",
            "¿Qué es lo que ya podrías hacer hoy con lo que tienes en la mesa?"),
    *arcano("II",
            "Una figura sentada, un libro entreabierto sobre el regazo, entre dos "
            "columnas.",
            "Derecho: hay algo que sabes y no has dicho, o que sabrías si te "
            "quedaras quieto un rato. Es la carta del saber que no se exhibe y del "
            "que espera el momento. Frente al Mago, que actúa, ella lee.",
            "Invertido: reserva convertida en secreto inútil. Guardar por costumbre "
            "lo que ya no hay motivo para guardar, o confundir el silencio con la "
            "profundidad.",
            "¿Qué sabes de esto que no has puesto en palabras todavía?"),
    *arcano("III",
            "Una mujer sentada con cetro y escudo, mirando a un lado.",
            "Derecho: algo está creciendo y hay que atenderlo. Es la carta de lo "
            "fértil y de lo que se hace cuidando, no forzando. También la "
            "abundancia concreta: lo que hay, no lo que se espera.",
            "Invertido: crecimiento sin cauce, o cuidado que asfixia. La "
            "sobreprotección de un proyecto o de una persona hasta impedirle "
            "crecer solo.",
            "¿Qué está creciendo aquí, y lo estoy atendiendo o lo estoy vigilando?"),
    *arcano("IV",
            "Un hombre sentado de perfil, con las piernas cruzadas y un cetro.",
            "Derecho: hace falta estructura y hace falta ya. Un marco, un límite, "
            "una decisión que ordene lo que está disperso. Es la carta menos "
            "poética del mazo y una de las más necesarias.",
            "Invertido: rigidez, o autoridad sostenida por costumbre y no por "
            "criterio. El marco que se levantó para proteger algo y ahora lo "
            "impide.",
            "¿Qué necesita aquí una estructura, y quién la va a poner?"),
    *arcano("V",
            "Una figura con mitra y bastón, dos personas más pequeñas ante ella.",
            "Derecho: hay algo que aprender de alguien, o algo que transmitir. Es "
            "la carta de la enseñanza y del marco compartido — la tradición, la "
            "regla, lo que se hereda. Salida en una tirada, suele señalar que "
            "conviene consultar antes de decidir.",
            "Invertido: dogma. Repetir una regla porque es la regla, o buscar un "
            "maestro para no tener que decidir. También el guía que se ha "
            "acostumbrado a que le crean.",
            "¿A quién debería preguntar, y qué me impide preguntarle?"),
    *arcano("VI",
            "Un joven entre dos figuras, y arriba una tercera con un arco.",
            "Derecho: hay que elegir, y elegir es perder una de las dos. No es la "
            "carta del amor: es la del cruce de caminos, y en el patrón de "
            "Marsella el joven está literalmente mirando hacia un lado.",
            "Invertido: la elección que no se toma. Quedarse en el cruce por no "
            "renunciar a nada, que es la manera más costosa de renunciar a las "
            "dos.",
            "¿Cuál es la elección que llevo tiempo sin tomar, y qué pierdo con cada "
            "opción?"),
)

C6 = cap(
    "Del VII al XII · la prueba",
    p("Los seis siguientes ya no son equipo: son las pruebas. Lo que ocurre cuando "
      "el camino se pone en marcha y deja de depender de lo que uno traía."),
    *arcano("VII",
            "Un hombre coronado sobre un carro tirado por dos caballos que van "
            "hacia lados distintos.",
            "Derecho: se avanza, y se avanza tirando de dos fuerzas que no van del "
            "todo en la misma dirección. Es la carta del control conseguido con "
            "esfuerzo y del avance que hay que sostener a mano.",
            "Invertido: el carro se para o se desvía. Fuerzas internas que van a lo "
            "suyo, o victoria conseguida y no aprovechada.",
            "¿Cuáles son las dos fuerzas que estoy tirando a la vez, y hacia dónde "
            "va cada una?"),
    *arcano("VIII",
            "Una mujer sentada, espada en una mano y balanza en la otra.",
            "Derecho: hay que medir y hay que decidir con lo medido. Es la carta de "
            "la consecuencia: lo que se hizo tiene efectos y toca contarlos. "
            "También el acuerdo justo, el contrato, lo que se pone por escrito.",
            "Invertido: la balanza torcida. Juzgar sin datos, o pedir justicia "
            "esperando que coincida con lo que uno quiere.",
            "¿Estoy midiendo esto de verdad, o estoy buscando que me dé la razón?"),
    *arcano("IX",
            "Un anciano encapuchado con un farol y un bastón, caminando.",
            "Derecho: toca retirarse un tramo. No para huir: para ver. Es la carta "
            "del que lleva su propia luz y avanza despacio, y suele salir cuando "
            "hace falta menos consulta y más silencio.",
            "Invertido: aislamiento. La retirada que dejó de ser instrumento y se "
            "volvió domicilio, con la superioridad que suele acompañarla.",
            "¿Qué vería de esto si me apartara una semana?"),
    *arcano("X",
            "Una rueda con figuras que suben por un lado y bajan por el otro.",
            "Derecho: esto cambia y no depende de ti. Es la carta del ciclo y del "
            "azar, y su lección es de las duras: hay un tramo del asunto que solo "
            "admite esperar bien. Enlaza directamente con el capítulo del Códice "
            "del Sí Mismo sobre lo que no depende de nosotros.",
            "Invertido: pelearse con la rueda. Empujar contra un ciclo, o "
            "atribuirse el mérito de una subida que era del propio giro.",
            "¿Qué parte de esto está girando sola, y qué estoy haciendo para "
            "frenarla?"),
    *arcano("XI",
            "Una mujer que abre con las manos la boca de un león, sin violencia "
            "aparente.",
            "Derecho: la fuerza que sirve aquí no es la que golpea. Es la de "
            "sostener sin ceder y sin pelear, día tras día. La carta de la "
            "constancia y del dominio de lo propio que no necesita demostrarse.",
            "Invertido: fuerza empleada en dominar lo que no se puede, o "
            "contención que ya es represión. También la blandura que se llama "
            "paciencia.",
            "¿Qué estoy intentando someter en vez de sostener?"),
    *arcano("XII",
            "Un hombre suspendido por un pie de una viga, cabeza abajo y "
            "tranquilo.",
            "Derecho: la espera con sentido. Es la carta del cambio de punto de "
            "vista conseguido pagando la incomodidad de quedarse quieto en una "
            "postura difícil. Nada avanza, y eso es lo correcto ahora.",
            "Invertido: sacrificio inútil. Aguantar por aguantar, o quedarse "
            "colgado esperando un rescate que no depende de nadie. También el "
            "mártir, que es el colgado que ha empezado a cobrar.",
            "¿Esta espera está haciendo algo, o solo me está costando?"),
)

C7 = cap(
    "Del XIII al XVIII · el paso",
    p("El tramo difícil. Seis arcanos que describen lo que se derrumba, lo que se "
      "ordena después y lo que se ve mal en la oscuridad."),
    *arcano("XIII",
            "Un esqueleto con una hoz que siega. En el patrón de Marsella esta "
            "carta va sin nombre escrito.",
            "Derecho: algo se acaba, y acabarse es su función. No es la carta de la "
            "muerte física: es la del corte, la del final que despeja. Que en "
            "Marsella no lleve nombre es la mejor pista sobre cómo leerla.",
            "Invertido: el final que no se deja ocurrir. Sostener con vida algo que "
            "ya terminó, con el coste que eso tiene. También el miedo al cambio "
            "convertido en régimen.",
            "¿Qué se ha terminado aquí y sigo tratando como vivo?"),
    *arcano("XIV",
            "Una figura con alas que trasvasa líquido entre dos vasijas sin "
            "derramar nada.",
            "Derecho: mezclar bien y en la proporción justa. Después del corte "
            "viene el trabajo fino de recomponer, y se hace despacio. Es la carta "
            "de la medida y de la paciencia técnica.",
            "Invertido: la mezcla que no cuaja, o el exceso disfrazado de "
            "equilibrio. También la tibieza, que no es templanza sino falta de "
            "criterio.",
            "¿En qué proporción tendría que estar esto, y en cuál está?"),
    *arcano("XV",
            "Una figura cornuda sobre un pedestal, con dos figuras menores "
            "atadas a él por el cuello con cuerdas flojas.",
            "Derecho: hay un apego que ata, y la cuerda está floja. Es la carta más "
            "malinterpretada del mazo: no habla del mal, habla de lo que uno "
            "sostiene sabiendo que le sujeta. Lo que la hace incómoda es la "
            "cuerda: se podría quitar.",
            "Invertido: la atadura empieza a soltarse, o se está negando que "
            "exista. Y el modo más eficaz de negarla es hablar mucho de la "
            "libertad.",
            "¿A qué estoy atado con una cuerda que podría quitarme, y qué gano "
            "quedándome?"),
    *arcano("XVI",
            "Una torre de la que caen dos figuras, alcanzada desde arriba.",
            "Derecho: lo que estaba construido sobre un supuesto falso se cae, y "
            "se cae de golpe. Es una carta dura y no es una carta mala: lo que se "
            "derrumba aquí se habría derrumbado igual más tarde y más caro.",
            "Invertido: el derrumbe se ha aplazado apuntalando la torre. Funciona, "
            "y cada apuntalamiento encarece el final.",
            "¿Qué estoy apuntalando que se va a caer de todos modos?"),
    *arcano("XVII",
            "Una figura desnuda arrodillada junto al agua, vertiendo dos "
            "cántaros, con estrellas encima.",
            "Derecho: después de la torre, esto. Es la carta de la reparación "
            "lenta y sin público: se vacía lo que se tenía, se deja correr, y "
            "vuelve la orientación. La más serena de las veintidós.",
            "Invertido: esperanza sin trabajo, o el desánimo que se instala cuando "
            "la reparación no va tan rápido como se querría.",
            "¿Qué tendría que vaciar aquí para que empiece a correr algo?"),
    *arcano("XVIII",
            "Dos perros aullando a la luna junto a un estanque del que sale un "
            "cangrejo, entre dos torres.",
            "Derecho: la percepción no es fiable ahora. Es la carta de lo que se "
            "ve mal a media luz: miedos que se agrandan, intuiciones que aciertan "
            "y no se pueden justificar, memoria que reescribe. No se decide bajo "
            "esta carta; se aguarda.",
            "Invertido: la niebla se levanta, o se está tomando por evidencia lo "
            "que era imaginación. En una tirada sobre otra persona, invertida "
            "suele señalar que la información que tienes es de segunda mano.",
            "¿Qué de esto sé, y qué me estoy imaginando?"),
)

C8 = cap(
    "Del XIX al XXI y el Loco · la salida",
    p("Los tres últimos numerados y el que no tiene número. Lo que hay después del "
      "paso, y el que vuelve a empezar."),
    *arcano("XIX",
            "Dos figuras juntas bajo un sol con rostro y rayos rectos.",
            "Derecho: se ve claro y se ve con otro. Es la carta de lo evidente "
            "compartido: el asunto se entiende, se puede decir en voz alta y no "
            "hace falta explicarlo. Después de la Luna, es el amanecer literal.",
            "Invertido: claridad convertida en exhibición, o luz que deslumbra y "
            "no deja ver el detalle. También la alegría que no admite matices.",
            "¿Qué está claro aquí que todavía no he dicho en voz alta?"),
    *arcano("XX",
            "Figuras que se levantan del suelo al son de una trompeta que suena "
            "desde arriba.",
            "Derecho: hay una llamada y hay que responder. Es la carta de la "
            "decisión que se venía posponiendo y del despertar que no se elige. "
            "Suele salir cuando el asunto ya está resuelto por dentro y falta "
            "actuar.",
            "Invertido: la llamada que se oye y no se atiende. Y su forma más "
            "común: reconocer que hay que hacer algo y ponerse a estudiar el tema "
            "un poco más.",
            "¿Qué es lo que ya sé que tengo que hacer?"),
    *arcano("XXI",
            "Una figura dentro de una corona de laurel, con las cuatro imágenes "
            "de los evangelistas en las esquinas.",
            "Derecho: está completo. Los cuatro elementos en las cuatro esquinas y "
            "el centro ocupado: el trabajo se cierra y el cierre se nota en el "
            "mundo concreto. Es la carta de lo terminado y de lo integrado.",
            "Invertido: el cierre que no llega, o el que se declara antes de "
            "tiempo. También la obra acabada que no se suelta.",
            "¿Qué falta exactamente para poder dar esto por cerrado?"),
    *arcano("0",
            "Un caminante con un hatillo al hombro y un perro que le muerde la "
            "pierna, andando sin mirar.",
            "Derecho: se echa a andar sin garantías y sin número. El Loco no está "
            "en la serie: la atraviesa. Es la carta del comienzo que no se "
            "justifica, de la libertad sin sitio fijo y del que no sabe todavía "
            "en qué se está metiendo — que es la única forma de meterse en algo "
            "nuevo.",
            "Invertido: irresponsabilidad. Empezar sin mirar por costumbre, o "
            "convertir la falta de compromiso en identidad.",
            "¿Qué empezaría si no tuviera que justificarlo ante nadie?"),
    sep(),
    nota("El itinerario completo, en una línea",
         "Del I al VI se reúne el equipo; del VII al XII se pone a prueba; del "
         "XIII al XVIII se derrumba y se recompone; del XIX al XXI se cierra. Y El "
         "Loco entra y sale por donde quiere, que es lo que significa no tener "
         "número. Cuando una tirada trae varios mayores, ese orden dice en qué "
         "tramo del recorrido está el asunto — y suele ser un tramo antes del que "
         "el consultante creía."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · LOS CINCUENTA Y SEIS MENORES
# ══════════════════════════════════════════════════════════════════════

C9 = cap(
    "Los cuatro palos",
    p("Los menores se organizan por palos, y cada palo es un elemento y una "
      "facultad. Sabiendo eso, la mitad del significado de cada carta ya está "
      "puesta antes de mirar el número."),
    fig("ar-palos", "Lám. 3",
        "Los cuatro palos con su elemento y sus cuatro figuras. Cada figura "
        "lleva además su propio elemento dentro del palo, y de ahí salen las "
        "dieciséis combinaciones."),
    ficha("Los cuatro palos", [
        ("Bastos · Fuego", "La voluntad y la empresa. Lo que se emprende, se "
                           "impulsa y se defiende. Área de la vida: proyectos, "
                           "trabajo propio, iniciativa."),
        ("Copas · Agua", "El sentimiento y el vínculo. Lo que se siente, se "
                         "recuerda y se comparte. Área: relaciones, familia, "
                         "estados de ánimo."),
        ("Espadas · Aire", "El pensamiento y la palabra. Lo que se decide, se "
                           "discute y se corta. Área: decisiones, conflictos, "
                           "comunicación."),
        ("Oros · Tierra", "El cuerpo y lo concreto. Lo que se sostiene, se "
                          "produce y se cuenta. Área: dinero, salud, casa, "
                          "trabajo por cuenta ajena."),
    ]),
    nota("La discusión de las Espadas",
         "Hay una disputa vieja sobre si las Espadas son Aire o Fuego, y los "
         "Bastos lo contrario. El argumento de los que las hacen Fuego es que la "
         "espada se forja; el de los que las hacen Aire —que es el mayoritario "
         "desde el XIX y el que este libro usa— es que la espada corta y "
         "distingue, que es lo que hace el pensamiento. Se dice aquí porque si "
         "lees otro libro y no coincide, ahora sabes por qué."),
    h("Las cuatro figuras y el elemento dentro del elemento"),
    p("Cada palo tiene cuatro figuras, y cada figura lleva su propio elemento. "
      "El Rey es el fuego del palo, la Reina su agua, el Caballo su aire y la "
      "Sota su tierra. De ahí salen dieciséis combinaciones que describen "
      "maneras de estar en un área, no personas."),
    ficha("Cómo se lee una figura", [
        ("Rey", "Fuego del palo. Manda y decide en esa área. La versión que "
                "dirige."),
        ("Reina", "Agua del palo. Sostiene y nutre esa área desde dentro. La "
                  "versión que cuida."),
        ("Caballo", "Aire del palo. Se mueve, viaja, lleva y trae. La versión que "
                    "actúa hacia fuera."),
        ("Sota", "Tierra del palo. Aprende, empieza, recibe. La versión que "
                 "estudia."),
    ]),
    p("El Rey de Oros es el fuego de la tierra: quien dirige lo concreto. La Sota "
      "de Espadas es la tierra del aire: quien está aprendiendo a pensar. Con las "
      "dos coordenadas —palo y figura— las dieciséis se deducen y no hay que "
      "memorizarlas."),
    nota("Las figuras no son personas",
         "El error más común con las dieciséis es leerlas como «alguien». A veces "
         "lo son, y casi siempre son un modo de estar: el consultante actuando "
         "como Sota cuando le tocaría actuar como Rey, o como Rey cuando debería "
         "estar aprendiendo. Preguntar «quién es esta carta» cierra la lectura; "
         "preguntar «desde dónde estoy actuando» la abre."),
)

C10 = cap(
    "Los ases y las diez etapas",
    p("Los cuatro ases y la escala del uno al diez, que es lo que convierte "
      "cuarenta cartas en un sistema en vez de una lista."),
    h("Los cuatro ases"),
    p("El as no es el número uno: es el elemento puro, la raíz del palo antes de "
      "manifestarse en nada concreto. Salido en una tirada, indica que el asunto "
      "está en su origen y todavía no tiene forma — y que la tiene disponible."),
    ficha("Los cuatro orígenes", [
        ("As de Bastos", "Fuego en bruto. Un impulso que aún no es proyecto. La "
                         "gana."),
        ("As de Copas", "Agua en bruto. Un sentimiento antes de tener objeto. La "
                        "apertura."),
        ("As de Espadas", "Aire en bruto. Una idea antes de argumento. La "
                          "claridad que corta."),
        ("As de Oros", "Tierra en bruto. Un recurso antes de gastarse. La "
                       "posibilidad material."),
    ]),
    h("Las diez etapas del número"),
    p("Del dos al diez, cada número describe una etapa del mismo proceso, "
      "independientemente del palo. Aprendida la escala una vez, sirve para las "
      "treinta y seis."),
    ficha("La escala, del dos al diez", [
        ("Dos", "La primera relación y la primera tensión. Dos cosas frente a "
                "frente: equilibrio o elección."),
        ("Tres", "Lo que resuelve el dos: aparece un tercero, una síntesis, un "
                 "resultado inicial."),
        ("Cuatro", "La estabilidad conseguida. Se consolida, y con ella empieza el "
                   "riesgo de acomodarse."),
        ("Cinco", "La rotura. El cuatro se quiebra porque tenía que quebrarse: es "
                  "el número de la crisis en los cuatro palos."),
        ("Seis", "La recomposición después del cinco. Se recupera el equilibrio, "
                 "ya con información."),
        ("Siete", "La prueba individual. Hay que sostener solo lo recuperado, y "
                  "aparece la tentación de soltarlo."),
        ("Ocho", "El movimiento y el oficio. Se trabaja, se acelera, se hace "
                 "cantidad."),
        ("Nueve", "El resultado casi cerrado, con lo que ha costado a la vista. El "
                  "número más ambivalente de la escala."),
        ("Diez", "El final del ciclo: colmado o agotado, según el palo. Lo que "
                 "sigue ya es otro as."),
    ]),
    nota("La utilidad real de la escala",
         "Que los cincos son crisis en los cuatro palos y los dieces son finales "
         "en los cuatro. Cuando en una tirada salen dos cincos, no hace falta "
         "saber nada más para decir que el asunto está en su punto de rotura. La "
         "escala es lo que permite leer una carta que no recuerdas: número más "
         "palo, y sale."),
)

C11 = cap(
    "Las treinta y seis y sus decanatos",
    p("Aquí está la pieza que ata este libro al Códice Zodiacal y la que da al "
      "tarot su capa más fina de precisión. Las treinta y seis cartas del dos al "
      "diez no son treinta y seis significados sueltos: son los treinta y seis "
      "decanatos del zodiaco, uno por carta, sin sobrar ni faltar ninguno."),
    fig("ar-decanatos", "Lám. 4",
        "Las treinta y seis. Cada fila es un signo con sus tres tramos de diez "
        "grados, y en cada tramo la carta que le corresponde. Ni una carta "
        "repetida, ni un decanato vacío."),
    h("La regla, que es lo bonito del asunto"),
    p("El reparto no hay que memorizarlo porque se deduce con dos criterios."),
    pasos(
        "El palo lo da el elemento del signo. Aries es Fuego, así que sus tres "
        "decanatos son de Bastos. Tauro es Tierra: Oros. Y así los doce.",
        "El trío de números lo da la modalidad. Los signos cardinales toman el "
        "dos, el tres y el cuatro; los fijos el cinco, el seis y el siete; los "
        "mutables el ocho, el nueve y el diez.",
        "Dentro del signo, el primer decanato va al primer número del trío, el "
        "segundo al segundo y el tercero al tercero.",
        "Y el regente de cada decanato sale del orden caldeo empezando en Marte, "
        "exactamente igual que en el Códice Zodiacal.",
    ),
    ficha("Un ejemplo entero", [
        ("Aries", "Fuego cardinal → Bastos, trío 2-3-4"),
        ("2 de Bastos", "Aries 0° a 10° · regente Marte · el impulso sin filtro"),
        ("3 de Bastos", "Aries 10° a 20° · regente Sol · el impulso con dirección"),
        ("4 de Bastos", "Aries 20° a 30° · regente Venus · el impulso que busca "
                        "compañía"),
    ]),
    nota("Por qué esto cierra sin sobrar nada",
         "Cuatro elementos por tres modalidades son doce signos, y ninguna casilla "
         "se repite. Doce signos por tres decanatos son treinta y seis. Cuatro "
         "palos por nueve números —del dos al diez— son también treinta y seis. "
         "Las dos rejillas tienen el mismo tamaño y encajan una en otra sin "
         "hueco. Que encajen no es una casualidad afortunada: es que quien montó "
         "el sistema en el siglo XIX contó primero."),
    h("Qué se gana leyendo así"),
    p("Precisión, y un puente. El seis de Copas dejará de ser «nostalgia» —que es "
      "lo que dicen la mayoría de los manuales— y será Escorpio en su segundo "
      "decanato, regido por el Sol: la intensidad con propósito. Es una lectura "
      "más específica, más difícil de estirar a conveniencia y con una tabla "
      "detrás que se puede comprobar."),
    p("Y el puente funciona en los dos sentidos. Si trabajas con el Códice "
      "Zodiacal, cada decanato tiene ahora una carta que lo representa; si "
      "trabajas con el tarot, cada carta menor tiene ahora treinta grados de "
      "zodiaco y un planeta regente detrás. Los dos libros se leen mejor juntos, "
      "y eso es deliberado."),
    nota("Y la honestidad de siempre",
         "Esta correspondencia es una construcción del siglo XIX, elegante y "
         "coherente, y no la revelación de un vínculo real entre unos cartones y "
         "unos grados de cielo. Su valor es el de cualquier buen sistema de "
         "clasificación: da a cada elemento un lugar único y permite razonar. Con "
         "eso basta y es mucho."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE IV · LA LECTURA
# ══════════════════════════════════════════════════════════════════════

C12 = cap(
    "Cómo se lee de verdad",
    p("El capítulo que la mayoría de los manuales se salta, porque explica el "
      "mecanismo y explicarlo parece quitarle magia. Ocurre lo contrario: "
      "entendido el mecanismo, la lectura mejora mucho."),
    h("Lo que pasa en una tirada"),
    pasos(
        "Se formula una pregunta. El solo hecho de tener que formularla ya obliga "
        "a concretar un asunto que estaba difuso, y una parte del rendimiento de "
        "la tirada se produce aquí, antes de tocar el mazo.",
        "Se saca un número fijo de cartas en posiciones con significado asignado. "
        "El azar aporta las figuras; la estructura de la tirada aporta el papel de "
        "cada una.",
        "Se mira lo que sale y se busca cómo encaja. Este es el paso donde ocurre "
        "el trabajo: la mente proyecta la situación sobre la figura y, al hacerlo, "
        "articula lo que sabía y no había dicho.",
        "Se dice en voz alta o se escribe. Sin este paso la tirada se disuelve: lo "
        "que no se formula no queda.",
    ),
    h("Por qué el azar es imprescindible"),
    p("Porque el valor del instrumento está en que te ponga delante figuras que "
      "no habrías elegido. Si eligieras las cartas, elegirías las que confirman "
      "lo que ya piensas — y no habría tirada, habría un espejo. El azar es lo "
      "que garantiza la incomodidad, y la incomodidad es lo que produce el "
      "hallazgo."),
    nota("La objeción obvia, respondida",
         "«Si es azar, entonces cualquier carta serviría para cualquier cosa.» No: "
         "eso pasaría si las cartas no tuvieran contorno. El aparato de este libro "
         "—letras, elementos, decanatos, escala del número— existe precisamente "
         "para que cada figura signifique algo bastante concreto y no admita "
         "cualquier lectura. Cuando una carta no encaja con lo que quieres oír, la "
         "estructura te impide estirarla, y ahí es donde el instrumento hace su "
         "mejor trabajo."),
    h("Las tres reglas del que lee bien"),
    lista(
        "Se lee lo que hay, no lo que se esperaba. Si la tirada no dice nada, se "
        "dice que no dice nada. Un lector que siempre encuentra un mensaje está "
        "fabricándolos.",
        "Se lee el conjunto antes que las cartas. Cuántos mayores, qué palos "
        "dominan, qué números se repiten: eso dice más que cualquier carta "
        "individual, y se ve en cinco segundos.",
        "Se termina en una acción concreta. Una tirada que acaba en una "
        "interpretación bonita no ha servido. Una que acaba en «voy a decirle esto "
        "a esta persona esta semana», sí.",
    ),
)

C13 = cap(
    "Las tiradas",
    p("Tres tiradas, diseñadas para este libro y pensadas para lo que el "
      "instrumento sí hace. Ninguna de las tres pregunta por el futuro."),
    fig("ar-tiradas", "Lám. 5",
        "Las tres disposiciones con el orden en que se saca cada carta."),
    h("Las Tres"),
    p("La básica, tres cartas en fila. Es la que se usa el noventa por ciento de "
      "las veces y la que conviene dominar antes de cualquier otra."),
    ficha("Las Tres · posiciones", [
        ("1 · Qué había", "El punto de partida real del asunto, no el que se "
                          "cuenta."),
        ("2 · Qué hay", "La situación tal como está ahora."),
        ("3 · Qué falta", "Lo que no se ha puesto todavía. No lo que pasará: lo "
                          "que falta."),
    ]),
    h("La Cruz de Cuatro"),
    p("Para cuando hay una decisión que tomar y no se avanza. La tercera posición "
      "es la que suele resolver la tirada."),
    ficha("La Cruz de Cuatro · posiciones", [
        ("1 · El hecho", "Al centro. Qué está pasando de verdad, sin "
                         "interpretación."),
        ("2 · Lo que aporto", "Arriba. Con qué cuento en esto."),
        ("3 · Lo que estorba", "A la izquierda. Y suele ser algo propio."),
        ("4 · El paso", "Abajo. La acción concreta que toca ahora."),
    ]),
    h("El Espejo"),
    p("La más incómoda y la más útil en conflictos con otra persona. Tres cartas."),
    ficha("El Espejo · posiciones", [
        ("1 · Como lo veo", "Mi versión del asunto."),
        ("2 · Como lo ve el otro", "Su versión. Esta carta se lee entera antes de "
                                   "discutirla."),
        ("3 · Lo que ninguno ve", "El punto ciego compartido. Es la posición que "
                                  "justifica la tirada."),
    ]),
    nota("Sobre la segunda posición del Espejo",
         "No informa de lo que la otra persona piensa: no hay manera de que un "
         "mazo sepa eso. Lo que hace es obligarte a construir su versión con "
         "material que no has elegido, y eso produce un ejercicio de perspectiva "
         "que la reflexión espontánea casi nunca produce. Es la misma técnica del "
         "triángulo de examen del Códice de las Invocaciones, con otras "
         "herramientas."),
    h("La regla del número de cartas"),
    p("Pocas. Tres o cuatro para casi todo, y nunca más de siete. Una tirada de "
      "diez u once cartas da tanta información que se puede construir con ella "
      "cualquier relato, y ahí se pierde el instrumento. La restricción es lo que "
      "obliga a la precisión — la misma razón por la que un buen diagnóstico usa "
      "pocas pruebas bien elegidas."),
)

C14 = cap(
    "La carta invertida",
    p("Un capítulo corto sobre una cuestión que divide a los lectores y que "
      "conviene resolver antes de empezar, porque hay que elegir y mantenerse."),
    h("Las dos escuelas"),
    ficha("Con inversiones y sin ellas", [
        ("Con inversiones", "Cada carta tiene dos lecturas según su orientación. "
                            "Duplica el vocabulario a 156 posiciones y afina "
                            "mucho, a costa de complicar el aprendizaje."),
        ("Sin inversiones", "Todas las cartas se leen derechas y el matiz lo dan "
                            "las cartas vecinas. Más simple, y algunos lectores "
                            "muy buenos no usan otra cosa."),
    ]),
    p("Este libro trabaja con inversiones, y da la lectura invertida de los "
      "veintidós mayores en los capítulos 5 al 8. Se elige así porque una carta "
      "invertida obliga a mirar el lado incómodo de la figura, y ese lado es "
      "justo el que un lector complaciente se salta."),
    h("Las cuatro formas de leer una inversión"),
    lista(
        "El exceso. La misma cualidad pasada de punto: la Fuerza que ya es "
        "terquedad, la Templanza que ya es tibieza. Es la lectura más frecuente y "
        "la que casi siempre funciona.",
        "El defecto. La cualidad que falta o no llega: el Emperador invertido como "
        "ausencia de estructura.",
        "El bloqueo. La energía de la carta existe y no circula. Muy útil en "
        "posiciones de «lo que estorba».",
        "La interioridad. Lo que la carta describe está ocurriendo por dentro y no "
        "se ha manifestado. Es la lectura menos usada y la más fina.",
    ),
    nota("La regla para no hacer trampas",
         "Elige de antemano cuál de las cuatro lecturas vas a usar en esa tirada y "
         "no la cambies a mitad. Si se permite elegir la que encaje mejor con cada "
         "carta, la inversión deja de significar nada: se convierte en un comodín. "
         "Anotar en el cuaderno qué lectura se usó es lo que permite comprobar, "
         "meses después, si se estaba leyendo o improvisando."),
)

C15 = cap(
    "Los errores del lector",
    p("Predecibles, y los ocho cuestan años cada uno."),
    pasos(
        "Memorizar setenta y ocho significados. No hace falta y no funciona: con "
        "el palo, el número y la escala del capítulo 10 se deducen casi todos. "
        "Quien memoriza no sabe leer, sabe recitar.",
        "Preguntar por el futuro. Es lo que el instrumento no hace, y forzarlo "
        "produce lecturas que no se pueden comprobar — con lo cual nunca se "
        "aprende de los errores.",
        "Repetir la tirada. Sacar otras cartas porque las primeras no gustaron. Es "
        "el equivalente de repetir un análisis hasta que salga bien, y es la señal "
        "más clara de que no se estaba preguntando: se estaba pidiendo permiso.",
        "Leer para otros antes de saber leer para uno. Trescientas tiradas propias "
        "y registradas antes de tocar el asunto de nadie. Sin excepción.",
        "Encontrar siempre un mensaje. Hay tiradas que no dicen nada, y decirlo es "
        "lo que separa un lector de un adivino. La honestidad de admitirlo es la "
        "credencial del oficio.",
        "Interpretar sin mirar el conjunto. Se cuentan los mayores, se ve qué palo "
        "domina y qué números se repiten ANTES de leer una sola carta.",
        "No cerrar en una acción. Una tirada sin acción concreta al final es "
        "entretenimiento con vocabulario esotérico.",
        "No escribir. Sin cuaderno no hay manera de saber si tus lecturas se "
        "sostienen, y por tanto no hay manera de mejorar. Llevas años leyendo, no "
        "aprendiendo.",
    ),
    nota("La prueba de realidad",
         "Coge diez tiradas de hace seis meses de tu cuaderno y léelas sin mirar "
         "lo que anotaste. Si tu interpretación de hoy no se parece a la de "
         "entonces, estabas improvisando. Si se parece, tienes un método. Es una "
         "prueba desagradable y es la única que existe."),
)

C16 = cap(
    "Lo que no se pregunta",
    p("El capítulo de ética del oficio, y el más importante del libro si alguna "
      "vez lees para otra persona. Son cinco prohibiciones y ninguna es "
      "negociable."),
    ficha("Las cinco", [
        ("Salud", "No se diagnostica, no se pronostica y no se opina sobre un "
                  "tratamiento. Nunca. Si alguien te consulta por un síntoma, la "
                  "respuesta es una sola frase: eso lo mira un médico."),
        ("Muerte", "No se pregunta cuándo va a morir nadie, ni el consultante ni un "
                   "tercero. El arcano XIII no habla de eso y tú tampoco."),
        ("Terceros ausentes", "No se lee sobre la intimidad de quien no está "
                              "presente ni ha dado su permiso. Lo que sí se puede "
                              "leer es la posición del consultante respecto a esa "
                              "persona, que es distinto y bastante más útil."),
        ("Asuntos legales y dinero", "No se aconseja sobre un pleito, un contrato "
                                     "o una inversión. Eso lo miran un abogado y "
                                     "un asesor, y equivocarse ahí tiene "
                                     "consecuencias que un lector no puede "
                                     "asumir."),
        ("Embarazo y decisiones irreversibles", "No se toca. Ninguna decisión que "
                                                "no se pueda deshacer se apoya en "
                                                "una tirada."),
    ]),
    h("Y una sexta, sobre el estado del consultante"),
    p("Si quien consulta está en crisis aguda —duelo reciente, ruptura de días, "
      "ansiedad alta, pensamientos de hacerse daño— no se le lee. No porque el "
      "tarot sea peligroso, sino porque en ese estado cualquier figura ambigua se "
      "lee del peor modo posible, y porque lo que esa persona necesita es otra "
      "cosa y tú se lo estás retrasando. La respuesta correcta es acompañar y "
      "señalar hacia ayuda profesional."),
    nota("Cómo se dice un no",
         "Sin misterio y sin dárselas de nada: «esto no se lee con cartas». Si "
         "insisten, se repite igual. Un lector que acepta cualquier pregunta para "
         "no decepcionar acaba haciendo daño, y lo hará sin enterarse — porque las "
         "consecuencias de una mala lectura casi nunca vuelven al que la hizo."),
    ritual(
        "La regla que resume las seis:",
        "el tarot sirve para ordenar lo que el consultante ya sabe.",
        "Nunca para sustituir lo que no sabe",
        "y tiene que preguntarle a otro.",
    ),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE V · EL OFICIO
# ══════════════════════════════════════════════════════════════════════

C17 = cap(
    "El cuaderno de tiradas",
    p("Si de este libro solo conservas una práctica, conserva esta. Es lo mismo "
      "que dicen los otros tres Códices y por el mismo motivo: sin registro "
      "escrito no hay forma de saber si algo funciona."),
    h("Por qué en el tarot importa más que en nada"),
    p("Porque la lectura de cartas es el terreno más fértil que existe para el "
      "autoengaño. Una tirada ambigua interpretada a posteriori siempre parece "
      "haber acertado: la memoria selecciona lo que encajó y descarta lo demás sin "
      "avisar. El cuaderno es el único antídoto, y funciona por una razón muy "
      "simple: lo escrito antes no se puede reescribir después."),
    ficha("Entrada por tirada", [
        ("Fecha y hora", "____________"),
        ("La pregunta", "Textual, tal como se formuló. Sin arreglarla luego"),
        ("Tirada", "Las Tres · Cruz de Cuatro · El Espejo · otra"),
        ("Las cartas", "Por posición, con su orientación"),
        ("El conjunto", "Cuántos mayores · qué palo domina · números repetidos"),
        ("La lectura", "Cuatro líneas como máximo. Si no cabe en cuatro, no la "
                       "tenías clara"),
        ("La acción", "Lo que voy a hacer en los próximos siete días"),
        ("Revisión", "Se deja EN BLANCO. Se rellena a las cuatro semanas"),
    ]),
    nota("La casilla de revisión es todo el método",
         "Cuatro semanas después se vuelve a la entrada y se anota, sin piedad, "
         "qué pasó: si la acción se hizo, si la lectura resultó pertinente o si "
         "fue un adorno. Cincuenta entradas con su revisión rellenada valen más "
         "que quinientas tiradas sin ella, y son la única forma de descubrir que "
         "hay cartas que llevas años leyendo mal."),
    h("La revisión trimestral"),
    pasos(
        "Cuenta las tiradas hechas y las revisiones rellenadas. El segundo número "
        "es el que importa.",
        "Cuenta cuántas acciones se ejecutaron de verdad. Por debajo de la mitad, "
        "no estás leyendo: estás consultando.",
        "Busca la carta que más te ha salido. Casi siempre hay una, y casi siempre "
        "señala un asunto que llevas sin resolver.",
        "Busca la lectura que resultó más equivocada y anota por qué. Este punto es "
        "el que produce el aprendizaje.",
    ),
)

C18 = cap(
    "El año de práctica",
    p("Un plan de doce meses. Es voluntario y es mejor que improvisar."),
    ficha("Los cuatro trimestres", [
        ("Meses 1–3", "Solo los veintidós mayores, apartados del resto del mazo. "
                      "Una carta al día, sacada por la mañana, leída en tres "
                      "líneas y revisada por la noche. Noventa entradas."),
        ("Meses 4–6", "Se añaden los cuatro palos con la escala del número. Una "
                      "tirada de Las Tres por semana, con revisión a cuatro "
                      "semanas."),
        ("Meses 7–9", "Se añaden los decanatos: cada carta menor se lee también "
                      "por su signo y su regente. Aquí es donde el Códice "
                      "Zodiacal se vuelve necesario."),
        ("Meses 10–12", "No se añade nada. Se sostiene, se revisa el año y se "
                        "releen las primeras noventa entradas. Ese último "
                        "ejercicio es el que enseña."),
    ]),
    h("Los tres indicadores"),
    pasos(
        "Revisiones rellenadas frente a tiradas hechas. Por encima del setenta por "
        "ciento hay práctica.",
        "Acciones ejecutadas frente a acciones anotadas. Es la medida de si el "
        "instrumento está sirviendo para algo.",
        "Coincidencia entre tu lectura de hoy y la de hace seis meses sobre la "
        "misma tirada. Es la medida de si tienes método o improvisas.",
    ),
    nota("Y la advertencia del segundo año",
         "El riesgo no es abandonar: es la fluidez. Cuando las setenta y ocho se "
         "leen sin esfuerzo, la tentación es leer rápido y bonito, y ahí la "
         "estructura empieza a estorbar y se abandona sin darse cuenta. La señal "
         "de alarma es dejar de contar los mayores antes de interpretar. Cuando "
         "llegues ahí, vuelve al capítulo 12 y a la casilla de revisión."),
)

C19 = cap(
    "Vocabulario",
    p("Los términos de este libro, para poder leer cualquier otro tratado sin "
      "perderse."),
    ficha("A – E", [
        ("Arcano", "Cada una de las setenta y ocho cartas. Mayor si pertenece a la "
                   "serie de veintidós; menor si pertenece a un palo."),
        ("As", "La primera carta de cada palo. No es el número uno: es el elemento "
               "puro, antes de forma."),
        ("Cartomancia", "Lectura de cartas con fines de adivinación. Se nombra aquí "
                        "para distinguirla: no es lo que este libro enseña."),
        ("Decanato", "Tramo de diez grados de un signo. Hay treinta y seis, y a "
                     "cada uno le corresponde una carta del dos al diez."),
        ("Escala del número", "La secuencia de significados del dos al diez, común "
                              "a los cuatro palos."),
    ]),
    ficha("F – P", [
        ("Figura", "Sota, Caballo, Reina o Rey. Cuatro por palo, dieciséis en "
                   "total."),
        ("Gematría", "Suma de los valores numéricos de las letras de una palabra. "
                     "Se desarrolla en el Códice de las Invocaciones."),
        ("Inversión", "Carta que sale del revés. Se lee como exceso, defecto, "
                      "bloqueo o interioridad — elegido de antemano."),
        ("Marsella", "Patrón de grabados francés estabilizado entre el XVII y el "
                     "XVIII. El que este libro sigue. Justicia en el VIII, Fuerza "
                     "en el XI."),
        ("Numeral", "Carta del dos al diez de un palo. Hay treinta y seis."),
        ("Palo", "Bastos, Copas, Espadas u Oros. Cada uno un elemento y un área de "
                 "la vida."),
        ("Proyectivo", "Instrumento cuya utilidad consiste en que quien lo mira "
                       "proyecte su propia situación sobre una imagen ambigua "
                       "pero acotada. Es lo que el tarot es."),
    ]),
    ficha("Q – Z", [
        ("Regente del decanato", "Planeta que rige un tramo de diez grados. Sale "
                                 "del orden caldeo empezando en Marte."),
        ("Reparto 3-7-12", "División de las veintidós letras en tres madres, siete "
                           "dobles y doce simples. De él heredan los mayores su "
                           "atribución."),
        ("Tirada", "Disposición de un número fijo de cartas en posiciones con "
                   "significado asignado."),
        ("Triunfos", "Nombre original de los arcanos mayores en los mazos "
                     "italianos del siglo XV. De ahí «tarocchi» y «tarot»."),
    ]),
    sep(),
    p("Y con esto se cierra el cuarto Códice. Cuatro libros: la rueda del año, el "
      "oficio del rito, la observación de sí y las setenta y ocho. Cuatro "
      "lenguajes distintos para la misma tarea, que es mirarse con algo más de "
      "precisión de la que se tiene por defecto."),
    p("Ninguno de los cuatro promete nada, y eso es a propósito. Lo que ofrecen es "
      "estructura donde había intuición, y un cuaderno para comprobar si la "
      "estructura sirve. Con eso, quien practique de verdad averiguará cosas sobre "
      "sí mismo que no sabía. Y quien no practique tendrá cuatro libros bonitos, "
      "que también es un destino digno pero es otro."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-arcanos",
    "titulo": "Códice de los Arcanos",
    "subtitulo": "Las setenta y ocho cartas como instrumento de lectura: los veintidós mayores, los cuatro palos y los treinta y seis decanatos",
    "autor": "Villumination 99",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-arcano",
    "acento": "carmin",
    "original": True,
    "laminas": ["arcanos.svg"],
    "claves": ["tarot", "arcanos mayores", "Marsella", "decanatos", "cábala",
               "Éliphas Lévi", "Papus", "villuminations"],
    "capitulos": [
        C1, C2, C3,                      # I · Antes de las cartas
        C4, C5, C6, C7, C8,              # II · Los veintidós mayores
        C9, C10, C11,                    # III · Los cincuenta y seis menores
        C12, C13, C14, C15, C16,         # IV · La lectura
        C17, C18, C19,                   # V · El oficio
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
          f"{palabras:,} palabras · 22 mayores y 36 decanatos deducidos · "
          f"→ {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
