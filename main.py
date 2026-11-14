# Example file showing a basic pygame "game loop"
import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True

FONDOS = []
for i in range(1, 11):
    IMAGEN_ORIGINAL = pygame.image.load(f"MEDIA/IMG{i}.PNG")
    FONDO = pygame.transform.scale(IMAGEN_ORIGINAL, (960, 540))
    FONDOS.append(FONDO)

INDICE = 0
DURACION = 3000 # milisegundos que dura cada fondo ,cada 1000 es 1 segundo como referencia
ULTIMO_CAMBIO = pygame.time.get_ticks()

pygame.mixer.music.load("MEDIA/AUD2.WAV")
pygame.mixer.music.play(-1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    AHORA = pygame.time.get_ticks()
    if AHORA - ULTIMO_CAMBIO >= DURACION:
        INDICE = (INDICE + 1) % len(FONDOS)
        ULTIMO_CAMBIO = AHORA

    FONDO = FONDOS[INDICE]

    # RENDER YOUR GAME HERE
    screen.blit(FONDO, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
