def f(w, b, p, c):
    if w + b < 2 or p > c[-1]:
        return p in c
    l = []
    if w - 1 >= 0:
        l.append(f(w - 1, b, p + 1, c))
    if w - 2 >= 0:
        l.append(f(w - 2, b, p + 1, c))
    if b - 1 >= 0:
        l.append(f(w , b - 1, p + 1, c))
    if b - 2 >= 0:
        l.append(f(w, b - 2, p + 1, c))

    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)

def f1(w, b, p, c):
    if w + b < 2 or p > c[-1]:
        return p in c
    l = []
    if w - 1 >= 0:
        l.append(f(w - 1, b, p + 1, c))
    if w - 2 >= 0:
        l.append(f(w - 2, b, p + 1, c))
    if b - 1 >= 0:
        l.append(f(w , b - 1, p + 1, c))
    if b - 2 >= 0:
        l.append(f(w, b - 2, p + 1, c))

    return any(l)

k_sum = []
for w in range(1, 9):
    for b in range(1, 9):
        if f1(w, b, 0, (2,)):
            k_sum.append(w + b)
print('19:', max(k_sum))

k_sum = []
for w in range(1, 9):
    for b in range(1, 9):
        if f(w, b, 0, (5,)) and not f(w, b, 0, (1, 3)):
            k_sum.append(w + b)
print('20:', min(k_sum), max(k_sum))

k = 0
for w in range(1, 9):
    for b in range(1, 9):
        if f(w, b, 0, (2, 4, 6, 8, 10, 12, 14, 16, 18)):
            k += 1
print('21:', k)

