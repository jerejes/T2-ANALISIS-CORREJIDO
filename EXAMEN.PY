laberinto = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1],
]

visitado = []
for i in range(9):
    visitado.append([0] * 9)

ruta = []


def mostrar(m):
    for fila in m:
        print(fila)
    print()


def valor(f, c):
    if laberinto[f][c] == 3 or laberinto[f][c] == 4:
        return laberinto[f][c]
    return 0


def es_pared(f, c):
    return laberinto[f][c] == 0


def puede_pasar(f, c):
    if f < 0 or f > 8 or c < 0 or c > 8:
        return False
    if es_pared(f, c):
        return False
    if visitado[f][c] == 1:
        return False
    return True


def resolver(f, c, puntos):
    visitado[f][c] = 1
    ruta.append([f, c])
    puntos = puntos + valor(f, c)

    # llego a F
    if f == 0 and c == 0:
        if puntos >= 23:
            return True
        visitado[f][c] = 0
        ruta.pop()
        return False

    if puede_pasar(f - 1, c):
        if resolver(f - 1, c, puntos):
            return True
    if puede_pasar(f, c + 1):
        if resolver(f, c + 1, puntos):
            return True
    if puede_pasar(f + 1, c):
        if resolver(f + 1, c, puntos):
            return True
    if puede_pasar(f, c - 1):
        if resolver(f, c - 1, puntos):
            return True

    visitado[f][c] = 0
    ruta.pop()
    return False


print("LABERINTO ORIGINAL")
for fila in laberinto:
    print(fila)
print()

if resolver(8, 0, 0):
    print("El raton SI logro salir del laberinto")
    print()
    print("ASI SE MUEVE EL RATON POR EL CAMINO CORRECTO, CUADRO POR CUADRO:")
    print()

    matriz = []
    for i in range(9):
        matriz.append([0] * 9)
    puntos = 0
    paso = 0
    for celda in ruta:
        paso = paso + 1
        matriz[celda[0]][celda[1]] = 1
        puntos = puntos + valor(celda[0], celda[1])
        print("Paso", paso, "- fila",
              celda[0], "columna", celda[1], "- puntos:", puntos)
        mostrar(matriz)

    print("Llego a F con", puntos, "puntos")
else:
    print("El raton NO logro salir del laberinto")
