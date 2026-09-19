# -*- coding: utf-8 -*-
"""
COMÚN A VARIOS LIBROS — inglés y francés
========================================
Los 192 segmentos que aparecen en más de un códice: la cubierta, la página de
créditos, el índice, los numerales de capítulo, el cierre y los repertorios
simbólicos compartidos (signos, planetas, elementos, letras hebreas).

Están aquí y no repetidos en cada libro porque el catálogo se indexa por el
hash del original: una misma cadena tiene una sola traducción por
construcción, y corregirla aquí la corrige en los ocho a la vez.

Los NOMBRES PROPIOS de las publicaciones oficiales no se traducen —«Dietary
Reference Intakes» se llama así también en la edición francesa, y traducirlo
haría imposible encontrar el documento—; sí se traduce su descripción.
"""

T = {

    # ── Cubierta, créditos y cierre ────────────────────────────────────────
    "Villuminations · Biblioteca": {
        "en": "Villuminations · Library", "fr": "Villuminations · Bibliothèque"},
    "Villuminations": {"en": "Villuminations", "fr": "Villuminations"},

    "<b>Edición cuidada 2026</b><br> Obra original · Primera edición, 2026<br> villuminations.com": {
        "en": "<b>Fine edition, 2026</b><br> Original work · First edition, 2026<br> villuminations.com",
        "fr": "<b>Édition soignée 2026</b><br> Œuvre originale · Première édition, 2026<br> villuminations.com"},

    "Sobre esta obra": {"en": "About this work", "fr": "À propos de cette œuvre"},

    "No se reproduce texto de ningún autor moderno. Donde una idea proviene "
    "de una fuente concreta se dice en el propio capítulo.": {
        "en": "No text by any modern author is reproduced here. Where an idea comes from "
              "a specific source, the chapter itself says so.",
        "fr": "Aucun texte d'auteur moderne n'est reproduit ici. Lorsqu'une idée provient "
              "d'une source précise, le chapitre lui-même le dit."},

    "<strong>Uso permitido.</strong> Tu compra te da una licencia personal e "
    "intransferible para leer e imprimir este archivo. No se autoriza su "
    "reventa, redistribución ni publicación total o parcial.": {
        "en": "<strong>Permitted use.</strong> Your purchase gives you a personal, "
              "non-transferable licence to read and print this file. Resale, "
              "redistribution and publication, in whole or in part, are not authorised.",
        "fr": "<strong>Usage autorisé.</strong> Votre achat vous accorde une licence "
              "personnelle et incessible pour lire et imprimer ce fichier. La revente, la "
              "redistribution et la publication, totale ou partielle, ne sont pas autorisées."},

    "Índice": {"en": "Contents", "fr": "Sommaire"},

    '<span class="v">VILLUMINATIONS</span>': {
        "en": '<span class="v">VILLUMINATIONS</span>',
        "fr": '<span class="v">VILLUMINATIONS</span>'},
    "villuminations.com": {"en": "villuminations.com", "fr": "villuminations.com"},
    "YouTube <b>@villuminations</b> &nbsp;·&nbsp; Instagram <b>@villuminations</b>": {
        "en": "YouTube <b>@villuminations</b> &nbsp;·&nbsp; Instagram <b>@villuminations</b>",
        "fr": "YouTube <b>@villuminations</b> &nbsp;·&nbsp; Instagram <b>@villuminations</b>"},

    "<strong>Sobre los derechos.</strong> Obra original. © 2026 Villuminations · "
    "villuminations.com. Todos los derechos reservados. Licencia de lectura personal: "
    "no se autoriza la reventa ni la redistribución del archivo. Si este libro te ha "
    "servido, la mejor forma de apoyarlo es recomendarlo por la vía legítima.": {
        "en": "<strong>On rights.</strong> Original work. © 2026 Villuminations · "
              "villuminations.com. All rights reserved. Personal reading licence: resale "
              "and redistribution of the file are not authorised. If this book has been "
              "useful to you, the best way to support it is to recommend it through "
              "legitimate channels.",
        "fr": "<strong>À propos des droits.</strong> Œuvre originale. © 2026 "
              "Villuminations · villuminations.com. Tous droits réservés. Licence de "
              "lecture personnelle : la revente et la redistribution du fichier ne sont pas "
              "autorisées. Si ce livre vous a servi, la meilleure façon de le soutenir est "
              "de le recommander par la voie légitime."},

    # ── Numerales de capítulo ──────────────────────────────────────────────
    # Se escriben uno a uno y no con un bucle porque el catálogo es de datos:
    # una tabla generada aquí no se podría revisar leyéndola.
    "Capítulo 1": {"en": "Chapter 1", "fr": "Chapitre 1"},
    "Capítulo 2": {"en": "Chapter 2", "fr": "Chapitre 2"},
    "Capítulo 3": {"en": "Chapter 3", "fr": "Chapitre 3"},
    "Capítulo 4": {"en": "Chapter 4", "fr": "Chapitre 4"},
    "Capítulo 5": {"en": "Chapter 5", "fr": "Chapitre 5"},
    "Capítulo 6": {"en": "Chapter 6", "fr": "Chapitre 6"},
    "Capítulo 7": {"en": "Chapter 7", "fr": "Chapitre 7"},
    "Capítulo 8": {"en": "Chapter 8", "fr": "Chapitre 8"},
    "Capítulo 9": {"en": "Chapter 9", "fr": "Chapitre 9"},
    "Capítulo 10": {"en": "Chapter 10", "fr": "Chapitre 10"},
    "Capítulo 11": {"en": "Chapter 11", "fr": "Chapitre 11"},
    "Capítulo 12": {"en": "Chapter 12", "fr": "Chapitre 12"},
    "Capítulo 13": {"en": "Chapter 13", "fr": "Chapitre 13"},
    "Capítulo 14": {"en": "Chapter 14", "fr": "Chapitre 14"},
    "Capítulo 15": {"en": "Chapter 15", "fr": "Chapitre 15"},
    "Capítulo 16": {"en": "Chapter 16", "fr": "Chapitre 16"},
    "Capítulo 17": {"en": "Chapter 17", "fr": "Chapitre 17"},
    "Capítulo 18": {"en": "Chapter 18", "fr": "Chapitre 18"},
    "Capítulo 19": {"en": "Chapter 19", "fr": "Chapitre 19"},
    "Capítulo 20": {"en": "Chapter 20", "fr": "Chapitre 20"},
    "Capítulo 21": {"en": "Chapter 21", "fr": "Chapitre 21"},
    "Capítulo 22": {"en": "Chapter 22", "fr": "Chapitre 22"},
    "Capítulo 23": {"en": "Chapter 23", "fr": "Chapitre 23"},
    "Capítulo 24": {"en": "Chapter 24", "fr": "Chapitre 24"},
    "Capítulo 25": {"en": "Chapter 25", "fr": "Chapitre 25"},

    # ── Encabezados recurrentes ────────────────────────────────────────────
    "Lo que este libro no afirma": {
        "en": "What this book does not claim", "fr": "Ce que ce livre n'affirme pas"},
    "La afirmación de este libro": {
        "en": "What this book claims", "fr": "Ce que ce livre affirme"},
    "Cómo comprobarlo tú mismo": {
        "en": "How to check it yourself", "fr": "Comment le vérifier vous-même"},
    "Las fuentes de este libro": {
        "en": "The sources of this book", "fr": "Les sources de ce livre"},
    "Glosario": {"en": "Glossary", "fr": "Glossaire"},
    "La prueba de realidad": {"en": "The reality check", "fr": "L'épreuve du réel"},
    "Y cómo se comprueba este libro a sí mismo": {
        "en": "And how this book checks itself",
        "fr": "Et comment ce livre se vérifie lui-même"},
    "Y la honestidad de siempre": {
        "en": "And the usual honesty", "fr": "Et l'honnêteté habituelle"},
    "Y la prueba inversa": {"en": "And the reverse test", "fr": "Et la preuve inverse"},
    "Qué esperar del cuaderno": {
        "en": "What to expect from the notebook",
        "fr": "Ce qu'il faut attendre du carnet"},
    "Qué esperar": {"en": "What to expect", "fr": "À quoi s'attendre"},
    "Cómo leerlo": {"en": "How to read it", "fr": "Comment le lire"},
    "Por qué funciona": {"en": "Why it works", "fr": "Pourquoi cela fonctionne"},
    "Rutas concretas": {"en": "Concrete routes", "fr": "Itinéraires concrets"},
    "Antes de empezar": {"en": "Before you start", "fr": "Avant de commencer"},
    "Lo que espero de esto": {
        "en": "What I expect from this", "fr": "Ce que j'en attends"},
    "Sobre la última línea": {
        "en": "About the last line", "fr": "À propos de la dernière ligne"},
    "El encuadre de este capítulo": {
        "en": "How this chapter is framed", "fr": "Le cadrage de ce chapitre"},
    "Los errores del principiante": {
        "en": "The beginner's mistakes", "fr": "Les erreurs du débutant"},
    "Contra el diario literario": {
        "en": "Against the literary diary", "fr": "Contre le journal littéraire"},
    "Qué se anota": {"en": "What gets written down", "fr": "Ce que l'on note"},
    "Los cuatro pasos": {"en": "The four steps", "fr": "Les quatre étapes"},
    "El hecho": {"en": "The fact", "fr": "Le fait"},
    "El cuerpo": {"en": "The body", "fr": "Le corps"},
    "El movimiento": {"en": "Movement", "fr": "Le mouvement"},
    "La hora": {"en": "The hour", "fr": "L'heure"},

    # ── Cuaderno de un año ─────────────────────────────────────────────────
    "Los cuatro trimestres": {"en": "The four quarters", "fr": "Les quatre trimestres"},
    "Meses 1–3": {"en": "Months 1–3", "fr": "Mois 1–3"},
    "Meses 4–6": {"en": "Months 4–6", "fr": "Mois 4–6"},
    "Meses 7–9": {"en": "Months 7–9", "fr": "Mois 7–9"},
    "Meses 10–12": {"en": "Months 10–12", "fr": "Mois 10–12"},
    "Los tres indicadores": {"en": "The three indicators", "fr": "Les trois indicateurs"},
    "Ficha de partida": {"en": "Starting record", "fr": "Fiche de départ"},
    "Fecha de inicio": {"en": "Start date", "fr": "Date de début"},
    "Fecha y hora": {"en": "Date and time", "fr": "Date et heure"},
    "Cierre del año": {"en": "Closing the year", "fr": "Clôture de l'année"},
    "El año de práctica": {"en": "The year of practice", "fr": "L'année de pratique"},
    "Se copia una por día": {"en": "Copy one a day", "fr": "On en copie une par jour"},
    "Revisión trimestral": {"en": "Quarterly review", "fr": "Bilan trimestriel"},
    "Cada tres meses": {"en": "Every three months", "fr": "Tous les trois mois"},
    "A los doce meses": {"en": "At twelve months", "fr": "Au bout de douze mois"},
    "Porcentaje de cumplimiento": {
        "en": "Adherence percentage", "fr": "Pourcentage d'observance"},
    "Tiempo de recuperación tras una interrupción": {
        "en": "Time to recover after an interruption",
        "fr": "Temps de reprise après une interruption"},
    "Lo que ha dicho quien convive conmigo": {
        "en": "What the person I live with has said",
        "fr": "Ce qu'a dit la personne qui vit avec moi"},
    "Lo que sigo haciendo un año después": {
        "en": "What I am still doing a year later",
        "fr": "Ce que je fais encore un an après"},

    # ── Fuentes oficiales · el nombre no se traduce, la glosa sí ───────────
    "Dietary Reference Intakes": {
        "en": "Dietary Reference Intakes", "fr": "Dietary Reference Intakes"},
    "National Academies · difundidas por la Oficina de Suplementos Dietéticos del NIH. "
    "RDA, AI y UL de vitaminas y minerales.": {
        "en": "National Academies · distributed by the NIH Office of Dietary Supplements. "
              "RDA, AI and UL for vitamins and minerals.",
        "fr": "National Academies · diffusées par l'Office of Dietary Supplements du NIH. "
              "AJR, AS et LS des vitamines et minéraux."},
    "Physical Activity Guidelines for Americans, 2.ª ed.": {
        "en": "Physical Activity Guidelines for Americans, 2nd ed.",
        "fr": "Physical Activity Guidelines for Americans, 2ᵉ éd."},
    "Departamento de Salud y Servicios Humanos de EE. UU., 2018. Dosis de actividad y "
    "curva de respuesta.": {
        "en": "U.S. Department of Health and Human Services, 2018. Activity dose and the "
              "response curve.",
        "fr": "Département de la Santé et des Services sociaux des États-Unis, 2018. Dose "
              "d'activité et courbe de réponse."},
    "Dietary Guidelines for Americans": {
        "en": "Dietary Guidelines for Americans", "fr": "Dietary Guidelines for Americans"},
    "USDA y HHS. Patrones alimentarios y límites de azúcares añadidos, grasa saturada y sodio.": {
        "en": "USDA and HHS. Dietary patterns and limits for added sugars, saturated fat "
              "and sodium.",
        "fr": "USDA et HHS. Modèles alimentaires et limites de sucres ajoutés, de graisses "
              "saturées et de sodium."},
    "FoodData Central": {"en": "FoodData Central", "fr": "FoodData Central"},
    "Servicio de Investigación Agrícola del USDA. Composición de alimentos, consultable "
    "en línea y sin coste.": {
        "en": "USDA Agricultural Research Service. Food composition, searchable online at "
              "no cost.",
        "fr": "Agricultural Research Service de l'USDA. Composition des aliments, "
              "consultable en ligne et gratuitement."},
    "FM 7-22 Holistic Health and Fitness": {
        "en": "FM 7-22 Holistic Health and Fitness",
        "fr": "FM 7-22 Holistic Health and Fitness"},
    "Ejército de EE. UU. Doctrina de entrenamiento físico, nutrición, sueño y preparación "
    "mental, publicada entera.": {
        "en": "U.S. Army. Doctrine on physical training, nutrition, sleep and mental "
              "readiness, published in full.",
        "fr": "Armée des États-Unis. Doctrine d'entraînement physique, de nutrition, de "
              "sommeil et de préparation mentale, publiée intégralement."},
    "Ecuación de levantamiento del NIOSH": {
        "en": "The NIOSH lifting equation", "fr": "Équation de levage du NIOSH"},
    "Instituto Nacional de Seguridad y Salud Ocupacional, CDC. Cálculo del peso "
    "recomendado en manipulación de cargas.": {
        "en": "National Institute for Occupational Safety and Health, CDC. Calculation of "
              "the recommended weight limit in manual handling.",
        "fr": "National Institute for Occupational Safety and Health, CDC. Calcul du poids "
              "recommandé en manutention de charges."},
    "Investigación en descarga y reposo en cama": {
        "en": "Research on unloading and bed rest",
        "fr": "Recherche sur la décharge et l'alitement"},
    "Programa de Investigación Humana de la NASA. Efectos de la ausencia de carga sobre "
    "músculo, hueso y sistema cardiovascular.": {
        "en": "NASA Human Research Program. Effects of unloading on muscle, bone and the "
              "cardiovascular system.",
        "fr": "Programme de recherche humaine de la NASA. Effets de l'absence de charge sur "
              "le muscle, l'os et le système cardiovasculaire."},
    "Registro de declaraciones de propiedades saludables": {
        "en": "Register of health claims",
        "fr": "Registre des allégations de santé"},
    "Comisión Europea, con las evaluaciones científicas de EFSA. Lo que se puede afirmar "
    "de un nutriente y lo que se solicitó y fue rechazado.": {
        "en": "European Commission, with the scientific assessments of EFSA. What may be "
              "claimed about a nutrient, and what was applied for and refused.",
        "fr": "Commission européenne, avec les évaluations scientifiques de l'EFSA. Ce que "
              "l'on peut affirmer d'un nutriment, et ce qui a été demandé puis refusé."},

    # ── Elementos ──────────────────────────────────────────────────────────
    "Fuego": {"en": "Fire", "fr": "Feu"},
    "Tierra": {"en": "Earth", "fr": "Terre"},
    "Aire": {"en": "Air", "fr": "Air"},
    "Agua": {"en": "Water", "fr": "Eau"},
    "FUEGO": {"en": "FIRE", "fr": "FEU"},
    "TIERRA": {"en": "EARTH", "fr": "TERRE"},
    "AIRE": {"en": "AIR", "fr": "AIR"},
    "AGUA": {"en": "WATER", "fr": "EAU"},

    # ── Signos y planetas ──────────────────────────────────────────────────
    "Aries": {"en": "Aries", "fr": "Bélier"},
    "Tauro": {"en": "Taurus", "fr": "Taureau"},
    "Géminis": {"en": "Gemini", "fr": "Gémeaux"},
    "Cáncer": {"en": "Cancer", "fr": "Cancer"},
    "Leo": {"en": "Leo", "fr": "Lion"},
    "Virgo": {"en": "Virgo", "fr": "Vierge"},
    "Libra": {"en": "Libra", "fr": "Balance"},
    "Escorpio": {"en": "Scorpio", "fr": "Scorpion"},
    "Sagitario": {"en": "Sagittarius", "fr": "Sagittaire"},
    "Capricornio": {"en": "Capricorn", "fr": "Capricorne"},
    "Acuario": {"en": "Aquarius", "fr": "Verseau"},
    "Piscis": {"en": "Pisces", "fr": "Poissons"},
    "Sol": {"en": "Sun", "fr": "Soleil"},
    "Luna": {"en": "Moon", "fr": "Lune"},
    "Mercurio": {"en": "Mercury", "fr": "Mercure"},
    "Venus": {"en": "Venus", "fr": "Vénus"},
    "Marte": {"en": "Mars", "fr": "Mars"},
    "Júpiter": {"en": "Jupiter", "fr": "Jupiter"},
    "Saturno": {"en": "Saturn", "fr": "Saturne"},
    "Decanato": {"en": "Decan", "fr": "Décan"},
    "La Luna": {"en": "The Moon", "fr": "La Lune"},
    "El Sol": {"en": "The Sun", "fr": "Le Soleil"},

    # ── Días, solos y con su planeta ───────────────────────────────────────
    "Lunes": {"en": "Monday", "fr": "Lundi"},
    "Martes": {"en": "Tuesday", "fr": "Mardi"},
    "Miércoles": {"en": "Wednesday", "fr": "Mercredi"},
    "Jueves": {"en": "Thursday", "fr": "Jeudi"},
    "Viernes": {"en": "Friday", "fr": "Vendredi"},
    "Sábado": {"en": "Saturday", "fr": "Samedi"},
    "Domingo": {"en": "Sunday", "fr": "Dimanche"},
    "Lunes · Luna": {"en": "Monday · Moon", "fr": "Lundi · Lune"},
    "Martes · Marte": {"en": "Tuesday · Mars", "fr": "Mardi · Mars"},
    "Miércoles · Mercurio": {"en": "Wednesday · Mercury", "fr": "Mercredi · Mercure"},
    "Jueves · Júpiter": {"en": "Thursday · Jupiter", "fr": "Jeudi · Jupiter"},
    "Viernes · Venus": {"en": "Friday · Venus", "fr": "Vendredi · Vénus"},
    "Sábado · Saturno": {"en": "Saturday · Saturn", "fr": "Samedi · Saturne"},
    "Domingo · Sol": {"en": "Sunday · Sun", "fr": "Dimanche · Soleil"},

    # ── Letras hebreas · se translitera, no se traduce ─────────────────────
    "LETRA": {"en": "LETTER", "fr": "LETTRE"},
    "Álef": {"en": "Aleph", "fr": "Aleph"},
    "Bet": {"en": "Beth", "fr": "Beth"},
    "Guímel": {"en": "Gimel", "fr": "Guimel"},
    "Dálet": {"en": "Daleth", "fr": "Daleth"},
    "He": {"en": "He", "fr": "Hé"},
    "Vav": {"en": "Vav", "fr": "Vav"},
    "Zayin": {"en": "Zayin", "fr": "Zayin"},
    "Jet": {"en": "Cheth", "fr": "Heth"},
    "Tet": {"en": "Teth", "fr": "Teth"},
    "Yod": {"en": "Yod", "fr": "Yod"},
    "Kaf": {"en": "Kaph", "fr": "Kaph"},
    "Lámed": {"en": "Lamed", "fr": "Lamed"},
    "Mem": {"en": "Mem", "fr": "Mem"},
    "Nun": {"en": "Nun", "fr": "Noun"},
    "Sámej": {"en": "Samekh", "fr": "Samekh"},
    "Ayin": {"en": "Ayin", "fr": "Ayin"},
    "Pe": {"en": "Pe", "fr": "Pé"},
    "Tsade": {"en": "Tzaddi", "fr": "Tsadé"},
    "Qof": {"en": "Qoph", "fr": "Qoph"},
    "Resh": {"en": "Resh", "fr": "Resh"},
    "Shin": {"en": "Shin", "fr": "Shin"},
    "Tav": {"en": "Tav", "fr": "Tav"},
    "II": {"en": "II", "fr": "II"},
    "III": {"en": "III", "fr": "III"},

    # ── Numerales en palabras ──────────────────────────────────────────────
    "Dos": {"en": "Two", "fr": "Deux"},
    "Tres": {"en": "Three", "fr": "Trois"},
    "Cuatro": {"en": "Four", "fr": "Quatre"},
    "Cinco": {"en": "Five", "fr": "Cinq"},
    "Seis": {"en": "Six", "fr": "Six"},
    "Siete": {"en": "Seven", "fr": "Sept"},
    "Ocho": {"en": "Eight", "fr": "Huit"},
    "Nueve": {"en": "Nine", "fr": "Neuf"},
    "Diez": {"en": "Ten", "fr": "Dix"},

    # ── Fisiología compartida ──────────────────────────────────────────────
    "Fuerza": {"en": "Strength", "fr": "Force"},
    "Masa muscular": {"en": "Muscle mass", "fr": "Masse musculaire"},
    "Capacidad aeróbica": {"en": "Aerobic capacity", "fr": "Capacité aérobie"},
    "Densidad mineral ósea": {"en": "Bone mineral density", "fr": "Densité minérale osseuse"},
    "Volumen plasmático": {"en": "Plasma volume", "fr": "Volume plasmatique"},
    "Rendimiento": {"en": "Performance", "fr": "Performance"},
    "Sueño": {"en": "Sleep", "fr": "Sommeil"},
    "Hierro": {"en": "Iron", "fr": "Fer"},
    "MET": {"en": "MET", "fr": "MET"},
    "Meses": {"en": "Months", "fr": "Mois"},
    "Enfriar": {"en": "Cool down", "fr": "Refroidir"},
    "AQUÍ": {"en": "HERE", "fr": "ICI"},
    "1 a 2 % por semana": {"en": "1 to 2 % per week", "fr": "1 à 2 % par semaine"},
    "Cae más rápido que la masa": {
        "en": "Falls faster than mass does", "fr": "Baisse plus vite que la masse"},
    "En torno a 1 a 1,5 % al mes": {
        "en": "Around 1 to 1.5 % a month", "fr": "Environ 1 à 1,5 % par mois"},
    "Baja en los primeros días": {
        "en": "Drops in the first few days", "fr": "Baisse dès les premiers jours"},
    "Medible en una o dos semanas": {
        "en": "Measurable within one or two weeks",
        "fr": "Mesurable en une ou deux semaines"},
}
