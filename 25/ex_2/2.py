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
for i in range(123_456_789, 923456789):
    d = f(i)
    if len(d) == 7 and '5' in str(sum(d)) and max(d) % 10 == 9:
        print(i, max(d))
        counter += 1
    if counter == 5:
        break