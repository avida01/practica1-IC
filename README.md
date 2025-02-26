# A* Pathfinding with Waypoints in Python (Pygame)

Este proyecto implementa un algoritmo de búsqueda A* para encontrar un camino entre un punto de inicio y un objetivo, pasando por varios puntos intermedios (waypoints), en un entorno de cuadrícula. El código está visualizado utilizando la biblioteca Pygame. El vehículo (representado como un rectángulo rojo) sigue el camino encontrado a través de la cuadrícula, y los puntos de paso intermedios se muestran en amarillo.

## Características
- **A* Pathfinding**: Utiliza el algoritmo A* para encontrar el camino más corto entre un punto de inicio y un objetivo, pasando por varios waypoints intermedios.
- **Puntos de paso (waypoints)**: El usuario puede definir puntos intermedios por los que el camino debe pasar antes de llegar al objetivo.
- **Interfaz gráfica**: Usando Pygame, se visualiza la cuadrícula, el camino calculado, los waypoints y el vehículo.
- **Recarga dinámica**: Presionando `Shift + R` se reinicia la cuadrícula y se recalcula el camino.

## Instalación

Para ejecutar este proyecto, necesitas tener Python y la biblioteca Pygame instalados. Si no tienes Pygame, puedes instalarlo usando el siguiente comando:

```bash
pip install pygame
