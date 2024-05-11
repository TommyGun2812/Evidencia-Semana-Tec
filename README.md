# Evidencia-Semana-Tec  
  
## Tomás Pérez Vera  
Archivo modificado: pacman.py  
Alumno: Tomás Pérez Vera  
Matrícula: A01028008  

Cambios realizados:     
1. Modificar mapa del juego: Se modificó el diseño del mapa del juego con respecto al código base, para ello se modificaron los valores de la lista tiles, de  tal manera que cada valor en uno, representa el camino en el que el personaje de pacman avanza para comerse las pastillas; y cada valor en cero representa los muros en que ni este personaje ni los fantasmas pueden atravesar. 
2. Aumentar velocidad de fantasmas: Con el objetivo de poder aumentar la velocidad con la que los fantasmas del juego se desplazan, se modificó el segundo parametro del método ontimer, de tal manera que de pasar de 100 a 75, esto provoca que se mande a llamar recursivamente la función move en un lapso de 75 milisegundos, la cual está encargada del movimiento de todos los personajes pertenecientes al juego, por ello se explica que la reducción del intervalo de tiempo en que se manda a llamar la función, provoca el aumento de la velocidad en el movimiento de los fantasmas.
3. Corregir sintaxis de código, para cumplir con estándar PEP 8: Con el fin de cumplir con el estándar PEP 8, el cósigo fue modificado en torno a la importación de librerías; eliminación de espacios en blanco; seguimiento de la convemción para comentarios, tanto de una sola línea como multilíena; y la inclusión de una línea en blanco al final del código.    


## Gonzalo Morán Sánchez 
Archivo modificado: tictactoe.py 
Alumno: Gonzalo Morán Sánchez 
Matrícula: A01710494  

Cambios realizados:     
1. Modificar el tamaño y el color de los símbolos "X" y "O" y centrarlos.
2. Verificar si la casilla correspondiente en el tablero está vacía antes de permitir que un jugador coloque su símbolo, si la casilla ya está ocupada, el jugador no puede colocar su símbolo en ella.
3. Corregir sintaxis de código para cumplir con estándar PEP 8, el código fue modificado en torno a la importación de librerías, eliminación de espacios en blanco; seguimiento de la convención para comentarios.  


## Ximena Cantera Reséndiz  
Archivo modificado: memoria.py  
Alumno: Ximena Cantera Reséndiz
Matrícula: A01277310

Cambios realizados:     
1. Contar y desplegar número de taps: Se modificó la vista del juego, se colocó un mensaje que muestre los taps que se realizan durante el jurgo. Para ello de definió un contador que aumentará con cada selección del cuadrado. El objetivo es que el jugador conozca el número de movimientos y poder superarlo en algún momento.
2. Detectar cuando todos los cuadros se han destapado. Por supuesto: Para identificar cuándo todos los cuadrados se hace una verificación para saber si todos los elementos en la lista `hide` (que representa el estado de los cuadrados oculto o destapado son `True`), lo que significa que todos los cuadrados están destapados. Si es así, muestra un mensaje de finalización del juego indicando que todos los cuadrados están destapados en la ventana. Esto se hace durante cada iteración de la función que imprime el tablero, permitiendo una actualización constante del estado de los cuadrados.
3. Finalmente, se hizo una correxión del código para cumplir con el estándar PEP 8, entre sus modificaciones fue aumentar espacios, la forma de importar librerías y seguimiento de comentarios.