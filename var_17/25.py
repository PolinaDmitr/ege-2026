def simp(x):
    d = set()
    i = 2
    while x >= i ** 2:
        while x % i == 0:
            d.add(i)
            x //= i
        i += 1
    if x != 1 and len(d) != 0:
        d.add(x)
    return d


l = []
k = 0
for n in range(9_500_001, 10_000_000):
    d = simp(n)
    if d and sum(d)//len(d) % 813 == 0:
        # print(n, sum(d)/len(d), d)
        l.append((n, sum(d) // len(d)))
        k += 1
    if k == 5:
        break

l.sort(key=lambda x: x[1])
print(l)