from re import *

p2 = [2 ** x for x in range(1, 14)]

# 8902??&
reg = r'^8902[0-9]{2}[0-9]+$'
start = 890200 // 1432 * 1432
for i in range(start, 10 ** 10, 1432):
    num_str = str(i)
    if len(findall(reg, num_str)) > 0:
        if num_str[6] != '0':
            num2 = int(num_str[6:])
            if num2 in p2:
                print(i, i // 1432)


print()
l = []
for a1 in '0123456789':
    for a2 in '0123456789':
        for a3 in p2:
            num = int(f'8902{a1}{a2}{a3}')
            if num % 1432 == 0:
                l.append(num)

l.sort()
for i in range(5):
    print(l[i], l[i] // 1432)







