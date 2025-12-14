from itertools import *
from math import prod

def f(x):
    return ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))

p = {1,3,4,9,11,13,15,17,19,21}
q = {3,6,9,12,15,18,21,24,27,30}
a_lib = {1,3,4,9,11,13,15,17,19,21, 3,6,9,12,15,18,21,24,27,30}

for k in range(1, len(a_lib) + 1):
    for a in combinations(a_lib, k):
        if all(f(x) for x in range(40)):
            print(a, prod(a))