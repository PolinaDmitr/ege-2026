#(A+2x>400−A) ∧ (mod(A,100) + mod(120,A) > 140)
def f(x_, a_):
    return (a_ + 2 * x_ > 400 - a_) and (a_ % 100 + 120 % a_ >140)


for a in range(1, 500):
    if all(f(x, a) for x in range(1, 5000)):
        print(a)
        break