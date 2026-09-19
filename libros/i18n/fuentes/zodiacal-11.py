# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · el cierre de la secta y la ficha de Aries
===========================================================
Aquí empiezan los doce capítulos de signo y con ellos las etiquetas de la
ficha, que se repiten doce veces cada una: elemento, modalidad, polaridad,
regente, metal, piedra, color, zona corporal y palabra clave. El catálogo las
comparte por construcción, así que basta con acertarlas una vez.

Las fechas van en el orden de cada lengua: «21 March to 20 April» y «Du 21
mars au 20 avril». La forma se mantendrá idéntica en los doce signos.

La palabra clave de cada signo es una frase de dos palabras en primera persona
—«Yo empiezo»— y se traduce igual de escueta: I begin, Je commence. Es lo que
va impreso bajo el sello, y crecerlas rompería la ficha.

El argumento de por qué Saturno es diurno y Marte nocturno se traduce entero
porque cierra con la regla que gobierna las doce secciones de «La mesa»: lo
que sobra se equilibra con lo que falta, no lo semejante atrae a lo semejante.
"""

T = {
    "Sol · Júpiter · Saturno": {
        "en": "Sun · Jupiter · Saturn", "fr": "Soleil · Jupiter · Saturne"},
    "Secta nocturna": {"en": "Nocturnal sect", "fr": "Secte nocturne"},
    "Luna · Venus · Marte": {"en": "Moon · Venus · Mars", "fr": "Lune · Vénus · Mars"},

    "Sin secta propia: toma la del momento. Diurno si sale antes del Sol, nocturno si sale "
    "después.": {
        "en": "With no sect of its own: it takes that of the moment. Diurnal if it rises before "
              "the Sun, nocturnal if it rises after.",
        "fr": "Sans secte propre : il prend celle du moment. Diurne s'il se lève avant le "
              "Soleil, nocturne s'il se lève après."},

    "La regla": {"en": "The rule", "fr": "La règle"},
    "Carta de día si el Sol está sobre el horizonte al nacer; de noche si está debajo.": {
        "en": "A day chart if the Sun is above the horizon at birth; a night chart if it is "
              "below.",
        "fr": "Thème de jour si le Soleil est au-dessus de l'horizon à la naissance ; de nuit "
              "s'il est au-dessous."},

    "La parte que más rinde": {
        "en": "The part that yields most", "fr": "La partie qui rapporte le plus"},

    "Que Saturno sea diurno y Marte nocturno es, a primera vista, contraintuitivo: se esperaría "
    "lo contrario del planeta del frío y del planeta del calor. La tradición lo explica por "
    "compensación, y el argumento es bueno: Saturno, que es seco y frío en exceso, se templa "
    "con el calor del día; Marte, que es caliente y seco en exceso, se templa con la humedad "
    "de la noche. Cada uno se coloca donde su exceso se corrige.": {
        "en": "That Saturn should be diurnal and Mars nocturnal is, at first sight, "
              "counter-intuitive: you would expect the opposite of the planet of cold and the "
              "planet of heat. The tradition explains it by compensation, and the argument is a "
              "good one: Saturn, which is dry and cold to excess, is tempered by the heat of "
              "the day; Mars, which is hot and dry to excess, is tempered by the moisture of "
              "the night. Each is placed where its excess is corrected.",
        "fr": "Que Saturne soit diurne et Mars nocturne est, à première vue, contre-intuitif : "
              "on attendrait le contraire de la planète du froid et de la planète de la chaleur. "
              "La tradition l'explique par compensation, et l'argument est bon : Saturne, sec et "
              "froid à l'excès, se tempère par la chaleur du jour ; Mars, chaud et sec à "
              "l'excès, se tempère par l'humidité de la nuit. Chacun se place là où son excès se "
              "corrige."},

    "Esa lógica de compensación es la misma que gobierna la sección «La mesa» de los doce "
    "capítulos de signo, y no es casualidad: viene del mismo sitio. Todo el sistema clásico "
    "está construido sobre la idea de que lo que sobra se equilibra con lo que falta, y no "
    "sobre la de que lo semejante se atrae.": {
        "en": "That logic of compensation is the same one that governs the section «The table» "
              "in the twelve sign chapters, and it is no coincidence: it comes from the same "
              "place. The whole classical system is built on the idea that what is in excess is "
              "balanced by what is lacking, and not on the idea that like attracts like.",
        "fr": "Cette logique de compensation est celle-là même qui gouverne la section « La "
              "table » des douze chapitres de signe, et ce n'est pas un hasard : elle vient du "
              "même endroit. Tout le système classique est bâti sur l'idée que ce qui est en "
              "trop s'équilibre par ce qui manque, et non sur celle que le semblable attire le "
              "semblable."},

    "Cómo usarla sin calcular nada": {
        "en": "How to use it without calculating anything",
        "fr": "Comment s'en servir sans rien calculer"},

    "Si sabes si naciste de día o de noche —y casi todo el mundo lo sabe—, ya tienes tu secta. "
    "Los tres planetas de tu bando son las funciones que te salen con menos esfuerzo; los del "
    "bando contrario, las que exigen trabajo consciente. Cruza eso con los siete regentes del "
    "capítulo 3 y tienes una lectura de tus facilidades y tus fricciones que no necesita "
    "ninguna carta y que suele resultar incómodamente reconocible.": {
        "en": "If you know whether you were born by day or by night —and almost everybody "
              "does— you already have your sect. The three planets of your camp are the "
              "functions that come to you with least effort; those of the opposite camp, the "
              "ones that demand conscious work. Cross that with the seven rulers of chapter 3 "
              "and you have a reading of your facilities and your frictions that needs no chart "
              "and that tends to be uncomfortably recognisable.",
        "fr": "Si vous savez si vous êtes né de jour ou de nuit —et presque tout le monde le "
              "sait—, vous avez déjà votre secte. Les trois planètes de votre camp sont les "
              "fonctions qui vous viennent avec le moins d'effort ; celles du camp opposé, "
              "celles qui exigent un travail conscient. Croisez cela avec les sept régents du "
              "chapitre 3 et vous avez une lecture de vos facilités et de vos frictions qui n'a "
              "besoin d'aucun thème et qui se révèle d'ordinaire inconfortablement "
              "reconnaissable."},

    # ── Aries ──────────────────────────────────────────────────────────────
    "21 de marzo a 20 de abril": {
        "en": "21 March to 20 April", "fr": "Du 21 mars au 20 avril"},

    "Correspondencias": {"en": "Correspondences", "fr": "Correspondances"},
    "Elemento": {"en": "Element", "fr": "Élément"},
    "Modalidad": {"en": "Modality", "fr": "Modalité"},
    "Polaridad": {"en": "Polarity", "fr": "Polarité"},
    "Activa": {"en": "Active", "fr": "Active"},
    "Regente": {"en": "Ruler", "fr": "Régent"},
    "Metal": {"en": "Metal", "fr": "Métal"},
    "Piedra": {"en": "Stone", "fr": "Pierre"},
    "Rubí y diamante": {"en": "Ruby and diamond", "fr": "Rubis et diamant"},
    "Color": {"en": "Colour", "fr": "Couleur"},
    "Rojo": {"en": "Red", "fr": "Rouge"},
    "Zona corporal": {"en": "Bodily zone", "fr": "Zone corporelle"},
    "Cabeza y cara": {"en": "Head and face", "fr": "Tête et visage"},
    "Palabra clave": {"en": "Key word", "fr": "Mot-clé"},
    "Yo empiezo": {"en": "I begin", "fr": "Je commence"},

    "El símbolo": {"en": "The symbol", "fr": "Le symbole"},

    "El carnero embiste. No rodea, no calcula el ángulo, no espera a que se abra la puerta: "
    "baja la cabeza y va. Ahí está todo Aries, y también el motivo de que sea el primer signo "
    "de la rueda — porque antes de cualquier construcción hace falta alguien dispuesto a dar "
    "el primer golpe.": {
        "en": "The ram charges. It does not go round, it does not work out the angle, it does "
              "not wait for the door to open: it lowers its head and goes. There is all of "
              "Aries, and also the reason it is the first sign of the wheel — because before "
              "any construction somebody is needed who is willing to strike the first blow.",
        "fr": "Le bélier fonce. Il ne contourne pas, il ne calcule pas l'angle, il n'attend pas "
              "que la porte s'ouvre : il baisse la tête et y va. Tout le Bélier est là, et aussi "
              "la raison pour laquelle il est le premier signe de la roue — car avant toute "
              "construction il faut quelqu'un qui soit prêt à porter le premier coup."},

    "Que la tradición le asigne la cabeza no es casual. Aries llega de cabeza en los dos "
    "sentidos: es el que piensa rápido y el que se golpea primero.": {
        "en": "That the tradition assigns it the head is no accident. Aries arrives head first "
              "in both senses: it is the one who thinks fast and the one who gets hit first.",
        "fr": "Que la tradition lui assigne la tête n'est pas fortuit. Le Bélier arrive tête la "
              "première dans les deux sens : c'est celui qui pense vite et celui qui se cogne le "
              "premier."},
}
