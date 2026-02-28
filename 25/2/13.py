def f(x):
    d = set()
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.add(i)
            x //= i
        i += 1
    if x > 1:
        d.add(x)
    return d


counter = 0
for i in range(5_400_001, 7_000_000):
    d = f(i)
    if len(d) > 1:
        m = min(d) + max(d)
        if m > 60_000 and str(m) == str(m)[-1 : : -1]:
            print(i, m)
            counter += 1
    if counter == 5:
        break
