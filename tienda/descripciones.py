# -*- coding: utf-8 -*-
"""
VILLUMINATIONS — Fichas de producto
-----------------------------------
El texto de las cinco fichas digitales de villuminations.com, en las tres
lenguas en que se venden. Vive aquí y no en Shopify por la misma razón que las
traducciones de los libros viven en i18n/: en el panel de la tienda no hay
historial, no hay revisión y no hay forma de comparar tres idiomas de un
vistazo. Se escribe aquí, se sube con publicar.py y se corrige aquí.

Reglas que sigue este texto, y que conviene no romper al editarlo:

· Solo se afirma lo que el producto tiene. Las cifras —páginas, capítulos,
  láminas, documentos— salen de los PDF ya auditados y no de la intuición
  comercial. Si un libro crece, cambian aquí antes de cambiar en la tienda.

· Ninguna ficha describe el contenido de otro producto. Los planes están en
  tres niveles y cada uno enumera lo suyo: el que compra Básico no lee ahí lo
  que hay dentro de Pro. La única excepción es Elite, que es acumulativo por
  definición y tiene que decirlo.

· Nada de promesas de resultado. Estos documentos son de referencia y de
  método; no prometen kilos, ni plazos, ni transformaciones. La ficha dice lo
  mismo que dice el libro por dentro, que además es lo que evita una
  devolución y una reseña de una estrella.

· El aviso sanitario o legal que lleva el producto dentro se resume en la
  ficha. Un comprador tiene derecho a saber antes de pagar que esto no
  sustituye a un profesional.

· La marca es VILLUMINATIONS, nunca «VILLUMINATIONS 99».

El campo «handle» es el de Shopify y no se toca: cambiarlo rompe los enlaces
que ya estén publicados.
"""

# --------------------------------------------------------------------------
# Los tres niveles de planes. Cada uno enumera SOLO sus propios documentos.
# --------------------------------------------------------------------------

BASICO = {
    "handle": "basico-volumen-limpio",
    "gid": "gid://shopify/Product/7141932138545",
    "titulo": {
        "es": "Básico · Volumen Limpio",
        "en": "Basic · Clean Bulk",
        "fr": "Basique · Prise de masse propre",
    },
    "es": """
<p><strong>Un documento de referencia para ganar masa sin ganar grasa a ciegas.</strong>
La guía rápida de volumen limpio: cómo se calcula el punto de partida, cuánto
superávit tiene sentido, qué se mide cada semana y qué se hace con lo medido.</p>

<h3>Qué recibes</h3>
<ul>
  <li><strong>Guía Rápida — Volumen Limpio</strong>, en PDF.</li>
  <li>Las tres ediciones: <strong>español, inglés y francés</strong>, en el mismo archivo de descarga.</li>
  <li>Versión de pantalla y versión preparada para imprimir.</li>
</ul>

<h3>Cómo está hecho</h3>
<p>Las cifras de referencia no son de una revista: proceden de fuentes oficiales
de acceso público y están recalculadas y comprobadas una a una. Cada tabla del
documento o se calcula o se verifica antes de imprimirse; si un número no
cuadra, el documento no se genera.</p>

<h3>Lo que no es</h3>
<p>No es una pauta dietética individualizada ni un programa de entrenamiento
personal. No considera patologías. Si tienes una condición médica, tomas
medicación, estás embarazada o tienes antecedentes de trastorno alimentario,
consúltalo antes con tu profesional sanitario.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS.</em></p>
""",
    "en": """
<p><strong>A reference document for gaining muscle without gaining fat blindly.</strong>
The quick guide to a clean bulk: how the starting point is calculated, how much
of a surplus makes sense, what gets measured each week and what to do with what
you measured.</p>

<h3>What you get</h3>
<ul>
  <li><strong>Quick Guide — Clean Bulk</strong>, as a PDF.</li>
  <li>All three editions: <strong>English, Spanish and French</strong>, in the same download.</li>
  <li>A screen version and a print-ready version.</li>
</ul>

<h3>How it is made</h3>
<p>The reference figures do not come from a magazine: they come from publicly
available official sources and have been recalculated and checked one by one.
Every table in the document is either computed or verified before it is
printed; if a number does not add up, the document is not generated.</p>

<h3>What it is not</h3>
<p>It is not an individualised dietary plan or a personal training programme. It
does not take pathologies into account. If you have a medical condition, take
medication, are pregnant or have a history of eating disorder, check with your
health professional first.</p>

<p><em>Digital download. An original work by VILLUMINATIONS.</em></p>
""",
    "fr": """
<p><strong>Un document de référence pour prendre du muscle sans prendre du gras à l'aveugle.</strong>
Le guide rapide de la prise de masse propre : comment se calcule le point de
départ, quel surplus a du sens, ce que l'on mesure chaque semaine et ce que
l'on fait de ce que l'on a mesuré.</p>

<h3>Ce que vous recevez</h3>
<ul>
  <li><strong>Guide rapide — Prise de masse propre</strong>, en PDF.</li>
  <li>Les trois éditions : <strong>français, espagnol et anglais</strong>, dans le même téléchargement.</li>
  <li>Une version écran et une version prête à imprimer.</li>
</ul>

<h3>Comment il est fait</h3>
<p>Les chiffres de référence ne sortent pas d'un magazine : ils proviennent de
sources officielles publiques et ont été recalculés et vérifiés un à un. Chaque
tableau du document est soit calculé soit contrôlé avant d'être imprimé ; si un
nombre ne tombe pas juste, le document n'est pas généré.</p>

<h3>Ce que ce n'est pas</h3>
<p>Ce n'est ni un régime individualisé ni un programme d'entraînement personnel.
Il ne tient pas compte des pathologies. Si vous avez une affection médicale, si
vous prenez un traitement, si vous êtes enceinte ou si vous avez des antécédents
de trouble du comportement alimentaire, consultez d'abord votre professionnel de
santé.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS.</em></p>
""",
}

