import numpy as np
from numpy import random
import random
from constants import *

print(fila, columna)
print(orientacion)
print(eslora)

def pintar_barco(eslora):
    while True:
        orientacion = np.random.choice(list('NSEW'))

        coordenadas = np.random.randint(0,10, size=2)
        fila = coordenadas[0]
        columna = coordenadas[1]

        Norte = tablero[fila:(fila - eslora):-1, columna]
        Sur = tablero[fila:(fila + eslora), columna]
        Este = tablero[fila, columna :(columna + eslora)]
        Oeste = tablero[fila, columna :(columna - eslora):-1]

        if (orientacion == 'N') and (len(Norte) == eslora) and ('O' not in Norte):
            tablero[fila:(fila - eslora):-1, columna] = 'O'
            break
        elif (orientacion == 'S') and (len(Sur) == eslora) and ('O' not in Sur):
            tablero[fila:(fila + eslora), columna] = 'O'
            break
        elif (orientacion == 'E') and (len(Este) == eslora) and ('O' not in Este):
            tablero[fila, columna :(columna + eslora)] = 'O'
            break
        elif (orientacion == 'W') and (len(Oeste) == eslora) and ('O' not in Oeste):
            tablero[fila, columna :(columna - eslora):-1] = 'O'
            break
        continue

def iniciar_juego():
    numero_barcos = 0
    while numero_barcos < 10:
        if numero_barcos == 0:
            pintar_barco(4,1)
        elif numero_barcos in [1,2]:
            pintar_barco(3,2)
        elif numero_barcos in [3,4,5]:
            pintar_barco(2,3)
        elif numero_barcos in [6,7,8,9]:
            pintar_barco(1,4)
        numero_barcos += 1
    print(tablero)

def quien_comienza():
    comienzo = random.randint(0, 1)
    if comienzo == 0:
        print("Comienzas tú!")
        return disparo_jugador()
    else:
        print("Va a empezar la máquina!")
        return disparo_bot()

def disparo_jugador():

    disparo_fila = input(int("¿Dónde te gustaría atacar? Elige la fila:\n"))
    disparo_colum = input(int("Ahora alige la columna\n"))
    continua_ejecucion = True

    while continua_ejecucion:

        if (0 > disparo_fila > 10) or (0 > disparo_colum > 10):
            print("Tus coordenadas son incorrectas :/ Introduce valores del 1 al 10!")
            return disparo_jugador()
        elif tablero_maquina[disparo_fila, disparo_colum] == '~':
            tablero_maquina[disparo_fila, disparo_colum] = "#"
            print("Tu disparo ha caído al agua! :(")
        elif tablero_maquina[disparo_fila, disparo_colum] == '#':
            print("Ya has disparado aquí, zoquetx!")
            return disparo_jugador()
        elif tablero_maquina[disparo_fila:, disparo_colum] == "O":
            tablero_maquina[disparo_fila:, disparo_colum] = "X"
            print("Le has dado a un barco de tu rival!")
            return disparo_jugador()
        else:
            print("Has acabado tu turno.")
            continua_ejecucion = False

def disparo_bot():

    disparo_fila_bot = random.randint(1, 10)
    disparo_colum_bot = random.randint(1, 10)
    continua_ejec_bot = True

    while continua_ejec_bot:

        if tablero[disparo_fila_bot, disparo_colum_bot] == '~':
            tablero[disparo_fila_bot, disparo_colum_bot] = "#"
        elif tablero[disparo_fila_bot:, disparo_colum_bot] == "O":
            tablero_maquina[disparo_fila_bot:, disparo_colum_bot] = "X"
            return disparo_bot()
        elif tablero[disparo_fila_bot:, disparo_colum_bot] == '#':
            return disparo_bot()
        else:
            continua_ejec_bot = False

