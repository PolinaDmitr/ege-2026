from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n > 80_000:
        return 100
    return f(n + 1) * n

for i in range(80_000, 50, -1):
    f(i)


# print((f(50) // 100 + f(53)) / f(55))
print((f(50) / f(55) / 100) + (f(53) / f(55)))