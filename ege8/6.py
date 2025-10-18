from math import comb, factorial

for k in range(19, 0, -1):
    count = comb(20, k)
    if 99_999 < count < 1_000_000:
        print(k, count)
        break

for k in range(19, 0, -1):
    count = factorial(20) / factorial(20 - k) / factorial(k)
    if 99_999 < count < 1_000_000:
        print(k, count)
        break