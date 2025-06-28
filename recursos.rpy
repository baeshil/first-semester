###### Personajes de la Historia (SOLO DEFINIDOS, LUEGO TENDRAN COLORES, y sprites.) #####
define die = Character ("Diego")
define mat = Character ("Matías")
define pjo = Character ("Profe Joel")
define pcr = Character ("Profe Cristian")

##### BACKGROUNDS #####
image intro = "images/bg/fotopmintro.png"

# Variables base del jugador
default nombre = "Estudiante"
default genero = ""  # El jugador elegirá entre 'masculino' o 'femenino'

# Pronombres y adjetivos adaptables según género
default bienvenida = ""
default nervio = ""
default emocion = ""
default sola_solo = ""
default tranquila_tranquilo = ""

# Afinidades con personajes principales
default afinidad_diego = 0
default afinidad_matias = 0
default afinidad_cristian = 0
default afinidad_joel = 0

# Estadísticas generales
default exploracion = 0
default independencia = 0
default academia = 0
default energia = 5
default responsabilidad = 0
default impulsividad = 0

# Flags o marcadores de ruta
default flag_cristian_preocupado = False
