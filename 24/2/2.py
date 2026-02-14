from re import *

pattern = r'[1-9A-E][0-9A-E]*[05A]|[5A]'
line = open('24_2.txt').readline()
k = [x.group() for x in finditer(pattern, line)]
k_max = max(k, key = lambda x : int(x, 15))
print(k_max, int(k_max, 15))
print(line.find(k_max) + len(k_max) - 1)