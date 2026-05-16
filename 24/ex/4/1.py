from re import *

numb_not_5 = r'([1-9][0-9]*[^05]|[12346789])'
numb_5 = r'([1-9][0-9]*[05]|[5])'

numb = fr'(\({numb_not_5}[+-]{numb_5}\))'
numbs = fr'((\({numb_not_5}[+-]{numb_5}\))+)'
numbs2 = fr'({numb}+)'

file = open('24_1.txt')
line = file.readline()

k = []
for i in finditer(numbs2, line):
    k.append(i.groups()[0])

k_max = max(k, key=len)
print(k_max, len(k_max))