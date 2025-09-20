#13
def f(n):
    s = ''
    while n != 0:
        s = str(n % 7) + s
        n //= 7
    return s


def f1(x):
    x_7 = f(x)
    if x % 2 == 0:
        x_7 = '52' + x_7 + '1'
    else:
        x_7 = x_7[-1] + x_7[1:len(x_7) - 1] + x_7[0] + '15'
    while x_7[0] == '0':
        x_7 = x_7[1:]
    return x_7


for i in range(1000, 0, -1):
    r = f1(i)
    if len(r) == 4:
        print(i)
        break
