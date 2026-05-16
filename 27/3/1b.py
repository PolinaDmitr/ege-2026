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


file = open('27-123b.txt')

cl1 = []
cl2 = []
cl3 = []

for i in file.readlines():
    l = i.replace(',', '.').split()
    x = float(l[0])
    y = float(l[1])
    type_star = l[2]
    if int(type_star[1]) >= 8:
        if x > 20:
            cl1.append((x, y))
        elif y < 22:
            cl2.append((x, y))
        else:
            cl3.append((x, y))

d_cl = []
cl = [cl1, cl2, cl3]
for i in range(3):
    for j in range(i + 1, 3):
        print(i, j)
        for p in cl[i]:
            for d in cl[j]:
                d_cl.append(dist(p, d))

print(min(d_cl) * 10000)

d2 = []
for i in cl:
    for p in i:
        for d in i:
            if p != d:
                d2.append(dist(p, d))

print(sum(d2) / len(d2) * 10000)

