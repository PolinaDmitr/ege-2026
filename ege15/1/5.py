#(x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))
#P = [25; 64] и Q = [40; 115]
def f(x_, a1_, a2_):
    return (25 <= x_ <= 64) <= (((40 <= x_ <= 115) and
            (not (a1_ <= x_ <= a2_))) <= (not (25 <= x_ <= 64)))

def f2(x_, a1_, a2_):
    p = 25 <= x_ <= 64
    q = 40 <= x_ <= 115
    a = a1_ <= x_ <= a2_
    return p <= ((q and (not a)) <= (not p))

l = []
for a1 in range(20, 120):
    for a2 in range(a1 + 1, 121):
        if all(f(x, a1, a2) for x in range(150)):
            l.append(a2 - a1)
            print(a2, a1, a2 - a1)
print(min(l))