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



file = open('27var03B.txt')
cl1 = []
cl2 = []
cl3 = []

for line in file.readlines():
    x, y = map(float, line.split())
    if x < 8 or x > 25:
        continue
    if x < 15:
        cl1.append((x, y))
    elif y > 10:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

cent1 = f(cl1)
cent2 = f(cl2)
cent3 = f(cl3)

cents = [cent1, cent2, cent3]
print(cents)
max_c = 0
min_c = 1000000

for i in range(3):
    for j in range(i + 1, 3):
        d = dist(cents[i], cents[j])
        if d > max_c:
            max_c = d
        if d < min_c:
            min_c = d

print(min_c * 10_000)
print(max_c * 10_000)