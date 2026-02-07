from re import *

line = open('24_12.txt').readline()
pattern = r'[1-9AB][0-9AB]*[2468A]'
l = findall(pattern, line)
k_max = max(l, key=len)
print(k_max, len(k_max))
