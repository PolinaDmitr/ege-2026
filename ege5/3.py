#4
def f(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s


def f1(x):
    x_3 = f(x)
    if x % 3 == 0:
        x_3 += x_3[-2:]
    else:
        x_3 += f((x % 3) * 3)
    return int(x_3, 3)


for i in range(1, 100):
    r = f1(i)
    print(i, r)
    if r > 150:
        break
