# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · fichas de los arcanos I a V
===================================================
Cada ficha tiene la misma forma: la letra, lo que rige, la descripción de la
lámina y tres párrafos —derecho, invertido y la pregunta—. Las etiquetas
«Derecho», «Invertido» y «La pregunta» van dentro del párrafo y no son un
segmento aparte, así que aparecen traducidas dentro de cada uno; conviene que
digan siempre lo mismo, porque el lector las usa para orientarse en la página.

Las letras hebreas llevan la transliteración usual de cada lengua: guímel es
Gimel en inglés y Guimel en francés, dálet es Daleth en las dos.
"""

T = {
    # ── I · El Mago ────────────────────────────────────────────────────────
    "Derecho: tienes los medios y todavía no has empezado. Es la carta del que puede, y por "
    "eso es la más incómoda de las veintidós: no admite la excusa de la falta de recursos. "
    "La mesa está puesta.": {
        "en": "Upright: you have the means and you have not started yet. It is the card of the "
              "one who can, and that is why it is the most uncomfortable of the twenty-two: it "
              "does not accept the excuse of lacking resources. The table is laid.",
        "fr": "À l'endroit : vous avez les moyens et vous n'avez pas encore commencé. C'est la "
              "carte de celui qui peut, et c'est pourquoi elle est la plus inconfortable des "
              "vingt-deux : elle n'admet pas l'excuse du manque de moyens. La table est mise."},

    "Invertido: habilidad sin dirección. Mucho talento repartido en demasiadas cosas, o "
    "destreza usada para quedar bien en vez de para hacer. También el charlatán, que es el "
    "mago que se quedó en el gesto.": {
        "en": "Reversed: skill without direction. A great deal of talent spread over too many "
              "things, or dexterity used to impress instead of to make. Also the charlatan, "
              "who is the magician who stopped at the gesture.",
        "fr": "Inversée : de l'habileté sans direction. Beaucoup de talent réparti sur trop de "
              "choses, ou de l'adresse employée à faire bonne figure plutôt qu'à faire. Aussi "
              "le charlatan, qui est le magicien resté au geste."},

    "La pregunta: ¿Qué es lo que ya podrías hacer hoy con lo que tienes en la mesa?": {
        "en": "The question: What could you already do today with what is on your table?",
        "fr": "La question : que pourriez-vous déjà faire aujourd'hui avec ce qui est sur la "
              "table ?"},

    # ── II · La Sacerdotisa ────────────────────────────────────────────────
    "II · La Sacerdotisa": {
        "en": "II · The High Priestess", "fr": "II · La Grande Prêtresse"},
    "Bet · valor 2 · doble · planeta": {
        "en": "Beth · value 2 · double · planet",
        "fr": "Beth · valeur 2 · double · planète"},
    "Una figura sentada, un libro entreabierto sobre el regazo, entre dos columnas.": {
        "en": "A seated figure, a half-open book on her lap, between two columns.",
        "fr": "Une figure assise, un livre entrouvert sur les genoux, entre deux colonnes."},

    "Derecho: hay algo que sabes y no has dicho, o que sabrías si te quedaras quieto un "
    "rato. Es la carta del saber que no se exhibe y del que espera el momento. Frente al "
    "Mago, que actúa, ella lee.": {
        "en": "Upright: there is something you know and have not said, or that you would know "
              "if you stayed still for a while. It is the card of knowledge that is not "
              "displayed and of the one who waits for the moment. Against the Magician, who "
              "acts, she reads.",
        "fr": "À l'endroit : il y a quelque chose que vous savez et n'avez pas dit, ou que vous "
              "sauriez si vous restiez immobile un moment. C'est la carte du savoir qui ne "
              "s'exhibe pas et de celui qui attend le moment. Face au Magicien, qui agit, elle "
              "lit."},

    "Invertido: reserva convertida en secreto inútil. Guardar por costumbre lo que ya no "
    "hay motivo para guardar, o confundir el silencio con la profundidad.": {
        "en": "Reversed: reserve turned into a useless secret. Keeping out of habit what there "
              "is no longer any reason to keep, or mistaking silence for depth.",
        "fr": "Inversée : une réserve devenue secret inutile. Garder par habitude ce qu'il n'y "
              "a plus de raison de garder, ou confondre le silence avec la profondeur."},

    "La pregunta: ¿Qué sabes de esto que no has puesto en palabras todavía?": {
        "en": "The question: What do you know about this that you have not yet put into words?",
        "fr": "La question : que savez-vous de cela que vous n'avez pas encore mis en mots ?"},

    # ── III · La Emperatriz ────────────────────────────────────────────────
    "III · La Emperatriz": {"en": "III · The Empress", "fr": "III · L'Impératrice"},
    "Guímel · valor 3 · doble · planeta": {
        "en": "Gimel · value 3 · double · planet",
        "fr": "Guimel · valeur 3 · double · planète"},
    "Una mujer sentada con cetro y escudo, mirando a un lado.": {
        "en": "A seated woman with sceptre and shield, looking to one side.",
        "fr": "Une femme assise avec sceptre et écu, le regard de côté."},

    "Derecho: algo está creciendo y hay que atenderlo. Es la carta de lo fértil y de lo que "
    "se hace cuidando, no forzando. También la abundancia concreta: lo que hay, no lo que "
    "se espera.": {
        "en": "Upright: something is growing and needs tending. It is the card of the fertile "
              "and of what gets made by tending rather than forcing. Also concrete abundance: "
              "what there is, not what is hoped for.",
        "fr": "À l'endroit : quelque chose pousse et demande à être soigné. C'est la carte du "
              "fertile et de ce qui se fait en prenant soin, non en forçant. Aussi l'abondance "
              "concrète : ce qu'il y a, non ce qu'on espère."},

    "Invertido: crecimiento sin cauce, o cuidado que asfixia. La sobreprotección de un "
    "proyecto o de una persona hasta impedirle crecer solo.": {
        "en": "Reversed: growth with no channel, or care that suffocates. Overprotecting a "
              "project or a person to the point of preventing them from growing on their own.",
        "fr": "Inversée : une croissance sans lit, ou un soin qui étouffe. La surprotection "
              "d'un projet ou d'une personne jusqu'à l'empêcher de grandir seul."},

    "La pregunta: ¿Qué está creciendo aquí, y lo estoy atendiendo o lo estoy vigilando?": {
        "en": "The question: What is growing here, and am I tending it or watching over it?",
        "fr": "La question : qu'est-ce qui pousse ici, et est-ce que j'en prends soin ou "
              "est-ce que je le surveille ?"},

    # ── IV · El Emperador ──────────────────────────────────────────────────
    "IV · El Emperador": {"en": "IV · The Emperor", "fr": "IV · L'Empereur"},
    "Dálet · valor 4 · doble · planeta": {
        "en": "Daleth · value 4 · double · planet",
        "fr": "Daleth · valeur 4 · double · planète"},
    "Un hombre sentado de perfil, con las piernas cruzadas y un cetro.": {
        "en": "A man seated in profile, legs crossed and holding a sceptre.",
        "fr": "Un homme assis de profil, les jambes croisées et un sceptre à la main."},

    "Derecho: hace falta estructura y hace falta ya. Un marco, un límite, una decisión que "
    "ordene lo que está disperso. Es la carta menos poética del mazo y una de las más "
    "necesarias.": {
        "en": "Upright: structure is needed and it is needed now. A frame, a limit, a decision "
              "that puts what is scattered in order. It is the least poetic card in the deck "
              "and one of the most necessary.",
        "fr": "À l'endroit : il faut de la structure et il en faut maintenant. Un cadre, une "
              "limite, une décision qui mette en ordre ce qui est dispersé. C'est la carte la "
              "moins poétique du jeu et l'une des plus nécessaires."},

    "Invertido: rigidez, o autoridad sostenida por costumbre y no por criterio. El marco "
    "que se levantó para proteger algo y ahora lo impide.": {
        "en": "Reversed: rigidity, or authority sustained by habit and not by judgement. The "
              "frame that was put up to protect something and now prevents it.",
        "fr": "Inversée : de la rigidité, ou une autorité tenue par habitude et non par "
              "discernement. Le cadre élevé pour protéger quelque chose et qui maintenant "
              "l'empêche."},

    "La pregunta: ¿Qué necesita aquí una estructura, y quién la va a poner?": {
        "en": "The question: What here needs a structure, and who is going to provide it?",
        "fr": "La question : qu'est-ce qui a besoin ici d'une structure, et qui va la mettre ?"},

    # ── V · El Sumo Sacerdote ──────────────────────────────────────────────
    "V · El Sumo Sacerdote": {
        "en": "V · The Hierophant", "fr": "V · Le Hiérophante"},
    "He · valor 5 · simple · signo": {
        "en": "He · value 5 · simple · sign", "fr": "Hé · valeur 5 · simple · signe"},
    "Una figura con mitra y bastón, dos personas más pequeñas ante ella.": {
        "en": "A figure with mitre and staff, two smaller people before him.",
        "fr": "Une figure à mitre et bâton, deux personnages plus petits devant elle."},

    "Derecho: hay algo que aprender de alguien, o algo que transmitir. Es la carta de la "
    "enseñanza y del marco compartido — la tradición, la regla, lo que se hereda. Salida en "
    "una tirada, suele señalar que conviene consultar antes de decidir.": {
        "en": "Upright: there is something to be learnt from someone, or something to pass on. "
              "It is the card of teaching and of the shared frame — tradition, the rule, what "
              "is inherited. When it comes up in a spread it usually indicates that it is "
              "worth consulting before deciding.",
        "fr": "À l'endroit : il y a quelque chose à apprendre de quelqu'un, ou quelque chose à "
              "transmettre. C'est la carte de l'enseignement et du cadre partagé — la "
              "tradition, la règle, ce dont on hérite. Sortie dans un tirage, elle signale "
              "d'ordinaire qu'il vaut mieux consulter avant de décider."},

    "Invertido: dogma. Repetir una regla porque es la regla, o buscar un maestro para no "
    "tener que decidir. También el guía que se ha acostumbrado a que le crean.": {
        "en": "Reversed: dogma. Repeating a rule because it is the rule, or looking for a "
              "master so as not to have to decide. Also the guide who has grown used to being "
              "believed.",
        "fr": "Inversée : le dogme. Répéter une règle parce que c'est la règle, ou chercher un "
              "maître pour ne pas avoir à décider. Aussi le guide qui s'est habitué à ce qu'on "
              "le croie."},
}
