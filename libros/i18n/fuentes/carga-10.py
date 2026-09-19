# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · las señales que paran una sesión y la ecuación del NIOSH
=============================================================================
La lista de las cinco señales se traduce sin adornos y sin reordenar. Cada
línea nombra un síntoma y nada más; el párrafo que las sigue es el que dice
qué hacer. Repartir el consejo por las cinco líneas las alargaría y haría más
difícil recorrerlas de un vistazo, que es exactamente para lo que están.

Los nombres largos de los factores llevan aquí la sigla delante —HM · Horizontal—
y en la lámina van sueltos. La sigla no cambia de idioma y el nombre sí, de
modo que las dos piezas se traducen por separado y se encuentran en la página.
"""

T = {
    "Dolor articular localizado": {
        "en": "Localised joint pain", "fr": "Douleur articulaire localisée"},
    "Se puede señalar con un dedo, aparece siempre en el mismo gesto y en el mismo punto "
    "del recorrido, no mejora al calentar. No es normal.": {
        "en": "You can point to it with one finger, it always appears in the same movement and "
              "at the same point of the range, it does not improve with warming up. It is not "
              "normal.",
        "fr": "On peut la montrer du doigt, elle apparaît toujours sur le même geste et au "
              "même point de l'amplitude, elle ne s'améliore pas à l'échauffement. Ce n'est "
              "pas normal."},

    "Dolor que crece sesión a sesión": {
        "en": "Pain that grows session by session",
        "fr": "Douleur qui grandit de séance en séance"},
    "Empieza al final del entrenamiento, luego al principio, luego en la vida diaria. Es el "
    "guion clásico de una lesión por sobreuso, y cuanto antes se corta, menos cuesta.": {
        "en": "It starts at the end of the session, then at the beginning, then in daily life. "
              "It is the classic script of an overuse injury, and the sooner it is cut short, "
              "the less it costs.",
        "fr": "Elle commence à la fin de l'entraînement, puis au début, puis dans la vie "
              "quotidienne. C'est le scénario classique d'une blessure de surmenage, et plus "
              "tôt on la coupe, moins elle coûte."},

    "Qué hacer con cada uno": {
        "en": "What to do with each one", "fr": "Que faire de chacune"},

    "Molestia muscular: seguir, moverse suave y no medir la calidad de una sesión por "
    "cuánto duele después.": {
        "en": "Muscular discomfort: carry on, move gently and do not measure the quality of a "
              "session by how much it hurts afterwards.",
        "fr": "Gêne musculaire : continuer, bouger doucement et ne pas mesurer la qualité "
              "d'une séance à ce qu'elle fait mal ensuite."},

    "Dolor en un gesto concreto: cambiar el gesto, no abandonar el patrón. Si duele el "
    "press de banca, prueba con mancuernas o con otro ángulo; casi siempre hay una "
    "variante que no duele, y seguir entrenando el patrón es mejor que dejarlo.": {
        "en": "Pain in a particular movement: change the movement, do not abandon the pattern. "
              "If the bench press hurts, try dumbbells or a different angle; there is almost "
              "always a variant that does not hurt, and carrying on training the pattern is "
              "better than dropping it.",
        "fr": "Douleur sur un geste précis : changer le geste, pas abandonner le schéma. Si le "
              "développé couché fait mal, essayez les haltères ou un autre angle ; il existe "
              "presque toujours une variante indolore, et continuer d'entraîner le schéma vaut "
              "mieux que de le laisser tomber."},

    "Dolor que crece: reducir la carga de ese patrón un escalón grande durante dos "
    "semanas, mantener el resto y observar. Si en dos semanas no mejora, consulta.": {
        "en": "Pain that grows: reduce the load of that pattern by one large step for two "
              "weeks, keep the rest and watch. If it has not improved in two weeks, seek "
              "advice.",
        "fr": "Douleur qui grandit : réduire la charge de ce schéma d'un grand palier pendant "
              "deux semaines, garder le reste et observer. Si en deux semaines cela ne "
              "s'améliore pas, consultez."},

    "Cualquier dolor con hinchazón, pérdida de fuerza súbita, bloqueo articular, hormigueo "
    "o pérdida de sensibilidad: consulta directamente y sin fase de prueba.": {
        "en": "Any pain with swelling, sudden loss of strength, a locked joint, tingling or "
              "loss of sensation: seek advice straight away and with no trial phase.",
        "fr": "Toute douleur avec gonflement, perte de force soudaine, blocage articulaire, "
              "fourmillements ou perte de sensibilité : consultez directement et sans phase "
              "d'essai."},

    "Y las señales que paran una sesión en el acto": {
        "en": "And the signs that stop a session on the spot",
        "fr": "Et les signaux qui arrêtent une séance sur-le-champ"},

    "Dolor u opresión en el pecho, o dolor que irradia al brazo, al cuello o a la "
    "mandíbula.": {
        "en": "Pain or tightness in the chest, or pain radiating to the arm, the neck or the "
              "jaw.",
        "fr": "Douleur ou oppression dans la poitrine, ou douleur qui irradie vers le bras, le "
              "cou ou la mâchoire."},
    "Falta de aire desproporcionada al esfuerzo que estás haciendo.": {
        "en": "Breathlessness out of proportion to the effort you are making.",
        "fr": "Essoufflement disproportionné par rapport à l'effort que vous fournissez."},
    "Mareo, visión borrosa, palpitaciones irregulares o sensación de desmayo.": {
        "en": "Dizziness, blurred vision, irregular palpitations or a feeling of fainting.",
        "fr": "Vertige, vision floue, palpitations irrégulières ou sensation d'évanouissement."},
    "Dolor de cabeza súbito e intenso durante un esfuerzo.": {
        "en": "A sudden, intense headache during an effort.",
        "fr": "Mal de tête soudain et intense pendant un effort."},
    "Orina de color oscuro tras una sesión inusualmente dura, sobre todo si va con dolor "
    "muscular desproporcionado e hinchazón.": {
        "en": "Dark-coloured urine after an unusually hard session, especially if it comes "
              "with disproportionate muscle pain and swelling.",
        "fr": "Urines de couleur foncée après une séance inhabituellement dure, surtout si "
              "elles s'accompagnent d'une douleur musculaire disproportionnée et d'un "
              "gonflement."},

    "Estas cinco no son «escuchar al cuerpo»: son motivo de atención médica el mismo día. "
    "Ninguna sesión de ningún plan de ningún libro merece la duda, y esta es la página que "
    "conviene recordar de todo el volumen.": {
        "en": "These five are not «listening to your body»: they are grounds for medical "
              "attention the same day. No session of any plan in any book is worth the doubt, "
              "and this is the page worth remembering out of the whole volume.",
        "fr": "Ces cinq-là ne relèvent pas de « l'écoute du corps » : ce sont des motifs de "
              "prise en charge médicale le jour même. Aucune séance d'aucun plan d'aucun livre "
              "ne vaut le doute, et voici la page qu'il faut retenir de tout le volume."},

    "La regla de las setenta y dos horas": {
        "en": "The seventy-two-hour rule", "fr": "La règle des soixante-douze heures"},

    "Si algo duele igual o peor tres días después de haber reducido la carga, ha dejado de "
    "ser un asunto de programación. Lo que sigue no es elegir otro ejercicio: es que "
    "alguien te vea.": {
        "en": "If something hurts the same or worse three days after you reduced the load, it "
              "has stopped being a matter of programming. What comes next is not choosing "
              "another exercise: it is having someone examine you.",
        "fr": "Si quelque chose fait aussi mal ou pire trois jours après avoir réduit la "
              "charge, ce n'est plus une affaire de programmation. La suite n'est pas de "
              "choisir un autre exercice : c'est que quelqu'un vous examine."},

    # ── La ecuación del levantamiento ──────────────────────────────────────
    "Existe una ecuación oficial que calcula cuánto peso es razonable levantar en una "
    "situación concreta. La publicó el instituto nacional de seguridad y salud laboral de "
    "Estados Unidos, se usa en inspección de trabajo en medio mundo, es de acceso libre, y "
    "prácticamente nadie que entrene la ha visto.": {
        "en": "There is an official equation that calculates how much weight it is reasonable "
              "to lift in a particular situation. It was published by the United States "
              "national institute for occupational safety and health, it is used in workplace "
              "inspection across half the world, it is freely available, and practically "
              "nobody who trains has ever seen it.",
        "fr": "Il existe une équation officielle qui calcule quel poids il est raisonnable de "
              "soulever dans une situation donnée. Elle a été publiée par l'institut national "
              "de sécurité et de santé au travail des États-Unis, elle sert à l'inspection du "
              "travail dans la moitié du monde, elle est en libre accès, et pratiquement "
              "personne qui s'entraîne ne l'a vue."},

    '<span class="fig-n">El peso recomendado y los seis factores que lo reducen</span> Se '
    "parte de una carga constante de 23 kilogramos en condiciones ideales y se multiplica "
    "por seis factores que valen entre cero y uno. Ningún factor puede mejorar el "
    "resultado: solo reducirlo. El que más penaliza, con diferencia, es la distancia "
    "horizontal de la carga al cuerpo.": {
        "en": '<span class="fig-n">The recommended weight and the six factors that reduce '
              "it</span> You start from a constant load of 23 kilograms under ideal "
              "conditions and multiply by six factors valued between zero and one. No factor "
              "can improve the result: only reduce it. The one that penalises most, by a wide "
              "margin, is the horizontal distance of the load from the body.",
        "fr": '<span class="fig-n">Le poids recommandé et les six facteurs qui le '
              "réduisent</span> On part d'une charge constante de 23 kilogrammes dans des "
              "conditions idéales et on multiplie par six facteurs qui valent entre zéro et "
              "un. Aucun facteur ne peut améliorer le résultat : seulement le réduire. Celui "
              "qui pénalise le plus, et de loin, est la distance horizontale de la charge au "
              "corps."},

    "El peso recomendado se obtiene multiplicando los 23 kg por seis factores que valen "
    "entre 0 y 1. Cada condición mala reduce el resultado, y por eso el mismo peso es "
    "seguro pegado al cuerpo y no lo es con los brazos estirados.": {
        "en": "The recommended weight is obtained by multiplying the 23 kg by six factors "
              "valued between 0 and 1. Each poor condition reduces the result, and that is why "
              "the same weight is safe held against the body and is not safe at arm's length.",
        "fr": "Le poids recommandé s'obtient en multipliant les 23 kg par six facteurs qui "
              "valent entre 0 et 1. Chaque mauvaise condition réduit le résultat, et c'est "
              "pourquoi le même poids est sûr collé au corps et ne l'est pas bras tendus."},

    "Los seis factores": {"en": "The six factors", "fr": "Les six facteurs"},

    "HM · Horizontal": {"en": "HM · Horizontal", "fr": "HM · Horizontal"},
    "Distancia de la carga al cuerpo. Es el factor que más penaliza: alejar la carga la "
    "multiplica": {
        "en": "Distance of the load from the body. It is the factor that penalises most: "
              "moving the load away multiplies it",
        "fr": "Distance de la charge au corps. C'est le facteur qui pénalise le plus : "
              "éloigner la charge la multiplie"},

    "VM · Vertical": {"en": "VM · Vertical", "fr": "VM · Vertical"},
    "DM · Distancia": {"en": "DM · Distance", "fr": "DM · Distance"},
    "AM · Asimetría": {"en": "AM · Asymmetry", "fr": "AM · Asymétrie"},
    "FM · Frecuencia": {"en": "FM · Frequency", "fr": "FM · Fréquence"},
    "Levantamientos por minuto y duración de la tarea": {
        "en": "Lifts per minute and duration of the task",
        "fr": "Levers par minute et durée de la tâche"},
    "CM · Agarre": {"en": "CM · Coupling", "fr": "CM · Prise"},
}
