def f(x):
    s = {1,}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


count = 0
for i in range(770_000, 0, -1):
    d = f(i)
    ar = sum(d)// len(d)
    if ar % 100 == 12:
        print(i, ar)
        count += 1
    if count == 5:
        break

d = f(769995)
print(d, sum(d), len(d), sum(d) // len(d))