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

file = open('27var03A.txt')
cl1 = []
cl2 = []

for line in file.readlines():
    x, y = map(float, line.split())
    if x > 15:
        continue
    if y > 10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cent1 = f(cl1)
cent2 = f(cl2)

print(abs(cent1[0] - cent2[0]) * 10_000)
print(abs(cent1[1] - cent2[1]) * 10_000)
