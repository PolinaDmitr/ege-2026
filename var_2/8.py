from itertools import *

k = 0

for n in range(5, 13):
    seq = product('012', repeat=n)
    for i in seq:
        if i[0] == '0':
            continue
        a = 0
        for j in range(len(i) - 1):
            if (i[j] in '02') != (i[j + 1] in '02'):
                a += 1
        if a > 3:
            if int(''.join(i), 3) % sum([int(x) for x in i]) == 0:
                k += 1
                print(''.join(i))

print(k)