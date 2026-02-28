def f(x):
    d = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if x > 1:
        d.append(x)
    return d


counter = 0
for i in range(2_700_034, 4_000_035, 100):
    d = f(i)
    d2 = [x for x in d if d.count(x) >= 5]
    if len(d2) > 0:
        print(i, min(d2))
        counter += 1
    if counter == 5:
        break
