#!/usr/bin/env python3
"""
DATOS OFICIALES — tablas de referencia de los Códices de fitness
===============================================================
Módulo compartido por el Códice de la Mesa, el de la Carga, el de la Voluntad y
el del Descanso. Aquí viven los valores de referencia y aquí se comprueban.

POR QUÉ ESTAS FUENTES Y NO OTRAS
Las obras del gobierno federal de Estados Unidos no están sujetas a copyright
(17 U.S.C. § 105). Eso convierte a un puñado de organismos en la única fuente
de datos de nutrición y entrenamiento que es a la vez de primer nivel y
legalmente libre:

  · DRI · Dietary Reference Intakes — las ingestas de referencia (RDA, AI, UL)
    establecidas por los comités del National Academies / Institute of
    Medicine y difundidas por la Oficina de Suplementos Dietéticos del NIH.
  · Physical Activity Guidelines for Americans, 2.ª edición (HHS, 2018) — la
    dosis de actividad física con su curva de respuesta.
  · Dietary Guidelines for Americans (USDA y HHS) — los patrones de dieta.
  · FoodData Central (USDA) — composición de alimentos.
  · FM 7-22 Holistic Health and Fitness (Ejército de EE. UU.) — doctrina de
    entrenamiento, sueño y nutrición de una institución que entrena a un millón
    de personas y publica su método entero.
  · Ecuación de levantamiento del NIOSH (CDC) — biomecánica de la carga.
  · Investigación de la NASA sobre descarga y reposo en cama — lo que le pasa a
    un cuerpo al que se le quita el peso.

A eso se suma, para Europa, el registro de declaraciones de propiedades
saludables de la Comisión Europea con las evaluaciones de EFSA: la lista
pública de lo que legalmente se puede afirmar de un nutriente y —lo
interesante— de lo que se pidió afirmar y fue RECHAZADO.

Nada de esto es material reservado. Es material público que casi nadie abre, y
esa es exactamente la diferencia que aprovecha esta colección.

ADVERTENCIA QUE VIAJA CON LOS DATOS
Los valores de referencia son poblacionales: describen lo que cubre las
necesidades de la mayoría de adultos sanos. No son una prescripción
individual, no consideran patologías, embarazo, lactancia ni medicación, y
ningún libro puede sustituir la valoración de un profesional sanitario.
"""

# ══════════════════════════════════════════════════════════════════════
#  MACRONUTRIENTES · rangos aceptables de distribución (AMDR) y mínimos
# ══════════════════════════════════════════════════════════════════════
# El AMDR es un rango de porcentaje de la energía total. Los tres suman 100 en
# sus extremos, y esa comprobación es la que hace este módulo.
AMDR = [
    # nutriente, mínimo %, máximo %, nota
    ("Hidratos de carbono", 45, 65,
     "Mínimo absoluto de 130 g al día, que es lo que consume el cerebro"),
    ("Grasas", 20, 35,
     "Por debajo del 20 % cuesta cubrir las grasas esenciales y las vitaminas "
     "liposolubles"),
    ("Proteínas", 10, 35,
     "El RDA es 0,8 g por kilo de peso, que para la mayoría cae cerca del 10 %"),
]

PROTEINA = {
    "rda": 0.8,                  # g por kg de peso corporal y día
    "amdr_min": 10, "amdr_max": 35,
    "nota": "El RDA de 0,8 g/kg es la cantidad que evita el déficit, no la que "
            "optimiza la ganancia de masa. Es un suelo, no un objetivo.",
}

FIBRA = {
    "hombres": 38, "mujeres": 25,      # g al día, AI
    "por_1000_kcal": 14,
    "nota": "La AI se fija en 14 g por cada 1 000 kcal, y de ahí salen las dos "
            "cifras según la ingesta energética típica de cada sexo.",
}

AGUA = {
    "hombres": 3.7, "mujeres": 2.7,    # litros al día, AI, TOTAL
    "nota": "Es agua TOTAL: incluye la de los alimentos y la de todas las "
            "bebidas. Alrededor del 20 % suele venir de la comida, así que el "
            "agua bebida queda bastante por debajo de esa cifra.",
}

