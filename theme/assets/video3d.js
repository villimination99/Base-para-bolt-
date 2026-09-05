/* Villumination - Escenario de video 3D interactivo
   ------------------------------------------------------------------
   Toma el marco del video y lo inclina siguiendo al puntero, con las
   capas del fondo moviendose menos que el video (parallax de verdad,
   no un unico bloque girando). En tactil no hay puntero que seguir, asi
   que el marco reacciona al arrastre y vuelve al centro al soltar.

   Reglas que respeta:
   - Nada se mueve si el visitante pidio menos movimiento.
   - El <video> alojado en Shopify solo se reproduce cuando esta a la
     vista; fuera de pantalla se pausa (no gasta bateria ni datos).
   - El iframe de YouTube/Vimeo NO se inserta hasta que se pulsa play:
     asi la portada no carga scripts de terceros ni cookies de entrada.
   - Un solo requestAnimationFrame por escenario y ningun trabajo entre
     fotogramas: el puntero solo apunta valores, el rAF los aplica.
*/
(function () {
  'use strict';

  function on(el, ev, fn) { el.addEventListener(ev, fn, false); }

  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

  var vivos = [];

  function limitar(v, min, max) { return v < min ? min : (v > max ? max : v); }

  function montar(root) {
    if (!root || root.dataset.v3dListo === '1') return;
    root.dataset.v3dListo = '1';

    var marco = root.querySelector('[data-v3d-marco]');
    var video = root.querySelector('video');
    var portada = root.querySelector('[data-v3d-portada]');
    var hueco = root.querySelector('[data-v3d-hueco]');
    var incrustar = root.dataset.v3dEmbed || '';
    var maxGiro = parseFloat(root.dataset.v3dGiro || '10') || 0;

    /* ---------- 1. Inclinacion ---------- */
    var raf = 0, objX = 0, objY = 0, curX = 0, curY = 0, activo = false;

    function pintar() {
      raf = 0;
      curX += (objX - curX) * 0.12;
      curY += (objY - curY) * 0.12;
      root.style.setProperty('--v3d-rx', curX.toFixed(3) + 'deg');
      root.style.setProperty('--v3d-ry', curY.toFixed(3) + 'deg');
      // Las luces se desplazan al reves que el marco: da sensacion de profundidad
      root.style.setProperty('--v3d-px', (curY * -1.6).toFixed(2) + 'px');
      root.style.setProperty('--v3d-py', (curX * 1.6).toFixed(2) + 'px');
      if (Math.abs(objX - curX) > 0.01 || Math.abs(objY - curY) > 0.01) pedir();
    }
    function pedir() { if (!raf) raf = requestAnimationFrame(pintar); }

    if (marco && maxGiro > 0 && !reduce) {
      var finoPuntero = true;
      try { finoPuntero = window.matchMedia('(hover: hover) and (pointer: fine)').matches; } catch (e2) {}

      if (finoPuntero) {
        root.addEventListener('pointermove', function (ev) {
          var r = root.getBoundingClientRect();
          if (!r.width || !r.height) return;
          var px = (ev.clientX - r.left) / r.width - 0.5;
          var py = (ev.clientY - r.top) / r.height - 0.5;
          objY = limitar(px * maxGiro * 2, -maxGiro, maxGiro);
          objX = limitar(-py * maxGiro * 1.2, -maxGiro, maxGiro);
          if (!activo) { activo = true; root.classList.add('is-tilt'); }
          pedir();
        });
        root.addEventListener('pointerleave', function () {
          objX = 0; objY = 0; activo = false;
          root.classList.remove('is-tilt');
          pedir();
        });
      } else {
        // Tactil: arrastrar gira, soltar recentra. touch-action pan-y para no
        // secuestrar el scroll vertical de la pagina.
        var arrastra = false, ux = 0, uy = 0;
        root.style.touchAction = 'pan-y';
        root.addEventListener('pointerdown', function (ev) {
          if (ev.pointerType === 'mouse') return;
          arrastra = true; ux = ev.clientX; uy = ev.clientY;
          root.classList.add('is-tilt');
        });
        root.addEventListener('pointermove', function (ev) {
          if (!arrastra) return;
          objY = limitar(objY + (ev.clientX - ux) * 0.35, -maxGiro, maxGiro);
          objX = limitar(objX - (ev.clientY - uy) * 0.22, -maxGiro, maxGiro);
          ux = ev.clientX; uy = ev.clientY;
          pedir();
        });
        var soltar = function () {
          if (!arrastra) return;
          arrastra = false; objX = 0; objY = 0;
          root.classList.remove('is-tilt');
          pedir();
        };
        root.addEventListener('pointerup', soltar);
        root.addEventListener('pointercancel', soltar);
      }
    }

    /* ---------- 2. Portada: cadena de respaldos ----------
       YouTube no genera todas las miniaturas para todos los videos.
       oardefault (proporcion original, la buena para un Short vertical) y
       maxresdefault (1280 px) faltan a menudo; hqdefault existe siempre pero
       es 480x360 y en un marco vertical sale recortada y borrosa. Se pide la
       mejor primero y se va bajando. Cuando YouTube no tiene la miniatura
       devuelve una imagen gris de 120x90, no un error, asi que tambien hay
       que descartarla por tamano. */
    if (portada) {
      var respaldos = [];
      if (portada.dataset.v3dAlt1) respaldos.push(portada.dataset.v3dAlt1);
      if (portada.dataset.v3dAlt2) respaldos.push(portada.dataset.v3dAlt2);
      var siguiente = function () {
        var url = respaldos.shift();
        if (url) portada.src = url;
      };
      on(portada, 'error', siguiente);
      on(portada, 'load', function () {
        // 120x90 es la imagen de relleno que devuelve YouTube cuando la
        // miniatura pedida no existe. Vale como "no la tengo".
        if (portada.naturalWidth <= 120 && portada.naturalHeight <= 90) siguiente();
      });
    }

    /* ---------- 3. Reproduccion ---------- */
    var boton = root.querySelector('[data-v3d-play]');

    function abrirIncrustado() {
      if (!hueco || !incrustar) return;
      if (hueco.dataset.puesto === '1') return;
      hueco.dataset.puesto = '1';
      var f = document.createElement('iframe');
      f.src = incrustar + (incrustar.indexOf('?') > -1 ? '&' : '?') + 'autoplay=1&rel=0&playsinline=1';
      f.title = root.dataset.v3dTitulo || 'Video';
      f.loading = 'lazy';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.setAttribute('allowfullscreen', '');
      f.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      hueco.appendChild(f);
      root.classList.add('is-playing');
      if (portada) portada.hidden = true;
    }

    if (boton) {
      boton.addEventListener('click', function () {
        if (incrustar) { abrirIncrustado(); return; }
        if (!video) return;
        if (video.paused) {
          video.muted = false;
          var p = video.play();
          if (p && p.catch) p.catch(function () { video.muted = true; video.play(); });
          root.classList.add('is-playing');
          if (portada) portada.hidden = true;
        } else {
          video.pause();
          root.classList.remove('is-playing');
        }
      });
    }

    /* ---------- 4. Halo de color tomado del propio video ----------
       El fondo de la seccion recoge los colores que hay en pantalla en ese
       momento, asi el video deja de parecer un rectangulo pegado encima del
       negro y pasa a formar parte de la pagina. Se pinta en un lienzo
       diminuto (32x18) que el CSS agranda y desenfoca: a ese tamano el coste
       es despreciable y aun asi el color es el correcto.
       Solo con video alojado en Shopify (un iframe ajeno no se puede leer).
       Se apaga con movimiento reducido y con el ahorro de datos. */
    var io = null, aLaVista = false;
    var auto = root.dataset.v3dAuto === '1';
    var halo = root.querySelector('[data-v3d-halo]');
    var haloT = 0;
    var ahorro = false;
    try { ahorro = !!(navigator.connection && navigator.connection.saveData); } catch (e3) {}

    if (halo && video && !reduce && !ahorro) {
      var hctx = null;
      try { hctx = halo.getContext('2d', { alpha: false }); } catch (e4) {}
      if (hctx) {
        halo.width = 32; halo.height = 18;
        var pintarHalo = function () {
          if (!aLaVista || document.hidden || video.readyState < 2) return;
          try { hctx.drawImage(video, 0, 0, 32, 18); halo.classList.add('is-on'); } catch (e5) {}
        };
        var latir = function () {
          pintarHalo();
          haloT = setTimeout(latir, 160);
        };
        video.addEventListener('loadeddata', pintarHalo);
        latir();
      }
    }

    /* ---------- 5. Solo trabaja cuando se ve ---------- */
    function aplicar() {
      if (!video) return;
      if (aLaVista && !document.hidden) {
        if (auto && video.paused) {
          var p = video.play();
          if (p && p.catch) p.catch(function () {});
        }
      } else if (!video.paused) {
        video.pause();
      }
    }

    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (ents) {
        aLaVista = ents[0].isIntersecting;
        root.classList.toggle('is-live', aLaVista);
        aplicar();
      }, { threshold: 0.2 });
      io.observe(root);
    } else {
      aLaVista = true;
      root.classList.add('is-live');
      aplicar();
    }

    var onOculto = function () { aplicar(); };
    document.addEventListener('visibilitychange', onOculto);

    vivos.push({
      root: root,
      soltar: function () {
        if (haloT) clearTimeout(haloT);
        if (io) io.disconnect();
        document.removeEventListener('visibilitychange', onOculto);
        if (raf) cancelAnimationFrame(raf);
        var i = vivos.indexOf(this);
        if (i > -1) vivos.splice(i, 1);
      }
    });
  }

  function arrancar(ambito) {
    var nodos = (ambito || document).querySelectorAll('[data-video-3d]');
    for (var i = 0; i < nodos.length; i++) montar(nodos[i]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { arrancar(); });
  } else {
    arrancar();
  }

  // Editor de temas: al recargar una seccion el nodo viejo se tira entero.
  document.addEventListener('shopify:section:load', function (e) {
    for (var i = vivos.length - 1; i >= 0; i--) {
      if (!document.documentElement.contains(vivos[i].root)) vivos[i].soltar();
    }
    arrancar(e.target);
  });
  document.addEventListener('shopify:section:unload', function (e) {
    for (var i = vivos.length - 1; i >= 0; i--) {
      if (e.target.contains(vivos[i].root)) vivos[i].soltar();
    }
  });
})();
