from re import *

file = open('24.txt')
line = file.readline()
reg = r'[1-9ABCD][0-9ABCD]*[2468AC]'

finds = findall(reg, line)
x_max = max(finds, key=lambda x: int(x, 14))
print(x_max)

print(line.find(x_max))


finds2 = [x for x in finditer(reg, line)]

max_pattern = max(finds2, key=lambda x: int(x.group(), 14))
print(max_pattern)
print(max_pattern.group())
