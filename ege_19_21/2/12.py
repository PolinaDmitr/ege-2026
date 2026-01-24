def f1(x, p):
    if x >= 30 or p > 3:
        return p == 3
    l = [f1(x + 1, p + 1), f1(x * 2, p + 1)]
    if (p + 1) % 3 == 0:
        return any(l)
    return any(l)

def f2(x, p):
    if x >= 30:
        return p % 3 == 2
    l = [f2(x + 1, p + 1), f2(x * 2, p + 1)]
    if (p + 1) % 3 == 2:
        return all(l)
    return any(l)

def f3(x, p):
    if x >= 30 or p > 4:
        return p == 4
    l = [f3(x + 1, p + 1), f3(x * 2, p + 1)]
    if (p + 1) % 3 == 0:
        return all(l)
    return any(l)


for i in range(1, 30):
    if f1(i, 0):
        print(i)

print()
for i in range(1, 30):
    if not f2(i, 0):
        print(i)

print()
for i in range(1, 30):
    if f3(i, 0):
        print(i)

