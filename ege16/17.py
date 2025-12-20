# F(n)=n, при n≥3000
# F(n)=n+x+F(n+2), при n<3000
# При каком целом значении х, значение
# выражения F(2984)−F(2988)=5916
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n, x):
    if n >= 3000:
        return n
    return n + x + f(n + 2, x)

for x in range(-100, 100):
    for i in range(3000, 2980, -1):
        f(i, x)
    if f(2984, x) - f(2988, x) == 5916:
        print(x)
