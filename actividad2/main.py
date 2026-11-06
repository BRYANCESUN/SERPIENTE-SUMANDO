import pygame
import constantes
from manzana import Manzana 
from personaje import Personaje

jugador = Personaje() #posicion inicial del personaje
manzana = Manzana(jugador.forma) #posicion inicial de la manzana basada en la serpiente

pygame.init()


pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) #genera la pantalla del juego con las dimensiones definidas en constantes.py
puntaje_manzanas = pygame.font.SysFont(constantes.FUENTE_PUNTAJE[0], constantes.FUENTE_PUNTAJE[1])

imagen_original = pygame.image.load(constantes.FONDO_DE_PANTALLA)  #sirve para cargar la imagen de fondo del juego desde el archivo especificado en constantes.py (son archivos png llamados tile1.png, tile2.png, etc.)

Fondo = pygame.transform.scale(imagen_original, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) #sirve para escalar la imagen al tamaño de la ventana para que encaje correctamente como fondo

pygame.display.set_caption("Snake") #sirve para establecer el título de la variable pantalla

reloj = pygame.time.Clock()  # Creo un objeto reloj para controlar el frame rate

pygame.mixer.music.load(constantes.MUSICA_FONDO)  # carga la música de fondo
pygame.mixer.music.set_volume(constantes.VOLUMEN_MUSICA)
pygame.mixer.music.play(-1)  # -1 significa que se repite para siempre

sonido_comer = pygame.mixer.Sound(constantes.SONIDO_COMER)  # carga el efecto de comer
sonido_comer.set_volume(constantes.VOLUMEN_EFECTOS)
sonido_muerte = pygame.mixer.Sound(constantes.SONIDO_MUERTE)  # carga el efecto de morir
sonido_muerte.set_volume(constantes.VOLUMEN_EFECTOS)

# Bucle principal del juego donde se manejarán los eventos y se actualizará la pantalla
# todos los eventos mantendrán el juego en ejecución hasta que se cierre la ventana con la 'X'
run = True
while run:

    #variable que controla el movimiento del jugador
    jugador.movimiento() #mover al jugador con la variable (movimiento) definida en el archivo personaje.py
    pantalla.fill(constantes.COLOR_FONDO)  # para que sirve .fill: llena la pantalla con el color especificado (en este caso verde) antes de dibujar los elementos del juego
    pantalla.blit(Fondo, (0, 0))  # Dibujo la imagen de fondo en la pantalla
    jugador.dibujar(pantalla) # Dibujo el personaje en la pantalla
    manzana.dibujar(pantalla)  # dibuja la manzana

    # si la cabeza de la serpiente está en la misma posición que la manzana, se la come
    if jugador.forma[0] == manzana.posicion:
        jugador.add = True               # le avisa al personaje que debe crecer
        manzana.reubicar(jugador.forma)  # la manzana aparece en otro lugar
        sonido_comer.play()  # reproduce el sonido de comer
        manzanas_comidas = len(jugador.forma) - 2  #cuántas manzanas lleva comidas
        if manzanas_comidas % 5 == 0:              # NUEVO: cada 5 manzanas
            jugador.retraso = max(jugador.retraso - constantes.REDUCCION_RETRASO, constantes.RETRASO_MINIMO)  # NUEVO: acelera

    for event in pygame.event.get(): # Recorremos todos los eventos que ocurren en la ventana para mantener el bucle en ejecución
        if event.type == pygame.QUIT: # Si se detecta el evento de cerrar la ventana, se termina el bucle y cambia la variable 'run' a False
            run = False

        # movimiento del personaje basado en las teclas presionadas (w, a, s, d) con restricciones para evitar que se mueva en la dirección opuesta inmediata 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                jugador.movimiento_up()
            elif event.key == pygame.K_s:
                jugador.movimiento_down()
            elif event.key == pygame.K_a:
                jugador.movimiento_left()
            elif event.key == pygame.K_d:
                jugador.movimiento_right()

    # Verifico si el jugador ha muerto (por chocar con los bordes o consigo mismo esto se establece en la función muerte() del archivo personaje.py)
    if jugador.muerte():
        pygame.mixer.music.stop()          # detiene la música de fondo
        sonido_muerte.play()               # suena el efecto de muerte
        pygame.time.delay(1000)
        run = False
    #puntaje del jugador basado en la cantidad de manzanas comidas
    puntaje = len(jugador.forma) - 3  # la serpiente empieza con 3 bloques
    texto = puntaje_manzanas.render("Puntaje: {}".format(constantes.PUNTAJE_INICIAL + puntaje), 1, constantes.COLOR_PUNTAJE) # Renderizo el texto del puntaje con color blanco
    pantalla.blit(texto, constantes.PUNTAJE_POSICION) #cordenadas donde se dibuja el puntaje en la pantalla
    pygame.display.update() # Actualizo la pantalla para reflejar los cambios realizados en cada iteración del bucle
    reloj.tick(constantes.FPS)  #sirve para llamar al método tick del reloj y controlar la velocidad de actualización del juego

pygame.quit()