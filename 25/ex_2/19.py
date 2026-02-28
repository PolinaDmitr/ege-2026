from re import *

def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

# 1N03*6*
reg = r'^1[1-9][0-9]*03[0-9]*6[0-9]*$'

for i in range(22768, 10 ** 8, 22768):
    s = str(i)
    if len(findall(reg, s)) > 0:
        l = []
        for j in range(len(s) - 1):
            if s[j] == '0' and s[j + 1] == '3':
                l.append(j)
        last03 = l[-1]
        sost = s[1 : last03]
        if sost[0] == '0':
            continue
        numb = int(sost)
        if f(numb):
            print(i, numb)

