from math import dist


def cent_cl(cl):
    cent = None
    min_dist = 10 ** 10
    for p in cl:
        sum_d = sum([dist((p[0], p[1]), (p1[0], p1[1])) for p1 in cl])
        if sum_d < min_dist:
            cent = p
            min_dist = sum_d
    return cent

cl1 = []
cl2 = []

red_star = []

file = open('27_A_28766.txt')
for i in file.readlines():
    l = i.split()
    x, y = float(l[0].replace(',', '.')), float(l[1].replace(',', '.'))
    name = l[2]
    if y > 10:
        cl1.append((x, y, name))
    else:
        cl2.append((x, y, name))
    if name[0] == 'Y' and name[-3:] == 'III':
        red_star.append((x, y, name))

print(cl1[:10])
print(cl2[:10])
print(red_star)

cl_min = min(cl1, cl2, key=len)

cent = cent_cl(cl_min)

dists = [dist((cent[0], cent[1]), (p[0], p[1])) for p in red_star]
print(min(dists) * 10_000)
print(max(dists) * 10_000)