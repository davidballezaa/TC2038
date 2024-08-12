# 1. Determina cuales son los dos puntos mas cercanos dadas sus coordenadas x, y

# Time Complexity: O(N^2)
# Space Complexity: O(1)

import math

coor = [[-2.423, -8.469],
[5.721,	9.354],
[6.766,	-3.823],
[4.129,	6.744],
[5.371,	-5.404]]

min_distance = float("inf")
min_points = []

for i in range(len(coor)):
    x1, y1 = coor[i]
    for j in range(i + 1, len(coor)):
        x2, y2 = coor[j]
        # Distancia (tuve que googlear la formula lol)
        distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        # Updateamos distancia mínima y puntos más cercanos cada que sea menor
        if distance < min_distance:
            min_points = [coor[i], coor[j]]
            min_distance = distance

print("Puntos más cercanos entre sí:", min_points)
