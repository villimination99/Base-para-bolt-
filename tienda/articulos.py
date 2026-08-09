#!/usr/bin/env python3
"""
VILLUMINATIONS — Artículos del blog
------------------------------------
Cinco entradas escritas para interceptar la pregunta que la gente sí teclea.
Nadie busca «Códice de la Mesa»; buscan «cuántas horas hay que dormir». Cada
artículo responde una de esas preguntas de verdad y, al final, señala el libro
que la desarrolla.

Tres reglas al escribir aquí, y no son de estilo:

· **No se destripa el libro.** Un artículo que vuelca las diecinueve tablas de
  micronutrientes deja al libro sin nada que vender. Se da lo suficiente para
  que la visita valga la pena por sí sola y se nombra el libro una vez.

· **Ninguna promesa de salud, y menos sobre lo que vendemos.** Se puede decir
  qué dice la evidencia pública sobre la creatina; no se puede decir que
  *nuestro* bote de creatina haga nada. La diferencia es jurídica, no de tono.

· **Cada cifra con su fuente, y la fuente en el texto.** Casi todo lo que hay
  aquí sale de organismos del Gobierno de EE. UU., que publican en abierto y
  cuyas obras **no están sujetas a derechos de autor conforme al 17 U.S.C.
  § 105**. Esa es la ventaja de esta tienda sobre un blog de fitness que copió
  las cifras de otro blog: las nuestras se pueden comprobar.

Medidas de buscador: 60 caracteres el título, 155 la descripción. Se comprueba
abajo, no se confía.
"""

BLOG = {
    "handle": "diario",
    "titulo": "Diario",
    "meta_titulo": "Diario — nutrición, carga y símbolo | VILLUMINATIONS",
    "meta_descripcion": (
        "Artículos de referencia sobre alimentación, entrenamiento, descanso y "
        "simbolismo. Cada cifra con la fuente pública de la que sale."
    ),
}

FIRMA = (
    '<p><em>Publicado por VILLUMINATIONS. Este texto es informativo y no '
    'sustituye la atención de un profesional sanitario colegiado.</em></p>'
)


def _fuentes(filas: str) -> str:
    return (
        "<h3>De dónde sale cada cifra</h3>\n"
        "<ul>\n" + filas + "</ul>\n"
        "<p>Los organismos del Gobierno de los Estados Unidos publican en "
        "abierto y sus obras <strong>no están sujetas a derechos de autor "
        "conforme al 17 U.S.C. § 105</strong>. Las cifras se pueden comprobar "
        "una por una; la redacción de este artículo es trabajo propio.</p>\n"
    )


ETIQUETA = (
    '<p><strong>Esto es un resumen.</strong> {frase} '
    'Está en <a href="/products/{handle}">{libro}</a>, '
    'un PDF de {paginas} páginas en español, inglés y francés.</p>'
)


