# 1. Determina cuales son los indices donde aparece patron en cadena
#    usando comparaciones entre caracteres unitarios.
#    La salida correcta deberia ser 10 y 15. Tu codigo debe averiguarlo.
# 2. Que complejidad tiene el algoritmo.

# Time Complexity: O(N)
# Space Complexity: O(1)

import os


# Function to read cadena and patrones from files
def read_text_and_patterns(text_file, patterns_file):
  with open(text_file, 'r') as f_text:
    cadena = f_text.read().strip()  # Read the entire content as the cadena

  with open(patterns_file, 'r') as f_patterns:
    patrones = [line.strip() for line in f_patterns.readlines()
                ]  # Each line is a different patron

  return cadena, patrones


# Function to find the indices of a patron in the cadena
def indicesPatron(cadena, patron):
  # edge case:
  if len(patron) > len(cadena):
    return False
  curr_patron_index = 0
  start_index = -1
  # iteramos por toda la cadena
  for i in range(len(cadena)):
    if cadena[i] == patron[curr_patron_index]:
      # checamos si ya iniciamos el indice
      if start_index == -1:
        start_index = i
      # si matchea y hemos acabado de recorrer el patron, retornamos True
      if curr_patron_index == len(patron) - 1:
        return [start_index, i + 1]
      curr_patron_index += 1
    else:
      # cuando no hace match, reiniciamos apuntador del patron
      start_index = -1
      curr_patron_index = 0
  return False


# File paths (relative paths)
text_file = './instances/string-matching-Texto.txt'
patterns_file = './instances/string-matching-Patrones.txt'

# Read the cadena and patrones from the files
cadena, patrones = read_text_and_patterns(text_file, patterns_file)

# Process each patron
for patron in patrones:
  print("Buscando: ", patron)
  print("Dentro de: ", cadena)
  result = indicesPatron(cadena, patron)
  if result:
    print(f"Patrón '{patron}' encontrado en índices: {result}")
  else:
    print(f"Patrón '{patron}' no encontrado")
  print()
