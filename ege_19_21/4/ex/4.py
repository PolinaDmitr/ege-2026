def f(a, b, p, c):
    if a + b >= 207 or p > c[-1]:
        return p in c
    l = [f(a + 1, b, p + 1, c),
         f(a, b + 1, p + 1, c),
         f(a * 2, b, p + 1, c),
         f(a, b * 2, p + 1, c)]
    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)

def f1(a, b, p, c):
    if a + b > 207 or p > c[-1]:
        return p in c
    l = [f(a + 1, b, p + 1, c),
         f(a, b + 1, p + 1, c),
         f(a * 2, b, p + 1, c),
         f(a, b * 2, p + 1, c)]
    return any(l)


for s in range(1, 190):
    if f1(17, s, 0, (2,)):
        print("19:", s)
        break

k = []
for s in range(1, 190):
    if f(17, s, 0, (3,)):
        k.append(s)
print("20:", k)

for s in range(1, 190):
    if f(17, s, 0, (2, 4)) and not f(17, s, 0, (2,)):
        print('21:', s)
        break
