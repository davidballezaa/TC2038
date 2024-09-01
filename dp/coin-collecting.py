# Time Complexity: O(rows*cols => n^2)
# Space Complexity: O(rows*cols => n^2)

def coinCollecting(matrix, n):
  coinsCollected = [[0 for i in range(n + 1)] for j in range(n + 1)] 
  for i in range(1, len(coinsCollected)):
    for j in range(1, len(coinsCollected[i])):
      # Relación de recursion
      coinsCollected[i][j] = max(coinsCollected[i-1][j], coinsCollected[i][j-1]) + matrix[i-1][j-1]

  return coinsCollected[n][n]

grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
]
print(coinCollecting(grid, 5))

"""
¿Por qué funciona la relación de recurrencia? 

La idea principal es que para llegar a una celda (i, j) en la matriz, solo puedes haber llegado desde la celda de arriba (i-1, j) o desde la celda de la izquierda (i, j-1).
Por lo tanto, para calcular la cantidad máxima de monedas recolectadas en (i, j), necesitas conocer la cantidad máxima de monedas recolectadas en esas dos celdas previas.
"""

