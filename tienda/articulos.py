#!/usr/bin/env python3
"""
VILLUMINATIONS — Artículos del blog
------------------------------------
Nueve entradas escritas para interceptar la pregunta que la gente sí teclea.
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

· **Cada cifra con su fuente, y la fuente en el texto.** Lo de nutrición y
  entrenamiento sale de organismos del Gobierno de EE. UU., que publican en
  abierto y cuyas obras **no están sujetas a derechos de autor conforme al
  17 U.S.C. § 105**. Lo esotérico se apoya en la **tradición común y el dominio
  público**, que es otra cosa. `_fuentes(filas, base=...)` firma con una o con
  otra; no hay firma por defecto que valga para las dos.

Medidas de buscador: 60 caracteres el título, 155 la descripción. Se comprueba
abajo, no se confía.
"""

# El blog no se creó de cero: se reutilizó el que Shopify deja puesto por
# defecto, que se llamaba «Actualités» —en francés, en una tienda cuyo idioma
# primario es el castellano— y solo contenía un borrador sin publicar. Se
# renombró con redirección automática en vez de añadir un tercer blog: dos
# blogs ya reparten el poco enlace entrante que hay, y tres lo repartirían más.
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


# Las dos bases legales del catálogo no son la misma y el pie de fuentes no
# puede darlas por intercambiables. Los datos de nutrición y entrenamiento
# vienen de agencias federales estadounidenses (17 U.S.C. § 105); lo esotérico
# se apoya en la tradición común y el dominio público. Antes esta función
# firmaba siempre con el § 105, y el artículo del decanato salió publicado
# invocando una ley que no le tocaba.
_CIERRE = {
    "federal": (
        "<p>Los organismos del Gobierno de los Estados Unidos publican en "
        "abierto y sus obras <strong>no están sujetas a derechos de autor "
        "conforme al 17 U.S.C. § 105</strong>. Las cifras se pueden comprobar "
        "una por una; la redacción de este artículo es trabajo propio.</p>\n"
    ),
    "tradicion": (
        "<p>Este artículo no se apoya en fuentes oficiales sino en la "
        "<strong>tradición común y el dominio público</strong>: material que "
        "se transmite por escrito desde hace siglos y no pertenece a nadie. La "
        "redacción, la selección y el orden son trabajo propio.</p>\n"
    ),
}


