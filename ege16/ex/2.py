from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return n
    return n * f(n - 1)


for i in range(1, 999):
    f(i)

print(f(1000))