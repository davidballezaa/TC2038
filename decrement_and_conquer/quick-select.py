def find_fake_coin(coins):
    l = 0
    r = len(coins) - 1

    while l <= r:
        # Divide el rango en dos mitades
        mid = l + (r - l) // 2

        # Comparar la suma de la mitad izquierda con la mitad derecha
        left_weight = sum(coins[l:mid+1])
        right_weight = sum(coins[mid+1:r+1])

        if left_weight < right_weight:
            # La moneda falsa está en la mitad izquierda
            r = mid
        elif left_weight > right_weight:
            # La moneda falsa está en la mitad derecha
            l = mid + 1
        else:
            # Caso especial si hay una sola moneda en la lista
            if r == l:
                return l
            return -1  # No se encontró la moneda falsa

    return l  # El índice de la moneda falsa

# Ejemplo de uso:
coins = [10, 10, 12, 10]  # Asumiendo que 9 es la moneda falsa
index_of_fake = find_fake_coin(coins)
print(f"La moneda falsa está en el indice: {index_of_fake}")
#la complejidad es O(Log n)