# ══════════════════════════════════════════════════════════════════════
#  MICRONUTRIENTES · la tabla con su mitad olvidada
# ══════════════════════════════════════════════════════════════════════
# Casi todas las tablas divulgativas imprimen el RDA y se callan el UL, que es
# el límite superior tolerable. Aquí van los dos, porque el UL es la parte que
# de verdad hace falta cuando alguien se está suplementando.
#   clave: (nombre, unidad, rda_hombre, rda_mujer, ul, nota)
MICRO = [
    ("Vitamina A", "µg RAE", 900, 700, 3000,
     "El UL es solo para la forma preformada (retinol), no para los "
     "carotenoides de los vegetales"),
    ("Vitamina C", "mg", 90, 75, 2000,
     "Quien fuma necesita 35 mg más al día"),
    ("Vitamina D", "µg", 15, 15, 100,
     "15 µg son 600 UI. A partir de los 71 años, 20 µg. El UL de 100 µg son "
     "4 000 UI"),
    ("Vitamina E", "mg", 15, 15, 1000,
     "El UL se refiere a las formas suplementarias, no a la de los alimentos"),
    ("Vitamina K", "µg", 120, 90, None,
     "Es AI, no RDA, y no tiene UL establecido. Interacciona con "
     "anticoagulantes: consultar"),
    ("Tiamina · B1", "mg", 1.2, 1.1, None, "Sin UL establecido"),
    ("Riboflavina · B2", "mg", 1.3, 1.1, None, "Sin UL establecido"),
    ("Niacina · B3", "mg NE", 16, 14, 35,
     "El UL de 35 mg es para el ácido nicotínico de suplementos: por encima da "
     "rubor y afecta al hígado"),
    ("Vitamina B6", "mg", 1.3, 1.3, 100,
     "El exceso sostenido produce neuropatía. Es uno de los UL que más se "
     "rebasan sin saberlo"),
    ("Folato", "µg DFE", 400, 400, 1000,
     "El UL de 1 000 µg es solo para el ácido fólico de suplementos y "
     "alimentos fortificados"),
    ("Vitamina B12", "µg", 2.4, 2.4, None,
     "Sin UL. Quien no come productos de origen animal necesita suplemento: "
     "esto no es opinable"),
    ("Calcio", "mg", 1000, 1000, 2500,
     "Las mujeres de 51 años en adelante y los hombres de 71 en adelante, "
     "1 200 mg"),
    ("Hierro", "mg", 8, 18, 45,
     "Los 18 mg son para mujeres con menstruación. Suplementar sin analítica "
     "es mala idea: el exceso se acumula"),
    ("Magnesio", "mg", 420, 320, 350,
     "Único caso en que el UL parece menor que el RDA: el UL de 350 mg se "
     "refiere SOLO al magnesio de suplementos, no al de los alimentos"),
    ("Zinc", "mg", 11, 8, 40,
     "El exceso sostenido interfiere con la absorción de cobre"),
    ("Selenio", "µg", 55, 55, 400,
     "Margen estrecho: el exceso es tóxico y la fuente más común de exceso son "
     "las nueces de Brasil"),
    ("Yodo", "µg", 150, 150, 1100, "Sin sal yodada es fácil quedarse corto"),
    ("Potasio", "mg", 3400, 2600, None,
     "Es AI, revisada en 2019. Sin UL para la ingesta alimentaria"),
    ("Sodio", "mg", 1500, 1500, None,
     "La AI es 1 500 mg. El límite de referencia para reducir riesgo (CDRR) "
     "está en 2 300 mg, que es lo que llevan unos 6 g de sal"),
]

