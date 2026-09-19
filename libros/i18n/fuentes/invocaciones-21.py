# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · la ficha del diario, la revisión y los siete errores
=================================================================================
La ficha del diario son siete campos con su glosa al lado, en columna
estrecha. Las glosas se traducen tan cortas como el original: «Otra palabra»
tiene que seguir cabiendo en una línea.

La entrada de ejemplo conserva sus cifras —17/03, 7:10, 9 min— porque el día
diecisiete no puede leerse como mes en ninguna de las tres lenguas y la hora
va en el mismo formato. Lo que sí se traduce son las palabras de estado y el
fallo. El párrafo pide entradas «cortas, feas y precisas» y el ejemplo tiene
que seguir siéndolo después de traducirlo.

Los siete errores se numeran solos en el documento; aquí solo van los tres
primeros y el resto sigue en la entrega siguiente.
"""

T = {
    "Duración": {"en": "Duration", "fr": "Durée"},
    "Minutos efectivos": {"en": "Actual minutes", "fr": "Minutes effectives"},

    "Operación": {"en": "Operation", "fr": "Opération"},
    "Rito diario / planetaria / examen / dedicación": {
        "en": "Daily rite / planetary / examination / dedication",
        "fr": "Rite quotidien / planétaire / examen / dédicace"},

    "Estado antes": {"en": "State before", "fr": "État avant"},
    "Una palabra. No un párrafo: una palabra": {
        "en": "One word. Not a paragraph: one word",
        "fr": "Un mot. Pas un paragraphe : un mot"},

    "Estado después": {"en": "State after", "fr": "État après"},
    "Otra palabra": {"en": "Another word", "fr": "Un autre mot"},

    "Qué falló": {"en": "What failed", "fr": "Ce qui a raté"},
    "El olvido, la interrupción, la prisa, la desgana": {
        "en": "Forgetting, interruption, haste, reluctance",
        "fr": "L'oubli, l'interruption, la hâte, le manque d'envie"},

    "Qué apareció": {"en": "What turned up", "fr": "Ce qui est apparu"},
    "Solo si apareció algo. Casi nunca aparece nada, y anotar que no apareció nada también es "
    "un dato": {
        "en": "Only if something did. Almost nothing ever turns up, and noting that nothing "
              "turned up is a datum too",
        "fr": "Seulement s'il est apparu quelque chose. Il n'apparaît presque jamais rien, et "
              "noter qu'il n'est rien apparu est aussi une donnée"},

    "La acción concreta": {"en": "The concrete action", "fr": "L'action concrète"},
    "Lo que vas a hacer en las próximas 24 horas": {
        "en": "What you are going to do in the next 24 hours",
        "fr": "Ce que vous allez faire dans les 24 heures qui viennent"},

    "La tentación de escribir bonito arruina el registro. Las entradas útiles son cortas, feas "
    "y precisas: «17/03, 7:10, 9 min, rito diario, antes: disperso, después: igual, falló la "
    "prisa en el norte». Eso, repetido cien veces, revela patrones que ningún párrafo elegante "
    "revela.": {
        "en": "The temptation to write nicely ruins the record. Useful entries are short, ugly "
              "and precise: «17/03, 7:10, 9 min, daily rite, before: scattered, after: same, "
              "haste in the north was what failed». That, repeated a hundred times, reveals "
              "patterns no elegant paragraph reveals.",
        "fr": "La tentation d'écrire joliment ruine le registre. Les entrées utiles sont "
              "courtes, laides et précises : « 17/03, 7:10, 9 min, rite quotidien, avant : "
              "dispersé, après : pareil, c'est la hâte au nord qui a raté ». Cela, répété cent "
              "fois, révèle des schémas qu'aucun paragraphe élégant ne révèle."},

    "La revisión, que es donde está el valor": {
        "en": "The review, which is where the value is",
        "fr": "La relecture, c'est là qu'est la valeur"},

    "Cada domingo, relee la semana entera. Diez minutos.": {
        "en": "Every Sunday, reread the whole week. Ten minutes.",
        "fr": "Chaque dimanche, relisez la semaine entière. Dix minutes."},

    "Cuenta las sesiones hechas frente a las previstas. El número, sin excusas al lado.": {
        "en": "Count the sessions done against the sessions planned. The number, with no "
              "excuses beside it.",
        "fr": "Comptez les séances faites face aux séances prévues. Le nombre, sans excuses à "
              "côté."},

    "Busca el patrón de los fallos: siempre falla el mismo día, la misma hora, el mismo "
    "movimiento.": {
        "en": "Look for the pattern in the failures: it is always the same day, the same hour, "
              "the same movement that fails.",
        "fr": "Cherchez le schéma des ratés : c'est toujours le même jour, la même heure, le "
              "même mouvement qui rate."},

    "Cada tres meses, relee el trimestre completo y escribe media página. Aquí es donde se ve "
    "lo que ninguna sesión individual muestra.": {
        "en": "Every three months, reread the whole quarter and write half a page. This is "
              "where you see what no individual session shows.",
        "fr": "Tous les trois mois, relisez le trimestre entier et écrivez une demi-page. C'est "
              "là qu'on voit ce qu'aucune séance isolée ne montre."},

    "Cada año, relee el año. Es la práctica más incómoda del libro y la que más enseña.": {
        "en": "Every year, reread the year. It is the most uncomfortable practice in the book "
              "and the one that teaches most.",
        "fr": "Chaque année, relisez l'année. C'est la pratique la plus inconfortable du livre "
              "et celle qui enseigne le plus."},

    # ── Los siete errores ──────────────────────────────────────────────────
    "Recogidos sin piedad, porque son predecibles y cuestan años.": {
        "en": "Set down without mercy, because they are predictable and they cost years.",
        "fr": "Consignés sans pitié, parce qu'ils sont prévisibles et qu'ils coûtent des années."},

    "Los siete errores": {"en": "The seven errors", "fr": "Les sept erreurs"},

    "Coleccionar en lugar de practicar. Leer diez libros, comprar cuatro armas, aprender doce "
    "sistemas y no haber hecho treinta días seguidos de nada. Es el error más común y el más "
    "cómodo, porque estudiar es agradable y repetir no.": {
        "en": "Collecting instead of practising. Reading ten books, buying four weapons, "
              "learning twelve systems and never having done thirty days in a row of anything. "
              "It is the commonest error and the most comfortable, because studying is pleasant "
              "and repeating is not.",
        "fr": "Collectionner au lieu de pratiquer. Lire dix livres, acheter quatre armes, "
              "apprendre douze systèmes et n'avoir jamais fait trente jours de suite de quoi que "
              "ce soit. C'est l'erreur la plus commune et la plus confortable, parce qu'étudier "
              "est agréable et répéter ne l'est pas."},

    "Empezar por lo complicado. La operación espectacular antes del rito diario. Sin la base "
    "instalada no hay atención disponible para nada elaborado, y lo elaborado sin atención es "
    "disfraz.": {
        "en": "Starting with the complicated. The spectacular operation before the daily rite. "
              "With the base not installed there is no attention available for anything "
              "elaborate, and the elaborate without attention is fancy dress.",
        "fr": "Commencer par le compliqué. L'opération spectaculaire avant le rite quotidien. "
              "Sans la base installée il n'y a pas d'attention disponible pour quoi que ce soit "
              "d'élaboré, et l'élaboré sans attention est un déguisement."},

    "Cambiar de sistema al primer aburrimiento. El aburrimiento de la segunda semana no es una "
    "señal de que el sistema no sirve: es exactamente el tramo que hay que atravesar, y "
    "cambiar de método en ese punto garantiza atravesarlo nunca.": {
        "en": "Changing system at the first sign of boredom. The boredom of the second week is "
              "not a sign that the system is no good: it is exactly the stretch that has to be "
              "crossed, and changing method at that point guarantees never crossing it.",
        "fr": "Changer de système au premier ennui. L'ennui de la deuxième semaine n'est pas le "
              "signe que le système ne vaut rien : c'est exactement le tronçon qu'il faut "
              "traverser, et changer de méthode à ce moment-là garantit de ne jamais le "
              "traverser."},
}
