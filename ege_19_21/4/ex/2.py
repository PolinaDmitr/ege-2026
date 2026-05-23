from functools import lru_cache


@lru_cache(maxsize=None)
def f(x, p, c):
    if x <= 3214 or p > c[-1]:
        return p in c
    l = [f(x - 4, p + 1, c), f(x - 5, p + 1, c),
         f(x // 3 + int(x % 3 != 0), p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)

s_sum = 0
for s in range(3215, 30_000):
    if f(s, 0, (2,)):
        s_sum += s
print("19:", s_sum)

k = []
for s in range(3215, 30_000):
    if f(s, 0, (3,)):
        k.append(s)
print("20:", max(k), min(k))

count = 0
for s in range(3215, 30_000):
    if f(s, 0, (2,4)) and not f(s, 0, (2,)):
        count += 1
print("21:", count)