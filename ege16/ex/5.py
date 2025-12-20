from functools import lru_cache


@lru_cache(maxsize=None)
def g(n):
    if n < 100:
        return n
    return f(n - 3) + 1

@lru_cache(maxsize=None)
def f(n):
    return g(n - 2)

@lru_cache(maxsize=None)
def g1(n):
    if n < 100:
        return n
    return g(n - 5) + 1

for i in range(100, 5000):
    g(i)
    g1(i)


print(f(5000))
print(g1(5000 - 2))