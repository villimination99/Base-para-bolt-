/* Las cifras del banner suben contando al cargar. Tres decisiones:
   1. El numero final ya esta escrito en el HTML, asi que si este script no
      llegara a ejecutarse la cifra se ve igual. La animacion adorna, no
      informa.
   2. Se anima con requestAnimationFrame y una curva que frena al final, que
      es como se lee natural una cuenta.
   3. Con "menos movimiento" activado no cuenta: aparece el numero y ya. */
(function () {
  var quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cifras = document.querySelectorAll('#hero-section [data-cuenta]');
  if (!cifras.length || quieto) return;
  var DUR = 1100, t0 = null;
  cifras.forEach(function (e) { e.textContent = '0'; });
  function paso(t) {
    if (t0 === null) t0 = t;
    var u = Math.min(1, (t - t0) / DUR);
    var k = 1 - Math.pow(1 - u, 3);          // frena al llegar
    cifras.forEach(function (e) {
      e.textContent = Math.round(parseFloat(e.getAttribute('data-cuenta')) * k);
    });
    if (u < 1) requestAnimationFrame(paso);
  }
  requestAnimationFrame(function () { requestAnimationFrame(paso); });
})();

/* Diagnóstico VILLUMINATIONS: identifica el origen real de cualquier fallo. */
(function () {
  var TAG = '[VILL]';
  window.addEventListener('error', function (e) {
    if (e && e.target && e.target !== window && (e.target.src || e.target.href)) {
      if (e.target.className && String(e.target.className).indexOf('exgif') !== -1) return;
      console.warn(TAG + ' recurso externo no cargó:', e.target.src || e.target.href,
        '— la página sigue funcionando sin él.');
      return;
    }
    var m = e && e.message ? e.message : '';
    if (/Script error/i.test(m) && !e.filename) {
      console.warn(TAG + ' "Script error." = un script de otro dominio falló y el navegador ' +
        'oculta el detalle por CORS. No proviene del código de esta página.');
      return;
    }
    console.error(TAG + ' error:', m, '@', (e.filename || '?') + ':' + (e.lineno || 0) + ':' + (e.colno || 0),
      (e.error && e.error.stack) ? '\n' + e.error.stack : '');
  }, true);
  window.addEventListener('unhandledrejection', function (e) {
    var r = e && e.reason;
    console.warn(TAG + ' promesa rechazada:', (r && (r.message || r.name)) || r || 'desconocida',
      (r && r.stack) ? '\n' + r.stack : '');
  });
})();

(function() {
  'use strict';

  /* ===== TOAST ===== */
  function showToast(msg) {
    var t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._hide);
    t._hide = setTimeout(function() { t.classList.remove('show'); }, 2500);
  }
  window.showToast = showToast;

  /* ===== MODAL GENÉRICO ===== */
  function openModal(html) {
    var overlay = document.getElementById('modal-overlay') || (function() {
      var d = document.createElement('div');
      d.id = 'modal-overlay';
      d.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.75);z-index:1200;display:none;align-items:center;justify-content:center;padding:16px;';
      d.innerHTML = '<div style="background:#1a1a28;border:1px solid #2a2a3a;border-radius:20px;max-width:480px;width:100%;max-height:85vh;overflow-y:auto;padding:24px;position:relative;"><button class="modal-close" style="position:absolute;top:14px;right:16px;background:none;border:none;color:#888899;font-size:1.3rem;cursor:pointer;font-family:inherit;">✕</button><div id="modal-content"></div></div>';
      document.body.appendChild(d);
      d.querySelector('.modal-close').addEventListener('click', function() { d.style.display = 'none'; });
      d.addEventListener('click', function(e) { if (e.target === this) this.style.display = 'none'; });
      return d;
    })();
    document.getElementById('modal-content').innerHTML = html;
    if (window.__modalHook) { try { window.__modalHook(document.getElementById('modal-content')); } catch(e) {} window.__modalHook = null; }
    overlay.style.display = 'flex';
  }
  window.closeModal = function() {
    var ov = document.getElementById('modal-overlay');
    if (ov) ov.style.display = 'none';
  };

  /* ===== PERFIL ===== */
  var profileModal = document.getElementById('profile-modal');
  var profileInfo = document.getElementById('profile-info');
  var profileForm = document.getElementById('profile-form');
  var currentUser = null;

  function getWeight() { return (currentUser && currentUser.weight) ? Number(currentUser.weight) : 75; }
  window.getUserWeight = getWeight;

  function loadUser() {
    try {
      var data = localStorage.getItem('vill_user');
      if (data) { currentUser = JSON.parse(data); return true; }
    } catch(e) {}
    return false;
  }
  function saveUser(user) {
    currentUser = user;
    try { localStorage.setItem('vill_user', JSON.stringify(user)); } catch(e) {}
    updateProfileUI();
    if (window.refreshCalories) window.refreshCalories();
  }
  function updateProfileUI() {
    if (currentUser) {
      profileForm.style.display = 'none';
      profileInfo.style.display = 'block';
      document.getElementById('profile-user-email').textContent = currentUser.email || '-';
      document.getElementById('profile-user-weight').textContent = currentUser.weight || '-';
      document.getElementById('profile-user-cal').textContent = currentUser.dailyCal || '-';
    } else {
      profileForm.style.display = 'block';
      profileInfo.style.display = 'none';
    }
  }
  document.getElementById('profile-btn').addEventListener('click', function() {
    loadUser(); updateProfileUI(); profileModal.classList.add('open');
  });
  document.getElementById('profile-close').addEventListener('click', function() { profileModal.classList.remove('open'); });
  profileModal.addEventListener('click', function(e) { if (e.target === this) this.classList.remove('open'); });

  /* ===================================================================
     LA CONTRASENA NO SE GUARDA. NUNCA.

     Antes esta pagina hacia exactamente esto:

         allUsers[email] = { password: pass, weight: w, ... };
         localStorage.setItem('vill_users', JSON.stringify(allUsers));

     o sea, la contrasena TAL CUAL, en texto plano, en el almacen del
     navegador. Y eso importa aunque este perfil sea local y no haya
     servidor detras, por una razon muy concreta: la gente reutiliza
     contrasenas. La que alguien escriba aqui es, con mucha probabilidad,
     la de su correo. En localStorage la puede leer cualquier script que
     corra en este dominio -- una app de Shopify, una etiqueta de
     analitica, un pixel de publicidad, una extension del navegador -- y
     tambien queda en las copias de seguridad del perfil. Se estaba
     recogiendo un riesgo real a cambio de una seguridad que no existia.

     Ahora se guarda una HUELLA: sal aleatoria por usuario y SHA-256 con
     mil vueltas. De ahi no se saca la contrasena. Las que ya estuvieran
     guardadas en claro se convierten al abrir la pagina y se borran.

     Aun asi, y con todas las letras: esto NO es una cuenta. Es un perfil
     que vive en este navegador, y cualquiera con acceso al aparato entra
     borrando una clave del almacen. Para cuentas de verdad estan las de
     cliente de Shopify, que ya tiene la tienda.
     =================================================================== */
  var SUB = (window.crypto && window.crypto.subtle) ? window.crypto.subtle : null;
  function sal() {
    var a = new Uint8Array(16);
    if (window.crypto && window.crypto.getRandomValues) window.crypto.getRandomValues(a);
    else for (var i = 0; i < 16; i++) a[i] = Math.floor(Math.random() * 256);
    return Array.prototype.map.call(a, function(b) { return ('0' + b.toString(16)).slice(-2); }).join('');
  }
  function hex(buf) {
    return Array.prototype.map.call(new Uint8Array(buf), function(b) { return ('0' + b.toString(16)).slice(-2); }).join('');
  }
  /* Mil vueltas de SHA-256. No es un KDF de manual, pero es lo que hay sin
     dependencias, y convierte un repaso de diccionario instantaneo en uno
     mil veces mas caro. Si el navegador no trae WebCrypto -- solo pasa
     fuera de HTTPS -- se degrada a una huella simple: peor, pero sigue sin
     ser la contrasena. */
  function huella(pass, s) {
    if (!SUB) {
      var x = 0, t = s + '|' + pass;
      for (var i = 0; i < t.length; i++) { x = ((x << 5) - x + t.charCodeAt(i)) | 0; }
      return Promise.resolve('sinsubtle:' + (x >>> 0).toString(16));
    }
    var enc = new TextEncoder();
    var p = SUB.digest('SHA-256', enc.encode(s + '|' + pass));
    for (var k = 0; k < 999; k++) {
      p = p.then(function(b) { return SUB.digest('SHA-256', b); });
    }
    return p.then(hex);
  }
  function leerUsuarios() {
    try { return JSON.parse(localStorage.getItem('vill_users') || '{}'); } catch(e) { return {}; }
  }
  function guardarUsuarios(u) {
    try { localStorage.setItem('vill_users', JSON.stringify(u)); } catch(e) {}
  }
  /* Migracion: si quedaba alguna contrasena en claro de la version anterior,
     se convierte a huella y se borra el texto. Se hace al cargar y sin pedir
     nada al visitante. */
  (function migrar() {
    var u = leerUsuarios(), pend = Object.keys(u).filter(function(k) { return u[k] && typeof u[k].password === 'string'; });
    if (!pend.length) return;
    Promise.all(pend.map(function(k) {
      var s = sal();
      return huella(u[k].password, s).then(function(hh) { u[k].salt = s; u[k].hash = hh; delete u[k].password; });
    })).then(function() { guardarUsuarios(u); });
  })();

  document.getElementById('register-btn').addEventListener('click', function() {
    var email = document.getElementById('login-email').value.trim();
    var pass = document.getElementById('login-password').value;
    var w = Number(document.getElementById('login-weight').value) || 75;
    if (!email || !pass) { showToast(T('t.mail', 'Completa email y contraseña')); return; }
    var allUsers = leerUsuarios();
    if (allUsers[email]) { showToast(T('t.exists', 'El usuario ya existe. Inicia sesión.')); return; }
    var s = sal();
    huella(pass, s).then(function(hh) {
      allUsers[email] = { salt: s, hash: hh, weight: w, dailyCal: 2200 };
      guardarUsuarios(allUsers);
      saveUser({ email: email, weight: w, dailyCal: 2200 });
      showToast(T('t.reg', '✓ Registro exitoso. Bienvenido'));
      profileModal.classList.remove('open');
      document.getElementById('login-password').value = '';
    });
  });
  document.getElementById('login-btn').addEventListener('click', function() {
    var email = document.getElementById('login-email').value.trim();
    var pass = document.getElementById('login-password').value;
    if (!email || !pass) { showToast(T('t.mail', 'Completa email y contraseña')); return; }
    var allUsers = leerUsuarios();
    var u = allUsers[email];
    if (!u) { showToast(T('t.nouser', 'Usuario no encontrado. Regístrate.')); return; }
    huella(pass, u.salt || '').then(function(hh) {
      if (hh !== u.hash) { showToast(T('t.badpw', 'Contraseña incorrecta')); return; }
      var w = Number(document.getElementById('login-weight').value) || u.weight || 75;
      u.weight = w;
      guardarUsuarios(allUsers);
      saveUser({ email: email, weight: w, dailyCal: u.dailyCal || 2200 });
      showToast(T('t.login', '✓ Sesión iniciada'));
      profileModal.classList.remove('open');
      document.getElementById('login-password').value = '';
    });
  });
  document.getElementById('logout-btn').addEventListener('click', function() {
    try { localStorage.removeItem('vill_user'); } catch(e) {}
    currentUser = null; updateProfileUI();
    if (window.refreshCalories) window.refreshCalories();
    showToast(T('t.logout', 'Sesión cerrada')); profileModal.classList.remove('open');
  });
  loadUser(); updateProfileUI();

  /* =====================================================================
     MUSCLE MAP 3D — el modelo se esculpe en el módulo ES al final
     de la página (SDF + marching cubes). Aquí solo cableamos botones
     y un watchdog por si el módulo no puede cargar.
     ===================================================================== */
  window.__mm3dReady = false;
  window.__mm3dStarted = false;
  document.querySelectorAll('.muscle-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var m = this.dataset.muscle;
      if (window.selectMuscle3D) {
        window.selectMuscle3D(m, true);
      } else {
        document.querySelectorAll('.muscle-btn').forEach(function(b) { b.classList.remove('active'); });
        this.classList.add('active');
        showMuscleModal(m);
      }
    });
  });
  /* El vigilante del mapa 3D.

     Antes esto era un setTimeout de 15 segundos desde que arranca el hub, y
     estaba mal por los dos lados a la vez:

       - Demasiado tarde cuando el modulo NO va a ejecutarse nunca -- el
         navegador no entiende modulos, el archivo dio 404, la sintaxis le
         sento mal. En esos casos ya se sabe en el primer segundo, y el
         visitante se quedaba un cuarto de minuto mirando "Esculpiendo
         anatomia 3D..." para que al final le dijeran que no hay mapa.
       - Y a la vez demasiado pronto con una conexion mala: son medio mega,
         y a 3G lenta pueden tardar mas de quince segundos en bajar. El
         respaldo saltaba encima de un modulo que venia de camino.

     El reloj no era la senal correcta. La senal correcta es el evento load:
     no se dispara hasta que los scripts diferidos y los modulos se han
     bajado y ejecutado. Si cuando llega load el modulo no ha arrancado, es
     que no va a arrancar -- da igual si tardo dos segundos o cuarenta.

     El margen de 600 ms de despues es para el propio modulo, que entre que
     empieza y marca la bandera crea el renderizador. Y el caso de que load
     ya haya pasado cuando esto se ejecuta esta cubierto mirando
     document.readyState, porque a un evento que ya ocurrio no se llega
     tarde: no se llega. */
  function vigilarMapa3D() {
    setTimeout(function() {
      if (window.__mm3dStarted) return;
      var c = document.getElementById('muscle-canvas');
      var l = document.getElementById('mm-loading');
      if (c) c.style.display = 'none';
      if (l) l.style.display = 'none';
      var f = document.getElementById('mm-fallback');
      if (f) f.style.display = 'block';
    }, 600);
  }
  if (document.readyState === 'complete') vigilarMapa3D();
  else window.addEventListener('load', vigilarMapa3D);

  /* ===== MUSCLE MODAL ===== */
  var ZONETAG = { Pecho: 'Pecho', Espalda: 'Espalda', Hombros: 'Hombros', Biceps: 'Biceps', Triceps: 'Triceps', Abdominales: 'Core', Cuadriceps: 'Piernas', Gluteos: 'Gluteos', Gemelos: 'Piernas' };
  var ZONELABEL = { Pecho: 'Pecho', Espalda: 'Espalda', Hombros: 'Hombros', Biceps: 'Bíceps', Triceps: 'Tríceps', Abdominales: 'Abdominales', Cuadriceps: 'Cuádriceps', Gluteos: 'Glúteos', Gemelos: 'Gemelos' };
  function zoneExercises(name) {
    var list;
    if (name === 'Gemelos') {
      list = EXERCISES.filter(function(e) { return /gemelo|pantorrilla|comba|cuerda|salto/i.test(e.name); });
      EXERCISES.forEach(function(e) {
        if (list.length < 4 && e.tags.indexOf('Piernas') !== -1 && list.indexOf(e) === -1) list.push(e);
      });
    } else {
      var tag = ZONETAG[name];
      list = EXERCISES.filter(function(e) { return e.tags.indexOf(tag) !== -1; });
    }
    return list.slice(0, 4);
  }
  window.addFromMap = function(id, zone) {
    window.addToRoutine(id);
    window.showMuscleModal(zone);
  };
  window.removeFromMap = function(id, zone) {
    window.removeFromRoutine(id);
    window.showMuscleModal(zone);
  };
  window.showMuscleModal = function(name) {
    var label = ZONELABEL[name];
    if (!label) return;
    var exs = zoneExercises(name);
    var html = '<div style="font-size:1.2rem;font-weight:800;background:linear-gradient(135deg,#FF2A6D,#05D9E8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:6px;">' + label + '</div>' +
      '<div style="color:#888899;margin-bottom:14px;">Ejercicios de la librería para este músculo — tócalos para sumarlos a tu rutina</div>' +
      exs.map(function(ex) {
        var inR = routineIds.indexOf(ex.id) !== -1;
        var btn = inR
          ? '<button class="mm-ex-add added" onclick="' + "removeFromMap('" + ex.id + "','" + name + "')" + '" title="Quitar de la rutina">✓</button>'
          : '<button class="mm-ex-add" onclick="' + "addFromMap('" + ex.id + "','" + name + "')" + '" title="Agregar a la rutina">＋</button>';
        return '<div class="mm-ex-row"><div><div class="mm-ex-name" style="cursor:pointer" title="Ver técnica correcta" onclick="event.stopPropagation();showExModal(\'' + ex.id + '\')">' + ex.icon + ' ' + TX(ex.name) + ' <span style="font-size:0.72rem;opacity:0.8">📖</span></div><div class="mm-ex-meta">' + ex.sets + ' · ≈' + exKcal(ex) + ' kcal · ' + TX(ex.diff) + '</div></div>' + btn + '</div>';
      }).join('') +
      '<div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap">' +
        '<button class="btn btn-primary" onclick="closeModal();document.getElementById(\'planner\').scrollIntoView({behavior:\'smooth\'})">Ir a mi rutina ↓</button>' +
        '<button class="btn btn-outline" onclick="closeModal()">Seguir explorando</button>' +
      '</div>';
    openModal(html);
  };

  /* =====================================================================
     ENTRENAMIENTO — BASE DE DATOS ÚNICA + kcal REALISTAS (MET)
     kcal por sesión = MET × peso(kg) × minutos/60
     ===================================================================== */
  var EXERCISES = [
    { id: 'squat',    icon: '🏋️', name: 'Sentadilla con barra', sets: '5x5',   tags: ['Piernas'],          diff: 'Intermedio',   met: 6.0, min: 12 },
    { id: 'legpress', icon: '🦵', name: 'Prensa de piernas',    sets: '4x12',  tags: ['Piernas'],          diff: 'Principiante', met: 5.0, min: 10 },
    { id: 'lunge',    icon: '🚶', name: 'Zancadas',             sets: '3x12',  tags: ['Piernas', 'Gluteos'], diff: 'Principiante', met: 5.0, min: 9 },
    { id: 'legext',   icon: '🦵', name: 'Extensión cuádriceps', sets: '3x15',  tags: ['Piernas'],          diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'legcurl',  icon: '🦵', name: 'Curl femoral',         sets: '3x12',  tags: ['Piernas'],          diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'hipthrust',icon: '🍑', name: 'Hip thrust',           sets: '4x10',  tags: ['Gluteos'],          diff: 'Intermedio',   met: 5.0, min: 10 },
    { id: 'calf',     icon: '🦶', name: 'Elevación de gemelos', sets: '4x15',  tags: ['Piernas'],          diff: 'Principiante', met: 3.5, min: 7 },
    { id: 'bench',    icon: '💪', name: 'Press de banca',       sets: '4x10',  tags: ['Pecho'],            diff: 'Intermedio',   met: 5.0, min: 10 },
    { id: 'incline',  icon: '💪', name: 'Press inclinado',      sets: '4x8',   tags: ['Pecho'],            diff: 'Intermedio',   met: 5.0, min: 10 },
    { id: 'fly',      icon: '🦋', name: 'Aperturas mancuerna',  sets: '3x12',  tags: ['Pecho'],            diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'dips',     icon: '🤸', name: 'Fondos en paralelas',  sets: '3x10',  tags: ['Pecho', 'Triceps'], diff: 'Avanzado',     met: 7.0, min: 8 },
    { id: 'pullup',   icon: '🆙', name: 'Dominadas',            sets: '4x8',   tags: ['Espalda', 'Biceps'], diff: 'Avanzado',    met: 8.0, min: 8 },
    { id: 'row',      icon: '🚣', name: 'Remo con barra',       sets: '4x10',  tags: ['Espalda'],          diff: 'Intermedio',   met: 6.0, min: 10 },
    { id: 'lat',      icon: '⬇️', name: 'Jalón al pecho',       sets: '3x12',  tags: ['Espalda'],          diff: 'Principiante', met: 5.0, min: 9 },
    { id: 'cablerow', icon: '🚣', name: 'Remo en polea baja',   sets: '3x12',  tags: ['Espalda'],          diff: 'Principiante', met: 5.0, min: 9 },
    { id: 'dead',     icon: '🏋️', name: 'Peso muerto',          sets: '4x6',   tags: ['Espalda', 'Piernas'], diff: 'Avanzado',   met: 6.0, min: 12 },
    { id: 'ohp',      icon: '🙌', name: 'Press militar',        sets: '4x8',   tags: ['Hombros'],          diff: 'Intermedio',   met: 5.0, min: 9 },
    { id: 'lateral',  icon: '↔️', name: 'Elevaciones laterales',sets: '4x15',  tags: ['Hombros'],          diff: 'Principiante', met: 3.5, min: 8 },
    { id: 'facepull', icon: '🪢', name: 'Face pull',            sets: '3x15',  tags: ['Hombros', 'Espalda'], diff: 'Principiante', met: 3.5, min: 7 },
    { id: 'curl',     icon: '💪', name: 'Curl de bíceps',       sets: '3x12',  tags: ['Biceps'],           diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'hammer',   icon: '🔨', name: 'Curl martillo',        sets: '3x12',  tags: ['Biceps'],           diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'tricep',   icon: '🦾', name: 'Extensión de tríceps', sets: '3x12',  tags: ['Triceps'],          diff: 'Principiante', met: 4.0, min: 8 },
    { id: 'plank',    icon: '🧱', name: 'Plancha',              sets: '3x60s', tags: ['Core'],             diff: 'Principiante', met: 3.3, min: 6 },
    { id: 'crunch',   icon: '🎯', name: 'Crunch abdominal',     sets: '4x20',  tags: ['Core'],             diff: 'Principiante', met: 3.8, min: 7 },
    { id: 'legraise', icon: '🦵', name: 'Elevación de piernas', sets: '3x15',  tags: ['Core'],             diff: 'Intermedio',   met: 3.8, min: 7 },
    { id: 'mclimber', icon: '⛰️', name: 'Mountain climbers',    sets: '3x30s', tags: ['Core', 'Cardio'],   diff: 'Intermedio',   met: 8.0, min: 5 },
    { id: 'burpee',   icon: '💥', name: 'Burpees',              sets: '3x12',  tags: ['Cardio'],           diff: 'Avanzado',     met: 8.0, min: 6 }
  ];
  function exKcal(ex) { return Math.round(ex.met * getWeight() * ex.min / 60); }
  function tagsPretty(tags) {
    var map = { Gluteos: 'Glúteos', Biceps: 'Bíceps', Triceps: 'Tríceps' };
    return tags.map(function(t) { return map[t] || t; }).join(', ');
  }

  var routineIds = [];
  try { var savedR = localStorage.getItem('vill_routine_v3'); if (savedR) routineIds = JSON.parse(savedR); } catch(e) {}

  var UNIT = (function() { try { return localStorage.getItem('vill_unit') || 'KG'; } catch(e) { return 'KG'; } })();
  var LB = 2.20462;
  function toDisplay(kg) { return UNIT === 'LB' ? Math.round(kg * LB * 10) / 10 : kg; }
  function toKg(v) { return UNIT === 'LB' ? v / LB : v; }
  window.getUnit = function() { return UNIT; };

  (function initUnitToggle() {
    var ut = document.getElementById('unit-toggle');
    if (!ut) return;
    ut.textContent = UNIT;
    ut.addEventListener('click', function() {
      UNIT = UNIT === 'KG' ? 'LB' : 'KG';
      try { localStorage.setItem('vill_unit', UNIT); } catch(e) {}
      this.textContent = UNIT;
      renderRoutine(); renderLibrary(); renderPRs();
      showToast(T('t.unit', 'Unidad') + ': ' + (UNIT === 'KG' ? T('t.kg', 'kilogramos') : T('t.lb', 'libras')));
    });
  })();
  function renderRoutine() {
    var list = document.getElementById('routine-list');
    var items = routineIds.map(function(id) { return EXERCISES.find(function(e) { return e.id === id; }); }).filter(Boolean);
    list.innerHTML = items.map(function(ex) {
      var lastW = WEIGHTS[ex.id] ? toDisplay(WEIGHTS[ex.id]) : '';
      var done = DONE_TODAY.indexOf(ex.id) !== -1;
      return '<div class="ex-item' + (done ? ' routine-done' : '') + '" data-id="' + ex.id + '"><div><div class="ex-name-t">' + (done ? '✓ ' : '') + TX(ex.name) + '</div><div class="ex-meta">' + ex.sets + ' · ≈' + exKcal(ex) + ' kcal</div></div><div class="ex-log"><input type="number" min="0" step="' + (UNIT === 'LB' ? '5' : '2.5') + '" class="w-input" id="w-' + ex.id + '" placeholder="' + UNIT.toLowerCase() + '" value="' + lastW + '"><button class="log-btn" title="Registrar serie" onclick="logSet(\'' + ex.id + '\')">✓</button><button class="ex-remove" onclick="removeFromRoutine(\'' + ex.id + '\')">✕</button></div></div>';
    }).join('') || '<p style="color:#888899;font-size:0.82rem;padding:8px 0">' + T('dyn.empty', 'Elige ejercicios en la galería de abajo ↓') + '</p>';
    var total = items.reduce(function(s, ex) { return s + exKcal(ex); }, 0);
    var totalMin = items.reduce(function(s, ex) { return s + ex.min; }, 0);
    document.getElementById('total-cal-value').textContent = '≈' + total;
    document.getElementById('cal-weight-note').textContent = T('dyn.basedon', 'Basado en') + ' ' + getWeight() + ' kg · ' + totalMin + ' ' + T('dyn.work', 'min de trabajo') + ' · ' + T('dyn.editweight', 'edita tu peso en el perfil');
  }
  window.addToRoutine = function(id) {
    if (routineIds.indexOf(id) === -1) {
      routineIds.push(id);
      renderRoutine(); renderLibrary();
      var ex = EXERCISES.find(function(e) { return e.id === id; });
      if (ex) showToast('✓ ' + TX(ex.name) + ' ' + T('dyn.added', 'agregado') + ' (≈' + exKcal(ex) + ' kcal)');
    }
  };
  window.removeFromRoutine = function(id) {
    routineIds = routineIds.filter(function(r) { return r !== id; });
    renderRoutine(); renderLibrary();
  };
  window.refreshCalories = function() { renderRoutine(); renderLibrary(); };

  /* =====================================================================
     SALUD EN CONJUNTO — registro de peso, niveles, PRs, panel diario, sueño
     ===================================================================== */
  function loadJSON(k, def) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : def; } catch(e) { return def; } }
  function saveJSON(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch(e) {} }
  function todayKey() {
    var d = new Date();
    return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
  }
  var STATS = loadJSON('vill_stats', { totalVolume: 0 });
  var DAYS = loadJSON('vill_days', {});
  var WEIGHTS = loadJSON('vill_weights', {});
  var DONE_STORE = loadJSON('vill_done', {});
  var DONE_TODAY = DONE_STORE[todayKey()] || [];
  var PRS = loadJSON('vill_prs', {});
  var CALGOAL = Number(loadJSON('vill_goal', 2200)) || 2200;
  window.getCalGoal = function() { return CALGOAL; };
  window.setCalGoal = function(v) {
    CALGOAL = Math.max(1200, Math.min(6000, Math.round(v)));
    saveJSON('vill_goal', CALGOAL);
    if (window.refreshCalGoalUI) window.refreshCalGoalUI();
    showToast('🎯 ' + T('t.goal', 'Meta diaria establecida') + ': ' + CALGOAL + ' kcal');
  };
  window.applyGoal = function(v) { window.setCalGoal(v); };
  window.openDietTab = function(term) {
    var tabs = document.querySelectorAll('.diet-tab');
    var target = null;
    tabs.forEach(function(t) {
      if (!target && (((t.dataset && t.dataset.plan) || '').toLowerCase().indexOf(term) !== -1 || t.textContent.toLowerCase().indexOf(term) !== -1)) target = t;
    });
    if (!target && tabs.length) target = tabs[0];
    if (target) target.click();
    var sec = document.getElementById('diet-plans');
    if (sec) sec.scrollIntoView({ behavior: 'smooth' });
  };

  /* ===== MENÚS SEMANALES COMPLETOS (Lun-Dom · rotación Mes A/B) ===== */
  var DIETWEEKS = {
    volumen: { note: 'Pre-cama opcional: caseína o yogur griego. Ajusta porciones a tu meta de la sección Objetivo.', weeks: [[
      ['Lun', 'Avena 80g + proteína + plátano + leche', 'Arroz 150g + pollo 200g + brócoli + EVOO', 'Yogur griego 200g + almendras 30g', 'Salmón 180g + batata 200g + ensalada'],
      ['Mar', 'Tortilla 3 huevos + tostada integral + fruta', 'Pasta 130g + atún 2 latas + tomate', 'Plátano + mantequilla de maní 20g', 'Pechuga 200g + arroz 120g + espinacas'],
      ['Mié', 'Avena 80g + fresas + nueces + miel', 'Arroz 150g + carne magra 180g + pimientos', 'Requesón 150g + fruta', 'Salmón 180g + quinoa 100g + aguacate'],
      ['Jue', 'Panqueques de avena (3) + huevo + plátano', 'Burrito bowl: arroz + ternera 180g + frijoles', 'Batido: leche + proteína + avena 40g', 'Pollo al horno 200g + papa 250g + verduras'],
      ['Vie', 'Yogur griego 250g + granola 60g + miel', 'Pasta 140g + pollo 180g + pesto ligero', 'Sándwich integral de pavo + queso', 'Merluza 200g + arroz 130g + brócoli'],
      ['Sáb', 'Huevos revueltos 3 + aguacate + pan integral', 'Arroz 160g + salmón teriyaki 180g', 'Fruta + puñado de nueces 30g', 'Pizza casera integral de pollo'],
      ['Dom', 'Avena nocturna + proteína + cacao', 'Lentejas guisadas 200g + arroz + huevo', 'Yogur + miel + almendras 25g', 'Ternera magra 180g + puré de batata']
    ], [
      ['Lun', 'Crema de arroz 90g + claras 4 + canela', 'Quinoa 150g + pavo 200g + calabacín', 'Batido de plátano + proteína + maní', 'Trucha 180g + papa 250g + espárragos'],
      ['Mar', 'Bagel integral + huevo + aguacate', 'Arroz 160g + tilapia 200g + verduras wok', 'Requesón 150g + piña', 'Pollo 200g + cuscús 120g + pimientos'],
      ['Mié', 'Avena 80g + manzana + canela + nueces', 'Fideos de arroz + ternera 180g + brócoli', 'Yogur griego + granola 50g', 'Salmón 180g + arroz 130g + ensalada'],
      ['Jue', 'Tortilla 3 huevos + champiñones + pan', 'Arroz 150g + pollo al curry 200g', 'Sándwich de atún integral', 'Carne magra 180g + quinoa + aguacate'],
      ['Vie', 'Smoothie: avena + frutos rojos + proteína', 'Pasta integral 140g + pavo molido 180g', 'Plátano + almendras 30g', 'Bacalao 200g + papa 220g + judías verdes'],
      ['Sáb', 'Waffles de avena + yogur + miel', 'Poke bowl: arroz + salmón 180g + edamame', 'Fruta + maní 30g', 'Fajitas de pollo con tortillas integrales'],
      ['Dom', 'Huevos 2 + pan + tomate rallado + EVOO', 'Garbanzos 200g + arroz + pollo 150g', 'Batido de cacao + proteína', 'Pavo 200g + puré de papa + verduras']
    ]] },
    definicion: { note: 'Menú de la fase Definición (sem 5-8). En fase Volumen (sem 1-4) sube los carbohidratos de comida y cena ~+40%.', weeks: [[
      ['Lun', 'Claras 5 + avena 50g + fresas', 'Pollo 200g + arroz 100g + ensalada grande', 'Yogur 0% + arándanos', 'Pescado blanco 220g + verduras al vapor'],
      ['Mar', 'Tortilla de claras + espinaca + pan (1)', 'Atún 2 latas + quinoa 80g + tomate', 'Manzana + almendras 15g', 'Pechuga 200g + brócoli + EVOO 1 cda'],
      ['Mié', 'Yogur griego 0% 250g + chía 1 cda', 'Ternera magra 180g + arroz 90g + pimientos', 'Requesón 100g', 'Salmón 160g + espárragos + ensalada'],
      ['Jue', 'Avena 50g + proteína + canela', 'Pavo 200g + batata 150g + verduras', 'Zanahoria + hummus 2 cdas', 'Tilapia 220g + calabacín + champiñones'],
      ['Vie', 'Claras 5 + 1 huevo + tostada', 'Pollo 200g + lentejas 120g + ensalada', 'Yogur 0% + fresas', 'Merluza 220g + judías verdes + limón'],
      ['Sáb', 'Smoothie verde: espinaca + proteína + piña', 'Arroz 100g + salmón 160g + pepino', 'Nueces 15g', 'Pechuga a la plancha + ensalada grande'],
      ['Dom', 'Tortitas de claras y avena + fruta', 'Carne magra 180g + quinoa 80g + verduras', 'Yogur 0% o gelatina proteica', 'Revuelto de claras + champiñones + pan (1)']
    ], [
      ['Lun', 'Yogur 0% + avena 40g + arándanos', 'Tilapia 220g + arroz 90g + brócoli', 'Pepino + hummus 2 cdas', 'Pollo 200g + ensalada grande + EVOO 1 cda'],
      ['Mar', 'Claras 5 + champiñones + tostada', 'Pavo 200g + quinoa 80g + espinacas', 'Manzana + maní 15g', 'Bacalao 220g + calabacín a la plancha'],
      ['Mié', 'Avena 50g + proteína + fresas', 'Pollo 200g + batata 140g + ensalada', 'Yogur 0% + canela', 'Atún fresco 180g + verduras wok'],
      ['Jue', 'Tortilla de claras + tomate + pan (1)', 'Ternera magra 170g + arroz 90g + pimiento', 'Requesón 100g + piña', 'Merluza 220g + espárragos'],
      ['Vie', 'Smoothie: proteína + espinaca + manzana', 'Salmón 150g + lentejas 100g + rúcula', 'Zanahoria + almendras 15g', 'Pechuga 200g + coliflor asada'],
      ['Sáb', 'Yogur griego 0% + chía + frutos rojos', 'Pollo 200g + cuscús 80g + ensalada', 'Palomitas naturales 20g', 'Pescado blanco 220g + verduras al vapor'],
      ['Dom', 'Tortitas de claras + cacao + ½ plátano', 'Pavo 200g + arroz 90g + brócoli', 'Yogur 0%', 'Revuelto de claras + atún + ensalada']
    ]] },
    ciclado: { note: '🔥 ALTO = día de entreno pesado (más carbos) · 🌙 BAJO = descanso o cardio suave (más grasas y proteína).', weeks: [[
      ['Lun 🔥', 'Avena 90g + plátano + proteína', 'Arroz 180g + pollo 200g + verduras', 'Pan de arroz + miel + batido', 'Pasta 140g + ternera magra + tomate'],
      ['Mar 🌙', 'Huevos 3 + ½ aguacate + espinacas', 'Ensalada grande + pollo 200g + EVOO', 'Nueces 30g + queso', 'Salmón 180g + brócoli + mantequilla 10g'],
      ['Mié 🌙', 'Yogur griego entero + chía + nueces', 'Atún + aguacate + ensalada + huevo', 'Almendras 30g', 'Pechuga 200g + calabacín + queso'],
      ['Jue 🔥', 'Panqueques de avena + miel + fruta', 'Arroz 180g + ternera 180g + pimientos', 'Plátano + batido de proteína', 'Papa 300g + pollo 200g + verduras'],
      ['Vie 🌙', 'Tortilla 3 huevos + champiñones', 'Salmón 180g + ensalada + aguacate', 'Queso + jamón de pavo', 'Merluza + espárragos + EVOO'],
      ['Sáb 🌙', 'Claras 4 + 2 huevos + espinaca', 'Pollo 200g + coliflor + tahini', 'Maní 30g', 'Carne 180g + ensalada + ½ aguacate'],
      ['Dom 🌙', 'Yogur griego + linaza + frutos rojos', 'Atún 2 latas + huevo + ensalada', 'Almendras 25g', 'Pescado blanco + verduras + EVOO']
    ], [
      ['Lun 🔥', 'Crema de arroz + claras + miel', 'Quinoa 170g + pavo 200g + verduras', 'Fruta + batido de proteína', 'Arroz 170g + salmón + calabacín'],
      ['Mar 🌙', 'Omelette 3 huevos + queso + tomate', 'Ensalada de pollo + aguacate + nueces', 'Queso fresco + pepino', 'Ternera + brócoli + EVOO'],
      ['Mié 🌙', 'Yogur entero + almendras + canela', 'Salmón + rúcula + huevo duro', 'Nueces 30g', 'Pollo + champiñones salteados'],
      ['Jue 🔥', 'Avena 90g + cacao + plátano', 'Pasta 150g + atún + tomate', 'Pan integral + miel + proteína', 'Batata 300g + ternera + ensalada'],
      ['Vie 🌙', 'Huevos revueltos + ½ aguacate', 'Pavo 200g + ensalada grande + EVOO', 'Avellanas 30g', 'Bacalao + espárragos + mantequilla 10g'],
      ['Sáb 🌙', 'Tortilla de claras + espinaca + queso', 'Pollo + arroz de coliflor + tahini', 'Maní 25g', 'Salmón + calabacín + limón'],
      ['Dom 🌙', 'Yogur griego + chía', 'Huevos + atún + aguacate + ensalada', 'Queso + nueces 20g', 'Merluza + verduras al vapor + EVOO']
    ]] },
    mediterranea: { note: 'EVOO como grasa principal · pescado azul 2-3×/semana · legumbres 3×/semana.', weeks: [[
      ['Lun', 'Yogur griego + nueces 30g + miel + arándanos', 'Salmón 180g + arroz integral + ensalada griega', 'Hummus + zanahoria', 'Garbanzos 150g + espinacas + ajo + EVOO'],
      ['Mar', 'Tostada integral + tomate + EVOO + jamón', 'Pollo al limón + cuscús + verduras', 'Aceitunas + queso feta', 'Sardinas 120g + ensalada + pan integral'],
      ['Mié', 'Avena + higos + almendras', 'Lentejas 200g + verduras + arroz', 'Yogur + miel', 'Merluza al horno + papas + pimientos'],
      ['Jue', 'Huevos 2 + pan integral + aguacate', 'Pasta integral + atún + alcaparras + tomate', 'Fruta + nueces', 'Pollo + berenjena asada + tzatziki'],
      ['Vie', 'Yogur griego + granola + fresas', 'Paella de mariscos (arroz 150g)', 'Hummus + pepino', 'Ensalada caprese + pan + jamón'],
      ['Sáb', 'Tostada + ricotta + miel + nuez', 'Salmón + quinoa + espárragos', 'Aceitunas + almendras', 'Pisto de verduras + huevo + pan'],
      ['Dom', 'Tortilla española ligera + ensalada', 'Pescado a la plancha + papas', 'Yogur + frutos rojos', 'Sopa de legumbres + queso feta']
    ], [
      ['Lun', 'Yogur + granola + higos', 'Dorada al horno + verduras + arroz', 'Almendras + fruta', 'Ensalada de garbanzos + atún + EVOO'],
      ['Mar', 'Pan integral + aguacate + tomate', 'Pollo al ajillo + cuscús + calabacín', 'Queso feta + aceitunas', 'Crema de calabaza + huevo + pan'],
      ['Mié', 'Avena + pera + nueces + canela', 'Arroz integral + gambas + ajo + espinaca', 'Yogur griego + miel', 'Bacalao + pisto + papa'],
      ['Jue', 'Huevos + pan + EVOO + tomate rallado', 'Lentejas + arroz + zanahoria + comino', 'Fruta + almendras', 'Pavo + berenjena + yogur con hierbas'],
      ['Vie', 'Yogur + fresas + chía', 'Pasta + sardinas + tomate + alcaparras', 'Hummus + ½ pan pita', 'Ensalada griega grande + pollo'],
      ['Sáb', 'Tostada + ricotta + arándanos', 'Salmón + bulgur + pepino + eneldo', 'Aceitunas + nueces', 'Verduras asadas + queso + pan'],
      ['Dom', 'Tortilla de espinaca + ensalada', 'Pescado blanco + papas al horno + limón', 'Yogur + miel + nuez', 'Sopa minestrone + queso rallado']
    ]] }
  };
  /* ===== GENERADOR DE MENÚS: 12 meses × 5 semanas, combinaciones sin repetirse ===== */
  var DIAS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
  var CICLO_ALTO = [true, false, false, true, false, false, false];
  function dietPools(plan) {
    var P = { des: [], com: [], col: [], cen: [] };
    DIETWEEKS[plan].weeks.forEach(function(wk) {
      wk.forEach(function(r) {
        if (P.des.indexOf(r[1]) === -1) P.des.push(r[1]);
        if (P.com.indexOf(r[2]) === -1) P.com.push(r[2]);
        if (P.col.indexOf(r[3]) === -1) P.col.push(r[3]);
        if (P.cen.indexOf(r[4]) === -1) P.cen.push(r[4]);
      });
    });
    return P;
  }
  function gcdInt(a, b) { return b ? gcdInt(b, a % b) : a; }
  function coprimeStride(base, len) {
    if (len <= 1) return 1;
    var s = base % len;
    if (s === 0) s = 1;
    while (gcdInt(s, len) !== 1) { s = (s % len) + 1; }
    return s;
  }
  function getWeekMenu(plan, mi, wi) {
    var rows = [], d;
    if (plan === 'ciclado') {
      var A = { des: [], com: [], col: [], cen: [] };
      var B = { des: [], com: [], col: [], cen: [] };
      var KEYS = ['des', 'com', 'col', 'cen'];
      DIETWEEKS.ciclado.weeks.forEach(function(wk) {
        wk.forEach(function(r, di) {
          var t = CICLO_ALTO[di] ? A : B;
          KEYS.forEach(function(key, ki) {
            if (t[key].indexOf(r[ki + 1]) === -1) t[key].push(r[ki + 1]);
          });
        });
      });
      var ai = 0, bi = 0;
      for (d = 0; d < 7; d++) {
        var alto = CICLO_ALTO[d];
        var P = alto ? A : B;
        var k = alto ? ai++ : bi++;
        rows.push([
          TX(DIAS[d]) + (alto ? ' 🔥' : ' 🌙'),
          TXDISH(P.des[(mi * 3 + wi * 5 + k * coprimeStride(3, P.des.length)) % P.des.length]),
          TXDISH(P.com[(mi * 7 + wi * 2 + k * coprimeStride(7, P.com.length) + 1) % P.com.length]),
          TXDISH(P.col[(mi * 5 + wi * 7 + k * coprimeStride(9, P.col.length) + 2) % P.col.length]),
          TXDISH(P.cen[(mi * 11 + wi * 3 + k * coprimeStride(11, P.cen.length) + 3) % P.cen.length])
        ]);
      }
      return rows;
    }
    var P2 = dietPools(plan);
    for (d = 0; d < 7; d++) {
      rows.push([
        DIAS[d],
        P2.des[(mi * 3 + wi * 5 + d * coprimeStride(3, P2.des.length)) % P2.des.length],
        P2.com[(mi * 7 + wi * 2 + d * coprimeStride(5, P2.com.length) + 1) % P2.com.length],
        P2.col[(mi * 5 + wi * 7 + d * coprimeStride(9, P2.col.length) + 4) % P2.col.length],
        P2.cen[(mi * 11 + wi * 3 + d * coprimeStride(11, P2.cen.length) + 2) % P2.cen.length]
      ]);
    }
    return rows;
  }
  function renderDietWeeks(mi, wi) {
    document.querySelectorAll('.diet-week').forEach(function(w) {
      var d = DIETWEEKS[w.dataset.plan];
      if (!d) return;
      var rows = getWeekMenu(w.dataset.plan, mi, wi);
      w.innerHTML = '<div style="overflow-x:auto"><table class="diet-menu" style="width:100%;min-width:560px;margin-top:12px;"><thead><tr><th>' + T('th.day','Día') + '</th><th>' + T('th.bre','Desayuno') + '</th><th>' + T('th.lun','Comida') + '</th><th>' + T('th.sna','Colación') + '</th><th>' + T('th.din','Cena') + '</th></tr></thead><tbody>' +
        rows.map(function(r) { return '<tr><td>' + r[0] + '</td><td>' + TXDISH(r[1]) + '</td><td>' + TXDISH(r[2]) + '</td><td>' + TXDISH(r[3]) + '</td><td>' + TXDISH(r[4]) + '</td></tr>'; }).join('') +
        '</tbody></table></div>' +
        (TX(d.note) ? '<p style="font-size:0.75rem;color:#889;margin-top:8px">' + TX(d.note) + '</p>' : '');
    });
  }
  (function initDietWeeks() {
    var selM = document.getElementById('mt-month');
    var selW = document.getElementById('mt-week');
    if (!selM || !selW) return;
    var MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    function buildMonths() {
      var v = selM.value;
      selM.innerHTML = MESES.map(function(m, i) { return '<option value="' + i + '">' + TX(m) + '</option>'; }).join('');
      if (v !== '' && v != null) selM.value = v;
    }
    window.__renderDietSel = function() { buildMonths(); apply(); };
    buildMonths();
    var now = new Date();
    function apply() {
      var mi = parseInt(selM.value, 10);
      var wi = parseInt(selW.value, 10);
      renderDietWeeks(mi, wi);
      var hint = document.getElementById('mt-hint');
      if (hint) hint.textContent = TX(MESES[mi]) + ' · ' + T('dyn.week','Semana') + ' ' + (wi + 1) + ' ' + T('dyn.hint60','— 60 semanas al año por plan, combinadas para no repetirse.');
    }
    selM.value = now.getMonth();
    selW.value = Math.min(4, Math.floor((now.getDate() - 1) / 7));
    selM.addEventListener('change', apply);
    selW.addEventListener('change', apply);
    apply();
  })();

  /* ===== BOTÁNICA NUTRICIONAL (propiedades reales, sin mitos) ===== */
  var BOTANICA = [
    { e: '🍉', n: 'Sandía', c: 'Frutas', k: 30, nut: 'Agua 92%, licopeno, citrulina', ben: 'Hidratación y antioxidantes para recuperar tras entrenar', uso: 'Post-entreno o snack; la sal solo aporta sabor y sodio — no quema grasa' },
    { e: '🍌', n: 'Plátano', c: 'Frutas', k: 89, nut: 'Potasio, B6, carbos rápidos', ben: 'Energía inmediata y función muscular (calambres)', uso: 'Pre-entreno o en batidos' },
    { e: '🫐', n: 'Arándanos', c: 'Frutas', k: 57, nut: 'Antocianinas, vitamina C', ben: 'Antioxidantes; apoyo cognitivo y vascular', uso: 'Con yogur o avena' },
    { e: '🍎', n: 'Manzana', c: 'Frutas', k: 52, nut: 'Pectina (fibra), polifenoles', ben: 'Saciedad y salud intestinal', uso: 'Snack con un puñado de maní' },
    { e: '🥑', n: 'Aguacate', c: 'Frutas', k: 160, nut: 'Grasas monoinsaturadas, potasio', ben: 'Salud cardiovascular; mejora absorción de vitaminas A-D-E-K', uso: 'En tostadas o ensaladas' },
    { e: '🍊', n: 'Naranja', c: 'Frutas', k: 47, nut: 'Vitamina C, folato', ben: 'Inmunidad y síntesis de colágeno', uso: 'Entera mejor que en jugo (conserva la fibra)' },
    { e: '🍍', n: 'Piña', c: 'Frutas', k: 50, nut: 'Bromelina, vitamina C', ben: 'Apoya la digestión de proteínas', uso: 'Postre tras comidas altas en proteína' },
    { e: '🥭', n: 'Mango', c: 'Frutas', k: 60, nut: 'Vitaminas A y C', ben: 'Piel, visión e inmunidad', uso: 'Snack o en smoothie' },
    { e: '🥬', n: 'Espinaca', c: 'Verduras', k: 23, nut: 'Hierro, folato, nitratos', ben: 'Transporte de oxígeno y rendimiento', uso: 'Salteada o camuflada en batidos' },
    { e: '🥦', n: 'Brócoli', c: 'Verduras', k: 34, nut: 'Sulforafano, fibra, vit C', ben: 'Antioxidante estrella y saciedad', uso: 'Al vapor 3-4 min (no lo hiervas de más)' },
    { e: '🥕', n: 'Zanahoria', c: 'Verduras', k: 41, nut: 'Betacaroteno', ben: 'Visión y piel', uso: 'Cruda con hummus' },
    { e: '🍅', n: 'Tomate', c: 'Verduras', k: 18, nut: 'Licopeno (aumenta al cocinar)', ben: 'Salud cardiovascular', uso: 'Salsa casera con EVOO' },
    { e: '🫑', n: 'Pimiento', c: 'Verduras', k: 31, nut: 'Más vitamina C que la naranja', ben: 'Inmunidad y colágeno', uso: 'Crudo en ensalada o salteado' },
    { e: '🧄', n: 'Ajo', c: 'Verduras', k: 149, nut: 'Alicina', ben: 'Apoyo cardiovascular e inmune', uso: 'Picado y reposado 10 min antes de cocinar' },
    { e: '🫚', n: 'Jengibre', c: 'Verduras', k: 80, nut: 'Gingerol', ben: 'Náuseas y molestias digestivas', uso: 'En té o rallado en comidas' },
    { e: '🌱', n: 'Chía', c: 'Semillas', k: 486, nut: 'Omega-3 (ALA), 34g de fibra', ben: 'Saciedad y salud intestinal', uso: '1 cda hidratada en agua o yogur' },
    { e: '🌾', n: 'Linaza', c: 'Semillas', k: 534, nut: 'Omega-3, lignanos', ben: 'Corazón y regularidad digestiva', uso: 'Molida (1 cda) en avena o batidos' },
    { e: '🎃', n: 'Pepitas de calabaza', c: 'Semillas', k: 559, nut: 'Magnesio, zinc', ben: 'Sueño reparador e inmunidad', uso: 'Puñado (25-30g) o en ensaladas' },
    { e: '🌻', n: 'Semillas de girasol', c: 'Semillas', k: 584, nut: 'Vitamina E, selenio', ben: 'Protección antioxidante celular', uso: 'Puñado o en pan casero' },
    { e: '🌰', n: 'Almendras', c: 'Semillas', k: 579, nut: 'Vitamina E, magnesio, proteína', ben: 'Corazón y saciedad entre comidas', uso: '20-30g como colación' },
    { e: '🥜', n: 'Maní', c: 'Semillas', k: 567, nut: '26g de proteína, niacina', ben: 'Proteína y energía económicas', uso: 'Mantequilla natural sin azúcar añadida' },
    { e: '🟠', n: 'Cúrcuma', c: 'Especias', k: 354, nut: 'Curcumina', ben: 'Antiinflamatorio suave (se absorbe mejor con pimienta negra)', uso: 'En arroces, guisos o leche dorada' },
    { e: '🟤', n: 'Canela', c: 'Especias', k: 247, nut: 'Polifenoles', ben: 'Apoyo modesto al control de la glucosa', uso: 'En avena, café o yogur' },
    { e: '🍫', n: 'Cacao puro', c: 'Especias', k: 228, nut: 'Flavanoles, magnesio', ben: 'Ánimo y salud vascular', uso: 'En polvo sin azúcar o chocolate 85%+' },
    { e: '🍵', n: 'Té verde', c: 'Especias', k: 1, nut: 'Catequinas (EGCG), L-teanina', ben: 'Enfoque calmado y antioxidantes', uso: '2-3 tazas; evítalo tarde-noche' },
    { e: '🌿', n: 'Menta', c: 'Especias', k: 44, nut: 'Mentol', ben: 'Alivio digestivo y frescura', uso: 'Infusión después de comer' },
    { e: '🥣', n: 'Avena', c: 'Granos', k: 389, nut: 'Betaglucanos', ben: 'Colesterol bajo control y energía sostenida', uso: 'La base de tus desayunos de plan' },
    { e: '🍚', n: 'Quinoa', c: 'Granos', k: 368, nut: 'Proteína completa (14g)', ben: 'Los 9 aminoácidos esenciales en un grano', uso: 'Sustituye al arroz 1:1' },
    { e: '🫘', n: 'Lentejas', c: 'Granos', k: 116, nut: 'Hierro, 9g proteína, fibra', ben: 'Energía estable y salud intestinal', uso: 'En guisos o ensaladas frías' },
    { e: '🧆', n: 'Garbanzos', c: 'Granos', k: 164, nut: 'Proteína + fibra', ben: 'Saciedad prolongada', uso: 'Hummus o tostados al horno' },
    { e: '🍙', n: 'Arroz integral', c: 'Granos', k: 111, nut: 'Carbos complejos, magnesio', ben: 'El combustible de tus entrenos', uso: 'Comida pre o post entreno' },
    { e: '🍓', n: 'Fresas', c: 'Frutas', k: 32, nut: 'Vitamina C, manganeso', ben: 'Antioxidantes con muy pocas calorías', uso: 'Con yogur o avena' },
    { e: '🥝', n: 'Kiwi', c: 'Frutas', k: 61, nut: 'Vit C, actinidina', ben: 'Digestión de proteínas e inmunidad', uso: 'Postre tras una cena proteica' },
    { e: '🍇', n: 'Uvas', c: 'Frutas', k: 69, nut: 'Polifenoles (resveratrol)', ben: 'Salud vascular', uso: 'Congeladas como snack fresco' },
    { e: '🍋', n: 'Limón', c: 'Frutas', k: 29, nut: 'Vitamina C', ben: 'Sabor sin calorías; te ayuda a beber más agua', uso: 'En agua o aliños' },
    { e: '🍒', n: 'Cerezas', c: 'Frutas', k: 63, nut: 'Antocianinas', ben: 'Se estudian para la recuperación muscular', uso: 'Puñado post-entreno' },
    { e: '🥥', n: 'Coco', c: 'Frutas', k: 354, nut: 'MCT; su agua aporta potasio', ben: 'El agua de coco es un electrolito natural', uso: 'Agua de coco post-entreno (los cubitos con chía son solo presentación 😉)' },
    { e: '🥒', n: 'Pepino', c: 'Verduras', k: 15, nut: 'Agua 96%', ben: 'Hidratación y volumen sin calorías', uso: 'En ensaladas o con hummus' },
    { e: '🧅', n: 'Cebolla', c: 'Verduras', k: 40, nut: 'Quercetina', ben: 'Antioxidante y mucho sabor con pocas kcal', uso: 'Base de guisos y salteados' },
    { e: '🍄', n: 'Champiñón', c: 'Verduras', k: 22, nut: 'Selenio; vit D si toma sol', ben: 'Umami saciante y ligerísimo', uso: 'Salteado o a la plancha' },
    { e: '🍠', n: 'Batata', c: 'Verduras', k: 86, nut: 'Betacaroteno, carbos complejos', ben: 'Energía estable para entrenar', uso: 'Asada pre o post entreno' },
    { e: '🍆', n: 'Berenjena', c: 'Verduras', k: 25, nut: 'Nasunina, fibra', ben: 'Antioxidante y saciante', uso: 'Asada o en pisto' },
    { e: '🌽', n: 'Maíz', c: 'Verduras', k: 86, nut: 'Luteína, fibra', ben: 'Vista y energía', uso: 'En ensaladas o mazorca' },
    { e: '🌰', n: 'Nueces', c: 'Semillas', k: 654, nut: 'Omega-3 (ALA) líder en frutos secos', ben: 'Cerebro y corazón', uso: '4-6 nueces al día' },
    { e: '⚪', n: 'Sésamo', c: 'Semillas', k: 573, nut: 'Calcio, lignanos', ben: 'Huesos y aroma tostado', uso: 'Tahini o espolvoreado' },
    { e: '🟢', n: 'Pistachos', c: 'Semillas', k: 560, nut: 'Proteína, luteína', ben: 'Pelarlos te hace comer más despacio', uso: '30g con cáscara como snack' },
    { e: '⚫', n: 'Pimienta negra', c: 'Especias', k: 251, nut: 'Piperina', ben: 'Multiplica la absorción de la curcumina', uso: 'Siempre junto a la cúrcuma' },
    { e: '🍀', n: 'Orégano', c: 'Especias', k: 265, nut: 'Carvacrol', ben: 'Especia muy antioxidante', uso: 'En salsas y proteínas' },
    { e: '🍯', n: 'Miel', c: 'Especias', k: 304, nut: 'Azúcares naturales', ben: 'Energía rápida — sigue siendo azúcar, con medida', uso: '1 cdita pre-entreno o en avena' },
    { e: '🌼', n: 'Manzanilla', c: 'Especias', k: 1, nut: 'Apigenina', ben: 'Relajación; aliada del sueño', uso: 'Infusión 30-60 min antes de dormir' },
    { e: '🪴', n: 'Romero', c: 'Especias', k: 131, nut: 'Ácido rosmarínico', ben: 'Aroma asociado a alerta y memoria', uso: 'En carnes, papas y aceites' },
    { e: '🍞', n: 'Pan integral', c: 'Granos', k: 247, nut: 'Fibra, vitaminas B', ben: 'El carbohidrato cotidiano, con su fibra', uso: 'Tostadas del desayuno' },
    { e: '🍝', n: 'Pasta integral', c: 'Granos', k: 158, nut: 'Carbos de absorción media', ben: 'Combustible clásico del deportista', uso: 'Comida pre-entreno (kcal en cocido)' },
    { e: '🫛', n: 'Edamame', c: 'Granos', k: 122, nut: 'Proteína vegetal completa', ben: 'De las mejores proteínas verdes', uso: 'Al vapor con sal marina' },
    { e: '🫘', n: 'Frijoles negros', c: 'Granos', k: 132, nut: 'Antocianinas, hierro, fibra', ben: 'Energía y salud intestinal', uso: 'En bowls con arroz' },
    { e: '🍈', n: 'Semillas de papaya', c: 'Semillas', k: 558, nut: 'Carpaína, papaína', ben: 'Tradición tropical contra parásitos; un estudio pequeño la respalda', uso: 'Dosis baja: 1 cdita molida en ayunas pocos días; evitar en embarazo — consulta a tu médico' },
    { e: '🪵', n: 'Clavo de olor', c: 'Especias', k: 274, nut: 'Eugenol', ben: 'Uno de los antioxidantes más potentes; antimicrobiano tradicional', uso: '1-2 clavos en infusión o molido en avena' },
    { e: '🍃', n: 'Epazote', c: 'Especias', k: 32, nut: 'Ascaridol', ben: 'Hierba mexicana usada por siglos contra parásitos intestinales', uso: 'Hojas frescas en frijoles (uso culinario); el aceite concentrado es tóxico — evítalo' },
    { e: '☘️', n: 'Tomillo', c: 'Especias', k: 101, nut: 'Timol', ben: 'Antimicrobiano culinario clásico; aliado respiratorio tradicional', uso: 'En carnes, sopas e infusiones' },
    { e: '🏵️', n: 'Diente de león', c: 'Verduras', k: 45, nut: 'Potasio, taraxacina', ben: 'Amargo tradicional para apoyo digestivo, hepático y renal', uso: 'Hojas tiernas en ensalada o infusión de raíz; diurético suave' }
  ];
  var BOTCATS = ['Todas', 'Frutas', 'Verduras', 'Semillas', 'Especias', 'Granos'];
  var botCat = 'Todas', botQ = '';
  function renderBotChips() {
    var el = document.getElementById('bot-chips');
    if (!el) return;
    el.innerHTML = BOTCATS.map(function(c) {
      return '<button class="diet-tab' + (c === botCat ? ' active' : '') + '" data-c="' + c + '">' + TX(c) + '</button>';
    }).join('');
  }
  function renderBot() {
    var grid = document.getElementById('bot-grid');
    if (!grid) return;
    var q = botQ.toLowerCase();
    var list = BOTANICA.filter(function(f) {
      if (botCat !== 'Todas' && f.c !== botCat) return false;
      return !q || f.n.toLowerCase().indexOf(q) !== -1 || f.nut.toLowerCase().indexOf(q) !== -1 || f.ben.toLowerCase().indexOf(q) !== -1;
    });
    grid.innerHTML = list.map(function(f) {
      var i = BOTANICA.indexOf(f);
      return '<div class="bot-card"><div class="bot-emoji">' + f.e + '</div><div class="bot-name">' + TX(f.n) + '</div><span class="bot-kcal">' + f.k + ' kcal / 100g</span><div class="bot-nut">' + TX(f.nut) + '</div><div class="bot-ben">' + TX(f.ben) + '</div><div class="bot-uso">💡 ' + TX(f.uso) + '</div><button class="bot-log" onclick="logBot(' + i + ')">' + T('dyn.log100', '🍽 Registrar 100 g') + '</button></div>';
    }).join('') || '<p style="color:#889;font-size:0.85rem">' + T('bot.nores', 'Sin resultados — prueba otra búsqueda.') + '</p>';
  }
  window.__renderBot = function() { try { renderBotChips(); } catch(e) {} renderBot(); };
  window.logBot = function(i) {
    var f = BOTANICA[i];
    if (!f) return;
    if (window.recordIntake) window.recordIntake(f.k);
    showToast('✓ ' + TX(f.n) + ': +' + f.k + ' ' + T('t.kcalhoy', 'kcal registradas hoy'));
  };
  (function initBotanica() {
    var chips = document.getElementById('bot-chips');
    if (!chips) return;
    chips.addEventListener('click', function(e) {
      var b = e.target.closest('.diet-tab');
      if (!b) return;
      botCat = b.dataset.c;
      renderBotChips(); renderBot();
    });
    document.getElementById('bot-search').addEventListener('input', function() {
      botQ = this.value.trim();
      renderBot();
    });
    renderBotChips(); renderBot();
  })();
  var BOTFACTS = [
    '¿Sabías que el pimiento rojo tiene más vitamina C que la naranja?',
    '¿Sabías que el licopeno del tomate se absorbe mejor cocinado con un poco de aceite?',
    '¿Sabías que el agua de coco aporta potasio y electrolitos naturales? Los cubitos con chía son solo una forma bonita de tomarla 😉',
    '¿Sabías que la curcumina de la cúrcuma se absorbe hasta 20× mejor con pimienta negra?',
    '¿Sabías que la avena contiene betaglucanos que ayudan a mantener el colesterol a raya?',
    '¿Sabías que la quinoa trae los 9 aminoácidos esenciales, como una proteína animal?',
    '¿Sabías que las cerezas concentran antocianinas que se estudian para la recuperación muscular?',
    '¿Sabías que la espinaca aporta nitratos que tu cuerpo usa para oxigenar el músculo?',
    '¿Sabías que 30 g de pepitas de calabaza cubren buena parte del magnesio del día?',
    '¿Sabías que pelar pistachos te hace comer más despacio y sentirte más lleno?'
  ];
  (function initBotExtras() {
    var factEl = document.getElementById('bot-fact-text');
    var factBox = document.getElementById('bot-fact');
    if (factEl && factBox) {
      var fi = Math.floor(Math.random() * BOTFACTS.length);
      var showFact = function() {
        factEl.textContent = TX(BOTFACTS[fi % BOTFACTS.length]);
        fi++;
      };
      showFact();
      setInterval(showFact, 8000);
      factBox.addEventListener('click', showFact);
    }
    var strip = document.getElementById('bot-grid');
    var prev = document.querySelector('#botanica .lib-prev');
    var next = document.querySelector('#botanica .lib-next');
    if (strip && prev && next) {
      prev.addEventListener('click', function() { strip.scrollBy({ left: -strip.clientWidth * 0.8, behavior: 'smooth' }); });
      next.addEventListener('click', function() { strip.scrollBy({ left: strip.clientWidth * 0.8, behavior: 'smooth' }); });
    }
  })();
  var PRIDS = ['squat', 'bench', 'dead', 'ohp'];
  var PRLABEL = { squat: 'pr-squat', bench: 'pr-bench', dead: 'pr-dead', ohp: 'pr-ohp' };
  function getDay() {
    var k = todayKey();
    if (!DAYS[k]) DAYS[k] = { in: 0, out: 0, vol: 0, sleep: null };
    return DAYS[k];
  }
  function saveHealth() {
    var keys = Object.keys(DAYS).sort();
    while (keys.length > 14) { delete DAYS[keys.shift()]; }
    saveJSON('vill_days', DAYS);
    saveJSON('vill_stats', STATS);
  }
  window.getRecentDays = function(n) {
    return Object.keys(DAYS).sort().slice(-n).map(function(k) {
      var d = DAYS[k];
      return { label: k.slice(8) + '/' + k.slice(5, 7), vol: d.vol, kin: d['in'], out: d.out, sleep: d.sleep };
    });
  };

  /* ---- Niveles de atleta (kg totales levantados) ---- */
  var LEVELS = [
    { name: 'Principiante', icon: '🌱', min: 0 },
    { name: 'Novato',       icon: '🔰', min: 5000 },
    { name: 'Guerrero',     icon: '⚔️', min: 25000 },
    { name: 'Élite',        icon: '💎', min: 75000 },
    { name: 'Titán',        icon: '⚡', min: 200000 },
    { name: 'Predator',     icon: '🦁', min: 500000 }
  ];
  function levelIndexOf(v) { var i = 0; for (var j = 0; j < LEVELS.length; j++) { if (v >= LEVELS[j].min) i = j; } return i; }

  function renderLevel() {
    var elI = document.getElementById('level-icon');
    if (!elI) return;
    var idx = levelIndexOf(STATS.totalVolume);
    var L = LEVELS[idx];
    var next = LEVELS[idx + 1];
    elI.textContent = L.icon;
    document.getElementById('level-name').textContent = TX(L.name);
    document.getElementById('level-total').textContent = STATS.totalVolume.toLocaleString('es');
    var pct = next ? Math.min(100, ((STATS.totalVolume - L.min) / (next.min - L.min)) * 100) : 100;
    document.getElementById('level-bar').style.width = pct + '%';
    document.getElementById('level-next').textContent = next
      ? T('dyn.missing', 'Faltan') + ' ' + Math.max(0, next.min - STATS.totalVolume).toLocaleString('es') + ' kg ' + T('dyn.forlevel', 'para') + ' ' + next.icon + ' ' + TX(next.name)
      : '👑 Nivel máximo alcanzado: eres un Predator.';
    document.getElementById('tier-strip').innerHTML = LEVELS.map(function(t, i) {
      var cls = i < idx ? 'unlocked' : (i === idx ? 'unlocked current' : 'locked');
      return '<div class="tier ' + cls + '"><span class="t-icon">' + t.icon + '</span>' + TX(t.name) + '<span class="t-kg">' + t.min.toLocaleString('es') + ' kg</span></div>';
    }).join('');
  }

  var DEMO_LB = [
    { name: 'Carlos M.', vol: 315400 },
    { name: 'Laura G.',  vol: 148200 },
    { name: 'Javier R.', vol: 82600 },
    { name: 'Sofía P.',  vol: 41800 },
    { name: 'Diego L.',  vol: 18900 }
  ];
  function renderLeaderboard() {
    var table = document.getElementById('leaderboard-table');
    if (!table) return;
    var rows = DEMO_LB.concat([{ name: 'Tú', vol: STATS.totalVolume, you: true }]);
    rows.sort(function(a, b) { return b.vol - a.vol; });
    var medals = ['🥇', '🥈', '🥉'];
    table.innerHTML = '<tr><th>#</th><th>' + TX('Atleta') + '</th><th>' + TX('Nivel') + '</th><th>' + TX('Kg totales') + '</th></tr>' +
      rows.map(function(r, i) {
        var L = LEVELS[levelIndexOf(r.vol)];
        var rankClass = i < 3 ? 'rank-' + (i + 1) : '';
        var style = r.you ? ' style="background:rgba(5,217,232,0.07)"' : '';
        var nm = r.you ? TX('⭐ Tú') : ((medals[i] ? medals[i] + ' ' : '') + r.name);
        return '<tr' + style + '><td class="' + rankClass + '">' + (i + 1) + '</td><td>' + nm + '</td><td>' + L.icon + ' ' + TX(L.name) + '</td><td>' + r.vol.toLocaleString('es') + '</td></tr>';
      }).join('');
  }

  function renderPRs() {
    PRIDS.forEach(function(id) {
      var el = document.getElementById(PRLABEL[id]);
      if (el) el.textContent = PRS[id] ? toDisplay(PRS[id]) : '—';
      var unitEl = el && el.parentElement ? el.parentElement.querySelector('.pr-unit') : null;
      if (unitEl) unitEl.textContent = UNIT.toLowerCase();
    });
  }

  function updateHealthPanel() {
    var grid = document.getElementById('health-grid');
    if (!grid) return;
    var d = getDay();
    var L = LEVELS[levelIndexOf(STATS.totalVolume)];
    grid.innerHTML =
      '<div class="health-card"><div class="h-val">' + Math.round(d['in']) + '</div><div class="h-lab">' + TX('🍽 kcal registradas') + '</div></div>' +
      '<div class="health-card"><div class="h-val">' + Math.round(d.out) + '</div><div class="h-lab">' + TX('🔥 kcal quemadas') + '</div></div>' +
      '<div class="health-card"><div class="h-val">' + d.vol.toLocaleString('es') + '</div><div class="h-lab">' + TX('🏋️ kg volumen hoy') + '</div></div>' +
      '<div class="health-card"><div class="h-val">' + Math.round(d.water || 0) + '</div><div class="h-lab">' + TX('💧 ml de agua') + '</div></div>' +
      '<div class="health-card"><div class="h-val">' + (d.sleep ? d.sleep + ' h' : '—') + '</div><div class="h-lab">' + TX('😴 sueño anoche') + '</div></div>' +
      '<div class="health-card"><div class="h-val">' + L.icon + '</div><div class="h-lab">' + TX(L.name) + '</div></div>';
  }

  window.recordIntake = function(kcal) {
    var d = getDay();
    d['in'] += kcal;
    saveHealth();
    updateHealthPanel();
  };
  window.addWater = function(ml) {
    var d = getDay();
    d.water = (d.water || 0) + ml;
    saveHealth();
    var v = document.getElementById('hydro-val');
    if (v) v.textContent = Math.round(d.water) + ' ml';
    updateHealthPanel();
    showToast('💧 +' + ml + ' ' + T('t.hydr', 'ml — hidratación al día'));
  };
  (function initHydro() {
    var v = document.getElementById('hydro-val');
    if (!v) return;
    v.textContent = Math.round(getDay().water || 0) + ' ml';
    var g = document.getElementById('hydro-goal');
    if (g) g.textContent = Math.round(getWeight() * 35);
  })();

  /* ---- Registrar peso usado en un ejercicio de la rutina ---- */
  window.logSet = function(id, srcId) {
    var ex = EXERCISES.find(function(e) { return e.id === id; });
    if (!ex) return;
    if (routineIds.indexOf(id) === -1) { routineIds.push(id); }
    var inp = document.getElementById(srcId || ('w-' + id));
    var raw = inp ? parseFloat(inp.value) : NaN;
    var kg = (raw && raw > 0) ? toKg(raw) : NaN;
    var bodyBased = false;
    if (!kg || kg <= 0) { kg = getWeight(); bodyBased = true; }
    var m = ex.sets.match(/^(\d+)x(\d+)(s?)$/);
    var sets = m ? parseInt(m[1], 10) : 3;
    var reps = m ? parseInt(m[2], 10) : 10;
    if (m && m[3] === 's') reps = Math.max(5, Math.round(reps / 6));
    var volume = Math.round(kg * sets * reps);
    if (!bodyBased && inp) { WEIGHTS[id] = Math.round(kg * 10) / 10; saveJSON('vill_weights', WEIGHTS); }
    if (DONE_TODAY.indexOf(id) === -1) {
      DONE_TODAY.push(id);
      DONE_STORE[todayKey()] = DONE_TODAY;
      saveJSON('vill_done', DONE_STORE);
    }
    var prevIdx = levelIndexOf(STATS.totalVolume);
    STATS.totalVolume += volume;
    var d = getDay();
    d.vol += volume;
    d.out += exKcal(ex);
    saveHealth();
    var newIdx = levelIndexOf(STATS.totalVolume);
    if (newIdx > prevIdx) {
      showToast('🎉 ' + T('t.lvl1', '¡SUBISTE DE NIVEL!') + ' ' + LEVELS[newIdx].icon + ' ' + T('t.lvl2', 'Ahora eres') + ' ' + TX(LEVELS[newIdx].name));
    } else {
      showToast('✓ ' + TX(ex.name) + ': +' + volume.toLocaleString('es') + ' ' + T('t.vol', 'kg de volumen') + (bodyBased ? ' (' + T('t.body', 'peso corporal') + ')' : ''));
    }
    if (PRIDS.indexOf(id) !== -1 && !bodyBased && kg > (PRS[id] || 0)) {
      PRS[id] = kg;
      saveJSON('vill_prs', PRS);
      renderPRs();
      showToast('🏆 ' + T('t.pr', '¡Nuevo PR en') + ' ' + TX(ex.name) + ': ' + toDisplay(Math.round(kg * 10) / 10) + ' ' + UNIT.toLowerCase() + '!');
    }
    renderLevel(); renderLeaderboard(); updateHealthPanel(); renderRoutine(); renderLibrary();
  };

  /* ---- Sueño & recuperación ---- */
  window.__renderSleepW = function() { try { renderSleepBars(); } catch(e) {} };
  function renderSleepBars() {
    var wrap = document.getElementById('sleep-bars');
    if (!wrap) return;
    var days = window.getRecentDays(7);
    var any = days.some(function(d) { return d.sleep; });
    if (!any) {
      wrap.innerHTML = '<span style="color:#667;font-size:0.75rem">' + T('sleep.empty', 'Aún sin registros — guarda tu primera noche y aquí verás tu semana.') + '</span>';
      return;
    }
    wrap.innerHTML = days.map(function(d) {
      var h = d.sleep || 0;
      var pct = Math.min(100, h / 12 * 100);
      return '<div class="sleep-bar-col"><div class="sleep-bar-fill" style="height:' + pct + '%"></div><span>' + d.label + '</span></div>';
    }).join('');
  }
  var sleepQuality = 'regular';
  (function initSleep() {
    var slider = document.getElementById('sleep-hours');
    if (!slider) return;
    var valEl = document.getElementById('sleep-hours-val');
    slider.addEventListener('input', function() { valEl.textContent = this.value; });
    document.querySelectorAll('.sq-btn').forEach(function(b) {
      b.addEventListener('click', function() {
        document.querySelectorAll('.sq-btn').forEach(function(x) { x.classList.remove('active'); });
        this.classList.add('active');
        sleepQuality = this.dataset.q;
      });
    });
    document.getElementById('sleep-save').addEventListener('click', function() {
      var h = parseFloat(slider.value);
      var d = getDay();
      d.sleep = h;
      saveHealth();
      var target = d.out >= 500 ? 8.5 : (d.out >= 250 ? 8 : 7.5);
      var v = document.getElementById('sleep-verdict');
      var extra = sleepQuality === 'ligero' ? ' Marcaste sueño ligero: evita cafeína tarde y pantallas justo antes de dormir.' : '';
      if (h >= target) {
        v.className = 'ok';
        v.innerHTML = T("slp.g1", '✅ <strong>Recuperación óptima.</strong> Dormiste ') + h + T("slp.g2", ' h y hoy llevas ~') + Math.round(d.out) + T("slp.g3", ' kcal quemadas entrenando. Tu cuerpo tiene el descanso que necesita para reparar músculo y fijar el progreso.') + extra;
      } else if (h >= target - 1) {
        v.className = 'mid';
        v.innerHTML = '🟡 <strong>' + T('slp.y1', 'Aceptable, pero justo.') + '</strong> ' + T('slp.y2', 'Con ~') + Math.round(d.out) + ' ' + T('slp.y3', 'kcal quemadas hoy lo ideal serían') + ' ' + target + ' h ' + T('slp.y4', 'y dormiste') + ' ' + h + ' h. ' + T('slp.y5', 'Intenta adelantar 30–60 min tu hora de acostarte.') + extra;
      } else {
        v.className = 'low';
        v.innerHTML = '🔴 <strong>' + T('slp.r1', 'Insuficiente para tu carga de hoy.') + '</strong> ' + T('slp.r2', 'Quemaste ~') + Math.round(d.out) + ' ' + T('slp.r3', 'kcal y dormiste') + ' ' + h + ' h (' + T('slp.r4', 'ideal') + ': ' + target + ' h). ' + T('slp.r5', 'Dormir poco frena la reparación muscular y suele aumentar el apetito al día siguiente.') + extra;
      }
      updateHealthPanel();
      renderSleepBars();
      showToast('😴 ' + T('t.slept', 'Sueño registrado') + ': ' + h + ' h');
    });
  })();

  (function initGoal() {
    var btn = document.getElementById('calc-btn');
    if (!btn) return;
    var wEl = document.getElementById('calc-weight');
    var w0 = getWeight();
    if (wEl && w0) wEl.value = w0;
    btn.addEventListener('click', function() {
      var sex = document.getElementById('calc-sex').value;
      var age = parseFloat(document.getElementById('calc-age').value);
      var h = parseFloat(document.getElementById('calc-height').value);
      var w = parseFloat(document.getElementById('calc-weight').value);
      var act = parseFloat(document.getElementById('calc-act').value);
      var adj = parseFloat(document.getElementById('calc-obj').value);
      if (!age || !h || !w) { showToast(T('t.calc', 'Completa edad, altura y peso')); return; }
      var bmr = 10 * w + 6.25 * h - 5 * age + (sex === 'm' ? 5 : -161);
      var tdee = Math.round(bmr * act);
      var meta = Math.max(1200, Math.round(tdee + adj));
      var objTxt = adj > 0 ? 'subir de peso' : (adj < 0 ? 'definir' : 'mantenerte');
      var box = document.getElementById('goal-result');
      box.innerHTML =
        '<div class="goal-line">Tu mantenimiento (TDEE): <strong>' + tdee.toLocaleString('es') + ' kcal/día</strong></div>' +
        '<div class="goal-line big">Meta para ' + objTxt + ': <strong>' + meta.toLocaleString('es') + ' kcal/día</strong></div>' +
        '<button class="btn btn-primary" onclick="applyGoal(' + meta + ')">🎯 Establecer como mi meta diaria</button>' +
        '<div style="margin-top:10px;font-size:0.7rem;color:#667">Fórmula Mifflin-St Jeor · estimación orientativa de bienestar, no consejo médico.</div>';
      box.style.display = 'block';
    });
  })();

  /* ===== Programa Mindfulness 21 días ===== */
  var MED21 = [
    { n: 'Respiración consciente', m: 5, s: ['Siéntate cómodo, espalda erguida, ojos suaves o cerrados.', 'Lleva la atención al aire entrando y saliendo por la nariz.', 'Cuando la mente se vaya (lo hará), regresa sin juzgar. Eso ES el entrenamiento.'] },
    { n: 'Conteo de respiraciones', m: 7, s: ['Respira natural; cuenta 1 en la primera exhalación.', 'Llega hasta 10 y vuelve a empezar.', '¿Perdiste la cuenta? Perfecto: nota a dónde se fue la mente y reinicia en 1.'] },
    { n: 'Escaneo corporal', m: 10, s: ['Recorre el cuerpo de pies a cabeza, zona por zona.', 'En cada zona nota tensión, temperatura y contacto — sin cambiar nada.', 'Si hay tensión, exhala "hacia" esa zona y suéltala un 10%.'] },
    { n: 'Respiración 4-7-8', m: 8, s: ['Inhala por la nariz 4 s, retén 7 s, exhala por la boca 8 s.', 'La exhalación larga activa el freno del sistema nervioso.', 'Usa el cronómetro de arriba con el patrón 4-7-8.'] },
    { n: 'Caminar consciente', m: 15, s: ['Camina algo más lento de lo normal, sin teléfono.', 'Siente cada pie: talón, planta, dedos.', 'Cuando notes el piloto automático, vuelve a los pies.'] },
    { n: 'Gratitud', m: 10, s: ['Piensa o escribe 3 cosas concretas de HOY que agradeces.', 'Por cada una: por qué ocurrió y quién contribuyó.', 'Nota cómo cambia el estado del cuerpo al evocarlas.'] },
    { n: 'Visualización atlética', m: 12, s: ['Elige un ejercicio (ej. sentadilla) y ensáyalo mentalmente.', 'Visualiza en primera persona: técnica, respiración, esfuerzo.', 'La corteza motora se activa al imaginar: es entrenamiento real.'] },
    { n: 'Metta (bondad)', m: 10, s: ['Repite mentalmente: "Que esté bien, que esté fuerte, que esté en paz".', 'Dirígelo a ti, luego a alguien querido, luego a alguien neutro.', 'No fuerces sentir nada: el gesto de desear ya entrena el ánimo.'] },
    { n: 'Respiración de caja', m: 10, s: ['Inhala 4 s · retén 4 s · exhala 4 s · retén 4 s.', 'La usan militares y deportistas para foco bajo presión.', 'Cronómetro de arriba: patrón Caja.'] },
    { n: 'Comer consciente', m: 10, s: ['Come una comida o snack sin pantallas.', 'Primeros 3 bocados: textura, temperatura, sabor, velocidad.', 'Suelta el cubierto entre bocados y nota la saciedad real.'] },
    { n: 'Paisaje de sonidos', m: 10, s: ['Ojos cerrados: deja que los sonidos vengan a ti.', 'Etiqueta suave: lejos, cerca, agudo, grave.', 'No persigas ni rechaces ninguno: solo recepción.'] },
    { n: 'Escaneo profundo', m: 15, s: ['Como el día 3, pero al doble de lentitud.', 'Incluye cara, mandíbula, lengua y manos: acumulan tensión.', 'Termina 1 minuto sintiendo el cuerpo como un todo.'] },
    { n: 'Respiración coherente', m: 10, s: ['Inhala 5 s, exhala 5 s: 6 respiraciones por minuto.', 'Este ritmo favorece la variabilidad cardiaca (HRV).', 'Cronómetro de arriba: patrón Coherente 5-5.'] },
    { n: 'Revisión + intención', m: 10, s: ['Mitad del camino: ¿qué práctica te dio más? ¿Cuál costó?', 'Escribe una frase con tu intención para la semana final.', 'Repite hoy tu práctica favorita 5 minutos.'] },
    { n: 'Visualizar la meta', m: 12, s: ['Visualiza tu meta física a 6 meses con detalle sensorial.', 'Ahora visualiza el PROCESO: tu semana típica para llegar ahí.', 'La meta motiva; el proceso construye. Ensaya el proceso.'] },
    { n: 'Anclaje 5-4-3-2-1', m: 8, s: ['Nombra 5 cosas que ves, 4 que sientes, 3 que oyes, 2 que hueles, 1 que saboreas.', 'Es un ancla instantánea para ansiedad o sobrecarga.', 'Hazlo dos veces; la segunda, más lento.'] },
    { n: 'Metta ampliada', m: 12, s: ['Como el día 8, y añade a alguien difícil y a "todos los que entrenan hoy".', 'Si aparece resistencia, obsérvala: también es práctica.', 'Cierra dirigiéndolo a ti otra vez.'] },
    { n: '4-7-8 largo', m: 10, s: ['Repite el patrón 4-7-8, ahora 10 minutos.', 'Nota cuánto más fácil fluye que el día 4.', 'Ideal 30-60 minutos antes de dormir.'] },
    { n: 'Caminata 20', m: 20, s: ['20 minutos, idealmente al aire libre y sin audífonos.', 'Alterna: 5 min pies · 5 min sonidos · 5 min respiración · 5 min abierto.', 'Termina notando tu estado frente al inicio.'] },
    { n: 'Silencio abierto', m: 15, s: ['Sin técnica: siéntate y observa lo que aparezca.', 'Pensamientos, sonidos, sensaciones: todo pasa, tú observas.', 'La práctica más avanzada: no hacer nada, del todo.'] },
    { n: 'Sesión maestra', m: 20, s: ['Diseña tu sesión: 5 min respiración + 10 min tu práctica favorita + 5 min metta o gratitud.', 'Ya tienes las herramientas: ahora son tuyas.', 'Repite el programa o crea tu rutina diaria de 10 minutos.'] }
  ];
  var MEDDONE = loadJSON('vill_med', []);
  function renderMedProgram() {
    var grid = document.getElementById('mp-grid');
    if (!grid) return;
    grid.innerHTML = MED21.map(function(d, i) {
      var done = MEDDONE.indexOf(i) !== -1;
      return '<button type="button" class="mp-day' + (done ? ' done' : '') + '" onclick="openMedDay(' + i + ')">' +
        '<span class="d-num">' + T('med.DAY','DÍA') + ' ' + (i + 1) + '</span>' +
        '<span class="d-name">' + TX(d.n) + '</span>' +
        '<span class="d-min">' + d.m + ' min</span>' +
      '</button>';
    }).join('');
    var doneEl = document.getElementById('mp-done');
    if (doneEl) doneEl.textContent = MEDDONE.length;
    var fill = document.getElementById('mp-fill');
    if (fill) fill.style.width = Math.round(MEDDONE.length / 21 * 100) + '%';
  }
  window.toggleMedDay = function(i) {
    var idx = MEDDONE.indexOf(i);
    if (idx === -1) {
      MEDDONE.push(i);
      showToast('🧘 ' + T('med.day','Día') + ' ' + (i + 1) + ' ' + T('med.dayDone','completado') + ' — ' + MEDDONE.length + '/21');
    } else {
      MEDDONE.splice(idx, 1);
    }
    saveJSON('vill_med', MEDDONE);
    renderMedProgram();
    window.openMedDay(i);
  };
  window.openMedDay = function(i) {
    var d = MED21[i];
    if (!d) return;
    var done = MEDDONE.indexOf(i) !== -1;
    var breathBtn = /4-7-8|caja|coherente/i.test(d.n)
      ? '<button class="btn btn-outline" type="button" onclick="closeModal();document.getElementById(\'meditation\').scrollIntoView({behavior:\'smooth\'})">' + T('med.timer','⏱ Abrir cronómetro') + '</button>'
      : '';
    var html = '<div style="font-size:1.15rem;font-weight:800;background:linear-gradient(135deg,#FF2A6D,#05D9E8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">' + T('med.day','Día') + ' ' + (i + 1) + ' · ' + TX(d.n) + '</div>' +
      '<div style="color:#888899;margin:4px 0 12px;">' + d.m + ' ' + T('med.min','minutos · práctica guiada') + '</div>' +
      '<div class="ex-tech" style="margin-top:0"><div class="et-title">' + T('med.how','🧘 Cómo hacerlo') + '</div><ol>' +
        d.s.map(function(x) { return '<li>' + TX(x) + '</li>'; }).join('') +
      '</ol></div>' +
      '<div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap">' +
        '<button class="btn ' + (done ? 'btn-pink' : 'btn-primary') + '" type="button" onclick="toggleMedDay(' + i + ')">' + (done ? T('med.undo','↺ Desmarcar') : T('med.done','✓ Marcar completado')) + '</button>' +
        breathBtn +
      '</div>';
    openModal(html);
  };
  renderMedProgram();

  renderPRs(); renderLevel(); renderLeaderboard(); updateHealthPanel(); renderSleepBars();

  /* ---- Recetas de recuperación (ordenadas por kcal) ---- */
  var RECIPES = [
    { t: 'Batido Recuperador Express', k: 320, p: 32, c: 38, f: 4, m: 5, tag: 'post-entreno',
      i: ['1 scoop de proteína whey', '1 plátano maduro', '250 ml leche o bebida de avena', '1 cda de miel', 'Hielo'] },
    { t: 'Tostada de Aguacate y Huevo', k: 380, p: 20, c: 32, f: 20, m: 10, tag: 'ligero',
      i: ['2 rebanadas de pan integral', '1/2 aguacate', '2 huevos pochados', 'Sal, pimienta y limón'] },
    { t: 'Yogur Griego con Frutos Rojos', k: 290, p: 24, c: 30, f: 7, m: 3, tag: 'snack',
      i: ['250 g yogur griego 0%', '100 g frutos rojos', '20 g almendras', '1 cda de miel'] },
    { t: 'Bowl de Quinoa y Pollo', k: 520, p: 42, c: 52, f: 14, m: 25, tag: 'comida completa',
      i: ['120 g quinoa cocida', '180 g pechuga de pollo', 'Brócoli al vapor', 'Aceite de oliva y limón'] },
    { t: 'Wrap de Pavo y Hummus', k: 460, p: 34, c: 44, f: 15, m: 8, tag: 'rápido',
      i: ['1 tortilla integral grande', '120 g pechuga de pavo', '3 cdas de hummus', 'Espinacas y tomate'] },
    { t: 'Salmón al Horno con Batata', k: 620, p: 42, c: 55, f: 20, m: 30, tag: 'cena fuerte',
      i: ['180 g salmón fresco', '200 g batata en cubos', 'Espárragos', 'Aceite de oliva, ajo y eneldo'] },
    { t: 'Arroz con Pollo Fitness', k: 680, p: 52, c: 72, f: 14, m: 25, tag: 'volumen',
      i: ['150 g arroz integral', '200 g pollo', 'Pimientos y cebolla', 'Especias al gusto'] },
    { t: 'Pasta Boloñesa Magra', k: 720, p: 46, c: 85, f: 18, m: 30, tag: 'volumen',
      i: ['130 g pasta integral', '180 g carne magra picada', 'Tomate triturado', 'Ajo, albahaca, parmesano'] },
    { t: 'Avena Nocturna Proteica', k: 540, p: 34, c: 62, f: 14, m: 5, tag: 'pre-cama',
      i: ['80 g avena', '1 scoop proteína', '200 ml leche', '1 cda mantequilla de maní', 'Canela'] },
    { t: 'Burrito Bowl de Ternera', k: 780, p: 50, c: 78, f: 26, m: 30, tag: 'máxima recarga',
      i: ['150 g arroz', '180 g ternera magra', 'Frijoles negros', 'Aguacate, pico de gallo, lima'] }
  ];
  function pickRecipes(target) {
    // Elegir 3 recetas cuyo total se acerque al objetivo de recarga
    var sorted = RECIPES.slice().sort(function(a, b) {
      return Math.abs(a.k - target / 2) - Math.abs(b.k - target / 2);
    });
    return sorted.slice(0, 3);
  }
  function showDietReco() {
    var items = routineIds.map(function(id) { return EXERCISES.find(function(e) { return e.id === id; }); }).filter(Boolean);
    if (!items.length) return;
    var burned = items.reduce(function(s, ex) { return s + exKcal(ex); }, 0);
    var protein = Math.round(getWeight() * 1.8);
    var box = document.getElementById('diet-reco');
    document.getElementById('reco-kcal').textContent = burned;
    var intensity = burned >= 500 ? 'una sesión exigente' : (burned >= 250 ? 'una sesión sólida' : 'una sesión ligera');
    document.getElementById('reco-text').innerHTML =
      'Has planificado <strong>' + intensity + '</strong>. Para recuperar bien, repón esas calorías con comida de calidad y apunta a <strong style="color:#FF2A6D">' + protein + ' g de proteína</strong> hoy (1.8 g/kg). ' +
      'Come dentro de las 2 h siguientes al entreno y prioriza carbohidratos para rellenar el glucógeno.';
    document.getElementById('reco-cards').innerHTML = pickRecipes(burned).map(function(r) {
      return '<div class="reco-card">' +
        '<div class="rc-title">' + r.t + '</div>' +
        '<span class="rc-kcal">' + r.k + ' kcal</span> <span style="font-size:0.68rem;color:#667">· ' + r.m + ' min · ' + r.tag + '</span>' +
        '<div class="rc-macros">' + r.p + 'g proteína · ' + r.c + 'g carbos · ' + r.f + 'g grasas</div>' +
        '<ul>' + r.i.map(function(x) { return '<li>' + x + '</li>'; }).join('') + '</ul>' +
      '</div>';
    }).join('');
    box.classList.add('show');
  }

  document.getElementById('save-routine-btn').addEventListener('click', function() {
    if (!routineIds.length) { showToast(T('t.addone', 'Agrega al menos un ejercicio a tu rutina')); return; }
    try {
      localStorage.setItem('vill_routine_v3', JSON.stringify(routineIds));
      var msg = document.getElementById('planner-save-msg');
      msg.style.display = 'block';
      setTimeout(function() { msg.style.display = 'none'; }, 2500);
    } catch(e) { showToast(T('t.nosave', 'No se pudo guardar')); }
    showDietReco();
    var box = document.getElementById('diet-reco');
    if (box) setTimeout(function() { box.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 120);
  });
  document.getElementById('clear-routine-btn').addEventListener('click', function() {
    routineIds = [];
    try { localStorage.removeItem('vill_routine_v3'); } catch(e) {}
    renderRoutine(); renderLibrary();
    var rb = document.getElementById('diet-reco');
    if (rb) rb.classList.remove('show');
    showToast(T('t.clean', 'Rutina limpiada'));
  });

  /* ---- LIBRERÍA CON FILTROS ---- */
  var LIB_FILTERS = ['Todos', 'Pecho', 'Espalda', 'Piernas', 'Gluteos', 'Hombros', 'Biceps', 'Triceps', 'Core', 'Cardio'];
  var activeFilter = 'Todos';
  var diffColors = { 'Principiante': '#2ECC71', 'Intermedio': '#FFD700', 'Avanzado': '#FF2A6D' };
  var TAGGLOW = {
    Pecho: 'rgba(255,42,109,0.30)', Espalda: 'rgba(5,217,232,0.30)', Piernas: 'rgba(46,204,113,0.28)',
    Gluteos: 'rgba(255,140,66,0.30)', Hombros: 'rgba(255,215,0,0.26)', Biceps: 'rgba(179,104,255,0.30)',
    Triceps: 'rgba(224,86,253,0.28)', Core: 'rgba(77,208,225,0.28)', Cardio: 'rgba(255,82,82,0.30)'
  };

  function renderChips() {
    var chips = document.getElementById('lib-chips');
    var map = { Gluteos: 'Glúteos', Biceps: 'Bíceps', Triceps: 'Tríceps' };
    chips.innerHTML = LIB_FILTERS.map(function(f) {
      return '<button class="lib-chip' + (f === activeFilter ? ' active' : '') + '" data-f="' + f + '">' + (f === 'Todos' ? T('dyn.all', 'Todos') : TX(map[f] || f)) + '</button>';
    }).join('');
    chips.querySelectorAll('.lib-chip').forEach(function(c) {
      c.addEventListener('click', function() {
        activeFilter = this.dataset.f;
        renderChips(); renderLibrary();
      });
    });
  }
  function renderLibrary() {
    var grid = document.getElementById('ex-grid');
    var list = EXERCISES.filter(function(ex) {
      return activeFilter === 'Todos' || ex.tags.indexOf(activeFilter) !== -1;
    });
    grid.innerHTML = list.map(function(ex) {
      var inR = routineIds.indexOf(ex.id) !== -1;
      var glow = TAGGLOW[ex.tags[0]] || 'rgba(5,217,232,0.22)';
      var done = DONE_TODAY.indexOf(ex.id) !== -1;
      return '<div class="ex-card" onclick="showExModal(\'' + ex.id + '\')">' +
        '<span class="ex-help" title="Ver técnica correcta">❓</span>' +
        '<div class="ex-icon" style="background:radial-gradient(circle at 30% 25%, ' + glow + ', #14141d 72%)">' + ex.icon + '</div>' +
        '<div class="ex-info">' +
          '<div class="ex-name">' + (done ? '<span style="color:#2ECC71">✓ </span>' : '') + TX(ex.name) + '</div>' +
          '<div class="ex-muscle">' + ex.sets + ' · ' + ex.tags.map(function(t) { var mm = { Gluteos: 'Glúteos', Biceps: 'Bíceps', Triceps: 'Tríceps' }; return TX(mm[t] || t); }).join(', ') + '</div>' +
          '<div class="ex-cal">🔥 ≈' + exKcal(ex) + ' ' + T('dyn.session', 'kcal / sesión') + ' (' + ex.min + ' min)</div>' +
          '<span class="ex-diff" style="color:' + diffColors[ex.diff] + '">' + TX(ex.diff) + '</span>' +
          '<div class="ex-weight-row" onclick="event.stopPropagation()">' +
            '<input type="number" min="0" step="' + (UNIT === 'LB' ? '5' : '2.5') + '" class="w-input" id="lw-' + ex.id + '" placeholder="' + UNIT.toLowerCase() + '" value="' + (WEIGHTS[ex.id] ? toDisplay(WEIGHTS[ex.id]) : '') + '">' +
            '<button class="log-btn" title="Registrar serie hecha" onclick="logSet(\'' + ex.id + '\', \'lw-' + ex.id + '\')">✓</button>' +
          '</div>' +
          '<button class="add-routine-btn' + (inR ? ' in-routine' : '') + '" onclick="event.stopPropagation();' + (inR ? 'removeFromRoutine' : 'addToRoutine') + '(\'' + ex.id + '\')">' + (inR ? T('dyn.inroutine', '✓ En rutina · quitar') : T('dyn.add', '＋ Agregar a rutina')) + '</button>' +
        '</div>' +
      '</div>';
    }).join('');
  }
  /* ===== TÉCNICA CORRECTA (27 ejercicios, criterio de entrenador) ===== */
  var TECH = {
    squat: { s: ['Barra sobre los trapecios (no el cuello), pies al ancho de hombros con puntas ~15° afuera.', 'Pecho arriba y core firme; inicia empujando la cadera atrás y flexionando rodillas.', 'Baja hasta muslos al menos paralelos, rodillas siempre en línea con los pies.', 'Empuja el suelo con todo el pie para subir; exhala arriba.'], e: ['Rodillas que colapsan hacia dentro.', 'Talones que se despegan del suelo.', 'Redondear la zona lumbar al fondo.'] },
    legpress: { s: ['Espalda y glúteos pegados al respaldo; pies al centro, ancho de hombros.', 'Baja controlado hasta ~90° de rodilla sin que la cadera se despegue.', 'Empuja con todo el pie hasta casi extender, sin bloquear las rodillas.'], e: ['Bajar tanto que la lumbar se levanta del respaldo.', 'Bloquear las rodillas con un golpe seco.', 'Empujar solo con las puntas de los pies.'] },
    lunge: { s: ['Da un paso largo manteniendo el torso vertical.', 'Baja hasta que ambas rodillas queden ~90°; la trasera casi toca el suelo.', 'Empuja con el talón de la pierna delantera para volver; alterna piernas.'], e: ['Paso demasiado corto (castiga la rodilla).', 'Rodilla delantera que viaja muy por delante de la punta.', 'Inclinar el torso hacia adelante.'] },
    legext: { s: ['Ajusta el rodillo justo sobre los tobillos y la rodilla alineada con el eje de la máquina.', 'Sube controlado hasta casi extender por completo; pausa 1 s arriba.', 'Baja en 2-3 s resistiendo el peso.'], e: ['Dar la patada con impulso.', 'Hiperextender con golpe al final.', 'Despegar la cadera del asiento.'] },
    legcurl: { s: ['Rodillo sobre el tendón de Aquiles; caderas pegadas al banco.', 'Flexiona llevando los talones hacia el glúteo sin arquear la lumbar.', 'Baja lento y controla el estiramiento.'], e: ['Arquear la zona lumbar.', 'Usar impulso para completar la repetición.', 'Trabajar solo medio rango.'] },
    hipthrust: { s: ['Apoya la espalda alta en el banco; barra sobre la cadera con protector.', 'Pies al ancho de cadera; empuja con los talones hasta alinear hombro-cadera-rodilla.', 'Aprieta el glúteo 1-2 s arriba con el mentón ligeramente al pecho.', 'Baja controlado sin rebotar en el suelo.'], e: ['Hiperextender la lumbar en la parte alta.', 'Empujar con las puntas en vez de los talones.', 'Hacer rango corto por exceso de peso.'] },
    calf: { s: ['Apoya solo los metatarsos en el borde del escalón o plataforma.', 'Baja 1-2 s hasta sentir el estiramiento completo del gemelo.', 'Sube lo más alto posible y aprieta 1-2 s en la punta.'], e: ['Rebotar abajo aprovechando el tendón.', 'Rango corto y rápido.', 'Doblar las rodillas para ayudarse.'] },
    bench: { s: ['Escápulas retraídas y clavadas al banco; pies firmes en el suelo.', 'Agarre algo más ancho que los hombros, muñecas rectas.', 'Baja la barra al pecho medio con codos a ~45-60° del torso.', 'Toca ligero y empuja en línea hacia arriba y ligeramente atrás.'], e: ['Rebotar la barra en el pecho.', 'Codos abiertos a 90° (castigan el hombro).', 'Despegar los glúteos del banco.'] },
    incline: { s: ['Banco entre 30-45°; escápulas retraídas.', 'La barra baja a la parte alta del pecho/clavícula.', 'Empuja vertical sin que los codos se abran en exceso.'], e: ['Inclinar demasiado el banco (se vuelve press de hombro).', 'Rebotar la barra.', 'Arco lumbar exagerado.'] },
    fly: { s: ['Mancuernas arriba con codos semiflexionados y fijos.', 'Abre en arco amplio hasta sentir el estiramiento del pecho, sin dolor de hombro.', 'Cierra como si abrazaras un barril, apretando el pecho.'], e: ['Flexionar los codos y convertirlo en press.', 'Bajar más allá del rango cómodo del hombro.', 'Usar un peso que rompa el arco.'] },
    dips: { s: ['Hombros deprimidos, lejos de las orejas; core firme.', 'Inclínate un poco adelante para enfocar el pecho.', 'Baja controlado hasta ~90° de codo y sube sin bloquear con golpe.'], e: ['Encoger los hombros hacia las orejas.', 'Bajar de más con molestia en el hombro.', 'Balancear las piernas para ayudarse.'] },
    pullup: { s: ['Agarre pronado algo más ancho que los hombros.', 'Inicia deprimiendo las escápulas (hombros lejos de orejas).', 'Sube llevando el pecho a la barra, codos hacia el suelo.', 'Baja controlado hasta casi extender los brazos.'], e: ['Balancearse (kipping) para subir.', 'No bajar completo (medio rango).', 'Encoger los hombros al colgar.'] },
    row: { s: ['Bisagra de cadera con torso ~45° y espalda neutra.', 'Tira de la barra hacia el abdomen bajo llevando los codos atrás.', 'Aprieta las escápulas 1 s y baja controlado.'], e: ['Dar tirones con la lumbar.', 'Levantar el torso en cada repetición.', 'Tirar hacia el pecho con codos abiertos.'] },
    lat: { s: ['Pecho alto, ligera inclinación atrás fija.', 'Tira de la barra hacia la clavícula llevando los codos abajo y atrás.', 'Controla la subida sintiendo el estiramiento del dorsal.'], e: ['Mecerse hacia atrás para mover más peso.', 'Jalar tras la nuca.', 'Tirar solo con los brazos sin activar la espalda.'] },
    cablerow: { s: ['Rodillas semiflexionadas y torso vertical estable.', 'Tira hacia el abdomen con los codos pegados al cuerpo.', 'Junta las escápulas al final y regresa lento.'], e: ['Mecerse adelante y atrás.', 'Encoger los hombros.', 'Redondear la lumbar al estirar.'] },
    dead: { s: ['Barra sobre el medio del pie; agarre justo fuera de las piernas.', 'Bisagra: cadera atrás, espalda neutra, pecho arriba; tensa la barra antes de despegar.', 'Empuja el suelo y sube con la barra pegada a las piernas.', 'Bloquea arriba con la cadera, sin hiperextender; baja con la misma bisagra.'], e: ['Redondear la zona lumbar.', 'Dejar que la barra se aleje del cuerpo.', 'Rebotar el peso contra el suelo.'] },
    ohp: { s: ['Barra a la altura de las clavículas, agarre justo fuera de hombros.', 'Glúteos y abdomen firmes: el cuerpo es una columna.', 'Empuja vertical y mete la cabeza al pasar la barra.', 'Bloquea arriba con los bíceps junto a las orejas.'], e: ['Arquear la lumbar en exceso.', 'Empujar la barra hacia adelante.', 'Impulsarse con las piernas (eso ya es push press).'] },
    lateral: { s: ['Codos semiflexionados y fijos durante todo el recorrido.', 'Sube liderando con los codos hasta la altura de los hombros.', 'Pausa breve y baja en 2-3 s.'], e: ['Encoger los trapecios al subir.', 'Balancear el cuerpo para impulsar.', 'Subir por encima del hombro con peso excesivo.'] },
    facepull: { s: ['Polea a la altura de la cara con cuerda.', 'Tira hacia la frente separando las manos, codos altos.', 'Rota los nudillos hacia atrás al final (rotación externa).'], e: ['Convertirlo en un remo bajo.', 'Usar demasiado peso.', 'Encoger los hombros hacia las orejas.'] },
    curl: { s: ['Codos pegados al torso y fijos.', 'Sube sin balancear; gira la palma hacia arriba si usas mancuerna.', 'Baja en 2-3 s hasta extender casi por completo.'], e: ['Balancear la cadera para ayudar.', 'Dejar que los codos viajen hacia adelante.', 'Trabajar solo medio rango.'] },
    hammer: { s: ['Agarre neutro (palmas enfrentadas) y codos fijos.', 'Sube controlado sin girar la muñeca.', 'Baja lento; trabaja braquial y antebrazo.'], e: ['Impulso con el torso.', 'Muñecas dobladas.', 'Dejar caer el peso en la bajada.'] },
    tricep: { s: ['Codos pegados al cuerpo y fijos como bisagras.', 'Extiende hasta bloquear abajo apretando el tríceps 1 s.', 'Sube controlado moviendo solo los antebrazos.'], e: ['Abrir los codos hacia afuera.', 'Inclinarse encima del peso.', 'Medio rango con exceso de carga.'] },
    plank: { s: ['Antebrazos bajo los hombros; cuerpo en línea recta de cabeza a talones.', 'Aprieta glúteo y abdomen con la pelvis ligeramente metida.', 'Mirada al suelo y respiración constante.'], e: ['Cadera caída o en pico.', 'Hiperextender el cuello mirando al frente.', 'Aguantar sin respirar.'] },
    crunch: { s: ['Lumbar pegada al suelo, manos a los lados de la cabeza sin tirar.', 'Despega solo las escápulas exhalando.', 'Baja controlado sin dejarte caer.'], e: ['Tirar del cuello con las manos.', 'Subir completo despegando la lumbar.', 'Usar impulso y velocidad.'] },
    legraise: { s: ['Lumbar presionada contra el suelo (manos bajo el glúteo si ayuda).', 'Baja las piernas solo hasta donde la lumbar no se arquee.', 'Sube exhalando con el abdomen, no con impulso.'], e: ['Arquear la lumbar al bajar.', 'Balancear las piernas.', 'Doblar y estirar rodillas sin control.'] },
    mclimber: { s: ['Plancha alta con hombros sobre las muñecas.', 'Lleva las rodillas al pecho alternando con ritmo, sin subir la cadera.', 'Core firme: la espalda no rebota.'], e: ['Cadera alta en pico.', 'Hombros que se van hacia atrás.', 'Perder la línea del cuerpo por ir rápido.'] },
    burpee: { s: ['Baja a sentadilla y apoya las manos.', 'Lanza los pies atrás a plancha firme (flexión opcional).', 'Recoge los pies y salta extendiendo la cadera.', 'Aterriza suave con rodillas flexionadas.'], e: ['Lumbar arqueada en la plancha.', 'Aterrizar con las piernas rígidas.', 'Sacrificar técnica por velocidad.'] }
  };
  function buildTechHTML(ex) {
    var t = TECH[ex.id];
    if (!t) return '';
    return '<div class="ex-tech">' +
      '<div class="et-title">' + T('ex.tech','📖 Técnica correcta') + '</div>' +
      '<ol>' + t.s.map(function(x) { return '<li>' + TX(x) + '</li>'; }).join('') + '</ol>' +
      '<div class="et-title et-warn">' + T('ex.err','⚠️ Errores comunes') + '</div>' +
      '<ul>' + t.e.map(function(x) { return '<li>' + TX(x) + '</li>'; }).join('') + '</ul>' +
      '<div class="et-note">' + T('ex.note','Domina el patrón con poco peso antes de progresar. Dolor articular (distinto al ardor muscular) = detente y revisa la técnica.') + '</div>' +
    '</div>';
  }
  window.showExModal = function(id) {
    var ex = EXERCISES.find(function(e) { return e.id === id; });
    if (!ex) return;
    var inR = routineIds.indexOf(ex.id) !== -1;
    var html = '<div style="font-size:1.2rem;font-weight:800;background:linear-gradient(135deg,#FF2A6D,#05D9E8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">' + ex.icon + ' ' + TX(ex.name) + '</div>' +
      '<div style="color:#888899;margin-top:4px;">' + tagsPretty(ex.tags) + ' · ' + TX(ex.diff) + '</div>' +
      '<div style="margin-top:12px;background:#16161f;border-radius:10px;padding:12px;font-size:0.85rem;line-height:1.7;">' +
        '<div>' + T('ex.sets','Series') + ': <strong style="color:#05D9E8">' + ex.sets + '</strong></div>' +
        '<div>' + T('ex.dur','Duración estimada') + ': <strong style="color:#05D9E8">' + ex.min + ' min</strong> (incluye descansos)</div>' +
        '<div>' + T('ex.met','Intensidad (MET)') + ': <strong style="color:#05D9E8">' + ex.met + '</strong></div>' +
        '<div>' + T('ex.cal','Calorías con tu peso') + ' (' + getWeight() + ' kg): <strong style="color:#FF2A6D">≈' + exKcal(ex) + ' kcal</strong></div>' +
      '</div>' +
      buildTechHTML(ex) +
      '<button class="btn ' + (inR ? 'btn-pink' : 'btn-primary') + '" style="margin-top:14px" onclick="' + (inR ? 'removeFromRoutine' : 'addToRoutine') + '(\'' + ex.id + '\');closeModal();">' + (inR ? T('ex.remove','Quitar de rutina') : T('dyn.add','＋ Agregar a rutina')) + '</button>';
    (function() {
      try {
        var u0 = ((window.EXGIF || {})[ex.id] || [])[0];
        if (u0 && u0.indexOf('cdn.shopify.com') !== -1) {
          var base = u0.split('#')[0];
          var pf = new Image(); pf.referrerPolicy = 'no-referrer';
          pf.src = base + (base.indexOf('?') === -1 ? '?' : '&') + 'width=480';
        }
      } catch(e) {}
    })();
    window.__modalHook = function(__mc) {
      var __t3 = __mc.querySelector('h3') || __mc.querySelector('h4');
      var __urls = (window.EXGIF || {})[ex.id];
      var __wrap = document.createElement('div');
      // Añade ?width= al CDN de Shopify para servir un gif más ligero (mitad de peso).
      function sized(u, w) {
        if (!u || u.indexOf('cdn.shopify.com') === -1) return u;
        var base = u.split('#')[0];
        return base + (base.indexOf('?') === -1 ? '?' : '&') + 'width=' + w;
      }
      if (__urls && __urls.length) {
        var curr = 0, tries = 0;
        var stage = document.createElement('div'); stage.className = 'exgif-stage';
        var pad = document.createElement('div'); pad.className = 'exgif-pad';
        var spin = document.createElement('div'); spin.className = 'exgif-spin';
        spin.textContent = T('gif.load', 'Cargando…');
        var img = document.createElement('img'); img.className = 'exgif-img';
        img.alt = TX(ex.name); img.decoding = 'async'; img.referrerPolicy = 'no-referrer';
        var settled = false, poll = null;
        function clearPoll() { if (poll) { clearInterval(poll); poll = null; } }
        function showImg() {
          if (settled) return; settled = true; clearPoll();
          img.style.opacity = '1'; if (spin.parentNode) spin.parentNode.removeChild(spin);
          // Precarga silenciosa del siguiente ángulo para que el cambio sea instantáneo.
          if (__urls.length > 1) { var nx = new Image(); nx.referrerPolicy = 'no-referrer'; nx.src = sized(__urls[(curr + 1) % __urls.length], 480); }
        }
        function retry() {
          if (settled) return; tries++;
          if (tries > 4) { spin.textContent = T('gif.slow', 'La demo tarda… revisa tu conexión'); return; }
          spin.textContent = T('gif.retry', 'Reintentando…');
          setTimeout(function() {
            if (settled) return;
            // 1ª/2ª: reintenta redimensionado; 3ª+: cae a la URL ORIGINAL sin width (plan B infalible).
            img.src = (tries >= 2) ? (__urls[curr].split('#')[0] + '&r=' + Date.now()) : (sized(__urls[curr], 480) + '&r=' + Date.now());
          }, 700);
        }
        img.addEventListener('load', showImg);
        img.addEventListener('error', retry);
        function loadAngle(idx) {
          settled = false; tries = 0; clearPoll(); img.style.opacity = '0';
          if (spin.parentNode !== stage) stage.appendChild(spin);
          spin.textContent = T('gif.load', 'Cargando…');
          img.removeAttribute('src');
          requestAnimationFrame(function() {
            img.src = sized(__urls[idx], 480);
            if (img.complete && img.naturalWidth > 0) { showImg(); return; }
            poll = setInterval(function() { if (img.naturalWidth > 0) showImg(); }, 200);
          });
        }
        pad.appendChild(img); stage.appendChild(pad); stage.appendChild(spin);
        if (__urls.length > 1) {
          var badge = document.createElement('div'); badge.className = 'exgif-badge';
          __urls.forEach(function(u, idx) {
            var b = document.createElement('button'); b.className = 'exgif-dot' + (idx === 0 ? ' on' : '');
            b.type = 'button'; b.textContent = (idx + 1);
            b.addEventListener('click', function(ev) {
              ev.stopPropagation(); if (idx === curr) return; curr = idx;
              badge.querySelectorAll('.exgif-dot').forEach(function(d, di) { d.className = 'exgif-dot' + (di === idx ? ' on' : ''); });
              loadAngle(idx);
            });
            badge.appendChild(b);
          });
          stage.appendChild(badge);
        }
        // Al ampliar: versión de mayor calidad (width mayor).
        stage.addEventListener('click', function() { if (settled) window.__exgifLightbox(sized(__urls[curr], 900), TX(ex.name)); });
        __wrap.appendChild(stage);
        var cap = document.createElement('div'); cap.className = 'exgif-cap';
        cap.setAttribute('data-tx', ''); cap.textContent = (__urls.length > 1 ? 'Toca los ángulos · pulsa para ampliar' : 'Demostración · pulsa para ampliar');
        __wrap.appendChild(cap);
        if (__t3 && __t3.parentNode) __t3.parentNode.insertBefore(__wrap, __t3.nextSibling); else __mc.insertBefore(__wrap, __mc.firstChild);
        loadAngle(0);
        return;
      } else {
        var cv = document.createElement('canvas'); cv.width = 230; cv.height = 190;
        cv.style.cssText = 'display:block;margin:8px auto 0;max-width:100%;background:radial-gradient(ellipse at 50% 60%, rgba(5,217,232,0.07), transparent 70%);border-radius:12px';
        __wrap.appendChild(cv);
        if (window.__exAnimStart) window.__exAnimStart(ex.id, cv);
      }
      if (__t3 && __t3.parentNode) __t3.parentNode.insertBefore(__wrap, __t3.nextSibling); else __mc.insertBefore(__wrap, __mc.firstChild);
    };
                        openModal(html);
  };
  function initLibNav() {
    var strip = document.getElementById('ex-grid');
    var prev = document.querySelector('.lib-prev');
    var next = document.querySelector('.lib-next');
    if (!strip || !prev || !next) return;
    prev.addEventListener('click', function() { strip.scrollBy({ left: -strip.clientWidth * 0.8, behavior: 'smooth' }); });
    next.addEventListener('click', function() { strip.scrollBy({ left: strip.clientWidth * 0.8, behavior: 'smooth' }); });
  }
  /* Botones sin type dentro de un posible <form> del tema */
  document.querySelectorAll('#vill-hub button:not([type])').forEach(function(b) { b.type = 'button'; });

  (function initMmClear() {
    var b = document.getElementById('mm-clear-btn');
    if (!b) return;
    b.addEventListener('click', function() {
      if (window.mmClearSelection3D) window.mmClearSelection3D();
      document.querySelectorAll('.muscle-btn').forEach(function(x) { x.classList.remove('active'); });
      var lab = document.getElementById('mm-selected-label');
      if (lab) { lab.textContent = ''; lab.style.display = 'none'; }
    });
  })();

  /* ===== LEMAS MOTIVACIONALES + IDIOMA (ES/EN/FR) ===== */
  var MOTTOS = {
    es: ['El cuerpo logra lo que la mente cree.', 'No cuentes los días: haz que los días cuenten.', 'Hoy, 1% mejor que ayer.', 'La disciplina pesa gramos; el arrepentimiento, toneladas.', 'Entrena · Come · Duerme · Repite.', 'Tu único rival es el de ayer.', 'La constancia convierte lo difícil en costumbre.', 'Hoy es un gran día para empezar.'],
    en: ['The body achieves what the mind believes.', 'Don’t count the days — make the days count.', 'Today: 1% better than yesterday.', 'Discipline weighs grams; regret weighs tons.', 'Train · Eat · Sleep · Repeat.', 'Your only rival is who you were yesterday.', 'Consistency turns hard into habit.', 'Today is a great day to start.'],
    fr: ['Le corps accomplit ce que l’esprit croit.', 'Ne compte pas les jours — fais que les jours comptent.', 'Aujourd’hui : 1% de mieux qu’hier.', 'La discipline pèse des grammes ; le regret, des tonnes.', 'Entraîne-toi · Mange · Dors · Répète.', 'Ton seul rival, c’est celui d’hier.', 'La constance transforme le difficile en habitude.', 'Aujourd’hui est un grand jour pour commencer.']
  };
  var CUR_LANG = 'es';
  (function initMotto() {
    var el = document.getElementById('hero-motto');
    if (!el) return;
    var mi = Math.floor(Math.random() * MOTTOS.es.length);
    function next() {
      el.classList.add('fade');
      setTimeout(function() {
        var arr = MOTTOS[CUR_LANG] || MOTTOS.es;
        mi = (mi + 1) % arr.length;
        el.textContent = '💬 ' + arr[mi];
        el.classList.remove('fade');
      }, 350);
    }
    setInterval(next, 6000);
    el.addEventListener('click', next);
  })();

  var SEC_IDS = ['muscle-map', 'planner', 'nutrition', 'goal', 'diet-plans', 'botanica', 'meditation', 'frequencies', 'level', 'progress', 'sleep', 'challenges'];
  var I18N = {
    en: {
      tag: '@villumination99 · VI.P',
      title: 'Transform your<br><span>Body &amp; Mind</span>',
      sub: 'Interactive 3D anatomy, calorie-accurate routines, smart nutrition, guided breathing and restorative frequencies — all in one place.',
      b1: '🧬 Explore 3D Anatomy', b2: '🏋️ Build my Routine',
      stats: ['Exercises', 'Frequencies', '3D Zones', 'Athlete Levels'],
      note: '🌐 Menus, foods and exercise data are shown in Spanish.',
      titles: { 'muscle-map': '3D Muscle Map', planner: 'Training', nutrition: 'Smart Nutrition', goal: 'Your Calorie Goal', 'diet-plans': 'Elite Diet Plans', botanica: '🌿 Nutritional Botany', meditation: 'Meditation & Guided Breathing', frequencies: 'Restorative Frequencies', level: 'Your Athlete Level', progress: 'Progress Analytics', sleep: 'Sleep & Recovery', challenges: 'Community Challenges' },
      idxTitle: 'Everything you\'ll find here',
      idxSub: '12 tools wired together: what you train feeds your level, what you eat feeds your charts. Tap any to jump straight in.',
      idx: { 'muscle-map': ['3D Muscle Map', 'Tap a muscle: see its exercises and add them'], 'planner': ['Training', 'Log kg and sets — every kilo counts'], 'nutrition': ['Nutrition', 'Scan your plate with AI and track macros'], 'goal': ['Calorie Goal', 'Get your TDEE and set a real target'], 'diet-plans': ['Diet Plans', '4 plans · Mon–Sun menus all year'], 'botanica': ['Nutritional Botany', '55 foods and their real properties'], 'meditation': ['Meditation', 'Guided breathing + 21-day program'], 'frequencies': ['Frequencies', 'Solfeggio, binaural and dual pulses'], 'level': ['Athlete Level', 'From Beginner to Predator'], 'progress': ['Progress', 'Your whole health in charts'], 'sleep': ['Sleep', 'Do you rest as much as you train?'], 'challenges': ['Challenges', 'Compete on the leaderboard'] },
      t: {
        'sub.map': 'Anatomy sculpted as one continuous surface, with definition grooves carved between muscles. Tap a zone: it lights up red on the body itself.',
        'sub.planner': 'Your routine for today: enter the weight, hit ✓ and every kilo feeds your athlete level, your PRs and the health panel. Pick exercises from the gallery below.',
        'sub.library': '27 exercises with real calories. Filter by muscle, swipe the gallery, enter the weight you used and hit ✓ to log the set — without leaving this page. Tap any ❓ card to see the correct technique.',
        'sub.nutrition': 'Track your macros and log food with the camera: local AI analyses the photo and suggests candidates for you to confirm.',
        'sub.goal': 'Work out how many calories your body needs, choose your goal — gain, maintain or cut — and set it as your daily Nutrition target.',
        'sub.diet': 'Pick a plan and follow the menus, recipes and shopping lists.',
        'sub.bot': 'Fruits, seeds, spices and grains with their real properties — so nature works in favour of your plan.',
        'sub.med': 'Follow the circle: it grows as you inhale, holds as you hold, and shrinks as you exhale. Ideal for visual people.',
        'sub.freq': '19 frequencies generated in real time: Solfeggio tones, binaural waves and dual pulses to sleep, meditate, focus or switch your mind on.',
        'sub.level': 'Every kilo you log in your routine adds total volume. Climb from Beginner to Predator and show up on the leaderboard.',
        'sub.progress': 'All your progress together: food logged, calories burned, volume lifted and rest.',
        'sub.sleep': 'Muscle repairs while you sleep. Log your hours and I will tell you whether it is enough for what you burned today.',
        'sub.chal': 'Compete on total volume with the community. Your level and your kilos show up on the leaderboard automatically.',
        'pl.today': '✅ My routine today',
        'pl.saved': '✓ Routine saved successfully',
        'pl.kcal': '🔥 Estimated calories for the session',
        'reco.burned': 'KCAL BURNED',
        'freq.t1': 'Solfeggio · pure tones',
        'freq.t2': 'Brainwaves · binaural',
        'freq.t3': 'Dual · 1–7 Hz pulses 🎧',
        'freq.tip': '📱 iPhone: sound is routed as “music”, so it plays even with the silent switch on — raise the volume with the side buttons. If you hear nothing, tap “Play” again.',
        'ph.food': 'Search food…',
        'ph.bot': 'Search food, nutrient or benefit…',
        'dyn.empty': 'Pick exercises from the gallery below ↓',
        'dyn.add': '＋ Add to routine',
        'dyn.inroutine': '✓ In routine · remove',
        'dyn.log100': '🍽 Log 100 g',
        'dyn.all': 'All',
        'dyn.basedon': 'Based on',
        'dyn.editweight': 'edit your weight in the profile',
        'dyn.work': 'min of work',
        'dyn.session': 'kcal / session',
        "dyn.phones": "use headphones",
        "dyn.missing": "Only",
        "dyn.forlevel": "to reach"
      },
      tx: {
        "Pecho": "Chest",
        "Espalda": "Back",
        "Hombros": "Shoulders",
        "Bíceps": "Biceps",
        "Tríceps": "Triceps",
        "Abdominales": "Abs",
        "Cuádriceps": "Quads",
        "Glúteos": "Glutes",
        "Gemelos": "Calves",
        "Principiante": "Beginner",
        "Novato": "Rookie",
        "Guerrero": "Warrior",
        "Élite": "Elite",
        "Titán": "Titan",
        "Predator": "Predator",
        "🍽 kcal registradas": "🍽 kcal logged",
        "🔥 kcal quemadas": "🔥 kcal burned",
        "🏋️ kg volumen hoy": "🏋️ kg volume today",
        "💧 ml de agua": "💧 ml of water",
        "😴 sueño anoche": "😴 sleep last night",
        "Atleta": "Athlete",
        "Nivel": "Level",
        "Kg totales": "Total kg",
        "⭐ Tú": "⭐ You",
        "😐 Ligero": "😐 Light",
        "🙂 Normal": "🙂 Normal",
        "😴 Profundo": "😴 Deep",
        "Todas": "All",
        "Frutas": "Fruits",
        "Verduras": "Vegetables",
        "Semillas": "Seeds",
        "Especias": "Spices",
        "Granos": "Grains",
        "Volumen Limpio": "Clean Bulk",
        "Definición + Volumen": "Cut + Bulk",
        "Ciclado de Carbos": "Carb Cycling",
        "Mediterránea": "Mediterranean",
        "Alivio Profundo": "Deep Relief",
        "Relajación física y descarga de tensión": "Physical relaxation and tension release",
        "Regeneración": "Regeneration",
        "Sensación de restauración y equilibrio": "A sense of restoration and balance",
        "Liberación": "Release",
        "Suelta el miedo y la culpa; base emocional": "Let go of fear and guilt; emotional grounding",
        "Cambio": "Change",
        "Facilita transiciones y deshace bloqueos": "Eases transitions and dissolves blocks",
        "Armonía Natural": "Natural Harmony",
        "Afinación suave; calma y coherencia": "Gentle tuning; calm and coherence",
        "Reparación": "Repair",
        "La \"frecuencia del amor\"; renovación y vitalidad": "The \"love frequency\"; renewal and vitality",
        "Conexión": "Connection",
        "Relaciones, empatía y comunicación": "Relationships, empathy and communication",
        "Despertar": "Awakening",
        "Intuición, claridad y expresión": "Intuition, clarity and expression",
        "Visión Interior": "Inner Vision",
        "Orden mental y equilibrio espiritual": "Mental order and spiritual balance",
        "Consciencia Plena": "Full Awareness",
        "Conexión superior y unidad": "Higher connection and unity",
        "Delta · Sueño Profundo": "Delta · Deep Sleep",
        "Descanso nocturno y recuperación total": "Night rest and full recovery",
        "Theta baja · Sanación": "Low Theta · Healing",
        "Relajación muy profunda, pre-sueño": "Very deep relaxation, pre-sleep",
        "Theta · Meditación": "Theta · Meditation",
        "Estados meditativos profundos y creatividad": "Deep meditative states and creativity",
        "Schumann · Tierra": "Schumann · Earth",
        "La resonancia de la Tierra; enraizamiento": "The Earth resonance; grounding",
        "Alpha · Relajación": "Alpha · Relaxation",
        "Calma alerta, ideal después de entrenar": "Alert calm, ideal after training",
        "Beta · Enfoque": "Beta · Focus",
        "Concentración estable para estudiar o trabajar": "Steady focus for study or work",
        "Gamma · Despertar": "Gamma · Awakening",
        "Alerta máxima, claridad y procesamiento mental": "Peak alertness, clarity and mental processing"
      },
      btns: { 'save-routine-btn': '💾 Save routine', 'clear-routine-btn': '🗑 Clear', 'calc-btn': 'Calculate my calories', 'sleep-save': 'Log last night', 'join-btn': 'Join the challenge', 'mm-clear-btn': '✕ Clear selection', 'scan-btn': '📷 Scan with camera', 'upload-btn': '🖼 Upload photo', 'capture-btn': '📸 Capture', 'stop-cam-btn': '⏹ Stop', 'breath-start': '▶ Start', 'breath-stop': '⏹ Stop', 'freq-stop-btn': '⏹ Stop', 'login-btn': 'Log in', 'register-btn': 'Sign up', 'logout-btn': 'Log out' }
    },
    fr: {
      tag: '@villumination99 · VI.P',
      title: 'Transforme ton<br><span>Corps &amp; Esprit</span>',
      sub: 'Anatomie 3D interactive, routines aux calories réelles, nutrition intelligente, respiration guidée et fréquences réparatrices — tout en un seul endroit.',
      b1: '🧬 Explorer l’anatomie 3D', b2: '🏋️ Créer ma routine',
      stats: ['Exercices', 'Fréquences', 'Zones 3D', 'Niveaux d’athlète'],
      note: '🌐 Les menus, aliments et exercices sont affichés en espagnol.',
      titles: { 'muscle-map': 'Carte musculaire 3D', planner: 'Entraînement', nutrition: 'Nutrition intelligente', goal: 'Ton objectif calorique', 'diet-plans': 'Plans diététiques d’élite', botanica: '🌿 Botanique nutritionnelle', meditation: 'Méditation & respiration guidée', frequencies: 'Fréquences réparatrices', level: 'Ton niveau d’athlète', progress: 'Analyse de progrès', sleep: 'Sommeil & récupération', challenges: 'Défis de la communauté' },
      idxTitle: 'Tout ce que tu trouveras ici',
      idxSub: '12 outils reliés entre eux : ce que tu t’entraînes nourrit ton niveau, ce que tu manges nourrit tes graphiques. Touche pour y aller direct.',
      idx: { 'muscle-map': ['Carte musculaire 3D', 'Touche un muscle : vois ses exercices'], 'planner': ['Entraînement', 'Enregistre kg et séries — chaque kilo compte'], 'nutrition': ['Nutrition', 'Scanne ton assiette avec l’IA, suis tes macros'], 'goal': ['Objectif calorique', 'Calcule ton TDEE et fixe ta vraie cible'], 'diet-plans': ['Plans diététiques', '4 plans · menus lun–dim toute l’année'], 'botanica': ['Botanique nutritionnelle', '55 aliments et leurs vraies propriétés'], 'meditation': ['Méditation', 'Respiration guidée + programme 21 jours'], 'frequencies': ['Fréquences', 'Solfeggio, binaurales et pulsations duales'], 'level': ['Niveau d’athlète', 'De Débutant à Predator'], 'progress': ['Progrès', 'Toute ta santé en graphiques'], 'sleep': ['Sommeil', 'Récupères-tu autant que tu t’entraînes ?'], 'challenges': ['Défis', 'Affronte le classement'] },
      t: {
        'sub.map': 'Anatomie sculptée en une seule surface continue, avec des sillons de définition entre les muscles. Touche une zone : elle s’illumine en rouge sur le corps.',
        'sub.planner': 'Ta routine du jour : saisis le poids, appuie sur ✓ et chaque kilo nourrit ton niveau d’athlète, tes RP et le panneau santé. Choisis les exercices dans la galerie ci-dessous.',
        'sub.library': '27 exercices aux calories réelles. Filtre par muscle, fais défiler la galerie, saisis le poids utilisé et appuie sur ✓ pour enregistrer la série — sans quitter la page. Touche une carte ❓ pour voir la technique correcte.',
        'sub.nutrition': 'Suis tes macros et enregistre tes repas avec la caméra : une IA locale analyse la photo et te propose des candidats à confirmer.',
        'sub.goal': 'Calcule les calories dont ton corps a besoin, choisis ton objectif — prendre, maintenir ou sécher — et fixe-le comme cible quotidienne de Nutrition.',
        'sub.diet': 'Choisis un plan et suis les menus, recettes et listes de courses.',
        'sub.bot': 'Fruits, graines, épices et céréales avec leurs vraies propriétés — pour que la nature travaille en faveur de ton plan.',
        'sub.med': 'Suis le cercle : il grandit quand tu inspires, se fige quand tu retiens, et se rétracte quand tu expires. Idéal pour les visuels.',
        'sub.freq': '19 fréquences générées en temps réel : tons Solfeggio, ondes binaurales et pulsations duales pour dormir, méditer, te concentrer ou activer ton esprit.',
        'sub.level': 'Chaque kilo enregistré dans ta routine ajoute du volume total. Passe de Débutant à Predator et apparais au classement.',
        'sub.progress': 'Tout ton progrès réuni : repas enregistrés, calories brûlées, volume soulevé et repos.',
        'sub.sleep': 'Le muscle se répare pendant ton sommeil. Enregistre tes heures et je te dis si c’est suffisant vu ce que tu as brûlé aujourd’hui.',
        'sub.chal': 'Affronte la communauté au volume total. Ton niveau et tes kilos apparaissent automatiquement au classement.',
        'pl.today': '✅ Ma routine du jour',
        'pl.saved': '✓ Routine enregistrée avec succès',
        'pl.kcal': '🔥 Calories estimées de la séance',
        'reco.burned': 'KCAL BRÛLÉES',
        'freq.t1': 'Solfeggio · tons purs',
        'freq.t2': 'Ondes cérébrales · binaurales',
        'freq.t3': 'Dual · pulsations 1–7 Hz 🎧',
        'freq.tip': '📱 iPhone : le son sort comme de la « musique », il joue donc même avec l’interrupteur silencieux — monte le volume avec les boutons latéraux. Si tu n’entends rien, appuie de nouveau sur « Lecture ».',
        'ph.food': 'Rechercher un aliment…',
        'ph.bot': 'Rechercher un aliment, nutriment ou bienfait…',
        'dyn.empty': 'Choisis des exercices dans la galerie ci-dessous ↓',
        'dyn.add': '＋ Ajouter à la routine',
        'dyn.inroutine': '✓ Dans la routine · retirer',
        'dyn.log100': '🍽 Enregistrer 100 g',
        'dyn.all': 'Tous',
        'dyn.basedon': 'Basé sur',
        'dyn.editweight': 'modifie ton poids dans le profil',
        'dyn.work': 'min de travail',
        'dyn.session': 'kcal / séance',
        "dyn.phones": "utilise des écouteurs",
        "dyn.missing": "Plus que",
        "dyn.forlevel": "pour"
      },
      tx: {
        "Pecho": "Poitrine",
        "Espalda": "Dos",
        "Hombros": "Épaules",
        "Bíceps": "Biceps",
        "Tríceps": "Triceps",
        "Abdominales": "Abdos",
        "Cuádriceps": "Quadriceps",
        "Glúteos": "Fessiers",
        "Gemelos": "Mollets",
        "Principiante": "Débutant",
        "Novato": "Novice",
        "Guerrero": "Guerrier",
        "Élite": "Élite",
        "Titán": "Titan",
        "Predator": "Predator",
        "🍽 kcal registradas": "🍽 kcal enregistrées",
        "🔥 kcal quemadas": "🔥 kcal brûlées",
        "🏋️ kg volumen hoy": "🏋️ kg volume aujourd’hui",
        "💧 ml de agua": "💧 ml d’eau",
        "😴 sueño anoche": "😴 sommeil cette nuit",
        "Atleta": "Athlète",
        "Nivel": "Niveau",
        "Kg totales": "Kg totaux",
        "⭐ Tú": "⭐ Toi",
        "😐 Ligero": "😐 Léger",
        "🙂 Normal": "🙂 Normal",
        "😴 Profundo": "😴 Profond",
        "Todas": "Toutes",
        "Frutas": "Fruits",
        "Verduras": "Légumes",
        "Semillas": "Graines",
        "Especias": "Épices",
        "Granos": "Céréales",
        "Volumen Limpio": "Prise de masse propre",
        "Definición + Volumen": "Sèche + Masse",
        "Ciclado de Carbos": "Cyclage des glucides",
        "Mediterránea": "Méditerranéenne",
        "Alivio Profundo": "Soulagement profond",
        "Relajación física y descarga de tensión": "Relaxation physique et relâchement des tensions",
        "Regeneración": "Régénération",
        "Sensación de restauración y equilibrio": "Sensation de restauration et d’équilibre",
        "Liberación": "Libération",
        "Suelta el miedo y la culpa; base emocional": "Lâche la peur et la culpabilité ; base émotionnelle",
        "Cambio": "Changement",
        "Facilita transiciones y deshace bloqueos": "Facilite les transitions et défait les blocages",
        "Armonía Natural": "Harmonie naturelle",
        "Afinación suave; calma y coherencia": "Accord doux ; calme et cohérence",
        "Reparación": "Réparation",
        "La \"frecuencia del amor\"; renovación y vitalidad": "La « fréquence de l’amour » ; renouveau et vitalité",
        "Conexión": "Connexion",
        "Relaciones, empatía y comunicación": "Relations, empathie et communication",
        "Despertar": "Éveil",
        "Intuición, claridad y expresión": "Intuition, clarté et expression",
        "Visión Interior": "Vision intérieure",
        "Orden mental y equilibrio espiritual": "Ordre mental et équilibre spirituel",
        "Consciencia Plena": "Pleine conscience",
        "Conexión superior y unidad": "Connexion supérieure et unité",
        "Delta · Sueño Profundo": "Delta · Sommeil profond",
        "Descanso nocturno y recuperación total": "Repos nocturne et récupération totale",
        "Theta baja · Sanación": "Thêta basse · Guérison",
        "Relajación muy profunda, pre-sueño": "Relaxation très profonde, avant le sommeil",
        "Theta · Meditación": "Thêta · Méditation",
        "Estados meditativos profundos y creatividad": "États méditatifs profonds et créativité",
        "Schumann · Tierra": "Schumann · Terre",
        "La resonancia de la Tierra; enraizamiento": "La résonance de la Terre ; enracinement",
        "Alpha · Relajación": "Alpha · Relaxation",
        "Calma alerta, ideal después de entrenar": "Calme alerte, idéal après l’entraînement",
        "Beta · Enfoque": "Bêta · Concentration",
        "Concentración estable para estudiar o trabajar": "Concentration stable pour étudier ou travailler",
        "Gamma · Despertar": "Gamma · Éveil",
        "Alerta máxima, claridad y procesamiento mental": "Vigilance maximale, clarté et traitement mental"
      },
      btns: { 'save-routine-btn': '💾 Enregistrer la routine', 'clear-routine-btn': '🗑 Vider', 'calc-btn': 'Calculer mes calories', 'sleep-save': 'Enregistrer la nuit', 'join-btn': 'Rejoindre le défi', 'mm-clear-btn': '✕ Effacer la sélection', 'scan-btn': '📷 Scanner avec la caméra', 'upload-btn': '🖼 Envoyer une photo', 'capture-btn': '📸 Capturer', 'stop-cam-btn': '⏹ Arrêter', 'breath-start': '▶ Démarrer', 'breath-stop': '⏹ Arrêter', 'freq-stop-btn': '⏹ Arrêter', 'login-btn': 'Se connecter', 'register-btn': 'S’inscrire', 'logout-btn': 'Se déconnecter' }
    }
  };

  (function extendI18N() {
    var addT = { en: {"freq.intro": "<strong>Use headphones</strong> (required for binaurals) and keep the volume gentle. These frequencies are a relaxation and wellbeing tool — they complement, not replace, rest, nutrition and training.", "ex.sets": "Sets", "ex.dur": "Estimated duration", "ex.met": "Intensity (MET)", "ex.cal": "Calories at your weight", "ex.tech": "📖 Correct technique", "ex.err": "⚠️ Common mistakes", "TX(ex.note)": "Master the pattern with light weight before adding load. Joint pain (unlike muscle burn) = stop and review your technique.", "ex.remove": "Remove from routine", "med.how": "🧘 How to do it", "med.min": "minutes · guided practice", "med.done": "✓ Mark as completed", "med.undo": "↺ Unmark", "med.timer": "⏱ Open breathing timer", "med.day": "Day", "med.DAY": "DAY", "med.dayDone": "completed", "dyn.week": "Week", "dyn.hint60": "— 60 weeks a year per plan, combined so they never repeat.", "th.day": "Day", "th.bre": "Breakfast", "th.lun": "Lunch", "th.sna": "Snack", "th.din": "Dinner"}, fr: {"freq.intro": "<strong>Utilise des écouteurs</strong> (obligatoire pour les binaurales) et un volume doux. Ces fréquences sont un outil de détente et de bien-être — elles complètent, sans remplacer, le repos, la nutrition et l’entraînement.", "ex.sets": "Séries", "ex.dur": "Durée estimée", "ex.met": "Intensité (MET)", "ex.cal": "Calories selon ton poids", "ex.tech": "📖 Technique correcte", "ex.err": "⚠️ Erreurs courantes", "TX(ex.note)": "Maîtrise le mouvement avec peu de poids avant de charger. Douleur articulaire (différente de la brûlure musculaire) = arrête et revois ta technique.", "ex.remove": "Retirer de la routine", "med.how": "🧘 Comment faire", "med.min": "minutes · pratique guidée", "med.done": "✓ Marquer comme terminé", "med.undo": "↺ Décocher", "med.timer": "⏱ Ouvrir le chrono respiration", "med.day": "Jour", "med.DAY": "JOUR", "med.dayDone": "terminé", "dyn.week": "Semaine", "dyn.hint60": "— 60 semaines par an et par plan, combinées pour ne jamais se répéter.", "th.day": "Jour", "th.bre": "Petit-déj", "th.lun": "Déjeuner", "th.sna": "Collation", "th.din": "Dîner"} };
    var addTX = { en: {"Toca un músculo del cuerpo o usa los botones · Arrastra para rotar · Pellizca para hacer zoom": "Tap a muscle on the body or use the buttons · Drag to rotate · Pinch to zoom", "Sexo": "Sex", "Edad": "Age", "Altura (cm)": "Height (cm)", "Peso (kg)": "Weight (kg)", "Actividad": "Activity", "Objetivo": "Goal", "Ciclos": "Cycles", "🔊 Volumen": "🔊 Volume", "⏱ Temporizador": "⏱ Timer", "Hombre": "Male", "Mujer": "Female", "Sedentario": "Sedentary", "Ligera (1-3 días/sem)": "Light (1-3 days/wk)", "Moderada (3-5 días/sem)": "Moderate (3-5 days/wk)", "Alta (6-7 días/sem)": "High (6-7 days/wk)", "Muy alta (atleta)": "Very high (athlete)", "Subir de peso (+400)": "Gain weight (+400)", "Mantener (0)": "Maintain (0)", "Mantener peso (0)": "Maintain weight (0)", "Definir (−400)": "Cut (−400)", "∞ Continuo": "∞ Continuous", "Semana 1": "Week 1", "Semana 2": "Week 2", "Semana 3": "Week 3", "Semana 4": "Week 4", "Semana 5": "Week 5", "Menú:": "Menu:", "Músculos": "Muscles", "Entrenamiento": "Training", "Nutrición": "Nutrition", "Planes": "Plans", "Botánica": "Botany", "Meditación": "Meditation", "Frecuencias": "Frequencies", "Progreso": "Progress", "Retos": "Challenges", "Sueño": "Sleep", "¿Listo para transformar tu cuerpo y tu mente?": "Ready to transform your body and mind?", "Todo lo que necesitas vive en esta página: entrena con técnica, come con datos, descansa mejor y mide tu progreso — gratis y sin apps.": "Everything you need lives on this page: train with technique, eat with data, rest better and track your progress — free, no apps.", "🏋️ Crear mi rutina ahora": "🏋️ Build my routine now", "🎯 Calcular mis calorías": "🎯 Calculate my calories", "Tu semana de sueño": "Your sleep week", "¿Cuántas horas dormiste anoche?": "How many hours did you sleep last night?", "🗓 Programa Mindfulness — 21 días": "🗓 Mindfulness Program — 21 days", "Un día = una práctica guiada. Toca cualquier día para ver las instrucciones paso a paso y márcalo al terminar — tu progreso se guarda.": "One day = one guided practice. Tap any day for step-by-step instructions and mark it when done — your progress is saved.", "completados": "done", "kg levantados en total": "kg lifted in total", "Meta": "Target", "Calorías hoy": "Calories today", "💧 Agua:": "💧 Water:", "ml sugeridos": "ml suggested", "Datos reales, cero mitos — aquí nada \"quema grasa\" por arte de magia 😉": "Real facts, zero myths — nothing here \"burns fat\" by magic 😉", "Usuario:": "User:", "Peso:": "Weight:", "Calorías diarias:": "Daily calories:", "Proteína": "Protein", "Carbos": "Carbs", "Carbohidratos": "Carbohydrates", "Grasas": "Fats", "Email": "Email", "Contraseña": "Password", "Peso corporal (kg) — para calcular tus calorías": "Body weight (kg) — to calculate your calories"}, fr: {"Toca un músculo del cuerpo o usa los botones · Arrastra para rotar · Pellizca para hacer zoom": "Touche un muscle du corps ou utilise les boutons · Glisse pour pivoter · Pince pour zoomer", "Sexo": "Sexe", "Edad": "Âge", "Altura (cm)": "Taille (cm)", "Peso (kg)": "Poids (kg)", "Actividad": "Activité", "Objetivo": "Objectif", "Ciclos": "Cycles", "🔊 Volumen": "🔊 Volume", "⏱ Temporizador": "⏱ Minuteur", "Hombre": "Homme", "Mujer": "Femme", "Sedentario": "Sédentaire", "Ligera (1-3 días/sem)": "Légère (1-3 j/sem)", "Moderada (3-5 días/sem)": "Modérée (3-5 j/sem)", "Alta (6-7 días/sem)": "Élevée (6-7 j/sem)", "Muy alta (atleta)": "Très élevée (athlète)", "Subir de peso (+400)": "Prendre du poids (+400)", "Mantener (0)": "Maintenir (0)", "Mantener peso (0)": "Maintenir le poids (0)", "Definir (−400)": "Sécher (−400)", "∞ Continuo": "∞ Continu", "Semana 1": "Semaine 1", "Semana 2": "Semaine 2", "Semana 3": "Semaine 3", "Semana 4": "Semaine 4", "Semana 5": "Semaine 5", "Menú:": "Menu :", "Músculos": "Muscles", "Entrenamiento": "Entraînement", "Nutrición": "Nutrition", "Planes": "Plans", "Botánica": "Botanique", "Meditación": "Méditation", "Frecuencias": "Fréquences", "Progreso": "Progrès", "Retos": "Défis", "Sueño": "Sommeil", "¿Listo para transformar tu cuerpo y tu mente?": "Prêt à transformer ton corps et ton esprit ?", "Todo lo que necesitas vive en esta página: entrena con técnica, come con datos, descansa mejor y mide tu progreso — gratis y sin apps.": "Tout ce dont tu as besoin vit sur cette page : entraîne-toi avec technique, mange avec des données, repose-toi mieux et mesure tes progrès — gratuit, sans applis.", "🏋️ Crear mi rutina ahora": "🏋️ Créer ma routine maintenant", "🎯 Calcular mis calorías": "🎯 Calculer mes calories", "Tu semana de sueño": "Ta semaine de sommeil", "¿Cuántas horas dormiste anoche?": "Combien d’heures as-tu dormi cette nuit ?", "🗓 Programa Mindfulness — 21 días": "🗓 Programme Mindfulness — 21 jours", "Un día = una práctica guiada. Toca cualquier día para ver las instrucciones paso a paso y márcalo al terminar — tu progreso se guarda.": "Un jour = une pratique guidée. Touche un jour pour voir les instructions pas à pas et coche-le une fois terminé — ta progression est enregistrée.", "completados": "terminés", "kg levantados en total": "kg soulevés au total", "Meta": "Objectif", "Calorías hoy": "Calories aujourd’hui", "💧 Agua:": "💧 Eau :", "ml sugeridos": "ml conseillés", "Datos reales, cero mitos — aquí nada \"quema grasa\" por arte de magia 😉": "Des faits réels, zéro mythe — ici rien ne « brûle les graisses » par magie 😉", "Usuario:": "Utilisateur :", "Peso:": "Poids :", "Calorías diarias:": "Calories quotidiennes :", "Proteína": "Protéines", "Carbos": "Glucides", "Carbohidratos": "Glucides", "Grasas": "Lipides", "Email": "E-mail", "Contraseña": "Mot de passe", "Peso corporal (kg) — para calcular tus calorías": "Poids corporel (kg) — pour calculer tes calories"} };
    ['en', 'fr'].forEach(function(l) {
      var o = I18N[l];
      Object.keys(addT[l]).forEach(function(k) { o.t[k] = addT[l][k]; });
      Object.keys(addTX[l]).forEach(function(k) { o.tx[k] = addTX[l][k]; });
    });
  })();


  (function extendI18N2() {
    var en2 = {"10 min": "10 min", "15 min": "15 min", "30 min": "30 min", "5 min": "5 min", "60 min": "60 min"};
    var fr2 = {"10 min": "10 min", "15 min": "15 min", "30 min": "30 min", "5 min": "5 min", "60 min": "60 min"};
    Object.keys(en2).forEach(function(k) { I18N.en.tx[k] = en2[k]; });
    Object.keys(fr2).forEach(function(k) { I18N.fr.tx[k] = fr2[k]; });
  })();


  (function extendI18N3() {
    var en3 = {"Librería de Ejercicios": "Exercise Library", "Piernas": "Legs", "Core": "Core", "Cardio": "Cardio", "Intermedio": "Intermediate", "Mantener": "Maintain", "Avanzado": "Advanced", "Enero": "January", "Febrero": "February", "Marzo": "March", "Abril": "April", "Mayo": "May", "Junio": "June", "Julio": "July", "Agosto": "August", "Septiembre": "September", "Octubre": "October", "Noviembre": "November", "Diciembre": "December", "Lun": "Mon", "Mar": "Tue", "Mié": "Wed", "Jue": "Thu", "Vie": "Fri", "Sáb": "Sat", "Dom": "Sun", "💪 Volumen Limpio – 4 semanas": "💪 Clean Bulk – 4 weeks", "2800-3200 kcal/día · Masa muscular sin grasa extra": "2800-3200 kcal/day · Muscle mass without extra fat", "⚖️ Definición + Volumen – 8 semanas": "⚖️ Cut + Bulk – 8 weeks", "Alterna fases: gana músculo y pierde grasa de forma sostenida": "Alternate phases: build muscle and lose fat sustainably", "🔄 Ciclado de Carbohidratos": "🔄 Carb Cycling", "Días altos en entreno pesado, días bajos en descanso": "High days for heavy training, low days for rest", "🇬🇷 Dieta Mediterránea Élite": "🇬🇷 Elite Mediterranean Diet", "La dieta más saludable del mundo, optimizada para atletas": "The world’s healthiest diet, optimized for athletes", "¿Cuál es tu tipo de cuerpo?": "What’s your body type?", "Ectomorfo": "Ectomorph", "Mesomorfo": "Mesomorph", "Endomorfo": "Endomorph", "Delgado, metabolismo rápido, le cuesta subir de peso.": "Slim, fast metabolism, struggles to gain weight.", "Atlético natural, gana músculo con facilidad.": "Naturally athletic, gains muscle easily.", "Estructura ancha, acumula grasa con facilidad.": "Broad frame, gains fat easily.", "<strong>Calorías:</strong> superávit de +300–500 kcal/día": "<strong>Calories:</strong> surplus of +300–500 kcal/day", "<strong>Macros:</strong> carbohidratos altos · 1.6–2 g/kg de proteína": "<strong>Macros:</strong> high carbs · 1.6–2 g/kg protein", "<strong>Entreno:</strong> básicos pesados (sentadilla, banca, peso muerto) y poco cardio": "<strong>Training:</strong> heavy compounds (squat, bench, deadlift) and little cardio", "<strong>Clave:</strong> 4–6 comidas al día; los batidos calóricos ayudan mucho": "<strong>Key:</strong> 4–6 meals a day; calorie shakes help a lot", "<strong>Calorías:</strong> mantenimiento o superávit ligero": "<strong>Calories:</strong> maintenance or a slight surplus", "<strong>Macros:</strong> balanceados · 1.6–2 g/kg de proteína": "<strong>Macros:</strong> balanced · 1.6–2 g/kg protein", "<strong>Entreno:</strong> fuerza + hipertrofia, cardio moderado": "<strong>Training:</strong> strength + hypertrophy, moderate cardio", "<strong>Clave:</strong> progresión constante de cargas (¡registra tus kilos!)": "<strong>Key:</strong> steady load progression (log your kilos!)", "<strong>Calorías:</strong> déficit de −300–500 kcal/día": "<strong>Calories:</strong> deficit of −300–500 kcal/day", "<strong>Macros:</strong> carbohidratos moderados · proteína alta (2 g/kg)": "<strong>Macros:</strong> moderate carbs · high protein (2 g/kg)", "<strong>Entreno:</strong> pesas + cardio regular (3-4×/semana)": "<strong>Training:</strong> weights + regular cardio (3-4×/week)", "<strong>Clave:</strong> constancia y control de porciones": "<strong>Key:</strong> consistency and portion control", "Ver plan para subir →": "See bulking plan →", "Ver plan equilibrado →": "See balanced plan →", "Ver plan de definición →": "See cutting plan →", "Los somatotipos son una guía orientativa, no categorías rígidas — la mayoría somos una mezcla. Estimaciones generales de bienestar, no consejo médico.": "Somatotypes are a rough guide, not rigid categories — most of us are a mix. General wellness estimates, not medical advice."};
    var fr3 = {"Librería de Ejercicios": "Bibliothèque d’exercices", "Piernas": "Jambes", "Core": "Core", "Cardio": "Cardio", "Intermedio": "Intermédiaire", "Mantener": "Maintenir", "Avanzado": "Avancé", "Enero": "Janvier", "Febrero": "Février", "Marzo": "Mars", "Abril": "Avril", "Mayo": "Mai", "Junio": "Juin", "Julio": "Juillet", "Agosto": "Août", "Septiembre": "Septembre", "Octubre": "Octobre", "Noviembre": "Novembre", "Diciembre": "Décembre", "Lun": "Lun", "Mar": "Mar", "Mié": "Mer", "Jue": "Jeu", "Vie": "Ven", "Sáb": "Sam", "Dom": "Dim", "💪 Volumen Limpio – 4 semanas": "💪 Prise de masse propre – 4 semaines", "2800-3200 kcal/día · Masa muscular sin grasa extra": "2800-3200 kcal/jour · Masse musculaire sans graisse superflue", "⚖️ Definición + Volumen – 8 semanas": "⚖️ Sèche + Masse – 8 semaines", "Alterna fases: gana músculo y pierde grasa de forma sostenida": "Alterne les phases : gagne du muscle et perds du gras durablement", "🔄 Ciclado de Carbohidratos": "🔄 Cyclage des glucides", "Días altos en entreno pesado, días bajos en descanso": "Jours hauts à l’entraînement lourd, jours bas au repos", "🇬🇷 Dieta Mediterránea Élite": "🇬🇷 Diète méditerranéenne élite", "La dieta más saludable del mundo, optimizada para atletas": "Le régime le plus sain du monde, optimisé pour les athlètes", "¿Cuál es tu tipo de cuerpo?": "Quel est ton type de corps ?", "Ectomorfo": "Ectomorphe", "Mesomorfo": "Mésomorphe", "Endomorfo": "Endomorphe", "Delgado, metabolismo rápido, le cuesta subir de peso.": "Mince, métabolisme rapide, du mal à prendre du poids.", "Atlético natural, gana músculo con facilidad.": "Athlétique naturel, prend du muscle facilement.", "Estructura ancha, acumula grasa con facilidad.": "Ossature large, stocke la graisse facilement.", "<strong>Calorías:</strong> superávit de +300–500 kcal/día": "<strong>Calories :</strong> surplus de +300–500 kcal/jour", "<strong>Macros:</strong> carbohidratos altos · 1.6–2 g/kg de proteína": "<strong>Macros :</strong> glucides élevés · 1,6–2 g/kg de protéines", "<strong>Entreno:</strong> básicos pesados (sentadilla, banca, peso muerto) y poco cardio": "<strong>Entraînement :</strong> polyarticulaires lourds (squat, développé, soulevé de terre) et peu de cardio", "<strong>Clave:</strong> 4–6 comidas al día; los batidos calóricos ayudan mucho": "<strong>Clé :</strong> 4–6 repas par jour ; les shakes caloriques aident beaucoup", "<strong>Calorías:</strong> mantenimiento o superávit ligero": "<strong>Calories :</strong> maintien ou léger surplus", "<strong>Macros:</strong> balanceados · 1.6–2 g/kg de proteína": "<strong>Macros :</strong> équilibrés · 1,6–2 g/kg de protéines", "<strong>Entreno:</strong> fuerza + hipertrofia, cardio moderado": "<strong>Entraînement :</strong> force + hypertrophie, cardio modéré", "<strong>Clave:</strong> progresión constante de cargas (¡registra tus kilos!)": "<strong>Clé :</strong> progression constante des charges (note tes kilos !)", "<strong>Calorías:</strong> déficit de −300–500 kcal/día": "<strong>Calories :</strong> déficit de −300–500 kcal/jour", "<strong>Macros:</strong> carbohidratos moderados · proteína alta (2 g/kg)": "<strong>Macros :</strong> glucides modérés · protéines élevées (2 g/kg)", "<strong>Entreno:</strong> pesas + cardio regular (3-4×/semana)": "<strong>Entraînement :</strong> musculation + cardio régulier (3-4×/semaine)", "<strong>Clave:</strong> constancia y control de porciones": "<strong>Clé :</strong> régularité et contrôle des portions", "Ver plan para subir →": "Voir le plan prise de masse →", "Ver plan equilibrado →": "Voir le plan équilibré →", "Ver plan de definición →": "Voir le plan sèche →", "Los somatotipos son una guía orientativa, no categorías rígidas — la mayoría somos una mezcla. Estimaciones generales de bienestar, no consejo médico.": "Les somatotypes sont un guide indicatif, pas des catégories rigides — la plupart d’entre nous sommes un mélange. Estimations générales de bien-être, pas un avis médical."};
    Object.keys(en3).forEach(function(k) { I18N.en.tx[k] = en3[k]; });
    Object.keys(fr3).forEach(function(k) { I18N.fr.tx[k] = fr3[k]; });
  })();


  (function extendI18N4() {
    var t4en = {"breath.ready": "Ready", "sleep.empty": "No entries yet — log your first night and your week will appear here.", "bot.nores": "No results — try another search.", "chal.join": "You’ve joined the 30-day plank challenge!", "dyn.added": "added", "sleep.guide": "<strong style=\"color:#fff\">💡 Quick guide</strong><br>\\n          Intense training days (&gt;500 kcal) call for ~8.5 h. Most adults need 7–9 h. Sleeping too little reduces muscle protein synthesis and raises next-day appetite."};
    var t4fr = {"breath.ready": "Prêt", "sleep.empty": "Aucun enregistrement — enregistre ta première nuit et ta semaine apparaîtra ici.", "bot.nores": "Aucun résultat — essaie une autre recherche.", "chal.join": "Tu as rejoint le défi planche 30 jours !", "dyn.added": "ajouté", "sleep.guide": "<strong style=\"color:#fff\">💡 Guide rapide</strong><br>\\n          Les jours d’entraînement intense (&gt;500 kcal) demandent ~8,5 h. La plupart des adultes ont besoin de 7–9 h. Dormir peu réduit la synthèse des protéines musculaires et augmente l’appétit du lendemain."};
    var en4 = {"🔥 Reto activo": "🔥 Active challenge", "30 Días de Plancha": "30-Day Plank", "Aumenta tu plancha 10 segundos cada día. Quedan 18 días.": "Add 10 seconds to your plank every day. 18 days left.", "Progreso comunitario": "Community progress", "1,247 de 1,860 participantes completaron el reto de hoy": "1,247 of 1,860 participants completed today’s challenge", "Leaderboard esta semana": "Leaderboard this week", "Tus Badges": "Your Badges", "Recetas destacadas": "Featured recipes", "Bowl Proteico Matutino": "Morning Protein Bowl", "Arroz con Pollo Fitness": "Fitness Chicken & Rice", "Salmón al Horno con Batata": "Baked Salmon with Sweet Potato", "Fase Volumen (Sem 1-4)": "Bulk Phase (Wk 1-4)", "Fase Definición (Sem 5-8)": "Cut Phase (Wk 5-8)", "2800-3200 kcal · 2g/kg proteína · 5g/kg carbos · 0.9g/kg grasas": "2800-3200 kcal · 2g/kg protein · 5g/kg carbs · 0.9g/kg fats", "2000-2400 kcal · 2.4g/kg proteína · 3g/kg carbos · 0.7g/kg grasas": "2000-2400 kcal · 2.4g/kg protein · 3g/kg carbs · 0.7g/kg fats", "Semana": "Week", "Kcal entreno": "Training kcal", "Kcal descanso": "Rest kcal", "4 · 7 · 8 — Anti-estrés": "4 · 7 · 8 — Anti-stress", "Caja 4 · 4 · 4 · 4 — Enfoque": "Box 4 · 4 · 4 · 4 — Focus", "Coherente 5 · 5 — Calma": "Coherent 5 · 5 — Calm", "Inhala 4s, retén 7s, exhala 8s. Perfecta antes de dormir.": "Inhale 4s, hold 7s, exhale 8s. Perfect before sleep.", "Cuatro fases iguales. La técnica de los Navy SEALs.": "Four equal phases. The Navy SEALs’ technique.", "Inhala 5s, exhala 5s. Equilibra el sistema nervioso.": "Inhale 5s, exhale 5s. Balances the nervous system.", "Inhala": "Inhale", "Retén": "Hold", "Exhala": "Exhale", "Pausa": "Pause", "Pre-cama opcional: caseína o yogur griego. Ajusta porciones a tu meta de la sección Objetivo.": "Optional pre-bed: casein or Greek yogurt. Adjust portions to your goal from the Goal section.", "Menú de la fase Definición (sem 5-8). En fase Volumen (sem 1-4) sube los carbohidratos de comida y cena ~+40%.": "Cut-phase menu (wk 5-8). In the Bulk phase (wk 1-4), raise lunch and dinner carbs by ~+40%.", "🔥 ALTO = día de entreno pesado (más carbos) · 🌙 BAJO = descanso o cardio suave (más grasas y proteína).": "🔥 HIGH = heavy training day (more carbs) · 🌙 LOW = rest or easy cardio (more fats and protein).", "EVOO como grasa principal · pescado azul 2-3×/semana · legumbres 3×/semana.": "EVOO as your main fat · oily fish 2-3×/week · legumes 3×/week.", "Valores aproximados por 100 g. Información general de bienestar — no sustituye consejo médico o nutricional profesional.": "Approximate values per 100 g. General wellness info — not a substitute for professional medical or nutrition advice.", "Campeón": "Champion", "Racha 7d": "7-day streak", "Fuerza": "Strength", "Zen": "Zen", "Sentadilla con barra": "Barbell squat", "Prensa de piernas": "Leg press", "Zancadas": "Lunges", "Extensión cuádriceps": "Leg extension", "Curl femoral": "Leg curl", "Hip thrust": "Hip thrust", "Elevación de gemelos": "Calf raise", "Press de banca": "Bench press", "Press inclinado": "Incline press", "Aperturas mancuerna": "Dumbbell flyes", "Fondos en paralelas": "Dips", "Dominadas": "Pull-ups", "Remo con barra": "Barbell row", "Jalón al pecho": "Lat pulldown", "Remo en polea baja": "Seated cable row", "Peso muerto": "Deadlift", "Press militar": "Overhead press", "Elevaciones laterales": "Lateral raises", "Face pull": "Face pull", "Curl de bíceps": "Biceps curl", "Curl martillo": "Hammer curl", "Extensión de tríceps": "Triceps extension", "Plancha": "Plank", "Crunch abdominal": "Crunch", "Elevación de piernas": "Leg raises", "Mountain climbers": "Mountain climbers", "Burpees": "Burpees", "¿Sabías que el pimiento rojo tiene más vitamina C que la naranja?": "Did you know red bell pepper has more vitamin C than oranges?", "¿Sabías que el licopeno del tomate se absorbe mejor cocinado con un poco de aceite?": "Did you know tomato lycopene absorbs better when cooked with a little oil?", "¿Sabías que el agua de coco aporta potasio y electrolitos naturales? Los cubitos con chía son solo una forma bonita de tomarla 😉": "Did you know coconut water provides potassium and natural electrolytes? Chia ice cubes are just a pretty way to drink it 😉", "¿Sabías que la curcumina de la cúrcuma se absorbe hasta 20× mejor con pimienta negra?": "Did you know turmeric’s curcumin absorbs up to 20× better with black pepper?", "¿Sabías que la avena contiene betaglucanos que ayudan a mantener el colesterol a raya?": "Did you know oats contain beta-glucans that help keep cholesterol in check?", "¿Sabías que la quinoa trae los 9 aminoácidos esenciales, como una proteína animal?": "Did you know quinoa provides all 9 essential amino acids, like an animal protein?", "¿Sabías que las cerezas concentran antocianinas que se estudian para la recuperación muscular?": "Did you know cherries pack anthocyanins being studied for muscle recovery?", "¿Sabías que la espinaca aporta nitratos que tu cuerpo usa para oxigenar el músculo?": "Did you know spinach provides nitrates your body uses to oxygenate muscle?", "¿Sabías que 30 g de pepitas de calabaza cubren buena parte del magnesio del día?": "Did you know 30 g of pumpkin seeds cover a good share of your daily magnesium?", "¿Sabías que pelar pistachos te hace comer más despacio y sentirte más lleno?": "Did you know shelling pistachios makes you eat slower and feel fuller?", "Sandía": "Watermelon", "Agua 92%, licopeno, citrulina": "92% water, lycopene, citrulline", "Hidratación y antioxidantes para recuperar tras entrenar": "Hydration and antioxidants to recover after training", "Post-entreno o snack; la sal solo aporta sabor y sodio — no quema grasa": "Post-workout or snack; salt only adds flavor and sodium — it doesn’t burn fat", "Plátano": "Banana", "Potasio, B6, carbos rápidos": "Potassium, B6, fast carbs", "Energía inmediata y función muscular (calambres)": "Instant energy and muscle function (cramps)", "Pre-entreno o en batidos": "Pre-workout or in shakes", "Arándanos": "Blueberries", "Antocianinas, vitamina C": "Anthocyanins, vitamin C", "Antioxidantes; apoyo cognitivo y vascular": "Antioxidants; cognitive and vascular support", "Con yogur o avena": "With yogurt or oats", "Manzana": "Apple", "Pectina (fibra), polifenoles": "Pectin (fiber), polyphenols", "Saciedad y salud intestinal": "Satiety and gut health", "Snack con un puñado de maní": "Snack with a handful of peanuts", "Aguacate": "Avocado", "Grasas monoinsaturadas, potasio": "Monounsaturated fats, potassium", "Salud cardiovascular; mejora absorción de vitaminas A-D-E-K": "Heart health; boosts absorption of vitamins A-D-E-K", "En tostadas o ensaladas": "On toast or salads", "Naranja": "Orange", "Vitamina C, folato": "Vitamin C, folate", "Inmunidad y síntesis de colágeno": "Immunity and collagen synthesis", "Entera mejor que en jugo (conserva la fibra)": "Whole beats juice (keeps the fiber)", "Piña": "Pineapple", "Bromelina, vitamina C": "Bromelain, vitamin C", "Apoya la digestión de proteínas": "Supports protein digestion", "Postre tras comidas altas en proteína": "Dessert after protein-rich meals", "Mango": "Mango", "Vitaminas A y C": "Vitamins A and C", "Piel, visión e inmunidad": "Skin, vision and immunity", "Snack o en smoothie": "Snack or in a smoothie", "Espinaca": "Spinach", "Hierro, folato, nitratos": "Iron, folate, nitrates", "Transporte de oxígeno y rendimiento": "Oxygen transport and performance", "Salteada o camuflada en batidos": "Sautéed or hidden in shakes", "Brócoli": "Broccoli", "Sulforafano, fibra, vit C": "Sulforaphane, fiber, vit C", "Antioxidante estrella y saciedad": "Star antioxidant and satiety", "Al vapor 3-4 min (no lo hiervas de más)": "Steam 3-4 min (don’t overboil)", "Zanahoria": "Carrot", "Betacaroteno": "Beta-carotene", "Visión y piel": "Vision and skin", "Cruda con hummus": "Raw with hummus", "Tomate": "Tomato", "Licopeno (aumenta al cocinar)": "Lycopene (rises when cooked)", "Salud cardiovascular": "Cardiovascular health", "Salsa casera con EVOO": "Homemade sauce with EVOO", "Pimiento": "Bell pepper", "Más vitamina C que la naranja": "More vitamin C than oranges", "Inmunidad y colágeno": "Immunity and collagen", "Crudo en ensalada o salteado": "Raw in salads or sautéed", "Ajo": "Garlic", "Alicina": "Allicin", "Apoyo cardiovascular e inmune": "Cardiovascular and immune support", "Picado y reposado 10 min antes de cocinar": "Chopped and rested 10 min before cooking", "Jengibre": "Ginger", "Gingerol": "Gingerol", "Náuseas y molestias digestivas": "Nausea and digestive discomfort", "En té o rallado en comidas": "In tea or grated into meals", "Chía": "Chia", "Omega-3 (ALA), 34g de fibra": "Omega-3 (ALA), 34g fiber", "1 cda hidratada en agua o yogur": "1 tbsp soaked in water or yogurt", "Linaza": "Flaxseed", "Omega-3, lignanos": "Omega-3, lignans", "Corazón y regularidad digestiva": "Heart and digestive regularity", "Molida (1 cda) en avena o batidos": "Ground (1 tbsp) in oats or shakes", "Pepitas de calabaza": "Pumpkin seeds", "Magnesio, zinc": "Magnesium, zinc", "Sueño reparador e inmunidad": "Restful sleep and immunity", "Puñado (25-30g) o en ensaladas": "A handful (25-30g) or in salads", "Semillas de girasol": "Sunflower seeds", "Vitamina E, selenio": "Vitamin E, selenium", "Protección antioxidante celular": "Cellular antioxidant protection", "Puñado o en pan casero": "A handful or in homemade bread", "Almendras": "Almonds", "Vitamina E, magnesio, proteína": "Vitamin E, magnesium, protein", "Corazón y saciedad entre comidas": "Heart health and satiety between meals", "20-30g como colación": "20-30g as a snack", "Maní": "Peanuts", "26g de proteína, niacina": "26g protein, niacin", "Proteína y energía económicas": "Budget-friendly protein and energy", "Mantequilla natural sin azúcar añadida": "Natural butter with no added sugar", "Cúrcuma": "Turmeric", "Curcumina": "Curcumin", "Antiinflamatorio suave (se absorbe mejor con pimienta negra)": "Mild anti-inflammatory (absorbs better with black pepper)", "En arroces, guisos o leche dorada": "In rice, stews or golden milk", "Canela": "Cinnamon", "Polifenoles": "Polyphenols", "Apoyo modesto al control de la glucosa": "Modest support for glucose control", "En avena, café o yogur": "In oats, coffee or yogurt", "Cacao puro": "Pure cocoa", "Flavanoles, magnesio": "Flavanols, magnesium", "Ánimo y salud vascular": "Mood and vascular health", "En polvo sin azúcar o chocolate 85%+": "Unsweetened powder or 85%+ chocolate", "Té verde": "Green tea", "Catequinas (EGCG), L-teanina": "Catechins (EGCG), L-theanine", "Enfoque calmado y antioxidantes": "Calm focus and antioxidants", "2-3 tazas; evítalo tarde-noche": "2-3 cups; avoid it late evening", "Menta": "Mint", "Mentol": "Menthol", "Alivio digestivo y frescura": "Digestive relief and freshness", "Infusión después de comer": "Infusion after meals", "Avena": "Oats", "Betaglucanos": "Beta-glucans", "Colesterol bajo control y energía sostenida": "Cholesterol in check and steady energy", "La base de tus desayunos de plan": "The base of your plan breakfasts", "Quinoa": "Quinoa", "Proteína completa (14g)": "Complete protein (14g)", "Los 9 aminoácidos esenciales en un grano": "All 9 essential amino acids in one grain", "Sustituye al arroz 1:1": "Swap for rice 1:1", "Lentejas": "Lentils", "Hierro, 9g proteína, fibra": "Iron, 9g protein, fiber", "Energía estable y salud intestinal": "Steady energy and gut health", "En guisos o ensaladas frías": "In stews or cold salads", "Garbanzos": "Chickpeas", "Proteína + fibra": "Protein + fiber", "Saciedad prolongada": "Long-lasting satiety", "Hummus o tostados al horno": "Hummus or oven-roasted", "Arroz integral": "Brown rice", "Carbos complejos, magnesio": "Complex carbs, magnesium", "El combustible de tus entrenos": "The fuel for your workouts", "Comida pre o post entreno": "Pre- or post-workout meal", "Fresas": "Strawberries", "Vitamina C, manganeso": "Vitamin C, manganese", "Antioxidantes con muy pocas calorías": "Antioxidants with very few calories", "Kiwi": "Kiwi", "Vit C, actinidina": "Vit C, actinidin", "Digestión de proteínas e inmunidad": "Protein digestion and immunity", "Postre tras una cena proteica": "Dessert after a protein dinner", "Uvas": "Grapes", "Polifenoles (resveratrol)": "Polyphenols (resveratrol)", "Salud vascular": "Vascular health", "Congeladas como snack fresco": "Frozen as a cool snack", "Limón": "Lemon", "Vitamina C": "Vitamin C", "Sabor sin calorías; te ayuda a beber más agua": "Flavor without calories; helps you drink more water", "En agua o aliños": "In water or dressings", "Cerezas": "Cherries", "Antocianinas": "Anthocyanins", "Se estudian para la recuperación muscular": "Studied for muscle recovery", "Puñado post-entreno": "A handful post-workout", "Coco": "Coconut", "MCT; su agua aporta potasio": "MCTs; its water provides potassium", "El agua de coco es un electrolito natural": "Coconut water is a natural electrolyte", "Agua de coco post-entreno (los cubitos con chía son solo presentación 😉)": "Coconut water post-workout (chia ice cubes are just for looks 😉)", "Pepino": "Cucumber", "Agua 96%": "96% water", "Hidratación y volumen sin calorías": "Hydration and volume without calories", "En ensaladas o con hummus": "In salads or with hummus", "Cebolla": "Onion", "Quercetina": "Quercetin", "Antioxidante y mucho sabor con pocas kcal": "Antioxidant and big flavor for few kcal", "Base de guisos y salteados": "The base of stews and stir-fries", "Champiñón": "Mushroom", "Selenio; vit D si toma sol": "Selenium; vit D if sun-exposed", "Umami saciante y ligerísimo": "Filling, ultra-light umami", "Salteado o a la plancha": "Sautéed or grilled", "Batata": "Sweet potato", "Betacaroteno, carbos complejos": "Beta-carotene, complex carbs", "Energía estable para entrenar": "Steady energy for training", "Asada pre o post entreno": "Roasted pre- or post-workout", "Berenjena": "Eggplant", "Nasunina, fibra": "Nasunin, fiber", "Antioxidante y saciante": "Antioxidant and filling", "Asada o en pisto": "Roasted or in ratatouille", "Maíz": "Corn", "Luteína, fibra": "Lutein, fiber", "Vista y energía": "Vision and energy", "En ensaladas o mazorca": "In salads or on the cob", "Nueces": "Walnuts", "Omega-3 (ALA) líder en frutos secos": "Top omega-3 (ALA) among nuts", "Cerebro y corazón": "Brain and heart", "4-6 nueces al día": "4-6 walnuts a day", "Sésamo": "Sesame", "Calcio, lignanos": "Calcium, lignans", "Huesos y aroma tostado": "Bones and a toasty aroma", "Tahini o espolvoreado": "Tahini or sprinkled on top", "Pistachos": "Pistachios", "Proteína, luteína": "Protein, lutein", "Pelarlos te hace comer más despacio": "Shelling them makes you eat slower", "30g con cáscara como snack": "30g in-shell as a snack", "Pimienta negra": "Black pepper", "Piperina": "Piperine", "Multiplica la absorción de la curcumina": "Multiplies curcumin absorption", "Siempre junto a la cúrcuma": "Always alongside turmeric", "Orégano": "Oregano", "Carvacrol": "Carvacrol", "Especia muy antioxidante": "A highly antioxidant spice", "En salsas y proteínas": "In sauces and proteins", "Miel": "Honey", "Azúcares naturales": "Natural sugars", "Energía rápida — sigue siendo azúcar, con medida": "Quick energy — still sugar, in moderation", "1 cdita pre-entreno o en avena": "1 tsp pre-workout or in oats", "Manzanilla": "Chamomile", "Apigenina": "Apigenin", "Relajación; aliada del sueño": "Relaxation; a sleep ally", "Infusión 30-60 min antes de dormir": "Infusion 30-60 min before bed", "Romero": "Rosemary", "Ácido rosmarínico": "Rosmarinic acid", "Aroma asociado a alerta y memoria": "An aroma linked to alertness and memory", "En carnes, papas y aceites": "On meats, potatoes and oils", "Pan integral": "Whole-grain bread", "Fibra, vitaminas B": "Fiber, B vitamins", "El carbohidrato cotidiano, con su fibra": "Your everyday carb, fiber included", "Tostadas del desayuno": "Breakfast toast", "Pasta integral": "Whole-grain pasta", "Carbos de absorción media": "Medium-absorption carbs", "Combustible clásico del deportista": "The athlete’s classic fuel", "Comida pre-entreno (kcal en cocido)": "Pre-workout meal (kcal cooked)", "Edamame": "Edamame", "Proteína vegetal completa": "Complete plant protein", "De las mejores proteínas verdes": "One of the best green proteins", "Al vapor con sal marina": "Steamed with sea salt", "Frijoles negros": "Black beans", "Antocianinas, hierro, fibra": "Anthocyanins, iron, fiber", "Energía y salud intestinal": "Energy and gut health", "En bowls con arroz": "In bowls with rice"};
    var fr4 = {"🔥 Reto activo": "🔥 Défi actif", "30 Días de Plancha": "Planche 30 jours", "Aumenta tu plancha 10 segundos cada día. Quedan 18 días.": "Ajoute 10 secondes à ta planche chaque jour. Il reste 18 jours.", "Progreso comunitario": "Progression communautaire", "1,247 de 1,860 participantes completaron el reto de hoy": "1 247 sur 1 860 participants ont complété le défi du jour", "Leaderboard esta semana": "Classement de la semaine", "Tus Badges": "Tes badges", "Recetas destacadas": "Recettes vedettes", "Bowl Proteico Matutino": "Bol protéiné du matin", "Arroz con Pollo Fitness": "Riz au poulet fitness", "Salmón al Horno con Batata": "Saumon au four et patate douce", "Fase Volumen (Sem 1-4)": "Phase Masse (Sem 1-4)", "Fase Definición (Sem 5-8)": "Phase Sèche (Sem 5-8)", "2800-3200 kcal · 2g/kg proteína · 5g/kg carbos · 0.9g/kg grasas": "2800-3200 kcal · 2 g/kg protéines · 5 g/kg glucides · 0,9 g/kg lipides", "2000-2400 kcal · 2.4g/kg proteína · 3g/kg carbos · 0.7g/kg grasas": "2000-2400 kcal · 2,4 g/kg protéines · 3 g/kg glucides · 0,7 g/kg lipides", "Semana": "Semaine", "Kcal entreno": "Kcal entraînement", "Kcal descanso": "Kcal repos", "4 · 7 · 8 — Anti-estrés": "4 · 7 · 8 — Anti-stress", "Caja 4 · 4 · 4 · 4 — Enfoque": "Carrée 4 · 4 · 4 · 4 — Focus", "Coherente 5 · 5 — Calma": "Cohérente 5 · 5 — Calme", "Inhala 4s, retén 7s, exhala 8s. Perfecta antes de dormir.": "Inspire 4s, retiens 7s, expire 8s. Parfaite avant de dormir.", "Cuatro fases iguales. La técnica de los Navy SEALs.": "Quatre phases égales. La technique des Navy SEALs.", "Inhala 5s, exhala 5s. Equilibra el sistema nervioso.": "Inspire 5s, expire 5s. Équilibre le système nerveux.", "Inhala": "Inspire", "Retén": "Retiens", "Exhala": "Expire", "Pausa": "Pause", "Pre-cama opcional: caseína o yogur griego. Ajusta porciones a tu meta de la sección Objetivo.": "Avant le coucher (optionnel) : caséine ou yaourt grec. Ajuste les portions à ton objectif de la section Objectif.", "Menú de la fase Definición (sem 5-8). En fase Volumen (sem 1-4) sube los carbohidratos de comida y cena ~+40%.": "Menu de la phase Sèche (sem 5-8). En phase Masse (sem 1-4), augmente les glucides du déjeuner et du dîner d’environ +40 %.", "🔥 ALTO = día de entreno pesado (más carbos) · 🌙 BAJO = descanso o cardio suave (más grasas y proteína).": "🔥 HAUT = jour d’entraînement lourd (plus de glucides) · 🌙 BAS = repos ou cardio léger (plus de lipides et protéines).", "EVOO como grasa principal · pescado azul 2-3×/semana · legumbres 3×/semana.": "EVOO comme graisse principale · poisson gras 2-3×/semaine · légumineuses 3×/semaine.", "Valores aproximados por 100 g. Información general de bienestar — no sustituye consejo médico o nutricional profesional.": "Valeurs approximatives pour 100 g. Informations générales de bien-être — ne remplace pas un avis médical ou nutritionnel professionnel.", "Campeón": "Champion", "Racha 7d": "Série 7 j", "Fuerza": "Force", "Zen": "Zen", "Sentadilla con barra": "Squat barre", "Prensa de piernas": "Presse à cuisses", "Zancadas": "Fentes", "Extensión cuádriceps": "Extension quadriceps", "Curl femoral": "Leg curl", "Hip thrust": "Hip thrust", "Elevación de gemelos": "Élévation mollets", "Press de banca": "Développé couché", "Press inclinado": "Développé incliné", "Aperturas mancuerna": "Écartés haltères", "Fondos en paralelas": "Dips", "Dominadas": "Tractions", "Remo con barra": "Rowing barre", "Jalón al pecho": "Tirage poitrine", "Remo en polea baja": "Rowing poulie basse", "Peso muerto": "Soulevé de terre", "Press militar": "Développé militaire", "Elevaciones laterales": "Élévations latérales", "Face pull": "Face pull", "Curl de bíceps": "Curl biceps", "Curl martillo": "Curl marteau", "Extensión de tríceps": "Extension triceps", "Plancha": "Planche", "Crunch abdominal": "Crunch", "Elevación de piernas": "Relevés de jambes", "Mountain climbers": "Mountain climbers", "Burpees": "Burpees", "¿Sabías que el pimiento rojo tiene más vitamina C que la naranja?": "Savais-tu que le poivron rouge contient plus de vitamine C que l’orange ?", "¿Sabías que el licopeno del tomate se absorbe mejor cocinado con un poco de aceite?": "Savais-tu que le lycopène de la tomate s’absorbe mieux cuit avec un peu d’huile ?", "¿Sabías que el agua de coco aporta potasio y electrolitos naturales? Los cubitos con chía son solo una forma bonita de tomarla 😉": "Savais-tu que l’eau de coco apporte potassium et électrolytes naturels ? Les glaçons au chia ne sont qu’une jolie façon de la boire 😉", "¿Sabías que la curcumina de la cúrcuma se absorbe hasta 20× mejor con pimienta negra?": "Savais-tu que la curcumine du curcuma s’absorbe jusqu’à 20× mieux avec du poivre noir ?", "¿Sabías que la avena contiene betaglucanos que ayudan a mantener el colesterol a raya?": "Savais-tu que l’avoine contient des bêta-glucanes qui aident à contrôler le cholestérol ?", "¿Sabías que la quinoa trae los 9 aminoácidos esenciales, como una proteína animal?": "Savais-tu que le quinoa apporte les 9 acides aminés essentiels, comme une protéine animale ?", "¿Sabías que las cerezas concentran antocianinas que se estudian para la recuperación muscular?": "Savais-tu que les cerises concentrent des anthocyanes étudiées pour la récupération musculaire ?", "¿Sabías que la espinaca aporta nitratos que tu cuerpo usa para oxigenar el músculo?": "Savais-tu que l’épinard apporte des nitrates que ton corps utilise pour oxygéner le muscle ?", "¿Sabías que 30 g de pepitas de calabaza cubren buena parte del magnesio del día?": "Savais-tu que 30 g de graines de courge couvrent une bonne part du magnésium quotidien ?", "¿Sabías que pelar pistachos te hace comer más despacio y sentirte más lleno?": "Savais-tu qu’écosser les pistaches te fait manger plus lentement et te sentir plus rassasié ?", "Sandía": "Pastèque", "Agua 92%, licopeno, citrulina": "Eau 92 %, lycopène, citrulline", "Hidratación y antioxidantes para recuperar tras entrenar": "Hydratation et antioxydants pour récupérer après l’entraînement", "Post-entreno o snack; la sal solo aporta sabor y sodio — no quema grasa": "Post-entraînement ou en-cas ; le sel n’apporte que goût et sodium — il ne brûle pas de graisse", "Plátano": "Banane", "Potasio, B6, carbos rápidos": "Potassium, B6, glucides rapides", "Energía inmediata y función muscular (calambres)": "Énergie immédiate et fonction musculaire (crampes)", "Pre-entreno o en batidos": "Avant l’entraînement ou en shake", "Arándanos": "Myrtilles", "Antocianinas, vitamina C": "Anthocyanes, vitamine C", "Antioxidantes; apoyo cognitivo y vascular": "Antioxydants ; soutien cognitif et vasculaire", "Con yogur o avena": "Avec yaourt ou avoine", "Manzana": "Pomme", "Pectina (fibra), polifenoles": "Pectine (fibre), polyphénols", "Saciedad y salud intestinal": "Satiété et santé intestinale", "Snack con un puñado de maní": "En-cas avec une poignée de cacahuètes", "Aguacate": "Avocat", "Grasas monoinsaturadas, potasio": "Graisses mono-insaturées, potassium", "Salud cardiovascular; mejora absorción de vitaminas A-D-E-K": "Santé cardiaque ; améliore l’absorption des vitamines A-D-E-K", "En tostadas o ensaladas": "Sur toasts ou salades", "Naranja": "Orange", "Vitamina C, folato": "Vitamine C, folate", "Inmunidad y síntesis de colágeno": "Immunité et synthèse du collagène", "Entera mejor que en jugo (conserva la fibra)": "Entière plutôt qu’en jus (garde la fibre)", "Piña": "Ananas", "Bromelina, vitamina C": "Bromélaïne, vitamine C", "Apoya la digestión de proteínas": "Soutient la digestion des protéines", "Postre tras comidas altas en proteína": "Dessert après un repas riche en protéines", "Mango": "Mangue", "Vitaminas A y C": "Vitamines A et C", "Piel, visión e inmunidad": "Peau, vision et immunité", "Snack o en smoothie": "En-cas ou en smoothie", "Espinaca": "Épinard", "Hierro, folato, nitratos": "Fer, folate, nitrates", "Transporte de oxígeno y rendimiento": "Transport de l’oxygène et performance", "Salteada o camuflada en batidos": "Sautée ou cachée dans les shakes", "Brócoli": "Brocoli", "Sulforafano, fibra, vit C": "Sulforaphane, fibre, vit C", "Antioxidante estrella y saciedad": "Antioxydant star et satiété", "Al vapor 3-4 min (no lo hiervas de más)": "À la vapeur 3-4 min (ne le surcuis pas)", "Zanahoria": "Carotte", "Betacaroteno": "Bêta-carotène", "Visión y piel": "Vision et peau", "Cruda con hummus": "Crue avec du houmous", "Tomate": "Tomate", "Licopeno (aumenta al cocinar)": "Lycopène (augmente à la cuisson)", "Salud cardiovascular": "Santé cardiovasculaire", "Salsa casera con EVOO": "Sauce maison à l’EVOO", "Pimiento": "Poivron", "Más vitamina C que la naranja": "Plus de vitamine C que l’orange", "Inmunidad y colágeno": "Immunité et collagène", "Crudo en ensalada o salteado": "Cru en salade ou sauté", "Ajo": "Ail", "Alicina": "Allicine", "Apoyo cardiovascular e inmune": "Soutien cardiovasculaire et immunitaire", "Picado y reposado 10 min antes de cocinar": "Haché et reposé 10 min avant cuisson", "Jengibre": "Gingembre", "Gingerol": "Gingérol", "Náuseas y molestias digestivas": "Nausées et inconfort digestif", "En té o rallado en comidas": "En thé ou râpé dans les plats", "Chía": "Chia", "Omega-3 (ALA), 34g de fibra": "Oméga-3 (ALA), 34 g de fibres", "1 cda hidratada en agua o yogur": "1 c. à s. hydratée dans l’eau ou le yaourt", "Linaza": "Lin", "Omega-3, lignanos": "Oméga-3, lignanes", "Corazón y regularidad digestiva": "Cœur et régularité digestive", "Molida (1 cda) en avena o batidos": "Moulue (1 c. à s.) dans l’avoine ou les shakes", "Pepitas de calabaza": "Graines de courge", "Magnesio, zinc": "Magnésium, zinc", "Sueño reparador e inmunidad": "Sommeil réparateur et immunité", "Puñado (25-30g) o en ensaladas": "Une poignée (25-30 g) ou en salade", "Semillas de girasol": "Graines de tournesol", "Vitamina E, selenio": "Vitamine E, sélénium", "Protección antioxidante celular": "Protection antioxydante cellulaire", "Puñado o en pan casero": "Une poignée ou dans le pain maison", "Almendras": "Amandes", "Vitamina E, magnesio, proteína": "Vitamine E, magnésium, protéines", "Corazón y saciedad entre comidas": "Cœur et satiété entre les repas", "20-30g como colación": "20-30 g en collation", "Maní": "Cacahuètes", "26g de proteína, niacina": "26 g de protéines, niacine", "Proteína y energía económicas": "Protéines et énergie économiques", "Mantequilla natural sin azúcar añadida": "Beurre naturel sans sucre ajouté", "Cúrcuma": "Curcuma", "Curcumina": "Curcumine", "Antiinflamatorio suave (se absorbe mejor con pimienta negra)": "Anti-inflammatoire doux (mieux absorbé avec du poivre noir)", "En arroces, guisos o leche dorada": "Dans riz, ragoûts ou lait d’or", "Canela": "Cannelle", "Polifenoles": "Polyphénols", "Apoyo modesto al control de la glucosa": "Soutien modeste du contrôle de la glycémie", "En avena, café o yogur": "Dans l’avoine, le café ou le yaourt", "Cacao puro": "Cacao pur", "Flavanoles, magnesio": "Flavanols, magnésium", "Ánimo y salud vascular": "Humeur et santé vasculaire", "En polvo sin azúcar o chocolate 85%+": "En poudre sans sucre ou chocolat 85 %+", "Té verde": "Thé vert", "Catequinas (EGCG), L-teanina": "Catéchines (EGCG), L-théanine", "Enfoque calmado y antioxidantes": "Concentration calme et antioxydants", "2-3 tazas; evítalo tarde-noche": "2-3 tasses ; évite-le en soirée", "Menta": "Menthe", "Mentol": "Menthol", "Alivio digestivo y frescura": "Soulagement digestif et fraîcheur", "Infusión después de comer": "Infusion après les repas", "Avena": "Avoine", "Betaglucanos": "Bêta-glucanes", "Colesterol bajo control y energía sostenida": "Cholestérol maîtrisé et énergie durable", "La base de tus desayunos de plan": "La base de tes petits-déjeuners du plan", "Quinoa": "Quinoa", "Proteína completa (14g)": "Protéine complète (14 g)", "Los 9 aminoácidos esenciales en un grano": "Les 9 acides aminés essentiels dans un grain", "Sustituye al arroz 1:1": "Remplace le riz 1:1", "Lentejas": "Lentilles", "Hierro, 9g proteína, fibra": "Fer, 9 g de protéines, fibres", "Energía estable y salud intestinal": "Énergie stable et santé intestinale", "En guisos o ensaladas frías": "En ragoûts ou salades froides", "Garbanzos": "Pois chiches", "Proteína + fibra": "Protéines + fibres", "Saciedad prolongada": "Satiété prolongée", "Hummus o tostados al horno": "Houmous ou rôtis au four", "Arroz integral": "Riz complet", "Carbos complejos, magnesio": "Glucides complexes, magnésium", "El combustible de tus entrenos": "Le carburant de tes entraînements", "Comida pre o post entreno": "Repas avant ou après l’entraînement", "Fresas": "Fraises", "Vitamina C, manganeso": "Vitamine C, manganèse", "Antioxidantes con muy pocas calorías": "Antioxydants avec très peu de calories", "Kiwi": "Kiwi", "Vit C, actinidina": "Vit C, actinidine", "Digestión de proteínas e inmunidad": "Digestion des protéines et immunité", "Postre tras una cena proteica": "Dessert après un dîner protéiné", "Uvas": "Raisins", "Polifenoles (resveratrol)": "Polyphénols (resvératrol)", "Salud vascular": "Santé vasculaire", "Congeladas como snack fresco": "Congelés en en-cas frais", "Limón": "Citron", "Vitamina C": "Vitamine C", "Sabor sin calorías; te ayuda a beber más agua": "Du goût sans calories ; aide à boire plus d’eau", "En agua o aliños": "Dans l’eau ou les vinaigrettes", "Cerezas": "Cerises", "Antocianinas": "Anthocyanes", "Se estudian para la recuperación muscular": "Étudiées pour la récupération musculaire", "Puñado post-entreno": "Une poignée après l’entraînement", "Coco": "Noix de coco", "MCT; su agua aporta potasio": "TCM ; son eau apporte du potassium", "El agua de coco es un electrolito natural": "L’eau de coco est un électrolyte naturel", "Agua de coco post-entreno (los cubitos con chía son solo presentación 😉)": "Eau de coco après l’entraînement (les glaçons au chia, c’est juste pour le style 😉)", "Pepino": "Concombre", "Agua 96%": "Eau 96 %", "Hidratación y volumen sin calorías": "Hydratation et volume sans calories", "En ensaladas o con hummus": "En salade ou avec du houmous", "Cebolla": "Oignon", "Quercetina": "Quercétine", "Antioxidante y mucho sabor con pocas kcal": "Antioxydant et beaucoup de goût pour peu de kcal", "Base de guisos y salteados": "Base des ragoûts et sautés", "Champiñón": "Champignon", "Selenio; vit D si toma sol": "Sélénium ; vit D s’il voit le soleil", "Umami saciante y ligerísimo": "Umami rassasiant et ultra-léger", "Salteado o a la plancha": "Sauté ou grillé", "Batata": "Patate douce", "Betacaroteno, carbos complejos": "Bêta-carotène, glucides complexes", "Energía estable para entrenar": "Énergie stable pour t’entraîner", "Asada pre o post entreno": "Rôtie avant ou après l’entraînement", "Berenjena": "Aubergine", "Nasunina, fibra": "Nasunine, fibres", "Antioxidante y saciante": "Antioxydante et rassasiante", "Asada o en pisto": "Rôtie ou en ratatouille", "Maíz": "Maïs", "Luteína, fibra": "Lutéine, fibres", "Vista y energía": "Vue et énergie", "En ensaladas o mazorca": "En salade ou en épi", "Nueces": "Noix", "Omega-3 (ALA) líder en frutos secos": "Oméga-3 (ALA) leader des fruits à coque", "Cerebro y corazón": "Cerveau et cœur", "4-6 nueces al día": "4-6 noix par jour", "Sésamo": "Sésame", "Calcio, lignanos": "Calcium, lignanes", "Huesos y aroma tostado": "Os et arôme grillé", "Tahini o espolvoreado": "Tahini ou saupoudré", "Pistachos": "Pistaches", "Proteína, luteína": "Protéines, lutéine", "Pelarlos te hace comer más despacio": "Les écosser te fait manger plus lentement", "30g con cáscara como snack": "30 g avec coque en en-cas", "Pimienta negra": "Poivre noir", "Piperina": "Pipérine", "Multiplica la absorción de la curcumina": "Multiplie l’absorption de la curcumine", "Siempre junto a la cúrcuma": "Toujours avec le curcuma", "Orégano": "Origan", "Carvacrol": "Carvacrol", "Especia muy antioxidante": "Épice très antioxydante", "En salsas y proteínas": "Dans les sauces et protéines", "Miel": "Miel", "Azúcares naturales": "Sucres naturels", "Energía rápida — sigue siendo azúcar, con medida": "Énergie rapide — ça reste du sucre, avec mesure", "1 cdita pre-entreno o en avena": "1 c. à c. avant l’entraînement ou dans l’avoine", "Manzanilla": "Camomille", "Apigenina": "Apigénine", "Relajación; aliada del sueño": "Relaxation ; alliée du sommeil", "Infusión 30-60 min antes de dormir": "Infusion 30-60 min avant le coucher", "Romero": "Romarin", "Ácido rosmarínico": "Acide rosmarinique", "Aroma asociado a alerta y memoria": "Arôme associé à la vigilance et la mémoire", "En carnes, papas y aceites": "Sur viandes, pommes de terre et huiles", "Pan integral": "Pain complet", "Fibra, vitaminas B": "Fibres, vitamines B", "El carbohidrato cotidiano, con su fibra": "Le glucide du quotidien, avec ses fibres", "Tostadas del desayuno": "Toasts du petit-déjeuner", "Pasta integral": "Pâtes complètes", "Carbos de absorción media": "Glucides à absorption moyenne", "Combustible clásico del deportista": "Le carburant classique du sportif", "Comida pre-entreno (kcal en cocido)": "Repas pré-entraînement (kcal cuites)", "Edamame": "Edamame", "Proteína vegetal completa": "Protéine végétale complète", "De las mejores proteínas verdes": "L’une des meilleures protéines vertes", "Al vapor con sal marina": "À la vapeur avec sel marin", "Frijoles negros": "Haricots noirs", "Antocianinas, hierro, fibra": "Anthocyanes, fer, fibres", "Energía y salud intestinal": "Énergie et santé intestinale", "En bowls con arroz": "En bowls avec du riz"};
    Object.keys(t4en).forEach(function(k) { I18N.en.t[k] = t4en[k]; });
    Object.keys(t4fr).forEach(function(k) { I18N.fr.t[k] = t4fr[k]; });
    Object.keys(en4).forEach(function(k) { I18N.en.tx[k] = en4[k]; });
    Object.keys(fr4).forEach(function(k) { I18N.fr.tx[k] = fr4[k]; });
    window.DISHLEX = { en: {"Avena nocturna": "Overnight oats", "Crema de arroz": "Cream of rice", "Tortilla española ligera": "Light Spanish omelette", "Tortilla de claras": "Egg-white omelette", "Tortilla de espinaca": "Spinach omelette", "Tortilla 3 huevos": "3-egg omelette", "Huevos revueltos 3": "3 scrambled eggs", "Huevos revueltos": "Scrambled eggs", "Revuelto de claras": "Egg-white scramble", "Tortitas de claras y avena": "Egg-white & oat pancakes", "Tortitas de claras": "Egg-white pancakes", "Panqueques de avena": "Oat pancakes", "Waffles de avena": "Oat waffles", "Bagel integral": "Whole-wheat bagel", "Pan de arroz": "Rice cakes", "pan pita": "pita bread", "Sándwich integral de pavo": "Whole-wheat turkey sandwich", "Sándwich de atún integral": "Whole-wheat tuna sandwich", "Smoothie verde": "Green smoothie", "mantequilla de maní": "peanut butter", "pavo molido": "ground turkey", "Ternera magra": "Lean beef", "ternera magra": "lean beef", "Carne magra": "Lean meat", "carne magra": "lean meat", "puré de batata": "sweet potato mash", "puré de papa": "mashed potatoes", "Pollo al horno": "Baked chicken", "Salmón al horno": "Baked salmon", "Merluza al horno": "Baked hake", "pollo al curry": "curry chicken", "Pollo al limón": "Lemon chicken", "Pollo al ajillo": "Garlic chicken", "a la plancha": "grilled", "al vapor": "steamed", "salmón teriyaki": "teriyaki salmon", "arroz de coliflor": "cauliflower rice", "arroz integral": "brown rice", "Arroz integral": "Brown rice", "Pasta integral": "Whole-wheat pasta", "pasta integral": "whole-wheat pasta", "pan integral": "whole-wheat bread", "Pan integral": "Whole-wheat bread", "tostada integral": "whole-wheat toast", "tortillas integrales": "whole-wheat tortillas", "Fajitas de pollo con": "Chicken fajitas with", "Pizza casera integral de pollo": "Homemade whole-wheat chicken pizza", "Lentejas guisadas": "Stewed lentils", "Sopa de legumbres": "Legume soup", "Sopa minestrone": "Minestrone soup", "Crema de calabaza": "Pumpkin soup", "Ensalada de garbanzos": "Chickpea salad", "Ensalada de pollo": "Chicken salad", "ensalada griega grande": "big Greek salad", "Ensalada griega grande": "Big Greek salad", "ensalada griega": "Greek salad", "Ensalada caprese": "Caprese salad", "Paella de mariscos": "Seafood paella", "ensalada grande": "big salad", "Ensalada grande": "Big salad", "yogur con hierbas": "herb yogurt", "Yogur griego entero": "Whole Greek yogurt", "Yogur griego": "Greek yogurt", "yogur griego": "Greek yogurt", "frutos rojos": "berries", "tomate rallado": "grated tomato", "jamón de pavo": "turkey ham", "huevo duro": "boiled egg", "verduras al vapor": "steamed vegetables", "verduras wok": "wok veggies", "judías verdes": "green beans", "berenjena asada": "roasted eggplant", "coliflor asada": "roasted cauliflower", "Palomitas naturales": "Plain popcorn", "gelatina proteica": "protein jelly", "fideos de arroz": "rice noodles", "pesto ligero": "light pesto", "Batido de plátano": "Banana shake", "Batido de cacao": "Cocoa shake", "proteína": "protein", "Proteína": "Protein", "plátano": "banana", "Plátano": "Banana", "leche": "milk", "claras": "egg whites", "Claras": "Egg whites", "huevos": "eggs", "Huevos": "Eggs", "huevo": "egg", "tostada": "toast", "fruta": "fruit", "Fruta": "Fruit", "fresas": "strawberries", "nueces": "walnuts", "Nueces": "Walnuts", "miel": "honey", "atún fresco": "fresh tuna", "atún": "tuna", "Atún": "Tuna", "latas": "cans", "tomate": "tomato", "brócoli": "broccoli", "pechuga a la plancha": "grilled chicken breast", "Pechuga a la plancha": "Grilled chicken breast", "Pechuga": "Chicken breast", "pechuga": "chicken breast", "espinacas": "spinach", "espinaca": "spinach", "Requesón": "Cottage cheese", "requesón": "cottage cheese", "Batido": "Shake", "batido": "shake", "aguacate": "avocado", "pavo": "turkey", "Pavo": "Turkey", "calabacín": "zucchini", "granola": "granola", "almendras": "almonds", "Almendras": "Almonds", "maní": "peanuts", "Maní": "Peanuts", "cacao": "cocoa", "Lentejas": "Lentils", "lentejas": "lentils", "Garbanzos": "Chickpeas", "garbanzos": "chickpeas", "Merluza": "Hake", "merluza": "hake", "Bacalao": "Cod", "bacalao": "cod", "Tilapia": "Tilapia", "Trucha": "Trout", "Dorada": "Sea bream", "gambas": "shrimp", "sardinas": "sardines", "Sardinas": "Sardines", "papas al horno": "baked potatoes", "papas": "potatoes", "papa": "potato", "Papa": "Potato", "batata": "sweet potato", "Batata": "Sweet potato", "espárragos": "asparagus", "pimientos": "peppers", "pimiento": "pepper", "champiñones": "mushrooms", "coliflor": "cauliflower", "pisto": "ratatouille", "Pisto": "Ratatouille", "cuscús": "couscous", "alcaparras": "capers", "aceitunas": "olives", "Aceitunas": "Olives", "queso feta": "feta cheese", "Queso feta": "Feta cheese", "queso fresco": "fresh cheese", "Queso fresco": "Fresh cheese", "queso rallado": "grated cheese", "queso": "cheese", "Queso": "Cheese", "higos": "figs", "pera": "pear", "manzana": "apple", "Manzana": "Apple", "piña": "pineapple", "arándanos": "blueberries", "canela": "cinnamon", "chía": "chia", "linaza": "flaxseed", "Avellanas": "Hazelnuts", "comino": "cumin", "ajo": "garlic", "rúcula": "arugula", "eneldo": "dill", "pepino": "cucumber", "Pepino": "Cucumber", "Zanahoria": "Carrot", "zanahoria": "carrot", "verduras asadas": "roasted vegetables", "Verduras asadas": "Roasted vegetables", "verduras": "vegetables", "Ensalada": "Salad", "ensalada": "salad", "mantequilla": "butter", "cdas": "tbsp", "cda": "tbsp", "Pollo": "Chicken", "pollo": "chicken", "Salmón": "Salmon", "salmón": "salmon", "Ternera": "Beef", "ternera": "beef", "Carne": "Meat", "carne": "meat", "Arroz": "Rice", "arroz": "rice", "Avena": "Oats", "avena": "oats", "Pasta": "Pasta", "Quinoa": "Quinoa", "quinoa": "quinoa", "Yogur": "Yogurt", "yogur": "yogurt", "Pescado blanco": "White fish", "pescado blanco": "white fish", "Pescado": "Fish", "pescado": "fish", " y ": " & "}, fr: {"Avena nocturna": "Avoine overnight", "Crema de arroz": "Crème de riz", "Tortilla española ligera": "Tortilla espagnole légère", "Tortilla de claras": "Omelette de blancs", "Tortilla de espinaca": "Omelette aux épinards", "Tortilla 3 huevos": "Omelette 3 œufs", "Huevos revueltos 3": "3 œufs brouillés", "Huevos revueltos": "Œufs brouillés", "Revuelto de claras": "Brouillade de blancs", "Tortitas de claras y avena": "Pancakes blancs-avoine", "Tortitas de claras": "Pancakes de blancs", "Panqueques de avena": "Pancakes d’avoine", "Waffles de avena": "Gaufres d’avoine", "Bagel integral": "Bagel complet", "Pan de arroz": "Galettes de riz", "pan pita": "pain pita", "Sándwich integral de pavo": "Sandwich complet à la dinde", "Sándwich de atún integral": "Sandwich complet au thon", "Smoothie verde": "Smoothie vert", "mantequilla de maní": "beurre de cacahuète", "pavo molido": "dinde hachée", "Ternera magra": "Bœuf maigre", "ternera magra": "bœuf maigre", "Carne magra": "Viande maigre", "carne magra": "viande maigre", "puré de batata": "purée de patate douce", "puré de papa": "purée de pommes de terre", "Pollo al horno": "Poulet au four", "Salmón al horno": "Saumon au four", "Merluza al horno": "Merlu au four", "pollo al curry": "poulet au curry", "Pollo al limón": "Poulet au citron", "Pollo al ajillo": "Poulet à l’ail", "a la plancha": "grillé", "al vapor": "à la vapeur", "salmón teriyaki": "saumon teriyaki", "arroz de coliflor": "riz de chou-fleur", "arroz integral": "riz complet", "Arroz integral": "Riz complet", "Pasta integral": "Pâtes complètes", "pasta integral": "pâtes complètes", "pan integral": "pain complet", "Pan integral": "Pain complet", "tostada integral": "toast complet", "tortillas integrales": "tortillas complètes", "Fajitas de pollo con": "Fajitas de poulet avec", "Pizza casera integral de pollo": "Pizza maison complète au poulet", "Lentejas guisadas": "Lentilles mijotées", "Sopa de legumbres": "Soupe de légumineuses", "Sopa minestrone": "Soupe minestrone", "Crema de calabaza": "Velouté de courge", "Ensalada de garbanzos": "Salade de pois chiches", "Ensalada de pollo": "Salade de poulet", "ensalada griega grande": "grande salade grecque", "Ensalada griega grande": "Grande salade grecque", "ensalada griega": "salade grecque", "Ensalada caprese": "Salade caprese", "Paella de mariscos": "Paella aux fruits de mer", "ensalada grande": "grande salade", "Ensalada grande": "Grande salade", "yogur con hierbas": "yaourt aux herbes", "Yogur griego entero": "Yaourt grec entier", "Yogur griego": "Yaourt grec", "yogur griego": "yaourt grec", "frutos rojos": "fruits rouges", "tomate rallado": "tomate râpée", "jamón de pavo": "jambon de dinde", "huevo duro": "œuf dur", "verduras al vapor": "légumes vapeur", "verduras wok": "légumes wok", "judías verdes": "haricots verts", "berenjena asada": "aubergine rôtie", "coliflor asada": "chou-fleur rôti", "Palomitas naturales": "Pop-corn nature", "gelatina proteica": "gelée protéinée", "fideos de arroz": "nouilles de riz", "pesto ligero": "pesto léger", "Batido de plátano": "Shake banane", "Batido de cacao": "Shake cacao", "proteína": "protéine", "Proteína": "Protéine", "plátano": "banane", "Plátano": "Banane", "leche": "lait", "claras": "blancs d’œufs", "Claras": "Blancs d’œufs", "huevos": "œufs", "Huevos": "Œufs", "huevo": "œuf", "tostada": "toast", "fruta": "fruit", "Fruta": "Fruit", "fresas": "fraises", "nueces": "noix", "Nueces": "Noix", "miel": "miel", "atún fresco": "thon frais", "atún": "thon", "Atún": "Thon", "latas": "boîtes", "tomate": "tomate", "brócoli": "brocoli", "pechuga a la plancha": "blanc de poulet grillé", "Pechuga a la plancha": "Blanc de poulet grillé", "Pechuga": "Blanc de poulet", "pechuga": "blanc de poulet", "espinacas": "épinards", "espinaca": "épinard", "Requesón": "Fromage blanc", "requesón": "fromage blanc", "Batido": "Shake", "batido": "shake", "aguacate": "avocat", "pavo": "dinde", "Pavo": "Dinde", "calabacín": "courgette", "granola": "granola", "almendras": "amandes", "Almendras": "Amandes", "maní": "cacahuètes", "Maní": "Cacahuètes", "cacao": "cacao", "Lentejas": "Lentilles", "lentejas": "lentilles", "Garbanzos": "Pois chiches", "garbanzos": "pois chiches", "Merluza": "Merlu", "merluza": "merlu", "Bacalao": "Cabillaud", "bacalao": "cabillaud", "Tilapia": "Tilapia", "Trucha": "Truite", "Dorada": "Daurade", "gambas": "crevettes", "sardinas": "sardines", "Sardinas": "Sardines", "papas al horno": "pommes de terre au four", "papas": "pommes de terre", "papa": "pomme de terre", "Papa": "Pomme de terre", "batata": "patate douce", "Batata": "Patate douce", "espárragos": "asperges", "pimientos": "poivrons", "pimiento": "poivron", "champiñones": "champignons", "coliflor": "chou-fleur", "pisto": "ratatouille", "Pisto": "Ratatouille", "cuscús": "couscous", "alcaparras": "câpres", "aceitunas": "olives", "Aceitunas": "Olives", "queso feta": "feta", "Queso feta": "Feta", "queso fresco": "fromage frais", "Queso fresco": "Fromage frais", "queso rallado": "fromage râpé", "queso": "fromage", "Queso": "Fromage", "higos": "figues", "pera": "poire", "manzana": "pomme", "Manzana": "Pomme", "piña": "ananas", "arándanos": "myrtilles", "canela": "cannelle", "chía": "chia", "linaza": "lin", "Avellanas": "Noisettes", "comino": "cumin", "ajo": "ail", "rúcula": "roquette", "eneldo": "aneth", "pepino": "concombre", "Pepino": "Concombre", "Zanahoria": "Carotte", "zanahoria": "carotte", "verduras asadas": "légumes rôtis", "Verduras asadas": "Légumes rôtis", "verduras": "légumes", "Ensalada": "Salade", "ensalada": "salade", "mantequilla": "beurre", "cdas": "c. à s.", "cda": "c. à s.", "Pollo": "Poulet", "pollo": "poulet", "Salmón": "Saumon", "salmón": "saumon", "Ternera": "Bœuf", "ternera": "bœuf", "Carne": "Viande", "carne": "viande", "Arroz": "Riz", "arroz": "riz", "Avena": "Avoine", "avena": "avoine", "Pasta": "Pâtes", "Quinoa": "Quinoa", "quinoa": "quinoa", "Yogur": "Yaourt", "yogur": "yaourt", "Pescado blanco": "Poisson blanc", "pescado blanco": "poisson blanc", "Pescado": "Poisson", "pescado": "poisson", " y ": " et "} };
    window.DISHKEYS = Object.keys(window.DISHLEX.en).sort(function(a, b) { return b.length - a.length; });
  })();


  (function extendI18N5() {
    var t5en = {"t.mail": "Fill in email and password", "t.exists": "User already exists. Log in.", "t.reg": "✓ Registered. Welcome", "t.nouser": "User not found. Sign up.", "t.badpw": "Wrong password", "t.login": "✓ Signed in", "t.logout": "Signed out", "t.unit": "Unit", "t.kg": "kilograms", "t.lb": "pounds", "t.goal": "Daily target set", "t.kcalhoy": "kcal logged today", "t.hydr": "ml — hydration for the day", "t.lvl1": "LEVEL UP!", "t.lvl2": "You are now", "t.vol": "kg of volume", "t.body": "bodyweight", "t.pr": "New PR on", "t.slept": "Sleep logged", "t.calc": "Fill in age, height and weight", "t.addone": "Add at least one exercise to your routine", "t.nosave": "Could not save", "t.clean": "Routine cleared", "t.breath": "Breathing session complete", "t.noaudio": "Your browser doesn’t support generated audio", "t.ios": "🔇 iOS blocked the audio — tap “Play” again", "t.sess": "⏱ Session complete", "t.stopf": "Frequency stopped", "t.sess2": "Session of", "t.done2": "complete", "t.logged": "logged", "t.cam": "Camera isn’t ready yet", "t.scan1": "Analyzing with on-device AI…", "t.newcap": "🔁 New capture", "slp.y1": "Acceptable, but tight.", "slp.y2": "With ~", "slp.y3": "kcal burned today the ideal would be", "slp.y4": "and you slept", "slp.y5": "Try moving bedtime 30–60 min earlier.", "slp.r1": "Not enough for today’s load.", "slp.r2": "You burned ~", "slp.r3": "kcal and slept", "slp.r4": "ideal", "slp.r5": "Short sleep slows muscle repair and tends to raise next-day appetite.", "t.scan2": "First time downloads the model (~4 MB); it runs on your device."};
    var t5fr = {"t.mail": "Renseigne e-mail et mot de passe", "t.exists": "Cet utilisateur existe déjà. Connecte-toi.", "t.reg": "✓ Inscription réussie. Bienvenue", "t.nouser": "Utilisateur introuvable. Inscris-toi.", "t.badpw": "Mot de passe incorrect", "t.login": "✓ Session ouverte", "t.logout": "Session fermée", "t.unit": "Unité", "t.kg": "kilogrammes", "t.lb": "livres", "t.goal": "Objectif quotidien défini", "t.kcalhoy": "kcal enregistrées aujourd’hui", "t.hydr": "ml — hydratation du jour", "t.lvl1": "NIVEAU SUPÉRIEUR !", "t.lvl2": "Tu es maintenant", "t.vol": "kg de volume", "t.body": "poids du corps", "t.pr": "Nouveau record sur", "t.slept": "Sommeil enregistré", "t.calc": "Renseigne âge, taille et poids", "t.addone": "Ajoute au moins un exercice à ta routine", "t.nosave": "Impossible d’enregistrer", "t.clean": "Routine vidée", "t.breath": "Séance de respiration terminée", "t.noaudio": "Ton navigateur ne prend pas en charge l’audio généré", "t.ios": "🔇 iOS a bloqué l’audio — touche « Lire » à nouveau", "t.sess": "⏱ Séance terminée", "t.stopf": "Fréquence arrêtée", "t.sess2": "Séance de", "t.done2": "terminée", "t.logged": "enregistré", "t.cam": "La caméra n’est pas encore prête", "t.scan1": "Analyse avec IA locale…", "t.newcap": "🔁 Nouvelle capture", "slp.y1": "Acceptable, mais juste.", "slp.y2": "Avec ~", "slp.y3": "kcal brûlées aujourd’hui, l’idéal serait", "slp.y4": "et tu as dormi", "slp.y5": "Essaie d’avancer ton coucher de 30–60 min.", "slp.r1": "Insuffisant pour ta charge du jour.", "slp.r2": "Tu as brûlé ~", "slp.r3": "kcal et dormi", "slp.r4": "idéal", "slp.r5": "Dormir peu freine la réparation musculaire et augmente souvent l’appétit du lendemain.", "t.scan2": "La première fois télécharge le modèle (~4 Mo) ; tout se passe sur ton appareil."};
    Object.keys(t5en).forEach(function(k) { I18N.en.t[k] = t5en[k]; });
    Object.keys(t5fr).forEach(function(k) { I18N.fr.t[k] = t5fr[k]; });
  })();


  (function extendI18N5b() {
    var gen = {"slp.g1": "✅ <strong>Optimal recovery.</strong> You slept ", "slp.g2": " h and today you’re at ~", "slp.g3": " kcal burned training. Your body has the rest it needs to repair muscle and lock in progress."};
    var gfr = {"slp.g1": "✅ <strong>Récupération optimale.</strong> Tu as dormi ", "slp.g2": " h et aujourd’hui tu en es à ~", "slp.g3": " kcal brûlées à l’entraînement. Ton corps a le repos nécessaire pour réparer le muscle et ancrer les progrès."};
    Object.keys(gen).forEach(function(k) { I18N.en.t[k] = gen[k]; });
    Object.keys(gfr).forEach(function(k) { I18N.fr.t[k] = gfr[k]; });
  })();


  (function extendI18N6() {
    var t6en = {"f.play": "▶ Play", "f.on": "⏸ Playing", "f.stop": "⏹ Stop", "f.playd": "▶ Play dual", "f.dualintro": "<strong style=\"color:#fff\">Dual pulses per ear (1–7 Hz).</strong> Each side beats at its own rate over a soft 210 Hz tone — in the 1–7 Hz range the ear perceives a pulse, not a tone. Use headphones at low volume. Used for deep relaxation or focus; scientific evidence is limited and the experience is personal.", "f.left": "Left", "f.right": "Right", "err.chart": "Chart unavailable.", "ex.note": "Master the pattern with light weight before progressing."};
    var t6fr = {"f.play": "▶ Lire", "f.on": "⏸ En lecture", "f.stop": "⏹ Arrêter", "f.playd": "▶ Lecture duale", "f.dualintro": "<strong style=\"color:#fff\">Pulsations duales par oreille (1–7 Hz).</strong> Chaque côté bat à son propre rythme sur un ton doux de 210 Hz — dans la plage 1–7 Hz, l’oreille perçoit une pulsation, pas un ton. Utilise des écouteurs à volume bas. Employé pour la relaxation profonde ou la concentration ; les preuves scientifiques sont limitées et l’expérience est personnelle.", "f.left": "Gauche", "f.right": "Droite", "err.chart": "Graphique indisponible.", "ex.note": "Ma\u00eetrise le sch\u00e9ma avec une charge l\u00e9g\u00e8re avant de progresser."};
    var en6 = {"Sentadilla": "Squat", "Banca": "Bench", "HZ · TONO PURO": "HZ · PURE TONE", "Respiración consciente": "Mindful breathing", "Conteo de respiraciones": "Breath counting", "Escaneo corporal": "Body scan", "Respiración 4-7-8": "4-7-8 breathing", "Caminar consciente": "Mindful walking", "Gratitud": "Gratitude", "Visualización atlética": "Athletic visualization", "Metta (bondad)": "Metta (loving-kindness)", "Respiración de caja": "Box breathing", "Comer consciente": "Mindful eating", "Paisaje de sonidos": "Soundscape", "Escaneo profundo": "Deep body scan", "Respiración coherente": "Coherent breathing", "Revisión + intención": "Review + intention", "Visualizar la meta": "Visualize the goal", "Anclaje 5-4-3-2-1": "5-4-3-2-1 grounding", "Metta ampliada": "Extended metta", "4-7-8 largo": "Long 4-7-8", "Caminata 20": "20-min walk", "Silencio abierto": "Open silence", "Sesión maestra": "Master session"};
    var fr6 = {"Sentadilla": "Squat", "Banca": "Développé", "HZ · TONO PURO": "HZ · TON PUR", "Respiración consciente": "Respiration consciente", "Conteo de respiraciones": "Comptage des respirations", "Escaneo corporal": "Scan corporel", "Respiración 4-7-8": "Respiration 4-7-8", "Caminar consciente": "Marche consciente", "Gratitud": "Gratitude", "Visualización atlética": "Visualisation athlétique", "Metta (bondad)": "Metta (bienveillance)", "Respiración de caja": "Respiration carrée", "Comer consciente": "Manger en conscience", "Paisaje de sonidos": "Paysage sonore", "Escaneo profundo": "Scan profond", "Respiración coherente": "Respiration cohérente", "Revisión + intención": "Bilan + intention", "Visualizar la meta": "Visualiser l’objectif", "Anclaje 5-4-3-2-1": "Ancrage 5-4-3-2-1", "Metta ampliada": "Metta élargie", "4-7-8 largo": "4-7-8 long", "Caminata 20": "Marche 20", "Silencio abierto": "Silence ouvert", "Sesión maestra": "Séance maîtresse"};
    Object.keys(t6en).forEach(function(k) { I18N.en.t[k] = t6en[k]; });
    Object.keys(t6fr).forEach(function(k) { I18N.fr.t[k] = t6fr[k]; });
    Object.keys(en6).forEach(function(k) { I18N.en.tx[k] = en6[k]; });
    Object.keys(fr6).forEach(function(k) { I18N.fr.tx[k] = fr6[k]; });
  })();


  (function extendI18N7() {
    var en7 = {"Siéntate cómodo, espalda erguida, ojos suaves o cerrados.": "Sit comfortably, spine tall, eyes soft or closed.", "Lleva la atención al aire entrando y saliendo por la nariz.": "Bring your attention to the air moving in and out through your nose.", "Cuando la mente se vaya (lo hará), regresa sin juzgar. Eso ES el entrenamiento.": "When the mind wanders (it will), come back without judging. That IS the training.", "Respira natural; cuenta 1 en la primera exhalación.": "Breathe naturally; count 1 on the first exhale.", "Llega hasta 10 y vuelve a empezar.": "Count up to 10, then start over.", "¿Perdiste la cuenta? Perfecto: nota a dónde se fue la mente y reinicia en 1.": "Lost count? Perfect: notice where your mind went and restart at 1.", "Recorre el cuerpo de pies a cabeza, zona por zona.": "Scan your body from feet to head, zone by zone.", "En cada zona nota tensión, temperatura y contacto — sin cambiar nada.": "In each zone notice tension, temperature and contact — without changing anything.", "Si hay tensión, exhala \"hacia\" esa zona y suéltala un 10%.": "If there is tension, exhale \"into\" that zone and release it by 10%.", "Inhala por la nariz 4 s, retén 7 s, exhala por la boca 8 s.": "Inhale through the nose 4 s, hold 7 s, exhale through the mouth 8 s.", "La exhalación larga activa el freno del sistema nervioso.": "The long exhale activates the nervous system’s brake.", "Usa el cronómetro de arriba con el patrón 4-7-8.": "Use the timer above with the 4-7-8 pattern.", "Camina algo más lento de lo normal, sin teléfono.": "Walk a bit slower than usual, phone-free.", "Siente cada pie: talón, planta, dedos.": "Feel each foot: heel, sole, toes.", "Cuando notes el piloto automático, vuelve a los pies.": "When you notice autopilot, return to your feet.", "Piensa o escribe 3 cosas concretas de HOY que agradeces.": "Think of or write 3 specific things from TODAY you are grateful for.", "Por cada una: por qué ocurrió y quién contribuyó.": "For each one: why it happened and who contributed.", "Nota cómo cambia el estado del cuerpo al evocarlas.": "Notice how your body’s state changes as you recall them.", "Elige un ejercicio (ej. sentadilla) y ensáyalo mentalmente.": "Pick an exercise (e.g. squat) and rehearse it mentally.", "Visualiza en primera persona: técnica, respiración, esfuerzo.": "Visualize in first person: technique, breathing, effort.", "La corteza motora se activa al imaginar: es entrenamiento real.": "The motor cortex fires when you imagine: it is real training.", "Repite mentalmente: \"Que esté bien, que esté fuerte, que esté en paz\".": "Mentally repeat: \"May I be well, may I be strong, may I be at peace\".", "Dirígelo a ti, luego a alguien querido, luego a alguien neutro.": "Direct it to yourself, then to a loved one, then to someone neutral.", "No fuerces sentir nada: el gesto de desear ya entrena el ánimo.": "Do not force any feeling: the act of wishing already trains the mind.", "Inhala 4 s · retén 4 s · exhala 4 s · retén 4 s.": "Inhale 4 s · hold 4 s · exhale 4 s · hold 4 s.", "La usan militares y deportistas para foco bajo presión.": "Used by the military and athletes for focus under pressure.", "Cronómetro de arriba: patrón Caja.": "Timer above: Box pattern.", "Come una comida o snack sin pantallas.": "Eat one meal or snack with no screens.", "Primeros 3 bocados: textura, temperatura, sabor, velocidad.": "First 3 bites: texture, temperature, flavor, speed.", "Suelta el cubierto entre bocados y nota la saciedad real.": "Put down your fork between bites and notice real fullness.", "Ojos cerrados: deja que los sonidos vengan a ti.": "Eyes closed: let the sounds come to you.", "Etiqueta suave: lejos, cerca, agudo, grave.": "Label gently: far, near, high, low.", "No persigas ni rechaces ninguno: solo recepción.": "Do not chase or reject any of them: just receive.", "Como el día 3, pero al doble de lentitud.": "Like day 3, but twice as slow.", "Incluye cara, mandíbula, lengua y manos: acumulan tensión.": "Include face, jaw, tongue and hands: they store tension.", "Termina 1 minuto sintiendo el cuerpo como un todo.": "Finish with 1 minute feeling the body as a whole.", "Inhala 5 s, exhala 5 s: 6 respiraciones por minuto.": "Inhale 5 s, exhale 5 s: 6 breaths per minute.", "Este ritmo favorece la variabilidad cardiaca (HRV).": "This rhythm supports heart-rate variability (HRV).", "Cronómetro de arriba: patrón Coherente 5-5.": "Timer above: Coherent 5-5 pattern.", "Mitad del camino: ¿qué práctica te dio más? ¿Cuál costó?": "Halfway there: which practice gave you the most? Which was hardest?", "Escribe una frase con tu intención para la semana final.": "Write one sentence with your intention for the final week.", "Repite hoy tu práctica favorita 5 minutos.": "Repeat your favorite practice today for 5 minutes.", "Visualiza tu meta física a 6 meses con detalle sensorial.": "Visualize your 6-month physical goal in sensory detail.", "Ahora visualiza el PROCESO: tu semana típica para llegar ahí.": "Now visualize the PROCESS: your typical week to get there.", "La meta motiva; el proceso construye. Ensaya el proceso.": "The goal motivates; the process builds. Rehearse the process.", "Nombra 5 cosas que ves, 4 que sientes, 3 que oyes, 2 que hueles, 1 que saboreas.": "Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste.", "Es un ancla instantánea para ansiedad o sobrecarga.": "It is an instant anchor for anxiety or overwhelm.", "Hazlo dos veces; la segunda, más lento.": "Do it twice; the second time, slower.", "Como el día 8, y añade a alguien difícil y a \"todos los que entrenan hoy\".": "Like day 8, and add someone difficult and \"everyone training today\".", "Si aparece resistencia, obsérvala: también es práctica.": "If resistance shows up, observe it: that is practice too.", "Cierra dirigiéndolo a ti otra vez.": "Close by directing it to yourself again.", "Repite el patrón 4-7-8, ahora 10 minutos.": "Repeat the 4-7-8 pattern, now for 10 minutes.", "Nota cuánto más fácil fluye que el día 4.": "Notice how much more easily it flows than day 4.", "Ideal 30-60 minutos antes de dormir.": "Ideal 30-60 minutes before bed.", "20 minutos, idealmente al aire libre y sin audífonos.": "20 minutes, ideally outdoors and without headphones.", "Alterna: 5 min pies · 5 min sonidos · 5 min respiración · 5 min abierto.": "Alternate: 5 min feet · 5 min sounds · 5 min breath · 5 min open.", "Termina notando tu estado frente al inicio.": "Finish by noticing your state versus the start.", "Sin técnica: siéntate y observa lo que aparezca.": "No technique: sit and watch whatever shows up.", "Pensamientos, sonidos, sensaciones: todo pasa, tú observas.": "Thoughts, sounds, sensations: everything passes, you observe.", "La práctica más avanzada: no hacer nada, del todo.": "The most advanced practice: doing nothing, completely.", "Diseña tu sesión: 5 min respiración + 10 min tu práctica favorita + 5 min metta o gratitud.": "Design your session: 5 min breathing + 10 min your favorite practice + 5 min metta or gratitude.", "Ya tienes las herramientas: ahora son tuyas.": "You have the tools now: they are yours.", "Repite el programa o crea tu rutina diaria de 10 minutos.": "Repeat the program or build your own 10-minute daily routine."};
    var fr7 = {"Siéntate cómodo, espalda erguida, ojos suaves o cerrados.": "Assieds-toi confortablement, dos droit, yeux doux ou fermés.", "Lleva la atención al aire entrando y saliendo por la nariz.": "Porte ton attention sur l’air qui entre et sort par le nez.", "Cuando la mente se vaya (lo hará), regresa sin juzgar. Eso ES el entrenamiento.": "Quand l’esprit s’échappe (il le fera), reviens sans juger. C’est ÇA l’entraînement.", "Respira natural; cuenta 1 en la primera exhalación.": "Respire naturellement ; compte 1 à la première expiration.", "Llega hasta 10 y vuelve a empezar.": "Va jusqu’à 10 puis recommence.", "¿Perdiste la cuenta? Perfecto: nota a dónde se fue la mente y reinicia en 1.": "Tu as perdu le compte ? Parfait : note où ton esprit est parti et repars à 1.", "Recorre el cuerpo de pies a cabeza, zona por zona.": "Parcours ton corps des pieds à la tête, zone par zone.", "En cada zona nota tensión, temperatura y contacto — sin cambiar nada.": "Dans chaque zone, note tension, température et contact — sans rien changer.", "Si hay tensión, exhala \"hacia\" esa zona y suéltala un 10%.": "S’il y a de la tension, expire « vers » cette zone et relâche-la de 10 %.", "Inhala por la nariz 4 s, retén 7 s, exhala por la boca 8 s.": "Inspire par le nez 4 s, retiens 7 s, expire par la bouche 8 s.", "La exhalación larga activa el freno del sistema nervioso.": "L’expiration longue active le frein du système nerveux.", "Usa el cronómetro de arriba con el patrón 4-7-8.": "Utilise le minuteur ci-dessus avec le schéma 4-7-8.", "Camina algo más lento de lo normal, sin teléfono.": "Marche un peu plus lentement que d’habitude, sans téléphone.", "Siente cada pie: talón, planta, dedos.": "Sens chaque pied : talon, plante, orteils.", "Cuando notes el piloto automático, vuelve a los pies.": "Quand tu remarques le pilote automatique, reviens aux pieds.", "Piensa o escribe 3 cosas concretas de HOY que agradeces.": "Pense ou écris 3 choses concrètes d’AUJOURD’HUI dont tu es reconnaissant.", "Por cada una: por qué ocurrió y quién contribuyó.": "Pour chacune : pourquoi c’est arrivé et qui y a contribué.", "Nota cómo cambia el estado del cuerpo al evocarlas.": "Note comment l’état de ton corps change en les évoquant.", "Elige un ejercicio (ej. sentadilla) y ensáyalo mentalmente.": "Choisis un exercice (ex. squat) et répète-le mentalement.", "Visualiza en primera persona: técnica, respiración, esfuerzo.": "Visualise à la première personne : technique, respiration, effort.", "La corteza motora se activa al imaginar: es entrenamiento real.": "Le cortex moteur s’active quand tu imagines : c’est un vrai entraînement.", "Repite mentalmente: \"Que esté bien, que esté fuerte, que esté en paz\".": "Répète mentalement : « Que je sois bien, que je sois fort, que je sois en paix ».", "Dirígelo a ti, luego a alguien querido, luego a alguien neutro.": "Adresse-le à toi, puis à un proche, puis à quelqu’un de neutre.", "No fuerces sentir nada: el gesto de desear ya entrena el ánimo.": "Ne force aucun ressenti : le geste de souhaiter entraîne déjà le moral.", "Inhala 4 s · retén 4 s · exhala 4 s · retén 4 s.": "Inspire 4 s · retiens 4 s · expire 4 s · retiens 4 s.", "La usan militares y deportistas para foco bajo presión.": "Utilisée par les militaires et les sportifs pour rester concentré sous pression.", "Cronómetro de arriba: patrón Caja.": "Minuteur ci-dessus : schéma Carrée.", "Come una comida o snack sin pantallas.": "Prends un repas ou un en-cas sans écrans.", "Primeros 3 bocados: textura, temperatura, sabor, velocidad.": "Les 3 premières bouchées : texture, température, goût, vitesse.", "Suelta el cubierto entre bocados y nota la saciedad real.": "Pose tes couverts entre les bouchées et note la vraie satiété.", "Ojos cerrados: deja que los sonidos vengan a ti.": "Yeux fermés : laisse les sons venir à toi.", "Etiqueta suave: lejos, cerca, agudo, grave.": "Étiquette doucement : loin, près, aigu, grave.", "No persigas ni rechaces ninguno: solo recepción.": "N’en poursuis ni n’en rejette aucun : simple réception.", "Como el día 3, pero al doble de lentitud.": "Comme le jour 3, mais deux fois plus lentement.", "Incluye cara, mandíbula, lengua y manos: acumulan tensión.": "Inclus visage, mâchoire, langue et mains : ils accumulent la tension.", "Termina 1 minuto sintiendo el cuerpo como un todo.": "Termine par 1 minute à sentir le corps comme un tout.", "Inhala 5 s, exhala 5 s: 6 respiraciones por minuto.": "Inspire 5 s, expire 5 s : 6 respirations par minute.", "Este ritmo favorece la variabilidad cardiaca (HRV).": "Ce rythme favorise la variabilité cardiaque (HRV).", "Cronómetro de arriba: patrón Coherente 5-5.": "Minuteur ci-dessus : schéma Cohérente 5-5.", "Mitad del camino: ¿qué práctica te dio más? ¿Cuál costó?": "À mi-chemin : quelle pratique t’a le plus apporté ? Laquelle a coûté ?", "Escribe una frase con tu intención para la semana final.": "Écris une phrase avec ton intention pour la dernière semaine.", "Repite hoy tu práctica favorita 5 minutos.": "Refais aujourd’hui ta pratique préférée pendant 5 minutes.", "Visualiza tu meta física a 6 meses con detalle sensorial.": "Visualise ton objectif physique à 6 mois avec des détails sensoriels.", "Ahora visualiza el PROCESO: tu semana típica para llegar ahí.": "Visualise maintenant le PROCESSUS : ta semaine type pour y arriver.", "La meta motiva; el proceso construye. Ensaya el proceso.": "L’objectif motive ; le processus construit. Répète le processus.", "Nombra 5 cosas que ves, 4 que sientes, 3 que oyes, 2 que hueles, 1 que saboreas.": "Nomme 5 choses que tu vois, 4 que tu touches, 3 que tu entends, 2 que tu sens, 1 que tu goûtes.", "Es un ancla instantánea para ansiedad o sobrecarga.": "C’est une ancre instantanée contre l’anxiété ou la surcharge.", "Hazlo dos veces; la segunda, más lento.": "Fais-le deux fois ; la seconde, plus lentement.", "Como el día 8, y añade a alguien difícil y a \"todos los que entrenan hoy\".": "Comme le jour 8, en ajoutant quelqu’un de difficile et « tous ceux qui s’entraînent aujourd’hui ».", "Si aparece resistencia, obsérvala: también es práctica.": "Si une résistance apparaît, observe-la : c’est aussi la pratique.", "Cierra dirigiéndolo a ti otra vez.": "Termine en te l’adressant à nouveau.", "Repite el patrón 4-7-8, ahora 10 minutos.": "Répète le schéma 4-7-8, cette fois 10 minutes.", "Nota cuánto más fácil fluye que el día 4.": "Note comme ça coule plus facilement qu’au jour 4.", "Ideal 30-60 minutos antes de dormir.": "Idéal 30-60 minutes avant de dormir.", "20 minutos, idealmente al aire libre y sin audífonos.": "20 minutes, idéalement en plein air et sans écouteurs.", "Alterna: 5 min pies · 5 min sonidos · 5 min respiración · 5 min abierto.": "Alterne : 5 min pieds · 5 min sons · 5 min respiration · 5 min ouvert.", "Termina notando tu estado frente al inicio.": "Termine en notant ton état par rapport au début.", "Sin técnica: siéntate y observa lo que aparezca.": "Sans technique : assieds-toi et observe ce qui apparaît.", "Pensamientos, sonidos, sensaciones: todo pasa, tú observas.": "Pensées, sons, sensations : tout passe, toi tu observes.", "La práctica más avanzada: no hacer nada, del todo.": "La pratique la plus avancée : ne rien faire, complètement.", "Diseña tu sesión: 5 min respiración + 10 min tu práctica favorita + 5 min metta o gratitud.": "Compose ta séance : 5 min de respiration + 10 min de ta pratique préférée + 5 min de metta ou gratitude.", "Ya tienes las herramientas: ahora son tuyas.": "Tu as maintenant les outils : ils sont à toi.", "Repite el programa o crea tu rutina diaria de 10 minutos.": "Refais le programme ou crée ta routine quotidienne de 10 minutes."};
    Object.keys(en7).forEach(function(k) { I18N.en.tx[k] = en7[k]; });
    Object.keys(fr7).forEach(function(k) { I18N.fr.tx[k] = fr7[k]; });
  })();


  (function extendI18N8() {
    var en8 = {"Barra sobre los trapecios (no el cuello), pies al ancho de hombros con puntas ~15° afuera.": "Bar on your traps (not your neck), feet shoulder-width with toes ~15° out.", "Pecho arriba y core firme; inicia empujando la cadera atrás y flexionando rodillas.": "Chest up and core braced; start by pushing your hips back and bending your knees.", "Baja hasta muslos al menos paralelos, rodillas siempre en línea con los pies.": "Go down until your thighs are at least parallel, knees always tracking over your feet.", "Empuja el suelo con todo el pie para subir; exhala arriba.": "Push the floor with your whole foot to stand up; exhale at the top.", "Espalda y glúteos pegados al respaldo; pies al centro, ancho de hombros.": "Back and glutes flat against the pad; feet centered, shoulder-width.", "Baja controlado hasta ~90° de rodilla sin que la cadera se despegue.": "Lower under control to ~90° at the knee without your hips lifting off.", "Empuja con todo el pie hasta casi extender, sin bloquear las rodillas.": "Press through your whole foot to near full extension, without locking your knees.", "Da un paso largo manteniendo el torso vertical.": "Take a long step keeping your torso upright.", "Baja hasta que ambas rodillas queden ~90°; la trasera casi toca el suelo.": "Lower until both knees are at ~90°; the back knee almost touches the floor.", "Empuja con el talón de la pierna delantera para volver; alterna piernas.": "Push through your front heel to return; alternate legs.", "Ajusta el rodillo justo sobre los tobillos y la rodilla alineada con el eje de la máquina.": "Set the pad just above your ankles, knee aligned with the machine’s axis.", "Sube controlado hasta casi extender por completo; pausa 1 s arriba.": "Lift under control to near full extension; pause 1 s at the top.", "Baja en 2-3 s resistiendo el peso.": "Lower in 2-3 s resisting the weight.", "Rodillo sobre el tendón de Aquiles; caderas pegadas al banco.": "Pad over your Achilles tendon; hips pressed into the bench.", "Flexiona llevando los talones hacia el glúteo sin arquear la lumbar.": "Curl your heels toward your glutes without arching your lower back.", "Baja lento y controla el estiramiento.": "Lower slowly and control the stretch.", "Apoya la espalda alta en el banco; barra sobre la cadera con protector.": "Upper back on the bench; bar over your hips with a pad.", "Pies al ancho de cadera; empuja con los talones hasta alinear hombro-cadera-rodilla.": "Feet hip-width; drive through your heels until shoulder-hip-knee align.", "Aprieta el glúteo 1-2 s arriba con el mentón ligeramente al pecho.": "Squeeze your glutes 1-2 s at the top, chin slightly tucked.", "Baja controlado sin rebotar en el suelo.": "Lower under control without bouncing off the floor.", "Apoya solo los metatarsos en el borde del escalón o plataforma.": "Only the balls of your feet on the edge of the step or platform.", "Baja 1-2 s hasta sentir el estiramiento completo del gemelo.": "Lower for 1-2 s until you feel a full calf stretch.", "Sube lo más alto posible y aprieta 1-2 s en la punta.": "Rise as high as possible and squeeze 1-2 s at the top.", "Escápulas retraídas y clavadas al banco; pies firmes en el suelo.": "Shoulder blades retracted and pinned to the bench; feet firm on the floor.", "Agarre algo más ancho que los hombros, muñecas rectas.": "Grip slightly wider than your shoulders, wrists straight.", "Baja la barra al pecho medio con codos a ~45-60° del torso.": "Lower the bar to mid-chest with elbows at ~45-60° from your torso.", "Toca ligero y empuja en línea hacia arriba y ligeramente atrás.": "Touch lightly and press up and slightly back in a straight line.", "Banco entre 30-45°; escápulas retraídas.": "Bench at 30-45°; shoulder blades retracted.", "La barra baja a la parte alta del pecho/clavícula.": "The bar comes down to your upper chest/collarbone.", "Empuja vertical sin que los codos se abran en exceso.": "Press vertically without flaring your elbows too much.", "Mancuernas arriba con codos semiflexionados y fijos.": "Dumbbells up with elbows slightly bent and fixed.", "Abre en arco amplio hasta sentir el estiramiento del pecho, sin dolor de hombro.": "Open in a wide arc until you feel a chest stretch, with no shoulder pain.", "Cierra como si abrazaras un barril, apretando el pecho.": "Close as if hugging a barrel, squeezing your chest.", "Hombros deprimidos, lejos de las orejas; core firme.": "Shoulders down, away from your ears; core braced.", "Inclínate un poco adelante para enfocar el pecho.": "Lean slightly forward to target your chest.", "Baja controlado hasta ~90° de codo y sube sin bloquear con golpe.": "Lower under control to ~90° at the elbow and press up without slamming into lockout.", "Agarre pronado algo más ancho que los hombros.": "Overhand grip slightly wider than your shoulders.", "Inicia deprimiendo las escápulas (hombros lejos de orejas).": "Start by depressing your shoulder blades (shoulders away from ears).", "Sube llevando el pecho a la barra, codos hacia el suelo.": "Pull your chest to the bar, driving your elbows toward the floor.", "Baja controlado hasta casi extender los brazos.": "Lower under control until your arms are nearly straight.", "Bisagra de cadera con torso ~45° y espalda neutra.": "Hip hinge with your torso at ~45° and a neutral spine.", "Tira de la barra hacia el abdomen bajo llevando los codos atrás.": "Pull the bar to your lower abs, driving your elbows back.", "Aprieta las escápulas 1 s y baja controlado.": "Squeeze your shoulder blades 1 s and lower under control.", "Pecho alto, ligera inclinación atrás fija.": "Chest up, slight fixed backward lean.", "Tira de la barra hacia la clavícula llevando los codos abajo y atrás.": "Pull the bar toward your collarbone, driving your elbows down and back.", "Controla la subida sintiendo el estiramiento del dorsal.": "Control the way up, feeling the lat stretch.", "Rodillas semiflexionadas y torso vertical estable.": "Knees slightly bent and torso upright and stable.", "Tira hacia el abdomen con los codos pegados al cuerpo.": "Pull to your abdomen with your elbows close to your body.", "Junta las escápulas al final y regresa lento.": "Squeeze your shoulder blades at the end and return slowly.", "Barra sobre el medio del pie; agarre justo fuera de las piernas.": "Bar over mid-foot; grip just outside your legs.", "Bisagra: cadera atrás, espalda neutra, pecho arriba; tensa la barra antes de despegar.": "Hinge: hips back, neutral spine, chest up; take the slack out of the bar before lifting.", "Empuja el suelo y sube con la barra pegada a las piernas.": "Push the floor and stand up with the bar close to your legs.", "Bloquea arriba con la cadera, sin hiperextender; baja con la misma bisagra.": "Lock out at the top with your hips, without hyperextending; lower with the same hinge.", "Barra a la altura de las clavículas, agarre justo fuera de hombros.": "Bar at collarbone height, grip just outside your shoulders.", "Glúteos y abdomen firmes: el cuerpo es una columna.": "Glutes and abs braced: your body is a column.", "Empuja vertical y mete la cabeza al pasar la barra.": "Press vertically and bring your head through as the bar passes.", "Bloquea arriba con los bíceps junto a las orejas.": "Lock out with your biceps next to your ears.", "Codos semiflexionados y fijos durante todo el recorrido.": "Elbows slightly bent and fixed through the whole range.", "Sube liderando con los codos hasta la altura de los hombros.": "Raise leading with your elbows up to shoulder height.", "Pausa breve y baja en 2-3 s.": "Brief pause and lower in 2-3 s.", "Polea a la altura de la cara con cuerda.": "Pulley at face height with a rope attachment.", "Tira hacia la frente separando las manos, codos altos.": "Pull toward your forehead, spreading your hands, elbows high.", "Rota los nudillos hacia atrás al final (rotación externa).": "Rotate your knuckles back at the end (external rotation).", "Codos pegados al torso y fijos.": "Elbows pinned to your torso and fixed.", "Sube sin balancear; gira la palma hacia arriba si usas mancuerna.": "Curl without swinging; rotate your palm up if using a dumbbell.", "Baja en 2-3 s hasta extender casi por completo.": "Lower in 2-3 s to near full extension.", "Agarre neutro (palmas enfrentadas) y codos fijos.": "Neutral grip (palms facing each other) and fixed elbows.", "Sube controlado sin girar la muñeca.": "Curl under control without rotating your wrist.", "Baja lento; trabaja braquial y antebrazo.": "Lower slowly; it works the brachialis and forearm.", "Codos pegados al cuerpo y fijos como bisagras.": "Elbows pinned to your body, fixed like hinges.", "Extiende hasta bloquear abajo apretando el tríceps 1 s.": "Extend to lockout at the bottom, squeezing your triceps 1 s.", "Sube controlado moviendo solo los antebrazos.": "Return under control moving only your forearms.", "Antebrazos bajo los hombros; cuerpo en línea recta de cabeza a talones.": "Forearms under your shoulders; body in a straight line from head to heels.", "Aprieta glúteo y abdomen con la pelvis ligeramente metida.": "Squeeze your glutes and abs with a slight pelvic tuck.", "Mirada al suelo y respiración constante.": "Eyes on the floor and steady breathing.", "Lumbar pegada al suelo, manos a los lados de la cabeza sin tirar.": "Lower back flat on the floor, hands beside your head without pulling.", "Despega solo las escápulas exhalando.": "Lift only your shoulder blades as you exhale.", "Baja controlado sin dejarte caer.": "Lower under control without dropping.", "Lumbar presionada contra el suelo (manos bajo el glúteo si ayuda).": "Lower back pressed into the floor (hands under your glutes if it helps).", "Baja las piernas solo hasta donde la lumbar no se arquee.": "Lower your legs only as far as your lower back stays flat.", "Sube exhalando con el abdomen, no con impulso.": "Raise them exhaling with your abs, not with momentum.", "Plancha alta con hombros sobre las muñecas.": "High plank with your shoulders over your wrists.", "Lleva las rodillas al pecho alternando con ritmo, sin subir la cadera.": "Drive your knees to your chest alternating with rhythm, without raising your hips.", "Core firme: la espalda no rebota.": "Core braced: your back does not bounce.", "Baja a sentadilla y apoya las manos.": "Drop into a squat and place your hands down.", "Lanza los pies atrás a plancha firme (flexión opcional).": "Kick your feet back to a solid plank (push-up optional).", "Recoge los pies y salta extendiendo la cadera.": "Bring your feet back in and jump, extending your hips.", "Aterriza suave con rodillas flexionadas.": "Land softly with bent knees."};
    var fr8 = {"Barra sobre los trapecios (no el cuello), pies al ancho de hombros con puntas ~15° afuera.": "Barre sur les trapèzes (pas la nuque), pieds largeur d’épaules, pointes ~15° vers l’extérieur.", "Pecho arriba y core firme; inicia empujando la cadera atrás y flexionando rodillas.": "Poitrine haute et gainage ferme ; commence en poussant les hanches en arrière et en fléchissant les genoux.", "Baja hasta muslos al menos paralelos, rodillas siempre en línea con los pies.": "Descends jusqu’à cuisses au moins parallèles, genoux toujours alignés avec les pieds.", "Empuja el suelo con todo el pie para subir; exhala arriba.": "Pousse le sol avec tout le pied pour remonter ; expire en haut.", "Espalda y glúteos pegados al respaldo; pies al centro, ancho de hombros.": "Dos et fessiers collés au dossier ; pieds au centre, largeur d’épaules.", "Baja controlado hasta ~90° de rodilla sin que la cadera se despegue.": "Descends en contrôle jusqu’à ~90° de genou sans décoller les hanches.", "Empuja con todo el pie hasta casi extender, sin bloquear las rodillas.": "Pousse avec tout le pied jusqu’à presque tendre, sans verrouiller les genoux.", "Da un paso largo manteniendo el torso vertical.": "Fais un grand pas en gardant le buste vertical.", "Baja hasta que ambas rodillas queden ~90°; la trasera casi toca el suelo.": "Descends jusqu’à ~90° aux deux genoux ; le genou arrière frôle le sol.", "Empuja con el talón de la pierna delantera para volver; alterna piernas.": "Pousse sur le talon de la jambe avant pour revenir ; alterne les jambes.", "Ajusta el rodillo justo sobre los tobillos y la rodilla alineada con el eje de la máquina.": "Règle le boudin juste au-dessus des chevilles, genou aligné avec l’axe de la machine.", "Sube controlado hasta casi extender por completo; pausa 1 s arriba.": "Monte en contrôle jusqu’à presque tendre ; pause 1 s en haut.", "Baja en 2-3 s resistiendo el peso.": "Redescends en 2-3 s en résistant à la charge.", "Rodillo sobre el tendón de Aquiles; caderas pegadas al banco.": "Boudin sur le tendon d’Achille ; hanches plaquées au banc.", "Flexiona llevando los talones hacia el glúteo sin arquear la lumbar.": "Fléchis en amenant les talons vers les fessiers sans cambrer les lombaires.", "Baja lento y controla el estiramiento.": "Redescends lentement et contrôle l’étirement.", "Apoya la espalda alta en el banco; barra sobre la cadera con protector.": "Haut du dos sur le banc ; barre sur les hanches avec protection.", "Pies al ancho de cadera; empuja con los talones hasta alinear hombro-cadera-rodilla.": "Pieds largeur de hanches ; pousse sur les talons jusqu’à aligner épaule-hanche-genou.", "Aprieta el glúteo 1-2 s arriba con el mentón ligeramente al pecho.": "Serre les fessiers 1-2 s en haut, menton légèrement rentré.", "Baja controlado sin rebotar en el suelo.": "Redescends en contrôle sans rebondir au sol.", "Apoya solo los metatarsos en el borde del escalón o plataforma.": "Seuls les avant-pieds sur le bord de la marche ou de la plateforme.", "Baja 1-2 s hasta sentir el estiramiento completo del gemelo.": "Descends 1-2 s jusqu’à sentir l’étirement complet du mollet.", "Sube lo más alto posible y aprieta 1-2 s en la punta.": "Monte le plus haut possible et serre 1-2 s sur la pointe.", "Escápulas retraídas y clavadas al banco; pies firmes en el suelo.": "Omoplates rétractées et vissées au banc ; pieds fermes au sol.", "Agarre algo más ancho que los hombros, muñecas rectas.": "Prise un peu plus large que les épaules, poignets droits.", "Baja la barra al pecho medio con codos a ~45-60° del torso.": "Descends la barre au milieu de la poitrine, coudes à ~45-60° du buste.", "Toca ligero y empuja en línea hacia arriba y ligeramente atrás.": "Touche légèrement et pousse vers le haut et légèrement en arrière.", "Banco entre 30-45°; escápulas retraídas.": "Banc entre 30-45° ; omoplates rétractées.", "La barra baja a la parte alta del pecho/clavícula.": "La barre descend vers le haut de la poitrine/clavicule.", "Empuja vertical sin que los codos se abran en exceso.": "Pousse à la verticale sans trop écarter les coudes.", "Mancuernas arriba con codos semiflexionados y fijos.": "Haltères en haut, coudes semi-fléchis et fixes.", "Abre en arco amplio hasta sentir el estiramiento del pecho, sin dolor de hombro.": "Ouvre en arc large jusqu’à sentir l’étirement de la poitrine, sans douleur d’épaule.", "Cierra como si abrazaras un barril, apretando el pecho.": "Referme comme si tu enlaçais un tonneau, en serrant la poitrine.", "Hombros deprimidos, lejos de las orejas; core firme.": "Épaules abaissées, loin des oreilles ; gainage ferme.", "Inclínate un poco adelante para enfocar el pecho.": "Penche-toi légèrement en avant pour cibler la poitrine.", "Baja controlado hasta ~90° de codo y sube sin bloquear con golpe.": "Descends en contrôle jusqu’à ~90° de coude et remonte sans verrouiller brutalement.", "Agarre pronado algo más ancho que los hombros.": "Prise en pronation un peu plus large que les épaules.", "Inicia deprimiendo las escápulas (hombros lejos de orejas).": "Commence en abaissant les omoplates (épaules loin des oreilles).", "Sube llevando el pecho a la barra, codos hacia el suelo.": "Monte en amenant la poitrine vers la barre, coudes vers le sol.", "Baja controlado hasta casi extender los brazos.": "Redescends en contrôle jusqu’à presque tendre les bras.", "Bisagra de cadera con torso ~45° y espalda neutra.": "Charnière de hanches, buste à ~45°, dos neutre.", "Tira de la barra hacia el abdomen bajo llevando los codos atrás.": "Tire la barre vers le bas-ventre en amenant les coudes en arrière.", "Aprieta las escápulas 1 s y baja controlado.": "Serre les omoplates 1 s et redescends en contrôle.", "Pecho alto, ligera inclinación atrás fija.": "Poitrine haute, légère inclinaison arrière fixe.", "Tira de la barra hacia la clavícula llevando los codos abajo y atrás.": "Tire la barre vers la clavicule en amenant les coudes vers le bas et l’arrière.", "Controla la subida sintiendo el estiramiento del dorsal.": "Contrôle la remontée en sentant l’étirement du dorsal.", "Rodillas semiflexionadas y torso vertical estable.": "Genoux semi-fléchis, buste vertical et stable.", "Tira hacia el abdomen con los codos pegados al cuerpo.": "Tire vers l’abdomen, coudes près du corps.", "Junta las escápulas al final y regresa lento.": "Rapproche les omoplates à la fin et reviens lentement.", "Barra sobre el medio del pie; agarre justo fuera de las piernas.": "Barre au milieu du pied ; prise juste à l’extérieur des jambes.", "Bisagra: cadera atrás, espalda neutra, pecho arriba; tensa la barra antes de despegar.": "Charnière : hanches en arrière, dos neutre, poitrine haute ; mets la barre en tension avant de décoller.", "Empuja el suelo y sube con la barra pegada a las piernas.": "Pousse le sol et remonte avec la barre collée aux jambes.", "Bloquea arriba con la cadera, sin hiperextender; baja con la misma bisagra.": "Verrouille en haut avec les hanches, sans hyperextension ; redescends avec la même charnière.", "Barra a la altura de las clavículas, agarre justo fuera de hombros.": "Barre à hauteur des clavicules, prise juste à l’extérieur des épaules.", "Glúteos y abdomen firmes: el cuerpo es una columna.": "Fessiers et abdos gainés : le corps est une colonne.", "Empuja vertical y mete la cabeza al pasar la barra.": "Pousse à la verticale et passe la tête quand la barre dépasse.", "Bloquea arriba con los bíceps junto a las orejas.": "Verrouille en haut, biceps près des oreilles.", "Codos semiflexionados y fijos durante todo el recorrido.": "Coudes semi-fléchis et fixes sur tout le trajet.", "Sube liderando con los codos hasta la altura de los hombros.": "Monte en guidant avec les coudes jusqu’à hauteur d’épaules.", "Pausa breve y baja en 2-3 s.": "Courte pause et redescends en 2-3 s.", "Polea a la altura de la cara con cuerda.": "Poulie à hauteur du visage avec une corde.", "Tira hacia la frente separando las manos, codos altos.": "Tire vers le front en écartant les mains, coudes hauts.", "Rota los nudillos hacia atrás al final (rotación externa).": "Tourne les phalanges vers l’arrière à la fin (rotation externe).", "Codos pegados al torso y fijos.": "Coudes collés au buste et fixes.", "Sube sin balancear; gira la palma hacia arriba si usas mancuerna.": "Monte sans balancer ; tourne la paume vers le haut avec un haltère.", "Baja en 2-3 s hasta extender casi por completo.": "Redescends en 2-3 s jusqu’à presque tendre.", "Agarre neutro (palmas enfrentadas) y codos fijos.": "Prise neutre (paumes face à face) et coudes fixes.", "Sube controlado sin girar la muñeca.": "Monte en contrôle sans tourner le poignet.", "Baja lento; trabaja braquial y antebrazo.": "Redescends lentement ; ça travaille le brachial et l’avant-bras.", "Codos pegados al cuerpo y fijos como bisagras.": "Coudes collés au corps, fixes comme des charnières.", "Extiende hasta bloquear abajo apretando el tríceps 1 s.": "Tends jusqu’au verrouillage en bas en serrant le triceps 1 s.", "Sube controlado moviendo solo los antebrazos.": "Remonte en contrôle en ne bougeant que les avant-bras.", "Antebrazos bajo los hombros; cuerpo en línea recta de cabeza a talones.": "Avant-bras sous les épaules ; corps en ligne droite de la tête aux talons.", "Aprieta glúteo y abdomen con la pelvis ligeramente metida.": "Serre fessiers et abdos, bassin légèrement rétroversé.", "Mirada al suelo y respiración constante.": "Regard au sol et respiration régulière.", "Lumbar pegada al suelo, manos a los lados de la cabeza sin tirar.": "Lombaires plaquées au sol, mains sur les côtés de la tête sans tirer.", "Despega solo las escápulas exhalando.": "Décolle seulement les omoplates en expirant.", "Baja controlado sin dejarte caer.": "Redescends en contrôle sans te laisser tomber.", "Lumbar presionada contra el suelo (manos bajo el glúteo si ayuda).": "Lombaires pressées au sol (mains sous les fessiers si besoin).", "Baja las piernas solo hasta donde la lumbar no se arquee.": "Descends les jambes seulement tant que les lombaires ne se cambrent pas.", "Sube exhalando con el abdomen, no con impulso.": "Remonte en expirant avec les abdos, pas avec l’élan.", "Plancha alta con hombros sobre las muñecas.": "Planche haute, épaules au-dessus des poignets.", "Lleva las rodillas al pecho alternando con ritmo, sin subir la cadera.": "Amène les genoux vers la poitrine en alternant en rythme, sans lever les hanches.", "Core firme: la espalda no rebota.": "Gainage ferme : le dos ne rebondit pas.", "Baja a sentadilla y apoya las manos.": "Descends en squat et pose les mains.", "Lanza los pies atrás a plancha firme (flexión opcional).": "Envoie les pieds en arrière en planche solide (pompe optionnelle).", "Recoge los pies y salta extendiendo la cadera.": "Ramène les pieds et saute en étendant les hanches.", "Aterriza suave con rodillas flexionadas.": "Atterris en douceur, genoux fléchis."};
    Object.keys(en8).forEach(function(k) { I18N.en.tx[k] = en8[k]; });
    Object.keys(fr8).forEach(function(k) { I18N.fr.tx[k] = fr8[k]; });
  })();


  (function extendI18N9() {
    var en9 = {"Rodillas que colapsan hacia dentro.": "Knees caving inward.", "Talones que se despegan del suelo.": "Heels lifting off the floor.", "Redondear la zona lumbar al fondo.": "Rounding your lower back at the bottom.", "Bajar tanto que la lumbar se levanta del respaldo.": "Going so deep your lower back lifts off the pad.", "Bloquear las rodillas con un golpe seco.": "Snapping your knees into lockout.", "Empujar solo con las puntas de los pies.": "Pushing only with your toes.", "Paso demasiado corto (castiga la rodilla).": "Step too short (hard on the knee).", "Rodilla delantera que viaja muy por delante de la punta.": "Front knee traveling far past your toes.", "Inclinar el torso hacia adelante.": "Leaning your torso forward.", "Dar la patada con impulso.": "Kicking the weight up with momentum.", "Hiperextender con golpe al final.": "Hyperextending with a snap at the end.", "Despegar la cadera del asiento.": "Lifting your hips off the seat.", "Arquear la zona lumbar.": "Arching your lower back.", "Usar impulso para completar la repetición.": "Using momentum to finish the rep.", "Trabajar solo medio rango.": "Working only half the range.", "Hiperextender la lumbar en la parte alta.": "Hyperextending your lower back at the top.", "Empujar con las puntas en vez de los talones.": "Pushing with your toes instead of your heels.", "Hacer rango corto por exceso de peso.": "Cutting the range short from too much weight.", "Rebotar abajo aprovechando el tendón.": "Bouncing at the bottom off the tendon.", "Rango corto y rápido.": "Short, fast range.", "Doblar las rodillas para ayudarse.": "Bending your knees to help.", "Rebotar la barra en el pecho.": "Bouncing the bar off your chest.", "Codos abiertos a 90° (castigan el hombro).": "Elbows flared to 90° (hard on the shoulder).", "Despegar los glúteos del banco.": "Lifting your glutes off the bench.", "Inclinar demasiado el banco (se vuelve press de hombro).": "Setting the bench too steep (it becomes a shoulder press).", "Rebotar la barra.": "Bouncing the bar.", "Arco lumbar exagerado.": "Excessive lower-back arch.", "Flexionar los codos y convertirlo en press.": "Bending your elbows and turning it into a press.", "Bajar más allá del rango cómodo del hombro.": "Going past your shoulder’s comfortable range.", "Usar un peso que rompa el arco.": "Using a weight that breaks the arc.", "Encoger los hombros hacia las orejas.": "Shrugging your shoulders toward your ears.", "Bajar de más con molestia en el hombro.": "Going too deep with shoulder discomfort.", "Balancear las piernas para ayudarse.": "Swinging your legs to help.", "Balancearse (kipping) para subir.": "Swinging (kipping) to get up.", "No bajar completo (medio rango).": "Not lowering all the way (half range).", "Encoger los hombros al colgar.": "Shrugging your shoulders while hanging.", "Dar tirones con la lumbar.": "Jerking with your lower back.", "Levantar el torso en cada repetición.": "Raising your torso on every rep.", "Tirar hacia el pecho con codos abiertos.": "Pulling to your chest with flared elbows.", "Mecerse hacia atrás para mover más peso.": "Rocking backward to move more weight.", "Jalar tras la nuca.": "Pulling behind your neck.", "Tirar solo con los brazos sin activar la espalda.": "Pulling only with your arms without engaging your back.", "Mecerse adelante y atrás.": "Rocking back and forth.", "Encoger los hombros.": "Shrugging your shoulders.", "Redondear la lumbar al estirar.": "Rounding your lower back on the stretch.", "Redondear la zona lumbar.": "Rounding your lower back.", "Dejar que la barra se aleje del cuerpo.": "Letting the bar drift away from your body.", "Rebotar el peso contra el suelo.": "Bouncing the weight off the floor.", "Arquear la lumbar en exceso.": "Over-arching your lower back.", "Empujar la barra hacia adelante.": "Pressing the bar forward.", "Impulsarse con las piernas (eso ya es push press).": "Driving with your legs (that’s a push press).", "Encoger los trapecios al subir.": "Shrugging your traps on the way up.", "Balancear el cuerpo para impulsar.": "Swinging your body for momentum.", "Subir por encima del hombro con peso excesivo.": "Raising above shoulder height with too much weight.", "Convertirlo en un remo bajo.": "Turning it into a low row.", "Usar demasiado peso.": "Using too much weight.", "Balancear la cadera para ayudar.": "Swinging your hips to help.", "Dejar que los codos viajen hacia adelante.": "Letting your elbows drift forward.", "Impulso con el torso.": "Momentum from your torso.", "Muñecas dobladas.": "Bent wrists.", "Dejar caer el peso en la bajada.": "Dropping the weight on the way down.", "Abrir los codos hacia afuera.": "Flaring your elbows out.", "Inclinarse encima del peso.": "Leaning over the weight.", "Medio rango con exceso de carga.": "Half range with too much load.", "Cadera caída o en pico.": "Hips sagging or piked.", "Hiperextender el cuello mirando al frente.": "Hyperextending your neck by looking forward.", "Aguantar sin respirar.": "Holding your breath.", "Tirar del cuello con las manos.": "Pulling on your neck with your hands.", "Subir completo despegando la lumbar.": "Coming all the way up, lifting your lower back.", "Usar impulso y velocidad.": "Using momentum and speed.", "Arquear la lumbar al bajar.": "Arching your lower back on the way down.", "Balancear las piernas.": "Swinging your legs.", "Doblar y estirar rodillas sin control.": "Bending and straightening your knees without control.", "Cadera alta en pico.": "Hips high in a pike.", "Hombros que se van hacia atrás.": "Shoulders drifting backward.", "Perder la línea del cuerpo por ir rápido.": "Losing your body line by going too fast.", "Lumbar arqueada en la plancha.": "Arched lower back in the plank.", "Aterrizar con las piernas rígidas.": "Landing with stiff legs.", "Sacrificar técnica por velocidad.": "Sacrificing technique for speed."};
    var fr9 = {"Rodillas que colapsan hacia dentro.": "Genoux qui rentrent vers l’intérieur.", "Talones que se despegan del suelo.": "Talons qui décollent du sol.", "Redondear la zona lumbar al fondo.": "Arrondir le bas du dos en position basse.", "Bajar tanto que la lumbar se levanta del respaldo.": "Descendre si bas que les lombaires décollent du dossier.", "Bloquear las rodillas con un golpe seco.": "Verrouiller les genoux d’un coup sec.", "Empujar solo con las puntas de los pies.": "Pousser seulement avec les pointes de pieds.", "Paso demasiado corto (castiga la rodilla).": "Pas trop court (ça punit le genou).", "Rodilla delantera que viaja muy por delante de la punta.": "Genou avant qui dépasse largement la pointe du pied.", "Inclinar el torso hacia adelante.": "Incliner le buste vers l’avant.", "Dar la patada con impulso.": "Donner le coup de pied avec de l’élan.", "Hiperextender con golpe al final.": "Hyperextension brutale en fin de mouvement.", "Despegar la cadera del asiento.": "Décoller les hanches du siège.", "Arquear la zona lumbar.": "Cambrer les lombaires.", "Usar impulso para completar la repetición.": "Utiliser l’élan pour finir la répétition.", "Trabajar solo medio rango.": "Travailler seulement à mi-amplitude.", "Hiperextender la lumbar en la parte alta.": "Hyperextension des lombaires en haut.", "Empujar con las puntas en vez de los talones.": "Pousser avec les pointes au lieu des talons.", "Hacer rango corto por exceso de peso.": "Réduire l’amplitude par excès de charge.", "Rebotar abajo aprovechando el tendón.": "Rebondir en bas en profitant du tendon.", "Rango corto y rápido.": "Amplitude courte et rapide.", "Doblar las rodillas para ayudarse.": "Plier les genoux pour s’aider.", "Rebotar la barra en el pecho.": "Faire rebondir la barre sur la poitrine.", "Codos abiertos a 90° (castigan el hombro).": "Coudes ouverts à 90° (ça punit l’épaule).", "Despegar los glúteos del banco.": "Décoller les fessiers du banc.", "Inclinar demasiado el banco (se vuelve press de hombro).": "Incliner trop le banc (ça devient un développé épaules).", "Rebotar la barra.": "Faire rebondir la barre.", "Arco lumbar exagerado.": "Cambrure lombaire exagérée.", "Flexionar los codos y convertirlo en press.": "Fléchir les coudes et le transformer en développé.", "Bajar más allá del rango cómodo del hombro.": "Descendre au-delà de l’amplitude confortable de l’épaule.", "Usar un peso que rompa el arco.": "Utiliser une charge qui casse l’arc.", "Encoger los hombros hacia las orejas.": "Hausser les épaules vers les oreilles.", "Bajar de más con molestia en el hombro.": "Descendre trop bas avec une gêne à l’épaule.", "Balancear las piernas para ayudarse.": "Balancer les jambes pour s’aider.", "Balancearse (kipping) para subir.": "Se balancer (kipping) pour monter.", "No bajar completo (medio rango).": "Ne pas redescendre complètement (mi-amplitude).", "Encoger los hombros al colgar.": "Hausser les épaules en suspension.", "Dar tirones con la lumbar.": "Donner des à-coups avec les lombaires.", "Levantar el torso en cada repetición.": "Relever le buste à chaque répétition.", "Tirar hacia el pecho con codos abiertos.": "Tirer vers la poitrine avec les coudes écartés.", "Mecerse hacia atrás para mover más peso.": "Se balancer en arrière pour déplacer plus de charge.", "Jalar tras la nuca.": "Tirer derrière la nuque.", "Tirar solo con los brazos sin activar la espalda.": "Tirer seulement avec les bras sans activer le dos.", "Mecerse adelante y atrás.": "Se balancer d’avant en arrière.", "Encoger los hombros.": "Hausser les épaules.", "Redondear la lumbar al estirar.": "Arrondir les lombaires à l’étirement.", "Redondear la zona lumbar.": "Arrondir le bas du dos.", "Dejar que la barra se aleje del cuerpo.": "Laisser la barre s’éloigner du corps.", "Rebotar el peso contra el suelo.": "Faire rebondir la charge au sol.", "Arquear la lumbar en exceso.": "Cambrer excessivement les lombaires.", "Empujar la barra hacia adelante.": "Pousser la barre vers l’avant.", "Impulsarse con las piernas (eso ya es push press).": "S’aider des jambes (c’est déjà un push press).", "Encoger los trapecios al subir.": "Hausser les trapèzes en montant.", "Balancear el cuerpo para impulsar.": "Balancer le corps pour prendre de l’élan.", "Subir por encima del hombro con peso excesivo.": "Monter au-dessus de l’épaule avec trop de charge.", "Convertirlo en un remo bajo.": "Le transformer en rowing bas.", "Usar demasiado peso.": "Utiliser trop de charge.", "Balancear la cadera para ayudar.": "Balancer les hanches pour aider.", "Dejar que los codos viajen hacia adelante.": "Laisser les coudes partir vers l’avant.", "Impulso con el torso.": "De l’élan avec le buste.", "Muñecas dobladas.": "Poignets pliés.", "Dejar caer el peso en la bajada.": "Laisser tomber la charge à la descente.", "Abrir los codos hacia afuera.": "Écarter les coudes vers l’extérieur.", "Inclinarse encima del peso.": "Se pencher au-dessus de la charge.", "Medio rango con exceso de carga.": "Mi-amplitude avec trop de charge.", "Cadera caída o en pico.": "Hanches affaissées ou en pic.", "Hiperextender el cuello mirando al frente.": "Hyperextension du cou en regardant devant.", "Aguantar sin respirar.": "Tenir sans respirer.", "Tirar del cuello con las manos.": "Tirer sur la nuque avec les mains.", "Subir completo despegando la lumbar.": "Monter complètement en décollant les lombaires.", "Usar impulso y velocidad.": "Utiliser élan et vitesse.", "Arquear la lumbar al bajar.": "Cambrer les lombaires à la descente.", "Balancear las piernas.": "Balancer les jambes.", "Doblar y estirar rodillas sin control.": "Plier et tendre les genoux sans contrôle.", "Cadera alta en pico.": "Hanches hautes en pic.", "Hombros que se van hacia atrás.": "Épaules qui partent en arrière.", "Perder la línea del cuerpo por ir rápido.": "Perdre l’alignement du corps en allant trop vite.", "Lumbar arqueada en la plancha.": "Lombaires cambrées en planche.", "Aterrizar con las piernas rígidas.": "Atterrir jambes raides.", "Sacrificar técnica por velocidad.": "Sacrifier la technique pour la vitesse."};
    Object.keys(en9).forEach(function(k) { I18N.en.tx[k] = en9[k]; });
    Object.keys(fr9).forEach(function(k) { I18N.fr.tx[k] = fr9[k]; });
  })();


  (function extendI18N10() {
    var en10 = {"© 2026 VILLUMINATIONS. Fitness &amp; Hábitos Sanos. Todos los derechos reservados.": "© 2026 VILLUMINATIONS. Fitness &amp; Healthy Habits. All rights reserved.", "Schumann · Tierra": "Schumann · Earth", "La resonancia del campo terrestre; calma y arraigo": "The resonance of the Earth’s field; calm and grounding", "Delta ultra · Descanso máximo": "Ultra delta · Deepest rest", "Pulso ultralento asociado al sueño profundo": "Ultra-slow pulse linked to deep sleep", "Semillas de papaya": "Papaya seeds", "Carpaína, papaína": "Carpaine, papain", "Tradición tropical contra parásitos; un estudio pequeño la respalda": "Tropical tradition against parasites; one small study supports it", "Dosis baja: 1 cdita molida en ayunas pocos días; evitar en embarazo — consulta a tu médico": "Low dose: 1 tsp ground, on an empty stomach for a few days; avoid in pregnancy — check with your doctor", "Clavo de olor": "Clove", "Eugenol": "Eugenol", "Uno de los antioxidantes más potentes; antimicrobiano tradicional": "One of the most potent antioxidants; a traditional antimicrobial", "1-2 clavos en infusión o molido en avena": "1-2 cloves in an infusion or ground into oats", "Epazote": "Epazote", "Ascaridol": "Ascaridole", "Hierba mexicana usada por siglos contra parásitos intestinales": "Mexican herb used for centuries against intestinal parasites", "Hojas frescas en frijoles (uso culinario); el aceite concentrado es tóxico — evítalo": "Fresh leaves in beans (culinary use); the concentrated oil is toxic — avoid it", "Tomillo": "Thyme", "Timol": "Thymol", "Antimicrobiano culinario clásico; aliado respiratorio tradicional": "A classic culinary antimicrobial; traditional respiratory ally", "En carnes, sopas e infusiones": "In meats, soups and infusions", "Diente de león": "Dandelion", "Potasio, taraxacina": "Potassium, taraxacin", "Amargo tradicional para apoyo digestivo, hepático y renal": "A traditional bitter for digestive, liver and kidney support", "Hojas tiernas en ensalada o infusión de raíz; diurético suave": "Young leaves in salads or a root infusion; a mild diuretic", "🌿 Botiquín Ancestral": "🌿 Ancestral Apothecary", "Preparaciones tradicionales con respaldo parcial de la ciencia — contadas con honestidad, sin promesas mágicas.": "Traditional preparations with partial scientific backing — told honestly, no magic promises.", "🥛 Leche dorada": "🥛 Golden milk", "Cúrcuma + pimienta negra + canela en leche tibia. Ritual ayurvédico nocturno: la piperina multiplica la absorción de la curcumina.": "Turmeric + black pepper + cinnamon in warm milk. A nightly Ayurvedic ritual: piperine multiplies curcumin absorption.", "🍋 Agua de jengibre y limón": "🍋 Ginger & lemon water", "Jengibre rallado + limón en agua tibia al despertar. Tradición digestiva presente en múltiples culturas.": "Grated ginger + lemon in warm water on waking. A digestive tradition found across many cultures.", "🎃 Semillas de calabaza en ayunas": "🎃 Pumpkin seeds on an empty stomach", "Remedio clásico contra parásitos intestinales (cucurbitina): 25-30 g molidas en ayunas. Siglos de tradición; evidencia moderna preliminar.": "A classic remedy against intestinal parasites (cucurbitin): 25-30 g ground, on an empty stomach. Centuries of tradition; modern evidence is preliminary.", "🍈 Agua de semillas de papaya": "🍈 Papaya seed water", "1 cdita de semillas molidas en ayunas por pocos días: tradición tropical para el intestino, con un pequeño estudio clínico a favor. Evitar en embarazo.": "1 tsp of ground seeds on an empty stomach for a few days: a tropical gut tradition, with one small clinical study in its favor. Avoid in pregnancy.", "⚠️ Sabiduría tradicional ≠ tratamiento. Si sospechas parásitos o un problema renal, acude a tu médico: estas preparaciones no sustituyen diagnóstico ni medicación.": "⚠️ Traditional wisdom ≠ treatment. If you suspect parasites or a kidney problem, see your doctor: these preparations do not replace diagnosis or medication."};
    var fr10 = {"© 2026 VILLUMINATIONS. Fitness &amp; Hábitos Sanos. Todos los derechos reservados.": "© 2026 VILLUMINATIONS. Fitness &amp; Habitudes Saines. Tous droits réservés.", "Schumann · Tierra": "Schumann · Terre", "La resonancia del campo terrestre; calma y arraigo": "La résonance du champ terrestre ; calme et ancrage", "Delta ultra · Descanso máximo": "Delta ultra · Repos maximal", "Pulso ultralento asociado al sueño profundo": "Pulsation ultra-lente associée au sommeil profond", "Semillas de papaya": "Graines de papaye", "Carpaína, papaína": "Carpaïne, papaïne", "Tradición tropical contra parásitos; un estudio pequeño la respalda": "Tradition tropicale contre les parasites ; une petite étude la soutient", "Dosis baja: 1 cdita molida en ayunas pocos días; evitar en embarazo — consulta a tu médico": "Faible dose : 1 c. à c. moulue à jeun quelques jours ; à éviter enceinte — consulte ton médecin", "Clavo de olor": "Clou de girofle", "Eugenol": "Eugénol", "Uno de los antioxidantes más potentes; antimicrobiano tradicional": "L’un des antioxydants les plus puissants ; antimicrobien traditionnel", "1-2 clavos en infusión o molido en avena": "1-2 clous en infusion ou moulus dans l’avoine", "Epazote": "Épazote", "Ascaridol": "Ascaridole", "Hierba mexicana usada por siglos contra parásitos intestinales": "Herbe mexicaine utilisée depuis des siècles contre les parasites intestinaux", "Hojas frescas en frijoles (uso culinario); el aceite concentrado es tóxico — evítalo": "Feuilles fraîches dans les haricots (usage culinaire) ; l’huile concentrée est toxique — à éviter", "Tomillo": "Thym", "Timol": "Thymol", "Antimicrobiano culinario clásico; aliado respiratorio tradicional": "Antimicrobien culinaire classique ; allié respiratoire traditionnel", "En carnes, sopas e infusiones": "Dans viandes, soupes et infusions", "Diente de león": "Pissenlit", "Potasio, taraxacina": "Potassium, taraxacine", "Amargo tradicional para apoyo digestivo, hepático y renal": "Amer traditionnel pour le soutien digestif, hépatique et rénal", "Hojas tiernas en ensalada o infusión de raíz; diurético suave": "Jeunes feuilles en salade ou infusion de racine ; diurétique doux", "🌿 Botiquín Ancestral": "🌿 Pharmacie Ancestrale", "Preparaciones tradicionales con respaldo parcial de la ciencia — contadas con honestidad, sin promesas mágicas.": "Préparations traditionnelles avec un soutien scientifique partiel — racontées honnêtement, sans promesses magiques.", "🥛 Leche dorada": "🥛 Lait d’or", "Cúrcuma + pimienta negra + canela en leche tibia. Ritual ayurvédico nocturno: la piperina multiplica la absorción de la curcumina.": "Curcuma + poivre noir + cannelle dans du lait tiède. Rituel ayurvédique du soir : la pipérine multiplie l’absorption de la curcumine.", "🍋 Agua de jengibre y limón": "🍋 Eau gingembre-citron", "Jengibre rallado + limón en agua tibia al despertar. Tradición digestiva presente en múltiples culturas.": "Gingembre râpé + citron dans de l’eau tiède au réveil. Tradition digestive présente dans de nombreuses cultures.", "🎃 Semillas de calabaza en ayunas": "🎃 Graines de courge à jeun", "Remedio clásico contra parásitos intestinales (cucurbitina): 25-30 g molidas en ayunas. Siglos de tradición; evidencia moderna preliminar.": "Remède classique contre les parasites intestinaux (cucurbitine) : 25-30 g moulues à jeun. Des siècles de tradition ; preuves modernes préliminaires.", "🍈 Agua de semillas de papaya": "🍈 Eau de graines de papaye", "1 cdita de semillas molidas en ayunas por pocos días: tradición tropical para el intestino, con un pequeño estudio clínico a favor. Evitar en embarazo.": "1 c. à c. de graines moulues à jeun quelques jours : tradition tropicale pour l’intestin, avec une petite étude clinique en sa faveur. À éviter enceinte.", "⚠️ Sabiduría tradicional ≠ tratamiento. Si sospechas parásitos o un problema renal, acude a tu médico: estas preparaciones no sustituyen diagnóstico ni medicación.": "⚠️ Sagesse traditionnelle ≠ traitement. Si tu suspectes des parasites ou un problème rénal, consulte ton médecin : ces préparations ne remplacent ni diagnostic ni médication."};
    Object.keys(en10).forEach(function(k) { I18N.en.tx[k] = en10[k]; });
    Object.keys(fr10).forEach(function(k) { I18N.fr.tx[k] = fr10[k]; });
  })();


  (function extendI18N11() {
    var en11 = {"🧅 Jarabe de cebolla y miel": "🧅 Onion & honey syrup", "Cebolla en rodajas reposada en miel unas horas: jarabe casero clásico para la garganta. La miel sí tiene evidencia real contra la tos (nunca en menores de 1 año).": "Sliced onion rested in honey for a few hours: the classic homemade throat syrup. Honey does have real evidence against cough (never under 1 year old).", "🌼 Infusión de manzanilla": "🌼 Chamomile infusion", "La apigenina de la manzanilla se une a receptores calmantes del cerebro. 30-60 min antes de dormir: la tradición universal del descanso.": "Chamomile’s apigenin binds to calming receptors in the brain. 30-60 min before bed: the universal rest tradition.", "🍚 Agua de arroz": "🍚 Rice water", "El agua del arroz cocido, suave con el estómago: tradición asiática y latina para días de digestión delicada.": "The water from cooked rice, gentle on the stomach: an Asian and Latin tradition for delicate-digestion days.", "🧄 Ajo reposado en ayunas": "🧄 Rested garlic on an empty stomach", "1 diente picado y reposado 10 min (activa la alicina). Tradición cardiovascular e inmune de la cocina de las abuelas.": "1 clove chopped and rested 10 min (activates allicin). A cardiovascular and immune tradition from grandma’s kitchen.", "‹ Desliza para ver más ›": "‹ Swipe to see more ›", "🔬 ¿Y las \"frecuencias que curan el cáncer\"?": "🔬 What about the \"cancer-curing frequencies\"?", "Quizá viste videos virales sobre 2127 Hz u otras \"frecuencias de Rife\" (2008, 880, 787, 727 Hz…). Vienen de Royal Raymond Rife (años 30), quien afirmó que cada enfermedad tiene una frecuencia capaz de destruirla. Sus resultados nunca se replicaron de forma independiente y la comunidad médica los considera pseudociencia.": "You may have seen viral videos about 2127 Hz or other \"Rife frequencies\" (2008, 880, 787, 727 Hz…). They come from Royal Raymond Rife (1930s), who claimed every disease has a frequency that can destroy it. His results were never independently replicated, and the medical community considers them pseudoscience.", "Lo que el sonido SÍ puede hacer por ti está aquí: bajar el estrés, acompañar tu sueño y tu enfoque — y eso, indirectamente, sí cuida tu sistema inmune. Si tú o alguien cercano enfrenta un cáncer, el camino es la medicina: diagnóstico y tratamiento con oncólogos.": "What sound CAN do for you is right here: lower stress, support your sleep and focus — and that, indirectly, does care for your immune system. If you or someone close is facing cancer, the path is medicine: diagnosis and treatment with oncologists.", "Campana de cristal": "Crystal bell", "El diapasón 4096 Hz de los baños de sonido; brillo y presencia": "The 4096 Hz tuner of sound baths; brightness and presence"};
    var fr11 = {"🧅 Jarabe de cebolla y miel": "🧅 Sirop d’oignon et miel", "Cebolla en rodajas reposada en miel unas horas: jarabe casero clásico para la garganta. La miel sí tiene evidencia real contra la tos (nunca en menores de 1 año).": "Oignon en tranches reposé dans du miel quelques heures : le sirop maison classique pour la gorge. Le miel a de vraies preuves contre la toux (jamais avant 1 an).", "🌼 Infusión de manzanilla": "🌼 Infusion de camomille", "La apigenina de la manzanilla se une a receptores calmantes del cerebro. 30-60 min antes de dormir: la tradición universal del descanso.": "L’apigénine de la camomille se lie aux récepteurs apaisants du cerveau. 30-60 min avant le coucher : la tradition universelle du repos.", "🍚 Agua de arroz": "🍚 Eau de riz", "El agua del arroz cocido, suave con el estómago: tradición asiática y latina para días de digestión delicada.": "L’eau du riz cuit, douce pour l’estomac : tradition asiatique et latine pour les jours de digestion délicate.", "🧄 Ajo reposado en ayunas": "🧄 Ail reposé à jeun", "1 diente picado y reposado 10 min (activa la alicina). Tradición cardiovascular e inmune de la cocina de las abuelas.": "1 gousse hachée et reposée 10 min (active l’allicine). Tradition cardiovasculaire et immunitaire de la cuisine des grands-mères.", "‹ Desliza para ver más ›": "‹ Fais glisser pour voir plus ›", "🔬 ¿Y las \"frecuencias que curan el cáncer\"?": "🔬 Et les « fréquences qui guérissent le cancer » ?", "Quizá viste videos virales sobre 2127 Hz u otras \"frecuencias de Rife\" (2008, 880, 787, 727 Hz…). Vienen de Royal Raymond Rife (años 30), quien afirmó que cada enfermedad tiene una frecuencia capaz de destruirla. Sus resultados nunca se replicaron de forma independiente y la comunidad médica los considera pseudociencia.": "Tu as peut-être vu des vidéos virales sur 2127 Hz ou d’autres « fréquences de Rife » (2008, 880, 787, 727 Hz…). Elles viennent de Royal Raymond Rife (années 30), qui affirmait que chaque maladie a une fréquence capable de la détruire. Ses résultats n’ont jamais été répliqués de façon indépendante et la communauté médicale les considère comme de la pseudoscience.", "Lo que el sonido SÍ puede hacer por ti está aquí: bajar el estrés, acompañar tu sueño y tu enfoque — y eso, indirectamente, sí cuida tu sistema inmune. Si tú o alguien cercano enfrenta un cáncer, el camino es la medicina: diagnóstico y tratamiento con oncólogos.": "Ce que le son PEUT faire pour toi est ici : réduire le stress, accompagner ton sommeil et ta concentration — et cela, indirectement, prend soin de ton système immunitaire. Si toi ou un proche affronte un cancer, le chemin est la médecine : diagnostic et traitement avec des oncologues.", "Campana de cristal": "Cloche de cristal", "El diapasón 4096 Hz de los baños de sonido; brillo y presencia": "Le diapason 4096 Hz des bains sonores ; éclat et présence"};
    Object.keys(en11).forEach(function(k) { I18N.en.tx[k] = en11[k]; });
    Object.keys(fr11).forEach(function(k) { I18N.fr.tx[k] = fr11[k]; });
  })();


  (function extendI18N12() {
    var t12en = {"f.freerange": "Pick between 20 and 20,000 Hz"};
    var t12fr = {"f.freerange": "Choisis entre 20 et 20 000 Hz"};
    var en12 = {"🎛️ Tono libre": "🎛️ Free tone", "Tono libre": "Free tone", "Escribe cualquier frecuencia y escúchala como tono puro. Volumen bajo y sesiones cortas.": "Type any frequency and hear it as a pure tone. Low volume, short sessions."};
    var fr12 = {"🎛️ Tono libre": "🎛️ Ton libre", "Tono libre": "Ton libre", "Escribe cualquier frecuencia y escúchala como tono puro. Volumen bajo y sesiones cortas.": "Saisis n’importe quelle fréquence et écoute-la en ton pur. Volume bas, sessions courtes."};
    Object.keys(t12en).forEach(function(k) { I18N.en.t[k] = t12en[k]; });
    Object.keys(t12fr).forEach(function(k) { I18N.fr.t[k] = t12fr[k]; });
    Object.keys(en12).forEach(function(k) { I18N.en.tx[k] = en12[k]; });
    Object.keys(fr12).forEach(function(k) { I18N.fr.tx[k] = fr12[k]; });
  })();


  (function extendI18N13() {
    var en13 = {"🍶 Caldo de huesos": "🍶 Bone broth", "Huesos cocidos a fuego lento 8-12 h: colágeno, glicina y minerales. Tradición milenaria de recuperación y básico moderno del descanso articular.": "Bones simmered 8-12 h: collagen, glycine and minerals. A millennia-old recovery tradition and a modern staple for joint rest.", "🧊 Contraste frío": "🧊 Cold finish", "Termina la ducha con 30-60 s de agua fría. Tradición nórdica; hoy se asocia a mejor recuperación percibida y a un estado de alerta inmediato.": "Finish your shower with 30-60 s of cold water. A Nordic tradition; today linked to better perceived recovery and instant alertness.", "🍃 Té de hojas de guayaba": "🍃 Guava leaf tea", "Infusión latinoamericana clásica para días de digestión revuelta. Sabor suave y siglos de uso en la mesa familiar.": "A classic Latin American infusion for upset-digestion days. Mild flavor and centuries at the family table.", "🌿 Agua de menta fresca": "🌿 Fresh mint water", "Hojas de menta machacadas en agua fría: frescura digestiva tras comidas pesadas, del Magreb a México.": "Crushed mint leaves in cold water: digestive freshness after heavy meals, from the Maghreb to Mexico."};
    var fr13 = {"🍶 Caldo de huesos": "🍶 Bouillon d’os", "Huesos cocidos a fuego lento 8-12 h: colágeno, glicina y minerales. Tradición milenaria de recuperación y básico moderno del descanso articular.": "Os mijotés 8-12 h : collagène, glycine et minéraux. Tradition millénaire de récupération et basique moderne du repos articulaire.", "🧊 Contraste frío": "🧊 Contraste froid", "Termina la ducha con 30-60 s de agua fría. Tradición nórdica; hoy se asocia a mejor recuperación percibida y a un estado de alerta inmediato.": "Termine ta douche par 30-60 s d’eau froide. Tradition nordique ; associée aujourd’hui à une meilleure récupération perçue et à une vigilance immédiate.", "🍃 Té de hojas de guayaba": "🍃 Thé de feuilles de goyave", "Infusión latinoamericana clásica para días de digestión revuelta. Sabor suave y siglos de uso en la mesa familiar.": "Infusion latino-américaine classique pour les jours de digestion difficile. Goût doux et des siècles à la table familiale.", "🌿 Agua de menta fresca": "🌿 Eau de menthe fraîche", "Hojas de menta machacadas en agua fría: frescura digestiva tras comidas pesadas, del Magreb a México.": "Feuilles de menthe écrasées dans l’eau froide : fraîcheur digestive après les repas copieux, du Maghreb au Mexique."};
    Object.keys(en13).forEach(function(k) { I18N.en.tx[k] = en13[k]; });
    Object.keys(fr13).forEach(function(k) { I18N.fr.tx[k] = fr13[k]; });
  })();


  (function exAnimEngine() {
    var A = {"squat": {"b": 3, "hot": "legs", "f": [[50, 16, 50, 30, 50, 56, 53, 75, 52, 92, 47, 75, 48, 92, 58, 38, 55, 30], [45, 37, 47, 48, 55, 67, 63, 75, 55, 92, 59, 77, 51, 92, 55, 55, 51, 48]]}, "lunge": {"b": 0, "hot": "legs", "f": [[50, 16, 50, 30, 50, 56, 56, 74, 58, 92, 44, 74, 42, 92, 54, 42, 56, 52], [48, 26, 48, 40, 48, 62, 62, 74, 66, 92, 38, 80, 30, 92, 52, 52, 54, 62]]}, "hinge": {"b": 1, "hot": "back", "f": [[50, 16, 50, 30, 50, 56, 52, 75, 52, 92, 48, 75, 48, 92, 54, 44, 55, 58], [68, 38, 62, 44, 48, 58, 54, 76, 52, 92, 50, 76, 48, 92, 64, 58, 66, 72]]}, "calf": {"b": 2, "hot": "legs", "f": [[50, 18, 50, 32, 50, 58, 51, 76, 51, 92, 49, 76, 49, 92, 55, 44, 56, 56], [50, 12, 50, 26, 50, 52, 51, 71, 51, 86, 49, 71, 49, 86, 55, 38, 56, 50]]}, "bench": {"b": 1, "hot": "chest", "lie": 1, "f": [[22, 76, 32, 74, 54, 76, 68, 64, 80, 90, 70, 66, 84, 90, 32, 60, 32, 48], [22, 76, 32, 74, 54, 76, 68, 64, 80, 90, 70, 66, 84, 90, 34, 70, 33, 64]]}, "pressV": {"b": 1, "hot": "arms", "f": [[50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 58, 30, 56, 20], [50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 60, 42, 58, 32]]}, "pullV": {"b": 0, "hot": "back", "f": [[50, 30, 50, 42, 50, 66, 52, 80, 52, 92, 48, 80, 48, 92, 58, 28, 58, 14], [50, 20, 50, 32, 50, 58, 53, 74, 52, 90, 47, 74, 48, 90, 60, 20, 58, 14]]}, "pullH": {"b": 1, "hot": "back", "f": [[62, 30, 58, 38, 48, 58, 54, 76, 52, 92, 50, 76, 48, 92, 66, 50, 70, 60], [62, 30, 58, 38, 48, 58, 54, 76, 52, 92, 50, 76, 48, 92, 60, 44, 56, 50]]}, "curl": {"b": 2, "hot": "arms", "f": [[50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 53, 46, 55, 58], [50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 53, 46, 50, 34]]}, "ext": {"b": 2, "hot": "arms", "f": [[50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 56, 40, 52, 30], [50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 56, 40, 60, 52]]}, "raise": {"b": 2, "hot": "arms", "f": [[50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 54, 44, 56, 54], [50, 18, 50, 32, 50, 58, 52, 76, 52, 92, 48, 76, 48, 92, 62, 34, 72, 32]]}, "seated": {"b": 0, "hot": "legs", "f": [[42, 26, 42, 40, 44, 62, 60, 62, 60, 88, 58, 64, 58, 88, 48, 50, 50, 60], [42, 26, 42, 40, 44, 62, 60, 62, 76, 60, 58, 64, 72, 64, 48, 50, 50, 60]]}, "plank": {"b": 0, "hot": "core", "lie": 1, "f": [[20, 62, 30, 64, 54, 68, 68, 72, 84, 88, 70, 74, 86, 90, 30, 78, 28, 90], [20, 64, 30, 66, 54, 70, 68, 74, 84, 88, 70, 76, 86, 90, 30, 80, 28, 90]]}, "crunch": {"b": 0, "hot": "core", "lie": 1, "f": [[22, 78, 32, 78, 54, 80, 64, 66, 76, 88, 66, 68, 80, 90, 26, 70, 22, 72], [30, 66, 38, 70, 54, 80, 64, 66, 76, 88, 66, 68, 80, 90, 34, 60, 30, 60]]}};
    var MAP = {"squat": "squat", "legpress": "squat", "lunge": "lunge", "legext": "seated", "legcurl": "seated", "hipthrust": "hinge", "calf": "calf", "bench": "bench", "incline": "bench", "fly": "bench", "dips": "pressV", "pullup": "pullV", "row": "pullH", "lat": "pullV", "cablerow": "pullH", "dead": "hinge", "ohp": "pressV", "lateral": "raise", "facepull": "pullH", "curl": "curl", "hammer": "curl", "tricep": "ext", "plank": "plank", "crunch": "crunch", "legraise": "crunch", "mclimber": "plank", "burpee": "squat"};
    var CYAN = '#05D9E8', PINK = '#FF2A6D';
    function lerp(a, b, t) { return a + (b - a) * t; }
    window.__exAnimStart = function(exId, cv) {
      var arch = A[MAP[exId]];
      if (!arch || !cv || !cv.getContext) { if (cv) cv.style.display = 'none'; return; }
      var ctx = cv.getContext('2d');
      var t0 = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();
      var frames = arch.f, n = frames.length, DUR = 1300;
      function pt(f, k, s) { return [f[k * 2] * s + (cv.width - 100 * s) / 2, f[k * 2 + 1] * s]; }
      function line(p, q) { ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(q[0], q[1]); ctx.stroke(); }
      function limb(p, q, w, col, far) {
        ctx.globalAlpha = far ? 0.35 : 1;
        ctx.strokeStyle = 'rgba(0,0,0,0.55)'; ctx.lineWidth = w + 3; ctx.lineCap = 'round'; line(p, q);
        ctx.shadowColor = col; ctx.shadowBlur = far ? 3 : 10;
        ctx.strokeStyle = col; ctx.lineWidth = w; line(p, q);
        ctx.shadowBlur = 0;
        if (!far) { ctx.strokeStyle = 'rgba(255,255,255,0.75)'; ctx.lineWidth = Math.max(1.4, w * 0.26);
          line([p[0] - 1.4, p[1] - 1.4], [q[0] - 1.4, q[1] - 1.4]); }
        ctx.globalAlpha = 1;
      }
      function joint(p, r, col) {
        var g = ctx.createRadialGradient(p[0] - r * 0.4, p[1] - r * 0.4, r * 0.15, p[0], p[1], r);
        g.addColorStop(0, '#ffffff'); g.addColorStop(0.4, col); g.addColorStop(1, '#062026');
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p[0], p[1], r, 0, 6.2832); ctx.fill();
      }
      function metalBar(x1, y1, x2, y2, w) {
        var g = ctx.createLinearGradient(x1, y1 - 3, x1, y1 + 3);
        g.addColorStop(0, '#f2f4fa'); g.addColorStop(0.5, '#8d93a8'); g.addColorStop(1, '#f2f4fa');
        ctx.strokeStyle = g; ctx.lineWidth = w; ctx.lineCap = 'round';
        ctx.shadowColor = 'rgba(255,255,255,0.5)'; ctx.shadowBlur = 6;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke(); ctx.shadowBlur = 0;
      }
      function draw(now) {
        if (!cv.isConnected) return;
        var el = ((now - t0) % (DUR * n)) / DUR;
        var i0 = Math.floor(el) % n, i1 = (i0 + 1) % n;
        var tt = el - Math.floor(el); tt = 0.5 - 0.5 * Math.cos(tt * Math.PI);
        var f = [], a0 = frames[i0], a1f = frames[i1];
        for (var k = 0; k < 18; k++) f.push(lerp(a0[k], a1f[k], tt));
        var s = cv.height / 105;
        ctx.clearRect(0, 0, cv.width, cv.height);
        var h = pt(f, 0, s), sh = pt(f, 1, s), hp = pt(f, 2, s), k1 = pt(f, 3, s), an1 = pt(f, 4, s),
            k2 = pt(f, 5, s), an2 = pt(f, 6, s), e = pt(f, 7, s), w = pt(f, 8, s);
        var gy = 93 * s;
        var fg = ctx.createLinearGradient(0, gy - 4, 0, gy + 10);
        fg.addColorStop(0, 'rgba(5,217,232,0.18)'); fg.addColorStop(1, 'rgba(5,217,232,0)');
        ctx.fillStyle = fg; ctx.fillRect(10, gy - 2, cv.width - 20, 12);
        ctx.strokeStyle = 'rgba(255,255,255,0.12)'; ctx.lineWidth = 1; line([10, gy], [cv.width - 10, gy]);
        ctx.fillStyle = 'rgba(0,0,0,0.5)';
        ctx.beginPath(); ctx.ellipse((an1[0] + an2[0]) / 2, gy + 3, 27, 5, 0, 0, 6.2832); ctx.fill();
        if (arch.lie && arch.b === 1) { ctx.strokeStyle = '#2a2d3d'; ctx.lineWidth = 8; ctx.lineCap = 'round';
          line([sh[0] - 16, hp[1] + 8], [hp[0] + 10, hp[1] + 8]); }
        var legC = arch.hot === 'legs' ? PINK : CYAN;
        var armC = (arch.hot === 'arms' || arch.hot === 'chest') ? PINK : CYAN;
        var bodC = (arch.hot === 'back' || arch.hot === 'core') ? PINK : CYAN;
        limb(hp, k2, 6, legC, true); limb(k2, an2, 6, legC, true);
        limb([sh[0] - 5, sh[1] + 2], [e[0] - 6, e[1] + 2], 5, armC, true);
        limb(hp, sh, 7.5, bodC, false);
        limb(hp, k1, 6.5, legC, false); limb(k1, an1, 6, legC, false);
        limb(an1, [an1[0] + 9, an1[1]], 5, legC, false);
        limb(sh, e, 5.5, armC, false); limb(e, w, 5, armC, false);
        limb(sh, [h[0], h[1] + 5], 4, bodC, false);
        joint(hp, 4.6, bodC); joint(k1, 3.8, legC); joint(sh, 4.4, bodC); joint(e, 3.4, armC);
        var hg = ctx.createRadialGradient(h[0] - 2.5, h[1] - 2.5, 1.5, h[0], h[1], 7.5);
        hg.addColorStop(0, '#ffffff'); hg.addColorStop(0.45, bodC); hg.addColorStop(1, '#051d22');
        ctx.shadowColor = bodC; ctx.shadowBlur = 14;
        ctx.fillStyle = hg; ctx.beginPath(); ctx.arc(h[0], h[1], 7, 0, 6.2832); ctx.fill();
        ctx.shadowBlur = 0;
        if (arch.b === 1) { metalBar(w[0] - 21, w[1], w[0] + 21, w[1], 3.5);
          joint([w[0] - 21, w[1]], 5.2, '#aeb4c8'); joint([w[0] + 21, w[1]], 5.2, '#aeb4c8'); }
        if (arch.b === 2) { joint(w, 5, '#aeb4c8'); }
        if (arch.b === 3) { metalBar(sh[0] - 19, sh[1] - 3, sh[0] + 19, sh[1] - 3, 3.5); }
        requestAnimationFrame(draw);
      }
      requestAnimationFrame(draw);
    };
  })();

  window.EXGIF = {"squat": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Squat_gif.gif?v=1784571345"], "legpress": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Legpress-_prensa_de_piernas.gif?v=1784571346", "https://cdn.shopify.com/s/files/1/0599/8467/4865/files/legpress_gif.gif?v=1784571346"], "lunge": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Lunge-_zancada.gif?v=1784571346", "https://cdn.shopify.com/s/files/1/0599/8467/4865/files/lunge_gif.gif?v=1784571345"], "legext": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Leg-extension_extension_de_quadriceps.gif?v=1784571346", "https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Legextension_gif.gif?v=1784571346"], "legcurl": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Leg-curl_curl_femoral.gif?v=1784571345"], "hipthrust": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/hip-thrust.gif?v=1784571346"], "calf": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Calf-extension.gif?v=1784571345"], "bench": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Bench-presa.gif?v=1784571346"], "incline": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Incline-bench_press_inclinado.gif?v=1784571345"], "fly": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Fly-_aperturas_mancuerna.gif?v=1784571346"], "dips": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Dips-_fondos_en_paralelas.gif?v=1784571346"], "pullup": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Pull-up.gif?v=1784571346"], "row": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/row-with_bar_remo_con_barra.gif?v=1784571346"], "lat": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Lat-jalon_al_pecho.gif?v=1784571346"], "cablerow": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Low-cablerow.gif?v=1784571346"], "dead": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Deadlift_gif.gif?v=1784571346"], "ohp": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/ohp-press_militar.gif?v=1784571345", "https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Burpee_gif.gif?v=1784571345"], "lateral": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/elevaciones-laterales.gif?v=1784571346"], "facepull": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/face-pull_gif.gif?v=1784571346"], "curl": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/curl_gif.gif?v=1784571346"], "hammer": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Hammer-curl_gif.gif?v=1784571346"], "tricep": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/extensio-n_de_triceps_gif.gif?v=1784571346"], "plank": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Plank_gif.gif?v=1784571345"], "crunch": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/crunch-abdominal_gif.gif?v=1784571346"], "legraise": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/legraise_gif.gif?v=1784571346"], "mclimber": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/mountain-climbers_gif.gif?v=1784571345"], "burpee": ["https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Burpee.gif?v=1784571346", "https://cdn.shopify.com/s/files/1/0599/8467/4865/files/Push-up_gif.gif?v=1784571346"]};
  (function extendI18N14() {
    var t14en = {"gif.load": "Loading\u2026"};
    var t14fr = {"gif.load": "Chargement…", "gif.retry": "Nouvelle tentative…", "gif.slow": "La démo est lente… vérifie ta connexion"};
    var en14 = {"Demostraci\u00f3n del movimiento": "Movement demonstration"};
    var fr14 = {"Demostración del movimiento": "Démonstration du mouvement"};
    Object.keys(t14en).forEach(function(k) { I18N.en.t[k] = t14en[k]; });
    Object.keys(t14fr).forEach(function(k) { I18N.fr.t[k] = t14fr[k]; });
    Object.keys(en14).forEach(function(k) { I18N.en.tx[k] = en14[k]; });
    Object.keys(fr14).forEach(function(k) { I18N.fr.tx[k] = fr14[k]; });
  })();

  window.__exgifLightbox = function(url, alt) {
    var lb = document.getElementById('exgif-lb');
    if (!lb) {
      lb = document.createElement('div'); lb.id = 'exgif-lb';
      var im = document.createElement('img'); im.id = 'exgif-lb-img'; lb.appendChild(im);
      var x = document.createElement('div'); x.className = 'lb-x'; x.textContent = '✕';
      lb.appendChild(x);
      lb.addEventListener('click', function() { lb.classList.remove('on'); });
      document.body.appendChild(lb);
    }
    var im2 = document.getElementById('exgif-lb-img');
    im2.src = url; im2.alt = alt || '';
    lb.classList.add('on');
  };
  (function extendI18N15() {
    var en15 = {"Demostración · pulsa para ampliar": "Demonstration · tap to enlarge", "Toca los ángulos · pulsa para ampliar": "Tap the angles · tap to enlarge"};
    var fr15 = {"Demostración · pulsa para ampliar": "Démonstration · touche pour agrandir", "Toca los ángulos · pulsa para ampliar": "Touche les angles · touche pour agrandir"};
    Object.keys(en15).forEach(function(k) { I18N.en.tx[k] = en15[k]; });
    Object.keys(fr15).forEach(function(k) { I18N.fr.tx[k] = fr15[k]; });
  })();

  var UI_ORIG = null;
  /* Diccionario activo. Devuelve null si aún no está listo (estos helpers se
     invocan en renders que corren ANTES de que I18N esté declarado). */
  function _dict() {
    try {
      if (typeof I18N === 'undefined' || !I18N) return null;
      if (typeof CUR_LANG === 'undefined' || !CUR_LANG || CUR_LANG === 'es') return null;
      return I18N[CUR_LANG] || null;
    } catch (e) { return null; }
  }
  function TX(es) {
    var D = _dict();
    if (D && D.tx && D.tx[es]) return D.tx[es];
    try { if (typeof CUR_LANG !== 'undefined' && CUR_LANG !== 'es' && typeof es === 'string' && /[A-Za-z\u00c1\u00c9\u00cd\u00d3\u00da\u00d1\u00e1\u00e9\u00ed\u00f3\u00fa\u00f1]{3}/.test(es)) (window.__i18nMiss = window.__i18nMiss || {})[es] = 1; } catch(e) {}
    return es;
  }
  function TXDISH(s) {
    try {
      if (typeof CUR_LANG === 'undefined' || CUR_LANG === 'es' || !window.DISHLEX || !window.DISHLEX[CUR_LANG]) return s;
      var Lx = window.DISHLEX[CUR_LANG], out = s;
      window.DISHKEYS.forEach(function(k) { if (out.indexOf(k) !== -1) out = out.split(k).join(Lx[k]); });
      return out;
    } catch (e) { return s; }
  }
  function T(k, es) {
    var D = _dict();
    if (D && D.t && D.t[k]) return D.t[k];
    try { if (typeof CUR_LANG !== 'undefined' && CUR_LANG !== 'es' && typeof es === 'string' && /[A-Za-z\u00c1\u00c9\u00cd\u00d3\u00da\u00d1\u00e1\u00e9\u00ed\u00f3\u00fa\u00f1]{3}/.test(es)) (window.__i18nMiss = window.__i18nMiss || {})[es] = '[' + k + ']'; } catch(e) {}
    return es;
  }
  window.__i18nReport = function() {
    var m = window.__i18nMiss || {}, a = Object.keys(m);
    console.log('[VILL i18n] textos pendientes de traducir: ' + a.length);
    a.forEach(function(s) { console.log('  \u00b7 ' + (m[s] === 1 ? '' : m[s] + ' ') + s); });
    return a;
  };
  function applyLang(l) {
    CUR_LANG = l;
    try { var hubEl = document.getElementById('vill-hub'); if (hubEl) hubEl.setAttribute('lang', l); } catch(e) {}
    try { localStorage.setItem('vill_lang', l); } catch(e) {}
    var pill = document.getElementById('lang-switch');
    if (pill) pill.querySelectorAll('button').forEach(function(b) { b.classList.toggle('active', b.dataset.l === l); });
    var q = function(s) { return document.querySelector(s); };
    // .hero-title ya no es un <h1> (ver el marcado): se busca por clase, que
    // es como se buscaba, asi que el cambio de etiqueta no le afecta.
    var tagEl = q('#hero-section .hero-tag'), titleEl = q('#hero-section .hero-title'), subEl = q('#hero-section .hero-sub');
    var b1 = q('#hero-section .hero-btns .btn-primary'), b2 = q('#hero-section .hero-btns .btn-outline');
    var statEls = document.querySelectorAll('#hero-section .hero-stat span');
    if (!UI_ORIG) {
      UI_ORIG = { tag: tagEl.innerHTML, title: titleEl.innerHTML, sub: subEl.innerHTML, b1: b1.innerHTML, b2: b2.innerHTML, stats: [], titles: {}, btns: {} };
      statEls.forEach(function(s) { UI_ORIG.stats.push(s.textContent); });
      SEC_IDS.forEach(function(id) { var h = q('#' + id + ' .section-title'); if (h) UI_ORIG.titles[id] = h.innerHTML; });
      Object.keys(I18N.en.btns).forEach(function(id) { var b = document.getElementById(id); if (b) UI_ORIG.btns[id] = b.innerHTML; });
      UI_ORIG.idxTitle = q('#hub-index-title').innerHTML;
      UI_ORIG.idxSub = q('#hub-index-sub').innerHTML;
      UI_ORIG.idx = {};
      document.querySelectorAll('.hub-card').forEach(function(c) {
        UI_ORIG.idx[c.dataset.sec] = [c.querySelector('.hc-name').innerHTML, c.querySelector('.hc-desc').innerHTML];
      });
      UI_ORIG.t = {};
      document.querySelectorAll('[data-i18n]').forEach(function(el) { UI_ORIG.t[el.dataset.i18n] = el.innerHTML; });
      UI_ORIG.txEls = [];
      document.querySelectorAll('[data-tx]').forEach(function(el) { UI_ORIG.txEls.push([el, el.innerHTML]); });
      UI_ORIG.ph = {};
      UI_ORIG.txEls.forEach(function(p) { p[0].innerHTML = TX(p[1]); });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el) { UI_ORIG.ph[el.dataset.i18nPh] = el.placeholder; });
    }
    var D = (l === 'es') ? null : I18N[l];
    tagEl.innerHTML = D ? D.tag : UI_ORIG.tag;
    titleEl.innerHTML = D ? D.title : UI_ORIG.title;
    subEl.innerHTML = D ? D.sub : UI_ORIG.sub;
    b1.innerHTML = D ? D.b1 : UI_ORIG.b1;
    b2.innerHTML = D ? D.b2 : UI_ORIG.b2;
    statEls.forEach(function(s, i) { s.textContent = D ? (D.stats[i] || UI_ORIG.stats[i]) : UI_ORIG.stats[i]; });
    SEC_IDS.forEach(function(id) {
      var h = q('#' + id + ' .section-title');
      if (h) h.innerHTML = D ? (D.titles[id] || UI_ORIG.titles[id]) : UI_ORIG.titles[id];
    });
    Object.keys(UI_ORIG.btns).forEach(function(id) {
      var b = document.getElementById(id);
      if (b) b.innerHTML = D ? (D.btns[id] || UI_ORIG.btns[id]) : UI_ORIG.btns[id];
    });
    var it = q('#hub-index-title'), is = q('#hub-index-sub');
    if (it) it.innerHTML = D ? D.idxTitle : UI_ORIG.idxTitle;
    if (is) is.innerHTML = D ? D.idxSub : UI_ORIG.idxSub;
    document.querySelectorAll('.hub-card').forEach(function(c) {
      var o = UI_ORIG.idx[c.dataset.sec];
      var t = (D && D.idx[c.dataset.sec]) ? D.idx[c.dataset.sec] : o;
      if (t) { c.querySelector('.hc-name').innerHTML = t[0]; c.querySelector('.hc-desc').innerHTML = t[1]; }
    });
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var k = el.dataset.i18n;
      var v = (D && D.t && D.t[k]) ? D.t[k] : UI_ORIG.t[k];
      if (v != null) el.innerHTML = v;
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el) {
      var k = el.dataset.i18nPh;
      var v = (D && D.t && D.t['ph.' + k]) ? D.t['ph.' + k] : UI_ORIG.ph[k];
      if (v != null) el.placeholder = v;
    });
    if (window.__villReady) {
      try {
        renderRoutine(); renderLibrary(); renderChips();
        renderLevel(); renderLeaderboard(); updateHealthPanel();
        if (window.__renderBot) window.__renderBot();
        if (window.__renderFreq) window.__renderFreq();
        if (window.__renderSleepW) { try { window.__renderSleepW(); } catch(e) {} }
        if (window.__updFreeBtn) { try { window.__updFreeBtn(); } catch(e) {} }
        try { if (typeof renderMedProgram === 'function') renderMedProgram(); } catch(e) {}
        if (window.__renderDietSel) { try { window.__renderDietSel(); } catch(e) {} }
        if (window.__renderMacros) { try { window.__renderMacros(); } catch(e) {} }
      } catch(e) {}
    }
    var note = document.getElementById('i18n-note');
    if (D) {
      if (!note) {
        note = document.createElement('p'); note.id = 'i18n-note'; note.className = 'i18n-note';
        var anchorEl = document.getElementById('hero-motto') || subEl;
        anchorEl.parentNode.insertBefore(note, anchorEl.nextSibling);
      }
      note.textContent = TX(D.note);
    } else if (note) { note.parentNode.removeChild(note); }
    var m = document.getElementById('hero-motto');
    if (m) m.textContent = '💬 ' + (MOTTOS[l] || MOTTOS.es)[0];
  }
  (function initLang() {
    var pill = document.getElementById('lang-switch');
    if (!pill) return;
    pill.addEventListener('click', function(e) {
      var b = e.target.closest('button');
      if (b && b.dataset.l) applyLang(b.dataset.l);
    });
    var saved = null;
    try { saved = localStorage.getItem('vill_lang'); } catch(e) {}
    var nav = (navigator.language || 'es').slice(0, 2).toLowerCase();
    var start = saved || (nav === 'es' ? 'es' : (nav === 'fr' ? 'fr' : 'en'));
    applyLang(start);
  })();

  renderRoutine(); renderChips(); renderLibrary(); initLibNav();
  window.__villReady = true;
  try { applyLang(CUR_LANG); } catch(e) {}

  /* =====================================================================
     CRONÓMETRO VISUAL DE RESPIRACIÓN
     ===================================================================== */
  (function initBreath() {
    var PATTERNS = {
      '478': [
        { label: 'Inhala', dur: 4, dir: 'in',  color: '#FF2A6D' },
        { label: 'Retén',  dur: 7, dir: 'hold', color: '#05D9E8' },
        { label: 'Exhala', dur: 8, dir: 'out', color: '#FFD700' }
      ],
      'box': [
        { label: 'Inhala', dur: 4, dir: 'in',  color: '#FF2A6D' },
        { label: 'Retén',  dur: 4, dir: 'hold', color: '#05D9E8' },
        { label: 'Exhala', dur: 4, dir: 'out', color: '#FFD700' },
        { label: 'Pausa',  dur: 4, dir: 'hold2', color: '#9B59B6' }
      ],
      'coherente': [
        { label: 'Inhala', dur: 5, dir: 'in',  color: '#FF2A6D' },
        { label: 'Exhala', dur: 5, dir: 'out', color: '#FFD700' }
      ]
    };
    var pattern = '478';
    var running = false;
    var rafId = null;

    var circle = document.getElementById('breath-circle');
    var ringEl = document.getElementById('breath-ring');
    var countEl = document.getElementById('breath-count');
    var phaseEl = document.getElementById('breath-phase');
    var cycleEl = document.getElementById('breath-cycle-label');

    document.querySelectorAll('.breath-pattern').forEach(function(b) {
      b.addEventListener('click', function() {
        document.querySelectorAll('.breath-pattern').forEach(function(x) { x.classList.remove('active'); });
        this.classList.add('active');
        pattern = this.dataset.pattern;
        if (running) stop();
      });
    });

    function setCircle(scale, durSec) {
      circle.style.transition = durSec > 0 ? 'transform ' + durSec + 's linear' : 'none';
      circle.style.transform = 'scale(' + scale + ')';
    }
    function setRing(pct, color) {
      ringEl.style.background = 'conic-gradient(' + color + ' ' + (pct * 360) + 'deg, #2a2a3a 0deg)';
    }
    function reset() {
      setCircle(0.62, 0);
      setRing(0, '#2a2a3a');
      countEl.textContent = '–';
      phaseEl.textContent = T('breath.ready', 'Listo');
      phaseEl.style.color = '#cdd';
      cycleEl.textContent = '';
      circle.style.borderColor = 'rgba(5,217,232,0.5)';
    }
    function stop() {
      running = false;
      if (rafId) cancelAnimationFrame(rafId);
      reset();
    }
    document.getElementById('breath-stop').addEventListener('click', function() { stop(); });

    document.getElementById('breath-start').addEventListener('click', function() {
      if (running) return;
      running = true;
      var steps = PATTERNS[pattern];
      var totalCycles = parseInt(document.getElementById('breath-cycles').value, 10);
      var cycle = 0, stepIdx = 0;
      var stepStart = performance.now();

      function beginStep() {
        var s = steps[stepIdx];
        phaseEl.textContent = TX(s.label);
        phaseEl.style.color = s.color;
        circle.style.borderColor = s.color;
        cycleEl.textContent = 'Ciclo ' + (cycle + 1) + ' de ' + totalCycles;
        if (s.dir === 'in') setCircle(1.0, s.dur);
        else if (s.dir === 'out') setCircle(0.62, s.dur);
        // hold: se queda donde está
        stepStart = performance.now();
      }
      beginStep();

      function tick(now) {
        if (!running) return;
        var s = steps[stepIdx];
        var elapsed = (now - stepStart) / 1000;
        var remaining = Math.max(0, s.dur - elapsed);
        countEl.textContent = Math.ceil(remaining);
        setRing(Math.min(1, elapsed / s.dur), s.color);
        if (elapsed >= s.dur) {
          stepIdx++;
          if (stepIdx >= steps.length) {
            stepIdx = 0;
            cycle++;
            if (cycle >= totalCycles) {
              running = false;
              phaseEl.textContent = '✓ Completado';
              phaseEl.style.color = '#2ECC71';
              countEl.textContent = '✓';
              setRing(1, '#2ECC71');
              showToast(T('t.breath', 'Sesión de respiración completada'));
              setTimeout(reset, 2500);
              return;
            }
          }
          beginStep();
        }
        rafId = requestAnimationFrame(tick);
      }
      rafId = requestAnimationFrame(tick);
    });
    reset();
  })();

  /* =====================================================================
     FRECUENCIAS — Solfeggio (tono puro) + Binaurales (dos canales)
     ===================================================================== */
  (function initFrequencies() {
    var SOLFEGGIO = [
      { id: 's174', hz: 174, name: 'Alivio Profundo',   desc: 'Relajación física y descarga de tensión' },
      { id: 's285', hz: 285, name: 'Regeneración',      desc: 'Sensación de restauración y equilibrio' },
      { id: 's396', hz: 396, name: 'Liberación',        desc: 'Suelta el miedo y la culpa; base emocional' },
      { id: 's417', hz: 417, name: 'Cambio',            desc: 'Facilita transiciones y deshace bloqueos' },
      { id: 's432', hz: 432, name: 'Armonía Natural',   desc: 'Afinación suave; calma y coherencia' },
      { id: 's528', hz: 528, name: 'Reparación',        desc: 'La "frecuencia del amor"; renovación y vitalidad' },
      { id: 's639', hz: 639, name: 'Conexión',          desc: 'Relaciones, empatía y comunicación' },
      { id: 's741', hz: 741, name: 'Despertar',         desc: 'Intuición, claridad y expresión' },
      { id: 's852', hz: 852, name: 'Visión Interior',   desc: 'Orden mental y equilibrio espiritual' },
      { id: 's963', hz: 963, name: 'Consciencia Plena', desc: 'Conexión superior y unidad' },
      { id: 'p4096', hz: 4096, name: 'Campana de cristal', desc: 'El diapasón 4096 Hz de los baños de sonido; brillo y presencia' }
    ];
    var BINAURAL = [
      { id: 'b25',  beat: 2.5,  name: 'Delta · Sueño Profundo', desc: 'Descanso nocturno y recuperación total' },
      { id: 'b45',  beat: 4.5,  name: 'Theta baja · Sanación',  desc: 'Relajación muy profunda, pre-sueño' },
      { id: 'b6',   beat: 6,    name: 'Theta · Meditación',     desc: 'Estados meditativos profundos y creatividad' },
      { id: 'b783', beat: 7.83, name: 'Schumann · Tierra',      desc: 'La resonancia de la Tierra; enraizamiento' },
      { id: 'b10',  beat: 10,   name: 'Alpha · Relajación',     desc: 'Calma alerta, ideal después de entrenar' },
      { id: 'b14',  beat: 14,   name: 'Beta · Enfoque',         desc: 'Concentración estable para estudiar o trabajar' },
      { id: 'b40',  beat: 40,   name: 'Gamma · Despertar',      desc: 'Alerta máxima, claridad y procesamiento mental' },
      /* Aqui habia un SEGUNDO Schumann con el mismo id 'b783' que el de arriba.
         La lista se busca por id, asi que la segunda tarjeta nunca sonaba: al
         pulsarla arrancaba la primera, y como el estado tambien se compara por
         id, las DOS se encendian a la vez. Una tarjeta que no se puede
         reproducir y dos que dicen estar sonando. Retirada la copia. */
      { id: 'b05',  beat: 0.5,  name: 'Delta ultra · Descanso máximo', desc: 'Pulso ultralento asociado al sueño profundo' }
    ];
    var CARRIER = 200; // Hz portadora para binaurales

    var grid = document.getElementById('freq-grid');
    var nowPlaying = document.getElementById('freq-now-playing');
    var audioCtx = null, oscs = [], gainNode = null;
    var currentId = null, timerId = null;
    var activeTab = 'solfeggio';
    var FADE = 0.8;
    var busGain = null, sinkDest = null, sinkEl = null, sinkActive = false;
    var IS_IOS = /iP(hone|ad|od)/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

    window.__renderFreq = function() { try { renderGrid(); } catch(e) {} };
    function renderGrid() {
      if (activeTab === 'dual') {
        var playingD = currentId === 'dual';
        grid.innerHTML = '<div class="dual-panel">' +
          '<p class="dual-desc">' + T('f.dualintro', '<strong style="color:#fff">Pulsos duales por oído (1–7 Hz).</strong> Cada lado late a su propio ritmo sobre un tono suave de 210 Hz — en el rango 1–7 Hz el oído percibe pulso, no tono. Úsalo con audífonos y volumen bajo. Se usa para relajación profunda o enfoque; la evidencia científica es limitada y la experiencia es personal.') + '</p>' +
          '<div class="dual-slider-row"><span>🎧 ' + T('f.left', 'Izquierdo') + '</span><input type="range" id="dual-l" min="1" max="7" step="0.5" value="' + dualL + '"><strong id="dual-l-val">' + dualL + ' Hz</strong></div>' +
          '<div class="dual-slider-row"><span>🎧 ' + T('f.right', 'Derecho') + '</span><input type="range" id="dual-r" min="1" max="7" step="0.5" value="' + dualR + '"><strong id="dual-r-val">' + dualR + ' Hz</strong></div>' +
          '<button class="btn ' + (playingD ? 'btn-pink' : 'btn-primary') + '" id="dual-toggle" style="justify-content:center">' + (playingD ? T('f.stop', '⏹ Detener') : T('f.playd', '▶ Reproducir dual')) + '</button>' +
        '</div>';
        wireDual();
        return;
      }
      var list = activeTab === 'solfeggio' ? SOLFEGGIO : BINAURAL;
      grid.innerHTML = list.map(function(f) {
        var big = activeTab === 'solfeggio' ? f.hz : f.beat;
        var unit = activeTab === 'solfeggio' ? TX('HZ · TONO PURO') : TX('HZ · BINAURAL 🎧');
        return '<div class="freq-card' + (currentId === f.id ? ' playing' : '') + '" data-id="' + f.id + '">' +
          '<div class="freq-ring"></div>' +
          '<div class="freq-hz">' + big + '</div>' +
          '<div class="freq-unit">' + unit + '</div>' +
          '<div class="freq-name">' + TX(f.name) + '</div>' +
          '<div class="freq-desc">' + TX(f.desc) + '</div>' +
          '<div class="freq-state">' + (currentId === f.id ? T('f.on', '⏸ Sonando') : T('f.play', '▶ Reproducir')) + '</div>' +
        '</div>';
      }).join('');
    }
    document.querySelectorAll('.freq-tab').forEach(function(t) {
      t.addEventListener('click', function() {
        document.querySelectorAll('.freq-tab').forEach(function(x) { x.classList.remove('active'); });
        this.classList.add('active');
        activeTab = this.dataset.tab;
        renderGrid();
      });
    });

    function getVolume() {
      return (document.getElementById('freq-volume').value / 100) * 0.25;
    }
    function ensureCtx() {
      if (!audioCtx) {
        var AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) { showToast(T('t.noaudio', 'Tu navegador no soporta audio generado')); return false; }
        audioCtx = new AC();
        audioCtx.onstatechange = function() {
          if (audioCtx && (audioCtx.state === 'suspended' || audioCtx.state === 'interrupted')) {
            try { audioCtx.resume(); } catch(e) {}
          }
        };
      }
      if (audioCtx.state !== 'running') { try { audioCtx.resume(); } catch(e) {} }
      if (!window.__villAudioUnlocked) {
        window.__villAudioUnlocked = true;
        try {
          var _b = audioCtx.createBuffer(1, 1, 22050);
          var _s = audioCtx.createBufferSource();
          _s.buffer = _b; _s.connect(audioCtx.destination); _s.start(0);
        } catch(e) {}
        /* El desbloqueo del contexto lo hace el buffer de arriba (mismo origen, sin URL).
           El audio audible viaja por audio-sink vía srcObject (MediaStream), inmune a
           esquemas data:/blob: que Safari o el WebView de Shopify rechazan. */
      }
      if (!busGain) {
        busGain = audioCtx.createGain();
        busGain.gain.value = 1;
        busGain.connect(audioCtx.destination);
        if (IS_IOS) {
          try {
            sinkDest = audioCtx.createMediaStreamDestination();
            sinkEl = document.getElementById('audio-sink');
            if (sinkEl && sinkDest) { sinkEl.srcObject = sinkDest.stream; sinkEl.volume = 1; }
          } catch(e) { sinkDest = null; }
        }
      }
      if (IS_IOS && sinkEl && sinkDest && sinkEl.paused) {
        var pp = sinkEl.play();
        if (pp && pp.then) {
          pp.then(function() {
            if (!sinkActive) {
              sinkActive = true;
              try { busGain.disconnect(); } catch(e) {}
              busGain.connect(sinkDest);
            }
          }).catch(function() {});
        }
      }
      clearTimeout(window.__villAudioCheck);
      window.__villAudioCheck = setTimeout(function() {
        if (audioCtx && audioCtx.state !== 'running') {
          try { audioCtx.resume(); } catch(e) {}
          showToast(T('t.ios', '🔇 iOS bloqueó el audio — toca “Reproducir” otra vez'));
        }
      }, 700);
      return true;
    }
    document.addEventListener('visibilitychange', function() {
      if (!document.hidden && audioCtx && audioCtx.state === 'suspended') { try { audioCtx.resume(); } catch(e) {} }
    });
    var dualL = 4, dualR = 6, lfoL = null, lfoR = null;
    function wireDual() {
      var sl = document.getElementById('dual-l');
      var sr = document.getElementById('dual-r');
      var tg = document.getElementById('dual-toggle');
      if (!sl || !sr || !tg) return;
      sl.addEventListener('input', function() {
        dualL = parseFloat(this.value);
        document.getElementById('dual-l-val').textContent = dualL + ' Hz';
        if (lfoL && audioCtx) lfoL.frequency.setValueAtTime(dualL, audioCtx.currentTime);
      });
      sr.addEventListener('input', function() {
        dualR = parseFloat(this.value);
        document.getElementById('dual-r-val').textContent = dualR + ' Hz';
        if (lfoR && audioCtx) lfoR.frequency.setValueAtTime(dualR, audioCtx.currentTime);
      });
      tg.addEventListener('click', function() {
        if (currentId === 'dual') { stopTone(); } else { playDual(dualL, dualR); }
      });
    }
    var freeBtn = document.getElementById('free-tone-btn');
    var freeInp = document.getElementById('free-hz');
    function updFreeBtn() {
      if (freeBtn) freeBtn.textContent = (currentId === 'free') ? T('f.stop', '⏹ Detener') : T('f.play', '▶ Reproducir');
    }
    window.__updFreeBtn = updFreeBtn;
    if (freeBtn) {
      freeBtn.addEventListener('click', function() {
        if (currentId === 'free') { stopTone(); updFreeBtn(); return; }
        var hz = parseFloat(freeInp && freeInp.value);
        if (!hz || hz < 20 || hz > 20000) { showToast(T('f.freerange', 'Elige entre 20 y 20 000 Hz')); return; }
        window.__freeTone = { id: 'free', hz: Math.round(hz * 100) / 100, name: 'Tono libre' };
        playById('free');
        updFreeBtn();
      });
      updFreeBtn();
    }

    var freeSl = document.getElementById('free-hz-slider');
    function hzToPos(hz) { return Math.round(1000 * Math.log(hz / 20) / Math.log(1000)); }
    function posToHz(p) { return Math.round(20 * Math.pow(1000, p / 1000)); }
    function retuneFree(hz) {
      if (currentId === 'free' && oscs[0]) {
        try {
          oscs[0].frequency.setValueAtTime(hz, audioCtx.currentTime);
          window.__freeTone = { id: 'free', hz: hz, name: 'Tono libre' };
          nowPlaying.textContent = '♪ ' + hz + ' Hz — ' + TX('Tono libre');
        } catch(e) {}
      }
    }
    if (freeSl && freeInp) {
      freeSl.value = hzToPos(parseFloat(freeInp.value) || 432);
      freeSl.addEventListener('input', function() {
        var hz = posToHz(parseInt(freeSl.value, 10));
        freeInp.value = hz;
        retuneFree(hz);
      });
      freeInp.addEventListener('input', function() {
        var hz = parseFloat(freeInp.value);
        if (hz >= 20 && hz <= 20000) { freeSl.value = hzToPos(hz); retuneFree(Math.round(hz)); }
      });
      freeInp.addEventListener('keydown', function(ev) { if (ev.key === 'Enter' && freeBtn) { ev.preventDefault(); freeBtn.click(); } });
    }

    function playDual(l, r) {
      if (!ensureCtx()) return;
      stopTone(true);
      gainNode = audioCtx.createGain();
      gainNode.gain.setValueAtTime(0.0001, audioCtx.currentTime);
      gainNode.gain.linearRampToValueAtTime(getVolume(), audioCtx.currentTime + FADE);
      gainNode.connect(busGain);
      function side(pan, f) {
        var carrier = audioCtx.createOscillator();
        carrier.type = 'sine';
        carrier.frequency.setValueAtTime(210, audioCtx.currentTime);
        var amp = audioCtx.createGain();
        amp.gain.setValueAtTime(0.5, audioCtx.currentTime);
        var lfo = audioCtx.createOscillator();
        lfo.type = 'sine';
        lfo.frequency.setValueAtTime(f, audioCtx.currentTime);
        var depth = audioCtx.createGain();
        depth.gain.setValueAtTime(0.5, audioCtx.currentTime);
        lfo.connect(depth);
        depth.connect(amp.gain);
        carrier.connect(amp);
        var pn = null;
        try { pn = audioCtx.createStereoPanner(); pn.pan.value = pan; } catch(e) { pn = null; }
        if (pn) { amp.connect(pn); pn.connect(gainNode); } else { amp.connect(gainNode); }
        carrier.start(); lfo.start();
        oscs.push(carrier, lfo);
        return lfo;
      }
      lfoL = side(-1, l);
      lfoR = side(1, r);
      currentId = 'dual';
      if (window.__updFreeBtn) setTimeout(window.__updFreeBtn, 0);
      nowPlaying.textContent = '♪ Dual: ' + l + ' Hz (izq) · ' + r + ' Hz (der) — usa audífonos';
      renderGrid();
      var mins = parseInt(document.getElementById('freq-timer-select').value, 10);
      if (mins > 0) {
        timerId = setTimeout(function() { stopTone(true); showToast(T('t.sess', '⏱ Sesión completada')); }, mins * 60000);
      }
    }
    function stopTone(silent) {
      clearTimeout(timerId); timerId = null;
      if (oscs.length && gainNode && audioCtx) {
        var t = audioCtx.currentTime;
        gainNode.gain.cancelScheduledValues(t);
        gainNode.gain.setValueAtTime(gainNode.gain.value, t);
        gainNode.gain.linearRampToValueAtTime(0.0001, t + FADE);
        var old = oscs.slice();
        setTimeout(function() {
          old.forEach(function(o) { try { o.stop(); o.disconnect(); } catch(e) {} });
        }, FADE * 1000 + 60);
      }
      oscs = []; gainNode = null; currentId = null; lfoL = null; lfoR = null;
      nowPlaying.textContent = '';
      renderGrid();
      if (window.__updFreeBtn) window.__updFreeBtn();
      if (!silent) showToast(T('t.stopf', 'Frecuencia detenida'));
    }
    function playById(id) {
      if (!ensureCtx()) return;
      stopTone(true);
      gainNode = audioCtx.createGain();
      gainNode.gain.setValueAtTime(0.0001, audioCtx.currentTime);
      gainNode.gain.linearRampToValueAtTime(getVolume(), audioCtx.currentTime + FADE);
      gainNode.connect(busGain);

      var solf = (id === 'free' && window.__freeTone) ? window.__freeTone : SOLFEGGIO.find(function(x) { return x.id === id; });
      var bin = BINAURAL.find(function(x) { return x.id === id; });
      if (solf) {
        var o = audioCtx.createOscillator();
        o.type = 'sine';
        o.frequency.setValueAtTime(solf.hz, audioCtx.currentTime);
        o.connect(gainNode);
        o.start();
        oscs = [o];
        nowPlaying.textContent = '♪ ' + solf.hz + ' Hz — ' + TX(solf.name);
      } else if (bin) {
        var oL = audioCtx.createOscillator();
        var oR = audioCtx.createOscillator();
        oL.type = 'sine'; oR.type = 'sine';
        oL.frequency.setValueAtTime(CARRIER, audioCtx.currentTime);
        oR.frequency.setValueAtTime(CARRIER + bin.beat, audioCtx.currentTime);
        var okPan = false;
        try {
          var pL = audioCtx.createStereoPanner();
          var pR = audioCtx.createStereoPanner();
          pL.pan.value = -1; pR.pan.value = 1;
          oL.connect(pL).connect(gainNode);
          oR.connect(pR).connect(gainNode);
          okPan = true;
        } catch(e) {}
        if (!okPan) { oL.connect(gainNode); oR.connect(gainNode); }
        oL.start(); oR.start();
        oscs = [oL, oR];
        nowPlaying.textContent = '♪ ' + bin.beat + ' Hz binaural — ' + TX(bin.name) + ' (' + T('dyn.phones', 'usa audífonos') + ')';
      } else { return; }

      currentId = id;
      renderGrid();
      if (window.__updFreeBtn) window.__updFreeBtn();
      var mins = parseInt(document.getElementById('freq-timer-select').value, 10);
      if (mins > 0) {
        timerId = setTimeout(function() {
          stopTone(true);
          showToast('⏱ ' + T('t.sess2', 'Sesión de') + ' ' + mins + ' min ' + T('t.done2', 'completada'));
        }, mins * 60000);
      }
    }

    grid.addEventListener('click', function(e) {
      var card = e.target.closest('.freq-card');
      if (!card) return;
      var id = card.dataset.id;
      if (currentId === id) stopTone();
      else playById(id);
    });
    document.getElementById('freq-volume').addEventListener('input', function() {
      if (gainNode && audioCtx) {
        gainNode.gain.cancelScheduledValues(audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(getVolume(), audioCtx.currentTime + 0.1);
      }
    });
    document.getElementById('freq-stop-btn').addEventListener('click', function() { stopTone(); });
    renderGrid();
  })();

  /* =====================================================================
     NUTRICIÓN — macros + ESCÁNER POR ANÁLISIS DE COLOR
     La foto se analiza localmente (histograma de tonos); el sistema
     sugiere alimentos compatibles y TÚ confirmas cuál es y la porción.
     ===================================================================== */
  (function initNutrition() {
    try {
      var FOODS = [
        { name: 'Pollo a la plancha',    kcal: 165, protein: 31,  carbs: 0,   fat: 3.6,  colors: ['white', 'brown'] },
        { name: 'Pechuga de pavo',       kcal: 135, protein: 30,  carbs: 0,   fat: 1,    colors: ['white'] },
        { name: 'Carne de res magra',    kcal: 250, protein: 26,  carbs: 0,   fat: 15,   colors: ['brown', 'red'] },
        { name: 'Salmón 150g',           kcal: 234, protein: 33,  carbs: 0,   fat: 10.5, colors: ['orange', 'red'] },
        { name: 'Atún en lata',          kcal: 132, protein: 29,  carbs: 0,   fat: 1,    colors: ['red', 'brown'] },
        { name: 'Huevo entero',          kcal: 78,  protein: 6,   carbs: 0.6, fat: 5,    colors: ['white', 'yellow'] },
        { name: 'Tortilla de huevo',     kcal: 154, protein: 11,  carbs: 1,   fat: 12,   colors: ['yellow'] },
        { name: 'Arroz blanco 150g',     kcal: 195, protein: 4,   carbs: 42,  fat: 0.4,  colors: ['white'] },
        { name: 'Arroz integral 100g',   kcal: 111, protein: 2.6, carbs: 23,  fat: 0.9,  colors: ['brown'] },
        { name: 'Pasta cocida 150g',     kcal: 220, protein: 8,   carbs: 43,  fat: 1.3,  colors: ['yellow', 'white'] },
        { name: 'Avena 50g',             kcal: 190, protein: 6.5, carbs: 34,  fat: 3.3,  colors: ['brown', 'white'] },
        { name: 'Pan integral 2 reb.',   kcal: 160, protein: 8,   carbs: 28,  fat: 2,    colors: ['brown'] },
        { name: 'Batata 150g',           kcal: 130, protein: 2,   carbs: 30,  fat: 0.1,  colors: ['orange'] },
        { name: 'Ensalada verde',        kcal: 35,  protein: 2,   carbs: 6,   fat: 0.4,  colors: ['green'] },
        { name: 'Brócoli 100g',          kcal: 34,  protein: 2.8, carbs: 7,   fat: 0.4,  colors: ['green'] },
        { name: 'Espinacas salteadas',   kcal: 41,  protein: 3,   carbs: 4,   fat: 2,    colors: ['green'] },
        { name: 'Aguacate medio',        kcal: 160, protein: 2,   carbs: 9,   fat: 15,   colors: ['green'] },
        { name: 'Plátano',               kcal: 105, protein: 1.3, carbs: 27,  fat: 0.4,  colors: ['yellow'] },
        { name: 'Manzana',               kcal: 95,  protein: 0.5, carbs: 25,  fat: 0.3,  colors: ['red', 'green'] },
        { name: 'Fresas 150g',           kcal: 48,  protein: 1,   carbs: 12,  fat: 0.5,  colors: ['red'] },
        { name: 'Tomate en ensalada',    kcal: 22,  protein: 1,   carbs: 5,   fat: 0.2,  colors: ['red'] },
        { name: 'Yogur griego 150g',     kcal: 100, protein: 17,  carbs: 6,   fat: 0.7,  colors: ['white'] },
        { name: 'Requesón 150g',         kcal: 120, protein: 18,  carbs: 5,   fat: 3,    colors: ['white'] },
        { name: 'Almendras 30g',         kcal: 174, protein: 6,   carbs: 6,   fat: 15,   colors: ['brown'] },
        { name: 'Chocolate negro 20g',   kcal: 110, protein: 1.5, carbs: 9,   fat: 8,    colors: ['dark', 'brown'] }
      ];
      var COLOR_LABELS = { red: '🔴 rojo', orange: '🟠 naranja', yellow: '🟡 amarillo', green: '🟢 verde', brown: '🟤 marrón', white: '⚪ claro', dark: '⚫ oscuro' };

      var foodLog = [];
      var macros = { protein: 145, carbs: 220, fat: 62, kcal: 1840 };
      var macroChart = null;

      if (typeof Chart !== 'undefined') {
        var ctx = document.getElementById('macro-chart').getContext('2d');
        if (typeof Chart === 'undefined') { console.warn('Chart.js no cargó (CDN)'); return; }
        macroChart = new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: [TX('Proteína'), TX('Carbohidratos'), TX('Grasas')],
            datasets: [{ data: [macros.protein * 4, macros.carbs * 4, macros.fat * 9], backgroundColor: ['#FF2A6D', '#05D9E8', '#FFD700'], borderWidth: 0, hoverOffset: 8 }]
          },
          options: { responsive: true, cutout: '70%', plugins: { legend: { display: false }, tooltip: { callbacks: { label: function(c) { return c.label + ': ' + (c.raw / 4).toFixed(0) + 'g'; } } } } }
        });
      }
      function updateMacroUI() {
        if (macroChart) {
          macroChart.data.datasets[0].data = [macros.protein * 4, macros.carbs * 4, macros.fat * 9];
          macroChart.data.labels = [TX('Proteína'), TX('Carbohidratos'), TX('Grasas')];
          macroChart.update();
        }
        document.getElementById('cal-count').textContent = Math.round(macros.kcal) + ' kcal';
        var goal = window.getCalGoal ? window.getCalGoal() : 2200;
        var pct = Math.min(macros.kcal / goal * 100, 100);
        var goalEl = document.getElementById('cal-goal');
        if (goalEl) goalEl.textContent = goal + ' kcal';
        document.getElementById('cal-bar').style.width = pct + '%';
        var legend = document.getElementById('macro-legend');
        var colors = ['#FF2A6D', '#05D9E8', '#FFD700'];
        var labels = [[TX('Proteína'), macros.protein.toFixed(0) + 'g'], [TX('Carbos'), macros.carbs.toFixed(0) + 'g'], [TX('Grasas'), macros.fat.toFixed(0) + 'g']];
        legend.innerHTML = labels.map(function(l, i) {
          return '<div class="macro-row"><span><span class="macro-dot" style="background:' + colors[i] + '"></span>' + l[0] + '</span><strong>' + l[1] + '</strong></div>';
        }).join('');
      }
      window.__renderMacros = updateMacroUI;
      function renderFoodLog() {
        var log = document.getElementById('food-log');
        log.innerHTML = foodLog.length === 0 ? '' : '<div style="font-size:0.78rem;color:#888899;margin-bottom:6px">Registro de hoy</div>' + foodLog.map(function(f) {
          return '<div class="food-log-item"><span>' + f.name + '</span><span style="color:#05D9E8">' + Math.round(f.kcal) + ' kcal</span></div>';
        }).join('');
      }
      window.refreshCalGoalUI = updateMacroUI;
      window.addFoodPortion = function(index, mult, portionLabel) {
        var f = FOODS[index];
        if (!f) return;
        var entry = {
          name: f.name + (portionLabel ? ' (' + portionLabel + ')' : ''),
          kcal: f.kcal * mult, protein: f.protein * mult, carbs: f.carbs * mult, fat: f.fat * mult
        };
        foodLog.push(entry);
        macros.protein += entry.protein;
        macros.carbs += entry.carbs;
        macros.fat += entry.fat;
        macros.kcal += entry.kcal;
        if (window.recordIntake) window.recordIntake(entry.kcal);
        renderFoodLog(); updateMacroUI();
        document.getElementById('scan-result').style.display = 'none';
        document.getElementById('food-suggestions').style.display = 'none';
        document.getElementById('food-input').value = '';
        showToast('✓ ' + entry.name + ' ' + T('t.logged', 'registrado') + ' (' + Math.round(entry.kcal) + ' kcal)');
      };

      /* ---- BÚSQUEDA MANUAL ---- */
      var input = document.getElementById('food-input');
      var sugg = document.getElementById('food-suggestions');
      input.addEventListener('input', function() {
        var q = this.value.toLowerCase().trim();
        if (!q) { sugg.style.display = 'none'; return; }
        var results = [];
        FOODS.forEach(function(f, i) { if (f.name.toLowerCase().indexOf(q) !== -1) results.push(i); });
        if (results.length) {
          sugg.style.display = 'block';
          sugg.innerHTML = results.map(function(i) {
            var f = FOODS[i];
            return '<div onclick="addFoodPortion(' + i + ',1,\'\')">' + f.name + ' <span style="color:#888899;font-size:0.75rem">' + f.kcal + ' kcal</span></div>';
          }).join('');
        } else { sugg.style.display = 'none'; }
      });
      document.getElementById('food-search-btn').addEventListener('click', function() {
        input.dispatchEvent(new Event('input'));
      });
      document.addEventListener('click', function(e) {
        if (!sugg.contains(e.target) && e.target !== input) sugg.style.display = 'none';
      });

      /* ---- ANÁLISIS DE COLOR DE LA IMAGEN ---- */
      function rgbToHsv(r, g, b) {
        r /= 255; g /= 255; b /= 255;
        var max = Math.max(r, g, b), min = Math.min(r, g, b);
        var h = 0, s = max === 0 ? 0 : (max - min) / max, v = max;
        var d = max - min;
        if (d !== 0) {
          if (max === r) h = ((g - b) / d) % 6;
          else if (max === g) h = (b - r) / d + 2;
          else h = (r - g) / d + 4;
          h *= 60;
          if (h < 0) h += 360;
        }
        return [h, s, v];
      }
      function bucketOf(h, s, v) {
        if (v < 0.18) return 'dark';
        if (s < 0.16) return v > 0.6 ? 'white' : 'dark';
        if (h < 18 || h >= 340) return 'red';
        if (h < 42) return (v < 0.55 || s < 0.55) ? 'brown' : 'orange';
        if (h < 70) return 'yellow';
        if (h < 165) return 'green';
        if (h < 260) return 'white';  // azules → probable plato/fondo, lo tratamos como neutro
        return 'red';
      }
      function analyzeCanvas(cnv) {
        var c = cnv.getContext('2d');
        var w = cnv.width, h = cnv.height;
        var data = c.getImageData(0, 0, w, h).data;
        var counts = { red: 0, orange: 0, yellow: 0, green: 0, brown: 0, white: 0, dark: 0 };
        var total = 0;
        // muestreo del centro (donde suele estar la comida), saltando píxeles
        var x0 = Math.floor(w * 0.15), x1 = Math.floor(w * 0.85);
        var y0 = Math.floor(h * 0.15), y1 = Math.floor(h * 0.85);
        for (var y = y0; y < y1; y += 4) {
          for (var x = x0; x < x1; x += 4) {
            var idx = (y * w + x) * 4;
            var hsv = rgbToHsv(data[idx], data[idx + 1], data[idx + 2]);
            counts[bucketOf(hsv[0], hsv[1], hsv[2])]++;
            total++;
          }
        }
        var sorted = Object.keys(counts).sort(function(a, b) { return counts[b] - counts[a]; });
        var top = sorted.filter(function(k) { return counts[k] / total > 0.08; }).slice(0, 4);
        // "dark" dominante suele ser fondo/sombra; "white" muy dominante suele ser el PLATO
        if (top.length > 1 && top[0] === 'dark') top.shift();
        if (top.length > 1 && top[0] === 'white' && counts.white / total > 0.45) top.shift();
        return top.slice(0, 3);
      }
      function scoreFoods(topColors) {
        return FOODS.map(function(f, i) {
          var score = 0;
          f.colors.forEach(function(c) {
            var pos = topColors.indexOf(c);
            if (pos === 0) score += 3;
            else if (pos === 1) score += 2;
            else if (pos === 2) score += 1;
          });
          return { i: i, score: score };
        }).filter(function(x) { return x.score > 0; })
          .sort(function(a, b) { return b.score - a.score; })
          .slice(0, 6);
      }

      /* ===== DETECCIÓN CON IA (MobileNet, carga perezosa) ===== */
      var AI_MAP = [
        ['banana', 'plátano'], ['orange', 'naranja'], ['lemon', 'limón'], ['pineapple', 'piña'],
        ['strawberr', 'fresa'], ['granny smith', 'manzana'], ['fig', 'manzana'], ['custard apple', 'manzana'],
        ['pomegranate', 'manzana'], ['broccoli', 'brócoli'], ['cauliflower', 'brócoli'], ['cucumber', 'pepino'],
        ['zucchini', 'calabac'], ['bell pepper', 'pimiento'], ['mushroom', 'champiñ'], ['corn', 'maíz'],
        ['cabbage', 'ensalada'], ['artichoke', 'ensalada'], ['guacamole', 'aguacate'], ['mashed potato', 'papa'],
        ['potato', 'papa'], ['french loaf', 'pan'], ['bagel', 'pan'], ['pretzel', 'pan'], ['dough', 'pan'],
        ['pizza', 'pizza'], ['cheeseburger', 'hamburgues'], ['hotdog', 'hot dog'], ['hot dog', 'hot dog'],
        ['burrito', 'burrito'], ['carbonara', 'pasta'], ['spaghetti', 'pasta'], ['meat loaf', 'carne'],
        ['ice cream', 'helado'], ['trifle', 'yogur'], ['chocolate', 'chocolate'], ['espresso', 'café'],
        ['eggnog', 'batido'], ['acorn squash', 'batata'], ['butternut', 'batata'], ['rotisserie', 'pollo'],
        ['drumstick', 'pollo'], ['crab', 'pescado'], ['lobster', 'pescado'], ['salmon', 'salmón'],
        ['omelet', 'tortilla'], ['egg', 'huevo'], ['rice', 'arroz'], ['soup', 'sopa'], ['consomme', 'sopa'], ['soup bowl', 'sopa'], ['mixing bowl', 'ensalada']
      ];
      var __mnet = null, __mnetLoading = null;
      function loadScriptOnce(u) {
        return new Promise(function(res, rej) {
          var s = document.createElement('script');
          s.src = u; s.crossOrigin = 'anonymous';
          /* Sin referente: jsdelivr no necesita saber en que pagina de la
             tienda esta el visitante para servir un archivo. */
          s.referrerPolicy = 'no-referrer';
          s.onload = res; s.onerror = rej;
          document.head.appendChild(s);
        });
      }
      /* El reconocedor de alimentos por camara. Son unos 4 MB de TensorFlow y
         MobileNet, asi que se bajan SOLO cuando alguien pulsa la camara, y de
         un CDN: meterlos en el tema seria multiplicar por siete su tamano para
         una funcion que la mayoria no usa.

         Si no se puede bajar -- red de empresa, filtro de pais, un corte -- no
         pasa nada visible: quien llama a esto cae al analisis por color, que
         va entero dentro del hub y no necesita internet.

         El detalle que se arreglo: __mnetLoading guardaba la promesa para no
         bajar el modelo dos veces, pero si la descarga FALLABA se quedaba
         guardada una promesa rechazada, y a partir de ahi cada intento moria
         al instante contra el fallo viejo. Un corte de dos segundos dejaba la
         IA apagada el resto de la visita. Ahora el fallo se limpia y el
         siguiente intento vuelve a probar de verdad. */
      function loadMobileNet() {
        if (__mnet) return Promise.resolve(__mnet);
        if (__mnetLoading) return __mnetLoading;
        __mnetLoading = (window.tf ? Promise.resolve() : loadScriptOnce('https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.17.0/dist/tf.min.js'))
          .then(function() { return window.mobilenet ? null : loadScriptOnce('https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@2.1.1/dist/mobilenet.min.js'); })
          .then(function() { return window.mobilenet.load({ version: 2, alpha: 0.5 }); })
          .then(function(m) { __mnet = m; return m; })
          .catch(function(e) { __mnetLoading = null; throw e; });
        return __mnetLoading;
      }
      function findFoodIdx(term) {
        term = term.toLowerCase();
        for (var i = 0; i < FOODS.length; i++) {
          if (FOODS[i].name.toLowerCase().indexOf(term) !== -1) return i;
        }
        return -1;
      }
      function centerCrop(cnv) {
        var c = document.createElement('canvas');
        var w = Math.round(cnv.width * 0.7), h = Math.round(cnv.height * 0.7);
        c.width = w; c.height = h;
        c.getContext('2d').drawImage(cnv, (cnv.width - w) / 2, (cnv.height - h) / 2, w, h, 0, 0, w, h);
        return c;
      }
      function classifyAI(cnv) {
        return loadMobileNet().then(function(m) {
          return Promise.all([m.classify(cnv, 5), m.classify(centerCrop(cnv), 5)]);
        }).then(function(both) {
          var preds = (both[0] || []).concat(both[1] || []);
          var byIdx = {};
          (preds || []).forEach(function(p) {
            if (p.probability < 0.10) return;
            var lbl = p.className.toLowerCase();
            AI_MAP.forEach(function(pair) {
              if (lbl.indexOf(pair[0]) !== -1) {
                var idx = findFoodIdx(pair[1]);
                if (idx !== -1 && (!(idx in byIdx) || byIdx[idx] < p.probability)) byIdx[idx] = p.probability;
              }
            });
          });
          return Object.keys(byIdx).map(function(k) { return { i: parseInt(k, 10), p: byIdx[k] }; })
            .sort(function(a, b) { return b.p - a.p; }).slice(0, 4);
        });
      }
      function renderAICandidates(cands) {
        var box = document.getElementById('scan-result');
        box.style.display = 'block';
        var chips = cands.map(function(c) {
          var f = FOODS[c.i];
          return '<div class="scan-cand"><div style="font-weight:700">' + f.name + ' <span style="color:#05D9E8;font-size:0.72rem">' + Math.round(c.p * 100) + '%</span></div>' +
            '<div style="color:#889;font-size:0.75rem;margin:2px 0 6px">' + f.kcal + ' kcal · ' + f.protein + 'g prot</div>' +
            '<div>' +
              '<button class="portion-btn" onclick="addFoodPortion(' + c.i + ',0.75,\'pequeña\')">Pequeña ×0.75</button>' +
              '<button class="portion-btn" onclick="addFoodPortion(' + c.i + ',1,\'normal\')">Normal ×1</button>' +
              '<button class="portion-btn" onclick="addFoodPortion(' + c.i + ',1.5,\'grande\')">Grande ×1.5</button>' +
            '</div></div>';
        }).join('');
        box.innerHTML = '<strong style="color:#05D9E8">🤖 Detección con IA</strong> — confirma el alimento y la porción:' +
          '<div class="scan-candidates">' + chips + '</div>' +
          '<button class="portion-btn" style="margin-top:8px" onclick="if(window.__scanHeur)__scanHeur()">¿No es esto? Ver análisis por colores</button>' +
          '<button class="portion-btn" style="margin-top:8px" type="button" onclick="document.getElementById(\'scan-btn\').click()">' + T('t.newcap', '🔁 Nueva captura') + '</button>';
      }
      function showScanResult(cnv) {
        var box = document.getElementById('scan-result');
        box.style.display = 'block';
        window.__scanHeur = function() { showScanHeuristic(cnv); };
        box.innerHTML = '<span style="color:#05D9E8">🤖 ' + T('t.scan1', 'Analizando con IA local…') + '</span> <span style="color:#667;font-size:0.75rem">' + T('t.scan2', "La primera vez descarga el modelo (~4 MB); funciona en tu dispositivo, nada se sube.") + '</span>';
        classifyAI(cnv).then(function(cands) {
          if (cands && cands.length) renderAICandidates(cands);
          else showScanHeuristic(cnv);
        }).catch(function() { showScanHeuristic(cnv); });
      }
      function showScanHeuristic(cnv) {
        var topColors = analyzeCanvas(cnv);
        var candidates = scoreFoods(topColors);
        var box = document.getElementById('scan-result');
        box.style.display = 'block';
        var colorTxt = topColors.map(function(c) { return COLOR_LABELS[c]; }).join(' · ');
        if (!candidates.length) {
          box.innerHTML = '<strong style="color:#05D9E8">Colores detectados:</strong> ' + colorTxt +
            '<br><span style="color:#888899;font-size:0.8rem">No encontré coincidencias claras. Usa el buscador de arriba para registrarlo manualmente.</span>';
          return;
        }
        var chips = candidates.map(function(c) {
          var f = FOODS[c.i];
          return '<button class="scan-cand" onclick="pickScanCandidate(' + c.i + ')">' + f.name + ' · ' + f.kcal + ' kcal</button>';
        }).join('');
        box.innerHTML = '<strong style="color:#05D9E8">Colores detectados:</strong> ' + colorTxt +
          '<div style="margin-top:8px;font-weight:600">¿Cuál de estos alimentos es?</div>' +
          '<div class="scan-candidates">' + chips + '</div>' +
          '<div class="scan-note">🔬 Análisis local por color (aproximado). Tú confirmas el alimento y la porción — así el registro siempre es correcto.</div>';
      }
      window.pickScanCandidate = function(i) {
        var f = FOODS[i];
        var box = document.getElementById('scan-result');
        box.innerHTML = '<strong style="color:#05D9E8">' + f.name + '</strong> · base ' + f.kcal + ' kcal' +
          '<div class="portion-row"><span style="font-size:0.78rem;color:#888899">Porción:</span>' +
          '<button class="portion-btn" onclick="addFoodPortion(' + i + ',0.75,\'pequeña\')">Pequeña ×0.75</button>' +
          '<button class="portion-btn" onclick="addFoodPortion(' + i + ',1,\'normal\')">Normal ×1</button>' +
          '<button class="portion-btn" onclick="addFoodPortion(' + i + ',1.5,\'grande\')">Grande ×1.5</button>' +
          '</div>';
      };

      /* ---- CÁMARA / FOTO ---- */
      var video = document.getElementById('cam-video');
      var scanCanvas = document.getElementById('scan-canvas');
      var scanBtn = document.getElementById('scan-btn');
      var captureBtn = document.getElementById('capture-btn');
      var stopCamBtn = document.getElementById('stop-cam-btn');
      var uploadBtn = document.getElementById('upload-btn');
      var photoInput = document.getElementById('photo-input');
      var camInput = document.getElementById('cam-input');

      function stopCamera() {
        if (window.camStream) {
          window.camStream.getTracks().forEach(function(t) { t.stop(); });
          window.camStream = null;
        }
        video.style.display = 'none';
        video.srcObject = null;
        captureBtn.style.display = 'none';
        stopCamBtn.style.display = 'none';
        scanBtn.style.display = 'inline-flex';
      }
      function scanFeedback(html) {
        var box = document.getElementById('scan-result');
        box.style.display = 'block';
        box.innerHTML = html;
      }
      var NATIVE_BTN = '<button class="portion-btn" type="button" onclick="document.getElementById(\'cam-input\').click()">📸 Usar cámara nativa</button>';
      scanBtn.addEventListener('click', function() {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
          scanFeedback('<span style="color:#FF9F43">Este navegador no permite cámara en vivo</span> — abriendo la cámara nativa…');
          camInput.click();
          return;
        }
        scanFeedback('<span style="color:#05D9E8">📷 Abriendo cámara…</span> acepta el permiso si aparece.');
        var timedOut = false;
        var guard = setTimeout(function() {
          timedOut = true;
          scanFeedback('La cámara en vivo no respondió (típico del navegador dentro de una app). ' + NATIVE_BTN +
            ' <span style="color:#667;font-size:0.75rem">La cámara nativa y “Subir foto” funcionan en cualquier navegador.</span>');
        }, 4000);
        navigator.mediaDevices.getUserMedia({ video: { facingMode: { ideal: 'environment' } }, audio: false })
          .catch(function() { return navigator.mediaDevices.getUserMedia({ video: true, audio: false }); })
          .then(function(stream) {
            clearTimeout(guard);
            if (timedOut) { stream.getTracks().forEach(function(t) { t.stop(); }); return; }
            window.camStream = stream;
            video.srcObject = stream;
            video.style.display = 'block';
            var p = video.play();
            if (p && p.catch) p.catch(function() {});
            captureBtn.style.display = 'inline-flex';
            stopCamBtn.style.display = 'inline-flex';
            scanBtn.style.display = 'none';
            scanFeedback('Apunta al plato con buena luz y pulsa <strong style="color:#05D9E8">📸 Capturar</strong>.');
          })
          .catch(function(err) {
            clearTimeout(guard);
            if (timedOut) return;
            var msg = (err && err.name === 'NotAllowedError')
              ? 'Permiso de cámara denegado (Ajustes → Safari → Cámara).'
              : 'No se pudo abrir la cámara en vivo.';
            scanFeedback('<span style="color:#FF9F43">' + msg + '</span> ' + NATIVE_BTN +
              ' <span style="color:#667;font-size:0.75rem">La cámara nativa y “Subir foto” funcionan en cualquier navegador.</span>');
          });
      });
      captureBtn.addEventListener('click', function() {
        if (!video.videoWidth) { showToast(T('t.cam', 'La cámara aún no está lista')); return; }
        scanCanvas.width = 320;
        scanCanvas.height = Math.round(320 * video.videoHeight / video.videoWidth);
        scanCanvas.getContext('2d').drawImage(video, 0, 0, scanCanvas.width, scanCanvas.height);
        showScanResult(scanCanvas);
        stopCamera();
      });
      stopCamBtn.addEventListener('click', stopCamera);
      uploadBtn.addEventListener('click', function() { photoInput.click(); });
      var handleScanFile = function() {
        var file = this.files && this.files[0];
        if (!file) return;
        var img = new Image();
        img.onload = function() {
          scanCanvas.width = 320;
          scanCanvas.height = Math.round(320 * img.height / img.width);
          scanCanvas.getContext('2d').drawImage(img, 0, 0, scanCanvas.width, scanCanvas.height);
          showScanResult(scanCanvas);
          URL.revokeObjectURL(img.src);
        };
        img.src = URL.createObjectURL(file);
        this.value = '';
      };
      photoInput.addEventListener('change', handleScanFile);
      camInput.addEventListener('change', handleScanFile);

      updateMacroUI();
    } catch(err) {
      console.warn('Nutrition error:', err.message);
    }
  })();

  /* ===== DIET TABS ===== */
  (function initDietTabs() {
    var tabs = document.querySelectorAll('.diet-tab');
    var contents = document.querySelectorAll('.diet-content');
    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
        tabs.forEach(function(t) { t.classList.remove('active'); });
        this.classList.add('active');
        var plan = this.dataset.plan;
        contents.forEach(function(c) { c.classList.remove('active'); });
        document.getElementById('plan-' + plan).classList.add('active');
      });
    });
  })();

  /* ===== PROGRESS CHART ===== */
  (function initProgress() {
    try {
      var weekData = { labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'], data: [2800, 3100, 2400, 3500, 3200, 4100, 2200] };
      var monthData = { labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7', 'Sem 8'], data: [18500, 21000, 19800, 24000, 22500, 26000, 23800, 28500] };
      if (typeof Chart === 'undefined') throw new Error('Chart.js no cargado');
      var ctx = document.getElementById('progress-chart').getContext('2d');
      var progressChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: weekData.labels,
          datasets: [{ label: 'Volumen (kg)', data: weekData.data, backgroundColor: 'rgba(5,217,232,0.25)', borderColor: '#05D9E8', borderWidth: 2, borderRadius: 8, borderSkipped: false }]
        },
        options: {
          responsive: true,
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: function(c) { return c.formattedValue + ' kg'; } } } },
          scales: { x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#888899' } }, y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#888899' } } }
        }
      });
      document.querySelectorAll('.period-tab').forEach(function(tab) {
        tab.addEventListener('click', function() {
          document.querySelectorAll('.period-tab').forEach(function(t) { t.classList.remove('active'); });
          this.classList.add('active');
          var d = this.dataset.period === 'month' ? monthData : weekData;
          progressChart.data.labels = d.labels;
          progressChart.data.datasets[0].data = d.data;
          progressChart.update();
        });
      });
    } catch(err) {
      console.warn('Progress error:', err.message);
      var pc = document.getElementById('progress-chart');
      if (pc && pc.parentElement) pc.parentElement.innerHTML = '<div class="module-error">📊 ' + T('err.chart', 'Gráfica no disponible.') + '</div>';
    }
  })();

  /* ===== CHALLENGES ===== */
  (function initChallenges() {
    /* leaderboard lo construye renderLeaderboard() con datos reales de volumen */
    var badges = ['🏆', '🔥', '💪', '🧘', '🥗'];
    var badgeLabels = ['Campeón', 'Racha 7d', 'Fuerza', 'Zen', 'Nutrición'];
    var row = document.getElementById('badges-row');
    row.innerHTML = badges.map(function(b, i) {
      return '<div class="badge-item"><span class="badge-icon">' + b + '</span><span class="badge-label">' + TX(badgeLabels[i]) + '</span></div>';
    }).join('');

    document.getElementById('join-btn').addEventListener('click', function() {
      showToast(T('chal.join', '¡Te has unido al reto de 30 días de plancha!'));
    });
  })();

})();
