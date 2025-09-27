def f(n):
    s = ''
    while n != 0:
        s = str(n % 4) + s
        n //= 4
    return s


def f1(x):
    x_4 = f(x)
    x_sum = 0
    for i in x_4:
        x_sum += int(i)
    if x_sum % 4 == 0:
        x_4 = x_4.replace('3', '*').replace('0', '3').replace('*', '0') + '21'
    else:
        x_4 += '22'
        x_4 = '11' + x_4[2:]    #x_4 может быть однозначным числом, поэтому сначала приписываем, потом отрезаем два первых разряда
    return int(x_4, 4)


r_min = 1000000 #заведомо большое
n_min = 0
for i in range(1, 10000):
    r = f1(i)
    if 200 < r < r_min:     #строгое, потому что нужно наименьшее n
        r_min = r
        n_min = i

print(r_min, n_min)
