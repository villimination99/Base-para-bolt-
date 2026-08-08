# -*- coding: utf-8 -*-
"""
VILLUMINATIONS — Fichas de los seis códices que faltaban en la tienda
---------------------------------------------------------------------
El catálogo tiene ocho libros y la tienda solo vendía dos. Aquí están los seis
restantes, con el mismo criterio que las fichas de descripciones.py: cifras
sacadas de los PDF auditados, ninguna promesa de resultado, el aviso de lectura
resumido antes de pagar y la base documental dicha con precisión.

Esa última parte importa más de lo que parece, y por eso cada ficha la dice de
una forma distinta. Los cuatro libros de cuerpo —Mesa, Carga, Descanso,
Voluntad— parten de material del Gobierno de los Estados Unidos, que no está
sujeto a derechos de autor conforme al 17 U.S.C. § 105: es una norma concreta y
se cita como tal. Los dos de trabajo interior —Arcanos y Sí Mismo— no se apoyan
en ninguna norma, sino en una tradición que lleva siglos imprimiéndose en obras
de dominio público. Las dos cosas son ciertas y no son la misma; confundirlas
sería inventarse una cobertura legal que uno de los dos grupos no tiene.

El campo «gid» se rellena cuando el producto existe. Hasta entonces va a None y
publicar.py sabe que hay que crearlo en lugar de actualizarlo.
"""

MESA = {
    "handle": "codice-de-la-mesa",
    "portada": "codice-mesa.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice de la Mesa",
        "en": "Codex of the Table",
        "fr": "Codex de la Table",
    },
    "es": """
<p><strong>Nutrición con las dos columnas de la tabla: lo que hay que tomar, lo que
conviene no pasar y de dónde sale cada cifra.</strong> Veinte capítulos, siete láminas
y un cuaderno de cuatro semanas.</p>

<h3>Qué contiene</h3>
<ul>
  <li>Las <strong>cuatro letras</strong> de las tablas de referencia que casi nadie explica, y qué significa cada una.</li>
  <li>El gasto de un día por partes, y el <strong>reparto de la energía</strong> entre los tres macronutrientes.</li>
  <li>Proteína como <strong>suelo y no como objetivo</strong>; los ciento treinta gramos de hidratos que pide el cerebro; por qué el mínimo de grasa es del veinte por ciento.</li>
  <li>Los <strong>diecinueve micronutrientes</strong> con sus dos columnas —lo recomendado y el límite superior— y cuáles admiten error y cuáles no.</li>
  <li><strong>Sodio y potasio</strong> leídos juntos, que es la única forma de que digan algo.</li>
  <li>Cómo se lee una <strong>etiqueta</strong>, con la tolerancia legal dicha en fracciones y las trampas más frecuentes.</li>
  <li>Qué se puede afirmar y <strong>qué se pidió y fue rechazado</strong>: el registro europeo de declaraciones de salud, con las aprobadas en su redacción oficial.</li>
  <li>Temperaturas de seguridad alimentaria y las cuatro situaciones en las que la tabla cambia.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>78 páginas</strong>. Incluye las tres ediciones —<strong>español (78 pp.),
inglés (76 pp.) y francés (80 pp.)</strong>— con marcadores de navegación y glosario.</p>

<h3>Cómo leerlo</h3>
<p>Es un libro de <em>referencia nutricional</em>, no un plan dietético personalizado.
Las cifras que recoge son promedios de población sana y hay que ajustarlas a tu
caso. Nada de lo que contiene diagnostica ni trata ninguna enfermedad, y no
sustituye la atención de un médico o de un dietista-nutricionista colegiado. Si
tienes una patología, alergia, embarazo o tratamiento en curso, consúltalo antes
con tu profesional sanitario.</p>

<p>Las tablas de referencia de nutrientes, los rangos de macronutrientes y los
criterios de inocuidad alimentaria de los que parte están publicados por
organismos del Gobierno de los Estados Unidos y <strong>no están sujetos a derechos de
autor conforme al 17 U.S.C. § 105</strong>. La redacción, la estructura, las fichas, las
comprobaciones y las ilustraciones son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>Nutrition with both columns of the table: what you have to get, what you had
better not exceed, and where every figure comes from.</strong> Twenty chapters, seven
plates and a four-week notebook.</p>

<h3>What it contains</h3>
<ul>
  <li>The <strong>four letters</strong> of the reference tables that hardly anybody explains, and what each one means.</li>
  <li>A day's expenditure broken down, and the <strong>division of energy</strong> between the three macronutrients.</li>
  <li>Protein as a <strong>floor and not a target</strong>; the hundred and thirty grams of carbohydrate the brain asks for; why the fat minimum is twenty per cent.</li>
  <li>The <strong>nineteen micronutrients</strong> with their two columns —the recommendation and the upper limit— and which of them tolerate error and which do not.</li>
  <li><strong>Sodium and potassium</strong> read together, which is the only way they say anything.</li>
  <li>How to read a <strong>label</strong>, with the legal tolerance given in fractions and the commonest traps.</li>
  <li>What may be claimed and <strong>what was applied for and refused</strong>: the European register of health claims, with the authorised ones in their official wording.</li>
  <li>Food safety temperatures and the four situations in which the table changes.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>76 pages</strong>. Includes all three editions —<strong>English (76 pp.),
Spanish (78 pp.) and French (80 pp.)</strong>— with navigation bookmarks and a glossary.</p>

<h3>How to read it</h3>
<p>It is a book of <em>nutritional reference</em>, not a personalised diet plan. The
figures it gathers are averages for a healthy population and have to be adjusted
to your case. Nothing in it diagnoses or treats any illness, and it does not
replace care from a doctor or a registered dietitian. If you have a medical
condition, an allergy, a pregnancy or an ongoing treatment, check with your
health professional first.</p>

<p>The nutrient reference tables, the macronutrient ranges and the food safety
criteria it starts from are published by agencies of the United States
Government and are <strong>not subject to copyright under 17 U.S.C. § 105</strong>. The
writing, the structure, the entries, the checks and the illustrations are
original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>La nutrition avec les deux colonnes de la table : ce qu'il faut prendre, ce
qu'il vaut mieux ne pas dépasser et d'où sort chaque chiffre.</strong> Vingt chapitres,
sept planches et un cahier de quatre semaines.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>Les <strong>quatre lettres</strong> des tables de référence que presque personne n'explique, et ce que signifie chacune.</li>
  <li>La dépense d'une journée détaillée, et la <strong>répartition de l'énergie</strong> entre les trois macronutriments.</li>
  <li>Les protéines comme <strong>plancher et non comme objectif</strong> ; les cent trente grammes de glucides que réclame le cerveau ; pourquoi le minimum de lipides est de vingt pour cent.</li>
  <li>Les <strong>dix-neuf micronutriments</strong> avec leurs deux colonnes —la recommandation et la limite supérieure— et lesquels tolèrent l'erreur et lesquels non.</li>
  <li><strong>Sodium et potassium</strong> lus ensemble, seule façon qu'ils disent quelque chose.</li>
  <li>Comment lire une <strong>étiquette</strong>, avec la tolérance légale donnée en fractions et les pièges les plus fréquents.</li>
  <li>Ce que l'on peut affirmer et <strong>ce qui a été demandé et refusé</strong> : le registre européen des allégations de santé, avec les autorisées dans leur rédaction officielle.</li>
  <li>Les températures de sécurité alimentaire et les quatre situations où la table change.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>80 pages</strong>. Comprend les trois éditions —<strong>français (80 p.),
espagnol (78 p.) et anglais (76 p.)</strong>— avec signets de navigation et glossaire.</p>

<h3>Comment le lire</h3>
<p>C'est un livre de <em>référence nutritionnelle</em>, non un régime personnalisé. Les
chiffres qu'il rassemble sont des moyennes de population en bonne santé et
doivent être ajustés à votre cas. Rien de ce qu'il contient ne diagnostique ni ne
traite une maladie, et cela ne remplace pas le suivi d'un médecin ou d'un
diététicien-nutritionniste. Si vous avez une pathologie, une allergie, une
grossesse ou un traitement en cours, consultez d'abord votre professionnel de
santé.</p>

<p>Les tables de référence des nutriments, les fourchettes de macronutriments et les
critères de sécurité alimentaire dont il part sont publiés par des organismes du
Gouvernement des États-Unis et <strong>ne sont pas soumis au droit d'auteur en vertu du
17 U.S.C. § 105</strong>. La rédaction, la structure, les fiches, les contrôles et les
illustrations sont un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

CARGA = {
    "handle": "codice-de-la-carga",
    "portada": "codice-carga.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice de la Carga",
        "en": "Codex of the Load",
        "fr": "Codex de la Charge",
    },
    "es": """
