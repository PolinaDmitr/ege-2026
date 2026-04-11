from math import dist

def cent_cl(cl):
    cent = None
    min_d = 10 ** 10
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_d:
            min_d = sum_d
            cent = p
    return cent

cl1 = []
cl2 = []
cl3 = []
y1 = []
y2 = []
y3 = []

file = open('27_B_28766.txt')
for p in file.readlines():
    l = p.replace(',', '.').split()
    x = float(l[0])
    y = float(l[1])
    spec = l[2]
    if x > 20:
        cl1.append((x, y))
        if spec[0] == 'Z' and spec[-1] == 'I' and len(spec) == 3:
            y1.append((x, y, spec))
    elif y > 22:
        cl2.append((x, y))
        if spec[0] == 'Z' and spec[-1] == 'I' and len(spec) == 3:
            y2.append((x, y, spec))
    else:
        cl3.append((x, y))
        if spec[0] == 'Z' and spec[-1] == 'I' and len(spec) == 3:
            y3.append((x, y, spec))

print(y1)
print(y2)
print(y3)

list_y = [y1, y2, y3]
dist_y = []
for ly in list_y:
    for i in range(len(ly) - 1):
        for j in range(i + 1, len(ly)):
            dist_y.append(dist((ly[i][0], ly[i][1]), (ly[j][0], ly[j][1])))
print(min(dist_y) * 10000)

#мы посмотрели, что маскимум в 1 кластере, а минимум в 3
cent1 = cent_cl(cl1)
cent3 = cent_cl(cl3)

print(dist(cent1, cent3) * 10000)

