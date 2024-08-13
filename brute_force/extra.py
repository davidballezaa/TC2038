# Time Complexity: O(n^2 * m)
# Space Complexity: O(n * m)

def find_common_substrings(s1, s2):
    """
    Encuentra todas las subcadenas comunes entre dos cadenas usando un enfoque de fuerza bruta.

    Parámetros:
    s1 -- La primera cadena de caracteres.
    s2 -- La segunda cadena de caracteres.

    Salida:
    Devuelve una lista con todas las subcadenas comunes.
    """
    common_substrings = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while (i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]):
                k += 1
            if k > 0:
                common_substrings.append(s1[i:i + k])
    return common_substrings

# Ejemplo de uso
s1 = "ABCBDAB"
s2 = "BDCABC"

common_substrings = find_common_substrings(s1, s2)
longest_common_substring = max(common_substrings, key=len)
print(f"La subcadena común más larga entre '{s1}' y '{s2}' es: '{longest_common_substring}'")


"""
Pregunta: ¿Habrá forma de hacerlo más eficiente?
Sí, existe una manera mucho más eficiente de resolver el problema de la subcadena común más larga. 
El enfoque de fuerza bruta que implementamos tiene una complejidad temporal exponencial, 
ya que generamos todas las subcadenas posibles de la primera cadena y las comparamos con la segunda cadena.
El método más eficiente es utilizar **programación dinámica**, que tiene una complejidad 
de tiempo de O(m * n), donde m y n son las longitudes de las cadenas. 
Este enfoque construye una tabla que almacena los resultados de subproblemas 
más pequeños, eliminando así la necesidad de generar y comparar todas las subcadenas.
"""
