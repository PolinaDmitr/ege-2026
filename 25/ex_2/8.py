def f(x):
    d = set()
    k = 0
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.add(i)
            k += 1
            x //= i
        i += 1
    if x > 1:
        d.add(x)
        k += 1
    return k, d


print(f(3), f(9), f(12), f(625))

counter = 0
for i in range(700_001, 1_500_000):
    k, d = f(i)
    if len(d) == 1 and k > 1:
        print(i, k, d)
        counter += 1
    if counter == 5:
        break
