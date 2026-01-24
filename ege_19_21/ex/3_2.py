import math


def f1(a, b, p):
    if a + b <= 200 or p > 2:
        return p == 2
    if (p + 1) % 2 == 0:
        return f1(a - 3, b - 4, p + 1) or f1(a - 8, b // 2, p + 1) \
            or f1((a // 2 + a % 2), b - 10, p + 1)
    return f1(a - 3, b - 4, p + 1) and f1(a - 8, b // 2, p + 1) \
            and f1((a // 2 + a % 2), b - 10, p + 1)

def f2(a, b, p):
    if a + b <= 200 or p > 3:
        return p == 3
    if (p + 1) % 2 != 0:
        return f2(a - 3, b - 4, p + 1) or f2(a - 8, b // 2, p + 1) \
            or f2((a // 2 + a % 2), b - 10, p + 1)
    return f2(a - 3, b - 4, p + 1) and f2(a - 8, b // 2, p + 1) \
            and f2((a // 2 + a % 2), b - 10, p + 1)

def f3(a, b, p):
    if a + b <= 200 or p > 4:
        return p == 4 or p == 2
    if (p + 1) % 2 == 0:
        return f3(a - 3, b - 4, p + 1) or f3(a - 8, b // 2, p + 1) \
            or f3((a // 2 + a % 2), b - 10, p + 1)
    return f3(a - 3, b - 4, p + 1) and f3(a - 8, b // 2, p + 1) \
            and f3((a // 2 + a % 2), b - 10, p + 1)



for i in range(100, 400):
    if f1(110, i, 0):
        print(i)
print()
for i in range(100, 400):
    if f2(110, i, 0):
        print(i)
print()
for i in range(100, 600):
    if f3(110, i, 0):
        print(i)


