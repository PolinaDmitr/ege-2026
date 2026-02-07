from re import *

file = open('24_26551.txt', 'r')
line = file.readline()
pattern = r'[1-9A-D][0-9A-D]*[02468AC]'
l = [(x.group(), int(x.group(), 14)) for x in finditer(pattern, line)]
print(l)
k = max(l, key=lambda x: x[1])
print(k)
print(len(k[0]))

file.close()
