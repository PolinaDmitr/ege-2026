from itertools import *

count = 0
for i in product(range(0, 25), repeat=4):
    if i[0] != 0:
        k1 = 0
        k2 = 0
        for j in i:
            if j % 2 == 0:
                k1 += 1
            if j > 15:
                k2 += 1
        if k1 == 1 and k2 <= 2:
            count += 1
print(count)

