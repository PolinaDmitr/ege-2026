from math import dist

def d_cl(cl):
    cent = (-1000, -1000)
    min_dist = 10 ** 10
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_dist:
            min_dist = sum_d
            cent = p
    return cent


fileA = open('27A_1.txt')
clA1 = []
clA2 = []

for line in fileA.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if x < 0:
        clA1.append((x, y))
    else:
        clA2.append((x, y))

centA1 = d_cl(clA1)
centA2 = d_cl(clA2)

print(centA1, centA2)
print((centA1[0] + centA2[0]) * 10_000)
print((centA1[1] + centA2[1]) * 10_000)

fileB = open('27B_1.txt')
clB1 = []
clB2 = []
clB3 = []

for line in fileB.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if -10 < y < 10:
        continue
    if x < 0:
        clB1.append((x, y))
    elif y > 10:
        clB2.append((x, y))
    else:
        clB3.append((x, y))


cl_min = min(clB1, clB2, clB3, key=len)
cl_max = max(clB1, clB2, clB3, key=len)

cl_max_x = max([x[0] for x in cl_max])
cl_min_y = max([y[1] for y in cl_min])

print(cl_max_x * 10000)
print(cl_min_y * 10000)