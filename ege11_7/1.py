from math import *

for n in range(1, 500):
    i_1 = 180 + ceil(log2(n))
    i_serial = ceil(i_1 / 8)
    info = (i_serial + 110) * n
    if info < 45 * 1024:
        print('yes', n)
    else:
        break