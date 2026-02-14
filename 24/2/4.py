from re import *

num = r'([1-9][0-9]{3}[.][0-9]+)'
pattern = rf'{num}[&]{num}'
line = open('24_4.txt').readline()
k = [x.group() for x in finditer(pattern, line)]
k_max = max(k, key=len)
print(k)
print(k_max, len(k_max))