# ══════════════════════════════════════════════════════════════════════
#  ACTIVIDAD FÍSICA · Physical Activity Guidelines, 2.ª edición
# ══════════════════════════════════════════════════════════════════════
ACTIVIDAD = {
    "moderada_min": 150, "moderada_max": 300,   # minutos por semana
    "vigorosa_min": 75, "vigorosa_max": 150,
    "fuerza_dias": 2,                            # días por semana, mínimo
    "equivalencia": 2,       # un minuto vigoroso cuenta como dos moderados
    "notas": [
        "La 2.ª edición de 2018 eliminó el requisito de que la actividad se "
        "acumulara en tandas de diez minutos o más. Ahora cuenta todo, desde el "
        "primer minuto.",
        "No hay un umbral por debajo del cual no haya beneficio. La curva de "
        "respuesta empieza a subir enseguida y su tramo más rentable está entre "
        "cero y los primeros 150 minutos.",
        "Por encima de 300 minutos semanales el beneficio sigue creciendo, pero "
        "cada minuto añadido rinde menos que el anterior.",
        "El trabajo de fuerza de dos días por semana no es opcional en las "
        "recomendaciones: figura al mismo nivel que el aerobio.",
    ],
}

# Equivalentes metabólicos: cuántas veces el gasto en reposo. Cifras de las
# tablas de compendio que usan las guías oficiales para clasificar intensidad.
MET = [
    ("Sentado, en reposo", 1.0, "reposo"),
    ("De pie, quieto", 1.3, "reposo"),
    ("Caminar despacio · 3 km/h", 2.5, "ligera"),
    ("Caminar a paso vivo · 5 km/h", 3.5, "moderada"),
    ("Bicicleta tranquila · 14 km/h", 4.0, "moderada"),
    ("Pesas, sesión general", 3.5, "moderada"),
    ("Pesas, esfuerzo alto", 6.0, "vigorosa"),
    ("Bicicleta · 20 km/h", 8.0, "vigorosa"),
    ("Trotar · 8 km/h", 8.0, "vigorosa"),
    ("Correr · 11 km/h", 11.0, "vigorosa"),
    ("Cuerda, ritmo rápido", 12.3, "vigorosa"),
]
# Los umbrales que usan las guías para clasificar
UMBRAL_MET = {"ligera": 1.6, "moderada": 3.0, "vigorosa": 6.0}

# ══════════════════════════════════════════════════════════════════════
#  DESCARGA · qué pasa cuando se le quita el peso a un cuerpo
# ══════════════════════════════════════════════════════════════════════
# Órdenes de magnitud de la literatura de reposo en cama y vuelo espacial. Se
# dan como rangos porque los estudios difieren según duración, población y
# método de medida; lo que no difiere es el signo.
DESCARGA = [
    ("Masa muscular", "1 a 2 % por semana",
     "En reposo en cama estricto. Los extensores de la pierna y la espalda son "
     "los primeros y los que más pierden"),
    ("Fuerza", "Cae más rápido que la masa",
     "La pérdida de fuerza precede a la de tamaño: parte es nerviosa"),
    ("Densidad mineral ósea", "En torno a 1 a 1,5 % al mes",
     "En huesos de carga —cadera, columna lumbar, calcáneo—. Los brazos apenas "
     "cambian"),
    ("Volumen plasmático", "Baja en los primeros días",
     "De ahí el mareo al incorporarse tras días en cama"),
    ("Capacidad aeróbica", "Medible en una o dos semanas",
     "Se recupera antes que el hueso, que es lo más lento de todo"),
]

# ══════════════════════════════════════════════════════════════════════
#  SUEÑO
# ══════════════════════════════════════════════════════════════════════
SUENO = {
    "adulto_horas": 7,          # horas o más, recomendación de salud pública
    "ciclo_min": 90,            # duración aproximada de un ciclo
    "ciclos_noche": (4, 6),
    "fases": [
        ("N1", "Transición", "1 a 5 min", "Muy ligero. Se puede negar haber "
                                          "dormido"),
        ("N2", "Sueño ligero", "La mayor parte de la noche",
         "Aquí se consolida buena parte de la memoria de procedimiento"),
        ("N3", "Sueño profundo", "Concentrado en la primera mitad",
         "El de la recuperación física. Si se recorta el sueño por el final, "
         "este se conserva"),
        ("REM", "Movimientos oculares rápidos", "Crece en cada ciclo",
         "Concentrado en la segunda mitad. Si se recorta el sueño por el final, "
         "este es el que se pierde"),
    ],
}

