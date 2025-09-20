#3
def f(n):
    n_bin = bin(n)[2:]
    n_bin += str(n_bin.count('1') % 2)
    n_bin += str(n_bin.count('1') % 2)
    return int(n_bin, 2)

# def f1(n):
#     n_bin = bin(n)[2:]
#     if n_bin.count('1') % 2 == 0:
#         n_bin += '00'
#     else:
#         n_bin += '10'
#     return int(n_bin, 2)


for i in range(1, 250):
    r = f(i)
    if r > 253:
        print(i)
        break
