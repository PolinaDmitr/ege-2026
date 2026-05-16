from re import *

file = open('24_4.txt')
line = file.readline()

word1 = r'([A-Z][a-z]*)'
word = r'([A-z][a-z]*)'
reg = fr'({word1}( {word})*[.])'

k = []
for i in finditer(reg, line):
    k.append(i.group(0))

k_max = max(k, key=len)
print(k_max, len(k_max), k_max.count(' ') + 1)