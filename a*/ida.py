import numpy as np
import heapq
from collections import deque

# Estado objetivo del puzzle
objetivo = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # Usamos 0 para representar el espacio vacío
])

# Calcula la distancia de Manhattan entre el estado actual y el objetivo
def manhattan_dist(estado, objetivo):
    dist = 0
    for i in range(1, 9):  # Excluye el espacio vacío
        x1, y1 = np.where(estado == i)
        x2, y2 = np.where(objetivo == i)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist[0]  # Devuelve como un solo entero

# Genera los vecinos posibles del estado actual al mover el espacio vacío
def generar_vecinos(estado):
    vecinos = []
    x, y = np.where(estado == 0)  # Encuentra el espacio vacío
    x, y = x[0], y[0]
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Asegura que el movimiento esté dentro de los límites
            nuevo_estado = estado.copy()
            nuevo_estado[x, y], nuevo_estado[nx, ny] = nuevo_estado[nx, ny], nuevo_estado[x, y]
            vecinos.append(nuevo_estado)
    
    return vecinos

# Implementa el algoritmo IDA*
def ida_star(estado_inicial, objetivo):
    def buscar(camino, g, threshold):
        estado_actual = camino[-1]
        f = g + manhattan_dist(estado_actual, objetivo)

        if f > threshold:
            return f  # Devuelve el nuevo límite
        if np.array_equal(estado_actual, objetivo):
            return "ENCONTRADO"  # Solución encontrada

        min_threshold = float('inf')
        for vecino in generar_vecinos(estado_actual):
            if any(np.array_equal(vecino, n) for n in camino):
                continue  # Evita ciclos
            camino.append(vecino)
            resultado = buscar(camino, g + 1, threshold)
            if resultado == "ENCONTRADO":
                return "ENCONTRADO"
            if resultado < min_threshold:
                min_threshold = resultado
            camino.pop()
        
        return min_threshold

    # Configuración inicial del IDA*
    threshold = manhattan_dist(estado_inicial, objetivo)
    camino = [estado_inicial]
    while True:
        resultado = buscar(camino, 0, threshold)
        if resultado == "ENCONTRADO":
            return camino
        if resultado == float('inf'):
            return None  # No hay solución
        threshold = resultado

# Imprime los pasos de la solución
def imprimir_solucion(solucion):
    if solucion is None:
        print("No se encontró una solución")
    else:
        print("Número de pasos:", len(solucion) - 1)
        for i, paso in enumerate(solucion):
            print(f"Paso {i}:")
            print(paso)

# Estado inicial del puzzle
estado_inicial = np.array([
    [3, 2, 0],
    [7, 1, 4],
    [6, 5, 8]
])

# Resuelve el puzzle usando IDA*
solucion = ida_star(estado_inicial, objetivo)

# Imprime la solución
imprimir_solucion(solucion)
