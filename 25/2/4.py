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
for i in range(89_427_151, 100_000_000):
    d = f(i)
    if len(d) == 8:
        d.sort()
        d2 = [d.count(x) for x in d]
        if d2.count(2) == 4 and d2.count(1) == 4 and d2[0] == 1:
            print(i, max(d))
            counter += 1
    if counter == 7:
        break
