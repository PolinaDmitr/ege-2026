def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s


start = (int(100_000_000 ** 0.5) // 9973 + 1) * 9973
print(start)
count = 0
for i in range(start, 1_000_000, 9973):
    x = i ** 2
    d = f(x)
    if len(d) == 7 and '4' in str(max(d)):
        print(x, max(d))
        count += 1
    if count == 5:
        break