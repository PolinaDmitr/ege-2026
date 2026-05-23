def f(b, w, p, c):
    if w + b < 2 or p > c[-1]:
        return p in c
    l = []
    if b - 1 >= 0:
        l.append(f(b - 1, w, p + 1, c))
    if b - 2 >= 0:
        l.append(f(b - 2, w, p + 1, c))
    if w - 1 >= 0:
        l.append(f(b, w - 1, p + 1, c))
    if w - 2 >= 0:
        l.append(f(b, w - 2, p + 1, c))
    if (p + 1) % 2 == c[0] % 2:
        return any(l)
    return all(l)

def f1(b, w, p, c):
    if w + b < 2 or p > c[-1]:
        return p in c
    l = []
    if b - 1 >= 0:
        l.append(f(b - 1, w, p + 1, c))
    if b - 2 >= 0:
        l.append(f(b - 2, w, p + 1, c))
    if w - 1 >= 0:
        l.append(f(b, w - 1, p + 1, c))
    if w - 2 >= 0:
        l.append(f(b, w - 2, p + 1, c))
    return any(l)


k_sum = []
for b in range(1, 9):
    for w in range(1, 9):
        if f1(b, w, 0, (2,)):
            k_sum.append(b + w)
print("19:", max(k_sum))

k_sum = []
for b in range(1, 9):
    for w in range(1, 9):
        if f(b, w, 0, (1, 3, 5)) and not f(b, w, 0, (1, 3)):
            k_sum.append(b + w)
print("20:", min(k_sum), max(k_sum))

k_sum = []
for b in range(1, 9):
    for w in range(1, 9):
        if f(b, w, 0, (2, 4, 6, 8, 10, 12, 14, 16)):
            k_sum.append(b + w)
print("21:", len(k_sum))