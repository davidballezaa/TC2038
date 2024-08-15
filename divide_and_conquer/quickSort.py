# Time Complexity: O(n^2) worst O(nlogn) regular

def quickSort(arr):
  if not arr:
    return []
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quickSort(left) + middle + quickSort(right)

print(quickSort([4, 1, 3, 7, 2, 8]))
  