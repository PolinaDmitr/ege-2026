def f(x):
    l = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 10 == 7 and i != 7:
                l.append(i)
            i_2 = x // i
            if i_2 != i and i_2 % 10 == 7 and i_2 != 7:
                l.append(i_2)
    return l


count = 0
for i in range(1_125_001, 2_000_000):
    l = f(i)
    if len(l) > 0:
        l.sort()
        print(i, l[0])
        count += 1
    if count == 5:
        break