/* ===========================================================================
   BANNER VI.P — el 3D y las cifras
   ---------------------------------------------------------------------------
   Tres comportamientos, y ninguno es imprescindible: si este archivo no
   llegara a cargarse, el banner se ve entero y funciona igual. Todo lo que
   hay aqui adorna.

   1. ENTRADA ESCALONADA. Las piezas llegan inclinadas hacia atras y se
      enderezan, de arriba abajo. Se dispara al ENTRAR EN PANTALLA, con un
      IntersectionObserver, y hay red de seguridad: si el navegador no lo
      trae, o si a los dos segundos no se ha disparado, se muestra todo. El
      contenido no puede quedarse escondido esperando a un efecto.

   2. INCLINACION AL PUNTERO. La tarjeta bajo el raton gira hacia el, y el
      icono y el texto flotan por delante en planos distintos. Se calcula con
      la posicion del raton dentro de la tarjeta y se escribe en dos variables
      de CSS, asi que el movimiento lo hace la hoja de estilos y este archivo
      solo pasa dos numeros. Solo con puntero fino: en tactil el dedo tapa
      justo lo que se inclina, y el hover se queda pegado despues de tocar.

   3. LAS CIFRAS SUBEN CONTANDO. El numero final ya esta en el HTML, asi que
      se lee igual sin JavaScript.

   Con "menos movimiento" del sistema activado no se hace nada de esto.
   =========================================================================== */
(function () {
  'use strict';

  var quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* requestAnimationFrame no existe en todos los motores viejos, y este
     archivo lo usa en dos sitios: la inclinacion al puntero y la cuenta de
     las cifras. Sin esta red, en un navegador antiguo el banner se veria bien
     -- todo lo de aqui adorna -- pero saltaria un error en consola en cuanto
     alguien pasara el raton por una tarjeta. Se resuelve una vez, aqui. */
  var pideFotograma = window.requestAnimationFrame
    ? window.requestAnimationFrame.bind(window)
    : function (fn) { return setTimeout(function () { fn(Date.now()); }, 16); };
  var cancelaFotograma = window.cancelAnimationFrame
    ? window.cancelAnimationFrame.bind(window)
    : clearTimeout;

  function arrancar(banner) {
    if (banner.dataset.vipListo) return;
    banner.dataset.vipListo = '1';

    /* ---------- 1. entrada ---------- */
    var piezas = [];
    var main = banner.querySelector('.vip-main');
    if (main) {
      ['.vip-badge', '.vip-title', '.vip-subtitle', '.vip-text', '.vip-ctas', '.vip-stats']
        .forEach(function (s) { var e = main.querySelector(s); if (e) piezas.push(e); });
    }
    var tarjetas = banner.querySelectorAll('.vip-tool');
    for (var i = 0; i < tarjetas.length; i++) piezas.push(tarjetas[i]);

    function mostrar() {
      piezas.forEach(function (e, k) {
        e.style.transitionDelay = Math.min(k * 55, 620) + 'ms';
        e.classList.add('vip-puesto');
      });
      contar();
    }

    if (quieto || !('IntersectionObserver' in window)) {
      piezas.forEach(function (e) { e.classList.remove('vip-ent'); });
      contar();
    } else {
      piezas.forEach(function (e) { e.classList.add('vip-ent'); });
      var io = new IntersectionObserver(function (ent) {
        for (var j = 0; j < ent.length; j++) {
          if (ent[j].isIntersecting) { io.disconnect(); mostrar(); return; }
        }
      }, { rootMargin: '0px 0px -12% 0px' });
      io.observe(banner);
      // Red de seguridad: nada puede quedarse invisible por un efecto.
      setTimeout(function () { io.disconnect(); mostrar(); }, 2200);
    }

    /* ---------- 2. inclinacion al puntero ---------- */
    var fino = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (fino && !quieto) {
      for (var t = 0; t < tarjetas.length; t++) inclinar(tarjetas[t]);
    }

    /* ---------- 3. las cifras ---------- */
    var contado = false;
    function contar() {
      if (contado || quieto) return;
      contado = true;
      var cifras = banner.querySelectorAll('.vip-stat strong');
      var metas = [], vale = false;
      for (var k = 0; k < cifras.length; k++) {
        var txt = (cifras[k].textContent || '').trim();
        var n = parseInt(txt.replace(/[^0-9]/g, ''), 10);
        // Solo se anima lo que es un numero limpio: si alguien escribe "24/7"
        // o "+100" en el editor, esa cifra se queda como esta.
        metas.push(/^[0-9]+$/.test(txt) && !isNaN(n) ? n : null);
        if (metas[k] !== null) vale = true;
      }
      if (!vale) return;
      for (var m = 0; m < cifras.length; m++) if (metas[m] !== null) cifras[m].textContent = '0';
      var DUR = 1000, t0 = null;
      function paso(ahora) {
        if (t0 === null) t0 = ahora;
        var u = Math.min(1, (ahora - t0) / DUR);
        var e = 1 - Math.pow(1 - u, 3);
        for (var q = 0; q < cifras.length; q++) {
          if (metas[q] !== null) cifras[q].textContent = Math.round(metas[q] * e);
        }
        if (u < 1) pideFotograma(paso);
      }
      pideFotograma(paso);
    }
  }

  function inclinar(el) {
    var raf = 0, ultimo = null;
    el.addEventListener('pointermove', function (ev) {
      ultimo = ev;
      if (raf) return;
      raf = pideFotograma(function () {
        raf = 0;
        var r = el.getBoundingClientRect();
        var x = (ultimo.clientX - r.left) / r.width - 0.5;
        var y = (ultimo.clientY - r.top) / r.height - 0.5;
        el.style.setProperty('--ry', (x * 13).toFixed(2) + 'deg');
        el.style.setProperty('--rx', (-y * 11).toFixed(2) + 'deg');
      });
    });
    el.addEventListener('pointerleave', function () {
      if (raf) { cancelaFotograma(raf); raf = 0; }
      el.style.setProperty('--ry', '0deg');
      el.style.setProperty('--rx', '0deg');
    });
  }

  function init() {
    var b = document.querySelectorAll('.vip-banner');
    for (var i = 0; i < b.length; i++) arrancar(b[i]);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  // El editor de Shopify vuelve a montar la seccion al tocar un ajuste.
  document.addEventListener('shopify:section:load', init);
})();
