# ( ¬ДЕЛ(x, 3) ∧ x ∉ {48, 52, 56} ) → (( |x – 50| ⩽ 7) → ( x in Q )) ∨ (x & A = 0)
# Q=[29;47]

def f(x, a):
    return ((x % 3 != 0) and (x not in (48, 52, 56))) <= (((abs(x - 50) <= 7) <= (29 <= x <= 47)) or (x & a == 0))


for a in range(1, 300):
    if all(f(x, a) for x in range(1, 500)):
        print(a)
        break