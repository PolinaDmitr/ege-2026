def f1(x, p):
    if x < 28 or p > 2:
        return p == 2
    if (p + 1) % 2 == 0:
        return f1(x - 3, p + 1) or f1(x - 6, p + 1) or f1(x // 3, p + 1)
    return f1(x - 3, p + 1) and f1(x - 6, p + 1) and f1(x // 3, p + 1)

def f2(x, p):
    if x < 28 or p > 3:
        return p == 3
    if (p + 1) % 2 != 0:
        return f2(x - 3, p + 1) or f2(x - 6, p + 1) or f2(x // 3, p + 1)
    return f2(x - 3, p + 1) and f2(x - 6, p + 1) and f2(x // 3, p + 1)

def f3(x, p):
    if x < 28 or p > 4:
        return p == 2 or p == 4
    if (p + 1) % 2 == 0:
        return f3(x - 3, p + 1) or f3(x - 6, p + 1) or f3(x // 3, p + 1)
    return f3(x - 3, p + 1) and f3(x - 6, p + 1) and f3(x // 3, p + 1)




for i in range(28, 150):
    if f1(i, 0):
        print(i)
print()
for i in range(28, 150):
    if f2(i, 0):
        print(i)
print()
for i in range(28, 150):
    if f3(i, 0):
        print(i)