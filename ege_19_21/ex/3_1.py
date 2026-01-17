from functools import lru_cache

def f(x, p):
    if x <= 30 or p > 4:
        return p == 2 or p == 4
    if p % 2 == 1:
        return f(x - 3, p + 1) or f(x - 5, p + 1) or f(x // 4, p + 1)
    return f(x - 3, p + 1) and f(x - 5, p + 1) and f(x // 4, p + 1)


for i in range(31, 150):
    if f(i, 0):
        print(i)