# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · el reparto del cuerpo y las tres piezas del retrato
=====================================================================
El aviso que abre el capítulo —esto no es medicina y no lo ha sido nunca, ni
cuando se usaba como tal— es la línea que separa este libro de un almanaque, y
va literal en las tres lenguas.

Las doce filas del reparto son etiquetas de tabla con una glosa detrás del
punto medio. Se traducen con los nombres anatómicos corrientes, no con los de
manual: cefalea tensional es tension headache y céphalée de tension, tránsito
es transit y transit, retorno venoso es venous return y retour veineux.

«El cuerpo» es el nombre de una sección que se repite en los doce capítulos de
signo y aparece entrecomillado: se fija aquí como «The body» y « Le corps »
para que las doce remisiones coincidan.

Ascendente es Ascendant en las dos lenguas, con mayúscula, porque el libro lo
trata como una de las tres piezas y no como un adjetivo.
"""

T = {
    '<span class="fig-n">Lám. 3</span> La melotesia: los doce signos repartidos del vértice '
    "del cráneo a la planta del pie, en el orden de la rueda. El color indica el elemento.": {
        "en": '<span class="fig-n">Pl. 3</span> Melothesia: the twelve signs distributed from '
              "the crown of the skull to the sole of the foot, in the order of the wheel. The "
              "colour indicates the element.",
        "fr": '<span class="fig-n">Pl. 3</span> La mélothésie : les douze signes répartis du '
              "sommet du crâne à la plante du pied, dans l'ordre de la roue. La couleur indique "
              "l'élément."},

    "Cómo leer esta lámina — y cómo no": {
        "en": "How to read this plate — and how not to",
        "fr": "Comment lire cette planche — et comment ne pas la lire"},

    "Lo primero, y va en serio: esto no es medicina y no lo ha sido nunca, ni cuando se usaba "
    "como tal. La melotesia es un sistema mnemotécnico y simbólico. No diagnostica, no predice "
    "dolencias y no debe usarse para decidir nada sobre tu salud. Si algo te duele, la "
    "respuesta está en una consulta médica.": {
        "en": "First of all, and this is meant seriously: this is not medicine and it never has "
              "been, not even when it was used as such. Melothesia is a mnemonic and symbolic "
              "system. It does not diagnose, it does not predict ailments and it must not be "
              "used to decide anything about your health. If something hurts, the answer is in "
              "a medical consultation.",
        "fr": "D'abord, et c'est sérieux : ceci n'est pas de la médecine et ne l'a jamais été, "
              "pas même quand on s'en servait comme telle. La mélothésie est un système "
              "mnémotechnique et symbolique. Elle ne diagnostique pas, elle ne prédit pas de "
              "maux et elle ne doit servir à décider quoi que ce soit sur votre santé. Si "
              "quelque chose vous fait mal, la réponse est dans une consultation médicale."},

    "Dicho eso, la lámina sí sirve para algo, y es bastante más útil de lo que parece: "
    "convierte los doce signos en doce zonas de mantenimiento. Cada capítulo de la segunda "
    "parte tiene una sección «El cuerpo» que desarrolla la zona de su signo con cuidados que "
    "son de sentido común —movilidad, descanso, hidratación, hábito postural— y no de "
    "superstición. Recorrer los doce signos a lo largo de un año es, entre otras cosas, "
    "revisar el cuerpo entero por partes.": {
        "en": "That said, the plate is good for something, and it is a good deal more useful "
              "than it looks: it turns the twelve signs into twelve zones of maintenance. Every "
              "chapter of the second part has a section «The body» that develops its sign's "
              "zone with care that is common sense —mobility, rest, hydration, postural habit— "
              "and not superstition. Going through the twelve signs over a year is, among other "
              "things, reviewing the whole body part by part.",
        "fr": "Cela dit, la planche sert bien à quelque chose, et elle est bien plus utile "
              "qu'elle n'en a l'air : elle transforme les douze signes en douze zones "
              "d'entretien. Chaque chapitre de la deuxième partie comporte une section « Le "
              "corps » qui développe la zone de son signe avec des soins de bon sens "
              "—mobilité, repos, hydratation, habitude posturale— et non de superstition. "
              "Parcourir les douze signes au long d'une année, c'est entre autres passer le "
              "corps entier en revue par parties."},

    "El reparto completo": {
        "en": "The complete distribution", "fr": "La répartition complète"},

    "Cabeza, cara, cerebro · Tensión mandibular, cefalea tensional": {
        "en": "Head, face, brain · Jaw tension, tension headache",
        "fr": "Tête, visage, cerveau · Tension de la mâchoire, céphalée de tension"},

    "Cuello, garganta, tiroides · Rigidez cervical": {
        "en": "Neck, throat, thyroid · Cervical stiffness",
        "fr": "Cou, gorge, thyroïde · Raideur cervicale"},

    "Hombros, brazos, manos, pulmones · Respiración corta": {
        "en": "Shoulders, arms, hands, lungs · Short breathing",
        "fr": "Épaules, bras, mains, poumons · Respiration courte"},

    "Pecho, estómago, diafragma · Digestión y emoción": {
        "en": "Chest, stomach, diaphragm · Digestion and emotion",
        "fr": "Poitrine, estomac, diaphragme · Digestion et émotion"},

    "Corazón, espalda alta, circulación · Postura y presencia": {
        "en": "Heart, upper back, circulation · Posture and presence",
        "fr": "Cœur, haut du dos, circulation · Posture et présence"},

    "Abdomen, intestino, bazo · Tránsito y tolerancias": {
        "en": "Abdomen, intestine, spleen · Transit and tolerances",
        "fr": "Abdomen, intestin, rate · Transit et tolérances"},

    "Riñones, lumbares, piel · Equilibrio hídrico": {
        "en": "Kidneys, lower back, skin · Water balance",
        "fr": "Reins, lombaires, peau · Équilibre hydrique"},

    "Pelvis, suelo pélvico, aparato reproductor": {
        "en": "Pelvis, pelvic floor, reproductive system",
        "fr": "Bassin, plancher pelvien, appareil reproducteur"},

    "Caderas, muslos, hígado · Movilidad de cadera": {
        "en": "Hips, thighs, liver · Hip mobility",
        "fr": "Hanches, cuisses, foie · Mobilité de hanche"},

    "Rodillas, huesos, articulaciones, dientes": {
        "en": "Knees, bones, joints, teeth", "fr": "Genoux, os, articulations, dents"},

    "Pantorrillas, tobillos, circulación de retorno": {
        "en": "Calves, ankles, venous return",
        "fr": "Mollets, chevilles, retour veineux"},

    "Pies, sistema linfático · Drenaje y apoyo": {
        "en": "Feet, lymphatic system · Drainage and support",
        "fr": "Pieds, système lymphatique · Drainage et appui"},

    "La estructura oculta del reparto": {
        "en": "The hidden structure of the distribution",
        "fr": "La structure cachée de la répartition"},

    "Merece la pena mirar la lámina dos veces, porque el reparto tiene una coherencia interna "
    "que no salta a la vista. Los tres signos de Fuego caen en cabeza, corazón y muslos: los "
    "tres motores del movimiento. Los de Tierra, en cuello, abdomen y rodillas: las tres "
    "articulaciones que sostienen la vertical. Los de Aire, en hombros, riñones y "
    "pantorrillas: los tres puntos de intercambio y de retorno. Y los de Agua, en pecho, "
    "pelvis y pies: los tres lugares donde el cuerpo guarda lo que no dice.": {
        "en": "It is worth looking at the plate twice, because the distribution has an internal "
              "coherence that does not leap out. The three Fire signs fall on head, heart and "
              "thighs: the three motors of movement. Those of Earth, on neck, abdomen and "
              "knees: the three joints that hold the vertical. Those of Air, on shoulders, "
              "kidneys and calves: the three points of exchange and of return. And those of "
              "Water, on chest, pelvis and feet: the three places where the body keeps what it "
              "does not say.",
        "fr": "Il vaut la peine de regarder la planche deux fois, car la répartition a une "
              "cohérence interne qui ne saute pas aux yeux. Les trois signes de Feu tombent sur "
              "la tête, le cœur et les cuisses : les trois moteurs du mouvement. Ceux de Terre, "
              "sur le cou, l'abdomen et les genoux : les trois articulations qui tiennent la "
              "verticale. Ceux d'Air, sur les épaules, les reins et les mollets : les trois "
              "points d'échange et de retour. Et ceux d'Eau, sur la poitrine, le bassin et les "
              "pieds : les trois lieux où le corps garde ce qu'il ne dit pas."},

    "Los ejes también funcionan en el cuerpo": {
        "en": "The axes work in the body too",
        "fr": "Les axes fonctionnent aussi dans le corps"},

    "Cada eje de signos opuestos une dos zonas que en la práctica trabajan juntas. Aries y "
    "Libra: cabeza y lumbares, los dos extremos de la cadena postural. Tauro y Escorpio: "
    "garganta y pelvis, los dos diafragmas del cuerpo. Géminis y Sagitario: hombros y caderas, "
    "las dos cinturas. Cáncer y Capricornio: estómago y rodillas. Leo y Acuario: corazón y "
    "retorno venoso. Virgo y Piscis: intestino y sistema linfático. Que la tradición acertara "
    "en esos emparejamientos con la anatomía que tenía disponible es, por lo menos, notable.": {
        "en": "Each axis of opposite signs joins two zones that in practice work together. "
              "Aries and Libra: head and lower back, the two ends of the postural chain. Taurus "
              "and Scorpio: throat and pelvis, the body's two diaphragms. Gemini and "
              "Sagittarius: shoulders and hips, the two girdles. Cancer and Capricorn: stomach "
              "and knees. Leo and Aquarius: heart and venous return. Virgo and Pisces: "
              "intestine and lymphatic system. That the tradition got those pairings right with "
              "the anatomy available to it is, at the very least, remarkable.",
        "fr": "Chaque axe de signes opposés unit deux zones qui en pratique travaillent "
              "ensemble. Bélier et Balance : tête et lombaires, les deux extrémités de la chaîne "
              "posturale. Taureau et Scorpion : gorge et bassin, les deux diaphragmes du corps. "
              "Gémeaux et Sagittaire : épaules et hanches, les deux ceintures. Cancer et "
              "Capricorne : estomac et genoux. Lion et Verseau : cœur et retour veineux. Vierge "
              "et Poissons : intestin et système lymphatique. Que la tradition ait vu juste dans "
              "ces appariements avec l'anatomie dont elle disposait est, pour le moins, "
              "remarquable."},

    # ── Por qué no te reconoces en tu signo ────────────────────────────────
    "Es la objeción más frecuente y la más razonable. Alguien lee la descripción de su signo "
    "solar, no se reconoce en absoluto, y concluye con toda lógica que el sistema no funciona. "
    "Conviene responderla bien, porque la respuesta explica cómo está construido este libro.": {
        "en": "It is the commonest objection and the most reasonable. Somebody reads the "
              "description of their sun sign, does not recognise themselves at all, and "
              "concludes, quite logically, that the system does not work. It deserves a proper "
              "answer, because the answer explains how this book is built.",
        "fr": "C'est l'objection la plus fréquente et la plus raisonnable. Quelqu'un lit la "
              "description de son signe solaire, ne s'y reconnaît pas du tout, et conclut en "
              "toute logique que le système ne marche pas. Il convient d'y répondre "
              "correctement, car la réponse explique comment ce livre est bâti."},

    "Hay tres respuestas, y las tres son verdad": {
        "en": "There are three answers, and all three are true",
        "fr": "Il y a trois réponses, et toutes les trois sont vraies"},

    "El decanato. Un signo son treinta grados y tres caras distintas. El capítulo anterior lo "
    "desarrolla: mucha gente que «no se parece a su signo» se reconoce inmediatamente al leer "
    "su decanato.": {
        "en": "The decan. A sign is thirty degrees and three different faces. The previous "
              "chapter develops it: many people who «are not like their sign» recognise "
              "themselves immediately on reading their decan.",
        "fr": "Le décan. Un signe fait trente degrés et trois faces différentes. Le chapitre "
              "précédent le développe : bien des gens qui « ne ressemblent pas à leur signe » "
              "se reconnaissent immédiatement en lisant leur décan."},

    "Los otros dos puntos. La astrología tradicional nunca describió a nadie por su Sol "
    "únicamente. Trabajaba con tres piezas: el Sol, la Luna y el Ascendente. El signo que dice "
    "la prensa es solo la primera.": {
        "en": "The other two points. Traditional astrology never described anybody by their Sun "
              "alone. It worked with three pieces: the Sun, the Moon and the Ascendant. The "
              "sign the newspapers give is only the first.",
        "fr": "Les deux autres points. L'astrologie traditionnelle n'a jamais décrit personne "
              "par son seul Soleil. Elle travaillait avec trois pièces : le Soleil, la Lune et "
              "l'Ascendant. Le signe que donne la presse n'est que le premier."},

    "Nadie es un signo. Los doce están en todo el mundo, unos desarrollados y otros dormidos, "
    "y eso es exactamente lo que hace útil el recorrido de doce meses que propone la tercera "
    "parte.": {
        "en": "Nobody is a sign. The twelve are in everybody, some developed and others asleep, "
              "and that is exactly what makes the twelve-month journey the third part proposes "
              "useful.",
        "fr": "Personne n'est un signe. Les douze sont en chacun, les uns développés et les "
              "autres endormis, et c'est exactement ce qui rend utile le parcours de douze mois "
              "que propose la troisième partie."},

    "Las tres piezas del retrato clásico": {
        "en": "The three pieces of the classical portrait",
        "fr": "Les trois pièces du portrait classique"},

    "Sol, Luna y Ascendente": {
        "en": "Sun, Moon and Ascendant", "fr": "Soleil, Lune et Ascendant"},

    "Lo que quieres ser. El proyecto, la dirección, la identidad que reconoces como tuya. Es "
    "el signo de la fecha.": {
        "en": "What you want to be. The project, the direction, the identity you recognise as "
              "yours. It is the sign of the date.",
        "fr": "Ce que vous voulez être. Le projet, la direction, l'identité que vous reconnaissez "
              "comme vôtre. C'est le signe de la date."},

    "Cómo reaccionas cuando no eliges. El hábito emocional, el ritmo, lo que buscas para "
    "calmarte. Cambia de signo cada dos días y medio.": {
        "en": "How you react when you are not choosing. The emotional habit, the rhythm, what "
              "you reach for to calm yourself. It changes sign every two and a half days.",
        "fr": "Comment vous réagissez quand vous ne choisissez pas. L'habitude émotionnelle, le "
              "rythme, ce que vous cherchez pour vous calmer. Elle change de signe tous les deux "
              "jours et demi."},
}
