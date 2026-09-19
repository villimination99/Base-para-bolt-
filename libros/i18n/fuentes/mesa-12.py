# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · el capítulo de la inocuidad alimentaria
===========================================================
Las temperaturas se quedan en grados centígrados en los tres idiomas. Es la
unidad con la que el generador las calcula y con la que están marcados los
termómetros de cocina que se venden en los tres mercados; convertirlas a
Fahrenheit en la versión inglesa introduciría un redondeo en una cifra que es
un umbral de seguridad, y un umbral redondeado deja de serlo.
"""

T = {
    "Una comida normal con proteína y con hidratos, cuando toque. Si la sesión fue muy dura y "
    "la siguiente es mañana, no hay ninguna prisa. Si hay otra sesión dentro de pocas horas, "
    "entonces sí conviene comer pronto y priorizar los hidratos, porque el depósito de "
    "glucógeno tarda en reponerse y ahí el reloj sí corre.": {
        "en": "A normal meal with protein and carbohydrate, whenever it falls. If the session "
              "was very hard and the next one is tomorrow, there is no hurry at all. If there "
              "is another session in a few hours, then it does pay to eat soon and to "
              "prioritise carbohydrate, because the glycogen store takes time to refill and "
              "there the clock really is running.",
        "fr": "Un repas normal avec des protéines et des glucides, au moment voulu. Si la "
              "séance a été très dure et que la suivante est demain, il n'y a aucune urgence. "
              "S'il y a une autre séance dans quelques heures, alors oui, il vaut mieux manger "
              "tôt et donner la priorité aux glucides, car la réserve de glycogène met du "
              "temps à se reconstituer et là l'horloge tourne pour de bon."},

    "El agua y el peso de después": {
        "en": "Water and the weight afterwards", "fr": "L'eau et le poids d'après"},

    "Perder un kilo durante una sesión larga es agua, no grasa, y conviene reponerla a lo "
    "largo de las horas siguientes con bebida y con comida que lleve sal. Pesarse justo "
    "después de entrenar y celebrar el número es el error de interpretación más común del "
    "gimnasio.": {
        "en": "Losing a kilo during a long session is water, not fat, and it should be "
              "replaced over the following hours with drink and with food that contains salt. "
              "Weighing yourself right after training and celebrating the number is the "
              "commonest misreading in the gym.",
        "fr": "Perdre un kilo pendant une séance longue, c'est de l'eau, pas de la graisse, et "
              "il convient de la reconstituer au cours des heures suivantes avec des boissons "
              "et des aliments salés. Se peser juste après l'entraînement et fêter le chiffre "
              "est l'erreur d'interprétation la plus répandue de la salle."},

    # ── Inocuidad ──────────────────────────────────────────────────────────
    "Este capítulo no aparece en ningún libro de fitness y debería aparecer en todos. Un plan "
    "de alimentación impecable ejecutado con un pollo mal conservado produce en dos días más "
    "perjuicio del que compensan seis meses de macros perfectos. Las cifras que siguen son "
    "públicas, del servicio de inocuidad alimentaria estadounidense, y son sencillas.": {
        "en": "This chapter appears in no fitness book and ought to appear in all of them. An "
              "impeccable eating plan carried out with badly kept chicken produces more harm "
              "in two days than six months of perfect macros make up for. The figures that "
              "follow are public, from the United States food safety service, and they are "
              "simple.",
        "fr": "Ce chapitre ne figure dans aucun livre de fitness et devrait figurer dans tous. "
              "Un plan alimentaire impeccable exécuté avec un poulet mal conservé fait en deux "
              "jours plus de dégâts que six mois de macros parfaits n'en compensent. Les "
              "chiffres qui suivent sont publics, issus du service états-unien de sécurité "
              "alimentaire, et ils sont simples."},

    '<span class="fig-n">La zona de peligro y las temperaturas que hay que superar</span> '
    "Entre los cuatro y los sesenta grados las bacterias se multiplican con rapidez. Las "
    "temperaturas internas seguras están todas por encima de esa franja, y ninguna se alcanza "
    "por color: se miden.": {
        "en": '<span class="fig-n">The danger zone and the temperatures you have to '
              'exceed</span> Between four and sixty degrees bacteria multiply rapidly. The '
              "safe internal temperatures are all above that band, and none of them is reached "
              "by colour: they are measured.",
        "fr": '<span class="fig-n">La zone de danger et les températures qu\'il faut '
              "dépasser</span> Entre quatre et soixante degrés, les bactéries se multiplient "
              "rapidement. Les températures internes sûres sont toutes au-dessus de cette "
              "plage, et aucune ne s'atteint à la couleur : elles se mesurent."},

    "Temperaturas internas seguras": {
        "en": "Safe internal temperatures", "fr": "Températures internes sûres"},

    "74 °C · sin excepción y sin reposo": {
        "en": "74 °C · no exceptions and no resting time",
        "fr": "74 °C · sans exception et sans repos"},
    "74 °C · hasta que humee, no solo templado": {
        "en": "74 °C · until it steams, not merely warm",
        "fr": "74 °C · jusqu'à ce que ça fume, pas seulement tiède"},

    "Carne picada de res, cerdo, cordero": {
        "en": "Minced beef, pork, lamb", "fr": "Viande hachée de bœuf, porc, agneau"},
    "71 °C · más alta que la del corte entero: al picar, la superficie se reparte por dentro": {
        "en": "71 °C · higher than for the whole cut: mincing spreads the surface through the "
              "inside",
        "fr": "71 °C · plus élevée que pour la pièce entière : en hachant, la surface se "
              "répartit à l'intérieur"},
    "71 °C · tortillas cuajadas, quiches, flanes": {
        "en": "71 °C · set omelettes, quiches, custards",
        "fr": "71 °C · omelettes prises, quiches, flans"},

    "Cortes enteros de res, cerdo, cordero": {
        "en": "Whole cuts of beef, pork, lamb",
        "fr": "Pièces entières de bœuf, porc, agneau"},
    "63 °C · más tres minutos de reposo": {
        "en": "63 °C · plus three minutes' resting time",
        "fr": "63 °C · plus trois minutes de repos"},
    "63 °C · o hasta que la carne se separe en láminas": {
        "en": "63 °C · or until the flesh flakes apart",
        "fr": "63 °C · ou jusqu'à ce que la chair se détache en lamelles"},

    "Por qué la carne picada necesita más temperatura que el filete": {
        "en": "Why mince needs a higher temperature than the steak",
        "fr": "Pourquoi la viande hachée exige plus de température que le steak"},

    "Es la pregunta que revela si alguien ha entendido el asunto. En un corte entero, la "
    "contaminación está en la superficie, y la superficie es justamente lo que recibe el calor "
    "directo: por eso un filete poco hecho por dentro puede ser seguro. Al picar la carne, esa "
    "superficie se distribuye por toda la masa, así que el interior necesita alcanzar la "
    "temperatura por sí mismo. Una hamburguesa poco hecha no es lo mismo que un entrecot poco "
    "hecho, y la diferencia no es de gusto.": {
        "en": "It is the question that reveals whether someone has understood the matter. In a "
              "whole cut the contamination is on the surface, and the surface is precisely "
              "what receives the direct heat: that is why a steak that is rare inside can be "
              "safe. When the meat is minced, that surface is distributed throughout the mass, "
              "so the inside needs to reach the temperature by itself. An underdone burger is "
              "not the same thing as an underdone rib steak, and the difference is not one of "
              "taste.",
        "fr": "C'est la question qui révèle si quelqu'un a compris l'affaire. Dans une pièce "
              "entière, la contamination est en surface, et la surface est justement ce qui "
              "reçoit la chaleur directe : c'est pourquoi un steak saignant à cœur peut être "
              "sûr. En hachant la viande, cette surface se répartit dans toute la masse, si "
              "bien que l'intérieur doit atteindre la température par lui-même. Un hamburger "
              "peu cuit n'est pas la même chose qu'une entrecôte peu cuite, et la différence "
              "n'est pas affaire de goût."},

    # ── Los cuatro pasos ───────────────────────────────────────────────────
    "Limpiar": {"en": "Clean", "fr": "Nettoyer"},
    "Manos veinte segundos con jabón, antes y después de tocar crudo. Tablas y superficies "
    "entre alimento y alimento": {
        "en": "Hands for twenty seconds with soap, before and after touching anything raw. "
              "Boards and surfaces between one food and the next",
        "fr": "Les mains vingt secondes au savon, avant et après avoir touché du cru. Planches "
              "et surfaces entre un aliment et le suivant"},

    "Separar": {"en": "Separate", "fr": "Séparer"},
    "Crudo lejos de listo para comer. Tabla distinta para carne cruda, y nunca el plato que "
    "llevó el crudo a la parrilla": {
        "en": "Raw away from ready to eat. A separate board for raw meat, and never the plate "
              "that carried the raw meat to the grill",
        "fr": "Le cru loin du prêt à manger. Une planche à part pour la viande crue, et jamais "
              "l'assiette qui a porté le cru jusqu'au gril"},

    "Cocinar": {"en": "Cook", "fr": "Cuire"},
    "Con termómetro y no con el color. El color de la carne no indica temperatura: hay carne "
    "gris a 60 °C y rosada a 75": {
        "en": "With a thermometer and not by colour. The colour of meat does not indicate "
              "temperature: there is grey meat at 60 °C and pink meat at 75",
        "fr": "Au thermomètre et non à la couleur. La couleur de la viande n'indique pas la "
              "température : il y a de la viande grise à 60 °C et rosée à 75"},

    "A la nevera antes de dos horas. Las porciones grandes, repartidas en recipientes bajos "
    "para que bajen rápido": {
        "en": "Into the fridge within two hours. Large portions divided into shallow "
              "containers so that they come down fast",
        "fr": "Au réfrigérateur avant deux heures. Les grandes quantités réparties dans des "
              "récipients bas pour qu'elles descendent vite"},

    "El paso que más se salta es el cuarto. Dejar enfriar una olla grande sobre la encimera "
    "toda la tarde la mantiene horas dentro de la zona de peligro por pura inercia térmica, "
    "aunque la superficie parezca fría. La solución es repartir en recipientes bajos y "
    "meterlos pronto: enfrían en una fracción del tiempo.": {
        "en": "The step most often skipped is the fourth. Leaving a big pot to cool on the "
              "worktop all afternoon keeps it for hours inside the danger zone through sheer "
              "thermal inertia, even though the surface feels cold. The solution is to divide "
              "it into shallow containers and put them away promptly: they cool in a fraction "
              "of the time.",
        "fr": "L'étape la plus souvent sautée est la quatrième. Laisser refroidir une grande "
              "marmite sur le plan de travail tout l'après-midi la maintient des heures dans "
              "la zone de danger par pure inertie thermique, même si la surface semble froide. "
              "La solution est de répartir dans des récipients bas et de les ranger vite : ils "
              "refroidissent en une fraction du temps."},

    "Los márgenes de tiempo": {
        "en": "The time margins", "fr": "Les marges de temps"},
    "A temperatura ambiente": {
        "en": "At room temperature", "fr": "À température ambiante"},
}