<p><strong>La dosis oficial de actividad, la escala que la mide, la ecuación de levantar
y lo que le pasa a un cuerpo sin peso.</strong> Diecinueve capítulos, siete láminas y un
cuaderno de carga.</p>

<h3>Qué contiene</h3>
<ul>
  <li><strong>Existe una dosis y está escrita</strong>: cuánta actividad, de qué clase y con qué reparto, según las guías públicas.</li>
  <li>La <strong>forma de la curva</strong> —qué se gana en cada tramo— y la moneda con la que se paga la intensidad.</li>
  <li>Los <strong>ocho patrones</strong> de movimiento y las <strong>seis variables</strong> con las que se programa una semana.</li>
  <li>La <strong>ecuación del levantamiento</strong> del NIOSH, con sus factores desarrollados uno a uno y la constante de 23 kg.</li>
  <li>Qué pasa cuando se quita el peso: el experimento del reposo, la pérdida y la <strong>recuperación</strong>.</li>
  <li>Cómo se distingue el <strong>dolor</strong> que informa del que avisa.</li>
  <li>Entrenar <strong>a partir de los sesenta</strong>, y una batería pública para medirse.</li>
  <li>Un capítulo de <strong>cómo comprobarlo tú mismo</strong>: dónde está cada fuente y cómo se verifica.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>70 páginas</strong>. Incluye las tres ediciones —<strong>español (70 pp.),
inglés (70 pp.) y francés (73 pp.)</strong>— con marcadores de navegación y glosario.</p>

