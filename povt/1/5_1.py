from itertools import *


def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def f(n):
    l = []
    for i in permutations(str(n), r=2):
        if i[0] != '0':
            l.append(int(''.join(i)))
    return l


count_max = 0
n_max = 0

for n in range(100, 1000):
    dig = f(n)
    simple_dig = [x for x in dig if simple(x)]
    if len(simple_dig) >= count_max:
        n_max = n
        count_max = len(simple_dig)

print(n_max)