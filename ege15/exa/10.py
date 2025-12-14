from itertools import *

def f(x):
    return ((x in a) <= (x in p)) and ((x not in q) <= (x not in a))

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30 }
a_lib = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

for k in range(1, len(a_lib) + 1):
    for a in combinations(a_lib, k):
        if all(f(x) for x in range(40)):
            print(a)
