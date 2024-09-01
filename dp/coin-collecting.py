# Time Complexity: O(rows*cols => n^2)
# Space Complexity: O(rows*cols => n^2)

def coinCollecting(matrix, n):
  coinsCollected = [[0 for i in range(n + 1)] for j in range(n + 1)] 
  for i in range(1, len(coinsCollected)):
    for j in range(1, len(coinsCollected[i])):
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