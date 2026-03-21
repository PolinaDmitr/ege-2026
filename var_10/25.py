def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d.add(1)
    d.add(x)
    return d


count = 0
for n in range(500_001, 1_000_000):
    d = f(n)
    sum_d = sum(d)
    if sum_d % 10 == 6:
        print(n, sum_d)
        count += 1
    if count == 5:
        break