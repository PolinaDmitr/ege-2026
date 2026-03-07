def f(n):
    s = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.append(i)
            if i != n//i:
                s.append(n//i)
    return s


print(f(9973))
start = (int(100000000 ** 0.5)// 9973 + 1) * 9973
print(int(100000000 ** 0.5), start, start ** 2)
print()

count = 0
for i in range(start, 1_000_000, 9973):
    x = i ** 2
    d = f(x)
    if len(d) == 7 and '4' in str(max(d)):
        print(x, max(d))
        count += 1
    if count == 5:
        break
