def f(x):
    delit = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            delit.append(i)
            x //= i
        i += 1
    if x > 1:
        delit.append(x)
    return delit


counter = 0
for i in range(3_502_101, 5_000_000):
    d = f(i)
    if len(d) == 4 and any(x % 10 == x // 10 for x in d):
        print(i, max(d))
        counter += 1
    if counter == 5:
        break