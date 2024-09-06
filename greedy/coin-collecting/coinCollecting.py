# Time Complexity: O(N)

def read_coins_file(file_name):
    """ Lee el archivo que contiene la matriz de monedas. """
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  # Tamaño de la cuadrícula (n x n)
        grid = []
        for line in lines[1:]:
            grid.append(list(map(int, line.strip().split())))
    return n, grid

def greedy_coin_collecting(n, grid):
    """ Algoritmo greedy para recolectar monedas. """
    i, j = 0, 0  # Posición inicial (0,0)
    path = [(i, j)]  # Para almacenar el camino seguido
    total_coins = grid[i][j]  # Empezamos con las monedas en (0,0)

    while i < n - 1 or j < n - 1:
        # Podemos movernos solo a la derecha o hacia abajo
        if i == n - 1:  # Si estamos en el borde inferior, solo podemos movernos a la derecha
            j += 1
        elif j == n - 1:  # Si estamos en el borde derecho, solo podemos movernos hacia abajo
            i += 1
        else:
            # Decisión greedy: Elegimos la celda con más monedas
            if grid[i + 1][j] > grid[i][j + 1]:
                i += 1  # Mover hacia abajo
            else:
                j += 1  # Mover hacia la derecha
        
        # Actualizamos el camino y el total de monedas
        path.append((i, j))
        total_coins += grid[i][j]
    
    return total_coins, path

def main():
    # Archivos que queremos leer
    file_names = ["coins-n5.txt", "coins-n10.txt", "coins-n20.txt", "coins-n100.txt"]
    
    for file_name in file_names:
        # Leer la cuadrícula de monedas
        n, grid = read_coins_file(file_name)
        
        # Aplicar el algoritmo greedy para recolectar monedas
        total_coins, path = greedy_coin_collecting(n, grid)
        
        # Imprimir los resultados
        print(f"Resultados para {file_name}:")
        print(f"Total de monedas recolectadas: {total_coins}")
        print(f"Camino tomado: {path}\n")

if __name__ == "__main__":
    main()

