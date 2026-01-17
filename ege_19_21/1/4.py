def f(x, c, p):
    if x <= 30 or c > p[-1]:
        return c in p
    if c % 2 != p[0] % 2:
        return f(x - 3, c + 1, p) or f(x - 5, c + 1, p) or f(x // 4, c + 1, p)
    return f(x - 3, c + 1, p) and f(x - 5, c + 1, p) and f(x // 4, c + 1, p)


for i in range(31, 150):
    if f(i, 0, (2,)):
        print(i)
print()
for i in range(31, 150):
    if f(i, 0, (3,)):
        print(i)
print()
for i in range(31, 150):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        print(i)
