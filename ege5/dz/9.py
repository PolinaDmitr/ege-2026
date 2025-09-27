def f(n):
    s = ''
    while n != 0:
        s = str(n % 8) + s
        n //= 8
    return s

def f1(x):
    x_8 = f(x)
    if x_8[0] == '5':
        x_8 = '11' + x_8.replace('1', '*').replace('2', '1').replace('*', '2')
    else:
        x_8 = '2' + x_8[1:] + '10'
    return int(x_8, 8)


r_max = 0
n_max = 0
for i in range(1, 1000):
    r = f1(i)
    if r_max <= r < 1354:   #если встретим такое же r, то должны переопределять, потому что в условии стоит "максимальное n"
        r_max = r
        n_max = i

print(n_max, r_max)
