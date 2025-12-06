from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase

def f(s_, a_):
    res = 0
    step = len(s_) - 1
    for i in range(len(s_)):
        res += alphabet.find(s_[i]) * a_ ** (step - i)
    return res

#KOTp+GOLODNIp=MEEOWp∗100p−20194023088_10
for p in range(33, 100):
    numb1 = f('KOT', p) + f('GOLODNI', p)
    numb2 = f('MEEOW', p) * f('100', p) - 20194023088
    if numb1 == numb2:
        print(p, f('PURR', p))
        break