# ══════════════════════════════════════════════════════════════════════
#  NIOSH · ecuación de levantamiento
# ══════════════════════════════════════════════════════════════════════
NIOSH = {
    "carga_constante": 23,      # kg, en condiciones ideales
    "factores": [
        ("HM", "Horizontal", "Distancia de la carga al cuerpo. Es el factor que "
                             "más penaliza: alejar la carga la multiplica"),
        ("VM", "Vertical", "Altura de las manos al empezar"),
        ("DM", "Distancia", "Cuánto sube la carga"),
        ("AM", "Asimetría", "Cuánto se gira el tronco"),
        ("FM", "Frecuencia", "Levantamientos por minuto y duración de la tarea"),
        ("CM", "Agarre", "Bueno, regular o malo"),
    ],
    "nota": "El peso recomendado se obtiene multiplicando los 23 kg por seis "
            "factores que valen entre 0 y 1. Cada condición mala reduce el "
            "resultado, y por eso el mismo peso es seguro pegado al cuerpo y no "
            "lo es con los brazos estirados.",
}

# ══════════════════════════════════════════════════════════════════════
#  GASTO ENERGÉTICO · de qué se compone el día
# ══════════════════════════════════════════════════════════════════════
# Porcentajes del gasto total diario. Se dan como rangos porque la proporción
# varía muchísimo entre personas; lo que no varía es el orden de importancia.
GASTO = [
    ("Metabolismo basal", 60, 70,
     "Lo que cuesta estar vivo en reposo. La mayor parte del día y la que "
     "menos se puede cambiar a voluntad"),
    ("Actividad no deportiva", 15, 30,
     "Andar, estar de pie, gesticular, tareas. Es el componente MÁS variable "
     "entre personas y el que se hunde en silencio al comer poco"),
    ("Efecto térmico de los alimentos", 8, 12,
     "Lo que cuesta digerir y asimilar. La proteína es la que más gasta en "
     "este apartado, con diferencia"),
    ("Ejercicio estructurado", 0, 30,
     "La parte que todo el mundo cuenta y que en la mayoría de la gente es "
     "la más pequeña de las cuatro"),
]

# Tolerancias del etiquetado en Estados Unidos, que son públicas y explican
# por qué dos análisis del mismo producto no dan lo mismo.
ETIQUETA = {
    "exceso_max": 20,     # % por encima del valor declarado, nutrientes a limitar
    "defecto_min": 80,    # % del valor declarado como mínimo, nutrientes añadidos
    "nota": "Para calorías, azúcares, grasa total, grasa saturada, colesterol y "
            "sodio, el valor medido no debe superar en más de una quinta parte "
            "al declarado. Para vitaminas, minerales, proteína y fibra, el "
            "medido debe alcanzar al menos cuatro quintos del declarado. Es "
            "decir: la etiqueta es una franja, no un número.",
}

# ══════════════════════════════════════════════════════════════════════
#  INOCUIDAD ALIMENTARIA · temperaturas internas seguras
# ══════════════════════════════════════════════════════════════════════
# Cifras del servicio de inocuidad e inspección de alimentos del USDA, en
# grados Celsius con su equivalente Fahrenheit original entre paréntesis en el
# texto. Es material público que no aparece en ningún libro de fitness.
INOCUIDAD = [
    ("Aves, entera o en piezas", 74, "Sin excepción y sin reposo"),
    ("Sobras y guisos recalentados", 74, "Hasta que humee, no solo templado"),
    ("Carne picada de res, cerdo, cordero", 71,
     "Más alta que la del corte entero: al picar, la superficie se reparte "
     "por dentro"),
    ("Platos con huevo", 71, "Tortillas cuajadas, quiches, flanes"),
    ("Cortes enteros de res, cerdo, cordero", 63, "Más tres minutos de reposo"),
    ("Pescado y marisco", 63, "O hasta que la carne se separe en láminas"),
]

ZONA_PELIGRO = {
    "min": 4, "max": 60,          # °C
    "horas": 2,                   # fuera de la nevera, a temperatura ambiente
    "horas_calor": 1,             # si hace más de 32 °C
    "nevera": 4, "congelador": -18,
    "pasos": [
        ("Limpiar", "Manos veinte segundos con jabón, antes y después de tocar "
                    "crudo. Tablas y superficies entre alimento y alimento"),
        ("Separar", "Crudo lejos de listo para comer. Tabla distinta para carne "
                    "cruda, y nunca el plato que llevó el crudo a la parrilla"),
        ("Cocinar", "Con termómetro y no con el color. El color de la carne no "
                    "indica temperatura: hay carne gris a 60 °C y rosada a 75"),
        ("Enfriar", "A la nevera antes de dos horas. Las porciones grandes, "
                    "repartidas en recipientes bajos para que bajen rápido"),
    ],
}

