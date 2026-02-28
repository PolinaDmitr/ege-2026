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

#представить число произведением простых множителей
#12 = 2 * 2 * 3 (2, 3)

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
for i in range(1_000_001, 2_000_000):
    d_s = [x for x in f(i) if s(x)]
    if len(d_s) == 3:
        print(i, max(d_s))
        count += 1
    if count == 5:
        break
print()

count = 0
for i in range(1_000_001, 2_000_000):
    d_s = set(r(i))
    if len(d_s) == 3:
        print(i, max(d_s))
        count += 1
    if count == 5:
        break

# 1000002 166667
# 1000004 89
# 1000006 71429
# 1000012 19231
# 1000013 383
