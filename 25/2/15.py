def f(x):
    d = set()
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.add(i)
            x //= i
        i += 1
    if x > 1:
        d.add(x)
    return d


counter = 0
for i in range(749999, 1, -1):
    d = f(i)
    l = [x for x in d if x % 10 == 7]
    if len(l) > 0:
        a = sum(l) // len(l)
        if a % 111 == 0:
            print(i, a)
            counter += 1
    if counter == 5:
        break

print(f(748663))