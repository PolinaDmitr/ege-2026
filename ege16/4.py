# G(n)=n, если n< 100.
# G(n)=F(n−3)+1, если n⩾ 100.
# F(n)=G(n−2)

# G(n)=n, если n< 100.
# G(n)=G(n−5)+1, если n⩾ 100.
# F(n)=G(n−2)
from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    return g(n - 2)


@lru_cache(maxsize=None)
def g(n):
    if n < 100:
        return n
    return f(n - 3) + 1

@lru_cache(maxsize=None)
def g2(n):
    if n < 100:
        return n
    return g(n - 5) + 1


for i in range(99, 5000):
    g(i)
    g2(i)

print(f(5000))
print(g2(5000 - 2))