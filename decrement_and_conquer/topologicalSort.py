# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# where V = vertices
# where E = edges 

from collections import deque

def topologicalSort(G):

  result = []
  
  inDegree = {node: 0 for node in G}
  
  # Calcular aristas de entrada por cada nodo
  for node in G:
    for neighbor in G[node]:
      inDegree[neighbor] += 1
  
  # Agregar nodos sin aristas de entrada a L
  L = deque([noInDegree for noInDegree in inDegree if inDegree[noInDegree] == 0])
  
  while L:
    currentNode = L.popleft()
    for neighbor in G[currentNode]:
      inDegree[neighbor] -= 1
      if inDegree[neighbor] == 0:
        L.append(neighbor)
    result.append(currentNode) 

  return result if len(result) == len(G) else "No se puede ordenar topologicamente"

G = {
  "A": ["C"],
  "B": ["C"],
  "C": ["D", "E"],
  "D": ["E"],
  "E": []
}

print(topologicalSort(G))    
