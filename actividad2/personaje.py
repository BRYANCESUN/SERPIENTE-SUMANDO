import pygame
import constantes
from pygame import Vector2

class Personaje:
    def __init__(self):
        self.forma = [Vector2(10,100),Vector2(10,110),Vector2(10,120)]
        self.direction = Vector2(0, -10)  # Dirección inicial del personaje (hacia arriba)
        self.ultima_direccion = Vector2(0, -10)  # Dirección del último paso que dio de verdad
        self.add = False
        self.ultimo_movimiento = pygame.time.get_ticks()  # momento del último paso
        self.retraso = constantes.RETRASO_MOVIMIENTO  #retraso  empieza igual que la constante.RETRASO_MOVIMIENTO para luego poder reducirlo según la dificultad

    def dibujar(self, pantalla):
        for bloque in self.forma:
            pygame.draw.rect(pantalla, constantes.COLOR_PERSONAJE, (bloque.x, bloque.y, constantes.ANCHURA_PERSONAJE, constantes.ALTURA_PERSONAJE))

    def movimiento(self):
        ahora = pygame.time.get_ticks()
        # Si todavía no pasa el tiempo de espera, no se mueve en este frame
        if ahora - self.ultimo_movimiento < self.retraso:
            return
        self.ultimo_movimiento = ahora

        if self.add:
            forma_copy = self.forma[:]    # copia todos los bloques del cuerpo (no quita la cola), así crece un bloque
            self.add = False
        else:
            forma_copy = self.forma[:-1]  # quita la cola, así mantiene su tamaño
        forma_copy.insert(0, self.forma[0] + self.direction)
        self.forma = forma_copy
        self.ultima_direccion = self.direction  # guarda hacia dónde se movió realmente

    def cambiar_direccion(self, nueva_direccion):
        # Solo cambia si la nueva dirección NO es la contraria al último paso real
        # (el contrario de un Vector2 es el mismo con signo negativo)
        if nueva_direccion != -self.ultima_direccion:
            self.direction = nueva_direccion

    def movimiento_up(self):
        self.cambiar_direccion(Vector2(0, -10)) #sirve para definir la direccion de movimiento del personaje hacia arriba
    def movimiento_down(self):
        self.cambiar_direccion(Vector2(0, 10)) #sirve para definir la direccion de movimiento del personaje hacia abajo
    def movimiento_left(self):
        self.cambiar_direccion(Vector2(-10, 0)) #sirve para definir la direccion de movimiento del personaje hacia la izquierda
    def movimiento_right(self):
        self.cambiar_direccion(Vector2(10, 0)) #sirve para definir la direccion de movimiento del personaje hacia la derecha

    def muerte(self):
        # Verifica si el personaje ha chocado con los bordes de la ventana y retorna True si es así, indicando que ha muerto para que en main.py se pueda terminar el juego
        if self.forma[0].x >= constantes.ANCHO_VENTANA or self.forma[0].y >= constantes.ALTO_VENTANA or self.forma[0].x < 0 or self.forma[0].y < 0:
            return True
        #si el personaje choca consigo mismo, también se considera muerte
        for i in self.forma[1:]:
            if self.forma[0] == i:
                return True
        return False