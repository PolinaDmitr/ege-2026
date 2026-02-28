def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if simple(i):
                s.add(i)
            i2 = x // i
            if simple(i2):
                s.add(i2)
    return s


count = 0
for i in range(1_000_001, 2_000_000):
    d = f(i)
    if len(d) == 3:
        print(i, max(d))
        count += 1
    if count == 5:
        break

print(f(1000002))