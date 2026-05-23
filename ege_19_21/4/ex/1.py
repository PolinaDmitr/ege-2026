from functools import lru_cache


@lru_cache(maxsize=None)
def f(x, p, c):
    if x <= 2143 or p > c[-1]:
        return p in c
    l = [f(x - 1, p + 1, c),
         f(x - 3, p + 1, c),
         f(x // 4 + int(x % 4 != 0), p + 1, c)]
    if (p + 1) % 2 != c[0] % 2:
        return all(l)
    return any(l)


s = 0
for i in range(2144, 20000):
    if f(i, 0, (2,)):
        s += i
print("19:", s)

k = []
for i in range(2144, 100_000):
    if f(i, 0, (3,)):
        k.append(i)
print("20:", min(k), max(k))
count = 0
for i in range(2144, 100_000):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        count += 1
print("21:", count)