<h3>Cómo leerlo</h3>
<p>Es un libro sobre <em>carga y adaptación</em>: sobre cuánto trabajo se puede acumular y
a qué ritmo. El entrenamiento con cargas conlleva riesgo de lesión. Nada de lo
que contiene diagnostica ni trata ninguna dolencia, y no sustituye la valoración
de un profesional sanitario colegiado ni la supervisión presencial de un
entrenador cualificado.</p>

<p>Los manuales de acondicionamiento físico y los criterios de manejo de cargas de
los que parte —entre ellos el FM 7-22 y las guías del NIOSH— están publicados por
organismos del Gobierno de los Estados Unidos y <strong>no están sujetos a derechos de
autor conforme al 17 U.S.C. § 105</strong>. La redacción, la estructura, las tablas y las
ilustraciones son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>The official dose of activity, the scale that measures it, the lifting equation
and what happens to a body with the weight taken away.</strong> Nineteen chapters, seven
plates and a load notebook.</p>

<h3>What it contains</h3>
<ul>
  <li><strong>There is a dose and it is written down</strong>: how much activity, of what kind and in what distribution, according to the public guidelines.</li>
  <li>The <strong>shape of the curve</strong> —what is gained in each stretch— and the currency intensity is paid in.</li>
  <li>The <strong>eight movement patterns</strong> and the <strong>six variables</strong> a week is programmed with.</li>
  <li>The NIOSH <strong>lifting equation</strong>, with its factors developed one by one and the 23 kg constant.</li>
  <li>What happens when the weight is removed: the bed-rest experiment, the loss and the <strong>recovery</strong>.</li>
  <li>How to tell the <strong>pain</strong> that informs from the pain that warns.</li>
  <li>Training <strong>from sixty onwards</strong>, and a public battery for measuring yourself.</li>
  <li>A chapter on <strong>how to check it yourself</strong>: where each source is and how it is verified.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>70 pages</strong>. Includes all three editions —<strong>English (70 pp.),
Spanish (70 pp.) and French (73 pp.)</strong>— with navigation bookmarks and a glossary.</p>

<h3>How to read it</h3>
<p>It is a book about <em>load and adaptation</em>: about how much work can be accumulated
and at what rate. Training with loads carries a risk of injury. Nothing in it
diagnoses or treats any complaint, and it does not replace assessment by a
registered health professional or in-person supervision by a qualified coach.</p>

<p>The physical conditioning manuals and load-handling criteria it starts from
—among them FM 7-22 and the NIOSH guidelines— are published by agencies of the
United States Government and are <strong>not subject to copyright under 17 U.S.C. §
105</strong>. The writing, the structure, the tables and the illustrations are original
work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>La dose officielle d'activité, l'échelle qui la mesure, l'équation du levage et
ce qui arrive à un corps privé de charge.</strong> Dix-neuf chapitres, sept planches et un
cahier de la charge.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li><strong>Il existe une dose et elle est écrite</strong> : combien d'activité, de quelle sorte et selon quelle répartition, d'après les guides publics.</li>
  <li>La <strong>forme de la courbe</strong> —ce que l'on gagne à chaque tronçon— et la monnaie avec laquelle se paie l'intensité.</li>
  <li>Les <strong>huit schémas</strong> de mouvement et les <strong>six variables</strong> avec lesquelles on programme une semaine.</li>
  <li>L'<strong>équation du levage</strong> du NIOSH, avec ses facteurs développés un à un et la constante de 23 kg.</li>
  <li>Ce qui se passe quand on retire la charge : l'expérience de l'alitement, la perte et la <strong>récupération</strong>.</li>
  <li>Comment distinguer la <strong>douleur</strong> qui renseigne de celle qui avertit.</li>
  <li>S'entraîner <strong>à partir de soixante ans</strong>, et une batterie publique pour se mesurer.</li>
  <li>Un chapitre sur <strong>comment le vérifier soi-même</strong> : où se trouve chaque source et comment on la contrôle.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>73 pages</strong>. Comprend les trois éditions —<strong>français (73 p.),
espagnol (70 p.) et anglais (70 p.)</strong>— avec signets de navigation et glossaire.</p>

<h3>Comment le lire</h3>
<p>C'est un livre sur la <em>charge et l'adaptation</em> : sur la quantité de travail que
l'on peut accumuler et à quel rythme. L'entraînement avec charges comporte un
risque de blessure. Rien de ce qu'il contient ne diagnostique ni ne traite un
mal, et cela ne remplace ni l'évaluation d'un professionnel de santé diplômé ni
la supervision en présentiel d'un entraîneur qualifié.</p>

<p>Les manuels de conditionnement physique et les critères de manutention dont il
part —dont le FM 7-22 et les guides du NIOSH— sont publiés par des organismes du
Gouvernement des États-Unis et <strong>ne sont pas soumis au droit d'auteur en vertu du
17 U.S.C. § 105</strong>. La rédaction, la structure, les tables et les illustrations sont
un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

