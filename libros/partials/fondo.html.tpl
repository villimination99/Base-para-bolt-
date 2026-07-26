<meta charset="utf-8">
<link rel="stylesheet" href="__ASSETS__/libro.css">
<style>
  @page{ size:148mm 210mm; margin:0 }
  html,body{ background:#050510 !important; }
  body{ width:148mm; height:210mm; margin:0; position:relative; overflow:hidden; }
  /* Textura de marca: rejilla técnica + halos de acento en las esquinas */
  .rejilla{
    position:absolute; inset:0;
    background-image:
      linear-gradient(rgba(0,180,255,.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,180,255,.035) 1px, transparent 1px);
    background-size:9mm 9mm;
  }
  .halo{
    position:absolute; inset:0;
    background:
      radial-gradient(70% 45% at 8% 0%,   rgba(var(--a-rgb),.13) 0%, transparent 62%),
      radial-gradient(60% 40% at 100% 100%, rgba(var(--a-rgb),.10) 0%, transparent 62%);
  }
  .filo{
    position:absolute; left:0; top:0; bottom:0; width:1.9mm;
    background:linear-gradient(180deg, var(--acento), var(--acento-2) 65%, transparent);
    opacity:.9;
  }
</style>
<body class="acento-__ACENTO__">
  <div class="rejilla"></div>
  <div class="halo"></div>
  <div class="filo"></div>
</body>
