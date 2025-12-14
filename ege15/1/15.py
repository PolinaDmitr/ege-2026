#НОД(A, 420, 2) \/ (¬НОД(A, x, 12) → ¬НОД(110, x, 11))
from math import gcd, lcm

def f(x_, a_):
    return (gcd(a_, 420) == 2) or ((gcd(a_, x_) != 12) <= gcd(110, x_) != 11)


l = []
for a in range(1, 1001):
    if all(f(x, a) for x in range(1, 5000)):
        l.append(a)
print(len(l))