DESCANSO = {
    "handle": "codice-del-descanso",
    "portada": "codice-descanso.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice del Descanso",
        "en": "Codex of Rest",
        "fr": "Codex du Repos",
    },
    "es": """
<p><strong>La arquitectura de una noche, la deuda que deja una semana corta y la
diferencia entre descansar y descargarse.</strong> Quince capítulos, seis láminas y un
cuaderno del descanso.</p>

<h3>Qué contiene</h3>
<ul>
  <li>El <strong>reloj interno</strong> y la arquitectura de una noche, fase por fase.</li>
  <li>La <strong>deuda</strong> de sueño: cómo se acumula, qué se recupera y qué no.</li>
  <li>La <strong>cuenta atrás</strong> de las horas previas, con cafeína, alcohol y nicotina tratados por separado y con sus tiempos.</li>
  <li>La <strong>habitación</strong>: temperatura, luz y ruido, con las cifras que sí están medidas.</li>
  <li>La <strong>siesta bien hecha</strong>, con su duración y su hora.</li>
  <li>Qué funciona de verdad <strong>cuando el sueño no llega</strong>, y en qué orden se prueba.</li>
  <li><strong>Turnos, viajes y noches rotas</strong>: qué se puede hacer cuando el horario no se elige.</li>
  <li>Sueño y entrenamiento <strong>en las dos direcciones</strong>, y qué se puede comprar de la recuperación y qué no.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>53 páginas</strong>. Incluye las tres ediciones —<strong>español (53 pp.),
inglés (52 pp.) y francés (55 pp.)</strong>— con marcadores de navegación y glosario.</p>

<h3>Cómo leerlo</h3>
<p>Es un libro sobre <em>higiene del sueño para personas sanas</em>. El insomnio
persistente, la apnea y la somnolencia diurna excesiva son cuadros clínicos:
nada de lo que contiene los diagnostica ni los trata, y no sustituye la atención
de un médico. Si llevas más de tres meses durmiendo mal, o si alguien te ha dicho
que dejas de respirar mientras duermes, el libro tiene un capítulo entero
dedicado a decirte que eso no es higiene del sueño y adónde hay que ir.</p>

<p>Las recomendaciones de duración, los datos de ritmo circadiano y las guías de
higiene del sueño de las que parte están publicadas por organismos del Gobierno
de los Estados Unidos y <strong>no están sujetas a derechos de autor conforme al 17
U.S.C. § 105</strong>. La redacción, la estructura, los protocolos y las ilustraciones
son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>The architecture of a night, the debt a short week leaves behind and the
difference between resting and merely switching off.</strong> Fifteen chapters, six
plates and a rest notebook.</p>

<h3>What it contains</h3>
<ul>
  <li>The <strong>internal clock</strong> and the architecture of a night, phase by phase.</li>
  <li>The sleep <strong>debt</strong>: how it accumulates, what is recovered and what is not.</li>
  <li>The <strong>countdown</strong> of the preceding hours, with caffeine, alcohol and nicotine treated separately and with their timings.</li>
  <li>The <strong>bedroom</strong>: temperature, light and noise, with the figures that have actually been measured.</li>
  <li>The <strong>nap done properly</strong>, with its length and its hour.</li>
  <li>What really works <strong>when sleep does not come</strong>, and in what order to try it.</li>
  <li><strong>Shifts, travel and broken nights</strong>: what can be done when the timetable is not yours to choose.</li>
  <li>Sleep and training <strong>in both directions</strong>, and what of recovery can be bought and what cannot.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>52 pages</strong>. Includes all three editions —<strong>English (52 pp.),
Spanish (53 pp.) and French (55 pp.)</strong>— with navigation bookmarks and a glossary.</p>

<h3>How to read it</h3>
<p>It is a book about <em>sleep hygiene for healthy people</em>. Persistent insomnia,
apnoea and excessive daytime sleepiness are clinical conditions: nothing in it
diagnoses or treats them, and it does not replace the care of a doctor. If you
have been sleeping badly for more than three months, or somebody has told you
that you stop breathing in your sleep, the book has a whole chapter devoted to
telling you that this is not sleep hygiene and where to go instead.</p>

<p>The duration recommendations, the circadian rhythm data and the sleep hygiene
guidelines it starts from are published by agencies of the United States
Government and are <strong>not subject to copyright under 17 U.S.C. § 105</strong>. The
writing, the structure, the protocols and the illustrations are original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>L'architecture d'une nuit, la dette que laisse une semaine trop courte et la
différence entre se reposer et simplement décrocher.</strong> Quinze chapitres, six
planches et un cahier du repos.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>L'<strong>horloge interne</strong> et l'architecture d'une nuit, phase par phase.</li>
  <li>La <strong>dette</strong> de sommeil : comment elle s'accumule, ce qui se récupère et ce qui ne se récupère pas.</li>
  <li>Le <strong>compte à rebours</strong> des heures qui précèdent, avec la caféine, l'alcool et la nicotine traités séparément et avec leurs délais.</li>
  <li>La <strong>chambre</strong> : température, lumière et bruit, avec les chiffres qui ont réellement été mesurés.</li>
  <li>La <strong>sieste bien faite</strong>, avec sa durée et son heure.</li>
  <li>Ce qui marche vraiment <strong>quand le sommeil ne vient pas</strong>, et dans quel ordre l'essayer.</li>
  <li><strong>Postes, voyages et nuits hachées</strong> : ce que l'on peut faire quand l'horaire ne se choisit pas.</li>
  <li>Sommeil et entraînement <strong>dans les deux sens</strong>, et ce qui s'achète de la récupération et ce qui ne s'achète pas.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>55 pages</strong>. Comprend les trois éditions —<strong>français (55 p.),
espagnol (53 p.) et anglais (52 p.)</strong>— avec signets de navigation et glossaire.</p>

<h3>Comment le lire</h3>
<p>C'est un livre sur l'<em>hygiène du sommeil pour personnes en bonne santé</em>.
L'insomnie persistante, l'apnée et la somnolence diurne excessive sont des
tableaux cliniques : rien de ce qu'il contient ne les diagnostique ni ne les
traite, et cela ne remplace pas le suivi d'un médecin. Si vous dormez mal depuis
plus de trois mois, ou si l'on vous a dit que vous cessiez de respirer en
dormant, le livre consacre un chapitre entier à vous dire que ce n'est pas de
l'hygiène du sommeil et où il faut aller.</p>

<p>Les recommandations de durée, les données de rythme circadien et les guides
d'hygiène du sommeil dont il part sont publiés par des organismes du Gouvernement
des États-Unis et <strong>ne sont pas soumis au droit d'auteur en vertu du 17 U.S.C. §
105</strong>. La rédaction, la structure, les protocoles et les illustrations sont un
travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

VOLUNTAD = {
    "handle": "codice-de-la-voluntad",
    "portada": "codice-voluntad.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice de la Voluntad",
        "en": "Codex of the Will",
        "fr": "Codex de la Volonté",
    },
    "es": """
