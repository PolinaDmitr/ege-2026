# F(n)=n при n<10;
# F(n)=3n+F(n−3), если n≥10.
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n < 10:
        return n
    return 2 * n + f(n - 3)


for i in range(6250):
    f(i)

print((f(6250) + 2 * f(6244)) / f(6238))


