from re import *

file = open('17_1.txt')
line = file.readline()

s = ''
max_k = 1
k = 1
for i in range(len(line)):
    if line[i] in '123456789AB':
        s += line[i]
        k += 1
    else:
        max_k = max(k, max_k)
        k = 0
        s = ''
print(max_k)
print('------------')

reg = '[123456789AB]+'
m = findall(reg, line)
print(len(max(m, key=len)))
