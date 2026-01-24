def f(x, p, c):
    if x > 128 or p > c[-1]:
        return p in c
    l = [f(x + 1, p + 1, c), f(x * 2, p + 1, c)]
    if p % 2 != c[0] % 2:
        return all(l)
    return any(l)

for i in range(1, 129):
    if f(i, 0, (1, 3)):
        print(i)
print()
for i in range(1, 129):
    if f(i, 0, (2, 4)) and not f(i, 0, (2,)):
        print(i)

print()
for i in range(1, 129):
    if f(i, 0, (1, 3, 5)) and not f(i, 0, (1, 3)):
        print(i)