def f(x):
    delit = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            delit.append(i)
            x //= i
        i += 1
    if x > 1:
        delit.append(x)
    return delit

counter = 0
for i in range(987_654_321, 1, -1):
    d = f(i)
    if len(d) == 13 and '1' in str(sum(d)):
        print(i, max(d))
        counter += 1
    if counter == 5:
        break

counter = 0
start = int(987_654_321 ** 0.5)
for i in range(start, 1, -1):
    x = i ** 2
    d = f(x)
    if len(d) == 13 and '1' in str(sum(d)):
        print(x, max(d))
        counter += 1
    if counter == 5:
        break
