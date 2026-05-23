from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n >= 4300:
        return g(n - 3)
    return f(n + 2) + 2

@lru_cache(maxsize=None)
def g(n):
    if n >= 11:
        return g(n - 3) + 5
    return q(n) + 6

@lru_cache(maxsize=None)
def q(n):
    if n >= 210_000:
        return n + 4
    return q(n + 3) + 2


for i in range(210_010, 0, -1):
    q(i)

for i in range(4310):
    g(i)

for i in range(4309, 0, -1):
    f(i)

print(f(1))