# ══════════════════════════════════════════════════════════════════════
#  ENTRENAMIENTO · patrones, variables y la prueba pública del Ejército
# ══════════════════════════════════════════════════════════════════════
PATRONES = [
    ("Sentadilla", "Rodilla y cadera flexionan juntas",
     "Sentadilla, prensa, zancada, subir escalón"),
    ("Bisagra de cadera", "La cadera manda y la rodilla apenas se dobla",
     "Peso muerto, buenos días, empuje de cadera, balanceo"),
    ("Empuje horizontal", "Alejar peso del pecho",
     "Press de banca, flexiones, fondos"),
    ("Empuje vertical", "Llevar peso por encima de la cabeza",
     "Press militar, press con mancuernas"),
    ("Tirón horizontal", "Traer peso hacia el tronco",
     "Remo con barra, remo con mancuerna, remo invertido"),
    ("Tirón vertical", "Traer el cuerpo o el peso desde arriba",
     "Dominadas, jalón al pecho"),
    ("Transporte", "Sostener y andar con carga",
     "Paseo del granjero, transporte lateral, acarreo frontal"),
    ("Antirrotación", "Resistir un giro sin girar",
     "Plancha, press Pallof, transporte a un solo lado"),
]

VARIABLES = [
    ("Intensidad", "Cuánto pesa respecto a tu máximo, o cuántas repeticiones "
                   "te quedaban en reserva al terminar la serie"),
    ("Volumen", "Series efectivas por músculo y por semana. La cuenta que de "
                "verdad predice la ganancia de tamaño"),
    ("Frecuencia", "Cuántas veces por semana recibe estímulo cada músculo"),
    ("Densidad", "Cuánto descansas entre series. Cambia el estímulo sin "
                 "cambiar el peso"),
    ("Recorrido", "Cuánto rango articular usas. La variable más barata y la "
                  "que más se sacrifica por vanidad"),
    ("Tempo", "A qué velocidad bajas y subes. La fase de bajada es donde más "
              "adaptación se genera"),
]

# La prueba de condición física del Ejército de Estados Unidos, en su versión
# de seis pruebas. Es pública, está descrita al detalle y sirve como batería de
# referencia porque mide seis cualidades distintas y no una sola.
ACFT = [
    ("Peso muerto máximo", "Tres repeticiones con la barra hexagonal",
     "Fuerza máxima de la cadena posterior"),
    ("Lanzamiento de balón", "Balón de 4,5 kg lanzado hacia atrás por encima "
                             "de la cabeza",
     "Potencia explosiva de todo el cuerpo"),
    ("Flexión con liberación de manos", "Pecho al suelo y manos fuera en cada "
                                        "repetición",
     "Resistencia del tren superior, sin recorrido a medias"),
    ("Sprint, arrastre y acarreo", "250 m: esprintar, arrastrar trineo, "
                                   "desplazamiento lateral y acarreo de dos "
                                   "pesas",
     "Potencia anaeróbica y agarre"),
    ("Plancha", "Sostenida, con el cuerpo alineado",
     "Resistencia del tronco en isometría"),
    ("Carrera de dos millas", "3,2 km cronometrados",
     "Capacidad aeróbica"),
]
ACFT_PUNTOS = {"minimo": 60, "maximo": 100,
               "nota": "Cada prueba puntúa de 0 a 100 y hay que sacar al menos "
                       "60 en cada una: no se compensa una prueba mala con otra "
                       "excelente. Esa regla es la lección transferible."}

