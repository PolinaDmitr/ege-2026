from math import dist

def f(cl):
    cent = (0, 0)
    min_d = 1000000
    for p in cl:
        d = sum(dist(p, p1) for p1 in cl)
        if d < min_d:
            min_d = d
            cent = p
    return cent


file = open('27var07A.txt')
cl1 = []
cl2 = []

for line in file.readlines():
    x, y = map(float, line.split())
    if x < 0 or y < 0:
        continue
    if y > 14:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cent_cl1 = f(cl1)
cent_cl2 = f(cl2)

print(max(cent_cl1[0], cent_cl2[0]) * 10_000)
print(max(cent_cl1[1], cent_cl2[1]) * 10_000)