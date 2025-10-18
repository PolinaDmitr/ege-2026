from itertools import *

c = set()
for i in permutations('ПАРИЖАНКА'):
    s = ''.join(i)
    s1 = s.replace('И', 'А')
    if s1.count('АА') == 1 and 'ААА' not in s1:
        c.add(s)
print(c, len(c))