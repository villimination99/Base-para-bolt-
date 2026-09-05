/* Villumination - Intro "Pulso".
   ------------------------------------------------------------------
   Una entrada, no una animacion. El visitante ENTRA a un gimnasio y sale a la
   tienda. 4,2 s en la version completa, 2,4 s en la corta.

     0,0-0,3  NEGRO. Ninguna pelicula empieza con imagen: empieza con negro.
     0,3-1,0  PULSO. Un electrocardiograma de verdad (onda P, complejo QRS,
              onda T) cruza la pantalla. El cabezal frena a camara lenta justo
              en el QRS: ahi esta el drama, y pasarlo a velocidad constante lo
              desperdiciaba.
     0,7      IMPACTO. En el pico R la linea revienta -- destello, dos ondas de
              choque, arcos de carga -- y la SALA se despliega desde el punto
              de fuga hacia el visitante.
     0,7-3,3  NUCLEO. Las particulas se organizan en una malla que gira y LATE,
              con pulsos recorriendo sus conexiones. Debajo, una frase.
     3,3-4,2  COLAPSO. La malla se contrae en el anillo del emblema y aparece
              la marca.

   Lo que sostiene que esto se lea como un plano y no como cinco efectos:

   - UNA SOLA CAMARA, de principio a fin, por un trayecto con arranque y
     frenada. El suelo, la malla y hasta el electrocardiograma se proyectan
     desde ese mismo punto de vista, asi que el mundo se mueve junto. Termina
     en cero justo cuando entra el emblema, que es un elemento de la pagina y
     no se puede mover.
   - LA PARTICULA i ES EL NODO i. No hay tres sistemas: hay uno recorriendo
     tres formas -- pico, esfera, anillo -- asi que los cambios son
     interpolaciones y no sustituciones. El anillo final es la esfera
     aplastada, o sea que el colapso sale gratis.
   - LAS ARISTAS SE CALCULAN UNA VEZ. La esfera es rigida y su topologia no
     cambia nunca; por fotograma solo quedan las transformaciones.
   - EL BRILLO son tres pasadas de trazo, no shadowBlur sobre un camino de
     doscientos puntos. Se ve igual y cuesta una fraccion.
   - NADA DE WebGL. hero-shader.js ya ocupa el unico contexto GL del tema, y
     esto se carga sin defer porque es lo PRIMERO que se ve.
   - EL MOTOR SE MIDE A SI MISMO. Con los primeros veinte fotogramas decide si
     este aparato puede permitirse los extras; el grano de pelicula, por
     ejemplo, solo se enciende si va sobrado. Ninguna decision de calidad se
     toma por el modelo ni por el ancho de pantalla.
   - DOS PUERTAS. El boton de entrar aparece a los 2,4 s, antes de que la
     secuencia acabe: la espera obligada no crece aunque crezca el espectaculo.
   - Con movimiento reducido no hay secuencia: se pinta el fotograma final, el
     mismo que ve todo el mundo.
   - Al cerrarse se para todo y se suelta el lienzo. Un bucle corriendo detras
     de la tienda es bateria robada.
*/
(function () {
  'use strict';

  var lienzo = document.getElementById('splash-canvas');
  var caja = document.querySelector('[data-splash]');
  if (!lienzo || !caja) return;

  var ctx = null;
  try { ctx = lienzo.getContext('2d'); } catch (e) { return; }
  if (!ctx) return;

  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e2) {}

  var ahorro = false;
  try { ahorro = !!(navigator.connection && navigator.connection.saveData); } catch (e3) {}

  /* ---------- calidad ----------
     Arranca en alto y solo baja. Nunca sube a media secuencia: un cambio de
     calidad en marcha se nota mas que ir un punto por debajo. */
  var CAL = { halo: true, enlaces: true, estelas: true, arcos: true, factor: 1 };
  if (ahorro) { CAL.halo = false; CAL.arcos = false; CAL.factor = 0.6; }

  /* ---------- medidas ---------- */
  // 1.5x como tope: la intro dura dos segundos y medio, no compensa pintar a
  // 3x en un movil y quedarse sin fotogramas justo en la primera impresion.
  var DPR = Math.min(window.devicePixelRatio || 1, ahorro ? 1 : 1.5);
  var W = 0, H = 0, cx = 0, cy = 0, radio = 0;
  var yBase = 0, alto = 0;   // linea base del trazo y amplitud del latido
  var XW = 0, X0 = 0, AV_MAX = 1, X_IZQ = 0;  // ventana horizontal del latido

  function medir() {
    var w = caja.clientWidth || window.innerWidth;
    var h = caja.clientHeight || window.innerHeight;
    lienzo.width = W = Math.max(1, Math.round(w * DPR));
    lienzo.height = H = Math.max(1, Math.round(h * DPR));
    lienzo.style.width = w + 'px';
    lienzo.style.height = h + 'px';
    cx = W / 2;
    // El anillo del emblema no esta en el centro vertical: debajo van el
    // titulo, el lema y el boton. Se mide el emblema de verdad en vez de
    // suponer, para que las particulas aterricen donde toca.
    var em = caja.querySelector('.splash-emblem');
    if (em) {
      var r = em.getBoundingClientRect(), rc = caja.getBoundingClientRect();
      // El CENTRO si sale del rectangulo: las transformaciones del emblema
      // giran y escalan sobre su propio centro, que no se mueve.
      cx = (r.left - rc.left + r.width / 2) * DPR;
      cy = (r.top - rc.top + r.height / 2) * DPR;
      // El RADIO no. Mientras dura la secuencia el emblema esta congelado en
      // el fotograma inicial de logoAppear, que es scale(0.5), asi que el
      // rectangulo mide la MITAD de lo que va a medir. Midiendolo asi, las
      // particulas formaban un anillo del tamano equivocado y la amplitud del
      // latido se quedaba en un munon. offsetWidth ignora las transformaciones
      // y devuelve el tamano real de maquetacion.
      radio = ((em.offsetWidth || r.width) / 2) * DPR;
    }
    if (!radio) { cy = H * 0.38; radio = Math.min(W, H) * 0.16; }

    // Composicion: la punta del pico R aterriza un pelo por debajo del
    // anillo, de modo que el estallido ocurre en la puerta del emblema y las
    // particulas apenas tienen que viajar para formarlo.
    alto = Math.min(H * 0.15, radio * 1.45, W * 0.30);
    yBase = cy + radio * 1.10 + alto;
    if (yBase > H * 0.90) yBase = H * 0.90;
    if (yBase - alto < cy + radio * 0.55) alto = yBase - cy - radio * 0.55;

    // VENTANA HORIZONTAL. El latido no puede ocupar siempre todo el ancho:
    // en una pantalla panoramica el complejo QRS se estiraba tanto que
    // quedaba en una arruga dentro de una raya inmensa, y el momento
    // dramatico de la secuencia se perdia. Se le da un ancho acotado y el
    // resto se rellena con la linea base plana, que es justo lo que se ve en
    // un monitor de verdad.
    XW = Math.min(W, Math.max(H * 1.0, W * 0.50));
    X0 = cx - XW * X_PICO;          // el pico R cae en el centro exacto
    X_IZQ = -X0 / XW;               // borde izquierdo en coordenadas de onda
    AV_MAX = (W - X0) / XW;         // borde derecho, idem
  }

  /* ---------- colores de la marca ---------- */
  function varCss(nombre, respaldo) {
    try {
      var v = getComputedStyle(document.documentElement).getPropertyValue(nombre).trim();
      return v || respaldo;
    } catch (e4) { return respaldo; }
  }
  var CIAN = varCss('--neon-cyan', '#00d4ff');
  var ROSA = varCss('--neon-pink', '#ff2ecb');
  var VERDE = varCss('--neon-green', '#00e87b');
  var PALETA = [CIAN, ROSA, VERDE];

  // rgba a partir de un #rrggbb, para poder graduar la opacidad dentro de un
  // gradiente (globalAlpha no sirve cuando dos capas se solapan).
  function rgba(hex, a) {
    var h = String(hex).replace('#', '');
    if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
    var n = parseInt(h, 16);
    if (isNaN(n)) return 'rgba(0,212,255,' + a + ')';
    return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')';
  }

  /* ---------- el latido ----------
     Un electrocardiograma de verdad, no una linea en zigzag: onda P, complejo
     QRS y onda T. Se reconoce al instante justamente porque es el de verdad.
     Devuelve el desplazamiento vertical en unidades de -1 a 1 para x en 0..1. */
  function latido(x) {
    if (x < 0.30 || x > 0.86) return 0;
    // Onda P: la pequena joroba previa
    if (x < 0.38) return Math.sin((x - 0.30) / 0.08 * Math.PI) * 0.12;
    if (x < 0.44) return 0;
    // Complejo QRS: bajada corta, pico alto y bajada profunda
    if (x < 0.47) return -((x - 0.44) / 0.03) * 0.18;
    if (x < 0.51) return -0.18 + ((x - 0.47) / 0.04) * 1.18;
    if (x < 0.55) return 1.00 - ((x - 0.51) / 0.04) * 1.42;
    if (x < 0.58) return -0.42 + ((x - 0.55) / 0.03) * 0.42;
    if (x < 0.68) return 0;
    // Onda T: la joroba ancha de recuperacion
    if (x < 0.86) return Math.sin((x - 0.68) / 0.18 * Math.PI) * 0.26;
    return 0;
  }
  var X_PICO = 0.51;   // donde revienta

  /* El trazo tambien viaja con la camara. Es un monitor DENTRO de la sala: si
     la camara se mueve y el monitor no, se ve que son dos capas y no un
     espacio. */
  function ptX(x) { return X0 + x * XW + camDX; }
  function ptY(x) { return yBase - latido(x) * alto + camDY; }

  /* ---------- ritmo del cabezal ----------
     La gracia esta aqui. Un barrido a velocidad constante desperdicia el
     unico momento interesante: el cabezal debe LLEGAR rapido a la zona del
     QRS y luego atravesarla a camara lenta, que es donde el ojo se queda.
     Cada par es (fraccion de tiempo, fraccion de recorrido). */
  var RITMO = [[0, 0], [0.26, 0.30], [0.40, 0.44], [0.66, 0.58], [1, 1]];
  function avanceEn(ft) {
    ft = lim(ft, 0, 1);
    for (var i = 1; i < RITMO.length; i++) {
      if (ft <= RITMO[i][0]) {
        var a = RITMO[i - 1], b = RITMO[i];
        var k = (ft - a[0]) / (b[0] - a[0]);
        var fin = (i === RITMO.length - 1) ? AV_MAX : b[1];
        return a[1] + (fin - a[1]) * k;
      }
    }
    return AV_MAX;
  }
  // Instante en el que el cabezal alcanza el pico R (lo necesitan el impacto,
  // el estallido y la sacudida, y tiene que ser EL MISMO para los tres).
  function tiempoDe(x) {
    for (var i = 1; i < RITMO.length; i++) {
      if (x <= RITMO[i][1]) {
        var a = RITMO[i - 1], b = RITMO[i];
        var k = (x - a[1]) / (b[1] - a[1]);
        return a[0] + (b[0] - a[0]) * k;
      }
    }
    return 1;
  }

  /* ---------- particulas ---------- */
  var N = 0, ps = [], anillo = [];
  // Un grupo por color de marca; dentro, las estelas se reparten en dos
  // grosores. El grosor es estado del trazado, asi que agrupar por el es lo
  // que permite dibujarlas de una sola pasada.
  var grupos = PALETA.map(function (c) {
    return { c: c, op: 0, n: 0, puntos: [], estelas: [[], []] };
  });
  function sembrar() {
    var ancho = W / DPR;
    N = Math.round((ancho < 700 ? 132 : 208) * CAL.factor);
    ps = [];
    anillo = [];
    var pkx = ptX(X_PICO), pky = ptY(X_PICO);
    for (var i = 0; i < N; i++) {
      // Dos tercios nacen EN el pico: son la explosion. El tercio restante
      // nace repartido por el trazo ya dibujado: son la linea deshaciendose.
      var deLinea = (i % 3) === 2;
      /* Se guarda la coordenada de ONDA, no la de pantalla. La posicion en
         pantalla depende de donde este la camara, y la camara se mueve entre
         que se siembran las particulas y que revientan: guardando pixeles, el
         estallido nacia quince pixeles por encima del trazo que se ve. */
      var tx = deLinea ? X_IZQ + Math.random() * (0.86 - X_IZQ) : X_PICO;
      var jx = deLinea ? 0 : (Math.random() - 0.5) * 10 * DPR;
      var jy = deLinea ? 0 : (Math.random() - 0.5) * 18 * DPR;
      var ox = ptX(tx) + jx, oy = ptY(tx) + jy;
      // Destino: tres de cada cuatro en el anillo del emblema; el resto en
      // una nube exterior que da profundidad y evita el anillo de juguete.
      // TODAS al anillo. Antes una de cada cuatro se iba a una nube exterior
      // que daba profundidad durante el estallido, pero al colapsar se quedaba
      // como escombros flotando alrededor del logotipo justo en el momento en
      // que la mirada tiene que ir a la marca.
      var enAnillo = true;
      var ang = (i / N) * Math.PI * 2 + (Math.random() - 0.5) * 0.14;
      var rr = radio * (1.00 + Math.random() * 0.16);
      // Salida radial desde el pico: una explosion de verdad sale del centro,
      // no en direcciones al azar que se anulan entre si.
      var sa = Math.atan2(oy - pky, ox - pkx) + (Math.random() - 0.5) * 1.5;
      if (!deLinea) sa = Math.random() * Math.PI * 2;
      var vel = (14 + Math.random() * 30) * DPR;
      var p = {
        ox: ox, oy: oy, txw: tx, jx: jx, jy: jy,
        dx: cx + Math.cos(ang) * rr,
        dy: cy + Math.sin(ang) * rr,
        vx: Math.cos(sa) * vel,
        vy: Math.sin(sa) * vel * 0.85,
        x: ox, y: oy, ax: ox, ay: oy, px: 0, py: 0,
        r: (enAnillo ? 1.1 + Math.random() * 1.5 : 0.7 + Math.random() * 1.0) * DPR,
        c: PALETA[i % PALETA.length],
        g: i % PALETA.length,
        retardo: deLinea ? Math.random() * 0.16 : Math.random() * 0.07,
        // Fase propia para el latir del estado final: si todas parpadean a la
        // vez parece un fallo de pantalla, no un organismo.
        fase: Math.random() * Math.PI * 2,
        ang: ang, rr: rr, aro: enAnillo, listo: false
      };
      p.grueso = p.r > 1.6 * DPR ? 1 : 0;
      ps.push(p);
      if (enAnillo) anillo.push(p);
    }
    // Ordenadas por angulo: asi enlazar la i con la i+1 dibuja el circulo
    // completo con N lineas, en vez de comparar todas contra todas.
    anillo.sort(function (a, b) { return a.ang - b.ang; });

    // La malla no es otro sistema de particulas: es EL MISMO. La particula i
    // es el nodo i de la esfera. Por eso el estallido puede convertirse en la
    // malla y la malla en el anillo sin que nada aparezca ni desaparezca.
    if (MALLA) { medirEsfera(); sembrarMalla(N); }
  }

  /* ---------- la malla ----------
     La referencia son lineas de luz formando una red, no una bola de puntos:
     las ARISTAS son las protagonistas y los nodos solo las sujetan.

     Dos decisiones sostienen todo esto:

     1. Los nodos se reparten con una red de Fibonacci, no al azar. El azar
        sobre una esfera deja calvas y grumos que se ven al primer vistazo.
     2. Las aristas se calculan UNA sola vez. La esfera es rigida, su
        topologia no cambia nunca, asi que por fotograma solo quedan las
        transformaciones y unos segmentos ya conocidos. Es lo que hace que
        una malla de seiscientas lineas cueste tres trazados.

     Y no hay WebGL a proposito: hero-shader.js ya ocupa el unico contexto GL
     del tema, un segundo contexto en plena carga inicial es la via rapida a
     una perdida de contexto en un movil viejo, y esto es lo PRIMERO que se
     ve. La proyeccion a mano da profundidad de verdad con una fraccion del
     riesgo. */
  var R_ESF = 0, FOCO = 0, INC_C = 1, INC_S = 0;
  var nodos = null, proyX = null, proyY = null, proyK = null, proyZ = null;
  var aristas = null, pulsos = [];

  function medirEsfera() {
    // Mas grande que el anillo, para que el colapso final se note como una
    // contraccion de verdad y no como un encogimiento tibio.
    /* El tope por ancho es W*0.319 y no W*0.40, y ese numero sale de medir.
       El radio proyectado maximo NO es R: con perspectiva, los nodos inclinados
       hacia el visitante se separan mas del centro que la propia silueta, y el
       maximo real es 1,083 R. Sumandole el desvio de la camara, el latido y la
       anticipacion del colapso, con 0.40 la esfera se salia 22 px por el borde
       en un iPhone 12 y 17 en un SE -- reportado con captura. Con 0.319 quedan
       16 px de margen en el peor caso de todos. */
    R_ESF = Math.min(radio * 2.5, H * 0.22, W * 0.319);
    FOCO = R_ESF * 2.6;
    var inc = 0.34;                 // inclinacion fija: una esfera vista de
    INC_C = Math.cos(inc);          // frente y sin inclinar parece un circulo
    INC_S = Math.sin(inc);
    // Las frases van debajo de la esfera, y donde acaba la esfera solo lo sabe
    // el motor. Se publica el radio en pixeles CSS y el CSS lo coloca solo,
    // sin que el JS toque posiciones ni mida nada del texto.
    try { caja.style.setProperty('--esfera-r', (R_ESF / DPR) + 'px'); } catch (e6) {}
  }

  function sembrarMalla(n) {
    nodos = new Float32Array(n * 3);
    var phi = Math.PI * (3 - Math.sqrt(5));   // angulo aureo
    for (var i = 0; i < n; i++) {
      var y = 1 - (i / (n - 1)) * 2;
      var r = Math.sqrt(Math.max(0, 1 - y * y));
      var th = phi * i;
      nodos[i * 3] = Math.cos(th) * r;
      nodos[i * 3 + 1] = y;
      nodos[i * 3 + 2] = Math.sin(th) * r;
    }
    proyX = new Float32Array(n); proyY = new Float32Array(n);
    proyK = new Float32Array(n); proyZ = new Float32Array(n);

    // Vecinos mas cercanos por producto escalar (sobre la esfera unidad, el
    // mayor producto escalar es el vecino mas cercano). Cuesta n al cuadrado
    // UNA vez: con doscientos nodos son cuarenta mil multiplicaciones al
    // sembrar, un suspiro, y no se vuelve a pagar nunca.
    var K = 3, pares = [], vistos = {};
    for (var a = 0; a < n; a++) {
      var ax = nodos[a * 3], ay = nodos[a * 3 + 1], az = nodos[a * 3 + 2];
      var mejores = [];
      for (var b = 0; b < n; b++) {
        if (b === a) continue;
        var d = ax * nodos[b * 3] + ay * nodos[b * 3 + 1] + az * nodos[b * 3 + 2];
        if (mejores.length < K) {
          mejores.push([d, b]);
          mejores.sort(function (u, v) { return u[0] - v[0]; });
        } else if (d > mejores[0][0]) {
          mejores[0] = [d, b];
          mejores.sort(function (u, v) { return u[0] - v[0]; });
        }
      }
      for (var m = 0; m < mejores.length; m++) {
        var j = mejores[m][1];
        var lo = a < j ? a : j, hi = a < j ? j : a;
        var clave = lo * n + hi;
        if (!vistos[clave]) { vistos[clave] = 1; pares.push(lo, hi); }
      }
    }
    aristas = new Int32Array(pares);

    // Pulsos recorriendo las conexiones: es lo que separa una maqueta de algo
    // vivo. Diez a la vez, y cada uno salta a otra arista al llegar al final.
    pulsos = [];
    var m2 = aristas.length / 2;
    for (var q = 0; q < Math.min(10, m2); q++) {
      pulsos.push({ e: (Math.random() * m2) | 0, t: Math.random(), v: 0.5 + Math.random() * 0.6 });
    }
  }

  /* El latido de la malla. Dos golpes seguidos y una pausa, como un corazon de
     verdad, no una onda senoidal: una esfera que gira es una demo tecnologica,
     una que LATE es un cuerpo esforzandose. Es lo que hace deportiva a esta
     parte de la secuencia, y cuesta una multiplicacion por fotograma. */
  function pulsoCorazon(t) {
    var f = (t * 1.85) % 1;                       // ~111 pulsaciones por minuto
    var a = Math.exp(-Math.pow((f - 0.00) / 0.075, 2));   // golpe fuerte
    var b = Math.exp(-Math.pow((f - 0.22) / 0.095, 2)) * 0.55;  // segundo golpe
    return a + b;
  }

  function proyectar(giro, escala) {
    var n = proyX.length;
    var R = R_ESF * (escala || 1);
    var c = Math.cos(giro), s = Math.sin(giro);
    for (var i = 0; i < n; i++) {
      var x = nodos[i * 3], y = nodos[i * 3 + 1], z = nodos[i * 3 + 2];
      var x2 = x * c - z * s;          // giro sobre el eje vertical
      var za = x * s + z * c;
      var y2 = y * INC_C - za * INC_S; // inclinacion fija
      var z2 = y * INC_S + za * INC_C;
      var k = FOCO / (FOCO + z2 * R);   // perspectiva
      proyX[i] = cx + camDX + x2 * R * k;
      proyY[i] = cy + camDY + y2 * R * k;
      proyK[i] = k;
      proyZ[i] = z2;                   // -1 delante, +1 detras
    }
  }

  /* Tres cubos de profundidad. Agrupar por profundidad hace dos cosas a la
     vez: permite pintar la malla entera en tres trazados en lugar de uno por
     arista, y da la niebla -- lo de detras mas fino y mas apagado -- que es
     lo unico que diferencia una esfera de un circulo de rayas. */
  var A_CUBO = [0.09, 0.20, 0.44], W_CUBO = [0.7, 1.0, 1.35];
  function dibujarMalla(op) {
    if (op <= 0.01 || !aristas) return;
    var m = aristas.length / 2;
    /* Puntas planas, no redondas. Cada punta redonda es un circulo que el
       rasterizador tiene que resolver aparte, y aqui hay seiscientas sesenta
       por pasada: con lineas de uno a dos pixeles no se distingue una de otra
       -- comparado con captura, sin diferencia visible -- y ademas los nodos
       se pintan encima, que es lo que de verdad redondea los extremos. Los
       pulsos SI las llevan, y se las ponen ellos. */
    ctx.lineCap = 'butt';
    for (var b = 0; b < 3; b++) {
      ctx.beginPath();
      var hay = false;
      for (var e = 0; e < m; e++) {
        var i = aristas[e * 2], j = aristas[e * 2 + 1];
        var zm = (proyZ[i] + proyZ[j]) * 0.5;
        var cubo = zm < -0.33 ? 2 : (zm < 0.33 ? 1 : 0);
        if (cubo !== b) continue;
        ctx.moveTo(proyX[i], proyY[i]);
        ctx.lineTo(proyX[j], proyY[j]);
        hay = true;
      }
      if (!hay) continue;
      ctx.strokeStyle = rgba(CIAN, A_CUBO[b] * op);
      ctx.lineWidth = W_CUBO[b] * DPR;
      ctx.stroke();
      // El brillo, solo en el cubo delantero. Es el "shiny" de la referencia,
      // y hacerlo en los tres costaria el triple sin verse mas.
      if (b === 2 && CAL.halo) {
        ctx.strokeStyle = rgba(CIAN, 0.10 * op);
        ctx.lineWidth = 3.6 * DPR;
        ctx.stroke();
      }
    }
  }

  function dibujarPulsos(dt, op) {
    if (op <= 0.01 || !aristas || !CAL.arcos) return;
    var m = aristas.length / 2;
    ctx.beginPath();
    for (var q = 0; q < pulsos.length; q++) {
      var P = pulsos[q];
      P.t += dt * P.v;
      if (P.t > 1) { P.t -= 1; P.e = (Math.random() * m) | 0; }
      var i = aristas[P.e * 2], j = aristas[P.e * 2 + 1];
      // Los de detras no se dibujan: un destello viajando por la cara oculta
      // distrae y encima no se entiende que esta pasando.
      if ((proyZ[i] + proyZ[j]) * 0.5 > 0.15) continue;
      var x1 = proyX[i], y1 = proyY[i], dx = proyX[j] - x1, dy = proyY[j] - y1;
      var t2 = P.t, t1 = t2 - 0.26 < 0 ? 0 : t2 - 0.26;
      ctx.moveTo(x1 + dx * t1, y1 + dy * t1);
      ctx.lineTo(x1 + dx * t2, y1 + dy * t2);
    }
    ctx.strokeStyle = rgba('#eafcff', 0.85 * op);
    ctx.lineWidth = 1.8 * DPR;
    ctx.lineCap = 'round';
    ctx.stroke();
  }

  /* ---------- el gimnasio ----------
     Antes la secuencia pasaba en la nada: objetos bonitos sobre negro. Ahora
     pasa en un SITIO, y el visitante entra en el. Es lo que convierte una
     animacion de marca en "acabo de entrar a mi gimnasio".

     Dos piezas y las dos son lineas rectas, que es lo mas barato que sabe
     dibujar un lienzo:

     1. El suelo en perspectiva, con la camara avanzando. El punto de fuga NO
        esta en el centro de la pantalla: esta exactamente en el emblema, asi
        que todo el espacio empuja la mirada hacia la marca y al final se entra
        literalmente en ella.
     2. Los racks a los lados, que pasan de largo segun avanza la camara. Sin
        ellos el suelo es una rejilla de ciencia ficcion cualquiera; con ellos
        se lee gimnasio a la primera.

     Todo se proyecta con la misma division por la profundidad que la malla, y
     el suelo entero cabe en UN trazado con un degradado que lo apaga hacia el
     horizonte, asi que cuesta dos llamadas de dibujo. */
  var Z_MIN = 0.42, SUELO_FILAS = 15, SUELO_CARRILES = 7;
  var VEL_CAM = 1.15;

  /* ---------- la camara, tipo dron ----------
     Esto es lo que separa "capas animadas" de 3D de verdad: el suelo, los
     racks y la esfera se proyectan TODOS desde el mismo punto de vista, asi
     que al mover la camara el mundo entero se mueve junto y el ojo lo lee como
     un espacio, no como dibujos superpuestos.

     El movimiento es un plano de grua: la camara orbita un poco a un lado, se
     eleva, y VUELVE A CERO justo cuando empieza el colapso. Lo de volver a
     cero no es un capricho: el emblema es un elemento de la pagina, esta
     clavado en su sitio, y si la camara siguiera desviada al final las
     particulas aterrizarian al lado de la marca en vez de encima. Un plano de
     dron de verdad tambien termina encuadrando al protagonista. */
  var camDX = 0, camDY = 0;
  /* La camara NO se para entre actos. Antes se quedaba quieta durante el
     latido y solo se movia en la malla, y por eso se notaba la costura: la
     secuencia parecia tres animaciones pegadas en vez de un plano.

     Ahora hay UN trayecto de principio a fin, escrito como puntos por los que
     la camara pasa -- (instante, desvio lateral, elevacion), los dos en
     fracciones de pantalla -- y entre punto y punto se interpola con una curva
     suave. Eso da lo que pide un plano de grua de verdad: arrancar despacio,
     acelerar y frenar. Antes era un seno puro, o sea velocidad constante por
     el centro, que es como no mueve la camara nadie.

     Y termina en cero ANTES de que aparezca el emblema. No es un capricho: el
     emblema es un elemento de la pagina y esta clavado en su sitio; si la
     camara siguiera desviada, las particulas aterrizarian al lado de la marca
     en vez de encima. Un plano de dron de verdad tambien acaba encuadrando al
     protagonista. */
  var RUTA = [
    [0.00, -0.100,  0.055],   // fuera, bajo y a la izquierda
    [0.28,  0.015,  0.012],   // cruza el centro justo con el impacto
    [0.55,  0.085, -0.038],   // orbita a la derecha y sube
    [0.80, -0.045, -0.018],   // vuelve
    [1.00,  0.000,  0.000]    // se posa en la marca
  ];
  function moverCamara(t) {
    if (!MALLA) { camDX = 0; camDY = 0; return; }
    var u = lim(t / T_MALLA, 0, 1);
    for (var i = 1; i < RUTA.length; i++) {
      if (u <= RUTA[i][0]) {
        var a = RUTA[i - 1], b = RUTA[i];
        var k = suave((u - a[0]) / (b[0] - a[0]));
        camDX = (a[1] + (b[1] - a[1]) * k) * W;
        camDY = (a[2] + (b[2] - a[2]) * k) * H;
        return;
      }
    }
    camDX = 0; camDY = 0;
  }

  function ejeY() { return cy + camDY; }         // horizonte = el emblema
  function ejeX() { return cx + camDX; }
  function alturaCam() { return H * 0.40; }
  function anchoSuelo() { return W * 1.35; }

  // Proyecta un punto del mundo: x a los lados, y hacia arriba desde el suelo,
  // z hacia el fondo.
  function pz(x, y, z) {
    var zz = z < Z_MIN ? Z_MIN : z;
    var e = 1 / zz;
    return [ejeX() + x * e, ejeY() + (alturaCam() - y) * e, e];
  }

  function suelo(t, op, rev) {
    if (op <= 0.01) return;
    /* La sala se despliega desde el punto de fuga hacia el visitante, en vez
       de aparecer con un fundido. Es la diferencia entre "aparece un fondo" y
       "se abre una sala delante de mi": la mirada arranca en el emblema, que es
       donde esta el punto de fuga, y el suelo viene hacia ella. Se hace sin
       dibujar nada de mas, simplemente no pintando todavia las filas que aun no
       han llegado. */
    var zCorte = SUELO_FILAS - (SUELO_FILAS - Z_MIN) * frena(rev === undefined ? 1 : rev);
    var av = (t * VEL_CAM) % 1;
    var yH = ejeY(), xH = ejeX(), aC = alturaCam(), aS = anchoSuelo();
    ctx.beginPath();
    // Transversales: las que se acercan a la camara se separan, que es lo que
    // da la sensacion de avanzar.
    for (var i = 0; i < SUELO_FILAS; i++) {
      var z = i + 1 - av;
      if (z < Z_MIN || z < zCorte) continue;
      var e = 1 / z, y = yH + aC * e;
      if (y > H + 6) continue;
      ctx.moveTo(xH - aS * e, y);
      ctx.lineTo(xH + aS * e, y);
    }
    // Longitudinales: todas mueren en el punto de fuga.
    var zCerca = 1 - av < zCorte ? zCorte : 1 - av;
    var e0 = 1 / zCerca, eN = 1 / SUELO_FILAS;
    for (var j = -SUELO_CARRILES; j <= SUELO_CARRILES; j++) {
      var xm = j * (aS / SUELO_CARRILES);
      ctx.moveTo(xH + xm * e0, yH + aC * e0);
      ctx.lineTo(xH + xm * eN, yH + aC * eN);
    }
    // El degradado apaga el suelo hacia el horizonte: sin el, las lineas del
    // fondo se amontonan en una franja solida y se pierde la profundidad.
    var g = ctx.createLinearGradient(0, H, 0, yH);
    g.addColorStop(0, rgba(CIAN, 0.30 * op));
    g.addColorStop(0.55, rgba(CIAN, 0.13 * op));
    g.addColorStop(1, rgba(CIAN, 0));
    ctx.strokeStyle = g;
    ctx.lineWidth = 1.1 * DPR;
    ctx.stroke();
  }

  /* SE RETIRARON LOS RACKS DE LOS LADOS. Eran siluetas en perspectiva que
     pasaban de largo a izquierda y derecha para que se leyera "gimnasio".
     Tenian sentido cuando el fondo era negro; desde que hay una foto de sala
     de verdad detras, a ese tamano ya no se leen como aparatos sino como
     simbolos sueltos cruzando la pantalla, que es exactamente como los
     reporto el cliente. La sala la cuentan ahora el suelo y la foto. */

  function gimnasio(t, op, rev) {
    if (op <= 0.01) return;
    // Solo el suelo. Es UN trazado y es el que lleva toda la lectura de "estoy
    // dentro de un sitio"; ademas su punto de fuga esta en el emblema, asi que
    // empuja la mirada hacia la marca.
    suelo(t, op, rev);
  }

  /* EL GRANO NO VA AQUI, VA EN CSS. La primera version lo pintaba en el
     lienzo: un relleno de patron a pantalla completa en cada fotograma. Medido,
     tumbo la secuencia de 60 fps a 30 con la CPU a 1/4 y a 20 con la CPU a 1/6.
     Son 740.000 pixeles escritos por fotograma para un efecto que, por
     definicion, tiene que ser casi imperceptible: la peor relacion posible
     entre lo que cuesta y lo que aporta.

     En CSS lo compone la tarjeta grafica y cuesta cero fotogramas. Esta en
     .splash-grano. */

  /* ---------- reparto de las frases ----------
     Las ventanas se calculan, no se escriben a mano, y el hueco entre una
     frase y la siguiente es MAYOR que el fundido. Escritas a mano habia 0,10 s
     de hueco contra 0,32 s de fundido, asi que durante 0,22 s se veian las dos
     frases superpuestas -- salio en una captura del cliente. Calculandolas, eso
     no puede volver a pasar aunque manana se configuren tres. */
  var F_HUECO = 0.55;                       // mayor que el fundido de 0,45 s
  function faseFrase(t) {
    if (!nFrases) return -1;
    var ini = T_ESFERA - 0.30, fin = T_MALLA - 0.10;
    var dur = ((fin - ini) - F_HUECO * (nFrases - 1)) / nFrases;
    if (dur <= 0.35) return -1;             // no caben: mejor ninguna que a medias
    for (var i = 0; i < nFrases; i++) {
      var a = ini + i * (dur + F_HUECO);
      if (t >= a && t < a + dur) return i;
    }
    return -1;
  }

  /* ---------- interaccion, para despues de la secuencia ---------- */
  /* La foto de la sala aparece cuando esta cargada, no antes. La secuencia no
     la espera en ningun momento: si tarda, si falla o si el visitante tiene
     bloqueadas las imagenes, la intro es exactamente la de siempre. */
  (function () {
    var escena = caja.querySelector('[data-splash-escena]');
    if (!escena) return;
    function lista() { escena.classList.add('esta-lista'); }
    if (escena.complete && escena.naturalWidth > 0) lista();
    else escena.addEventListener('load', lista);
  })();

  var cajaFrases = caja.querySelector('[data-splash-frases]');
  var nFrases = cajaFrases ? cajaFrases.children.length : 0;
  if (!nFrases) cajaFrases = null;

  var puntero = { x: -9999, y: -9999, activo: false };
  function mover(ev) {
    var t = ev.touches ? ev.touches[0] : ev;
    var r = caja.getBoundingClientRect();
    puntero.x = (t.clientX - r.left) * DPR;
    puntero.y = (t.clientY - r.top) * DPR;
    puntero.activo = true;
  }
  function salir() { puntero.activo = false; puntero.x = -9999; puntero.y = -9999; }

  /* ---------- curvas ---------- */
  function lim(v, a, b) { return v < a ? a : (v > b ? b : v); }
  function suave(x) { x = lim(x, 0, 1); return x * x * (3 - 2 * x); }
  function frena(x) { x = lim(x, 0, 1); return 1 - Math.pow(1 - x, 3); }
  function frenaMas(x) { x = lim(x, 0, 1); return 1 - Math.pow(1 - x, 4.5); }

  /* ---------- tiempos de la secuencia (segundos) ----------
     Una intro es un peaje que el visitante paga antes de ver la tienda, asi
     que hay DOS duraciones y la elige el comerciante desde el editor:

       completa  latido -> malla que gira -> colapso en la marca   3,60 s
       corta     latido -> emblema, directo                        2,40 s

     En las dos, el boton de entrar aparece ANTES del final. La secuencia
     sigue para quien quiera verla, pero nadie se queda esperando: eso es la
     diferencia entre un espectaculo y un peaje. */
  var MALLA = (caja.getAttribute('data-duracion') || 'completa') !== 'corta';
  var T_ENCIENDE = 0.30;  // la linea base se despliega
  var T_TRAZO = 1.05;     // el cabezal termina el recorrido
  var T_ESFERA = 1.75;    // las particulas ya han llegado a la esfera
  var T_MALLA = 3.30;     // fin del giro, empieza el colapso
  var T_FORMA = MALLA ? 4.20 : 2.40;   // las particulas ya estan en el anillo
  var T_PUERTA = MALLA ? 2.40 : T_FORMA;  // cuando se abre la puerta de la tienda
  var T_IMPACTO = T_ENCIENDE + tiempoDe(X_PICO) * (T_TRAZO - T_ENCIENDE);

  var raf = 0, t0 = null, muerto = false, listo = false, puerta = false;
  var tPrevio = null, fraseActual = -2;

  /* ---------- arcos de carga ----------
     Rayos cortos del pico al anillo. Se regeneran cada pocos fotogramas: un
     rayo quieto deja de ser un rayo. */
  var arcos = [], arcoSello = -1;
  function generarArcos(pkx, pky) {
    arcos = [];
    var n = 5;
    for (var i = 0; i < n; i++) {
      var ang = -Math.PI / 2 + (i - (n - 1) / 2) * 0.42;
      var fx = cx + Math.cos(ang) * radio * 1.02;
      var fy = cy + Math.sin(ang) * radio * 1.02;
      var pts = [], seg = 7;
      for (var j = 0; j <= seg; j++) {
        var k = j / seg;
        var x = pkx + (fx - pkx) * k, y = pky + (fy - pky) * k;
        if (j > 0 && j < seg) {
          var amp = Math.sin(k * Math.PI) * 13 * DPR;
          x += (Math.random() - 0.5) * amp;
          y += (Math.random() - 0.5) * amp;
        }
        pts.push(x, y);
      }
      arcos.push(pts);
    }
  }

  /* ---------- dibujo del trazo ----------
     Tres pasadas: halo ancho y apagado, cuerpo con el color de marca y nucleo
     casi blanco en la cola caliente. Es el truco clasico de neon y cuesta la
     centesima parte de un shadowBlur sobre todo el camino. */
  function camino(desde, hasta) {
    ctx.beginPath();
    var pasos = 96, primero = true;
    for (var i = 0; i <= pasos; i++) {
      var x = desde + (hasta - desde) * (i / pasos);
      var px = ptX(x), py = ptY(x);
      if (primero) { ctx.moveTo(px, py); primero = false; } else ctx.lineTo(px, py);
    }
  }

  function trazo(avance, op) {
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';

    // El monitor vacio: la linea base tenue de borde a borde. Da contexto al
    // cabezal y evita que el trazo parezca nacer de la nada cuando la ventana
    // del latido es mas estrecha que la pantalla.
    ctx.beginPath();
    ctx.moveTo(0, yBase); ctx.lineTo(W, yBase);
    ctx.strokeStyle = rgba(CIAN, 0.14 * op);
    ctx.lineWidth = 1.4 * DPR;
    ctx.stroke();

    if (CAL.halo) {
      camino(X_IZQ, avance);
      ctx.strokeStyle = rgba(CIAN, 0.10 * op);
      ctx.lineWidth = 13 * DPR;
      ctx.stroke();
      ctx.strokeStyle = rgba(CIAN, 0.18 * op);
      ctx.lineWidth = 6.5 * DPR;
      ctx.stroke();
    }
    camino(X_IZQ, avance);
    ctx.strokeStyle = rgba(CIAN, 0.92 * op);
    ctx.lineWidth = 2.6 * DPR;
    ctx.stroke();

    // Cola caliente: el ultimo tramo recorrido, en blanco. Es lo que hace que
    // se lea como algo que esta pasando AHORA y no como un dibujo terminado.
    var cola = Math.max(X_IZQ, avance - 0.11);
    if (cola < avance) {
      camino(cola, avance);
      ctx.strokeStyle = rgba('#eafcff', 0.95 * op);
      ctx.lineWidth = 1.5 * DPR;
      ctx.stroke();
    }
  }

  function cabezal(x, op) {
    var hx = ptX(x), hy = ptY(x);
    // Destello de lente: circulo caliente + un trazo horizontal, que es como
    // se comporta una luz muy brillante en una camara.
    var g = ctx.createRadialGradient(hx, hy, 0, hx, hy, 34 * DPR);
    g.addColorStop(0, rgba('#ffffff', 0.95 * op));
    g.addColorStop(0.22, rgba(CIAN, 0.55 * op));
    g.addColorStop(1, rgba(CIAN, 0));
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(hx, hy, 34 * DPR, 0, Math.PI * 2);
    ctx.fill();

    var gl = ctx.createLinearGradient(hx - 60 * DPR, hy, hx + 60 * DPR, hy);
    gl.addColorStop(0, rgba(CIAN, 0));
    gl.addColorStop(0.5, rgba('#ffffff', 0.42 * op));
    gl.addColorStop(1, rgba(CIAN, 0));
    ctx.fillStyle = gl;
    ctx.fillRect(hx - 60 * DPR, hy - 1.1 * DPR, 120 * DPR, 2.2 * DPR);

    ctx.fillStyle = rgba('#ffffff', op);
    ctx.beginPath();
    ctx.arc(hx, hy, 3.2 * DPR, 0, Math.PI * 2);
    ctx.fill();
  }

  /* ---------- vigilante de fotogramas ---------- */
  var ventana = [], ultimoMs = 0;
  var recortado = false, brilloRecortado = false, granoDecidido = false;

  /* ---------- por que TODAS las decisiones se toman a partir de 1,30 s ----------
     Las tres se tomaban antes en el fotograma veintiuno, y eso las tomaba
     todas mal. Los veinte primeros fotogramas de esta secuencia son el telon
     negro: la parte mas barata que existe aqui. Un aparato lento pasaba esa
     medida sobrado, se quedaba con todos los adornos y despues se arrastraba
     durante el resto de la pelicula.

     A partir de 1,30 s ya estan en pantalla la sala en perspectiva, el
     estallido y las particulas. Es el primer instante en el que la medida dice
     algo. Y sigue siendo ANTES de que aparezca la malla, en 1,75 s, que es lo
     que estos escalones recortan: se decide antes de gastar, no despues, y
     nada desaparece a la vista.

     El escalon de emergencia ademas queda ARMADO hasta el final del acto en
     vez de dispararse una sola vez. Un aparato puede ir bien a los 1,30 s y
     hundirse a los 2,5 -- otra pestana que despierta, una foto que termina de
     decodificarse -- y antes de esto nadie lo recogia. */
  var T_DECIDE = 1.30;

  function vigilar(ahora, t) {
    if (ultimoMs) {
      ventana.push(ahora - ultimoMs);
      if (ventana.length > 20) ventana.shift();

      if (ventana.length === 20 && t > T_DECIDE && t < T_FORMA) {
        var suma = 0;
        for (var i = 0; i < 20; i++) suma += ventana[i];
        var media = suma / 20;

        /* EL GRANO SE GANA, NO SE REGALA. Empieza apagado y solo se enciende
           si este aparato en concreto va sobrado. Medido, cuesta la mitad del
           presupuesto en un aparato lento: 60 fps se quedaban en 30 con la CPU
           a 1/6. Es una textura que tiene que ser casi imperceptible, asi que
           pagar por ella medio ritmo de fotogramas es un mal trato. Y se mide
           el aparato, no se adivina por el modelo ni por el ancho de pantalla:
           dos telefonos iguales rinden distinto, y el mismo telefono rinde
           distinto con veinte pestanas abiertas. Entra con un fundido para que
           no se vea aparecer. */
        if (!granoDecidido) {
          granoDecidido = true;
          if (media <= 20) caja.classList.add('con-grano');
        }

        /* Primer escalon, por encima de 26 ms de media -- o sea, este aparato
           ya no sostiene 60 fps: se retira el brillo de la malla. Medido, es
           la pasada mas cara de toda la secuencia (un trazo de 3,6 px sobre el
           tercio delantero entero) y es lo unico que se puede quitar sin que
           la escena cambie de forma: la malla sigue con sus tres
           profundidades y su niebla, solo pierde el halo. */
        if (!brilloRecortado && media > 26) {
          brilloRecortado = true;
          CAL.halo = false;
        }

        /* Segundo escalon, la emergencia: por encima de 45 ms se cae todo lo
           accesorio y la mitad de las particulas. Prefiero una secuencia mas
           sobria a 60 fps que la completa a saltos. */
        if (!recortado && media > 45) {
          recortado = true;
          CAL.halo = false; CAL.enlaces = false; CAL.estelas = false; CAL.arcos = false;
          for (var j = ps.length - 1; j >= 0; j -= 2) ps.splice(j, 1);
          anillo = ps.filter(function (p) { return p.aro; });
        }
      }
    }
    ultimoMs = ahora;
  }

  function pintar(ahora) {
    raf = 0;
    if (muerto) return;
    if (t0 === null) t0 = ahora;
    var t = (ahora - t0) / 1000;
    // Paso de tiempo real, acotado. Sin acotar, volver de una pestana en
    // segundo plano mete un salto de varios segundos y los pulsos se
    // teletransportan; con el tope, como mucho dan un brinco de un tercio de
    // segundo. Y sin usarlo, los pulsos irian al doble de rapido a 60 fps que
    // a 30, que es justo lo que no puede pasar.
    var dtSeg = tPrevio === null ? 0.016 : Math.min(0.10, t - tPrevio);
    tPrevio = t;
    vigilar(ahora, t);

    ctx.clearRect(0, 0, W, H);

    /* El gimnasio va debajo de todo: es el SITIO donde ocurre la secuencia.
       Entra con el impacto -- antes hay solo un monitor y una linea, y meter
       una sala entera ahi le quitaria protagonismo al latido -- y se apaga con
       el colapso, cuando ya solo importa la marca. */
    moverCamara(t);
    if (MALLA) {
      // La sala tarda casi un segundo en abrirse del todo: es una transicion,
      // no un fundido, y da tiempo a verla llegar.
      var revGim = lim((t - T_IMPACTO - 0.05) / 0.95, 0, 1);
      var opGim = suave((t - T_IMPACTO - 0.05) / 0.40);
      if (t > T_MALLA) opGim *= 1 - suave((t - T_MALLA) / (T_FORMA - T_MALLA));
      gimnasio(t, opGim, revGim);
    }

    // Sacudida de camara en el impacto. Muy corta y muy pequena: el objetivo
    // es que se SIENTA el golpe, no que la pantalla se maree.
    var golpe = t - T_IMPACTO;
    var sac = 0;
    if (golpe > 0 && golpe < 0.22) sac = Math.sin(golpe / 0.22 * Math.PI * 3) * (1 - golpe / 0.22) * 5 * DPR;
    if (sac) { ctx.save(); ctx.translate(0, sac); }

    /* --- 1. Encendido: la linea base se despliega desde el centro --- */
    if (t < T_ENCIENDE) {
      var e = frena(t / T_ENCIENDE);
      var mitad = (W / 2) * e;
      ctx.strokeStyle = rgba(CIAN, 0.45 + 0.35 * e);
      ctx.lineWidth = 2 * DPR;
      ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(cx - mitad, yBase);
      ctx.lineTo(cx + mitad, yBase);
      ctx.stroke();
      // Los dos cabezales que abren la linea
      ctx.fillStyle = rgba('#eafcff', 0.9);
      ctx.beginPath(); ctx.arc(cx - mitad, yBase, 2.6 * DPR, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(cx + mitad, yBase, 2.6 * DPR, 0, Math.PI * 2); ctx.fill();
    }

    /* --- 2. El pulso --- */
    var avance = 0;
    if (t >= T_ENCIENDE) {
      avance = avanceEn((t - T_ENCIENDE) / (T_TRAZO - T_ENCIENDE));
      // El trazo se apaga mientras las particulas toman el relevo, para que
      // no haya un fotograma con la linea entera y las particulas encima.
      var apaga = t > T_IMPACTO
        ? 1 - suave((t - T_IMPACTO) / 0.55)
        : 1;
      if (apaga > 0.01) {
        trazo(avance, apaga);
        if (avance < AV_MAX) cabezal(avance, apaga);
      }
    }

    /* --- 3. Impacto --- */
    if (golpe > 0) {
      var pkx = ptX(X_PICO), pky = ptY(X_PICO);

      // Destello blanco. Dura 140 ms: es el parpadeo del golpe.
      if (golpe < 0.14) {
        var fl = 1 - golpe / 0.14;
        var rf = Math.min(W, H) * 0.85;
        var gf = ctx.createRadialGradient(pkx, pky, 0, pkx, pky, rf);
        gf.addColorStop(0, rgba('#ffffff', 0.46 * fl));
        gf.addColorStop(0.35, rgba(CIAN, 0.17 * fl));
        gf.addColorStop(1, rgba(CIAN, 0));
        ctx.fillStyle = gf;
        ctx.fillRect(pkx - rf, pky - rf, rf * 2, rf * 2);
      }

      // Dos ondas de choque a velocidades distintas: una sola lee como un
      // circulo, dos leen como una detonacion.
      var ondas = [[0, 0.85, CIAN, 3.0], [0.07, 0.62, ROSA, 2.0]];
      for (var o = 0; o < ondas.length; o++) {
        var od = ondas[o], ed = (golpe - od[0]) / od[1];
        if (ed > 0 && ed < 1) {
          var rr2 = frena(ed) * Math.min(W, H) * 0.92;
          ctx.beginPath();
          ctx.arc(pkx, pky, rr2, 0, Math.PI * 2);
          ctx.strokeStyle = rgba(od[2], (1 - ed) * (1 - ed) * 0.75);
          ctx.lineWidth = od[3] * DPR * (1 - ed * 0.6);
          ctx.stroke();
        }
      }

      // Arcos de carga: la energia del latido subiendo al emblema.
      if (CAL.arcos && golpe > 0.05 && golpe < 0.42) {
        var sello = Math.floor(golpe / 0.055);
        if (sello !== arcoSello) { arcoSello = sello; generarArcos(pkx, pky); }
        var oa = Math.sin(lim((golpe - 0.05) / 0.37, 0, 1) * Math.PI) * 0.85;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        for (var a = 0; a < arcos.length; a++) {
          var pts = arcos[a];
          ctx.beginPath();
          ctx.moveTo(pts[0], pts[1]);
          for (var q = 2; q < pts.length; q += 2) ctx.lineTo(pts[q], pts[q + 1]);
          ctx.strokeStyle = rgba(a % 2 ? ROSA : CIAN, 0.30 * oa);
          ctx.lineWidth = 4 * DPR;
          ctx.stroke();
          ctx.strokeStyle = rgba('#eafcff', 0.80 * oa);
          ctx.lineWidth = 1.2 * DPR;
          ctx.stroke();
        }
      }
    }

    /* --- 4. Las particulas: estallido, malla y formacion --- */
    if (t > T_IMPACTO) {
      var dur = (MALLA ? T_ESFERA : T_FORMA) - T_IMPACTO;
      var fGlobal = lim((t - T_IMPACTO) / (T_FORMA - T_IMPACTO), 0, 1);

      // La esfera empieza a girar en cuanto las particulas salen hacia ella,
      // no cuando llegan: asi aterrizan sobre algo que ya se mueve y el acto
      // no arranca con un fotograma quieto.
      var opMalla = 0;
      if (MALLA) {
        var giro = (t - T_IMPACTO) * 0.62;
        // Latido, y antes del colapso una anticipacion: la esfera se estira un
        // punto justo antes de encogerse. Sin ella el colapso arranca de golpe
        // y se nota que es una interpolacion; con ella parece que toma impulso.
        var escala = 1 + pulsoCorazon(t) * 0.035;
        if (t > T_MALLA - 0.28) {
          var ant = lim((t - (T_MALLA - 0.28)) / 0.28, 0, 1);
          escala += Math.sin(ant * Math.PI) * 0.075;
        }
        proyectar(giro, escala);
        // Entra mientras las particulas viajan y se va con el colapso.
        // Entra PRONTO, mientras las particulas todavia viajan hacia ella: asi
        // vuelan hacia una estructura que ya esta ahi, en lugar de aterrizar
        // en el vacio y encenderse despues. Medido, con la entrada tardia el
        // centro se quedaba al 5,7 % de pixeles encendidos a 1,1 s; con esta,
        // no baja del 10 % en ningun momento del acto.
        opMalla = suave((t - T_IMPACTO - 0.15) / 0.50);
        if (t > T_MALLA) opMalla *= 1 - suave((t - T_MALLA) / (T_FORMA - T_MALLA) * 1.15);
        dibujarMalla(opMalla);
        dibujarPulsos(dtSeg, opMalla);
      }
      for (var gz = 0; gz < grupos.length; gz++) {
        var Gz = grupos[gz];
        Gz.op = 0; Gz.n = 0; Gz.puntos.length = 0;
        Gz.estelas[0].length = 0; Gz.estelas[1].length = 0;
      }

      for (var k = 0; k < ps.length; k++) {
        var p = ps[k];
        var tp = t - T_IMPACTO - p.retardo;
        if (tp < 0) continue;
        var f = lim(tp / dur, 0, 1);

        p.ax = p.x; p.ay = p.y;

        // El destino de cada acto. La particula k ES el nodo k de la malla,
        // asi que el objetivo de la esfera sale de la proyeccion de ese nodo
        // y el morfismo es una interpolacion, no una sustitucion.
        var enEsfera = MALLA && t > T_IMPACTO;
        var objX, objY, objR = p.r;

        if (enEsfera && t < T_MALLA) {
          objX = proyX[k]; objY = proyY[k];
          objR = p.r * (0.55 + 0.75 * proyK[k]);   // niebla: lejos, mas pequeno
          // Especular: los nodos del cuadrante superior izquierdo reciben mas
          // luz. Sin esto la esfera es una nube de puntos planos; con esto tiene
          // volumen, que es lo que se pedia por "realismo". Cuesta una resta.
          var lx = (objX - cx) / (R_ESF || 1), ly = (objY - cy) / (R_ESF || 1);
          var luzN = lim(0.62 - lx * 0.42 - ly * 0.42, 0, 1.35);
          objR *= 0.72 + luzN * 0.62;
        } else if (enEsfera) {
          // COLAPSO. El anillo es la esfera aplastada, asi que esto no es un
          // efecto nuevo: es la misma interpolacion tirando hacia el aro.
          var gc = frenaMas(lim((t - T_MALLA) / (T_FORMA - T_MALLA), 0, 1));
          objX = proyX[k] + (p.dx - proyX[k]) * gc;
          objY = proyY[k] + (p.dy - proyY[k]) * gc;
          objR = p.r * (0.55 + 0.75 * proyK[k]) * (1 - gc) + p.r * gc;
        } else {
          objX = p.dx; objY = p.dy;
        }

        if (f < 1) {
          // El estallido empuja hacia fuera y la formacion tira hacia el
          // destino. Mezclar las dos da la sensacion de explosion que se
          // reordena, en vez de dos movimientos pegados uno tras otro.
          var salida = frena(lim(tp / 0.30, 0, 1));
          // El origen se vuelve a calcular con la camara de ESTE fotograma,
          // asi que el estallido sale siempre del trazo que se esta viendo.
          var oxc = ptX(p.txw) + p.jx, oyc = ptY(p.txw) + p.jy;
          var ex = oxc + p.vx * salida * 7;
          var ey = oyc + p.vy * salida * 7;
          var g2 = frenaMas(f);
          // Un poco de giro al entrar: caer en linea recta al sitio parece
          // un iman; entrar en espiral parece que se estan colocando.
          var giro2 = (1 - g2) * 0.9;
          var dx2 = objX - cx, dy2 = objY - cy;
          var cs = Math.cos(giro2), sn = Math.sin(giro2);
          var tx2 = cx + dx2 * cs - dy2 * sn;
          var ty2 = cy + dx2 * sn + dy2 * cs;
          p.x = ex + (tx2 - ex) * g2;
          p.y = ey + (ty2 - ey) * g2;
        } else if (enEsfera && t < T_FORMA) {
          // Ya en la malla: la particula ES el nodo, sin muelle de por medio.
          p.x = objX; p.y = objY;
        } else {
          // Estado final: iman vivo. Muelle hacia su sitio, respiracion propia
          // y empuje del puntero.
          if (!p.listo) { p.listo = true; p.px = 0; p.py = 0; }
          var resp = Math.sin(t * 1.7 + p.fase) * 0.5 * DPR;
          var mx = cx + Math.cos(p.ang) * (p.rr + resp);
          var my = cy + Math.sin(p.ang) * (p.rr + resp);
          p.px += (mx - p.x) * 0.006;
          p.py += (my - p.y) * 0.006;
          if (puntero.activo) {
            var ddx = p.x - puntero.x, ddy = p.y - puntero.y;
            var d2 = ddx * ddx + ddy * ddy;
            var alcance = (150 * DPR) * (150 * DPR);
            if (d2 < alcance && d2 > 1) {
              var fu = (1 - d2 / alcance) * 2.2;
              var d = Math.sqrt(d2);
              p.px -= (ddx / d) * fu;
              p.py -= (ddy / d) * fu;
            }
          }
          p.px *= 0.9; p.py *= 0.9;
          p.x += p.px; p.y += p.py;
        }

        // El dibujo NO va aqui. Con 168 particulas, una llamada de dibujo por
        // particula (mas su estela) son mas de trescientas por fotograma, y en
        // un movil de gama media eso era el fotograma de 83 ms justo en el
        // impacto. Se apunta en su grupo y se dibujan todas juntas despues.
        var grupo = grupos[p.g];
        grupo.op += f < 1 ? 0.45 + 0.55 * f : 1;
        grupo.n++;
        grupo.puntos.push(p.x, p.y, objR);
        if (CAL.estelas && f < 0.85) {
          var vdx = p.x - p.ax, vdy = p.y - p.ay;
          var v2 = vdx * vdx + vdy * vdy;
          if (v2 > (1.4 * DPR) * (1.4 * DPR)) {
            var vlen = Math.sqrt(v2);
            var largo = Math.min(vlen * 2.2, 16 * DPR) / vlen;
            grupo.estelas[p.grueso].push(p.x - vdx * largo, p.y - vdy * largo, p.x, p.y);
          }
        }
      }

      // Un solo trazado por color (y por grosor en las estelas): nueve
      // llamadas de dibujo en lugar de trescientas y pico, con exactamente el
      // mismo resultado en pantalla.
      ctx.lineCap = 'round';
      for (var gi = 0; gi < grupos.length; gi++) {
        var G = grupos[gi];
        if (!G.n) continue;
        var opm = G.op / G.n;
        for (var gg = 0; gg < 2; gg++) {
          var es = G.estelas[gg];
          if (!es.length) continue;
          ctx.beginPath();
          for (var q = 0; q < es.length; q += 4) { ctx.moveTo(es[q], es[q + 1]); ctx.lineTo(es[q + 2], es[q + 3]); }
          ctx.strokeStyle = rgba(G.c, 0.42 * opm);
          ctx.lineWidth = (gg ? 2.1 : 1.2) * DPR;
          ctx.stroke();
        }
        var pt = G.puntos;
        ctx.beginPath();
        for (var w = 0; w < pt.length; w += 3) {
          ctx.moveTo(pt[w] + pt[w + 2], pt[w + 1]);
          ctx.arc(pt[w], pt[w + 1], pt[w + 2], 0, Math.PI * 2);
        }
        ctx.fillStyle = rgba(G.c, 0.92 * opm);
        ctx.fill();
      }

      // Nucleo cargandose. Rellena el hueco entre el trazo que se apaga y el
      // emblema que todavia no ha entrado, y hace de ancla visual para que las
      // particulas parezcan atraidas por algo y no vagando.
      var carga = suave(lim((t - T_IMPACTO - 0.18) / 0.85, 0, 1));
      if (MALLA && t < T_MALLA) carga *= 0.45;   // la malla manda, el nucleo acompana
      if (carga > 0.01) {
        var lat = 1 + Math.sin(t * 5.5) * 0.05 * (1 - carga);
        var gr = radio * (0.30 + 0.72 * carga) * lat;
        var gn = ctx.createRadialGradient(cx + camDX, cy + camDY, 0, cx + camDX, cy + camDY, gr);
        gn.addColorStop(0, rgba('#ffffff', 0.20 * carga));
        gn.addColorStop(0.30, rgba(CIAN, 0.16 * carga));
        gn.addColorStop(0.70, rgba('#7b2fff', 0.09 * carga));
        gn.addColorStop(1, rgba(CIAN, 0));
        ctx.fillStyle = gn;
        ctx.beginPath();
        ctx.arc(cx + camDX, cy + camDY, gr, 0, Math.PI * 2);
        ctx.fill();
      }

      /* Se retiraron dos adornos de aqui: los enlaces entre particulas vecinas
         del anillo y el barrido tipo radar. Los dos nacieron cuando el anillo
         era el unico acto y habia que darle algo que mirar. Con la malla
         delante sobran: se pisaban con ella, y en el colapso competian con el
         logotipo justo cuando la mirada tiene que ir a la marca. Menos cosas y
         cada una con su porque. */
    }

    if (sac) ctx.restore();

    // Las frases. Solo se toca el DOM cuando CAMBIA la que toca: escribir un
    // atributo sesenta veces por segundo para poner el mismo valor invalida
    // estilo en cada fotograma por nada.
    if (MALLA && cajaFrases) {
      var cual = faseFrase(t);
      if (cual !== fraseActual) {
        fraseActual = cual;
        if (cual < 0) cajaFrases.removeAttribute('data-frase');
        else {
          var idx = cual % nFrases;
          cajaFrases.setAttribute('data-frase', String(idx));
          // La marca de "ya se vio" NO se quita nunca. Sin ella, al salir la
          // frase las palabras volvian a caer dentro de su mascara, cada una
          // con su retardo, y durante la despedida se veia el texto
          // desmontandose a trozos. Cada frase se muestra una sola vez, asi
          // que una vez revelada se queda arriba y de la salida se encarga
          // solo la opacidad.
          var el = cajaFrases.children[idx];
          if (el) el.classList.add('vista');
        }
      }
    }

    // DOS puertas, y esto importa. La de arriba abre la tienda: el boton de
    // entrar aparece ANTES de que la secuencia termine, para que nadie tenga
    // que esperar a ver el final. La de abajo marca el final de verdad y trae
    // el titulo y el eslogan.
    //
    // Las dos se ponen desde el bucle y no con temporizadores aparte: si la
    // pestana estuvo en segundo plano, el reloj de la secuencia y el del
    // texto siguen siendo el mismo. Y es UNA sola fuente de verdad, en vez de
    // retardos copiados a mano en varias reglas de CSS que se descuadran en
    // cuanto se toca cualquiera.
    if (!puerta && t >= T_PUERTA) { puerta = true; caja.classList.add('intro-puerta'); }
    if (!listo && t >= T_FORMA) { listo = true; caja.classList.add('intro-lista'); }

    /* APERTURA EN NEGRO. Ninguna pelicula empieza con imagen: empieza con
       negro. Doscientos milisegundos de negro absoluto y despues se levanta.
       Va al FINAL del pintado, encima de todo lo demas, porque es un telon. */
    if (t < 0.34) {
      ctx.fillStyle = 'rgba(0,0,0,' + (1 - suave((t - 0.10) / 0.24)).toFixed(3) + ')';
      ctx.fillRect(0, 0, W, H);
    }


    pedir();
  }

  function pedir() { if (!muerto && !raf) raf = requestAnimationFrame(pintar); }

  /* ---------- estado final, sin secuencia ---------- */
  function estatico() {
    // El mismo fotograma final que ve todo el mundo. Antes pintaba ademas los
    // enlaces entre particulas vecinas, que se retiraron de la secuencia: quien
    // pide menos movimiento no tiene por que ver una version distinta.
    ctx.clearRect(0, 0, W, H);
    for (var k = 0; k < ps.length; k++) {
      var p = ps[k];
      ctx.beginPath();
      ctx.arc(p.dx, p.dy, p.r, 0, Math.PI * 2);
      ctx.fillStyle = rgba(p.c, 0.9);
      ctx.fill();
    }
  }

  /* ---------- arranque y limpieza ---------- */
  function soltar() {
    if (muerto) return;
    muerto = true;
    if (raf) { cancelAnimationFrame(raf); raf = 0; }
    caja.removeEventListener('pointermove', mover);
    caja.removeEventListener('pointerleave', salir);
    window.removeEventListener('resize', alRedimensionar);
    try { ctx.clearRect(0, 0, W, H); } catch (e5) {}
  }

  function alRedimensionar() {
    medir();
    sembrar();
    if (reduce) estatico();
  }

  medir();
  sembrar();

  if (reduce) {
    estatico();
    caja.classList.add('intro-puerta');
    caja.classList.add('intro-lista');
  } else {
    caja.addEventListener('pointermove', mover);
    caja.addEventListener('pointerleave', salir);
    window.addEventListener('resize', alRedimensionar);
    pedir();
    // Red de seguridad: si el bucle no llegase a correr (pestana en segundo
    // plano desde el principio, o un fallo raro), el boton de entrar tiene que
    // aparecer igualmente. Nunca se puede quedar la tienda sin puerta.
    setTimeout(function () {
      if (!puerta) { puerta = true; caja.classList.add('intro-puerta'); }
      if (!listo) { listo = true; caja.classList.add('intro-lista'); }
    }, T_FORMA * 1000 + 900);
  }

  // El cierre lo decide base.js; aqui solo hay que enterarse para soltar.
  caja.addEventListener('villu:intro-cerrada', soltar);
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { if (raf) { cancelAnimationFrame(raf); raf = 0; } }
    else if (!muerto && !reduce) pedir();
  });
})();
