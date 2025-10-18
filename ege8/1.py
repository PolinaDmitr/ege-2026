from itertools import *

l = []
for i in product('0123456', repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        s1 = s.replace('0', 'a').replace('2', 'a')\
        .replace('4', 'a').replace('6', 'a')
        if s1.count('aa') >= 2 and 'aaa' not in s1:
            l.append(s)
print(len(l))
print('kaaak', 'kaaak'.count('aa'))