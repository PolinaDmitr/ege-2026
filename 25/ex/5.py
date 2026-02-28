def f(x):
    s = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return list(s)


for i in range(178965, 178982 + 1):
    d = f(i)
    if len(d) == 4:
        d.sort()
        print(i, d)