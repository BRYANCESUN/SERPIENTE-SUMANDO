# SERPIENTE-SUMANDO

**Alumno:** Bryan Manuel Alvarado Ramirez
**Materia:** Lógica de Programación — CESUN Universidad
**Docente:** Miguel Angel Cardona Contreras
**Grupo:** 01IDESVA

## Descripción
Proyecto de videojuegos en Python con Pygame para que niños practiquen
sumas sencillas y desarrollen reflejos y habilidad motriz con sus dedos.

## Objetivo general del juego
Resolver correctamente las sumas para avanzar de nivel, cuidando las vidas
del jugador.

## Contenido del repositorio
- `actividad1/`: Jugando Sumando
- `actividad2/`: Snake

## Investigación sobre Pygame

### ¿Qué es Pygame y para qué se utiliza?
Pygame es una librería de Python que sirve para crear juegos simples en 2D. En esencia, es una librería ideal para novatos: es muy útil para los que están empezando a programar, ya que, al usar el lenguaje Python, es muy intuitiva. Pygame surgió alrededor del año 2000, creada por Pete Shinners.

Es una librería de código abierto, es decir, cualquier persona puede usarla y modificar su código según sus necesidades, sin pagar nada. Por eso es muy buena para aprender, ya que no tiene restricciones a la hora de cambiarla.

Pygame se creó con base en otra librería llamada SDL (Simple DirectMedia Layer), que está escrita en lenguaje C. Más que una librería, Pygame funciona como un traductor entre Python y SDL: Python, al ser un lenguaje muy intuitivo, nos sirve para plasmar nuestras ideas, y SDL se encarga del trabajo pesado, que es comunicarse directamente con la computadora para mostrar la ventana y las imágenes, reproducir los sonidos y leer el teclado y el mouse.

### ¿Cómo se relaciona Pygame con los temas vistos en clase?
Pygame, al utilizar Python como base, sirve para aprender e ir reforzando uno por uno los conocimientos adquiridos en clase, como los bucles (`while`), los eventos (`QUIT`), las condicionales (`if/elif/else`), las estructuras de datos (listas/tuplas) y las clases (personaje: serpiente / consumible: manzana). Todo esto lo aprendimos en clase por separado; sin embargo, Pygame nos permite juntar todos los conocimientos que fuimos adquiriendo durante el curso y usarlos en un solo programa, que en este caso es un juego, lo cual es una manera práctica y divertida de aprender. Al realizar el juego, te das cuenta poco a poco de la estructura y de los elementos que debes utilizar en cada paso, y así refuerzas y entiendes más a detalle lo aprendido.

- **While:** es un bucle que se encarga de mantener el juego en funcionamiento, ejecutando todo el código una y otra vez hasta que se termina el bucle con un evento de salida, como darle clic a la X.
- **Eventos:** son las acciones del jugador que el juego detecta, como presionar una tecla o cerrar la ventana (`QUIT`). En mis dos juegos uso las teclas W, A, S, D para mover al personaje.
- **Condicionales (`if`):** sirven para determinar qué pasa cuando se realiza cierta acción. Por ejemplo, si se presiona la tecla W el personaje se mueve; en Snake, si la serpiente toca la manzana, crece; y en Jugando Sumando, si el cuadrado cae en el pico con el resultado correcto, pasa al siguiente nivel, y si no, pierde una vida.
- **Listas:** sirven para guardar varios elementos que van cambiando durante el juego. En Snake, el cuerpo de la serpiente es una lista con la posición de cada bloque, y por eso puede crecer. En Jugando Sumando, guardo en una lista los 10 números de los picos.
- **Tuplas:** sirven para datos que no cambian, como los colores, por ejemplo `(255, 0, 0)` para el rojo.
- **Clases:** sirven para crear al personaje con todas sus características (forma, color, velocidad, tamaño) y sus acciones (moverse, saltar, dibujarse), para después usarlo dentro del bucle principal (`while`).

### ¿Qué significa que Pygame permite "tomar mucho o poco" de la librería?
Pygame, como ya se ha dicho, no es un motor ni un lenguaje para la creación de videojuegos; solo sirve como un puente (traductor) entre el lenguaje Python y SDL, que es una librería de bajo nivel que se encarga de comunicarse con la computadora. En términos sencillos, un motor como Unity ya viene armado con todo para crear videojuegos, mientras que Pygame solo es una caja de herramientas con las funciones básicas, sin toda la capacidad ni las propiedades de un motor.

Sabiendo lo anterior, tomar mucho o poco significa que Pygame está dividido en módulos (por ejemplo, `display` para la ventana, `draw` para dibujar, `image` para las imágenes, `mixer` para el sonido y `font` para los textos), y yo elijo cuáles usar según lo que necesite mi juego. Por ejemplo, en Snake tomé mucho, porque usé sonidos, imágenes y sprites; en Jugando Sumando tomé menos, porque no tiene sonido y los picos los dibujé con figuras. Así, Pygame se concentra más en la eficiencia y la ligereza que en ser un motor completo y pesado.

Esta misma idea la aplico al organizar mi código: lo divido en varios archivos según mis preferencias (`main.py`, `constantes.py`, `personaje.py`, etc.), para que sea más fácil darle mantenimiento.

En términos sencillos, si un motor de videojuegos como Unity es un auto deportivo, Pygame sería un carrito de golf: sirven para lo mismo, pero con diferente capacidad.

### Nota sobre pygame-ce
En este proyecto se utiliza la versión comunitaria de Pygame (pygame-ce), ya que al tratar de instalar la librería normal mandaba un error: tengo instalado Python 3.14 y Pygame todavía no es compatible con esa versión, pero pygame-ce sí. Es básicamente la misma librería, con todas sus funciones y herramientas, pero es compatible porque la comunidad le da mantenimiento constante. Además, en el código se sigue escribiendo `import pygame`, así que no tuve que cambiar nada.

**Fuentes:**
- https://www.pygame.org/docs/
- https://pyga.me/

