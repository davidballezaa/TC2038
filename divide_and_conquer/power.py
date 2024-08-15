def power(a, n):
  if n == 0:
    return 1
  if n == 1:
    return a
  return power(a, n/2) * power(a, n/2) if n % 2 == 0 else power(a, n//2)*power(a, n//2 + 1)

print(power(2, 5))
print(power(2, 4))