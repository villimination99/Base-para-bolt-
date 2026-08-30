# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · cierre de las láminas, cubierta, créditos e índice
========================================================================
Los tres términos griegos —órexis, hormé, sunkatáthesis— no se traducen en
ninguna de las tres lenguas. Son los nombres de las tres disciplinas clásicas
y van en cursiva bajo su rótulo en español; quien busque cualquiera de los
tres encontrará la misma literatura en los tres idiomas, y una traducción los
volvería irrastreables. Lo que sí se traduce es el rótulo de encima y la glosa
de debajo.

Los créditos, como los del libro de los arcanos, apoyan la obra en la
tradición común y no en una norma legal: los ejercicios de examen de
conciencia llevan siglos por escrito y no son de nadie.
"""

T = {
    "Avisa de una pérdida": {
        "en": "It warns of a loss", "fr": "Elle signale une perte"},
    "Volverse relato sobre uno mismo": {
        "en": "Turning into a story about oneself",
        "fr": "Devenir un récit sur soi-même"},

    "VERGÜENZA": {"en": "SHAME", "fr": "HONTE"},
    "Calor, ganas de desaparecer": {
        "en": "Heat, wanting to disappear", "fr": "Chaleur, envie de disparaître"},
    "Avisa de una norma propia": {
        "en": "It warns of a rule of one's own",
        "fr": "Elle signale une règle propre"},
    "Extenderse de un acto a la identidad": {
        "en": "Spreading from an act to the identity",
        "fr": "S'étendre d'un acte à l'identité"},

    "NI EXPRESARLAS NI REPRIMIRLAS · MIRARLAS HASTA QUE PASEN": {
        "en": "NEITHER EXPRESS THEM NOR REPRESS THEM · WATCH THEM UNTIL THEY PASS",
        "fr": "NI LES EXPRIMER NI LES RÉPRIMER · LES REGARDER JUSQU'AU BOUT"},

    # ── Lámina: las tres disciplinas ───────────────────────────────────────
    "DESEO": {"en": "DESIRE", "fr": "DÉSIR"},
    "órexis": {"en": "órexis", "fr": "órexis"},
    "Lo que quiero y lo que rechazo": {
        "en": "What I want and what I refuse",
        "fr": "Ce que je veux et ce que je refuse"},
    "Aquí se aprende a no querer lo que no depende de mí.": {
        "en": "Here you learn not to want what does not depend on you.",
        "fr": "Ici on apprend à ne pas vouloir ce qui ne dépend pas de soi."},

    "ACCIÓN": {"en": "ACTION", "fr": "ACTION"},
    "hormé": {"en": "hormé", "fr": "hormé"},
    "Lo que hago y con quién": {
        "en": "What I do and with whom", "fr": "Ce que je fais et avec qui"},
    "Aquí se aprende a actuar bien con los demás, gane o pierda.": {
        "en": "Here you learn to act well towards others, win or lose.",
        "fr": "Ici on apprend à bien agir avec les autres, qu'on gagne ou qu'on perde."},

    "ASENTIMIENTO": {"en": "ASSENT", "fr": "ASSENTIMENT"},
    "sunkatáthesis": {"en": "sunkatáthesis", "fr": "sunkatáthesis"},
    "A qué le doy la razón": {
        "en": "What I grant to be true", "fr": "À quoi je donne raison"},
    "Aquí se aprende a no tragarse la primera impresión.": {
        "en": "Here you learn not to swallow the first impression.",
        "fr": "Ici on apprend à ne pas avaler la première impression."},

    "EN ESTE ORDEN · NO SE PASA A LA SIGUIENTE SIN LA ANTERIOR": {
        "en": "IN THIS ORDER · YOU DO NOT MOVE ON WITHOUT THE ONE BEFORE",
        "fr": "DANS CET ORDRE · ON NE PASSE PAS À LA SUIVANTE SANS LA PRÉCÉDENTE"},

    # ── Cubierta ───────────────────────────────────────────────────────────
    "Códice del Sí Mismo": {"en": "Codex of the Self", "fr": "Codex du Soi"},

    "Manual de observación interior: la atención dividida, los tres centros y el trabajo de "
    "estar presente": {
        "en": "A manual of inner observation: divided attention, the three centres and the "
              "work of being present",
        "fr": "Manuel d'observation intérieure : l'attention divisée, les trois centres et le "
              "travail d'être présent"},

    # ── Créditos ───────────────────────────────────────────────────────────
    "<strong>Códice del Sí Mismo</strong> es una obra original de Villuminations,\n"
    "     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.\n"
    "     Obra original · Primera edición, 2026.": {
        "en": "<strong>Codex of the Self</strong> is an original work by Villuminations, "
              "written and typeset entirely for <strong>villuminations.com</strong>. "
              "Original work · First edition, 2026.",
        "fr": "<strong>Codex du Soi</strong> est une œuvre originale de Villuminations, écrite "
              "et composée intégralement pour <strong>villuminations.com</strong>. Œuvre "
              "originale · Première édition, 2026."},

    "El material del que parte pertenece a la <strong>tradición común</strong>:\n"
    "     los ejercicios clásicos de examen de conciencia, atención y registro\n"
    "     interior se transmiten por escrito desde hace siglos y no son propiedad\n"
    "     de nadie. Lo que aquí se ofrece —la redacción, la estructura de\n"
    "     capítulos, las prácticas, las fichas y las ilustraciones— es trabajo\n"
    "     propio y está protegido como tal.": {
        "en": "The material it starts from belongs to the <strong>common tradition</strong>: "
              "the classical exercises of examination of conscience, attention and inner "
              "record-keeping have been transmitted in writing for centuries and are nobody's "
              "property. What is offered here —the writing, the chapter structure, the "
              "practices, the entries and the illustrations— is original work and is protected "
              "as such.",
        "fr": "Le matériau dont il part appartient à la <strong>tradition commune</strong> : "
              "les exercices classiques d'examen de conscience, d'attention et de relevé "
              "intérieur se transmettent par écrit depuis des siècles et n'appartiennent à "
              "personne. Ce qui est proposé ici —la rédaction, la structure des chapitres, les "
              "pratiques, les fiches et les illustrations— est un travail propre et protégé "
              "comme tel."},

    "<strong>Cómo leer este libro.</strong> Es un libro de\n"
    "     <em>trabajo interior</em>, escrito en un lenguaje simbólico. No es\n"
    "     psicología clínica ni terapia. Nada de lo que sigue diagnostica ni trata\n"
    "     ningún trastorno, y no sustituye la atención de un psicólogo o un\n"
    "     psiquiatra colegiado. Si atraviesas una crisis, busca ayuda profesional:\n"
    "     este libro puede acompañar ese camino, no reemplazarlo.": {
        "en": "<strong>How to read this book.</strong> It is a book of <em>inner work</em>, "
              "written in a symbolic language. It is not clinical psychology and it is not "
              "therapy. Nothing that follows diagnoses or treats any disorder, and it does not "
              "replace the care of a registered psychologist or psychiatrist. If you are going "
              "through a crisis, seek professional help: this book can accompany that road, "
              "not replace it.",
        "fr": "<strong>Comment lire ce livre.</strong> C'est un livre de <em>travail "
              "intérieur</em>, écrit dans un langage symbolique. Ce n'est ni de la psychologie "
              "clinique ni une thérapie. Rien de ce qui suit ne diagnostique ni ne traite le "
              "moindre trouble, et cela ne remplace pas les soins d'un psychologue ou d'un "
              "psychiatre inscrit à l'ordre. Si vous traversez une crise, cherchez une aide "
              "professionnelle : ce livre peut accompagner ce chemin, non le remplacer."},

    # ── Índice ─────────────────────────────────────────────────────────────
    "No estabas aquí": {"en": "You were not here", "fr": "Vous n'étiez pas là"},
    "Las cuatro cosas que no sabemos de nosotros": {
        "en": "The four things we do not know about ourselves",
        "fr": "Les quatre choses que nous ignorons de nous"},
    "De dónde viene esto": {"en": "Where this comes from", "fr": "D'où vient tout ceci"},
    "La atención dividida": {"en": "Divided attention", "fr": "L'attention divisée"},
    "Los tres centros": {"en": "The three centres", "fr": "Les trois centres"},
}
