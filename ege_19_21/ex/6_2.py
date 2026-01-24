

def f1(x, p):
    if x <= 19 or p > 2:
        return p == 2
    l = [f1(x - 5, p + 1)]
    if x % 2 == 0:
        l.append(f1(x // 2, p + 1))
    if x % 3 == 0:
        l.append(f1(x // 3, p + 1))
    if x % 2 != 0 and x % 3 != 0:
        l.append(f1(x + 1, p + 1))
    if (p + 1) % 2 == 0:
        return any(l)
    return all(l)


for i in range(20, 100):
    if f1(i, 0):
        print(i)