def f(a, b, c, p):
    if a + b >= 100 or c > p[-1]:
        return c in p
    if c % 2 != p[0] % 2:
        return f(a + 3, b, c + 1, p) or f(a * 2, b, c + 1, p) or \
            f(a, b + 3, c + 1, p) or f(a, b * 2, c + 1, p)
    return f(a + 3, b, c + 1, p) and f(a * 2, b, c + 1, p) and \
            f(a, b + 3, c + 1, p) and f(a, b * 2, c + 1, p)

def f2(x, c):
    if x >= 82 or c > 3:
        return c == 3
    if c % 2 == 1:
        return f2(x + 2, c + 1) and f2(x + 4, c + 1) and f2(x * 3, c + 1)
    return f2(x + 2, c + 1) or f2(x + 4, c + 1) or f2(x * 3, c + 1)


for i in range(1, 83):
    if f(17, i, 0, (2,)):
        print(i)
print()
for i in range(1, 83):
    if f(17, i, 0, (3,)):
        print(i)
print()
for i in range(1, 83):
    if f(17, i, 0, (2, 4)) and not f(17, i, 0, (2,)):
        print(i)
