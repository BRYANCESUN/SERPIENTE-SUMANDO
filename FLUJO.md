# Flujo de trabajo del repositorio

## Ramas
- **main**: versión estable del proyecto. Solo recibe código probado desde `v01`.
- **v01**: rama de integración. Aquí se juntan y se prueban los avances.
- **actividad1**: juego Jugando Sumando.
- **actividad2**: juego Snake.

## Proceso
1. Cada nueva actividad se crea como rama a partir de `v01`.
2. El código de la actividad se guarda en su propia carpeta (`actividad1/`, `actividad2/`...) para evitar conflictos entre archivos con el mismo nombre.
3. Se hacen commits con mensajes descriptivos en la rama de la actividad.
4. Al terminar, se hace merge de la actividad hacia `v01`.
5. Se prueba que los juegos funcionen en `v01`.
6. Si todo funciona, se hace merge de `v01` hacia `main`.

## Entorno de desarrollo
- Python 3.14 con **pygame-ce** (versión comunitaria de Pygame compatible con Python 3.14).
- Entorno virtual `.venv` (ignorado por Git mediante `.gitignore`).

## Durante el curso
Las siguientes actividades seguirán este mismo flujo (`actividad3`, `actividad4`...)
y `main` siempre tendrá la última versión estable del proyecto.