# ══════════════════════════════════════════════════════════════════════
#  LOS CINCO DOMINIOS DE PREPARACIÓN
# ══════════════════════════════════════════════════════════════════════
# El tercer campo NO es un índice de otros títulos: es lo que se rompe primero
# cuando ese dominio está bajo. Es el dato que convierte la rueda en una
# herramienta de diagnóstico en vez de en un catálogo.
DOMINIOS = [
    ("Físico", "Fuerza, resistencia, movilidad y potencia",
     "Se pierde autonomía y aparecen las lesiones"),
    ("Nutricional", "Lo que entra y cuándo",
     "No se recupera de lo que se entrena"),
    ("Mental", "Objetivos, atención, diálogo interno y activación",
     "Nada se sostiene más de unas semanas"),
    ("Del sueño", "Duración, horario y calidad",
     "Se hunden los otros cuatro a la vez"),
    ("Espiritual", "Sentido, valores y propósito propio",
     "Solo tú puedes juzgarlo, y por eso aquí no se juzga"),
]

# Respiración de compás cuadrado: la herramienta de bajada de activación que
# figura en la doctrina pública de preparación mental.
RESPIRACION = {"fases": ["Inspirar", "Sostener", "Espirar", "Sostener"],
               "segundos": 4, "rondas": (4, 6),
               "nota": "Cuatro tiempos iguales. Lo que hace bajar la activación "
                       "es alargar la espiración y sostener sin tensión, no "
                       "llenar mucho los pulmones."}

# ══════════════════════════════════════════════════════════════════════
#  RELOJ INTERNO Y CAFEÍNA
# ══════════════════════════════════════════════════════════════════════
# Hitos del día biológico, situados en horas relativas a la hora habitual de
# despertar (0 = despertar). Son promedios de un cronotipo intermedio.
CIRCADIANO = [
    (-2, "Mínimo de temperatura central",
     "El punto más bajo del día. Despertar aquí es lo que peor sienta"),
    (0, "Despertar", "Sube el cortisol de forma brusca: es normal y es útil"),
    (0.6, "Pico de cortisol matinal", "Treinta a cuarenta y cinco minutos "
                                      "después de abrir los ojos"),
    (7, "Bajón de alerta de la tarde", "No lo causa la comida: ocurre igual en "
                                       "ayunas. Es el hueco de la siesta corta"),
    (10, "Máximo de fuerza y temperatura", "La franja en que mejor se rinde en "
                                           "casi todas las pruebas físicas"),
    (14, "Zona de mantenimiento de la vigilia", "Las dos o tres horas antes de "
                                                "dormir en que cuesta más "
                                                "dormirse, aunque haya sueño"),
    (15, "Inicio de la melatonina", "Con luz tenue. La luz intensa a esta hora "
                                    "lo retrasa"),
    (16, "Sueño", "Si el horario es estable"),
]

CAFEINA = {
    "vida_media": 5,          # horas, adulto medio
    "rango_vida_media": (3, 7),
    "efecto_min": 20,         # minutos hasta notar el efecto
    "nota": "Cada vida media elimina la mitad de lo que quedaba. Con cinco "
            "horas, a las diez queda una cuarta parte y a las quince, una "
            "octava. La velocidad varía mucho entre personas: hay quien la "
            "elimina al doble de rápido que su vecino.",
}


