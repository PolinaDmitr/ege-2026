def f(x, a1, a2):
    return ((59 <= x <= 228) <= (a1 <= x <= a2)) or (((x % 3 == 0) <= (257 <= x <= 356)) <= ((5 <= x <= 600) <= (a1 <= x <= a2)))

l = []
for a1 in range(1, 602):
    for a2 in range(a1 + 1, 603):
        if all(f(x, a1, a2) for x in range(650)):
            l.append((a2 - a1, a1, a2))
print(min(l))

for x in range(2, 300):
    if not f(x, 59, 226):
        print(x)