<p><strong>Adherencia, hábito y regreso: por qué los planes buenos se caen y cómo se
construye uno que sobreviva a los días malos.</strong> Dieciséis capítulos, cinco láminas
y un cuaderno de la voluntad.</p>

<h3>Qué contiene</h3>
<ul>
  <li>Por qué este libro <strong>no habla de motivación</strong>, y qué pone en su lugar.</li>
  <li>La <strong>única variable que domina</strong> el resultado de cualquier plan, y las tres palancas del bucle del hábito.</li>
  <li>El <strong>plan que sobrevive al día malo</strong>: cómo se diseña la versión mínima antes de necesitarla.</li>
  <li>La diferencia entre <strong>el fallo y la recaída</strong>, que no son lo mismo y no se tratan igual.</li>
  <li>Las <strong>habilidades de rendimiento</strong> de un manual público: activación, respiración y objetivos que sirven para algo.</li>
  <li><strong>Medirse sin castigarse</strong>, y diseñar el entorno antes que la fuerza de voluntad.</li>
  <li>Identidad, comparación y el <strong>ruido de fuera</strong>.</li>
  <li>Cómo <strong>volver después de meses</strong> — el capítulo que casi ningún libro escribe.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>56 páginas</strong>. Incluye las tres ediciones —<strong>español (56 pp.),
inglés (55 pp.) y francés (59 pp.)</strong>— con marcadores de navegación y glosario.</p>

<h3>Cómo leerlo</h3>
<p>Es un libro sobre <em>adherencia</em>: sobre por qué un plan correcto se abandona y qué
se puede construir para que sobreviva a los días malos. No es un tratado de
psicología clínica. Nada de lo que contiene diagnostica ni trata un trastorno de
la conducta alimentaria, una depresión ni una adicción, y no sustituye la
atención de un profesional sanitario colegiado.</p>

<p>Los manuales de instrucción física y preparación mental de los que parte —entre
ellos el FM 7-22 del Ejército— están publicados por el Gobierno de los Estados
Unidos y <strong>no están sujetos a derechos de autor conforme al 17 U.S.C. § 105</strong>. La
redacción, la estructura en cinco partes, los ejercicios de registro, las tablas
y las ilustraciones son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>Adherence, habit and coming back: why good plans fall over and how to build one
that survives the bad days.</strong> Sixteen chapters, five plates and a will notebook.</p>

<h3>What it contains</h3>
<ul>
  <li>Why this book <strong>does not talk about motivation</strong>, and what it puts in its place.</li>
  <li>The <strong>single variable that dominates</strong> the outcome of any plan, and the three levers of the habit loop.</li>
  <li>The <strong>plan that survives the bad day</strong>: how the minimum version is designed before you need it.</li>
  <li>The difference between <strong>a lapse and a relapse</strong>, which are not the same and are not handled the same way.</li>
  <li>The <strong>performance skills</strong> from a public manual: activation, breathing and goals that are actually good for something.</li>
  <li><strong>Measuring yourself without punishing yourself</strong>, and designing the environment rather than relying on willpower.</li>
  <li>Identity, comparison and the <strong>noise from outside</strong>.</li>
  <li>How to <strong>come back after months away</strong> — the chapter hardly any book writes.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>55 pages</strong>. Includes all three editions —<strong>English (55 pp.),
Spanish (56 pp.) and French (59 pp.)</strong>— with navigation bookmarks and a glossary.</p>

<h3>How to read it</h3>
<p>It is a book about <em>adherence</em>: about why a correct plan gets abandoned and what
can be built so that it survives the bad days. It is not a treatise on clinical
psychology. Nothing in it diagnoses or treats an eating disorder, a depression or
an addiction, and it does not replace care from a registered health professional.</p>

