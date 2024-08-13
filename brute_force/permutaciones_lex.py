# Time Complexity: O(n!)
# Space Complexity: O(n!)


def permutacionesLex(n):
    """
  Genera todas las permutaciones de n elementos en orden lexicográfico.

  Parámetro:
  n -- Un entero positivo que indica el número de elementos a permutar.

  Salida:
  Devuelve una lista con todas las permutaciones posibles en orden lexicográfico.
  """

    # Inicializamos p con la permutación base [1, 2, ..., n]
    p = list(range(1, n + 1))
    # Lista para almacenar las permutaciones
    L = []
    # Agregamos la permutación inicial a la lista
    L.append(p.copy())

    while True:
        # 1. Encontramos el mayor índice i tal que p[i] < p[i + 1]
        i = len(p) - 2
        while i >= 0 and p[i] >= p[i + 1]:
            i -= 1
        # Si no se encuentra tal índice, se han generado todas las permutaciones
        if i == -1:
            break

        # 2. Encontramos el mayor índice j tal que p[i] < p[j]
        j = len(p) - 1
        while p[i] >= p[j]:
            j -= 1

        # 3. Intercambiamos p[i] con p[j]
        p[i], p[j] = p[j], p[i]

        # 4. Invertimos el orden de la sección p[i+1] hasta p[n-1]
        p = p[:i + 1] + p[i + 1:][::-1]

        # 5. Agregamos la nueva permutación a la lista L
        L.append(p.copy())

    # Imprimir todas las permutaciones en orden lexicográfico
    for perm in L:
        print(perm)

    return L


# Ejemplo de uso
n = 3
permutacionesLex(n)
