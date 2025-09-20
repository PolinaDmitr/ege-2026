#5
def f(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s


def f1(x):
    x_3 = f(x)
    s = 0
    for i in x_3:
        s += int(i)
    # s2 = x_3.count('1') + x_3.count('2') * 2
    # print(s == s2, s, x_3)
    if s % 2 == 0:
        x_3 = '12' + x_3[2:] + '0'
    else:
        x_3 = '10' + x_3[2:] + '2'
    # print(x_3)
    return int(x_3, 3)


for i in range(1, 100):
    r = f1(i)
    if r > 105:
        print(i)
