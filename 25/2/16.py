from re import *
from itertools import *

reg = r'^20[13579][13579]22[02468]*$'

start = 201122 // 10980 * 10980

for i in range(start, 10 ** 10, 10980):
    if len(findall(reg, str(i))):
        print(i, i // 10980)

# 20@@22#

l = []
for k in range(5):
    for a1 in '13579':
        for a2 in '13579':
            for a in product('02468', repeat=k):
                a3 = ''.join(a)
                numb = int(f'20{a1}{a2}22{a3}')
                if numb % 10980 == 0:
                    l.append(numb)
l.sort()
print()
for i in range(5):
    print(l[i], l[i] // 10980)


