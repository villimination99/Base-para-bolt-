# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · melotesia y fases de la Luna
==============================================
Las zonas del cuerpo van en dos columnas de 124 unidades a los lados de la
silueta, y el propio generador avisa de que una etiqueta cortada no sirve de
nada. Se traducen dentro del mismo ancho: «Pieds et lymphe» en vez del
«système lymphatique» entero, que se sale de la columna y está de todos modos
en la ficha del capítulo.

Los rótulos de las ocho fases están abreviados a nueve caracteres por la misma
razón —a partir de ahí se tocan entre sí—, así que las tres lenguas respetan
ese tope. La dirección del ciclo no se marca en cada rótulo porque ya la dicen
los dos extremos de la línea: LUNA CRECIENTE a la izquierda y LUNA MENGUANTE a
la derecha. Por eso «CRESCENT» y «GIBBOUS» pueden aparecer dos veces sin
ambigüedad, exactamente como el diagrama los coloca.

Los verbos van debajo, a cuerpo 11, y son los que más sitio ocupan: se
traducen con una sola palabra corta. «Culminar» es «Peak» en inglés porque
«Culminate» no cabe.
"""

T = {
    # ── Lámina 4 · el zodiaco del cuerpo ───────────────────────────────────
    "Cuello y garganta": {"en": "Neck and throat", "fr": "Cou et gorge"},
    "Hombros, brazos, pulmón": {
        "en": "Shoulders, arms, lungs", "fr": "Épaules, bras, poumons"},
    "Pecho y estómago": {"en": "Chest and stomach", "fr": "Poitrine et estomac"},
    "Corazón y espalda alta": {
        "en": "Heart and upper back", "fr": "Cœur et haut du dos"},
    "Abdomen e intestino": {
        "en": "Abdomen and intestine", "fr": "Abdomen et intestin"},
    "Riñones y lumbares": {
        "en": "Kidneys and lower back", "fr": "Reins et lombaires"},
    "Pelvis y zona genital": {
        "en": "Pelvis and genitals", "fr": "Bassin et zone génitale"},
    "Caderas y muslos": {"en": "Hips and thighs", "fr": "Hanches et cuisses"},
    "Rodillas y huesos": {"en": "Knees and bones", "fr": "Genoux et os"},
    "Pantorrillas y tobillos": {
        "en": "Calves and ankles", "fr": "Mollets et chevilles"},
    "Pies y sistema linfático": {
        "en": "Feet and lymphatic system", "fr": "Pieds et lymphe"},

    # ── Lámina 6 · las ocho fases ──────────────────────────────────────────
    "NUEVA": {"en": "NEW", "fr": "NOUVELLE"},
    "Sembrar": {"en": "Sow", "fr": "Semer"},
    "CRECIENTE": {"en": "CRESCENT", "fr": "CROISSANT"},
    "Empezar": {"en": "Begin", "fr": "Débuter"},
    "CUARTO C.": {"en": "1ST QTR.", "fr": "1ER Q."},
    "Decidir": {"en": "Decide", "fr": "Décider"},
    "GIBOSA C.": {"en": "GIBBOUS", "fr": "GIBBEUSE"},
    "Sostener": {"en": "Sustain", "fr": "Tenir"},
    "LLENA": {"en": "FULL", "fr": "PLEINE"},
    "Culminar": {"en": "Peak", "fr": "Culminer"},
    "GIBOSA M.": {"en": "GIBBOUS", "fr": "GIBBEUSE"},
    "Revisar": {"en": "Review", "fr": "Revoir"},
    "CUARTO M.": {"en": "LAST QTR.", "fr": "DERN. Q."},
    "Soltar": {"en": "Release", "fr": "Lâcher"},
    "MENGUANTE": {"en": "CRESCENT", "fr": "CROISSANT"},
    "Cerrar": {"en": "Close", "fr": "Clore"},

    "LUNA CRECIENTE": {"en": "WAXING MOON", "fr": "LUNE CROISSANTE"},
    "LUNA MENGUANTE": {"en": "WANING MOON", "fr": "LUNE DÉCROISSANTE"},

    # ── Lámina 7 · la geometría de la rueda ────────────────────────────────
    "OPOSICIÓN · 180°": {"en": "OPPOSITION · 180°", "fr": "OPPOSITION · 180°"},
}
