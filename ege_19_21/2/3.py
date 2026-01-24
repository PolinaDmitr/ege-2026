def f(a, b, p, c):
    if a + b <= 200 or p > c[-1]:
        return p in c
    l = [f(a - 3, b - 4, p + 1, c), f(a - 8, b // 2, p + 1, c), f(a // 2 + a % 2, b - 10, p + 1, c)]
    if p % 2 != c[0] % 2:
        return any(l)
    return all(l)


l1 = []
for i in range(100, 350):
    if f(110, i, 0, (2,)):
        l1.append(i)
print('19 -', l1[0])

l2 = []
for i in range(100, 350):
    if f(110, i, 0, (3,)) and not f(110, i, 0, (1,)):
        l2.append(i)
print('20 -', l2[0], l2[1])

l3 = []
for i in range(100, 350):
    if f(110, i, 0, (2, 4)) and not f(110, i, 0, (2,)):
        print(i)
