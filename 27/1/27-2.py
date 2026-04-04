from math import dist

def cent_cl(cl):
    cent = None
    max_d = 0
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d > max_d:
            max_d = sum_d
            cent = p
    return cent


fileA = open('27_2_a.txt')
cl1 = []
cl2 = []

for line in fileA.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if y < 8:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cl_min = min(cl1, cl2, key=len)
cl_max = max(cl1, cl2, key=len)

anti_cent1 = cent_cl(cl_min)
anti_cent2 = cent_cl(cl_max)

print(abs(anti_cent1[0] + anti_cent1[1]) * 10_000)
print(abs(anti_cent2[0] + anti_cent2[1]) * 10_000)

fileB = open('27_2_b.txt')

cl1 = []
cl2 = []
cl3 = []

for line in fileB.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if y < 0 or x < 0 or x > 26:
        continue

    if x > 18:
        cl1.append((x, y))
    elif y > 20:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

cent1 = cent_cl(cl1)
cent2 = cent_cl(cl2)
cent3 = cent_cl(cl3)

print(dist(cent1, (0, 0)), dist(cent2, (0, 0)), dist(cent3, (0, 0)))
#1 - самый дальний
#3 - самый близкий

print(cent1[0] * 10000)
print(cent3[1] * 10000)