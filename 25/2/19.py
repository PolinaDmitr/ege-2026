# 1N03*6*
from re import *

def f(x):
    if x < 4:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

reg = r'^1[1-9][0-9]*03[0-9]*6[0-9]*$'

for i in range(22768, 10 ** 8, 22768):
    num = str(i)
    if len(findall(reg, num)) > 0:
        l = []
        for j in range(len(num) - 1):
            if num[j] == '0' and num[j + 1] == '3':
                l.append(j)
        last_03 = l[-1]
        num_s = int(num[1 : last_03])
        if f(num_s):
            print(i, num_s)


