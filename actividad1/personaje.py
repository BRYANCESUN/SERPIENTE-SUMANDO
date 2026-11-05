import pygame
import constantes
 
#se que la forma del personaje (renctangulo) con pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
#se dibuja el personaje y su color con: pygame.draw.rect(ventana, (255,255,0), self.forma)
class personaje ():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE,
                                 constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
 
        #velocidad vertical: si es negativa sube, si es positiva baja
        self.vel_y = 0
        #True cuando el personaje esta parado sobre la plataforma
        self.en_suelo = False
 
    #regresa al personaje al centro de la plataforma
    def reiniciar(self):
        self.forma.center = (constantes.SPAWN_X, constantes.SPAWN_Y)
        self.vel_y = 0
        self.en_suelo = False
 
    #delta_x = cuanto se mueve de lado (teclas A y D)
    #saltar = True si se esta presionando la tecla de salto
    #bajar = True si se esta presionando la tecla S
    #plataforma = el rectangulo donde el personaje se puede parar
    def movimiento(self, delta_x, saltar, bajar, plataforma):
        #mover de lado
        self.forma.x = self.forma.x + delta_x
 
        #que no se salga de la pantalla por los lados
        if self.forma.left < 0:
            self.forma.left = 0
        if self.forma.right > constantes.ANCHO_VENTANA:
            self.forma.right = constantes.ANCHO_VENTANA
 
        #saltar: solo si esta parado sobre la plataforma
        if saltar == True and self.en_suelo == True:
            self.vel_y = constantes.POTENCIA_SALTO
 
        #la gravedad hace que la velocidad vaya aumentando hacia abajo
        self.vel_y = self.vel_y + constantes.GRAVEDAD
 
        #con la tecla S en el aire cae mas rapido
        if bajar == True and self.en_suelo == False:
            self.vel_y = self.vel_y + constantes.GRAVEDAD
 
        #se guarda donde estaba la parte de abajo del personaje antes de moverlo
        parte_baja_anterior = self.forma.bottom
 
        #mover el personaje hacia arriba o hacia abajo
        self.forma.y = self.forma.y + self.vel_y
        self.en_suelo = False
 
        #revisar si el personaje cayo sobre la plataforma
        #tiene que cumplir 3 cosas: va cayendo, venia desde arriba de la plataforma
        #y esta encima de ella (no a un lado)
        va_cayendo = self.vel_y >= 0
        venia_de_arriba = parte_baja_anterior <= plataforma.top
        ya_la_toco = self.forma.bottom >= plataforma.top
        esta_encima = self.forma.right > plataforma.left and self.forma.left < plataforma.right
        if va_cayendo and venia_de_arriba and ya_la_toco and esta_encima:
            #se coloca justo encima de la plataforma y se detiene
            self.forma.bottom = plataforma.top
            self.vel_y = 0
            self.en_suelo = True
 
        #el techo de la pantalla detiene al personaje
        if self.forma.top < 0:
            self.forma.top = 0
            self.vel_y = 0
 
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, constantes.COLOR_PERSONAJE, self.forma)
        #borde negro para que se vea bien sobre el fondo azul claro
        pygame.draw.rect(ventana, constantes.NEGRO, self.forma, 2)