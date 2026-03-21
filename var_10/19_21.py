def f1(a, b, p):
    if a + b >= 178 or p > 2:
        return p == 2
    l = [f1(a + 4, b, p + 1), f1(a, b + 3, p + 1), f1(a * 2, b, p + 1), f1(a, b * 3, p + 1)]
    return any(l)

def f2(a, b, p, c):
    if a + b >= 178 or p > c[-1]:
        return p in c
    l = [f2(a + 4, b, p + 1, c), f2(a, b + 3, p + 1, c),
         f2(a * 2, b, p + 1, c), f2(a, b * 3, p + 1, c)]
    if (p + 1) % 2 != c[-1] % 2:
        return all(l)   #когда не ход нашего игрока
    return any(l)


for s in range(1, 157):
    if f1(21, s, 0):
        print('19:', s)
        break

z20 = []
for s in range(1, 157):
    if f2(21, s, 0, (3,)):
        z20.append(s)
print('20:', sum(z20))

z21 = 1
for s in range(1, 157):
    if f2(21, s, 0, (1,3,5)) and not f2(21, s, 0, (1,3)):
        z21 *= s
print('21:', z21)
