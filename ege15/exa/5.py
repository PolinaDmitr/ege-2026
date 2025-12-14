def f(x):
    return (25 <= x <= 64) <= (((40 <= x <= 115) and (not (a1 <= x <= a2))) <= (not (25 <= x <= 64)))

l = []
for a1 in range(20, 120):
    for a2 in range(a1 + 1, 121):
        if all(f(x) for x in range(150)):
            l.append(a2 - a1)
print(min(l))