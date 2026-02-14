from re import *

l =  open('24_13.txt').readline()
print(l[:100])
num = r'([1-9][0-9]*[02468]|[02468])'
pattern = rf'{num}(?:[*+]{num})+'
f = [x.group() for x in finditer(pattern, l)]
k_max = max(f, key=len)
print(k_max, len(k_max))