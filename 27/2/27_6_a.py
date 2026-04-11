from math import dist

def anti_cent_cl(cl):
    anti_cent = None
    max_d = 0
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

for i in file.readlines():
    x, y = map(float, i.split())
    if y > 10:
        cl1.append((x, y))
    elif x > 25:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

an_c1 = anti_cent_cl(cl1)
an_c2 = anti_cent_cl(cl2)
an_c3 = anti_cent_cl(cl3)
anti_centers = [an_c1, an_c2, an_c3]

all_point = cl1 + cl2 + cl3
max_ant = 0
ret = None
for p in all_point:
    sum_d = sum([dist(p, p1) for p1 in anti_centers])
    if sum_d > max_ant:
        max_ant = sum_d
        ret = p

print(ret[0] * 10000)
print(ret[1] * 10000)




