/* VILLUMINATION 3D — core store interactions (vanilla JS, no dependencies) */
(function () {
  'use strict';
  var T = window.theme || {};
  var routes = T.routes || {};
  var settings = T.settings || {};
  var strings = T.strings || {};

  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  /* Editor de Shopify: al editar una sección, Shopify sustituye su HTML y el JS ligado a
     esos elementos deja de existir. Se registran los módulos y se vuelven a ejecutar en
     shopify:section:load. once() garantiza que un elemento ya inicializado no se vuelva a
     enganchar, así no se duplican manejadores en las secciones que no cambiaron. */
  var MODS = [];
  function mod(fn) { MODS.push(fn); try { fn(); } catch (e) {} }
  function once(el, key) {
    if (!el) return false;
    var k = 'vinit' + key;
    if (el.getAttribute('data-' + k)) return false;
    el.setAttribute('data-' + k, '1');
    return true;
  }
  document.addEventListener('shopify:section:load', function () {
    MODS.forEach(function (f) { try { f(); } catch (e) {} });
  });


  var currencyCode = ((settings.moneyFormat || '').match(/[A-Z]{3}/) || ['USD'])[0];
  function money(cents) {
    try { return (cents / 100).toLocaleString(undefined, { style: 'currency', currency: currencyCode }); }
    catch (e) { return '$' + (cents / 100).toFixed(2); }
  }

  /* Almacenamiento seguro. En Safari privado, con "bloquear todas las cookies"
     o dentro de algunos navegadores integrados, el simple hecho de leer
     sessionStorage lanza SecurityError; sin esta envoltura ese error tumbaba
     todo el script (menú, carrito, buscador…) en esos dispositivos. */
  var store = {
    get: function (k, session) {
      try { return (session ? sessionStorage : localStorage).getItem(k); } catch (e) { return null; }
    },
    set: function (k, v, session) {
      try { (session ? sessionStorage : localStorage).setItem(k, v); } catch (e) {}
    }
  };

  /* ---------- Splash intro ---------- */
  (function () {
    var splash = $('[data-splash]');
    if (!splash) return;
    var enter = $('#splash-enter');
    var once = settings.splashOnce;
    if (once && store.get('v99_intro_seen', true)) { splash.style.display = 'none'; return; }
    document.body.style.overflow = 'hidden';
    var done = false;
    function dismiss() {
      if (done) return; done = true;
      splash.classList.add('dismissed');
      document.body.style.overflow = '';
      if (once) store.set('v99_intro_seen', '1', true);
      // intro.js escucha esto para parar su bucle y soltar el lienzo. Sin el
      // aviso, la secuencia seguiria pintando detras de la tienda: bateria
      // gastada en algo que ya nadie ve.
      try { splash.dispatchEvent(new CustomEvent('villu:intro-cerrada')); } catch (e) {}
      setTimeout(function () { splash.style.display = 'none'; }, 900);
    }
    if (enter) enter.addEventListener('click', dismiss);

    // Saltar, disponible desde el primer fotograma. El boton grande de entrar
    // solo aparece al terminar la secuencia; quien ya conoce la tienda no
    // tiene por que esperar a nada para pasar.
    var saltar = $('[data-splash-skip]', splash);
    if (saltar) saltar.addEventListener('click', dismiss);

    // Fail-safes so the intro can never trap the page:
    splash.addEventListener('click', function (e) { if (e.target === splash || e.target.classList.contains('splash-bg')) dismiss(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') dismiss(); });

    // Doce segundos y no dieciseis: si alguien deja la pestana abierta, la
    // intro no puede quedarse pintando indefinidamente delante de la tienda.
    setTimeout(dismiss, 12000);
  })();

  /* ---------- Navbar scroll ---------- */
  var navbar = $('.navbar');
  if (navbar) {
    // El evento scroll llega decenas de veces por segundo. Se apunta y se
    // resuelve una vez por fotograma, y solo se toca el DOM si el estado
    // cambia de verdad: tocar classList obliga a recalcular estilos.
    var navRaf = 0, navOn = null, annH = 0, navTop = null;

    // Alto de la barra de anuncios. La barra de navegacion es fija en top:0 y
    // tapaba el anuncio por completo: quien lo escribiera no lo veia nadie.
    // Se mide aqui y se publica como --nav-top, que baja a 0 conforme se
    // desplaza, asi el anuncio se lee arriba y la barra acaba pegada al borde.
    var ann = $('.announcement-bar');
    function medirAnn() {
      annH = ann ? ann.getBoundingClientRect().height : 0;
      navTop = null; // fuerza a reescribir la variable en el proximo fotograma
    }
    if (ann && 'ResizeObserver' in window) new ResizeObserver(medirAnn).observe(ann);

    var apply = function () {
      navRaf = 0;
      var y = window.scrollY || 0;
      var want = y > 40;
      if (want !== navOn) {
        navOn = want;
        navbar.classList.toggle('scrolled', want);
      }
      if (annH > 0) {
        var t = Math.max(0, Math.round(annH - y));
        if (t !== navTop) {
          navTop = t;
          document.documentElement.style.setProperty('--nav-top', t + 'px');
        }
      }
    };
    var onScroll = function () { if (!navRaf) navRaf = requestAnimationFrame(apply); };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () { medirAnn(); onScroll(); });
    medirAnn();
    apply();
  }

  /* ---------- Mobile menu ---------- */
  (function () {
    var toggle = $('.mobile-toggle');
    var menu = $('#mobile-menu');
    if (!toggle || !menu) return;
    var foco = panelAccesible(menu);
    function open() {
      menu.classList.add('open');
      document.body.style.overflow = 'hidden';
      toggle.setAttribute('aria-expanded', 'true');
      foco.entrar();
    }
    function close() {
      var estaba = menu.classList.contains('open');
      menu.classList.remove('open');
      document.body.style.overflow = '';
      toggle.setAttribute('aria-expanded', 'false');
      if (estaba) foco.salir();
    }
    // El botón solo abría: al volver a pulsarlo no pasaba nada y había que
    // buscar la X o el fondo para cerrar.
    toggle.addEventListener('click', function () {
      if (menu.classList.contains('open')) close(); else open();
    });
    $all('[data-mobile-close]', menu).forEach(function (b) { b.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

    // Al girar una tableta a horizontal la barra de escritorio toma el relevo y
    // el botón de menú desaparece, pero el panel seguía abierto y el body
    // bloqueado: la página quedaba sin poder desplazarse.
    if (window.matchMedia) {
      var wide = matchMedia('(min-width: 1024px)');
      var onWide = function (ev) { if (ev.matches) close(); };
      if (wide.addEventListener) wide.addEventListener('change', onWide);
      else if (wide.addListener) wide.addListener(onWide);
    }
  })();

  /* ---------- Cart drawer ---------- */
  var drawer = $('#cart-drawer');
  /* ---------- Panel accesible con teclado ----------
     Un panel que tapa la pagina tiene que hacer tres cosas, y el menu movil
     y el carrito no hacian ninguna (el visor de zoom si, de ahi salio el
     patron):
       1. Llevar el foco dentro al abrirse. Si no, quien navega con teclado o
          lector de pantalla no se entera de que ha pasado algo.
       2. Atrapar el foco mientras esta abierto. Sin esto, a las cuatro
          tabulaciones el foco se escapaba al contenido de detras y el
          visitante iba recorriendo enlaces que no puede ver. Medido.
       3. Devolver el foco a donde estaba al cerrarse, para no perder el
          sitio en la pagina.
     inert seria mas limpio que un capturador de Tab, pero no llega a Safari
     16 y en esta tienda pesan mucho los iPhone; el capturador funciona en
     todas partes. */
  var FOCO_SEL = 'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])';

  function panelAccesible(panel) {
    var previo = null;
    function visibles() {
      return $all(FOCO_SEL, panel).filter(function (e) {
        return e.offsetWidth > 0 || e.offsetHeight > 0 || e.getClientRects().length;
      });
    }
    function alTabular(e) {
      if (e.key !== 'Tab') return;
      var f = visibles();
      if (!f.length) { e.preventDefault(); return; }
      var primero = f[0], ultimo = f[f.length - 1];
      // Si el foco se ha ido fuera del panel (por ejemplo tras cargar
      // contenido nuevo), se trae de vuelta.
      if (!panel.contains(document.activeElement)) { e.preventDefault(); primero.focus(); return; }
      if (e.shiftKey && document.activeElement === primero) { e.preventDefault(); ultimo.focus(); }
      else if (!e.shiftKey && document.activeElement === ultimo) { e.preventDefault(); primero.focus(); }
    }
    return {
      entrar: function () {
        previo = document.activeElement;
        document.addEventListener('keydown', alTabular, true);
        // Un fotograma de margen: el panel se abre con una transicion y
        // enfocar un elemento aun oculto no hace nada.
        requestAnimationFrame(function () {
          var f = visibles();
          if (f.length) f[0].focus();
        });
      },
      salir: function () {
        document.removeEventListener('keydown', alTabular, true);
        if (previo && previo.focus && document.documentElement.contains(previo)) previo.focus();
        previo = null;
      }
    };
  }

  var focoCarrito = null;
  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (!focoCarrito) focoCarrito = panelAccesible(drawer);
    focoCarrito.entrar();
  }
  function closeDrawer() {
    if (!drawer) return;
    var estaba = drawer.classList.contains('open');
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (estaba && focoCarrito) focoCarrito.salir();
  }

  function updateCartCount(n) {
    $all('[data-cart-count]').forEach(function (el) {
      el.textContent = n;
      if (n > 0) { el.removeAttribute('hidden'); } else { el.setAttribute('hidden', ''); }
    });
  }

  /* Aviso visible. Sin esto, un fallo del carrito es invisible para el cliente. */
  function toast(msg, isError) {
    if (!msg) return;
    var t = document.createElement('div');
    t.className = 'toast';
    t.setAttribute('role', isError ? 'alert' : 'status');
    if (isError) { t.style.borderColor = 'var(--neon-orange)'; t.style.color = 'var(--neon-orange)'; }
    t.textContent = msg;
    document.body.appendChild(t);
    requestAnimationFrame(function () { t.classList.add('show'); });
    setTimeout(function () {
      t.classList.remove('show');
      setTimeout(function () { if (t.parentNode) t.parentNode.removeChild(t); }, 400);
    }, 4000);
  }

  /* Shopify responde 422 cuando no puede añadir (sin stock, excede inventario…).
     Hay que comprobar r.ok: si no, el fallo se toma por éxito y el cliente no ve nada. */
  function cartRequest(url, payload) {
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (data) {
        if (!r.ok) {
          var err = new Error(data.description || data.message || 'No se pudo actualizar el carrito');
          err.data = data;
          throw err;
        }
        return data;
      });
    });
  }

  /* Cola: las peticiones del carrito se ejecutan en orden. Pulsar +/- rápido lanzaba
     llamadas solapadas cuyas respuestas podían llegar desordenadas y dejar mal la cantidad. */
  var cartChain = Promise.resolve();
  function queueCart(task) {
    var run = cartChain.then(task, task);
    cartChain = run.catch(function () {});
    return run;
  }

  function cartAdd(id, qty) {
    return queueCart(function () { return cartRequest(routes.cartAdd, { id: id, quantity: qty || 1 }); });
  }

  function cartChange(key, qty) {
    return queueCart(function () { return cartRequest(routes.cartChange, { id: key, quantity: qty }); });
  }

  /* La PÁGINA de carrito también debe refrescarse: al cambiar la cantidad por AJAX, sus
     precios de línea y el subtotal se quedaban obsoletos hasta recargar a mano. */
  function syncCartPage() {
    var page = $('[data-cart-page]');
    if (!page) return Promise.resolve();
    return fetch(routes.cart + '?section_id=main')
      .then(function (r) { return r.text(); })
      .then(function (markup) {
        var doc = new DOMParser().parseFromString(markup, 'text/html');
        var fresh = doc.querySelector('[data-cart-page]');
        if (fresh) page.innerHTML = fresh.innerHTML;
      })
      .catch(function () {});
  }

  /* Refresca lo que esté visible: el carrito lateral y/o la página de carrito. */
  function syncCart() { return Promise.all([syncDrawer(), syncCartPage()]); }

  // Una sola petición: Shopify renderiza sections/cart-drawer.liquid (barra de envío gratis
  // y venta cruzada incluidas) y el contador se lee del propio marcado devuelto.
  function syncDrawer() {
    var body = $('[data-cart-drawer-body]');
    return fetch(routes.cart + '?section_id=cart-drawer')
      .then(function (r) { return r.text(); })
      .then(function (markup) {
        var doc = new DOMParser().parseFromString(markup, 'text/html');
        var fresh = doc.querySelector('[data-cart-drawer-body]');
        if (!fresh) return;
        updateCartCount(parseInt(fresh.getAttribute('data-cart-count') || '0', 10));
        if (body) body.innerHTML = fresh.innerHTML;
      })
      .catch(function () {});
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cart-drawer-open]') && settings.cartType === 'drawer') { e.preventDefault(); openDrawer(); return; }
    if (e.target.closest('[data-cart-drawer-close]')) { closeDrawer(); return; }

    var remove = e.target.closest('.cart-drawer-item-remove');
    if (remove) { e.preventDefault(); cartChange(remove.getAttribute('data-key'), 0).then(syncCart).catch(function (err) { toast(err && err.message, true); }); return; }

    var qUp = e.target.closest('[data-qty-up]');
    var qDown = e.target.closest('[data-qty-down]');
    if (qUp || qDown) {
      var wrap = (qUp || qDown).closest('[data-qty]');
      var input = $('[data-qty-input]', wrap);
      if (!input) return;
      var val = parseInt(input.value, 10) || 0;
      val = qUp ? val + 1 : Math.max(parseInt(input.min || '0', 10), val - 1);
      // El botón "+" subía sin límite aunque no hubiera existencias.
      var max = parseInt(input.getAttribute('max') || '', 10);
      if (!isNaN(max) && val > max) val = max;
      input.value = val;
      var key = input.getAttribute('data-key');
      if (key) { cartChange(key, val).then(syncCart).catch(function (err) { toast(err && err.message, true); }); }
      return;
    }

    if (e.target.closest('[data-scroll-top]')) { window.scrollTo({ top: 0, behavior: 'smooth' }); return; }
  });

  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });

  // Live qty typing in drawer
  document.addEventListener('change', function (e) {
    // Vale tanto para el carrito lateral como para la página de carrito.
    var input = e.target.closest('[data-cart-drawer-body] [data-qty-input], [data-cart-page] [data-qty-input]');
    if (input && input.getAttribute('data-key')) {
      cartChange(input.getAttribute('data-key'), Math.max(0, parseInt(input.value, 10) || 0)).then(syncCart).catch(function (err) { toast(err && err.message, true); });
    }
  });

  /* ---------- Quick add (product cards) ---------- */
  document.addEventListener('submit', function (e) {
    var form = e.target.closest('[data-quick-add]');
    if (!form) return;
    e.preventDefault();
    var id = form.querySelector('[name="id"]').value;
    var btn = form.querySelector('button');
    if (btn) btn.classList.add('is-loading');
    cartAdd(id, 1).then(function () {
      if (btn) btn.classList.remove('is-loading');
      if (settings.cartType === 'drawer') { syncDrawer().then(openDrawer); }
      else { window.location.href = routes.cart; }
    }).catch(function (err) {
      if (btn) btn.classList.remove('is-loading');
      toast(err && err.message, true);
    });
  });

  /* ---------- Product page ---------- */
  /* Registrado con mod(): al recargar la seccion en el editor de temas hay que
     volver a enlazar los selectores de variante, si no la ficha se queda muerta. */
  mod(function () {
    var section = $('.product-page');
    if (!section || !once(section, 'prod')) return;
    var variants = [];
    var json = $('[data-product-json]', section);
    if (json) { try { variants = JSON.parse(json.textContent); } catch (e) {} }

    var idInput = $('[data-variant-id]', section);
    var priceEls = $all('[data-price]', section);
    var compareEl = $('[data-compare]', section);
    var addBtn = $('[data-add-btn]', section);
    var addText = $('[data-add-text]', section);
    var savePctEl = $('[data-save-pct]', section);
    var saveWrap = $('[data-save-wrap]', section);
    var saveEl = $('[data-save]', section);
    var stockEl = $('[data-stock]', section);
    var lowStock = parseInt(section.getAttribute('data-low-stock') || '0', 10);

    // Mapa de existencias por variante: [id, cantidad, gestión, política]
    var inv = {};
    var invTag = $('[data-inventory-json]', section);
    if (invTag) {
      try {
        JSON.parse(invTag.textContent).forEach(function (r) {
          inv[r[0]] = { qty: r[1], tracked: r[2], policy: r[3] };
        });
      } catch (e) {}
    }
    function stockOf(v) {
      var rec = v && inv[v.id];
      if (rec) return rec;
      // Reserva por si el mapa no estuviera: los datos de la variante.
      return v ? { qty: v.inventory_quantity, tracked: v.inventory_management, policy: v.inventory_policy } : null;
    }

    // La posición se lee del nombre (option1, option2, option3). Antes se
    // recogían los marcados en orden de aparición: si un grupo se quedaba sin
    // ninguno marcado, la lista se acortaba, los índices se desplazaban y se
    // podía emparejar una variante distinta a la elegida.
    function optionPosition(input) {
      var m = (input.name || '').match(/(\d+)/);
      return m ? parseInt(m[1], 10) - 1 : 0;
    }
    function selectedOptions() {
      var out = [];
      $all('[data-option-selector]', section).forEach(function (i) {
        if (i.checked) out[optionPosition(i)] = i.value;
      });
      return out;
    }
    function optionCount() {
      var n = 0;
      $all('[data-option-selector]', section).forEach(function (i) {
        var p = optionPosition(i) + 1;
        if (p > n) n = p;
      });
      return n;
    }
    function matchVariant() {
      var opts = selectedOptions();
      var need = optionCount();
      if (!need) return variants[0];
      // Toda opción debe estar elegida; si falta alguna no hay variante válida.
      for (var i = 0; i < need; i++) { if (opts[i] == null) return null; }
      return variants.find(function (v) {
        for (var i = 0; i < need; i++) { if (v.options[i] !== opts[i]) return false; }
        return true;
      });
    }

    // Marca las combinaciones agotadas o inexistentes para que el cliente no
    // vaya probando a ciegas. No se desactivan: si se desactivaran, quien
    // eligiera una talla que solo existe en un color quedaría atrapado.
    function markOptions() {
      var current = selectedOptions();
      $all('[data-option-selector]', section).forEach(function (input) {
        var trial = current.slice();
        trial[optionPosition(input)] = input.value;
        var matches = variants.filter(function (v) {
          for (var i = 0; i < trial.length; i++) {
            if (trial[i] != null && v.options[i] !== trial[i]) return false;
          }
          return true;
        });
        var label = section.querySelector('label[for="' + input.id + '"]');
        if (!label) return;
        label.classList.toggle('is-unavailable', matches.length === 0);
        label.classList.toggle('is-sold-out', matches.length > 0 && !matches.some(function (v) { return v.available; }));
      });
    }
    function setUnavailable() {
      // La combinación elegida no existe. Antes se hacía "return" y quedaba el estado de la
      // variante ANTERIOR: precio viejo, su id en el formulario y el botón activo, de modo que
      // el cliente podía comprar una variante distinta a la que seleccionó.
      if (idInput) idInput.value = '';
      if (addBtn) {
        addBtn.disabled = true;
        if (addText) addText.textContent = strings.unavailable || 'No disponible';
      }
      var sBtnU = $('[data-sticky-add]', section);
      if (sBtnU) { sBtnU.disabled = true; sBtnU.textContent = strings.unavailable || 'No disponible'; }
      if (compareEl) compareEl.style.display = 'none';
      if (savePctEl) savePctEl.style.display = 'none';
      if (saveWrap) saveWrap.style.display = 'none';
      if (stockEl) stockEl.style.display = 'none';
    }

    // Sin esto el cliente podía pedir 50 unidades de algo con 3 en existencia:
    // Shopify rechazaba el carrito y el error aparecía después, sin explicación
    // clara. Ahora el propio campo no deja pasar de lo que hay.
    function applyStockLimit(v) {
      var qtyEl = section.querySelector('[name="quantity"]');
      if (!qtyEl) return;
      var rec = stockOf(v);
      var tracked = rec && rec.tracked != null && rec.tracked !== '';
      var denies = !rec || rec.policy !== 'continue';
      var q = rec ? rec.qty : null;
      if (tracked && denies && typeof q === 'number' && q > 0) {
        qtyEl.setAttribute('max', q);
        if ((parseInt(qtyEl.value, 10) || 1) > q) qtyEl.value = q;
      } else {
        qtyEl.removeAttribute('max');
      }
    }

    function update() {
      markOptions();
      var v = matchVariant();
      if (!v) { setUnavailable(); return; }
      applyStockLimit(v);
      if (idInput) idInput.value = v.id;
      priceEls.forEach(function (el) { el.textContent = money(v.price); });
      var onSale = v.compare_at_price > v.price;
      if (compareEl) {
        if (onSale) { compareEl.textContent = money(v.compare_at_price); compareEl.style.display = ''; }
        else { compareEl.style.display = 'none'; }
      }
      if (savePctEl) {
        if (onSale) { savePctEl.textContent = '-' + Math.round((v.compare_at_price - v.price) * 100 / v.compare_at_price) + '%'; savePctEl.style.display = ''; }
        else { savePctEl.style.display = 'none'; }
      }
      if (saveWrap) {
        if (onSale) { if (saveEl) saveEl.textContent = money(v.compare_at_price - v.price); saveWrap.style.display = ''; }
        else { saveWrap.style.display = 'none'; }
      }
      if (stockEl) {
        var srec = stockOf(v);
        var q = srec ? srec.qty : null;
        var managed = srec && srec.tracked != null && srec.tracked !== '';
        if (lowStock > 0 && managed && typeof q === 'number' && q > 0 && q <= lowStock) {
          var tpl = stockEl.getAttribute('data-stock-tpl') || '';
          var span = stockEl.querySelector('span');
          if (span) span.textContent = tpl.replace('[n]', q);
          stockEl.style.display = '';
        } else { stockEl.style.display = 'none'; }
      }
      if (addBtn) {
        addBtn.disabled = !v.available;
        if (addText) addText.textContent = v.available ? (strings.addToCart || 'Add to cart') : (strings.soldOut || 'Sold out');
      }
      // La barra fija debe reflejar la disponibilidad, no quedarse "activa" en agotados
      var sBtn = $('[data-sticky-add]', section);
      if (sBtn) {
        sBtn.disabled = !v.available;
        sBtn.textContent = v.available ? (strings.addToCart || 'Add to cart') : (strings.soldOut || 'Sold out');
      }
      try {
        var url = new URL(window.location);
        url.searchParams.set('variant', v.id);
        window.history.replaceState({}, '', url);
      } catch (e) {}
    }
    $all('[data-option-selector]', section).forEach(function (i) { i.addEventListener('change', update); });
    markOptions();   // estado inicial al cargar la ficha

    $all('[data-media-target]', section).forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        var id = thumb.getAttribute('data-media-target');
        $all('.product-media-item', section).forEach(function (m) { m.classList.toggle('is-active', m.getAttribute('data-media-id') === id); });
        $all('[data-media-target]', section).forEach(function (t) { t.classList.toggle('is-active', t === thumb); });
      });
    });

    var pform = $('#product-form', section) || $('form', section);
    if (pform) {
      pform.addEventListener('submit', function (e) {
        e.preventDefault();
        var id = idInput ? idInput.value : (pform.querySelector('[name="id"]') || {}).value;
        // Sin variante válida no se envía nada: evita pedidos de la variante equivocada.
        if (!id) { toast(strings.unavailable || 'No disponible', true); return; }
        var qtyEl = pform.querySelector('[name="quantity"]');
        var qty = parseInt(qtyEl ? qtyEl.value : '1', 10) || 1;
        if (addBtn) addBtn.classList.add('is-loading');
        cartAdd(id, qty).then(function () {
          if (addBtn) addBtn.classList.remove('is-loading');
          if (settings.cartType === 'drawer') { syncDrawer().then(openDrawer); }
          else { window.location.href = routes.cart; }
        }).catch(function (err) {
          if (addBtn) addBtn.classList.remove('is-loading');
          toast(err && err.message, true);
        });
      });
    }

    /* Sticky add-to-cart bar: appears once the main purchase area scrolls out of view */
    var stickyBar = $('[data-sticky-atc]', section);
    var purchaseAnchor = $('.product-purchase', section);
    if (stickyBar && purchaseAnchor && 'IntersectionObserver' in window) {
      var sObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          // show only when the buy button is above the viewport (already scrolled past)
          var past = !e.isIntersecting && e.boundingClientRect.top < 0;
          stickyBar.classList.toggle('is-visible', past);
          stickyBar.setAttribute('aria-hidden', past ? 'false' : 'true');
        });
      }, { threshold: 0 });
      sObs.observe(purchaseAnchor);
      var sAdd = $('[data-sticky-add]', stickyBar);
      if (sAdd && addBtn) sAdd.addEventListener('click', function () { addBtn.click(); });
    }
  });

  /* ---------- Collection sort auto-submit ---------- */
  $all('[data-collection-sort] select').forEach(function (sel) {
    sel.addEventListener('change', function () {
      var url = new URL(window.location);
      url.searchParams.set('sort_by', sel.value);
      url.searchParams.delete('page');
      window.location.href = url.toString();
    });
  });

  /* ---------- Miniaturas de video: cadena de respaldo ----------
     i.ytimg.com no es el CDN de Shopify y falla mas de lo que parece: la
     bloquean casi todos los bloqueadores de anuncios, y hay videos que no
     tienen todos los tamanos de miniatura. Sin esto, la tarjeta se quedaba en
     negro puro con el icono de imagen rota asomando.

     Se prueba el siguiente tamano y, si tampoco carga, se retira la imagen y
     queda el respaldo de marca que ya esta pintado debajo. El manejador va
     aqui y no en un atributo onerror porque la politica de seguridad de
     contenido de algunas tiendas bloquea el JavaScript suelto en atributos. */
  $all('[data-v-thumb]').forEach(function (img) {
    function fallo() {
      var alt1 = img.getAttribute('data-alt1');
      if (alt1) { img.removeAttribute('data-alt1'); img.src = alt1; return; }
      img.classList.add('esta-rota');
    }
    img.addEventListener('error', fallo);
    // Una imagen que ya venia fallada del cache no vuelve a emitir 'error'.
    if (img.complete && img.naturalWidth === 0) fallo();
  });

  /* ---------- Lazy YouTube embeds ---------- */
  $all('[data-video-embed]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('data-video-embed');
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0';
      iframe.title = btn.getAttribute('aria-label') || 'Video';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      iframe.loading = 'lazy';
      iframe.className = 'video-card-iframe';
      btn.parentNode.replaceChild(iframe, btn);
    });
  });

  /* ---------- Desplegables del escritorio en pantallas táctiles ----------
     La barra de escritorio aparece a partir de 1024px, que es justo el ancho
     de una tableta en horizontal. Ahí el puntero no tiene hover: al tocar
     "Catálogo" se navegaba a la colección y el mega-menú, que solo se abre
     con :hover, no se veía nunca. Primer toque abre, segundo navega. */
  mod(function () {
    if (!window.matchMedia || !matchMedia('(hover: none)').matches) return;

    function closeAll(except) {
      $all('.nav-item.is-open').forEach(function (o) {
        if (o === except) return;
        o.classList.remove('is-open');
        var a = o.querySelector('.nav-link');
        if (a) a.setAttribute('aria-expanded', 'false');
      });
    }

    $all('.nav-item > .nav-link').forEach(function (link) {
      if (!once(link, 'tapdd')) return;
      var item = link.parentElement;
      if (!item.querySelector('.nav-dropdown')) return;
      link.setAttribute('aria-expanded', 'false');
      link.addEventListener('click', function (e) {
        if (item.classList.contains('is-open')) return;   // segundo toque: navega
        e.preventDefault();
        closeAll(item);
        item.classList.add('is-open');
        link.setAttribute('aria-expanded', 'true');
      });
    });

    if (once(document.documentElement, 'tapddout')) {
      document.addEventListener('click', function (e) {
        if (e.target.closest('.nav-item')) return;
        closeAll(null);
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeAll(null);
      });
    }
  });

  /* ---------- Mobile submenu toggle (tap to open/close) ---------- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-mobile-toggle]');
    if (!t) return;
    var sub = t.parentElement.querySelector('.mobile-submenu');
    if (!sub) return;
    var open = t.getAttribute('aria-expanded') === 'true';
    t.setAttribute('aria-expanded', String(!open));
    if (open) { sub.setAttribute('hidden', ''); } else { sub.removeAttribute('hidden'); }
    t.classList.toggle('is-open', !open);
  });

  /* ---------- Language: manual persist + one-time auto-detect ---------- */
  (function () {
    var sel = $('[data-lang-select]');
    var form = document.getElementById('LangSelectorForm');
    if (sel && form) {
      sel.addEventListener('change', function () {
        store.set('v99_lang_choice', sel.value);
        form.submit();
      });
    }
    // Auto-detect (browser language) only once, never overriding a manual choice.
    if (!settings.autoLang || !form || !sel) return;
    try {
      if (store.get('v99_lang_choice') || store.get('v99_lang_auto', true)) return;
      store.set('v99_lang_auto', '1', true);
      var current = (settings.locale || 'es').slice(0, 2).toLowerCase();
      // navigator.languages es el más fiable en iOS/Android/Mac/Windows; probamos
      // las preferencias del visitante en orden hasta encontrar un idioma disponible.
      var langs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
      var match = null;
      for (var li = 0; li < langs.length && !match; li++) {
        var wanted = (langs[li] || '').slice(0, 2).toLowerCase();
        if (!wanted) continue;
        if (wanted === current) return; // ya está en su idioma
        Array.prototype.forEach.call(sel.options, function (o) {
          if (!match && o.value.slice(0, 2).toLowerCase() === wanted) match = o.value;
        });
      }
      if (match) { sel.value = match; form.submit(); }
    } catch (e) {}
  })();

  /* ---------- Carousels (videos, etc.) ---------- */
  mod(function () {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    $all('[data-carousel]').forEach(function (root) {
      if (!once(root, 'car')) return;
      var track = $('[data-carousel-track]', root);
      if (!track) return;
      var prev = $('[data-carousel-prev]', root);
      var next = $('[data-carousel-next]', root);
      function step() { return Math.max(track.clientWidth * 0.8, 200); }
      function updateArrows() {
        var atStart = track.scrollLeft <= 4;
        var atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
        var noOverflow = track.scrollWidth <= track.clientWidth + 4;
        [prev, next].forEach(function (b) { if (b) b.style.display = noOverflow ? 'none' : ''; });
        if (prev) prev.classList.toggle('is-disabled', atStart);
        if (next) next.classList.toggle('is-disabled', atEnd);
      }
      if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
      if (next) next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
      track.addEventListener('scroll', function () { window.requestAnimationFrame(updateArrows); }, { passive: true });
      window.addEventListener('resize', updateArrows);
      updateArrows();

      var speed = parseFloat(root.getAttribute('data-autoplay')) || 0;
      if (speed > 0 && !reduced) {
        var timer = null;
        function tick() {
          if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) {
            track.scrollTo({ left: 0, behavior: 'smooth' });
          } else {
            track.scrollBy({ left: step(), behavior: 'smooth' });
          }
        }
        function start() { if (!timer) timer = setInterval(tick, speed * 1000); }
        function stop() { if (timer) { clearInterval(timer); timer = null; } }
        start();
        root.addEventListener('mouseenter', stop);
        root.addEventListener('mouseleave', start);
        root.addEventListener('focusin', stop);
        root.addEventListener('focusout', start);
        root.addEventListener('touchstart', stop, { passive: true });
        document.addEventListener('visibilitychange', function () { if (document.hidden) { stop(); } else { start(); } });
      }
    });
  });

  /* ---------- Flipbook / PDF catalog (lazy) ---------- */
  $all('[data-flipbook-load]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var frame = btn.closest('[data-flipbook]');
      if (!frame) return;
      var url = frame.getAttribute('data-flipbook');
      if (!url) return;
      var iframe = document.createElement('iframe');
      iframe.src = url;
      iframe.title = 'Catálogo';
      iframe.loading = 'lazy';
      iframe.setAttribute('allowfullscreen', '');
      frame.innerHTML = '';
      frame.appendChild(iframe);
    });
  });

  /* ---------- FAQ (details already native; smooth single-open optional) ---------- */
  $all('.faq-list').forEach(function (list) {
    list.addEventListener('toggle', function (e) {
      var t = e.target;
      if (t.tagName === 'DETAILS' && t.open) {
        $all('details.faq-item', list).forEach(function (d) { if (d !== t) d.open = false; });
      }
    }, true);
  });

  /* ---------- Animated counters (stats band) ---------- */
  mod(function () {
    var els = $all('[data-countup]');
    els = els.filter(function (e) { return once(e, 'countup'); });
    if (!els.length) return;
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function animate(el) {
      var target = parseFloat(el.getAttribute('data-countup')) || 0;
      if (reduced) { el.textContent = target.toLocaleString(); return; }
      var start = null, dur = 1600;
      function frame(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased).toLocaleString();
        if (p < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }
    if (!('IntersectionObserver' in window)) { els.forEach(animate); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { animate(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.4 });
    els.forEach(function (el) { io.observe(el); });
  });

  /* ---------- Countdown ---------- */
  $all('[data-countdown]').forEach(function (root) {
    var target = new Date((root.getAttribute('data-countdown') || '').replace(/-/g, '/')).getTime();
    if (isNaN(target)) return;
    var d = $('[data-cd-days]', root), h = $('[data-cd-hours]', root), m = $('[data-cd-mins]', root), s = $('[data-cd-secs]', root);
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function tick() {
      var diff = target - Date.now();
      if (diff <= 0) {
        root.innerHTML = '<p class="countdown-expired">' + (root.getAttribute('data-expired') || '') + '</p>';
        clearInterval(iv);
        return;
      }
      var sec = Math.floor(diff / 1000);
      if (d) d.textContent = pad(Math.floor(sec / 86400));
      if (h) h.textContent = pad(Math.floor((sec % 86400) / 3600));
      if (m) m.textContent = pad(Math.floor((sec % 3600) / 60));
      if (s) s.textContent = pad(sec % 60);
    }
    tick();
    var iv = setInterval(tick, 1000);
  });

  /* ---------- Footer motivational quotes (fade rotation) ---------- */
  mod(function () {
    var wrap = $('[data-quotes]');
    if (!wrap || !once(wrap, 'quotes')) return;
    var textEl = $('[data-quote-text]', wrap);
    var listEl = $('[data-quote-list]', wrap);
    if (!textEl || !listEl) return;
    var quotes = [];
    try { quotes = JSON.parse(listEl.textContent).map(function (q) { return q.trim(); }).filter(Boolean); } catch (e) { return; }
    if (quotes.length < 2) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var i = 0;
    setInterval(function () {
      i = (i + 1) % quotes.length;
      textEl.classList.add('is-fading');
      setTimeout(function () { textEl.textContent = quotes[i]; textEl.classList.remove('is-fading'); }, 400);
    }, 5000);
  });

  /* ---------- Hero rotating words ---------- */
  mod(function () {
    var el = $('[data-typed]');
    if (!el || !once(el, 'typed')) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var words = [];
    try { words = JSON.parse(el.getAttribute('data-typed')).map(function (w) { return w.trim(); }); } catch (e) { return; }
    if (words.length < 2) return;
    el.style.transition = 'opacity 0.25s ease';
    var i = 0;
    setInterval(function () {
      i = (i + 1) % words.length;
      el.style.opacity = '0';
      setTimeout(function () { el.textContent = words[i]; el.style.opacity = '1'; }, 250);
    }, 2600);
  });

  /* Pre-decodifica la 2ª imagen de cada tarjeta al entrar en pantalla, para que
     el cambio al pasar el cursor sea instantáneo (sin tirón de decodificación). */
  (function () {
    var imgs = $all('[data-decode]');
    if (!imgs.length || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var img = e.target;
        io.unobserve(img);
        try { img.loading = 'eager'; if (img.decode) img.decode().catch(function () {}); } catch (err) {}
      });
    }, { rootMargin: '300px 1100px' }); // margen horizontal amplio: precarga las diapositivas vecinas de los carruseles
    imgs.forEach(function (img) { io.observe(img); });
  });

  /* ---------- Product image lightbox (zoom) ---------- */
  (function () {
    var zoomables = $all('[data-zoomable]');
    if (!zoomables.length) return;
    var box = null, boxImg = null;
    function build() {
      box = document.createElement('div');
      box.className = 'img-lightbox';
      box.setAttribute('role', 'dialog');
      box.setAttribute('aria-modal', 'true');
      box.innerHTML = '<button class="img-lightbox-close" aria-label="Cerrar">&times;</button><img alt="">';
      boxImg = box.querySelector('img');
      // El puntero muestra "zoom-out" sobre todo el visor, así que cualquier
      // clic dentro debe cerrarlo. Antes solo cerraba el fondo o la X, y esa X
      // quedaba tapada por la barra de navegación: no había forma de salir
      // salvo con Escape.
      box.addEventListener('click', close);
      document.body.appendChild(box);
    }
    var lastFocus = null;
    function open(src, alt) {
      if (!box) build();
      lastFocus = document.activeElement;
      boxImg.src = src; boxImg.alt = alt || '';
      requestAnimationFrame(function () {
        box.classList.add('is-open');
        var c = box.querySelector('.img-lightbox-close');
        if (c) c.focus();
      });
      document.documentElement.style.overflow = 'hidden';
    }
    function close() {
      if (!box || !box.classList.contains('is-open')) return;
      box.classList.remove('is-open');
      document.documentElement.style.overflow = '';
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    zoomables.forEach(function (img) {
      img.style.cursor = 'zoom-in';
      // Accesible por teclado: cualquiera puede abrir el zoom con Enter/Espacio
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      function fire() { open(img.getAttribute('data-zoom-src') || img.currentSrc || img.src, img.alt); }
      img.addEventListener('click', fire);
      img.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); }
      });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  })();

  /* ---------- Predictive search (live results) ---------- */
  (function () {
    var panel = $('[data-search-panel]');
    var toggle = $('[data-search-toggle]');
    if (!panel || !toggle) return;
    var input = $('[data-search-input]', panel);
    var results = $('[data-search-results]', panel);
    var closeBtn = $('[data-search-close]', panel);
    var timer = null, controller = null, lastQ = '';

    function open() {
      panel.hidden = false;
      requestAnimationFrame(function () { panel.classList.add('is-open'); if (input) input.focus(); });
      toggle.setAttribute('aria-expanded', 'true');
    }
    function close() {
      panel.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      if (input) input.setAttribute('aria-expanded', 'false');
      setTimeout(function () { panel.hidden = true; }, 220);
    }
    toggle.addEventListener('click', function () { panel.hidden ? open() : close(); });
    if (closeBtn) closeBtn.addEventListener('click', close);

    /* ---- Dictado por voz ----
       El navegador escribe en el mismo campo, asi que la busqueda predictiva
       que ya existe se dispara sola: no hay una segunda ruta que mantener.
       El boton solo se destapa si el reconocimiento existe de verdad. */
    (function () {
      var btnVoz = $('[data-search-voice]', panel);
      var Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!btnVoz || !Reco) return;
      btnVoz.hidden = false;

      var reco = null;
      function parar() {
        if (reco) { try { reco.stop(); } catch (e) {} reco = null; }
        btnVoz.classList.remove('is-listening');
        btnVoz.setAttribute('aria-pressed', 'false');
      }
      btnVoz.addEventListener('click', function () {
        if (reco) { parar(); return; }
        reco = new Reco();
        // El idioma sale del <html lang>, asi que dicta en el idioma que el
        // visitante esta viendo y no siempre en el principal de la tienda.
        reco.lang = document.documentElement.lang || 'es';
        reco.interimResults = true;
        reco.continuous = false;
        btnVoz.classList.add('is-listening');
        btnVoz.setAttribute('aria-pressed', 'true');
        reco.onresult = function (ev) {
          var texto = '';
          for (var i = 0; i < ev.results.length; i++) texto += ev.results[i][0].transcript;
          if (!input) return;
          input.value = texto;
          // El evento input es lo que despierta a la busqueda predictiva.
          input.dispatchEvent(new Event('input', { bubbles: true }));
        };
        reco.onerror = parar;
        reco.onend = function () { parar(); if (input) input.focus(); };
        try { reco.start(); } catch (e) { parar(); }
      });
      // Si se cierra el panel mientras escucha, se corta el microfono.
      if (closeBtn) closeBtn.addEventListener('click', parar);
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') parar(); });
    })();
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { close(); toggle.focus(); } });

    var esc = function (s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; };

    // suggest.json devuelve el precio como texto; normalizamos separadores de
    // miles/decimales de cualquier localización antes de formatear.
    function priceText(v) {
      if (v == null || v === '') return '';
      var s = String(v).replace(/[^0-9.,]/g, '');
      if (/[.,]\d{1,2}$/.test(s)) {
        var sep = s.slice(-3).match(/[.,]/)[0];
        var other = sep === ',' ? '.' : ',';
        s = s.split(other).join('').replace(sep, '.');
      } else {
        s = s.replace(/[.,]/g, '');
      }
      var n = parseFloat(s);
      return isNaN(n) ? String(v) : money(Math.round(n * 100));
    }

    function render(items, q) {
      if (!items.length) {
        results.innerHTML = '<p class="search-empty">' + esc((strings.noResults || 'Sin resultados para') + ' "' + q + '"') + '</p>';
        return;
      }
      results.innerHTML = items.map(function (p) {
        var img = p.featured_image && p.featured_image.url ? p.featured_image.url : '';
        return '<a class="search-item" role="option" href="' + esc(p.url) + '">' +
          '<span class="search-item-media">' + (img ? '<img src="' + esc(img) + '" alt="" width="48" height="48" loading="lazy">' : '') + '</span>' +
          '<span class="search-item-info"><span class="search-item-title">' + esc(p.title) + '</span>' +
          '<span class="search-item-price">' + esc(priceText(p.price)) + '</span></span></a>';
      }).join('') + '<a class="search-all" href="' + esc(routes.search + '?q=' + encodeURIComponent(q)) + '">' +
        esc(strings.viewAll || 'Ver todos los resultados') + '</a>';
    }

    // Si la búsqueda falla no dejamos el panel colgado en "…": ofrecemos el
    // enlace a la búsqueda completa, que es una página normal y siempre carga.
    function renderError(q) {
      results.innerHTML = '<p class="search-empty">' + esc(strings.searchError || 'No se pudo buscar ahora mismo.') + '</p>' +
        '<a class="search-all" href="' + esc(routes.search + '?q=' + encodeURIComponent(q)) + '">' +
        esc(strings.viewAll || 'Ver todos los resultados') + '</a>';
      if (input) input.setAttribute('aria-expanded', 'false');
    }

    function search(q) {
      if (controller) controller.abort();
      controller = new AbortController();
      // routes.predictiveSearch respeta el prefijo de idioma (/fr/, /es/);
      // la ruta fija /search/suggest.json devolvía resultados en otro idioma.
      var base = routes.predictiveSearch || '/search/suggest.json';
      var url = base + (base.indexOf('?') > -1 ? '&' : '?') + 'q=' + encodeURIComponent(q) +
        '&resources[type]=product&resources[limit]=6&resources[options][unavailable_products]=last';
      fetch(url, { signal: controller.signal })
        .then(function (r) {
          if (!r.ok) throw new Error('search ' + r.status);
          return r.json();
        })
        .then(function (d) {
          var items = (d.resources && d.resources.results && d.resources.results.products) || [];
          render(items, q);
          if (input) input.setAttribute('aria-expanded', items.length ? 'true' : 'false');
        })
        .catch(function (e) {
          // Abortar es normal (el visitante siguió escribiendo): no es un fallo.
          if (e && e.name === 'AbortError') return;
          lastQ = '';   // permite reintentar escribiendo lo mismo otra vez
          renderError(q);
        });
    }

    if (input) {
      input.addEventListener('input', function () {
        var q = input.value.trim();
        clearTimeout(timer);
        if (q.length < 2) { results.innerHTML = ''; input.setAttribute('aria-expanded', 'false'); return; }
        if (q === lastQ) return;
        lastQ = q;
        results.innerHTML = '<p class="search-loading">…</p>';
        timer = setTimeout(function () { search(q); }, 250);
      });

      // Navegación con teclado dentro de la lista de resultados.
      input.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp' && e.key !== 'Enter') return;
        var links = results.querySelectorAll('a');
        if (!links.length) return;
        if (e.key === 'Enter') {
          var active = results.querySelector('.is-active');
          if (active) { e.preventDefault(); active.click(); }
          return;
        }
        e.preventDefault();
        var idx = -1;
        for (var i = 0; i < links.length; i++) {
          if (links[i].classList.contains('is-active')) { idx = i; links[i].classList.remove('is-active'); break; }
        }
        idx = e.key === 'ArrowDown' ? idx + 1 : idx - 1;
        if (idx < 0) idx = links.length - 1;
        if (idx >= links.length) idx = 0;
        links[idx].classList.add('is-active');
        links[idx].scrollIntoView({ block: 'nearest' });
      });
    }

    // Cerrar al pulsar fuera del panel.
    document.addEventListener('click', function (e) {
      if (panel.hidden) return;
      if (panel.contains(e.target) || toggle.contains(e.target)) return;
      close();
    });
  })();

  /* ---------- Modelos 3D y realidad aumentada ----------
     model_viewer_tag solo escribe el elemento <model-viewer>: es un elemento
     personalizado que no existe hasta que se cargan las funciones oficiales de
     Shopify. Sin esto el visor no giraba, no tenía controles y el botón de RA
     no hacía nada. Se carga solo si la página tiene algún modelo. */
  var xrRequested = false;

  function initModelViewers() {
    if (!window.Shopify || typeof window.Shopify.ModelViewerUI !== 'function') return;
    Array.prototype.forEach.call(document.querySelectorAll('model-viewer'), function (el) {
      if (!once(el, 'mvui')) return;
      try { new window.Shopify.ModelViewerUI(el); } catch (e) {}
    });
  }

  function setupXR() {
    if (!window.ShopifyXR) {
      // La librería avisa cuando termina de arrancar.
      document.addEventListener('shopify_xr_initialized', setupXR);
      return;
    }
    Array.prototype.forEach.call(document.querySelectorAll('[data-model-json]'), function (tag) {
      if (!once(tag, 'xrjson')) return;
      try { window.ShopifyXR.addModels(JSON.parse(tag.textContent)); } catch (e) {}
    });
    try { window.ShopifyXR.setupXRElements(); } catch (e) {}
  }

  mod(function () {
    if (!document.querySelector('model-viewer')) return;
    if (!window.Shopify || typeof window.Shopify.loadFeatures !== 'function') return;

    // Al recargar una sección en el editor solo hay que registrar lo nuevo.
    if (xrRequested) { initModelViewers(); setupXR(); return; }
    xrRequested = true;

    if (!document.getElementById('shopify-model-viewer-ui-styles')) {
      var link = document.createElement('link');
      link.id = 'shopify-model-viewer-ui-styles';
      link.rel = 'stylesheet';
      link.href = 'https://cdn.shopify.com/shopifycloud/model-viewer-ui/assets/v1.0/model-viewer-ui.css';
      document.head.appendChild(link);
    }

    window.Shopify.loadFeatures([
      { name: 'model-viewer-ui', version: '1.0', onLoad: function (errors) { if (!errors) initModelViewers(); } },
      { name: 'shopify-xr', version: '1.0', onLoad: function (errors) { if (!errors) setupXR(); } }
    ]);
  });

  /* ---------- Recomendaciones de producto ----------
     Las elige Shopify; aqui solo se piden. Se traen con la API de renderizado
     de secciones y solo cuando el bloque esta a punto de entrar en pantalla,
     asi la ficha de producto no espera por ellas. Si Shopify no devuelve nada
     util, el contenedor se retira entero y no queda un hueco en la pagina. */
  mod(function () {
    $all('[data-recos]').forEach(function (host) {
      if (!once(host, 'recos')) return;
      var url = host.getAttribute('data-url');
      if (!url) return;

      function traer() {
        fetch(url)
          .then(function (r) { return r.ok ? r.text() : Promise.reject(r.status); })
          .then(function (html) {
            var caja = document.createElement('div');
            caja.innerHTML = html;
            var dentro = caja.querySelector('[data-recos]');
            if (dentro && dentro.innerHTML.trim()) {
              host.innerHTML = dentro.innerHTML;
              // Las tarjetas recien llegadas necesitan que se les enganchen
              // los efectos y el anadir-al-carrito, igual que a las demas.
              document.dispatchEvent(new CustomEvent('shopify:section:load'));
            } else {
              host.remove();
            }
          })
          .catch(function () { host.remove(); });
      }

      if (!('IntersectionObserver' in window)) { traer(); return; }
      var io = new IntersectionObserver(function (en) {
        if (!en[0] || !en[0].isIntersecting) return;
        io.disconnect();
        traer();
      }, { rootMargin: '0px 0px 300px 0px' });
      io.observe(host);
    });
  });

  /* ---------- Recently viewed (localStorage, no server/app needed) ---------- */
  (function () {
    var KEY = 'v99_recently_viewed';
    function read() { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
    function write(list) { try { localStorage.setItem(KEY, JSON.stringify(list.slice(0, 12))); } catch (e) {} }

    // 1) Record the product currently being viewed
    var cur = $('[data-rv-current]');
    if (cur) {
      try {
        var p = JSON.parse(cur.textContent);
        if (p && p.id && p.url) {
          var list = read().filter(function (x) { return x.id !== p.id; });
          list.unshift(p);
          write(list);
        }
      } catch (e) {}
    }

    // 2) Render the history section (excluding the product being viewed)
    //    Registrado con mod(): al añadir o mover esta sección en el editor de
    //    temas, antes se quedaba oculta hasta recargar la página entera.
    mod(function () {
    var host = $('[data-recently-viewed]');
    if (!host || !once(host, 'rv')) return;
    var grid = $('[data-rv-grid]', host);
    if (!grid) return;
    var limit = parseInt(host.getAttribute('data-limit') || '4', 10);
    var currentId = null;
    if (cur) { try { currentId = JSON.parse(cur.textContent).id; } catch (e) {} }
    var items = read().filter(function (x) { return x && x.id !== currentId && x.url; }).slice(0, limit);
    if (!items.length) return;

    var esc = function (s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; };
    grid.innerHTML = items.map(function (p) {
      return '<div class="product-card rv-card">' +
        '<a href="' + esc(p.url) + '" class="product-card-image" aria-label="' + esc(p.title) + '">' +
          (p.image ? '<img src="' + esc(p.image) + '" alt="' + esc(p.title) + '" width="400" height="400" loading="lazy" decoding="async">' : '') +
        '</a>' +
        '<div class="product-card-body">' +
          '<h3 class="product-card-title"><a href="' + esc(p.url) + '">' + esc(p.title) + '</a></h3>' +
          '<div class="product-card-footer"><div class="product-price"><span class="product-price-amount">' + esc(p.price) + '</span></div></div>' +
        '</div></div>';
    }).join('');
    host.hidden = false;
    });
  })();

  /* ---------- Copy coupon code ---------- */
  /* Registrado con mod(): el cupón de una sección de boletín añadida desde el
     editor no reaccionaba al pulsarlo hasta recargar la página. */
  mod(function () {
  $all('[data-copy-code]').forEach(function (btn) {
    if (!once(btn, 'copy')) return;
    btn.addEventListener('click', function () {
      var code = btn.getAttribute('data-code') || '';
      var done = function () {
        btn.classList.add('copied');
        var hint = btn.querySelector('.nl-code-hint');
        if (hint) {
          // Guardamos el texto original una sola vez: al pulsar dos veces
          // seguidas se quedaba "¡Copiado!" fijo para siempre.
          if (!hint.getAttribute('data-label')) hint.setAttribute('data-label', hint.textContent);
          hint.textContent = strings.copied || 'OK';
          setTimeout(function () {
            hint.textContent = hint.getAttribute('data-label');
            btn.classList.remove('copied');
          }, 1600);
        }
      };
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(code).then(done).catch(done); }
      else { var t = document.createElement('textarea'); t.value = code; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(t); done(); }
    });
  });
  });

  /* ---------- Back to top ---------- */
  (function () {
    var btn = $('[data-back-to-top]');
    if (!btn) return;
    var shown = false;
    function onScroll() {
      var s = (window.scrollY || document.documentElement.scrollTop) > 600;
      if (s !== shown) { shown = s; btn.classList.toggle('is-visible', s); }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    btn.addEventListener('click', function () {
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    });
    onScroll();
  })();
})();
