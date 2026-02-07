from re import *

line = open('24_10.txt').readline()
pattern = r'(?:[18]{2}[DR])*'
l = findall(pattern, line)
k = max(l, key=len)
print(len(k) / 3)