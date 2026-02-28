def f(x):
    delit = set()
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            delit.add(i)
            x //= i
        i += 1
    if x > 1:
        delit.add(x)
    return list(delit)


counter = 0
for i in range(456_790, 1_000_000):
    d = f(i)
    if len(d) >= 4:
        d.sort()
        m = d[0] + d[1] + d[-1] + d[-2]
        if m % 114 == 39:
            print(i, m, d)
            counter += 1
    if counter == 5:
        break
