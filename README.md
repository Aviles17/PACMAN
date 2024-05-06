
# PACMAN - Analisis de Algoritmos
<p align="center">
  <img src="https://www.javeriana.edu.co/recursosdb/20129/601896/escudo-footer.png" width="200"/>
</p>

[![Build Status](https://img.shields.io/pypi/pyversions/pybit)](https://www.python.org/downloads/)

## Descripción
El proyecto Pacman AI, significando Inteligencia Artificial, desarrollado para la clase de Análisis de Algoritmos de la Pontificia Universidad Javeriana es una implementación del famoso juego de los años 80, que tiene como propósito el analizar diferentes algoritmos asociados a una de sus características mas reconocida, el mapa o laberinto donde el juego se desarrolla. Para el propósito de la clase, siendo este el realizar un análisis exhaustivo sobre ciertas rutinas bajo ciertos contextos, nuestro proyecto inicia desde la pregunta:

**¿Cómo pueden las entidades dentro del juego conocer el camino más optimo a alguna ubicación especifica dentro del laberinto?**

## Objetivos

- Desarrollar o usar una implementación del juego Pacman
- Crear un grafo dirigido que copie el mapa del juego Pacman
- Implementar el **algoritmo de Dijkstra** para encontrar el comino más corto con base al grafo creado anteriormente
- Implementar la heurística de **Distancia Manhattan** con el algoritmo de **A***
- Generar un reporte que compare ambos algoritmos donde se incluya tiempo de ejecución y nodos visitados

## Hoja de Ruta
### Selección de tecnologias
Para el desarrollo del proyecto siguiendo los objetivos lo primero es tomar la decisión entre usar una implementación del juego ya hecha o crear una propia. Después de una investigación se llego a la conclusión que, aunque existen muchas opciones, estas son muy específicas y puede llegar a ser difícil llegar a trabajar de forma interoperable con estas, debido a esto se decidió crear la aplicación desde cero.

Ahora, ya que el objetivo del proyecto no es la creación de un juego como tal, sino solo el análisis de los algoritmos seleccionados. La interfaz grafica (GUI) que se muestra en el repositorio es demasiado minimalista, llegando hasta a ser incompleta. De la misma forma, la lógica del juego también llega a estar incompleta debido a este mismo factor.

Se uso la biblioteca `turtle` que es reconocida por su uso para dibujar figuras de forma rápida y eficientemente. No se uso la famosa biblioteca `pygame` debido a los objetivos y análisis expresado anteriormente, además de una limitante en tiempo.

### Crear Laberinto con Turtle
Para la creación de los mapas donde se desempeñará nuestro análisis se creó un algoritmo el cual es capaz de convertir una matriz a un mapa visual, esto se hace a través de tres simples instrucciones que funcionan como los bloques de construcción dentro del algoritmo. Los valores son los siguientes: *0* : Implica un espacio vacío, *1* : Implica un bloque solido horizontal, *2* : Implica un bloque solido vertical.

<p align="center">
  <img src="https://github.com/Aviles17/PACMAN/assets/110882455/d0df2e02-3d55-4da8-92f6-d7b3763263e7" width="400" hspace="20" />
  <img src="https://github.com/Aviles17/PACMAN/assets/110882455/5bbe0a08-53f5-4a80-925c-5c66b6e3e58b" width="300" hspace="20" />
</p>

### Laberinto como un grafo
Para poder generar un grafo a partir de los elementos visuales ya creado se toma como ventaja el ya tener una estructura guardada con la *meta-data* del mapa, ya que con esta podemos conocer las esquinas y aristas del mapa. Bajo esta información es donde se ubican los nodos del grafo dirigido, ya que siempre que el jugador o la IA tome una decisión de tomar otra dirección va a ser un nodo. Una vez creados los nodos solo es crear las conexiones, las cuales son bidireccionales y repetibles, y guardar la estructura para futuro uso.

<p align="center">
  <img src="https://github.com/Aviles17/PACMAN/assets/110882455/ac8c4747-71a6-42d1-928b-6f36d7f1ec98" width="300" hspace="20" />
  <img src="https://github.com/Aviles17/PACMAN/assets/110882455/f56aa4ef-a09b-49d5-b22e-901ab63af77a" width="300" hspace="20" />
</p>


### Algoritmos Seleccionados
Los algoritmos implementados para el analisis, los cuales estan incluidos dentro del repositorio, son el Algoritmo de camino mas corto o Algoritmo de Dijkstra y el algoritmo de A* que funciona con la hueristica Distancia Manhattan.

El **algoritmo de Dijkstra** es uno de los mas famosos en cuanto a grafos se refiere. Basicamente es un algortimo que usa las cragas de cada unas de las conexiones para determinar el camino mas corto a escoger.

El **algoritmo A* ** es similar a un algoritmo voraz, dispone de dos posiciones en una estructura como un grafo o árbol y determina el camino de dos nodos, los cuales toma como parámetros de entrada. Es un proceso volátil, pues puede encontrar la solución a un problema, pero no da ninguna garantía de su efectividad o de si lo hará en primer lugar. (Salhi, 2017)

## Inició Rapido
Para instalar todas las bibliotecas necesarias para el proyecto necesitas utilizar Python 3.9 preferiblemente o Python 3.10.

Utilizando la herramienta `pip` se pueden instalar todas las dependencias del proyecto. 
```
cd PACMAN
pip install -r requirements.txt
```

### Guia de Uso
Para la ejecución del proyecto es necesario e imperativo hacer uso correcto de las opciones de ejecución, ya que de lo contrario la salida del código será ` Cantidad de argumentos digitados no existen dentro del sistema`.

| Opción | Valores que toma |
|----------|----------|
| -g  | Hace referencia al modo del juego, en este caso se puede seleccionar entre 3 modos, *d* : Algoritmo de Dijkstra (Utiliza el algoritmo para reccorrer el mapa), *m*: Algoritmo A* (Utiliza el algoritmo para reccorrer el mapa), *s*: Juego Libre   |
| -m   | Seleccionar alguno de los mapas presentes en el script Mapas.py (Opciones [B,C,E])   |
| -e  | Valor que puede ser 1 o 0, reportando si el usuario quiere un reporte al final de la ejecución  |

Por lo que una ejecución normal del proyecto se vera de la siguiente forma:
```
cd PACMAN
Pacman.py -g d -m E -e 1
```

## Autores
<table>
  <tr>
<td align="center"><a href="https://github.com/Aviles17"><img src="https://avatars.githubusercontent.com/u/110882455?v=4" width="100px;" alt=""/><br /><sub><b>Santiago Avilés</b></sub></a><br /></td>
<td align="center"><a href="https://github.com/CesarMaldonado14"><img src="https://avatars.githubusercontent.com/u/110882173?v=4" width="100px;" alt=""/><br /><sub><b>César Maldonado</b></sub></a><br /></td>
  </tr>
</table>

## Referencias
Salhi, S (2017) Heuristic Search: The Emerging Science of Problem Solving. Palgrave Macmillan Cham. Recuperado de: https://books.google.com.co/books?
