from re import *

file = open('24_1.txt')
line = file.readline()

numb_5 = r'([1-9][0-9]*[05]|[5])'
numb_not_5 = r'([1-9][0-9]*[12346789]|[12346789])'

numbs = fr'((\({numb_not_5}[+-]{numb_5}\))+)'

k = []
for i in finditer(numbs, line):
    k.append(i.group())

k_max = max(k, key=len)

print(k_max, len(k_max))