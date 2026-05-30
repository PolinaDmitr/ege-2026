def f(x, p, c):
    if x >= 82 or p > c[-1]:
        return p in c
    l = [f(x + 10, p + 1, c),
         f(x * 2, p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return all(l)
    return any(l)


for s in range(1, 82):
    if f(s, 0, (2,)):
        print('19:', s)
        break

k = []
for s in range(1, 82):
    if f(s, 0, (1, 3)) and not f(s, 0, (1,)):
        k.append(s)
print('20:', min(k), max(k))

for s in range(1, 82):
    if f(s, 0, (2, 4)) and not f(s, 0, (2,)):
        print('21:', s)
        break