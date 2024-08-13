# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

def powerSetBin(n):
  """
  Genera recursivamente el conjunto potencia de n elementos en forma de listas binarias.

  Parámetro:
  n -- Un entero positivo que indica el número de elementos.

  Salida:
  Devuelve una lista con los 2^n subconjuntos representados como listas binarias.
  """

  # Caso base: si n es 1, retornamos las listas [[0], [1]]
  if n == 1:
      return [[0], [1]]

  # Caso recursivo
  else:
      # L1 contiene el conjunto potencia para n-1 elementos
      L1 = powerSetBin(n - 1)
      # L2 es una copia de L1 en orden inverso
      L2 = [subset.copy() for subset in reversed(L1)]

      # Agregar 0 al inicio de cada subconjunto en L1
      for subset in L1:
          subset.insert(0, 0)

      # Agregar 1 al inicio de cada subconjunto en L2
      for subset in L2:
          subset.insert(0, 1)

      # Retornar la concatenación de L1 y L2, que son todos los subconjuntos posibles
      return L1 + L2

# Ejemplo de uso
n = 3
result = powerSetBin(n)

# Imprimir todos los subconjuntos en formato binario, uno por línea
for subset in result:
  print(subset)
