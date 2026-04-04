from math import dist

def cent_cl(cl):
    cent = None
    min_d = 10 ** 15
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_d:
            min_d = sum_d
            cent = p
    return cent


file_a = open('27_3_a.txt')
cl1 = []
cl2 = []
for line in file_a.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if y < -30 or x < -10:
        continue

    if x > 0:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cent1 = cent_cl(cl1)
cent2 = cent_cl(cl2)

print((cent1[0] - cent2[0]) * 10_000)
print((cent1[1] - cent2[1]) * 10_000)

file_b = open('27_3_b.txt')
cl1 = []
cl2 = []
cl3 = []

for line in file_b.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if x < 0 or y < 0 or x > 36:
        continue

    if x > 22:
        cl1.append((x, y))
    elif y > 16:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

cent1 = cent_cl(cl1)
cent2 = cent_cl(cl2)
cent3 = cent_cl(cl3)

print((cent1[0] + cent2[0] + cent3[0]) / 3 * 10_000)
print((cent1[1] + cent2[1] + cent3[1]) / 3 * 10_000)