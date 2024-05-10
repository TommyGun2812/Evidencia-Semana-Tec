# Evidencia-Semana-Tec  
  
## Tomás Pérez Vera  
Archivo modificado: pacman.py  
Alumno: Tomás Pérez Vera  
Matrícula: A01028008  
Cambios realizados:     
1. Modificar mapa del juego: Se modificó el diseño del mapa del juego con respecto al código base, para ello se modificaron los valores de la lista tiles, de  tal manera que cada valor en uno, representa el camino en el que el personaje de pacman avanza para comerse las pastillas; y cada valor en cero representa los muros en que ni este personaje ni los fantasmas pueden atravesar. 
2. Aumentar velocidad de fantasmas: Con el objetivo de poder aumentar la velocidad con la que los fantasmas del juego se desplazan, se modificó el segundo parametro del método ontimer, de tal manera que de pasar de 100 a 75, esto provoca que se mande a llamar recursivamente la función move en un lapso de 75 milisegundos, la cual está encargada del movimiento de todos los personajes pertenecientes al juego, por ello se explica que la reducción del intervalo de tiempo en que se manda a llamar la función, provoca el aumento de la velocidad en el movimiento de los fantasmas.
3. Corregir sintaxis de código, para cumplir con estándar PEP 8: Con el fin de cumplir con el estándar PEP 8, el cósigo fue modificado en torno a la importación de librerías; eliminación de espacios en blanco; seguimiento de la convemción para comentarios, tanto de una sola línea como multilíena; y la inclusión de una línea en blanco al final del código.    
