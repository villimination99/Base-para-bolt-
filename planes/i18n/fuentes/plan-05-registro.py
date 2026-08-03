# -*- coding: utf-8 -*-
"""
PLAN 05 · PRO — Registro de progreso semanal
============================================
Plantilla de seguimiento. Las etiquetas de columna se traducen cortas a
propósito: en una tabla de ancho fijo, una etiqueta larga en francés parte la
celda y descoloca la rejilla entera.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Seguimiento de 4 semanas</small>\n        <span class="glow">REGISTRO DE<br>PROGRESO</span>': {
        "en": '<small>4-week tracking</small>\n        <span class="glow">PROGRESS<br>TRACKER</span>',
        "fr": '<small>Suivi sur 4 semaines</small>\n        <span class="glow">SUIVI DES<br>PROGRÈS</span>'},
    "Lo que no se mide no se mejora. Cuatro semanas de datos para decidir\n        con hechos y <em>no</em> con sensaciones.": {
        "en": "What is not measured does not improve. Four weeks of data so you can decide on facts and <em>not</em> on feelings.",
        "fr": "Ce qui ne se mesure pas ne s'améliore pas. Quatre semaines de données pour décider sur des faits et <em>non</em> sur des impressions."},
    '<span class="chip on">Mediciones</span>\n        <span class="chip on">Adherencia</span>\n        <span class="chip">Entrenamiento</span>\n        <span class="chip">Gráfica de tendencia</span>': {
        "en": '<span class="chip on">Measurements</span>\n        <span class="chip on">Adherence</span>\n        <span class="chip">Training</span>\n        <span class="chip">Trend chart</span>',
        "fr": '<span class="chip on">Mesures</span>\n        <span class="chip on">Observance</span>\n        <span class="chip">Entraînement</span>\n        <span class="chip">Courbe de tendance</span>'},
    "Medidas corporales": {"en": "Body measurements", "fr": "Mesures corporelles"},
    '<strong>Edición 2026</strong><br>\n        <span class="muted">Plantilla de seguimiento mensual · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br>\n        <span class="muted">Monthly tracking template · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br>\n        <span class="muted">Modèle de suivi mensuel · 8 pages</span>'},

    # ── 01 · Protocolo de medición ────────────────────────────────────
    "01 · Protocolo de medición": {
        "en": "01 · Measurement protocol", "fr": "01 · Protocole de mesure"},
    'MEDIR <span class="a">BIEN</span> ANTES QUE MEDIR MUCHO': {
        "en": 'MEASURE <span class="a">WELL</span> BEFORE MEASURING OFTEN',
        "fr": 'MESURER <span class="a">BIEN</span> AVANT DE MESURER BEAUCOUP'},
    "Un dato tomado en malas condiciones es peor que no tener dato: te lleva a cambiar un plan que estaba funcionando. Estas son las condiciones que hacen que tus números sean comparables entre semanas.": {
        "en": "A reading taken in poor conditions is worse than no reading at all: it makes you change a plan that was working. These are the conditions that make your numbers comparable from week to week.",
        "fr": "Une donnée relevée dans de mauvaises conditions est pire que pas de donnée du tout : elle vous pousse à changer un plan qui fonctionnait. Voici les conditions qui rendent vos chiffres comparables d'une semaine à l'autre."},
    "Medida": {"en": "Measurement", "fr": "Mesure"},
    "Cómo hacerlo bien": {"en": "How to do it right", "fr": "Comment bien le faire"},
    "Todos los días, al levantarte": {
        "en": "Every day, on waking", "fr": "Chaque jour, au lever"},
    "Tras ir al baño, en ayunas, sin ropa, misma báscula y mismo suelo": {
        "en": "After the bathroom, fasted, undressed, same scale and same floor",
        "fr": "Après les toilettes, à jeun, sans vêtements, même balance et même sol"},
    "Lunes en ayunas": {"en": "Monday, fasted", "fr": "Lundi à jeun"},
    "A la altura del ombligo, de pie, relajado, al final de una espiración normal": {
        "en": "At navel height, standing, relaxed, at the end of a normal exhale",
        "fr": "À hauteur du nombril, debout, détendu, en fin d'expiration normale"},
    "Por la línea de los pezones, brazos relajados a los lados": {
        "en": "Across the nipple line, arms relaxed at your sides",
        "fr": "Au niveau des mamelons, bras relâchés le long du corps"},
    "Brazo contraído, en el punto de mayor perímetro, siempre el mismo lado": {
        "en": "Arm flexed, at its widest point, always the same side",
        "fr": "Bras contracté, au point le plus large, toujours du même côté"},
    "Pierna": {"en": "Thigh", "fr": "Cuisse"},
    "15 cm por encima de la rótula, marcado siempre igual": {
        "en": "15 cm above the kneecap, marked the same way every time",
        "fr": "15 cm au-dessus de la rotule, repérés toujours de la même façon"},
    "Fotos": {"en": "Photos", "fr": "Photos"},
    "Lunes, cada 2 semanas": {"en": "Monday, every 2 weeks", "fr": "Lundi, toutes les 2 semaines"},
    "Misma luz, misma hora, misma distancia y mismas tres poses": {
        "en": "Same light, same time, same distance and the same three poses",
        "fr": "Même lumière, même heure, même distance et les mêmes trois poses"},
    "Trabaja con el promedio, no con el dato del día": {
        "en": "Work with the average, not with a single day's reading",
        "fr": "Travaillez avec la moyenne, pas avec la donnée du jour"},
    "Tu peso puede variar 1,5 kg entre dos días por agua, sal, glucógeno o tránsito intestinal. Suma los siete pesos de la semana, divide entre siete y compara <strong>ese promedio</strong> con el de la semana anterior. Es la única comparación honesta.": {
        "en": "Your weight can swing 1.5 kg between two days because of water, salt, glycogen or gut transit. Add up the seven weigh-ins of the week, divide by seven and compare <strong>that average</strong> with the previous week's. It is the only honest comparison.",
        "fr": "Votre poids peut varier de 1,5 kg d'un jour à l'autre à cause de l'eau, du sel, du glycogène ou du transit. Additionnez les sept pesées de la semaine, divisez par sept et comparez <strong>cette moyenne</strong> à celle de la semaine précédente. C'est la seule comparaison honnête."},
    "Cómo usar este registro": {"en": "How to use this tracker", "fr": "Comment utiliser ce suivi"},
    "<b>Rellena a diario, no el domingo de memoria</b>Dos minutos cada noche valen más que media hora reconstruyendo la semana.": {
        "en": "<b>Fill it in daily, not from memory on Sunday</b>Two minutes each night are worth more than half an hour reconstructing the week.",
        "fr": "<b>Remplissez chaque jour, pas le dimanche de mémoire</b>Deux minutes chaque soir valent mieux qu'une demi-heure à reconstituer la semaine."},
    "<b>Anota lo que hiciste, no lo que pretendías</b>El registro solo sirve si es honesto, incluidos los días malos. Especialmente los días malos.": {
        "en": "<b>Log what you did, not what you meant to do</b>The record is only useful if it is honest, bad days included. Especially bad days.",
        "fr": "<b>Notez ce que vous avez fait, pas ce que vous vouliez faire</b>Le relevé ne sert que s'il est honnête, mauvais jours compris. Surtout les mauvais jours."},
    "<b>Revisa cada lunes y toma UNA decisión</b>Mantener, sumar o restar. Un solo cambio por semana; si cambias tres variables no sabrás cuál funcionó.": {
        "en": "<b>Review every Monday and take ONE decision</b>Hold, add or cut. One change a week; if you change three variables you will not know which one worked.",
        "fr": "<b>Faites le point chaque lundi et prenez UNE décision</b>Maintenir, ajouter ou retirer. Un seul changement par semaine ; si vous en changez trois, vous ne saurez pas lequel a marché."},
    "<b>Al cerrar las 4 semanas, ve a la página 7</b>Ahí vuelcas todo y ves la tendencia real del mes de un vistazo.": {
        "en": "<b>When the 4 weeks are up, go to page 7</b>That is where you pour everything in and see the month's real trend at a glance.",
        "fr": "<b>Au terme des 4 semaines, allez à la page 7</b>C'est là que vous reportez tout et voyez la tendance réelle du mois d'un coup d'œil."},
    "de peso por promedio": {"en": "of weight by average", "fr": "de poids en moyenne"},
    "cambio por semana": {"en": "change per week", "fr": "de variation par semaine"},
    "de registro al día": {"en": "of logging per day", "fr": "de saisie par jour"},

    # ── Semanas ───────────────────────────────────────────────────────
    'SEMANA <span class="a">1</span> · REGISTRO COMPLETO': {
        "en": 'WEEK <span class="a">1</span> · FULL LOG',
        "fr": 'SEMAINE <span class="a">1</span> · RELEVÉ COMPLET'},
    'SEMANA <span class="a">2</span> · REGISTRO COMPLETO': {
        "en": 'WEEK <span class="a">2</span> · FULL LOG',
        "fr": 'SEMAINE <span class="a">2</span> · RELEVÉ COMPLET'},
    'SEMANA <span class="a">3</span> · REGISTRO COMPLETO': {
        "en": 'WEEK <span class="a">3</span> · FULL LOG',
        "fr": 'SEMAINE <span class="a">3</span> · RELEVÉ COMPLET'},
    'SEMANA <span class="a">4</span> · REGISTRO COMPLETO': {
        "en": 'WEEK <span class="a">4</span> · FULL LOG',
        "fr": 'SEMAINE <span class="a">4</span> · RELEVÉ COMPLET'},
    'Fecha de inicio: <span class="fill w"></span>&nbsp;&nbsp; Fecha de fin: <span class="fill w"></span>': {
        "en": 'Start date: <span class="fill w"></span>&nbsp;&nbsp; End date: <span class="fill w"></span>',
        "fr": 'Date de début : <span class="fill w"></span>&nbsp;&nbsp; Date de fin : <span class="fill w"></span>'},
    "Mediciones corporales · lunes en ayunas": {
        "en": "Body measurements · Monday, fasted",
        "fr": "Mesures corporelles · lundi à jeun"},
    "Diferencia": {"en": "Difference", "fr": "Différence"},
    "Notas": {"en": "Notes", "fr": "Notes"},
    "Peso medio de la semana (kg)": {
        "en": "Average weight for the week (kg)",
        "fr": "Poids moyen de la semaine (kg)"},
    "Pecho (cm)": {"en": "Chest (cm)", "fr": "Poitrine (cm)"},
    "Bíceps derecho (cm)": {"en": "Right biceps (cm)", "fr": "Biceps droit (cm)"},
    "Pierna derecha (cm)": {"en": "Right thigh (cm)", "fr": "Cuisse droite (cm)"},
    "% de grasa estimado": {"en": "Estimated body fat %", "fr": "% de masse grasse estimé"},
    "Peso a. m.": {"en": "AM weight", "fr": "Poids du matin"},
    "Kcal reales": {"en": "Actual kcal", "fr": "Kcal réelles"},
    "Agua": {"en": "Water", "fr": "Eau"},
    "Suplementos": {"en": "Supplements", "fr": "Compléments"},
    "Lunes": {"en": "Monday", "fr": "Lundi"},
    '<span class="box"></span>Crea <span class="box"></span>Omega <span class="box"></span>D3': {
        "en": '<span class="box"></span>Crea <span class="box"></span>Omega <span class="box"></span>D3',
        "fr": '<span class="box"></span>Créa <span class="box"></span>Oméga <span class="box"></span>D3'},
    "Martes": {"en": "Tuesday", "fr": "Mardi"},
    "Jueves": {"en": "Thursday", "fr": "Jeudi"},
    "Viernes": {"en": "Friday", "fr": "Vendredi"},
    "Sábado": {"en": "Saturday", "fr": "Samedi"},
    "Domingo": {"en": "Sunday", "fr": "Dimanche"},
    "Sesión": {"en": "Session", "fr": "Séance"},
    "Ejercicio principal": {"en": "Main lift", "fr": "Exercice principal"},
    "Carga × reps": {"en": "Load × reps", "fr": "Charge × reps"},
    "Sueño (h)": {"en": "Sleep (h)", "fr": "Sommeil (h)"},
    "Energía 1-10": {"en": "Energy 1-10", "fr": "Énergie 1-10"},
    "Sesión 1": {"en": "Session 1", "fr": "Séance 1"},
    "Sesión 2": {"en": "Session 2", "fr": "Séance 2"},
    "Sesión 3": {"en": "Session 3", "fr": "Séance 3"},
    "Sesión 4": {"en": "Session 4", "fr": "Séance 4"},
    '<strong>Decisión del lunes:</strong>\n      <span class="opt"><span class="box"></span>Mantener</span>\n      <span class="opt"><span class="box"></span>Sumar 200 kcal</span>\n      <span class="opt"><span class="box"></span>Restar 200 kcal</span>\n      &nbsp;·&nbsp; Motivo: <span class="fill w"></span>': {
        "en": '<strong>Monday decision:</strong>\n      <span class="opt"><span class="box"></span>Hold</span>\n      <span class="opt"><span class="box"></span>Add 200 kcal</span>\n      <span class="opt"><span class="box"></span>Cut 200 kcal</span>\n      &nbsp;·&nbsp; Reason: <span class="fill w"></span>',
        "fr": '<strong>Décision du lundi :</strong>\n      <span class="opt"><span class="box"></span>Maintenir</span>\n      <span class="opt"><span class="box"></span>Ajouter 200 kcal</span>\n      <span class="opt"><span class="box"></span>Retirer 200 kcal</span>\n      &nbsp;·&nbsp; Motif : <span class="fill w"></span>'},

    # ── Resumen y tendencia ───────────────────────────────────────────
    "Resumen del mes": {"en": "Month summary", "fr": "Bilan du mois"},
    'LA <span class="a">TENDENCIA</span> DEL MES': {
        "en": 'THE MONTH\'S <span class="a">TREND</span>',
        "fr": 'LA <span class="a">TENDANCE</span> DU MOIS'},
    "Marca un punto por semana y únelos. Lo que importa no es ningún punto concreto, sino <strong>la dirección de la línea</strong>.": {
        "en": "Mark one point per week and join them up. What matters is not any single point but <strong>the direction of the line</strong>.",
        "fr": "Placez un point par semaine et reliez-les. Ce qui compte n'est aucun point précis, mais <strong>la direction de la ligne</strong>."},
    "PESO MEDIO (kg)": {"en": "AVERAGE WEIGHT (kg)", "fr": "POIDS MOYEN (kg)"},
    "Resumen comparativo de las 4 semanas": {
        "en": "Side-by-side summary of the 4 weeks",
        "fr": "Bilan comparatif des 4 semaines"},
    "Total": {"en": "Total", "fr": "Total"},
    "Peso medio (kg)": {"en": "Average weight (kg)", "fr": "Poids moyen (kg)"},
    "Días con macros cumplidos": {"en": "Days macros were met", "fr": "Jours avec macros atteintes"},
    "Media de horas de sueño": {"en": "Average hours of sleep", "fr": "Moyenne d'heures de sommeil"},
    "Récords personales del mes": {
        "en": "Personal bests of the month", "fr": "Records personnels du mois"},

    # ── Interpretación ────────────────────────────────────────────────
    # Ojo: el plan 01 usa la clase «lo» y este la clase «ok» para la misma
    # frase. Son segmentos distintos porque el marcado forma parte del
    # segmento, y por eso hacen falta las dos entradas.
    '<span class="tag ok">No cambies nada</span>': {
        "en": '<span class="tag ok">Change nothing</span>',
        "fr": '<span class="tag ok">Ne changez rien</span>'},
    "Interpretación": {"en": "Interpretation", "fr": "Interprétation"},
    'QUÉ TE ESTÁN <span class="a">DICIENDO TUS DATOS</span>': {
        "en": 'WHAT YOUR <span class="a">DATA IS TELLING YOU</span>',
        "fr": 'CE QUE <span class="a">VOS DONNÉES VOUS DISENT</span>'},
    "Peso": {"en": "Weight", "fr": "Poids"},
    "Fuerza": {"en": "Strength", "fr": "Force"},
    "Lectura": {"en": "Reading", "fr": "Lecture"},
    "Sube": {"en": "Rising", "fr": "En hausse"},
    "Estable": {"en": "Flat", "fr": "Stable"},
    "Baja": {"en": "Falling", "fr": "En baisse"},
    "Volumen limpio perfecto": {"en": "Textbook clean bulk", "fr": "Prise de masse propre parfaite"},
    "Superávit excesivo": {"en": "Surplus too large", "fr": "Surplus excessif"},
    "Recomposición en marcha": {"en": "Recomposition under way", "fr": "Recomposition en cours"},
    "Definición ideal": {"en": "Ideal cut", "fr": "Sèche idéale"},
    "Estás perdiendo músculo": {"en": "You are losing muscle", "fr": "Vous perdez du muscle"},
    "Mala recuperación o registro poco fiable": {
        "en": "Poor recovery or unreliable logging",
        "fr": "Mauvaise récupération ou relevé peu fiable"},
    '<span class="tag ok">Mantén y ten paciencia</span>': {
        "en": '<span class="tag ok">Hold and be patient</span>',
        "fr": '<span class="tag ok">Maintenez et patientez</span>'},
    '<span class="tag ok">Mantén el déficit</span>': {
        "en": '<span class="tag ok">Keep the deficit</span>',
        "fr": '<span class="tag ok">Gardez le déficit</span>'},
    '<span class="tag no">Sube proteína y calorías</span>': {
        "en": '<span class="tag no">Raise protein and calories</span>',
        "fr": '<span class="tag no">Plus de protéines et kcal</span>'},
    '<span class="tag no">Revisa sueño y medición</span>': {
        "en": '<span class="tag no">Check sleep and measurement</span>',
        "fr": '<span class="tag no">Vérifiez sommeil et mesures</span>'},
    '<span class="tag hi">Resta 200 kcal</span>': {
        "en": '<span class="tag hi">Cut 200 kcal</span>',
        "fr": '<span class="tag hi">Retirez 200 kcal</span>'},
    "Antes de cambiar el plan, comprueba estas cuatro cosas": {
        "en": "Before you change the plan, check these four things",
        "fr": "Avant de changer le plan, vérifiez ces quatre points"},
    "¿He registrado <strong>todo</strong> lo que he comido, incluidos aceites, salsas y bebidas?": {
        "en": "Have I logged <strong>everything</strong> I ate, including oils, sauces and drinks?",
        "fr": "Ai-je noté <strong>tout</strong> ce que j'ai mangé, huiles, sauces et boissons comprises ?"},
    "¿He comparado promedios semanales o me estoy fijando en el peso de un día suelto?": {
        "en": "Have I compared weekly averages, or am I fixating on a single day's weight?",
        "fr": "Ai-je comparé des moyennes hebdomadaires, ou suis-je fixé sur le poids d'un seul jour ?"},
    "¿He dormido menos de 7 horas más de dos noches esta semana?": {
        "en": "Have I slept less than 7 hours on more than two nights this week?",
        "fr": "Ai-je dormi moins de 7 heures plus de deux nuits cette semaine ?"},
    "¿He completado todas las sesiones planificadas con las cargas previstas?": {
        "en": "Have I completed every planned session with the loads I intended?",
        "fr": "Ai-je réalisé toutes les séances prévues avec les charges prévues ?"},
    "Si alguna respuesta es «no», el problema no es el plan: es la ejecución. Corrige la ejecución antes de tocar los números.": {
        "en": "If any answer is «no», the problem is not the plan: it is the execution. Fix the execution before touching the numbers.",
        "fr": "Si une réponse est « non », le problème n'est pas le plan : c'est l'exécution. Corrigez-la avant de toucher aux chiffres."},
    "Conclusiones del mes y objetivos del siguiente": {
        "en": "Conclusions for the month and targets for the next",
        "fr": "Conclusions du mois et objectifs du suivant"},
    'EL DATO SOLO SIRVE <span class="a">SI SE MIDE IGUAL</span>': {
        "en": 'A NUMBER ONLY COUNTS <span class="a">IF IT IS MEASURED THE SAME WAY</span>',
        "fr": 'UNE DONNÉE NE VAUT <span class="a">QUE SI ELLE EST MESURÉE PAREIL</span>'},
    "Misma hora, misma báscula, mismas condiciones: <strong>la tendencia de cuatro semanas</strong> es la única cifra que decide algo. Un solo día nunca es una señal, por mucho que lo parezca.": {
        "en": "Same time, same scale, same conditions: <strong>the four-week trend</strong> is the only figure that decides anything. A single day is never a signal, however much it looks like one.",
        "fr": "Même heure, même balance, mêmes conditions : <strong>la tendance sur quatre semaines</strong> est le seul chiffre qui décide de quelque chose. Un jour isolé n'est jamais un signal, même quand il en a l'air."},
    "<b>Aviso importante</b><br>\n      Plantilla de seguimiento con finalidad informativa y educativa. No constituye consejo\n      médico, diagnóstico ni tratamiento, y no sustituye la valoración de un profesional\n      sanitario colegiado. El registro de peso y medidas puede resultar contraproducente en\n      personas con antecedentes de trastorno de la conducta alimentaria: en ese caso, consulta\n      con un profesional antes de usar este documento. Los resultados varían entre personas y no\n      están garantizados. Contenido protegido por derechos de autor: prohibida su reproducción,\n      distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      A tracking template for informational and educational purposes. It does not constitute medical advice, diagnosis or treatment, and it does not replace assessment by a registered health professional. Logging weight and measurements can be counterproductive for people with a history of eating disorders: in that case, consult a professional before using this document. Results vary between individuals and are not guaranteed. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Modèle de suivi à finalité informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement. Le relevé du poids et des mesures peut être contre-productif en cas d'antécédents de trouble du comportement alimentaire : consultez alors un professionnel avant usage. Les résultats varient et ne sont pas garantis. Contenu protégé : reproduction, distribution ou revente interdites sans autorisation écrite de VILLUMINATIONS."},
}
