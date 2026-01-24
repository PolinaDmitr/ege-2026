def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f1(x, p):
    if simple(x) or p > 2:
        return p == 2
    if (p + 1) % 2 == 0:
        return f1(x + 1, p + 1) or f1(x + 3, p + 1) or f1(x * 2, p + 1)
    return f1(x + 1, p + 1) and f1(x + 3, p + 1) and f1(x * 2, p + 1)

def f2(x, p):
    if simple(x) or p > 3:
        return p == 3
    if (p + 1) % 2 != 0:
        return f2(x + 1, p + 1) or f2(x + 3, p + 1) or f2(x * 2, p + 1)
    return f2(x + 1, p + 1) and f2(x + 3, p + 1) and f2(x * 2, p + 1)

def f2_1(x, p):
    if simple(x) or p > 2:
        return p == 1
    return f2_1(x + 1, p + 1) or f2_1(x + 3, p + 1) or f2_1(x * 2, p + 1)

def f3(x, p):
    if simple(x) or p > 4:
        return p == 2 or p == 4
    if (p + 1) % 2 == 0:
        return f3(x + 1, p + 1) or f3(x + 3, p + 1) or f3(x * 2, p + 1)
    return f3(x + 1, p + 1) and f3(x + 3, p + 1) and f3(x * 2, p + 1)


l = [x for x in range(1, 101) if not simple(x)]

for i in l:
    if f1(i, 0):
        print(i)
print()
for i in l:
    if f2(i, 0) and not f2_1(i, 0):
        print(i)
print()
for i in l:
    if f3(i, 0):
        print(i)
