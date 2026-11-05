import pygame
import random
import constantes
 
#dibuja un texto en la pantalla con una sombra negra para que se lea bien sobre el fondo azul claro
#centro = (x, y) del punto donde queda el centro del texto
def dibujar_texto(ventana, texto, fuente, color, centro):
    sombra = fuente.render(texto, True, constantes.NEGRO)
    ventana.blit(sombra, sombra.get_rect(center=(centro[0] + 2, centro[1] + 2)))
    imagen = fuente.render(texto, True, color)
    ventana.blit(imagen, imagen.get_rect(center=centro))
 
 
#esta clase guarda todo lo de las sumas: la plataforma, los picos, las vidas y el nivel
class Nivel ():
    def __init__(self):
        #la plataforma es un rectangulo (x, y, ancho, alto) puesto en el centro de la pantalla
        x_plataforma = (constantes.ANCHO_VENTANA - constantes.PLATAFORMA_ANCHO) // 2
        self.plataforma = pygame.Rect(x_plataforma, constantes.PLATAFORMA_Y,
                                      constantes.PLATAFORMA_ANCHO,
                                      constantes.PLATAFORMA_ALTO)
 
        #fuentes (tipo y tamaño de letra) para los textos
        self.fuente = pygame.font.SysFont("Arial", 40, bold=True)
        self.fuente_numero = pygame.font.SysFont("Arial", 30, bold=True)
        self.fuente_chica = pygame.font.SysFont("Arial", 26, bold=True)
 
        self.reiniciar_juego()
 
    #empieza una partida nueva: nivel 1 y 3 vidas
    def reiniciar_juego(self):
        self.numero = 1
        self.vidas = constantes.VIDAS_INICIALES
        self.crear_suma()
 
    #sube de nivel y crea una suma nueva
    def siguiente_nivel(self):
        self.numero = self.numero + 1
        self.crear_suma()
 
    #crea una suma y los 10 numeros de los picos (1 correcto y 9 incorrectos)
    def crear_suma(self):
        #los numeros de la suma crecen con el nivel, pero nunca pasan de 10
        maximo = min(5 + self.numero, 10)
        self.num1 = random.randint(1, maximo)
        self.num2 = random.randint(1, maximo)
        self.resultado = self.num1 + self.num2
 
        #lista con las respuestas incorrectas posibles (del 1 al 20, menos la correcta)
        incorrectas = []
        for n in range(1, 21):
            if n != self.resultado:
                incorrectas.append(n)
 
        #se eligen 9 incorrectas al azar y se agrega la correcta
        self.opciones = random.sample(incorrectas, constantes.NUM_PICOS - 1)
        self.opciones.append(self.resultado)
        #se revuelven para que la correcta quede en un pico diferente cada vez
        random.shuffle(self.opciones)
 
    #revisa si el personaje ya toco los picos
    #regresa: None (todavia no), "correcto", "fallo" o "gameover"
    def revisar_picos(self, forma):
        #si la parte de abajo del personaje aun no llega a los picos, no pasa nada
        if forma.bottom < constantes.PUNTA_PICOS_Y + 10:
            return None
 
        #se calcula en cual pico cayo usando el centro del personaje
        numero_pico = forma.centerx // constantes.ANCHO_PICO
        if numero_pico > constantes.NUM_PICOS - 1:
            numero_pico = constantes.NUM_PICOS - 1
 
        if self.opciones[numero_pico] == self.resultado:
            return "correcto"
 
        #si fallo se resta una vida
        self.vidas = self.vidas - 1
        if self.vidas <= 0:
            return "gameover"
        return "fallo"
 
    #dibuja la plataforma y los picos con sus numeros
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, constantes.COLOR_PLATAFORMA, self.plataforma)
        pygame.draw.rect(ventana, constantes.NEGRO, self.plataforma, 2)
 
        for i in range(constantes.NUM_PICOS):
            x = i * constantes.ANCHO_PICO
            #un pico es un triangulo con 3 puntos: izquierda, punta y derecha
            triangulo = [(x + 4, constantes.BASE_PICOS_Y),
                         (x + constantes.ANCHO_PICO // 2, constantes.PUNTA_PICOS_Y),
                         (x + constantes.ANCHO_PICO - 4, constantes.BASE_PICOS_Y)]
            pygame.draw.polygon(ventana, constantes.COLOR_PICO, triangulo)
            pygame.draw.polygon(ventana, constantes.BLANCO, triangulo, 2)
 
            #el numero se escribe arriba de la punta del pico
            centro_numero = (x + constantes.ANCHO_PICO // 2, constantes.PUNTA_PICOS_Y - 22)
            dibujar_texto(ventana, str(self.opciones[i]), self.fuente_numero,
                          constantes.BLANCO, centro_numero)
 
    #dibuja la suma (arriba al centro), el nivel (izquierda) y las vidas (derecha)
    def dibujar_info(self, ventana):
        texto_suma = "¿Cuánto es " + str(self.num1) + " + " + str(self.num2) + "?"
        dibujar_texto(ventana, texto_suma, self.fuente,
                      constantes.BLANCO, (constantes.ANCHO_VENTANA // 2, 50))
        dibujar_texto(ventana, "Nivel " + str(self.numero), self.fuente_chica,
                      constantes.BLANCO, (90, 30))
        dibujar_texto(ventana, "Vidas: " + str(self.vidas), self.fuente_chica,
                      constantes.ROJO, (constantes.ANCHO_VENTANA - 90, 30))