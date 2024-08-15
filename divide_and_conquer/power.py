# Time complexity: Since we're not saving results, we're doing O(N)
# If we saved the results of our computations, we would have O(logN) complexity

def power(a, n):
  if n == 0:
    return 1
  if n == 1:
    return a
  return power(a, n/2) * power(a, n/2) if n % 2 == 0 else power(a, n//2)*power(a, n//2 + 1)

print(power(2, 5))
print(power(2, 4))