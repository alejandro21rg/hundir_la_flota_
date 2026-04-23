from utils_final import crear_tablero, colocar_barcos, disparar, crear_lista_barcos, crear_lista_barcos_manual, disparo_maquina, quedan_barcos, imprimir_tablero
import time

# Tableros

tablero_jugador_barcos = crear_tablero()
tablero_jugador_disparos = crear_tablero()

tablero_rival_barcos = crear_tablero()
tablero_rival_disparos = crear_tablero()

# Lista de disparos

lista_disparos_jugador = []
lista_disparos_rival = []

# Crear barcos

print("===> BIENVENIDO A HUNDIR LA FLOTA, COLOCA TUS BARCOS <===")
lista_barcos_jugador = crear_lista_barcos_manual()

print("\n===> COLOCANDO BARCOS DEL RIVAL <===")
lista_barcos_rival = crear_lista_barcos()

# Colocar barcos

colocar_barcos(lista_barcos_jugador, tablero_jugador_barcos)
colocar_barcos(lista_barcos_rival, tablero_rival_barcos)

print("\n=== EMPIEZA EL JUEGO ===")

# Bucle principal

while True:

  
    # Turno Jugador
   
    while True:
        print("\nTu tablero de disparos:")
        print(tablero_jugador_disparos)

        print("\nDisparos realizados por el jugador:")
        for d in lista_disparos_jugador:
             print(d)

        resultado = disparar(
            tablero_rival_barcos,
            tablero_jugador_disparos,
            lista_disparos_jugador,
            lista_barcos_rival   
        )

        print("Resultado:", resultado)

        time.sleep(1.5)

        print("\nTablero actualizado:")
        imprimir_tablero(tablero_jugador_disparos)
        time.sleep(1.5)

        # Jugador gana
        if not quedan_barcos(tablero_rival_barcos):
            print("\n ¡HAS GANADO! Has conseguido 30 min. más de descanso")
            break

        if "Tocado" in resultado:
            print("¡Te toca tirar de nuevo!")
            continue
        else:
            break

    # Terminar juego si gana jugador
    if not quedan_barcos(tablero_rival_barcos):
        break

  
    # Turno Rival

    while True:
        print("\nTurno del rival...")
        time.sleep(1.5)

        print("\nDisparos del rival hasta ahora:")
        for d in lista_disparos_rival:
            print(d)

        resultado_maquina = disparo_maquina(
            tablero_jugador_barcos,
            tablero_rival_disparos,
            lista_disparos_rival,
            lista_barcos_jugador
        )

        print("\n" + resultado_maquina)

        time.sleep(1.5)

        print("\nTu tablero de barcos:")
        print(tablero_jugador_barcos)

        time.sleep(1.5)

        # Rival gana
        if not quedan_barcos(tablero_jugador_barcos):
            print("\n HAS PERDIDO... El rival ha hundido todos tus barcos.")
            break

        if "Tocado" in resultado_maquina:
            print("Al rival le toca tirar de nuevo")
            continue
        else:
            break

    # Terminar juego si gana el rival
    
    if not quedan_barcos(tablero_jugador_barcos):
        break