ARTICULOS = [
    # ------------------------------------------------------------------ 1
    {
        "handle": "como-se-lee-una-etiqueta-nutricional",
        "titulo": "Cómo se lee una etiqueta nutricional",
        "resumen": (
            "El porcentaje que casi nadie sabe interpretar, la regla del 5 y el "
            "20, la tolerancia legal que permite que la cifra no sea exacta y "
            "las tres trampas más frecuentes."
        ),
        "etiquetas": ["nutrición", "etiquetado", "referencia"],
        "meta": (
            "Cómo se lee una etiqueta nutricional | VILLUMINATIONS",
            "La regla del 5 y el 20, el porcentaje de valor diario, la "
            "tolerancia legal y por qué «0 g de grasas trans» puede no ser cero.",
        ),
        "cuerpo": """
<p>Una etiqueta nutricional no está escrita para que la entiendas de un
vistazo: está escrita para cumplir una norma. Eso la hace fiable y la hace
opaca a la vez. Estas son las cuatro cosas que hay que saber para leerla en
diez segundos.</p>

<h2>1. La ración manda sobre todo lo demás</h2>

<p>Todas las cifras del panel se refieren a <strong>una ración</strong>, no al
envase. Es el error más común y el más caro: una bolsa que parece individual
puede declarar dos raciones y media, y entonces las calorías que has leído hay
que multiplicarlas por dos y medio.</p>

<p>Antes de mirar nada, mira dos líneas: <em>tamaño de la ración</em> y
<em>raciones por envase</em>. Si no cuadran con lo que te vas a comer, el resto
del panel no dice lo que crees que dice.</p>

<h2>2. El porcentaje se refiere a una persona que no eres tú</h2>

<p>El <strong>porcentaje de valor diario</strong> está calculado sobre una dieta
de referencia de <strong>2000 kcal</strong>. No es tu dieta: es un convenio para
que las etiquetas se puedan comparar entre sí. Si comes 2600 kcal, todos esos
porcentajes se te quedan altos; si comes 1600, cortos.</p>

<p>Sirve para comparar dos productos, no para planificar tu día.</p>

<h2>3. La regla del 5 y el 20</h2>

<p>Es el atajo que publica la propia autoridad de etiquetado y funciona sin
calculadora:</p>

<ul>
  <li><strong>5 % o menos</strong> del valor diario en un nutriente: ese producto
  es <em>bajo</em> en eso.</li>
  <li><strong>20 % o más</strong>: es <em>alto</em> en eso.</li>
</ul>

<p>Lo útil es aplicarla en las dos direcciones. Quieres el 20 % o más en fibra,
calcio, hierro o potasio. Quieres el 5 % o menos en grasas saturadas, sodio y
azúcares añadidos. Con dos productos en la mano, esa comparación se hace en
cinco segundos y acierta casi siempre.</p>

<h2>4. La cifra impresa tiene margen legal</h2>

<p>Aquí está lo que casi nadie sabe. La cifra de la etiqueta <strong>no es
exacta, y no tiene por qué serlo</strong>: la norma admite una tolerancia, y la
admite en dos direcciones distintas según el nutriente.</p>

<ul>
  <li>En los nutrientes que conviene tener —vitaminas y minerales añadidos,
  proteína, fibra— el producto debe contener <strong>al menos</strong> lo
  declarado. Puede tener más.</li>
  <li>En los que conviene limitar —calorías, azúcares, grasa total, grasa
  saturada, sodio— el producto <strong>no puede pasarse</strong> de lo declarado
  más allá de un margen. Puede tener menos.</li>
</ul>

<p>Es decir: el fabricante tiene incentivo para declarar la proteína por lo bajo
y el sodio por lo alto, porque así cumple con holgura en los dos sentidos. La
etiqueta es honesta y aun así te está dando el escenario que más le conviene.</p>

<h3>La trampa del redondeo</h3>

<p>Cuando una cantidad cae por debajo de cierto umbral, la norma permite
declararla como cero. Por eso existen productos que anuncian
<strong>«0 g de grasas trans»</strong> y llevan aceite parcialmente hidrogenado
en la lista de ingredientes. Cada ración tiene poco; tres raciones ya no.</p>

<p>La regla práctica: <strong>cuando el panel diga cero y la lista de
ingredientes diga lo contrario, gana la lista de ingredientes.</strong></p>

<h2>La lista de ingredientes, en orden de peso</h2>

<p>Los ingredientes van ordenados de mayor a menor cantidad. Eso convierte la
lista en un gráfico de barras sin barras: si el azúcar aparece en tercer lugar,
hay más azúcar que de todo lo que venga después junto.</p>

<p>El truco del que hay que desconfiar es la <strong>división del azúcar</strong>:
un producto que lleva jarabe de glucosa, azúcar moreno, dextrosa y concentrado
de zumo reparte lo mismo entre cuatro nombres, y así ninguno sube a los primeros
puestos. Sumados serían el primero.</p>

<h2>Lo que una declaración puede y no puede decir</h2>

<p>«Sin azúcar añadido» no significa sin azúcar: un zumo de manzana no lleva
azúcar añadido y va cargado de azúcar propio. «Ligero» puede referirse al color.
«Natural» no tiene, en la práctica, una definición que obligue a nada.</p>

<p>Las declaraciones que sí están reguladas —las que relacionan un nutriente con
una función del organismo— tienen un registro público donde se puede consultar
cuáles se aprobaron y, más interesante, <strong>cuáles se pidieron y fueron
rechazadas</strong>. Esa segunda lista es la que enseña de verdad qué está
demostrado y qué no.</p>

""" + _fuentes(
            "<li><strong>FDA</strong> — Panel de información nutricional, regla del "
            "5 y el 20, tolerancias y reglas de redondeo.</li>\n"
            "<li><strong>ODS · NIH</strong> — Ingestas dietéticas de referencia.</li>\n"
            "<li><strong>Registro europeo de declaraciones nutricionales y de "
            "propiedades saludables</strong> — aprobadas y rechazadas.</li>\n"
        ) + ETIQUETA.format(
            frase="El detalle —las cuatro letras de las tablas de referencia, los "
                  "diecinueve micronutrientes con su recomendación y su límite "
                  "superior, y las declaraciones aprobadas en su redacción "
                  "oficial— pide más sitio.",
            handle="codice-de-la-mesa", libro="el Códice de la Mesa", paginas="78",
        ) + FIRMA,
    },

    # ------------------------------------------------------------------ 2
    {
        "handle": "cuanta-actividad-fisica-hace-falta",
        "titulo": "Cuánta actividad física hace falta de verdad",
        "resumen": (
            "Existe una dosis, está escrita y no es la que se repite en el "
            "gimnasio. Cuántos minutos, de qué clase, y por qué el primer tramo "
            "vale más que todos los demás."
        ),
        "etiquetas": ["entrenamiento", "actividad física", "referencia"],
        "meta": (
            "Cuánta actividad física hace falta | VILLUMINATIONS",
            "La dosis semanal que recomiendan las guías públicas, el cambio de "
            "2 por 1 entre moderada y vigorosa, y la forma real de la curva.",
        ),
        "cuerpo": """
<p>La pregunta tiene respuesta publicada, y es más concreta de lo que la
mayoría imagina. No es «muévete más»: es una cantidad, con unidades.</p>

<h2>La dosis, en una línea</h2>

<p>Para un adulto sano, las guías públicas de actividad física recomiendan a la
semana:</p>

<ul>
  <li><strong>De 150 a 300 minutos</strong> de actividad aeróbica de intensidad
  <em>moderada</em>, o</li>
  <li><strong>de 75 a 150 minutos</strong> de intensidad <em>vigorosa</em>, o
  cualquier combinación equivalente de las dos, y</li>
  <li><strong>dos días o más</strong> de trabajo de fuerza que involucre todos
  los grupos musculares principales.</li>
</ul>

<p>El cambio entre las dos es <strong>dos por uno</strong>: un minuto vigoroso
cuenta como dos moderados. Así se puede repartir sin hacer cuentas raras.</p>

<h3>Dónde está la frontera entre moderada y vigorosa</h3>

<p>Sin pulsómetro, con la prueba de la conversación: en actividad
<strong>moderada</strong> puedes hablar pero no cantar. En
<strong>vigorosa</strong> no puedes decir más de unas pocas palabras seguidas sin
parar a respirar.</p>

<h2>La curva no es una recta</h2>

<p>Esto es lo que cambia la forma de plantearse el asunto. El beneficio no crece
de forma proporcional al esfuerzo: <strong>el tramo que más rinde con diferencia
es el que va de cero a poco</strong>. Alguien que no hace nada y empieza a
moverse gana muchísimo más que alguien que ya cumple la dosis y la dobla.</p>

<p>Dos consecuencias prácticas, y las dos van contra lo que se suele oír:</p>

<ul>
  <li>Si no haces nada, <strong>no hace falta llegar a los 150 minutos para que
  valga la pena</strong>. Veinte minutos de caminata tres veces por semana ya
  está comprando el tramo caro de la curva.</li>
  <li>Si ya cumples, <strong>doblar el volumen rinde poco</strong>. Ahí el margen
  está en la calidad, la fuerza y el descanso, no en más minutos.</li>
</ul>

<h2>Lo del mínimo de diez minutos ya no está</h2>

<p>Durante años se repitió que una sesión tenía que durar al menos diez minutos
para contar. <strong>Esa condición se eliminó</strong> en la revisión de las
guías: cuenta todo. Subir escaleras, cargar la compra, tres minutos de camino
rápido. La actividad se acumula, no necesita permiso de duración.</p>

<h2>La fuerza no es opcional</h2>

<p>Los dos días de trabajo muscular a la semana están en la recomendación con el
mismo rango que la parte aeróbica, y son la parte que más gente se salta. No
hace falta un gimnasio: cuenta el peso corporal, las bandas y las cargas de la
vida diaria, siempre que el músculo llegue a un punto donde repetir cueste.</p>

<p>Y a partir de los sesenta y cinco se añade una tercera pata que casi nunca se
menciona: <strong>entrenamiento de equilibrio</strong>. Es la que previene la
caída, que en esa franja de edad hace más daño que casi cualquier otra cosa.</p>

<h2>Estar sentado cuenta aparte</h2>

<p>La otra mitad del mensaje: <strong>moverse más y estar sentado menos son dos
recomendaciones distintas</strong>, no la misma dicha dos veces. Se puede cumplir
la dosis semanal y pasar el resto del día sentado, y eso sigue siendo un
problema por su cuenta.</p>

""" + _fuentes(
            "<li><strong>health.gov</strong> — Guías de actividad física, segunda "
            "edición: dosis semanal, cambio 2 por 1, retirada del mínimo de diez "
            "minutos, equilibrio a partir de los 65.</li>\n"
            "<li><strong>FM 7-22</strong> — Doctrina de preparación física: patrones "
            "de movimiento y programación.</li>\n"
            "<li><strong>CDC / NIOSH</strong> — Criterios de manejo manual de cargas.</li>\n"
        ) + ETIQUETA.format(
            frase="Los ocho patrones de movimiento, las seis variables con las que "
                  "se programa una semana y la ecuación de levantamiento con sus "
                  "factores desarrollados uno a uno ocupan bastante más.",
            handle="codice-de-la-carga", libro="el Códice de la Carga", paginas="70",
        ) + FIRMA,
    },

    # ------------------------------------------------------------------ 3
    {
        "handle": "cuantas-horas-hay-que-dormir",
        "titulo": "Cuántas horas hay que dormir, y qué pasa si no",
        "resumen": (
            "La cifra por edades, qué se recupera de una semana corta y qué no, "
            "la cuenta atrás de las últimas horas y la señal de que el problema "
            "ya no es de higiene del sueño."
        ),
        "etiquetas": ["sueño", "recuperación", "referencia"],
        "meta": (
            "Cuántas horas hay que dormir | VILLUMINATIONS",
            "Las horas recomendadas por edad, la deuda de sueño, la cafeína y el "
            "alcohol con sus tiempos, y cuándo dejar de leer consejos.",
        ),
        "cuerpo": """
<p>La respuesta corta lleva años publicada y sigue sorprendiendo por lo poco
flexible que es.</p>

<h2>La cifra, por edades</h2>

<table>
  <thead><tr><th>Edad</th><th>Horas por noche</th></tr></thead>
  <tbody>
    <tr><td>13 a 18 años</td><td>De 8 a 10</td></tr>
    <tr><td>18 a 60 años</td><td>7 o más</td></tr>
    <tr><td>61 a 64 años</td><td>De 7 a 9</td></tr>
    <tr><td>65 años en adelante</td><td>De 7 a 8</td></tr>
  </tbody>
</table>

<p>Fíjate en que la recomendación para adultos es un <strong>suelo</strong>, no
un objetivo: siete o más. La creencia de que uno «necesita cinco horas» casi
nunca describe a alguien que funcione con cinco horas; describe a alguien que
lleva tanto tiempo cansado que ha olvidado cómo es no estarlo.</p>

<h2>La deuda: qué se recupera y qué no</h2>

<p>Dormir poco de lunes a viernes y estirar el fin de semana recupera
<strong>parte</strong> de lo perdido, no todo, y tiene un precio: dormir tres
horas de más el sábado retrasa el reloj interno y hace que el domingo por la
noche no llegue el sueño. Se paga el sábado con el lunes.</p>

<p>Lo que peor se recupera es lo que peor se nota: la atención sostenida se
degrada de forma progresiva y la percepción de estar degradado <strong>no</strong>
la acompaña. Quien lleva una semana durmiendo seis horas rinde bastante peor de
lo que cree.</p>

<h2>La cuenta atrás de las últimas horas</h2>

<p>Tres sustancias con tres tiempos distintos, y conviene tratarlas por
separado:</p>

<ul>
  <li><strong>Cafeína.</strong> Tarda del orden de cinco horas en eliminar la
  mitad de la dosis, y eso significa que un café de las cuatro de la tarde
  todavía tiene un cuarto en circulación a medianoche. La sensibilidad varía
  mucho de una persona a otra; el margen de seis a ocho horas antes de acostarse
  es el que funciona para la mayoría.</li>
  <li><strong>Alcohol.</strong> Es el más engañoso, porque ayuda a dormirse y
  estropea lo que viene después: <strong>fragmenta la segunda mitad de la
  noche</strong>, justo donde está el sueño que restaura. Dormirse antes y
  descansar peor.</li>
  <li><strong>Nicotina.</strong> Es un estimulante y, además, la retirada nocturna
  despierta.</li>
</ul>

<h2>La habitación: tres cifras y ninguna más</h2>

<p>De todo lo que se dice sobre el dormitorio, lo que está medido se reduce a
tres cosas: <strong>fresco, oscuro y silencioso</strong>. La temperatura por
debajo de la de confort diurno; la luz cuanto menos mejor, incluida la del
móvil; y el ruido constante molesta menos que el intermitente.</p>

<p>Lo demás —almohadas, aromas, aplicaciones— puede gustarte, pero no está en el
mismo nivel de evidencia y no compensa un horario irregular.</p>

<h2>La intervención que más rinde es la más aburrida</h2>

<p>Por encima de todo lo anterior: <strong>una hora fija de levantarse, todos los
días, incluido el fin de semana</strong>. El reloj interno se ancla en la hora de
despertar y en la luz de la mañana, no en la hora de acostarse. Es gratis, no
requiere comprar nada y gana a cualquier suplemento.</p>

<h3>La siesta, si se hace bien</h3>

<p>De diez a veinte minutos, y temprano. Más larga entra en sueño profundo y se
despierta uno peor que antes; más tarde, le roba presión de sueño a la noche.</p>

<h2>Cuándo dejar de leer consejos</h2>

<p>Todo lo anterior es <strong>higiene del sueño para personas sanas</strong>. Hay
dos situaciones en las que no aplica y en las que seguir leyendo artículos es
perder tiempo:</p>

<ul>
  <li>Llevas <strong>más de tres meses</strong> durmiendo mal la mayoría de las
  noches, con consecuencias durante el día. Eso ya tiene nombre clínico y
  tratamiento, y el tratamiento que funciona no es un consejo de blog.</li>
  <li>Alguien te ha dicho que <strong>dejas de respirar mientras duermes</strong>,
  o roncas y te levantas cansado sin explicación. Eso se estudia, no se corrige
  con la temperatura del cuarto.</li>
</ul>

<p>En los dos casos, el paso siguiente es un médico.</p>

""" + _fuentes(
            "<li><strong>CDC</strong> — Horas de sueño recomendadas por grupo de edad.</li>\n"
            "<li><strong>NHLBI · NIH</strong> — Deuda de sueño, ritmo circadiano e "
            "higiene del sueño.</li>\n"
            "<li><strong>NIOSH</strong> — Trabajo por turnos y sueño.</li>\n"
        ) + ETIQUETA.format(
            frase="La arquitectura de una noche fase por fase, qué hacer cuando el "
                  "sueño no llega y en qué orden probarlo, y los turnos y viajes "
                  "cuando el horario no se elige, están desarrollados aparte.",
            handle="codice-del-descanso", libro="el Códice del Descanso", paginas="53",
        ) + FIRMA,
    },

    # ------------------------------------------------------------------ 4
    {
        "handle": "que-suplementos-tienen-evidencia",
        "titulo": "Qué suplementos tienen evidencia y cuáles no",
        "resumen": (
            "Los pocos que han pasado la prueba, los muchos que no, y el dato "
            "sobre cómo se regulan que cambia la forma de comprarlos."
        ),
        "etiquetas": ["suplementos", "evidencia", "referencia"],
        "meta": (
            "Qué suplementos tienen evidencia | VILLUMINATIONS",
            "Creatina, cafeína, proteína y los que no llegan. Cómo se regulan de "
            "verdad y qué sello mirar si compites.",
        ),
        "cuerpo": """
<p>Antes de la lista, el dato que reordena todo lo demás.</p>

<h2>Un suplemento no se aprueba antes de venderse</h2>

<p>A diferencia de un medicamento, un complemento alimenticio
<strong>no pasa por una autorización previa</strong> que verifique que hace lo
que dice. El fabricante es responsable de que su producto sea seguro y de que la
etiqueta no engañe, y la autoridad actúa sobre todo <em>después</em>, si algo
sale mal.</p>

<p>Eso no significa que sean inútiles ni peligrosos. Significa que la frase «está
a la venta» no aporta ninguna información sobre si funciona. Hay que mirar la
evidencia por separado, producto por producto.</p>

<h2>Los que han pasado la prueba</h2>

<h3>Creatina monohidrato</h3>
<p>Es el suplemento deportivo más estudiado que existe, con diferencia y por
muchos años de ventaja. Se investiga en el rango de <strong>3 a 5 gramos
diarios</strong>. Es también uno de los más baratos, lo que dice bastante sobre
la relación entre precio y evidencia en este mercado.</p>

<h3>Cafeína</h3>
<p>Ayuda ergogénica reconocida, estudiada habitualmente en el rango de
<strong>3 a 6 mg por kilo de peso</strong> tomada entre media hora y una hora
antes. Subir de ahí no mejora el efecto y sí empeora el sueño de esa noche
—que, si has leído el artículo sobre descanso, es pagar por un lado lo que
ganas por el otro.</p>

<h3>Proteína en polvo</h3>
<p>Aquí conviene ser exacto: la proteína en polvo <strong>no es un compuesto
activo, es comida cómoda</strong>. Lo que tiene evidencia es llegar a la proteína
total del día; el polvo es una forma práctica de llegar, no una vía distinta. Si
ya llegas comiendo, no añade nada.</p>

<h3>Beta-alanina y citrulina malato</h3>
<p>Efectos reales pero modestos, y en tipos de esfuerzo bastante concretos. No
están al nivel de los tres anteriores y no son el primer sitio donde gastar.</p>

<h2>Los que no llegan</h2>

<p>La lista es más larga que la anterior. Lo habitual no es que un suplemento
esté <em>refutado</em>, sino que los estudios que lo sostienen sean pequeños, en
animales, o a dosis que no se parecen a las del bote.</p>

<p>Tres señales de que estás ante uno de esos:</p>

<ul>
  <li><strong>La dosis del bote no es la del estudio.</strong> Es la trampa más
  común. Se cita una investigación seria hecha con una cantidad que el producto
  no lleva ni de lejos.</li>
  <li><strong>Mezcla propia sin cantidades.</strong> Si la etiqueta dice «complejo
  patentado» y lista doce ingredientes sin decir cuánto hay de cada uno, no se
  puede comparar con nada. Ese es el objetivo.</li>
  <li><strong>Promete varias cosas a la vez.</strong> Energía, concentración,
  quemar grasa y dormir mejor no son el mismo mecanismo.</li>
</ul>

<h3>El caso de los BCAA</h3>
<p>Merecen mención aparte porque se venden mucho. Si tu ingesta de proteína del
día ya es adecuada, los aminoácidos ramificados por separado añaden poco: ya los
estás tomando dentro de la proteína completa.</p>

<h2>La jerarquía, y esto es lo importante</h2>

<p>El orden en que las cosas mueven el resultado, de más a menos:</p>

<ol>
  <li>Calorías totales y proteína del día.</li>
  <li>Entrenamiento constante, con progresión.</li>
  <li>Sueño suficiente.</li>
  <li><strong>Y después, muy después, los suplementos.</strong></li>
</ol>

<p>Un suplemento sobre una base rota no arregla nada. La expresión honesta es que
los suplementos son el uno por ciento final, y solo tienen sentido cuando el
noventa y nueve restante ya está en su sitio.</p>

<h2>Si compites, mira el sello</h2>

<p>Un producto puede estar contaminado con sustancias no declaradas sin que el
fabricante lo pretenda. Para quien pasa controles antidopaje, la única
protección práctica son los programas de <strong>verificación por tercero</strong>
que analizan lote a lote. El sello va en el envase y se puede comprobar en el
registro del programa.</p>

<p>Y una advertencia general: <strong>si tomas medicación, estás embarazada o
tienes una patología, consulta antes</strong>. Las interacciones existen y algunas
son serias.</p>

""" + _fuentes(
            "<li><strong>ODS · NIH</strong> — Fichas de datos sobre suplementos "
            "dietéticos y su marco regulatorio.</li>\n"
            "<li><strong>FDA</strong> — Régimen de los complementos alimenticios: "
            "responsabilidad del fabricante y ausencia de autorización previa.</li>\n"
            "<li><strong>Registro europeo de declaraciones de propiedades "
            "saludables</strong> — qué se aprobó y qué se rechazó.</li>\n"
        ) + (
            '<p><strong>Lo que vendemos y lo que decimos.</strong> En esta tienda hay '
            '<a href="/collections/suplementos">suplementos</a>, y por eso conviene '
            'ser claro: este artículo describe lo que dice la evidencia pública '
            'sobre unas sustancias, no lo que hace ningún bote concreto. Las fichas '
            'de nuestros productos no prometen efectos sobre la salud, y no es por '
            'modestia.</p>\n'
            '<p>La <a href="/products/pro-definicion-volumen">guía de suplementación '
            'del nivel Pro</a> desarrolla esto con la jerarquía completa, el criterio '
            'de la dosis del metaanálisis y un presupuesto mensual por niveles.</p>'
        ) + FIRMA,
    },

    # ------------------------------------------------------------------ 5
    {
        "handle": "que-es-un-decanato",
        "titulo": "Qué es un decanato, y por qué tu signo no te describe",
        "resumen": (
            "Los treinta grados de cada signo se dividen en tres. Esa división "
            "de diez grados explica por qué mucha gente no se reconoce en la "
            "descripción general de su signo."
        ),
        "etiquetas": ["zodiaco", "simbolismo", "referencia"],
        "meta": (
            "Qué es un decanato | VILLUMINATIONS",
            "Los treinta y seis decanatos, los dos sistemas de regencia y por qué "
            "la descripción general de un signo falla tan a menudo.",
        ),
        "cuerpo": """
<p>Casi todo el mundo que ha leído la descripción de su signo ha tenido la misma
sensación: acierta a medias. Hay una razón estructural para eso, y tiene más de
dos mil años.</p>

<h2>Treinta grados divididos en tres</h2>

<p>El círculo del zodiaco tiene 360 grados repartidos entre doce signos, así que
cada signo ocupa <strong>treinta grados</strong>. Esos treinta grados no se
tratan como un bloque homogéneo: se dividen en tres tramos de diez, y a cada
tramo se le llama <strong>decanato</strong>.</p>

<ul>
  <li>Primer decanato: grados 0 a 10 del signo</li>
  <li>Segundo decanato: grados 10 a 20</li>
  <li>Tercer decanato: grados 20 a 30</li>
</ul>

<p>Doce signos por tres tramos dan <strong>treinta y seis decanatos</strong>. Y
esa es la primera respuesta a por qué la descripción general falla: alguien
nacido en el primer decanato de un signo y alguien del tercero comparten
etiqueta y poco más. Entre los dos hay veinte grados, que es más de lo que
separa a muchos signos vecinos.</p>

<h2>Cada tramo tiene su regente</h2>

<p>Lo que convierte esto en un sistema y no en una simple división es que cada
decanato lleva asociado un planeta regente. Hay <strong>dos formas clásicas de
asignarlo</strong>, y conviene saber que existen las dos porque las fuentes
mezclan una y otra sin avisar:</p>

<ul>
  <li><strong>La secuencia caldea.</strong> Los siete planetas tradicionales se
  recorren en un orden fijo, decanato tras decanato, dando la vuelta entera al
  zodiaco. Es un mecanismo puramente secuencial.</li>
  <li><strong>Por triplicidad.</strong> Los tres decanatos de un signo se reparten
  entre los regentes de los tres signos de su mismo elemento. Así, el primer
  decanato lo rige el propio signo y los otros dos sus hermanos de elemento.</li>
</ul>

<p>Los dos sistemas dan resultados distintos para el mismo grado. No es un error
de nadie: son tradiciones diferentes que sobrevivieron en paralelo. Lo que sí es
un error es usar uno y citar la autoridad del otro.</p>

<h2>Y todavía hay una división más fina</h2>

<p>Por debajo del decanato están los <strong>términos</strong>, a veces llamados
límites: una división de cada signo en cinco tramos <em>desiguales</em>,
asignados también a planetas. Es la tabla más fina y más olvidada del sistema
clásico, y la que menos aparece en los sitios de astrología popular, precisamente
porque no se resume en una frase.</p>

<p>Que los tramos sean desiguales es lo interesante: indica que la tabla no salió
de un reparto geométrico bonito, sino de una tradición que se transmitió por
copia durante siglos.</p>

<h2>Por qué esto no es una ciencia predictiva</h2>

<p>Conviene decirlo sin rodeos, porque cambia cómo se usa todo lo anterior. Los
signos, los decanatos y los términos son un <strong>lenguaje simbólico</strong>:
una manera antigua y muy afinada de nombrar temperamentos, tensiones y ciclos.
Son útiles como vocabulario para mirarse, igual que lo es cualquier tipología
bien construida.</p>

<p>No anuncian hechos futuros, no diagnostican nada y no sustituyen a un médico
ni a un psicólogo. Quien te venda lo contrario te está vendiendo otra cosa.</p>

<h2>La otra razón por la que tu signo falla</h2>

<p>Aparte del decanato hay una segunda causa, y es más simple: la descripción
popular de un signo se refiere solo a la posición del Sol. Es un dato entre
varios. Reducir una carta entera a ese único elemento es como describir un libro
por su primera palabra.</p>

<h3>Una nota sobre las eras</h3>

<p>Como el eje de la Tierra se bambolea muy despacio, el punto de referencia se
desplaza alrededor de un grado cada setenta y dos años. De ahí salen las
llamadas «eras», y de ahí sale también la discusión periódica sobre si los
signos «se han movido». La respuesta depende de qué zodiaco se use, y las dos
posturas son coherentes consigo mismas.</p>

""" + _fuentes(
            "<li>La secuencia de los decanatos, las dignidades y los términos "
            "egipcios se transmiten por escrito desde hace más de dos milenios en "
            "obras de <strong>dominio público</strong>, y no son propiedad de nadie.</li>\n"
            "<li>Las cifras de precesión son astronómicas y comprobables.</li>\n"
        ) + ETIQUETA.format(
            frase="La tabla completa de los treinta y seis decanatos con su regente, "
                  "las cuatro dignidades esenciales con el grado exacto de cada "
                  "exaltación y los sesenta términos egipcios no caben en un artículo.",
            handle="codice-zodiacal", libro="el Códice Zodiacal", paginas="144",
        ) + (
            '<p><em>Publicado por VILLUMINATIONS. La astrología que se practica aquí '
            'es un lenguaje simbólico, no una ciencia predictiva: nada de lo que se '
            'dice anuncia hechos futuros ni sustituye la atención de un profesional '
            'sanitario.</em></p>'
        ),
    },
]

