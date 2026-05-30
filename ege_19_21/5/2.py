def f(x, p, c):
    if x >= 100 or p > c[-1]:
        return p in c
    l = [f(x + 2, p + 1, c),
         f(x + 4, p + 1, c),
         f(x * 2, p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return all(l)
    return any(l)


k = []
for s in range(1, 100):
    if f(s, 0, (1, 3, 5)) and not f(s, 0, (3, )):
        k.append(s)
print(k)