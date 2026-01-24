from math import *
def is_simple(n):
    if n == 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def f(a,m):
    if is_simple(a): return m % 2 == 0
    if m == 0: return 0
    h = [f(a * 2,m - 1),f(a + 3,m - 1),f(a + 1,m - 1)]
    return any(h) if m % 2 else all(h)


print('19)', min([i for i in range(1,102) if f(i,2) and not(f(i,0))])) #так как число изначально
#может оказаться простым и тогда победа на 0-м ходе зачтётся как победа на 2-м, то пишем not(f(i,0))
print('20)', *[i for i in range(1,102) if f(i,3) and (not f(i,1))][-2:])
print('21)', max([i for i in range(1,102) if f(i,4) and (not f(i,2)) and not(f(i,0))]))