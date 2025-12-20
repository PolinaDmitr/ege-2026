from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n <= 6:
        return 5 ** n
    return f(n - 3) + 2

for i in range(170_000):
    f(i)

print(f(100000 - 50000) + f(100000 + 50000))

