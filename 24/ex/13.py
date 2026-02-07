from re import *

line = open('24_13.txt').readline()
numb = r'[1-9][0-9]*[02468])|[02468]'
pattern = rf'{numb}([*+]{numb})+'
l = findall(pattern, line)
k = max(l, key=len)
print(k, len(k))