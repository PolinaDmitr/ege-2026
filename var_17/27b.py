from math import dist

def cent_cl(cl):
    cent = None
    min_d = 10 ** 10
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_d:
            min_d = sum_d
            cent = p
    return cent


def radian(cl):
    cent = cent_cl(cl)
    rad = 0
    for p in cl:
        d = dist(p, cent)
        if d > rad:
            rad = d
    return rad

file = open('27-76b.txt')

cl1 = []
cl2 = []
cl3 = []
cl4 = []

for i in file.readlines():
    x, y = map(float, i.replace(',', '.').split())
    if y < 1.25 * x:
        if y < -x + 8:
            cl1.append((x, y))
        else:
            cl2.append((x, y))
    else:
        if y < -1.6 * x + 10:
            cl3.append((x, y))
        else:
            cl4.append((x, y))


r1 = radian(cl1)
r2 = radian(cl2)
r3 = radian(cl3)
r4 = radian(cl4)

print(r1, r2, r3, r4)
print((r1 + r2 + r3 + r4)/4 * 10_000)