PRO = {
    "handle": "pro-definicion-volumen",
    "gid": "gid://shopify/Product/7141932171313",
    "titulo": {
        "es": "Pro · Definición + Volumen",
        "en": "Pro · Cutting + Bulking",
        "fr": "Pro · Sèche + Prise de masse",
    },
    "es": """
<p><strong>Cinco documentos para llevar un ciclo completo de definición y volumen
con números propios y no con reglas prestadas.</strong></p>

<h3>Qué recibes</h3>
<ul>
  <li><strong>Guía Rápida — Volumen Limpio</strong></li>
  <li><strong>Ciclado de Carbohidratos</strong></li>
  <li><strong>Guía de Suplementación</strong></li>
  <li><strong>Plan Definición + Volumen — 8 Semanas</strong></li>
  <li><strong>Registro de Progreso Semanal</strong></li>
</ul>
<p>Cinco PDF en <strong>español, inglés y francés</strong>, con versión de pantalla y
versión preparada para imprimir.</p>

<h3>Cómo está hecho</h3>
<p>Todas las cifras proceden de fuentes oficiales de acceso público y están
recalculadas. La guía de suplementación dice también lo que <em>no</em> tiene
respaldo, que es la mitad que suele faltar. El registro semanal está pensado
para escribirse a mano: es la parte que convierte ocho semanas sueltas en datos
comparables.</p>

<h3>Lo que no es</h3>
<p>No es una pauta dietética individualizada ni sustituye la atención de un
médico o de un dietista-nutricionista colegiado. No considera patologías. Si
tienes una condición médica, alergia, embarazo o tratamiento en curso,
consúltalo antes con tu profesional sanitario.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS.</em></p>
""",
    "en": """
<p><strong>Five documents for running a full cutting-and-bulking cycle on your own
numbers rather than on borrowed rules.</strong></p>

<h3>What you get</h3>
<ul>
  <li><strong>Quick Guide — Clean Bulk</strong></li>
  <li><strong>Carbohydrate Cycling</strong></li>
  <li><strong>Supplementation Guide</strong></li>
  <li><strong>Cutting + Bulking Plan — 8 Weeks</strong></li>
  <li><strong>Weekly Progress Record</strong></li>
</ul>
<p>Five PDFs in <strong>English, Spanish and French</strong>, with a screen version and a
print-ready version.</p>

<h3>How it is made</h3>
<p>Every figure comes from publicly available official sources and has been
recalculated. The supplementation guide also says what is <em>not</em> supported by
evidence, which is the half usually left out. The weekly record is meant to be
filled in by hand: it is the part that turns eight loose weeks into comparable
data.</p>

<h3>What it is not</h3>
<p>It is not an individualised dietary plan and it does not replace care from a
doctor or a registered dietitian. It does not take pathologies into account. If
you have a medical condition, an allergy, a pregnancy or an ongoing treatment,
check with your health professional first.</p>

<p><em>Digital download. An original work by VILLUMINATIONS.</em></p>
""",
    "fr": """
<p><strong>Cinq documents pour mener un cycle complet de sèche et de prise de masse
avec ses propres chiffres et non avec des règles empruntées.</strong></p>

<h3>Ce que vous recevez</h3>
<ul>
  <li><strong>Guide rapide — Prise de masse propre</strong></li>
  <li><strong>Cyclage des glucides</strong></li>
  <li><strong>Guide de la supplémentation</strong></li>
  <li><strong>Plan Sèche + Prise de masse — 8 semaines</strong></li>
  <li><strong>Relevé de progression hebdomadaire</strong></li>
</ul>
<p>Cinq PDF en <strong>français, espagnol et anglais</strong>, avec une version écran et une
version prête à imprimer.</p>

<h3>Comment c'est fait</h3>
<p>Tous les chiffres proviennent de sources officielles publiques et ont été
recalculés. Le guide de la supplémentation dit aussi ce qui <em>n'est pas</em> étayé,
c'est-à-dire la moitié qui manque d'ordinaire. Le relevé hebdomadaire est prévu
pour être écrit à la main : c'est la partie qui transforme huit semaines éparses
en données comparables.</p>

<h3>Ce que ce n'est pas</h3>
<p>Ce n'est pas un régime individualisé et cela ne remplace pas le suivi d'un
médecin ou d'un diététicien-nutritionniste. Cela ne tient pas compte des
pathologies. Si vous avez une pathologie, une allergie, une grossesse ou un
traitement en cours, consultez d'abord votre professionnel de santé.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS.</em></p>
""",
}

