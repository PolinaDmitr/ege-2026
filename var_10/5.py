def f(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s


def alg(x):
    x4 = f(x)
    sum_x4 = sum(int(x) for x in x4)
    if sum_x4 % 4 == 0:
        r_4 = (x4.replace('3', '*')
               .replace('0', '3')
               .replace('*', '0')) + '21'
    else:
        r_4 = '11' + x4[2:] + '22'
    return int(r_4, 4)


r_min = 100000000
n_min = 0
for n in range(5, 100000):
    r = alg(n)
    if 200 < r <= r_min:
        r_min = r
        n_min = n
print(r_min, n_min)
