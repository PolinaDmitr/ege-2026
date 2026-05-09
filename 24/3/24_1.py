from re import *

file = open('24_1.txt')
line = file.readline()

max_len = 0
s = ''

for i in line:
    if i in '123456789AB':
        s += i
    else:
        max_len = max(max_len, len(s))
        s = ''

print(max_len)

reg = r'[1-9AB]+'
l = findall(reg, line)

max_l = max(l, key=len)
print(max_l, len(max_l))