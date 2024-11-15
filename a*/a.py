import numpy as np
import heapq
from pygame.locals import *
from pygame.locals import Color
import pygame

# Calcula la distancia Manhattan
def manhattan_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Función para obtener los vecinos válidos
def get_neighbors(map_cells, estado, filas, columnas):
    vecinos = []
    fila, columna = estado
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha

    for dr, dc in direcciones:
        nueva_fila, nueva_columna = fila + dr, columna + dc
        # Solo añade el vecino si es una celda transitable (1)
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and map_cells[nueva_fila][nueva_columna] == 1:
            vecinos.append((nueva_fila, nueva_columna))

    return vecinos

# Algoritmo A*
def aStar(map_cells, estadoInicial, estadoObjetivo, filas, columnas):
    print(f"Iniciando búsqueda A* desde {estadoInicial} hasta {estadoObjetivo}")
    d = manhattan_dist(estadoInicial, estadoObjetivo)
    q = []
    heapq.heappush(q, (d, 0, estadoInicial, [estadoInicial]))
    visitados = set()

    while q:
        _, pasos, estado, camino = heapq.heappop(q)
        print(f"Visitando: {estado}, Camino actual: {camino}")

        if estado in visitados:
            continue

        visitados.add(estado)

        # Verifica si se ha alcanzado el objetivo
        if estado == estadoObjetivo:
            print("Objetivo alcanzado!")
            return camino, len(camino) - 1

        # Explora los vecinos del estado actual
        for vecino in get_neighbors(map_cells, estado, filas, columnas):
            if vecino not in visitados:
                distancia = manhattan_dist(vecino, estadoObjetivo)
                heapq.heappush(q, (distancia + pasos + 1, pasos + 1, vecino, camino + [vecino]))

    print("No se encontró un camino.")
    return None, 0  # Si no se encuentra un camino

# Lee el archivo del mapa
def loadMap(fileName):
    f = open(fileName , "r")
    text = list()
    for line in f:
        aux = line.split('\n')
        text.append(list(map(int, aux[0].split('  '))))
    map_cells = np.array(text)
    return map_cells

# Muestra las coordenadas en la pantalla
def showCoors(pygame, screen, rows, cols, font, map_cells):
    white = Color('white')
    black = Color('black')
    surface = pygame.Surface((cols * tile_size, rows * tile_size), pygame.SRCALPHA, 32)
    pygame.draw.rect(surface, (255, 255, 255, 80), (0, 0, cols*tile_size, rows*tile_size))
    screen.blit(surface, (0, 0))

    for i in range(rows):
        for j in range(cols):
            textColor = white if map_cells[i][j] == 1 else black
            text = font.render(f"{i},{j}", True, textColor)
            screen.blit(text, (j*tile_size + (tile_size/6), i*tile_size + (tile_size/3)))

# Crea el mapa de tiles, calculando las coordenadas usando tile_size
def tiles(screen, map_cells, tile1, tile2):
    for i in range(len(map_cells)):
        for j in range(len(map_cells[0])):
            screen.blit(tile1 if map_cells[i][j] == 0 else tile2, (j * tile_size, i * tile_size))

# Dibuja el camino en amarillo
def yellow_path(pygame, screen, path_tile, path, step):
    for s in range(step + 1):
        i = path[s][1]
        j = path[s][0]
        screen.blit(path_tile, (i * tile_size, j * tile_size))

# Función principal
def main1():
    global tile_size
    tile_size = 40  # Tamaño de celdas

    pos_init = (9, 1)
    pos_target = (5, 8)
    
    map_cells = loadMap('map2.txt')  # Obtiene el mapa desde un archivo, como un array de numpy
    
    filas, columnas = map_cells.shape  # Número de filas y columnas

    # Verifica que el inicio y el objetivo sean celdas transitables
    if map_cells[pos_init] != 1 or map_cells[pos_target] != 1:
        print("Error: La posición inicial o el objetivo están bloqueados.")
        return

    # Llama a la función que encuentra el camino usando A*
    path, steps = aStar(map_cells, pos_init, pos_target, filas, columnas)

    if path is None:
        print('No hay camino')
        return

    print('Mapa:\n', map_cells)
    print('Pasos:', steps)
    print('Camino:', path)

    # Inicializa la pantalla con Pygame
    pygame.init()
    screen = pygame.display.set_mode((columnas * tile_size, filas * tile_size))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Skull')
    font = pygame.font.SysFont('arial.ttf', 20)

    # Carga y escala las imágenes de los tiles
    img1 = pygame.image.load("tile1.png")
    img2 = pygame.image.load("tile2.png")
    img3 = pygame.image.load("skull.png")
    img4 = pygame.image.load("treasure.png")
    tile_green = pygame.transform.scale(img1, (tile_size, tile_size))
    tile_grey = pygame.transform.scale(img2, (tile_size, tile_size))
    skull = pygame.transform.scale(img3, (tile_size, tile_size))  # imagen de la calavera
    treasure = pygame.transform.scale(img4, (tile_size, tile_size))  # imagen del tesoro

    path_tile = pygame.Surface((tile_size, tile_size))  # tile amarillo para el camino
    path_tile.fill(Color('yellow'))

    loop = True  # Bucle de animación
    step = 0  # Contador de pasos para el camino
    litle_step = 0.0  # Tamaño de paso

    # Posición inicial de la calavera
    xb, yb = pos_init[1] * tile_size, pos_init[0] * tile_size

    # Bucle principal de Pygame
    while loop:
        tiles(screen, map_cells, tile_green, tile_grey)
        screen.blit(treasure, (pos_target[1] * tile_size, pos_target[0] * tile_size))
        
        yellow_path(pygame, screen, path_tile, path, step)
        screen.blit(skull, (xb, yb))
        
        showCoors(pygame, screen, filas, columnas, font, map_cells)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

        # Controla la animación de la calavera
        if step < (len(path) - 1):
            xb = path[step][1] * tile_size
            yb = path[step][0] * tile_size

        litle_step += 0.10

        # Avanza al siguiente paso en el camino
        if litle_step > 0.90:
            litle_step = 0
            step += 1
            if step >= len(path):
                step = 0

        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(32)
    
    pygame.quit()

if __name__ == '__main__':
    main1()
