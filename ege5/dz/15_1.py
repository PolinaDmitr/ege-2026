def f(n):
    n_bin = bin(n)[2:]
    if (int(n_bin[:-1], 2) % 4) == int(n_bin[-1]):
        return True
    if (len(n_bin) > 2) and (int(n_bin[:-2]) % 4 == (int(n_bin[-2:], 2)) and n_bin[-2:] in ('10', '11')):   #нужно обратить внимание на условие с остатками
        return True
    return False


l = []
for i in range(2, 1000):
    count = 0
    for j in range(i, i + 65):
        if f(j):
            count += 1
            # print(j, bin(j))
    l.append(count)
print(l)
print(max(l))
