/* Villumination - Secuencia de marca animada e interactiva.
   ------------------------------------------------------------------
   Es la version en vivo del video de estudio/video/. Frente a un archivo de
   video tiene tres ventajas que importan en una tienda:
     - El texto es texto de verdad: Google lo indexa, un lector de pantalla
       lo lee y se traduce con el resto del tema. Un video no.
     - Pesa unos 9 KB en vez de varios megabytes, y no hay que esperar a que
       cargue ni se ve pixelada en una pantalla de alta densidad.
     - Reacciona al visitante: los haces se inclinan hacia el dedo o el raton
       y el pulso del marco se acelera al tocar.

   El fondo va en un lienzo; los textos son nodos del documento con opacidad
   animada desde el mismo reloj, para que imagen y letra vayan sincronizadas.

   Se para fuera de pantalla, con la pestana oculta y con movimiento
   reducido (en ese caso muestra el fotograma final, que es el que lleva la
   llamada a la accion: quien pide menos movimiento tambien tiene derecho a
   ver el boton).
*/
(function () {
  'use strict';

  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  var vivos = [];

  function lim(v, a, b) { return v < a ? a : (v > b ? b : v); }
  function suave(x) { x = lim(x, 0, 1); return x * x * (3 - 2 * x); }
  function salida(x) { x = lim(x, 0, 1); return 1 - Math.pow(1 - x, 3); }
  function ventana(t, de, a, entra, sale) {
    if (t < de || t > a) return 0;
    return Math.min(suave((t - de) / entra), suave((a - t) / sale));
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

    var DUR = parseFloat(raiz.dataset.secDuracion) || 14;
    var W = 0, H = 0, raf = 0, aLaVista = false, t0 = null, ultimo = -1e9;
    var punteroX = 0.5, punteroY = 0.5, tocando = 0;

    // 30 fps: es una animacion ambiental lenta, a 60 se ve igual y cuesta el
    // doble. En equipos flojos, 20 y lienzo reducido, igual que en los haces.
    var MS = 1000 / 30, tope = 1;
    try {
      if ((navigator.hardwareConcurrency || 8) <= 4 ||
          (navigator.connection && navigator.connection.saveData)) { MS = 1000 / 20; tope = 0.7; }
    } catch (e3) {}

    function medir() {
      var dpr = Math.min(window.devicePixelRatio || 1, tope);
      var w = Math.max(1, Math.round(raiz.offsetWidth * dpr));
      var h = Math.max(1, Math.round(raiz.offsetHeight * dpr));
      if (w === W && h === H) return;
      lienzo.width = W = w; lienzo.height = H = h;
    }

    /* ---------- fondo ---------- */
    function fondo(t) {
      ctx.fillStyle = raiz.dataset.secFondo || '#05060a';
      ctx.fillRect(0, 0, W, H);

      // Haces. Se inclinan hacia el puntero: es la parte interactiva, y es
      // sutil a proposito, para que acompane sin distraer de la compra.
      var sesgo = (punteroX - 0.5) * 1.5;   // desplazamiento lateral, en anchos de haz
      ctx.globalCompositeOperation = 'screen';
      var n = 9;
      for (var i = 0; i <= n; i++) {
        var x = (i / n) * W;
        var fase = t * 0.9 + i * 0.7;
        var alto = H * (0.72 + 0.28 * Math.sin(fase));
        var an = W * 0.05;
        var a = (0.20 + 0.16 * Math.sin(fase * 1.3 + 1.0)) * (1 + tocando * 0.5);
        var c = ['rgba(0,240,255,', 'rgba(139,92,246,', 'rgba(255,46,203,'][i % 3];
        var g = ctx.createLinearGradient(x, H, x + an * sesgo, H - alto);
        g.addColorStop(0, c + a.toFixed(3) + ')');
        g.addColorStop(1, c + '0)');
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.moveTo(x - an * 0.5, H);
        ctx.lineTo(x + an * 0.5, H);
        ctx.lineTo(x + an * 1.6 + an * sesgo, H - alto);
        ctx.lineTo(x - an * 1.6 + an * sesgo, H - alto);
        ctx.fill();
      }
      ctx.globalCompositeOperation = 'source-over';

      // Marco: se dibuja al principio y luego lleva un pulso, el mismo
      // motivo que el hero de la portada.
      var m = Math.min(W, H) * 0.075;
      var x0 = m, y0 = m, x1 = W - m, y1 = H - m;
      var per = 2 * ((x1 - x0) + (y1 - y0));
      var hecho = t < 1.8 ? salida(t / 1.8) : 1;
      ctx.save();
      ctx.lineWidth = Math.max(2, Math.min(W, H) * 0.006);
      ctx.lineJoin = 'round';
      ctx.strokeStyle = 'rgba(0,240,255,0.42)';
      ctx.setLineDash([per * hecho, per]);
      ctx.beginPath();
      ctx.moveTo(x0, y0); ctx.lineTo(x1, y0); ctx.lineTo(x1, y1); ctx.lineTo(x0, y1); ctx.closePath();
      ctx.stroke();
      if (hecho > 0.98) {
        ctx.strokeStyle = 'rgba(190,250,255,0.92)';
        ctx.shadowColor = 'rgba(0,240,255,0.85)';
        ctx.shadowBlur = Math.min(W, H) * 0.03;
        ctx.setLineDash([per * 0.13, per]);
        ctx.lineDashOffset = -(((t - 1.8) * per * (0.20 + tocando * 0.25)) % per);
        ctx.beginPath();
        ctx.moveTo(x0, y0); ctx.lineTo(x1, y0); ctx.lineTo(x1, y1); ctx.lineTo(x0, y1); ctx.closePath();
        ctx.stroke();
      }
      ctx.restore();
    }

    /* ---------- un fotograma ---------- */
    // Reparto del tiempo entre las escenas que existan de verdad: la seccion
    // permite quitar bloques, y con un reparto fijo las escenas sobrantes
    // dejarian huecos en negro.
    function pintar(t) {
      fondo(t);
      var k = escenas.length;
      var trozo = DUR / k;
      for (var i = 0; i < k; i++) {
        var de = i * trozo;
        var o = ventana(t, de, de + trozo * 1.12, trozo * 0.30, trozo * 0.30);
        var e = escenas[i];
        e.style.opacity = o;
        // Un desplazamiento corto hacia arriba al entrar: el ojo lo lee como
        // "esto acaba de llegar" sin que haga falta ningun texto extra.
        var sub = (1 - salida((t - de) / (trozo * 0.45))) * 14;
        e.style.transform = 'translate3d(0,' + sub.toFixed(1) + 'px,0)';
        e.setAttribute('aria-hidden', o < 0.15 ? 'true' : 'false');
      }
    }

    function bucle(ahora) {
      raf = 0;
      if (!aLaVista || document.hidden) return;
      if (t0 === null) t0 = ahora;
      if (ahora - ultimo < MS) { pedir(); return; }
      ultimo = ahora;
      tocando *= 0.94;
      pintar(((ahora - t0) / 1000) % DUR);
      pedir();
    }
    function pedir() { if (!raf && aLaVista && !document.hidden) raf = requestAnimationFrame(bucle); }
    function parar() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }

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
    medir();
    if (reduce) {
      // Fotograma final: es el que lleva el logo y la llamada a la accion.
      pintar(DUR * (escenas.length - 0.35) / escenas.length);
      raiz.classList.add('is-live');
      return;
    }

    var io = null;
    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (e) {
        aLaVista = e[0].isIntersecting;
        raiz.classList.toggle('is-live', aLaVista);
        if (aLaVista) { medir(); pedir(); } else { parar(); }
      }, { threshold: 0.15 });
      io.observe(raiz);
    } else {
      aLaVista = true; raiz.classList.add('is-live'); pedir();
    }

    var onVis = function () { document.hidden ? parar() : pedir(); };
    var onSize = function () { medir(); pedir(); };
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
