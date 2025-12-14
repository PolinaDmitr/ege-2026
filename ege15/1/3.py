#(x < A) ∧ (y < 3A) ∨ (2x + y > 128)
def f(x_, y_, a_):
    return (x_ < a_) and (y_ < 3 * a_) or (2 * x_ + y_ > 128)

for a in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        for y in range(1, 10000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break

    if flag:
        print(a)
        break

for a in range(1, 100):
    if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)):
        print(a)
        break
