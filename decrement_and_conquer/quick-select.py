# Time complexity: Worst O(n^2), best / average O(n)

def lomuto_partition(A, L, R):
  """
  Particiona el array usando el esquema de Lomuto basado en el pseudocódigo.

  Parámetros:
  A (list): La lista de elementos a particionar.
  L (int): El índice inicial de la porción de la lista a particionar.
  R (int): El índice final de la porción de la lista a particionar.

  Retorna:
  int: El índice del pivote después de la partición.
  """
  s = L
  pivote = A[L]

  for i in range(L + 1, R + 1):
      if A[i] < pivote:
          s = s + 1
          A[s], A[i] = A[i], A[s]

  A[s], A[L] = A[L], A[s]
  return s

def quick_select(A, L, R, k):
  """
  Encuentra el k-ésimo elemento más pequeño en la lista.

  Parámetros:
  A (list): La lista de elementos.
  L (int): El índice inicial de la porción de la lista.
  R (int): El índice final de la porción de la lista.
  k (int): El índice del k-ésimo elemento más pequeño que estamos buscando.

  Retorna:
  int: El valor del k-ésimo elemento más pequeño.
  """
  if L == R:  # Caso base: si la lista contiene solo un elemento.
      return A[L]

  # Particionar la lista y obtener el índice del pivote.
  s = lomuto_partition(A, L, R)

  # Si el pivote está en la posición k, hemos encontrado el k-ésimo elemento más pequeño.
  if s == k:
      return A[s]
  # Si el pivote está a la derecha de k, buscamos en la parte izquierda.
  elif s > k:
      return quick_select(A, L, s - 1, k)
  # Si el pivote está a la izquierda de k, buscamos en la parte derecha.
  else:
      return quick_select(A, s + 1, R, k)

# Ejemplo de uso
A = [2, 1, 4, 5, 6, 7, 24, 8, 9]
k = 2  # Queremos encontrar el tercer elemento más pequeño (k = 2 en índice 0-based)
resultado = quick_select(A, 0, len(A) - 1, k)
print(f"El {k+1}-ésimo elemento más pequeño es: {resultado}")
