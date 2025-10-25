from itertools import *

def f(t: tuple):
    for i in range(len(t) - 1):
        if t[i] % 2 != 0 and t[i + 1] % 2 != 0:
            return False
    return True

numb = 0
for i in product(range(9), repeat=6):
    if i[0] != 0:
        numb += 1
        if f(i) and numb % 10 == 5:
            print(i, numb)


