def f(x, p):
    if x < 20 or p > 3:
        return p == 3
    l = [f(x - 10, p + 1), f(x // 2, p + 1)]
    if p % 2 != 0:
        return any(l)
    return all(l)

def f2(x, p):
    if x < 20 or p > 4:
        return p == 4
    l = [f2(x - 10, p + 1), f2(x // 2, p + 1)]
    if p % 2 == 0:
        return any(l)
    return all(l)

def f3(x, p):
    if x < 20 or p > 5:
        return p == 5
    l = [f3(x - 10, p + 1), f3(x // 2, p + 1)]
    if p % 2 != 0:
        return any(l)
    return all(l)

for i in range(31, 200):
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