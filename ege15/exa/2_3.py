def f(x, y):
    a = 4 <= x <= 82
    b = 211 % x == 0 and x not in (1, 211)
    c = y % x == 0 and x not in (1, y)
    return (b or not a) <= (not c)


delit = []
for y in range(1, 10000):
    d = [x for x in range(2, y) if y % x == 0]
    if len(d) > 0 and all(f(x, y) for x in range(1, 10000)):
        delit.append((len(d), y))

print(max(delit))