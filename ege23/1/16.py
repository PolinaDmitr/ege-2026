def f(a, b, l):
    print(l)
    if a == b and len(l) > 0:
        return 1
    if a < 40 or a > 49:
        return 0
    m = []
    if a + 1 not in l:
        l1 = list(l)
        l1.append(a + 1)
        m.append(f(a + 1, b, l1))
    if a - 1 not in l:
        l2 = list(l)
        l2.append(a - 1)
        m.append(f(a - 1, b, l2))
    if a + 3 not in l:
        l3 = list(l)
        l3.append(a + 3)
        m.append(f(a + 3, b, l3))
    if a - 3 not in l:
        l4 = list(l)
        l4.append(a - 3)
        m.append(f(a - 3, b, l4))
    return sum(m)


print(f(42, 42, []))
t = (1, 2, 3)
t2 = (*t, 4)
print(t2)