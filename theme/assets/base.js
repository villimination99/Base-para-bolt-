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
    setTimeout(dismiss, 12000);
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
    var priceEl = $('[data-price]', section);
    var compareEl = $('[data-compare]', section);
    var addBtn = $('[data-add-btn]', section);
    var addText = $('[data-add-text]', section);

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
      if (priceEl) priceEl.textContent = money(v.price);
      if (compareEl) {
        if (v.compare_at_price > v.price) { compareEl.textContent = money(v.compare_at_price); compareEl.style.display = ''; }
        else { compareEl.style.display = 'none'; }
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
})();
