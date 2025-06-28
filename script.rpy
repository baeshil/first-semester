label start:
    scene black with fade
    play music "intro_theme.mp3" fadein 1.0

    "La PAES ha terminado. El verano se esfumó y hoy empieza tu vida universitaria."
    "Estás a punto de ingresar a la carrera de Ingeniería Civil Informática."

    $ nombre = renpy.input("¿Cuál es tu nombre?")
    $ nombre = nombre.strip()

    menu:
        "¿Cuál es tu género?"
        "Masculino":
            $ genero = "masculino"
        "Femenino":
            $ genero = "femenino"

    if genero == "femenino":
        $ bienvenida = "Bienvenida"
        $ nervio = "nerviosa"
        $ emocion = "emocionada"
        $ sola_solo = "sola"
        $ tranquila_tranquilo = "tranquila"
    else:
        $ bienvenida = "Bienvenido"
        $ nervio = "nervioso"
        $ emocion = "emocionado"
        $ sola_solo = "solo"
        $ tranquila_tranquilo = "tranquilo"

    "[bienvenida], [nombre]. Tu historia está por comenzar."

    jump capitulo_1


label capitulo_1:

    # INICIO DEL JUEGO
    scene fotopmintro with fade

    "Soy un alguien... promedio, tengo una familia que me quiere, saqué buenas notas en la media y en general..."
    "La vida no me ha tratado mal, he sacado una nota decente en la PAES, la cual me permitió entrar en esta universidad."
    "Hoy es mi primer día, oficialmente me convierto en estudiante de ingeniería."
    "Durante la media no tuve pasiones afirmadas debido a una falta de convicción y por juntarme con personas igual de vagas que yo."
    "Pero hoy es el día, finalmente perseguiré una vida mejor, una 'vida universitaria de color rosa'."
    "O al menos eso pensé al comenzar..."
    "Sinceramente me pregunto qué me deparará en esta nueva etapa."

    scene entrada_principal_borroso with fade

    "El campus está lleno de gente. Caras nuevas, emociones mezcladas."
    "Pero este es mi momento."
    stop music fadeout 1.0
    jump semana_1


label semana_1:

    scene entrada_principal_borroso with dissolve
    play music "campus_ambiente.mp3" fadein 0.5

    "El sol brilla... sobre las nubes."
    "La entrada principal de la universidad te recibe con banderas y gente."

    menu:
        "¿Qué harás?"
        "Caminar [sola_solo] y observar el entorno":
            $ exploracion += 1
            "Miras los edificios, las salas… algo en ti se llena de entusiasmo."
        "Buscar a alguien con quien hablar":
            $ afinidad_diego += 1
            show diego_doodle at left with fade
            die "¡Hey! ¿También vas a Informática? Soy Diego. Ojalá seamos compañeros."
        "Revisar tu horario rápidamente":
            show joel_prueba at center with fade
            $ afinidad_joel += 1
            pjo "Hola, ¿eres de primer año? [tranquila_tranquilo], al inicio es difícil, pero te acostumbrarás."

    stop music fadeout 1.0
    scene comedor_pequeno_borroso with dissolve
    play music "interesante.mp3" fadein 1.0

    "Se reunieron múltiples estudiantes en un punto específico. Un hombre se encuentra hablando."
    "Supones que es el director de carrera, por lo que te sientas en una de las últimas 3 sillas libres."
    "Dos personas se sientan junto a ti. Uno parece muy motivado, el otro completamente desinteresado."

    show diego_doodle at left
    show matias_doodle at right

    "Uno habla para sí mismo, emocionado."
    "El otro se encuentra bostezando, aburrido."

    menu:
        "¿Con quién hablarás?"
        "Hablar con el emocionado":
            $ afinidad_diego += 1
            "Conectan hablando de videojuegos y lógica matemática."
        "Hablar con el aburrido":
            $ afinidad_matias += 1
            "Te comenta que odia madrugar y que nunca lo verán en una ayudantía."
        "Quedarte en silencio":
            $ independencia += 1
            "Solo escuchas. Tal vez ya tendrás tiempo de conocerlos mejor."

    scene pasillo_1_borroso with fade
    "Según el horario... tengo una clase pronto, es momento de ir entonces."

    scene pasillo_2_borroso_1 with fade
    "No es aquí..."

    scene pasillo_3_borroso with fade 
    "Ni aquí."
    "Voy a volver a bajar."

    scene entrada_2_borroso with fade
    "Pff... espera, era en el edificio de la biblioteca."

    scene bibe with fade
    scene bibe2 with fade
    scene bibesp with fade

    scene aula_intro_prog with dissolve
    "Primer encuentro con tus profes."

    show joel_prueba at center with fade
    pjo "Soy Joel. Su profesor de Introducción a la Ingeniería este semestre."

    show cris_prueba at right with fade
    pcr "Yo soy Cristian. Su profesor de Programación por este semestre."
    pcr "Hay otro profesor de programación, Raúl. Lastimosamente no pudo venir pues se enfermó."

    menu:
        "¿Qué harás después de clase?"
        "Hablar con Joel":
            $ afinidad_joel += 1
            pjo "¿Tienes dudas? Siempre puedes escribirme por correo o consultarme directamente."
        "Hablar con Cristian":
            $ afinidad_cristian += 1
            pcr "Mucho gusto, ¿has programado alguna vez antes?"
        "Salir rápido con Matías":
            $ afinidad_matias += 1
            show matias_doodle at left with fade
            mat "¡Vamos a ver si hay comida gratis por ahí!"

    scene entrada_1_borroso with fade
    "La primera semana pasa rápido. Te adaptas, conoces los pasillos y a tus compañeros."
stop music fadeout 1.0
scene resumen_semana with fade
play music "Resumen_progreso.mp3" fadein 1.0

"Resumen de tu primera semana universitaria:"

# Afinidades
if afinidad_diego >= 2:
    "Te estás llevando bien con Diego. Podría ser un gran apoyo académico."
elif afinidad_diego == 1:
    "Conociste a Diego. Aún falta fortalecer ese vínculo."
if genero == "femenino":
    $ final_oa = "a"
else:
    $ final_oa = "o"
if afinidad_matias >= 2:
    "Matías ya te considera su compañer[final_oa] de carrete."
elif afinidad_matias == 1:
    "Hablaste un poco con Matías. ¿Será buena influencia?"

if afinidad_cristian >= 2:
    "Cristian te ve como un estudiante con potencial."
elif afinidad_cristian == 1:
    "Cristian te ha notado. Quizás le interese tu progreso."

if afinidad_joel >= 1:
    "Joel recuerda tu participación en clases."
else:
    "Aún no has interactuado con Joel."

# Estadísticas generales
if exploracion >= 1:
    "Has comenzado a explorar el campus por tu cuenta."

if independencia >= 1:
    "Mostraste independencia en tus decisiones."

if academia >= 2:
    "Tu enfoque académico ha sido fuerte esta semana."
elif academia == 1:
    "Tu enfoque académico ha sido moderado. Podrías mejorar."
else:
    "No has dado mucha prioridad a los estudios aún."

if energia <= 2:
    "Debes cuidar tu energía. Las semanas siguientes serán más exigentes."

"Tu historia recién comienza... pero ya estás formando tu camino."

call screen resumen_barras

return  # O jump semana_2 si la continúas
