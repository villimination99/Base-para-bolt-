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
          f"{len(MET)} actividades · {len(FUENTES)} fuentes · todo cuadra")
