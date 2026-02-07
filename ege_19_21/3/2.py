def f(x, p, c):
    if x >= 97 or p > c[-1]:
        return p in c
    l = [f(x + 1, p + 1, c), f(x + 3, p + 1, c), f(x + 5, p + 1, c),
         f(x + 7, p + 1, c), f(x + 8, p + 1, c), f(x + 12, p + 1, c)]
    if p % 2 != c[0] % 2:
        return any(l)
    return all(l)

def g(s_, m_):
    x = 0
    for i in range(1, s_ + 1):
        x += m_ * i
    return x


for s in range(1, 11):
    for m in range(2, 21):
        x = g(s, m)
        if f(x, 0, (2,)):
            print(s, m)
#3
print()
for s in range(1, 11):
    for m in range(2, 21):
        x = g(s, m)
        if f(x, 0, (1,)):
            print(s, m)
#9
print()
for s in range(1, 11):
    for m in range(2, 21):
        x = g(s, m)
        if f(x, 0, (3,)):
            print(s, m)
#8 3
