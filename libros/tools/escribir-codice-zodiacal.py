#!/usr/bin/env python3
"""
CÓDICE ZODIACAL — obra original de VILLUMINATIONS
====================================================
Aquí se escribe el libro. No es texto extraído de ningún PDF: es redacción
propia sobre material tradicional (las correspondencias astrológicas clásicas
tienen siglos y no son propiedad de nadie), ampliada con la vertiente de
cuerpo y hábito que es lo que diferencia a esta obra.

Editar este archivo y ejecutar:
    python3 tools/escribir-codice-zodiacal.py && python3 build.py codice
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
def fechas(t):   return {"t": "fechas", "x": t}


def fig(simbolo, tit, pie, clase=""):
    """Lámina del repertorio gráfico (ver tools/dibujar-zodiaco.py)."""
    return {"t": "figura", "x": simbolo, "tit": tit, "pie": pie, "clase": clase}


def cap(titulo, *bloques, medallon=None):
    d = {"titulo": titulo, "bloques": [b for b in bloques if b]}
    if medallon:
        d["medallon"] = medallon
    return d


# ── Los treinta y seis decanatos ──────────────────────────────────────
# Reparto clásico: los siete planetas en orden caldeo (del más lento al más
# rápido) recorren los 36 tramos de diez grados empezando en Marte, que es el
# regente del primer decanato de Aries. La cuenta no cierra en múltiplo de
# siete y por eso la serie va desfasándose signo a signo: no es un error de la
# tradición, es la propia mecánica del reparto.
CALDEO = ["Saturno", "Júpiter", "Marte", "Sol", "Venus", "Mercurio", "Luna"]

DECANATOS = {}
_i = CALDEO.index("Marte")
for _s in ("aries tauro geminis cancer leo virgo libra escorpio sagitario "
           "capricornio acuario piscis").split():
    DECANATOS[_s] = [CALDEO[(_i + _k) % 7] for _k in range(3)]
    _i = (_i + 3) % 7


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · FUNDAMENTOS
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "Antes de abrir la rueda",
    p("Este libro no te va a decir lo que va a pasar. Va a hacer algo más útil: "
      "darte un lenguaje para observarte."),
    p("La astrología tradicional que aquí se recoge es un sistema simbólico con "
      "más de dos mil años de historia. Nació como una forma de ordenar el año, "
      "el cuerpo y el carácter en doce categorías reconocibles, y sobrevivió "
      "porque esas categorías describen bien las tensiones humanas de siempre: el "
      "impulso y la paciencia, la palabra y el silencio, la entrega y el límite. "
      "Es un mapa del temperamento, no un horario del futuro."),
    h("Lo que este libro sí es"),
    lista(
        "Un tratado de los doce signos con sus correspondencias clásicas completas: "
        "elemento, modalidad, polaridad, regente, metal, piedra, color y zona "
        "corporal.",
        "Un retrato psicológico honesto de cada signo, con sus fuerzas y con sus "
        "sombras — porque un signo sin sombra es publicidad, no descripción.",
        "La tabla completa de los treinta y seis decanatos, con fechas y regente, "
        "que es la parte del sistema que explica por qué tanta gente no se reconoce "
        "en la descripción general de su signo.",
        "Las cuatro dignidades esenciales signo por signo, con el grado exacto de "
        "cada exaltación y de cada caída.",
        "Los sesenta términos egipcios —cinco tramos desiguales por signo— que son "
        "la tabla más fina y más olvidada del sistema clásico.",
        "La división en veintiocho mansiones lunares, con su aritmética exacta y "
        "con una explicación honesta de por qué las listas de nombres no coinciden "
        "entre tradiciones.",
        "La precesión de los equinoccios con sus cifras reales, la diferencia "
        "entre zodiaco tropical y sidéreo y de dónde salen las «eras».",
        "La doctrina de la secta —cartas de día y de noche— que la astrología "
        "helenística usaba y la moderna dejó caer.",
        "La melotesia: el reparto tradicional del cuerpo entre los doce signos, "
        "desarrollado signo a signo como doce zonas de mantenimiento.",
        "La geometría de la rueda —oposición, trígono, cuadratura, sextil— y los "
        "seis ejes de signos opuestos explicados uno por uno.",
        "El sistema de días y horas planetarias, con la aritmética que explica de "
        "dónde salió el orden de la semana que usas todos los días.",
        "Una vertiente de mesa y de hábito que casi ningún tratado desarrolla, "
        "escrita en clave de compensación de patrones y no de superstición.",
        "Un programa de doce meses de trabajo interior, con una práctica concreta "
        "por signo, el ciclo lunar como armazón y un registro para escribir lo que "
        "observas.",
        "Siete láminas dibujadas para este libro y un vocabulario final para poder "
        "leer cualquier otro tratado sin perderse.",
    ),
    h("Lo que este libro no es"),
    p("No es un manual de predicción, no calcula cartas natales y no promete "
      "resultados. Tampoco es un texto médico ni psicológico: cuando en estas "
      "páginas se habla del cuerpo, se habla de hábitos de cuidado, no de "
      "diagnósticos ni de tratamientos. Si algo te duele, la respuesta está en una "
      "consulta, no en un signo."),
    nota("Cómo leerlo",
         "Puedes leerlo entero de una vez para tener el mapa completo, o ir directo "
         "a tu signo. Pero el mayor provecho está en el uso que propone la tercera "
         "parte: recorrer los doce signos a lo largo de un año, un mes cada uno, "
         "trabajando la cualidad que le corresponde. Nadie es solo su signo solar; "
         "todos llevamos los doce dentro, unos desarrollados y otros dormidos."),
    sep(),
    p("Una última advertencia, y va en serio. Si usas este sistema para justificarte "
      "—«soy así porque soy Escorpio»— lo has convertido en una jaula y habrás "
      "perdido el tiempo. El signo describe la materia prima con la que trabajas, "
      "no la sentencia. Todo lo que sigue está escrito para lo contrario: para que "
      "reconozcas tu patrón y luego decidas qué haces con él."),
)

C2 = cap(
    "La rueda y sus cuatro elementos",
    p("La rueda zodiacal no es una lista de doce categorías sueltas. Es una "
      "estructura con tres clasificaciones que se cruzan, y entender ese cruce vale "
      "más que memorizar los doce signos por separado."),
    h("Los cuatro elementos: la materia del temperamento"),
    p("Cada signo pertenece a un elemento, y el elemento describe de qué está hecha "
      "su energía antes de cualquier otra consideración."),
    ficha("Los cuatro elementos", [
        ("Fuego", "Aries, Leo, Sagitario · Impulso, iniciativa, entusiasmo, calor"),
        ("Tierra", "Tauro, Virgo, Capricornio · Forma, constancia, resultado, cuerpo"),
        ("Aire", "Géminis, Libra, Acuario · Idea, relación, palabra, distancia"),
        ("Agua", "Cáncer, Escorpio, Piscis · Emoción, memoria, vínculo, profundidad"),
    ]),
    fig("dia-casillas", "Lám. 4",
        "Las doce casillas: cuatro elementos por tres modalidades. Ninguna "
        "combinación se repite, y ahí está la razón de que el sistema funcione "
        "como clasificación."),
    p("Los elementos se ordenan en dos parejas naturales. Fuego y Aire son "
      "expansivos: salen hacia fuera, se comunican, se gastan rápido. Tierra y Agua "
      "son receptivos: acumulan, conservan, tardan en moverse y tardan en parar. "
      "Casi todos los conflictos de convivencia que verás descritos en este libro "
      "salen de esa diferencia de ritmo, no de mala voluntad."),
    h("Las tres modalidades: cómo se mueve esa energía"),
    ficha("Las tres modalidades", [
        ("Cardinal", "Aries, Cáncer, Libra, Capricornio · Inician. Abren estación"),
        ("Fijo", "Tauro, Leo, Escorpio, Acuario · Sostienen. Mantienen el centro"),
        ("Mutable", "Géminis, Virgo, Sagitario, Piscis · Adaptan. Cierran y transforman"),
    ]),
    p("La modalidad explica por qué dos signos del mismo elemento se comportan de "
      "forma tan distinta. Aries, Leo y Sagitario son los tres de Fuego, pero Aries "
      "enciende, Leo mantiene la llama y Sagitario la reparte. El elemento dice "
      "«qué»; la modalidad dice «cómo»."),
    h("Las dos polaridades: hacia dónde apunta"),
    p("La tercera clasificación alterna signo a signo alrededor de la rueda. Los "
      "signos de Fuego y Aire se llaman tradicionalmente activos o diurnos: su "
      "movimiento natural va del interior hacia el mundo. Los de Tierra y Agua son "
      "receptivos o nocturnos: su movimiento va del mundo hacia el interior."),
    nota("El cruce es lo que individualiza",
         "Doce signos = cuatro elementos × tres modalidades. Ninguna combinación se "
         "repite, y por eso el sistema funciona como clasificación: cada signo es el "
         "único que ocupa su casilla. Capricornio es el único Tierra Cardinal, "
         "Escorpio el único Agua Fijo. Cuando dudes de la naturaleza de un signo, "
         "reconstruye su casilla y saldrá solo."),
    sep(),
    h("La rueda como año y como proceso"),
    p("La secuencia de los doce signos describe un ciclo completo, y esa es la clave "
      "que convierte el zodiaco en herramienta de trabajo. Empieza en Aries con el "
      "impulso puro —la semilla que rompe la tierra—, gana cuerpo en Tauro, se hace "
      "consciente en Géminis, se interioriza en Cáncer. Llega a su expresión plena en "
      "Leo, se depura en Virgo, se abre al otro en Libra, se transforma en Escorpio. "
      "Busca sentido en Sagitario, lo estructura en Capricornio, lo comparte en "
      "Acuario y lo disuelve en Piscis para que Aries pueda volver a empezar."),
    fig("dia-rueda", "Lám. 5",
        "La rueda completa. Anillo exterior: los doce signos con su glifo y su "
        "color de elemento. Anillo intermedio: la modalidad (C, F, M). Anillo "
        "interior: el sigilo del planeta regente. En el centro, los cuatro "
        "elementos en cruz."),
    p("Leído así, el zodiaco deja de ser una etiqueta de nacimiento y se convierte en "
      "un itinerario. Es exactamente el uso que propone la tercera parte de este libro."),
)

C3 = cap(
    "Los siete regentes tradicionales",
    p("Antes del telescopio, la astrología trabajaba con los siete cuerpos visibles a "
      "ojo desnudo. Este libro se mantiene en ese sistema clásico por una razón "
      "práctica: es coherente, cerrado y directamente utilizable, y las "
      "correspondencias de metal, piedra y órgano que verás en cada capítulo están "
      "construidas sobre él."),
    ficha("Los siete y lo que gobiernan", [
        ("Sol", "Leo · Oro · Identidad, vitalidad, corazón"),
        ("Luna", "Cáncer · Plata · Memoria, ritmo, estómago"),
        ("Mercurio", "Géminis y Virgo · Azogue · Palabra, análisis, sistema nervioso"),
        ("Venus", "Tauro y Libra · Cobre · Valor, vínculo, riñón y garganta"),
        ("Marte", "Aries y Escorpio · Hierro · Impulso, deseo, sangre y músculo"),
        ("Júpiter", "Sagitario y Piscis · Estaño · Sentido, expansión, hígado"),
        ("Saturno", "Capricornio y Acuario · Plomo · Límite, tiempo, hueso y piel"),
    ]),
    fig("dia-regentes", "Lám. 6",
        "Los siete regentes en orden caldeo, de Saturno —el más lento en su "
        "recorrido aparente— a la Luna. A la derecha, los signos que gobierna cada "
        "uno. Este orden manda también en los decanatos y en las horas planetarias."),
    h("Por qué cada planeta gobierna dos signos"),
    p("El Sol y la Luna gobiernan un signo cada uno: son los dos luminares y no se "
      "reparten. Los otros cinco gobiernan dos, uno de naturaleza diurna y otro "
      "nocturna, y esa doble regencia explica parentescos que de otro modo parecen "
      "arbitrarios."),
    lista(
        "Mercurio en Géminis habla y conecta; en Virgo ordena y depura. La misma "
        "inteligencia, primero hacia fuera y luego hacia dentro.",
        "Venus en Tauro disfruta y posee; en Libra armoniza y comparte. El mismo "
        "sentido del valor, primero en la materia y luego en la relación.",
        "Marte en Aries ataca de frente; en Escorpio persiste en silencio. La misma "
        "fuerza, primero visible y luego subterránea.",
        "Júpiter en Sagitario busca horizonte; en Piscis busca compasión. El mismo "
        "impulso de sentido, primero hacia lo lejano y luego hacia lo profundo.",
        "Saturno en Capricornio construye estructuras; en Acuario las cuestiona. El "
        "mismo rigor, primero para levantar y luego para revisar.",
    ),
    nota("Una nota de honestidad",
         "La astrología moderna asignó Urano a Acuario, Neptuno a Piscis y Plutón a "
         "Escorpio. Es una tradición válida y muy extendida, pero rompe la simetría "
         "del sistema de siete y complica las correspondencias corporales. Aquí se "
         "usa el esquema clásico. Si trabajas con el moderno, todo lo que sigue sigue "
         "siendo compatible: solo añade una capa más."),
)

C4 = cap(
    "Los treinta y seis decanatos",
    p("Aquí empieza la parte del sistema que casi ningún libro divulgativo "
      "explica, y que sin embargo resuelve la objeción más común que se le hace a "
      "la astrología: «no me parezco a mi signo»."),
    p("La respuesta tradicional es que un signo no es un bloque uniforme. Ocupa "
      "treinta grados de la rueda, y esos treinta grados se dividen en tres tramos "
      "de diez que se llaman decanatos —o, en los tratados antiguos, «caras». Cada "
      "tramo tiene un planeta al frente que matiza el signo sin cambiar su "
      "naturaleza. Un Tauro de la primera cara y un Tauro de la tercera comparten "
      "elemento, modalidad y regente, y se comportan de forma perceptiblemente "
      "distinta."),
    h("Cómo se reparten"),
    p("El reparto no es arbitrario: sigue el orden caldeo, la secuencia de los "
      "siete planetas ordenados del más lento al más rápido en su recorrido "
      "aparente. Saturno, Júpiter, Marte, Sol, Venus, Mercurio, Luna. La serie "
      "arranca en Marte, que rige el primer decanato de Aries, y desde ahí avanza "
      "un paso por cada tramo de diez grados, dando la vuelta cuando se agota."),
    nota("Por qué la serie se desfasa",
         "Treinta y seis decanatos y siete planetas: 36 no es múltiplo de 7. La "
         "serie no cierra, y por eso cada signo empieza con un planeta distinto al "
         "que le tocaría si el reparto fuera regular. No es un error de "
         "transmisión: es la mecánica del propio reparto, y es la razón de que la "
         "tabla haya que aprenderla y no deducirla."),
    fig("dia-decanos", "Lám. 1",
        "Los treinta y seis decanatos. Cada fila es un signo; cada columna, un "
        "tramo de diez grados con el planeta que lo rige. La serie recorre el "
        "orden caldeo sin interrupción de Aries a Piscis."),
    h("Cómo usar tu decanato"),
    pasos(
        "Localiza tu signo por la fecha de nacimiento.",
        "Dentro del capítulo de tu signo, busca la sección «Los tres decanatos» y "
        "encuentra el tramo que contiene tu fecha.",
        "Lee la descripción general del signo y luego el matiz del decanato. El "
        "primero te da el material; el segundo, el acabado.",
        "Si tu fecha cae en el límite de dos tramos —el día exacto del cambio—, "
        "lee los dos. La frontera es real pero no es un tabique: quien nace en ella "
        "suele reconocerse en ambos.",
    ),
    nota("Una advertencia honesta",
         "El sistema de decanatos que aquí se usa es el de las «caras» "
         "planetarias, el más antiguo y el más extendido en la tradición "
         "occidental. Existen otros repartos —por ejemplo, asignar cada decanato "
         "al signo siguiente del mismo elemento— y son igual de legítimos. Este "
         "libro elige uno y lo mantiene coherente de principio a fin, que es la "
         "única forma de que un sistema simbólico sirva para algo."),
)

C5 = cap(
    "La geometría de la rueda",
    p("Los signos no se leen de uno en uno. Lo que la tradición observó desde el "
      "principio es que la posición relativa de dos puntos de la rueda dice tanto "
      "como los puntos mismos, y que esas relaciones se pueden medir en grados. Son "
      "los aspectos, y son la gramática con la que el zodiaco pasa de vocabulario a "
      "lengua."),
    p("Para lo que este libro propone —trabajar los doce signos como cualidades— "
      "los aspectos importan por una razón muy práctica: explican por qué algunas "
      "cualidades te resultan fáciles de sumar y otras entran siempre en conflicto."),
    fig("dia-aspectos", "Lám. 2",
        "Los cuatro aspectos mayores dibujados sobre la rueda de doce. La figura "
        "geométrica no es un adorno: es la relación misma."),
    h("La oposición · 180°"),
    p("Dos signos enfrentados, seis casillas de distancia. Comparten modalidad y "
      "tienen elementos complementarios —Fuego con Aire, Tierra con Agua—, de modo "
      "que la tensión nunca es de incompatibilidad sino de dirección: los dos "
      "empujan con la misma fuerza hacia lados contrarios."),
    p("Las seis oposiciones del zodiaco forman los seis ejes, y cada capítulo de "
      "signo lleva el suyo explicado. Si tuvieras que quedarte con una sola idea de "
      "este capítulo, quédate con esta: tu signo opuesto no es tu enemigo, es la "
      "mitad de tu propia pregunta que tú no formulas."),
    h("El trígono · 120°"),
    p("Cuatro casillas de distancia: mismo elemento. Es la relación más fluida de "
      "la rueda, y también la más peligrosa por comodidad. Entre signos del mismo "
      "elemento no hay traducción que hacer, así que tampoco hay aprendizaje "
      "obligado. Aries, Leo y Sagitario se entienden sin explicarse — y ninguno de "
      "los tres frena a los otros dos."),
    h("La cuadratura · 90°"),
    p("Tres casillas: misma modalidad, elementos que no se llevan. Es el roce "
      "clásico. Dos signos cardinales quieren dirigir a la vez, dos fijos se "
      "plantan en direcciones distintas, dos mutables cambian de plan sin avisarse. "
      "La tradición la llama aspecto «duro», y la palabra es exacta: es el aspecto "
      "que obliga a crecer porque no se puede resolver ignorándolo."),
    h("El sextil · 60°"),
    p("Dos casillas: elementos afines de la misma polaridad —Fuego con Aire, Tierra "
      "con Agua—. Se llevan bien pero no se confunden, y por eso es el aspecto más "
      "productivo del zodiaco: hay afinidad suficiente para colaborar y diferencia "
      "suficiente para aportar algo. La tradición lo describe como una oportunidad "
      "que hay que tomar; el matiz importa, porque el sextil no actúa solo."),
    sep(),
    ficha("Resumen de los cuatro aspectos", [
        ("Oposición · 180°", "6 casillas · Misma modalidad, elementos complementarios · Tensión fértil"),
        ("Trígono · 120°", "4 casillas · Mismo elemento · Fluidez, riesgo de comodidad"),
        ("Cuadratura · 90°", "3 casillas · Misma modalidad, elementos discordes · Roce que obliga"),
        ("Sextil · 60°", "2 casillas · Elementos afines · Oportunidad si se toma"),
        ("Conjunción · 0°", "Misma casilla · Refuerzo. Suma de intensidad, no de matiz"),
    ]),
    nota("Cómo aprovecharlo sin carta natal",
         "Este libro no calcula cartas. Pero los aspectos se pueden usar sin "
         "calcular nada: cuando una de las doce prácticas te resulte "
         "insoportablemente ajena, mira qué relación guarda con tu signo. Si es "
         "cuadratura u oposición, tienes la explicación — y también la confirmación "
         "de que esa es precisamente la práctica que más te va a servir."),
)

C6 = cap(
    "El zodiaco del cuerpo",
    p("Hay una tradición dentro de la tradición que merece un capítulo propio, "
      "porque es la más antigua y la más olvidada: el reparto del cuerpo humano "
      "entre los doce signos. Los tratados la llaman melotesia, y aparece en los "
      "textos griegos, en los médicos árabes y en prácticamente todos los "
      "almanaques europeos hasta el siglo XVIII."),
    p("El orden es de una sencillez que da que pensar: los signos se reparten el "
      "cuerpo de la cabeza a los pies, en el mismo orden en que ocupan la rueda. "
      "Aries la cabeza, Piscis los pies, y los diez restantes descendiendo por el "
      "cuerpo sin saltarse un tramo."),
    fig("dia-cuerpo", "Lám. 3",
        "La melotesia: los doce signos repartidos del vértice del cráneo a la "
        "planta del pie, en el orden de la rueda. El color indica el elemento."),
    h("Cómo leer esta lámina — y cómo no"),
    p("Lo primero, y va en serio: esto no es medicina y no lo ha sido nunca, ni "
      "cuando se usaba como tal. La melotesia es un sistema mnemotécnico y "
      "simbólico. No diagnostica, no predice dolencias y no debe usarse para "
      "decidir nada sobre tu salud. Si algo te duele, la respuesta está en una "
      "consulta médica."),
    p("Dicho eso, la lámina sí sirve para algo, y es bastante más útil de lo que "
      "parece: convierte los doce signos en doce zonas de mantenimiento. Cada "
      "capítulo de la segunda parte tiene una sección «El cuerpo» que desarrolla la "
      "zona de su signo con cuidados que son de sentido común —movilidad, "
      "descanso, hidratación, hábito postural— y no de superstición. Recorrer los "
      "doce signos a lo largo de un año es, entre otras cosas, revisar el cuerpo "
      "entero por partes."),
    ficha("El reparto completo", [
        ("Aries", "Cabeza, cara, cerebro · Tensión mandibular, cefalea tensional"),
        ("Tauro", "Cuello, garganta, tiroides · Rigidez cervical"),
        ("Géminis", "Hombros, brazos, manos, pulmones · Respiración corta"),
        ("Cáncer", "Pecho, estómago, diafragma · Digestión y emoción"),
        ("Leo", "Corazón, espalda alta, circulación · Postura y presencia"),
        ("Virgo", "Abdomen, intestino, bazo · Tránsito y tolerancias"),
        ("Libra", "Riñones, lumbares, piel · Equilibrio hídrico"),
        ("Escorpio", "Pelvis, suelo pélvico, aparato reproductor"),
        ("Sagitario", "Caderas, muslos, hígado · Movilidad de cadera"),
        ("Capricornio", "Rodillas, huesos, articulaciones, dientes"),
        ("Acuario", "Pantorrillas, tobillos, circulación de retorno"),
        ("Piscis", "Pies, sistema linfático · Drenaje y apoyo"),
    ]),
    h("La estructura oculta del reparto"),
    p("Merece la pena mirar la lámina dos veces, porque el reparto tiene una "
      "coherencia interna que no salta a la vista. Los tres signos de Fuego caen en "
      "cabeza, corazón y muslos: los tres motores del movimiento. Los de Tierra, en "
      "cuello, abdomen y rodillas: las tres articulaciones que sostienen la "
      "vertical. Los de Aire, en hombros, riñones y pantorrillas: los tres puntos "
      "de intercambio y de retorno. Y los de Agua, en pecho, pelvis y pies: los "
      "tres lugares donde el cuerpo guarda lo que no dice."),
    nota("Los ejes también funcionan en el cuerpo",
         "Cada eje de signos opuestos une dos zonas que en la práctica trabajan "
         "juntas. Aries y Libra: cabeza y lumbares, los dos extremos de la cadena "
         "postural. Tauro y Escorpio: garganta y pelvis, los dos diafragmas del "
         "cuerpo. Géminis y Sagitario: hombros y caderas, las dos cinturas. Cáncer "
         "y Capricornio: estómago y rodillas. Leo y Acuario: corazón y retorno "
         "venoso. Virgo y Piscis: intestino y sistema linfático. Que la tradición "
         "acertara en esos emparejamientos con la anatomía que tenía disponible es, "
         "por lo menos, notable."),
)

C7 = cap(
    "Por qué no te reconoces en tu signo",
    p("Es la objeción más frecuente y la más razonable. Alguien lee la descripción "
      "de su signo solar, no se reconoce en absoluto, y concluye con toda lógica que "
      "el sistema no funciona. Conviene responderla bien, porque la respuesta "
      "explica cómo está construido este libro."),
    h("Hay tres respuestas, y las tres son verdad"),
    pasos(
        "El decanato. Un signo son treinta grados y tres caras distintas. El "
        "capítulo anterior lo desarrolla: mucha gente que «no se parece a su signo» "
        "se reconoce inmediatamente al leer su decanato.",
        "Los otros dos puntos. La astrología tradicional nunca describió a nadie por "
        "su Sol únicamente. Trabajaba con tres piezas: el Sol, la Luna y el "
        "Ascendente. El signo que dice la prensa es solo la primera.",
        "Nadie es un signo. Los doce están en todo el mundo, unos desarrollados y "
        "otros dormidos, y eso es exactamente lo que hace útil el recorrido de doce "
        "meses que propone la tercera parte.",
    ),
    h("Las tres piezas del retrato clásico"),
    ficha("Sol, Luna y Ascendente", [
        ("El Sol", "Lo que quieres ser. El proyecto, la dirección, la identidad "
                   "que reconoces como tuya. Es el signo de la fecha."),
        ("La Luna", "Cómo reaccionas cuando no eliges. El hábito emocional, el "
                    "ritmo, lo que buscas para calmarte. Cambia de signo cada dos "
                    "días y medio."),
        ("El Ascendente", "Cómo apareces y cómo entras en las situaciones. La "
                          "puerta de la casa. Depende de la hora exacta de "
                          "nacimiento y cambia cada dos horas."),
    ]),
    p("La distinción es más útil de lo que parece. Explica, por ejemplo, por qué "
      "alguien se describe como reservado y sus conocidos lo describen como "
      "expansivo: el Sol y el Ascendente pueden apuntar a lados distintos. O por qué "
      "una persona ordenadísima en el trabajo es un desastre emocional: el Sol en "
      "Tierra y la Luna en Agua conviven sin problema en el mismo cuerpo."),
    nota("Este libro no calcula tu carta",
         "Averiguar la Luna y el Ascendente requiere la fecha, la hora y el lugar "
         "de nacimiento, y un cálculo que no cabe en un libro. Hay calculadoras "
         "gratuitas y fiables en cualquier parte. Lo que este libro te da es lo "
         "otro, y es lo que casi nunca se da: los doce signos descritos con la "
         "profundidad suficiente para que, cuando sepas cuáles son tus tres, sepas "
         "qué hacer con ellos."),
    h("Cómo leer el libro cuando ya conoces tus tres signos"),
    lista(
        "Lee tu Sol como el capítulo de la dirección: lo que intentas construir.",
        "Lee tu Luna como el capítulo del cuerpo y del hábito: la sección «La "
        "mesa» de tu Luna suele describirte mucho mejor que la de tu Sol.",
        "Lee tu Ascendente como el capítulo de la primera impresión: si alguien te "
        "describe de una forma que no reconoces, mira ahí.",
        "Lee el opuesto de tu Sol como el capítulo de la tarea pendiente. Es "
        "incómodo a propósito.",
    ),
    sep(),
    p("Y si no sabes ninguno de los tres y no te apetece averiguarlo, el libro "
      "sigue funcionando. Los doce capítulos describen doce formas de estar en el "
      "mundo, y todas están dentro de ti en alguna proporción. La tercera parte "
      "propone recorrerlas una por mes, y ese recorrido no necesita ninguna carta: "
      "necesita un cuaderno."),
)

C8 = cap(
    "Las once claves de cada signo",
    p("Los doce capítulos de la segunda parte tienen exactamente la misma "
      "estructura. Se hizo así a propósito: cuando todos los signos se describen "
      "con las mismas claves, las diferencias reales entre ellos se vuelven "
      "visibles y dejan de depender del entusiasmo del que escribe. Es también la "
      "única forma de que el libro se pueda usar como obra de consulta y no solo "
      "de lectura."),
    pasos(
        "El sello. El medallón del signo, con su glifo, el sigilo de su regente y "
        "la marca de su elemento. Los colores no decoran: dicen el elemento.",
        "La ficha. Fechas, elemento, modalidad, polaridad, regente, metal, piedra, "
        "color, zona corporal y palabra clave. La tarjeta de identidad clásica.",
        "El símbolo. De dónde viene la imagen y qué contiene. El símbolo no es "
        "adorno: es la forma comprimida de todo lo demás.",
        "La fuerza. Lo que el signo hace bien cuando está en su mejor versión.",
        "La sombra. La misma cualidad llevada al exceso o al defecto. Nunca es un "
        "rasgo distinto: siempre es la fuerza desbordada.",
        "El eje. El signo opuesto y la pregunta que los dos comparten. Es la clave "
        "que más incomoda y la que más rinde.",
        "Los tres decanatos. Los treinta grados divididos en tres caras, con las "
        "fechas y el planeta de cada una. Aquí está la explicación de por qué "
        "mucha gente no se reconoce en la descripción general.",
        "El cuerpo. La zona que la tradición asigna al signo y el cuidado que "
        "realmente le corresponde.",
        "La mesa. Alimentos y hábitos afines a su temperamento, en clave de "
        "compensación y no de superstición.",
        "La práctica. Un ejercicio concreto de cuatro semanas para desarrollar la "
        "cualidad del signo, sea o no tu signo solar.",
        "Las relaciones y el trabajo del mes. Con qué temperamentos encaja sin "
        "esfuerzo y con cuáles hay que traducir; y tres preguntas para el cuaderno, "
        "que son la parte que de verdad cambia algo.",
    ),
    nota("Sobre «la mesa»",
         "La sección de alimentación de cada signo no afirma que tu fecha de "
         "nacimiento determine lo que debes comer. Lo que hace es más razonable: "
         "cada temperamento tiene tendencias reconocibles —el que va acelerado suele "
         "comer deprisa, el que es constante tiende a repetir el mismo plato "
         "durante años— y esas tendencias sí se pueden compensar. Son "
         "recomendaciones de sentido común nutricional aplicadas al patrón de cada "
         "signo, y en ningún caso una pauta dietética individualizada."),
    nota("Ninguna sección es un veredicto",
         "Conviene repetirlo antes de entrar en los doce capítulos: lo que sigue "
         "describe tendencias, no destinos. Si al leer tu signo encuentras una "
         "sombra que reconoces, eso es información útil. Si encuentras una que no "
         "reconoces, no la fuerces: el sistema es un espejo, y un espejo que no "
         "devuelve nada simplemente no está enfocando ahí."),
)



# ══════════════════════════════════════════════════════════════════════
#  PARTE I bis · LAS TABLAS QUE SE DEJARON DE IMPRIMIR
# ══════════════════════════════════════════════════════════════════════

C9 = cap(
    "Las dignidades esenciales",
    p("Aquí empieza la parte del sistema clásico que la divulgación moderna ha "
      "dejado caer casi por completo, y no por mala fe: porque es árida, se "
      "aprende con tabla delante y no cabe en un horóscopo de revista. Es también "
      "la parte que convierte el zodiaco en un sistema con reglas en lugar de una "
      "colección de descripciones."),
    p("La idea es sencilla. Un planeta no se comporta igual en los doce signos. "
      "En unos está en su terreno y opera con facilidad; en otros trabaja "
      "incómodo, contra su propia naturaleza. La tradición fijó cuatro grados de "
      "esa comodidad y les puso nombre."),
    ficha("Las cuatro dignidades", [
        ("Domicilio", "El planeta está en el signo que rige. En su casa: hace lo "
                      "que sabe hacer sin resistencia."),
        ("Exaltación", "Está en el signo donde la tradición dice que se le honra. "
                       "Rinde más de lo que le corresponde, y en un grado exacto "
                       "—no en todo el signo—."),
        ("Exilio", "Está en el signo opuesto al que rige. Trabaja al revés de su "
                   "naturaleza y le cuesta el doble."),
        ("Caída", "Está en el signo opuesto al de su exaltación. Ni se le honra "
                  "ni se le atiende."),
    ]),
    fig("dia-dignidades", "Lám. 8",
        "Las cuatro dignidades signo por signo. Con el grado exacto donde cae "
        "cada exaltación y cada caída. Los guiones no son huecos por olvido: "
        "hay signos que no albergan ninguna exaltación."),
    h("Dos columnas son datos y dos se deducen"),
    p("Merece la pena ver la mecánica, porque explica por qué la tabla es "
      "coherente y no un catálogo arbitrario. Los domicilios y las exaltaciones "
      "son lo que la tradición fija: hay que aprenderlos. El exilio y la caída no "
      "hace falta aprenderlos, porque salen solos — el exilio de un planeta está "
      "siempre en el signo opuesto a su domicilio, y su caída en el opuesto a su "
      "exaltación. Media tabla es deducción."),
    nota("Un detalle que casi nunca se dice",
         "Las exaltaciones llevan grado exacto: el Sol en el 19 de Aries, la Luna "
         "en el 3 de Tauro, Júpiter en el 15 de Cáncer, Mercurio en el 15 de "
         "Virgo, Saturno en el 21 de Libra, Marte en el 28 de Capricornio y Venus "
         "en el 27 de Piscis. Siete planetas, siete grados, siete signos. Los "
         "cinco signos restantes —Géminis, Leo, Escorpio, Sagitario y Acuario— no "
         "albergan ninguna exaltación, y esa asimetría es original: la tradición "
         "nunca la rellenó."),
    h("Para qué sirve esto sin carta natal"),
    p("Para leer el libro con más precisión, y para una cosa muy concreta. Cuando "
      "en la segunda parte se dice que Marte en Aries ataca de frente y en "
      "Escorpio persiste en silencio, esa diferencia no es literaria: Marte "
      "gobierna los dos signos, pero uno es diurno y otro nocturno. Y cuando se "
      "dice que Saturno en Libra construye acuerdos, es porque ahí está exaltado — "
      "el mismo Saturno que en Aries, su caída, no sabe hacer otra cosa que "
      "frenar."),
    lista(
        "Marte está en domicilio en Aries y en Escorpio, en exilio en Tauro y "
        "Libra, exaltado en el 28 de Capricornio y caído en el 28 de Cáncer.",
        "Venus está en domicilio en Tauro y Libra, en exilio en Aries y Escorpio, "
        "exaltada en el 27 de Piscis y caída en el 27 de Virgo.",
        "Mercurio es el único que tiene domicilio y exaltación en el mismo signo "
        "—Virgo—, y por eso Virgo es el signo más mercurial de los dos que rige.",
        "Saturno rige Capricornio y Acuario, y está exaltado en Libra: el rigor "
        "encuentra su mejor versión en el signo del equilibrio, que es una de las "
        "afirmaciones más finas de todo el sistema.",
    ),
)

C10 = cap(
    "Los términos: la tabla más olvidada",
    p("Si el capítulo anterior recuperaba una tabla poco impresa, este recupera "
      "una que ha desaparecido casi por completo de la divulgación — y es, "
      "probablemente, la pieza más sofisticada del sistema clásico."),
    p("La tradición no se detuvo en dividir cada signo en tres decanatos de diez "
      "grados. Hizo una segunda división, más fina y deliberadamente irregular: "
      "cinco tramos por signo, de longitud desigual, uno para cada planeta "
      "excepto los luminares. Se llaman términos, o límites, o confines según la "
      "traducción; en griego, horoi."),
    fig("dia-terminos", "Lám. 9",
        "Los sesenta términos. Cada barra son los treinta grados de un signo "
        "partidos en cinco tramos desiguales; la longitud dibujada es su número "
        "de grados, así que la lámina se puede medir con una regla."),
    h("Lo que hace especial a esta tabla"),
    lista(
        "Es irregular a propósito. Los decanatos son tres tramos iguales de diez "
        "grados; los términos son cinco tramos que van de dos a doce grados. La "
        "irregularidad no es descuido: es información.",
        "Solo intervienen cinco planetas. El Sol y la Luna quedan fuera del "
        "reparto de términos, igual que quedan fuera de la doble regencia. Los "
        "luminares no se subdividen.",
        "Cada fila suma exactamente treinta. Es la única tabla de este libro que "
        "se puede verificar aritméticamente, y por eso las de estas páginas se "
        "calculan y se comprueban en lugar de copiarse.",
        "El planeta que abre cada signo tiene sentido: Júpiter abre Aries, Venus "
        "abre Tauro, Mercurio abre Géminis, Marte abre Cáncer. No es el regente "
        "del signo, y ese desajuste es la parte que más discutieron los antiguos.",
    ),
    nota("Los dos repartos que llegaron hasta nosotros",
         "Existen dos tablas de términos en la tradición: la egipcia, que es la "
         "que este libro usa y la más antigua, y la de Ptolomeo, que la corrigió "
         "para hacerla más regular. Ptolomeo declaró que la egipcia no seguía "
         "«ningún orden natural» y propuso la suya. La egipcia le sobrevivió y es "
         "la que siguieron usando los astrólogos árabes y medievales. Se elige "
         "aquí por eso y porque es la que aparece en más manuscritos."),
    h("Cómo se usa"),
    pasos(
        "Localiza el grado exacto que te interese dentro del signo. Si trabajas "
        "solo con tu signo solar, tu grado es aproximadamente el número de días "
        "transcurridos desde que empezó el signo.",
        "Busca en la lámina en qué tramo cae ese grado.",
        "El planeta de ese tramo es el matiz más fino que el sistema clásico "
        "ofrece sobre tu posición. Se lee sobre el decanato, que se lee sobre el "
        "signo: tres capas, de la más gruesa a la más fina.",
    ),
    nota("Un ejemplo, para que no quede en abstracto",
         "Alguien nacido el 12 de abril está en Aries, tercer decanato regido por "
         "Venus, y su grado —el 22 o el 23 de Aries— cae en el término de Marte. "
         "Aries de Venus con término de Marte: el impulso que busca compañía y "
         "que, en el último tramo, recupera el filo. Ese nivel de detalle no lo da "
         "ningún otro sistema de doce categorías."),
)

C11 = cap(
    "Las veintiocho mansiones de la Luna",
    p("Un segundo zodiaco, paralelo al de doce y bastante más antiguo en su lógica: "
      "el que se construye siguiendo a la Luna en vez de al Sol."),
    p("El razonamiento es de una elegancia notable. La Luna tarda unos "
      "veintisiete días y un tercio en dar la vuelta completa al cielo respecto a "
      "las estrellas. Si se quiere un signo por noche, hacen falta veintiocho "
      "divisiones, no doce. Y de ahí sale el sistema que en árabe se llama manāzil "
      "—las estaciones o posadas de la Luna—, que en la India tiene su equivalente "
      "en los nakshatras y que en Europa circuló hasta el Renacimiento en los "
      "tratados de correspondencias."),
    h("La aritmética exacta"),
    ficha("La división en veintiocho", [
        ("Grados por mansión", "360 ÷ 28 = 12° 51′ 25,7″"),
        ("Mansiones por signo", "2 y 1/3 · ninguna mansión coincide con un signo"),
        ("Ciclo de la Luna", "27,32 días sidéreos · de ahí las 28 posadas"),
        ("Primera mansión", "Empieza en el 0° de Aries, igual que el zodiaco solar"),
        ("Desajuste con los doce", "Es deliberado: son dos rejillas distintas "
                                   "sobre el mismo círculo"),
    ]),
    p("Ese desajuste es lo interesante. Como 28 no divide a 12, las dos rejillas "
      "no encajan nunca: cada mansión cae a caballo entre grados de signos "
      "distintos. Quien trabaje con las dos obtiene una lectura cruzada mucho más "
      "fina que con una sola — y quien busque que coincidan perderá el tiempo, "
      "porque no están hechas para coincidir."),
    nota("Por qué este libro NO da la lista de nombres",
         "Y conviene explicarlo, porque es lo primero que se echa en falta. Las "
         "veintiocho mansiones tienen nombre en al menos tres tradiciones "
         "—nakshatras indios, manāzil árabes y los nombres latinizados de los "
         "manuscritos europeos— y las tres listas no coinciden: ni en las "
         "estrellas que anclan cada mansión, ni en dónde empieza la primera, ni en "
         "la transcripción de los nombres, que en los manuscritos latinos aparecen "
         "deformados de mil maneras. Dar una lista como si fuera LA lista sería "
         "inventar una autoridad que no existe. Se da la división, que sí es firme, "
         "y se dice dónde está el desacuerdo."),
    h("Lo que sí se puede usar hoy"),
    p("La estructura, que es lo que de verdad sirve. Veintiocho tramos de casi "
      "trece grados, recorridos por la Luna a razón de uno por noche, dan un "
      "calendario de veintiocho jornadas que se repite trece veces al año. Es un "
      "armazón temporal más fino que el mes y más grueso que el día."),
    pasos(
        "Empieza cualquier noche y numera veintiocho jornadas seguidas.",
        "A cada jornada asígnale una sola cosa que observar. Una, no una lista.",
        "Al cerrar las veintiocho, relee. Lo que aparece no es un patrón lunar: es "
        "un patrón tuyo, visible porque lo has medido con una rejilla constante.",
        "Vuelve a empezar. Trece veces al año, y al final tienes un año de "
        "observación en tramos comparables entre sí.",
    ),
    nota("Y la honestidad de siempre",
         "No hay evidencia de que la posición de la Luna respecto a las estrellas "
         "influya en nada de lo que aquí se propone observar. El valor de las "
         "veintiocho mansiones en este libro es el de cualquier rejilla regular: "
         "permite comparar. Es exactamente el mismo valor que tiene una hoja de "
         "cuaderno cuadriculada, y no es poco."),
)

C12 = cap(
    "El zodiaco que se movió de sitio",
    p("Este capítulo aborda la objeción más seria que se le puede hacer a la "
      "astrología, la única que es puramente factual, y lo hace de frente porque "
      "esquivarla sería deshonesto y porque la respuesta es más interesante que "
      "la objeción."),
    h("El hecho"),
    p("La Tierra no gira sobre un eje fijo. Su eje describe un cono lentísimo, y "
      "como consecuencia el punto donde el Sol cruza el ecuador celeste en "
      "primavera —el punto vernal, el cero del zodiaco— se desplaza hacia atrás "
      "sobre el círculo. El fenómeno se llama precesión de los equinoccios, lo "
      "describió Hiparco de Nicea hacia el 130 antes de nuestra era, y sus cifras "
      "son las siguientes."),
    ficha("Los números, que no se discuten", [
        ("Velocidad", "Unos 50,3 segundos de arco al año"),
        ("Un grado", "Cada 71 años y medio, aproximadamente"),
        ("Ciclo completo", "Unos 25 800 años"),
        ("Desde Ptolomeo", "Unos 24 grados acumulados desde el siglo II"),
        ("Consecuencia", "El signo de Aries ya no coincide con la constelación de "
                         "Aries"),
    ]),
    fig("dia-precesion", "Lám. 10",
        "Dos rejillas sobre el mismo círculo: fuera, los doce signos donde los "
        "fijó la tradición; dentro, las constelaciones del mismo nombre, corridas "
        "veinticuatro grados por la precesión. El hueco entre las dos es el dato "
        "de este capítulo."),
    h("Lo que esto significa, dicho sin rodeos"),
    p("Que cuando alguien dice «soy Aries» no está diciendo que el Sol estuviera "
      "delante de la constelación de Aries el día de su nacimiento. Estaba delante "
      "de la de Piscis. El signo y la constelación comparten nombre y ya no "
      "comparten sitio."),
    h("Las dos respuestas que existen, y son las dos legítimas"),
    ficha("Zodiaco tropical y zodiaco sidéreo", [
        ("Tropical", "Cuenta desde el equinoccio de primavera, que es un hecho "
                     "estacional. El 0° de Aries es «el día en que empieza la "
                     "primavera», no «la constelación de Aries». Es el que usa la "
                     "astrología occidental y el que usa este libro."),
        ("Sidéreo", "Cuenta desde las estrellas y corrige la deriva. Es el que usa "
                    "la astrología india, y es astronómicamente más literal. La "
                    "diferencia entre los dos se llama ayanamsa y hoy vale unos "
                    "24 grados."),
    ]),
    p("Que existan dos zodiacos incompatibles y que ambas tradiciones lleven "
      "siglos funcionando con el suyo dice algo importante sobre qué clase de "
      "sistema es este. Si midiera una influencia física de las estrellas, uno de "
      "los dos tendría que estar equivocado y sería comprobable cuál. Como es un "
      "sistema simbólico de clasificación, los dos funcionan igual de bien dentro "
      "de sus propias reglas — y eso, más que una defensa, es una descripción."),
    nota("La posición de este libro",
         "Se usa el zodiaco tropical y se dice por qué: porque lo que este libro "
         "hace con los doce signos es un calendario del temperamento anclado en "
         "las estaciones, y el ciclo de las estaciones es real, comprobable y no "
         "se ha movido de sitio. Aries es el impulso que rompe el invierno; eso "
         "sigue ocurriendo cada marzo con independencia de qué estrellas haya "
         "detrás. Si alguien te dice que la precesión «refuta» la astrología, ha "
         "refutado una versión que ningún astrólogo serio sostiene desde "
         "Ptolomeo — y si te dice que la precesión no importa, tampoco te está "
         "diciendo la verdad."),
    h("El bonus, que es lo que vale el capítulo"),
    p("Los famosos «signos de los tiempos» —la era de Piscis, la era de Acuario— "
      "salen exactamente de aquí. Como el punto vernal retrocede un signo cada "
      "2 150 años aproximadamente (25 800 dividido entre 12), la constelación que "
      "aloja el equinoccio de primavera cambia cada dos milenios. De ahí la era de "
      "Aries, la de Piscis y la de Acuario. La aritmética es impecable; las fechas "
      "exactas de los cambios no, porque las constelaciones no tienen fronteras "
      "iguales y cada autor pone el límite donde le conviene. Cuando leas una "
      "fecha muy precisa para el comienzo de la era de Acuario, sabes ya que "
      "alguien ha elegido una frontera y no te lo ha dicho."),
)

C13 = cap(
    "La secta: cartas de día y de noche",
    p("Una última pieza recuperada, breve y de las que más cambian la lectura: la "
      "doctrina de la secta, que la astrología helenística usaba en todo momento y "
      "que la moderna abandonó casi por entero."),
    h("La división"),
    p("Los siete planetas se reparten en dos bandos. Uno diurno, encabezado por el "
      "Sol; otro nocturno, encabezado por la Luna. Y la pertenencia importa porque "
      "un planeta de la secta que coincide con la hora del nacimiento opera con "
      "más soltura que el mismo planeta a contramano."),
    ficha("Los dos bandos", [
        ("Secta diurna", "Sol · Júpiter · Saturno"),
        ("Secta nocturna", "Luna · Venus · Marte"),
        ("Mercurio", "Sin secta propia: toma la del momento. Diurno si sale antes "
                     "del Sol, nocturno si sale después."),
        ("La regla", "Carta de día si el Sol está sobre el horizonte al nacer; de "
                     "noche si está debajo."),
    ]),
    h("La parte que más rinde"),
    p("Que Saturno sea diurno y Marte nocturno es, a primera vista, "
      "contraintuitivo: se esperaría lo contrario del planeta del frío y del "
      "planeta del calor. La tradición lo explica por compensación, y el argumento "
      "es bueno: Saturno, que es seco y frío en exceso, se templa con el calor del "
      "día; Marte, que es caliente y seco en exceso, se templa con la humedad de "
      "la noche. Cada uno se coloca donde su exceso se corrige."),
    p("Esa lógica de compensación es la misma que gobierna la sección «La mesa» de "
      "los doce capítulos de signo, y no es casualidad: viene del mismo sitio. Todo "
      "el sistema clásico está construido sobre la idea de que lo que sobra se "
      "equilibra con lo que falta, y no sobre la de que lo semejante se atrae."),
    nota("Cómo usarla sin calcular nada",
         "Si sabes si naciste de día o de noche —y casi todo el mundo lo sabe—, ya "
         "tienes tu secta. Los tres planetas de tu bando son las funciones que te "
         "salen con menos esfuerzo; los del bando contrario, las que exigen "
         "trabajo consciente. Cruza eso con los siete regentes del capítulo 3 y "
         "tienes una lectura de tus facilidades y tus fricciones que no necesita "
         "ninguna carta y que suele resultar incómodamente reconocible."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LOS DOCE SIGNOS
# ══════════════════════════════════════════════════════════════════════

CLAVE = {
    "Aries": "aries", "Tauro": "tauro", "Géminis": "geminis", "Cáncer": "cancer",
    "Leo": "leo", "Virgo": "virgo", "Libra": "libra", "Escorpio": "escorpio",
    "Sagitario": "sagitario", "Capricornio": "capricornio",
    "Acuario": "acuario", "Piscis": "piscis",
}

# Fechas de los tres decanatos. Van a mano y no calculadas: el Sol no recorre
# los treinta grados en días exactos y las tablas al uso redondean de formas
# distintas. Estas son las de este libro, y son coherentes con los rangos de
# cada capítulo.
DECANO_FECHAS = {
    "Aries":       ("21–31 de marzo", "1–10 de abril", "11–20 de abril"),
    "Tauro":       ("21–30 de abril", "1–11 de mayo", "12–21 de mayo"),
    "Géminis":     ("22 de mayo–1 de junio", "2–11 de junio", "12–21 de junio"),
    "Cáncer":      ("22 de junio–2 de julio", "3–12 de julio", "13–22 de julio"),
    "Leo":         ("23 de julio–2 de agosto", "3–12 de agosto", "13–22 de agosto"),
    "Virgo":       ("23 de agosto–2 de septiembre", "3–12 de septiembre",
                    "13–22 de septiembre"),
    "Libra":       ("23 de septiembre–3 de octubre", "4–13 de octubre",
                    "14–22 de octubre"),
    "Escorpio":    ("23 de octubre–2 de noviembre", "3–12 de noviembre",
                    "13–22 de noviembre"),
    "Sagitario":   ("23 de noviembre–2 de diciembre", "3–12 de diciembre",
                    "13–21 de diciembre"),
    "Capricornio": ("22–31 de diciembre", "1–10 de enero", "11–20 de enero"),
    "Acuario":     ("21–31 de enero", "1–9 de febrero", "10–19 de febrero"),
    "Piscis":      ("20 de febrero–1 de marzo", "2–11 de marzo", "12–20 de marzo"),
}

# Carácter de cada decanato: la cualidad del signo teñida por su regente.
DECANO_GLOSA = {
    "Aries": (
        "El impulso sin filtro. Arranca lo que nadie se atreve a arrancar y se "
        "aburre en cuanto la cosa ya funciona.",
        "El impulso con dirección. Aquí el arranque quiere ser visto, y eso — "
        "paradójicamente — lo hace más constante.",
        "El impulso que busca compañía. El más negociador de los tres, y el que "
        "menos disfruta ganando solo."),
    "Tauro": (
        "La constancia con curiosidad. Tauro que además pregunta: el más práctico "
        "y el más resolutivo de los tres.",
        "La constancia como refugio. El más doméstico, el más apegado a lo "
        "conocido y el que peor lleva la mudanza.",
        "La constancia hecha estructura. Tarda en arrancar como nadie y, una vez "
        "en marcha, no hay quien lo detenga."),
    "Géminis": (
        "La curiosidad con horizonte: quiere saberlo todo y de todo. El más "
        "viajero, también con la cabeza.",
        "La curiosidad afilada: contrasta, discute, provoca. El más incisivo y el "
        "que más enemigos hace sin querer.",
        "La curiosidad con voz propia. Aquí la palabra deja de ser juego y se "
        "convierte en oficio."),
    "Cáncer": (
        "La sensibilidad que cuida y embellece. El más acogedor del zodiaco entero.",
        "La sensibilidad que se explica. Pone palabras a lo que siente, cosa "
        "rarísima en un signo de Agua.",
        "La sensibilidad sin diluir. El más intuitivo, y el más expuesto a su "
        "propia marea."),
    "Leo": (
        "El brillo con disciplina. Menos vistoso de entrada y mucho más duradero.",
        "El brillo generoso. Da lo que tiene y multiplica lo que toca; el mejor "
        "anfitrión de la rueda.",
        "El brillo combativo. Necesita un adversario para estar a gusto, y si no "
        "lo hay se lo inventa."),
    "Virgo": (
        "El análisis con centro. Ordena para construir, no solo para corregir.",
        "El análisis con gusto. Aquí el detalle se vuelve artesanía: el más fino "
        "de los tres.",
        "El análisis puro. El más preciso del zodiaco y el que más se desgasta en "
        "el detalle."),
    "Libra": (
        "El equilibrio emocional. Percibe el clima de una habitación antes de "
        "que nadie haya hablado.",
        "El equilibrio con criterio. Aquí la balanza deja de dudar y decide.",
        "El equilibrio expansivo. Media, reúne, abre la mesa y hace sitio."),
    "Escorpio": (
        "La intensidad frontal. El más directo de los tres y el que menos "
        "disimula lo que quiere.",
        "La intensidad con propósito. Transforma para algo, no por costumbre.",
        "La intensidad vinculada. El más magnético, y también el más celoso."),
    "Sagitario": (
        "La búsqueda que estudia. Necesita el dato antes de la fe.",
        "La búsqueda que siente. Cree con el cuerpo, no con el argumento.",
        "La búsqueda que se compromete. Aquí el viaje deja de ser viaje y se "
        "convierte en camino."),
    "Capricornio": (
        "La ambición con amplitud. Construye grande desde el primer plano.",
        "La ambición que ejecuta. El más duro consigo mismo de todo el zodiaco.",
        "La ambición que se muestra. Llega a lo alto y necesita que se vea."),
    "Acuario": (
        "La independencia amable. Reúne gente sin dejarse atar por nadie.",
        "La independencia mental. El más brillante y el más impersonal.",
        "La independencia con corazón. Le importa el grupo de verdad, no solo la "
        "idea del grupo."),
    "Piscis": (
        "La sensibilidad con forma. El único de los tres que consigue terminar lo "
        "que imagina.",
        "La sensibilidad generosa. Compasión que se organiza en obra.",
        "La sensibilidad combativa. Defiende lo frágil, y en esa defensa "
        "encuentra su propio límite."),
}

# El eje: cada signo forma pareja con su opuesto. No son enemigos — son las dos
# mitades de una misma pregunta.
EJE = {
    "Aries": ("Libra", "El eje del yo y del nosotros. Aries sabe lo que quiere y "
              "no sabe consultarlo; Libra sabe consultarlo y no sabe lo que "
              "quiere. Cada uno tiene exactamente la mitad que al otro le falta."),
    "Libra": ("Aries", "El eje del nosotros y del yo. Libra pregunta antes de "
              "moverse y a veces se queda sin moverse nunca; Aries se mueve sin "
              "preguntar. La salud está en el centro del eje, no en un extremo."),
    "Tauro": ("Escorpio", "El eje de lo que se conserva y lo que se transforma. "
              "Tauro guarda; Escorpio quema. Ambos hablan de valor: uno lo mide "
              "en permanencia y el otro en intensidad."),
    "Escorpio": ("Tauro", "El eje de lo que se transforma y lo que se conserva. "
                 "Escorpio necesita aprender que no todo tiene que morir para "
                 "renacer, y Tauro que no todo se puede quedar como está."),
    "Géminis": ("Sagitario", "El eje del dato y del sentido. Géminis acumula "
                "información y Sagitario busca qué significa. Sin Géminis, "
                "Sagitario predica sin saber; sin Sagitario, Géminis sabe sin "
                "saber para qué."),
    "Sagitario": ("Géminis", "El eje del sentido y del dato. Sagitario ve el "
                  "mapa entero y se salta las calles; Géminis conoce todas las "
                  "calles y no sabe adónde va."),
    "Cáncer": ("Capricornio", "El eje del hogar y del mundo. Cáncer construye "
               "hacia dentro y Capricornio hacia fuera. Los dos están "
               "construyendo lo mismo: un lugar donde estar a salvo."),
    "Capricornio": ("Cáncer", "El eje del mundo y del hogar. Capricornio "
                    "conquista y luego no sabe volver a casa; Cáncer se queda en "
                    "casa y luego se pregunta por qué no conquistó nada."),
    "Leo": ("Acuario", "El eje del individuo y del colectivo. Leo necesita ser "
            "alguien y Acuario necesita que no importe quién es. Ninguna de las "
            "dos cosas funciona sola."),
    "Acuario": ("Leo", "El eje del colectivo y del individuo. Acuario ama a la "
                "humanidad y le cuesta el vecino concreto; Leo ama al vecino "
                "concreto y se olvida de la humanidad."),
    "Virgo": ("Piscis", "El eje del detalle y del todo. Virgo distingue y Piscis "
              "disuelve. Uno cura con precisión y el otro con presencia, y hacen "
              "falta las dos."),
    "Piscis": ("Virgo", "El eje del todo y del detalle. Piscis lo siente todo y "
               "no ordena nada; Virgo lo ordena todo y a veces se pierde lo que "
               "estaba ordenando."),
}


def signo(nombre, rango, datos, simbolo, fuerza, sombra, cuerpo, mesa,
          practica_intro, practica, relaciones, preguntas):
    clave = CLAVE[nombre]
    grados = ("0° a 10°", "10° a 20°", "20° a 30°")
    tabla_decanos = [
        (f"{grados[i]} · {DECANO_FECHAS[nombre][i]}",
         f"{DECANATOS[clave][i]} — {DECANO_GLOSA[nombre][i]}")
        for i in range(3)
    ]
    opuesto, texto_eje = EJE[nombre]
    return {
        "titulo": nombre,
        "medallon": f"z-{clave}",
        "bloques": [
            fechas(rango),
            ficha("Correspondencias", datos),
            h("El símbolo"), *[p(x) for x in simbolo],
            h("La fuerza"), *[p(x) for x in fuerza],
            h("La sombra"), *[p(x) for x in sombra],
            nota(f"El eje {nombre}–{opuesto}", texto_eje),
            h("Los tres decanatos"),
            p(f"Los treinta grados de {nombre} no son homogéneos. La tradición los "
              "divide en tres tramos de diez y pone al frente de cada uno un "
              "planeta distinto, que matiza el signo sin cambiarlo. Busca tu fecha: "
              "si nunca te has reconocido del todo en la descripción general, aquí "
              "suele estar la explicación."),
            ficha("Las tres caras del signo", tabla_decanos),
            h("El cuerpo"), *[p(x) for x in cuerpo],
            h("La mesa"), lista(*mesa),
            h("La práctica del signo"), p(practica_intro), pasos(*practica),
            h("Las relaciones"), lista(*relaciones),
            h("El trabajo del mes"), pasos(*preguntas),
        ],
    }


ARIES = signo(
    "Aries", "21 de marzo a 20 de abril",
    [("Elemento", "Fuego"), ("Modalidad", "Cardinal"), ("Polaridad", "Activa"),
     ("Regente", "Marte"), ("Metal", "Hierro"), ("Piedra", "Rubí y diamante"),
     ("Color", "Rojo"), ("Zona corporal", "Cabeza y cara"),
     ("Palabra clave", "Yo empiezo")],
    ["El carnero embiste. No rodea, no calcula el ángulo, no espera a que se abra la "
     "puerta: baja la cabeza y va. Ahí está todo Aries, y también el motivo de que "
     "sea el primer signo de la rueda — porque antes de cualquier construcción hace "
     "falta alguien dispuesto a dar el primer golpe.",
     "Que la tradición le asigne la cabeza no es casual. Aries llega de cabeza en "
     "los dos sentidos: es el que piensa rápido y el que se golpea primero."],
    ["Aries arranca lo que otros llevan meses considerando. Tiene una relación "
     "limpia con la acción: si algo hay que hacer, se hace, y la deliberación viene "
     "después o no viene. Esa capacidad de iniciar sin garantías es rara y "
     "extraordinariamente valiosa, porque casi ningún proyecto nace con las "
     "condiciones aseguradas.",
     "Es también un signo sin doblez. La franqueza de Aries puede resultar brusca, "
     "pero rara vez es traicionera: lo que te dice es lo que piensa, y lo que piensa "
     "lo piensa ahora. No guarda rencor porque no guarda casi nada — descarga y "
     "sigue."],
    ["La misma velocidad que le permite empezar le impide terminar. Aries acumula "
     "proyectos abiertos como otros acumulan objetos, y confunde el entusiasmo "
     "inicial con la capacidad de sostenerlo. El resultado es un historial de "
     "comienzos brillantes y cierres ajenos.",
     "Su segunda sombra es la irritabilidad. La energía marciana que no encuentra "
     "una salida constructiva se convierte en fricción con lo que tiene delante, y "
     "eso desgasta relaciones que Aries valora de verdad. No es agresividad: es "
     "energía sin cauce.",
     "La tercera es la impaciencia con el ritmo de los demás. Aries interpreta la "
     "cautela como cobardía cuando muchas veces es simple prudencia."],
    ["La tradición le asigna la cabeza, la cara y el cerebro, y de ahí vienen sus "
     "dos vulnerabilidades reales: la tensión mandibular y la cefalea de origen "
     "tensional. Aries aprieta los dientes — literalmente — y suele descubrirlo "
     "cuando ya le duele la articulación.",
     "El cuidado que le corresponde no es descansar, porque el reposo forzado le "
     "resulta insoportable. Es canalizar. Aries necesita gasto físico intenso y "
     "regular, no como estética sino como válvula: sin él, la energía se le queda "
     "dentro y se le convierte en tensión."],
    ["Comer despacio, que para Aries es la práctica más difícil de este libro. "
     "Poner el cubierto en la mesa entre bocados.",
     "Hierro de fuentes reales — carne roja magra, legumbre con vitamina C, hoja "
     "verde oscura — porque su regente lo pide y porque gasta mucho.",
     "Vigilar el estimulante. Aries no necesita cafeína: necesita menos. Es el signo "
     "que peor tolera sumar aceleración a la que ya trae.",
     "Cena temprana y ligera. La cabeza acelerada no se apaga con el estómago lleno."],
    "Aries no aprende a esperar leyendo sobre la espera. Aprende poniéndole un "
    "número, un plazo y un testigo.",
    ["Elige una sola cosa empezada y sin terminar. Una. Escríbela en un papel y "
     "ponla donde la veas cada mañana.",
     "Divídela en cuatro partes que puedas cerrar en una semana cada una. Si una "
     "parte no cabe en una semana, divídela otra vez.",
     "Cada semana cierras una parte y la marcas. No empiezas nada nuevo hasta que "
     "el papel esté completo — y esta es la regla que dolerá.",
     "Al cuarto cierre, escribe en el cuaderno qué sentiste al terminar algo. Aries "
     "conoce muy bien la euforia de empezar y muy poco la satisfacción de acabar."],
    ["Con Leo y Sagitario, sus compañeros de Fuego: se entienden sin explicarse, "
     "aunque nadie frena a nadie.",
     "Con Libra, su signo opuesto: la atracción es real y la lección también. Libra "
     "le enseña a considerar al otro antes de moverse.",
     "Con Géminis y Acuario, de Aire: le alimentan las ideas y le siguen el ritmo.",
     "Con Cáncer y Capricornio hay que traducir. Los tres son cardinales y los tres "
     "quieren dirigir, cada uno en una dirección distinta.",
     "Con Tauro la fricción es de ritmo puro: uno acelera, el otro se planta. "
     "Funciona bien cuando cada uno reconoce que el otro tiene la pieza que le falta."],
    ["¿Qué he empezado este mes y qué he terminado? Escribe las dos listas y "
     "compara su longitud sin justificarte.",
     "¿Dónde gasté energía en fricción que no llevaba a ningún sitio?",
     "¿A quién le he metido prisa esta semana, y qué necesitaba realmente esa persona?"],
)

TAURO = signo(
    "Tauro", "21 de abril a 21 de mayo",
    [("Elemento", "Tierra"), ("Modalidad", "Fija"), ("Polaridad", "Receptiva"),
     ("Regente", "Venus"), ("Metal", "Cobre"), ("Piedra", "Esmeralda"),
     ("Color", "Verde"), ("Zona corporal", "Cuello, garganta y nuca"),
     ("Palabra clave", "Yo sostengo")],
    ["El toro no embiste: pasta. Está donde está, ocupa su sitio y no lo abandona "
     "porque alguien se lo pida. Su fuerza no es explosiva como la de Aries — es de "
     "resistencia, y por eso Tauro gana casi todas las guerras largas.",
     "La garganta como zona del signo une dos cosas que Tauro tiene en común: la voz "
     "y el gusto. Es el signo de los sentidos y el de la palabra que se cumple."],
    ["Tauro termina. Es su gran virtud y la más infravalorada del zodiaco: donde "
     "otros pierden el interés, Tauro sigue, y sigue, y acaba. La constancia no "
     "brilla, pero es lo único que convierte un plan en un resultado.",
     "Tiene además una capacidad de disfrute que ningún otro signo iguala. Tauro "
     "sabe estar en la comida, en el cuerpo, en el descanso, en la calma. En una "
     "época que confunde velocidad con vida, esa capacidad es una ventaja seria y no "
     "una debilidad."],
    ["Su sombra es la inercia. La misma estabilidad que le permite sostener lo bueno "
     "le hace sostener lo que ya no sirve — un trabajo, una relación, una rutina "
     "vacía — mucho después de saberlo. Tauro no se resiste al cambio por miedo: se "
     "resiste porque cambiar cuesta energía y él la administra con avaricia.",
     "La segunda sombra es la posesión. Tauro asocia el valor con la tenencia, y ese "
     "reflejo se le extiende a las personas con más facilidad de la que reconoce.",
     "La tercera es la comodidad como techo. Cuando Tauro está a gusto deja de "
     "crecer, y puede pasarse años cómodo en algo que se le ha quedado pequeño."],
    ["Cuello, garganta y tiroides son su territorio, y la tensión cervical su queja "
     "más frecuente. Tauro carga los hombros: literalmente los sube y los mantiene "
     "arriba, y acaba con la nuca rígida sin haber hecho nada más que aguantar.",
     "Su otro punto es metabólico. Tauro tiene tendencia a la lentitud digestiva y a "
     "acomodarse en un peso que sube muy despacio y baja todavía más despacio. No "
     "es un problema de voluntad: es que su cuerpo conserva por diseño.",
     "Lo que le funciona es movimiento diario moderado y sostenido —caminar, nadar, "
     "cargar peso— antes que sesiones heroicas y esporádicas. Tauro responde "
     "extraordinariamente bien a la constancia porque la constancia es su idioma."],
    ["Movilidad cervical y de hombro todos los días, aunque sean tres minutos. Es su "
     "mantenimiento no negociable.",
     "Romper la monotonía del plato. Tauro come lo mismo durante años; introducir una "
     "verdura nueva por semana le aporta más de lo que parece.",
     "Cuidar la sal y el azúcar añadido, que son sus dos debilidades sensoriales.",
     "Comer sentado, sin pantalla y sin prisa — esto Tauro ya lo hace bien, y "
     "conviene decírselo."],
    "Tauro no necesita aprender a sostener. Necesita aprender a soltar, y para eso "
    "hace falta un ejercicio incómodo con una fecha.",
    ["Escribe tres cosas que sostienes y que ya no te sirven. Un objeto, una "
     "costumbre y un compromiso.",
     "Elige la más pequeña de las tres y suéltala esta semana. Solo la más pequeña: "
     "no es una purga, es un entrenamiento.",
     "Anota qué temiste perder al soltarla y qué perdiste de verdad. Casi nunca "
     "coinciden, y descubrirlo es el objetivo del ejercicio.",
     "Repite con la segunda al mes siguiente. La tercera puede esperar un año: Tauro "
     "no se transforma a empujones."],
    ["Con Virgo y Capricornio, sus compañeros de Tierra: se reconocen y construyen "
     "juntos sin necesidad de hablarlo.",
     "Con Escorpio, su signo opuesto: la atracción es magnética y el choque también. "
     "Dos fijos que no ceden.",
     "Con Cáncer y Piscis, de Agua: el encaje es natural. Tauro da suelo, el Agua da "
     "profundidad.",
     "Con Aries y Sagitario hay que traducir el ritmo. Ellos van, él llega.",
     "Con Acuario la distancia es real: uno valora lo probado, el otro lo nuevo por "
     "el hecho de serlo."],
    ["¿Qué estoy sosteniendo por costumbre y no por decisión?",
     "¿Cuándo fue la última vez que hice algo por primera vez?",
     "¿Confundí esta semana estar cómodo con estar bien?"],
)

GEMINIS = signo(
    "Géminis", "22 de mayo a 21 de junio",
    [("Elemento", "Aire"), ("Modalidad", "Mutable"), ("Polaridad", "Activa"),
     ("Regente", "Mercurio"), ("Metal", "Azogue"), ("Piedra", "Ágata"),
     ("Color", "Amarillo"), ("Zona corporal", "Brazos, manos y pulmones"),
     ("Palabra clave", "Yo conecto")],
    ["Dos figuras, no una. El símbolo de Géminis no es un ser doble por capricho: es "
     "la representación exacta de una mente que siempre está en dos sitios, viendo "
     "el asunto y viéndose ver el asunto.",
     "Los brazos y las manos como zona del signo señalan lo mismo: Géminis es el que "
     "toma, muestra, señala, escribe y suelta. Su relación con el mundo pasa por lo "
     "que puede manipular y nombrar."],
    ["Géminis entiende rápido y explica mejor. Tiene una capacidad de traducción "
     "—entre disciplinas, entre personas, entre niveles de complejidad— que lo "
     "convierte en la pieza que hace funcionar los grupos donde nadie se entiende.",
     "Su curiosidad es genuina y sin jerarquías: le interesa la física cuántica y le "
     "interesa el cotilleo del portal, y en ambos casos por el mismo motivo. Esa "
     "amplitud lo mantiene joven mentalmente durante décadas."],
    ["La dispersión es su sombra evidente. Géminis empieza siete conversaciones, "
     "abre once pestañas y termina el día con la sensación exacta de no haber hecho "
     "nada, porque efectivamente no ha profundizado en nada.",
     "La segunda es la superficialidad como estrategia. Géminis puede hablar de "
     "cualquier cosa durante diez minutos, y descubre pronto que eso basta para "
     "parecer competente. El atajo funciona tan bien que puede pasarse la vida sin "
     "aprender nada a fondo.",
     "La tercera es la evasión por la palabra. Cuando algo duele, Géminis lo cuenta, "
     "lo analiza, lo convierte en anécdota — y así consigue no sentirlo."],
    ["Pulmones y sistema nervioso. Géminis es el signo que respira mal: corto, alto, "
     "rápido, con el pecho y no con el abdomen, porque su mente va por delante de su "
     "cuerpo casi todo el tiempo.",
     "Su otra vulnerabilidad es la sobreestimulación. Géminis no se agota por "
     "esfuerzo físico, se agota por entradas de información, y lo confunde con "
     "cansancio general. El insomnio de Géminis es un insomnio de mente encendida.",
     "Lo que le funciona es cualquier práctica que ancle la atención en el cuerpo: "
     "respiración diafragmática, actividades que exijan coordinación —escalada, "
     "baile, artes marciales— y silencio deliberado, que para él es el ejercicio "
     "más difícil."],
    ["Comidas regulares. Géminis se salta comidas por distracción y luego resuelve "
     "con lo que hay, que nunca es lo mejor.",
     "Magnesio y omega-3, que son los dos nutrientes con más relación con el sistema "
     "nervioso y la función cognitiva.",
     "Bajar la cafeína y subir el agua. La deshidratación leve le afecta a la "
     "concentración más de lo que cree.",
     "Comer sin pantalla y sin conversación al menos una vez al día. Para Géminis es "
     "un ejercicio, no una comida."],
    "Géminis no necesita más información. Necesita profundidad, y la profundidad "
    "solo se entrena repitiendo.",
    ["Elige un solo tema. Uno que te interese de verdad y del que sepas poco.",
     "Dedícale veinte minutos diarios durante cuatro semanas. El mismo tema, los "
     "mismos veinte minutos. Sin cambiar.",
     "Cada semana escribe una página sobre lo aprendido — a mano, sin buscar nada "
     "mientras escribes. Escribir de memoria es lo que revela si sabes o solo "
     "reconoces.",
     "Al final del mes, explícaselo a alguien durante diez minutos sin notas. Ahí se "
     "verá la diferencia entre haber leído y haber aprendido."],
    ["Con Libra y Acuario, sus compañeros de Aire: conversación infinita y ninguna "
     "necesidad de justificarse.",
     "Con Sagitario, su signo opuesto: los dos son mutables y curiosos, pero "
     "Sagitario busca sentido donde Géminis busca datos. Se complementan bien.",
     "Con Aries y Leo, de Fuego: le dan dirección a su dispersión.",
     "Con Virgo hay parentesco —comparten regente— y también fricción: la misma "
     "inteligencia, uno expandiendo y otro depurando.",
     "Con Tauro, Cáncer y Piscis hay que traducir la velocidad y la profundidad "
     "emocional. Géminis habla de lo que ellos sienten."],
    ["¿En qué he profundizado este mes, y en qué solo he picoteado?",
     "¿Qué he contado esta semana para no tener que sentirlo?",
     "¿Cuánto tiempo he pasado en silencio, sin pantalla y sin conversación?"],
)

CANCER = signo(
    "Cáncer", "22 de junio a 22 de julio",
    [("Elemento", "Agua"), ("Modalidad", "Cardinal"), ("Polaridad", "Receptiva"),
     ("Regente", "Luna"), ("Metal", "Plata"), ("Piedra", "Perla y piedra lunar"),
     ("Color", "Plateado"), ("Zona corporal", "Estómago y pecho"),
     ("Palabra clave", "Yo protejo")],
    ["El cangrejo lleva la casa encima y avanza de lado. Las dos cosas describen a "
     "Cáncer con precisión: necesita un refugio propio para funcionar, y rara vez va "
     "de frente cuando algo le importa de verdad.",
     "El caparazón esconde un cuerpo blando, y esa es la clave del signo. La dureza "
     "de Cáncer es siempre exterior y siempre defensiva. Debajo hay una "
     "sensibilidad que él protege porque sabe que es real."],
    ["Cáncer sostiene a los demás. Tiene un radar emocional que detecta el estado de "
     "una habitación antes de que nadie hable, y una capacidad de cuidado que crea "
     "los vínculos más duraderos del zodiaco. Donde hay un Cáncer, hay alguien "
     "acordándose de lo que a ti te importa.",
     "Es además el signo con mejor memoria emocional. Recuerda cómo se sintió, no "
     "solo lo que pasó, y esa memoria le da una comprensión de las personas que la "
     "inteligencia analítica no alcanza."],
    ["Su sombra es el repliegue. Cuando algo le hiere, Cáncer se mete en el "
     "caparazón y desde dentro interpreta el silencio como confirmación de que tenía "
     "razón en retirarse. El mecanismo se alimenta a sí mismo.",
     "La segunda es el cuidado con factura. Cáncer da mucho, y a veces espera una "
     "reciprocidad que nunca ha pedido en voz alta — y se resiente cuando no llega. "
     "El resentimiento silencioso es su forma más habitual de daño.",
     "La tercera es vivir en el pasado. La misma memoria que le da profundidad le "
     "ata a agravios de hace años que sigue sintiendo en presente."],
    ["Estómago y aparato digestivo, y aquí la correspondencia clásica coincide con "
     "algo que la fisiología reconoce: Cáncer somatiza en el estómago. La tensión "
     "emocional se le convierte en digestión pesada, acidez o nudo.",
     "Su otro punto es la retención. Cáncer es el signo lunar y su cuerpo sigue "
     "ciclos: retiene líquido, fluctúa de peso a lo largo del mes y se desanima "
     "midiéndose en el día equivocado.",
     "Lo que le funciona es el ritmo. Horarios de comida y de sueño estables, "
     "actividad física en el agua o suave y continua, y una regla que le cuesta: "
     "medirse siempre en el mismo punto del ciclo y no interpretar la fluctuación "
     "como fracaso."],
    ["Comer en un entorno tranquilo. Para Cáncer no es un lujo: la digestión le "
     "depende del estado emocional más que a ningún otro signo.",
     "Reducir el exceso de sal y de ultraprocesado, que agravan su tendencia a "
     "retener.",
     "Cuidar la relación entre emoción y comida. Cáncer es el signo que come para "
     "consolarse, y reconocerlo sin culpa es el primer paso.",
     "Cenar dos o tres horas antes de dormir, siempre. Su estómago no descansa si "
     "está trabajando."],
    "Cáncer no necesita endurecerse. Necesita aprender a pedir en voz alta, que es "
    "distinto.",
    ["Identifica una cosa que necesitas de alguien y que nunca has pedido "
     "explícitamente. Escríbela con sus palabras exactas.",
     "Pídela. Sin preámbulo, sin justificar por qué la mereces y sin envolverla en "
     "una queja. Una frase.",
     "Anota lo que pasó: qué temías, qué ocurrió y en qué se parecieron.",
     "Repite con una segunda petición a la semana siguiente. Cáncer descubre en este "
     "ejercicio que el rechazo que teme casi nunca llega, y que cuando llega se "
     "sobrevive."],
    ["Con Escorpio y Piscis, sus compañeros de Agua: se entienden en un nivel que no "
     "necesita palabras.",
     "Con Capricornio, su signo opuesto: el eje casa–trabajo, refugio–estructura. "
     "Complementarios de manual cuando hay respeto.",
     "Con Tauro y Virgo, de Tierra: le dan la estabilidad concreta que su mundo "
     "emocional necesita.",
     "Con Aries y Libra hay que traducir. Los tres son cardinales; Cáncer dirige "
     "desde el vínculo y eso no siempre se ve como liderazgo.",
     "Con Géminis y Acuario la distancia es de temperatura: ellos analizan lo que "
     "Cáncer siente, y eso puede parecerle frialdad sin que lo sea."],
    ["¿Qué he necesitado este mes y no he pedido?",
     "¿A qué agravio antiguo le sigo dando presente?",
     "¿Me he retirado alguna vez esta semana esperando que alguien viniera a "
     "buscarme?"],
)

LEO = signo(
    "Leo", "23 de julio a 22 de agosto",
    [("Elemento", "Fuego"), ("Modalidad", "Fija"), ("Polaridad", "Activa"),
     ("Regente", "Sol"), ("Metal", "Oro"), ("Piedra", "Ámbar y rubí"),
     ("Color", "Dorado"), ("Zona corporal", "Corazón y espalda alta"),
     ("Palabra clave", "Yo expreso")],
    ["El león no persigue: está. Su autoridad no viene del movimiento sino de la "
     "presencia, y por eso Leo es el único signo cuyo símbolo no necesita hacer nada "
     "para significar lo que significa.",
     "Que su regente sea el Sol y su zona el corazón dice lo mismo dos veces: Leo es "
     "el centro que da calor a lo que le rodea. Cuando funciona, todo el sistema "
     "gira mejor. Cuando se apaga, se nota en todos."],
    ["Leo genera. Tiene una capacidad de dar impulso, ánimo y reconocimiento que "
     "levanta equipos enteros, y una generosidad que es real y no calculada: cuando "
     "Leo da, da de verdad y no lleva la cuenta.",
     "Es también el signo más leal del zodiaco. Una vez que Leo te ha incluido en su "
     "círculo, te defiende públicamente y sin condiciones, incluso cuando le sale "
     "caro. Esa lealtad es su rasgo más noble y el menos publicitado."],
    ["Su sombra es la necesidad de reconocimiento. Leo hace cosas admirables y "
     "necesita que se admiren, y cuando el reconocimiento no llega puede pasar de la "
     "generosidad al reproche con una velocidad que le sorprende a él mismo.",
     "La segunda es el orgullo como cárcel. Leo tiene una dificultad genuina para "
     "reconocer un error en público, y ese bloqueo le ha costado más relaciones que "
     "cualquier defecto real.",
     "La tercera es la dramatización. Leo agranda lo que le pasa —no por mentir, "
     "sino porque lo vive grande— y eso desgasta la credibilidad que tanto le "
     "importa."],
    ["Corazón, sistema circulatorio y zona dorsal alta. Leo carga la espalda entre "
     "los omóplatos: es el signo que aguanta con el pecho fuera y paga la postura.",
     "Su punto real de atención es cardiovascular, y no por superstición: Leo tiende "
     "a la intensidad sostenida sin descanso y a no reconocer el agotamiento hasta "
     "que es evidente. El signo que menos se permite parar es el que más lo necesita.",
     "Lo que le funciona es trabajo cardiovascular regular y moderado —no solo "
     "intenso—, fortalecimiento de la espalda alta para compensar la postura, y una "
     "disciplina que le cuesta especialmente: descansar antes de estar agotado."],
    ["Vigilar la tensión arterial y el perfil lipídico a partir de los treinta y "
     "cinco. Es el consejo menos glamuroso de este libro y el más útil para Leo.",
     "Bajar el sodio y el alcohol social, que en Leo suele ser considerable.",
     "Potasio y magnesio: hoja verde, plátano, aguacate, frutos secos.",
     "No comer de pie ni entre compromisos. Leo se salta la comida por atender a "
     "otros y luego resuelve mal y tarde."],
    "Leo no necesita más brillo. Necesita comprobar que sigue siendo él sin público.",
    ["Elige algo que hagas bien y que normalmente compartes. Cualquier cosa: "
     "cocinar, entrenar, escribir, arreglar algo.",
     "Hazlo durante cuatro semanas sin contárselo a nadie y sin publicarlo. Ni una "
     "foto, ni un comentario.",
     "Cada semana anota qué sentiste al no poder mostrarlo. Ahí aparece la "
     "información que Leo necesita.",
     "Al final, decide qué parte de tu satisfacción venía del hacer y qué parte del "
     "ser visto. No hay respuesta mala; hay respuesta honesta."],
    ["Con Aries y Sagitario, sus compañeros de Fuego: energía compartida y ningún "
     "malentendido.",
     "Con Acuario, su signo opuesto: el eje individuo–colectivo. Los dos fijos, los "
     "dos con razón, y mucho que aprender uno del otro.",
     "Con Géminis y Libra, de Aire: le dan público, brillo y conversación.",
     "Con Tauro y Escorpio hay choque de fijeza: nadie retrocede y todos lo saben.",
     "Con Virgo, Cáncer y Capricornio hay que traducir el volumen. Leo expresa lo "
     "que ellos prefieren contener."],
    ["¿Qué he hecho este mes que nadie ha visto?",
     "¿Dónde me impidió el orgullo reconocer un error a tiempo?",
     "¿A quién he dado reconocimiento esta semana sin esperar el mío?"],
)

VIRGO = signo(
    "Virgo", "23 de agosto a 22 de septiembre",
    [("Elemento", "Tierra"), ("Modalidad", "Mutable"), ("Polaridad", "Receptiva"),
     ("Regente", "Mercurio"), ("Metal", "Azogue"), ("Piedra", "Jaspe y peridoto"),
     ("Color", "Ocre"), ("Zona corporal", "Intestino y aparato digestivo"),
     ("Palabra clave", "Yo depuro")],
    ["La virgen con la espiga en la mano: la imagen es de cosecha y de selección. "
     "Virgo separa el grano de la paja, y ese gesto —discriminar, quedarse con lo "
     "que sirve— es todo el signo.",
     "Que comparta regente con Géminis y sea de Tierra explica su carácter: la misma "
     "inteligencia mercurial, pero aplicada a lo concreto y orientada al resultado "
     "útil en lugar de a la conversación."],
    ["Virgo hace que las cosas funcionen. Ve el detalle que falla antes de que falle "
     "y tiene una capacidad de mejora continua que convierte procesos mediocres en "
     "procesos buenos. Casi ninguna organización sobrevive sin un Virgo, y casi "
     "ninguna lo reconoce.",
     "Es también el signo más dispuesto a servir sin protagonismo. Virgo trabaja "
     "porque hay que hacerlo, no porque se le vea hacerlo, y esa modestia funcional "
     "es rara y valiosa."],
    ["La crítica es su sombra, y empieza por dentro. Virgo se exige un estándar que "
     "no aplicaría a nadie más y luego lo proyecta, y así consigue estar "
     "insatisfecho con su propio trabajo y con el de todos.",
     "La segunda es la parálisis por perfección. Virgo prefiere no entregar antes "
     "que entregar imperfecto, y ese reflejo le ha costado oportunidades enteras.",
     "La tercera es la preocupación como hábito. Virgo confunde anticipar problemas "
     "con prevenirlos, y puede pasarse años resolviendo mentalmente situaciones que "
     "no van a ocurrir."],
    ["Intestino, y aquí la tradición dio en el blanco de una forma que hoy resulta "
     "llamativa. Virgo es el signo digestivo, y es el que más claramente somatiza la "
     "tensión en el aparato digestivo: intestino irritable, distensión, "
     "intolerancias que aparecen y desaparecen.",
     "Su segundo punto es la hipervigilancia corporal. Virgo se observa mucho, y esa "
     "atención —que en dosis justas es prevención— se convierte con facilidad en "
     "ansiedad por la salud.",
     "Lo que le funciona es rutina digestiva estable, fibra y fermentados, "
     "y una regla que le cuesta aceptar: dejar de investigar cada síntoma. Virgo "
     "necesita menos información sobre su cuerpo y más confianza en él."],
    ["Fibra y alimentos fermentados a diario: es el signo que más se beneficia de "
     "cuidar la microbiota.",
     "Masticar bien y no comer con prisa ni de pie. La digestión de Virgo empieza en "
     "la boca y él suele saltarse ese paso.",
     "Evitar las dietas de eliminación por sospecha. Virgo se quita alimentos sin "
     "diagnóstico y acaba con una dieta pobre y un miedo nuevo.",
     "Una comida a la semana sin analizar nada. Ni macros, ni etiquetas, ni cálculo. "
     "Es un ejercicio terapéutico para este signo."],
    "Virgo no necesita mejorar nada más. Necesita practicar entregar algo imperfecto "
    "y comprobar que no se hunde el mundo.",
    ["Elige una tarea que llevas retrasando por no tenerla lista.",
     "Ponle un plazo de una semana y entrégala en ese plazo, en el estado en que "
     "esté. Sin una última revisión.",
     "Anota qué error temías y qué consecuencia real tuvo. Sé literal: qué pasó, no "
     "qué podría haber pasado.",
     "Repite tres veces más. Al cuarto ciclo Virgo suele descubrir que el ochenta "
     "por ciento entregado a tiempo vale más que el cien por cien que no llega."],
    ["Con Tauro y Capricornio, sus compañeros de Tierra: se entienden en lo concreto "
     "y en la exigencia.",
     "Con Piscis, su signo opuesto: el eje forma–disolución. Piscis le enseña a "
     "Virgo que no todo se ordena, y Virgo le enseña a Piscis que algo hay que "
     "ordenar.",
     "Con Cáncer y Escorpio, de Agua: encaje natural entre cuidado y precisión.",
     "Con Géminis hay parentesco mercurial y también choque: uno abre, el otro "
     "cierra.",
     "Con Aries, Leo y Sagitario hay que traducir el estándar. Ellos improvisan "
     "donde Virgo prepara."],
    ["¿Qué he dejado sin entregar por no estar perfecto?",
     "¿Cuántas de las preocupaciones de este mes se han cumplido?",
     "¿Le he dicho a alguien algo que hacía bien, o solo lo que podía mejorar?"],
)

LIBRA = signo(
    "Libra", "23 de septiembre a 22 de octubre",
    [("Elemento", "Aire"), ("Modalidad", "Cardinal"), ("Polaridad", "Activa"),
     ("Regente", "Venus"), ("Metal", "Cobre"), ("Piedra", "Ópalo y cuarzo rosa"),
     ("Color", "Rosa"), ("Zona corporal", "Riñones y zona lumbar"),
     ("Palabra clave", "Yo equilibro")],
    ["La balanza es el único símbolo del zodiaco que no es un ser vivo, y eso "
     "importa. Libra no representa una criatura con impulsos: representa una "
     "función, la de pesar. Su naturaleza es relacional desde el símbolo mismo.",
     "El riñón como zona del signo dice lo mismo en clave fisiológica: es el órgano "
     "que equilibra, filtra y mantiene la proporción interna. Libra hace con las "
     "relaciones lo que el riñón hace con la sangre."],
    ["Libra ve los dos lados, y no como concesión sino como percepción real. Esa "
     "capacidad lo convierte en el mediador natural del zodiaco: puede sostener dos "
     "posiciones contrarias sin descalificar ninguna, que es una habilidad "
     "extraordinariamente escasa.",
     "Tiene además un sentido de la proporción que se aplica a todo: al trato, al "
     "espacio, a la estética, al tono de una conversación. Libra sabe cuándo algo "
     "está de más, y esa sensibilidad hace que la gente esté cómoda a su lado sin "
     "saber por qué."],
    ["La indecisión es su sombra conocida, pero el mecanismo real es otro: Libra "
     "no duda porque no sepa, duda porque decidir significa desequilibrar, y "
     "desequilibrar le resulta violento.",
     "La segunda sombra es la complacencia. Libra cede para mantener la armonía y "
     "acumula cesiones no dichas, hasta que un día se rompe por algo pequeño y nadie "
     "entiende por qué.",
     "La tercera es la dependencia del vínculo. Libra puede definirse tanto por la "
     "relación que sostiene que pierde de vista qué quiere él, y descubrirlo tarde "
     "es doloroso."],
    ["Riñones y zona lumbar. Libra es el signo de la lumbalgia postural y de la "
     "hidratación insuficiente, y las dos cosas van juntas más de lo que parece.",
     "Su otro punto es la tensión por conflicto no resuelto, que se le acumula "
     "literalmente en la zona baja de la espalda. Libra aguanta situaciones "
     "incómodas por no romper la calma, y el cuerpo lleva la cuenta.",
     "Lo que le funciona es agua —de verdad, dos litros y medio— fortalecimiento del "
     "core y del glúteo para sostener la lumbar, y aprender a tener el conflicto en "
     "el momento en lugar de aplazarlo. Esto último le arregla más espaldas que "
     "cualquier ejercicio."],
    ["Hidratación por objetivo, no por sed: Libra no bebe hasta que tiene sed y "
     "entonces ya va tarde.",
     "Moderar el azúcar y el alcohol, que son sus dos debilidades venusinas.",
     "Cuidar el sodio por la función renal, sobre todo si hay tendencia a retener.",
     "Comer acompañado cuando pueda. Libra come mejor en compañía, y eso no es un "
     "capricho: come más despacio y con más placer."],
    "Libra no necesita más opciones. Necesita practicar decidir y sostener la "
    "decisión sin renegociarla.",
    ["Cada día durante cuatro semanas toma una decisión pequeña en menos de un "
     "minuto y sin consultar a nadie. Qué comes, qué ves, por dónde vas.",
     "No la revises. Aunque veas después una opción mejor, la decisión está tomada.",
     "Cada semana anota una decisión que sostuviste y una que te costó no reabrir.",
     "En la cuarta semana, elige una decisión grande que llevas aplazando y aplícale "
     "el mismo procedimiento: plazo corto, sin consulta, sin revisión."],
    ["Con Géminis y Acuario, sus compañeros de Aire: se entienden y se estimulan sin "
     "esfuerzo.",
     "Con Aries, su signo opuesto: el eje yo–tú en estado puro. La tensión es "
     "constante y la lección, mutua.",
     "Con Leo y Sagitario, de Fuego: le dan la decisión que a él le cuesta.",
     "Con Cáncer y Capricornio hay que traducir: tres cardinales queriendo dirigir "
     "en direcciones distintas.",
     "Con Virgo y Piscis la diferencia es de criterio: uno pesa, otro depura y otro "
     "disuelve."],
    ["¿Qué decisión he aplazado este mes y qué me ha costado aplazarla?",
     "¿En qué he cedido sin decirlo, y cuánto se ha acumulado?",
     "¿Qué quiero yo, al margen de lo que quiere la persona que tengo enfrente?"],
)

ESCORPIO = signo(
    "Escorpio", "23 de octubre a 22 de noviembre",
    [("Elemento", "Agua"), ("Modalidad", "Fija"), ("Polaridad", "Receptiva"),
     ("Regente", "Marte"), ("Metal", "Hierro"), ("Piedra", "Granate y obsidiana"),
     ("Color", "Granate oscuro"), ("Zona corporal", "Sistema reproductor y excretor"),
     ("Palabra clave", "Yo transformo")],
    ["El escorpión no pelea de frente: espera, y golpea una sola vez donde importa. "
     "Es el mismo Marte de Aries, pero subterráneo: donde Aries embiste a la vista, "
     "Escorpio calcula en silencio.",
     "La tradición asigna a Escorpio la zona de la generación y la eliminación, y no "
     "por morbo: son las dos funciones donde el cuerpo crea y destruye. Escorpio es "
     "el signo de lo que muere para que algo nazca."],
    ["Escorpio ve lo que se esconde. Tiene una percepción de la motivación ajena que "
     "resulta incómoda por lo certera, y una tolerancia a la verdad desagradable que "
     "ningún otro signo iguala: donde los demás miran hacia otro lado, Escorpio "
     "mira.",
     "Es también el signo con más capacidad de regeneración. Escorpio atraviesa "
     "crisis que hundirían a cualquiera y sale distinto, no dañado. Su relación con "
     "la pérdida es de transformación, no de resistencia."],
    ["El control es su sombra central. Escorpio ha aprendido que saber es "
     "protegerse, y de ahí a vigilar, comprobar y retener información hay un paso "
     "corto que da con facilidad.",
     "La segunda es el rencor. Escorpio no olvida, y su memoria del agravio tiene "
     "una precisión y una duración que a él mismo le pesan.",
     "La tercera es el hermetismo. Escorpio pide una transparencia que no da, y "
     "justifica la asimetría con la desconfianza. Es el signo que exige llaves y no "
     "entrega las suyas."],
    ["Sistema reproductor y excretor, y por extensión todo lo relacionado con la "
     "eliminación. Escorpio es el signo que retiene: emocionalmente y también en la "
     "dificultad para soltar tensión física acumulada.",
     "Su punto real es el desgaste por intensidad interna. Escorpio no descansa "
     "mentalmente aunque descanse el cuerpo, y eso se traduce en bruxismo, sueño "
     "poco reparador y tensión pélvica y lumbar.",
     "Lo que le funciona es descarga física intensa —es el signo que más se beneficia "
     "del entrenamiento duro— combinada con prácticas de relajación que le cuestan "
     "porque implican bajar la guardia. Escorpio necesita las dos, y solo hace la "
     "primera."],
    ["Hidratación abundante y fibra, por la función excretora que le corresponde.",
     "Vigilar el alcohol como anestesia. Escorpio bebe para bajar la intensidad, y "
     "es el signo con más riesgo de convertirlo en costumbre.",
     "Cuidar el hígado y no tomar como reto el ayuno extremo ni las dietas "
     "punitivas: Escorpio tiende a la disciplina de castigo.",
     "Comer sin pantallas ni trabajo. Escorpio come mientras piensa en un problema, "
     "y así no descansa ni digiere."],
    "Escorpio no necesita más control. Necesita comprobar que puede mostrar algo y "
    "seguir a salvo.",
    ["Elige una persona en la que confíes de verdad. Una.",
     "Cuéntale una cosa tuya que normalmente no contarías. No la más grave: una de "
     "las medianas.",
     "Anota lo que temías que pasara y lo que pasó realmente.",
     "Repite una vez por semana durante el mes, con la misma persona o con otra. El "
     "objetivo no es abrirse con todo el mundo: es desmontar la creencia de que "
     "mostrarse equivale a quedar expuesto."],
    ["Con Cáncer y Piscis, sus compañeros de Agua: profundidad compartida sin "
     "explicaciones.",
     "Con Tauro, su signo opuesto: dos fijos con una atracción intensa y una lucha "
     "por el control que puede durar años.",
     "Con Virgo y Capricornio, de Tierra: encaje excelente entre intensidad y "
     "estructura.",
     "Con Leo y Acuario hay choque de fijeza en su versión más dura.",
     "Con Géminis, Libra y Sagitario hay que traducir la profundidad: ellos aligeran "
     "lo que Escorpio necesita mirar de frente."],
    ["¿Qué información he retenido este mes para mantener el control?",
     "¿A quién le sigo cobrando algo que ya pasó?",
     "¿Qué he pedido a otros que no estoy dando yo?"],
)

SAGITARIO = signo(
    "Sagitario", "23 de noviembre a 21 de diciembre",
    [("Elemento", "Fuego"), ("Modalidad", "Mutable"), ("Polaridad", "Activa"),
     ("Regente", "Júpiter"), ("Metal", "Estaño"), ("Piedra", "Topacio y lapislázuli"),
     ("Color", "Púrpura"), ("Zona corporal", "Caderas, muslos e hígado"),
     ("Palabra clave", "Yo busco")],
    ["El centauro apunta al horizonte. Mitad animal y mitad humano, con el arco "
     "tenso hacia arriba: Sagitario es el instinto puesto al servicio de una "
     "búsqueda de sentido. No dispara por disparar; dispara lejos.",
     "Las caderas y los muslos como zona del signo son el motor del desplazamiento. "
     "Sagitario es el signo del viaje, y el viaje puede ser geográfico, intelectual "
     "o espiritual, pero siempre es un movimiento hacia lo que no conoce."],
    ["Sagitario amplía. Donde otros ven un problema local, él ve el contexto, y esa "
     "capacidad de dar perspectiva es su mejor regalo: hablar con un Sagitario "
     "cuando estás atascado hace que el atasco parezca más pequeño.",
     "Es además el signo más honesto del zodiaco, a veces brutalmente. Sagitario "
     "dice lo que ve, y aunque el momento no siempre sea el mejor, su franqueza es "
     "una forma de respeto: no te está manejando."],
    ["Su sombra es la fuga. Cuando algo se estrecha —una relación, un trabajo, una "
     "conversación difícil— Sagitario descubre de pronto una oportunidad "
     "fascinante en otro sitio. Llama libertad a lo que a veces es evitación.",
     "La segunda es el exceso. Júpiter amplifica todo lo que toca, y en Sagitario "
     "eso significa demasiado de todo: comida, planes, promesas, opiniones.",
     "La tercera es el dogma. El signo que busca la verdad tiene una tendencia "
     "curiosa a creer que ya la encontró, y entonces predica en lugar de buscar."],
    ["Caderas, muslos e hígado. Sagitario es el signo con más tendencia a la lesión "
     "de la articulación de la cadera y del isquiotibial, y casi siempre por lo "
     "mismo: hace mucho, con entusiasmo y sin preparar.",
     "El hígado, regido por Júpiter, señala su otro punto: Sagitario es el signo del "
     "exceso metabólico, el de la sobremesa larga y la copa de más.",
     "Lo que le funciona es movilidad de cadera antes de cualquier esfuerzo, "
     "progresión gradual de cargas —lo contrario de su instinto— y una relación más "
     "moderada con el alcohol. Sagitario responde muy bien al entrenamiento; lo que "
     "le falla es el calentamiento."],
    ["Moderar la cantidad. Sagitario no come mal: come demasiado, y en general "
     "acompañado y a gusto.",
     "Cuidar el hígado: menos alcohol, menos frito, más verdura amarga y agua.",
     "Comer con horario aunque viaje. Es el signo que come a cualquier hora y "
     "cualquier cosa cuando está en movimiento.",
     "Fibra y fruta: su tránsito digestivo agradece la regularidad que su vida no "
     "tiene."],
    "Sagitario no necesita más horizonte. Necesita comprobar qué hay al fondo de una "
    "sola cosa.",
    ["Elige algo que empezaste con entusiasmo y abandonaste al perder la novedad.",
     "Retómalo con un compromiso de cuatro semanas y un plazo escrito. Solo cuatro "
     "semanas: es un plazo que Sagitario puede sostener.",
     "Cuando aparezca la idea nueva y fascinante —aparecerá, sobre la segunda "
     "semana—, anótala en una lista y no la persigas.",
     "Al final del mes, lee la lista de ideas que no persiguiste. Sagitario suele "
     "descubrir que la mitad ya no le interesan, y esa es toda la lección."],
    ["Con Aries y Leo, sus compañeros de Fuego: entusiasmo compartido y ningún "
     "freno.",
     "Con Géminis, su signo opuesto: dos mutables curiosos, uno buscando datos y el "
     "otro sentido. Se complementan muy bien.",
     "Con Libra y Acuario, de Aire: conversación de altura y espacio mutuo.",
     "Con Virgo y Piscis hay fricción mutable: cuatro formas distintas de "
     "adaptarse y ninguna que se parezca.",
     "Con Tauro, Cáncer y Capricornio hay que traducir la necesidad de raíz: ellos "
     "la tienen y Sagitario la interpreta como límite."],
    ["¿De qué he escapado este mes llamándolo oportunidad?",
     "¿Dónde me pasé de la raya sin darme cuenta?",
     "¿Qué he sostenido más de cuatro semanas seguidas?"],
)

CAPRICORNIO = signo(
    "Capricornio", "22 de diciembre a 20 de enero",
    [("Elemento", "Tierra"), ("Modalidad", "Cardinal"), ("Polaridad", "Receptiva"),
     ("Regente", "Saturno"), ("Metal", "Plomo"), ("Piedra", "Ónix y azabache"),
     ("Color", "Gris y negro"), ("Zona corporal", "Rodillas, huesos, piel y dientes"),
     ("Palabra clave", "Yo construyo")],
    ["La cabra montesa sube. No corre, no salta con gracia: encuentra el apoyo "
     "siguiente y lo usa, y así llega donde no llega nadie. En algunas versiones del "
     "símbolo la mitad inferior es un pez, y esa cola marina guarda el secreto del "
     "signo: debajo de la escalada hay una profundidad que Capricornio rara vez "
     "muestra.",
     "Saturno, su regente, es el planeta del límite y del tiempo. Capricornio es el "
     "único signo que entiende el tiempo como aliado y no como amenaza."],
    ["Capricornio termina lo que empieza y lo termina bien. Tiene una capacidad de "
     "esfuerzo sostenido a largo plazo que ningún otro signo iguala, y una "
     "tolerancia a la gratificación aplazada que le permite construir cosas que "
     "tardan años.",
     "Es también el signo más responsable. Cuando Capricornio se compromete, el "
     "compromiso se cumple, y esa fiabilidad absoluta es la razón de que acabe "
     "cargando con el peso de casi todos los grupos en los que entra."],
    ["Su sombra es la dureza, y empieza consigo mismo. Capricornio se exige un "
     "rendimiento que no negocia ni cuando está enfermo, y desde ahí juzga a los "
     "demás por un estándar que nadie le ha pedido.",
     "La segunda es la confusión entre valor y utilidad. Capricornio se siente "
     "valioso cuando produce, y cuando no produce se siente prescindible. Es la "
     "trampa más cara del signo.",
     "La tercera es el aislamiento. Pedir ayuda le parece una forma de fallar, así "
     "que carga solo hasta que no puede más, y entonces tampoco lo dice."],
    ["Rodillas, huesos, piel y dientes: todas las estructuras. Capricornio es el "
     "signo de la articulación que se desgasta por carga sostenida y de la "
     "rigidez que llega con los años antes de lo que debería.",
     "Su punto real es el desgaste crónico. Capricornio no se lesiona de golpe: se "
     "va desgastando durante años sin quejarse, y llega al médico cuando el daño ya "
     "está establecido. También es el signo con más tendencia a la tensión "
     "mantenida y al agotamiento por acumulación.",
     "Lo que le funciona es movilidad y fuerza —no solo fuerza—, descanso "
     "programado como parte del plan y no como premio, y revisiones periódicas. "
     "Capricornio necesita que el descanso esté en el calendario, porque si no está "
     "escrito no existe."],
    ["Calcio, vitamina D y proteína suficiente: es el signo del hueso y conviene "
     "tomárselo literalmente.",
     "Colágeno y omega-3 para la articulación, y agua para el tejido.",
     "Comer sentado y a su hora. Capricornio come trabajando, y eso a la larga se "
     "paga.",
     "Vigilar el café como combustible. Capricornio sustituye descanso por "
     "estimulante durante años."],
    "Capricornio no necesita rendir más. Necesita comprobar que sigue valiendo "
    "cuando no produce.",
    ["Bloquea en el calendario cuatro periodos de tres horas, uno por semana, sin "
     "ninguna tarea productiva. Escritos, con hora, como una reunión.",
     "Cúmplelos con la misma seriedad con la que cumples un compromiso de trabajo. "
     "Esta es la parte difícil.",
     "Cada semana anota qué sentiste durante esas horas. Capricornio suele encontrar "
     "culpa, y nombrarla es el objetivo.",
     "En la cuarta semana, pide ayuda con algo. Una cosa concreta, a una persona "
     "concreta. Y déjala hacerlo a su manera."],
    ["Con Tauro y Virgo, sus compañeros de Tierra: se reconocen en el esfuerzo y en "
     "el criterio.",
     "Con Cáncer, su signo opuesto: el eje trabajo–hogar. Cáncer le recuerda que "
     "existe algo además de construir.",
     "Con Escorpio y Piscis, de Agua: la estructura encuentra profundidad y "
     "viceversa.",
     "Con Aries y Libra hay que traducir: tres cardinales dirigiendo hacia lugares "
     "distintos.",
     "Con Géminis y Sagitario la distancia es de gravedad: ellos aligeran lo que "
     "Capricornio toma en serio."],
    ["¿Qué he hecho este mes que no servía para nada y me ha gustado?",
     "¿A quién le he pedido ayuda?",
     "¿Cuántas veces he seguido trabajando estando enfermo o agotado?"],
)

ACUARIO = signo(
    "Acuario", "21 de enero a 19 de febrero",
    [("Elemento", "Aire"), ("Modalidad", "Fija"), ("Polaridad", "Activa"),
     ("Regente", "Saturno"), ("Metal", "Plomo"), ("Piedra", "Amatista y zafiro"),
     ("Color", "Azul eléctrico"), ("Zona corporal", "Tobillos y sistema circulatorio"),
     ("Palabra clave", "Yo comprendo")],
    ["El aguador vierte. No es un signo de agua —es de Aire— y esa aparente "
     "contradicción es la clave: lo que Acuario derrama no es líquido, es "
     "conocimiento. Reparte lo que ha comprendido, y lo reparte para todos.",
     "Que su regente clásico sea Saturno explica algo que sorprende: Acuario no es "
     "caótico. Tiene una estructura mental rigurosa, solo que la aplica a cuestionar "
     "las estructuras existentes en lugar de a sostenerlas."],
    ["Acuario ve lo que viene. Tiene una capacidad genuina de pensar fuera del marco "
     "recibido y de imaginar cómo podrían ser las cosas si no fueran como son, y esa "
     "visión es la que produce los cambios que después todos dan por evidentes.",
     "Es también el signo con más sentido de lo colectivo. A Acuario le importa de "
     "verdad lo que le pasa a gente que no conoce, y esa capacidad de indignarse por "
     "una injusticia ajena es su rasgo más noble."],
    ["Su sombra es la distancia emocional. Acuario ama a la humanidad y le cuesta "
     "estar presente con la persona que tiene delante, y esa asimetría duele a los "
     "suyos.",
     "La segunda es la rebeldía automática. Acuario puede oponerse a algo solo "
     "porque es lo establecido, y confundir la contra por sistema con el pensamiento "
     "propio.",
     "La tercera es la terquedad. Es un signo fijo, aunque no lo parezca: cuando "
     "Acuario ha decidido cómo son las cosas, discutir con él es agotador y "
     "generalmente inútil."],
    ["Tobillos y circulación, en particular el retorno venoso. Acuario es el signo "
     "de la mala circulación periférica, de las extremidades frías y del tobillo que "
     "se torcía de joven y sigue siendo el punto débil.",
     "Su otro punto es nervioso. Acuario vive en la cabeza, se olvida del cuerpo "
     "durante horas y luego se sorprende de estar agotado. Es, junto con Géminis, el "
     "signo que peor registra sus propias señales físicas.",
     "Lo que le funciona es actividad que mueva la sangre a las extremidades —"
     "caminar, bici, natación—, no estar sentado horas sin moverse, y trabajo "
     "específico de tobillo y pantorrilla. Y algo más difícil: bajar al cuerpo con "
     "regularidad, porque no baja solo."],
    ["Alimentos que cuiden la circulación: omega-3, frutos rojos, cítricos, poca sal.",
     "Comer a horas. Acuario se olvida de comer cuando algo le interesa, y es capaz "
     "de descubrir a las cinco de la tarde que no ha desayunado.",
     "Hidratación y magnesio para la función nerviosa.",
     "No convertir la dieta en una posición ideológica. Acuario adopta patrones "
     "alimentarios por convicción y a veces olvida comprobar si le sientan bien."],
    "Acuario no necesita más ideas. Necesita practicar la presencia con una persona "
    "concreta.",
    ["Elige una persona cercana. Una sola.",
     "Quédate con ella treinta minutos a la semana durante cuatro semanas, sin "
     "pantallas, sin debate de ideas y sin resolverle nada. Solo estar y escuchar.",
     "No propongas soluciones. Esto para Acuario es casi imposible y es el núcleo "
     "del ejercicio.",
     "Cada semana anota qué supiste de esa persona que no sabías. Acuario suele "
     "descubrir que conocía sus opiniones y no su vida."],
    ["Con Géminis y Libra, sus compañeros de Aire: entendimiento inmediato y espacio "
     "mutuo.",
     "Con Leo, su signo opuesto: el eje colectivo–individuo. Dos fijos con mucho que "
     "enseñarse y poca disposición a ceder.",
     "Con Aries y Sagitario, de Fuego: comparten el gusto por la libertad y el "
     "movimiento.",
     "Con Tauro y Escorpio hay choque de fijeza pura.",
     "Con Cáncer y Piscis hay que traducir la temperatura: ellos sienten donde "
     "Acuario comprende."],
    ["¿A quién he escuchado este mes sin intentar arreglarle nada?",
     "¿Me he opuesto a algo solo por ser lo establecido?",
     "¿Cuánto tiempo he estado sentado sin moverme, y cuándo bajé al cuerpo?"],
)

PISCIS = signo(
    "Piscis", "20 de febrero a 20 de marzo",
    [("Elemento", "Agua"), ("Modalidad", "Mutable"), ("Polaridad", "Receptiva"),
     ("Regente", "Júpiter"), ("Metal", "Estaño"), ("Piedra", "Aguamarina y amatista"),
     ("Color", "Turquesa"), ("Zona corporal", "Pies y sistema linfático"),
     ("Palabra clave", "Yo disuelvo")],
    ["Dos peces atados nadando en direcciones opuestas. El símbolo describe la "
     "tensión permanente del signo: una parte va hacia el mundo y otra hacia la "
     "disolución, y las dos están unidas por el mismo hilo.",
     "Piscis cierra la rueda, y esa posición explica su naturaleza. Es el signo "
     "donde las formas se deshacen para que el ciclo pueda volver a empezar: por eso "
     "su límite personal es poroso y por eso su compasión no tiene fronteras."],
    ["Piscis siente lo que le pasa al otro. No lo deduce: lo siente, y esa empatía "
     "directa hace que la gente se abra con él sin saber por qué. Es el signo al que "
     "se le cuenta lo que no se cuenta.",
     "Tiene además una capacidad creativa que viene de la misma fuente: al no tener "
     "el límite tan marcado, accede a asociaciones e imágenes que a otros les están "
     "cerradas. Los signos de Piscis son desproporcionadamente frecuentes entre "
     "músicos, poetas y terapeutas, y no es casualidad."],
    ["Su sombra es la falta de límite. Piscis absorbe el estado emocional de quien "
     "tiene cerca y acaba sin saber qué siente él, agotado por emociones que no eran "
     "suyas.",
     "La segunda es la evasión. Cuando la realidad aprieta, Piscis se va: a la "
     "fantasía, al sueño, a la sustancia, a la relación que le rescate. Es el signo "
     "con más facilidad para no estar donde está.",
     "La tercera es el victimismo. Piscis puede instalarse en el papel de quien "
     "sufre porque desde ahí no hay que decidir nada, y ese refugio es cómodo y "
     "corrosivo."],
    ["Pies y sistema linfático, las dos estructuras del signo. Piscis tiene los pies "
     "como punto débil real —hongos, fascitis, apoyo deficiente— y tendencia a "
     "retener líquido y a la circulación linfática perezosa.",
     "Su otro punto es la sensibilidad general: a los medicamentos, al alcohol, a la "
     "cafeína, a los ambientes. Piscis reacciona a dosis a las que otros no "
     "reaccionan, y conviene que lo sepa.",
     "Lo que le funciona es movimiento en el agua —donde está en casa—, cuidado "
     "activo del pie y del calzado, y una estructura horaria que no le nace pero le "
     "sostiene. Piscis florece con rutina, aunque la rutina no le apetezca."],
    ["Reducir alcohol y azúcar de forma seria: es el signo que peor los tolera.",
     "Comer a horas fijas. Piscis come cuando se acuerda, y su energía depende de "
     "eso más de lo que cree.",
     "Cuidar la retención: menos sal, más agua, movimiento diario.",
     "Vigilar la cafeína y los estimulantes, que le afectan al doble que a la media."],
    "Piscis no necesita sentir más. Necesita practicar el límite, y el límite se "
    "entrena diciendo no.",
    ["Cada semana durante un mes, di no a una cosa. Una petición, una invitación, un "
     "favor.",
     "Sin explicación larga y sin disculpa. «No puedo» es una frase completa.",
     "Anota qué sentiste al decirlo y qué pasó después. Piscis descubre casi siempre "
     "que la catástrofe que temía no ocurre.",
     "En la cuarta semana, di no a algo que sí podrías hacer pero no quieres. Ese es "
     "el ejercicio de verdad."],
    ["Con Cáncer y Escorpio, sus compañeros de Agua: se entienden en un nivel que no "
     "requiere lenguaje.",
     "Con Virgo, su signo opuesto: el eje disolución–forma. Virgo le da estructura y "
     "él le da a Virgo permiso para no controlarlo todo.",
     "Con Tauro y Capricornio, de Tierra: le dan el suelo que su naturaleza no "
     "tiene.",
     "Con Géminis y Sagitario hay fricción mutable: mucho movimiento y poca "
     "dirección común.",
     "Con Acuario y Libra la diferencia es de registro: ellos piensan la emoción y "
     "Piscis la habita."],
    ["¿Qué emoción de este mes no era mía?",
     "¿De qué me evadí, y a dónde fui?",
     "¿A qué dije no, y qué pasó realmente después?"],
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · PRÁCTICA
# ══════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════
#  PARTE III · EL USO
# ══════════════════════════════════════════════════════════════════════

C21 = cap(
    "La Luna y sus ocho fases",
    p("De los siete cuerpos clásicos, la Luna es el único cuyo ciclo se puede "
      "seguir a simple vista sin instrumentos y sin tablas. Veintinueve días y "
      "medio, ocho fases reconocibles, y una correspondencia con el ritmo del "
      "trabajo humano que llevó a repartir las tareas del campo según su curso en "
      "casi todas las culturas agrícolas conocidas."),
    p("Lo que sigue no es una afirmación sobre la influencia física de la Luna en "
      "las plantas ni en el cuerpo — ese debate pertenece a la ciencia y no a este "
      "libro. Es algo distinto y perfectamente utilizable: un calendario de cuatro "
      "semanas con un verbo distinto en cada tramo. Su valor no está en la Luna: "
      "está en tener una estructura de veintinueve días que se repite sin que haya "
      "que decidirla."),
    fig("dia-lunar", "Lám. 7",
        "Las ocho fases y el verbo que la tradición asocia a cada una. De "
        "izquierda a derecha: cuatro fases crecientes y cuatro menguantes."),
    h("El ciclo como estructura de trabajo"),
    ficha("Los ocho tramos y su tarea", [
        ("Luna nueva", "Sembrar. Se decide y se escribe qué se va a hacer. No se "
                       "empieza todavía: se define."),
        ("Creciente", "Empezar. El primer movimiento concreto, aunque sea mínimo."),
        ("Cuarto creciente", "Decidir. Aparece el primer obstáculo real y hay que "
                             "elegir cómo seguir."),
        ("Gibosa creciente", "Sostener. El tramo aburrido, y el que separa los "
                             "proyectos que salen de los que no."),
        ("Luna llena", "Culminar. Se mira lo hecho y se enseña. También el tramo "
                       "en que todo se ve más intenso de lo que es."),
        ("Gibosa menguante", "Revisar. Se corrige con la información que ya se "
                             "tiene y antes no se tenía."),
        ("Cuarto menguante", "Soltar. Se quita lo que no va a llegar. Es el tramo "
                             "que casi nadie hace."),
        ("Menguante", "Cerrar. Se anota qué ha funcionado y se deja el terreno "
                      "limpio para el ciclo siguiente."),
    ]),
    h("Cómo usarlo con este libro"),
    pasos(
        "Cada mes del recorrido de doce meses coincide aproximadamente con un ciclo "
        "lunar. Empieza la práctica del signo en luna nueva y no antes.",
        "Las cuatro semanas de la práctica encajan con las cuatro fases: definir, "
        "empezar, sostener, cerrar. La práctica del signo ya está escrita en cuatro "
        "pasos precisamente por esto.",
        "Escribe el registro del mes en luna menguante, no en llena. En llena todo "
        "parece más importante de lo que es y el registro sale exagerado.",
        "Si un mes se te descuadra, no lo arregles: anótalo. El ciclo que se rompe "
        "informa más que el que sale perfecto.",
    ),
    nota("Lo que la Luna no hace",
         "No provoca partos, no altera el sueño de forma demostrada, no determina "
         "el resultado de una decisión y no explica el mal humor de nadie. La "
         "atribución de esos efectos es cultural, no física, y este libro no la "
         "sostiene. Lo que aquí se propone es usar un ciclo visible y regular como "
         "armazón temporal: la misma función que cumple una agenda, con la ventaja "
         "de que a esta no hay que darle cuerda."),
)

C22 = cap(
    "Los días y las horas planetarias",
    p("Este capítulo recoge la parte más técnica y menos divulgada del sistema "
      "clásico, y también la que produce el pequeño asombro de ver que una "
      "costumbre cotidiana esconde una estructura matemática antigua. La semana "
      "que usas todos los días es un artefacto astrológico, y sus nombres lo "
      "delatan."),
    h("Los siete días"),
    ficha("Cada día y su regente", [
        ("Lunes", "Luna · lunes, lundi, Monday. Rutina, casa, cuidado, memoria"),
        ("Martes", "Marte · martes, mardi. Empuje, conflicto, ejercicio, decisión"),
        ("Miércoles", "Mercurio · miércoles, mercredi. Palabra, trámite, estudio"),
        ("Jueves", "Júpiter · jueves, jeudi. Expansión, acuerdo, viaje, generosidad"),
        ("Viernes", "Venus · viernes, vendredi. Vínculo, disfrute, arte, reconciliación"),
        ("Sábado", "Saturno · sábado, Saturday. Límite, orden, cierre, revisión"),
        ("Domingo", "Sol · domingo, Sunday, dies solis. Centro, descanso, identidad"),
    ]),
    p("Las lenguas romances conservan cinco de los siete nombres planetarios y "
      "sustituyeron los dos restantes por términos cristianos —el día del Señor y "
      "el sábado hebreo—; el inglés y las lenguas germánicas conservan los siete, "
      "con los planetas traducidos a dioses locales: Tiw por Marte, Woden por "
      "Mercurio, Thor por Júpiter, Frigg por Venus. La estructura es la misma en "
      "todas."),
    h("La pregunta que casi nadie se hace"),
    p("¿Por qué ese orden? Los planetas ordenados por lentitud van Saturno, "
      "Júpiter, Marte, Sol, Venus, Mercurio, Luna. Pero la semana va Luna, Marte, "
      "Mercurio, Júpiter, Venus, Saturno, Sol. No coincide, y no es un orden "
      "arbitrario: es una consecuencia aritmética del reparto de las horas."),
    h("Las veinticuatro horas"),
    p("El sistema clásico divide el día en veinticuatro horas planetarias y les "
      "asigna un regente cada una, siguiendo el orden caldeo en bucle. La primera "
      "hora del día pertenece al planeta que da nombre al día. Y aquí ocurre lo "
      "interesante: veinticuatro dividido entre siete da tres, y sobran tres. De "
      "modo que la hora veinticinco —la primera del día siguiente— cae siempre tres "
      "puestos más abajo en la escalera caldea."),
    pasos(
        "Empieza en el domingo, día del Sol. Primera hora: Sol.",
        "Reparte las 24 horas en orden caldeo descendente y en bucle: Sol, Venus, "
        "Mercurio, Luna, Saturno, Júpiter, Marte, Sol, Venus…",
        "La hora 24 del domingo cae en Mercurio. La 25 —primera del lunes— cae en "
        "la Luna. Y lunes es, efectivamente, el día de la Luna.",
        "Repite y saldrán los siete días en el orden exacto de la semana: Luna, "
        "Marte, Mercurio, Júpiter, Venus, Saturno, Sol. Toda la semana está "
        "contenida en un salto de tres.",
    ),
    nota("Lo que acabas de ver",
         "La semana de siete días con esos nombres y en ese orden es la huella "
         "fósil de un sistema de horas planetarias que se dejó de usar hace siglos. "
         "Ha sobrevivido en el calendario de medio mundo sin que casi nadie sepa de "
         "dónde viene. Si buscabas conocimiento oculto en el sentido literal —algo "
         "que está a la vista y nadie mira—, esto es lo más oculto que hay en este "
         "libro."),
    h("Las horas no son de sesenta minutos"),
    p("Un detalle que la mayoría de las tablas modernas pasa por alto: las horas "
      "planetarias son desiguales. El día se cuenta de amanecer a atardecer y se "
      "divide en doce partes; la noche, de atardecer a amanecer, en otras doce. En "
      "verano las horas diurnas son largas y las nocturnas cortas, y en invierno al "
      "contrario. Solo en los equinoccios miden sesenta minutos."),
    pasos(
        "Busca la hora de amanecer y de atardecer de tu día y tu ciudad.",
        "Resta: obtienes la duración del día. Divídela entre doce y tendrás la "
        "duración de una hora planetaria diurna.",
        "La primera hora empieza en el amanecer y pertenece al regente del día.",
        "Ve avanzando en orden caldeo descendente. La hora trece empieza en el "
        "atardecer y continúa la serie sin interrupción.",
    ),
    h("Para qué sirve esto, honestamente"),
    p("No sirve para predecir nada, y este libro no va a sugerir lo contrario. "
      "Sirve para dos cosas reales. La primera es histórica: entender de dónde "
      "salió el calendario que usas. La segunda es práctica y bastante eficaz: "
      "repartir las tareas de la semana por afinidad simbólica. Poner las "
      "conversaciones difíciles en miércoles, el entrenamiento fuerte en martes, "
      "el cierre de cuentas en sábado y el descanso de verdad en domingo no tiene "
      "ningún efecto astral — y funciona, porque cualquier estructura repetida "
      "funciona mejor que decidir cada día desde cero."),
    ficha("Reparto semanal sugerido", [
        ("Lunes · Luna", "Planificar, ordenar la casa, cocinar para la semana"),
        ("Martes · Marte", "Entrenamiento exigente, tareas que dan pereza, decisiones"),
        ("Miércoles · Mercurio", "Escribir, estudiar, gestiones, conversaciones difíciles"),
        ("Jueves · Júpiter", "Reuniones, propuestas, lo que hay que hacer crecer"),
        ("Viernes · Venus", "Personas, disfrute, arreglar lo que se rompió"),
        ("Sábado · Saturno", "Revisar, tirar, cerrar, cuentas, mantenimiento"),
        ("Domingo · Sol", "Descanso real. Sin pantalla y sin lista de tareas"),
    ]),
)

C23 = cap(
    "La mesa de los cuatro temperamentos",
    p("Este capítulo es el más práctico del libro y también el que más se separa de "
      "la tradición astrológica, así que conviene decir de entrada en qué se apoya. "
      "La teoría clásica de los temperamentos —colérico, melancólico, sanguíneo, "
      "flemático— es la misma que reparte los cuatro elementos, y durante siglos "
      "fue el marco con el que se pensó la alimentación en Europa. Como fisiología "
      "está superada. Como descripción de patrones de conducta alrededor de la "
      "comida sigue siendo sorprendentemente útil, y es en ese único sentido en el "
      "que se usa aquí."),
    nota("El límite de este capítulo",
         "Nada de lo que sigue es una pauta dietética individualizada. No hay "
         "cálculo de requerimientos, no hay patologías consideradas y no hay "
         "seguimiento — las tres cosas que definen el trabajo de un "
         "dietista-nutricionista. Lo que hay son hábitos de sentido común "
         "agrupados por patrón de conducta. Si tienes una patología, estás "
         "embarazada, tomas medicación o quieres una pauta de verdad, eso lo "
         "prescribe un profesional sanitario colegiado y no un libro."),
    h("Fuego · Aries, Leo, Sagitario"),
    p("El patrón es la velocidad. Fuego come rápido, come de pie, se salta comidas "
      "cuando está ocupado y luego compensa de golpe. Suele tolerar bien el volumen "
      "de comida y mal el horario irregular, y confunde con frecuencia la "
      "aceleración con la energía."),
    lista(
        "La corrección principal no es qué comer sino a qué velocidad. Cubierto en "
        "la mesa entre bocados, y veinte minutos mínimos por comida.",
        "Horario estable antes que composición perfecta. Para este temperamento, "
        "comer siempre a la misma hora rinde más que cualquier cambio de menú.",
        "Vigilar los estimulantes. Es el patrón que peor tolera sumar cafeína a una "
        "activación que ya viene de serie.",
        "Cena temprana y ligera: la cabeza acelerada no se apaga con el estómago "
        "lleno, y el sueño es donde este temperamento pierde más.",
        "Gasto físico intenso y regular. No como estética: como válvula. Sin "
        "descarga, la energía se convierte en tensión y la tensión en picoteo.",
    ),
    h("Tierra · Tauro, Virgo, Capricornio"),
    p("El patrón es la repetición. Tierra come bien y come lo mismo: encuentra "
      "cuatro platos que funcionan y los sostiene durante años. La virtud es "
      "enorme —la constancia es la variable que más pesa en cualquier hábito "
      "alimentario— y el riesgo es doble: monotonía de nutrientes y dificultad "
      "para cambiar cuando el cuerpo cambia."),
    lista(
        "Aprovechar la constancia, que es su ventaja real: batch cooking, compra "
        "planificada, mismo día para lo mismo. A este temperamento el sistema le "
        "sale gratis.",
        "Forzar variedad dentro de la estructura, no contra ella. Misma comida, "
        "distinta verdura o distinta legumbre cada semana.",
        "Fibra y agua, que es donde suele quedarse corto: el tránsito lento es la "
        "queja más habitual de este patrón.",
        "Movimiento diario moderado antes que sesiones heroicas y esporádicas. "
        "Tierra responde extraordinariamente bien a lo sostenido porque es su idioma.",
        "Revisar la ración con honestidad cada cierto tiempo. Es el temperamento "
        "que mejor se adapta a comer bien y peor se da cuenta de que come de más.",
    ),
    h("Aire · Géminis, Libra, Acuario"),
    p("El patrón es la desconexión. Aire come mientras hace otra cosa: leyendo, "
      "hablando, delante de una pantalla. Suele tener poca conciencia de la "
      "cantidad ingerida, olvida comidas enteras sin dramatismo y luego pica "
      "durante toda la tarde sin registrarlo como comer."),
    lista(
        "Comer sin pantalla y sin lectura. Para este patrón es la intervención "
        "única con más efecto, y la más difícil de aceptar.",
        "Estructurar las comidas: es el temperamento que más se beneficia de tener "
        "cinco momentos definidos en el día en lugar de un continuo.",
        "Vigilar el picoteo, que aquí es casi siempre nervioso y no de hambre. "
        "Antes de picar, un vaso de agua y cinco minutos.",
        "Cuidar la proteína en cada comida: al comer distraído, es el macronutriente "
        "que este patrón se salta con más facilidad.",
        "Respiración y descanso. Aire tiende a la respiración corta y al sueño "
        "tardío, y las dos cosas se notan en el apetito del día siguiente.",
    ),
    h("Agua · Cáncer, Escorpio, Piscis"),
    p("El patrón es el vínculo entre comida y emoción. Agua come para calmarse, "
      "asocia platos concretos a memorias concretas y come menos cuando algo le "
      "pesa. No es un defecto de voluntad: es que en este temperamento la comida "
      "cumple una función emocional real, y las pautas que la ignoran fracasan."),
    lista(
        "Reconocer el hambre emocional en lugar de combatirla. Antes de comer "
        "fuera de horario, una pregunta escrita: ¿de qué tengo hambre?",
        "Cuidar la digestión, que es donde este patrón acusa el estado de ánimo. "
        "Comidas más pequeñas y más frecuentes cuando la etapa es difícil.",
        "No prohibir el plato de consuelo: darle un sitio. Una vez por semana, "
        "consciente y sin culpa, funciona mucho mejor que la prohibición.",
        "Reducir el azúcar de rescate. Es el temperamento que más lo usa como "
        "regulador emocional y el que más nota el bajón posterior.",
        "Sal, agua y sueño en ese orden de importancia. Agua retiene, y casi "
        "siempre por descanso insuficiente antes que por dieta.",
    ),
    sep(),
    h("La tabla de las cuatro correcciones"),
    ficha("Un resumen que cabe en la nevera", [
        ("Fuego", "Corrige la VELOCIDAD. Comer despacio y a la misma hora"),
        ("Tierra", "Corrige la VARIEDAD. Misma estructura, distinto contenido"),
        ("Aire", "Corrige la ATENCIÓN. Sin pantalla, con horario"),
        ("Agua", "Corrige el MOTIVO. Preguntar antes de comer fuera de hora"),
    ]),
    nota("Y la corrección que sirve para los cuatro",
         "Si de todo este capítulo solo te vas a llevar una cosa, llévate esta: "
         "ninguna de las cuatro correcciones habla de qué comer. Las cuatro hablan "
         "de cómo. Es la parte que casi ningún plan de alimentación aborda y la que "
         "decide si el resto se sostiene."),
)


C17 = cap(
    "El año como espiral",
    p("Aquí está el uso que convierte este libro en herramienta. La propuesta es "
      "sencilla de enunciar y exigente de cumplir: recorrer los doce signos a lo "
      "largo de un año, un mes cada uno, trabajando la práctica que le corresponde."),
    p("No importa cuál sea tu signo solar. Los doce describen cualidades humanas "
      "completas, y todos las tenemos: unas desarrolladas por temperamento y otras "
      "atrofiadas por falta de uso. El objetivo de este recorrido no es reforzar lo "
      "que ya haces bien, sino visitar durante cuatro semanas la cualidad que peor "
      "llevas."),
    h("Cómo se organiza"),
    ficha("El calendario del recorrido", [
        ("Mes 1 · Aries", "Terminar lo empezado"),
        ("Mes 2 · Tauro", "Soltar lo que ya no sirve"),
        ("Mes 3 · Géminis", "Profundizar en un solo tema"),
        ("Mes 4 · Cáncer", "Pedir en voz alta"),
        ("Mes 5 · Leo", "Hacer sin público"),
        ("Mes 6 · Virgo", "Entregar imperfecto"),
        ("Mes 7 · Libra", "Decidir y sostener"),
        ("Mes 8 · Escorpio", "Mostrar algo propio"),
        ("Mes 9 · Sagitario", "Sostener cuatro semanas"),
        ("Mes 10 · Capricornio", "Descansar sin producir"),
        ("Mes 11 · Acuario", "Estar presente con alguien"),
        ("Mes 12 · Piscis", "Decir no"),
    ]),
    p("Puedes empezar en el mes zodiacal que corresponda a la fecha en que abras el "
      "libro, o empezar por Aries en marzo para que el recorrido coincida con el "
      "ciclo natural. La segunda opción tiene una ventaja: el signo del mes está "
      "«en el aire», y el trabajo se apoya en la estación."),
    h("Las tres reglas del recorrido"),
    pasos(
        "Una práctica por mes. No dos. La tentación de acelerar es exactamente el "
        "patrón que este método corrige.",
        "Se escribe. Las tres preguntas del final de cada signo se responden por "
        "escrito, a mano, el último día del mes. Sin escribir no hay recorrido: hay "
        "buenas intenciones.",
        "No se salta el signo incómodo. El signo cuya práctica te parezca "
        "innecesaria o ridícula es, casi con total seguridad, el que más te hace "
        "falta.",
    ),
    nota("Qué esperar",
         "Este recorrido no cambia tu carácter, y desconfía de cualquier libro que "
         "prometa eso. Lo que hace es más modesto y más real: te muestra doce formas "
         "de operar, te obliga a practicar las que no usas y te deja un registro "
         "escrito de lo que observaste. Al final del año tendrás doce páginas de tu "
         "puño y letra sobre ti mismo. Vale más que cualquier interpretación ajena."),
)

C18 = cap(
    "Registro de observación",
    p("Estas páginas son para escribir. La parte del libro que produce resultados no "
      "es la que se lee: es la que se rellena."),
    h("Ficha de partida"),
    ficha("Antes de empezar el recorrido", [
        ("Fecha de inicio", "________________________"),
        ("Mi signo solar", "________________________"),
        ("El signo cuya práctica me parece más innecesaria", "________________"),
        ("El signo cuya práctica me da más pereza", "________________"),
        ("Lo que quiero observar este año", "________________________"),
    ]),
    nota("Una pista sobre las dos preguntas del medio",
         "El signo que te parece innecesario y el que te da pereza suelen ser el "
         "mismo, y suele ser el que trabaja justo la cualidad que te falta. Anótalos "
         "ahora, antes de empezar, y vuelve a leerlos dentro de un año."),
    h("Registro mensual"),
    p("Para cada mes del recorrido, anota lo mismo: el signo, la práctica, si la "
      "cumpliste y qué observaste. Cuatro líneas por mes bastan. Lo importante no es "
      "la extensión: es que exista el registro y que sea honesto."),
    ficha("Plantilla mensual", [
        ("Signo del mes", "________________________"),
        ("Práctica", "________________________"),
        ("Semanas cumplidas", "1 · 2 · 3 · 4"),
        ("Lo que me costó", "________________________"),
        ("Lo que descubrí", "________________________"),
    ]),
    h("Cierre del año"),
    ficha("Al terminar los doce meses", [
        ("Práctica que más me costó", "________________________"),
        ("Práctica que más me sirvió", "________________________"),
        ("Lo que sigo haciendo un año después", "________________"),
        ("El signo que resultó ser el mío de verdad", "________________"),
    ]),
    sep(),
    p("Esa última pregunta es la única trampa del libro, y conviene explicarla. "
      "Después de un año recorriendo los doce signos, muchos lectores descubren que "
      "la cualidad que más les ha transformado no era la de su signo solar, sino la "
      "de otro que al principio les resultaba ajeno. No significa que su signo esté "
      "mal calculado. Significa que el zodiaco no es una etiqueta que se recibe al "
      "nacer, sino un repertorio que se aprende a usar."),
    p("Y con eso, el libro ha hecho su trabajo."),
)



C24 = cap(
    "Vocabulario del zodiaco",
    p("Los términos que aparecen en este libro, definidos con la precisión "
      "suficiente para leer cualquier otro tratado sin perderse. Van en orden "
      "alfabético y no de aparición: es un capítulo para volver, no para leer de "
      "corrido."),
    ficha("A – D", [
        ("Ascendente", "Signo que asomaba por el horizonte este en el momento del "
                       "nacimiento. Cambia cada dos horas aproximadamente y "
                       "describe la manera de aparecer y de entrar en las "
                       "situaciones. Requiere hora exacta."),
        ("Aspecto", "Distancia angular entre dos puntos de la rueda, medida en "
                    "grados. Los cuatro mayores son oposición (180°), trígono "
                    "(120°), cuadratura (90°) y sextil (60°)."),
        ("Caldeo (orden)", "Los siete planetas clásicos ordenados por lentitud "
                           "aparente: Saturno, Júpiter, Marte, Sol, Venus, "
                           "Mercurio, Luna. Rige el reparto de decanatos y de "
                           "horas planetarias."),
        ("Cardinal", "Modalidad de los cuatro signos que abren estación: Aries, "
                     "Cáncer, Libra, Capricornio. Inician."),
        ("Cuadratura", "Aspecto de 90°. Une signos de la misma modalidad y "
                       "elementos discordes. Roce que obliga a crecer."),
        ("Decanato", "Cada uno de los tres tramos de diez grados en que se divide "
                     "un signo. También llamado «cara». Cada uno tiene un planeta "
                     "regente propio."),
        ("Diurno", "Sinónimo tradicional de polaridad activa: los signos de Fuego "
                   "y Aire. Su movimiento va del interior hacia el mundo."),
    ]),
    ficha("E – M", [
        ("Eje", "Pareja de signos opuestos, a 180°. Hay seis en la rueda, y cada "
                "uno plantea una pregunta que sus dos extremos responden por "
                "mitades."),
        ("Elemento", "Fuego, Tierra, Aire o Agua. Describe de qué está hecha la "
                     "energía de un signo. Tres signos por elemento."),
        ("Fijo", "Modalidad de los cuatro signos que sostienen la estación: Tauro, "
                 "Leo, Escorpio, Acuario. Mantienen."),
        ("Luminares", "El Sol y la Luna, los dos únicos cuerpos clásicos que "
                      "gobiernan un solo signo cada uno."),
        ("Melotesia", "Reparto tradicional del cuerpo humano entre los doce "
                      "signos, de la cabeza a los pies. Sistema simbólico y "
                      "mnemotécnico, nunca diagnóstico."),
        ("Modalidad", "Cardinal, Fijo o Mutable. Describe cómo se mueve la energía "
                      "de un signo. Cuatro signos por modalidad."),
        ("Mutable", "Modalidad de los cuatro signos que cierran estación: Géminis, "
                    "Virgo, Sagitario, Piscis. Adaptan y transforman."),
    ]),
    ficha("N – Z", [
        ("Nocturno", "Sinónimo tradicional de polaridad receptiva: los signos de "
                     "Tierra y Agua. Su movimiento va del mundo hacia el interior."),
        ("Oposición", "Aspecto de 180°. Une signos de la misma modalidad y "
                      "elementos complementarios. Tensión fértil, no conflicto."),
        ("Polaridad", "Activa o receptiva. Alterna signo a signo alrededor de la "
                      "rueda."),
        ("Regente", "Planeta que gobierna un signo. En el sistema clásico de siete, "
                    "cinco planetas rigen dos signos cada uno y los luminares uno."),
        ("Sextil", "Aspecto de 60°. Une signos de elementos afines y la misma "
                   "polaridad. Oportunidad que hay que tomar activamente."),
        ("Signo solar", "El signo que ocupaba el Sol en la fecha de nacimiento. Es "
                        "el que se pregunta en la conversación corriente, y solo "
                        "una de las tres piezas del retrato clásico."),
        ("Trígono", "Aspecto de 120°. Une signos del mismo elemento. Fluidez, con "
                    "el riesgo de que la comodidad impida aprender."),
        ("Triplicidad", "Los tres signos que comparten elemento. Sinónimo de "
                        "trígono cuando se habla de grupos y no de ángulos."),
    ]),
    nota("Sobre lo que este vocabulario no incluye",
         "No aparecen aquí las casas, los planetas transaturninos, los nodos "
         "lunares ni las técnicas predictivas. No es un olvido: este libro trabaja "
         "deliberadamente con el sistema de siete planetas y doce signos, que es "
         "cerrado, coherente y suficiente para todo lo que aquí se propone. Si "
         "sigues por tu cuenta, esos términos son el paso siguiente."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-zodiacal",
    "titulo": "Códice Zodiacal",
    "subtitulo": "Los doce signos como mapa del carácter, del cuerpo y del trabajo interior",
    "autor": "Villuminations",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-zodiaco",
    "acento": "cyan",
    "original": True,
    "laminas": ["zodiaco.svg"],   # sprites que se inyectan en el documento
    "claves": ["zodiaco", "astrología", "doce signos", "decanatos",
               "horas planetarias", "hábitos", "villuminations"],
    "capitulos": [
        # I · Fundamentos
        C1, C2, C3, C4, C5, C6, C7, C8,
        # I bis · Las tablas que se dejaron de imprimir
        C9, C10, C11, C12, C13,
        # II · Los doce signos
        ARIES, TAURO, GEMINIS, CANCER, LEO, VIRGO,
        LIBRA, ESCORPIO, SAGITARIO, CAPRICORNIO, ACUARIO, PISCIS,
        # III · El uso
        C17, C21, C22, C23, C24, C18,
    ],
}


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    destino = SRC / f"{LIBRO['id']}.json"
    destino.write_text(json.dumps(LIBRO, ensure_ascii=False, indent=1))
    palabras = sum(
        len(b["x"].split()) if isinstance(b.get("x"), str) else
        sum(len(str(i).split()) for i in b["x"]) if isinstance(b.get("x"), list) else 0
        for c in LIBRO["capitulos"] for b in c["bloques"]
    )
    print(f"  {LIBRO['titulo']}: {len(LIBRO['capitulos'])} capítulos · "
          f"{palabras:,} palabras · → {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
