def f(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s


def alg(n):
    n_4 = f(n)
    if sum(int(x) for x in n_4) % 4 == 0:
        r = (n_4.replace('3', '*').replace('0', '3')
             .replace('*', '0')) + '21'
    else:
        r = '11' + n_4[2:] + '22'
    return int(r, 4)


r_min = 10000000
n_min = 0
for n in range(100000):
    r = alg(n)
    if 200 < r < r_min:
        r_min = r
        n_min = n

print(r_min, n_min)