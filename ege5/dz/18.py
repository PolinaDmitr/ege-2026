def f3(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

def f(x):
    x_3 = f3(x)
    count_odd = x_3.count('1')
    if len(x_3) - count_odd > count_odd:
        x_3 = '22' + x_3
    else:
        x_3 = '11' + x_3
    return int(x_3, 3)


r_min = 1000000
for i in range(11, 100000):
    r = f(i)
    if 100 < r < r_min:
        r_min = r
print(r_min)
