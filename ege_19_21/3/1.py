def f1(x, p):
    if x >= 100 or p > 2:
        return p == 2
    if p % 2 != 0:
        return f1(x + 2, p + 1) and f1(x + 4, p + 1) and f1(x * 2, p + 1)
    return f1(x + 2, p + 1) or f1(x + 4, p + 1)

def f2(x, p, c):
    if x >= 100 or p > c[-1]:
        return p in c
    l = [f2(x + 2, p + 1, c), f2(x + 4, p + 1, c), f2(x * 2, p + 1, c)]
    if p % 2 != c[0] % 2:
        return all(l)
    return any(l)


for i in range(1, 100):
    if f1(i, 0):
        print(i)
#94
print()
for i in range(1, 100):
    if f2(i, 0, (1, 3, 5)) and not f2(i, 0, (3,)):
        print(i)
#86 87 (ну вот под вопросом, почему получилось больше)
print()
for i in range(1, 100):
    if f2(i, 0, (2, 4)) and not f2(i, 0, (2,)):
        print(i)
#46 91