# ══════════════════════════════════════════════════════════════════════
#  COMPROBACIONES
# ══════════════════════════════════════════════════════════════════════
def comprobar():
    """Si una tabla no cuadra, el generador que la use no debe escribir nada.

    Estas comprobaciones no validan las fuentes —para eso están las fuentes—
    sino la transcripción: que los rangos cierren, que ningún RDA supere su UL
    sin motivo declarado y que no falte ninguna columna.
    """
    # Los tres AMDR tienen que poder sumar 100 en algún punto de sus rangos.
    minimos = sum(a[1] for a in AMDR)
    maximos = sum(a[2] for a in AMDR)
    if not (minimos <= 100 <= maximos):
        raise SystemExit(
            f"Los AMDR no admiten el 100 %: suman entre {minimos} y {maximos}")

    # Fibra: las dos cifras tienen que ser coherentes con los 14 g/1000 kcal.
    for sexo, gramos, kcal in (("hombres", FIBRA["hombres"], 2700),
                               ("mujeres", FIBRA["mujeres"], 1800)):
        esperado = kcal * FIBRA["por_1000_kcal"] / 1000
        if abs(esperado - gramos) > 3:
            raise SystemExit(
                f"Fibra en {sexo}: {gramos} g no cuadra con 14 g/1000 kcal "
                f"sobre {kcal} kcal (saldrían {esperado:.0f} g)")

    # Micronutrientes: estructura completa y RDA por debajo del UL, salvo el
    # magnesio, cuyo UL se refiere solo a los suplementos y lo dice su nota.
    for fila in MICRO:
        if len(fila) != 6:
            raise SystemExit(f"Fila incompleta en MICRO: {fila[0]}")
        nombre, unidad, rh, rm, ul, notaest = fila
        if ul is None:
            continue
        if max(rh, rm) > ul and "SOLO" not in notaest:
            raise SystemExit(
                f"{nombre}: el RDA ({max(rh, rm)}) supera el UL ({ul}) y la "
                "nota no explica por qué")

    # Actividad: la equivalencia vigoroso/moderado tiene que cuadrar con los
    # dos pares de cifras de las guías.
    a = ACTIVIDAD
    if a["moderada_min"] != a["vigorosa_min"] * a["equivalencia"]:
        raise SystemExit("El mínimo vigoroso no equivale al mínimo moderado")
    if a["moderada_max"] != a["vigorosa_max"] * a["equivalencia"]:
        raise SystemExit("El máximo vigoroso no equivale al máximo moderado")

    # MET: cada actividad tiene que caer en la banda que declara.
    for nombre, met, banda in MET:
        if banda == "reposo" and met >= UMBRAL_MET["ligera"]:
            raise SystemExit(f"{nombre}: {met} MET no es reposo")
        if banda == "moderada" and not (UMBRAL_MET["moderada"] <= met
                                        < UMBRAL_MET["vigorosa"]):
            raise SystemExit(f"{nombre}: {met} MET no es moderada")
        if banda == "vigorosa" and met < UMBRAL_MET["vigorosa"]:
            raise SystemExit(f"{nombre}: {met} MET no es vigorosa")

    # Sueño: los ciclos tienen que cubrir la recomendación.
    minimo, maximo = SUENO["ciclos_noche"]
    horas_max = maximo * SUENO["ciclo_min"] / 60
    if horas_max < SUENO["adulto_horas"]:
        raise SystemExit(
            f"{maximo} ciclos de {SUENO['ciclo_min']} min no llegan a las "
            f"{SUENO['adulto_horas']} horas recomendadas")

    if len(NIOSH["factores"]) != 6:
        raise SystemExit("La ecuación del NIOSH tiene seis factores")

    # Gasto: los cuatro componentes tienen que poder sumar 100 en algún punto
    # de sus rangos, igual que los macronutrientes.
    gmin = sum(g[1] for g in GASTO)
    gmax = sum(g[2] for g in GASTO)
    if not (gmin <= 100 <= gmax):
        raise SystemExit(
            f"Los componentes del gasto no admiten el 100 %: {gmin} a {gmax}")
    if GASTO[0][1] < 50:
        raise SystemExit("El metabolismo basal tiene que ser el componente "
                         "mayoritario; si no, la tabla está mal transcrita")

    # Inocuidad: ninguna temperatura segura puede caer dentro de la zona de
    # peligro, que es justamente lo que la cocción tiene que superar.
    for alimento, grados, _ in INOCUIDAD:
        if grados <= ZONA_PELIGRO["max"]:
            raise SystemExit(
                f"{alimento}: {grados} °C no supera la zona de peligro "
                f"({ZONA_PELIGRO['max']} °C)")
    if ZONA_PELIGRO["nevera"] > ZONA_PELIGRO["min"]:
        raise SystemExit("La nevera tiene que estar por debajo del suelo de la "
                         "zona de peligro")
    if ZONA_PELIGRO["horas_calor"] >= ZONA_PELIGRO["horas"]:
        raise SystemExit("Con calor el margen tiene que ser MENOR, no mayor")
    if len(ZONA_PELIGRO["pasos"]) != 4:
        raise SystemExit("Los pasos de inocuidad son cuatro")

    # Etiquetado: las dos tolerancias tienen que ser simétricas respecto al
    # 100 %, que es como están redactadas en la norma.
    if ETIQUETA["exceso_max"] != 100 - ETIQUETA["defecto_min"]:
        raise SystemExit("Las dos tolerancias de etiquetado no son simétricas")

    # La prueba del Ejército: seis pruebas y un mínimo que no se compensa.
    if len(ACFT) != 6:
        raise SystemExit("La prueba de condición física tiene seis pruebas")
    if not 0 < ACFT_PUNTOS["minimo"] < ACFT_PUNTOS["maximo"]:
        raise SystemExit("El mínimo por prueba tiene que estar bajo el máximo")

    # Patrones y variables: sin nombres repetidos, que es el error típico al
    # ampliar una lista.
    for etiqueta, tabla in (("patrones", PATRONES), ("variables", VARIABLES),
                            ("dominios", DOMINIOS)):
        nombres = [t[0] for t in tabla]
        if len(set(nombres)) != len(nombres):
            raise SystemExit(f"Hay {etiqueta} repetidos")
    if len(DOMINIOS) != 5:
        raise SystemExit("Los dominios de preparación son cinco")

    # Respiración cuadrada: cuatro fases del mismo largo, o no es cuadrada.
    if len(RESPIRACION["fases"]) != 4:
        raise SystemExit("La respiración de compás cuadrado tiene cuatro fases")

    # Circadiano: los hitos tienen que ir en orden y el sueño tiene que caer
    # a una distancia del despertar coherente con la recomendación.
    horas = [h for h, _, _ in CIRCADIANO]
    if horas != sorted(horas):
        raise SystemExit("Los hitos circadianos no están en orden")
    despierto = next(h for h, n, _ in CIRCADIANO if n == "Sueño")
    if not 15 <= despierto <= 24 - SUENO["adulto_horas"] + 1:
        raise SystemExit(
            f"El sueño a las {despierto} h de vigilia no deja sitio para las "
            f"{SUENO['adulto_horas']} horas recomendadas")

    # Cafeína: la vida media declarada tiene que caer dentro de su rango.
    lo, hi = CAFEINA["rango_vida_media"]
    if not lo <= CAFEINA["vida_media"] <= hi:
        raise SystemExit("La vida media de la cafeína cae fuera de su rango")
    return True


