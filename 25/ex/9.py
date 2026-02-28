def fact(x):
    d = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if x > 1:
        d.append(x)
    return set(d)


count = 0
for i in range(5_700_000, 60_000_000):
    d = fact(i)
    if len(d) > 0:
        m = max(d) + min(d)
        if m > 70_000 and (m ** 0.5 == int(m ** 0.5)):
            print(i, m)
            count += 1
    if count == 5:
        break