#((x ∈ A) → (x ∈ P)) ∧ (¬(x ∈ Q) → ¬(x ∈ A))
#P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#Q = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 }
import math
from itertools import *


def f(p_, q_, a_, x_):
    return ((x_ in a_) <= (x_ in p_)) and ((x_ not in q_) <= (x_ not in a_))


p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
a_lib = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

for k in range(0, len(a_lib) + 1):
    for i in combinations(a_lib, k):
        if all(f(p, q, i, x) for x in range(40)):
            print(i, math.prod(i))
