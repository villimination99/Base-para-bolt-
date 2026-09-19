# -*- coding: utf-8 -*-
"""
RÓTULOS DE LAS LÁMINAS
======================
Los emblemas y las figuras son un sprite compartido: los once planes usan el
mismo fichero. Traducir estos rótulos una vez cubre las ilustraciones de todo
el catálogo, y por eso este módulo es el de mayor rendimiento por línea.

Se traducen los rótulos, nunca la geometría. La anatomía usa el término
anatómico habitual en cada lengua, no el calco.
"""

T = {
    # ── Anatomía ──────────────────────────────────────────────────────
    "Antebrazo": {"en": "Forearm", "fr": "Avant-bras"},
    "Bíceps braquial": {"en": "Biceps brachii", "fr": "Biceps brachial"},
    "Tríceps braquial": {"en": "Triceps brachii", "fr": "Triceps brachial"},
    "Deltoides": {"en": "Deltoid", "fr": "Deltoïde"},
    "Pectoral mayor": {"en": "Pectoralis major", "fr": "Grand pectoral"},
    "Dorsal ancho": {"en": "Latissimus dorsi", "fr": "Grand dorsal"},
    "Trapecio superior": {"en": "Upper trapezius", "fr": "Trapèze supérieur"},
    "Trapecio y romboides": {"en": "Trapezius and rhomboids", "fr": "Trapèze et rhomboïdes"},
    "Recto abdominal": {"en": "Rectus abdominis", "fr": "Grand droit"},
    "Oblicuos": {"en": "Obliques", "fr": "Obliques"},
    "Erector lumbar": {"en": "Erector spinae", "fr": "Érecteurs du rachis"},
    "Glúteo mayor": {"en": "Gluteus maximus", "fr": "Grand fessier"},
    "Cuádriceps": {"en": "Quadriceps", "fr": "Quadriceps"},
    "Isquiotibiales": {"en": "Hamstrings", "fr": "Ischio-jambiers"},
    "Gemelo y sóleo": {"en": "Gastrocnemius and soleus", "fr": "Jumeaux et soléaire"},
    "Tibial anterior": {"en": "Tibialis anterior", "fr": "Tibial antérieur"},
    "VISTA ANTERIOR": {"en": "FRONT VIEW", "fr": "VUE ANTÉRIEURE"},
    "VISTA POSTERIOR": {"en": "BACK VIEW", "fr": "VUE POSTÉRIEURE"},
    "ANTERIOR": {"en": "FRONT", "fr": "ANTÉRIEUR"},
    "POSTERIOR": {"en": "BACK", "fr": "POSTÉRIEUR"},
    "Torso": {"en": "Torso", "fr": "Tronc"},
    "Espalda": {"en": "Back", "fr": "Dos"},
    "Piernas": {"en": "Legs", "fr": "Jambes"},
    "Lumbar": {"en": "Lower back", "fr": "Lombaires"},
    "Rodilla": {"en": "Knee", "fr": "Genou"},
    "rodilla": {"en": "knee", "fr": "genou"},

    # ── Técnica de levantamiento ──────────────────────────────────────
    "Barra sobre": {"en": "Bar over", "fr": "Barre au-dessus"},
    "Cadera atrás,": {"en": "Hips back,", "fr": "Hanches en arrière,"},
    "Lumbar neutra": {"en": "Neutral lower back", "fr": "Lombaires neutres"},
    "pecho arriba": {"en": "chest up", "fr": "poitrine haute"},
    "hacia dentro": {"en": "tracking inward", "fr": "vers l'intérieur"},
    "redondeada": {"en": "rounded", "fr": "arrondies"},
    "el trapecio": {"en": "the trapezius", "fr": "le trapèze"},
    "en todo el rango": {"en": "through the full range", "fr": "sur toute l'amplitude"},
    "Sin tensión": {"en": "No tension", "fr": "Sans tension"},

    # ── Porciones con la mano ─────────────────────────────────────────
    "PALMA": {"en": "PALM", "fr": "PAUME"},
    "PUÑO": {"en": "FIST", "fr": "POING"},
    "PULGAR": {"en": "THUMB", "fr": "POUCE"},
    "120–150 g de carne": {"en": "120–150 g of meat", "fr": "120–150 g de viande"},
    "o pescado · ≈30 g prot.": {"en": "or fish · ≈30 g prot.", "fr": "ou poisson · ≈30 g prot."},
    "180 g cocido de arroz": {"en": "180 g cooked rice", "fr": "180 g de riz cuit"},
    "o pasta · ≈45 g carbos": {"en": "or pasta · ≈45 g carbs", "fr": "ou pâtes · ≈45 g glucides"},
    "1 cucharada de aceite": {"en": "1 tablespoon of oil", "fr": "1 cuillère à soupe d'huile"},
    "o 20 g frutos secos ≈14 g": {
        "en": "or 20 g nuts ≈14 g", "fr": "ou 20 g de fruits secs ≈14 g"},
    "Verdura": {"en": "Vegetables", "fr": "Légumes"},
    "Carbohidrato": {"en": "Carbohydrate", "fr": "Glucides"},
    "Grasa": {"en": "Fat", "fr": "Lipides"},
    "Prot.": {"en": "Prot.", "fr": "Prot."},
    "Carbos": {"en": "Carbs", "fr": "Glucides"},
    "g/kg": {"en": "g/kg", "fr": "g/kg"},

    # ── El plato ──────────────────────────────────────────────────────
    "EL PLATO": {"en": "THE PLATE", "fr": "L'ASSIETTE"},
    "El plato repartido": {"en": "The plate, divided", "fr": "L'assiette répartie"},
    "Media verdura, un cuarto": {
        "en": "Half vegetables, one quarter", "fr": "Moitié légumes, un quart"},
    "proteína, un cuarto carbos": {
        "en": "protein, one quarter carbs", "fr": "protéines, un quart glucides"},
    "MEDITERRÁNEA": {"en": "MEDITERRANEAN", "fr": "MÉDITERRANÉENNE"},
    "ACOMPAÑAMIENTO": {"en": "SIDE DISH", "fr": "ACCOMPAGNEMENT"},
    "Fibra, fruta y verdura": {
        "en": "Fibre, fruit and vegetables", "fr": "Fibres, fruits et légumes"},
    "Completa el total": {"en": "Makes up the total", "fr": "Complète le total"},

    # ── Días de la semana ─────────────────────────────────────────────
    "LUN": {"en": "MON", "fr": "LUN"},
    "MAR": {"en": "TUE", "fr": "MAR"},
    "MIÉ": {"en": "WED", "fr": "MER"},
    "JUE": {"en": "THU", "fr": "JEU"},
    "VIE": {"en": "FRI", "fr": "VEN"},
    "SÁB": {"en": "SAT", "fr": "SAM"},
    "DOM": {"en": "SUN", "fr": "DIM"},
    "7 días": {"en": "7 days", "fr": "7 jours"},
    "Siete días": {"en": "Seven days", "fr": "Sept jours"},
    "7 noches": {"en": "7 nights", "fr": "7 nuits"},
    "21 días": {"en": "21 days", "fr": "21 jours"},
    "4 semanas": {"en": "4 weeks", "fr": "4 semaines"},
    "8 semanas": {"en": "8 weeks", "fr": "8 semaines"},
    "12 semanas": {"en": "12 weeks", "fr": "12 semaines"},
    "10 rutinas": {"en": "10 routines", "fr": "10 routines"},
    "60–90 min": {"en": "60–90 min", "fr": "60–90 min"},

    # ── Ciclado de carbohidratos ──────────────────────────────────────
    "CICLADO": {"en": "CYCLING", "fr": "CYCLAGE"},
    "ALTO": {"en": "HIGH", "fr": "HAUT"},
    "MEDIO": {"en": "MEDIUM", "fr": "MOYEN"},
    "BAJO": {"en": "LOW", "fr": "BAS"},
    "1 g/kg carbos": {"en": "1 g/kg carbs", "fr": "1 g/kg glucides"},
    "1,5 g/kg carbos": {"en": "1.5 g/kg carbs", "fr": "1,5 g/kg glucides"},
    "Carga y descarga": {"en": "Load and unload", "fr": "Charge et décharge"},
    "La regla que no cambia: el día alto va donde está el mayor volumen de entrenamiento. La media semanal queda en déficit aunque tres días estén en superávit.": {
        "en": "The rule that does not change: the high day goes where the training volume is highest. The weekly average still lands in deficit even though three days are in surplus.",
        "fr": "La règle qui ne change pas : le jour haut se place là où le volume d'entraînement est le plus élevé. La moyenne hebdomadaire reste en déficit même si trois jours sont en surplus."},
    "SUPERÁVIT": {"en": "SURPLUS", "fr": "SURPLUS"},
    "Volumen limpio": {"en": "Clean bulking", "fr": "Prise de masse propre"},
    "DEF": {"en": "CUT", "fr": "SÈCHE"},
    "VOL": {"en": "BULK", "fr": "MASSE"},
    "Definir y construir": {"en": "Cut and build", "fr": "Sécher et construire"},

    # ── Ventana e insulina ────────────────────────────────────────────
    "SENSIBILIDAD A LA INSULINA": {
        "en": "INSULIN SENSITIVITY", "fr": "SENSIBILITÉ À L'INSULINE"},
    "COMIDA PRE": {"en": "PRE-WORKOUT MEAL", "fr": "REPAS AVANT"},
    "ENTRENO": {"en": "TRAINING", "fr": "SÉANCE"},
    "POST 0–90 min": {"en": "POST 0–90 min", "fr": "APRÈS 0–90 min"},
    "RESTO DEL DÍA": {"en": "REST OF THE DAY", "fr": "RESTE DE LA JOURNÉE"},
    "+ 0,4 g/kg proteína · poca grasa": {
        "en": "+ 0.4 g/kg protein · low fat", "fr": "+ 0,4 g/kg protéines · peu de lipides"},
    "+ 0,4 g/kg proteína rápida": {
        "en": "+ 0.4 g/kg fast protein", "fr": "+ 0,4 g/kg protéines rapides"},
    "Intra: 30–40 g": {"en": "Intra: 30–40 g", "fr": "Intra : 30–40 g"},
    "si supera 75 min": {"en": "if it runs over 75 min", "fr": "si elle dépasse 75 min"},
    "El músculo capta glucosa con más eficacia justo después de entrenar: ahí van los carbohidratos de digestión rápida.": {
        "en": "Muscle takes up glucose most efficiently right after training: that is where the fast-digesting carbohydrates go.",
        "fr": "Le muscle capte le glucose le plus efficacement juste après l'entraînement : c'est là que vont les glucides à digestion rapide."},

    # ── HIIT e intervalos ─────────────────────────────────────────────
    "INTERVALOS": {"en": "INTERVALS", "fr": "INTERVALLES"},
    "TRABAJO · DESCANSO": {"en": "WORK · REST", "fr": "TRAVAIL · REPOS"},
    "Trabajo y descanso": {"en": "Work and rest", "fr": "Travail et repos"},
    "Trabajo al máximo": {"en": "All-out work", "fr": "Travail à fond"},
    "Descanso activo: camina y respira por la nariz": {
        "en": "Active rest: walk and breathe through your nose",
        "fr": "Repos actif : marchez et respirez par le nez"},
    "85–95 % FC máx.": {"en": "85–95 % max HR", "fr": "85–95 % FC max"},
    "FC máx.": {"en": "Max HR", "fr": "FC max"},
    "LISS": {"en": "LISS", "fr": "LISS"},
    "La frecuencia cardiaca no vuelve a reposo entre intervalos: esa deuda acumulada es la que produce el efecto metabólico del HIIT.": {
        "en": "Heart rate does not return to rest between intervals: that accumulated debt is what produces the metabolic effect of HIIT.",
        "fr": "La fréquence cardiaque ne revient pas au repos entre les intervalles : c'est cette dette accumulée qui produit l'effet métabolique du HIIT."},
    "Full body": {"en": "Full body", "fr": "Corps entier"},
    "Descanso": {"en": "Rest", "fr": "Repos"},
    "DESCANSO": {"en": "REST", "fr": "REPOS"},
    "Reposo": {"en": "At rest", "fr": "Au repos"},
    "PROGRESIÓN": {"en": "PROGRESSION", "fr": "PROGRESSION"},

    # ── Sueño ─────────────────────────────────────────────────────────
    "5 CICLOS · 90 MIN": {"en": "5 CYCLES · 90 MIN", "fr": "5 CYCLES · 90 MIN"},
    "Cinco ciclos": {"en": "Five cycles", "fr": "Cinq cycles"},
    "DESPIERTO": {"en": "AWAKE", "fr": "ÉVEIL"},
    "REM": {"en": "REM", "fr": "REM"},
    "LIGERO N1-N2": {"en": "LIGHT N1-N2", "fr": "LÉGER N1-N2"},
    "PROFUNDO N3": {"en": "DEEP N3", "fr": "PROFOND N3"},
    "DOS FASES": {"en": "TWO PHASES", "fr": "DEUX PHASES"},
    "Sueño profundo · primera mitad de la noche": {
        "en": "Deep sleep · first half of the night",
        "fr": "Sommeil profond · première moitié de la nuit"},
    "REM · segunda mitad": {"en": "REM · second half", "fr": "REM · seconde moitié"},
    "Hormona de crecimiento y reparación muscular": {
        "en": "Growth hormone and muscle repair",
        "fr": "Hormone de croissance et réparation musculaire"},
    "Memoria y regulación emocional": {
        "en": "Memory and emotional regulation",
        "fr": "Mémoire et régulation émotionnelle"},

    # ── Respiración ───────────────────────────────────────────────────
    "CAJA 4-4-4-4 · ENFOQUE": {"en": "BOX 4-4-4-4 · FOCUS", "fr": "CARRÉ 4-4-4-4 · CONCENTRATION"},
    "INHALA 4": {"en": "INHALE 4", "fr": "INSPIRE 4"},
    "RETÉN 4": {"en": "HOLD 4", "fr": "RETIENS 4"},
    "EXHALA 4": {"en": "EXHALE 4", "fr": "EXPIRE 4"},
    "RETÉN VACÍO 4": {"en": "HOLD EMPTY 4", "fr": "RETIENS À VIDE 4"},
    "TÉCNICA 4-7-8 · ANTES DE DORMIR": {
        "en": "4-7-8 TECHNIQUE · BEFORE SLEEP", "fr": "TECHNIQUE 4-7-8 · AVANT LE COUCHER"},
    "INHALA 4 s": {"en": "INHALE 4 s", "fr": "INSPIRE 4 s"},
    "RETÉN 7 s": {"en": "HOLD 7 s", "fr": "RETIENS 7 s"},
    "EXHALA 8 s": {"en": "EXHALE 8 s", "fr": "EXPIRE 8 s"},
    "Por la nariz": {"en": "Through the nose", "fr": "Par le nez"},
    "Por la boca, con sonido": {
        "en": "Through the mouth, audibly", "fr": "Par la bouche, avec un son"},
    "4 ciclos · activa el sistema parasimpático en menos de un minuto": {
        "en": "4 cycles · engages the parasympathetic system in under a minute",
        "fr": "4 cycles · active le système parasympathique en moins d'une minute"},
    "5–10 ciclos antes de una serie máxima": {
        "en": "5–10 cycles before a maximal set",
        "fr": "5–10 cycles avant une série maximale"},
    "Respiración pautada": {"en": "Paced breathing", "fr": "Respiration guidée"},
    "ATENCIÓN": {"en": "ATTENTION", "fr": "ATTENTION"},

    # ── Emblemas y navegación de láminas ──────────────────────────────
    "1 · SALIDA": {"en": "1 · START", "fr": "1 · DÉPART"},
    "2 · PARALELO": {"en": "2 · PARALLEL", "fr": "2 · PARALLÈLE"},
    "3 · PROFUNDO": {"en": "3 · DEEP", "fr": "3 · PROFOND"},
    "4 · ERRORES": {"en": "4 · FAULTS", "fr": "4 · ERREURS"},
    "SUPLEMENTOS": {"en": "SUPPLEMENTS", "fr": "COMPLÉMENTS"},
    "Dosis y momento": {"en": "Dose and timing", "fr": "Dose et moment"},
    "REGISTRO": {"en": "TRACKING", "fr": "SUIVI"},
    "Medir para corregir": {"en": "Measure to correct", "fr": "Mesurer pour corriger"},
    "GUÍA": {"en": "GUIDE", "fr": "GUIDE"},
    "Guía semanal": {"en": "Weekly guide", "fr": "Guide hebdomadaire"},
    "TÚ": {"en": "YOU", "fr": "VOUS"},
}
