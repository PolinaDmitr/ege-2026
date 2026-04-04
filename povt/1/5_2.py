def f(n):
    n_bin = bin(n)[2:]
    one1 = 0
    zero2 = 0
    for i in range(1, len(n_bin), 2):
        if n_bin[i] == '1':
            one1 += 1
    for i in range(0, len(n_bin), 2):
        if n_bin[i] == '0':
            zero2 += 1
    return abs(one1 - zero2)



for n in range(2, 100000):
    if f(n) == 5:
        print(n)
        break