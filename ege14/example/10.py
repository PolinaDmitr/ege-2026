from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

def f(x_, p_):
    s = ''
    while x_ != 0:
        s = alphabet[x_ % p_] + s
        x_ //= p_
    return s


for x in range(7290, 0, -1):
    numb = 27 ** 298 + 27 ** 269 - x
    s_numb = f(numb, 27)
    print(s_numb.count('0'))