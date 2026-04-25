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

file = open('27-76a.txt')
cl1 = []
cl2 = []

for i in file.readlines():
    x, y = map(float, i.replace(',', '.').split())
    if x > 4:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

r1 = radian(cl1)
r2 = radian(cl2)

print((r1 + r1) / 2 * 10000)

