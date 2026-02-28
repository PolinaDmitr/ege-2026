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
for i in range(2_700_034, 3_700_035, 100):
    d = f(i)
    d.sort()
    l = [d.count(x) for x in d]
    if any(x >= 5 for x in l):
        print(i, [d[x] for x in range(len(l)) if l[x] >= 5][0])
        counter +=1
    if counter == 5:
        break
