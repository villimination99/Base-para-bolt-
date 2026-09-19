# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · las horas planetarias y el reparto semanal
============================================================
El párrafo de las lenguas compara lo que conservan las romances y lo que
conservan las germánicas, y nombra a los cuatro dioses nórdicos que "traducen"
a los planetas: Tiw, Woden, Thor, Frigg. Los cuatro nombres se quedan como
están en las tres ediciones, igual que dies solis, porque son la prueba.

La demostración del salto de tres es aritmética pura —24 dividido entre 7 da
tres y sobran tres— y todas sus cifras van intactas. El lector tiene que poder
rehacerla contando horas.

«Lo más oculto que hay en este libro» es la coda del capítulo y juega con el
sentido literal de oculto: algo que está a la vista y nadie mira. El juego se
conserva en las tres lenguas porque es lo que la frase dice.

El reparto semanal se presenta a sí mismo sin efecto astral, y esa negación va
en la misma frase que la afirmación de que funciona. Las dos mitades se
mantienen juntas.
"""

T = {
    "Venus · viernes, vendredi. Vínculo, disfrute, arte, reconciliación": {
        "en": "Venus · viernes, vendredi. Bond, enjoyment, art, reconciliation",
        "fr": "Vénus · viernes, vendredi. Lien, plaisir, art, réconciliation"},

    "Saturno · sábado, Saturday. Límite, orden, cierre, revisión": {
        "en": "Saturn · sábado, Saturday. Limit, order, closing, review",
        "fr": "Saturne · sábado, Saturday. Limite, ordre, clôture, révision"},

    "Sol · domingo, Sunday, dies solis. Centro, descanso, identidad": {
        "en": "Sun · domingo, Sunday, dies solis. Centre, rest, identity",
        "fr": "Soleil · domingo, Sunday, dies solis. Centre, repos, identité"},

    "Las lenguas romances conservan cinco de los siete nombres planetarios y sustituyeron los "
    "dos restantes por términos cristianos —el día del Señor y el sábado hebreo—; el inglés y "
    "las lenguas germánicas conservan los siete, con los planetas traducidos a dioses locales: "
    "Tiw por Marte, Woden por Mercurio, Thor por Júpiter, Frigg por Venus. La estructura es la "
    "misma en todas.": {
        "en": "The Romance languages keep five of the seven planetary names and replaced the "
              "remaining two with Christian terms —the Lord's day and the Hebrew sabbath—; "
              "English and the Germanic languages keep all seven, with the planets translated "
              "into local gods: Tiw for Mars, Woden for Mercury, Thor for Jupiter, Frigg for "
              "Venus. The structure is the same in all of them.",
        "fr": "Les langues romanes conservent cinq des sept noms planétaires et ont remplacé les "
              "deux autres par des termes chrétiens —le jour du Seigneur et le sabbat hébreu— ; "
              "l'anglais et les langues germaniques conservent les sept, les planètes traduites "
              "en dieux locaux : Tiw pour Mars, Woden pour Mercure, Thor pour Jupiter, Frigg "
              "pour Vénus. La structure est la même partout."},

    "La pregunta que casi nadie se hace": {
        "en": "The question hardly anybody asks",
        "fr": "La question que presque personne ne se pose"},

    "¿Por qué ese orden? Los planetas ordenados por lentitud van Saturno, Júpiter, Marte, Sol, "
    "Venus, Mercurio, Luna. Pero la semana va Luna, Marte, Mercurio, Júpiter, Venus, Saturno, "
    "Sol. No coincide, y no es un orden arbitrario: es una consecuencia aritmética del reparto "
    "de las horas.": {
        "en": "Why that order? The planets arranged by slowness run Saturn, Jupiter, Mars, Sun, "
              "Venus, Mercury, Moon. But the week runs Moon, Mars, Mercury, Jupiter, Venus, "
              "Saturn, Sun. It does not match, and it is not an arbitrary order: it is an "
              "arithmetical consequence of the distribution of the hours.",
        "fr": "Pourquoi cet ordre ? Les planètes rangées par lenteur donnent Saturne, Jupiter, "
              "Mars, Soleil, Vénus, Mercure, Lune. Mais la semaine donne Lune, Mars, Mercure, "
              "Jupiter, Vénus, Saturne, Soleil. Cela ne coïncide pas, et ce n'est pas un ordre "
              "arbitraire : c'est une conséquence arithmétique de la répartition des heures."},

    "Las veinticuatro horas": {"en": "The twenty-four hours", "fr": "Les vingt-quatre heures"},

    "El sistema clásico divide el día en veinticuatro horas planetarias y les asigna un "
    "regente cada una, siguiendo el orden caldeo en bucle. La primera hora del día pertenece "
    "al planeta que da nombre al día. Y aquí ocurre lo interesante: veinticuatro dividido "
    "entre siete da tres, y sobran tres. De modo que la hora veinticinco —la primera del día "
    "siguiente— cae siempre tres puestos más abajo en la escalera caldea.": {
        "en": "The classical system divides the day into twenty-four planetary hours and "
              "assigns a ruler to each, following the Chaldean order in a loop. The first hour "
              "of the day belongs to the planet that gives the day its name. And here is where "
              "it gets interesting: twenty-four divided by seven gives three, with three left "
              "over. So the twenty-fifth hour —the first of the next day— always falls three "
              "places further down the Chaldean ladder.",
        "fr": "Le système classique divise le jour en vingt-quatre heures planétaires et leur "
              "assigne un régent à chacune, en suivant l'ordre chaldéen en boucle. La première "
              "heure du jour appartient à la planète qui donne son nom au jour. Et c'est ici que "
              "cela devient intéressant : vingt-quatre divisé par sept donne trois, et il reste "
              "trois. De sorte que la vingt-cinquième heure —la première du jour suivant— tombe "
              "toujours trois places plus bas sur l'échelle chaldéenne."},

    "Empieza en el domingo, día del Sol. Primera hora: Sol.": {
        "en": "Start on Sunday, the Sun's day. First hour: Sun.",
        "fr": "Commencez le dimanche, jour du Soleil. Première heure : Soleil."},

    "Reparte las 24 horas en orden caldeo descendente y en bucle: Sol, Venus, Mercurio, Luna, "
    "Saturno, Júpiter, Marte, Sol, Venus…": {
        "en": "Distribute the 24 hours in descending Chaldean order and in a loop: Sun, Venus, "
              "Mercury, Moon, Saturn, Jupiter, Mars, Sun, Venus…",
        "fr": "Répartissez les 24 heures dans l'ordre chaldéen descendant et en boucle : Soleil, "
              "Vénus, Mercure, Lune, Saturne, Jupiter, Mars, Soleil, Vénus…"},

    "La hora 24 del domingo cae en Mercurio. La 25 —primera del lunes— cae en la Luna. Y lunes "
    "es, efectivamente, el día de la Luna.": {
        "en": "Sunday's 24th hour falls on Mercury. The 25th —the first of Monday— falls on the "
              "Moon. And Monday is, indeed, the Moon's day.",
        "fr": "La 24e heure du dimanche tombe sur Mercure. La 25e —première du lundi— tombe sur "
              "la Lune. Et le lundi est, en effet, le jour de la Lune."},

    "Repite y saldrán los siete días en el orden exacto de la semana: Luna, Marte, Mercurio, "
    "Júpiter, Venus, Saturno, Sol. Toda la semana está contenida en un salto de tres.": {
        "en": "Repeat and the seven days will come out in the exact order of the week: Moon, "
              "Mars, Mercury, Jupiter, Venus, Saturn, Sun. The whole week is contained in a "
              "jump of three.",
        "fr": "Recommencez et les sept jours sortiront dans l'ordre exact de la semaine : Lune, "
              "Mars, Mercure, Jupiter, Vénus, Saturne, Soleil. Toute la semaine tient dans un "
              "saut de trois."},

    "Lo que acabas de ver": {
        "en": "What you have just seen", "fr": "Ce que vous venez de voir"},

    "La semana de siete días con esos nombres y en ese orden es la huella fósil de un sistema "
    "de horas planetarias que se dejó de usar hace siglos. Ha sobrevivido en el calendario de "
    "medio mundo sin que casi nadie sepa de dónde viene. Si buscabas conocimiento oculto en el "
    "sentido literal —algo que está a la vista y nadie mira—, esto es lo más oculto que hay en "
    "este libro.": {
        "en": "The seven-day week with those names and in that order is the fossil trace of a "
              "system of planetary hours that fell out of use centuries ago. It has survived in "
              "the calendar of half the world with hardly anybody knowing where it came from. "
              "If you were looking for hidden knowledge in the literal sense —something in "
              "plain sight that nobody looks at— this is the most hidden thing in this book.",
        "fr": "La semaine de sept jours avec ces noms et dans cet ordre est la trace fossile d'un "
              "système d'heures planétaires abandonné depuis des siècles. Elle a survécu dans le "
              "calendrier de la moitié du monde sans que presque personne sache d'où elle vient. "
              "Si vous cherchiez de la connaissance cachée au sens littéral —quelque chose qui "
              "est sous les yeux et que nul ne regarde—, voilà ce qu'il y a de plus caché dans "
              "ce livre."},

    "Las horas no son de sesenta minutos": {
        "en": "The hours are not of sixty minutes",
        "fr": "Les heures ne font pas soixante minutes"},

    "Un detalle que la mayoría de las tablas modernas pasa por alto: las horas planetarias son "
    "desiguales. El día se cuenta de amanecer a atardecer y se divide en doce partes; la "
    "noche, de atardecer a amanecer, en otras doce. En verano las horas diurnas son largas y "
    "las nocturnas cortas, y en invierno al contrario. Solo en los equinoccios miden sesenta "
    "minutos.": {
        "en": "A detail most modern tables overlook: the planetary hours are unequal. The day "
              "is counted from sunrise to sunset and divided into twelve parts; the night, from "
              "sunset to sunrise, into another twelve. In summer the daytime hours are long and "
              "the night ones short, and in winter the other way round. Only at the equinoxes "
              "do they measure sixty minutes.",
        "fr": "Un détail que la plupart des tables modernes laissent passer : les heures "
              "planétaires sont inégales. Le jour se compte du lever au coucher du soleil et se "
              "divise en douze parts ; la nuit, du coucher au lever, en douze autres. En été les "
              "heures diurnes sont longues et les nocturnes courtes, et en hiver l'inverse. Ce "
              "n'est qu'aux équinoxes qu'elles font soixante minutes."},

    "Busca la hora de amanecer y de atardecer de tu día y tu ciudad.": {
        "en": "Look up the time of sunrise and sunset for your day and your city.",
        "fr": "Cherchez l'heure du lever et du coucher du soleil pour votre jour et votre ville."},

    "Resta: obtienes la duración del día. Divídela entre doce y tendrás la duración de una "
    "hora planetaria diurna.": {
        "en": "Subtract: you get the length of the day. Divide it by twelve and you have the "
              "length of one daytime planetary hour.",
        "fr": "Soustrayez : vous obtenez la durée du jour. Divisez-la par douze et vous aurez la "
              "durée d'une heure planétaire diurne."},

    "La primera hora empieza en el amanecer y pertenece al regente del día.": {
        "en": "The first hour begins at sunrise and belongs to the day's ruler.",
        "fr": "La première heure commence au lever du soleil et appartient au régent du jour."},

    "Ve avanzando en orden caldeo descendente. La hora trece empieza en el atardecer y "
    "continúa la serie sin interrupción.": {
        "en": "Go on advancing in descending Chaldean order. The thirteenth hour begins at "
              "sunset and continues the series without a break.",
        "fr": "Avancez dans l'ordre chaldéen descendant. La treizième heure commence au coucher "
              "du soleil et poursuit la série sans interruption."},

    "Para qué sirve esto, honestamente": {
        "en": "What this is for, honestly", "fr": "À quoi cela sert, honnêtement"},

    "No sirve para predecir nada, y este libro no va a sugerir lo contrario. Sirve para dos "
    "cosas reales. La primera es histórica: entender de dónde salió el calendario que usas. La "
    "segunda es práctica y bastante eficaz: repartir las tareas de la semana por afinidad "
    "simbólica. Poner las conversaciones difíciles en miércoles, el entrenamiento fuerte en "
    "martes, el cierre de cuentas en sábado y el descanso de verdad en domingo no tiene ningún "
    "efecto astral — y funciona, porque cualquier estructura repetida funciona mejor que "
    "decidir cada día desde cero.": {
        "en": "It is no use for predicting anything, and this book is not going to suggest "
              "otherwise. It is good for two real things. The first is historical: understanding "
              "where the calendar you use came from. The second is practical and quite "
              "effective: distributing the week's tasks by symbolic affinity. Putting the "
              "difficult conversations on Wednesday, the hard training on Tuesday, the closing "
              "of accounts on Saturday and real rest on Sunday has no astral effect whatever — "
              "and it works, because any repeated structure works better than deciding each day "
              "from scratch.",
        "fr": "Cela ne sert à prédire quoi que ce soit, et ce livre ne va pas suggérer le "
              "contraire. Cela sert à deux choses réelles. La première est historique : "
              "comprendre d'où est sorti le calendrier dont vous vous servez. La seconde est "
              "pratique et assez efficace : répartir les tâches de la semaine par affinité "
              "symbolique. Mettre les conversations difficiles au mercredi, l'entraînement dur "
              "au mardi, la clôture des comptes au samedi et le vrai repos au dimanche n'a aucun "
              "effet astral — et cela fonctionne, parce que n'importe quelle structure répétée "
              "fonctionne mieux que de décider chaque jour à partir de zéro."},

    "Reparto semanal sugerido": {
        "en": "Suggested weekly distribution", "fr": "Répartition hebdomadaire suggérée"},

    "Planificar, ordenar la casa, cocinar para la semana": {
        "en": "Planning, tidying the house, cooking for the week",
        "fr": "Planifier, ranger la maison, cuisiner pour la semaine"},

    "Entrenamiento exigente, tareas que dan pereza, decisiones": {
        "en": "Demanding training, tasks you keep putting off, decisions",
        "fr": "Entraînement exigeant, tâches qui rebutent, décisions"},

    "Escribir, estudiar, gestiones, conversaciones difíciles": {
        "en": "Writing, studying, paperwork, difficult conversations",
        "fr": "Écrire, étudier, démarches, conversations difficiles"},

    "Reuniones, propuestas, lo que hay que hacer crecer": {
        "en": "Meetings, proposals, whatever has to be made to grow",
        "fr": "Réunions, propositions, ce qu'il faut faire croître"},

    "Personas, disfrute, arreglar lo que se rompió": {
        "en": "People, enjoyment, mending what got broken",
        "fr": "Les personnes, le plaisir, réparer ce qui s'est cassé"},

    "Revisar, tirar, cerrar, cuentas, mantenimiento": {
        "en": "Reviewing, throwing out, closing, accounts, maintenance",
        "fr": "Réviser, jeter, clore, comptes, entretien"},

    "Descanso real. Sin pantalla y sin lista de tareas": {
        "en": "Real rest. No screen and no to-do list",
        "fr": "Repos réel. Sans écran et sans liste de tâches"},
}
