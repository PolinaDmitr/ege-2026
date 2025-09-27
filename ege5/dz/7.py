def f(n):
    s = ''
    while n != 0:
        s = str(n % 4) + s
        n //= 4
    return s

def f1(x):
    x_4 = f(x)
    if x % 4 == 0:
        x_4 = '2' + x_4 + '03'
    else:
        x_4 += f(x % 4 * 5)
    return int(x_4, 4)


for i in range(1000, 1, -1):
    r = f1(i)
    if r <= 567:
        print(i)
        break
