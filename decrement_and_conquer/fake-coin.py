# Time complexity: O(log3(n))

def encontrar_moneda_falsa(monedas, inicio=0, moneda_legitima=None):
    """
    Encuentra la moneda falsa en un conjunto de monedas.

    Parámetros:
    monedas (list): Lista de pesos de las monedas. Se asume que una sola moneda tiene un peso diferente.
    inicio (int): Índice de inicio para ajustar la posición de la moneda en la lista original.
    moneda_legitima (int): Peso de una moneda que se sabe legítima, para comparación.

    Retorna:
    int: El índice de la moneda falsa en la lista original.
    """

    n = len(monedas)

    # Caso base: si solo queda una moneda, esa es la falsa
    if n == 1:
        return inicio

    # Caso especial: si quedan dos monedas, comparamos con una moneda legítima
    if n == 2:
        if moneda_legitima is not None:
            if monedas[0] == moneda_legitima:
                return inicio + 1  # La segunda moneda es la falsa
            else:
                return inicio  # La primera moneda es la falsa
        else:
            # Si no tenemos una moneda legítima, usamos cualquier otra del tercer grupo.
            return inicio if monedas[0] != monedas[1] else inicio + 1

    # Divide el conjunto de monedas en tres grupos
    tercio = n // 3

    grupo1 = monedas[:tercio]
    grupo2 = monedas[tercio:2*tercio]
    grupo3 = monedas[2*tercio:] if 2*tercio < n else []

    # Compara los pesos de los dos primeros grupos usando una balanza imaginaria
    peso_grupo1 = sum(grupo1)
    peso_grupo2 = sum(grupo2)

    if peso_grupo1 == peso_grupo2:
        # La moneda falsa está en el tercer grupo (los otros dos tienen el mismo peso)
        # Usamos una moneda del grupo 1 como moneda legítima para la siguiente comparación
        return encontrar_moneda_falsa(grupo3, inicio + 2 * tercio, grupo1[0])
    else:
        # La moneda falsa está en el grupo1 o grupo2
        # Usamos una moneda del tercer grupo si no está vacío como legítima, porque no ha sido comparado,
        # o en caso de que no exista un tercer grupo, continuamos la búsqueda.
        return encontrar_moneda_falsa(grupo1 + grupo2, inicio, grupo3[0] if grupo3 else None)

indice_falsa = encontrar_moneda_falsa([1, 1, 1, 1, 1, 1, 1, 100, 1, 1, 1]) # 7
print(f"La moneda falsa está en el índice: {indice_falsa}")
