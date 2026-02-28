from re import *

reg = r'^1592[02468]*6.8$'
# print(1592608 // 1996 * 1996) #1590812

for i in range(1590812, 10**10, 1996):
    f = findall(reg, str(i))
    if len(f) != 0:
        print(i, i // 1996)