def main():
    print("****¡HOLAAA Bienvenido al simulador de partidos de tenis!****")
    jugador1 = input("Ingresa el nombre del primer jugador: ")
    jugador2 = input("Ingresa el nombre del segundo jugador: ")

    #Se juegan 6 juegos por set(en el mejor de los casos 4) y gana el mejor de 3 sets.
    # Sin embargo definimos 20 en cada uno en caso de empate. 
    #Se sigue jugando, hasta encontrar un ganador de juego o/y set.
    juegos_por_set = 6
    intentos_por_juego = 50
    sets = 3  # Para definir el ganador del partido, se juegan 3 sets y gana el mejor de los 3 sets.

    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    juegos_ganados_jugador1 = 0
    juegos_ganados_jugador2 = 0
    sets_jugador1 = 0
    sets_jugador2 = 0

    print(f"\n¡Comienza el partido de tenis!")
    # Repetir el ciclo para 3 sets. Gana el partido el mejor de 3 sets.
    for set_actual in range(sets):
        print(f" DAMOS INICIO al SET No. {set_actual + 1}\n")
        for juego_actual in range(juegos_por_set):
            #Mostramos en pantalla el juego y set actual
            print(f"--> Comienza el JUEGO {juego_actual + 1} del SET {set_actual + 1} <--")
            #Si el num de juego es par hacemos cambio de cancha
            if (juego_actual + 1) % 2 == 0:
                print(f"¡Cambio de cancha! {jugador1} y {jugador2} cambian de cancha.\n")
            for juego in range(intentos_por_juego):
                #Mostramos en terminal el puntaje actual de los jugadores
                print(f"Puntaje de {jugador1}: {puntaje_jugador1} - Puntaje de {jugador2}: {puntaje_jugador2}")
                #Verificamos quien gana los puntos
                while True:
                    ganador_punto = input(f"¿Quién gana el punto {jugador1} o {jugador2}? ")
                    if ganador_punto == jugador1:
                        puntaje_jugador1 += 1
                        break
                    elif ganador_punto == jugador2:
                        puntaje_jugador2 += 1
                        break
                    else:
                        print("Nombre de jugador incorrecto. Inténtalo de nuevo.")
                    
                #Verificamos quien gana el juego de acuerdo a las reglas del tenis. El ganador de un juego es el primero que
                #gane 4 puntos y tenga una diferencia de 2 puntos con el otro jugador. Si quedan en empate 40-40, se juega
                #hasta que uno de los dos jugadores gane dos puntos seguidos y quede con una diferencia de 2 puntos.
                if abs(puntaje_jugador1 - puntaje_jugador2) >= 2 and (puntaje_jugador1 >= 4 or puntaje_jugador2 >= 4):
                    ganador_juego = jugador1 if puntaje_jugador1 > puntaje_jugador2 else jugador2
                    print(f"\n¡Termina el JUEGO {juego_actual + 1} del SET {set_actual + 1} y el GANADOR es {ganador_juego}! \n")
                    #Reiniciamos el puntaje de los jugadores cada vez que se gana un juego
                    if puntaje_jugador1 > puntaje_jugador2:
                        puntaje_jugador1 = 0
                        puntaje_jugador2 = 0
                        juegos_ganados_jugador1 += 1
                    else:
                        puntaje_jugador1 = 0
                        puntaje_jugador2 = 0
                        juegos_ganados_jugador2 += 1
                    break
              
         # Calculamos el ganador del set
        # El ganador del set es el primero que gane 4 juegos de 6 y tenga una diferencia de 2 juegos con el otro jugador.
        # Si quedan en empate 3-3, se juega hasta que uno de los dos jugadores gane dos juegos seguidos y quede con una
        # diferencia de 2 juegos.
        while juegos_ganados_jugador1 == juegos_ganados_jugador2 == 3:
            print("¡Empate 3-3 en el set! Juguemos más juegos hasta que uno de los jugadores gane por 2 juegos de diferencia.")
            while abs(juegos_ganados_jugador1 - juegos_ganados_jugador2) < 2:
                # Repetir juegos hasta que uno de los jugadores gane por 2 juegos de diferencia. Por ejemplo, si el marcador
                # esta 3-3 se juega hasta que uno de los dos obtenga 3-5 o 4-6 o 5-7, etc.
                for juego in range(intentos_por_juego):
                    #Mostramos en terminal el puntaje actual de los jugadores
                    print(f"Puntaje de {jugador1}: {puntaje_jugador1} - Puntaje de {jugador2}: {puntaje_jugador2}")
                    #Verificamos quien gana los puntos
                    while True:
                        ganador_punto = input(f"¿Quién gana el punto {jugador1} o {jugador2}? ")
                        if ganador_punto == jugador1:
                            puntaje_jugador1 += 1
                            break
                        elif ganador_punto == jugador2:
                            puntaje_jugador2 += 1
                            break
                        else:
                            print("Nombre de jugador incorrecto. Inténtalo de nuevo.")
                    #Verificamos quien gana el juego de acuerdo a las reglas del tenis. El ganador de un juego es el primero que
                    #gane 4 puntos y tenga una diferencia de 2 puntos con el otro jugador. Si quedan en empate 40-40, se juega
                    #hasta que uno de los dos jugadores gane dos puntos seguidos y quede con una diferencia de 2 puntos.
                    if abs(puntaje_jugador1 - puntaje_jugador2) >= 2 and (puntaje_jugador1 >= 4 or puntaje_jugador2 >= 4):
                        ganador_juego = jugador1 if puntaje_jugador1 > puntaje_jugador2 else jugador2
                        print(f"\n¡Termina el JUEGO {juego_actual + 1} del SET {set_actual + 1} y el GANADOR es {ganador_juego}! \n")
                        #Reiniciamos el puntaje de los jugadores cada vez que se gana un juego
                        if puntaje_jugador1 > puntaje_jugador2:
                            puntaje_jugador1 = 0
                            puntaje_jugador2 = 0
                            juegos_ganados_jugador1 += 1
                        else:
                            puntaje_jugador1 = 0
                            puntaje_jugador2 = 0
                            juegos_ganados_jugador2 += 1
                        break
        #Calculamos el ganador del set. El ganador del set es el primero que gane 4 juegos de 6 y
        #tenga una diferencia de 2 juegos con el otro jugador.  
        if abs(juegos_ganados_jugador1 - juegos_ganados_jugador2) >= 2 and (juegos_ganados_jugador1 >= 4 or juegos_ganados_jugador2 >= 4):
            ganador_set = jugador1 if juegos_ganados_jugador1 > juegos_ganados_jugador2 else jugador2
            print(f"¡{ganador_set} GANA el SET No. {set_actual + 1}!\n")
        if juegos_ganados_jugador1 > juegos_ganados_jugador2:
            sets_jugador1 += 1
        else:
            sets_jugador2 += 1
        juegos_ganados_jugador1 = 0
        juegos_ganados_jugador2 = 0


    # Calculamos el ganador del partido
    if sets_jugador1 > sets_jugador2:
        ganador_partido = jugador1
    else:
        ganador_partido = jugador2
    print(f"\n¡{ganador_partido} GANA el PARTIDO DE TENIS!")

if __name__ == "__main__":
    main()
