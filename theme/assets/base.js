/* VILLUMINATION 3D — core store interactions (vanilla JS, no dependencies) */
(function () {
  'use strict';
  var T = window.theme || {};
  var routes = T.routes || {};
  var settings = T.settings || {};
  var strings = T.strings || {};

  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }

  var currencyCode = ((settings.moneyFormat || '').match(/[A-Z]{3}/) || ['USD'])[0];
  function money(cents) {
    try { return (cents / 100).toLocaleString(undefined, { style: 'currency', currency: currencyCode }); }
    catch (e) { return '$' + (cents / 100).toFixed(2); }
  }

  /* ---------- Splash intro ---------- */
  (function () {
    var splash = $('[data-splash]');
    if (!splash) return;
    var enter = $('#splash-enter');
    var once = settings.splashOnce;
    if (once && sessionStorage.getItem('v99_intro_seen')) { splash.style.display = 'none'; return; }
    document.body.style.overflow = 'hidden';
    var done = false;
    function dismiss() {
      if (done) return; done = true;
      splash.classList.add('dismissed');
      document.body.style.overflow = '';
      if (once) sessionStorage.setItem('v99_intro_seen', '1');
      setTimeout(function () { splash.style.display = 'none'; }, 900);
    }
    if (enter) enter.addEventListener('click', dismiss);
    // Fail-safes so the intro can never trap the page:
    splash.addEventListener('click', function (e) { if (e.target === splash || e.target.classList.contains('splash-bg')) dismiss(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') dismiss(); });
    setTimeout(dismiss, 16000);
  })();

  /* ---------- Navbar scroll ---------- */
  var navbar = $('.navbar');
  if (navbar) {
    var onScroll = function () { navbar.classList.toggle('scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Mobile menu ---------- */
  (function () {
    var toggle = $('.mobile-toggle');
    var menu = $('#mobile-menu');
    if (!toggle || !menu) return;
    function open() { menu.classList.add('open'); document.body.style.overflow = 'hidden'; toggle.setAttribute('aria-expanded', 'true'); }
    function close() { menu.classList.remove('open'); document.body.style.overflow = ''; toggle.setAttribute('aria-expanded', 'false'); }
    toggle.addEventListener('click', open);
    $all('[data-mobile-close]', menu).forEach(function (b) { b.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  })();

  /* ---------- Cart drawer ---------- */
  var drawer = $('#cart-drawer');
  function openDrawer() { if (!drawer) return; drawer.classList.add('open'); drawer.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; }
  function closeDrawer() { if (!drawer) return; drawer.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; }

  function updateCartCount(n) {
    $all('[data-cart-count]').forEach(function (el) {
      el.textContent = n;
      if (n > 0) { el.removeAttribute('hidden'); } else { el.setAttribute('hidden', ''); }
    });
  }

  function cartAdd(id, qty) {
    return fetch(routes.cartAdd, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ id: id, quantity: qty || 1 })
    }).then(function (r) { return r.json(); });
  }

  function cartChange(key, qty) {
    return fetch(routes.cartChange, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ id: key, quantity: qty })
    }).then(function (r) { return r.json(); });
  }

  function imgAt(src, size) {
    if (!src) return '';
    return src.replace(/(\.(?:jpg|jpeg|png|webp|gif))(\?.*)?$/i, '_' + size + '$1$2');
  }

  function syncDrawer() {
    var body = $('[data-cart-drawer-body]');
    return fetch(routes.cart + '.js').then(function (r) { return r.json(); }).then(function (cart) {
      updateCartCount(cart.item_count);
      if (!body) return cart;
      if (cart.item_count === 0) {
        body.innerHTML = '<div class="cart-drawer-empty"><p>' + (strings.cartEmpty || 'Tu carrito está vacío') + '</p>' +
          '<a href="' + routes.cart + '" class="btn btn-outline" data-cart-drawer-close>' + (strings.shop || 'Tienda') + '</a></div>';
        return cart;
      }
      var html = '<ul class="cart-drawer-items" role="list">';
      cart.items.forEach(function (item) {
        html += '<li class="cart-drawer-item" data-key="' + item.key + '">' +
          '<a href="' + item.url + '" class="cart-drawer-item-media">' +
          (item.image ? '<img src="' + imgAt(item.image, '160x') + '" alt="" width="72" height="72" loading="lazy">' : '') + '</a>' +
          '<div class="cart-drawer-item-info"><a href="' + item.url + '" class="cart-drawer-item-title">' + item.product_title + '</a>' +
          '<div class="cart-drawer-qty" data-qty><button type="button" data-qty-down aria-label="-">−</button>' +
          '<input type="number" value="' + item.quantity + '" min="0" data-qty-input data-key="' + item.key + '">' +
          '<button type="button" data-qty-up aria-label="+">+</button></div></div>' +
          '<div class="cart-drawer-item-right"><span class="cart-drawer-item-price">' + money(item.final_line_price) + '</span>' +
          '<button type="button" class="cart-drawer-item-remove" data-key="' + item.key + '" aria-label="remove">✕</button></div></li>';
      });
      html += '</ul><div class="cart-drawer-foot"><div class="cart-drawer-subtotal"><span>' + (strings.subtotal || 'Subtotal') + '</span>' +
        '<span class="cart-drawer-subtotal-amount">' + money(cart.total_price) + '</span></div>' +
        '<form action="' + routes.cart + '" method="post"><button type="submit" name="checkout" class="btn btn-primary btn-block">' + (strings.checkout || 'Finalizar compra') + '</button></form>' +
        '<a href="' + routes.cart + '" class="cart-drawer-viewcart">' + (strings.viewCart || 'Ver carrito completo') + '</a></div>';
      body.innerHTML = html;
      return cart;
    });
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cart-drawer-open]') && settings.cartType === 'drawer') { e.preventDefault(); openDrawer(); return; }
    if (e.target.closest('[data-cart-drawer-close]')) { closeDrawer(); return; }

    var remove = e.target.closest('.cart-drawer-item-remove');
    if (remove) { e.preventDefault(); cartChange(remove.getAttribute('data-key'), 0).then(syncDrawer); return; }

    var qUp = e.target.closest('[data-qty-up]');
    var qDown = e.target.closest('[data-qty-down]');
    if (qUp || qDown) {
      var wrap = (qUp || qDown).closest('[data-qty]');
      var input = $('[data-qty-input]', wrap);
      if (!input) return;
      var val = parseInt(input.value, 10) || 0;
      val = qUp ? val + 1 : Math.max(parseInt(input.min || '0', 10), val - 1);
      input.value = val;
      var key = input.getAttribute('data-key');
      if (key) { cartChange(key, val).then(syncDrawer); }
      return;
    }

    if (e.target.closest('[data-scroll-top]')) { window.scrollTo({ top: 0, behavior: 'smooth' }); return; }
  });

  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });

  // Live qty typing in drawer
  document.addEventListener('change', function (e) {
    var input = e.target.closest('[data-cart-drawer-body] [data-qty-input]');
    if (input && input.getAttribute('data-key')) {
      cartChange(input.getAttribute('data-key'), Math.max(0, parseInt(input.value, 10) || 0)).then(syncDrawer);
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
    }).catch(function () { if (btn) btn.classList.remove('is-loading'); });
  });

  /* ---------- Product page ---------- */
  (function () {
    var section = $('.product-page');
    if (!section) return;
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

    function selectedOptions() { return $all('[data-option-selector]:checked', section).map(function (i) { return i.value; }); }
    function matchVariant() {
      var opts = selectedOptions();
      if (!opts.length) return variants[0];
      return variants.find(function (v) { return opts.every(function (o, i) { return v.options[i] === o; }); });
    }
    function update() {
      var v = matchVariant();
      if (!v) return;
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
        var q = v.inventory_quantity, managed = v.inventory_management != null && v.inventory_management !== '';
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
      try {
        var url = new URL(window.location);
        url.searchParams.set('variant', v.id);
        window.history.replaceState({}, '', url);
      } catch (e) {}
    }
    $all('[data-option-selector]', section).forEach(function (i) { i.addEventListener('change', update); });

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
        var qtyEl = pform.querySelector('[name="quantity"]');
        var qty = parseInt(qtyEl ? qtyEl.value : '1', 10) || 1;
        if (addBtn) addBtn.classList.add('is-loading');
        cartAdd(id, qty).then(function () {
          if (addBtn) addBtn.classList.remove('is-loading');
          if (settings.cartType === 'drawer') { syncDrawer().then(openDrawer); }
          else { window.location.href = routes.cart; }
        }).catch(function () { if (addBtn) addBtn.classList.remove('is-loading'); });
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
  })();

  /* ---------- Collection sort auto-submit ---------- */
  $all('[data-collection-sort] select').forEach(function (sel) {
    sel.addEventListener('change', function () {
      var url = new URL(window.location);
      url.searchParams.set('sort_by', sel.value);
      url.searchParams.delete('page');
      window.location.href = url.toString();
    });
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
        try { localStorage.setItem('v99_lang_choice', sel.value); } catch (e) {}
        form.submit();
      });
    }
    // Auto-detect (browser language) only once, never overriding a manual choice.
    if (!settings.autoLang || !form || !sel) return;
    try {
      if (localStorage.getItem('v99_lang_choice') || sessionStorage.getItem('v99_lang_auto')) return;
      sessionStorage.setItem('v99_lang_auto', '1');
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
  (function () {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    $all('[data-carousel]').forEach(function (root) {
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
  })();

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
  (function () {
    var els = $all('[data-countup]');
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
  })();

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
  (function () {
    var wrap = $('[data-quotes]');
    if (!wrap) return;
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
  })();

  /* ---------- Hero rotating words ---------- */
  (function () {
    var el = $('[data-typed]');
    if (!el) return;
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
  })();

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
  })();

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
      box.addEventListener('click', function (e) { if (e.target === box || e.target.classList.contains('img-lightbox-close')) close(); });
      document.body.appendChild(box);
    }
    function open(src, alt) {
      if (!box) build();
      boxImg.src = src; boxImg.alt = alt || '';
      requestAnimationFrame(function () { box.classList.add('is-open'); });
      document.documentElement.style.overflow = 'hidden';
    }
    function close() {
      if (!box) return;
      box.classList.remove('is-open');
      document.documentElement.style.overflow = '';
    }
    zoomables.forEach(function (img) {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function () { open(img.getAttribute('data-zoom-src') || img.currentSrc || img.src, img.alt); });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  })();

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
    var host = $('[data-recently-viewed]');
    if (!host) return;
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
  })();

  /* ---------- Copy coupon code ---------- */
  $all('[data-copy-code]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var code = btn.getAttribute('data-code') || '';
      var done = function () {
        btn.classList.add('copied');
        var hint = btn.querySelector('.nl-code-hint');
        if (hint) { var prev = hint.textContent; hint.textContent = '¡Copiado!'; setTimeout(function () { hint.textContent = prev; btn.classList.remove('copied'); }, 1600); }
      };
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(code).then(done).catch(done); }
      else { var t = document.createElement('textarea'); t.value = code; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(t); done(); }
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
