# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · cierre de Sagitario y apertura de Capricornio
===============================================================
La práctica de Sagitario funciona por sustracción: la idea nueva y fascinante
se anota y no se persigue, y al final del mes se relee la lista. El original
avisa de cuándo aparecerá —«sobre la segunda semana»— y ese pronóstico es lo
que hace que el ejercicio se sostenga: se conserva con su inciso.

La cabra montesa de Capricornio lleva cola de pez en algunas versiones del
símbolo, y el párrafo se apoya en ella para decir que debajo de la escalada
hay una profundidad. La imagen doble se traduce entera; sin la cola, la frase
siguiente no se sostiene.

«Se siente valioso cuando produce» es la trampa central del signo y va con las
dos mitades enfrentadas: cuando produce y cuando no produce.
"""

T = {
    "Comer con horario aunque viaje. Es el signo que come a cualquier hora y cualquier cosa "
    "cuando está en movimiento.": {
        "en": "Eating to a schedule even when travelling. It is the sign that eats at any hour "
              "and eats anything when it is on the move.",
        "fr": "Manger à heures fixes même en voyage. C'est le signe qui mange à n'importe quelle "
              "heure et n'importe quoi quand il est en mouvement."},

    "Fibra y fruta: su tránsito digestivo agradece la regularidad que su vida no tiene.": {
        "en": "Fibre and fruit: its digestive transit is grateful for the regularity its life "
              "does not have.",
        "fr": "Fibres et fruits : son transit digestif apprécie la régularité que sa vie n'a "
              "pas."},

    "Sagitario no necesita más horizonte. Necesita comprobar qué hay al fondo de una sola "
    "cosa.": {
        "en": "Sagittarius does not need more horizon. It needs to find out what is at the "
              "bottom of one single thing.",
        "fr": "Le Sagittaire n'a pas besoin de plus d'horizon. Il a besoin de vérifier ce qu'il y "
              "a au fond d'une seule chose."},

    "Elige algo que empezaste con entusiasmo y abandonaste al perder la novedad.": {
        "en": "Choose something you began with enthusiasm and abandoned when it stopped being "
              "new.",
        "fr": "Choisissez quelque chose que vous avez commencé avec enthousiasme et abandonné "
              "quand la nouveauté est retombée."},

    "Retómalo con un compromiso de cuatro semanas y un plazo escrito. Solo cuatro semanas: es "
    "un plazo que Sagitario puede sostener.": {
        "en": "Take it up again with a four-week commitment and a written deadline. Only four "
              "weeks: it is a span Sagittarius can sustain.",
        "fr": "Reprenez-le avec un engagement de quatre semaines et un délai écrit. Quatre "
              "semaines seulement : c'est un délai que le Sagittaire peut tenir."},

    "Cuando aparezca la idea nueva y fascinante —aparecerá, sobre la segunda semana—, anótala "
    "en una lista y no la persigas.": {
        "en": "When the new and fascinating idea appears —it will, around the second week— "
              "write it down on a list and do not chase it.",
        "fr": "Quand l'idée nouvelle et fascinante apparaîtra —elle apparaîtra, vers la deuxième "
              "semaine—, notez-la sur une liste et ne la poursuivez pas."},

    "Al final del mes, lee la lista de ideas que no persiguiste. Sagitario suele descubrir que "
    "la mitad ya no le interesan, y esa es toda la lección.": {
        "en": "At the end of the month, read the list of ideas you did not chase. Sagittarius "
              "usually discovers that half of them no longer interest it, and that is the whole "
              "lesson.",
        "fr": "À la fin du mois, lisez la liste des idées que vous n'avez pas poursuivies. Le "
              "Sagittaire découvre d'ordinaire que la moitié ne l'intéressent plus, et c'est là "
              "toute la leçon."},

    "Con Aries y Leo, sus compañeros de Fuego: entusiasmo compartido y ningún freno.": {
        "en": "With Aries and Leo, its companions in Fire: shared enthusiasm and no brakes.",
        "fr": "Avec le Bélier et le Lion, ses compagnons de Feu : enthousiasme partagé et aucun "
              "frein."},

    "Con Géminis, su signo opuesto: dos mutables curiosos, uno buscando datos y el otro "
    "sentido. Se complementan muy bien.": {
        "en": "With Gemini, its opposite sign: two curious mutable signs, one looking for data "
              "and the other for meaning. They complement each other very well.",
        "fr": "Avec les Gémeaux, son signe opposé : deux mutables curieux, l'un cherchant des "
              "données et l'autre du sens. Ils se complètent très bien."},

    "Con Libra y Acuario, de Aire: conversación de altura y espacio mutuo.": {
        "en": "With Libra and Aquarius, of Air: conversation of some height and mutual space.",
        "fr": "Avec la Balance et le Verseau, d'Air : conversation de haute volée et espace "
              "mutuel."},

    "Con Virgo y Piscis hay fricción mutable: cuatro formas distintas de adaptarse y ninguna "
    "que se parezca.": {
        "en": "With Virgo and Pisces there is mutable friction: four different ways of adapting "
              "and not one of them alike.",
        "fr": "Avec la Vierge et les Poissons, il y a friction mutable : quatre façons "
              "différentes de s'adapter et aucune qui se ressemble."},

    "Con Tauro, Cáncer y Capricornio hay que traducir la necesidad de raíz: ellos la tienen y "
    "Sagitario la interpreta como límite.": {
        "en": "With Taurus, Cancer and Capricorn the need for roots has to be translated: they "
              "have it and Sagittarius reads it as a limit.",
        "fr": "Avec le Taureau, le Cancer et le Capricorne, il faut traduire le besoin de racine : "
              "eux l'ont et le Sagittaire l'interprète comme une limite."},

    "¿De qué he escapado este mes llamándolo oportunidad?": {
        "en": "What have I escaped from this month by calling it an opportunity?",
        "fr": "À quoi ai-je échappé ce mois-ci en l'appelant une occasion ?"},

    "¿Dónde me pasé de la raya sin darme cuenta?": {
        "en": "Where did I overstep the line without noticing?",
        "fr": "Où ai-je dépassé la mesure sans m'en rendre compte ?"},

    "¿Qué he sostenido más de cuatro semanas seguidas?": {
        "en": "What have I sustained for more than four weeks in a row?",
        "fr": "Qu'ai-je tenu plus de quatre semaines d'affilée ?"},

    # ── Capricornio ────────────────────────────────────────────────────────
    "22 de diciembre a 20 de enero": {
        "en": "22 December to 20 January", "fr": "Du 22 décembre au 20 janvier"},

    "Plomo": {"en": "Lead", "fr": "Plomb"},
    "Ónix y azabache": {"en": "Onyx and jet", "fr": "Onyx et jais"},
    "Gris y negro": {"en": "Grey and black", "fr": "Gris et noir"},
    "Rodillas, huesos, piel y dientes": {
        "en": "Knees, bones, skin and teeth", "fr": "Genoux, os, peau et dents"},
    "Yo construyo": {"en": "I build", "fr": "Je bâtis"},

    "La cabra montesa sube. No corre, no salta con gracia: encuentra el apoyo siguiente y lo "
    "usa, y así llega donde no llega nadie. En algunas versiones del símbolo la mitad inferior "
    "es un pez, y esa cola marina guarda el secreto del signo: debajo de la escalada hay una "
    "profundidad que Capricornio rara vez muestra.": {
        "en": "The mountain goat climbs. It does not run, it does not leap gracefully: it finds "
              "the next foothold and uses it, and so it gets where nobody else gets. In some "
              "versions of the symbol the lower half is a fish, and that sea tail holds the "
              "sign's secret: beneath the climb there is a depth Capricorn seldom shows.",
        "fr": "La chèvre de montagne monte. Elle ne court pas, elle ne bondit pas avec grâce : "
              "elle trouve l'appui suivant et s'en sert, et ainsi elle arrive là où personne "
              "n'arrive. Dans certaines versions du symbole la moitié inférieure est un poisson, "
              "et cette queue marine garde le secret du signe : sous l'escalade il y a une "
              "profondeur que le Capricorne montre rarement."},

    "Saturno, su regente, es el planeta del límite y del tiempo. Capricornio es el único signo "
    "que entiende el tiempo como aliado y no como amenaza.": {
        "en": "Saturn, its ruler, is the planet of limit and of time. Capricorn is the only "
              "sign that understands time as an ally and not as a threat.",
        "fr": "Saturne, son régent, est la planète de la limite et du temps. Le Capricorne est le "
              "seul signe qui comprenne le temps comme un allié et non comme une menace."},

    "Capricornio termina lo que empieza y lo termina bien. Tiene una capacidad de esfuerzo "
    "sostenido a largo plazo que ningún otro signo iguala, y una tolerancia a la gratificación "
    "aplazada que le permite construir cosas que tardan años.": {
        "en": "Capricorn finishes what it begins and finishes it well. It has a capacity for "
              "sustained long-term effort that no other sign matches, and a tolerance for "
              "deferred gratification that lets it build things that take years.",
        "fr": "Le Capricorne termine ce qu'il commence et le termine bien. Il a une capacité "
              "d'effort soutenu sur le long terme qu'aucun autre signe n'égale, et une tolérance "
              "à la gratification différée qui lui permet de bâtir des choses qui prennent des "
              "années."},

    "Es también el signo más responsable. Cuando Capricornio se compromete, el compromiso se "
    "cumple, y esa fiabilidad absoluta es la razón de que acabe cargando con el peso de casi "
    "todos los grupos en los que entra.": {
        "en": "It is also the most responsible sign. When Capricorn commits, the commitment is "
              "kept, and that absolute reliability is the reason it ends up carrying the weight "
              "of almost every group it joins.",
        "fr": "C'est aussi le signe le plus responsable. Quand le Capricorne s'engage, "
              "l'engagement est tenu, et cette fiabilité absolue est la raison pour laquelle il "
              "finit par porter le poids de presque tous les groupes où il entre."},

    "Su sombra es la dureza, y empieza consigo mismo. Capricornio se exige un rendimiento que "
    "no negocia ni cuando está enfermo, y desde ahí juzga a los demás por un estándar que "
    "nadie le ha pedido.": {
        "en": "Its shadow is hardness, and it starts with itself. Capricorn demands of itself a "
              "performance it will not negotiate even when it is ill, and from there it judges "
              "others by a standard nobody asked it for.",
        "fr": "Son ombre est la dureté, et elle commence avec lui-même. Le Capricorne s'impose un "
              "rendement qu'il ne négocie pas même quand il est malade, et de là il juge les "
              "autres selon un standard que personne ne lui a demandé."},

    "La segunda es la confusión entre valor y utilidad. Capricornio se siente valioso cuando "
    "produce, y cuando no produce se siente prescindible. Es la trampa más cara del signo.": {
        "en": "The second is the confusion between worth and usefulness. Capricorn feels "
              "valuable when it produces, and when it does not produce it feels dispensable. It "
              "is the sign's most expensive trap.",
        "fr": "La deuxième est la confusion entre valeur et utilité. Le Capricorne se sent de la "
              "valeur quand il produit, et quand il ne produit pas il se sent superflu. C'est le "
              "piège le plus coûteux du signe."},

    "La tercera es el aislamiento. Pedir ayuda le parece una forma de fallar, así que carga "
    "solo hasta que no puede más, y entonces tampoco lo dice.": {
        "en": "The third is isolation. Asking for help looks to it like a form of failing, so "
              "it carries the load alone until it cannot carry any more, and then it does not "
              "say so either.",
        "fr": "La troisième est l'isolement. Demander de l'aide lui paraît une façon d'échouer, "
              "alors il porte seul jusqu'à n'en plus pouvoir, et alors il ne le dit pas non "
              "plus."},

    "El eje Capricornio–Cáncer": {
        "en": "The Capricorn–Cancer axis", "fr": "L'axe Capricorne–Cancer"},

    "El eje del mundo y del hogar. Capricornio conquista y luego no sabe volver a casa; Cáncer "
    "se queda en casa y luego se pregunta por qué no conquistó nada.": {
        "en": "The axis of the world and the home. Capricorn conquers and then does not know "
              "how to come home; Cancer stays at home and then asks itself why it conquered "
              "nothing.",
        "fr": "L'axe du monde et du foyer. Le Capricorne conquiert puis ne sait pas rentrer à la "
              "maison ; le Cancer reste à la maison puis se demande pourquoi il n'a rien "
              "conquis."},
}
