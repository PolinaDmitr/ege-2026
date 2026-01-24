def f(a, b, m):
    if a + b <= 60:
        return m % 2 == 0
    if m == 0:
        return 0
    t = [f(a - 5, b, m - 1), f(a, b - 3, m - 1), f(a // 2, b, m - 1), f(a, (b + 1) // 2, m - 1)]
    return any(t) if m % 2 != 0 else all(t)

def f1(a, b, m):
    if a + b <= 60:
        return m % 2 == 0
    if m == 0:
        return 0
    t = [f1(a - 5, b, m - 1), f1(a, b - 3, m - 1), f1(a // 2, b, m - 1), f1(a, (b + 1) // 2, m - 1)]
    return any(t) if m % 2 != 0 else any(t)

print(max([S for S in range(5, 151) if f1(130, S, 2)]))
print(*sorted([S for S in range(5, 151) if not f(130, S, 1) and f(130, S, 3)])[:2])
p = 1
for S in range(5, 151):
    if not f(130, S, 3) and f(130, S, 5):
        p *= S
print(p)