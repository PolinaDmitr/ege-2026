def f(x, p):
    if x < 20 or p > 3:
        return p == 3
    if (p + 1) % 2 == 0:
        return f(x - 10, p + 1) or f(x // 2, p + 1)
    return f(x - 10, p + 1) and f(x // 2, p + 1)

def f2(x, p):
    if x < 20 or p > 4:
        return p == 4
    if (p + 1) % 2 != 0:
        return f2(x - 10, p + 1) or f2(x // 2, p + 1)
    return f2(x - 10, p + 1) and f2(x // 2, p + 1)

def f3(x, p):
    if x < 20 or p > 5:
        return p == 5
    if (p + 1) % 2 == 0:
        return f3(x - 10, p + 1) or f3(x // 2, p + 1)
    return f3(x - 10, p + 1) and f3(x // 2, p + 1)


for i in range(31, 150):
    if f(i, 0):
        print(i)
print()
for i in range(31, 200):
    if f2(i, 0):
        print(i)
print()
for i in range(31, 200):
    if f3(i, 0):
        print(i)