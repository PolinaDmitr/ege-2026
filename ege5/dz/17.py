def f3(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

def f(x):
    x_3 = f3(x)
    x_sum = 0
    for i in x_3:
        x_sum += int(i)
    if x_sum % 4 == 0:
        x_3 = '1' + x_3
        x_3 = x_3[:-2]
    else:
        x_3 += f3(x_sum % 4 * 3)
    return int(x_3, 3)


r_min = 1000000
for i in range(1, 100000):
    r = f(i)
    if 353 < r < r_min:
        r_min = r
print(r_min)