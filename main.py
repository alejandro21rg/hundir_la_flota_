from utils import crear_tablero, colocar_barcos, disparar, crear_lista_barcos, crear_lista_barcos_manual, disparo_maquina, quedan_barcos

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

#  Bucle principal
while True:

  
    # TURNO JUGADOR
   
    while True:
        print("\nTu tablero de disparos:")
        print(tablero_jugador_disparos)

        resultado = disparar(
            tablero_rival_barcos,
            tablero_jugador_disparos,
            lista_disparos_jugador   
        )

        print("Resultado:", resultado)

        # Jugador gana
        if not quedan_barcos(tablero_rival_barcos):
            print("\n ¡HAS GANADO! Has conseguido 30 min. más de descanso")
            break

        if "Tocado" in resultado:
            print("¡Repites turno!")
            continue
        else:
            break

    # salir si gana jugador
    if not quedan_barcos(tablero_rival_barcos):
        break

  
    #  TURNO RIVAL

    while True:
        resultado_maquina = disparo_maquina(
            tablero_jugador_barcos,
            tablero_rival_disparos,
            lista_disparos_rival
        )

        print("\n" + resultado_maquina)

        print("\nTu tablero de barcos:")
        print(tablero_jugador_barcos)

        # Rival gana
        if not quedan_barcos(tablero_jugador_barcos):
            print("\n HAS PERDIDO... El rival ha hundido todos tus barcos.")
            break

        if "Tocado" in resultado_maquina:
            print("El rival repite turno")
            continue
        else:
            break

    # salir si pierde jugador
    if not quedan_barcos(tablero_jugador_barcos):
        break