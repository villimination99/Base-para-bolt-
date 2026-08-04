# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · el cierre, la emergencia y el diario
=================================================================
El capítulo del cierre está escrito en imperativo corto y así se queda: «Si
abriste, cierras» no se convierte en una recomendación por el camino. Las
cuatro consecuencias del cierre se traducen como lo que son —efectos
comprobables— sin subirles el tono.

El cierre de emergencia va partido en cinco <span>, uno por paso, y se traduce
renglón a renglón: el lector lo va a leer de pie y con prisa, que es
exactamente el caso para el que está escrito. La frase entrecomillada —«Esto
queda cerrado.»— es la que se dice en voz alta y conserva el punto dentro de
las comillas, como en el original.

«Cuándo parar» describe tres señales clínicas y termina mandando a un
profesional. Se traduce sin suavizar, igual que la advertencia del capítulo
anterior.
"""

T = {
    "Errores frecuentes en esta operación": {
        "en": "Frequent errors in this operation",
        "fr": "Erreurs fréquentes dans cette opération"},

    "Examinar dos cosas a la vez. No funciona: se mezclan y se pierde el hilo. Una por "
    "sesión.": {
        "en": "Examining two things at once. It does not work: they mix and the thread is "
              "lost. One per session.",
        "fr": "Examiner deux choses à la fois. Cela ne marche pas : elles se mêlent et l'on perd "
              "le fil. Une par séance."},

    "Discutir con ella. No es un juicio, es una entrevista. El operante que discute está otra "
    "vez dentro.": {
        "en": "Arguing with it. This is not a trial, it is an interview. The operator who "
              "argues is inside it again.",
        "fr": "Discuter avec elle. Ce n'est pas un procès, c'est un entretien. L'opérant qui "
              "discute est de nouveau dedans."},

    "Buscar una conclusión en la primera sesión. Un patrón de veinte años no se examina en "
    "veinte minutos. Tres o cuatro sesiones sobre el mismo asunto, separadas por semanas, "
    "rinden mucho más que una sesión larga.": {
        "en": "Looking for a conclusion in the first session. A twenty-year pattern is not "
              "examined in twenty minutes. Three or four sessions on the same matter, weeks "
              "apart, yield far more than one long session.",
        "fr": "Chercher une conclusion dès la première séance. Un schéma de vingt ans ne "
              "s'examine pas en vingt minutes. Trois ou quatre séances sur la même affaire, "
              "séparées par des semaines, rendent bien plus qu'une seule séance longue."},

    "No cerrar. Este es el error grave. Una sesión de examen que termina sin el rito de cierre "
    "deja el asunto abierto y dando vueltas el resto del día. Se cierra siempre, incluso "
    "—sobre todo— cuando ha ido mal.": {
        "en": "Not closing. This is the serious error. An examination session that ends without "
              "the closing rite leaves the matter open and turning over for the rest of the "
              "day. You always close, even —above all— when it has gone badly.",
        "fr": "Ne pas clore. Voilà l'erreur grave. Une séance d'examen qui se termine sans le "
              "rite de clôture laisse l'affaire ouverte et tournant en rond le reste de la "
              "journée. On clôt toujours, même —surtout— quand cela s'est mal passé."},

    "Cuándo parar": {"en": "When to stop", "fr": "Quand s'arrêter"},

    "Cuando aparece llanto que no se puede sostener, cuando el pulso no baja, cuando la sesión "
    "deja de ser un examen y se convierte en revivir. En cualquiera de esos tres casos se "
    "cierra inmediatamente, se anota qué pasó y no se vuelve a ese asunto en solitario. No es "
    "un fracaso de la técnica: es la técnica informando de que ese material necesita a otra "
    "persona en la habitación, y esa persona es un profesional.": {
        "en": "When crying appears that cannot be held, when the pulse does not come down, when "
              "the session stops being an examination and turns into reliving. In any of those "
              "three cases you close immediately, write down what happened and do not go back "
              "to that matter alone. It is not a failure of the technique: it is the technique "
              "reporting that this material needs another person in the room, and that person "
              "is a professional.",
        "fr": "Quand surviennent des pleurs qu'on ne peut pas soutenir, quand le pouls ne "
              "redescend pas, quand la séance cesse d'être un examen et devient une "
              "reviviscence. Dans chacun de ces trois cas on clôt immédiatement, on note ce qui "
              "s'est passé et on ne revient pas seul sur cette affaire. Ce n'est pas un échec de "
              "la technique : c'est la technique qui signale que ce matériau demande une autre "
              "personne dans la pièce, et que cette personne est un professionnel."},

    # ── El cierre ──────────────────────────────────────────────────────────
    "Todos los manuales insisten en el cierre y casi ningún practicante lo hace bien. Merece "
    "capítulo aparte porque es el punto donde una práctica sana se distingue de una práctica "
    "que desgasta.": {
        "en": "Every manual insists on the closing and hardly any practitioner does it "
              "properly. It deserves a chapter of its own because it is the point where a "
              "healthy practice is distinguished from one that wears you down.",
        "fr": "Tous les manuels insistent sur la clôture et presque aucun praticien ne la fait "
              "bien. Elle mérite un chapitre à part parce que c'est le point où une pratique "
              "saine se distingue d'une pratique qui use."},

    "Qué es el cierre": {"en": "What the closing is", "fr": "Ce qu'est la clôture"},

    "Una secuencia fija que deshace lo hecho, en orden inverso y sin prisa: se despiden los "
    "cuartos, se traza el pentagrama en la dirección contraria, se repite el eje, se camina "
    "el círculo al revés y se sale. Tres minutos, siempre los mismos.": {
        "en": "A fixed sequence that undoes what was done, in reverse order and without haste: "
              "the quarters are dismissed, the pentagram is traced in the opposite direction, "
              "the axis is repeated, the circle is walked the other way round and you step out. "
              "Three minutes, always the same three.",
        "fr": "Une séquence fixe qui défait ce qui a été fait, dans l'ordre inverse et sans "
              "hâte : on congédie les quartiers, on trace le pentagramme dans le sens contraire, "
              "on répète l'axe, on marche le cercle à l'envers et on sort. Trois minutes, "
              "toujours les mêmes."},

    "Qué hace, en términos comprobables": {
        "en": "What it does, in verifiable terms",
        "fr": "Ce qu'elle fait, en termes vérifiables"},

    "Marca un final. Sin final explícito, una sesión intensa se prolonga difusamente en el "
    "resto del día: la cabeza sigue en la operación sin estar en ella.": {
        "en": "It marks an end. With no explicit end, an intense session carries on diffusely "
              "through the rest of the day: your head stays in the operation without being in "
              "it.",
        "fr": "Elle marque une fin. Sans fin explicite, une séance intense se prolonge "
              "diffusément dans le reste de la journée : la tête reste dans l'opération sans y "
              "être."},

    "Devuelve al cuerpo. La secuencia de cierre es física y termina en la habitación, con las "
    "manos en el pecho y tres respiraciones. Es un procedimiento de aterrizaje.": {
        "en": "It gives you back your body. The closing sequence is physical and it ends in the "
              "room, with your hands on your chest and three breaths. It is a landing "
              "procedure.",
        "fr": "Elle rend au corps. La séquence de clôture est physique et se termine dans la "
              "pièce, les mains sur la poitrine et trois respirations. C'est une procédure "
              "d'atterrissage."},

    "Enseña al sistema nervioso que esto tiene límites. Un estado alterado que se sabe "
    "reversible se explora con mucha más libertad que uno que se teme. El cierre es lo que "
    "hace segura la apertura.": {
        "en": "It teaches the nervous system that this has limits. An altered state known to be "
              "reversible is explored with far more freedom than one that is feared. The "
              "closing is what makes the opening safe.",
        "fr": "Elle apprend au système nerveux que cela a des limites. Un état modifié que l'on "
              "sait réversible s'explore avec bien plus de liberté qu'un état que l'on craint. "
              "La clôture est ce qui rend l'ouverture sûre."},

    "Protege la práctica a largo plazo. La gente que abandona después de meses casi siempre "
    "abandona por acumulación: sesiones que no acabaron y dejaron residuo. El cierre es "
    "mantenimiento.": {
        "en": "It protects the practice in the long run. People who give up after months "
              "almost always give up through accumulation: sessions that never ended and left a "
              "residue. Closing is maintenance.",
        "fr": "Elle protège la pratique sur la durée. Les gens qui abandonnent au bout de "
              "quelques mois abandonnent presque toujours par accumulation : des séances qui ne "
              "se sont pas terminées et qui ont laissé un résidu. La clôture, c'est de "
              "l'entretien."},

    "La regla sin excepciones": {
        "en": "The rule with no exceptions", "fr": "La règle sans exceptions"},

    "Si abriste, cierras. Si te interrumpen, cierras — aunque sea en treinta segundos y de "
    "pie. Si la sesión ha ido mal, cierras con más cuidado, no con menos. Si te has dormido a "
    "mitad, cierras al despertar. No hay ningún caso en que salir sin cerrar sea la opción "
    "correcta.": {
        "en": "If you opened, you close. If you are interrupted, you close — even if it takes "
              "thirty seconds and you do it standing. If the session has gone badly, you close "
              "with more care, not less. If you fell asleep halfway through, you close when you "
              "wake. There is no case in which leaving without closing is the right option.",
        "fr": "Si vous avez ouvert, vous clôturez. Si l'on vous interrompt, vous clôturez — même "
              "en trente secondes et debout. Si la séance s'est mal passée, vous clôturez avec "
              "plus de soin, pas moins. Si vous vous êtes endormi au milieu, vous clôturez au "
              "réveil. Il n'existe aucun cas où sortir sans clore soit la bonne option."},

    "El cierre de emergencia": {
        "en": "The emergency closing", "fr": "La clôture d'urgence"},

    "Para cuando hay que salir ya: alguien llama, suena una alarma, algo se ha torcido. Veinte "
    "segundos, de pie, en el centro.": {
        "en": "For when you have to leave right now: somebody is at the door, an alarm goes "
              "off, something has gone wrong. Twenty seconds, standing, in the centre.",
        "fr": "Pour quand il faut sortir tout de suite : quelqu'un appelle, une alarme sonne, "
              "quelque chose a mal tourné. Vingt secondes, debout, au centre."},

    "<span>Manos al pecho.</span><span>«Esto queda cerrado.»</span><span>Tres respiraciones "
    "completas, largas.</span><span>Un paso fuera del círculo, mirando al "
    "norte.</span><span>Y se anota después, aunque sea una línea.</span>": {
        "en": "<span>Hands to the chest.</span><span>«This is now closed.»</span><span>Three "
              "full breaths, long ones.</span><span>One step outside the circle, facing "
              "north.</span><span>And you write it down afterwards, even if it is one "
              "line.</span>",
        "fr": "<span>Les mains sur la poitrine.</span><span>« Ceci est clos. »</span><span>Trois "
              "respirations complètes, longues.</span><span>Un pas hors du cercle, face au "
              "nord.</span><span>Et on le note ensuite, ne serait-ce qu'une ligne.</span>"},

    "No es tan bueno como el cierre completo y es infinitamente mejor que nada. Que exista un "
    "procedimiento de emergencia es, además, lo que permite operar tranquilo sabiendo que se "
    "puede salir.": {
        "en": "It is not as good as the complete closing and it is infinitely better than "
              "nothing. That an emergency procedure exists at all is, besides, what lets you "
              "operate calmly, knowing you can get out.",
        "fr": "Elle ne vaut pas la clôture complète et elle vaut infiniment mieux que rien. "
              "Qu'une procédure d'urgence existe est en outre ce qui permet d'opérer "
              "tranquillement, en sachant qu'on peut sortir."},

    # ── El diario ──────────────────────────────────────────────────────────
    "Si de este libro solo pudieras conservar una práctica, conserva esta. El diario no es un "
    "accesorio de la práctica: es el instrumento que convierte sesiones sueltas en "
    "conocimiento acumulado.": {
        "en": "If you could keep only one practice from this book, keep this one. The journal "
              "is not an accessory to the practice: it is the instrument that turns loose "
              "sessions into accumulated knowledge.",
        "fr": "Si vous ne pouviez garder qu'une seule pratique de ce livre, gardez celle-ci. Le "
              "journal n'est pas un accessoire de la pratique : c'est l'instrument qui "
              "transforme des séances éparses en connaissance accumulée."},

    "Por qué sin diario no hay práctica": {
        "en": "Why there is no practice without a journal",
        "fr": "Pourquoi sans journal il n'y a pas de pratique"},

    "Por una razón muy simple y bastante humillante: la memoria de los propios estados "
    "internos es malísima. A las dos semanas no recuerdas cómo fue una sesión, y lo que "
    "recuerdas está reescrito por lo que ha pasado desde entonces. Sin registro escrito no "
    "puedes saber si algo está funcionando, y por tanto no puedes corregir nada. Estás "
    "repitiendo, no practicando.": {
        "en": "For a very simple and fairly humbling reason: memory for your own internal "
              "states is dreadful. Two weeks on you do not remember how a session went, and "
              "what you do remember has been rewritten by what has happened since. With no "
              "written record you cannot know whether anything is working, and therefore you "
              "cannot correct anything. You are repeating, not practising.",
        "fr": "Pour une raison très simple et assez humiliante : la mémoire de ses propres états "
              "internes est déplorable. Au bout de deux semaines vous ne vous rappelez plus "
              "comment s'est passée une séance, et ce dont vous vous souvenez a été réécrit par "
              "ce qui est arrivé depuis. Sans trace écrite vous ne pouvez pas savoir si quelque "
              "chose fonctionne, et donc vous ne pouvez rien corriger. Vous répétez, vous ne "
              "pratiquez pas."},

    "Entrada mínima por sesión": {
        "en": "Minimum entry per session", "fr": "Entrée minimale par séance"},

    "La hora real, no la prevista": {
        "en": "The actual time, not the planned one",
        "fr": "L'heure réelle, non celle qui était prévue"},
}
