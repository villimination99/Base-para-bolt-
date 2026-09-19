# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · fichas de los arcanos X a XIV
=====================================================
La ficha del decimotercero no nombra la carta ni en el título ni en el cuerpo:
dice «esta carta va sin nombre escrito», que es exactamente lo que ocurre en
el patrón de Marsella. La traducción respeta el rodeo en los tres idiomas. Un
«Death» o un «La Mort» servicial estropearía el único argumento de la ficha.

Las letras siguen su transliteración: yod, kaf, lámed, mem y nun son yod, kaph,
lamed, mem y nun en inglés, y yod, kaph, lamed, mem y noun en francés.
"""

T = {
    # ── X · La Rueda ───────────────────────────────────────────────────────
    "X · La Rueda": {"en": "X · The Wheel", "fr": "X · La Roue"},
    "Yod · valor 10 · simple · signo": {
        "en": "Yod · value 10 · simple · sign", "fr": "Yod · valeur 10 · simple · signe"},
    "Una rueda con figuras que suben por un lado y bajan por el otro.": {
        "en": "A wheel with figures rising on one side and falling on the other.",
        "fr": "Une roue avec des figures qui montent d'un côté et descendent de l'autre."},

    "Derecho: esto cambia y no depende de ti. Es la carta del ciclo y del azar, y su "
    "lección es de las duras: hay un tramo del asunto que solo admite esperar bien. Enlaza "
    "con la distinción más vieja y más útil de la filosofía práctica: la que separa lo que "
    "depende de nosotros de lo que no.": {
        "en": "Upright: this changes and it does not depend on you. It is the card of the "
              "cycle and of chance, and its lesson is one of the hard ones: there is a stretch "
              "of the matter that admits nothing but waiting well. It connects with the oldest "
              "and most useful distinction in practical philosophy: the one that separates "
              "what depends on us from what does not.",
        "fr": "À l'endroit : cela change et cela ne dépend pas de vous. C'est la carte du cycle "
              "et du hasard, et sa leçon est des plus dures : il y a un tronçon de l'affaire "
              "qui n'admet rien d'autre que de bien attendre. Elle rejoint la distinction la "
              "plus ancienne et la plus utile de la philosophie pratique : celle qui sépare ce "
              "qui dépend de nous de ce qui n'en dépend pas."},

    "Invertido: pelearse con la rueda. Empujar contra un ciclo, o atribuirse el mérito de "
    "una subida que era del propio giro.": {
        "en": "Reversed: fighting the wheel. Pushing against a cycle, or claiming credit for a "
              "rise that belonged to the turn itself.",
        "fr": "Inversée : se battre contre la roue. Pousser contre un cycle, ou s'attribuer le "
              "mérite d'une montée qui venait du tour lui-même."},

    "La pregunta: ¿Qué parte de esto está girando sola, y qué estoy haciendo para frenarla?": {
        "en": "The question: What part of this is turning on its own, and what am I doing to "
              "brake it?",
        "fr": "La question : quelle part de cela tourne toute seule, et que fais-je pour la "
              "freiner ?"},

    # ── XI · La Fuerza ─────────────────────────────────────────────────────
    "XI · La Fuerza": {"en": "XI · Strength", "fr": "XI · La Force"},
    "Kaf · valor 20 · doble · planeta": {
        "en": "Kaph · value 20 · double · planet",
        "fr": "Kaph · valeur 20 · double · planète"},
    "Una mujer que abre con las manos la boca de un león, sin violencia aparente.": {
        "en": "A woman opening a lion's jaws with her hands, with no apparent violence.",
        "fr": "Une femme qui ouvre de ses mains la gueule d'un lion, sans violence apparente."},

    "Derecho: la fuerza que sirve aquí no es la que golpea. Es la de sostener sin ceder y "
    "sin pelear, día tras día. La carta de la constancia y del dominio de lo propio que no "
    "necesita demostrarse.": {
        "en": "Upright: the strength that serves here is not the kind that strikes. It is the "
              "kind that holds without yielding and without fighting, day after day. The card "
              "of constancy and of a self-command that needs no demonstrating.",
        "fr": "À l'endroit : la force qui sert ici n'est pas celle qui frappe. C'est celle qui "
              "tient sans céder et sans se battre, jour après jour. La carte de la constance "
              "et d'une maîtrise de soi qui n'a pas besoin de se montrer."},

    "Invertido: fuerza empleada en dominar lo que no se puede, o contención que ya es "
    "represión. También la blandura que se llama paciencia.": {
        "en": "Reversed: strength spent on mastering what cannot be mastered, or restraint "
              "that has become repression. Also the softness that calls itself patience.",
        "fr": "Inversée : une force employée à dominer ce qui ne peut l'être, ou une retenue "
              "devenue répression. Aussi la mollesse qui se fait appeler patience."},

    "La pregunta: ¿Qué estoy intentando someter en vez de sostener?": {
        "en": "The question: What am I trying to subdue instead of hold?",
        "fr": "La question : qu'est-ce que j'essaie de soumettre au lieu de le tenir ?"},

    # ── XII · El Colgado ───────────────────────────────────────────────────
    "XII · El Colgado": {"en": "XII · The Hanged Man", "fr": "XII · Le Pendu"},
    "Lámed · valor 30 · simple · signo": {
        "en": "Lamed · value 30 · simple · sign",
        "fr": "Lamed · valeur 30 · simple · signe"},
    "Un hombre suspendido por un pie de una viga, cabeza abajo y tranquilo.": {
        "en": "A man suspended by one foot from a beam, head down and untroubled.",
        "fr": "Un homme suspendu par un pied à une poutre, tête en bas et tranquille."},

    "Derecho: la espera con sentido. Es la carta del cambio de punto de vista conseguido "
    "pagando la incomodidad de quedarse quieto en una postura difícil. Nada avanza, y eso "
    "es lo correcto ahora.": {
        "en": "Upright: waiting that means something. It is the card of the change of "
              "viewpoint bought by paying the discomfort of staying still in an awkward "
              "position. Nothing advances, and that is the right thing now.",
        "fr": "À l'endroit : l'attente qui a du sens. C'est la carte du changement de point de "
              "vue obtenu en payant l'inconfort de rester immobile dans une posture difficile. "
              "Rien n'avance, et c'est ce qu'il faut en ce moment."},

    "Invertido: sacrificio inútil. Aguantar por aguantar, o quedarse colgado esperando un "
    "rescate que no depende de nadie. También el mártir, que es el colgado que ha empezado "
    "a cobrar.": {
        "en": "Reversed: useless sacrifice. Enduring for the sake of enduring, or hanging "
              "there waiting for a rescue that is nobody's to give. Also the martyr, who is "
              "the hanged man who has started charging for it.",
        "fr": "Inversée : le sacrifice inutile. Tenir pour tenir, ou rester suspendu en "
              "attendant un sauvetage qui ne dépend de personne. Aussi le martyr, qui est le "
              "pendu qui a commencé à se faire payer."},

    "La pregunta: ¿Esta espera está haciendo algo, o solo me está costando?": {
        "en": "The question: Is this waiting doing anything, or is it only costing me?",
        "fr": "La question : cette attente fait-elle quelque chose, ou ne fait-elle que me "
              "coûter ?"},

    # ── XIII · El Arcano sin Nombre ────────────────────────────────────────
    "El tramo difícil. Seis arcanos que describen lo que se derrumba, lo que se ordena "
    "después y lo que se ve mal en la oscuridad.": {
        "en": "The hard stretch. Six arcana describing what collapses, what gets ordered "
              "afterwards and what is badly seen in the dark.",
        "fr": "Le tronçon difficile. Six arcanes qui décrivent ce qui s'effondre, ce qui "
              "s'ordonne ensuite et ce qu'on voit mal dans le noir."},

    "Mem · valor 40 · madre · elemento": {
        "en": "Mem · value 40 · mother · element",
        "fr": "Mem · valeur 40 · mère · élément"},
    "Un esqueleto con una hoz que siega. En el patrón de Marsella esta carta va sin nombre "
    "escrito.": {
        "en": "A skeleton with a scythe, reaping. In the Marseille pattern this card carries "
              "no written name.",
        "fr": "Un squelette qui fauche. Dans le patron de Marseille, cette carte ne porte aucun "
              "nom écrit."},

    "Derecho: algo se acaba, y acabarse es su función. No es la carta de la muerte física: "
    "es la del corte, la del final que despeja. Que en Marsella no lleve nombre es la mejor "
    "pista sobre cómo leerla.": {
        "en": "Upright: something is ending, and ending is its function. It is not the card of "
              "physical death: it is the card of the cut, of the ending that clears the "
              "ground. That it carries no name in Marseille is the best clue to how to read "
              "it.",
        "fr": "À l'endroit : quelque chose se termine, et se terminer est sa fonction. Ce n'est "
              "pas la carte de la mort physique : c'est celle de la coupe, de la fin qui "
              "dégage. Qu'elle ne porte pas de nom à Marseille est le meilleur indice sur la "
              "façon de la lire."},

    "Invertido: el final que no se deja ocurrir. Sostener con vida algo que ya terminó, con "
    "el coste que eso tiene. También el miedo al cambio convertido en régimen.": {
        "en": "Reversed: the ending that is not allowed to happen. Keeping alive something "
              "that already finished, with the cost that carries. Also fear of change turned "
              "into a regime.",
        "fr": "Inversée : la fin qu'on ne laisse pas arriver. Maintenir en vie ce qui est déjà "
              "terminé, avec ce que cela coûte. Aussi la peur du changement devenue régime."},

    "La pregunta: ¿Qué se ha terminado aquí y sigo tratando como vivo?": {
        "en": "The question: What has ended here that I keep treating as alive?",
        "fr": "La question : qu'est-ce qui s'est terminé ici et que je continue de traiter "
              "comme vivant ?"},

    # ── XIV · La Templanza ─────────────────────────────────────────────────
    "XIV · La Templanza": {"en": "XIV · Temperance", "fr": "XIV · Tempérance"},
    "Nun · valor 50 · simple · signo": {
        "en": "Nun · value 50 · simple · sign", "fr": "Noun · valeur 50 · simple · signe"},
}
