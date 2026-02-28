def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    s.add(1)
    return s


count = 0
for i in range(770_000 - 1, 1, -1):
    d = f(i)
    a = sum(d) // len(d)
    if a % 100 == 12:
        print(i, a)
        count += 1
    if count == 5:
        break

# 769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912
