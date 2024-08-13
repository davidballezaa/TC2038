# 1. Determina cuales son los indices donde aparece patron en cadena 
#    usando comparaciones entre caracteres unitarios. 
#    La salida correcta deberia ser 10 y 15. Tu codigo debe averiguarlo. 
# 2. Que complejidad tiene el algoritmo.

# Time Complexity: O(N)
# Space Complexity: O(1)


cadena = "this is a small example"
patron = "is"

print("Buscando: ", patron)
print("Dentro de: ", cadena)

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

print(indicesPatron(cadena, patron))



