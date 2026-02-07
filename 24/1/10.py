from re import *

line = open('24_10_re.txt').readline()
pattern = '[1-9ABCD][0-9ABCD]*[02468AC]'
f = findall(pattern, line)
k = max(f, key=lambda x: int(x, 14))
print(len(k))