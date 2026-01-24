def f(x, p):
    if x <= 27 or p > 2:
        return p == 2
    l = [f(x - 3, p + 1), f(x - 6, p + 1), f(x // 3, p + 1)]
    if (p + 1) % 2 == 0:
        return any(l)
    return all(l)

def f2(x, p):
    if x <= 27 or p > 3:
        return p == 3
    l = [f2(x - 3, p + 1), f2(x - 6, p + 1), f2(x // 3, p + 1)]
    if (p + 1) % 2 != 0:
        return any(l)
    return all(l)

def f2_1(x, p):
    if x <= 27 or p > 1:
        return p == 1
    l = [f2_1(x - 3, p + 1), f2_1(x - 6, p + 1), f2_1(x // 3, p + 1)]
    return any(l)

def f3(x, p):
    if x <= 27 or p > 4:
        return p == 2 or p == 4
    l = [f3(x - 3, p + 1), f3(x - 6, p + 1), f3(x // 3, p + 1)]
    if (p + 1) % 2 == 0:
        return any(l)
    return all(l)


for i in range(28, 200):
    if f(i, 0):
        print(i)
print()
for i in range(28, 200):
    if f2(i, 0) and not f2_1(i, 0):
        print(i)
print()
for i in range(28, 200):
    if f3(i, 0):
        print(i)



