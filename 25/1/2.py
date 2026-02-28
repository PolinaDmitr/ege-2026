def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


counter = 0
for i in range(1_125_001, 2_000_000):
    d = [x for x in f(i) if x > 7 and x % 10 == 7]
    if len(d) > 0:
        print(i, min(d))
        counter += 1
    if counter == 5:
        break