<p>The physical instruction and mental preparation manuals it starts from —among
them the Army's FM 7-22— are published by the United States Government and are
<strong>not subject to copyright under 17 U.S.C. § 105</strong>. The writing, the five-part
structure, the recording exercises, the tables and the illustrations are original
work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>Adhésion, habitude et retour : pourquoi les bons plans s'effondrent et comment
en bâtir un qui survive aux mauvais jours.</strong> Seize chapitres, cinq planches et un
cahier de la volonté.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>Pourquoi ce livre <strong>ne parle pas de motivation</strong>, et ce qu'il met à la place.</li>
  <li>La <strong>seule variable qui domine</strong> le résultat de n'importe quel plan, et les trois leviers de la boucle de l'habitude.</li>
  <li>Le <strong>plan qui survit au mauvais jour</strong> : comment on conçoit la version minimale avant d'en avoir besoin.</li>
  <li>La différence entre <strong>l'écart et la rechute</strong>, qui ne sont pas la même chose et ne se traitent pas de la même façon.</li>
  <li>Les <strong>habiletés de performance</strong> d'un manuel public : activation, respiration et objectifs qui servent à quelque chose.</li>
  <li><strong>Se mesurer sans se punir</strong>, et concevoir l'environnement plutôt que compter sur la volonté.</li>
  <li>Identité, comparaison et le <strong>bruit du dehors</strong>.</li>
  <li>Comment <strong>revenir après des mois</strong> — le chapitre que presque aucun livre n'écrit.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>59 pages</strong>. Comprend les trois éditions —<strong>français (59 p.),
espagnol (56 p.) et anglais (55 p.)</strong>— avec signets de navigation et glossaire.</p>

<h3>Comment le lire</h3>
<p>C'est un livre sur l'<em>adhésion</em> : sur les raisons pour lesquelles un plan correct
est abandonné et sur ce que l'on peut bâtir pour qu'il survive aux mauvais jours.
Ce n'est pas un traité de psychologie clinique. Rien de ce qu'il contient ne
diagnostique ni ne traite un trouble du comportement alimentaire, une dépression
ou une addiction, et cela ne remplace pas le suivi d'un professionnel de santé
diplômé.</p>

<p>Les manuels d'instruction physique et de préparation mentale dont il part —dont
le FM 7-22 de l'Armée— sont publiés par le Gouvernement des États-Unis et <strong>ne sont
pas soumis au droit d'auteur en vertu du 17 U.S.C. § 105</strong>. La rédaction, la
structure en cinq parties, les exercices de relevé, les tables et les
illustrations sont un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

