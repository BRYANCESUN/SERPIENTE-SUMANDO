
#pantalla
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_FONDO = (144, 238, 144)
FPS = 60
FONDO_DE_PANTALLA = "tiles/tile1.png" #cambiar el numero (1 al 5) para cambiar el fondo de pantalla


# Constantes personaje
ALTURA_PERSONAJE = 10 # siempre debe ser igual al tamaño de la manzana y a lo que avanza la serpiente en cada paso
ANCHURA_PERSONAJE = 10 # siempre debe ser igual al tamaño de la manzana y a lo que avanza la serpiente en cada paso
COLOR_PERSONAJE = (255, 0, 0)
RETRASO_MOVIMIENTO = 80  # milisegundos entre cada paso (más bajo = más rápido) es como la velocidad del personaje

# Constantes manzana
ALTURA_MANZANA = 10
ANCHURA_MANZANA = 10 
COLOR_MANZANA = (0, 200, 0)  # verde, para que se distinga de la serpiente roja
IMAGEN_MANZANA = "frutas/fruta12.png"  # cambiar el numero (1 al 12) para cambiar la fruta

#puntaje (score)
PUNTAJE_POSICION = (700, 10)  # coordenadas donde se dibuja el puntaje en la pantalla
PUNTAJE_INICIAL = 0  # la serpiente empieza con 3 bloques
FUENTE_PUNTAJE = ("TAHOMA", 20)  # fuente y tamaño del texto del puntaje
COLOR_PUNTAJE = (255, 127, 0)  # color del texto del puntaje (naranja)

#audio
MUSICA_FONDO = "sonidos/fondo1.mp3"   # música que suena todo el juego
SONIDO_COMER = "sonidos/comer.wav"    # suena al comer una manzana
SONIDO_MUERTE = "sonidos/muerte.wav"  # suena al perder
VOLUMEN_MUSICA = 0.3  # de 0.0 minimo es decir no se eschucha y 1.0 máximo es lo mas fuerte
VOLUMEN_EFECTOS = 0.7

# Constantes de dificultad (velocidad)
REDUCCION_RETRASO = 5   # milisegundos que se le quitan al retraso cada 5 manzanas
RETRASO_MINIMO = 20     # retraso más bajo permitido la serpiente ya no acelera más