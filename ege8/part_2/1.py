from itertools import *


# a - 0, e - 1, k - 2, n- 3, o - 4, t - 5
# k o t e n o k
# toonkke - 5443221
print(int('5443221', 6) + 1)
# 5443212
print(int('5443212', 6) + 1)

num = 1
for i in product(sorted('kotena'), repeat=7):
    if sorted(i) == sorted('kotenok'):
        if num % 2 != 0:
            print(i, num)
    num += 1
#270927
