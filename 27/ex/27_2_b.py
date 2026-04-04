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


file = open('27var07B.txt')
cl1 = []
cl2 = []
cl3 = []

for line in file.readlines():
    x, y = map(float, line.split())
    if x < 11 or x > 30:
        continue
    if x > 20:
        cl1.append((x, y))
    elif y < 12:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

print(min(len(cl1), len(cl2), len(cl3)))
print(max(len(cl1), len(cl2), len(cl3)))