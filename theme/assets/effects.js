/* VILLUMINATION 3D — visual effects layer.
   Lightweight, dependency-free, and disabled automatically when the visitor
   prefers reduced motion. Everything here is progressive enhancement. */
(function () {
  'use strict';
  var T = window.theme || {};
  var settings = T.settings || {};
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  var hex = function (c, fallback) { return (c && /^#/.test(c)) ? c : fallback; };
  var CYAN = hex(getComputedStyle(document.documentElement).getPropertyValue('--neon-cyan').trim(), '#00d4ff');
  var PINK = hex(getComputedStyle(document.documentElement).getPropertyValue('--neon-pink').trim(), '#ff2ecb');
  var GREEN = hex(getComputedStyle(document.documentElement).getPropertyValue('--neon-green').trim(), '#00e87b');

  /* ============ 1. Scroll reveal (fail-safe: content can NEVER stay hidden) ============ */
  (function () {
    var els = $all('[data-reveal]');
    if (!els.length) return;
    function showAll() { els.forEach(function (el) { el.classList.add('is-visible'); el.classList.remove('reveal-init'); }); }
    // If reveal is off, reduced motion, or no observer support → just show everything.
    if (!settings.scrollReveal || reduce || !('IntersectionObserver' in window)) { showAll(); return; }
    var vh = window.innerHeight || 800;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); } });
    }, { threshold: 0, rootMargin: '0px 0px -4% 0px' });
    els.forEach(function (el) {
      var rect = el.getBoundingClientRect();
      // Never hide anything already on screen or taller than the viewport (that is
      // what turned long pages black — the ratio threshold could never be met).
      if (rect.top < vh || rect.height > vh * 0.85) { el.classList.add('is-visible'); return; }
      el.classList.add('reveal-init');
      io.observe(el);
    });
    // Absolute safety net — reveal any stragglers a moment after load.
    setTimeout(showAll, 2500);
    window.addEventListener('load', function () { setTimeout(showAll, 300); });
  })();

  /* ============ 2. Parallax ============ */
  (function () {
    if (!settings.parallax || reduce) return;
    var els = $all('[data-parallax-speed]');
    if (!els.length) return;
    var ticking = false;
    function apply() {
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > vh) return;
        var speed = parseFloat(el.getAttribute('data-parallax-speed')) || 0.3;
        var offset = (rect.top - vh / 2) * speed * -0.4;
        el.style.transform = 'translate3d(0,' + offset.toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(apply); } }, { passive: true });
    apply();
  })();

  /* ============ 3. Card tilt (3D hover) ============ */
  (function () {
    if (!settings.cardTilt || reduce || window.matchMedia('(hover: none)').matches) return;
    $all('.js-tilt').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(700px) rotateY(' + (px * 7).toFixed(2) + 'deg) rotateX(' + (-py * 7).toFixed(2) + 'deg) translateZ(0)';
      });
      card.addEventListener('pointerleave', function () { card.style.transform = ''; });
    });
  })();

  /* ============ 4. Seasonal floating effects ============ */
  (function () {
    var kind = settings.seasonalEffect;
    if (!kind || kind === 'none' || reduce) return;
    var canvas = document.createElement('canvas');
    canvas.className = 'fx-seasonal-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var W, H, DPR = Math.min(window.devicePixelRatio || 1, 2);
    var count = Math.max(10, Math.min(120, settings.seasonalDensity || 50));
    var parts = [];
    var palette = [CYAN, PINK, GREEN, '#ffd000'];

    function resize() { W = canvas.width = innerWidth * DPR; H = canvas.height = innerHeight * DPR; canvas.style.width = innerWidth + 'px'; canvas.style.height = innerHeight + 'px'; }
    function rnd(a, b) { return a + Math.random() * (b - a); }
    function spawn() {
      return { x: rnd(0, W), y: rnd(-H, 0), r: rnd(3, 9) * DPR, vy: rnd(0.4, 1.6) * DPR, vx: rnd(-0.4, 0.4) * DPR, sway: rnd(0, 6.28), rot: rnd(0, 6.28), vr: rnd(-0.04, 0.04), color: palette[(Math.random() * palette.length) | 0] };
    }
    function heart(p) {
      ctx.beginPath();
      var s = p.r / 8;
      ctx.moveTo(p.x, p.y);
      ctx.bezierCurveTo(p.x - 5 * s, p.y - 4 * s, p.x - 8 * s, p.y + 2 * s, p.x, p.y + 7 * s);
      ctx.bezierCurveTo(p.x + 8 * s, p.y + 2 * s, p.x + 5 * s, p.y - 4 * s, p.x, p.y);
      ctx.fill();
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        p.y += p.vy; p.x += p.vx + Math.sin(p.sway) * 0.5 * DPR; p.sway += 0.02; p.rot += p.vr;
        if (p.y > H + 20) { parts[i] = spawn(); parts[i].y = -10; continue; }
        ctx.save(); ctx.globalAlpha = 0.85;
        if (kind === 'snow') { ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * 0.5, 0, 6.28); ctx.fill(); }
        else if (kind === 'hearts') { ctx.fillStyle = p.color; heart(p); }
        else if (kind === 'sparks') { ctx.fillStyle = p.color; ctx.shadowBlur = 8; ctx.shadowColor = p.color; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * 0.4, 0, 6.28); ctx.fill(); }
        else { ctx.translate(p.x, p.y); ctx.rotate(p.rot); ctx.fillStyle = p.color; ctx.fillRect(-p.r * 0.5, -p.r * 0.25, p.r, p.r * 0.5); } /* confetti */
        ctx.restore();
      }
      raf = requestAnimationFrame(draw);
    }
    var raf;
    function start() { resize(); parts = []; for (var i = 0; i < count; i++) parts.push(spawn()); cancelAnimationFrame(raf); draw(); }
    window.addEventListener('resize', function () { clearTimeout(canvas._t); canvas._t = setTimeout(start, 200); });
    // Pause when tab hidden to save CPU
    document.addEventListener('visibilitychange', function () { if (document.hidden) { cancelAnimationFrame(raf); } else { draw(); } });
    start();
  })();

  /* ============ 4b. Holo stage: pointer-driven 3D tilt (product showcase) ============ */
  (function () {
    var stages = $all('[data-tilt-3d]');
    if (!stages.length) return;
    var noHover = window.matchMedia('(hover: none)').matches;
    stages.forEach(function (stage) {
      var obj = $('.holo-obj', stage);
      if (!obj) return;
      if (reduce || noHover) { obj.classList.add('holo-auto'); return; } // fallback: gentle auto-rotation
      stage.addEventListener('pointermove', function (e) {
        var r = stage.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        obj.style.transform = 'rotateY(' + (px * 26).toFixed(2) + 'deg) rotateX(' + (-py * 14).toFixed(2) + 'deg)';
      });
      stage.addEventListener('pointerleave', function () { obj.style.transform = ''; obj.classList.add('holo-auto'); });
      stage.addEventListener('pointerenter', function () { obj.classList.remove('holo-auto'); });
      obj.classList.add('holo-auto');
    });
  })();

  /* ============ 4c. Ambient futuristic background (aurora + drifting particles) ============
     Fondo negro intacto: pinta detrás del contenido (z-index -1), 30 fps,
     se pausa con la pestaña oculta y respeta prefers-reduced-motion. */
  (function () {
    var mode = settings.ambient || 'full';
    if (mode === 'none') return;
    var canvas = document.createElement('canvas');
    canvas.className = 'fx-ambient-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var DPR = 1; // fondo difuso: resolución nativa baja = más rápido
    var W, H;
    function resize() { W = canvas.width = innerWidth; H = canvas.height = innerHeight; }
    resize();
    window.addEventListener('resize', function () { clearTimeout(canvas._t); canvas._t = setTimeout(resize, 250); });

    var ORBS = [
      { x: 0.18, y: 0.25, r: 0.42, c: '0,212,255',  s: 0.00016, ph: 0 },
      { x: 0.82, y: 0.65, r: 0.48, c: '255,46,203', s: 0.00013, ph: 2.1 },
      { x: 0.50, y: 0.90, r: 0.38, c: '123,47,255', s: 0.00019, ph: 4.2 }
    ];
    var parts = [];
    var N = Math.min(38, Math.floor(innerWidth / 34));
    function rnd(a, b) { return a + Math.random() * (b - a); }
    for (var i = 0; i < N; i++) {
      parts.push({ x: rnd(0, 1), y: rnd(0, 1), v: rnd(0.00006, 0.00022), r: rnd(0.7, 1.9), a: rnd(0.12, 0.4),
                   c: ['0,212,255', '255,46,203', '0,232,123'][i % 3], tw: rnd(0, 6.28) });
    }

    function drawFrame(t) {
      ctx.clearRect(0, 0, W, H);
      if (mode !== 'particles') {
        for (var o = 0; o < ORBS.length; o++) {
          var b = ORBS[o];
          var ox = (b.x + Math.sin(t * b.s + b.ph) * 0.08) * W;
          var oy = (b.y + Math.cos(t * b.s * 1.3 + b.ph) * 0.06) * H;
          var rad = b.r * Math.max(W, H);
          var g = ctx.createRadialGradient(ox, oy, 0, ox, oy, rad);
          g.addColorStop(0, 'rgba(' + b.c + ',0.05)');
          g.addColorStop(1, 'rgba(' + b.c + ',0)');
          ctx.fillStyle = g;
          ctx.fillRect(0, 0, W, H);
        }
      }
      if (mode !== 'aurora') {
        for (var p = 0; p < parts.length; p++) {
          var q = parts[p];
          q.y -= q.v; q.tw += 0.02;
          if (q.y < -0.02) { q.y = 1.02; q.x = Math.random(); }
          var al = q.a * (0.6 + 0.4 * Math.sin(q.tw));
          ctx.fillStyle = 'rgba(' + q.c + ',' + al.toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(q.x * W, q.y * H, q.r, 0, 6.2832); ctx.fill();
        }
      }
    }

    if (reduce) { drawFrame(0); return; } // estático con reduced-motion
    var last = 0, raf;
    function loop(t) {
      raf = requestAnimationFrame(loop);
      if (t - last < 33) return; // ~30 fps
      last = t;
      drawFrame(t);
    }
    raf = requestAnimationFrame(loop);
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) { cancelAnimationFrame(raf); } else { raf = requestAnimationFrame(loop); }
    });
  })();

  /* ============ 5. Interactive 3D splash (magnetic particle field) ============
     Renders into #splash-canvas. Pointer / touch "pulls" the neon particles
     like magnets. Pure 2D canvas — no WebGL library, ~2KB runtime. */
  (function () {
    var canvas = $('#splash-canvas');
    var splash = $('[data-splash-3d]');
    if (!canvas || !splash || reduce) return;
    var ctx = canvas.getContext('2d');
    var DPR = Math.min(window.devicePixelRatio || 1, 2);
    var W, H, pts = [], pointer = { x: -9999, y: -9999, active: false };
    var palette = [CYAN, PINK, GREEN];
    var N = window.innerWidth < 700 ? 46 : 90;

    function resize() { W = canvas.width = innerWidth * DPR; H = canvas.height = innerHeight * DPR; canvas.style.width = innerWidth + 'px'; canvas.style.height = innerHeight + 'px'; }
    function build() {
      pts = [];
      for (var i = 0; i < N; i++) {
        pts.push({ x: Math.random() * W, y: Math.random() * H, hx: Math.random() * W, hy: Math.random() * H, vx: 0, vy: 0, r: (Math.random() * 2 + 1) * DPR, c: palette[i % palette.length] });
      }
    }
    function move(e) {
      var t = e.touches ? e.touches[0] : e;
      pointer.x = t.clientX * DPR; pointer.y = t.clientY * DPR; pointer.active = true;
    }
    function leave() { pointer.active = false; pointer.x = -9999; pointer.y = -9999; }

    var raf;
    function frame() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        // spring back to home
        p.vx += (p.hx - p.x) * 0.005;
        p.vy += (p.hy - p.y) * 0.005;
        if (pointer.active) {
          var dx = p.x - pointer.x, dy = p.y - pointer.y;
          var d2 = dx * dx + dy * dy;
          var radius = (170 * DPR) * (170 * DPR);
          if (d2 < radius && d2 > 1) {
            var f = (1 - d2 / radius) * 2.4; // magnetic pull toward pointer
            p.vx -= (dx / Math.sqrt(d2)) * f;
            p.vy -= (dy / Math.sqrt(d2)) * f;
          }
        }
        p.vx *= 0.9; p.vy *= 0.9;
        p.x += p.vx; p.y += p.vy;
        // links
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j], lx = p.x - q.x, ly = p.y - q.y, ld = lx * lx + ly * ly;
          if (ld < (110 * DPR) * (110 * DPR)) {
            ctx.strokeStyle = p.c; ctx.globalAlpha = 0.12 * (1 - ld / ((110 * DPR) * (110 * DPR)));
            ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
          }
        }
        ctx.globalAlpha = 0.9; ctx.fillStyle = p.c; ctx.shadowBlur = 6; ctx.shadowColor = p.c;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.28); ctx.fill(); ctx.shadowBlur = 0;
      }
      ctx.globalAlpha = 1;
      raf = requestAnimationFrame(frame);
    }
    function init() { resize(); build(); cancelAnimationFrame(raf); frame(); }
    window.addEventListener('resize', function () { clearTimeout(canvas._t); canvas._t = setTimeout(init, 200); });
    splash.addEventListener('pointermove', move);
    splash.addEventListener('touchmove', move, { passive: true });
    splash.addEventListener('pointerleave', leave);
    splash.addEventListener('touchend', leave);
    init();
    // stop the loop once the splash is dismissed
    var mo = new MutationObserver(function () {
      if (splash.classList.contains('dismissed')) { cancelAnimationFrame(raf); mo.disconnect(); }
    });
    mo.observe(splash, { attributes: true, attributeFilter: ['class'] });
  })();
})();
