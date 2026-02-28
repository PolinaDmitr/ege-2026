# 987654321
def f(x):
    d = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if x > 1:
        d.append(x)
    return d


counter = 0
for i in range(987_654_321, 1, -1):
    d = f(i)
    if len(d) == 13 and '1' in str(sum(d)):
        print(i, max(d))
        counter += 1
    if counter == 5:
        break