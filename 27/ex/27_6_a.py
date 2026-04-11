from math import dist

def anti_cent_cl(cl):
    max_d = 0
    anti_cent = None
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d > max_d:
            max_d = sum_d
            anti_cent = p
    return anti_cent


file = open('27_6_a.txt')
file.readline()
cl1 = []
cl2 = []
cl3 = []

for line in file.readlines():
    x, y = map(float, line.split())
    if y < 0:
        cl1.append((x, y))
    elif y > 10:
        cl2.append((x, y))
    else:
        cl3.append((x, y))


anti_centers = [anti_cent_cl(cl1), anti_cent_cl(cl2), anti_cent_cl(cl3)]
all_cl = cl1 + cl2 + cl3

retrans = None
max_d = 0
for p in all_cl:
    sum_d = sum(dist(p, p1) for p1 in anti_centers)
    if sum_d > max_d:
        max_d = sum_d
        retrans = p

print(retrans)
