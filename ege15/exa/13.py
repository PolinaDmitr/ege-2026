def f(x, y):
    a = 100 <= x <= 200
    b = 2 <= x < 121 and 121 % x == 0
    c = 2 <= x < y and y % x == 0
    return c <= (a and not b)

for y in range(1, 20000):
    if all(f(x, y) for x in range(1, 10000)) and any(y % x == 0 for x in range(2, y)):
        print(y)
        break