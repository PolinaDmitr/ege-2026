def f(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

# 194321

start = 999_999_999 // 194321 * 194321
print(start)
count = 0
for i in range(start, 0, -194321):
    d = f(i)
    if len(d) > 0 and i % len(d) == 0 and (i / len(d)) % 194321 == 0:
        print(i, sum(d))
        count += 1
    if count == 5:
        break