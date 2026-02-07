def f(x, p, c):
    if x >= 82 or p > c[-1]:
        return p in c
    l = [f(x + 10, p + 1, c), f(x * 2, p + 1, c)]
    if p % 2 != c[0] % 2:
        return all(l)
    return any(l)


for i in range(1, 82):
    if f(i, 0, (2,)):
        print(i)
#36
print()
for i in range(1, 82):
    if f(i, 0, (1, 3)) and not f(i, 0, (1,)):
        print(i)
#52 61
print()
for i in range(1, 82):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        print(i)
#26