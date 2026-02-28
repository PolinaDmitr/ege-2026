def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def dell(n):
    m = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if simple(i):
                m.append(i)
            dob = n // i
            if dob != i:
                if simple(dob):
                    m.append(dob)
    return m


count = 0
for i in range(7_800_001, 50_000_000):
    delit = dell(i)
    delit.sort()
    m = delit[0] + delit[-1] if len(delit) >= 2 else sum(delit)
    len_d = len(delit)
    if m % 100 == 63 and m % len_d == 0:
        print(i, m, delit)
        count += 1
    if count == 5:
        break