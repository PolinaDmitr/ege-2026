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


cl1 = []
cl2 = []
cl3 = []

file = open('27_10_b.txt')
for point in file.readlines():
    x, y = map(float, point.replace(',', '.').split())
    if -10 < x < 0 or 11 < x < 17.5:
        continue
    if x > 18:
        cl1.append((x, y))
    elif x < -30:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

cent1 = cent_cl(cl1)
cent2 = cent_cl(cl2)
cent3 = cent_cl(cl3)

cl1.remove(cent1)

cent1_2 = cent_cl(cl1)
cent2_2 = cent_cl([x for x in cl2 if x != cent2])
cent3_2 = cent_cl([x for x in cl3 if x != cent3])

print(abs(cent1_2[0] + cent2_2[0] + cent3_2[0]) * 10000)
print(abs(cent1_2[1] + cent2_2[1] + cent3_2[1]) * 10000)
