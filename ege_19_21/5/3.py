def f(a, b, p, c):
    if a == b or p > c[-1]:
        return p in c
    l = []
    if a < b:
        l.append(f(a + 1, b, p + 1, c))
        l.append(f(a + 3, b, p + 1, c))
    else:
        l.append(f(a, b + 1, p + 1, c))
        l.append(f(a, b + 3, p + 1, c))
    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)


for s in range(1, 24):
    if f(13, s, 0, (2,)):
        print('19:', s)
        break

k = []
for s in range(1, 24):
    if f(13, s, 0, (3,)):
        k.append(s)
print('20:', k[0], k[1])

k = []
for s in range(1, 24):
    if f(13, s, 0, (2,)):
        k.append(s)
print(k)
k = []
for s in range(1, 24):
    if f(13, s, 0, (4,)):
        k.append(s)
print(k)
k = []
for s in range(1, 24):
    if f(13, s, 0, (2,4)):
        k.append(s)
print(k)