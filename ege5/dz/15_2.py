def f(n):
    n_bin = bin(n)[2:]
    n_bin += bin(n % 4)[2:]
    return int(n_bin, 2)


l = [f(n) for n in range(1, 1000)]
l.sort()
m = []
for i in range(len(l)):
    count = 0
    j = i
    l_i = l[i]
    while j < len(l) and (l[j] < l[i] + 65):
        count += 1
        j += 1
    m.append(count)

print(max(m))
