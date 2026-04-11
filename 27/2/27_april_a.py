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


file = open('27_A_28766.txt')
cl1 = []
cl2 = []
red = []
for p in file.readlines():
    l = p.split()
    x = float(l[0].replace(',', '.'))
    y = float(l[1].replace(',', '.'))
    spec = l[2]
    if y > 8:
        cl1.append((x, y))
    else:
        cl2.append((x, y))
    if spec[0] == 'Y' and spec[-3:] == 'III':
        red.append((x, y, spec))

print(red)
cl_min = min(cl1, cl2, key=len)
cent = cent_cl(cl_min)
dist_red = [dist(cent, (r[0], r[1])) for r in red]
print(min(dist_red) * 10000)
print(max(dist_red) * 10000)

