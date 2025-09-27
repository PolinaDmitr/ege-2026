def f(n):
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        n_bin = '10' + n_bin
    else:
        n_bin = '1' + n_bin + '01'
    return int(n_bin, 2)


for n in range(100, 1, -1):
    r = f(n)
    if r < 30:
        print(n)
        break
