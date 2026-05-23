from functools import lru_cache


@lru_cache(maxsize=None)
def f(x, p, c):
    if x <= 2143 or p > c[-1]:
        return p in c
    l = [f(x - 1, p + 1, c),
         f(x - 3, p + 1, c),
         f(x // 4 + int(x % 4 != 0), p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)


s_sum = 0
for s in range(2144, 35_000):
    if f(s, 0, (2,)):
        s_sum += s
print('19:', s_sum)

k = []
for s in range(2144, 50_000):
    if f(s, 0, (3,)):
        k.append(s)
print('20:', min(k), max(k))


count = 0
for s in range(2144, 150_000):
    if f(s, 0, (2, 4)) and not f(s, 0, (2,)):
        count += 1
print('21:', count)


