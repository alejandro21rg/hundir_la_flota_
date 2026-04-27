Descripción
Proyecto python en versión terminal -- 3.12 
Librerías: -Numpy -Time
Este proyecto implementa el clásico juego de estrategia Hundir la Flota, donde dos jugadores intentan adivinar la ubicación de los barcos del oponente en un tablero oculto.

El objetivo es destruir toda la flota enemiga antes de que el rival haga lo mismo.
Cómo jugar:
1.	Cada jugador dispone de un tablero (generalmente 10x10).
2.	Los jugadores colocan sus barcos en posiciones estratégicas:
      o	Horizontal o vertical
      o	Sin solaparse
3.	Tipos de barcos:
      o	4 casillas
      o	3 casillas
      o	2 casillas
4.	Turnos:
      o	Cada jugador dispara a una coordenada (ej: 1,1).
      o	El oponente responde:
            	Agua → fallo
            	Tocado → impacto
            	Hundido → barco destruido
  	
Si se acierta en el disparo se vuelve a disparar, si se falla pasa turno.

6.	Fin del juego:
       o	Gana quien hunda todos los barcos del rival.
