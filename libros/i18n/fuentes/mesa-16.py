# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · el cuaderno de cuatro semanas, los límites y el glosario
============================================================================
Las tres letras del cuaderno de la primera semana —C de cocinado, F de un
paquete, R de restaurante— tienen que seguir siendo tres letras distintas en
cada idioma y seguir queriendo decir lo mismo, porque el lector las escribe a
mano al margen de su cuaderno. En inglés salen C, P y R; en francés, C, P y R
también. Traducir la frase y dejar las letras españolas dejaría al lector
marcando una «F» que no es la inicial de nada.

Las siglas del glosario —AI, AMDR, CDRR, DFE, EAR, NE, RAE, RDA, UL— no se
tocan: son las que figuran en las tablas que el capítulo de fuentes enseña a
consultar. Lo que se traduce es su desarrollo.
"""

T = {
    # ── El cuaderno ────────────────────────────────────────────────────────
    "Cuatro semanas, y no una dieta. El cuaderno no impone qué comer: averigua qué comes, que "
    "es información que casi nadie tiene sobre sí mismo y que ninguna aplicación da porque las "
    "aplicaciones piden lo que creemos comer.": {
        "en": "Four weeks, and not a diet. The notebook does not impose what to eat: it finds "
              "out what you eat, which is information almost nobody has about themselves and "
              "which no app supplies, because apps ask for what we believe we eat.",
        "fr": "Quatre semaines, et non un régime. Le carnet n'impose pas quoi manger : il "
              "découvre ce que vous mangez, une information que presque personne n'a sur "
              "soi-même et qu'aucune application ne donne, parce que les applications "
              "demandent ce que nous croyons manger."},

    "Semana 1 · Registrar sin cambiar nada": {
        "en": "Week 1 · Record without changing anything",
        "fr": "Semaine 1 · Noter sans rien changer"},

    "Anota lo que comes, sin pesar y sin juzgar. Alimento y tamaño aproximado en medidas de "
    "mano. Sin cifras.": {
        "en": "Write down what you eat, without weighing and without judging. Food and "
              "approximate size in hand measures. No figures.",
        "fr": "Notez ce que vous mangez, sans peser et sans juger. L'aliment et sa taille "
              "approximative en mesures de main. Aucun chiffre."},

    "Marca cada comida con una de tres letras: C si la cocinaste, F si vino de un paquete, R "
    "si fue en un restaurante o similar.": {
        "en": "Mark each meal with one of three letters: C if you cooked it, P if it came out "
              "of a packet, R if it was in a restaurant or similar.",
        "fr": "Marquez chaque repas d'une de ces trois lettres : C si vous l'avez cuisiné, P "
              "s'il sortait d'un paquet, R si c'était au restaurant ou assimilé."},

    "Al final de la semana cuenta las letras. Ese reparto explica tu ingesta de sodio, de "
    "azúcares añadidos y de fibra mejor que cualquier cálculo.": {
        "en": "At the end of the week count the letters. That split explains your intake of "
              "sodium, added sugars and fibre better than any calculation.",
        "fr": "À la fin de la semaine, comptez les lettres. Cette répartition explique votre "
              "apport en sodium, en sucres ajoutés et en fibres mieux que n'importe quel "
              "calcul."},

    "No cambies nada esta semana. La medida se contamina si la intervención empieza antes.": {
        "en": "Change nothing this week. The measurement is contaminated if the intervention "
              "starts first.",
        "fr": "Ne changez rien cette semaine. La mesure est faussée si l'intervention commence "
              "avant."},

    "Semana 2 · Las tres casillas": {
        "en": "Week 2 · The three boxes", "fr": "Semaine 2 · Les trois cases"},

    "Cuenta cuántas comidas de la semana llevaron verdura. Objetivo de referencia: la "
    "mayoría.": {
        "en": "Count how many meals in the week contained vegetables. Reference target: most "
              "of them.",
        "fr": "Comptez combien de repas de la semaine comportaient des légumes. Objectif de "
              "référence : la plupart."},

    "Cuenta cuántas llevaron una fuente clara de proteína del tamaño de tu palma.": {
        "en": "Count how many contained a clear protein source the size of your palm.",
        "fr": "Comptez combien comportaient une source claire de protéines de la taille de "
              "votre paume."},

    "Cuenta cuántos días tomaste legumbre, fruto seco o semilla.": {
        "en": "Count how many days you had pulses, nuts or seeds.",
        "fr": "Comptez combien de jours vous avez pris des légumineuses, des fruits à coque ou "
              "des graines."},

    "Añade UNA de las tres donde falte, la que menos esfuerzo te cueste. Una, no las tres.": {
        "en": "Add ONE of the three where it is missing, whichever costs you least effort. "
              "One, not all three.",
        "fr": "Ajoutez UNE des trois là où elle manque, celle qui vous coûte le moins d'effort. "
              "Une, pas les trois."},

    "Semana 3 · Los huecos probables": {
        "en": "Week 3 · The likely gaps", "fr": "Semaine 3 · Les manques probables"},

    "Repasa la lista de categorías del capítulo del plato y marca las que no aparecen nunca en "
    "tu semana.": {
        "en": "Go back over the list of categories in the plate chapter and mark the ones that "
              "never appear in your week.",
        "fr": "Reprenez la liste des catégories du chapitre de l'assiette et cochez celles qui "
              "n'apparaissent jamais dans votre semaine."},

    "Para cada hueco, mira en la tabla de los diecinueve qué nutrientes cubría esa categoría.": {
        "en": "For each gap, look in the table of nineteen to see which nutrients that "
              "category covered.",
        "fr": "Pour chaque manque, regardez dans le tableau des dix-neuf quels nutriments cette "
              "catégorie couvrait."},

    "Si el hueco es pescado azul, lácteo o alimento de origen animal, ahí es donde tiene "
    "sentido plantear un análisis o una consulta, no un bote elegido por internet.": {
        "en": "If the gap is oily fish, dairy or food of animal origin, that is where it makes "
              "sense to consider a blood test or a consultation, not a tub chosen online.",
        "fr": "Si le manque est le poisson gras, les produits laitiers ou les aliments "
              "d'origine animale, c'est là qu'il est sensé d'envisager une analyse ou une "
              "consultation, pas un pot choisi sur internet."},

    "Escribe la pregunta que le harías a un profesional. Una frase. Esa frase es el producto "
    "de tres semanas de cuaderno.": {
        "en": "Write down the question you would ask a professional. One sentence. That "
              "sentence is the product of three weeks of notebook.",
        "fr": "Écrivez la question que vous poseriez à un professionnel. Une phrase. Cette "
              "phrase est le produit de trois semaines de carnet."},

    "Semana 4 · La auditoría del botiquín": {
        "en": "Week 4 · Auditing the medicine cabinet",
        "fr": "Semaine 4 · L'audit de l'armoire à pharmacie"},

    "Junta todos los suplementos y alimentos fortificados que tomas y escribe, nutriente por "
    "nutriente, cuánto suman al día.": {
        "en": "Gather every supplement and fortified food you take and write down, nutrient by "
              "nutrient, how much they add up to per day.",
        "fr": "Rassemblez tous les compléments et aliments enrichis que vous prenez et notez, "
              "nutriment par nutriment, à combien ils s'élèvent par jour."},

    "Compara cada suma con la columna del techo de la tabla de los diecinueve. Presta atención "
    "especial a vitamina B6, vitamina A preformada, hierro, selenio, zinc y magnesio en forma "
    "de sales.": {
        "en": "Compare each total with the ceiling column in the table of nineteen. Pay "
              "particular attention to vitamin B6, preformed vitamin A, iron, selenium, zinc "
              "and magnesium in salt form.",
        "fr": "Comparez chaque total à la colonne du plafond du tableau des dix-neuf. Faites "
              "particulièrement attention à la vitamine B6, à la vitamine A préformée, au fer, "
              "au sélénium, au zinc et au magnésium sous forme de sels."},

    "Cualquier suma que pase del techo, o que se acerque, va a la consulta. No se ajusta a "
    "ojo.": {
        "en": "Any total that goes over the ceiling, or comes close, goes to the consultation. "
              "It is not adjusted by eye.",
        "fr": "Tout total qui dépasse le plafond, ou qui s'en approche, part en consultation. "
              "Cela ne se règle pas à l'œil."},

    "Lo que no sepas justificar con un motivo concreto —una carencia documentada, una dieta "
    "que excluye una categoría, una etapa de la vida— es candidato a desaparecer. La mayoría "
    "de los botiquines pierden la mitad en este paso y nadie nota nada.": {
        "en": "Anything you cannot justify with a specific reason —a documented deficiency, a "
              "diet that excludes a category, a stage of life— is a candidate for "
              "disappearing. Most medicine cabinets lose half at this step and nobody notices "
              "a thing.",
        "fr": "Tout ce que vous ne savez pas justifier par un motif précis —une carence "
              "documentée, un régime qui exclut une catégorie, une étape de la vie— est "
              "candidat à disparaître. La plupart des armoires à pharmacie perdent la moitié à "
              "cette étape et personne ne remarque quoi que ce soit."},

    "No adelgaza. Lo que hace es convertir «creo que como bastante bien» en una descripción "
    "con datos, y de paso ahorrar dinero en productos que no hacían nada. Si al terminar las "
    "cuatro semanas tienes una frase clara para llevarle a un profesional y un botiquín más "
    "pequeño, el cuaderno cumplió.": {
        "en": "It does not make you thinner. What it does is turn «I think I eat pretty well» "
              "into a description with data, and along the way save money on products that "
              "were doing nothing. If at the end of the four weeks you have a clear sentence "
              "to take to a professional and a smaller medicine cabinet, the notebook did its "
              "job.",
        "fr": "Il ne fait pas maigrir. Ce qu'il fait, c'est transformer « je crois que je mange "
              "plutôt bien » en une description avec des données, et au passage économiser de "
              "l'argent sur des produits qui ne faisaient rien. Si au bout des quatre semaines "
              "vous avez une phrase claire à porter à un professionnel et une armoire à "
              "pharmacie plus petite, le carnet a rempli son office."},

    # ── Los límites ────────────────────────────────────────────────────────
    "Último capítulo, y el que fija los límites. Hay preguntas que una tabla de referencia no "
    "puede contestar, y presionarla para que lo haga es la forma en que la nutrición "
    "divulgativa se convierte en daño.": {
        "en": "Last chapter, and the one that sets the limits. There are questions a reference "
              "table cannot answer, and pressing it to do so is the way popular nutrition "
              "turns into harm.",
        "fr": "Dernier chapitre, et celui qui fixe les limites. Il existe des questions "
              "auxquelles un tableau de référence ne peut pas répondre, et le forcer à le "
              "faire est la façon dont la nutrition de vulgarisation se transforme en "
              "dommage."},

    "Cinco preguntas para las que este libro no sirve": {
        "en": "Five questions this book is no use for",
        "fr": "Cinq questions pour lesquelles ce livre ne sert à rien"},

    "«¿Cuánto tengo que comer para adelgazar X kilos en Y semanas?». Este libro trata de "
    "suficiencia de nutrientes, no de balance energético individual, y desconfía por principio "
    "de cualquier cifra prometida con plazo.": {
        "en": "«How much do I have to eat to lose X kilos in Y weeks?». This book is about "
              "nutrient sufficiency, not individual energy balance, and it distrusts on "
              "principle any figure promised with a deadline.",
        "fr": "« Combien dois-je manger pour perdre X kilos en Y semaines ? ». Ce livre traite "
              "de la suffisance en nutriments, pas du bilan énergétique individuel, et il se "
              "méfie par principe de tout chiffre promis avec un délai."},

    "«¿Qué tomo para mi enfermedad?». Ninguna cifra de aquí está establecida para condiciones "
    "clínicas, y varias se invierten en presencia de insuficiencia renal, hepática o "
    "cardíaca.": {
        "en": "«What do I take for my illness?». No figure here is established for clinical "
              "conditions, and several reverse in the presence of renal, hepatic or cardiac "
              "insufficiency.",
        "fr": "« Que dois-je prendre pour ma maladie ? ». Aucun chiffre d'ici n'est établi pour "
              "des situations cliniques, et plusieurs s'inversent en présence d'une "
              "insuffisance rénale, hépatique ou cardiaque."},

    "«¿Vale esto en el embarazo?». No. Las referencias del embarazo y la lactancia son otras, "
    "algunas bastante distintas, y hay al menos un nutriente donde el margen es crítico. Esa "
    "etapa se lleva con seguimiento.": {
        "en": "«Does this hold in pregnancy?». No. The references for pregnancy and "
              "breastfeeding are different ones, some of them considerably so, and there is at "
              "least one nutrient where the margin is critical. That stage is handled with "
              "supervision.",
        "fr": "« Est-ce valable pendant la grossesse ? ». Non. Les références de la grossesse "
              "et de l'allaitement sont différentes, certaines nettement, et il existe au "
              "moins un nutriment dont la marge est critique. Cette étape se mène avec un "
              "suivi."},

    "«¿Sirve para mi hijo?». No. Toda la tabla es de adultos. Las referencias pediátricas "
    "cambian con la edad y con el peso, y extrapolar por regla de tres es un error.": {
        "en": "«Is it any use for my child?». No. The whole table is for adults. Paediatric "
              "references change with age and with weight, and extrapolating by simple "
              "proportion is a mistake.",
        "fr": "« Est-ce valable pour mon enfant ? ». Non. Tout le tableau concerne des "
              "adultes. Les références pédiatriques changent avec l'âge et avec le poids, et "
              "extrapoler par règle de trois est une erreur."},

    "«¿Estoy deficiente?». Eso se contesta con una analítica y un contexto clínico, nunca con "
    "un registro de comida. Ninguna app tiene esa información.": {
        "en": "«Am I deficient?». That is answered with a blood test and a clinical context, "
              "never with a food diary. No app has that information.",
        "fr": "« Suis-je carencé ? ». Cela se répond avec une analyse et un contexte clinique, "
              "jamais avec un carnet alimentaire. Aucune application n'a cette information."},

    "Tres señales de que hay que consultar y no leer": {
        "en": "Three signs that you should consult and not read",
        "fr": "Trois signes qu'il faut consulter et non lire"},

    "Pérdida de peso sin proponérselo, cansancio persistente, caída de pelo marcada o "
    "cualquier cambio digestivo que dure semanas.": {
        "en": "Unintended weight loss, persistent tiredness, marked hair loss or any digestive "
              "change lasting weeks.",
        "fr": "Une perte de poids non voulue, une fatigue persistante, une chute de cheveux "
              "marquée ou tout changement digestif qui dure des semaines."},

    "Cualquier plan que te haga excluir un grupo entero de alimentos durante más de unas "
    "semanas, sea el que sea y por buena que suene la razón.": {
        "en": "Any plan that has you exclude a whole food group for more than a few weeks, "
              "whichever it is and however good the reason sounds.",
        "fr": "Tout plan qui vous fait exclure un groupe entier d'aliments pendant plus de "
              "quelques semaines, quel qu'il soit et si bonne que paraisse la raison."},

    "Cualquier suplemento que tomes sin poder explicar en una frase para qué es y cómo sabrás "
    "si funcionó.": {
        "en": "Any supplement you take without being able to explain in one sentence what it "
              "is for and how you will know whether it worked.",
        "fr": "Tout complément que vous prenez sans pouvoir expliquer en une phrase à quoi il "
              "sert et comment vous saurez s'il a fonctionné."},

    # ── Glosario ───────────────────────────────────────────────────────────
    "AI · Ingesta adecuada": {
        "en": "AI · Adequate intake", "fr": "AI · Apport suffisant"},
    "Valor de referencia usado cuando no hay datos para calcular un requerimiento medio. Menos "
    "sólido que un RDA.": {
        "en": "A reference value used when there are no data to calculate an average "
              "requirement. Less solid than an RDA.",
        "fr": "Valeur de référence utilisée quand les données manquent pour calculer un besoin "
              "moyen. Moins solide qu'un RDA."},

    "AMDR · Rango aceptable": {
        "en": "AMDR · Acceptable range", "fr": "AMDR · Fourchette acceptable"},
    "Intervalo de porcentaje de la energía que puede aportar un macronutriente.": {
        "en": "The range of the percentage of energy a macronutrient may supply.",
        "fr": "Intervalle du pourcentage de l'énergie qu'un macronutriment peut apporter."},

    "Biodisponibilidad": {"en": "Bioavailability", "fr": "Biodisponibilité"},
    "Proporción de un nutriente ingerido que llega a estar realmente disponible para el "
    "organismo.": {
        "en": "The proportion of an ingested nutrient that actually becomes available to the "
              "body.",
        "fr": "Proportion d'un nutriment ingéré qui devient réellement disponible pour "
              "l'organisme."},

    "CDRR": {"en": "CDRR", "fr": "CDRR"},
    "Valor de reducción del riesgo crónico. Categoría introducida para el sodio en 2019.": {
        "en": "Chronic disease risk reduction intake. A category introduced for sodium in 2019.",
        "fr": "Valeur de réduction du risque chronique. Catégorie introduite pour le sodium en "
              "2019."},

    "DFE · Equivalente de folato": {
        "en": "DFE · Folate equivalent", "fr": "DFE · Équivalent de folates"},
    "Unidad que corrige la distinta absorción del folato natural y del ácido fólico "
    "sintético.": {
        "en": "The unit that corrects for the different absorption of natural folate and "
              "synthetic folic acid.",
        "fr": "Unité qui corrige la différence d'absorption entre les folates naturels et "
              "l'acide folique synthétique."},

    "EAR · Requerimiento medio": {
        "en": "EAR · Average requirement", "fr": "EAR · Besoin moyen"},
    "Cantidad que cubre la necesidad de la mitad de la población. Sirve para evaluar grupos, "
    "no individuos.": {
        "en": "The amount that covers the need of half the population. It serves to assess "
              "groups, not individuals.",
        "fr": "Quantité qui couvre le besoin de la moitié de la population. Elle sert à évaluer "
              "des groupes, pas des individus."},

    "Fitato": {"en": "Phytate", "fr": "Phytate"},
    "Compuesto de cereales integrales y legumbres que reduce la absorción de varios "
    "minerales.": {
        "en": "A compound in wholegrain cereals and pulses that reduces the absorption of "
              "several minerals.",
        "fr": "Composé des céréales complètes et des légumineuses qui réduit l'absorption de "
              "plusieurs minéraux."},

    "Hierro hemo y no hemo": {
        "en": "Haem and non-haem iron", "fr": "Fer héminique et non héminique"},
    "El primero, de origen animal, se absorbe bastante mejor; el segundo, vegetal, depende del "
    "acompañamiento.": {
        "en": "The first, of animal origin, is absorbed considerably better; the second, from "
              "plants, depends on what comes alongside.",
        "fr": "Le premier, d'origine animale, s'absorbe nettement mieux ; le second, végétal, "
              "dépend de l'accompagnement."},

    "Equivalente metabólico. Múltiplo del gasto energético en reposo: un MET equivale "
    "aproximadamente a una kilocaloría por kilo de peso y hora.": {
        "en": "Metabolic equivalent. A multiple of resting energy expenditure: one MET is "
              "roughly one kilocalorie per kilo of body weight per hour.",
        "fr": "Équivalent métabolique. Multiple de la dépense énergétique de repos : un MET "
              "équivaut à peu près à une kilocalorie par kilo de poids et par heure."},

    "NE · Equivalente de niacina": {
        "en": "NE · Niacin equivalent", "fr": "NE · Équivalent niacine"},
    "Unidad que incluye la niacina fabricada a partir de triptófano.": {
        "en": "The unit that includes the niacin made from tryptophan.",
        "fr": "Unité qui inclut la niacine fabriquée à partir du tryptophane."},

    "RAE · Equivalente de retinol": {
        "en": "RAE · Retinol equivalent", "fr": "RAE · Équivalent de rétinol"},
    "Unidad que corrige la distinta actividad del retinol y de los carotenoides.": {
        "en": "The unit that corrects for the different activity of retinol and of the "
              "carotenoids.",
        "fr": "Unité qui corrige la différence d'activité entre le rétinol et les "
              "caroténoïdes."},

    "RDA · Ingesta recomendada": {
        "en": "RDA · Recommended intake", "fr": "RDA · Apport recommandé"},
    "Requerimiento medio más dos desviaciones típicas. Cubre a cerca del 97 % de la "
    "población.": {
        "en": "The average requirement plus two standard deviations. It covers close to 97 % "
              "of the population.",
        "fr": "Le besoin moyen plus deux écarts types. Il couvre près de 97 % de la "
              "population."},

    "UL · Límite superior": {"en": "UL · Upper limit", "fr": "UL · Limite supérieure"},
    "Techo por encima del cual el riesgo de efectos adversos empieza a aumentar.": {
        "en": "The ceiling above which the risk of adverse effects begins to rise.",
        "fr": "Plafond au-dessus duquel le risque d'effets indésirables commence à augmenter."},

    # ── Cierre ─────────────────────────────────────────────────────────────
    "Y con esto se cierra el libro. No trae ninguna dieta, y eso es exactamente lo que ofrece: "
    "la tabla completa en vez de la mitad publicitable, el techo junto a la recomendación, las "
    "unidades explicadas, las fuentes con nombre y con ruta para que puedas discutirle al "
    "libro, y una advertencia repetida las veces necesarias de que ninguna cifra poblacional "
    "es una prescripción para una persona.": {
        "en": "And with that the book closes. It brings no diet at all, and that is exactly "
              "what it offers: the complete table instead of the advertisable half, the "
              "ceiling next to the recommendation, the units explained, the sources with a "
              "name and a route so that you can argue back at the book, and a warning repeated "
              "as often as necessary that no population figure is a prescription for a person.",
        "fr": "Et sur cela le livre se referme. Il n'apporte aucun régime, et c'est exactement "
              "ce qu'il offre : le tableau complet au lieu de la moitié publicitaire, le "
              "plafond à côté de la recommandation, les unités expliquées, les sources avec un "
              "nom et un chemin pour que vous puissiez contredire le livre, et un "
              "avertissement répété autant de fois qu'il le faut : aucun chiffre de population "
              "n'est une prescription pour une personne."},

    "Si dentro de un año lo único que queda de estas páginas es la costumbre de mirar las dos "
    "columnas antes de comprar un bote, y la de leer la etiqueta por cien gramos en vez de por "
    "porción, el libro habrá hecho su trabajo. Todo lo demás es aparato para llegar a esas dos "
    "costumbres.": {
        "en": "If a year from now the only thing left of these pages is the habit of looking "
              "at both columns before buying a tub, and that of reading the label per hundred "
              "grams instead of per serving, the book will have done its job. Everything else "
              "is apparatus for arriving at those two habits.",
        "fr": "Si dans un an la seule chose qui reste de ces pages est l'habitude de regarder "
              "les deux colonnes avant d'acheter un pot, et celle de lire l'étiquette pour "
              "cent grammes plutôt que par portion, le livre aura fait son travail. Tout le "
              "reste n'est qu'appareillage pour parvenir à ces deux habitudes."},
}
