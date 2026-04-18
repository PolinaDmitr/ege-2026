def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s

def funct(x, y):
    a = 4 <= x <= 82
    # b = 211 % x == 0 and x not in (1, 211)
    c = y % x == 0 and x not in (1, y)
    # return (b or not a) <= (not c)
    return (not a) <= (not c)

l = []

for y in range(1, 10000):
    d = [x for x in range(2, y) if y % x == 0]
    if len(d) > 0 and all(funct(x, y) for x in range(1, 10000)):
        l.append((len(d), y))

print(max(l))


# к задаче 11
print(len(f(404)) + 2)
