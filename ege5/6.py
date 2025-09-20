#10
def f(n):
    s = ''
    while n != 0:
        s = str(n % 6) + s
        n //= 6
    return s


def f1(x):
    x_6 = f(x)
    s = 0
    for i in x_6:
        s += int(i)
    if s % 5 == 0:
        x_6 = '11' + x_6.replace('3', '*').replace('0', '3').replace('*', '0')
    else:
        x_6 = x_6[0] + '05' + x_6[3:] + '44'
    return int(x_6, 6)


r_min = 200_000
n_max = 0
for i in range(1, 1000):
    r = f1(i)
    if 1500 < r <= r_min:
        print(r, i)
        r_min = r
        n_max = i
print()
print(r_min, n_max)
