def f(x_, y_, a_):
    return (x_ < a_) and (y_ < 3 * a_) or (2 * x_ + y_ > 128)

for a in range(1, 500):
    if all(f(x, y, a) for x in range(1, 500) for y in range(1, 500)):
        print(a)
        break