def _fuentes(filas: str, base: str = "federal") -> str:
    if base not in _CIERRE:
        raise ValueError(f"base legal desconocida: {base}")
    titulo = ("De dónde sale cada cifra" if base == "federal"
              else "De dónde sale lo que aquí se cuenta")
    return (
        f"<h3>{titulo}</h3>\n"
        "<ul>\n" + filas + "</ul>\n" + _CIERRE[base]
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
            "<li>Las cifras de precesión son astronómicas y comprobables.</li>\n",
            base="tradicion"
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
    # ------------------------------------------------------------------ 6
    {
        "handle": "cuanta-proteina-hace-falta-al-dia",
        "titulo": "Cuánta proteína hace falta al día",
        "resumen": (
            "La cantidad oficial, por qué es un mínimo y no un objetivo, cómo "
            "se calcula con tu peso y qué pasa de verdad si te pasas."
        ),
        "etiquetas": ["nutrición", "proteína", "referencia"],
        "meta": (
            "Cuánta proteína hace falta al día | VILLUMINATIONS",
            "0,8 g por kilo es el mínimo oficial, no el objetivo de quien "
            "entrena. Cómo se calcula, cuánto absorbes de una vez y qué pasa "
            "si te pasas.",
        ),
        "cuerpo": """
<p>Es la pregunta que más se teclea sobre nutrición y la que peor se contesta,
porque hay dos cifras distintas circulando y casi nadie aclara que responden a
preguntas diferentes.</p>

<h2>La cifra oficial: 0,8 g por kilo</h2>

<p>La recomendación pública para una persona adulta sana es de
<strong>0,8 gramos de proteína por kilo de peso corporal y día</strong>. Para
setenta kilos son 56 gramos. La guía alimentaria federal la repite y el panel de
la etiqueta usa un valor diario de <strong>50 gramos</strong> como referencia.</p>

<p>Lo que casi nunca se dice es qué significa esa cifra. No es un óptimo: es la
cantidad que cubre las necesidades de <strong>casi toda</strong> la población
sana. Es un suelo pensado para que nadie se quede corto, no un techo ni una
meta. Confundir el suelo con el objetivo es el error del que salen todos los
demás.</p>

<h2>El otro rango: el de quien entrena</h2>

<p>Cuando hay entrenamiento de fuerza de por medio, las revisiones de nutrición
deportiva trabajan con un rango bastante más alto, entre
<strong>1,2 y 2,0 gramos por kilo</strong>, y con la parte alta reservada a
fases de déficit calórico, donde la proteína protege la masa magra mientras el
peso baja.</p>

<p>Conviene decir de dónde sale cada cosa: los 0,8 g/kg son una recomendación
pública de organismos federales; el rango de 1,2 a 2,0 procede de la literatura
de nutrición deportiva y de las tomas de postura de sociedades profesionales.
Son dos fuentes distintas y no se citan como si fueran la misma.</p>

<h2>El margen del 10 al 35 %</h2>

<p>Hay una tercera manera de mirarlo, por porcentaje de calorías. El rango
aceptable para la proteína en una dieta adulta va del <strong>10 al 35 % de las
calorías totales</strong>. Es amplio a propósito: dentro de ese margen hay
muchas dietas correctas y muy distintas entre sí.</p>

<p>Sirve de comprobación cruzada. Si haces los gramos por kilo y el resultado se
sale del 35 % de tus calorías, algo no cuadra en el reparto.</p>

<h2>«Solo se absorben 30 gramos de una vez»</h2>

<p>Esto se repite mucho y es falso tal como se dice. El intestino absorbe
prácticamente toda la proteína que le llega; lo que se satura no es la
absorción, sino el <strong>estímulo de síntesis muscular</strong> de una sola
comida, que llega a su techo en algún punto entre veinte y cuarenta gramos según
la persona y la cantidad de músculo que tenga.</p>

<p>La consecuencia práctica no es «no comas más de treinta», sino
<strong>repartir</strong>: tres o cuatro tomas con proteína a lo largo del día
aprovechan mejor que una cena enorme.</p>

<h2>Qué pasa si te pasas</h2>

<p>En una persona con los riñones sanos, no hay evidencia pública de daño renal
por comer más proteína de la recomendada. Lo que sí ocurre es más prosaico: la
proteína sacia mucho, y cada gramo que entra por ahí es un gramo que no entra
por otro sitio. Comer 3 g/kg no es peligroso, es simplemente
<strong>innecesario</strong> y desplaza a los hidratos que alimentan el
entrenamiento.</p>

<p>Quien tenga una enfermedad renal diagnosticada está en otro escenario y esa
cifra la fija su médico, no un artículo.</p>

<h2>Cómo se calcula en treinta segundos</h2>

<ul>
  <li>Peso en kilos × 0,8 → el mínimo para no quedarse corto.</li>
  <li>Peso en kilos × 1,6 → punto de partida razonable si entrenas fuerza.</li>
  <li>Divide el resultado entre las comidas que haces al día.</li>
</ul>

<p>Con setenta kilos: 56 g de suelo, 112 g como objetivo entrenando, unos 28 g
en cada una de cuatro comidas.</p>

""" + _fuentes(
            "<li>Los 0,8 g/kg y el rango del 10 al 35 % de las calorías son "
            "recomendaciones publicadas por organismos del Gobierno de los "
            "Estados Unidos.</li>\n"
            "<li>El valor diario de 50 g es el que fija la norma de etiquetado "
            "para el panel nutricional.</li>\n"
            "<li>El rango de 1,2 a 2,0 g/kg procede de la literatura de "
            "nutrición deportiva, no de una recomendación federal, y así se "
            "dice en el texto.</li>\n"
        ) + ETIQUETA.format(
            frase="El reparto por comidas, las tablas de contenido proteico por "
                  "alimento y cómo encaja la proteína con el resto del día están "
                  "desarrollados entero.",
            handle="codice-de-la-mesa", libro="el Códice de la Mesa", paginas="78",
        ) + FIRMA,
    },
    # ------------------------------------------------------------------ 7
    {
        "handle": "gimnasio-en-casa-que-comprar-primero",
        "titulo": "Gimnasio en casa: qué comprar primero",
        "resumen": (
            "El orden en que conviene gastar el dinero, qué resuelve cada "
            "pieza y las tres compras que casi todo el mundo hace demasiado "
            "pronto."
        ),
        "etiquetas": ["equipo", "entrenamiento", "guía"],
        "meta": (
            "Gimnasio en casa: qué comprar primero | VILLUMINATIONS",
            "El orden en que conviene gastar: suelo, banco, barra, bandas. Qué "
            "resuelve cada pieza y las tres compras que se hacen demasiado "
            "pronto.",
        ),
        "cuerpo": """
<p>Montar un gimnasio en casa sale mal casi siempre por lo mismo: se compra por
ilusión y no por orden. Este es el orden que aguanta, con el criterio detrás de
cada paso.</p>

<h2>Antes de comprar nada: cuánto hace falta entrenar</h2>

<p>La recomendación pública de actividad física para personas adultas son
<strong>150 minutos semanales</strong> de actividad aeróbica moderada —o 75 de
intensidad alta— más <strong>dos días de trabajo de fuerza</strong> que
involucren los grandes grupos musculares.</p>

<p>Eso define lo que hay que comprar. Dos sesiones de fuerza a la semana no
piden una sala entera: piden poder cargar los patrones básicos —empujar, tirar,
flexionar cadera y rodilla— con una progresión posible.</p>

<h2>1. El suelo, antes que el hierro</h2>

<p>Es la compra menos emocionante y la que más se agradece. Unas
<a href="/collections/equipo">losetas encajables</a> hacen tres cosas: protegen
el suelo de la casa, amortiguan las articulaciones y delimitan un espacio que
tu cabeza reconoce como «aquí se entrena». Lo tercero no es místico: reduce la
fricción de empezar, que es donde se abandona.</p>

<h2>2. Un banco regulable</h2>

<p>Es la pieza que más ejercicios desbloquea por dólar gastado. Con un banco que
se incline, se abata y se ponga plano tienes press en tres ángulos, remo
apoyado, extensiones lumbares y todo el trabajo de brazo sentado. Sin él, media
lista de ejercicios no existe.</p>

<p>Al comparar bancos, mira la carga admitida que declara el fabricante y las
posiciones reales de respaldo. Un banco de tres posiciones y uno de siete no son
el mismo mueble.</p>

<h2>3. Carga que progrese</h2>

<p>La fuerza depende de poder <strong>subir la carga poco a poco</strong>. Ese
es el criterio para elegir entre una barra con discos, un juego de mancuernas
regulables o una máquina de carga con discos: la pregunta no es cuánto levanta
hoy, sino en cuántos escalones puede subir.</p>

<p>Una barra hexagonal es, para casa, la más agradecida: permite peso muerto con
la espalda en mejor posición que la barra recta y sirve también para encogimientos
y zancadas.</p>

<h2>4. Bandas y chaleco, cuando ya hay rutina</h2>

<p>Las bandas resuelven lo que el peso libre hace peor —abducciones, activación
de glúteo, trabajo accesorio— y ocupan un cajón. El chaleco lastrado convierte
en entrenamiento algo que ya hacías: caminar. Ninguna de las dos es una primera
compra; las dos son excelentes cuartas compras.</p>

<h2>Las tres compras prematuras</h2>

<ul>
  <li><strong>Una máquina grande de un solo ejercicio.</strong> Ocupa lo que
  ocupa un banco y una barra juntos y hace una cosa. Tiene sentido cuando ese
  ejercicio concreto es el eje de tu programa, no antes.</li>
  <li><strong>Mancuernas fijas por pares.</strong> Se quedan cortas en dos meses
  y no hay escalón siguiente.</li>
  <li><strong>Accesorios antes que carga.</strong> Rodillos, poleas pequeñas,
  agarres. Todos útiles, ninguno mueve la aguja si aún no puedes progresar en
  los básicos.</li>
</ul>

<h2>La lista corta</h2>

<ul>
  <li>Losetas para dos metros cuadrados.</li>
  <li>Banco regulable.</li>
  <li>Una barra y discos, o carga regulable equivalente.</li>
  <li>Un juego de bandas.</li>
</ul>

<p>Con eso se cubren los dos días de fuerza de la recomendación pública durante
años. Todo lo demás es afinado, y se compra cuando el programa lo pide.</p>

""" + _fuentes(
            "<li>Los 150 minutos semanales y los dos días de fuerza son la "
            "recomendación de actividad física publicada por el Gobierno de los "
            "Estados Unidos.</li>\n"
            "<li>Las cargas admitidas y las medidas de cada pieza salen de la "
            "documentación del fabricante y solo se publican cuando esa "
            "documentación no se contradice a sí misma.</li>\n"
        ) + ETIQUETA.format(
            frase="La progresión de cargas semana a semana, los patrones básicos "
                  "y cómo se ordena una sesión con este material están "
                  "desarrollados entero.",
            handle="codice-de-la-carga", libro="el Códice de la Carga", paginas="70",
        ) + FIRMA,
    },
    # ------------------------------------------------------------------ 8
    {
        "handle": "que-es-un-arcano-mayor",
        "titulo": "Qué es un arcano mayor",
        "resumen": (
            "Los veintidós, por qué el Loco lleva un cero, en qué se "
            "diferencian de los menores y qué significa realmente que una "
            "carta salga «del revés»."
        ),
        "etiquetas": ["simbolismo", "arcanos", "referencia"],
        "meta": (
            "Qué es un arcano mayor | VILLUMINATIONS",
            "Los veintidós arcanos mayores, por qué el Loco lleva un cero, la "
            "diferencia con los menores y qué significa una carta invertida.",
        ),
        "cuerpo": """
<p>«Arcano» significa simplemente <em>secreto</em>, y en la baraja designa a las
cartas que no pertenecen a ningún palo. Son veintidós y forman una secuencia
cerrada que se transmite por escrito desde hace siglos.</p>

<h2>Veintidós cartas y dos barajas dentro de una</h2>

<p>Una baraja completa tiene setenta y ocho cartas repartidas en dos bloques muy
distintos:</p>

<ul>
  <li>Los <strong>arcanos menores</strong>, cincuenta y seis cartas en cuatro
  palos con sus figuras. Son la estructura que heredó la baraja de juego
  corriente.</li>
  <li>Los <strong>arcanos mayores</strong>, veintidós cartas sueltas, numeradas
  y con nombre propio.</li>
</ul>

<p>Los menores hablan de circunstancias; los mayores, de procesos. Esa es la
diferencia funcional, y explica por qué en una lectura un mayor «pesa» más: no
describe un episodio, describe la corriente en la que ocurre.</p>

<h2>Por qué el Loco lleva un cero</h2>

<p>Es la rareza más famosa del sistema y no es un capricho. Veintiuna cartas van
numeradas del I al XXI; el Loco queda fuera de esa cuenta y por eso se le asigna
el <strong>cero</strong>, un número que en las barajas antiguas simplemente no
estaba.</p>

<p>La consecuencia es que el Loco no tiene sitio fijo. Puede leerse al principio
—lo que aún no ha empezado— o al final —lo que vuelve al mundo después de
haberlo recorrido—, y las dos colocaciones tienen tradición detrás. Un sistema
que deja una pieza sin posición fija está diciendo algo sobre sí mismo: la
secuencia es un recorrido, no una escalera.</p>

<h2>La secuencia como recorrido</h2>

<p>Leídos en orden, los veintiún numerados describen un trayecto reconocible:
primero las figuras de autoridad y aprendizaje, después las pruebas y los
vuelcos, y al final las cartas grandes de disolución y recomposición. No hace
falta creer en nada para ver el patrón; es la misma armadura que tienen los
relatos de viaje desde mucho antes de que existiera la baraja.</p>

<p>De ahí sale la costumbre de agruparlos en <strong>tres tramos de siete</strong>.
Es una lectura tardía y no la única, pero ordena bien la memoria.</p>

<h2>Qué significa una carta invertida</h2>

<p>Que una carta salga del revés no invierte su significado como un signo menos.
En la tradición se lee como el mismo contenido en otra intensidad o en otra
dirección: bloqueado, todavía interior, excesivo o ya agotado.</p>

<p>Hay escuelas enteras que no usan inversiones y leen las setenta y ocho
siempre derechas. Ninguna de las dos posturas es la correcta: son convenios de
lectura, y lo que importa es no mezclarlos a media tirada.</p>

<h2>Lo que esto no es</h2>

<p>Conviene decirlo claro. Los arcanos son un <strong>lenguaje simbólico</strong>
de dominio público: un vocabulario muy trabajado para nombrar estados y
procesos. No anuncian hechos futuros, no diagnostican nada y no sustituyen a un
médico ni a un psicólogo colegiado.</p>

<p>Usados como espejo funcionan; usados como pronóstico, no. Quien te venda lo
segundo te está vendiendo otra cosa.</p>

""" + _fuentes(
            "<li>La secuencia de los veintidós arcanos, su numeración y las "
            "convenciones de lectura se transmiten por escrito desde hace siglos "
            "en obras de <strong>dominio público</strong>, y no son propiedad de "
            "nadie.</li>\n"
            "<li>La redacción, la selección y el orden de este artículo son "
            "trabajo propio.</li>\n",
            base="tradicion"
        ) + ETIQUETA.format(
            frase="Los veintidós uno por uno, con su lámina, sus correspondencias "
                  "clásicas y las dos convenciones de inversión enfrentadas, no "
                  "caben en un artículo.",
            handle="codice-de-los-arcanos", libro="el Códice de los Arcanos",
            paginas="62",
        ) + (
            '<p><em>Publicado por VILLUMINATIONS. El tarot que se practica aquí '
            'es un lenguaje simbólico, no una ciencia predictiva: nada de lo que '
            'se dice anuncia hechos futuros ni sustituye la atención de un '
            'profesional sanitario.</em></p>'
        ),
    },
    # ------------------------------------------------------------------ 9
    {
        "handle": "como-elegir-una-proteina-en-polvo",
        "titulo": "Cómo elegir una proteína en polvo",
        "resumen": (
            "Concentrado, aislado o vegetal; qué mirar en el panel antes que "
            "el precio del bote, y las dos trampas de etiqueta que hacen que "
            "pagues por menos proteína de la que crees."
        ),
        "etiquetas": ["proteína", "suplementos", "guía"],
        "meta": (
            "Cómo elegir una proteína en polvo | VILLUMINATIONS",
            "Concentrado, aislado o vegetal, el coste por gramo de proteína y "
            "las dos trampas de etiqueta que hacen que pagues por menos de lo "
            "que crees.",
        ),
        "cuerpo": """
<p>Casi todo el mundo elige la proteína por el precio del bote, y el precio del
bote es el dato menos informativo de la etiqueta. Estas son las cuatro
decisiones reales, en el orden en que importan.</p>

<h2>1. El coste por gramo de proteína, no por bote</h2>

<p>Es la única comparación honesta y se hace en diez segundos: divide el precio
entre los gramos de proteína totales del envase. Los gramos totales son
<em>raciones por envase × gramos de proteína por ración</em>, y las dos cifras
están en el panel.</p>

<p>Dos botes al mismo precio pueden llevar el doble de proteína uno que otro,
porque el peso del envase incluye cacao, aromas, espesantes y azúcar. La
báscula pesa el polvo; tú pagas por la proteína.</p>

<h2>2. Concentrado, aislado o vegetal</h2>

<p>La diferencia entre los dos primeros es cuánto se ha filtrado el suero:</p>

<ul>
  <li><strong>Concentrado.</strong> Menos filtrado, así que lleva algo más de
  grasa y de lactosa y algo menos de proteína por gramo de polvo. Es el más
  barato y, si la lactosa no te da problemas, es una elección perfectamente
  razonable.</li>
  <li><strong>Aislado.</strong> Más filtrado: más proteína por gramo y muy poca
  lactosa. Cuesta más. Tiene sentido si te sienta mal el concentrado o si
  cuentas los macros con precisión.</li>
  <li><strong>Vegetal.</strong> Guisante, haba, arroz o mezclas. La razón para
  elegirla no es que sea «mejor»: es que no lleva lácteos. Conviene que el
  perfil de aminoácidos esenciales esté completo, y eso lo consiguen las
  mezclas mejor que una sola fuente.</li>
</ul>

<p>Para casi todo el mundo, la diferencia práctica entre las tres es pequeña al
lado de llegar a la proteína total del día, que es lo que de verdad mueve la
aguja.</p>

<h2>3. Las dos trampas de la etiqueta</h2>

<h3>La mezcla sin cantidades</h3>

<p>Si la etiqueta lista una «mezcla patentada» con ocho ingredientes y una sola
cifra al final, no puedes saber cuánto hay de cada uno. Ese es exactamente el
motivo por el que se presenta así. La regla es simple: <strong>si no puedes
comparar dos productos con lo que dice la etiqueta, la etiqueta está haciendo
su trabajo y tú no puedes hacer el tuyo</strong>.</p>

<h3>El relleno con aminoácidos sueltos</h3>

<p>La cantidad de proteína declarada se calcula, en la práctica, a partir del
nitrógeno. Aminoácidos baratos como la glicina o la taurina aportan nitrógeno
sin aportar una proteína completa, así que añadirlos sube la cifra del panel sin
subir lo que le sirve al músculo.</p>

<p>Cómo detectarlo: mira la lista de ingredientes. Si aparecen aminoácidos
sueltos <em>antes</em> o justo después de la fuente proteica, y el producto es
llamativamente barato por gramo, desconfía. Una proteína honesta empieza su
lista por la proteína.</p>

<h2>4. Lo que no debería influir en la decisión</h2>

<ul>
  <li><strong>El sabor de la foto.</strong> Cambia entre lotes y no dice nada
  del contenido.</li>
  <li><strong>«Sin azúcar».</strong> Suele significar edulcorado con otra cosa.
  Legítimo, pero no es un dato de calidad.</li>
  <li><strong>Las promesas del envase.</strong> Un complemento alimenticio no
  pasa por autorización previa antes de venderse, así que lo que promete el bote
  no lo ha validado nadie. Está desarrollado en
  <a href="/blogs/diario/que-suplementos-tienen-evidencia">qué suplementos
  tienen evidencia y cuáles no</a>.</li>
</ul>

<h2>La comprobación de treinta segundos</h2>

<ol>
  <li>Gramos de proteína por ración ÷ gramos de polvo por ración. Por encima de
  0,7 es un producto denso; por debajo de 0,6, estás comprando bastante relleno.</li>
  <li>Precio ÷ gramos de proteína del envase. Ese es el número que compara.</li>
  <li>Primera línea de la lista de ingredientes: ¿es la proteína?</li>
  <li>¿Hay alguna «mezcla patentada» sin cantidades? Si la hay, siguiente
  producto.</li>
</ol>

<p>Con eso se descarta la mayor parte del mercado sin leer una sola reseña. Las
que hay <a href="/collections/suplementos">en esta tienda</a> declaran los
gramos por toma y la lista completa de ingredientes en la ficha, que es lo que
hace falta para hacer esta cuenta.</p>

""" + _fuentes(
            "<li>Las reglas del panel de información nutricional, la lista de "
            "ingredientes por orden de peso y el régimen de los complementos "
            "alimenticios —sin autorización previa a la venta— los publica la "
            "autoridad federal de alimentos y medicamentos.</li>\n"
            "<li>El cálculo de proteína a partir del nitrógeno es el método "
            "analítico recogido en la propia norma de etiquetado.</li>\n"
        ) + ETIQUETA.format(
            frase="El reparto de la proteína por comidas, las tablas de "
                  "contenido por alimento y cómo encaja con el resto del día "
                  "están desarrollados entero.",
            handle="codice-de-la-mesa", libro="el Códice de la Mesa", paginas="78",
        ) + FIRMA,
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
