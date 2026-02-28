def f(x):
    d = set()
    i = 2
    k = 0
    while i ** 2 <= x:
        while x % i == 0:
            d.add(i)
            k += 1
            x //= i
        i += 1
    if x > 1:
        d.add(x)
        k += 1
    return d, k


counter = 0
for i in range(700_001, 1_000_000):
    d, k = f(i)
    if len(d) == 1 and k > 1:
        print(i, d)
        counter += 1
    if counter == 5:
        break