ELITE = {
    "handle": "elite-todo-incluido-coaching",
    "gid": "gid://shopify/Product/7141932204081",
    "titulo": {
        "es": "Elite · Todo Incluido + Coaching",
        "en": "Elite · Everything Included + Coaching",
        "fr": "Elite · Tout inclus + Coaching",
    },
    "es": """
<p><strong>Los once documentos del catálogo de planes, completos.</strong> Alimentación,
entrenamiento, descanso, atención y el seguimiento semanal que los sostiene.</p>

<h3>Qué recibes</h3>
<ul>
  <li><strong>Guía Rápida — Volumen Limpio</strong></li>
  <li><strong>Ciclado de Carbohidratos</strong></li>
  <li><strong>Guía de Suplementación</strong></li>
  <li><strong>Plan Definición + Volumen — 8 Semanas</strong></li>
  <li><strong>Registro de Progreso Semanal</strong></li>
  <li><strong>Dieta Mediterránea — 4 Semanas</strong></li>
  <li><strong>10 Rutinas HIIT</strong></li>
  <li><strong>Plan de Entrenamiento — 8 Semanas</strong></li>
  <li><strong>Meditación y Mindfulness — 21 Días</strong></li>
  <li><strong>Protocolo de Sueño</strong></li>
  <li><strong>Coaching Semanal 1 a 1</strong></li>
</ul>
<p>Once PDF en <strong>español, inglés y francés</strong> —treinta y tres documentos en
total—, con versión de pantalla y versión preparada para imprimir.</p>

<h3>Cómo está hecho</h3>
<p>Todas las cifras proceden de fuentes oficiales de acceso público y están
recalculadas y comprobadas. Es material de referencia y de método: dice de
dónde sale cada número y dónde deja de haber evidencia. El protocolo de sueño y
el cuaderno de meditación están escritos igual que el resto — sin promesas y
con instrucciones que se pueden ejecutar el mismo día.</p>

<h3>Lo que no es</h3>
<p>No es una pauta dietética individualizada ni sustituye la atención de un
médico, un psicólogo o un dietista-nutricionista colegiado. No considera
patologías. Si tienes una condición médica, alergia, embarazo o tratamiento en
curso, consúltalo antes con tu profesional sanitario.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS.</em></p>
""",
    "en": """
<p><strong>All eleven documents in the plans catalogue, complete.</strong> Food, training,
rest, attention and the weekly follow-up that holds them together.</p>

<h3>What you get</h3>
<ul>
  <li><strong>Quick Guide — Clean Bulk</strong></li>
  <li><strong>Carbohydrate Cycling</strong></li>
  <li><strong>Supplementation Guide</strong></li>
  <li><strong>Cutting + Bulking Plan — 8 Weeks</strong></li>
  <li><strong>Weekly Progress Record</strong></li>
  <li><strong>Mediterranean Diet — 4 Weeks</strong></li>
  <li><strong>10 HIIT Sessions</strong></li>
  <li><strong>Training Plan — 8 Weeks</strong></li>
  <li><strong>Meditation and Mindfulness — 21 Days</strong></li>
  <li><strong>Sleep Protocol</strong></li>
  <li><strong>Weekly One-to-One Coaching</strong></li>
</ul>
<p>Eleven PDFs in <strong>English, Spanish and French</strong> —thirty-three documents in
all— with a screen version and a print-ready version.</p>

<h3>How it is made</h3>
<p>Every figure comes from publicly available official sources and has been
recalculated and checked. This is reference and method material: it says where
each number comes from and where the evidence runs out. The sleep protocol and
the meditation notebook are written like the rest — no promises, and
instructions you can carry out the same day.</p>

<h3>What it is not</h3>
<p>It is not an individualised dietary plan and it does not replace care from a
registered doctor, psychologist or dietitian. It does not take pathologies into
account. If you have a medical condition, an allergy, a pregnancy or an ongoing
treatment, check with your health professional first.</p>

<p><em>Digital download. An original work by VILLUMINATIONS.</em></p>
""",
    "fr": """
<p><strong>Les onze documents du catalogue de plans, au complet.</strong> Alimentation,
entraînement, repos, attention et le suivi hebdomadaire qui les tient ensemble.</p>

<h3>Ce que vous recevez</h3>
<ul>
  <li><strong>Guide rapide — Prise de masse propre</strong></li>
  <li><strong>Cyclage des glucides</strong></li>
  <li><strong>Guide de la supplémentation</strong></li>
  <li><strong>Plan Sèche + Prise de masse — 8 semaines</strong></li>
  <li><strong>Relevé de progression hebdomadaire</strong></li>
  <li><strong>Régime méditerranéen — 4 semaines</strong></li>
  <li><strong>10 séances HIIT</strong></li>
  <li><strong>Plan d'entraînement — 8 semaines</strong></li>
  <li><strong>Méditation et pleine conscience — 21 jours</strong></li>
  <li><strong>Protocole de sommeil</strong></li>
  <li><strong>Coaching hebdomadaire en tête-à-tête</strong></li>
</ul>
<p>Onze PDF en <strong>français, espagnol et anglais</strong> —trente-trois documents en
tout—, avec une version écran et une version prête à imprimer.</p>

<h3>Comment c'est fait</h3>
<p>Tous les chiffres proviennent de sources officielles publiques et ont été
recalculés et contrôlés. C'est du matériau de référence et de méthode : il dit
d'où vient chaque nombre et où s'arrête la preuve. Le protocole de sommeil et le
cahier de méditation sont écrits comme le reste — sans promesses, et avec des
instructions exécutables le jour même.</p>

<h3>Ce que ce n'est pas</h3>
<p>Ce n'est pas un régime individualisé et cela ne remplace pas le suivi d'un
médecin, d'un psychologue ou d'un diététicien-nutritionniste. Cela ne tient pas
compte des pathologies. Si vous avez une pathologie, une allergie, une grossesse
ou un traitement en cours, consultez d'abord votre professionnel de santé.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS.</em></p>
""",
}

