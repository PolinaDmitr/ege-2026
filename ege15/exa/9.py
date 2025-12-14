#(A+2x>400−A)∧(mod(A,100)+mod(120,A)>140)
def f(x):
    return (a + 2 * x > 400 - a) and (a % 100 + 120 % a > 140)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break