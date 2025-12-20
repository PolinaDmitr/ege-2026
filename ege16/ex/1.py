# import sys
#
# sys.setrecursionlimit(1100)
m = {}

def f(n):
    if n in m:
        return m[n]
    if n == 1:
        return n
    result = n + f(n - 1)
    m[n] = result
    return result

for i in range(1, 999):
    f(i)

print(f(1000))