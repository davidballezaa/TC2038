# Time Complexity: O(len(C)*K)

def coin_change(C, K):
  n = len(C)
  T = [[0 for j in range(K + 1)] for i in range(n + 1)]
  T[0][0] = 1

  for i in range(n+1):
    for j in range(K+1):
      T[i][j] += T[i-1][j]
      if j - C[i-1] >= 0:
        T[i][j] += T[i][j - C[i-1]]
  return T[n][K]
    
print(coin_change([1, 2, 5, 10], 5))
  
