def f(x, p, c):
    if x >= 231 or p > c[-1]:
        return p in c
    l = [f(x * 3, p + 1, c)]
    if p % 2 == 0:
        l.append(f(x + 3, p + 1, c))
    else:
        l.append(f(x + 5, p + 1, c))
    if p % 2 != c[0] % 2:
        return any(l)
    return all(l)


for i in range(10, 121):
    if f(i, 0, (2,)):
        print(i)
print()
for i in range(10, 121):
    if f(i, 0, (3,)) and not f(i, 0, (1,)):
        print(i)
print()
for i in range(10, 121):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        print(i)