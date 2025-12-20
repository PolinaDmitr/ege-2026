# F(n)=13 при n<13;
# F(n)=13−F(n−1), если n⩾13 и значение n не кратно 5;
# F(n)=13+F(n−1), если n⩾13 и значение n кратно 5
from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n < 13:
        return 13
    if n % 5 == 0:
        return 13 + f(n - 1)
    return 13 - f(n - 1)


for i in range(13, 3013):
    f(i)

print(f(3013))