/* Haces holograficos.

   Adaptacion a JavaScript plano del componente React "beams-background":
   pilares de luz que suben desde el suelo, con las tres componentes de color
   separadas para imitar la aberracion cromatica de una proyeccion, mas
   lineas de barrido y vinetado.

   No hay React aqui, ni hace falta: el original solo usaba useRef y useEffect
   para agarrar el lienzo y montar el bucle. Lo demas es canvas 2D.

   Lo que se ha anadido respecto al original, porque una tienda no es una demo:
   - Se para cuando la seccion no se ve y cuando la pestana pasa a segundo
     plano. El original pintaba siempre, incluso en una pestana oculta.
   - Respeta movimiento reducido (pinta un fotograma y se queda quieto) y
     ahorro de datos (no arranca).
   - Limita la resolucion a 1x y a 2 megapixeles: el original usaba
     offsetWidth crudo, y en un movil de pantalla grande eso es dibujar
     decenas de gradientes por fotograma sobre un lienzo enorme.
   - Se suelta al recargarse la seccion en el editor, como el hero.
*/
(function () {
  'use strict';

  var vivos = [];

  function init(lienzo) {
    if (!lienzo || lienzo.getAttribute('data-vinit-haces')) return;
    lienzo.setAttribute('data-vinit-haces', '1');

    if (navigator.connection && navigator.connection.saveData) return;
    var ctx = null;
    try { ctx = lienzo.getContext('2d'); } catch (e) { return; }
    if (!ctx) return;

    var caja = lienzo.parentNode;
    var d = lienzo.dataset;
    var densidad = Math.max(4, parseInt(d.densidad, 10) || 30);
    var velocidad = parseFloat(d.velocidad) || 1;
    var aberracion = parseFloat(d.aberracion); if (isNaN(aberracion)) aberracion = 2.5;
    var fuerza = (parseFloat(d.opacidad) || 50) / 100;
    var cRojo = d.rojo || '255,0,0';
    var cAzul = d.azul || '0,50,255';
    var cNucleo = d.nucleo || '200,255,255';

    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var ancho = 0, alto = 0, t = 0, raf = 0, visible = true, enPantalla = true, muerto = false;
    var offs = [];
    function on(o, ev, fn, op) { o.addEventListener(ev, fn, op); offs.push(function () { o.removeEventListener(ev, fn, op); }); }

    // Ruido barato por superposicion de senos: da una silueta organica sin
    // cargar ninguna libreria.
    function ruido(x, tt) {
      return (Math.sin(x * 0.01 + tt) + Math.sin(x * 0.03 + tt * 2) * 0.5 + Math.sin(x * 0.1 + tt * 4) * 0.25) / 1.75;
    }

    function medir() {
      // 1x y no 1.5x: el lienzo lleva filter:blur(4px) encima, asi que los
      // pixeles de mas se destruyen antes de que nadie los vea.
      //
      // En un equipo flojo se baja a 0.65x. Medido en un movil de 390 px con
      // la CPU frenada 4x (gama baja o bateria al minimo): a 1x los haces
      // dejaban la pagina en 17 fps, a 0.65x vuelve a 60. La diferencia de
      // imagen es de 3 sobre 255 de media, invisible en un fondo oscuro y
      // desenfocado, pero como no es exactamente cero solo se aplica donde
      // hace falta: los equipos capaces se quedan con la calidad completa.
      var tope = 1;
      try {
        if ((navigator.hardwareConcurrency || 8) <= 4 ||
            (navigator.connection && navigator.connection.saveData)) tope = 0.65;
      } catch (eT) {}
      var dpr = Math.min(window.devicePixelRatio || 1, tope);
      var w = Math.max(1, Math.round(caja.offsetWidth * dpr));
      var h = Math.max(1, Math.round(caja.offsetHeight * dpr));
      var k = Math.min(1, Math.sqrt(2000000 / Math.max(1, w * h)));
      w = Math.max(1, Math.round(w * k)); h = Math.max(1, Math.round(h * k));
      if (lienzo.width !== w || lienzo.height !== h) { lienzo.width = w; lienzo.height = h; }
      ancho = w; alto = h;
    }

    function haz(x, tt, color, mod) {
      var n = ruido(x, tt * 0.5);
      // 0.85 + ruido: los pilares llegan casi arriba del todo. Con el 0.6
      // del original se quedaban en el tercio inferior y, con el vineteado
      // encima, apenas se veian.
      var altoHaz = alto * (0.85 + n * 0.35);
      var anchoHaz = (ancho / densidad) * mod;
      var g = ctx.createLinearGradient(x, alto, x, alto - altoHaz);
      g.addColorStop(0, color);
      g.addColorStop(1, 'transparent');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.moveTo(x - anchoHaz / 2, alto);
      ctx.lineTo(x + anchoHaz / 2, alto);
      ctx.lineTo(x + anchoHaz, alto - altoHaz);
      ctx.lineTo(x - anchoHaz, alto - altoHaz);
      ctx.fill();
    }

    // 30 fotogramas por segundo. Esto es una luz de fondo que se desplaza
    // despacio: a 60 se ve exactamente igual y cuesta el doble. Medido en un
    // movil con la CPU frenada, la diferencia es de mas de 100 ms por
    // fotograma, que es hilo principal robado al desplazamiento y a los
    // botones. En equipos con pocos nucleos o con ahorro de datos, 20.
    var MS_POR_FOTOGRAMA = 1000 / 30;
    try {
      if ((navigator.hardwareConcurrency || 8) <= 4 ||
          (navigator.connection && navigator.connection.saveData)) MS_POR_FOTOGRAMA = 1000 / 20;
    } catch (e) {}
    // Muy negativo a proposito: el limitador NO debe aplicarse al primer
    // fotograma. Con 0, si el script arranca antes de 33 ms el primer dibujo
    // se descartaba, y con movimiento reducido nadie lo reprogramaba nunca:
    // el lienzo se quedaba vacio para siempre. Se vio en la prueba de
    // navegador con reducedMotion, no en la revision del codigo.
    var ultimo = -1e9;

    function pintar(ahora) {
      raf = 0;
      if (muerto || !visible || !enPantalla) return;
      if (ahora === undefined) ahora = performance.now();
      if (ahora - ultimo < MS_POR_FOTOGRAMA) { if (!reduce) pedir(); return; }
      // Se guarda el instante ideal, no el real: asi un fotograma que llega
      // tarde no arrastra el ritmo de todos los siguientes.
      ultimo = ahora - ((ahora - ultimo) % MS_POR_FOTOGRAMA);
      ctx.clearRect(0, 0, ancho, alto);
      // "screen" y no "lighter": suma luz sin quemar la imagen a blanco.
      ctx.globalCompositeOperation = 'screen';
      if (!reduce) t += 0.01 * velocidad * (MS_POR_FOTOGRAMA / 16.67);
      var paso = ancho / densidad;
      for (var i = 0; i <= densidad; i++) {
        var x = i * paso;
        var aR = fuerza * (0.5 + 0.5 * Math.cos(i * 0.5 + t));
        haz(x - aberracion, t + i * 0.1, 'rgba(' + cRojo + ',' + (aR * 0.5).toFixed(3) + ')', 1.5);
        var aA = fuerza * (0.5 + 0.5 * Math.sin(i * 0.6 + t * 1.1));
        haz(x + aberracion, t + i * 0.12 + 10, 'rgba(' + cAzul + ',' + (aA * 0.5).toFixed(3) + ')', 1.5);
        var aN = fuerza * (0.6 + 0.4 * Math.sin(i * 0.3 - t));
        haz(x, t + i * 0.1 + 5, 'rgba(' + cNucleo + ',' + (aN * 0.3).toFixed(3) + ')', 0.8);
      }
      if (!reduce) pedir();
    }
    function pedir() { if (!muerto && visible && enPantalla && !raf) raf = requestAnimationFrame(pintar); }
    function parar() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }

    on(window, 'resize', function () { medir(); pedir(); });
    on(document, 'visibilitychange', function () {
      visible = document.visibilityState === 'visible';
      visible ? pedir() : parar();
    });

    var io = null, ro = null;
    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (en) {
        enPantalla = en[0] ? en[0].isIntersecting : true;
        enPantalla ? pedir() : parar();
      }, { threshold: 0 });
      io.observe(lienzo);
    }
    if ('ResizeObserver' in window) {
      ro = new ResizeObserver(function () { medir(); pedir(); });
      ro.observe(caja);
    }

    function soltar() {
      if (muerto) return;
      muerto = true;
      parar();
      for (var i = 0; i < offs.length; i++) offs[i]();
      offs = [];
      if (io) { io.disconnect(); io = null; }
      if (ro) { ro.disconnect(); ro = null; }
      var at = vivos.indexOf(entrada);
      if (at !== -1) vivos.splice(at, 1);
    }
    var entrada = { lienzo: lienzo, soltar: soltar };
    vivos.push(entrada);

    lienzo.classList.add('is-live');
    medir(); pintar();
  }

  function arrancar() {
    for (var j = vivos.length - 1; j >= 0; j--) {
      if (!document.contains(vivos[j].lienzo)) vivos[j].soltar();
    }
    var lista = document.querySelectorAll('[data-haces]');
    for (var i = 0; i < lista.length; i++) init(lista[i]);
  }
  arrancar();
  document.addEventListener('shopify:section:load', arrancar);
  document.addEventListener('shopify:section:unload', arrancar);
})();
