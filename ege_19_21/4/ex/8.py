def f(x, p, c, k):
    if x < 6:
        if x % 2 != 0:
            return p in c and k >= 0
        return p not in c and k >= 0
    if (p + 1) % 2 == c[0] % 2:
        l = [f(x // 2 + x % 2, p + 1, c, k - 1)]
        if x - 3 >= 0:
            l.append(f(x - 3, p + 1, c, k - 1))
        if x - 5 >= 0:
            l.append(f(x - 5, p + 1, c, k - 1))
        return any(l)
    l = [f(x // 2 + x % 2, p + 1, c, k)]
    if x - 3 >= 0:
        l.append(f(x - 3, p + 1, c, k))
    if x - 5 >= 0:
        l.append(f(x - 5, p + 1, c, k))
    return all(l)


for x in range(6, 100):
    if f(x, 0, (1, 3), 2) and not f(x, 0, (1,), 2):
        print('19:', x)
        break