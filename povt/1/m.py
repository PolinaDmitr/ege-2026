from math import pi

s = pi * 4 * 173110000 ** 2
need = (s // 100  + 1) * 8
print(need / (10 ** 12 * 8))

a = pi * 173110000 // 10 + 1
b = 2 * pi * 173110000 // 10 + 1
print(a * b * 8, need)
print(a * b * 8 / (10 ** 12 * 8))