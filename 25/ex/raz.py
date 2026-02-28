def fact(x):
    d = []
    i = 2  #первый простой делитель
    while i ** 2 <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if x > 1:
        d.append(x)
    return d


for i in range(20):
    print(i, fact(i))