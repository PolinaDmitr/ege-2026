def f(a, b, p, s, c):
    l = []
    delta = abs(a - b)
    k_max = max(a, b)
    k_min = min(a, b)
    if abs((k_max - 1) - (k_min + 1)) < delta:
        print(f'step {p} by a={a} b={b}', (k_max - 1), (k_min + 1))
        l.append(f((k_max - 1), (k_min + 1), p + 1, s + f'-{(k_max - 1)}-{k_min + 1}', c))
    if abs((k_max - 2) - (k_min + 2)) < delta:
        print(f'step {p} by a={a} b={b}', (k_max - 2), (k_min + 2))
        l.append(f((k_max - 2), (k_min + 2), p + 1, s + f'-{(k_max - 2)}-{k_min + 2}', c))
    if abs((k_max - 3) - (k_min + 3)) < delta:
        print(f'step {p} by a={a} b={b}', (k_max - 3), (k_min + 3))
        l.append(f((k_max - 3), (k_min + 3), p + 1, s + f'-{(k_max - 3)}-{k_min + 3}', c))
    if len(l) == 0:
        return p
        # print(f'a= {a} b= {b} p= {p} s= {s}')
    return l

# f(8, 3, 0, '')
# print()
# f(17, 7, 0, '')

print(f(8, 3, 0, '', (1,)))
print(f(17, 7, 0, '0', (1, 2, 3)))