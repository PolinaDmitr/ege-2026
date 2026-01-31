from functools import lru_cache

@lru_cache(maxsize=None)
def f(a, b, c_3, c_5):
    if a > b:
        return 0
    if a == b:
        return int(c_3 == c_5)
    if a % 3 == 0:
        c_3 += 1
    if a % 5 == 0:
        c_5 += 1
    return f(a + 1, b, c_3, c_5) + f(a + 4, b, c_3, c_5) + f(a * 3, b, c_3, c_5)


result = f(1, 180, 0, 0)
print(sum(int(x) for x in str(result)))