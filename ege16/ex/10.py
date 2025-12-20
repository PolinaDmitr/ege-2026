from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1
    return 2 * n + f(n - 1)

for i in range(1, 58_000):
    f(i)

numb = f(57693)
sum_numb = sum([int(x) for x in str(numb)])
print(sum_numb ** 2)