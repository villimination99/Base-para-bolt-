/* VILLUMINATION 3D — Fondo de shader "borde pulsante" para el hero.
   WebGL puro, sin dependencias ni framework.

   El shader GLSL es una adaptacion de Paper Shaders (Pulsing Border),
   https://shaders.paper.design/pulsing-border — licencia Apache-2.0.

   Se ha portado a JavaScript plano desde el componente React original: este
   tema es Liquid, no React. En el camino se han eliminado las ramas que el
   preset deja apagadas (desenfoque de 5 muestras, distorsion por cursor,
   mezcla OKLab, warp, deriva, rotacion, vineta) porque no cambian el resultado
   visual y si cuestan GPU en cada fotograma.

   Se ha anadido lo que no traia: u_scroll, para que el fondo reaccione al
   desplazamiento de la pagina.

   Respeta las mismas reglas que el resto del tema: movimiento reducido, ahorro
   de datos, pausa al salir de pantalla, pausa con la pestana oculta, tope de
   densidad de pixeles y guarda de idempotencia para el editor. */
(function () {
  'use strict';

  // Registro de instancias vivas: permite soltarlas cuando el editor de temas
  // reemplaza la seccion y su lienzo desaparece de la pagina.
  var live = [];

  var VERT = 'attribute vec2 a_position;void main(){gl_Position=vec4(a_position,0.0,1.0);}';

  var FRAG = [
    '#ifdef GL_FRAGMENT_PRECISION_HIGH',
    'precision highp float;',
    '#else',
    'precision mediump float;',
    '#endif',
    'uniform vec3 u_colors[4];',
    'uniform vec4 u_scene;',   // resolucion.xy, tiempo, numero de colores
    'uniform vec4 u_shape;',   // escala, intensidad, grosor, grano
    'uniform vec4 u_extra;',   // scroll, contraste, semilla, 0
    '#define u_resolution u_scene.xy',
    '#define u_time u_scene.z',
    '#define u_colorCount u_scene.w',
    '#define u_scale u_shape.x',
    '#define u_intensity u_shape.y',
    '#define u_paramA u_shape.z',
    '#define u_grain u_shape.w',
    '#define u_scroll u_extra.x',
    '#define u_contrast u_extra.y',
    '#define u_seed u_extra.z',
    // ruido blanco uniforme para el grano (hash de Dave Hoskins)
    'float grainHash(vec2 p){vec3 p3=fract(vec3(p.xyx)*0.1031);p3+=dot(p3,p3.yzx+33.33);return fract((p3.x+p3.y)*p3.z);}',
    // mezcla por la paleta; sin OKLab porque el preset lo trae apagado
    'vec3 palette(float x){',
    '  float n=max(u_colorCount-1.0,1.0);',
    '  float f=clamp(x,0.0,1.0)*n;',
    '  vec3 col=u_colors[0];',
    '  for(int i=0;i<3;i++){',
    '    if(float(i)<n) col=mix(col,u_colors[i+1],smoothstep(0.0,1.0,clamp(f-float(i),0.0,1.0)));',
    '  }',
    '  return col;',
    '}',
    'void main(){',
    '  vec2 screenUv=gl_FragCoord.xy/u_resolution.xy;',
    '  float lado=min(u_resolution.x,u_resolution.y);',
    '  vec2 p=(gl_FragCoord.xy-0.5*u_resolution.xy)/lado;',
    // el scroll acerca el marco y aviva el pulso
    '  float zoom=u_scale*(1.0-u_scroll*0.28);',
    '  p*=zoom;',
    // El marco se deduce de lo que DE VERDAD se ve. Con la caja fija de
    // 0.82 x 0.47, en un movil vertical el eje X solo llegaba a ±0.62: los
    // dos lados quedaban fuera de pantalla y el visitante veia una unica
    // barra horizontal en vez de un marco. Pasaba en iPhone y en iPad; solo
    // en escritorio se veia entero. Ahora la caja ocupa el 80 % de la mitad
    // visible en cada eje, asi que el marco se cierra en cualquier formato.
    '  vec2 mitad=0.5*u_resolution.xy/lado*zoom;',
    // En vertical el marco se acerca a los bordes: la pantalla es estrecha y
    // el titulo necesita el ancho. Con el 0.80 fijo, en un iPhone el titulo
    // se metia SIETE PIXELES dentro del neon por los dos lados (medido).
    // En apaisado sobra sitio y un marco mas recogido se ve mejor.
    '  float ar=u_resolution.x/u_resolution.y;',
    '  float factor=mix(0.88,0.80,clamp((ar-0.6)/0.8,0.0,1.0));',
    '  vec2 box=mitad*factor;',
    '  vec2 d=abs(p)-box;',
    '  float outside=length(max(d,0.0))+min(max(d.x,d.y),0.0);',
    '  float thickness=mix(0.018,0.11,u_paramA)*(1.0+u_scroll*0.9);',
    // El neon de verdad es una linea FINA y muy brillante rodeada de un halo
    // ancho que cae rapido. Un unico trazo grueso con desenfoque uniforme se
    // lee como una mancha de luz, que es lo que se veia.
    '  float dist=abs(outside);',
    '  float nucleo=1.0-smoothstep(thickness*0.10,thickness*0.40,dist);',
    '  float halo=exp(-dist/max(thickness*0.70,0.0005));',
    '  float edge=clamp(nucleo+halo*0.55,0.0,1.0);',
    '  float perimeter=atan(p.y*box.x,p.x*box.y)/6.2831853+0.5;',
    '  float speed=1.8+u_scroll*3.4;',
    '  float inten=u_intensity+u_scroll*0.45;',
    '  float pulse=0.5+0.5*sin(perimeter*(5.0+inten*9.0)-u_time*speed);',
    '  float trail=pow(pulse,mix(7.0,2.0,clamp(inten,0.0,1.0)));',
    // Segundo pulso, mas lento y en sentido contrario. Dos luces que se
    // cruzan leen como energia; una sola lee como un led parpadeando.
    '  float pulso2=0.5+0.5*sin(perimeter*(3.0+inten*5.0)+u_time*speed*0.62+2.1);',
    '  trail=max(trail,pow(pulso2,mix(9.0,3.0,clamp(inten,0.0,1.0)))*0.55);',
    // Esquinas marcadas, como el visor de la seccion de video: da familia a
    // las dos secciones. Solo brilla donde ya hay borde, no inventa luz.
    '  float dEsq=length(abs(p)-box);',
    '  float esquina=exp(-dEsq*dEsq*70.0);',
    '  float innerGlow=exp(-dist*24.0)*(0.32+u_scroll*0.30);',
    // Rejilla en fuga bajo el horizonte. Da profundidad al interior, que
    // antes era un rectangulo negro vacio, y es el mismo motivo que la
    // seccion de video: las dos secciones se leen como familia.
    '  float rejilla=0.0;',
    // El horizonte va al 38 % por debajo del centro: mas arriba, las lineas
    // caian justo detras del subtitulo y le robaban nitidez.
    '  float horiz=-mitad.y*0.38;',
    '  float bajo=horiz-p.y;',
    '  if(bajo>0.004){',
    '    float z=0.13/bajo;',
    '    float lz=abs(fract(z-u_time*0.09)-0.5);',
    '    float lx=abs(fract(p.x*z*0.85)-0.5);',
    // Se apaga en los dos extremos: pegada al horizonte se amontona y abajo
    // del todo compite con el borde del marco.
    '    float caida=exp(-bajo*2.2)*smoothstep(0.0,0.10,bajo);',
    '    rejilla=(smoothstep(0.050,0.0,lz)+smoothstep(0.035,0.0,lx))*caida*0.22;',
    '  }',
    // Carril tenue SIEMPRE visible y el pulso encima. Sin el, palette(0)
    // devuelve el propio color de fondo, asi que el tramo sin luz se borraba
    // y el marco se leia como roto en vez de como una luz que recorre un
    // carril. Se vio en una captura del movil, no en el codigo.
    '  vec3 carril=palette(0.20);',
    '  vec3 luz=palette(trail);',
    '  vec3 col=u_colors[0];',
    '  col=mix(col,palette(0.45),rejilla);',
    '  col=mix(col,carril,nucleo*0.50+halo*0.16);',
    '  col=mix(col,luz,clamp(edge*trail+innerGlow+esquina*nucleo*0.85,0.0,1.0));',
    '  col=(col-0.5)*u_contrast+0.5;',
    // El grano se aparta del centro: ahi va el titulo y el ruido le quitaba
    // nitidez. En los bordes se mantiene, que es donde aporta textura.
    '  float delCentro=clamp(length(p)/max(length(mitad),0.0001),0.0,1.0);',
    '  if(u_grain>0.0001) col+=(grainHash(gl_FragCoord.xy+vec2(u_seed*17.0,u_seed*31.0))-0.5)*u_grain*(0.18+0.82*delCentro);',
    '  gl_FragColor=vec4(clamp(col,0.0,1.0),1.0);',
    '}'
  ].join('\n');

  function hexToRgb(hex, fallback) {
    var h = String(hex || '').trim().replace('#', '');
    if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
    if (!/^[0-9a-f]{6}$/i.test(h)) return fallback;
    return [parseInt(h.slice(0, 2), 16) / 255, parseInt(h.slice(2, 4), 16) / 255, parseInt(h.slice(4, 6), 16) / 255];
  }

  function init(canvas) {
    if (!canvas || canvas.getAttribute('data-vinit-shader')) return;
    canvas.setAttribute('data-vinit-shader', '1');

    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var saveData = !!(navigator.connection && navigator.connection.saveData);
    // host = la capa del fondo (para medir), root = la seccion entera.
    // --hs-scroll tiene que vivir en la seccion: si se escribe en la capa
    // del fondo, el contenido del hero es su hermano y no la hereda.
    var host = canvas.parentNode;
    var root = (canvas.closest && canvas.closest('.hero-shader')) || host;

    // Sin WebGL, con movimiento reducido o con ahorro de datos, el degradado
    // CSS del contenedor se queda como fondo: nunca hay un hueco vacio.
    if (saveData) return;
    if (!window.WebGLRenderingContext) return;

    // Los parametros se leen una sola vez y viven fuera del contexto: si el
    // navegador tira el contexto y hay que reconstruirlo, no se vuelven a
    // parsear ni se pierden.
    var d = canvas.dataset;
    var bg = hexToRgb(d.bg, [0.02, 0.027, 0.051]);
    var c1 = hexToRgb(d.c1, [0.071, 0.380, 0.627]);
    var c2 = hexToRgb(d.c2, [0.208, 0.769, 0.910]);
    var c3 = hexToRgb(d.c3, [0.949, 0.984, 1.0]);
    var scale = parseFloat(d.scale) || 1.26;
    var intensity = parseFloat(d.intensity); if (isNaN(intensity)) intensity = 0.35;
    var thickness = parseFloat(d.thickness); if (isNaN(thickness)) thickness = 0.28;
    var grain = parseFloat(d.grain); if (isNaN(grain)) grain = 0.042;
    var timeScale = parseFloat(d.speed); if (isNaN(timeScale)) timeScale = 0.575;
    var scrollOn = d.scroll !== 'false';

    var gl = null, prog = null, buf = null;
    var uColors, uScene, uShape, uExtra;

    /* Todo el montaje de WebGL en una funcion, para poder repetirlo.
       El navegador puede retirar el contexto cuando le convenga: al pasar de
       un grafico a otro, bajo presion de memoria, o cuando hay demasiados
       lienzos vivos. En el editor de temas pasa de verdad, porque cada
       recarga de la seccion crea uno nuevo, y desplazandose rapido se
       encadenan varias. Sin esto el hero se quedaba muerto para siempre. */
    function construirGL() {
      if (!gl) {
        try {
          gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'low-power' })
            || canvas.getContext('experimental-webgl', { antialias: false, alpha: false });
        } catch (e) { return false; }
      }
      if (!gl || gl.isContextLost()) return false;

      function compile(type, src) {
        var s = gl.createShader(type);
        gl.shaderSource(s, src); gl.compileShader(s);
        if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) { gl.deleteShader(s); return null; }
        return s;
      }
      var vs = compile(gl.VERTEX_SHADER, VERT);
      var fs = compile(gl.FRAGMENT_SHADER, FRAG);
      if (!vs || !fs) return false;
      prog = gl.createProgram();
      gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
      gl.deleteShader(vs); gl.deleteShader(fs);
      if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return false;
      gl.useProgram(prog);

      buf = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buf);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      var loc = gl.getAttribLocation(prog, 'a_position');
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

      uColors = gl.getUniformLocation(prog, 'u_colors');
      uScene = gl.getUniformLocation(prog, 'u_scene');
      uShape = gl.getUniformLocation(prog, 'u_shape');
      uExtra = gl.getUniformLocation(prog, 'u_extra');

      gl.uniform3fv(uColors, new Float32Array([].concat(bg, c1, c2, c3)));
      gl.uniform4f(uShape, scale, intensity, thickness, grain);
      return true;
    }

    if (!construirGL()) return;

    var raf = 0, visible = true, inView = true, disposed = false;
    var start = performance.now();
    var scroll = 0, targetScroll = 0, lastNow = null, lastVar = null;
    var needsResize = true, offs = [];

    // Cada escuchador se apunta para poder soltarlo: en el editor de temas la
    // seccion se recarga muchas veces y, sin esto, cada recarga dejaba una
    // instancia viva escuchando scroll y resize para siempre.
    function on(target, type, fn, opts) {
      target.addEventListener(type, fn, opts);
      offs.push(function () { target.removeEventListener(type, fn, opts); });
    }

    function resize() {
      needsResize = false;
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = Math.max(1, Math.round(canvas.clientWidth * dpr));
      var h = Math.max(1, Math.round(canvas.clientHeight * dpr));
      // Tope de 2 megapixeles: en pantallas grandes evita fundir la GPU.
      var k = Math.min(1, Math.sqrt(2000000 / Math.max(1, w * h)));
      w = Math.max(1, Math.round(w * k)); h = Math.max(1, Math.round(h * k));
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w; canvas.height = h; gl.viewport(0, 0, w, h);
      }
    }

    // Medir el hero obliga al navegador a recalcular la maqueta. Por eso se
    // hace dentro del fotograma y no en el escuchador de scroll: asi se paga
    // una vez por fotograma en lugar de una vez por evento.
    function readScroll() {
      if (!scrollOn || !root) return;
      var r = root.getBoundingClientRect();
      if (r.height <= 0) return;
      var t = -r.top / r.height;
      targetScroll = t < 0 ? 0 : (t > 1 ? 1 : t);
    }

    function request() { if (!disposed && visible && inView && !raf) raf = requestAnimationFrame(frame); }

    function frame(now) {
      raf = 0;
      if (disposed || !visible || !inView) return;
      // Dibujar sobre un contexto perdido no pinta nada y deja el hero en
      // negro. Si se ha perdido, se espera a que el navegador lo devuelva.
      if (!gl || gl.isContextLost()) return;
      var dt = lastNow === null ? 0 : Math.min((now - lastNow) / 1000, 0.1);
      lastNow = now;
      if (needsResize) resize();
      readScroll();
      scroll += (targetScroll - scroll) * (1 - Math.exp(-8 * dt));

      // El mismo valor se publica como variable CSS para que el contenido del
      // hero reaccione al scroll sin necesidad de otro escuchador. Solo se
      // escribe cuando cambia de verdad: escribirla cada fotograma obligaba a
      // recalcular estilos aun con la pagina quieta.
      var vs = scroll.toFixed(3);
      if (vs !== lastVar && root && root.style) { lastVar = vs; root.style.setProperty('--hs-scroll', vs); }

      var t = reduce ? 0 : ((now - start) / 1000) * timeScale;
      gl.uniform4f(uScene, canvas.width, canvas.height, t, 4);
      gl.uniform4f(uExtra, scroll, 1.005, 1.0, 0.0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      // Con movimiento reducido se pinta un fotograma fijo y se para, salvo
      // que el scroll aun se este asentando.
      if (!reduce || Math.abs(targetScroll - scroll) > 0.001) request();
      else lastNow = null;
    }

    function pause() { if (raf) { cancelAnimationFrame(raf); raf = 0; } lastNow = null; }

    on(window, 'scroll', request, { passive: true });
    on(window, 'resize', function () { needsResize = true; request(); });
    on(document, 'visibilitychange', function () {
      visible = document.visibilityState === 'visible';
      if (visible) request(); else pause();
    });

    /* preventDefault en webglcontextlost es obligatorio: sin el, el navegador
       no vuelve a emitir webglcontextrestored nunca y el lienzo queda muerto.
       Con el, el hero se reconstruye solo y mientras tanto se ve el degradado
       CSS de debajo, que nunca se retira. */
    on(canvas, 'webglcontextlost', function (e) {
      e.preventDefault();
      pause();
      canvas.classList.remove('is-live');
    });
    on(canvas, 'webglcontextrestored', function () {
      if (disposed) return;
      prog = null; buf = null;
      if (!construirGL()) return;
      needsResize = true;
      lastNow = null;
      canvas.classList.add('is-live');
      request();
    });

    var io = null, ro = null;
    if ('IntersectionObserver' in window) {
      io = new IntersectionObserver(function (en) {
        inView = en[0] ? en[0].isIntersecting : true;
        if (inView) request(); else pause();
      }, { threshold: 0 });
      io.observe(canvas);
    }
    // El hero cambia de alto al girar el movil o al abrir la barra del
    // navegador sin que llegue un evento resize: ResizeObserver si lo ve.
    if ('ResizeObserver' in window) {
      ro = new ResizeObserver(function () { needsResize = true; request(); });
      ro.observe(canvas);
    }

    function dispose() {
      if (disposed) return;
      disposed = true;
      pause();
      for (var i = 0; i < offs.length; i++) offs[i]();
      offs = [];
      if (io) { io.disconnect(); io = null; }
      if (ro) { ro.disconnect(); ro = null; }
      // Soltar los recursos antes de tirar el contexto: en el editor, donde se
      // crean y destruyen lienzos a cada recarga, ayuda al navegador a
      // reciclar en vez de acumular hasta quedarse sin contextos.
      if (gl && !gl.isContextLost()) {
        if (buf) { gl.deleteBuffer(buf); buf = null; }
        if (prog) { gl.deleteProgram(prog); prog = null; }
        var lose = gl.getExtension('WEBGL_lose_context');
        if (lose) lose.loseContext();
      }
      gl = null;
      var at = live.indexOf(entry);
      if (at !== -1) live.splice(at, 1);
    }

    var entry = { canvas: canvas, dispose: dispose };
    live.push(entry);

    canvas.classList.add('is-live');
    resize(); readScroll(); request();
  }

  // Cuantos lienzos WebGL puede haber vivos a la vez. Los navegadores tienen
  // su propio tope (alrededor de 16 en Chrome) y, al pasarse, matan el mas
  // antiguo sin avisar. En el editor, desplazandose rapido, cada recarga de la
  // seccion crea uno nuevo y se pueden encadenar varios antes de que dé tiempo
  // a limpiar. Con un tope propio y muy por debajo del suyo, el que se retira
  // lo elegimos nosotros y de forma ordenada.
  var MAX_VIVOS = 4;

  function boot() {
    // Antes de arrancar nada se sueltan las instancias cuyo lienzo ya no esta
    // en la pagina: el editor de temas reemplaza el HTML de la seccion entera.
    for (var j = live.length - 1; j >= 0; j--) {
      if (!document.contains(live[j].canvas)) live[j].dispose();
    }
    // Y si aun asi quedan demasiadas, se retiran las mas antiguas.
    while (live.length >= MAX_VIVOS) live[0].dispose();
    var list = document.querySelectorAll('[data-hero-shader]');
    for (var i = 0; i < list.length; i++) init(list[i]);
  }
  boot();
  // El editor de temas sustituye el HTML de la seccion: hay que reenganchar.
  document.addEventListener('shopify:section:load', boot);
  document.addEventListener('shopify:section:unload', boot);
})();
