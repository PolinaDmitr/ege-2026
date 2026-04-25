from math import dist

s = []
for i in range(-100, 100):
    if dist((-1, i), (0, 0)) <= 20:
        s.append(i)
print(s)
print('19 zad:', len(s))


def f(a, b, k, c):
    if dist((a, b), (0, 0)) > 20 or k > c[-1]:
        return k in c
    l = [f(a - 10, b + 5, k + 1, c), f(a - 5, b - 5, k + 1, c), f(a + 5, b - 5, k + 1, c)]
    if k % 2 == c[-1] % 2:
        return all(l)
    return any(l)

k1 = 0
k2 = 0
for i in s:
    if f(-1, i, 1, (2,)):
        k1 += 1
    elif f(-1, i, 1, (4,)):
        k2 += 1
print('zad 20: ', k1, k2)


s3 = []
for i in s:
    if f(-1, i, 1, (3, 5)) and not f(-1, i, 1, (3,)):
        s3.append(i)
print(s3)
print('zad 21', max(s3))


