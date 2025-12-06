from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

# def f(x_, p_):
#     s = ''
#     while x_ != 0:
#         s = alphabet[x_ % p_] + s
#         x_ //= p_
#     return s

def f(s_, p_):
    r = 0
    for i in range(len(s_)):
        r += alphabet.find(s_[i]) * p_ ** (len(s_) - i - 1)
    return r


# print(int('KOT', 33))
# print(f('KOT', 33))
for p in range(33, 100):
    num1 = f('KOT', p) + f('GOLODNI', p)
    num2 = f('MEEOW', p) * f('100', p) - 20194023088
    if num1 == num2:
        print(p, f('PURR', p))
        break