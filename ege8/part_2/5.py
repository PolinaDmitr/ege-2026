from itertools import *

count = 0
for i in permutations('0123456789ABC', 7):
    if i[0] != '0':
        s = ''.join(i)
        s = s.replace('3', '1').replace('5', '1')\
        .replace('7', '1').replace('9', '1')
        if '1B' not in s and 'B1' not in s:
            count += 1
print(count)