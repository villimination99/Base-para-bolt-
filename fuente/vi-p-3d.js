import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { MarchingCubes } from 'three/addons/objects/MarchingCubes.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

try {
  const canvas = document.getElementById('muscle-canvas');
  const loading = document.getElementById('mm-loading');

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x0b0d16, 0.10);
  const camera = new THREE.PerspectiveCamera(33, canvas.clientWidth / canvas.clientHeight, 0.1, 100);

  /* ENCUADRAR ES CUENTA, NO GUSTO. Antes la distancia era un 3.7 fijo y el
     lienzo cambia de forma segun el aparato: en un movil el cuerpo llenaba la
     caja y en un escritorio ancho se quedaba en una figurita de 16 % del ancho
     perdida en un rectangulo negro. Aqui la distancia sale de la altura que se
     quiere llenar y del campo de vision, y ademas se compara con lo que cabe
     de ANCHO, que es lo que manda en un lienzo apaisado. */
  const CUERPO_ALTO = 1.86, CUERPO_ANCHO = 0.62;
  function distanciaParaEncuadrar(llenado) {
    const fv = camera.fov * Math.PI / 180;
    const dV = (CUERPO_ALTO / llenado) / (2 * Math.tan(fv / 2));
    const fh = 2 * Math.atan(Math.tan(fv / 2) * camera.aspect);
    const dH = (CUERPO_ANCHO / llenado) / (2 * Math.tan(fh / 2));
    return Math.max(dV, dH);
  }
  /* La misma cuenta, encuadrando UNA ALTURA EN METROS en vez de una fraccion
     del cuerpo. Es lo que usa el foco de cada musculo. */
  function distanciaParaEncuadrarAlto(alto) {
    const fv = camera.fov * Math.PI / 180;
    const dV = alto / (2 * Math.tan(fv / 2));
    const fh = 2 * Math.atan(Math.tan(fv / 2) * camera.aspect);
    const dH = (alto * 0.62) / (2 * Math.tan(fh / 2));   // un musculo es mas alto que ancho
    return Math.max(dV, dH);
  }
  let distBase = distanciaParaEncuadrar(0.88);
  camera.position.set(0.42, 1.16, distBase);

  const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  window.__mm3dStarted = true;

  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(renderer), 0.04).texture;

  /* ---- Luces de estudio con rim azul ---- */
  scene.add(new THREE.HemisphereLight(0x35507a, 0x0a0a12, 0.35));
  const keyLight = new THREE.DirectionalLight(0xfff4e8, 1.05);
  keyLight.position.set(2.4, 3.4, 3.2);
  keyLight.castShadow = true;
  keyLight.shadow.mapSize.set(1024, 1024);
  keyLight.shadow.camera.near = 0.5; keyLight.shadow.camera.far = 12;
  keyLight.shadow.camera.left = -2; keyLight.shadow.camera.right = 2;
  keyLight.shadow.camera.top = 3.2; keyLight.shadow.camera.bottom = -1;
  scene.add(keyLight);
  const rimL = new THREE.DirectionalLight(0x2f6bff, 1.9);
  rimL.position.set(-3.4, 1.7, -2.0);
  scene.add(rimL);
  const rimR = new THREE.DirectionalLight(0x1e4dff, 1.3);
  rimR.position.set(3.2, 0.9, -2.6);
  scene.add(rimR);
  const fillCyan = new THREE.PointLight(0x05D9E8, 0.3, 8);
  fillCyan.position.set(0, 0.5, 2.6);
  scene.add(fillCyan);
  // Rebote del suelo: sin él las piernas caen a negro y el volumen se pierde
  const bounce = new THREE.DirectionalLight(0x9fb0d4, 0.42);
  bounce.position.set(0.6, -1.8, 1.6);
  scene.add(bounce);

  /* ---- Suelo + anillo + partículas ---- */
  // Suelo invisible que SOLO recibe sombra (nada de disco gris flotando)
  const ground = new THREE.Mesh(new THREE.CircleGeometry(1.9, 64), new THREE.ShadowMaterial({ opacity: 0.45 }));
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);
  // Halo de contacto degradado (textura de canvas: 128px, coste nulo)
  const gcv = document.createElement('canvas'); gcv.width = gcv.height = 128;
  const g2d = gcv.getContext('2d');
  const grd = g2d.createRadialGradient(64, 64, 3, 64, 64, 64);
  grd.addColorStop(0, 'rgba(5,217,232,0.30)');
  grd.addColorStop(0.42, 'rgba(5,217,232,0.08)');
  grd.addColorStop(1, 'rgba(5,217,232,0)');
  g2d.fillStyle = grd; g2d.fillRect(0, 0, 128, 128);
  const glow = new THREE.Mesh(
    new THREE.PlaneGeometry(3.4, 3.4),
    new THREE.MeshBasicMaterial({ map: new THREE.CanvasTexture(gcv), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending })
  );
  glow.rotation.x = -Math.PI / 2; glow.position.y = 0.0015;
  scene.add(glow);
  const ring = new THREE.Mesh(
    new THREE.RingGeometry(1.05, 1.09, 64),
    new THREE.MeshBasicMaterial({ color: 0x05D9E8, transparent: true, opacity: 0.22, side: THREE.DoubleSide })
  );
  ring.rotation.x = -Math.PI / 2;
  ring.position.y = 0.002;
  scene.add(ring);
  const pGeo = new THREE.BufferGeometry();
  const PCOUNT = 150;
  const pPos = new Float32Array(PCOUNT * 3);
  for (let i = 0; i < PCOUNT; i++) {
    pPos[i * 3] = (Math.random() - 0.5) * 8;
    pPos[i * 3 + 1] = Math.random() * 3.4;
    pPos[i * 3 + 2] = (Math.random() - 0.5) * 8;
  }
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  const particles = new THREE.Points(pGeo, new THREE.PointsMaterial({
    color: 0x3f6bff, size: 0.02, transparent: true, opacity: 0.3, blending: THREE.AdditiveBlending
  }));
  scene.add(particles);

  /* =====================================================================
     MATERIAL "ARCILLA" con highlight EN LA SUPERFICIE
     Cada vértice lleva pesos (selW/hovW/crease); el shader pinta la zona activa
     directamente sobre el cuerpo (nada de globos flotantes).
     ===================================================================== */
  const uPulse = { value: 0 }, uScanY = { value: 0 };
  /* Sube de 0 a 1 en la entrada: el cuerpo aparece en hueso y los colores se
     encienden despues, que se lee mejor que darlo todo hecho de golpe. */
  const uPaleta = { value: 0 };
  let tPaleta0 = 0;
  // Material de lámina anatómica: mate, hueso cálido, sin barniz plástico.
  const clayMat = new THREE.MeshPhysicalMaterial({
    color: 0xd8d3ca, roughness: 0.62, metalness: 0.0,
    clearcoat: 0.05, clearcoatRoughness: 0.80, envMapIntensity: 0.50,
    sheen: 0.30, sheenRoughness: 0.85, sheenColor: new THREE.Color(0xffd9c4)
  });
  clayMat.onBeforeCompile = function(shader) {
    shader.uniforms.uPulse = uPulse;
    shader.uniforms.uScanY = uScanY;
    shader.uniforms.uPaleta = uPaleta;
    shader.vertexShader = shader.vertexShader
      .replace('#include <common>', `#include <common>
attribute float selW; attribute float hovW; attribute float clothId; attribute float crease; attribute float ao;
attribute vec3 zoneRGB; attribute float zoneW;
varying float vSelW; varying float vHovW; varying float vCloth; varying float vCre; varying float vAO; varying vec3 vLocal;
varying vec3 vZoneRGB; varying float vZoneW;`)
      .replace('#include <begin_vertex>', `#include <begin_vertex>
vSelW = selW; vHovW = hovW; vCloth = clothId; vCre = crease; vAO = ao; vLocal = position;
vZoneRGB = zoneRGB; vZoneW = zoneW;`);
    shader.fragmentShader = shader.fragmentShader
      .replace('#include <common>', `#include <common>
varying float vSelW; varying float vHovW; varying float vCloth; varying float vCre; varying float vAO; varying vec3 vLocal;
varying vec3 vZoneRGB; varying float vZoneW;
uniform float uPulse; uniform float uScanY; uniform float uPaleta;
float vhash(vec3 p){ p = fract(p * 0.3183099 + vec3(0.71, 0.113, 0.419)); p *= 17.0; return fract(p.x * p.y * p.z * (p.x + p.y + p.z)); }
float vnoise(vec3 x){ vec3 i = floor(x), f = fract(x); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(vhash(i), vhash(i + vec3(1,0,0)), f.x), mix(vhash(i + vec3(0,1,0)), vhash(i + vec3(1,1,0)), f.x), f.y),
             mix(mix(vhash(i + vec3(0,0,1)), vhash(i + vec3(1,0,1)), f.x), mix(vhash(i + vec3(0,1,1)), vhash(i + vec3(1,1,1)), f.x), f.y), f.z); }`)
      .replace('#include <color_fragment>', `#include <color_fragment>
{
  float cre = clamp(vCre, 0.0, 1.0);
  float cloth = clamp(vCloth, 0.0, 1.0);
  float sel = clamp(vSelW, 0.0, 1.0);
  float hov = clamp(vHovW, 0.0, 1.0) * (1.0 - sel);
  float occ = clamp(vAO, 0.0, 1.0);
  // Micro-relieve procedural: rompe el albedo uniforme que delata al plástico
  float grain = vnoise(vLocal * 46.0) - 0.5;
  float fiber = vnoise(vLocal * vec3(120.0, 26.0, 120.0)) - 0.5; // fibra alargada
  diffuseColor.rgb *= 1.0 + grain * 0.10 + fiber * 0.055;
  // Oclusión ambiental horneada desde el propio SDF: hunde axilas, ingles, pliegues
  diffuseColor.rgb *= mix(1.0, occ, 0.88);
  // Ropa
  diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.070, 0.070, 0.086), cloth);
  // Surco anatómico: sombra profunda + tinte frío en el fondo
  float deep = smoothstep(0.20, 1.0, cre);
  diffuseColor.rgb *= (1.0 - 0.60 * cre);
  diffuseColor.rgb = mix(diffuseColor.rgb, diffuseColor.rgb * vec3(0.80, 0.86, 1.0), deep * 0.75);
  /* LA PALETA PERMANENTE. Cada grupo lleva su color siempre puesto, para que
     el cuerpo se lea de un vistazo sin ir tocando musculo a musculo. Se apaga
     en el grupo seleccionado, para que el rojo del elegido no compita con su
     propio color, y baja a un tercio en los demas cuando hay uno elegido:
     enfocar es tanto encender uno como apagar el resto. uPulse solo late
     cuando hay seleccion, asi que sirve de senal sin otro uniforme.
     La mezcla es COMPLETA y un punto mas oscura que el color puro: con una
     mezcla parcial el color se perdia, porque la piel base es hueso claro y
     el entorno ilumina fuerte. Medido sobre la escena, no supuesto. */
  float hayElegido = step(0.01, uPulse);
  float pal = clamp(vZoneW, 0.0, 1.0) * uPaleta * (1.0 - cloth) * (1.0 - sel)
            * mix(1.0, 0.34, hayElegido);
  diffuseColor.rgb = mix(diffuseColor.rgb, vZoneRGB * 0.82, pal);
  // Músculo activo / bajo el cursor
  diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.86, 0.09, 0.11), sel * 0.90);
  diffuseColor.rgb = mix(diffuseColor.rgb, vec3(1.0, 0.55, 0.25), hov * 0.28);
}`)
      .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
{
  float sel = clamp(vSelW, 0.0, 1.0);
  float hov = clamp(vHovW, 0.0, 1.0) * (1.0 - sel);
  float cre = clamp(vCre, 0.0, 1.0);
  float occ = clamp(vAO, 0.0, 1.0);
  // Luz de borde: se apaga en las zonas ocluidas, como la luz real
  float ndv = clamp(dot(normalize(vViewPosition), normal), 0.0, 1.0);
  float fres = pow(1.0 - ndv, 3.2);
  totalEmissiveRadiance += vec3(0.03, 0.62, 0.70) * fres * (0.40 - 0.18 * cre) * occ;
  float edge = smoothstep(0.05, 0.35, sel) * (1.0 - smoothstep(0.55, 0.95, sel));
  totalEmissiveRadiance += vec3(1.0, 0.10, 0.05) * (sel * (0.18 + 0.16 * uPulse) + edge * 0.38);
  float band = smoothstep(0.085, 0.0, abs(vLocal.y - uScanY));
  totalEmissiveRadiance += vec3(1.0, 0.42, 0.30) * sel * band * 0.85;
  totalEmissiveRadiance += vec3(1.0, 0.5, 0.2) * hov * 0.12;
  /* Un punto de emision del propio color del grupo. Sin esto, en las caras
     que miran a la luz el especular blanco se come el tono y el brazo vuelve
     a parecer de hueso. No se busca que brille: se busca que el color no
     dependa de como caiga la luz. */
  float palE = clamp(vZoneW, 0.0, 1.0) * uPaleta * (1.0 - clamp(vCloth, 0.0, 1.0)) * (1.0 - sel)
             * mix(1.0, 0.34, step(0.01, uPulse));
  totalEmissiveRadiance += vZoneRGB * palE * 0.16 * occ;
}`)
      .replace('#include <roughnessmap_fragment>', `#include <roughnessmap_fragment>
roughnessFactor += (vnoise(vLocal * 60.0) - 0.5) * 0.17;
roughnessFactor = mix(roughnessFactor, 0.92, clamp(vCloth, 0.0, 1.0));
roughnessFactor = mix(roughnessFactor, 0.78, clamp(vCre, 0.0, 1.0) * 0.8);
roughnessFactor = clamp(roughnessFactor, 0.05, 1.0);`);
  };

  const bodyRoot = new THREE.Group();
  scene.add(bodyRoot);

  /* ---- SDF helpers ---- */
  function clamp01(t) { return t < 0 ? 0 : (t > 1 ? 1 : t); }
  function smin(a, b, k) {
    const h = clamp01(0.5 + 0.5 * (b - a) / k);
    return b * (1 - h) + a * h - k * h * (1 - h);
  }
  function smax(a, b, k) { return -smin(-a, -b, k); }
  function sdEll(px, py, pz, cx, cy, cz, rx, ry, rz) {
    const x = (px - cx) / rx, y = (py - cy) / ry, z = (pz - cz) / rz;
    const k0 = Math.sqrt(x * x + y * y + z * z);
    if (k0 === 0) return -Math.min(rx, Math.min(ry, rz));
    const x1 = x / rx, y1 = y / ry, z1 = z / rz;
    const k1 = Math.sqrt(x1 * x1 + y1 * y1 + z1 * z1);
    return k0 * (k0 - 1) / k1;
  }
  function sdCap(px, py, pz, ax, ay, az, bx, by, bz, r) {
    const bax = bx - ax, bay = by - ay, baz = bz - az;
    const pax = px - ax, pay = py - ay, paz = pz - az;
    const h = clamp01((pax * bax + pay * bay + paz * baz) / (bax * bax + bay * bay + baz * baz));
    const dx = pax - bax * h, dy = pay - bay * h, dz = paz - baz * h;
    return Math.sqrt(dx * dx + dy * dy + dz * dz) - r;
  }
  function sdRC(px, py, pz, ax, ay, az, bx, by, bz, r1, r2) {
    const bax = bx - ax, bay = by - ay, baz = bz - az;
    const l2 = bax * bax + bay * bay + baz * baz;
    const rr = r1 - r2, a2 = l2 - rr * rr, il2 = 1 / l2;
    const pax = px - ax, pay = py - ay, paz = pz - az;
    const y = pax * bax + pay * bay + paz * baz;
    const z = y - l2;
    const qx = pax * l2 - bax * y, qy = pay * l2 - bay * y, qz = paz * l2 - baz * y;
    const x2 = qx * qx + qy * qy + qz * qz;
    const y2 = y * y * l2, z2 = z * z * l2;
    const k = (rr < 0 ? -1 : 1) * rr * rr * x2;
    if ((z < 0 ? -1 : 1) * a2 * z2 > k) return Math.sqrt(x2 + z2) * il2 - r2;
    if ((y < 0 ? -1 : 1) * a2 * y2 < k) return Math.sqrt(x2 + y2) * il2 - r1;
    return (Math.sqrt(x2 * a2 * il2) + y * rr) * il2 - r1;
  }

  /* ---- SURCOS DE DEFINICIÓN (líneas talladas entre músculos) ---- */
  // Cada surco es una cápsula fina que se SUSTRAE de la superficie.
  const GROOVES = [
    { a: [0.000, 0.960, 0.118], b: [0.000, 1.225, 0.116], r: 0.0085, m: 0 }, // línea alba
    { a: [-0.062, 1.168, 0.116], b: [0.062, 1.168, 0.116], r: 0.0080, m: 0 }, // cortes abdominales
    { a: [-0.062, 1.088, 0.116], b: [0.062, 1.088, 0.116], r: 0.0080, m: 0 },
    { a: [-0.058, 1.008, 0.114], b: [0.058, 1.008, 0.114], r: 0.0080, m: 0 },
    { a: [0.027, 1.265, 0.110], b: [0.145, 1.273, 0.070], r: 0.0080, m: 1 }, // pliegue subpectoral
    { a: [0.149, 1.372, 0.086], b: [0.174, 1.323, 0.084], r: 0.0080, m: 1 }, // deltoides-brazo
    { a: [0.096, 1.000, 0.098], b: [0.126, 1.090, 0.056], r: 0.0080, m: 1 }, // V del oblicuo
    { a: [0.000, 1.032, -0.084], b: [0.000, 1.371, -0.112], r: 0.0090, m: 0 }, // surco espinal
    { a: [0.092, 0.552, 0.088], b: [0.092, 0.716, 0.082], r: 0.0080, m: 1 }, // cuádriceps
    { a: [0.257, 1.246, -0.002], b: [0.254, 1.349, 0.000], r: 0.0075, m: 1 }, // bíceps-tríceps
    { a: [0.021, 1.438, 0.087], b: [0.122, 1.419, 0.080], r: 0.0075, m: 1 }, // clavícula
    { a: [0.018, 1.553, 0.063], b: [0.057, 1.485, 0.061], r: 0.0060, m: 1 }, // esternocleidomastoideo
    { a: [0.000, 1.284, 0.107], b: [0.000, 1.353, 0.100], r: 0.0075, m: 0 }, // esternón
    { a: [0.090, 1.185, 0.081], b: [0.128, 1.237, 0.054], r: 0.0060, m: 1 }, // serrato
    { a: [0.143, 1.466, 0.069], b: [0.163, 1.382, 0.082], r: 0.0060, m: 1 }, // deltoides ant/lat
    { a: [0.168, 1.468, -0.075], b: [0.190, 1.387, -0.084], r: 0.0060, m: 1 }, // deltoides lat/post
    { a: [0.205, 1.227, -0.071], b: [0.188, 1.343, -0.085], r: 0.0060, m: 1 }, // tríceps cabeza larga
    { a: [0.198, 1.009, 0.062], b: [0.219, 1.125, 0.070], r: 0.0055, m: 1 }, // braquiorradial
    { a: [0.037, 1.509, -0.062], b: [0.114, 1.418, -0.090], r: 0.0070, m: 1 }, // trapecio superior
    { a: [0.054, 1.286, -0.111], b: [0.117, 1.353, -0.101], r: 0.0070, m: 1 }, // escápula
    { a: [0.047, 0.702, -0.084], b: [0.116, 0.703, -0.087], r: 0.0075, m: 1 }, // pliegue glúteo
    { a: [0.124, 0.555, 0.073], b: [0.133, 0.742, 0.073], r: 0.0070, m: 1 }, // recto femoral
    { a: [0.056, 0.753, 0.086], b: [0.120, 0.549, 0.073], r: 0.0060, m: 1 }, // sartorio
    { a: [0.099, 0.512, 0.074], b: [0.098, 0.442, 0.066], r: 0.0065, m: 1 }, // rótula
    { a: [0.099, 0.302, -0.059], b: [0.099, 0.419, -0.063], r: 0.0065, m: 1 }, // gemelo int/ext
    { a: [0.077, 0.202, 0.030], b: [0.080, 0.396, 0.045], r: 0.0055, m: 1 }, // tibial anterior
    { a: [0.099, 0.152, -0.043], b: [0.099, 0.248, -0.045], r: 0.0055, m: 1 }  // tendón de Aquiles
  ];

  /* ---- ANATOMÍA v5 (proporciones corregidas; pies en y=0, altura ~1.83) ---- */
  function bodySDF(px, py, pz) {
    const ax = Math.abs(px);

    // Caja torácica: más alta y estrecha en Z (el tórax humano es ovalado, no un barril)
    let d = sdEll(px, py, pz, 0, 1.330, -0.004, 0.178, 0.170, 0.112);
    d = smin(d, sdEll(px, py, pz, 0, 1.100, 0, 0.132, 0.140, 0.092), 0.10);
    d = smin(d, sdEll(px, py, pz, 0, 0.880, 0, 0.138, 0.115, 0.100), 0.09);
    d = smin(d, sdCap(px, py, pz, -0.140, 1.442, -0.005, 0.140, 1.442, -0.005, 0.056), 0.07);
    // Placa abdominal PLANA y pegada (evita el vientre abultado)
    d = smin(d, sdEll(px, py, pz, 0, 1.080, 0.082, 0.086, 0.170, 0.038), 0.05);
    // Cuello (más fino) + cabeza + mandíbula
    d = smin(d, sdCap(px, py, pz, 0, 1.480, 0.004, 0, 1.575, 0.010, 0.050), 0.045);
    let hd = sdEll(px, py, pz, 0, 1.688, 0.010, 0.090, 0.112, 0.096);
    hd = smin(hd, sdEll(px, py, pz, 0, 1.612, 0.040, 0.066, 0.050, 0.070), 0.04);
    d = smin(d, hd, 0.04);
    // Esternón: hunde el centro del pecho para que los pectorales no se fundan en una teta única
    d = smax(d, -sdCap(px, py, pz, 0, 1.262, 0.104, 0, 1.362, 0.098, 0.013), 0.045);

    // Trapecio (bajo, en pendiente) y deltoides (compacto, encaja en el hombro)
    d = smin(d, sdCap(ax, py, pz, 0.035, 1.490, -0.010, 0.123, 1.438, -0.006, 0.032), 0.06);
    d = smin(d, sdEll(ax, py, pz, 0.178, 1.418, -0.002, 0.070, 0.078, 0.072), 0.065);
    // Brazo pegado al torso, húmero afinado hacia el codo
    d = smin(d, sdRC(ax, py, pz, 0.189, 1.398, 0, 0.217, 1.178, 0.010, 0.054, 0.047), 0.06);
    d = smin(d, sdEll(ax, py, pz, 0.206, 1.322, 0.040, 0.036, 0.070, 0.034), 0.032); // bíceps
    d = smin(d, sdEll(ax, py, pz, 0.211, 1.305, -0.042, 0.036, 0.080, 0.036), 0.032); // tríceps
    d = smin(d, sdEll(ax, py, pz, 0.219, 1.168, 0.008, 0.040, 0.044, 0.040), 0.05);  // codo
    d = smin(d, sdRC(ax, py, pz, 0.219, 1.158, 0.012, 0.226, 0.940, 0.044, 0.044, 0.036), 0.045);
    d = smin(d, sdEll(ax, py, pz, 0.221, 1.088, 0.034, 0.031, 0.062, 0.030), 0.03);  // extensores
    /* LA MANO. Antes era una sola elipse y se leia como una manopla.
       Los dedos NO se pueden tallar aqui, y conviene saber por que: la
       rejilla mide 112 voxeles para 1,96 m de alto, o sea 1,75 cm por voxel
       en vertical. Un dedo tiene menos de un centimetro de ancho, asi que no
       hay malla que lo recoja -- subir la resolucion cuesta al cubo y en un
       movil ya va justa. Lo que si se resuelve, y es lo que cambia como se
       lee la mano de lejos, es la silueta: palma plana, pulgar separado y un
       bloque de dedos que se estrecha. */
    d = smin(d, sdEll(ax, py, pz, 0.229, 0.888, 0.056, 0.030, 0.046, 0.048), 0.035); // palma
    d = smin(d, sdEll(ax, py, pz, 0.206, 0.892, 0.078, 0.016, 0.030, 0.024), 0.022); // pulgar
    d = smin(d, sdEll(ax, py, pz, 0.232, 0.826, 0.056, 0.026, 0.040, 0.042), 0.028); // dedos
    d = smin(d, sdEll(ax, py, pz, 0.233, 0.792, 0.052, 0.019, 0.024, 0.032), 0.024); // puntas

    // Dorsal (ala), PECTORAL alto y plano (ya no cuelga), oblicuo discreto
    d = smin(d, sdEll(ax, py, pz, 0.122, 1.246, -0.048, 0.070, 0.138, 0.052), 0.06);
    d = smin(d, sdEll(ax, py, pz, 0.082, 1.318, 0.088, 0.080, 0.058, 0.030), 0.045);
    d = smin(d, sdEll(ax, py, pz, 0.108, 1.052, 0.040, 0.024, 0.072, 0.024), 0.055);

    // Pelvis estrecha (nada de bulto): la cadera se estrecha antes del muslo
    d = smin(d, sdEll(px, py, pz, 0, 0.800, -0.006, 0.118, 0.070, 0.086), 0.06);
    // Glúteo y pierna: muslo → rodilla → gemelo → pie
    d = smin(d, sdEll(ax, py, pz, 0.074, 0.798, -0.078, 0.072, 0.078, 0.062), 0.05);
    d = smin(d, sdRC(ax, py, pz, 0.088, 0.790, 0, 0.098, 0.492, 0.008, 0.084, 0.062), 0.06);
    d = smin(d, sdEll(ax, py, pz, 0.092, 0.650, 0.046, 0.050, 0.112, 0.036), 0.04);   // cuádriceps
    d = smin(d, sdEll(ax, py, pz, 0.092, 0.640, -0.042, 0.048, 0.106, 0.038), 0.045); // femoral
    d = smin(d, sdEll(ax, py, pz, 0.098, 0.478, 0.014, 0.046, 0.052, 0.046), 0.038);  // rodilla
    d = smin(d, sdRC(ax, py, pz, 0.098, 0.468, 0.002, 0.097, 0.132, -0.006, 0.050, 0.037), 0.042);
    d = smin(d, sdEll(ax, py, pz, 0.099, 0.368, -0.030, 0.040, 0.086, 0.037), 0.03);  // gemelo
    /* EL PIE, que era una piedra. Talon, empeine y bloque de dedos: tres
       masas de mas de tres centimetros cada una, que si caben en la rejilla.
       Con una sola elipse la figura parecia flotar sobre dos bultos. */
    d = smin(d, sdEll(ax, py, pz, 0.098, 0.062, -0.012, 0.038, 0.052, 0.042), 0.03);  // talon
    d = smin(d, sdEll(ax, py, pz, 0.100, 0.046, 0.052, 0.042, 0.036, 0.078), 0.035); // empeine
    d = smin(d, sdEll(ax, py, pz, 0.102, 0.030, 0.124, 0.040, 0.020, 0.038), 0.026); // dedos

    /* AXILA: el brazo se fundia con el torso y de frente la silueta salia sin
       cintura de hombro. Se resta una capsula corta entre el costado y el
       humero -- lo justo para que se vea el hueco, sin abrir un agujero. */
    d = smax(d, -sdCap(ax, py, pz, 0.148, 1.392, -0.004, 0.166, 1.286, 0.000, 0.030), 0.055);
    // Entrepierna: sustraer una cuña vertical para separar los muslos limpiamente
    d = smax(d, -sdCap(px, py, pz, 0, 0.560, -0.030, 0, 0.760, -0.010, 0.030), 0.05);
    // Ombligo
    d = smax(d, -sdEll(px, py, pz, 0, 1.030, 0.122, 0.012, 0.013, 0.016), 0.014);
    // Los surcos ya no se tallan en la malla (eran más finos que un vóxel):
    // ahora se sombrean por vértice con el atributo 'crease' → nítidos a cualquier zoom.
    return d;
  }

  /* ---- Voxelizar + triangulizar (resolución alta para que los surcos se vean) ---- */
  const isMobile = Math.min(window.innerWidth, window.innerHeight) < 700;
  // Rejilla EMPAQUETADA: el cuerpo llena el cubo de vóxeles en vez de ocupar el 8%.
  // Escala no uniforme -> 2.2x más detalle en X y 3.4x en Z al mismo coste.
  const SX = 0.40, SY = 0.98, SZ = 0.26, CY = 0.935;
  const RES = isMobile ? 88 : 112;
  const MAXPOLY = isMobile ? 100000 : 160000; // medido: ~59k / ~96k triángulos reales
  const mc = new MarchingCubes(RES, clayMat, false, false, MAXPOLY);
  mc.isolation = 0;
  mc.position.set(0, CY, 0);
  mc.scale.set(SX, SY, SZ);
  mc.castShadow = true;
  mc.frustumCulled = false;
  bodyRoot.add(mc);

  // Atributos por vértice (deben existir ANTES de compilar el shader)
  const creaseArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('crease', new THREE.BufferAttribute(creaseArr, 1));
  const aoArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('ao', new THREE.BufferAttribute(aoArr, 1));
  const clothArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('clothId', new THREE.BufferAttribute(clothArr, 1));
  const selWArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('selW', new THREE.BufferAttribute(selWArr, 1));
  const hovWArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('hovW', new THREE.BufferAttribute(hovWArr, 1));
  /* La paleta permanente: cada vertice guarda el color de su grupo y con
     cuanta fuerza. Se pinta UNA vez al terminar la malla, no en cada
     seleccion, asi que no cuesta nada por fotograma. */
  const zoneRGBArr = new Float32Array(MAXPOLY * 3 * 3);
  mc.geometry.setAttribute('zoneRGB', new THREE.BufferAttribute(zoneRGBArr, 3));
  const zoneWArr = new Float32Array(MAXPOLY * 3);
  mc.geometry.setAttribute('zoneW', new THREE.BufferAttribute(zoneWArr, 1));

  const half = RES / 2;
  const size2 = RES * RES;
  const field = mc.field;
  field.fill(-1000);

  /* ---- ZONAS MUSCULARES (id 1..9): picking invisible + pintado por vértice ---- */
  /* ---------- LAS ZONAS TIENEN FORMA DE MUSCULO ----------
     Cada entrada es [x, y, z, radio x, radio y, radio z, espejo]. Con
     'espejo' a 1 la forma se aplica a los dos lados del cuerpo.

     La espalda era UNA esfera centrada de 16 cm de radio y en pantalla se veia
     lo que era: un disco rojo pegado entre los omoplatos, del tamano de un
     plato. Ningun musculo tiene esa forma. Ahora son cuatro piezas por lado
     -- trapecio, el ala del dorsal y la zona lumbar -- y el resaltado sigue la
     espalda en vez de taparla.

     Y esto no es solo pintura: la misma lista decide QUE musculo hay bajo el
     dedo, asi que afinar las formas afina tambien la punteria. */
  /* LAS ZONAS. Cada pieza es una elipse [x, y, z, rx, ry, rz, espejo].
     Con la union suave de pesoDeZona() las piezas se FUNDEN, asi que ahora
     interesa poner varias pequenas siguiendo la linea del musculo en vez de
     una grande: eso da forma de biceps o de dorsal en vez de forma de huevo.
     Antes, con union dura, cada pieza extra se veia como un ovalo aparte y
     por eso habia tan pocas. */
  const ZONES = [
    { id: 1, name: 'Pecho', list: [
        [ 0.062, 1.318,  0.096, 0.062, 0.052, 0.046, 1],
        [ 0.098, 1.330,  0.086, 0.056, 0.048, 0.044, 1],
        [ 0.108, 1.356,  0.072, 0.052, 0.040, 0.040, 1],
        [ 0.040, 1.300,  0.092, 0.044, 0.048, 0.042, 1] ]},
    { id: 2, name: 'Espalda', list: [
        [ 0.052, 1.452, -0.040, 0.070, 0.052, 0.046, 1],
        [ 0.030, 1.396, -0.056, 0.058, 0.058, 0.044, 1],
        [ 0.096, 1.336, -0.074, 0.070, 0.070, 0.046, 1],
        [ 0.104, 1.268, -0.070, 0.062, 0.070, 0.044, 1],
        [ 0.086, 1.196, -0.068, 0.058, 0.072, 0.044, 1],
        [ 0.044, 1.124, -0.076, 0.048, 0.070, 0.042, 1] ]},
    { id: 3, name: 'Hombros', list: [
        [ 0.172, 1.432,  0.020, 0.062, 0.060, 0.056, 1],
        [ 0.188, 1.424, -0.016, 0.060, 0.062, 0.056, 1],
        [ 0.176, 1.436, -0.056, 0.056, 0.058, 0.050, 1],
        [ 0.156, 1.452, -0.014, 0.050, 0.046, 0.050, 1] ]},
    { id: 4, name: 'Biceps', list: [
        [ 0.204, 1.336,  0.048, 0.038, 0.044, 0.038, 1],
        [ 0.208, 1.288,  0.048, 0.038, 0.048, 0.038, 1],
        [ 0.210, 1.240,  0.042, 0.034, 0.042, 0.034, 1] ]},
    { id: 5, name: 'Triceps', list: [
        [ 0.210, 1.332, -0.050, 0.038, 0.046, 0.040, 1],
        [ 0.214, 1.284, -0.052, 0.038, 0.050, 0.040, 1],
        [ 0.214, 1.234, -0.046, 0.034, 0.044, 0.036, 1] ]},
    { id: 6, name: 'Abdominales', list: [
        [ 0.034, 1.156,  0.092, 0.042, 0.048, 0.038, 1],
        [ 0.034, 1.078,  0.092, 0.042, 0.048, 0.038, 1],
        [ 0.032, 1.000,  0.088, 0.040, 0.048, 0.036, 1],
        [ 0.086, 1.108,  0.056, 0.036, 0.070, 0.036, 1],
        [ 0.084, 1.020,  0.052, 0.034, 0.060, 0.034, 1] ]},
    { id: 7, name: 'Cuadriceps', list: [
        [ 0.086, 0.756,  0.052, 0.048, 0.058, 0.042, 1],
        [ 0.090, 0.686,  0.054, 0.050, 0.058, 0.042, 1],
        [ 0.094, 0.618,  0.052, 0.048, 0.056, 0.040, 1],
        [ 0.098, 0.556,  0.048, 0.044, 0.052, 0.038, 1],
        [ 0.100, 0.500,  0.044, 0.038, 0.042, 0.034, 1] ]},
    { id: 8, name: 'Gluteos', list: [
        [ 0.072, 0.828, -0.078, 0.062, 0.058, 0.058, 1],
        [ 0.080, 0.766, -0.074, 0.060, 0.056, 0.056, 1] ]},
    { id: 9, name: 'Gemelos', list: [
        [ 0.096, 0.406, -0.034, 0.042, 0.054, 0.040, 1],
        [ 0.098, 0.344, -0.034, 0.042, 0.054, 0.040, 1],
        [ 0.098, 0.284, -0.030, 0.034, 0.046, 0.034, 1],
        [ 0.096, 0.232, -0.026, 0.026, 0.038, 0.028, 1] ]}
  ];

  /* El color de cada grupo. Elegidos para que se distingan tambien a ojo
     daltonico: no hay dos vecinos que compartan tono, y ninguno cae en el
     rojo puro, que esta reservado al musculo SELECCIONADO. */
  const COLORES = {
    Pecho:       [0.88, 0.20, 0.30],
    Espalda:     [0.16, 0.42, 0.92],
    Hombros:     [0.99, 0.42, 0.04],
    Biceps:      [0.52, 0.26, 0.90],
    Triceps:     [0.10, 0.66, 0.80],
    Abdominales: [0.16, 0.72, 0.36],
    Cuadriceps:  [0.94, 0.74, 0.10],
    Gluteos:     [0.90, 0.30, 0.62],
    Gemelos:     [0.38, 0.62, 0.22]
  };
  /* Esfera envolvente de cada grupo. La paleta recorre 200.000 vertices por
     nueve grupos por hasta seis piezas: sin un descarte previo son millones
     de raices cuadradas y se notan en el reloj de esculpido. Con esto, un
     vertice del gemelo descarta el pecho en una resta. */
  ZONES.forEach(function(z) {
    let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9, z0 = 1e9, z1 = -1e9;
    for (const e of z.list) {
      const r = 1.55;                       // hasta donde llega el borde
      x0 = Math.min(x0, (e[6] ? -1 : 1) * e[0] - e[3] * r); x1 = Math.max(x1, e[0] + e[3] * r);
      y0 = Math.min(y0, e[1] - e[4] * r);   y1 = Math.max(y1, e[1] + e[4] * r);
      z0 = Math.min(z0, e[2] - e[5] * r);   z1 = Math.max(z1, e[2] + e[5] * r);
    }
    z.caja = [x0, x1, y0, y1, z0, z1];
    z.espejo = z.list.every(e => e[6]);
  });

  const NAME2ID = {};
  ZONES.forEach(function(z) { NAME2ID[z.name] = z.id; });
  const CAN_HOVER = window.matchMedia && window.matchMedia('(hover: hover)').matches;
  let vposCache = null, vertCount = 0;
  function paintWeight(attrName, zoneName) {
    if (!vposCache) return;
    const attr = mc.geometry.getAttribute(attrName);
    const arr = attr.array;
    const zone = zoneName ? ZONES.find(function(z) { return z.name === zoneName; }) : null;
    if (!zone) {
      for (let i = 0; i < vertCount; i++) arr[i] = 0;
      attr.needsUpdate = true;
      return;
    }
    const L = zone.list;
    for (let i = 0; i < vertCount; i++) {
      arr[i] = pesoDeZona(L, vposCache[i * 3], vposCache[i * 3 + 1], vposCache[i * 3 + 2]);
    }
    attr.needsUpdate = true;
  }

  /* EL PESO DE UN VERTICE DENTRO DE UN MUSCULO, con union SUAVE.

     Antes se resolvia con el MINIMO de las piezas: la mas cercana mandaba y
     las demas no contaban. Un minimo es una union DURA, y por eso se veia lo
     que se veia -- el cuadriceps como cuatro ovalos sueltos y la espalda como
     un racimo de bolas con los bordes marcados. Cada pieza dibujaba su propio
     borde porque ninguna sabia de las otras.

     Ahora las piezas se suman como probabilidades: cada una aporta su peso y
     el total es 1 - producto(1 - peso). Dos piezas que se solapan se
     refuerzan en vez de competir, el borde comun desaparece y queda una sola
     mancha continua con forma de musculo. Es la idea del smin() que ya usa el
     escultor, aplicada al pintado. */
  function pesoDeZona(L, x, y, z) {
    let noPertenece = 1;
    for (let j = 0; j < L.length; j++) {
      const e = L[j];
      const px = e[6] ? Math.abs(x) : x;
      const dx = (px - e[0]) / e[3], dy = (y - e[1]) / e[4], dz = (z - e[2]) / e[5];
      const nd = dx * dx + dy * dy + dz * dz;
      if (nd > 2.45) continue;               // ni con el borde llega
      const d = Math.sqrt(nd);
      /* Borde de medio radio. La unidad es RADIO NORMALIZADO, no metros: 1.0
         es la superficie de la elipse. Con 0.30 las piezas se fundian, si,
         pero cada una seguia dibujando su circulo por dentro y el abdominal
         se leia como un racimo. A 0.55 el degradado de una llega al centro de
         la vecina y la mancha sale continua. */
      const w = d <= 1 ? 1 : Math.max(0, 1 - (d - 1) / 0.55);
      if (w <= 0) continue;
      const ws = w * w * (3 - 2 * w);        // suave en los extremos
      noPertenece *= (1 - ws);
      if (noPertenece < 0.002) return 1;
    }
    return 1 - noPertenece;
  }

  window.mmClearSelection3D = function() {
    activeGroup = null;
    paintWeight('selW', null);
    paintWeight('hovW', null);
  };

  /* Aqui vivian once esferas invisibles que hacian de blanco para el dedo.
     Se retiraron enteras: eran la causa de que se pudiese seleccionar un
     musculo tapado por el cuerpo. Ahora el blanco es la propia piel. */


  /* ---- Construcción por rebanadas (no congela la página) ---- */
  let iz = 0;
  let _tCampo0 = 0;
  function buildSlices() {
    if (!_tCampo0) _tCampo0 = performance.now();
    const t0 = performance.now();
    const voxX = (2 * SX) / RES;
    /* 30 ms por fotograma era la mitad del tiempo tirada: mientras se
       esculpe no hay nada que mirar salvo el porcentaje, asi que ceder el
       hilo cada 30 ms solo servia para que la espera durase el doble.
       Medido: el relleno de voxeles son ~6 s de CPU y se convertian en el
       doble de reloj de pared. Con 55 ms el aprovechamiento sube y sigue por
       debajo del umbral en el que el navegador marca una tarea larga que
       bloquea la interaccion. */
    while (iz < RES && performance.now() - t0 < 55) {
      const wz = ((iz - half) / half) * SZ;
      for (let iy = 0; iy < RES; iy++) {
        const wy = ((iy - half) / half) * SY + CY;
        if (wy < -0.03 || wy > 1.90) continue;
        const rowBase = iz * size2 + iy * RES;
        let ix = 0;
        while (ix < RES) {
          const wx = ((ix - half) / half) * SX;
          const d = bodySDF(wx, wy, wz);
          field[rowBase + ix] = -d * 600;
          // Sphere tracing: la propia distancia dice cuántos vóxeles se pueden
          // saltar sin cambiar de signo. Deja 3 vóxeles de margen en la cáscara.
          const ad = d < 0 ? -d : d, sgn = d < 0 ? -1 : 1;
          const skip = Math.floor(ad / voxX) - 3;
          if (skip > 0) {
            for (let k = 1; k <= skip; k++) field[rowBase + ix + k] = -sgn * (ad - k * voxX) * 600;
            ix += skip + 1;
          } else ix++;
        }
      }
      iz++;
    }
    if (loading) loading.textContent = 'Esculpiendo anatomía 3D… ' + Math.round(iz / RES * 88) + '%';
    if (iz < RES) {
      requestAnimationFrame(buildSlices);
    } else {
      try {
        if (loading) loading.textContent = 'Calculando luz y relieve…';
        const _tMC = performance.now();
        mc.update();
        const _tTrian = performance.now();
        // Pintar pesos y surcos por vértice sobre la malla final
        const posAttr = mc.geometry.getAttribute('position');
        const nrmAttr = mc.geometry.getAttribute('normal');
        const n = Math.min(mc.geometry.drawRange.count, posAttr.count);
        const cAttr = mc.geometry.getAttribute('clothId');
        const krAttr = mc.geometry.getAttribute('crease');
        const aoAttr = mc.geometry.getAttribute('ao');
        vposCache = new Float32Array(n * 3);
        vertCount = n;
        const CW = 0.020; // ancho del degradado del surco
        // Esferas envolventes: descartan en un solo test las líneas lejanas
        const GB = [];
        for (let g = 0; g < GROOVES.length; g++) {
          const G = GROOVES[g];
          const hl = Math.sqrt((G.b[0] - G.a[0]) * (G.b[0] - G.a[0]) + (G.b[1] - G.a[1]) * (G.b[1] - G.a[1]) + (G.b[2] - G.a[2]) * (G.b[2] - G.a[2])) / 2;
          const rr = hl + G.r + CW;
          GB.push([(G.a[0] + G.b[0]) / 2, (G.a[1] + G.b[1]) / 2, (G.a[2] + G.b[2]) / 2, rr * rr]);
        }
        // Caché de oclusión por vóxel: miles de vértices comparten celda
        const AOS = isMobile ? 4 : 5;
        const aoCache = new Float32Array(RES * RES * RES).fill(-1);
        for (let i = 0; i < n; i++) {
          // local -> mundo (la malla va escalada de forma no uniforme)
          const vx = posAttr.getX(i) * SX, vy = posAttr.getY(i) * SY + CY, vz = posAttr.getZ(i) * SZ;
          vposCache[i * 3] = vx; vposCache[i * 3 + 1] = vy; vposCache[i * 3 + 2] = vz;
          let cw = 0;
          if (Math.abs(vx) < 0.21) {
            /* Los shorts acaban mas arriba que antes (0.718 en vez de
               0.610). Tapaban la mitad del cuadriceps, y en un mapa muscular
               eso es esconder justo lo que se viene a ver. */
            const ft = Math.min((vy - 0.718) / 0.014, (0.852 - vy) / 0.014);
            cw = Math.max(0, Math.min(1, ft));
          }
          cAttr.array[i] = cw;
          // Surcos anatómicos sombreados
          let kr = 0;
          for (let g = 0; g < GROOVES.length; g++) {
            const B = GB[g], G = GROOVES[g];
            const gx = G.m ? (vx < 0 ? -vx : vx) : vx;
            const q0 = gx - B[0], q1 = vy - B[1], q2 = vz - B[2];
            if (q0 * q0 + q1 * q1 + q2 * q2 > B[3]) continue;
            const ax0 = G.a[0], ay0 = G.a[1], az0 = G.a[2];
            const bax = G.b[0] - ax0, bay = G.b[1] - ay0, baz = G.b[2] - az0;
            const pax = gx - ax0, pay = vy - ay0, paz = vz - az0;
            const ll = bax * bax + bay * bay + baz * baz;
            let h = ll > 0 ? (pax * bax + pay * bay + paz * baz) / ll : 0;
            h = h < 0 ? 0 : (h > 1 ? 1 : h);
            const dx = pax - bax * h, dy = pay - bay * h, dz = paz - baz * h;
            const dist = Math.sqrt(dx * dx + dy * dy + dz * dz) - G.r;
            const w = dist <= 0 ? 1 : (dist >= CW ? 0 : 1 - dist / CW);
            if (w > kr) kr = w;
          }
          krAttr.array[i] = kr * (1 - cw); // la ropa no lleva surcos
          // ---- Oclusión ambiental: rayos cortos sobre el propio SDF ----
          let aov = 1;
          const qx = Math.round((vx / SX) * half + half);
          const qy = Math.round(((vy - CY) / SY) * half + half);
          const qz = Math.round((vz / SZ) * half + half);
          if (qx >= 0 && qx < RES && qy >= 0 && qy < RES && qz >= 0 && qz < RES) {
            const gi = (qz * RES + qy) * RES + qx;
            if (aoCache[gi] >= 0) aov = aoCache[gi];
            else {
              let nx = nrmAttr.getX(i) / SX, ny = nrmAttr.getY(i) / SY, nz = nrmAttr.getZ(i) / SZ;
              const nl = Math.sqrt(nx * nx + ny * ny + nz * nz) || 1;
              nx /= nl; ny /= nl; nz /= nl;
              let occ = 0, sca = 1;
              for (let s = 1; s <= AOS; s++) {
                const hh = 0.008 + 0.030 * s; // calibrado: cavidades ~0.55, planos ~0.98
                occ += (hh - bodySDF(vx + nx * hh, vy + ny * hh, vz + nz * hh)) * sca;
                sca *= 0.75;
              }
              aov = 1 - 4.0 * occ;
              aov = aov < 0.15 ? 0.15 : (aov > 1 ? 1 : aov); // nunca negro absoluto
              aoCache[gi] = aov;
            }
          }
          aoAttr.array[i] = aov;
        }
        cAttr.needsUpdate = true;
        krAttr.needsUpdate = true;
        aoAttr.needsUpdate = true;

        /* LA PALETA, pintada una sola vez. Para cada vertice se mira a que
           grupo pertenece con mas fuerza y se le guarda su color. Con union
           suave dos grupos vecinos se solapan en el borde, asi que gana el
           mas fuerte y el peso guardado es su margen sobre el segundo: eso
           difumina la frontera entre pecho y hombro en vez de cortarla. */
        const _tVert = performance.now();
        const zcAttr = mc.geometry.getAttribute('zoneRGB');
        const zwAttr = mc.geometry.getAttribute('zoneW');
        for (let i = 0; i < n; i++) {
          const vx = vposCache[i * 3], vy = vposCache[i * 3 + 1], vz = vposCache[i * 3 + 2];
          let mejor = 0, segundo = 0, col = null;
          for (let k = 0; k < ZONES.length; k++) {
            const C = ZONES[k].caja;
            const cx = ZONES[k].espejo ? (vx < 0 ? -vx : vx) : vx;
            if (cx < C[0] || cx > C[1] || vy < C[2] || vy > C[3] || vz < C[4] || vz > C[5]) continue;
            const w = pesoDeZona(ZONES[k].list, vx, vy, vz);
            if (w > mejor) { segundo = mejor; mejor = w; col = COLORES[ZONES[k].name]; }
            else if (w > segundo) segundo = w;
          }
          if (col && mejor > 0.02) {
            zcAttr.array[i * 3] = col[0];
            zcAttr.array[i * 3 + 1] = col[1];
            zcAttr.array[i * 3 + 2] = col[2];
            zwAttr.array[i] = mejor * (mejor - segundo * 0.55);
          } else {
            zwAttr.array[i] = 0;
          }
        }
        zcAttr.needsUpdate = true;
        zwAttr.needsUpdate = true;

        if (activeGroup) paintWeight('selW', activeGroup);
        if (loading) loading.style.display = 'none';
        window.__mmTris = Math.round(n / 3);
        window.__mmFases = {
          voxeles: Math.round(_tMC - _tCampo0),
          triangular: Math.round(_tTrian - _tMC),
          porVertice: Math.round(_tVert - _tTrian),
          paleta: Math.round(performance.now() - _tVert)
        };
        window.__mm3dReady = true;
      } catch (e2) {
        console.warn('MC update error:', e2);
        if (loading) loading.style.display = 'none';
        canvas.style.display = 'none';
        const fb = document.getElementById('mm-fallback');
        if (fb) fb.style.display = 'block';
      }
    }
  }
  requestAnimationFrame(buildSlices);

  /* ---- Shorts (ropa aparte, como la referencia) ---- */
  /* Los shorts ahora se PINTAN sobre la superficie esculpida (atributo clothId
     + shader). Al ser parte del propio cuerpo, jamás flotan ni dejan huecos. */

  /* ---- Selección / hover: el rojo se pinta EN la superficie ---- */
  let activeGroup = null;
  let hoverGroup = null;
  const LABELS = { Gluteos: 'Glúteos', Biceps: 'Bíceps', Triceps: 'Tríceps', Cuadriceps: 'Cuádriceps' };
  window.selectMuscle3D = function(name, openInfo) {
    activeGroup = name;
    paintWeight('selW', name);
    document.getElementById('mm-selected-label').textContent = name ? '● ' + (LABELS[name] || name) : '';
    document.getElementById('mm-selected-label').style.display = '';
    document.querySelectorAll('.muscle-btn').forEach(function(b) {
      b.classList.toggle('active', b.dataset.muscle === name);
    });
    if (openInfo && window.showMuscleModal) window.showMuscleModal(name);
    if (window.__mmFocus) window.__mmFocus(name);
    /* La rotacion automatica se para AL ELEGIR y no vuelve sola. Volvia a los
       6 s y se llevaba el musculo fuera de plano justo cuando el visitante
       estaba leyendo su ficha: la camara le quitaba de delante lo que acababa
       de pedir. Vuelve solo al quitar la seleccion. */
    controls.autoRotate = false;
    clearTimeout(window.selectMuscle3D._t);
    if (!name) {
      window.selectMuscle3D._t = setTimeout(function() {
        if (!REDUCED) controls.autoRotate = true;
      }, 900);
    }
  };

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 1.15;
  controls.maxDistance = 7.0;
  controls.maxPolarAngle = Math.PI * 0.62;
  controls.target.set(0, 0.98, 0);
  const REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let giroScroll = 0;
  controls.autoRotate = !REDUCED;
  controls.autoRotateSpeed = 0.9;

  /* ---- Encuadre cinematográfico al elegir un músculo ---- */
  // [azimut, altura del objetivo, radio] por grupo: la cámara rodea al modelo
  // hasta ponerse delante del músculo, como una cámara de estudio.
  /* [azimut, altura del objetivo, cuanto se acerca] por grupo. El tercer
     numero ya no son metros: es la fraccion de pantalla que llena el cuerpo en
     ese plano, asi que el encuadre se comporta igual en un movil y en un
     escritorio panoramico. Mas alto = mas cerca. */
  /* EL ENCUADRE DE CADA MUSCULO: [angulo, altura del centro, ALTO A ENCUADRAR].

     El tercer numero era antes un "factor de acercamiento" que dividia la
     distancia de encuadre del cuerpo entero. Y no acercaba: para el pecho
     valia 1.15, o sea un 13 % mas cerca de la vista general. Al pedir Pecho
     el visitante veia el cuerpo entero un pelin mas grande. Un boton que dice
     "enfocar" y no enfoca es peor que no tenerlo.

     Ahora el tercer numero son METROS: cuanto del cuerpo tiene que llenar la
     pantalla. La distancia sale de esa altura y no de los 1,86 m del cuerpo,
     asi que acercar de verdad ya no depende de acertar un factor a ojo.
     "Que quepan 46 cm" se comprueba con una regla. */
  const FOCUS = {
    Pecho:       [0.00, 1.31, 0.46], Abdominales: [0.00, 1.07, 0.52],
    Hombros:     [0.72, 1.42, 0.40], Biceps:      [1.05, 1.29, 0.40],
    Triceps:     [2.25, 1.28, 0.40], Espalda:     [Math.PI, 1.28, 0.62],
    Gluteos:     [Math.PI, 0.80, 0.44], Cuadriceps: [0.24, 0.63, 0.60],
    Gemelos:     [2.88, 0.33, 0.40]
  };

  /* POR QUE ESTO NO ES UN LERP POR FOTOGRAMA.
     Lo era, y medido NO LLEGABA: de los nueve musculos, siete se quedaban a
     medio camino a los 2,5 s -- cuadriceps se quedaba a 73 grados, o sea que
     al pedir cuadriceps se veia la ESPALDA. Tres razones, y las tres son del
     mismo tipo: un lerp del 5,5 % por fotograma tarda unos cincuenta
     fotogramas en cubrir el 95 % del giro, la rotacion automatica seguia
     empujando en sentido contrario, y el propio lerp se apagaba al acercarse
     porque cada paso es mas pequeno que el anterior.

     Ahora es una transicion con RELOJ: se guarda de donde sale, se sabe a
     donde va, y se recorre en 0,85 s con una curva suave. Llega siempre, y
     llega en el mismo tiempo tanto si el aparato va a 60 fps como a 24. */
  let tween = null;
  const _sph = new THREE.Spherical(), _off = new THREE.Vector3();
  function cortaAngulo(d) {
    d = d % (Math.PI * 2);
    if (d > Math.PI) d -= Math.PI * 2;
    if (d < -Math.PI) d += Math.PI * 2;
    return d;
  }
  window.__mmFocus = function(name) {
    const f = FOCUS[name];
    if (!f) { tween = null; return; }
    /* Se encuadra el ALTO del musculo, no el del cuerpo. Con suelo: por
       debajo de 0.55 m la camara se metia dentro de la piel y salia un plano
       de textura sin forma. */
    const dest = { th: f[0], y: f[1], r: Math.max(0.55, distanciaParaEncuadrarAlto(f[2])) };
    if (REDUCED) {   // sin movimiento: se salta el viaje y se planta el plano
      controls.target.set(0, dest.y, 0);
      _sph.set(dest.r, 1.34, dest.th);
      camera.position.copy(controls.target).add(_off.setFromSpherical(_sph));
      tween = null; controls.update(); return;
    }
    _off.copy(camera.position).sub(controls.target);
    _sph.setFromVector3(_off);
    tween = {
      t0: performance.now(), dur: 850,
      th0: _sph.theta, dth: cortaAngulo(dest.th - _sph.theta),
      ph0: _sph.phi,   dph: 1.34 - _sph.phi,
      r0: _sph.radius, dr: dest.r - _sph.radius,
      y0: controls.target.y, dy: dest.y - controls.target.y
    };
  };
  controls.addEventListener('start', function() { tween = null; });

  /* ---------- SENALAR: contra la PIEL, no contra globos invisibles ----------
     Antes el rayo se lanzaba contra once esferas invisibles y el CUERPO NO
     ESTABA en esa lista. Consecuencia: el cuerpo no tapaba nada, asi que
     mirando al modelo de frente se podia pulsar sobre el pecho y seleccionar
     los gluteos, porque la esfera de los gluteos seguia ahi detras y el rayo
     la atravesaba. Se seleccionaba lo que no se veia.

     Ahora el rayo se lanza contra la MALLA de verdad. Se toma el punto exacto
     de la superficie donde cayo el dedo y se busca que zona muscular lo
     contiene. Dos cosas salen gratis: el cuerpo se tapa a si mismo -- de
     frente es imposible tocar la espalda -- y el punto es el que se ve, no una
     aproximacion. Y desaparecen once mallas de la escena. */
  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2();
  const _hit = new THREE.Vector3();

  function zonaDelPunto(p) {
    let mejor = null, mejorD = 1e9;
    for (let i = 0; i < ZONES.length; i++) {
      const L = ZONES[i].list;
      for (let j = 0; j < L.length; j++) {
        const e = L[j];
        const px = e[6] ? Math.abs(p.x) : p.x;
        const dx = (px - e[0]) / e[3], dy = (p.y - e[1]) / e[4], dz = (p.z - e[2]) / e[5];
        const d = dx * dx + dy * dy + dz * dz;
        if (d < mejorD) { mejorD = d; mejor = ZONES[i].name; }
      }
    }
    // Fuera de toda zona con holgura: es tronco neutro, cabeza, mano o pie.
    return mejorD <= 2.25 ? mejor : null;
  }

  function pick(x, y) {
    if (!window.__mm3dReady) return null;
    const rect = canvas.getBoundingClientRect();
    mouse.set(((x - rect.left) / rect.width) * 2 - 1, -((y - rect.top) / rect.height) * 2 + 1);
    raycaster.setFromCamera(mouse, camera);
    const hits = raycaster.intersectObject(mc, false);
    if (!hits.length) return null;
    // La malla va escalada sin uniformidad; el punto llega en mundo y el
    // cuerpo esta centrado en el origen, asi que basta con deshacer el grupo.
    _hit.copy(hits[0].point);
    bodyRoot.worldToLocal(_hit);
    return zonaDelPunto(_hit);
  }

  canvas.addEventListener('click', function(e) {
    const name = pick(e.clientX, e.clientY);
    if (name) window.selectMuscle3D(name, true);
  });
  canvas.addEventListener('touchend', function(e) {
    if (e.changedTouches && e.changedTouches.length === 1) {
      const t = e.changedTouches[0];
      const name = pick(t.clientX, t.clientY);
      if (name) window.selectMuscle3D(name, true);
    }
  }, { passive: true });

  /* El hover se repinta SOLO cuando cambia de musculo. Antes se repintaba en
     cada mousemove: eso es recorrer los cien mil vertices de la malla y volver
     a subir el atributo entero a la tarjeta grafica varias veces por segundo,
     moviendo el raton sobre el fondo vacio y sin que cambiase nada en pantalla.
     Y el rayo tambien se lanza a lo sumo una vez por fotograma. */
  let ultimoHover = null, hoverPend = null, hoverRaf = 0;
  canvas.addEventListener('mousemove', function(e) {
    hoverPend = { x: e.clientX, y: e.clientY };
    if (hoverRaf) return;
    hoverRaf = requestAnimationFrame(function () {
      hoverRaf = 0;
      const name = pick(hoverPend.x, hoverPend.y);
      canvas.style.cursor = name ? 'pointer' : 'grab';
      hoverGroup = name;
      if (CAN_HOVER && name !== ultimoHover) {
        ultimoHover = name;
        paintWeight('hovW', (name && name !== activeGroup) ? name : null);
      }
    });
  });
  canvas.addEventListener('mouseleave', function() {
    if (ultimoHover !== null) { ultimoHover = null; paintWeight('hovW', null); }
  });

  /* ---- Animación ---- */
  /* ------------------------------------------------------------------
     EL BUCLE SE PARA CUANDO EL MAPA NO SE VE
     Esta pagina tiene trece secciones y el mapa es la primera. Sin esto,
     alguien que baja hasta Retos deja detras un WebGL pintando sesenta
     fotogramas por segundo de un lienzo que no esta en pantalla: la GPU
     encendida, el movil caliente y la bateria bajando por una figura que
     nadie mira. requestAnimationFrame solo se detiene cuando la PESTANA
     pasa a segundo plano, no cuando el lienzo sale del encuadre.

     Se para de verdad -- no se pinta en negro, no se baja a 30: no se
     encadena el siguiente fotograma -- y se reanuda en cuanto vuelve a
     asomar, con el reloj puesto donde lo dejo para que la respiracion no
     de un salto. */
  let time = 0;
  let visible = true, corriendo = false;
  function animate() {
    if (!visible) { corriendo = false; return; }
    requestAnimationFrame(animate);
    corriendo = true;
    /* Un contador de fotogramas, expuesto a proposito: es lo unico que
       permite COMPROBAR desde fuera que el bucle se para de verdad al
       salir de pantalla. Una bandera diria lo que queremos oir; esto dice
       lo que pasa. Cuesta una suma por fotograma. */
    window.__mm3dFrames = (window.__mm3dFrames || 0) + 1;
    time += 0.016;
    if (!REDUCED) {
      const breathe = 1 + Math.sin(time * 1.3) * 0.004;
      bodyRoot.scale.set(breathe, 1, breathe);
      particles.rotation.y += 0.0006;
    }
    uPulse.value = activeGroup ? (0.62 + Math.sin(time * 5) * 0.22) : 0;
    /* La paleta se enciende sola cuando la malla esta lista, POR RELOJ y no
       por fotograma. La primera version sumaba 0.016 en cada pasada, y eso
       ata la duracion a la velocidad de la maquina: medido en un equipo con
       GL por software, a los tres segundos iba por 0.16 -- habria tardado
       veinte en encenderse, y en un movil viejo lo mismo. Asi tarda 900 ms
       en cualquier aparato. */
    if (window.__mm3dReady && uPaleta.value < 1) {
      if (REDUCED) uPaleta.value = 1;
      else {
        if (!tPaleta0) tPaleta0 = performance.now();
        uPaleta.value = Math.min(1, (performance.now() - tPaleta0) / 900);
      }
    }
    // Barrido del escáner: recorre el cuerpo en coordenadas locales (-1..1)
    uScanY.value = activeGroup ? (((time * 0.42) % 2) - 1) : 99;
    ring.material.opacity = 0.16 + Math.sin(time * 2) * 0.08;
    // El viaje de camara. Termina solo, y mientras dura la rotacion
    // automatica no puede empujar en contra.
    if (tween) {
      let u = (performance.now() - tween.t0) / tween.dur;
      if (u >= 1) { u = 1; }
      const k = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;  // suave a los dos lados
      controls.target.set(0, tween.y0 + tween.dy * k, 0);
      _sph.set(tween.r0 + tween.dr * k, tween.ph0 + tween.dph * k, tween.th0 + tween.dth * k);
      camera.position.copy(controls.target).add(_off.setFromSpherical(_sph));
      if (u === 1) tween = null;
    }
    /* EL SCROLL MUEVE EL CUERPO.
       ------------------------------------------------------------------
       Mientras el mapa cruza la pantalla, la figura gira un cuarto de vuelta
       ligada a la POSICION del scroll, no al tiempo: subes y baja, bajas y
       sube. Es lo que hace que se sienta como un objeto en la mano y no como
       un video que se reproduce solo.

       Tres decisiones:
       - Se gira el CUERPO (bodyRoot), no la camara. Asi se suma a lo que el
         visitante haga con el dedo en vez de pelearse con OrbitControls.
       - Se apaga si hay un musculo elegido: el encuadre acaba de llevar la
         camara a un sitio concreto y girar la figura debajo lo desharia.
       - Y se apaga entero con "menos movimiento" del sistema.

       Se hace aqui, dentro del bucle que ya existe, y no con un observador
       aparte: leer la posicion una vez por fotograma que ya se iba a pintar
       cuesta lo que cuesta una resta. Y sin libreria: GSAP con ScrollTrigger
       son unos 70 KB comprimidos, y esta pagina acaba de bajar de 301 a 100. */
    if (!REDUCED && !activeGroup) {
      /* El alto y la posicion del lienzo en el documento se guardan y solo
         se vuelven a medir al cambiar el tamano. Antes se llamaba a
         getBoundingClientRect() en CADA fotograma, y eso obliga al
         navegador a recalcular la maqueta de la pagina entera sesenta
         veces por segundo para leer un numero que casi nunca cambia.
         scrollY no obliga a nada. */
      const alto = window.innerHeight || 800;
      const arriba = cajaTop - (window.pageYOffset || document.documentElement.scrollTop || 0);
      /* 0 cuando el lienzo entra por abajo, 1 cuando sale por arriba */
      const u = 1 - (arriba + cajaAlto) / (alto + cajaAlto);
      if (u > -0.1 && u < 1.1) {
        const objetivo = (Math.min(1, Math.max(0, u)) - 0.5) * (Math.PI * 0.5);
        /* Se persigue el objetivo en vez de saltar a el: el scroll llega a
           tirones y sin suavizado la figura tiembla. */
        giroScroll += (objetivo - giroScroll) * 0.09;
        bodyRoot.rotation.y = giroScroll;
      }
    } else if (bodyRoot.rotation.y !== 0 && !activeGroup) {
      giroScroll += (0 - giroScroll) * 0.12;
      bodyRoot.rotation.y = Math.abs(giroScroll) < 0.001 ? 0 : giroScroll;
    }

    controls.update();
    renderer.render(scene, camera);
  }
  /* La medida del lienzo dentro del documento: se toma una vez y se
     refresca al cambiar el tamano o al desplazarse (pasivo, no bloquea). */
  let cajaTop = 0, cajaAlto = 1;
  function medirCaja() {
    const r = canvas.getBoundingClientRect();
    cajaTop = r.top + (window.pageYOffset || document.documentElement.scrollTop || 0);
    cajaAlto = r.height || 1;
  }
  medirCaja();

  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver(function(entradas) {
      const dentro = entradas[0] && entradas[0].isIntersecting;
      if (dentro === visible) return;
      visible = dentro;
      if (visible) { medirCaja(); if (!corriendo) animate(); }
    }, { rootMargin: '120px 0px' });
    obs.observe(canvas);
  }

  animate();

  window.addEventListener('resize', function() {
    medirCaja();
    const w = canvas.clientWidth, h = canvas.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    /* Arrastrar la ventana de un portatil a un monitor externo cambia la
       densidad de pixeles sin recargar. Sin refrescarla aqui, el mapa se
       queda dibujado a la densidad del otro monitor: borroso en uno o
       gastando el cuadruple en el otro. */
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(w, h);
    // Al cambiar la forma del lienzo cambia lo que cabe dentro. Sin esto,
    // girar el movil dejaba el cuerpo recortado o diminuto hasta recargar.
    const nueva = distanciaParaEncuadrar(0.88);
    if (!tween && !activeGroup) {
      _off.copy(camera.position).sub(controls.target);
      _sph.setFromVector3(_off);
      _sph.radius *= nueva / distBase;
      camera.position.copy(controls.target).add(_off.setFromSpherical(_sph));
    }
    distBase = nueva;
  });

} catch (err) {
  console.warn('Muscle Map 3D error:', err);
  const c = document.getElementById('muscle-canvas');
  const l = document.getElementById('mm-loading');
  if (c) c.style.display = 'none';
  if (l) l.style.display = 'none';
  const f = document.getElementById('mm-fallback');
  if (f) f.style.display = 'block';
}
