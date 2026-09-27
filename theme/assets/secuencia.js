/* Villumination - Secuencia de marca. El motor.
   ==================================================================
   QUE ES. Cinco escenas que se suceden solas, en bucle, debajo de la
   cabecera de la portada. Es lo segundo que ve quien llega, despues de la
   intro, y funciona como el video de una marca -- salvo que no es un video:

     - El texto es texto de verdad. Google lo indexa, un lector de pantalla
       lo lee y se traduce con el resto del tema. Un .mp4 no hace ninguna de
       las tres cosas.
     - Pesa kilobytes, no megabytes, y se ve nitido en cualquier pantalla.
     - Reacciona al dedo y al raton.

   POR QUE SE REESCRIBIO. La version anterior hacia lo correcto por dentro y
   se veia mal por fuera, y casi todo venia de una sola linea de la hoja de
   estilos: `filter: blur(5px)` sobre el lienzo ENTERO. Ese desenfoque estaba
   para disimular que los haces eran poligonos con los bordes rectos, pero al
   aplicarse a todo se llevaba por delante tambien el marco y el texto del
   fondo. El resultado, en una captura, era exactamente lo que parece un
   video mal comprimido: barras verticales borrosas.

   LA IDEA DE AHORA: SEPARAR LA LUZ DE LA GEOMETRIA.

     - Lo BLANDO -- haces, resplandor del suelo, bruma -- se pinta en un
       lienzo aparte a un sexto de resolucion y se estira encima. El propio
       escalado del navegador lo suaviza, que es lo que hace de verdad una
       camara con la luz, y sale gratis: son treinta y seis veces menos
       pixeles que pintar.
     - Lo NITIDO -- corchetes, polvo, riel de progreso -- se pinta a
       resolucion completa encima. Nada de esto se desenfoca jamas.

   Esa sola separacion es la diferencia entre "parece un video" y "parece un
   video malo".

   EL RITMO. El tiempo ya no se reparte a partes iguales. La marca es una
   palabra y los tres pilares son nueve lineas de texto: darles los mismos
   segundos era la razon de que unas escenas se leyeran con prisa y otras se
   quedaran esperando. Cada tipo de escena tiene su peso.

   EL REPARTO DE TAREAS CON LA HOJA DE ESTILOS. El motor solo dice CUANDO:
   a cada escena le pone `--p`, su progreso local de 0 a 1. El COMO -- que la
   marca se componga letra a letra, que los pilares se apilen en orden, que
   la cifra suba como un cuentakilometros -- vive entero en el CSS. Asi la
   coreografia se puede cambiar sin tocar una linea de JavaScript.

   SE PARA fuera de pantalla, con la pestana oculta y con movimiento
   reducido. En ese ultimo caso pinta el fotograma final, que es el que lleva
   la llamada a la accion: quien pide menos movimiento tambien tiene derecho
   a ver el boton.
*/
(function () {
  'use strict';

  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  var vivos = [];

  /* Cuanto dura cada escena, en partes. La suma no importa: se normaliza
     con las escenas que existan de verdad, porque la seccion permite quitar
     bloques desde el editor.

     Los numeros salen de contar lo que hay que LEER en cada una. La marca es
     una palabra; los pilares son tres titulos y tres subtitulos, nueve veces
     mas texto. Antes las dos tenian los mismos segundos. */
  var PESOS = { marca: 0.85, lema: 1.05, pilares: 1.65, cifra: 0.95, cierre: 1.5 };

  function lim(v, a, b) { return v < a ? a : (v > b ? b : v); }
  function suave(x) { x = lim(x, 0, 1); return x * x * (3 - 2 * x); }
  function salida(x) { x = lim(x, 0, 1); return 1 - Math.pow(1 - x, 3); }

  /* La ventana de una escena: sube en `cruce`, se mantiene y baja en `cruce`.
     Los dos lados usan el mismo suavizado, asi que al cruzarse dos escenas
     la suma no se hunde. Fuera de [de, a] vale cero. */
  function ventanaEn(t, de, a, cruce) {
    if (t < de || t > a) return 0;
    return Math.min(suave((t - de) / cruce), suave((a - t) / cruce));
  }

  function montar(raiz) {
    if (!raiz || raiz.dataset.secListo === '1') return;
    raiz.dataset.secListo = '1';

    var lienzo = raiz.querySelector('[data-sec-lienzo]');
    var escenas = raiz.querySelectorAll('[data-sec-escena]');
    if (!lienzo || !escenas.length) return;

    var ctx = null;
    try { ctx = lienzo.getContext('2d'); } catch (e2) { return; }
    if (!ctx) return;

    /* El lienzo de la luz. Va aparte y a un sexto de escala. */
    var luz = document.createElement('canvas');
    var lctx = null;
    try { lctx = luz.getContext('2d'); } catch (e3) {}

    var DUR = parseFloat(raiz.dataset.secDuracion) || 18;
    var W = 0, H = 0, LW = 0, LH = 0, raf = 0, aLaVista = false, t0 = null, ultimo = -1e9;
    var punteroX = 0.5, punteroY = 0.5, tocando = 0;

    /* SESENTA fotogramas donde se pueda. La version anterior iba fija a 30
       para ahorrar, y a 30 una camara lenta se ve a tirones: el ojo humano
       distingue perfectamente un barrido de luz a 30 de uno a 60. En un
       aparato flojo o con ahorro de datos se baja a 24 y se reduce la
       resolucion, que es donde de verdad esta el coste. */
    /* El tope de densidad baja de 2 a 1,4: lo que se pinta a pantalla
       completa -- vineta, grano, luz -- cuesta el CUADRADO de este
       numero, asi que 2 costaba cuatro veces mas que 1. A 1,4 los
       corchetes y el riel siguen viendose finos y el coste baja a la
       mitad. */
    var MS = 1000 / 60, tope = 1.4;
    try {
      var nucleos = navigator.hardwareConcurrency || 8;
      var ahorro = navigator.connection && navigator.connection.saveData;
      if (nucleos <= 4 || ahorro) { MS = 1000 / 24; tope = 1; }
      else if (nucleos <= 6) { MS = 1000 / 30; tope = 1.2; }
    } catch (e4) {}

    function medir() {
      var dpr = Math.min(window.devicePixelRatio || 1, tope);
      var w = Math.max(1, Math.round(raiz.offsetWidth * dpr));
      var h = Math.max(1, Math.round(raiz.offsetHeight * dpr));
      if (w === W && h === H) return;
      lienzo.width = W = w; lienzo.height = H = h;
      LW = Math.max(1, Math.round(W / 6));
      LH = Math.max(1, Math.round(H / 6));
      luz.width = LW; luz.height = LH;
    }

    /* ---------- 1. LA LUZ, a un sexto de escala ----------
       Todo lo que aqui se pinta va a estirarse seis veces, asi que puede
       dibujarse a brochazos: no hay borde que se vaya a notar. */
    function pintarLuz(t) {
      if (!lctx) return;
      lctx.clearRect(0, 0, LW, LH);

      /* LOS HACES, Y POR QUE NO SON POLIGONOS.
         La primera version los dibujaba como trapecios con un degradado a lo
         largo. El degradado suaviza el haz por arriba y por abajo, pero los
         LADOS se quedan rectos: en la pantalla eso se lee como un zigzag de
         cunas de color, que es geometria, no luz. Es lo mismo que pasaba
         antes y lo que el desenfoque general venia a tapar.

         Un degradado RADIAL no tiene lados: se apaga en todas las
         direcciones a la vez. Cada haz es una pila de tres manchas radiales
         estiradas a lo alto, superpuestas y sumadas. No hay un solo borde
         recto en todo el fondo.

         Se inclinan hacia donde esta el dedo o el raton: es la parte que
         responde al visitante, y es deliberadamente sutil para acompanar sin
         robarle la atencion a lo que se vende. */
      var sesgo = (punteroX - 0.5) * 0.9;
      lctx.globalCompositeOperation = 'lighter';
      var colores = [[0, 240, 255], [139, 92, 246], [255, 46, 203]];
      var n = 6;
      for (var i = 0; i < n; i++) {
        var fase = t * 0.32 + i * 1.5;
        var c = colores[i % 3];
        var base = (i + 0.5) / n + Math.sin(fase) * 0.045;
        var a = (0.17 + 0.10 * Math.sin(fase * 1.12 + 1)) * (1 + tocando * 0.55);
        for (var j = 0; j < 3; j++) {
          /* Cada mancha baja un poco mas y se abre un poco mas, como se abre
             un haz al alejarse del foco. */
          var f = j / 2;
          var cx = LW * (base + sesgo * (0.18 + f * 0.5));
          var cy = LH * (0.04 + f * 0.62);
          var r = LW * (0.13 + f * 0.13) * (1 + 0.10 * Math.sin(fase * 0.8));
          var g = lctx.createRadialGradient(cx, cy, 0, cx, cy, r);
          var aj = a * (1 - f * 0.45);
          g.addColorStop(0, 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + aj.toFixed(3) + ')');
          g.addColorStop(0.45, 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + (aj * 0.34).toFixed(3) + ')');
          g.addColorStop(1, 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',0)');
          lctx.save();
          /* Estirada a lo alto: un circulo aplastado es un haz. */
          lctx.translate(cx, cy);
          lctx.scale(1, 2.5 - f * 0.9);
          lctx.translate(-cx, -cy);
          lctx.fillStyle = g;
          lctx.beginPath();
          lctx.arc(cx, cy, r, 0, 6.2832);
          lctx.fill();
          lctx.restore();
        }
      }

      /* El suelo. Una sola banda de luz abajo, que es lo que convierte esto
         de "fondo abstracto" en "sitio": la luz tiene que caer en algo. */
      var suelo = lctx.createLinearGradient(0, LH * 0.62, 0, LH);
      suelo.addColorStop(0, 'rgba(0,240,255,0)');
      suelo.addColorStop(0.72, 'rgba(0,200,235,' + (0.10 + tocando * 0.05).toFixed(3) + ')');
      suelo.addColorStop(1, 'rgba(120,80,255,0.05)');
      lctx.fillStyle = suelo;
      lctx.fillRect(0, LH * 0.62, LW, LH * 0.38);

      /* Bruma: dos manchas lentas que se cruzan. Rompen la simetria de los
         haces, que si no se leen como un patron repetido. */
      for (var b = 0; b < 2; b++) {
        var bx = LW * (0.5 + 0.34 * Math.sin(t * 0.13 + b * 2.1));
        var by = LH * (0.45 + 0.2 * Math.cos(t * 0.09 + b * 1.3));
        var r = Math.max(LW, LH) * 0.45;
        var gb = lctx.createRadialGradient(bx, by, 0, bx, by, r);
        gb.addColorStop(0, b ? 'rgba(255,46,203,0.075)' : 'rgba(0,240,255,0.085)');
        gb.addColorStop(1, 'rgba(0,0,0,0)');
        lctx.fillStyle = gb;
        lctx.fillRect(0, 0, LW, LH);
      }
      lctx.globalCompositeOperation = 'source-over';
    }

    /* ---------- 2. EL POLVO, a resolucion completa ----------
       Particulas flotando en la luz. Son lo unico del fondo que se pinta
       nitido, y por eso funcionan: dan una referencia de foco que hace que
       la luz de detras se lea como profundidad y no como desenfoque. */
    var motas = [];
    function sembrarMotas() {
      motas = [];
      var cuantas = W < 900 ? 26 : 44;
      for (var i = 0; i < cuantas; i++) {
        motas.push({
          x: Math.random(), y: Math.random(),
          v: 0.006 + Math.random() * 0.016,
          r: 0.4 + Math.random() * 1.5,
          f: Math.random() * 6.28,
          a: 0.16 + Math.random() * 0.34
        });
      }
    }
    function pintarMotas(t) {
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      for (var i = 0; i < motas.length; i++) {
        var m = motas[i];
        /* Suben despacio y vuelven por abajo. El seno las mece de lado, que
           es como se mueve una mota de polvo de verdad en una corriente. */
        var y = (m.y - t * m.v) % 1; if (y < 0) y += 1;
        var x = m.x + Math.sin(t * 0.35 + m.f) * 0.012 + (punteroX - 0.5) * 0.02;
        var brillo = m.a * (0.55 + 0.45 * Math.sin(t * 1.4 + m.f));
        ctx.fillStyle = 'rgba(190,245,255,' + brillo.toFixed(3) + ')';
        ctx.beginPath();
        ctx.arc(x * W, y * H, m.r * (W / 900 + 0.6), 0, 6.2832);
        ctx.fill();
      }
      ctx.restore();
    }

    /* ---------- 3. LOS CORCHETES ----------
       Cuatro escuadras en las esquinas en vez del rectangulo completo que
       habia antes. Un rectangulo cerrado alrededor del texto es un borde de
       diapositiva; cuatro escuadras son un visor -- el encuadre de una
       camara, el marco de una placa -- y ademas dejan respirar la
       composicion por los cuatro lados.

       Entran trazandose en los primeros 1,4 s y luego respiran. */
    function pintarCorchetes(t) {
      var m = Math.min(W, H) * 0.062;
      var x0 = m, y0 = m, x1 = W - m, y1 = H - m;
      var largo = Math.min(W, H) * 0.14;
      var hecho = t < 1.4 ? salida(t / 1.4) : 1;
      var lat = largo * hecho;
      var respira = 0.72 + 0.28 * Math.sin(t * 1.15) + tocando * 0.3;

      ctx.save();
      ctx.lineWidth = Math.max(2, Math.min(W, H) * 0.0055);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      /* Mas brillo que antes: la vineta ahora vive en la hoja de estilos y se
         pinta POR ENCIMA del lienzo, asi que tambien apaga los corchetes.
         Esto lo compensa. */
      ctx.strokeStyle = 'rgba(190,250,255,' + lim(0.68 * respira + 0.3, 0, 1).toFixed(3) + ')';
      ctx.shadowColor = 'rgba(0,240,255,0.8)';
      ctx.shadowBlur = Math.min(W, H) * 0.022 * respira;

      var esquinas = [[x0, y0, 1, 1], [x1, y0, -1, 1], [x1, y1, -1, -1], [x0, y1, 1, -1]];
      for (var i = 0; i < 4; i++) {
        var q = esquinas[i];
        ctx.beginPath();
        ctx.moveTo(q[0] + q[2] * lat, q[1]);
        ctx.lineTo(q[0], q[1]);
        ctx.lineTo(q[0], q[1] + q[3] * lat);
        ctx.stroke();
      }
      ctx.restore();
    }

    /* ---------- 4. EL RIEL ----------
       Una linea fina abajo que se llena a lo largo del ciclo. Sin esto, el
       visitante no sabe si lo que esta mirando va a alguna parte o se quedo
       colgado, y en una portada esa duda se paga cerrando la pestana. */
    function pintarRiel(t) {
      var m = Math.min(W, H) * 0.062;
      var y = H - m * 0.44;
      var x0 = m, x1 = W - m;
      var p = lim(t / DUR, 0, 1);
      ctx.save();
      ctx.lineWidth = Math.max(1.5, Math.min(W, H) * 0.0035);
      ctx.lineCap = 'round';
      ctx.strokeStyle = 'rgba(160,220,255,0.22)';
      ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
      var g = ctx.createLinearGradient(x0, 0, x1, 0);
      g.addColorStop(0, 'rgba(0,240,255,0.95)');
      g.addColorStop(0.55, 'rgba(139,92,246,0.95)');
      g.addColorStop(1, 'rgba(255,46,203,0.95)');
      ctx.strokeStyle = g;
      ctx.shadowColor = 'rgba(0,240,255,0.7)';
      ctx.shadowBlur = Math.min(W, H) * 0.014;
      ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x0 + (x1 - x0) * p, y); ctx.stroke();
      ctx.restore();
    }

    /* ---------- 5. VINETA Y GRANO ---------- */
    /* LA VINETA Y EL GRANO YA NO SE PINTAN AQUI.
       Estaban en el lienzo y costaban 4,4 ms de cada fotograma: dos rellenos
       a pantalla completa, sesenta veces por segundo, para dibujar algo que
       NO CAMBIA. Ahora viven en la hoja de estilos como dos capas encima del
       lienzo: el navegador las pinta una vez y despues solo las compone, que
       es trabajo de la tarjeta grafica y no del hilo que tiene que cargar la
       tienda. El grano se queda quieto: moverlo era bonito y volvia a costar
       un repintado por fotograma. */

    /* ---------- el reparto del tiempo ----------
       Se calcula una vez y se guarda: entrada, salida y peso de cada escena.
       Las ventanas se solapan un 16 % para que NUNCA haya un fotograma con
       todas las escenas apagadas -- ese hueco en negro era uno de los fallos
       que el detector encontro en la version anterior de esta seccion. */
    var tramos = [], CRUCE = 0.5;
    function repartir() {
      tramos = [];
      var total = 0, i;
      for (i = 0; i < escenas.length; i++) {
        var tipo = escenas[i].getAttribute('data-sec-tipo') || '';
        total += (PESOS[tipo] || 1);
      }
      var acum = 0;
      for (i = 0; i < escenas.length; i++) {
        var w = (PESOS[escenas[i].getAttribute('data-sec-tipo') || ''] || 1) / total;
        tramos.push({ de: acum * DUR, dura: w * DUR });
        acum += w;
      }
      /* EL CRUCE ES UNO SOLO PARA TODAS, y esa es la clave. Con un cruce
         proporcional a cada escena, la que sale y la que entra usaban
         curvas de duraciones distintas: no eran espejo la una de la otra y
         en algunos instantes las DOS se leian a la vez. Con un unico valor,
         cualquier cambio es la misma disolvencia simetrica -- las dos a 0,5
         en el punto medio -- y eso vale igual para la costura del bucle,
         donde se cruzan la ultima escena y la primera. */
      CRUCE = Math.min(0.62, DUR * 0.035);
    }

    /* ---------- un fotograma ---------- */
    function pintar(t) {
      ctx.fillStyle = raiz.dataset.secFondo || '#05060a';
      ctx.fillRect(0, 0, W, H);

      pintarLuz(t);
      if (lctx) {
        ctx.save();
        ctx.imageSmoothingEnabled = true;
        /* Se estira un pelin mas grande que el lienzo y centrado, para que
           el suavizado de los bordes caiga fuera de la vista. */
        ctx.drawImage(luz, -W * 0.02, -H * 0.02, W * 1.04, H * 1.04);
        ctx.restore();
      }
      pintarMotas(t);
      pintarCorchetes(t);
      pintarRiel(t);

      for (var i = 0; i < escenas.length; i++) {
        var tr = tramos[i];
        /* EL CRUCE, Y POR QUE ES SIMETRICO.
           La primera version entraba en el 26 % de su tramo y salia en el
           30 %, con un solape del 16 %. Los numeros no cuadraban: en mitad
           del cambio la que se iba estaba ya por debajo de 0,18 y la que
           llegaba todavia por debajo de 0,23, asi que durante unos
           fotogramas la pantalla se quedaba practicamente a oscuras. El
           detector conto doce de cada ciento setenta.

           Ahora la entrada, la salida y el solape valen lo mismo, 0,25, y
           los dos suavizados son el mismo espejado: se cruzan a la mitad,
           los dos a 0,5, y la suma no baja nunca. Es una disolvencia de
           verdad, no dos desvanecidos que se persiguen. */
        var de = tr.de, a = tr.de + tr.dura + CRUCE;
        /* Y EL BUCLE TIENE QUE CERRAR. La ultima escena termina PASADO el
           final del ciclo, y la primera empieza en cero: al dar la vuelta
           quedaba un salto en negro justo en la costura. Se mira la ventana
           tambien una vuelta antes y una despues, y se queda la mayor: asi
           el final y el principio se solapan como cualquier otro cambio. */
        var o = Math.max(
          ventanaEn(t, de, a, CRUCE),
          Math.max(ventanaEn(t + DUR, de, a, CRUCE),
                   ventanaEn(t - DUR, de, a, CRUCE)));

        var e = escenas[i];

        /* SOLO SE ESCRIBE EN LAS ESCENAS QUE ESTAN ENCENDIDAS, Y ESA ES LA
           OPTIMIZACION QUE IMPORTA. Cambiar una propiedad personalizada
           obliga al navegador a recalcular el estilo de TODO lo que cuelga
           del elemento: las trece letras de la marca, los tres pilares con
           sus seis textos... Hacerlo en las cinco escenas sesenta veces por
           segundo era la mayor parte del coste, y la compuerta lo vio como
           una portada que tardaba casi cinco segundos en pintarse.

           En cualquier instante hay UNA escena encendida, o dos en mitad de
           un cruce. Las otras tres o cuatro no necesitan saber la hora: si
           ya estaban apagadas, se las deja en paz. */
        var apagada = o <= 0.0005;
        if (apagada && e._secApagada) continue;
        e._secApagada = apagada;

        /* p: el progreso DENTRO de la escena, de 0 a 1. Es todo el contrato
           con la hoja de estilos; el resto de la coreografia vive alli. */
        var p = lim((t - de) / tr.dura, 0, 1);
        e.style.opacity = o;
        e.style.setProperty('--p', p.toFixed(3));

        /* EL ENLACE INVISIBLE. Una escena apagada sigue estando en la pagina:
           con solo opacity:0 su boton se puede pulsar igual. Durante la mayor
           parte del ciclo habia un enlace al catalogo, invisible, encima del
           centro de la seccion: tocar ahi te sacaba de la portada sin haber
           visto ningun boton. Se apaga con la escena. */
        var viva = o > 0.5;
        e.style.pointerEvents = viva ? 'auto' : 'none';
        e.setAttribute('aria-hidden', viva ? 'false' : 'true');
        if ('inert' in e) e.inert = !viva;
      }
    }

    /* Un fotograma entero: el fondo y las escenas, mas la cifra que sube.
       Va junto en una sola funcion para que no exista la posibilidad de
       pintar el fondo y olvidarse del contador. */
    function pintarTodo(t) { pintar(t); pintarCifra(t); }

    function bucle(ahora) {
      raf = 0;
      if (!aLaVista || document.hidden) return;
      if (t0 === null) t0 = ahora;
      if (ahora - ultimo < MS) { pedir(); return; }
      ultimo = ahora;
      tocando *= 0.95;
      pintarTodo(((ahora - t0) / 1000) % DUR);
      pedir();
    }
    function pedir() { if (!raf && aLaVista && !document.hidden) raf = requestAnimationFrame(bucle); }

    /* SE ARRANCA EN CUANTO SE VE, sin retrasos. Hubo aqui un setTimeout de
       350 ms "para dejar pintar la portada primero". No servia de nada, y la
       medicion lo demostro: el elemento que marca el LCP es el LEMA, que es
       el texto mas grande de la pagina y esta DENTRO de esta seccion. Con el
       lema en primer lugar, cuanto antes pinte, mejor: retrasarlo era
       empeorar justo el numero que se queria arreglar. */
    function arrancarConCalma() { pedir(); }
    function parar() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }

    /* ---------- la marca, letra a letra ----------
       El documento lleva el texto entero y limpio, que es lo que leen el
       buscador, el traductor de Shopify y un lector de pantalla. Las letras
       sueltas las fabrica el motor DESPUES, en una copia marcada como
       decorativa. Si el guion no llega a ejecutarse, lo que queda es el
       texto de siempre y no se pierde nada. */
    function partirMarca() {
      var p = raiz.querySelector('.secuencia-marca');
      if (!p || p.dataset.partida === '1') return;
      var txt = (p.textContent || '').trim();
      if (!txt || txt.length > 40) return;
      p.dataset.partida = '1';

      var oculto = document.createElement('span');
      oculto.className = 'visually-hidden';
      oculto.textContent = txt;

      var caja = document.createElement('span');
      caja.className = 'secuencia-marca-letras';
      caja.setAttribute('aria-hidden', 'true');
      var mitad = (txt.length - 1) / 2;
      for (var i = 0; i < txt.length; i++) {
        var s = document.createElement('span');
        s.className = 'secuencia-letra';
        s.textContent = txt.charAt(i) === ' ' ? ' ' : txt.charAt(i);
        /* d: a que distancia del centro esta la letra, de 0 a 1. La palabra
           se compone desde el centro hacia fuera, que es como se lee un
           logotipo, y no de izquierda a derecha, que es como se teclea. */
        s.style.setProperty('--d', (Math.abs(i - mitad) / (mitad || 1)).toFixed(3));
        s.style.setProperty('--s', (i < mitad ? -1 : 1).toString());
        caja.appendChild(s);
      }
      p.textContent = '';
      p.appendChild(oculto);
      p.appendChild(caja);
    }

    /* ---------- la cifra, como un cuentakilometros ----------
       El numero sale del catalogo de verdad (lo pone Liquid). Aqui solo se
       le anima la subida: de cero a su valor mientras dura su escena. */
    var cifraEl = raiz.querySelector('.secuencia-cifra');
    var cifraFin = 0;
    if (cifraEl) {
      cifraFin = parseInt((cifraEl.textContent || '').replace(/\D+/g, ''), 10);
      if (!isFinite(cifraFin)) { cifraEl = null; }
      else {
        cifraEl.setAttribute('data-sec-cifra', String(cifraFin));
        /* Se reserva el ancho del numero final para que al contar no se mueva
           nada a su alrededor. */
        cifraEl.style.setProperty('--sec-digitos', String(String(cifraFin).length));
      }
    }
    function pintarCifra(t) {
      if (!cifraEl) return;
      var i = -1, k;
      for (k = 0; k < escenas.length; k++)
        if (escenas[k].contains(cifraEl)) { i = k; break; }
      if (i < 0) return;
      var tr = tramos[i];
      var p = lim((t - tr.de) / (tr.dura * 0.62), 0, 1);
      cifraEl.textContent = String(Math.round(salida(p) * cifraFin));
    }

    /* ---------- interaccion ---------- */
    function mover(ev) {
      var r = raiz.getBoundingClientRect();
      if (!r.width) return;
      punteroX = lim((ev.clientX - r.left) / r.width, 0, 1);
      punteroY = lim((ev.clientY - r.top) / r.height, 0, 1);
    }
    raiz.addEventListener('pointermove', mover);
    raiz.addEventListener('pointerdown', function (ev) { mover(ev); tocando = 1; });
    raiz.addEventListener('pointerleave', function () { punteroX = 0.5; punteroY = 0.5; });

    /* ---------- arranque ---------- */
    partirMarca();
    medir();
    sembrarMotas();
    repartir();

    if (reduce) {
      /* El fotograma del cierre: el que lleva la marca y el boton. */
      var ult = tramos[tramos.length - 1];
      pintarTodo(ult.de + ult.dura * 0.55);
      raiz.classList.add('is-live', 'sin-movimiento');
      return;
    }

    var io = null;
    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (e) {
        aLaVista = e[0].isIntersecting;
        raiz.classList.toggle('is-live', aLaVista);
        if (aLaVista) { medir(); arrancarConCalma(); } else { parar(); }
      }, { threshold: 0.15 });
      io.observe(raiz);
    } else {
      aLaVista = true; raiz.classList.add('is-live'); arrancarConCalma();
    }

    var onVis = function () { document.hidden ? parar() : pedir(); };
    var onSize = function () { medir(); sembrarMotas(); pedir(); };
    document.addEventListener('visibilitychange', onVis);
    window.addEventListener('resize', onSize);

    vivos.push({
      raiz: raiz,
      soltar: function () {
        parar();
        if (io) io.disconnect();
        document.removeEventListener('visibilitychange', onVis);
        window.removeEventListener('resize', onSize);
        var i = vivos.indexOf(this);
        if (i > -1) vivos.splice(i, 1);
      }
    });
  }

  function arrancar(ambito) {
    var n = (ambito || document).querySelectorAll('[data-secuencia]');
    for (var i = 0; i < n.length; i++) montar(n[i]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { arrancar(); });
  } else { arrancar(); }

  document.addEventListener('shopify:section:load', function (e) {
    for (var i = vivos.length - 1; i >= 0; i--)
      if (!document.documentElement.contains(vivos[i].raiz)) vivos[i].soltar();
    arrancar(e.target);
  });
  document.addEventListener('shopify:section:unload', function (e) {
    for (var i = vivos.length - 1; i >= 0; i--)
      if (e.target.contains(vivos[i].raiz)) vivos[i].soltar();
  });
})();
