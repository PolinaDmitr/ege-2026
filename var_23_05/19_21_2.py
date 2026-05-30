def f1(x, p, c):
    if x >= 125 or p > c[-1]:
        return p in c
    l = [f1(x + 2, p + 1, c),
         f1(x + 4, p + 1, c),
         f1(x * 2, p + 1, c)]
    return any(l)

def f(x, p, c):
    if x >= 125 or p > c[-1]:
        return p in c
    l = [f(x + 2, p + 1, c),
         f(x + 4, p + 1, c),
         f(x * 2, p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return all(l)
    return any(l)

for s in range(1, 125):
    if f1(s, 0, (1, )):
        print('19:', s)
        break

k = []
for s in range(1, 125):
    if f(s, 0, (2,)):
        k.append(s)
print('20:', k[0], k[1])

for s in range(1, 125):
    if f(s, 0, (2, 4,)) and not f(s, 0, (2,)):
        print('21:', s)



