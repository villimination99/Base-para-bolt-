/* Guion de la secuencia de marca de Villumination.
   ------------------------------------------------------------------
   TODO depende de una unica variable de tiempo que fija el renderizador
   (window.__t, en segundos). No hay requestAnimationFrame ni Date.now: si
   el tiempo lo pone quien captura, cada fotograma sale identico ejecucion
   tras ejecucion y el video es reproducible. Esa es la unica forma de
   grabar sin que el resultado dependa de lo rapido que vaya la maquina. */
(function () {
  'use strict';

  // 22 s: el video anterior tenia cinco escenas y se quedaba corto para
  // contar QUE se vende. Ahora hay ocho, con las cuatro familias reales del
  // catalogo, y el cierre sigue llevandose cuatro segundos largos porque es
  // el momento en que alguien decide entrar.
  var DURACION = 22;
  var C = document.getElementById('lienzo');
  var g = C.getContext('2d');

  /* ---------- utilidades ---------- */
  var lim = function (v, a, b) { return v < a ? a : (v > b ? b : v); };
  // Curva suave estandar: arranca y frena sin tirones.
  var suave = function (x) { x = lim(x, 0, 1); return x * x * (3 - 2 * x); };
  // Entrada con rebote corto, para los titulos
  var salida = function (x) { x = lim(x, 0, 1); return 1 - Math.pow(1 - x, 3); };
  // Ventana: 0 antes de "de", 1 dentro, 0 despues de "a"
  function ventana(t, de, a, entra, sale) {
    entra = entra || 0.45; sale = sale || 0.45;
    if (t < de || t > a) return 0;
    return Math.min(suave((t - de) / entra), suave((a - t) / sale));
  }

  /* ---------- fondo: haces + marco, la lengua visual de la tienda ---------- */
  function fondo(t, W, H) {
    g.fillStyle = '#05060a';
    g.fillRect(0, 0, W, H);

    // Haces verticales, el mismo lenguaje que la seccion "Haces de luz"
    g.globalCompositeOperation = 'screen';
    var n = 9;
    for (var i = 0; i <= n; i++) {
      var x = (i / n) * W;
      var fase = t * 0.9 + i * 0.7;
      var alto = H * (0.55 + 0.35 * Math.sin(fase));
      var ancho = W * 0.055;
      var a = 0.10 + 0.10 * Math.sin(fase * 1.3 + 1.0);
      var col = [
        'rgba(0,240,255,', 'rgba(139,92,246,', 'rgba(255,46,203,'
      ][i % 3];
      var grad = g.createLinearGradient(x, H, x, H - alto);
      grad.addColorStop(0, col + a.toFixed(3) + ')');
      grad.addColorStop(1, col + '0)');
      g.fillStyle = grad;
      g.beginPath();
      g.moveTo(x - ancho * 0.5, H);
      g.lineTo(x + ancho * 0.5, H);
      g.lineTo(x + ancho * 1.6, H - alto);
      g.lineTo(x - ancho * 1.6, H - alto);
      g.fill();
    }
    g.globalCompositeOperation = 'source-over';

    // Marco de neon que se dibuja al principio y respira despues.
    // Es el mismo motivo que el hero de la tienda: quien vea el video y
    // luego entre en la web reconoce la marca al instante.
    var m = W * 0.085;
    var x0 = m, y0 = m, x1 = W - m, y1 = H - m;
    var per = 2 * ((x1 - x0) + (y1 - y0));
    var dibujado = t < 2.0 ? salida(t / 2.0) : 1;

    g.save();
    g.lineWidth = Math.max(2, W * 0.005);
    g.lineJoin = 'round';
    g.strokeStyle = 'rgba(0,240,255,0.28)';
    g.setLineDash([per * dibujado, per]);
    g.lineDashOffset = 0;
    g.beginPath();
    g.moveTo(x0, y0); g.lineTo(x1, y0); g.lineTo(x1, y1); g.lineTo(x0, y1); g.closePath();
    g.stroke();

    // Pulso que recorre el carril, como en el hero
    if (dibujado > 0.98) {
      var largoPulso = per * 0.13;
      g.strokeStyle = 'rgba(190,250,255,0.95)';
      g.shadowColor = 'rgba(0,240,255,0.9)';
      g.shadowBlur = W * 0.035;
      g.setLineDash([largoPulso, per]);
      g.lineDashOffset = -(((t - 2.0) * per * 0.20) % per);
      g.beginPath();
      g.moveTo(x0, y0); g.lineTo(x1, y0); g.lineTo(x1, y1); g.lineTo(x0, y1); g.closePath();
      g.stroke();
    }
    g.restore();

    // Vineta. Los haces suben por el centro justo donde va el texto, y sin
    // esto las letras compiten con la luz. Oscurece los bordes y el centro
    // alto, que es donde cae la tipografia grande.
    var vin = g.createRadialGradient(W * 0.5, H * 0.46, Math.min(W, H) * 0.1,
                                     W * 0.5, H * 0.46, Math.max(W, H) * 0.72);
    vin.addColorStop(0, 'rgba(5,6,10,0.55)');
    vin.addColorStop(0.45, 'rgba(5,6,10,0.30)');
    vin.addColorStop(1, 'rgba(5,6,10,0.92)');
    g.fillStyle = vin;
    g.fillRect(0, 0, W, H);

    // Barrido horizontal, una sola pasada por escena
    var barr = (t * 0.34) % 1;
    var yB = barr * H;
    var gb = g.createLinearGradient(0, yB - H * 0.06, 0, yB + H * 0.06);
    gb.addColorStop(0, 'rgba(255,255,255,0)');
    gb.addColorStop(0.5, 'rgba(255,255,255,0.045)');
    gb.addColorStop(1, 'rgba(255,255,255,0)');
    g.fillStyle = gb;
    g.fillRect(0, yB - H * 0.06, W, H * 0.12);
  }

  /* ---------- contenido ---------- */
  // Las cuatro familias reales del catalogo, con los iconos del propio tema
  // para que el video y la tienda hablen el mismo idioma visual.
  var PILARES = [
    ['FUERZA', 'EQUIPO Y ACCESORIOS',
     '<path d="M14.4 14.4 9.6 9.6"/><path d="M18.657 21.485a2 2 0 1 1-2.829-2.828l-1.767 1.768a2 2 0 1 1-2.829-2.829l6.364-6.364a2 2 0 1 1 2.829 2.829l1.767-1.768a2 2 0 1 1 2.829 2.829z"/><path d="m21.5 21.5-1.4-1.4"/><path d="M3.9 3.9 2.5 2.5"/><path d="M6.404 12.768a2 2 0 1 1-2.829-2.829l1.768-1.767a2 2 0 1 1-2.829-2.829l2.829-2.829a2 2 0 1 1 2.829 2.829l1.767-1.768a2 2 0 1 1 2.829 2.829z"/>'],
    ['NUTRICIÓN', 'SUPLEMENTOS',
     '<path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/><path d="m8.5 8.5 7 7"/>'],
    ['RENDIMIENTO', 'ROPA DEPORTIVA',
     '<path d="M20.38 3.46 16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23Z"/>'],
    ['CONSTANCIA', 'PLANES Y CÓDICES',
     '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>']
  ];

  // Tres cifras reales de la tienda, verificadas por la API de Shopify.
  var CIFRAS = [
    ['37', 'PRODUCTOS EN CATÁLOGO'],
    ['5', 'IDIOMAS'],
    ['8', 'CÓDICES DIGITALES']
  ];

  var lema = document.getElementById('lema');
  lema.innerHTML = 'NO TE<br><em>CONFORMES</em>';

  function pilarHTML(p) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.7" ' +
      'stroke-linecap="round" stroke-linejoin="round">' + p[2] + '</svg>' +
      '<b>' + p[0] + '<i>' + p[1] + '</i></b>';
  }

  var cont = document.getElementById('pilares');
  var cont2 = document.getElementById('pilares2');
  PILARES.slice(2).forEach(function (p) {
    var d = document.createElement('div');
    d.className = 'pilar';
    d.innerHTML = pilarHTML(p);
    cont2.appendChild(d);
  });

  var contCifras = document.getElementById('cifras2');
  CIFRAS.slice(1).forEach(function (c) {
    var d = document.createElement('div');
    d.innerHTML = '<b>' + c[0] + '</b><span>' + c[1] + '</span>';
    contCifras.appendChild(d);
  });

  PILARES.slice(0, 2).forEach(function (p) {
    var d = document.createElement('div');
    d.className = 'pilar';
    d.innerHTML = pilarHTML(p);
    cont.appendChild(d);
  });

  var capas = {};
  ['c1', 'c2', 'c3', 'c3b', 'c4', 'c4b', 'c4c', 'c5'].forEach(function (id) {
    capas[id] = document.getElementById(id);
  });
  var cifraEl = document.getElementById('cifra');
  var marcaEl = document.querySelector('.marca');
  var anillo = document.getElementById('anilloTrazo');

  /* ---------- un fotograma ---------- */
  function pintar(t) {
    var W = C.width, H = C.height;
    fondo(t, W, H);

    // El guion, escrito una sola vez y aplicado en bucle: con ocho escenas,
    // repetir el bloque de opacidad y desplazamiento ocho veces era pedir un
    // descuadre. Cada entrada es [capa, entra, sale, margen de entrada,
    // margen de salida].
    var GUION = [
      ['c1',   0.5,  3.1, 0.70, 0.50],   // VILLUMINATION
      ['c2',   3.2,  6.0, 0.55, 0.45],   // NO TE CONFORMES
      ['c3',   6.1,  9.0, 0.50, 0.45],   // fuerza y nutricion
      ['c3b',  9.1, 12.0, 0.50, 0.45],   // rendimiento y constancia
      ['c4',  12.1, 14.8, 0.45, 0.45],   // 37 productos
      ['c4b', 14.9, 17.4, 0.45, 0.45],   // 5 idiomas y 8 codices
      ['c4c', 17.5, 19.6, 0.45, 0.45],   // frase de cierre
      ['c5',  19.7, 21.9, 0.60, 1.60]    // logo, dominio y llamada a la accion
    ];

    for (var g = 0; g < GUION.length; g++) {
      var e = GUION[g];
      var o = ventana(t, e[1], e[2], e[3], e[4]);
      capas[e[0]].style.opacity = o;
    }

    // Detalles que no son solo opacidad
    // El interletrado de la marca se cierra al entrar
    marcaEl.style.letterSpacing = (0.60 - 0.30 * salida((t - 0.5) / 1.6)).toFixed(3) + 'em';

    // El lema sube y crece un punto
    lema.style.transform = 'translateY(' + (1 - salida((t - 3.2) / 1.1)) * 4 + 'vw) scale(' +
      (0.94 + 0.06 * salida((t - 3.2) / 1.1)).toFixed(4) + ')';

    // Los pilares entran en cascada, cada tanda desde su propio arranque
    [[cont, 6.3], [cont2, 9.3]].forEach(function (par) {
      var items = par[0].children;
      for (var i = 0; i < items.length; i++) {
        var ent = salida((t - (par[1] + i * 0.45)) / 0.75);
        items[i].style.opacity = ent;
        items[i].style.transform = 'translateX(' + ((1 - ent) * -6).toFixed(2) + 'vw)';
      }
    });

    // La cifra grande cuenta hasta el numero real de productos
    cifraEl.textContent = Math.round(37 * salida((t - 12.2) / 1.3));

    // Las dos cifras pequenas entran una detras de otra
    var cs = contCifras.children;
    for (var k = 0; k < cs.length; k++) {
      cs[k].style.opacity = salida((t - (15.1 + k * 0.5)) / 0.7);
    }

    // El anillo del cierre gira despacio
    anillo.style.transformOrigin = '50% 50%';
    anillo.style.transform = 'rotate(' + (t * 26).toFixed(1) + 'deg)';
  }

  /* ---------- interfaz para el renderizador ---------- */
  function medir() {
    var dpr = window.devicePixelRatio || 1;
    C.width = Math.round(C.offsetWidth * dpr);
    C.height = Math.round(C.offsetHeight * dpr);
  }
  medir();
  window.addEventListener('resize', medir);

  window.__duracion = DURACION;
  window.__pintar = function (t) { pintar(t); };
  // Fotograma inicial para poder mirar la pagina sin renderizador
  window.__pintar(0);

  // Vista previa en vivo solo si nadie va a capturar (para revisar a ojo)
  if (!window.__capturando) {
    var inicio = null;
    (function bucle(now) {
      if (inicio === null) inicio = now;
      window.__pintar(((now - inicio) / 1000) % DURACION);
      requestAnimationFrame(bucle);
    })(performance.now());
  }
})();
