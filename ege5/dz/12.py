def f5(n):
    s = ''
    while n != 0:
        s = str(n % 5) + s
        n //= 5
    return s


def f(x):
    x_5 = f5(x)
    if len(x_5) % 2 != 0:
        x_5 += str(x % 5)
    c = len(x_5) // 2
    x_5 = x_5[c:] + x_5[:c]
    return int(x_5, 5)


for i in range(1, 1000):
    r = f(i)
    if r > 50:
        print(i)
        break
