# -*- coding: utf-8 -*-
"""
CADENAS COMPARTIDAS POR VARIOS PLANES
=====================================
Encabezados de tabla, días, momentos del día, niveles y etiquetas de nivel de
suscripción que aparecen en dos o más documentos. Traducir aquí rinde por
varios planes a la vez, porque el catálogo indexa por contenido.
"""

T = {
    # ── Encabezados de tabla ──────────────────────────────────────────
    "Acción": {"en": "Action", "fr": "Action"},
    "Cuándo": {"en": "When", "fr": "Quand"},
    "Detalle": {"en": "Detail", "fr": "Détail"},
    "Dosis": {"en": "Dose", "fr": "Dose"},
    "Duración": {"en": "Duration", "fr": "Durée"},
    "Día": {"en": "Day", "fr": "Jour"},
    "Ejercicio": {"en": "Exercise", "fr": "Exercice"},
    "Fase": {"en": "Phase", "fr": "Phase"},
    "Fecha": {"en": "Date", "fr": "Date"},
    "Foco": {"en": "Focus", "fr": "Objectif"},
    "Inicio": {"en": "Start", "fr": "Début"},
    "Kcal": {"en": "Kcal", "fr": "Kcal"},
    "Mejora": {"en": "Improvement", "fr": "Progression"},
    "Minuto": {"en": "Minute", "fr": "Minute"},
    "Métrica": {"en": "Metric", "fr": "Indicateur"},
    "Objetivo": {"en": "Target", "fr": "Objectif"},
    "Por qué": {"en": "Why", "fr": "Pourquoi"},
    "Producto": {"en": "Product", "fr": "Produit"},
    "Progresión": {"en": "Progression", "fr": "Progression"},
    "Páginas": {"en": "Pages", "fr": "Pages"},
    "Semanas": {"en": "Weeks", "fr": "Semaines"},
    "Suplemento": {"en": "Supplement", "fr": "Complément"},
    "Técnica": {"en": "Technique", "fr": "Technique"},
    "Variable": {"en": "Variable", "fr": "Variable"},
    "RIR": {"en": "RIR", "fr": "RIR"},

    # ── Días abreviados ───────────────────────────────────────────────
    "Lun": {"en": "Mon", "fr": "Lun"},
    "Mar": {"en": "Tue", "fr": "Mar"},
    "Mié": {"en": "Wed", "fr": "Mer"},
    "Jue": {"en": "Thu", "fr": "Jeu"},
    "Vie": {"en": "Fri", "fr": "Ven"},
    "Sáb": {"en": "Sat", "fr": "Sam"},
    "Dom": {"en": "Sun", "fr": "Dim"},
    "Miércoles": {"en": "Wednesday", "fr": "Mercredi"},

    # ── Momentos del día ──────────────────────────────────────────────
    "Desayuno": {"en": "Breakfast", "fr": "Petit-déjeuner"},
    "Almuerzo": {"en": "Lunch", "fr": "Déjeuner"},
    "Cena": {"en": "Dinner", "fr": "Dîner"},
    "Noche": {"en": "Night", "fr": "Soir"},
    "Antes de dormir": {"en": "Before sleep", "fr": "Avant le coucher"},
    "Pre-entreno": {"en": "Pre-workout", "fr": "Avant séance"},
    "Post-entreno": {"en": "Post-workout", "fr": "Après séance"},
    "2 h antes": {"en": "2 h before", "fr": "2 h avant"},
    "2 min": {"en": "2 min", "fr": "2 min"},

    # ── Niveles y objetivos ───────────────────────────────────────────
    "Principiante": {"en": "Beginner", "fr": "Débutant"},
    "Intermedio": {"en": "Intermediate", "fr": "Intermédiaire"},
    "Avanzado": {"en": "Advanced", "fr": "Avancé"},
    "Ganar músculo": {"en": "Build muscle", "fr": "Prendre du muscle"},
    "Perder grasa": {"en": "Lose fat", "fr": "Perdre du gras"},
    "Balance": {"en": "Balance", "fr": "Équilibre"},
    "Completo": {"en": "Full", "fr": "Complet"},

    # ── Zonas del cuerpo y ejercicios ─────────────────────────────────
    "Pecho": {"en": "Chest", "fr": "Pectoraux"},
    "Hombro": {"en": "Shoulder", "fr": "Épaule"},
    "Bíceps": {"en": "Biceps", "fr": "Biceps"},
    "Tríceps": {"en": "Triceps", "fr": "Triceps"},
    "Core": {"en": "Core", "fr": "Gainage"},
    "Core completo": {"en": "Full core", "fr": "Gainage complet"},
    "Plancha": {"en": "Plank", "fr": "Planche"},
    "Cardio": {"en": "Cardio", "fr": "Cardio"},

    # ── Seguimiento ───────────────────────────────────────────────────
    "Peso corporal": {"en": "Body weight", "fr": "Poids corporel"},
    "Cintura (cm)": {"en": "Waist (cm)", "fr": "Tour de taille (cm)"},
    "Semana anterior": {"en": "Previous week", "fr": "Semaine précédente"},
    "Marca anterior": {"en": "Previous best", "fr": "Ancien record"},
    "Marca nueva": {"en": "New best", "fr": "Nouveau record"},
    "Sesiones completadas": {"en": "Sessions completed", "fr": "Séances réalisées"},
    "Días de registro": {"en": "Days logged", "fr": "Jours enregistrés"},
    "Días planificados": {"en": "Days planned", "fr": "Jours planifiés"},
    "Adherencia nutricional": {"en": "Nutrition adherence", "fr": "Observance nutritionnelle"},
    "Entrenamiento y recuperación": {
        "en": "Training and recovery", "fr": "Entraînement et récupération"},
    "Sem. 1": {"en": "Wk 1", "fr": "Sem. 1"},
    "Sem. 2": {"en": "Wk 2", "fr": "Sem. 2"},
    "Sem. 3": {"en": "Wk 3", "fr": "Sem. 3"},
    "Sem. 4": {"en": "Wk 4", "fr": "Sem. 4"},
    "Semana 5": {"en": "Week 5", "fr": "Semaine 5"},
    "Semana 6": {"en": "Week 6", "fr": "Semaine 6"},
    "Semana 7": {"en": "Week 7", "fr": "Semaine 7"},
    "Semana 8": {"en": "Week 8", "fr": "Semaine 8"},

    # ── Suplementos ───────────────────────────────────────────────────
    "Cafeína": {"en": "Caffeine", "fr": "Caféine"},
    "Ashwagandha KSM-66": {"en": "Ashwagandha KSM-66", "fr": "Ashwagandha KSM-66"},
    "300–600 mg": {"en": "300–600 mg", "fr": "300–600 mg"},

    # ── Secciones y venta ─────────────────────────────────────────────
    "01 · Fundamentos": {"en": "01 · Fundamentals", "fr": "01 · Fondamentaux"},
    "Fundamentos<br>y guías rápidas": {
        "en": "Fundamentals<br>and quick guides",
        "fr": "Fondamentaux<br>et guides rapides"},
    "Nutrición avanzada<br>y seguimiento": {
        "en": "Advanced nutrition<br>and tracking",
        "fr": "Nutrition avancée<br>et suivi"},
    "Entrenamiento, HIIT,<br>sueño y coaching 1 a 1": {
        "en": "Training, HIIT,<br>sleep and one-to-one coaching",
        "fr": "Entraînement, HIIT,<br>sommeil et coaching individuel"},
    "Tu plan actual<br>Nutrición avanzada": {
        "en": "Your current plan<br>Advanced nutrition",
        "fr": "Votre formule actuelle<br>Nutrition avancée"},
    "Tu plan actual<br>Todo incluido + coaching": {
        "en": "Your current plan<br>Everything included + coaching",
        "fr": "Votre formule actuelle<br>Tout inclus + coaching"},
    "<span>YouTube <b>@villuminations</b></span><span>Instagram <b>@villuminations</b></span>": {
        "en": "<span>YouTube <b>@villuminations</b></span><span>Instagram <b>@villuminations</b></span>",
        "fr": "<span>YouTube <b>@villuminations</b></span><span>Instagram <b>@villuminations</b></span>"},
}
