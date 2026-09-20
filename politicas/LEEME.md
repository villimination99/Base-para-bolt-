# Las politicas de VILLUMINATIONS

Los tres archivos `.txt` de esta carpeta son la **fuente**: el texto exacto que
va pegado en Shopify -> Configuracion -> Politicas. Si se cambia el texto, se
cambia aqui primero y se vuelve a pegar; nunca al reves.

| Archivo | Donde se pega |
| --- | --- |
| `informacion-de-contacto.txt` | Informacion de contacto |
| `aviso-legal.txt` | Aviso legal |
| `condiciones-del-servicio.txt` | Condiciones del servicio |

Faltan tres a proposito: **reembolso**, **privacidad** y **envio** ya estaban
correctas en la tienda y no se tocan.

## Por que existe la compuerta

En una entrega anterior el texto salio con dos marcadores mios sin sustituir
—`‹NEQ, o: no aplica›` y `‹TPS/TVQ, o: no aplica›`— y se publicaron tal cual en
la tienda, en dos documentos. El fallo no fue de quien los pego: fue de quien
los escribio y no los reviso.

`comprobar.mjs` es la respuesta a eso. Antes de entregar nada:

    node politicas/comprobar.mjs

Falla si queda un marcador, un corchete de plantilla, una variable sin
sustituir, una entidad HTML, un espacio al final de linea; si falta la
direccion completa, el correo o el telefono; si reaparece la plataforma europea
de litigios (apagada el 20 de julio de 2025) o el nombre viejo de la tienda; o
si las condiciones no traen sus 25 secciones enteras y en orden.

## Datos que usan los tres textos

- VILLUMINATIONS
- 183 Rue Edouard-Rousseau, Granby (Quebec) J2H 0A6, Canada
- +1 450 558-7463
- villumination@outlook.com

La direccion sale de la que la tienda tiene registrada en Shopify, no de una
suposicion.

## Lo que falta

Las lineas de **NEQ** y de **TPS/TVQ** estan quitadas, no vacias. En Quebec,
quien trabaja por cuenta propia bajo un nombre comercial que no es su nombre y
apellido tiene que inscribirse en el Registraire des entreprises y recibe un
NEQ; la inscripcion a la TPS/TVQ solo es obligatoria al pasar de 30 000 $ de
ventas en cuatro trimestres. Cuando esos numeros existan, se anaden aqui y se
vuelve a pegar. Un hueco, nunca.

## Traducciones

Las seis politicas estan registradas en **ingles, frances, aleman y japones**
(24 traducciones, key `body`, via `translationsRegister`). Todas se leyeron de
vuelta desde la tienda con `outdated: false`.

Importante: el digest de Shopify se calcula sobre el texto ESPANOL. Si se
cambia una sola letra del espanol, las cuatro traducciones de esa politica
quedan marcadas como `outdated` y hay que volver a registrarlas. Por eso el
orden es siempre: primero el espanol definitivo, despues las traducciones.

En ingles las comillas son "...", en aleman „...", en frances « ... » y en
japones 「...」. El espanol usa «...». No se copian las comillas de un idioma a
otro: es el fallo que hubo que corregir en ingles y aleman.
