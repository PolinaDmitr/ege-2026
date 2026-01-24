def f1(x, p):
    if x >= 30 or p > 3:
        return p == 3
    if (p + 1) % 3 == 0:
        return f1(x + 1, p + 1) or f1(x * 2, p + 1)
    return f1(x + 1, p + 1) or f1(x * 2, p + 1)

def f2(x, p):
    if x >= 30:
        return p % 2 != 0
    if (p + 1) % 3 == 2:
        return f2(x + 1, p + 1) and f2(x * 2, p + 1)
    return f2(x + 1, p + 1) or f2(x * 2, p + 1)

def f3(x, p):
    if x >= 30 or p > 4:
        return p == 4
    if (p + 1) % 3 == 0:
        return f3(x + 1, p + 1) and f3(x * 2, p + 1)
    return f3(x + 1, p + 1) or f3(x * 2, p + 1)


for i in range(1, 30):
    if f1(i, 0):
        print(i)
print()
for i in range(1, 30):
    if f2(i, 0):
        print(i)
print()
for i in range(1, 30):
    if f3(i, 0):
        print(i)
