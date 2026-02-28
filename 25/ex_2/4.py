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
for i in range(89427151, 189427150):
    d = f(i)
    if len(d) == 8:
        double = [d.count(x) for x in d]
        if sum(double) == 2 + 2 + 2 + 2 + 1 + 1 + 1 + 1 and double[0] == 1:
            print(i, max(d), d)
            counter += 1
    if counter == 7:
        break