# Pancakes Profundidad Iterativa

Este programa resuelve el problema de pancake sorting mediante el uso de la profundidad iterativa.

**Lenguaje utilizado**: Python

## Funciones

 ### **'__ init __(self, pancakes)'**
 Este el constructor de la clase Pancakes que recibe como parametros una lista de letras desordenadas, la profundidad del programa empieza en 1.
 
 ### **'voltear(self, posicion, pancakes)'**
 
Esta funcion recibe como parametro la posición donde se van a voltear los pancakes y la lista a voltear y devuelve los pancakes volteados desde esa posición.

 ### **'busqProfundidad(self, nodo, ant)'**
 Esta funcion recibe como parametros el nodo a partir del cual se realizará la busqueda en profundidad y el movimiento anterior que se realizó (en forma de lista) y en caso de encontrar solución dentro del limite de la profundidad actual va a retornar la serie de movimientos que se tiene que realizar para ordenar de menor a mayor los pancakes y en caso de no encontrar solución returnará -1.
 
 ### **'busqProfundidadIte(self, nodo)'**
 Esta función recibe como parametro el nodo a partir del cual iniciará el programa y devolverá la solución si la función busqProfundidad() devuelve solución,
 en caso de que haya recibido un -1 (no se ha encontrado solución) aumentará la profundidad limite del programa en 1.
 
 ## Como utilizar el código
 Para poder utilizar el código se tiene que crear una instancia de la clase "Pancakes" añadiendole como parametro una lista desordenada de letras minusculas y luego llamar a la funcion busqProfundidadIte() dandole como parametro la lista a ordenar. El resultado de la ejecución será una serie de numeros que indican los movimientos que se tienen que realizar para resolver ese problema.
 
A continuación se presenta un ejemplo de como utilizar el código:

![image](https://user-images.githubusercontent.com/125157604/229011500-b4d28666-bb37-43fd-85d7-6679699df0c1.png)

