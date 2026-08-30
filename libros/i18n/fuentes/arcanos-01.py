# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · figuras, tiradas, cubierta, créditos e índice
=====================================================================
Los créditos de este libro no citan el 17 U.S.C. § 105 como los de la
colección de salud, y no puede corregirse por analogía: su base es otra. Lo
que aquí es de todos no lo es por una norma federal estadounidense, sino
porque la secuencia de los arcanos y sus correspondencias llevan siglos
imprimiéndose en obras de dominio público. La frase «tradición común» es
deliberada y se traduce como lo que es, no como una cita legal.

Los nombres de las figuras vuelven a ser los de cada baraja: Caballo es Knight
y Cavalier, Sota es Page y Valet.
"""

T = {
    "Caballo": {"en": "Knight", "fr": "Cavalier"},
    "Reina": {"en": "Queen", "fr": "Reine"},
    "Rey": {"en": "King", "fr": "Roi"},

    "COPAS": {"en": "CUPS", "fr": "COUPES"},
    "ESPADAS": {"en": "SWORDS", "fr": "ÉPÉES"},
    "OROS": {"en": "PENTACLES", "fr": "DENIERS"},

    "CADA FIGURA LLEVA SU PROPIO ELEMENTO DENTRO DEL PALO": {
        "en": "EACH COURT CARD CARRIES ITS OWN ELEMENT WITHIN THE SUIT",
        "fr": "CHAQUE FIGURE PORTE SON PROPRE ÉLÉMENT DANS LA COULEUR"},

    # ── Lámina: las tres tiradas ───────────────────────────────────────────
    "LAS TRES": {"en": "THE THREE", "fr": "LES TROIS"},
    "Qué había · qué hay · qué falta": {
        "en": "What was · what is · what is missing",
        "fr": "Ce qui fut · ce qui est · ce qui manque"},

    "LA CRUZ DE CUATRO": {"en": "THE CROSS OF FOUR", "fr": "LA CROIX DE QUATRE"},
    "El hecho · lo que aporto · lo que estorba · el paso": {
        "en": "The fact · what I bring · what hinders · the step",
        "fr": "Le fait · ce que j'apporte · ce qui gêne · le pas"},

    "EL ESPEJO": {"en": "THE MIRROR", "fr": "LE MIROIR"},
    "Como lo veo · como lo ve el otro · lo que ninguno ve": {
        "en": "As I see it · as the other sees it · what neither sees",
        "fr": "Comme je le vois · comme l'autre le voit · ce qu'aucun ne voit"},

    "TRES TIRADAS PROPIAS · NINGUNA PREDICE NADA": {
        "en": "THREE SPREADS OF OUR OWN · NONE PREDICTS ANYTHING",
        "fr": "TROIS TIRAGES PROPRES · AUCUN NE PRÉDIT RIEN"},

    # ── Cubierta ───────────────────────────────────────────────────────────
    "Códice de los Arcanos": {
        "en": "Codex of the Arcana", "fr": "Codex des Arcanes"},

    "Las setenta y ocho cartas como instrumento de lectura: los veintidós mayores, los "
    "cuatro palos y los treinta y seis decanatos": {
        "en": "The seventy-eight cards as an instrument of reading: the twenty-two major "
              "arcana, the four suits and the thirty-six decans",
        "fr": "Les soixante-dix-huit cartes comme instrument de lecture : les vingt-deux "
              "majeurs, les quatre couleurs et les trente-six décans"},

    # ── Créditos ───────────────────────────────────────────────────────────
    "<strong>Códice de los Arcanos</strong> es una obra original de Villuminations,\n"
    "     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.\n"
    "     Obra original · Primera edición, 2026.": {
        "en": "<strong>Codex of the Arcana</strong> is an original work by Villuminations, "
              "written and typeset entirely for <strong>villuminations.com</strong>. "
              "Original work · First edition, 2026.",
        "fr": "<strong>Codex des Arcanes</strong> est une œuvre originale de Villuminations, "
              "écrite et composée intégralement pour <strong>villuminations.com</strong>. "
              "Œuvre originale · Première édition, 2026."},

    "El material del que parte pertenece a la <strong>tradición común</strong>:\n"
    "     la secuencia de los arcanos, su iconografía y las correspondencias\n"
    "     clásicas se transmiten por escrito desde hace siglos en obras de dominio\n"
    "     público y no son propiedad de nadie. Lo que aquí se ofrece —la redacción,\n"
    "     la estructura de capítulos, las lecturas, las fichas y las\n"
    "     ilustraciones— es trabajo propio y está protegido como tal.": {
        "en": "The material it starts from belongs to the <strong>common tradition</strong>: "
              "the sequence of the arcana, their iconography and the classical "
              "correspondences have been transmitted in writing for centuries in works in the "
              "public domain and are nobody's property. What is offered here —the writing, "
              "the chapter structure, the readings, the card entries and the illustrations— "
              "is original work and is protected as such.",
        "fr": "Le matériau dont il part appartient à la <strong>tradition commune</strong> : "
              "la séquence des arcanes, leur iconographie et les correspondances classiques "
              "se transmettent par écrit depuis des siècles dans des œuvres du domaine public "
              "et n'appartiennent à personne. Ce qui est proposé ici —la rédaction, la "
              "structure des chapitres, les lectures, les fiches et les illustrations— est un "
              "travail propre et protégé comme tel."},

    "<strong>Cómo leer este libro.</strong> Los arcanos son un\n"
    "     <em>lenguaje simbólico</em>: una manera antigua y muy afinada de nombrar\n"
    "     situaciones y temperamentos. No es una ciencia predictiva. Nada de lo que\n"
    "     sigue anuncia hechos futuros, diagnostica enfermedades ni sustituye la\n"
    "     atención de un médico o un psicólogo colegiado.": {
        "en": "<strong>How to read this book.</strong> The arcana are a <em>symbolic "
              "language</em>: an old and very finely tuned way of naming situations and "
              "temperaments. It is not a predictive science. Nothing that follows announces "
              "future events, diagnoses illnesses or replaces the care of a registered doctor "
              "or psychologist.",
        "fr": "<strong>Comment lire ce livre.</strong> Les arcanes sont un <em>langage "
              "symbolique</em> : une manière ancienne et très affinée de nommer des "
              "situations et des tempéraments. Ce n'est pas une science prédictive. Rien de "
              "ce qui suit n'annonce de faits futurs, ne diagnostique de maladies ni ne "
              "remplace les soins d'un médecin ou d'un psychologue inscrit à l'ordre."},

    # ── Índice ─────────────────────────────────────────────────────────────
    "Lo que el tarot es": {"en": "What tarot is", "fr": "Ce qu'est le tarot"},
    "La historia real": {"en": "The real history", "fr": "L'histoire réelle"},
    "La estructura de las setenta y ocho": {
        "en": "The structure of the seventy-eight",
        "fr": "La structure des soixante-dix-huit"},
    "Los mayores y sus letras": {
        "en": "The major arcana and their letters",
        "fr": "Les majeurs et leurs lettres"},
    "Del I al VI · la salida": {
        "en": "From I to VI · the setting out", "fr": "Du I au VI · le départ"},
    "Del VII al XII · la prueba": {
        "en": "From VII to XII · the trial", "fr": "Du VII au XII · l'épreuve"},
    "Del XIII al XVIII · el paso": {
        "en": "From XIII to XVIII · the passage", "fr": "Du XIII au XVIII · le passage"},
    "Del XIX al XXI y el Loco · la salida": {
        "en": "From XIX to XXI and the Fool · the way out",
        "fr": "Du XIX au XXI et le Mat · la sortie"},
    "Los cuatro palos": {"en": "The four suits", "fr": "Les quatre couleurs"},
    "Los ases y las diez etapas": {
        "en": "The aces and the ten stages", "fr": "Les as et les dix étapes"},
    "Las treinta y seis y sus decanatos": {
        "en": "The thirty-six and their decans",
        "fr": "Les trente-six et leurs décans"},
}
