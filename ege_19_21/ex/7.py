def f(x1, x2, p):
    if x1 + x2 >= 100 or p > 2:
        return p == 2
    if p % 2 == 1:
        return f(x1 + 3, x2, p + 1) or f(x1 * 2, x2, p + 1) or \
            f(x1, x2 + 3, p + 1) or f(x1, x2 * 2, p + 1)
    return f(x1 + 3, x2, p + 1) and f(x1 * 2, x2, p + 1) and \
        f(x1, x2 + 3, p + 1) and f(x1, x2 * 2, p + 1)


for i in range(1, 83):
    if f(17, i, 0):
        print(i)