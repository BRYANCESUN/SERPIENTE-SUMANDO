ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ALTO_PERSONAJE = 50
ANCHO_PERSONAJE = 50
FPS = 60
VELOCIDAD_PERSONAJE = 5
TAM_CELDA = 500
TILE_TIPES = 2
 
#FISICA DEL PERSONAJE
GRAVEDAD = 1              # en cada frame la velocidad de caida aumenta en 1
POTENCIA_SALTO = -15      # fuerza del salto (negativo = hacia arriba)
 
#PLATAFORMA (donde empieza el personaje)
PLATAFORMA_ANCHO = 250
PLATAFORMA_ALTO = 20
PLATAFORMA_Y = 200        # altura de la plataforma en la pantalla
 
#PICOS (los que tienen los resultados)
NUM_PICOS = 10
ANCHO_PICO = ANCHO_VENTANA // NUM_PICOS   # cada pico mide 80 px de ancho
ALTO_PICO = 40
BASE_PICOS_Y = ALTO_VENTANA - 20          # altura donde esta la base de los picos
PUNTA_PICOS_Y = BASE_PICOS_Y - ALTO_PICO  # altura donde esta la punta de los picos
 
#POSICION DONDE APARECE EL PERSONAJE (centrado y encima de la plataforma)
SPAWN_X = ANCHO_VENTANA // 2
SPAWN_Y = PLATAFORMA_Y - ALTO_PERSONAJE // 2
 
#REGLAS DEL JUEGO
VIDAS_INICIALES = 3
FRAMES_MENSAJE = 90       # cuanto dura el mensaje en pantalla (90 frames = 1.5 segundos)
 
#COLORES
COLOR_PERSONAJE = (255, 255, 0)  # Color amarillo
COLOR_BG = (0, 0, 20)  # Color negro oscuro
COLOR_GRID = (50, 50, 50)  # Color gris para la cuadrícula
BLANCO = (255, 255, 255)  # Color blanco
NEGRO = (0, 0, 0)  # Color negro
ROJO = (255, 0, 0)  # Color rojo
VERDE = (0, 255, 0)  # Color verde
AZUL = (0, 0, 255)  # Color azul
COLOR_PLATAFORMA = (70, 70, 100)  # Color gris azulado de la plataforma
COLOR_PICO = (30, 30, 120)  # Color azul oscuro de los picos
