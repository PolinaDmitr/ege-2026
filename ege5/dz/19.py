def f(n):
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        n_bin_sum = n_bin.count('1')
        n_bin = bin(n_bin_sum)[2:] + n_bin
        n_bin += str(n_bin_sum % 2)     #только на примере понятно, что бит чётности от изначального n
    else:
        n_bin_sum = n_bin.count('1')
        n_bin = n_bin + '0' + bin(n_bin_sum)[2:]
    return int(n_bin, 2)


n_min = 0
r_max = 0
for i in range(1, 1000000):
    r = f(i)
    if r_max < r < 256:
        r_max = r
        n_min = i
print(r_max, n_min)
