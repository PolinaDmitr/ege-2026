def f1(a, b, p):
    if a + b <= 60 or p > 2:
        return p == 2
    if (p + 1) % 2 == 0:
        return f1(a - 5, b, p + 1) or f1(a, b - 3, p + 1) \
            or f1(a // 2, b, p + 1) or f1(a, b // 2 + b % 2, p + 1)
    return f1(a - 5, b, p + 1) or f1(a, b - 3, p + 1) \
        or f1(a // 2, b, p + 1) or f1(a, b // 2 + b % 2, p + 1)

def f2(a, b, p):
    if a + b <= 60 or p > 3:
        return p == 3
    if (p + 1) % 2 != 0:
        return f2(a - 5, b, p + 1) or f2(a, b - 3, p + 1) \
            or f2(a // 2, b, p + 1) or f2(a, b // 2 + b % 2, p + 1)
    return f2(a - 5, b, p + 1) and f2(a, b - 3, p + 1) \
        and f2(a // 2, b, p + 1) and f2(a, b // 2 + b % 2, p + 1)

def f3(a, b, p):
    if a + b <= 60 or p > 5:
        return p == 3 or p == 5
    if (p + 1) % 2 != 0:
        return f3(a - 5, b, p + 1) or f3(a, b - 3, p + 1) \
            or f3(a // 2, b, p + 1) or f3(a, b // 2 + b % 2, p + 1)
    return f3(a - 5, b, p + 1) and f3(a, b - 3, p + 1) \
        and f3(a // 2, b, p + 1) and f3(a, b // 2 + b % 2, p + 1)


for i in range(5, 151):
    if f1(130, i, 0):
        print(i)
print()

for i in range(5, 151):
    if f2(130, i, 0):
        print(i)

print()

for i in range(5, 151):
    if f3(130, i, 0):
        print(i)