from re import *

l =  open('24_13.txt').readline()
print(l[:100])
pattern = r'[1-9][0-9]*[02468](?:[*+][1-9][0-9]*[02468])*'
f = findall(pattern, l)
print(f[:100])