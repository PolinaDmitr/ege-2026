def f(n):
    s = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.append(i)
            if i != n//i:
                s.append(n//i)
    return s


finish = 1_000_000_000 // 194321 * 194321
print(finish)
print()

count = 0
for i in range(finish, 99_999_999, -194321):
    d = f(i)
    c = len(d)
    if c > 0  and i % c == 0 and (i / c) % 194321 == 0:
        print(i, sum(d))
        count += 1
    if count == 5:
        break
