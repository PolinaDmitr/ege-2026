from re import *

numb_a = r'([1-9][0-9]*[02468]|[2468])'
numb_b = r'([1-9][0-9]*[13579]|[13579])'

numb = fr'(\({numb_a}[+-]{numb_b}\))'
numbs = fr'{numb}+'

file = open('24_2.txt')
line = file.readline()

k = []

for i in finditer(numbs, line):
    k.append(i.group(0))

k_max = max(k, key=len)
print(k_max, len(k_max))