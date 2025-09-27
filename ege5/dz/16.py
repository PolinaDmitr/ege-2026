def f8(n):
    s = ''
    while n != 0:
        s = str(n % 8) + s
        n //= 8
    return s

def f(x):
    x_8 = f8(x)
    count_even = 0
    for i in x_8:
        if i in '0246':
            count_even += 1
    if count_even % 2 != 0:
        x_8 = x_8[-3:] + '46'
    else:
        x_8 = f8(x % 6 * 5) + x_8
    return int(x_8, 8)


r_min = 100000
for i in range(80, 10000):
    r = f(i)
    r_min = min(r, r_min)
print(r_min)
