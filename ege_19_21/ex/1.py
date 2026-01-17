def f(x, p):
    if x >= 37 or p > 2:
        return p == 2
    if p % 2 == 1:
        return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 3, p + 1)
    return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x * 3, p + 1)

def f2(x, p):
    if x >= 37 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f2(x + 1, p + 1) or f2(x + 2, p + 1) or f2(x * 3, p + 1)
    return f2(x + 1, p + 1) and f2(x + 2, p + 1) and f2(x * 3, p + 1)

def f3(x, p):
    if x >= 37 and (p == 2 or p == 4):
        p2.append(p)
        return True
    if x >= 37:
        return False
    if p % 2 == 1:
        return f3(x + 1, p + 1, p2) or f3(x + 2, p + 1, p2) or f3(x * 3, p + 1, p2)
    return f3(x + 1, p + 1, p2) and f3(x + 2, p + 1, p2) and f3(x * 3, p + 1, p2)


for i in range(1, 40):
    if f(i, 0):
        print(i)

print()

for i in range(1, 40):
    if f2(i, 0):
        print(i)

print()

for i in range(1, 40):
    p2 = []
    if f3(i, 0, p2):
        print(i, p2)

