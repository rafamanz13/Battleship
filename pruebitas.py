import numpy as np
from constants import *
def pintar_barco(eslora, tablero):
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
'''
Mirar si nos combiene hacer una función para la lógica de disparos y llamarla
en disparo_bot y disparo_jugador
'''
def disparo_bot():
    disparo_fila_bot = np.randomandom.randint(1, 10)
    disparo_colum_bot = np.random.randint(1, 10)
    continua_ejec_bot = True
    while continua_ejec_bot:
        if (tablero_juego[disparo_fila_bot, disparo_colum_bot] == '~'):
            tablero_juego[disparo_fila_bot, disparo_colum_bot] = '#'
        elif (tablero_juego[disparo_fila_bot:, disparo_colum_bot] == 'O'):
            tablero_juego_maquina[disparo_fila_bot:, disparo_colum_bot] = 'X'
            return disparo_bot()
        elif (tablero_juego[disparo_fila_bot:, disparo_colum_bot] == '#'):
            return disparo_bot()
        else:
            continua_ejec_bot = False
        print('Tablero jugador 1: ', tablero_juego)
def disparo_jugador():
    disparo_fila = int(input("¿Dónde te gustaría atacar? Elige la fila:\n"))
    disparo_colum = int(input("Ahora alige la columna\n"))
    continua_ejecucion = True
    while continua_ejecucion:
        if (0 > disparo_fila > 10) or (0 > disparo_colum > 10):
            print("Tus coordenadas son incorrectas :/ Introduce valores del 1 al 10!")
            return disparo_jugador()
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == '~'):
            tablero_juego_maquina[disparo_fila, disparo_colum] = '#'
            tablero_guia[disparo_fila, disparo_colum] = '#'
            print("Tu disparo ha caído al agua! :(")
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == '#'): #Comprobar como hacerlo par aque no salga al fallar el tiro
            print("Ya has disparado aquí, zoquetx!")
            return disparo_jugador()
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == 'O'):
            tablero_juego_maquina[disparo_fila, disparo_colum] = 'X'
            tablero_guia[disparo_fila, disparo_colum] = 'X'
            print("Le has dado a un barco de tu rival!")
            return disparo_jugador()
        else:
            print("Has acabado tu turno.")
            continua_ejecucion = False
def quien_comienza():
    #Mirar si se puede hacer con esto o lo quitamos
    comienzo = np.random.randint(0, 1)
    if comienzo == 0:
        print("Comienzas tú!")
        return disparo_jugador()
    else:
        print("Va a empezar la máquina!")
        return disparo_bot()
def iniciar_juego():
    numero_barcos = 0
    while numero_barcos < 10:
        if numero_barcos == 0:
            pintar_barco(4, tablero_juego)
            pintar_barco(4, tablero_juego_maquina)
        elif numero_barcos in [1,2]:
            pintar_barco(3, tablero_juego)
            pintar_barco(3, tablero_juego_maquina)
        elif numero_barcos in [3,4,5]:
            pintar_barco(2, tablero_juego)
            pintar_barco(2, tablero_juego_maquina)
        elif numero_barcos in [6,7,8,9]:
            pintar_barco(1, tablero_juego)
            pintar_barco(1, tablero_juego_maquina)
        numero_barcos += 1
    print('Tablero del jugador 1 \n',tablero_juego)
    print('Tablero de la máquina \n', tablero_juego_maquina)
    quien_comienza() #Hacer lógica para que al fallar siga la máquina tirando

    def comprobacion_maquina:

        condicion = True
        while condicion:
            if "O" in tablero:
                return disparo_bot()
            else:
                print("Tu flota se ha hundido :( PERDISTE!")
                condicion = False

    def nueva_partida:

        condicion = True
        juego_nuevo = input("¿Te gustaría volver a jugar? Introduce PLAYAGAIN para jugar de nuevo o cualquier tecla para salir")

        if juego_nuevo == PLAYAGAIN:
            return disparo_bot()
        elif juego_nuevo == DATA:
            print("Vámonos al beercamp con Tito") #EASTEREGG
        else:
            print("Gracias por jugar al Hundir la Flota de Gonzalo y Rafa!")
            condicion = False
