from re import findall
from itertools import *


reg = r'^20[13579][13579]22[02468]*$'

counter = 0
start = 201122 // 10980 * 10980
for i in range(start, 10 ** 10, 10980):
    d = findall(reg, str(i))
    if len(d) > 0:
        print(i, i // 10980)
        counter += 1
    if counter == 5:
        break


for r in range(6):
    for a1 in '13579':
        for a2 in '13579':
            for a3 in product('02468', repeat=r):
                numb = int(f'20{a1}{a2}22{''.join(a3)}')
                if numb % 10980 == 0 and numb < 10 ** 10:
                    print(numb, numb / 10980)

