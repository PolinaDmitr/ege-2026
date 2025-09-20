#8
def f(n):
    s = ''
    while n != 0:
        s = str(n % 9) + s
        n //= 9
    return s


def f1(x):
    x_9 = f(x)
    # print(x_9)
    if x_9[0] == '7':
        x_9 = '34' + x_9.replace('3', '*').replace('6', '3').replace('*', '6')
    else:
        x_9 = '3' + x_9[1:] + '45'
    # print(x_9)
    return int(x_9, 9)


for i in range(1000, 1, -1):
    r = f1(i)
    if r < 2876:
        print(i)
        break
