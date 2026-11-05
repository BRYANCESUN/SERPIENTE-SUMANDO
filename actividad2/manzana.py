import pygame
import random
import constantes
from pygame import Vector2

class Manzana(pygame.sprite.Sprite):  # la manzana ahora es un Sprite de Pygame
    def __init__(self, cuerpo_serpiente):
        super().__init__()  # inicializa la parte de Sprite (obligatorio)

        # image: el dibujo del sprite (un cuadro de 10x10 pintado de verde)
        imagen_original = pygame.image.load(constantes.IMAGEN_MANZANA)  # carga la imagen de la manzana
        self.image = pygame.transform.scale(imagen_original, (constantes.ANCHURA_MANZANA, constantes.ALTURA_MANZANA))  # la ajusta al tamaño de la manzana

        # rect: el rectángulo que guarda la posición y el tamaño del sprite
        self.rect = self.image.get_rect()

        self.posicion = Vector2(0, 0)
        self.reubicar(cuerpo_serpiente)  # la coloca en un lugar al azar desde el inicio

    def reubicar(self, cuerpo_serpiente):
        # Busca una posición al azar que NO esté encima de la serpiente
        while True:
            x = random.randrange(0, constantes.ANCHO_VENTANA, constantes.ANCHURA_MANZANA)
            y = random.randrange(0, constantes.ALTO_VENTANA, constantes.ALTURA_MANZANA)
            nueva_posicion = Vector2(x, y)

            if nueva_posicion not in cuerpo_serpiente:
                self.posicion = nueva_posicion
                self.rect.topleft = (x, y)  # mueve el rect del sprite a la nueva posición
                return

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)  # dibuja la imagen del sprite en la posición de su rect