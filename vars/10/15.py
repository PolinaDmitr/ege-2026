def f(x, a1, a2):
    return (not (0 <= x <= 53) and not (52 <= x <= 105) and not (a1 <= x <= a2)) <= (x ** 2 > 303601)


a = []
for a1 in range(0, 600):
    for a2 in range(a1 + 1, 601):
        if all(f(x / 2, a1, a2) for x in range(1200)):
            print(a1, a2)
            a.append(a2 - a1)
print(min(a))
