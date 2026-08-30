# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · aspectos, dignidades, precesión y portada
===========================================================
Los aspectos llevan su nombre de oficio en cada lengua: Trígono es Trine y
Trigone, Cuadratura es Square y Carré. Los grados no se tocan.

Las dignidades esenciales también son términos técnicos con equivalente fijo:
domicilio, exaltación, exilio y caída son domicile, exaltation, detriment y
fall en inglés, y domicile, exaltation, exil y chute en francés. Los rótulos
de la lámina van abreviados como en el original.

La lámina de la precesión da dos cifras que son datos y no adornos: 50,3
segundos de arco al año y una vuelta en 25 800. Se conservan, con el punto
decimal y la coma de millar que le tocan al inglés y el espacio que le toca al
francés.

Los créditos se apoyan en la <strong>tradición común</strong> —las
correspondencias, los regentes y los decanatos llevan dos milenios
imprimiéndose—, no en ninguna norma federal estadounidense. La distinción es
deliberada y se traduce como lo que es.
"""

T = {
    # ── Lámina 7 · la geometría de la rueda ────────────────────────────────
    "Signos enfrentados: tensión": {
        "en": "Signs facing each other: tension",
        "fr": "Signes face à face : tension"},

    "TRÍGONO · 120°": {"en": "TRINE · 120°", "fr": "TRIGONE · 120°"},
    "Mismo elemento: fluidez": {
        "en": "Same element: fluency", "fr": "Même élément : fluidité"},

    "CUADRATURA · 90°": {"en": "SQUARE · 90°", "fr": "CARRÉ · 90°"},
    "Misma modalidad: roce": {
        "en": "Same modality: friction", "fr": "Même modalité : friction"},

    "SEXTIL · 60°": {"en": "SEXTILE · 60°", "fr": "SEXTILE · 60°"},
    "Afinidad: oportunidad": {
        "en": "Affinity: opportunity", "fr": "Affinité : occasion"},

    # ── Lámina · las dignidades esenciales ─────────────────────────────────
    "DOMICILIO": {"en": "DOMICILE", "fr": "DOMICILE"},
    "EXALTA": {"en": "EXALTS", "fr": "EXALT."},
    "EXILIO": {"en": "DETRIMENT", "fr": "EXIL"},
    "CAÍDA": {"en": "FALL", "fr": "CHUTE"},

    # ── Lámina · la precesión ──────────────────────────────────────────────
    "CINCO TRAMOS DESIGUALES · TREINTA GRADOS JUSTOS": {
        "en": "FIVE UNEQUAL STRETCHES · THIRTY EXACT DEGREES",
        "fr": "CINQ TRONÇONS INÉGAUX · TRENTE DEGRÉS JUSTES"},

    "24° DE DESFASE ACUMULADO": {
        "en": "24° OF ACCUMULATED DRIFT", "fr": "24° DE DÉCALAGE ACCUMULÉ"},

    "SIGNOS": {"en": "SIGNS", "fr": "SIGNES"},
    "fuera": {"en": "outside", "fr": "dehors"},
    "CONSTELACIONES": {"en": "CONSTELLATIONS", "fr": "CONSTELLATIONS"},
    "dentro": {"en": "inside", "fr": "dedans"},

    "50,3 SEGUNDOS DE ARCO AL AÑO · UNA VUELTA EN 25 800": {
        "en": "50.3 ARCSECONDS A YEAR · ONE TURN IN 25,800",
        "fr": "50,3 SECONDES D'ARC PAR AN · UN TOUR EN 25 800"},

    # ── Portada y créditos ─────────────────────────────────────────────────
    "Códice Zodiacal": {"en": "Zodiacal Codex", "fr": "Codex Zodiacal"},

    "Los doce signos como mapa del carácter, del cuerpo y del trabajo interior": {
        "en": "The twelve signs as a map of character, of the body and of inner work",
        "fr": "Les douze signes comme carte du caractère, du corps et du travail intérieur"},

    "<strong>Códice Zodiacal</strong> es una obra original de Villuminations,\n"
    "     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.\n"
    "     Obra original · Primera edición, 2026.": {
        "en": "<strong>Zodiacal Codex</strong> is an original work by Villuminations, written "
              "and typeset entirely for <strong>villuminations.com</strong>. Original work · "
              "First edition, 2026.",
        "fr": "<strong>Codex Zodiacal</strong> est une œuvre originale de Villuminations, "
              "écrite et composée intégralement pour <strong>villuminations.com</strong>. "
              "Œuvre originale · Première édition, 2026."},

    "El material del que parte pertenece a la <strong>tradición común</strong>:\n"
    "     las correspondencias astrológicas clásicas, los regentes planetarios, la\n"
    "     división en elementos y modalidades y las tablas de decanatos se\n"
    "     transmiten por escrito desde hace más de dos milenios y no son propiedad\n"
    "     de nadie. Lo que aquí se ofrece —la redacción, la estructura de nueve\n"
    "     claves, las prácticas de cuatro semanas, la lectura corporal y de hábito\n"
    "     de cada signo, las fichas, los ejercicios de registro y las\n"
    "     ilustraciones— es trabajo propio y está protegido como tal.": {
        "en": "The material it starts from belongs to the <strong>common tradition</strong>: "
              "the classical astrological correspondences, the planetary rulers, the division "
              "into elements and modalities and the tables of decans have been transmitted in "
              "writing for more than two millennia and are nobody's property. What is offered "
              "here —the writing, the structure of nine keys, the four-week practices, the "
              "reading of body and habit for each sign, the sign entries, the record-keeping "
              "exercises and the illustrations— is original work and is protected as such.",
        "fr": "Le matériau dont il part appartient à la <strong>tradition commune</strong> : "
              "les correspondances astrologiques classiques, les régents planétaires, la "
              "division en éléments et modalités et les tables de décans se transmettent par "
              "écrit depuis plus de deux millénaires et n'appartiennent à personne. Ce qui est "
              "proposé ici —la rédaction, la structure en neuf clés, les pratiques de quatre "
              "semaines, la lecture du corps et des habitudes de chaque signe, les fiches, les "
              "exercices de registre et les illustrations— est un travail propre et protégé "
              "comme tel."},

    "<strong>Cómo leer este libro.</strong> La astrología que aquí se practica\n"
    "     es un <em>lenguaje simbólico</em>: una manera antigua y muy afinada de\n"
    "     nombrar temperamentos, tensiones y ciclos. No es una ciencia predictiva.\n"
    "     Nada de lo que sigue anuncia hechos futuros, diagnostica enfermedades ni\n"
    "     sustituye la atención de un médico, un psicólogo o un dietista-nutricionista\n"
    "     colegiado. Las pautas de alimentación, sueño y movimiento son de sentido\n"
    "     común y deben adaptarse a tu caso; si tienes una patología, embarazo o\n"
    "     tratamiento en curso, consúltalas antes con tu profesional sanitario.": {
        "en": "<strong>How to read this book.</strong> The astrology practised here is a "
              "<em>symbolic language</em>: an old and very finely tuned way of naming "
              "temperaments, tensions and cycles. It is not a predictive science. Nothing that "
              "follows announces future events, diagnoses illnesses or replaces the care of a "
              "registered doctor, psychologist or dietitian. The guidance on food, sleep and "
              "movement is common sense and has to be adapted to your case; if you have a "
              "medical condition, a pregnancy or an ongoing treatment, check it first with "
              "your health professional.",
        "fr": "<strong>Comment lire ce livre.</strong> L'astrologie que l'on pratique ici est "
              "un <em>langage symbolique</em> : une manière ancienne et très affinée de nommer "
              "des tempéraments, des tensions et des cycles. Ce n'est pas une science "
              "prédictive. Rien de ce qui suit n'annonce des faits à venir, ne diagnostique de "
              "maladies ni ne remplace le suivi d'un médecin, d'un psychologue ou d'un "
              "diététicien-nutritionniste. Les conseils d'alimentation, de sommeil et de "
              "mouvement relèvent du bon sens et doivent être adaptés à votre cas ; si vous "
              "avez une pathologie, une grossesse ou un traitement en cours, consultez-les "
              "d'abord avec votre professionnel de santé."},

    # ── Índice ─────────────────────────────────────────────────────────────
    "Antes de abrir la rueda": {
        "en": "Before opening the wheel", "fr": "Avant d'ouvrir la roue"},
    "La rueda y sus cuatro elementos": {
        "en": "The wheel and its four elements",
        "fr": "La roue et ses quatre éléments"},
    "Los siete regentes tradicionales": {
        "en": "The seven traditional rulers", "fr": "Les sept régents traditionnels"},
    "Los treinta y seis decanatos": {
        "en": "The thirty-six decans", "fr": "Les trente-six décans"},
    "La geometría de la rueda": {
        "en": "The geometry of the wheel", "fr": "La géométrie de la roue"},
    "El zodiaco del cuerpo": {
        "en": "The zodiac of the body", "fr": "Le zodiaque du corps"},
    "Por qué no te reconoces en tu signo": {
        "en": "Why you do not recognise yourself in your sign",
        "fr": "Pourquoi vous ne vous reconnaissez pas dans votre signe"},
}
