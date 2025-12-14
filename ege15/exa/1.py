def f(x_, a_):
    return (x_ % 128 == 0) <= ((x_ % a_ != 0) <= (x_ % 80 != 0))

for a in range(1, 2000):
    if all(f(x, a) for x in range(1, 20000)):
        print(a)