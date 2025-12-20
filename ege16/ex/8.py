# F(n)=F(n−4)+3580, если n≥19;
# F(n)=6×(G(n−7)−36), если n<19;
# G(n)=n/20+28, если n≥248045;
# G(n)=G(n+9)−4, если n<248045.
from functools import lru_cache

@lru_cache(maxsize=None)
def g(n):
    if n >= 248_045:
        return n / 20 + 28
    return g(n + 9) - 4

@lru_cache(maxsize=None)
def f(n):
    if n < 19:
        return 6 * (g(n - 7) - 36)
    return f(n - 4) + 3580

for i in range(248045, 0, -1):
    g(i)

print(f(673))


