import sys
from functools import lru_cache
# sys.setrecursionlimit(1002)

m = {}

def f1(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

def f2(n):
    if n <= 1:
        return 1
    if n in m:
        return m[n]
    result = n * f2(n - 1)
    m[n] = result
    return result

@lru_cache(maxsize=None)
def f3(n):
    if n <= 1:
        return 1
    return n * f2(n - 1)


print(f1(1000))
for i in range(1, 1000):
    f2(i)
print(f2(1000))
for i in range(1, 1000):
    f3(i)
print(f3(1000))

l = [0] * 1001
l[1] = 1
for i in range(2, 1000 + 1):
    l[i] = l[i - 1] + i
print(l)
print(l[1000])