ARCANOS = {
    "handle": "codice-de-los-arcanos",
    "portada": "codice-arcanos.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice de los Arcanos",
        "en": "Codex of the Arcana",
        "fr": "Codex des Arcanes",
    },
    "es": """
<p><strong>Las setenta y ocho cartas como instrumento de lectura: los veintidós mayores,
los cuatro palos y los treinta y seis decanatos.</strong> Diecinueve capítulos, cinco
láminas y un año de práctica.</p>

<h3>Qué contiene</h3>
<ul>
  <li><strong>La historia real</strong> del tarot, sin la leyenda egipcia: de dónde viene cada pieza y quién la añadió.</li>
  <li>Los <strong>veintidós mayores</strong> con su letra, su correspondencia y su lámina descrita, repartidos en cuatro tramos de recorrido.</li>
  <li>Los <strong>cuatro palos</strong>, los ases y las diez etapas del número.</li>
  <li>Las <strong>treinta y seis cartas menores</strong> con su decanato y su regente — la parte que convierte una baraja en un sistema.</li>
  <li><strong>Cómo se lee de verdad</strong>: las tiradas, la carta invertida y los errores del lector.</li>
  <li><strong>Lo que no se pregunta</strong>, y por qué: el capítulo que fija los límites del oficio.</li>
  <li>El <strong>cuaderno de tiradas</strong> y un año de práctica con revisión.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>62 páginas</strong>. Incluye las tres ediciones —<strong>español (62 pp.),
inglés (67 pp.) y francés (64 pp.)</strong>— con marcadores de navegación y vocabulario
final. Los nombres de las cartas van en la baraja de cada lengua.</p>

<h3>Cómo leerlo</h3>
<p>Los arcanos son un <em>lenguaje simbólico</em>: una manera antigua y muy afinada de
nombrar situaciones y temperamentos. No es una ciencia predictiva. Nada de lo que
contiene anuncia hechos futuros, diagnostica enfermedades ni sustituye la
atención de un médico o un psicólogo colegiado.</p>

<p>El material del que parte pertenece a la <strong>tradición común</strong>: la secuencia de los
arcanos, su iconografía y las correspondencias clásicas se transmiten por escrito
desde hace siglos en obras de dominio público y no son propiedad de nadie. La
redacción, la estructura, las lecturas, las fichas y las ilustraciones son
trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>The seventy-eight cards as an instrument of reading: the twenty-two major
arcana, the four suits and the thirty-six decans.</strong> Nineteen chapters, five plates
and a year of practice.</p>

<h3>What it contains</h3>
<ul>
  <li><strong>The real history</strong> of the tarot, without the Egyptian legend: where each piece came from and who added it.</li>
  <li>The <strong>twenty-two major arcana</strong> with their letter, their correspondence and their image described, laid out in four stretches of a journey.</li>
  <li>The <strong>four suits</strong>, the aces and the ten stages of number.</li>
  <li>The <strong>thirty-six minor cards</strong> with their decan and their ruler — the part that turns a deck into a system.</li>
  <li><strong>How it is really read</strong>: the spreads, the reversed card and the reader's errors.</li>
  <li><strong>What is not asked</strong>, and why: the chapter that sets the limits of the craft.</li>
  <li>The <strong>spread notebook</strong> and a year of practice with review.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>67 pages</strong>. Includes all three editions —<strong>English (67 pp.),
Spanish (62 pp.) and French (64 pp.)</strong>— with navigation bookmarks and a closing
vocabulary. The card names follow each language's own deck.</p>

<h3>How to read it</h3>
<p>The arcana are a <em>symbolic language</em>: an old and very finely tuned way of naming
situations and temperaments. It is not a predictive science. Nothing in it
announces future events, diagnoses illnesses or replaces the care of a registered
doctor or psychologist.</p>

<p>The material it starts from belongs to the <strong>common tradition</strong>: the sequence of
the arcana, their iconography and the classical correspondences have been
transmitted in writing for centuries in works in the public domain and are
nobody's property. The writing, the structure, the readings, the card entries and
the illustrations are original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>Les soixante-dix-huit cartes comme instrument de lecture : les vingt-deux
majeurs, les quatre couleurs et les trente-six décans.</strong> Dix-neuf chapitres, cinq
planches et une année de pratique.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li><strong>L'histoire réelle</strong> du tarot, sans la légende égyptienne : d'où vient chaque pièce et qui l'a ajoutée.</li>
  <li>Les <strong>vingt-deux majeurs</strong> avec leur lettre, leur correspondance et leur image décrite, répartis en quatre tronçons de parcours.</li>
  <li>Les <strong>quatre couleurs</strong>, les as et les dix étapes du nombre.</li>
  <li>Les <strong>trente-six cartes mineures</strong> avec leur décan et leur régent — la partie qui fait d'un jeu un système.</li>
  <li><strong>Comment on lit vraiment</strong> : les tirages, la carte inversée et les erreurs du lecteur.</li>
  <li><strong>Ce que l'on ne demande pas</strong>, et pourquoi : le chapitre qui fixe les limites du métier.</li>
  <li>Le <strong>cahier de tirages</strong> et une année de pratique avec relecture.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>64 pages</strong>. Comprend les trois éditions —<strong>français (64 p.),
espagnol (62 p.) et anglais (67 p.)</strong>— avec signets de navigation et vocabulaire
final. Les noms des cartes suivent le jeu propre à chaque langue.</p>

<h3>Comment le lire</h3>
<p>Les arcanes sont un <em>langage symbolique</em> : une manière ancienne et très affinée de
nommer des situations et des tempéraments. Ce n'est pas une science prédictive.
Rien de ce qu'il contient n'annonce des faits à venir, ne diagnostique de maladies
ni ne remplace le suivi d'un médecin ou d'un psychologue.</p>

<p>Le matériau dont il part appartient à la <strong>tradition commune</strong> : la séquence des
arcanes, leur iconographie et les correspondances classiques se transmettent par
écrit depuis des siècles dans des œuvres du domaine public et n'appartiennent à
personne. La rédaction, la structure, les lectures, les fiches et les
illustrations sont un travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

SI_MISMO = {
    "handle": "codice-del-si-mismo",
    "portada": "codice-si-mismo.png",
    "coleccion": "conocimiento",
    "gid": None,
    "titulo": {
        "es": "Códice del Sí Mismo",
        "en": "Codex of the Self",
        "fr": "Codex du Soi",
    },
    "es": """
<p><strong>Manual de observación interior: la atención dividida, los tres centros y el
trabajo de estar presente.</strong> Veinticinco capítulos, siete láminas y un año de
observación.</p>

<h3>Qué contiene</h3>
<ul>
  <li>Las <strong>cuatro cosas que no sabemos de nosotros</strong>, y de dónde viene esta clase de trabajo.</li>
  <li>La <strong>atención dividida</strong> y los <strong>tres centros</strong>: las dos herramientas sobre las que se apoya todo lo demás.</li>
  <li>El <strong>bucle de la identificación</strong> y la práctica de nombrar, con su regla de observación.</li>
  <li>Los <strong>seis recuerdos del día</strong>, el registro escrito y la respiración pautada.</li>
  <li>Las <strong>cuatro difíciles</strong> y el <strong>inventario nocturno</strong>.</li>
  <li><strong>Lo que depende de mí</strong>, los papeles, las cuentas pendientes y el sufrimiento innecesario.</li>
  <li>Las <strong>tres disciplinas</strong> clásicas y la vista desde arriba.</li>
  <li>Los <strong>errores del principiante</strong> y un año de observación con revisión trimestral.</li>
</ul>

<h3>Formato</h3>
<p>PDF A5, <strong>77 páginas</strong>. Incluye las tres ediciones —<strong>español (77 pp.),
inglés (81 pp.) y francés (82 pp.)</strong>— con marcadores de navegación y glosario.</p>

