#(x∈C)→((x∈A)∧(x∉B))
def f(x_, y_):
    a = 100 <= x_ <= 200
    b = (1 < x_ < 121) and (121 % x_ == 0)
    c = (1 < x_ < y_) and (y_ % x_ == 0)
    return c <= (a and (not b))


for y in range(1, 15000):
    if any(y % x == 0 for x in range(2, y)) \
            and all(f(x, y) for x in range(-1000, 20000)):
        print(y)
        break