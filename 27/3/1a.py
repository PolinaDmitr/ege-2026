from math import dist

def cent(cl):
    cent = None
    min_d = 10 ** 10
    for p in cl:
        d = sum([dist(p, p1) for p1 in cl])
        if d < min_d:
            cent = p
            min_d = d
    return cent


file = open('27-123a.txt')

cl1 = []
cl2 = []

kvaz1 = []
kvaz2 = []

for i in file.readlines():
    l = i.replace(',', '.').split()
    x = float(l[0])
    y = float(l[1])
    type_star = l[2]

    if y > 10:
        cl1.append((x, y))
        if len(type_star) >= 3 and 'VII' in type_star:
            kvaz1.append((x, y))
    else:
        cl2.append((x, y))
        if len(type_star) >= 3 and 'VII' in type_star:
            kvaz2.append((x, y))

cent1 = cent(cl1)
cent2 = cent(cl2)

kvaz_d = []
for i in kvaz1:
    kvaz_d.append(dist(i, cent1))
for i in kvaz2:
    kvaz_d.append(dist(i, cent2))

print(abs(min(kvaz_d)) * 10_000)
print(abs(max(kvaz_d)) * 10_000)