<h3>Cómo leerlo</h3>
<p>Es un libro de <em>trabajo interior</em>, escrito en un lenguaje simbólico. No es
psicología clínica ni terapia. Nada de lo que contiene diagnostica ni trata
ningún trastorno, y no sustituye la atención de un psicólogo o un psiquiatra
colegiado. Si atraviesas una crisis, busca ayuda profesional: este libro puede
acompañar ese camino, no reemplazarlo.</p>

<p>El material del que parte pertenece a la <strong>tradición común</strong>: los ejercicios
clásicos de examen de conciencia, atención y registro interior se transmiten por
escrito desde hace siglos y no son propiedad de nadie. La redacción, la
estructura, las prácticas, las fichas y las ilustraciones son trabajo propio.</p>

<p><em>Descarga digital. Obra original de VILLUMINATIONS · Primera edición, 2026.</em></p>
""",
    "en": """
<p><strong>A manual of inner observation: divided attention, the three centres and the work
of being present.</strong> Twenty-five chapters, seven plates and a year of observation.</p>

<h3>What it contains</h3>
<ul>
  <li>The <strong>four things we do not know about ourselves</strong>, and where this kind of work comes from.</li>
  <li><strong>Divided attention</strong> and the <strong>three centres</strong>: the two tools everything else rests on.</li>
  <li>The <strong>loop of identification</strong> and the practice of naming, with its rule of observation.</li>
  <li>The <strong>six recollections of the day</strong>, the written record and paced breathing.</li>
  <li>The <strong>four difficult ones</strong> and the <strong>nightly inventory</strong>.</li>
  <li><strong>What depends on me</strong>, the roles, the unfinished business and unnecessary suffering.</li>
  <li>The <strong>three classical disciplines</strong> and the view from above.</li>
  <li>The <strong>beginner's errors</strong> and a year of observation with quarterly review.</li>
</ul>

<h3>Format</h3>
<p>A5 PDF, <strong>81 pages</strong>. Includes all three editions —<strong>English (81 pp.),
Spanish (77 pp.) and French (82 pp.)</strong>— with navigation bookmarks and a glossary.</p>

<h3>How to read it</h3>
<p>It is a book of <em>inner work</em>, written in a symbolic language. It is not clinical
psychology or therapy. Nothing in it diagnoses or treats any disorder, and it
does not replace the care of a registered psychologist or psychiatrist. If you
are going through a crisis, seek professional help: this book can accompany that
road, not replace it.</p>

<p>The material it starts from belongs to the <strong>common tradition</strong>: the classical
exercises of self-examination, attention and inner record have been transmitted
in writing for centuries and are nobody's property. The writing, the structure,
the practices, the entries and the illustrations are original work.</p>

<p><em>Digital download. An original work by VILLUMINATIONS · First edition, 2026.</em></p>
""",
    "fr": """
<p><strong>Manuel d'observation intérieure : l'attention divisée, les trois centres et le
travail d'être présent.</strong> Vingt-cinq chapitres, sept planches et une année
d'observation.</p>

<h3>Ce qu'il contient</h3>
<ul>
  <li>Les <strong>quatre choses que nous ignorons de nous-mêmes</strong>, et d'où vient ce genre de travail.</li>
  <li>L'<strong>attention divisée</strong> et les <strong>trois centres</strong> : les deux outils sur lesquels tout le reste s'appuie.</li>
  <li>La <strong>boucle de l'identification</strong> et la pratique de nommer, avec sa règle d'observation.</li>
  <li>Les <strong>six rappels de la journée</strong>, le relevé écrit et la respiration cadencée.</li>
  <li>Les <strong>quatre difficiles</strong> et l'<strong>inventaire du soir</strong>.</li>
  <li><strong>Ce qui dépend de moi</strong>, les rôles, les comptes en suspens et la souffrance inutile.</li>
  <li>Les <strong>trois disciplines</strong> classiques et la vue d'en haut.</li>
  <li>Les <strong>erreurs du débutant</strong> et une année d'observation avec relecture trimestrielle.</li>
</ul>

<h3>Format</h3>
<p>PDF A5, <strong>82 pages</strong>. Comprend les trois éditions —<strong>français (82 p.),
espagnol (77 p.) et anglais (81 p.)</strong>— avec signets de navigation et glossaire.</p>

<h3>Comment le lire</h3>
<p>C'est un livre de <em>travail intérieur</em>, écrit dans un langage symbolique. Ce n'est
ni de la psychologie clinique ni une thérapie. Rien de ce qu'il contient ne
diagnostique ni ne traite un trouble, et cela ne remplace pas le suivi d'un
psychologue ou d'un psychiatre. Si vous traversez une crise, cherchez une aide
professionnelle : ce livre peut accompagner ce chemin, non le remplacer.</p>

<p>Le matériau dont il part appartient à la <strong>tradition commune</strong> : les exercices
classiques d'examen de conscience, d'attention et de relevé intérieur se
transmettent par écrit depuis des siècles et n'appartiennent à personne. La
rédaction, la structure, les pratiques, les fiches et les illustrations sont un
travail propre.</p>

<p><em>Téléchargement numérique. Œuvre originale de VILLUMINATIONS · Première édition, 2026.</em></p>
""",
}

NUEVOS = [MESA, CARGA, DESCANSO, VOLUNTAD, ARCANOS, SI_MISMO]
