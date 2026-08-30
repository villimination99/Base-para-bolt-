# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · la tabla de las siete operaciones
==============================================================
Cada operación ocupa cuatro casillas —función, lo que se trabaja, la fórmula
del objetivo y el soporte— y las cuatro se traducen por separado porque la
tabla las reparte en filas distintas. Los encabezados cortos («Función»,
«Se trabaja», «Soporte») se mantienen cortos: la columna es estrecha.

Las sumas de los cuadrados —15, 34, 65, 111, 175— no se tocan: son el
resultado de n·(n²+1)/2 y ya están comprobadas en el capítulo de los kameas.
Los huecos «___» del objetivo se conservan tal cual, que es donde el lector
escribe.
"""

T = {
    "Se trabaja": {"en": "What you work on", "fr": "Ce qu'on travaille"},
    "Lo que hay que terminar, soltar o decir no": {
        "en": "What has to be finished, let go of, or refused",
        "fr": "Ce qu'il faut terminer, lâcher ou refuser"},

    "El objetivo se escribe así": {
        "en": "The objective is written like this",
        "fr": "L'objectif s'écrit ainsi"},

    "«Voy a cerrar ___» o «voy a dejar de ___»": {
        "en": "«I am going to close ___» or «I am going to stop ___»",
        "fr": "« Je vais clore ___ » ou « je vais cesser de ___ »"},

    "Soporte": {"en": "Support", "fr": "Support"},
    "Cuadrado de 3×3 · suma 15 · color negro o plomo": {
        "en": "3×3 square · sum 15 · colour black or lead grey",
        "fr": "Carré 3×3 · somme 15 · couleur noir ou plomb"},

    "Júpiter · jueves": {"en": "Jupiter · Thursday", "fr": "Jupiter · jeudi"},
    "La expansión y la generosidad": {
        "en": "Expansion and generosity", "fr": "L'expansion et la générosité"},

    "Lo que debe crecer; lo que uno retiene sin motivo": {
        "en": "What ought to grow; what one holds back for no reason",
        "fr": "Ce qui doit croître ; ce que l'on retient sans motif"},

    "«Voy a abrir ___» o «voy a dar ___»": {
        "en": "«I am going to open ___» or «I am going to give ___»",
        "fr": "« Je vais ouvrir ___ » ou « je vais donner ___ »"},

    "Cuadrado de 4×4 · suma 34 · color púrpura o azul": {
        "en": "4×4 square · sum 34 · colour purple or blue",
        "fr": "Carré 4×4 · somme 34 · couleur pourpre ou bleu"},

    "Marte · martes": {"en": "Mars · Tuesday", "fr": "Mars · mardi"},
    "El empuje y la defensa": {
        "en": "Drive and defence", "fr": "L'élan et la défense"},

    "Lo que se posterga por miedo; el límite que no se pone": {
        "en": "What gets put off out of fear; the limit that never gets set",
        "fr": "Ce que l'on remet par peur ; la limite que l'on ne pose pas"},

    "«Voy a hacer hoy ___» o «voy a decir ___»": {
        "en": "«Today I am going to do ___» or «I am going to say ___»",
        "fr": "« Je vais faire aujourd'hui ___ » ou « je vais dire ___ »"},

    "Cuadrado de 5×5 · suma 65 · color rojo": {
        "en": "5×5 square · sum 65 · colour red",
        "fr": "Carré 5×5 · somme 65 · couleur rouge"},

    "Sol · domingo": {"en": "Sun · Sunday", "fr": "Soleil · dimanche"},
    "La identidad y el centro": {
        "en": "Identity and the centre", "fr": "L'identité et le centre"},

    "Lo que se reconoce como propio; lo que se hace por encargo ajeno": {
        "en": "What is recognised as one's own; what is done on somebody else's orders",
        "fr": "Ce que l'on reconnaît comme sien ; ce que l'on fait sur commande d'autrui"},

    "«Voy a reconocer ___» o «esto no es mío: ___»": {
        "en": "«I am going to acknowledge ___» or «this is not mine: ___»",
        "fr": "« Je vais reconnaître ___ » ou « ceci n'est pas à moi : ___ »"},

    "Cuadrado de 6×6 · suma 111 · color oro": {
        "en": "6×6 square · sum 111 · colour gold",
        "fr": "Carré 6×6 · somme 111 · couleur or"},

    "Venus · viernes": {"en": "Venus · Friday", "fr": "Vénus · vendredi"},
    "El vínculo y el valor": {
        "en": "The bond and worth", "fr": "Le lien et la valeur"},

    "Lo que se ha descuidado en una relación; lo que se valora de verdad": {
        "en": "What has been neglected in a relationship; what is really valued",
        "fr": "Ce que l'on a négligé dans une relation ; ce à quoi l'on tient vraiment"},

    "«Voy a atender ___» o «voy a reparar ___»": {
        "en": "«I am going to attend to ___» or «I am going to repair ___»",
        "fr": "« Je vais m'occuper de ___ » ou « je vais réparer ___ »"},

    "Cuadrado de 7×7 · suma 175 · color verde o cobre": {
        "en": "7×7 square · sum 175 · colour green or copper",
        "fr": "Carré 7×7 · somme 175 · couleur vert ou cuivre"},
}
