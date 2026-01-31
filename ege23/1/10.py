from functools import lru_cache


@lru_cache(maxsize=None)
def f(a, b, c1, c2):
    if a % 2 == 0:
        c1 += 1
    else:
        c2 += 1
    if a == b:
        return int(c1 == c2)
    if a > b:
        return 0
    return f(a + 2, b, c1, c2) + f(a + 3, b, c1, c2) + f(a * 3, b, c1, c2)


n = f(1, 123, 0, 0)
print(n)
print(sum(int(x) for x in str(n)))