import numpy as np
from numpy import random

# Creamos el tablero del jugador 1
tablero = np.full((10,10), '~')
# Creamos el tablero con el que jugará la máquina
tablero_maquina = tablero
# Creamos una lista para poder cambiar de tablero
eslora = 4
#Definimos las primeras coordenadas del barco
coordenadas = np.random.randint(0,10, size=2)
fila = coordenadas[0]
columna = coordenadas[1]
#Definimos las diferentes orientaciones que puede tener el barco
orientacion = np.random.choice(list('NSEW'))
#Definimos la lógica para el encuadre de los barcos en el tablero
Norte = tablero[fila:(fila - eslora):-1, columna]
Sur = tablero[fila:(fila + eslora), columna]
Este = tablero[fila, columna :(columna + eslora)]
Oeste = tablero[fila, columna :(columna - eslora):-1]