TOPE_TITULO = 60
TOPE_DESCRIPCION = 155


def comprobar() -> list:
    """Lo que se pasa de medida o le falta un campo. Vacío es lo correcto."""
    malos = []
    vistos = set()
    for a in ARTICULOS:
        t, d = a["meta"]
        if len(t) > TOPE_TITULO:
            malos.append(f"{a['handle']} · título {len(t)}/{TOPE_TITULO}")
        if len(d) > TOPE_DESCRIPCION:
            malos.append(f"{a['handle']} · descripción {len(d)}/{TOPE_DESCRIPCION}")
        if a["handle"] in vistos:
            malos.append(f"{a['handle']} · handle repetido")
        vistos.add(a["handle"])
        for campo in ("titulo", "resumen", "cuerpo", "etiquetas"):
            if not a.get(campo):
                malos.append(f"{a['handle']} · falta {campo}")
    if len(BLOG["meta_titulo"]) > TOPE_TITULO:
        malos.append(f"blog · título {len(BLOG['meta_titulo'])}/{TOPE_TITULO}")
    if len(BLOG["meta_descripcion"]) > TOPE_DESCRIPCION:
        malos.append(f"blog · descripción {len(BLOG['meta_descripcion'])}")
    return malos


if __name__ == "__main__":
    malos = comprobar()
    print(f"\n  {len(ARTICULOS)} artículos · {len(malos)} fuera de medida\n")
    for m in malos:
        print(f"    {m}")
    for a in ARTICULOS:
        palabras = len(a["cuerpo"].split())
        print(f"    {a['handle']:44} {palabras:5} palabras")
    print()
