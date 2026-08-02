#!/usr/bin/env python3
"""
CÓDICE DE LA MESA — obra original de VILLUMINATION 99
=====================================================
Quinto libro de la colección y primero de la serie de fitness. Nutrición
adulta a partir de fuentes públicas y libres: las obras del gobierno federal
de Estados Unidos no están sujetas a copyright (17 U.S.C. § 105), y eso pone
al alcance de cualquiera las Dietary Reference Intakes, las Dietary
Guidelines, FoodData Central y el FM 7-22 del Ejército. A eso se añade el
registro europeo de declaraciones de propiedades saludables, que es público y
que además guarda la lista de lo que se pidió afirmar y fue RECHAZADO.

Las cifras NO se teclean aquí: vienen de tools/datos_oficiales.py, que se
comprueba antes de escribir nada. Si una tabla no cuadra, no hay libro.

    python3 tools/escribir-codice-mesa.py && python3 build.py mesa
"""

import importlib.util
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"

# Los datos se importan del módulo comprobado. Duplicar una tabla aquí sería
# firmar que algún día el texto dirá una cifra y la lámina otra.
_spec = importlib.util.spec_from_file_location(
    "datos_oficiales", Path(__file__).with_name("datos_oficiales.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
D.comprobar()

MICRO = {fila[0]: fila for fila in D.MICRO}


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


def num(v):
    """Formato español: coma decimal y espacio fino de millar."""
    if isinstance(v, float) and v != int(v):
        return f"{v:g}".replace(".", ",")
    v = int(v)
    return f"{v:,}".replace(",", " ")


_LETRAS = {1: "una", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
           7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once",
           12: "doce"}


def letras(n):
    """El numeral en palabras. Se usa para que el texto no pueda decir «siete
    fuentes» el día que el módulo de datos tenga ocho."""
    return _LETRAS.get(n, str(n))


def fila_micro(clave):
    """Una entrada de la tabla oficial, formateada para una ficha."""
    nombre, unidad, rh, rm, ul, notaest = MICRO[clave]
    techo = f"{num(ul)} {unidad}" if ul is not None else "sin límite establecido"
    return [
        ("Referencia", f"{num(rh)} {unidad} en hombres · {num(rm)} en mujeres"),
        ("Techo (UL)", techo),
        ("Lo que hay que saber", notaest),
    ]


# ══════════════════════════════════════════════════════════════════════
#  PARTE I · CÓMO SE LEE UNA TABLA
# ══════════════════════════════════════════════════════════════════════

C1 = cap(
    "Lo que este libro afirma",
    p("Este libro no tiene un método. No hay una dieta de VILLUMINATION 99, no "
      "hay alimentos prohibidos y no hay una lista de suplementos al final. Lo "
      "digo en la primera línea porque es lo contrario de lo que un libro de "
      "nutrición suele ofrecer, y porque el resto solo se entiende con esto "
      "delante."),
    h("La afirmación"),
    p("Existe un cuerpo de datos de nutrición humana que es a la vez de primer "
      "nivel y de acceso libre, y casi nadie lo abre. Está en las Ingestas "
      "Dietéticas de Referencia, en las guías alimentarias oficiales, en la base "
      "de composición de alimentos del Departamento de Agricultura de Estados "
      "Unidos y en los manuales de campo de un ejército que alimenta y entrena a "
      "un millón de personas y publica su doctrina entera. Todo eso es gratis, "
      "está en línea y no lo protege ningún copyright."),
    p("Lo que sí protege el copyright, y lo que sí cuesta dinero, son las "
      "interpretaciones: los libros de dieta, los planes de pago, los "
      "influencers. Este libro hace el camino inverso. Va a la fuente, saca la "
      "tabla entera —no la mitad bonita— y explica cómo se lee."),
    h("Por qué la mitad de la tabla que falta importa tanto"),
    p("Cualquier folleto de nutrición imprime la cantidad recomendada de un "
      "nutriente. Muy pocos imprimen su límite superior tolerable, que es la "
      "otra columna del mismo documento oficial. El resultado es un público que "
      "sabe cuánto magnesio «necesita» y no tiene idea de a partir de cuánto "
      "empieza el problema, en un momento histórico en el que suplementarse es "
      "tan fácil como pedir un paquete."),
    p("Este libro imprime las dos columnas de los diecinueve nutrientes, y "
      "dedica un capítulo entero a ordenarlos por lo estrecho que es el margen "
      "entre una y otra. Ese orden es un cálculo, no una opinión, y cambia por "
      "completo la idea que uno tiene de qué se puede tomar a ciegas."),
    sep(),
    h("Lo que este libro no afirma"),
    lista(
        "No es una prescripción individual. Los valores de referencia son "
        "poblacionales: describen lo que cubre las necesidades de casi todos los "
        "adultos sanos, no las tuyas.",
        "No considera patologías, embarazo, lactancia, infancia, vejez avanzada "
        "ni medicación. Cualquiera de esas cuatro palabras cambia las cifras, y "
        "en algunos casos las invierte.",
        "No sustituye a un profesional sanitario. Un análisis de sangre y una "
        "consulta valen más que este libro entero, y este libro está escrito "
        "para que llegues a esa consulta sabiendo qué preguntar.",
        "No promete resultados de composición corporal. Ninguna cifra de aquí "
        "adelgaza a nadie; lo que hacen es evitar que te falte algo mientras "
        "haces lo que sí funciona.",
    ),
    nota("Advertencia que viaja con los datos",
         "Si tomas medicación —anticoagulantes, tiroideos, antihipertensivos, "
         "metformina, litio, entre otros— hay nutrientes de esta tabla que "
         "interaccionan con ella de forma clínicamente relevante. La vitamina K y "
         "los anticoagulantes son el caso de manual, pero no el único. No "
         "cambies una ingesta ni empieces un suplemento sin decírselo a quien te "
         "receta. Esto no es una fórmula de cortesía: es el consejo más útil del "
         "libro."),
    sep(),
    h("De dónde sale cada cifra"),
    p(f"De {letras(len(D.FUENTES))} fuentes públicas, todas citadas por su "
      "nombre en el último "
      "capítulo con indicación de dónde se consultan. Ninguna cifra de este "
      "libro está inventada, redondeada por comodidad ni copiada de otro libro "
      "de divulgación."),
    p("Y hay algo más, que es lo que convierte a esta colección en un sistema y "
      "no en un montón de libros con la misma portada: las tablas se comprueban "
      "solas. El programa que compone estas páginas ejecuta primero una batería "
      "de verificaciones —que los rangos de macronutrientes admitan el cien por "
      "cien, que la fibra cuadre con su regla de catorce gramos por cada mil "
      "kilocalorías, que ningún valor de referencia supere su propio techo sin "
      "una nota que explique por qué— y si alguna falla, se niega a escribir el "
      "libro. Una de esas comprobaciones cazó un error mío mientras escribía "
      "esto. Por eso están."),
    nota("Cómo encaja con los otros tres de la serie",
         "Este libro se ocupa de lo que entra. El Códice de la Carga se ocupa de "
         "lo que se hace con el cuerpo, con la dosis oficial de actividad y la "
         "biomecánica de levantar peso. El Códice de la Voluntad se ocupa de la "
         "única variable que decide si un plan sirve, que es cuánto se cumple. Y "
         "el Códice del Descanso se ocupa de la mitad del día que casi todo el "
         "mundo trata como tiempo muerto. Los cuatro comparten el mismo módulo de "
         "datos comprobados, así que ninguno puede contradecir a otro en una "
         "cifra."),
)

C2 = cap(
    "Las cuatro letras que nadie explica",
    p("Antes de la primera cifra hay que entender cuatro siglas, porque son la "
      "diferencia entre leer una tabla de nutrición y creer que la lees. Las "
      "cuatro salen del mismo marco oficial, y el marco es más interesante que "
      "las cifras."),
    ficha("El marco de referencia, en cuatro piezas", [
        ("EAR", "Requerimiento medio estimado. La cantidad que cubre la "
                "necesidad de la MITAD de la población. Es la cifra estadística "
                "de partida, y no es un objetivo para nadie."),
        ("RDA", "Ingesta diaria recomendada. Se calcula sumando al EAR dos "
                "desviaciones típicas, de modo que cubra a cerca del 97 % de la "
                "gente. Casi seguro es más de lo que tú necesitas."),
        ("AI", "Ingesta adecuada. Se usa cuando no hay datos suficientes para "
               "calcular un EAR. Es un valor observado en poblaciones sanas, no "
               "un valor derivado: tiene menos fuerza y muy pocas tablas lo "
               "distinguen del RDA."),
        ("UL", "Límite superior tolerable. El techo por encima del cual el "
               "riesgo de efectos adversos empieza a subir. No es una dosis "
               "tóxica: es donde deja de haber margen conocido."),
    ]),
    h("La consecuencia que casi nadie saca"),
    p("Si el valor recomendado está puesto para cubrir al noventa y siete por "
      "ciento de la población, entonces la mayoría de la gente está por encima "
      "de su necesidad real cuando lo alcanza. Quedarse un poco por debajo del "
      "RDA no significa tener un déficit: significa que no se puede saber, "
      "porque el déficit se define contra la necesidad individual y esa cifra no "
      "aparece en ninguna tabla."),
    p("De ahí que la pregunta «¿llego al cien por cien de la recomendación?» sea "
      "una mala pregunta, y que la buena sea «¿mi patrón de comida hace probable "
      "que me falte algo?». La segunda se contesta mirando la variedad de la "
      "dieta y, si hace falta, un análisis. La primera se contesta con una "
      "aplicación que te dará un número falso con dos decimales."),
    nota("El error técnico que cometen casi todas las apps",
         "Los propios documentos oficiales advierten de esto: el valor "
         "recomendado sirve para orientar a un individuo, y el requerimiento "
         "medio es el que sirve para evaluar la ingesta de un grupo. Usar el "
         "recomendado para juzgar a una población hace que casi todo el mundo "
         "parezca deficiente. Es exactamente el error que fabrica titulares y "
         "vende suplementos, y está desaconsejado por escrito en la fuente que "
         "esos titulares citan."),
    sep(),
    h("Y una pieza más, que llegó en 2019"),
    p("Para el sodio se añadió una categoría nueva: un valor de reducción del "
      "riesgo crónico. No es una ingesta necesaria ni un techo de toxicidad; es "
      "el punto a partir del cual bajar el consumo se asocia a menos riesgo "
      "cardiovascular en la población. Se verá con cifras en el capítulo del "
      "sodio, y conviene saber que existe porque es la primera vez que este "
      "marco reconoce que «suficiente» y «saludable» no son la misma pregunta."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE II · LA ENERGÍA Y SU REPARTO
# ══════════════════════════════════════════════════════════════════════

C3 = cap(
    "El reparto de la energía",
    p("La primera decisión de cualquier dieta no es qué comer, sino cómo se "
      "reparte la energía del día entre las tres fuentes que la dan. Y aquí la "
      "respuesta oficial es mucho más ancha de lo que aparenta el debate "
      "público."),
    fig("me-amdr",
        "Los tres rangos aceptables, a escala sobre el cien por cien",
        "Cada barra es el rango de porcentaje de la energía total que admiten "
        "los valores de referencia para ese macronutriente. Los tres rangos se "
        "solapan y dan margen de sobra para dietas muy distintas: por eso una "
        "dieta con el treinta por ciento de proteína y otra con el quince pueden "
        "ser las dos correctas."),
    h("Lo que dice el rango"),
    ficha("Rangos aceptables de distribución", [
        (nombre, f"del {mn} al {mx} % de la energía · {nt[0].lower() + nt[1:]}")
        for nombre, mn, mx, nt in D.AMDR
    ]),
    p("La lectura importante de esta tabla es negativa: dentro de esos márgenes "
      "no hay un reparto oficialmente mejor. La discusión sobre si conviene más "
      "grasa o más hidrato ocurre entera dentro de la zona permitida, y por eso "
      "llevamos treinta años sin cerrarla."),
    p("Lo que sí está fuera del rango es lo interesante. Bajar de los mínimos "
      "tiene consecuencias conocidas y sale de la zona en la que la seguridad "
      "está establecida. Los tres mínimos, con su motivo, aparecen en los tres "
      "capítulos siguientes."),
    nota("Cómo se convierte un porcentaje en gramos",
         "Un gramo de hidrato o de proteína aporta cuatro kilocalorías; uno de "
         "grasa, nueve. Así que el treinta por ciento de una dieta de 2 000 kcal "
         "son 600 kcal, y 600 dividido entre 9 son unos 67 gramos de grasa. "
         "Sirve para cualquier combinación y es toda la aritmética que este "
         "libro necesita."),
    sep(),
    h("Y el cuarto macronutriente, del que nadie habla"),
    p("El alcohol aporta siete kilocalorías por gramo y no tiene rango "
      "aceptable, porque no tiene función nutricional: no hay una ingesta "
      "recomendada de alcohol y ningún organismo la ha establecido nunca. Las "
      "guías alimentarias lo tratan solo como un límite, y su recomendación "
      "explícita para quien no bebe es no empezar. Es un dato que se cae de casi "
      "todas las tablas de macronutrientes y que cambia la contabilidad de "
      "cualquiera que beba a diario."),
)

C4 = cap(
    "Proteína: un suelo, no un objetivo",
    p("La cifra oficial de proteína es la más citada y la peor entendida de toda "
      "la nutrición. Merece un capítulo entero porque el malentendido va en las "
      "dos direcciones a la vez: hay quien cree que es un objetivo ambicioso y "
      "quien cree que es un techo de seguridad, y no es ninguna de las dos "
      "cosas."),
    ficha("La cifra y lo que significa", [
        ("Valor recomendado", f"{num(D.PROTEINA['rda'])} g por kilo de peso "
                              "corporal y día"),
        ("Para 70 kg", f"{num(70 * D.PROTEINA['rda'])} g al día"),
        ("Rango aceptable", f"del {D.PROTEINA['amdr_min']} al "
                            f"{D.PROTEINA['amdr_max']} % de la energía"),
        ("Qué es exactamente", D.PROTEINA["nota"]),
    ]),
    h("Por qué es un suelo"),
    p("Ese valor se estableció para responder a una pregunta muy concreta: "
      "cuánta proteína hace falta para que un adulto sano no pierda nitrógeno, "
      "es decir, para que no se descomponga su propio tejido. Es el umbral de la "
      "no-carencia. La pregunta de cuánta proteína conviene a alguien que "
      "entrena para ganar masa muscular es otra pregunta, y el marco de "
      "referencia no la responde porque no la formuló."),
    p("La literatura de ciencias del deporte sí la ha formulado, y sus revisiones "
      "convergen en un rango bastante más alto, del orden de uno y medio a dos "
      "gramos por kilo para quien entrena fuerza con intención de ganar tejido. "
      "Digo con toda claridad que ese rango NO sale de las fuentes oficiales de "
      "este libro: sale de literatura científica que no es de dominio público y "
      "que aquí solo se menciona. Lo digo porque un libro que mezcla las dos "
      "cosas sin avisar te hace creer que un gobierno respalda una cifra que no "
      "ha respaldado."),
    p("Y digo también lo que sí respaldan las fuentes oficiales, que es "
      "suficiente para casi todo el mundo: el rango aceptable llega hasta el "
      "treinta y cinco por ciento de la energía. En una dieta de 2 000 "
      "kilocalorías eso son 175 gramos de proteína al día. Es decir, que las "
      "cifras que maneja el gimnasio caben holgadamente dentro de la zona "
      "considerada segura. No hace falta violar ninguna recomendación oficial "
      "para comer bastante proteína, y esa es la respuesta a la mitad de los "
      "argumentos de internet."),
    sep(),
    h("Las dos cosas que la tabla no dice y sí importan"),
    lista(
        "La proteína no se guarda. A diferencia de la grasa y, en pequeña "
        "medida, del hidrato, no hay un depósito de aminoácidos de reserva. Lo "
        "que no se usa se oxida o se convierte. De ahí que repartirla a lo largo "
        "del día tenga más sentido que concentrarla, aunque el total sea igual.",
        "La calidad se mide por lo que falta. Una fuente proteica se juzga por "
        "el aminoácido esencial en el que es más pobre. Las de origen animal "
        "raramente cojean; las vegetales cojean de forma predecible —los cereales "
        "de lisina, las legumbres de metionina— y por eso combinarlas resuelve el "
        "problema sin necesidad de hacerlo en la misma comida.",
        "El peso que se usa en la fórmula es el peso corporal. En obesidad "
        "importante esa cuenta sobreestima la necesidad, porque el tejido "
        "adiposo no demanda aminoácidos como el músculo. Es una de las "
        "situaciones en las que la fórmula general deja de servir y hay que "
        "individualizar con ayuda.",
    ),
    nota("Lo que legalmente se puede afirmar en Europa",
         "El registro europeo de declaraciones de propiedades saludables "
         "autoriza decir que la proteína contribuye al mantenimiento y al "
         "crecimiento de la masa muscular, y también al mantenimiento de los "
         "huesos. No autoriza decir que un batido concreto construya músculo por "
         "sí mismo, ni que queme grasa. La diferencia entre las dos frases es "
         "exactamente la diferencia entre nutrición y publicidad."),
)

C5 = cap(
    "Hidratos: los ciento treinta gramos del cerebro",
    p("El mínimo de hidratos de carbono es la cifra que mejor ilustra cómo se "
      "construye una recomendación, porque no viene de una teoría sobre la "
      "dieta: viene de medir lo que consume un órgano."),
    ficha("El mínimo y de dónde sale", [
        ("Valor recomendado", "130 g al día, para cualquier adulto"),
        ("Rango aceptable", "del 45 al 65 % de la energía"),
        ("Origen de la cifra", "El consumo de glucosa del cerebro. Ese órgano "
                               "gasta del orden de 100 a 140 gramos diarios y no "
                               "negocia."),
        ("Fibra aparte", "La fibra es hidrato de carbono, pero tiene su propia "
                         "cifra de referencia y su propio capítulo."),
    ]),
    h("Y aquí la parte que casi nadie cuenta"),
    p("El propio marco de referencia reconoce que el hidrato de carbono no es un "
      "nutriente esencial en el sentido estricto, porque el cuerpo puede "
      "fabricar glucosa a partir de aminoácidos y del glicerol de las grasas, y "
      "porque el cerebro puede cubrir buena parte de su gasto con cuerpos "
      "cetónicos cuando se le entrena a ello. Eso es lo que hace fisiológicamente "
      "posibles las dietas muy bajas en hidratos, y es honesto decirlo en un "
      "libro que da una cifra mínima."),
    p("Lo que se dice a continuación es igual de importante: que algo sea posible "
      "no lo convierte en recomendable por defecto, y el mínimo de ciento "
      "treinta gramos está puesto para el adulto medio en condiciones "
      "ordinarias, no como veredicto sobre una estrategia dietética concreta. "
      "Quien baja de ahí a propósito está fuera del rango donde la seguridad "
      "está establecida por consenso, y eso no es una condena: es información "
      "que merece conocer antes de decidir, y una razón de peso para hacerlo "
      "acompañado."),
    sep(),
    h("Azúcares añadidos: el único límite duro de las guías"),
    p("Las guías alimentarias oficiales ponen un tope explícito a los azúcares "
      "añadidos: menos del diez por ciento de la energía diaria. En una dieta de "
      "2 000 kilocalorías son 200 kilocalorías, es decir unos cincuenta gramos, "
      "que es aproximadamente lo que lleva una lata y media de refresco."),
    p("Conviene notar la palabra «añadidos». El azúcar de una pieza de fruta "
      "entera no cuenta en ese límite, y el de un zumo sí cuenta en la práctica "
      "porque se comporta como añadido aunque la etiqueta no lo llame así. Esa "
      "distinción —matriz del alimento frente a molécula— es la que explica por "
      "qué las guías hablan de alimentos y no solo de nutrientes."),
    nota("Índice glucémico: por qué no aparece en las tablas oficiales",
         "El índice glucémico mide la respuesta a un alimento aislado, en ayunas "
         "y en cantidad estandarizada, y esas tres condiciones no se dan casi "
         "nunca en una comida real: la grasa, la proteína, la fibra, el "
         "procesado y hasta el orden en que se come alteran la respuesta. Por eso "
         "el marco de referencia no fija objetivos de índice glucémico. Es útil "
         "como concepto y malo como criterio de compra."),
)

C6 = cap(
    "Grasas: por qué el mínimo es del veinte por ciento",
    p("El rango de la grasa tiene el suelo más interesante de los tres, porque "
      "no está puesto por la grasa en sí. Está puesto por lo que la grasa "
      "transporta."),
    ficha("El rango y sus dos extremos", [
        ("Rango aceptable", "del 20 al 35 % de la energía"),
        ("Por qué no menos del 20 %", "Por debajo de ahí cuesta cubrir los ácidos "
                                      "grasos esenciales y las vitaminas "
                                      "liposolubles, que necesitan grasa en la "
                                      "misma comida para absorberse."),
        ("Grasa saturada", "Las guías la limitan a menos del 10 % de la energía."),
        ("Grasas trans industriales", "Sin ingesta segura conocida. Lo más bajo "
                                      "posible."),
    ]),
    h("Los dos que son realmente esenciales"),
    p("De todas las grasas, solo dos son estrictamente esenciales: el ácido "
      "linoleico y el alfa-linolénico. El cuerpo no puede fabricarlos y tiene "
      "que recibirlos. Los demás, incluidos los de cadena larga de los que tanto "
      "se habla, se pueden sintetizar a partir de esos dos, aunque la conversión "
      "es limitada y ahí sí hay discusión legítima sobre si conviene tomarlos "
      "directamente."),
    p("Ambos tienen su propia ingesta adecuada en las tablas oficiales, y ambos "
      "se cubren con cantidades muy modestas de aceites vegetales, frutos secos "
      "y semillas. Es una de esas cosas que la industria de los suplementos "
      "preferiría que no supieras."),
    sep(),
    h("Las cuatro liposolubles y la razón por la que van juntas"),
    p("Las vitaminas A, D, E y K comparten una propiedad que las hace un grupo: "
      "se absorben con la grasa y se almacenan en el tejido graso y en el "
      "hígado. De ahí se siguen dos consecuencias, una buena y una mala."),
    lista(
        "La buena: no hace falta tomarlas todos los días. El depósito cubre "
        "periodos largos, y por eso una analítica de vitamina D refleja meses de "
        "hábito y no lo que cenaste ayer.",
        "La mala: el exceso tampoco se elimina por la orina. Son las vitaminas en "
        "las que la suplementación descuidada hace daño de verdad, y tres de las "
        "cuatro tienen un techo establecido que se puede alcanzar con productos "
        "de venta libre.",
    ),
    nota("La interacción que hay que decir en voz alta",
         "La vitamina K participa en la coagulación, y ahí está el conflicto con "
         "los anticoagulantes de tipo antagonista de la vitamina K. La solución "
         "no es eliminar las verduras de hoja: es mantener una ingesta ESTABLE y "
         "que quien ajusta la dosis lo sepa. Lo que descontrola el tratamiento es "
         "la variación brusca, no la cantidad."),
)

C7 = cap(
    "Fibra y agua: las dos cifras que se calculan",
    p("Estas dos referencias tienen algo en común que las hace instructivas: no "
      "son números caídos del cielo, son el resultado de una regla. Y conocer la "
      "regla vale más que memorizar el número."),
    h("Fibra: catorce gramos por cada mil kilocalorías"),
    ficha("La regla y sus dos resultados", [
        ("Regla", f"{D.FIBRA['por_1000_kcal']} g de fibra por cada 1 000 kcal de "
                  "la dieta"),
        ("Hombres", f"{D.FIBRA['hombres']} g al día"),
        ("Mujeres", f"{D.FIBRA['mujeres']} g al día"),
        ("Por qué difieren", D.FIBRA["nota"]),
    ]),
    p("La consecuencia práctica es directa: si comes bastante menos energía que "
      "la ingesta típica sobre la que se calcularon esas cifras —porque estás en "
      "déficit, porque eres de constitución pequeña o porque tu gasto es bajo— tu "
      "objetivo de fibra es proporcionalmente menor, y no tienes que forzar los "
      "treinta y ocho gramos. La regla escala; el número de la etiqueta, no."),
    p("En el otro sentido: quien come 3 500 kilocalorías porque entrena mucho "
      "necesita cerca de cincuenta gramos, y eso no sale por accidente. Es una de "
      "las carencias más comunes en dietas de volumen construidas a base de "
      "batidos y arroz blanco."),
    nota("Subir la fibra de golpe es un error clásico",
         "Duplicar la fibra en dos días produce hinchazón, gases y, en algunos "
         "casos, más estreñimiento en vez de menos. Se sube por escalones de unos "
         "cinco gramos por semana y se acompaña de agua, porque parte del efecto "
         "de la fibra depende de que haya líquido con el que formar gel."),
    sep(),
    h("Agua: la cifra que casi todo el mundo lee mal"),
    ficha("La referencia y su letra pequeña", [
        ("Hombres", f"{num(D.AGUA['hombres'])} litros al día"),
        ("Mujeres", f"{num(D.AGUA['mujeres'])} litros al día"),
        ("Atención", D.AGUA["nota"]),
    ]),
    p("Es agua TOTAL: la de las bebidas y la de los alimentos. Una fruta es en su "
      "mayor parte agua, y una sopa, un yogur o un plato de verdura aportan "
      "cantidades que no son marginales. Con la comida ronda un veinte por ciento "
      "del total, así que el agua que hay que beber queda claramente por debajo "
      "de esas cifras. Los ocho vasos diarios que se repiten en todas partes no "
      "salen de ningún documento oficial: son una simplificación que sobrevivió "
      "por repetición."),
    p("Y una advertencia en la otra dirección, porque existe y se olvida: se "
      "puede beber demasiada agua. Superar durante horas la capacidad de "
      "excreción del riñón diluye el sodio de la sangre, y eso es un cuadro "
      "grave. Ocurre sobre todo en pruebas de resistencia largas donde se bebe "
      "mucho y solo agua. La señal de que el equilibrio es razonable es de una "
      "banalidad tranquilizadora: orina clara varias veces al día y sed ausente."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE III · LA TABLA ENTERA
# ══════════════════════════════════════════════════════════════════════

C8 = cap(
    "Los diecinueve, con sus dos columnas",
    p("Aquí está la tabla que casi nadie imprime completa. Diecinueve "
      "micronutrientes con su valor de referencia para hombres y para mujeres y, "
      "en la misma línea, su techo. La columna de la derecha es la que falta en "
      "el resto de sitios, y es la que hace falta el día que alguien decide "
      "comprarse un bote."),
    fig("me-micro",
        "Los diecinueve nutrientes con su referencia y su techo",
        "Cada fila lleva el valor recomendado y, cuando existe, el límite "
        "superior tolerable. Las filas sin techo no son las más seguras: son "
        "aquellas para las que no había datos suficientes para establecer uno, "
        "que es una situación distinta y no necesariamente mejor.",
        "media"),
    h("Cómo leer las filas sin techo"),
    p("Nueve de los diecinueve no tienen límite establecido. Es tentador leerlo "
      "como «este se puede tomar sin cuidado», y es lo contrario de lo que "
      "significa. Un techo se establece cuando existen datos suficientes sobre "
      "efectos adversos para fijar un punto; su ausencia indica falta de datos, "
      "no ausencia de riesgo. Los documentos oficiales lo dicen con estas "
      "palabras y aun así se malinterpreta en todas partes."),
    sep(),
    h("Las unidades tramposas"),
    p("Cuatro nutrientes se miden en unidades que incorporan una conversión, y si "
      "no se sabe, las cuentas salen mal por un factor grande. Son estas:"),
    ficha("Unidades que esconden una equivalencia", [
        ("µg RAE · vitamina A", "Equivalentes de actividad de retinol. Un "
                                "microgramo de retinol equivale a doce de "
                                "betacaroteno de los alimentos y a veinticuatro "
                                "de los demás carotenoides con actividad. Comer "
                                "zanahorias no es lo mismo que tomar retinol, y "
                                "el techo se refiere solo al segundo."),
        ("µg DFE · folato", "Equivalentes dietéticos de folato. El ácido fólico "
                            "de los suplementos y de los alimentos fortificados "
                            "se absorbe bastante mejor que el folato natural, y "
                            "la unidad lo corrige. El techo se refiere solo a la "
                            "forma sintética."),
        ("mg NE · niacina", "Equivalentes de niacina. El cuerpo fabrica niacina "
                            "a partir de triptófano, a razón de unos sesenta "
                            "miligramos de aminoácido por cada miligramo de "
                            "vitamina, y la unidad lo incluye."),
        ("mg · vitamina E", "Solo cuenta el alfa-tocoferol, y solo determinadas "
                            "formas estereoisoméricas. Buena parte de la "
                            "«vitamina E» de algunas etiquetas no cuenta para "
                            "esta cifra."),
    ]),
    nota("Lo que el marco da por supuesto",
         "Estas cifras suponen una dieta mixta y variada, porque la "
         "biodisponibilidad depende del acompañamiento. Los propios documentos "
         "señalan dos casos concretos: el hierro de origen vegetal se absorbe "
         "bastante peor, y una dieta sin carne puede requerir del orden del "
         "ochenta por ciento más de hierro; y una dieta muy rica en fitatos "
         "—legumbres y cereales integrales, que por lo demás son excelentes— "
         "puede elevar la necesidad de zinc hasta la mitad. No es un argumento "
         "contra las dietas vegetales: es la letra pequeña que hay que conocer "
         "para llevarlas bien."),
)

C9 = cap(
    "El margen: cuáles admiten error y cuáles no",
    p("Esta es la lámina que no existe en ningún otro sitio, y la razón por la "
      "que valía la pena imprimir las dos columnas. Si se divide el techo entre "
      "el valor recomendado se obtiene una cifra que dice cuántas veces la "
      "recomendación puede tomarse antes de entrar en la zona sin margen "
      "conocido. Ordenados por esa cifra, los nutrientes se separan de una "
      "manera que sorprende."),
    fig("me-margen",
        "Los nutrientes ordenados por lo estrecho que es su margen",
        "El cociente entre el techo y el valor recomendado, en escala "
        "logarítmica. Cuanto más corta la barra, menos espacio hay entre lo que "
        "se recomienda y lo que conviene no pasar. Las barras marcadas en rojo "
        "son las de margen inferior a seis veces: ahí una suplementación a ciegas "
        "puede acercarse al techo sin que nadie se dé cuenta."),
    h("Los de margen estrecho, uno por uno"),
    p("Estos son los que exigen leer la etiqueta y, en varios casos, un análisis "
      "previo. No son peligrosos: son los que no perdonan la aritmética "
      "descuidada de tomar tres productos que llevan lo mismo."),
    ficha("Magnesio", fila_micro("Magnesio")),
    p("Es el único caso en que el techo parece menor que la recomendación, y esa "
      "aparente contradicción es de las cosas más útiles que enseña esta tabla: "
      "el techo se refiere SOLO al magnesio de los suplementos y de los "
      "medicamentos, no al de los alimentos. Se puede comer magnesio "
      "tranquilamente; el efecto laxante que limita la cifra viene de las sales "
      "concentradas, no de las almendras."),
    ficha("Hierro", fila_micro("Hierro")),
    p("La diferencia entre sexos es la mayor de toda la tabla y tiene una causa "
      "obvia. Lo que no es obvio es la asimetría del error: quedarse corto de "
      "hierro se corrige; pasarse de forma sostenida deposita hierro en órganos "
      "y no hay una vía fisiológica cómoda de sacarlo. Existen además personas "
      "con una predisposición genética a absorber más de lo normal que no lo "
      "saben. De todos los suplementos de venta libre, este es el que menos "
      "sentido tiene tomar sin una analítica delante."),
    ficha("Selenio", fila_micro("Selenio")),
    p("El caso didáctico del libro. La nuez de Brasil es la fuente alimentaria "
      "más concentrada que se conoce, con del orden de setenta a noventa "
      "microgramos por unidad, lo que significa que un puñado generoso puede "
      "acercarse al techo diario con comida corriente y sin ningún suplemento. "
      "No es motivo de alarma —una o dos al día cubren la necesidad de sobra— "
      "sino la demostración de que «natural» y «sin techo» no son sinónimos."),
    ficha("Vitamina B6", fila_micro("Vitamina B6")),
    p("Aquí el margen parece amplio, y lo es en números; el problema es que las "
      "dosis de los productos comerciales lo son también. Hay complejos que "
      "llevan cincuenta o cien miligramos por cápsula, es decir decenas de veces "
      "la referencia, y el efecto adverso descrito por exceso sostenido es una "
      "neuropatía sensitiva. Es el ejemplo más limpio de un techo que se rebasa "
      "sin mala intención, sumando dos productos que ya lo llevan."),
    ficha("Vitamina A", fila_micro("Vitamina A")),
    p("Con la distinción de la unidad ya explicada: el techo vale para el retinol "
      "preformado, el de los suplementos, el hígado y algunos aceites. Los "
      "carotenoides de las verduras no lo comprometen. Es una de esas veces en "
      "que dos sustancias con el mismo nombre en la etiqueta no se comportan "
      "igual."),
    sep(),
    h("Y el de margen ancho que aun así hay que vigilar"),
    ficha("Vitamina D", fila_micro("Vitamina D")),
    p("La incluyo porque es el suplemento más vendido y el más razonable de la "
      "lista —la síntesis cutánea depende de la latitud, la estación, la ropa y "
      "la edad, y hay poblaciones enteras que no llegan por vía alimentaria—, y "
      "porque el margen invita a confiarse. Conviene tener las dos "
      "equivalencias a mano: quince microgramos son 600 unidades "
      "internacionales, y el techo de cien microgramos son 4 000. Hay productos "
      "de 10 000 en el mercado."),
    nota("La regla que resume el capítulo",
         "Comer no acerca a nadie al techo, salvo el caso curioso de las nueces "
         "de Brasil. Suplementar sí, y suplementar a la vez con un multivitamínico, "
         "un producto específico y un alimento fortificado es la forma habitual "
         "de llegar sin querer. Antes de añadir un bote, suma lo que ya tomas."),
)

C10 = cap(
    "Sodio y potasio: el par que se lee junto",
    p("Los dos últimos de la tabla merecen capítulo propio porque son el único "
      "par que funciona como balanza, y porque el sodio es el nutriente donde el "
      "marco de referencia tuvo que inventarse una categoría nueva."),
    ficha("Sodio", fila_micro("Sodio")),
    ficha("Potasio", fila_micro("Potasio")),
    h("Las tres cifras del sodio"),
    p("La ingesta adecuada está en 1 500 miligramos. El valor de reducción del "
      "riesgo crónico está en 2 300, que es el sodio de unos seis gramos de sal, "
      "algo más de una cucharadita rasa. Y el consumo real de la población "
      "occidental supera ampliamente esa segunda cifra. Las tres juntas cuentan "
      "una historia que ninguna cuenta sola: no es que haga falta más sodio, es "
      "que hay que bajarlo, y el objetivo realista no es el mínimo sino el "
      "segundo número."),
    p("Y una precisión que casi nunca se hace: la mayor parte del sodio de la "
      "dieta occidental no viene del salero. Viene del pan, de los embutidos, de "
      "los quesos, de las conservas, de las salsas y de los precocinados. Quien "
      "quita el salero y sigue comiendo lo mismo apenas mueve la cifra, y quien "
      "cocina en casa con sal casi siempre está mejor que quien no la usa pero "
      "come de paquete."),
    sep(),
    h("Por qué el potasio va en la misma frase"),
    p("El efecto del sodio sobre la presión arterial depende en parte de cuánto "
      "potasio se come, y el patrón alimentario que las guías recomiendan opera "
      "en las dos direcciones a la vez: más verdura, fruta, legumbre y tubérculo "
      "suben el potasio y, por sustitución, bajan el sodio, porque desplazan "
      "precisamente a los alimentos que lo llevan. Es un caso claro de por qué "
      "las recomendaciones se dan en forma de patrón de comida y no de lista de "
      "moléculas."),
    p("La referencia de potasio se revisó en 2019 a la baja respecto a la "
      "anterior, y sigue sin tener techo para la ingesta alimentaria. Para los "
      "suplementos es otra historia y hay medicaciones —algunos "
      "antihipertensivos, algunos diuréticos— que retienen potasio. Con "
      "insuficiencia renal, este párrafo se invierte por completo y hay que "
      "seguir indicación médica y no un libro."),
    nota("El caso del deportista que sudó mucho",
         "En ejercicio prolongado con calor sí se pierden cantidades relevantes "
         "de sodio, y ahí la recomendación general de reducirlo no aplica durante "
         "la prueba. Es la única situación de este libro donde el consejo "
         "poblacional y el consejo del momento apuntan en sentidos opuestos, y "
         "merece decirse para que nadie se deshidrate por seguir bien una guía "
         "escrita para otra circunstancia."),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE IV · DE LAS CIFRAS A LA COMIDA
# ══════════════════════════════════════════════════════════════════════

C11 = cap(
    "El plato y la mano",
    p("Todo lo anterior son cifras, y nadie come cifras. Este capítulo es la "
      "traducción, y usa dos instrumentos que no se compran: la forma del plato y "
      "el tamaño de la mano."),
    fig("me-plato",
        "El reparto del plato y la mano como medida",
        "La mitad del plato de verdura y fruta, un cuarto de proteína y un cuarto "
        "de cereal o tubérculo reproduce sin contar nada un reparto que cae "
        "dentro de los rangos aceptables. Las cuatro medidas de la mano escalan "
        "con el cuerpo: una mano grande pertenece a una persona grande, que "
        "necesita más."),
    h("Por qué la mano funciona"),
    p("La objeción evidente a medir con la mano es que no es precisa, y la "
      "respuesta es que tampoco lo es la báscula cuando se usa dos semanas y se "
      "abandona. La mano tiene dos ventajas que ninguna balanza tiene: está "
      "siempre disponible y es proporcional a quien la lleva. Un hombre de "
      "noventa kilos tiene la palma más grande que una mujer de cincuenta y, sin "
      "hacer ninguna cuenta, su ración de proteína sale mayor en la proporción "
      "aproximadamente correcta."),
    ficha("Las cuatro medidas", [
        ("Palma sin dedos", "Una ración de proteína: carne, pescado, huevo, tofu, "
                            "legumbre cocida"),
        ("Puño cerrado", "Una ración de verdura. Una o dos por comida, sin "
                         "cálculo"),
        ("Mano en cuenco", "Una ración de cereal, tubérculo o fruta"),
        ("Pulgar entero", "Una ración de grasa densa: aceite, frutos secos, "
                          "aguacate, queso curado"),
    ]),
    p("Con dos raciones de proteína, dos o tres de verdura, dos de cereal y dos de "
      "grasa al día se cubre un patrón razonable para mucha gente. Quien entrena "
      "fuerte sube proteína y cereal; quien está en déficit baja cereal y grasa "
      "antes que proteína y verdura. No es exacto y no pretende serlo: pretende "
      "sobrevivir al mes tres, que es donde mueren los sistemas exactos."),
    sep(),
    h("La lista de la compra que sale de este libro"),
    p("No es una lista de superalimentos. Es la lista de las categorías que "
      "cubren los huecos que la tabla suele mostrar, ordenada por lo que resuelve "
      "cada una:"),
    lista(
        "Verdura de hoja verde: folato, vitamina K, potasio, magnesio, fibra. La "
        "categoría que más casillas tacha por unidad de esfuerzo.",
        "Legumbre: proteína, fibra, hierro no hemo, potasio, folato. Con vitamina "
        "C en la misma comida —un tomate, un pimiento, un cítrico— la absorción "
        "del hierro mejora de forma apreciable.",
        "Pescado azul: los ácidos grasos de cadena larga, vitamina D y yodo. Dos "
        "veces por semana es el consejo estándar de las guías.",
        "Huevo: proteína completa, colina, vitaminas del grupo B, y liposolubles "
        "en la yema. Rehabilitado hace años en las guías; la restricción "
        "sistemática que se recomendaba antaño ya no figura.",
        "Frutos secos y semillas: grasas esenciales, magnesio, vitamina E, fibra. "
        "Aquí es donde vive la nuez de Brasil, así que una o dos y no un puñado.",
        "Lácteo o su equivalente fortificado: calcio, proteína, vitamina B12 y a "
        "menudo vitamina D. Si se sustituye por bebida vegetal, comprobar que "
        "esté fortificada, porque la mayoría de las no fortificadas no aportan "
        "nada de esto.",
        "Sal yodada: es la vía por la que la población cubre el yodo. Sin ella y "
        "sin pescado ni lácteos, quedarse corto es fácil.",
    ),
    nota("Y una categoría más, para quien no come productos animales",
         "La vitamina B12 no está en los vegetales en forma aprovechable. No es "
         "una cuestión de planificar mejor: es un suplemento o un alimento "
         "fortificado, y no es opinable. El resto de una dieta vegetal bien "
         "llevada resiste cualquier análisis; este punto concreto no admite "
         "improvisación, y la carencia sostenida hace daño neurológico que no "
         "siempre se recupera."),
)

C12 = cap(
    "Lo que se puede afirmar y lo que se pidió y fue rechazado",
    p("Este es el capítulo que justifica media colección. En Europa existe un "
      "registro público donde consta cada declaración de propiedades saludables "
      "que se ha solicitado para un nutriente, su evaluación científica y el "
      "veredicto. La parte que se publicita es la de las autorizadas. La "
      "interesante es la otra."),
    h("Cómo funciona el registro"),
    p("Una empresa que quiere poner en un envase que su producto hace algo tiene "
      "que solicitar la autorización de esa frase. Un panel científico evalúa si "
      "existe una relación causa-efecto suficientemente establecida entre el "
      "nutriente y el efecto, y emite un dictamen. Después se autoriza o no. "
      "Todo el expediente queda público, incluidos los rechazos."),
    p("Eso convierte al registro en algo que no existe en ningún otro campo: una "
      "lista oficial de afirmaciones que la industria quiso hacer y no pudo "
      "sostener. No es material reservado; es material público que casi nadie "
      "consulta, y ahí está la diferencia."),
    sep(),
    h("Algunas autorizadas, con su letra pequeña"),
    lista(
        "La proteína contribuye al crecimiento y al mantenimiento de la masa "
        "muscular. Autorizada, y por eso la ves en todos los envases de batido.",
        "La creatina aumenta el rendimiento físico en series de ejercicios breves "
        "de alta intensidad. Autorizada con una condición de uso concreta, del "
        "orden de tres gramos diarios. Es una de las poquísimas ayudas "
        "ergogénicas con declaración autorizada, y conviene saber que la frase "
        "autorizada habla de series breves e intensas, no de resistencia ni de "
        "composición corporal.",
        "Las soluciones de hidratos y electrolitos contribuyen a mantener el "
        "rendimiento en ejercicio de resistencia prolongado. Autorizada; es la "
        "base legal de las bebidas deportivas, y la palabra «prolongado» hace "
        "todo el trabajo.",
        "La vitamina D contribuye al mantenimiento de huesos y a la función "
        "muscular normal. Autorizada. Nota la palabra «normal»: la declaración "
        "cubre el mantenimiento de una función, no una mejora del rendimiento.",
    ),
    h("Y algunas que se solicitaron y no se autorizaron"),
    lista(
        "Las declaraciones de la glucosamina sobre el cartílago y las "
        "articulaciones. Evaluadas y no autorizadas por relación causa-efecto "
        "insuficientemente establecida. Se sigue vendiendo con enorme éxito.",
        "Las declaraciones de los aminoácidos ramificados sobre la masa muscular "
        "y la recuperación. Evaluadas y no autorizadas.",
        "Las declaraciones de la L-carnitina sobre la oxidación de las grasas y "
        "el control del peso. Evaluadas y no autorizadas.",
        "Las declaraciones de pérdida de peso asociadas a los extractos de té "
        "verde. Evaluadas y no autorizadas.",
        "El término «antioxidante» como reclamo genérico. No es una declaración "
        "admisible por sí sola: hay que especificar el nutriente y el efecto "
        "concreto, y solo unos pocos tienen ese efecto reconocido.",
        "«Depurativo», «detox», «alcaliniza» y toda la familia. No existe "
        "declaración autorizada de esa naturaleza, lo que significa que cuando la "
        "lees en un envase estás leyendo algo que no ha pasado ninguna evaluación.",
    ),
    nota("El caso más curioso del registro: la cafeína",
         "El panel científico evaluó favorablemente varias declaraciones de la "
         "cafeína sobre el estado de alerta, la concentración y el rendimiento de "
         "resistencia. Aun así, esas declaraciones no llegaron a autorizarse por "
         "consideraciones de salud pública ajenas a la eficacia: preocupaba que "
         "animaran a consumirla más. Es el único ejemplo que conozco de una "
         "sustancia que superó la parte científica y no pasó la política, y "
         "explica por qué no verás esa frase en una lata aunque el efecto esté "
         "descrito."),
    sep(),
    h("La regla de lectura de etiquetas que sale de aquí"),
    pasos(
        "Busca la frase concreta. Si dice «contribuye al funcionamiento normal "
        "de», es una declaración autorizada y describe mantenimiento, no mejora.",
        "Desconfía de las frases que hablan de un producto en vez de un "
        "nutriente. Las declaraciones se autorizan para nutrientes; ningún envase "
        "tiene autorizado decir que él, específicamente, hace algo.",
        "Comprueba la condición de uso. Muchas declaraciones autorizadas exigen "
        "una cantidad mínima por porción, y un producto puede llevar el nutriente "
        "en cantidad simbólica y aun así nombrarlo.",
        "Si el reclamo está en el frente en letras grandes y no aparece en ningún "
        "sitio en la forma reglada, es marketing y no una propiedad evaluada.",
    ),
)


# ══════════════════════════════════════════════════════════════════════
#  PARTE V · EL OFICIO
# ══════════════════════════════════════════════════════════════════════

C13 = cap(
    "Cómo comprobarlo tú mismo",
    p("Un libro que dice «según los organismos oficiales» y no dice cuál ni dónde "
      "no se puede verificar, y por tanto no se puede corregir. Este capítulo es "
      f"el aparato de comprobación: {letras(len(D.FUENTES))} fuentes, todas "
      "gratuitas, todas en línea, con lo que se busca en cada una."),
    ficha("Las fuentes de este libro", [(n, d) for n, d in D.FUENTES]),
    sep(),
    h("Dónde se consulta cada cosa"),
    ficha("Rutas concretas", [
        ("RDA, AI y UL", "Las fichas de la Oficina de Suplementos Dietéticos del "
                         "Instituto Nacional de la Salud de Estados Unidos, en "
                         "ods.od.nih.gov. Hay una por nutriente, en versión para "
                         "público general y en versión para profesionales, y esa "
                         "segunda es la que trae las tablas completas."),
        ("Composición de alimentos", "FoodData Central, del Departamento de "
                                     "Agricultura, en fdc.nal.usda.gov. Se busca "
                                     "un alimento y da su perfil completo, "
                                     "nutriente por nutriente."),
        ("Patrones alimentarios y límites", "Las Dietary Guidelines for "
                                            "Americans, en health.gov. El "
                                            "documento entero se descarga en PDF."),
        ("Dosis de actividad física", "Las Physical Activity Guidelines for "
                                      "Americans, segunda edición, en el mismo "
                                      "sitio. Es la fuente del Códice de la Carga."),
        ("Doctrina de entrenamiento y sueño", "El FM 7-22, Holistic Health and "
                                              "Fitness, en la biblioteca de "
                                              "publicaciones del Ejército de "
                                              "Estados Unidos. Publicado íntegro "
                                              "y descargable."),
        ("Biomecánica de la carga", "La ecuación de levantamiento del NIOSH, en "
                                    "cdc.gov/niosh."),
        ("Declaraciones de salud en Europa", "El registro de la Comisión "
                                             "Europea. Se puede filtrar por "
                                             "nutriente y por estado, y el estado "
                                             "incluye las no autorizadas."),
    ]),
    nota("Por qué fuentes estadounidenses en un libro en español",
         "Por una razón puramente legal y una práctica. La legal: las obras del "
         "gobierno federal de Estados Unidos no están sujetas a copyright, lo que "
         "permite construir sobre ellas un libro que es enteramente propiedad de "
         "quien lo escribe. La práctica: son las tablas que el resto del mundo "
         "usa como referencia, incluidas las agencias europeas, que publican las "
         "suyas con valores muy próximos. Donde Europa difiere de forma "
         "relevante, este libro lo dice."),
    sep(),
    h("Y cómo se comprueba este libro a sí mismo"),
    p("Las cifras de estas páginas no se teclearon en el texto. Viven en un "
      "único módulo de datos que el programa de composición ejecuta antes de "
      "escribir una sola línea, y que se niega a seguir si alguna de estas "
      "comprobaciones falla:"),
    lista(
        "Que los tres rangos de macronutrientes admitan el cien por cien de la "
        "energía en algún punto.",
        "Que las dos cifras de fibra sean coherentes con la regla de catorce "
        "gramos por cada mil kilocalorías.",
        "Que las diecinueve filas de micronutrientes estén completas y que ningún "
        "valor recomendado supere su propio techo, salvo el caso del magnesio, "
        "cuya nota explica por qué.",
        "Que la equivalencia entre minutos moderados y vigorosos cuadre en los "
        "dos extremos del rango de actividad.",
        "Que cada actividad de la escala metabólica caiga dentro de la banda de "
        "intensidad que declara.",
    ),
    p("Esa última comprobación cazó un error real durante la escritura: yo había "
      "clasificado una intensidad como moderada cuando su valor la ponía justo "
      "en el umbral de vigorosa. Corregí el dato, no la comprobación. Lo cuento "
      "porque un libro que presume de rigor debería mostrar el momento en que el "
      "rigor le llevó la contraria."),
)

C14 = cap(
    "Cuaderno de la mesa",
    p("Cuatro semanas, y no una dieta. El cuaderno no impone qué comer: "
      "averigua qué comes, que es información que casi nadie tiene sobre sí "
      "mismo y que ninguna aplicación da porque las aplicaciones piden lo que "
      "creemos comer."),
    h("Semana 1 · Registrar sin cambiar nada"),
    pasos(
        "Anota lo que comes, sin pesar y sin juzgar. Alimento y tamaño "
        "aproximado en medidas de mano. Sin cifras.",
        "Marca cada comida con una de tres letras: C si la cocinaste, F si vino "
        "de un paquete, R si fue en un restaurante o similar.",
        "Al final de la semana cuenta las letras. Ese reparto explica tu ingesta "
        "de sodio, de azúcares añadidos y de fibra mejor que cualquier cálculo.",
        "No cambies nada esta semana. La medida se contamina si la intervención "
        "empieza antes.",
    ),
    h("Semana 2 · Las tres casillas"),
    pasos(
        "Cuenta cuántas comidas de la semana llevaron verdura. Objetivo de "
        "referencia: la mayoría.",
        "Cuenta cuántas llevaron una fuente clara de proteína del tamaño de tu "
        "palma.",
        "Cuenta cuántos días tomaste legumbre, fruto seco o semilla.",
        "Añade UNA de las tres donde falte, la que menos esfuerzo te cueste. Una, "
        "no las tres.",
    ),
    h("Semana 3 · Los huecos probables"),
    pasos(
        "Repasa la lista de categorías del capítulo del plato y marca las que no "
        "aparecen nunca en tu semana.",
        "Para cada hueco, mira en la tabla de los diecinueve qué nutrientes "
        "cubría esa categoría.",
        "Si el hueco es pescado azul, lácteo o alimento de origen animal, ahí es "
        "donde tiene sentido plantear un análisis o una consulta, no un bote "
        "elegido por internet.",
        "Escribe la pregunta que le harías a un profesional. Una frase. Esa frase "
        "es el producto de tres semanas de cuaderno.",
    ),
    h("Semana 4 · La auditoría del botiquín"),
    pasos(
        "Junta todos los suplementos y alimentos fortificados que tomas y "
        "escribe, nutriente por nutriente, cuánto suman al día.",
        "Compara cada suma con la columna del techo de la tabla de los "
        "diecinueve. Presta atención especial a vitamina B6, vitamina A "
        "preformada, hierro, selenio, zinc y magnesio en forma de sales.",
        "Cualquier suma que pase del techo, o que se acerque, va a la consulta. "
        "No se ajusta a ojo.",
        "Lo que no sepas justificar con un motivo concreto —una carencia "
        "documentada, una dieta que excluye una categoría, una etapa de la vida— "
        "es candidato a desaparecer. La mayoría de los botiquines pierden la "
        "mitad en este paso y nadie nota nada.",
    ),
    nota("Qué esperar del cuaderno",
         "No adelgaza. Lo que hace es convertir «creo que como bastante bien» en "
         "una descripción con datos, y de paso ahorrar dinero en productos que no "
         "hacían nada. Si al terminar las cuatro semanas tienes una frase clara "
         "para llevarle a un profesional y un botiquín más pequeño, el cuaderno "
         "cumplió."),
)

C15 = cap(
    "Lo que no se pregunta a una tabla",
    p("Último capítulo, y el que fija los límites. Hay preguntas que una tabla de "
      "referencia no puede contestar, y presionarla para que lo haga es la forma "
      "en que la nutrición divulgativa se convierte en daño."),
    h("Cinco preguntas para las que este libro no sirve"),
    lista(
        "«¿Cuánto tengo que comer para adelgazar X kilos en Y semanas?». Este "
        "libro trata de suficiencia de nutrientes, no de balance energético "
        "individual, y desconfía por principio de cualquier cifra prometida con "
        "plazo.",
        "«¿Qué tomo para mi enfermedad?». Ninguna cifra de aquí está establecida "
        "para condiciones clínicas, y varias se invierten en presencia de "
        "insuficiencia renal, hepática o cardíaca.",
        "«¿Vale esto en el embarazo?». No. Las referencias del embarazo y la "
        "lactancia son otras, algunas bastante distintas, y hay al menos un "
        "nutriente donde el margen es crítico. Esa etapa se lleva con seguimiento.",
        "«¿Sirve para mi hijo?». No. Toda la tabla es de adultos. Las referencias "
        "pediátricas cambian con la edad y con el peso, y extrapolar por regla de "
        "tres es un error.",
        "«¿Estoy deficiente?». Eso se contesta con una analítica y un contexto "
        "clínico, nunca con un registro de comida. Ninguna app tiene esa "
        "información.",
    ),
    h("Tres señales de que hay que consultar y no leer"),
    lista(
        "Pérdida de peso sin proponérselo, cansancio persistente, caída de pelo "
        "marcada o cualquier cambio digestivo que dure semanas.",
        "Cualquier plan que te haga excluir un grupo entero de alimentos durante "
        "más de unas semanas, sea el que sea y por buena que suene la razón.",
        "Cualquier suplemento que tomes sin poder explicar en una frase para qué "
        "es y cómo sabrás si funcionó.",
    ),
    sep(),
    h("Glosario"),
    ficha("", [
        ("AI · Ingesta adecuada", "Valor de referencia usado cuando no hay datos "
                                  "para calcular un requerimiento medio. Menos "
                                  "sólido que un RDA."),
        ("AMDR · Rango aceptable", "Intervalo de porcentaje de la energía que "
                                   "puede aportar un macronutriente."),
        ("Biodisponibilidad", "Proporción de un nutriente ingerido que llega a "
                              "estar realmente disponible para el organismo."),
        ("CDRR", "Valor de reducción del riesgo crónico. Categoría introducida "
                 "para el sodio en 2019."),
        ("DFE · Equivalente de folato", "Unidad que corrige la distinta "
                                        "absorción del folato natural y del ácido "
                                        "fólico sintético."),
        ("EAR · Requerimiento medio", "Cantidad que cubre la necesidad de la "
                                      "mitad de la población. Sirve para evaluar "
                                      "grupos, no individuos."),
        ("Fitato", "Compuesto de cereales integrales y legumbres que reduce la "
                   "absorción de varios minerales."),
        ("Hierro hemo y no hemo", "El primero, de origen animal, se absorbe "
                                  "bastante mejor; el segundo, vegetal, depende "
                                  "del acompañamiento."),
        ("MET", "Equivalente metabólico. Múltiplo del gasto en reposo. Se usa en "
                "el Códice de la Carga."),
        ("NE · Equivalente de niacina", "Unidad que incluye la niacina fabricada "
                                        "a partir de triptófano."),
        ("RAE · Equivalente de retinol", "Unidad que corrige la distinta "
                                         "actividad del retinol y de los "
                                         "carotenoides."),
        ("RDA · Ingesta recomendada", "Requerimiento medio más dos desviaciones "
                                      "típicas. Cubre a cerca del 97 % de la "
                                      "población."),
        ("UL · Límite superior", "Techo por encima del cual el riesgo de efectos "
                                 "adversos empieza a aumentar."),
    ]),
    sep(),
    p("Y con esto se cierra el primero de los cuatro Códices de fitness. No "
      "trae ninguna dieta, y eso es lo que ofrece: la tabla completa en vez de la "
      "mitad publicitable, las fuentes con nombre para que puedas discutirle al "
      "libro, y una advertencia repetida las veces necesarias de que ninguna "
      "cifra poblacional es una prescripción para una persona."),
    p("El siguiente se ocupa de lo que se hace con el cuerpo, y empieza con la "
      "cifra de actividad física que un gobierno estableció y casi nadie ha "
      "leído entera."),
)



# ══════════════════════════════════════════════════════════════════════
#  CAPÍTULOS AÑADIDOS EN LA SEGUNDA EDICIÓN
# ══════════════════════════════════════════════════════════════════════

CE1 = cap(
    "De qué se compone el gasto de un día",
    p("Antes de hablar de cuánto comer conviene saber en qué se va la energía, "
      "porque el reparto real no se parece nada al que la gente imagina. Casi "
      "todo el mundo cree que el ejercicio es el gran sumidero del día. Es el "
      "más pequeño de los cuatro."),
    fig("me-gasto",
        "Los cuatro componentes del gasto diario",
        "Porcentajes del gasto total, en rangos típicos. El metabolismo basal se "
        "lleva la mayor parte y apenas se puede cambiar a voluntad; la actividad "
        "no deportiva es el componente más variable entre personas; el ejercicio "
        "estructurado, en la mayoría de la gente, es la porción menor."),
    ficha("Los cuatro, uno por uno",
          [(nombre, f"del {lo} al {hi} % · {nota[0].lower() + nota[1:]}")
           for nombre, lo, hi, nota in D.GASTO]),
    h("La consecuencia incómoda"),
    p("Si el ejercicio estructurado es como mucho una fracción modesta del "
      "gasto, entonces intentar compensar comida con ejercicio es una batalla "
      "perdida de antemano por pura aritmética. Media hora de carrera decente "
      "ronda las cuatrocientas kilocalorías en una persona de setenta kilos; una "
      "cena de restaurante puede llevar el doble en veinte minutos y sin "
      "esfuerzo. Este dato no es un argumento contra el ejercicio: es un "
      "argumento contra usarlo para lo que no sirve."),
    p("Y en la otra dirección hay una noticia mejor. La actividad no deportiva "
      "—andar, estar de pie, subir escaleras, moverse mientras se trabaja— puede "
      "duplicarse entre dos personas del mismo peso, y en el conjunto del día "
      "aporta bastante más que la sesión de gimnasio. Es el componente sobre el "
      "que más se puede influir sin quitarle tiempo a nada."),
    sep(),
    h("El componente que se hunde en silencio"),
    p("Cuando alguien reduce mucho lo que come de forma sostenida, ese "
      "componente baja sin que la persona lo decida ni lo note: se mueve menos, "
      "gesticula menos, sube menos escaleras, pasa más rato sentada. La "
      "consecuencia práctica es que el déficit real acaba siendo menor que el "
      "planeado, y de ahí buena parte de la frustración de los meses tres y "
      "cuatro de cualquier dieta."),
    p("El antídoto no es apretar más. Es proteger deliberadamente el movimiento "
      "cotidiano —un objetivo de pasos, subir andando, llamadas de pie— "
      "precisamente en las etapas en que se come menos. Es de las cosas más "
      "útiles que se pueden hacer y no aparece en ninguna dieta."),
    nota("El efecto térmico y la proteína",
         "De los tres macronutrientes, el que más energía cuesta procesar es la "
         "proteína, con diferencia. No convierte a nadie en una máquina de "
         "quemar grasa —la magnitud es modesta— pero explica parte de por qué "
         "las dietas con más proteína salen algo mejor en los estudios de "
         "pérdida de peso, junto con la saciedad, que probablemente pesa más."),
)

CE2 = cap(
    "Cómo se lee una etiqueta",
    p("La etiqueta de un envase es el único documento nutricional que la mayoría "
      "de la gente tiene delante todos los días, y casi nadie sabe leerlo. Tiene "
      "cuatro trampas conocidas y una franja de tolerancia legal que muy poca "
      "gente sospecha."),
    fig("me-etiqueta",
        "Anatomía de una etiqueta y sus tolerancias legales",
        "La columna por cien gramos es la única comparable entre productos. La "
        "porción la elige el fabricante. Y a la derecha, la tolerancia: el valor "
        "declarado no es un número, es una franja."),
    h("La primera trampa: la porción"),
    p("La ley obliga a declarar los valores por cien gramos, y eso es lo que "
      "hace comparables dos productos. Junto a esa columna suele aparecer otra "
      "«por porción», y la porción la decide quien vende. Una porción de treinta "
      "gramos de un cereal de desayuno es aproximadamente una cuarta parte de lo "
      "que cualquiera se sirve, y todas las cifras de esa columna están "
      "divididas por cuatro respecto a lo que va a pasar de verdad."),
    p("Regla: comparar siempre por cien gramos, y después mirar cuánto se come "
      "de verdad. Nunca al revés."),
    h("La segunda: el orden de los ingredientes"),
    p("Los ingredientes van por peso descendente, y eso convierte a la lista en "
      "una radiografía bastante honesta. Si el azúcar aparece en los tres "
      "primeros puestos, el producto es principalmente azúcar por mucho que la "
      "portada hable de fibra. La contramedida de la industria es dividir el "
      "azúcar en varios nombres —jarabe, dextrosa, concentrado de zumo, melaza— "
      "para que cada uno pese menos y baje puestos. Sumarlos mentalmente "
      "devuelve la imagen real."),
    h("La tercera: las palabras que no significan nada"),
    lista(
        "«Natural» no tiene una definición reglada que sirva para juzgar nada.",
        "«Artesano», «casero», «de siempre», «receta tradicional» son estilo, no "
        "composición.",
        "«Sin azúcares añadidos» no equivale a poco azúcar: un zumo cumple y "
        "lleva tanto azúcar como un refresco.",
        "«Light» solo obliga a una reducción respecto al producto de referencia, "
        "que puede seguir siendo altísimo en términos absolutos.",
        "«Enriquecido con vitaminas» suele señalar un producto que necesitaba "
        "una razón para estar en el carro.",
    ),
    sep(),
    h("La cuarta, y la que nadie cuenta: la tolerancia"),
    p("Las normas de etiquetado admiten una diferencia entre lo declarado y lo "
      "medido, y las cifras son públicas. Para lo que conviene limitar —calorías, "
      "azúcares, grasas, sodio— el valor medido no debe superar en más de una "
      "quinta parte al declarado. Para lo que conviene alcanzar —vitaminas, "
      "minerales, proteína, fibra— el medido debe llegar al menos a cuatro "
      "quintos de lo declarado."),
    p(D.ETIQUETA["nota"]),
    p("De aquí se sigue algo práctico: contar calorías con dos decimales es "
      "aritmética de fantasía. Un día entero de comida envasada puede llevar una "
      "desviación apreciable respecto a lo apuntado sin que nadie haya "
      "incumplido nada. Eso no invalida el registro; invalida la precisión "
      "falsa, y aconseja usar tendencias de varias semanas en vez de cuadrar "
      "días sueltos."),
    nota("La lectura de treinta segundos",
         "En la práctica, tres miradas bastan para casi todo: la columna por cien "
         "gramos, los tres primeros ingredientes y la cifra de sal. Con eso se "
         "distingue un alimento de un producto sin haber aprendido nada de "
         "bioquímica."),
)

CE3 = cap(
    "Comer alrededor del entrenamiento",
    p("Es la pregunta que más se hace y la que menos importa, y merece un "
      "capítulo precisamente para ponerla en su sitio. El orden de importancia "
      "va de arriba abajo, y la mayoría de la gente empieza por el último "
      "escalón."),
    ficha("Orden de importancia real", [
        ("1 · El total del día", "Energía y proteína totales. Aquí se decide "
                                 "casi todo, y sin esto ordenado el resto no "
                                 "cambia nada."),
        ("2 · La calidad del patrón", "Que haya verdura, fruta, legumbre, "
                                      "cereal poco procesado y una fuente "
                                      "proteica decente."),
        ("3 · El reparto a lo largo del día", "Repartir la proteína en tres o "
                                              "cuatro tomas en vez de "
                                              "concentrarla. Efecto modesto y "
                                              "real."),
        ("4 · El momento exacto respecto a la sesión", "La famosa ventana. Es el "
                                                       "escalón más pequeño de "
                                                       "los cuatro."),
    ]),
    h("Qué pasó con la ventana anabólica"),
    p("Durante años se enseñó que había una media hora sagrada después de "
      "entrenar en la que había que meter proteína o se perdía la sesión. Esa "
      "urgencia no ha resistido bien el examen: si se ha comido en las horas "
      "previas, el margen es de horas y no de minutos, y el total del día pesa "
      "muchísimo más."),
    p("Donde el momento sí importa es en dos situaciones concretas y acotadas: "
      "cuando se entrena en ayunas y la comida siguiente queda muy lejos, y "
      "cuando hay dos sesiones exigentes separadas por pocas horas, que es "
      "situación de deportista y no de la mayoría."),
    sep(),
    h("Antes de entrenar"),
    lista(
        "Una comida normal dos o tres horas antes funciona para casi todo el "
        "mundo y no requiere nada especial.",
        "Si se entrena poco después de comer, conviene bajar la grasa y la "
        "fibra de esa comida: retrasan el vaciado del estómago y es lo que "
        "produce la sensación de piedra.",
        "Entrenar en ayunas no es peligroso ni mágico. Rinde algo peor en "
        "sesiones largas o muy intensas y da igual en sesiones cortas. Es una "
        "preferencia, no una estrategia.",
        "El café antes de entrenar tiene un efecto sobre el rendimiento bien "
        "descrito. Ojo con la hora: el capítulo de la cafeína del Códice del "
        "Descanso explica por qué una sesión de tarde puede costar sueño.",
    ),
    h("Durante"),
    p("Por debajo de una hora de esfuerzo, agua. A partir de ahí, y sobre todo "
      "con calor o en pruebas largas, tiene sentido aportar hidratos y "
      "electrolitos: es exactamente la única declaración de salud autorizada "
      "para las bebidas deportivas, y la palabra que hace todo el trabajo en esa "
      "frase es «prolongado»."),
    h("Después"),
    p("Una comida normal con proteína y con hidratos, cuando toque. Si la sesión "
      "fue muy dura y la siguiente es mañana, no hay ninguna prisa. Si hay otra "
      "sesión dentro de pocas horas, entonces sí conviene comer pronto y "
      "priorizar los hidratos, porque el depósito de glucógeno tarda en "
      "reponerse y ahí el reloj sí corre."),
    nota("El agua y el peso de después",
         "Perder un kilo durante una sesión larga es agua, no grasa, y conviene "
         "reponerla a lo largo de las horas siguientes con bebida y con comida "
         "que lleve sal. Pesarse justo después de entrenar y celebrar el número "
         "es el error de interpretación más común del gimnasio."),
)

CE4 = cap(
    "Lo que no se cocina bien hace más daño que lo que se come mal",
    p("Este capítulo no aparece en ningún libro de fitness y debería aparecer en "
      "todos. Un plan de alimentación impecable ejecutado con un pollo mal "
      "conservado produce en dos días más perjuicio del que compensan seis meses "
      "de macros perfectos. Las cifras que siguen son públicas, del servicio de "
      "inocuidad alimentaria estadounidense, y son sencillas."),
    fig("me-inocuidad",
        "La zona de peligro y las temperaturas que hay que superar",
        "Entre los cuatro y los sesenta grados las bacterias se multiplican con "
        "rapidez. Las temperaturas internas seguras están todas por encima de "
        "esa franja, y ninguna se alcanza por color: se miden."),
    ficha("Temperaturas internas seguras",
          [(alimento, f"{grados} °C · {nota[0].lower() + nota[1:]}")
           for alimento, grados, nota in D.INOCUIDAD]),
    h("Por qué la carne picada necesita más temperatura que el filete"),
    p("Es la pregunta que revela si alguien ha entendido el asunto. En un corte "
      "entero, la contaminación está en la superficie, y la superficie es "
      "justamente lo que recibe el calor directo: por eso un filete poco hecho "
      "por dentro puede ser seguro. Al picar la carne, esa superficie se "
      "distribuye por toda la masa, así que el interior necesita alcanzar la "
      "temperatura por sí mismo. Una hamburguesa poco hecha no es lo mismo que "
      "un entrecot poco hecho, y la diferencia no es de gusto."),
    sep(),
    h("Los cuatro pasos"),
    ficha("", [(nombre, glosa) for nombre, glosa in D.ZONA_PELIGRO["pasos"]]),
    p("El paso que más se salta es el cuarto. Dejar enfriar una olla grande "
      "sobre la encimera toda la tarde la mantiene horas dentro de la zona de "
      "peligro por pura inercia térmica, aunque la superficie parezca fría. La "
      "solución es repartir en recipientes bajos y meterlos pronto: enfrían en "
      "una fracción del tiempo."),
    ficha("Los márgenes de tiempo", [
        ("A temperatura ambiente",
         f"como mucho {D.ZONA_PELIGRO['horas']} horas fuera de la nevera"),
        ("Con más de 32 °C",
         f"como mucho {D.ZONA_PELIGRO['horas_calor']} hora"),
        ("Nevera", f"{D.ZONA_PELIGRO['nevera']} °C o menos, comprobado con "
                   "termómetro y no con la rueda del mando"),
        ("Congelador", f"{D.ZONA_PELIGRO['congelador']} °C. Congelar no mata "
                       "bacterias: las detiene. Al descongelar vuelven a "
                       "multiplicarse"),
    ]),
    h("Tres cosas que casi todo el mundo hace mal"),
    lista(
        "Descongelar sobre la encimera. La superficie entra en la zona de "
        "peligro mucho antes de que el centro se descongele. Se descongela en la "
        "nevera, en agua fría cambiada cada media hora, o en el microondas para "
        "cocinar inmediatamente después.",
        "Lavar el pollo crudo bajo el grifo. No elimina bacterias y salpica "
        "gotas a más de medio metro alrededor, contaminando fregadero, encimera "
        "y lo que haya cerca. El calor de la sartén hace ese trabajo; el grifo "
        "solo lo reparte.",
        "Usar el mismo plato para llevar la carne cruda a la parrilla y "
        "recogerla hecha. Es la vía de contaminación cruzada más frecuente en "
        "cualquier cocina doméstica, y se resuelve con un plato limpio.",
    ),
    nota("Quién tiene que ser más estricto",
         "Embarazadas, mayores, niños pequeños y personas con la inmunidad "
         "comprometida tienen un riesgo apreciablemente mayor, y en ese caso "
         "algunas categorías —quesos de leche cruda, huevo crudo, pescado crudo, "
         "embutidos no curados, brotes germinados— dejan de ser una cuestión de "
         "preferencia. Si estás en alguno de esos grupos, esto se consulta y no "
         "se improvisa."),
)

CE5 = cap(
    "Las cuatro situaciones en las que la tabla cambia",
    p("Todo lo anterior está escrito para un adulto sano. Hay al menos cuatro "
      "situaciones en las que las cifras se mueven, y en dos de ellas se mueven "
      "tanto que aplicar la tabla general es un error."),
    h("1 · A partir de los sesenta y cinco"),
    ficha("Lo que cambia", [
        ("Proteína", "El suelo poblacional de 0,8 g/kg se queda corto para "
                     "frenar la pérdida de masa muscular asociada a la edad. La "
                     "literatura geriátrica maneja cifras claramente mayores. "
                     "Esto no sale de las tablas de referencia: sale de otra "
                     "literatura, y lo digo."),
        ("Vitamina D", "La referencia sube a partir de los 71 años, y la "
                       "síntesis en la piel disminuye con la edad."),
        ("Vitamina B12", "La absorción empeora por la menor acidez gástrica, y "
                         "por eso a esta edad se recomienda a menudo la forma de "
                         "alimentos fortificados o suplemento, que se absorbe "
                         "mejor que la de la carne."),
        ("Calcio", "La referencia sube en mujeres desde los 51 y en hombres "
                   "desde los 71."),
        ("Agua", "La sensación de sed disminuye con la edad, así que el aviso "
                 "interno deja de ser fiable y hay que beber por horario."),
    ]),
    h("2 · Dieta sin productos de origen animal"),
    p("Es una dieta que resiste cualquier análisis si se lleva con atención, y "
      "tiene exactamente cinco puntos que exigen atención y no opinión:"),
    lista(
        "Vitamina B12: suplemento o alimento fortificado. Sin excepciones y sin "
        "debate. La carencia sostenida produce daño neurológico que no siempre "
        "revierte.",
        "Hierro: se absorbe bastante peor el de origen vegetal, y las propias "
        "fuentes oficiales señalan una necesidad notablemente mayor. La vitamina "
        "C en la misma comida ayuda de forma apreciable.",
        "Zinc: los fitatos de legumbres y cereales integrales reducen su "
        "absorción, y la necesidad puede subir hasta la mitad. Remojar, "
        "fermentar y germinar reduce el efecto.",
        "Yodo: sin pescado ni lácteos, la sal yodada es la vía. Las algas son "
        "una fuente imprevisible: algunas llevan cantidades enormes y superan el "
        "techo con facilidad.",
        "Grasas de cadena larga: la conversión desde las vegetales es limitada. "
        "Existe una alternativa de origen no animal para quien quiera cubrirlo.",
    ),
    h("3 · Quien entrena en serio"),
    p("Cambia sobre todo la proteína, ya tratada, y cambia la energía total, que "
      "es lo que casi nadie ajusta. Comer para entrenar cinco horas semanales no "
      "es lo mismo que comer para entrenar una, y la señal más común de que la "
      "energía se ha quedado corta no es el hambre: es la fatiga persistente, el "
      "sueño malo, el estancamiento del rendimiento y, en mujeres, la alteración "
      "del ciclo, que es un signo que merece consulta y no ajuste por internet."),
    h("4 · Embarazo y lactancia"),
    p("Aquí este libro se detiene. Las referencias cambian en varios nutrientes, "
      "en algunos de forma sustancial, hay uno donde el margen es crítico y hay "
      "categorías de alimentos con recomendaciones específicas por riesgo "
      "microbiológico. Es la única situación de todo el libro en la que no doy "
      "ninguna cifra: se sigue el seguimiento profesional y punto."),
    nota("Y una quinta que no es una situación sino una advertencia",
         "Cualquier enfermedad renal, hepática, cardíaca o digestiva reordena "
         "esta tabla, y en algunos casos la invierte: hay nutrientes que pasan "
         "de recomendables a limitados. Si tienes un diagnóstico, la tabla que "
         "vale es la que te dé quien te trata, no esta."),
)


# ══════════════════════════════════════════════════════════════════════
LIBRO = {
    "id": "codice-mesa",
    "titulo": "Códice de la Mesa",
    "subtitulo": "Nutrición con las dos columnas de la tabla: lo que hay que tomar, lo que conviene no pasar y de dónde sale cada cifra",
    "autor": "Villumination 99",
    "fuente": "Obra original · Primera edición, 2026",
    "mascota": "r-mesa",
    "acento": "mesa",
    "original": True,
    "laminas": ["mesa.svg"],
    "claves": ["nutrición", "micronutrientes", "límite superior tolerable",
               "macronutrientes", "fibra", "suplementación", "etiquetado",
               "villuminations"],
    "capitulos": [
        C1, C2,                          # I · Cómo se lee una tabla
        CE1, C3, C4, C5, C6, C7,         # II · La energía y su reparto
        C8, C9, C10,                     # III · La tabla entera
        C11, CE2, CE3, CE4, C12,         # IV · De las cifras a la comida
        CE5, C13, C14, C15,              # V · El oficio
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
          f"{palabras:,} palabras · {len(D.MICRO)} micronutrientes con techo · "
          f"→ {destino.relative_to(SRC.parent)}")


if __name__ == "__main__":
    main()
