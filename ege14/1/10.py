from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase

def f(n_, a_):
    s = ''
    while n_ != 0:
        s = alphabet[n_ % a_] + s
        n_ //=a_
    return s


def f2(n_, a_):
    z = 0
    while n_ != 0:
        if n_ % a_ == 0:
            z += 1
        n_ //=a_
    return z


zero_max = 0
for x in range(7290, 0, -1):
    numb = 27 ** 298 + 27 ** 269 - x
    zero_max = max(zero_max, f(numb, 27).count('0'))
print(zero_max)

zero_max = 0
for x in range(7290, 0, -1):
    numb = 27 ** 298 + 27 ** 269 - x
    zero_max = max(zero_max, f2(numb, 27))
print(zero_max)
