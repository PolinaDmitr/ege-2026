def f(n):
    n_bin = bin(n)[2:]
    if n % 3 == 0:
        n_bin += n_bin[-3:]
    else:
        n_bin += bin(n % 3 * 3)[2:]
    return int(n_bin, 2)


for i in range(10000, 0, -1):
    r = f(i)
    if r < 100:
        print(i)
        break
