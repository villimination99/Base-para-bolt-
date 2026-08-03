# -*- coding: utf-8 -*-
"""
CADENAS COMUNES A TODOS LOS PLANES
==================================
Cabeceras, pies, logotipos, avisos legales y bloques de venta que se repiten
en los once documentos. Traducir esto una vez cubre una porción grande de
todos ellos a la vez, porque el catálogo indexa por contenido: dos cadenas
iguales en dos planes comparten traducción por construcción.

Las cadenas que no se traducen —el nombre de marca, el dominio, las rutas de
las fuentes— aparecen igualmente con su valor idéntico. No es redundancia: es
lo que permite que la cobertura del 100 % signifique «revisado» y no
«coincidió por casualidad».
"""

T = {
    # ── Marca y navegación ────────────────────────────────────────────
    "<span>VI</span>": {
        "en": "<span>VI</span>",
        "fr": "<span>VI</span>"},
    '<span class="v">VILLUMINATIONS</span>': {
        "en": '<span class="v">VILLUMINATIONS</span>',
        "fr": '<span class="v">VILLUMINATIONS</span>'},
    "villuminations.com": {
        "en": "villuminations.com",
        "fr": "villuminations.com"},
    "© 2026 VILLUMINATIONS · @villuminations": {
        "en": "© 2026 VILLUMINATIONS · @villuminations",
        "fr": "© 2026 VILLUMINATIONS · @villuminations"},
    '<strong>@villuminations</strong><br>\n        <span class="muted">© 2026 VILLUMINATIONS · Todos los derechos reservados</span>': {
        "en": '<strong>@villuminations</strong><br>\n        <span class="muted">© 2026 VILLUMINATIONS · All rights reserved</span>',
        "fr": '<strong>@villuminations</strong><br>\n        <span class="muted">© 2026 VILLUMINATIONS · Tous droits réservés</span>'},
    '<span>YouTube <b>@villuminations</b></span>\n        <span>Instagram <b>@villuminations</b></span>': {
        "en": '<span>YouTube <b>@villuminations</b></span>\n        <span>Instagram <b>@villuminations</b></span>',
        "fr": '<span>YouTube <b>@villuminations</b></span>\n        <span>Instagram <b>@villuminations</b></span>'},

    # ── Niveles de suscripción ────────────────────────────────────────
    '<span class="dot"></span>Plan Básico · 9,99 $/mes': {
        "en": '<span class="dot"></span>Basic plan · $9.99/month',
        "fr": '<span class="dot"></span>Formule Essentielle · 9,99 $/mois'},
    '<span class="dot"></span>Plan Pro · 19,99 $/mes': {
        "en": '<span class="dot"></span>Pro plan · $19.99/month',
        "fr": '<span class="dot"></span>Formule Pro · 19,99 $/mois'},
    '<span class="dot"></span>Plan Elite · 34,99 $/mes': {
        "en": '<span class="dot"></span>Elite plan · $34.99/month',
        "fr": '<span class="dot"></span>Formule Élite · 34,99 $/mois'},
    "BÁSICO": {"en": "BASIC", "fr": "ESSENTIEL"},
    "PRO": {"en": "PRO", "fr": "PRO"},
    "ELITE": {"en": "ELITE", "fr": "ÉLITE"},
    "Tu plan actual<br>Guías rápidas y fundamentos": {
        "en": "Your current plan<br>Quick guides and fundamentals",
        "fr": "Votre formule actuelle<br>Guides rapides et fondamentaux"},
    # La tarjeta de nivel describe el nivel, nunca el catálogo: enumerar los
    # otros documentos en el pie de un PDF estropea el misterio del resto.
    "Todo incluido<br>+ coaching 1 a 1": {
        "en": "Everything included<br>+ one-to-one coaching",
        "fr": "Tout inclus<br>+ coaching individuel"},

    # ── Página de fuentes verificadas (idéntica en los once) ──────────
    "Fuentes verificadas": {
        "en": "Verified sources", "fr": "Sources vérifiées"},
    'DE DÓNDE SALE <span class="a">CADA CIFRA</span>': {
        "en": 'WHERE EVERY <span class="a">NUMBER COMES FROM</span>',
        "fr": "D'OÙ VIENT <span class=\"a\">CHAQUE CHIFFRE</span>"},
    "Todo dato numérico de este documento procede de fuentes\n      públicas, gratuitas y comprobables. Ninguna cifra está inventada,\n      redondeada por comodidad ni copiada de otra publicación divulgativa.\n      Esta página existe para que puedas verificarlo tú mismo.": {
        "en": "Every number in this document comes from sources that are public, free and checkable. Not one figure is invented, rounded for convenience or copied from another popular publication. This page exists so that you can verify it yourself.",
        "fr": "Tous les chiffres de ce document proviennent de sources publiques, gratuites et vérifiables. Aucun n'est inventé, arrondi par commodité ni recopié d'un autre ouvrage de vulgarisation. Cette page existe pour que vous puissiez le vérifier vous-même."},
    "Por qué estas fuentes y no otras": {
        "en": "Why these sources and no others",
        "fr": "Pourquoi ces sources et pas d'autres"},
    "Las obras del gobierno federal de Estados Unidos no están sujetas a\n        derechos de autor (17 U.S.C. § 105). Eso convierte a un puñado de\n        organismos en la única fuente de datos de nutrición y entrenamiento\n        que es a la vez de primer nivel y legalmente libre. No es material\n        reservado: es material público que casi nadie abre.": {
        "en": "Works of the United States federal government are not subject to copyright (17 U.S.C. § 105). That makes a handful of agencies the only source of nutrition and training data that is both first-rate and legally free. This is not restricted material: it is public material that almost nobody opens.",
        "fr": "Les œuvres du gouvernement fédéral des États-Unis ne sont pas soumises au droit d'auteur (17 U.S.C. § 105). Cela fait d'une poignée d'organismes la seule source de données en nutrition et en entraînement qui soit à la fois de premier plan et juridiquement libre. Ce n'est pas du matériel réservé : c'est du matériel public que presque personne n'ouvre."},
    "Qué buscas": {"en": "What you are looking for", "fr": "Ce que vous cherchez"},
    "Qué encontrarás": {"en": "What you will find", "fr": "Ce que vous y trouverez"},
    "Dónde": {"en": "Where", "fr": "Où"},
    "<b>Ingestas de referencia</b>": {
        "en": "<b>Reference intakes</b>", "fr": "<b>Apports de référence</b>"},
    "RDA, AI y límite superior tolerable de cada vitamina y mineral": {
        "en": "RDA, AI and tolerable upper intake level for every vitamin and mineral",
        "fr": "AJR, AS et limite supérieure tolérable de chaque vitamine et minéral"},
    "ods.od.nih.gov": {"en": "ods.od.nih.gov", "fr": "ods.od.nih.gov"},
    "<b>Composición de alimentos</b>": {
        "en": "<b>Food composition</b>", "fr": "<b>Composition des aliments</b>"},
    "El perfil completo de cualquier alimento, nutriente por nutriente": {
        "en": "The full profile of any food, nutrient by nutrient",
        "fr": "Le profil complet de n'importe quel aliment, nutriment par nutriment"},
    "fdc.nal.usda.gov": {"en": "fdc.nal.usda.gov", "fr": "fdc.nal.usda.gov"},
    "<b>Guías alimentarias</b>": {
        "en": "<b>Dietary guidelines</b>", "fr": "<b>Recommandations alimentaires</b>"},
    "Patrones de dieta y límites de azúcares añadidos, grasa saturada y sodio": {
        "en": "Dietary patterns and limits for added sugars, saturated fat and sodium",
        "fr": "Modèles alimentaires et limites de sucres ajoutés, graisses saturées et sodium"},
    "health.gov": {"en": "health.gov", "fr": "health.gov"},
    "<b>Guías de actividad física</b>": {
        "en": "<b>Physical activity guidelines</b>",
        "fr": "<b>Recommandations d'activité physique</b>"},
    "La dosis semanal, su curva de respuesta y el requisito de fuerza": {
        "en": "The weekly dose, its response curve and the strength requirement",
        "fr": "La dose hebdomadaire, sa courbe de réponse et l'exigence de force"},
    "<b>Doctrina de preparación física</b>": {
        "en": "<b>Physical readiness doctrine</b>",
        "fr": "<b>Doctrine de préparation physique</b>"},
    "FM 7-22: entrenamiento, nutrición, sueño y preparación mental": {
        "en": "FM 7-22: training, nutrition, sleep and mental readiness",
        "fr": "FM 7-22 : entraînement, nutrition, sommeil et préparation mentale"},
    "armypubs.army.mil": {"en": "armypubs.army.mil", "fr": "armypubs.army.mil"},
    "<b>Ecuación de levantamiento</b>": {
        "en": "<b>Lifting equation</b>", "fr": "<b>Équation de levage</b>"},
    "Cuánto peso es razonable levantar en cada situación concreta": {
        "en": "How much weight is reasonable to lift in each specific situation",
        "fr": "Quel poids il est raisonnable de soulever dans chaque situation"},
    "cdc.gov/niosh": {"en": "cdc.gov/niosh", "fr": "cdc.gov/niosh"},
    "<b>Inocuidad alimentaria</b>": {
        "en": "<b>Food safety</b>", "fr": "<b>Sécurité alimentaire</b>"},
    "Temperaturas internas seguras y zona de peligro": {
        "en": "Safe internal temperatures and the danger zone",
        "fr": "Températures internes sûres et zone de danger"},
    "foodsafety.gov": {"en": "foodsafety.gov", "fr": "foodsafety.gov"},
    "<b>Declaraciones de salud</b>": {
        "en": "<b>Health claims</b>", "fr": "<b>Allégations de santé</b>"},
    "Lo que se puede afirmar de un nutriente en Europa, y lo que fue rechazado": {
        "en": "What may legally be claimed about a nutrient in Europe, and what was refused",
        "fr": "Ce que l'on peut affirmer d'un nutriment en Europe, et ce qui a été refusé"},
    "Registro de la Comisión Europea": {
        "en": "European Commission register", "fr": "Registre de la Commission européenne"},
    "Cómo se comprueba este documento a sí mismo": {
        "en": "How this document checks itself",
        "fr": "Comment ce document se vérifie lui-même"},
    "Las cifras de referencia no están escritas a mano: viven en un módulo\n        de datos que el programa de composición verifica antes de escribir una\n        sola línea. Comprueba que los rangos de macronutrientes admitan el\n        cien por cien de la energía, que ninguno de los 19\n        micronutrientes tenga un valor recomendado por encima de su propio\n        techo sin nota que lo explique, y que ninguna temperatura de cocción\n        segura caiga dentro de la zona de peligro. Si una sola comprobación\n        falla, el documento no se compone.": {
        "en": "The reference figures are not typed by hand: they live in a data module that the typesetting program verifies before writing a single line. It checks that the macronutrient ranges can add up to one hundred per cent of energy, that none of the 19 micronutrients has a recommended value above its own ceiling without a note explaining why, and that no safe cooking temperature falls inside the danger zone. If a single check fails, the document is not typeset.",
        "fr": "Les valeurs de référence ne sont pas saisies à la main : elles vivent dans un module de données que le programme de composition vérifie avant d'écrire une seule ligne. Il contrôle que les fourchettes de macronutriments puissent totaliser cent pour cent de l'énergie, qu'aucun des 19 micronutriments n'ait un apport recommandé supérieur à son propre plafond sans note l'expliquant, et qu'aucune température de cuisson sûre ne tombe dans la zone de danger. Si un seul contrôle échoue, le document n'est pas composé."},
    "<b>Los valores de referencia son poblacionales</b><br>\n      Describen lo que cubre las necesidades de la mayoría de adultos sanos. No\n      son una prescripción individual, no contemplan patologías, embarazo,\n      lactancia ni medicación, y ninguna publicación sustituye la valoración de\n      un profesional sanitario colegiado. Si tomas medicación, algunos de los\n      nutrientes citados interaccionan con ella de forma clínicamente\n      relevante: no cambies una ingesta ni empieces un suplemento sin\n      decírselo a quien te receta.": {
        "en": "<b>Reference values are population values</b><br>\n      They describe what covers the needs of most healthy adults. They are not an individual prescription, they do not account for disease, pregnancy, breastfeeding or medication, and no publication replaces assessment by a registered health professional. If you take medication, some of the nutrients named here interact with it in clinically relevant ways: do not change an intake or start a supplement without telling whoever prescribes for you.",
        "fr": "<b>Les valeurs de référence sont des valeurs de population</b><br>\n      Elles décrivent ce qui couvre les besoins de la plupart des adultes en bonne santé. Ce n'est pas une prescription individuelle, elles ne tiennent compte ni des pathologies, ni de la grossesse, ni de l'allaitement, ni des médicaments, et aucune publication ne remplace l'évaluation d'un professionnel de santé. Si vous prenez un traitement, certains des nutriments cités interagissent avec lui de façon cliniquement significative : ne modifiez pas un apport et ne commencez pas un complément sans en parler à qui vous le prescrit."},

    # ── Avisos legales ────────────────────────────────────────────────
    "<b>Aviso importante</b><br>\n      Este documento tiene finalidad exclusivamente informativa y educativa. No constituye\n      consejo médico, diagnóstico ni tratamiento, y no sustituye la valoración de un profesional\n      sanitario colegiado. Consulta con tu médico antes de iniciar cualquier plan nutricional o\n      de entrenamiento, especialmente si estás embarazada o en periodo de lactancia, eres menor\n      de edad, tomas medicación o padeces alguna patología (cardiovascular, metabólica, renal,\n      hepática o trastorno de la conducta alimentaria). Los resultados varían entre personas y\n      no están garantizados. VILLUMINATIONS no se hace responsable del uso que el lector haga\n      de esta información. Contenido protegido por derechos de autor: prohibida su reproducción,\n      distribución o reventa total o parcial sin autorización escrita.": {
        "en": "<b>Important notice</b><br>\n      This document is for informational and educational purposes only. It does not constitute medical advice, diagnosis or treatment, and it does not replace assessment by a registered health professional. Consult your doctor before starting any nutrition or training plan, especially if you are pregnant or breastfeeding, are a minor, take medication or have any medical condition (cardiovascular, metabolic, renal, hepatic, or an eating disorder). Results vary between individuals and are not guaranteed. VILLUMINATIONS accepts no responsibility for the use the reader makes of this information. Copyrighted content: reproduction, distribution or resale in whole or in part without written permission is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Ce document a une finalité exclusivement informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation d'un professionnel de santé. Consultez votre médecin avant d'entreprendre tout programme nutritionnel ou d'entraînement, en particulier si vous êtes enceinte ou allaitante, mineure, sous traitement ou atteinte d'une pathologie (cardiovasculaire, métabolique, rénale, hépatique ou trouble du comportement alimentaire). Les résultats varient d'une personne à l'autre et ne sont pas garantis. VILLUMINATIONS décline toute responsabilité quant à l'usage que le lecteur fera de ces informations. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente, totale ou partielle, sans autorisation écrite est interdite."},
}
