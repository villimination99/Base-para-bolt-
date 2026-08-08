---
tags:
  - memoria
  - indice
actualizado: 2026-08-08
---

# VILLUMINATIONS — estado del proyecto

Nota escrita a mano, no generada. Las otras 1277 notas de esta bóveda salen del
grafo de `graphify` y se regeneran solas; esta no. Es la memoria: lo que hay que
saber antes de tocar nada, y lo que quedó a medias.

## Qué es esto

Una tienda Shopify —**villuminations.com**, CAD, plan Basic, Canadá— que vende
material propio en PDF y mercancía de proveedor. Cuarenta productos: once
propios y veintinueve de reventa.

Lo propio son **once documentos** que viven en este repositorio y se generan,
no se editan a mano:

- **Ocho libros** (`libros/`): Mesa, Carga, Descanso, Voluntad, Arcanos, Sí
  Mismo, Zodiacal e Invocaciones. Cada uno en español, inglés y francés. 24 PDF.
- **Tres niveles de planes** (`planes/`): Básico (1 documento), Pro (5) y Elite
  (11), también en tres lenguas. 66 PDF.

## Reglas que no se negocian

Están aquí porque se han roto antes y cuesta caro repararlas.

**La marca se escribe `VILLUMINATIONS`.** Ni «VILLUMINATIONS 99», ni
«VIllumination», ni «Ma boutique», que es lo que Shopify pone por defecto en
francés. Los tres aparecieron en la tienda a la vez y un comprador veía tres
vendedores distintos según qué ficha mirase.

**Todo el contenido es obra original y sin dueño ajeno.** Dos bases legales
distintas, y no se pueden mezclar:

- Los datos de nutrición y entrenamiento salen de organismos del Gobierno de
  los Estados Unidos y **no están sujetos a derechos de autor conforme al
  17 U.S.C. § 105**. Eso cubre las cifras, no la redacción.
- Los libros esotéricos se apoyan en la **tradición común y el dominio
  público**: la secuencia de los arcanos, las correspondencias clásicas, los
  ejercicios de examen de conciencia. Esa es otra cosa y hay que decirla como
  tal. Confundir las dos es un error jurídico, no de estilo.

No se le quita la firma a nadie.

**Cada producto se explica solo.** Una ficha no nombra ni describe lo que
contienen las demás: el catálogo se descubre comprando, no leyendo. La única
excepción es que cada nivel enumera sus propios documentos, y Elite dice que es
acumulativo porque lo es por definición.

**Rama de trabajo: `claude/shopify-diet-plans-9k0wti`.** No se empuja a otra sin
permiso. PR abierto: el #2.

## Cómo está montado

La localización tiene una regla que gobierna todo lo demás: **el marcado vive
una vez y las traducciones son datos**. Cada segmento se indexa por el SHA1 de
su original castellano normalizado. Por debajo del 100 % de cobertura el PDF no
se escribe: sale `Incompleto` y no hay libro. Eso es deliberado — es preferible
un libro que no existe a uno que aparece medio traducido.

Hay guardas que abortan la construcción, y conviene no desactivarlas:

- **Ancho de lámina** (`cargar-traducciones.py`): una etiqueta traducida que no
  cabe en su hueco rompe el dibujo, así que se rechaza antes.
- **Cuenta de láminas** (`comprobar_laminas` en `build.py`): si la prosa promete
  «siete láminas» y solo hay seis dibujadas, el libro no se publica. Se añadió
  porque tres libros mentían en tres idiomas a la vez.
- **Etiquetas cortas**: las fases lunares no pasan de 9 caracteres, la
  melotesia de columnas de 124 unidades.

Números duros: **5027 segmentos** traducidos al inglés y al francés, **90 PDF**
en 5 paquetes, 0 problemas de auditoría.

## Lo que falta

Por orden de urgencia real:

1. **No hay app de descargas digitales.** Los once productos digitales están
   publicados y cobran, y el comprador no recibe nada. Es lo único que separa
   esto de una tienda que funciona. Se instala desde el panel; no se puede hacer
   por API.
2. **Los 29 productos de proveedor no tienen traducción.** La tienda va en tres
   lenguas para lo propio y solo en castellano para el resto.
3. **Precio provisional de 9,99 CAD** en los seis libros nuevos, puesto para que
   no quedaran a cero estando publicados. Los decide el dueño.
4. **Los dos jabones** están en UNLISTED y sin colección. Si se quieren vender
   hacen falta las dos cosas.

## Fiabilidad de esta bóveda

El grafo del que sale tiene **1042 nodos y 1487 aristas**, y su diagnóstico
avisa de **116 aristas que apuntan a nodos inexistentes** — identificadores que
la extracción semántica inventó y que no casan con los del análisis del código.
Las notas correspondientes tendrán enlaces rotos. No es un fallo del contenido,
pero conviene saberlo antes de fiarse de un enlace concreto.

Para regenerarla: `/graphify .` desde la raíz, y luego `graphify export obsidian`.
