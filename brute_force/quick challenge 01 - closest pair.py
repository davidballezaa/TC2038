# 1. Determina cuales son los dos puntos mas cercanos dadas sus coordenadas x, y

# Time Complexity: O(N^2)
# Space Complexity: O(1)

import os
import math

# Function to read coordinates from a file
def read_coordinates_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  # First line is the number of points
        coordinates = []
        for line in lines[1:n + 1]:
            x, y = map(float, line.strip().split())
            coordinates.append([x, y])
    return coordinates


# Function to find the two closest points
def find_closest_points(coordinates):
    min_distance = float("inf")
    min_points = []

    for i in range(len(coordinates)):
        x1, y1 = coordinates[i]
        for j in range(i + 1, len(coordinates)):
            x2, y2 = coordinates[j]
            # Distance formula
            distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
            # Update minimum distance and closest points if a smaller distance is found
            if distance < min_distance:
                min_points = [coordinates[i], coordinates[j]]
                min_distance = distance

    return min_points, min_distance


# Directory containing the files
directory = './instances/'

# List of file names
file_names = [
    'puntos-n10.txt', 'puntos-n11.txt', 'puntos-n15.txt', 'puntos-n20.txt',
    'puntos-n50.txt', 'puntos-n100.txt'
]

# Iterate over each file, read coordinates, and find the closest points
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    coordinates = read_coordinates_from_file(file_path)
    closest_points, distance = find_closest_points(coordinates)
    print(f"File: {file_name}")
    print("Puntos más cercanos entre sí:", closest_points)
    print("Distancia:", distance)
    print()
