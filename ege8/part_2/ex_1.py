from itertools import *

# a - 0, e - 1, k - 2, n - 3, o - 4, t - 5
# toonkke
# 5443221
l = sorted('kotenok', reverse=True)
print(l)
print(int('5443221', 6) + 1)
print(int('5443212', 6) + 1)

count = 1
for i in product('kotena', repeat=7):
    if sorted(i) == sorted('kotenok') and count % 2 != 0:
        print(count)
    count += 1
