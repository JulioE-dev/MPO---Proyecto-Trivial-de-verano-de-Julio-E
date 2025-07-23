# MENSAJES DE BIENVENIDA
print("¡Bienvenidos al Trivial de verano de Julio E.!")
print("En este Trivial podrás elegir entre un TRIVIAL GENERAL o categorías como CINE, MUNDO GAMER, DJS Y MÚSICA ELECTRONICA o TECONOLOGÍA")
print("Al finalizar, veremos la nota que sacaste")
print("Buena Suerte, Champion! Demuestranos tus conocimientos!")

# PREGUNTAS DEL TRIVIAL GENERAL


def cargar_preguntas_TRIVIAL_GENERAL():
    print("#########################################")
    print("HAS ELEGIDO EL TRIVIAL DE CULTURA GENERAL!\nVAMOS A VER QUÉ TAL ANDAS DE CULTURA!!")
    print("#########################################")
    return [
        {
            "pregunta": "¿Cuál es el país más grande del mundo en superficie?",
            "opciones": ["A. China", "B. Rusia", "C. Canadá", "D. Estados Unidos"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿En qué año llegó el ser humano a la Luna por primera vez?",
            "opciones": ["A. 1965", "B. 1969", "C. 1972", "D. 1959"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el idioma más hablado en el mundo por número de hablantes nativos?",
            "opciones": ["A. Español", "B. Inglés", "C. Árabe", "D. Chino mandarín"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Quién pintó la obra 'La última cena'?",
            "opciones": ["A. Miguel Ángel", "B. Rafael", "C. Leonardo da Vinci", "D. Van Gogh"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el símbolo químico del oro?",
            "opciones": ["A. Ag", "B. Au", "C. Gd", "D. O"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es la capital de Australia?",
            "opciones": ["A. Sídney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué parte del cuerpo humano produce insulina?",
            "opciones": ["A. Hígado", "B. Estómago", "C. Páncreas", "D. Riñón"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["A. Julio Cortázar", "B. Gabriel García Márquez", "C. Mario Vargas Llosa", "D. Pablo Neruda"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuántos planetas tiene el sistema solar?",
            "opciones": ["A. 7", "B. 8", "C. 9", "D. 10"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el océano más grande del mundo?",
            "opciones": ["A. Atlántico", "B. Índico", "C. Antártico", "D. Pacífico"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Qué día se celebra el Día Internacional de la Mujer?",
            "opciones": ["A. 5 de mayo", "B. 8 de marzo", "C. 25 de noviembre", "D. 10 de octubre"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿En qué país se encuentran las ruinas de Machu Picchu?",
            "opciones": ["A. México", "B. Bolivia", "C. Perú", "D. Ecuador"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué instrumento mide los terremotos?",
            "opciones": ["A. Anemómetro", "B. Sismógrafo", "C. Termómetro", "D. Barómetro"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el metal más ligero?",
            "opciones": ["A. Litio", "B. Aluminio", "C. Sodio", "D. Titanio"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
            "opciones": ["A. Thomas Jefferson", "B. George Washington", "C. Abraham Lincoln", "D. John Adams"],
            "respuesta_correcta": "B"
        },

    ]

# PREGUNTAS DEL TRIVIAL DE CINE


def cargar_preguntas_CINE():
    print("##############################")
    print("HAS ELEGIDO LA CATEGORÍA CINE!\nVEAMOS QUÉ SABES DE CINE, CHAMPION!!")
    print("##############################")
    return [
        {
            "pregunta": "¿Cuál es el nombre del androide interpretado por Ian Holm en la película 'Alien' (1979)?",
            "opciones": ["A. Bishop", "B. Ash", "C. David", "D. Walter"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué director es responsable de la trilogía 'The Dark Knight'?",
            "opciones": ["A. Zack Snyder", "B. Christopher Nolan", "C. Tim Burton", "D. Joss Whedon"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿En qué película de ciencia ficción Tom Cruise queda atrapado en un bucle temporal enfrentando una invasión alienígena?",
            "opciones": ["A. Oblivion", "B. La Guerra de los Mundos", "C. Al Filo del Mañana", "D. Minority Report"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué actriz interpretó a Laurie Strode en la franquicia 'Halloween'?",
            "opciones": ["A. Neve Campbell", "B. Sigourney Weaver", "C. Jamie Lee Curtis", "D. Linda Blair"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué superhéroe del MCU usa un martillo llamado Mjolnir?",
            "opciones": ["A. Capitán América", "B. Thor", "C. Iron Man", "D. Hulk"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el nombre del asesino enmascarado en 'Viernes 13'?",
            "opciones": ["A. Michael Myers", "B. Freddy Krueger", "C. Jason Voorhees", "D. Leatherface"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué actor interpretó a Wolverine en la mayoría de las películas de X-Men?",
            "opciones": ["A. Hugh Jackman", "B. Chris Hemsworth", "C. Ryan Reynolds", "D. Tom Hardy"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué película de terror popularizó la técnica de cámara en mano con estilo 'documental' en 1999?",
            "opciones": ["A. Actividad Paranormal", "B. El Proyecto de la Bruja de Blair", "C. REC", "D. Cloverfield"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿En 'The Matrix', qué pastilla elige tomar Neo?",
            "opciones": ["A. Azul", "B. Verde", "C. Roja", "D. Amarilla"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál de estos personajes NO pertenece al universo Marvel?",
            "opciones": ["A. Spider-Man", "B. Wonder Woman", "C. Doctor Strange", "D. Black Panther"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Quién interpretó al *JOKER* en la película *The Dark Knight*?",
            "opciones": ["A. Jack Nicholson", "B. Heath Andrew Ledger", "C. Jared Leto", "D. Mark Hamill"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué elemento es la debilidad de Superman?",
            "opciones": ["A. Vibranium", "B. Kryptonita", "C. Adamantium", "D. Grafeno"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cómo se llama el alienígena simbionte que se une a Eddie Brock?",
            "opciones": ["A. Carnage", "B. Venom", "C. Riot", "D. Anti-Venom"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es la famosa frase de *Terminator* que dice Arnold Schwarzenegger en *Terminator 2 El Juicio Final*?",
            "opciones": ["A. Say hello to my little friend", "B. I'll be back", "C. Get to the chopper!", "D. Sayonara Baby!"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Qué película de ciencia ficción se desarrolla en el planeta Arrakis?",
            "opciones": ["A. Star Wars", "B. Avatar", "C. Dune", "D. Interstellar"],
            "respuesta_correcta": "C"
        },

    ]

# PREGUNTAS DEL TRIVIAL DE MUNDO GAMER


def cargar_preguntas_MUNDO_GAMER():
    print("####################################")
    print("HAS ELEGIDO LA CATEGORÍA MUNDO GAMER!\nVEAMOS SI ERES UN PROPLAYER O UN NOOB!!")
    print("####################################")
    return [
        {
            "pregunta": "¿Cuál es el personaje principal de la saga The Legend of Zelda?",
            "opciones": ["A. Zelda", "B. Link", "C. Ganon", "D. Epona"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿En qué videojuego aparece por primera vez Mario Bros?",
            "opciones": ["A. Super Mario Bros", "B. Donkey Kong", "C. Mario Kart", "D. Mario Party"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál de estos juegos fue desarrollado por Mojang?",
            "opciones": ["A. Terraria", "B. Roblox", "C. Minecraft", "D. Fortnite"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué tipo de juego es League of Legends?",
            "opciones": ["A. RPG", "B. MOBA", "C. FPS", "D. Simulador"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué empresa desarrolló la consola PlayStation?",
            "opciones": ["A. Microsoft", "B. Nintendo", "C. Sega", "D. Sony"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Cuál es el nombre del protagonista de la saga Halo?",
            "opciones": ["A. Master Chief", "B. Marcus Fenix", "C. Samus Aran", "D. Commander Shepard"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué empresa desarrolló la consola GameBoy?",
            "opciones": ["A. Microsoft", "B. Nintendo", "C. Sega", "D. Sony"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál de estos juegos es exclusivo de Nintendo?",
            "opciones": ["A. God of War", "B. Forza Horizon", "C. Super Smash Bros", "D. Halo"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿En qué ciudad se desarrolla principalmente Grand Theft Auto: Vice City?",
            "opciones": ["A. Liberty City", "B. Los Santos", "C. Vice City", "D. San Fierro"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué color es el logo principal de Steam?",
            "opciones": ["A. Rojo", "B. Verde", "C. Azul", "D. Negro"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el nombre del villano principal en la saga 'The Legend of Zelda'?",
            "opciones": ["A. Bowser", "B. Ganon", "C. Ridley", "D. Sephiroth"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué videojuego popularizó el modo Battle Royale?",
            "opciones": ["A. Call of Duty", "B. Fortnite", "C. PUBG", "D. Apex Legends"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué compañía desarrolló el juego 'The Witcher 3: Wild Hunt'?",
            "opciones": ["A. Ubisoft", "B. Bethesda", "C. Rockstar Games", "D. CD Projekt Red"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿En qué año se lanzó la consola PlayStation 5?",
            "opciones": ["A. 2018", "B. 2019", "C. 2020", "D. 2021"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué juego es conocido por la frase 'Finish Him!'?",
            "opciones": ["A. Tekken", "B. Street Fighter", "C. Mortal Kombat", "D. Killer Instinct"],
            "respuesta_correcta": "C"
        }

    ]

# PREGUNTAS DEL TRIVIAL DE DJS Y MÚSICA ELECTRÓNICA


def cargar_preguntas_MÚSICA():
    print("#################################################")
    print("HAS ELEGIDO LA CATEGORÍA DJS Y MÚSICA ELECTRÓNICA!\nVEAMOS SI ERES MÁS DEL FARY O DE MULERO!!")
    print("#################################################")
    return [
        {
            "pregunta": "¿Quién es considerado el 'padre del techno' de Detroit?",
            "opciones": ["A. Carl Cox", "B. Kevin Saunderson", "C. Derrick May", "D. Jeff Mills"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué DJ es famoso por usar una cabeza de ratón como casco?",
            "opciones": ["A. Marshmello", "B. Daft Punk", "C. Deadmau5", "D. Steve Aoki"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué festival de música electrónica es conocido por su sede principal en Bélgica?",
            "opciones": ["A. Ultra Music Festival", "B. Tomorrowland", "C. Creamfields", "D. EDC"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué dúo francés ganó un Grammy con el álbum 'Random Access Memories'?",
            "opciones": ["A. Justice", "B. Daft Punk", "C. Disclosure", "D. Galantis"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál de estos DJs es originario de los Países Bajos?",
            "opciones": ["A. Tiësto", "B. Skrillex", "C. David Guetta", "D. Calvin Harris"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué género es característico por su BPM alto y uso de distorsión en los bombos?",
            "opciones": ["A. Trance", "B. House", "C. Hardcore", "D. Chillstep"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué DJ lanzó el tema viral 'Scary Monsters and Nice Sprites'?",
            "opciones": ["A. Skrillex", "B. Marshmello", "C. Diplo", "D. Martin Garrix"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué artista colaboró con Avicii en 'Wake Me Up' como vocalista?",
            "opciones": ["A. Aloe Blacc", "B. David Guetta", "C. Kygo", "D. Zedd"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué festival tiene una edición en México y es parte de la marca EDC?",
            "opciones": ["A. Dreamfields", "B. Tomorrowland", "C. Electric Zoo", "D. Electric Daisy Carnival"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿En qué ciudad nació y reside DJ Julio E?",
            "opciones": ["A. Barcelona", "B. Sevilla", "C. Madrid", "D. Valencia"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿En qué año nació DJ Julio E?",
            "opciones": ["A. 1975", "B. 1980", "C. 1985", "D. 1990"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el nombre del colectivo y netlabel creado por DJ Julio E?",
            "opciones": ["A. Madrid Beats", "B. Abx Sounds Netlabel", "C. Electro Madrid", "D. Getafe Records"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué instrumento de Roland es clave en la creación del Acid House clásico?",
            "opciones": ["A. Roland TR-808", "B. Korg MS-20", "C. Roland TB-303", "D. Moog Sub 37"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué DJ es conocido por lanzar pasteles al público durante sus shows?",
            "opciones": ["A. Steve Aoki", "B. Diplo", "C. Armin van Buuren", "D. Hardwell"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué DJ ganó notoriedad por producir tanto drum & bass como house, techno y funk en España?",
            "opciones": ["A. Ricardo Villalobos", "B. DJ Blass", "C. DJ Julio E", "D. Chancha Vía Circuito"],
            "respuesta_correcta": "C"
        },

    ]

# PREGUNTAS DEL TRIVIAL DE TECNOLOGÍAS


def cargar_preguntas_TRIVIAL_TECNOLOGÍAS():
    print("#######################################")
    print("HAS ELEGIDO LA CATEGORÍA DE TECNOLOGÍAS!\nVEAMOS QUE TAL TE MUEVES EN EL SIGLO XXI!!")
    print("#######################################")
    return [
        {
            "pregunta": "¿Qué etiqueta HTML se utiliza para crear un enlace?",
            "opciones": ["A. <link>", "B. <a>", "C. <href>", "D. <url>"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué atributo se usa en HTML para abrir un enlace en una nueva pestaña?",
            "opciones": ["A. open='new'", "B. target='_blank'", "C. newtab='yes'", "D. mode='external'"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué método de JavaScript se usa para imprimir algo en la consola?",
            "opciones": ["A. print()", "B. echo()", "C. log()", "D. console.log()"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Cuál es el tipo de dato que representa una lista en Python?",
            "opciones": ["A. tuple", "B. dict", "C. list", "D. set"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es la extensión de archivo estándar para archivos HTML?",
            "opciones": ["A. .ht", "B. .html", "C. .xml", "D. .txt"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué protocolo se utiliza comúnmente para enviar correos electrónicos?",
            "opciones": ["A. FTP", "B. SMTP", "C. HTTP", "D. POP3"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué palabra clave en Python se utiliza para definir una función?",
            "opciones": ["A. function", "B. define", "C. def", "D. fun"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué propiedad CSS se usa para cambiar el color del texto?",
            "opciones": ["A. font-color", "B. text-color", "C. color", "D. text-style"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el puerto estándar para HTTP?",
            "opciones": ["A. 20", "B. 21", "C. 80", "D. 443"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cómo se representa un diccionario en Python?",
            "opciones": ["A. [ ]", "B. ( )", "C. { }", "D. < >"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué función de JavaScript convierte una cadena en entero?",
            "opciones": ["A. parseInt()", "B. int()", "C. toNumber()", "D. convert()"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué es JSON?",
            "opciones": ["A. Un lenguaje de programación", "B. Un protocolo de red", "C. Un formato de intercambio de datos", "D. Un navegador web"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué comando se usa para instalar paquetes en Python?",
            "opciones": ["A. python install", "B. pip install", "C. pkg install", "D. py get"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál de estos protocolos es seguro para navegación web?",
            "opciones": ["A. HTTP", "B. FTP", "C. HTTPS", "D. SSH"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué operador en JavaScript se usa para comparar valor y tipo?",
            "opciones": ["A. ==", "B. !=", "C. ===", "D. <>"],
            "respuesta_correcta": "C"
        },
    ]

# MOSTRAMOS LA PREGUNTA Y SUS OPCIONES DE RESPUESTA


def mostrar_pregunta(p):
    print("\n" + p["pregunta"])
    for opcion in p["opciones"]:
        print(opcion)

# PEDIMOS AL USUARIO UNA RESPUESTA VÁLIDA (A, B, C o D).


def obtener_respuesta():
    while True:
        r = input("Tu respuesta (A, B, C o D): ").upper()
        if r in ["A", "B", "C", "D"]:
            return r
        print("Respuesta no válida. Intenta de nuevo.")

# EJECUTAMOS EL TRIVIAL DE GENERAL.
# CARGAMOS LAS PREGUNTAS Y LAS MOSTRAMOS AL USUARIO.
# RECOGEMOS SUS RESPUESTAS Y EVALUAMOS SI SON CORRECTAS O NO.
# MOSTRAMOS EL NÚMERO DE ACIERTOS Y UN MENSAJE FINAL PERSONALIZADO SEGÚN EL NÚMERO DE ACIERTOS.


def TRIVIAL_GENERAL():
    preguntas = cargar_preguntas_TRIVIAL_GENERAL()
    aciertos = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if r == p["respuesta_correcta"]:
            print("👍 Correcto")
            aciertos += 1
        else:
            print(f"👎 Incorrecto. Era: {p['respuesta_correcta']}")

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print(f"\nAciertos: {aciertos} de {total} ({porcentaje:.2f}%)")
    if aciertos < 7:
        print("DEJA DE VER LA TV Y EL SMARTPHONE Y LEE ALGÚN LIBRO DE VEZ EN CUANDO! ")
    elif 7 <= aciertos <= 14:
        print("MUY BIEN!! SE NOTA QUE HAS ESTUDIADO!!")
    elif aciertos == 15:
        print("ERES UN AUTÉNTICO ERUDITO, TU LEMA ES: EL SABER NO OCUPA LUGAR!")

# EJECUTAMOS EL TRIVIAL DE CINE.
# CARGAMOS LAS PREGUNTAS Y LAS MOSTRAMOS AL USUARIO.
# RECOGEMOS SUS RESPUESTAS Y EVALUAMOS SI SON CORRECTAS O NO.
# MOSTRAMOS EL NÚMERO DE ACIERTOS Y UN MENSAJE FINAL PERSONALIZADO SEGÚN EL NÚMERO DE ACIERTOS.


def TRIVIAL_CINE():
    preguntas = cargar_preguntas_CINE()
    aciertos = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if r == p["respuesta_correcta"]:
            print("👍 Correcto")
            aciertos += 1
        else:
            print(f"👎 Incorrecto. Era: {p['respuesta_correcta']}")

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print(f"\nAciertos: {aciertos} de {total} ({porcentaje:.2f}%)")
    if aciertos < 7:
        print("NO VES MUCHO CINE, EH! ")
    elif 7 <= aciertos <= 14:
        print("MUY BIEN CONOCES LA MAYORÍA DE LAS PELÍCULAS!!")
    elif aciertos == 15:
        print("ERES UN AUTÉNTICO CINÉFILO, LA VIDA ES UN GRAN PLATÓ ES TU LEMA!")


def TRIVIAL_MUNDO_GAMER():
    preguntas = cargar_preguntas_MUNDO_GAMER()
    aciertos = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if r == p["respuesta_correcta"]:
            print("👍 Correcto")
            aciertos += 1
        else:
            print(f"👎 Incorrecto. Era: {p['respuesta_correcta']}")

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print(f"\nAciertos: {aciertos} de {total} ({porcentaje:.2f}%)")
    if aciertos < 7:
        print("DEBES JUGAR UN POCO MÁS! DILE A MAMI QUE TE COMPRE UNA PLAY Y EL HOBBY CONSOLAS YA!")
    elif 7 <= aciertos <= 14:
        print("MUY BIEN!! AUNQUE TE FALTA UN POCO PARA SER UN PROPLAYER!!")
    elif aciertos == 15:
        print("ERES UN AUTÉNTICO GAMER, PERO SAL A LA CALLE A VIVIR UN POCO!")

# EJECUTAMOS EL TRIVIAL DE DJS Y MÚSICA ELECTRÓNICA.
# CARGAMOS LAS PREGUNTAS Y LAS MOSTRAMOS AL USUARIO.
# RECOGEMOS SUS RESPUESTAS Y EVALUAMOS SI SON CORRECTAS O NO.
# MOSTRAMOS EL NÚMERO DE ACIERTOS Y UN MENSAJE FINAL PERSONALIZADO SEGÚN EL NÚMERO DE ACIERTOS.


def TRIVIAL_MÚSICA():
    preguntas = cargar_preguntas_MÚSICA()
    aciertos = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if r == p["respuesta_correcta"]:
            print("👍 Correcto")
            aciertos += 1
        else:
            print(f"👎 Incorrecto. Era: {p['respuesta_correcta']}")

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print(f"\nAciertos: {aciertos} de {total} ({porcentaje:.2f}%)")
    if aciertos < 7:
        print("DEBES SALIR DE FIESTA UN POCO MÁS! VETE A ALGÚN FESTIVAL YA!")
    elif 7 <= aciertos <= 14:
        print("SE VE QUE TE GUSTA MUCHO LA MÚSICA, MUCHACHO!!")
    elif aciertos == 15:
        print("ERES UN AUTÉNTICO FIESTERO, LA MÚSICA ES VIDA PARA TÍ!")

# EJECUTAMOS EL TRIVIAL DE TECNOLOGÍAS.
# CARGAMOS LAS PREGUNTAS Y LAS MOSTRAMOS AL USUARIO.
# RECOGEMOS SUS RESPUESTAS Y EVALUAMOS SI SON CORRECTAS O NO.
# MOSTRAMOS EL NÚMERO DE ACIERTOS Y UN MENSAJE FINAL PERSONALIZADO SEGÚN EL NÚMERO DE ACIERTOS.


def TRIVIAL_TECNOLOGÍAS():
    preguntas = cargar_preguntas_TRIVIAL_TECNOLOGÍAS()
    aciertos = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        if r == p["respuesta_correcta"]:
            print("👍 Correcto")
            aciertos += 1
        else:
            print(f"👎 Incorrecto. Era: {p['respuesta_correcta']}")

    total = len(preguntas)
    porcentaje = aciertos / total * 100
    print(f"\nAciertos: {aciertos} de {total} ({porcentaje:.2f}%)")
    if aciertos < 7:
        print("LO TUYO NO ES LA TECNOLOGÍA! ¿TE QUEDASTE EN EL MEDIEVO O QUÉ?!")
    elif 7 <= aciertos <= 14:
        print("BIEN! PARECE QUE USAS EL LAPTOP PARA ALGO MÁS QUE PARA VER TU PERFIL DE FACEBOOK, MUCHACHO!!")
    elif aciertos == 15:
        print("ERES UN AUTÉNTICO DEVELOPER! NO HABRÁS ESTUDIADO EN THE POWER, ¿NO?")

# MENÚ DE INICIO
# EL USUARIO PUEDO ELEGIR ENTRE UN TRIVIAA DE CULTURA GENERAL, ELEGIR CATEGORÍA O SALIR DEL JUEGO.
# SI ELIJE CATEGORÍA, MOSTRAMOS OTRO MENÚ CON LAS OPCIONES DE CINE, MUNDO GAMER, DJS Y MÚSICA ELECTRÓNICA O TECNOLOGÍAS.
# SI ELIJE SALIR, MOSTRAMOS UN MENSAJE DE DESPEDIDA Y TERMINAMOS EL PROGRAMA.


def menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - EMPEZAR TRIVIAL DE CULTURA GENERAL")
        print("2 - ELEGIR CATEGORÍA")
        print("3 - SALIR")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            TRIVIAL_GENERAL()
        elif opcion == "2":
            menu_categorias()
        elif opcion == "3":
            print(
                "¡HASTA LUEGO, CHAMPION!\n¡ESPERO QUE HAYAS DISFRUTADO DEL TRIVIAL!\n¡VUELVE CUANDO QUIERAS!")
            break
        else:
            print("OPCIÓN NO VALIDA. POR FAVOR, INTÉNTALO DE NUEVO.")

# MENÚ DE CATEGORÍAS
# EL USUARIO PUEDE ELEGIR ENTRE LAS CATEGORÍAS: CINE, MUNDO GAMER, DJS Y MÚSICA ELECTRÓNICA O TECNOLOGÍAS.
# SI ELIJE UNA CATEGORÍA, EJECUTAMOS EL TRIVIAL CORRESPONDIENTE.
# SI ELIJE VOLVER AL MENÚ ANTERIOR, SALIMOS DEL BUCLE Y VOLVEMOS AL MENÚ PRINCIPAL.


def menu_categorias():
    while True:
        print("\n### MENÚ CATEGORÍAS ###")
        print("1 - CINE")
        print("2 - MUNDO GAMER")
        print("3 - DJS Y MÚSICA ELECTRONICA")
        print("4 - TECNOLOGÍAS")
        print("5 - MENÚ ANTERIOR")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            TRIVIAL_CINE()
        elif opcion == "2":
            TRIVIAL_MUNDO_GAMER()
        elif opcion == "3":
            TRIVIAL_MÚSICA()
        elif opcion == "4":
            TRIVIAL_TECNOLOGÍAS()
        elif opcion == "5":
            break
        else:
            print("OPCIÓN NO VÁLIDA. POR FAVOR, INTÉNTALO DE NUEVO.")


menu()
