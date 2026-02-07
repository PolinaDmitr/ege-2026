from re import *

line = open('24_11.txt').readline()
pattern = r'(?:[18][18][DR])+'
l = findall(pattern, line)
k = max(l, key=len)
print(len(k) // 3)
