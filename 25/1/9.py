# 7 800 000
def s(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    s.add(1)
    return s

def r(x):
    d = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if x > 1:
        d.append(x)
    return d



count = 0
for i in range(7_800_001, 10_000_000):
    d_s = [x for x in f(i) if s(x)]
    if len(d_s) > 0:
        m = min(d_s) + max(d_s)
        if m % 100 == 63 and m % len(d_s) == 0:
            print(i, m)
            count += 1
    if count == 5:
        break
print()

count = 0
for i in range(7_800_001, 10_000_000):
    d_s = set(r(i))
    if len(d_s) > 0:
        m = min(d_s) + max(d_s)
        if m % 100 == 63 and m % len(d_s) == 0:
            print(i, m)
            count += 1
    if count == 5:
        break


# 7800610 780063
# 7801042 8463
# 7801312 1863
# 7801916 8163
# 7802032 69663



