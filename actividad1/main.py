import pygame
import constantes
from personaje import personaje
import mundo
from nivel import Nivel, dibujar_texto
 
pygame.init()
 
#se crea la pantalla del juego con este linea de código
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
 
pygame.display.set_caption("JUGANDO SUMANDO")
 
#cargar imagenes del mundo
title_list = []
for x in range(constantes.TILE_TIPES):
    tile_image = pygame.image.load(f"tiles//tile_{x+1}.png")
    tile_image = pygame.transform.scale(tile_image, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
    title_list.append(tile_image)
 
#cordenadas donde se dibujara el personaje (centrado sobre la plataforma)
jugador = personaje(constantes.SPAWN_X, constantes.SPAWN_Y)
 
world_data = [
    [1]
]
 
word = mundo.Mundo()
word.process_data(world_data, title_list)
 
#el nivel guarda la suma, los picos, la plataforma, las vidas y el numero de nivel
nivel = Nivel()
 
#fuentes para los mensajes grandes de la pantalla
fuente_grande = pygame.font.SysFont("Arial", 64, bold=True)
fuente_mediana = pygame.font.SysFont("Arial", 28, bold=True)
 
#estado del juego, puede ser:
#"jugando"  = el jugador puede mover el personaje
#"correcto" = acerto, se muestra el mensaje un momento
#"fallo"    = fallo, se muestra el mensaje un momento
#"gameover" = se acabaron las vidas, se espera a que presione R
estado = "jugando"
#cuenta los frames que lleva el mensaje en pantalla
temporizador = 0
 
#tamaño de la celda de la cuadrícula en píxeles de la pantalla
TAM_CELDA = constantes.TAM_CELDA
def dibujar_grid():
    for x in range (constantes.ANCHO_VENTANA // constantes.TAM_CELDA):
        pygame.draw.line(ventana, constantes.BLANCO, (x * constantes.TAM_CELDA, 0), (x * constantes.TAM_CELDA, constantes.ALTO_VENTANA))
    for y in range (constantes.ALTO_VENTANA // constantes.TAM_CELDA):
        pygame.draw.line(ventana, constantes.COLOR_GRID, (0, y * constantes.TAM_CELDA), (constantes.ANCHO_VENTANA, y * constantes.TAM_CELDA))
 
 
#variables de movimiento
#mover_arriba ahora sirve para SALTAR (tecla W, flecha arriba o espacio)
#mover_abajo sirve para caer mas rapido (tecla S)
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False
 
#controlar el frame rate
reloj =pygame.time.Clock()
 
#se crea un bucle con while para mantener la ventana abierta
#el bucle se mantendra mientras sucesa cualquier tipo de evento, exepto cerrar la ventana con la X
#se utiliza pygame.display.update() para actualizar la pantalla y que se vea el personaje dibujado y todo lo que se vaya agregando a la pantalla
run = True
while run:
 
    #que vaya a 60 FPS
    reloj.tick(constantes.FPS)
 
    ventana.fill(constantes.COLOR_BG)
 
    #la cuadricula queda tapada por el fondo, se deja por si la necesitas despues
    dibujar_grid()
 
    #calcular el movimiento del personaje de lado
    #(para arriba y abajo ya se encarga la gravedad)
    delta_x = 0
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD_PERSONAJE
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD_PERSONAJE
 
    #--- LOGICA DEL JUEGO ---
    if estado == "jugando":
        #mover el personaje (de lado, salto, gravedad y choque con la plataforma)
        jugador.movimiento(delta_x, mover_arriba, mover_abajo, nivel.plataforma)
 
        #revisar si el personaje ya cayo en algun pico
        #resultado puede ser None (todavia no), "correcto", "fallo" o "gameover"
        resultado = nivel.revisar_picos(jugador.forma)
        if resultado != None:
            estado = resultado
            temporizador = constantes.FRAMES_MENSAJE
 
    elif estado == "correcto" or estado == "fallo":
        #se espera un momento con el mensaje en pantalla
        temporizador = temporizador - 1
        if temporizador <= 0:
            #si acerto, pasa al siguiente nivel con una suma nueva
            if estado == "correcto":
                nivel.siguiente_nivel()
            #el personaje vuelve a la plataforma y se sigue jugando
            jugador.reiniciar()
            estado = "jugando"
 
    #--- DIBUJAR (lo que se dibuja al final queda encima de lo demas) ---
    #dibujar el mundo
    word.draw(ventana)
    #dibujar la plataforma y los picos
    nivel.dibujar(ventana)
    #dibujar el personaje
    jugador.dibujar(ventana)
    #dibujar la suma, el nivel y las vidas
    nivel.dibujar_info(ventana)
 
    #mensajes grandes en el centro de la pantalla
    centro = (constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 - 40)
    if estado == "correcto":
        dibujar_texto(ventana, "¡CORRECTO!", fuente_grande, constantes.VERDE, centro)
    elif estado == "fallo":
        dibujar_texto(ventana, "¡Incorrecto! -1 vida", fuente_grande, constantes.ROJO, centro)
    elif estado == "gameover":
        dibujar_texto(ventana, "FIN DEL JUEGO", fuente_grande, constantes.ROJO, centro)
        texto_final = "Llegaste al nivel " + str(nivel.numero) + ". Presiona R para jugar de nuevo"
        dibujar_texto(ventana, texto_final, fuente_mediana, constantes.BLANCO,
                      (constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 + 20))
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #mover el personaje en caso de evento de tocar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            #la tecla ESC cierra el juego
            if event.key == pygame.K_ESCAPE:
                run = False
            #la tecla R empieza una partida nueva cuando ya no quedan vidas
            if event.key == pygame.K_r and estado == "gameover":
                nivel.reiniciar_juego()
                jugador.reiniciar()
                estado = "jugando"
 
            #para cuando se suelte una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
 
    pygame.display.update()
pygame.quit()

