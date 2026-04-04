from math import dist

def cent_cl(cl):
    cent = None
    sum_min = 10 ** 20
    for point in cl:
        p_sum = sum([dist(point, point_1) for point_1 in cl])
        if p_sum < sum_min:
            sum_min = p_sum
            cent = point
    return cent


file = open('27_1_a.txt')
cl1 = []
cl2 = []

for line in file.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if x > 0:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cent1 = cent_cl(cl1)
cent2 = cent_cl(cl2)

print(abs(cent1[0] + cent2[0]) * 10_000)
print(abs(cent1[1] + cent2[1]) * 10_000)