FUENTES = [
    ("Dietary Reference Intakes",
     "National Academies · difundidas por la Oficina de Suplementos "
     "Dietéticos del NIH. RDA, AI y UL de vitaminas y minerales."),
    ("Physical Activity Guidelines for Americans, 2.ª ed.",
     "Departamento de Salud y Servicios Humanos de EE. UU., 2018. Dosis de "
     "actividad y curva de respuesta."),
    ("Dietary Guidelines for Americans",
     "USDA y HHS. Patrones alimentarios y límites de azúcares añadidos, grasa "
     "saturada y sodio."),
    ("FoodData Central",
     "Servicio de Investigación Agrícola del USDA. Composición de alimentos, "
     "consultable en línea y sin coste."),
    ("FM 7-22 Holistic Health and Fitness",
     "Ejército de EE. UU. Doctrina de entrenamiento físico, nutrición, sueño y "
     "preparación mental, publicada entera."),
    ("Ecuación de levantamiento del NIOSH",
     "Instituto Nacional de Seguridad y Salud Ocupacional, CDC. Cálculo del "
     "peso recomendado en manipulación de cargas."),
    ("Investigación en descarga y reposo en cama",
     "Programa de Investigación Humana de la NASA. Efectos de la ausencia de "
     "carga sobre músculo, hueso y sistema cardiovascular."),
    ("Registro de declaraciones de propiedades saludables",
     "Comisión Europea, con las evaluaciones científicas de EFSA. Lo que se "
     "puede afirmar de un nutriente y lo que se solicitó y fue rechazado."),
]


if __name__ == "__main__":
    comprobar()
    print(f"  datos_oficiales: {len(MICRO)} micronutrientes · "
          f"{len(MET)} actividades · {len(INOCUIDAD)} temperaturas · "
          f"{len(PATRONES)} patrones · {len(ACFT)} pruebas · "
          f"{len(CIRCADIANO)} hitos del reloj · {len(FUENTES)} fuentes · "
          "todo cuadra")
