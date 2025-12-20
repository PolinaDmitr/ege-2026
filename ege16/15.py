# F(n)=1 при n=1;
# F(n)=2⋅n+F(n−1), если n>1.
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n <= 1:
        return 1
    return 2 * n + f(n - 1)


for i in range(1, 57693):
    f(i)

numb = f(57693)
sum_d = sum([int(x) for x in str(numb)])
print(sum_d ** 2)