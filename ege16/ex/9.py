from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n < 13:
        return 13
    if n % 5 == 0:
        return 13+f(n - 1)
    return 13 - f(n - 1)

for i in range(3000):
    f(i)

print(f(3013))