# --------------------------------------------------------------------------
# Los dos libros que ya tienen ficha en la tienda. Las cifras —capítulos,
# láminas, páginas— salen de los PDF auditados; build.py se niega a componer
# un libro cuyo texto prometa más láminas de las que dibuja, así que aquí se
# pueden copiar sin miedo.
# --------------------------------------------------------------------------

ZODIACAL = {
    "handle": "el-zodiaco",
    "gid": "gid://shopify/Product/7139483910193",
    "titulo": {
        "es": "Códice Zodiacal",
        "en": "Zodiacal Codex",
        "fr": "Codex Zodiacal",
    },
    "es": """
<p><strong>Los doce signos como mapa del carácter, del cuerpo y del trabajo
interior.</strong> Treinta y un capítulos, diez láminas dibujadas para este libro y
un año de práctica escrita.</p>

<h3>Qué contiene</h3>
<ul>
  <li>Los doce signos con sus <strong>once claves</strong>: correspondencias completas, símbolo, fuerza, sombra, eje, decanatos, cuerpo, mesa, práctica y relaciones.</li>
  <li>La tabla de los <strong>treinta y seis decanatos</strong>, que explica por qué tanta gente no se reconoce en la descripción general de su signo.</li>
  <li>Las <strong>cuatro dignidades esenciales</strong> con el grado exacto de cada exaltación y cada caída.</li>
  <li>Los <strong>sesenta términos egipcios</strong>, la tabla más fina y más olvidada del sistema clásico.</li>
  <li>Las <strong>veintiocho mansiones lunares</strong>, con su aritmética y con una explicación honesta de por qué las listas de nombres no coinciden entre tradiciones.</li>
  <li>La <strong>precesión de los equinoccios</strong> con sus cifras reales, y de dónde salen las «eras».</li>
  <li>Un <strong>programa de doce meses</strong> con una práctica concreta por signo y un registro para escribir lo que observas.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>144 páginas</strong>. Incluye las tres ediciones —<strong>español (144 pp.),
inglés (145 pp.) y francés (149 pp.)</strong>— con marcadores de navegación y
vocabulario final.</p>

<h3>Cómo leerlo</h3>
<p>La astrología que aquí se practica es un <em>lenguaje simbólico</em>: una manera
antigua y muy afinada de nombrar temperamentos, tensiones y ciclos. No es una
ciencia predictiva. Nada de lo que contiene anuncia hechos futuros, diagnostica
enfermedades ni sustituye la atención de un médico, un psicólogo o un
dietista-nutricionista colegiado.</p>

<p>El material del que parte pertenece a la <strong>tradición común</strong>: las
correspondencias clásicas, los regentes planetarios y las tablas de decanatos
se transmiten por escrito desde hace más de dos milenios y no son propiedad de
nadie. La redacción, la estructura, las prácticas, las fichas y las
ilustraciones son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>The twelve signs as a map of character, of the body and of inner work.</strong>
Thirty-one chapters, ten plates drawn for this book and a year of written
practice.</p>

<h3>What it contains</h3>
<ul>
  <li>The twelve signs with their <strong>eleven keys</strong>: complete correspondences, symbol, strength, shadow, axis, decans, body, table, practice and relations.</li>
  <li>The table of the <strong>thirty-six decans</strong>, which explains why so many people do not recognise themselves in the general description of their sign.</li>
  <li>The <strong>four essential dignities</strong> with the exact degree of each exaltation and each fall.</li>
  <li>The <strong>sixty Egyptian terms</strong>, the finest and most forgotten table of the classical system.</li>
  <li>The <strong>twenty-eight lunar mansions</strong>, with their arithmetic and an honest explanation of why the lists of names do not agree between traditions.</li>
  <li>The <strong>precession of the equinoxes</strong> with its real figures, and where the «ages» come from.</li>
  <li>A <strong>twelve-month programme</strong> with one concrete practice per sign and a record for writing down what you observe.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>145 pages</strong>. Includes all three editions —<strong>English (145 pp.),
Spanish (144 pp.) and French (149 pp.)</strong>— with navigation bookmarks and a
closing vocabulary.</p>

<h3>How to read it</h3>
<p>The astrology practised here is a <em>symbolic language</em>: an old and very finely
tuned way of naming temperaments, tensions and cycles. It is not a predictive
science. Nothing in it announces future events, diagnoses illnesses or replaces
the care of a registered doctor, psychologist or dietitian.</p>

<p>The material it starts from belongs to the <strong>common tradition</strong>: the classical
correspondences, the planetary rulers and the tables of decans have been
transmitted in writing for more than two millennia and are nobody's property.
The writing, the structure, the practices, the entries and the illustrations
are original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>Les douze signes comme carte du caractère, du corps et du travail
intérieur.</strong> Trente et un chapitres, dix planches dessinées pour ce livre et une
année de pratique écrite.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>Les douze signes avec leurs <strong>onze clés</strong> : correspondances complètes, symbole, force, ombre, axe, décans, corps, table, pratique et relations.</li>
  <li>La table des <strong>trente-six décans</strong>, qui explique pourquoi tant de gens ne se reconnaissent pas dans la description générale de leur signe.</li>
  <li>Les <strong>quatre dignités essentielles</strong> avec le degré exact de chaque exaltation et de chaque chute.</li>
  <li>Les <strong>soixante termes égyptiens</strong>, la table la plus fine et la plus oubliée du système classique.</li>
  <li>Les <strong>vingt-huit demeures lunaires</strong>, avec leur arithmétique et une explication honnête de la raison pour laquelle les listes de noms ne concordent pas d'une tradition à l'autre.</li>
  <li>La <strong>précession des équinoxes</strong> avec ses chiffres réels, et d'où sortent les « ères ».</li>
  <li>Un <strong>programme de douze mois</strong> avec une pratique concrète par signe et un registre où écrire ce que vous observez.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>149 pages</strong>. Comprend les trois éditions —<strong>français (149 p.),
espagnol (144 p.) et anglais (145 p.)</strong>— avec signets de navigation et
vocabulaire final.</p>

<h3>Comment le lire</h3>
<p>L'astrologie que l'on pratique ici est un <em>langage symbolique</em> : une manière
ancienne et très affinée de nommer des tempéraments, des tensions et des cycles.
Ce n'est pas une science prédictive. Rien de ce qu'il contient n'annonce des
faits à venir, ne diagnostique de maladies ni ne remplace le suivi d'un médecin,
d'un psychologue ou d'un diététicien-nutritionniste.</p>

<p>Le matériau dont il part appartient à la <strong>tradition commune</strong> : les
correspondances classiques, les régents planétaires et les tables de décans se
transmettent par écrit depuis plus de deux millénaires et n'appartiennent à
personne. La rédaction, la structure, les pratiques, les fiches et les
illustrations sont un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

INVOCACIONES = {
    "handle": "las-conjuraciones-y-la-invocacion-del-sello-salomon",
    "gid": "gid://shopify/Product/7139485974577",
    "titulo": {
        "es": "Códice de las Invocaciones",
        "en": "Codex of Invocations",
        "fr": "Codex des Invocations",
    },
    "es": """
<p><strong>Manual de práctica ritual: el círculo, las armas, los nombres y el rito
diario.</strong> Veinticinco capítulos, ocho láminas dibujadas para esta edición y un
programa de doce meses.</p>

<h3>Qué contiene</h3>
<ul>
  <li>El <strong>rito diario</strong> completo, de siete a diez minutos, con sus cuatro movimientos y las fórmulas silabeadas para poder vocalizarlas.</li>
  <li>El <strong>círculo</strong>, las <strong>cuatro armas</strong> y la ceremonia mínima de dedicación, con el orden en que se dedican y por qué.</li>
  <li>Los <strong>siete cuadrados planetarios</strong>, las <strong>horas planetarias</strong> y las veintidós letras, con su aritmética comprobable.</li>
  <li>La <strong>operación planetaria</strong> y la <strong>operación de examen</strong>, paso a paso, con sus errores frecuentes y con la señal de cuándo parar.</li>
  <li>Un capítulo entero sobre <strong>el cierre</strong>, incluido el cierre de emergencia de veinte segundos.</li>
  <li>El <strong>diario de práctica</strong>: qué se anota, cómo se revisa cada semana, cada trimestre y cada año.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>88 páginas</strong>. Incluye las tres ediciones —<strong>español (88 pp.),
inglés (91 pp.) y francés (92 pp.)</strong>— con marcadores de navegación y
vocabulario del oficio.</p>

<h3>Cómo leerlo</h3>
<p>El libro contesta de frente a la pregunta que plantea su título, y su respuesta
es que lo que acude es una parte del operante que normalmente no está
disponible. No hay pactos, ni influencia sobre terceros, ni conocimiento
secreto. Personificar contenidos internos es una técnica potente y no es inocua
para todo el mundo: si tienes antecedentes de episodios psicóticos, de
disociación o de trastorno de identidad, o estás en una crisis aguda, esta clase
de práctica debe hacerse con acompañamiento profesional.</p>

<p>El material del que parte pertenece a la <strong>tradición común</strong> y a obras de
dominio público. La redacción, la estructura, las fórmulas en castellano, el
encuadre, las ocho láminas y los ejercicios de registro son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>A manual of ritual practice: the circle, the weapons, the names and the
daily rite.</strong> Twenty-five chapters, eight plates drawn for this edition and a
twelve-month programme.</p>

<h3>What it contains</h3>
<ul>
  <li>The complete <strong>daily rite</strong>, seven to ten minutes, with its four movements and the formulae syllabified so they can be vocalised.</li>
  <li>The <strong>circle</strong>, the <strong>four weapons</strong> and the minimum ceremony of dedication, with the order in which they are dedicated and why.</li>
  <li>The <strong>seven planetary squares</strong>, the <strong>planetary hours</strong> and the twenty-two letters, with their checkable arithmetic.</li>
  <li>The <strong>planetary operation</strong> and the <strong>examination operation</strong>, step by step, with their frequent errors and the sign of when to stop.</li>
  <li>A whole chapter on <strong>closing</strong>, including the twenty-second emergency closing.</li>
  <li>The <strong>practice journal</strong>: what gets written down, how it is reviewed each week, each quarter and each year.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>91 pages</strong>. Includes all three editions —<strong>English (91 pp.),
Spanish (88 pp.) and French (92 pp.)</strong>— with navigation bookmarks and a
vocabulary of the trade.</p>

<h3>How to read it</h3>
<p>The book answers head-on the question its title raises, and its answer is that
what comes is a part of the operator that is not normally available. There are
no pacts, no influence over third parties and no secret knowledge. Personifying
internal contents is a powerful technique and it is not harmless for everybody:
if you have a history of psychotic episodes, of dissociation or of an identity
disorder, or you are in an acute crisis, this kind of practice must be done with
professional support.</p>

<p>The material it starts from belongs to the <strong>common tradition</strong> and to works in
the public domain. The writing, the structure, the formulae in the vernacular,
the framing, the eight plates and the recording exercises are original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>Manuel de pratique rituelle : le cercle, les armes, les noms et le rite
quotidien.</strong> Vingt-cinq chapitres, huit planches dessinées pour cette édition et
un programme de douze mois.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>Le <strong>rite quotidien</strong> complet, de sept à dix minutes, avec ses quatre mouvements et les formules syllabées pour pouvoir les vocaliser.</li>
  <li>Le <strong>cercle</strong>, les <strong>quatre armes</strong> et la cérémonie minimale de dédicace, avec l'ordre dans lequel on les dédie et pourquoi.</li>
  <li>Les <strong>sept carrés planétaires</strong>, les <strong>heures planétaires</strong> et les vingt-deux lettres, avec leur arithmétique vérifiable.</li>
  <li>L'<strong>opération planétaire</strong> et l'<strong>opération d'examen</strong>, pas à pas, avec leurs erreurs fréquentes et le signal indiquant quand s'arrêter.</li>
  <li>Un chapitre entier sur <strong>la clôture</strong>, y compris la clôture d'urgence de vingt secondes.</li>
  <li>Le <strong>journal de pratique</strong> : ce que l'on note, comment on le relit chaque semaine, chaque trimestre et chaque année.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>92 pages</strong>. Comprend les trois éditions —<strong>français (92 p.),
espagnol (88 p.) et anglais (91 p.)</strong>— avec signets de navigation et
vocabulaire du métier.</p>

<h3>Comment le lire</h3>
<p>Le livre répond de front à la question que pose son titre, et sa réponse est que
ce qui vient est une part de l'opérant qui n'est pas ordinairement disponible.
Il n'y a ni pactes, ni influence sur des tiers, ni savoir secret. Personnifier
des contenus internes est une technique puissante et elle n'est pas anodine pour
tout le monde : si vous avez des antécédents d'épisodes psychotiques, de
dissociation ou de trouble de l'identité, ou si vous traversez une crise aiguë,
ce genre de pratique doit se faire avec un accompagnement professionnel.</p>

<p>Le matériau dont il part appartient à la <strong>tradition commune</strong> et à des œuvres
du domaine public. La rédaction, la structure, les formules en langue vulgaire,
le cadrage, les huit planches et les exercices de relevé sont un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

FICHAS = [BASICO, PRO, ELITE, ZODIACAL, INVOCACIONES]
IDIOMAS = ("es", "en", "fr")
