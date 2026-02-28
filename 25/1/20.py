from re import *
# 1592#6?8

pattern = r'^1592[02468]*6.8$'

print(15920608 // 1996 * 1996)  #15920096

for i in range(15920096, 10 ** 10, 1996):
    f = findall(pattern, str(i))
    if len(f) > 0:
        print(i, i // 1996)

# 1592464688 797828
# 1592484648 797838
