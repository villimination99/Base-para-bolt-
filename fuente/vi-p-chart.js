/* Chart.js recortado a lo que el hub usa de verdad.
   ------------------------------------------------------------------
   El paquete completo trae treinta y tantos tipos de grafica. VI.P dibuja
   dos: el anillo de macros (doughnut) y las barras de progreso semanal.
   Importar solo esas piezas deja fuera lineas, radares, burbujas, dispersion,
   sus escalas y sus animaciones asociadas.

   Se expone en window.Chart porque vi-p.js es un script clasico que hace
   "new Chart(...)", igual que hacia con la version del CDN. Para el hub no
   cambia nada; simplemente ya no sale a internet a buscarla.
*/
import {
  Chart,
  ArcElement, BarElement,
  DoughnutController, BarController,
  CategoryScale, LinearScale,
  Tooltip, Legend
} from 'chart.js';

Chart.register(
  ArcElement, BarElement,
  DoughnutController, BarController,
  CategoryScale, LinearScale,
  Tooltip, Legend
);

window.Chart = Chart;
