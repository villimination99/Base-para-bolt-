# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · entrenar a partir de los sesenta y la batería de pruebas
=============================================================================
El capítulo de los adultos mayores tiene un argumento que se puede estropear
al traducir: la recomendación de equilibrio no es un consuelo ni una versión
rebajada del entrenamiento, es una recomendación añadida que las guías dan
solo aquí. La traducción mantiene ese matiz en cada frase, incluida la del
aerobio, donde el listón se adapta y no se cancela.

La cifra de proteína, 0,8 g por kilo, cambia de puntuación por idioma. Y sigue
diciendo, en las tres, que no sale de las tablas de referencia sino de otra
literatura: la advertencia es del autor sobre su propia fuente y no puede
perderse.
"""

T = {
    "Tres días": {"en": "Three days", "fr": "Trois jours"},
    "Diez minutos de escaleras, cuesta o caminata rápida": {
        "en": "Ten minutes of stairs, a hill or brisk walking",
        "fr": "Dix minutes d'escaliers, de côte ou de marche rapide"},
    "Todos los días": {"en": "Every day", "fr": "Tous les jours"},
    "Levantarse cada media hora del asiento. No cuenta para la dosis y cuenta para otra "
    "cosa": {
        "en": "Getting up from your seat every half hour. It does not count towards the dose "
              "and it counts towards something else",
        "fr": "Se lever de son siège toutes les demi-heures. Cela ne compte pas pour la dose "
              "et cela compte pour autre chose"},

    "Esta semana no llega a la recomendación, y va incluida a propósito. La curva del "
    "capítulo dos dice que el salto de cero a esto es el más rentable de toda la gráfica; "
    "el salto de esto a la recomendación completa rinde menos. Un libro honesto tiene que "
    "decir que la versión pequeña vale mucho, porque la alternativa real no suele ser la "
    "versión grande: es nada.": {
        "en": "This week does not reach the recommendation, and it is included on purpose. The "
              "curve in chapter two says the jump from zero to this is the most profitable in "
              "the whole graph; the jump from this to the full recommendation returns less. An "
              "honest book has to say that the small version is worth a great deal, because "
              "the real alternative is usually not the big version: it is nothing.",
        "fr": "Cette semaine n'atteint pas la recommandation, et elle est incluse exprès. La "
              "courbe du chapitre deux dit que le saut de zéro à ceci est le plus rentable de "
              "tout le graphique ; le saut de ceci à la recommandation complète rapporte "
              "moins. Un livre honnête doit dire que la petite version vaut beaucoup, car "
              "l'alternative réelle n'est en général pas la grande version : c'est rien."},

    "Sobre el calentamiento y el estiramiento": {
        "en": "On warming up and stretching",
        "fr": "Sur l'échauffement et les étirements"},

    "Calentar sirve, y sirve sobre todo para rendir mejor en las primeras series: cinco o "
    "diez minutos de movimiento general y unas series ligeras del ejercicio que vas a "
    "hacer. Estirar antes, en cambio, no previene lesiones —la evidencia sobre eso es "
    "bastante mala— y el estiramiento estático prolongado justo antes reduce un poco la "
    "fuerza disponible. Si te gusta estirar, hazlo después o en otro momento del día.": {
        "en": "Warming up works, and it works above all for performing better in the first "
              "sets: five or ten minutes of general movement and a few light sets of the "
              "exercise you are about to do. Stretching beforehand, on the other hand, does "
              "not prevent injuries —the evidence on that is quite poor— and prolonged static "
              "stretching immediately before slightly reduces the strength available. If you "
              "like stretching, do it afterwards or at another time of day.",
        "fr": "S'échauffer sert, et cela sert surtout à mieux rendre dans les premières "
              "séries : cinq ou dix minutes de mouvement général et quelques séries légères de "
              "l'exercice que vous allez faire. S'étirer avant, en revanche, ne prévient pas "
              "les blessures —les preuves à ce sujet sont assez mauvaises— et l'étirement "
              "statique prolongé juste avant réduit un peu la force disponible. Si vous aimez "
              "vous étirer, faites-le après ou à un autre moment de la journée."},

    # ── Entrenar a partir de los sesenta ───────────────────────────────────
    "Las guías de actividad física tienen una sección específica para adultos mayores, y "
    "contiene la única recomendación de todo el documento que no aparece para el resto de "
    "la población. Merece un capítulo porque casi nadie la conoce y porque es la que más "
    "años de autonomía compra.": {
        "en": "The physical activity guidelines have a specific section for older adults, and "
              "it contains the only recommendation in the whole document that does not appear "
              "for the rest of the population. It deserves a chapter because almost nobody "
              "knows about it and because it is the one that buys the most years of "
              "independence.",
        "fr": "Les recommandations d'activité physique comportent une section propre aux "
              "adultes âgés, et elle contient la seule recommandation de tout le document qui "
              "n'apparaît pas pour le reste de la population. Elle mérite un chapitre parce "
              "que presque personne ne la connaît et parce que c'est celle qui achète le plus "
              "d'années d'autonomie."},

    "Lo que añaden las guías para adultos mayores": {
        "en": "What the guidelines add for older adults",
        "fr": "Ce que les recommandations ajoutent pour les adultes âgés"},

    "Equilibrio": {"en": "Balance", "fr": "Équilibre"},
    "Trabajo de equilibrio como componente propio, además del aerobio y de la fuerza. Es "
    "la recomendación adicional y va dirigida a lo que de verdad quita autonomía, que son "
    "las caídas.": {
        "en": "Balance work as a component in its own right, on top of aerobic work and "
              "strength. It is the additional recommendation and it is aimed at what really "
              "takes independence away, which is falls.",
        "fr": "Le travail d'équilibre comme composante à part entière, en plus de l'aérobie et "
              "de la force. C'est la recommandation supplémentaire et elle vise ce qui ôte "
              "vraiment l'autonomie : les chutes."},

    "Igual de necesaria que a cualquier edad, y más urgente: la pérdida de masa muscular "
    "con los años es lo que convierte una caída en una fractura y una fractura en una vida "
    "distinta.": {
        "en": "Just as necessary as at any age, and more urgent: the loss of muscle mass over "
              "the years is what turns a fall into a fracture and a fracture into a different "
              "life.",
        "fr": "Aussi nécessaire qu'à tout âge, et plus urgente : la perte de masse musculaire "
              "avec les années est ce qui transforme une chute en fracture et une fracture en "
              "une autre vie."},

    "Aerobio": {"en": "Aerobic work", "fr": "Aérobie"},
    "La misma dosis, con la coletilla de que quien no pueda alcanzarla debe ser tan activo "
    "como su condición le permita. El listón se adapta; no se cancela.": {
        "en": "The same dose, with the rider that anyone unable to reach it should be as "
              "active as their condition allows. The bar adapts; it is not cancelled.",
        "fr": "La même dose, avec la mention que qui ne peut pas l'atteindre doit être aussi "
              "actif que son état le permet. La barre s'adapte ; elle ne s'annule pas."},

    "Adaptación": {"en": "Adaptation", "fr": "Adaptation"},
    "Ajustar el esfuerzo al nivel de forma, con especial atención a las condiciones "
    "crónicas. Adaptar no es rebajar a cero.": {
        "en": "Adjusting the effort to the level of fitness, with particular attention to "
              "chronic conditions. Adapting is not lowering to zero.",
        "fr": "Ajuster l'effort au niveau de forme, avec une attention particulière aux "
              "affections chroniques. Adapter n'est pas ramener à zéro."},

    "El equilibrio se entrena, y es barato": {
        "en": "Balance can be trained, and it is cheap",
        "fr": "L'équilibre s'entraîne, et c'est bon marché"},

    "Sostenerse sobre una pierna mientras te lavas los dientes. Dos minutos al día que no "
    "ocupan tiempo nuevo.": {
        "en": "Standing on one leg while you brush your teeth. Two minutes a day that take up "
              "no new time.",
        "fr": "Tenir sur une jambe pendant que vous vous brossez les dents. Deux minutes par "
              "jour qui n'occupent aucun temps nouveau."},
    "Caminar en línea, talón contra punta, unos metros por el pasillo.": {
        "en": "Walking in a line, heel to toe, a few metres down the corridor.",
        "fr": "Marcher en ligne, talon contre pointe, sur quelques mètres dans le couloir."},
    "Levantarse de una silla sin usar los brazos, varias veces seguidas. Es a la vez "
    "fuerza y equilibrio, y es la prueba que mejor predice la autonomía a diez años.": {
        "en": "Getting up from a chair without using your arms, several times in a row. It is "
              "strength and balance at once, and it is the test that best predicts "
              "independence ten years out.",
        "fr": "Se lever d'une chaise sans se servir des bras, plusieurs fois de suite. C'est à "
              "la fois de la force et de l'équilibre, et c'est le test qui prédit le mieux "
              "l'autonomie à dix ans."},
    "Cambios de dirección y de superficie al andar: hierba, cuesta, arena. El equilibrio se "
    "entrena obligándolo a corregir.": {
        "en": "Changes of direction and of surface while walking: grass, a slope, sand. "
              "Balance is trained by forcing it to correct.",
        "fr": "Des changements de direction et de surface en marchant : herbe, côte, sable. "
              "L'équilibre s'entraîne en l'obligeant à corriger."},
    "Todo esto se hace con un apoyo cerca al principio. La progresión es quitar el apoyo, "
    "no empezar sin él.": {
        "en": "All of this is done with a support nearby at first. The progression is removing "
              "the support, not starting without it.",
        "fr": "Tout cela se fait avec un appui à portée au début. La progression consiste à "
              "retirer l'appui, pas à commencer sans lui."},

    "La pérdida de músculo con la edad, en su tamaño real": {
        "en": "The loss of muscle with age, at its real size",
        "fr": "La perte de muscle avec l'âge, à sa taille réelle"},

    "A partir de la mediana edad se pierde masa muscular de forma continua si no se hace "
    "nada al respecto, y la fuerza se pierde todavía más deprisa que la masa. Ese proceso "
    "no es una fatalidad biológica que haya que aceptar: responde al entrenamiento de "
    "fuerza a cualquier edad, y hay programas documentados que producen ganancias en "
    "personas de más de ochenta años.": {
        "en": "From middle age onwards, muscle mass is lost continuously if nothing is done "
              "about it, and strength is lost faster still than mass. That process is not a "
              "biological fate to be accepted: it responds to strength training at any age, "
              "and there are documented programmes producing gains in people over eighty.",
        "fr": "À partir du milieu de la vie, on perd de la masse musculaire en continu si "
              "l'on n'y fait rien, et la force se perd encore plus vite que la masse. Ce "
              "processus n'est pas une fatalité biologique à accepter : il répond à "
              "l'entraînement de force à tout âge, et il existe des programmes documentés qui "
              "produisent des gains chez des personnes de plus de quatre-vingts ans."},

    "El error más común es el contrario del que se supone: no es entrenar demasiado "
    "fuerte, es entrenar demasiado suave. Un peso que se puede levantar treinta veces sin "
    "esfuerzo no produce adaptación a ninguna edad. La progresión tiene que existir también "
    "aquí, con más cuidado en la técnica y más margen en el descanso, pero tiene que "
    "existir.": {
        "en": "The commonest mistake is the opposite of the assumed one: it is not training "
              "too hard, it is training too gently. A weight that can be lifted thirty times "
              "without effort produces no adaptation at any age. Progression has to exist here "
              "too, with more care over technique and more margin in the rest, but it has to "
              "exist.",
        "fr": "L'erreur la plus courante est l'inverse de celle qu'on suppose : ce n'est pas "
              "de s'entraîner trop fort, c'est de s'entraîner trop doucement. Un poids que "
              "l'on peut soulever trente fois sans effort ne produit aucune adaptation, à "
              "aucun âge. La progression doit exister ici aussi, avec plus de soin sur la "
              "technique et plus de marge sur le repos, mais elle doit exister."},

    "La proteína en esta etapa": {
        "en": "Protein at this stage", "fr": "Les protéines à cette étape"},

    "El suelo poblacional de 0,8 gramos por kilo se queda corto para frenar la pérdida de "
    "masa a partir de cierta edad, y la literatura geriátrica maneja cifras claramente "
    "mayores. Esa cifra no sale de las tablas de referencia y lo digo: sale de otra "
    "literatura. Es una conversación que merece tenerse con un profesional, sobre todo si "
    "hay función renal comprometida, donde la respuesta puede ser la contraria.": {
        "en": "The population floor of 0.8 grams per kilo falls short for holding back the "
              "loss of mass beyond a certain age, and the geriatric literature works with "
              "clearly higher figures. That figure does not come from the reference tables and "
              "I say so: it comes from a different literature. It is a conversation worth "
              "having with a professional, particularly where kidney function is compromised, "
              "in which case the answer may be the opposite.",
        "fr": "Le plancher de population de 0,8 gramme par kilo est insuffisant pour freiner "
              "la perte de masse à partir d'un certain âge, et la littérature gériatrique "
              "manie des chiffres nettement plus élevés. Ce chiffre ne sort pas des tables de "
              "référence et je le dis : il sort d'une autre littérature. C'est une "
              "conversation qui mérite d'être tenue avec un professionnel, surtout en cas de "
              "fonction rénale altérée, où la réponse peut être l'inverse."},

    # ── La batería de pruebas ──────────────────────────────────────────────
    "El peso corporal oscila varios kilos en cuestión de días por agua, sal, glucógeno y "
    "contenido intestinal, así que medir el progreso con la báscula es reaccionar a ruido. "
    "Medirlo con pruebas físicas es mucho mejor, y existe una batería completa, descrita "
    "al detalle y de acceso libre, que el Ejército de Estados Unidos publica entera.": {
        "en": "Body weight swings by several kilos within days through water, salt, glycogen "
              "and gut contents, so measuring progress with the scales is reacting to noise. "
              "Measuring it with physical tests is far better, and there is a complete "
              "battery, described in detail and freely available, which the United States Army "
              "publishes in full.",
        "fr": "Le poids du corps oscille de plusieurs kilos en quelques jours à cause de "
              "l'eau, du sel, du glycogène et du contenu intestinal, si bien que mesurer le "
              "progrès à la balance revient à réagir au bruit. Le mesurer par des épreuves "
              "physiques est bien meilleur, et il existe une batterie complète, décrite en "
              "détail et en libre accès, que l'armée des États-Unis publie intégralement."},

    '<span class="fig-n">Seis pruebas, seis cualidades distintas</span> La batería está '
    "construida para que ninguna prueba se pueda compensar con otra: hay un mínimo por "
    "prueba. Esa regla es la lección transferible, aunque nunca vayas a hacer ninguna de "
    "las seis.": {
        "en": '<span class="fig-n">Six tests, six different qualities</span> The battery is '
              "built so that no test can be offset by another: there is a minimum for each "
              "one. That rule is the transferable lesson, even if you never do any of the six.",
        "fr": '<span class="fig-n">Six épreuves, six qualités différentes</span> La batterie '
              "est construite pour qu'aucune épreuve ne puisse être compensée par une autre : "
              "il y a un minimum par épreuve. Cette règle est la leçon transférable, même si "
              "vous ne faites jamais aucune des six."},

    "Qué mide cada una": {"en": "What each one measures", "fr": "Ce que mesure chacune"},
}
