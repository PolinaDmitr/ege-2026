from itertools import *

count = 0
for i in permutations('0123456789', 6):
    if i[0] != '0':
        s = ''.join(i)
        s_numb = int(s)
        if s_numb % 4 == 0:
            s1 = s.replace('0', 'a').replace('2', 'a').replace('4', 'a')\
            .replace('6', 'a').replace('8', 'a')
            if 'aa' not in s1:
                count += 1
print(count)