def f(x):
    s = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


count = 0
for i in range(500_001, 1_000_000):
    r = sum(f(i))
    if r % 10 == 6:
        print(i, r)
        count += 1
    if count == 5:
        break