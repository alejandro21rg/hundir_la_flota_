import numpy as np


# Crear tablero
def crear_tablero():
    return np.full((10, 10), "_")

# Imprimir tablero
def imprimir_tablero(tablero):
    print("  0 1 2 3 4 5 6 7 8 9")
    for i, fila in enumerate(tablero):
        print(i, " ".join(fila))

# Colocar barcos
def colocar_barcos(lista_barcos, tablero):
    for barco in lista_barcos:
        for fila, col in barco:
            tablero[fila][col] = "O"
    return tablero


def disparar(tablero_rival, tablero_disparos, lista_disparo):

    while True:
        try:
            fila = int(input("Fila (0-9): "))
            columna = int(input("Columna (0-9): "))

            # Disparar en el tablero
            tam = tablero_rival.shape[0]
            if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
                print("Coordenadas fuera del tablero")
                continue

            casilla = (fila, columna)

            # Evitar repetir disparos
            if casilla in lista_disparo:
                print("Ya has disparado ahí")
                continue

            break

        except ValueError:
            print("Introduce números válidos")

    # Registrar disparo
    lista_disparo.append(casilla)

    # Resultado
    if tablero_rival[fila][columna] == "O":
        tablero_rival[fila][columna] = "X"
        tablero_disparos[fila][columna] = "X"
        return "Tocado"
    else:
        tablero_disparos[fila][columna] = "A"
        return "Agua, tienes menos puntería que los jugadores del Cádiz C.F"


# Disparo máquina
def disparo_maquina(tablero_objetivo_r, tablero_disparos_r, lista_disparos):
    while True:
        fila = np.random.randint(0, 10)
        columna = np.random.randint(0, 10)

        casilla = (fila, columna)

        if casilla not in lista_disparos:
            lista_disparos.append(casilla)

            if tablero_objetivo_r[fila][columna] == "O":
                tablero_objetivo_r[fila][columna] = "X"
                tablero_disparos_r[fila][columna] = "X"
                return f"Rival dispara a {casilla}: Tocado"

            else:
                tablero_objetivo_r[fila][columna] = "A"
                tablero_disparos_r[fila][columna] = "A"
                return f"Rival dispara a {casilla}: Agua"


# Crear barco aleatorio
def crear_barco(eslora):
    orientacion = np.random.choice(["H", "V"])

    if orientacion == "H":
        fila = np.random.randint(0, 10)
        col = np.random.randint(0, 10 - eslora)
        barco = [(fila, col + i) for i in range(eslora)]

    else:
        fila = np.random.randint(0, 10 - eslora)
        col = np.random.randint(0, 10)
        barco = [(fila + i, col) for i in range(eslora)]

    return barco


# Validar barco
def es_valido(barco, tablero):
    for fila, col in barco:
        if tablero[fila][col] != "_":
            return False
    return True


# Crear lista barcos
def crear_lista_barcos():
    lista_esloras = [2, 2, 2, 3, 3, 4]
    tablero_aux = crear_tablero()
    lista_barcos = []

    for eslora in lista_esloras:
        colocado = False

        while not colocado:
            barco = crear_barco(eslora)

            if es_valido(barco, tablero_aux):
                colocar_barcos([barco], tablero_aux)
                lista_barcos.append(barco)
                colocado = True

    return lista_barcos

# Crear barco manual
def crear_barco_manual(eslora):
    print(f"\nColoca un barco de tamaño {eslora}")

    while True:
        try:
            fila = int(input("Fila inicial (0-9): "))
            col = int(input("Columna inicial (0-9): "))

            if fila < 0 or fila > 9 or col < 0 or col > 9:
                print(" Coordenadas fuera del tablero")
                continue
            break
        except:
            print("Introduce números válidos")

    while True:
        orientacion = input("Orientación (H/V): ").upper()

        if orientacion in ["H", "V"]:
             break
        else:
                print("Orientación incorrecta. Usa solo H o V.")

    # Crear Barco       
    barco = []

    for i in range(eslora):
        if orientacion == "H":
            nueva_fila = fila
            nueva_col = col + i
        else:
            nueva_fila = fila + i
            nueva_col = col

        
        if nueva_fila > 9 or nueva_col > 9:
            print("El barco se sale del tablero")
            return None

        barco.append((nueva_fila, nueva_col))

    return barco

# Crear lista de barcos

def crear_lista_barcos_manual():
    lista_esloras = [2, 2, 2, 3, 3, 4]
    tablero_aux = crear_tablero()
    lista_barcos = []

    for eslora in lista_esloras:
        colocado = False

        while not colocado:
            barco = crear_barco_manual(eslora)

            if barco is None:
                continue

            if es_valido(barco, tablero_aux):
                colocar_barcos([barco], tablero_aux)
                lista_barcos.append(barco)
                print("Barco colocado")
                print(tablero_aux)
                colocado = True
            else:
                print("Se solapa con otro barco, prueba otra posición")

    return lista_barcos

# Final del juego

def quedan_barcos(tablero):
    return "O" in tablero