from math import dist

def cent_cl(cl):
    cent = None
    min_dist = 10 ** 10
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_dist:
            cent = p
            min_dist = sum_d
    return cent

cl1 = []
star_yellow_1 = []
cl2 = []
star_yellow_2 = []
cl3 = []
star_yellow_3 = []

file = open('27_B_28766.txt')
for i in file.readlines():
    l = i.split()
    x = float(l[0].replace(',', '.'))
    y = float(l[1].replace(',', '.'))
    classification = l[2]
    if y > 21:
        cl1.append((x, y))
        if classification[0] == 'Z' and classification[-1] == 'I' and len(classification) == 3:
            star_yellow_1.append((x, y, classification))
    elif x > 20:
        cl2.append((x, y))
        if classification[0] == 'Z' and classification[-1] == 'I' and len(classification) == 3:
            star_yellow_2.append((x, y, classification))
    else:
        cl3.append((x, y))
        if classification[0] == 'Z' and classification[-1] == 'I' and len(classification) == 3:
            star_yellow_3.append((x, y, classification))


stars_y = [star_yellow_1, star_yellow_2, star_yellow_3]
y_dist = []

for y_cl in stars_y:
    for i in range(len(y_cl) - 1):
        for j in range(i + 1, len(y_cl)):
            y_dist.append(dist((y_cl[i][0], y_cl[i][1]), (y_cl[j][0], y_cl[j][1])))
print(min(y_dist) * 10_000)
print(len(star_yellow_1), len(star_yellow_2), len(star_yellow_3))

print(dist(cent_cl(cl2), cent_cl(cl3)) * 10_000)
