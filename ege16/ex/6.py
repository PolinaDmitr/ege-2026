from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n < 8:
        return 3 * n
    return f(n - 3) + 2

for i in range(13_000):
    f(i)


print(3 * (f(12345 - 2) + 5))