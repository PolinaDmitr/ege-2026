from re import *

line = open('24_hard_2.txt').readline()
num = r'([1-9][0-9]*|[0-9])'
prod = rf'({num}[*])*[0]([*]{num})*'
pattern = rf'{prod}([+]{prod})+'
print(line[:100])
x = [x.group() for x in finditer(pattern, line)]
x_max = max(x, key=len)
print(x_max)
print(len(x_max))
