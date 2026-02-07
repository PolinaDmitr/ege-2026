def d(x):
    l = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    if len(l) > 0:
        return l
    return {1}


def f(x, p, c):
    if x >= 63 or p > c[-1]:
        return p in c
    steps = d(x)
    l = []
    for j in steps:
        l.append(f(x + j, p + 1, c))
    if p % 2 != c[0] % 2:
        return any(l)
    return all(l)


for i in range(1, 63):
    if f(i, 0, (2,)):
        print(i)
#39
print()
for i in range(1, 63):
    if f(i, 0, (3,)) and not f(i, 0, (1,)):
        print(i)
#26, 40
print()
for i in range(1, 63):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        print(i)
#38

