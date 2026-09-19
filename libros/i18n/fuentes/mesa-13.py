# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · márgenes de conservación y el registro de declaraciones
===========================================================================
Las declaraciones autorizadas son frases legales: existen redactadas palabra
por palabra en las tres lenguas y no se traducen libremente, se copian de la
redacción oficial. Por eso «prolongado», «normal» o «series breves de alta
intensidad» aparecen exactamente donde aparecen; el capítulo entero consiste
en enseñar a leer esas palabras, y una paráfrasis las borraría.
"""

T = {
    "como mucho 2 horas fuera de la nevera": {
        "en": "2 hours out of the fridge at most",
        "fr": "2 heures hors du réfrigérateur au maximum"},
    "Con más de 32 °C": {"en": "Above 32 °C", "fr": "Au-delà de 32 °C"},
    "como mucho 1 hora": {"en": "1 hour at most", "fr": "1 heure au maximum"},

    "Nevera": {"en": "Fridge", "fr": "Réfrigérateur"},
    "4 °C o menos, comprobado con termómetro y no con la rueda del mando": {
        "en": "4 °C or less, checked with a thermometer and not with the control dial",
        "fr": "4 °C ou moins, vérifié au thermomètre et non à la molette du bouton"},

    "Congelador": {"en": "Freezer", "fr": "Congélateur"},
    "-18 °C. Congelar no mata bacterias: las detiene. Al descongelar vuelven a multiplicarse": {
        "en": "-18 °C. Freezing does not kill bacteria: it stops them. On thawing they start "
              "multiplying again",
        "fr": "-18 °C. Congeler ne tue pas les bactéries : cela les arrête. À la "
              "décongélation, elles se remultiplient"},

    "Tres cosas que casi todo el mundo hace mal": {
        "en": "Three things almost everyone gets wrong",
        "fr": "Trois choses que presque tout le monde fait mal"},

    "Descongelar sobre la encimera. La superficie entra en la zona de peligro mucho antes de "
    "que el centro se descongele. Se descongela en la nevera, en agua fría cambiada cada media "
    "hora, o en el microondas para cocinar inmediatamente después.": {
        "en": "Thawing on the worktop. The surface enters the danger zone long before the "
              "centre thaws. You thaw in the fridge, in cold water changed every half hour, or "
              "in the microwave to cook immediately afterwards.",
        "fr": "Décongeler sur le plan de travail. La surface entre dans la zone de danger bien "
              "avant que le cœur ne dégèle. On décongèle au réfrigérateur, dans de l'eau "
              "froide changée toutes les demi-heures, ou au micro-ondes pour cuire "
              "immédiatement après."},

    "Lavar el pollo crudo bajo el grifo. No elimina bacterias y salpica gotas a más de medio "
    "metro alrededor, contaminando fregadero, encimera y lo que haya cerca. El calor de la "
    "sartén hace ese trabajo; el grifo solo lo reparte.": {
        "en": "Washing raw chicken under the tap. It does not remove bacteria and it splashes "
              "droplets more than half a metre around, contaminating the sink, the worktop and "
              "whatever is nearby. The heat of the pan does that job; the tap only spreads it "
              "about.",
        "fr": "Laver le poulet cru sous le robinet. Cela n'élimine pas les bactéries et "
              "projette des gouttelettes à plus d'un demi-mètre alentour, contaminant l'évier, "
              "le plan de travail et ce qui se trouve à proximité. La chaleur de la poêle fait "
              "ce travail ; le robinet ne fait que le répandre."},

    "Usar el mismo plato para llevar la carne cruda a la parrilla y recogerla hecha. Es la vía "
    "de contaminación cruzada más frecuente en cualquier cocina doméstica, y se resuelve con "
    "un plato limpio.": {
        "en": "Using the same plate to carry the raw meat to the grill and to bring it back "
              "cooked. It is the commonest route of cross-contamination in any domestic "
              "kitchen, and it is solved with a clean plate.",
        "fr": "Utiliser la même assiette pour porter la viande crue au gril et la récupérer "
              "cuite. C'est la voie de contamination croisée la plus fréquente dans n'importe "
              "quelle cuisine domestique, et elle se règle avec une assiette propre."},

    "Quién tiene que ser más estricto": {
        "en": "Who has to be stricter", "fr": "Qui doit être plus strict"},

    "Embarazadas, mayores, niños pequeños y personas con la inmunidad comprometida tienen un "
    "riesgo apreciablemente mayor, y en ese caso algunas categorías —quesos de leche cruda, "
    "huevo crudo, pescado crudo, embutidos no curados, brotes germinados— dejan de ser una "
    "cuestión de preferencia. Si estás en alguno de esos grupos, esto se consulta y no se "
    "improvisa.": {
        "en": "Pregnant women, older people, small children and people with compromised "
              "immunity carry an appreciably greater risk, and in that case some categories "
              "—raw-milk cheeses, raw egg, raw fish, uncured charcuterie, sprouted seeds— stop "
              "being a matter of preference. If you are in one of those groups, this gets "
              "asked about and not improvised.",
        "fr": "Les femmes enceintes, les personnes âgées, les jeunes enfants et les personnes "
              "immunodéprimées courent un risque nettement plus élevé, et dans ce cas "
              "certaines catégories —fromages au lait cru, œuf cru, poisson cru, charcuteries "
              "non séchées, graines germées— cessent d'être une affaire de préférence. Si vous "
              "faites partie de l'un de ces groupes, cela se demande et ne s'improvise pas."},

    # ── El registro de declaraciones ───────────────────────────────────────
    "Este es el capítulo que justifica media colección. En Europa existe un registro público "
    "donde consta cada declaración de propiedades saludables que se ha solicitado para un "
    "nutriente, su evaluación científica y el veredicto. La parte que se publicita es la de "
    "las autorizadas. La interesante es la otra.": {
        "en": "This is the chapter that justifies half a collection. In Europe there is a "
              "public register recording every health claim that has been applied for on "
              "behalf of a nutrient, its scientific assessment and the verdict. The part that "
              "gets advertised is the authorised one. The interesting part is the other one.",
        "fr": "Voici le chapitre qui justifie la moitié d'une collection. Il existe en Europe "
              "un registre public où figure chaque allégation de santé demandée pour un "
              "nutriment, son évaluation scientifique et le verdict. La partie dont on fait "
              "publicité est celle des allégations autorisées. La partie intéressante est "
              "l'autre."},

    "Cómo funciona el registro": {
        "en": "How the register works", "fr": "Comment fonctionne le registre"},

    "Una empresa que quiere poner en un envase que su producto hace algo tiene que solicitar "
    "la autorización de esa frase. Un panel científico evalúa si existe una relación "
    "causa-efecto suficientemente establecida entre el nutriente y el efecto, y emite un "
    "dictamen. Después se autoriza o no. Todo el expediente queda público, incluidos los "
    "rechazos.": {
        "en": "A company that wants to put on a packet that its product does something has to "
              "apply for authorisation of that sentence. A scientific panel assesses whether a "
              "sufficiently established cause-and-effect relationship exists between the "
              "nutrient and the effect, and issues an opinion. It is then authorised or not. "
              "The whole file stays public, rejections included.",
        "fr": "Une entreprise qui veut inscrire sur un emballage que son produit fait quelque "
              "chose doit demander l'autorisation de cette phrase. Un panel scientifique "
              "évalue s'il existe une relation de cause à effet suffisamment établie entre le "
              "nutriment et l'effet, et rend un avis. L'allégation est ensuite autorisée ou "
              "non. Tout le dossier reste public, refus compris."},

    "Eso convierte al registro en algo que no existe en ningún otro campo: una lista oficial "
    "de afirmaciones que la industria quiso hacer y no pudo sostener. No es material "
    "reservado; es material público que casi nadie consulta, y ahí está la diferencia.": {
        "en": "That turns the register into something that exists in no other field: an "
              "official list of claims the industry wanted to make and could not sustain. It "
              "is not restricted material; it is public material almost nobody consults, and "
              "that is where the difference lies.",
        "fr": "Cela fait du registre quelque chose qui n'existe dans aucun autre domaine : une "
              "liste officielle d'affirmations que l'industrie a voulu faire et n'a pas pu "
              "soutenir. Ce ne sont pas des documents réservés ; ce sont des documents publics "
              "que presque personne ne consulte, et c'est là toute la différence."},

    "Algunas autorizadas, con su letra pequeña": {
        "en": "Some authorised ones, with their small print",
        "fr": "Quelques-unes autorisées, avec leurs petits caractères"},

    "La proteína contribuye al crecimiento y al mantenimiento de la masa muscular. Autorizada, "
    "y por eso la ves en todos los envases de batido.": {
        "en": "Protein contributes to the growth and maintenance of muscle mass. Authorised, "
              "and that is why you see it on every shake container.",
        "fr": "Les protéines contribuent au développement et au maintien de la masse "
              "musculaire. Autorisée, et c'est pourquoi vous la voyez sur tous les pots de "
              "boisson protéinée."},

    "La creatina aumenta el rendimiento físico en series de ejercicios breves de alta "
    "intensidad. Autorizada con una condición de uso concreta, del orden de tres gramos "
    "diarios. Es una de las poquísimas ayudas ergogénicas con declaración autorizada, y "
    "conviene saber que la frase autorizada habla de series breves e intensas, no de "
    "resistencia ni de composición corporal.": {
        "en": "Creatine increases physical performance in successive bursts of short-term, "
              "high-intensity exercise. Authorised with a specific condition of use, of the "
              "order of three grams a day. It is one of the very few ergogenic aids with an "
              "authorised claim, and it is worth knowing that the authorised sentence talks "
              "about short intense bursts, not about endurance or body composition.",
        "fr": "La créatine améliore les performances physiques lors de séries successives "
              "d'exercices très intenses de courte durée. Autorisée avec une condition "
              "d'emploi précise, de l'ordre de trois grammes par jour. C'est l'une des très "
              "rares aides ergogéniques dotées d'une allégation autorisée, et il faut savoir "
              "que la phrase autorisée parle de séries brèves et intenses, non d'endurance ni "
              "de composition corporelle."},

    "Las soluciones de hidratos y electrolitos contribuyen a mantener el rendimiento en "
    "ejercicio de resistencia prolongado. Autorizada; es la base legal de las bebidas "
    "deportivas, y la palabra «prolongado» hace todo el trabajo.": {
        "en": "Carbohydrate-electrolyte solutions contribute to the maintenance of endurance "
              "performance during prolonged endurance exercise. Authorised; it is the legal "
              "basis of sports drinks, and the word «prolonged» does all the work.",
        "fr": "Les solutions de glucides et d'électrolytes contribuent au maintien des "
              "performances d'endurance lors d'exercices d'endurance prolongés. Autorisée ; "
              "c'est la base légale des boissons pour sportifs, et le mot « prolongés » fait "
              "tout le travail."},

    "La vitamina D contribuye al mantenimiento de huesos y a la función muscular normal. "
    "Autorizada. Nota la palabra «normal»: la declaración cubre el mantenimiento de una "
    "función, no una mejora del rendimiento.": {
        "en": "Vitamin D contributes to the maintenance of bones and to normal muscle "
              "function. Authorised. Note the word «normal»: the claim covers the maintenance "
              "of a function, not an improvement in performance.",
        "fr": "La vitamine D contribue au maintien d'une ossature normale et à une fonction "
              "musculaire normale. Autorisée. Notez le mot « normale » : l'allégation couvre "
              "le maintien d'une fonction, pas une amélioration des performances."},

    "Y algunas que se solicitaron y no se autorizaron": {
        "en": "And some that were applied for and not authorised",
        "fr": "Et quelques-unes demandées et non autorisées"},

    "Las declaraciones de la glucosamina sobre el cartílago y las articulaciones. Evaluadas y "
    "no autorizadas por relación causa-efecto insuficientemente establecida. Se sigue "
    "vendiendo con enorme éxito.": {
        "en": "The glucosamine claims about cartilage and joints. Assessed and not authorised "
              "for insufficiently established cause and effect. It goes on selling "
              "enormously well.",
        "fr": "Les allégations de la glucosamine sur le cartilage et les articulations. "
              "Évaluées et non autorisées pour relation de cause à effet insuffisamment "
              "établie. Elle continue de se vendre avec un immense succès."},

    "Las declaraciones de los aminoácidos ramificados sobre la masa muscular y la "
    "recuperación. Evaluadas y no autorizadas.": {
        "en": "The branched-chain amino acid claims about muscle mass and recovery. Assessed "
              "and not authorised.",
        "fr": "Les allégations des acides aminés ramifiés sur la masse musculaire et la "
              "récupération. Évaluées et non autorisées."},

    "Las declaraciones de la L-carnitina sobre la oxidación de las grasas y el control del "
    "peso. Evaluadas y no autorizadas.": {
        "en": "The L-carnitine claims about fat oxidation and weight control. Assessed and not "
              "authorised.",
        "fr": "Les allégations de la L-carnitine sur l'oxydation des graisses et le contrôle "
              "du poids. Évaluées et non autorisées."},
}
